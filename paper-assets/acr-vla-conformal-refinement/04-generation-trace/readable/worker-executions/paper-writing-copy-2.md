# paper writing

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_20260515T191259.log`
- **Structured JSON:** [`a7fefd9038635d9c857f.json`](../../sessions/a7/a7fefd9038635d9c857f.json)

## Before a recorded user message

28 recorded events

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
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
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
  "uuid": "fff5e1aa-1413-45d0-a3e9-e7629920a981",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Assistant

_source line 3_

I'll read the LaTeX writing skill first, then write the method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "d1088cf5-4f8b-4fc1-92b3-a48bcf0174cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeZmpBAFi1smttE8tQAEeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13103,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13103
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

_source line 4_

<details open><summary>🔧 Tool call — Read · `toolu_012ekbodKkmdzV6s1FUTQasE`</summary>

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
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "e4e09ded-c9eb-49b5-9afb-c270659f2524",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeZmpBAFi1smttE8tQAEeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13103,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13103
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

### Runtime record

_source line 5_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778886600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4655a087-fa0b-4136-9a8a-f5e952c88afd",
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c"
}
```

---

### Tool result

_source line 6 · 2026-05-15T19:13:13.945Z_

<details><summary>↩ Tool result · `toolu_012ekbodKkmdzV6s1FUTQasE`</summary>

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
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "7f1d67c6-4887-4d0d-900f-8a007d6d6237",
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

<details open><summary>🔧 Tool call — Bash · `toolu_019wF5NkUDZKd9QhkpZzFK3p`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/ 2>/dev/null",
  "description": "Check existing paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "d72fc793-3b82-4510-83a2-ec89c5752b0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TeZmpBAFi1smttE8tQAEeM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13103,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13103
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

_source line 8 · 2026-05-15T19:13:14.970Z_

<details><summary>↩ Tool result · `toolu_019wF5NkUDZKd9QhkpZzFK3p`</summary>

