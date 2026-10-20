# paper writing method v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_paper_writing_method_v2_20260514T092526.log`
- **Structured JSON:** [`2f91d31b914759402856.json`](../../sessions/2f/2f91d31b914759402856.json)

## Before a recorded user message

35 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
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
  "uuid": "803a145d-bd6e-47d9-bd52-bc50fffdcd2b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
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
    "resetsAt": 1779303600,
    "rateLimitType": "seven_day",
    "utilization": 0.3,
    "isUsingOverage": false
  },
  "uuid": "6ffda458-855b-4f6c-a8b5-6c7f0ab5c1bb",
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f"
}
```

---

### Assistant

_source line 4_

I'll start by reading the LaTeX writing conventions skill, then draft the method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "e3fe851b-0656-4a5b-b7b0-ce3f488033f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmozC81XfVmuvJHfvmqaAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12781,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12781
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

<details open><summary>🔧 Tool call — Read · `toolu_01AfncmcpPWbuYKPCVB9BxKi`</summary>

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
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "75836cce-ce72-41d2-bd8b-51ee5128a72d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmozC81XfVmuvJHfvmqaAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12781,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12781
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

_source line 6 · 2026-05-14T09:25:41.035Z_

<details><summary>↩ Tool result · `toolu_01AfncmcpPWbuYKPCVB9BxKi`</summary>

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
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "10744acd-97e0-4122-9c9f-cfa2a26eadf7",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01DjEq2C5nu5ixf32tjJHyA6`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "4ca2282f-4556-464f-ba47-889066da1583",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmozC81XfVmuvJHfvmqaAP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12781,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12781
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

_source line 8 · 2026-05-14T09:25:41.170Z_

<details><summary>↩ Tool result · `toolu_01DjEq2C5nu5ixf32tjJHyA6`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "6f03000f-b06f-4fb7-a990-5876812d85f1",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 9,
    "numFiles": 0,
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
Let me also check if there's an existing experiments.tex or any other paper files to ensure consistency with the labels and references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "8d22d991-ae55-48fc-a40d-85e5fb6284fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVX5ArhMFzAJ852sCFXPjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5675,
      "cache_read_input_tokens": 24622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5675
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

Let me check existing paper files for reference consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "e72a15ff-758c-42ca-b5b4-b6543505e366",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVX5ArhMFzAJ852sCFXPjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5675,
      "cache_read_input_tokens": 24622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5675
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

<details open><summary>🔧 Tool call — Glob · `toolu_018ttbKpW8CqpHGSh5HihF5P`</summary>

