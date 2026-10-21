# paper writing related work

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260513T173628.log`
- **Structured JSON:** [`3184eee64fa309f94a75.json`](../../sessions/31/3184eee64fa309f94a75.json)

## Before a recorded user message

21 recorded events

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
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
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
  "uuid": "fbb18616-61ba-440b-b4d9-ed9c2d7703eb",
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
    "resetsAt": 1778707800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d169b2c4-4d70-475a-80e7-86dcf63733a1",
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978"
}
```

---

### Assistant

_source line 4_

I'll read the LaTeX writing skill and the method section draft first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "1bdda51d-4254-4ed5-9cb2-2ec5003d8121",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdhZkrsNrXKxSK824VoYtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13177,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13177
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

<details open><summary>🔧 Tool call — Read · `toolu_01AX5FtoSVZAckAjSq5q99sc`</summary>

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
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "7629ba15-16a9-459b-846f-323cc43bf9d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdhZkrsNrXKxSK824VoYtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13177,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13177
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

_source line 6 · 2026-05-13T17:36:40.036Z_

<details><summary>↩ Tool result · `toolu_01AX5FtoSVZAckAjSq5q99sc`</summary>

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
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "d6979d79-6cdb-4011-94f8-df76c6c119ce",
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

<details open><summary>🔧 Tool call — Read · `toolu_0147wsJ6w4zuXLRNqUt5MqkD`</summary>

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
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "24b0e295-52b0-44b7-9f3e-d8c37a156866",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KdhZkrsNrXKxSK824VoYtk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13177,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13177
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

_source line 8 · 2026-05-13T17:36:40.149Z_