```text
corl_paper_outline.md
experiments.tex
experiments_c64a8c.tex
introduction.tex
introduction_c83872.tex
method_section_draft.tex
references.bib
references_e9d4d2.bib
related_work.tex
related_work_9c2927.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "4441ffc7-7b15-4184-abe8-d644ee47216b",
  "tool_use_result": {
    "stdout": "corl_paper_outline.md\nexperiments.tex\nexperiments_c64a8c.tex\nintroduction.tex\nintroduction_c83872.tex\nmethod_section_draft.tex\nreferences.bib\nreferences_e9d4d2.bib\nrelated_work.tex\nrelated_work_9c2927.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me look at the existing method section draft and any other relevant files for context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "2cde56a8-5a0b-495e-b745-18289c2716f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhpTiDvcpdcLUrvpcVNJxc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5758,
      "cache_read_input_tokens": 24944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5758
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

_source line 10_

Let me check the existing draft and the paper outline for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "8e346400-230d-4695-ac79-27700b1223a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhpTiDvcpdcLUrvpcVNJxc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5758,
      "cache_read_input_tokens": 24944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5758
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01Qv5cPBLd7NMJk9dr4QXgMo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_section_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "8f9d1f05-0430-4b9c-a808-0d3c47c36621",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhpTiDvcpdcLUrvpcVNJxc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5758,
      "cache_read_input_tokens": 24944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5758
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_018gnz9JyoCTiucYahaHBiqz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/corl_paper_outline.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "499b7f49-d196-47c9-9f1a-6d309225156b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MhpTiDvcpdcLUrvpcVNJxc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5758,
      "cache_read_input_tokens": 24944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5758
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

_source line 13 · 2026-05-15T19:13:20.754Z_

<details><summary>↩ Tool result · `toolu_01Qv5cPBLd7NMJk9dr4QXgMo`</summary>

```text
1	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
2	%% Section 3 -- Motivating Experiment
3	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
4	
5	\section{Motivating Experiment}
6	\label{sec:motivating}
7	
8	Before committing to the full \textbf{ACR-VLA} pipeline, we ask a targeted question: \emph{does per-DOF uncertainty carry more actionable information for correction than a scalar summary?}  We design a controlled 3D point-reaching experiment that isolates this factor.
9	
10	\paragraph{Setup.}
11	A synthetic policy outputs actions $a\in\mathbb{R}^{3}$ with known anisotropic Gaussian noise: $\sigma_x{=}0.5,\;\sigma_y{=}0.1,\;\sigma_z{=}0.1$, simulating the depth ambiguity a monocular camera introduces along the $x$-axis.  At test time a target shift of $+0.3$ is applied along $x$, creating a systematic perturbation whose correction should be modulated by uncertainty structure.
12	
13	We train three correction MLPs (2 layers, hidden dim 64, 20{,}000 training samples), differing only in their uncertainty conditioning:
14	\begin{itemize}[nosep]
15	  \item \textbf{Model A} (scalar): conditioned on the average standard deviation $\bar{\sigma}=\tfrac{1}{3}\sum_j\sigma_j$.
16	  \item \textbf{Model B} (per-DOF): conditioned on the full vector $[\sigma_x,\sigma_y,\sigma_z]$.
17	  \item \textbf{Model C} (none): conditioned on observation features only, with no uncertainty input.
18	\end{itemize}
19	To match the regime of our full pipeline, where ground-truth variances are unavailable, we report results with \emph{estimated} uncertainty computed from $K{=}10$ samples (the same budget used in \textbf{ACR-VLA}).
20	
21	\paragraph{Results.}
22	Table~\ref{tab:motivating} reports per-axis MSE over 5{,}000 test episodes at a 5:1 anisotropy ratio ($\sigma_x/\sigma_y$) with $K{=}10$ estimated uncertainty.
23	
24	\begin{table}[t]
25	\centering
26	\caption{Per-axis MSE ($\downarrow$) of correction models on the 3D point-reaching task (5:1 anisotropy, $K{=}10$ estimated uncertainty). Model~B, which receives per-DOF uncertainty, preserves accuracy on the low-uncertainty axes ($y,z$) where Model~A and~C over-correct.}
27	\label{tab:motivating}
28	\small
29	\begin{tabular}{lccccc}
30	\toprule
31	Model & Conditioning & MSE$_x$ & MSE$_y$ & MSE$_z$ & Total MSE \\
32	\midrule
33	A & scalar $\bar\sigma$ & 0.1874 & 0.0247 & 0.0243 & 0.0788 \\
34	\textbf{B} & \textbf{per-DOF} $[\sigma_x,\sigma_y,\sigma_z]$ & \textbf{0.1829} & \textbf{0.0191} & \textbf{0.0185} & \textbf{0.0735} \\
35	C & none & 0.2151 & 0.0250 & 0.0246 & 0.0882 \\
36	\bottomrule
37	\end{tabular}
38	\end{table}
39	
40	Model~B reduces total MSE by 6.7\% relative to~A and by 16.7\% relative to~C.  The gains concentrate on the non-perturbed axes: $y$- and $z$-axis MSE drop by 22.7\% and 23.9\% versus~A, indicating that Model~B learns to leave low-uncertainty dimensions largely untouched while directing correction effort toward the high-uncertainty $x$-axis.  Model~A, receiving only a scalar average, lacks the information to make this distinction and applies a uniform correction that degrades the already-accurate axes.
41	
42	With oracle (ground-truth) variances, the ranking $\text{B}>\text{A}>\text{C}$ is preserved with larger margins (non-perturbed axis improvements of 30--38\% over~A).  Moving from oracle to $K{=}10$ estimation reduces relative gains by roughly 15 percentage points, reflecting finite-sample noise, but does not alter the ordering.  The pattern also holds at weaker anisotropy ratios (2:1 and 1.5:1): across all six conditions tested, Model~B consistently outperforms both baselines.
43	
44	\paragraph{Takeaway.}
45	Even a simple MLP can exploit per-DOF uncertainty structure for dimension-selective correction---a capability that scalar summaries cannot provide.  This motivates the design of \textbf{ACR-VLA}, which extracts rich per-DOF features from a flow-matching VLA and feeds them into a learned correction module (Section~\ref{sec:method}).
46	
47	
48	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
49	%% Section 4 -- Method
50	%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
51	
52	\section{Method}
53	\label{sec:method}
54	
55	\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA) is an inference-time, post-hoc module that attaches to any flow-matching VLA without modifying its weights.  It comprises three components (Figure~\ref{fig:pipeline}):
56	\begin{enumerate}[nosep]
57	  \item \textbf{Conformalized Gaussian Scoring} (CGS, \S\ref{sec:cgs}): draws $K{=}10$ action samples per step, fits a shrinkage-regularized Gaussian, and extracts a 40-dimensional structured uncertainty feature.
58	  \item \textbf{Adaptive Conformal Inference with Chunk Overlap Consistency} (ACI+COC, \S\ref{sec:aci}): maintains an online conformal threshold that adapts to distribution shift using a self-referential coverage signal from overlapping action chunks.
59	  \item \textbf{Conformal Refinement Module} (CRM, \S\ref{sec:crm}): a lightweight MLP that takes the CGS features as conditioning and outputs a dimension-selective residual correction.
60	\end{enumerate}
61	
62	We instantiate \textbf{ACR-VLA} on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that predicts action chunks of size 50 with action dimension $d{=}6$ (3 translation + 3 rotation; the gripper is handled separately outside the conformal pipeline).
63	
64	
65	%%% 4.1 CGS %%%
66	\subsection{Conformalized Gaussian Scoring}
67	\label{sec:cgs}
68	
69	CGS converts a set of stochastic action samples from the base VLA into a compact uncertainty descriptor that captures \emph{which} degrees of freedom are uncertain and \emph{how} they co-vary---information that a scalar nonconformity score discards.
70	
71	\paragraph{Sampling and truncation.}
72	At each control step, we draw $K{=}10$ action chunks from the frozen base VLA via independent flow-matching rollouts.  Although SmolVLA predicts 50-step chunks, under receding-horizon execution only the first few steps influence the robot before re-planning.  We therefore retain only the first $H{=}5$ steps, yielding $K$ samples $\{a_h^{(k)}\}_{k=1}^{K}$ with $a_h^{(k)}\in\mathbb{R}^{d}$ for each horizon step $h=1,\dots,H$.
73	
74	\paragraph{Shrinkage covariance estimation.}
75	For each step $h$, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well}:
76	\begin{equation}
77	  \boldsymbol{\Sigma}_h = (1-\alpha_{\mathrm{LW}})\,\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}} + \alpha_{\mathrm{LW}}\,\frac{\mathrm{tr}(\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}})}{d}\,\mathbf{I},
78	  \label{eq:shrinkage}
79	\end{equation}
80	where $\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}}$ is the empirical covariance and $\alpha_{\mathrm{LW}}$ is the analytically optimal shrinkage intensity.  With a dimension-to-sample ratio $p/n = d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\% estimation error due to the Marchenko--Pastur effect; shrinkage reduces this to below 5\%~\cite{ledoit2004well}.
81	
82	\paragraph{Mahalanobis nonconformity score.}
83	We define a joint multivariate nonconformity score:
84	\begin{equation}
85	  s_h(a) = (a - \boldsymbol{\mu}_h)^\top \boldsymbol{\Sigma}_h^{-1} (a - \boldsymbol{\mu}_h).
86	  \label{eq:mahal}
87	\end{equation}
88	This single score captures cross-DOF covariance structure.  In contrast, treating each DOF independently and applying Bonferroni correction across all $d{\times}H = 30$ marginals yields intervals that are substantially wider than necessary.  Our joint formulation requires Bonferroni correction only across $H{=}5$ horizon steps (target level $\alpha/H$ per step), preserving tight per-step regions~\cite{braun2025cgs}.
89	
90	\paragraph{CGS feature vector.}
91	We assemble a 40-dimensional feature $\boldsymbol{\varphi}_{\mathrm{CGS}}$ that is passed to the refinement module:
92	\begin{equation}
93	  \boldsymbol{\varphi}_{\mathrm{CGS}} = \bigl[\,\underbrace{\sigma_{j,h}}_{j=1..d,\;h=1..H}\;;\;\underbrace{q_h}_{h=1..H}\;;\;\underbrace{v_h}_{h=1..H}\,\bigr] \;\in\;\mathbb{R}^{40},
94	  \label{eq:cgs_feat}
95	\end{equation}
96	where $\sigma_{j,h} = \sqrt{(\boldsymbol{\Sigma}_h)_{jj}}$ is the per-DOF standard deviation (30D), $q_h$ is the ACI-calibrated Mahalanobis threshold at step $h$ (5D, see \S\ref{sec:aci}), and $v_h = \tfrac{1}{2}\log\det(\boldsymbol{\Sigma}_h)$ is the log-volume of the covariance ellipsoid (5D).  Together, these encode \emph{which dimensions are uncertain} (per-DOF std), the \emph{overall calibrated confidence level} (conformal radius), and the \emph{spread of the predictive distribution} (log-volume).  Compared with the scalar Euclidean distance used in ReconVLA~\cite{chen2026reconvla}, this representation captures substantially more structure.
97	
98	\paragraph{Relationship to single-pass uncertainty.}
99	Recent work~\cite{xing2026diu} shows that for flow-matching models the divergence of the velocity field recovers per-DOF aleatoric uncertainty from a single forward pass.  CGS instead estimates \emph{model uncertainty} via multi-sample covariance: a sampling-based signal that reflects both epistemic and aleatoric components, and that rises under distribution shift when the policy is uncertain about the correct action.  For action correction, this shift-sensitive signal is more actionable than a purely aleatoric estimate, since it identifies \emph{where the model needs help} rather than where the task is inherently ambiguous.  We validate this distinction empirically in ablation~A7.
100	
101	
102	%%% 4.2 ACI + COC %%%
103	\subsection{Adaptive Conformal Inference via Chunk Overlap Consistency}
104	\label{sec:aci}
105	
106	CGS requires a conformal threshold $q_h$ to convert Mahalanobis scores into calibrated prediction regions.  Static calibration on a held-out set, as in conformal quantile regression~\cite{romano2019cqr}, assumes exchangeability between calibration and deployment data---an assumption that breaks under the distribution shifts common in real-world manipulation.  We instead adopt Adaptive Conformal Inference (ACI)~\cite{gibbs2021aci}, which provides long-run coverage guarantees under arbitrary distribution shift, and equip it with a novel self-referential coverage signal.
107	
108	\paragraph{The coverage signal problem.}
109	ACI updates the miscoverage level $\alpha_t$ at each step based on whether the true action falls inside the conformal region.  In robotics, the most direct signal would check whether the \emph{executed} action lies within the predicted region.  However, contact dynamics cause the achieved end-effector displacement to differ from the commanded action, corrupting this signal.
110	
111	\paragraph{Chunk Overlap Consistency (COC).}
112	We exploit the temporal overlap inherent in receding-horizon action chunking.  At control step $t$, the VLA predicts a chunk $[a_t^1,\dots,a_t^H]$ with associated conformal ellipsoids $\{C_t^h\}_{h=1}^H$ derived from the Mahalanobis score (\ref{eq:mahal}) and threshold $q_h$.  After executing $a_t^1$ and observing the new state $s_{t+1}$, we draw $K{=}10$ fresh samples and compute the new first-step mean $\boldsymbol{\mu}_{t+1}^1$.  The COC coverage indicator is:
113	\begin{equation}
114	  \mathrm{err}_t = \mathbb{1}\bigl[\boldsymbol{\mu}_{t+1}^1 \notin C_t^2\bigr],
115	  \label{eq:coc}
116	\end{equation}
117	i.e., we check whether the next step's predicted action falls within the \emph{previous} step's conformal region for the overlapping horizon position.
118	
119	COC has four properties that make it well-suited for online calibration:
120	(i)~it is self-referential, requiring no external supervisor or trained reward model;
121	(ii)~it compares prediction-to-prediction rather than prediction-to-execution, making it robust to contact dynamics;
122	(iii)~it directly measures calibration quality---whether the conformal regions are appropriately sized;
123	(iv)~it produces a signal at every control step, not only at episode boundaries.
124	
125	\paragraph{Online update rule.}
126	The ACI update follows \cite{gibbs2021aci}:
127	\begin{equation}
128	  \alpha_{t+1} = \alpha_t + \gamma\bigl(\alpha_{\mathrm{target}} - \mathrm{err}_t\bigr),
129	  \label{eq:aci_update}
130	\end{equation}
131	where $\gamma$ is the learning rate and $\alpha_{\mathrm{target}}$ is the desired miscoverage rate.  When $\mathrm{err}_t{=}1$ (the region failed to cover), $\alpha_{t+1}$ decreases, widening the next region; when $\mathrm{err}_t{=}0$, $\alpha_{t+1}$ increases, tightening it.  Within each episode, we apply exponentially weighted conformal prediction~\cite{barber2023conformal} with decay parameter $\rho$ to down-weight stale calibration data.  Across episodes, the fraction of intra-episode COC hits serves as $\mathrm{err}_t$ for a cross-episode ACI update, enabling the threshold to adapt over the course of deployment.
132	
133	
134	%%% 4.3 CRM %%%
135	\subsection{Conformal Refinement Module}
136	\label{sec:crm}
137	
138	The Conformal Refinement Module (CRM) is a lightweight network that performs dimension-selective action correction, conditioned on the structured uncertainty features from CGS.
139	
140	\paragraph{Architecture.}
141	CRM is a 2-layer MLP with hidden dimension 256 (${\sim}$337K parameters).  Its input concatenates three sources:
142	(i)~the frozen observation embedding $\mathbf{z}_{\mathrm{obs}}$ from the base VLA encoder,
143	(ii)~the 40D CGS feature $\boldsymbol{\varphi}_{\mathrm{CGS}}$, and
144	(iii)~the mean action $\boldsymbol{\mu} \in \mathbb{R}^{30}$ ($d{\times}H = 6{\times}5$).
145	The output is a residual correction $\boldsymbol{\delta} \in \mathbb{R}^{30}$, and the refined action is:
146	\begin{equation}
147	  \mathbf{a}^* = \boldsymbol{\mu} + \mathrm{CRM}(\mathbf{z}_{\mathrm{obs}},\;\boldsymbol{\varphi}_{\mathrm{CGS}},\;\boldsymbol{\mu}).
148	  \label{eq:crm}
149	\end{equation}
150	
151	\paragraph{Training.}
152	CRM is trained with a single objective:
153	\begin{equation}
154	  \mathcal{L} = \bigl\|\mathbf{a}^* - \mathbf{a}_{\mathrm{expert}}\bigr\|_2^2,
155	  \label{eq:crm_loss}
156	\end{equation}
157	on demonstration trajectories from LIBERO~\cite{liu2023libero} augmented with synthetic perturbations (camera shifts, sensor noise, robot-state perturbation, lighting and background variation).  During training, CGS features are computed online: for each augmented observation, we run $K{=}10$ forward passes through the frozen base VLA and extract $\boldsymbol{\varphi}_{\mathrm{CGS}}$.  This ensures CRM sees realistic uncertainty patterns that co-vary with the perturbation type---for instance, camera shifts produce elevated translational variance while leaving rotational variance largely unchanged.
158	
159	ACI operates exclusively at inference time: it adjusts the conformal threshold $q_h$, which enters CRM through the conformal-radius components of $\boldsymbol{\varphi}_{\mathrm{CGS}}$.  This decoupling of training and calibration eliminates the multi-objective conflicts that arise when calibration-aware losses compete with the primary correction objective in a small-capacity network~\cite{wang2025cploop}.
160	
161	\paragraph{Why per-DOF conditioning enables selective correction.}
162	To build intuition, consider a camera perturbation that introduces translational ambiguity in the $x$-$y$ plane while leaving $z$-translation and rotation well-determined.  A scalar nonconformity score (e.g., average Euclidean sample distance, as in \cite{chen2026reconvla}) compresses this into ``moderate uncertainty everywhere,'' providing no basis for selective correction.  The per-DOF structure in $\boldsymbol{\varphi}_{\mathrm{CGS}}$ instead reveals that $\sigma_{x},\sigma_{y} \gg \sigma_{z},\sigma_{\mathrm{rot}}$, enabling CRM to apply large corrections to the uncertain translational axes while preserving the base VLA's accurate rotational predictions.  Section~\ref{sec:motivating} validates this mechanism in a controlled setting; Section~\ref{sec:experiments} demonstrates it on real VLA tasks.
163	
164	\paragraph{Inference protocol.}
165	Each control step proceeds as: draw $K{=}10$ samples $\to$ compute CGS $\to$ apply CRM $\to$ execute the first action of the refined chunk $\to$ observe new state $\to$ draw $K{=}10$ fresh samples $\to$ compute COC (\ref{eq:coc}) $\to$ ACI update (\ref{eq:aci_update}).  The entire module adds ${\sim}$337K parameters and $K{=}10$ extra forward passes to the base VLA, with no retraining of the base model.
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "92a8e2b9-3c7b-4cb0-9722-df1342832a87",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_section_draft.tex",
      "content": "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%% Section 3 -- Motivating Experiment\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\section{Motivating Experiment}\n\\label{sec:motivating}\n\nBefore committing to the full \\textbf{ACR-VLA} pipeline, we ask a targeted question: \\emph{does per-DOF uncertainty carry more actionable information for correction than a scalar summary?}  We design a controlled 3D point-reaching experiment that isolates this factor.\n\n\\paragraph{Setup.}\nA synthetic policy outputs actions $a\\in\\mathbb{R}^{3}$ with known anisotropic Gaussian noise: $\\sigma_x{=}0.5,\\;\\sigma_y{=}0.1,\\;\\sigma_z{=}0.1$, simulating the depth ambiguity a monocular camera introduces along the $x$-axis.  At test time a target shift of $+0.3$ is applied along $x$, creating a systematic perturbation whose correction should be modulated by uncertainty structure.\n\nWe train three correction MLPs (2 layers, hidden dim 64, 20{,}000 training samples), differing only in their uncertainty conditioning:\n\\begin{itemize}[nosep]\n  \\item \\textbf{Model A} (scalar): conditioned on the average standard deviation $\\bar{\\sigma}=\\tfrac{1}{3}\\sum_j\\sigma_j$.\n  \\item \\textbf{Model B} (per-DOF): conditioned on the full vector $[\\sigma_x,\\sigma_y,\\sigma_z]$.\n  \\item \\textbf{Model C} (none): conditioned on observation features only, with no uncertainty input.\n\\end{itemize}\nTo match the regime of our full pipeline, where ground-truth variances are unavailable, we report results with \\emph{estimated} uncertainty computed from $K{=}10$ samples (the same budget used in \\textbf{ACR-VLA}).\n\n\\paragraph{Results.}\nTable~\\ref{tab:motivating} reports per-axis MSE over 5{,}000 test episodes at a 5:1 anisotropy ratio ($\\sigma_x/\\sigma_y$) with $K{=}10$ estimated uncertainty.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-axis MSE ($\\downarrow$) of correction models on the 3D point-reaching task (5:1 anisotropy, $K{=}10$ estimated uncertainty). Model~B, which receives per-DOF uncertainty, preserves accuracy on the low-uncertainty axes ($y,z$) where Model~A and~C over-correct.}\n\\label{tab:motivating}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Conditioning & MSE$_x$ & MSE$_y$ & MSE$_z$ & Total MSE \\\\\n\\midrule\nA & scalar $\\bar\\sigma$ & 0.1874 & 0.0247 & 0.0243 & 0.0788 \\\\\n\\textbf{B} & \\textbf{per-DOF} $[\\sigma_x,\\sigma_y,\\sigma_z]$ & \\textbf{0.1829} & \\textbf{0.0191} & \\textbf{0.0185} & \\textbf{0.0735} \\\\\nC & none & 0.2151 & 0.0250 & 0.0246 & 0.0882 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel~B reduces total MSE by 6.7\\% relative to~A and by 16.7\\% relative to~C.  The gains concentrate on the non-perturbed axes: $y$- and $z$-axis MSE drop by 22.7\\% and 23.9\\% versus~A, indicating that Model~B learns to leave low-uncertainty dimensions largely untouched while directing correction effort toward the high-uncertainty $x$-axis.  Model~A, receiving only a scalar average, lacks the information to make this distinction and applies a uniform correction that degrades the already-accurate axes.\n\nWith oracle (ground-truth) variances, the ranking $\\text{B}>\\text{A}>\\text{C}$ is preserved with larger margins (non-perturbed axis improvements of 30--38\\% over~A).  Moving from oracle to $K{=}10$ estimation reduces relative gains by roughly 15 percentage points, reflecting finite-sample noise, but does not alter the ordering.  The pattern also holds at weaker anisotropy ratios (2:1 and 1.5:1): across all six conditions tested, Model~B consistently outperforms both baselines.\n\n\\paragraph{Takeaway.}\nEven a simple MLP can exploit per-DOF uncertainty structure for dimension-selective correction---a capability that scalar summaries cannot provide.  This motivates the design of \\textbf{ACR-VLA}, which extracts rich per-DOF features from a flow-matching VLA and feeds them into a learned correction module (Section~\\ref{sec:method}).\n\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%% Section 4 -- Method\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA) is an inference-time, post-hoc module that attaches to any flow-matching VLA without modifying its weights.  It comprises three components (Figure~\\ref{fig:pipeline}):\n\\begin{enumerate}[nosep]\n  \\item \\textbf{Conformalized Gaussian Scoring} (CGS, \\S\\ref{sec:cgs}): draws $K{=}10$ action samples per step, fits a shrinkage-regularized Gaussian, and extracts a 40-dimensional structured uncertainty feature.\n  \\item \\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency} (ACI+COC, \\S\\ref{sec:aci}): maintains an online conformal threshold that adapts to distribution shift using a self-referential coverage signal from overlapping action chunks.\n  \\item \\textbf{Conformal Refinement Module} (CRM, \\S\\ref{sec:crm}): a lightweight MLP that takes the CGS features as conditioning and outputs a dimension-selective residual correction.\n\\end{enumerate}\n\nWe instantiate \\textbf{ACR-VLA} on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that predicts action chunks of size 50 with action dimension $d{=}6$ (3 translation + 3 rotation; the gripper is handled separately outside the conformal pipeline).\n\n\n%%% 4.1 CGS %%%\n\\subsection{Conformalized Gaussian Scoring}\n\\label{sec:cgs}\n\nCGS converts a set of stochastic action samples from the base VLA into a compact uncertainty descriptor that captures \\emph{which} degrees of freedom are uncertain and \\emph{how} they co-vary---information that a scalar nonconformity score discards.\n\n\\paragraph{Sampling and truncation.}\nAt each control step, we draw $K{=}10$ action chunks from the frozen base VLA via independent flow-matching rollouts.  Although SmolVLA predicts 50-step chunks, under receding-horizon execution only the first few steps influence the robot before re-planning.  We therefore retain only the first $H{=}5$ steps, yielding $K$ samples $\\{a_h^{(k)}\\}_{k=1}^{K}$ with $a_h^{(k)}\\in\\mathbb{R}^{d}$ for each horizon step $h=1,\\dots,H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1-\\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity.  With a dimension-to-sample ratio $p/n = d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error due to the Marchenko--Pastur effect; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nWe define a joint multivariate nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis single score captures cross-DOF covariance structure.  In contrast, treating each DOF independently and applying Bonferroni correction across all $d{\\times}H = 30$ marginals yields intervals that are substantially wider than necessary.  Our joint formulation requires Bonferroni correction only across $H{=}5$ horizon steps (target level $\\alpha/H$ per step), preserving tight per-step regions~\\cite{braun2025cgs}.\n\n\\paragraph{CGS feature vector.}\nWe assemble a 40-dimensional feature $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$ that is passed to the refinement module:\n\\begin{equation}\n  \\boldsymbol{\\varphi}_{\\mathrm{CGS}} = \\bigl[\\,\\underbrace{\\sigma_{j,h}}_{j=1..d,\\;h=1..H}\\;;\\;\\underbrace{q_h}_{h=1..H}\\;;\\;\\underbrace{v_h}_{h=1..H}\\,\\bigr] \\;\\in\\;\\mathbb{R}^{40},\n  \\label{eq:cgs_feat}\n\\end{equation}\nwhere $\\sigma_{j,h} = \\sqrt{(\\boldsymbol{\\Sigma}_h)_{jj}}$ is the per-DOF standard deviation (30D), $q_h$ is the ACI-calibrated Mahalanobis threshold at step $h$ (5D, see \\S\\ref{sec:aci}), and $v_h = \\tfrac{1}{2}\\log\\det(\\boldsymbol{\\Sigma}_h)$ is the log-volume of the covariance ellipsoid (5D).  Together, these encode \\emph{which dimensions are uncertain} (per-DOF std), the \\emph{overall calibrated confidence level} (conformal radius), and the \\emph{spread of the predictive distribution} (log-volume).  Compared with the scalar Euclidean distance used in ReconVLA~\\cite{chen2026reconvla}, this representation captures substantially more structure.\n\n\\paragraph{Relationship to single-pass uncertainty.}\nRecent work~\\cite{xing2026diu} shows that for flow-matching models the divergence of the velocity field recovers per-DOF aleatoric uncertainty from a single forward pass.  CGS instead estimates \\emph{model uncertainty} via multi-sample covariance: a sampling-based signal that reflects both epistemic and aleatoric components, and that rises under distribution shift when the policy is uncertain about the correct action.  For action correction, this shift-sensitive signal is more actionable than a purely aleatoric estimate, since it identifies \\emph{where the model needs help} rather than where the task is inherently ambiguous.  We validate this distinction empirically in ablation~A7.\n\n\n%%% 4.2 ACI + COC %%%\n\\subsection{Adaptive Conformal Inference via Chunk Overlap Consistency}\n\\label{sec:aci}\n\nCGS requires a conformal threshold $q_h$ to convert Mahalanobis scores into calibrated prediction regions.  Static calibration on a held-out set, as in conformal quantile regression~\\cite{romano2019cqr}, assumes exchangeability between calibration and deployment data---an assumption that breaks under the distribution shifts common in real-world manipulation.  We instead adopt Adaptive Conformal Inference (ACI)~\\cite{gibbs2021aci}, which provides long-run coverage guarantees under arbitrary distribution shift, and equip it with a novel self-referential coverage signal.\n\n\\paragraph{The coverage signal problem.}\nACI updates the miscoverage level $\\alpha_t$ at each step based on whether the true action falls inside the conformal region.  In robotics, the most direct signal would check whether the \\emph{executed} action lies within the predicted region.  However, contact dynamics cause the achieved end-effector displacement to differ from the commanded action, corrupting this signal.\n\n\\paragraph{Chunk Overlap Consistency (COC).}\nWe exploit the temporal overlap inherent in receding-horizon action chunking.  At control step $t$, the VLA predicts a chunk $[a_t^1,\\dots,a_t^H]$ with associated conformal ellipsoids $\\{C_t^h\\}_{h=1}^H$ derived from the Mahalanobis score (\\ref{eq:mahal}) and threshold $q_h$.  After executing $a_t^1$ and observing the new state $s_{t+1}$, we draw $K{=}10$ fresh samples and compute the new first-step mean $\\boldsymbol{\\mu}_{t+1}^1$.  The COC coverage indicator is:\n\\begin{equation}\n  \\mathrm{err}_t = \\mathbb{1}\\bigl[\\boldsymbol{\\mu}_{t+1}^1 \\notin C_t^2\\bigr],\n  \\label{eq:coc}\n\\end{equation}\ni.e., we check whether the next step's predicted action falls within the \\emph{previous} step's conformal region for the overlapping horizon position.\n\nCOC has four properties that make it well-suited for online calibration:\n(i)~it is self-referential, requiring no external supervisor or trained reward model;\n(ii)~it compares prediction-to-prediction rather than prediction-to-execution, making it robust to contact dynamics;\n(iii)~it directly measures calibration quality---whether the conformal regions are appropriately sized;\n(iv)~it produces a signal at every control step, not only at episode boundaries.\n\n\\paragraph{Online update rule.}\nThe ACI update follows \\cite{gibbs2021aci}:\n\\begin{equation}\n  \\alpha_{t+1} = \\alpha_t + \\gamma\\bigl(\\alpha_{\\mathrm{target}} - \\mathrm{err}_t\\bigr),\n  \\label{eq:aci_update}\n\\end{equation}\nwhere $\\gamma$ is the learning rate and $\\alpha_{\\mathrm{target}}$ is the desired miscoverage rate.  When $\\mathrm{err}_t{=}1$ (the region failed to cover), $\\alpha_{t+1}$ decreases, widening the next region; when $\\mathrm{err}_t{=}0$, $\\alpha_{t+1}$ increases, tightening it.  Within each episode, we apply exponentially weighted conformal prediction~\\cite{barber2023conformal} with decay parameter $\\rho$ to down-weight stale calibration data.  Across episodes, the fraction of intra-episode COC hits serves as $\\mathrm{err}_t$ for a cross-episode ACI update, enabling the threshold to adapt over the course of deployment.\n\n\n%%% 4.3 CRM %%%\n\\subsection{Conformal Refinement Module}\n\\label{sec:crm}\n\nThe Conformal Refinement Module (CRM) is a lightweight network that performs dimension-selective action correction, conditioned on the structured uncertainty features from CGS.\n\n\\paragraph{Architecture.}\nCRM is a 2-layer MLP with hidden dimension 256 (${\\sim}$337K parameters).  Its input concatenates three sources:\n(i)~the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ from the base VLA encoder,\n(ii)~the 40D CGS feature $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$, and\n(iii)~the mean action $\\boldsymbol{\\mu} \\in \\mathbb{R}^{30}$ ($d{\\times}H = 6{\\times}5$).\nThe output is a residual correction $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the refined action is:\n\\begin{equation}\n  \\mathbf{a}^* = \\boldsymbol{\\mu} + \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}},\\;\\boldsymbol{\\varphi}_{\\mathrm{CGS}},\\;\\boldsymbol{\\mu}).\n  \\label{eq:crm}\n\\end{equation}\n\n\\paragraph{Training.}\nCRM is trained with a single objective:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,\n  \\label{eq:crm_loss}\n\\end{equation}\non demonstration trajectories from LIBERO~\\cite{liu2023libero} augmented with synthetic perturbations (camera shifts, sensor noise, robot-state perturbation, lighting and background variation).  During training, CGS features are computed online: for each augmented observation, we run $K{=}10$ forward passes through the frozen base VLA and extract $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$.  This ensures CRM sees realistic uncertainty patterns that co-vary with the perturbation type---for instance, camera shifts produce elevated translational variance while leaving rotational variance largely unchanged.\n\nACI operates exclusively at inference time: it adjusts the conformal threshold $q_h$, which enters CRM through the conformal-radius components of $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$.  This decoupling of training and calibration eliminates the multi-objective conflicts that arise when calibration-aware losses compete with the primary correction objective in a small-capacity network~\\cite{wang2025cploop}.\n\n\\paragraph{Why per-DOF conditioning enables selective correction.}\nTo build intuition, consider a camera perturbation that introduces translational ambiguity in the $x$-$y$ plane while leaving $z$-translation and rotation well-determined.  A scalar nonconformity score (e.g., average Euclidean sample distance, as in \\cite{chen2026reconvla}) compresses this into ``moderate uncertainty everywhere,'' providing no basis for selective correction.  The per-DOF structure in $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$ instead reveals that $\\sigma_{x},\\sigma_{y} \\gg \\sigma_{z},\\sigma_{\\mathrm{rot}}$, enabling CRM to apply large corrections to the uncertain translational axes while preserving the base VLA's accurate rotational predictions.  Section~\\ref{sec:motivating} validates this mechanism in a controlled setting; Section~\\ref{sec:experiments} demonstrates it on real VLA tasks.\n\n\\paragraph{Inference protocol.}\nEach control step proceeds as: draw $K{=}10$ samples $\\to$ compute CGS $\\to$ apply CRM $\\to$ execute the first action of the refined chunk $\\to$ observe new state $\\to$ draw $K{=}10$ fresh samples $\\to$ compute COC (\\ref{eq:coc}) $\\to$ ACI update (\\ref{eq:aci_update}).  The entire module adds ${\\sim}$337K parameters and $K{=}10$ extra forward passes to the base VLA, with no retraining of the base model.\n",
      "numLines": 166,
      "startLine": 1,
      "totalLines": 166
    }
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:13:20.766Z_

