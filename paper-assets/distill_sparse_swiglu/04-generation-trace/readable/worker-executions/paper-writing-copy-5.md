# paper writing

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_20260516T125328.log`
- **Structured JSON:** [`8195d526c049113c66e6.json`](../../sessions/81/8195d526c049113c66e6.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
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
  "uuid": "e4636897-6968-44c7-9fe0-33c0a9693853",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-14-projects-distill-sparse-swiglu/memory/"
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
  "uuid": "66feadca-887e-4c89-91f0-a4843d07a7e9",
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill file and existing paper sections for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "873cb1c7-4b2b-499b-98ad-e6bdcaa2b385",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5gzMGyPzVHFZYRphZKrsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12950,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12950
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

<details open><summary>🔧 Tool call — Read · `toolu_01573jsE7ejCNuwq8kAQTprz`</summary>

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
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "ff78fcec-151e-4e80-b201-19b6ab92e4f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5gzMGyPzVHFZYRphZKrsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12950,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12950
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

_source line 6 · 2026-05-16T12:53:38.222Z_

<details><summary>↩ Tool result · `toolu_01573jsE7ejCNuwq8kAQTprz`</summary>

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
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "1709b2c3-f697-440d-ad93-b5657767e025",
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

<details open><summary>🔧 Tool call — Read · `toolu_01PUjqQ5BGPVWTyjFKtpd5Js`</summary>

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
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "4464c8f6-366e-41ec-a4ba-b42a4f911441",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5gzMGyPzVHFZYRphZKrsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12950,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12950
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

_source line 8 · 2026-05-16T12:53:38.707Z_

<details><summary>↩ Tool result · `toolu_01PUjqQ5BGPVWTyjFKtpd5Js`</summary>

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
36	\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. \textbf{Bold}: best among compensation-free methods per sparsity level. BCE uses a different inference protocol (hard mask + compensation network).}
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
51	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
52	& KL global (Ours) & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 27.89 & 1.29 \\ % exp_id: bench_kl50_global
53	& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \textbf{2.12} \\ % exp_id: d030_kl50_uniform
54	& BCE (2700 steps)$^\ast$ & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\ % exp_id: eval_bce_v3_s42
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
79	\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$, unified benchmark protocol).}
80	\label{tab:ablation}
81	\small
82	\begin{tabular}{lcc}
83	\toprule
84	Configuration & PPL$\downarrow$ & $\Delta$ from Ours \\
85	\midrule
86	KL + Gumbel (Ours) & \textbf{11.79} & --- \\ % exp_id: bench_kl50_global
87	KL + STE & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
88	BCE + Compensation (hard mask) & 25.44 & +13.65 \\ % exp_id: bce_comp_staged_s42
89	BCE (no compensation) & 27.97 & +16.18 \\ % exp_id: eval_bce_v3_s42
90	\bottomrule
91	\end{tabular}
92	\end{table}
93	
94	\paragraph{Gumbel vs.\ STE.}
95	Replacing Gumbel-Sigmoid relaxation with Straight-Through Estimation~\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98). % exp_id: ste_baseline_s42
96	Gumbel relaxation provides smooth gradients through the mask sampling, accounting for 34.5\% of the total improvement over vanilla TEAL (3.98 out of 11.52 PPL gap).
97	
98	\paragraph{SPON Contribution.}
99	Under the same evaluation protocol (\texttt{evaluate.py}), adding SPON~\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79, a 2.4\% relative improvement.\footnote{SPON analysis uses \texttt{evaluate.py} protocol; main results (Table~\ref{tab:main}) use the unified benchmark protocol. The coincidental equality of 11.79 in both settings does not imply equivalence.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42
100	We analyze this limited contribution further in \S\ref{sec:spon}.
101	
102	\paragraph{BCE + Compensation.}
103	Compensation (output rescaling after hard-mask pruning) improves BCE from 27.97 to 25.44 (9.0\% relative), but this hard-mask protocol remains 2.16$\times$ worse than KL under TEAL inference. % exp_id: bce_comp_staged_s42
104	We report this separately as it uses a different inference protocol (hard mask vs.\ TEAL global allocation).
105	
106	
107	\subsection{Sparsity Scaling and Phase Transition}
108	\label{sec:scaling}
109	
110	Table~\ref{tab:scaling} and Figure~\ref{fig:sparsity_sweep} show PPL as a function of sparsity for KL-predictor-TEAL and vanilla TEAL.
111	
112	\begin{table}[t]
113	\centering
114	\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows super-linearly.}
115	\label{tab:scaling}
116	\small
117	\begin{tabular}{lccc}
118	\toprule
119	Sparsity & KL (Ours) & TEAL vanilla & Relative advantage \\
120	\midrule
121	30\% & \textbf{8.98} & 10.97 & 18\% \\ % exp_id: kl_30_global_teal
122	50\% & \textbf{11.79} & 23.31 & 49\% \\ % exp_id: bench_kl50_global
123	70\% & \textbf{17.91} & 100.11 & 82\% \\ % exp_id: kl_70_global_teal
124	\bottomrule
125	\end{tabular}
126	\end{table}
127	
128	The KL predictor's advantage grows from 18\% at 30\% sparsity to 82\% at 70\% sparsity.
129	At high sparsity, TEAL's magnitude-based scoring collapses (PPL 100.11), while the learned predictor maintains coherent allocation by exploiting input-dependent contextual information.
130	
131	\paragraph{Downstream Phase Transition.}
132	Table~\ref{tab:phase} examines how downstream task accuracy degrades with increasing sparsity under uniform allocation (which maximizes MMLU at each level).
133	
134	\begin{table}[t]
135	\centering
136	\caption{Phase transition in MMLU accuracy under uniform allocation. Random performance is 25\%.}
137	\label{tab:phase}
138	\small
139	\begin{tabular}{lcc}
140	\toprule
141	Sparsity & MMLU (\%) & Regime \\
142	\midrule
143	0\% (Dense) & 65.27 & Full capacity \\
144	30\% & 40.61 & Operable (15\% above random) \\ % exp_id: kl_30_uniform
145	40\% & 30.68 & Degradation band \\ % exp_id: kl_40_uniform
146	50\% & 27.77 & Capacity-limited ($\approx$ random) \\ % exp_id: kl_50_uniform
147	\bottomrule
148	\end{tabular}
149	\end{table}
150	
151	The transition from operable to capacity-limited is gradual—a degradation band spanning 30--50\% sparsity—rather than a sharp cliff.
152	At 30\%, the model retains sufficient capacity for knowledge recall (MMLU 40.61\%, 15 points above random), while at 50\%, no allocation strategy recovers meaningful performance.
153	This suggests 30\% as the recommended operating point for deployment scenarios requiring both perplexity and downstream task fidelity.
154	
155	
156	\subsection{SPON Orthogonality Analysis}
157	\label{sec:spon}
158	
159	We analyze why SPON's contribution is limited by decomposing the output perturbation at 50\% sparsity (Figure~\ref{fig:subsumption}).
160	
161	The predictor's effect on the hidden state has L2 norm 482.65, while SPON's additive correction has norm 76.2—only 15.8\% of the predictor's magnitude. % exp_id: spon_decomposition
162	The cosine similarity between the two perturbation directions is 0.196, confirming near-orthogonality: SPON corrects in a direction largely independent of the predictor's effect, but its small magnitude limits impact.
163	
164	Under the \texttt{evaluate.py} protocol, SPON provides: 7.3\% improvement under hard-mask inference (9.22 $\to$ 8.99) and 2.4\% under TEAL-path inference (12.08 $\to$ 11.79). % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42
165	The interaction norm between predictor and SPON effects is 147.74, indicating non-trivial coupling but insufficient magnitude for SPON to meaningfully complement KL distillation.
166	The KL predictor already captures most of the recoverable signal, leaving little residual for static bias correction.
167	
168	
169	\subsection{Cross-Architecture Generalization}
170	
171	To verify that KL distillation is not specific to LLaMA's architecture, we evaluate on Mistral-7B-v0.3~\cite{jiang2023mistral}, which differs in using Grouped Query Attention (GQA) and sliding window attention.
172	
173	\begin{table}[t]
174	\centering
175	\caption{Cross-architecture results at 50\% sparsity (WikiText-2 PPL$\downarrow$).}
176	\label{tab:cross_arch}
177	\small
178	\begin{tabular}{lccc}
179	\toprule
180	Model & Dense PPL & KL TEAL PPL & Relative degradation \\
181	\midrule
182	LLaMA-3.1-8B & 6.12 & 11.79 & +93\% \\ % exp_id: bench_kl50_global
183	Mistral-7B-v0.3 & 5.52 & 8.98 & +63\% \\ % exp_id: kl_50_mistral
184	\bottomrule
185	\end{tabular}
186	\end{table}
187	
188	The KL predictor transfers to Mistral with lower relative degradation (+63\% vs.\ +93\% on LLaMA). % exp_id: mistral_kl_s42, bench_kl50_global
189	Mistral's GQA mechanism produces more informative key-value representations at each layer, potentially providing richer input signals for the sparsity predictor.
190	The result confirms that KL distillation for contextual sparsity prediction generalizes across SwiGLU-based architectures with different attention configurations.
191	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "3dcab8c7-8bfa-4514-8448-332e17d74a10",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex",
      "content": "\\section{Experiments}\n\n\\subsection{Experimental Setup}\n\n\\paragraph{Model and Predictor.}\nWe evaluate on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\\cite{shazeer2020glu} with $d_{\\text{model}}=4096$ and $d_{\\text{ff}}=14336$ across 32 layers.\nThe sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \\to 128$) + Linear($128 \\to 14336$), trained to predict activation magnitudes from the FFN input representation.\n\n\\paragraph{Training.}\nAll predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW with learning rate $1 \\times 10^{-3}$ and cosine decay.\nThe KL predictor uses Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} with temperature $\\tau=1.0$ annealed to $0.1$ over training.\n\n\\paragraph{Evaluation.}\nWe report perplexity on WikiText-2~\\cite{merity2017pointer} (seq\\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).\n\n\\paragraph{Inference Protocol.}\nAt inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.\nWe term this \\textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.\n\n\\paragraph{Baselines.}\nWe compare against: (1) \\textbf{Vanilla TEAL}~\\cite{liu2025teal}, which uses activation magnitudes directly; (2) \\textbf{BCE predictor}, trained with per-neuron binary cross-entropy loss for 1000 and 2700 steps; (3) \\textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \\textbf{WINA}~\\cite{liu2025teal}, an importance-weighted variant.\n\n\n\\subsection{Main Results}\n\nTable~\\ref{tab:main} presents the primary comparison across sparsity levels.\nAt 30\\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.98, reducing TEAL's degradation from dense (10.97 $\\to$ 8.98, an 18\\% improvement). % exp_id: kl_30_global_teal\nUniform allocation at 30\\% yields the lowest PPL (8.82) and notably recovers MMLU to 40.61\\%, compared to 38.61\\% for TEAL and 25.27\\% for KL-global. % exp_id: kl_30_uniform\nThis indicates that at moderate sparsity, the allocation strategy—not the predictor—is the primary lever for knowledge-intensive tasks.\n\nAt 50\\% sparsity, the advantage of KL distillation over vanilla TEAL widens: PPL 11.79 vs.\\ 23.31, a 49\\% reduction. % exp_id: bench_kl50_global, bench_teal50\nHowever, all methods exhibit downstream collapse on MMLU (27.89\\% $\\approx$ random at 25\\%) and GSM8K ($<$2.2\\%), indicating a capacity-limited regime where no allocation strategy can recover reasoning ability. % exp_id: kl_50_downstream\n\n\\begin{table}[t]\n\\centering\n\\caption{Main results on LLaMA-3.1-8B. PPL$\\downarrow$ on WikiText-2; accuracy$\\uparrow$ on downstream tasks. \\textbf{Bold}: best among compensation-free methods per sparsity level. BCE uses a different inference protocol (hard mask + compensation network).}\n\\label{tab:main}\n\\small\n\\begin{tabular}{llccccc}\n\\toprule\nSparsity & Method & PPL$\\downarrow$ & ARC-c & WG & MMLU & GSM8K \\\\\n\\midrule\n0\\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\\\\n\\midrule\n\\multirow{3}{*}{30\\%}\n& TEAL vanilla & 10.97 & \\textbf{42.32} & 66.06 & 38.61 & 7.88 \\\\ % exp_id: bench_teal30\n& KL global (Ours) & 8.98 & 39.68 & \\textbf{70.17} & 25.27 & \\textbf{8.79} \\\\ % exp_id: lm_eval_kl_30pct_s42\n& KL uniform & \\textbf{8.82} & 40.78 & 68.59 & \\textbf{40.61} & 7.35 \\\\ % exp_id: bench_kl30_uniform\n\\midrule\n\\multirow{4}{*}{50\\%}\n& TEAL vanilla & 23.31 & 28.41 & 53.04 & \\textbf{28.32} & 1.97 \\\\ % exp_id: bench_teal50\n& KL global (Ours) & \\textbf{11.79} & \\textbf{32.85} & \\textbf{63.46} & 27.89 & 1.29 \\\\ % exp_id: bench_kl50_global\n& KL uniform & 11.96 & 32.76 & 62.90 & 27.77 & \\textbf{2.12} \\\\ % exp_id: d030_kl50_uniform\n& BCE (2700 steps)$^\\ast$ & 27.97 & 23.98 & 50.59 & 30.02 & 4.85 \\\\ % exp_id: eval_bce_v3_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Iso-Compute Analysis}\n\\label{sec:isocompute}\n\nA natural question is whether BCE training simply requires more compute to converge.\nWe train the BCE predictor for 2700 steps (2.71$\\times$ the KL budget) and evaluate under identical TEAL inference.\nAs Table~\\ref{tab:main} shows, the BCE predictor at 2700 steps achieves PPL 27.97—still 2.37$\\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce_isocompute_s42\n\nThe failure is structural, not computational.\nBCE loss decomposes into independent per-neuron gradients, training each neuron's prediction in isolation.\nThis factorized objective cannot learn the inter-neuron correlations required for global top-$k$ allocation, where the keep/prune decision for neuron $i$ depends on the scores of all other neurons across all layers.\nWe observe that BCE training loss saturates early: between steps 500 and 2700, the loss decreases by only 0.006, confirming that additional compute yields diminishing returns under the wrong objective.\n\n\n\\subsection{Ablation Studies}\n\nTable~\\ref{tab:ablation} isolates the contribution of each design choice at 50\\% sparsity.\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation at 50\\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\\downarrow$, unified benchmark protocol).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nConfiguration & PPL$\\downarrow$ & $\\Delta$ from Ours \\\\\n\\midrule\nKL + Gumbel (Ours) & \\textbf{11.79} & --- \\\\ % exp_id: bench_kl50_global\nKL + STE & 15.77 & +3.98 \\\\ % exp_id: ste_baseline_s42\nBCE + Compensation (hard mask) & 25.44 & +13.65 \\\\ % exp_id: bce_comp_staged_s42\nBCE (no compensation) & 27.97 & +16.18 \\\\ % exp_id: eval_bce_v3_s42\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Gumbel vs.\\ STE.}\nReplacing Gumbel-Sigmoid relaxation with Straight-Through Estimation~\\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98). % exp_id: ste_baseline_s42\nGumbel relaxation provides smooth gradients through the mask sampling, accounting for 34.5\\% of the total improvement over vanilla TEAL (3.98 out of 11.52 PPL gap).\n\n\\paragraph{SPON Contribution.}\nUnder the same evaluation protocol (\\texttt{evaluate.py}), adding SPON~\\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79, a 2.4\\% relative improvement.\\footnote{SPON analysis uses \\texttt{evaluate.py} protocol; main results (Table~\\ref{tab:main}) use the unified benchmark protocol. The coincidental equality of 11.79 in both settings does not imply equivalence.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42\nWe analyze this limited contribution further in \\S\\ref{sec:spon}.\n\n\\paragraph{BCE + Compensation.}\nCompensation (output rescaling after hard-mask pruning) improves BCE from 27.97 to 25.44 (9.0\\% relative), but this hard-mask protocol remains 2.16$\\times$ worse than KL under TEAL inference. % exp_id: bce_comp_staged_s42\nWe report this separately as it uses a different inference protocol (hard mask vs.\\ TEAL global allocation).\n\n\n\\subsection{Sparsity Scaling and Phase Transition}\n\\label{sec:scaling}\n\nTable~\\ref{tab:scaling} and Figure~\\ref{fig:sparsity_sweep} show PPL as a function of sparsity for KL-predictor-TEAL and vanilla TEAL.\n\n\\begin{table}[t]\n\\centering\n\\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows super-linearly.}\n\\label{tab:scaling}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nSparsity & KL (Ours) & TEAL vanilla & Relative advantage \\\\\n\\midrule\n30\\% & \\textbf{8.98} & 10.97 & 18\\% \\\\ % exp_id: kl_30_global_teal\n50\\% & \\textbf{11.79} & 23.31 & 49\\% \\\\ % exp_id: bench_kl50_global\n70\\% & \\textbf{17.91} & 100.11 & 82\\% \\\\ % exp_id: kl_70_global_teal\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL predictor's advantage grows from 18\\% at 30\\% sparsity to 82\\% at 70\\% sparsity.\nAt high sparsity, TEAL's magnitude-based scoring collapses (PPL 100.11), while the learned predictor maintains coherent allocation by exploiting input-dependent contextual information.\n\n\\paragraph{Downstream Phase Transition.}\nTable~\\ref{tab:phase} examines how downstream task accuracy degrades with increasing sparsity under uniform allocation (which maximizes MMLU at each level).\n\n\\begin{table}[t]\n\\centering\n\\caption{Phase transition in MMLU accuracy under uniform allocation. Random performance is 25\\%.}\n\\label{tab:phase}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nSparsity & MMLU (\\%) & Regime \\\\\n\\midrule\n0\\% (Dense) & 65.27 & Full capacity \\\\\n30\\% & 40.61 & Operable (15\\% above random) \\\\ % exp_id: kl_30_uniform\n40\\% & 30.68 & Degradation band \\\\ % exp_id: kl_40_uniform\n50\\% & 27.77 & Capacity-limited ($\\approx$ random) \\\\ % exp_id: kl_50_uniform\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe transition from operable to capacity-limited is gradual—a degradation band spanning 30--50\\% sparsity—rather than a sharp cliff.\nAt 30\\%, the model retains sufficient capacity for knowledge recall (MMLU 40.61\\%, 15 points above random), while at 50\\%, no allocation strategy recovers meaningful performance.\nThis suggests 30\\% as the recommended operating point for deployment scenarios requiring both perplexity and downstream task fidelity.\n\n\n\\subsection{SPON Orthogonality Analysis}\n\\label{sec:spon}\n\nWe analyze why SPON's contribution is limited by decomposing the output perturbation at 50\\% sparsity (Figure~\\ref{fig:subsumption}).\n\nThe predictor's effect on the hidden state has L2 norm 482.65, while SPON's additive correction has norm 76.2—only 15.8\\% of the predictor's magnitude. % exp_id: spon_decomposition\nThe cosine similarity between the two perturbation directions is 0.196, confirming near-orthogonality: SPON corrects in a direction largely independent of the predictor's effect, but its small magnitude limits impact.\n\nUnder the \\texttt{evaluate.py} protocol, SPON provides: 7.3\\% improvement under hard-mask inference (9.22 $\\to$ 8.99) and 2.4\\% under TEAL-path inference (12.08 $\\to$ 11.79). % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42\nThe interaction norm between predictor and SPON effects is 147.74, indicating non-trivial coupling but insufficient magnitude for SPON to meaningfully complement KL distillation.\nThe KL predictor already captures most of the recoverable signal, leaving little residual for static bias correction.\n\n\n\\subsection{Cross-Architecture Generalization}\n\nTo verify that KL distillation is not specific to LLaMA's architecture, we evaluate on Mistral-7B-v0.3~\\cite{jiang2023mistral}, which differs in using Grouped Query Attention (GQA) and sliding window attention.\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-architecture results at 50\\% sparsity (WikiText-2 PPL$\\downarrow$).}\n\\label{tab:cross_arch}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nModel & Dense PPL & KL TEAL PPL & Relative degradation \\\\\n\\midrule\nLLaMA-3.1-8B & 6.12 & 11.79 & +93\\% \\\\ % exp_id: bench_kl50_global\nMistral-7B-v0.3 & 5.52 & 8.98 & +63\\% \\\\ % exp_id: kl_50_mistral\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe KL predictor transfers to Mistral with lower relative degradation (+63\\% vs.\\ +93\\% on LLaMA). % exp_id: mistral_kl_s42, bench_kl50_global\nMistral's GQA mechanism produces more informative key-value representations at each layer, potentially providing richer input signals for the sparsity predictor.\nThe result confirms that KL distillation for contextual sparsity prediction generalizes across SwiGLU-based architectures with different attention configurations.\n",
      "numLines": 191,
      "startLine": 1,
      "totalLines": 191
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01DeY3Qc8d5VeWLbhecibDPV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "c708c5d5-0351-4163-b36d-09eef9953198",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H5gzMGyPzVHFZYRphZKrsP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12950,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12950
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

_source line 10 · 2026-05-16T12:53:39.185Z_

<details><summary>↩ Tool result · `toolu_01DeY3Qc8d5VeWLbhecibDPV`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26	At inference, the scores are fed to a global top-$k$ allocation mechanism~\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\rho) \times L \times d_{\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\rho$.
27	
28	
29	\subsection{Predictor Architecture}
30	\label{sec:method:predictor}
31	
32	Each layer $\ell$ has an independent two-layer MLP predictor:
33	\begin{align}
34	f_\theta^{(\ell)}(\mathbf{h}) = \text{GELU}(\mathbf{h} \mathbf{W}_1^{(\ell)}) \, \mathbf{W}_2^{(\ell)},
35	\label{eq:predictor}
36	\end{align}
37	where $\mathbf{W}_1^{(\ell)} \in \mathbb{R}^{d \times d_b}$ and $\mathbf{W}_2^{(\ell)} \in \mathbb{R}^{d_b \times d_{\text{ff}}}$ with bottleneck dimension $d_b{=}128$.
38	The predictor takes the hidden state after attention (before the FFN) and outputs $d_{\text{ff}}$-dimensional logits $\mathbf{s}^{(\ell)}$, from which the mask is derived.
39	
40	Each predictor has $(4096 \times 128) + (128 \times 14336) = 2.37\text{M}$ parameters.
41	With 32 independent predictors (one per layer), the total overhead is 75.9M parameters---less than 1\% of the 8B base model.
42	The predictors operate independently across layers, requiring no cross-layer communication at inference.
43	
44	
45	\subsection{Gumbel-Sigmoid Relaxation}
46	\label{sec:method:gumbel}
47	
48	The hard mask $m_j = \mathbf{1}[s_j > \text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.
49	We apply Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} to produce differentiable soft masks:
50	\begin{align}
51	\tilde{m}_j = \sigma_\tau\!\left(\log \frac{s_j}{1 - s_j} + g_1 - g_2\right), \quad g_1, g_2 \sim \text{Gumbel}(0,1),
52	\label{eq:gumbel}
53	\end{align}
54	where $\sigma_\tau(x) = \text{sigmoid}(x / \tau)$ and $\tau$ is a temperature parameter.
55	The Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\tau \to 0$, $\tilde{m}_j$ approaches a binary decision.
56	
57	We anneal $\tau$ from 1.0 to 0.1 over training using a cosine schedule.
58	At high temperature, the soft mask permits gradient flow through all neurons, enabling broad exploration.
59	As temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.
60	
61	\paragraph{Comparison with Straight-Through Estimation.}
62	The straight-through estimator (STE)~\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\partial m / \partial s = 1$).
63	In our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the Lagrangian multiplier and failure to converge to the target sparsity.
64	Gumbel relaxation eliminates this pathology, contributing a 34.5\% improvement (PPL 15.77 $\to$ 11.79 at 50\% sparsity), as we verify empirically in \S\ref{sec:experiments}.
65	
66	
67	\subsection{KL Divergence Training Objective}
68	\label{sec:method:kl}
69	
70	Let $\mathbf{z}_{\text{dense}}$ denote the output logits from a full dense forward pass, and $\mathbf{z}_{\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\{\tilde{\mathbf{m}}^{(\ell)}\}_\ell$ applied at every layer.
71	We minimize the forward KL divergence between the dense and sparse output distributions:
72	\begin{align}
73	\mathcal{L}_{\text{KL}} = D_{\text{KL}}(p_{\text{dense}} \,\|\, p_{\text{sparse}}) = \sum_{v} p_{\text{dense}}^{(v)} \log \frac{p_{\text{dense}}^{(v)}}{p_{\text{sparse}}^{(v)}},
74	\label{eq:kl_loss}
75	\end{align}
76	where $p_{\text{dense}} = \text{softmax}(\mathbf{z}_{\text{dense}})$ and $p_{\text{sparse}} = \text{softmax}(\mathbf{z}_{\text{sparse}})$, summed over the vocabulary $v$ and averaged over sequence positions.
77	The base model is frozen; only the predictor parameters receive gradients.
78	
79	We use forward KL ($D_{\text{KL}}(p_{\text{dense}} \| p_{\text{sparse}})$) rather than reverse KL ($D_{\text{KL}}(p_{\text{sparse}} \| p_{\text{dense}})$).
80	Forward KL is mean-seeking: it penalizes the sparse model heavily wherever the dense model assigns high probability, forcing the sparse distribution to cover the dense model's primary predictions.
81	This is appropriate for sparsity prediction, where the goal is to preserve the dense model's top-token behavior rather than explore alternative modes.
82	No temperature scaling ($T{=}1$) is applied, following the finding that logit-level distillation without temperature is sufficient when the student retains the teacher's architecture~\cite{hinton2015distilling}.
83	
84	
85	\subsection{Lagrangian Sparsity Constraint}
86	\label{sec:method:lagrangian}
87	
88	We enforce a model-level sparsity target $\rho$ via constrained optimization.
89	Let $\bar{s} = \frac{1}{L} \sum_\ell \frac{1}{d_{\text{ff}}} \sum_j \tilde{m}_j^{(\ell)}$ denote the average fraction of retained neurons.
90	The constrained problem is:
91	\begin{align}
92	\min_\theta \; \mathcal{L}_{\text{KL}} \quad \text{s.t.} \quad \bar{s} \leq 1 - \rho.
93	\label{eq:constrained}
94	\end{align}
95	We relax this via the Lagrangian:
96	\begin{align}
97	\mathcal{L} = \mathcal{L}_{\text{KL}} + \lambda \cdot (\bar{s} - (1 - \rho)),
98	\label{eq:lagrangian}
99	\end{align}
100	where $\lambda \geq 0$ is the dual variable, updated by gradient ascent:
101	\begin{align}
102	\lambda \leftarrow \lambda + \eta_\lambda \cdot (\bar{s} - (1 - \rho)).
103	\label{eq:dual_update}
104	\end{align}
105	When sparsity undershoots the target ($\bar{s}$ too large), $\lambda$ increases, strengthening the pruning pressure.
106	When sparsity overshoots, $\lambda$ decreases, allowing the KL objective to recover quality.
107	This eliminates manual tuning of the quality-sparsity tradeoff weight: the dual variable adapts automatically to balance the two objectives throughout training.
108	
109	
110	\subsection{Gradient Analysis: BCE vs.\ KL}
111	\label{sec:method:gradient}
112	
113	This section formalizes the structural difference between BCE and KL training signals---the core theoretical argument for why KL distillation is better suited to global top-$k$ inference.
114	
115	\paragraph{BCE gradient structure.}
116	The standard approach trains the predictor against oracle masks $m_j^* = \mathbf{1}[|g_j| \geq \text{top-}k\text{ threshold}]$ derived from the dense model's activation magnitudes.
117	The loss decomposes per neuron:
118	\begin{align}
119	\mathcal{L}_{\text{BCE}} = -\frac{1}{d_{\text{ff}}} \sum_{j=1}^{d_{\text{ff}}} \bigl[ m_j^* \log \sigma(s_j) + (1 - m_j^*) \log(1 - \sigma(s_j)) \bigr].
120	\label{eq:bce}
121	\end{align}
122	The gradient with respect to predictor logit $s_j$ is:
123	\begin{align}
124	\frac{\partial \mathcal{L}_{\text{BCE}}}{\partial s_j} = \sigma(s_j) - m_j^*.
125	\label{eq:bce_grad}
126	\end{align}
127	This gradient depends \emph{only} on neuron $j$'s own prediction and target.
128	Each neuron is trained independently---there is no inter-neuron coupling in the learning signal.
129	
130	\paragraph{KL gradient structure.}
131	Under KL distillation, the gradient for predictor logit $s_j^{(\ell)}$ in layer $\ell$ is:
132	\begin{align}
133	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \underbrace{\frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}_{\text{sparse}}}}_{\text{(a)}} \cdot \underbrace{\frac{\partial \mathbf{z}_{\text{sparse}}}{\partial \mathbf{h}^{(\ell)}}}_{\text{(b)}} \cdot \underbrace{\frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}}}_{\text{(c)}} \cdot \underbrace{\frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}}}_{\text{(d)}},
134	\label{eq:kl_grad}
135	\end{align}
136	where each factor has a distinct role:
137	\begin{itemize}
138	\item[\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.
139	\item[\textbf{(b)}] The Jacobian through all downstream layers from layer $\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\ell, \ell{+}1, \ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.
140	\item[\textbf{(c)}] The effect of mask element $\tilde{m}_j^{(\ell)}$ on the layer output: $\partial \mathbf{h}^{(\ell)} / \partial \tilde{m}_j^{(\ell)} = (g_j^{(\ell)} \cdot [\mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}]_j) \cdot \mathbf{W}_{d,j}^{(\ell)}$, where $\mathbf{W}_{d,j}^{(\ell)}$ is column $j$ of the down-projection. The down-projection linearly mixes all neurons' contributions, so changing $\tilde{m}_j$ affects the full $d$-dimensional hidden state.
141	\item[\textbf{(d)}] The Gumbel-Sigmoid derivative, providing the differentiable path from logit to mask.
142	\end{itemize}
143	
144	\paragraph{The structural mismatch.}
145	The key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \emph{all} other neurons' mask values.
146	BCE's factorized gradient (Eq.~\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.
147	Under global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons---a combinatorial interaction that BCE cannot capture.
148	
149	Concretely, BCE achieves high per-neuron classification accuracy (typically $>$90\% agreement with oracle masks) yet produces poor output quality under TEAL allocation, because it optimizes a proxy (per-neuron accuracy) misaligned with the true objective (output preservation under global budget allocation).
150	KL directly optimizes the end-to-end objective, with gradients that naturally reflect inter-neuron dependencies through the model's computation graph.
151	As we show in \S\ref{sec:experiments}, this structural advantage persists even when BCE is given 2.71$\times$ more training compute: the gap is architectural, not computational.
152	
153	
154	\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}
155	\label{sec:method:taxonomy}
156	
157	We organize prior work along two axes: \emph{correction granularity} (how the mask adapts to input) and \emph{training signal coupling} (whether the objective captures inter-neuron dependencies).
158	
159	\begin{table}[t]
160	\centering
161	\caption{Taxonomy of learned sparsity prediction methods. Rows indicate correction granularity; columns indicate training signal coupling. Our method fills a previously unexplored cell.}
162	\label{tab:taxonomy}
163	\small
164	\begin{tabular}{lccc}
165	\toprule
166	 & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\
167	\midrule
168	Static & --- & --- & SPON \\
169	Per-layer & --- & ShadowLLM & --- \\
170	Per-token & FastForward & --- & \textbf{Ours} \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	\paragraph{Correction granularity.}
176	\emph{Static} methods~\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.
177	\emph{Per-layer} methods~\cite{akhauri2024shadowllm} condition on a layer-level summary (e.g., the attention output) but share predictions across tokens within a layer.
178	\emph{Per-token} methods~\cite{gautam2026fastforward,liu2023dejavu} produce a unique mask for each input position.
179	
180	\paragraph{Training signal coupling.}
181	\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.
182	\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.
183	\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.
184	
185	SPON~\cite{xu2026spon} operates at the intersection of static granularity and coupled training: it distills a per-layer bias correction via KL but cannot adapt to per-input neuron importance.
186	FastForward~\cite{gautam2026fastforward} achieves per-token granularity but uses BCE training, losing inter-neuron coupling.
187	Our method combines per-token contextual prediction with coupled KL training (Table~\ref{tab:taxonomy}), unifying the advantages of both axes: input-dependent mask generation trained with a signal that captures global neuron interactions through the output distribution.
188	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "6ca0d26c-57dc-45be-9948-90e5da40e411",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.\nThe method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass, eliminating the need for auxiliary error compensation networks at inference.\n\n\\subsection{Problem Formulation}\n\\label{sec:method:formulation}\n\nConsider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\\cite{shazeer2020glu}.\nFor layer $\\ell$, the FFN computes:\n\\begin{align}\n\\mathbf{y}^{(\\ell)} = \\bigl(\\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)},\n\\label{eq:swiglu}\n\\end{align}\nwhere $\\mathbf{x}^{(\\ell)} \\in \\mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\\sigma$ denotes SiLU, $\\mathbf{W}_g^{(\\ell)}, \\mathbf{W}_u^{(\\ell)} \\in \\mathbb{R}^{d \\times d_{\\text{ff}}}$ and $\\mathbf{W}_d^{(\\ell)} \\in \\mathbb{R}^{d_{\\text{ff}} \\times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\\text{ff}}{=}14{,}336$.\n\nDefine the gate activation $\\mathbf{g}^{(\\ell)} = \\sigma(\\mathbf{x}^{(\\ell)} \\mathbf{W}_g^{(\\ell)}) \\in \\mathbb{R}^{d_{\\text{ff}}}$.\nEach element $g_j^{(\\ell)}$ determines the contribution of neuron $j$ to the output.\nWe introduce a binary mask $\\mathbf{m}^{(\\ell)} \\in \\{0,1\\}^{d_{\\text{ff}}}$ that zeros out pruned neurons:\n\\begin{align}\n\\mathbf{y}_{\\text{sparse}}^{(\\ell)} = \\bigl(\\mathbf{m}^{(\\ell)} \\odot \\mathbf{g}^{(\\ell)} \\odot \\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}\\bigr) \\mathbf{W}_d^{(\\ell)}.\n\\label{eq:sparse_ffn}\n\\end{align}\nOur goal is to learn a mask predictor $f_\\theta^{(\\ell)}(\\mathbf{h}) \\to \\mathbf{s}^{(\\ell)} \\in (0,1)^{d_{\\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\\mathbf{h}$.\nAt inference, the scores are fed to a global top-$k$ allocation mechanism~\\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\\rho) \\times L \\times d_{\\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\\rho$.\n\n\n\\subsection{Predictor Architecture}\n\\label{sec:method:predictor}\n\nEach layer $\\ell$ has an independent two-layer MLP predictor:\n\\begin{align}\nf_\\theta^{(\\ell)}(\\mathbf{h}) = \\text{GELU}(\\mathbf{h} \\mathbf{W}_1^{(\\ell)}) \\, \\mathbf{W}_2^{(\\ell)},\n\\label{eq:predictor}\n\\end{align}\nwhere $\\mathbf{W}_1^{(\\ell)} \\in \\mathbb{R}^{d \\times d_b}$ and $\\mathbf{W}_2^{(\\ell)} \\in \\mathbb{R}^{d_b \\times d_{\\text{ff}}}$ with bottleneck dimension $d_b{=}128$.\nThe predictor takes the hidden state after attention (before the FFN) and outputs $d_{\\text{ff}}$-dimensional logits $\\mathbf{s}^{(\\ell)}$, from which the mask is derived.\n\nEach predictor has $(4096 \\times 128) + (128 \\times 14336) = 2.37\\text{M}$ parameters.\nWith 32 independent predictors (one per layer), the total overhead is 75.9M parameters---less than 1\\% of the 8B base model.\nThe predictors operate independently across layers, requiring no cross-layer communication at inference.\n\n\n\\subsection{Gumbel-Sigmoid Relaxation}\n\\label{sec:method:gumbel}\n\nThe hard mask $m_j = \\mathbf{1}[s_j > \\text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.\nWe apply Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} to produce differentiable soft masks:\n\\begin{align}\n\\tilde{m}_j = \\sigma_\\tau\\!\\left(\\log \\frac{s_j}{1 - s_j} + g_1 - g_2\\right), \\quad g_1, g_2 \\sim \\text{Gumbel}(0,1),\n\\label{eq:gumbel}\n\\end{align}\nwhere $\\sigma_\\tau(x) = \\text{sigmoid}(x / \\tau)$ and $\\tau$ is a temperature parameter.\nThe Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\\tau \\to 0$, $\\tilde{m}_j$ approaches a binary decision.\n\nWe anneal $\\tau$ from 1.0 to 0.1 over training using a cosine schedule.\nAt high temperature, the soft mask permits gradient flow through all neurons, enabling broad exploration.\nAs temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.\n\n\\paragraph{Comparison with Straight-Through Estimation.}\nThe straight-through estimator (STE)~\\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\\partial m / \\partial s = 1$).\nIn our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the Lagrangian multiplier and failure to converge to the target sparsity.\nGumbel relaxation eliminates this pathology, contributing a 34.5\\% improvement (PPL 15.77 $\\to$ 11.79 at 50\\% sparsity), as we verify empirically in \\S\\ref{sec:experiments}.\n\n\n\\subsection{KL Divergence Training Objective}\n\\label{sec:method:kl}\n\nLet $\\mathbf{z}_{\\text{dense}}$ denote the output logits from a full dense forward pass, and $\\mathbf{z}_{\\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\\{\\tilde{\\mathbf{m}}^{(\\ell)}\\}_\\ell$ applied at every layer.\nWe minimize the forward KL divergence between the dense and sparse output distributions:\n\\begin{align}\n\\mathcal{L}_{\\text{KL}} = D_{\\text{KL}}(p_{\\text{dense}} \\,\\|\\, p_{\\text{sparse}}) = \\sum_{v} p_{\\text{dense}}^{(v)} \\log \\frac{p_{\\text{dense}}^{(v)}}{p_{\\text{sparse}}^{(v)}},\n\\label{eq:kl_loss}\n\\end{align}\nwhere $p_{\\text{dense}} = \\text{softmax}(\\mathbf{z}_{\\text{dense}})$ and $p_{\\text{sparse}} = \\text{softmax}(\\mathbf{z}_{\\text{sparse}})$, summed over the vocabulary $v$ and averaged over sequence positions.\nThe base model is frozen; only the predictor parameters receive gradients.\n\nWe use forward KL ($D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}})$) rather than reverse KL ($D_{\\text{KL}}(p_{\\text{sparse}} \\| p_{\\text{dense}})$).\nForward KL is mean-seeking: it penalizes the sparse model heavily wherever the dense model assigns high probability, forcing the sparse distribution to cover the dense model's primary predictions.\nThis is appropriate for sparsity prediction, where the goal is to preserve the dense model's top-token behavior rather than explore alternative modes.\nNo temperature scaling ($T{=}1$) is applied, following the finding that logit-level distillation without temperature is sufficient when the student retains the teacher's architecture~\\cite{hinton2015distilling}.\n\n\n\\subsection{Lagrangian Sparsity Constraint}\n\\label{sec:method:lagrangian}\n\nWe enforce a model-level sparsity target $\\rho$ via constrained optimization.\nLet $\\bar{s} = \\frac{1}{L} \\sum_\\ell \\frac{1}{d_{\\text{ff}}} \\sum_j \\tilde{m}_j^{(\\ell)}$ denote the average fraction of retained neurons.\nThe constrained problem is:\n\\begin{align}\n\\min_\\theta \\; \\mathcal{L}_{\\text{KL}} \\quad \\text{s.t.} \\quad \\bar{s} \\leq 1 - \\rho.\n\\label{eq:constrained}\n\\end{align}\nWe relax this via the Lagrangian:\n\\begin{align}\n\\mathcal{L} = \\mathcal{L}_{\\text{KL}} + \\lambda \\cdot (\\bar{s} - (1 - \\rho)),\n\\label{eq:lagrangian}\n\\end{align}\nwhere $\\lambda \\geq 0$ is the dual variable, updated by gradient ascent:\n\\begin{align}\n\\lambda \\leftarrow \\lambda + \\eta_\\lambda \\cdot (\\bar{s} - (1 - \\rho)).\n\\label{eq:dual_update}\n\\end{align}\nWhen sparsity undershoots the target ($\\bar{s}$ too large), $\\lambda$ increases, strengthening the pruning pressure.\nWhen sparsity overshoots, $\\lambda$ decreases, allowing the KL objective to recover quality.\nThis eliminates manual tuning of the quality-sparsity tradeoff weight: the dual variable adapts automatically to balance the two objectives throughout training.\n\n\n\\subsection{Gradient Analysis: BCE vs.\\ KL}\n\\label{sec:method:gradient}\n\nThis section formalizes the structural difference between BCE and KL training signals---the core theoretical argument for why KL distillation is better suited to global top-$k$ inference.\n\n\\paragraph{BCE gradient structure.}\nThe standard approach trains the predictor against oracle masks $m_j^* = \\mathbf{1}[|g_j| \\geq \\text{top-}k\\text{ threshold}]$ derived from the dense model's activation magnitudes.\nThe loss decomposes per neuron:\n\\begin{align}\n\\mathcal{L}_{\\text{BCE}} = -\\frac{1}{d_{\\text{ff}}} \\sum_{j=1}^{d_{\\text{ff}}} \\bigl[ m_j^* \\log \\sigma(s_j) + (1 - m_j^*) \\log(1 - \\sigma(s_j)) \\bigr].\n\\label{eq:bce}\n\\end{align}\nThe gradient with respect to predictor logit $s_j$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{BCE}}}{\\partial s_j} = \\sigma(s_j) - m_j^*.\n\\label{eq:bce_grad}\n\\end{align}\nThis gradient depends \\emph{only} on neuron $j$'s own prediction and target.\nEach neuron is trained independently---there is no inter-neuron coupling in the learning signal.\n\n\\paragraph{KL gradient structure.}\nUnder KL distillation, the gradient for predictor logit $s_j^{(\\ell)}$ in layer $\\ell$ is:\n\\begin{align}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\underbrace{\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}_{\\text{sparse}}}}_{\\text{(a)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{z}_{\\text{sparse}}}{\\partial \\mathbf{h}^{(\\ell)}}}_{\\text{(b)}} \\cdot \\underbrace{\\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}}}_{\\text{(c)}} \\cdot \\underbrace{\\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}}}_{\\text{(d)}},\n\\label{eq:kl_grad}\n\\end{align}\nwhere each factor has a distinct role:\n\\begin{itemize}\n\\item[\\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.\n\\item[\\textbf{(b)}] The Jacobian through all downstream layers from layer $\\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\\ell, \\ell{+}1, \\ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.\n\\item[\\textbf{(c)}] The effect of mask element $\\tilde{m}_j^{(\\ell)}$ on the layer output: $\\partial \\mathbf{h}^{(\\ell)} / \\partial \\tilde{m}_j^{(\\ell)} = (g_j^{(\\ell)} \\cdot [\\mathbf{x}^{(\\ell)} \\mathbf{W}_u^{(\\ell)}]_j) \\cdot \\mathbf{W}_{d,j}^{(\\ell)}$, where $\\mathbf{W}_{d,j}^{(\\ell)}$ is column $j$ of the down-projection. The down-projection linearly mixes all neurons' contributions, so changing $\\tilde{m}_j$ affects the full $d$-dimensional hidden state.\n\\item[\\textbf{(d)}] The Gumbel-Sigmoid derivative, providing the differentiable path from logit to mask.\n\\end{itemize}\n\n\\paragraph{The structural mismatch.}\nThe key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \\emph{all} other neurons' mask values.\nBCE's factorized gradient (Eq.~\\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.\nUnder global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons---a combinatorial interaction that BCE cannot capture.\n\nConcretely, BCE achieves high per-neuron classification accuracy (typically $>$90\\% agreement with oracle masks) yet produces poor output quality under TEAL allocation, because it optimizes a proxy (per-neuron accuracy) misaligned with the true objective (output preservation under global budget allocation).\nKL directly optimizes the end-to-end objective, with gradients that naturally reflect inter-neuron dependencies through the model's computation graph.\nAs we show in \\S\\ref{sec:experiments}, this structural advantage persists even when BCE is given 2.71$\\times$ more training compute: the gap is architectural, not computational.\n\n\n\\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}\n\\label{sec:method:taxonomy}\n\nWe organize prior work along two axes: \\emph{correction granularity} (how the mask adapts to input) and \\emph{training signal coupling} (whether the objective captures inter-neuron dependencies).\n\n\\begin{table}[t]\n\\centering\n\\caption{Taxonomy of learned sparsity prediction methods. Rows indicate correction granularity; columns indicate training signal coupling. Our method fills a previously unexplored cell.}\n\\label{tab:taxonomy}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\\\\n\\midrule\nStatic & --- & --- & SPON \\\\\nPer-layer & --- & ShadowLLM & --- \\\\\nPer-token & FastForward & --- & \\textbf{Ours} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Correction granularity.}\n\\emph{Static} methods~\\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.\n\\emph{Per-layer} methods~\\cite{akhauri2024shadowllm} condition on a layer-level summary (e.g., the attention output) but share predictions across tokens within a layer.\n\\emph{Per-token} methods~\\cite{gautam2026fastforward,liu2023dejavu} produce a unique mask for each input position.\n\n\\paragraph{Training signal coupling.}\n\\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.\n\\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.\n\\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.\n\nSPON~\\cite{xu2026spon} operates at the intersection of static granularity and coupled training: it distills a per-layer bias correction via KL but cannot adapt to per-input neuron importance.\nFastForward~\\cite{gautam2026fastforward} achieves per-token granularity but uses BCE training, losing inter-neuron coupling.\nOur method combines per-token contextual prediction with coupled KL training (Table~\\ref{tab:taxonomy}), unifying the advantages of both axes: input-dependent mask generation trained with a signal that captures global neuron interactions through the output distribution.\n",
      "numLines": 188,
      "startLine": 1,
      "totalLines": 188
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
Now I have all the context I need. Let me also check if there's an existing introduction.tex file and look at the paper directory structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "595fd596-0f27-463d-b0af-2410515bce0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011a5u6KBhpv1JXaDGFaYubd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15392,
      "cache_read_input_tokens": 24791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15392
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

Let me check the paper directory structure and any existing bib file for citation keys.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "18618760-ef81-4b36-beab-207c4dad6d8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011a5u6KBhpv1JXaDGFaYubd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15392,
      "cache_read_input_tokens": 24791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15392
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

<details open><summary>🔧 Tool call — Glob · `toolu_017sgW41cs4L1RP51ta9nFao`</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "1a9ce90f-fc99-4efd-9a1a-46f53946c2ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011a5u6KBhpv1JXaDGFaYubd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15392,
      "cache_read_input_tokens": 24791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15392
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

_source line 14 · 2026-05-16T12:53:44.820Z_

<details><summary>↩ Tool result · `toolu_017sgW41cs4L1RP51ta9nFao`</summary>

```text
paper/references.bib
paper/method.tex
paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "246793aa-8e86-4171-ac23-d524a1088839",
  "tool_use_result": {
    "filenames": [
      "paper/references.bib",
      "paper/method.tex",
      "paper/experiments.tex"
    ],
    "durationMs": 18,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_0155Fu1yWSSGh5GByzVfdzXo`</summary>

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
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "38e0cfee-cd13-4466-a860-69dd122fcef0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aJiCqnBdq37DvWWezYs26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 40183,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 194
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

_source line 16 · 2026-05-16T12:53:47.088Z_

<details><summary>↩ Tool result · `toolu_0155Fu1yWSSGh5GByzVfdzXo`</summary>

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
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "536cede3-22b4-47eb-89fd-02fa670c787e",
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

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context. Let me write the introduction section. I need to:

1. Follow ACL2023 format
2. ~1100 words
3. Follow the story arc provided
4. Use exact numbers provided
5. Use exact citation keys from the bib file
6. Avoid banned phrases
7. Use "no prior work has" instead of "we are the first to"
8. Direct, compelling tone, no filler
9. Reference Figure 1 with \ref{fig:taxonomy}

Let me also check for WINA reference - the experiments.tex mentions WINA as a variant of TEAL, citing \cite{liu2025teal}. So WINA is part of TEAL.


Now I'm drafting the introduction, making sure to establish the motivation clearly, present the problem space with the exact statistics, and build toward the contribution while maintaining the narrative flow.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "0e214fcd-c99a-4902-98e0-58550737db3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HF9JCiYPExzZV5guELAjdc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5145,
      "cache_read_input_tokens": 40377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5145
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

_source line 18_

Writing the introduction now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "53e84f81-67d5-4cbb-97c2-ab588bb212e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HF9JCiYPExzZV5guELAjdc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5145,
      "cache_read_input_tokens": 40377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5145
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

_source line 19_

<details open><summary>🔧 Tool call — Write · `toolu_01GwTUjNWyaWXtF4CaQKzA3t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
  "content": "\\section{Introduction}\n\nSwiGLU feed-forward networks~\\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.\nExploiting this sparsity can yield up to 2$\\times$ inference speedup by pruning 50\\% of FFN neurons per token---without modifying the pretrained weights.\nYet the gap between potential and practice remains wide.\nTraining-free methods such as TEAL~\\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\\% sparsity on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}---a 281\\% increase.\nLearned predictors~\\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add latency and memory overhead at inference.\nThe question is whether a predictor can be trained so that compensation becomes unnecessary.\n\nThe answer depends on the training objective.\nCurrent learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.\nThe gradient of BCE with respect to neuron $j$'s score is $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j = \\sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.\nBut at inference, no neuron is evaluated in isolation.\nTEAL's global top-$k$ mechanism~\\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.\nWhether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \\times d_{\\text{ff}}$ neurons.\nThis creates a structural mismatch: the training objective decomposes per neuron, while the inference allocation is a global combinatorial decision.\nBCE can achieve $>$90\\% per-neuron classification accuracy against oracle masks yet still produce poor output quality under global allocation, because it optimizes a proxy misaligned with the true objective.\n\nKL divergence resolves this mismatch by coupling all neurons through the output distribution.\nInstead of classifying individual neurons, we minimize $D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}})$ between the dense and sparse model outputs, training the predictor to preserve the full next-token distribution under pruning.\nThe gradient for neuron $j$ in layer $\\ell$ factors as:\n\\begin{equation*}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}} \\cdot \\frac{\\partial \\mathbf{z}}{\\partial \\mathbf{h}^{(\\ell)}} \\cdot \\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}} \\cdot \\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}},\n\\end{equation*}\nwhere the Jacobian $\\partial \\mathbf{z} / \\partial \\mathbf{h}^{(\\ell)}$ propagates through all downstream layers, making each neuron's gradient dependent on every other neuron's mask state.\nChanging one neuron's mask affects all output logits; KL captures this because it measures distributional divergence over the entire vocabulary.\nA Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} provides differentiable mask sampling during training, bridging the gap between soft training masks and hard inference decisions.\nThe predictor itself is a lightweight two-layer MLP (Linear $4096 \\to 128$, GELU, Linear $128 \\to 14336$) with 2.37M parameters per layer and 75.9M total---under 1\\% of the base model---and requires no compensation network at inference.\n\nEmpirically, the structural argument is borne out across sparsity levels, training budgets, and architectures.\nAt 50\\% sparsity on LLaMA-3.1-8B, the KL-trained predictor achieves PPL 11.79 under TEAL's global allocation, compared to 23.31 for vanilla TEAL.\nBCE trained for 2700 steps (2.71$\\times$ our compute budget) reaches only 27.97, and its training loss saturates with $\\Delta = -0.006$ over the final 2200 steps---confirming that the failure is structural, not computational.\nThe KL advantage scales super-linearly with sparsity: 18\\% relative improvement at 30\\%, 49\\% at 50\\%, and 82\\% at 70\\%.\nCross-architecture evaluation on Mistral-7B-v0.3~\\cite{jiang2023mistral} yields +63\\% relative degradation from dense, compared to +93\\% on LLaMA, confirming generalization to SwiGLU models with different attention configurations.\nWe also analyze SPON's~\\cite{xu2026spon} static bias correction and find it near-orthogonal to the predictor's effect (cosine similarity 0.196), recovering only 2.4\\% of remaining error---the KL predictor already captures most of the recoverable signal.\n\nTo situate these findings, we propose a two-dimensional taxonomy (Figure~\\ref{fig:taxonomy}) that classifies sparsity prediction methods along \\emph{correction granularity} (static, per-layer, per-token) and \\emph{training signal coupling} (decomposed, intermediate, coupled).\nPrior methods occupy distinct cells: SPON~\\cite{xu2026spon} combines static correction with coupled KL training; ShadowLLM~\\cite{akhauri2024shadowllm} uses per-layer prediction with intermediate MSE; FastForward~\\cite{gautam2026fastforward} and DejaVu~\\cite{liu2023dejavu} achieve per-token granularity but with decomposed BCE objectives.\nNo prior work has combined per-token contextual prediction with a coupled training signal.\nOur method fills this cell, unifying input-dependent mask generation with an objective that reflects global neuron interactions through the output distribution.\n\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item We show that a KL-trained contextual predictor eliminates the need for error compensation networks in activation sparsity, and provide a formal gradient analysis explaining the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation.\n\\item We propose a 2D taxonomy (correction granularity $\\times$ training signal coupling) that unifies existing activation sparsity methods (Figure~\\ref{fig:taxonomy}) and identifies the previously unexplored cell our method occupies.\n\\item We identify a phase transition in sparsity regimes---allocation-fixable ($\\leq$30\\%, where predictor and allocation choices recover downstream performance) vs.\\ capacity-limited ($\\geq$50\\%, where no method recovers reasoning ability)---and confirm via SPON orthogonality analysis that static correction provides diminishing returns once a coupled predictor is present.\n\\end{itemize}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "de5d2d41-9943-4b3f-91c7-062d3e403936",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HF9JCiYPExzZV5guELAjdc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5145,
      "cache_read_input_tokens": 40377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5145
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

_source line 20 · 2026-05-16T12:54:43.101Z_

<details><summary>↩ Tool result · `toolu_01GwTUjNWyaWXtF4CaQKzA3t`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "a0a51458-acd4-4c95-94f5-5ecce8ace60a",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
    "content": "\\section{Introduction}\n\nSwiGLU feed-forward networks~\\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.\nExploiting this sparsity can yield up to 2$\\times$ inference speedup by pruning 50\\% of FFN neurons per token---without modifying the pretrained weights.\nYet the gap between potential and practice remains wide.\nTraining-free methods such as TEAL~\\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\\% sparsity on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}---a 281\\% increase.\nLearned predictors~\\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add latency and memory overhead at inference.\nThe question is whether a predictor can be trained so that compensation becomes unnecessary.\n\nThe answer depends on the training objective.\nCurrent learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.\nThe gradient of BCE with respect to neuron $j$'s score is $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j = \\sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.\nBut at inference, no neuron is evaluated in isolation.\nTEAL's global top-$k$ mechanism~\\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.\nWhether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \\times d_{\\text{ff}}$ neurons.\nThis creates a structural mismatch: the training objective decomposes per neuron, while the inference allocation is a global combinatorial decision.\nBCE can achieve $>$90\\% per-neuron classification accuracy against oracle masks yet still produce poor output quality under global allocation, because it optimizes a proxy misaligned with the true objective.\n\nKL divergence resolves this mismatch by coupling all neurons through the output distribution.\nInstead of classifying individual neurons, we minimize $D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}})$ between the dense and sparse model outputs, training the predictor to preserve the full next-token distribution under pruning.\nThe gradient for neuron $j$ in layer $\\ell$ factors as:\n\\begin{equation*}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}} \\cdot \\frac{\\partial \\mathbf{z}}{\\partial \\mathbf{h}^{(\\ell)}} \\cdot \\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}} \\cdot \\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}},\n\\end{equation*}\nwhere the Jacobian $\\partial \\mathbf{z} / \\partial \\mathbf{h}^{(\\ell)}$ propagates through all downstream layers, making each neuron's gradient dependent on every other neuron's mask state.\nChanging one neuron's mask affects all output logits; KL captures this because it measures distributional divergence over the entire vocabulary.\nA Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} provides differentiable mask sampling during training, bridging the gap between soft training masks and hard inference decisions.\nThe predictor itself is a lightweight two-layer MLP (Linear $4096 \\to 128$, GELU, Linear $128 \\to 14336$) with 2.37M parameters per layer and 75.9M total---under 1\\% of the base model---and requires no compensation network at inference.\n\nEmpirically, the structural argument is borne out across sparsity levels, training budgets, and architectures.\nAt 50\\% sparsity on LLaMA-3.1-8B, the KL-trained predictor achieves PPL 11.79 under TEAL's global allocation, compared to 23.31 for vanilla TEAL.\nBCE trained for 2700 steps (2.71$\\times$ our compute budget) reaches only 27.97, and its training loss saturates with $\\Delta = -0.006$ over the final 2200 steps---confirming that the failure is structural, not computational.\nThe KL advantage scales super-linearly with sparsity: 18\\% relative improvement at 30\\%, 49\\% at 50\\%, and 82\\% at 70\\%.\nCross-architecture evaluation on Mistral-7B-v0.3~\\cite{jiang2023mistral} yields +63\\% relative degradation from dense, compared to +93\\% on LLaMA, confirming generalization to SwiGLU models with different attention configurations.\nWe also analyze SPON's~\\cite{xu2026spon} static bias correction and find it near-orthogonal to the predictor's effect (cosine similarity 0.196), recovering only 2.4\\% of remaining error---the KL predictor already captures most of the recoverable signal.\n\nTo situate these findings, we propose a two-dimensional taxonomy (Figure~\\ref{fig:taxonomy}) that classifies sparsity prediction methods along \\emph{correction granularity} (static, per-layer, per-token) and \\emph{training signal coupling} (decomposed, intermediate, coupled).\nPrior methods occupy distinct cells: SPON~\\cite{xu2026spon} combines static correction with coupled KL training; ShadowLLM~\\cite{akhauri2024shadowllm} uses per-layer prediction with intermediate MSE; FastForward~\\cite{gautam2026fastforward} and DejaVu~\\cite{liu2023dejavu} achieve per-token granularity but with decomposed BCE objectives.\nNo prior work has combined per-token contextual prediction with a coupled training signal.\nOur method fills this cell, unifying input-dependent mask generation with an objective that reflects global neuron interactions through the output distribution.\n\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item We show that a KL-trained contextual predictor eliminates the need for error compensation networks in activation sparsity, and provide a formal gradient analysis explaining the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation.\n\\item We propose a 2D taxonomy (correction granularity $\\times$ training signal coupling) that unifies existing activation sparsity methods (Figure~\\ref{fig:taxonomy}) and identifies the previously unexplored cell our method occupies.\n\\item We identify a phase transition in sparsity regimes---allocation-fixable ($\\leq$30\\%, where predictor and allocation choices recover downstream performance) vs.\\ capacity-limited ($\\geq$50\\%, where no method recovers reasoning ability)---and confirm via SPON orthogonality analysis that static correction provides diminishing returns once a coupled predictor is present.\n\\end{itemize}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 21_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "55ab4107-02f9-485a-8b95-4b5720f13303",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011SRuobem15rHbYMizPCETo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 45522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2196
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

_source line 22_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HCzSYFyWxr7y9gb6sDnQcb`</summary>

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
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "7b83b3d4-e360-442d-9178-bd4af388d30d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011SRuobem15rHbYMizPCETo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2196,
      "cache_read_input_tokens": 45522,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2196
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

_source line 23 · 2026-05-16T12:54:46.807Z_

<details><summary>↩ Tool result · `toolu_01HCzSYFyWxr7y9gb6sDnQcb`</summary>

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
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "16cf176e-d906-48c3-882f-c9f06d9234be",
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

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01FCHNrDTcyX9Bo3RMMSoDCE`</summary>

```json
{
  "name": "introduction.tex",
  "type": "paper",
  "description": "Introduction section (§1) for EMNLP 2026 paper on KL distillation for contextual sparsity prediction in SwiGLU LLMs",
  "project": "distill_sparse_swiglu",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
  "tags": [
    "paper",
    "introduction",
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
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "0f99f2df-75ee-4433-becd-ba7b29d7cd18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9a3wetADDBrT4RgfH6MHP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 47718,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 25 · 2026-05-16T12:54:51.575Z_

<details><summary>↩ Tool result · `toolu_01FCHNrDTcyX9Bo3RMMSoDCE`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_d8e146\", \"name\": \"introduction.tex\", \"type\": \"paper\", \"description\": \"Introduction section (§1) for EMNLP 2026 paper on KL distillation for contextual sparsity prediction in SwiGLU LLMs\", \"path\": \"projects/distill_sparse_swiglu/artifacts/_project/paper/introduction.tex\", \"url\": null, \"project\": \"distill_sparse_swiglu\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T12:54:51.509666+00:00\", \"tags\": [\"paper\", \"introduction\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "9a4489ce-9d4c-4eaf-ba14-049d1a6b5b3d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_d8e146\\\", \\\"name\\\": \\\"introduction.tex\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Introduction section (§1) for EMNLP 2026 paper on KL distillation for contextual sparsity prediction in SwiGLU LLMs\\\", \\\"path\\\": \\\"projects/distill_sparse_swiglu/artifacts/_project/paper/introduction.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"distill_sparse_swiglu\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T12:54:51.509666+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"introduction\\\", \\\"latex\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_d8e146\", \"name\": \"introduction.tex\", \"type\": \"paper\", \"description\": \"Introduction section (§1) for EMNLP 2026 paper on KL distillation for contextual sparsity prediction in SwiGLU LLMs\", \"path\": \"projects/distill_sparse_swiglu/artifacts/_project/paper/introduction.tex\", \"url\": null, \"project\": \"distill_sparse_swiglu\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T12:54:51.509666+00:00\", \"tags\": [\"paper\", \"introduction\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

Introduction written to `paper/introduction.tex`. ~1050 words, 5 paragraphs following the specified story arc:

1. **Hook** — SwiGLU sparsity potential vs. training-free degradation (TEAL 23.31 PPL) and learned predictor overhead
2. **Structural mismatch** — BCE gradient is per-neuron factorized, but inference uses global top-k; formal gradient equation showing independence
3. **KL mechanism** — gradient chain rule through full Jacobian couples all neurons; Gumbel-Sigmoid relaxation; predictor architecture (2.37M/layer, 75.9M total)
4. **Results** — KL 11.79 vs TEAL 23.31 vs BCE 27.97; scaling 18%/49%/82%; Mistral +63%; SPON cos_sim 0.196, 2.4% recovery
5. **Contributions** — 3 bulleted items: KL eliminates compensation + gradient analysis, 2D taxonomy, phase transition + SPON orthogonality

All required citation keys, numbers, and the Figure 1 reference are included. No banned phrases used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "uuid": "54d26a71-145f-40b1-ada5-dd3eae7c94a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEqpZo2TjGsSsAp55UxstQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 519,
      "cache_read_input_tokens": 48540,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 519
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

Introduction written to `paper/introduction.tex`. ~1050 words, 5 paragraphs following the specified story arc:

1. **Hook** — SwiGLU sparsity potential vs. training-free degradation (TEAL 23.31 PPL) and learned predictor overhead
2. **Structural mismatch** — BCE gradient is per-neuron factorized, but inference uses global top-k; formal gradient equation showing independence
3. **KL mechanism** — gradient chain rule through full Jacobian couples all neurons; Gumbel-Sigmoid relaxation; predictor architecture (2.37M/layer, 75.9M total)
4. **Results** — KL 11.79 vs TEAL 23.31 vs BCE 27.97; scaling 18%/49%/82%; Mistral +63%; SPON cos_sim 0.196, 2.4% recovery
5. **Contributions** — 3 bulleted items: KL eliminates compensation + gradient analysis, 2D taxonomy, phase transition + SPON orthogonality

All required citation keys, numbers, and the Figure 1 reference are included. No banned phrases used.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 88911,
  "duration_api_ms": 89816,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "ce39fdc5-433d-4234-853d-6ca693c4413f",
  "total_cost_usd": 0.4457195,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 37218,
    "cache_read_input_tokens": 258972,
    "output_tokens": 3244,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37218,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 280,
        "cache_read_input_tokens": 48540,
        "cache_creation_input_tokens": 519,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 519
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2386,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0024660000000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 3244,
      "cacheReadInputTokens": 258972,
      "cacheCreationInputTokens": 37218,
      "webSearchRequests": 0,
      "costUSD": 0.4432535,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b4d3fb7d-5008-46df-8de5-1b3854f572ea"
}
```

</details>

---
