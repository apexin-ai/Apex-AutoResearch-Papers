# paper writing

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 107
- **Recorded user turns:** 1
- **Tool calls:** 34
- **Original source:** `logs/workers/worker_paper_writing_20260516T123624.log`
- **Structured JSON:** [`ef6cbbf6b163322f4b7c.json`](../../sessions/ef/ef6cbbf6b163322f4b7c.json)

## Before a recorded user message

11 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
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
  "uuid": "cf8777f0-7a9a-46da-924f-7e66dcc7c744",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/memory/"
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
    "resetsAt": 1778940600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "14b8d091-f23e-458e-87ea-02875e9bdeea",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the required files to understand the context and writing conventions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "054692dc-cc2d-4011-933c-9854c64bf0b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3wWj3djX81AtetwiK629r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13368,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13368
      },
      "output_tokens": 40,
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

<details open><summary>🔧 Tool call — Read · `toolu_01YbaCXPVjB5rQJB6MA1Pmgk`</summary>

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
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "147b79f8-dbad-4227-985a-96873f3b0ce6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3wWj3djX81AtetwiK629r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13368,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13368
      },
      "output_tokens": 40,
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

_source line 6 · 2026-05-16T12:36:34.197Z_

<details><summary>↩ Tool result · `toolu_01YbaCXPVjB5rQJB6MA1Pmgk`</summary>

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
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "b840cd20-b182-4629-a28e-d66f16305e60",
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

<details open><summary>🔧 Tool call — Read · `toolu_01UGEjTui3JwaLrb6VuYAAoi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "541ecb17-72b2-41dc-a30f-0585d5555f27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3wWj3djX81AtetwiK629r",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13368,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13368
      },
      "output_tokens": 40,
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

_source line 8 · 2026-05-16T12:36:34.285Z_

<details><summary>↩ Tool result · `toolu_01UGEjTui3JwaLrb6VuYAAoi`</summary>

```text
1	\section{Experiments}
2	
3	\subsection{Experimental Setup}
4	
5	\paragraph{Model and Predictor.}
6	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
7	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + Linear($128 \to 14336$), trained to predict activation magnitudes from the FFN input representation.
8	
9	\paragraph{Training.}
10	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \times 10^{-3}$ and cosine decay.
11	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
12	
13	\paragraph{Evaluation.}
14	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
15	
16	\paragraph{Inference Protocol.}
17	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
18	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
19	
20	\paragraph{Baselines.}
21	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
22	
23	
24	\subsection{Main Results}
25	
26	Table~\ref{tab:main} presents the primary comparison across sparsity levels.
27	At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.98, reducing TEAL's degradation from dense (10.97 $\to$ 8.98, an 18\% improvement). % exp_id: kl_30_global_teal
28	Uniform allocation at 30\% yields the lowest PPL (8.82) and notably recovers MMLU to 40.61\%, compared to 38.61\% for TEAL and 25.27\% for KL-global. % exp_id: kl_30_uniform
29	This indicates that at moderate sparsity, the allocation strategy—not the predictor—is the primary lever for knowledge-intensive tasks.
30	
31	At 50\% sparsity, the advantage of KL distillation over vanilla TEAL widens: PPL 11.79 vs.\ 23.31, a 49\% reduction. % exp_id: bench_kl50_global, bench_teal50
32	However, all methods exhibit downstream collapse on MMLU (27.89\% $\approx$ random at 25\%) and GSM8K ($<$2.2\%), indicating a capacity-limited regime where no allocation strategy can recover reasoning ability. % exp_id: kl_50_downstream
33	
34	\begin{table}[t]
35	\centering
36	\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. Best per sparsity level in \textbf{bold}.}
37	\label{tab:main}
38	\small
39	\begin{tabular}{llccccc}
40	\toprule
41	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
42	\midrule
43	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
44	\midrule
45	\multirow{3}{*}{30\%}
46	& TEAL vanilla & 10.97 & \textbf{42.32} & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
47	& KL global (Ours) & 8.98 & 39.68 & \textbf{70.17} & 25.27 & \textbf{8.79} \\ % exp_id: lm_eval_kl_30pct_s42
48	& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.61} & 7.35 \\ % exp_id: bench_kl30_uniform
49	\midrule
50	\multirow{4}{*}{50\%}
51	& TEAL vanilla & 23.31 & 28.41 & 53.04 & 28.32 & 1.97 \\ % exp_id: teal_50_vanilla
52	& KL global (Ours) & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & \textbf{27.89} & 1.29 \\ % exp_id: kl_50_global_teal
53	& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \textbf{2.12} \\ % exp_id: kl_50_uniform
54	& BCE (2700 steps) & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\ % exp_id: bce_isocompute_s42
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	
60	\subsection{Iso-Compute Analysis}
61	\label{sec:isocompute}
62	
63	A natural question is whether BCE training simply requires more compute to converge.
64	We train the BCE predictor for 2700 steps (2.71$\times$ the KL budget) and evaluate under identical TEAL inference.
65	As Table~\ref{tab:main} shows, the BCE predictor at 2700 steps achieves PPL 27.97—still 2.37$\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce_isocompute_s42
66	
67	The failure is structural, not computational.
68	BCE loss decomposes into independent per-neuron gradients, training each neuron's prediction in isolation.
69	This factorized objective cannot learn the inter-neuron correlations required for global top-$k$ allocation, where the keep/prune decision for neuron $i$ depends on the scores of all other neurons across all layers.
70	We observe that BCE training loss saturates early: between steps 500 and 2700, the loss decreases by only 0.006, confirming that additional compute yields diminishing returns under the wrong objective.
71	
72	
73	\subsection{Ablation Studies}
74	
75	Table~\ref{tab:ablation} isolates the contribution of each design choice at 50\% sparsity.
76	
77	\begin{table}[t]
78	\centering
79	\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$). $^\dagger$SPON $\Delta$ measured with \texttt{evaluate.py}; absolute PPL estimated from $\Delta$.}
80	\label{tab:ablation}
81	\small
82	\begin{tabular}{lcc}
83	\toprule
84	Configuration & PPL$\downarrow$ & $\Delta$ from Ours \\
85	\midrule
86	KL + Gumbel (Ours) & \textbf{11.79} & --- \\ % exp_id: bench_kl50_global
87	KL + Gumbel + SPON & 11.58$^\dagger$ & $-$0.21 \\ % exp_id: spon_2048_s42
88	KL + STE & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
89	BCE + Compensation (hard mask) & 25.44 & +13.65 \\ % exp_id: bce_comp_staged_s42
90	BCE (no compensation) & 27.97 & +16.18 \\ % exp_id: eval_bce_v3_s42
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	\paragraph{Gumbel vs.\ STE.}
96	Replacing Gumbel-Sigmoid relaxation with Straight-Through Estimation~\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98). % exp_id: ste_baseline_s42
97	Gumbel relaxation provides smooth gradients through the mask sampling, accounting for 34.5\% of the total improvement over vanilla TEAL (3.98 out of 11.52 PPL gap).
98	
99	\paragraph{SPON Contribution.}
100	Adding SPON~\cite{xu2026spon} bias correction yields an estimated PPL of 11.58, a marginal 0.21 improvement (1.8\% relative) over KL+Gumbel alone. % exp_id: spon_2048_s42
101	We analyze this limited contribution further in \S\ref{sec:spon}.
102	
103	\paragraph{BCE + Compensation.}
104	Compensation (output rescaling after hard-mask pruning) improves BCE from 27.97 to 25.44 (9.0\% relative), but this hard-mask protocol remains 2.16$\times$ worse than KL under TEAL inference. % exp_id: bce_comp_staged_s42
105	We report this separately as it uses a different inference protocol (hard mask vs.\ TEAL global allocation).
106	
107	
108	\subsection{Sparsity Scaling and Phase Transition}
109	\label{sec:scaling}
110	
111	Table~\ref{tab:scaling} and Figure~\ref{fig:sparsity_sweep} show PPL as a function of sparsity for KL-predictor-TEAL and vanilla TEAL.
112	
113	\begin{table}[t]
114	\centering
115	\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows super-linearly.}
116	\label{tab:scaling}
117	\small
118	\begin{tabular}{lccc}
119	\toprule
120	Sparsity & KL (Ours) & TEAL vanilla & Relative advantage \\
121	\midrule
122	30\% & \textbf{8.98} & 10.97 & 18\% \\ % exp_id: kl_30_global_teal
123	50\% & \textbf{11.79} & 23.31 & 49\% \\ % exp_id: bench_kl50_global
124	70\% & \textbf{17.91} & 100.11 & 82\% \\ % exp_id: kl_70_global_teal
125	\bottomrule
126	\end{tabular}
127	\end{table}
128	
129	The KL predictor's advantage grows from 18\% at 30\% sparsity to 82\% at 70\% sparsity.
130	At high sparsity, TEAL's magnitude-based scoring collapses (PPL 100.11), while the learned predictor maintains coherent allocation by exploiting input-dependent contextual information.
131	
132	\paragraph{Downstream Phase Transition.}
133	Table~\ref{tab:phase} examines how downstream task accuracy degrades with increasing sparsity under uniform allocation (which maximizes MMLU at each level).
134	
135	\begin{table}[t]
136	\centering
137	\caption{Phase transition in MMLU accuracy under uniform allocation. Random performance is 25\%.}
138	\label{tab:phase}
139	\small
140	\begin{tabular}{lcc}
141	\toprule
142	Sparsity & MMLU (\%) & Regime \\
143	\midrule
144	0\% (Dense) & 65.27 & Full capacity \\
145	30\% & 40.61 & Operable (15\% above random) \\ % exp_id: kl_30_uniform
146	40\% & 30.68 & Degradation band \\ % exp_id: kl_40_uniform
147	50\% & 27.77 & Capacity-limited ($\approx$ random) \\ % exp_id: kl_50_uniform
148	\bottomrule
149	\end{tabular}
150	\end{table}
151	
152	The transition from operable to capacity-limited is gradual—a degradation band spanning 30--50\% sparsity—rather than a sharp cliff.
153	At 30\%, the model retains sufficient capacity for knowledge recall (MMLU 40.61\%, 15 points above random), while at 50\%, no allocation strategy recovers meaningful performance.
154	This suggests 30\% as the recommended operating point for deployment scenarios requiring both perplexity and downstream task fidelity.
155	
156	
157	\subsection{SPON Orthogonality Analysis}
158	\label{sec:spon}
159	
160	We analyze why SPON's contribution is limited by decomposing the output perturbation at 50\% sparsity (Figure~\ref{fig:subsumption}).
161	
162	The predictor's effect on the hidden state has L2 norm 482.65, while SPON's additive correction has norm 76.2—only 15.8\% of the predictor's magnitude. % exp_id: spon_decomposition
163	The cosine similarity between the two perturbation directions is 0.196, confirming near-orthogonality: SPON corrects in a direction largely independent of the predictor's effect, but its small magnitude limits impact.
164	
165	In terms of PPL recovery, SPON provides: 7.3\% improvement under hard-mask inference (9.22 $\to$ 8.99) and 4.8\% under TEAL-path inference (12.08 $\to$ 11.79). % exp_id: spon_ppl_recovery
166	The interaction norm between predictor and SPON effects is 147.74, indicating non-trivial coupling but insufficient magnitude for SPON to meaningfully complement KL distillation.
167	This subsumption effect explains why the combination yields only marginal gains: the KL predictor already captures most of the recoverable signal, leaving little residual for SPON to correct.
168	
169	
170	\subsection{Cross-Architecture Generalization}
171	
172	To verify that KL distillation is not specific to LLaMA's architecture, we evaluate on Mistral-7B-v0.3~\cite{jiang2023mistral}, which differs in using Grouped Query Attention (GQA) and sliding window attention.
173	
174	\begin{table}[t]
175	\centering
176	\caption{Cross-architecture results at 50\% sparsity (WikiText-2 PPL$\downarrow$).}
177	\label{tab:cross_arch}
178	\small
179	\begin{tabular}{lccc}
180	\toprule
181	Model & Dense PPL & KL TEAL PPL & Relative degradation \\
182	\midrule
183	LLaMA-3.1-8B & 6.12 & 11.79 & +93\% \\ % exp_id: bench_kl50_global
184	Mistral-7B-v0.3 & 5.52 & 8.98 & +63\% \\ % exp_id: kl_50_mistral
185	\bottomrule
186	\end{tabular}
187	\end{table}
188	
189	The KL predictor transfers to Mistral with lower relative degradation (+63\% vs.\ +93\% on LLaMA). % exp_id: mistral_kl_s42, bench_kl50_global
190	Mistral's GQA mechanism produces more informative key-value representations at each layer, potentially providing richer input signals for the sparsity predictor.
191	The result confirms that KL distillation for contextual sparsity prediction generalizes across SwiGLU-based architectures with different attention configurations.
192	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "6d8e33cb-89a1-4842-9564-d8edec2d4a8e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "\\section{Experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + Linear($128 \\to 14336$), trained to predict activation magnitudes from the FFN input representation.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \\times 10^{-3}$ and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly; (2) \\textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \\textbf{WINA}~\\cite{liu2025teal}, an importance-weighted variant.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison across sparsity levels.\nAt 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.98, reducing TEAL's degradation from dense (10.97 $\\to$ 8.98, an 18\\% improvement). % exp_id: kl_30_global_teal\nUniform allocation at 30\\% yields the lowest PPL (8.82) and notably recovers MMLU to 40.61\\%, compared to 38.61\\% for TEAL and 25.27\\% for KL-global. % exp_id: kl_30_uniform\nThis indicates that at moderate sparsity, the allocation strategy—not the predictor—is the primary lever for knowledge-intensive tasks.\n\nAt 50\\% sparsity, the advantage of KL distillation over vanilla TEAL widens: PPL 11.79 vs.\\ 23.31, a 49\\% reduction. % exp_id: bench_kl50_global, bench_teal50\nHowever, all methods exhibit downstream collapse on MMLU (27.89\\% $\\approx$ random at 25\\%) and GSM8K ($<$2.2\\%), indicating a capacity-limited regime where no allocation strategy can recover reasoning ability. % exp_id: kl_50_downstream\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. PPL$\\downarrow$ on WikiText-2; accuracy$\\uparrow$ on downstream tasks. Best per sparsity level in \\textbf{bold}.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & \\textbf{42.32} & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global (Ours) & 8.98 & 39.68 & \\textbf{70.17} & 25.27 & \\textbf{8.79} \\\\ % exp_id: lm_eval_kl_30pct_s42\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.61} & 7.35 \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{4}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & 28.32 & 1.97 \\\\ % exp_id: teal_50_vanilla\n& KL global (Ours) & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & \\textbf{27.89} & 1.29 \\\\ % exp_id: kl_50_global_teal\n& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \\textbf{2.12} \\\\ % exp_id: kl_50_uniform\n& BCE (2700 steps) & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\\\ % exp_id: bce_isocompute_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Iso-Compute Analysis}\n\\label{sec:isocompute}\n\nA natural question is whether BCE training simply requires more compute to converge.\nWe train the BCE predictor for 2700 steps (2.71$\\times$ the KL budget) and evaluate under identical TEAL inference.\nAs Table~\\ref{tab:main} shows, the BCE predictor at 2700 steps achieves PPL 27.97—still 2.37$\\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce_isocompute_s42\n\nThe failure is structural, not computational.\nBCE loss decomposes into independent per-neuron gradients, training each neuron's prediction in isolation.\nThis factorized objective cannot learn the inter-neuron correlations required for global top-$k$ allocation, where the keep/prune decision for neuron $i$ depends on the scores of all other neurons across all layers.\nWe observe that BCE training loss saturates early: between steps 500 and 2700, the loss decreases by only 0.006, confirming that additional compute yields diminishing returns under the wrong objective.\n\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation at 50\\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$). $^\\dagger$SPON $\\Delta$ measured with \\texttt{evaluate.py}; absolute PPL estimated from $\\Delta$.}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & PPL$\\downarrow$ & $\\Delta$ from Ours \\\\\n\\midrule\nKL + Gumbel (Ours) & \\textbf{11.79} & --- \\\\ % exp_id: bench_kl50_global\nKL + Gumbel + SPON & 11.58$^\\dagger$ & $-$0.21 \\\\ % exp_id: spon_2048_s42\nKL + STE & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\nBCE + Compensation (hard mask) & 25.44 & +13.65 \\\\ % exp_id: bce_comp_staged_s42\nBCE (no compensation) & 27.97 & +16.18 \\\\ % exp_id: eval_bce_v3_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gumbel vs.\\ STE.}\nReplacing Gumbel-Sigmoid relaxation with Straight-Through Estimation~\\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98). % exp_id: ste_baseline_s42\nGumbel relaxation provides smooth gradients through the mask sampling, accounting for 34.5\\% of the total improvement over vanilla TEAL (3.98 out of 11.52 PPL gap).\n\n\\paragraph{SPON Contribution.}\nAdding SPON~\\cite{xu2026spon} bias correction yields an estimated PPL of 11.58, a marginal 0.21 improvement (1.8\\% relative) over KL+Gumbel alone. % exp_id: spon_2048_s42\nWe analyze this limited contribution further in \\S\\ref{sec:spon}.\n\n\\paragraph{BCE + Compensation.}\nCompensation (output rescaling after hard-mask pruning) improves BCE from 27.97 to 25.44 (9.0\\% relative), but this hard-mask protocol remains 2.16$\\times$ worse than KL under TEAL inference. % exp_id: bce_comp_staged_s42\nWe report this separately as it uses a different inference protocol (hard mask vs.\\ TEAL global allocation).\n\n\n\\subsection{Sparsity Scaling and Phase Transition}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} and Figure~\\ref{fig:sparsity_sweep} show PPL as a function of sparsity for KL-predictor-TEAL and vanilla TEAL.\n\n\\begin{table}[t]\n\\centering\n\\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows super-linearly.}\n\\label{tab:scaling}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nSparsity & KL (Ours) & TEAL vanilla & Relative advantage \\\\\n\\midrule\n30\\% & \\textbf{8.98} & 10.97 & 18\\% \\\\ % exp_id: kl_30_global_teal\n50\\% & \\textbf{11.79} & 23.31 & 49\\% \\\\ % exp_id: bench_kl50_global\n70\\% & \\textbf{17.91} & 100.11 & 82\\% \\\\ % exp_id: kl_70_global_teal\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL predictor's advantage grows from 18\\% at 30\\% sparsity to 82\\% at 70\\% sparsity.\nAt high sparsity, TEAL's magnitude-based scoring collapses (PPL 100.11), while the learned predictor maintains coherent allocation by exploiting input-dependent contextual information.\n\n\\paragraph{Downstream Phase Transition.}\nTable~\\ref{tab:phase} examines how downstream task accuracy degrades with increasing sparsity under uniform allocation (which maximizes MMLU at each level).\n\n\\begin{table}[t]\n\\centering\n\\caption{Phase transition in MMLU accuracy under uniform allocation. Random performance is 25\\%.}\n\\label{tab:phase}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSparsity & MMLU (\\%) & Regime \\\\\n\\midrule\n0\\% (Dense) & 65.27 & Full capacity \\\\\n30\\% & 40.61 & Operable (15\\% above random) \\\\ % exp_id: kl_30_uniform\n40\\% & 30.68 & Degradation band \\\\ % exp_id: kl_40_uniform\n50\\% & 27.77 & Capacity-limited ($\\approx$ random) \\\\ % exp_id: kl_50_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe transition from operable to capacity-limited is gradual—a degradation band spanning 30--50\\% sparsity—rather than a sharp cliff.\nAt 30\\%, the model retains sufficient capacity for knowledge recall (MMLU 40.61\\%, 15 points above random), while at 50\\%, no allocation strategy recovers meaningful performance.\nThis suggests 30\\% as the recommended operating point for deployment scenarios requiring both perplexity and downstream task fidelity.\n\n\n\\subsection{SPON Orthogonality Analysis}\n\\label{sec:spon}\n\nWe analyze why SPON's contribution is limited by decomposing the output perturbation at 50\\% sparsity (Figure~\\ref{fig:subsumption}).\n\nThe predictor's effect on the hidden state has L2 norm 482.65, while SPON's additive correction has norm 76.2—only 15.8\\% of the predictor's magnitude. % exp_id: spon_decomposition\nThe cosine similarity between the two perturbation directions is 0.196, confirming near-orthogonality: SPON corrects in a direction largely independent of the predictor's effect, but its small magnitude limits impact.\n\nIn terms of PPL recovery, SPON provides: 7.3\\% improvement under hard-mask inference (9.22 $\\to$ 8.99) and 4.8\\% under TEAL-path inference (12.08 $\\to$ 11.79). % exp_id: spon_ppl_recovery\nThe interaction norm between predictor and SPON effects is 147.74, indicating non-trivial coupling but insufficient magnitude for SPON to meaningfully complement KL distillation.\nThis subsumption effect explains why the combination yields only marginal gains: the KL predictor already captures most of the recoverable signal, leaving little residual for SPON to correct.\n\n\n\\subsection{Cross-Architecture Generalization}\n\nTo verify that KL distillation is not specific to LLaMA's architecture, we evaluate on Mistral-7B-v0.3~\\cite{jiang2023mistral}, which differs in using Grouped Query Attention (GQA) and sliding window attention.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture results at 50\\% sparsity (WikiText-2 PPL$\\downarrow$).}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nModel & Dense PPL & KL TEAL PPL & Relative degradation \\\\\n\\midrule\nLLaMA-3.1-8B & 6.12 & 11.79 & +93\\% \\\\ % exp_id: bench_kl50_global\nMistral-7B-v0.3 & 5.52 & 8.98 & +63\\% \\\\ % exp_id: kl_50_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL predictor transfers to Mistral with lower relative degradation (+63\\% vs.\\ +93\\% on LLaMA). % exp_id: mistral_kl_s42, bench_kl50_global\nMistral's GQA mechanism produces more informative key-value representations at each layer, potentially providing richer input signals for the sparsity predictor.\nThe result confirms that KL distillation for contextual sparsity prediction generalizes across SwiGLU-based architectures with different attention configurations.\n",
      "numLines": 192,
      "startLine": 1,
      "totalLines": 192
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

Now let me check if there's a notation table or other context files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "e41882b8-42f7-49f7-82d1-b3d8ab6d1248",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfYf1UrPKGBJDNeZL2Egr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10164,
      "cache_read_input_tokens": 25209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10164
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

_source line 10_

<details open><summary>🔧 Tool call — Agent · `toolu_013inttiumy1irsrZ96v4KMi`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find notation table and paper files",
  "prompt": "Search for any notation table, symbol definitions, or paper-related files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/. Look for:\n1. A notation_table file (any extension)\n2. Any other .tex files in the paper/ directory\n3. Any ideas.md or similar planning docs that mention notation\n\nUse \"medium\" search breadth."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "e0454cb5-6ae4-4f98-bea2-0d95e5a7b326",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfYf1UrPKGBJDNeZL2Egr2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10164,
      "cache_read_input_tokens": 25209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10164
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

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Find notation table and paper files",
  "task_type": "local_agent",
  "prompt": "Search for any notation table, symbol definitions, or paper-related files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/. Look for:\n1. A notation_table file (any extension)\n2. Any other .tex files in the paper/ directory\n3. Any ideas.md or similar planning docs that mention notation\n\nUse \"medium\" search breadth.",
  "uuid": "d1d31541-04aa-41cc-b276-44285e2c61e8",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

## Round 1

96 recorded events

### User

_source line 12 · 2026-05-16T12:36:42.215Z_

Search for any notation table, symbol definitions, or paper-related files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/. Look for:
1. A notation_table file (any extension)
2. Any other .tex files in the paper/ directory
3. Any ideas.md or similar planning docs that mention notation

Use "medium" search breadth.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "8b198073-9d45-44c1-84ff-b5a6d26cd271"
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Finding **/*notation*",
  "usage": {
    "total_tokens": 27258,
    "tool_uses": 1,
    "duration_ms": 1855
  },
  "last_tool_name": "Glob",
  "uuid": "d3c65b6a-a799-4dd1-8964-7607b6897a10",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_016TfwGvQNqSwszNXZyBq699`</summary>

```json
{
  "pattern": "**/*notation*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "a3d112c0-edcd-4206-9928-a94c05535a2e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PjfeeTZBioJFe8G8dC5Sdk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27247,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27247,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 15 · 2026-05-16T12:36:44.101Z_

<details><summary>↩ Tool result · `toolu_016TfwGvQNqSwszNXZyBq699`</summary>

```text
.venv/lib/python3.14/site-packages/fontTools/annotations.py
.venv/lib/python3.14/site-packages/fontTools/__pycache__/annotations.cpython-314.pyc
logs/workers/worker_paper_figure_fig2_v4_annotation_fix_20260516T002434.log
logs/workers/worker_paper_figure_fig2_v4_annotation_fix_20260516T002434_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "d7aadef6-ea09-4f5f-92fb-57475c1e79bd"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Finding **/paper/**/*.tex",
  "usage": {
    "total_tokens": 27262,
    "tool_uses": 2,
    "duration_ms": 2449
  },
  "last_tool_name": "Glob",
  "uuid": "bbfcbf10-3057-4ec6-b777-13139418c19a",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01E8NKyvHYURUeKqjgPvu9va`</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "25f03e21-03fe-4b91-ad7a-70185d50d4b7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PjfeeTZBioJFe8G8dC5Sdk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27247,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27247,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 18 · 2026-05-16T12:36:44.691Z_

<details><summary>↩ Tool result · `toolu_01E8NKyvHYURUeKqjgPvu9va`</summary>

```text
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/methodology_6e294a.tex
artifacts/_project/paper/related_work_c10e4f.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments.tex
paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "00e820e8-95e4-408f-9057-a3627f26c571"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Finding **/ideas.md",
  "usage": {
    "total_tokens": 27266,
    "tool_uses": 3,
    "duration_ms": 2524
  },
  "last_tool_name": "Glob",
  "uuid": "49e3e38f-6981-4dd6-b072-b01fa69a5286",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01SYz3CmnFbkr7MLgPp6EkMw`</summary>

```json
{
  "pattern": "**/ideas.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "90c0baba-f68b-426d-89de-05ab3efa7af5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PjfeeTZBioJFe8G8dC5Sdk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27247,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27247,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 21 · 2026-05-16T12:36:44.768Z_

<details><summary>↩ Tool result · `toolu_01SYz3CmnFbkr7MLgPp6EkMw`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "05b0ee15-2ce9-4c39-b4a3-9f271cdf8957"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Finding **/*.md",
  "usage": {
    "total_tokens": 27270,
    "tool_uses": 4,
    "duration_ms": 2812
  },
  "last_tool_name": "Glob",
  "uuid": "bce57cce-b616-4363-a784-702117706cd1",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Glob · `toolu_01H5NVQBHRkuzPHdQ7aggCKx`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "eff77184-69ae-4224-8ca3-52fad91551d4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PjfeeTZBioJFe8G8dC5Sdk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27247,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27247,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 24 · 2026-05-16T12:36:45.058Z_

<details><summary>↩ Tool result · `toolu_01H5NVQBHRkuzPHdQ7aggCKx`</summary>

```text
artifacts/mvp_bce_s42/report/report_mvp_bce_s42.md
artifacts/_project/report/bce_mvp_3seed_analysis.md
artifacts/bce_mvp_3seed_analysis.md
task_context/history/reviewer/loop_1.md
task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
task_context/history/agent/loop_1_1778861972.md
task_context/history/agent/loop_1_1778864854.md
docs/IDEA_BRIEF.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_1_1778865194.md
task_context/history/agent/loop_1_1778871099.md
artifacts/dream_reports/dream_20260515T164925/best/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/median/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T164925/best/review_report.md
artifacts/dream_reports/dream_20260515T164925/median/review_report.md
artifacts/dream_reports/dream_20260515T164925/worst/review_report.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_2.md
task_context/history/agent/loop_2_1778873177.md
task_context/history/agent/loop_2_1778873913.md
task_context/history/agent/loop_2_1778874382.md
task_context/history/agent/loop_2_1778876214.md
task_context/history/agent/loop_2_1778876347.md
task_context/history/agent/loop_2_1778878864.md
artifacts/plan_007/report/plan_007_wikitext2_ppl_results.md
artifacts/plan_006/report/diagnostic_report.md
task_context/history/agent/loop_2_1778882860.md
task_context/history/agent/loop_2_1778882930.md
task_context/history/agent/loop_2_1778883107.md
task_context/history/agent/loop_3.md
artifacts/plan_009_readiness_report.md
task_context/history/agent/loop_3_1778884170.md
task_context/history/agent/loop_2_1778884213.md
task_context/history/agent/loop_3_1778884273.md
task_context/history/agent/loop_2_1778885311.md
task_context/history/agent/loop_3_1778885581.md
task_context/history/reviewer/loop_3.md
task_context/history/agent/loop_3_1778885890.md
task_context/history/agent/loop_3_1778887468.md
task_context/history/agent/loop_3_1778888363.md
.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md
.venv/lib/python3.14/site-packages/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/_core/src/npysort/x86-simd-sort/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/fft/pocketfft/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/distributions/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/mt19937/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/pcg64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/philox/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/sfc64/LICENSE.md
.venv/lib/python3.14/site-packages/numpy-2.4.5.dist-info/licenses/numpy/random/src/splitmix64/LICENSE.md
task_context/history/agent/loop_3_1778888545.md
task_context/history/agent/loop_3_1778890852.md
artifacts/training_free_baselines/data/teal_baseline_sweep_p0_rerun.md
task_context/history/agent/loop_3_1778891037.md
task_context/history/agent/loop_3_1778891456.md
artifacts/lm_eval_status_check.md
task_context/history/agent/loop_3_1778896565.md
artifacts/gsm8k_gen_compare/report/gsm8k_gen_compare_report.md
task_context/history/agent/loop_4.md
task_context/history/agent/loop_3_1778896576.md
task_context/history/agent/loop_4_1778896580.md
task_context/history/agent/loop_3_1778896594.md
task_context/history/agent/loop_4_1778896626.md
task_context/history/agent/loop_4_1778896630.md
task_context/history/agent/loop_3_1778896709.md
task_context/history/agent/loop_4_1778898052.md
artifacts/process_check_loop5.md
artifacts/literature_ppl_downstream_disconnect.md
task_context/history/agent/loop_4_1778898562.md
task_context/history/agent/loop_4_1778899923.md
.claude/sessions/agent_42dd644f/CLAUDE.md
.claude/sessions/agent_42dd644f/AGENTS.md
.claude/sessions/agent_f8235f3f/CLAUDE.md
.claude/sessions/agent_f8235f3f/AGENTS.md
artifacts/_project/intermediate/plan_007_eval_batch_commands.md
.claude/sessions/agent_29e28dae/CLAUDE.md
.claude/sessions/agent_29e28dae/AGENTS.md
task_context/history/agent/loop_4_1778900747.md
.claude/sessions/agent_453ff340/CLAUDE.md
.claude/sessions/agent_453ff340/AGENTS.md
task_context/history/reviewer/loop_4.md
artifacts/_project/report/plan008_ppl_summary.md
artifacts/plan008_ppl_summary.md
artifacts/_project/report/framing_proposal_30pct_downstream.md
artifacts/framing_proposal_30pct_downstream.md
task_context/history/agent/loop_4_1778903040.md
.claude/sessions/agent_14ee8c60/CLAUDE.md
.claude/sessions/agent_14ee8c60/AGENTS.md
task_context/history/agent/loop_4_1778903117.md
.claude/sessions/agent_c9230555/CLAUDE.md
.claude/sessions/agent_c9230555/AGENTS.md
task_context/history/agent/loop_4_1778903261.md
.claude/sessions/agent_2236c95b/CLAUDE.md
.claude/sessions/agent_2236c95b/AGENTS.md
task_context/history/agent/loop_4_1778906676.md
.claude/sessions/agent_86d5f8b8/CLAUDE.md
.claude/sessions/agent_86d5f8b8/AGENTS.md
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "13bbba61-11c2-45d5-9eaf-9dda18cfb352"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Finding **/paper/*.tex",
  "usage": {
    "total_tokens": 30848,
    "tool_uses": 5,
    "duration_ms": 5117
  },
  "last_tool_name": "Glob",
  "uuid": "abd7d2d6-83d6-4cf5-8f04-657cd0c5f6fb",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Glob · `toolu_01TpFuYZWnFb2SXQijqxSSEH`</summary>

```json
{
  "pattern": "**/paper/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "04979b87-1eff-4d4f-9983-de11ec274282",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JCpwB2c6dvToDMjAhAbHZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 27247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3572,
        "ephemeral_1h_input_tokens": 0
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