<details><summary>↩ Tool result · `toolu_018gnz9JyoCTiucYahaHBiqz`</summary>

```text
1	# ACR-VLA: CoRL 2026 Paper Outline
2	
3	## Title Candidates
4	
5	1. **ACR-VLA: Inference-Time Action Correction for Vision-Language-Action Models via Sample-Then-Correct**
6	2. **Sample-Then-Correct: Observation-Conditioned Residual Correction Improves VLA Robustness Beyond Sample Selection**
7	3. **Beyond Sample Selection: Learned Action Correction for Frozen Vision-Language-Action Models**
8	
9	Preferred: #2 — 直接点明贡献（sample-then-correct pipeline）+ 核心发现（obs-conditioned > conformal features）。
10	
11	---
12	
13	## Abstract Key Points
14	
15	- **Problem**: Flow-matching VLAs achieve near-saturated performance on standard benchmarks but remain fragile under distribution shift. Existing inference-time methods are limited to sample selection (ReconVLA) or require task-level RL training (SC-VLA).
16	- **Method**: ACR-VLA — a sample-then-correct pipeline: (1) draw K=10 samples from frozen VLA, (2) conformal prediction selects best candidate, (3) lightweight CRM (250K params) applies learned residual correction conditioned on observation features.
17	- **Key finding 1**: Sample-then-correct > sample-then-select. obs_only CRM achieves 19.0% on LIBERO-Object vs 12.0% argmin selection (+7.0pp).
18	- **Key finding 2 (negative result)**: Per-DOF conformal features as CRM input offer no advantage over observation features — perdof CRM 11.0% ≈ argmin 12.0%, while obs_only 19.0%.
19	- **Key finding 3**: Correction magnitude control is critical and previously unrecognized — norm=1.42 yields 0%, norm=0.1-0.2 yields +7pp, obs_only CRM is uniquely robust across the magnitude range.
20	- **Stats**: Fisher exact test p < 0.05 on combined seed=42+43 (200 trials). [pending seed=43 completion]
21	
22	---
23	
24	## 1. Introduction (~1.5 pages)
25	
26	### Motivation
27	- VLAs (π₀, OpenVLA, SmolVLA) represent a paradigm shift in robot learning, but distribution shift remains a major challenge.
28	- LIBERO benchmark exposes robustness gap: VLA performance degrades significantly under object/spatial perturbations.
29	
30	### Gap
31	- **Sample selection** (ReconVLA argmin over K candidates): bounded by candidate quality — when all samples are poor, selection fails.
32	- **RL-based refinement** (SC-VLA): requires per-task RL training, not plug-and-play.
33	- **No prior work** on inference-time learned action correction for frozen VLAs.
34	
35	### Contributions (3 bullet points)
36	1. **Sample-then-correct pipeline**: First system to apply learned residual correction on conformal-selected VLA actions. obs_only CRM improves SmolVLA success rate by +7.0pp on LIBERO-Object over sample selection alone.
37	2. **Systematic conditioning comparison + honest negative result**: Per-DOF conformal statistics — intuitively richer features — provide no CRM benefit. Observation features suffice. This challenges synthetic-experiment intuition and reveals the gap between per-step MSE and closed-loop success.
38	3. **Correction magnitude sensitivity**: First empirical study of correction magnitude control for VLA action refinement. obs_only CRM is robust across norms; perdof CRM collapses at high correction magnitudes.
39	
40	---
41	
42	## 2. Related Work (~1 page)
43	
44	### Categories to cover:
45	
46	| Category | Key papers | Our positioning |
47	|----------|-----------|-----------------|
48	| Vision-Language-Action Models | π₀ (Black et al. 2024), OpenVLA (Kim et al. 2024), SmolVLA (Leal et al. 2025) | We use SmolVLA as frozen backbone; method is backbone-agnostic |
49	| Inference-time scaling for VLAs | ReconVLA (Liang et al. 2025), VLA-Pilot (Zhang et al. 2025) | ReconVLA = selection-only baseline; VLA-Pilot too slow (2.41s/step) |
50	| Residual RL / action correction | SC-VLA (Qu et al. 2025), residual policy learning (Silver et al. 2018, Johannink et al. 2019) | SC-VLA requires task-level RL; our CRM is trained offline on demonstration data |
51	| Conformal prediction in robotics | ReconVLA, conformal prediction for planning (Lindemann et al. 2023) | We use CP for sample selection stage, not for output guarantees |
52	| Test-time compute / inference scaling | Snell et al. 2024, Brown et al. 2024 | Broader context: our work extends inference-time scaling from selection to correction |
53	
54	---
55	
56	## 3. Method (~2 pages)
57	
58	### 3.1 Problem Setup
59	- Frozen VLA backbone (SmolVLA), flow-matching action generation
60	- LIBERO evaluation under distribution shift (spatial perturbation, object substitution)
61	
62	### 3.2 Conformal Sample Selection
63	- Draw K=10 action samples from VLA
64	- Per-DOF conformal prediction: nonconformity scores from calibration set
65	- Argmin selection: pick sample with lowest aggregate nonconformity score
66	- **Figure 1**: Pipeline overview diagram (sample → score → select → correct)
67	
68	### 3.3 Correction Residual Module (CRM)
69	- Architecture: 3-layer MLP, 250K parameters, ~3ms inference overhead
70	- Input variants: (a) per-DOF conformal features, (b) observation features (obs_only), (c) scalar conformal score
71	- Output: residual correction δ added to selected action
72	- Training: MSE loss on demonstration actions, trained on calibration split
73	
74	### 3.4 Correction Magnitude Control
75	- L2 norm clipping of CRM output: ||δ||₂ ≤ norm_max
76	- Why it matters: unconstrained CRM (norm=1.42) → 0% success; norm ∈ [0.1, 0.2] → optimal
77	- obs_only vs perdof: differential sensitivity to norm_max (obs_only robust, perdof collapses)
78	
79	---
80	
81	## 4. Experiments (~2.5 pages)
82	
83	### 4.1 Setup
84	- **Backbone**: SmolVLA (fine-tuned on LIBERO)
85	- **Benchmark**: LIBERO-Spatial (10 tasks), LIBERO-Object (10 tasks)
86	- **Baselines**: VLA-only K=1, VLA-mean K=10, argmin K=10 (≈ ReconVLA selection)
87	- **CRM variants**: perdof, obs_only, scalar, all at norm=0.1
88	- **Evaluation**: 10 rollouts × 10 tasks = 100 trials per method; 2 seeds (42, 43) = 200 trials for significance
89	
90	### 4.2 Main Results
91	
92	**Table 1: Object Benchmark (seed=42, 10-task)**
93	
94	| Method | SR (%) | Δ vs argmin |
95	|--------|--------|-------------|
96	| VLA-only K=1 | 12.0 | — |
97	| VLA-mean K=10 | 12.0 | 0.0 |
98	| argmin K=10 | 12.0 | baseline |
99	| scalar CRM 0.1 | 9.0 | -3.0 |
100	| perdof CRM 0.1 | 11.0 | -1.0 |
101	| **obs_only CRM 0.1** | **19.0** | **+7.0** |
102	
103	**Table 2: Spatial Benchmark (seed=42, 10-task)** — honest null result
104	
105	| Method | SR (%) |
106	|--------|--------|
107	| argmin K=10 | 34.0 |
108	| perdof CRM 0.1 | 35.0 |
109	| obs_only CRM 0.1 | 35.0 |
110	| VLA-only K=1 | 30.0 |
111	
112	Exp IDs: eval-acr-object-v4-obs-only, eval-acr-spatial-v4-obs-only-r3, eval-argmin-only-spatial-r2
113	
114	### 4.3 Magnitude Sensitivity Analysis
115	
116	**Table 3 / Figure 2: Magnitude sweep (obs_only vs perdof)**
117	
118	| norm | obs_only (spatial) | perdof (spatial) | gap |
119	|------|-------------------|------------------|-----|
120	| 0.05 | 35.0% | 31.0% | +4pp |
121	| 0.1 | 35.0% | 35.0% | 0pp |
122	| 0.2 | 35.0% | 28.3% | +6.7pp |
123	| 0.3 | 36.0% | 26.0% | +10pp |
124	
125	- **Figure 2**: Line plot — obs_only flat, perdof declining with norm. Clear visual story.
126	- Object magnitude (obs_only norm=0.1: 19%, norm=0.2: 18-22%) — if available.
127	
128	Exp IDs: eval-mag-obsonly-norm005, eval-mag-obsonly-norm02, eval-mag-perdof-norm03, eval-mag-obsonly-norm03
129	
130	### 4.4 Statistical Significance
131	
132	**Table 4: Combined seed=42+43 results** [pending seed=43 completion]
133	- Fisher exact test: obs_only vs argmin, 200 trials
134	- Bootstrap 95% CI for success rate difference
135	- Per-task breakdown showing which tasks drive the improvement
136	
137	### 4.5 Per-Task Analysis
138	
139	**Figure 3: Per-task success rate heatmap** (methods × tasks)
140	- Shows obs_only gains come from medium-difficulty tasks (not hard tasks where all fail, not easy tasks where all succeed)
141	- Hard tasks (T2, T7) = 0% for all methods → VLA backbone limitation, not CRM scope
142	
143	---
144	
145	## 5. Discussion (~1 page)
146	
147	### 5.1 Why Does obs_only Work But perdof Doesn't?
148	- Hypothesis: per-DOF conformal features are noisy with K=10 (covariance estimation from 10 samples)
149	- obs_only uses stable image/proprioception features → more reliable correction signal
150	- perdof learns overconfident correction patterns that collapse at higher norms
151	- Gap between per-step MSE (where perdof looks good in training) and closed-loop success
152	
153	### 5.2 Why Does Spatial Show No CRM Effect?
154	- Spatial perturbations (position offsets) → VLA actions are less systematically biased → CRM correction cannot find consistent error patterns
155	- Hard tasks (T2, T7) are VLA backbone failures (0% across all methods), not correctable
156	- Object perturbations (object substitution) → larger action distribution shift → more room for learned correction
157	
158	### 5.3 Limitations
159	- Simulation only (LIBERO); real-world transfer untested
160	- Single VLA backbone (SmolVLA); generality to π₀, OpenVLA unknown
161	- CRM trained on same task distribution; cross-task generalization not evaluated
162	- Absolute performance remains low (19%) — CRM improves relative to baseline but tasks remain hard
163	- K=10 samples = 10× inference cost (shared with ReconVLA)
164	
165	### 5.4 Future Work
166	- Real-robot evaluation
167	- Scaling to stronger VLA backbones (π₀)
168	- Adaptive magnitude control (learned norm instead of fixed clipping)
169	- Cross-task CRM transfer
170	
171	---
172	
173	## 6. Figures & Tables Checklist
174	
175	| ID | Type | Content | Data source | Status |
176	|----|------|---------|-------------|--------|
177	| Fig 1 | Diagram | Pipeline overview: sample → conformal score → select → CRM correct | N/A | TODO |
178	| Fig 2 | Line plot | Magnitude sensitivity: obs_only vs perdof across norms | magnitude sweep exps | data ready (spatial), object pending |
179	| Fig 3 | Heatmap | Per-task success rates (methods × tasks) | all object + spatial evals | data ready |
180	| Tab 1 | Table | Object benchmark main results (6 methods) | object evals seed=42 | FINAL |
181	| Tab 2 | Table | Spatial benchmark (honest null) | spatial evals seed=42 | LOCKED |
182	| Tab 3 | Table | Magnitude sweep | magnitude sweep exps | partial |
183	| Tab 4 | Table | Statistical significance (seed 42+43 combined) | seed=43 evals | PENDING |
184	| Tab 5 | Table | CRM architecture / training details | implementation | TODO |
185	
186	---
187	
188	## 7. Writing Timeline (CoRL 2026)
189	
190	| Date | Milestone |
191	|------|-----------|
192	| May 15-17 | Outline finalized, seed=43 results in |
193	| May 18-20 | Method + Experiments sections drafted |
194	| May 21-23 | Intro + Related Work drafted, figures generated |
195	| May 24-25 | Full draft review, abstract polished |
196	| **May 26** | **Abstract submission** |
197	| May 27-30 | Revise based on internal review, camera-ready figures |
198	| Jun 1 | Final proofread |
199	| **Jun 2** | **Full paper submission** |
200	
201	---
202	
203	## Key Risks
204	
205	1. **seed=43 不复现**: obs_only 优势消失 → Fisher test fails → 论文 claim 不成立。应对：如果 p > 0.05，降级为 workshop paper 或增加 seed=44。
206	2. **Object obs_only norm=0.2 未超 norm=0.1**: magnitude story 在 object 上弱化。应对：spatial magnitude sweep 仍可支撑 robustness claim。
207	3. **Reviewer 认为 obs_only 就是普通 residual MLP**: 需要强调 systematic comparison + conformal selection 前置 + magnitude discovery 的整体贡献。
208	4. **绝对性能低 (19%)**: 需要 contextualize — LIBERO-Object 在分布偏移下本身很难，VLA-only 仅 12%。相对提升 58% (7/12) 是 meaningful 的。
209	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "9546c7a2-79ba-4236-9db6-d0794ef549de",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/corl_paper_outline.md",
      "content": "# ACR-VLA: CoRL 2026 Paper Outline\n\n## Title Candidates\n\n1. **ACR-VLA: Inference-Time Action Correction for Vision-Language-Action Models via Sample-Then-Correct**\n2. **Sample-Then-Correct: Observation-Conditioned Residual Correction Improves VLA Robustness Beyond Sample Selection**\n3. **Beyond Sample Selection: Learned Action Correction for Frozen Vision-Language-Action Models**\n\nPreferred: #2 — 直接点明贡献（sample-then-correct pipeline）+ 核心发现（obs-conditioned > conformal features）。\n\n---\n\n## Abstract Key Points\n\n- **Problem**: Flow-matching VLAs achieve near-saturated performance on standard benchmarks but remain fragile under distribution shift. Existing inference-time methods are limited to sample selection (ReconVLA) or require task-level RL training (SC-VLA).\n- **Method**: ACR-VLA — a sample-then-correct pipeline: (1) draw K=10 samples from frozen VLA, (2) conformal prediction selects best candidate, (3) lightweight CRM (250K params) applies learned residual correction conditioned on observation features.\n- **Key finding 1**: Sample-then-correct > sample-then-select. obs_only CRM achieves 19.0% on LIBERO-Object vs 12.0% argmin selection (+7.0pp).\n- **Key finding 2 (negative result)**: Per-DOF conformal features as CRM input offer no advantage over observation features — perdof CRM 11.0% ≈ argmin 12.0%, while obs_only 19.0%.\n- **Key finding 3**: Correction magnitude control is critical and previously unrecognized — norm=1.42 yields 0%, norm=0.1-0.2 yields +7pp, obs_only CRM is uniquely robust across the magnitude range.\n- **Stats**: Fisher exact test p < 0.05 on combined seed=42+43 (200 trials). [pending seed=43 completion]\n\n---\n\n## 1. Introduction (~1.5 pages)\n\n### Motivation\n- VLAs (π₀, OpenVLA, SmolVLA) represent a paradigm shift in robot learning, but distribution shift remains a major challenge.\n- LIBERO benchmark exposes robustness gap: VLA performance degrades significantly under object/spatial perturbations.\n\n### Gap\n- **Sample selection** (ReconVLA argmin over K candidates): bounded by candidate quality — when all samples are poor, selection fails.\n- **RL-based refinement** (SC-VLA): requires per-task RL training, not plug-and-play.\n- **No prior work** on inference-time learned action correction for frozen VLAs.\n\n### Contributions (3 bullet points)\n1. **Sample-then-correct pipeline**: First system to apply learned residual correction on conformal-selected VLA actions. obs_only CRM improves SmolVLA success rate by +7.0pp on LIBERO-Object over sample selection alone.\n2. **Systematic conditioning comparison + honest negative result**: Per-DOF conformal statistics — intuitively richer features — provide no CRM benefit. Observation features suffice. This challenges synthetic-experiment intuition and reveals the gap between per-step MSE and closed-loop success.\n3. **Correction magnitude sensitivity**: First empirical study of correction magnitude control for VLA action refinement. obs_only CRM is robust across norms; perdof CRM collapses at high correction magnitudes.\n\n---\n\n## 2. Related Work (~1 page)\n\n### Categories to cover:\n\n| Category | Key papers | Our positioning |\n|----------|-----------|-----------------|\n| Vision-Language-Action Models | π₀ (Black et al. 2024), OpenVLA (Kim et al. 2024), SmolVLA (Leal et al. 2025) | We use SmolVLA as frozen backbone; method is backbone-agnostic |\n| Inference-time scaling for VLAs | ReconVLA (Liang et al. 2025), VLA-Pilot (Zhang et al. 2025) | ReconVLA = selection-only baseline; VLA-Pilot too slow (2.41s/step) |\n| Residual RL / action correction | SC-VLA (Qu et al. 2025), residual policy learning (Silver et al. 2018, Johannink et al. 2019) | SC-VLA requires task-level RL; our CRM is trained offline on demonstration data |\n| Conformal prediction in robotics | ReconVLA, conformal prediction for planning (Lindemann et al. 2023) | We use CP for sample selection stage, not for output guarantees |\n| Test-time compute / inference scaling | Snell et al. 2024, Brown et al. 2024 | Broader context: our work extends inference-time scaling from selection to correction |\n\n---\n\n## 3. Method (~2 pages)\n\n### 3.1 Problem Setup\n- Frozen VLA backbone (SmolVLA), flow-matching action generation\n- LIBERO evaluation under distribution shift (spatial perturbation, object substitution)\n\n### 3.2 Conformal Sample Selection\n- Draw K=10 action samples from VLA\n- Per-DOF conformal prediction: nonconformity scores from calibration set\n- Argmin selection: pick sample with lowest aggregate nonconformity score\n- **Figure 1**: Pipeline overview diagram (sample → score → select → correct)\n\n### 3.3 Correction Residual Module (CRM)\n- Architecture: 3-layer MLP, 250K parameters, ~3ms inference overhead\n- Input variants: (a) per-DOF conformal features, (b) observation features (obs_only), (c) scalar conformal score\n- Output: residual correction δ added to selected action\n- Training: MSE loss on demonstration actions, trained on calibration split\n\n### 3.4 Correction Magnitude Control\n- L2 norm clipping of CRM output: ||δ||₂ ≤ norm_max\n- Why it matters: unconstrained CRM (norm=1.42) → 0% success; norm ∈ [0.1, 0.2] → optimal\n- obs_only vs perdof: differential sensitivity to norm_max (obs_only robust, perdof collapses)\n\n---\n\n## 4. Experiments (~2.5 pages)\n\n### 4.1 Setup\n- **Backbone**: SmolVLA (fine-tuned on LIBERO)\n- **Benchmark**: LIBERO-Spatial (10 tasks), LIBERO-Object (10 tasks)\n- **Baselines**: VLA-only K=1, VLA-mean K=10, argmin K=10 (≈ ReconVLA selection)\n- **CRM variants**: perdof, obs_only, scalar, all at norm=0.1\n- **Evaluation**: 10 rollouts × 10 tasks = 100 trials per method; 2 seeds (42, 43) = 200 trials for significance\n\n### 4.2 Main Results\n\n**Table 1: Object Benchmark (seed=42, 10-task)**\n\n| Method | SR (%) | Δ vs argmin |\n|--------|--------|-------------|\n| VLA-only K=1 | 12.0 | — |\n| VLA-mean K=10 | 12.0 | 0.0 |\n| argmin K=10 | 12.0 | baseline |\n| scalar CRM 0.1 | 9.0 | -3.0 |\n| perdof CRM 0.1 | 11.0 | -1.0 |\n| **obs_only CRM 0.1** | **19.0** | **+7.0** |\n\n**Table 2: Spatial Benchmark (seed=42, 10-task)** — honest null result\n\n| Method | SR (%) |\n|--------|--------|\n| argmin K=10 | 34.0 |\n| perdof CRM 0.1 | 35.0 |\n| obs_only CRM 0.1 | 35.0 |\n| VLA-only K=1 | 30.0 |\n\nExp IDs: eval-acr-object-v4-obs-only, eval-acr-spatial-v4-obs-only-r3, eval-argmin-only-spatial-r2\n\n### 4.3 Magnitude Sensitivity Analysis\n\n**Table 3 / Figure 2: Magnitude sweep (obs_only vs perdof)**\n\n| norm | obs_only (spatial) | perdof (spatial) | gap |\n|------|-------------------|------------------|-----|\n| 0.05 | 35.0% | 31.0% | +4pp |\n| 0.1 | 35.0% | 35.0% | 0pp |\n| 0.2 | 35.0% | 28.3% | +6.7pp |\n| 0.3 | 36.0% | 26.0% | +10pp |\n\n- **Figure 2**: Line plot — obs_only flat, perdof declining with norm. Clear visual story.\n- Object magnitude (obs_only norm=0.1: 19%, norm=0.2: 18-22%) — if available.\n\nExp IDs: eval-mag-obsonly-norm005, eval-mag-obsonly-norm02, eval-mag-perdof-norm03, eval-mag-obsonly-norm03\n\n### 4.4 Statistical Significance\n\n**Table 4: Combined seed=42+43 results** [pending seed=43 completion]\n- Fisher exact test: obs_only vs argmin, 200 trials\n- Bootstrap 95% CI for success rate difference\n- Per-task breakdown showing which tasks drive the improvement\n\n### 4.5 Per-Task Analysis\n\n**Figure 3: Per-task success rate heatmap** (methods × tasks)\n- Shows obs_only gains come from medium-difficulty tasks (not hard tasks where all fail, not easy tasks where all succeed)\n- Hard tasks (T2, T7) = 0% for all methods → VLA backbone limitation, not CRM scope\n\n---\n\n## 5. Discussion (~1 page)\n\n### 5.1 Why Does obs_only Work But perdof Doesn't?\n- Hypothesis: per-DOF conformal features are noisy with K=10 (covariance estimation from 10 samples)\n- obs_only uses stable image/proprioception features → more reliable correction signal\n- perdof learns overconfident correction patterns that collapse at higher norms\n- Gap between per-step MSE (where perdof looks good in training) and closed-loop success\n\n### 5.2 Why Does Spatial Show No CRM Effect?\n- Spatial perturbations (position offsets) → VLA actions are less systematically biased → CRM correction cannot find consistent error patterns\n- Hard tasks (T2, T7) are VLA backbone failures (0% across all methods), not correctable\n- Object perturbations (object substitution) → larger action distribution shift → more room for learned correction\n\n### 5.3 Limitations\n- Simulation only (LIBERO); real-world transfer untested\n- Single VLA backbone (SmolVLA); generality to π₀, OpenVLA unknown\n- CRM trained on same task distribution; cross-task generalization not evaluated\n- Absolute performance remains low (19%) — CRM improves relative to baseline but tasks remain hard\n- K=10 samples = 10× inference cost (shared with ReconVLA)\n\n### 5.4 Future Work\n- Real-robot evaluation\n- Scaling to stronger VLA backbones (π₀)\n- Adaptive magnitude control (learned norm instead of fixed clipping)\n- Cross-task CRM transfer\n\n---\n\n## 6. Figures & Tables Checklist\n\n| ID | Type | Content | Data source | Status |\n|----|------|---------|-------------|--------|\n| Fig 1 | Diagram | Pipeline overview: sample → conformal score → select → CRM correct | N/A | TODO |\n| Fig 2 | Line plot | Magnitude sensitivity: obs_only vs perdof across norms | magnitude sweep exps | data ready (spatial), object pending |\n| Fig 3 | Heatmap | Per-task success rates (methods × tasks) | all object + spatial evals | data ready |\n| Tab 1 | Table | Object benchmark main results (6 methods) | object evals seed=42 | FINAL |\n| Tab 2 | Table | Spatial benchmark (honest null) | spatial evals seed=42 | LOCKED |\n| Tab 3 | Table | Magnitude sweep | magnitude sweep exps | partial |\n| Tab 4 | Table | Statistical significance (seed 42+43 combined) | seed=43 evals | PENDING |\n| Tab 5 | Table | CRM architecture / training details | implementation | TODO |\n\n---\n\n## 7. Writing Timeline (CoRL 2026)\n\n| Date | Milestone |\n|------|-----------|\n| May 15-17 | Outline finalized, seed=43 results in |\n| May 18-20 | Method + Experiments sections drafted |\n| May 21-23 | Intro + Related Work drafted, figures generated |\n| May 24-25 | Full draft review, abstract polished |\n| **May 26** | **Abstract submission** |\n| May 27-30 | Revise based on internal review, camera-ready figures |\n| Jun 1 | Final proofread |\n| **Jun 2** | **Full paper submission** |\n\n---\n\n## Key Risks\n\n1. **seed=43 不复现**: obs_only 优势消失 → Fisher test fails → 论文 claim 不成立。应对：如果 p > 0.05，降级为 workshop paper 或增加 seed=44。\n2. **Object obs_only norm=0.2 未超 norm=0.1**: magnitude story 在 object 上弱化。应对：spatial magnitude sweep 仍可支撑 robustness claim。\n3. **Reviewer 认为 obs_only 就是普通 residual MLP**: 需要强调 systematic comparison + conformal selection 前置 + magnitude discovery 的整体贡献。\n4. **绝对性能低 (19%)**: 需要 contextualize — LIBERO-Object 在分布偏移下本身很难，VLA-only 仅 12%。相对提升 58% (7/12) 是 meaningful 的。\n",
      "numLines": 209,
      "startLine": 1,
      "totalLines": 209
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
Now I have a clear picture. The old method section had incorrect framing (per-DOF as main contribution, ACI+COC module, 40D CGS features). The new method section should:

1. Frame obs_only CRM as the main method
2. Remove ACI/COC (not part of the final pipeline)
3. Remove CGS feature vector (CRM doesn't use it)
4. Use argmin selection (not conformal region)
5. Emphasize magnitude control as critical finding
6. Honest about per-DOF features not helping

Let me also check the introduction for context on notation and framing.


Now I'm drafting the method section while reviewing the existing introduction and experiments to ensure consistent notation throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "b4be59c8-b788-4c94-8f5c-b6d4a1f125b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiRvTzowX5vu7VPBXMW5ad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9684,
      "cache_read_input_tokens": 30702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9684
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

Now I have full context. The old draft has incorrect framing (per-DOF as main contribution, ACI+COC, 40D CGS features). Writing the new method section with the corrected framing: obs_only CRM as the method, magnitude control as critical, honest negative result on per-DOF features.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "3edf10a6-433f-45bf-bf22-b0d7a5492ff4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiRvTzowX5vu7VPBXMW5ad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9684,
      "cache_read_input_tokens": 30702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9684
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

<details open><summary>🔧 Tool call — Read · `toolu_01PdioELp3Qnp9RLnzhgxraW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "a8e5efb8-f205-48c0-b6a4-4a5adfc914d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GiRvTzowX5vu7VPBXMW5ad",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9684,
      "cache_read_input_tokens": 30702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9684
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

