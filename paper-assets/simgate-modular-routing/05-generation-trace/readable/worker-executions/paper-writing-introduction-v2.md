# paper writing introduction v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_writing_introduction_v2_20260514T093915.log`
- **Structured JSON:** [`4be073dd5b5f575b9131.json`](../../sessions/4b/4be073dd5b5f575b9131.json)

## Before a recorded user message

25 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
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
  "uuid": "0125e5bb-c21a-4549-a6ac-0d5a89a1eedc",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779303600,
    "rateLimitType": "seven_day",
    "utilization": 0.3,
    "isUsingOverage": false
  },
  "uuid": "9a3d1253-a669-4092-98a7-1674fe018b22",
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3"
}
```

---

### Assistant

_source line 4_

I'll read the LaTeX writing skill first, then draft the introduction.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "6366db5b-a574-47fc-a661-f0118a3b8a3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uXeKpaAsrVbxLVN4VWVB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12651
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

<details open><summary>🔧 Tool call — Read · `toolu_016YJ2V7rYCkmj28N8Ubzbsf`</summary>

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
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "edb57fc9-bfa1-493b-baf2-0d5e8443b618",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uXeKpaAsrVbxLVN4VWVB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12651
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

_source line 6 · 2026-05-14T09:39:28.477Z_

<details><summary>↩ Tool result · `toolu_016YJ2V7rYCkmj28N8Ubzbsf`</summary>

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
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "ff71968a-e72b-4c5a-8bc4-40a4b665dbd0",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01WBtJ2Prw1ECvYtavuNAWfm`</summary>

```json
{
  "pattern": "**/*introduction*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "68054a58-172a-4d04-8f0e-e793d04c25c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uXeKpaAsrVbxLVN4VWVB4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12651,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12651
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

_source line 8 · 2026-05-14T09:39:29.041Z_

<details><summary>↩ Tool result · `toolu_01WBtJ2Prw1ECvYtavuNAWfm`</summary>

```text
artifacts/_project/paper/introduction_draft.md
artifacts/_project/paper/introduction_draft_d860d5.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "a5308641-33bf-40da-9469-d97ce299b4ac",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/introduction_draft.md",
      "artifacts/_project/paper/introduction_draft_d860d5.md"
    ],
    "durationMs": 8,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing introduction drafts to understand what's already been written.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "53620475-4324-4f45-9950-97ebfdd211f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W54ErqXC1Vw5scXHL8mMh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 24492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5698
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

Let me check the existing drafts for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "e8f364ce-ffdc-410b-947c-a3440cb1068a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W54ErqXC1Vw5scXHL8mMh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 24492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5698
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

