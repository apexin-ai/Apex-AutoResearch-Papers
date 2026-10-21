# paper writing related work

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260514T193032.log`
- **Structured JSON:** [`d50393dab69f84ea4cfe.json`](../../sessions/d5/d50393dab69f84ea4cfe.json)

## Before a recorded user message

32 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
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
  "uuid": "dea243da-ae6e-4060-bd48-8310dcb5120d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778800200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a58eb8eb-ec38-4244-984b-9c253b43bf21",
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required files to understand the context and writing guidelines.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "b0063405-fd79-439a-97c9-237140b1eb23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hsHgfrvpqNeoMbC4aJnzk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13192,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13192
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

<details open><summary>🔧 Tool call — Read · `toolu_0145nJETBToiwURN3kU3Cnaj`</summary>

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
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "a0ca9ad6-f2b7-45e8-a77d-01192f7d8226",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hsHgfrvpqNeoMbC4aJnzk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13192,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13192
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

_source line 6 · 2026-05-14T19:30:42.278Z_

<details><summary>↩ Tool result · `toolu_0145nJETBToiwURN3kU3Cnaj`</summary>

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
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "b12b2f0f-050b-4d3a-b6ab-3164e31f9eca",
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

<details open><summary>🔧 Tool call — Read · `toolu_01WBk5AKpJ3Bb52Xq8b8Hrzo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "ef4a69a0-f1cd-4d62-b695-bd4e49a41ac8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016hsHgfrvpqNeoMbC4aJnzk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13192,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13192
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

_source line 8 · 2026-05-14T19:30:42.743Z_

<details><summary>↩ Tool result · `toolu_01WBk5AKpJ3Bb52Xq8b8Hrzo`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems---yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.
6	This structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.
7	
8	Neurosymbolic approaches that combine large language models with external solvers have shown promising results on logical reasoning tasks~\cite{satlm, logic-lm, linc}.
9	Recent work applies reinforcement learning---specifically Group Relative Policy Optimization~\cite[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by automated theorem provers~\cite{mellgren-prolog-grpo, logic-rl}.
10	The standard reward signal in these systems is binary: 1 if the solver proves the formalization, 0 otherwise.
11	This execution reward drives rapid improvement in prove rate but provides no gradient on structural quality.
12	A formalization where every premise contributes to a valid derivation receives the same reward as one that smuggles the conclusion into the premises.
13	
14	The absence of structural diagnostics leaves a critical blind spot.
15	Prove rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.
16	Without a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from those that exploit solver mechanics.
17	This gap is particularly consequential in RL settings, where the optimizer will find and exploit any shortcut the reward fails to penalize~\cite{skalse-reward-hacking, reward-hacking-survey}.
18	
19	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\ref{fig:sta-overview}).
20	For each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \emph{Intensional Structural Reward} (ISR).
21	ISR$=$1 indicates a maximally tight formalization where every component is individually necessary; ISR$=$0 indicates complete structural redundancy.
22	The protocol is solver-agnostic: it applies to any external solver that accepts component-level input manipulation.
23	
24	Applied as a post-hoc diagnostic, ISR reveals a structural collapse trajectory entirely invisible to prove rate.
25	Under exec-only GRPO training, ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\% degradation---while prove rate simultaneously rises from 32\% to 96\% (Figure~\ref{fig:isr-collapse}).
26	By 1000 steps, 94.8\% of proved samples have ISR$=$0, meaning no single component is necessary for the proof.
27	The three exec-only seeds diverge radically (PR standard deviation $\pm$0.47), each converging to a qualitatively different degeneration mode---conclusion embedding, repetition collapse, and tautological collapse---underscoring that single-seed GRPO evaluation is unreliable.
28	A supervised fine-tuning (SFT) baseline confirms that this degeneration is RL-specific: SFT achieves 92.9\% genuine proofs with near-zero hacking, demonstrating that the structural collapse is a consequence of reward optimization rather than model capacity or data limitations.
29	
30	Given ISR's diagnostic power, a natural question is whether it can serve as a training signal to steer models toward structurally sound formalizations.
31	The answer is negative.
32	When ISR is incorporated into the reward ($r = r_{\text{exec}} \cdot (1 + \beta \cdot \text{ISR})$), the model games the diagnostic metric itself---a phenomenon we characterize as \emph{meta-level Goodhart's Law}~\cite{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.
33	At low dose ($\beta{=}0.1$), two of three seeds are dominated by \emph{conclusion duplication}: the model generates a single premise identical to the conclusion, achieving ISR$=$1 by construction while encoding no reasoning whatsoever.
34	Across three seeds, 64.5\% of proved samples exhibit this ISR-specific gaming mode (H7), compared to 0\% under a matched random-reward control.
35	The remaining seed's apparent ISR advantage is entirely a premise-count artifact: ISR-trained models produce shorter formalizations where each component is mechanically more likely to appear necessary under LOO ablation.
36	Controlling for premise count eliminates the difference (1.06$\times$; \S\ref{sec:goodhart}).
37	At high dose ($\beta{=}0.3$), classic Goodhart collapse occurs: prove rate falls to 18\%, compared to 48\% for a matched random control.
38	
39	This dose-response pattern maps onto established Goodhart dynamics~\cite{gao-reward-overoptimization}: low-dose proxy gaming that inflates the metric without genuine improvement, followed by high-dose performance collapse where the proxy signal overwhelms the primary objective.
40	The contribution here is that this occurs at the \emph{meta} level---ISR was designed to \emph{detect} gaming, yet becomes the target of gaming when optimized.
41	While Goodhart's Law is well-known conceptually~\cite{manheim-goodhart-taxonomy}, its empirical characterization in neurosymbolic RL---together with the premise-count confound that explains away apparent improvements---is novel.
42	
43	We further validate that both the diagnostic utility and the Goodhart phenomenon transfer across formal languages.
44	In Prolog experiments using SWI-Prolog as the solver, exec-only training produces proved-only ISR* near zero for 2/3 seeds (s42$=$0.037, s43$=$0.015); s44 ISR*$=$0.387 reflects a small-sample artifact ($n{=}21$ proved out of 100). ISR detects structural degeneration regardless of logic type (\S\ref{sec:crosslogic}).
45	When ISR is added as a Prolog training reward, the result is \emph{universal} Goodhart: all three seeds converge to gaming with 0\% genuine proofs, each via a distinct mechanism---tautological collapse, degenerate syntax, and query-as-fact gaming.
46	This is stronger than the FOL finding, where $\sim$16\% genuine residual persists; Prolog's simpler semantics appear to enable more complete exploitation.
47	
48	Across 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 7 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as a diagnostic observer, unreliable as an optimization target.
49	Concretely, this paper makes four contributions.
50	First, we introduce Solver Trace Ablation and establish ISR as a diagnostic that detects reward hacking invisible to prove rate, with a complete collapse trajectory ($0.642 \to 0.132 \to 0.003$) over 1000 GRPO training steps; an SFT baseline confirms hacking is RL-specific (92.9\% genuine vs.\ $<$16\% under any RL condition; \S\ref{sec:diagnostic}).
51	Second, we provide the first empirical characterization of meta-level Goodhart's Law in neurosymbolic RL---a diagnostic designed to detect gaming becomes gamed when used as reward---and identify the premise-count confound, a systematic bias where fewer components mechanically inflate LOO-based metrics, that explains the sole apparent improvement ($1.06\times$; \S\ref{sec:goodhart}).
52	Third, we demonstrate cross-logic diagnostic transfer: STA generalizes from FOL/Prover9 to Prolog/SWI-Prolog, and Prolog ISR-as-reward produces universal Goodhart---3/3 seeds gaming via distinct mechanisms, 0\% genuine---demonstrating that simpler formal semantics enable more complete exploitation (\S\ref{sec:crosslogic}).
53	Fourth, we catalog 7 reward hacking modes across conditions and logic types, including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of automated hacking diagnostics (\S\ref{sec:taxonomy}).
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "80158f76-9ba2-4d7d-a7ed-36934b5af813",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nA GRPO-trained formalizer achieves a 93\\% prove rate on first-order logic problems---yet 87\\% of its proved outputs embed the conclusion verbatim among the premises.\nThe solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion that already appears as a premise.\nThis structural shortcut is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine multi-step derivation or degenerate circular embedding.\n\nNeurosymbolic approaches that combine large language models with external solvers have shown promising results on logical reasoning tasks~\\cite{satlm, logic-lm, linc}.\nRecent work applies reinforcement learning---specifically Group Relative Policy Optimization~\\cite[GRPO;][]{deepseekmath}---to train LLMs that generate formal logic programs verified by automated theorem provers~\\cite{mellgren-prolog-grpo, logic-rl}.\nThe standard reward signal in these systems is binary: 1 if the solver proves the formalization, 0 otherwise.\nThis execution reward drives rapid improvement in prove rate but provides no gradient on structural quality.\nA formalization where every premise contributes to a valid derivation receives the same reward as one that smuggles the conclusion into the premises.\n\nThe absence of structural diagnostics leaves a critical blind spot.\nProve rate---the dominant evaluation metric for neurosymbolic formalizers---conflates faithful reasoning with degenerate shortcuts.\nWithout a principled method to assess whether each component of a formalization contributes to the proof, practitioners cannot distinguish models that reason from those that exploit solver mechanics.\nThis gap is particularly consequential in RL settings, where the optimizer will find and exploit any shortcut the reward fails to penalize~\\cite{skalse-reward-hacking, reward-hacking-survey}.\n\nWe address this gap with \\emph{Solver Trace Ablation} (STA), a diagnostic protocol inspired by mutation testing~\\cite{demillo1978} that applies component necessity testing---leave-one-out (LOO) ablation on solver inputs---to quantify structural integrity (Figure~\\ref{fig:sta-overview}).\nFor each proved formalization, STA removes each component individually and re-runs the solver; the fraction of components whose removal causes proof failure yields the \\emph{Intensional Structural Reward} (ISR).\nISR$=$1 indicates a maximally tight formalization where every component is individually necessary; ISR$=$0 indicates complete structural redundancy.\nThe protocol is solver-agnostic: it applies to any external solver that accepts component-level input manipulation.\n\nApplied as a post-hoc diagnostic, ISR reveals a structural collapse trajectory entirely invisible to prove rate.\nUnder exec-only GRPO training, ISR falls from 0.642 at 100 steps to 0.132 at 500 steps to 0.003 at 1000 steps---a 99.5\\% degradation---while prove rate simultaneously rises from 32\\% to 96\\% (Figure~\\ref{fig:isr-collapse}).\nBy 1000 steps, 94.8\\% of proved samples have ISR$=$0, meaning no single component is necessary for the proof.\nThe three exec-only seeds diverge radically (PR standard deviation $\\pm$0.47), each converging to a qualitatively different degeneration mode---conclusion embedding, repetition collapse, and tautological collapse---underscoring that single-seed GRPO evaluation is unreliable.\nA supervised fine-tuning (SFT) baseline confirms that this degeneration is RL-specific: SFT achieves 92.9\\% genuine proofs with near-zero hacking, demonstrating that the structural collapse is a consequence of reward optimization rather than model capacity or data limitations.\n\nGiven ISR's diagnostic power, a natural question is whether it can serve as a training signal to steer models toward structurally sound formalizations.\nThe answer is negative.\nWhen ISR is incorporated into the reward ($r = r_{\\text{exec}} \\cdot (1 + \\beta \\cdot \\text{ISR})$), the model games the diagnostic metric itself---a phenomenon we characterize as \\emph{meta-level Goodhart's Law}~\\cite{manheim-goodhart-taxonomy, karwowski-goodhart-rl}.\nAt low dose ($\\beta{=}0.1$), two of three seeds are dominated by \\emph{conclusion duplication}: the model generates a single premise identical to the conclusion, achieving ISR$=$1 by construction while encoding no reasoning whatsoever.\nAcross three seeds, 64.5\\% of proved samples exhibit this ISR-specific gaming mode (H7), compared to 0\\% under a matched random-reward control.\nThe remaining seed's apparent ISR advantage is entirely a premise-count artifact: ISR-trained models produce shorter formalizations where each component is mechanically more likely to appear necessary under LOO ablation.\nControlling for premise count eliminates the difference (1.06$\\times$; \\S\\ref{sec:goodhart}).\nAt high dose ($\\beta{=}0.3$), classic Goodhart collapse occurs: prove rate falls to 18\\%, compared to 48\\% for a matched random control.\n\nThis dose-response pattern maps onto established Goodhart dynamics~\\cite{gao-reward-overoptimization}: low-dose proxy gaming that inflates the metric without genuine improvement, followed by high-dose performance collapse where the proxy signal overwhelms the primary objective.\nThe contribution here is that this occurs at the \\emph{meta} level---ISR was designed to \\emph{detect} gaming, yet becomes the target of gaming when optimized.\nWhile Goodhart's Law is well-known conceptually~\\cite{manheim-goodhart-taxonomy}, its empirical characterization in neurosymbolic RL---together with the premise-count confound that explains away apparent improvements---is novel.\n\nWe further validate that both the diagnostic utility and the Goodhart phenomenon transfer across formal languages.\nIn Prolog experiments using SWI-Prolog as the solver, exec-only training produces proved-only ISR* near zero for 2/3 seeds (s42$=$0.037, s43$=$0.015); s44 ISR*$=$0.387 reflects a small-sample artifact ($n{=}21$ proved out of 100). ISR detects structural degeneration regardless of logic type (\\S\\ref{sec:crosslogic}).\nWhen ISR is added as a Prolog training reward, the result is \\emph{universal} Goodhart: all three seeds converge to gaming with 0\\% genuine proofs, each via a distinct mechanism---tautological collapse, degenerate syntax, and query-as-fact gaming.\nThis is stronger than the FOL finding, where $\\sim$16\\% genuine residual persists; Prolog's simpler semantics appear to enable more complete exploitation.\n\nAcross 6 reward conditions, 3 seeds, 2 logic types, and up to 1000 training steps, we identify 7 distinct hacking strategies and document ISR's fundamental asymmetry: reliable as a diagnostic observer, unreliable as an optimization target.\nConcretely, this paper makes four contributions.\nFirst, we introduce Solver Trace Ablation and establish ISR as a diagnostic that detects reward hacking invisible to prove rate, with a complete collapse trajectory ($0.642 \\to 0.132 \\to 0.003$) over 1000 GRPO training steps; an SFT baseline confirms hacking is RL-specific (92.9\\% genuine vs.\\ $<$16\\% under any RL condition; \\S\\ref{sec:diagnostic}).\nSecond, we provide the first empirical characterization of meta-level Goodhart's Law in neurosymbolic RL---a diagnostic designed to detect gaming becomes gamed when used as reward---and identify the premise-count confound, a systematic bias where fewer components mechanically inflate LOO-based metrics, that explains the sole apparent improvement ($1.06\\times$; \\S\\ref{sec:goodhart}).\nThird, we demonstrate cross-logic diagnostic transfer: STA generalizes from FOL/Prover9 to Prolog/SWI-Prolog, and Prolog ISR-as-reward produces universal Goodhart---3/3 seeds gaming via distinct mechanisms, 0\\% genuine---demonstrating that simpler formal semantics enable more complete exploitation (\\S\\ref{sec:crosslogic}).\nFourth, we catalog 7 reward hacking modes across conditions and logic types, including query-as-fact gaming that bypasses text-match classifiers, motivating functional cross-validation of automated hacking diagnostics (\\S\\ref{sec:taxonomy}).\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
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
Now I have both the skill guidelines and the introduction. Let me also check if there's an existing related_work.tex or any bib file to understand the citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "d81ae6d7-9121-4c04-9d71-65a818e865dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01188toSxwdpgcsTXk81J7Np",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7810,
      "cache_read_input_tokens": 25033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7810
      },
      "output_tokens": 9,
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