_source line 18 · 2026-05-15T19:13:31.170Z_

<details><summary>↩ Tool result · `toolu_01PdioELp3Qnp9RLnzhgxraW`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	% Para 1: Problem — VLA success + robustness gap under distribution shift
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla} have reached 97--99\% success rates on standard manipulation benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this near-saturation masks a fragile reality: under distribution shifts common in real-world deployment---camera viewpoint changes, lighting variation, sensor noise, object layout differences---the same policies suffer substantial performance degradation~\cite{fei2025liberoplus}.
7	Closing this robustness gap is a prerequisite for deploying learned manipulation policies outside tightly controlled lab settings.
8	
9	% Para 2: Existing approaches — training-time vs inference-time, what they miss
10	Two lines of work address VLA robustness.
11	\emph{Training-time methods} improve the base policy itself: SRPO~\cite{srpo2025} applies self-referential policy optimization, while RobustVLA~\cite{robustvla2025} and DiG-Flow~\cite{digflow2025} incorporate robustness-aware objectives into training.
12	These methods are effective but require retraining or fine-tuning, and their gains are bounded by the training distribution.
13	\emph{Inference-time methods} leave the policy frozen and intervene at deployment.
14	ReconVLA~\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean, using scalar Euclidean distance as an uncertainty proxy.
15	SAFE~\cite{gu2025safe} detects anomalous states and triggers fallback behaviors.
16	UPS~\cite{yuan2026ups} and CP-in-the-Loop~\cite{wang2025cploop} use conformal prediction for binary decisions---execute or abstain, safe or unsafe---but do not use conformal statistics as features for continuous correction.
17	A2C2~\cite{a2c2_2025} learns a residual correction that runs asynchronously alongside the base policy, yet applies it without uncertainty conditioning, lacking any mechanism to modulate correction magnitude across action dimensions.
18	In short, no existing method performs inference-time action correction conditioned on \emph{structured, per-degree-of-freedom uncertainty}.
19	
20	% Para 3: Our insight — per-DOF conformal features as continuous input to learned correction
21	Our key observation is that the stochastic samples already produced by a flow-matching VLA contain rich, structured uncertainty information that current methods discard.
22	By fitting a shrinkage-regularized Gaussian to $K{=}10$ samples and computing multivariate conformal statistics~\cite{braun2025cgs}, we obtain a 40-dimensional feature vector that encodes \emph{which} action dimensions are uncertain (per-DOF standard deviations), the \emph{calibrated confidence level} (conformal radii from Adaptive Conformal Inference~\cite{gibbs2021aci}), and the \emph{overall predictive spread} (log-volume of the covariance ellipsoid).
23	This representation captures substantially more structure than the scalar distances used in ReconVLA~\cite{chen2026reconvla}: it preserves the cross-DOF covariance structure that enables a downstream module to correct high-uncertainty dimensions aggressively while leaving confident predictions untouched.
24	A controlled 3D point-reaching experiment confirms this: a correction MLP conditioned on per-DOF uncertainty reduces total error by 6.7\% over scalar conditioning and by 16.7\% over no uncertainty input, with 22--24\% improvements concentrated on the non-perturbed axes where scalar conditioning cannot distinguish signal from noise (Section~\ref{sec:motivating}).
25	
26	% Para 4: ACR-VLA overview — 3 components, key design choices
27	We introduce \textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that attaches to any frozen flow-matching VLA and performs dimension-selective action correction.
28	ACR-VLA comprises three components:
29	(i)~\textbf{Conformalized Gaussian Scoring (CGS)} draws $K{=}10$ samples per control step, fits a Ledoit--Wolf shrinkage covariance, and extracts a 40D structured uncertainty feature;
30	(ii)~\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency (ACI+COC)} maintains an online conformal threshold~\cite{gibbs2021aci} using a self-referential coverage signal derived from overlapping action chunks---requiring no external supervisor, reward model, or ground-truth actions;
31	(iii)~\textbf{Conformal Refinement Module (CRM)}, a lightweight MLP (${\sim}$337K parameters) that takes the CGS features as conditioning and outputs a dimension-selective residual correction.
32	We note that conformal prediction serves here as a \emph{feature extraction and calibration mechanism}, not as a guarantee on the corrected output: CGS features provide structured uncertainty conditioning for CRM, while ACI+COC adapts these features online under distribution shift.
33	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
34	
35	% Para 5: Contributions — numbered list
36	Our contributions are:
37	\begin{enumerate}[leftmargin=*,nosep]
38	  \item \textbf{Per-DOF conformal features for dimension-selective correction.}
39	  We show that the 40D CGS representation---per-DOF standard deviations, calibrated conformal radii, and covariance log-volume---enables CRM to selectively correct uncertain action dimensions while preserving accurate ones.
40	  On LIBERO, ACR-VLA improves base SmolVLA success by \textbf{XX.X}\,pp, and ablations confirm that per-DOF features outperform both scalar uncertainty and no-uncertainty baselines (Section~\ref{sec:experiments}).
41	
42	  \item \textbf{Self-referential online calibration via Chunk Overlap Consistency.}
43	  COC exploits the temporal overlap in receding-horizon action chunks to provide a coverage signal for ACI without external supervision.
44	  This enables the conformal threshold to adapt online under arbitrary distribution shift, maintaining calibrated uncertainty features throughout deployment (Section~\ref{sec:aci}).
45	
46	  \item \textbf{Systematic evaluation across multiple LIBERO task suites.}
47	  We evaluate ACR-VLA on LIBERO-Spatial and LIBERO-Object, providing per-task breakdowns, ablations isolating the contribution of each component (CGS features, ACI+COC calibration, CRM architecture), and analysis of when and why dimension-selective correction helps (Section~\ref{sec:experiments}).
48	\end{enumerate}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "fff8cd34-13c2-4325-9430-f2cca0e274e2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% Para 1: Problem — VLA success + robustness gap under distribution shift\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla} have reached 97--99\\% success rates on standard manipulation benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this near-saturation masks a fragile reality: under distribution shifts common in real-world deployment---camera viewpoint changes, lighting variation, sensor noise, object layout differences---the same policies suffer substantial performance degradation~\\cite{fei2025liberoplus}.\nClosing this robustness gap is a prerequisite for deploying learned manipulation policies outside tightly controlled lab settings.\n\n% Para 2: Existing approaches — training-time vs inference-time, what they miss\nTwo lines of work address VLA robustness.\n\\emph{Training-time methods} improve the base policy itself: SRPO~\\cite{srpo2025} applies self-referential policy optimization, while RobustVLA~\\cite{robustvla2025} and DiG-Flow~\\cite{digflow2025} incorporate robustness-aware objectives into training.\nThese methods are effective but require retraining or fine-tuning, and their gains are bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen and intervene at deployment.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean, using scalar Euclidean distance as an uncertainty proxy.\nSAFE~\\cite{gu2025safe} detects anomalous states and triggers fallback behaviors.\nUPS~\\cite{yuan2026ups} and CP-in-the-Loop~\\cite{wang2025cploop} use conformal prediction for binary decisions---execute or abstain, safe or unsafe---but do not use conformal statistics as features for continuous correction.\nA2C2~\\cite{a2c2_2025} learns a residual correction that runs asynchronously alongside the base policy, yet applies it without uncertainty conditioning, lacking any mechanism to modulate correction magnitude across action dimensions.\nIn short, no existing method performs inference-time action correction conditioned on \\emph{structured, per-degree-of-freedom uncertainty}.\n\n% Para 3: Our insight — per-DOF conformal features as continuous input to learned correction\nOur key observation is that the stochastic samples already produced by a flow-matching VLA contain rich, structured uncertainty information that current methods discard.\nBy fitting a shrinkage-regularized Gaussian to $K{=}10$ samples and computing multivariate conformal statistics~\\cite{braun2025cgs}, we obtain a 40-dimensional feature vector that encodes \\emph{which} action dimensions are uncertain (per-DOF standard deviations), the \\emph{calibrated confidence level} (conformal radii from Adaptive Conformal Inference~\\cite{gibbs2021aci}), and the \\emph{overall predictive spread} (log-volume of the covariance ellipsoid).\nThis representation captures substantially more structure than the scalar distances used in ReconVLA~\\cite{chen2026reconvla}: it preserves the cross-DOF covariance structure that enables a downstream module to correct high-uncertainty dimensions aggressively while leaving confident predictions untouched.\nA controlled 3D point-reaching experiment confirms this: a correction MLP conditioned on per-DOF uncertainty reduces total error by 6.7\\% over scalar conditioning and by 16.7\\% over no uncertainty input, with 22--24\\% improvements concentrated on the non-perturbed axes where scalar conditioning cannot distinguish signal from noise (Section~\\ref{sec:motivating}).\n\n% Para 4: ACR-VLA overview — 3 components, key design choices\nWe introduce \\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that attaches to any frozen flow-matching VLA and performs dimension-selective action correction.\nACR-VLA comprises three components:\n(i)~\\textbf{Conformalized Gaussian Scoring (CGS)} draws $K{=}10$ samples per control step, fits a Ledoit--Wolf shrinkage covariance, and extracts a 40D structured uncertainty feature;\n(ii)~\\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency (ACI+COC)} maintains an online conformal threshold~\\cite{gibbs2021aci} using a self-referential coverage signal derived from overlapping action chunks---requiring no external supervisor, reward model, or ground-truth actions;\n(iii)~\\textbf{Conformal Refinement Module (CRM)}, a lightweight MLP (${\\sim}$337K parameters) that takes the CGS features as conditioning and outputs a dimension-selective residual correction.\nWe note that conformal prediction serves here as a \\emph{feature extraction and calibration mechanism}, not as a guarantee on the corrected output: CGS features provide structured uncertainty conditioning for CRM, while ACI+COC adapts these features online under distribution shift.\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\n\n% Para 5: Contributions — numbered list\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{Per-DOF conformal features for dimension-selective correction.}\n  We show that the 40D CGS representation---per-DOF standard deviations, calibrated conformal radii, and covariance log-volume---enables CRM to selectively correct uncertain action dimensions while preserving accurate ones.\n  On LIBERO, ACR-VLA improves base SmolVLA success by \\textbf{XX.X}\\,pp, and ablations confirm that per-DOF features outperform both scalar uncertainty and no-uncertainty baselines (Section~\\ref{sec:experiments}).\n\n  \\item \\textbf{Self-referential online calibration via Chunk Overlap Consistency.}\n  COC exploits the temporal overlap in receding-horizon action chunks to provide a coverage signal for ACI without external supervision.\n  This enables the conformal threshold to adapt online under arbitrary distribution shift, maintaining calibrated uncertainty features throughout deployment (Section~\\ref{sec:aci}).\n\n  \\item \\textbf{Systematic evaluation across multiple LIBERO task suites.}\n  We evaluate ACR-VLA on LIBERO-Spatial and LIBERO-Object, providing per-task breakdowns, ablations isolating the contribution of each component (CGS features, ACI+COC calibration, CRM architecture), and analysis of when and why dimension-selective correction helps (Section~\\ref{sec:experiments}).\n\\end{enumerate}\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
I see the introduction still has the old framing too (40D CGS features, ACI+COC, per-DOF as main contribution). But the task asks me to write the method section, not the introduction. I'll focus on the method section as specified. The introduction will need to be updated separately.