<details><summary>↩ Tool result · `toolu_0147wsJ6w4zuXLRNqUt5MqkD`</summary>

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
62	We instantiate \textbf{ACR-VLA} on SmolVLA~\cite{smolvla2025}, a 450M-parameter flow-matching VLA that predicts action chunks of size 50 with action dimension $d{=}6$ (3 translation + 3 rotation; the gripper is handled separately outside the conformal pipeline).
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
96	where $\sigma_{j,h} = \sqrt{(\boldsymbol{\Sigma}_h)_{jj}}$ is the per-DOF standard deviation (30D), $q_h$ is the ACI-calibrated Mahalanobis threshold at step $h$ (5D, see \S\ref{sec:aci}), and $v_h = \tfrac{1}{2}\log\det(\boldsymbol{\Sigma}_h)$ is the log-volume of the covariance ellipsoid (5D).  Together, these encode \emph{which dimensions are uncertain} (per-DOF std), the \emph{overall calibrated confidence level} (conformal radius), and the \emph{spread of the predictive distribution} (log-volume).  Compared with the scalar Euclidean distance used in ReconVLA~\cite{reconvla2026}, this representation is strictly more informative.
97	
98	\paragraph{Epistemic vs.\ aleatoric positioning.}
99	Recent work~\cite{diu2026} shows that for flow-matching models the divergence of the velocity field recovers per-DOF aleatoric uncertainty from a single forward pass.  CGS instead estimates epistemic uncertainty via multi-sample covariance: it rises when the model is uncertain about the correct action (e.g., out-of-distribution observations), rather than reflecting irreducible task ambiguity.  For action correction, epistemic uncertainty is the more relevant signal---it identifies \emph{where the model needs help}.  We validate this distinction empirically in ablation~A7.
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
141	CRM is a 2-layer MLP with hidden dimension 256 (${\sim}$250K parameters).  Its input concatenates three sources:
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
157	on demonstration trajectories from LIBERO~\cite{liberoplus2025} augmented with synthetic perturbations (camera shifts, sensor noise, robot-state perturbation, lighting and background variation).  During training, CGS features are computed online: for each augmented observation, we run $K{=}10$ forward passes through the frozen base VLA and extract $\boldsymbol{\varphi}_{\mathrm{CGS}}$.  This ensures CRM sees realistic uncertainty patterns that co-vary with the perturbation type---for instance, camera shifts produce elevated translational variance while leaving rotational variance largely unchanged.
158	
159	ACI operates exclusively at inference time: it adjusts the conformal threshold $q_h$, which enters CRM through the conformal-radius components of $\boldsymbol{\varphi}_{\mathrm{CGS}}$.  This decoupling of training and calibration eliminates the multi-objective conflicts that arise when calibration-aware losses compete with the primary correction objective in a small-capacity network~\cite{cploop2025}.
160	
161	\paragraph{Why per-DOF conditioning enables selective correction.}
162	To build intuition, consider a camera perturbation that introduces translational ambiguity in the $x$-$y$ plane while leaving $z$-translation and rotation well-determined.  A scalar nonconformity score (e.g., average Euclidean sample distance, as in \cite{reconvla2026}) compresses this into ``moderate uncertainty everywhere,'' providing no basis for selective correction.  The per-DOF structure in $\boldsymbol{\varphi}_{\mathrm{CGS}}$ instead reveals that $\sigma_{x},\sigma_{y} \gg \sigma_{z},\sigma_{\mathrm{rot}}$, enabling CRM to apply large corrections to the uncertain translational axes while preserving the base VLA's accurate rotational predictions.  Section~\ref{sec:motivating} validates this mechanism in a controlled setting; Section~\ref{sec:experiments} demonstrates it on real VLA tasks.
163	
164	\paragraph{Inference protocol.}
165	Each control step proceeds as: draw $K{=}10$ samples $\to$ compute CGS $\to$ apply CRM $\to$ execute the first action of the refined chunk $\to$ observe new state $\to$ draw $K{=}10$ fresh samples $\to$ compute COC (\ref{eq:coc}) $\to$ ACI update (\ref{eq:aci_update}).  The entire module adds ${\sim}$250K parameters and $K{=}10$ extra forward passes to the base VLA, with no retraining of the base model.
166	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "57c9fe16-d916-4369-9714-81144e14a63c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_section_draft.tex",
      "content": "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%% Section 3 -- Motivating Experiment\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\section{Motivating Experiment}\n\\label{sec:motivating}\n\nBefore committing to the full \\textbf{ACR-VLA} pipeline, we ask a targeted question: \\emph{does per-DOF uncertainty carry more actionable information for correction than a scalar summary?}  We design a controlled 3D point-reaching experiment that isolates this factor.\n\n\\paragraph{Setup.}\nA synthetic policy outputs actions $a\\in\\mathbb{R}^{3}$ with known anisotropic Gaussian noise: $\\sigma_x{=}0.5,\\;\\sigma_y{=}0.1,\\;\\sigma_z{=}0.1$, simulating the depth ambiguity a monocular camera introduces along the $x$-axis.  At test time a target shift of $+0.3$ is applied along $x$, creating a systematic perturbation whose correction should be modulated by uncertainty structure.\n\nWe train three correction MLPs (2 layers, hidden dim 64, 20{,}000 training samples), differing only in their uncertainty conditioning:\n\\begin{itemize}[nosep]\n  \\item \\textbf{Model A} (scalar): conditioned on the average standard deviation $\\bar{\\sigma}=\\tfrac{1}{3}\\sum_j\\sigma_j$.\n  \\item \\textbf{Model B} (per-DOF): conditioned on the full vector $[\\sigma_x,\\sigma_y,\\sigma_z]$.\n  \\item \\textbf{Model C} (none): conditioned on observation features only, with no uncertainty input.\n\\end{itemize}\nTo match the regime of our full pipeline, where ground-truth variances are unavailable, we report results with \\emph{estimated} uncertainty computed from $K{=}10$ samples (the same budget used in \\textbf{ACR-VLA}).\n\n\\paragraph{Results.}\nTable~\\ref{tab:motivating} reports per-axis MSE over 5{,}000 test episodes at a 5:1 anisotropy ratio ($\\sigma_x/\\sigma_y$) with $K{=}10$ estimated uncertainty.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-axis MSE ($\\downarrow$) of correction models on the 3D point-reaching task (5:1 anisotropy, $K{=}10$ estimated uncertainty). Model~B, which receives per-DOF uncertainty, preserves accuracy on the low-uncertainty axes ($y,z$) where Model~A and~C over-correct.}\n\\label{tab:motivating}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nModel & Conditioning & MSE$_x$ & MSE$_y$ & MSE$_z$ & Total MSE \\\\\n\\midrule\nA & scalar $\\bar\\sigma$ & 0.1874 & 0.0247 & 0.0243 & 0.0788 \\\\\n\\textbf{B} & \\textbf{per-DOF} $[\\sigma_x,\\sigma_y,\\sigma_z]$ & \\textbf{0.1829} & \\textbf{0.0191} & \\textbf{0.0185} & \\textbf{0.0735} \\\\\nC & none & 0.2151 & 0.0250 & 0.0246 & 0.0882 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nModel~B reduces total MSE by 6.7\\% relative to~A and by 16.7\\% relative to~C.  The gains concentrate on the non-perturbed axes: $y$- and $z$-axis MSE drop by 22.7\\% and 23.9\\% versus~A, indicating that Model~B learns to leave low-uncertainty dimensions largely untouched while directing correction effort toward the high-uncertainty $x$-axis.  Model~A, receiving only a scalar average, lacks the information to make this distinction and applies a uniform correction that degrades the already-accurate axes.\n\nWith oracle (ground-truth) variances, the ranking $\\text{B}>\\text{A}>\\text{C}$ is preserved with larger margins (non-perturbed axis improvements of 30--38\\% over~A).  Moving from oracle to $K{=}10$ estimation reduces relative gains by roughly 15 percentage points, reflecting finite-sample noise, but does not alter the ordering.  The pattern also holds at weaker anisotropy ratios (2:1 and 1.5:1): across all six conditions tested, Model~B consistently outperforms both baselines.\n\n\\paragraph{Takeaway.}\nEven a simple MLP can exploit per-DOF uncertainty structure for dimension-selective correction---a capability that scalar summaries cannot provide.  This motivates the design of \\textbf{ACR-VLA}, which extracts rich per-DOF features from a flow-matching VLA and feeds them into a learned correction module (Section~\\ref{sec:method}).\n\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n%% Section 4 -- Method\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA) is an inference-time, post-hoc module that attaches to any flow-matching VLA without modifying its weights.  It comprises three components (Figure~\\ref{fig:pipeline}):\n\\begin{enumerate}[nosep]\n  \\item \\textbf{Conformalized Gaussian Scoring} (CGS, \\S\\ref{sec:cgs}): draws $K{=}10$ action samples per step, fits a shrinkage-regularized Gaussian, and extracts a 40-dimensional structured uncertainty feature.\n  \\item \\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency} (ACI+COC, \\S\\ref{sec:aci}): maintains an online conformal threshold that adapts to distribution shift using a self-referential coverage signal from overlapping action chunks.\n  \\item \\textbf{Conformal Refinement Module} (CRM, \\S\\ref{sec:crm}): a lightweight MLP that takes the CGS features as conditioning and outputs a dimension-selective residual correction.\n\\end{enumerate}\n\nWe instantiate \\textbf{ACR-VLA} on SmolVLA~\\cite{smolvla2025}, a 450M-parameter flow-matching VLA that predicts action chunks of size 50 with action dimension $d{=}6$ (3 translation + 3 rotation; the gripper is handled separately outside the conformal pipeline).\n\n\n%%% 4.1 CGS %%%\n\\subsection{Conformalized Gaussian Scoring}\n\\label{sec:cgs}\n\nCGS converts a set of stochastic action samples from the base VLA into a compact uncertainty descriptor that captures \\emph{which} degrees of freedom are uncertain and \\emph{how} they co-vary---information that a scalar nonconformity score discards.\n\n\\paragraph{Sampling and truncation.}\nAt each control step, we draw $K{=}10$ action chunks from the frozen base VLA via independent flow-matching rollouts.  Although SmolVLA predicts 50-step chunks, under receding-horizon execution only the first few steps influence the robot before re-planning.  We therefore retain only the first $H{=}5$ steps, yielding $K$ samples $\\{a_h^{(k)}\\}_{k=1}^{K}$ with $a_h^{(k)}\\in\\mathbb{R}^{d}$ for each horizon step $h=1,\\dots,H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1-\\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity.  With a dimension-to-sample ratio $p/n = d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error due to the Marchenko--Pastur effect; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nWe define a joint multivariate nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis single score captures cross-DOF covariance structure.  In contrast, treating each DOF independently and applying Bonferroni correction across all $d{\\times}H = 30$ marginals yields intervals that are substantially wider than necessary.  Our joint formulation requires Bonferroni correction only across $H{=}5$ horizon steps (target level $\\alpha/H$ per step), preserving tight per-step regions~\\cite{braun2025cgs}.\n\n\\paragraph{CGS feature vector.}\nWe assemble a 40-dimensional feature $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$ that is passed to the refinement module:\n\\begin{equation}\n  \\boldsymbol{\\varphi}_{\\mathrm{CGS}} = \\bigl[\\,\\underbrace{\\sigma_{j,h}}_{j=1..d,\\;h=1..H}\\;;\\;\\underbrace{q_h}_{h=1..H}\\;;\\;\\underbrace{v_h}_{h=1..H}\\,\\bigr] \\;\\in\\;\\mathbb{R}^{40},\n  \\label{eq:cgs_feat}\n\\end{equation}\nwhere $\\sigma_{j,h} = \\sqrt{(\\boldsymbol{\\Sigma}_h)_{jj}}$ is the per-DOF standard deviation (30D), $q_h$ is the ACI-calibrated Mahalanobis threshold at step $h$ (5D, see \\S\\ref{sec:aci}), and $v_h = \\tfrac{1}{2}\\log\\det(\\boldsymbol{\\Sigma}_h)$ is the log-volume of the covariance ellipsoid (5D).  Together, these encode \\emph{which dimensions are uncertain} (per-DOF std), the \\emph{overall calibrated confidence level} (conformal radius), and the \\emph{spread of the predictive distribution} (log-volume).  Compared with the scalar Euclidean distance used in ReconVLA~\\cite{reconvla2026}, this representation is strictly more informative.\n\n\\paragraph{Epistemic vs.\\ aleatoric positioning.}\nRecent work~\\cite{diu2026} shows that for flow-matching models the divergence of the velocity field recovers per-DOF aleatoric uncertainty from a single forward pass.  CGS instead estimates epistemic uncertainty via multi-sample covariance: it rises when the model is uncertain about the correct action (e.g., out-of-distribution observations), rather than reflecting irreducible task ambiguity.  For action correction, epistemic uncertainty is the more relevant signal---it identifies \\emph{where the model needs help}.  We validate this distinction empirically in ablation~A7.\n\n\n%%% 4.2 ACI + COC %%%\n\\subsection{Adaptive Conformal Inference via Chunk Overlap Consistency}\n\\label{sec:aci}\n\nCGS requires a conformal threshold $q_h$ to convert Mahalanobis scores into calibrated prediction regions.  Static calibration on a held-out set, as in conformal quantile regression~\\cite{romano2019cqr}, assumes exchangeability between calibration and deployment data---an assumption that breaks under the distribution shifts common in real-world manipulation.  We instead adopt Adaptive Conformal Inference (ACI)~\\cite{gibbs2021aci}, which provides long-run coverage guarantees under arbitrary distribution shift, and equip it with a novel self-referential coverage signal.\n\n\\paragraph{The coverage signal problem.}\nACI updates the miscoverage level $\\alpha_t$ at each step based on whether the true action falls inside the conformal region.  In robotics, the most direct signal would check whether the \\emph{executed} action lies within the predicted region.  However, contact dynamics cause the achieved end-effector displacement to differ from the commanded action, corrupting this signal.\n\n\\paragraph{Chunk Overlap Consistency (COC).}\nWe exploit the temporal overlap inherent in receding-horizon action chunking.  At control step $t$, the VLA predicts a chunk $[a_t^1,\\dots,a_t^H]$ with associated conformal ellipsoids $\\{C_t^h\\}_{h=1}^H$ derived from the Mahalanobis score (\\ref{eq:mahal}) and threshold $q_h$.  After executing $a_t^1$ and observing the new state $s_{t+1}$, we draw $K{=}10$ fresh samples and compute the new first-step mean $\\boldsymbol{\\mu}_{t+1}^1$.  The COC coverage indicator is:\n\\begin{equation}\n  \\mathrm{err}_t = \\mathbb{1}\\bigl[\\boldsymbol{\\mu}_{t+1}^1 \\notin C_t^2\\bigr],\n  \\label{eq:coc}\n\\end{equation}\ni.e., we check whether the next step's predicted action falls within the \\emph{previous} step's conformal region for the overlapping horizon position.\n\nCOC has four properties that make it well-suited for online calibration:\n(i)~it is self-referential, requiring no external supervisor or trained reward model;\n(ii)~it compares prediction-to-prediction rather than prediction-to-execution, making it robust to contact dynamics;\n(iii)~it directly measures calibration quality---whether the conformal regions are appropriately sized;\n(iv)~it produces a signal at every control step, not only at episode boundaries.\n\n\\paragraph{Online update rule.}\nThe ACI update follows \\cite{gibbs2021aci}:\n\\begin{equation}\n  \\alpha_{t+1} = \\alpha_t + \\gamma\\bigl(\\alpha_{\\mathrm{target}} - \\mathrm{err}_t\\bigr),\n  \\label{eq:aci_update}\n\\end{equation}\nwhere $\\gamma$ is the learning rate and $\\alpha_{\\mathrm{target}}$ is the desired miscoverage rate.  When $\\mathrm{err}_t{=}1$ (the region failed to cover), $\\alpha_{t+1}$ decreases, widening the next region; when $\\mathrm{err}_t{=}0$, $\\alpha_{t+1}$ increases, tightening it.  Within each episode, we apply exponentially weighted conformal prediction~\\cite{barber2023conformal} with decay parameter $\\rho$ to down-weight stale calibration data.  Across episodes, the fraction of intra-episode COC hits serves as $\\mathrm{err}_t$ for a cross-episode ACI update, enabling the threshold to adapt over the course of deployment.\n\n\n%%% 4.3 CRM %%%\n\\subsection{Conformal Refinement Module}\n\\label{sec:crm}\n\nThe Conformal Refinement Module (CRM) is a lightweight network that performs dimension-selective action correction, conditioned on the structured uncertainty features from CGS.\n\n\\paragraph{Architecture.}\nCRM is a 2-layer MLP with hidden dimension 256 (${\\sim}$250K parameters).  Its input concatenates three sources:\n(i)~the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ from the base VLA encoder,\n(ii)~the 40D CGS feature $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$, and\n(iii)~the mean action $\\boldsymbol{\\mu} \\in \\mathbb{R}^{30}$ ($d{\\times}H = 6{\\times}5$).\nThe output is a residual correction $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the refined action is:\n\\begin{equation}\n  \\mathbf{a}^* = \\boldsymbol{\\mu} + \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}},\\;\\boldsymbol{\\varphi}_{\\mathrm{CGS}},\\;\\boldsymbol{\\mu}).\n  \\label{eq:crm}\n\\end{equation}\n\n\\paragraph{Training.}\nCRM is trained with a single objective:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,\n  \\label{eq:crm_loss}\n\\end{equation}\non demonstration trajectories from LIBERO~\\cite{liberoplus2025} augmented with synthetic perturbations (camera shifts, sensor noise, robot-state perturbation, lighting and background variation).  During training, CGS features are computed online: for each augmented observation, we run $K{=}10$ forward passes through the frozen base VLA and extract $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$.  This ensures CRM sees realistic uncertainty patterns that co-vary with the perturbation type---for instance, camera shifts produce elevated translational variance while leaving rotational variance largely unchanged.\n\nACI operates exclusively at inference time: it adjusts the conformal threshold $q_h$, which enters CRM through the conformal-radius components of $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$.  This decoupling of training and calibration eliminates the multi-objective conflicts that arise when calibration-aware losses compete with the primary correction objective in a small-capacity network~\\cite{cploop2025}.\n\n\\paragraph{Why per-DOF conditioning enables selective correction.}\nTo build intuition, consider a camera perturbation that introduces translational ambiguity in the $x$-$y$ plane while leaving $z$-translation and rotation well-determined.  A scalar nonconformity score (e.g., average Euclidean sample distance, as in \\cite{reconvla2026}) compresses this into ``moderate uncertainty everywhere,'' providing no basis for selective correction.  The per-DOF structure in $\\boldsymbol{\\varphi}_{\\mathrm{CGS}}$ instead reveals that $\\sigma_{x},\\sigma_{y} \\gg \\sigma_{z},\\sigma_{\\mathrm{rot}}$, enabling CRM to apply large corrections to the uncertain translational axes while preserving the base VLA's accurate rotational predictions.  Section~\\ref{sec:motivating} validates this mechanism in a controlled setting; Section~\\ref{sec:experiments} demonstrates it on real VLA tasks.\n\n\\paragraph{Inference protocol.}\nEach control step proceeds as: draw $K{=}10$ samples $\\to$ compute CGS $\\to$ apply CRM $\\to$ execute the first action of the refined chunk $\\to$ observe new state $\\to$ draw $K{=}10$ fresh samples $\\to$ compute COC (\\ref{eq:coc}) $\\to$ ACI update (\\ref{eq:aci_update}).  The entire module adds ${\\sim}$250K parameters and $K{=}10$ extra forward passes to the base VLA, with no retraining of the base model.\n",
      "numLines": 166,
      "startLine": 1,
      "totalLines": 166
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the method and the writing conventions. Let me write the Related Work section based on the detailed instructions provided.

