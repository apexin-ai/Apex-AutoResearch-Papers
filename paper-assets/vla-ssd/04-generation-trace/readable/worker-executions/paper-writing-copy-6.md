# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_writing_20260516T030955.log`
- **Structured JSON:** [`1fae89cf3a7210272718.json`](../../sessions/1f/1fae89cf3a7210272718.json)

## Before a recorded user message

20 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
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
  "uuid": "0724fded-cf2c-46b1-ad58-2a550d6eeeae",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1778907600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b2c1d471-4ce9-4020-99af-f84bb8bb4d0f",
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and key paper sections in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "ec1f598a-dab7-4dc8-9086-c8ff57fa30f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3H6EArt8zsaorev2mdz2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12603,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12603
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

<details open><summary>🔧 Tool call — Read · `toolu_01S2VrZH5qBKWRBEMHUHfYuQ`</summary>

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
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "6a8c25e0-4d9f-458c-8a82-4ce5bce85d9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3H6EArt8zsaorev2mdz2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12603,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12603
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

_source line 6 · 2026-05-16T03:10:05.719Z_

<details><summary>↩ Tool result · `toolu_01S2VrZH5qBKWRBEMHUHfYuQ`</summary>

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
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "f2daea02-6098-48bb-b2c1-69fb45707382",
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

<details open><summary>🔧 Tool call — Read · `toolu_01Xc6fnwhEPTP3QAeYKwg6TA`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "9abce730-f110-4410-8292-b42d160614c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3H6EArt8zsaorev2mdz2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12603,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12603
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

_source line 8 · 2026-05-16T03:10:06.050Z_

<details><summary>↩ Tool result · `toolu_01Xc6fnwhEPTP3QAeYKwg6TA`</summary>

