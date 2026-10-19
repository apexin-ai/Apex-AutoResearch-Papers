# paper writing experiments

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260515T192214.log`
- **Structured JSON:** [`9618e94f28b3619d340e.json`](../../sessions/96/9618e94f28b3619d340e.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
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
  "uuid": "8386b6d2-ba0b-48c6-b7ca-cf7a19583edc",
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
  "uuid": "f4c649b3-b0d8-444e-a0fe-e8a817b8dfdd",
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d"
}
```

---

### Assistant

_source line 4_

I'll start by reading the LaTeX writing skill and checking the existing paper structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "7fdcc24e-2385-41a7-9dce-1056bcf3cc2f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEg9nHvSBkk5RCZbPPY8td",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13698,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13698
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

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01AufFY1grhcfBxFHFDhjFXW`</summary>

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
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "0d65fbeb-8c99-484d-9991-be0d621cefc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEg9nHvSBkk5RCZbPPY8td",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13698,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13698
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

_source line 6 · 2026-05-15T19:22:27.803Z_

<details><summary>↩ Tool result · `toolu_01AufFY1grhcfBxFHFDhjFXW`</summary>

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
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "6b0381b7-0e0d-42ea-ba1e-8b54f51fdef1",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01LD4Ez4Y7JDMMVh3CHrfKPF`</summary>

```json
{
  "pattern": "**/*.tex",
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
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "87987822-cd3c-4189-a627-f95e3ee88ef4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XEg9nHvSBkk5RCZbPPY8td",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13698,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13698
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

_source line 8 · 2026-05-15T19:22:28.515Z_

<details><summary>↩ Tool result · `toolu_01LD4Ez4Y7JDMMVh3CHrfKPF`</summary>

```text
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "c2b63b28-fc2b-4de6-b8b1-3e76fa9205f4",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work_9c2927.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/introduction_c83872.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/method_section_draft.tex",
      "artifacts/_project/paper/experiments_c64a8c.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/method_fb526b.tex",
      "artifacts/_project/paper/method.tex"
    ],
    "durationMs": 12,
    "numFiles": 9,
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
Let me read the existing experiments.tex and the method.tex to understand the notation and style used.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "003f0ea9-e619-42ee-bef6-ac6499051807",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNf2uYoNKeoajxzAvw6J9v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5790,
      "cache_read_input_tokens": 25539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5790
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

Let me check the existing method section and experiments file for notation and style consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "200bb465-edd8-4157-88be-8a2b19f30f88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNf2uYoNKeoajxzAvw6J9v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5790,
      "cache_read_input_tokens": 25539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5790
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

<details open><summary>🔧 Tool call — Read · `toolu_01PXALJSyZ6Je66uB5UgYSvE`</summary>

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
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "bdc473a9-3a88-4fe1-b7e4-ef4b3532c8c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNf2uYoNKeoajxzAvw6J9v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5790,
      "cache_read_input_tokens": 25539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5790
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

_source line 12 · 2026-05-15T19:22:33.837Z_

<details><summary>↩ Tool result · `toolu_01PXALJSyZ6Je66uB5UgYSvE`</summary>

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
42	This is a simplified selection baseline inspired by the conformal selection frontend of ReconVLA~\cite{chen2026reconvla}, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring to isolate the effect of the downstream correction module. The selected $a_{\mathrm{base}} \in \mathbb{R}^{d \times H}$ is the starting point for residual correction.
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
86	The necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\cite{silver2018residual} introduced bounded residual corrections for combining learned and classical controllers. TRANSIC~\cite{jiang2024transic} uses learned binary gating to selectively apply residual actions across different task phases. PLD~\cite{xiao2026pld} schedules magnitude bounds during training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no scheduling, just a hard constraint that prevents the correction from overwhelming the base policy.
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
103	The computational overhead consists of $K{=}10$ extra forward passes through the base VLA (shared with any multi-sample selection method such as ReconVLA~\cite{chen2026reconvla}) plus ${\sim}$3\,ms for CRM inference. The base VLA is never modified.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "89b969f6-3a77-4668-8c1d-b7259b7505a3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis is a simplified selection baseline inspired by the conformal selection frontend of ReconVLA~\\cite{chen2026reconvla}, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring to isolate the effect of the downstream correction module. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 3-layer MLP with input normalization (input$\\to$256$\\to$256$\\to$30; 329K parameters for the primary obs\\_only variant).\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.\n\n\\paragraph{Small corrections are effective.}\nConstraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.\n\n\\paragraph{Connection to residual policy learning.}\nThe necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced bounded residual corrections for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating to selectively apply residual actions across different task phases. PLD~\\cite{xiao2026pld} schedules magnitude bounds during training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no scheduling, just a hard constraint that prevents the correction from overwhelming the base policy.\n\n\\paragraph{Differential sensitivity across CRM variants.}\nObservation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.\n  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).\n  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead consists of $K{=}10$ extra forward passes through the base VLA (shared with any multi-sample selection method such as ReconVLA~\\cite{chen2026reconvla}) plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_012M7mYGwWuk1fjJQmqqnptE`</summary>

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
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "d0d28c0e-db97-4d17-9121-c2c051834262",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BNf2uYoNKeoajxzAvw6J9v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5790,
      "cache_read_input_tokens": 25539,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5790
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

_source line 14 · 2026-05-15T19:22:34.236Z_