Key points from the method section that inform the Related Work:
1. ACR-VLA is inference-time, post-hoc, doesn't modify base VLA weights
2. CGS extracts 40D per-DOF features from multi-sample flow-matching
3. ACI+COC provides online calibration under distribution shift
4. CRM does dimension-selective correction conditioned on CGS features
5. Built on SmolVLA (flow-matching VLA)


6. Key distinctions: per-DOF vs scalar, epistemic vs aleatoric, learned correction vs sample selection, continuous features vs binary decision

Now I'm structuring the Related Work section into four paragraphs. First, I'll cover VLA robustness methods like SRPO, RobustVLA, DiG-Flow, SnapFlow, TT-VLA, VLA-GSE, and Cosmos-Policy, emphasizing how ACR-VLA complements these training-time approaches with its inference-time post-hoc design. Then I'll move into uncertainty quantification for robot learning, followed by sections on calibration and distribution shift, and finally dimension-selective correction methods. The next thinking appears to be empty, so I'll output nothing and let the current rewritten thinking stand as is.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "e3cc11aa-57b0-4fc4-8fc7-58698adc7047",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHbzXEahtkuUg9iQXaTXSA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11045,
      "cache_read_input_tokens": 25018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11045
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

Now let me check the target directory exists and write the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "2fb68264-7d47-4b3c-8775-ab70b3660bd7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHbzXEahtkuUg9iQXaTXSA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11045,
      "cache_read_input_tokens": 25018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11045
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