_source line 27 · 2026-05-16T12:36:47.368Z_

<details><summary>↩ Tool result · `toolu_01TpFuYZWnFb2SXQijqxSSEH`</summary>

```text
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/methodology_6e294a.tex
artifacts/_project/paper/related_work_c10e4f.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/experiments.tex
paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "5dd642ed-b832-4e86-ae2c-612e8e2004bc"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Finding **/symbol*",
  "usage": {
    "total_tokens": 30849,
    "tool_uses": 6,
    "duration_ms": 5534
  },
  "last_tool_name": "Glob",
  "uuid": "4f9059a9-d3c7-4c27-b513-e68755316d63",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Glob · `toolu_013VMY5h3UhGJF9iZq4ETn3o`</summary>

```json
{
  "pattern": "**/symbol*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "78abfb54-de1d-4c8d-882e-48a9387f685e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JCpwB2c6dvToDMjAhAbHZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 27247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3572,
        "ephemeral_1h_input_tokens": 0
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

_source line 30 · 2026-05-16T12:36:47.779Z_

<details><summary>↩ Tool result · `toolu_013VMY5h3UhGJF9iZq4ETn3o`</summary>

```text
.venv/lib/python3.14/site-packages/numpy/f2py/symbolic.py
.venv/lib/python3.14/site-packages/numpy/f2py/symbolic.pyi
.venv/lib/python3.14/site-packages/numpy/f2py/__pycache__/symbolic.cpython-314.pyc
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "c7a354d9-f385-4d8c-8b57-91e32ea8a416"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 30850,
    "tool_uses": 7,
    "duration_ms": 5781
  },
  "last_tool_name": "Bash",
  "uuid": "0c37af4c-e252-45a4-9fd2-f7dde3255b02",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01RpMff9p5Cyvif55GZ9ygEV`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper -maxdepth 2 -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "c2a05460-aea0-4ead-ace7-d58abfa475ca",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JCpwB2c6dvToDMjAhAbHZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 27247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3572,
        "ephemeral_1h_input_tokens": 0
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

_source line 33 · 2026-05-16T12:36:48.216Z_

<details><summary>↩ Tool result · `toolu_01RpMff9p5Cyvif55GZ9ygEV`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "88e57691-0ab1-4b91-8a53-fb5d63e79d2b"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 30851,
    "tool_uses": 8,
    "duration_ms": 6241
  },
  "last_tool_name": "Bash",
  "uuid": "1acd3f76-c467-474e-8a5e-5334e34e5ac6",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01J7LCcyah72LmyzzcwD7ozo`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -maxdepth 2 -name \"*.md\" -not -path \"./.venv/*\" -not -path \"*/.venv/*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "5f012262-aad7-4fc3-b162-d45d35c73cb7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JCpwB2c6dvToDMjAhAbHZc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3572,
      "cache_read_input_tokens": 27247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3572,
        "ephemeral_1h_input_tokens": 0
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

_source line 36 · 2026-05-16T12:36:48.537Z_

<details><summary>↩ Tool result · `toolu_01J7LCcyah72LmyzzcwD7ozo`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/literature_sparsity_threshold.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/eval_kl30_30pct_command.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/server_status_check.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/process_check_loop5.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/benchmark_comparison_table.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/literature_ppl_downstream_disconnect.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/bce_mvp_3seed_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/process_verify_loop6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/lm_eval_status_check.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/plan_009_readiness_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/iso_compute_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/plan008_ppl_summary.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "f03c3041-9219-4d59-b10b-6011e3e8f4c1"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Reading memory.md",
  "usage": {
    "total_tokens": 32515,
    "tool_uses": 9,
    "duration_ms": 7944
  },
  "last_tool_name": "Read",
  "uuid": "7cf2838a-6b56-4b7e-a475-28e4e2b05c2c",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01P1jBfZN7sgffqtoVwDJk1L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "9e65dea5-2e2d-4e72-b395-8d96c54c8498",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013meVEJAA4Uw2RknTttYdAn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 30819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 39 · 2026-05-16T12:36:50.167Z_

<details><summary>↩ Tool result · `toolu_01P1jBfZN7sgffqtoVwDJk1L`</summary>

```text
1	# Memory — distill_sparse_swiglu
2	
3	## 关键决策原因
4	
5	### Uniform Allocation 为何是论文推荐配置
6	- Global top-k 将 sparsity 集中在后层（Layer 26-31: 41-70%），导致 MMLU 崩溃至 25.3%
7	- Uniform per-layer allocation 强制每层同 sparsity，30% 时 MMLU 恢复至 40.6%
8	- 机制解释：后层承载知识检索，过度剪枝直接破坏 factual recall
9	
10	### Phase Transition 而非 Quadratic Scaling (D034)
11	- 原 Claim 3 用 "quadratic scaling" 描述 sparsity 增加时 downstream 退化
12	- 数据显示 30→40% 是 cliff（MMLU 40.6%→30.7%），不是连续退化
13	- Reframe 为 "phase transition"：存在临界点，跨过后不可修复
14	
15	### BCE Framing: "Objective Mismatch" (非 Anti-Learning)
16	- BCE 训练 per-neuron binary classification（每个神经元独立判断是否激活）
17	- 推理时用 global top-k 选择（全局排序取 top）
18	- 训练目标（独立 binary）和推理协议（全局 top-k）结构性不兼容
19	- "Anti-learning" 暗示模型学错了，实际是目标函数和推理协议的 mismatch
20	
21	### SPON Framing: "Marginal Complement" (非 KL Subsumes SPON)
22	- SPON 提供正交信号（结构先验），KL 无法 subsume 因为二者优化不同目标
23	- 正确描述：SPON 在 KL 基础上提供 marginal complement（边际补充）
24	
25	## 约束
26	
27	### 服务器环境
28	- westd-34887, conda base 环境, `/root/miniconda3/bin/python`
29	- 工作目录: `/root/distill_sparse_swiglu/`
30	- 模型: Llama-3.1-8B at `/root/autodl-tmp/models/llama-3.1-8b/`
31	- Mistral-7B at `/root/autodl-tmp/models/mistral-7b/`
32	- WANDB_MODE=offline（服务器无 wandb API key）
33	- GPU 白名单: cuda:0 + cuda:1 only
34	
35	### 数据红线
36	- KL PPL 引用: 4-seed mean 12.00±0.07（禁用单 seed 最佳 11.91）
37	- D032 TEAL 30% PPL = 8.98（13.63 是 50% target 的结果，D032 错误修正已撤回）
38	- Mistral registry 数据疑似污染（D032），暂不引用
39	
40	## 经验教训
41	
42	### Benchmark 一致性 (D029)
43	- 论文所有对比必须用相同 few-shot 设置（ARC-c=25, WG=5, MMLU=5, GSM8K=8）
44	- 不同 shot 数的结果不可直接对比
45	- bench_dense 是统一 baseline，所有新 bench 对齐它的设置
46	
47	### 50% Uniform 无法拯救
48	- 50% uniform MMLU=27.77% ≈ random
49	- 不要再尝试 allocation 方法拯救 50%，已验证不可能
50	
51	### 不要凭推理改数字 (D032 教训)
52	- 修正数据前必须复现验证
53	- D032 曾错误推理 30% TEAL PPL 为 13.63，实际 8.98 是正确值
54	
55	## Checkpoints 路径
56	- KL 30%: `checkpoints/kl_sparsity30_s42_v3/predictor_kl_normalized.pt`
57	- KL 40%: `checkpoints/kl_sparsity40_s42/predictor_kl_normalized.pt`
58	- KL 50%: `checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt`
59	- BCE v3: `checkpoints/bce_isocompute_v3_s42/`
60	
61	## 论文 Narrative
62	- 骨架: PPL-Downstream Disconnect（文献空白最大）
63	- 血肉: Sparsity Threshold（30% 可修复，50% 不可修复）
64	- DDL: EMNLP 2026 ARR May, 2026-05-25（剩 9 天）
65	- A+C 混合 framing，Director 已批准
66	
67	## Table 1 数据完成度 (2026-05-16 12:30 UTC)
68	- Dense ✅ | TEAL 30% ✅ | TEAL 50% ✅
69	- KL 30% global ✅ | KL 30% uniform ✅
70	- KL 40% global ⏳ | KL 40% uniform ✅  
71	- KL 50% global ✅ | KL 50% uniform ⏳
72	- BCE 50% ✅
73	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "b977a8eb-d644-45ea-bdf6-66c16e009e29"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Reading docs/IDEA_BRIEF.md",
  "usage": {
    "total_tokens": 32518,
    "tool_uses": 10,
    "duration_ms": 8369
  },
  "last_tool_name": "Read",
  "uuid": "d0cf595c-5e56-4d32-8d56-fd37df8ff26c",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01XG1RfduFdmcCciQU3EKUNx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "9f7c3835-1ae3-4e34-ad7e-06a9ca5323c0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013meVEJAA4Uw2RknTttYdAn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 30819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

### System

