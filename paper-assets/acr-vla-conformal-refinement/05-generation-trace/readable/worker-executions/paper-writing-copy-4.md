# paper writing

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_writing_20260515T193525.log`
- **Structured JSON:** [`216dcab1972902f42d48.json`](../../sessions/21/216dcab1972902f42d48.json)

## Before a recorded user message

31 recorded events

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
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
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
  "uuid": "b35f5462-02f0-40e7-9936-0e6f3e011fe8",
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
  "uuid": "a51f77e7-f021-48bf-a57c-584b1f5a7a2d",
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772"
}
```

---

### Assistant

_source line 4_

Let me start by reading the writing guidelines, then check the existing paper structure for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "66bc9bcb-a292-4b75-be43-5d5c5a2c990a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaztEkyMUx81DYqB3fJ6Gp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12991,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12991
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

<details open><summary>🔧 Tool call — Read · `toolu_01PGKT1ctbEtfFGkz7KBoobF`</summary>

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
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "ea541109-b120-4fef-b10a-000036b1ef2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaztEkyMUx81DYqB3fJ6Gp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12991,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12991
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

_source line 6 · 2026-05-15T19:35:46.641Z_

<details><summary>↩ Tool result · `toolu_01PGKT1ctbEtfFGkz7KBoobF`</summary>

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
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "71475c23-55db-4888-be24-a402a844c04b",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01BZF3KydrXid8pW8kFjwGVz`</summary>

```json
{
  "pattern": "**/*",
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
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "9c2ddfbc-63c5-4fa1-ac19-ce24f986343f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FaztEkyMUx81DYqB3fJ6Gp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12991,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12991
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

_source line 8 · 2026-05-15T19:35:47.249Z_

<details><summary>↩ Tool result · `toolu_01BZF3KydrXid8pW8kFjwGVz`</summary>

```text
artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/corl_paper_outline.md
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_ac6246.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/sections/introduction.tex
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "202a29e3-445f-4733-bfa0-bdb551b9bb41",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references_e9d4d2.bib",
      "artifacts/_project/paper/related_work_9c2927.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/introduction_c83872.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/method_section_draft.tex",
      "artifacts/_project/paper/experiments_c64a8c.tex",
      "artifacts/_project/paper/corl_paper_outline.md",
      "artifacts/_project/paper/method_fb526b.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/experiments_ac6246.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/sections/introduction.tex",
      "artifacts/_project/paper/references.bib"
    ],
    "durationMs": 24,
    "numFiles": 14,
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
Let me read the existing related work draft and the introduction to understand the paper's positioning, and also check the bib file for the cite keys mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "275a2b9a-5beb-4777-a309-d7822e94c46f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NE11BqvCWjdzDYSs26znKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5860,
      "cache_read_input_tokens": 24832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5860
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

Let me read the existing drafts and bib file for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "67f0f33f-184b-46a3-a3d5-e8fec998055c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NE11BqvCWjdzDYSs26znKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5860,
      "cache_read_input_tokens": 24832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5860
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

<details open><summary>🔧 Tool call — Read · `toolu_01NRnVb9fkakEx1xhHufys68`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "52e0d616-bb00-4359-8b20-8bf8f44fb1a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NE11BqvCWjdzDYSs26znKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5860,
      "cache_read_input_tokens": 24832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5860
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

_source line 12 · 2026-05-15T19:35:53.514Z_

<details><summary>↩ Tool result · `toolu_01NRnVb9fkakEx1xhHufys68`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{VLA Robustness Methods.}
5	Recent work has sought to improve the robustness of vision-language-action models through training-time interventions.
6	SRPO~\cite{srpo2025} applies self-referential reinforcement learning to fine-tune VLA policies, achieving strong gains on the LIBERO-Plus benchmark.
7	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.
8	DiG-Flow~\cite{digflow2025} introduces discrepancy-guided flow matching, steering the generative process toward more accurate denoising trajectories during training.
9	SnapFlow~\cite{luan2026snapflow} distills multi-step flow-matching into single-step inference, reducing latency while preserving action quality.
10	TT-VLA~\cite{liu2026ttvla} adapts VLA parameters at test time via reinforcement learning, blurring the line between training-time and inference-time approaches.
11	VLA-GSE~\cite{vla_gse_2026} improves generalization through parameter-efficient fine-tuning with gated sparse experts, and Cosmos-Policy~\cite{cosmos_policy_2026} leverages video foundation models for visuomotor control.
12	These methods are complementary to ACR-VLA: they improve the base policy itself, whereas ACR-VLA operates as a post-hoc inference-time module that attaches to any frozen flow-matching VLA without modifying its weights.
13	This orthogonality means ACR-VLA can be composed with any of the above methods to provide additional robustness through uncertainty-conditioned correction.
14	
15	\paragraph{Uncertainty Quantification for Robot Learning.}
16	Quantifying predictive uncertainty in learned policies is essential for safe deployment.
17	Deep Ensembles~\cite{lakshminarayanan2017ensembles} and MC-Dropout~\cite{gal2016dropout} are foundational approaches that estimate epistemic uncertainty through multiple forward passes or stochastic weight perturbations, but both produce scalar or loosely structured uncertainty estimates that do not distinguish which action dimensions are uncertain.
18	In the generative policy setting, Diffusion Policy~\cite{chi2023diffusion_policy} introduced the diffusion-based action generation paradigm that flow-matching VLAs build upon; its stochastic sampling naturally admits multi-sample uncertainty estimation, though the original work does not exploit this for correction.
19	DiU~\cite{xing2026diu} shows that for flow-matching models, the divergence of the velocity field recovers per-DOF \emph{aleatoric} uncertainty from a single forward pass, providing an efficient uncertainty signal without additional sampling.
20	ACR-VLA differs along two axes.
21	First, it estimates \emph{model uncertainty} via multi-sample covariance---a sampling-based signal that reflects both epistemic and aleatoric components, and that rises under distribution shift when the policy is uncertain about the correct action---which we find more actionable for correction than single-pass aleatoric estimates (validated in ablation A7).
22	Second, it produces a structured 40-dimensional feature vector (per-DOF standard deviations, calibrated conformal radii, and log-volume) rather than a scalar summary, enabling dimension-selective correction as demonstrated in Section~\ref{sec:motivating}.
23	
24	\paragraph{Conformal Prediction in Robotics.}
25	Conformal prediction (CP) provides distribution-free coverage guarantees and has seen growing adoption in robotics.
26	\citet{angelopoulos2023gentle} provide a comprehensive tutorial on the framework.
27	Conformalized Quantile Regression~\cite{romano2019cqr} extends CP to heteroscedastic settings, while Adaptive Conformal Inference~\cite{gibbs2021aci} maintains coverage under distribution shift through online threshold updates---a property critical for non-stationary robotic environments.
28	\citet{barber2023conformal} further relax the exchangeability assumption, enabling conformal methods under general temporal dependence.
29	Braun et al.~\cite{braun2025cgs} introduce Conformalized Gaussian Scoring for multivariate prediction regions, which ACR-VLA builds upon for its per-DOF feature extraction.
30	In robotics applications, CP-in-the-Loop~\cite{wang2025cploop} integrates conformal regions into trajectory optimization as constraints, and Conformalized Teleoperation~\cite{zhao2024conformalized} uses CP to provide safety guarantees during shared autonomy.
31	UPS~\cite{yuan2026ups} employs CP for binary policy gating---deciding whether to execute or abstain---while SAFE~\cite{gu2025safe} uses anomaly detection to trigger safe fallback behaviors.
32	A common thread in these systems is that CP serves as a \emph{binary decision mechanism} (accept/reject, execute/abstain, safe/unsafe).
33	ACR-VLA departs from this paradigm by using conformal statistics as \emph{continuous input features} to a learned correction module, enabling graded, dimension-selective refinement rather than all-or-nothing decisions.
34	
35	\paragraph{Inference-Time Action Correction.}
36	The most closely related line of work addresses action refinement at inference time without retraining the base policy.
37	A2C2~\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's action chunk generation, reducing effective latency.
38	However, A2C2 applies a generic residual without uncertainty conditioning: it has no mechanism to modulate correction magnitude based on per-dimension confidence, which can lead to unnecessary perturbation of already-accurate action components.
39	ReconVLA~\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean based on scalar Euclidean distance, using this distance as a proxy for uncertainty.
40	While effective as a variance-reduction strategy, sample selection is fundamentally limited: it cannot synthesize an action better than any individual sample, and its scalar uncertainty measure does not distinguish which degrees of freedom are unreliable.
41	ACR-VLA addresses both limitations.
42	Compared to A2C2, it conditions correction on calibrated per-DOF conformal features, enabling the refinement module to selectively correct high-uncertainty dimensions while preserving accurate predictions on others.
43	Compared to ReconVLA, it performs learned synthesis rather than selection, producing corrections that can improve upon any individual sample, and replaces the scalar Euclidean proxy with a 40-dimensional structured representation that captures per-DOF variance, calibrated confidence, and distributional volume.
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "b7d02a02-c529-4bcd-85a9-5e28d83e52fc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{VLA Robustness Methods.}\nRecent work has sought to improve the robustness of vision-language-action models through training-time interventions.\nSRPO~\\cite{srpo2025} applies self-referential reinforcement learning to fine-tune VLA policies, achieving strong gains on the LIBERO-Plus benchmark.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.\nDiG-Flow~\\cite{digflow2025} introduces discrepancy-guided flow matching, steering the generative process toward more accurate denoising trajectories during training.\nSnapFlow~\\cite{luan2026snapflow} distills multi-step flow-matching into single-step inference, reducing latency while preserving action quality.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time via reinforcement learning, blurring the line between training-time and inference-time approaches.\nVLA-GSE~\\cite{vla_gse_2026} improves generalization through parameter-efficient fine-tuning with gated sparse experts, and Cosmos-Policy~\\cite{cosmos_policy_2026} leverages video foundation models for visuomotor control.\nThese methods are complementary to ACR-VLA: they improve the base policy itself, whereas ACR-VLA operates as a post-hoc inference-time module that attaches to any frozen flow-matching VLA without modifying its weights.\nThis orthogonality means ACR-VLA can be composed with any of the above methods to provide additional robustness through uncertainty-conditioned correction.\n\n\\paragraph{Uncertainty Quantification for Robot Learning.}\nQuantifying predictive uncertainty in learned policies is essential for safe deployment.\nDeep Ensembles~\\cite{lakshminarayanan2017ensembles} and MC-Dropout~\\cite{gal2016dropout} are foundational approaches that estimate epistemic uncertainty through multiple forward passes or stochastic weight perturbations, but both produce scalar or loosely structured uncertainty estimates that do not distinguish which action dimensions are uncertain.\nIn the generative policy setting, Diffusion Policy~\\cite{chi2023diffusion_policy} introduced the diffusion-based action generation paradigm that flow-matching VLAs build upon; its stochastic sampling naturally admits multi-sample uncertainty estimation, though the original work does not exploit this for correction.\nDiU~\\cite{xing2026diu} shows that for flow-matching models, the divergence of the velocity field recovers per-DOF \\emph{aleatoric} uncertainty from a single forward pass, providing an efficient uncertainty signal without additional sampling.\nACR-VLA differs along two axes.\nFirst, it estimates \\emph{model uncertainty} via multi-sample covariance---a sampling-based signal that reflects both epistemic and aleatoric components, and that rises under distribution shift when the policy is uncertain about the correct action---which we find more actionable for correction than single-pass aleatoric estimates (validated in ablation A7).\nSecond, it produces a structured 40-dimensional feature vector (per-DOF standard deviations, calibrated conformal radii, and log-volume) rather than a scalar summary, enabling dimension-selective correction as demonstrated in Section~\\ref{sec:motivating}.\n\n\\paragraph{Conformal Prediction in Robotics.}\nConformal prediction (CP) provides distribution-free coverage guarantees and has seen growing adoption in robotics.\n\\citet{angelopoulos2023gentle} provide a comprehensive tutorial on the framework.\nConformalized Quantile Regression~\\cite{romano2019cqr} extends CP to heteroscedastic settings, while Adaptive Conformal Inference~\\cite{gibbs2021aci} maintains coverage under distribution shift through online threshold updates---a property critical for non-stationary robotic environments.\n\\citet{barber2023conformal} further relax the exchangeability assumption, enabling conformal methods under general temporal dependence.\nBraun et al.~\\cite{braun2025cgs} introduce Conformalized Gaussian Scoring for multivariate prediction regions, which ACR-VLA builds upon for its per-DOF feature extraction.\nIn robotics applications, CP-in-the-Loop~\\cite{wang2025cploop} integrates conformal regions into trajectory optimization as constraints, and Conformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to provide safety guarantees during shared autonomy.\nUPS~\\cite{yuan2026ups} employs CP for binary policy gating---deciding whether to execute or abstain---while SAFE~\\cite{gu2025safe} uses anomaly detection to trigger safe fallback behaviors.\nA common thread in these systems is that CP serves as a \\emph{binary decision mechanism} (accept/reject, execute/abstain, safe/unsafe).\nACR-VLA departs from this paradigm by using conformal statistics as \\emph{continuous input features} to a learned correction module, enabling graded, dimension-selective refinement rather than all-or-nothing decisions.\n\n\\paragraph{Inference-Time Action Correction.}\nThe most closely related line of work addresses action refinement at inference time without retraining the base policy.\nA2C2~\\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's action chunk generation, reducing effective latency.\nHowever, A2C2 applies a generic residual without uncertainty conditioning: it has no mechanism to modulate correction magnitude based on per-dimension confidence, which can lead to unnecessary perturbation of already-accurate action components.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean based on scalar Euclidean distance, using this distance as a proxy for uncertainty.\nWhile effective as a variance-reduction strategy, sample selection is fundamentally limited: it cannot synthesize an action better than any individual sample, and its scalar uncertainty measure does not distinguish which degrees of freedom are unreliable.\nACR-VLA addresses both limitations.\nCompared to A2C2, it conditions correction on calibrated per-DOF conformal features, enabling the refinement module to selectively correct high-uncertainty dimensions while preserving accurate predictions on others.\nCompared to ReconVLA, it performs learned synthesis rather than selection, producing corrections that can improve upon any individual sample, and replaces the scalar Euclidean proxy with a 40-dimensional structured representation that captures per-DOF variance, calibrated confidence, and distributional volume.\n",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01LPMnYiMoBh2BFd3tnsbue4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "550e514d-2373-467c-a835-0f08a1985986",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NE11BqvCWjdzDYSs26znKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5860,
      "cache_read_input_tokens": 24832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5860
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

_source line 14 · 2026-05-15T19:35:53.908Z_

<details><summary>↩ Tool result · `toolu_01LPMnYiMoBh2BFd3tnsbue4`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	% Para 1: Problem — VLA success + robustness gap under distribution shift
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla} have reached 97--99\% success rates on standard manipulation benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet this near-saturation masks a fragile reality: under distribution shifts common in real-world deployment---camera viewpoint changes, lighting variation, sensor noise, object layout differences---the same policies suffer substantial performance degradation~\cite{fei2025liberoplus}.
7	Closing this robustness gap is a prerequisite for deploying learned manipulation policies outside tightly controlled lab settings.
8	
9	% Para 2: Existing approaches — training-time vs inference-time, what they miss
10	Two lines of work address VLA robustness.
11	\emph{Training-time methods} improve the base policy itself: SRPO~\cite{srpo2025} applies self-referential policy optimization, while RobustVLA~\cite{robustvla2025} and DiG-Flow~\cite{digflow2025} incorporate robustness-aware objectives into training.
12	These methods are effective but require retraining or fine-tuning, and their gains are bounded by the training distribution.
13	\emph{Inference-time methods} leave the policy frozen and intervene at deployment.
14	ReconVLA~\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean, using scalar Euclidean distance as an uncertainty proxy.
15	SAFE~\cite{gu2025safe} detects anomalous states and triggers fallback behaviors.
16	UPS~\cite{yuan2026ups} and CP-in-the-Loop~\cite{wang2025cploop} use conformal prediction for binary decisions---execute or abstain, safe or unsafe---but do not use conformal statistics as features for continuous correction.
17	A2C2~\cite{a2c2_2025} learns a residual correction that runs asynchronously alongside the base policy, yet applies it without uncertainty conditioning, lacking any mechanism to modulate correction magnitude across action dimensions.
18	In short, no existing method performs inference-time action correction conditioned on \emph{structured, per-degree-of-freedom uncertainty}.
19	
20	% Para 3: Our insight — per-DOF conformal features as continuous input to learned correction
21	Our key observation is that the stochastic samples already produced by a flow-matching VLA contain rich, structured uncertainty information that current methods discard.
22	By fitting a shrinkage-regularized Gaussian to $K{=}10$ samples and computing multivariate conformal statistics~\cite{braun2025cgs}, we obtain a 40-dimensional feature vector that encodes \emph{which} action dimensions are uncertain (per-DOF standard deviations), the \emph{calibrated confidence level} (conformal radii from Adaptive Conformal Inference~\cite{gibbs2021aci}), and the \emph{overall predictive spread} (log-volume of the covariance ellipsoid).
23	This representation captures substantially more structure than the scalar distances used in ReconVLA~\cite{chen2026reconvla}: it preserves the cross-DOF covariance structure that enables a downstream module to correct high-uncertainty dimensions aggressively while leaving confident predictions untouched.
24	A controlled 3D point-reaching experiment confirms this: a correction MLP conditioned on per-DOF uncertainty reduces total error by 6.7\% over scalar conditioning and by 16.7\% over no uncertainty input, with 22--24\% improvements concentrated on the non-perturbed axes where scalar conditioning cannot distinguish signal from noise (Section~\ref{sec:motivating}).
25	
26	% Para 4: ACR-VLA overview — 3 components, key design choices
27	We introduce \textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that attaches to any frozen flow-matching VLA and performs dimension-selective action correction.
28	ACR-VLA comprises three components:
29	(i)~\textbf{Conformalized Gaussian Scoring (CGS)} draws $K{=}10$ samples per control step, fits a Ledoit--Wolf shrinkage covariance, and extracts a 40D structured uncertainty feature;
30	(ii)~\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency (ACI+COC)} maintains an online conformal threshold~\cite{gibbs2021aci} using a self-referential coverage signal derived from overlapping action chunks---requiring no external supervisor, reward model, or ground-truth actions;
31	(iii)~\textbf{Conformal Refinement Module (CRM)}, a lightweight MLP (${\sim}$337K parameters) that takes the CGS features as conditioning and outputs a dimension-selective residual correction.
32	We note that conformal prediction serves here as a \emph{feature extraction and calibration mechanism}, not as a guarantee on the corrected output: CGS features provide structured uncertainty conditioning for CRM, while ACI+COC adapts these features online under distribution shift.
33	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
34	
35	% Para 5: Contributions — numbered list
36	Our contributions are:
37	\begin{enumerate}[leftmargin=*,nosep]
38	  \item \textbf{Per-DOF conformal features for dimension-selective correction.}
39	  We show that the 40D CGS representation---per-DOF standard deviations, calibrated conformal radii, and covariance log-volume---enables CRM to selectively correct uncertain action dimensions while preserving accurate ones.
40	  On LIBERO, ACR-VLA improves base SmolVLA success by \textbf{XX.X}\,pp, and ablations confirm that per-DOF features outperform both scalar uncertainty and no-uncertainty baselines (Section~\ref{sec:experiments}).
41	
42	  \item \textbf{Self-referential online calibration via Chunk Overlap Consistency.}
43	  COC exploits the temporal overlap in receding-horizon action chunks to provide a coverage signal for ACI without external supervision.
44	  This enables the conformal threshold to adapt online under arbitrary distribution shift, maintaining calibrated uncertainty features throughout deployment (Section~\ref{sec:aci}).
45	
46	  \item \textbf{Systematic evaluation across multiple LIBERO task suites.}
47	  We evaluate ACR-VLA on LIBERO-Spatial and LIBERO-Object, providing per-task breakdowns, ablations isolating the contribution of each component (CGS features, ACI+COC calibration, CRM architecture), and analysis of when and why dimension-selective correction helps (Section~\ref{sec:experiments}).
48	\end{enumerate}
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "4feb2fac-464a-46ca-9017-32af9f8c8060",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% Para 1: Problem — VLA success + robustness gap under distribution shift\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla} have reached 97--99\\% success rates on standard manipulation benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet this near-saturation masks a fragile reality: under distribution shifts common in real-world deployment---camera viewpoint changes, lighting variation, sensor noise, object layout differences---the same policies suffer substantial performance degradation~\\cite{fei2025liberoplus}.\nClosing this robustness gap is a prerequisite for deploying learned manipulation policies outside tightly controlled lab settings.\n\n% Para 2: Existing approaches — training-time vs inference-time, what they miss\nTwo lines of work address VLA robustness.\n\\emph{Training-time methods} improve the base policy itself: SRPO~\\cite{srpo2025} applies self-referential policy optimization, while RobustVLA~\\cite{robustvla2025} and DiG-Flow~\\cite{digflow2025} incorporate robustness-aware objectives into training.\nThese methods are effective but require retraining or fine-tuning, and their gains are bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen and intervene at deployment.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean, using scalar Euclidean distance as an uncertainty proxy.\nSAFE~\\cite{gu2025safe} detects anomalous states and triggers fallback behaviors.\nUPS~\\cite{yuan2026ups} and CP-in-the-Loop~\\cite{wang2025cploop} use conformal prediction for binary decisions---execute or abstain, safe or unsafe---but do not use conformal statistics as features for continuous correction.\nA2C2~\\cite{a2c2_2025} learns a residual correction that runs asynchronously alongside the base policy, yet applies it without uncertainty conditioning, lacking any mechanism to modulate correction magnitude across action dimensions.\nIn short, no existing method performs inference-time action correction conditioned on \\emph{structured, per-degree-of-freedom uncertainty}.\n\n% Para 3: Our insight — per-DOF conformal features as continuous input to learned correction\nOur key observation is that the stochastic samples already produced by a flow-matching VLA contain rich, structured uncertainty information that current methods discard.\nBy fitting a shrinkage-regularized Gaussian to $K{=}10$ samples and computing multivariate conformal statistics~\\cite{braun2025cgs}, we obtain a 40-dimensional feature vector that encodes \\emph{which} action dimensions are uncertain (per-DOF standard deviations), the \\emph{calibrated confidence level} (conformal radii from Adaptive Conformal Inference~\\cite{gibbs2021aci}), and the \\emph{overall predictive spread} (log-volume of the covariance ellipsoid).\nThis representation captures substantially more structure than the scalar distances used in ReconVLA~\\cite{chen2026reconvla}: it preserves the cross-DOF covariance structure that enables a downstream module to correct high-uncertainty dimensions aggressively while leaving confident predictions untouched.\nA controlled 3D point-reaching experiment confirms this: a correction MLP conditioned on per-DOF uncertainty reduces total error by 6.7\\% over scalar conditioning and by 16.7\\% over no uncertainty input, with 22--24\\% improvements concentrated on the non-perturbed axes where scalar conditioning cannot distinguish signal from noise (Section~\\ref{sec:motivating}).\n\n% Para 4: ACR-VLA overview — 3 components, key design choices\nWe introduce \\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that attaches to any frozen flow-matching VLA and performs dimension-selective action correction.\nACR-VLA comprises three components:\n(i)~\\textbf{Conformalized Gaussian Scoring (CGS)} draws $K{=}10$ samples per control step, fits a Ledoit--Wolf shrinkage covariance, and extracts a 40D structured uncertainty feature;\n(ii)~\\textbf{Adaptive Conformal Inference with Chunk Overlap Consistency (ACI+COC)} maintains an online conformal threshold~\\cite{gibbs2021aci} using a self-referential coverage signal derived from overlapping action chunks---requiring no external supervisor, reward model, or ground-truth actions;\n(iii)~\\textbf{Conformal Refinement Module (CRM)}, a lightweight MLP (${\\sim}$337K parameters) that takes the CGS features as conditioning and outputs a dimension-selective residual correction.\nWe note that conformal prediction serves here as a \\emph{feature extraction and calibration mechanism}, not as a guarantee on the corrected output: CGS features provide structured uncertainty conditioning for CRM, while ACI+COC adapts these features online under distribution shift.\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\n\n% Para 5: Contributions — numbered list\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{Per-DOF conformal features for dimension-selective correction.}\n  We show that the 40D CGS representation---per-DOF standard deviations, calibrated conformal radii, and covariance log-volume---enables CRM to selectively correct uncertain action dimensions while preserving accurate ones.\n  On LIBERO, ACR-VLA improves base SmolVLA success by \\textbf{XX.X}\\,pp, and ablations confirm that per-DOF features outperform both scalar uncertainty and no-uncertainty baselines (Section~\\ref{sec:experiments}).\n\n  \\item \\textbf{Self-referential online calibration via Chunk Overlap Consistency.}\n  COC exploits the temporal overlap in receding-horizon action chunks to provide a coverage signal for ACI without external supervision.\n  This enables the conformal threshold to adapt online under arbitrary distribution shift, maintaining calibrated uncertainty features throughout deployment (Section~\\ref{sec:aci}).\n\n  \\item \\textbf{Systematic evaluation across multiple LIBERO task suites.}\n  We evaluate ACR-VLA on LIBERO-Spatial and LIBERO-Object, providing per-task breakdowns, ablations isolating the contribution of each component (CGS features, ACI+COC calibration, CRM architecture), and analysis of when and why dimension-selective correction helps (Section~\\ref{sec:experiments}).\n\\end{enumerate}\n",
      "numLines": 49,
      "startLine": 1,
      "totalLines": 49
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01GkDVwTp6VMb9mve5ibnQKH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "5271f8b6-ace2-408d-b959-9b89a4b22ad9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NE11BqvCWjdzDYSs26znKM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5860,
      "cache_read_input_tokens": 24832,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5860
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

_source line 16 · 2026-05-15T19:35:54.154Z_

<details><summary>↩ Tool result · `toolu_01GkDVwTp6VMb9mve5ibnQKH`</summary>

```text
1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	@article{barber2023conformal,
21	    title={Conformal Prediction Beyond Exchangeability},
22	    author={Rina Foygel Barber and Emmanuel J. Cand{\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},
23	    journal={Annals of Statistics},
24	    volume={51},
25	    number={2},
26	    pages={816--845},
27	    year={2023}
28	}
29	
30	@misc{black2024pi0,
31	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
32	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
33	    year={2024},
34	    eprint={2410.24164},
35	    archivePrefix={arXiv},
36	    primaryClass={cs.RO}
37	}
38	
39	@misc{braun2025cgs,
40	    title={Multivariate Standardized Residuals for Conformal Prediction},
41	    author={Sacha Braun and Eug{\`e}ne Berta and Michael I. Jordan and Francis Bach},
42	    year={2025},
43	    eprint={2507.20941},
44	    archivePrefix={arXiv},
45	    primaryClass={stat.ML}
46	}
47	
48	@misc{brohan2023rt2,
49	    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
50	    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},
51	    year={2023},
52	    eprint={2307.15818},
53	    archivePrefix={arXiv},
54	    primaryClass={cs.RO}
55	}
56	
57	@misc{chen2026reconvla,
58	    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},
59	    author={Lingling Chen and Zongyao Lyu and William J. Beksi},
60	    year={2026},
61	    eprint={2604.16677},
62	    archivePrefix={arXiv},
63	    primaryClass={cs.RO}
64	}
65	
66	@misc{cosmos_policy_2026,
67	    title={Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning},
68	    author={Moo Jin Kim and Yihuai Gao and Tsung-Yi Lin and Yen-Chen Lin and Yunhao Ge and Grace Lam and Percy Liang and Shuran Song and Ming-Yu Liu and Chelsea Finn and Jinwei Gu},
69	    year={2026},
70	    eprint={2601.16163},
71	    archivePrefix={arXiv},
72	    primaryClass={cs.AI}
73	}
74	
75	@misc{digflow2025,
76	    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},
77	    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},
78	    year={2025},
79	    eprint={2512.01715},
80	    archivePrefix={arXiv},
81	    primaryClass={cs.RO}
82	}
83	
84	@misc{fei2025liberoplus,
85	    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},
86	    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},
87	    year={2025},
88	    eprint={2510.13626},
89	    archivePrefix={arXiv},
90	    primaryClass={cs.RO}
91	}
92	
93	@inproceedings{gal2016dropout,
94	    title={Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
95	    author={Yarin Gal and Zoubin Ghahramani},
96	    booktitle={International Conference on Machine Learning (ICML)},
97	    year={2016}
98	}
99	
100	@misc{ghosh2024octo,
101	    title={Octo: An Open-Source Generalist Robot Policy},
102	    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},
103	    year={2024},
104	    eprint={2405.12213},
105	    archivePrefix={arXiv},
106	    primaryClass={cs.RO}
107	}
108	
109	@inproceedings{gibbs2021aci,
110	    title={Adaptive Conformal Inference Under Distribution Shift},
111	    author={Isaac Gibbs and Emmanuel Cand{\`e}s},
112	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
113	    year={2021}
114	}
115	
116	@inproceedings{gu2025safe,
117	    title={SAFE: Multitask Failure Detection for Vision-Language-Action Models},
118	    author={Qiao Gu and Yuanliang Ju and Shengxiang Sun and Igor Gilitschenski and Haruki Nishimura and Masha Itkina and Florian Shkurti},
119	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
120	    year={2025}
121	}
122	
123	@misc{kim2024openvla,
124	    title={OpenVLA: An Open-Source Vision-Language-Action Model},
125	    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},
126	    year={2024},
127	    eprint={2406.09246},
128	    archivePrefix={arXiv},
129	    primaryClass={cs.RO}
130	}
131	
132	@inproceedings{lakshminarayanan2017ensembles,
133	    title={Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
134	    author={Balaji Lakshminarayanan and Alexander Pritzel and Charles Blundell},
135	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
136	    year={2017}
137	}
138	
139	@article{ledoit2004well,
140	    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},
141	    author={Olivier Ledoit and Michael Wolf},
142	    journal={Journal of Multivariate Analysis},
143	    volume={88},
144	    number={2},
145	    pages={365--411},
146	    year={2004}
147	}
148	
149	@inproceedings{lipman2023flow,
150	    title={Flow Matching for Generative Modeling},
151	    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},
152	    booktitle={International Conference on Learning Representations (ICLR)},
153	    year={2023}
154	}
155	
156	@inproceedings{liu2023libero,
157	    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
158	    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},
159	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
160	    year={2023}
161	}
162	
163	@misc{liu2026ttvla,
164	    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},
165	    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},
166	    year={2026},
167	    eprint={2601.06748},
168	    archivePrefix={arXiv},
169	    primaryClass={cs.RO}
170	}
171	
172	@misc{luan2026snapflow,
173	    title={SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation},
174	    author={Wuyang Luan and Junhui Li and Weiguang Zhao and Wenjian Zhang and Tieru Wu and Rui Ma},
175	    year={2026},
176	    eprint={2604.05656},
177	    archivePrefix={arXiv},
178	    primaryClass={cs.RO}
179	}
180	
181	@misc{robustvla2025,
182	    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},
183	    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},
184	    year={2025},
185	    eprint={2511.01331},
186	    archivePrefix={arXiv},
187	    primaryClass={cs.RO}
188	}
189	
190	@inproceedings{romano2019cqr,
191	    title={Conformalized Quantile Regression},
192	    author={Yaniv Romano and Evan Patterson and Emmanuel J. Cand{\`e}s},
193	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
194	    year={2019}
195	}
196	
197	@article{shafer2008tutorial,
198	    title={A Tutorial on Conformal Prediction},
199	    author={Glenn Shafer and Vladimir Vovk},
200	    journal={Journal of Machine Learning Research},
201	    volume={9},
202	    pages={371--421},
203	    year={2008}
204	}
205	
206	@misc{shukor2025smolvla,
207	    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},
208	    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},
209	    year={2025},
210	    eprint={2506.01844},
211	    archivePrefix={arXiv},
212	    primaryClass={cs.RO}
213	}
214	
215	@misc{srpo2025,
216	    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},
217	    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},
218	    year={2025},
219	    eprint={2511.15605},
220	    archivePrefix={arXiv},
221	    primaryClass={cs.RO}
222	}
223	
224	@misc{vla_gse_2026,
225	    title={VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts},
226	    author={Yuhua Jiang and Junjie Lu and Xinyao Qin and Xiaoyu Chen and Kaixin Wang and Feifei Gao and Li Zhao},
227	    year={2026},
228	    eprint={2605.06175},
229	    archivePrefix={arXiv},
230	    primaryClass={cs.RO}
231	}
232	
233	@misc{wang2025cploop,
234	    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},
235	    author={Han Wang and Chao Ning},
236	    year={2025},
237	    eprint={2510.16376},
238	    archivePrefix={arXiv},
239	    primaryClass={cs.RO}
240	}
241	
242	@misc{xing2026diu,
243	    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},
244	    author={Jiarui Xing and Song Wang and Jian Wang},
245	    year={2026},
246	    eprint={2605.00941},
247	    archivePrefix={arXiv},
248	    primaryClass={cs.LG}
249	}
250	
251	@misc{yuan2026ups,
252	    title={When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering},
253	    author={Jessie Yuan and Yilin Wu and Andrea Bajcsy},
254	    year={2026},
255	    eprint={2602.22474},
256	    archivePrefix={arXiv},
257	    primaryClass={cs.RO}
258	}
259	
260	@inproceedings{chi2023diffusion_policy,
261	    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
262	    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},
263	    booktitle={Robotics: Science and Systems (RSS)},
264	    year={2023},
265	    note={Also published in IJRR 2024. arXiv:2303.04137}
266	}
267	
268	@inproceedings{zhao2024conformalized,
269	    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},
270	    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},
271	    booktitle={Robotics: Science and Systems (RSS)},
272	    year={2024}
273	}
274	
275	@inproceedings{silver2018residual,
276	    title={Residual Policy Learning},
277	    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},
278	    booktitle={Robotics: Science and Systems (RSS)},
279	    year={2018},
280	    note={arXiv:1812.06298}
281	}
282	
283	@inproceedings{jiang2024transic,
284	    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},
285	    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},
286	    booktitle={Conference on Robot Learning (CoRL)},
287	    year={2024},
288	    note={arXiv:2405.10315}
289	}
290	
291	@inproceedings{xiao2026pld,
292	    title={PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning},
293	    author={Tong Xiao and Disheng Liu and Wen Jiang and Guanjun Wu and Jiaming Liu and Bin Zhao and Zhigang Wang and Xuelong Li},
294	    booktitle={International Conference on Learning Representations (ICLR)},
295	    year={2026},
296	    note={arXiv:2511.00091}
297	}
298	
299	@misc{pan2025drc,
300	    title={DRC: Decaying Relative Correction for Policy Refinement},
301	    author={Xinjie Pan and Ruizhe Shi and Dongjie Yu and Zhiyuan Nan and Xiaowei Hu and Muxin Wei and Pengfei Li and Xin Li and Zhixiang Wang and Liang Gao and Xue Liu},
302	    year={2025},
303	    eprint={2503.15368},
304	    archivePrefix={arXiv},
305	    primaryClass={cs.RO}
306	}
307	
308	@inproceedings{zhou2025acp_cbf,
309	    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},
310	    author={Zetian Zhou and Shuo Yang and Wenhao Luo},
311	    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
312	    year={2025},
313	    note={arXiv:2503.17678}
314	}
315	
316	@misc{zollo2025vla_calibration,
317	    title={Confidence Calibration in Vision-Language-Action Models},
318	    author={Matteo Zollo and Richard Zemel},
319	    year={2025},
320	    eprint={2507.17383},
321	    archivePrefix={arXiv},
322	    primaryClass={cs.RO}
323	}
324	
325	@inproceedings{ross2011dagger,
326	    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},
327	    author={St{\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},
328	    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},
329	    year={2011}
330	}
331	
332	@misc{tang2026shifting,
333	    title={Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model},
334	    author={Yanchuan Tang and Taowen Wang and Yuefei Chen and Boxuan Zhang and Qiang Guan and Ruixiang Tang},
335	    year={2026},
336	    eprint={2603.18342},
337	    archivePrefix={arXiv},
338	    primaryClass={cs.RO}
339	}
340	
341	@misc{liu2026scvla,
342	    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},
343	    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},
344	    year={2026},
345	    eprint={2602.21633},
346	    archivePrefix={arXiv},
347	    primaryClass={cs.RO}
348	}
349	
350	@misc{li2025vlapilot,
351	    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},
352	    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},
353	    year={2025},
354	    eprint={2511.14178},
355	    archivePrefix={arXiv},
356	    primaryClass={cs.RO}
357	}
358	
359	@inproceedings{zhong2026acotvla,
360	    title={ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models},
361	    author={Linqing Zhong and Yi Liu and Yifei Wei and Ziyu Xiong and Maoqing Yao and Si Liu and Guanghui Ren},
362	    year={2026},
363	    eprint={2601.11404},
364	    archivePrefix={arXiv},
365	    primaryClass={cs.RO},
366	    booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}
367	}
368	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "fe970050-2786-4da1-94b8-94cd98e077c3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib",
      "content": "@misc{a2c2_2025,\n    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},\n    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},\n    year={2025},\n    eprint={2509.23224},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@article{angelopoulos2023gentle,\n    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n    author={Anastasios N. Angelopoulos and Stephen Bates},\n    journal={Foundations and Trends in Machine Learning},\n    year={2023},\n    eprint={2107.07511},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@article{barber2023conformal,\n    title={Conformal Prediction Beyond Exchangeability},\n    author={Rina Foygel Barber and Emmanuel J. Cand{\\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},\n    journal={Annals of Statistics},\n    volume={51},\n    number={2},\n    pages={816--845},\n    year={2023}\n}\n\n@misc{black2024pi0,\n    title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},\n    year={2024},\n    eprint={2410.24164},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{braun2025cgs,\n    title={Multivariate Standardized Residuals for Conformal Prediction},\n    author={Sacha Braun and Eug{\\`e}ne Berta and Michael I. Jordan and Francis Bach},\n    year={2025},\n    eprint={2507.20941},\n    archivePrefix={arXiv},\n    primaryClass={stat.ML}\n}\n\n@misc{brohan2023rt2,\n    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},\n    year={2023},\n    eprint={2307.15818},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{chen2026reconvla,\n    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},\n    author={Lingling Chen and Zongyao Lyu and William J. Beksi},\n    year={2026},\n    eprint={2604.16677},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{cosmos_policy_2026,\n    title={Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning},\n    author={Moo Jin Kim and Yihuai Gao and Tsung-Yi Lin and Yen-Chen Lin and Yunhao Ge and Grace Lam and Percy Liang and Shuran Song and Ming-Yu Liu and Chelsea Finn and Jinwei Gu},\n    year={2026},\n    eprint={2601.16163},\n    archivePrefix={arXiv},\n    primaryClass={cs.AI}\n}\n\n@misc{digflow2025,\n    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},\n    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},\n    year={2025},\n    eprint={2512.01715},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{fei2025liberoplus,\n    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},\n    year={2025},\n    eprint={2510.13626},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gal2016dropout,\n    title={Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n    author={Yarin Gal and Zoubin Ghahramani},\n    booktitle={International Conference on Machine Learning (ICML)},\n    year={2016}\n}\n\n@misc{ghosh2024octo,\n    title={Octo: An Open-Source Generalist Robot Policy},\n    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},\n    year={2024},\n    eprint={2405.12213},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gibbs2021aci,\n    title={Adaptive Conformal Inference Under Distribution Shift},\n    author={Isaac Gibbs and Emmanuel Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2021}\n}\n\n@inproceedings{gu2025safe,\n    title={SAFE: Multitask Failure Detection for Vision-Language-Action Models},\n    author={Qiao Gu and Yuanliang Ju and Shengxiang Sun and Igor Gilitschenski and Haruki Nishimura and Masha Itkina and Florian Shkurti},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2025}\n}\n\n@misc{kim2024openvla,\n    title={OpenVLA: An Open-Source Vision-Language-Action Model},\n    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},\n    year={2024},\n    eprint={2406.09246},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n    title={Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n    author={Balaji Lakshminarayanan and Alexander Pritzel and Charles Blundell},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2017}\n}\n\n@article{ledoit2004well,\n    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},\n    author={Olivier Ledoit and Michael Wolf},\n    journal={Journal of Multivariate Analysis},\n    volume={88},\n    number={2},\n    pages={365--411},\n    year={2004}\n}\n\n@inproceedings{lipman2023flow,\n    title={Flow Matching for Generative Modeling},\n    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2023}\n}\n\n@inproceedings{liu2023libero,\n    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2023}\n}\n\n@misc{liu2026ttvla,\n    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},\n    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},\n    year={2026},\n    eprint={2601.06748},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{luan2026snapflow,\n    title={SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation},\n    author={Wuyang Luan and Junhui Li and Weiguang Zhao and Wenjian Zhang and Tieru Wu and Rui Ma},\n    year={2026},\n    eprint={2604.05656},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{robustvla2025,\n    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},\n    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},\n    year={2025},\n    eprint={2511.01331},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{romano2019cqr,\n    title={Conformalized Quantile Regression},\n    author={Yaniv Romano and Evan Patterson and Emmanuel J. Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2019}\n}\n\n@article{shafer2008tutorial,\n    title={A Tutorial on Conformal Prediction},\n    author={Glenn Shafer and Vladimir Vovk},\n    journal={Journal of Machine Learning Research},\n    volume={9},\n    pages={371--421},\n    year={2008}\n}\n\n@misc{shukor2025smolvla,\n    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},\n    year={2025},\n    eprint={2506.01844},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{srpo2025,\n    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},\n    year={2025},\n    eprint={2511.15605},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{vla_gse_2026,\n    title={VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts},\n    author={Yuhua Jiang and Junjie Lu and Xinyao Qin and Xiaoyu Chen and Kaixin Wang and Feifei Gao and Li Zhao},\n    year={2026},\n    eprint={2605.06175},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{wang2025cploop,\n    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},\n    author={Han Wang and Chao Ning},\n    year={2025},\n    eprint={2510.16376},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{xing2026diu,\n    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},\n    author={Jiarui Xing and Song Wang and Jian Wang},\n    year={2026},\n    eprint={2605.00941},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@misc{yuan2026ups,\n    title={When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering},\n    author={Jessie Yuan and Yilin Wu and Andrea Bajcsy},\n    year={2026},\n    eprint={2602.22474},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{chi2023diffusion_policy,\n    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2023},\n    note={Also published in IJRR 2024. arXiv:2303.04137}\n}\n\n@inproceedings{zhao2024conformalized,\n    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},\n    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2024}\n}\n\n@inproceedings{silver2018residual,\n    title={Residual Policy Learning},\n    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2018},\n    note={arXiv:1812.06298}\n}\n\n@inproceedings{jiang2024transic,\n    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},\n    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},\n    booktitle={Conference on Robot Learning (CoRL)},\n    year={2024},\n    note={arXiv:2405.10315}\n}\n\n@inproceedings{xiao2026pld,\n    title={PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning},\n    author={Tong Xiao and Disheng Liu and Wen Jiang and Guanjun Wu and Jiaming Liu and Bin Zhao and Zhigang Wang and Xuelong Li},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2026},\n    note={arXiv:2511.00091}\n}\n\n@misc{pan2025drc,\n    title={DRC: Decaying Relative Correction for Policy Refinement},\n    author={Xinjie Pan and Ruizhe Shi and Dongjie Yu and Zhiyuan Nan and Xiaowei Hu and Muxin Wei and Pengfei Li and Xin Li and Zhixiang Wang and Liang Gao and Xue Liu},\n    year={2025},\n    eprint={2503.15368},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhou2025acp_cbf,\n    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},\n    author={Zetian Zhou and Shuo Yang and Wenhao Luo},\n    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n    year={2025},\n    note={arXiv:2503.17678}\n}\n\n@misc{zollo2025vla_calibration,\n    title={Confidence Calibration in Vision-Language-Action Models},\n    author={Matteo Zollo and Richard Zemel},\n    year={2025},\n    eprint={2507.17383},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{ross2011dagger,\n    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},\n    author={St{\\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},\n    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},\n    year={2011}\n}\n\n@misc{tang2026shifting,\n    title={Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model},\n    author={Yanchuan Tang and Taowen Wang and Yuefei Chen and Boxuan Zhang and Qiang Guan and Ruixiang Tang},\n    year={2026},\n    eprint={2603.18342},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{liu2026scvla,\n    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},\n    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},\n    year={2026},\n    eprint={2602.21633},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{li2025vlapilot,\n    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},\n    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},\n    year={2025},\n    eprint={2511.14178},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhong2026acotvla,\n    title={ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models},\n    author={Linqing Zhong and Yi Liu and Yifei Wei and Ziyu Xiong and Maoqing Yao and Si Liu and Guanghui Ren},\n    year={2026},\n    eprint={2601.11404},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO},\n    booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}\n}\n",
      "numLines": 368,
      "startLine": 1,
      "totalLines": 368
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
Now I have all the context I need. Let me also check the method section to understand more about the ACR-VLA system for accurate positioning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "702dca3f-6fc3-40ed-8442-b71726ae84aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCyhcVx9JW3zuibX5tzZ5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9987,
      "cache_read_input_tokens": 30692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9987
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