<details open><summary>🔧 Tool call — Bash · `toolu_01SeJsPF4Wpr1ZSAuJczPgxW`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "445a38eb-d2ef-46ab-ba41-9c2200868fbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHbzXEahtkuUg9iQXaTXSA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11045,
      "cache_read_input_tokens": 25018,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11045
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

_source line 12 · 2026-05-13T17:36:59.270Z_

<details><summary>↩ Tool result · `toolu_01SeJsPF4Wpr1ZSAuJczPgxW`</summary>

```text
method_section_draft.tex
references.bib
references_e9d4d2.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "042e6a42-549d-401b-8780-e91b86442a24",
  "tool_use_result": {
    "stdout": "method_section_draft.tex\nreferences.bib\nreferences_e9d4d2.bib",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Write · `toolu_01GSt7Effd8CqF4TRqRuBd2A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{VLA Robustness Methods.}\nRecent work has sought to improve the robustness of vision-language-action models through training-time interventions.\nSRPO~\\cite{srpo2025} applies self-referential reinforcement learning to fine-tune VLA policies, achieving strong gains on the LIBERO-Plus benchmark.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.\nDiG-Flow~\\cite{digflow2025} introduces discrepancy-guided flow matching, steering the generative process toward more accurate denoising trajectories during training.\nSnapFlow~\\cite{luan2026snapflow} distills multi-step flow-matching into single-step inference, reducing latency while preserving action quality.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time via reinforcement learning, blurring the line between training-time and inference-time approaches.\nVLA-GSE~\\cite{vla_gse_2026} improves generalization through parameter-efficient fine-tuning with gated sparse experts, and Cosmos-Policy~\\cite{cosmos_policy_2026} leverages video foundation models for visuomotor control.\nThese methods are complementary to ACR-VLA: they improve the base policy itself, whereas ACR-VLA operates as a post-hoc inference-time module that attaches to any frozen flow-matching VLA without modifying its weights.\nThis orthogonality means ACR-VLA can be composed with any of the above methods to provide additional robustness through uncertainty-conditioned correction.\n\n\\paragraph{Uncertainty Quantification for Robot Learning.}\nQuantifying predictive uncertainty in learned policies is essential for safe deployment.\nDeep Ensembles~\\cite{lakshminarayanan2017ensembles} and MC-Dropout~\\cite{gal2016dropout} are foundational approaches that estimate epistemic uncertainty through multiple forward passes or stochastic weight perturbations, but both produce scalar or loosely structured uncertainty estimates that do not distinguish which action dimensions are uncertain.\nIn the generative policy setting, Diffusion Policy~\\cite{chi2023diffusion_policy} introduced the diffusion-based action generation paradigm that flow-matching VLAs build upon; its stochastic sampling naturally admits multi-sample uncertainty estimation, though the original work does not exploit this for correction.\nDiU~\\cite{xing2026diu} shows that for flow-matching models, the divergence of the velocity field recovers per-DOF \\emph{aleatoric} uncertainty from a single forward pass, providing an efficient uncertainty signal without additional sampling.\nACR-VLA differs along two axes.\nFirst, it estimates \\emph{epistemic} uncertainty via multi-sample covariance---a signal that identifies where the model lacks knowledge rather than where the task is inherently ambiguous---which is more relevant for action correction.\nSecond, it produces a structured 40-dimensional feature vector (per-DOF standard deviations, calibrated conformal radii, and log-volume) rather than a scalar summary, enabling dimension-selective correction as demonstrated in Section~\\ref{sec:motivating}.\n\n\\paragraph{Conformal Prediction in Robotics.}\nConformal prediction (CP) provides distribution-free coverage guarantees and has seen growing adoption in robotics.\n\\citet{angelopoulos2023gentle} provide a comprehensive tutorial on the framework.\nConformalized Quantile Regression~\\cite{romano2019cqr} extends CP to heteroscedastic settings, while Adaptive Conformal Inference~\\cite{gibbs2021aci} maintains coverage under distribution shift through online threshold updates---a property critical for non-stationary robotic environments.\n\\citet{barber2023conformal} further relax the exchangeability assumption, enabling conformal methods under general temporal dependence.\nBraun et al.~\\cite{braun2025cgs} introduce Conformalized Gaussian Scoring for multivariate prediction regions, which ACR-VLA builds upon for its per-DOF feature extraction.\nIn robotics applications, CP-in-the-Loop~\\cite{wang2025cploop} integrates conformal regions into trajectory optimization as constraints, and Conformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to provide safety guarantees during shared autonomy.\nUPS~\\cite{yuan2026ups} employs CP for binary policy gating---deciding whether to execute or abstain---while SAFE~\\cite{gu2025safe} uses anomaly detection to trigger safe fallback behaviors.\nA common thread in these systems is that CP serves as a \\emph{binary decision mechanism} (accept/reject, execute/abstain, safe/unsafe).\nACR-VLA departs from this paradigm by using conformal statistics as \\emph{continuous input features} to a learned correction module, enabling graded, dimension-selective refinement rather than all-or-nothing decisions.\n\n\\paragraph{Inference-Time Action Correction.}\nThe most closely related line of work addresses action refinement at inference time without retraining the base policy.\nA2C2~\\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's action chunk generation, reducing effective latency.\nHowever, A2C2 applies a generic residual without uncertainty conditioning: it has no mechanism to modulate correction magnitude based on per-dimension confidence, which can lead to unnecessary perturbation of already-accurate action components.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean based on scalar Euclidean distance, using this distance as a proxy for uncertainty.\nWhile effective as a variance-reduction strategy, sample selection is fundamentally limited: it cannot synthesize an action better than any individual sample, and its scalar uncertainty measure does not distinguish which degrees of freedom are unreliable.\nACR-VLA addresses both limitations.\nCompared to A2C2, it conditions correction on calibrated per-DOF conformal features, enabling the refinement module to selectively correct high-uncertainty dimensions while preserving accurate predictions on others.\nCompared to ReconVLA, it performs learned synthesis rather than selection, producing corrections that can improve upon any individual sample, and replaces the scalar Euclidean proxy with a 40-dimensional structured representation that captures per-DOF variance, calibrated confidence, and distributional volume.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "f545015c-ec84-46e8-9996-8dfeb92ba92c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MT936Z388x4pRma7G9mP2S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 688,
      "cache_read_input_tokens": 36063,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 688
      },
      "output_tokens": 53,
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