```text
1	---
2	name: red-section
3	description: "当实验结论为 negative / 审稿人指出 core claim 不成立 / 你要写或修改任何 paper/**/*.md 或 .tex 文件时,立即使用本 skill。提供 Framing 调整提案模板、写作规范、审稿攻击面预演。违反即被 Reviewer critical 打回。"
4	always: true
5	roles:
6	  - agent
7	---
8	
9	# Red Section — Narrative Re-framing
10	
11	## 什么时候用
12	- 实验 conclusion = negative
13	- 审稿人指出 core claim 不成立
14	- 写论文前（作为通用写作规范）
15	
16	## Negative 结果的正确心态
17	"不是失败，是发现了 X"。你的输出应该是 framing 调整提案，而不是 failure report。
18	
19	## 产出格式
20	
21	### Framing 调整提案模板
22	1. 原 claim：什么
23	2. 实验结果：什么（客观数字，不加修饰）
24	3. 重新审视：
25	   - 这个结果挑战了哪个 hypothesis？
26	   - 是否暴露了被忽略的变量？
27	   - 在新的 framing 下，哪些已做实验依然有效？哪些要补？
28	4. 新的 narrative 骨架（3 种备选，供 Director 选）
29	5. 对论文各章节的影响（abstract / intro / method / experiments / discussion / conclusion 逐一评估）
30	6. 建议下一步实验（必须至少 3 组备选，填新 framing 下的矩阵空格）
31	
32	### 写作规范（所有写作场景通用）
33	- 禁止 cherry-picking
34	- 所有数字必须追溯到 registry
35	- 强度与 evidence 匹配（1 个数据集 → 不能说 "consistently"）
36	- 每个定量 claim 必须附 exp_id
37	- 限制强度词（"significantly" 必须有统计检验）
38	
39	### 审稿攻击面预演
40	- 这个 section 最容易被审稿人攻击的点
41	- 预写 rebuttal 要点
42	
43	## 输出给谁
44	- Framing 调整提案 → Main Agent 向 Director 汇报
45	- 写作 skill 合规检查 → Reviewer 审查时验证
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "fe71114b-fbeb-4f01-aba2-cb00b66142e8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md",
      "content": "---\nname: red-section\ndescription: \"当实验结论为 negative / 审稿人指出 core claim 不成立 / 你要写或修改任何 paper/**/*.md 或 .tex 文件时,立即使用本 skill。提供 Framing 调整提案模板、写作规范、审稿攻击面预演。违反即被 Reviewer critical 打回。\"\nalways: true\nroles:\n  - agent\n---\n\n# Red Section — Narrative Re-framing\n\n## 什么时候用\n- 实验 conclusion = negative\n- 审稿人指出 core claim 不成立\n- 写论文前（作为通用写作规范）\n\n## Negative 结果的正确心态\n\"不是失败，是发现了 X\"。你的输出应该是 framing 调整提案，而不是 failure report。\n\n## 产出格式\n\n### Framing 调整提案模板\n1. 原 claim：什么\n2. 实验结果：什么（客观数字，不加修饰）\n3. 重新审视：\n   - 这个结果挑战了哪个 hypothesis？\n   - 是否暴露了被忽略的变量？\n   - 在新的 framing 下，哪些已做实验依然有效？哪些要补？\n4. 新的 narrative 骨架（3 种备选，供 Director 选）\n5. 对论文各章节的影响（abstract / intro / method / experiments / discussion / conclusion 逐一评估）\n6. 建议下一步实验（必须至少 3 组备选，填新 framing 下的矩阵空格）\n\n### 写作规范（所有写作场景通用）\n- 禁止 cherry-picking\n- 所有数字必须追溯到 registry\n- 强度与 evidence 匹配（1 个数据集 → 不能说 \"consistently\"）\n- 每个定量 claim 必须附 exp_id\n- 限制强度词（\"significantly\" 必须有统计检验）\n\n### 审稿攻击面预演\n- 这个 section 最容易被审稿人攻击的点\n- 预写 rebuttal 要点\n\n## 输出给谁\n- Framing 调整提案 → Main Agent 向 Director 汇报\n- 写作 skill 合规检查 → Reviewer 审查时验证\n",
      "numLines": 46,
      "startLine": 1,
      "totalLines": 46
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01QMJ8pLyjj5ZnrN8F1w7kwx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "cff00999-5da5-4bbf-bd80-9f568cb3d0a5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3H6EArt8zsaorev2mdz2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12603,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12603
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

_source line 10 · 2026-05-16T03:10:06.522Z_

<details><summary>↩ Tool result · `toolu_01QMJ8pLyjj5ZnrN8F1w7kwx`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Vision-language-action models (VLAs) achieve strong manipulation performance by fine-tuning large language models on robot demonstration data~\cite{brohan2023_rt2,kim2024_openvla}.
5	The prevailing architectural assumption is that LLM fine-tuning injects action-relevant representational knowledge into the system---that the language backbone learns to transform visual input into representations suited for action prediction.
6	Yet this assumption has not been tested at the representational level.
7	Where do the representations that drive action prediction actually originate?
8	The answer has direct consequences for VLA design: if the LLM backbone is the primary source of action structure, scaling and training the LLM is the critical lever; if instead the pretrained vision encoder already supplies this structure, investment should prioritize visual representation quality.
9	
10	Recent work has begun to probe this question from complementary angles.
11	At the behavioral level, \cite{grant2026} demonstrated that VLA policies are disproportionately driven by visual input, with language instructions having limited influence on action selection.
12	Representational analyses of VLA internals further suggest that language instructions are largely ignored by the action generation pathway~\cite{haon2025}.
13	However, these studies operate at the behavioral or single-component level---none has performed a systematic \emph{representational decomposition} that quantifies how each architectural component (vision encoder, projector, LLM layers) independently contributes to action-relevant structure.
14	Without such a decomposition, it remains unclear whether VLA fine-tuning creates new action knowledge or merely reconfigures structure inherited from pretrained components.
15	
16	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA that chains a frozen SigLIP vision encoder~\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone fine-tuned on LIBERO-10~\cite{liu2023_libero}.
17	We extract representations from the projector output, each of the 32 LLM layers at both distributed image-token and readout-token positions, and two external baselines---CLIP ViT-L/14~\cite{radford2021_clip} and DINOv2 ViT-L/14~\cite{oquab2024_dinov2}---that isolate the effect of pretraining objective (vision-language vs.\ vision-only).
18	To disentangle training from architecture, we cross two factors in a $2 \times 2$ factorial design: LLM training status (trained vs.\ untrained, with the untrained control reinitializing all 6.74B LLM parameters) and instruction presence (with vs.\ without language instruction).
19	We quantify action-relevant structure using Representational Similarity Analysis (RSA)~\cite{kriegeskorte2008}, which measures geometric alignment between representations and the action space, and functional MLP probes~\cite{alain2017}, which measure decodability of action vectors from frozen representations.
20	
21	Three findings emerge from this decomposition.
22	\emph{First}, the frozen vision-language encoder provides the dominant source of action-relevant geometric structure.
23	SigLIP+Projector achieves the highest action-space alignment (RSA $\rho = 0.615$); CLIP, an independent VL-pretrained encoder with no VLA training signal, achieves $\rho = 0.557$---both far exceeding vision-only DINOv2 ($\rho = 0.388$).
24	This 0.169-point gap between CLIP and DINOv2, two ViT-L/14 architectures differing primarily in pretraining objective, isolates VL pretraining as the operative factor.
25	The LLM never exceeds $\rho = 0.501$ at any layer.
26	\emph{Second}, the LLM degrades distributed geometric structure ($\rho$: $0.615 \to 0.501$) but concentrates a functionally superior representation at the readout token (probe $R^2 = 0.731$ vs.\ $0.706$ for the projector, $p = 0.001$), characterizing the LLM as an information \emph{router} rather than a knowledge source.
27	\emph{Third}, the geometric structure is invariant to LLM training ($\Delta\rho = 0.021$, $p = 0.20$, n.s.), while functional concentration at the readout requires it ($\Delta R^2 = 0.045$, $p < 0.0001$).
28	Training teaches routing, not representation creation.
29	
30	These findings make three contributions:
31	\begin{itemize}[nosep,leftmargin=*]
32	  \item We provide the first representational decomposition of a VLA, separately quantifying the action-relevant structure contributed by the vision encoder, projector, and LLM layers using both geometric (RSA) and functional (probe $R^2$) metrics.
33	  \item We demonstrate that VL-pretrained vision encoders---not LLM fine-tuning---are the primary source of action-relevant geometric structure, with two independent VL encoders (SigLIP, CLIP) both substantially exceeding vision-only DINOv2.
34	  \item We characterize the LLM as an information router that concentrates pre-existing vision-encoder geometry at the readout token for action decoding, with training teaching the routing policy rather than creating new representations.
35	\end{itemize}
36	These results suggest that vision encoder pretraining quality---specifically, vision-language alignment---is the primary lever for action representations in current VLA architectures, and that the LLM backbone's role is information routing rather than knowledge injection (\S\ref{sec:discussion}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "97ba3df2-a840-428f-8a10-2981013e3378",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nVision-language-action models (VLAs) achieve strong manipulation performance by fine-tuning large language models on robot demonstration data~\\cite{brohan2023_rt2,kim2024_openvla}.\nThe prevailing architectural assumption is that LLM fine-tuning injects action-relevant representational knowledge into the system---that the language backbone learns to transform visual input into representations suited for action prediction.\nYet this assumption has not been tested at the representational level.\nWhere do the representations that drive action prediction actually originate?\nThe answer has direct consequences for VLA design: if the LLM backbone is the primary source of action structure, scaling and training the LLM is the critical lever; if instead the pretrained vision encoder already supplies this structure, investment should prioritize visual representation quality.\n\nRecent work has begun to probe this question from complementary angles.\nAt the behavioral level, \\cite{grant2026} demonstrated that VLA policies are disproportionately driven by visual input, with language instructions having limited influence on action selection.\nRepresentational analyses of VLA internals further suggest that language instructions are largely ignored by the action generation pathway~\\cite{haon2025}.\nHowever, these studies operate at the behavioral or single-component level---none has performed a systematic \\emph{representational decomposition} that quantifies how each architectural component (vision encoder, projector, LLM layers) independently contributes to action-relevant structure.\nWithout such a decomposition, it remains unclear whether VLA fine-tuning creates new action knowledge or merely reconfigures structure inherited from pretrained components.\n\nWe address this gap by decomposing OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA that chains a frozen SigLIP vision encoder~\\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone fine-tuned on LIBERO-10~\\cite{liu2023_libero}.\nWe extract representations from the projector output, each of the 32 LLM layers at both distributed image-token and readout-token positions, and two external baselines---CLIP ViT-L/14~\\cite{radford2021_clip} and DINOv2 ViT-L/14~\\cite{oquab2024_dinov2}---that isolate the effect of pretraining objective (vision-language vs.\\ vision-only).\nTo disentangle training from architecture, we cross two factors in a $2 \\times 2$ factorial design: LLM training status (trained vs.\\ untrained, with the untrained control reinitializing all 6.74B LLM parameters) and instruction presence (with vs.\\ without language instruction).\nWe quantify action-relevant structure using Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008}, which measures geometric alignment between representations and the action space, and functional MLP probes~\\cite{alain2017}, which measure decodability of action vectors from frozen representations.\n\nThree findings emerge from this decomposition.\n\\emph{First}, the frozen vision-language encoder provides the dominant source of action-relevant geometric structure.\nSigLIP+Projector achieves the highest action-space alignment (RSA $\\rho = 0.615$); CLIP, an independent VL-pretrained encoder with no VLA training signal, achieves $\\rho = 0.557$---both far exceeding vision-only DINOv2 ($\\rho = 0.388$).\nThis 0.169-point gap between CLIP and DINOv2, two ViT-L/14 architectures differing primarily in pretraining objective, isolates VL pretraining as the operative factor.\nThe LLM never exceeds $\\rho = 0.501$ at any layer.\n\\emph{Second}, the LLM degrades distributed geometric structure ($\\rho$: $0.615 \\to 0.501$) but concentrates a functionally superior representation at the readout token (probe $R^2 = 0.731$ vs.\\ $0.706$ for the projector, $p = 0.001$), characterizing the LLM as an information \\emph{router} rather than a knowledge source.\n\\emph{Third}, the geometric structure is invariant to LLM training ($\\Delta\\rho = 0.021$, $p = 0.20$, n.s.), while functional concentration at the readout requires it ($\\Delta R^2 = 0.045$, $p < 0.0001$).\nTraining teaches routing, not representation creation.\n\nThese findings make three contributions:\n\\begin{itemize}[nosep,leftmargin=*]\n  \\item We provide the first representational decomposition of a VLA, separately quantifying the action-relevant structure contributed by the vision encoder, projector, and LLM layers using both geometric (RSA) and functional (probe $R^2$) metrics.\n  \\item We demonstrate that VL-pretrained vision encoders---not LLM fine-tuning---are the primary source of action-relevant geometric structure, with two independent VL encoders (SigLIP, CLIP) both substantially exceeding vision-only DINOv2.\n  \\item We characterize the LLM as an information router that concentrates pre-existing vision-encoder geometry at the readout token for action decoding, with training teaching the routing policy rather than creating new representations.\n\\end{itemize}\nThese results suggest that vision encoder pretraining quality---specifically, vision-language alignment---is the primary lever for action representations in current VLA architectures, and that the LLM backbone's role is information routing rather than knowledge injection (\\S\\ref{sec:discussion}).",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01XhgVihMfNyAgKXAdzehfrE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "7e5df3aa-16a8-4c0c-bfa6-be8f7b3d1a8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3H6EArt8zsaorev2mdz2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12603,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12603
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

_source line 12 · 2026-05-16T03:10:07.435Z_

<details><summary>↩ Tool result · `toolu_01XhgVihMfNyAgKXAdzehfrE`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	Our experiments reveal a coherent picture of how action-relevant structure flows through a VLA.
6	The vision encoder is the \emph{source}: VL-pretrained encoders provide geometric structure aligned with the action space (SigLIP+Projector RSA $\rho = 0.615$; CLIP $\rho = 0.557$), far exceeding what the LLM produces at any layer ($\rho \leq 0.501$).
7	The LLM is a \emph{router}: it degrades distributed geometric structure ($\rho$: $0.615 \to 0.501$; $R^2$: $0.706 \to 0.683$) while concentrating a functionally superior representation at the readout token ($R^2 = 0.731$).
8	Training teaches the \emph{routing policy}: the geometric structure itself is invariant to training ($\Delta\rho = 0.021$, $p = 0.20$), but functional concentration at the readout requires it ($\Delta R^2 = 0.045$, $p < 0.0001$).
9	Notably, the projector alone captures 96.6\% of the trained readout's functional capacity ($0.706/0.731$), suggesting that the LLM's contribution, while statistically significant, is incremental.
10	
11	\paragraph{VL pretraining as a general source of action-relevant geometry.}
12	The inclusion of CLIP ViT-L/14 as an external baseline provides evidence that action-relevant geometric structure is a general product of vision-language pretraining, not an artifact of SigLIP's specific architecture or training data.
13	Both VL-pretrained encoders---SigLIP ($\rho = 0.615$) and CLIP ($\rho = 0.557$)---substantially exceed vision-only DINOv2 ($\rho = 0.388$).
14	The 0.169-point gap between CLIP and DINOv2, both ViT-L/14 architectures differing primarily in pretraining objective, isolates language grounding as the operative factor.
15	The additional increment from CLIP to SigLIP+Projector ($\Delta = 0.058$) is consistent with the projector's VLA-supervised alignment providing a modest boost, but the dominant contribution ($\rho = 0.557 \gg 0.388$) originates in VL pretraining itself.
16	
17	\paragraph{Geometric-functional dissociation.}
18	A recurring finding across our analyses is the dissociation between geometric alignment (RSA) and functional decodability (probe $R^2$).
19	DINOv2 achieves probe performance statistically indistinguishable from the SigLIP+Projector ($R^2$: $0.712$ vs.\ $0.706$, $p = 0.22$) despite substantially lower RSA ($0.388$ vs.\ $0.615$).
20	This dissociation implies that action information---in the sense of decodable content---is broadly available in strong visual features regardless of pretraining objective; what VL pretraining adds is \emph{geometric alignment}, organizing that information into a structure that mirrors the action space.
21	For VLA design, this distinction matters: encoder selection determines not just what information is available, but how it is organized, with downstream consequences for how easily the LLM can route it.
22	
23	\paragraph{Metric sensitivity: RSA versus CKA.}
24	The divergence between RSA and linear CKA underscores the importance of multi-metric evaluation.
25	Linear CKA produces a ranking---untrained LLM ($0.089$) $>$ trained ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$)---that partially reverses the RSA ordering.
26	Under linear CKA, training appears to \emph{reduce} similarity to the action space, an interpretation that contradicts both RSA and functional probe evidence.
27	RDM kernel CKA resolves this discrepancy, restoring the RSA-consistent ranking (trained $0.260$ $>$ Proj $0.257$ $>$ untrained $0.246$ $>$ DINOv2 $0.241$).
28	The divergence likely reflects linear CKA's sensitivity to second-order statistics and its known vulnerability to dimension mismatch between high-dimensional representations and the 7-D action space~\cite{kornblith2019}.
29	The practical implication is that the LLM transforms rather than destroys action structure, but the narrative one draws depends critically on which metric is employed.
30	
31	\paragraph{Implications for VLA design.}
32	Our findings suggest four practical considerations.
33	\emph{First}, vision encoder pretraining quality is the primary lever for action-relevant representations; investing in stronger VL encoders may yield larger gains than scaling the LLM backbone.
34	\emph{Second}, for downstream modules that operate on distributed representations (e.g., auxiliary losses, multi-task heads), the projector output may be preferable to LLM-processed features, given its higher geometric fidelity and 96.6\% of readout-level decodability.
35	\emph{Third}, the LLM's value lies in readout concentration---routing distributed information to a single decoding site---which informs action head design: architectures that exploit this concentration (e.g., reading from a dedicated token rather than pooling LLM features) may better leverage the LLM's trained routing.
36	\emph{Fourth}, the invariance of representation geometry to language instructions ($\Delta\rho = 0.004$, n.s.; content controls within $\pm 0.017$) suggests that instructions influence action selection through a mechanism other than modulating visual representation structure, inviting further investigation into how language conditions behavior in VLAs.
37	
38	\paragraph{Connection to behavioral evidence.}
39	Our representational findings complement the behavioral results of \cite{grant2026}, who showed that VLA policies are disproportionately driven by visual input and that language instructions are ``encoded but not used'' for action selection.
40	Our data provide a representational account of these behavioral patterns: vision dominates because the frozen encoder supplies the action-relevant geometric structure that the LLM routes to the readout, while instruction content does not modulate this geometric structure (all four instruction conditions yield RSA within $\pm 0.017$).
41	The alignment between representational and behavioral evidence strengthens the case that VL-pretrained vision encoders, rather than LLM reasoning, are the primary computational substrate for action generation in current VLA architectures.
42	
43	\paragraph{Limitations.}
44	Several limitations scope our conclusions.
45	We study a single VLA architecture (OpenVLA-7B) on a single benchmark suite (LIBERO); generalization to other architectures (e.g., RT-2~\cite{brohan2023_rt2}) and domains (e.g., mobile manipulation, dexterous hands) remains to be established.
46	RSA captures structural alignment between representations and actions but does not establish causal contribution---high RSA does not guarantee that the representation is causally used by the policy.
47	The CLIP and DINOv2 action probes were trained with different hyperparameters (100 epochs) than the projector and LLM probes (50 epochs); while within-experiment comparisons are valid, absolute $R^2$ values are not directly comparable across these two probe sets, and we have been careful to restrict cross-experiment claims accordingly.
48	Finally, our analyses characterize frozen representations post hoc; they do not address how these representations emerge during VLA pretraining or fine-tuning, nor whether architectural interventions (e.g., unfreezing the vision encoder) would alter the source--router dynamic we observe.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "da1a9250-cd08-4c79-af84-5d4b6933b9ef",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nOur experiments reveal a coherent picture of how action-relevant structure flows through a VLA.\nThe vision encoder is the \\emph{source}: VL-pretrained encoders provide geometric structure aligned with the action space (SigLIP+Projector RSA $\\rho = 0.615$; CLIP $\\rho = 0.557$), far exceeding what the LLM produces at any layer ($\\rho \\leq 0.501$).\nThe LLM is a \\emph{router}: it degrades distributed geometric structure ($\\rho$: $0.615 \\to 0.501$; $R^2$: $0.706 \\to 0.683$) while concentrating a functionally superior representation at the readout token ($R^2 = 0.731$).\nTraining teaches the \\emph{routing policy}: the geometric structure itself is invariant to training ($\\Delta\\rho = 0.021$, $p = 0.20$), but functional concentration at the readout requires it ($\\Delta R^2 = 0.045$, $p < 0.0001$).\nNotably, the projector alone captures 96.6\\% of the trained readout's functional capacity ($0.706/0.731$), suggesting that the LLM's contribution, while statistically significant, is incremental.\n\n\\paragraph{VL pretraining as a general source of action-relevant geometry.}\nThe inclusion of CLIP ViT-L/14 as an external baseline provides evidence that action-relevant geometric structure is a general product of vision-language pretraining, not an artifact of SigLIP's specific architecture or training data.\nBoth VL-pretrained encoders---SigLIP ($\\rho = 0.615$) and CLIP ($\\rho = 0.557$)---substantially exceed vision-only DINOv2 ($\\rho = 0.388$).\nThe 0.169-point gap between CLIP and DINOv2, both ViT-L/14 architectures differing primarily in pretraining objective, isolates language grounding as the operative factor.\nThe additional increment from CLIP to SigLIP+Projector ($\\Delta = 0.058$) is consistent with the projector's VLA-supervised alignment providing a modest boost, but the dominant contribution ($\\rho = 0.557 \\gg 0.388$) originates in VL pretraining itself.\n\n\\paragraph{Geometric-functional dissociation.}\nA recurring finding across our analyses is the dissociation between geometric alignment (RSA) and functional decodability (probe $R^2$).\nDINOv2 achieves probe performance statistically indistinguishable from the SigLIP+Projector ($R^2$: $0.712$ vs.\\ $0.706$, $p = 0.22$) despite substantially lower RSA ($0.388$ vs.\\ $0.615$).\nThis dissociation implies that action information---in the sense of decodable content---is broadly available in strong visual features regardless of pretraining objective; what VL pretraining adds is \\emph{geometric alignment}, organizing that information into a structure that mirrors the action space.\nFor VLA design, this distinction matters: encoder selection determines not just what information is available, but how it is organized, with downstream consequences for how easily the LLM can route it.\n\n\\paragraph{Metric sensitivity: RSA versus CKA.}\nThe divergence between RSA and linear CKA underscores the importance of multi-metric evaluation.\nLinear CKA produces a ranking---untrained LLM ($0.089$) $>$ trained ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$)---that partially reverses the RSA ordering.\nUnder linear CKA, training appears to \\emph{reduce} similarity to the action space, an interpretation that contradicts both RSA and functional probe evidence.\nRDM kernel CKA resolves this discrepancy, restoring the RSA-consistent ranking (trained $0.260$ $>$ Proj $0.257$ $>$ untrained $0.246$ $>$ DINOv2 $0.241$).\nThe divergence likely reflects linear CKA's sensitivity to second-order statistics and its known vulnerability to dimension mismatch between high-dimensional representations and the 7-D action space~\\cite{kornblith2019}.\nThe practical implication is that the LLM transforms rather than destroys action structure, but the narrative one draws depends critically on which metric is employed.\n\n\\paragraph{Implications for VLA design.}\nOur findings suggest four practical considerations.\n\\emph{First}, vision encoder pretraining quality is the primary lever for action-relevant representations; investing in stronger VL encoders may yield larger gains than scaling the LLM backbone.\n\\emph{Second}, for downstream modules that operate on distributed representations (e.g., auxiliary losses, multi-task heads), the projector output may be preferable to LLM-processed features, given its higher geometric fidelity and 96.6\\% of readout-level decodability.\n\\emph{Third}, the LLM's value lies in readout concentration---routing distributed information to a single decoding site---which informs action head design: architectures that exploit this concentration (e.g., reading from a dedicated token rather than pooling LLM features) may better leverage the LLM's trained routing.\n\\emph{Fourth}, the invariance of representation geometry to language instructions ($\\Delta\\rho = 0.004$, n.s.; content controls within $\\pm 0.017$) suggests that instructions influence action selection through a mechanism other than modulating visual representation structure, inviting further investigation into how language conditions behavior in VLAs.\n\n\\paragraph{Connection to behavioral evidence.}\nOur representational findings complement the behavioral results of \\cite{grant2026}, who showed that VLA policies are disproportionately driven by visual input and that language instructions are ``encoded but not used'' for action selection.\nOur data provide a representational account of these behavioral patterns: vision dominates because the frozen encoder supplies the action-relevant geometric structure that the LLM routes to the readout, while instruction content does not modulate this geometric structure (all four instruction conditions yield RSA within $\\pm 0.017$).\nThe alignment between representational and behavioral evidence strengthens the case that VL-pretrained vision encoders, rather than LLM reasoning, are the primary computational substrate for action generation in current VLA architectures.\n\n\\paragraph{Limitations.}\nSeveral limitations scope our conclusions.\nWe study a single VLA architecture (OpenVLA-7B) on a single benchmark suite (LIBERO); generalization to other architectures (e.g., RT-2~\\cite{brohan2023_rt2}) and domains (e.g., mobile manipulation, dexterous hands) remains to be established.\nRSA captures structural alignment between representations and actions but does not establish causal contribution---high RSA does not guarantee that the representation is causally used by the policy.\nThe CLIP and DINOv2 action probes were trained with different hyperparameters (100 epochs) than the projector and LLM probes (50 epochs); while within-experiment comparisons are valid, absolute $R^2$ values are not directly comparable across these two probe sets, and we have been careful to restrict cross-experiment claims accordingly.\nFinally, our analyses characterize frozen representations post hoc; they do not address how these representations emerge during VLA pretraining or fine-tuning, nor whether architectural interventions (e.g., unfreezing the vision encoder) would alter the source--router dynamic we observe.",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01UgygeUGL7msbiNWdAG1jYT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "33c1232d-00b2-4318-8159-17b0d53d8027",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S3H6EArt8zsaorev2mdz2X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12603,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12603
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

_source line 14 · 2026-05-16T03:10:07.788Z_

<details><summary>↩ Tool result · `toolu_01UgygeUGL7msbiNWdAG1jYT`</summary>

```text
1	papers:
2	  # ============================================================
3	  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability
4	  # ============================================================
5	  - id: grant2026
6	    title: "Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models"
7	    authors: "Bryce Grant, Xijia Zhao, Peng Wang"
8	    year: 2026
9	    venue: "arXiv preprint (under review)"
10	    arxiv_id: "2603.19233"
11	    category: direct-competitor
12	    role: competitor
13	    key_findings: >
14	      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).
15	      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;
16	      when multiple goals share a scene, language becomes essential ("encoded but not used").
17	      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).
18	      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).
19	    relevance_to_us: >
20	      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.
21	      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.
22	    novelty_gap: >
23	      No trained vs untrained representation analysis. They compare different model architectures,
24	      we compare trained vs untrained representation structure within the same architecture.
25	      Their "encoded but not used" is a behavioral-level conclusion; we demonstrate at the representation level
26	      that instruction conditioning comes from the input pathway, not training. Complementary work.
27	    notes: >
28	      Action Atlas interactive exploration tool released. 6 models: OpenVLA, X-VLA, pi0.5, SmolVLA, GR00T, Octo.
29	      OFT checkpoint difference may affect direct comparability.
30	
31	  - id: swann2026
32	    title: "Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models"
33	    authors: "Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer, Monroe Kennedy III, Mac Schwager"
34	    year: 2026
35	    venue: "arXiv preprint"
36	    arxiv_id: "2603.19183"
37	    category: direct-competitor
38	    role: competitor
39	    key_findings: >
40	      SAE features on OpenVLA: majority of extracted features correspond to memorized training sequences,
41	      but some correspond to interpretable, general, and steerable motion primitives and semantic properties.
42	    relevance_to_us: >
43	      Also OpenVLA interpretability work. They use SAE for feature-level decomposition,
44	      we use probing + RSA for representation-level analysis. Methodologically complementary.
45	    novelty_gap: >
46	      No language features analysis. No trained vs untrained comparison.
47	      Does not investigate source of instruction conditioning (input pathway vs training).
48	    notes: "Stanford team. Published on arXiv same day as Grant 2026 (2026-03-19)."
49	
50	  - id: rizzardo2026
51	    title: "Observing and Controlling Features in Vision-Language-Action Models"
52	    authors: "Rizzardo et al."
53	    year: 2026
54	    venue: "arXiv preprint"
55	    arxiv_id: "2603.05487"
56	    category: direct-competitor
57	    role: competitor
58	    key_findings: >
59	      Introduces feature-observability and feature-controllability concepts bridging LLM mechanistic
60	      interpretability and VLAs. Linear classifier observation + optimal-control-based minimal intervention steering.
61	      Validated on pi0.5 and OpenVLA — targeted interventions steer robot behavior while preserving closed-loop capabilities.
62	    relevance_to_us: >
63	      Also VLA internal representation analysis. They focus on how to steer,
64	      we focus on where conditioning comes from (input pathway vs training).
65	    novelty_gap: >
66	      No trained vs untrained comparison. No instruction pathway vs training separation analysis.
67	      Focuses on controllability rather than representation structure origin.
68	    notes: "Submitted 2026-03-05."
69	
70	  - id: haon2025
71	    title: "Mechanistic Interpretability for Steering Vision-Language-Action Models"
72	    authors: "Bear Haon, Kaylene Stocking, Ian Chuang, Claire Tomlin"
73	    year: 2025
74	    venue: "CoRL 2025"
75	    arxiv_id: "2509.00328"
76	    category: direct-competitor
77	    role: methodology
78	    key_findings: >
79	      First VLA mechanistic interpretability framework. Projects feedforward activations onto token embedding basis,
80	      identifies sparse semantic directions (speed, direction) causally linked to action selection.
81	      Activation steering modulates behavior in real time without fine-tuning.
82	      Validated on Pi0 and OpenVLA in LIBERO (simulation) and UR5 (real robot).
83	    relevance_to_us: >
84	      Methodological reference: their activation steering proves VLAs have interpretable semantic directions.
85	      Our RSA/probing results can dialogue with their mechanistic findings.
86	    novelty_gap: >
87	      No trained vs untrained comparison. No systematic representation structure analysis (RSA/CKA).
88	      Focuses on individual semantic direction causal intervention, not overall structure comparison.
89	    notes: "CoRL 2025 accepted. Pioneering work in VLA interpretability."
90	
91	  - id: molinari2025
92	    title: "Emergent World Representations in OpenVLA"
93	    authors: "Marco Molinari, Leonardo Nevali, Saharsha Navani, Omar G. Younis"
94	    year: 2025
95	    venue: "arXiv preprint"
96	    arxiv_id: "2509.24559"
97	    category: direct-competitor
98	    role: context
99	    key_findings: >
100	      OpenVLA implicitly learns a world model. Embedding arithmetic tests state transition knowledge;
101	      linear/non-linear probes show statistically significant state transition prediction ability across layers.
102	      SAE pipeline analyzes fine-grained world model structure.
103	    relevance_to_us: >
104	      Also OpenVLA probing work. They study world model, we study instruction conditioning.
105	      Their layer-wise probe results can be compared with our layer-wise RSA.
106	    novelty_gap: >
107	      No language/instruction analysis. No trained vs untrained comparison.
108	      Only focuses on state transitions, not goal/instruction representation.
109	    notes: "Submitted 2025-09-29. Has OpenReview discussion."
110	
111	  - id: lu2025
112	    title: "Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture"
113	    authors: "Hong Lu, Hengxu Li, Prithviraj Singh Shahani, Stephanie Herbers, Matthias Scheutz"
114	    year: 2025
115	    venue: "arXiv preprint"
116	    arxiv_id: "2502.04558"
117	    category: direct-competitor
118	    role: methodology
119	    key_findings: >
120	      Probes OpenVLA hidden layers to extract symbolic representations (object properties, relations, action states).
121	      LIBERO-spatial pick-and-place probing accuracy > 0.90 across most layers.
122	      Integration with cognitive architecture improves interpretability and robustness.
123	    relevance_to_us: >
124	      Directly related methodology: both use linear probes on OpenVLA layers on LIBERO.
125	      Their finding that symbolic states are decodable (>0.90) is consistent with our goal classification at 100%.
126	    novelty_gap: >
127	      Only trained model probing, no untrained control.
128	      Only LIBERO-spatial single task, no cross-task/cross-condition analysis.
129	      No instruction conditioning source analysis.
130	    notes: "Submitted 2025-02-06. Tufts University."
131	
132	  - id: fang_intention2025
133	    title: "From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models"
134	    authors: "Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng"
135	    year: 2025
136	    venue: "arXiv preprint"
137	    arxiv_id: "2506.09930"
138	    category: direct-competitor
139	    role: context
140	    key_findings: >
141	      Unified probing suite (50 simulation tasks, 10 subcategories) evaluating VLA generalization boundaries.
142	      VLM backbone provides robust perceptual understanding + high-level planning (good intentions),
143	      but cannot reliably translate to precise motor execution (perception-to-action gap).
144	      Action data fine-tuning erodes original VLM generalist reasoning abilities.
145	    relevance_to_us: >
146	      "Fine-tuning erodes VLM reasoning" echoes our "training doesn't improve representation" finding.
147	      They discover intention != execution at behavioral level; we discover
148	      training ~= untrained in representation structure.
149	    novelty_gap: >
150	      Behavioral-level probing (success rates), not representation-level analysis.
151	      No trained vs untrained representation structure comparison.
152	    notes: "Submitted 2025-06-11. INT-ACT benchmark open-sourced. NYU/ai4ce team."
153	
154	  # ============================================================
155	  # DIRECT COMPETITORS — Language Grounding / Counterfactual
156	  # ============================================================
157	  - id: fang_cf2026
158	    title: "When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs"
159	    authors: "Yu Fang, Yuchun Feng, Dong Jing, Jiaqi Liu, Yue Yang, Zhenyu Wei, Daniel Szafir, Mingyu Ding"
160	    year: 2026
161	    venue: "arXiv preprint"
162	    arxiv_id: "2602.17659"
163	    category: direct-competitor
164	    role: competitor
165	    key_findings: >
166	      Introduces LIBERO-CF counterfactual benchmark. VLAs exhibit severe counterfactual failures:
167	      vision shortcuts + dataset biases cause models to ignore language intent.
168	      OpenVLA-OFT: 4.7% grounding rate, 0.4% success rate.
169	      Best model: 30.8% grounding rate, 13.2% success rate.
170	      Proposes Counterfactual Action Guidance (CAG) dual-branch inference scheme.
171	    relevance_to_us: >
172	      Directly validates "language encoded but not used" severity under counterfactual settings.
173	      Their behavioral findings complement our representation-level findings.
174	      They test OpenVLA-OFT — same checkpoint issue as Grant 2026.
175	    novelty_gap: >
176	      Pure behavioral benchmark, no representation analysis.
177	      No trained vs untrained comparison. No instruction pathway causal analysis.
178	    notes: "Submitted 2026-02-19. LIBERO-CF has 4 sub-suites (CF-Spatial, CF-Object, CF-Long, CF-OOD)."
179	
180	  - id: hou2026
181	    title: "LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models"
182	    authors: "Yuchen Hou, Lin Zhao"
183	    year: 2026
184	    venue: "arXiv preprint"
185	    arxiv_id: "2603.00592"
186	    category: direct-competitor
187	    role: context
188	    key_findings: >
189	      SOTA VLAs achieve >95% on standard benchmarks but largely ignore language instructions.
190	      Four-dimensional semantic perturbation method exposes language understanding deficits.
191	      LIBERO assigns only 1 task per layout, so models dont need to understand language.
192	      LangGap benchmark forces multi-task shared layouts; data augmentation improves from 0% to 90%.
193	    relevance_to_us: >
194	      Systematic diagnosis of "VLAs ignore language" supports our story:
195	      instruction conditioning comes from input pathway, not training — even trained VLAs dont truly leverage language.
196	    novelty_gap: >
197	      Behavioral-level diagnosis + data augmentation solution. No representation analysis.
198	      No trained vs untrained comparison. No input pathway causal analysis.
199	    notes: "Submitted 2026-02-28. GitHub open-sourced."
200	
201	  # ============================================================
202	  # METHOD COMPONENT — RSA, CKA, Linear Probing
203	  # ============================================================
204	  - id: kriegeskorte2008
205	    title: "Representational Similarity Analysis - Connecting the Branches of Systems Neuroscience"
206	    authors: "Nikolaus Kriegeskorte, Marieke Mur, Peter Bandettini"
207	    year: 2008
208	    venue: "Frontiers in Systems Neuroscience"
209	    arxiv_id: null
210	    doi: "10.3389/neuro.06.004.2008"
211	    category: method-component
212	    role: methodology
213	    key_findings: >
214	      Introduces Representational Dissimilarity Matrix (RDM) framework for comparing multi-channel
215	      neural activity measurements with computational models and behavior.
216	      Validated on fMRI visual cortex data.
217	    relevance_to_us: "RSA is one of our core analysis methods for comparing trained/untrained/DINO representation structures."
218	    novelty_gap: null
219	    notes: "Original RSA paper. 5000+ citations."
220	
221	  - id: kornblith2019
222	    title: "Similarity of Neural Network Representations Revisited"
223	    authors: "Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton"
224	    year: 2019
225	    venue: "ICML 2019"
226	    arxiv_id: "1905.00414"
227	    category: method-component
228	    role: methodology
229	    key_findings: >
230	      Introduces Centered Kernel Alignment (CKA) as representation similarity metric.
231	      CKA reliably identifies representation correspondences across differently initialized networks,
232	      outperforming CCA-based methods.
233	    relevance_to_us: >
234	      CKA is one of our core tools for comparing trained vs untrained representations.
235	      Deep-layer CKA reaching 0.86 demonstrates high representation similarity.
236	    novelty_gap: null
237	    notes: "Google Brain. CKA is now standard for representation comparison."
238	
239	  - id: alain2017
240	    title: "Understanding Intermediate Layers Using Linear Classifier Probes"
241	    authors: "Guillaume Alain, Yoshua Bengio"
242	    year: 2017
243	    venue: "ICLR 2017 Workshop"
244	    arxiv_id: "1610.01644"
245	    category: method-component
246	    role: methodology
247	    key_findings: >
248	      Proposes linear classifier probes to monitor feature suitability for classification at every layer.
249	      Linear separability increases monotonically along network depth.
250	      Validated on Inception v3 and ResNet-50.
251	    relevance_to_us: "Linear probing is the methodological foundation for our goal classification and action prediction experiments."
252	    novelty_gap: null
253	    notes: "Foundational probing methodology work."
254	
255	  # ============================================================
256	  # VISION ENCODERS — SigLIP, DINOv2, CLIP
257	  # ============================================================
258	  - id: zhai2023_siglip
259	    title: "Sigmoid Loss for Language Image Pre-Training"
260	    authors: "Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, Lucas Beyer"
261	    year: 2023
262	    venue: "ICCV 2023"
263	    arxiv_id: "2303.15343"
264	    category: vision-encoder
265	    role: baseline
266	    verified: true
267	    key_findings: >
268	      Replaces softmax contrastive loss with pairwise sigmoid loss for VL pretraining.
269	      Eliminates global batch normalization, enabling smaller batch training.
270	      SigLIP-SO400M achieves competitive zero-shot performance with simpler training.
271	    relevance_to_us: >
272	      SigLIP-SO400M is OpenVLA's frozen vision encoder. Our RSA=0.615 for SigLIP+Projector
273	      shows this encoder provides dominant action-relevant geometric structure.
274	    novelty_gap: null
275	    notes: "Google. OpenVLA uses SigLIP-SO400M/14 variant."
276	
277	  - id: oquab2024_dinov2
278	    title: "DINOv2: Learning Robust Visual Features without Supervision"
279	    authors: "Maxime Oquab, Timothée Darcet, Théo Moutakanni, et al."
280	    year: 2024
281	    venue: "TMLR 2024"
282	    arxiv_id: "2304.07193"
283	    category: vision-encoder
284	    role: baseline
285	    verified: true
286	    key_findings: >
287	      Self-supervised ViT trained on curated 142M image dataset (LVD-142M).
288	      Produces general-purpose features competitive with task-specific models.
289	      No language supervision — purely vision self-supervised.
290	    relevance_to_us: >
291	      Vision-only baseline in our analysis. DINO RSA=0.388 << SigLIP 0.615,
292	      but DINO R²=0.712 ≈ Projector R²=0.706 — key geometric-functional dissociation.
293	    novelty_gap: null
294	    notes: "Meta AI. DINOv2 ViT-L/14 used as vision-only control."
295	
296	  - id: radford2021_clip
297	    title: "Learning Transferable Visual Models From Natural Language Supervision"
298	    authors: "Alec Radford, Jong Wook Kim, Chris Hallacy, et al."
299	    year: 2021
300	    venue: "ICML 2021"
301	    arxiv_id: "2103.00020"
302	    category: vision-encoder
303	    role: baseline
304	    verified: true
305	    key_findings: >
306	      Contrastive language-image pretraining on 400M image-text pairs.
307	      Zero-shot transfer competitive with supervised baselines.
308	      Pioneering VL pretraining approach.
309	    relevance_to_us: >
310	      CLIP ViT-L/14 RSA=0.557 confirms VL pretraining universality:
311	      both CLIP (0.557) and SigLIP+Proj (0.615) >> DINO (0.388).
312	      Action-relevant geometric structure is a universal product of VL pretraining.
313	    novelty_gap: null
314	    notes: "OpenAI. CLIP ViT-L/14 used as VL pretraining generalization control (plan_012)."
315	
316	  # ============================================================
317	  # BACKGROUND — VLM Design, Frozen Encoders, Multi-modal Fusion
318	  # ============================================================
319	  - id: karamcheti2024
320	    title: "Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models"
321	    authors: "Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Percy Liang, Thomas Kollar, Dorsa Sadigh"
322	    year: 2024
323	    venue: "arXiv preprint"
324	    arxiv_id: "2402.07865"
325	    category: background
326	    role: baseline
327	    key_findings: >
328	      Systematic investigation of VLM design space: pretrained visual representations, base vs instruct-tuned LM, etc.
329	      Different vision encoder ensembles (SigLIP, DINOv2) improve performance.
330	      OpenVLA is directly built on the Prismatic architecture.
331	    relevance_to_us: >
332	      OpenVLA's VLM backbone origin. The SigLIP+DINOv2 fusion design choice
333	      is the architectural basis for our analysis of "frozen vision encoder carries instruction conditioning."
334	    novelty_gap: >
335	      VLM design space exploration, no VLA-specific representation analysis.
336	      No trained vs untrained comparison.
337	    notes: "Significant author overlap with OpenVLA team."
338	
339	  - id: vla_survey2025
340	    title: "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges"
341	    authors: "Multiple authors"
342	    year: 2025
343	    venue: "arXiv preprint"
344	    arxiv_id: "2505.04769"
345	    category: background
346	    role: context
347	    key_findings: >
348	      Comprehensive survey of 100+ VLA architectures, 26 major VLA datasets.
349	      Large-scale quantitative analysis linking model design choices to normalized performance.
350	      Covers fusion strategy, action representation, encoder selection.
351	    relevance_to_us: "Provides VLA landscape for positioning our work in the representation analysis sub-direction."
352	    novelty_gap: "Survey, no original experimental analysis."
353	    notes: "Most comprehensive VLA survey as of 2025-05."
354	
355	  # ============================================================
356	  # EVALUATION — LIBERO Benchmark Ecosystem
357	  # ============================================================
358	  - id: liu2023_libero
359	    title: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
360	    authors: "Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone"
361	    year: 2023
362	    venue: "NeurIPS 2023"
363	    arxiv_id: "2306.03310"
364	    category: evaluation
365	    role: baseline
366	    key_findings: >
367	      130 tasks across 4 suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long).
368	      Procedural generation + skill blending + human teleoperation demonstrations.
369	      Lifelong learning benchmark with knowledge transfer evaluation.
370	    relevance_to_us: "Our primary experimental platform. LIBERO-10 (fine-tuning) + LIBERO-Goal (OOD test)."
371	    novelty_gap: null
372	    notes: "NeurIPS 2023 Datasets and Benchmarks track."
373	
374	  - id: fei2025_libero_plus
375	    title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
376	    authors: "Senyu Fei, Siyin Wang, Junhao Shi, et al."
377	    year: 2025
378	    venue: "arXiv preprint"
379	    arxiv_id: "2510.13626"
380	    category: evaluation
381	    role: context
382	    key_findings: >
383	      7-dimension controlled perturbations expose VLA fragility.
384	      Performance drops from 95% to <30% (camera viewpoint, robot initial state most sensitive).
385	      Models are insensitive to language variations — largely ignore language instructions.
386	      Positional bias over genuine semantic understanding.
387	    relevance_to_us: >
388	      "Models ignore language instructions" is consistent with our finding that
389	      training doesnt improve representation structure — VLAs have not truly learned language grounding.
390	    novelty_gap: "Behavioral robustness analysis, no representation-level analysis."
391	    notes: "Submitted 2025-10. OpenMOSS team."
392	
393	  - id: zhou2025_libero_pro
394	    title: "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization"
395	    authors: "Xueyang Zhou, Yangming Xu, Guiyao Tie, et al."
396	    year: 2025
397	    venue: "arXiv preprint"
398	    arxiv_id: "2510.03827"
399	    category: evaluation
400	    role: context
401	    key_findings: >
402	      Standard LIBERO >90% accuracy, but generalized setting collapses to 0.0%.
403	      Exposes reliance on rote memorization (action sequences + environment layouts)
404	      rather than genuine task understanding or environmental perception.
405	    relevance_to_us: >
406	      "Memorization not understanding" supports our story:
407	      VLA training improves action sequence memorization, not representation structure.
408	    novelty_gap: "Behavioral evaluation, no representation analysis."
409	    notes: "Submitted 2025-10."
410	
411	  - id: libero_para2026
412	    title: "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models"
413	    authors: "Multiple authors"
414	    year: 2026
415	    venue: "arXiv preprint"
416	    arxiv_id: "2603.28301"
417	    category: evaluation
418	    role: context
419	    key_findings: >
420	      7 VLA configurations (0.6B-7.5B) show 22-52pp performance degradation under paraphrasing.
421	      80-96% of failures from planning-level trajectory divergence (not execution errors),
422	      indicating paraphrasing disrupts task identification.
423	      Synonym substitution alone causes large drops — relies on surface-level matching, not semantic grounding.
424	    relevance_to_us: >
425	      Further confirms VLAs lack true language grounding.
426	      Complements our "instruction conditioning comes from input pathway structure, not semantic training."
427	    novelty_gap: "Paraphrase robustness diagnosis, no representation analysis."
428	    notes: "Submitted 2026-03-30."
429	
430	  # ============================================================
431	  # RELATED ARCHITECTURE — VLA Models
432	  # ============================================================
433	  - id: kim2024_openvla
434	    title: "OpenVLA: An Open-Source Vision-Language-Action Model"
435	    authors: "Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, et al."
436	    year: 2024
437	    venue: "arXiv preprint"
438	    arxiv_id: "2406.09246"
439	    category: related-architecture
440	    role: baseline
441	    key_findings: >
442	      7B-param VLA trained on 970k real-world robot demonstrations (Open X-Embodiment).
443	      Llama 2 7B backbone + DINOv2+SigLIP fused vision encoder.
444	      Outperforms RT-2-X (55B) by 16.5% absolute with 7x fewer parameters.
445	    relevance_to_us: >
446	      Our analysis target. All probing/RSA/CKA experiments use OpenVLA-7B.
447	      Architecture details (frozen SigLIP, Llama 2 backbone) directly affect our interpretation
448	      of "input pathway vs training."
449	    novelty_gap: null
450	    notes: "Stanford/Toyota/Google. Open-source checkpoints + training code."
451	
452	  - id: brohan2023_rt2
453	    title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
454	    authors: "Anthony Brohan et al."
455	    year: 2023
456	    venue: "arXiv preprint"
457	    arxiv_id: "2307.15818"
458	    category: related-architecture
459	    role: context
460	    key_findings: >
461	      Co-fine-tunes VLM (PaLM-E 55B) on robotic trajectory data + internet-scale VL tasks.
462	      Robot actions represented as text tokens.
463	      Demonstrates emergent capabilities: novel object generalization, chain-of-thought reasoning.
464	    relevance_to_us: >
465	      Pioneering VLA architecture. RT-2 uses PaLM-E, OpenVLA uses Llama 2,
466	      but shares the "LLM backbone + frozen vision encoder" core design.
467	      Our findings may generalize to similar architectures.
468	    novelty_gap: "No representation analysis. No trained vs untrained comparison."
469	    notes: "Google DeepMind. 55B params, not open-source."
470	
471	  - id: ghosh2024_octo
472	    title: "Octo: An Open-Source Generalist Robot Policy"
473	    authors: "Octo Model Team, Dibya Ghosh, Homer Walke, Karl Pertsch, et al."
474	    year: 2024
475	    venue: "arXiv preprint"
476	    arxiv_id: "2405.12213"
477	    category: related-architecture
478	    role: context
479	    key_findings: >
480	      Transformer-based diffusion policy pretrained on 800k robot episodes (Open X-Embodiment).
481	      Lightweight CNN vision encoder + language model for text instructions.
482	      27M (Small) / 93M (Base) params, consumer GPU fine-tuning.
483	    relevance_to_us: >
484	      Alternative VLA architecture (not LLM-based). Grant 2026 tests include Octo.
485	      If our findings generalize to Octo, the input pathway effect is cross-architectural.
486	    novelty_gap: "No representation analysis. No frozen encoder analysis."
487	    notes: "Berkeley. Author overlap with OpenVLA."
488	
489	  - id: black2024_pi0
490	    title: "pi0: A Vision-Language-Action Flow Model for General Robot Control"
491	    authors: "Kevin Black et al."
492	    year: 2024
493	    venue: "arXiv preprint"
494	    arxiv_id: "2410.24164"
495	    category: related-architecture
496	    role: context
497	    key_findings: >
498	      Flow matching action head (not autoregressive tokens), 50Hz continuous trajectories.
499	      Pre-trained VLM backbone + flow matching combination.
500	      7 robotic platforms, 68 tasks. Real-world dexterous manipulation.
501	    relevance_to_us: >
502	      pi0 uses continuous flow matching vs discrete tokens — different action representation.
503	      Grant 2026 and Haon 2025 both tested Pi0/pi0.5, enabling cross-reference with our OpenVLA results.
504	    novelty_gap: "No representation structure analysis."
505	    notes: "Physical Intelligence. Commercial frontier VLA."
506	
507	# ============================================================
508	# CATEGORY INDEX
509	# ============================================================
510	categories:
511	  direct-competitor:
512	    description: "VLA representation / interpretability / language grounding analysis"
513	    papers:
514	      - grant2026
515	      - swann2026
516	      - rizzardo2026
517	      - haon2025
518	      - molinari2025
519	      - lu2025
520	      - fang_intention2025
521	      - fang_cf2026
522	      - hou2026
523	
524	  method-component:
525	    description: "RSA, CKA, linear probing methodological references"
526	    papers:
527	      - kriegeskorte2008
528	      - kornblith2019
529	      - alain2017
530	
531	  vision-encoder:
532	    description: "Vision encoder architectures used in our analysis (SigLIP, DINOv2, CLIP)"
533	    papers:
534	      - zhai2023_siglip
535	      - oquab2024_dinov2
536	      - radford2021_clip
537	
538	  background:
539	    description: "VLM design space, frozen encoder effects, multi-modal fusion"
540	    papers:
541	      - karamcheti2024
542	      - vla_survey2025
543	
544	  evaluation:
545	    description: "LIBERO benchmark ecosystem and VLA robustness evaluation"
546	    papers:
547	      - liu2023_libero
548	      - fei2025_libero_plus
549	      - zhou2025_libero_pro
550	      - libero_para2026
551	
552	  related-architecture:
553	    description: "VLA model architectures (OpenVLA, RT-2, Octo, pi0)"
554	    papers:
555	      - kim2024_openvla
556	      - brohan2023_rt2
557	      - ghosh2024_octo
558	      - black2024_pi0
559	
560	# ============================================================
561	# SYNTHESIS: OUR NOVELTY POSITION
562	# ============================================================
563	synthesis:
564	  our_core_claim: "Instruction Input Pathway Drives Conditioning, Not Training"
565	
566	  what_others_have_done:
567	    behavioral_level:
568	      - "Grant 2026: vision pathway dominates, language 'encoded but not used' (activation injection)"
569	      - "LIBERO-CF/LangGap/LIBERO-Plus: VLAs ignore language instructions (counterfactual/robustness tests)"
570	      - "LIBERO-PRO: models rely on memorization not understanding"
571	      - "Fang 2025: fine-tuning erodes VLM reasoning (intention != execution)"
572	    representation_level:
573	      - "Swann 2026: SAE features mostly memorized sequences, some interpretable (OpenVLA)"
574	      - "Molinari 2025: world model emerges in middle layers (OpenVLA)"
575	      - "Lu 2025: symbolic states decodable with >0.90 accuracy (OpenVLA + LIBERO)"
576	      - "Haon 2025: sparse semantic directions causally linked to actions (Pi0 + OpenVLA)"
577	      - "Rizzardo 2026: feature-observability and controllability (pi0.5 + OpenVLA)"
578	
579	  what_nobody_has_done:
580	    - "Trained vs untrained VLA representation comparison (we find trained ~= untrained >> DINO)"
581	    - "Instruction input pathway vs LLM training separation analysis (6 probing rounds + RSA all consistent)"
582	    - "Systematic layer-wise RSA/CKA comparison of trained/untrained/DINO representation structures"
583	    - "Instruction ablation causal verification: removing instruction drops RSA to DINO level"
584	
585	  key_differentiation_from_grant2026: >
586	    Grant 2026 compares different VLA models (architectural differences);
587	    we compare trained vs untrained within the same model (training effect isolation).
588	    Grant finds "language encoded but not used" (behavioral level);
589	    we find "conditioning comes from input pathway, not training" (representation level).
590	    Complementary, not competing. Related Work must qualify OFT vs standard fine-tuning difference.
591	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "e3549fa3-5bb2-4568-bac4-0247e989c707",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml",
      "content": "papers:\n  # ============================================================\n  # DIRECT COMPETITORS — VLA Representation Analysis / Interpretability\n  # ============================================================\n  - id: grant2026\n    title: \"Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models\"\n    authors: \"Bryce Grant, Xijia Zhao, Peng Wang\"\n    year: 2026\n    venue: \"arXiv preprint (under review)\"\n    arxiv_id: \"2603.19233\"\n    category: direct-competitor\n    role: competitor\n    key_findings: >\n      Visual pathway dominates action generation across all 6 tested VLA architectures (80M–7B params, 394K+ rollout episodes, 4 benchmarks).\n      Language sensitivity depends on task structure: when visual context uniquely specifies the task, language is IGNORED;\n      when multiple goals share a scene, language becomes essential (\"encoded but not used\").\n      Cross-task activation injection steers robots toward source-task positions (99.8% trajectory alignment with source in X-VLA).\n      Multi-pathway architectures (pi0.5, SmolVLA, GR00T) separate motor programs (expert pathway) from goal semantics (VLM pathway).\n    relevance_to_us: >\n      Most direct competitor. Behavioral intervention (activation injection, SAE, probing) reveals vision dominance + language encoded but not used.\n      Uses OpenVLA-OFT checkpoint; we use standard fine-tuning — must qualify this difference in Related Work.\n    novelty_gap: >\n      No trained vs untrained representation analysis. They compare different model architectures,\n      we compare trained vs untrained representation structure within the same architecture.\n      Their \"encoded but not used\" is a behavioral-level conclusion; we demonstrate at the representation level\n      that instruction conditioning comes from the input pathway, not training. Complementary work.\n    notes: >\n      Action Atlas interactive exploration tool released. 6 models: OpenVLA, X-VLA, pi0.5, SmolVLA, GR00T, Octo.\n      OFT checkpoint difference may affect direct comparability.\n\n  - id: swann2026\n    title: \"Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models\"\n    authors: \"Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer, Monroe Kennedy III, Mac Schwager\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.19183\"\n    category: direct-competitor\n    role: competitor\n    key_findings: >\n      SAE features on OpenVLA: majority of extracted features correspond to memorized training sequences,\n      but some correspond to interpretable, general, and steerable motion primitives and semantic properties.\n    relevance_to_us: >\n      Also OpenVLA interpretability work. They use SAE for feature-level decomposition,\n      we use probing + RSA for representation-level analysis. Methodologically complementary.\n    novelty_gap: >\n      No language features analysis. No trained vs untrained comparison.\n      Does not investigate source of instruction conditioning (input pathway vs training).\n    notes: \"Stanford team. Published on arXiv same day as Grant 2026 (2026-03-19).\"\n\n  - id: rizzardo2026\n    title: \"Observing and Controlling Features in Vision-Language-Action Models\"\n    authors: \"Rizzardo et al.\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.05487\"\n    category: direct-competitor\n    role: competitor\n    key_findings: >\n      Introduces feature-observability and feature-controllability concepts bridging LLM mechanistic\n      interpretability and VLAs. Linear classifier observation + optimal-control-based minimal intervention steering.\n      Validated on pi0.5 and OpenVLA — targeted interventions steer robot behavior while preserving closed-loop capabilities.\n    relevance_to_us: >\n      Also VLA internal representation analysis. They focus on how to steer,\n      we focus on where conditioning comes from (input pathway vs training).\n    novelty_gap: >\n      No trained vs untrained comparison. No instruction pathway vs training separation analysis.\n      Focuses on controllability rather than representation structure origin.\n    notes: \"Submitted 2026-03-05.\"\n\n  - id: haon2025\n    title: \"Mechanistic Interpretability for Steering Vision-Language-Action Models\"\n    authors: \"Bear Haon, Kaylene Stocking, Ian Chuang, Claire Tomlin\"\n    year: 2025\n    venue: \"CoRL 2025\"\n    arxiv_id: \"2509.00328\"\n    category: direct-competitor\n    role: methodology\n    key_findings: >\n      First VLA mechanistic interpretability framework. Projects feedforward activations onto token embedding basis,\n      identifies sparse semantic directions (speed, direction) causally linked to action selection.\n      Activation steering modulates behavior in real time without fine-tuning.\n      Validated on Pi0 and OpenVLA in LIBERO (simulation) and UR5 (real robot).\n    relevance_to_us: >\n      Methodological reference: their activation steering proves VLAs have interpretable semantic directions.\n      Our RSA/probing results can dialogue with their mechanistic findings.\n    novelty_gap: >\n      No trained vs untrained comparison. No systematic representation structure analysis (RSA/CKA).\n      Focuses on individual semantic direction causal intervention, not overall structure comparison.\n    notes: \"CoRL 2025 accepted. Pioneering work in VLA interpretability.\"\n\n  - id: molinari2025\n    title: \"Emergent World Representations in OpenVLA\"\n    authors: \"Marco Molinari, Leonardo Nevali, Saharsha Navani, Omar G. Younis\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2509.24559\"\n    category: direct-competitor\n    role: context\n    key_findings: >\n      OpenVLA implicitly learns a world model. Embedding arithmetic tests state transition knowledge;\n      linear/non-linear probes show statistically significant state transition prediction ability across layers.\n      SAE pipeline analyzes fine-grained world model structure.\n    relevance_to_us: >\n      Also OpenVLA probing work. They study world model, we study instruction conditioning.\n      Their layer-wise probe results can be compared with our layer-wise RSA.\n    novelty_gap: >\n      No language/instruction analysis. No trained vs untrained comparison.\n      Only focuses on state transitions, not goal/instruction representation.\n    notes: \"Submitted 2025-09-29. Has OpenReview discussion.\"\n\n  - id: lu2025\n    title: \"Probing a Vision-Language-Action Model for Symbolic States and Integration into a Cognitive Architecture\"\n    authors: \"Hong Lu, Hengxu Li, Prithviraj Singh Shahani, Stephanie Herbers, Matthias Scheutz\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2502.04558\"\n    category: direct-competitor\n    role: methodology\n    key_findings: >\n      Probes OpenVLA hidden layers to extract symbolic representations (object properties, relations, action states).\n      LIBERO-spatial pick-and-place probing accuracy > 0.90 across most layers.\n      Integration with cognitive architecture improves interpretability and robustness.\n    relevance_to_us: >\n      Directly related methodology: both use linear probes on OpenVLA layers on LIBERO.\n      Their finding that symbolic states are decodable (>0.90) is consistent with our goal classification at 100%.\n    novelty_gap: >\n      Only trained model probing, no untrained control.\n      Only LIBERO-spatial single task, no cross-task/cross-condition analysis.\n      No instruction conditioning source analysis.\n    notes: \"Submitted 2025-02-06. Tufts University.\"\n\n  - id: fang_intention2025\n    title: \"From Intention to Execution: Probing the Generalization Boundaries of Vision-Language-Action Models\"\n    authors: \"Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2506.09930\"\n    category: direct-competitor\n    role: context\n    key_findings: >\n      Unified probing suite (50 simulation tasks, 10 subcategories) evaluating VLA generalization boundaries.\n      VLM backbone provides robust perceptual understanding + high-level planning (good intentions),\n      but cannot reliably translate to precise motor execution (perception-to-action gap).\n      Action data fine-tuning erodes original VLM generalist reasoning abilities.\n    relevance_to_us: >\n      \"Fine-tuning erodes VLM reasoning\" echoes our \"training doesn't improve representation\" finding.\n      They discover intention != execution at behavioral level; we discover\n      training ~= untrained in representation structure.\n    novelty_gap: >\n      Behavioral-level probing (success rates), not representation-level analysis.\n      No trained vs untrained representation structure comparison.\n    notes: \"Submitted 2025-06-11. INT-ACT benchmark open-sourced. NYU/ai4ce team.\"\n\n  # ============================================================\n  # DIRECT COMPETITORS — Language Grounding / Counterfactual\n  # ============================================================\n  - id: fang_cf2026\n    title: \"When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs\"\n    authors: \"Yu Fang, Yuchun Feng, Dong Jing, Jiaqi Liu, Yue Yang, Zhenyu Wei, Daniel Szafir, Mingyu Ding\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2602.17659\"\n    category: direct-competitor\n    role: competitor\n    key_findings: >\n      Introduces LIBERO-CF counterfactual benchmark. VLAs exhibit severe counterfactual failures:\n      vision shortcuts + dataset biases cause models to ignore language intent.\n      OpenVLA-OFT: 4.7% grounding rate, 0.4% success rate.\n      Best model: 30.8% grounding rate, 13.2% success rate.\n      Proposes Counterfactual Action Guidance (CAG) dual-branch inference scheme.\n    relevance_to_us: >\n      Directly validates \"language encoded but not used\" severity under counterfactual settings.\n      Their behavioral findings complement our representation-level findings.\n      They test OpenVLA-OFT — same checkpoint issue as Grant 2026.\n    novelty_gap: >\n      Pure behavioral benchmark, no representation analysis.\n      No trained vs untrained comparison. No instruction pathway causal analysis.\n    notes: \"Submitted 2026-02-19. LIBERO-CF has 4 sub-suites (CF-Spatial, CF-Object, CF-Long, CF-OOD).\"\n\n  - id: hou2026\n    title: \"LangGap: Diagnosing and Closing the Language Gap in Vision-Language-Action Models\"\n    authors: \"Yuchen Hou, Lin Zhao\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.00592\"\n    category: direct-competitor\n    role: context\n    key_findings: >\n      SOTA VLAs achieve >95% on standard benchmarks but largely ignore language instructions.\n      Four-dimensional semantic perturbation method exposes language understanding deficits.\n      LIBERO assigns only 1 task per layout, so models dont need to understand language.\n      LangGap benchmark forces multi-task shared layouts; data augmentation improves from 0% to 90%.\n    relevance_to_us: >\n      Systematic diagnosis of \"VLAs ignore language\" supports our story:\n      instruction conditioning comes from input pathway, not training — even trained VLAs dont truly leverage language.\n    novelty_gap: >\n      Behavioral-level diagnosis + data augmentation solution. No representation analysis.\n      No trained vs untrained comparison. No input pathway causal analysis.\n    notes: \"Submitted 2026-02-28. GitHub open-sourced.\"\n\n  # ============================================================\n  # METHOD COMPONENT — RSA, CKA, Linear Probing\n  # ============================================================\n  - id: kriegeskorte2008\n    title: \"Representational Similarity Analysis - Connecting the Branches of Systems Neuroscience\"\n    authors: \"Nikolaus Kriegeskorte, Marieke Mur, Peter Bandettini\"\n    year: 2008\n    venue: \"Frontiers in Systems Neuroscience\"\n    arxiv_id: null\n    doi: \"10.3389/neuro.06.004.2008\"\n    category: method-component\n    role: methodology\n    key_findings: >\n      Introduces Representational Dissimilarity Matrix (RDM) framework for comparing multi-channel\n      neural activity measurements with computational models and behavior.\n      Validated on fMRI visual cortex data.\n    relevance_to_us: \"RSA is one of our core analysis methods for comparing trained/untrained/DINO representation structures.\"\n    novelty_gap: null\n    notes: \"Original RSA paper. 5000+ citations.\"\n\n  - id: kornblith2019\n    title: \"Similarity of Neural Network Representations Revisited\"\n    authors: \"Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton\"\n    year: 2019\n    venue: \"ICML 2019\"\n    arxiv_id: \"1905.00414\"\n    category: method-component\n    role: methodology\n    key_findings: >\n      Introduces Centered Kernel Alignment (CKA) as representation similarity metric.\n      CKA reliably identifies representation correspondences across differently initialized networks,\n      outperforming CCA-based methods.\n    relevance_to_us: >\n      CKA is one of our core tools for comparing trained vs untrained representations.\n      Deep-layer CKA reaching 0.86 demonstrates high representation similarity.\n    novelty_gap: null\n    notes: \"Google Brain. CKA is now standard for representation comparison.\"\n\n  - id: alain2017\n    title: \"Understanding Intermediate Layers Using Linear Classifier Probes\"\n    authors: \"Guillaume Alain, Yoshua Bengio\"\n    year: 2017\n    venue: \"ICLR 2017 Workshop\"\n    arxiv_id: \"1610.01644\"\n    category: method-component\n    role: methodology\n    key_findings: >\n      Proposes linear classifier probes to monitor feature suitability for classification at every layer.\n      Linear separability increases monotonically along network depth.\n      Validated on Inception v3 and ResNet-50.\n    relevance_to_us: \"Linear probing is the methodological foundation for our goal classification and action prediction experiments.\"\n    novelty_gap: null\n    notes: \"Foundational probing methodology work.\"\n\n  # ============================================================\n  # VISION ENCODERS — SigLIP, DINOv2, CLIP\n  # ============================================================\n  - id: zhai2023_siglip\n    title: \"Sigmoid Loss for Language Image Pre-Training\"\n    authors: \"Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, Lucas Beyer\"\n    year: 2023\n    venue: \"ICCV 2023\"\n    arxiv_id: \"2303.15343\"\n    category: vision-encoder\n    role: baseline\n    verified: true\n    key_findings: >\n      Replaces softmax contrastive loss with pairwise sigmoid loss for VL pretraining.\n      Eliminates global batch normalization, enabling smaller batch training.\n      SigLIP-SO400M achieves competitive zero-shot performance with simpler training.\n    relevance_to_us: >\n      SigLIP-SO400M is OpenVLA's frozen vision encoder. Our RSA=0.615 for SigLIP+Projector\n      shows this encoder provides dominant action-relevant geometric structure.\n    novelty_gap: null\n    notes: \"Google. OpenVLA uses SigLIP-SO400M/14 variant.\"\n\n  - id: oquab2024_dinov2\n    title: \"DINOv2: Learning Robust Visual Features without Supervision\"\n    authors: \"Maxime Oquab, Timothée Darcet, Théo Moutakanni, et al.\"\n    year: 2024\n    venue: \"TMLR 2024\"\n    arxiv_id: \"2304.07193\"\n    category: vision-encoder\n    role: baseline\n    verified: true\n    key_findings: >\n      Self-supervised ViT trained on curated 142M image dataset (LVD-142M).\n      Produces general-purpose features competitive with task-specific models.\n      No language supervision — purely vision self-supervised.\n    relevance_to_us: >\n      Vision-only baseline in our analysis. DINO RSA=0.388 << SigLIP 0.615,\n      but DINO R²=0.712 ≈ Projector R²=0.706 — key geometric-functional dissociation.\n    novelty_gap: null\n    notes: \"Meta AI. DINOv2 ViT-L/14 used as vision-only control.\"\n\n  - id: radford2021_clip\n    title: \"Learning Transferable Visual Models From Natural Language Supervision\"\n    authors: \"Alec Radford, Jong Wook Kim, Chris Hallacy, et al.\"\n    year: 2021\n    venue: \"ICML 2021\"\n    arxiv_id: \"2103.00020\"\n    category: vision-encoder\n    role: baseline\n    verified: true\n    key_findings: >\n      Contrastive language-image pretraining on 400M image-text pairs.\n      Zero-shot transfer competitive with supervised baselines.\n      Pioneering VL pretraining approach.\n    relevance_to_us: >\n      CLIP ViT-L/14 RSA=0.557 confirms VL pretraining universality:\n      both CLIP (0.557) and SigLIP+Proj (0.615) >> DINO (0.388).\n      Action-relevant geometric structure is a universal product of VL pretraining.\n    novelty_gap: null\n    notes: \"OpenAI. CLIP ViT-L/14 used as VL pretraining generalization control (plan_012).\"\n\n  # ============================================================\n  # BACKGROUND — VLM Design, Frozen Encoders, Multi-modal Fusion\n  # ============================================================\n  - id: karamcheti2024\n    title: \"Prismatic VLMs: Investigating the Design Space of Visually-Conditioned Language Models\"\n    authors: \"Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Percy Liang, Thomas Kollar, Dorsa Sadigh\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2402.07865\"\n    category: background\n    role: baseline\n    key_findings: >\n      Systematic investigation of VLM design space: pretrained visual representations, base vs instruct-tuned LM, etc.\n      Different vision encoder ensembles (SigLIP, DINOv2) improve performance.\n      OpenVLA is directly built on the Prismatic architecture.\n    relevance_to_us: >\n      OpenVLA's VLM backbone origin. The SigLIP+DINOv2 fusion design choice\n      is the architectural basis for our analysis of \"frozen vision encoder carries instruction conditioning.\"\n    novelty_gap: >\n      VLM design space exploration, no VLA-specific representation analysis.\n      No trained vs untrained comparison.\n    notes: \"Significant author overlap with OpenVLA team.\"\n\n  - id: vla_survey2025\n    title: \"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges\"\n    authors: \"Multiple authors\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2505.04769\"\n    category: background\n    role: context\n    key_findings: >\n      Comprehensive survey of 100+ VLA architectures, 26 major VLA datasets.\n      Large-scale quantitative analysis linking model design choices to normalized performance.\n      Covers fusion strategy, action representation, encoder selection.\n    relevance_to_us: \"Provides VLA landscape for positioning our work in the representation analysis sub-direction.\"\n    novelty_gap: \"Survey, no original experimental analysis.\"\n    notes: \"Most comprehensive VLA survey as of 2025-05.\"\n\n  # ============================================================\n  # EVALUATION — LIBERO Benchmark Ecosystem\n  # ============================================================\n  - id: liu2023_libero\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, Peter Stone\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    arxiv_id: \"2306.03310\"\n    category: evaluation\n    role: baseline\n    key_findings: >\n      130 tasks across 4 suites (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long).\n      Procedural generation + skill blending + human teleoperation demonstrations.\n      Lifelong learning benchmark with knowledge transfer evaluation.\n    relevance_to_us: \"Our primary experimental platform. LIBERO-10 (fine-tuning) + LIBERO-Goal (OOD test).\"\n    novelty_gap: null\n    notes: \"NeurIPS 2023 Datasets and Benchmarks track.\"\n\n  - id: fei2025_libero_plus\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    authors: \"Senyu Fei, Siyin Wang, Junhao Shi, et al.\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2510.13626\"\n    category: evaluation\n    role: context\n    key_findings: >\n      7-dimension controlled perturbations expose VLA fragility.\n      Performance drops from 95% to <30% (camera viewpoint, robot initial state most sensitive).\n      Models are insensitive to language variations — largely ignore language instructions.\n      Positional bias over genuine semantic understanding.\n    relevance_to_us: >\n      \"Models ignore language instructions\" is consistent with our finding that\n      training doesnt improve representation structure — VLAs have not truly learned language grounding.\n    novelty_gap: \"Behavioral robustness analysis, no representation-level analysis.\"\n    notes: \"Submitted 2025-10. OpenMOSS team.\"\n\n  - id: zhou2025_libero_pro\n    title: \"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization\"\n    authors: \"Xueyang Zhou, Yangming Xu, Guiyao Tie, et al.\"\n    year: 2025\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2510.03827\"\n    category: evaluation\n    role: context\n    key_findings: >\n      Standard LIBERO >90% accuracy, but generalized setting collapses to 0.0%.\n      Exposes reliance on rote memorization (action sequences + environment layouts)\n      rather than genuine task understanding or environmental perception.\n    relevance_to_us: >\n      \"Memorization not understanding\" supports our story:\n      VLA training improves action sequence memorization, not representation structure.\n    novelty_gap: \"Behavioral evaluation, no representation analysis.\"\n    notes: \"Submitted 2025-10.\"\n\n  - id: libero_para2026\n    title: \"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models\"\n    authors: \"Multiple authors\"\n    year: 2026\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2603.28301\"\n    category: evaluation\n    role: context\n    key_findings: >\n      7 VLA configurations (0.6B-7.5B) show 22-52pp performance degradation under paraphrasing.\n      80-96% of failures from planning-level trajectory divergence (not execution errors),\n      indicating paraphrasing disrupts task identification.\n      Synonym substitution alone causes large drops — relies on surface-level matching, not semantic grounding.\n    relevance_to_us: >\n      Further confirms VLAs lack true language grounding.\n      Complements our \"instruction conditioning comes from input pathway structure, not semantic training.\"\n    novelty_gap: \"Paraphrase robustness diagnosis, no representation analysis.\"\n    notes: \"Submitted 2026-03-30.\"\n\n  # ============================================================\n  # RELATED ARCHITECTURE — VLA Models\n  # ============================================================\n  - id: kim2024_openvla\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, et al.\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2406.09246\"\n    category: related-architecture\n    role: baseline\n    key_findings: >\n      7B-param VLA trained on 970k real-world robot demonstrations (Open X-Embodiment).\n      Llama 2 7B backbone + DINOv2+SigLIP fused vision encoder.\n      Outperforms RT-2-X (55B) by 16.5% absolute with 7x fewer parameters.\n    relevance_to_us: >\n      Our analysis target. All probing/RSA/CKA experiments use OpenVLA-7B.\n      Architecture details (frozen SigLIP, Llama 2 backbone) directly affect our interpretation\n      of \"input pathway vs training.\"\n    novelty_gap: null\n    notes: \"Stanford/Toyota/Google. Open-source checkpoints + training code.\"\n\n  - id: brohan2023_rt2\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Anthony Brohan et al.\"\n    year: 2023\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2307.15818\"\n    category: related-architecture\n    role: context\n    key_findings: >\n      Co-fine-tunes VLM (PaLM-E 55B) on robotic trajectory data + internet-scale VL tasks.\n      Robot actions represented as text tokens.\n      Demonstrates emergent capabilities: novel object generalization, chain-of-thought reasoning.\n    relevance_to_us: >\n      Pioneering VLA architecture. RT-2 uses PaLM-E, OpenVLA uses Llama 2,\n      but shares the \"LLM backbone + frozen vision encoder\" core design.\n      Our findings may generalize to similar architectures.\n    novelty_gap: \"No representation analysis. No trained vs untrained comparison.\"\n    notes: \"Google DeepMind. 55B params, not open-source.\"\n\n  - id: ghosh2024_octo\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Octo Model Team, Dibya Ghosh, Homer Walke, Karl Pertsch, et al.\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2405.12213\"\n    category: related-architecture\n    role: context\n    key_findings: >\n      Transformer-based diffusion policy pretrained on 800k robot episodes (Open X-Embodiment).\n      Lightweight CNN vision encoder + language model for text instructions.\n      27M (Small) / 93M (Base) params, consumer GPU fine-tuning.\n    relevance_to_us: >\n      Alternative VLA architecture (not LLM-based). Grant 2026 tests include Octo.\n      If our findings generalize to Octo, the input pathway effect is cross-architectural.\n    novelty_gap: \"No representation analysis. No frozen encoder analysis.\"\n    notes: \"Berkeley. Author overlap with OpenVLA.\"\n\n  - id: black2024_pi0\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Kevin Black et al.\"\n    year: 2024\n    venue: \"arXiv preprint\"\n    arxiv_id: \"2410.24164\"\n    category: related-architecture\n    role: context\n    key_findings: >\n      Flow matching action head (not autoregressive tokens), 50Hz continuous trajectories.\n      Pre-trained VLM backbone + flow matching combination.\n      7 robotic platforms, 68 tasks. Real-world dexterous manipulation.\n    relevance_to_us: >\n      pi0 uses continuous flow matching vs discrete tokens — different action representation.\n      Grant 2026 and Haon 2025 both tested Pi0/pi0.5, enabling cross-reference with our OpenVLA results.\n    novelty_gap: \"No representation structure analysis.\"\n    notes: \"Physical Intelligence. Commercial frontier VLA.\"\n\n# ============================================================\n# CATEGORY INDEX\n# ============================================================\ncategories:\n  direct-competitor:\n    description: \"VLA representation / interpretability / language grounding analysis\"\n    papers:\n      - grant2026\n      - swann2026\n      - rizzardo2026\n      - haon2025\n      - molinari2025\n      - lu2025\n      - fang_intention2025\n      - fang_cf2026\n      - hou2026\n\n  method-component:\n    description: \"RSA, CKA, linear probing methodological references\"\n    papers:\n      - kriegeskorte2008\n      - kornblith2019\n      - alain2017\n\n  vision-encoder:\n    description: \"Vision encoder architectures used in our analysis (SigLIP, DINOv2, CLIP)\"\n    papers:\n      - zhai2023_siglip\n      - oquab2024_dinov2\n      - radford2021_clip\n\n  background:\n    description: \"VLM design space, frozen encoder effects, multi-modal fusion\"\n    papers:\n      - karamcheti2024\n      - vla_survey2025\n\n  evaluation:\n    description: \"LIBERO benchmark ecosystem and VLA robustness evaluation\"\n    papers:\n      - liu2023_libero\n      - fei2025_libero_plus\n      - zhou2025_libero_pro\n      - libero_para2026\n\n  related-architecture:\n    description: \"VLA model architectures (OpenVLA, RT-2, Octo, pi0)\"\n    papers:\n      - kim2024_openvla\n      - brohan2023_rt2\n      - ghosh2024_octo\n      - black2024_pi0\n\n# ============================================================\n# SYNTHESIS: OUR NOVELTY POSITION\n# ============================================================\nsynthesis:\n  our_core_claim: \"Instruction Input Pathway Drives Conditioning, Not Training\"\n\n  what_others_have_done:\n    behavioral_level:\n      - \"Grant 2026: vision pathway dominates, language 'encoded but not used' (activation injection)\"\n      - \"LIBERO-CF/LangGap/LIBERO-Plus: VLAs ignore language instructions (counterfactual/robustness tests)\"\n      - \"LIBERO-PRO: models rely on memorization not understanding\"\n      - \"Fang 2025: fine-tuning erodes VLM reasoning (intention != execution)\"\n    representation_level:\n      - \"Swann 2026: SAE features mostly memorized sequences, some interpretable (OpenVLA)\"\n      - \"Molinari 2025: world model emerges in middle layers (OpenVLA)\"\n      - \"Lu 2025: symbolic states decodable with >0.90 accuracy (OpenVLA + LIBERO)\"\n      - \"Haon 2025: sparse semantic directions causally linked to actions (Pi0 + OpenVLA)\"\n      - \"Rizzardo 2026: feature-observability and controllability (pi0.5 + OpenVLA)\"\n\n  what_nobody_has_done:\n    - \"Trained vs untrained VLA representation comparison (we find trained ~= untrained >> DINO)\"\n    - \"Instruction input pathway vs LLM training separation analysis (6 probing rounds + RSA all consistent)\"\n    - \"Systematic layer-wise RSA/CKA comparison of trained/untrained/DINO representation structures\"\n    - \"Instruction ablation causal verification: removing instruction drops RSA to DINO level\"\n\n  key_differentiation_from_grant2026: >\n    Grant 2026 compares different VLA models (architectural differences);\n    we compare trained vs untrained within the same model (training effect isolation).\n    Grant finds \"language encoded but not used\" (behavioral level);\n    we find \"conditioning comes from input pathway, not training\" (representation level).\n    Complementary, not competing. Related Work must qualify OFT vs standard fine-tuning difference.\n",
      "numLines": 591,
      "startLine": 1,
      "totalLines": 591
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
Now I have all the context I need. Let me also quickly read the method and experiments sections to make sure I don't miss any positioning details.

