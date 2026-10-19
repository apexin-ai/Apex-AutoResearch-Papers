# paper writing

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_writing_20260515T202415.log`
- **Structured JSON:** [`0904490d491e0688f34a.json`](../../sessions/09/0904490d491e0688f34a.json)

## Before a recorded user message

24 recorded events

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
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
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
  "uuid": "babcec7e-25b0-41f9-992d-455d3e81b989",
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
    "resetsAt": 1778886600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b868f8ab-bc76-48cf-863b-15629cce686b",
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me first read the latex-paper skill as instructed, then write the abstract.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "9cdb5a41-cdf9-478b-bcc0-f6431dcf12fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzwucrHjSCNuTWY66mEHgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12074,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12074
      },
      "output_tokens": 58,
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

<details open><summary>🔧 Tool call — Read · `toolu_01WqTqBa9PH3ra6x7PPSP39L`</summary>

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
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "c529eff6-eadc-4cbe-9148-34c0777869ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzwucrHjSCNuTWY66mEHgA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12074,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12074
      },
      "output_tokens": 58,
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

_source line 6 · 2026-05-15T20:24:28.788Z_

<details><summary>↩ Tool result · `toolu_01WqTqBa9PH3ra6x7PPSP39L`</summary>

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
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "57a32f4d-2713-421a-b123-6809d67c6b59",
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

### Assistant

_source line 7_

Now let me check the current state of the artifacts directory and any existing abstract.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "1d6ad2cf-5e9d-4aaf-888e-e93514afbaf4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpT89nuiwpb2DYJoqtqdLg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5549,
      "cache_read_input_tokens": 23915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5549
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

_source line 8_

<details open><summary>🔧 Tool call — Bash · `toolu_01QkJK1fefE3KNfxrh7qg7hV`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
  "description": "Check if paper directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "54011cf9-5e90-49c7-8b12-27563ecdd488",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FpT89nuiwpb2DYJoqtqdLg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5549,
      "cache_read_input_tokens": 23915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5549
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

_source line 9 · 2026-05-15T20:24:34.063Z_

<details><summary>↩ Tool result · `toolu_01QkJK1fefE3KNfxrh7qg7hV`</summary>

```text
total 196
drwxr-xr-x 3 ubuntu ubuntu  4096 May 15 20:22 .
drwxr-xr-x 7 ubuntu ubuntu  4096 May 15 13:59 ..
-rw-r--r-- 1 ubuntu ubuntu 11061 May 15 18:59 corl_paper_outline.md
-rw-r--r-- 1 ubuntu ubuntu 13669 May 15 19:27 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu 13333 May 15 19:24 experiments_ac6246.tex
-rw-r--r-- 1 ubuntu ubuntu 12214 May 13 21:57 experiments_c64a8c.tex
-rw-r--r-- 1 ubuntu ubuntu  6352 May 13 21:54 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  6344 May 13 21:47 introduction_c83872.tex
-rw-r--r-- 1 ubuntu ubuntu  7446 May 15 20:22 introduction_scenarioC.tex
-rw-r--r-- 1 ubuntu ubuntu  7397 May 15 19:50 introduction_scenarioC_607d8d.tex
-rw-r--r-- 1 ubuntu ubuntu 10449 May 15 20:18 method.tex
-rw-r--r-- 1 ubuntu ubuntu 10229 May 15 19:14 method_fb526b.tex
-rw-r--r-- 1 ubuntu ubuntu 16004 May 13 21:54 method_section_draft.tex
-rw-r--r-- 1 ubuntu ubuntu 15177 May 15 19:56 references.bib
-rw-r--r-- 1 ubuntu ubuntu 11296 May 13 16:58 references_e9d4d2.bib
-rw-r--r-- 1 ubuntu ubuntu  8827 May 15 20:22 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  8094 May 15 19:36 related_work_80791f.tex
-rw-r--r-- 1 ubuntu ubuntu  6382 May 13 17:37 related_work_9c2927.tex
drwxr-xr-x 2 ubuntu ubuntu  4096 May 15 20:22 sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "bead63c5-eb1b-434e-92a4-f19201b7ae40",
  "tool_use_result": {
    "stdout": "total 196\ndrwxr-xr-x 3 ubuntu ubuntu  4096 May 15 20:22 .\ndrwxr-xr-x 7 ubuntu ubuntu  4096 May 15 13:59 ..\n-rw-r--r-- 1 ubuntu ubuntu 11061 May 15 18:59 corl_paper_outline.md\n-rw-r--r-- 1 ubuntu ubuntu 13669 May 15 19:27 experiments.tex\n-rw-r--r-- 1 ubuntu ubuntu 13333 May 15 19:24 experiments_ac6246.tex\n-rw-r--r-- 1 ubuntu ubuntu 12214 May 13 21:57 experiments_c64a8c.tex\n-rw-r--r-- 1 ubuntu ubuntu  6352 May 13 21:54 introduction.tex\n-rw-r--r-- 1 ubuntu ubuntu  6344 May 13 21:47 introduction_c83872.tex\n-rw-r--r-- 1 ubuntu ubuntu  7446 May 15 20:22 introduction_scenarioC.tex\n-rw-r--r-- 1 ubuntu ubuntu  7397 May 15 19:50 introduction_scenarioC_607d8d.tex\n-rw-r--r-- 1 ubuntu ubuntu 10449 May 15 20:18 method.tex\n-rw-r--r-- 1 ubuntu ubuntu 10229 May 15 19:14 method_fb526b.tex\n-rw-r--r-- 1 ubuntu ubuntu 16004 May 13 21:54 method_section_draft.tex\n-rw-r--r-- 1 ubuntu ubuntu 15177 May 15 19:56 references.bib\n-rw-r--r-- 1 ubuntu ubuntu 11296 May 13 16:58 references_e9d4d2.bib\n-rw-r--r-- 1 ubuntu ubuntu  8827 May 15 20:22 related_work.tex\n-rw-r--r-- 1 ubuntu ubuntu  8094 May 15 19:36 related_work_80791f.tex\n-rw-r--r-- 1 ubuntu ubuntu  6382 May 13 17:37 related_work_9c2927.tex\ndrwxr-xr-x 2 ubuntu ubuntu  4096 May 15 20:22 sections",
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

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01TDiEN5mCnyL5eFm2qsv6f5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
  "limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "fd2258cc-562e-42dd-a9c3-299799786cc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLj5XBqi75v1nATCoyJ56P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 775,
      "cache_read_input_tokens": 29464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 775
      },
      "output_tokens": 71,
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