Now let me write the method section according to the task specification. Key changes from old draft:
- No ACI/COC
- No 40D CGS feature vector
- CRM takes observation embedding only (obs_only), NOT CGS features
- Argmin selection (not conformal region)


- Magnitude control emerges as the critical finding
- Per-DOF features should only appear as an ablation variant

Let me draft this carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "b58cecee-6fd3-4c31-9e35-6ec398e3be04",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSJE8TbPfWDQnfZEHzpJ5v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2098,
      "cache_read_input_tokens": 40386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2098
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

_source line 20_

<details open><summary>🔧 Tool call — Write · `toolu_01SsJgJ8EXMpYbEsAT4N4HfM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
  "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis argmin selection approximates the conformal selection strategy of ReconVLA~\\cite{chen2026reconvla}, but replaces its scalar Euclidean distance with a Mahalanobis score that accounts for cross-DOF covariance structure. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 2-layer MLP with hidden dimension 256 (${\\sim}$N parameters).% TODO: exact param count pending from checkpoint\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF features and scalar conformal scores, and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.\n\n\\paragraph{Small corrections are effective.}\nConstraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.\n\n\\paragraph{Connection to residual policy learning.}\nThe necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced bounded residual corrections for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating to selectively apply residual actions across different task phases. PLD~\\cite{xiao2026pld} schedules magnitude bounds during training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no scheduling, just a hard constraint that prevents the correction from overwhelming the base policy.\n\n\\paragraph{Differential sensitivity across CRM variants.}\nObservation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.\n  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).\n  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead consists of $K{=}10$ extra forward passes through the base VLA (shared with any multi-sample selection method such as ReconVLA~\\cite{chen2026reconvla}) plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "fc5c11cc-7b26-4f0b-921c-94f48a69c565",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSJE8TbPfWDQnfZEHzpJ5v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2098,
      "cache_read_input_tokens": 40386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2098
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

_source line 21 · 2026-05-15T19:14:41.836Z_

<details><summary>↩ Tool result · `toolu_01SsJgJ8EXMpYbEsAT4N4HfM`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "1f360d74-d2b8-4f6c-b8d8-6b35f8989b7d",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
    "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis argmin selection approximates the conformal selection strategy of ReconVLA~\\cite{chen2026reconvla}, but replaces its scalar Euclidean distance with a Mahalanobis score that accounts for cross-DOF covariance structure. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 2-layer MLP with hidden dimension 256 (${\\sim}$N parameters).% TODO: exact param count pending from checkpoint\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF features and scalar conformal scores, and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.\n\n\\paragraph{Small corrections are effective.}\nConstraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.\n\n\\paragraph{Connection to residual policy learning.}\nThe necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced bounded residual corrections for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating to selectively apply residual actions across different task phases. PLD~\\cite{xiao2026pld} schedules magnitude bounds during training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no scheduling, just a hard constraint that prevents the correction from overwhelming the base policy.\n\n\\paragraph{Differential sensitivity across CRM variants.}\nObservation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.\n  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).\n  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead consists of $K{=}10$ extra forward passes through the base VLA (shared with any multi-sample selection method such as ReconVLA~\\cite{chen2026reconvla}) plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 22_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "568f2b9e-6703-4b3e-9693-030464020695",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXjLgzG5tXedcqtp4F4Ghr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3492,
      "cache_read_input_tokens": 42484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3492
      },
      "output_tokens": 1,
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

_source line 23_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VAhCquPVHwqUyE1xAQCBv4`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "eec59e4f-dbf8-4d50-b067-817231e65713",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXjLgzG5tXedcqtp4F4Ghr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3492,
      "cache_read_input_tokens": 42484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3492
      },
      "output_tokens": 1,
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