<details open><summary>🔧 Tool call — Read · `toolu_01VLVUiNt8PHMX5mz8rWMtXH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "db7d17ed-4a40-4402-9a28-f16fc4e3f9c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W54ErqXC1Vw5scXHL8mMh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 24492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5698
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

_source line 12 · 2026-05-14T09:39:34.086Z_

<details><summary>↩ Tool result · `toolu_01VLVUiNt8PHMX5mz8rWMtXH`</summary>

```text
1	# Introduction — Draft v1
2	
3	\section{Introduction}
4	
5	When LLM agents interact with rule-governed environments---manipulating temperatures, mixing chemicals, navigating physical constraints---they face a failure mode qualitatively distinct from suboptimality: \emph{catastrophic death}. A single hallucinated state transition can trigger an irreversible termination penalty, collapsing the episode score to $-100$. Deterministic external computation---environment simulators or code interpreters---eliminates such hallucinations by providing exact state transitions. But what does a router actually learn when trained to select between internal LLM reasoning and deterministic computation? Recent work on tool-use learning \cite{toolformer-2024,art-2023,chameleon-2024,retool-2026} and adaptive computation \cite{cogrouter-2026,ares-2026,mixture-of-recursions-2025} has developed methods for deciding when and how to invoke external modules, yet these approaches frame routing as a general capability or efficiency question---selecting the right tool, calibrating reasoning depth---without examining whether \emph{failure avoidance} constitutes a distinct and potentially dominant routing signal.
6	
7	We address this question by analyzing routing between internal reasoning, following the ReAct interleaved reasoning-and-acting paradigm \cite{react-2023}, and deterministic computation on ScienceWorld, an interactive science environment with sparse rewards and catastrophic failure penalties. A natural first approach is per-step oracle comparison: at each decision point, run both modalities and prefer the one yielding higher immediate reward. However, in sparse-reward environments where non-zero reward arrives only at episode termination, this strategy degenerates. On ScienceWorld, per-step oracle labeling produces \textbf{[PLACEHOLDER: 98\%]} ties---neither modality shows a per-step advantage on the vast majority of steps---rendering the resulting labels uninformative for router training. This \emph{oracle degeneracy} motivates a shift from step-level to episode-level analysis.
8	
9	We introduce \emph{episode-level counterfactual analysis}: for each task instance, we run complete episodes under pure-internal and pure-deterministic strategies, then compare episode-level outcomes to generate routing labels. Across [PLACEHOLDER: 30] ScienceWorld task types ([PLACEHOLDER: 249] episodes), this methodology reveals a striking concentration of routing signal. The full performance gap between deterministic and internal-reasoning strategies is [PLACEHOLDER: $\Delta_{\text{full}} = +37.9$] points. When we exclude episodes where either strategy results in agent death and recompute the gap, it collapses to [PLACEHOLDER: $\Delta_{\text{no\_death}} = +0.2$]---effectively zero. Death avoidance accounts for [PLACEHOLDER: 99\%] of the routing signal (death avoidance fraction [PLACEHOLDER: 98.75\%]). The per-task correlation between death rate differential and performance gap is $r =$ [PLACEHOLDER: 0.989] ($p < 0.0001$). Episode-level label distribution confirms this asymmetry: [PLACEHOLDER: 41\%] of episodes prefer deterministic computation, only [PLACEHOLDER: 0.5\%] prefer internal reasoning, and [PLACEHOLDER: 59\%] show no preference. When agents do not die, both reasoning modalities perform approximately equally.
10	
11	Our contributions are:
12	\begin{itemize}
13	    \item We propose \textbf{episode-level counterfactual analysis} for routing label generation, overcoming the degeneracy of per-step oracle labeling in sparse-reward interactive environments (per-step tie rate of [PLACEHOLDER: 98\%] on ScienceWorld).
14	    \item We introduce a \textbf{death decomposition framework} that separates routing signal into death-avoidance and non-death components, quantifying how much routing value derives from catastrophic failure prevention versus positive task guidance.
15	    \item We provide \textbf{empirical evidence} across [PLACEHOLDER: 30] ScienceWorld task types that death avoidance accounts for [PLACEHOLDER: 99\%] of routing signal between internal LLM reasoning and deterministic computation, with non-death performance near-equivalent between modalities ([PLACEHOLDER: $\Delta_{\text{no\_death}} = +0.2$]).
16	\end{itemize}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "c6dfb0f4-7441-4716-a072-21ae1ca09993",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_draft.md",
      "content": "# Introduction — Draft v1\n\n\\section{Introduction}\n\nWhen LLM agents interact with rule-governed environments---manipulating temperatures, mixing chemicals, navigating physical constraints---they face a failure mode qualitatively distinct from suboptimality: \\emph{catastrophic death}. A single hallucinated state transition can trigger an irreversible termination penalty, collapsing the episode score to $-100$. Deterministic external computation---environment simulators or code interpreters---eliminates such hallucinations by providing exact state transitions. But what does a router actually learn when trained to select between internal LLM reasoning and deterministic computation? Recent work on tool-use learning \\cite{toolformer-2024,art-2023,chameleon-2024,retool-2026} and adaptive computation \\cite{cogrouter-2026,ares-2026,mixture-of-recursions-2025} has developed methods for deciding when and how to invoke external modules, yet these approaches frame routing as a general capability or efficiency question---selecting the right tool, calibrating reasoning depth---without examining whether \\emph{failure avoidance} constitutes a distinct and potentially dominant routing signal.\n\nWe address this question by analyzing routing between internal reasoning, following the ReAct interleaved reasoning-and-acting paradigm \\cite{react-2023}, and deterministic computation on ScienceWorld, an interactive science environment with sparse rewards and catastrophic failure penalties. A natural first approach is per-step oracle comparison: at each decision point, run both modalities and prefer the one yielding higher immediate reward. However, in sparse-reward environments where non-zero reward arrives only at episode termination, this strategy degenerates. On ScienceWorld, per-step oracle labeling produces \\textbf{[PLACEHOLDER: 98\\%]} ties---neither modality shows a per-step advantage on the vast majority of steps---rendering the resulting labels uninformative for router training. This \\emph{oracle degeneracy} motivates a shift from step-level to episode-level analysis.\n\nWe introduce \\emph{episode-level counterfactual analysis}: for each task instance, we run complete episodes under pure-internal and pure-deterministic strategies, then compare episode-level outcomes to generate routing labels. Across [PLACEHOLDER: 30] ScienceWorld task types ([PLACEHOLDER: 249] episodes), this methodology reveals a striking concentration of routing signal. The full performance gap between deterministic and internal-reasoning strategies is [PLACEHOLDER: $\\Delta_{\\text{full}} = +37.9$] points. When we exclude episodes where either strategy results in agent death and recompute the gap, it collapses to [PLACEHOLDER: $\\Delta_{\\text{no\\_death}} = +0.2$]---effectively zero. Death avoidance accounts for [PLACEHOLDER: 99\\%] of the routing signal (death avoidance fraction [PLACEHOLDER: 98.75\\%]). The per-task correlation between death rate differential and performance gap is $r =$ [PLACEHOLDER: 0.989] ($p < 0.0001$). Episode-level label distribution confirms this asymmetry: [PLACEHOLDER: 41\\%] of episodes prefer deterministic computation, only [PLACEHOLDER: 0.5\\%] prefer internal reasoning, and [PLACEHOLDER: 59\\%] show no preference. When agents do not die, both reasoning modalities perform approximately equally.\n\nOur contributions are:\n\\begin{itemize}\n    \\item We propose \\textbf{episode-level counterfactual analysis} for routing label generation, overcoming the degeneracy of per-step oracle labeling in sparse-reward interactive environments (per-step tie rate of [PLACEHOLDER: 98\\%] on ScienceWorld).\n    \\item We introduce a \\textbf{death decomposition framework} that separates routing signal into death-avoidance and non-death components, quantifying how much routing value derives from catastrophic failure prevention versus positive task guidance.\n    \\item We provide \\textbf{empirical evidence} across [PLACEHOLDER: 30] ScienceWorld task types that death avoidance accounts for [PLACEHOLDER: 99\\%] of routing signal between internal LLM reasoning and deterministic computation, with non-death performance near-equivalent between modalities ([PLACEHOLDER: $\\Delta_{\\text{no\\_death}} = +0.2$]).\n\\end{itemize}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01CV9Ev2TzxwNvbgs6SJFjFG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_draft_d860d5.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "06a3e76a-23e9-47f3-9369-e7e2795654fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W54ErqXC1Vw5scXHL8mMh3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5698,
      "cache_read_input_tokens": 24492,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5698
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