<details><summary>↩ Tool result · `toolu_012M7mYGwWuk1fjJQmqqnptE`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate ACR-VLA on two LIBERO task suites to test three claims:
5	(i)~per-DOF conformal conditioning improves task success over scalar and no-uncertainty baselines;
6	(ii)~each component (CGS features, ACI+COC calibration, CRM architecture) contributes to the overall gain;
7	(iii)~the improvement concentrates on tasks where the base VLA exhibits anisotropic uncertainty.
8	
9	
10	\subsection{Experimental Setup}
11	\label{sec:exp_setup}
12	
13	\paragraph{Benchmarks.}
14	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
15	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object placement) and \textbf{LIBERO-Object} (10 tasks requiring generalization across object instances).
16	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite.
17	Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that predicts action chunks of length 50.
21	We use the community-fine-tuned checkpoint \texttt{lerobot/smolvla\_libero}.
22	The policy receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
23	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper.
24	The gripper dimension is handled outside the conformal pipeline via direct thresholding.
25	
26	\paragraph{CGS configuration.}
27	At each control step, we draw $K{=}10$ action chunks via independent flow-matching rollouts and retain the first $H{=}5$ steps of each chunk (Section~\ref{sec:cgs}).
28	The Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well} is computed per horizon step, yielding the 40D CGS feature: 30D per-DOF standard deviations ($d{\times}H = 6{\times}5$), 5D conformal radii, and 5D log-volume terms.
29	
30	\paragraph{CRM architecture and training.}
31	The Conformal Refinement Module is a 2-layer MLP with hidden dimension 256 (${\sim}$337K parameters).
32	Its input concatenates the frozen observation embedding (${\sim}$960D), the 40D CGS feature, and the 30D mean action, totaling ${\sim}$1{,}030D.
33	The output is a 30D residual correction ($d{\times}H$).
34	We train CRM on 26{,}737 precomputed samples (12{,}167 from LIBERO-Spatial + 14{,}570 from LIBERO-Object), constructed from 10 demonstrations per task across all 20 tasks.
35	For each demonstration step, we run $K{=}10$ SmolVLA forward passes and extract CGS features.
36	Training data is augmented with additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and uncertainty features ($\sigma \approx 0.006$), simulating noisy action predictions while preserving clean regression targets.
37	Optimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs.
38	All experiments use seed 42.
39	
40	\paragraph{ACI+COC configuration.}
41	The target miscoverage rate is $\alpha_{\mathrm{target}}{=}0.1$.
42	The ACI learning rate $\gamma$ and exponential decay $\rho$ for within-episode weighting are hyperparameters.
43	% [TODO: specify selection method once finalized — grid search / manual tuning / default values]
44	
45	\paragraph{Baselines.}
46	We compare against:
47	\begin{itemize}[nosep]
48	  \item \textbf{SmolVLA (base)}: the frozen base VLA with no correction, executing the mean of $K{=}10$ samples.
49	  \item \textbf{ReconVLA}~\cite{chen2026reconvla}: draws $K{=}10$ samples and selects the one minimizing scalar Euclidean distance to the sample mean.
50	\end{itemize}
51	Both baselines use the same SmolVLA checkpoint and sampling budget ($K{=}10$) as ACR-VLA, ensuring that differences reflect the correction mechanism rather than the base policy or compute budget.
52	
53	\paragraph{Metrics.}
54	The primary metric is task success rate (\%), reported as mean $\pm$ standard deviation across rollouts.
55	We additionally report per-task breakdowns to identify where ACR-VLA provides the largest gains.
56	
57	
58	\subsection{Main Results}
59	\label{sec:main_results}
60	
61	Table~\ref{tab:main} compares ACR-VLA against baselines on both LIBERO suites.
62	
63	\begin{table}[t]
64	\centering
65	\caption{Task success rate (\%~$\uparrow$) on LIBERO-Spatial and LIBERO-Object (10 tasks $\times$ 10 rollouts each). ACR-VLA attaches to the same frozen SmolVLA checkpoint used by all methods.}
66	\label{tab:main}
67	\small
68	\begin{tabular}{lcc}
69	\toprule
70	Method & LIBERO-Spatial & LIBERO-Object \\
71	\midrule
72	SmolVLA (base) & \textbf{--} & \textbf{--} \\
73	ReconVLA~\cite{chen2026reconvla} & \textbf{--} & \textbf{--} \\
74	\textbf{ACR-VLA (ours)} & \textbf{--} & \textbf{--} \\
75	\bottomrule
76	\end{tabular}
77	\end{table}
78	
79	ACR-VLA achieves \textbf{XX.X}\% on LIBERO-Spatial and \textbf{XX.X}\% on LIBERO-Object, improving over the base SmolVLA by \textbf{XX.X}\,pp and \textbf{XX.X}\,pp respectively.
80	Compared to ReconVLA, which uses the same $K{=}10$ sampling budget but selects actions via scalar Euclidean distance, ACR-VLA provides \textbf{XX.X}\,pp and \textbf{XX.X}\,pp improvements.
81	This gap confirms that per-DOF conformal conditioning enables more effective correction than scalar uncertainty selection.
82	
83	ReconVLA improves over the base SmolVLA by \textbf{XX.X}\,pp on average, demonstrating that multi-sample inference alone provides some benefit.
84	However, ReconVLA's sample-selection mechanism cannot synthesize corrections beyond the support of the original samples, whereas CRM's residual output can interpolate and extrapolate corrections conditioned on the uncertainty structure.
85	
86	
87	\subsection{Ablation Studies}
88	\label{sec:ablations}
89	
90	We isolate the contribution of each design choice through targeted ablations (Table~\ref{tab:ablation}).
91	
92	\begin{table}[t]
93	\centering
94	\caption{Ablation results on LIBERO-Spatial and LIBERO-Object. Each row modifies one component of ACR-VLA. Success rate (\%~$\uparrow$).}
95	\label{tab:ablation}
96	\small
97	\begin{tabular}{llcc}
98	\toprule
99	ID & Variant & Spatial & Object \\
100	\midrule
101	-- & ACR-VLA (full) & \textbf{--} & \textbf{--} \\
102	\midrule
103	A3 & CRM w/o conformal features & \textbf{--} & \textbf{--} \\
104	A4 & CRM w/ scalar uncertainty & \textbf{--} & \textbf{--} \\
105	A5 & Per-DOF Bonferroni (no joint Mahalanobis) & \textbf{--} & \textbf{--} \\
106	A7 & DiU single-pass~\cite{xing2026diu} replaces CGS & \textbf{--} & \textbf{--} \\
107	\bottomrule
108	\end{tabular}
109	\end{table}
110	
111	\paragraph{A3: CRM without conformal features.}
112	This variant removes all CGS features and conditions CRM only on the observation embedding and mean action, isolating whether uncertainty conditioning contributes beyond the base residual correction.
113	% [TODO: pending A3 results — report success delta and interpret]
114	
115	\paragraph{A4: Scalar vs.\ per-DOF uncertainty.}
116	This variant replaces the 40D CGS feature with a single scalar (average standard deviation across all DOFs and horizon steps), testing whether the per-DOF structure provides value beyond a scalar uncertainty summary---mirroring the controlled comparison in Section~\ref{sec:motivating}.
117	% [TODO: pending A4 results — report success delta and compare with MVP findings]
118	
119	\paragraph{A5: Per-DOF Bonferroni vs.\ joint Mahalanobis.}
120	This variant treats each of the $d{\times}H{=}30$ action dimensions independently with Bonferroni correction, rather than using the joint Mahalanobis formulation that captures cross-DOF covariance.
121	% [TODO: pending A5 results — report success delta and interpret region tightness]
122	
123	\paragraph{A7: CGS (multi-sample) vs.\ DiU (single-pass).}
124	This variant replaces the $K{=}10$ sample-based CGS features with single-pass divergence-based uncertainty from DiU~\cite{xing2026diu}, which captures per-DOF aleatoric uncertainty without additional sampling.
125	This ablation tests whether the multi-sample covariance signal---which reflects both epistemic and aleatoric components---provides a more actionable conditioning signal than single-pass aleatoric estimates.
126	% [TODO: pending A7 results — report success delta and interpret epistemic vs aleatoric]
127	
128	\paragraph{$K$ sensitivity.}
129	Figure~\ref{fig:k_sensitivity} shows ACR-VLA success as a function of the sample budget $K \in \{5, 10, 15, 20\}$.
130	
131	\begin{figure}[t]
132	\centering
133	% \includegraphics[width=\linewidth]{figures/k_sensitivity.pdf}
134	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}[Placeholder: $K$ sensitivity plot]\vspace{2em}}}
135	\caption{Task success rate vs.\ number of action samples $K$ on LIBERO-Spatial and LIBERO-Object. $K{=}10$ provides a favorable accuracy--compute trade-off.}
136	\label{fig:k_sensitivity}
137	\end{figure}
138	
139	% [TODO: pending K=5/15/20 experiments — fill in trend description after results]
140	We use $K{=}10$ as the default throughout our main experiments.
141	Each additional sample requires one full forward pass through the 450M-parameter base VLA, so the sample budget directly trades compute for covariance estimation quality ($d/K{=}0.6$ at $K{=}10$).
142	
143	
144	\subsection{Analysis}
145	\label{sec:analysis}
146	
147	\paragraph{Per-task breakdown.}
148	Table~\ref{tab:per_task} reports per-task success rates on LIBERO-Spatial.
149	
150	\begin{table}[t]
151	\centering
152	\caption{Per-task success rate (\%~$\uparrow$) on LIBERO-Spatial (10 rollouts per task).}
153	\label{tab:per_task}
154	\small
155	\begin{tabular}{lccc}
156	\toprule
157	Task & SmolVLA & ReconVLA & ACR-VLA \\
158	\midrule
159	Task 1  & \textbf{--} & \textbf{--} & \textbf{--} \\
160	Task 2  & \textbf{--} & \textbf{--} & \textbf{--} \\
161	Task 3  & \textbf{--} & \textbf{--} & \textbf{--} \\
162	Task 4  & \textbf{--} & \textbf{--} & \textbf{--} \\
163	Task 5  & \textbf{--} & \textbf{--} & \textbf{--} \\
164	Task 6  & \textbf{--} & \textbf{--} & \textbf{--} \\
165	Task 7  & \textbf{--} & \textbf{--} & \textbf{--} \\
166	Task 8  & \textbf{--} & \textbf{--} & \textbf{--} \\
167	Task 9  & \textbf{--} & \textbf{--} & \textbf{--} \\
168	Task 10 & \textbf{--} & \textbf{--} & \textbf{--} \\
169	\midrule
170	Average & \textbf{--} & \textbf{--} & \textbf{--} \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	ACR-VLA's gains are non-uniform across tasks.
176	We hypothesize that tasks where the base VLA exhibits high anisotropic uncertainty---i.e., large variance along some DOFs but not others---benefit most from per-DOF conditioning, as the CRM can selectively correct the uncertain dimensions.
177	Tasks where uncertainty is isotropically low (the base VLA is already confident and accurate) see smaller improvements, since there is less room for correction.
178	
179	\paragraph{CGS feature visualization.}
180	
181	\begin{figure}[t]
182	\centering
183	% \includegraphics[width=\linewidth]{figures/cgs_features.pdf}
184	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}[Placeholder: CGS feature visualization]\vspace{2em}}}
185	\caption{Per-DOF standard deviations from CGS across a representative episode. High-uncertainty dimensions (e.g., $x$-translation near contact) receive larger CRM corrections, while low-uncertainty dimensions remain largely unmodified.}
186	\label{fig:cgs_vis}
187	\end{figure}
188	
189	Figure~\ref{fig:cgs_vis} visualizes the per-DOF standard deviations from CGS across a representative LIBERO-Spatial episode alongside the CRM correction magnitudes.
190	The CRM learns to modulate its correction in proportion to the per-DOF uncertainty: dimensions with elevated $\sigma_{j,h}$ receive larger residuals, while dimensions with low variance are left approximately unchanged.
191	This dimension-selective behavior is the mechanism by which ACR-VLA avoids degrading already-accurate action components---a failure mode of both scalar-conditioned and unconditional correction approaches.
192	
193	\paragraph{When does ACR-VLA help most?}
194	Across both suites, the largest improvements occur in episodes where the base VLA produces actions with high translational variance but low rotational variance (or vice versa).
195	In these anisotropic-uncertainty regimes, scalar methods like ReconVLA cannot distinguish the uncertain from the confident dimensions and either under-correct or over-correct uniformly.
196	ACR-VLA's per-DOF conditioning resolves this ambiguity, directing correction effort where it is needed.
197	Conversely, in episodes where the base VLA is uniformly confident, ACR-VLA's corrections are small and success rates match the baseline, indicating that the module does not introduce harmful corrections when the base policy is already performing well.
198	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "acc98709-5202-425d-8186-60fc1f2f0f23",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to test three claims:\n(i)~per-DOF conformal conditioning improves task success over scalar and no-uncertainty baselines;\n(ii)~each component (CGS features, ACI+COC calibration, CRM architecture) contributes to the overall gain;\n(iii)~the improvement concentrates on tasks where the base VLA exhibits anisotropic uncertainty.\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object placement) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite.\nSuccess is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that predicts action chunks of length 50.\nWe use the community-fine-tuned checkpoint \\texttt{lerobot/smolvla\\_libero}.\nThe policy receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper.\nThe gripper dimension is handled outside the conformal pipeline via direct thresholding.\n\n\\paragraph{CGS configuration.}\nAt each control step, we draw $K{=}10$ action chunks via independent flow-matching rollouts and retain the first $H{=}5$ steps of each chunk (Section~\\ref{sec:cgs}).\nThe Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well} is computed per horizon step, yielding the 40D CGS feature: 30D per-DOF standard deviations ($d{\\times}H = 6{\\times}5$), 5D conformal radii, and 5D log-volume terms.\n\n\\paragraph{CRM architecture and training.}\nThe Conformal Refinement Module is a 2-layer MLP with hidden dimension 256 (${\\sim}$337K parameters).\nIts input concatenates the frozen observation embedding (${\\sim}$960D), the 40D CGS feature, and the 30D mean action, totaling ${\\sim}$1{,}030D.\nThe output is a 30D residual correction ($d{\\times}H$).\nWe train CRM on 26{,}737 precomputed samples (12{,}167 from LIBERO-Spatial + 14{,}570 from LIBERO-Object), constructed from 10 demonstrations per task across all 20 tasks.\nFor each demonstration step, we run $K{=}10$ SmolVLA forward passes and extract CGS features.\nTraining data is augmented with additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$), simulating noisy action predictions while preserving clean regression targets.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs.\nAll experiments use seed 42.\n\n\\paragraph{ACI+COC configuration.}\nThe target miscoverage rate is $\\alpha_{\\mathrm{target}}{=}0.1$.\nThe ACI learning rate $\\gamma$ and exponential decay $\\rho$ for within-episode weighting are hyperparameters.\n% [TODO: specify selection method once finalized — grid search / manual tuning / default values]\n\n\\paragraph{Baselines.}\nWe compare against:\n\\begin{itemize}[nosep]\n  \\item \\textbf{SmolVLA (base)}: the frozen base VLA with no correction, executing the mean of $K{=}10$ samples.\n  \\item \\textbf{ReconVLA}~\\cite{chen2026reconvla}: draws $K{=}10$ samples and selects the one minimizing scalar Euclidean distance to the sample mean.\n\\end{itemize}\nBoth baselines use the same SmolVLA checkpoint and sampling budget ($K{=}10$) as ACR-VLA, ensuring that differences reflect the correction mechanism rather than the base policy or compute budget.\n\n\\paragraph{Metrics.}\nThe primary metric is task success rate (\\%), reported as mean $\\pm$ standard deviation across rollouts.\nWe additionally report per-task breakdowns to identify where ACR-VLA provides the largest gains.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares ACR-VLA against baselines on both LIBERO suites.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%~$\\uparrow$) on LIBERO-Spatial and LIBERO-Object (10 tasks $\\times$ 10 rollouts each). ACR-VLA attaches to the same frozen SmolVLA checkpoint used by all methods.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMethod & LIBERO-Spatial & LIBERO-Object \\\\\n\\midrule\nSmolVLA (base) & \\textbf{--} & \\textbf{--} \\\\\nReconVLA~\\cite{chen2026reconvla} & \\textbf{--} & \\textbf{--} \\\\\n\\textbf{ACR-VLA (ours)} & \\textbf{--} & \\textbf{--} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nACR-VLA achieves \\textbf{XX.X}\\% on LIBERO-Spatial and \\textbf{XX.X}\\% on LIBERO-Object, improving over the base SmolVLA by \\textbf{XX.X}\\,pp and \\textbf{XX.X}\\,pp respectively.\nCompared to ReconVLA, which uses the same $K{=}10$ sampling budget but selects actions via scalar Euclidean distance, ACR-VLA provides \\textbf{XX.X}\\,pp and \\textbf{XX.X}\\,pp improvements.\nThis gap confirms that per-DOF conformal conditioning enables more effective correction than scalar uncertainty selection.\n\nReconVLA improves over the base SmolVLA by \\textbf{XX.X}\\,pp on average, demonstrating that multi-sample inference alone provides some benefit.\nHowever, ReconVLA's sample-selection mechanism cannot synthesize corrections beyond the support of the original samples, whereas CRM's residual output can interpolate and extrapolate corrections conditioned on the uncertainty structure.\n\n\n\\subsection{Ablation Studies}\n\\label{sec:ablations}\n\nWe isolate the contribution of each design choice through targeted ablations (Table~\\ref{tab:ablation}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation results on LIBERO-Spatial and LIBERO-Object. Each row modifies one component of ACR-VLA. Success rate (\\%~$\\uparrow$).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nID & Variant & Spatial & Object \\\\\n\\midrule\n-- & ACR-VLA (full) & \\textbf{--} & \\textbf{--} \\\\\n\\midrule\nA3 & CRM w/o conformal features & \\textbf{--} & \\textbf{--} \\\\\nA4 & CRM w/ scalar uncertainty & \\textbf{--} & \\textbf{--} \\\\\nA5 & Per-DOF Bonferroni (no joint Mahalanobis) & \\textbf{--} & \\textbf{--} \\\\\nA7 & DiU single-pass~\\cite{xing2026diu} replaces CGS & \\textbf{--} & \\textbf{--} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{A3: CRM without conformal features.}\nThis variant removes all CGS features and conditions CRM only on the observation embedding and mean action, isolating whether uncertainty conditioning contributes beyond the base residual correction.\n% [TODO: pending A3 results — report success delta and interpret]\n\n\\paragraph{A4: Scalar vs.\\ per-DOF uncertainty.}\nThis variant replaces the 40D CGS feature with a single scalar (average standard deviation across all DOFs and horizon steps), testing whether the per-DOF structure provides value beyond a scalar uncertainty summary---mirroring the controlled comparison in Section~\\ref{sec:motivating}.\n% [TODO: pending A4 results — report success delta and compare with MVP findings]\n\n\\paragraph{A5: Per-DOF Bonferroni vs.\\ joint Mahalanobis.}\nThis variant treats each of the $d{\\times}H{=}30$ action dimensions independently with Bonferroni correction, rather than using the joint Mahalanobis formulation that captures cross-DOF covariance.\n% [TODO: pending A5 results — report success delta and interpret region tightness]\n\n\\paragraph{A7: CGS (multi-sample) vs.\\ DiU (single-pass).}\nThis variant replaces the $K{=}10$ sample-based CGS features with single-pass divergence-based uncertainty from DiU~\\cite{xing2026diu}, which captures per-DOF aleatoric uncertainty without additional sampling.\nThis ablation tests whether the multi-sample covariance signal---which reflects both epistemic and aleatoric components---provides a more actionable conditioning signal than single-pass aleatoric estimates.\n% [TODO: pending A7 results — report success delta and interpret epistemic vs aleatoric]\n\n\\paragraph{$K$ sensitivity.}\nFigure~\\ref{fig:k_sensitivity} shows ACR-VLA success as a function of the sample budget $K \\in \\{5, 10, 15, 20\\}$.\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/k_sensitivity.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: $K$ sensitivity plot]\\vspace{2em}}}\n\\caption{Task success rate vs.\\ number of action samples $K$ on LIBERO-Spatial and LIBERO-Object. $K{=}10$ provides a favorable accuracy--compute trade-off.}\n\\label{fig:k_sensitivity}\n\\end{figure}\n\n% [TODO: pending K=5/15/20 experiments — fill in trend description after results]\nWe use $K{=}10$ as the default throughout our main experiments.\nEach additional sample requires one full forward pass through the 450M-parameter base VLA, so the sample budget directly trades compute for covariance estimation quality ($d/K{=}0.6$ at $K{=}10$).\n\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Per-task breakdown.}\nTable~\\ref{tab:per_task} reports per-task success rates on LIBERO-Spatial.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task success rate (\\%~$\\uparrow$) on LIBERO-Spatial (10 rollouts per task).}\n\\label{tab:per_task}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & SmolVLA & ReconVLA & ACR-VLA \\\\\n\\midrule\nTask 1  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 2  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 3  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 4  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 5  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 6  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 7  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 8  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 9  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 10 & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\n\\midrule\nAverage & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nACR-VLA's gains are non-uniform across tasks.\nWe hypothesize that tasks where the base VLA exhibits high anisotropic uncertainty---i.e., large variance along some DOFs but not others---benefit most from per-DOF conditioning, as the CRM can selectively correct the uncertain dimensions.\nTasks where uncertainty is isotropically low (the base VLA is already confident and accurate) see smaller improvements, since there is less room for correction.\n\n\\paragraph{CGS feature visualization.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/cgs_features.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: CGS feature visualization]\\vspace{2em}}}\n\\caption{Per-DOF standard deviations from CGS across a representative episode. High-uncertainty dimensions (e.g., $x$-translation near contact) receive larger CRM corrections, while low-uncertainty dimensions remain largely unmodified.}\n\\label{fig:cgs_vis}\n\\end{figure}\n\nFigure~\\ref{fig:cgs_vis} visualizes the per-DOF standard deviations from CGS across a representative LIBERO-Spatial episode alongside the CRM correction magnitudes.\nThe CRM learns to modulate its correction in proportion to the per-DOF uncertainty: dimensions with elevated $\\sigma_{j,h}$ receive larger residuals, while dimensions with low variance are left approximately unchanged.\nThis dimension-selective behavior is the mechanism by which ACR-VLA avoids degrading already-accurate action components---a failure mode of both scalar-conditioned and unconditional correction approaches.\n\n\\paragraph{When does ACR-VLA help most?}\nAcross both suites, the largest improvements occur in episodes where the base VLA produces actions with high translational variance but low rotational variance (or vice versa).\nIn these anisotropic-uncertainty regimes, scalar methods like ReconVLA cannot distinguish the uncertain from the confident dimensions and either under-correct or over-correct uniformly.\nACR-VLA's per-DOF conditioning resolves this ambiguity, directing correction effort where it is needed.\nConversely, in episodes where the base VLA is uniformly confident, ACR-VLA's corrections are small and success rates match the baseline, indicating that the module does not introduce harmful corrections when the base policy is already performing well.\n",
      "numLines": 198,
      "startLine": 1,
      "totalLines": 198
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
Now I have a clear picture of the existing experiments section (which has wrong framing — it claims per-DOF conformal conditioning helps, when the actual results show the opposite) and the method section (which already reflects the correct framing with obs_only as the primary variant).

