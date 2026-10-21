# paper writing related work

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260518T102014.log`
- **Structured JSON:** [`78cd47b9cab481dc5fd4.json`](../../sessions/78/78cd47b9cab481dc5fd4.json)

## Before a recorded user message

49 recorded events

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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
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
  "uuid": "b359fcf7-6daa-4ae9-bea5-5b5ac2c8e2b3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1779100800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "23d2d6aa-f361-4303-910f-45c7f6ef4714",
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and all context documents in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "085eae0e-eca6-47da-92ef-ff249af3adf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGdBNKWZdFNVgFJkbQfyHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13866
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

<details open><summary>🔧 Tool call — Read · `toolu_0184AjvmUt4wp9gPF1v71wvF`</summary>

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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "257b3247-bb1f-48c5-a112-b8b0e290bf7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGdBNKWZdFNVgFJkbQfyHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13866
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

_source line 6 · 2026-05-18T10:20:27.571Z_

<details><summary>↩ Tool result · `toolu_0184AjvmUt4wp9gPF1v71wvF`</summary>

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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "d6904626-73d6-4ae8-bd6f-67c880927eb3",
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

<details open><summary>🔧 Tool call — Read · `toolu_01UWKn23bZCJHTtTfSEBRDA5`</summary>

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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "fbfa6e12-d014-4681-b297-db097a9814e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGdBNKWZdFNVgFJkbQfyHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13866
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

_source line 8 · 2026-05-18T10:20:27.906Z_

<details><summary>↩ Tool result · `toolu_01UWKn23bZCJHTtTfSEBRDA5`</summary>

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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "62a49bdc-ba14-4314-bc98-8f2b7ee7a462",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Y9JjEd31SnA4rWEnZ5ovvm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "eb3b8781-57fd-4dc3-98e8-c4a01a4623ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGdBNKWZdFNVgFJkbQfyHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13866
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

_source line 10 · 2026-05-18T10:20:28.381Z_

<details><summary>↩ Tool result · `toolu_01Y9JjEd31SnA4rWEnZ5ovvm`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	Methods for improving VLA robustness divide into training-time and inference-time approaches.
6	
7	\paragraph{Training-time methods.}
8	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.
9	SRPO~\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.
10	DiG-Flow~\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.
11	TT-VLA~\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.
12	A shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.
13	
14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.
17	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\,s per control step---prohibitive for real-time manipulation.
18	A2C2~\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.
19	
20	A2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy.
21	The key architectural difference is that ACR-VLA operates as a two-stage pipeline---multi-sample conformal selection followed by bounded residual correction---whereas A2C2 applies per-step correction directly to the base policy's action chunks without a selection stage.
22	ACR-VLA additionally enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\ref{sec:magnitude_results}).
23	Selection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.
24	Correction alone lacks a mechanism to identify a good starting point.
25	ACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.
26	
27	\subsection{Conformal Prediction in Robotics}
28	
29	Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\cite{angelopoulos2023gentle}.
30	For multivariate outputs, Braun et al.~\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.
31	
32	In robotics, CP has been applied to several safety-critical settings.
33	Conformalized Teleoperation~\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.
34	CP-in-the-Loop~\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.
35	ACP+CBF~\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.
36	A common pattern across these methods is that CP serves as a \emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.
37	
38	ACR-VLA uses Mahalanobis nonconformity scores derived from shrinkage covariance estimates in its selection stage, but does \emph{not} claim formal coverage guarantees for the corrected output.
39	CP serves here as a scoring mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure is available as conditioning features for the correction module (though our ablations find that observation features alone suffice; Section~\ref{sec:ablation}).
40	The downstream correction module produces a refined action whose relationship to the original conformal region is no longer governed by coverage theory.
41	
42	\subsection{Residual Policy Learning}
43	
44	Residual policy learning augments a base controller with a learned additive correction.
45	Silver et al.~\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization to ensure the learned residual starts from the base policy's behavior and gradually improves upon it.
46	Subsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.
47	TRANSIC~\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to decide whether to apply a sim-to-real residual, demonstrating that ungated correction causes model collapse.
48	PLD~\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\xi, \xi]$) via off-policy RL, then distills improved trajectories back into the base model.
49	DRC~\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade after application.
50	
51	Magnitude control is the key connection to ACR-VLA: Silver et al.\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, DRC uses exponential decay after correction events.
52	ACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\ref{sec:experiments}).
53	We view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.
54	A second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.
55	
56	\subsection{Uncertainty Quantification for VLAs}
57	
58	Recent work has developed UQ methods tailored to VLA architectures.
59	DiU~\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.
60	SAFE~\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering intervention when anomalous states are detected.
61	Zollo and Zemel~\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.
62	
63	ACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.
64	The multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.
65	Functionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\cite{zollo2025vla_calibration} targets confidence reliability.
66	Our ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "c44a71e1-2fa9-4e90-9b94-02d8676e1e61",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.\nTT-VLA~\\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.\nA shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\\,s per control step---prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy.\nThe key architectural difference is that ACR-VLA operates as a two-stage pipeline---multi-sample conformal selection followed by bounded residual correction---whereas A2C2 applies per-step correction directly to the base policy's action chunks without a selection stage.\nACR-VLA additionally enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nSelection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.\nCorrection alone lacks a mechanism to identify a good starting point.\nACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.\n\n\\subsection{Conformal Prediction in Robotics}\n\nConformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\\cite{angelopoulos2023gentle}.\nFor multivariate outputs, Braun et al.~\\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.\n\nIn robotics, CP has been applied to several safety-critical settings.\nConformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.\nCP-in-the-Loop~\\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.\nACP+CBF~\\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.\nA common pattern across these methods is that CP serves as a \\emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.\n\nACR-VLA uses Mahalanobis nonconformity scores derived from shrinkage covariance estimates in its selection stage, but does \\emph{not} claim formal coverage guarantees for the corrected output.\nCP serves here as a scoring mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure is available as conditioning features for the correction module (though our ablations find that observation features alone suffice; Section~\\ref{sec:ablation}).\nThe downstream correction module produces a refined action whose relationship to the original conformal region is no longer governed by coverage theory.\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization to ensure the learned residual starts from the base policy's behavior and gradually improves upon it.\nSubsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to decide whether to apply a sim-to-real residual, demonstrating that ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade after application.\n\nMagnitude control is the key connection to ACR-VLA: Silver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, DRC uses exponential decay after correction events.\nACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nWe view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.\nA second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.\n\n\\subsection{Uncertainty Quantification for VLAs}\n\nRecent work has developed UQ methods tailored to VLA architectures.\nDiU~\\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.\nSAFE~\\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering intervention when anomalous states are detected.\nZollo and Zemel~\\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.\n\nACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.\nThe multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.\nFunctionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\\cite{zollo2025vla_calibration} targets confidence reliability.\nOur ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.",
      "numLines": 66,
      "startLine": 1,
      "totalLines": 66
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01Vig8wxrW2PaFuRr6uztB9W`</summary>

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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "d39b363f-167a-4b19-8f5d-f4a7ea193f32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGdBNKWZdFNVgFJkbQfyHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13866
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

_source line 12 · 2026-05-18T10:20:32.217Z_

