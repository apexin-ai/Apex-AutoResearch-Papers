# paper writing

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_paper_writing_20260516T130650.log`
- **Structured JSON:** [`c71498695eb7c69d7f6e.json`](../../sessions/c7/c71498695eb7c69d7f6e.json)

## Before a recorded user message

22 recorded events

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
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
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
  "uuid": "385ad8fb-b53f-4864-b06e-f01fee8ae9dc",
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
  "uuid": "2c08bb56-bf10-4c38-99c9-d7214fc4b43c",
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to write a Related Work section for their EMNLP 2026 paper. Let me first read the latex-paper skill as instructed, then write the section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "786a2e4c-716c-446c-9df0-4281b799bec7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4MwgFiwHVspDDTCD5Mjyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12625,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12625
      },
      "output_tokens": 37,
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

<details open><summary>🔧 Tool call — Read · `toolu_01FxZLteoefwkH5xAUQSLSGL`</summary>

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
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "6725bdbe-0734-48d2-89bd-17185ccdc587",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4MwgFiwHVspDDTCD5Mjyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12625,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12625
      },
      "output_tokens": 37,
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

_source line 6 · 2026-05-16T13:07:01.128Z_

<details><summary>↩ Tool result · `toolu_01FxZLteoefwkH5xAUQSLSGL`</summary>

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
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "56c15cc6-774f-498f-ae96-19869e1c5da2",
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

<details open><summary>🔧 Tool call — Glob · `toolu_01HtNNTUAvsvSFx9kpoB5BTL`</summary>

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
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "3277104f-039d-48dc-bfdc-0d82605363d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D4MwgFiwHVspDDTCD5Mjyz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12625,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12625
      },
      "output_tokens": 37,
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

_source line 8 · 2026-05-16T13:07:01.877Z_

<details><summary>↩ Tool result · `toolu_01HtNNTUAvsvSFx9kpoB5BTL`</summary>

```text
paper/references.bib
paper/method.tex
paper/introduction.tex
paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "10aa9eab-ffbe-4f73-875a-b7cbae983475",
  "tool_use_result": {
    "filenames": [
      "paper/references.bib",
      "paper/method.tex",
      "paper/introduction.tex",
      "paper/experiments.tex"
    ],
    "durationMs": 13,
    "numFiles": 4,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 9_

Let me check the existing paper files for context on the writing style and the references.bib for available citation keys.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "da810952-83f7-46bf-ab66-cab175877200",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5Xk2iqvnHGSmEjdaRegur",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5729,
      "cache_read_input_tokens": 24466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5729
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

<details open><summary>🔧 Tool call — Read · `toolu_01WSjXiwhRw62wqXmSHUxyzn`</summary>

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
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "3b841a39-4151-4bf3-bd5b-95abe92c6335",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5Xk2iqvnHGSmEjdaRegur",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5729,
      "cache_read_input_tokens": 24466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5729
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

_source line 11 · 2026-05-16T13:07:07.384Z_

<details><summary>↩ Tool result · `toolu_01WSjXiwhRw62wqXmSHUxyzn`</summary>

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
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "26c97696-ee69-4574-b295-50f32f3caafa",
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

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01GcokKLYs1AWY2UAhM7Wnow`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "23e1d38a-1fa0-44b9-8bfe-ab73653087f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A5Xk2iqvnHGSmEjdaRegur",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5729,
      "cache_read_input_tokens": 24466,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5729
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

_source line 13 · 2026-05-16T13:07:08.053Z_

<details><summary>↩ Tool result · `toolu_01GcokKLYs1AWY2UAhM7Wnow`</summary>

```text
1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Exploiting this sparsity can yield up to 2$\times$ inference speedup by pruning 50\% of FFN neurons per token---without modifying the pretrained weights.
5	Yet the gap between potential and practice remains wide.
6	Training-free methods such as TEAL~\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\% sparsity on LLaMA-3.1-8B~\cite{grattafiori2024llama3}---a 281\% increase.
7	Learned predictors~\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add latency and memory overhead at inference.
8	The question is whether a predictor can be trained so that compensation becomes unnecessary.
9	
10	The answer depends on the training objective.
11	Current learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.
12	The gradient of BCE with respect to neuron $j$'s score is $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.
13	But at inference, no neuron is evaluated in isolation.
14	TEAL's global top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
15	Whether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \times d_{\text{ff}}$ neurons.
16	This creates a structural mismatch: the training objective decomposes per neuron, while the inference allocation is a global combinatorial decision.
17	BCE can achieve $>$90\% per-neuron classification accuracy against oracle masks yet still produce poor output quality under global allocation, because it optimizes a proxy misaligned with the true objective.
18	
19	KL divergence resolves this mismatch by coupling all neurons through the output distribution.
20	Instead of classifying individual neurons, we minimize $D_{\text{KL}}(p_{\text{dense}} \| p_{\text{sparse}})$ between the dense and sparse model outputs, training the predictor to preserve the full next-token distribution under pruning.
21	The gradient for neuron $j$ in layer $\ell$ factors as:
22	\begin{equation*}
23	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial \mathbf{h}^{(\ell)}} \cdot \frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}} \cdot \frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}},
24	\end{equation*}
25	where the Jacobian $\partial \mathbf{z} / \partial \mathbf{h}^{(\ell)}$ propagates through all downstream layers, making each neuron's gradient dependent on every other neuron's mask state.
26	Changing one neuron's mask affects all output logits; KL captures this because it measures distributional divergence over the entire vocabulary.
27	A Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} provides differentiable mask sampling during training, bridging the gap between soft training masks and hard inference decisions.
28	The predictor itself is a lightweight two-layer MLP (Linear $4096 \to 128$, GELU, Linear $128 \to 14336$) with 2.37M parameters per layer and 75.9M total---under 1\% of the base model---and requires no compensation network at inference.
29	
30	Empirically, the structural argument is borne out across sparsity levels, training budgets, and architectures.
31	At 50\% sparsity on LLaMA-3.1-8B, the KL-trained predictor achieves PPL 11.79 under TEAL's global allocation, compared to 23.31 for vanilla TEAL.
32	BCE trained for 2700 steps (2.71$\times$ our compute budget) reaches only 27.97, and its training loss saturates with $\Delta = -0.006$ over the final 2200 steps---confirming that the failure is structural, not computational.
33	The KL advantage scales super-linearly with sparsity: 18\% relative improvement at 30\%, 49\% at 50\%, and 82\% at 70\%.
34	Cross-architecture evaluation on Mistral-7B-v0.3~\cite{jiang2023mistral} yields +63\% relative degradation from dense, compared to +93\% on LLaMA, confirming generalization to SwiGLU models with different attention configurations.
35	We also analyze SPON's~\cite{xu2026spon} static bias correction and find it near-orthogonal to the predictor's effect (cosine similarity 0.196), recovering only 2.4\% of remaining error---the KL predictor already captures most of the recoverable signal.
36	
37	To situate these findings, we propose a two-dimensional taxonomy (Figure~\ref{fig:taxonomy}) that classifies sparsity prediction methods along \emph{correction granularity} (static, per-layer, per-token) and \emph{training signal coupling} (decomposed, intermediate, coupled).
38	Prior methods occupy distinct cells: SPON~\cite{xu2026spon} combines static correction with coupled KL training; ShadowLLM~\cite{akhauri2024shadowllm} uses per-layer prediction with intermediate MSE; FastForward~\cite{gautam2026fastforward} and DejaVu~\cite{liu2023dejavu} achieve per-token granularity but with decomposed BCE objectives.
39	No prior work has combined per-token contextual prediction with a coupled training signal.
40	Our method fills this cell, unifying input-dependent mask generation with an objective that reflects global neuron interactions through the output distribution.
41	
42	Our contributions are:
43	\begin{itemize}[nosep,leftmargin=*]
44	\item We show that a KL-trained contextual predictor eliminates the need for error compensation networks in activation sparsity, and provide a formal gradient analysis explaining the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation.
45	\item We propose a 2D taxonomy (correction granularity $\times$ training signal coupling) that unifies existing activation sparsity methods (Figure~\ref{fig:taxonomy}) and identifies the previously unexplored cell our method occupies.
46	\item We identify a phase transition in sparsity regimes---allocation-fixable ($\leq$30\%, where predictor and allocation choices recover downstream performance) vs.\ capacity-limited ($\geq$50\%, where no method recovers reasoning ability)---and confirm via SPON orthogonality analysis that static correction provides diminishing returns once a coupled predictor is present.
47	\end{itemize}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "5dbaf0d9-2ea3-40dc-8c3d-75865dc3591b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nSwiGLU feed-forward networks~\\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.\nExploiting this sparsity can yield up to 2$\\times$ inference speedup by pruning 50\\% of FFN neurons per token---without modifying the pretrained weights.\nYet the gap between potential and practice remains wide.\nTraining-free methods such as TEAL~\\cite{liu2025teal} select neurons by activation magnitude alone, degrading perplexity from 6.12 (dense) to 23.31 at 50\\% sparsity on LLaMA-3.1-8B~\\cite{grattafiori2024llama3}---a 281\\% increase.\nLearned predictors~\\cite{liu2023dejavu,gautam2026fastforward} close part of this gap by training small auxiliary networks to anticipate which neurons will be important, but they rely on error compensation modules (output rescaling networks or additive correction layers) that add latency and memory overhead at inference.\nThe question is whether a predictor can be trained so that compensation becomes unnecessary.\n\nThe answer depends on the training objective.\nCurrent learned predictors use binary cross-entropy (BCE) loss: each neuron is independently classified as ``keep'' or ``prune'' against an oracle mask derived from the dense model's activations.\nThe gradient of BCE with respect to neuron $j$'s score is $\\partial \\mathcal{L}_{\\text{BCE}} / \\partial s_j = \\sigma(s_j) - m_j^*$---a function of neuron $j$ alone, independent of every other neuron in the network.\nBut at inference, no neuron is evaluated in isolation.\nTEAL's global top-$k$ mechanism~\\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.\nWhether neuron $j$ survives depends not on its own score but on how that score compares to the scores of all $L \\times d_{\\text{ff}}$ neurons.\nThis creates a structural mismatch: the training objective decomposes per neuron, while the inference allocation is a global combinatorial decision.\nBCE can achieve $>$90\\% per-neuron classification accuracy against oracle masks yet still produce poor output quality under global allocation, because it optimizes a proxy misaligned with the true objective.\n\nKL divergence resolves this mismatch by coupling all neurons through the output distribution.\nInstead of classifying individual neurons, we minimize $D_{\\text{KL}}(p_{\\text{dense}} \\| p_{\\text{sparse}})$ between the dense and sparse model outputs, training the predictor to preserve the full next-token distribution under pruning.\nThe gradient for neuron $j$ in layer $\\ell$ factors as:\n\\begin{equation*}\n\\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial s_j^{(\\ell)}} = \\frac{\\partial \\mathcal{L}_{\\text{KL}}}{\\partial \\mathbf{z}} \\cdot \\frac{\\partial \\mathbf{z}}{\\partial \\mathbf{h}^{(\\ell)}} \\cdot \\frac{\\partial \\mathbf{h}^{(\\ell)}}{\\partial \\tilde{m}_j^{(\\ell)}} \\cdot \\frac{\\partial \\tilde{m}_j^{(\\ell)}}{\\partial s_j^{(\\ell)}},\n\\end{equation*}\nwhere the Jacobian $\\partial \\mathbf{z} / \\partial \\mathbf{h}^{(\\ell)}$ propagates through all downstream layers, making each neuron's gradient dependent on every other neuron's mask state.\nChanging one neuron's mask affects all output logits; KL captures this because it measures distributional divergence over the entire vocabulary.\nA Gumbel-Sigmoid relaxation~\\cite{jang2017gumbel} provides differentiable mask sampling during training, bridging the gap between soft training masks and hard inference decisions.\nThe predictor itself is a lightweight two-layer MLP (Linear $4096 \\to 128$, GELU, Linear $128 \\to 14336$) with 2.37M parameters per layer and 75.9M total---under 1\\% of the base model---and requires no compensation network at inference.\n\nEmpirically, the structural argument is borne out across sparsity levels, training budgets, and architectures.\nAt 50\\% sparsity on LLaMA-3.1-8B, the KL-trained predictor achieves PPL 11.79 under TEAL's global allocation, compared to 23.31 for vanilla TEAL.\nBCE trained for 2700 steps (2.71$\\times$ our compute budget) reaches only 27.97, and its training loss saturates with $\\Delta = -0.006$ over the final 2200 steps---confirming that the failure is structural, not computational.\nThe KL advantage scales super-linearly with sparsity: 18\\% relative improvement at 30\\%, 49\\% at 50\\%, and 82\\% at 70\\%.\nCross-architecture evaluation on Mistral-7B-v0.3~\\cite{jiang2023mistral} yields +63\\% relative degradation from dense, compared to +93\\% on LLaMA, confirming generalization to SwiGLU models with different attention configurations.\nWe also analyze SPON's~\\cite{xu2026spon} static bias correction and find it near-orthogonal to the predictor's effect (cosine similarity 0.196), recovering only 2.4\\% of remaining error---the KL predictor already captures most of the recoverable signal.\n\nTo situate these findings, we propose a two-dimensional taxonomy (Figure~\\ref{fig:taxonomy}) that classifies sparsity prediction methods along \\emph{correction granularity} (static, per-layer, per-token) and \\emph{training signal coupling} (decomposed, intermediate, coupled).\nPrior methods occupy distinct cells: SPON~\\cite{xu2026spon} combines static correction with coupled KL training; ShadowLLM~\\cite{akhauri2024shadowllm} uses per-layer prediction with intermediate MSE; FastForward~\\cite{gautam2026fastforward} and DejaVu~\\cite{liu2023dejavu} achieve per-token granularity but with decomposed BCE objectives.\nNo prior work has combined per-token contextual prediction with a coupled training signal.\nOur method fills this cell, unifying input-dependent mask generation with an objective that reflects global neuron interactions through the output distribution.\n\nOur contributions are:\n\\begin{itemize}[nosep,leftmargin=*]\n\\item We show that a KL-trained contextual predictor eliminates the need for error compensation networks in activation sparsity, and provide a formal gradient analysis explaining the structural mismatch between per-neuron BCE training and global top-$k$ inference allocation.\n\\item We propose a 2D taxonomy (correction granularity $\\times$ training signal coupling) that unifies existing activation sparsity methods (Figure~\\ref{fig:taxonomy}) and identifies the previously unexplored cell our method occupies.\n\\item We identify a phase transition in sparsity regimes---allocation-fixable ($\\leq$30\\%, where predictor and allocation choices recover downstream performance) vs.\\ capacity-limited ($\\geq$50\\%, where no method recovers reasoning ability)---and confirm via SPON orthogonality analysis that static correction provides diminishing returns once a coupled predictor is present.\n\\end{itemize}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me look at the bib keys mentioned in the task:
- liu2025teal ✓
- lee2024cats ✓
- zhang2025rsparse ✓
- liu2023dejavu ✓
- akhauri2024shadowllm ✓
- gautam2026fastforward ✓
- song2024powerinfer ✓
- xu2026spon ✓
- mirzadeh2024relu ✓
- song2024turbosparse ✓