_source line 14 · 2026-05-13T17:37:38.122Z_

<details><summary>↩ Tool result · `toolu_01GSt7Effd8CqF4TRqRuBd2A`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "08111f7d-6ea7-4e55-82ee-14a157cb100e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{VLA Robustness Methods.}\nRecent work has sought to improve the robustness of vision-language-action models through training-time interventions.\nSRPO~\\cite{srpo2025} applies self-referential reinforcement learning to fine-tune VLA policies, achieving strong gains on the LIBERO-Plus benchmark.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.\nDiG-Flow~\\cite{digflow2025} introduces discrepancy-guided flow matching, steering the generative process toward more accurate denoising trajectories during training.\nSnapFlow~\\cite{luan2026snapflow} distills multi-step flow-matching into single-step inference, reducing latency while preserving action quality.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time via reinforcement learning, blurring the line between training-time and inference-time approaches.\nVLA-GSE~\\cite{vla_gse_2026} improves generalization through parameter-efficient fine-tuning with gated sparse experts, and Cosmos-Policy~\\cite{cosmos_policy_2026} leverages video foundation models for visuomotor control.\nThese methods are complementary to ACR-VLA: they improve the base policy itself, whereas ACR-VLA operates as a post-hoc inference-time module that attaches to any frozen flow-matching VLA without modifying its weights.\nThis orthogonality means ACR-VLA can be composed with any of the above methods to provide additional robustness through uncertainty-conditioned correction.\n\n\\paragraph{Uncertainty Quantification for Robot Learning.}\nQuantifying predictive uncertainty in learned policies is essential for safe deployment.\nDeep Ensembles~\\cite{lakshminarayanan2017ensembles} and MC-Dropout~\\cite{gal2016dropout} are foundational approaches that estimate epistemic uncertainty through multiple forward passes or stochastic weight perturbations, but both produce scalar or loosely structured uncertainty estimates that do not distinguish which action dimensions are uncertain.\nIn the generative policy setting, Diffusion Policy~\\cite{chi2023diffusion_policy} introduced the diffusion-based action generation paradigm that flow-matching VLAs build upon; its stochastic sampling naturally admits multi-sample uncertainty estimation, though the original work does not exploit this for correction.\nDiU~\\cite{xing2026diu} shows that for flow-matching models, the divergence of the velocity field recovers per-DOF \\emph{aleatoric} uncertainty from a single forward pass, providing an efficient uncertainty signal without additional sampling.\nACR-VLA differs along two axes.\nFirst, it estimates \\emph{epistemic} uncertainty via multi-sample covariance---a signal that identifies where the model lacks knowledge rather than where the task is inherently ambiguous---which is more relevant for action correction.\nSecond, it produces a structured 40-dimensional feature vector (per-DOF standard deviations, calibrated conformal radii, and log-volume) rather than a scalar summary, enabling dimension-selective correction as demonstrated in Section~\\ref{sec:motivating}.\n\n\\paragraph{Conformal Prediction in Robotics.}\nConformal prediction (CP) provides distribution-free coverage guarantees and has seen growing adoption in robotics.\n\\citet{angelopoulos2023gentle} provide a comprehensive tutorial on the framework.\nConformalized Quantile Regression~\\cite{romano2019cqr} extends CP to heteroscedastic settings, while Adaptive Conformal Inference~\\cite{gibbs2021aci} maintains coverage under distribution shift through online threshold updates---a property critical for non-stationary robotic environments.\n\\citet{barber2023conformal} further relax the exchangeability assumption, enabling conformal methods under general temporal dependence.\nBraun et al.~\\cite{braun2025cgs} introduce Conformalized Gaussian Scoring for multivariate prediction regions, which ACR-VLA builds upon for its per-DOF feature extraction.\nIn robotics applications, CP-in-the-Loop~\\cite{wang2025cploop} integrates conformal regions into trajectory optimization as constraints, and Conformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to provide safety guarantees during shared autonomy.\nUPS~\\cite{yuan2026ups} employs CP for binary policy gating---deciding whether to execute or abstain---while SAFE~\\cite{gu2025safe} uses anomaly detection to trigger safe fallback behaviors.\nA common thread in these systems is that CP serves as a \\emph{binary decision mechanism} (accept/reject, execute/abstain, safe/unsafe).\nACR-VLA departs from this paradigm by using conformal statistics as \\emph{continuous input features} to a learned correction module, enabling graded, dimension-selective refinement rather than all-or-nothing decisions.\n\n\\paragraph{Inference-Time Action Correction.}\nThe most closely related line of work addresses action refinement at inference time without retraining the base policy.\nA2C2~\\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's action chunk generation, reducing effective latency.\nHowever, A2C2 applies a generic residual without uncertainty conditioning: it has no mechanism to modulate correction magnitude based on per-dimension confidence, which can lead to unnecessary perturbation of already-accurate action components.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean based on scalar Euclidean distance, using this distance as a proxy for uncertainty.\nWhile effective as a variance-reduction strategy, sample selection is fundamentally limited: it cannot synthesize an action better than any individual sample, and its scalar uncertainty measure does not distinguish which degrees of freedom are unreliable.\nACR-VLA addresses both limitations.\nCompared to A2C2, it conditions correction on calibrated per-DOF conformal features, enabling the refinement module to selectively correct high-uncertainty dimensions while preserving accurate predictions on others.\nCompared to ReconVLA, it performs learned synthesis rather than selection, producing corrections that can improve upon any individual sample, and replaces the scalar Euclidean proxy with a 40-dimensional structured representation that captures per-DOF variance, calibrated confidence, and distributional volume.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 15_