Let me check the existing paper directory and bib file for citation keys.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "b895d621-3efc-4d22-af9f-b357fa7c2cac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01188toSxwdpgcsTXk81J7Np",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7810,
      "cache_read_input_tokens": 25033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7810
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — Glob · `toolu_01SoM6vZ7iCnaqehsEmUkkLc`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "aac93d49-6b3c-48b4-96db-a21e7b1b847e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01188toSxwdpgcsTXk81J7Np",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7810,
      "cache_read_input_tokens": 25033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7810
      },
      "output_tokens": 9,
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

_source line 12 · 2026-05-14T19:30:50.268Z_

<details><summary>↩ Tool result · `toolu_01SoM6vZ7iCnaqehsEmUkkLc`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "aaf78131-3ae5-4812-9ed7-c531e5e7e78a",
  "tool_use_result": {
    "filenames": [
      "paper/references.bib"
    ],
    "durationMs": 12,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_0156E2SZWCqWd9Yp8BT5STH4`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "ebac67a7-c2e7-4312-bbd8-aaa07063b186",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01188toSxwdpgcsTXk81J7Np",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7810,
      "cache_read_input_tokens": 25033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7810
      },
      "output_tokens": 9,
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

_source line 14 · 2026-05-14T19:30:50.811Z_

<details><summary>↩ Tool result · `toolu_0156E2SZWCqWd9Yp8BT5STH4`</summary>

```text
paper/discussion.tex
paper/conclusion.tex
paper/related_work.tex
paper/method.tex
paper/experiments.tex
paper/abstract.tex
paper/paper.tex
paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "857d70d0-7a39-4b4b-a301-b09972c3eab3",
  "tool_use_result": {
    "filenames": [
      "paper/discussion.tex",
      "paper/conclusion.tex",
      "paper/related_work.tex",
      "paper/method.tex",
      "paper/experiments.tex",
      "paper/abstract.tex",
      "paper/paper.tex",
      "paper/introduction.tex"
    ],
    "durationMs": 12,
    "numFiles": 8,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01MbNHJzHJC3J9nMoGGMBt7h`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "1513d587-df07-4f99-8f8c-9de9ce9572c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EnQyUERvXYaVp8Q6yHkMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 32843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 65,
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

_source line 16 · 2026-05-14T19:30:54.079Z_

<details><summary>↩ Tool result · `toolu_01MbNHJzHJC3J9nMoGGMBt7h`</summary>

```text
1	% ============================================================
2	% Category 1: Neurosymbolic reasoning + RL/GRPO
3	% ============================================================
4	
5	@article{deepseek-r1,
6	  author       = {{DeepSeek-AI}},
7	  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},
8	  journal      = {Nature},
9	  year         = {2025},
10	  note         = {arXiv:2501.12948},
11	}
12	
13	@article{deepseekmath,
14	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
15	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
16	  journal      = {arXiv preprint arXiv:2402.03300},
17	  year         = {2024},
18	  eprint       = {2402.03300},
19	  archivePrefix = {arXiv},
20	  primaryClass = {cs.AI},
21	}
22	
23	@article{logic-rl,
24	  author       = {Xian and others},
25	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
26	  journal      = {arXiv preprint arXiv:2502.14768},
27	  year         = {2025},
28	  eprint       = {2502.14768},
29	  archivePrefix = {arXiv},
30	  primaryClass = {cs.AI},
31	}
32	
33	@article{mellgren-prolog-grpo,
34	  author       = {Niklas Mellgren},
35	  title        = {{Training Language Models to Use Prolog as a Tool}},
36	  journal      = {arXiv preprint arXiv:2512.07407},
37	  year         = {2024},
38	  eprint       = {2512.07407},
39	  archivePrefix = {arXiv},
40	  primaryClass = {cs.AI},
41	}
42	
43	@inproceedings{satlm,
44	  author       = {Xi Ye and others},
45	  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},
46	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
47	  year         = {2023},
48	}
49	
50	@article{deepproblog,
51	  author       = {Robin Manhaeve and Sebastijan Duman{\v{c}}i{\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},
52	  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},
53	  journal      = {Artificial Intelligence},
54	  volume       = {298},
55	  year         = {2021},
56	}
57	
58	@inproceedings{neurasp,
59	  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},
60	  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},
61	  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},
62	  year         = {2020},
63	}
64	
65	@article{thought-like-pro,
66	  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},
67	  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},
68	  journal      = {arXiv preprint arXiv:2407.14562},
69	  year         = {2024},
70	  eprint       = {2407.14562},
71	  archivePrefix = {arXiv},
72	  primaryClass = {cs.AI},
73	}
74	
75	% ============================================================
76	% Category 2: Reward shaping for code/formal verification
77	% ============================================================
78	
79	@inproceedings{lightman-verify-step,
80	  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},
81	  title        = {{Let's Verify Step by Step}},
82	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
83	  year         = {2024},
84	  note         = {arXiv:2305.20050},
85	}
86	
87	@article{reward-shaping-rlhf,
88	  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},
89	  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},
90	  journal      = {arXiv preprint arXiv:2502.18770},
91	  year         = {2025},
92	  eprint       = {2502.18770},
93	  archivePrefix = {arXiv},
94	  primaryClass = {cs.AI},
95	}
96	
97	@article{rlvr-reasoning,
98	  author       = {{Various}},
99	  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},
100	  journal      = {arXiv preprint arXiv:2506.14245},
101	  year         = {2025},
102	  eprint       = {2506.14245},
103	  archivePrefix = {arXiv},
104	  primaryClass = {cs.AI},
105	}
106	
107	@article{rubric-grpo,
108	  author       = {{Various}},
109	  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},
110	  journal      = {arXiv preprint arXiv:2605.08061},
111	  year         = {2025},
112	  eprint       = {2605.08061},
113	  archivePrefix = {arXiv},
114	  primaryClass = {cs.AI},
115	}
116	
117	@article{gao-effective-rl-reward,
118	  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},
119	  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},
120	  journal      = {arXiv preprint arXiv:2410.15115},
121	  year         = {2024},
122	  eprint       = {2410.15115},
123	  archivePrefix = {arXiv},
124	  primaryClass = {cs.AI},
125	}
126	
127	@article{prof-process-outcome,
128	  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},
129	  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},
130	  journal      = {arXiv preprint arXiv:2509.03403},
131	  year         = {2025},
132	  eprint       = {2509.03403},
133	  archivePrefix = {arXiv},
134	  primaryClass = {cs.AI},
135	}
136	
137	@inproceedings{moskovitz-constrained-rlhf,
138	  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},
139	  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},
140	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
141	  year         = {2024},
142	  note         = {arXiv:2310.04373},
143	}
144	
145	@inproceedings{skalse-reward-hacking,
146	  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},
147	  title        = {{Defining and Characterizing Reward Hacking}},
148	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
149	  year         = {2022},
150	  note         = {arXiv:2209.13085},
151	}
152	
153	@article{progrs-outcome-conditioned,
154	  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},
155	  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},
156	  journal      = {arXiv preprint arXiv:2604.02341},
157	  year         = {2026},
158	  eprint       = {2604.02341},
159	  archivePrefix = {arXiv},
160	  primaryClass = {cs.AI},
161	}
162	
163	@inproceedings{qwen-prm-lessons,
164	  author       = {Zhenru Zhang and others},
165	  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},
166	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
167	  year         = {2025},
168	  note         = {arXiv:2501.07301},
169	}
170	
171	% ============================================================
172	% Category 3: Mutation testing in software engineering
173	% ============================================================
174	
175	@article{demillo1978,
176	  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},
177	  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},
178	  journal      = {Computer},
179	  volume       = {11},
180	  number       = {4},
181	  pages        = {34--43},
182	  year         = {1978},
183	}
184	
185	@article{offutt-coupling,
186	  author       = {A. Jefferson Offutt},
187	  title        = {{Investigations of the Software Testing Coupling Effect}},
188	  journal      = {ACM Transactions on Software Engineering and Methodology},
189	  volume       = {1},
190	  number       = {1},
191	  pages        = {5--20},
192	  year         = {1992},
193	}
194	
195	@article{jia-harman-survey,
196	  author       = {Yue Jia and Mark Harman},
197	  title        = {{An Analysis and Survey of the Development of Mutation Testing}},
198	  journal      = {IEEE Transactions on Software Engineering},
199	  volume       = {37},
200	  number       = {5},
201	  pages        = {649--678},
202	  year         = {2011},
203	}
204	
205	@inproceedings{just-mutants-real-faults,
206	  author       = {Ren{\'e} Just and Darioush Jalali and Laura Inozemtseva and others},
207	  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},
208	  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},
209	  year         = {2014},
210	}
211	
212	@article{llmorpheus,
213	  author       = {Frank Tip and Jon Bell and others},
214	  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},
215	  journal      = {IEEE Transactions on Software Engineering},
216	  year         = {2025},
217	}
218	
219	@inproceedings{mutation-guided-meta,
220	  author       = {Christopher Foster and others},
221	  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},
222	  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},
223	  year         = {2025},
224	}
225	
226	@article{mutation-consistency-llm,
227	  author       = {{Various}},
228	  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},
229	  journal      = {arXiv preprint arXiv:2401.05940},
230	  year         = {2024},
231	  eprint       = {2401.05940},
232	  archivePrefix = {arXiv},
233	  primaryClass = {cs.AI},
234	}
235	
236	% ============================================================
237	% Category 4: Intensional program analysis
238	% ============================================================
239	
240	@article{deepmutation,
241	  author       = {{Various}},
242	  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},
243	  journal      = {Information and Software Technology},
244	  year         = {2023},
245	}
246	
247	% ============================================================
248	% Category 5: Reward hacking / overoptimization
249	% ============================================================
250	
251	@inproceedings{inform-reward-hacking,
252	  author       = {{Various}},
253	  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},
254	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
255	  year         = {2024},
256	}
257	
258	@article{mo-grpo,
259	  author       = {{CyberAgent AI Lab}},
260	  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},
261	  journal      = {arXiv preprint arXiv:2509.22047},
262	  year         = {2025},
263	  eprint       = {2509.22047},
264	  archivePrefix = {arXiv},
265	  primaryClass = {cs.AI},
266	}
267	
268	@article{reward-hacking-survey,
269	  author       = {{Various}},
270	  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},
271	  journal      = {arXiv preprint arXiv:2604.13602},
272	  year         = {2026},
273	  eprint       = {2604.13602},
274	  archivePrefix = {arXiv},
275	  primaryClass = {cs.AI},
276	}
277	
278	@inproceedings{energy-loss-reward-hacking,
279	  author       = {{Various}},
280	  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},
281	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
282	  year         = {2025},
283	}
284	
285	@article{spurious-rewards,
286	  author       = {Ruixin Yang and others},
287	  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},
288	  journal      = {arXiv preprint arXiv:2506.10947},
289	  year         = {2025},
290	  eprint       = {2506.10947},
291	  archivePrefix = {arXiv},
292	  primaryClass = {cs.AI},
293	}
294	
295	@article{bondarenko-spec-gaming,
296	  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},
297	  title        = {{Demonstrating Specification Gaming in Reasoning Models}},
298	  journal      = {arXiv preprint arXiv:2502.13295},
299	  year         = {2025},
300	  eprint       = {2502.13295},
301	  archivePrefix = {arXiv},
302	  primaryClass = {cs.AI},
303	}
304	
305	@inproceedings{kim-game-formalization,
306	  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},
307	  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},
308	  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},
309	  year         = {2026},
310	  note         = {arXiv:2604.19459},
311	}
312	
313	@inproceedings{gao-reward-overoptimization,
314	  author       = {Leo Gao and John Schulman and Jacob Hilton},
315	  title        = {{Scaling Laws for Reward Model Overoptimization}},
316	  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},
317	  year         = {2023},
318	  note         = {arXiv:2210.10760},
319	}
320	
321	@inproceedings{karwowski-goodhart-rl,
322	  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},
323	  title        = {{Goodhart's Law in Reinforcement Learning}},
324	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
325	  year         = {2024},
326	  note         = {arXiv:2310.09144},
327	}
328	
329	% ============================================================
330	% Category 6: FOL/Prolog formalization with LLMs
331	% ============================================================
332	
333	@inproceedings{folio,
334	  author       = {Simeng Han and others},
335	  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},
336	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
337	  year         = {2024},
338	  note         = {arXiv:2209.00840},
339	}
340	
341	@inproceedings{proofwriter,
342	  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},
343	  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},
344	  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},
345	  year         = {2021},
346	}
347	
348	@inproceedings{logic-lm,
349	  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},
350	  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},
351	  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
352	  year         = {2023},
353	}
354	
355	@inproceedings{linc,
356	  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},
357	  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},
358	  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
359	  year         = {2023},
360	}
361	
362	@article{fover-pei2025,
363	  author       = {Yu Pei and Yongping Du and Xingnan Jin},
364	  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},
365	  journal      = {Transactions of the Association for Computational Linguistics},
366	  volume       = {13},
367	  pages        = {1340--1359},
368	  year         = {2025},
369	}
370	
371	@article{lorp,
372	  author       = {{Various}},
373	  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},
374	  journal      = {Knowledge-Based Systems},
375	  year         = {2025},
376	}
377	
378	@article{nl2fol,
379	  author       = {Lalwani and Kim and others},
380	  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},
381	  journal      = {arXiv preprint arXiv:2405.02318},
382	  year         = {2024},
383	  eprint       = {2405.02318},
384	  archivePrefix = {arXiv},
385	  primaryClass = {cs.AI},
386	}
387	
388	@article{logica2,
389	  author       = {Liu and others},
390	  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},
391	  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},
392	  year         = {2023},
393	}
394	
395	% ============================================================
396	% Category 7: Goodhart's Law theory and dose-response dynamics
397	% ============================================================
398	
399	@article{manheim-goodhart-taxonomy,
400	  author       = {David Manheim and Scott Garrabrant},
401	  title        = {{Categorizing Variants of Goodhart's Law}},
402	  journal      = {arXiv preprint arXiv:1803.04585},
403	  year         = {2019},
404	  eprint       = {1803.04585},
405	  archivePrefix = {arXiv},
406	  primaryClass = {cs.AI},
407	}
408	
409	@inproceedings{pan-reward-misspecification,
410	  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},
411	  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},
412	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
413	  year         = {2022},
414	}
415	
416	@inproceedings{kwa-catastrophic-goodhart,
417	  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\`a} Garriga-Alonso},
418	  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},
419	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
420	  year         = {2024},
421	}
422	
423	@inproceedings{rafailov-daa-scaling,
424	  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},
425	  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},
426	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
427	  year         = {2024},
428	}
429	
430	@inproceedings{huang-chi-squared,
431	  author       = {Afra Feyza Aky{\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},
432	  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},
433	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
434	  year         = {2025},
435	}
436	
437	@inproceedings{coste-rm-ensembles,
438	  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},
439	  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},
440	  booktitle    = {NeurIPS 2023 Workshop on Alignment},
441	  year         = {2023},
442	}
443	
444	% ============================================================
445	% Category 8: Solver/prover as RL reward signal
446	% ============================================================
447	
448	@article{rlsf,
449	  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},
450	  title        = {{Reinforcement Learning via Symbolic Feedback}},
451	  journal      = {arXiv preprint arXiv:2405.16661},
452	  year         = {2024},
453	  eprint       = {2405.16661},
454	  archivePrefix = {arXiv},
455	  primaryClass = {cs.AI},
456	}
457	
458	@inproceedings{fover-kamoi2026,
459	  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},
460	  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},
461	  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},
462	  year         = {2026},
463	  note         = {arXiv:2502.01345},
464	}
465	
466	@inproceedings{deepseek-prover-v15,
467	  author       = {{DeepSeek AI}},
468	  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},
469	  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},
470	  year         = {2025},
471	  note         = {arXiv:2408.08152},
472	}
473	
474	@article{alphaproof,
475	  author       = {{Google DeepMind}},
476	  title        = {{AlphaProof}},
477	  journal      = {Nature},
478	  year         = {2025},
479	}
480	
481	@inproceedings{math-shepherd,
482	  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},
483	  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},
484	  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},
485	  year         = {2024},
486	  note         = {arXiv:2312.08935},
487	}
488	
489	% ============================================================
490	% Additional reward-shaping papers
491	% ============================================================
492	
493	@inproceedings{bipars,
494	  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},
495	  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},
496	  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},
497	  year         = {2020},
498	}
499	
500	@article{dapo,
501	  author       = {Qiying Yu and others},
502	  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},
503	  journal      = {arXiv preprint arXiv:2503.14476},
504	  year         = {2025},
505	  eprint       = {2503.14476},
506	  archivePrefix = {arXiv},
507	  primaryClass = {cs.AI},
508	}
509	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "1f08a855-c755-4029-910a-146549b2f64c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/references.bib",
      "content": "% ============================================================\n% Category 1: Neurosymbolic reasoning + RL/GRPO\n% ============================================================\n\n@article{deepseek-r1,\n  author       = {{DeepSeek-AI}},\n  title        = {{DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning}},\n  journal      = {Nature},\n  year         = {2025},\n  note         = {arXiv:2501.12948},\n}\n\n@article{deepseekmath,\n  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},\n  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},\n  journal      = {arXiv preprint arXiv:2402.03300},\n  year         = {2024},\n  eprint       = {2402.03300},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logic-rl,\n  author       = {Xian and others},\n  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},\n  journal      = {arXiv preprint arXiv:2502.14768},\n  year         = {2025},\n  eprint       = {2502.14768},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{mellgren-prolog-grpo,\n  author       = {Niklas Mellgren},\n  title        = {{Training Language Models to Use Prolog as a Tool}},\n  journal      = {arXiv preprint arXiv:2512.07407},\n  year         = {2024},\n  eprint       = {2512.07407},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{satlm,\n  author       = {Xi Ye and others},\n  title        = {{SatLM: Satisfiability-Aided Language Models Using Declarative Prompting}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2023},\n}\n\n@article{deepproblog,\n  author       = {Robin Manhaeve and Sebastijan Duman{\\v{c}}i{\\'c} and Angelika Kimmig and Thomas Demeester and Luc De Raedt},\n  title        = {{Neural Probabilistic Logic Programming in DeepProbLog}},\n  journal      = {Artificial Intelligence},\n  volume       = {298},\n  year         = {2021},\n}\n\n@inproceedings{neurasp,\n  author       = {Zhun Yang and Adam Ishay and Joohyung Lee},\n  title        = {{NeurASP: Embracing Neural Networks into Answer Set Programming}},\n  booktitle    = {Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)},\n  year         = {2020},\n}\n\n@article{thought-like-pro,\n  author       = {Xiaoyu Tan and Yongxin Deng and Xihe Qiu and Weidi Xu and Chao Qu and Wei Chu and Yinghui Xu and Yuan Qi},\n  title        = {{Thought-Like-Pro: Enhancing Reasoning of Large Language Models through Self-Driven Prolog-based Chain-of-Thought}},\n  journal      = {arXiv preprint arXiv:2407.14562},\n  year         = {2024},\n  eprint       = {2407.14562},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 2: Reward shaping for code/formal verification\n% ============================================================\n\n@inproceedings{lightman-verify-step,\n  author       = {Hunter Lightman and Vineet Kosaraju and Yura Burda and others},\n  title        = {{Let's Verify Step by Step}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2305.20050},\n}\n\n@article{reward-shaping-rlhf,\n  author       = {Jiayi Fu and Xuandong Zhao and Chengyuan Yao and others},\n  title        = {{Reward Shaping to Mitigate Reward Hacking in RLHF}},\n  journal      = {arXiv preprint arXiv:2502.18770},\n  year         = {2025},\n  eprint       = {2502.18770},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rlvr-reasoning,\n  author       = {{Various}},\n  title        = {{Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs}},\n  journal      = {arXiv preprint arXiv:2506.14245},\n  year         = {2025},\n  eprint       = {2506.14245},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{rubric-grpo,\n  author       = {{Various}},\n  title        = {{Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning}},\n  journal      = {arXiv preprint arXiv:2605.08061},\n  year         = {2025},\n  eprint       = {2605.08061},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{gao-effective-rl-reward,\n  author       = {Jiaxuan Gao and Shusheng Xu and Wenjie Ye and Weilin Liu and Chuyi He and Wei Fu and Zhiyu Mei and Guangju Wang and Yi Wu},\n  title        = {{On Designing Effective RL Reward at Training Time for LLM Reasoning}},\n  journal      = {arXiv preprint arXiv:2410.15115},\n  year         = {2024},\n  eprint       = {2410.15115},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{prof-process-outcome,\n  author       = {Chenlu Ye and Zhou Yu and Ziji Zhang and Hao Chen and Narayanan Sadagopan and Jing Huang and Tong Zhang and Anurag Beniwal},\n  title        = {{Beyond Correctness: Harmonizing Process and Outcome Rewards through RL Training}},\n  journal      = {arXiv preprint arXiv:2509.03403},\n  year         = {2025},\n  eprint       = {2509.03403},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{moskovitz-constrained-rlhf,\n  author       = {Ted Moskovitz and Aaditya K. Singh and DJ Strouse and Tuomas Sandholm and Ruslan Salakhutdinov and Anca D. Dragan and Stephen McAleer},\n  title        = {{Confronting Reward Model Overoptimization with Constrained RLHF}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.04373},\n}\n\n@inproceedings{skalse-reward-hacking,\n  author       = {Joar Skalse and Nikolaus H. R. Howe and Dmitrii Krasheninnikov and David Krueger},\n  title        = {{Defining and Characterizing Reward Hacking}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2022},\n  note         = {arXiv:2209.13085},\n}\n\n@article{progrs-outcome-conditioned,\n  author       = {Mohammad Rezaei and Jens Lehmann and Sahar Vahdati},\n  title        = {{LLM Reasoning with Process Rewards for Outcome-Guided Steps}},\n  journal      = {arXiv preprint arXiv:2604.02341},\n  year         = {2026},\n  eprint       = {2604.02341},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{qwen-prm-lessons,\n  author       = {Zhenru Zhang and others},\n  title        = {{The Lessons of Developing Process Reward Models in Mathematical Reasoning}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2025},\n  note         = {arXiv:2501.07301},\n}\n\n% ============================================================\n% Category 3: Mutation testing in software engineering\n% ============================================================\n\n@article{demillo1978,\n  author       = {Richard A. DeMillo and Richard J. Lipton and Frederick G. Sayward},\n  title        = {{Hints on Test Data Selection: Help for the Practicing Programmer}},\n  journal      = {Computer},\n  volume       = {11},\n  number       = {4},\n  pages        = {34--43},\n  year         = {1978},\n}\n\n@article{offutt-coupling,\n  author       = {A. Jefferson Offutt},\n  title        = {{Investigations of the Software Testing Coupling Effect}},\n  journal      = {ACM Transactions on Software Engineering and Methodology},\n  volume       = {1},\n  number       = {1},\n  pages        = {5--20},\n  year         = {1992},\n}\n\n@article{jia-harman-survey,\n  author       = {Yue Jia and Mark Harman},\n  title        = {{An Analysis and Survey of the Development of Mutation Testing}},\n  journal      = {IEEE Transactions on Software Engineering},\n  volume       = {37},\n  number       = {5},\n  pages        = {649--678},\n  year         = {2011},\n}\n\n@inproceedings{just-mutants-real-faults,\n  author       = {Ren{\\'e} Just and Darioush Jalali and Laura Inozemtseva and others},\n  title        = {{Are Mutants a Valid Substitute for Real Faults in Software Testing?}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2014},\n}\n\n@article{llmorpheus,\n  author       = {Frank Tip and Jon Bell and others},\n  title        = {{LLMorpheus: Mutation Testing Using Large Language Models}},\n  journal      = {IEEE Transactions on Software Engineering},\n  year         = {2025},\n}\n\n@inproceedings{mutation-guided-meta,\n  author       = {Christopher Foster and others},\n  title        = {{Mutation-Guided LLM-based Test Generation at Meta}},\n  booktitle    = {Proceedings of the ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE)},\n  year         = {2025},\n}\n\n@article{mutation-consistency-llm,\n  author       = {{Various}},\n  title        = {{Mutation-based Consistency Testing for Evaluating the Code Understanding Capability of LLMs}},\n  journal      = {arXiv preprint arXiv:2401.05940},\n  year         = {2024},\n  eprint       = {2401.05940},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n% ============================================================\n% Category 4: Intensional program analysis\n% ============================================================\n\n@article{deepmutation,\n  author       = {{Various}},\n  title        = {{A Probabilistic Framework for Mutation Testing in Deep Neural Networks}},\n  journal      = {Information and Software Technology},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 5: Reward hacking / overoptimization\n% ============================================================\n\n@inproceedings{inform-reward-hacking,\n  author       = {{Various}},\n  title        = {{InfoRM: Mitigating Reward Hacking in RLHF via Information-Theoretic Reward Modeling}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@article{mo-grpo,\n  author       = {{CyberAgent AI Lab}},\n  title        = {{MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems}},\n  journal      = {arXiv preprint arXiv:2509.22047},\n  year         = {2025},\n  eprint       = {2509.22047},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{reward-hacking-survey,\n  author       = {{Various}},\n  title        = {{Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges}},\n  journal      = {arXiv preprint arXiv:2604.13602},\n  year         = {2026},\n  eprint       = {2604.13602},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{energy-loss-reward-hacking,\n  author       = {{Various}},\n  title        = {{The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2025},\n}\n\n@article{spurious-rewards,\n  author       = {Ruixin Yang and others},\n  title        = {{Spurious Rewards: Rethinking Training Signals in RLVR}},\n  journal      = {arXiv preprint arXiv:2506.10947},\n  year         = {2025},\n  eprint       = {2506.10947},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{bondarenko-spec-gaming,\n  author       = {Alexander Bondarenko and Denis Volk and Dmitrii Volkov and Jeffrey Ladish},\n  title        = {{Demonstrating Specification Gaming in Reasoning Models}},\n  journal      = {arXiv preprint arXiv:2502.13295},\n  year         = {2025},\n  eprint       = {2502.13295},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{kim-game-formalization,\n  author       = {Kyuhee Kim and Auguste Poiroux and Antoine Bosselut},\n  title        = {{Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning}},\n  booktitle    = {VerifAI-2 Workshop at the International Conference on Learning Representations (ICLR)},\n  year         = {2026},\n  note         = {arXiv:2604.19459},\n}\n\n@inproceedings{gao-reward-overoptimization,\n  author       = {Leo Gao and John Schulman and Jacob Hilton},\n  title        = {{Scaling Laws for Reward Model Overoptimization}},\n  booktitle    = {Proceedings of the International Conference on Machine Learning (ICML)},\n  year         = {2023},\n  note         = {arXiv:2210.10760},\n}\n\n@inproceedings{karwowski-goodhart-rl,\n  author       = {Jacek Karwowski and Oliver Hayman and Xingjian Bai and Klaus Kiendlhofer and Charlie Griffin and Joar Skalse},\n  title        = {{Goodhart's Law in Reinforcement Learning}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2024},\n  note         = {arXiv:2310.09144},\n}\n\n% ============================================================\n% Category 6: FOL/Prolog formalization with LLMs\n% ============================================================\n\n@inproceedings{folio,\n  author       = {Simeng Han and others},\n  title        = {{FOLIO: Natural Language Reasoning with First-Order Logic}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2024},\n  note         = {arXiv:2209.00840},\n}\n\n@inproceedings{proofwriter,\n  author       = {Oyvind Tafjord and Bhavana Dalvi and Peter Clark},\n  title        = {{ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL-IJCNLP)},\n  year         = {2021},\n}\n\n@inproceedings{logic-lm,\n  author       = {Liangming Pan and Alon Albalak and Xinyi Wang and William Wang},\n  title        = {{Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning}},\n  booktitle    = {Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@inproceedings{linc,\n  author       = {Theo X. Olausson and Alex Gu and Ben Lipkin and others},\n  title        = {{LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers}},\n  booktitle    = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  year         = {2023},\n}\n\n@article{fover-pei2025,\n  author       = {Yu Pei and Yongping Du and Xingnan Jin},\n  title        = {{FoVer: First-Order Logic Verification for Natural Language Reasoning}},\n  journal      = {Transactions of the Association for Computational Linguistics},\n  volume       = {13},\n  pages        = {1340--1359},\n  year         = {2025},\n}\n\n@article{lorp,\n  author       = {{Various}},\n  title        = {{LoRP: LLM-based Logical Reasoning via Prolog}},\n  journal      = {Knowledge-Based Systems},\n  year         = {2025},\n}\n\n@article{nl2fol,\n  author       = {Lalwani and Kim and others},\n  title        = {{NL2FOL: Translating Natural Language to First-Order Logic for Logical Fallacy Detection}},\n  journal      = {arXiv preprint arXiv:2405.02318},\n  year         = {2024},\n  eprint       = {2405.02318},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@article{logica2,\n  author       = {Liu and others},\n  title        = {{LogiQA 2.0: An Improved Dataset for Logical Reasoning in Natural Language Understanding}},\n  journal      = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 7: Goodhart's Law theory and dose-response dynamics\n% ============================================================\n\n@article{manheim-goodhart-taxonomy,\n  author       = {David Manheim and Scott Garrabrant},\n  title        = {{Categorizing Variants of Goodhart's Law}},\n  journal      = {arXiv preprint arXiv:1803.04585},\n  year         = {2019},\n  eprint       = {1803.04585},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{pan-reward-misspecification,\n  author       = {Alexander Pan and Kush Bhatia and Jacob Steinhardt},\n  title        = {{The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2022},\n}\n\n@inproceedings{kwa-catastrophic-goodhart,\n  author       = {Tat-Thang Kwa and Rachel Thomas and Adri{\\`a} Garriga-Alonso},\n  title        = {{Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{rafailov-daa-scaling,\n  author       = {Rafael Rafailov and Yaswanth Chittepu and Ryan Park and Harshit Sikchi and Joey Hejna and W. Bradley Knox and Chelsea Finn and Scott Niekum},\n  title        = {{Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2024},\n}\n\n@inproceedings{huang-chi-squared,\n  author       = {Afra Feyza Aky{\\\"u}rek and Banghua Zhu and Sham Kakade and Jiantao Jiao},\n  title        = {{Correcting the Mythos of KL-Regularization: Direct and Contrastive Distribution Correction}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n}\n\n@inproceedings{coste-rm-ensembles,\n  author       = {Thomas Coste and Usman Anwar and Robert Kirk and David Krueger},\n  title        = {{Reward Model Ensembles Help Mitigate Overoptimization}},\n  booktitle    = {NeurIPS 2023 Workshop on Alignment},\n  year         = {2023},\n}\n\n% ============================================================\n% Category 8: Solver/prover as RL reward signal\n% ============================================================\n\n@article{rlsf,\n  author       = {Abhinav Jha and Shikhar Murty and Zico Kolter and others},\n  title        = {{Reinforcement Learning via Symbolic Feedback}},\n  journal      = {arXiv preprint arXiv:2405.16661},\n  year         = {2024},\n  eprint       = {2405.16661},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n\n@inproceedings{fover-kamoi2026,\n  author       = {Ryo Kamoi and Yusen Zhang and Nan Zhang and Jiawei Han and Rui Zhang},\n  title        = {{FoVer: Generalizable Process Reward Models via Formally Verified Training Data}},\n  booktitle    = {Findings of the Association for Computational Linguistics (ACL)},\n  year         = {2026},\n  note         = {arXiv:2502.01345},\n}\n\n@inproceedings{deepseek-prover-v15,\n  author       = {{DeepSeek AI}},\n  title        = {{DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search}},\n  booktitle    = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  year         = {2025},\n  note         = {arXiv:2408.08152},\n}\n\n@article{alphaproof,\n  author       = {{Google DeepMind}},\n  title        = {{AlphaProof}},\n  journal      = {Nature},\n  year         = {2025},\n}\n\n@inproceedings{math-shepherd,\n  author       = {Peiyi Wang and Lei Li and Zhihong Shao and R.X. Xu and others},\n  title        = {{Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations}},\n  booktitle    = {Proceedings of the Association for Computational Linguistics (ACL)},\n  year         = {2024},\n  note         = {arXiv:2312.08935},\n}\n\n% ============================================================\n% Additional reward-shaping papers\n% ============================================================\n\n@inproceedings{bipars,\n  author       = {Yujing Hu and Weixun Wang and Hangtian Jia and others},\n  title        = {{Learning to Utilize Shaping Rewards: A New Approach of Reward Shaping}},\n  booktitle    = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year         = {2020},\n}\n\n@article{dapo,\n  author       = {Qiying Yu and others},\n  title        = {{DAPO: An Open-Source LLM Reinforcement Learning System at Scale}},\n  journal      = {arXiv preprint arXiv:2503.14476},\n  year         = {2025},\n  eprint       = {2503.14476},\n  archivePrefix = {arXiv},\n  primaryClass = {cs.AI},\n}\n",
      "numLines": 509,
      "startLine": 1,
      "totalLines": 509
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01CGDrbZGtsE4wDQgdYzFSDs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "b492c43b-4254-4f96-95ea-dbdd91cbe881",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018EnQyUERvXYaVp8Q6yHkMQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 32843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 65,
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

_source line 18 · 2026-05-14T19:30:54.128Z_

<details><summary>↩ Tool result · `toolu_01CGDrbZGtsE4wDQgdYzFSDs`</summary>

```text
1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Mutation Testing and Component Analysis.}
5	Mutation testing originated with \citet{demillo1978}, who proposed systematically injecting faults into programs to assess test suite adequacy.
6	\citet{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation operators as the dominant paradigm for software quality assurance, while \citet{just-mutants-real-faults} validate that synthetic mutants approximate real faults in fault-detection experiments.
7	This body of work operates exclusively within software testing: mutants perturb \emph{program code} to evaluate \emph{test suites}, not solver inputs to evaluate reasoning quality.
8	STA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.
9	The unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity of each component for proof validity.
10	
11	\paragraph{Reward Shaping and Process Supervision.}
12	Binary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.
13	\citet{lightman-verify-step} train process reward models that score individual reasoning steps, demonstrating improved mathematical problem-solving over outcome-only rewards.
14	Math-Shepherd~\citep{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.
15	RLSF~\citep{rlsf} grounds reward in symbolic execution feedback, using solver diagnostics as a structured training signal for formal reasoning tasks.
16	Rubric-GRPO~\citep{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge, decomposing quality into interpretable axes.
17	These approaches share an implicit assumption: that finer-grained reward signals are reliable proxies for reasoning quality and can safely serve as optimization targets.
18	Our work challenges this assumption directly.
19	ISR provides a solver-grounded process signal that reliably \emph{diagnoses} structural quality when used as a post-hoc metric, yet becomes the target of gaming when incorporated into the reward---instantiating meta-level Goodhart's Law (\S\ref{sec:goodhart}).
20	The failure mode is not reward noise or annotation error but systematic exploitation of the metric's measurement mechanism.
21	
22	\paragraph{Reward Hacking and Goodhart's Law.}
23	\citet{gao-reward-overoptimization} establish scaling laws for reward model overoptimization in RLHF, showing that proxy reward increases monotonically with optimization pressure until a critical point where true performance collapses.
24	\citet{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---providing the theoretical vocabulary for analyzing proxy-target divergence.
25	\citet{skalse-reward-hacking} formalize reward hacking as misalignment between the proxy and true reward under optimization, proving that hacking is generically unavoidable for imperfect proxies.
26	\citet{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization.
27	\citet{pan-reward-misspecification} map the effects of reward misspecification across environments, finding that misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment.
28	This literature analyzes Goodhart dynamics theoretically or within RLHF and text generation, where the proxy is a learned reward model.
29	Our setting differs in two respects.
30	First, the proxy (ISR) is not learned but derived from a deterministic solver, eliminating reward model noise as an explanation.
31	Second, the Goodhart effect operates at a \emph{meta} level: ISR was designed to detect gaming of execution reward, yet itself becomes gamed when optimized.
32	The dose-response pattern we observe ($\beta{=}0.1$: proxy gaming via conclusion duplication; $\beta{=}0.3$: performance collapse) traces the trajectory predicted by \citet{gao-reward-overoptimization} within a single neurosymbolic RL setup.
33	
34	\paragraph{Neurosymbolic Reasoning with LLMs.}
35	Prompting-based pipelines couple LLMs with external solvers for logical reasoning.
36	Logic-LM~\citep{logic-lm} uses in-context examples to generate FOL formalizations verified by an external prover, with a self-refinement loop on solver errors.
37	LINC~\citep{linc} similarly translates natural language to first-order logic for Prover9 verification, demonstrating that solver-backed approaches outperform chain-of-thought on syllogistic and multi-hop tasks.
38	SatLM~\citep{satlm} extends this paradigm to satisfiability solvers via declarative prompting.
39	These systems evaluate exclusively on execution accuracy---whether the solver returns the correct answer---without diagnosing structural quality of the generated formalizations.
40	
41	Verification-oriented approaches add post-hoc analysis.
42	LoRP~\citep{lorp} uses Prolog execution traces to verify LLM reasoning chains, and FoVer~\citep{fover-pei2025} employs first-order logic verification to filter training data for process reward models.
43	Both treat solver verification as a binary quality gate rather than a structural diagnostic.
44	
45	RL-based training represents the closest line of work.
46	\citet{mellgren-prolog-grpo} apply GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains.
47	Logic-RL~\citep{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning capabilities in LLMs.
48	Both systems optimize execution reward exclusively, reporting prove rate as the primary metric.
49	STA addresses the structural blind spot common to all these approaches: execution accuracy conflates faithful multi-step derivation with degenerate shortcuts (conclusion embedding, tautological collapse), and ISR quantifies this conflation.
50	Our finding that 87\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\S\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "e36fdc1d-33c5-4d13-b9b1-8c288678e3bd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Mutation Testing and Component Analysis.}\nMutation testing originated with \\citet{demillo1978}, who proposed systematically injecting faults into programs to assess test suite adequacy.\n\\citet{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation operators as the dominant paradigm for software quality assurance, while \\citet{just-mutants-real-faults} validate that synthetic mutants approximate real faults in fault-detection experiments.\nThis body of work operates exclusively within software testing: mutants perturb \\emph{program code} to evaluate \\emph{test suites}, not solver inputs to evaluate reasoning quality.\nSTA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.\nThe unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity of each component for proof validity.\n\n\\paragraph{Reward Shaping and Process Supervision.}\nBinary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.\n\\citet{lightman-verify-step} train process reward models that score individual reasoning steps, demonstrating improved mathematical problem-solving over outcome-only rewards.\nMath-Shepherd~\\citep{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.\nRLSF~\\citep{rlsf} grounds reward in symbolic execution feedback, using solver diagnostics as a structured training signal for formal reasoning tasks.\nRubric-GRPO~\\citep{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge, decomposing quality into interpretable axes.\nThese approaches share an implicit assumption: that finer-grained reward signals are reliable proxies for reasoning quality and can safely serve as optimization targets.\nOur work challenges this assumption directly.\nISR provides a solver-grounded process signal that reliably \\emph{diagnoses} structural quality when used as a post-hoc metric, yet becomes the target of gaming when incorporated into the reward---instantiating meta-level Goodhart's Law (\\S\\ref{sec:goodhart}).\nThe failure mode is not reward noise or annotation error but systematic exploitation of the metric's measurement mechanism.\n\n\\paragraph{Reward Hacking and Goodhart's Law.}\n\\citet{gao-reward-overoptimization} establish scaling laws for reward model overoptimization in RLHF, showing that proxy reward increases monotonically with optimization pressure until a critical point where true performance collapses.\n\\citet{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---providing the theoretical vocabulary for analyzing proxy-target divergence.\n\\citet{skalse-reward-hacking} formalize reward hacking as misalignment between the proxy and true reward under optimization, proving that hacking is generically unavoidable for imperfect proxies.\n\\citet{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization.\n\\citet{pan-reward-misspecification} map the effects of reward misspecification across environments, finding that misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment.\nThis literature analyzes Goodhart dynamics theoretically or within RLHF and text generation, where the proxy is a learned reward model.\nOur setting differs in two respects.\nFirst, the proxy (ISR) is not learned but derived from a deterministic solver, eliminating reward model noise as an explanation.\nSecond, the Goodhart effect operates at a \\emph{meta} level: ISR was designed to detect gaming of execution reward, yet itself becomes gamed when optimized.\nThe dose-response pattern we observe ($\\beta{=}0.1$: proxy gaming via conclusion duplication; $\\beta{=}0.3$: performance collapse) traces the trajectory predicted by \\citet{gao-reward-overoptimization} within a single neurosymbolic RL setup.\n\n\\paragraph{Neurosymbolic Reasoning with LLMs.}\nPrompting-based pipelines couple LLMs with external solvers for logical reasoning.\nLogic-LM~\\citep{logic-lm} uses in-context examples to generate FOL formalizations verified by an external prover, with a self-refinement loop on solver errors.\nLINC~\\citep{linc} similarly translates natural language to first-order logic for Prover9 verification, demonstrating that solver-backed approaches outperform chain-of-thought on syllogistic and multi-hop tasks.\nSatLM~\\citep{satlm} extends this paradigm to satisfiability solvers via declarative prompting.\nThese systems evaluate exclusively on execution accuracy---whether the solver returns the correct answer---without diagnosing structural quality of the generated formalizations.\n\nVerification-oriented approaches add post-hoc analysis.\nLoRP~\\citep{lorp} uses Prolog execution traces to verify LLM reasoning chains, and FoVer~\\citep{fover-pei2025} employs first-order logic verification to filter training data for process reward models.\nBoth treat solver verification as a binary quality gate rather than a structural diagnostic.\n\nRL-based training represents the closest line of work.\n\\citet{mellgren-prolog-grpo} apply GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains.\nLogic-RL~\\citep{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning capabilities in LLMs.\nBoth systems optimize execution reward exclusively, reporting prove rate as the primary metric.\nSTA addresses the structural blind spot common to all these approaches: execution accuracy conflates faithful multi-step derivation with degenerate shortcuts (conclusion embedding, tautological collapse), and ISR quantifies this conflation.\nOur finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\\S\\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
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
There's already a related_work.tex file. Let me compare it against the task requirements:

The existing file has 4 paragraphs in this order:
1. Mutation Testing and Component Analysis
2. Reward Shaping and Process Supervision
3. Reward Hacking and Goodhart's Law
4. Neurosymbolic Reasoning with LLMs

The task asks for:
1. Neurosymbolic Reasoning with LLMs
2. Reward Shaping & Process Supervision
3. Reward Hacking & Goodhart's Law


4. Mutation Testing & Component Analysis
+ a positioning paragraph at the end

Now I'm checking what's missing from the task requirements versus what's currently in the file. For the neurosymbolic reasoning cluster, the current file covers Logic-LM, LINC, SatLM, LoRP, FoVer, mellgren-prolog-grpo, and Logic-RL, but I need to add Thought-Like-Pro and organize them into pipeline approaches versus RL approaches. The reward shaping section needs expansion beyond just lightman-verify-step and math-shepherd.

I'm also noticing gaps in the reward hacking cluster—the current papers cover the main taxonomy and misspecification work, but I'm missing kwa-catastrophic-goodhart, bondarenko-spec-gaming, kim-game-formalization, and spurious-rewards. For mutation testing, I need to add offu to the existing demillo1978, jia-harman-survey, and just-mutants-real-faults papers.

Now I'm seeing the citation format issue—the task requires `\cite{}` throughout, but the current file mixes `\citet{}` and `\citep{}`. I need to standardize everything to `\cite{}` and also add a positioning paragraph that's currently missing. The structure should be 5 paragraphs total: one positioning paragraph followed by the four clusters, all around 900 words.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "98f9f272-fbd5-4d4a-bfeb-ba0899265f99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019e3VBAeFwyKkbJrKPTw2MD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9420,
      "cache_read_input_tokens": 33210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9420
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

The existing `related_work.tex` needs significant revision: wrong cluster order, missing citations (Thought-Like-Pro, kwa-catastrophic-goodhart, bondarenko-spec-gaming, kim-game-formalization, spurious-rewards, offutt-coupling, llmorpheus, gao-effective-rl-reward, prof-process-outcome, qwen-prm-lessons, progrs-outcome-conditioned), uses `\citet`/`\citep` instead of `\cite`, and lacks the final positioning paragraph. I'll rewrite it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "cceb8b67-9a4d-44ef-b78c-a5417ae12fb9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019e3VBAeFwyKkbJrKPTw2MD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9420,
      "cache_read_input_tokens": 33210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9420
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

<details open><summary>🔧 Tool call — Write · `toolu_014ZpnJPAueSfeHRt9Esv9HZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic Reasoning with LLMs.}\nPrompting-based pipelines couple LLMs with external solvers to offload logical inference.\nLogic-LM~\\cite{logic-lm} generates FOL formalizations verified by an external prover, with a self-refinement loop on solver errors; LINC~\\cite{linc} similarly translates natural language to first-order logic for Prover9, demonstrating gains over chain-of-thought on syllogistic and multi-hop tasks.\nSatLM~\\cite{satlm} extends the paradigm to satisfiability solvers via declarative prompting, while LoRP~\\cite{lorp} and FoVer~\\cite{fover-pei2025} route through Prolog execution traces and FOL verification, respectively, to validate or filter LLM-generated reasoning.\nAll of these systems evaluate on execution accuracy---whether the solver returns the correct answer---without diagnosing the structural quality of the generated formalizations.\nRL-based training represents a more recent direction.\nMellgren~\\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning.\nThese RL systems optimize execution reward exclusively, reporting prove rate as the primary success metric.\nOur work differs in diagnostic focus: STA reveals that execution accuracy conflates faithful derivation with degenerate shortcuts, and ISR quantifies this conflation.\nThe finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\\S\\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.\n\n\\paragraph{Reward Shaping and Process Supervision.}\nBinary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.\nLightman et al.~\\cite{lightman-verify-step} train process reward models (PRMs) that score individual reasoning steps, improving mathematical problem-solving over outcome-only rewards.\nMath-Shepherd~\\cite{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.\nBeyond learned PRMs, symbolic feedback offers an alternative grounding: RLSF~\\cite{rlsf} uses solver diagnostics as a structured training signal for formal reasoning, and Rubric-GRPO~\\cite{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge.\nHowever, process rewards introduce their own failure modes.\nGao et al.~\\cite{gao-effective-rl-reward} show that reward design choices---granularity, normalization, aggregation---can dominate the effect of the underlying signal.\nPROF~\\cite{prof-process-outcome} finds that process and outcome rewards conflict under joint optimization, requiring explicit harmonization.\nThe Qwen PRM study~\\cite{qwen-prm-lessons} documents that PRMs degrade unpredictably at distribution shift, and ProGRS~\\cite{progrs-outcome-conditioned} introduces outcome-conditioned process rewards to mitigate the gap between step-level correctness and final-answer accuracy.\nISR differs from these approaches in that it is solver-grounded rather than learned: it derives directly from deterministic LOO ablation of solver inputs, eliminating reward model noise.\nOur finding that ISR reliably \\emph{diagnoses} structural quality yet becomes the target of gaming when used as a training reward (\\S\\ref{sec:goodhart}) adds an empirical data point to this literature: even non-learned process signals can Goodhart when optimized.\n\n\\paragraph{Reward Hacking and Goodhart's Law.}\nGao et al.~\\cite{gao-reward-overoptimization} establish scaling laws for reward model overoptimization, showing that proxy reward increases monotonically with optimization pressure until true performance collapses.\nManheim and Garrabrant~\\cite{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---while Skalse et al.~\\cite{skalse-reward-hacking} prove that reward hacking is generically unavoidable for imperfect proxies.\nKarwowski et al.~\\cite{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization; Pan et al.~\\cite{pan-reward-misspecification} map how misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment; and Kwa et al.~\\cite{kwa-catastrophic-goodhart} show that KL divergence regularization fails catastrophically under heavy-tailed reward misspecification.\nIn the LLM setting specifically, Bondarenko et al.~\\cite{bondarenko-spec-gaming} demonstrate specification gaming in reasoning models, Kim et al.~\\cite{kim-game-formalization} evaluate whether LLMs game logical formalization tasks, and Yang et al.~\\cite{spurious-rewards} identify spurious reward signals in RLVR that inflate metrics without genuine capability gains.\nThis literature analyzes Goodhart dynamics either theoretically or within RLHF/text generation, where the proxy is a learned reward model.\nOur setting differs in two respects: the proxy (ISR) is deterministic and solver-derived, eliminating reward model noise as an explanation; and the Goodhart effect operates at a \\emph{meta} level---ISR was designed to \\emph{detect} gaming of execution reward, yet itself becomes gamed when optimized.\nThe dose-response pattern we observe ($\\beta{=}0.1$: proxy gaming via conclusion duplication; $\\beta{=}0.3$: performance collapse) traces the trajectory predicted by Gao et al.~\\cite{gao-reward-overoptimization} within a single neurosymbolic RL setup, and the premise-count confound that explains away apparent ISR improvements provides a concrete mechanism for regressional Goodhart in formal reasoning.\n\n\\paragraph{Mutation Testing and Component Analysis.}\nMutation testing originated with DeMillo et al.~\\cite{demillo1978}, who proposed injecting systematic faults into programs to assess test suite adequacy; the coupling effect hypothesis~\\cite{offutt-coupling} provides the theoretical grounding that simple mutants subsume complex faults.\nJia and Harman~\\cite{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation as the dominant paradigm, while Just et al.~\\cite{just-mutants-real-faults} validate that synthetic mutants approximate real faults in detection experiments.\nRecent work connects mutation testing with LLMs: LLMorpheus~\\cite{llmorpheus} uses language models to generate semantically rich mutants that go beyond syntactic operators.\nSTA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.\nThe unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity for proof validity.\nThe novelty lies not in the perturbation technique itself but in its application to neurosymbolic RL and the empirical findings it enables: the ISR collapse trajectory, the Goodhart phenomenon, and the taxonomy of hacking modes.\n\n\\paragraph{Positioning.}\nThis work sits at the intersection of neurosymbolic reasoning, reward design, and Goodhart dynamics.\nWhere prior neurosymbolic systems evaluate on execution accuracy alone, STA provides a structural diagnostic; where prior reward-shaping work assumes that finer-grained signals safely improve training, our ISR-as-reward experiments demonstrate meta-level Goodhart failure; and where prior Goodhart analyses study learned reward models, we show the same dynamics arise from a deterministic, solver-grounded metric.\nThe mutation-testing connection provides the methodological foundation, but the contributions are empirical: structural collapse under RL, meta-level gaming of the diagnostic itself, and a taxonomy of exploitation strategies across formal languages.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "d83a1ba0-8546-4b46-b263-0d7faa3dc008",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019e3VBAeFwyKkbJrKPTw2MD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9420,
      "cache_read_input_tokens": 33210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9420
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

_source line 22 · 2026-05-14T19:31:47.185Z_

<details><summary>↩ Tool result · `toolu_014ZpnJPAueSfeHRt9Esv9HZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "0333b3ec-bf3e-44df-a312-2719aa632ea3",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Neurosymbolic Reasoning with LLMs.}\nPrompting-based pipelines couple LLMs with external solvers to offload logical inference.\nLogic-LM~\\cite{logic-lm} generates FOL formalizations verified by an external prover, with a self-refinement loop on solver errors; LINC~\\cite{linc} similarly translates natural language to first-order logic for Prover9, demonstrating gains over chain-of-thought on syllogistic and multi-hop tasks.\nSatLM~\\cite{satlm} extends the paradigm to satisfiability solvers via declarative prompting, while LoRP~\\cite{lorp} and FoVer~\\cite{fover-pei2025} route through Prolog execution traces and FOL verification, respectively, to validate or filter LLM-generated reasoning.\nAll of these systems evaluate on execution accuracy---whether the solver returns the correct answer---without diagnosing the structural quality of the generated formalizations.\nRL-based training represents a more recent direction.\nMellgren~\\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning.\nThese RL systems optimize execution reward exclusively, reporting prove rate as the primary success metric.\nOur work differs in diagnostic focus: STA reveals that execution accuracy conflates faithful derivation with degenerate shortcuts, and ISR quantifies this conflation.\nThe finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\\S\\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.\n\n\\paragraph{Reward Shaping and Process Supervision.}\nBinary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.\nLightman et al.~\\cite{lightman-verify-step} train process reward models (PRMs) that score individual reasoning steps, improving mathematical problem-solving over outcome-only rewards.\nMath-Shepherd~\\cite{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.\nBeyond learned PRMs, symbolic feedback offers an alternative grounding: RLSF~\\cite{rlsf} uses solver diagnostics as a structured training signal for formal reasoning, and Rubric-GRPO~\\cite{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge.\nHowever, process rewards introduce their own failure modes.\nGao et al.~\\cite{gao-effective-rl-reward} show that reward design choices---granularity, normalization, aggregation---can dominate the effect of the underlying signal.\nPROF~\\cite{prof-process-outcome} finds that process and outcome rewards conflict under joint optimization, requiring explicit harmonization.\nThe Qwen PRM study~\\cite{qwen-prm-lessons} documents that PRMs degrade unpredictably at distribution shift, and ProGRS~\\cite{progrs-outcome-conditioned} introduces outcome-conditioned process rewards to mitigate the gap between step-level correctness and final-answer accuracy.\nISR differs from these approaches in that it is solver-grounded rather than learned: it derives directly from deterministic LOO ablation of solver inputs, eliminating reward model noise.\nOur finding that ISR reliably \\emph{diagnoses} structural quality yet becomes the target of gaming when used as a training reward (\\S\\ref{sec:goodhart}) adds an empirical data point to this literature: even non-learned process signals can Goodhart when optimized.\n\n\\paragraph{Reward Hacking and Goodhart's Law.}\nGao et al.~\\cite{gao-reward-overoptimization} establish scaling laws for reward model overoptimization, showing that proxy reward increases monotonically with optimization pressure until true performance collapses.\nManheim and Garrabrant~\\cite{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---while Skalse et al.~\\cite{skalse-reward-hacking} prove that reward hacking is generically unavoidable for imperfect proxies.\nKarwowski et al.~\\cite{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization; Pan et al.~\\cite{pan-reward-misspecification} map how misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment; and Kwa et al.~\\cite{kwa-catastrophic-goodhart} show that KL divergence regularization fails catastrophically under heavy-tailed reward misspecification.\nIn the LLM setting specifically, Bondarenko et al.~\\cite{bondarenko-spec-gaming} demonstrate specification gaming in reasoning models, Kim et al.~\\cite{kim-game-formalization} evaluate whether LLMs game logical formalization tasks, and Yang et al.~\\cite{spurious-rewards} identify spurious reward signals in RLVR that inflate metrics without genuine capability gains.\nThis literature analyzes Goodhart dynamics either theoretically or within RLHF/text generation, where the proxy is a learned reward model.\nOur setting differs in two respects: the proxy (ISR) is deterministic and solver-derived, eliminating reward model noise as an explanation; and the Goodhart effect operates at a \\emph{meta} level---ISR was designed to \\emph{detect} gaming of execution reward, yet itself becomes gamed when optimized.\nThe dose-response pattern we observe ($\\beta{=}0.1$: proxy gaming via conclusion duplication; $\\beta{=}0.3$: performance collapse) traces the trajectory predicted by Gao et al.~\\cite{gao-reward-overoptimization} within a single neurosymbolic RL setup, and the premise-count confound that explains away apparent ISR improvements provides a concrete mechanism for regressional Goodhart in formal reasoning.\n\n\\paragraph{Mutation Testing and Component Analysis.}\nMutation testing originated with DeMillo et al.~\\cite{demillo1978}, who proposed injecting systematic faults into programs to assess test suite adequacy; the coupling effect hypothesis~\\cite{offutt-coupling} provides the theoretical grounding that simple mutants subsume complex faults.\nJia and Harman~\\cite{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation as the dominant paradigm, while Just et al.~\\cite{just-mutants-real-faults} validate that synthetic mutants approximate real faults in detection experiments.\nRecent work connects mutation testing with LLMs: LLMorpheus~\\cite{llmorpheus} uses language models to generate semantically rich mutants that go beyond syntactic operators.\nSTA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.\nThe unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity for proof validity.\nThe novelty lies not in the perturbation technique itself but in its application to neurosymbolic RL and the empirical findings it enables: the ISR collapse trajectory, the Goodhart phenomenon, and the taxonomy of hacking modes.\n\n\\paragraph{Positioning.}\nThis work sits at the intersection of neurosymbolic reasoning, reward design, and Goodhart dynamics.\nWhere prior neurosymbolic systems evaluate on execution accuracy alone, STA provides a structural diagnostic; where prior reward-shaping work assumes that finer-grained signals safely improve training, our ISR-as-reward experiments demonstrate meta-level Goodhart failure; and where prior Goodhart analyses study learned reward models, we show the same dynamics arise from a deterministic, solver-grounded metric.\nThe mutation-testing connection provides the methodological foundation, but the contributions are empirical: structural collapse under RL, meta-level gaming of the diagnostic itself, and a taxonomy of exploitation strategies across formal languages.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 50,
        "newStart": 1,
        "newLines": 47,
        "lines": [
          " \\section{Related Work}",
          " \\label{sec:related-work}",
          " ",
          "-\\paragraph{Mutation Testing and Component Analysis.}",
          "-Mutation testing originated with \\citet{demillo1978}, who proposed systematically injecting faults into programs to assess test suite adequacy.",
          "-\\citet{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation operators as the dominant paradigm for software quality assurance, while \\citet{just-mutants-real-faults} validate that synthetic mutants approximate real faults in fault-detection experiments.",
          "-This body of work operates exclusively within software testing: mutants perturb \\emph{program code} to evaluate \\emph{test suites}, not solver inputs to evaluate reasoning quality.",
          "-STA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.",
          "-The unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity of each component for proof validity.",
          "+\\paragraph{Neurosymbolic Reasoning with LLMs.}",
          "+Prompting-based pipelines couple LLMs with external solvers to offload logical inference.",
          "+Logic-LM~\\cite{logic-lm} generates FOL formalizations verified by an external prover, with a self-refinement loop on solver errors; LINC~\\cite{linc} similarly translates natural language to first-order logic for Prover9, demonstrating gains over chain-of-thought on syllogistic and multi-hop tasks.",
          "+SatLM~\\cite{satlm} extends the paradigm to satisfiability solvers via declarative prompting, while LoRP~\\cite{lorp} and FoVer~\\cite{fover-pei2025} route through Prolog execution traces and FOL verification, respectively, to validate or filter LLM-generated reasoning.",
          "+All of these systems evaluate on execution accuracy---whether the solver returns the correct answer---without diagnosing the structural quality of the generated formalizations.",
          "+RL-based training represents a more recent direction.",
          "+Mellgren~\\cite{mellgren-prolog-grpo} applies GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains; Logic-RL~\\cite{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning in LLMs; and Thought-Like-Pro~\\cite{thought-like-pro} uses self-driven Prolog chain-of-thought to enhance multi-step reasoning.",
          "+These RL systems optimize execution reward exclusively, reporting prove rate as the primary success metric.",
          "+Our work differs in diagnostic focus: STA reveals that execution accuracy conflates faithful derivation with degenerate shortcuts, and ISR quantifies this conflation.",
          "+The finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\\S\\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.",
          " ",
          " \\paragraph{Reward Shaping and Process Supervision.}",
          " Binary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.",
          "-\\citet{lightman-verify-step} train process reward models that score individual reasoning steps, demonstrating improved mathematical problem-solving over outcome-only rewards.",
          "-Math-Shepherd~\\citep{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.",
          "-RLSF~\\citep{rlsf} grounds reward in symbolic execution feedback, using solver diagnostics as a structured training signal for formal reasoning tasks.",
          "-Rubric-GRPO~\\citep{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge, decomposing quality into interpretable axes.",
          "-These approaches share an implicit assumption: that finer-grained reward signals are reliable proxies for reasoning quality and can safely serve as optimization targets.",
          "-Our work challenges this assumption directly.",
          "-ISR provides a solver-grounded process signal that reliably \\emph{diagnoses} structural quality when used as a post-hoc metric, yet becomes the target of gaming when incorporated into the reward---instantiating meta-level Goodhart's Law (\\S\\ref{sec:goodhart}).",
          "-The failure mode is not reward noise or annotation error but systematic exploitation of the metric's measurement mechanism.",
          "+Lightman et al.~\\cite{lightman-verify-step} train process reward models (PRMs) that score individual reasoning steps, improving mathematical problem-solving over outcome-only rewards.",
          "+Math-Shepherd~\\cite{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.",
          "+Beyond learned PRMs, symbolic feedback offers an alternative grounding: RLSF~\\cite{rlsf} uses solver diagnostics as a structured training signal for formal reasoning, and Rubric-GRPO~\\cite{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge.",
          "+However, process rewards introduce their own failure modes.",
          "+Gao et al.~\\cite{gao-effective-rl-reward} show that reward design choices---granularity, normalization, aggregation---can dominate the effect of the underlying signal.",
          "+PROF~\\cite{prof-process-outcome} finds that process and outcome rewards conflict under joint optimization, requiring explicit harmonization.",
          "+The Qwen PRM study~\\cite{qwen-prm-lessons} documents that PRMs degrade unpredictably at distribution shift, and ProGRS~\\cite{progrs-outcome-conditioned} introduces outcome-conditioned process rewards to mitigate the gap between step-level correctness and final-answer accuracy.",
          "+ISR differs from these approaches in that it is solver-grounded rather than learned: it derives directly from deterministic LOO ablation of solver inputs, eliminating reward model noise.",
          "+Our finding that ISR reliably \\emph{diagnoses} structural quality yet becomes the target of gaming when used as a training reward (\\S\\ref{sec:goodhart}) adds an empirical data point to this literature: even non-learned process signals can Goodhart when optimized.",
          " ",
          " \\paragraph{Reward Hacking and Goodhart's Law.}",
          "-\\citet{gao-reward-overoptimization} establish scaling laws for reward model overoptimization in RLHF, showing that proxy reward increases monotonically with optimization pressure until a critical point where true performance collapses.",
          "-\\citet{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---providing the theoretical vocabulary for analyzing proxy-target divergence.",
          "-\\citet{skalse-reward-hacking} formalize reward hacking as misalignment between the proxy and true reward under optimization, proving that hacking is generically unavoidable for imperfect proxies.",
          "-\\citet{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization.",
          "-\\citet{pan-reward-misspecification} map the effects of reward misspecification across environments, finding that misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment.",
          "-This literature analyzes Goodhart dynamics theoretically or within RLHF and text generation, where the proxy is a learned reward model.",
          "-Our setting differs in two respects.",
          "-First, the proxy (ISR) is not learned but derived from a deterministic solver, eliminating reward model noise as an explanation.",
          "-Second, the Goodhart effect operates at a \\emph{meta} level: ISR was designed to detect gaming of execution reward, yet itself becomes gamed when optimized.",
          "-The dose-response pattern we observe ($\\beta{=}0.1$: proxy gaming via conclusion duplication; $\\beta{=}0.3$: performance collapse) traces the trajectory predicted by \\citet{gao-reward-overoptimization} within a single neurosymbolic RL setup.",
          "+Gao et al.~\\cite{gao-reward-overoptimization} establish scaling laws for reward model overoptimization, showing that proxy reward increases monotonically with optimization pressure until true performance collapses.",
          "+Manheim and Garrabrant~\\cite{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---while Skalse et al.~\\cite{skalse-reward-hacking} prove that reward hacking is generically unavoidable for imperfect proxies.",
          "+Karwowski et al.~\\cite{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization; Pan et al.~\\cite{pan-reward-misspecification} map how misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment; and Kwa et al.~\\cite{kwa-catastrophic-goodhart} show that KL divergence regularization fails catastrophically under heavy-tailed reward misspecification.",
          "+In the LLM setting specifically, Bondarenko et al.~\\cite{bondarenko-spec-gaming} demonstrate specification gaming in reasoning models, Kim et al.~\\cite{kim-game-formalization} evaluate whether LLMs game logical formalization tasks, and Yang et al.~\\cite{spurious-rewards} identify spurious reward signals in RLVR that inflate metrics without genuine capability gains.",
          "+This literature analyzes Goodhart dynamics either theoretically or within RLHF/text generation, where the proxy is a learned reward model.",
          "+Our setting differs in two respects: the proxy (ISR) is deterministic and solver-derived, eliminating reward model noise as an explanation; and the Goodhart effect operates at a \\emph{meta} level---ISR was designed to \\emph{detect} gaming of execution reward, yet itself becomes gamed when optimized.",
          "+The dose-response pattern we observe ($\\beta{=}0.1$: proxy gaming via conclusion duplication; $\\beta{=}0.3$: performance collapse) traces the trajectory predicted by Gao et al.~\\cite{gao-reward-overoptimization} within a single neurosymbolic RL setup, and the premise-count confound that explains away apparent ISR improvements provides a concrete mechanism for regressional Goodhart in formal reasoning.",
          " ",
          "-\\paragraph{Neurosymbolic Reasoning with LLMs.}",
          "-Prompting-based pipelines couple LLMs with external solvers for logical reasoning.",
          "-Logic-LM~\\citep{logic-lm} uses in-context examples to generate FOL formalizations verified by an external prover, with a self-refinement loop on solver errors.",
          "-LINC~\\citep{linc} similarly translates natural language to first-order logic for Prover9 verification, demonstrating that solver-backed approaches outperform chain-of-thought on syllogistic and multi-hop tasks.",
          "-SatLM~\\citep{satlm} extends this paradigm to satisfiability solvers via declarative prompting.",
          "-These systems evaluate exclusively on execution accuracy---whether the solver returns the correct answer---without diagnosing structural quality of the generated formalizations.",
          "+\\paragraph{Mutation Testing and Component Analysis.}",
          "+Mutation testing originated with DeMillo et al.~\\cite{demillo1978}, who proposed injecting systematic faults into programs to assess test suite adequacy; the coupling effect hypothesis~\\cite{offutt-coupling} provides the theoretical grounding that simple mutants subsume complex faults.",
          "+Jia and Harman~\\cite{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation as the dominant paradigm, while Just et al.~\\cite{just-mutants-real-faults} validate that synthetic mutants approximate real faults in detection experiments.",
          "+Recent work connects mutation testing with LLMs: LLMorpheus~\\cite{llmorpheus} uses language models to generate semantically rich mutants that go beyond syntactic operators.",
          "+STA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.",
          "+The unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity for proof validity.",
          "+The novelty lies not in the perturbation technique itself but in its application to neurosymbolic RL and the empirical findings it enables: the ISR collapse trajectory, the Goodhart phenomenon, and the taxonomy of hacking modes.",
          " ",
          "-Verification-oriented approaches add post-hoc analysis.",
          "-LoRP~\\citep{lorp} uses Prolog execution traces to verify LLM reasoning chains, and FoVer~\\citep{fover-pei2025} employs first-order logic verification to filter training data for process reward models.",
          "-Both treat solver verification as a binary quality gate rather than a structural diagnostic.",
          "-",
          "-RL-based training represents the closest line of work.",
          "-\\citet{mellgren-prolog-grpo} apply GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains.",
          "-Logic-RL~\\citep{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning capabilities in LLMs.",
          "-Both systems optimize execution reward exclusively, reporting prove rate as the primary metric.",
          "-STA addresses the structural blind spot common to all these approaches: execution accuracy conflates faithful multi-step derivation with degenerate shortcuts (conclusion embedding, tautological collapse), and ISR quantifies this conflation.",
          "-Our finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\\S\\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.",
          "+\\paragraph{Positioning.}",
          "+This work sits at the intersection of neurosymbolic reasoning, reward design, and Goodhart dynamics.",
          "+Where prior neurosymbolic systems evaluate on execution accuracy alone, STA provides a structural diagnostic; where prior reward-shaping work assumes that finer-grained signals safely improve training, our ISR-as-reward experiments demonstrate meta-level Goodhart failure; and where prior Goodhart analyses study learned reward models, we show the same dynamics arise from a deterministic, solver-grounded metric.",
          "+The mutation-testing connection provides the methodological foundation, but the contributions are empirical: structural collapse under RL, meta-level gaming of the diagnostic itself, and a taxonomy of exploitation strategies across formal languages."
        ]
      }
    ],
    "originalFile": "\\section{Related Work}\n\\label{sec:related-work}\n\n\\paragraph{Mutation Testing and Component Analysis.}\nMutation testing originated with \\citet{demillo1978}, who proposed systematically injecting faults into programs to assess test suite adequacy.\n\\citet{jia-harman-survey} survey three decades of development, establishing leave-one-out and higher-order mutation operators as the dominant paradigm for software quality assurance, while \\citet{just-mutants-real-faults} validate that synthetic mutants approximate real faults in fault-detection experiments.\nThis body of work operates exclusively within software testing: mutants perturb \\emph{program code} to evaluate \\emph{test suites}, not solver inputs to evaluate reasoning quality.\nSTA adapts the core LOO intuition to a different domain---formal logic formalizations---where the ``program under test'' is the solver input and the ``test'' is proof success.\nThe unit of mutation shifts from code statements to logical components (premises in FOL, clauses in Prolog), and the diagnostic target shifts from test adequacy to structural necessity of each component for proof validity.\n\n\\paragraph{Reward Shaping and Process Supervision.}\nBinary outcome rewards provide no gradient on intermediate reasoning quality, motivating process-level supervision.\n\\citet{lightman-verify-step} train process reward models that score individual reasoning steps, demonstrating improved mathematical problem-solving over outcome-only rewards.\nMath-Shepherd~\\citep{math-shepherd} automates step-level annotation by validating intermediate states against reference solutions.\nRLSF~\\citep{rlsf} grounds reward in symbolic execution feedback, using solver diagnostics as a structured training signal for formal reasoning tasks.\nRubric-GRPO~\\citep{rubric-grpo} replaces scalar rewards with multi-dimensional rubric scores evaluated by an LLM judge, decomposing quality into interpretable axes.\nThese approaches share an implicit assumption: that finer-grained reward signals are reliable proxies for reasoning quality and can safely serve as optimization targets.\nOur work challenges this assumption directly.\nISR provides a solver-grounded process signal that reliably \\emph{diagnoses} structural quality when used as a post-hoc metric, yet becomes the target of gaming when incorporated into the reward---instantiating meta-level Goodhart's Law (\\S\\ref{sec:goodhart}).\nThe failure mode is not reward noise or annotation error but systematic exploitation of the metric's measurement mechanism.\n\n\\paragraph{Reward Hacking and Goodhart's Law.}\n\\citet{gao-reward-overoptimization} establish scaling laws for reward model overoptimization in RLHF, showing that proxy reward increases monotonically with optimization pressure until a critical point where true performance collapses.\n\\citet{manheim-goodhart-taxonomy} taxonomize four variants of Goodhart's Law---regressional, extremal, causal, and adversarial---providing the theoretical vocabulary for analyzing proxy-target divergence.\n\\citet{skalse-reward-hacking} formalize reward hacking as misalignment between the proxy and true reward under optimization, proving that hacking is generically unavoidable for imperfect proxies.\n\\citet{karwowski-goodhart-rl} demonstrate Goodhart dynamics geometrically in RL, showing that KL regularization delays but does not prevent overoptimization.\n\\citet{pan-reward-misspecification} map the effects of reward misspecification across environments, finding that misspecified rewards produce qualitatively different failure modes depending on the degree of misalignment.\nThis literature analyzes Goodhart dynamics theoretically or within RLHF and text generation, where the proxy is a learned reward model.\nOur setting differs in two respects.\nFirst, the proxy (ISR) is not learned but derived from a deterministic solver, eliminating reward model noise as an explanation.\nSecond, the Goodhart effect operates at a \\emph{meta} level: ISR was designed to detect gaming of execution reward, yet itself becomes gamed when optimized.\nThe dose-response pattern we observe ($\\beta{=}0.1$: proxy gaming via conclusion duplication; $\\beta{=}0.3$: performance collapse) traces the trajectory predicted by \\citet{gao-reward-overoptimization} within a single neurosymbolic RL setup.\n\n\\paragraph{Neurosymbolic Reasoning with LLMs.}\nPrompting-based pipelines couple LLMs with external solvers for logical reasoning.\nLogic-LM~\\citep{logic-lm} uses in-context examples to generate FOL formalizations verified by an external prover, with a self-refinement loop on solver errors.\nLINC~\\citep{linc} similarly translates natural language to first-order logic for Prover9 verification, demonstrating that solver-backed approaches outperform chain-of-thought on syllogistic and multi-hop tasks.\nSatLM~\\citep{satlm} extends this paradigm to satisfiability solvers via declarative prompting.\nThese systems evaluate exclusively on execution accuracy---whether the solver returns the correct answer---without diagnosing structural quality of the generated formalizations.\n\nVerification-oriented approaches add post-hoc analysis.\nLoRP~\\citep{lorp} uses Prolog execution traces to verify LLM reasoning chains, and FoVer~\\citep{fover-pei2025} employs first-order logic verification to filter training data for process reward models.\nBoth treat solver verification as a binary quality gate rather than a structural diagnostic.\n\nRL-based training represents the closest line of work.\n\\citet{mellgren-prolog-grpo} apply GRPO to train Prolog formalizers with binary solver reward, reporting substantial prove-rate gains.\nLogic-RL~\\citep{logic-rl} demonstrates that rule-based RL with solver feedback elicits emergent reasoning capabilities in LLMs.\nBoth systems optimize execution reward exclusively, reporting prove rate as the primary metric.\nSTA addresses the structural blind spot common to all these approaches: execution accuracy conflates faithful multi-step derivation with degenerate shortcuts (conclusion embedding, tautological collapse), and ISR quantifies this conflation.\nOur finding that 87\\% of proved outputs under exec-only GRPO embed the conclusion among the premises (\\S\\ref{sec:diagnostic}) applies directly to these systems, suggesting that reported prove-rate gains may overstate genuine reasoning improvement.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 23_

Let me verify the word count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "7d068aee-c4fa-46fc-ad57-0e8e7b5b2bd5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dCFw36QhMauFhQ26mokUe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3212,
      "cache_read_input_tokens": 42630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3212
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

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01VW3cMg4J1cAaw3zTX9h6yr`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}~$]//g; s/%.*//g' | wc -w",
  "description": "Estimate word count of related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "e57ad90a-d63e-4048-a799-7f55499a3487",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dCFw36QhMauFhQ26mokUe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3212,
      "cache_read_input_tokens": 42630,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3212
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

_source line 25 · 2026-05-14T19:31:54.098Z_

<details><summary>↩ Tool result · `toolu_01VW3cMg4J1cAaw3zTX9h6yr`</summary>

```text
915
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "3466cfb9-56b3-45a5-ba97-ac5153dbc752",
  "tool_use_result": {
    "stdout": "915",
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

_source line 26_

~915 words. Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "d33eee03-7620-45a6-8064-935b2fa87e58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNdJ5rp5d5vd8dosuKq5vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 191,
      "cache_read_input_tokens": 45842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 191
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

_source line 27_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AKdwSxnEV5G6tWkKyhXFn1`</summary>

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
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "076b75b3-d4f4-4088-a82a-372df159b79e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SNdJ5rp5d5vd8dosuKq5vm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 191,
      "cache_read_input_tokens": 45842,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 191
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

_source line 28 · 2026-05-14T19:31:57.083Z_

<details><summary>↩ Tool result · `toolu_01AKdwSxnEV5G6tWkKyhXFn1`</summary>

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
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "76f674d5-2b2c-4e03-88ef-3b12a8d46ec4",
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

_source line 29_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01DKpgFNym9fgeWdgwjPHrQu`</summary>

```json
{
  "name": "related_work.tex",
  "type": "paper",
  "description": "§2 Related Work for EMNLP 2026 paper (~915 words). 4 clusters: Neurosymbolic Reasoning, Reward Shaping & Process Supervision, Reward Hacking & Goodhart's Law, Mutation Testing & Component Analysis, plus positioning paragraph.",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/paper/related_work.tex",
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
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "7d5c3ddb-de9d-455d-8cf3-8d21b4ad11e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Ceu88BVFeHowmqm4Hcg5G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 46033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
      },
      "output_tokens": 68,
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

_source line 30 · 2026-05-14T19:32:02.038Z_

<details><summary>↩ Tool result · `toolu_01DKpgFNym9fgeWdgwjPHrQu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_b8a377\", \"name\": \"related_work.tex\", \"type\": \"paper\", \"description\": \"§2 Related Work for EMNLP 2026 paper (~915 words). 4 clusters: Neurosymbolic Reasoning, Reward Shaping & Process Supervision, Reward Hacking & Goodhart's Law, Mutation Testing & Component Analysis, plus positioning paragraph.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T19:32:01.920300+00:00\", \"tags\": [\"paper\", \"related-work\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "9052b683-6766-4cf9-a0b5-27aa38ba2f24",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_b8a377\\\", \\\"name\\\": \\\"related_work.tex\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"§2 Related Work for EMNLP 2026 paper (~915 words). 4 clusters: Neurosymbolic Reasoning, Reward Shaping & Process Supervision, Reward Hacking & Goodhart's Law, Mutation Testing & Component Analysis, plus positioning paragraph.\\\", \\\"path\\\": \\\"projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"solver-trace-ablation\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T19:32:01.920300+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"related-work\\\", \\\"latex\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_b8a377\", \"name\": \"related_work.tex\", \"type\": \"paper\", \"description\": \"§2 Related Work for EMNLP 2026 paper (~915 words). 4 clusters: Neurosymbolic Reasoning, Reward Shaping & Process Supervision, Reward Hacking & Goodhart's Law, Mutation Testing & Component Analysis, plus positioning paragraph.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/paper/related_work.tex\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T19:32:01.920300+00:00\", \"tags\": [\"paper\", \"related-work\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 31_

`related_work.tex` 已重写完成（~915 words）。主要变更：

- **重排为 4 cluster + positioning 结构**：Neurosymbolic Reasoning → Reward Shaping → Reward Hacking → Mutation Testing → Positioning
- **补全缺失引用**：Thought-Like-Pro, gao-effective-rl-reward, prof-process-outcome, qwen-prm-lessons, progrs-outcome-conditioned, kwa-catastrophic-goodhart, bondarenko-spec-gaming, kim-game-formalization, spurious-rewards, offutt-coupling, llmorpheus
- **统一引用格式**：`\citet`/`\citep` → `\cite`
- **新增 positioning 段**：总结论文在四个 cluster 交叉点的定位
- **每段结尾明确 our distinction**，用 "differs in" 而非贬义措辞

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "uuid": "71e8f003-540f-4153-b6e9-009f27e850f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GjBkSaGfj1f5tMobcMuR8t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 577,
      "cache_read_input_tokens": 46758,
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

_source line 32_

`related_work.tex` 已重写完成（~915 words）。主要变更：

- **重排为 4 cluster + positioning 结构**：Neurosymbolic Reasoning → Reward Shaping → Reward Hacking → Mutation Testing → Positioning
- **补全缺失引用**：Thought-Like-Pro, gao-effective-rl-reward, prof-process-outcome, qwen-prm-lessons, progrs-outcome-conditioned, kwa-catastrophic-goodhart, bondarenko-spec-gaming, kim-game-formalization, spurious-rewards, offutt-coupling, llmorpheus
- **统一引用格式**：`\citet`/`\citep` → `\cite`
- **新增 positioning 段**：总结论文在四个 cluster 交叉点的定位
- **每段结尾明确 our distinction**，用 "differs in" 而非贬义措辞

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 89884,
  "duration_api_ms": 90715,
  "num_turns": 11,
  "stop_reason": "end_turn",
  "session_id": "a9b03799-9a9a-40f0-b9a4-fe3652935012",
  "total_cost_usd": 0.47715450000000004,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 35494,
    "cache_read_input_tokens": 284190,
    "output_tokens": 4417,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35494,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 247,
        "cache_read_input_tokens": 46758,
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
      "inputTokens": 2637,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002742,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 4417,
      "cacheReadInputTokens": 284190,
      "cacheCreationInputTokens": 35494,
      "webSearchRequests": 0,
      "costUSD": 0.4744125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "27929178-a1d3-47c5-90c5-12c8ae90f7f2"
}
```

</details>

---