Let me now write the Related Work section. Key considerations:

1. 5 paragraphs organized by \paragraph{}
2. ~0.75-1 page CoRL format
3. Positioning-focused, not survey
4. Available \cite{} keys: kim2024_openvla, karamcheti2024, brohan2023_rt2, liu2023_libero, kriegeskorte2008, kornblith2019, alain2017, zhai2023_siglip, oquab2024_dinov2, radford2021_clip, grant2026, haon2025


5. Papers not in .bib: mentioned in natural language (e.g., "Lu et al.~(2025)") without \cite{}
6. End with a paragraph stating our unique contribution

I'll structure this around five core themes: vision-language-action models, behavioral analysis of VLAs, mechanistic interpretability approaches, vision encoder representations, and representational similarity analysis. Then I'll close with how our work fills a gap at the intersection of these areas.

Let me draft this carefully, keeping each paragraph tight and focused on positioning rather than surveying the entire landscape.

Now I'm cataloging which papers I need to reference—some like Swann et al., Rizzardo et al., Molinari et al., and Lu et al. aren't in the bibliography, so I'll cite them inline. Others like the OpenVLA and RT-2 papers are already in the bib, along with the vision encoder work from CLIP, SigLIP, and DINOv2, plus the representational analysis methods like RSA and CKA.