_source line 14 · 2026-05-14T09:39:35.275Z_

<details><summary>↩ Tool result · `toolu_01CV9Ev2TzxwNvbgs6SJFjFG`</summary>

```text
1	# Introduction — Draft v1
2	
3	\section{Introduction}
4	
5	When LLM agents interact with rule-governed environments---manipulating temperatures, mixing chemicals, navigating physical constraints---they face a failure mode qualitatively distinct from suboptimality: \emph{catastrophic death}. A single hallucinated state transition can trigger an irreversible termination penalty, collapsing the episode score to $-100$. Deterministic external computation---environment simulators or code interpreters---eliminates such hallucinations by providing exact state transitions. But what does a router actually learn when trained to select between internal LLM reasoning and deterministic computation? Recent work on tool-use learning \cite{toolformer-2024,art-2023,chameleon-2024,retool-2026} and adaptive computation \cite{cogrouter-2026,ares-2026,mixture-of-recursions-2025} has developed methods for deciding when and how to invoke external modules, yet these approaches frame routing as a general capability or efficiency question---selecting the right tool, calibrating reasoning depth---without examining whether \emph{failure avoidance} constitutes a distinct and potentially dominant routing signal.
6	
7	We address this question by analyzing routing between internal reasoning, following the ReAct interleaved reasoning-and-acting paradigm \cite{react-2023}, and deterministic computation on ScienceWorld, an interactive science environment with sparse rewards and catastrophic failure penalties. A natural first approach is per-step oracle comparison: at each decision point, run both modalities and prefer the one yielding higher immediate reward. However, in sparse-reward environments where non-zero reward arrives only at episode termination, this strategy degenerates. On ScienceWorld, per-step oracle labeling produces \textbf{[PLACEHOLDER: 98\%]} ties---neither modality shows a per-step advantage on the vast majority of steps---rendering the resulting labels uninformative for router training. This \emph{oracle degeneracy} motivates a shift from step-level to episode-level analysis.
8	
9	We introduce \emph{episode-level counterfactual analysis}: for each task instance, we run complete episodes under pure-internal and pure-deterministic strategies, then compare episode-level outcomes to generate routing labels. Across [PLACEHOLDER: 30] ScienceWorld task types ([PLACEHOLDER: 249] episodes), this methodology reveals a striking concentration of routing signal. The full performance gap between deterministic and internal-reasoning strategies is [PLACEHOLDER: $\Delta_{\text{full}} = +37.9$] points. When we exclude episodes where either strategy results in agent death and recompute the gap, it collapses to [PLACEHOLDER: $\Delta_{\text{no\_death}} = +0.2$]---effectively zero. Death avoidance accounts for [PLACEHOLDER: 99\%] of the routing signal (death avoidance fraction [PLACEHOLDER: 98.75\%]). The per-task correlation between death rate differential and performance gap is $r =$ [PLACEHOLDER: 0.989] ($p < 0.0001$). Episode-level label distribution confirms this asymmetry: [PLACEHOLDER: 41\%] of episodes prefer deterministic computation, only [PLACEHOLDER: 0.5\%] prefer internal reasoning, and [PLACEHOLDER: 59\%] show no preference. When agents do not die, both reasoning modalities perform approximately equally.
10	
11	Our contributions are:
12	\begin{itemize}
13	    \item We propose \textbf{episode-level counterfactual analysis} for routing label generation, overcoming the degeneracy of per-step oracle labeling in sparse-reward interactive environments (per-step tie rate of [PLACEHOLDER: 98\%] on ScienceWorld).
14	    \item We introduce a \textbf{death decomposition framework} that separates routing signal into death-avoidance and non-death components, quantifying how much routing value derives from catastrophic failure prevention versus positive task guidance.
15	    \item We provide \textbf{empirical evidence} across [PLACEHOLDER: 30] ScienceWorld task types that death avoidance accounts for [PLACEHOLDER: 99\%] of routing signal between internal LLM reasoning and deterministic computation, with non-death performance near-equivalent between modalities ([PLACEHOLDER: $\Delta_{\text{no\_death}} = +0.2$]).
16	\end{itemize}
17	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "00f531ef-84e0-4ac7-9e08-c838962a87b8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_draft_d860d5.md",
      "content": "# Introduction — Draft v1\n\n\\section{Introduction}\n\nWhen LLM agents interact with rule-governed environments---manipulating temperatures, mixing chemicals, navigating physical constraints---they face a failure mode qualitatively distinct from suboptimality: \\emph{catastrophic death}. A single hallucinated state transition can trigger an irreversible termination penalty, collapsing the episode score to $-100$. Deterministic external computation---environment simulators or code interpreters---eliminates such hallucinations by providing exact state transitions. But what does a router actually learn when trained to select between internal LLM reasoning and deterministic computation? Recent work on tool-use learning \\cite{toolformer-2024,art-2023,chameleon-2024,retool-2026} and adaptive computation \\cite{cogrouter-2026,ares-2026,mixture-of-recursions-2025} has developed methods for deciding when and how to invoke external modules, yet these approaches frame routing as a general capability or efficiency question---selecting the right tool, calibrating reasoning depth---without examining whether \\emph{failure avoidance} constitutes a distinct and potentially dominant routing signal.\n\nWe address this question by analyzing routing between internal reasoning, following the ReAct interleaved reasoning-and-acting paradigm \\cite{react-2023}, and deterministic computation on ScienceWorld, an interactive science environment with sparse rewards and catastrophic failure penalties. A natural first approach is per-step oracle comparison: at each decision point, run both modalities and prefer the one yielding higher immediate reward. However, in sparse-reward environments where non-zero reward arrives only at episode termination, this strategy degenerates. On ScienceWorld, per-step oracle labeling produces \\textbf{[PLACEHOLDER: 98\\%]} ties---neither modality shows a per-step advantage on the vast majority of steps---rendering the resulting labels uninformative for router training. This \\emph{oracle degeneracy} motivates a shift from step-level to episode-level analysis.\n\nWe introduce \\emph{episode-level counterfactual analysis}: for each task instance, we run complete episodes under pure-internal and pure-deterministic strategies, then compare episode-level outcomes to generate routing labels. Across [PLACEHOLDER: 30] ScienceWorld task types ([PLACEHOLDER: 249] episodes), this methodology reveals a striking concentration of routing signal. The full performance gap between deterministic and internal-reasoning strategies is [PLACEHOLDER: $\\Delta_{\\text{full}} = +37.9$] points. When we exclude episodes where either strategy results in agent death and recompute the gap, it collapses to [PLACEHOLDER: $\\Delta_{\\text{no\\_death}} = +0.2$]---effectively zero. Death avoidance accounts for [PLACEHOLDER: 99\\%] of the routing signal (death avoidance fraction [PLACEHOLDER: 98.75\\%]). The per-task correlation between death rate differential and performance gap is $r =$ [PLACEHOLDER: 0.989] ($p < 0.0001$). Episode-level label distribution confirms this asymmetry: [PLACEHOLDER: 41\\%] of episodes prefer deterministic computation, only [PLACEHOLDER: 0.5\\%] prefer internal reasoning, and [PLACEHOLDER: 59\\%] show no preference. When agents do not die, both reasoning modalities perform approximately equally.\n\nOur contributions are:\n\\begin{itemize}\n    \\item We propose \\textbf{episode-level counterfactual analysis} for routing label generation, overcoming the degeneracy of per-step oracle labeling in sparse-reward interactive environments (per-step tie rate of [PLACEHOLDER: 98\\%] on ScienceWorld).\n    \\item We introduce a \\textbf{death decomposition framework} that separates routing signal into death-avoidance and non-death components, quantifying how much routing value derives from catastrophic failure prevention versus positive task guidance.\n    \\item We provide \\textbf{empirical evidence} across [PLACEHOLDER: 30] ScienceWorld task types that death avoidance accounts for [PLACEHOLDER: 99\\%] of routing signal between internal LLM reasoning and deterministic computation, with non-death performance near-equivalent between modalities ([PLACEHOLDER: $\\Delta_{\\text{no\\_death}} = +0.2$]).\n\\end{itemize}\n",
      "numLines": 17,
      "startLine": 1,
      "totalLines": 17
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
Now I have both drafts (they're identical) and the writing guidelines. Let me write the v2 introduction with:

1. All A-source numbers (plan-012-full, 11 tasks / 245 episodes)
2. Exactly 2 contributions (not 3)
3. ~600 words
4. Following all writing rules

Let me draft this carefully.

Key numbers to use:
- Δ_full = +29.60
- Δ_no_death = +2.84
- DAF = 90.41%


- r = 0.9698, p = 8.12e-7
- Death rates: internal 42.9%, deterministic 16.3%
- Label distribution: 86 det_preferred, 9 internal_preferred, 150 no_preference
- Oracle: 96.2% matches always-det
- Per-step tie rate: 98.2%
- find-non-living-thing: n=40, zero deaths, Δ_full = +9.58
- Implicit router: logit acc 74.5%, bal_acc 79%; generation acc 65.36%, internal recall 51.5%

Structure:
- P1: Hook + Problem (~150 words)
- P2: Contributions and results (~150 words)
- P3: Our Approach + Core Finding (~200 words)
- P4: Contributions (exactly 2) (~100 words)

For the contributions, I'm framing this as: first, we develop an episode-level counterfactual methodology with a death avoidance decomposition framework that uses death-aware labeling to overcome the per-step oracle degeneracy problem in sparse-reward settings. Second, across 11 ScienceWorld task types with 245 episodes, we show that death avoidance drives 90.41% of the routing signal, while non-death performance differences are minimal (Δ_no_death = +2.84, only 9.6% of total effect), though some tasks like find-non-living-thing reveal residual routing value even with zero deaths. The router acts as a diagnostic tool revealing what the implicit policy actually learns beyond death avoidance.

Now I'm drafting the introduction. I need to be precise with the model name (Qwen2.5-7B-Instruct), avoid overstatement phrases, keep it around 600 words, and anchor everything with concrete numbers from the analysis. Starting with a concrete hook about what happens when the agent encounters a failure scenario.

I'm setting up the core tension: internal reasoning hallucinates state transitions in complex environments like ScienceWorld, while deterministic external computation avoids these failures. This frames the research question around routing to prevent catastrophic failure rather than just matching capability to task. Existing work treats tool selection as a capability problem, but the key insight is that routing decisions should prioritize avoiding failure modes where hallucination is most dangerous.

The challenge is that standard per-step oracle approaches break down under sparse rewards—on ScienceWorld, 98% of steps give identical scores since rewards only arrive at episode end, leaving no signal to train a router. Keyword heuristics fail too since ScienceWorld uses generic action verbs rather than domain-specific language. So I'm proposing episode-level counterfactual analysis instead: run full episodes with pure internal reasoning and pure deterministic strategies, then compare outcomes to generate routing labels. Early results across 11 task types show the deterministic approach succeeds where pure reasoning fails.

The gap is striking: deterministic gains 29.6 points overall, but when I exclude episodes where either strategy kills the agent, that advantage shrinks to just 2.84 points—meaning death avoidance accounts for 90% of the performance difference. The correlation between death rate differential and performance gap is extremely strong (r = 0.97, p < 0.001), confirming this is the dominant factor. Internal reasoning dies in 43% of episodes versus 16% for deterministic, and the episode labels reflect this: most prefer deterministic, a few prefer internal reasoning.

I'm laying out the core contributions: first, an episode-level counterfactual framework that generates routing labels by comparing outcomes and decomposes the signal through death avoidance metrics, which solves the problem of per-step oracle degeneracy in sparse-reward settings. Second, across the 245 ScienceWorld episodes spanning 11 task types, death avoidance is responsible for 90% of the routing signal between the two strategies, with the remaining performance gap being minimal. I'm checking the word count across the sections I've drafted—looks like I'm around 540 words, which is a bit under the 600-word budget, so I should expand slightly in a few places. Let me verify the cross-references are correct and make sure I'm not using any of the prohibited phrases like "to the best of our knowledge." I also want to double-check that I'm accurately representing the findings—particularly that the 96.2% match with deterministic routing is the correct interpretation, not a claim that selective routing outperforms it. The citations to the methodology sections look good, and I should refine the prose to read more smoothly before finalizing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "725bd044-7480-4e91-a958-74cd53fc7f7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGvw8F1D554ou5EDcUkUmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2335,
      "cache_read_input_tokens": 30190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2335
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

Now I'll write the v2 introduction with all A-source numbers and exactly 2 contributions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "2b701f9b-d287-45fa-9f12-3c66be513ef6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGvw8F1D554ou5EDcUkUmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2335,
      "cache_read_input_tokens": 30190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2335
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

<details open><summary>🔧 Tool call — Write · `toolu_01YQLUFpqSbupS1ULXZCHAaH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_v2_draft.md",
  "content": "# Introduction — Draft v2 (A-source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Introduction}\n\nWhen a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated, or failing to model that metal conducts heat differently than glass---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\n\nExisting routing approaches \\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 98.2\\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\\S\\ref{sec:collection}). Keyword-based heuristics (\\S\\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\\texttt{pour}, \\texttt{move}, \\texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.\n\nWe propose \\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\S\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\Delta_{\\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$---a Death Avoidance Factor (DAF; \\S\\ref{sec:daf}) of 90.41\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), confirming that death avoidance is the primary mechanism across task types (\\S\\ref{sec:death-decomp}). Death rates differ sharply: 42.9\\% for internal reasoning versus 16.3\\% for deterministic computation. Episode-level labels reflect this asymmetry: of 245 episodes, 86 prefer deterministic, 9 prefer internal, and 150 show no preference---96.2\\% of oracle routing decisions match an unconditional always-deterministic strategy (\\S\\ref{sec:baselines}).\n\nOur contributions:\n\\begin{enumerate}\n\\item \\textbf{Episode-level counterfactual methodology with death avoidance decomposition.} We introduce a framework that generates routing labels from episode-level outcome comparisons and decomposes the routing signal via the DAF metric and death-aware labeling (\\S\\ref{sec:collection}, \\S\\ref{sec:daf}). This overcomes per-step oracle degeneracy (98.2\\% tie rate) in sparse-reward environments.\n\\item \\textbf{Death avoidance dominates routing signal on ScienceWorld.} Across 11 task types (245 episodes), death avoidance accounts for 90.41\\% of the routing signal between Qwen2.5-7B-Instruct internal reasoning and deterministic computation. Non-death differences are small ($\\Delta_{\\text{no\\_death}} = +2.84$, 9.6\\% of $\\Delta_{\\text{full}}$) but reveal residual routing value---e.g., \\texttt{find-non-living-thing} has zero deaths yet $\\Delta_{\\text{full}} = +9.58$ (\\S\\ref{sec:death-decomp}). Router training as a diagnostic probe shows counterfactual labels encode learnable patterns at the representation level (logit accuracy 74.5\\%, balanced accuracy 79\\%) despite a generation-level expression gap (\\S\\ref{sec:router-diagnostic}).\n\\end{enumerate}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "dc63efb0-c08e-41f6-9b09-bd73071cae21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JGvw8F1D554ou5EDcUkUmF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2335,
      "cache_read_input_tokens": 30190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2335
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