<details><summary>↩ Tool result · `toolu_01Vig8wxrW2PaFuRr6uztB9W`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	% --- Para 1: VLAs are impressive but fragile under distribution shift ---
5	Vision-Language-Action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached near-saturation on in-distribution benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this performance masks severe fragility: visual and physical perturbations common in deployment (camera viewpoint shifts, object layout changes, robot initial-state variation) routinely degrade success by over 65 percentage points.
7	On the LIBERO+ benchmark~\cite{fei2025liberoplus}, $\pi_0$ drops from 94.2\% to 6.6\% under initial-state perturbation, and UniVLA drops from 95.2\% to 4.3\% under viewpoint changes.
8	Closing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled laboratory settings.
9	
10	% --- Para 2: Existing approaches and the gap ---
11	Two lines of work address this challenge.
12	Training-time methods improve the base policy through robustness-aware objectives~\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\cite{liu2026ttvla}, but require retraining or per-task RL and remain bounded by the training distribution.
13	Inference-time methods leave the policy frozen: ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression for uncertainty quantification and out-of-distribution detection, but does not learn corrective residuals; A2C2~\cite{a2c2_2025} trains a per-step correction head on frozen VLA action chunks, but applies correction unconditionally without multi-sample selection or explicit magnitude control; VLA-Pilot~\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\,s per control step.
14	Despite growing interest in inference-time action refinement, fundamental design questions remain unanswered: how much does candidate selection contribute relative to learned correction?
15	What observation features should condition the correction module?
16	How sensitive is closed-loop performance to correction magnitude?
17	No existing work provides a systematic decomposition of these factors.
18	
19	% --- Para 3: Our approach — sample-then-correct ---
20	We introduce ACR-VLA, an inference-time action refinement module for frozen flow-matching VLAs.
21	At each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the candidate closest to the sample mean by $L_2$ distance, and applies a learned residual correction via a lightweight Conformal Residual Module (CRM).
22	The CRM is a ${\sim}$327K-parameter MLP that takes as input the frozen VLA's observation embedding ($\mathbb{R}^{960}$) concatenated with the selected action ($\mathbb{R}^{30}$) and predicts a residual $\boldsymbol{\delta}$ whose $L_2$ norm is clipped to a bound $\varepsilon$, producing the corrected action $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
23	The key design insight is twofold: correction on a pre-screened starting point is more reliable than correction on an arbitrary single sample, and bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.
24	The base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.
25	
26	% --- Para 4: Three key findings ---
27	We evaluate ACR-VLA on LIBERO-Object and LIBERO-Spatial (10 tasks, 100 trials each) using SmolVLA~\cite{shukor2025smolvla} as the frozen backbone.
28	Three findings emerge.
29	
30	\textbf{(1) The full pipeline significantly improves over the frozen VLA, with correction as the dominant factor.}
31	With observation-only conditioning at $\varepsilon{=}0.2$, the pipeline achieves 17.5\% mean success across 6 seeds versus 11.2\% for VLA-only across 5 seeds (+6.3\,pp, pooled Fisher's exact $p = 0.0074$, Cohen's $d = 1.21$).
32	Component decomposition reveals that correction accounts for ${\sim}$5\,pp and selection for ${\sim}$1\,pp: at $K{=}1$ (correction without selection), success is 10.3\%, at the VLA-only level; argmin selection alone yields 12.4\%.
33	Neither component suffices in isolation.
34	On LIBERO-Spatial, all methods cluster within 30--35\%, a null result that bounds the scope of action-level correction to object-centric manipulation (Section~\ref{sec:main_results}, Table~\ref{tab:main}).
35	
36	\textbf{(2) Observation features suffice for correction; conformal uncertainty features hurt.}
37	We compare three CRM conditioning variants at fixed $\varepsilon{=}0.1$: observation-only conditioning (19\%, seed 42) substantially outperforms per-DOF conformal conditioning (11\%), argmin selection alone (12\%), and scalar uncertainty conditioning (9\%).
38	The observation-only variant is also robust across magnitude bounds, maintaining 13.5--17.5\% for all tested $\varepsilon$, while per-DOF conditioning collapses from 14\% to 0\% as $\varepsilon$ increases.
39	The root cause is noisy covariance estimation from only $K{=}10$ samples in 6 dimensions (Section~\ref{sec:ablation}, Section~\ref{sec:magnitude_results}).
40	
41	\textbf{(3) Multi-sample correction requires stochastic action diversity.}
42	SmolVLA (flow-matching) produces diverse samples suitable for selection and correction.
43	OpenVLA~\cite{kim2024openvla} (autoregressive tokenization) generates 8 out of 10 identical samples with per-DOF variance below $10^{-30}$.
44	This establishes an architectural applicability boundary: the pipeline is specific to stochastic generative VLAs (Section~\ref{sec:applicability}, Figure~\ref{fig:diversity}).
45	
46	% --- Para 5: Contributions ---
47	Our contributions are:
48	\begin{enumerate}[leftmargin=*,nosep]
49	  \item \textbf{A multi-sample inference-time correction pipeline with component decomposition.}
50	  We propose ACR-VLA, which combines $L_2$ argmin selection with bounded residual correction for frozen flow-matching VLAs, and decompose the pipeline into selection (${\sim}$1\,pp) and correction (${\sim}$5\,pp) contributions.
51	  The full pipeline achieves a statistically significant +6.3\,pp improvement over the frozen VLA baseline ($p = 0.0074$, 6 seeds) on LIBERO-Object (Section~\ref{sec:main_results}).
52	
53	  \item \textbf{First systematic conditioning and magnitude study, with an honest negative on conformal features.}
54	  We compare three conditioning variants across a $6{\times}$ range of magnitude bounds and find that observation-only conditioning is robust across all settings, while per-DOF conformal features and scalar uncertainty are harmful.
55	  This challenges the intuition that richer uncertainty features improve correction (Section~\ref{sec:ablation}, Section~\ref{sec:magnitude_results}).
56	
57	  \item \textbf{Applicability boundary: stochastic diversity as a prerequisite.}
58	  We show that tokenized VLAs lack the sample diversity required for multi-sample correction and that action-level correction does not transfer to spatial reasoning tasks, establishing clear scope boundaries for inference-time action refinement (Section~\ref{sec:applicability}).
59	\end{enumerate}
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "f93a3919-2148-4147-9d31-9bfdc9e840bf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% --- Para 1: VLAs are impressive but fragile under distribution shift ---\nVision-Language-Action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla,lipman2023flow} have reached near-saturation on in-distribution benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this performance masks severe fragility: visual and physical perturbations common in deployment (camera viewpoint shifts, object layout changes, robot initial-state variation) routinely degrade success by over 65 percentage points.\nOn the LIBERO+ benchmark~\\cite{fei2025liberoplus}, $\\pi_0$ drops from 94.2\\% to 6.6\\% under initial-state perturbation, and UniVLA drops from 95.2\\% to 4.3\\% under viewpoint changes.\nClosing this robustness gap without retraining the base policy is a prerequisite for deploying VLAs outside tightly controlled laboratory settings.\n\n% --- Para 2: Existing approaches and the gap ---\nTwo lines of work address this challenge.\nTraining-time methods improve the base policy through robustness-aware objectives~\\cite{srpo2025,robustvla2025,digflow2025} or test-time reinforcement learning~\\cite{liu2026ttvla}, but require retraining or per-task RL and remain bounded by the training distribution.\nInference-time methods leave the policy frozen: ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression for uncertainty quantification and out-of-distribution detection, but does not learn corrective residuals; A2C2~\\cite{a2c2_2025} trains a per-step correction head on frozen VLA action chunks, but applies correction unconditionally without multi-sample selection or explicit magnitude control; VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary optimization over action samples, but incurs 2.41\\,s per control step.\nDespite growing interest in inference-time action refinement, fundamental design questions remain unanswered: how much does candidate selection contribute relative to learned correction?\nWhat observation features should condition the correction module?\nHow sensitive is closed-loop performance to correction magnitude?\nNo existing work provides a systematic decomposition of these factors.\n\n% --- Para 3: Our approach — sample-then-correct ---\nWe introduce ACR-VLA, an inference-time action refinement module for frozen flow-matching VLAs.\nAt each control step, ACR-VLA draws $K{=}10$ action samples from the frozen VLA, selects the candidate closest to the sample mean by $L_2$ distance, and applies a learned residual correction via a lightweight Conformal Residual Module (CRM).\nThe CRM is a ${\\sim}$327K-parameter MLP that takes as input the frozen VLA's observation embedding ($\\mathbb{R}^{960}$) concatenated with the selected action ($\\mathbb{R}^{30}$) and predicts a residual $\\boldsymbol{\\delta}$ whose $L_2$ norm is clipped to a bound $\\varepsilon$, producing the corrected action $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\nThe key design insight is twofold: correction on a pre-screened starting point is more reliable than correction on an arbitrary single sample, and bounding the correction magnitude prevents compounding errors from destabilizing the closed-loop trajectory.\nThe base VLA is never modified; ACR-VLA attaches as a post-hoc module to any frozen flow-matching VLA.\n\n% --- Para 4: Three key findings ---\nWe evaluate ACR-VLA on LIBERO-Object and LIBERO-Spatial (10 tasks, 100 trials each) using SmolVLA~\\cite{shukor2025smolvla} as the frozen backbone.\nThree findings emerge.\n\n\\textbf{(1) The full pipeline significantly improves over the frozen VLA, with correction as the dominant factor.}\nWith observation-only conditioning at $\\varepsilon{=}0.2$, the pipeline achieves 17.5\\% mean success across 6 seeds versus 11.2\\% for VLA-only across 5 seeds (+6.3\\,pp, pooled Fisher's exact $p = 0.0074$, Cohen's $d = 1.21$).\nComponent decomposition reveals that correction accounts for ${\\sim}$5\\,pp and selection for ${\\sim}$1\\,pp: at $K{=}1$ (correction without selection), success is 10.3\\%, at the VLA-only level; argmin selection alone yields 12.4\\%.\nNeither component suffices in isolation.\nOn LIBERO-Spatial, all methods cluster within 30--35\\%, a null result that bounds the scope of action-level correction to object-centric manipulation (Section~\\ref{sec:main_results}, Table~\\ref{tab:main}).\n\n\\textbf{(2) Observation features suffice for correction; conformal uncertainty features hurt.}\nWe compare three CRM conditioning variants at fixed $\\varepsilon{=}0.1$: observation-only conditioning (19\\%, seed 42) substantially outperforms per-DOF conformal conditioning (11\\%), argmin selection alone (12\\%), and scalar uncertainty conditioning (9\\%).\nThe observation-only variant is also robust across magnitude bounds, maintaining 13.5--17.5\\% for all tested $\\varepsilon$, while per-DOF conditioning collapses from 14\\% to 0\\% as $\\varepsilon$ increases.\nThe root cause is noisy covariance estimation from only $K{=}10$ samples in 6 dimensions (Section~\\ref{sec:ablation}, Section~\\ref{sec:magnitude_results}).\n\n\\textbf{(3) Multi-sample correction requires stochastic action diversity.}\nSmolVLA (flow-matching) produces diverse samples suitable for selection and correction.\nOpenVLA~\\cite{kim2024openvla} (autoregressive tokenization) generates 8 out of 10 identical samples with per-DOF variance below $10^{-30}$.\nThis establishes an architectural applicability boundary: the pipeline is specific to stochastic generative VLAs (Section~\\ref{sec:applicability}, Figure~\\ref{fig:diversity}).\n\n% --- Para 5: Contributions ---\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A multi-sample inference-time correction pipeline with component decomposition.}\n  We propose ACR-VLA, which combines $L_2$ argmin selection with bounded residual correction for frozen flow-matching VLAs, and decompose the pipeline into selection (${\\sim}$1\\,pp) and correction (${\\sim}$5\\,pp) contributions.\n  The full pipeline achieves a statistically significant +6.3\\,pp improvement over the frozen VLA baseline ($p = 0.0074$, 6 seeds) on LIBERO-Object (Section~\\ref{sec:main_results}).\n\n  \\item \\textbf{First systematic conditioning and magnitude study, with an honest negative on conformal features.}\n  We compare three conditioning variants across a $6{\\times}$ range of magnitude bounds and find that observation-only conditioning is robust across all settings, while per-DOF conformal features and scalar uncertainty are harmful.\n  This challenges the intuition that richer uncertainty features improve correction (Section~\\ref{sec:ablation}, Section~\\ref{sec:magnitude_results}).\n\n  \\item \\textbf{Applicability boundary: stochastic diversity as a prerequisite.}\n  We show that tokenized VLAs lack the sample diversity required for multi-sample correction and that action-level correction does not transfer to spatial reasoning tasks, establishing clear scope boundaries for inference-time action refinement (Section~\\ref{sec:applicability}).\n\\end{enumerate}\n",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 60
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_015nxdaxQHM1ScEs18gGKnS3`</summary>

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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "95f9a026-0c50-4051-bc49-7829e9b210ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGdBNKWZdFNVgFJkbQfyHx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13866,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13866
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

_source line 14 · 2026-05-18T10:20:32.359Z_

<details><summary>↩ Tool result · `toolu_015nxdaxQHM1ScEs18gGKnS3`</summary>

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
30	The CRM consists of three fully connected layers with ReLU activations: $\mathrm{Linear}(n_{\mathrm{in}}, 256) \to \mathrm{ReLU} \to \mathrm{Linear}(256, 256) \to \mathrm{ReLU} \to \mathrm{Linear}(256, 30)$, preceded by input normalization. For the primary obs\_only variant ($n_{\mathrm{in}}{=}990$), the input is the concatenation of the frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{960}$ from SmolVLA's vision-language encoder and the selected action $a_{\mathrm{base}} \in \mathbb{R}^{30}$ ($H{=}5$ steps $\times$ $d{=}6$ DOFs); concatenation order is arbitrary for fully connected layers, for a total of 327,198 parameters (${\sim}$327K). The output is a residual $\boldsymbol{\delta} \in \mathbb{R}^{30}$, and the corrected action is:
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
62	Constraining $\varepsilon$ to $[0.05, 0.2]$ yields stable corrections. We use $\varepsilon{=}0.2$ as the primary setting. The obs\_only variant is robust across all tested bounds ($\varepsilon \in [0.03, \text{uncapped}]$), maintaining 13.5--17.5\% on LIBERO-Object across the tested range ($n{=}1$--$6$ per point). The perdof variant degrades progressively as $\varepsilon$ increases, collapsing from 14\% to 0\% over the same range. The root cause is noisy covariance estimation at $K{=}10$ samples in $d{=}6$ dimensions: per-DOF directional signals are poorly estimated with only 10 samples, harmless when clipped to small magnitude but catastrophic when the bound is loose. Section~\ref{sec:magnitude_results} presents the full sensitivity analysis.
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
79	The computational overhead is $K{=}10$ extra forward passes through the base VLA plus ${\sim}$0.3\,ms for CRM inference. The base VLA is never modified.
80	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "e622a275-b022-4355-b243-227b0fa4531e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves actions from a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the candidate closest to the sample mean, and apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image, language instruction, proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the pipeline.\n\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that generates actions via learned flow matching~\\cite{lipman2023flow}. Each forward pass produces a stochastic action sample, so querying $\\pi_\\theta$ independently $K$ times yields $K$ candidate action chunks. Our goal is to produce a single action more accurate than any individual sample, with no changes to~$\\pi_\\theta$. The method applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Multi-Sample Selection}\n\\label{sec:selection}\n\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts and truncate each to $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for horizon step $h = 1, \\dots, H$. For each step, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and select the sample with the smallest total $L_2$ distance to the mean across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} \\bigl\\|a_h^{(k)} - \\boldsymbol{\\mu}_h\\bigr\\|_2^2.\n  \\label{eq:argmin}\n\\end{equation}\nThis procedure identifies the most representative sample from the action distribution. Unlike the element-wise mean, which blends potentially incompatible action modes and can produce out-of-distribution actions, argmin selection returns an actual sample from the VLA's generative process and preserves within-sample temporal coherence across the $H$ steps. The selection operates independently of the downstream correction module: it is a statistical denoising step that provides the CRM with a higher-quality starting point.\n\n\\subsection{Correction Module (CRM)}\n\\label{sec:crm}\n\nThe CRM is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a bounded residual correction conditioned on the current observation and the selected action itself.\n\n\\paragraph{Architecture.}\nThe CRM consists of three fully connected layers with ReLU activations: $\\mathrm{Linear}(n_{\\mathrm{in}}, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 256) \\to \\mathrm{ReLU} \\to \\mathrm{Linear}(256, 30)$, preceded by input normalization. For the primary obs\\_only variant ($n_{\\mathrm{in}}{=}990$), the input is the concatenation of the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{960}$ from SmolVLA's vision-language encoder and the selected action $a_{\\mathrm{base}} \\in \\mathbb{R}^{30}$ ($H{=}5$ steps $\\times$ $d{=}6$ DOFs); concatenation order is arbitrary for fully connected layers, for a total of 327,198 parameters (${\\sim}$327K). The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound that limits the correction magnitude (Section~\\ref{sec:magnitude}). The CRM never sees individual action candidates: it receives only the already-selected $a_{\\mathrm{base}}$ and predicts a correction toward the expert action.\n\n\\paragraph{Conditioning variants.}\nWe compare three CRM variants that share the same MLP architecture but differ in their input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only} (primary): $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}] \\in \\mathbb{R}^{990}$, 327K parameters. No conformal or uncertainty features.\n  \\item \\textbf{perdof}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, \\mathbf{u}_{\\mathrm{dof}}] \\in \\mathbb{R}^{1030}$, 337K parameters. The 40-dimensional vector $\\mathbf{u}_{\\mathrm{dof}}$ consists of 30 per-DOF standard deviations ($H{\\times}d$), 5 conformal prediction radii~\\cite{angelopoulos2023gentle} (one per horizon step), and 5 log-volume terms derived from the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well} of the $K$ samples.\n  \\item \\textbf{scalar}: $[\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}};\\, u_s] \\in \\mathbb{R}^{991}$, 327K parameters, where $u_s$ is a single scalar uncertainty summary.\n\\end{itemize}\nThe obs\\_only variant is our primary method. Despite the name ``Conformal Residual Module,'' the primary variant does not condition on conformal statistics. The perdof variant conditions on conformal-calibrated uncertainty features~\\cite{braun2025cgs}, but Section~\\ref{sec:ablation} shows that these features fail to improve closed-loop performance at the $K{=}10$ sample budget.\n\n\\paragraph{Training.}\nThe CRM is trained offline on demonstration trajectories from LIBERO~\\cite{liu2023libero} with $L_2$ loss:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2,\n  \\label{eq:loss}\n\\end{equation}\nwhere $\\mathbf{a}_{\\mathrm{expert}}$ is the demonstration action. The training set comprises 26{,}737 precomputed samples from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, apply argmin selection~(\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$, and train the CRM to predict the residual that moves $a_{\\mathrm{base}}$ toward $\\mathbf{a}_{\\mathrm{expert}}$. Data augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and, for variants that receive uncertainty inputs, noise on those features ($\\sigma \\approx 0.006$). Both forms of augmentation improve generalization to the state distribution encountered during closed-loop evaluation, which diverges from the demonstration distribution due to compounding errors~\\cite{ross2011dagger}.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) controls how far the CRM can deviate from the selected action and is critical for stable closed-loop performance.\n\nWithout clipping, the CRM's natural output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, compounding error across the trajectory destroys task performance: the perdof variant achieves 0\\% success on LIBERO-Spatial across three seeds. Each over-corrected action shifts the state distribution away from the CRM's training regime, and subsequent corrections compound the deviation. This failure is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger} but manifests at inference time rather than during data collection.\n% exp_id: eval-acr-spatial-v4-default-r3 (uncapped norm~1.42, perdof 0%, 3 seeds)\n\nConstraining $\\varepsilon$ to $[0.05, 0.2]$ yields stable corrections. We use $\\varepsilon{=}0.2$ as the primary setting. The obs\\_only variant is robust across all tested bounds ($\\varepsilon \\in [0.03, \\text{uncapped}]$), maintaining 13.5--17.5\\% on LIBERO-Object across the tested range ($n{=}1$--$6$ per point). The perdof variant degrades progressively as $\\varepsilon$ increases, collapsing from 14\\% to 0\\% over the same range. The root cause is noisy covariance estimation at $K{=}10$ samples in $d{=}6$ dimensions: per-DOF directional signals are poorly estimated with only 10 samples, harmless when clipped to small magnitude but catastrophic when the bound is loose. Section~\\ref{sec:magnitude_results} presents the full sensitivity analysis.\n% exp_id: magnitude sweep obs_only seeds 42-46, perdof seeds 42-46\n\nThe necessity of magnitude control connects ACR-VLA to the residual policy learning literature. Silver et al.~\\cite{silver2018residual} introduced residual learning with zero-initialization for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} applies learned binary gating to selectively enable residual actions. PLD~\\cite{xiao2026pld} bounds corrections within a fixed range during RL training. ACR-VLA uses fixed $L_2$ norm clipping, the simplest instantiation: a hard constraint that prevents the correction from overwhelming the base policy, with no learned gating or multi-stage pipeline.\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute the sample mean $\\boldsymbol{\\mu}_h$ per horizon step and select $a_{\\mathrm{base}}$ via $L_2$ argmin~(\\ref{eq:argmin}).\n  \\item Extract the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ from the frozen VLA encoder.\n  \\item Compute $\\boldsymbol{\\delta} = \\mathrm{CRM}([\\mathbf{z}_{\\mathrm{obs}};\\, a_{\\mathrm{base}}])$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead is $K{=}10$ extra forward passes through the base VLA plus ${\\sim}$0.3\\,ms for CRM inference. The base VLA is never modified.\n",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 80
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
Now I have all the context. Let me analyze the current related work and understand what needs to change:

1. The current related work has 4 subsections: VLA Robustness, Conformal Prediction in Robotics, Residual Policy Learning, Uncertainty Quantification for VLAs
2. The task requires restructuring to 3 subsections: VLA Robustness, Residual Policy Learning, Inference-Time Compute Scaling
3. "Conformal Prediction in Robotics" needs to be REMOVED as standalone section


4. "Uncertainty Quantification for VLAs" needs to be REMOVED or condensed

I'm also noticing some critical corrections needed in how the method is described. The ACR-VLA selection mechanism is based on L2 distance to the sample mean, not Mahalanobis distance or conformal scoring. The main approach doesn't actually use conformal features—that only appears in an ablation variant that performs worse. I need to be careful not to mischaracterize the method as building on conformal prediction or CGS when the core contribution is really about sample selection combined with learned correction. The language around "conformal" should be toned down since it's not central to what the method does.

Looking at the related work section, I'm catching several inaccuracies that need fixing. Lines 25 and 30 incorrectly describe the selection stage, and line 38 falsely claims Mahalanobis scoring is used. The "Conformal Prediction in Robotics" section is giving too much weight to conformal methods, and the uncertainty quantification section is bloated. I should restructure this with the three required subsections and ground everything in what ACR-VLA actually does: L2-based selection, a lightweight MLP for correction, and no reliance on conformal prediction in the primary variant.

Now I'm organizing the new structure around VLA robustness, residual policy learning, and inference-time scaling. The key positioning is that A2C2 is the closest concurrent work, magnitude control through L2 norm clipping is underexplored, and ACR-VLA uses supervised learning rather than RL for its correction module. I'll keep each section tight and focused on how ACR-VLA relates to these areas.

For the inference-time compute section, I'm pulling in test-time scaling work from LLMs and connecting it to embodied AI, then showing how the K-value curve demonstrates ACR-VLA's approach. I need to weave in conformal prediction briefly when discussing ReconVLA's calibration methods, and I'll be careful to avoid em-dashes and -ing phrase endings while positioning our work rather than surveying the field. I'm reviewing the introduction to make sure my related work section aligns with the key technical details—ACR-VLA's approach of drawing K=10 action samples, selecting the one closest to the mean via L2 distance, then applying a learned residual correction through a small MLP. The correction contributes about 5 percentage points of improvement while selection adds roughly 1 percentage point. I also need to note that observation features alone work best; adding conformal uncertainty features actually hurts performance. And I should capture the difference in how SmolVLA produces diverse samples through flow-matching while OpenVLA's autoregressive approach doesn't generate that same diversity.

Now I'm structuring the related work into subsections covering VLA robustness methods, residual policy learning, and inference-time compute scaling. For the robustness section, I'll contrast training-time approaches like SRPO, RobustVLA, DiG-Flow, and TT-VLA—which all require retraining or per-task RL—against inference-time methods like ReconVLA that use conformal quantile regression, then position A2C2 within that landscape.

Drafting the sections... For magnitude control, I'm using L2 norm clipping with a supervised loss rather than reinforcement learning. On the inference side, I'm looking at how scaling compute at test time helps—similar to best-of-N sampling in language models, but adapted for embodied tasks. The K-value experiments show consistent gains as we increase the number of correction attempts from 1 to 10. I should also weave in conformal prediction briefly when discussing robustness properties. I'm deciding where to place the note about conformal calibration—it fits best in the A2C2 comparison paragraph rather than as a separate sentence. Looking at the references I need to remove, I should be careful not to include citations from the sections being deleted (the Conformal Prediction and Uncertainty Quantification sections). I can mention ReconVLA's conformal calibration briefly since it's already in the inference-time paragraph, but I'll keep the related work section clean and focused without over-including content from removed sections. Now I'm writing out the full related work section. and gradient updates during deployment. These training-time approaches all demand retraining, reward engineering, or task-specific RL—they can't simply be dropped into an existing frozen VLA as a plug-and-play fix.

For inference-time methods, ReconVLA uses conformal quantile regression and Mahalanobis distance for uncertainty calibration and anomaly detection, though it skips learning residual corrections. SC-VLA refines actions online through sparse world imagination paired with residual RL, but still needs task-level training for the correction policy. VLA-Pilot leverages evolutionary diffusion guided by an MLLM verifier for plug-and-play correction, but the 2.41 second overhead per step makes it impractical for real-time control.

A2C2 learns a lightweight correction head that runs at every step to adjust actions within pre-generated chunks, maintaining closed-loop responsiveness, though it applies corrections unconditionally without first selecting a strong starting action or limiting correction magnitude. A2C2 is the closest work to what I'm proposing—both attach a correction module to a frozen VLA without retraining—but the key differences are that ACR-VLA uses a two-stage pipeline with multi-sample selection followed by bounded residual correction rather than direct per-step correction, and it enforces explicit magnitude control through L2 norm clipping, which ablations show is essential.

Now looking at residual policy learning more broadly, the framework augments a base controller with learned additive corrections, and the critical challenge is controlling residual magnitude since unconstrained corrections cause compounding errors and policy collapse. My approach conditions the correction module on the frozen VLA's observation embedding, which proves more robust than alternatives like conditioning on uncertainty features. The clipping threshold ε turns out to be surprisingly critical—performance varies significantly across different task suites, suggesting that magnitude control during inference-time correction is a largely unexplored design space. What really sets ACR-VLA apart from these other approaches is that it doesn't require any RL training, reward functions, or environment interaction; instead, the correction module learns directly from offline demonstrations using supervised L2 loss. Now I'm shifting to consider how inference-time compute scaling relates to this work, drawing parallels to how language models benefit from allocating more computation at test time through techniques like best-of-N sampling with verifiers.

This same principle applies to embodied AI—sampling multiple actions from a stochastic policy mirrors the repeated sampling strategies used in language models. ACR-VLA follows this pattern by drawing 10 samples from the frozen VLA at each control step and selecting the action closest to the sample mean, and the experiments show consistent improvements as K increases from 1 to 5 to 10, mirroring the scaling trends we see in language models.

The main distinction here is that instead of relying on a learned verifier like in language models, ACR-VLA uses a statistical selection criterion based on L2 distance to the mean, then applies a learned correction step—this hybrid approach could become increasingly relevant as multi-sample inference becomes standard practice in VLAs. I'm working through the phrasing to avoid sentence-final -ing constructions. The key revisions are converting participial phrases like "ensuring" and "requiring" into infinitive or prepositional forms—"to ensure" and "with no need for"—to maintain cleaner sentence structure while preserving the meaning. I'm checking the formatting conventions in the original file—it uses `\paragraph{}` for the training-time and inference-time subsections, so I'll apply that same style to the VLA Robustness section while keeping other sections as regular paragraphs. Since the target is around 1 page with three balanced subsections, I need to trim the current draft and remove the extra subsection to hit the page budget. I'm verifying the citations are all included—test-time compute scaling, the K-value monotonic improvement trend, and making sure the section references match what's actually defined in the method file rather than using generic labels. I'm verifying that each subsection properly concludes by connecting back to how ACR-VLA relates to the cited work, and I've confirmed all three sections do this—the VLA Robustness section contrasts with A2C2, Residual Policy Learning distinguishes the supervised approach, and Inference-Time Compute Scaling clarifies the selection versus verification difference. I've also double-checked that I'm using the correct terminology for the selection mechanism (L2 argmin, closest to sample mean) and have positioned A2C2 appropriately as concurrent work with clear distinctions around the two-stage pipeline, magnitude control, and conditioning strategy. Ready to write the final version.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "29265428-4c52-45c2-a9ee-bf60b043bc56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5RuS8ZPVfBnQKk3DD72xt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18353,
      "cache_read_input_tokens": 25707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18353
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

Now I have all the context. Let me write the rewritten Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "987fcdcd-33ad-4a6f-b6c8-d27263377f62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5RuS8ZPVfBnQKk3DD72xt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18353,
      "cache_read_input_tokens": 25707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18353
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

<details open><summary>🔧 Tool call — Write · `toolu_01Xds4sNF5F7M84TnkkeEoh8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.\nAll four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\\,s per control step, prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.\nFirst, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.\nSecond, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nThird, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.\nOur perdof ablation variant additionally conditions on conformal uncertainty features~\\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\\ref{sec:ablation}).\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.\nSubsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.\n\nMagnitude control is the key connection to ACR-VLA.\nSilver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.\nACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nThis suggests that magnitude control in VLA inference-time correction is an underexplored design axis.\nA second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.\n\n\\subsection{Inference-Time Compute Scaling}\n\nTest-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.\nSnell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.\nRoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.\nDA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.\n\nThis paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.\nACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.\nThe K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.\nThe key difference from language model settings is the absence of a learned verifier.\nACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "c3af1a3b-f464-40d0-855e-b4bece4c309e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D5RuS8ZPVfBnQKk3DD72xt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18353,
      "cache_read_input_tokens": 25707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 18353
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

