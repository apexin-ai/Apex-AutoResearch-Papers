# paper writing discussion conclusion

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_writing_discussion_conclusion_20260515T203818.log`
- **Structured JSON:** [`bc5b6f6fdd8483f52ed1.json`](../../sessions/bc/bc5b6f6fdd8483f52ed1.json)

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
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
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
  "uuid": "d335299d-736d-4d63-b642-e4f9fdc8aeba",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
  "uuid": "9ed76806-0fc5-426c-b3a5-7f60e8c26320",
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d"
}
```

---

### Assistant

_source line 4_

I'll read the LaTeX writing conventions first, then write the sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "672cee51-c21f-4735-a493-b35a3d92636e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyEM12MAJKBhzh5q9nSs1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13028
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

<details open><summary>🔧 Tool call — Read · `toolu_01VfV8dwQK6WBTBbLmQXjLXv`</summary>

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
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "556c5fdd-d2d9-4488-b284-4d207d01a5e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyEM12MAJKBhzh5q9nSs1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13028
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

_source line 6 · 2026-05-15T20:38:37.384Z_

<details><summary>↩ Tool result · `toolu_01VfV8dwQK6WBTBbLmQXjLXv`</summary>

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
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "bf4be3a1-af3f-4478-8834-1e1dc51546b1",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01YYAaGAW9d5KNtn4Z47t8Ce`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "db6acc00-3373-4c66-86bd-d2771959c0a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DyEM12MAJKBhzh5q9nSs1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13028
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

_source line 8 · 2026-05-15T20:38:38.736Z_

<details><summary>↩ Tool result · `toolu_01YYAaGAW9d5KNtn4Z47t8Ce`</summary>

```text
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/experiments_ac6246.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/abstract_a1674b.tex
artifacts/_project/paper/sections/introduction.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/introduction_scenarioC_607d8d.tex
artifacts/_project/paper/introduction_scenarioC.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/related_work_80791f.tex
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "a3a15162-8991-4c74-90ea-00d2e5bf0451",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/method_section_draft.tex",
      "artifacts/_project/paper/experiments_ac6246.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/abstract_a1674b.tex",
      "artifacts/_project/paper/sections/introduction.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/introduction_c83872.tex",
      "artifacts/_project/paper/introduction_scenarioC_607d8d.tex",
      "artifacts/_project/paper/introduction_scenarioC.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/related_work_9c2927.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/related_work_80791f.tex",
      "artifacts/_project/paper/method_fb526b.tex",
      "artifacts/_project/paper/experiments_c64a8c.tex",
      "artifacts/_project/paper/abstract.tex"
    ],
    "durationMs": 7,
    "numFiles": 16,
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
Let me check the existing paper sections for style consistency, particularly the experiments section since the discussion will reference it heavily.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "fc588f84-59b4-4b0a-ba41-a319af23a9b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuKnEuYgyQ1SBxNrqrzbbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5887,
      "cache_read_input_tokens": 24869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5887
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

Let me check the existing sections for style consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "99ec81f8-99fa-4665-be99-7a64ca2e1e9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuKnEuYgyQ1SBxNrqrzbbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5887,
      "cache_read_input_tokens": 24869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5887
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

