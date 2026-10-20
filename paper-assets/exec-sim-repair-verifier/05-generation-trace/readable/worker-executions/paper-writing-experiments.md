# paper writing experiments

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260515T091611.log`
- **Structured JSON:** [`7d28e60111ee0bf703a7.json`](../../sessions/7d/7d28e60111ee0bf703a7.json)

## Before a recorded user message

27 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier",
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
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
  "uuid": "392e8f46-9401-47c4-bbb6-714f57170a34",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-16-projects-exec-sim-repair-verifier/memory/"
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
    "resetsAt": 1779206400,
    "rateLimitType": "seven_day",
    "utilization": 0.77,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "800041de-3adf-4c71-acde-896445ec9dcd",
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a"
}
```

---

### Assistant

_source line 4_

I'll start by reading the three required files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "8557671b-0a60-4729-8cc4-f4f6121b3ee9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM6ggHqBv2EfzjLH4NiZJD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13426,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13426
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

<details open><summary>🔧 Tool call — Read · `toolu_01Aq8uLWmFsobZpvTFkyUMaB`</summary>

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
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "addd9ce5-4c72-49db-9c4b-dd381b9bf016",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM6ggHqBv2EfzjLH4NiZJD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13426,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13426
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

_source line 6 · 2026-05-15T09:16:21.905Z_

<details><summary>↩ Tool result · `toolu_01Aq8uLWmFsobZpvTFkyUMaB`</summary>

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
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "e6a99fac-7ffb-4da3-bde5-62c7c2e9488e",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Jqb1PND1Na14T6s3RdVVXu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "b7bfc736-a0ea-4eb8-a29f-f12f043909f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM6ggHqBv2EfzjLH4NiZJD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13426,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13426
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

_source line 8 · 2026-05-15T09:16:22.372Z_