I'm drafting the related work section now, keeping in mind the guidelines about avoiding cherry-picking claims and only using "significantly" when I have statistical backing. Let me write out the VLA models paragraph first, covering how RT-2 pioneered the approach with PaLM-E and how OpenVLA scaled it up with open weights and a larger demonstration dataset.

Writing the related work section... that chains frozen vision encoders with a Llama-2 backbone. These architectures share a core assumption---that LLM fine-tuning injects action-relevant knowledge---that our work directly tests at the representational level.

\paragraph{Behavioral analysis of VLAs.}
A growing body of work reveals that VLAs rely disproportionately on visual input. \cite{grant2026} showed across six VLA architectures that visual pathways dominate action generation, with language instructions ``encoded but not used'' when visual context uniquely specifies the task. Hou and Zhao~(2026) diagnosed this systematically via semantic perturbations, finding that SOTA VLAs achieve $>$95\% on standard benchmarks while largely ignoring language. Fei et al.~(2025) demonstrated similar insensitivity through controlled robustness perturbations on LIBERO. These studies establish the behavioral phenomenon; our work provides a representational account by showing that action-relevant geometric structure originates in the frozen vision encoder and is invariant to both LLM training and instruction content.

\paragraph{Mechanistic interpretability of VLAs.}
Recent work has begun probing VLA internals. \cite{haon2025} identified sparse semantic directions in OpenVLA activations that are causally linked to action selection, enabling real-time behavior steering without fine-tuning. Swann et al.~(2026) applied sparse autoencoders to OpenVLA, finding that most extracted features correspond to memorized training sequences, with some interpretable motion primitives. Rizzardo et al.~(2026) introduced feature-observability and controllability concepts for VLA steering. Lu et al.~(2025) probed OpenVLA hidden layers on LIBERO, finding symbolic states decodable with $>$0.90 accuracy. Several recent studies have examined VLA internals through various mechanistic lenses---from identifying causal action-selection directions to extracting sparse features and probing for decodable symbolic representations.