Let me write the new experiments.tex with the correct data and framing. The key points:

1. obs_only is the winning variant, not per-DOF
2. Spatial is a null result
3. Per-DOF is an honest negative result
4. Magnitude control is critical


5. I should check the document structure to see how everything fits together.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "e15d8c23-6e09-4d1c-ae86-9ed6c0a5a0ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tUnFYhnvsMxcZT5kBzQBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7997,
      "cache_read_input_tokens": 31329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7997
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

Now I have full context. The old experiments.tex has the wrong framing (claims per-DOF helps). Let me write the replacement with correct data and honest reporting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "dc3fddbf-e090-44ca-93db-b4b618fc7480",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tUnFYhnvsMxcZT5kBzQBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7997,
      "cache_read_input_tokens": 31329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7997
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

<details open><summary>🔧 Tool call — Write · `toolu_01KxMgp59fDLagHYauxab6RF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex",
  "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to answer three questions:\n(i)~Does observation-conditioned residual correction improve over conformal selection alone?\n(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?\n(iii)~How sensitive is performance to the magnitude bound $\\varepsilon$?\nThe answers are: yes (+7.0\\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\\_only is robust across a wide range.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\nWe use the checkpoint \\texttt{lerobot/smolvla\\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.\n\n\\paragraph{Baselines.}\nAll methods use the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.\n  \\item \\textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\\ref{sec:selection}), no CRM correction.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nAll CRM variants share the same 3-layer MLP architecture (input$\\to$256$\\to$256$\\to$30) and differ only in their conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ (329K params). This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).\n\\end{itemize}\n\n\\paragraph{Training.}\nCRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.\nFor each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\\mathrm{base}}$.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.\nData augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$).\nThe default magnitude bound is $\\varepsilon = 0.1$ for all CRM variants unless stated otherwise.\n\n\\paragraph{Statistical protocol.}\nWe report success rates from seed 42 (10 rollouts $\\times$ 10 tasks = 100 episodes per suite).\nFisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\\textsc{pending}: seed43].\nUntil then, we report absolute differences descriptively without claiming statistical significance.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares all methods on both benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\\times$ 10 rollouts each, seed 42). $\\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Object (\\%) & Spatial (\\%) & $\\Delta$ Object \\\\\n\\midrule\nVLA-only ($K{=}1$)    & 12.0 & 30.0 & $\\phantom{+}0.0$ \\\\\nVLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\\phantom{+}0.0$ \\\\\nArgmin ($K{=}10$)      & 12.0 & 34.0 & --- \\\\\n\\midrule\nscalar ($\\varepsilon{=}0.1$)  & \\phantom{0}9.0 & 32.0 & $-3.0$ \\\\\nperdof ($\\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\\\\n\\textbf{obs\\_only} ($\\varepsilon{=}0.1$) & \\textbf{19.0} & \\textbf{35.0} & $\\mathbf{+7.0}$ \\\\\n\\midrule\nobs\\_only ($\\varepsilon{=}0.2$) & \\textbf{22.0} & 35.0 & $+10.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Object benchmark: correction helps.}\nOn LIBERO-Object, obs\\_only at $\\varepsilon{=}0.1$ achieves 19.0\\%, a +7.0\\,pp improvement over the Argmin baseline (12.0\\%).\nIncreasing the magnitude bound to $\\varepsilon{=}0.2$ yields 22.0\\% (+10.0\\,pp).\nThis is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.\n\nThree baselines---VLA-only, VLA-mean, and Argmin---all achieve exactly 12.0\\%, indicating that multi-sample averaging and Mahalanobis-based selection hit a ceiling on this benchmark.\nThe CRM breaks through this ceiling by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.\n\n\\paragraph{Spatial benchmark: correction does not help.}\nOn LIBERO-Spatial, all methods cluster within a 5\\,pp band (30--35\\%).\nThe best CRM variants (obs\\_only, perdof) achieve 35\\%, only 1\\,pp above the Argmin baseline (34\\%).\nThis is a null result that we report prominently.\n\nWe interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.\nThe VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.\nResidual correction at the action level is the wrong granularity for this type of generalization.\n\n\\paragraph{Key finding.}\nSample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.\nFor spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.\n\n\n\\subsection{CRM Conditioning Ablation}\n\\label{sec:ablation}\n\nWe focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\\ref{tab:main}).\n\n\\paragraph{Ranking.}\nobs\\_only (19.0\\%) $\\gg$ Argmin (12.0\\%) $\\approx$ perdof (11.0\\%) $>$ scalar (9.0\\%).\n\nThis ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \\emph{hurt} rather than help.\nScalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\\,pp below the Argmin baseline that uses no correction at all.\n\n\\paragraph{Why does richer conditioning fail?}\nWe identify three factors:\n\n\\emph{(1) Noisy covariance estimation.}\nWith $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.\nWhile Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.\nFeeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).\n\n\\emph{(2) Observation features are sufficient.}\nThe frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.\nThis information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.\nThe CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.\n\n\\emph{(3) Per-step MSE $\\neq$ episode success.}\nIn offline evaluation, per-DOF conformal features reduce the per-step mean squared error between corrected actions and expert demonstrations.\nHowever, this per-step improvement does not translate to higher episode success rates in closed-loop evaluation, where small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.\nThe additional noise from conformal features may cause occasional large corrections that, while reducing average MSE, lead to catastrophic failures in individual episodes.\n\n\\paragraph{Connection to magnitude sensitivity.}\nThe obs\\_only variant is also more robust across magnitude bounds $\\varepsilon$ than perdof (Section~\\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.\n\n\n\\subsection{Magnitude Sensitivity}\n\\label{sec:magnitude_results}\n\nThe norm bound $\\varepsilon$ determines how much CRM can deviate from the conformal-selected action.\nFigure~\\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\\varepsilon \\in [0.05, 1.42]$.\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/magnitude_sweep.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: Magnitude sweep --- obs\\_only vs.\\ perdof vs.\\ Argmin reference]\\vspace{2em}}}\n\\caption{Success rate (\\%) on LIBERO-Spatial as a function of magnitude bound $\\varepsilon$. obs\\_only (solid blue) maintains 35--36\\% across $\\varepsilon \\in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\\varepsilon$. The Argmin baseline (dotted gray, 34\\%) is independent of $\\varepsilon$. At $\\varepsilon{=}1.42$ (unbounded), both CRM variants achieve 0\\%.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Spatial across magnitude bounds $\\varepsilon$. The Argmin baseline (34\\%, no correction) is independent of $\\varepsilon$.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\\\\n\\midrule\nobs\\_only & 35.0 & 35.0 & 36.0 & 0.0 \\\\\nperdof    & 31.0 & 35.0 & 26.0 & 0.0 \\\\\n\\midrule\nArgmin (ref.) & \\multicolumn{4}{c}{34.0 (flat, no correction)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{obs\\_only is robust.}\nThe obs\\_only variant maintains 35--36\\% across the full range $\\varepsilon \\in [0.05, 0.3]$---a remarkably flat profile.\nThis stability means the practitioner need not carefully tune $\\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.\n\n\\paragraph{perdof is fragile.}\nIn contrast, perdof peaks at 35\\% when $\\varepsilon{=}0.1$ but collapses to 26\\% at $\\varepsilon{=}0.3$---a 9\\,pp drop.\nThis fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.\nAt $\\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.\n\n\\paragraph{Unbounded correction is catastrophic.}\nAt $\\varepsilon{=}1.42$ (the natural, unbounded CRM output norm), both variants achieve 0\\% success.\nThis confirms the failure mode described in Section~\\ref{sec:magnitude}: without clipping, the corrected action deviates so far from the base policy's output that compounding error across the trajectory destroys performance entirely.\nThe Argmin baseline (34\\%) outperforms all CRM variants at this setting, demonstrating that \\emph{any} correction is harmful when unbounded.\n\n\\paragraph{Practical recommendation.}\nThe safe operating range is $\\varepsilon \\in [0.05, 0.2]$.\nWithin this range, obs\\_only is the only variant that consistently matches or exceeds the Argmin baseline.\nWe use $\\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nPer-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.\n\n[\\textsc{pending}: seed43] --- A per-task heatmap comparing obs\\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.\nWe expect the analysis to show that obs\\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.\nTask difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "5addd483-c43a-46e3-bc8b-7113cd219350",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012tUnFYhnvsMxcZT5kBzQBe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7997,
      "cache_read_input_tokens": 31329,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7997
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

_source line 18 · 2026-05-15T19:24:01.354Z_

<details><summary>↩ Tool result · `toolu_01KxMgp59fDLagHYauxab6RF`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "a1c2ab0b-56f1-4936-a20c-6badf28ee614",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex",
    "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to answer three questions:\n(i)~Does observation-conditioned residual correction improve over conformal selection alone?\n(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?\n(iii)~How sensitive is performance to the magnitude bound $\\varepsilon$?\nThe answers are: yes (+7.0\\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\\_only is robust across a wide range.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\nWe use the checkpoint \\texttt{lerobot/smolvla\\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.\n\n\\paragraph{Baselines.}\nAll methods use the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.\n  \\item \\textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\\ref{sec:selection}), no CRM correction.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nAll CRM variants share the same 3-layer MLP architecture (input$\\to$256$\\to$256$\\to$30) and differ only in their conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ (329K params). This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).\n\\end{itemize}\n\n\\paragraph{Training.}\nCRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.\nFor each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\\mathrm{base}}$.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.\nData augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$).\nThe default magnitude bound is $\\varepsilon = 0.1$ for all CRM variants unless stated otherwise.\n\n\\paragraph{Statistical protocol.}\nWe report success rates from seed 42 (10 rollouts $\\times$ 10 tasks = 100 episodes per suite).\nFisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\\textsc{pending}: seed43].\nUntil then, we report absolute differences descriptively without claiming statistical significance.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares all methods on both benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\\times$ 10 rollouts each, seed 42). $\\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Object (\\%) & Spatial (\\%) & $\\Delta$ Object \\\\\n\\midrule\nVLA-only ($K{=}1$)    & 12.0 & 30.0 & $\\phantom{+}0.0$ \\\\\nVLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\\phantom{+}0.0$ \\\\\nArgmin ($K{=}10$)      & 12.0 & 34.0 & --- \\\\\n\\midrule\nscalar ($\\varepsilon{=}0.1$)  & \\phantom{0}9.0 & 32.0 & $-3.0$ \\\\\nperdof ($\\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\\\\n\\textbf{obs\\_only} ($\\varepsilon{=}0.1$) & \\textbf{19.0} & \\textbf{35.0} & $\\mathbf{+7.0}$ \\\\\n\\midrule\nobs\\_only ($\\varepsilon{=}0.2$) & \\textbf{22.0} & 35.0 & $+10.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Object benchmark: correction helps.}\nOn LIBERO-Object, obs\\_only at $\\varepsilon{=}0.1$ achieves 19.0\\%, a +7.0\\,pp improvement over the Argmin baseline (12.0\\%).\nIncreasing the magnitude bound to $\\varepsilon{=}0.2$ yields 22.0\\% (+10.0\\,pp).\nThis is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.\n\nThree baselines---VLA-only, VLA-mean, and Argmin---all achieve exactly 12.0\\%, indicating that multi-sample averaging and Mahalanobis-based selection hit a ceiling on this benchmark.\nThe CRM breaks through this ceiling by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.\n\n\\paragraph{Spatial benchmark: correction does not help.}\nOn LIBERO-Spatial, all methods cluster within a 5\\,pp band (30--35\\%).\nThe best CRM variants (obs\\_only, perdof) achieve 35\\%, only 1\\,pp above the Argmin baseline (34\\%).\nThis is a null result that we report prominently.\n\nWe interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.\nThe VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.\nResidual correction at the action level is the wrong granularity for this type of generalization.\n\n\\paragraph{Key finding.}\nSample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.\nFor spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.\n\n\n\\subsection{CRM Conditioning Ablation}\n\\label{sec:ablation}\n\nWe focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\\ref{tab:main}).\n\n\\paragraph{Ranking.}\nobs\\_only (19.0\\%) $\\gg$ Argmin (12.0\\%) $\\approx$ perdof (11.0\\%) $>$ scalar (9.0\\%).\n\nThis ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \\emph{hurt} rather than help.\nScalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\\,pp below the Argmin baseline that uses no correction at all.\n\n\\paragraph{Why does richer conditioning fail?}\nWe identify three factors:\n\n\\emph{(1) Noisy covariance estimation.}\nWith $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.\nWhile Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.\nFeeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).\n\n\\emph{(2) Observation features are sufficient.}\nThe frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.\nThis information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.\nThe CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.\n\n\\emph{(3) Per-step MSE $\\neq$ episode success.}\nIn offline evaluation, per-DOF conformal features reduce the per-step mean squared error between corrected actions and expert demonstrations.\nHowever, this per-step improvement does not translate to higher episode success rates in closed-loop evaluation, where small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.\nThe additional noise from conformal features may cause occasional large corrections that, while reducing average MSE, lead to catastrophic failures in individual episodes.\n\n\\paragraph{Connection to magnitude sensitivity.}\nThe obs\\_only variant is also more robust across magnitude bounds $\\varepsilon$ than perdof (Section~\\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.\n\n\n\\subsection{Magnitude Sensitivity}\n\\label{sec:magnitude_results}\n\nThe norm bound $\\varepsilon$ determines how much CRM can deviate from the conformal-selected action.\nFigure~\\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\\varepsilon \\in [0.05, 1.42]$.\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/magnitude_sweep.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: Magnitude sweep --- obs\\_only vs.\\ perdof vs.\\ Argmin reference]\\vspace{2em}}}\n\\caption{Success rate (\\%) on LIBERO-Spatial as a function of magnitude bound $\\varepsilon$. obs\\_only (solid blue) maintains 35--36\\% across $\\varepsilon \\in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\\varepsilon$. The Argmin baseline (dotted gray, 34\\%) is independent of $\\varepsilon$. At $\\varepsilon{=}1.42$ (unbounded), both CRM variants achieve 0\\%.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Spatial across magnitude bounds $\\varepsilon$. The Argmin baseline (34\\%, no correction) is independent of $\\varepsilon$.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\\\\n\\midrule\nobs\\_only & 35.0 & 35.0 & 36.0 & 0.0 \\\\\nperdof    & 31.0 & 35.0 & 26.0 & 0.0 \\\\\n\\midrule\nArgmin (ref.) & \\multicolumn{4}{c}{34.0 (flat, no correction)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{obs\\_only is robust.}\nThe obs\\_only variant maintains 35--36\\% across the full range $\\varepsilon \\in [0.05, 0.3]$---a remarkably flat profile.\nThis stability means the practitioner need not carefully tune $\\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.\n\n\\paragraph{perdof is fragile.}\nIn contrast, perdof peaks at 35\\% when $\\varepsilon{=}0.1$ but collapses to 26\\% at $\\varepsilon{=}0.3$---a 9\\,pp drop.\nThis fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.\nAt $\\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.\n\n\\paragraph{Unbounded correction is catastrophic.}\nAt $\\varepsilon{=}1.42$ (the natural, unbounded CRM output norm), both variants achieve 0\\% success.\nThis confirms the failure mode described in Section~\\ref{sec:magnitude}: without clipping, the corrected action deviates so far from the base policy's output that compounding error across the trajectory destroys performance entirely.\nThe Argmin baseline (34\\%) outperforms all CRM variants at this setting, demonstrating that \\emph{any} correction is harmful when unbounded.\n\n\\paragraph{Practical recommendation.}\nThe safe operating range is $\\varepsilon \\in [0.05, 0.2]$.\nWithin this range, obs\\_only is the only variant that consistently matches or exceeds the Argmin baseline.\nWe use $\\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nPer-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.\n\n[\\textsc{pending}: seed43] --- A per-task heatmap comparing obs\\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.\nWe expect the analysis to show that obs\\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.\nTask difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 197,
        "newStart": 1,
        "newLines": 193,
        "lines": [
          "+",
          " \\section{Experiments}",
          " \\label{sec:experiments}",
          " ",
          "-We evaluate ACR-VLA on two LIBERO task suites to test three claims:",
          "-(i)~per-DOF conformal conditioning improves task success over scalar and no-uncertainty baselines;",
          "-(ii)~each component (CGS features, ACI+COC calibration, CRM architecture) contributes to the overall gain;",
          "-(iii)~the improvement concentrates on tasks where the base VLA exhibits anisotropic uncertainty.",
          "+We evaluate ACR-VLA on two LIBERO task suites to answer three questions:",
          "+(i)~Does observation-conditioned residual correction improve over conformal selection alone?",
          "+(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?",
          "+(iii)~How sensitive is performance to the magnitude bound $\\varepsilon$?",
          "+The answers are: yes (+7.0\\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\\_only is robust across a wide range.",
          " ",
          "-",
          " \\subsection{Experimental Setup}",
          " \\label{sec:exp_setup}",
          " ",
          " \\paragraph{Benchmarks.}",
          " We use two suites from the LIBERO benchmark~\\cite{liu2023libero}:",
          "-\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object placement) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across object instances).",
          "-Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite.",
          "-Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.",
          "+\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).",
          "+Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.",
          " ",
          " \\paragraph{Base VLA.}",
          "-We build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that predicts action chunks of length 50.",
          "-We use the community-fine-tuned checkpoint \\texttt{lerobot/smolvla\\_libero}.",
          "-The policy receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.",
          "-Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper.",
          "-The gripper dimension is handled outside the conformal pipeline via direct thresholding.",
          "+We build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.",
          "+We use the checkpoint \\texttt{lerobot/smolvla\\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.",
          "+Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.",
          " ",
          "-\\paragraph{CGS configuration.}",
          "-At each control step, we draw $K{=}10$ action chunks via independent flow-matching rollouts and retain the first $H{=}5$ steps of each chunk (Section~\\ref{sec:cgs}).",
          "-The Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well} is computed per horizon step, yielding the 40D CGS feature: 30D per-DOF standard deviations ($d{\\times}H = 6{\\times}5$), 5D conformal radii, and 5D log-volume terms.",
          "-",
          "-\\paragraph{CRM architecture and training.}",
          "-The Conformal Refinement Module is a 2-layer MLP with hidden dimension 256 (${\\sim}$337K parameters).",
          "-Its input concatenates the frozen observation embedding (${\\sim}$960D), the 40D CGS feature, and the 30D mean action, totaling ${\\sim}$1{,}030D.",
          "-The output is a 30D residual correction ($d{\\times}H$).",
          "-We train CRM on 26{,}737 precomputed samples (12{,}167 from LIBERO-Spatial + 14{,}570 from LIBERO-Object), constructed from 10 demonstrations per task across all 20 tasks.",
          "-For each demonstration step, we run $K{=}10$ SmolVLA forward passes and extract CGS features.",
          "-Training data is augmented with additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$), simulating noisy action predictions while preserving clean regression targets.",
          "-Optimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs.",
          "-All experiments use seed 42.",
          "-",
          "-\\paragraph{ACI+COC configuration.}",
          "-The target miscoverage rate is $\\alpha_{\\mathrm{target}}{=}0.1$.",
          "-The ACI learning rate $\\gamma$ and exponential decay $\\rho$ for within-episode weighting are hyperparameters.",
          "-% [TODO: specify selection method once finalized — grid search / manual tuning / default values]",
          "-",
          " \\paragraph{Baselines.}",
          "-We compare against:",
          "+All methods use the same frozen SmolVLA checkpoint:",
          " \\begin{itemize}[nosep]",
          "-  \\item \\textbf{SmolVLA (base)}: the frozen base VLA with no correction, executing the mean of $K{=}10$ samples.",
          "-  \\item \\textbf{ReconVLA}~\\cite{chen2026reconvla}: draws $K{=}10$ samples and selects the one minimizing scalar Euclidean distance to the sample mean.",
          "+  \\item \\textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.",
          "+  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.",
          "+  \\item \\textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\\ref{sec:selection}), no CRM correction.",
          " \\end{itemize}",
          "-Both baselines use the same SmolVLA checkpoint and sampling budget ($K{=}10$) as ACR-VLA, ensuring that differences reflect the correction mechanism rather than the base policy or compute budget.",
          " ",
          "-\\paragraph{Metrics.}",
          "-The primary metric is task success rate (\\%), reported as mean $\\pm$ standard deviation across rollouts.",
          "-We additionally report per-task breakdowns to identify where ACR-VLA provides the largest gains.",
          "+\\paragraph{CRM variants.}",
          "+All CRM variants share the same 3-layer MLP architecture (input$\\to$256$\\to$256$\\to$30) and differ only in their conditioning input:",
          "+\\begin{itemize}[nosep]",
          "+  \\item \\textbf{obs\\_only}: frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ (329K params). This is our primary method.",
          "+  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).",
          "+  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).",
          "+\\end{itemize}",
          " ",
          "+\\paragraph{Training.}",
          "+CRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.",
          "+For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\\mathrm{base}}$.",
          "+Optimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.",
          "+Data augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$).",
          "+The default magnitude bound is $\\varepsilon = 0.1$ for all CRM variants unless stated otherwise.",
          " ",
          "+\\paragraph{Statistical protocol.}",
          "+We report success rates from seed 42 (10 rollouts $\\times$ 10 tasks = 100 episodes per suite).",
          "+Fisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\\textsc{pending}: seed43].",
          "+Until then, we report absolute differences descriptively without claiming statistical significance.",
          "+",
          "+",
          " \\subsection{Main Results}",
          " \\label{sec:main_results}",
          " ",
          "-Table~\\ref{tab:main} compares ACR-VLA against baselines on both LIBERO suites.",
          "+Table~\\ref{tab:main} compares all methods on both benchmarks.",
          " ",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Task success rate (\\%~$\\uparrow$) on LIBERO-Spatial and LIBERO-Object (10 tasks $\\times$ 10 rollouts each). ACR-VLA attaches to the same frozen SmolVLA checkpoint used by all methods.}",
          "+\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\\times$ 10 rollouts each, seed 42). $\\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}",
          " \\label{tab:main}",
          " \\small",
          "-\\begin{tabular}{lcc}",
          "+\\begin{tabular}{lccc}",
          " \\toprule",
          "-Method & LIBERO-Spatial & LIBERO-Object \\\\",
          "+Method & Object (\\%) & Spatial (\\%) & $\\Delta$ Object \\\\",
          " \\midrule",
          "-SmolVLA (base) & \\textbf{--} & \\textbf{--} \\\\",
          "-ReconVLA~\\cite{chen2026reconvla} & \\textbf{--} & \\textbf{--} \\\\",
          "-\\textbf{ACR-VLA (ours)} & \\textbf{--} & \\textbf{--} \\\\",
          "+VLA-only ($K{=}1$)    & 12.0 & 30.0 & $\\phantom{+}0.0$ \\\\",
          "+VLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\\phantom{+}0.0$ \\\\",
          "+Argmin ($K{=}10$)      & 12.0 & 34.0 & --- \\\\",
          "+\\midrule",
          "+scalar ($\\varepsilon{=}0.1$)  & \\phantom{0}9.0 & 32.0 & $-3.0$ \\\\",
          "+perdof ($\\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\\\",
          "+\\textbf{obs\\_only} ($\\varepsilon{=}0.1$) & \\textbf{19.0} & \\textbf{35.0} & $\\mathbf{+7.0}$ \\\\",
          "+\\midrule",
          "+obs\\_only ($\\varepsilon{=}0.2$) & \\textbf{22.0} & 35.0 & $+10.0$ \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-ACR-VLA achieves \\textbf{XX.X}\\% on LIBERO-Spatial and \\textbf{XX.X}\\% on LIBERO-Object, improving over the base SmolVLA by \\textbf{XX.X}\\,pp and \\textbf{XX.X}\\,pp respectively.",
          "-Compared to ReconVLA, which uses the same $K{=}10$ sampling budget but selects actions via scalar Euclidean distance, ACR-VLA provides \\textbf{XX.X}\\,pp and \\textbf{XX.X}\\,pp improvements.",
          "-This gap confirms that per-DOF conformal conditioning enables more effective correction than scalar uncertainty selection.",
          "+\\paragraph{Object benchmark: correction helps.}",
          "+On LIBERO-Object, obs\\_only at $\\varepsilon{=}0.1$ achieves 19.0\\%, a +7.0\\,pp improvement over the Argmin baseline (12.0\\%).",
          "+Increasing the magnitude bound to $\\varepsilon{=}0.2$ yields 22.0\\% (+10.0\\,pp).",
          "+This is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.",
          " ",
          "-ReconVLA improves over the base SmolVLA by \\textbf{XX.X}\\,pp on average, demonstrating that multi-sample inference alone provides some benefit.",
          "-However, ReconVLA's sample-selection mechanism cannot synthesize corrections beyond the support of the original samples, whereas CRM's residual output can interpolate and extrapolate corrections conditioned on the uncertainty structure.",
          "+Three baselines---VLA-only, VLA-mean, and Argmin---all achieve exactly 12.0\\%, indicating that multi-sample averaging and Mahalanobis-based selection hit a ceiling on this benchmark.",
          "+The CRM breaks through this ceiling by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.",
          " ",
          "+\\paragraph{Spatial benchmark: correction does not help.}",
          "+On LIBERO-Spatial, all methods cluster within a 5\\,pp band (30--35\\%).",
          "+The best CRM variants (obs\\_only, perdof) achieve 35\\%, only 1\\,pp above the Argmin baseline (34\\%).",
          "+This is a null result that we report prominently.",
          " ",
          "-\\subsection{Ablation Studies}",
          "-\\label{sec:ablations}",
          "+We interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.",
          "+The VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.",
          "+Residual correction at the action level is the wrong granularity for this type of generalization.",
          " ",
          "-We isolate the contribution of each design choice through targeted ablations (Table~\\ref{tab:ablation}).",
          "+\\paragraph{Key finding.}",
          "+Sample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.",
          "+For spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.",
          " ",
          "-\\begin{table}[t]",
          "-\\centering",
          "-\\caption{Ablation results on LIBERO-Spatial and LIBERO-Object. Each row modifies one component of ACR-VLA. Success rate (\\%~$\\uparrow$).}",
          "-\\label{tab:ablation}",
          "-\\small",
          "-\\begin{tabular}{llcc}",
          "-\\toprule",
          "-ID & Variant & Spatial & Object \\\\",
          "-\\midrule",
          "--- & ACR-VLA (full) & \\textbf{--} & \\textbf{--} \\\\",
          "-\\midrule",
          "-A3 & CRM w/o conformal features & \\textbf{--} & \\textbf{--} \\\\",
          "-A4 & CRM w/ scalar uncertainty & \\textbf{--} & \\textbf{--} \\\\",
          "-A5 & Per-DOF Bonferroni (no joint Mahalanobis) & \\textbf{--} & \\textbf{--} \\\\",
          "-A7 & DiU single-pass~\\cite{xing2026diu} replaces CGS & \\textbf{--} & \\textbf{--} \\\\",
          "-\\bottomrule",
          "-\\end{tabular}",
          "-\\end{table}",
          " ",
          "-\\paragraph{A3: CRM without conformal features.}",
          "-This variant removes all CGS features and conditions CRM only on the observation embedding and mean action, isolating whether uncertainty conditioning contributes beyond the base residual correction.",
          "-% [TODO: pending A3 results — report success delta and interpret]",
          "+\\subsection{CRM Conditioning Ablation}",
          "+\\label{sec:ablation}",
          " ",
          "-\\paragraph{A4: Scalar vs.\\ per-DOF uncertainty.}",
          "-This variant replaces the 40D CGS feature with a single scalar (average standard deviation across all DOFs and horizon steps), testing whether the per-DOF structure provides value beyond a scalar uncertainty summary---mirroring the controlled comparison in Section~\\ref{sec:motivating}.",
          "-% [TODO: pending A4 results — report success delta and compare with MVP findings]",
          "+We focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\\ref{tab:main}).",
          " ",
          "-\\paragraph{A5: Per-DOF Bonferroni vs.\\ joint Mahalanobis.}",
          "-This variant treats each of the $d{\\times}H{=}30$ action dimensions independently with Bonferroni correction, rather than using the joint Mahalanobis formulation that captures cross-DOF covariance.",
          "-% [TODO: pending A5 results — report success delta and interpret region tightness]",
          "+\\paragraph{Ranking.}",
          "+obs\\_only (19.0\\%) $\\gg$ Argmin (12.0\\%) $\\approx$ perdof (11.0\\%) $>$ scalar (9.0\\%).",
          " ",
          "-\\paragraph{A7: CGS (multi-sample) vs.\\ DiU (single-pass).}",
          "-This variant replaces the $K{=}10$ sample-based CGS features with single-pass divergence-based uncertainty from DiU~\\cite{xing2026diu}, which captures per-DOF aleatoric uncertainty without additional sampling.",
          "-This ablation tests whether the multi-sample covariance signal---which reflects both epistemic and aleatoric components---provides a more actionable conditioning signal than single-pass aleatoric estimates.",
          "-% [TODO: pending A7 results — report success delta and interpret epistemic vs aleatoric]",
          "+This ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \\emph{hurt} rather than help.",
          "+Scalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\\,pp below the Argmin baseline that uses no correction at all.",
          " ",
          "-\\paragraph{$K$ sensitivity.}",
          "-Figure~\\ref{fig:k_sensitivity} shows ACR-VLA success as a function of the sample budget $K \\in \\{5, 10, 15, 20\\}$.",
          "+\\paragraph{Why does richer conditioning fail?}",
          "+We identify three factors:",
          " ",
          "-\\begin{figure}[t]",
          "-\\centering",
          "-% \\includegraphics[width=\\linewidth]{figures/k_sensitivity.pdf}",
          "-\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: $K$ sensitivity plot]\\vspace{2em}}}",
          "-\\caption{Task success rate vs.\\ number of action samples $K$ on LIBERO-Spatial and LIBERO-Object. $K{=}10$ provides a favorable accuracy--compute trade-off.}",
          "-\\label{fig:k_sensitivity}",
          "-\\end{figure}",
          "+\\emph{(1) Noisy covariance estimation.}",
          "+With $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.",
          "+While Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.",
          "+Feeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).",
          " ",
          "-% [TODO: pending K=5/15/20 experiments — fill in trend description after results]",
          "-We use $K{=}10$ as the default throughout our main experiments.",
          "-Each additional sample requires one full forward pass through the 450M-parameter base VLA, so the sample budget directly trades compute for covariance estimation quality ($d/K{=}0.6$ at $K{=}10$).",
          "+\\emph{(2) Observation features are sufficient.}",
          "+The frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.",
          "+This information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.",
          "+The CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.",
          " ",
          "+\\emph{(3) Per-step MSE $\\neq$ episode success.}",
          "+In offline evaluation, per-DOF conformal features reduce the per-step mean squared error between corrected actions and expert demonstrations.",
          "+However, this per-step improvement does not translate to higher episode success rates in closed-loop evaluation, where small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.",
          "+The additional noise from conformal features may cause occasional large corrections that, while reducing average MSE, lead to catastrophic failures in individual episodes.",
          " ",
          "-\\subsection{Analysis}",
          "-\\label{sec:analysis}",
          "+\\paragraph{Connection to magnitude sensitivity.}",
          "+The obs\\_only variant is also more robust across magnitude bounds $\\varepsilon$ than perdof (Section~\\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.",
          " ",
          "-\\paragraph{Per-task breakdown.}",
          "-Table~\\ref{tab:per_task} reports per-task success rates on LIBERO-Spatial.",
          " ",
          "+\\subsection{Magnitude Sensitivity}",
          "+\\label{sec:magnitude_results}",
          "+",
          "+The norm bound $\\varepsilon$ determines how much CRM can deviate from the conformal-selected action.",
          "+Figure~\\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\\varepsilon \\in [0.05, 1.42]$.",
          "+",
          "+\\begin{figure}[t]",
          "+\\centering",
          "+% \\includegraphics[width=\\linewidth]{figures/magnitude_sweep.pdf}",
          "+\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: Magnitude sweep --- obs\\_only vs.\\ perdof vs.\\ Argmin reference]\\vspace{2em}}}",
          "+\\caption{Success rate (\\%) on LIBERO-Spatial as a function of magnitude bound $\\varepsilon$. obs\\_only (solid blue) maintains 35--36\\% across $\\varepsilon \\in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\\varepsilon$. The Argmin baseline (dotted gray, 34\\%) is independent of $\\varepsilon$. At $\\varepsilon{=}1.42$ (unbounded), both CRM variants achieve 0\\%.}",
          "+\\label{fig:magnitude}",
          "+\\end{figure}",
          "+",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Per-task success rate (\\%~$\\uparrow$) on LIBERO-Spatial (10 rollouts per task).}",
          "-\\label{tab:per_task}",
          "+\\caption{Success rate (\\%) on LIBERO-Spatial across magnitude bounds $\\varepsilon$. The Argmin baseline (34\\%, no correction) is independent of $\\varepsilon$.}",
          "+\\label{tab:magnitude}",
          " \\small",
          "-\\begin{tabular}{lccc}",
          "+\\begin{tabular}{lcccc}",
          " \\toprule",
          "-Task & SmolVLA & ReconVLA & ACR-VLA \\\\",
          "+$\\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\\\",
          " \\midrule",
          "-Task 1  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "-Task 2  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "-Task 3  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "-Task 4  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "-Task 5  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "-Task 6  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "-Task 7  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "-Task 8  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "-Task 9  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "-Task 10 & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "+obs\\_only & 35.0 & 35.0 & 36.0 & 0.0 \\\\",
          "+perdof    & 31.0 & 35.0 & 26.0 & 0.0 \\\\",
          " \\midrule",
          "-Average & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\",
          "+Argmin (ref.) & \\multicolumn{4}{c}{34.0 (flat, no correction)} \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}",
          " ",
          "-ACR-VLA's gains are non-uniform across tasks.",
          "-We hypothesize that tasks where the base VLA exhibits high anisotropic uncertainty---i.e., large variance along some DOFs but not others---benefit most from per-DOF conditioning, as the CRM can selectively correct the uncertain dimensions.",
          "-Tasks where uncertainty is isotropically low (the base VLA is already confident and accurate) see smaller improvements, since there is less room for correction.",
          "+\\paragraph{obs\\_only is robust.}",
          "+The obs\\_only variant maintains 35--36\\% across the full range $\\varepsilon \\in [0.05, 0.3]$---a remarkably flat profile.",
          "+This stability means the practitioner need not carefully tune $\\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.",
          " ",
          "-\\paragraph{CGS feature visualization.}",
          "+\\paragraph{perdof is fragile.}",
          "+In contrast, perdof peaks at 35\\% when $\\varepsilon{=}0.1$ but collapses to 26\\% at $\\varepsilon{=}0.3$---a 9\\,pp drop.",
          "+This fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.",
          "+At $\\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.",
          " ",
          "-\\begin{figure}[t]",
          "-\\centering",
          "-% \\includegraphics[width=\\linewidth]{figures/cgs_features.pdf}",
          "-\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: CGS feature visualization]\\vspace{2em}}}",
          "-\\caption{Per-DOF standard deviations from CGS across a representative episode. High-uncertainty dimensions (e.g., $x$-translation near contact) receive larger CRM corrections, while low-uncertainty dimensions remain largely unmodified.}",
          "-\\label{fig:cgs_vis}",
          "-\\end{figure}",
          "+\\paragraph{Unbounded correction is catastrophic.}",
          "+At $\\varepsilon{=}1.42$ (the natural, unbounded CRM output norm), both variants achieve 0\\% success.",
          "+This confirms the failure mode described in Section~\\ref{sec:magnitude}: without clipping, the corrected action deviates so far from the base policy's output that compounding error across the trajectory destroys performance entirely.",
          "+The Argmin baseline (34\\%) outperforms all CRM variants at this setting, demonstrating that \\emph{any} correction is harmful when unbounded.",
          " ",
          "-Figure~\\ref{fig:cgs_vis} visualizes the per-DOF standard deviations from CGS across a representative LIBERO-Spatial episode alongside the CRM correction magnitudes.",
          "-The CRM learns to modulate its correction in proportion to the per-DOF uncertainty: dimensions with elevated $\\sigma_{j,h}$ receive larger residuals, while dimensions with low variance are left approximately unchanged.",
          "-This dimension-selective behavior is the mechanism by which ACR-VLA avoids degrading already-accurate action components---a failure mode of both scalar-conditioned and unconditional correction approaches.",
          "+\\paragraph{Practical recommendation.}",
          "+The safe operating range is $\\varepsilon \\in [0.05, 0.2]$.",
          "+Within this range, obs\\_only is the only variant that consistently matches or exceeds the Argmin baseline.",
          "+We use $\\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.",
          " ",
          "-\\paragraph{When does ACR-VLA help most?}",
          "-Across both suites, the largest improvements occur in episodes where the base VLA produces actions with high translational variance but low rotational variance (or vice versa).",
          "-In these anisotropic-uncertainty regimes, scalar methods like ReconVLA cannot distinguish the uncertain from the confident dimensions and either under-correct or over-correct uniformly.",
          "-ACR-VLA's per-DOF conditioning resolves this ambiguity, directing correction effort where it is needed.",
          "-Conversely, in episodes where the base VLA is uniformly confident, ACR-VLA's corrections are small and success rates match the baseline, indicating that the module does not introduce harmful corrections when the base policy is already performing well.",
          "+",
          "+\\subsection{Per-Task Analysis}",
          "+\\label{sec:per_task}",
          "+",
          "+Per-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.",
          "+",
          "+[\\textsc{pending}: seed43] --- A per-task heatmap comparing obs\\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.",
          "+We expect the analysis to show that obs\\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.",
          "+Task difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover)."
        ]
      }
    ],
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to test three claims:\n(i)~per-DOF conformal conditioning improves task success over scalar and no-uncertainty baselines;\n(ii)~each component (CGS features, ACI+COC calibration, CRM architecture) contributes to the overall gain;\n(iii)~the improvement concentrates on tasks where the base VLA exhibits anisotropic uncertainty.\n\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object placement) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite.\nSuccess is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA that predicts action chunks of length 50.\nWe use the community-fine-tuned checkpoint \\texttt{lerobot/smolvla\\_libero}.\nThe policy receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper.\nThe gripper dimension is handled outside the conformal pipeline via direct thresholding.\n\n\\paragraph{CGS configuration.}\nAt each control step, we draw $K{=}10$ action chunks via independent flow-matching rollouts and retain the first $H{=}5$ steps of each chunk (Section~\\ref{sec:cgs}).\nThe Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well} is computed per horizon step, yielding the 40D CGS feature: 30D per-DOF standard deviations ($d{\\times}H = 6{\\times}5$), 5D conformal radii, and 5D log-volume terms.\n\n\\paragraph{CRM architecture and training.}\nThe Conformal Refinement Module is a 2-layer MLP with hidden dimension 256 (${\\sim}$337K parameters).\nIts input concatenates the frozen observation embedding (${\\sim}$960D), the 40D CGS feature, and the 30D mean action, totaling ${\\sim}$1{,}030D.\nThe output is a 30D residual correction ($d{\\times}H$).\nWe train CRM on 26{,}737 precomputed samples (12{,}167 from LIBERO-Spatial + 14{,}570 from LIBERO-Object), constructed from 10 demonstrations per task across all 20 tasks.\nFor each demonstration step, we run $K{=}10$ SmolVLA forward passes and extract CGS features.\nTraining data is augmented with additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$), simulating noisy action predictions while preserving clean regression targets.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs.\nAll experiments use seed 42.\n\n\\paragraph{ACI+COC configuration.}\nThe target miscoverage rate is $\\alpha_{\\mathrm{target}}{=}0.1$.\nThe ACI learning rate $\\gamma$ and exponential decay $\\rho$ for within-episode weighting are hyperparameters.\n% [TODO: specify selection method once finalized — grid search / manual tuning / default values]\n\n\\paragraph{Baselines.}\nWe compare against:\n\\begin{itemize}[nosep]\n  \\item \\textbf{SmolVLA (base)}: the frozen base VLA with no correction, executing the mean of $K{=}10$ samples.\n  \\item \\textbf{ReconVLA}~\\cite{chen2026reconvla}: draws $K{=}10$ samples and selects the one minimizing scalar Euclidean distance to the sample mean.\n\\end{itemize}\nBoth baselines use the same SmolVLA checkpoint and sampling budget ($K{=}10$) as ACR-VLA, ensuring that differences reflect the correction mechanism rather than the base policy or compute budget.\n\n\\paragraph{Metrics.}\nThe primary metric is task success rate (\\%), reported as mean $\\pm$ standard deviation across rollouts.\nWe additionally report per-task breakdowns to identify where ACR-VLA provides the largest gains.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares ACR-VLA against baselines on both LIBERO suites.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%~$\\uparrow$) on LIBERO-Spatial and LIBERO-Object (10 tasks $\\times$ 10 rollouts each). ACR-VLA attaches to the same frozen SmolVLA checkpoint used by all methods.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nMethod & LIBERO-Spatial & LIBERO-Object \\\\\n\\midrule\nSmolVLA (base) & \\textbf{--} & \\textbf{--} \\\\\nReconVLA~\\cite{chen2026reconvla} & \\textbf{--} & \\textbf{--} \\\\\n\\textbf{ACR-VLA (ours)} & \\textbf{--} & \\textbf{--} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nACR-VLA achieves \\textbf{XX.X}\\% on LIBERO-Spatial and \\textbf{XX.X}\\% on LIBERO-Object, improving over the base SmolVLA by \\textbf{XX.X}\\,pp and \\textbf{XX.X}\\,pp respectively.\nCompared to ReconVLA, which uses the same $K{=}10$ sampling budget but selects actions via scalar Euclidean distance, ACR-VLA provides \\textbf{XX.X}\\,pp and \\textbf{XX.X}\\,pp improvements.\nThis gap confirms that per-DOF conformal conditioning enables more effective correction than scalar uncertainty selection.\n\nReconVLA improves over the base SmolVLA by \\textbf{XX.X}\\,pp on average, demonstrating that multi-sample inference alone provides some benefit.\nHowever, ReconVLA's sample-selection mechanism cannot synthesize corrections beyond the support of the original samples, whereas CRM's residual output can interpolate and extrapolate corrections conditioned on the uncertainty structure.\n\n\n\\subsection{Ablation Studies}\n\\label{sec:ablations}\n\nWe isolate the contribution of each design choice through targeted ablations (Table~\\ref{tab:ablation}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Ablation results on LIBERO-Spatial and LIBERO-Object. Each row modifies one component of ACR-VLA. Success rate (\\%~$\\uparrow$).}\n\\label{tab:ablation}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nID & Variant & Spatial & Object \\\\\n\\midrule\n-- & ACR-VLA (full) & \\textbf{--} & \\textbf{--} \\\\\n\\midrule\nA3 & CRM w/o conformal features & \\textbf{--} & \\textbf{--} \\\\\nA4 & CRM w/ scalar uncertainty & \\textbf{--} & \\textbf{--} \\\\\nA5 & Per-DOF Bonferroni (no joint Mahalanobis) & \\textbf{--} & \\textbf{--} \\\\\nA7 & DiU single-pass~\\cite{xing2026diu} replaces CGS & \\textbf{--} & \\textbf{--} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{A3: CRM without conformal features.}\nThis variant removes all CGS features and conditions CRM only on the observation embedding and mean action, isolating whether uncertainty conditioning contributes beyond the base residual correction.\n% [TODO: pending A3 results — report success delta and interpret]\n\n\\paragraph{A4: Scalar vs.\\ per-DOF uncertainty.}\nThis variant replaces the 40D CGS feature with a single scalar (average standard deviation across all DOFs and horizon steps), testing whether the per-DOF structure provides value beyond a scalar uncertainty summary---mirroring the controlled comparison in Section~\\ref{sec:motivating}.\n% [TODO: pending A4 results — report success delta and compare with MVP findings]\n\n\\paragraph{A5: Per-DOF Bonferroni vs.\\ joint Mahalanobis.}\nThis variant treats each of the $d{\\times}H{=}30$ action dimensions independently with Bonferroni correction, rather than using the joint Mahalanobis formulation that captures cross-DOF covariance.\n% [TODO: pending A5 results — report success delta and interpret region tightness]\n\n\\paragraph{A7: CGS (multi-sample) vs.\\ DiU (single-pass).}\nThis variant replaces the $K{=}10$ sample-based CGS features with single-pass divergence-based uncertainty from DiU~\\cite{xing2026diu}, which captures per-DOF aleatoric uncertainty without additional sampling.\nThis ablation tests whether the multi-sample covariance signal---which reflects both epistemic and aleatoric components---provides a more actionable conditioning signal than single-pass aleatoric estimates.\n% [TODO: pending A7 results — report success delta and interpret epistemic vs aleatoric]\n\n\\paragraph{$K$ sensitivity.}\nFigure~\\ref{fig:k_sensitivity} shows ACR-VLA success as a function of the sample budget $K \\in \\{5, 10, 15, 20\\}$.\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/k_sensitivity.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: $K$ sensitivity plot]\\vspace{2em}}}\n\\caption{Task success rate vs.\\ number of action samples $K$ on LIBERO-Spatial and LIBERO-Object. $K{=}10$ provides a favorable accuracy--compute trade-off.}\n\\label{fig:k_sensitivity}\n\\end{figure}\n\n% [TODO: pending K=5/15/20 experiments — fill in trend description after results]\nWe use $K{=}10$ as the default throughout our main experiments.\nEach additional sample requires one full forward pass through the 450M-parameter base VLA, so the sample budget directly trades compute for covariance estimation quality ($d/K{=}0.6$ at $K{=}10$).\n\n\n\\subsection{Analysis}\n\\label{sec:analysis}\n\n\\paragraph{Per-task breakdown.}\nTable~\\ref{tab:per_task} reports per-task success rates on LIBERO-Spatial.\n\n\\begin{table}[t]\n\\centering\n\\caption{Per-task success rate (\\%~$\\uparrow$) on LIBERO-Spatial (10 rollouts per task).}\n\\label{tab:per_task}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nTask & SmolVLA & ReconVLA & ACR-VLA \\\\\n\\midrule\nTask 1  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 2  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 3  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 4  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 5  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 6  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 7  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 8  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 9  & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\nTask 10 & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\n\\midrule\nAverage & \\textbf{--} & \\textbf{--} & \\textbf{--} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nACR-VLA's gains are non-uniform across tasks.\nWe hypothesize that tasks where the base VLA exhibits high anisotropic uncertainty---i.e., large variance along some DOFs but not others---benefit most from per-DOF conditioning, as the CRM can selectively correct the uncertain dimensions.\nTasks where uncertainty is isotropically low (the base VLA is already confident and accurate) see smaller improvements, since there is less room for correction.\n\n\\paragraph{CGS feature visualization.}\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/cgs_features.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: CGS feature visualization]\\vspace{2em}}}\n\\caption{Per-DOF standard deviations from CGS across a representative episode. High-uncertainty dimensions (e.g., $x$-translation near contact) receive larger CRM corrections, while low-uncertainty dimensions remain largely unmodified.}\n\\label{fig:cgs_vis}\n\\end{figure}\n\nFigure~\\ref{fig:cgs_vis} visualizes the per-DOF standard deviations from CGS across a representative LIBERO-Spatial episode alongside the CRM correction magnitudes.\nThe CRM learns to modulate its correction in proportion to the per-DOF uncertainty: dimensions with elevated $\\sigma_{j,h}$ receive larger residuals, while dimensions with low variance are left approximately unchanged.\nThis dimension-selective behavior is the mechanism by which ACR-VLA avoids degrading already-accurate action components---a failure mode of both scalar-conditioned and unconditional correction approaches.\n\n\\paragraph{When does ACR-VLA help most?}\nAcross both suites, the largest improvements occur in episodes where the base VLA produces actions with high translational variance but low rotational variance (or vice versa).\nIn these anisotropic-uncertainty regimes, scalar methods like ReconVLA cannot distinguish the uncertain from the confident dimensions and either under-correct or over-correct uniformly.\nACR-VLA's per-DOF conditioning resolves this ambiguity, directing correction effort where it is needed.\nConversely, in episodes where the base VLA is uniformly confident, ACR-VLA's corrections are small and success rates match the baseline, indicating that the module does not introduce harmful corrections when the base policy is already performing well.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 19_

Now let me register this artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "c0afcc90-29f1-49f4-9d5d-f4bd6cba5aa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191Zy3zqN9epH8n7WZUuuRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4382,
      "cache_read_input_tokens": 39326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4382
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ec169Gcu4TPswL45fbG6HU`</summary>

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
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "3485c807-8e73-49c7-b27a-abd96a70f79c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0191Zy3zqN9epH8n7WZUuuRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4382,
      "cache_read_input_tokens": 39326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4382
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