Let me also check the method section for precise technical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "c86c3b31-f5b7-4a7e-a502-40fda646b71a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCyhcVx9JW3zuibX5tzZ5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9987,
      "cache_read_input_tokens": 30692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9987
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

<details open><summary>🔧 Tool call — Read · `toolu_01ER1FVmfFrrS8o8CVf51189`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "21caede4-85bb-4eec-b4ee-d6a09e2184ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VCyhcVx9JW3zuibX5tzZ5p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9987,
      "cache_read_input_tokens": 30692,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9987
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

_source line 20 · 2026-05-15T19:35:59.477Z_

<details><summary>↩ Tool result · `toolu_01ER1FVmfFrrS8o8CVf51189`</summary>

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
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "c5903611-2150-430f-be1a-6eef6d80696c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis is a simplified selection baseline inspired by the conformal selection frontend of ReconVLA~\\cite{chen2026reconvla}, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring to isolate the effect of the downstream correction module. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 3-layer MLP with input normalization (input$\\to$256$\\to$256$\\to$30; 329K parameters for the primary obs\\_only variant).\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.",
      "numLines": 80,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper's technical content and positioning. Let me write the Related Work section according to the specified structure with the 4 subsections. Key things to note:

1. The current method section reveals that CRM is actually observation-only (doesn't use per-DOF conformal features) - this is a design choice. The conformal scoring is used for selection, not correction conditioning.

2. I need to be careful about:
   - ReconVLA: describe as conformal prediction method, not "scalar Euclidean distance"
   - The argmin baseline is "a simplified selection baseline inspired by ReconVLA's conformal selection frontend"
   - ACR-VLA uses CP for selection stage, not claiming coverage guarantees for corrected output
   - CRM is supervised offline training (L2 loss), not RL
   - The negative result on per-DOF conformal features as CRM input

3. Only use the specified cite keys.

Let me now write the section following the 4-subsection structure requested.

I'm organizing the experimental setup into four subsections to clearly delineate the baselines, our method's components, and the training procedures, making sure to cite only the specified sources.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "87537cb4-6779-4afb-a73a-3b94afc9d641",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EEkpXk1rYEkcY5j8F3B4qS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2791,
      "cache_read_input_tokens": 40679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2791
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

Now I have full context. Writing the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "ae33c590-0b29-41d0-a8a9-e1128f733fbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EEkpXk1rYEkcY5j8F3B4qS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2791,
      "cache_read_input_tokens": 40679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2791
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

<details open><summary>🔧 Tool call — Write · `toolu_01YHzQNeHrbnutnc5AwYVTzX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own rollouts as training signal.\nDiG-Flow~\\cite{digflow2025} regularizes the flow-matching denoising trajectory via a discrepancy-guided objective.\nTT-VLA~\\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.\nA shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} uses conformal prediction over multiple VLA samples for action selection and failure detection, providing a principled uncertainty-aware framework that operates without retraining.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\\,s per control step---prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.\n\nACR-VLA occupies a specific point in this design space: inference-time, plug-and-play (no retraining of the base VLA), and combining conformal selection with learned correction.\nSelection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.\nCorrection alone (as in A2C2) lacks a mechanism to identify a good starting point.\nACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.\n\n\\subsection{Conformal Prediction in Robotics}\n\nConformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\\cite{angelopoulos2023gentle}.\nFor multivariate outputs, Braun et al.~\\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.\n\nIn robotics, CP has been applied to several safety-critical settings.\nConformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.\nCP-in-the-Loop~\\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.\nACP+CBF~\\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.\nA common pattern across these methods is that CP serves as a \\emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.\n\nACR-VLA uses conformal statistics (Mahalanobis scores, per-DOF standard deviations, covariance log-volume) in its selection stage, but does \\emph{not} claim formal coverage guarantees for the corrected output.\nCP serves here as a scoring and feature extraction mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure informs the per-DOF uncertainty representation.\nThe downstream correction module then operates on the selected action conditioned on observations, producing a refined action whose relationship to the original conformal region is no longer governed by coverage theory.\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy.\nSubsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} introduces a scheduled magnitude bound $\\xi$ for residual RL on VLAs, progressively increasing the allowed correction range during training.\nDRC~\\cite{pan2025drc} applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones.\n\nMagnitude control is the key connection to ACR-VLA: Silver et al.\\ use residual scaling, TRANSIC uses binary gating, PLD uses scheduling, DRC uses temporal decay.\nACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nWe view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.\nA second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.\n\n\\subsection{Uncertainty Quantification for VLAs}\n\nRecent work has developed UQ methods tailored to VLA architectures.\nDiU~\\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.\nSAFE~\\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected.\nZollo and Zemel~\\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.\n\nACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.\nThe multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.\nFunctionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\\cite{zollo2025vla_calibration} targets confidence reliability.\nOur ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "04743ad4-00a3-4ef2-8288-d0befcd3da9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EEkpXk1rYEkcY5j8F3B4qS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2791,
      "cache_read_input_tokens": 40679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2791
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

_source line 24 · 2026-05-15T19:36:57.991Z_

<details><summary>↩ Tool result · `toolu_01YHzQNeHrbnutnc5AwYVTzX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "6d6bc26a-768f-4fa0-9633-88458eb3a025",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own rollouts as training signal.\nDiG-Flow~\\cite{digflow2025} regularizes the flow-matching denoising trajectory via a discrepancy-guided objective.\nTT-VLA~\\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.\nA shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} uses conformal prediction over multiple VLA samples for action selection and failure detection, providing a principled uncertainty-aware framework that operates without retraining.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\\,s per control step---prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.\n\nACR-VLA occupies a specific point in this design space: inference-time, plug-and-play (no retraining of the base VLA), and combining conformal selection with learned correction.\nSelection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.\nCorrection alone (as in A2C2) lacks a mechanism to identify a good starting point.\nACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.\n\n\\subsection{Conformal Prediction in Robotics}\n\nConformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\\cite{angelopoulos2023gentle}.\nFor multivariate outputs, Braun et al.~\\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.\n\nIn robotics, CP has been applied to several safety-critical settings.\nConformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.\nCP-in-the-Loop~\\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.\nACP+CBF~\\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.\nA common pattern across these methods is that CP serves as a \\emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.\n\nACR-VLA uses conformal statistics (Mahalanobis scores, per-DOF standard deviations, covariance log-volume) in its selection stage, but does \\emph{not} claim formal coverage guarantees for the corrected output.\nCP serves here as a scoring and feature extraction mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure informs the per-DOF uncertainty representation.\nThe downstream correction module then operates on the selected action conditioned on observations, producing a refined action whose relationship to the original conformal region is no longer governed by coverage theory.\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy.\nSubsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} introduces a scheduled magnitude bound $\\xi$ for residual RL on VLAs, progressively increasing the allowed correction range during training.\nDRC~\\cite{pan2025drc} applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones.\n\nMagnitude control is the key connection to ACR-VLA: Silver et al.\\ use residual scaling, TRANSIC uses binary gating, PLD uses scheduling, DRC uses temporal decay.\nACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nWe view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.\nA second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.\n\n\\subsection{Uncertainty Quantification for VLAs}\n\nRecent work has developed UQ methods tailored to VLA architectures.\nDiU~\\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.\nSAFE~\\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected.\nZollo and Zemel~\\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.\n\nACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.\nThe multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.\nFunctionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\\cite{zollo2025vla_calibration} targets confidence reliability.\nOur ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 43,
        "newStart": 1,
        "newLines": 64,
        "lines": [
          "-\\section{Related Work}",
          "-\\label{sec:related}",
          "+\\section{Related Work}\\label{sec:related_work}",
          " ",
          "-\\paragraph{VLA Robustness Methods.}",
          "-Recent work has sought to improve the robustness of vision-language-action models through training-time interventions.",
          "-SRPO~\\cite{srpo2025} applies self-referential reinforcement learning to fine-tune VLA policies, achieving strong gains on the LIBERO-Plus benchmark.",
          "+\\subsection{VLA Robustness}",
          "+",
          "+Methods for improving VLA robustness divide into training-time and inference-time approaches.",
          "+",
          "+\\paragraph{Training-time methods.}",
          " RobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.",
          "-DiG-Flow~\\cite{digflow2025} introduces discrepancy-guided flow matching, steering the generative process toward more accurate denoising trajectories during training.",
          "-SnapFlow~\\cite{luan2026snapflow} distills multi-step flow-matching into single-step inference, reducing latency while preserving action quality.",
          "-TT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time via reinforcement learning, blurring the line between training-time and inference-time approaches.",
          "-VLA-GSE~\\cite{vla_gse_2026} improves generalization through parameter-efficient fine-tuning with gated sparse experts, and Cosmos-Policy~\\cite{cosmos_policy_2026} leverages video foundation models for visuomotor control.",
          "-These methods are complementary to ACR-VLA: they improve the base policy itself, whereas ACR-VLA operates as a post-hoc inference-time module that attaches to any frozen flow-matching VLA without modifying its weights.",
          "-This orthogonality means ACR-VLA can be composed with any of the above methods to provide additional robustness through uncertainty-conditioned correction.",
          "+SRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own rollouts as training signal.",
          "+DiG-Flow~\\cite{digflow2025} regularizes the flow-matching denoising trajectory via a discrepancy-guided objective.",
          "+TT-VLA~\\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.",
          "+A shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.",
          " ",
          "-\\paragraph{Uncertainty Quantification for Robot Learning.}",
          "-Quantifying predictive uncertainty in learned policies is essential for safe deployment.",
          "-Deep Ensembles~\\cite{lakshminarayanan2017ensembles} and MC-Dropout~\\cite{gal2016dropout} are foundational approaches that estimate epistemic uncertainty through multiple forward passes or stochastic weight perturbations, but both produce scalar or loosely structured uncertainty estimates that do not distinguish which action dimensions are uncertain.",
          "-In the generative policy setting, Diffusion Policy~\\cite{chi2023diffusion_policy} introduced the diffusion-based action generation paradigm that flow-matching VLAs build upon; its stochastic sampling naturally admits multi-sample uncertainty estimation, though the original work does not exploit this for correction.",
          "-DiU~\\cite{xing2026diu} shows that for flow-matching models, the divergence of the velocity field recovers per-DOF \\emph{aleatoric} uncertainty from a single forward pass, providing an efficient uncertainty signal without additional sampling.",
          "-ACR-VLA differs along two axes.",
          "-First, it estimates \\emph{model uncertainty} via multi-sample covariance---a sampling-based signal that reflects both epistemic and aleatoric components, and that rises under distribution shift when the policy is uncertain about the correct action---which we find more actionable for correction than single-pass aleatoric estimates (validated in ablation A7).",
          "-Second, it produces a structured 40-dimensional feature vector (per-DOF standard deviations, calibrated conformal radii, and log-volume) rather than a scalar summary, enabling dimension-selective correction as demonstrated in Section~\\ref{sec:motivating}.",
          "+\\paragraph{Inference-time methods.}",
          "+ReconVLA~\\cite{chen2026reconvla} uses conformal prediction over multiple VLA samples for action selection and failure detection, providing a principled uncertainty-aware framework that operates without retraining.",
          "+SC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.",
          "+VLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\\,s per control step---prohibitive for real-time manipulation.",
          "+A2C2~\\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.",
          " ",
          "-\\paragraph{Conformal Prediction in Robotics.}",
          "-Conformal prediction (CP) provides distribution-free coverage guarantees and has seen growing adoption in robotics.",
          "-\\citet{angelopoulos2023gentle} provide a comprehensive tutorial on the framework.",
          "-Conformalized Quantile Regression~\\cite{romano2019cqr} extends CP to heteroscedastic settings, while Adaptive Conformal Inference~\\cite{gibbs2021aci} maintains coverage under distribution shift through online threshold updates---a property critical for non-stationary robotic environments.",
          "-\\citet{barber2023conformal} further relax the exchangeability assumption, enabling conformal methods under general temporal dependence.",
          "-Braun et al.~\\cite{braun2025cgs} introduce Conformalized Gaussian Scoring for multivariate prediction regions, which ACR-VLA builds upon for its per-DOF feature extraction.",
          "-In robotics applications, CP-in-the-Loop~\\cite{wang2025cploop} integrates conformal regions into trajectory optimization as constraints, and Conformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to provide safety guarantees during shared autonomy.",
          "-UPS~\\cite{yuan2026ups} employs CP for binary policy gating---deciding whether to execute or abstain---while SAFE~\\cite{gu2025safe} uses anomaly detection to trigger safe fallback behaviors.",
          "-A common thread in these systems is that CP serves as a \\emph{binary decision mechanism} (accept/reject, execute/abstain, safe/unsafe).",
          "-ACR-VLA departs from this paradigm by using conformal statistics as \\emph{continuous input features} to a learned correction module, enabling graded, dimension-selective refinement rather than all-or-nothing decisions.",
          "+ACR-VLA occupies a specific point in this design space: inference-time, plug-and-play (no retraining of the base VLA), and combining conformal selection with learned correction.",
          "+Selection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.",
          "+Correction alone (as in A2C2) lacks a mechanism to identify a good starting point.",
          "+ACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.",
          " ",
          "-\\paragraph{Inference-Time Action Correction.}",
          "-The most closely related line of work addresses action refinement at inference time without retraining the base policy.",
          "-A2C2~\\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's action chunk generation, reducing effective latency.",
          "-However, A2C2 applies a generic residual without uncertainty conditioning: it has no mechanism to modulate correction magnitude based on per-dimension confidence, which can lead to unnecessary perturbation of already-accurate action components.",
          "-ReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean based on scalar Euclidean distance, using this distance as a proxy for uncertainty.",
          "-While effective as a variance-reduction strategy, sample selection is fundamentally limited: it cannot synthesize an action better than any individual sample, and its scalar uncertainty measure does not distinguish which degrees of freedom are unreliable.",
          "-ACR-VLA addresses both limitations.",
          "-Compared to A2C2, it conditions correction on calibrated per-DOF conformal features, enabling the refinement module to selectively correct high-uncertainty dimensions while preserving accurate predictions on others.",
          "-Compared to ReconVLA, it performs learned synthesis rather than selection, producing corrections that can improve upon any individual sample, and replaces the scalar Euclidean proxy with a 40-dimensional structured representation that captures per-DOF variance, calibrated confidence, and distributional volume.",
          "+\\subsection{Conformal Prediction in Robotics}",
          "+",
          "+Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\\cite{angelopoulos2023gentle}.",
          "+For multivariate outputs, Braun et al.~\\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.",
          "+",
          "+In robotics, CP has been applied to several safety-critical settings.",
          "+Conformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.",
          "+CP-in-the-Loop~\\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.",
          "+ACP+CBF~\\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.",
          "+A common pattern across these methods is that CP serves as a \\emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.",
          "+",
          "+ACR-VLA uses conformal statistics (Mahalanobis scores, per-DOF standard deviations, covariance log-volume) in its selection stage, but does \\emph{not} claim formal coverage guarantees for the corrected output.",
          "+CP serves here as a scoring and feature extraction mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure informs the per-DOF uncertainty representation.",
          "+The downstream correction module then operates on the selected action conditioned on observations, producing a refined action whose relationship to the original conformal region is no longer governed by coverage theory.",
          "+",
          "+\\subsection{Residual Policy Learning}",
          "+",
          "+Residual policy learning augments a base controller with a learned additive correction.",
          "+Silver et al.~\\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy.",
          "+Subsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.",
          "+TRANSIC~\\cite{jiang2024transic} uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse.",
          "+PLD~\\cite{xiao2026pld} introduces a scheduled magnitude bound $\\xi$ for residual RL on VLAs, progressively increasing the allowed correction range during training.",
          "+DRC~\\cite{pan2025drc} applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones.",
          "+",
          "+Magnitude control is the key connection to ACR-VLA: Silver et al.\\ use residual scaling, TRANSIC uses binary gating, PLD uses scheduling, DRC uses temporal decay.",
          "+ACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).",
          "+We view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.",
          "+A second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.",
          "+",
          "+\\subsection{Uncertainty Quantification for VLAs}",
          "+",
          "+Recent work has developed UQ methods tailored to VLA architectures.",
          "+DiU~\\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.",
          "+SAFE~\\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected.",
          "+Zollo and Zemel~\\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.",
          "+",
          "+ACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.",
          "+The multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.",
          "+Functionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\\cite{zollo2025vla_calibration} targets confidence reliability.",
          "+Our ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge."
        ]
      }
    ],
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{VLA Robustness Methods.}\nRecent work has sought to improve the robustness of vision-language-action models through training-time interventions.\nSRPO~\\cite{srpo2025} applies self-referential reinforcement learning to fine-tune VLA policies, achieving strong gains on the LIBERO-Plus benchmark.\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.\nDiG-Flow~\\cite{digflow2025} introduces discrepancy-guided flow matching, steering the generative process toward more accurate denoising trajectories during training.\nSnapFlow~\\cite{luan2026snapflow} distills multi-step flow-matching into single-step inference, reducing latency while preserving action quality.\nTT-VLA~\\cite{liu2026ttvla} adapts VLA parameters at test time via reinforcement learning, blurring the line between training-time and inference-time approaches.\nVLA-GSE~\\cite{vla_gse_2026} improves generalization through parameter-efficient fine-tuning with gated sparse experts, and Cosmos-Policy~\\cite{cosmos_policy_2026} leverages video foundation models for visuomotor control.\nThese methods are complementary to ACR-VLA: they improve the base policy itself, whereas ACR-VLA operates as a post-hoc inference-time module that attaches to any frozen flow-matching VLA without modifying its weights.\nThis orthogonality means ACR-VLA can be composed with any of the above methods to provide additional robustness through uncertainty-conditioned correction.\n\n\\paragraph{Uncertainty Quantification for Robot Learning.}\nQuantifying predictive uncertainty in learned policies is essential for safe deployment.\nDeep Ensembles~\\cite{lakshminarayanan2017ensembles} and MC-Dropout~\\cite{gal2016dropout} are foundational approaches that estimate epistemic uncertainty through multiple forward passes or stochastic weight perturbations, but both produce scalar or loosely structured uncertainty estimates that do not distinguish which action dimensions are uncertain.\nIn the generative policy setting, Diffusion Policy~\\cite{chi2023diffusion_policy} introduced the diffusion-based action generation paradigm that flow-matching VLAs build upon; its stochastic sampling naturally admits multi-sample uncertainty estimation, though the original work does not exploit this for correction.\nDiU~\\cite{xing2026diu} shows that for flow-matching models, the divergence of the velocity field recovers per-DOF \\emph{aleatoric} uncertainty from a single forward pass, providing an efficient uncertainty signal without additional sampling.\nACR-VLA differs along two axes.\nFirst, it estimates \\emph{model uncertainty} via multi-sample covariance---a sampling-based signal that reflects both epistemic and aleatoric components, and that rises under distribution shift when the policy is uncertain about the correct action---which we find more actionable for correction than single-pass aleatoric estimates (validated in ablation A7).\nSecond, it produces a structured 40-dimensional feature vector (per-DOF standard deviations, calibrated conformal radii, and log-volume) rather than a scalar summary, enabling dimension-selective correction as demonstrated in Section~\\ref{sec:motivating}.\n\n\\paragraph{Conformal Prediction in Robotics.}\nConformal prediction (CP) provides distribution-free coverage guarantees and has seen growing adoption in robotics.\n\\citet{angelopoulos2023gentle} provide a comprehensive tutorial on the framework.\nConformalized Quantile Regression~\\cite{romano2019cqr} extends CP to heteroscedastic settings, while Adaptive Conformal Inference~\\cite{gibbs2021aci} maintains coverage under distribution shift through online threshold updates---a property critical for non-stationary robotic environments.\n\\citet{barber2023conformal} further relax the exchangeability assumption, enabling conformal methods under general temporal dependence.\nBraun et al.~\\cite{braun2025cgs} introduce Conformalized Gaussian Scoring for multivariate prediction regions, which ACR-VLA builds upon for its per-DOF feature extraction.\nIn robotics applications, CP-in-the-Loop~\\cite{wang2025cploop} integrates conformal regions into trajectory optimization as constraints, and Conformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to provide safety guarantees during shared autonomy.\nUPS~\\cite{yuan2026ups} employs CP for binary policy gating---deciding whether to execute or abstain---while SAFE~\\cite{gu2025safe} uses anomaly detection to trigger safe fallback behaviors.\nA common thread in these systems is that CP serves as a \\emph{binary decision mechanism} (accept/reject, execute/abstain, safe/unsafe).\nACR-VLA departs from this paradigm by using conformal statistics as \\emph{continuous input features} to a learned correction module, enabling graded, dimension-selective refinement rather than all-or-nothing decisions.\n\n\\paragraph{Inference-Time Action Correction.}\nThe most closely related line of work addresses action refinement at inference time without retraining the base policy.\nA2C2~\\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's action chunk generation, reducing effective latency.\nHowever, A2C2 applies a generic residual without uncertainty conditioning: it has no mechanism to modulate correction magnitude based on per-dimension confidence, which can lead to unnecessary perturbation of already-accurate action components.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the one closest to the sample mean based on scalar Euclidean distance, using this distance as a proxy for uncertainty.\nWhile effective as a variance-reduction strategy, sample selection is fundamentally limited: it cannot synthesize an action better than any individual sample, and its scalar uncertainty measure does not distinguish which degrees of freedom are unreliable.\nACR-VLA addresses both limitations.\nCompared to A2C2, it conditions correction on calibrated per-DOF conformal features, enabling the refinement module to selectively correct high-uncertainty dimensions while preserving accurate predictions on others.\nCompared to ReconVLA, it performs learned synthesis rather than selection, producing corrections that can improve upon any individual sample, and replaces the scalar Euclidean proxy with a 40-dimensional structured representation that captures per-DOF variance, calibrated confidence, and distributional volume.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 25_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "a345892d-1ba4-4e34-a1e6-3c0c1c16e3d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmJtnqRjGm6UcZMYt56cW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 43470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2469
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