I'm now looking at how different vision encoder architectures contribute to this picture. We're comparing three encoders with distinct pretraining approaches: SigLIP, which uses sigmoid loss for vision-language alignment and serves as OpenVLA's frozen backbone; CLIP, an independent vision-language baseline trained on massive image-text pairs; and DINOv2, a vision-only self-supervised model without language supervision. This comparison lets us isolate what's specific to language-aligned pretraining versus what emerges from pure visual learning.

The key insight is that fine-tuning doesn't actually improve the geometric structure the model inherits from its vision encoder—in fact, prior work shows VLA fine-tuning can degrade the original VLM's reasoning abilities. For measuring how representations change across components, I'm using both geometric metrics like RSA and CKA to compare representation geometry, plus linear probes to measure functional decodability. These complementary approaches are crucial because they can diverge—geometric similarity doesn't always predict functional performance.

What distinguishes this analysis is the component-level decomposition that separately evaluates the vision encoder, projector, and LLM layers rather than treating the model as a monolith, combined with trained-versus-untrained controls that show geometric structure persists regardless of fine-tuning while functional routing depends on it. By layering geometric metrics, functional probes, and instruction ablations together, I'm building converging evidence that the vision encoder is where action-relevant structure originates. Verifying all the citation keys are correct and checking that the natural language author mentions match what's used in the Introduction and Discussion sections.