<details open><summary>🔧 Tool call — Read · `toolu_011CXuzQg8fC4k8oXJGBnDgb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "89169a6a-a2fa-4e88-85ee-e9ae1191ef47",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuKnEuYgyQ1SBxNrqrzbbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5887,
      "cache_read_input_tokens": 24869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5887
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

_source line 12 · 2026-05-15T20:38:44.025Z_

<details><summary>↩ Tool result · `toolu_011CXuzQg8fC4k8oXJGBnDgb`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction improve over conformal selection alone?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+7.0\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\_only is robust across a wide range.
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
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\ref{sec:selection}), no CRM correction.
30	\end{itemize}
31	
32	\paragraph{CRM variants.}
33	All CRM variants share the same 3-layer MLP architecture (input$\to$256$\to$256$\to$30) and differ only in their conditioning input:
34	\begin{itemize}[nosep]
35	  \item \textbf{obs\_only}: frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ (329K params). This is our primary method.
36	  \item \textbf{perdof}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).
37	  \item \textbf{scalar}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).
38	\end{itemize}
39	
40	\paragraph{Training.}
41	CRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.
42	For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\mathrm{base}}$.
43	Optimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.
44	Data augmentation includes additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and uncertainty features ($\sigma \approx 0.006$).
45	The default magnitude bound is $\varepsilon = 0.1$ for all CRM variants unless stated otherwise.
46	
47	\paragraph{Statistical protocol.}
48	We report success rates from seed 42 (10 rollouts $\times$ 10 tasks = 100 episodes per suite).
49	Fisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\textsc{pending}: seed43].
50	Until then, we report absolute differences descriptively without claiming statistical significance.
51	
52	
53	\subsection{Main Results}
54	\label{sec:main_results}
55	
56	Table~\ref{tab:main} compares all methods on both benchmarks.
57	
58	\begin{table}[t]
59	\centering
60	\caption{Task success rate (\%\,$\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\times$ 10 rollouts each, seed 42). $\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}
61	\label{tab:main}
62	\small
63	\begin{tabular}{lccc}
64	\toprule
65	Method & Object (\%) & Spatial (\%) & $\Delta$ Object \\
66	\midrule
67	VLA-only ($K{=}1$)    & 12.0 & 30.0 & $\phantom{+}0.0$ \\
68	VLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\phantom{+}0.0$ \\
69	Argmin ($K{=}10$)      & 12.0 & 34.0 & --- \\
70	\midrule
71	scalar ($\varepsilon{=}0.1$)  & \phantom{0}9.0 & 32.0 & $-3.0$ \\
72	perdof ($\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\
73	\textbf{obs\_only} ($\varepsilon{=}0.1$) & \textbf{19.0} & \textbf{35.0} & $\mathbf{+7.0}$ \\
74	\midrule
75	obs\_only ($\varepsilon{=}0.2$) & \textbf{22.0} & 35.0 & $+10.0$ \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	\paragraph{Object benchmark: correction helps.}
81	On LIBERO-Object, obs\_only at $\varepsilon{=}0.1$ achieves 19.0\%, a +7.0\,pp improvement over the Argmin baseline (12.0\%).
82	Increasing the magnitude bound to $\varepsilon{=}0.2$ yields 22.0\% (+10.0\,pp).
83	This is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.
84	
85	Three baselines---VLA-only, VLA-mean, and Argmin---all achieve 12.0\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.
86	On LIBERO-Spatial, by contrast, Argmin improves +4\,pp over VLA-only (34\% vs.\ 30\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.
87	The obs\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.
88	
89	\paragraph{Spatial benchmark: correction does not help.}
90	On LIBERO-Spatial, all methods cluster within a 5\,pp band (30--35\%).
91	The best CRM variants (obs\_only, perdof) achieve 35\%, only 1\,pp above the Argmin baseline (34\%).
92	This is a null result that we report prominently.
93	
94	We interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.
95	The VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.
96	Residual correction at the action level is the wrong granularity for this type of generalization.
97	
98	\paragraph{Key finding.}
99	Sample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.
100	For spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.
101	
102	
103	\subsection{CRM Conditioning Ablation}
104	\label{sec:ablation}
105	
106	We focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\ref{tab:main}).
107	
108	\paragraph{Ranking.}
109	obs\_only (19.0\%) $\gg$ Argmin (12.0\%) $\approx$ perdof (11.0\%) $>$ scalar (9.0\%).
110	
111	This ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \emph{hurt} rather than help.
112	Scalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\,pp below the Argmin baseline that uses no correction at all.
113	
114	\paragraph{Why does richer conditioning fail?}
115	We identify three factors:
116	
117	\emph{(1) Noisy covariance estimation.}
118	With $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.
119	While Ledoit--Wolf shrinkage~\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.
120	Feeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).
121	
122	\emph{(2) Observation features are sufficient.}
123	The frozen VLA observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.
124	This information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.
125	The CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.
126	
127	\emph{(3) Per-step MSE $\neq$ episode success.}
128	In offline evaluation, per-DOF conformal features reduce the per-step mean squared error between corrected actions and expert demonstrations.
129	However, this per-step improvement does not translate to higher episode success rates in closed-loop evaluation, where small per-step errors compound and the robot visits states far from the demonstration distribution~\cite{ross2011dagger}.
130	The additional noise from conformal features may cause occasional large corrections that, while reducing average MSE, lead to catastrophic failures in individual episodes.
131	
132	\paragraph{Connection to magnitude sensitivity.}
133	The obs\_only variant is also more robust across magnitude bounds $\varepsilon$ than perdof (Section~\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.
134	
135	
136	\subsection{Magnitude Sensitivity}
137	\label{sec:magnitude_results}
138	
139	The norm bound $\varepsilon$ determines how much CRM can deviate from the conformal-selected action.
140	Figure~\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\varepsilon \in [0.05, 1.42]$.
141	
142	\begin{figure}[t]
143	\centering
144	% \includegraphics[width=\linewidth]{figures/magnitude_sweep.pdf}
145	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}[Placeholder: Magnitude sweep --- obs\_only vs.\ perdof vs.\ Argmin reference]\vspace{2em}}}
146	\caption{Success rate (\%) on LIBERO-Spatial as a function of magnitude bound $\varepsilon$. obs\_only (solid blue) maintains 35--36\% across $\varepsilon \in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\varepsilon$. The Argmin baseline (dotted gray, 34\%) is independent of $\varepsilon$. Without magnitude control ($\varepsilon{\approx}1.42$), perdof achieves 0\% on spatial.}
147	\label{fig:magnitude}
148	\end{figure}
149	
150	\begin{table}[t]
151	\centering
152	\caption{Success rate (\%) on LIBERO-Spatial across magnitude bounds $\varepsilon$. The Argmin baseline (34\%, no correction) is independent of $\varepsilon$.}
153	\label{tab:magnitude}
154	\small
155	\begin{tabular}{lcccc}
156	\toprule
157	$\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\
158	\midrule
159	obs\_only & 35.0 & 35.0 & 36.0 & --- \\
160	perdof    & 31.0 & 35.0 & 26.0 & 0.0 \\
161	\midrule
162	Argmin (ref.) & \multicolumn{4}{c}{34.0 (flat, no correction)} \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\paragraph{obs\_only is robust.}
168	The obs\_only variant maintains 35--36\% across the full range $\varepsilon \in [0.05, 0.3]$---a remarkably flat profile.
169	This stability means the practitioner need not carefully tune $\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.
170	
171	\paragraph{perdof is fragile.}
172	In contrast, perdof peaks at 35\% when $\varepsilon{=}0.1$ but collapses to 26\% at $\varepsilon{=}0.3$---a 9\,pp drop.
173	This fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.
174	At $\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.
175	
176	\paragraph{Unbounded correction is catastrophic.}
177	Without magnitude control ($\varepsilon{\approx}1.42$, the natural CRM output norm), perdof achieves 0\% on LIBERO-Spatial---compounding error across the trajectory destroys performance entirely (Section~\ref{sec:magnitude}).
178	The Argmin baseline (34\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.
179	The obs\_only variant was not evaluated at $\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.
180	
181	\paragraph{Practical recommendation.}
182	The safe operating range is $\varepsilon \in [0.05, 0.2]$.
183	Within this range, obs\_only is the only variant that consistently matches or exceeds the Argmin baseline.
184	We use $\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.
185	
186	
187	\subsection{Per-Task Analysis}
188	\label{sec:per_task}
189	
190	Per-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.
191	
192	[\textsc{pending}: seed43] --- A per-task heatmap comparing obs\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.
193	We expect the analysis to show that obs\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.
194	Task difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).
195	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "413182c8-2105-4b3c-8247-331465c2e4b2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to answer three questions:\n(i)~Does observation-conditioned residual correction improve over conformal selection alone?\n(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?\n(iii)~How sensitive is performance to the magnitude bound $\\varepsilon$?\nThe answers are: yes (+7.0\\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\\_only is robust across a wide range.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\nWe use the checkpoint \\texttt{lerobot/smolvla\\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.\n\n\\paragraph{Baselines.}\nAll methods use the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.\n  \\item \\textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\\ref{sec:selection}), no CRM correction.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nAll CRM variants share the same 3-layer MLP architecture (input$\\to$256$\\to$256$\\to$30) and differ only in their conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ (329K params). This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).\n\\end{itemize}\n\n\\paragraph{Training.}\nCRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.\nFor each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\\mathrm{base}}$.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.\nData augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$).\nThe default magnitude bound is $\\varepsilon = 0.1$ for all CRM variants unless stated otherwise.\n\n\\paragraph{Statistical protocol.}\nWe report success rates from seed 42 (10 rollouts $\\times$ 10 tasks = 100 episodes per suite).\nFisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\\textsc{pending}: seed43].\nUntil then, we report absolute differences descriptively without claiming statistical significance.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares all methods on both benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\\times$ 10 rollouts each, seed 42). $\\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Object (\\%) & Spatial (\\%) & $\\Delta$ Object \\\\\n\\midrule\nVLA-only ($K{=}1$)    & 12.0 & 30.0 & $\\phantom{+}0.0$ \\\\\nVLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\\phantom{+}0.0$ \\\\\nArgmin ($K{=}10$)      & 12.0 & 34.0 & --- \\\\\n\\midrule\nscalar ($\\varepsilon{=}0.1$)  & \\phantom{0}9.0 & 32.0 & $-3.0$ \\\\\nperdof ($\\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\\\\n\\textbf{obs\\_only} ($\\varepsilon{=}0.1$) & \\textbf{19.0} & \\textbf{35.0} & $\\mathbf{+7.0}$ \\\\\n\\midrule\nobs\\_only ($\\varepsilon{=}0.2$) & \\textbf{22.0} & 35.0 & $+10.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Object benchmark: correction helps.}\nOn LIBERO-Object, obs\\_only at $\\varepsilon{=}0.1$ achieves 19.0\\%, a +7.0\\,pp improvement over the Argmin baseline (12.0\\%).\nIncreasing the magnitude bound to $\\varepsilon{=}0.2$ yields 22.0\\% (+10.0\\,pp).\nThis is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.\n\nThree baselines---VLA-only, VLA-mean, and Argmin---all achieve 12.0\\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.\nOn LIBERO-Spatial, by contrast, Argmin improves +4\\,pp over VLA-only (34\\% vs.\\ 30\\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.\nThe obs\\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.\n\n\\paragraph{Spatial benchmark: correction does not help.}\nOn LIBERO-Spatial, all methods cluster within a 5\\,pp band (30--35\\%).\nThe best CRM variants (obs\\_only, perdof) achieve 35\\%, only 1\\,pp above the Argmin baseline (34\\%).\nThis is a null result that we report prominently.\n\nWe interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.\nThe VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.\nResidual correction at the action level is the wrong granularity for this type of generalization.\n\n\\paragraph{Key finding.}\nSample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.\nFor spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.\n\n\n\\subsection{CRM Conditioning Ablation}\n\\label{sec:ablation}\n\nWe focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\\ref{tab:main}).\n\n\\paragraph{Ranking.}\nobs\\_only (19.0\\%) $\\gg$ Argmin (12.0\\%) $\\approx$ perdof (11.0\\%) $>$ scalar (9.0\\%).\n\nThis ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \\emph{hurt} rather than help.\nScalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\\,pp below the Argmin baseline that uses no correction at all.\n\n\\paragraph{Why does richer conditioning fail?}\nWe identify three factors:\n\n\\emph{(1) Noisy covariance estimation.}\nWith $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.\nWhile Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.\nFeeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).\n\n\\emph{(2) Observation features are sufficient.}\nThe frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.\nThis information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.\nThe CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.\n\n\\emph{(3) Per-step MSE $\\neq$ episode success.}\nIn offline evaluation, per-DOF conformal features reduce the per-step mean squared error between corrected actions and expert demonstrations.\nHowever, this per-step improvement does not translate to higher episode success rates in closed-loop evaluation, where small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.\nThe additional noise from conformal features may cause occasional large corrections that, while reducing average MSE, lead to catastrophic failures in individual episodes.\n\n\\paragraph{Connection to magnitude sensitivity.}\nThe obs\\_only variant is also more robust across magnitude bounds $\\varepsilon$ than perdof (Section~\\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.\n\n\n\\subsection{Magnitude Sensitivity}\n\\label{sec:magnitude_results}\n\nThe norm bound $\\varepsilon$ determines how much CRM can deviate from the conformal-selected action.\nFigure~\\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\\varepsilon \\in [0.05, 1.42]$.\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/magnitude_sweep.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: Magnitude sweep --- obs\\_only vs.\\ perdof vs.\\ Argmin reference]\\vspace{2em}}}\n\\caption{Success rate (\\%) on LIBERO-Spatial as a function of magnitude bound $\\varepsilon$. obs\\_only (solid blue) maintains 35--36\\% across $\\varepsilon \\in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\\varepsilon$. The Argmin baseline (dotted gray, 34\\%) is independent of $\\varepsilon$. Without magnitude control ($\\varepsilon{\\approx}1.42$), perdof achieves 0\\% on spatial.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Spatial across magnitude bounds $\\varepsilon$. The Argmin baseline (34\\%, no correction) is independent of $\\varepsilon$.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\\\\n\\midrule\nobs\\_only & 35.0 & 35.0 & 36.0 & --- \\\\\nperdof    & 31.0 & 35.0 & 26.0 & 0.0 \\\\\n\\midrule\nArgmin (ref.) & \\multicolumn{4}{c}{34.0 (flat, no correction)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{obs\\_only is robust.}\nThe obs\\_only variant maintains 35--36\\% across the full range $\\varepsilon \\in [0.05, 0.3]$---a remarkably flat profile.\nThis stability means the practitioner need not carefully tune $\\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.\n\n\\paragraph{perdof is fragile.}\nIn contrast, perdof peaks at 35\\% when $\\varepsilon{=}0.1$ but collapses to 26\\% at $\\varepsilon{=}0.3$---a 9\\,pp drop.\nThis fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.\nAt $\\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.\n\n\\paragraph{Unbounded correction is catastrophic.}\nWithout magnitude control ($\\varepsilon{\\approx}1.42$, the natural CRM output norm), perdof achieves 0\\% on LIBERO-Spatial---compounding error across the trajectory destroys performance entirely (Section~\\ref{sec:magnitude}).\nThe Argmin baseline (34\\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.\nThe obs\\_only variant was not evaluated at $\\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.\n\n\\paragraph{Practical recommendation.}\nThe safe operating range is $\\varepsilon \\in [0.05, 0.2]$.\nWithin this range, obs\\_only is the only variant that consistently matches or exceeds the Argmin baseline.\nWe use $\\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nPer-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.\n\n[\\textsc{pending}: seed43] --- A per-task heatmap comparing obs\\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.\nWe expect the analysis to show that obs\\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.\nTask difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).\n",
      "numLines": 195,
      "startLine": 1,
      "totalLines": 195
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01MSoMmnSZ1Cs5isroNo34zH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "7fd7bcd9-9eb7-4858-96da-4e3651d29e0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuKnEuYgyQ1SBxNrqrzbbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5887,
      "cache_read_input_tokens": 24869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5887
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

_source line 14 · 2026-05-15T20:38:44.401Z_

<details><summary>↩ Tool result · `toolu_01MSoMmnSZ1Cs5isroNo34zH`</summary>

```text
1	Flow-matching vision-language-action models (VLAs) achieve high success rates on standard manipulation benchmarks but degrade sharply under distribution shift---dropping over 65 percentage points on LIBERO-Plus perturbations.
2	Existing inference-time remedies either select among multiple action samples, which cannot exceed the quality of the best candidate, or learn corrections through reinforcement learning or slow optimization loops.
3	%
4	We propose ACR-VLA, an inference-time two-stage pipeline that wraps a frozen flow-matching VLA without retraining.
5	At each control step, ACR-VLA draws $K{=}10$ action samples, selects one via Mahalanobis-based conformal scoring, and applies a bounded residual correction through a lightweight Conformal Residual Module (CRM, ${\sim}$329K parameters, ${\sim}$3\,ms overhead).
6	%
7	On LIBERO-Object, observation-conditioned CRM achieves 19.0\% success versus 12.0\% for selection alone (+7.0\,pp, 58\% relative gain).
8	Conditioning CRM on per-DOF conformal features (11.0\%) or scalar uncertainty (9.0\%) fails to improve over selection alone (12.0\%)---only observation features reach 19.0\%---an honest negative result we attribute to noisy covariance estimation at the $K{=}10$ sample budget.
9	Magnitude control proves critical: unbounded correction leads to 0\% success.
10	On LIBERO-Spatial, correction and selection perform comparably (best CRM within 1\,pp of the selection baseline), indicating the benefit is task-dependent.
11	%
12	Sample-then-correct outperforms sample-then-select for object manipulation, but whether correction helps depends on the structure of the distribution shift.
13	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "99618fd7-5e34-4bd8-a46f-5ad36d2ab284",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/abstract.tex",
      "content": "Flow-matching vision-language-action models (VLAs) achieve high success rates on standard manipulation benchmarks but degrade sharply under distribution shift---dropping over 65 percentage points on LIBERO-Plus perturbations.\nExisting inference-time remedies either select among multiple action samples, which cannot exceed the quality of the best candidate, or learn corrections through reinforcement learning or slow optimization loops.\n%\nWe propose ACR-VLA, an inference-time two-stage pipeline that wraps a frozen flow-matching VLA without retraining.\nAt each control step, ACR-VLA draws $K{=}10$ action samples, selects one via Mahalanobis-based conformal scoring, and applies a bounded residual correction through a lightweight Conformal Residual Module (CRM, ${\\sim}$329K parameters, ${\\sim}$3\\,ms overhead).\n%\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for selection alone (+7.0\\,pp, 58\\% relative gain).\nConditioning CRM on per-DOF conformal features (11.0\\%) or scalar uncertainty (9.0\\%) fails to improve over selection alone (12.0\\%)---only observation features reach 19.0\\%---an honest negative result we attribute to noisy covariance estimation at the $K{=}10$ sample budget.\nMagnitude control proves critical: unbounded correction leads to 0\\% success.\nOn LIBERO-Spatial, correction and selection perform comparably (best CRM within 1\\,pp of the selection baseline), indicating the benefit is task-dependent.\n%\nSample-then-correct outperforms sample-then-select for object manipulation, but whether correction helps depends on the structure of the distribution shift.\n",
      "numLines": 13,
      "startLine": 1,
      "totalLines": 13
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01ERjmJuwoQufPsAezoMdbjJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "2e4010c2-e963-48b9-a26e-e4f8b46cc156",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TuKnEuYgyQ1SBxNrqrzbbu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5887,
      "cache_read_input_tokens": 24869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5887
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