_source line 18 · 2026-05-14T09:40:28.414Z_

<details><summary>↩ Tool result · `toolu_01YQLUFpqSbupS1ULXZCHAaH`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_v2_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "7fab3b1e-cfd7-43bf-8ce3-1d98f6436447",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_v2_draft.md",
    "content": "# Introduction — Draft v2 (A-source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Introduction}\n\nWhen a Qwen2.5-7B-Instruct agent attempts to boil water in ScienceWorld \\cite{scienceworld-2022}, it must track temperature thresholds, container states, and heat source interactions across dozens of steps. Internal LLM reasoning hallucinates these state transitions---predicting water has boiled when the stove was never activated, or failing to model that metal conducts heat differently than glass---triggering agent death with a $-100$ penalty. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations by executing exact state transitions. The natural question: when should an agent route computation externally versus reasoning internally?\n\nExisting routing approaches \\cite{toolformer-2024,art-2023,chameleon-2024} frame tool selection as a capability or efficiency decision---matching subtasks to tools that can solve them. This framing ignores a potentially dominant signal: routing to \\emph{avoid catastrophic failure}. Understanding what routing actually learns requires counterfactual analysis, but the standard per-step oracle approach degenerates under sparse rewards. On ScienceWorld, where non-zero reward arrives only at episode termination, 98.2\\% of steps produce identical scores regardless of modality---no step-level signal exists to train a router (\\S\\ref{sec:collection}). Keyword-based heuristics (\\S\\ref{sec:rule}) also fail structurally: ScienceWorld actions use generic verbs (\\texttt{pour}, \\texttt{move}, \\texttt{activate}) rather than science-specific terminology, providing no lexical basis for routing decisions.\n\nWe propose \\emph{episode-level counterfactual analysis}: run complete episodes under pure-internal (ReAct~\\cite{react-2023}) and pure-deterministic strategies, then compare episode outcomes to generate routing labels (\\S\\ref{sec:collection}). Across 11 ScienceWorld task types (245 episodes), the full deterministic advantage is $\\Delta_{\\text{full}} = +29.60$ points. Excluding episodes where either strategy causes agent death, this gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$---a Death Avoidance Factor (DAF; \\S\\ref{sec:daf}) of 90.41\\%. The per-task correlation between death rate differential and performance gap is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), confirming that death avoidance is the primary mechanism across task types (\\S\\ref{sec:death-decomp}). Death rates differ sharply: 42.9\\% for internal reasoning versus 16.3\\% for deterministic computation. Episode-level labels reflect this asymmetry: of 245 episodes, 86 prefer deterministic, 9 prefer internal, and 150 show no preference---96.2\\% of oracle routing decisions match an unconditional always-deterministic strategy (\\S\\ref{sec:baselines}).\n\nOur contributions:\n\\begin{enumerate}\n\\item \\textbf{Episode-level counterfactual methodology with death avoidance decomposition.} We introduce a framework that generates routing labels from episode-level outcome comparisons and decomposes the routing signal via the DAF metric and death-aware labeling (\\S\\ref{sec:collection}, \\S\\ref{sec:daf}). This overcomes per-step oracle degeneracy (98.2\\% tie rate) in sparse-reward environments.\n\\item \\textbf{Death avoidance dominates routing signal on ScienceWorld.} Across 11 task types (245 episodes), death avoidance accounts for 90.41\\% of the routing signal between Qwen2.5-7B-Instruct internal reasoning and deterministic computation. Non-death differences are small ($\\Delta_{\\text{no\\_death}} = +2.84$, 9.6\\% of $\\Delta_{\\text{full}}$) but reveal residual routing value---e.g., \\texttt{find-non-living-thing} has zero deaths yet $\\Delta_{\\text{full}} = +9.58$ (\\S\\ref{sec:death-decomp}). Router training as a diagnostic probe shows counterfactual labels encode learnable patterns at the representation level (logit accuracy 74.5\\%, balanced accuracy 79\\%) despite a generation-level expression gap (\\S\\ref{sec:router-diagnostic}).\n\\end{enumerate}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 19_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "8c08ac01-c287-4687-8bae-f718bff22f58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QBmAMJpkJ99dzKzzVsc8rh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3466,
      "cache_read_input_tokens": 32525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3466
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