- song2025prosparse ✓

I'm noticing some discrepancies between what the task specifies and what's in the bibliography. The luo2024sparsing entry appears as luo2024sparsinglaw in the actual references, and federici2024dip is listed as federici2025dip. I need to verify these exact keys before proceeding.

Looking at the WINA reference the task mentions, I don't see a standalone entry for it in the bib file—it seems to be part of the TEAL paper discussion, so I'll need to check if that's a separate citation or if it's covered under the liu2025teal reference.

Now I'm ready to draft the Related Work section following the ACL 2023 format with the four-cluster structure, keeping it around 700 words and making sure each cluster ends with how our work differs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "df00aca7-48ba-436a-8bac-4a305bc6f2b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReM7sZjTJgJqfZdACJqvZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7252,
      "cache_read_input_tokens": 30195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7252
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

_source line 15_

Now I have the full context. Let me check if the paper directory exists at the output path.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "278d5ac8-22aa-46cb-902d-070e3b105a78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReM7sZjTJgJqfZdACJqvZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7252,
      "cache_read_input_tokens": 30195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7252
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

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01ASUfpWLG9jiijbKTQBrTKg`</summary>

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
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "31f8742d-7565-4dae-9346-6b6d44f59900",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ReM7sZjTJgJqfZdACJqvZC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7252,
      "cache_read_input_tokens": 30195,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7252
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

_source line 17 · 2026-05-16T13:07:35.628Z_

<details><summary>↩ Tool result · `toolu_01ASUfpWLG9jiijbKTQBrTKg`</summary>

```text
experiments.tex
introduction.tex
method.tex
references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "d320c907-d986-4685-8c11-84aa0139036d",
  "tool_use_result": {
    "stdout": "experiments.tex\nintroduction.tex\nmethod.tex\nreferences.bib",
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

I note two bib key discrepancies: the task specifies `luo2024sparsing` and `federici2024dip`, but the actual .bib file has `luo2024sparsinglaw` and `federici2025dip`. I'll use the actual keys from the .bib file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "d1fd765b-3103-4bb4-b5c6-c4be4a59f2a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMC1boNAzQsea1iFDSqoVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 37447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
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

<details open><summary>🔧 Tool call — Write · `toolu_01Fs9E6DxHLxGQcmFkg2bi1E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
  "content": "\\section{Related Work}\n\n\\paragraph{Training-Free Activation Sparsity.}\nTraining-free methods exploit inherent activation sparsity without auxiliary learned components.\nTEAL~\\cite{liu2025teal} applies global top-$k$ selection by activation magnitude across all FFN layers, achieving 40--50\\% sparsity with no training cost; its importance-weighted variant (WINA) rescales magnitudes by learned column norms but remains input-independent at the selection stage.\nCATS~\\cite{lee2024cats} introduces contextually-aware thresholding that adapts a fixed percentile cutoff per layer, designed for SiLU/SwiGLU activations where magnitudes do not naturally cluster near zero.\nR-Sparse~\\cite{zhang2025rsparse} decomposes weight matrices via rank-aware SVD and predicts sparsity from low-rank projections, reporting 43\\% wall-clock speedup without fine-tuning.\nDIP~\\cite{federici2025dip} combines dynamic input pruning with cache-aware masking for efficient batched inference.\nDespite varying selection strategies, all training-free methods determine masks from fixed statistics or input-independent criteria.\nOur predictor differs fundamentally: it generates \\emph{input-dependent} masks trained to minimize output-distribution divergence, enabling allocation decisions that account for token-specific neuron interactions.\n\n\\paragraph{Predictor-Based Contextual Sparsity.}\nLearned predictors replace heuristic selection with small auxiliary networks that anticipate activation patterns.\nDejaVu~\\cite{liu2023dejavu} introduced this paradigm with a two-layer MLP trained via binary cross-entropy (BCE) to classify each neuron independently, achieving 2$\\times$ speedup on OPT-175B.\nShadowLLM~\\cite{akhauri2024shadowllm} improves predictor architecture with attention-based routing and MSE-based intermediate supervision but retains per-neuron decomposition in its training signal.\nFastForward~\\cite{gautam2026fastforward} augments the predictor with a 67.2M-parameter error compensation network that corrects output distortion from misclassified neurons, using BCE loss for mask prediction and an additive correction to recover accuracy---adding inference latency proportional to compensation depth.\nPowerInfer~\\cite{song2024powerinfer} exploits the power-law distribution of neuron activation frequencies for heterogeneous GPU--CPU scheduling, treating hot neurons as static and cold neurons as input-dependent.\nAll predictor-based methods train with decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other neurons' mask states.\nOur method uses a \\emph{coupled} KL objective: the gradient for any single neuron propagates through all downstream layers and the full output distribution, naturally optimizing for global allocation quality without requiring error compensation modules.\n\n\\paragraph{Static Bias Correction.}\nSPON~\\cite{xu2026spon} addresses sparsity-induced distributional shift by learning input-independent bias vectors via KL divergence between sparse and dense outputs.\nThese bias vectors are absorbed into model parameters at deployment, incurring zero additional inference cost.\nSPON demonstrates that even a static correction can partially recover output fidelity under fixed-threshold sparsity.\nHowever, its correction is fundamentally limited to systematic (input-independent) bias; it cannot adapt to token-specific activation patterns.\nOur work also employs KL divergence as the training signal but trains a \\emph{contextual predictor} rather than a static correction.\nWe empirically show that SPON's bias vectors are near-orthogonal to our predictor's effect (cosine similarity 0.196), recovering only 2.4\\% of residual error when applied on top of our method---confirming that the KL predictor already captures most recoverable signal, leaving little for static correction to exploit.\n\n\\paragraph{Activation Function Engineering.}\nAn alternative line of work modifies the activation function itself to induce natural sparsity.\nReLU Strikes Back~\\cite{mirzadeh2024relu} replaces SiLU with ReLU and applies continual pretraining, yielding $>$90\\% natural zero activations that trivially enable sparse computation.\nTurboSparse~\\cite{song2024turbosparse} introduces dReLU (double-ReLU gating) for extreme sparsity ratios exceeding 90\\%, while ProSparse~\\cite{song2025prosparse} progressively sparsifies activations during pretraining through scheduled activation penalties.\nComplementing these empirical methods, the Sparsing Law~\\cite{luo2024sparsinglaw} characterizes how activation density in SiLU/SwiGLU models increases with training compute---formalizing why longer-trained models resist magnitude-based pruning and motivating external prediction mechanisms.\nMiniTron~\\cite{muralidharan2024minitron} combines structured pruning with knowledge distillation but modifies model architecture permanently.\nAll activation-engineering approaches require modifying pretrained weights or retraining from scratch, altering the model's learned representations.\nOur method is a plug-in predictor that operates on \\emph{unmodified} SwiGLU models: it attaches lightweight prediction heads without changing any pretrained parameter, preserving full compatibility with existing model checkpoints and inference infrastructure.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "ab4d82b2-7406-4509-a7b7-08fd2649c7ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UMC1boNAzQsea1iFDSqoVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 37447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
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

_source line 20 · 2026-05-16T13:08:11.383Z_

<details><summary>↩ Tool result · `toolu_01Fs9E6DxHLxGQcmFkg2bi1E`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "846137b4-c259-474a-b22d-ad4f2df471b8",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex",
    "content": "\\section{Related Work}\n\n\\paragraph{Training-Free Activation Sparsity.}\nTraining-free methods exploit inherent activation sparsity without auxiliary learned components.\nTEAL~\\cite{liu2025teal} applies global top-$k$ selection by activation magnitude across all FFN layers, achieving 40--50\\% sparsity with no training cost; its importance-weighted variant (WINA) rescales magnitudes by learned column norms but remains input-independent at the selection stage.\nCATS~\\cite{lee2024cats} introduces contextually-aware thresholding that adapts a fixed percentile cutoff per layer, designed for SiLU/SwiGLU activations where magnitudes do not naturally cluster near zero.\nR-Sparse~\\cite{zhang2025rsparse} decomposes weight matrices via rank-aware SVD and predicts sparsity from low-rank projections, reporting 43\\% wall-clock speedup without fine-tuning.\nDIP~\\cite{federici2025dip} combines dynamic input pruning with cache-aware masking for efficient batched inference.\nDespite varying selection strategies, all training-free methods determine masks from fixed statistics or input-independent criteria.\nOur predictor differs fundamentally: it generates \\emph{input-dependent} masks trained to minimize output-distribution divergence, enabling allocation decisions that account for token-specific neuron interactions.\n\n\\paragraph{Predictor-Based Contextual Sparsity.}\nLearned predictors replace heuristic selection with small auxiliary networks that anticipate activation patterns.\nDejaVu~\\cite{liu2023dejavu} introduced this paradigm with a two-layer MLP trained via binary cross-entropy (BCE) to classify each neuron independently, achieving 2$\\times$ speedup on OPT-175B.\nShadowLLM~\\cite{akhauri2024shadowllm} improves predictor architecture with attention-based routing and MSE-based intermediate supervision but retains per-neuron decomposition in its training signal.\nFastForward~\\cite{gautam2026fastforward} augments the predictor with a 67.2M-parameter error compensation network that corrects output distortion from misclassified neurons, using BCE loss for mask prediction and an additive correction to recover accuracy---adding inference latency proportional to compensation depth.\nPowerInfer~\\cite{song2024powerinfer} exploits the power-law distribution of neuron activation frequencies for heterogeneous GPU--CPU scheduling, treating hot neurons as static and cold neurons as input-dependent.\nAll predictor-based methods train with decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other neurons' mask states.\nOur method uses a \\emph{coupled} KL objective: the gradient for any single neuron propagates through all downstream layers and the full output distribution, naturally optimizing for global allocation quality without requiring error compensation modules.\n\n\\paragraph{Static Bias Correction.}\nSPON~\\cite{xu2026spon} addresses sparsity-induced distributional shift by learning input-independent bias vectors via KL divergence between sparse and dense outputs.\nThese bias vectors are absorbed into model parameters at deployment, incurring zero additional inference cost.\nSPON demonstrates that even a static correction can partially recover output fidelity under fixed-threshold sparsity.\nHowever, its correction is fundamentally limited to systematic (input-independent) bias; it cannot adapt to token-specific activation patterns.\nOur work also employs KL divergence as the training signal but trains a \\emph{contextual predictor} rather than a static correction.\nWe empirically show that SPON's bias vectors are near-orthogonal to our predictor's effect (cosine similarity 0.196), recovering only 2.4\\% of residual error when applied on top of our method---confirming that the KL predictor already captures most recoverable signal, leaving little for static correction to exploit.\n\n\\paragraph{Activation Function Engineering.}\nAn alternative line of work modifies the activation function itself to induce natural sparsity.\nReLU Strikes Back~\\cite{mirzadeh2024relu} replaces SiLU with ReLU and applies continual pretraining, yielding $>$90\\% natural zero activations that trivially enable sparse computation.\nTurboSparse~\\cite{song2024turbosparse} introduces dReLU (double-ReLU gating) for extreme sparsity ratios exceeding 90\\%, while ProSparse~\\cite{song2025prosparse} progressively sparsifies activations during pretraining through scheduled activation penalties.\nComplementing these empirical methods, the Sparsing Law~\\cite{luo2024sparsinglaw} characterizes how activation density in SiLU/SwiGLU models increases with training compute---formalizing why longer-trained models resist magnitude-based pruning and motivating external prediction mechanisms.\nMiniTron~\\cite{muralidharan2024minitron} combines structured pruning with knowledge distillation but modifies model architecture permanently.\nAll activation-engineering approaches require modifying pretrained weights or retraining from scratch, altering the model's learned representations.\nOur method is a plug-in predictor that operates on \\emph{unmodified} SwiGLU models: it attaches lightweight prediction heads without changing any pretrained parameter, preserving full compatibility with existing model checkpoints and inference infrastructure.\n",
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

Written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex`. Four clusters (~690 words), each ending with a clear distinction statement. Uses the actual bib keys from `references.bib` (`luo2024sparsinglaw` and `federici2025dip` rather than the slightly different keys in the task spec).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "uuid": "42193839-0b2c-47cb-9e49-34a769d2da01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0117USErnKwPEU1Xmj2aAMQ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 38294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1482
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

_source line 22_

Written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex`. Four clusters (~690 words), each ending with a clear distinction statement. Uses the actual bib keys from `references.bib` (`luo2024sparsinglaw` and `federici2025dip` rather than the slightly different keys in the task spec).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 80023,
  "duration_api_ms": 81298,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "212830c6-71b7-44f0-84f5-70626d8d6b48",
  "total_cost_usd": 0.31703925000000005,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 27935,
    "cache_read_input_tokens": 142243,
    "output_tokens": 2766,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 27935,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 101,
        "cache_read_input_tokens": 38294,
        "cache_creation_input_tokens": 1482,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1482
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2054,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002139,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 2766,
      "cacheReadInputTokens": 142243,
      "cacheCreationInputTokens": 27935,
      "webSearchRequests": 0,
      "costUSD": 0.31490025000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d2744ab7-78bb-43a1-a254-7f0772c36a1b"
}
```

</details>

---