Now let me register this artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "47311b96-c2c8-44f3-bb27-e2071d4a7dfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01He959BsjJFao4BKrmPVR5w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 36751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1689
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

_source line 16_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01L3D7gPu8kFpWYgkKcydvZv`</summary>

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
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "ce4acb64-e653-4e1f-b88c-3ffbdae31f9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01He959BsjJFao4BKrmPVR5w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1689,
      "cache_read_input_tokens": 36751,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1689
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

_source line 17 · 2026-05-13T17:37:45.556Z_

<details><summary>↩ Tool result · `toolu_01L3D7gPu8kFpWYgkKcydvZv`</summary>

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
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "6b1a2dea-74de-4040-bd61-5e45f7e695f6",
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

_source line 18_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_017sdsp8UnweWQMn9zjwDN8Y`</summary>

```json
{
  "name": "related_work_section",
  "type": "paper",
  "description": "Related Work section for ACR-VLA paper, covering 4 paragraphs: VLA Robustness Methods, Uncertainty Quantification, Conformal Prediction in Robotics, Inference-Time Action Correction",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
  "tags": [
    "paper",
    "related-work",
    "latex"
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
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "df10b9b0-b906-48bd-b303-32d09e39862d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PzdcE6dtRwpJn72fZUNTe1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 38440,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
      },
      "output_tokens": 53,
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

_source line 19 · 2026-05-13T17:37:51.402Z_

<details><summary>↩ Tool result · `toolu_017sdsp8UnweWQMn9zjwDN8Y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_9c2927\", \"name\": \"related_work_section\", \"type\": \"paper\", \"description\": \"Related Work section for ACR-VLA paper, covering 4 paragraphs: VLA Robustness Methods, Uncertainty Quantification, Conformal Prediction in Robotics, Inference-Time Action Correction\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_9c2927.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-13T17:37:51.382451+00:00\", \"tags\": [\"paper\", \"related-work\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "ca20ab2b-390e-4a3e-ad74-e8a9eccf2df7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260513_9c2927\\\", \\\"name\\\": \\\"related_work_section\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Related Work section for ACR-VLA paper, covering 4 paragraphs: VLA Robustness Methods, Uncertainty Quantification, Conformal Prediction in Robotics, Inference-Time Action Correction\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_9c2927.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-13T17:37:51.382451+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"related-work\\\", \\\"latex\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260513_9c2927\", \"name\": \"related_work_section\", \"type\": \"paper\", \"description\": \"Related Work section for ACR-VLA paper, covering 4 paragraphs: VLA Robustness Methods, Uncertainty Quantification, Conformal Prediction in Robotics, Inference-Time Action Correction\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_9c2927.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-13T17:37:51.382451+00:00\", \"tags\": [\"paper\", \"related-work\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