_source line 18 · 2026-05-18T10:22:54.075Z_

<details><summary>↩ Tool result · `toolu_01Xds4sNF5F7M84TnkkeEoh8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "c2cbf063-b126-48de-bd2e-44a9dbe99547",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.\nAll four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\\,s per control step, prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.\nFirst, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.\nSecond, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nThird, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.\nOur perdof ablation variant additionally conditions on conformal uncertainty features~\\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\\ref{sec:ablation}).\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.\nSubsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.\n\nMagnitude control is the key connection to ACR-VLA.\nSilver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.\nACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nThis suggests that magnitude control in VLA inference-time correction is an underexplored design axis.\nA second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.\n\n\\subsection{Inference-Time Compute Scaling}\n\nTest-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.\nSnell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.\nRoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.\nDA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.\n\nThis paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.\nACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.\nThe K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.\nThe key difference from language model settings is the absence of a learned verifier.\nACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 62,
        "newStart": 5,
        "newLines": 48,
        "lines": [
          " Methods for improving VLA robustness divide into training-time and inference-time approaches.",
          " ",
          " \\paragraph{Training-time methods.}",
          "-RobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.",
          "-SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.",
          "-DiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.",
          "-TT-VLA~\\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.",
          "-A shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.",
          "+SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.",
          "+RobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.",
          "+DiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.",
          "+TT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.",
          "+All four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.",
          " ",
          " \\paragraph{Inference-time methods.}",
          "-ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.",
          "-SC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.",
          "-VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\\,s per control step---prohibitive for real-time manipulation.",
          "-A2C2~\\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.",
          "+ReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.",
          "+SC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.",
          "+VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\\,s per control step, prohibitive for real-time manipulation.",
          "+A2C2~\\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.",
          " ",
          "-A2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy.",
          "-The key architectural difference is that ACR-VLA operates as a two-stage pipeline---multi-sample conformal selection followed by bounded residual correction---whereas A2C2 applies per-step correction directly to the base policy's action chunks without a selection stage.",
          "-ACR-VLA additionally enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).",
          "-Selection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.",
          "-Correction alone lacks a mechanism to identify a good starting point.",
          "-ACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.",
          "+A2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.",
          "+First, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.",
          "+Second, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).",
          "+Third, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.",
          "+Our perdof ablation variant additionally conditions on conformal uncertainty features~\\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\\ref{sec:ablation}).",
          " ",
          "-\\subsection{Conformal Prediction in Robotics}",
          "-",
          "-Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\\cite{angelopoulos2023gentle}.",
          "-For multivariate outputs, Braun et al.~\\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.",
          "-",
          "-In robotics, CP has been applied to several safety-critical settings.",
          "-Conformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.",
          "-CP-in-the-Loop~\\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.",
          "-ACP+CBF~\\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.",
          "-A common pattern across these methods is that CP serves as a \\emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.",
          "-",
          "-ACR-VLA uses Mahalanobis nonconformity scores derived from shrinkage covariance estimates in its selection stage, but does \\emph{not} claim formal coverage guarantees for the corrected output.",
          "-CP serves here as a scoring mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure is available as conditioning features for the correction module (though our ablations find that observation features alone suffice; Section~\\ref{sec:ablation}).",
          "-The downstream correction module produces a refined action whose relationship to the original conformal region is no longer governed by coverage theory.",
          "-",
          " \\subsection{Residual Policy Learning}",
          " ",
          " Residual policy learning augments a base controller with a learned additive correction.",
          "-Silver et al.~\\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization to ensure the learned residual starts from the base policy's behavior and gradually improves upon it.",
          "-Subsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.",
          "-TRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to decide whether to apply a sim-to-real residual, demonstrating that ungated correction causes model collapse.",
          "+Silver et al.~\\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.",
          "+Subsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.",
          "+TRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.",
          " PLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.",
          "-DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade after application.",
          "+DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.",
          " ",
          "-Magnitude control is the key connection to ACR-VLA: Silver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, DRC uses exponential decay after correction events.",
          "-ACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).",
          "-We view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.",
          "-A second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.",
          "+Magnitude control is the key connection to ACR-VLA.",
          "+Silver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.",
          "+ACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).",
          "+This suggests that magnitude control in VLA inference-time correction is an underexplored design axis.",
          "+A second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.",
          " ",
          "-\\subsection{Uncertainty Quantification for VLAs}",
          "+\\subsection{Inference-Time Compute Scaling}",
          " ",
          "-Recent work has developed UQ methods tailored to VLA architectures.",
          "-DiU~\\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.",
          "-SAFE~\\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering intervention when anomalous states are detected.",
          "-Zollo and Zemel~\\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.",
          "+Test-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.",
          "+Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.",
          "+RoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.",
          "+DA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.",
          " ",
          "-ACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.",
          "-The multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.",
          "-Functionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\\cite{zollo2025vla_calibration} targets confidence reliability.",
          "-Our ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.",
          "\\ No newline at end of file",
          "+This paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.",
          "+ACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.",
          "+The K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.",
          "+The key difference from language model settings is the absence of a learned verifier.",
          "+ACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common."
        ]
      }
    ],
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization and smoothness regularization to stabilize action predictions under observation noise and action perturbations.\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as references to shape rewards for failed trajectories via latent world model representations.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control, without modifying the flow-matching trajectory.\nTT-VLA~\\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.\nA shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and uses squared Mahalanobis distance for out-of-distribution detection, enabling uncertainty-guided action selection and proactive failure detection without retraining.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\\,s per control step---prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that runs at every control step to correct each action within a pre-generated chunk, restoring closed-loop responsiveness; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy.\nThe key architectural difference is that ACR-VLA operates as a two-stage pipeline---multi-sample conformal selection followed by bounded residual correction---whereas A2C2 applies per-step correction directly to the base policy's action chunks without a selection stage.\nACR-VLA additionally enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nSelection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.\nCorrection alone lacks a mechanism to identify a good starting point.\nACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.\n\n\\subsection{Conformal Prediction in Robotics}\n\nConformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\\cite{angelopoulos2023gentle}.\nFor multivariate outputs, Braun et al.~\\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.\n\nIn robotics, CP has been applied to several safety-critical settings.\nConformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.\nCP-in-the-Loop~\\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.\nACP+CBF~\\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.\nA common pattern across these methods is that CP serves as a \\emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.\n\nACR-VLA uses Mahalanobis nonconformity scores derived from shrinkage covariance estimates in its selection stage, but does \\emph{not} claim formal coverage guarantees for the corrected output.\nCP serves here as a scoring mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure is available as conditioning features for the correction module (though our ablations find that observation features alone suffice; Section~\\ref{sec:ablation}).\nThe downstream correction module produces a refined action whose relationship to the original conformal region is no longer governed by coverage theory.\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization to ensure the learned residual starts from the base policy's behavior and gradually improves upon it.\nSubsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to decide whether to apply a sim-to-real residual, demonstrating that ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade after application.\n\nMagnitude control is the key connection to ACR-VLA: Silver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, DRC uses exponential decay after correction events.\nACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nWe view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.\nA second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.\n\n\\subsection{Uncertainty Quantification for VLAs}\n\nRecent work has developed UQ methods tailored to VLA architectures.\nDiU~\\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.\nSAFE~\\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering intervention when anomalous states are detected.\nZollo and Zemel~\\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.\n\nACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.\nThe multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.\nFunctionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\\cite{zollo2025vla_calibration} targets confidence reliability.\nOur ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 19_

Now let me verify the file is clean of em-dashes, explanatory en-dashes, and -ing phrase endings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "27a93ffb-ae62-4096-8518-499074041302",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132eDSnTPH5P6ni51Ru3EWN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7649,
      "cache_read_input_tokens": 44060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7649
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

<details open><summary>🔧 Tool call — Bash · `toolu_01GRoTTec6xwgPG7HRsgVedL`</summary>

```json
{
  "command": "grep -n \"—\\|---\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "description": "Check for em-dashes in the new file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "fc6f4382-ce01-437d-9884-bdda351ce190",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132eDSnTPH5P6ni51Ru3EWN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7649,
      "cache_read_input_tokens": 44060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7649
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

_source line 21 · 2026-05-18T10:22:58.875Z_

<details><summary>↩ Tool result · `toolu_01GRoTTec6xwgPG7HRsgVedL`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "eb525985-34d4-488f-a50a-47b8d12bde1d",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_015gppFsps9JbRwo4T5KTmR2`</summary>

```json
{
  "command": "grep -n \" -- \" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "description": "Check for explanatory en-dashes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "7c277ba6-6a98-4652-b63d-8ca6b3632de1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132eDSnTPH5P6ni51Ru3EWN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7649,
      "cache_read_input_tokens": 44060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7649
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

_source line 23 · 2026-05-18T10:22:59.691Z_

<details><summary>↩ Tool result · `toolu_015gppFsps9JbRwo4T5KTmR2`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "24017989-e3c2-41dc-bee8-79d3086f2d86",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ai1UZxckXMJM9D1hwSAqD5`</summary>

```json
{
  "command": "grep -nE \"ing[.,;]?\\s*$\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "description": "Check for -ing phrase endings at end of lines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "26c011ff-a842-4047-98fe-3b993779174d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132eDSnTPH5P6ni51Ru3EWN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7649,
      "cache_read_input_tokens": 44060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7649
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

_source line 25 · 2026-05-18T10:23:01.109Z_

<details><summary>↩ Tool result · `toolu_01Ai1UZxckXMJM9D1hwSAqD5`</summary>

```text
43:Test-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.
44:Snell et al.~\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "8a99440e-c19b-4128-80ae-98fce4eb72f3",
  "tool_use_result": {
    "stdout": "43:Test-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.\n44:Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.",
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

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_019AYPtzzX9H4NeoWoL1ZSvE`</summary>

```json
{
  "command": "grep -niE \"(delve|leverage|utilize|facilitate|myriad|plethora|paradigm shift|in the realm|notably|it is worth noting)\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "description": "Check for AI-style word blacklist"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "4b9b0932-6726-49bd-b0a3-4eb5de9918e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0132eDSnTPH5P6ni51Ru3EWN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7649,
      "cache_read_input_tokens": 44060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7649
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

_source line 27 · 2026-05-18T10:23:02.614Z_

<details><summary>↩ Tool result · `toolu_019AYPtzzX9H4NeoWoL1ZSvE`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "d39654e1-8c56-4750-9ae7-58c07128f8e7",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
The grep found two lines ending with -ing patterns:
- Line 43: "for improving language model performance without additional training." - "training" here is a noun (not a participial phrase like "demonstrating the effectiveness"). This is fine.
- Line 44: "establishing a compute-optimal framework for test-time scaling." - "establishing" IS a participial phrase ending. I need to fix this.

Also "scaling" at the end of line 44 is a noun ("test-time scaling"), but "establishing a compute-optimal framework" is a participial phrase. Let me rephrase.

Let me fix line 44. Instead of "...can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling", I could write: "...can match or exceed the gains from larger models. Their compute-optimal framework provides a principled basis for test-time scaling."


Or I could use "and establish" to make it a coordinated verb phrase instead. That's cleaner and avoids the participial construction altogether.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "b551b1b0-1b4f-480e-a58b-df3fade2de10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rhq6N3P3WvWTkLPpiNZuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 51709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 833
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

_source line 29_

Line 44 has a ", establishing..." participial phrase ending. Let me fix it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "4afa8534-59fb-4a0e-837f-befa011657c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rhq6N3P3WvWTkLPpiNZuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 51709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 833
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

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01HCKX344B1tPdjJ6R72EjpN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "old_string": "Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.",
  "new_string": "Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models and establish a compute-optimal framework for test-time scaling."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "c1b68ed4-f226-43fe-aef4-97d102695f23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Rhq6N3P3WvWTkLPpiNZuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 51709,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 833
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

_source line 31 · 2026-05-18T10:23:14.538Z_

<details><summary>↩ Tool result · `toolu_01HCKX344B1tPdjJ6R72EjpN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "1cb470e8-8596-40ae-891d-0983ead34dbc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "oldString": "Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.",
    "newString": "Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models and establish a compute-optimal framework for test-time scaling.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.\nAll four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\\,s per control step, prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.\nFirst, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.\nSecond, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nThird, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.\nOur perdof ablation variant additionally conditions on conformal uncertainty features~\\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\\ref{sec:ablation}).\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.\nSubsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.\n\nMagnitude control is the key connection to ACR-VLA.\nSilver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.\nACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nThis suggests that magnitude control in VLA inference-time correction is an underexplored design axis.\nA second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.\n\n\\subsection{Inference-Time Compute Scaling}\n\nTest-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.\nSnell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.\nRoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.\nDA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.\n\nThis paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.\nACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.\nThe K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.\nThe key difference from language model settings is the absence of a learned verifier.\nACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common.\n",
    "structuredPatch": [
      {
        "oldStart": 41,
        "oldLines": 7,
        "newStart": 41,
        "newLines": 7,
        "lines": [
          " \\subsection{Inference-Time Compute Scaling}",
          " ",
          " Test-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.",
          "-Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models, establishing a compute-optimal framework for test-time scaling.",
          "+Snell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models and establish a compute-optimal framework for test-time scaling.",
          " RoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.",
          " DA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 32_

Let me also check for any remaining -ing participial phrase patterns (comma + -ing).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "a0283429-a991-40cc-a641-30960197114e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVd3Gf81DzBbvBbffpsY2d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 52542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 751
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

_source line 33_

<details open><summary>🔧 Tool call — Bash · `toolu_01EemURbmTnMZLXdnz12Zdiy`</summary>

```json
{
  "command": "grep -n \", [a-z]*ing \" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex | grep -v \"\\\\\\\\cite\\|clipping\\|conditioning\\|matching\\|missing\\|existing\\|gating\\|string\"",
  "description": "Check for comma + -ing participial phrase patterns"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "5c6bace2-c7ca-49d4-bbc6-6d40d800399a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MVd3Gf81DzBbvBbffpsY2d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 751,
      "cache_read_input_tokens": 52542,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 751
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

_source line 34 · 2026-05-18T10:23:19.096Z_

<details><summary>↩ Tool result · `toolu_01EemURbmTnMZLXdnz12Zdiy`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "73630a7b-21c8-45b2-9ac0-80fa0c4c86c8",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Grep · `toolu_01DkQC9j5LkdqPoBMiKAJk97`</summary>

```json
{
  "pattern": ", [a-z]+ing ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "00b2c8cf-7b5e-4996-a74a-5d1a257116c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXkRWu9WnYGFppQpeLfp9n",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 53293,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 201
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

_source line 36 · 2026-05-18T10:23:21.982Z_

<details><summary>↩ Tool result · `toolu_01DkQC9j5LkdqPoBMiKAJk97`</summary>

```text
8:SRPO~\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.
33:DRC~\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "0f7adb80-009d-4624-84d0-53aca80eeb6e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "8:SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.\n33:DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.",
    "numLines": 2
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
Line 8: "fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories." - This is a participial phrase. Let me rephrase.

Line 33: "applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time." - This is also a participial phrase ending. Let me rephrase.

For line 8: "SRPO~\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories."

For line 33: "DRC~\cite{pan2025drc} applies exponential decay to each expert correction event so that corrective signals persist and fade over time."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "7a242e8e-7f8c-4b95-abb6-2e69928f8529",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017PRyAmXMCAhcTwLFSCvNiM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 225,
      "cache_read_input_tokens": 53494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 225
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

_source line 38_

Two more participial phrase patterns to fix.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "b43b4b05-a00f-4e95-bec9-f30549cacbe9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017PRyAmXMCAhcTwLFSCvNiM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 225,
      "cache_read_input_tokens": 53494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 225
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

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_01ASWYzpAuvwCLLvStsEBryC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "old_string": "SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.",
  "new_string": "SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "5ea0cfc0-cd86-4248-a16f-3d5d325d547f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017PRyAmXMCAhcTwLFSCvNiM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 225,
      "cache_read_input_tokens": 53494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 225
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

_source line 40 · 2026-05-18T10:23:27.430Z_

<details><summary>↩ Tool result · `toolu_01ASWYzpAuvwCLLvStsEBryC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "8c42e7fc-cd7f-4d30-8611-74a21512d826",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "oldString": "SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.",
    "newString": "SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.\nAll four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\\,s per control step, prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.\nFirst, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.\nSecond, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nThird, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.\nOur perdof ablation variant additionally conditions on conformal uncertainty features~\\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\\ref{sec:ablation}).\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.\nSubsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.\n\nMagnitude control is the key connection to ACR-VLA.\nSilver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.\nACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nThis suggests that magnitude control in VLA inference-time correction is an underexplored design axis.\nA second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.\n\n\\subsection{Inference-Time Compute Scaling}\n\nTest-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.\nSnell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models and establish a compute-optimal framework for test-time scaling.\nRoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.\nDA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.\n\nThis paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.\nACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.\nThe K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.\nThe key difference from language model settings is the absence of a learned verifier.\nACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common.\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 7,
        "newStart": 5,
        "newLines": 7,
        "lines": [
          " Methods for improving VLA robustness divide into training-time and inference-time approaches.",
          " ",
          " \\paragraph{Training-time methods.}",
          "-SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own successful rollouts as reward references for failed trajectories.",
          "+SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories.",
          " RobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.",
          " DiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.",
          " TT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_019AnQ5NfbkwQahfuRGBH4iY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "old_string": "DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.",
  "new_string": "DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event so that corrective signals persist and fade over time."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "47d02396-b987-4ebc-9a1c-0cea377854c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MwZCZJLkccY46tJXbk4wnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 483,
      "cache_read_input_tokens": 53719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 483
      },
      "output_tokens": 72,
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

_source line 42 · 2026-05-18T10:23:30.667Z_

<details><summary>↩ Tool result · `toolu_019AnQ5NfbkwQahfuRGBH4iY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "1bf133fd-1952-4cf7-a59f-0a322430ea98",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
    "oldString": "DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.",
    "newString": "DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event so that corrective signals persist and fade over time.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.\nAll four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\\,s per control step, prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.\nFirst, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.\nSecond, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nThird, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.\nOur perdof ablation variant additionally conditions on conformal uncertainty features~\\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\\ref{sec:ablation}).\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.\nSubsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.\n\nMagnitude control is the key connection to ACR-VLA.\nSilver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.\nACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nThis suggests that magnitude control in VLA inference-time correction is an underexplored design axis.\nA second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.\n\n\\subsection{Inference-Time Compute Scaling}\n\nTest-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.\nSnell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models and establish a compute-optimal framework for test-time scaling.\nRoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.\nDA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.\n\nThis paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.\nACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.\nThe K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.\nThe key difference from language model settings is the absence of a learned verifier.\nACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common.\n",
    "structuredPatch": [
      {
        "oldStart": 30,
        "oldLines": 7,
        "newStart": 30,
        "newLines": 7,
        "lines": [
          " Subsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.",
          " TRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.",
          " PLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.",
          "-DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over time.",
          "+DRC~\\cite{pan2025drc} applies exponential decay to each expert correction event so that corrective signals persist and fade over time.",
          " ",
          " Magnitude control is the key connection to ACR-VLA.",
          " Silver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 43_

Now let me verify the final file and check for any remaining issues.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "bde82bfb-0c33-4f9c-acc6-aec2492944ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFYLGgHst6xVQVWvhTRZiB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 54202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 274
      },
      "output_tokens": 6,
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

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01Fcod56uMR1AtVv3ehM47qK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "b2539a91-fb45-430f-8f13-6243011480f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WFYLGgHst6xVQVWvhTRZiB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 274,
      "cache_read_input_tokens": 54202,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 274
      },
      "output_tokens": 6,
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

_source line 45 · 2026-05-18T10:23:33.692Z_

<details><summary>↩ Tool result · `toolu_01Fcod56uMR1AtVv3ehM47qK`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	Methods for improving VLA robustness divide into training-time and inference-time approaches.
6	
7	\paragraph{Training-time methods.}
8	SRPO~\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories.
9	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.
10	DiG-Flow~\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.
11	TT-VLA~\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.
12	All four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.
13	
14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.
17	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\,s per control step, prohibitive for real-time manipulation.
18	A2C2~\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.
19	
20	A2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.
21	First, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.
22	Second, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\ref{sec:magnitude_results}).
23	Third, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.
24	Our perdof ablation variant additionally conditions on conformal uncertainty features~\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\ref{sec:ablation}).
25	
26	\subsection{Residual Policy Learning}
27	
28	Residual policy learning augments a base controller with a learned additive correction.
29	Silver et al.~\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.
30	Subsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.
31	TRANSIC~\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.
32	PLD~\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\xi, \xi]$) via off-policy RL, then distills improved trajectories back into the base model.
33	DRC~\cite{pan2025drc} applies exponential decay to each expert correction event so that corrective signals persist and fade over time.
34	
35	Magnitude control is the key connection to ACR-VLA.
36	Silver et al.\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.
37	ACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\ref{sec:experiments}).
38	This suggests that magnitude control in VLA inference-time correction is an underexplored design axis.
39	A second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.
40	
41	\subsection{Inference-Time Compute Scaling}
42	
43	Test-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.
44	Snell et al.~\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models and establish a compute-optimal framework for test-time scaling.
45	RoVer~\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.
46	DA-SIP~\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.
47	
48	This paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.
49	ACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.
50	The K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.
51	The key difference from language model settings is the absence of a learned verifier.
52	ACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common.
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "b1b7851b-ade7-4292-aa71-06a0eb822915",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning and uses the policy's own successful rollouts as reward references for failed trajectories.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian and smoothness regularization to stabilize predictions under observation noise.\nDiG-Flow~\\cite{digflow2025} uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance representation-level control.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time through RL with progress rewards, but requires per-task reward design and gradient updates during deployment.\nAll four methods require retraining, reward engineering, or per-task RL, and cannot serve as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} applies conformal quantile regression to calibrate per-action uncertainty bounds and Mahalanobis distance for out-of-distribution detection, but does not learn corrective residuals.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, which still requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier at the cost of 2.41\\,s per control step, prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns a lightweight correction head that corrects each action within a pre-generated chunk at every control step to restore closed-loop responsiveness. It applies correction unconditionally, without first selecting a high-quality starting action or controlling correction magnitude.\n\nA2C2 is the closest concurrent work to ACR-VLA: both attach a lightweight correction module to a frozen VLA without retraining the base policy. The key differences are threefold.\nFirst, ACR-VLA operates as a two-stage pipeline, where multi-sample selection (choosing the candidate closest to the sample mean by $L_2$ distance) precedes bounded residual correction, whereas A2C2 applies per-step correction directly without a selection stage.\nSecond, ACR-VLA enforces explicit magnitude control via $L_2$ norm clipping, which our ablations show is critical for preventing compounding correction errors (Section~\\ref{sec:magnitude_results}).\nThird, ACR-VLA conditions the correction module on the frozen VLA's observation embedding rather than temporal action features.\nOur perdof ablation variant additionally conditions on conformal uncertainty features~\\cite{braun2025cgs,angelopoulos2023gentle}, but observation-only conditioning proves sufficient and more robust across magnitude bounds (Section~\\ref{sec:ablation}).\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers with zero-initialization to ensure the learned residual starts from the base policy's behavior.\nSubsequent work has focused on controlling residual magnitude, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate conditioned on the current state to selectively enable sim-to-real residual actions; ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} freezes the VLA backbone and trains lightweight residual actors with bounded corrections ($[-\\xi, \\xi]$) via off-policy RL, then distills improved trajectories back into the base model.\nDRC~\\cite{pan2025drc} applies exponential decay to each expert correction event so that corrective signals persist and fade over time.\n\nMagnitude control is the key connection to ACR-VLA.\nSilver et al.\\ use zero-initialization, TRANSIC uses binary gating, PLD uses fixed action bounds, and DRC uses exponential decay.\nACR-VLA uses fixed $L_2$ norm clipping, the simplest possible scheme, yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nThis suggests that magnitude control in VLA inference-time correction is an underexplored design axis.\nA second distinction separates ACR-VLA from all four methods: each requires RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, with no need for reward design or environment access.\n\n\\subsection{Inference-Time Compute Scaling}\n\nTest-time compute scaling has emerged as a powerful axis for improving language model performance without additional training.\nSnell et al.~\\cite{snell2024scaling} show that allocating more compute at inference time through best-of-N sampling with a verifier can match or exceed the gains from larger models and establish a compute-optimal framework for test-time scaling.\nRoVer~\\cite{dai2025rover} extends this to reward-free settings by using self-verification to select among multiple candidate responses without an explicit reward model.\nDA-SIP~\\cite{chun2025dasip} introduces decision-aware sample importance weighting that connects optimal sample selection to downstream task loss rather than generic quality metrics.\n\nThis paradigm is beginning to transfer to embodied AI, where drawing multiple action samples from a stochastic policy is analogous to repeated sampling from a language model.\nACR-VLA instantiates this connection: at each control step, it draws $K{=}10$ samples from the frozen VLA and selects the candidate closest to the sample mean.\nThe K-value curve shows monotonic improvement from $K{=}1$ to $K{=}5$ to $K{=}10$ (Section~\\ref{sec:experiments}), consistent with the scaling behavior observed in language model test-time compute.\nThe key difference from language model settings is the absence of a learned verifier.\nACR-VLA replaces the verifier with a statistical selection criterion ($L_2$ argmin) followed by a learned correction step, a design point that may prove relevant as multi-sample VLA inference becomes more common.\n",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017h4KAiBCS3jrS4ErKcQUHJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__send_progress",
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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "6b34bfec-3d8c-4c0e-a525-977783cd25a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoAAnEiGJAc8HoLUgsdjbC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1882,
      "cache_read_input_tokens": 54476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1882
      },
      "output_tokens": 44,
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

_source line 47 · 2026-05-18T10:23:38.387Z_

<details><summary>↩ Tool result · `toolu_017h4KAiBCS3jrS4ErKcQUHJ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__send_progress"
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
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "8e7a7551-f861-4b66-8ec1-4008a137e3a6",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__send_progress"
    ],
    "query": "select:mcp__agent-ml-research__send_progress",
    "total_deferred_tools": 50
  }
}
```

</details>

---

### Assistant

_source line 48_

File written. Summary of changes:

**Structure**: 4 subsections → 3 subsections
- **VLA Robustness** (~0.4 page): Training-time (SRPO, RobustVLA, DiG-Flow, TT-VLA) and inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2) methods, with A2C2 positioned as closest concurrent work via threefold comparison
- **Residual Policy Learning** (~0.3 page): Silver 2018, TRANSIC, PLD, DRC; magnitude control as underexplored axis; ACR-VLA's supervised L2 loss vs RL distinction
- **Inference-Time Compute Scaling** (~0.3 page): Snell et al., RoVer, DA-SIP; ACR-VLA's K-value curve as embodied AI instantiation

**D058 corrections applied**:
- All references to "Mahalanobis scoring" and "conformal selection" removed from ACR-VLA's selection description → replaced with "L2 argmin" / "candidate closest to the sample mean by L2 distance"
- Removed "Conformal Prediction in Robotics" standalone section entirely
- Removed "Uncertainty Quantification for VLAs" standalone section entirely
- Conformal features mentioned only once, as perdof ablation (line 24)
- No claim that ACR-VLA "builds upon" CGS

**Style compliance**: zero em-dashes, zero explanatory en-dashes, zero -ing participial phrase endings, zero blacklisted AI words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "uuid": "702e7f45-1e90-4242-8271-555599f548d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QCQKe59JtjSBvZEC6AdpJM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 56358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
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

### Task result

_source line 49_

File written. Summary of changes:

**Structure**: 4 subsections → 3 subsections
- **VLA Robustness** (~0.4 page): Training-time (SRPO, RobustVLA, DiG-Flow, TT-VLA) and inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2) methods, with A2C2 positioned as closest concurrent work via threefold comparison
- **Residual Policy Learning** (~0.3 page): Silver 2018, TRANSIC, PLD, DRC; magnitude control as underexplored axis; ACR-VLA's supervised L2 loss vs RL distinction
- **Inference-Time Compute Scaling** (~0.3 page): Snell et al., RoVer, DA-SIP; ACR-VLA's K-value curve as embodied AI instantiation

**D058 corrections applied**:
- All references to "Mahalanobis scoring" and "conformal selection" removed from ACR-VLA's selection description → replaced with "L2 argmin" / "candidate closest to the sample mean by L2 distance"
- Removed "Conformal Prediction in Robotics" standalone section entirely
- Removed "Uncertainty Quantification for VLAs" standalone section entirely
- Conformal features mentioned only once, as perdof ablation (line 24)
- No claim that ACR-VLA "builds upon" CGS

**Style compliance**: zero em-dashes, zero explanatory en-dashes, zero -ing participial phrase endings, zero blacklisted AI words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 204857,
  "duration_api_ms": 205993,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "9e15174f-1edf-4e89-b935-74637ed5cdef",
  "total_cost_usd": 0.8053045000000001,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 44800,
    "cache_read_input_tokens": 511401,
    "output_tokens": 10696,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44800,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 387,
        "cache_read_input_tokens": 56358,
        "cache_creation_input_tokens": 283,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 283
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2024,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021290000000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 10696,
      "cacheReadInputTokens": 511401,
      "cacheCreationInputTokens": 44800,
      "webSearchRequests": 0,
      "costUSD": 0.8031755,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b4b41dd3-59f3-4c22-aefa-5cf417982a4f"
}
```

</details>

---