_source line 26_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FHmntVHEPirVf6wBrYbDQg`</summary>

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
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "9935a4fb-0f16-42a6-abcb-57549b94bcb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmJtnqRjGm6UcZMYt56cW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 43470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2469
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

_source line 27 · 2026-05-15T19:37:01.193Z_

<details><summary>↩ Tool result · `toolu_01FHmntVHEPirVf6wBrYbDQg`</summary>

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
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "b915d074-2a4a-45b5-bf67-90649aa8e452",
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

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_016epyStbb7DJZo5b3vUhfVS`</summary>

```json
{
  "name": "related_work_v2",
  "type": "paper",
  "description": "Related Work section (Section 2) for ACR-VLA CoRL 2026 paper. 4 subsections: VLA Robustness, Conformal Prediction in Robotics, Residual Policy Learning, Uncertainty Quantification for VLAs.",
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
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "39173126-8bd5-48f2-93d5-a8684979793f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WrtfU9hzo1qPQXM3oy4Ead",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 45939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
      },
      "output_tokens": 52,
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

_source line 29 · 2026-05-15T19:37:05.886Z_

<details><summary>↩ Tool result · `toolu_016epyStbb7DJZo5b3vUhfVS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_80791f\", \"name\": \"related_work_v2\", \"type\": \"paper\", \"description\": \"Related Work section (Section 2) for ACR-VLA CoRL 2026 paper. 4 subsections: VLA Robustness, Conformal Prediction in Robotics, Residual Policy Learning, Uncertainty Quantification for VLAs.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_80791f.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T19:37:05.805592+00:00\", \"tags\": [\"paper\", \"related-work\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "6e7329f5-93cb-4186-800c-fca3c05a6217",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_80791f\\\", \\\"name\\\": \\\"related_work_v2\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Related Work section (Section 2) for ACR-VLA CoRL 2026 paper. 4 subsections: VLA Robustness, Conformal Prediction in Robotics, Residual Policy Learning, Uncertainty Quantification for VLAs.\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_80791f.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T19:37:05.805592+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"related-work\\\", \\\"latex\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_80791f\", \"name\": \"related_work_v2\", \"type\": \"paper\", \"description\": \"Related Work section (Section 2) for ACR-VLA CoRL 2026 paper. 4 subsections: VLA Robustness, Conformal Prediction in Robotics, Residual Policy Learning, Uncertainty Quantification for VLAs.\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_80791f.tex\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T19:37:05.805592+00:00\", \"tags\": [\"paper\", \"related-work\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