_source line 20_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VvvZUaXN2oGjzYfCV3vtWh`</summary>

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
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "6804482d-8fd7-4ef7-862c-8284d7f98096",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QBmAMJpkJ99dzKzzVsc8rh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3466,
      "cache_read_input_tokens": 32525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3466
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

_source line 21 · 2026-05-14T09:40:31.173Z_

<details><summary>↩ Tool result · `toolu_01VvvZUaXN2oGjzYfCV3vtWh`</summary>

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
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "fef12b6e-619d-4e86-9467-adcb8192a780",
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

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_017e7oQtLfJ2iJGmmYP76rVT`</summary>

```json
{
  "name": "introduction_v2_draft",
  "type": "paper",
  "description": "Introduction section v2 draft with A-source data (plan-012-full, 11 tasks / 245 episodes). ~580 words, 4 paragraphs, exactly 2 contributions. All placeholders replaced with verified numbers.",
  "project": "simgate-modular-routing",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/introduction_v2_draft.md",
  "tags": [
    "paper",
    "introduction",
    "v2",
    "a-source"
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
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "f781bd6b-726b-499b-8f37-740f9e64c524",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B9JJ5tEpthyvSxozTtrtR8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 820,
      "cache_read_input_tokens": 35991,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 820
      },
      "output_tokens": 69,
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

_source line 23 · 2026-05-14T09:40:36.662Z_

<details><summary>↩ Tool result · `toolu_017e7oQtLfJ2iJGmmYP76rVT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_32f156\", \"name\": \"introduction_v2_draft\", \"type\": \"paper\", \"description\": \"Introduction section v2 draft with A-source data (plan-012-full, 11 tasks / 245 episodes). ~580 words, 4 paragraphs, exactly 2 contributions. All placeholders replaced with verified numbers.\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/introduction_v2_draft_32f156.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T09:40:36.601149+00:00\", \"tags\": [\"paper\", \"introduction\", \"v2\", \"a-source\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "744c6e3d-53fa-4ccb-9e8d-b20c8b0b3041",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_32f156\\\", \\\"name\\\": \\\"introduction_v2_draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Introduction section v2 draft with A-source data (plan-012-full, 11 tasks / 245 episodes). ~580 words, 4 paragraphs, exactly 2 contributions. All placeholders replaced with verified numbers.\\\", \\\"path\\\": \\\"projects/simgate-modular-routing/artifacts/_project/paper/introduction_v2_draft_32f156.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"simgate-modular-routing\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T09:40:36.601149+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"introduction\\\", \\\"v2\\\", \\\"a-source\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_32f156\", \"name\": \"introduction_v2_draft\", \"type\": \"paper\", \"description\": \"Introduction section v2 draft with A-source data (plan-012-full, 11 tasks / 245 episodes). ~580 words, 4 paragraphs, exactly 2 contributions. All placeholders replaced with verified numbers.\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/introduction_v2_draft_32f156.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T09:40:36.601149+00:00\", \"tags\": [\"paper\", \"introduction\", \"v2\", \"a-source\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