Now I'm making sure the positioning stays consistent—the frozen encoder as the source of geometric structure, the LLM functioning as a router rather than a knowledge source, and how training shapes the routing policy. The Related Work section aligns with these core claims.

Since this is descriptive rather than experimental, I'm not running into issues with the constraint about needing trained and untrained data before making conclusions.

I should tighten up the writing though. Looking at the sentence counts, the Behavioral and Mechanistic sections are running long—I need to compress those down to the target range of 2-4 sentences per category. I'm completing the thought about how VLAs rely heavily on visual input while language instructions are largely ignored, and our work explains this at the representational level by showing that action-relevant structure comes from the frozen vision encoder. For mechanistic interpretability, recent work has identified sparse semantic directions in model activations that causally control action selection, and other studies are examining how information flows through VLA architectures.

Now I'm looking at the vision encoders we're using to analyze this—we're comparing three different pretraining approaches: a vision-language encoder from OpenVLA, an independent vision-language baseline, and a vision-only encoder, all using the same ViT-L architecture.

By contrasting the vision-language pretrained encoders with the vision-only one, I can isolate how much language grounding actually contributes to the action-relevant structure. This connects to recent work showing that fine-tuning VLAs can actually degrade their reasoning abilities, which aligns with what we're finding—that fine-tuning doesn't meaningfully improve the geometric structure that comes from the vision encoder itself.