_source line 11 · 2026-05-15T20:24:37.073Z_

<details><summary>↩ Tool result · `toolu_01TDiEN5mCnyL5eFm2qsv6f5`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	% Para 1: Problem — VLAs degrade under distribution shift; existing solutions have trade-offs
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla} achieve 97--99\% success on standard manipulation benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\cite{fei2025liberoplus}.
7	Two families of methods address this robustness gap.
8	\emph{Training-time methods}~\cite{robustvla2025,srpo2025,digflow2025} improve the base policy through robustness-aware objectives, but require retraining and remain bounded by the training distribution.
9	\emph{Inference-time methods} leave the policy frozen and intervene at deployment.
10	ReconVLA~\cite{chen2026reconvla} draws multiple action samples and selects the best one via conformal scoring---a pure \emph{sample selection} strategy that cannot produce actions better than the best candidate.
11	SC-VLA~\cite{sc_vla_2026} learns a residual correction via reinforcement learning, requiring per-task environment interaction.
12	VLA-Pilot~\cite{vla_pilot_2025} steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41\,s per control step.
13	A2C2~\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.
14	In short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.
15	
16	% Para 2: Gap — sample selection is limited; learned correction can go beyond, but what conditioning?
17	The fundamental limitation of sample selection is that it is bounded by the quality of the available candidates: when all $K$ samples are poor, selecting the best one still yields a poor action.
18	Learned correction can synthesize actions beyond the support of the original samples, potentially recovering from systematic biases in the base policy.
19	However, a critical open question is what information the correction module should be conditioned on.
20	An intuitive hypothesis is that \emph{structured uncertainty features}---per-degree-of-freedom conformal statistics capturing which action dimensions are uncertain and by how much---should enable more targeted corrections than raw observation features alone.
21	We test this hypothesis systematically.
22	
23	% Para 3: Our approach — ACR-VLA pipeline overview
24	We introduce \textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that wraps any frozen flow-matching VLA and performs learned residual action correction.
25	ACR-VLA operates as a \emph{sample-then-correct} pipeline:
26	(i)~draw $K{=}10$ action samples via independent flow-matching rollouts;
27	(ii)~score each sample using Mahalanobis nonconformity under a Ledoit--Wolf shrinkage covariance~\cite{braun2025cgs} and select the lowest-scoring candidate;
28	(iii)~apply a lightweight Conformal Residual Module (CRM)---a 3-layer MLP (${\sim}$329K parameters) that takes the frozen VLA's observation embedding as input and outputs a bounded residual correction.
29	The corrected action is $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta}, \|\boldsymbol{\delta}\|_2 \leq \varepsilon)$, where the norm bound $\varepsilon$ constrains how far the correction can deviate from the selected action.
30	CRM is trained offline via $L_2$ regression on demonstration data; the base VLA is never modified.
31	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA, and evaluate on two LIBERO task suites~\cite{liu2023libero}.
32	
33	% Para 4: Key findings — what we find, including negatives
34	Our experiments yield three findings.
35	\emph{First}, sample-then-correct outperforms sample-then-select: on LIBERO-Object (10 tasks with novel object instances), observation-conditioned CRM achieves 19.0\% success versus 12.0\% for conformal selection alone, a +7.0\,pp improvement.
36	Three baselines---single-sample VLA, 10-sample mean, and argmin selection---all plateau at 12.0\%, indicating that neither averaging nor selection breaks through on this benchmark.
37	\emph{Second}, per-DOF conformal features as CRM conditioning are an \emph{honest negative result}: the perdof variant (11.0\%) performs comparably to argmin selection (12.0\%) and far below observation-only conditioning (19.0\%).
38	This contradicts the intuition that richer uncertainty features should yield better corrections.
39	We attribute this to noisy covariance estimation at the $K{=}10$ sample budget ($d/K = 0.6$): while shrinkage stabilizes selection scoring, the per-DOF statistics derived from it carry estimation noise that degrades CRM predictions under the compounding distribution shift of closed-loop evaluation~\cite{ross2011dagger}.
40	\emph{Third}, correction magnitude control is critical and has not been systematically studied in prior residual policy work~\cite{silver2018residual,jiang2024transic,xiao2026pld}: without clipping ($\|\boldsymbol{\delta}\|_2 \approx 1.42$), CRM achieves 0\% success---compounding error destroys the trajectory entirely.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "79a34d6e-aef7-4147-9da9-8b603c9157f8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% Para 1: Problem — VLAs degrade under distribution shift; existing solutions have trade-offs\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla} achieve 97--99\\% success on standard manipulation benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\\cite{fei2025liberoplus}.\nTwo families of methods address this robustness gap.\n\\emph{Training-time methods}~\\cite{robustvla2025,srpo2025,digflow2025} improve the base policy through robustness-aware objectives, but require retraining and remain bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen and intervene at deployment.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the best one via conformal scoring---a pure \\emph{sample selection} strategy that cannot produce actions better than the best candidate.\nSC-VLA~\\cite{sc_vla_2026} learns a residual correction via reinforcement learning, requiring per-task environment interaction.\nVLA-Pilot~\\cite{vla_pilot_2025} steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41\\,s per control step.\nA2C2~\\cite{a2c2_2025} learns a per-step correction head for pre-generated action chunks on a frozen VLA, but applies correction unconditionally without multi-sample selection or explicit magnitude control.\nIn short, no existing inference-time method combines multi-sample conformal selection with bounded residual correction in a two-stage pipeline.\n\n% Para 2: Gap — sample selection is limited; learned correction can go beyond, but what conditioning?\nThe fundamental limitation of sample selection is that it is bounded by the quality of the available candidates: when all $K$ samples are poor, selecting the best one still yields a poor action.\nLearned correction can synthesize actions beyond the support of the original samples, potentially recovering from systematic biases in the base policy.\nHowever, a critical open question is what information the correction module should be conditioned on.\nAn intuitive hypothesis is that \\emph{structured uncertainty features}---per-degree-of-freedom conformal statistics capturing which action dimensions are uncertain and by how much---should enable more targeted corrections than raw observation features alone.\nWe test this hypothesis systematically.\n\n% Para 3: Our approach — ACR-VLA pipeline overview\nWe introduce \\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that wraps any frozen flow-matching VLA and performs learned residual action correction.\nACR-VLA operates as a \\emph{sample-then-correct} pipeline:\n(i)~draw $K{=}10$ action samples via independent flow-matching rollouts;\n(ii)~score each sample using Mahalanobis nonconformity under a Ledoit--Wolf shrinkage covariance~\\cite{braun2025cgs} and select the lowest-scoring candidate;\n(iii)~apply a lightweight Conformal Residual Module (CRM)---a 3-layer MLP (${\\sim}$329K parameters) that takes the frozen VLA's observation embedding as input and outputs a bounded residual correction.\nThe corrected action is $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta}, \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon)$, where the norm bound $\\varepsilon$ constrains how far the correction can deviate from the selected action.\nCRM is trained offline via $L_2$ regression on demonstration data; the base VLA is never modified.\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA, and evaluate on two LIBERO task suites~\\cite{liu2023libero}.\n\n% Para 4: Key findings — what we find, including negatives\nOur experiments yield three findings.\n\\emph{First}, sample-then-correct outperforms sample-then-select: on LIBERO-Object (10 tasks with novel object instances), observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for conformal selection alone, a +7.0\\,pp improvement.\nThree baselines---single-sample VLA, 10-sample mean, and argmin selection---all plateau at 12.0\\%, indicating that neither averaging nor selection breaks through on this benchmark.\n\\emph{Second}, per-DOF conformal features as CRM conditioning are an \\emph{honest negative result}: the perdof variant (11.0\\%) performs comparably to argmin selection (12.0\\%) and far below observation-only conditioning (19.0\\%).\nThis contradicts the intuition that richer uncertainty features should yield better corrections.\nWe attribute this to noisy covariance estimation at the $K{=}10$ sample budget ($d/K = 0.6$): while shrinkage stabilizes selection scoring, the per-DOF statistics derived from it carry estimation noise that degrades CRM predictions under the compounding distribution shift of closed-loop evaluation~\\cite{ross2011dagger}.\n\\emph{Third}, correction magnitude control is critical and has not been systematically studied in prior residual policy work~\\cite{silver2018residual,jiang2024transic,xiao2026pld}: without clipping ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$), CRM achieves 0\\% success---compounding error destroys the trajectory entirely.",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
I have enough context now. Let me draft the abstract following the constraints:

- Strictly under 200 words
- CoRL 2026 format
- High-level language, don't copy contribution list
- Highlight: inference-time refinement, no VLA retraining, empirical gains on LIBERO
- No "first", "novel", "state-of-the-art", "significantly"
- No MetaWorld
- Only LIBERO-Object and LIBERO-Spatial data
- 4 sentences structure as outlined
- Pure text, no \begin{abstract} tags


- Two-stage pipeline: sample K actions, select via Mahalanobis confidence, refine with diffusion

Now I'm drafting the opening sentences to establish the problem—flow-matching VLAs work well on standard benchmarks but fail dramatically under distribution shift, with performance dropping over 65 points on LIBERO-Plus. Then I'll introduce the approach: a frozen inference-time wrapper that samples multiple actions, uses Mahalanobis distance for selection, and applies diffusion-based refinement without any retraining.

Let me continue with the experimental results. The Conformal Residual Module achieves meaningful gains on LIBERO-Object—19% success with correction versus 12% for selection alone, a 58% relative improvement. Per-DOF features didn't help, which I'm attributing to noisy covariance estimates at small sample sizes. Magnitude control is essential since unbounded corrections completely fail. On LIBERO-Spatial the gains are smaller, suggesting the benefit varies by task. The sample-then-correct approach outperforms selection-only in most cases. then-select for object manipulation, but whether correction helps depends on the structure of the distribution shift. Flow-matching vision-language-action models achieve high success rates on standard manipulation benchmarks but degrade sharply under distribution shift — dropping over 65 percentage points on LIBERO-Plus perturbations. Existing inference-time approaches either select among multiple action samples, which can't exceed the quality of the best candidate, or learn corrections through reinforcement learning or slow optimization loops. I'm proposing ACR-VLA, an inference-time two-stage pipeline that wraps a frozen flow-matching VLA without retraining — it draws K=10 action samples and selects one via Mahalanobis-based conformal scoring, then applies a lightweight Conformal Residual Module with about 329K parameters and 3ms overhead to refine the action. On LIBERO-Object, the observation-conditioned correction achieves 19.0% success versus 12.0% for selection alone, a 7 percentage point gain or 58% relative improvement. Per-degree-of-freedom conformal features don't improve over scalar baselines though.