```json
{
  "pattern": "**/*paper*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "c6270fb7-b8ce-49eb-8090-cf6bca1d713c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVX5ArhMFzAJ852sCFXPjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5675,
      "cache_read_input_tokens": 24622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5675
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

_source line 12 · 2026-05-14T09:25:47.008Z_

<details><summary>↩ Tool result · `toolu_018ttbKpW8CqpHGSh5HihF5P`</summary>

```text
artifacts/_project/report/paper_data_tables.md
artifacts/_project/paper/paper_outline.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "89e2068a-c635-4823-ac96-71feba1f4203",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/report/paper_data_tables.md",
      "artifacts/_project/paper/paper_outline.md"
    ],
    "durationMs": 7,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_019HiJCEsqbFJWLcpNSBhFkh`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "1d5fc3aa-4276-4b4d-b8a2-834b2c9ced38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVX5ArhMFzAJ852sCFXPjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5675,
      "cache_read_input_tokens": 24622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5675
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

_source line 14 · 2026-05-14T09:25:47.587Z_

<details><summary>↩ Tool result · `toolu_019HiJCEsqbFJWLcpNSBhFkh`</summary>

```text
artifacts/dream_reports/dream_20260513T153257/best/paper.tex
artifacts/dream_reports/dream_20260513T153257/median/paper.tex
artifacts/dream_reports/dream_20260513T153257/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "8ff85105-a9f6-44e8-9700-5282f880a7ba",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260513T153257/best/paper.tex",
      "artifacts/dream_reports/dream_20260513T153257/median/paper.tex",
      "artifacts/dream_reports/dream_20260513T153257/worst/paper.tex"
    ],
    "durationMs": 10,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_011978Gn9MiZvkdFBsY38tWf`</summary>

```json
{
  "pattern": "**/*experiment*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "f7eb0cb2-a868-4e02-b09e-b42fad09dc1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVX5ArhMFzAJ852sCFXPjf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5675,
      "cache_read_input_tokens": 24622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5675
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

_source line 16 · 2026-05-14T09:25:48.176Z_

<details><summary>↩ Tool result · `toolu_011978Gn9MiZvkdFBsY38tWf`</summary>

```text
artifacts/_project/paper/experiment_tables.md
artifacts/_project/report/experiment_tables.md
artifacts/_project/paper/experiments_draft_dd9866.md
artifacts/_project/paper/experiments_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "3a23b746-4e23-4e41-910e-91077cd8f41d",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/experiment_tables.md",
      "artifacts/_project/report/experiment_tables.md",
      "artifacts/_project/paper/experiments_draft_dd9866.md",
      "artifacts/_project/paper/experiments_draft.md"
    ],
    "durationMs": 21,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_013gmRZPEP4qnQ1QaD2iFMGk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "dd7310b1-a5a0-49f3-927c-3710cc6d2fb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2wwsWGV5Cm9ugfxtuaqVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 30297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 550
      },
      "output_tokens": 67,
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

_source line 18 · 2026-05-14T09:25:51.172Z_

<details><summary>↩ Tool result · `toolu_013gmRZPEP4qnQ1QaD2iFMGk`</summary>

```text
1	# Experiments — Draft v1
2	
3	\section{Experiments}
4	
5	\subsection{Setup}
6	\label{sec:exp-setup}
7	
8	We evaluate on ScienceWorld \cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \S\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.
9	
10	\subsection{Death Avoidance Decomposition}
11	\label{sec:death-decomp}
12	
13	The full performance gap between deterministic and internal strategies across 245 episodes is $\Delta_{\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\Delta_{\text{no\_death}} = +2.84$. The resulting Death Avoidance Factor (\S\ref{sec:daf}) is 90.41\%: approximately 90\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.
14	
15	This concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\Delta_{\text{full}}$ is $r = 0.9698$ ($p = 8.12 \times 10^{-7}$), as shown in Figure~\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\% of episodes compared to 16.3\% for deterministic computation---a 2.6$\times$ ratio that drives the bulk of the observed score difference.
16	
17	The episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \texttt{det\_preferred}, only 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.
18	
19	One task reveals the residual non-death signal. \texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\Delta_{\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\% (internal) and 25\% (deterministic), producing $\Delta_{\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.
20	
21	When both modalities survive, their task performance is near-equivalent ($\Delta_{\text{no\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.
22	
23	\subsection{Baselines}
24	\label{sec:baselines}
25	
26	\begin{table}[t]
27	\centering
28	\small
29	\begin{tabular}{@{}lccc@{}}
30	\toprule
31	Strategy & Score & 95\% CI & Death \% \\
32	\midrule
33	Always-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\
34	Always-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\
35	Random & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\
36	Oracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\
37	\midrule
38	Implicit Router & \multicolumn{3}{c}{[PLACEHOLDER]} \\
39	\bottomrule
40	\end{tabular}
41	\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\% of its decisions match the always-deterministic strategy.}
42	\label{tab:baselines}
43	\end{table}
44	
45	Table~\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\Delta_{\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\% of its routing decisions matching always-deterministic. This \emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\%) proportional to its 50/50 allocation.
46	
47	Keyword-based routing (\S\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\texttt{pick up}, \texttt{move}, \texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\%, degenerating to always-deterministic) or negligible (v2: 4.9\%, v3: 2.8\%, both degenerating to always-internal). No keyword granularity bridges this gap.
48	
49	\subsection{Router Training as Diagnostic}
50	\label{sec:router-diagnostic}
51	
52	A natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.
53	
54	\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.
55	
56	\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\% with balanced accuracy of 79\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\% with internal recall of 51.5\%, revealing a gap between logit-level pattern recognition and generation-level expression. [PLACEHOLDER: ablation-b end-to-end evaluation results for Table~\ref{tab:baselines}.]
57	
58	These results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.
59	
60	\subsection{Limitations}
61	\label{sec:limitations}
62	
63	Our analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "0bbcea7e-816f-4d68-a0dd-288967fa79d7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiments_draft.md",
      "content": "# Experiments — Draft v1\n\n\\section{Experiments}\n\n\\subsection{Setup}\n\\label{sec:exp-setup}\n\nWe evaluate on ScienceWorld \\cite{scienceworld-2022}, a text-based interactive environment for elementary science tasks with sparse terminal rewards and a $-100$ penalty upon agent death. Using the counterfactual methodology described in \\S\\ref{sec:collection}, we collect 245 episode pairs across 11 task types (20--40 episodes per type). The LLM backbone is Qwen2.5-7B-Instruct, served via vLLM, with episodes capped at 30 steps. The internal-reasoning strategy follows the ReAct paradigm \\cite{react-2023}; the deterministic strategy uses the environment simulator for exact state transitions.\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\nThe full performance gap between deterministic and internal strategies across 245 episodes is $\\Delta_{\\text{full}} = +29.60$ points. When we exclude all episodes where either strategy results in agent death, the gap collapses to $\\Delta_{\\text{no\\_death}} = +2.84$. The resulting Death Avoidance Factor (\\S\\ref{sec:daf}) is 90.41\\%: approximately 90\\% of the deterministic strategy's advantage over internal reasoning is attributable to death avoidance rather than superior task performance when both agents survive.\n\nThis concentration is consistent across task types. The Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$), as shown in Figure~\\ref{fig:decomposition}. Knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap for a given task type. The internal strategy dies in 42.9\\% of episodes compared to 16.3\\% for deterministic computation---a 2.6$\\times$ ratio that drives the bulk of the observed score difference.\n\nThe episode-level label distribution reflects this asymmetry. Of 245 episodes, 86 are labeled \\texttt{det\\_preferred}, only 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}. The near-absence of internal-preferred labels---combined with the dominance of no-preference labels---indicates that when internal reasoning does not lead to catastrophic failure, it performs comparably to deterministic computation. The few internal-preferred episodes arise from tasks where deterministic computation's rigid action space occasionally produces suboptimal trajectories despite avoiding death.\n\nOne task reveals the residual non-death signal. \\texttt{find-non-living-thing} ($n=40$) is the only task type with zero deaths under both strategies, yet it shows $\\Delta_{\\text{full}} = +9.58$, entirely from non-death performance differences. This confirms that routing value beyond death avoidance exists: deterministic computation can provide advantages through more accurate state tracking even when agents survive. However, this signal is not the dominant factor across the benchmark. Among the 10 death-prone task types, death avoidance overwhelms non-death differences. For example, \\texttt{measure-melting-point-unknown} ($n=20$) exhibits death rates of 55\\% (internal) and 25\\% (deterministic), producing $\\Delta_{\\text{full}} = +30.05$---a gap driven primarily by the 30-percentage-point death rate differential rather than non-death performance.\n\nWhen both modalities survive, their task performance is near-equivalent ($\\Delta_{\\text{no\\_death}} = +2.84$). The value of deterministic computation in this environment is concentrated in preventing catastrophic failures, not in providing positive task guidance.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-44.89$, $-33.37$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-13.66$, $-5.11$] & 16.3 \\\\\nRandom & $-22.38$ & [$-27.75$, $-17.09$] & 27.8 \\\\\nOracle & $-6.58$ & [$-10.65$, $-2.43$] & 14.3 \\\\\n\\midrule\nImplicit Router & \\multicolumn{3}{c}{[PLACEHOLDER]} \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 task types, 245 episodes). Confidence intervals computed via bootstrap. The oracle selects the higher-scoring strategy per episode; 96.2\\% of its decisions match the always-deterministic strategy.}\n\\label{tab:baselines}\n\\end{table}\n\nTable~\\ref{tab:baselines} reports episode-weighted mean scores and death rates for four unconditional strategies. Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points, consistent with $\\Delta_{\\text{full}}$. The oracle, which selects the higher-scoring strategy per episode, improves only modestly to $-6.58$, with 96.2\\% of its routing decisions matching always-deterministic. This \\emph{oracle degeneracy} indicates that the optimal episode-level routing policy closely resembles unconditional deterministic computation---the routing signal is insufficient to improve upon simply always choosing the deterministic strategy. Random routing ($-22.38$) falls between the two pure strategies, with a death rate (27.8\\%) proportional to its 50/50 allocation.\n\nKeyword-based routing (\\S\\ref{sec:rule}) structurally fails to provide meaningful discrimination. ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms, causing keyword match rates to cluster at extremes: near-total (v1: 85.8\\%, degenerating to always-deterministic) or negligible (v2: 4.9\\%, v3: 2.8\\%, both degenerating to always-internal). No keyword granularity bridges this gap.\n\n\\subsection{Router Training as Diagnostic}\n\\label{sec:router-diagnostic}\n\nA natural question is whether the episode-level counterfactual labels can train a step-level router. We investigate this as a diagnostic probe of label informativeness rather than a routing system proposal, testing two architectures.\n\n\\paragraph{Classification head.} We append a linear classification head to the LLM's hidden representations, trained on episode-level routing labels. Across all configurations tested---class weighting, focal loss, minority undersampling, and temperature scaling---the classifier degenerates to predicting always-deterministic (0\\% internal recall in all cases). The episode-level labeling granularity does not transfer to step-level classification through this architecture.\n\n\\paragraph{Implicit router.} We fine-tune a smaller model (Qwen3-1.7B) to internalize routing decisions within its generation process. At the logit level, routing patterns emerge: accuracy reaches 74.5\\% with balanced accuracy of 79\\%, demonstrating that the counterfactual labels encode learnable routing structure beyond what a degenerate always-deterministic predictor captures. At the generation level, however, accuracy drops to 65.36\\% with internal recall of 51.5\\%, revealing a gap between logit-level pattern recognition and generation-level expression. [PLACEHOLDER: ablation-b end-to-end evaluation results for Table~\\ref{tab:baselines}.]\n\nThese results yield two observations. First, the counterfactual labels encode genuine routing patterns at the representation level---the logit-level success rules out uninformative labels as the cause of classification head failure, pointing instead to the episode-to-step granularity mismatch as the bottleneck. Second, while the labels reveal learnable routing patterns at the logit level, generation-level expression of these patterns remains an open challenge. Whether this gap stems from the labeling granularity, the generation decoding process, or model capacity is under investigation; step-level counterfactual labeling may be a productive direction for bridging it.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\nOur analysis is conducted on a single benchmark (ScienceWorld) with a single LLM backbone (Qwen2.5-7B-Instruct), and generalization to other interactive environments and model scales remains to be established. ScienceWorld's severe $-100$ death penalty may amplify the death avoidance signal; environments with less catastrophic failure penalties could exhibit a lower DAF, though the qualitative finding---death avoidance as a major component of routing signal---may still hold. Our counterfactual labels operate at episode granularity; step-level labeling with denser reward signals is a natural extension that could improve both decomposition resolution and router training. The gap between logit-level and generation-level routing accuracy in the implicit router warrants further investigation.\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_0152paG6KMJ1rzV5oieUpTvN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "283908ef-22ed-4644-a6e6-6be640518f59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2wwsWGV5Cm9ugfxtuaqVm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 30297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 550
      },
      "output_tokens": 67,
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

_source line 20 · 2026-05-14T09:25:51.556Z_

<details><summary>↩ Tool result · `toolu_0152paG6KMJ1rzV5oieUpTvN`</summary>

```text
1	# EMNLP 2026 Short Paper Outline
2	
3	## Title Candidates
4	
5	1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**
6	2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**
7	3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**
8	
9	Recommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)
10	
11	---
12	
13	## Abstract Skeleton (~150 words)
14	
15	Key points to cover:
16	
17	- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?
18	- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.
19	- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.
20	- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).
21	- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.
22	
23	---
24	
25	## Section Structure
26	
27	### 1. Introduction (0.8 pages)
28	
29	**Key points:**
30	- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question
31	- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone
32	- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis
33	- **Contributions** (bulleted):
34	  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy
35	  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]
36	  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router
37	
38	### 2. Method (1.0 pages)
39	
40	**Key points:**
41	- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision
42	- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]
43	- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full
44	
45	### 3. Experiments (1.5 pages)
46	
47	**Key points:**
48	- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router
49	- **3.2 Death Decomposition Results** (core result):
50	  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]
51	  - 10/11 death-prone tasks: death-dominated gaps
52	  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]
53	  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]
54	- **3.3 Baseline Comparison**:
55	  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]
56	  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)
57	  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate
58	- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities [A: plan-012-full, 245eps/11tasks]
59	
60	### 4. Related Work (0.5 pages, integrated or separate)
61	
62	**Key points:**
63	- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router
64	- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture
65	- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)
66	- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop
67	
68	### 5. Conclusion (0.3 pages)
69	
70	**Key points:**
71	- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology
72	- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)
73	- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling
74	
75	---
76	
77	## Figure/Table Plan
78	
79	### Table 1: Baseline Comparison
80	| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |
81	|--------|-------|--------|-------------|------------|-----------|
82	| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |
83	| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |
84	| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |
85	| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |
86	| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |
87	| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |
88	| Learned Router (implicit) | TBD | — | — | — | TBD |
89	
90	*Source: plan-003-baseline-245eps, plan-011-rule-based*
91	
92	### Figure 1: Death Decomposition (core figure)
93	- **Type**: Grouped bar chart or stacked bar
94	- **X-axis**: 11 task types (sorted by death fraction)
95	- **Y-axis**: Score delta (deterministic − internal)
96	- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)
97	- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)
98	- **Annotation**: Overall death fraction = 90.41%
99	
100	*Source: plan-012-full*
101	
102	### Figure 2: Cross-task Correlation (if space permits)
103	- **Type**: Scatter plot with regression line
104	- **X-axis**: Per-task death rate difference (internal − deterministic)
105	- **Y-axis**: Δ_full per task
106	- **Regression line**: r=0.9698, p=8.12e-07
107	- **11 points**, labeled by task type
108	- **Purpose**: Visually demonstrates near-perfect linear relationship
109	
110	*Source: plan-012-full, plan-012-decomposition*
111	
112	**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.
113	
114	---
115	
116	## Key References
117	
118	### Tool-Use Learning
119	- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*
120	- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*
121	- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*
122	- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*
123	
124	### Agent Routing / Adaptive Computation
125	- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)
126	- ITP-R — imagination-based routing to LLM world model
127	- ARES — adaptive routing for efficient serving
128	- Raposo et al. (2024). Mixture-of-Depths. *ICML*
129	
130	### Agent Frameworks
131	- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*
132	- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*
133	
134	### Methodology
135	- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)
136	
137	### Environment
138	- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*
139	
140	### Code Execution Routing
141	- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math
142	- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning
143	
144	---
145	
146	## Provenance: Claims → Experiments
147	
148	| Claim | Source Experiment | Key Metric |
149	|-------|------------------|------------|
150	| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |
151	| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |
152	| Baseline scores (Table 1) | plan-003-baseline-245eps | metrics per condition |
153	| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |
154	| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |
155	| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |
156	| Episode label distribution 86/9/150 | plan-012-full | label_dist |
157	| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |
158	| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |
159	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "fd069e7e-d82a-456e-8b56-1c4ca40eb689",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/paper_outline.md",
      "content": "# EMNLP 2026 Short Paper Outline\n\n## Title Candidates\n\n1. **Death Avoidance Dominates Routing Signal: A Counterfactual Analysis of LLM Agent Tool Use in Interactive Environments**\n2. **When Does Deterministic Computation Help LLM Agents? Episode-Level Counterfactual Analysis Reveals Death Avoidance Dominance**\n3. **90% Death Avoidance: Decomposing the Routing Signal Between LLM Reasoning and Deterministic Simulation**\n\nRecommended: **Title 1** (clear claim + methodology in title; fits short paper convention of stating the finding)\n\n---\n\n## Abstract Skeleton (~150 words)\n\nKey points to cover:\n\n- **Problem**: LLM agents hallucinate state transitions in rule-governed environments, causing catastrophic failures (deaths). Routing between internal LLM reasoning and deterministic computation (simulators) can mitigate this, but what exactly does routing learn?\n- **Methodological gap**: Per-step oracle labeling degenerates in sparse-reward settings (98% tie rate on ScienceWorld). We propose episode-level counterfactual analysis.\n- **Core finding**: Death avoidance accounts for ~90% of routing signal (Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%; Pearson r=0.97, p<1e-6 across 11 task types / 245 episodes) [A: plan-012-full, 245eps/11tasks]. Non-death performance is approximately equal between modalities.\n- **Supporting finding**: Keyword heuristics structurally fail (match rates degenerate to ≈always-det or ≈always-internal); episode-level counterfactual labels can train a lightweight router (internal_recall=51.5%).\n- **Implication**: The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n---\n\n## Section Structure\n\n### 1. Introduction (0.8 pages)\n\n**Key points:**\n- LLM agents on rule-governed environments (physics, chemistry) suffer catastrophic failures from hallucinated state transitions → motivate the routing question\n- Existing work: tool-use learning (Toolformer, ART, Chameleon) learns *when* to invoke tools but doesn't analyze *what* routing learns; ITP-R routes to approximate world models but underperforms pure internal reasoning; ReTool/AgentMath use implicit routing entangled with backbone\n- Per-step oracle labeling degenerates in sparse-reward environments (98% tie rate) → need episode-level analysis\n- **Contributions** (bulleted):\n  1. Episode-level counterfactual methodology that overcomes per-step oracle degeneracy\n  2. Empirical finding: death avoidance accounts for ≥90% of routing signal on ScienceWorld (11 tasks, 245 episodes) [A: plan-012-full, 245eps/11tasks]\n  3. Structural failure analysis of keyword heuristics; demonstration that counterfactual labels can train a lightweight diagnostic router\n\n### 2. Method (1.0 pages)\n\n**Key points:**\n- **2.1 Problem Setup**: ScienceWorld environment; two computation modalities (internal LLM reasoning vs. deterministic simulation via environment forking); per-step routing decision\n- **2.2 Episode-Level Counterfactual Labeling**: Why per-step oracle fails (98% tie rate in sparse rewards) → run complete episodes under pure-internal and pure-deterministic strategies → compare episode-level scores → label: det-preferred / internal-preferred / no-preference. Distribution: 86 det-pref / 9 int-pref / 150 no-pref (245 episodes) [A: plan-012-full, 245eps/11tasks]\n- **2.3 Death Decomposition Framework**: Decompose Δ_full into death-avoidance component (Δ_death) and non-death component (Δ_nd). Death avoidance fraction = (Δ_full - Δ_nd) / Δ_full. Cross-task correlation: Pearson r between per-task death rate difference and Δ_full\n\n### 3. Experiments (1.5 pages)\n\n**Key points:**\n- **3.1 Setup**: Qwen3-1.7B backbone; ScienceWorld 11 task types × 20-40 episodes; evaluation: always-internal, always-deterministic, oracle, random, keyword heuristic, learned router\n- **3.2 Death Decomposition Results** (core result):\n  - Δ_full=+29.60, Δ_nd=+2.84, death fraction=90.41% [A: plan-012-full, 245eps/11tasks]\n  - 10/11 death-prone tasks: death-dominated gaps\n  - 1 exception: find-non-living-thing (n=40, 0 deaths, Δ=+9.58 from non-death mechanisms) [A: plan-012-full, 245eps/11tasks]\n  - Pearson r=0.9698 (p=8.12e-07) [A: plan-012-full, 245eps/11tasks]\n- **3.3 Baseline Comparison**:\n  - always-internal: -39.07, always-det: -9.47, oracle: -6.58, random: -22.38 [A: plan-003-baseline-245eps]\n  - Keyword heuristic: structural failure (v1 85.8% match → ≈always-det; v2 4.9% → ≈always-internal)\n  - Learned router (ablation-b): internal_recall=51.5%, first non-degenerate; classification head variants all degenerate\n- **3.4 Analysis**: Death rate: internal 42.9% vs. deterministic 16.3%; alive-episode scores nearly equal across modalities [A: plan-012-full, 245eps/11tasks]\n\n### 4. Related Work (0.5 pages, integrated or separate)\n\n**Key points:**\n- **Tool-use learning**: Toolformer (self-supervised API insertion), ART (LLM-as-router), Chameleon (LLM-as-planner), ToolkenGPT (token-level triggers). Differentiation: episode-level counterfactual labeling, safety-aware framing, explicit modular router\n- **Adaptive computation / routing**: CogRouter (RL-based), ARES, Mixture-of-Depths. Our focus: empirical analysis of *what* routing learns, not a new routing architecture\n- **World model routing**: ITP-R, Dyna-Think. Our deterministic computation is exact (simulator), not approximate (LLM world model)\n- **Agent frameworks**: ReAct, Reflexion. Orthogonal — we analyze the routing decision within an agent loop\n\n### 5. Conclusion (0.3 pages)\n\n**Key points:**\n- Summary: death avoidance ≥90% of routing signal; episode-level counterfactual analysis as diagnostic methodology\n- **Limitations**: single benchmark (ScienceWorld), episode-level granularity (not step-level), DAgger distribution shift (train on pure strategies, deploy on mixed)\n- **Future work**: step-level labeling with denser reward signals, extension to MATH/code interpretation domains, DAgger-style iterative relabeling\n\n---\n\n## Figure/Table Plan\n\n### Table 1: Baseline Comparison\n| Method | Score | 90% CI | Success Rate | Death Rate | Sim Ratio |\n|--------|-------|--------|-------------|------------|-----------|\n| Always-Internal | -39.07 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.00 |\n| Always-Deterministic | -9.47 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 1.00 |\n| Oracle | -6.58 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.96 |\n| Random | -22.38 [A: plan-003-baseline-245eps] | TBD | TBD | TBD | 0.50 |\n| Keyword Heuristic (v1) | ≈ Always-Det | — | — | — | 0.86 |\n| Keyword Heuristic (v2) | ≈ Always-Int | — | — | — | 0.05 |\n| Learned Router (implicit) | TBD | — | — | — | TBD |\n\n*Source: plan-003-baseline-245eps, plan-011-rule-based*\n\n### Figure 1: Death Decomposition (core figure)\n- **Type**: Grouped bar chart or stacked bar\n- **X-axis**: 11 task types (sorted by death fraction)\n- **Y-axis**: Score delta (deterministic − internal)\n- **Bars**: Δ_full decomposed into Δ_death (death-avoidance component, dark) and Δ_nd (non-death component, light)\n- **Highlight**: find-non-living-thing as sole exception (Δ_nd = Δ_full = 9.58, zero deaths)\n- **Annotation**: Overall death fraction = 90.41%\n\n*Source: plan-012-full*\n\n### Figure 2: Cross-task Correlation (if space permits)\n- **Type**: Scatter plot with regression line\n- **X-axis**: Per-task death rate difference (internal − deterministic)\n- **Y-axis**: Δ_full per task\n- **Regression line**: r=0.9698, p=8.12e-07\n- **11 points**, labeled by task type\n- **Purpose**: Visually demonstrates near-perfect linear relationship\n\n*Source: plan-012-full, plan-012-decomposition*\n\n**Space strategy**: Figure 1 is mandatory. Figure 2 can be merged as an inset in Figure 1, or moved to appendix if space is tight. Table 1 is mandatory. Per-task breakdown table → appendix.\n\n---\n\n## Key References\n\n### Tool-Use Learning\n- Schick et al. (2024). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS*\n- Paranjape et al. (2023). ART: Automatic Multi-step Reasoning and Tool-Use. *arXiv*\n- Lu et al. (2024). Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models. *NeurIPS*\n- Hao et al. (2024). ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings. *NeurIPS*\n\n### Agent Routing / Adaptive Computation\n- CogRouter — RL-based cognitive routing (ScienceWorld SOTA)\n- ITP-R — imagination-based routing to LLM world model\n- ARES — adaptive routing for efficient serving\n- Raposo et al. (2024). Mixture-of-Depths. *ICML*\n\n### Agent Frameworks\n- Yao et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR*\n- Shinn et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. *NeurIPS*\n\n### Methodology\n- Ross et al. (2011). A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning. *AISTATS* (DAgger)\n\n### Environment\n- Wang et al. (2022). ScienceWorld: Is your Agent Smarter than a 5th Grader? *EMNLP*\n\n### Code Execution Routing\n- Gou et al. (2024). ReTool / ToRA — tool-integrated reasoning for math\n- Chen et al. (2023). AgentMath — code-augmented mathematical reasoning\n\n---\n\n## Provenance: Claims → Experiments\n\n| Claim | Source Experiment | Key Metric |\n|-------|------------------|------------|\n| Δ_full=+29.60, death fraction=90.41% | plan-012-full | delta_full, death_avoidance_fraction |\n| r=0.9698, p=8.12e-07 | plan-012-full | pearson_r, pearson_p |\n| Baseline scores (Table 1) | plan-003-baseline-245eps | metrics per condition |\n| Keyword heuristic failure | plan-011-rule-based | v1_match_rate, v2_match_rate |\n| Learned router internal_recall=51.5% | plan-004-ablation-b | per_class.internal.recall |\n| find-non-living-thing Δ=9.58 | plan-012-decomposition | key_tasks.find_non_living_thing |\n| Episode label distribution 86/9/150 | plan-012-full | label_dist |\n| Death rates: int 42.9%, det 16.3% | plan-012-full | death_rate_int, death_rate_det |\n| Per-step oracle 98% tie rate | plan-012-decomposition | (derived from label_dist) |\n",
      "numLines": 159,
      "startLine": 1,
      "totalLines": 159
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
Now I have good context. Let me also check the experiment_tables.md for exact numbers to ensure I use A-source data correctly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "88da1c5b-9bc4-41c2-b5b7-97e69a7da39b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jokkihU7JhnhizSsbfow7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6156,
      "cache_read_input_tokens": 30847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6156
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

Let me check the experiment tables for exact A-source numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "51de083f-7002-438e-b6f7-5a0384076044",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jokkihU7JhnhizSsbfow7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6156,
      "cache_read_input_tokens": 30847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6156
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

<details open><summary>🔧 Tool call — Read · `toolu_01Ndkscvifckvpx1y8UtoiG2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiment_tables.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "889fb8e8-1fc0-45f7-98fc-7abd3fc691e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jokkihU7JhnhizSsbfow7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6156,
      "cache_read_input_tokens": 30847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6156
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

_source line 24 · 2026-05-14T09:25:56.699Z_

<details><summary>↩ Tool result · `toolu_01Ndkscvifckvpx1y8UtoiG2`</summary>

```text
1	# Experiment Tables for EMNLP 2026 Short Paper
2	
3	> **Status**: Preliminary (pre-analysis: prescreening 5 ep/task + MVP 20 ep/task, N=249 episodes).
4	> Plan-001b full data collection in progress; numbers will be updated upon completion.
5	
6	---
7	
8	## Table 1: Death Decomposition Analysis (plan-012)
9	
10	Core result: deterministic simulation advantage is almost entirely explained by death avoidance.
11	
12	| Metric | Episode-weighted | Task-weighted† |
13	|--------|:---------------:|:-------------:|
14	| Δ_full (det − internal) | **+38.33** | **+41.48** |
15	| Δ_nd (non-death episodes only) | +0.48 | +0.91 |
16	| DAF (death avoidance fraction) | 98.8% | 93.9% |
17	| DAF 95% CI (bootstrap) | [93.9%, 104.5%] | [84.6%, 99.8%] |
18	| Pearson *r* (Δ_death_rate vs Δ_full) | 0.986 | — |
19	| *p*-value | <0.0001 | — |
20	| Δ_penalty_removed | +0.98 | — |
21	| Internal death rate | 49.0% | — |
22	| Deterministic death rate | 11.7% | — |
23	| Tasks / Episodes | 30 / 249 | 30 / 249 |
24	
25	**Data source**: `results/death_decomposition_report.json` (plan-012, 2026-05-14).
26	Episode-weighted = aggregate means across all episodes; Task-weighted† = mean of per-task metrics (from registry, pending re-verification).
27	
28	### Signal Source Decomposition (episode-level)
29	
30	| Signal Source | Count | % of Episodes |
31	|--------------|:-----:|:------------:|
32	| death_asymmetry | 93 | 37.3% |
33	| tied_alive (no-preference) | 117 | 47.0% |
34	| both_dead (no-preference) | 29 | 11.6% |
35	| score_comparison | 10 | 4.0% |
36	
37	**Interpretation**: 93/102 det-preferred labels (91.2%) come from death asymmetry; only 9 (8.8%) from genuine score differences.
38	
39	---
40	
41	## Table 2: Keyword Routing Baseline (plan-011)
42	
43	All keyword heuristics degenerate — none provides meaningful routing signal.
44	
45	| Version | Keywords | N | Match Rate | Routing Acc.† | Effective Behavior |
46	|---------|:--------:|:---:|:----------:|:------------:|-------------------|
47	| v1 (generic) | 20 (incl. *connect*) | 204 | 86.1% | 97.6% | ≈ always-det |
48	| v2 (science) | 17 | 203 | 4.9% | 1.2% | ≈ always-internal |
49	| v3 (state-change) | 12 | ~233 | 2.8% | 1.5% | ≈ always-internal |
50	
51	**v1 keywords**: heat, cool, boil, melt, freeze, burn, mix, pour, react, dissolve, combine, activate, deactivate, turn on, turn off, **connect**, disconnect, change state, phase change, temperature
52	**v2 keywords**: heat, cool, boil, melt, freeze, burn, mix, pour, react, dissolve, activate, change state, ignite, combust, evaporate, condense, oxidize
53	**v3 keywords**: heat, cool, boil, melt, freeze, burn, mix, pour, react, dissolve, activate, change-state
54	
55	†Routing accuracy = fraction of scorable episodes where keyword routing matches oracle label. v1 gets high accuracy only because match_rate≈86% routes everything to det, which happens to match the dominant label.
56	
57	**Structural failure**: ScienceWorld actions use generic interaction verbs (*connect*, *move*, *pick up*), not science-specific keywords. Removing *connect* alone drops match rate from 86% to 5%. No static keyword set captures the task-relevant routing signal.
58	
59	**Data source**: `results/rule_based_accuracy_v1_rerun.json`, `rule_based_accuracy_v2_test.json`, registry plan-011 (v3). Episodes vary slightly due to race condition in concurrent evaluation (see registry notes).
60	
61	---
62	
63	## Table 3: Label Distribution (episode-level, N=249)
64	
65	| Label | Count | Percentage |
66	|-------|:-----:|:----------:|
67	| det-preferred | 102 | 41.0% |
68	| internal-preferred | 1 | 0.4% |
69	| no-preference | 146 | 58.6% |
70	
71	**Data source**: `results/death_decomposition_report.json` aggregate.label_distribution.
72	
73	### Task-level Signal Category (plan-005, N=314 episodes, 30 tasks)
74	
75	| Category | Tasks | % Tasks | Episodes | % Episodes |
76	|----------|:-----:|:-------:|:--------:|:----------:|
77	| Death-dominated (DAF ≥ 95%) | 25 | 83.3% | 250 | 79.6% |
78	| Genuine-det (DAF < 95%, Δ > 0) | 3 | 10.0% | 19 | 6.1% |
79	| Internal-preferred (Δ ≤ 0) | 2 | 6.7% | 45 | 14.3% |
80	
81	**Data source**: `results/plan005/analysis/taxonomy_summary.json` (includes partial plan-001b data).
82	
83	---
84	
85	## Table 4: Baseline Comparison (episode-weighted mean scores)
86	
87	| Method | Mean Score | Notes |
88	|--------|:---------:|-------|
89	| always-internal | −47.5 | LLM internal reasoning only; 49% death rate |
90	| always-deterministic | −9.2 | Deterministic simulation only; 11.7% death rate |
91	| keyword-v1 (generic) | ≈ always-det | Degenerates: 86% match rate → routes everything to det |
92	| keyword-v2 (science) | ≈ always-internal | Degenerates: 5% match rate → routes everything to internal |
93	| keyword-v3 (state-change) | ≈ always-internal | Degenerates: 3% match rate → routes everything to internal |
94	| oracle (episode-level) | *pending* | Upper bound; requires plan-001b full data |
95	
96	**Data source**: Episode-weighted means from `results/death_decomposition_report.json`.
97	
98	---
99	
100	## Data Provenance Summary
101	
102	| Source | File / Key | Episodes | Status |
103	|--------|-----------|:--------:|--------|
104	| plan-012 decomposition | `death_decomposition_report.json` | 249 | **DONE** (preliminary) |
105	| plan-011 keyword baseline | `rule_based_accuracy_*.json` | 204 | **DONE** |
106	| plan-005 taxonomy | `plan005/analysis/taxonomy_summary.json` | 314 | **DONE** (includes partial plan-001b) |
107	| plan-001b full collection | `plan_c/` (in progress) | — | **RUNNING** |
108	
109	### Update plan
110	When plan-001b completes (~40 tasks × 20 ep/task = 800+ episodes):
111	1. Re-run decomposition analysis → update Table 1
112	2. Re-compute label distribution → update Table 3
113	3. Compute oracle baseline score → fill Table 4 oracle row
114	4. Remove "preliminary" status
115	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "55b6df7f-1eea-4aa2-a0af-5dcbc7e67098",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/experiment_tables.md",
      "content": "# Experiment Tables for EMNLP 2026 Short Paper\n\n> **Status**: Preliminary (pre-analysis: prescreening 5 ep/task + MVP 20 ep/task, N=249 episodes).\n> Plan-001b full data collection in progress; numbers will be updated upon completion.\n\n---\n\n## Table 1: Death Decomposition Analysis (plan-012)\n\nCore result: deterministic simulation advantage is almost entirely explained by death avoidance.\n\n| Metric | Episode-weighted | Task-weighted† |\n|--------|:---------------:|:-------------:|\n| Δ_full (det − internal) | **+38.33** | **+41.48** |\n| Δ_nd (non-death episodes only) | +0.48 | +0.91 |\n| DAF (death avoidance fraction) | 98.8% | 93.9% |\n| DAF 95% CI (bootstrap) | [93.9%, 104.5%] | [84.6%, 99.8%] |\n| Pearson *r* (Δ_death_rate vs Δ_full) | 0.986 | — |\n| *p*-value | <0.0001 | — |\n| Δ_penalty_removed | +0.98 | — |\n| Internal death rate | 49.0% | — |\n| Deterministic death rate | 11.7% | — |\n| Tasks / Episodes | 30 / 249 | 30 / 249 |\n\n**Data source**: `results/death_decomposition_report.json` (plan-012, 2026-05-14).\nEpisode-weighted = aggregate means across all episodes; Task-weighted† = mean of per-task metrics (from registry, pending re-verification).\n\n### Signal Source Decomposition (episode-level)\n\n| Signal Source | Count | % of Episodes |\n|--------------|:-----:|:------------:|\n| death_asymmetry | 93 | 37.3% |\n| tied_alive (no-preference) | 117 | 47.0% |\n| both_dead (no-preference) | 29 | 11.6% |\n| score_comparison | 10 | 4.0% |\n\n**Interpretation**: 93/102 det-preferred labels (91.2%) come from death asymmetry; only 9 (8.8%) from genuine score differences.\n\n---\n\n## Table 2: Keyword Routing Baseline (plan-011)\n\nAll keyword heuristics degenerate — none provides meaningful routing signal.\n\n| Version | Keywords | N | Match Rate | Routing Acc.† | Effective Behavior |\n|---------|:--------:|:---:|:----------:|:------------:|-------------------|\n| v1 (generic) | 20 (incl. *connect*) | 204 | 86.1% | 97.6% | ≈ always-det |\n| v2 (science) | 17 | 203 | 4.9% | 1.2% | ≈ always-internal |\n| v3 (state-change) | 12 | ~233 | 2.8% | 1.5% | ≈ always-internal |\n\n**v1 keywords**: heat, cool, boil, melt, freeze, burn, mix, pour, react, dissolve, combine, activate, deactivate, turn on, turn off, **connect**, disconnect, change state, phase change, temperature\n**v2 keywords**: heat, cool, boil, melt, freeze, burn, mix, pour, react, dissolve, activate, change state, ignite, combust, evaporate, condense, oxidize\n**v3 keywords**: heat, cool, boil, melt, freeze, burn, mix, pour, react, dissolve, activate, change-state\n\n†Routing accuracy = fraction of scorable episodes where keyword routing matches oracle label. v1 gets high accuracy only because match_rate≈86% routes everything to det, which happens to match the dominant label.\n\n**Structural failure**: ScienceWorld actions use generic interaction verbs (*connect*, *move*, *pick up*), not science-specific keywords. Removing *connect* alone drops match rate from 86% to 5%. No static keyword set captures the task-relevant routing signal.\n\n**Data source**: `results/rule_based_accuracy_v1_rerun.json`, `rule_based_accuracy_v2_test.json`, registry plan-011 (v3). Episodes vary slightly due to race condition in concurrent evaluation (see registry notes).\n\n---\n\n## Table 3: Label Distribution (episode-level, N=249)\n\n| Label | Count | Percentage |\n|-------|:-----:|:----------:|\n| det-preferred | 102 | 41.0% |\n| internal-preferred | 1 | 0.4% |\n| no-preference | 146 | 58.6% |\n\n**Data source**: `results/death_decomposition_report.json` aggregate.label_distribution.\n\n### Task-level Signal Category (plan-005, N=314 episodes, 30 tasks)\n\n| Category | Tasks | % Tasks | Episodes | % Episodes |\n|----------|:-----:|:-------:|:--------:|:----------:|\n| Death-dominated (DAF ≥ 95%) | 25 | 83.3% | 250 | 79.6% |\n| Genuine-det (DAF < 95%, Δ > 0) | 3 | 10.0% | 19 | 6.1% |\n| Internal-preferred (Δ ≤ 0) | 2 | 6.7% | 45 | 14.3% |\n\n**Data source**: `results/plan005/analysis/taxonomy_summary.json` (includes partial plan-001b data).\n\n---\n\n## Table 4: Baseline Comparison (episode-weighted mean scores)\n\n| Method | Mean Score | Notes |\n|--------|:---------:|-------|\n| always-internal | −47.5 | LLM internal reasoning only; 49% death rate |\n| always-deterministic | −9.2 | Deterministic simulation only; 11.7% death rate |\n| keyword-v1 (generic) | ≈ always-det | Degenerates: 86% match rate → routes everything to det |\n| keyword-v2 (science) | ≈ always-internal | Degenerates: 5% match rate → routes everything to internal |\n| keyword-v3 (state-change) | ≈ always-internal | Degenerates: 3% match rate → routes everything to internal |\n| oracle (episode-level) | *pending* | Upper bound; requires plan-001b full data |\n\n**Data source**: Episode-weighted means from `results/death_decomposition_report.json`.\n\n---\n\n## Data Provenance Summary\n\n| Source | File / Key | Episodes | Status |\n|--------|-----------|:--------:|--------|\n| plan-012 decomposition | `death_decomposition_report.json` | 249 | **DONE** (preliminary) |\n| plan-011 keyword baseline | `rule_based_accuracy_*.json` | 204 | **DONE** |\n| plan-005 taxonomy | `plan005/analysis/taxonomy_summary.json` | 314 | **DONE** (includes partial plan-001b) |\n| plan-001b full collection | `plan_c/` (in progress) | — | **RUNNING** |\n\n### Update plan\nWhen plan-001b completes (~40 tasks × 20 ep/task = 800+ episodes):\n1. Re-run decomposition analysis → update Table 1\n2. Re-compute label distribution → update Table 3\n3. Compute oracle baseline score → fill Table 4 oracle row\n4. Remove \"preliminary\" status\n",
      "numLines": 115,
      "startLine": 1,
      "totalLines": 115
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Important: The experiment_tables.md contains B-source numbers (30 tasks / 249 episodes). The task specifies I must use A-source numbers (plan-012-full, 11 tasks / 245 episodes). Let me check the experiments_draft.md which already uses A-source numbers:
- 245 episodes, 11 task types
- Δ_full = +29.60
- Δ_no_death = +2.84
- DAF = 90.41%


- r = 0.9698, p = 8.12e-7

Now I'm looking at the label distribution and death rates across the different approaches, which confirm these are the right numbers. I should reference the dream paper.tex format as I structure the method section into its four main components: counterfactual episode collection, death-aware labeling, the death avoidance factor calculation, and the rule extraction process.

I need to be precise about the exact numbers from the source—245 episodes across 11 tasks—and make sure the labeling cases are presented as mutually exclusive rather than hierarchical. The death avoidance factor needs careful treatment around boundary conditions, and I should wrap up the rule extraction section with language about observation-based approaches. I'll draft the LaTeX carefully now, incorporating the proper citations and section labels.

Writing the method section...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "d58c1003-3275-421d-8c66-aae9282536c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxsG5uqTaDEXBxbSRCKAEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2392,
      "cache_read_input_tokens": 37003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2392
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

_source line 26_

Now I have all the context. Writing the method section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "ce57317b-9415-4102-aba3-bfbeb7d09787",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxsG5uqTaDEXBxbSRCKAEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2392,
      "cache_read_input_tokens": 37003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2392
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

_source line 27_

<details open><summary>🔧 Tool call — Write · `toolu_01BFs6c55XHswu6THWjRhkd8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md",
  "content": "# Method Section — Draft v2 (A-Source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Method}\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nPer-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \\cite{scienceworld-2022}, 98.2\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n\nFor each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.\n\nEach episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. We evaluate on ScienceWorld \\cite{scienceworld-2022}, which spans 30 task types covering physical and chemical reasoning with a $-100$ penalty upon agent death. After prescreening (5 episodes per type for signal estimation), we perform targeted full collection on 11 task types, yielding 245 episode pairs (20--40 per type).\n\n\\subsection{Death-Aware Labeling}\n\\label{sec:labeling}\n\nEach counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:\n\n\\begin{enumerate}\n    \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ the surviving strategy is preferred.\n    \\item \\textbf{Both dead}: $d^{\\text{int}} = d^{\\text{det}} = 1$ $\\rightarrow$ \\texttt{no\\_preference}.\n    \\item \\textbf{Score comparison}: both survive and $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ the higher-scoring strategy is preferred.\n    \\item \\textbf{Tied alive}: both survive and $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n\\end{enumerate}\n\nAcross 245 episodes, this yields 86 (35.1\\%) \\texttt{det\\_preferred}, 9 (3.7\\%) \\texttt{internal\\_preferred}, and 150 (61.2\\%) \\texttt{no\\_preference}. The near-absence of \\texttt{internal\\_preferred} labels combined with the dominance of \\texttt{no\\_preference} indicates that the deterministic strategy's advantage is concentrated in death avoidance rather than superior task performance when both agents survive.\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we define the Death Avoidance Factor (DAF):\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{no\\_death}}}{\\Delta_{\\text{full}}}\n\\end{equation}\nwhere $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{no\\_death}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\\Delta_{\\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\\Delta_{\\text{full}}| > 0$.\n\nOn 245 episodes across 11 task types: $\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{no\\_death}} = +2.84$, yielding DAF $= 90.41\\%$. The cross-task consistency is strong: the Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$) across 11 task types, indicating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.\n\n\\subsection{Rule-Based Baseline}\n\\label{sec:rule}\n\nAs a simple routing heuristic, we test keyword-based rules that route to deterministic computation when the action contains science-related verbs. We evaluate three keyword lists of decreasing breadth:\n\n\\begin{itemize}\n    \\item \\textbf{v1} (20 generic verbs including \\emph{connect}, \\emph{move}): matches 85.8\\% of actions, degenerating to always-deterministic.\n    \\item \\textbf{v2} (17 science-specific verbs: \\emph{heat}, \\emph{boil}, \\emph{melt}, \\emph{freeze}, \\ldots): matches 4.9\\%, degenerating to always-internal.\n    \\item \\textbf{v3} (12 state-change verbs): matches 2.8\\%, degenerating to always-internal.\n\\end{itemize}\n\nThe structural cause is that ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms. No keyword granularity bridges the gap between near-total and negligible match rates, precluding meaningful routing discrimination. This structural failure motivates observation-based approaches that use environment observations and agent state as routing features rather than action keywords.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "8470588d-ceef-4679-b41b-cfac8c03de57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxsG5uqTaDEXBxbSRCKAEY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2392,
      "cache_read_input_tokens": 37003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2392
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

_source line 28 · 2026-05-14T09:26:42.371Z_

<details><summary>↩ Tool result · `toolu_01BFs6c55XHswu6THWjRhkd8`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "d4aa53b6-ed3a-4458-b2da-34adab0016db",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md",
    "content": "# Method Section — Draft v2 (A-Source: plan-012-full, 11 tasks / 245 episodes)\n\n\\section{Method}\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nPer-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \\cite{scienceworld-2022}, 98.2\\% of steps produce identical intermediate scores regardless of modality, yielding no routing signal. We instead perform episode-level counterfactual analysis.\n\nFor each task instance, we execute two complete episodes under identical initial conditions (same random seed, same task variation). The \\emph{pure-internal} episode follows the ReAct paradigm \\cite{react-2023}, where the LLM interleaves chain-of-thought reasoning with environment actions. The \\emph{pure-deterministic} episode uses the environment simulator to compute exact state transitions for each action. In both cases the LLM selects which action to take; deterministic computation replaces only the state-transition prediction, not action selection---equivalent to giving the agent access to a perfect world model.\n\nEach episode pair produces a tuple $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$, where $s$ denotes the terminal score and $d \\in \\{0,1\\}$ indicates agent death. Episodes are capped at 30 steps. The LLM backbone is Qwen2.5-7B-Instruct served via vLLM. We evaluate on ScienceWorld \\cite{scienceworld-2022}, which spans 30 task types covering physical and chemical reasoning with a $-100$ penalty upon agent death. After prescreening (5 episodes per type for signal estimation), we perform targeted full collection on 11 task types, yielding 245 episode pairs (20--40 per type).\n\n\\subsection{Death-Aware Labeling}\n\\label{sec:labeling}\n\nEach counterfactual pair receives an episode-level routing label based on $(s^{\\text{int}}, s^{\\text{det}}, d^{\\text{int}}, d^{\\text{det}})$. ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. The label is assigned by one of four mutually exclusive cases:\n\n\\begin{enumerate}\n    \\item \\textbf{Death asymmetry}: $d^{\\text{int}} \\neq d^{\\text{det}}$ $\\rightarrow$ the surviving strategy is preferred.\n    \\item \\textbf{Both dead}: $d^{\\text{int}} = d^{\\text{det}} = 1$ $\\rightarrow$ \\texttt{no\\_preference}.\n    \\item \\textbf{Score comparison}: both survive and $s^{\\text{det}} \\neq s^{\\text{int}}$ $\\rightarrow$ the higher-scoring strategy is preferred.\n    \\item \\textbf{Tied alive}: both survive and $s^{\\text{det}} = s^{\\text{int}}$ $\\rightarrow$ \\texttt{no\\_preference}.\n\\end{enumerate}\n\nAcross 245 episodes, this yields 86 (35.1\\%) \\texttt{det\\_preferred}, 9 (3.7\\%) \\texttt{internal\\_preferred}, and 150 (61.2\\%) \\texttt{no\\_preference}. The near-absence of \\texttt{internal\\_preferred} labels combined with the dominance of \\texttt{no\\_preference} indicates that the deterministic strategy's advantage is concentrated in death avoidance rather than superior task performance when both agents survive.\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we define the Death Avoidance Factor (DAF):\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{no\\_death}}}{\\Delta_{\\text{full}}}\n\\end{equation}\nwhere $\\Delta_{\\text{full}}$ is the mean score gap ($s^{\\text{det}} - s^{\\text{int}}$) across all episodes and $\\Delta_{\\text{no\\_death}}$ is the same gap restricted to episodes where neither strategy results in death. DAF $= 1$ indicates all routing signal stems from death avoidance; DAF $= 0$ indicates all signal stems from non-death performance differences. When $\\Delta_{\\text{full}} = 0$, DAF is undefined, as no routing signal exists to decompose; we report DAF only for task types where $|\\Delta_{\\text{full}}| > 0$.\n\nOn 245 episodes across 11 task types: $\\Delta_{\\text{full}} = +29.60$, $\\Delta_{\\text{no\\_death}} = +2.84$, yielding DAF $= 90.41\\%$. The cross-task consistency is strong: the Pearson correlation between per-task death rate differential (internal minus deterministic) and $\\Delta_{\\text{full}}$ is $r = 0.9698$ ($p = 8.12 \\times 10^{-7}$) across 11 task types, indicating that knowing how much more frequently the internal strategy dies is nearly sufficient to predict the full performance gap.\n\n\\subsection{Rule-Based Baseline}\n\\label{sec:rule}\n\nAs a simple routing heuristic, we test keyword-based rules that route to deterministic computation when the action contains science-related verbs. We evaluate three keyword lists of decreasing breadth:\n\n\\begin{itemize}\n    \\item \\textbf{v1} (20 generic verbs including \\emph{connect}, \\emph{move}): matches 85.8\\% of actions, degenerating to always-deterministic.\n    \\item \\textbf{v2} (17 science-specific verbs: \\emph{heat}, \\emph{boil}, \\emph{melt}, \\emph{freeze}, \\ldots): matches 4.9\\%, degenerating to always-internal.\n    \\item \\textbf{v3} (12 state-change verbs): matches 2.8\\%, degenerating to always-internal.\n\\end{itemize}\n\nThe structural cause is that ScienceWorld actions use generic interaction verbs (\\texttt{pick up}, \\texttt{move}, \\texttt{connect}) rather than science-specific terms. No keyword granularity bridges the gap between near-total and negligible match rates, precluding meaningful routing discrimination. This structural failure motivates observation-based approaches that use environment observations and agent state as routing features rather than action keywords.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 29_

Now let me register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "1241a22d-a025-42d7-94c1-a6b32eeeeef9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FV4KbwpToa2AbjvqfVjEy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2265,
      "cache_read_input_tokens": 39395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2265
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

_source line 30_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RMJQhAJsXfYJ8EKVo3wyCk`</summary>

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
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "520f12af-a1e4-4eb3-a98c-819ac412f78c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FV4KbwpToa2AbjvqfVjEy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2265,
      "cache_read_input_tokens": 39395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2265
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

_source line 31 · 2026-05-14T09:26:45.394Z_

<details><summary>↩ Tool result · `toolu_01RMJQhAJsXfYJ8EKVo3wyCk`</summary>

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
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "cd8f9cb1-dc18-4434-8049-0c5de29a06d4",
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

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_013AiMnaDw283WRHxuJ2NhuF`</summary>

```json
{
  "name": "method_v2_draft",
  "type": "paper",
  "description": "Method section v2 draft (LaTeX) for EMNLP 2026 short paper. 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor, Rule-Based Baseline. ~700 words, A-source data (plan-012-full, 11 tasks / 245 episodes).",
  "project": "simgate-modular-routing",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft.md",
  "tags": [
    "paper",
    "method",
    "latex",
    "v2",
    "a-source"
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
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "7dff4230-0a32-4857-aaaa-0958b3cac965",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Jed1XFA72b9ySKD2RUjJu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 41660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
      },
      "output_tokens": 69,
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

_source line 33 · 2026-05-14T09:26:50.847Z_

<details><summary>↩ Tool result · `toolu_013AiMnaDw283WRHxuJ2NhuF`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_875550\", \"name\": \"method_v2_draft\", \"type\": \"paper\", \"description\": \"Method section v2 draft (LaTeX) for EMNLP 2026 short paper. 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor, Rule-Based Baseline. ~700 words, A-source data (plan-012-full, 11 tasks / 245 episodes).\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft_875550.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T09:26:50.786906+00:00\", \"tags\": [\"paper\", \"method\", \"latex\", \"v2\", \"a-source\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "03f49e76-2b91-46bf-ae56-18637f25f5ac",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_875550\\\", \\\"name\\\": \\\"method_v2_draft\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Method section v2 draft (LaTeX) for EMNLP 2026 short paper. 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor, Rule-Based Baseline. ~700 words, A-source data (plan-012-full, 11 tasks / 245 episodes).\\\", \\\"path\\\": \\\"projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft_875550.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"simgate-modular-routing\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T09:26:50.786906+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"method\\\", \\\"latex\\\", \\\"v2\\\", \\\"a-source\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_875550\", \"name\": \"method_v2_draft\", \"type\": \"paper\", \"description\": \"Method section v2 draft (LaTeX) for EMNLP 2026 short paper. 4 subsections: Counterfactual Episode Collection, Death-Aware Labeling, Death Avoidance Factor, Rule-Based Baseline. ~700 words, A-source data (plan-012-full, 11 tasks / 245 episodes).\", \"path\": \"projects/simgate-modular-routing/artifacts/_project/paper/method_v2_draft_875550.md\", \"url\": null, \"project\": \"simgate-modular-routing\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T09:26:50.786906+00:00\", \"tags\": [\"paper\", \"method\", \"latex\", \"v2\", \"a-source\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

Method section v2 写入 `artifacts/_project/paper/method_v2_draft.md` 并已注册。

结构概要：
- **§3.1 Counterfactual Episode Collection** — 解释 per-step oracle 退化（98.2% tie rate）→ episode-level counterfactual 方案；pure-internal (ReAct) vs pure-deterministic；operational definition of deterministic computation；245 episodes / 11 task types
- **§3.2 Death-Aware Labeling** — 四个 mutually exclusive cases（death asymmetry / both dead / score comparison / tied alive）；label 分布 86/9/150
- **§3.3 Death Avoidance Factor** — DAF 公式、boundary case（Δ_full=0 → undefined）；Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%；Pearson r=0.9698
- **§3.4 Rule-Based Baseline** — 三个 keyword list (v1: 85.8%, v2: 4.9%, v3: 2.8%) 全部退化；以 observation-based approaches 收尾

所有数值均来自 A-source（plan-012-full, 11 tasks / 245 episodes）。Labels 与 experiments_draft.md 中的 `\ref{sec:collection}`, `\ref{sec:daf}`, `\ref{sec:rule}` 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "uuid": "c1648a06-cf9f-413a-b9bb-f6d6060e38fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Swpu8DLMokuaVkqWQ5Mpw5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 42380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 645
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

_source line 35_

Method section v2 写入 `artifacts/_project/paper/method_v2_draft.md` 并已注册。

结构概要：
- **§3.1 Counterfactual Episode Collection** — 解释 per-step oracle 退化（98.2% tie rate）→ episode-level counterfactual 方案；pure-internal (ReAct) vs pure-deterministic；operational definition of deterministic computation；245 episodes / 11 task types
- **§3.2 Death-Aware Labeling** — 四个 mutually exclusive cases（death asymmetry / both dead / score comparison / tied alive）；label 分布 86/9/150
- **§3.3 Death Avoidance Factor** — DAF 公式、boundary case（Δ_full=0 → undefined）；Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%；Pearson r=0.9698
- **§3.4 Rule-Based Baseline** — 三个 keyword list (v1: 85.8%, v2: 4.9%, v3: 2.8%) 全部退化；以 observation-based approaches 收尾

所有数值均来自 A-source（plan-012-full, 11 tasks / 245 episodes）。Labels 与 experiments_draft.md 中的 `\ref{sec:collection}`, `\ref{sec:daf}`, `\ref{sec:rule}` 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 83416,
  "duration_api_ms": 84454,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "88af4e73-ae5e-44da-8870-377ac0fe3e6f",
  "total_cost_usd": 0.4216655,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 31184,
    "cache_read_input_tokens": 258045,
    "output_tokens": 3815,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31184,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 384,
        "cache_read_input_tokens": 42380,
        "cache_creation_input_tokens": 645,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 645
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2218,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0023079999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 3815,
      "cacheReadInputTokens": 258045,
      "cacheCreationInputTokens": 31184,
      "webSearchRequests": 0,
      "costUSD": 0.41935750000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9b5f4a06-78ca-4810-8706-b7d3cb32ac11"
}
```

</details>

---