Related Work 已写入 `artifacts/_project/paper/related_work.tex`。

结构概要：
- **VLA Robustness**: training-time (RobustVLA, SRPO, DiG-Flow, TT-VLA) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2)。定位 ACR-VLA 为 selection + correction 的组合，plug-and-play，无需 retraining。
- **Conformal Prediction in Robotics**: CP 基础 (Angelopoulos, CGS) + 机器人应用 (Conformalized Teleoperation, CP-Loop, ACP+CBF)。明确 ACR-VLA 用 CP 做 scoring/selection，不声明 corrected output 的 coverage guarantees。
- **Residual Policy Learning**: Silver → TRANSIC → PLD → DRC 的 magnitude control 演进。ACR-VLA 用最简单的 L2 norm clipping，且是 supervised offline training 而非 RL。
- **Uncertainty Quantification for VLAs**: DiU (single-pass) vs ACR-VLA (multi-sample)；SAFE (failure detection)；VLA calibration。包含 negative result：per-DOF conformal features 作为 CRM 输入未能提升性能。

所有引用均来自指定 cite key 列表，未编造任何引用。ReconVLA 正确描述为 conformal prediction method。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "uuid": "bce2a351-d534-4631-8ecb-54915672f716",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RbHjNyooPa7SjhHDbksDht",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 597,
      "cache_read_input_tokens": 46659,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 597
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