Related Work section 已写入 `artifacts/_project/paper/related_work.tex`，共 4 段约 870 words：

1. **VLA Robustness Methods** — 覆盖 SRPO/RobustVLA/DiG-Flow/SnapFlow/TT-VLA/VLA-GSE/Cosmos-Policy，强调 training-time 与 ACR-VLA inference-time 的正交互补性
2. **Uncertainty Quantification for Robot Learning** — 覆盖 Deep Ensembles/MC-Dropout/Diffusion Policy/DiU，区分 scalar vs per-DOF、aleatoric vs epistemic、single-pass vs multi-sample
3. **Conformal Prediction in Robotics** — 覆盖 CP 基础理论（Angelopoulos/Romano CQR/Gibbs ACI/Barber）和应用（CP-in-the-Loop/Conformalized Teleoperation/UPS/SAFE/Braun CGS），论点：CP 作为 binary decision vs 作为 continuous features for learned correction
4. **Inference-Time Action Correction** — 与 A2C2（generic residual, no uncertainty conditioning）和 ReconVLA（scalar distance, sample selection only）做精确对比

所有引用严格使用提供的 bibtex_key 列表，未编造任何引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "uuid": "4997fb49-1ec3-4390-81ba-37160185aed5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cuh1bQf6cWD4ENcKqeyKoc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 39160,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 577
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