Introduction v2 written to `artifacts/_project/paper/introduction_v2_draft.md`.

**Changes from v1:**
- All placeholders replaced with A-source numbers (plan-012-full, 11 tasks / 245 episodes)
- Contributions reduced from 3 to exactly 2 (C1: methodology + DAF framework; C2: empirical finding + router diagnostic)
- Hook made concrete (Qwen2.5-7B-Instruct boiling water, specific hallucination examples)
- Added keyword heuristic failure point (P2) and find-non-living-thing residual case (C2)
- All 6 cross-references used (\S ref to collection, daf, rule, death-decomp, baselines, router-diagnostic)
- No B-source numbers, no banned phrases, no routing superiority claims

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "uuid": "38cb666f-e1f1-4d3d-a2af-6f32dfb90116",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DS9E5c4naJw3H7jQZT2VJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 578,
      "cache_read_input_tokens": 36811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 578
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

_source line 25_

Introduction v2 written to `artifacts/_project/paper/introduction_v2_draft.md`.

**Changes from v1:**
- All placeholders replaced with A-source numbers (plan-012-full, 11 tasks / 245 episodes)
- Contributions reduced from 3 to exactly 2 (C1: methodology + DAF framework; C2: empirical finding + router diagnostic)
- Hook made concrete (Qwen2.5-7B-Instruct boiling water, specific hallucination examples)
- Added keyword heuristic failure point (P2) and find-non-living-thing residual case (C2)
- All 6 cross-references used (\S ref to collection, daf, rule, death-decomp, baselines, router-diagnostic)
- No B-source numbers, no banned phrases, no routing superiority claims

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 78778,
  "duration_api_ms": 79686,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "f2943daa-c538-48d7-9f16-af57d19067d3",
  "total_cost_usd": 0.357003,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 25548,
    "cache_read_input_tokens": 171850,
    "output_tokens": 4367,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 25548,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 202,
        "cache_read_input_tokens": 36811,
        "cache_creation_input_tokens": 578,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 578
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2088,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002178,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 4367,
      "cacheReadInputTokens": 171850,
      "cacheCreationInputTokens": 25548,
      "webSearchRequests": 0,
      "costUSD": 0.354825,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "e78c5bb8-dc22-4eaa-87a3-e57d9f22c0fd"
}
```

</details>

---