_source line 42_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 32521,
    "tool_uses": 11,
    "duration_ms": 8573
  },
  "last_tool_name": "Bash",
  "uuid": "ec04175a-1dc9-49a5-bd17-93048efecd02",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01Xkn4VPg9gtbxLakCtjnnye`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper -type f | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "52dfcb47-6475-42a6-bfdd-3d8f296f7736",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013meVEJAA4Uw2RknTttYdAn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 30819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 44 · 2026-05-16T12:36:51.039Z_

<details><summary>↩ Tool result · `toolu_01XG1RfduFdmcCciQU3EKUNx`</summary>

```text
1	# Idea Brief: Composing Static and Contextual Corrections for Activation Sparsity in SwiGLU LLMs via Output-Distribution Distillation
2	
3	
4	- **Idea ID**: `idea_018`
5	- **Created**: 2026-05-15
6	- **Approved**: 2026-05-15
7	- **Source**: foreign:be-idea-gen-0509-2
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026)
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Efficient Methods for NLP.
14	
15	Direction: Efficiency methods for NLP — NOT limited to LLM inference optimization. In-scope: speculative decoding, KV-cache compression/eviction, quantization-aware distillation, parameter-efficient fine-tuning, efficient long-context serving, MoE routing, attention approximations, efficient smaller models for specific NLP tasks, pruning for task-specific deployment.
16	
17	Contribution type: METHOD ONLY. Propose new algorithms — not profiling studies.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Generous for efficiency work.
21	2. Time: ≤16 days. Build on vLLM, SGLang, llama.cpp, TensorRT-LLM, HF Transformers, FlashAttention, bitsandbytes.
22	3. Eval: perplexity (Wiki/C4), MMLU, HumanEval, LongBench, RULER, MT-Bench. Report wall-clock and throughput on H100.
23	
24	Look for: cache-aware methods for new workloads (long thinking traces, agent loops, RAG), quantization-aware distillation, structured sparsity during inference, efficient serving of reasoning models with variable-length thinking. Avoid: vanilla 4-bit quantization, generic LoRA, plain speculative decoding.
25	
26	Tag: direction=efficiency, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Core Problem
29	
30	Training-free activation sparsity methods (WINA, TEAL, R-Sparse) have enabled 40-60% model-level neuron pruning on native SwiGLU LLMs, but leave a substantial quality gap: at 50% model-level activation sparsity on Llama-3-8B, WINA achieves 59.57% average across six standard benchmarks (PIQA, ARC-c, WinoGrande, HellaSwag, MMLU, GSM8K) versus the dense model's 66.38% — a 6.81-point drop, with reasoning-heavy tasks (GSM8K, MMLU) degrading disproportionately. Two recent learned approaches partially address this gap from complementary but individually incomplete directions. SPON (Resting Neurons, arXiv 2512.12744v3, ICML 2026 per arXiv metadata updated on the April 30 notification date) introduces static, input-independent learnable bias vectors trained via KL-divergence distillation, recovering ~1 point over WINA on five QA benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande; 71.96 vs 70.97 weighted average) at zero inference overhead — demonstrating that output-distribution alignment helps, but leaving input-dependent importance patterns entirely unaddressed. FastForward (arXiv 2602.00397) trains contextual predictors with weighted BCE loss plus an error compensation network (2-layer MLP, r'=d_model/8) trained with MSE loss that operates at inference time, achieving MMLU 67.17 vs dense 67.84 at 50% FFN sparsity on Llama-3.1-8B — demonstrating that contextual prediction helps, but requiring the auxiliary compensation network to address the output-quality deficiency inherent in BCE's per-neuron objective. The compensation network adds ~8.0 MB of weights per layer (r'=d_model/8=512; two matrices of 4096×512, totaling 4,194,304 params × 2 bytes FP16 ≈ 8.0 MB) and associated GEMV operations at inference time — substantial overhead that motivates seeking training objectives that eliminate the need for compensation entirely. The critical insight is that BCE's training signal decomposes as L_BCE = Σ_j l(y_j, s_j), a per-neuron factorization that treats each neuron's activation decision as independent of all others. This cannot capture joint interaction effects — the fact that pruning neuron A may only degrade output quality when neuron B in the same or subsequent layer is also pruned. FastForward's error compensation network is an engineering fix for this limitation: it patches output errors post-hoc rather than training the predictor to avoid them. KL divergence on output logits, by contrast, backpropagates through the full sparse forward pass via ∂L_KL/∂θ = ∂L_KL/∂p_sparse · ∂p_sparse/∂h_out · ∂h_out/∂m · ∂m/∂θ, where the term ∂h_out/∂m captures how each neuron's mask decision jointly affects the output in combination with all other active neurons. This yields a testable prediction: KL's advantage over BCE should increase with sparsity level, because higher sparsity creates more simultaneous neuron removals and thus more pairwise and higher-order interaction terms that the per-neuron decomposition cannot model. However, DejaVu demonstrated >99% per-neuron prediction accuracy with pure BCE, suggesting the independent decomposition is a surprisingly good approximation at moderate sparsity — making the practical significance of joint interactions an empirical question that our ablation directly tests. A further open question is whether learned sparsity predictors trained on short calibration sequences generalize to long-context settings — SVD Contextual Sparsity Predictors (arXiv 2603.14110) explicitly found that learned predictors suffer from out-of-distribution sensitivity compared to weight-structure-based approaches, making long-context evaluation essential for any learned predictor method.
31	
32	## Opportunity / Why Now
33	
34	The landscape reveals four actionable opportunities. First, the composition question: SPON's static bias correction fixes average-case representational drift (input-independent) while contextual prediction handles per-input variation (input-dependent) — orthogonal mechanisms that should provide additive benefits. Note that IFPruning (arXiv 2501.02086) also combines quasi-static (instruction-level) and dynamic (input-level) sparsity, but through a fundamentally different mechanism: a 302M-parameter predictor that jointly fine-tunes the base LLM with cross-entropy loss, producing instruction-level masks (same mask for all tokens). Our composition is between an input-independent bias correction (zero overhead, folded into bias terms, applied to frozen models) and a lightweight token-level contextual predictor — a simpler, more modular, and post-training-compatible approach. If confirmed empirically, the SPON + contextual predictor composition becomes a practical recipe with a clear mechanistic explanation. Second, the training objective question: if a KL-trained predictor (no compensation) matches or exceeds the quality of FastForward's full BCE + compensation system, the practical benefit is substantial — a simpler inference pipeline with lower overhead. FastForward's compensation MLP adds ~8.0 MB of weights per layer (r'=d_model/8=512; 4,194,304 params in FP16) and associated GEMV operations at inference time — ~256 MB total across 32 layers; eliminating it simplifies deployment without sacrificing quality. This transforms the contribution from 'KL is slightly better than BCE' to 'KL training makes error compensation unnecessary.' Third, we observe that BCE's per-neuron decomposition L_BCE = Σ_j l(y_j, s_j) is analogous to a mean-field factorization that treats each neuron's activation decision as independent, ignoring joint interaction effects. At sparsity level s, the number of simultaneously pruned neuron pairs scales as O(s²D²), so the approximation gap grows quadratically with sparsity — yielding a testable prediction that KL's advantage should be substantially larger at 50% than at 40% sparsity. We note that this is an information-theoretic analogy rather than a formal variational inference procedure: BCE predictors achieve high per-neuron accuracy (>99% in DejaVu at moderate sparsity on ReLU models), so the practical significance of the interaction terms is an empirical question — which is exactly what the sparsity-level ablation tests. If confirmed, this provides actionable guidance: use KL when targeting aggressive sparsity levels where joint interactions dominate; BCE may suffice at conservative levels. Fourth, long-context generalization: learned sparsity predictors are trained on short calibration sequences, but deployed on inputs of arbitrary length. SVD Contextual Sparsity Predictors (arXiv 2603.14110) showed that learned predictors exhibit out-of-distribution sensitivity — our LongBench and MT-Bench evaluation directly tests whether KL-trained predictors (which optimize for output-distribution preservation rather than per-neuron pattern matching) exhibit better generalization than BCE-trained ones, and whether SPON's static correction provides a context-length-invariant baseline that stabilizes long-context performance. If time permits, RULER's synthetic tasks (needle-in-a-haystack retrieval, variable tracking, multi-hop tracing) at controlled context lengths provide fine-grained diagnostics complementing LongBench's natural-language tasks. The contribution is fivefold: (1) the first empirical study of whether static bias correction (SPON) and contextual prediction compose additively for activation sparsity — the headline result; (2) a controlled four-condition ablation (BCE, BCE+compensation, KL, KL+compensation) testing whether KL training subsumes error compensation; (3) a testable interaction prediction (KL advantage grows with sparsity) grounded in the analogy between BCE's per-neuron decomposition and mean-field factorization, with appropriate caveats about the empirical nature of the question; (4) a systematic three-tier comparison (training-free, static-learned, contextual-learned) on native SwiGLU at decode time with honest wall-clock overhead reporting; and (5) long-context generalization evaluation testing whether learned predictors trained on short sequences maintain quality on LongBench tasks (4K–32K tokens) and MT-Bench, addressing a gap identified by recent work on predictor OOD sensitivity.
35	
36	## Landscape (SOTA & Limitations)
37	
38	Training-free activation sparsity on SwiGLU has rapidly progressed: WINA (ICLR 2026) achieves the training-free SOTA with weight-informed scoring and TEAL's greedy per-layer sparsity allocation across both MLP and attention layers, reporting 59.57% average on Llama-3-8B at 50% model-level sparsity versus 66.38% dense; La RoSA (ICML 2025) uses layerwise orthogonal rotations with top-K selection to achieve consistent model-level sparsity (0.17 perplexity gap on Llama-2-7B at 40% sparsity, 1.30x wall-clock speedup), surpassing TEAL by 1.77% on zero-shot tasks without training or magnitude-based pruning; WAS (EMNLP 2025) achieves 60% model-level sparsity via weight-aware scoring with constrained Bayesian optimization; WiSparse (arXiv 2026) preserves 97% of dense performance at 50% sparsity via weight-aware mixed-granularity allocation; TEAL (ICLR 2025) achieves 40-50% sparsity with 1.5-1.8x speedup via magnitude pruning with greedy per-layer allocation; R-Sparse (ICLR 2025) achieves 50% model-level sparsity via rank-aware input channel scoring; ActTail (arXiv 2026) uses Heavy-Tailed Self-Regularization for global sparsity allocation; DIP (MLSys 2025) achieves predictor-free dynamic pruning on SwiGLU at ~40% speedup plus LoRA adapters trained via logit-matching knowledge distillation (loss function unspecified in paper, likely KL) for accuracy recovery — the closest existing system combining distillation with sparsity, though critically it trains the LoRA recovery module with distillation rather than the sparsity predictor itself, and uses magnitude-based (not predicted) sparsity masks. On the learned side, SPON/Resting Neurons (arXiv 2512.12744v3, ICML 2026 per arXiv metadata updated on the April 30 notification date) injects learnable input-independent activation vectors trained via KL-divergence distillation, recovering ~1 point over WINA at 50% model-level sparsity on five QA benchmarks (ARC-Challenge, ARC-Easy, BoolQ, PIQA, Winogrande; 71.96 vs 70.97), with zero inference overhead since vectors fold into bias terms, training in ~1 hour on 4x A6000; SPON also reports perplexity on WikiText and validates cross-dataset generalization by calibrating on C4 while evaluating on WikiText. FastForward (arXiv 2602.00397, Jan 2026) trains a contextual predictor (single-head attention + 2-layer MLP, bottleneck r=d_model/16) with weighted BCE loss plus an error compensation network (2-layer MLP, r'=d_model/8=512) trained with MSE loss ||Y_dense − Y_sparse||², achieving MMLU 67.17 vs dense 67.84 at 50% FFN sparsity on Llama-3.1-8B — critically, the compensation network operates at inference time (not just training), adding ~8.0 MB per layer (4,194,304 params × 2 bytes FP16, ~256 MB total across 32 layers) in per-layer weight reads and compute overhead. FastForward targets prefill optimization and evaluates on LongBench (English tasks, 4K-32K tokens) achieving <6% accuracy loss at 50% FFN sparsity — demonstrating that their predictor generalizes beyond short training sequences via an attention-mixing mechanism, but requiring the compensation network for this generalization. IFPruning (arXiv 2501.02086, Jan 2025) trains a 302M-parameter sparsity predictor that combines instruction-level (quasi-static) and input-level (contextual) sparsity selection, jointly optimizing the predictor and LLM weights via cross-entropy loss. While IFPruning also composes static and contextual sparsity components, it operates at a fundamentally different granularity and setting: instruction-level masks (same mask for all tokens in a sequence) requiring task-description input, a large predictor (302M params vs our ~75.5M total), and joint LLM fine-tuning that modifies the base model — whereas our composition applies input-independent bias correction (zero overhead, folded into bias terms) with token-level contextual prediction, both post-training on frozen models. ShadowLLM (EMNLP 2024) trains single-hidden-layer predictors using MSE loss on per-neuron importance. Sirius (NeurIPS 2024) addresses quality degradation from contextual sparsity via periodic full-model correction every 16 tokens with speculative-decoding-style rollback, achieving 20-35% latency reduction — a complementary approach to our static+contextual composition since Sirius interleaves sparse and dense inference rather than composing learned correction mechanisms. Spark Transformer (NeurIPS 2025) reparameterizes existing FFN weights and attention key embeddings during pre-training (Gemma-2 recipe) to form implicit sparsity predictors with a hardware-friendly 'statistical top-k' linear-time approximate algorithm, achieving 2.5x FLOP reduction with 1.79x CPU / 1.40x GPU decode speedup and only 8% of FFN neurons activated — complementary to our post-training approach which works on frozen models without pre-training modification. ActiveFlow (arXiv 2025) combines cross-layer preloading with sparse-aware self-distillation using KL-divergence to adapt model weights (not predictor parameters) for on-device deployment, demonstrating that KL-based training recovers 2.64-10.21% accuracy over TEAL — further evidence that output-distribution distillation is effective for sparsity recovery, though applied to weight adaptation rather than predictor training. Polar Sparsity (NeurIPS 2025) trained BCE routers and evaluated on LongBench for instruction-tuned models, concluding MLP sparsity offers limited benefits on SwiGLU in batch-scaling scenarios — however, this was with activation-pattern prediction, not output-distribution alignment in low-batch decode; their long-context evaluation was limited to 16K tokens. MaskLLM (NeurIPS 2024 Spotlight) uses Gumbel Softmax for static 2:4 masks. SDMPrune (arXiv 2025) uses self-distillation for MLP weight pruning, not activation sparsity. SVD Contextual Sparsity Predictors (arXiv 2603.14110, Mar 2026) provide training-free predictors using truncated SVD of gate projections, targeting ReGLU-based models with high inherent sparsity — critically, they found that learned predictors suffer from out-of-distribution sensitivity on unseen data (ROC-AUC degrades on held-out sequences) while SVD predictors maintain robust performance by leveraging weight structure rather than data-dependent patterns. This OOD sensitivity finding directly motivates our LongBench evaluation: if learned predictors are fragile to distribution shift, their behavior on long-context tasks (absent from short calibration data) is an important empirical question. No prior work (a) trains the sparsity predictor itself with KL-divergence distillation, (b) tests whether SPON's static correction composes additively with contextual prediction in a post-training, frozen-model setting, (c) empirically tests whether KL's advantage over BCE grows with sparsity level (with a clear hypothesis grounded in BCE's per-neuron independence assumption), or (d) evaluates whether KL-trained predictors generalize better than BCE-trained ones on long-context tasks.
39	
40	## Proposed Approach
41	
42	We study the composition of two learned correction mechanisms for activation sparsity — static bias correction and contextual prediction — trained via output-distribution distillation (KL divergence) on native SwiGLU LLMs at decode time, with a controlled four-condition ablation testing whether KL training subsumes error compensation. For each SwiGLU MLP block in Llama 3.1 8B (32 layers, d_model=4096, intermediate_size=14336), we attach a low-rank predictor that maps the layer input hidden state h ∈ R^d to a continuous sparsity score over the intermediate dimension D via two linear projections: h → W_down (4096 × 128) → ReLU → W_up (128 × 14336), yielding ~2.36M parameters per layer (~75.5M total, <1% of 8B model). Architecture is fixed at rank r=128 (no rank sweep, following reviewer guidance to narrow scope). During training, scores are converted to differentiable binary masks via Gumbel-sigmoid relaxation with temperature annealing (τ: 5 → 0.1). The primary training loss is: L = KL(p_dense || p_sparse) + λ_mse · MSE(h_dense_l, h_sparse_l) + λ_sparse · max(0, s − s_target), where KL divergence on output logits is the primary signal (capturing joint neuron interactions through end-to-end gradient flow via ∂L_KL/∂θ = ∂L_KL/∂p_sparse · ∂p_sparse/∂h_out · ∂h_out/∂m · ∂m/∂θ), per-layer MSE provides gradient signal for early layers, and the sparsity penalty enforces target model-level sparsity s_target = 0.5. Only predictor parameters are updated during ~1K gradient steps on SlimPajama calibration data with the base LLM frozen. MLP/attention sparsity allocation: We use TEAL's greedy per-layer allocation algorithm (also adopted by WINA) to distribute the 50% global FLOPs budget across all layers. The algorithm iteratively increases sparsity in the least-sensitive layer (measured by calibration perplexity impact) until the aggregate meets the global target. The exact per-layer and per-component (MLP, attention) sparsity ratios are determined by this calibration-based optimization — we do not impose any fixed ratio between MLP and attention sparsity. We report both the global model-level sparsity (50%) and the effective per-component sparsity ratios resulting from the allocation, ensuring transparent comparison with baselines that may use different allocation strategies. Within MLP layers, our contextual predictor replaces WINA's heuristic scoring to determine which neurons to activate; within attention layers, WINA's original weight-informed scoring is used unchanged. At inference, the predictor produces a binary mask via top-k selection, and the sparse SwiGLU forward pass skips columns of gate/up projections and rows of the down projection using Triton sparse GEMV kernels from the TEAL/WINA codebases. Predictor overhead — FLOPs and wall-clock (honest reporting): Each predictor adds ~4.72M FLOPs per layer (two GEMVs of 4096×128 and 128×14336) versus ~176M FLOPs saved at 50% MLP sparsity — a ~37:1 FLOPs ratio. However, batch=1 decode is memory-bandwidth-bound, not compute-bound. On H100 (3.35 TB/s peak HBM bandwidth), the small predictor GEMVs achieve only ~100 GB/s effective bandwidth due to low matrix occupancy and kernel launch overhead, yielding ~0.047 ms per layer or ~1.5 ms total predictor overhead across 32 layers. The larger FFN matrices being skipped achieve ~500 GB/s effective bandwidth, yielding ~0.35 ms savings per layer or ~11.3 ms total savings. The realistic wall-clock savings-to-overhead ratio is approximately 4-8:1 — still attractive for decode acceleration, but substantially lower than the 37:1 FLOPs ratio. We report both metrics throughout to avoid misleading claims. Four-condition ablation (the key experimental design addition): (a) BCE only — our predictor architecture trained with weighted BCE loss (FastForward-style exponential weighting), no compensation; (b) BCE + error compensation — same BCE predictor plus FastForward's 2-layer compensation MLP (r'=d_model/8=512, adding ~8.0 MB per layer: W_comp1 ∈ R^{4096×512} + W_comp2 ∈ R^{512×4096} = 4,194,304 params × 2 bytes FP16), trained with MSE loss ||Y_dense − (Y_sparse + g_φ(h))||², with compensation network active at inference time; (c) KL only — our predictor trained with KL-divergence loss, no compensation; (d) KL + error compensation — if time permits. Condition (b) is critical: it replicates FastForward's full approach (BCE + compensation) rather than testing BCE in isolation, ensuring a fair comparison. If KL-only (c) matches or exceeds BCE+compensation (b), the finding is that KL training makes error compensation unnecessary — yielding a simpler system with lower inference overhead (eliminating ~256 MB of compensation weights and associated compute across 32 layers). Evaluation benchmarks (aligned with user requirements): (1) Perplexity on WikiText-2 and C4 — standard for sparsity papers, reported by SPON and most training-free baselines, trivial to compute; (2) ARC-Challenge — science reasoning; (3) WinoGrande — coreference resolution; (4) MMLU — multitask knowledge; (5) GSM8K — mathematical reasoning; (6) HumanEval — code generation; (7) MT-Bench — multi-turn instruction-following quality under sparsity, evaluated using GPT-4 as judge (80 questions, 8 categories), testing whether sparsity disproportionately degrades open-ended generation; (8) LongBench (English subset) — long-context evaluation (4K-32K tokens) testing predictor generalization beyond training distribution, directly comparable to FastForward's LongBench results. Core evaluation: perplexity + 5 discriminative benchmarks + LongBench + MT-Bench (8 benchmarks). Conditional extension: if time permits, we add RULER (COLM 2024) — synthetic long-context evaluation with 13 tasks across 4 categories (Retrieval, Multi-hop Tracing, Aggregation, QA) at 2 context lengths (4K, 16K), providing fine-grained capability-level diagnostics that complement LongBench's aggregate scores. RULER is valuable but not essential for the paper's core claims; prioritizing the four-condition ablation + composition + LongBench ensures the key experiments are completed. This benchmark set covers all user-required evaluation axes: perplexity, knowledge/reasoning (MMLU, ARC-c, GSM8K), code (HumanEval), long-context (LongBench, optionally RULER), and instruction-following (MT-Bench). Long-context generalization: The predictor is trained on SlimPajama calibration sequences (typically 2048 tokens). LongBench tasks require processing 4K-32K token inputs, testing whether learned neuron importance patterns generalize beyond the training context length. SVD Contextual Sparsity Predictors (arXiv 2603.14110) found that learned predictors suffer OOD sensitivity on unseen data, making this a plausible failure mode. If long-context performance degrades disproportionately, this is itself a finding — motivating context-length-aware predictor training or hybrid approaches where static SPON correction (which is context-length-invariant by construction) provides a robust baseline while contextual prediction adapts to input-specific patterns. FastForward reports their predictor generalizes to LongBench via an attention-mixing mechanism; our four-condition ablation will reveal whether KL-trained predictors (which optimize output-distribution preservation) exhibit different generalization characteristics than BCE-trained ones (which optimize per-neuron pattern accuracy). Experiments focus on Llama 3.1 8B at 50% model-level sparsity as the primary operating point. For the KL-BCE sparsity interaction test, we additionally train KL and BCE predictors at 40% model-level sparsity (2 extra training runs) to test the prediction that KL's advantage over BCE grows with sparsity level. All other baselines and the composition experiment are evaluated at 50% only, saving ~3-4 days versus evaluating at both levels. Baselines use consistent model-level sparsity: training-free baselines are WINA, TEAL, and R-Sparse; learned baselines are SPON (reimplemented — bias vectors + KL training, architecturally trivial, validated by reproducing Table 2 numbers on Llama 3 8B before evaluating on Llama 3.1 8B) and the four-condition ablation above. Key experiments ordered by importance: (1) SPON + KL predictor composition (headline): apply SPON bias correction AND contextual KL prediction simultaneously, testing whether static correction (fixing average-case drift) and contextual prediction (handling per-input variation) provide additive benefits. (2) KL-only vs BCE+compensation: the critical test of whether end-to-end KL training subsumes the need for error compensation — if confirmed, this is the key practical recommendation (eliminating ~256 MB of compensation weights and per-layer GEMV overhead). (3) KL vs BCE sparsity-level interaction: testing at both 40% and 50% whether KL's advantage over BCE (both without compensation) grows with sparsity, confirming the interaction prediction. (4) Three-tier comparison: training-free (WINA, TEAL, R-Sparse) vs static-learned (SPON) vs contextual-learned (ours), establishing marginal value of each tier. (5) Long-context generalization: LongBench evaluation across all conditions, testing whether KL-trained predictors generalize better than BCE-trained ones to long contexts, and whether SPON's static correction stabilizes long-context performance. (6) Per-task analysis: decompose improvements by benchmark type (perplexity vs knowledge/reasoning vs code vs long-context vs instruction-following). Improvement target: 1.5-3 points average recovery over WINA at 50% model-level sparsity (WINA baseline: 59.57 on 6 benchmarks), conservatively grounded in: SPON's ~1 point static recovery (verified on five QA benchmarks), contextual KL prediction contributing an estimated 0.5-1.5 points (conservative — FastForward's near-dense MMLU quality was achieved at FFN-only sparsity with error compensation, a less aggressive operating point than our model-level sparsity without compensation), and a potential 0-0.5 point composition 
43	
44	## Resource Estimate
45	
46	- **auto_research**: {'claude_api_cost': '$160-270', 'estimated_gpu_cost': '$225-350', 'gpu_hours': '~90-140h H100 (predictor at r=128, 50% model-level sparsity primary, 40% for KL-BCE interaction only, four-condition ablation [BCE, BCE+comp, KL, KL+comp], SPON reimplementation + validation, SPON+predictor composition, core evaluations across 8 benchmarks including LongBench long-context and MT-Bench instruction-following, wall-clock profiling; RULER conditional)', 'gpu_utilization': 'High (~80-90%)', 'risk_note': "Timeline is tight with 14 days remaining. Primary execution risk: validating SPON reimplementation (must reproduce published Llama-3-8B Table 2 numbers on QA benchmarks before proceeding). Mitigation: SPON is architecturally trivial (bias vectors + standard KL training, ~1 hour on 4× A6000). Secondary risk: LongBench evaluation time on long sequences — mitigated by selecting the English-language subset (matching FastForward's evaluation protocol) and parallelizing evaluation across GPUs. Tertiary risk: MT-Bench requires GPT-4 judge API calls — mitigated by low cost (~$5-10 for 80 questions × multiple configurations) and fast turnaround. Quaternary risk: implementing FastForward's compensation MLP for the ablation — mitigated by simple 2-layer MLP architecture (d_model → d_model/8 → d_model with MSE loss). Quinary risk: Triton sparse kernel integration — mitigated by using existing TEAL/WINA kernel codebases. RULER risk: mitigated by making it conditional — core claims do not depend on RULER results. Fallback plan: if SPON reproduction takes >2 days, use SPON's published numbers on the QA subset and note the benchmark-set difference. If LongBench evaluation runs over schedule, prioritize single-document QA and summarization subtasks. Paper writing risk: 3 days allocated; structure and related work can be drafted in parallel with experiments.", 'speed_bottleneck': 'Single-GPU training on 8B model; LongBench evaluation on long sequences (4K-32K tokens) at batch=1 decode is the primary bottleneck. Narrowing to 50% primary sparsity (40% only for 2 interaction runs), dropping rank sweep, and making RULER conditional saves ~30% versus earlier proposals. Explicit 3-day paper writing buffer prevents timeline overrun.', 'team': '0 (initial 2-4h setup for codebase scaffolding and GPU provisioning)', 'timeline': '14 days total with 2-4 H100s running concurrently: Days 1-2: codebase scaffolding, SPON validation, MT-Bench/LongBench evaluation pipeline setup. Days 3-6: train 4 ablation conditions at 50% + 2 interaction runs at 40%. Days 7-9: SPON+KL composition, all core evaluations including perplexity (WikiText-2, C4), discriminative benchmarks (ARC-c, WinoGrande, MMLU, GSM8K, HumanEval), LongBench (English subset, 4K-32K tokens), MT-Bench (80 multi-turn questions with GPT-4 judge). Days 10-11: wall-clock profiling, long-context analysis, figure generation; conditionally run RULER (2 context lengths × 3 representative tasks) if schedule permits. Days 12-14: paper writing with auto assistance — feasible for May 25 ARR deadline. Note: LongBench evaluation on long sequences at batch=1 decode adds ~8-12h of GPU time; MT-Bench adds ~2-3h including judge API calls.'}
47	- **human_in_loop**: {'claude_api_cost': '$60-110', 'estimated_gpu_cost': '$170-265', 'gpu_hours': '~68-105h H100', 'gpu_utilization': 'Moderate (~40-55%)', 'team': '1 researcher, ~30min/day review', 'timeline': '2.5-3 weeks (including paper writing)'}
48	- **manual**: {'estimated_gpu_cost': '$170-240', 'gpu_hours': '~68-95h H100', 'gpu_utilization': 'Low (~15-25%)', 'team': '1 ML researcher', 'timeline': '3-4 weeks (including paper writing)'}
49	
50	## Key References
51	
52	- Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time (ICML 2023)
53	- CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models (COLM 2024)
54	- RULER: What's the Real Context Size of Your Long-Context Language Models? (COLM 2024, arXiv 2404.06654)
55	- MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models (NeurIPS 2024 Spotlight)
56	- ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models (EMNLP 2024)
57	- Sirius: Contextual Sparsity with Correction for Efficient LLMs (NeurIPS 2024)
58	- Instruction-Following Pruning for Large Language Models (IFPruning, arXiv 2501.02086, Jan 2025)
59	- TEAL: Training-Free Activation Sparsity in Large Language Models (ICLR 2025)
60	- R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference (ICLR 2025)
61	- La RoSA: Enhancing LLM Efficiency via Layerwise Rotated Sparse Activation (ICML 2025)
62	- DaSS: Dependency-Aware Semi-Structured Sparsity of GLU Variants in Large Language Models (TMLR 2025)
63	- Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking (DIP, MLSys 2025)
64	- SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity (ICML 2025)
65	- WAS: Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling (EMNLP 2025)
66	- Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity (NeurIPS 2025)
67	- Spark Transformer: Reactivating Sparsity in FFN and Attention (NeurIPS 2025)
68	- Scaling Up On-Device LLMs via Active-Weight Swapping Between DRAM and Flash (ActiveFlow, arXiv 2504.08378)
69	- Resting Neurons, Active Insights (SPON): Improving Input Sparsification for Large Language Models (ICML 2026 per arXiv metadata, arXiv 2512.12744v3)
70	- FastForward: Accelerating LLM Prefill with Predictive FFN Sparsity (arXiv 2602.00397, Jan 2026)
71	- WINA: Weight Informed Neuron Activation for Accelerating Large Language Model Inference (ICLR 2026)
72	- WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity (arXiv 2026)
73	- ActTail: Global Activation Sparsity in Large Language Models (arXiv 2026)
74	- SVD Contextual Sparsity Predictors for Fast LLM Inference (arXiv 2603.14110, Mar 2026)
75	
76	## Reviewer Evaluation
77	
78	**Scores**:
79	  - clarity: **{'rationale': 'Exceptionally well-written after 9 rounds of revision. The four-condition ablation design is crystal clear. The mean-field analogy is properly caveated. The improvement target arithmetic (1 SPON + 0.5-1.5 contextual + 0-0.5 composition = 1.5-3 points) is transparent and internally consistent. Explicit fallbacks for each potential negative result demonstrate mature experimental planning. Wall-clock vs FLOPs overhead is honestly reported.', 'score': 5}**/5
80	  - feasibility: **{'rationale': "The 14-day timeline with 9 benchmarks, 6 training runs, SPON reimplementation+validation, and 3-day paper writing is extremely tight. RULER being conditional is pragmatic but may leave user requirements unmet. The 90-140 H100-hour estimate is within the 200h budget but assumes zero debugging setbacks. SPON reimplementation risk is real — even 'architecturally trivial' methods can take days to validate. The compensation network weight calculation (8.0 MB per layer) and wall-clock analysis (4-8:1 ratio) are now honest and well-grounded.", 'score': 3}**/5
81	  - impact: **{'rationale': 'If KL-only matches BCE+compensation, the practical impact is significant — eliminating ~256 MB of compensation weights per model simplifies deployment substantially. The composition recipe (SPON + KL predictor) would provide actionable guidance for practitioners. The three-tier comparison (training-free → static-learned → contextual-learned) establishes marginal value at each tier. Long-context generalization results would address a real deployment concern identified by SVD Contextual Sparsity Predictors.', 'score': 4}**/5
82	  - novelty: **{'rationale': 'The composition of static bias correction (SPON) with KL-trained contextual predictors is genuinely novel — no prior work combines these in a post-training frozen-model setting. The four-condition ablation (BCE, BCE+compensation, KL, KL+compensation) testing whether KL subsumes error compensation is a well-designed experiment with clear practical implications. The mean-field analogy is now appropriately caveated. However, the individual components (KL distillation, contextual predictors, bias correction) are all established — the novelty is in their composition and systematic comparison.', 'score': 4}**/5
83	
84	## Human Review Note
85	
86	## Agent 审核结果（完整三阶段 pipeline）
87	
88	**Verdict**: PASS
89	
90	**入口三重共识 (X)**: 24.0%
91	**终审自评 (Y)**: 36.0%
92	**出口三重共识 (Z)**: 30.0%
93	**Z 区间**: [26.0%, 35.0%]
94	**真实提升 (Z-X)**: +6.0 pp
95	**幻觉幅度 (Y-Z)**: +6.0 pp
96	**出口一致性**: 高（std=1.15%，远低于 3% 阈值）
97	**出口三次评估**: [30.0, 30.0, 32.0]
98	
99	### 优化方案 / 拒绝详情
100	【优化方案】
101	
102	1. **[标题 / 摘要 / Introduction] — 将 narrative 主线从三条平行贡献线收束为单一 headline question: "Does KL distillation eliminate the need for error compensation networks in activation sparsity?"** — [Clarity + Significance]
103	   原始 proposal 同时推进 composition additivity、KL-vs-BCE scaling、KL subsumes compensation 三条线，缺乏 reviewers 能在 30 秒内复述的 takeaway。修改后以一个 binary、falsifiable、有直接工程后果（省 ~256MB）的问题为主线，composition framework 和 scaling analysis 作为支撑贡献。同时将 value proposition 从 "recovery magnitude" 转向 "principled understanding of when and why KL outperforms BCE + modular design principles for correction stacking"，更适合中等效果量的论文。
104	
105	2. **[Theoretical Motivation 段落] — 将 BCE mean-field 从 "information-theoretic analogy" 升级为 gradient structure 的数学事实 + mean-field / variational inference 概念 framing** — [Novelty + Soundness]
106	   原始 proposal 仅用一句 "analogous to a mean-field factorization" 带过，自我降调为 "practical significance is an empirical question"。修改后明确写出：(a) BCE 梯度 ∂L_BCE/∂s_j 只依赖第 j 个 neuron（factorized，mean-field），KL 梯度 ∂L_KL/∂s_j 通过 ∂logits/∂h · ∂h/∂m 耦合所有 active neurons（coupled，考虑联合分布）——这是梯度结构的数学性质而非类比；(b) 将 BCE 对应为独立 Bernoulli 假设，KL 对应为考虑联合分布的推断，借用 ML 社区成熟的 mean-field vs variational inference 认知框架；(c) 给出 first-order Taylor expansion 下的 approximate analysis，明确 notation（s = sparsity ratio, D = FFN intermediate dimension），推导 cross-term scaling O(s²D²)，诚实标注为 approximate bound。
107	
108	3. **[Theoretical Motivation 段落] — 提出定量可证伪预测：KL-vs-BCE 性能差距近似按 s² 二次增长，偏离程度量化 higher-order interaction 的贡献** — [Novelty + Soundness]
109	   原始 proposal 仅有定性预测（"KL's advantage over BCE grows with sparsity"）。修改后将预测精确化为 s² 二次 scaling curve，同时预注册：偏离二次曲线的程度（线性、更陡、phase transition）本身是 informative 的发现。同时加入 Taylor expansion accuracy test——在各 sparsity level 下直接测量 actual output perturbation vs first-order Taylor prediction，诚实报告 approximation 的有效范围。如果 first-order 在 >40% sparsity 误差大，降低理论 claim 为 "directional intuition, empirically validated by sweep"。
110	
111	4. **[Methodology / Framework 段落] — 引入 formal modular decomposition framework: static c_s ⊕ contextual c_θ(x)，定义正交性条件和 additive composition 充分条件** — [Novelty]
112	   原始 proposal 将 SPON + contextual predictor 的组合描述为具体实验，无框架性贡献。修改后将其形式化为可复用的分解框架：任何 correction mechanism 可沿 static-vs-contextual 轴分类并在此框架内组合。Additive composition 成立的条件（output-space interaction term negligible）被显式定义，使 composition 不再是 ad hoc 叠加而是有理论支撑的 design principle。
113	
114	5. **[Related Work / Framework] — 引入二维 taxonomy: x 轴 correction granularity（static → per-layer → per-token → per-neuron）, y 轴 training signal coupling（decomposed/BCE → intermediate/MSE → coupled/KL）** — [Novelty + Significance]
115	   原始 proposal 按时间顺序列举 prior work，缺乏组织结构。修改后用二维坐标系将 WINA, SPON, FastForward, IFPruning, 本文方法投射到具体位置，明确指出文献中的空白象限及其原因。这是零实验成本的 conceptual contribution，让 reviewer 读完 related work 后感觉"对这个领域的理解变清晰了"。
116	
117	6. **[Related Work] — 加入 training signal taxonomy: KL（output-level coupled）→ MSE（intermediate-level）→ BCE（per-unit decomposed）** — [Related Work + Soundness]
118	   原始 proposal 未讨论为什么只比较 KL 和 BCE。修改后明确说明 KL 和 BCE 代表 training signal spectrum 的两个端点（fully coupled vs fully decomposed），是 most informative comparison。MSE 列为 extension experiment。
119	
120	7. **[Related Work] — 大幅扩展相关工作覆盖** — [Related Work]
121	   原始 proposal 仅覆盖 WINA/TEAL/R-Sparse/La RoSA、SPON、FastForward、IFPruning。修改后增加：(a) KD literature（DistilBERT, TinyBERT）——KL 在 weight pruning/KD 中已知有效，但 activation sparsity masking predictor 训练是不同场景（binary gating, post-training, frozen weights）；(b) weight pruning mask learning（movement pruning, Diff pruning）——关键区别是 activation mask 是 input-dependent per-token 而 weight mask 是 static；(c) MoE routing parallel（Expert Choice Routing, Gumbel-softmax vs Gumbel-sigmoid）——降至 discussion/future direction 而非 contribution claim；(d) system-level alternatives（PowerInfer, TurboSparse offloading）——本文聚焦 on-device single-GPU 场景；(e) ReLU-fication 路径（ReluLLaMA, SiReLU）——替代范式，需 retraining，本文是 post-training；(f) 明确 DejaVu >99% per-neuron accuracy 是在 ReLU 模型（OPT-175B）上测得，SwiGLU 模型 sparsity structure 根本不同，数据不直接可比。
122	
123	8. **[Framing / Scope] — 将 "end-to-end vs surrogate loss for discrete gating" 的通用 framing 收窄回 "activation sparsity for SwiGLU LLMs"，跨领域类比降至 Discussion** — [Soundness，防 overclaiming]
124	   Round 2 曾扩大 framing 至 MoE/pruning/early-exit 通用问题，但所有实验仅在 activation sparsity 一个 setting 进行，构成 overclaiming 风险。修改后 title/abstract/intro scope 限定为 activation sparsity，跨领域 implications 作为 Discussion 中的 future direction 提出而非 contribution claim。
125	
126	9. **[实验设计 — 核心] — 加入 STE (Straight-Through Estimator) baseline 作为 core experiment** — [Soundness]
127	   原始 proposal 未讨论 Gumbel-sigmoid relaxation 的选择。修改后在 KL-only condition 上加入 STE baseline（一个额外 training run），隔离 "KL 的优势是来自 loss function 还是 Gumbel relaxation 的 side effect"。这是必要的 confound control——如果没有它，reviewer 可以用 "gains from relaxation not loss" 一句话否决核心论点。
128	
129	10. **[实验设计 — 核心] — 加入 iso-compute KL vs BCE 对比，报告 per-step training FLOPs 和 total training time** — [Soundness，防致命质疑]
130	    原始 proposal 完全未讨论 KL 和 BCE 的训练成本差异。KL 需要 full model forward pass 计算 output logits，BCE 可用预计算缓存的 per-neuron ground truth。如果 KL 优势仅来自"用了更多计算"，结论 trivially true。修改后明确报告两者的 training FLOPs，并加入 iso-compute 对比（给 BCE 等量额外 training steps），在等计算条件下比较。这消除了一个可能导致论文被一句话否决的方法论漏洞。
131	
132	11. **[实验设计 — 核心] — 加入 output-space superposition linearity test 作为 additive composition 的主要验证** — [Soundness]
133	    原始 proposal 未包含任何 composition 验证。Round 1 加入的 cosine similarity 在参数空间进行，但参数空间低相关 ≠ output 空间独立性。修改后用 output-space linearity test（‖Δlogits(s+c) - Δlogits(s) - Δlogits(c)‖ vs individual magnitudes）作为主要 evidence，cosine similarity 降为 supplementary。Per-layer orthogonality spectrum + TEAL sensitivity correlation 作为 secondary analysis 保留。
134	
135	12. **[实验设计 — 核心] — 加入完整 outcome space analysis（四象限 dual-outcome 设计）** — [Soundness + Significance]
136	    原始 proposal 无 null result 讨论。修改后显式覆盖四种可能结果：(i) KL-only ≥ BCE+comp → 主结论成立；(ii) KL-only < BCE+comp 但 KL+comp > BCE+comp → KL 有增量价值但不消解补偿；(iii) KL ≈ BCE → mean-field sufficient 的 negative result，对社区有价值；(iv) 组合负干涉 → 揭示 correction 冗余/冲突模式。确保论文无论结果如何都有贡献。特别强调 outcome (iii) 作为同等重要的发现——如果 BCE 的 factorized gradient 在实践中足够好，这才是反直觉的结论。
137	
138	13. **[实验设计 — Sparsity Sweep] — 从 2 个 sparsity levels（40%, 50%）扩展到 7 个（30/35/40/45/50/55/60%）** — [Soundness + Analysis Depth]
139	    原始 proposal 仅在 40% 和 50% 做 KL-vs-BCE 对比。修改后扩展至 7 个水平（仅需调整 sparsity allocation，不需额外模型训练），增强 trend analysis 的统计 power，支撑 s² scaling prediction 的 curve fitting，并可能揭示 phase transition。
140	
141	14. **[实验设计 — 模型] — 加入 Mistral-7B-v0.3 作为 generalization validation（核心子集：perplexity + ARC-c + MMLU）** — [Soundness]
142	    原始 proposal 仅在 Llama 3.1 8B 单一模型上实验。修改后增加不同架构（GQA + sliding window attention）的第二模型验证，在核心 benchmark 子集上检验 findings 是否 transfer。Scale beyond 7-8B 列为 explicit limitation + theoretical prediction（更大模型 higher D → larger cross-terms → 可能 amplify KL advantage，但 parameter redundancy may counteract）。
143	
144	15. **[实验设计 — 统计] — 升级统计方案：headline comparison 5 seeds，其余 3 seeds，paired bootstrap + effect size（Cohen's d）** — [Soundness]
145	    原始 proposal 无统计 rigor 提及。修改后 KL-only vs BCE+comp 使用 5 seeds 保证足够统计 power，其余条件 3 seeds。报告 mean ± std，paired bootstrap significance tests，Spearman rank correlation for sparsity trend，Cohen's d effect size。
146	
147	16. **[实验设计 — Efficiency] — 加入 efficiency-accuracy Pareto frontier 分析 + quantization 正交性声明 + scope 限定** — [Significance + Soundness]
148	    原始 proposal 未包含 Pareto analysis，也未提及 quantization 正交性。修改后在同一 plot 展示各方法的 accuracy vs inference overhead（FLOPs/memory/latency），论证 KL-only（无 compensation network）在 Pareto frontier 的独特位置——comparable accuracy, significantly less overhead。明确 "activation sparsity orthogonal to and composable with weight quantization (INT4/INT8)"，scope 限定为 memory-bound autoregressive decode (batch ≤ 4)。
149	
150	17. **[实验设计 — 分析] — LongBench per-task-type breakdown 和 token-level linguistic disagreement analysis 作为 secondary/supplementary** — [Analysis Depth + EMNLP Venue Fit]
151	    原始 proposal 仅报告 aggregate LongBench 分数。修改后按 task type 分拆报告（single-doc QA, multi-doc QA, summarization, few-shot, code），分析 KL predictor 是否有 task-dependent generalization patterns。Token-level linguistic analysis（mask disagreement tokens 按 frequency rank, syntactic depth, dependency distance 归类）保留为 appendix-level supplementary analysis，不升格为核心贡献以避免 scope 分散。
152	
153	18. **[实验设计 — Scope Management] — 明确 core / secondary / extension 三层实验优先级** — [Feasibility]
154	    原始 proposal 无优先级区分。修改后明确：**Core**（四条件 ablation + STE baseline, 7-level sparsity sweep, output-space composition test, iso-compute comparison, Taylor accuracy test, Llama 8B full benchmark + Pareto analysis）；**Secondary**（Mistral-7B core subset, LongBench per-task breakdown, per-layer orthogonality spectrum）；**Extension/if-time-permits**（RULER, hidden-state MSE baseline, token-level linguistic analysis, additional seeds for non-headline comparisons）。实现建立在 SPON 和 FastForward 的 released codebases 上。
155	
156	【主要风险】: 
157	
158	1. **Novelty 天花板不可消除**: 本文无新算法、无新架构，核心是 existing components 的 systematic composition + loss function 替换 + controlled ablation。尽管 framing（二维 taxonomy, formal decomposition framework, mean-field/VI 概念框架, s² quantitative prediction）已做到该天花板下接近最优，但 reviewer 仍可能给出 "incremental engineering / confirmatory study" 的 novelty 评价。这是结构性风险，无法通过进一步 proposal 优化消除——只有实验结果本身（surprising scaling pattern, phase transition, 或 null result 颠覆 KD 领域已有直觉）才能突破此天花板。
159	
160	2. **Effect size uncertainty + iso-compute 条件下 KL 优势可能消失**: 如果 KL-only vs BCE+comp 在 iso-compute 条件下差异不显著，论文从 "KL subsumes compensation" 退化为 "KL and BCE comparable under equal compute"——outcome space analysis 保证了这仍是有价值的 negative result，但 impact 和 narrative strength 降档明显。
161	
162	【实施评估】:
163	- **计算资源**: 需要 1-2 块 H100 或 A100-80GB GPU。核心训练：5 conditions（BCE-only, BCE+comp, KL-only, KL+comp, KL+STE）× 5 seeds（headline）或 3 seeds（others）× 32 layers predictor training on Llama 3.1 8B ≈ 每 condition ~2-4 GPU-hours（rank-128 predictor ~2.36M params/layer 训练快），总 core training ~40-8
164	
165	
166	## MVP Validation Results
167	
168	- **Date**: 2026-05-15
169	- **Hypothesis Supported**: Yes
170	
171	### Key Metrics
172	
173	KL sparse PPL: 12.52 ± 0.92 | BCE sparse PPL: 44.05 ± 0.72 | Δ = 31.53 PPL | KL hard-mask PPL: 9.20 vs true dense: 6.12 | KL per-layer sparsity range: 0.22-0.80 | BCE per-layer: 0.43-0.66 | Seeds: 3 per condition | Model: Llama 3.1 8B | Target sparsity: 50%
174	
175	### Summary
176	
177	KL-divergence output distribution distillation produces dramatically better SwiGLU sparsity predictors than BCE per-neuron training. 3-seed validation at 50% model-level sparsity: KL sparse PPL 12.52 ± 0.92 vs BCE 44.05 ± 0.72 (Llama 3.1 8B, WikiText-2). KL predictor learns non-uniform per-layer sparsity (0.22-0.80) capturing joint neuron interactions, while BCE produces near-uniform allocation (0.43-0.66). KL hard-mask PPL (9.20) approaches true dense (6.12), confirming precise identification of unimportant neurons.
178	
179	### Recommendation
180	
181	GO — 核心假设得到强力支持。KL 训练的优势来自端到端梯度流捕获联合神经元交互，这是一个清晰的研究 story。建议立即进入 research phase：(1) 写 paper_framing.md 定义 claims (2) 四条件 ablation 分离 KL vs compensation 的独立贡献 (3) SPON 组合实验验证加性收益。目标 EMNLP 2026 ARR (DDL 5/25)。
182	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "904286ff-ebb7-4bdb-ab90-995e10934e70"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-16T12:36:50.842Z_

<details><summary>↩ Tool result · `toolu_01Xkn4VPg9gtbxLakCtjnnye`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "5dbcfa90-bde8-4ac3-b3f1-64950930a400"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Searching for notation|symbol|\\\\newcommand|\\\\DeclareMathOperator",
  "usage": {
    "total_tokens": 32524,
    "tool_uses": 12,
    "duration_ms": 9192
  },
  "last_tool_name": "Grep",
  "uuid": "e32be0a3-46b1-4d04-b7ef-573e8822db88",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_012CVrnvxK43YjJGbCx6nMJ6`</summary>

```json
{
  "pattern": "notation|symbol|\\\\newcommand|\\\\DeclareMathOperator",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "type": "tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "22f32bb6-6c1d-4c88-9a1b-b8c6086d00c1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013meVEJAA4Uw2RknTttYdAn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1658,
      "cache_read_input_tokens": 30819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1658,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 48 · 2026-05-16T12:36:51.430Z_

<details><summary>↩ Tool result · `toolu_012CVrnvxK43YjJGbCx6nMJ6`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "698f1abb-d029-42ee-ad72-575266a56689"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Reading paper/experiments.tex",
  "usage": {
    "total_tokens": 49928,
    "tool_uses": 13,
    "duration_ms": 11085
  },
  "last_tool_name": "Read",
  "uuid": "3a24e0e9-f196-4f2c-a8ea-7ac4fc8e3125",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01Q4aa7qshDHjxUDkE7hcwcd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "fa558917-e312-40c9-8430-6a35ef450f70",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RYH7Un5fbEB7Zsn9N2FH5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 17402,
      "cache_read_input_tokens": 32477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17402,
        "ephemeral_1h_input_tokens": 0
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

_source line 51 · 2026-05-16T12:36:53.306Z_

<details><summary>↩ Tool result · `toolu_01Q4aa7qshDHjxUDkE7hcwcd`</summary>

```text
1	\section{Experiments}
2	
3	\subsection{Experimental Setup}
4	
5	\paragraph{Model and Predictor.}
6	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
7	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + Linear($128 \to 14336$), trained to predict activation magnitudes from the FFN input representation.
8	
9	\paragraph{Training.}
10	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \times 10^{-3}$ and cosine decay.
11	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
12	
13	\paragraph{Evaluation.}
14	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
15	
16	\paragraph{Inference Protocol.}
17	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
18	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
19	
20	\paragraph{Baselines.}
21	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
22	
23	
24	\subsection{Main Results}
25	
26	Table~\ref{tab:main} presents the primary comparison across sparsity levels.
27	At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.98, reducing TEAL's degradation from dense (10.97 $\to$ 8.98, an 18\% improvement). % exp_id: kl_30_global_teal
28	Uniform allocation at 30\% yields the lowest PPL (8.82) and notably recovers MMLU to 40.61\%, compared to 38.61\% for TEAL and 25.27\% for KL-global. % exp_id: kl_30_uniform
29	This indicates that at moderate sparsity, the allocation strategy—not the predictor—is the primary lever for knowledge-intensive tasks.
30	
31	At 50\% sparsity, the advantage of KL distillation over vanilla TEAL widens: PPL 11.79 vs.\ 23.31, a 49\% reduction. % exp_id: bench_kl50_global, bench_teal50
32	However, all methods exhibit downstream collapse on MMLU (27.89\% $\approx$ random at 25\%) and GSM8K ($<$2.2\%), indicating a capacity-limited regime where no allocation strategy can recover reasoning ability. % exp_id: kl_50_downstream
33	
34	\begin{table}[t]
35	\centering
36	\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. Best per sparsity level in \textbf{bold}.}
37	\label{tab:main}
38	\small
39	\begin{tabular}{llccccc}
40	\toprule
41	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
42	\midrule
43	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
44	\midrule
45	\multirow{3}{*}{30\%}
46	& TEAL vanilla & 10.97 & \textbf{42.32} & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
47	& KL global (Ours) & 8.98 & 39.68 & \textbf{70.17} & 25.27 & \textbf{8.79} \\ % exp_id: lm_eval_kl_30pct_s42
48	& KL uniform & \textbf{8.82} & 40.78 & 68.59 & \textbf{40.61} & 7.35 \\ % exp_id: bench_kl30_uniform
49	\midrule
50	\multirow{4}{*}{50\%}
51	& TEAL vanilla & 23.31 & 28.41 & 53.04 & 28.32 & 1.97 \\ % exp_id: teal_50_vanilla
52	& KL global (Ours) & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & \textbf{27.89} & 1.29 \\ % exp_id: kl_50_global_teal
53	& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \textbf{2.12} \\ % exp_id: kl_50_uniform
54	& BCE (2700 steps) & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\ % exp_id: bce_isocompute_s42
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	
60	\subsection{Iso-Compute Analysis}
61	\label{sec:isocompute}
62	
63	A natural question is whether BCE training simply requires more compute to converge.
64	We train the BCE predictor for 2700 steps (2.71$\times$ the KL budget) and evaluate under identical TEAL inference.
65	As Table~\ref{tab:main} shows, the BCE predictor at 2700 steps achieves PPL 27.97—still 2.37$\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce_isocompute_s42
66	
67	The failure is structural, not computational.
68	BCE loss decomposes into independent per-neuron gradients, training each neuron's prediction in isolation.
69	This factorized objective cannot learn the inter-neuron correlations required for global top-$k$ allocation, where the keep/prune decision for neuron $i$ depends on the scores of all other neurons across all layers.
70	We observe that BCE training loss saturates early: between steps 500 and 2700, the loss decreases by only 0.006, confirming that additional compute yields diminishing returns under the wrong objective.
71	
72	
73	\subsection{Ablation Studies}
74	
75	Table~\ref{tab:ablation} isolates the contribution of each design choice at 50\% sparsity.
76	
77	\begin{table}[t]
78	\centering
79	\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$). $^\dagger$SPON $\Delta$ measured with \texttt{evaluate.py}; absolute PPL estimated from $\Delta$.}
80	\label{tab:ablation}
81	\small
82	\begin{tabular}{lcc}
83	\toprule
84	Configuration & PPL$\downarrow$ & $\Delta$ from Ours \\
85	\midrule
86	KL + Gumbel (Ours) & \textbf{11.79} & --- \\ % exp_id: bench_kl50_global
87	KL + Gumbel + SPON & 11.58$^\dagger$ & $-$0.21 \\ % exp_id: spon_2048_s42
88	KL + STE & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
89	BCE + Compensation (hard mask) & 25.44 & +13.65 \\ % exp_id: bce_comp_staged_s42
90	BCE (no compensation) & 27.97 & +16.18 \\ % exp_id: eval_bce_v3_s42
91	\bottomrule
92	\end{tabular}
93	\end{table}
94	
95	\paragraph{Gumbel vs.\ STE.}
96	Replacing Gumbel-Sigmoid relaxation with Straight-Through Estimation~\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98). % exp_id: ste_baseline_s42
97	Gumbel relaxation provides smooth gradients through the mask sampling, accounting for 34.5\% of the total improvement over vanilla TEAL (3.98 out of 11.52 PPL gap).
98	
99	\paragraph{SPON Contribution.}
100	Adding SPON~\cite{xu2026spon} bias correction yields an estimated PPL of 11.58, a marginal 0.21 improvement (1.8\% relative) over KL+Gumbel alone. % exp_id: spon_2048_s42
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "ba8d109f-c3d6-47ac-bbcb-823b1ca88be4"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 49929,
    "tool_uses": 14,
    "duration_ms": 11193
  },
  "last_tool_name": "Bash",
  "uuid": "a37ac697-d084-4ef8-9acf-5b1fd53f756e",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_018HMqpZBVFrLgVfsVLMXaeP`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "66c3f20a-9af1-4b13-9b54-918ef96abfec",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RYH7Un5fbEB7Zsn9N2FH5U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 17402,
      "cache_read_input_tokens": 32477,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17402,
        "ephemeral_1h_input_tokens": 0
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

_source line 54 · 2026-05-16T12:36:53.464Z_

<details><summary>↩ Tool result · `toolu_018HMqpZBVFrLgVfsVLMXaeP`</summary>

```text
total 36
drwxr-xr-x  2 ubuntu ubuntu  4096 May 16 12:34 .
drwxr-xr-x 11 ubuntu ubuntu  4096 May 16 12:32 ..
-rw-r--r--  1 ubuntu ubuntu 11232 May 16 12:34 experiments.tex
-rw-r--r--  1 ubuntu ubuntu 13121 May 16 09:41 references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "9e0d6cab-13a6-4b13-852a-ff3dd712dcd8"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Searching for \\\\newcommand|\\\\DeclareMathOperator|notation|symbol",
  "usage": {
    "total_tokens": 52969,
    "tool_uses": 15,
    "duration_ms": 14088
  },
  "last_tool_name": "Grep",
  "uuid": "247f903d-faa1-4422-8455-26404f1e220e",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Grep · `toolu_01V8MME75JnTNcj7TRr33kjj`</summary>

```json
{
  "pattern": "\\\\newcommand|\\\\DeclareMathOperator|notation|symbol",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "type": "bib",
  "head_limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "7b1aaee2-1a47-46cf-af12-df93b12d86b0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AYRqeqdKcYpxywDB7EEpw4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 49879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3038,
        "ephemeral_1h_input_tokens": 0
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

_source line 57 · 2026-05-16T12:36:56.333Z_

<details><summary>↩ Tool result · `toolu_01V8MME75JnTNcj7TRr33kjj`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "28328876-0d4e-4f52-9467-e26de34a9faa"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 52970,
    "tool_uses": 16,
    "duration_ms": 14301
  },
  "last_tool_name": "Bash",
  "uuid": "c01d6989-5d76-4159-b9b8-537ea7b1b3b9",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_015tMVbfk56GSxNZpDENCcrt`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -name \"*.yaml\" -o -name \"*.md\" | xargs grep -l \"notation\\|symbol\\|variable\" 2>/dev/null | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "0cbbd1dd-7ef8-44ff-9a1b-681f339a2125",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AYRqeqdKcYpxywDB7EEpw4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 49879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3038,
        "ephemeral_1h_input_tokens": 0
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

_source line 60 · 2026-05-16T12:36:56.764Z_

<details><summary>↩ Tool result · `toolu_015tMVbfk56GSxNZpDENCcrt`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.venv/lib/python3.14/site-packages/pyparsing/ai/best_practices.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/paper_agent_f4a39553/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/.claude/sessions/paper_agent_f4a39553/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/review_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/literature_ppl_downstream_disconnect.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "be62280b-9463-4592-94a6-5d84c4e67e44"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 52971,
    "tool_uses": 17,
    "duration_ms": 14619
  },
  "last_tool_name": "Bash",
  "uuid": "1e7d6ebb-23b3-49ad-9ca7-10cf99602e76",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_01WJkjYwTe4uGyVsmY3NKQu2`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ | grep -E \"main|notation|symbol|preamble\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "41d82257-5447-481b-bb44-c6d212424118",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AYRqeqdKcYpxywDB7EEpw4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3038,
      "cache_read_input_tokens": 49879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3038,
        "ephemeral_1h_input_tokens": 0
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

_source line 63 · 2026-05-16T12:36:56.898Z_

<details><summary>↩ Tool result · `toolu_01WJkjYwTe4uGyVsmY3NKQu2`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "81e79cea-9336-4009-b43b-00c91d37586a"
}
```

</details>

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 54016,
    "tool_uses": 18,
    "duration_ms": 16575
  },
  "last_tool_name": "Bash",
  "uuid": "4abab6ee-9260-49bd-8899-073f981cd6c7",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01DUYRbcVuij21CCV8M1v6LM`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -maxdepth 3 -name \"main.tex\" -o -name \"*preamble*\" -o -name \"paper_framing.md\" 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "35156cd6-4655-415b-9768-9585a1d3cd04",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ReFnArUtikUw8fsiBo5vfm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 52917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1043,
        "ephemeral_1h_input_tokens": 0
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

_source line 66 · 2026-05-16T12:36:58.856Z_

<details><summary>↩ Tool result · `toolu_01DUYRbcVuij21CCV8M1v6LM`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "793188be-4845-4841-9ccc-ca8e2f50e9db"
}
```

</details>

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Reading writing_plan.yaml",
  "usage": {
    "total_tokens": 54017,
    "tool_uses": 19,
    "duration_ms": 17041
  },
  "last_tool_name": "Read",
  "uuid": "98f5dd30-a97b-4e16-8929-c96a517687d0",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01JsYfTVjmWYwU3YyKPPWPsL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "8d7a7050-64ce-4952-af34-43eb33bb8cb0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ReFnArUtikUw8fsiBo5vfm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 52917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1043,
        "ephemeral_1h_input_tokens": 0
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

_source line 69 · 2026-05-16T12:36:59.265Z_

<details><summary>↩ Tool result · `toolu_01JsYfTVjmWYwU3YyKPPWPsL`</summary>

```text
1	meta:
2	  venue: EMNLP 2026 (ARR May cycle)
3	  track: Efficient Methods for NLP
4	  template: acl2023  # ARR confirmed acl2023 style
5	  template_note: ""
6	  page_limit: 8
7	  deadline: 2026-05-25
8	  core_claim: >
9	    Output-distribution distillation (KL) simultaneously achieves better quality
10	    and simpler architecture (no error compensation) for activation sparsity prediction
11	    in SwiGLU LLMs. The KL advantage is structural — BCE's per-neuron objective is
12	    mismatched with global top-k inference — and persists across 30–70% sparsity with
13	    growing gap (18%→48%→82%). SPON's static correction is orthogonal to KL and too
14	    weak to complement it. We unify existing methods through a 2D taxonomy and validate
15	    across architectures (LLaMA-3.1-8B / Mistral-7B-v0.3).
16	  created_at: 2026-05-16T00:00:00Z
17	  verify_refs: true
18	
19	paper_outline:
20	  - section: abstract
21	    word_budget: 200
22	    core_bullets:
23	      - "问题: SwiGLU LLMs 的 activation sparsity 推理加速需要 predictor，但现有 BCE-trained predictor 需额外 compensation network（67.2M params）"
24	      - "Insight: KL divergence 训练将所有 neuron 决策通过 output distribution 耦合，自然捕获 joint interaction"
25	      - "结果: KL-only predictor PPL 12.00±0.07 @ 50% sparsity（无 compensation），BCE iso-compute 2700步 PPL 27.97（structural mismatch）"
26	      - "分析: SPON static correction 与 KL 近正交（cos_sim=0.196），magnitude 仅 15.8%——KL subsumes SPON 效果"
27	      - "贡献: 2D taxonomy 统一现有方法，30-70% sparsity scaling（KL优势 18%→48%→82%），跨架构验证（Mistral-7B）"
28	    dependencies: [experiments, method]
29	
30	  - section: introduction
31	    word_budget: 1100
32	    core_bullets:
33	      - "Hook: SwiGLU LLMs 可通过 50% neuron pruning 获得 ~2x 推理加速，但 training-free 方法 PPL 退化 94-480%"
34	      - "Context: learned predictor 是当前最佳方案（DejaVu, FastForward），但都用 BCE loss + compensation network"
35	      - "Gap: BCE 优化 per-neuron binary accuracy，与 global top-k 推理管线结构性错配——梯度 factorized，miss joint interaction"
36	      - "Insight: KL divergence 训练 loss 通过 d_logits/dh * dh/dm 耦合所有 active neurons，自然建模 joint effect"
37	      - "Mechanism: Gumbel-sigmoid relaxation + KL loss + Lagrangian sparsity constraint，无需 compensation network"
38	      - "Contributions: [C1] KL-trained predictor 消除 compensation 需求 + structural mismatch 机制论证, [C2] 2D taxonomy 统一现有方法, [C3] SPON subsumption + sparsity scaling phase transition + cross-arch"
39	    dependencies: [experiments, method]
40	    citation_hints:
41	      - "TEAL (Liu et al., 2025)"
42	      - "DejaVu (Liu et al., 2023)"
43	      - "FastForward (Gautam et al., 2026)"
44	      - "SPON (Xu et al., 2026)"
45	      - "ShadowLLM (Akhauri et al., 2024)"
46	    figures: [fig1_overview]
47	
48	  - section: related_work
49	    word_budget: 700
50	    core_bullets:
51	      - "Cluster 1 — Training-free activation sparsity: TEAL, WINA, R-Sparse, CATS, SparseInfer → 无需训练但质量差距大"
52	      - "Cluster 2 — Predictor-based contextual sparsity: DejaVu, ShadowLLM, FastForward → BCE loss + compensation，推理开销"
53	      - "Cluster 3 — Static bias correction: SPON → KL-trained bias 但 input-independent，不做 per-token adaptation"
54	      - "Cluster 4 — Activation function engineering: ReLU Strikes Back, TurboSparse, ProSparse → 修改激活函数路线，我们不改预训练模型"
55	      - "定位: 唯一使用 KL 训练 contextual sparsity predictor 的工作"
56	    dependencies: [introduction]
57	    citation_hints:
58	      - "R-Sparse (Zhang et al., 2025)"
59	      - "CATS (Lee et al., 2024)"
60	      - "DIP (Federici et al., 2024)"
61	      - "Minitron (Muralidharan et al., 2024)"
62	
63	  - section: method
64	    word_budget: 1600
65	    core_bullets:
66	      - "§3.1 Problem Formulation: SwiGLU FFN sparsity — gate activation 驱动 neuron selection"
67	      - "§3.2 Predictor Architecture: lightweight MLP predictor (1.5M params/layer, 32 layers)"
68	      - "§3.3 Gumbel-Sigmoid Relaxation: differentiable sampling，tau annealing（STE baseline 对比）"
69	      - "§3.4 KL Divergence Training: forward KL(dense || sparse) → output distribution preservation"
70	      - "§3.5 Lagrangian Sparsity Constraint: dual variable lambda 自动调节 sparsity target"
71	      - "§3.6 Gradient Analysis — BCE vs KL: BCE 梯度 dL/ds_j factorized（per-neuron independent），KL 梯度 dL/ds_j 通过 Jacobian 耦合所有 neurons → structural mismatch with global top-k"
72	      - "§3.7 Taxonomy: correction granularity (static/per-layer/per-token) × training signal coupling (decomposed/intermediate/coupled)"
73	    dependencies: []
74	    notation_table:
75	      h: "hidden states after attention"
76	      m: "binary sparsity mask (per-neuron)"
77	      s: "soft mask probabilities (predictor output)"
78	      sigma_tau: "Gumbel-sigmoid with temperature tau"
79	      D_KL: "forward KL divergence"
80	      lambda: "Lagrangian dual variable for sparsity constraint"
81	    registry_refs: [ste_baseline_s42, plan_005_subsumption_s42]
82	
83	  - section: experiments
84	    word_budget: 2000
85	    core_bullets:
86	      - "§5.1 Setup: LLaMA-3.1-8B + Mistral-7B-v0.3, WikiText-2 PPL, 50% model-level sparsity, 1000 training steps, C4 calibration"
87	      - "§5.2 Main Results (Table 1): 同推理协议 predictor-TEAL 对比. KL 12.00 vs Vanilla TEAL 23.31 vs BCE iso-compute 27.97"
88	      - "§5.3 Iso-compute Defense (Table 2): BCE 2700步 FLOPs 1.0× still PPL=27.97, loss saturates — structural mismatch not compute deficit"
89	      - "§5.4 Ablation Studies (Table 3): Gumbel vs STE, SPON add-on effect"
90	      - "§5.5 Sparsity Scaling + Phase Transition (Figure 2 + Table 4 + Table 6): PPL scaling 30%→50%→70%, KL advantage 18%→48%→82%. Phase transition: gradual degradation band (not cliff). 30% uniform MMLU=40.61% > TEAL 30%=38.61% (allocation-fixable). 50% all methods ≈random MMLU (capacity-limited). Uniform primarily benefits knowledge-intensive tasks. 30% = recommended operating point."
91	      - "§5.6 SPON Orthogonality Analysis (Figure 3): cos_sim=0.196, magnitude=15.8%, recovery=7.3%"
92	      - "§5.7 Cross-Architecture (Mistral): KL TEAL PPL 8.98, 62.7% relative degradation vs Llama 96%"
93	      - "§5.8 Downstream (Table 1 extended): KL 50% global ARC-c 32.85%/WG 63.46%/MMLU 27.89%/GSM8K 1.29% vs TEAL 50% 28.41%/53.04%/28.32%/1.97%. Uniform primarily benefits MMLU at 30% (25.27→40.61%). Pending: bench_kl50_uniform, bench_kl40_global"
94	    dependencies: []
95	    registry_refs:
96	      - mvp_kl_norm_v2_s42
97	      - mvp_kl_norm_v2_s123
98	      - kl_only_s0
99	      - kl_only_s1
100	      - training_free_baselines
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "505966e2-736f-4e0d-9596-db11b64bdf36"
}
```

</details>

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 54018,
    "tool_uses": 20,
    "duration_ms": 17206
  },
  "last_tool_name": "Bash",
  "uuid": "32b8fecd-98c2-41e9-b259-7812e5874d9a",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01S4eeeW6KyJFfZydaHxU7jb`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/*.{tex,md} 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "489b6fa2-f345-4571-be20-bba4d6010765",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ReFnArUtikUw8fsiBo5vfm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1043,
      "cache_read_input_tokens": 52917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1043,
        "ephemeral_1h_input_tokens": 0
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

_source line 72 · 2026-05-16T12:36:59.485Z_

<details><summary>↩ Tool result · reported error · `toolu_01S4eeeW6KyJFfZydaHxU7jb`</summary>

```text
Exit code 2
-rw-r--r-- 1 ubuntu ubuntu 12791 May 16 12:36 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/AGENTS.md
-rw------- 1 ubuntu ubuntu  3797 May 16 12:31 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md
-rw-r--r-- 1 ubuntu ubuntu  3195 May 16 12:24 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md
-rw-r--r-- 1 ubuntu ubuntu  8088 May 16 12:23 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md
-rw-r--r-- 1 ubuntu ubuntu  1903 May 16 12:20 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "ddb10f44-8713-4980-ab26-03e544213c24",
  "tool_use_result": "Error: Exit code 2\n-rw-r--r-- 1 ubuntu ubuntu 12791 May 16 12:36 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/AGENTS.md\n-rw------- 1 ubuntu ubuntu  3797 May 16 12:31 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/ROADMAP.md\n-rw-r--r-- 1 ubuntu ubuntu  3195 May 16 12:24 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md\n-rw-r--r-- 1 ubuntu ubuntu  8088 May 16 12:23 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md\n-rw-r--r-- 1 ubuntu ubuntu  1903 May 16 12:20 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/report.md"
}
```

</details>

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Reading writing_plan.yaml",
  "usage": {
    "total_tokens": 57394,
    "tool_uses": 21,
    "duration_ms": 19109
  },
  "last_tool_name": "Read",
  "uuid": "cbd67f2b-5f6f-4f99-9105-b26e81e3cd4e",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_01UyEnME4VgCfQ3zZZHLj1Rv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml",
  "limit": 200,
  "offset": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "f899922d-30b4-40b3-870c-999be574eb69",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BTH8WqjVmiovRk5bKideUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3374,
      "cache_read_input_tokens": 53960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3374,
        "ephemeral_1h_input_tokens": 0
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

_source line 75 · 2026-05-16T12:37:01.342Z_

<details><summary>↩ Tool result · `toolu_01UyEnME4VgCfQ3zZZHLj1Rv`</summary>

```text
70	      - "§3.5 Lagrangian Sparsity Constraint: dual variable lambda 自动调节 sparsity target"
71	      - "§3.6 Gradient Analysis — BCE vs KL: BCE 梯度 dL/ds_j factorized（per-neuron independent），KL 梯度 dL/ds_j 通过 Jacobian 耦合所有 neurons → structural mismatch with global top-k"
72	      - "§3.7 Taxonomy: correction granularity (static/per-layer/per-token) × training signal coupling (decomposed/intermediate/coupled)"
73	    dependencies: []
74	    notation_table:
75	      h: "hidden states after attention"
76	      m: "binary sparsity mask (per-neuron)"
77	      s: "soft mask probabilities (predictor output)"
78	      sigma_tau: "Gumbel-sigmoid with temperature tau"
79	      D_KL: "forward KL divergence"
80	      lambda: "Lagrangian dual variable for sparsity constraint"
81	    registry_refs: [ste_baseline_s42, plan_005_subsumption_s42]
82	
83	  - section: experiments
84	    word_budget: 2000
85	    core_bullets:
86	      - "§5.1 Setup: LLaMA-3.1-8B + Mistral-7B-v0.3, WikiText-2 PPL, 50% model-level sparsity, 1000 training steps, C4 calibration"
87	      - "§5.2 Main Results (Table 1): 同推理协议 predictor-TEAL 对比. KL 12.00 vs Vanilla TEAL 23.31 vs BCE iso-compute 27.97"
88	      - "§5.3 Iso-compute Defense (Table 2): BCE 2700步 FLOPs 1.0× still PPL=27.97, loss saturates — structural mismatch not compute deficit"
89	      - "§5.4 Ablation Studies (Table 3): Gumbel vs STE, SPON add-on effect"
90	      - "§5.5 Sparsity Scaling + Phase Transition (Figure 2 + Table 4 + Table 6): PPL scaling 30%→50%→70%, KL advantage 18%→48%→82%. Phase transition: gradual degradation band (not cliff). 30% uniform MMLU=40.61% > TEAL 30%=38.61% (allocation-fixable). 50% all methods ≈random MMLU (capacity-limited). Uniform primarily benefits knowledge-intensive tasks. 30% = recommended operating point."
91	      - "§5.6 SPON Orthogonality Analysis (Figure 3): cos_sim=0.196, magnitude=15.8%, recovery=7.3%"
92	      - "§5.7 Cross-Architecture (Mistral): KL TEAL PPL 8.98, 62.7% relative degradation vs Llama 96%"
93	      - "§5.8 Downstream (Table 1 extended): KL 50% global ARC-c 32.85%/WG 63.46%/MMLU 27.89%/GSM8K 1.29% vs TEAL 50% 28.41%/53.04%/28.32%/1.97%. Uniform primarily benefits MMLU at 30% (25.27→40.61%). Pending: bench_kl50_uniform, bench_kl40_global"
94	    dependencies: []
95	    registry_refs:
96	      - mvp_kl_norm_v2_s42
97	      - mvp_kl_norm_v2_s123
98	      - kl_only_s0
99	      - kl_only_s1
100	      - training_free_baselines
101	      - bce_isocompute_v2_s42
102	      - eval_bce_v3_s42
103	      - bce_comp_staged_s42
104	      - ste_baseline_s42
105	      - plan_005_subsumption_s42
106	      - spon_2048_s42
107	      - kl_sparsity30_s42_v3
108	      - kl_sparsity70_s42_v2
109	      - mistral_kl_s42
110	      - bench_teal30
111	      - bench_teal50
112	      - bench_kl50_global
113	      - lm_eval_kl_30pct_s42
114	      - bench_kl30_uniform
115	      - d030_kl40_uniform
116	      - d030_kl50_uniform
117	    tables: [tab1_main_results, tab2_isocompute, tab3_ablation, tab4_sparsity_sweep, tab5_cross_arch, tab6_phase_transition]
118	    figures: [fig2_sparsity_sweep, fig3_subsumption]
119	
120	  - section: conclusion
121	    word_budget: 400
122	    core_bullets:
123	      - "Summary: KL-trained predictor 消除 compensation 需求，structural mismatch 机制论证"
124	      - "Key numbers: PPL 12.00 @ 50% sparsity, KL advantage 18-82% across 30-70%, 跨架构一致"
125	      - "Limitations: WikiText-2 PPL 为主指标，downstream 部分数据待补，训练成本 1000 steps（~17min on A6000），仅验证 7-8B 模型"
126	      - "Future: N:M structured sparsity, 更大模型（13B/70B）, phase transition boundary 精确定位"
127	    dependencies: [experiments, method]
128	
129	visualization_plan:
130	  - fig_id: fig1_overview
131	    type: conceptual
132	    tool: matplotlib
133	    description: "2D taxonomy (correction granularity × training signal coupling), Ours 高亮"
134	    placement: introduction
135	    aspect_ratio: "16:9"
136	    data_source: "manual"
137	    status: done
138	
139	  - fig_id: fig2_sparsity_sweep
140	    type: statistical
141	    tool: matplotlib
142	    description: >
143	      Log-scale 折线图：KL predictor-TEAL vs vanilla TEAL at 30/50/70% sparsity.
144	      KL advantage 18%→48%→82%. 同推理协议 (D035).
145	    placement: experiments
146	    aspect_ratio: "4:3"
147	    data_source: "registry: kl_sparsity30_s42_v3, mvp_kl_norm_v2_s42, kl_sparsity70_s42_v2, training_free_baselines"
148	    status: done
149	
150	  - fig_id: fig3_subsumption
151	    type: statistical
152	    tool: matplotlib
153	    description: "两面板: (a) effect decomposition bars, (b) SPON recovery PPL"
154	    placement: experiments
155	    aspect_ratio: "8:3.5"
156	    data_source: "registry: plan_005_subsumption_s42, spon_2048_s42"
157	    status: done
158	
159	table_plan:
160	  - table_id: tab_taxonomy
161	    caption: "Two-dimensional taxonomy of activation sparsity methods"
162	    placement: method
163	    type: configuration
164	    columns: ["", "Decomposed (BCE)", "Intermediate (MSE)", "Coupled (KL)"]
165	    rows:
166	      - ["Static", "—", "—", "SPON"]
167	      - ["Per-layer", "—", "ShadowLLM", "—"]
168	      - ["Per-token contextual", "FastForward", "—", "Ours"]
169	    data_source: "manual"
170	    notes: "Ours 加粗。如空间紧张可合并到 fig1_overview"
171	
172	  - table_id: tab1_main_results
173	    caption: "Main results on LLaMA-3.1-8B grouped by sparsity level (PPL + downstream, same few-shot protocol)"
174	    placement: experiments
175	    type: comparison
176	    columns: [Method, PPL↓, ARC-c, WG, MMLU, GSM8K]
177	    rows_spec:
178	      - "--- Dense ---"
179	      - "Dense: 6.12, 58.28%, 78.06%, 65.27%, 48.75%"
180	      - "--- 30% Sparsity ---"
181	      - "TEAL 30% vanilla: 10.97, 42.32%, 66.06%, 38.61%, 7.88%"
182	      - "KL 30% global (Ours): 8.98, 39.68%, 70.17%, 25.27%, 8.79%"
183	      - "KL 30% uniform: 8.82, 40.78%, 68.59%, 40.61%, 7.35%"
184	      - "--- 50% Sparsity ---"
185	      - "TEAL 50% vanilla: 23.31, 28.41%, 53.04%, 28.32%, 1.97%"
186	      - "KL 50% global (Ours): 11.79, 32.85%, 63.46%, 27.89%, 1.29%"
187	      - "KL 50% uniform: 11.96, 32.76%, 62.90%, 27.77%, 2.12%"
188	      - "BCE iso-compute (2700 steps): 27.97, 23.98%, 50.59%, 30.02%, 4.85%"
189	    data_source: "registry: training_free_baselines, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, bench_kl30_uniform, d030_kl50_uniform, eval_bce_v3_s42, bench_dense"
190	    notes: >
191	      Few-shot: ARC-c=25, WG=5, MMLU=5, GSM8K=8. 加粗 KL global 行。
192	      Claim 3 key: KL 30% uniform MMLU=40.61% > TEAL 30%=38.61% (allocation-fixable).
193	      50%: all methods ≈random MMLU (capacity-limited).
194	      Uniform allocation primarily benefits knowledge-intensive tasks (MMLU).
195	      Pending: bench_kl50_uniform, bench_kl40_global (will be patched in).
196	
197	  - table_id: tab2_isocompute
198	    caption: "Iso-compute ablation: KL vs BCE with matched total FLOPs at 50% sparsity"
199	    placement: experiments
200	    type: ablation
201	    columns: [Method, Steps, FLOPs ratio, PPL↓, ARC-c, WG, MMLU, GSM8K]
202	    rows_spec:
203	      - "KL (Ours): 1000, 1.0×, 11.79, 32.85%, 63.46%, 27.89%, 1.29%"
204	      - "BCE iso-compute: 2700, 1.0×, 27.97, 23.98%, 50.59%, 30.02%, 4.85%"
205	      - "Dense: —, —, 6.12, 58.28%, 78.06%, 65.27%, 48.75%"
206	    data_source: "registry: bench_kl50_global, eval_bce_v3_s42, bench_dense"
207	    notes: >
208	      BCE loss saturates (step 500→2700: Δ=-0.006), confirming structural mismatch
209	      not compute deficit. KL dominates PPL + WG; BCE slightly ahead on MMLU/GSM8K
210	      (both near random — capacity-limited regime, not meaningful advantage).
211	
212	  - table_id: tab3_ablation
213	    caption: "Ablation: relaxation method and SPON supplementary effect"
214	    placement: experiments
215	    type: ablation
216	    columns: [Configuration, TEAL PPL↓, Δ vs Ours]
217	    rows_spec:
218	      - "KL + Gumbel (Ours): 12.00, —"
219	      - "KL + STE: 15.77, +3.77 (Gumbel contributes 31.4%)"
220	      - "KL + Gumbel + SPON: 11.79, -0.21 (4.8% TEAL-path recovery)"
221	      - "BCE + Comp (hard mask): 25.44, +13.44 (comp 改善 10% vs no-comp 27.96)"
222	    data_source: "registry: mvp_kl_norm_v2_s42, ste_baseline_s42, spon_2048_s42, bce_comp_staged_s42"
223	    baseline_row: "KL + Gumbel (Ours)"
224	    notes: "BCE+comp uses hard mask inference (not TEAL), separated per D035"
225	
226	  - table_id: tab4_sparsity_sweep
227	    caption: "Sparsity scaling: KL predictor-TEAL vs vanilla TEAL (same inference protocol)"
228	    placement: experiments
229	    type: comparison
230	    columns: [Sparsity, KL predictor-TEAL, Vanilla TEAL, KL Advantage]
231	    rows_spec:
232	      - "30% (achieved 28.5%): 8.98, 10.97, 18%"
233	      - "50%: 12.00, 23.31, 48%"
234	      - "70% (achieved 69.9%): 17.91, 100.11, 82%"
235	    data_source: "registry: kl_sparsity30_s42_v3, mvp_kl_norm_v2_s42, kl_sparsity70_s42_v2, training_free_baselines"
236	    notes: "D035 同推理协议。KL advantage grows with sparsity — phase transition between allocation-fixable (≤30%) and capacity-limited (≥50%) regimes."
237	
238	  - table_id: tab5_cross_arch
239	    caption: "Cross-architecture generalization at 50% sparsity"
240	    placement: experiments
241	    type: comparison
242	    columns: [Model, Dense PPL, KL predictor-TEAL PPL, Relative Degradation]
243	    rows_spec:
244	      - "LLaMA-3.1-8B: 6.12, 12.00±0.07, +96%"
245	      - "Mistral-7B-v0.3: 5.52, 8.98, +63%"
246	    data_source: "registry: mvp_kl_norm_v2_s42, kl_only_s0, kl_only_s1, mvp_kl_norm_v2_s123, mistral_kl_s42"
247	    notes: "Mistral uses GQA + sliding window attention. Mistral shows lower relative degradation."
248	
249	  - table_id: tab6_phase_transition
250	    caption: "Phase transition analysis: allocation strategy × sparsity level (downstream)"
251	    placement: experiments
252	    type: comparison
253	    columns: [Sparsity, Method, PPL, ARC-c, WG, MMLU, GSM8K]
254	    rows_spec:
255	      - "30%: TEAL vanilla, 10.97, 42.32%, 66.06%, 38.61%, 7.88%"
256	      - "30%: KL global, 8.98, 39.68%, 70.17%, 25.27%, 8.79%"
257	      - "30%: KL uniform, 8.82, 40.78%, 68.59%, 40.61%, 7.35%"
258	      - "40%: KL uniform, 8.36, 41.81%, 67.17%, 30.68%, 3.94%"
259	      - "50%: TEAL vanilla, 23.31, 28.41%, 53.04%, 28.32%, 1.97%"
260	      - "50%: KL global, 11.79, 32.85%, 63.46%, 27.89%, 1.29%"
261	      - "50%: KL uniform, 11.96, 32.76%, 62.90%, 27.77%, 2.12%"
262	    data_source: "registry: d030_kl30_uniform, d030_kl40_uniform, d030_kl50_uniform"
263	    notes: >
264	      Gradual degradation band (not cliff): MMLU drops from 40.6%→30.7%→27.8% (random ~25%).
265	      30% = recommended operating point where allocation is fixable.
266	      Can be placed in §5.5 inline or appendix depending on space.
267	
268	literature_strategy:
269	  citation_budget: 35
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "1ba6d6fb-77c5-49ed-bd13-70d7bab9f05a"
}
```

</details>

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Reading paper_framing.md",
  "usage": {
    "total_tokens": 57395,
    "tool_uses": 22,
    "duration_ms": 19341
  },
  "last_tool_name": "Read",
  "uuid": "f3346281-2f0c-4fda-9e29-9a304296730e",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Read · `toolu_01G9wD37MdT4CC5NfWaVoKJG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "79326e98-edf4-4436-94e1-14286ce6844f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BTH8WqjVmiovRk5bKideUp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3374,
      "cache_read_input_tokens": 53960,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3374,
        "ephemeral_1h_input_tokens": 0
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

_source line 78 · 2026-05-16T12:37:01.563Z_

<details><summary>↩ Tool result · `toolu_01G9wD37MdT4CC5NfWaVoKJG`</summary>

```text
1	# Paper Framing — distill_sparse_swiglu
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 2026 cycle)
5	- Deadline: 2026-05-25 (ARR submission)
6	- Track: Efficient Methods for NLP
7	
8	## Core Claims
9	
10	1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent "unfair comparison" attacks. **Iso-compute evidence (eval_bce_v3_s42)**: with 2.71× more gradient updates, BCE TEAL PPL=27.97 vs KL=12.00 (2.33× gap persists), and BCE loss saturates (step 500→2700: Δ=-0.006). The advantage is structural: BCE optimizes per-neuron binary classification, but inference uses global top-k budget allocation — per-neuron scoring is suboptimal under global reallocation. KL directly optimizes output distribution, naturally compatible with any allocation strategy. (Headline claim)
11	
12	2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL "subsuming" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)
13	
14	3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, downstream collapse is caused by per-layer allocation imbalance from global top-k (fixable: uniform per-layer allocation restores MMLU from random→40.6%, surpassing TEAL's 38.6% on knowledge-intensive tasks). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition is a gradual degradation band: 30% MMLU=40.6% (dense 62%, allocation-fixable), 40% MMLU=30.7% (partially degraded, PPL-optimal at 8.36 but downstream compromised), 50% MMLU=27.8% (≈random, capacity-limited). Recommended operating point: 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports "PPL is a poor proxy for downstream quality" narrative. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)
15	
16	## Story Spine
17	
18	- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).
19	
20	- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.
21	
22	- **Our framing / headline question**: "Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.
23	
24	- **Headline result template**: "On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] quality but adds 67.2M parameters ([W] ms/token overhead) — demonstrating that output-distribution distillation renders error compensation unnecessary—SPON's residual correction is orthogonal to KL's dominant effect and too weak to complement it—enabling a simpler, lighter inference pipeline with strictly better efficiency-quality tradeoff."
25	
26	## Two-Dimensional Taxonomy (Conceptual Contribution)
27	
28	|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
29	|--------------------------|:-----------------:|:-------------------:|:-------------:|
30	| Static                   | —                 | —                   | SPON          |
31	| Per-layer                | —                 | ShadowLLM           | —             |
32	| Per-token contextual     | FastForward       | —                   | **Ours**      |
33	
34	Positions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.
35	
36	## Anticipated Reviewer Concerns
37	
38	1. **"Incremental / no new algorithm"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.
39	
40	2. **"KL wins only because more compute"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.
41	
42	3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.
43	
44	4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).
45	
46	5. **"Effect size may not hold on downstream tasks"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.
47	
48	6. **"Unfair comparison: BCE+comp close to KL but at higher inference cost"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.
49	
50	## Venue Fit
51	- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation
52	- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue
53	- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "b35c573e-2656-4f3b-932d-42e84611f31b"
}
```

</details>

---

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 64633,
    "tool_uses": 23,
    "duration_ms": 22130
  },
  "last_tool_name": "Bash",
  "uuid": "0a01510a-85dc-4baf-a278-ab7103306041",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_01FZY8ioSs7Pv9kBbQMCpAau`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu -name \"*.tex\" -not -path \"./.venv/*\" -not -path \"*/.venv/*\" 2>/dev/null | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "7abaad31-e964-4f19-80dc-d6dda31f1b00",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDBc8trY3ZgHWcKd1dNdMB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7230,
      "cache_read_input_tokens": 57334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7230,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 81 · 2026-05-16T12:37:04.417Z_

<details><summary>↩ Tool result · `toolu_01FZY8ioSs7Pv9kBbQMCpAau`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology_6e294a.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/related_work_c10e4f.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "f0f6ba47-ec3d-4920-b2aa-bcc0ae13e8cd"
}
```

</details>

---

### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running grep -r \"newcommand\\|DeclareMathOperator\" /home/u…",
  "usage": {
    "total_tokens": 64637,
    "tool_uses": 24,
    "duration_ms": 22502
  },
  "last_tool_name": "Bash",
  "uuid": "78a800f8-44f8-4718-9a32-e6f3ba110592",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_015AjGW2JtAm3V7NgCfX52wg`</summary>

```json
{
  "command": "grep -r \"newcommand\\|DeclareMathOperator\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu --include=\"*.tex\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "8dc06417-dd77-4761-9ac0-e1368452f538",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDBc8trY3ZgHWcKd1dNdMB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 7230,
      "cache_read_input_tokens": 57334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7230,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 84 · 2026-05-16T12:37:04.785Z_

<details><summary>↩ Tool result · `toolu_015AjGW2JtAm3V7NgCfX52wg`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/median/paper.tex:\newcommand{\method}{KL-Sparse}
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.tex:\newcommand{\method}{SwiGLU}
/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/dream_reports/dream_20260515T164925/worst/paper.tex:\newcommand{\ours}{KL-Sparse}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "b35f2fb0-ee62-41be-b8fb-c810d0c385cb"
}
```

</details>

---

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Reading artifacts/_project/paper/methodology.tex",
  "usage": {
    "total_tokens": 65649,
    "tool_uses": 25,
    "duration_ms": 24689
  },
  "last_tool_name": "Read",
  "uuid": "f3bf54a4-baeb-4d4d-a0e9-10c04c07b79a",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Read · `toolu_01BeDSTxkfb4XXtcGNxKUvAn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "22ed0645-94c9-4f68-86f4-8755b30a5257",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K24Jop1HhGMvCAWfoofq9X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 64564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 87 · 2026-05-16T12:37:06.911Z_

<details><summary>↩ Tool result · `toolu_01BeDSTxkfb4XXtcGNxKUvAn`</summary>

```text
1	\section{Methodology}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:method:formulation}
6	
7	We consider a pretrained SwiGLU-based language model with $L$ transformer layers.
8	Each feed-forward network (FFN) in layer $\ell$ computes:
9	\begin{equation}
10	\mathbf{h}^{(\ell)} = \bigl(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{gate}}^{(\ell)} \odot \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{up}}^{(\ell)})\bigr) \mathbf{W}_{\text{down}}^{(\ell)},
11	\label{eq:swiglu}
12	\end{equation}
13	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{T \times d}$ is the input hidden state ($d{=}4096$ for Llama-3.1-8B), $\sigma$ denotes SiLU, $\mathbf{W}_{\text{gate}}^{(\ell)}, \mathbf{W}_{\text{up}}^{(\ell)} \in \mathbb{R}^{d \times D}$ and $\mathbf{W}_{\text{down}}^{(\ell)} \in \mathbb{R}^{D \times d}$ are the FFN weight matrices, $D{=}14{,}336$ is the intermediate dimension, and $\odot$ is element-wise multiplication.
14	
15	A substantial fraction of intermediate neurons produce near-zero activation magnitudes $|\mathbf{W}_{\text{gate}}^{(\ell)} \odot \sigma(\mathbf{W}_{\text{up}}^{(\ell)})|$ for any given input, making them candidates for pruning \cite{placeholder_teal,placeholder_dejavu}.
16	Our goal is to train a lightweight \emph{contextual sparsity predictor} $P^{(\ell)}$ for each layer $\ell$ that maps the current hidden state to a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^D$ indicating which neurons to retain.
17	The sparse FFN computation becomes:
18	\begin{equation}
19	\tilde{\mathbf{h}}^{(\ell)} = \bigl(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{gate}}^{(\ell)} \odot \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{up}}^{(\ell)}) \odot \mathbf{m}^{(\ell)}\bigr) \mathbf{W}_{\text{down}}^{(\ell)}.
20	\label{eq:sparse_ffn}
21	\end{equation}
22	We seek a training objective for $P^{(\ell)}$ that preserves the model's output distribution under sparsification, without requiring auxiliary error compensation networks at inference time.
23	
24	\subsection{Predictor Architecture}
25	\label{sec:method:predictor}
26	
27	Each layer $\ell$ has an independent two-layer MLP predictor:
28	\begin{equation}
29	P^{(\ell)}(\mathbf{x}) = \mathbf{W}_2^{(\ell)}\, \text{ReLU}\!\bigl(\mathbf{W}_1^{(\ell)} \mathbf{x}\bigr),
30	\label{eq:predictor}
31	\end{equation}
32	where $\mathbf{W}_1^{(\ell)} \in \mathbb{R}^{d \times d_b}$ and $\mathbf{W}_2^{(\ell)} \in \mathbb{R}^{d_b \times D}$ with bottleneck dimension $d_b{=}256$.
33	The predictor outputs $D$-dimensional logits $\mathbf{s}^{(\ell)} = P^{(\ell)}(\mathbf{x}^{(\ell)})$, from which the binary mask is derived.
34	The total predictor overhead is 75.96M parameters across 32 layers (${\approx}1\%$ of the 8B base model), requiring no additional parameters at inference beyond the predictors themselves.
35	
36	\subsection{KL Distillation Loss}
37	\label{sec:method:kl}
38	
39	The central design choice is the training objective.
40	Prior contextual sparsity predictors \cite{placeholder_dejavu,placeholder_shadowllm,placeholder_fastforward} train with binary cross-entropy (BCE), treating each neuron as an independent binary classification target against the oracle mask (typically the top-$k$ neurons by activation magnitude).
41	We instead train predictors via output-distribution distillation: the sparse model's logit distribution should match the dense model's.
42	
43	Concretely, let $\mathbf{y}_{\text{dense}} = f(\mathbf{x})$ denote the logits from a full dense forward pass, and $\mathbf{y}_{\text{sparse}} = f(\mathbf{x}; \{\mathbf{m}^{(\ell)}\}_\ell)$ the logits from a forward pass with predictor-generated masks applied at every layer.
44	The loss is the forward KL divergence:
45	\begin{equation}
46	\mathcal{L}_{\text{KL}} = \text{KL}\!\bigl(p_{\text{dense}} \,\|\, p_{\text{sparse}}\bigr) = \sum_{v} p_{\text{dense}}^{(v)} \log \frac{p_{\text{dense}}^{(v)}}{p_{\text{sparse}}^{(v)}},
47	\label{eq:kl_loss}
48	\end{equation}
49	where $p_{\text{dense}} = \text{softmax}(\mathbf{y}_{\text{dense}})$ and $p_{\text{sparse}} = \text{softmax}(\mathbf{y}_{\text{sparse}})$, summed over vocabulary $v$ and averaged over sequence positions.
50	The base model is frozen; only the predictor parameters $\{P^{(\ell)}\}_\ell$ receive gradients.
51	
52	\paragraph{Gradient coupling.}
53	The critical difference from BCE lies in the gradient structure.
54	For a predictor logit $s_j^{(\ell)}$ controlling neuron $j$ in layer $\ell$, the KL gradient is:
55	\begin{equation}
56	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{y}_{\text{sparse}}} \cdot \frac{\partial \mathbf{y}_{\text{sparse}}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial m_j^{(\ell)}} \cdot \frac{\partial m_j^{(\ell)}}{\partial s_j^{(\ell)}}.
57	\label{eq:kl_gradient}
58	\end{equation}
59	The Jacobian $\partial \mathbf{y}_{\text{sparse}} / \partial \mathbf{h}^{(\ell)}$ back-propagates through all downstream layers, coupling the gradient for neuron $j$ to the states of \emph{all} retained neurons across the network.
60	This means the predictor receives a learning signal that reflects how each neuron's inclusion or exclusion jointly affects the output distribution.
61	
62	In contrast, BCE defines a per-neuron loss $\mathcal{L}_{\text{BCE}} = -\sum_j [t_j \log \sigma(s_j) + (1{-}t_j)\log(1{-}\sigma(s_j))]$ against oracle targets $t_j$.
63	Its gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - t_j$ depends only on neuron $j$'s own prediction and target---a factorized signal that cannot capture inter-neuron interactions.
64	At higher sparsity levels, where pruning decisions interact more strongly through the nonlinear forward pass, this factorization becomes increasingly limiting (\S\ref{sec:experiments}).
65	
66	\subsection{Gumbel-Sigmoid Relaxation}
67	\label{sec:method:gumbel}
68	
69	KL distillation requires differentiating through the sparse forward pass, which in turn requires continuous relaxation of the discrete mask.
70	We use Gumbel-sigmoid sampling \cite{placeholder_gumbel}:
71	\begin{equation}
72	m_j^{\text{soft}} = \sigma\!\left(\frac{s_j + g_1 - g_2}{\tau}\right), \quad g_1, g_2 \sim \text{Gumbel}(0,1),
73	\label{eq:gumbel}
74	\end{equation}
75	where $\tau$ is a temperature parameter controlling the sharpness of the relaxation.
76	During training, $\tau$ anneals from 1.0 to 0.1 over the course of optimization, progressively sharpening the soft masks toward binary decisions.
77	At inference, the soft mask is replaced by a hard threshold or folded into the TEAL global allocation (\S\ref{sec:method:teal}).
78	
79	\paragraph{Why not straight-through estimation?}
80	The straight-through estimator (STE)~\cite{placeholder_ste} applies a hard threshold in the forward pass and passes gradients through unchanged.
81	In our setting, STE causes severe training instability: the discrete threshold means small parameter changes can flip large numbers of neurons simultaneously, producing discontinuous jumps in sparsity.
82	This manifests as violent oscillation of the Lagrangian multiplier $\lambda$ (standard deviation 354 over training vs.\ smooth convergence under Gumbel), failure to reach the target sparsity (achieved 47.0\% vs.\ target 50\%), and degraded TEAL PPL (15.77 vs.\ 12.00).
83	Gumbel-sigmoid's continuous relaxation provides smooth gradients that stabilize both the sparsity constraint and the KL objective.
84	
85	\subsection{Lagrangian Sparsity Control}
86	\label{sec:method:lagrangian}
87	
88	We enforce a model-level sparsity target $s_{\text{target}}$ (e.g., 0.5 for 50\% neuron pruning) via an augmented Lagrangian penalty.
89	Let $\bar{s} = \frac{1}{L} \sum_\ell \text{mean}(\mathbf{m}^{(\ell)})$ be the average fraction of \emph{retained} neurons across all layers and tokens in a batch.
90	The total loss is:
91	\begin{equation}
92	\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{KL}} + \lambda \cdot \max\!\bigl(0,\; |\bar{s} - s_{\text{target}}| - \epsilon\bigr),
93	\label{eq:lagrangian}
94	\end{equation}
95	with tolerance $\epsilon{=}0.02$.
96	The multiplier $\lambda$ adapts every 25 steps: if the constraint is violated ($|\bar{s} - s_{\text{target}}| > \epsilon$), $\lambda \leftarrow 2\lambda$; otherwise $\lambda \leftarrow \lambda/2$, clamped to $[0.1, \lambda_{\max}]$ with $\lambda_{\max}{=}5000$ and initial $\lambda_0{=}1.0$.
97	
98	This formulation serves two purposes.
99	First, the tolerance band $\epsilon$ prevents the multiplier from oscillating when sparsity is near the target.
100	Second, the exponential update schedule reacts quickly to large violations (the multiplier can increase 1000$\times$ within 250 steps) while decaying gently when the constraint is satisfied.
101	Unlike a fixed regularization weight, the Lagrangian formulation decouples the sparsity target from the magnitude of the KL loss, which varies across layers and training stages.
102	
103	\subsection{TEAL-Compatible Inference}
104	\label{sec:method:teal}
105	
106	At inference time, we adopt the TEAL global top-$k$ allocation strategy \cite{placeholder_teal} to guarantee exact model-level sparsity.
107	Rather than applying a fixed threshold per layer, TEAL computes a global importance score for every neuron across all layers and retains the top $(1{-}s_{\text{target}}) \times L \times D$ neurons.
108	
109	We compose the predictor with TEAL by defining the importance score for neuron $j$ in layer $\ell$ as:
110	\begin{equation}
111	\text{score}_j^{(\ell)} = \sigma\bigl(s_j^{(\ell)}\bigr) \cdot \bigl|a_j^{(\ell)}\bigr|,
112	\label{eq:teal_score}
113	\end{equation}
114	where $\sigma(s_j^{(\ell)})$ is the predictor's sigmoid probability and $|a_j^{(\ell)}|$ is the activation magnitude.
115	Before global ranking, scores are normalized by per-layer mean to prevent layers with systematically larger activations from dominating the budget.
116	This scoring combines the predictor's learned contextual signal with TEAL's magnitude-based importance, enabling the predictor to redirect the global budget toward neurons it deems critical for output preservation.
117	
118	The inference pipeline requires only a single additional forward pass through the lightweight predictors (${\sim}76$M parameters), with no compensation networks, no auxiliary GEMV operations, and no post-hoc bias correction.
119	
120	\subsection{Training Procedure}
121	\label{sec:method:training}
122	
123	\paragraph{Setup.}
124	The base model (Llama-3.1-8B) is frozen throughout.
125	We train only the predictor parameters on the WikiText-103 training split for 1{,}000 steps with batch size 4 and sequence length 2{,}048.
126	We use AdamW \cite{placeholder_adamw} with learning rate $10^{-3}$, 100-step linear warmup, and cosine decay.
127	Gradient checkpointing is applied to the base model to fit within GPU memory.
128	
129	\paragraph{Computational cost.}
130	Each KL training step requires two forward passes through the base model (one dense for the reference distribution, one sparse with predictor masks) plus a backward pass through the sparse path.
131	This is $2.71\times$ the per-step cost of BCE training, which only requires the dense forward pass to extract oracle targets followed by a predictor-only backward pass.
132	The total training cost is approximately 550 GPU-seconds on two RTX PRO 6000 Blackwell GPUs (1{,}000 steps $\times$ 0.549s/step).
133	
134	\begin{algorithm}[t]
135	\caption{KL-Distilled Sparsity Predictor Training}
136	\label{alg:training}
137	\begin{algorithmic}[1]
138	\REQUIRE Dense model $f$, target sparsity $s_{\text{target}}$, tolerance $\epsilon$, steps $N$
139	\STATE Initialize predictors $\{P^{(\ell)}\}_{\ell=1}^{L}$; $\lambda \leftarrow 1.0$; $\tau \leftarrow 1.0$
140	\FOR{step $= 1$ \TO $N$}
141	    \STATE Sample batch $\mathbf{x}$
142	    \STATE $\mathbf{y}_{\text{dense}} \leftarrow f(\mathbf{x})$ \hfill \COMMENT{dense forward, no grad}
143	    \FOR{each layer $\ell$}
144	        \STATE $\mathbf{s}^{(\ell)} \leftarrow P^{(\ell)}(\mathbf{x}^{(\ell)})$
145	        \STATE $\mathbf{m}^{(\ell)} \leftarrow \sigma\!\bigl((\mathbf{s}^{(\ell)} + g_1 - g_2)/\tau\bigr)$ \hfill \COMMENT{Gumbel-sigmoid}
146	    \ENDFOR
147	    \STATE $\mathbf{y}_{\text{sparse}} \leftarrow f(\mathbf{x}; \{\mathbf{m}^{(\ell)}\}_\ell)$ \hfill \COMMENT{sparse forward, with grad}
148	    \STATE $\mathcal{L}_{\text{KL}} \leftarrow \text{KL}(p_{\text{dense}} \| p_{\text{sparse}})$
149	    \STATE $\bar{s} \leftarrow \text{mean}(\{\mathbf{m}^{(\ell)}\})$
150	    \STATE $\mathcal{L}_{\text{total}} \leftarrow \mathcal{L}_{\text{KL}} + \lambda \cdot \max(0, |\bar{s} - s_{\text{target}}| - \epsilon)$
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "30944ffb-e025-4246-a536-10dcc52d4b98"
}
```

</details>

---

### System

_source line 88_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "description": "Running head -50 /home/ubuntu/.agent-ml-research-idea_gen…",
  "usage": {
    "total_tokens": 65652,
    "tool_uses": 26,
    "duration_ms": 24993
  },
  "last_tool_name": "Bash",
  "uuid": "b975eb94-42ce-4681-9e12-c7a62fe37dc3",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_018HjTifGnqqAf2Vg29xTTbY`</summary>

```json
{
  "command": "head -50 /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "e433a1fe-37f9-41a7-b6ab-2c5a9613301e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01K24Jop1HhGMvCAWfoofq9X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 64564,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1006,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 90 · 2026-05-16T12:37:07.283Z_

<details><summary>↩ Tool result · `toolu_018HjTifGnqqAf2Vg29xTTbY`</summary>

```text
\section{Methodology}
\label{sec:method}

\subsection{Problem Formulation}
\label{sec:method:formulation}

We consider a pretrained SwiGLU-based language model with $L$ transformer layers.
Each feed-forward network (FFN) in layer $\ell$ computes:
\begin{equation}
\mathbf{h}^{(\ell)} = \bigl(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{gate}}^{(\ell)} \odot \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{up}}^{(\ell)})\bigr) \mathbf{W}_{\text{down}}^{(\ell)},
\label{eq:swiglu}
\end{equation}
where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{T \times d}$ is the input hidden state ($d{=}4096$ for Llama-3.1-8B), $\sigma$ denotes SiLU, $\mathbf{W}_{\text{gate}}^{(\ell)}, \mathbf{W}_{\text{up}}^{(\ell)} \in \mathbb{R}^{d \times D}$ and $\mathbf{W}_{\text{down}}^{(\ell)} \in \mathbb{R}^{D \times d}$ are the FFN weight matrices, $D{=}14{,}336$ is the intermediate dimension, and $\odot$ is element-wise multiplication.

A substantial fraction of intermediate neurons produce near-zero activation magnitudes $|\mathbf{W}_{\text{gate}}^{(\ell)} \odot \sigma(\mathbf{W}_{\text{up}}^{(\ell)})|$ for any given input, making them candidates for pruning \cite{placeholder_teal,placeholder_dejavu}.
Our goal is to train a lightweight \emph{contextual sparsity predictor} $P^{(\ell)}$ for each layer $\ell$ that maps the current hidden state to a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^D$ indicating which neurons to retain.
The sparse FFN computation becomes:
\begin{equation}
\tilde{\mathbf{h}}^{(\ell)} = \bigl(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{gate}}^{(\ell)} \odot \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{up}}^{(\ell)}) \odot \mathbf{m}^{(\ell)}\bigr) \mathbf{W}_{\text{down}}^{(\ell)}.
\label{eq:sparse_ffn}
\end{equation}
We seek a training objective for $P^{(\ell)}$ that preserves the model's output distribution under sparsification, without requiring auxiliary error compensation networks at inference time.

\subsection{Predictor Architecture}
\label{sec:method:predictor}

Each layer $\ell$ has an independent two-layer MLP predictor:
\begin{equation}
P^{(\ell)}(\mathbf{x}) = \mathbf{W}_2^{(\ell)}\, \text{ReLU}\!\bigl(\mathbf{W}_1^{(\ell)} \mathbf{x}\bigr),
\label{eq:predictor}
\end{equation}
where $\mathbf{W}_1^{(\ell)} \in \mathbb{R}^{d \times d_b}$ and $\mathbf{W}_2^{(\ell)} \in \mathbb{R}^{d_b \times D}$ with bottleneck dimension $d_b{=}256$.
The predictor outputs $D$-dimensional logits $\mathbf{s}^{(\ell)} = P^{(\ell)}(\mathbf{x}^{(\ell)})$, from which the binary mask is derived.
The total predictor overhead is 75.96M parameters across 32 layers (${\approx}1\%$ of the 8B base model), requiring no additional parameters at inference beyond the predictors themselves.

\subsection{KL Distillation Loss}
\label{sec:method:kl}

The central design choice is the training objective.
Prior contextual sparsity predictors \cite{placeholder_dejavu,placeholder_shadowllm,placeholder_fastforward} train with binary cross-entropy (BCE), treating each neuron as an independent binary classification target against the oracle mask (typically the top-$k$ neurons by activation magnitude).
We instead train predictors via output-distribution distillation: the sparse model's logit distribution should match the dense model's.

Concretely, let $\mathbf{y}_{\text{dense}} = f(\mathbf{x})$ denote the logits from a full dense forward pass, and $\mathbf{y}_{\text{sparse}} = f(\mathbf{x}; \{\mathbf{m}^{(\ell)}\}_\ell)$ the logits from a forward pass with predictor-generated masks applied at every layer.
The loss is the forward KL divergence:
\begin{equation}
\mathcal{L}_{\text{KL}} = \text{KL}\!\bigl(p_{\text{dense}} \,\|\, p_{\text{sparse}}\bigr) = \sum_{v} p_{\text{dense}}^{(v)} \log \frac{p_{\text{dense}}^{(v)}}{p_{\text{sparse}}^{(v)}},
\label{eq:kl_loss}
\end{equation}
where $p_{\text{dense}} = \text{softmax}(\mathbf{y}_{\text{dense}})$ and $p_{\text{sparse}} = \text{softmax}(\mathbf{y}_{\text{sparse}})$, summed over vocabulary $v$ and averaged over sequence positions.
The base model is frozen; only the predictor parameters $\{P^{(\ell)}\}_\ell$ receive gradients.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "0f0d9ac3-e1e2-4dca-af76-712c3bb292d7"
}
```

</details>

---

### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a0a9a14c600047e49",
  "tool_use_id": "toolu_013inttiumy1irsrZ96v4KMi",
  "status": "completed",
  "output_file": "",
  "summary": "Find notation table and paper files",
  "usage": {
    "total_tokens": 72018,
    "tool_uses": 26,
    "duration_ms": 35511
  },
  "uuid": "a3d42555-9ea5-468a-a581-ec839a00d03f",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f"
}
```

---

### Tool result

_source line 92 · 2026-05-16T12:37:17.730Z_

<details><summary>↩ Tool result · `toolu_013inttiumy1irsrZ96v4KMi`</summary>

````text
Perfect! Now I have comprehensive information about the notation and paper structure. Let me compile the final report.

## Summary

I've completed a medium-breadth search of the distill_sparse_swiglu project. Here are my findings:

### 1. **Notation Table Location**

The primary notation definitions are embedded in **writing_plan.yaml** at lines 74-80 within the Method section:

```yaml
notation_table:
  h: "hidden states after attention"
  m: "binary sparsity mask (per-neuron)"
  s: "soft mask probabilities (predictor output)"
  sigma_tau: "Gumbel-sigmoid with temperature tau"
  D_KL: "forward KL divergence"
  lambda: "Lagrangian dual variable for sparsity constraint"
```

**File path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml`

### 2. **Math Notation in LaTeX Files**

Detailed notation is defined in **methodology.tex** (the method section):

**File path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex`

Key symbols used throughout with explicit definitions:
- **d** = model hidden dimension (4096 for Llama-3.1-8B)
- **D** = FFN intermediate dimension (14,336)
- **L** = number of transformer layers (32)
- **x^(ℓ)** = input hidden state for layer ℓ
- **m^(ℓ)** = binary sparsity mask per layer
- **s^(ℓ)** = predictor logits
- **W_gate, W_up, W_down** = FFN weight matrices
- **m_j^soft** = Gumbel-sigmoid relaxed mask
- **τ** = temperature parameter
- **λ** = Lagrangian dual variable
- **s_target** = target sparsity ratio

### 3. **Paper-Related Files**

**Paper source files (main content)**:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex` (main section)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex` (method with detailed notation)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/related_work.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib`

**Planning and framing documents**:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md` (complete paper narrative, claims, and 2D taxonomy)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml` (structured outline with notation_table, figure/table plans)

### 4. **Other Planning Documents Mentioning Notation**

- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md` (key decision reasons, abbreviated notation)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md` (full research brief with mathematical details)

### 5. **Key Finding**

There is **no standalone notation_table file** (such as notation_table.tex, notation_table.yaml, symbols.md) in the project root. The notation definitions are integrated into:
1. The YAML writing plan (structured, human-readable reference)
2. The LaTeX methodology file (with full mathematical exposition including equations and gradient analysis)

The notation system is relatively compact with ~15 core symbols, all consistently used across the paper sections.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "9cb5d4fe-e44f-40eb-9737-6cb39f3f80e5",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for any notation table, symbol definitions, or paper-related files in the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/. Look for:\n1. A notation_table file (any extension)\n2. Any other .tex files in the paper/ directory\n3. Any ideas.md or similar planning docs that mention notation\n\nUse \"medium\" search breadth.",
    "agentId": "a0a9a14c600047e49",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information about the notation and paper structure. Let me compile the final report.\n\n## Summary\n\nI've completed a medium-breadth search of the distill_sparse_swiglu project. Here are my findings:\n\n### 1. **Notation Table Location**\n\nThe primary notation definitions are embedded in **writing_plan.yaml** at lines 74-80 within the Method section:\n\n```yaml\nnotation_table:\n  h: \"hidden states after attention\"\n  m: \"binary sparsity mask (per-neuron)\"\n  s: \"soft mask probabilities (predictor output)\"\n  sigma_tau: \"Gumbel-sigmoid with temperature tau\"\n  D_KL: \"forward KL divergence\"\n  lambda: \"Lagrangian dual variable for sparsity constraint\"\n```\n\n**File path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml`\n\n### 2. **Math Notation in LaTeX Files**\n\nDetailed notation is defined in **methodology.tex** (the method section):\n\n**File path**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex`\n\nKey symbols used throughout with explicit definitions:\n- **d** = model hidden dimension (4096 for Llama-3.1-8B)\n- **D** = FFN intermediate dimension (14,336)\n- **L** = number of transformer layers (32)\n- **x^(ℓ)** = input hidden state for layer ℓ\n- **m^(ℓ)** = binary sparsity mask per layer\n- **s^(ℓ)** = predictor logits\n- **W_gate, W_up, W_down** = FFN weight matrices\n- **m_j^soft** = Gumbel-sigmoid relaxed mask\n- **τ** = temperature parameter\n- **λ** = Lagrangian dual variable\n- **s_target** = target sparsity ratio\n\n### 3. **Paper-Related Files**\n\n**Paper source files (main content)**:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex` (main section)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex` (method with detailed notation)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/related_work.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib`\n\n**Planning and framing documents**:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md` (complete paper narrative, claims, and 2D taxonomy)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/writing_plan.yaml` (structured outline with notation_table, figure/table plans)\n\n### 4. **Other Planning Documents Mentioning Notation**\n\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/memory.md` (key decision reasons, abbreviated notation)\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/docs/IDEA_BRIEF.md` (full research brief with mathematical details)\n\n### 5. **Key Finding**\n\nThere is **no standalone notation_table file** (such as notation_table.tex, notation_table.yaml, symbols.md) in the project root. The notation definitions are integrated into:\n1. The YAML writing plan (structured, human-readable reference)\n2. The LaTeX methodology file (with full mathematical exposition including equations and gradient analysis)\n\nThe notation system is relatively compact with ~15 core symbols, all consistently used across the paper sections."
      }
    ],
    "totalDurationMs": 35514,
    "totalTokens": 72977,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6365,
      "cache_read_input_tokens": 65570,
      "output_tokens": 1035,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6365
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1035,
          "cache_read_input_tokens": 65570,
          "cache_creation_input_tokens": 6365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6365,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 7,
      "searchCount": 8,
      "bashCount": 11,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Read · `toolu_011toRvZGFhUei3XCmj3c436`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "3aa603a2-4812-4188-8529-2e357729836c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDAf5ZCa2t8D7UAY2dLxxZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 35373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1253
      },
      "output_tokens": 63,
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

_source line 94 · 2026-05-16T12:37:20.672Z_

<details><summary>↩ Tool result · `toolu_011toRvZGFhUei3XCmj3c436`</summary>

```text
1	# Paper Framing — distill_sparse_swiglu
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 2026 cycle)
5	- Deadline: 2026-05-25 (ARR submission)
6	- Track: Efficient Methods for NLP
7	
8	## Core Claims
9	
10	1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent "unfair comparison" attacks. **Iso-compute evidence (eval_bce_v3_s42)**: with 2.71× more gradient updates, BCE TEAL PPL=27.97 vs KL=12.00 (2.33× gap persists), and BCE loss saturates (step 500→2700: Δ=-0.006). The advantage is structural: BCE optimizes per-neuron binary classification, but inference uses global top-k budget allocation — per-neuron scoring is suboptimal under global reallocation. KL directly optimizes output distribution, naturally compatible with any allocation strategy. (Headline claim)
11	
12	2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL "subsuming" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)
13	
14	3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, downstream collapse is caused by per-layer allocation imbalance from global top-k (fixable: uniform per-layer allocation restores MMLU from random→40.6%, surpassing TEAL's 38.6% on knowledge-intensive tasks). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition is a gradual degradation band: 30% MMLU=40.6% (dense 62%, allocation-fixable), 40% MMLU=30.7% (partially degraded, PPL-optimal at 8.36 but downstream compromised), 50% MMLU=27.8% (≈random, capacity-limited). Recommended operating point: 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports "PPL is a poor proxy for downstream quality" narrative. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)
15	
16	## Story Spine
17	
18	- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).
19	
20	- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.
21	
22	- **Our framing / headline question**: "Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.
23	
24	- **Headline result template**: "On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] quality but adds 67.2M parameters ([W] ms/token overhead) — demonstrating that output-distribution distillation renders error compensation unnecessary—SPON's residual correction is orthogonal to KL's dominant effect and too weak to complement it—enabling a simpler, lighter inference pipeline with strictly better efficiency-quality tradeoff."
25	
26	## Two-Dimensional Taxonomy (Conceptual Contribution)
27	
28	|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |
29	|--------------------------|:-----------------:|:-------------------:|:-------------:|
30	| Static                   | —                 | —                   | SPON          |
31	| Per-layer                | —                 | ShadowLLM           | —             |
32	| Per-token contextual     | FastForward       | —                   | **Ours**      |
33	
34	Positions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.
35	
36	## Anticipated Reviewer Concerns
37	
38	1. **"Incremental / no new algorithm"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.
39	
40	2. **"KL wins only because more compute"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.
41	
42	3. **"Gumbel-sigmoid relaxation, not KL, explains gains"**: Addressed by STE baseline (plan_002) isolating loss function contribution.
43	
44	4. **"Single model / limited generalization"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).
45	
46	5. **"Effect size may not hold on downstream tasks"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.
47	
48	6. **"Unfair comparison: BCE+comp close to KL but at higher inference cost"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.
49	
50	## Venue Fit
51	- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation
52	- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue
53	- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "49b3c3c1-1c44-46d6-9fa0-1a7161fd73ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper_framing.md",
      "content": "# Paper Framing — distill_sparse_swiglu\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR May 2026 cycle)\n- Deadline: 2026-05-25 (ARR submission)\n- Track: Efficient Methods for NLP\n\n## Core Claims\n\n1. **KL-trained sparsity predictors eliminate the need for error compensation networks**: At 50% model-level sparsity on SwiGLU LLMs, a KL-trained contextual predictor (no compensation) matches or exceeds BCE+compensation quality (FastForward-style), eliminating 67.2M compensation parameters (~256MB, 32 layers × bottleneck MLP) and per-layer GEMV overhead at inference. All quality comparisons must be presented alongside inference cost (params, FLOPs, latency) to prevent \"unfair comparison\" attacks. **Iso-compute evidence (eval_bce_v3_s42)**: with 2.71× more gradient updates, BCE TEAL PPL=27.97 vs KL=12.00 (2.33× gap persists), and BCE loss saturates (step 500→2700: Δ=-0.006). The advantage is structural: BCE optimizes per-neuron binary classification, but inference uses global top-k budget allocation — per-neuron scoring is suboptimal under global reallocation. KL directly optimizes output distribution, naturally compatible with any allocation strategy. (Headline claim)\n\n2. **SPON's static correction is orthogonal to KL and too weak to complement it**: Logit-space decomposition (plan_005) shows SPON's bias correction is near-orthogonal to KL's mask effect (cos_sim=0.196, per-layer ≤0) with only 15.8% relative magnitude. Cross-layer interaction is non-trivial (30.6%) but PPL recovery remains modest (7.3%, 0.23 PPL). Rather than KL \"subsuming\" SPON, the two target different error components—but SPON's component is too small to provide meaningful complementary benefit. Strengthens Claim 1: static correction is not just redundant but irrelevant to the dominant error mode that KL addresses. (Evidence: plan_005_subsumption_s42, spon_2048_s42, D009, D010)\n\n3. **Sparsity regime determines whether allocation or capacity is the bottleneck (phase transition finding)**: Empirical discovery from D030 uniform allocation experiments reveals a qualitative phase transition, not the originally predicted quadratic scaling. At ≤30% sparsity, downstream collapse is caused by per-layer allocation imbalance from global top-k (fixable: uniform per-layer allocation restores MMLU from random→40.6%, surpassing TEAL's 38.6% on knowledge-intensive tasks). At ≥50%, model capacity itself is insufficient — no allocation strategy can recover (uniform MMLU=27.8%≈random). The transition is a gradual degradation band: 30% MMLU=40.6% (dense 62%, allocation-fixable), 40% MMLU=30.7% (partially degraded, PPL-optimal at 8.36 but downstream compromised), 50% MMLU=27.8% (≈random, capacity-limited). Recommended operating point: 30% sparsity with uniform allocation. At 30%, KL uniform dominates on the efficiency-quality Pareto frontier: PPL 8.82 vs TEAL 10.97 (−19.6%), with comparable-to-better downstream (MMLU +2.0pp, WG +2.5pp; ARC-c −1.5pp, GSM8K −0.5pp within noise). The advantage is primarily in PPL and knowledge-intensive tasks, not uniform across all benchmarks. The failure mode changes qualitatively: allocation-fixable (≤30%) vs capacity-limited (≥50%). PPL non-monotonicity (40%=8.36 < 30%=8.82) while downstream is strictly monotonic further supports \"PPL is a poor proxy for downstream quality\" narrative. This yields a practical deployment guideline and a mechanistic understanding of when/why sparse inference degrades. (Evidence: d030_kl30_uniform, d030_kl50_uniform, d030_kl40_uniform, bench_teal30, bench_teal50, bench_kl30_global, bench_kl50_global, lm_eval downstream series)\n\n## Story Spine\n\n- **Problem**: SwiGLU activation sparsity enables 40-60% neuron pruning at inference, but training-free heuristics (WINA/TEAL) leave a 6+ point quality gap, while learned BCE predictors require auxiliary compensation networks adding ~256MB overhead (FastForward).\n\n- **Existing approaches & gaps**: (a) Training-free (WINA, TEAL, R-Sparse): no training cost, but quality gap too large for deployment. (b) Static learned (SPON): zero-overhead bias correction via KL distillation, but input-independent — cannot adapt to per-input neuron importance. (c) Contextual learned (FastForward): BCE predictor + compensation MLP, near-dense quality but inference overhead from compensation network. Gap: no prior work trains the contextual predictor itself with KL, and no work quantifies how much static correction remains useful once a coupled-loss contextual predictor is in place.\n\n- **Our framing / headline question**: \"Does output-distribution distillation (KL) make error compensation unnecessary for contextual sparsity prediction?\" The theoretical grounding: BCE gradient dL_BCE/ds_j depends only on neuron j (factorized), while KL gradient dL_KL/ds_j couples all active neurons through d_logits/dh * dh/dm — a mathematical property of the gradient structure, not an analogy. This means KL captures joint interaction effects that BCE misses, especially at high sparsity.\n\n- **Headline result template**: \"On [benchmarks], a KL-trained predictor at 50% model-level sparsity achieves [X] quality (within [Y]% of dense) without compensation, while BCE+compensation achieves [Z] quality but adds 67.2M parameters ([W] ms/token overhead) — demonstrating that output-distribution distillation renders error compensation unnecessary—SPON's residual correction is orthogonal to KL's dominant effect and too weak to complement it—enabling a simpler, lighter inference pipeline with strictly better efficiency-quality tradeoff.\"\n\n## Two-Dimensional Taxonomy (Conceptual Contribution)\n\n|                          | Decomposed (BCE) | Intermediate (MSE) | Coupled (KL) |\n|--------------------------|:-----------------:|:-------------------:|:-------------:|\n| Static                   | —                 | —                   | SPON          |\n| Per-layer                | —                 | ShadowLLM           | —             |\n| Per-token contextual     | FastForward       | —                   | **Ours**      |\n\nPositions prior work and ours on two axes: correction granularity (static -> per-token) x training signal coupling (decomposed/BCE -> coupled/KL). Highlights the empty cell we fill.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Incremental / no new algorithm\"**: Mitigate with formal decomposition framework, quantitative s^2 prediction, and comprehensive four-quadrant outcome analysis showing all results are informative.\n\n2. **\"KL wins only because more compute\"**: **Fully addressed** by iso-compute ablation (eval_bce_v3_s42): BCE with 2.71× more FLOPs → TEAL PPL=27.97 vs KL=12.00 (2.33× gap). BCE loss saturates, confirming structural mismatch not compute deficit.\n\n3. **\"Gumbel-sigmoid relaxation, not KL, explains gains\"**: Addressed by STE baseline (plan_002) isolating loss function contribution.\n\n4. **\"Single model / limited generalization\"**: Addressed by Mistral-7B-v0.3 validation (plan_009) with different architecture (GQA + sliding window).\n\n5. **\"Effect size may not hold on downstream tasks\"**: Core defense: PPL + 4 discriminative tasks (ARC-c, WinoGrande, MMLU, GSM8K) under unified few-shot protocol across all conditions. LongBench (P1, if GPU budget allows) strengthens long-context coverage. MT-Bench deferred unless time permits — requires external LLM API for judging.\n\n6. **\"Unfair comparison: BCE+comp close to KL but at higher inference cost\"**: All result tables and figures must co-report quality AND inference cost (compensation params, per-token FLOPs, end-to-end latency). Efficiency-accuracy Pareto frontier (plan_007) is the definitive visualization. Even if BCE+comp matches KL on PPL, KL wins on the Pareto frontier — that IS the claim.\n\n## Venue Fit\n- EMNLP Efficient Methods track: strong fit for activation sparsity + distillation\n- NLP-specific evaluation (LongBench long-context, MT-Bench multi-turn) strengthens EMNLP fit vs pure systems venue\n- Novelty ceiling acknowledged: contribution is systematic composition + rigorous ablation, not new architecture\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  }
}
```

</details>

---

### Tool call

_source line 95_

<details open><summary>🔧 Tool call — Read · `toolu_01WPCa6Nj5rtxKX1mFhz51uN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "5f39b4ad-ab9b-4a19-a28e-a7bd3efb3a6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MDAf5ZCa2t8D7UAY2dLxxZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1253,
      "cache_read_input_tokens": 35373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1253
      },
      "output_tokens": 63,
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

_source line 96 · 2026-05-16T12:37:21.585Z_

<details><summary>↩ Tool result · `toolu_01WPCa6Nj5rtxKX1mFhz51uN`</summary>

```text
1	\section{Methodology}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:method:formulation}
6	
7	We consider a pretrained SwiGLU-based language model with $L$ transformer layers.
8	Each feed-forward network (FFN) in layer $\ell$ computes:
9	\begin{equation}
10	\mathbf{h}^{(\ell)} = \bigl(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{gate}}^{(\ell)} \odot \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{up}}^{(\ell)})\bigr) \mathbf{W}_{\text{down}}^{(\ell)},
11	\label{eq:swiglu}
12	\end{equation}
13	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{T \times d}$ is the input hidden state ($d{=}4096$ for Llama-3.1-8B), $\sigma$ denotes SiLU, $\mathbf{W}_{\text{gate}}^{(\ell)}, \mathbf{W}_{\text{up}}^{(\ell)} \in \mathbb{R}^{d \times D}$ and $\mathbf{W}_{\text{down}}^{(\ell)} \in \mathbb{R}^{D \times d}$ are the FFN weight matrices, $D{=}14{,}336$ is the intermediate dimension, and $\odot$ is element-wise multiplication.
14	
15	A substantial fraction of intermediate neurons produce near-zero activation magnitudes $|\mathbf{W}_{\text{gate}}^{(\ell)} \odot \sigma(\mathbf{W}_{\text{up}}^{(\ell)})|$ for any given input, making them candidates for pruning \cite{placeholder_teal,placeholder_dejavu}.
16	Our goal is to train a lightweight \emph{contextual sparsity predictor} $P^{(\ell)}$ for each layer $\ell$ that maps the current hidden state to a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^D$ indicating which neurons to retain.
17	The sparse FFN computation becomes:
18	\begin{equation}
19	\tilde{\mathbf{h}}^{(\ell)} = \bigl(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{gate}}^{(\ell)} \odot \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_{\text{up}}^{(\ell)}) \odot \mathbf{m}^{(\ell)}\bigr) \mathbf{W}_{\text{down}}^{(\ell)}.
20	\label{eq:sparse_ffn}
21	\end{equation}
22	We seek a training objective for $P^{(\ell)}$ that preserves the model's output distribution under sparsification, without requiring auxiliary error compensation networks at inference time.
23	
24	\subsection{Predictor Architecture}
25	\label{sec:method:predictor}
26	
27	Each layer $\ell$ has an independent two-layer MLP predictor:
28	\begin{equation}
29	P^{(\ell)}(\mathbf{x}) = \mathbf{W}_2^{(\ell)}\, \text{ReLU}\!\bigl(\mathbf{W}_1^{(\ell)} \mathbf{x}\bigr),
30	\label{eq:predictor}
31	\end{equation}
32	where $\mathbf{W}_1^{(\ell)} \in \mathbb{R}^{d \times d_b}$ and $\mathbf{W}_2^{(\ell)} \in \mathbb{R}^{d_b \times D}$ with bottleneck dimension $d_b{=}256$.
33	The predictor outputs $D$-dimensional logits $\mathbf{s}^{(\ell)} = P^{(\ell)}(\mathbf{x}^{(\ell)})$, from which the binary mask is derived.
34	The total predictor overhead is 75.96M parameters across 32 layers (${\approx}1\%$ of the 8B base model), requiring no additional parameters at inference beyond the predictors themselves.
35	
36	\subsection{KL Distillation Loss}
37	\label{sec:method:kl}
38	
39	The central design choice is the training objective.
40	Prior contextual sparsity predictors \cite{placeholder_dejavu,placeholder_shadowllm,placeholder_fastforward} train with binary cross-entropy (BCE), treating each neuron as an independent binary classification target against the oracle mask (typically the top-$k$ neurons by activation magnitude).
41	We instead train predictors via output-distribution distillation: the sparse model's logit distribution should match the dense model's.
42	
43	Concretely, let $\mathbf{y}_{\text{dense}} = f(\mathbf{x})$ denote the logits from a full dense forward pass, and $\mathbf{y}_{\text{sparse}} = f(\mathbf{x}; \{\mathbf{m}^{(\ell)}\}_\ell)$ the logits from a forward pass with predictor-generated masks applied at every layer.
44	The loss is the forward KL divergence:
45	\begin{equation}
46	\mathcal{L}_{\text{KL}} = \text{KL}\!\bigl(p_{\text{dense}} \,\|\, p_{\text{sparse}}\bigr) = \sum_{v} p_{\text{dense}}^{(v)} \log \frac{p_{\text{dense}}^{(v)}}{p_{\text{sparse}}^{(v)}},
47	\label{eq:kl_loss}
48	\end{equation}
49	where $p_{\text{dense}} = \text{softmax}(\mathbf{y}_{\text{dense}})$ and $p_{\text{sparse}} = \text{softmax}(\mathbf{y}_{\text{sparse}})$, summed over vocabulary $v$ and averaged over sequence positions.
50	The base model is frozen; only the predictor parameters $\{P^{(\ell)}\}_\ell$ receive gradients.
51	
52	\paragraph{Gradient coupling.}
53	The critical difference from BCE lies in the gradient structure.
54	For a predictor logit $s_j^{(\ell)}$ controlling neuron $j$ in layer $\ell$, the KL gradient is:
55	\begin{equation}
56	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{y}_{\text{sparse}}} \cdot \frac{\partial \mathbf{y}_{\text{sparse}}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial m_j^{(\ell)}} \cdot \frac{\partial m_j^{(\ell)}}{\partial s_j^{(\ell)}}.
57	\label{eq:kl_gradient}
58	\end{equation}
59	The Jacobian $\partial \mathbf{y}_{\text{sparse}} / \partial \mathbf{h}^{(\ell)}$ back-propagates through all downstream layers, coupling the gradient for neuron $j$ to the states of \emph{all} retained neurons across the network.
60	This means the predictor receives a learning signal that reflects how each neuron's inclusion or exclusion jointly affects the output distribution.
61	
62	In contrast, BCE defines a per-neuron loss $\mathcal{L}_{\text{BCE}} = -\sum_j [t_j \log \sigma(s_j) + (1{-}t_j)\log(1{-}\sigma(s_j))]$ against oracle targets $t_j$.
63	Its gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - t_j$ depends only on neuron $j$'s own prediction and target---a factorized signal that cannot capture inter-neuron interactions.
64	At higher sparsity levels, where pruning decisions interact more strongly through the nonlinear forward pass, this factorization becomes increasingly limiting (\S\ref{sec:experiments}).
65	
66	\subsection{Gumbel-Sigmoid Relaxation}
67	\label{sec:method:gumbel}
68	
69	KL distillation requires differentiating through the sparse forward pass, which in turn requires continuous relaxation of the discrete mask.
70	We use Gumbel-sigmoid sampling \cite{placeholder_gumbel}:
71	\begin{equation}
72	m_j^{\text{soft}} = \sigma\!\left(\frac{s_j + g_1 - g_2}{\tau}\right), \quad g_1, g_2 \sim \text{Gumbel}(0,1),
73	\label{eq:gumbel}
74	\end{equation}
75	where $\tau$ is a temperature parameter controlling the sharpness of the relaxation.
76	During training, $\tau$ anneals from 1.0 to 0.1 over the course of optimization, progressively sharpening the soft masks toward binary decisions.
77	At inference, the soft mask is replaced by a hard threshold or folded into the TEAL global allocation (\S\ref{sec:method:teal}).
78	
79	\paragraph{Why not straight-through estimation?}
80	The straight-through estimator (STE)~\cite{placeholder_ste} applies a hard threshold in the forward pass and passes gradients through unchanged.
81	In our setting, STE causes severe training instability: the discrete threshold means small parameter changes can flip large numbers of neurons simultaneously, producing discontinuous jumps in sparsity.
82	This manifests as violent oscillation of the Lagrangian multiplier $\lambda$ (standard deviation 354 over training vs.\ smooth convergence under Gumbel), failure to reach the target sparsity (achieved 47.0\% vs.\ target 50\%), and degraded TEAL PPL (15.77 vs.\ 12.00).
83	Gumbel-sigmoid's continuous relaxation provides smooth gradients that stabilize both the sparsity constraint and the KL objective.
84	
85	\subsection{Lagrangian Sparsity Control}
86	\label{sec:method:lagrangian}
87	
88	We enforce a model-level sparsity target $s_{\text{target}}$ (e.g., 0.5 for 50\% neuron pruning) via an augmented Lagrangian penalty.
89	Let $\bar{s} = \frac{1}{L} \sum_\ell \text{mean}(\mathbf{m}^{(\ell)})$ be the average fraction of \emph{retained} neurons across all layers and tokens in a batch.
90	The total loss is:
91	\begin{equation}
92	\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{KL}} + \lambda \cdot \max\!\bigl(0,\; |\bar{s} - s_{\text{target}}| - \epsilon\bigr),
93	\label{eq:lagrangian}
94	\end{equation}
95	with tolerance $\epsilon{=}0.02$.
96	The multiplier $\lambda$ adapts every 25 steps: if the constraint is violated ($|\bar{s} - s_{\text{target}}| > \epsilon$), $\lambda \leftarrow 2\lambda$; otherwise $\lambda \leftarrow \lambda/2$, clamped to $[0.1, \lambda_{\max}]$ with $\lambda_{\max}{=}5000$ and initial $\lambda_0{=}1.0$.
97	
98	This formulation serves two purposes.
99	First, the tolerance band $\epsilon$ prevents the multiplier from oscillating when sparsity is near the target.
100	Second, the exponential update schedule reacts quickly to large violations (the multiplier can increase 1000$\times$ within 250 steps) while decaying gently when the constraint is satisfied.
101	Unlike a fixed regularization weight, the Lagrangian formulation decouples the sparsity target from the magnitude of the KL loss, which varies across layers and training stages.
102	
103	\subsection{TEAL-Compatible Inference}
104	\label{sec:method:teal}
105	
106	At inference time, we adopt the TEAL global top-$k$ allocation strategy \cite{placeholder_teal} to guarantee exact model-level sparsity.
107	Rather than applying a fixed threshold per layer, TEAL computes a global importance score for every neuron across all layers and retains the top $(1{-}s_{\text{target}}) \times L \times D$ neurons.
108	
109	We compose the predictor with TEAL by defining the importance score for neuron $j$ in layer $\ell$ as:
110	\begin{equation}
111	\text{score}_j^{(\ell)} = \sigma\bigl(s_j^{(\ell)}\bigr) \cdot \bigl|a_j^{(\ell)}\bigr|,
112	\label{eq:teal_score}
113	\end{equation}
114	where $\sigma(s_j^{(\ell)})$ is the predictor's sigmoid probability and $|a_j^{(\ell)}|$ is the activation magnitude.
115	Before global ranking, scores are normalized by per-layer mean to prevent layers with systematically larger activations from dominating the budget.
116	This scoring combines the predictor's learned contextual signal with TEAL's magnitude-based importance, enabling the predictor to redirect the global budget toward neurons it deems critical for output preservation.
117	
118	The inference pipeline requires only a single additional forward pass through the lightweight predictors (${\sim}76$M parameters), with no compensation networks, no auxiliary GEMV operations, and no post-hoc bias correction.
119	
120	\subsection{Training Procedure}
121	\label{sec:method:training}
122	
123	\paragraph{Setup.}
124	The base model (Llama-3.1-8B) is frozen throughout.
125	We train only the predictor parameters on the WikiText-103 training split for 1{,}000 steps with batch size 4 and sequence length 2{,}048.
126	We use AdamW \cite{placeholder_adamw} with learning rate $10^{-3}$, 100-step linear warmup, and cosine decay.
127	Gradient checkpointing is applied to the base model to fit within GPU memory.
128	
129	\paragraph{Computational cost.}
130	Each KL training step requires two forward passes through the base model (one dense for the reference distribution, one sparse with predictor masks) plus a backward pass through the sparse path.
131	This is $2.71\times$ the per-step cost of BCE training, which only requires the dense forward pass to extract oracle targets followed by a predictor-only backward pass.
132	The total training cost is approximately 550 GPU-seconds on two RTX PRO 6000 Blackwell GPUs (1{,}000 steps $\times$ 0.549s/step).
133	
134	\begin{algorithm}[t]
135	\caption{KL-Distilled Sparsity Predictor Training}
136	\label{alg:training}
137	\begin{algorithmic}[1]
138	\REQUIRE Dense model $f$, target sparsity $s_{\text{target}}$, tolerance $\epsilon$, steps $N$
139	\STATE Initialize predictors $\{P^{(\ell)}\}_{\ell=1}^{L}$; $\lambda \leftarrow 1.0$; $\tau \leftarrow 1.0$
140	\FOR{step $= 1$ \TO $N$}
141	    \STATE Sample batch $\mathbf{x}$
142	    \STATE $\mathbf{y}_{\text{dense}} \leftarrow f(\mathbf{x})$ \hfill \COMMENT{dense forward, no grad}
143	    \FOR{each layer $\ell$}
144	        \STATE $\mathbf{s}^{(\ell)} \leftarrow P^{(\ell)}(\mathbf{x}^{(\ell)})$
145	        \STATE $\mathbf{m}^{(\ell)} \leftarrow \sigma\!\bigl((\mathbf{s}^{(\ell)} + g_1 - g_2)/\tau\bigr)$ \hfill \COMMENT{Gumbel-sigmoid}
146	    \ENDFOR
147	    \STATE $\mathbf{y}_{\text{sparse}} \leftarrow f(\mathbf{x}; \{\mathbf{m}^{(\ell)}\}_\ell)$ \hfill \COMMENT{sparse forward, with grad}
148	    \STATE $\mathcal{L}_{\text{KL}} \leftarrow \text{KL}(p_{\text{dense}} \| p_{\text{sparse}})$
149	    \STATE $\bar{s} \leftarrow \text{mean}(\{\mathbf{m}^{(\ell)}\})$
150	    \STATE $\mathcal{L}_{\text{total}} \leftarrow \mathcal{L}_{\text{KL}} + \lambda \cdot \max(0, |\bar{s} - s_{\text{target}}| - \epsilon)$
151	    \STATE Update $\{P^{(\ell)}\}$ via AdamW on $\mathcal{L}_{\text{total}}$
152	    \IF{step $\bmod$ 25 $= 0$}
153	        \STATE $\lambda \leftarrow \begin{cases} \min(2\lambda,\, \lambda_{\max}) & \text{if } |\bar{s} - s_{\text{target}}| > \epsilon \\ \max(\lambda/2,\, 0.1) & \text{otherwise}\end{cases}$
154	    \ENDIF
155	    \STATE $\tau \leftarrow \text{anneal}(\tau)$ \hfill \COMMENT{$1.0 \to 0.1$, cosine schedule}
156	\ENDFOR
157	\RETURN $\{P^{(\ell)}\}_{\ell=1}^{L}$
158	\end{algorithmic}
159	\end{algorithm}
160	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "55e99cca-a2ae-40d8-b71a-32621126257a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Methodology}\n\\label{sec:method}\n\n\\subsection{Problem Formulation}\n\\label{sec:method:formulation}\n\nWe consider a pretrained SwiGLU-based language model with $L$ transformer layers.\nEach feed-forward network (FFN) in layer $\\ell$ computes:\n\\begin{equation}\n\\mathbf{h}^{(\\ell)} = \\bigl(\\mathbf{x}^{(\\ell)} \\mathbf{W}_{\\text{gate}}^{(\\ell)} \\odot \\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_{\\text{up}}^{(\\ell)})\\bigr) \\mathbf{W}_{\\text{down}}^{(\\ell)},\n\\label{eq:swiglu}\n\\end{equation}\nwhere $\\mathbf{x}^{(\\ell)} \\in \\mathbb{R}^{T \\times d}$ is the input hidden state ($d{=}4096$ for Llama-3.1-8B), $\\sigma$ denotes SiLU, $\\mathbf{W}_{\\text{gate}}^{(\\ell)}, \\mathbf{W}_{\\text{up}}^{(\\ell)} \\in \\mathbb{R}^{d \\times D}$ and $\\mathbf{W}_{\\text{down}}^{(\\ell)} \\in \\mathbb{R}^{D \\times d}$ are the FFN weight matrices, $D{=}14{,}336$ is the intermediate dimension, and $\\odot$ is element-wise multiplication.\n\nA substantial fraction of intermediate neurons produce near-zero activation magnitudes $|\\mathbf{W}_{\\text{gate}}^{(\\ell)} \\odot \\sigma(\\mathbf{W}_{\\text{up}}^{(\\ell)})|$ for any given input, making them candidates for pruning \\cite{placeholder_teal,placeholder_dejavu}.\nOur goal is to train a lightweight \\emph{contextual sparsity predictor} $P^{(\\ell)}$ for each layer $\\ell$ that maps the current hidden state to a binary mask $\\mathbf{m}^{(\\ell)} \\in \\{0,1\\}^D$ indicating which neurons to retain.\nThe sparse FFN computation becomes:\n\\begin{equation}\n\\tilde{\\mathbf{h}}^{(\\ell)} = \\bigl(\\mathbf{x}^{(\\ell)} \\mathbf{W}_{\\text{gate}}^{(\\ell)} \\odot \\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_{\\text{up}}^{(\\ell)}) \\odot \\mathbf{m}^{(\\ell)}\\bigr) \\mathbf{W}_{\\text{down}}^{(\\ell)}.\n\\label{eq:sparse_ffn}\n\\end{equation}\nWe seek a training objective for $P^{(\\ell)}$ that preserves the model's output distribution under sparsification, without requiring auxiliary error compensation networks at inference time.\n\n\\subsection{Predictor Architecture}\n\\label{sec:method:predictor}\n\nEach layer $\\ell$ has an independent two-layer MLP predictor:\n\\begin{equation}\nP^{(\\ell)}(\\mathbf{x}) = \\mathbf{W}_2^{(\\ell)}\\, \\text{ReLU}\\!\\bigl(\\mathbf{W}_1^{(\\ell)} \\mathbf{x}\\bigr),\n\\label{eq:predictor}\n\\end{equation}\nwhere $\\mathbf{W}_1^{(\\ell)} \\in \\mathbb{R}^{d \\times d_b}$ and $\\mathbf{W}_2^{(\\ell)} \\in \\mathbb{R}^{d_b \\times D}$ with bottleneck dimension $d_b{=}256$.\nThe predictor outputs $D$-dimensional logits $\\mathbf{s}^{(\\ell)} = P^{(\\ell)}(\\mathbf{x}^{(\\ell)})$, from which the binary mask is derived.\nThe total predictor overhead is 75.96M parameters across 32 layers (${\\approx}1\\%$ of the 8B base model), requiring no additional parameters at inference beyond the predictors themselves.\n\n\\subsection{KL Distillation Loss}\n\\label{sec:method:kl}\n\nThe central design choice is the training objective.\nPrior contextual sparsity predictors \\cite{placeholder_dejavu,placeholder_shadowllm,placeholder_fastforward} train with binary cross-entropy (BCE), treating each neuron as an independent binary classification target against the oracle mask (typically the top-$k$ neurons by activation magnitude).\nWe instead train predictors via output-distribution distillation: the sparse model's logit distribution should match the dense model's.\n\nConcretely, let $\\mathbf{y}_{\\text{dense}} = f(\\mathbf{x})$ denote the logits from a full dense forward pass, and $\\mathbf{y}_{\\text{sparse}} = f(\\mathbf{x}; \\{\\mathbf{m}^{(\\ell)}\\}_\\ell)$ the logits from a forward pass with predictor-generated masks applied at every layer.\nThe loss is the forward KL divergence:\n\\begin{equation}\n\\mathcal{L}_{\\text{KL}} = \\text{KL}\\!\\bigl(p_{\\text{dense}} \\,\\|\\, p_{\\text{sparse}}\\bigr) = \\sum_{v} p_{\\text{dense}}^{(v)} \\log \\frac{p_{\\text{dense}}^{(v)}}{p_{\\text{sparse}}^{(v)}},\n\\label{eq:kl_loss}\n\\end{equation}\nwhere $p_{\\text{dense}} = \\text{softmax}(\\mathbf{y}_{\\text{dense}})$ and $p_{\\text{sparse}} = \\text{softmax}(\\mathbf{y}_{\\text{sparse}})$, summed over vocabulary $v$ and averaged over sequence positions.\nThe base model is frozen; only the predictor parameters $\\{P^{(\\ell)}\\}_\\ell$ receive gradients.\n\n\\paragraph{Gradient coupling.}\nThe critical difference from BCE lies in the gradient structure.\nFor a predictor logit $s_j^{(\\ell)}$ controlling neuron $j$ in layer $\\ell$, the KL gradient is:\n\\begin{equation}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{y}_{\\text{sparse}}} \\cdot \\frac{\\partial \\mathbf{y}_{\\text{sparse}}}{\\partial \\mathbf{h}^{(\\ell)}} \\cdot \\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial m_j^{(\\ell)}} \\cdot \\frac{\\partial m_j^{(\\ell)}}{\\partial s_j^{(\\ell)}}.\n\\label{eq:kl_gradient}\n\\end{equation}\nThe Jacobian $\\partial \\mathbf{y}_{\\text{sparse}} / \\partial \\mathbf{h}^{(\\ell)}$ back-propagates through all downstream layers, coupling the gradient for neuron $j$ to the states of \\emph{all} retained neurons across the network.\nThis means the predictor receives a learning signal that reflects how each neuron's inclusion or exclusion jointly affects the output distribution.\n\nIn contrast, BCE defines a per-neuron loss $\\mathcal{L}_{\\text{BCE}} = -\\sum_j [t_j \\log \\sigma(s_j) + (1{-}t_j)\\log(1{-}\\sigma(s_j))]$ against oracle targets $t_j$.\nIts gradient $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j = \\sigma(s_j) - t_j$ depends only on neuron $j$'s own prediction and target---a factorized signal that cannot capture inter-neuron interactions.\nAt higher sparsity levels, where pruning decisions interact more strongly through the nonlinear forward pass, this factorization becomes increasingly limiting (\\S\\ref{sec:experiments}).\n\n\\subsection{Gumbel-Sigmoid Relaxation}\n\\label{sec:method:gumbel}\n\nKL distillation requires differentiating through the sparse forward pass, which in turn requires continuous relaxation of the discrete mask.\nWe use Gumbel-sigmoid sampling \\cite{placeholder_gumbel}:\n\\begin{equation}\nm_j^{\\text{soft}} = \\sigma\\!\\left(\\frac{s_j + g_1 - g_2}{\\tau}\\right), \\quad g_1, g_2 \\sim \\text{Gumbel}(0,1),\n\\label{eq:gumbel}\n\\end{equation}\nwhere $\\tau$ is a temperature parameter controlling the sharpness of the relaxation.\nDuring training, $\\tau$ anneals from 1.0 to 0.1 over the course of optimization, progressively sharpening the soft masks toward binary decisions.\nAt inference, the soft mask is replaced by a hard threshold or folded into the TEAL global allocation (\\S\\ref{sec:method:teal}).\n\n\\paragraph{Why not straight-through estimation?}\nThe straight-through estimator (STE)~\\cite{placeholder_ste} applies a hard threshold in the forward pass and passes gradients through unchanged.\nIn our setting, STE causes severe training instability: the discrete threshold means small parameter changes can flip large numbers of neurons simultaneously, producing discontinuous jumps in sparsity.\nThis manifests as violent oscillation of the Lagrangian multiplier $\\lambda$ (standard deviation 354 over training vs.\\ smooth convergence under Gumbel), failure to reach the target sparsity (achieved 47.0\\% vs.\\ target 50\\%), and degraded TEAL PPL (15.77 vs.\\ 12.00).\nGumbel-sigmoid's continuous relaxation provides smooth gradients that stabilize both the sparsity constraint and the KL objective.\n\n\\subsection{Lagrangian Sparsity Control}\n\\label{sec:method:lagrangian}\n\nWe enforce a model-level sparsity target $s_{\\text{target}}$ (e.g., 0.5 for 50\\% neuron pruning) via an augmented Lagrangian penalty.\nLet $\\bar{s} = \\frac{1}{L} \\sum_\\ell \\text{mean}(\\mathbf{m}^{(\\ell)})$ be the average fraction of \\emph{retained} neurons across all layers and tokens in a batch.\nThe total loss is:\n\\begin{equation}\n\\mathcal{L}_{\\text{total}} = \\mathcal{L}_{\\text{KL}} + \\lambda \\cdot \\max\\!\\bigl(0,\\; |\\bar{s} - s_{\\text{target}}| - \\epsilon\\bigr),\n\\label{eq:lagrangian}\n\\end{equation}\nwith tolerance $\\epsilon{=}0.02$.\nThe multiplier $\\lambda$ adapts every 25 steps: if the constraint is violated ($|\\bar{s} - s_{\\text{target}}| > \\epsilon$), $\\lambda \\leftarrow 2\\lambda$; otherwise $\\lambda \\leftarrow \\lambda/2$, clamped to $[0.1, \\lambda_{\\max}]$ with $\\lambda_{\\max}{=}5000$ and initial $\\lambda_0{=}1.0$.\n\nThis formulation serves two purposes.\nFirst, the tolerance band $\\epsilon$ prevents the multiplier from oscillating when sparsity is near the target.\nSecond, the exponential update schedule reacts quickly to large violations (the multiplier can increase 1000$\\times$ within 250 steps) while decaying gently when the constraint is satisfied.\nUnlike a fixed regularization weight, the Lagrangian formulation decouples the sparsity target from the magnitude of the KL loss, which varies across layers and training stages.\n\n\\subsection{TEAL-Compatible Inference}\n\\label{sec:method:teal}\n\nAt inference time, we adopt the TEAL global top-$k$ allocation strategy \\cite{placeholder_teal} to guarantee exact model-level sparsity.\nRather than applying a fixed threshold per layer, TEAL computes a global importance score for every neuron across all layers and retains the top $(1{-}s_{\\text{target}}) \\times L \\times D$ neurons.\n\nWe compose the predictor with TEAL by defining the importance score for neuron $j$ in layer $\\ell$ as:\n\\begin{equation}\n\\text{score}_j^{(\\ell)} = \\sigma\\bigl(s_j^{(\\ell)}\\bigr) \\cdot \\bigl|a_j^{(\\ell)}\\bigr|,\n\\label{eq:teal_score}\n\\end{equation}\nwhere $\\sigma(s_j^{(\\ell)})$ is the predictor's sigmoid probability and $|a_j^{(\\ell)}|$ is the activation magnitude.\nBefore global ranking, scores are normalized by per-layer mean to prevent layers with systematically larger activations from dominating the budget.\nThis scoring combines the predictor's learned contextual signal with TEAL's magnitude-based importance, enabling the predictor to redirect the global budget toward neurons it deems critical for output preservation.\n\nThe inference pipeline requires only a single additional forward pass through the lightweight predictors (${\\sim}76$M parameters), with no compensation networks, no auxiliary GEMV operations, and no post-hoc bias correction.\n\n\\subsection{Training Procedure}\n\\label{sec:method:training}\n\n\\paragraph{Setup.}\nThe base model (Llama-3.1-8B) is frozen throughout.\nWe train only the predictor parameters on the WikiText-103 training split for 1{,}000 steps with batch size 4 and sequence length 2{,}048.\nWe use AdamW \\cite{placeholder_adamw} with learning rate $10^{-3}$, 100-step linear warmup, and cosine decay.\nGradient checkpointing is applied to the base model to fit within GPU memory.\n\n\\paragraph{Computational cost.}\nEach KL training step requires two forward passes through the base model (one dense for the reference distribution, one sparse with predictor masks) plus a backward pass through the sparse path.\nThis is $2.71\\times$ the per-step cost of BCE training, which only requires the dense forward pass to extract oracle targets followed by a predictor-only backward pass.\nThe total training cost is approximately 550 GPU-seconds on two RTX PRO 6000 Blackwell GPUs (1{,}000 steps $\\times$ 0.549s/step).\n\n\\begin{algorithm}[t]\n\\caption{KL-Distilled Sparsity Predictor Training}\n\\label{alg:training}\n\\begin{algorithmic}[1]\n\\REQUIRE Dense model $f$, target sparsity $s_{\\text{target}}$, tolerance $\\epsilon$, steps $N$\n\\STATE Initialize predictors $\\{P^{(\\ell)}\\}_{\\ell=1}^{L}$; $\\lambda \\leftarrow 1.0$; $\\tau \\leftarrow 1.0$\n\\FOR{step $= 1$ \\TO $N$}\n    \\STATE Sample batch $\\mathbf{x}$\n    \\STATE $\\mathbf{y}_{\\text{dense}} \\leftarrow f(\\mathbf{x})$ \\hfill \\COMMENT{dense forward, no grad}\n    \\FOR{each layer $\\ell$}\n        \\STATE $\\mathbf{s}^{(\\ell)} \\leftarrow P^{(\\ell)}(\\mathbf{x}^{(\\ell)})$\n        \\STATE $\\mathbf{m}^{(\\ell)} \\leftarrow \\sigma\\!\\bigl((\\mathbf{s}^{(\\ell)} + g_1 - g_2)/\\tau\\bigr)$ \\hfill \\COMMENT{Gumbel-sigmoid}\n    \\ENDFOR\n    \\STATE $\\mathbf{y}_{\\text{sparse}} \\leftarrow f(\\mathbf{x}; \\{\\mathbf{m}^{(\\ell)}\\}_\\ell)$ \\hfill \\COMMENT{sparse forward, with grad}\n    \\STATE $\\mathcal{L}_{\\text{KL}} \\leftarrow \\text{KL}(p_{\\text{dense}} \\| p_{\\text{sparse}})$\n    \\STATE $\\bar{s} \\leftarrow \\text{mean}(\\{\\mathbf{m}^{(\\ell)}\\})$\n    \\STATE $\\mathcal{L}_{\\text{total}} \\leftarrow \\mathcal{L}_{\\text{KL}} + \\lambda \\cdot \\max(0, |\\bar{s} - s_{\\text{target}}| - \\epsilon)$\n    \\STATE Update $\\{P^{(\\ell)}\\}$ via AdamW on $\\mathcal{L}_{\\text{total}}$\n    \\IF{step $\\bmod$ 25 $= 0$}\n        \\STATE $\\lambda \\leftarrow \\begin{cases} \\min(2\\lambda,\\, \\lambda_{\\max}) & \\text{if } |\\bar{s} - s_{\\text{target}}| > \\epsilon \\\\ \\max(\\lambda/2,\\, 0.1) & \\text{otherwise}\\end{cases}$\n    \\ENDIF\n    \\STATE $\\tau \\leftarrow \\text{anneal}(\\tau)$ \\hfill \\COMMENT{$1.0 \\to 0.1$, cosine schedule}\n\\ENDFOR\n\\RETURN $\\{P^{(\\ell)}\\}_{\\ell=1}^{L}$\n\\end{algorithmic}\n\\end{algorithm}\n",
      "numLines": 160,
      "startLine": 1,
      "totalLines": 160
    }
  }
}
```

</details>

---

### Assistant

_source line 97_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me also check the references.bib file to make sure I use the correct citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "afbf4a77-004d-42bd-b3b6-1cf7c7437cb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5ctpMPJM2hDwoyiaZs2fG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7395,
      "cache_read_input_tokens": 36626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7395
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

_source line 98_

<details open><summary>🔧 Tool call — Read · `toolu_01RqZssQko8pWBkYjoRXWFej`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "375c7a88-0710-47db-8500-741722ce9390",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5ctpMPJM2hDwoyiaZs2fG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7395,
      "cache_read_input_tokens": 36626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7395
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

_source line 99 · 2026-05-16T12:37:26.292Z_

<details><summary>↩ Tool result · `toolu_01RqZssQko8pWBkYjoRXWFej`</summary>

```text
1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{xu2026spon,
6	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
7	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
8	  year = {2026},
9	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
10	  url = {https://arxiv.org/abs/2512.12744},
11	}
12	
13	@inproceedings{muralidharan2024minitron,
14	  title = {Compact Language Models via Pruning and Knowledge Distillation},
15	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
16	  year = {2024},
17	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
18	  url = {https://arxiv.org/abs/2407.14679},
19	}
20	
21	@inproceedings{hou2025instruction,
22	  title = {Instruction-Following Pruning for Large Language Models},
23	  author = {Bairu Hou and Qibin Chen and Jianyu Wang and Guoli Yin and Chong Wang and Nan Du and Ruoming Pang and Shiyu Chang and Tao Lei},
24	  year = {2025},
25	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
26	  url = {https://arxiv.org/abs/2501.02086},
27	}
28	
29	% =============================================================================
30	% Direction 2: Output distribution preservation in pruning/sparsity
31	% =============================================================================
32	
33	@article{unknown2025distilling,
34	  title = {Distilling to Hybrid Attention Models via KL-Guided Layer Selection},
35	  author = {Unknown},
36	  year = {2025},
37	  journal = {arXiv preprint arXiv:2512.20569},
38	  url = {https://arxiv.org/abs/2512.20569},
39	}
40	
41	% =============================================================================
42	% Direction 3: SPON and learnable bias correction for sparsity
43	% =============================================================================
44	
45	@article{gautam2026fastforward,
46	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
47	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},
48	  year = {2026},
49	  journal = {arXiv preprint arXiv:2602.00397},
50	  url = {https://arxiv.org/abs/2602.00397},
51	}
52	
53	@article{an2025amber,
54	  title = {Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models},
55	  author = {Tai An and Ruwu Cai and Yanzhe Zhang and Yang Liu and Hao Chen and Pengcheng Xie and Sheng Chang and Yiwu Yao and Gongyi Wang},
56	  year = {2025},
57	  journal = {arXiv preprint arXiv:2508.02128},
58	  url = {https://arxiv.org/abs/2508.02128},
59	}
60	
61	% =============================================================================
62	% Direction 4: Predictor-based activation sparsity
63	% =============================================================================
64	
65	@inproceedings{liu2025teal,
66	  title = {Training-Free Activation Sparsity in Large Language Models},
67	  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},
68	  year = {2025},
69	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
70	  url = {https://arxiv.org/abs/2408.14690},
71	}
72	
73	@inproceedings{liu2023dejavu,
74	  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},
75	  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},
76	  year = {2023},
77	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
78	  url = {https://arxiv.org/abs/2310.17157},
79	}
80	
81	@inproceedings{akhauri2024shadowllm,
82	  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},
83	  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},
84	  year = {2024},
85	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
86	  url = {https://arxiv.org/abs/2406.16635},
87	}
88	
89	@inproceedings{shin2025sparseinfer,
90	  title = {SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference},
91	  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},
92	  year = {2025},
93	  booktitle = {Proceedings of the Design, Automation and Test in Europe Conference (DATE)},
94	  url = {https://arxiv.org/abs/2411.12692},
95	}
96	
97	@article{serbin2026svdcsp,
98	  title = {SVD Contextual Sparsity Predictors for Fast LLM Inference},
99	  author = {Georgii Serbin and Kirill Koshkin and Zhongao Sun and Anastasiya Bistrigova and C.C. Korikov},
100	  year = {2026},
101	  journal = {arXiv preprint arXiv:2603.14110},
102	  url = {https://arxiv.org/abs/2603.14110},
103	}
104	
105	@article{lee2024cats,
106	  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},
107	  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},
108	  year = {2024},
109	  journal = {arXiv preprint arXiv:2404.08763},
110	  url = {https://arxiv.org/abs/2404.08763},
111	}
112	
113	@inproceedings{zhang2025rsparse,
114	  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},
115	  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},
116	  year = {2025},
117	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
118	  url = {https://arxiv.org/abs/2504.19449},
119	}
120	
121	@inproceedings{federici2025dip,
122	  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},
123	  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},
124	  year = {2024},
125	  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},
126	  url = {https://arxiv.org/abs/2412.01380},
127	}
128	
129	% =============================================================================
130	% Activation function replacement and sparsity enhancement
131	% =============================================================================
132	
133	@inproceedings{mirzadeh2024relu,
134	  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},
135	  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},
136	  year = {2024},
137	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
138	  url = {https://arxiv.org/abs/2310.04564},
139	}
140	
141	@article{song2024turbosparse,
142	  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},
143	  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},
144	  year = {2024},
145	  journal = {arXiv preprint arXiv:2406.05955},
146	  url = {https://arxiv.org/abs/2406.05955},
147	}
148	
149	@inproceedings{song2025prosparse,
150	  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},
151	  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},
152	  year = {2025},
153	  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},
154	  url = {https://arxiv.org/abs/2402.13516},
155	}
156	
157	@article{luo2024sparsinglaw,
158	  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},
159	  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},
160	  year = {2024},
161	  journal = {arXiv preprint arXiv:2411.02335},
162	  url = {https://arxiv.org/abs/2411.02335},
163	}
164	
165	@inproceedings{dhar2025clustering,
166	  title = {A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering},
167	  author = {Nobel Dhar and Bobin Deng and Md Romyull Islam and Xinyue Zhang and Kazi Fahim Ahmad Nasif and Kun Suo},
168	  year = {2025},
169	  booktitle = {Proceedings of Euro-Par},
170	  url = {https://arxiv.org/abs/2507.14179},
171	}
172	
173	@inproceedings{song2024powerinfer,
174	  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},
175	  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},
176	  year = {2024},
177	  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},
178	  url = {https://arxiv.org/abs/2312.12456},
179	}
180	
181	@inproceedings{shrestha2025polar,
182	  title = {Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity},
183	  author = {Susav Shrestha and Brad Settlemyer and Nikoli Dryden and Narasimha Reddy},
184	  year = {2025},
185	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
186	  url = {https://arxiv.org/abs/2505.14884},
187	}
188	
189	% =============================================================================
190	% KL distillation for model compression
191	% =============================================================================
192	
193	@inproceedings{gu2024minillm,
194	  title = {MiniLLM: Knowledge Distillation of Large Language Models},
195	  author = {Yuxian Gu and Li Dong and Furu Wei and Minlie Huang},
196	  year = {2024},
197	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
198	  url = {https://arxiv.org/abs/2306.08543},
199	}
200	
201	@inproceedings{ko2024distillm,
202	  title = {DistiLLM: Towards Streamlined Distillation for Large Language Models},
203	  author = {Jongwoo Ko and Sungnyun Kim and Tianyi Chen and Se-Young Yun},
204	  year = {2024},
205	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
206	  url = {https://arxiv.org/abs/2402.03898},
207	}
208	
209	@inproceedings{wu2025rethinking,
210	  title = {Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models},
211	  author = {Taiqiang Wu and Chaofan Tao and Jiahao Wang and Runming Yang and Zhe Zhao and Ngai Wong},
212	  year = {2025},
213	  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},
214	  url = {https://arxiv.org/abs/2404.02657},
215	}
216	
217	% =============================================================================
218	% Foundational references
219	% =============================================================================
220	
221	@article{grattafiori2024llama3,
222	  title = {The Llama 3 Herd of Models},
223	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},
224	  year = {2024},
225	  journal = {arXiv preprint arXiv:2407.21783},
226	  url = {https://arxiv.org/abs/2407.21783},
227	}
228	
229	@article{jiang2023mistral,
230	  title = {Mistral 7B},
231	  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},
232	  year = {2023},
233	  journal = {arXiv preprint arXiv:2310.06825},
234	  url = {https://arxiv.org/abs/2310.06825},
235	}
236	
237	@inproceedings{jang2017gumbel,
238	  title = {Categorical Reparameterization with Gumbel-Softmax},
239	  author = {Eric Jang and Shixiang Gu and Ben Poole},
240	  year = {2017},
241	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
242	  url = {https://arxiv.org/abs/1611.01144},
243	}
244	
245	@article{shazeer2020glu,
246	  title = {GLU Variants Improve Transformer},
247	  author = {Noam Shazeer},
248	  year = {2020},
249	  journal = {arXiv preprint arXiv:2002.05202},
250	  url = {https://arxiv.org/abs/2002.05202},
251	}
252	
253	@inproceedings{merity2017pointer,
254	  title = {Pointer Sentinel Mixture Models},
255	  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},
256	  year = {2017},
257	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
258	  url = {https://arxiv.org/abs/1609.07843},
259	}
260	
261	@inproceedings{hinton2015distilling,
262	  title = {Distilling the Knowledge in a Neural Network},
263	  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},
264	  year = {2015},
265	  booktitle = {NeurIPS 2014 Deep Learning Workshop},
266	  url = {https://arxiv.org/abs/1503.02531},
267	}
268	
269	@article{bengio2013ste,
270	  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},
271	  author = {Yoshua Bengio and Nicholas L\'{e}onard and Aaron Courville},
272	  year = {2013},
273	  journal = {arXiv preprint arXiv:1308.3432},
274	  url = {https://arxiv.org/abs/1308.3432},
275	}
276	
277	@article{raffel2020t5,
278	  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
279	  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
280	  year = {2020},
281	  journal = {Journal of Machine Learning Research},
282	  url = {https://arxiv.org/abs/1910.10683},
283	}
284	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "0cefc1f6-5a5a-411b-9a01-21f515a12931",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib",
      "content": "% =============================================================================\n% Direction 1: KL distillation for structured/activation sparsity\n% =============================================================================\n\n@inproceedings{xu2026spon,\n  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},\n  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},\n  year = {2026},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2512.12744},\n}\n\n@inproceedings{muralidharan2024minitron,\n  title = {Compact Language Models via Pruning and Knowledge Distillation},\n  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},\n  year = {2024},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2407.14679},\n}\n\n@inproceedings{hou2025instruction,\n  title = {Instruction-Following Pruning for Large Language Models},\n  author = {Bairu Hou and Qibin Chen and Jianyu Wang and Guoli Yin and Chong Wang and Nan Du and Ruoming Pang and Shiyu Chang and Tao Lei},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2501.02086},\n}\n\n% =============================================================================\n% Direction 2: Output distribution preservation in pruning/sparsity\n% =============================================================================\n\n@article{unknown2025distilling,\n  title = {Distilling to Hybrid Attention Models via KL-Guided Layer Selection},\n  author = {Unknown},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2512.20569},\n  url = {https://arxiv.org/abs/2512.20569},\n}\n\n% =============================================================================\n% Direction 3: SPON and learnable bias correction for sparsity\n% =============================================================================\n\n@article{gautam2026fastforward,\n  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},\n  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2602.00397},\n  url = {https://arxiv.org/abs/2602.00397},\n}\n\n@article{an2025amber,\n  title = {Amber Pruner: Leveraging N:M Activation Sparsity for Efficient Prefill in Large Language Models},\n  author = {Tai An and Ruwu Cai and Yanzhe Zhang and Yang Liu and Hao Chen and Pengcheng Xie and Sheng Chang and Yiwu Yao and Gongyi Wang},\n  year = {2025},\n  journal = {arXiv preprint arXiv:2508.02128},\n  url = {https://arxiv.org/abs/2508.02128},\n}\n\n% =============================================================================\n% Direction 4: Predictor-based activation sparsity\n% =============================================================================\n\n@inproceedings{liu2025teal,\n  title = {Training-Free Activation Sparsity in Large Language Models},\n  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2408.14690},\n}\n\n@inproceedings{liu2023dejavu,\n  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},\n  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},\n  year = {2023},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2310.17157},\n}\n\n@inproceedings{akhauri2024shadowllm,\n  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},\n  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},\n  year = {2024},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},\n  url = {https://arxiv.org/abs/2406.16635},\n}\n\n@inproceedings{shin2025sparseinfer,\n  title = {SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference},\n  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},\n  year = {2025},\n  booktitle = {Proceedings of the Design, Automation and Test in Europe Conference (DATE)},\n  url = {https://arxiv.org/abs/2411.12692},\n}\n\n@article{serbin2026svdcsp,\n  title = {SVD Contextual Sparsity Predictors for Fast LLM Inference},\n  author = {Georgii Serbin and Kirill Koshkin and Zhongao Sun and Anastasiya Bistrigova and C.C. Korikov},\n  year = {2026},\n  journal = {arXiv preprint arXiv:2603.14110},\n  url = {https://arxiv.org/abs/2603.14110},\n}\n\n@article{lee2024cats,\n  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},\n  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2404.08763},\n  url = {https://arxiv.org/abs/2404.08763},\n}\n\n@inproceedings{zhang2025rsparse,\n  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},\n  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2504.19449},\n}\n\n@inproceedings{federici2025dip,\n  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},\n  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},\n  year = {2024},\n  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},\n  url = {https://arxiv.org/abs/2412.01380},\n}\n\n% =============================================================================\n% Activation function replacement and sparsity enhancement\n% =============================================================================\n\n@inproceedings{mirzadeh2024relu,\n  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},\n  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2310.04564},\n}\n\n@article{song2024turbosparse,\n  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},\n  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2406.05955},\n  url = {https://arxiv.org/abs/2406.05955},\n}\n\n@inproceedings{song2025prosparse,\n  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},\n  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2402.13516},\n}\n\n@article{luo2024sparsinglaw,\n  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},\n  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2411.02335},\n  url = {https://arxiv.org/abs/2411.02335},\n}\n\n@inproceedings{dhar2025clustering,\n  title = {A Sparsity Predicting Approach for Large Language Models via Activation Pattern Clustering},\n  author = {Nobel Dhar and Bobin Deng and Md Romyull Islam and Xinyue Zhang and Kazi Fahim Ahmad Nasif and Kun Suo},\n  year = {2025},\n  booktitle = {Proceedings of Euro-Par},\n  url = {https://arxiv.org/abs/2507.14179},\n}\n\n@inproceedings{song2024powerinfer,\n  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},\n  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},\n  year = {2024},\n  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},\n  url = {https://arxiv.org/abs/2312.12456},\n}\n\n@inproceedings{shrestha2025polar,\n  title = {Polar Sparsity: High Throughput Batched LLM Inferencing with Scalable Contextual Sparsity},\n  author = {Susav Shrestha and Brad Settlemyer and Nikoli Dryden and Narasimha Reddy},\n  year = {2025},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  url = {https://arxiv.org/abs/2505.14884},\n}\n\n% =============================================================================\n% KL distillation for model compression\n% =============================================================================\n\n@inproceedings{gu2024minillm,\n  title = {MiniLLM: Knowledge Distillation of Large Language Models},\n  author = {Yuxian Gu and Li Dong and Furu Wei and Minlie Huang},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/2306.08543},\n}\n\n@inproceedings{ko2024distillm,\n  title = {DistiLLM: Towards Streamlined Distillation for Large Language Models},\n  author = {Jongwoo Ko and Sungnyun Kim and Tianyi Chen and Se-Young Yun},\n  year = {2024},\n  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},\n  url = {https://arxiv.org/abs/2402.03898},\n}\n\n@inproceedings{wu2025rethinking,\n  title = {Rethinking Kullback-Leibler Divergence in Knowledge Distillation for Large Language Models},\n  author = {Taiqiang Wu and Chaofan Tao and Jiahao Wang and Runming Yang and Zhe Zhao and Ngai Wong},\n  year = {2025},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},\n  url = {https://arxiv.org/abs/2404.02657},\n}\n\n% =============================================================================\n% Foundational references\n% =============================================================================\n\n@article{grattafiori2024llama3,\n  title = {The Llama 3 Herd of Models},\n  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},\n  year = {2024},\n  journal = {arXiv preprint arXiv:2407.21783},\n  url = {https://arxiv.org/abs/2407.21783},\n}\n\n@article{jiang2023mistral,\n  title = {Mistral 7B},\n  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},\n  year = {2023},\n  journal = {arXiv preprint arXiv:2310.06825},\n  url = {https://arxiv.org/abs/2310.06825},\n}\n\n@inproceedings{jang2017gumbel,\n  title = {Categorical Reparameterization with Gumbel-Softmax},\n  author = {Eric Jang and Shixiang Gu and Ben Poole},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1611.01144},\n}\n\n@article{shazeer2020glu,\n  title = {GLU Variants Improve Transformer},\n  author = {Noam Shazeer},\n  year = {2020},\n  journal = {arXiv preprint arXiv:2002.05202},\n  url = {https://arxiv.org/abs/2002.05202},\n}\n\n@inproceedings{merity2017pointer,\n  title = {Pointer Sentinel Mixture Models},\n  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},\n  year = {2017},\n  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},\n  url = {https://arxiv.org/abs/1609.07843},\n}\n\n@inproceedings{hinton2015distilling,\n  title = {Distilling the Knowledge in a Neural Network},\n  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},\n  year = {2015},\n  booktitle = {NeurIPS 2014 Deep Learning Workshop},\n  url = {https://arxiv.org/abs/1503.02531},\n}\n\n@article{bengio2013ste,\n  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},\n  author = {Yoshua Bengio and Nicholas L\\'{e}onard and Aaron Courville},\n  year = {2013},\n  journal = {arXiv preprint arXiv:1308.3432},\n  url = {https://arxiv.org/abs/1308.3432},\n}\n\n@article{raffel2020t5,\n  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},\n  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},\n  year = {2020},\n  journal = {Journal of Machine Learning Research},\n  url = {https://arxiv.org/abs/1910.10683},\n}\n",
      "numLines": 284,
      "startLine": 1,
      "totalLines": 284
    }
  }
}
```

</details>

---

### Assistant

_source line 100_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the method.tex file. I need to:

1. Follow the structure given in the task
2. Use the correct citation keys from references.bib
3. Use consistent notation from the notation_table and methodology.tex
4. ~1600 words
5. acl2023 format
6. No banned phrases
7. Connect to experiments in §5
8. Formal but readable math exposition

Key corrections from constraint C003:
- Predictor uses GELU (not ReLU) - wait, the task says σ = SiLU for the SwiGLU gate, and predictor architecture uses σ(hW_1)W_2. Let me check what the experiments.tex says...


- The experiments.tex confirms: two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear(4096→128) + Linear(128→14336), so d_b = 128
- Constraint C003 specifies the correct parameters: GELU activation, d_b=128, 2.37M/layer, 75.9M total
- The old methodology.tex version with ReLU and d_b=256 is outdated and needs to be replaced with these correct specifications

Now I'm clarifying the predictor architecture: 32 independent predictors (one per layer) with weight matrices W_1 ∈ R^{4096×128} and W_2 ∈ R^{128×14336}, using GELU as the activation function. I need to be careful with notation since σ is already defined as Gumbel-sigmoid in the notation table, so I should use a different symbol for the predictor's activation to avoid confusion.

I'm ready to write the method section now, organizing it into the key subsections: problem formulation, predictor architecture, Gumbel-sigmoid relaxation, KL divergence training objective, Lagrangian sparsity constraint, gradient analysis comparing BCE versus KL, and the two-dimensional taxonomy. I'll make sure all parameter counts and citations align with the experimental setup and maintain consistent mathematical notation throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "ba18eab3-5fb6-4ba6-ab19-4ad7c2f52180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WdxuHKZ91iLWn3i33HFTB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5189,
      "cache_read_input_tokens": 44021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5189
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

_source line 101_

Now I have all the context. Let me write the method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "38268f53-0ed9-47d9-9a8b-7e7ce300f975",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WdxuHKZ91iLWn3i33HFTB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5189,
      "cache_read_input_tokens": 44021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5189
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

_source line 102_

<details open><summary>🔧 Tool call — Bash · `toolu_01KtLaTNe1D1xDVdawtddLvz`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/",
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
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "d30e83bf-d2df-4b78-9dd2-3ae04d810a1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WdxuHKZ91iLWn3i33HFTB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5189,
      "cache_read_input_tokens": 44021,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5189
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

_source line 103 · 2026-05-16T12:37:49.603Z_

<details><summary>↩ Tool result · `toolu_01KtLaTNe1D1xDVdawtddLvz`</summary>

```text
experiments.tex
references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "84142449-1198-46df-929d-ce83a2dbe418",
  "tool_use_result": {
    "stdout": "experiments.tex\nreferences.bib",
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

_source line 104_

<details open><summary>🔧 Tool call — Write · `toolu_011iRj866utL4WWPRh4UNSP5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\nWe present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.\nThe method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.\n\n\\subsection{Problem Formulation}\n\\label{sec:method:formulation}\n\nConsider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\\cite{shazeer2020glu}.\nFor layer $\\ell$, the FFN computes:\n\\begin{align}\n\\mathbf{y}^{(\\ell)} = \\bigl(\\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)},\n\\label{eq:swiglu}\n\\end{align}\nwhere $\\mathbf{x}^{(\\ell)} \\in \\mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\\sigma$ denotes SiLU, $\\mathbf{W}_g^{(\\ell)}, \\mathbf{W}_u^{(\\ell)} \\in \\mathbb{R}^{d \\times d_{\\text{ff}}}$ and $\\mathbf{W}_d^{(\\ell)} \\in \\mathbb{R}^{d_{\\text{ff}} \\times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\\text{ff}}{=}14{,}336$.\n\nDefine the gate activation $\\mathbf{g}^{(\\ell)} = \\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\in \\mathbb{R}^{d_{\\text{ff}}}$.\nEach element $g_j^{(\\ell)}$ determines the contribution of neuron $j$ to the output.\nWe introduce a binary mask $\\mathbf{m}^{(\\ell)} \\in \\{0,1\\}^{d_{\\text{ff}}}$ that zeros out pruned neurons:\n\\begin{align}\n\\mathbf{y}_{\\text{sparse}}^{(\\ell)} = \\bigl(\\mathbf{m}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)}.\n\\label{eq:sparse_ffn}\n\\end{align}\nOur goal is to learn a mask predictor $f_\\theta^{(\\ell)}(\\mathbf{h}) \\to \\mathbf{s}^{(\\ell)} \\in (0,1)^{d_{\\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\\mathbf{h}$.\nAt inference, the scores are fed to a global top-$k$ allocation mechanism~\\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\\rho) \\times L \\times d_{\\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\\rho$.\n\n\n\\subsection{Predictor Architecture}\n\\label{sec:method:predictor}\n\nEach layer $\\ell$ has an independent two-layer MLP predictor:\n\\begin{align}\nf_\\theta^{(\\ell)}(\\mathbf{h}) = \\text{GELU}(\\mathbf{h} \\mathbf{W}_1^{(\\ell)}) \\, \\mathbf{W}_2^{(\\ell)},\n\\label{eq:predictor}\n\\end{align}\nwhere $\\mathbf{W}_1^{(\\ell)} \\in \\mathbb{R}^{d \\times d_b}$ and $\\mathbf{W}_2^{(\\ell)} \\in \\mathbb{R}^{d_b \\times d_{\\text{ff}}}$ with bottleneck dimension $d_b{=}128$.\nThe predictor takes the hidden state after attention (before the FFN) and outputs $d_{\\text{ff}}$-dimensional logits $\\mathbf{s}^{(\\ell)}$, from which the mask is derived.\n\nEach predictor has $(4096 \\times 128) + (128 \\times 14336) = 2.37\\text{M}$ parameters.\nWith 32 independent predictors (one per layer), the total overhead is 75.9M parameters---less than 1\\% of the 8B base model.\nThe predictors operate independently across layers, requiring no cross-layer communication at inference.\n\n\n\\subsection{Gumbel-Sigmoid Relaxation}\n\\label{sec:method:gumbel}\n\nThe hard mask $m_j = \\mathbf{1}[s_j > \\text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.\nWe apply Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} to produce differentiable soft masks:\n\\begin{align}\n\\tilde{m}_j = \\sigma_\\tau\\!\\left(\\log \\frac{s_j}{1 - s_j} + g_1 - g_2\\right), \\quad g_1, g_2 \\sim \\text{Gumbel}(0,1),\n\\label{eq:gumbel}\n\\end{align}\nwhere $\\sigma_\\tau(x) = \\text{sigmoid}(x / \\tau)$ and $\\tau$ is a temperature parameter.\nThe Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\\tau \\to 0$, $\\tilde{m}_j$ approaches a binary decision.\n\nWe anneal $\\tau$ from 1.0 to 0.1 over training using a cosine schedule.\nAt high temperature, the soft mask permits gradient flow through all neurons, enabling broad exploration.\nAs temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.\n\n\\paragraph{Comparison with Straight-Through Estimation.}\nThe straight-through estimator (STE)~\\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\\partial m / \\partial s = 1$).\nIn our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the Lagrangian multiplier and failure to converge to the target sparsity.\nGumbel relaxation eliminates this pathology, contributing a 34.5\\% improvement (PPL 15.77 $\\to$ 11.79 at 50\\% sparsity), as we verify empirically in \\S\\ref{sec:experiments}.\n\n\n\\subsection{KL Divergence Training Objective}\n\\label{sec:method:kl}\n\nLet $\\mathbf{z}_{\\text{dense}}$ denote the output logits from a full dense forward pass, and $\\mathbf{z}_{\\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\\{\\tilde{\\mathbf{m}}^{(\\ell)}\\}_\\ell$ applied at every layer.\nWe minimize the forward KL divergence between the dense and sparse output distributions:\n\\begin{align}\n\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(p_{\\text{dense}} \\,\\|\\, p_{\\text{sparse}}) = \\sum_{v} p_{\\text{dense}}^{(v)} \\log \\frac{p_{\\text{dense}}^{(v)}}{p_{\\text{sparse}}^{(v)}},\n\\label{eq:kl_loss}\n\\end{align}\nwhere $p_{\\text{dense}} = \\text{softmax}(\\mathbf{z}_{\\text{dense}})$ and $p_{\\text{sparse}} = \\text{softmax}(\\mathbf{z}_{\\text{sparse}})$, summed over the vocabulary $v$ and averaged over sequence positions.\nThe base model is frozen; only the predictor parameters receive gradients.\n\nWe use forward KL ($D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}})$) rather than reverse KL ($D_{\\text{KL}}(p_{\\text{sparse}} \\| p_{\\text{dense}})$).\nForward KL is mean-seeking: it penalizes the sparse model heavily wherever the dense model assigns high probability, forcing the sparse distribution to cover the dense model's primary predictions.\nThis is appropriate for sparsity prediction, where the goal is to preserve the dense model's top-token behavior rather than explore alternative modes.\nNo temperature scaling ($T{=}1$) is applied, following the finding that logit-level distillation without temperature is sufficient when the student retains the teacher's architecture~\\cite{hinton2015distilling}.\n\n\n\\subsection{Lagrangian Sparsity Constraint}\n\\label{sec:method:lagrangian}\n\nWe enforce a model-level sparsity target $\\rho$ via constrained optimization.\nLet $\\bar{s} = \\frac{1}{L} \\sum_\\ell \\frac{1}{d_{\\text{ff}}} \\sum_j \\tilde{m}_j^{(\\ell)}$ denote the average fraction of retained neurons.\nThe constrained problem is:\n\\begin{align}\n\\min_\\theta \\; \\mathcal{L}_{\\text{KL}} \\quad \\text{s.t.} \\quad \\bar{s} \\leq 1 - \\rho.\n\\label{eq:constrained}\n\\end{align}\nWe relax this via the Lagrangian:\n\\begin{align}\n\\mathcal{L} = \\mathcal{L}_{\\text{KL}} + \\lambda \\cdot (\\bar{s} - (1 - \\rho)),\n\\label{eq:lagrangian}\n\\end{align}\nwhere $\\lambda \\geq 0$ is the dual variable, updated by gradient ascent:\n\\begin{align}\n\\lambda \\leftarrow \\lambda + \\eta_\\lambda \\cdot (\\bar{s} - (1 - \\rho)).\n\\label{eq:dual_update}\n\\end{align}\nWhen sparsity undershoots the target ($\\bar{s}$ too large), $\\lambda$ increases, strengthening the pruning pressure.\nWhen sparsity overshoots, $\\lambda$ decreases, allowing the KL objective to recover quality.\nThis eliminates manual tuning of the quality-sparsity tradeoff weight: the dual variable adapts automatically to balance the two objectives throughout training.\n\n\n\\subsection{Gradient Analysis: BCE vs.\\ KL}\n\\label{sec:method:gradient}\n\nThis section formalizes the structural difference between BCE and KL training signals---the core theoretical argument for why KL distillation is better suited to global top-$k$ inference.\n\n\\paragraph{BCE gradient structure.}\nThe standard approach trains the predictor against oracle masks $m_j^* = \\mathbf{1}[|g_j| \\geq \\text{top-}k\\text{ threshold}]$ derived from the dense model's activation magnitudes.\nThe loss decomposes per neuron:\n\\begin{align}\n\\mathcal{L}_{\\text{BCE}} = -\\frac{1}{d_{\\text{ff}}} \\sum_{j=1}^{d_{\\text{ff}}} \\bigl[ m_j^* \\log \\sigma(s_j) + (1 - m_j^*) \\log(1 - \\sigma(s_j)) \\bigr].\n\\label{eq:bce}\n\\end{align}\nThe gradient with respect to predictor logit $s_j$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{BCE}}}{\\partial s_j} = \\sigma(s_j) - m_j^*.\n\\label{eq:bce_grad}\n\\end{align}\nThis gradient depends \\emph{only} on neuron $j$'s own prediction and target.\nEach neuron is trained independently---there is no inter-neuron coupling in the learning signal.\n\n\\paragraph{KL gradient structure.}\nUnder KL distillation, the gradient for predictor logit $s_j^{(\\ell)}$ in layer $\\ell$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\underbrace{\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}_{\\text{sparse}}}}_{\\text{(a)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{z}_{\\text{sparse}}}{\\partial \\mathbf{h}^{(\\ell)}}}_{\\text{(b)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}}}_{\\text{(c)}} \\cdot \\underbrace{\\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}}}_{\\text{(d)}},\n\\label{eq:kl_grad}\n\\end{align}\nwhere each factor has a distinct role:\n\\begin{itemize}\n\\item[\\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.\n\\item[\\textbf{(b)}] The Jacobian through all downstream layers from layer $\\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\\ell, \\ell{+}1, \\ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.\n\\item[\\textbf{(c)}] The effect of mask element $\\tilde{m}_j^{(\\ell)}$ on the layer output: $\\partial \\mathbf{h}^{(\\ell)} / \\partial \\tilde{m}_j^{(\\ell)} = (g_j^{(\\ell)} \\cdot [\\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}]_j) \\cdot \\mathbf{W}_{d,j}^{(\\ell)}$, where $\\mathbf{W}_{d,j}^{(\\ell)}$ is column $j$ of the down-projection. The down-projection linearly mixes all neurons' contributions, so changing $\\tilde{m}_j$ affects the full $d$-dimensional hidden state.\n\\item[\\textbf{(d)}] The Gumbel-Sigmoid derivative, providing the differentiable path from logit to mask.\n\\end{itemize}\n\n\\paragraph{The structural mismatch.}\nThe key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \\emph{all} other neurons' mask values.\nBCE's factorized gradient (Eq.~\\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.\nUnder global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons---a combinatorial interaction that BCE cannot capture.\n\nConcretely, BCE achieves high per-neuron classification accuracy (typically $>$90\\% agreement with oracle masks) yet produces poor output quality under TEAL allocation, because it optimizes a proxy (per-neuron accuracy) misaligned with the true objective (output preservation under global budget allocation).\nKL directly optimizes the end-to-end objective, with gradients that naturally reflect inter-neuron dependencies through the model's computation graph.\nAs we show in \\S\\ref{sec:experiments}, this structural advantage persists even when BCE is given 2.71$\\times$ more training compute: the gap is architectural, not computational.\n\n\n\\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}\n\\label{sec:method:taxonomy}\n\nWe organize prior work along two axes: \\emph{correction granularity} (how the mask adapts to input) and \\emph{training signal coupling} (whether the objective captures inter-neuron dependencies).\n\n\\begin{table}[t]\n\\centering\n\\caption{Taxonomy of learned sparsity prediction methods. Rows indicate correction granularity; columns indicate training signal coupling. Our method fills a previously unexplored cell.}\n\\label{tab:taxonomy}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON \\\\\nPer-layer & --- & ShadowLLM & --- \\\\\nPer-token & FastForward & --- & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-layer} methods~\\cite{akhauri2024shadowllm} condition on a layer-level summary (e.g., the attention output) but share predictions across tokens within a layer.\n\\emph{Per-token} methods~\\cite{gautam2026fastforward,liu2023dejavu} produce a unique mask for each input position.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.\n\nSPON~\\cite{xu2026spon} operates at the intersection of static granularity and coupled training: it distills a per-layer bias correction via KL but cannot adapt to per-input neuron importance.\nFastForward~\\cite{gautam2026fastforward} achieves per-token granularity but uses BCE training, losing inter-neuron coupling.\nOur method combines per-token contextual prediction with coupled KL training (Table~\\ref{tab:taxonomy}), unifying the advantages of both axes: input-dependent mask generation trained with a signal that captures global neuron interactions through the output distribution.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "9ccee6c5-ee91-4770-969a-53142bcbb17f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011MNpesWn1T4BbMVD9ajZeT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 49210,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 904
      },
      "output_tokens": 45,
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

_source line 105 · 2026-05-16T12:39:23.005Z_

<details><summary>↩ Tool result · `toolu_011iRj866utL4WWPRh4UNSP5`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "ee5e87c0-f8f4-4314-98da-e3c7efaf7110",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\nWe present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.\nThe method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.\n\n\\subsection{Problem Formulation}\n\\label{sec:method:formulation}\n\nConsider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\\cite{shazeer2020glu}.\nFor layer $\\ell$, the FFN computes:\n\\begin{align}\n\\mathbf{y}^{(\\ell)} = \\bigl(\\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)},\n\\label{eq:swiglu}\n\\end{align}\nwhere $\\mathbf{x}^{(\\ell)} \\in \\mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\\sigma$ denotes SiLU, $\\mathbf{W}_g^{(\\ell)}, \\mathbf{W}_u^{(\\ell)} \\in \\mathbb{R}^{d \\times d_{\\text{ff}}}$ and $\\mathbf{W}_d^{(\\ell)} \\in \\mathbb{R}^{d_{\\text{ff}} \\times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\\text{ff}}{=}14{,}336$.\n\nDefine the gate activation $\\mathbf{g}^{(\\ell)} = \\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\in \\mathbb{R}^{d_{\\text{ff}}}$.\nEach element $g_j^{(\\ell)}$ determines the contribution of neuron $j$ to the output.\nWe introduce a binary mask $\\mathbf{m}^{(\\ell)} \\in \\{0,1\\}^{d_{\\text{ff}}}$ that zeros out pruned neurons:\n\\begin{align}\n\\mathbf{y}_{\\text{sparse}}^{(\\ell)} = \\bigl(\\mathbf{m}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)}.\n\\label{eq:sparse_ffn}\n\\end{align}\nOur goal is to learn a mask predictor $f_\\theta^{(\\ell)}(\\mathbf{h}) \\to \\mathbf{s}^{(\\ell)} \\in (0,1)^{d_{\\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\\mathbf{h}$.\nAt inference, the scores are fed to a global top-$k$ allocation mechanism~\\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\\rho) \\times L \\times d_{\\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\\rho$.\n\n\n\\subsection{Predictor Architecture}\n\\label{sec:method:predictor}\n\nEach layer $\\ell$ has an independent two-layer MLP predictor:\n\\begin{align}\nf_\\theta^{(\\ell)}(\\mathbf{h}) = \\text{GELU}(\\mathbf{h} \\mathbf{W}_1^{(\\ell)}) \\, \\mathbf{W}_2^{(\\ell)},\n\\label{eq:predictor}\n\\end{align}\nwhere $\\mathbf{W}_1^{(\\ell)} \\in \\mathbb{R}^{d \\times d_b}$ and $\\mathbf{W}_2^{(\\ell)} \\in \\mathbb{R}^{d_b \\times d_{\\text{ff}}}$ with bottleneck dimension $d_b{=}128$.\nThe predictor takes the hidden state after attention (before the FFN) and outputs $d_{\\text{ff}}$-dimensional logits $\\mathbf{s}^{(\\ell)}$, from which the mask is derived.\n\nEach predictor has $(4096 \\times 128) + (128 \\times 14336) = 2.37\\text{M}$ parameters.\nWith 32 independent predictors (one per layer), the total overhead is 75.9M parameters---less than 1\\% of the 8B base model.\nThe predictors operate independently across layers, requiring no cross-layer communication at inference.\n\n\n\\subsection{Gumbel-Sigmoid Relaxation}\n\\label{sec:method:gumbel}\n\nThe hard mask $m_j = \\mathbf{1}[s_j > \\text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.\nWe apply Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} to produce differentiable soft masks:\n\\begin{align}\n\\tilde{m}_j = \\sigma_\\tau\\!\\left(\\log \\frac{s_j}{1 - s_j} + g_1 - g_2\\right), \\quad g_1, g_2 \\sim \\text{Gumbel}(0,1),\n\\label{eq:gumbel}\n\\end{align}\nwhere $\\sigma_\\tau(x) = \\text{sigmoid}(x / \\tau)$ and $\\tau$ is a temperature parameter.\nThe Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\\tau \\to 0$, $\\tilde{m}_j$ approaches a binary decision.\n\nWe anneal $\\tau$ from 1.0 to 0.1 over training using a cosine schedule.\nAt high temperature, the soft mask permits gradient flow through all neurons, enabling broad exploration.\nAs temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.\n\n\\paragraph{Comparison with Straight-Through Estimation.}\nThe straight-through estimator (STE)~\\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\\partial m / \\partial s = 1$).\nIn our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the Lagrangian multiplier and failure to converge to the target sparsity.\nGumbel relaxation eliminates this pathology, contributing a 34.5\\% improvement (PPL 15.77 $\\to$ 11.79 at 50\\% sparsity), as we verify empirically in \\S\\ref{sec:experiments}.\n\n\n\\subsection{KL Divergence Training Objective}\n\\label{sec:method:kl}\n\nLet $\\mathbf{z}_{\\text{dense}}$ denote the output logits from a full dense forward pass, and $\\mathbf{z}_{\\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\\{\\tilde{\\mathbf{m}}^{(\\ell)}\\}_\\ell$ applied at every layer.\nWe minimize the forward KL divergence between the dense and sparse output distributions:\n\\begin{align}\n\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(p_{\\text{dense}} \\,\\|\\, p_{\\text{sparse}}) = \\sum_{v} p_{\\text{dense}}^{(v)} \\log \\frac{p_{\\text{dense}}^{(v)}}{p_{\\text{sparse}}^{(v)}},\n\\label{eq:kl_loss}\n\\end{align}\nwhere $p_{\\text{dense}} = \\text{softmax}(\\mathbf{z}_{\\text{dense}})$ and $p_{\\text{sparse}} = \\text{softmax}(\\mathbf{z}_{\\text{sparse}})$, summed over the vocabulary $v$ and averaged over sequence positions.\nThe base model is frozen; only the predictor parameters receive gradients.\n\nWe use forward KL ($D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}})$) rather than reverse KL ($D_{\\text{KL}}(p_{\\text{sparse}} \\| p_{\\text{dense}})$).\nForward KL is mean-seeking: it penalizes the sparse model heavily wherever the dense model assigns high probability, forcing the sparse distribution to cover the dense model's primary predictions.\nThis is appropriate for sparsity prediction, where the goal is to preserve the dense model's top-token behavior rather than explore alternative modes.\nNo temperature scaling ($T{=}1$) is applied, following the finding that logit-level distillation without temperature is sufficient when the student retains the teacher's architecture~\\cite{hinton2015distilling}.\n\n\n\\subsection{Lagrangian Sparsity Constraint}\n\\label{sec:method:lagrangian}\n\nWe enforce a model-level sparsity target $\\rho$ via constrained optimization.\nLet $\\bar{s} = \\frac{1}{L} \\sum_\\ell \\frac{1}{d_{\\text{ff}}} \\sum_j \\tilde{m}_j^{(\\ell)}$ denote the average fraction of retained neurons.\nThe constrained problem is:\n\\begin{align}\n\\min_\\theta \\; \\mathcal{L}_{\\text{KL}} \\quad \\text{s.t.} \\quad \\bar{s} \\leq 1 - \\rho.\n\\label{eq:constrained}\n\\end{align}\nWe relax this via the Lagrangian:\n\\begin{align}\n\\mathcal{L} = \\mathcal{L}_{\\text{KL}} + \\lambda \\cdot (\\bar{s} - (1 - \\rho)),\n\\label{eq:lagrangian}\n\\end{align}\nwhere $\\lambda \\geq 0$ is the dual variable, updated by gradient ascent:\n\\begin{align}\n\\lambda \\leftarrow \\lambda + \\eta_\\lambda \\cdot (\\bar{s} - (1 - \\rho)).\n\\label{eq:dual_update}\n\\end{align}\nWhen sparsity undershoots the target ($\\bar{s}$ too large), $\\lambda$ increases, strengthening the pruning pressure.\nWhen sparsity overshoots, $\\lambda$ decreases, allowing the KL objective to recover quality.\nThis eliminates manual tuning of the quality-sparsity tradeoff weight: the dual variable adapts automatically to balance the two objectives throughout training.\n\n\n\\subsection{Gradient Analysis: BCE vs.\\ KL}\n\\label{sec:method:gradient}\n\nThis section formalizes the structural difference between BCE and KL training signals---the core theoretical argument for why KL distillation is better suited to global top-$k$ inference.\n\n\\paragraph{BCE gradient structure.}\nThe standard approach trains the predictor against oracle masks $m_j^* = \\mathbf{1}[|g_j| \\geq \\text{top-}k\\text{ threshold}]$ derived from the dense model's activation magnitudes.\nThe loss decomposes per neuron:\n\\begin{align}\n\\mathcal{L}_{\\text{BCE}} = -\\frac{1}{d_{\\text{ff}}} \\sum_{j=1}^{d_{\\text{ff}}} \\bigl[ m_j^* \\log \\sigma(s_j) + (1 - m_j^*) \\log(1 - \\sigma(s_j)) \\bigr].\n\\label{eq:bce}\n\\end{align}\nThe gradient with respect to predictor logit $s_j$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{BCE}}}{\\partial s_j} = \\sigma(s_j) - m_j^*.\n\\label{eq:bce_grad}\n\\end{align}\nThis gradient depends \\emph{only} on neuron $j$'s own prediction and target.\nEach neuron is trained independently---there is no inter-neuron coupling in the learning signal.\n\n\\paragraph{KL gradient structure.}\nUnder KL distillation, the gradient for predictor logit $s_j^{(\\ell)}$ in layer $\\ell$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\underbrace{\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}_{\\text{sparse}}}}_{\\text{(a)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{z}_{\\text{sparse}}}{\\partial \\mathbf{h}^{(\\ell)}}}_{\\text{(b)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}}}_{\\text{(c)}} \\cdot \\underbrace{\\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}}}_{\\text{(d)}},\n\\label{eq:kl_grad}\n\\end{align}\nwhere each factor has a distinct role:\n\\begin{itemize}\n\\item[\\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.\n\\item[\\textbf{(b)}] The Jacobian through all downstream layers from layer $\\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\\ell, \\ell{+}1, \\ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.\n\\item[\\textbf{(c)}] The effect of mask element $\\tilde{m}_j^{(\\ell)}$ on the layer output: $\\partial \\mathbf{h}^{(\\ell)} / \\partial \\tilde{m}_j^{(\\ell)} = (g_j^{(\\ell)} \\cdot [\\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}]_j) \\cdot \\mathbf{W}_{d,j}^{(\\ell)}$, where $\\mathbf{W}_{d,j}^{(\\ell)}$ is column $j$ of the down-projection. The down-projection linearly mixes all neurons' contributions, so changing $\\tilde{m}_j$ affects the full $d$-dimensional hidden state.\n\\item[\\textbf{(d)}] The Gumbel-Sigmoid derivative, providing the differentiable path from logit to mask.\n\\end{itemize}\n\n\\paragraph{The structural mismatch.}\nThe key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \\emph{all} other neurons' mask values.\nBCE's factorized gradient (Eq.~\\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.\nUnder global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons---a combinatorial interaction that BCE cannot capture.\n\nConcretely, BCE achieves high per-neuron classification accuracy (typically $>$90\\% agreement with oracle masks) yet produces poor output quality under TEAL allocation, because it optimizes a proxy (per-neuron accuracy) misaligned with the true objective (output preservation under global budget allocation).\nKL directly optimizes the end-to-end objective, with gradients that naturally reflect inter-neuron dependencies through the model's computation graph.\nAs we show in \\S\\ref{sec:experiments}, this structural advantage persists even when BCE is given 2.71$\\times$ more training compute: the gap is architectural, not computational.\n\n\n\\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}\n\\label{sec:method:taxonomy}\n\nWe organize prior work along two axes: \\emph{correction granularity} (how the mask adapts to input) and \\emph{training signal coupling} (whether the objective captures inter-neuron dependencies).\n\n\\begin{table}[t]\n\\centering\n\\caption{Taxonomy of learned sparsity prediction methods. Rows indicate correction granularity; columns indicate training signal coupling. Our method fills a previously unexplored cell.}\n\\label{tab:taxonomy}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON \\\\\nPer-layer & --- & ShadowLLM & --- \\\\\nPer-token & FastForward & --- & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-layer} methods~\\cite{akhauri2024shadowllm} condition on a layer-level summary (e.g., the attention output) but share predictions across tokens within a layer.\n\\emph{Per-token} methods~\\cite{gautam2026fastforward,liu2023dejavu} produce a unique mask for each input position.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.\n\nSPON~\\cite{xu2026spon} operates at the intersection of static granularity and coupled training: it distills a per-layer bias correction via KL but cannot adapt to per-input neuron importance.\nFastForward~\\cite{gautam2026fastforward} achieves per-token granularity but uses BCE training, losing inter-neuron coupling.\nOur method combines per-token contextual prediction with coupled KL training (Table~\\ref{tab:taxonomy}), unifying the advantages of both axes: input-dependent mask generation trained with a signal that captures global neuron interactions through the output distribution.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 106_

Method section written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex`.

Key points:
- ~1600 words, 7 subsections following the specified structure
- All numbers verified against C003: GELU activation, $d_b{=}128$, 2.37M/layer, 75.9M total
- Gradient analysis formalized with labeled chain-rule factors and explicit structural mismatch argument
- Two-dimensional taxonomy as a table placing SPON, ShadowLLM, FastForward, and Ours
- Forward references to §5 for empirical validation of each design choice
- Citations use exact keys from `references.bib`
- No banned phrases

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "uuid": "0addaf54-1354-4408-baec-4ff01a75d2ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NWpec7MQAsAYFZDzWAuSYY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4976,
      "cache_read_input_tokens": 50114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4976
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

_source line 107_

Method section written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex`.

Key points:
- ~1600 words, 7 subsections following the specified structure
- All numbers verified against C003: GELU activation, $d_b{=}128$, 2.37M/layer, 75.9M total
- Gradient analysis formalized with labeled chain-rule factors and explicit structural mismatch argument
- Two-dimensional taxonomy as a table placing SPON, ShadowLLM, FastForward, and Ours
- Forward references to §5 for empirical validation of each design choice
- Citations use exact keys from `references.bib`
- No banned phrases

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 179603,
  "duration_api_ms": 180551,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "e2262063-9ced-40a4-bd3f-d2c59df81e7f",
  "total_cost_usd": 0.7158167000000001,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 43249,
    "cache_read_input_tokens": 252394,
    "output_tokens": 6574,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 43249,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 186,
        "cache_read_input_tokens": 50114,
        "cache_creation_input_tokens": 4976,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4976
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2863,
      "outputTokens": 3732,
      "cacheReadInputTokens": 434767,
      "cacheCreationInputTokens": 71935,
      "webSearchRequests": 0,
      "costUSD": 0.15491845,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 6574,
      "cacheReadInputTokens": 252394,
      "cacheCreationInputTokens": 43249,
      "webSearchRequests": 0,
      "costUSD": 0.5608982499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "93036578-733a-4a8a-85f7-518efba81c26"
}
```

</details>

---