I'm noticing that per-DOF features actually perform worse at 11.0% versus 9.0%, which I think comes down to noisy covariance estimation when the sample budget is small. Magnitude control turns out to be critical here—unbounded correction completely fails at 0% success. On LIBERO-Spatial, correction and selection perform similarly within 1 percentage point, so the benefit really depends on the task structure.

The pattern emerging is that sample-then-correct works better for object manipulation, but whether correction actually helps hinges on how the distribution shift is structured.

Now I'm refining the abstract to avoid certain language constraints—removing "first" even when it's just used for sequencing, and checking that I haven't used "novel," "state-of-the-art," or "significantly." The draft is coming together under 200 words, and I'm revising the opening to describe ACR-VLA as a two-stage inference pipeline that works with frozen flow-matching VLAs without requiring retraining.

The method samples K=10 actions, scores them using Mahalanobis-based conformal scoring, then applies bounded residual corrections through a lightweight module. Results show strong gains on LIBERO-Object—19.0% success with correction versus 12.0% for selection alone—but per-degree-of-freedom conformal features underperform scalar baselines, which I'm attributing to noisy covariance estimation at small sample sizes. Magnitude control is essential since unbounded correction fails entirely. On LIBERO-Spatial, the benefits are more modest and task-dependent, suggesting the approach works best for object manipulation under certain distribution shifts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "a9712ec3-0d8d-4da5-bbf9-5a6760aeccfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TinuVn4qYyexXoNAhpQLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1604,
      "cache_read_input_tokens": 30239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1604
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