_source line 21_

Related Work section 已写入 `artifacts/_project/paper/related_work.tex`，共 4 段约 870 words：

1. **VLA Robustness Methods** — 覆盖 SRPO/RobustVLA/DiG-Flow/SnapFlow/TT-VLA/VLA-GSE/Cosmos-Policy，强调 training-time 与 ACR-VLA inference-time 的正交互补性
2. **Uncertainty Quantification for Robot Learning** — 覆盖 Deep Ensembles/MC-Dropout/Diffusion Policy/DiU，区分 scalar vs per-DOF、aleatoric vs epistemic、single-pass vs multi-sample
3. **Conformal Prediction in Robotics** — 覆盖 CP 基础理论（Angelopoulos/Romano CQR/Gibbs ACI/Barber）和应用（CP-in-the-Loop/Conformalized Teleoperation/UPS/SAFE/Braun CGS），论点：CP 作为 binary decision vs 作为 continuous features for learned correction
4. **Inference-Time Action Correction** — 与 A2C2（generic residual, no uncertainty conditioning）和 ReconVLA（scalar distance, sample selection only）做精确对比

所有引用严格使用提供的 bibtex_key 列表，未编造任何引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 87577,
  "duration_api_ms": 88423,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "9d91cb51-ad66-48d3-bf78-275c4fed0978",
  "total_cost_usd": 0.3499675,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 27896,
    "cache_read_input_tokens": 187273,
    "output_tokens": 3170,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27896,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 357,
        "cache_read_input_tokens": 39160,
        "cache_creation_input_tokens": 577,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 577
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2591,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002686,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 3170,
      "cacheReadInputTokens": 187273,
      "cacheCreationInputTokens": 27896,
      "webSearchRequests": 0,
      "costUSD": 0.34728149999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bd642a2c-e08a-44c7-9408-e32fe63f3bb2"
}
```

</details>

---