_source line 24 · 2026-05-15T19:14:44.108Z_

<details><summary>↩ Tool result · `toolu_01VAhCquPVHwqUyE1xAQCBv4`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "816cc814-5f4e-4993-b393-0c43e2e76fbe",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 50
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01N3REWNrq9gDXaPUdLFwD6k`</summary>

```json
{
  "name": "method-section-v2",
  "type": "paper",
  "description": "Method section (Section 3) for CoRL 2026 paper. Corrected framing: obs_only CRM as main method, argmin selection baseline, magnitude control as critical finding, per-DOF as ablation variant. Replaces method_section_draft.tex.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
  "tags": [
    "paper",
    "method",
    "corl2026",
    "v2"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "70ad24e5-3b4e-4624-8c91-bd3855b562c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sn99Nxxjpd14gJm5StVmvm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 45976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
      },
      "output_tokens": 52,
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

_source line 26 · 2026-05-15T19:14:49.838Z_

<details><summary>↩ Tool result · `toolu_01N3REWNrq9gDXaPUdLFwD6k`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_fb526b\", \"name\": \"method-section-v2\", \"type\": \"paper\", \"description\": \"Method section (Section 3) for CoRL 2026 paper. Corrected framing: obs_only CRM as main method, argmin selection baseline, magnitude control as critical finding, per-DOF as ablation variant. Replaces method_section_draft.tex.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_fb526b.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T19:14:49.692917+00:00\", \"tags\": [\"paper\", \"method\", \"corl2026\", \"v2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "54a87dc2-1585-40ec-855a-c55a27add7b9",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_fb526b\\\", \\\"name\\\": \\\"method-section-v2\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Method section (Section 3) for CoRL 2026 paper. Corrected framing: obs_only CRM as main method, argmin selection baseline, magnitude control as critical finding, per-DOF as ablation variant. Replaces method_section_draft.tex.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_fb526b.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T19:14:49.692917+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"method\\\", \\\"corl2026\\\", \\\"v2\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_fb526b\", \"name\": \"method-section-v2\", \"type\": \"paper\", \"description\": \"Method section (Section 3) for CoRL 2026 paper. Corrected framing: obs_only CRM as main method, argmin selection baseline, magnitude control as critical finding, per-DOF as ablation variant. Replaces method_section_draft.tex.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_fb526b.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T19:14:49.692917+00:00\", \"tags\": [\"paper\", \"method\", \"corl2026\", \"v2\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

Method section written to `artifacts/_project/paper/method.tex`.

**Structure**: 5 subsections, 5 numbered equations, ~2 pages in CoRL format.

| Subsection | Content |
|---|---|
| 3.1 Problem Setup | Frozen VLA, 7-DOF (6 arm + gripper separate), C=50 chunks truncated to H=5 |
| 3.2 Selection | K=10 samples → Ledoit-Wolf shrinkage covariance (Eq.1) → Mahalanobis score (Eq.2) → argmin selection (Eq.3) |
| 3.3 CRM | obs_only 2-layer MLP, magnitude-bounded correction (Eq.4), L2 training loss (Eq.5), 26,737 training samples |
| 3.4 Magnitude Control | Unbounded → 0% catastrophic failure; ε=0.1 default; obs_only robust across [0.05, 0.3], perdof collapses |
| 3.5 Inference Protocol | Step-by-step pipeline, K=10 overhead + ~3ms CRM |

**Key changes from old draft**: Removed ACI/COC and 40D CGS feature vector entirely. CRM takes only observation embedding. Per-DOF features mentioned only as ablation comparisons. Argmin selection replaces conformal regions. One `% TODO` left for exact parameter count from checkpoint.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "uuid": "9403f0c9-cb8e-4a4e-9d52-99e49539386c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013S5Zwv7MGX7XPb5myy1MQk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 606,
      "cache_read_input_tokens": 46798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 606
      },
      "output_tokens": 1,
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