_source line 16 · 2026-05-15T20:38:45.030Z_

<details><summary>↩ Tool result · `toolu_01ERjmJuwoQufPsAezoMdbjJ`</summary>

```text
1	
2	\section{Method}
3	\label{sec:method}
4	
5	\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
6	
7	\subsection{Problem Setup}
8	\label{sec:problem_setup}
9	
10	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.
11	
12	At each control step, $\pi_\theta$ can be queried multiple times via independent flow-matching rollouts~\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\pi_\theta$.
13	
14	\subsection{Multi-Sample Generation and Conformal Selection}
15	\label{sec:selection}
16	
17	\paragraph{Sampling and truncation.}
18	We draw $K{=}10$ action chunks from $\pi_\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\{a_h^{(k)}\}_{k=1}^K$ with $a_h^{(k)} \in \mathbb{R}^d$ for each horizon step $h = 1, \dots, H$.
19	
20	\paragraph{Shrinkage covariance estimation.}
21	For each horizon step $h$, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well}:
22	\begin{equation}
23	  \boldsymbol{\Sigma}_h = (1 - \alpha_{\mathrm{LW}})\,\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}} + \alpha_{\mathrm{LW}}\,\frac{\mathrm{tr}(\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}})}{d}\,\mathbf{I},
24	  \label{eq:shrinkage}
25	\end{equation}
26	where $\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}}$ is the empirical covariance and $\alpha_{\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\% estimation error; shrinkage reduces this to below 5\%~\cite{ledoit2004well}.
27	
28	\paragraph{Mahalanobis nonconformity score.}
29	For each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:
30	\begin{equation}
31	  s_h(a) = (a - \boldsymbol{\mu}_h)^\top \boldsymbol{\Sigma}_h^{-1} (a - \boldsymbol{\mu}_h).
32	  \label{eq:mahal}
33	\end{equation}
34	This score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\cite{braun2025cgs}.
35	
36	\paragraph{Argmin selection.}
37	We select the sample with the lowest total nonconformity across all horizon steps:
38	\begin{equation}
39	  a_{\mathrm{base}} = \argmin_{k \in \{1,\dots,K\}} \sum_{h=1}^{H} s_h\bigl(a_h^{(k)}\bigr).
40	  \label{eq:argmin}
41	\end{equation}
42	This selection procedure uses Mahalanobis-based scoring~\cite{braun2025cgs} to identify the sample closest to the consensus of the action distribution, isolating the effect of the downstream correction module. The selected $a_{\mathrm{base}} \in \mathbb{R}^{d \times H}$ is the starting point for residual correction.
43	
44	\subsection{Conformal Residual Module}
45	\label{sec:crm}
46	
47	The Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.
48	
49	\paragraph{Architecture.}
50	CRM is a 3-layer MLP with input normalization (input$\to$256$\to$256$\to$30; 329K parameters for the primary obs\_only variant).
51	Its input is the frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\boldsymbol{\delta} \in \mathbb{R}^{d \times H} = \mathbb{R}^{30}$, and the corrected action is:
52	\begin{equation}
53	  \mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}\bigl(\boldsymbol{\delta},\; \|\boldsymbol{\delta}\|_2 \leq \varepsilon\bigr),
54	  \label{eq:crm}
55	\end{equation}
56	where $\varepsilon$ is a norm bound hyperparameter (Section~\ref{sec:magnitude}).
57	
58	\paragraph{Observation-only conditioning.}
59	CRM receives only the observation embedding $\mathbf{z}_{\mathrm{obs}}$ and does \emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.
60	
61	\paragraph{Training.}
62	CRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\cite{liu2023libero}:
63	\begin{equation}
64	  \mathcal{L} = \bigl\|\mathbf{a}^* - \mathbf{a}_{\mathrm{expert}}\bigr\|_2^2.
65	  \label{eq:loss}
66	\end{equation}
67	The training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\ref{eq:argmin}) to obtain $a_{\mathrm{base}}$. The expert action $\mathbf{a}_{\mathrm{expert}}$ is the corresponding demonstration action.
68	
69	We apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\sigma \approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\cite{ross2011dagger}.
70	
71	\paragraph{Base VLA.}
72	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.
73	
74	\subsection{Magnitude Control}
75	\label{sec:magnitude}
76	
77	The norm bound $\varepsilon$ in~(\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.
78	
79	\paragraph{Unbounded correction fails catastrophically.}
80	Without clipping, the natural CRM output has $\|\boldsymbol{\delta}\|_2 \approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.
81	
82	\paragraph{Small corrections are effective.}
83	Constraining $\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.
84	
85	\paragraph{Connection to residual policy learning.}
86	The necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\cite{silver2018residual} introduced residual policy learning with zero-initialization for combining learned and classical controllers. TRANSIC~\cite{jiang2024transic} uses learned binary gating conditioned on the current state to selectively apply residual actions. PLD~\cite{xiao2026pld} introduces a magnitude bound $\xi$ for the residual actor, tuned per benchmark, during off-policy RL training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no multi-stage pipeline, just a hard constraint that prevents the correction from overwhelming the base policy.
87	
88	\paragraph{Differential sensitivity across CRM variants.}
89	Observation-conditioned CRM (obs\_only) maintains 35--36\% success on LIBERO-Spatial across the full range $\varepsilon \in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\% at $\varepsilon = 0.1$ to 26\% at $\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\ref{sec:ablation}).
90	
91	\subsection{Inference Protocol}
92	\label{sec:inference_protocol}
93	
94	Each control step proceeds as follows:
95	\begin{enumerate}[nosep]
96	  \item Draw $K{=}10$ action chunks from the frozen VLA $\pi_\theta$ and truncate to $H{=}5$ steps.
97	  \item Compute shrinkage covariance $\boldsymbol{\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.
98	  \item Select $a_{\mathrm{base}}$ via argmin over total nonconformity~(\ref{eq:argmin}).
99	  \item Compute residual $\boldsymbol{\delta} = \mathrm{CRM}(\mathbf{z}_{\mathrm{obs}})$ and clip to $\|\boldsymbol{\delta}\|_2 \leq \varepsilon$.
100	  \item Execute the first action of $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
101	  \item Observe new state and re-plan from step~1.
102	\end{enumerate}
103	The computational overhead consists of $K{=}10$ extra forward passes through the base VLA plus ${\sim}$3\,ms for CRM inference. The base VLA is never modified.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "e8d2e57f-dea7-443f-8c57-baf13d638b9b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis selection procedure uses Mahalanobis-based scoring~\\cite{braun2025cgs} to identify the sample closest to the consensus of the action distribution, isolating the effect of the downstream correction module. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 3-layer MLP with input normalization (input$\\to$256$\\to$256$\\to$30; 329K parameters for the primary obs\\_only variant).\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.\n\n\\paragraph{Small corrections are effective.}\nConstraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.\n\n\\paragraph{Connection to residual policy learning.}\nThe necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced residual policy learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating conditioned on the current state to selectively apply residual actions. PLD~\\cite{xiao2026pld} introduces a magnitude bound $\\xi$ for the residual actor, tuned per benchmark, during off-policy RL training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no multi-stage pipeline, just a hard constraint that prevents the correction from overwhelming the base policy.\n\n\\paragraph{Differential sensitivity across CRM variants.}\nObservation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.\n  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).\n  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead consists of $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper's style, content, and conventions. Let me also check the introduction for cross-referencing style.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "48d1263c-67d0-4bae-a66d-5aa559482d00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mj4nT86aMtRHGybEsPrjP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8770,
      "cache_read_input_tokens": 30756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8770
      },
      "output_tokens": 12,
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

_source line 18_

Now I have the full context. Let me write the discussion and conclusion sections.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "e4c418c7-735b-4fb5-8c40-7faa30467423",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mj4nT86aMtRHGybEsPrjP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8770,
      "cache_read_input_tokens": 30756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8770
      },
      "output_tokens": 12,
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

<details open><summary>🔧 Tool call — Bash · `toolu_01Qo3bGZzduppCtqfNYrQWNN`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections/",
  "description": "Check existing sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "06d9b208-d27b-4a5a-89bc-54c766cc6749",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018mj4nT86aMtRHGybEsPrjP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8770,
      "cache_read_input_tokens": 30756,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8770
      },
      "output_tokens": 12,
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

_source line 20 · 2026-05-15T20:38:50.529Z_

<details><summary>↩ Tool result · `toolu_01Qo3bGZzduppCtqfNYrQWNN`</summary>

```text
introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "f4c58690-3d68-429f-b23c-00357df00ebd",
  "tool_use_result": {
    "stdout": "introduction.tex",
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

_source line 21_

<details open><summary>🔧 Tool call — Write · `toolu_01ULcGaSFZf8JnzakbuFidXf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections/discussion.tex",
  "content": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why per-DOF conformal features fail.}\nThe negative result on conformal conditioning (Section~\\ref{sec:ablation}) warrants explanation.\n% exp_id: perdof_eps0.1_object → 11.0%, obs_only_eps0.1_object → 19.0%\nAt $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio $d/K = 0.6$ means that even with Ledoit--Wolf shrinkage~\\cite{ledoit2004well}, per-DOF statistics---standard deviations, conformal radii---carry substantial estimation noise.\nThe frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes the geometric information these features attempt to capture: object identity, spatial layout, and gripper-object relationship.\nAdding noisy low-dimensional statistics to a rich representation does not improve the CRM's predictions; it degrades them.\n\nA subtler issue is the gap between offline and closed-loop metrics.\nPer-DOF features reduce per-step MSE on held-out demonstration data, yet this does not translate to higher episode success.\nIn closed-loop execution, compounding error~\\cite{ross2011dagger} shifts the state distribution away from training data, and the noisy conformal features amplify this drift---occasional large corrections that reduce average MSE can cause catastrophic failures in individual episodes.\nThis challenges the intuition from controlled synthetic settings that richer uncertainty features improve corrections, and raises an open question: would larger $K$ (e.g., $K{=}50$) yield reliable enough covariance estimates for per-DOF features to help?\nWe cannot test this due to the $K$-fold increase in VLA forward passes per control step.\n\n\\paragraph{When does action-level correction help?}\n% exp_id: obs_only_eps0.1_object → 19.0%, argmin_K10_object → 12.0%\n% exp_id: obs_only_eps0.1_spatial → 35.0%, argmin_K10_spatial → 34.0%\nThe +7.0\\,pp gain on LIBERO-Object versus the null result on LIBERO-Spatial (Table~\\ref{tab:main}) reveals a structural distinction.\nObject perturbations (novel object instances) create systematic action biases: the VLA produces actions with consistent directional errors that a learned module can identify and compensate from observation features alone.\nSpatial perturbations (layout changes) require higher-level re-planning---the actions may be locally reasonable but directed at the wrong goal location.\nAction-level residuals are effective for fine-grained motor adjustments, not for strategic re-planning.\nThis suggests that the benefit of post-hoc correction depends on whether the distribution shift manifests as correctable motor error or as a planning-level failure.\n\n\\paragraph{Limitations.}\nWe identify seven limitations, each of which qualifies the scope of our findings:\n\\begin{enumerate}[nosep]\n  \\item \\emph{Simulation only.} All experiments use LIBERO~\\cite{liu2023libero}; real-robot transfer is untested.\n  \\item \\emph{Single VLA backbone.} We evaluate only SmolVLA~\\cite{shukor2025smolvla} (450M parameters). Whether ACR-VLA transfers to larger VLAs (e.g., $\\pi_0$, OpenVLA) is unknown.\n  \\item \\emph{Limited benchmarks.} Two LIBERO suites (20 tasks total); other manipulation benchmarks and perturbation types are not evaluated.\n  % exp_id: obs_only per-task variance — some object tasks underperform argmin\n  \\item \\emph{Per-task variance.} On individual LIBERO-Object tasks, obs\\_only occasionally underperforms the Argmin baseline. The method does not universally help.\n  \\item \\emph{Magnitude bound requires tuning.} We use $\\varepsilon{=}0.1$ throughout, but the optimal $\\varepsilon$ likely varies across VLA architectures and task domains.\n  % exp_id: seed42 only; seed43 pending\n  \\item \\emph{Single-seed results.} All primary results use seed 42. Seed 43 replication is pending; we make no statistical significance claims.\n  % exp_id: obs_only_eps0.1_object → 19.0%\n  \\item \\emph{Absolute performance.} 19.0\\% success on LIBERO-Object is far from deployment-ready. ACR-VLA reduces the gap relative to selection-only but does not close it.\n\\end{enumerate}\n\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\n% exp_id: obs_only_eps0.1_object → 19.0%, argmin_K10_object → 12.0%\n% exp_id: obs_only_eps0.1_spatial → 35.0%, argmin_K10_spatial → 34.0%\nWe presented ACR-VLA, a sample-then-correct pipeline that wraps a frozen flow-matching VLA with multi-sample conformal selection followed by a lightweight residual correction module (${\\sim}$329K parameters, ${\\sim}$3\\,ms overhead).\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% task success versus 12.0\\% for selection alone (+7.0\\,pp).\nOn LIBERO-Spatial, correction provides no measurable benefit over selection ($\\pm$1\\,pp), indicating the approach is effective for fine-grained motor correction under object-level distribution shift but not for spatial re-planning.\n\n% exp_id: perdof_eps0.1_object → 11.0%, obs_only_eps0.1_object → 19.0%\nOur central negative result is that per-DOF conformal features do not improve correction over observation-only conditioning, despite providing intuitively richer uncertainty information.\nAt the $K{=}10$ sample budget, covariance estimation noise outweighs the information gain.\nThis is a cautionary finding for the broader agenda of uncertainty-conditioned action correction: the gap between offline prediction accuracy and closed-loop task success remains a fundamental challenge.\n\nConcrete next steps include: (i)~validation across multiple VLA backbones and scales, (ii)~real-robot transfer experiments, (iii)~adaptive magnitude scheduling (learned $\\varepsilon$ conditioned on observation uncertainty), and (iv)~higher-$K$ sampling to revisit whether per-DOF conformal features become useful with better covariance estimates.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "dc23e5d8-2378-4f92-b14f-d5e86767a5e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6x7tYLnVnjL6pgcWhDbiL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 39526,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 192
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

_source line 22 · 2026-05-15T20:39:38.593Z_

<details><summary>↩ Tool result · `toolu_01ULcGaSFZf8JnzakbuFidXf`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "edace56e-2ed9-4b22-b476-5d0cd5bfd7f4",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/sections/discussion.tex",
    "content": "\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why per-DOF conformal features fail.}\nThe negative result on conformal conditioning (Section~\\ref{sec:ablation}) warrants explanation.\n% exp_id: perdof_eps0.1_object → 11.0%, obs_only_eps0.1_object → 19.0%\nAt $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio $d/K = 0.6$ means that even with Ledoit--Wolf shrinkage~\\cite{ledoit2004well}, per-DOF statistics---standard deviations, conformal radii---carry substantial estimation noise.\nThe frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes the geometric information these features attempt to capture: object identity, spatial layout, and gripper-object relationship.\nAdding noisy low-dimensional statistics to a rich representation does not improve the CRM's predictions; it degrades them.\n\nA subtler issue is the gap between offline and closed-loop metrics.\nPer-DOF features reduce per-step MSE on held-out demonstration data, yet this does not translate to higher episode success.\nIn closed-loop execution, compounding error~\\cite{ross2011dagger} shifts the state distribution away from training data, and the noisy conformal features amplify this drift---occasional large corrections that reduce average MSE can cause catastrophic failures in individual episodes.\nThis challenges the intuition from controlled synthetic settings that richer uncertainty features improve corrections, and raises an open question: would larger $K$ (e.g., $K{=}50$) yield reliable enough covariance estimates for per-DOF features to help?\nWe cannot test this due to the $K$-fold increase in VLA forward passes per control step.\n\n\\paragraph{When does action-level correction help?}\n% exp_id: obs_only_eps0.1_object → 19.0%, argmin_K10_object → 12.0%\n% exp_id: obs_only_eps0.1_spatial → 35.0%, argmin_K10_spatial → 34.0%\nThe +7.0\\,pp gain on LIBERO-Object versus the null result on LIBERO-Spatial (Table~\\ref{tab:main}) reveals a structural distinction.\nObject perturbations (novel object instances) create systematic action biases: the VLA produces actions with consistent directional errors that a learned module can identify and compensate from observation features alone.\nSpatial perturbations (layout changes) require higher-level re-planning---the actions may be locally reasonable but directed at the wrong goal location.\nAction-level residuals are effective for fine-grained motor adjustments, not for strategic re-planning.\nThis suggests that the benefit of post-hoc correction depends on whether the distribution shift manifests as correctable motor error or as a planning-level failure.\n\n\\paragraph{Limitations.}\nWe identify seven limitations, each of which qualifies the scope of our findings:\n\\begin{enumerate}[nosep]\n  \\item \\emph{Simulation only.} All experiments use LIBERO~\\cite{liu2023libero}; real-robot transfer is untested.\n  \\item \\emph{Single VLA backbone.} We evaluate only SmolVLA~\\cite{shukor2025smolvla} (450M parameters). Whether ACR-VLA transfers to larger VLAs (e.g., $\\pi_0$, OpenVLA) is unknown.\n  \\item \\emph{Limited benchmarks.} Two LIBERO suites (20 tasks total); other manipulation benchmarks and perturbation types are not evaluated.\n  % exp_id: obs_only per-task variance — some object tasks underperform argmin\n  \\item \\emph{Per-task variance.} On individual LIBERO-Object tasks, obs\\_only occasionally underperforms the Argmin baseline. The method does not universally help.\n  \\item \\emph{Magnitude bound requires tuning.} We use $\\varepsilon{=}0.1$ throughout, but the optimal $\\varepsilon$ likely varies across VLA architectures and task domains.\n  % exp_id: seed42 only; seed43 pending\n  \\item \\emph{Single-seed results.} All primary results use seed 42. Seed 43 replication is pending; we make no statistical significance claims.\n  % exp_id: obs_only_eps0.1_object → 19.0%\n  \\item \\emph{Absolute performance.} 19.0\\% success on LIBERO-Object is far from deployment-ready. ACR-VLA reduces the gap relative to selection-only but does not close it.\n\\end{enumerate}\n\n\n\\section{Conclusion}\n\\label{sec:conclusion}\n\n% exp_id: obs_only_eps0.1_object → 19.0%, argmin_K10_object → 12.0%\n% exp_id: obs_only_eps0.1_spatial → 35.0%, argmin_K10_spatial → 34.0%\nWe presented ACR-VLA, a sample-then-correct pipeline that wraps a frozen flow-matching VLA with multi-sample conformal selection followed by a lightweight residual correction module (${\\sim}$329K parameters, ${\\sim}$3\\,ms overhead).\nOn LIBERO-Object, observation-conditioned CRM achieves 19.0\\% task success versus 12.0\\% for selection alone (+7.0\\,pp).\nOn LIBERO-Spatial, correction provides no measurable benefit over selection ($\\pm$1\\,pp), indicating the approach is effective for fine-grained motor correction under object-level distribution shift but not for spatial re-planning.\n\n% exp_id: perdof_eps0.1_object → 11.0%, obs_only_eps0.1_object → 19.0%\nOur central negative result is that per-DOF conformal features do not improve correction over observation-only conditioning, despite providing intuitively richer uncertainty information.\nAt the $K{=}10$ sample budget, covariance estimation noise outweighs the information gain.\nThis is a cautionary finding for the broader agenda of uncertainty-conditioned action correction: the gap between offline prediction accuracy and closed-loop task success remains a fundamental challenge.\n\nConcrete next steps include: (i)~validation across multiple VLA backbones and scales, (ii)~real-robot transfer experiments, (iii)~adaptive magnitude scheduling (learned $\\varepsilon$ conditioned on observation uncertainty), and (iv)~higher-$K$ sampling to revisit whether per-DOF conformal features become useful with better covariance estimates.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 23_

Written to `artifacts/_project/paper/sections/discussion.tex`. Discussion is ~0.5 pages (3 paragraphs: negative result explanation, object-vs-spatial analysis, 7 explicit limitations). Conclusion is ~0.3 pages (3 paragraphs: what/found, negative result implications, future directions). All quantitative claims have `% exp_id:` comments and use the exact numbers provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "uuid": "27f45f51-e39c-4fce-a7da-8f65ed5e637d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FiWBLr9mC5SvZSV6rjs2x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1864,
      "cache_read_input_tokens": 39718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1864
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

Written to `artifacts/_project/paper/sections/discussion.tex`. Discussion is ~0.5 pages (3 paragraphs: negative result explanation, object-vs-spatial analysis, 7 explicit limitations). Conclusion is ~0.3 pages (3 paragraphs: what/found, negative result implications, future directions). All quantitative claims have `% exp_id:` comments and use the exact numbers provided.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 71884,
  "duration_api_ms": 72531,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "9c90d656-cedf-44a6-ac74-c03eb5480e0d",
  "total_cost_usd": 0.32317925,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 29741,
    "cache_read_input_tokens": 146710,
    "output_tokens": 2455,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29741,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 97,
        "cache_read_input_tokens": 39718,
        "cache_creation_input_tokens": 1864,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1864
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2438,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002538,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 2455,
      "cacheReadInputTokens": 146710,
      "cacheCreationInputTokens": 29741,
      "webSearchRequests": 0,
      "costUSD": 0.32064125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8d91cf36-d378-4557-9b97-d56230a05655"
}
```

</details>

---