<details><summary>↩ Tool result · `toolu_01Jqb1PND1Na14T6s3RdVVXu`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate \cls{}, \cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.
5	
6	\subsection{Experimental Setup}
7	\label{sec:setup}
8	
9	\paragraph{Dataset.}
10	We construct a function-level benchmark from HumanEval~\cite{chen2021humaneval} and MBPP~\cite{austin2021mbpp} by generating mutated variants (five mutation types: \texttt{wrong\_operator}, \texttt{off\_by\_one}, \texttt{boundary\_error}, \texttt{return\_value}, \texttt{type\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\approx$ 52:48, majority baseline 51.75\%).
11	
12	\paragraph{Models and training.}
13	We fine-tune Qwen3-4B and Qwen3-8B~\cite{yang2024qwen25} with LoRA~\cite{hu2022lora} (rank 16, lr $2{\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.
14	
15	\paragraph{Oracle analysis and statistics.}
16	We use SWE-bench Verified~\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\S\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\ trajectory-level comparison uses TOST~\cite{schuirmann1987tost} with $\pm$2\pp{} margin.
17	
18	
19	\subsection{Function-Level Results}
20	\label{sec:func_results}
21	
22	Table~\ref{tab:main_results} reports function-level results across formulations.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \cls{}: per-test binary classification; \cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\pm$ std over seeds reported where applicable.}
28	\label{tab:main_results}
29	\resizebox{\columnwidth}{!}{%
30	\setlength{\tabcolsep}{4pt}
31	\begin{tabular}{llcc}
32	\toprule
33	\textbf{Method} & \textbf{Model} & \textbf{Seeds} & \textbf{Accuracy (\%)} \\
34	\midrule
35	\cls{} (fine-tuned) & 4B & 5 & \textbf{88.43 $\pm$ 0.78} \\
36	\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\pm$ 0.36 \\
37	TRAJ (fine-tuned) & 4B & 5 & 86.30 $\pm$ 0.97 \\
38	\midrule
39	ZS LLM-as-judge & 8B & 1 & 64.40 \\
40	ZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\
41	\bottomrule
42	\end{tabular}}
43	\end{table}
44	
45	Fine-tuned \cls{} achieves a mean accuracy of 88.43\% ($\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\% ($\pm$0.36; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \cwm{} and 86.30\% ($\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \cls{}--\cwm{} gap is 1.24\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.
46	
47	Zero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\% and Qwen3-32B (NF4) achieves 71.69\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\%, pass recall 35.1\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \cls{} by 16.74\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.
48	
49	
50	\subsection{Scaling Behavior}
51	\label{sec:scaling}
52	
53	Table~\ref{tab:scaling} compares \cls{} and \cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.
54	
55	\begin{table}[t]
56	\centering
57	\small
58	\caption{Model-size scaling: \cls{} vs.\ \cwm{} accuracy (\%) at 4B and 8B. Three matched seeds in full precision. The \cls{}--\cwm{} gap widens from 1.18\pp{} to 2.43\pp{}.}
59	\label{tab:scaling}
60	\setlength{\tabcolsep}{4pt}
61	\begin{tabular}{llccccc}
62	\toprule
63	\textbf{Method} & \textbf{Size} & \textbf{s42} & \textbf{s123} & \textbf{s456} & \textbf{Mean} & \textbf{Gap} \\
64	\midrule
65	\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \multirow{2}{*}{1.18} \\
66	\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\
67	\midrule
68	\cls{} & 8B & \textbf{90.48} & 89.40 & 88.31 & \textbf{89.40} & \multirow{2}{*}{\textbf{2.43}} \\
69	\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\
70	\bottomrule
71	\end{tabular}
72	\end{table}
73	
74	At 4B, \cls{} and \cwm{} are separated by 1.18\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\pp{} ($p = 0.0066$, 95\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.
75	
76	The asymmetry in scaling efficiency is striking: from 4B to 8B, \cls{} gains +0.99\pp{} (88.41 $\to$ 89.40) while \cwm{} loses $-$0.27\pp{} (87.23 $\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \cwm{} accuracy. However, the \cwm{} regression ($-$0.27\pp{}) falls within seed noise (3-seed std ${\sim}$0.5\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\ref{fig:scaling_gap} visualizes the diverging trajectories.
77	
78	
79	\subsection{Per-Test vs.\ Trajectory-Level Equivalence}
80	\label{sec:equivalence}
81	
82	A natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.
83	
84	The pooled gap is $-$0.45\pp{} (95\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\pm$2\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.
85	
86	Critically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\ confidence intervals would be approximately $2\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.
87	
88	The practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.
89	
90	
91	\subsection{Accuracy-Utility Frontier}
92	\label{sec:oracle-results}
93	
94	Where does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\ trajectory-level oracle resolve rates under both i.i.d.\ and block-correlated error models (using the empirical ICC $= 0.191$).
95	
96	\begin{table}[t]
97	\centering
98	\small
99	\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\% mean, 0\% median.}
100	\label{tab:oracle}
101	\resizebox{\columnwidth}{!}{%
102	\setlength{\tabcolsep}{3pt}
103	\begin{tabular}{lcccc}
104	\toprule
105	\textbf{$T$} & \textbf{Inst.\%} & \textbf{i.i.d.\ (\pp{})} & \textbf{Block (\pp{})} & \textbf{Contrib.\%} \\
106	\midrule
107	$1$ & 68.7 & $-$0.04 & $-$0.09 & $\approx$0 \\
108	$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\
109	$3$--$5$ & 7.1 & 25.00 & 40.74 & $\approx$26 \\
110	$\geq 6$ & 5.1 & 30.00 & 40.06 & $\approx$19 \\
111	\midrule
112	\textbf{All} & 100.0 & --- & \textbf{10.93} & 100.0 \\
113	\bottomrule
114	\end{tabular}}
115	\end{table}
116	
117	Table~\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\% of instances), where block-correlated advantage reaches 31.69\pp{}, contributing 55.3\% of the total advantage. Instances with $T \geq 3$ exhibit block advantages exceeding 40\pp{} but constitute only 12.2\% of instances. The overall block-correlated advantage is 10.93\pp{}, driven almost entirely by the $T \geq 2$ minority. Figure~\ref{fig:oracle_stratified} visualizes this distribution.
118	
119	Block correlation amplifies the advantage relative to the i.i.d.\ model: at $T = 2$, the block advantage (31.69\pp{}) is 1.7$\times$ the i.i.d.\ advantage (18.49\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.
120	
121	\paragraph{P2P regression signal.}
122	The P2P regression rate in SWE-bench Verified is low: 1.04\% mean and 0\% median---77\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.
123	
124	
125	\subsection{Repo-Level Results}
126	\label{sec:repo}
127	
128	Table~\ref{tab:repo_level} compares \cls{} and \cwm{} on SWE-bench Verified per-test data (Qwen3-4B, LoRA, seed 42, max sequence length 2,048).
129	
130	\begin{table}[t]
131	\centering
132	\small
133	\caption{Repo-level per-test verification on SWE-bench Verified (Qwen3-4B, seed 42). CWM: $n{=}500$ random subset; CLS: $n{=}9{,}784$ full test set. \cwm{} falls below majority baseline, indicating negative utility. Unparseable: fraction of outputs that cannot be parsed into a verdict.}
134	\label{tab:repo_level}
135	\resizebox{\columnwidth}{!}{%
136	\setlength{\tabcolsep}{4pt}
137	\begin{tabular}{lccccc}
138	\toprule
139	\textbf{Method} & \textbf{Acc.\%} & \textbf{Fail \fone{}} & \textbf{Pass \fone{}} & \textbf{Macro \fone{}} & \textbf{Unparse.\%} \\
140	\midrule
141	\cls{} & \textbf{76.92} & \textbf{65.01} & \textbf{82.78} & \textbf{73.90} & 1.3 \\
142	\cwm{} & 66.60 & 27.70 & 78.30 & 52.99 & 75.2 \\
143	Majority & 72.96 & --- & --- & --- & --- \\
144	\bottomrule
145	\end{tabular}}
146	\end{table}
147	
148	The \cls{}--\cwm{} gap widens from 1.24\pp{} at function level to 10.32\pp{} at repo level. \cls{} achieves 76.92\% accuracy (macro \fone{} 73.90\%), while \cwm{} falls to 66.60\%---below the majority baseline (72.96\%), indicating negative utility.
149	
150	The primary driver is output format compliance collapse: 75.2\% of \cwm{} outputs are unparseable vs.\ 1.3\% for \cls{}. Crucially, the generation budget (1,024 tokens) is sufficient---mean generated output is 3,398 characters (${\sim}$850--1,100 tokens, within budget)---indicating that token-budget exhaustion is not the dominant cause. An earlier configuration with a 64-token budget produced 93\% unparseable outputs; increasing to 1,024 tokens reduced this to 75.2\%, indicating that format non-compliance, not insufficient budget, is the dominant failure mode: the model generates unstructured text rather than format-compliant execution outputs at repository-level complexity. \cls{}, producing a single binary token per test, is immune by construction.
151	
152	CWM results are from a 500-sample subset (95\% CI: [62.5\%, 70.7\%]); CLS uses the full 9,784-sample test set. A full 9,784-sample CWM evaluation is underway; preliminary 500-sample results are reported here and will be updated upon completion. Both are single-seed; multi-seed replication is also in progress.
153	
154	\subsection{Analysis}
155	\label{sec:analysis}
156	
157	\paragraph{(a) Variance compression.}
158	\cwm{}'s 5-seed standard deviation (0.36\pp{}) is notably lower than \cls{} (0.78\pp{}) and TRAJ (0.97\pp{}). This is consistent with the bottleneck hypothesis: if \cwm{} performance is capped by output-format constraints (exact string matching), seed-to-seed variability is naturally compressed relative to formulations whose performance depends more on learned representations---though reduced variance could also reflect ceiling effects inherent to exact-match evaluation.
159	
160	\paragraph{(b) Error complementarity.}
161	\cls{} and \cwm{} make errors in opposite directions. Among \cls{} errors (seed 42), 75.5\% are false negatives (FAIL $\to$ PASS), meaning the classifier tends to over-predict passing. Among \cwm{} errors, 83.1\% are false positives (PASS $\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\% accuracy, a 3.12\pp{} improvement over \cls{} alone (87.51\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains, though we leave this to future work.
162	
163	\paragraph{(c) Per-test precision and recall.}
164	At the per-test level (seed 42), \cls{} achieves fail \fone{} 87.86\% (precision 82.75\%, recall 93.64\%) and pass \fone{} 87.15\%. Of 114 problems, 48 (42.1\%) are perfectly predicted. Performance varies by mutation type: \texttt{return\_value} is easiest (97.3\%) while \texttt{off\_by\_one} is hardest (82.6\%). Multi-F2P instances with 6--10 tests reach 96.3\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.
165	
166	\paragraph{(d) Majority voting.}
167	Majority voting ($K{=}3$) decreases accuracy from 87.51\% to 86.83\% ($-$0.68\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.
168	
169	\paragraph{(e) Block correlation.}
170	Prediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\times$ more all-correct problems than expected under i.i.d.\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\S\ref{sec:oracle}) is the more relevant estimate for deployment.
171	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "e90f7a52-714c-49e8-8378-fd8db6fa3551",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate \\cls{}, \\cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Dataset.}\nWe construct a function-level benchmark from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} by generating mutated variants (five mutation types: \\texttt{wrong\\_operator}, \\texttt{off\\_by\\_one}, \\texttt{boundary\\_error}, \\texttt{return\\_value}, \\texttt{type\\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.\n\n\\paragraph{Oracle analysis and statistics.}\nWe use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin.\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \\cls{}: per-test binary classification; \\cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\\pm$ std over seeds reported where applicable.}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\\pm$ 0.36 \\\\\nTRAJ (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\nZS LLM-as-judge & 8B & 1 & 64.40 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFine-tuned \\cls{} achieves a mean accuracy of 88.43\\% ($\\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\\% ($\\pm$0.36; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \\cwm{} and 86.30\\% ($\\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \\cls{}--\\cwm{} gap is 1.24\\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.\n\nZero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\\% and Qwen3-32B (NF4) achieves 71.69\\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\\%, pass recall 35.1\\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \\cls{} by 16.74\\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} compares \\cls{} and \\cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: \\cls{} vs.\\ \\cwm{} accuracy (\\%) at 4B and 8B. Three matched seeds in full precision. The \\cls{}--\\cwm{} gap widens from 1.18\\pp{} to 2.43\\pp{}.}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{Gap} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \\multirow{2}{*}{1.18} \\\\\n\\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\\\\n\\midrule\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & 88.31 & \\textbf{89.40} & \\multirow{2}{*}{\\textbf{2.43}} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 4B, \\cls{} and \\cwm{} are separated by 1.18\\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\\pp{} ($p = 0.0066$, 95\\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.\n\nThe asymmetry in scaling efficiency is striking: from 4B to 8B, \\cls{} gains +0.99\\pp{} (88.41 $\\to$ 89.40) while \\cwm{} loses $-$0.27\\pp{} (87.23 $\\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \\cwm{} accuracy. However, the \\cwm{} regression ($-$0.27\\pp{}) falls within seed noise (3-seed std ${\\sim}$0.5\\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\\ref{fig:scaling_gap} visualizes the diverging trajectories.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{sec:equivalence}\n\nA natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \\cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.\n\nThe pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\\pm$2\\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.\n\nCritically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\\ confidence intervals would be approximately $2\\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.\n\nThe practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{sec:oracle-results}\n\nWhere does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\\ trajectory-level oracle resolve rates under both i.i.d.\\ and block-correlated error models (using the empirical ICC $= 0.191$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\\% of instances), where block-correlated advantage reaches 31.69\\pp{}, contributing 55.3\\% of the total advantage. Instances with $T \\geq 3$ exhibit block advantages exceeding 40\\pp{} but constitute only 12.2\\% of instances. The overall block-correlated advantage is 10.93\\pp{}, driven almost entirely by the $T \\geq 2$ minority. Figure~\\ref{fig:oracle_stratified} visualizes this distribution.\n\nBlock correlation amplifies the advantage relative to the i.i.d.\\ model: at $T = 2$, the block advantage (31.69\\pp{}) is 1.7$\\times$ the i.i.d.\\ advantage (18.49\\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.\n\n\\paragraph{P2P regression signal.}\nThe P2P regression rate in SWE-bench Verified is low: 1.04\\% mean and 0\\% median---77\\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.\n\n\n\\subsection{Repo-Level Results}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test data (Qwen3-4B, LoRA, seed 42, max sequence length 2,048).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level per-test verification on SWE-bench Verified (Qwen3-4B, seed 42). CWM: $n{=}500$ random subset; CLS: $n{=}9{,}784$ full test set. \\cwm{} falls below majority baseline, indicating negative utility. Unparseable: fraction of outputs that cannot be parsed into a verdict.}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Acc.\\%} & \\textbf{Fail \\fone{}} & \\textbf{Pass \\fone{}} & \\textbf{Macro \\fone{}} & \\textbf{Unparse.\\%} \\\\\n\\midrule\n\\cls{} & \\textbf{76.92} & \\textbf{65.01} & \\textbf{82.78} & \\textbf{73.90} & 1.3 \\\\\n\\cwm{} & 66.60 & 27.70 & 78.30 & 52.99 & 75.2 \\\\\nMajority & 72.96 & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe \\cls{}--\\cwm{} gap widens from 1.24\\pp{} at function level to 10.32\\pp{} at repo level. \\cls{} achieves 76.92\\% accuracy (macro \\fone{} 73.90\\%), while \\cwm{} falls to 66.60\\%---below the majority baseline (72.96\\%), indicating negative utility.\n\nThe primary driver is output format compliance collapse: 75.2\\% of \\cwm{} outputs are unparseable vs.\\ 1.3\\% for \\cls{}. Crucially, the generation budget (1,024 tokens) is sufficient---mean generated output is 3,398 characters (${\\sim}$850--1,100 tokens, within budget)---indicating that token-budget exhaustion is not the dominant cause. An earlier configuration with a 64-token budget produced 93\\% unparseable outputs; increasing to 1,024 tokens reduced this to 75.2\\%, indicating that format non-compliance, not insufficient budget, is the dominant failure mode: the model generates unstructured text rather than format-compliant execution outputs at repository-level complexity. \\cls{}, producing a single binary token per test, is immune by construction.\n\nCWM results are from a 500-sample subset (95\\% CI: [62.5\\%, 70.7\\%]); CLS uses the full 9,784-sample test set. A full 9,784-sample CWM evaluation is underway; preliminary 500-sample results are reported here and will be updated upon completion. Both are single-seed; multi-seed replication is also in progress.\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{(a) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.36\\pp{}) is notably lower than \\cls{} (0.78\\pp{}) and TRAJ (0.97\\pp{}). This is consistent with the bottleneck hypothesis: if \\cwm{} performance is capped by output-format constraints (exact string matching), seed-to-seed variability is naturally compressed relative to formulations whose performance depends more on learned representations---though reduced variance could also reflect ceiling effects inherent to exact-match evaluation.\n\n\\paragraph{(b) Error complementarity.}\n\\cls{} and \\cwm{} make errors in opposite directions. Among \\cls{} errors (seed 42), 75.5\\% are false negatives (FAIL $\\to$ PASS), meaning the classifier tends to over-predict passing. Among \\cwm{} errors, 83.1\\% are false positives (PASS $\\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\\% accuracy, a 3.12\\pp{} improvement over \\cls{} alone (87.51\\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains, though we leave this to future work.\n\n\\paragraph{(c) Per-test precision and recall.}\nAt the per-test level (seed 42), \\cls{} achieves fail \\fone{} 87.86\\% (precision 82.75\\%, recall 93.64\\%) and pass \\fone{} 87.15\\%. Of 114 problems, 48 (42.1\\%) are perfectly predicted. Performance varies by mutation type: \\texttt{return\\_value} is easiest (97.3\\%) while \\texttt{off\\_by\\_one} is hardest (82.6\\%). Multi-F2P instances with 6--10 tests reach 96.3\\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.\n\n\\paragraph{(d) Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{(e) Block correlation.}\nPrediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\\times$ more all-correct problems than expected under i.i.d.\\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\\S\\ref{sec:oracle}) is the more relevant estimate for deployment.\n",
      "numLines": 171,
      "startLine": 1,
      "totalLines": 171
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01RkWDsx4h3mBT2WH9tJrAKV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/writing_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "1ebc1ab0-5971-48d5-b850-42f82ced9eef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM6ggHqBv2EfzjLH4NiZJD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13426,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13426
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

_source line 10 · 2026-05-15T09:16:22.839Z_

<details><summary>↩ Tool result · `toolu_01RkWDsx4h3mBT2WH9tJrAKV`</summary>

```text
1	meta:
2	  venue: EMNLP 2026
3	  track: main (ARR submission)
4	  template: docs/paper/  # Existing ACL/ARR template already in place
5	  template_note: "Reusing existing acl2023.sty template from prior draft. Already configured with \\usepackage[review]{acl}."
6	  page_limit: 8  # + unlimited references/appendix (ARR format)
7	  deadline: 2026-05-25
8	  core_claim: >
9	    Binary pass/fail classification and execution output generation achieve equivalent accuracy
10	    on simple function-level code (~88% vs ~87%), but classification yields a 25.59pp same-size
11	    advantage at repo-level complexity (4B-4B, single seed) where CWM suffers format compliance
12	    collapse (53-67% unparseable, parseable-only accuracy below random at 42-43%). The advantage
13	    is complexity-dependent: from near-null at function level to critical at repository level.
14	    C1 has two layers: (1) same-size gap (4B-4B=25.59pp, 8B-8B=TBD); (2) CLS scaling gain
15	    (+0.96pp 4B→8B) vs CWM no gain (-0.23pp), indicating generation bottleneck not capacity.
16	  working_title: >
17	    Classification Scales Where Generation Stalls:
18	    Reformulating Execution Simulation for Code Repair Verification
19	  created_at: 2026-05-15T18:00:00Z
20	  notes:
21	    - "Registry is truth source for ALL numbers."
22	    - "Seeds 789/0 (CLS function-level) used 4-bit NF4 quantization — must note in paper."
23	    - "C1 two-layer structure: (1) same-size primary (4B-4B=25.59pp s42, 8B-8B=TBD); (2) scaling evidence (CLS +0.96pp, CWM -0.23pp). Cross-size 8B-CLS vs 4B-CWM (25.48-26.51pp, 2 seeds) disclosed as secondary."
24	    - "CLS 4B s123 test eval not yet run — 4B-4B currently single-seed."
25	    - "CWM 8B repo-level training in progress (repo-level-cwm-8b-conda-v4). When done, patch 8B-8B direct comparison."
26	    - "Existing .tex files form the base — Workers should rewrite from existing structure, not from scratch."
27	    - "D088 protocol: val-selected checkpoint as primary metric. Appendix: full val+test sweep curves."
28	    - "Val/test have zero problem overlap + mutation type composition shift (D087). Must disclose."
29	
30	paper_outline:
31	  - section: abstract
32	    word_budget: 200
33	    core_bullets:
34	      - "Problem: execution-free verification for code repair faces granularity-accuracy tradeoff"
35	      - "Insight: reformulating from generation to per-test binary classification; advantage is complexity-dependent"
36	      - "Function-level: CLS ≈ CWM (gap 1.24pp, 5 seeds); 8B gap widens to 2.43pp (p=0.008)"
37	      - "Per-test ≡ trajectory-level (TOST p=0.007); oracle ensemble 90.63%; advantage concentrates at T≥2 (31% instances, 55% advantage)"
38	      - "Repo-level: same-size 4B-4B CLS 83.63% vs CWM 58.04% = 25.59pp (s42); CWM below majority baseline (72.96%); 53-67% unparseable from format non-compliance; parseable-only acc 42-43% (below random). Cross-size 8B-CLS vs 4B-CWM = 25.48-26.51pp (2 seeds) disclosed separately."
39	      - "Zero-shot 32B (71.7%) far below fine-tuned 4B (88.4%)"
40	    dependencies: [experiments, method, introduction]
41	
42	  - section: introduction
43	    word_budget: 1000
44	    core_bullets:
45	      - "Hook: Test-time scaling for LLM code repair relies on verification. Full execution costs $1-3 per candidate. Execution-free alternatives must choose between accuracy and diagnostic granularity."
46	      - "Gap: CWM predicts execution outputs via generation — suffers format compliance collapse at repo-level complexity. Trajectory-level verifiers lose per-test diagnostics."
47	      - "Insight: CWM failure modes are artifacts of the generation formulation. Classification eliminates them — but the advantage only emerges beyond a complexity threshold."
48	      - "C1: Complexity-dependent advantage — near-null at function level (1.24pp), amplifies to 25.59pp same-size at repo level (4B-4B, s42). Two layers: (a) same-size gap grows with complexity; (b) CLS scaling gain (+0.96pp) vs CWM no gain (-0.23pp) = generation bottleneck evidence."
49	      - "C2: Per-test diagnostic granularity at equivalent trajectory-level accuracy (TOST p=0.007)"
50	      - "C3: Accuracy-utility frontier — advantage concentrates in multi-F2P instances"
51	    dependencies: [experiments]
52	    citation_hints:
53	      - "Code World Models (Ding et al. 2024; Meta 2025)"
54	      - "SWE-bench (Jimenez et al. 2024)"
55	      - "SWE-RM, SWE-agent, Agentless"
56	    figures: [fig1_reformulation]
57	
58	  - section: related_work
59	    word_budget: 600
60	    core_bullets:
61	      - "Execution simulation: CWM, Self-Execution, CodeMind — we reformulate as classification"
62	      - "LLM verification for code: SWE-RM, reward models, LLM-as-judge — we show per-test classification achieves equivalent accuracy with diagnostic granularity"
63	      - "APR and SWE-bench: SWE-agent, Agentless — verification as bottleneck for test-time scaling"
64	      - "Classification vs generation in NLP: extractive vs abstractive QA — our work extends this lens to code verification"
65	    dependencies: [introduction]
66	    citation_hints:
67	      - "CWM, Self-Execution, CodeMind"
68	      - "SWE-RM, SWE-RewardBench"
69	      - "SWE-bench, SWE-agent, Agentless"
70	
71	  - section: method
72	    word_budget: 1000
73	    core_bullets:
74	      - "§2.1 Problem Setup: given code patch p and test suite T, goal is per-test binary verdict"
75	      - "§2.2 Verification Formulations: CLS (1-token binary), CWM (variable-length generation + exact match), TRAJ (patch-level binary, no per-test signal)"
76	      - "§2.3 CWM Failure Modes: (a) token-budget exhaustion, (b) string-value prediction errors, (c) format compliance collapse at repo-level — all absent in CLS by construction"
77	      - "§2.4 Oracle Framework: formalize per-test advantage as f(accuracy, T, regression_rate, ICC)"
78	    dependencies: []
79	
80	  - section: experiments
81	    word_budget: 2800
82	    core_bullets:
83	      - "§3.1 Setup: Function-level: HumanEval+MBPP mutants (19,076 samples, 5 mutation types, train/val/test 15,290/1,896/1,890). Repo-level: SWE-bench Verified mutants (train ~70K, val 9,335, test 9,784). Models: Qwen3-4B/8B, LoRA rank=16. Seeds 42/123/456 bfloat16; seeds 789/0 NF4. Checkpoint selection: val-best (D088 protocol). Statistics: clustered bootstrap (114 clusters, 10K resamples), TOST (±2pp)."
84	      - "§3.2 Function-Level Results (Table 1): CLS 88.43±0.78 vs CWM 87.19±0.37 (gap 1.24pp, 5 seeds); TRAJ 86.30±0.97; ZS 8B 64.40% / 32B 71.69%. Near-equivalent at function level."
85	      - "§3.3 Scaling Behavior (Table 2): 8B CLS 89.39 vs CWM 86.96 (gap 2.43pp, 3 seeds, p=0.008). CLS gains +0.96pp scaling; CWM loses -0.23pp. Generation bottleneck, not capacity."
86	      - "§3.4 Per-Test vs Trajectory-Level Equivalence: pooled gap -0.45pp, TOST p=0.007, ±2pp. ICC=0.191, DEFF=3.97. Equivalent accuracy with free diagnostic granularity."
87	      - "§3.5 Accuracy-Utility Frontier (Table 3): T=1 (69%): no advantage; T=2 (19%): block advantage 31.7pp, 55% contribution. P2P regression ~1% = honest negative."
88	      - "§3.6 Repo-Level Results (Table 4): TWO-LAYER C1 STRUCTURE. Primary: same-size 4B-4B CLS 83.63% vs CWM 58.04% = 25.59pp (s42, val-selected). Secondary: cross-size 8B CLS vs 4B CWM = 25.48-26.51pp (2 seeds). 8B-8B placeholder pending CWM 8B. CWM below majority baseline (72.96%) by ~14pp. Unparseable 53.7-67.2%. Parseable-only acc 42-43% (below random). Scaling evidence: CLS 4B→8B at repo level (83.63→83.52% s42, noise-level); CWM 8B TBD — if CWM 8B ≈ 4B, confirms generation bottleneck. Disclose: val-selected checkpoints, val/test zero-overlap, CLS 4B-4B single seed."
89	      - "§3.7 Analysis: (a) Error complementarity (CLS: 75.5% FN, CWM: 83.1% FP, oracle 90.63%); (b) CWM error mode breakdown (77% no-keyword/token-exhaustion, 23% ambiguous, parseable-only 42.88%); (c) Variance compression (CWM std 0.37 < CLS 0.78); (d) Per-repo variation (scikit-learn ~0% unparse vs sphinx 100%); (e) Block correlation ICC=0.191"
90	    dependencies: []
91	    registry_refs:
92	      - multi-seed-core
93	      - cls-seed789
94	      - cls-seed0
95	      - cwm-baseline
96	      - cwm-seed123
97	      - cwm-seed456
98	      - cwm-seed789
99	      - cwm-seed0
100	      - model-size-scaling-cls8b
101	      - cls8b-seed123
102	      - cls8b-seed456
103	      - model-size-scaling-cwm8b
104	      - cwm8b-seed123
105	      - cwm8b-seed456
106	      - traj-level-finetuned
107	      - traj-level-seed123
108	      - traj-level-seed456
109	      - traj-level-seed789
110	      - traj-level-seed0
111	      - llm-judge-8b-zeroshot
112	      - llm-judge-32b-zeroshot
113	      - 5-paired-clustered-bootstrap
114	      - block-corr-empirical
115	      - oracle-f2p-stratified
116	      - p2p-regression-rate
117	      - per-test-precision-recall
118	      - per-test-majority-voting
119	      - repo-level-cls-v5
120	      - repo-level-cwm-v12
121	      - repo-level-cwm-seed123-conda
122	      - cls8b-s42-ckpt1000-test8192-eval
123	      - cls8b-seed123-ckpt3000-test8192-eval-v2
124	    tables: [tab1_main_results, tab2_scaling, tab3_oracle_frontier, tab4_repo_level]
125	    figures: [fig2_gap_amplification, fig3_oracle_stratified]
126	
127	  - section: conclusion
128	    word_budget: 400
129	    core_bullets:
130	      - "Summary: reformulating execution simulation from generation to classification provides a complexity-dependent advantage — near-null at function level (1.24pp), critical at repository level (25.59pp same-size 4B-4B)"
131	      - "CWM failure at repo-level is format compliance collapse, not resource insufficiency — parseable-only accuracy below random. CLS scaling gain (+0.96pp) vs CWM no gain (-0.23pp) further supports generation bottleneck hypothesis."
132	      - "Limitations: (1) single model family (Qwen3); (2) repo-level 4B-4B single seed, 8B-8B pending CWM 8B; (3) val/test distribution shift; (4) P2P regression too low for per-test signal; (5) no downstream re-repair experiment"
133	      - "Future: ensemble verification, diagnostic re-repair, CWM 8B repo-level, multi-model validation"
134	    dependencies: [experiments, method]
135	
136	visualization_plan:
137	  - fig_id: fig1_reformulation
138	    type: conceptual
139	    tool: matplotlib
140	    description: >
141	      Task reformulation overview: three pipelines — CLS (1 token), CWM (N tokens + exact match),
142	      TRAJ (1 token, no per-test). Highlight CWM failure modes. Clean academic style.
143	    placement: introduction
144	    aspect_ratio: "16:9"
145	    data_source: "manual"
146	
147	  - fig_id: fig2_gap_amplification
148	    type: statistical
149	    tool: matplotlib
150	    description: >
151	      Gap amplification visualization. X-axis: complexity levels (Function 4B, Function 8B, Repo-level 4B-4B).
152	      Y-axis: CLS-CWM accuracy gap (pp). Values: 1.24, 2.43, 25.59.
153	      Error bars where multi-seed available. Log-scale Y or broken axis to show both small and large gaps.
154	      Key message: gap explodes with complexity. Use same-size comparison for repo-level bar.
155	    data_source: "registry: multi-seed-core, model-size-scaling-cls8b, cls4b-v5-ckpt4600-test-eval, repo-level-cwm-v12"
156	    placement: experiments
157	    aspect_ratio: "4:3"
158	
159	  - fig_id: fig3_oracle_stratified
160	    type: statistical
161	    tool: matplotlib
162	    description: >
163	      Oracle per-test advantage stratified by F2P test count (T=1, T=2, T=3-5, T≥6).
164	      Primary bars: block advantage (pp). Secondary: instance percentage.
165	      T=2 contributes 55.3% of total. Include i.i.d. comparison.
166	    data_source: "registry: oracle-f2p-stratified"
167	    placement: experiments
168	    aspect_ratio: "4:3"
169	
170	table_plan:
171	  - table_id: tab1_main_results
172	    caption: "Function-level per-test verification on HumanEval+MBPP (1,890 test samples). Mean ± std over seeds."
173	    placement: experiments
174	    type: comparison
175	    columns: [Method, Model, Seeds, Accuracy]
176	    data_source: "registry: multi-seed-core, cls-seed789, cls-seed0, cwm-*, traj-level-*, llm-judge-*"
177	    notes: "Compact 4-column format for 8-page budget. F1 details in appendix."
178	
179	  - table_id: tab2_scaling
180	    caption: "Model-size scaling: CLS vs CWM accuracy (%) at 4B and 8B. Three matched bfloat16 seeds."
181	    placement: experiments
182	    type: comparison
183	    columns: [Method, Size, s42, s123, s456, Mean, Gap]
184	    data_source: "registry: multi-seed-core, cwm-*, model-size-scaling-*, cls8b-*, cwm8b-*"
185	
186	  - table_id: tab3_oracle_frontier
187	    caption: "Oracle per-test advantage by F2P test count on SWE-bench Verified (500 instances). Block model uses ICC=0.191."
188	    placement: experiments
189	    type: statistics
190	    columns: [T, Inst_Pct, IID_pp, Block_pp, Contrib_Pct]
191	    data_source: "registry: oracle-f2p-stratified"
192	
193	  - table_id: tab4_repo_level
194	    caption: "Repo-level per-test verification on SWE-bench Verified (val-selected checkpoints). Same-size comparisons primary; cross-size disclosed."
195	    placement: experiments
196	    type: comparison
197	    columns: [Method, Size, Seed, Accuracy, F1_Macro, Unparseable_Pct, vs_Majority]
198	    rows_structure: >
199	      Row 1: CLS 4B s42 — 83.63%, 75.63, 0%, +10.67pp (cls4b-v5-ckpt4600-test-eval)
200	      Row 2: CWM 4B s42 — 58.04%, 51.67, 53.7%, -14.92pp (repo-level-cwm-v12)
201	      Row 3: CWM 4B s123 — 59.09%, 43.43, 67.2%, -13.87pp (repo-level-cwm-seed123-conda)
202	      Row 4: CLS 8B s42 — 83.52%, 77.50, 0%, +10.56pp (cls8b-s42-ckpt1000-test8192-eval)
203	      Row 5: CLS 8B s123 — 85.60%, 78.38, 0%, +12.64pp (cls8b-seed123-ckpt3000-test8192-eval)
204	      Row 6: CWM 8B s42 — TBD (repo-level-cwm-8b-conda-v4, in progress)
205	      Same-size gap: 4B-4B = 25.59pp (s42); 8B-8B = TBD
206	    data_source: "registry: cls4b-v5-ckpt4600-test-eval, cls8b-s42-ckpt1000-test8192-eval, cls8b-seed123-ckpt3000-test8192-eval-v2, repo-level-cwm-v12, repo-level-cwm-seed123-conda"
207	    notes: >
208	      Val-selected checkpoints (D088). Test set n=9,784. Majority baseline 72.96%.
209	      Primary comparison: same-size 4B-4B (25.59pp, single seed). 8B-8B pending CWM 8B.
210	      Cross-size 8B CLS vs 4B CWM (25.48-26.51pp, 2 seeds) disclosed as secondary.
211	      Parseable-only CWM accuracy (42-43%) reported in text. Val/test zero-overlap disclosed.
212	      CLS 4B s123 test eval not yet available — note single-seed limitation for 4B-4B.
213	
214	literature_strategy:
215	  citation_budget: 30
216	  macro_context:
217	    - "execution simulation for code / code world models"
218	    - "LLM-based code verification and repair scaling"
219	    - "task reformulation (classification vs generation) in NLP"
220	  micro_clusters:
221	    - cluster_name: "Execution Simulation"
222	      search_queries:
223	        - "code world models execution simulation LLM 2024 2025"
224	        - "self-execution simulation code prediction"
225	      must_cite:
226	        - "Code World Models (Ding et al. 2024)"
227	        - "Meta CWM (2025)"
228	      target_count: 4
229	
230	    - cluster_name: "LLM Verification for Code"
231	      search_queries:
232	        - "SWE-RM reward model code repair verification"
233	        - "LLM-as-judge code correctness"
234	        - "SWE-RewardBench"
235	      must_cite:
236	        - "SWE-RM (Zhang et al. 2025)"
237	      target_count: 4
238	
239	    - cluster_name: "APR and SWE-bench"
240	      search_queries:
241	        - "SWE-bench automated program repair LLM 2024 2025"
242	        - "SWE-agent Agentless repair"
243	        - "test-time compute scaling code repair"
244	      must_cite:
245	        - "SWE-bench (Jimenez et al. 2024)"
246	        - "SWE-agent (Yang et al. 2024)"
247	        - "Agentless (Xia et al. 2024)"
248	      target_count: 6
249	
250	    - cluster_name: "Task Reformulation NLP"
251	      search_queries:
252	        - "classification vs generation NLP reformulation"
253	        - "extractive vs abstractive comparison"
254	      must_cite: []
255	      target_count: 3
256	
257	    - cluster_name: "Code LLMs and Benchmarks"
258	      search_queries:
259	        - "Qwen2.5 Qwen3 code model 2025"
260	        - "HumanEval MBPP benchmark"
261	      must_cite:
262	        - "Qwen2.5 (Yang et al. 2024)"
263	        - "HumanEval (Chen et al. 2021)"
264	        - "MBPP (Austin et al. 2021)"
265	      target_count: 5
266	
267	    - cluster_name: "Statistical Methods"
268	      search_queries:
269	        - "TOST equivalence test"
270	        - "clustered bootstrap"
271	      must_cite:
272	        - "TOST (Schuirmann 1987)"
273	        - "Bootstrap (Davison & Hinkley 1997)"
274	      target_count: 3
275	
276	    - cluster_name: "LoRA and Efficient Fine-tuning"
277	      search_queries:
278	        - "LoRA low-rank adaptation fine-tuning"
279	        - "QLoRA quantized fine-tuning"
280	      must_cite:
281	        - "LoRA (Hu et al. 2022)"
282	        - "QLoRA (Dettmers et al. 2024)"
283	      target_count: 2
284	
285	writing_order:
286	  - experiments
287	  - method
288	  - introduction
289	  - related_work
290	  - abstract
291	  - conclusion
292	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "2aa9270c-3e04-451f-a8a6-5bff2412af38",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/writing_plan.yaml",
      "content": "meta:\n  venue: EMNLP 2026\n  track: main (ARR submission)\n  template: docs/paper/  # Existing ACL/ARR template already in place\n  template_note: \"Reusing existing acl2023.sty template from prior draft. Already configured with \\\\usepackage[review]{acl}.\"\n  page_limit: 8  # + unlimited references/appendix (ARR format)\n  deadline: 2026-05-25\n  core_claim: >\n    Binary pass/fail classification and execution output generation achieve equivalent accuracy\n    on simple function-level code (~88% vs ~87%), but classification yields a 25.59pp same-size\n    advantage at repo-level complexity (4B-4B, single seed) where CWM suffers format compliance\n    collapse (53-67% unparseable, parseable-only accuracy below random at 42-43%). The advantage\n    is complexity-dependent: from near-null at function level to critical at repository level.\n    C1 has two layers: (1) same-size gap (4B-4B=25.59pp, 8B-8B=TBD); (2) CLS scaling gain\n    (+0.96pp 4B→8B) vs CWM no gain (-0.23pp), indicating generation bottleneck not capacity.\n  working_title: >\n    Classification Scales Where Generation Stalls:\n    Reformulating Execution Simulation for Code Repair Verification\n  created_at: 2026-05-15T18:00:00Z\n  notes:\n    - \"Registry is truth source for ALL numbers.\"\n    - \"Seeds 789/0 (CLS function-level) used 4-bit NF4 quantization — must note in paper.\"\n    - \"C1 two-layer structure: (1) same-size primary (4B-4B=25.59pp s42, 8B-8B=TBD); (2) scaling evidence (CLS +0.96pp, CWM -0.23pp). Cross-size 8B-CLS vs 4B-CWM (25.48-26.51pp, 2 seeds) disclosed as secondary.\"\n    - \"CLS 4B s123 test eval not yet run — 4B-4B currently single-seed.\"\n    - \"CWM 8B repo-level training in progress (repo-level-cwm-8b-conda-v4). When done, patch 8B-8B direct comparison.\"\n    - \"Existing .tex files form the base — Workers should rewrite from existing structure, not from scratch.\"\n    - \"D088 protocol: val-selected checkpoint as primary metric. Appendix: full val+test sweep curves.\"\n    - \"Val/test have zero problem overlap + mutation type composition shift (D087). Must disclose.\"\n\npaper_outline:\n  - section: abstract\n    word_budget: 200\n    core_bullets:\n      - \"Problem: execution-free verification for code repair faces granularity-accuracy tradeoff\"\n      - \"Insight: reformulating from generation to per-test binary classification; advantage is complexity-dependent\"\n      - \"Function-level: CLS ≈ CWM (gap 1.24pp, 5 seeds); 8B gap widens to 2.43pp (p=0.008)\"\n      - \"Per-test ≡ trajectory-level (TOST p=0.007); oracle ensemble 90.63%; advantage concentrates at T≥2 (31% instances, 55% advantage)\"\n      - \"Repo-level: same-size 4B-4B CLS 83.63% vs CWM 58.04% = 25.59pp (s42); CWM below majority baseline (72.96%); 53-67% unparseable from format non-compliance; parseable-only acc 42-43% (below random). Cross-size 8B-CLS vs 4B-CWM = 25.48-26.51pp (2 seeds) disclosed separately.\"\n      - \"Zero-shot 32B (71.7%) far below fine-tuned 4B (88.4%)\"\n    dependencies: [experiments, method, introduction]\n\n  - section: introduction\n    word_budget: 1000\n    core_bullets:\n      - \"Hook: Test-time scaling for LLM code repair relies on verification. Full execution costs $1-3 per candidate. Execution-free alternatives must choose between accuracy and diagnostic granularity.\"\n      - \"Gap: CWM predicts execution outputs via generation — suffers format compliance collapse at repo-level complexity. Trajectory-level verifiers lose per-test diagnostics.\"\n      - \"Insight: CWM failure modes are artifacts of the generation formulation. Classification eliminates them — but the advantage only emerges beyond a complexity threshold.\"\n      - \"C1: Complexity-dependent advantage — near-null at function level (1.24pp), amplifies to 25.59pp same-size at repo level (4B-4B, s42). Two layers: (a) same-size gap grows with complexity; (b) CLS scaling gain (+0.96pp) vs CWM no gain (-0.23pp) = generation bottleneck evidence.\"\n      - \"C2: Per-test diagnostic granularity at equivalent trajectory-level accuracy (TOST p=0.007)\"\n      - \"C3: Accuracy-utility frontier — advantage concentrates in multi-F2P instances\"\n    dependencies: [experiments]\n    citation_hints:\n      - \"Code World Models (Ding et al. 2024; Meta 2025)\"\n      - \"SWE-bench (Jimenez et al. 2024)\"\n      - \"SWE-RM, SWE-agent, Agentless\"\n    figures: [fig1_reformulation]\n\n  - section: related_work\n    word_budget: 600\n    core_bullets:\n      - \"Execution simulation: CWM, Self-Execution, CodeMind — we reformulate as classification\"\n      - \"LLM verification for code: SWE-RM, reward models, LLM-as-judge — we show per-test classification achieves equivalent accuracy with diagnostic granularity\"\n      - \"APR and SWE-bench: SWE-agent, Agentless — verification as bottleneck for test-time scaling\"\n      - \"Classification vs generation in NLP: extractive vs abstractive QA — our work extends this lens to code verification\"\n    dependencies: [introduction]\n    citation_hints:\n      - \"CWM, Self-Execution, CodeMind\"\n      - \"SWE-RM, SWE-RewardBench\"\n      - \"SWE-bench, SWE-agent, Agentless\"\n\n  - section: method\n    word_budget: 1000\n    core_bullets:\n      - \"§2.1 Problem Setup: given code patch p and test suite T, goal is per-test binary verdict\"\n      - \"§2.2 Verification Formulations: CLS (1-token binary), CWM (variable-length generation + exact match), TRAJ (patch-level binary, no per-test signal)\"\n      - \"§2.3 CWM Failure Modes: (a) token-budget exhaustion, (b) string-value prediction errors, (c) format compliance collapse at repo-level — all absent in CLS by construction\"\n      - \"§2.4 Oracle Framework: formalize per-test advantage as f(accuracy, T, regression_rate, ICC)\"\n    dependencies: []\n\n  - section: experiments\n    word_budget: 2800\n    core_bullets:\n      - \"§3.1 Setup: Function-level: HumanEval+MBPP mutants (19,076 samples, 5 mutation types, train/val/test 15,290/1,896/1,890). Repo-level: SWE-bench Verified mutants (train ~70K, val 9,335, test 9,784). Models: Qwen3-4B/8B, LoRA rank=16. Seeds 42/123/456 bfloat16; seeds 789/0 NF4. Checkpoint selection: val-best (D088 protocol). Statistics: clustered bootstrap (114 clusters, 10K resamples), TOST (±2pp).\"\n      - \"§3.2 Function-Level Results (Table 1): CLS 88.43±0.78 vs CWM 87.19±0.37 (gap 1.24pp, 5 seeds); TRAJ 86.30±0.97; ZS 8B 64.40% / 32B 71.69%. Near-equivalent at function level.\"\n      - \"§3.3 Scaling Behavior (Table 2): 8B CLS 89.39 vs CWM 86.96 (gap 2.43pp, 3 seeds, p=0.008). CLS gains +0.96pp scaling; CWM loses -0.23pp. Generation bottleneck, not capacity.\"\n      - \"§3.4 Per-Test vs Trajectory-Level Equivalence: pooled gap -0.45pp, TOST p=0.007, ±2pp. ICC=0.191, DEFF=3.97. Equivalent accuracy with free diagnostic granularity.\"\n      - \"§3.5 Accuracy-Utility Frontier (Table 3): T=1 (69%): no advantage; T=2 (19%): block advantage 31.7pp, 55% contribution. P2P regression ~1% = honest negative.\"\n      - \"§3.6 Repo-Level Results (Table 4): TWO-LAYER C1 STRUCTURE. Primary: same-size 4B-4B CLS 83.63% vs CWM 58.04% = 25.59pp (s42, val-selected). Secondary: cross-size 8B CLS vs 4B CWM = 25.48-26.51pp (2 seeds). 8B-8B placeholder pending CWM 8B. CWM below majority baseline (72.96%) by ~14pp. Unparseable 53.7-67.2%. Parseable-only acc 42-43% (below random). Scaling evidence: CLS 4B→8B at repo level (83.63→83.52% s42, noise-level); CWM 8B TBD — if CWM 8B ≈ 4B, confirms generation bottleneck. Disclose: val-selected checkpoints, val/test zero-overlap, CLS 4B-4B single seed.\"\n      - \"§3.7 Analysis: (a) Error complementarity (CLS: 75.5% FN, CWM: 83.1% FP, oracle 90.63%); (b) CWM error mode breakdown (77% no-keyword/token-exhaustion, 23% ambiguous, parseable-only 42.88%); (c) Variance compression (CWM std 0.37 < CLS 0.78); (d) Per-repo variation (scikit-learn ~0% unparse vs sphinx 100%); (e) Block correlation ICC=0.191\"\n    dependencies: []\n    registry_refs:\n      - multi-seed-core\n      - cls-seed789\n      - cls-seed0\n      - cwm-baseline\n      - cwm-seed123\n      - cwm-seed456\n      - cwm-seed789\n      - cwm-seed0\n      - model-size-scaling-cls8b\n      - cls8b-seed123\n      - cls8b-seed456\n      - model-size-scaling-cwm8b\n      - cwm8b-seed123\n      - cwm8b-seed456\n      - traj-level-finetuned\n      - traj-level-seed123\n      - traj-level-seed456\n      - traj-level-seed789\n      - traj-level-seed0\n      - llm-judge-8b-zeroshot\n      - llm-judge-32b-zeroshot\n      - 5-paired-clustered-bootstrap\n      - block-corr-empirical\n      - oracle-f2p-stratified\n      - p2p-regression-rate\n      - per-test-precision-recall\n      - per-test-majority-voting\n      - repo-level-cls-v5\n      - repo-level-cwm-v12\n      - repo-level-cwm-seed123-conda\n      - cls8b-s42-ckpt1000-test8192-eval\n      - cls8b-seed123-ckpt3000-test8192-eval-v2\n    tables: [tab1_main_results, tab2_scaling, tab3_oracle_frontier, tab4_repo_level]\n    figures: [fig2_gap_amplification, fig3_oracle_stratified]\n\n  - section: conclusion\n    word_budget: 400\n    core_bullets:\n      - \"Summary: reformulating execution simulation from generation to classification provides a complexity-dependent advantage — near-null at function level (1.24pp), critical at repository level (25.59pp same-size 4B-4B)\"\n      - \"CWM failure at repo-level is format compliance collapse, not resource insufficiency — parseable-only accuracy below random. CLS scaling gain (+0.96pp) vs CWM no gain (-0.23pp) further supports generation bottleneck hypothesis.\"\n      - \"Limitations: (1) single model family (Qwen3); (2) repo-level 4B-4B single seed, 8B-8B pending CWM 8B; (3) val/test distribution shift; (4) P2P regression too low for per-test signal; (5) no downstream re-repair experiment\"\n      - \"Future: ensemble verification, diagnostic re-repair, CWM 8B repo-level, multi-model validation\"\n    dependencies: [experiments, method]\n\nvisualization_plan:\n  - fig_id: fig1_reformulation\n    type: conceptual\n    tool: matplotlib\n    description: >\n      Task reformulation overview: three pipelines — CLS (1 token), CWM (N tokens + exact match),\n      TRAJ (1 token, no per-test). Highlight CWM failure modes. Clean academic style.\n    placement: introduction\n    aspect_ratio: \"16:9\"\n    data_source: \"manual\"\n\n  - fig_id: fig2_gap_amplification\n    type: statistical\n    tool: matplotlib\n    description: >\n      Gap amplification visualization. X-axis: complexity levels (Function 4B, Function 8B, Repo-level 4B-4B).\n      Y-axis: CLS-CWM accuracy gap (pp). Values: 1.24, 2.43, 25.59.\n      Error bars where multi-seed available. Log-scale Y or broken axis to show both small and large gaps.\n      Key message: gap explodes with complexity. Use same-size comparison for repo-level bar.\n    data_source: \"registry: multi-seed-core, model-size-scaling-cls8b, cls4b-v5-ckpt4600-test-eval, repo-level-cwm-v12\"\n    placement: experiments\n    aspect_ratio: \"4:3\"\n\n  - fig_id: fig3_oracle_stratified\n    type: statistical\n    tool: matplotlib\n    description: >\n      Oracle per-test advantage stratified by F2P test count (T=1, T=2, T=3-5, T≥6).\n      Primary bars: block advantage (pp). Secondary: instance percentage.\n      T=2 contributes 55.3% of total. Include i.i.d. comparison.\n    data_source: \"registry: oracle-f2p-stratified\"\n    placement: experiments\n    aspect_ratio: \"4:3\"\n\ntable_plan:\n  - table_id: tab1_main_results\n    caption: \"Function-level per-test verification on HumanEval+MBPP (1,890 test samples). Mean ± std over seeds.\"\n    placement: experiments\n    type: comparison\n    columns: [Method, Model, Seeds, Accuracy]\n    data_source: \"registry: multi-seed-core, cls-seed789, cls-seed0, cwm-*, traj-level-*, llm-judge-*\"\n    notes: \"Compact 4-column format for 8-page budget. F1 details in appendix.\"\n\n  - table_id: tab2_scaling\n    caption: \"Model-size scaling: CLS vs CWM accuracy (%) at 4B and 8B. Three matched bfloat16 seeds.\"\n    placement: experiments\n    type: comparison\n    columns: [Method, Size, s42, s123, s456, Mean, Gap]\n    data_source: \"registry: multi-seed-core, cwm-*, model-size-scaling-*, cls8b-*, cwm8b-*\"\n\n  - table_id: tab3_oracle_frontier\n    caption: \"Oracle per-test advantage by F2P test count on SWE-bench Verified (500 instances). Block model uses ICC=0.191.\"\n    placement: experiments\n    type: statistics\n    columns: [T, Inst_Pct, IID_pp, Block_pp, Contrib_Pct]\n    data_source: \"registry: oracle-f2p-stratified\"\n\n  - table_id: tab4_repo_level\n    caption: \"Repo-level per-test verification on SWE-bench Verified (val-selected checkpoints). Same-size comparisons primary; cross-size disclosed.\"\n    placement: experiments\n    type: comparison\n    columns: [Method, Size, Seed, Accuracy, F1_Macro, Unparseable_Pct, vs_Majority]\n    rows_structure: >\n      Row 1: CLS 4B s42 — 83.63%, 75.63, 0%, +10.67pp (cls4b-v5-ckpt4600-test-eval)\n      Row 2: CWM 4B s42 — 58.04%, 51.67, 53.7%, -14.92pp (repo-level-cwm-v12)\n      Row 3: CWM 4B s123 — 59.09%, 43.43, 67.2%, -13.87pp (repo-level-cwm-seed123-conda)\n      Row 4: CLS 8B s42 — 83.52%, 77.50, 0%, +10.56pp (cls8b-s42-ckpt1000-test8192-eval)\n      Row 5: CLS 8B s123 — 85.60%, 78.38, 0%, +12.64pp (cls8b-seed123-ckpt3000-test8192-eval)\n      Row 6: CWM 8B s42 — TBD (repo-level-cwm-8b-conda-v4, in progress)\n      Same-size gap: 4B-4B = 25.59pp (s42); 8B-8B = TBD\n    data_source: \"registry: cls4b-v5-ckpt4600-test-eval, cls8b-s42-ckpt1000-test8192-eval, cls8b-seed123-ckpt3000-test8192-eval-v2, repo-level-cwm-v12, repo-level-cwm-seed123-conda\"\n    notes: >\n      Val-selected checkpoints (D088). Test set n=9,784. Majority baseline 72.96%.\n      Primary comparison: same-size 4B-4B (25.59pp, single seed). 8B-8B pending CWM 8B.\n      Cross-size 8B CLS vs 4B CWM (25.48-26.51pp, 2 seeds) disclosed as secondary.\n      Parseable-only CWM accuracy (42-43%) reported in text. Val/test zero-overlap disclosed.\n      CLS 4B s123 test eval not yet available — note single-seed limitation for 4B-4B.\n\nliterature_strategy:\n  citation_budget: 30\n  macro_context:\n    - \"execution simulation for code / code world models\"\n    - \"LLM-based code verification and repair scaling\"\n    - \"task reformulation (classification vs generation) in NLP\"\n  micro_clusters:\n    - cluster_name: \"Execution Simulation\"\n      search_queries:\n        - \"code world models execution simulation LLM 2024 2025\"\n        - \"self-execution simulation code prediction\"\n      must_cite:\n        - \"Code World Models (Ding et al. 2024)\"\n        - \"Meta CWM (2025)\"\n      target_count: 4\n\n    - cluster_name: \"LLM Verification for Code\"\n      search_queries:\n        - \"SWE-RM reward model code repair verification\"\n        - \"LLM-as-judge code correctness\"\n        - \"SWE-RewardBench\"\n      must_cite:\n        - \"SWE-RM (Zhang et al. 2025)\"\n      target_count: 4\n\n    - cluster_name: \"APR and SWE-bench\"\n      search_queries:\n        - \"SWE-bench automated program repair LLM 2024 2025\"\n        - \"SWE-agent Agentless repair\"\n        - \"test-time compute scaling code repair\"\n      must_cite:\n        - \"SWE-bench (Jimenez et al. 2024)\"\n        - \"SWE-agent (Yang et al. 2024)\"\n        - \"Agentless (Xia et al. 2024)\"\n      target_count: 6\n\n    - cluster_name: \"Task Reformulation NLP\"\n      search_queries:\n        - \"classification vs generation NLP reformulation\"\n        - \"extractive vs abstractive comparison\"\n      must_cite: []\n      target_count: 3\n\n    - cluster_name: \"Code LLMs and Benchmarks\"\n      search_queries:\n        - \"Qwen2.5 Qwen3 code model 2025\"\n        - \"HumanEval MBPP benchmark\"\n      must_cite:\n        - \"Qwen2.5 (Yang et al. 2024)\"\n        - \"HumanEval (Chen et al. 2021)\"\n        - \"MBPP (Austin et al. 2021)\"\n      target_count: 5\n\n    - cluster_name: \"Statistical Methods\"\n      search_queries:\n        - \"TOST equivalence test\"\n        - \"clustered bootstrap\"\n      must_cite:\n        - \"TOST (Schuirmann 1987)\"\n        - \"Bootstrap (Davison & Hinkley 1997)\"\n      target_count: 3\n\n    - cluster_name: \"LoRA and Efficient Fine-tuning\"\n      search_queries:\n        - \"LoRA low-rank adaptation fine-tuning\"\n        - \"QLoRA quantized fine-tuning\"\n      must_cite:\n        - \"LoRA (Hu et al. 2022)\"\n        - \"QLoRA (Dettmers et al. 2024)\"\n      target_count: 2\n\nwriting_order:\n  - experiments\n  - method\n  - introduction\n  - related_work\n  - abstract\n  - conclusion\n",
      "numLines": 292,
      "startLine": 1,
      "totalLines": 292
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have all three files. Let me carefully construct the rewritten experiments.tex based on the task requirements. Let me go through each section:

§3.1 Setup - Micro adjustments: add repo-level dataset, ICC citation, D088 protocol
§3.2 Function-Level Results (Table 1) - Keep as-is
§3.3 Scaling (Table 2) - Keep, add forward reference to §3.6


§3.4 Per-Test vs Trajectory-Level - Keep as-is
§3.5 Oracle Frontier (Table 3) - Keep as-is
§3.6 Repo-Level Results - Complete rewrite with two-layer C1, new Table 4
§3.7 Analysis - Rewrite with v12 data

Now I'm writing out the complete file, being careful to incorporate all the specific numbers and metrics from the task, particularly the new Table 4 data for repo-level results.

Generating markdown table... Now I'm looking at the error analysis across the two approaches—CLS has mostly false negatives while CWM tends toward false positives, and combining them gets us to about 90.63% accuracy. CWM's main failure modes are unparseable outputs and missing execution keywords, with huge variation across repositories. I'm also noting that CWM shows much tighter variance across seeds compared to the other methods, and I need to examine the per-test precision and recall breakdown.

Looking at the fail case metrics and majority voting results, I see the F1 score is strong but majority voting actually hurts performance slightly. The block correlation is quite low, suggesting the methods aren't capturing the same underlying signal. Now I'm setting up the LaTeX table for the experiments section with columns for method, model size, seed, accuracy, macro F1, unparseable rate, and comparison to majority voting—I need to verify the cross-size comparisons are correct.

Let me double-check the scaling behavior: the 8B CLS model shows essentially no degradation when comparing different seeds, which is good noise-level consistency. I also need to make sure I'm adding the ICC citation properly in section 3.1 alongside the existing bootstrap and TOST references, and include the SWE-bench Verified dataset details with the majority baseline. The D088 validation-selected checkpoint protocol needs to be documented as well.

Now I'm structuring the full paper carefully—opening section 3, then expanding the setup with repo-level dataset information, keeping the function-level and scaling results tables, maintaining the oracle frontier analysis, completely rewriting the repo-level results section, and revising the analysis. I need to stay within the word budget while ensuring all tables compile correctly.

For the ICC citation, I'll add it in the statistics paragraph of section 3.1 where it's most relevant. I'm also noting that the Majority baseline row in table 4 should use LaTeX dashes, and I'll use the existing macros like `\pp{}`, `\cls{}`, `\cwm{}`, and `\fone{}` as they're defined in the preamble. The existing file is around 1700 words, so I need to expand to roughly 2800, with the main growth coming from sections 3.6 and 3.7.

I'm planning the structure: section 3.1 will cover setup with both function and repo-level dataset descriptions plus the D088 protocol, section 3.2 keeps the function-level results mostly intact, section 3.3 handles scaling with a forward reference, section 3.4 stays as-is for per-test versus trajectory analysis, section 3.5 maintains the oracle frontier discussion, then sections 3.6 and 3.7 get substantial rewrites to reach the target word count. Now I'm drafting the complete file with careful attention to the numbers and precise formatting.

Generating markdown table... I'm finishing up the table formatting with em dashes for the missing CWM 8B row and the majority baseline row. Now I need to move into writing the repo-level section, which should cover the key findings: the performance gap between 4B models, how CWM underperforms compared to majority voting, the unparseable rates, the accuracy when only looking at parseable outputs, and format compliance issues. Looking at the analysis section requirements, I need to document how CLS and CWM errors complement each other—CLS catches function-level issues with high false negatives while CWM's false positives dominate, and together they achieve over 90% accuracy. Then I'm examining CWM's error patterns across the repository data, where unparseable cases vary dramatically by project and the parseable-only accuracy falls below random chance, suggesting the model struggles with execution keyword detection.

I'm also tracking how variance differs across methods—CWM's predictions are much tighter than trajectory-based approaches—and noting the per-test performance metrics showing strong F1 on failure cases and near-perfect accuracy on return value checks. The majority voting ensemble actually hurts performance slightly, and the block correlation analysis reveals moderate intra-cluster dependence that affects effective sample size.

Now I'm restructuring the analysis to lead with error complementarity, then move through CWM's failure modes, variance patterns, granular test-level results, ensemble effects, and finally the correlation structure. I also need to add the ICC citation in the statistics paragraph of section 3.1 since it's currently missing.

Let me verify the comparative math against majority voting one more time to make sure all the deltas are correct, then estimate the word count for the full rewrite—I'm looking at roughly 300 words for the expanded introduction section, and I'll need to check how the remaining sections scale. Looking at the existing tables in the document, they bold the best value in each column, so I should follow that convention. The best accuracy is 85.60 from CLS 8B s123, but since the task emphasizes same-size 4B-to-4B comparison as primary, I'll bold 83.63 as the best performance in the 4B category to keep the focus aligned with the main evaluation framework. I'm finalizing the table structure with proper grouping for the model sizes and baselines using midrules, and I need to make sure there are no LaTeX comments in the output since the task explicitly forbids them. Now I'll write out the complete LaTeX file, starting with the experiments section where I'll add the ICC citation to the statistics paragraph and include a forward reference to the repo-level complexity analysis. For the repo-level dataset, I'm extracting test instances from repository patches, resulting in roughly 70K training samples with separate validation and test sets that don't overlap on problems. The majority baseline sits at 72.96%, and the mutation composition varies between splits due to the non-overlapping problem structure. For the models, I'm fine-tuning Qwen3-4B and Qwen3-8B using LoRA with specific hyperparameters across five random seeds, experimenting with different quantization approaches for different seed runs.

For evaluation, I'm using SWE-bench Verified to analyze the accuracy-utility frontier, applying clustered bootstrap for confidence intervals across the problem clusters, and using equivalence testing to compare per-test versus trajectory-level results. I'm working through the structure of the paper now. The current rewritten thinking shows the section headers and placeholders for the function-level, scaling behavior, equivalence, and oracle results sections. For the scaling behavior section, I need to add a forward reference that connects the diverging trajectories observed there to the repository-level analysis that comes later. Then I'll move into completing the repo-level results section and the analysis that follows, being careful to preserve all the numerical details and findings from the original. (a) Error complementarity:
Among classifier errors, about three-quarters are false negatives where it predicts passing when tests actually fail, suggesting it's too optimistic. The string-matching model does the opposite—most of its errors are false positives that incorrectly flag passing tests as failures. When I combine them optimally, taking whichever model is correct, accuracy jumps to 90.63%, showing these errors are genuinely complementary and ensemble methods could exploit this.

(b) CWM error mode breakdown:
At the repository level, the string-matching model's output format completely breaks down—over half the test instances produce unparseable results that can't be evaluated. Among those unparseable outputs, most contain no execution keywords at all, while others have conflicting keywords for both pass and fail states. Even when outputs are parseable, the model only achieves 42.88% accuracy, which is worse than random guessing, meaning its predictions are actively misleading. The problem varies wildly across repositories, with some like scikit-learn having almost no format issues while others like sphinx are severely affected.

(c) Variance compression:
The string-matching model shows much lower variability across different random seeds compared to the other approaches, which aligns with the idea that its performance is bottlenecked by format constraints rather than learned representations.

(d) Per-test precision and recall:
The classifier achieves strong performance on individual tests, with high precision and recall for both failure and pass predictions.  Performance varies significantly by mutation type—some are nearly trivial to detect while others like off-by-one errors are much harder. When there are multiple failing-to-passing tests in a problem, accuracy jumps substantially, confirming that having more test-level information is crucial.

(e) Majority voting:
Combining three models through majority voting actually hurts performance slightly, suggesting the errors are systematic patterns rather than random noise that ensemble methods could smooth out.

(f) Block correlation:
Errors on tests within the same problem tend to be correlated, indicating that certain problem characteristics drive multiple prediction failures. The same-size 4B model comparison shows a stark 25.59 percentage point gap, with my approach reaching 83.63% accuracy versus the baseline at 58.04%. Notably, the baseline actually underperforms a naive majority classifier, suggesting it provides negative utility. Testing with a different seed confirms this isn't a one-off result—the failure pattern holds across multiple runs.

The core issue is format compliance: the baseline produces unparseable outputs for over half its predictions, while my approach generates zero malformed outputs by design. Even when the baseline does produce valid predictions, they're worse than random guessing, indicating the model struggles fundamentally with repository-level complexity. I'm also including results from the 8B variant to show how this scales.

Looking at the 8B results, there's a substantial performance gap—my 8B model achieves 83-85% accuracy compared to the baseline's much lower performance. Interestingly, scaling from 4B to 8B within my approach shows almost no improvement at the repository level, suggesting I might be hitting a capacity ceiling at this complexity, or the difference could just be checkpoint variance. The baseline's 8B training is still running, but if it performs similarly to the 4B version, that would point to a fundamental generation bottleneck rather than a model capacity issue.

I should note that the 4B comparison relies on a single seed, and there's some variance in the results I'm tracking. I'm verifying that all required elements are covered in the analysis—the performance gaps, unparseable rates, accuracy metrics, format compliance issues, cross-size comparisons, and the key disclosures about single seed runs, zero problem overlap between validation and test sets, and checkpoint selection variance. as percentage points, and `\fone{}` renders as the F₁ metric notation. Now I'm ready to construct the complete file, making sure the table fits within a single column using `\resizebox`. For rows with missing data like CWM 8B, I'll use em dashes, and I need to handle the Majority baseline row carefully to match the expected format.

Let me clarify the data sources first—the error complementarity section references function-level results from seed 42, while the CWM error breakdown also comes from function-level analysis despite the v12 version label. I'm verifying the breakdown for unparseable cases: 76.9% lack execution keywords and 22.9% have ambiguous keywords, which accounts for nearly all cases. I should also highlight the striking per-repo variation where scikit-learn has essentially no unparseable instances while sphinx reaches 100%. Before writing, I need to be careful about language—avoiding unsupported claims like "significantly" without statistical tests, "state-of-the-art," or "consistently outperforms," especially given the limited seeds at the repo level. Let me do a final sanity check on the numbers and then write the complete section. I've verified the cross-size comparisons are correct: 8B CLS outperforms 4B CWM by 25.48 percentage points at seed 42 and 26.51 points at seed 123. Now I'm deciding whether to keep the scaling gap figure reference in section 3.3 or add it elsewhere—I think I'll keep it where it is and add a reference in section 3.6 when discussing repo-level gaps, since the figure naturally illustrates that amplification across complexity levels.

I need to clarify what "v12 data" means for the analysis section. The v12 run is the repo-level-cwm-v12 registry entry, which provides the error mode breakdown percentages, while the error complementarity metrics come from function-level analysis and remain consistent regardless of version. Now I'm ready to write the complete section.

Looking at the `\pp{}` macro usage in the existing text, it appears after percentage values like "1.24\pp{}" and "$-$0.27\pp{}", so I need to understand what it adds to these numbers.

The macro just renders "pp" as text, so I'll apply it consistently after all percentage point values throughout the document. For the table, I should check whether the existing format uses the macro or just plain numbers in the cells.

Looking at Table 3, the headers explicitly include `(\pp{})` to indicate the unit, so the cell values are just numbers. I'll follow the same pattern for my table—using "vs Maj.\ (\pp{})" as the header so the values like "+10.67" and "−14.92" don't need individual unit markers.

Generating markdown table... Generating the results table... I'm deciding which accuracy values to bold in the table. The best 4B result is 83.63, which is the primary comparison point, but 85.60 from the 8B model also beats the majority baseline. I'll bold the overall best accuracy to keep it simple and consistent with standard paper conventions. I need to use em dashes for the CWM 8B seed since the task specifies that format, and I'm keeping the resizebox on Table 1 unchanged per the instructions. Now I'm ready to write out the complete file, though I should also check what changes are needed for the Analysis paragraph ordering. I'm looking at the Macro F1 scores in Table 4 to determine what to highlight—the best overall is 78.38 for CLS 8B s123, but since the primary comparison is 4B-to-4B, I'll bold the CLS 4B value of 83.63 as the key reference point. Now I'm ready to write the full section, starting with the opening that establishes the 25.59 percentage point gap between CLS and CWM at the 4B scale. Looking at the 8B WM results coming in — if the performance stays flat compared to 4B, that points to a generation bottleneck rather than a capacity issue. I should also note the experimental setup: the 4B CLS baseline uses a single seed, there's zero overlap between validation and test problems, and the checkpoints were selected from the validation set.

Now for section 3.7, I'm examining the error breakdown from the v12 repo-level data. The unparseable rate is stark — over half the outputs can't be parsed in the smaller model (53.7%) and two-thirds in the larger one (67.2%). Within those unparseable cases, most are missing execution keywords entirely, with a smaller portion having conflicting keywords. What's striking is that when outputs are parseable, the accuracy still falls below random chance, suggesting the model isn't learning the format meaningfully. The variation across repositories is dramatic too — some codebases like scikit-learn have almost no unparseable outputs while others like sphinx hit 100%, indicating that format compliance is heavily dependent on the specific repository context. I'm settling on using the precise 42.88% figure for the detailed analysis in §3.7(b) while keeping the approximate 42–43% range in §3.6 to account for variation across seeds.

Now I need to figure out the parseable-only accuracy for s123—the task doesn't provide it directly. Let me work through the numbers: with 67.2% unparseable (6,574 out of 9,784 samples) and an overall accuracy of 59.09%, I can calculate how many samples were actually correct across the parseable subset.

If unparseable outputs aren't simply counted as errors, they must be handled differently—maybe they default to a particular prediction or are excluded from the accuracy calculation entirely. Looking at the pattern across the models, it seems like the task is giving me the overall accuracy figures directly, so I should focus on extracting the parseable-only accuracy from what's already provided rather than trying to derive it from the unparseable rate. So unparseable outputs are just defaulting to the majority class prediction of pass, which explains why they achieve around 73% accuracy—matching the baseline rate. The parseable outputs perform much worse at 42.88%, suggesting the model struggles when it actually tries to parse. For the writeup, I'll use the approximate range of 42-43% for s123 since I don't have the exact figure, but I'll cite the precise 42.88% for s42 where I have it. Now I need to decide whether to keep or remove the old note about the CWM subset being from 500 samples.

Looking at the new data, all results are on the full test set of 9,784 samples, so that old subset note is outdated and should be removed. The CWM results now use the complete test set, not a smaller sample.

For the §3.6 structure, I'm following the task's outline: starting with the 4B-4B gap, then CWM performance below majority, unparseable rates, parseable-only accuracy, the format compliance collapse explanation, cross-size comparison, CWM 8B progress, and disclosures. This flows naturally. I should also consider whether to reference the scaling gap figure here, since it shows how the gap amplifies across different complexity levels.

The new table needs a Size column added, and I'll use `\textbf{}` for formatting the best values—probably just the primary comparison result of 83.63 for the same-size 4B-4B case to keep it simple. I'll bold the CLS 4B s42 accuracy as the primary result since that's the main comparison. Now I'm structuring Table 4 with seven data rows across the two model sizes, and I need to set up the column alignment with left-aligned method and size columns, then centered numeric columns. For the "vs Maj." column, I'm making sure positive values get a `+` prefix and negative values use the proper minus sign formatting.

Now I'm reviewing which sections need changes: §3.4 and §3.5 stay untouched, §3.2 remains as-is, §3.3 gets mostly preserved but I'll add a forward reference to §3.6, and §3.1 needs minor adjustments to include the repo-level dataset information.

Time to write the full experiments.tex file using the exact numbers from the task. I need to add the ICC citation using the key "shrout1979icc" and incorporate the D088 protocol mention in §3.1 when discussing how repo-level models use validation-selected checkpoints.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "17358a0e-1b09-460a-8e42-758ba4b0ac23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBNL1uLQfm6MHCHSR1w7NS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 25267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17563
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

_source line 12_

Now I'll compose the full rewritten experiments.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "876a7164-3ad6-4ed6-a8be-8bf93c8d123f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBNL1uLQfm6MHCHSR1w7NS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 25267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17563
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

_source line 13_

<details open><summary>🔧 Tool call — Write · `toolu_017LbSemzWjDCYDWQseDN5nF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate \\cls{}, \\cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Function-level dataset.}\nWe construct a function-level benchmark from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} by generating mutated variants (five mutation types: \\texttt{wrong\\_operator}, \\texttt{off\\_by\\_one}, \\texttt{boundary\\_error}, \\texttt{return\\_value}, \\texttt{type\\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\n\\paragraph{Repo-level dataset.}\nWe construct a repo-level benchmark from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\\%. Mutation type composition differs between validation and test due to the non-overlapping problem split.\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).\n\n\\paragraph{Oracle analysis and statistics.}\nWe use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\\cite{shrout1979icc}.\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \\cls{}: per-test binary classification; \\cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\\pm$ std over seeds reported where applicable.}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\\pm$ 0.36 \\\\\nTRAJ (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\nZS LLM-as-judge & 8B & 1 & 64.40 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFine-tuned \\cls{} achieves a mean accuracy of 88.43\\% ($\\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\\% ($\\pm$0.36; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \\cwm{} and 86.30\\% ($\\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \\cls{}--\\cwm{} gap is 1.24\\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.\n\nZero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\\% and Qwen3-32B (NF4) achieves 71.69\\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\\%, pass recall 35.1\\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \\cls{} by 16.74\\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} compares \\cls{} and \\cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: \\cls{} vs.\\ \\cwm{} accuracy (\\%) at 4B and 8B. Three matched seeds in full precision. The \\cls{}--\\cwm{} gap widens from 1.18\\pp{} to 2.43\\pp{}.}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{Gap} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \\multirow{2}{*}{1.18} \\\\\n\\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\\\\n\\midrule\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & 88.31 & \\textbf{89.40} & \\multirow{2}{*}{\\textbf{2.43}} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 4B, \\cls{} and \\cwm{} are separated by 1.18\\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\\pp{} ($p = 0.0066$, 95\\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.\n\nThe asymmetry in scaling efficiency is striking: from 4B to 8B, \\cls{} gains +0.99\\pp{} (88.41 $\\to$ 89.40) while \\cwm{} loses $-$0.27\\pp{} (87.23 $\\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \\cwm{} accuracy. However, the \\cwm{} regression ($-$0.27\\pp{}) falls within seed noise (3-seed std ${\\sim}$0.5\\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\\ref{fig:scaling_gap} visualizes the diverging trajectories. Whether this divergence amplifies at repository-level complexity is examined in \\S\\ref{sec:repo}.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{sec:equivalence}\n\nA natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \\cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.\n\nThe pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\\pm$2\\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.\n\nCritically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\\ confidence intervals would be approximately $2\\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.\n\nThe practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{sec:oracle-results}\n\nWhere does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\\ trajectory-level oracle resolve rates under both i.i.d.\\ and block-correlated error models (using the empirical ICC $= 0.191$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\\% of instances), where block-correlated advantage reaches 31.69\\pp{}, contributing 55.3\\% of the total advantage. Instances with $T \\geq 3$ exhibit block advantages exceeding 40\\pp{} but constitute only 12.2\\% of instances. The overall block-correlated advantage is 10.93\\pp{}, driven almost entirely by the $T \\geq 2$ minority. Figure~\\ref{fig:oracle_stratified} visualizes this distribution.\n\nBlock correlation amplifies the advantage relative to the i.i.d.\\ model: at $T = 2$, the block advantage (31.69\\pp{}) is 1.7$\\times$ the i.i.d.\\ advantage (18.49\\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.\n\n\\paragraph{P2P regression signal.}\nThe P2P regression rate in SWE-bench Verified is low: 1.04\\% mean and 0\\% median---77\\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.\n\n\n\\subsection{Repo-Level Results}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Same-size 4B comparison is primary; \\cls{} 8B included for scaling context; \\cwm{} 8B in progress.}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{Seed} & \\textbf{Acc (\\%)} & \\textbf{Macro \\fone{}} & \\textbf{Unparse (\\%)} & \\textbf{vs Maj.\\ (\\pp{})} \\\\\n\\midrule\n\\cls{} & 4B & 42 & \\textbf{83.63} & 75.63 & 0.0 & +10.67 \\\\\n\\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\\\\n\\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\\\\n\\midrule\n\\cls{} & 8B & 42 & 83.52 & 77.50 & 0.0 & +10.56 \\\\\n\\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & +12.64 \\\\\n\\cwm{} & 8B & --- & --- & --- & --- & --- \\\\\n\\midrule\nMajority & --- & --- & 72.96 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe same-size 4B comparison reveals a 25.59\\pp{} gap: \\cls{} achieves 83.63\\% accuracy (macro \\fone{} 75.63) versus \\cwm{} at 58.04\\% (macro \\fone{} 51.67) on seed 42. \\cwm{} falls 14.92\\pp{} below the majority baseline (72.96\\%), indicating negative utility---a system that always predicts pass outperforms \\cwm{}. A second \\cwm{} seed (123) yields 59.09\\% with a higher unparseable rate (67.2\\% vs.\\ 53.7\\%), confirming the failure is not seed-specific.\n\nThe primary driver is output format compliance collapse. \\cwm{} produces unparseable outputs for 53.7\\% (seed 42) and 67.2\\% (seed 123) of test instances, while \\cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \\cwm{} outputs, accuracy is 42--43\\%---below random chance---indicating that even well-formed \\cwm{} predictions are anti-informative at this complexity level. \\cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\\pp{}) to repo level (25.59\\pp{}).\n\nFor scaling context, we include \\cls{} 8B results. \\cls{} 8B achieves 83.52\\% (seed 42) and 85.60\\% (seed 123), yielding cross-size gaps of 25.48\\pp{} and 26.51\\pp{} against \\cwm{} 4B at the corresponding seeds. Within \\cls{}, the 4B$\\to$8B transition at repo level shows 83.63\\% $\\to$ 83.52\\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \\cwm{} 8B training is in progress; if \\cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.\n\n\\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 test evaluation has not been run. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences.\n\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} make errors in opposite directions at function level. Among \\cls{} errors (seed 42), 75.5\\% are false negatives (FAIL $\\to$ PASS), meaning the classifier tends to over-predict passing. Among \\cwm{} errors, 83.1\\% are false positives (PASS $\\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\\% accuracy, a 3.12\\pp{} improvement over \\cls{} alone (87.51\\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAt repo level, \\cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\\%, seed 42) and 6,574 (67.2\\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\\% contain no execution keywords whatsoever, while 22.9\\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \\cwm{} achieves only 42.88\\% accuracy (seed 42)---below the 50\\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.\n\n\\paragraph{(c) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.36\\pp{}) is lower than \\cls{} (0.78\\pp{}) and TRAJ (0.97\\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \\cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(d) Per-test precision and recall.}\nAt the per-test level (seed 42), \\cls{} achieves fail \\fone{} 87.86\\% (precision 82.75\\%, recall 93.64\\%) and pass \\fone{} 87.15\\%. Of 114 problems, 48 (42.1\\%) are perfectly predicted. Performance varies by mutation type: \\texttt{return\\_value} is easiest (97.3\\%) while \\texttt{off\\_by\\_one} is hardest (82.6\\%). Multi-F2P instances with 6--10 tests reach 96.3\\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.\n\n\\paragraph{(e) Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{(f) Block correlation.}\nPrediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\\times$ more all-correct problems than expected under i.i.d.\\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\\S\\ref{sec:oracle-results}) is the more relevant estimate for deployment.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "9e7f313e-0a7b-41c1-80df-8ea1cae50ea5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GBNL1uLQfm6MHCHSR1w7NS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17563,
      "cache_read_input_tokens": 25267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 17563
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

_source line 14 · 2026-05-15T09:23:03.382Z_

<details><summary>↩ Tool result · `toolu_017LbSemzWjDCYDWQseDN5nF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "a78171bd-1754-4b07-ba61-fe13c7cbcb97",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
    "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate \\cls{}, \\cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Function-level dataset.}\nWe construct a function-level benchmark from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} by generating mutated variants (five mutation types: \\texttt{wrong\\_operator}, \\texttt{off\\_by\\_one}, \\texttt{boundary\\_error}, \\texttt{return\\_value}, \\texttt{type\\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\n\\paragraph{Repo-level dataset.}\nWe construct a repo-level benchmark from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\\%. Mutation type composition differs between validation and test due to the non-overlapping problem split.\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).\n\n\\paragraph{Oracle analysis and statistics.}\nWe use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\\cite{shrout1979icc}.\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \\cls{}: per-test binary classification; \\cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\\pm$ std over seeds reported where applicable.}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\\pm$ 0.36 \\\\\nTRAJ (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\nZS LLM-as-judge & 8B & 1 & 64.40 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFine-tuned \\cls{} achieves a mean accuracy of 88.43\\% ($\\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\\% ($\\pm$0.36; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \\cwm{} and 86.30\\% ($\\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \\cls{}--\\cwm{} gap is 1.24\\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.\n\nZero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\\% and Qwen3-32B (NF4) achieves 71.69\\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\\%, pass recall 35.1\\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \\cls{} by 16.74\\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} compares \\cls{} and \\cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: \\cls{} vs.\\ \\cwm{} accuracy (\\%) at 4B and 8B. Three matched seeds in full precision. The \\cls{}--\\cwm{} gap widens from 1.18\\pp{} to 2.43\\pp{}.}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{Gap} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \\multirow{2}{*}{1.18} \\\\\n\\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\\\\n\\midrule\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & 88.31 & \\textbf{89.40} & \\multirow{2}{*}{\\textbf{2.43}} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 4B, \\cls{} and \\cwm{} are separated by 1.18\\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\\pp{} ($p = 0.0066$, 95\\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.\n\nThe asymmetry in scaling efficiency is striking: from 4B to 8B, \\cls{} gains +0.99\\pp{} (88.41 $\\to$ 89.40) while \\cwm{} loses $-$0.27\\pp{} (87.23 $\\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \\cwm{} accuracy. However, the \\cwm{} regression ($-$0.27\\pp{}) falls within seed noise (3-seed std ${\\sim}$0.5\\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\\ref{fig:scaling_gap} visualizes the diverging trajectories. Whether this divergence amplifies at repository-level complexity is examined in \\S\\ref{sec:repo}.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{sec:equivalence}\n\nA natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \\cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.\n\nThe pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\\pm$2\\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.\n\nCritically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\\ confidence intervals would be approximately $2\\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.\n\nThe practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{sec:oracle-results}\n\nWhere does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\\ trajectory-level oracle resolve rates under both i.i.d.\\ and block-correlated error models (using the empirical ICC $= 0.191$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\\% of instances), where block-correlated advantage reaches 31.69\\pp{}, contributing 55.3\\% of the total advantage. Instances with $T \\geq 3$ exhibit block advantages exceeding 40\\pp{} but constitute only 12.2\\% of instances. The overall block-correlated advantage is 10.93\\pp{}, driven almost entirely by the $T \\geq 2$ minority. Figure~\\ref{fig:oracle_stratified} visualizes this distribution.\n\nBlock correlation amplifies the advantage relative to the i.i.d.\\ model: at $T = 2$, the block advantage (31.69\\pp{}) is 1.7$\\times$ the i.i.d.\\ advantage (18.49\\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.\n\n\\paragraph{P2P regression signal.}\nThe P2P regression rate in SWE-bench Verified is low: 1.04\\% mean and 0\\% median---77\\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.\n\n\n\\subsection{Repo-Level Results}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Same-size 4B comparison is primary; \\cls{} 8B included for scaling context; \\cwm{} 8B in progress.}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{Seed} & \\textbf{Acc (\\%)} & \\textbf{Macro \\fone{}} & \\textbf{Unparse (\\%)} & \\textbf{vs Maj.\\ (\\pp{})} \\\\\n\\midrule\n\\cls{} & 4B & 42 & \\textbf{83.63} & 75.63 & 0.0 & +10.67 \\\\\n\\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\\\\n\\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\\\\n\\midrule\n\\cls{} & 8B & 42 & 83.52 & 77.50 & 0.0 & +10.56 \\\\\n\\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & +12.64 \\\\\n\\cwm{} & 8B & --- & --- & --- & --- & --- \\\\\n\\midrule\nMajority & --- & --- & 72.96 & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe same-size 4B comparison reveals a 25.59\\pp{} gap: \\cls{} achieves 83.63\\% accuracy (macro \\fone{} 75.63) versus \\cwm{} at 58.04\\% (macro \\fone{} 51.67) on seed 42. \\cwm{} falls 14.92\\pp{} below the majority baseline (72.96\\%), indicating negative utility---a system that always predicts pass outperforms \\cwm{}. A second \\cwm{} seed (123) yields 59.09\\% with a higher unparseable rate (67.2\\% vs.\\ 53.7\\%), confirming the failure is not seed-specific.\n\nThe primary driver is output format compliance collapse. \\cwm{} produces unparseable outputs for 53.7\\% (seed 42) and 67.2\\% (seed 123) of test instances, while \\cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \\cwm{} outputs, accuracy is 42--43\\%---below random chance---indicating that even well-formed \\cwm{} predictions are anti-informative at this complexity level. \\cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\\pp{}) to repo level (25.59\\pp{}).\n\nFor scaling context, we include \\cls{} 8B results. \\cls{} 8B achieves 83.52\\% (seed 42) and 85.60\\% (seed 123), yielding cross-size gaps of 25.48\\pp{} and 26.51\\pp{} against \\cwm{} 4B at the corresponding seeds. Within \\cls{}, the 4B$\\to$8B transition at repo level shows 83.63\\% $\\to$ 83.52\\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \\cwm{} 8B training is in progress; if \\cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.\n\n\\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 test evaluation has not been run. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences.\n\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{(a) Error complementarity.}\n\\cls{} and \\cwm{} make errors in opposite directions at function level. Among \\cls{} errors (seed 42), 75.5\\% are false negatives (FAIL $\\to$ PASS), meaning the classifier tends to over-predict passing. Among \\cwm{} errors, 83.1\\% are false positives (PASS $\\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\\% accuracy, a 3.12\\pp{} improvement over \\cls{} alone (87.51\\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.\n\n\\paragraph{(b) CWM error mode breakdown.}\nAt repo level, \\cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\\%, seed 42) and 6,574 (67.2\\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\\% contain no execution keywords whatsoever, while 22.9\\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \\cwm{} achieves only 42.88\\% accuracy (seed 42)---below the 50\\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.\n\n\\paragraph{(c) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.36\\pp{}) is lower than \\cls{} (0.78\\pp{}) and TRAJ (0.97\\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \\cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.\n\n\\paragraph{(d) Per-test precision and recall.}\nAt the per-test level (seed 42), \\cls{} achieves fail \\fone{} 87.86\\% (precision 82.75\\%, recall 93.64\\%) and pass \\fone{} 87.15\\%. Of 114 problems, 48 (42.1\\%) are perfectly predicted. Performance varies by mutation type: \\texttt{return\\_value} is easiest (97.3\\%) while \\texttt{off\\_by\\_one} is hardest (82.6\\%). Multi-F2P instances with 6--10 tests reach 96.3\\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.\n\n\\paragraph{(e) Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{(f) Block correlation.}\nPrediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\\times$ more all-correct problems than expected under i.i.d.\\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\\S\\ref{sec:oracle-results}) is the more relevant estimate for deployment.\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 14,
        "newStart": 6,
        "newLines": 17,
        "lines": [
          " \\subsection{Experimental Setup}",
          " \\label{sec:setup}",
          " ",
          "-\\paragraph{Dataset.}",
          "+\\paragraph{Function-level dataset.}",
          " We construct a function-level benchmark from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} by generating mutated variants (five mutation types: \\texttt{wrong\\_operator}, \\texttt{off\\_by\\_one}, \\texttt{boundary\\_error}, \\texttt{return\\_value}, \\texttt{type\\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).",
          " ",
          "+\\paragraph{Repo-level dataset.}",
          "+We construct a repo-level benchmark from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\\%. Mutation type composition differs between validation and test due to the non-overlapping problem split.",
          "+",
          " \\paragraph{Models and training.}",
          "-We fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.",
          "+We fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).",
          " ",
          " \\paragraph{Oracle analysis and statistics.}",
          "-We use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin.",
          "+We use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\\cite{shrout1979icc}.",
          " ",
          " ",
          " \\subsection{Function-Level Results}"
        ]
      },
      {
        "oldStart": 73,
        "oldLines": 7,
        "newStart": 76,
        "newLines": 7,
        "lines": [
          " ",
          " At 4B, \\cls{} and \\cwm{} are separated by 1.18\\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\\pp{} ($p = 0.0066$, 95\\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.",
          " ",
          "-The asymmetry in scaling efficiency is striking: from 4B to 8B, \\cls{} gains +0.99\\pp{} (88.41 $\\to$ 89.40) while \\cwm{} loses $-$0.27\\pp{} (87.23 $\\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \\cwm{} accuracy. However, the \\cwm{} regression ($-$0.27\\pp{}) falls within seed noise (3-seed std ${\\sim}$0.5\\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\\ref{fig:scaling_gap} visualizes the diverging trajectories.",
          "+The asymmetry in scaling efficiency is striking: from 4B to 8B, \\cls{} gains +0.99\\pp{} (88.41 $\\to$ 89.40) while \\cwm{} loses $-$0.27\\pp{} (87.23 $\\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \\cwm{} accuracy. However, the \\cwm{} regression ($-$0.27\\pp{}) falls within seed noise (3-seed std ${\\sim}$0.5\\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\\ref{fig:scaling_gap} visualizes the diverging trajectories. Whether this divergence amplifies at repository-level complexity is examined in \\S\\ref{sec:repo}.",
          " ",
          " ",
          " \\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}"
        ]
      },
      {
        "oldStart": 125,
        "oldLines": 46,
        "newStart": 128,
        "newLines": 58,
        "lines": [
          " \\subsection{Repo-Level Results}",
          " \\label{sec:repo}",
          " ",
          "-Table~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test data (Qwen3-4B, LoRA, seed 42, max sequence length 2,048).",
          "+Table~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.",
          " ",
          " \\begin{table}[t]",
          " \\centering",
          " \\small",
          "-\\caption{Repo-level per-test verification on SWE-bench Verified (Qwen3-4B, seed 42). CWM: $n{=}500$ random subset; CLS: $n{=}9{,}784$ full test set. \\cwm{} falls below majority baseline, indicating negative utility. Unparseable: fraction of outputs that cannot be parsed into a verdict.}",
          "+\\caption{Repo-level per-test verification on SWE-bench Verified test set ($n{=}9{,}784$, val-selected checkpoints). Same-size 4B comparison is primary; \\cls{} 8B included for scaling context; \\cwm{} 8B in progress.}",
          " \\label{tab:repo_level}",
          " \\resizebox{\\columnwidth}{!}{%",
          "-\\setlength{\\tabcolsep}{4pt}",
          "-\\begin{tabular}{lccccc}",
          "+\\setlength{\\tabcolsep}{3pt}",
          "+\\begin{tabular}{llccccc}",
          " \\toprule",
          "-\\textbf{Method} & \\textbf{Acc.\\%} & \\textbf{Fail \\fone{}} & \\textbf{Pass \\fone{}} & \\textbf{Macro \\fone{}} & \\textbf{Unparse.\\%} \\\\",
          "+\\textbf{Method} & \\textbf{Size} & \\textbf{Seed} & \\textbf{Acc (\\%)} & \\textbf{Macro \\fone{}} & \\textbf{Unparse (\\%)} & \\textbf{vs Maj.\\ (\\pp{})} \\\\",
          " \\midrule",
          "-\\cls{} & \\textbf{76.92} & \\textbf{65.01} & \\textbf{82.78} & \\textbf{73.90} & 1.3 \\\\",
          "-\\cwm{} & 66.60 & 27.70 & 78.30 & 52.99 & 75.2 \\\\",
          "-Majority & 72.96 & --- & --- & --- & --- \\\\",
          "+\\cls{} & 4B & 42 & \\textbf{83.63} & 75.63 & 0.0 & +10.67 \\\\",
          "+\\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\\\",
          "+\\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\\\",
          "+\\midrule",
          "+\\cls{} & 8B & 42 & 83.52 & 77.50 & 0.0 & +10.56 \\\\",
          "+\\cls{} & 8B & 123 & 85.60 & 78.38 & 0.0 & +12.64 \\\\",
          "+\\cwm{} & 8B & --- & --- & --- & --- & --- \\\\",
          "+\\midrule",
          "+Majority & --- & --- & 72.96 & --- & --- & --- \\\\",
          " \\bottomrule",
          " \\end{tabular}}",
          " \\end{table}",
          " ",
          "-The \\cls{}--\\cwm{} gap widens from 1.24\\pp{} at function level to 10.32\\pp{} at repo level. \\cls{} achieves 76.92\\% accuracy (macro \\fone{} 73.90\\%), while \\cwm{} falls to 66.60\\%---below the majority baseline (72.96\\%), indicating negative utility.",
          "+The same-size 4B comparison reveals a 25.59\\pp{} gap: \\cls{} achieves 83.63\\% accuracy (macro \\fone{} 75.63) versus \\cwm{} at 58.04\\% (macro \\fone{} 51.67) on seed 42. \\cwm{} falls 14.92\\pp{} below the majority baseline (72.96\\%), indicating negative utility---a system that always predicts pass outperforms \\cwm{}. A second \\cwm{} seed (123) yields 59.09\\% with a higher unparseable rate (67.2\\% vs.\\ 53.7\\%), confirming the failure is not seed-specific.",
          " ",
          "-The primary driver is output format compliance collapse: 75.2\\% of \\cwm{} outputs are unparseable vs.\\ 1.3\\% for \\cls{}. Crucially, the generation budget (1,024 tokens) is sufficient---mean generated output is 3,398 characters (${\\sim}$850--1,100 tokens, within budget)---indicating that token-budget exhaustion is not the dominant cause. An earlier configuration with a 64-token budget produced 93\\% unparseable outputs; increasing to 1,024 tokens reduced this to 75.2\\%, indicating that format non-compliance, not insufficient budget, is the dominant failure mode: the model generates unstructured text rather than format-compliant execution outputs at repository-level complexity. \\cls{}, producing a single binary token per test, is immune by construction.",
          "+The primary driver is output format compliance collapse. \\cwm{} produces unparseable outputs for 53.7\\% (seed 42) and 67.2\\% (seed 123) of test instances, while \\cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \\cwm{} outputs, accuracy is 42--43\\%---below random chance---indicating that even well-formed \\cwm{} predictions are anti-informative at this complexity level. \\cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\\pp{}) to repo level (25.59\\pp{}).",
          " ",
          "-CWM results are from a 500-sample subset (95\\% CI: [62.5\\%, 70.7\\%]); CLS uses the full 9,784-sample test set. A full 9,784-sample CWM evaluation is underway; preliminary 500-sample results are reported here and will be updated upon completion. Both are single-seed; multi-seed replication is also in progress.",
          "+For scaling context, we include \\cls{} 8B results. \\cls{} 8B achieves 83.52\\% (seed 42) and 85.60\\% (seed 123), yielding cross-size gaps of 25.48\\pp{} and 26.51\\pp{} against \\cwm{} 4B at the corresponding seeds. Within \\cls{}, the 4B$\\to$8B transition at repo level shows 83.63\\% $\\to$ 83.52\\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \\cwm{} 8B training is in progress; if \\cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.",
          " ",
          "+\\paragraph{Limitations.} The same-size 4B comparison uses a single seed; \\cls{} 4B seed 123 test evaluation has not been run. The validation and test sets have zero problem overlap but differ in mutation type composition, introducing potential distribution shift. All repo-level results use val-selected checkpoints, and checkpoint selection variance could contribute to observed differences.",
          "+",
          "+",
          " \\subsection{Analysis}",
          " \\label{sec:analysis}",
          " ",
          "-\\paragraph{(a) Variance compression.}",
          "-\\cwm{}'s 5-seed standard deviation (0.36\\pp{}) is notably lower than \\cls{} (0.78\\pp{}) and TRAJ (0.97\\pp{}). This is consistent with the bottleneck hypothesis: if \\cwm{} performance is capped by output-format constraints (exact string matching), seed-to-seed variability is naturally compressed relative to formulations whose performance depends more on learned representations---though reduced variance could also reflect ceiling effects inherent to exact-match evaluation.",
          "+\\paragraph{(a) Error complementarity.}",
          "+\\cls{} and \\cwm{} make errors in opposite directions at function level. Among \\cls{} errors (seed 42), 75.5\\% are false negatives (FAIL $\\to$ PASS), meaning the classifier tends to over-predict passing. Among \\cwm{} errors, 83.1\\% are false positives (PASS $\\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\\% accuracy, a 3.12\\pp{} improvement over \\cls{} alone (87.51\\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains.",
          " ",
          "-\\paragraph{(b) Error complementarity.}",
          "-\\cls{} and \\cwm{} make errors in opposite directions. Among \\cls{} errors (seed 42), 75.5\\% are false negatives (FAIL $\\to$ PASS), meaning the classifier tends to over-predict passing. Among \\cwm{} errors, 83.1\\% are false positives (PASS $\\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\\% accuracy, a 3.12\\pp{} improvement over \\cls{} alone (87.51\\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains, though we leave this to future work.",
          "+\\paragraph{(b) CWM error mode breakdown.}",
          "+At repo level, \\cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\\%, seed 42) and 6,574 (67.2\\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\\% contain no execution keywords whatsoever, while 22.9\\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \\cwm{} achieves only 42.88\\% accuracy (seed 42)---below the 50\\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.",
          " ",
          "-\\paragraph{(c) Per-test precision and recall.}",
          "+\\paragraph{(c) Variance compression.}",
          "+\\cwm{}'s 5-seed standard deviation (0.36\\pp{}) is lower than \\cls{} (0.78\\pp{}) and TRAJ (0.97\\pp{}) at function level. This is consistent with the bottleneck hypothesis: if \\cwm{} performance is capped by output-format constraints, seed-to-seed variability is compressed relative to formulations whose performance depends more on learned representations.",
          "+",
          "+\\paragraph{(d) Per-test precision and recall.}",
          " At the per-test level (seed 42), \\cls{} achieves fail \\fone{} 87.86\\% (precision 82.75\\%, recall 93.64\\%) and pass \\fone{} 87.15\\%. Of 114 problems, 48 (42.1\\%) are perfectly predicted. Performance varies by mutation type: \\texttt{return\\_value} is easiest (97.3\\%) while \\texttt{off\\_by\\_one} is hardest (82.6\\%). Multi-F2P instances with 6--10 tests reach 96.3\\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.",
          " ",
          "-\\paragraph{(d) Majority voting.}",
          "+\\paragraph{(e) Majority voting.}",
          " Majority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.",
          " ",
          "-\\paragraph{(e) Block correlation.}",
          "-Prediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\\times$ more all-correct problems than expected under i.i.d.\\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\\S\\ref{sec:oracle}) is the more relevant estimate for deployment.",
          "+\\paragraph{(f) Block correlation.}",
          "+Prediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\\times$ more all-correct problems than expected under i.i.d.\\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\\S\\ref{sec:oracle-results}) is the more relevant estimate for deployment."
        ]
      }
    ],
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate \\cls{}, \\cwm{}, and trajectory-level scoring (TRAJ) across model sizes and complexity levels.\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Dataset.}\nWe construct a function-level benchmark from HumanEval~\\cite{chen2021humaneval} and MBPP~\\cite{austin2021mbpp} by generating mutated variants (five mutation types: \\texttt{wrong\\_operator}, \\texttt{off\\_by\\_one}, \\texttt{boundary\\_error}, \\texttt{return\\_value}, \\texttt{type\\_error}), with labels verified by execution (5s timeout). The dataset contains 19,076 samples (train 15,290 / val 1,896 / test 1,890; pass:fail $\\approx$ 52:48, majority baseline 51.75\\%).\n\n\\paragraph{Models and training.}\nWe fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge.\n\n\\paragraph{Oracle analysis and statistics.}\nWe use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin.\n\n\n\\subsection{Function-Level Results}\n\\label{sec:func_results}\n\nTable~\\ref{tab:main_results} reports function-level results across formulations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Function-level per-test verification results on HumanEval+MBPP test set (1,890 samples). \\cls{}: per-test binary classification; \\cwm{}: execution output generation; TRAJ: trajectory-level scoring; ZS: zero-shot LLM-as-judge. Mean $\\pm$ std over seeds reported where applicable.}\n\\label{tab:main_results}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{Method} & \\textbf{Model} & \\textbf{Seeds} & \\textbf{Accuracy (\\%)} \\\\\n\\midrule\n\\cls{} (fine-tuned) & 4B & 5 & \\textbf{88.43 $\\pm$ 0.78} \\\\\n\\cwm{} (fine-tuned) & 4B & 5 & 87.19 $\\pm$ 0.36 \\\\\nTRAJ (fine-tuned) & 4B & 5 & 86.30 $\\pm$ 0.97 \\\\\n\\midrule\nZS LLM-as-judge & 8B & 1 & 64.40 \\\\\nZS LLM-as-judge & 32B (NF4) & 1 & 71.69 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFine-tuned \\cls{} achieves a mean accuracy of 88.43\\% ($\\pm$0.78 across seeds 87.83, 89.52, 87.88, 89.00, 87.94), compared to 87.19\\% ($\\pm$0.36; seeds: 87.51, 87.20, 86.98, 86.67, 87.57) for \\cwm{} and 86.30\\% ($\\pm$0.97; seeds: 85.66, 85.47, 87.40, 87.31, 85.66) for TRAJ. The \\cls{}--\\cwm{} gap is 1.24\\pp{}, which is modest at this complexity level---both formulations operate on short, single-function code with simple return values, where generation is not yet bottlenecked by token budget or string complexity.\n\nZero-shot baselines lag by a wide margin: Qwen3-8B achieves 64.40\\% and Qwen3-32B (NF4) achieves 71.69\\%, both far below fine-tuned 4B models. The 8B zero-shot model exhibits a strong FAIL bias (fail recall 95.8\\%, pass recall 35.1\\%), indicating that zero-shot prompting cannot achieve the balanced precision/recall that fine-tuning produces. Even with 8$\\times$ more parameters, the 32B zero-shot model trails the fine-tuned 4B \\cls{} by 16.74\\pp{}, confirming that task-specific fine-tuning, rather than model scale alone, is necessary for reliable per-test verification.\n\n\n\\subsection{Scaling Behavior}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} compares \\cls{} and \\cwm{} at two model sizes using three matched seeds (42, 123, 456), all trained in full bfloat16 precision to ensure a controlled comparison.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Model-size scaling: \\cls{} vs.\\ \\cwm{} accuracy (\\%) at 4B and 8B. Three matched seeds in full precision. The \\cls{}--\\cwm{} gap widens from 1.18\\pp{} to 2.43\\pp{}.}\n\\label{tab:scaling}\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{llccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Size} & \\textbf{s42} & \\textbf{s123} & \\textbf{s456} & \\textbf{Mean} & \\textbf{Gap} \\\\\n\\midrule\n\\cls{} & 4B & 87.83 & 89.52 & 87.88 & 88.41 & \\multirow{2}{*}{1.18} \\\\\n\\cwm{} & 4B & 87.51 & 87.20 & 86.98 & 87.23 & \\\\\n\\midrule\n\\cls{} & 8B & \\textbf{90.48} & 89.40 & 88.31 & \\textbf{89.40} & \\multirow{2}{*}{\\textbf{2.43}} \\\\\n\\cwm{} & 8B & 87.67 & 86.98 & 86.24 & 86.96 & \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAt 4B, \\cls{} and \\cwm{} are separated by 1.18\\pp{} on the matched three-seed subset. At 8B, the gap more than doubles to 2.43\\pp{}. Clustered bootstrap analysis yields a mean gap of 2.26\\pp{} ($p = 0.0066$, 95\\% CI $[1.80, 2.71]$), confirming the widening is not a sampling artifact.\n\nThe asymmetry in scaling efficiency is striking: from 4B to 8B, \\cls{} gains +0.99\\pp{} (88.41 $\\to$ 89.40) while \\cwm{} loses $-$0.27\\pp{} (87.23 $\\to$ 86.96). The additional model capacity benefits classification---where the model needs only to discriminate pass from fail---but provides no measurable improvement for generation, where the model must additionally produce exact output strings. This pattern is consistent with the hypothesis that the string-prediction bottleneck, not model capacity, bounds \\cwm{} accuracy. However, the \\cwm{} regression ($-$0.27\\pp{}) falls within seed noise (3-seed std ${\\sim}$0.5\\pp{}) and could reflect suboptimal hyperparameter transfer (LoRA rank and learning rate were not re-tuned for 8B) rather than a fundamental bottleneck; disentangling these factors requires larger-scale experiments. We also acknowledge the limited model-level statistical power of three seeds: while the clustered bootstrap provides instance-level confidence (1,890 samples $\\times$ 10K resamples), three model instances cannot fully separate seed variance from systematic scaling effects. Figure~\\ref{fig:scaling_gap} visualizes the diverging trajectories.\n\n\n\\subsection{Per-Test vs.\\ Trajectory-Level Equivalence}\n\\label{sec:equivalence}\n\nA natural concern is whether per-test predictions, when aggregated to the variant level, match the accuracy of a model trained directly at that granularity. We address this by comparing \\cls{} (aggregated via all-pass rule) against TRAJ on 523 variant-level instances across five seeds.\n\nThe pooled gap is $-$0.45\\pp{} (95\\% CI [$-$1.71, +0.84]), with per-seed gaps ranging from $-$1.84 to +1.45\\pp{} (seed 42: $-$0.97; seed 123: +1.45; seed 456: $-$1.84; seed 789: $-$0.78; seed 0: $-$0.29). The TOST equivalence test rejects the null hypothesis of non-equivalence at $p = 0.007$ with a $\\pm$2\\pp{} margin, confirming that per-test classification and trajectory-level scoring achieve statistically equivalent variant-level accuracy.\n\nCritically, however, predictions within the same problem are not independent. The intraclass correlation coefficient is ICC $= 0.191$ ($p < 0.0001$), yielding a design effect DEFF $= 3.97$. This means that naive i.i.d.\\ confidence intervals would be approximately $2\\times$ too narrow. All statistical tests in this paper use clustered bootstrap to account for this within-problem correlation.\n\nThe practical implication is clear: per-test classification provides per-test diagnostic information---which specific tests fail and why---at no cost to variant-level accuracy. A trajectory-level model gives only a binary patch verdict, discarding the per-test signal that downstream repair systems could exploit for targeted re-repair.\n\n\n\\subsection{Accuracy-Utility Frontier}\n\\label{sec:oracle-results}\n\nWhere does per-test granularity actually help? We formalize this via an oracle analysis on SWE-bench Verified, stratifying instances by the number of F2P tests $T$ and comparing per-test vs.\\ trajectory-level oracle resolve rates under both i.i.d.\\ and block-correlated error models (using the empirical ICC $= 0.191$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Oracle accuracy-utility frontier: per-test advantage stratified by F2P test count ($T$) on SWE-bench Verified (500 instances). Block-correlated model uses empirical ICC $= 0.191$. P2P regression rate: 1.04\\% mean, 0\\% median.}\n\\label{tab:oracle}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{$T$} & \\textbf{Inst.\\%} & \\textbf{i.i.d.\\ (\\pp{})} & \\textbf{Block (\\pp{})} & \\textbf{Contrib.\\%} \\\\\n\\midrule\n$1$ & 68.7 & $-$0.04 & $-$0.09 & $\\approx$0 \\\\\n$2$ & 19.1 & 18.49 & 31.69 & 55.3 \\\\\n$3$--$5$ & 7.1 & 25.00 & 40.74 & $\\approx$26 \\\\\n$\\geq 6$ & 5.1 & 30.00 & 40.06 & $\\approx$19 \\\\\n\\midrule\n\\textbf{All} & 100.0 & --- & \\textbf{10.93} & 100.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nTable~\\ref{tab:oracle} reveals a sharp concentration of per-test advantage. When $T = 1$---the dominant case at 68.7\\% of SWE-bench instances---per-test and trajectory-level are informationally equivalent (block advantage $-$0.09\\pp{}), because a single F2P test provides no more signal than a binary patch verdict. The advantage materializes at $T = 2$ (19.1\\% of instances), where block-correlated advantage reaches 31.69\\pp{}, contributing 55.3\\% of the total advantage. Instances with $T \\geq 3$ exhibit block advantages exceeding 40\\pp{} but constitute only 12.2\\% of instances. The overall block-correlated advantage is 10.93\\pp{}, driven almost entirely by the $T \\geq 2$ minority. Figure~\\ref{fig:oracle_stratified} visualizes this distribution.\n\nBlock correlation amplifies the advantage relative to the i.i.d.\\ model: at $T = 2$, the block advantage (31.69\\pp{}) is 1.7$\\times$ the i.i.d.\\ advantage (18.49\\pp{}). This occurs because correlated errors make the per-test classifier more likely to get all tests correct or all wrong for a given problem, increasing the information value of each additional test.\n\n\\paragraph{P2P regression signal.}\nThe P2P regression rate in SWE-bench Verified is low: 1.04\\% mean and 0\\% median---77\\% of incorrect patches break zero P2P tests. This means per-test granularity on the P2P dimension currently provides minimal signal. The practical value of per-test verification concentrates in F2P discrimination, particularly for instances with multiple F2P tests.\n\n\n\\subsection{Repo-Level Results}\n\\label{sec:repo}\n\nTable~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test data (Qwen3-4B, LoRA, seed 42, max sequence length 2,048).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Repo-level per-test verification on SWE-bench Verified (Qwen3-4B, seed 42). CWM: $n{=}500$ random subset; CLS: $n{=}9{,}784$ full test set. \\cwm{} falls below majority baseline, indicating negative utility. Unparseable: fraction of outputs that cannot be parsed into a verdict.}\n\\label{tab:repo_level}\n\\resizebox{\\columnwidth}{!}{%\n\\setlength{\\tabcolsep}{4pt}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Method} & \\textbf{Acc.\\%} & \\textbf{Fail \\fone{}} & \\textbf{Pass \\fone{}} & \\textbf{Macro \\fone{}} & \\textbf{Unparse.\\%} \\\\\n\\midrule\n\\cls{} & \\textbf{76.92} & \\textbf{65.01} & \\textbf{82.78} & \\textbf{73.90} & 1.3 \\\\\n\\cwm{} & 66.60 & 27.70 & 78.30 & 52.99 & 75.2 \\\\\nMajority & 72.96 & --- & --- & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe \\cls{}--\\cwm{} gap widens from 1.24\\pp{} at function level to 10.32\\pp{} at repo level. \\cls{} achieves 76.92\\% accuracy (macro \\fone{} 73.90\\%), while \\cwm{} falls to 66.60\\%---below the majority baseline (72.96\\%), indicating negative utility.\n\nThe primary driver is output format compliance collapse: 75.2\\% of \\cwm{} outputs are unparseable vs.\\ 1.3\\% for \\cls{}. Crucially, the generation budget (1,024 tokens) is sufficient---mean generated output is 3,398 characters (${\\sim}$850--1,100 tokens, within budget)---indicating that token-budget exhaustion is not the dominant cause. An earlier configuration with a 64-token budget produced 93\\% unparseable outputs; increasing to 1,024 tokens reduced this to 75.2\\%, indicating that format non-compliance, not insufficient budget, is the dominant failure mode: the model generates unstructured text rather than format-compliant execution outputs at repository-level complexity. \\cls{}, producing a single binary token per test, is immune by construction.\n\nCWM results are from a 500-sample subset (95\\% CI: [62.5\\%, 70.7\\%]); CLS uses the full 9,784-sample test set. A full 9,784-sample CWM evaluation is underway; preliminary 500-sample results are reported here and will be updated upon completion. Both are single-seed; multi-seed replication is also in progress.\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{(a) Variance compression.}\n\\cwm{}'s 5-seed standard deviation (0.36\\pp{}) is notably lower than \\cls{} (0.78\\pp{}) and TRAJ (0.97\\pp{}). This is consistent with the bottleneck hypothesis: if \\cwm{} performance is capped by output-format constraints (exact string matching), seed-to-seed variability is naturally compressed relative to formulations whose performance depends more on learned representations---though reduced variance could also reflect ceiling effects inherent to exact-match evaluation.\n\n\\paragraph{(b) Error complementarity.}\n\\cls{} and \\cwm{} make errors in opposite directions. Among \\cls{} errors (seed 42), 75.5\\% are false negatives (FAIL $\\to$ PASS), meaning the classifier tends to over-predict passing. Among \\cwm{} errors, 83.1\\% are false positives (PASS $\\to$ FAIL), reflecting string-matching failures that incorrectly reject correct outputs. An oracle combination that takes the correct answer whenever either model is right achieves 90.63\\% accuracy, a 3.12\\pp{} improvement over \\cls{} alone (87.51\\%). This complementarity suggests that ensemble approaches combining classification and generation signals could yield further gains, though we leave this to future work.\n\n\\paragraph{(c) Per-test precision and recall.}\nAt the per-test level (seed 42), \\cls{} achieves fail \\fone{} 87.86\\% (precision 82.75\\%, recall 93.64\\%) and pass \\fone{} 87.15\\%. Of 114 problems, 48 (42.1\\%) are perfectly predicted. Performance varies by mutation type: \\texttt{return\\_value} is easiest (97.3\\%) while \\texttt{off\\_by\\_one} is hardest (82.6\\%). Multi-F2P instances with 6--10 tests reach 96.3\\% accuracy, corroborating the oracle finding that per-test granularity is most valuable with multiple F2P tests.\n\n\\paragraph{(d) Majority voting.}\nMajority voting ($K{=}3$) decreases accuracy from 87.51\\% to 86.83\\% ($-$0.68\\pp{}): errors are systematic rather than stochastic, so sampling-based ensembles do not help.\n\n\\paragraph{(e) Block correlation.}\nPrediction errors within the same problem are correlated: ICC $= 0.191$ ($p < 0.0001$), DEFF $= 3.97$, with 2.81$\\times$ more all-correct problems than expected under i.i.d.\\ errors. All statistical tests use clustered bootstrap to account for this, and the block-correlated oracle model (\\S\\ref{sec:oracle}) is the more relevant estimate for deployment.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
The file has been written. Let me verify it by reading it back to make sure everything is correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "23f6e3ae-6bfb-4232-9759-05b030797495",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdBLYbjJCSg73v8rtFfFa3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20981,
      "cache_read_input_tokens": 42830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20981
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

Let me verify the output compiles structurally by checking for balanced LaTeX environments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "b6168644-b1fd-40ef-b342-1ddf5463d6b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdBLYbjJCSg73v8rtFfFa3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20981,
      "cache_read_input_tokens": 42830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20981
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

<details open><summary>🔧 Tool call — Bash · `toolu_01YVSD1XUsiQmnznZevP5ppY`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper && grep -c '\\\\begin{table}' experiments.tex && grep -c '\\\\end{table}' experiments.tex && grep -c '\\\\begin{tabular}' experiments.tex && grep -c '\\\\end{tabular}' experiments.tex && grep -c '\\\\toprule' experiments.tex && grep -c '\\\\bottomrule' experiments.tex",
  "description": "Count LaTeX table environment open/close pairs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "917d2a8b-5f90-4bcc-8c4c-3983c1d09d1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdBLYbjJCSg73v8rtFfFa3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20981,
      "cache_read_input_tokens": 42830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20981
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

_source line 18 · 2026-05-15T09:23:09.706Z_

<details><summary>↩ Tool result · `toolu_01YVSD1XUsiQmnznZevP5ppY`</summary>

```text
4
4
4
4
4
4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "f53e9b87-deca-409f-854e-2a141b1c2b1b",
  "tool_use_result": {
    "stdout": "4\n4\n4\n4\n4\n4",
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_015ySkN3eBc3dHuxPWtVGLRy`</summary>

```json
{
  "command": "wc -w /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "description": "Count words in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "36ad7ce8-9b7f-4724-a55a-f158a27ed17b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AdBLYbjJCSg73v8rtFfFa3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20981,
      "cache_read_input_tokens": 42830,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20981
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

_source line 20 · 2026-05-15T09:23:10.258Z_

<details><summary>↩ Tool result · `toolu_015ySkN3eBc3dHuxPWtVGLRy`</summary>

```text
2336 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "404b0dbf-a7c7-410c-9b86-5afb02b39960",
  "tool_use_result": {
    "stdout": "2336 /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
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

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
4 tables, all balanced (4 begin/end pairs each for table, tabular, toprule, bottomrule). 

Word count: 2336 words including LaTeX markup. Actual prose word count is somewhat lower than the raw count since LaTeX commands eat into the count. But the task budget is ~2800 words, and this is close. The raw `wc -w` count of 2336 includes all LaTeX commands like `\cls{}`, `\cwm{}`, `\textbf{}`, etc. The actual prose word count should be around 2000-2200 words. 

The 2800-word budget is an upper limit, not a target, so I'm good on length. Let me double-check that all the key numbers are actually in there.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "d8614fac-59b4-4c97-8f14-e6733df9aed9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNxSSAbCZicnqg4GpdmQtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 63811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 461
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

_source line 22_

4 tables, all balanced. 2336 raw words (LaTeX markup included; prose is within the ~2800 budget).

Let me spot-check the key numbers are present.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "febdde45-4ece-4435-859d-022d3b51f7a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNxSSAbCZicnqg4GpdmQtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 63811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 461
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

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_013hMSfARZ4GYDmg4e2wFvMk`</summary>

```json
{
  "command": "grep -n '25.59\\|83.63\\|58.04\\|42.88\\|53.7\\|67.2\\|72.96\\|shrout1979icc\\|D088\\|9,784\\|9,335\\|70K\\|76.9\\|22.9\\|5,255\\|6,574\\|25.48\\|26.51\\|42--43' /home/ubuntu/.agent-ml-research-idea_gen_0509_16/projects/exec-sim-repair-verifier/docs/paper/experiments.tex",
  "description": "Verify key numbers and references in experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "f4d4f40c-0eec-4915-9347-4b8d73508a56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QNxSSAbCZicnqg4GpdmQtf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 461,
      "cache_read_input_tokens": 63811,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 461
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

### Runtime record

_source line 24_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779206400,
    "rateLimitType": "seven_day",
    "utilization": 0.78,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "2b1153db-6095-4bb4-b8ee-0fc49b35d921",
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a"
}
```

---

### Tool result

_source line 25 · 2026-05-15T09:23:20.715Z_

<details><summary>↩ Tool result · `toolu_013hMSfARZ4GYDmg4e2wFvMk`</summary>

```text
13:We construct a repo-level benchmark from SWE-bench Verified~\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\%. Mutation type composition differs between validation and test due to the non-overlapping problem split.
16:We fine-tune Qwen3-4B and Qwen3-8B~\cite{yang2024qwen25} with LoRA~\cite{hu2022lora} (rank 16, lr $2{\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).
19:We use SWE-bench Verified~\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\S\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\ trajectory-level comparison uses TOST~\cite{schuirmann1987tost} with $\pm$2\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\cite{shrout1979icc}.
131:Table~\ref{tab:repo_level} compares \cls{} and \cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.
144:\cls{} & 4B & 42 & \textbf{83.63} & 75.63 & 0.0 & +10.67 \\
145:\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\
146:\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\
152:Majority & --- & --- & 72.96 & --- & --- & --- \\
157:The same-size 4B comparison reveals a 25.59\pp{} gap: \cls{} achieves 83.63\% accuracy (macro \fone{} 75.63) versus \cwm{} at 58.04\% (macro \fone{} 51.67) on seed 42. \cwm{} falls 14.92\pp{} below the majority baseline (72.96\%), indicating negative utility---a system that always predicts pass outperforms \cwm{}. A second \cwm{} seed (123) yields 59.09\% with a higher unparseable rate (67.2\% vs.\ 53.7\%), confirming the failure is not seed-specific.
159:The primary driver is output format compliance collapse. \cwm{} produces unparseable outputs for 53.7\% (seed 42) and 67.2\% (seed 123) of test instances, while \cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \cwm{} outputs, accuracy is 42--43\%---below random chance---indicating that even well-formed \cwm{} predictions are anti-informative at this complexity level. \cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\pp{}) to repo level (25.59\pp{}).
161:For scaling context, we include \cls{} 8B results. \cls{} 8B achieves 83.52\% (seed 42) and 85.60\% (seed 123), yielding cross-size gaps of 25.48\pp{} and 26.51\pp{} against \cwm{} 4B at the corresponding seeds. Within \cls{}, the 4B$\to$8B transition at repo level shows 83.63\% $\to$ 83.52\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \cwm{} 8B training is in progress; if \cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.
173:At repo level, \cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\%, seed 42) and 6,574 (67.2\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\% contain no execution keywords whatsoever, while 22.9\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \cwm{} achieves only 42.88\% accuracy (seed 42)---below the 50\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "d6a07dcd-d8cd-4ac0-acf9-ba47c7b018c6",
  "tool_use_result": {
    "stdout": "13:We construct a repo-level benchmark from SWE-bench Verified~\\cite{chowdhury2024swebenchverified} mutants, extracting per-test instances from repository-scale patches. The dataset contains approximately 70K training samples, with validation ($n{=}9{,}335$) and test ($n{=}9{,}784$) splits having zero problem overlap. The majority baseline (always predict pass) is 72.96\\%. Mutation type composition differs between validation and test due to the non-overlapping problem split.\n16:We fine-tune Qwen3-4B and Qwen3-8B~\\cite{yang2024qwen25} with LoRA~\\cite{hu2022lora} (rank 16, lr $2{\\times}10^{-5}$, 3 epochs) across five seeds (42, 123, 456, 789, 0). Seeds 42/123/456 use bfloat16; seeds 789/0 use NF4 quantization~\\cite{dettmers2024qlora}. We report matched-precision subsets where precision matters. Zero-shot baselines use Qwen3-8B and Qwen3-32B (NF4) as LLM-as-judge. Repo-level models use val-selected checkpoints: we select the checkpoint with highest validation accuracy for test evaluation (D088 protocol).\n19:We use SWE-bench Verified~\\cite{chowdhury2024swebenchverified} (500 instances) to derive the accuracy-utility frontier (\\S\\ref{sec:oracle}). All confidence intervals use clustered bootstrap~\\cite{davison1997bootstrap} (114 problem clusters, 10K resamples); the per-test vs.\\ trajectory-level comparison uses TOST~\\cite{schuirmann1987tost} with $\\pm$2\\pp{} margin. Within-problem correlation is quantified via the intraclass correlation coefficient~\\cite{shrout1979icc}.\n131:Table~\\ref{tab:repo_level} compares \\cls{} and \\cwm{} on SWE-bench Verified per-test classification at repository-level complexity. All checkpoints are selected by validation accuracy (D088 protocol); the test set ($n{=}9{,}784$) has zero problem overlap with validation.\n144:\\cls{} & 4B & 42 & \\textbf{83.63} & 75.63 & 0.0 & +10.67 \\\\\n145:\\cwm{} & 4B & 42 & 58.04 & 51.67 & 53.7 & $-$14.92 \\\\\n146:\\cwm{} & 4B & 123 & 59.09 & 43.43 & 67.2 & $-$13.87 \\\\\n152:Majority & --- & --- & 72.96 & --- & --- & --- \\\\\n157:The same-size 4B comparison reveals a 25.59\\pp{} gap: \\cls{} achieves 83.63\\% accuracy (macro \\fone{} 75.63) versus \\cwm{} at 58.04\\% (macro \\fone{} 51.67) on seed 42. \\cwm{} falls 14.92\\pp{} below the majority baseline (72.96\\%), indicating negative utility---a system that always predicts pass outperforms \\cwm{}. A second \\cwm{} seed (123) yields 59.09\\% with a higher unparseable rate (67.2\\% vs.\\ 53.7\\%), confirming the failure is not seed-specific.\n159:The primary driver is output format compliance collapse. \\cwm{} produces unparseable outputs for 53.7\\% (seed 42) and 67.2\\% (seed 123) of test instances, while \\cls{} produces zero unparseable outputs across all configurations. The generation budget (1,024 tokens) is sufficient for the outputs required---this is not a token-budget limitation but a failure of the model to produce structured execution predictions when faced with repository-level code complexity. Among parseable \\cwm{} outputs, accuracy is 42--43\\%---below random chance---indicating that even well-formed \\cwm{} predictions are anti-informative at this complexity level. \\cls{}, producing a single binary token per test, is immune to format compliance failures by construction. Figure~\\ref{fig:scaling_gap} visualizes the gap amplification from function level (1.24\\pp{}) to repo level (25.59\\pp{}).\n161:For scaling context, we include \\cls{} 8B results. \\cls{} 8B achieves 83.52\\% (seed 42) and 85.60\\% (seed 123), yielding cross-size gaps of 25.48\\pp{} and 26.51\\pp{} against \\cwm{} 4B at the corresponding seeds. Within \\cls{}, the 4B$\\to$8B transition at repo level shows 83.63\\% $\\to$ 83.52\\% (seed 42), a difference within noise, suggesting that classification may be approaching a capacity ceiling at repo-level complexity or that checkpoint selection variance dominates at this scale. \\cwm{} 8B training is in progress; if \\cwm{} 8B performs similarly to 4B, this would confirm a generation bottleneck rather than a capacity limitation.\n173:At repo level, \\cwm{} output format compliance collapses. Of 9,784 test instances, 5,255 (53.7\\%, seed 42) and 6,574 (67.2\\%, seed 123) produce unparseable outputs. Among unparseable outputs, 76.9\\% contain no execution keywords whatsoever, while 22.9\\% contain ambiguous co-occurring keywords for both pass and fail. Among parseable outputs, \\cwm{} achieves only 42.88\\% accuracy (seed 42)---below the 50\\% random baseline, indicating that even when the model produces well-formed outputs, its predictions are anti-informative. Format compliance varies across repositories: scikit-learn instances yield near-zero unparseable rates, while sphinx instances are 100\\% unparseable. This per-repo variation suggests that certain code contexts---likely those with complex execution traces or domain-specific output patterns---prevent the model from generating structured responses.",
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

All key numbers verified present: 25.59pp gap, 83.63/58.04 accuracy, 42.88% parseable-only, 53.7/67.2% unparseable, 72.96% majority, shrout1979icc citation, D088 protocol, dataset sizes (70K/9,335/9,784), error mode breakdown (76.9%/22.9%), cross-size gaps (25.48/26.51pp), 42--43% parseable range, absolute counts (5,255/6,574).

完成。experiments.tex 已完全重写：
- §3.1: 新增 repo-level dataset 段落（70K/9,335/9,784）、ICC 引用（shrout1979icc）、D088 val-selected checkpoint protocol
- §3.2–§3.5: 保持不变，§3.3 末尾加了 §3.6 前向引用
- §3.6: 两层 C1 结构完全重写——7 列新 Table 4（含 Size 列），same-size 4B-4B 25.59pp 为主，cross-size 8B CLS vs 4B CWM 为辅，CWM 8B placeholder，单 seed 限制显式披露
- §3.7: 重写为 6 段（a–f），新增 (b) CWM error mode breakdown（v12 repo-level 数据：unparseable 分类、parseable-only 42.88%、per-repo variation）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "uuid": "b6743e9f-c1cb-4800-a370-48b97b8acb62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWSNDJDmh7YJUBEUoc4AxL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2091,
      "cache_read_input_tokens": 64272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2091
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

_source line 27_

All key numbers verified present: 25.59pp gap, 83.63/58.04 accuracy, 42.88% parseable-only, 53.7/67.2% unparseable, 72.96% majority, shrout1979icc citation, D088 protocol, dataset sizes (70K/9,335/9,784), error mode breakdown (76.9%/22.9%), cross-size gaps (25.48/26.51pp), 42--43% parseable range, absolute counts (5,255/6,574).

完成。experiments.tex 已完全重写：
- §3.1: 新增 repo-level dataset 段落（70K/9,335/9,784）、ICC 引用（shrout1979icc）、D088 val-selected checkpoint protocol
- §3.2–§3.5: 保持不变，§3.3 末尾加了 §3.6 前向引用
- §3.6: 两层 C1 结构完全重写——7 列新 Table 4（含 Size 列），same-size 4B-4B 25.59pp 为主，cross-size 8B CLS vs 4B CWM 为辅，CWM 8B placeholder，单 seed 限制显式披露
- §3.7: 重写为 6 段（a–f），新增 (b) CWM error mode breakdown（v12 repo-level 数据：unparseable 分类、parseable-only 42.88%、per-repo variation）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 433938,
  "duration_api_ms": 434919,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "a29dc0d3-e559-4cb8-b535-ce37aa598d9a",
  "total_cost_usd": 1.007479,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 54522,
    "cache_read_input_tokens": 208021,
    "output_tokens": 22389,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 54522,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 392,
        "cache_read_input_tokens": 64272,
        "cache_creation_input_tokens": 2091,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2091
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2856,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002946,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 22389,
      "cacheReadInputTokens": 208021,
      "cacheCreationInputTokens": 54522,
      "webSearchRequests": 0,
      "costUSD": 1.004533,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "739af956-c9ab-46dd-9208-daca521a1ce2"
}
```

</details>

---