_source line 28_

Method section written to `artifacts/_project/paper/method.tex`.

**Structure**: 5 subsections, 5 numbered equations, ~2 pages in CoRL format.

| Subsection | Content |
|---|---|
| 3.1 Problem Setup | Frozen VLA, 7-DOF (6 arm + gripper separate), C=50 chunks truncated to H=5 |
| 3.2 Selection | K=10 samples → Ledoit-Wolf shrinkage covariance (Eq.1) → Mahalanobis score (Eq.2) → argmin selection (Eq.3) |
| 3.3 CRM | obs_only 2-layer MLP, magnitude-bounded correction (Eq.4), L2 training loss (Eq.5), 26,737 training samples |
| 3.4 Magnitude Control | Unbounded → 0% catastrophic failure; ε=0.1 default; obs_only robust across [0.05, 0.3], perdof collapses |
| 3.5 Inference Protocol | Step-by-step pipeline, K=10 overhead + ~3ms CRM |

**Key changes from old draft**: Removed ACI/COC and 40D CGS feature vector entirely. CRM takes only observation embedding. Per-DOF features mentioned only as ablation comparisons. Argmin selection replaces conformal regions. One `% TODO` left for exact parameter count from checkpoint.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 110659,
  "duration_api_ms": 113054,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "2a62dc55-f0dd-4c78-b903-0838867d5b9c",
  "total_cost_usd": 0.47009625000000005,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 35563,
    "cache_read_input_tokens": 243131,
    "output_tokens": 4944,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35563,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 353,
        "cache_read_input_tokens": 46798,
        "cache_creation_input_tokens": 606,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 606
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2517,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002612,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 4944,
      "cacheReadInputTokens": 243131,
      "cacheCreationInputTokens": 35563,
      "webSearchRequests": 0,
      "costUSD": 0.46748425000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "52743de2-93a0-41df-9b86-79900098099d"
}
```

</details>

---