_source line 21 · 2026-05-15T19:24:04.176Z_

<details><summary>↩ Tool result · `toolu_01Ec169Gcu4TPswL45fbG6HU`</summary>

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
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "f52c0411-7bb1-4553-8018-68005f2dfedc",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01R6eKrDXV8c4Wh8pqLsVKMt`</summary>

```json
{
  "name": "experiments-section-v2",
  "type": "paper",
  "description": "Complete Experiments section (Section 4) for CoRL 2026 paper. Replaces old version with correct framing: obs_only +7.0pp on Object, spatial null result, per-DOF negative result, magnitude sensitivity analysis.",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex",
  "tags": [
    "paper",
    "experiments",
    "corl2026",
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
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "bf275cb0-9899-4996-94ff-76ab691c5657",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmHCv9KqDXAMFfvyUVVuAH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 822,
      "cache_read_input_tokens": 43708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 822
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

_source line 23 · 2026-05-15T19:24:09.973Z_

<details><summary>↩ Tool result · `toolu_01R6eKrDXV8c4Wh8pqLsVKMt`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_ac6246\", \"name\": \"experiments-section-v2\", \"type\": \"paper\", \"description\": \"Complete Experiments section (Section 4) for CoRL 2026 paper. Replaces old version with correct framing: obs_only +7.0pp on Object, spatial null result, per-DOF negative result, magnitude sensitivity analysis.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_ac6246.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T19:24:09.848800+00:00\", \"tags\": [\"paper\", \"experiments\", \"corl2026\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "d38d685f-1e32-4916-8d45-e2776f3b505e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_ac6246\\\", \\\"name\\\": \\\"experiments-section-v2\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Complete Experiments section (Section 4) for CoRL 2026 paper. Replaces old version with correct framing: obs_only +7.0pp on Object, spatial null result, per-DOF negative result, magnitude sensitivity analysis.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_ac6246.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T19:24:09.848800+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"experiments\\\", \\\"corl2026\\\", \\\"latex\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_ac6246\", \"name\": \"experiments-section-v2\", \"type\": \"paper\", \"description\": \"Complete Experiments section (Section 4) for CoRL 2026 paper. Replaces old version with correct framing: obs_only +7.0pp on Object, spatial null result, per-DOF negative result, magnitude sensitivity analysis.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_ac6246.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T19:24:09.848800+00:00\", \"tags\": [\"paper\", \"experiments\", \"corl2026\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

Written to `artifacts/_project/paper/experiments.tex`. Structure:

- **4.1 Setup** — SmolVLA backbone, LIBERO-Spatial/Object, 3 baselines (VLA-only, VLA-mean, Argmin), 3 CRM variants (obs\_only, perdof, scalar), training details, statistical protocol with `\pending{seed43}` placeholder.
- **4.2 Main Results** — Table 1 with all 7 rows, both benchmarks. Object: obs\_only 19.0% (+7.0pp), all baselines at 12.0% ceiling. Spatial: null result (30–35% band), reported prominently.
- **4.3 Conditioning Ablation** — obs\_only >> perdof ≈ Argmin > scalar. Three-part explanation: noisy covariance at K=10, observation features sufficient, per-step MSE ≠ episode success.
- **4.4 Magnitude Sensitivity** — Table + figure placeholder. obs\_only flat at 35–36% across ε∈[0.05,0.3], perdof collapses 9pp at ε=0.3, unbounded (ε=1.42) → 0% for both. Safe range: [0.05, 0.2].
- **4.5 Per-Task Analysis** — Placeholder with `\pending{seed43}`, describes planned heatmap and difficulty analysis.

All numbers match the provided tables exactly. Labels use the specified scheme (`sec:exp_setup`, `sec:main_results`, `sec:ablation`, `sec:magnitude_results`, `sec:per_task`).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "uuid": "c1b9f38d-8a61-470c-98e6-40df99e95bbc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EFLvuBfg5XCWP1Z9XqM6xF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 44530,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 588
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

Written to `artifacts/_project/paper/experiments.tex`. Structure:

- **4.1 Setup** — SmolVLA backbone, LIBERO-Spatial/Object, 3 baselines (VLA-only, VLA-mean, Argmin), 3 CRM variants (obs\_only, perdof, scalar), training details, statistical protocol with `\pending{seed43}` placeholder.
- **4.2 Main Results** — Table 1 with all 7 rows, both benchmarks. Object: obs\_only 19.0% (+7.0pp), all baselines at 12.0% ceiling. Spatial: null result (30–35% band), reported prominently.
- **4.3 Conditioning Ablation** — obs\_only >> perdof ≈ Argmin > scalar. Three-part explanation: noisy covariance at K=10, observation features sufficient, per-step MSE ≠ episode success.
- **4.4 Magnitude Sensitivity** — Table + figure placeholder. obs\_only flat at 35–36% across ε∈[0.05,0.3], perdof collapses 9pp at ε=0.3, unbounded (ε=1.42) → 0% for both. Safe range: [0.05, 0.2].
- **4.5 Per-Task Analysis** — Placeholder with `\pending{seed43}`, describes planned heatmap and difficulty analysis.

All numbers match the provided tables exactly. Labels use the specified scheme (`sec:exp_setup`, `sec:main_results`, `sec:ablation`, `sec:magnitude_results`, `sec:per_task`).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 116525,
  "duration_api_ms": 117432,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "6de03f19-98ae-4731-a266-0b5e55e1636d",
  "total_cost_usd": 0.44669075,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 33277,
    "cache_read_input_tokens": 196273,
    "output_tokens": 5493,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33277,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 395,
        "cache_read_input_tokens": 44530,
        "cache_creation_input_tokens": 588,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 588
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3108,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003203,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 5493,
      "cacheReadInputTokens": 196273,
      "cacheCreationInputTokens": 33277,
      "webSearchRequests": 0,
      "costUSD": 0.44348775,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9465127a-acf1-469b-806e-8ace3586175f"
}
```

</details>

---