_source line 13_

<details open><summary>🔧 Tool call — Write · `toolu_01Xw5mS6eJdAADpi6EgZnmYs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract.tex",
  "content": "Flow-matching vision-language-action models (VLAs) achieve high success rates on standard manipulation benchmarks but degrade sharply under distribution shift---dropping over 65 percentage points on LIBERO-Plus perturbations.\nExisting inference-time remedies either select among multiple action samples, which cannot exceed the quality of the best candidate, or learn corrections through reinforcement learning or slow optimization loops.\n%\nWe propose ACR-VLA, an inference-time two-stage pipeline that wraps a frozen flow-matching VLA without retraining.\nAt each control step, ACR-VLA draws $K{=}10$ action samples, selects one via Mahalanobis-based conformal scoring, and applies a bounded residual correction through a lightweight Conformal Residual Module (CRM, ${\\sim}$329K parameters, ${\\sim}$3\\,ms overhead).\n%\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for selection alone (+7.0\\,pp, 58\\% relative gain).\nPer-degree-of-freedom conformal features do not improve over scalar baselines (11.0\\% vs.\\ 9.0\\%), an honest negative we attribute to noisy covariance estimation at small sample budgets.\nMagnitude control proves critical: unbounded correction leads to 0\\% success.\nOn LIBERO-Spatial, correction and selection perform comparably (${\\pm}$1\\,pp), indicating the benefit is task-dependent.\n%\nSample-then-correct outperforms sample-then-select for object manipulation, but whether correction helps depends on the structure of the distribution shift.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "708ee61f-be72-4a44-af25-1500442ede8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016TinuVn4qYyexXoNAhpQLf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1604,
      "cache_read_input_tokens": 30239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1604
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

_source line 14 · 2026-05-15T20:25:13.139Z_

<details><summary>↩ Tool result · `toolu_01Xw5mS6eJdAADpi6EgZnmYs`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "15904825-12af-4780-9e77-51fc6d234e58",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract.tex",
    "content": "Flow-matching vision-language-action models (VLAs) achieve high success rates on standard manipulation benchmarks but degrade sharply under distribution shift---dropping over 65 percentage points on LIBERO-Plus perturbations.\nExisting inference-time remedies either select among multiple action samples, which cannot exceed the quality of the best candidate, or learn corrections through reinforcement learning or slow optimization loops.\n%\nWe propose ACR-VLA, an inference-time two-stage pipeline that wraps a frozen flow-matching VLA without retraining.\nAt each control step, ACR-VLA draws $K{=}10$ action samples, selects one via Mahalanobis-based conformal scoring, and applies a bounded residual correction through a lightweight Conformal Residual Module (CRM, ${\\sim}$329K parameters, ${\\sim}$3\\,ms overhead).\n%\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for selection alone (+7.0\\,pp, 58\\% relative gain).\nPer-degree-of-freedom conformal features do not improve over scalar baselines (11.0\\% vs.\\ 9.0\\%), an honest negative we attribute to noisy covariance estimation at small sample budgets.\nMagnitude control proves critical: unbounded correction leads to 0\\% success.\nOn LIBERO-Spatial, correction and selection perform comparably (${\\pm}$1\\,pp), indicating the benefit is task-dependent.\n%\nSample-then-correct outperforms sample-then-select for object manipulation, but whether correction helps depends on the structure of the distribution shift.\n",
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

Let me verify the word count.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "d77f6050-c4b3-4904-a495-ab4dc5a00c9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKTwSADDvuoevnQkMRLm9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2718,
      "cache_read_input_tokens": 31843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2718
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Q1UPGm3eUiB5Yzd2cbkmX8`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract.tex | sed 's/%//g' | sed 's/\\\\[a-zA-Z]*{[^}]*}//g; s/\\\\[a-zA-Z]*//g; s/[{}$~]//g; s/---/—/g; s/--/-/g' | wc -w",
  "description": "Count words in abstract (approximate, stripping LaTeX commands)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "227c2b85-44c4-464c-a311-fe4223804d0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKTwSADDvuoevnQkMRLm9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2718,
      "cache_read_input_tokens": 31843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2718
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