For measuring representational structure, I'm using both RSA and CKA as complementary geometric metrics, combined with linear probes to evaluate functional performance. This dual approach is important because we're discovering that geometric alignment and functional decodability don't always track together, which tells us something meaningful about what makes representations useful for VLA design.

Our contribution stands out in a few key ways. We're doing component-level representational decomposition—breaking down and separately measuring how much each part contributes to the overall structure. I'm checking the sentence counts across each section to make sure the paper stays within the target page length for CoRL format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "82b1efc0-f983-4425-aa19-84124460e094",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJr8gdKGsae8AFWJtvm7at",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19496,
      "cache_read_input_tokens": 24444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19496
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

Now let me write the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "30a49b30-9b5c-4bfc-95c1-deef762db5ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJr8gdKGsae8AFWJtvm7at",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19496,
      "cache_read_input_tokens": 24444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19496
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

<details open><summary>🔧 Tool call — Write · `toolu_01RmpPRDda6FehacMwSQBE1d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstration data to produce action-conditioned policies.\nRT-2~\\cite{brohan2023_rt2} pioneered this paradigm by co-fine-tuning PaLM-E on robotic trajectories; OpenVLA~\\cite{kim2024_openvla} extended it with open-source weights and 970K demonstrations, built on the Prismatic VLM architecture~\\cite{karamcheti2024} that chains frozen vision encoders with a Llama-2 backbone.\nThese architectures share a core design assumption---that LLM fine-tuning injects action-relevant knowledge---that our work tests at the representational level.\n\n\\paragraph{Behavioral analysis of VLAs.}\nA growing body of work reveals that VLAs rely disproportionately on visual input.\n\\cite{grant2026} showed across six architectures that visual pathways dominate action generation, with language instructions ``encoded but not used'' when visual context uniquely specifies the task.\nHou and Zhao~(2026) and Fei et al.~(2025) corroborated this through semantic perturbations and controlled robustness tests on LIBERO, finding that models largely ignore language instructions.\nThese studies establish the behavioral phenomenon; we provide a representational account showing that action-relevant geometric structure originates in the frozen vision encoder and is invariant to both LLM training and instruction content.\n\n\\paragraph{Mechanistic interpretability of VLAs.}\nRecent work has probed VLA internals from several angles.\n\\cite{haon2025} identified sparse semantic directions in OpenVLA causally linked to action selection, enabling activation steering without fine-tuning.\nSwann et al.~(2026) applied sparse autoencoders, finding features dominated by memorized sequences with some interpretable motion primitives; Rizzardo et al.~(2026) introduced feature-observability and controllability concepts for VLA steering.\nLu et al.~(2025) and Molinari et al.~(2025) probed OpenVLA layers, extracting symbolic states and world-model representations respectively.\nThese studies analyze individual features or single components; we complement them with a systematic decomposition quantifying each architectural component's contribution to action structure, with trained-versus-untrained controls absent from all prior work.\n\n\\paragraph{Vision encoder representations.}\nOur analysis leverages three encoders spanning different pretraining objectives: SigLIP~\\cite{zhai2023_siglip} (OpenVLA's frozen VL encoder), CLIP~\\cite{radford2021_clip} (independent VL baseline), and DINOv2~\\cite{oquab2024_dinov2} (vision-only control), all at ViT-L/14 scale.\nComparing VL-pretrained and vision-only encoders at matched architecture isolates the contribution of language grounding to action-relevant structure.\nRelatedly, Fang et al.~(2025) showed that VLA fine-tuning erodes original VLM reasoning abilities, consistent with our finding that fine-tuning does not improve the geometric structure inherited from the vision encoder.\n\n\\paragraph{Representational similarity analysis.}\nWe adopt RSA~\\cite{kriegeskorte2008} and CKA~\\cite{kornblith2019} as complementary geometric metrics, paired with linear probes~\\cite{alain2017} for functional evaluation.\nThis multi-metric approach proves essential: we show that geometric alignment and functional decodability can dissociate (e.g., DINOv2 matches VL encoders on probe $R^2$ but not RSA), revealing distinct aspects of representation quality relevant to VLA design.\n\n\\paragraph{Positioning.}\nOur work is distinguished from prior VLA analyses by three features.\nFirst, we perform a \\emph{component-level} representational decomposition---separately quantifying vision encoder, projector, and each LLM layer---rather than analyzing individual features or the model as a whole.\nSecond, we introduce trained-versus-untrained controls that isolate the effect of VLA fine-tuning, revealing that geometric structure is training-invariant while functional routing requires it.\nThird, we combine geometric and functional metrics with instruction ablation, providing converging evidence that the vision encoder is the \\emph{source} and the LLM is the \\emph{router} of action-relevant structure---complementing the behavioral evidence of \\cite{grant2026}, the mechanistic directions of \\cite{haon2025}, and the feature-level analyses of Swann et al.~(2026).\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "a0b9908f-a0f1-4e69-bc02-ea4a18ac73af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJr8gdKGsae8AFWJtvm7at",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19496,
      "cache_read_input_tokens": 24444,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19496
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

_source line 18 · 2026-05-16T03:11:25.209Z_

<details><summary>↩ Tool result · `toolu_01RmpPRDda6FehacMwSQBE1d`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "7b069d99-8a09-476c-9289-55235f890dc5",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstration data to produce action-conditioned policies.\nRT-2~\\cite{brohan2023_rt2} pioneered this paradigm by co-fine-tuning PaLM-E on robotic trajectories; OpenVLA~\\cite{kim2024_openvla} extended it with open-source weights and 970K demonstrations, built on the Prismatic VLM architecture~\\cite{karamcheti2024} that chains frozen vision encoders with a Llama-2 backbone.\nThese architectures share a core design assumption---that LLM fine-tuning injects action-relevant knowledge---that our work tests at the representational level.\n\n\\paragraph{Behavioral analysis of VLAs.}\nA growing body of work reveals that VLAs rely disproportionately on visual input.\n\\cite{grant2026} showed across six architectures that visual pathways dominate action generation, with language instructions ``encoded but not used'' when visual context uniquely specifies the task.\nHou and Zhao~(2026) and Fei et al.~(2025) corroborated this through semantic perturbations and controlled robustness tests on LIBERO, finding that models largely ignore language instructions.\nThese studies establish the behavioral phenomenon; we provide a representational account showing that action-relevant geometric structure originates in the frozen vision encoder and is invariant to both LLM training and instruction content.\n\n\\paragraph{Mechanistic interpretability of VLAs.}\nRecent work has probed VLA internals from several angles.\n\\cite{haon2025} identified sparse semantic directions in OpenVLA causally linked to action selection, enabling activation steering without fine-tuning.\nSwann et al.~(2026) applied sparse autoencoders, finding features dominated by memorized sequences with some interpretable motion primitives; Rizzardo et al.~(2026) introduced feature-observability and controllability concepts for VLA steering.\nLu et al.~(2025) and Molinari et al.~(2025) probed OpenVLA layers, extracting symbolic states and world-model representations respectively.\nThese studies analyze individual features or single components; we complement them with a systematic decomposition quantifying each architectural component's contribution to action structure, with trained-versus-untrained controls absent from all prior work.\n\n\\paragraph{Vision encoder representations.}\nOur analysis leverages three encoders spanning different pretraining objectives: SigLIP~\\cite{zhai2023_siglip} (OpenVLA's frozen VL encoder), CLIP~\\cite{radford2021_clip} (independent VL baseline), and DINOv2~\\cite{oquab2024_dinov2} (vision-only control), all at ViT-L/14 scale.\nComparing VL-pretrained and vision-only encoders at matched architecture isolates the contribution of language grounding to action-relevant structure.\nRelatedly, Fang et al.~(2025) showed that VLA fine-tuning erodes original VLM reasoning abilities, consistent with our finding that fine-tuning does not improve the geometric structure inherited from the vision encoder.\n\n\\paragraph{Representational similarity analysis.}\nWe adopt RSA~\\cite{kriegeskorte2008} and CKA~\\cite{kornblith2019} as complementary geometric metrics, paired with linear probes~\\cite{alain2017} for functional evaluation.\nThis multi-metric approach proves essential: we show that geometric alignment and functional decodability can dissociate (e.g., DINOv2 matches VL encoders on probe $R^2$ but not RSA), revealing distinct aspects of representation quality relevant to VLA design.\n\n\\paragraph{Positioning.}\nOur work is distinguished from prior VLA analyses by three features.\nFirst, we perform a \\emph{component-level} representational decomposition---separately quantifying vision encoder, projector, and each LLM layer---rather than analyzing individual features or the model as a whole.\nSecond, we introduce trained-versus-untrained controls that isolate the effect of VLA fine-tuning, revealing that geometric structure is training-invariant while functional routing requires it.\nThird, we combine geometric and functional metrics with instruction ablation, providing converging evidence that the vision encoder is the \\emph{source} and the LLM is the \\emph{router} of action-relevant structure---complementing the behavioral evidence of \\cite{grant2026}, the mechanistic directions of \\cite{haon2025}, and the feature-level analyses of Swann et al.~(2026).\n",
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

Related Work 已写入 `docs/paper/related_work.tex`。

结构：6 个 `\paragraph{}`——5 个分类 + 1 个 Positioning 收尾段。12 个已有 bib key 通过 `\cite{}` 引用；Swann、Rizzardo、Lu、Molinari、Hou、Fei、Fang 等不在 `.bib` 中的论文用自然语言提及，无 `\cite{}`。核心定位：与 Grant (behavioral)、Haon (mechanistic directions)、Swann (feature-level SAE) 互补，我们的独特贡献在 component-level decomposition + trained-vs-untrained controls + geometric/functional dual metrics。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "uuid": "a35317aa-3998-4b75-9982-6ca3ef7a400d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019bBqLFExTdYbD9TPhKNGkt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4941,
      "cache_read_input_tokens": 43940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4941
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

_source line 20_

Related Work 已写入 `docs/paper/related_work.tex`。

结构：6 个 `\paragraph{}`——5 个分类 + 1 个 Positioning 收尾段。12 个已有 bib key 通过 `\cite{}` 引用；Swann、Rizzardo、Lu、Molinari、Hou、Fei、Fang 等不在 `.bib` 中的论文用自然语言提及，无 `\cite{}`。核心定位：与 Grant (behavioral)、Haon (mechanistic directions)、Swann (feature-level SAE) 互补，我们的独特贡献在 component-level decomposition + trained-vs-untrained controls + geometric/functional dual metrics。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 88721,
  "duration_api_ms": 89330,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "61587265-fc0a-49c6-874c-78a6b9c627f5",
  "total_cost_usd": 0.4100125,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 37040,
    "cache_read_input_tokens": 80225,
    "output_tokens": 5449,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 37040,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 200,
        "cache_read_input_tokens": 43940,
        "cache_creation_input_tokens": 4941,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4941
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2055,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00215,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 5449,
      "cacheReadInputTokens": 80225,
      "cacheCreationInputTokens": 37040,
      "webSearchRequests": 0,
      "costUSD": 0.4078625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8f33efe2-ebfe-491f-9eaa-661d45e56ac5"
}
```

</details>

---