_source line 31_

Related Work 已写入 `artifacts/_project/paper/related_work.tex`。

结构概要：
- **VLA Robustness**: training-time (RobustVLA, SRPO, DiG-Flow, TT-VLA) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2)。定位 ACR-VLA 为 selection + correction 的组合，plug-and-play，无需 retraining。
- **Conformal Prediction in Robotics**: CP 基础 (Angelopoulos, CGS) + 机器人应用 (Conformalized Teleoperation, CP-Loop, ACP+CBF)。明确 ACR-VLA 用 CP 做 scoring/selection，不声明 corrected output 的 coverage guarantees。
- **Residual Policy Learning**: Silver → TRANSIC → PLD → DRC 的 magnitude control 演进。ACR-VLA 用最简单的 L2 norm clipping，且是 supervised offline training 而非 RL。
- **Uncertainty Quantification for VLAs**: DiU (single-pass) vs ACR-VLA (multi-sample)；SAFE (failure detection)；VLA calibration。包含 negative result：per-DOF conformal features 作为 CRM 输入未能提升性能。

所有引用均来自指定 cite key 列表，未编造任何引用。ReconVLA 正确描述为 conformal prediction method。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 95496,
  "duration_api_ms": 96047,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "f8e60658-d44f-4b41-b5f1-c3e5d5881772",
  "total_cost_usd": 0.43923974999999993,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 35415,
    "cache_read_input_tokens": 244112,
    "output_tokens": 3732,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 35415,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 388,
        "cache_read_input_tokens": 46659,
        "cache_creation_input_tokens": 597,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 597
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2405,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00249,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 3732,
      "cacheReadInputTokens": 244112,
      "cacheCreationInputTokens": 35415,
      "webSearchRequests": 0,
      "costUSD": 0.43674974999999994,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "da41136d-8799-4666-8dd2-290b6dd386dd"
}
```

</details>

---