_source line 17 · 2026-05-15T20:25:18.379Z_

<details><summary>↩ Tool result · `toolu_01Q1UPGm3eUiB5Yzd2cbkmX8`</summary>

```text
182
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "d7a62c3d-f4d5-497a-831e-ef5c85799fb2",
  "tool_use_result": {
    "stdout": "182",
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

_source line 18_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "2791c97f-3d32-4810-a6c5-bd027ee3710f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GoMXxJcAL1v1QoF15R4LK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 217,
      "cache_read_input_tokens": 34561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 217
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

_source line 19_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LP28XYAWs1ZR3RwMZdR2oC`</summary>

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
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "d39432e8-7046-4944-ae6d-ec4d172ba732",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012GoMXxJcAL1v1QoF15R4LK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 217,
      "cache_read_input_tokens": 34561,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 217
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

_source line 20 · 2026-05-15T20:25:21.493Z_

<details><summary>↩ Tool result · `toolu_01LP28XYAWs1ZR3RwMZdR2oC`</summary>

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
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "cd6aa2e3-57cb-4952-a96d-d4c4205aa596",
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

_source line 21_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01RVqQHqgCuMgewF7RPbxiyd`</summary>

```json
{
  "name": "ACR-VLA Abstract (CoRL 2026)",
  "type": "paper",
  "description": "Abstract for ACR-VLA paper, 182 words, CoRL 2026 format. Covers problem (VLA degradation under shift), method (two-stage sample-then-correct pipeline), results (LIBERO-Object/Spatial), and honest negatives.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract.tex",
  "tags": [
    "abstract",
    "corl2026",
    "paper"
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
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "421469ea-562f-4de6-806f-ecfd896a9450",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A8UocH29u1x5Tut4FeBpji",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 718,
      "cache_read_input_tokens": 34778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 718
      },
      "output_tokens": 64,
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

_source line 22 · 2026-05-15T20:25:27.190Z_

<details><summary>↩ Tool result · `toolu_01RVqQHqgCuMgewF7RPbxiyd`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_a1674b\", \"name\": \"ACR-VLA Abstract (CoRL 2026)\", \"type\": \"paper\", \"description\": \"Abstract for ACR-VLA paper, 182 words, CoRL 2026 format. Covers problem (VLA degradation under shift), method (two-stage sample-then-correct pipeline), results (LIBERO-Object/Spatial), and honest negatives.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract_a1674b.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T20:25:27.106651+00:00\", \"tags\": [\"abstract\", \"corl2026\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "8a8b2cda-e60d-4348-b1e5-37afc4c2385e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_a1674b\\\", \\\"name\\\": \\\"ACR-VLA Abstract (CoRL 2026)\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Abstract for ACR-VLA paper, 182 words, CoRL 2026 format. Covers problem (VLA degradation under shift), method (two-stage sample-then-correct pipeline), results (LIBERO-Object/Spatial), and honest negatives.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract_a1674b.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T20:25:27.106651+00:00\\\", \\\"tags\\\": [\\\"abstract\\\", \\\"corl2026\\\", \\\"paper\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_a1674b\", \"name\": \"ACR-VLA Abstract (CoRL 2026)\", \"type\": \"paper\", \"description\": \"Abstract for ACR-VLA paper, 182 words, CoRL 2026 format. Covers problem (VLA degradation under shift), method (two-stage sample-then-correct pipeline), results (LIBERO-Object/Spatial), and honest negatives.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract_a1674b.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T20:25:27.106651+00:00\", \"tags\": [\"abstract\", \"corl2026\", \"paper\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

已写入 `artifacts/_project/paper/abstract.tex`，182 词，符合 CoRL 200 词限制。

结构：
1. **问题**（2 句）：VLA 在分布偏移下退化 >65pp，现有方法受限于 selection 上界或需要 RL
2. **方法**（2 句）：ACR-VLA 两阶段 pipeline，frozen VLA + CRM 329K params / 3ms
3. **结果**（4 句）：Object +7.0pp，per-DOF negative，unbounded → 0%，Spatial null result
4. **Takeaway**（1 句）：correction benefit is task-dependent

无 "first"/"novel"/"state-of-the-art"/"significantly"，无 MetaWorld。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "uuid": "7acf890a-9ec7-45d9-b3f5-d30f61e4da03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8LjCde5ZJ4x8TqWTmfgCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 35496,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 713
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

_source line 24_

已写入 `artifacts/_project/paper/abstract.tex`，182 词，符合 CoRL 200 词限制。

结构：
1. **问题**（2 句）：VLA 在分布偏移下退化 >65pp，现有方法受限于 selection 上界或需要 RL
2. **方法**（2 句）：ACR-VLA 两阶段 pipeline，frozen VLA + CRM 329K params / 3ms
3. **结果**（4 句）：Object +7.0pp，per-DOF negative，unbounded → 0%，Spatial null result
4. **Takeaway**（1 句）：correction benefit is task-dependent

无 "first"/"novel"/"state-of-the-art"/"significantly"，无 MetaWorld。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 68512,
  "duration_api_ms": 69049,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "93cd08c6-375b-4693-ab9b-8acc7fb01a6b",
  "total_cost_usd": 0.36550649999999996,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 24368,
    "cache_read_input_tokens": 232137,
    "output_tokens": 3820,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24368,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 212,
        "cache_read_input_tokens": 35496,
        "cache_creation_input_tokens": 713,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 713
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1488,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001583,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 3820,
      "cacheReadInputTokens": 232137,
      "cacheCreationInputTokens": 24368,
      "webSearchRequests": 0,
      "costUSD": 0.36392349999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "931b70f6-adb7-4d9a-8189-7295dff01019"
}
```

</details>

---
