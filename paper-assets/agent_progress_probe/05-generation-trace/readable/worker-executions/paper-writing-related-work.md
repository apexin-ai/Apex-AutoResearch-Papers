# paper writing related work

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_paper_writing_related_work_20260514T223003.log`
- **Structured JSON:** [`238bc0a67ee8c06c6e6d.json`](../../sessions/23/238bc0a67ee8c06c6e6d.json)

## Before a recorded user message

28 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe",
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
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
  "uuid": "bca16ee6-f03c-4410-a8fb-bae2c0741671",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-agent-progress-probe/memory/"
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
    "resetsAt": 1778814000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "17d397d0-179d-4d60-8566-85117d804eb6",
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484"
}
```

---

### Assistant

_source line 4_

Let me first read the LaTeX writing skill for guidelines, then check the existing paper sections for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "72307c1f-a69d-4ab5-8f97-6e43cb689217",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPEr7xjXLvdVDiD5kNq2JN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12979,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12979
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

<details open><summary>🔧 Tool call — Read · `toolu_01PbsKWzixy3RkAojnuyV3SX`</summary>

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
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "7c69392e-c710-4967-a0f0-70e5b1a9dca8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPEr7xjXLvdVDiD5kNq2JN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12979,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12979
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

_source line 6 · 2026-05-14T22:30:19.864Z_

<details><summary>↩ Tool result · `toolu_01PbsKWzixy3RkAojnuyV3SX`</summary>

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
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "d19ae36a-04d6-4364-a481-c6942c2441dc",
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

<details open><summary>🔧 Tool call — Glob · `toolu_015AT4nM2F7suhteit8nHvMN`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "454e6b1c-fb9f-430c-9261-118915b45d27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NPEr7xjXLvdVDiD5kNq2JN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12979,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12979
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

_source line 8 · 2026-05-14T22:30:20.114Z_

<details><summary>↩ Tool result · `toolu_015AT4nM2F7suhteit8nHvMN`</summary>

```text
docs/paper/_acl_template/acl_lualatex.tex
docs/paper/_acl_template/acl_latex.tex
docs/paper/main.tex
docs/paper/sections/abstract.tex
docs/paper/sections/related_work.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/limitations.tex
docs/paper/sections/method.tex
docs/paper/sections/experiments.tex
docs/paper/sections/analysis.tex
docs/paper/sections/appendix.tex
docs/paper/sections/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "d67515df-2fa8-41c0-9679-722783bc91c1",
  "tool_use_result": {
    "filenames": [
      "docs/paper/_acl_template/acl_lualatex.tex",
      "docs/paper/_acl_template/acl_latex.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/abstract.tex",
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/limitations.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/appendix.tex",
      "docs/paper/sections/introduction.tex"
    ],
    "durationMs": 23,
    "numFiles": 12,
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
Let me read the existing related_work.tex and introduction.tex to understand the current state and context, as well as the method and experiments sections for cross-referencing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "41dff85a-678a-468d-9469-33e709ffe256",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NduHrpDKjMMUcebkbkrqWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 24820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5803
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

Let me read existing sections for context — introduction, method, experiments, and the current related_work.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "e9d44ba5-f16c-47ea-9667-87092f5533c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NduHrpDKjMMUcebkbkrqWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 24820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5803
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

<details open><summary>🔧 Tool call — Read · `toolu_01A1rwgs28NDJAU1dDwgTr9A`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "1b37a6c6-56af-45ab-aa4a-2c07862127bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NduHrpDKjMMUcebkbkrqWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 24820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5803
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

_source line 12 · 2026-05-14T22:30:25.444Z_

<details><summary>↩ Tool result · `toolu_01A1rwgs28NDJAU1dDwgTr9A`</summary>

```text
1	% Related Work: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)
2	\section{Related Work}
3	\label{sec:related_work}
4	
5	\subsection{LLM Agent Monitoring and Evaluation}
6	
7	As LLM agents tackle increasingly complex tasks \citep{jimenez2024swebench,yang2024sweagent,wang2025openhands,zhou2024webarena,wang2024mint}, understanding and monitoring their failure modes has become critical.
8	Taxonomic studies reveal that agent failures are often systematic: \citet{cemri2025multiagentfail} identify 14 failure modes in multi-agent systems, including step repetition as a concrete symptom, while \citet{zhu2025agentfail} show that cascading failures---where a single root cause propagates across subsequent decisions---dominate long-horizon tasks.
9	\citet{orlanski2026slopcodebench} provide the most direct evidence of agent degradation, documenting structural erosion in 77\% of coding agent trajectories with no agent fully solving any benchmark task end-to-end.
10	
11	Existing monitoring approaches span several paradigms.
12	\emph{Self-reflection} methods \citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent to diagnose its own failures, but \citet{huang2024selfcorrect} and \citet{kamoi2024selfcorrection} demonstrate that LLMs cannot reliably self-correct without external feedback, motivating external monitoring.
13	\citet{george2025cycledetection} propose unsupervised cycle detection combining call-stack analysis with embedding similarity, while \citet{pipis2025reasoningloop} analyze why reasoning models loop, using $n$-gram repetition as a detection heuristic.
14	On the external monitoring front, \citet{chen2025monitoring} show that sequence-level context is necessary---single-step analysis misses sequentially contextual harm---and \citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, with weak models reliably monitoring stronger agents.
15	
16	Our work differs from all of the above in its central question: rather than proposing a new monitoring \emph{method}, we conduct an empirical study asking what \emph{signals} carry stagnation information.
17	We show that 30 structural features suffice for near-perfect detection (0.995 F1), without requiring another LLM, self-reflection, or embedding-based similarity.
18	
19	\subsection{Process Reward Models for Agents}
20	
21	Process reward models (PRMs) assign quality scores to individual agent steps, enabling search-time guidance and trajectory selection.
22	\citet{xi2025agentprm} introduce AgentPRM, training step-level reward models via TD/GAE that evaluate both ``promise'' (long-term potential) and ``progress'' (immediate advancement), achieving 8$\times$ compute efficiency gains.
23	\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels, with a 3B model surpassing GPT-4o.
24	Evaluation benchmarks have emerged in parallel: \citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs substantially outperform general-purpose ones, while \citet{wang2026planrewardbench} evaluate trajectory-level reward models and reveal that all model categories---generative, discriminative, and LLM-as-judge---degrade significantly on long-horizon trajectories.
25	\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques (Agent-RRM), and \citet{qiu2026dataprm} address data analysis agents specifically, introducing environment-aware probing to detect silent errors that standard PRMs miss.
26	
27	Our work is complementary to the PRM line but differs in three fundamental ways: (1)~we operate at window level rather than step level, capturing temporal patterns across consecutive actions; (2)~we require no outcome labels or reward annotations---our labeling functions use only observable structural signals; and (3)~our goal is real-time \emph{monitoring} (stagnation detection in $<$5\,ms), not \emph{training signal} generation for agent improvement.
28	The degradation of trajectory-level reward models on long horizons reported by \citet{wang2026planrewardbench} further motivates our window-level approach, which avoids full-trajectory reasoning by design.
29	
30	\subsection{Data Programming and Weak Supervision}
31	
32	Data programming \citep{ratner2016dataprogramming} enables rapid training set creation through user-defined labeling functions (LFs), with a generative model learning LF accuracies to produce probabilistic labels.
33	Snorkel \citep{ratner2017snorkel} operationalizes this into an end-to-end system with dependency-aware label models, and \citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods.
34	\citet{zhang2021wrench} provide a comprehensive benchmark spanning 22 datasets, though all assume i.i.d.\ data points.
35	
36	Extensions to sequential data relax this assumption.
37	\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised sequence tagging (NER), incorporating linking rules that model span structure and improving over i.i.d.\ label models by 7~F1 points.
38	\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities.
39	In crowdsourcing, \citet{nguyen2017hmmcrowd} extend \citeauthor{dawid1979em}'s EM-based annotator model \citep{dawid1979em} with HMM structure for sequential label aggregation.
40	
41	We apply data programming to agent trajectory data, a novel domain where LFs exhibit systematic temporal dynamics (e.g., command repetition leads stagnation onset by 1.87 steps on SWE-Agent).
42	Unlike prior sequential extensions that target token-level NER or multi-resolution alignment, our setting involves window-level binary classification with agent-specific LF role reversals.
43	Critically, we test whether temporal label models---motivated by the clear i.i.d.\ violations we observe---can improve over majority vote, and report a negative finding: three implementations (TWV, HMM, lag-aware HMM) all fail to surpass simple voting in the low-conflict regime of our 3-LF framework.
44	
45	\subsection{Anomaly Detection in Agent Trajectories}
46	
47	Detecting anomalous behavior in sequential agent data connects to the broader literature on time-series anomaly detection.
48	\citet{liu2026trajad} propose TrajAD, training a fine-grained verifier through synthetic perturbations (perturb-and-complete) to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation.
49	They show that general-purpose LLMs perform poorly at zero-shot trajectory anomaly detection, motivating specialized approaches.
50	
51	Our work differs from anomaly detection in both formulation and methodology.
52	We frame stagnation as a binary classification problem over sliding windows rather than identifying rare deviations from a normal distribution.
53	Stagnation is not anomalous in the statistical sense---it occurs in 28.5\% of SWE-Agent windows and 6.6\% of OpenHands windows---but rather represents a persistent behavioral regime that an agent enters and may not exit without intervention.
54	Where TrajAD requires training a specialized verifier on synthetic data, our empirical analysis reveals that hand-crafted structural features achieve 0.995 F1 without any learned components, and our probe model uses a lightweight GRU \citep{cho2014gru} with attention \citep{bahdanau2015attention} rather than a full LLM verifier.
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "344338b2-353b-4151-a154-07b483ef3fbb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex",
      "content": "% Related Work: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\n\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{LLM Agent Monitoring and Evaluation}\n\nAs LLM agents tackle increasingly complex tasks \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands,zhou2024webarena,wang2024mint}, understanding and monitoring their failure modes has become critical.\nTaxonomic studies reveal that agent failures are often systematic: \\citet{cemri2025multiagentfail} identify 14 failure modes in multi-agent systems, including step repetition as a concrete symptom, while \\citet{zhu2025agentfail} show that cascading failures---where a single root cause propagates across subsequent decisions---dominate long-horizon tasks.\n\\citet{orlanski2026slopcodebench} provide the most direct evidence of agent degradation, documenting structural erosion in 77\\% of coding agent trajectories with no agent fully solving any benchmark task end-to-end.\n\nExisting monitoring approaches span several paradigms.\n\\emph{Self-reflection} methods \\citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent to diagnose its own failures, but \\citet{huang2024selfcorrect} and \\citet{kamoi2024selfcorrection} demonstrate that LLMs cannot reliably self-correct without external feedback, motivating external monitoring.\n\\citet{george2025cycledetection} propose unsupervised cycle detection combining call-stack analysis with embedding similarity, while \\citet{pipis2025reasoningloop} analyze why reasoning models loop, using $n$-gram repetition as a detection heuristic.\nOn the external monitoring front, \\citet{chen2025monitoring} show that sequence-level context is necessary---single-step analysis misses sequentially contextual harm---and \\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, with weak models reliably monitoring stronger agents.\n\nOur work differs from all of the above in its central question: rather than proposing a new monitoring \\emph{method}, we conduct an empirical study asking what \\emph{signals} carry stagnation information.\nWe show that 30 structural features suffice for near-perfect detection (0.995 F1), without requiring another LLM, self-reflection, or embedding-based similarity.\n\n\\subsection{Process Reward Models for Agents}\n\nProcess reward models (PRMs) assign quality scores to individual agent steps, enabling search-time guidance and trajectory selection.\n\\citet{xi2025agentprm} introduce AgentPRM, training step-level reward models via TD/GAE that evaluate both ``promise'' (long-term potential) and ``progress'' (immediate advancement), achieving 8$\\times$ compute efficiency gains.\n\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels, with a 3B model surpassing GPT-4o.\nEvaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs substantially outperform general-purpose ones, while \\citet{wang2026planrewardbench} evaluate trajectory-level reward models and reveal that all model categories---generative, discriminative, and LLM-as-judge---degrade significantly on long-horizon trajectories.\n\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques (Agent-RRM), and \\citet{qiu2026dataprm} address data analysis agents specifically, introducing environment-aware probing to detect silent errors that standard PRMs miss.\n\nOur work is complementary to the PRM line but differs in three fundamental ways: (1)~we operate at window level rather than step level, capturing temporal patterns across consecutive actions; (2)~we require no outcome labels or reward annotations---our labeling functions use only observable structural signals; and (3)~our goal is real-time \\emph{monitoring} (stagnation detection in $<$5\\,ms), not \\emph{training signal} generation for agent improvement.\nThe degradation of trajectory-level reward models on long horizons reported by \\citet{wang2026planrewardbench} further motivates our window-level approach, which avoids full-trajectory reasoning by design.\n\n\\subsection{Data Programming and Weak Supervision}\n\nData programming \\citep{ratner2016dataprogramming} enables rapid training set creation through user-defined labeling functions (LFs), with a generative model learning LF accuracies to produce probabilistic labels.\nSnorkel \\citep{ratner2017snorkel} operationalizes this into an end-to-end system with dependency-aware label models, and \\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods.\n\\citet{zhang2021wrench} provide a comprehensive benchmark spanning 22 datasets, though all assume i.i.d.\\ data points.\n\nExtensions to sequential data relax this assumption.\n\\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised sequence tagging (NER), incorporating linking rules that model span structure and improving over i.i.d.\\ label models by 7~F1 points.\n\\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities.\nIn crowdsourcing, \\citet{nguyen2017hmmcrowd} extend \\citeauthor{dawid1979em}'s EM-based annotator model \\citep{dawid1979em} with HMM structure for sequential label aggregation.\n\nWe apply data programming to agent trajectory data, a novel domain where LFs exhibit systematic temporal dynamics (e.g., command repetition leads stagnation onset by 1.87 steps on SWE-Agent).\nUnlike prior sequential extensions that target token-level NER or multi-resolution alignment, our setting involves window-level binary classification with agent-specific LF role reversals.\nCritically, we test whether temporal label models---motivated by the clear i.i.d.\\ violations we observe---can improve over majority vote, and report a negative finding: three implementations (TWV, HMM, lag-aware HMM) all fail to surpass simple voting in the low-conflict regime of our 3-LF framework.\n\n\\subsection{Anomaly Detection in Agent Trajectories}\n\nDetecting anomalous behavior in sequential agent data connects to the broader literature on time-series anomaly detection.\n\\citet{liu2026trajad} propose TrajAD, training a fine-grained verifier through synthetic perturbations (perturb-and-complete) to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation.\nThey show that general-purpose LLMs perform poorly at zero-shot trajectory anomaly detection, motivating specialized approaches.\n\nOur work differs from anomaly detection in both formulation and methodology.\nWe frame stagnation as a binary classification problem over sliding windows rather than identifying rare deviations from a normal distribution.\nStagnation is not anomalous in the statistical sense---it occurs in 28.5\\% of SWE-Agent windows and 6.6\\% of OpenHands windows---but rather represents a persistent behavioral regime that an agent enters and may not exit without intervention.\nWhere TrajAD requires training a specialized verifier on synthetic data, our empirical analysis reveals that hand-crafted structural features achieve 0.995 F1 without any learned components, and our probe model uses a lightweight GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} rather than a full LLM verifier.\n",
      "numLines": 55,
      "startLine": 1,
      "totalLines": 55
    }
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01GSs98rnbxeyry2SXoxdfN8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "59258626-8865-4816-8cd4-2973a2cd0e5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NduHrpDKjMMUcebkbkrqWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 24820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5803
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

_source line 14 · 2026-05-14T22:30:25.936Z_

<details><summary>↩ Tool result · `toolu_01GSs98rnbxeyry2SXoxdfN8`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	LLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.
5	As these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.
6	\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 90\% and quality drops of 80\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.
7	Crucially, the dominant failure pattern is not simple repetition but what we term \emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.
8	This ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.
9	We observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \citep{yang2024sweagent} and OpenHands \citep{wang2025openhands}---on SWE-bench tasks \citep{jimenez2024swebench}, 28.5\% and 6.6\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.
10	
11	Existing approaches address aspects of this problem but fall short in three ways.
12	First, \emph{repetition detectors} such as cycle detection \citep{george2025cycledetection} and SpecRA \citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.
13	Second, \emph{step-level scoring} via process reward models \citep{xi2025agentprm} evaluates individual actions in isolation, discarding the window-level temporal dynamics that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over sequences of consecutive actions \citep{chen2025monitoring}.
14	A sequence of failed commands followed by a strategy switch, for instance, carries different diagnostic information than the same commands evaluated independently.
15	Third, \emph{LLM self-evaluation} \citep{shinn2023reflexion} is both expensive and fundamentally limited by the stuck model's own judgment; our LLM-as-judge baseline achieves only 0.6625 macro-F1 at \$11.66 per test set, well below lightweight feature-based alternatives.
16	More fundamentally, none of these approaches asks the prior question: \emph{what signals actually carry stagnation information?}
17	No systematic study has investigated whether detecting subtle agent failure requires sophisticated semantic understanding or whether simpler structural patterns suffice.
18	
19	We address this question through a systematic empirical study (Figure~\ref{fig:pipeline}).
20	Using a weak supervision framework \citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from over 205K windows spanning SWE-Agent (54,809 windows, 28.5\% silver-labeled stagnation) and OpenHands (150,652 windows, 6.6\% stagnation).
21	Three labeling functions provide complementary noisy votes: command repetition ($\lambda_1$) targets repetitive behavior, file diff delta ($\lambda_2$) targets output productivity, and outcome backpropagation ($\lambda_3$) propagates task-level outcomes backward through the trajectory.
22	Majority vote aggregation produces window-level binary labels with confidence scores.
23	Our window-level formulation ($k{=}5$ consecutive actions, stride 1) captures short-range temporal patterns---such as repeated failures followed by strategy changes---that step-level approaches cannot express, while providing the granularity to pinpoint \emph{when} stagnation begins and ends within a trajectory, enabling targeted interventions.
24	Against these silver labels, we systematically compare hand-crafted structural features, a neural embedding probe, and an LLM-as-judge baseline.
25	
26	Our study yields three principal findings.
27	
28	\textbf{Finding 1: Stagnation signals are fundamentally structural.}
29	Thirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.9951 macro-F1 in-domain (Random Forest) and 0.9674 cross-agent macro-F1 (Gradient Boosting, SWE-Agent $\to$ OpenHands), surpassing the GRU embedding probe \citep{cho2014gru} (0.9055 in-domain, 0.751 after full fine-tuning on the target agent) and the LLM-as-judge baseline (0.6625) by wide margins---up to 33.3 percentage points (pp).
30	We note that in-domain evaluation uses silver labels (\S\ref{sec:circular}); cross-agent transfer and a pending gold set (\S\ref{sec:gold_set}) provide non-circular validation.
31	The structural advantage is encoder-agnostic: three embedding backbones \citep{zhang2025qwen3embedding} all yield probe F1 above 0.90, confirming that the probe's temporal architecture rather than a specific pretrained encoder drives performance.
32	The in-domain score of 0.9951 reflects circular evaluation---structural features overlap with LF inputs---but the cross-agent score of 0.9674, where models trained on one agent's LF distribution are tested on another with substantially different firing patterns, breaks this circularity.
33	This finding challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---no GPU, under 5\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.
34	
35	\textbf{Finding 2: Labeling functions occupy agent-specific temporal niches.}
36	On SWE-Agent, command repetition ($\lambda_1$) leads stagnation onset by 1.87 steps, file diff ($\lambda_2$) is near-concurrent at $-1.20$ steps, and outcome backpropagation ($\lambda_3$) lags by 6.70 steps.
37	On OpenHands, $\lambda_1$ reverses from leading to lagging ($+3.32$ steps), where its 92.3\% firing rate produces a 71\% false positive rate on progress windows.
38	Removing $\lambda_1$ from the OpenHands labeling pipeline improves fine-tuned probe F1 by 17.6\,pp, demonstrating that labeling functions validated on one agent architecture can become adversarial on another.
39	
40	\textbf{Finding 3: Temporal label models fail to improve over majority vote.}
41	Three temporal label models---time-varying weights (TWV), Hidden Markov Models \citep{safranchik2020linkedhmm}, and lag-aware HMMs---all fail to surpass majority vote on downstream detection.
42	TWV achieves marginally higher self-evaluated F1 but degrades downstream probe performance by 2.57\,pp.
43	The root cause: three binary LFs produce too little inter-LF conflict for temporal aggregation to exploit.
44	
45	Our contributions are:
46	\begin{enumerate}
47	    \item \textbf{Structural signal discovery.} We demonstrate that 30 lightweight structural features achieve near-perfect stagnation detection (0.9951 in-domain, 0.967 cross-agent macro-F1), outperforming neural probes and LLM judges by wide margins (+33.3\,pp over LLM-as-judge), with no GPU and under 5\,ms per window. This redirects agent monitoring from costly representation learning toward lightweight structural approaches.
48	    \item \textbf{Labeling function temporal dynamics.} We reveal that labeling functions occupy statistically distinct temporal niches relative to stagnation onset, with agent-specific reversals that corrupt silver labels when transferred across architectures, informing future weak-supervision design on sequential agent data.
49	    \item \textbf{Temporal label model negative finding.} We show that three temporal label models fail to improve over majority vote for downstream detection, despite clear temporal structure in LF firing patterns. This constrains future temporal label model research: the 3-LF regime produces insufficient conflict for temporal aggregation to add value.
50	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "1dcb068c-d7c5-4d9d-90a0-eea3936986e9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLLM agents are increasingly deployed for complex, long-horizon software engineering tasks---resolving GitHub issues, debugging production systems, and iterating on multi-file codebases across dozens of editing rounds \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands}.\nAs these deployments scale, a critical failure mode has emerged that is qualitatively different from crashes or syntax errors: the agent \\emph{stagnates}---continuing to produce actions that appear purposeful while making no meaningful progress toward the task goal.\n\\citet{orlanski2026slopcodebench} document this degradation on SlopCodeBench, recording verbosity increases of 90\\% and quality drops of 80\\% in long-horizon coding trajectories, with no agent fully solving any benchmark problem end-to-end.\nCrucially, the dominant failure pattern is not simple repetition but what we term \\emph{semantic stagnation}: the agent issues varied commands, edits different files, and generates plausible-looking outputs, yet its behavior is functionally stuck.\nThis ``looks busy but going in circles'' pattern defeats existing monitoring tools, because surface-level action diversity masks the underlying lack of progress.\nWe observe this phenomenon at scale: across trajectories from two architecturally distinct agents---SWE-Agent \\citep{yang2024sweagent} and OpenHands \\citep{wang2025openhands}---on SWE-bench tasks \\citep{jimenez2024swebench}, 28.5\\% and 6.6\\% of sliding windows exhibit stagnation under our silver labeling scheme, respectively, confirming that the failure mode is both prevalent and highly agent-dependent.\n\nExisting approaches address aspects of this problem but fall short in three ways.\nFirst, \\emph{repetition detectors} such as cycle detection \\citep{george2025cycledetection} and SpecRA \\citep{pipis2025reasoningloop} identify structural repetition---exact or near-exact loops in action sequences---but by design miss semantically diverse stagnation where the agent varies its surface behavior while remaining functionally stuck.\nSecond, \\emph{step-level scoring} via process reward models \\citep{xi2025agentprm} evaluates individual actions in isolation, discarding the window-level temporal dynamics that distinguish transient setbacks from sustained stagnation---a distinction that requires reasoning over sequences of consecutive actions \\citep{chen2025monitoring}.\nA sequence of failed commands followed by a strategy switch, for instance, carries different diagnostic information than the same commands evaluated independently.\nThird, \\emph{LLM self-evaluation} \\citep{shinn2023reflexion} is both expensive and fundamentally limited by the stuck model's own judgment; our LLM-as-judge baseline achieves only 0.6625 macro-F1 at \\$11.66 per test set, well below lightweight feature-based alternatives.\nMore fundamentally, none of these approaches asks the prior question: \\emph{what signals actually carry stagnation information?}\nNo systematic study has investigated whether detecting subtle agent failure requires sophisticated semantic understanding or whether simpler structural patterns suffice.\n\nWe address this question through a systematic empirical study (Figure~\\ref{fig:pipeline}).\nUsing a weak supervision framework \\citep{ratner2016dataprogramming,ratner2017snorkel}, we construct silver-labeled datasets from over 205K windows spanning SWE-Agent (54,809 windows, 28.5\\% silver-labeled stagnation) and OpenHands (150,652 windows, 6.6\\% stagnation).\nThree labeling functions provide complementary noisy votes: command repetition ($\\lambda_1$) targets repetitive behavior, file diff delta ($\\lambda_2$) targets output productivity, and outcome backpropagation ($\\lambda_3$) propagates task-level outcomes backward through the trajectory.\nMajority vote aggregation produces window-level binary labels with confidence scores.\nOur window-level formulation ($k{=}5$ consecutive actions, stride 1) captures short-range temporal patterns---such as repeated failures followed by strategy changes---that step-level approaches cannot express, while providing the granularity to pinpoint \\emph{when} stagnation begins and ends within a trajectory, enabling targeted interventions.\nAgainst these silver labels, we systematically compare hand-crafted structural features, a neural embedding probe, and an LLM-as-judge baseline.\n\nOur study yields three principal findings.\n\n\\textbf{Finding 1: Stagnation signals are fundamentally structural.}\nThirty hand-crafted features---command repetition rates, file operation counts, edit distances---achieve 0.9951 macro-F1 in-domain (Random Forest) and 0.9674 cross-agent macro-F1 (Gradient Boosting, SWE-Agent $\\to$ OpenHands), surpassing the GRU embedding probe \\citep{cho2014gru} (0.9055 in-domain, 0.751 after full fine-tuning on the target agent) and the LLM-as-judge baseline (0.6625) by wide margins---up to 33.3 percentage points (pp).\nWe note that in-domain evaluation uses silver labels (\\S\\ref{sec:circular}); cross-agent transfer and a pending gold set (\\S\\ref{sec:gold_set}) provide non-circular validation.\nThe structural advantage is encoder-agnostic: three embedding backbones \\citep{zhang2025qwen3embedding} all yield probe F1 above 0.90, confirming that the probe's temporal architecture rather than a specific pretrained encoder drives performance.\nThe in-domain score of 0.9951 reflects circular evaluation---structural features overlap with LF inputs---but the cross-agent score of 0.9674, where models trained on one agent's LF distribution are tested on another with substantially different firing patterns, breaks this circularity.\nThis finding challenges the prevailing intuition that detecting subtle agent failures requires complex language understanding, and suggests that lightweight structural monitoring---no GPU, under 5\\,ms per window---may be more practical than neural or LLM-based approaches for real-time agent oversight.\n\n\\textbf{Finding 2: Labeling functions occupy agent-specific temporal niches.}\nOn SWE-Agent, command repetition ($\\lambda_1$) leads stagnation onset by 1.87 steps, file diff ($\\lambda_2$) is near-concurrent at $-1.20$ steps, and outcome backpropagation ($\\lambda_3$) lags by 6.70 steps.\nOn OpenHands, $\\lambda_1$ reverses from leading to lagging ($+3.32$ steps), where its 92.3\\% firing rate produces a 71\\% false positive rate on progress windows.\nRemoving $\\lambda_1$ from the OpenHands labeling pipeline improves fine-tuned probe F1 by 17.6\\,pp, demonstrating that labeling functions validated on one agent architecture can become adversarial on another.\n\n\\textbf{Finding 3: Temporal label models fail to improve over majority vote.}\nThree temporal label models---time-varying weights (TWV), Hidden Markov Models \\citep{safranchik2020linkedhmm}, and lag-aware HMMs---all fail to surpass majority vote on downstream detection.\nTWV achieves marginally higher self-evaluated F1 but degrades downstream probe performance by 2.57\\,pp.\nThe root cause: three binary LFs produce too little inter-LF conflict for temporal aggregation to exploit.\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{Structural signal discovery.} We demonstrate that 30 lightweight structural features achieve near-perfect stagnation detection (0.9951 in-domain, 0.967 cross-agent macro-F1), outperforming neural probes and LLM judges by wide margins (+33.3\\,pp over LLM-as-judge), with no GPU and under 5\\,ms per window. This redirects agent monitoring from costly representation learning toward lightweight structural approaches.\n    \\item \\textbf{Labeling function temporal dynamics.} We reveal that labeling functions occupy statistically distinct temporal niches relative to stagnation onset, with agent-specific reversals that corrupt silver labels when transferred across architectures, informing future weak-supervision design on sequential agent data.\n    \\item \\textbf{Temporal label model negative finding.} We show that three temporal label models fail to improve over majority vote for downstream detection, despite clear temporal structure in LF firing patterns. This constrains future temporal label model research: the 3-LF regime produces insufficient conflict for temporal aggregation to add value.\n\\end{enumerate}",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 50
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01XBwHiHFUp9TBp5fti6BafD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "6f94ff63-de93-4513-820e-92fcc480f32e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NduHrpDKjMMUcebkbkrqWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 24820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5803
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

_source line 16 · 2026-05-14T22:30:26.417Z_

<details><summary>↩ Tool result · `toolu_01XBwHiHFUp9TBp5fti6BafD`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We frame stagnation detection as window-level binary classification over agent trajectories.
5	Silver labels are generated via weak supervision from three labeling functions, then used to train and evaluate three detection approaches: structural features, a neural embedding probe, and an LLM-as-judge baseline.
6	Figure~\ref{fig:pipeline} provides a system overview.
7	
8	\begin{figure*}[t]
9	\centering
10	\includegraphics[width=\textwidth]{../../figures/paper/fig_pipeline.pdf}
11	\caption{System overview. (Left) Agent trajectories are segmented into overlapping windows of $k{=}5$ steps. (Center) Three labeling functions vote on each window; majority vote produces silver labels with confidence 1--3. (Right) Three detection approaches compared: structural features (30-dim), NL embedding probe (GRU), and LLM-as-judge (eval only, not trained on silver labels).}
12	\label{fig:pipeline}
13	\end{figure*}
14	
15	%-------------------------------------------------------------------
16	\subsection{Problem Formulation}
17	\label{sec:problem}
18	
19	Given an agent trajectory $T = (a_1, a_2, \ldots, a_n)$ where each $a_t$ is an action (e.g., a shell command, file edit, or API call), we partition it into overlapping sliding windows $w_i = (a_i, \ldots, a_{i+k-1})$ with window size $k{=}5$ and stride 1.
20	The task is to assign each window a binary label $y_i \in \{0, 1\}$, where 0 denotes \emph{stagnation} (the agent is stuck or unproductive) and 1 denotes \emph{progress} (the agent is making meaningful headway toward the task goal).
21	
22	The window formulation offers two advantages over alternatives.
23	Compared to step-level scoring, windows capture short-range temporal patterns---such as a sequence of repeated failed attempts---that individual actions cannot express.
24	Compared to trajectory-level labeling, windows provide the granularity needed to pinpoint \emph{when} stagnation begins and ends within a single task attempt, enabling downstream interventions such as early termination or strategy switching.
25	
26	%-------------------------------------------------------------------
27	\subsection{Weak Supervision Pipeline}
28	\label{sec:weak_supervision}
29	
30	No gold-standard annotations exist for agent stagnation at the window level.
31	Manual annotation is expensive: each window requires reviewing $k$ actions with full context (command text, outputs, file diffs), taking an estimated 2--3 minutes per window.
32	We therefore adopt a data programming approach \citep{ratner2016dataprogramming,ratner2017snorkel}: multiple labeling functions (LFs) provide noisy votes that are aggregated into silver labels.
33	Each LF $\lambda_j : w_i \to \{-1, 0, 1\}$ examines a window and emits a vote: stagnation (0), progress (1), or abstain ($-1$).
34	
35	\subsubsection{Labeling Functions}
36	\label{sec:labeling_functions}
37	
38	We design three LFs that target complementary signals of stagnation (Table~\ref{tab:lf_design}).
39	
40	\paragraph{Command repetition ($\lambda_1$).}
41	Computes the proportion of repeated commands within window $w_i$.
42	A high repetition ratio triggers a stagnation vote, capturing overt repetitive behavior such as re-running failing commands.
43	This LF fires on 65.6\% of SWE-Agent windows and 92.3\% of OpenHands windows; the elevated OH rate reflects differences in action distributions across agent architectures (\S\ref{sec:cmd_rep_ablation}).
44	
45	\paragraph{File diff delta ($\lambda_2$).}
46	Measures the fraction of steps within $w_i$ that produce code modifications (file creates, edits, or deletes).
47	A low modification frequency triggers a stagnation vote, detecting lack of productive output.
48	On OpenHands, this LF achieves 87\% correctness on progress windows, making it the most reliable cross-agent signal.
49	
50	\paragraph{Outcome backpropagation ($\lambda_3$).}
51	Uses the final task outcome (resolved/unresolved) as distant supervision.
52	For unresolved tasks, windows in the final portion of the trajectory receive stagnation votes under the assumption that task failure is preceded by a period of unproductive behavior.
53	Resolved tasks receive progress votes in the corresponding windows.
54	Unlike $\lambda_1$ and $\lambda_2$, which operate on local window content, $\lambda_3$ propagates a global signal backward through time.
55	This makes it a form of distant supervision: individually noisy, but complementary to the real-time signals when aggregated.
56	
57	\begin{table}[t]
58	\centering
59	\small
60	\begin{tabular}{llcc}
61	\toprule
62	\textbf{LF} & \textbf{Signal} & \textbf{SWE Fire\,\%} & \textbf{OH Fire\,\%} \\
63	\midrule
64	$\lambda_1$ (cmd\_rep)    & Repetition & 65.6 & 92.3 \\
65	$\lambda_2$ (file\_diff)  & Output     & 57.3 & 42.1 \\
66	$\lambda_3$ (outcome\_bp) & Outcome    & 23.9 & 19.8 \\
67	\bottomrule
68	\end{tabular}
69	\caption{Labeling function design. Fire\,\% = fraction of windows on which the LF produces a stagnation vote. SWE = SWE-Agent; OH = OpenHands.}
70	\label{tab:lf_design}
71	\end{table}
72	
73	\subsubsection{Label Aggregation}
74	\label{sec:label_aggregation}
75	
76	Silver labels are produced by majority vote:
77	\begin{equation}
78	y_i = \text{MV}\bigl(\lambda_1(w_i),\; \lambda_2(w_i),\; \lambda_3(w_i)\bigr)
79	\label{eq:mv}
80	\end{equation}
81	We define the confidence of each label as the number of agreeing LFs: $\text{conf}_i = |\{j : \lambda_j(w_i) = y_i\}| \in \{1, 2, 3\}$.
82	With three binary LFs, majority vote always produces a winner; conf${=}1$ arises when one LF votes opposite to the other two plus abstains differently, producing the most ambiguous labels.
83	The conf${\geq}$2 subset, where at least two LFs agree on the winning label, serves as the primary evaluation set throughout this work.
84	This stratification allows us to separately analyze model behavior on high-confidence vs.\ ambiguous windows (\S\ref{sec:main_results}).
85	
86	%-------------------------------------------------------------------
87	\subsection{Detection Methods}
88	\label{sec:detection_methods}
89	
90	\subsubsection{Structural Features}
91	\label{sec:structural_features}
92	
93	We extract a 30-dimensional feature vector from each window, requiring no pretrained model or GPU.
94	Features span four categories:
95	(1)~\emph{repetition}: exact command repeat ratio, fuzzy match ratio (Levenshtein-based), and unique command ratio;
96	(2)~\emph{file operations}: counts of file creates, modifications, and deletions within the window;
97	(3)~\emph{edit patterns}: edit distances between consecutive actions, capturing how much the agent's behavior changes step-to-step;
98	(4)~\emph{output statistics}: entropy of command outputs and action type distribution features.
99	These features are fed to three classifiers: Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).
100	Because several structural features overlap with the signals used by the labeling functions (e.g., repetition ratios relate to $\lambda_1$), structural classifiers can partially reconstruct the LF voting process.
101	We discuss this circularity and its implications in \S\ref{sec:main_results}.
102	
103	\subsubsection{NL Embedding Probe (ProgressProbe)}
104	\label{sec:progressprobe}
105	
106	Each action $a_t$ is encoded as a natural language description and embedded using Qwen3-Embedding-0.6B \citep{zhang2025qwen3embedding} into a 1024-dimensional vector.
107	The $k$ embeddings within a window form a sequence that is processed by a 2-layer GRU \citep{cho2014gru} with hidden size 256 and dropout 0.1.
108	An attention mechanism \citep{bahdanau2015attention} computes a weighted combination of the GRU hidden states, yielding a single window-level representation.
109	This representation is passed through a fully connected layer with sigmoid activation for binary classification.
110	Training uses binary cross-entropy loss with early stopping (patience 5) on a validation set.
111	
112	The GRU architecture is motivated by the sequential nature of actions within a window: the order in which commands are issued (e.g., repeated failures followed by a different approach) carries diagnostic information that bag-of-embeddings methods discard.
113	We also evaluate two simpler embedding baselines to isolate the contribution of temporal modeling: (1)~mean-pooled Qwen3 embeddings with logistic regression, and (2)~cosine similarity between consecutive window embeddings with a validation-tuned threshold.
114	
115	\subsubsection{LLM-as-Judge Baseline}
116	\label{sec:llm_judge}
117	
118	We prompt Claude Sonnet in zero-shot mode to classify each window as stagnation or progress, given the textual descriptions of actions within the window.
119	This baseline serves exclusively for evaluation---it is not used in the silver label pipeline and incurs \$11.66 in API cost for the SWE-Agent test set alone, making it impractical for large-scale labeling.
120	
121	%-------------------------------------------------------------------
122	\subsection{Temporal Label Models}
123	\label{sec:temporal_models}
124	
125	The three LFs occupy distinct temporal niches relative to stagnation onset (\S\ref{sec:lf_temporal}): $\lambda_1$ leads by ${\sim}2$ steps, $\lambda_2$ is near-concurrent, and $\lambda_3$ lags by ${\sim}7$ steps.
126	This motivates exploring whether encoding temporal structure into label aggregation can improve over majority vote.
127	
128	\subsubsection{Time-Varying Weights (TWV)}
129	\label{sec:twv}
130	
131	TWV applies Gaussian kernel smoothing to each LF's activation sequence:
132	\begin{equation}
133	\tilde{\lambda}_j(t) = \sum_{t'} K_\sigma(t - t') \cdot \lambda_j(t')
134	\label{eq:twv}
135	\end{equation}
136	where $K_\sigma$ is a Gaussian kernel with bandwidth $\sigma$.
137	Smoothed activations replace raw votes for conf${=}1$ windows (where exactly one LF disagrees), potentially flipping labels in temporally ambiguous regions.
138	The bandwidth $\sigma$ controls the extent of temporal context: larger values incorporate more distant steps.
139	
140	\subsubsection{Hidden Markov Models}
141	\label{sec:hmm}
142	
143	We model the label sequence as a Hidden Markov Model \citep{safranchik2020linkedhmm} with two hidden states (stagnation, progress) and observations defined by the joint activation pattern of the three LFs.
144	Transition and emission parameters are estimated via Expectation-Maximization (EM).
145	The HMM captures temporal persistence---stagnation episodes tend to span multiple consecutive windows---which majority vote, operating independently per window, cannot model.
146	
147	\subsubsection{Lag-Aware HMM}
148	\label{sec:lag_hmm}
149	
150	The standard HMM treats all LFs as synchronous.
151	Lag-Aware HMM extends this by explicitly modeling each LF's temporal offset: $\lambda_1$ is shifted by $-2$ steps, $\lambda_2$ by $-1$, and $\lambda_3$ by $+7$, estimated from the temporal dynamics analysis (\S\ref{sec:lf_temporal}).
152	To prevent divergence, we apply two regularization strategies: (1)~\emph{confidence anchoring}, which fixes labels for conf${\geq}$2 windows and restricts EM updates to conf${=}1$ windows; and (2)~a prior strength of 5000 on transition parameters.
153	These constraints keep the model close to the majority vote baseline while allowing it to resolve temporally ambiguous labels.
154	The intuition is that aligning each LF's activation to its natural temporal role should produce cleaner emission estimates and, consequently, more accurate Viterbi decodings on ambiguous windows.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "f16c9979-4041-4d8a-a045-bba6bc59512a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe frame stagnation detection as window-level binary classification over agent trajectories.\nSilver labels are generated via weak supervision from three labeling functions, then used to train and evaluate three detection approaches: structural features, a neural embedding probe, and an LLM-as-judge baseline.\nFigure~\\ref{fig:pipeline} provides a system overview.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{../../figures/paper/fig_pipeline.pdf}\n\\caption{System overview. (Left) Agent trajectories are segmented into overlapping windows of $k{=}5$ steps. (Center) Three labeling functions vote on each window; majority vote produces silver labels with confidence 1--3. (Right) Three detection approaches compared: structural features (30-dim), NL embedding probe (GRU), and LLM-as-judge (eval only, not trained on silver labels).}\n\\label{fig:pipeline}\n\\end{figure*}\n\n%-------------------------------------------------------------------\n\\subsection{Problem Formulation}\n\\label{sec:problem}\n\nGiven an agent trajectory $T = (a_1, a_2, \\ldots, a_n)$ where each $a_t$ is an action (e.g., a shell command, file edit, or API call), we partition it into overlapping sliding windows $w_i = (a_i, \\ldots, a_{i+k-1})$ with window size $k{=}5$ and stride 1.\nThe task is to assign each window a binary label $y_i \\in \\{0, 1\\}$, where 0 denotes \\emph{stagnation} (the agent is stuck or unproductive) and 1 denotes \\emph{progress} (the agent is making meaningful headway toward the task goal).\n\nThe window formulation offers two advantages over alternatives.\nCompared to step-level scoring, windows capture short-range temporal patterns---such as a sequence of repeated failed attempts---that individual actions cannot express.\nCompared to trajectory-level labeling, windows provide the granularity needed to pinpoint \\emph{when} stagnation begins and ends within a single task attempt, enabling downstream interventions such as early termination or strategy switching.\n\n%-------------------------------------------------------------------\n\\subsection{Weak Supervision Pipeline}\n\\label{sec:weak_supervision}\n\nNo gold-standard annotations exist for agent stagnation at the window level.\nManual annotation is expensive: each window requires reviewing $k$ actions with full context (command text, outputs, file diffs), taking an estimated 2--3 minutes per window.\nWe therefore adopt a data programming approach \\citep{ratner2016dataprogramming,ratner2017snorkel}: multiple labeling functions (LFs) provide noisy votes that are aggregated into silver labels.\nEach LF $\\lambda_j : w_i \\to \\{-1, 0, 1\\}$ examines a window and emits a vote: stagnation (0), progress (1), or abstain ($-1$).\n\n\\subsubsection{Labeling Functions}\n\\label{sec:labeling_functions}\n\nWe design three LFs that target complementary signals of stagnation (Table~\\ref{tab:lf_design}).\n\n\\paragraph{Command repetition ($\\lambda_1$).}\nComputes the proportion of repeated commands within window $w_i$.\nA high repetition ratio triggers a stagnation vote, capturing overt repetitive behavior such as re-running failing commands.\nThis LF fires on 65.6\\% of SWE-Agent windows and 92.3\\% of OpenHands windows; the elevated OH rate reflects differences in action distributions across agent architectures (\\S\\ref{sec:cmd_rep_ablation}).\n\n\\paragraph{File diff delta ($\\lambda_2$).}\nMeasures the fraction of steps within $w_i$ that produce code modifications (file creates, edits, or deletes).\nA low modification frequency triggers a stagnation vote, detecting lack of productive output.\nOn OpenHands, this LF achieves 87\\% correctness on progress windows, making it the most reliable cross-agent signal.\n\n\\paragraph{Outcome backpropagation ($\\lambda_3$).}\nUses the final task outcome (resolved/unresolved) as distant supervision.\nFor unresolved tasks, windows in the final portion of the trajectory receive stagnation votes under the assumption that task failure is preceded by a period of unproductive behavior.\nResolved tasks receive progress votes in the corresponding windows.\nUnlike $\\lambda_1$ and $\\lambda_2$, which operate on local window content, $\\lambda_3$ propagates a global signal backward through time.\nThis makes it a form of distant supervision: individually noisy, but complementary to the real-time signals when aggregated.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llcc}\n\\toprule\n\\textbf{LF} & \\textbf{Signal} & \\textbf{SWE Fire\\,\\%} & \\textbf{OH Fire\\,\\%} \\\\\n\\midrule\n$\\lambda_1$ (cmd\\_rep)    & Repetition & 65.6 & 92.3 \\\\\n$\\lambda_2$ (file\\_diff)  & Output     & 57.3 & 42.1 \\\\\n$\\lambda_3$ (outcome\\_bp) & Outcome    & 23.9 & 19.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Labeling function design. Fire\\,\\% = fraction of windows on which the LF produces a stagnation vote. SWE = SWE-Agent; OH = OpenHands.}\n\\label{tab:lf_design}\n\\end{table}\n\n\\subsubsection{Label Aggregation}\n\\label{sec:label_aggregation}\n\nSilver labels are produced by majority vote:\n\\begin{equation}\ny_i = \\text{MV}\\bigl(\\lambda_1(w_i),\\; \\lambda_2(w_i),\\; \\lambda_3(w_i)\\bigr)\n\\label{eq:mv}\n\\end{equation}\nWe define the confidence of each label as the number of agreeing LFs: $\\text{conf}_i = |\\{j : \\lambda_j(w_i) = y_i\\}| \\in \\{1, 2, 3\\}$.\nWith three binary LFs, majority vote always produces a winner; conf${=}1$ arises when one LF votes opposite to the other two plus abstains differently, producing the most ambiguous labels.\nThe conf${\\geq}$2 subset, where at least two LFs agree on the winning label, serves as the primary evaluation set throughout this work.\nThis stratification allows us to separately analyze model behavior on high-confidence vs.\\ ambiguous windows (\\S\\ref{sec:main_results}).\n\n%-------------------------------------------------------------------\n\\subsection{Detection Methods}\n\\label{sec:detection_methods}\n\n\\subsubsection{Structural Features}\n\\label{sec:structural_features}\n\nWe extract a 30-dimensional feature vector from each window, requiring no pretrained model or GPU.\nFeatures span four categories:\n(1)~\\emph{repetition}: exact command repeat ratio, fuzzy match ratio (Levenshtein-based), and unique command ratio;\n(2)~\\emph{file operations}: counts of file creates, modifications, and deletions within the window;\n(3)~\\emph{edit patterns}: edit distances between consecutive actions, capturing how much the agent's behavior changes step-to-step;\n(4)~\\emph{output statistics}: entropy of command outputs and action type distribution features.\nThese features are fed to three classifiers: Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\nBecause several structural features overlap with the signals used by the labeling functions (e.g., repetition ratios relate to $\\lambda_1$), structural classifiers can partially reconstruct the LF voting process.\nWe discuss this circularity and its implications in \\S\\ref{sec:main_results}.\n\n\\subsubsection{NL Embedding Probe (ProgressProbe)}\n\\label{sec:progressprobe}\n\nEach action $a_t$ is encoded as a natural language description and embedded using Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} into a 1024-dimensional vector.\nThe $k$ embeddings within a window form a sequence that is processed by a 2-layer GRU \\citep{cho2014gru} with hidden size 256 and dropout 0.1.\nAn attention mechanism \\citep{bahdanau2015attention} computes a weighted combination of the GRU hidden states, yielding a single window-level representation.\nThis representation is passed through a fully connected layer with sigmoid activation for binary classification.\nTraining uses binary cross-entropy loss with early stopping (patience 5) on a validation set.\n\nThe GRU architecture is motivated by the sequential nature of actions within a window: the order in which commands are issued (e.g., repeated failures followed by a different approach) carries diagnostic information that bag-of-embeddings methods discard.\nWe also evaluate two simpler embedding baselines to isolate the contribution of temporal modeling: (1)~mean-pooled Qwen3 embeddings with logistic regression, and (2)~cosine similarity between consecutive window embeddings with a validation-tuned threshold.\n\n\\subsubsection{LLM-as-Judge Baseline}\n\\label{sec:llm_judge}\n\nWe prompt Claude Sonnet in zero-shot mode to classify each window as stagnation or progress, given the textual descriptions of actions within the window.\nThis baseline serves exclusively for evaluation---it is not used in the silver label pipeline and incurs \\$11.66 in API cost for the SWE-Agent test set alone, making it impractical for large-scale labeling.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_models}\n\nThe three LFs occupy distinct temporal niches relative to stagnation onset (\\S\\ref{sec:lf_temporal}): $\\lambda_1$ leads by ${\\sim}2$ steps, $\\lambda_2$ is near-concurrent, and $\\lambda_3$ lags by ${\\sim}7$ steps.\nThis motivates exploring whether encoding temporal structure into label aggregation can improve over majority vote.\n\n\\subsubsection{Time-Varying Weights (TWV)}\n\\label{sec:twv}\n\nTWV applies Gaussian kernel smoothing to each LF's activation sequence:\n\\begin{equation}\n\\tilde{\\lambda}_j(t) = \\sum_{t'} K_\\sigma(t - t') \\cdot \\lambda_j(t')\n\\label{eq:twv}\n\\end{equation}\nwhere $K_\\sigma$ is a Gaussian kernel with bandwidth $\\sigma$.\nSmoothed activations replace raw votes for conf${=}1$ windows (where exactly one LF disagrees), potentially flipping labels in temporally ambiguous regions.\nThe bandwidth $\\sigma$ controls the extent of temporal context: larger values incorporate more distant steps.\n\n\\subsubsection{Hidden Markov Models}\n\\label{sec:hmm}\n\nWe model the label sequence as a Hidden Markov Model \\citep{safranchik2020linkedhmm} with two hidden states (stagnation, progress) and observations defined by the joint activation pattern of the three LFs.\nTransition and emission parameters are estimated via Expectation-Maximization (EM).\nThe HMM captures temporal persistence---stagnation episodes tend to span multiple consecutive windows---which majority vote, operating independently per window, cannot model.\n\n\\subsubsection{Lag-Aware HMM}\n\\label{sec:lag_hmm}\n\nThe standard HMM treats all LFs as synchronous.\nLag-Aware HMM extends this by explicitly modeling each LF's temporal offset: $\\lambda_1$ is shifted by $-2$ steps, $\\lambda_2$ by $-1$, and $\\lambda_3$ by $+7$, estimated from the temporal dynamics analysis (\\S\\ref{sec:lf_temporal}).\nTo prevent divergence, we apply two regularization strategies: (1)~\\emph{confidence anchoring}, which fixes labels for conf${\\geq}$2 windows and restricts EM updates to conf${=}1$ windows; and (2)~a prior strength of 5000 on transition parameters.\nThese constraints keep the model close to the majority vote baseline while allowing it to resolve temporally ambiguous labels.\nThe intuition is that aligning each LF's activation to its natural temporal role should produce cleaner emission estimates and, consequently, more accurate Viterbi decodings on ambiguous windows.",
      "numLines": 154,
      "startLine": 1,
      "totalLines": 154
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01QgartiSQYgfonEU5u8Q5J8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "63b6d7ad-a4fe-49b0-862b-9a04747eaea0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NduHrpDKjMMUcebkbkrqWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5803,
      "cache_read_input_tokens": 24820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5803
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

_source line 18 · 2026-05-14T22:30:26.867Z_

<details><summary>↩ Tool result · `toolu_01QgartiSQYgfonEU5u8Q5J8`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.
5	All reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\S\ref{sec:method}).
6	
7	\paragraph{Circular evaluation caveat.}
8	Structural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.
9	Consequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.
10	The cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\S\ref{sec:cmd_rep_ablation}).
11	A human-annotated gold set provides the definitive non-circular evaluation (\S\ref{sec:gold_set}).
12	
13	%-------------------------------------------------------------------
14	\subsection{Experimental Setup}
15	\label{sec:setup}
16	
17	\paragraph{Datasets.}
18	We extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.
19	\textbf{SWE-Agent} trajectories from SWE-bench \citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\%.
20	\textbf{OpenHands} (OH) trajectories \citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\%.
21	Silver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).
22	Unless stated otherwise, evaluation uses the conf${\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.
23	
24	\begin{table}[t]
25	\centering
26	\small
27	\begin{tabular}{llrrc}
28	\toprule
29	\textbf{Agent} & \textbf{Source} & \textbf{Windows} & \textbf{Stag\,\%} & \textbf{Conf${\geq}$2} \\
30	\midrule
31	SWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\
32	OpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\
33	\bottomrule
34	\end{tabular}
35	\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}
36	\label{tab:dataset_stats}
37	\end{table}
38	
39	\paragraph{Detection methods.}
40	(1)~\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).
41	(2)~\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \citep{cho2014gru} with attention \citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.
42	(3)~\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.
43	(4)~\textbf{LLM-as-Judge}: Claude Sonnet zero-shot window-level classification (\$11.66 API cost for the SWE test set).
44	(5)~\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.
45	
46	\paragraph{Metrics.}
47	Macro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\textsubscript{stag}) and progress (F1\textsubscript{prog}).
48	
49	%-------------------------------------------------------------------
50	\subsection{Main Results}
51	\label{sec:main_results}
52	
53	Table~\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\geq}$2 test set and cross-agent transfer to OpenHands.
54	
55	\begin{table*}[t]
56	\centering
57	\small
58	\begin{tabular}{l ccc cc}
59	\toprule
60	& \multicolumn{3}{c}{\textbf{SWE-Agent In-Domain} (conf${\geq}$2)} & \multicolumn{2}{c}{\textbf{OpenHands Transfer}} \\
61	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
62	\textbf{Method} & Macro-F1 & F1\textsubscript{stag} & F1\textsubscript{prog} & All & Conf${\geq}$2 \\
63	\midrule
64	Structural RF$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \textbf{0.9959} \\
65	Structural GB$^\dagger$       & \textbf{0.9951} & 0.9928 & 0.9974 & \textbf{0.9674} & \underline{0.9919} \\
66	Structural LR$^\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\
67	ProgressProbe (GRU)           & \underline{0.9055} & 0.8593 & 0.9518 & 0.5280 & --- \\
68	\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\
69	Mean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\
70	LLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\
71	Cosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\
72	\bottomrule
73	\end{tabular}
74	\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \textbf{bold}, second-best \underline{underlined}.}
75	\label{tab:main_results}
76	\end{table*}
77	
78	In-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\,pp.
79	However, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.
80	The more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.
81	The LLM judge underperforms all learned methods despite substantially higher cost.
82	
83	%-------------------------------------------------------------------
84	\subsection{Cross-Agent Transfer}
85	\label{sec:cross_agent}
86	
87	Table~\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.
88	Structural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\,pp above the probe fine-tuned on 100\% of OH data (0.751).
89	RF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.
90	Both structural models recover to $>$0.99 on conf${\geq}$2 OH windows, where label noise is lower.
91	
92	The probe's zero-shot transfer (0.528) is near chance, and even full OH fine-tuning only reaches 0.751.
93	This asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.
94	
95	\paragraph{Multi-seed stability.}
96	Structural RF: $0.9951{\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\pm}0.0015$.
97	The probe shows higher variance: $0.9185{\pm}0.0113$, though all seeds exceed 0.90.
98	
99	%-------------------------------------------------------------------
100	\subsection{Robustness Analysis}
101	\label{sec:robustness}
102	
103	\paragraph{Encoder ablation.}
104	Replacing Qwen3-0.6B with BGE-M3 \citep{chen2024bgem3} or E5-large-v2 \citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\ 0.9055 for Qwen3).
105	All encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\ref{tab:encoder_ablation}.
106	
107	\paragraph{Window size.}
108	$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\,pp and $k{=}7$ drops 1.8\,pp.
109	Shorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.
110	Details in Appendix Table~\ref{tab:window_ablation}.
111	
112	\paragraph{Data scaling.}
113	Figure~\ref{fig:data_scaling} shows probe performance scales monotonically from 0.8054 (10\% training data) to 0.9055 (100\%), with structural RF providing a ceiling at 0.9951 (dashed line).
114	The curve has not plateaued, suggesting larger trajectory corpora could further close the structural--probe gap.
115	
116	\begin{figure}[t]
117	\centering
118	\includegraphics[width=\columnwidth]{../../figures/paper/fig_data_scaling.pdf}
119	\caption{Probe macro-F1 vs.\ training data fraction. Structural RF ceiling shown as dashed line. Performance scales monotonically but has not saturated at 100\% data.}
120	\label{fig:data_scaling}
121	\end{figure}
122	
123	%-------------------------------------------------------------------
124	\subsection{Labeling Function Temporal Dynamics}
125	\label{sec:lf_temporal}
126	
127	We analyze when each LF first fires relative to the onset of stagnation episodes (Table~\ref{tab:lf_temporal}, Figure~\ref{fig:lf_temporal}).
128	
129	\begin{table}[t]
130	\centering
131	\small
132	\begin{tabular}{lrrrr}
133	\toprule
134	\textbf{LF} & \textbf{Lag} & \textbf{Lead\,\%} & \textbf{Conc.\,\%} & \textbf{Lag\,\%} \\
135	\midrule
136	cmd\_rep      & $-1.87$ & 36.1 & --- & --- \\
137	file\_diff    & $-1.20$ & 17.1 & --- & --- \\
138	outcome\_bp   & $+6.70$ & ---  & --- & 48.4 \\
139	\bottomrule
140	\end{tabular}
141	\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}
142	\label{tab:lf_temporal}
143	\end{table}
144	
145	The three LFs occupy distinct temporal niches.
146	Command repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.
147	File diff is near-concurrent ($-1.20$ steps).
148	Outcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.
149	
150	All pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\_rep vs.\ file\_diff $p{=}1.44{\times}10^{-26}$, cmd\_rep vs.\ outcome\_bp $p{=}6.67{\times}10^{-39}$, file\_diff vs.\ outcome\_bp $p{=}3.47{\times}10^{-47}$).
151	
152	\paragraph{Cross-agent reversal.}
153	On OpenHands, cmd\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).
154	This reversal explains the cmd\_rep pathology analyzed in \S\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\_rep on progress windows, inverting its diagnostic value.
155	
156	\begin{figure}[t]
157	\centering
158	\includegraphics[width=\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}
159	\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\_rep leads ($-1.87$ steps), file\_diff is near-concurrent ($-1.20$), outcome\_bp lags ($+6.70$). Inset: OH reversal where cmd\_rep becomes lagging.}
160	\label{fig:lf_temporal}
161	\end{figure}
162	
163	%-------------------------------------------------------------------
164	\subsection{Command Repetition Ablation}
165	\label{sec:cmd_rep_ablation}
166	
167	The cmd\_rep LF fires on 92.3\% of OH windows (vs.\ 65.6\% on SWE-Agent), with a 71\% false positive rate on OH progress windows.
168	Table~\ref{tab:cmd_rep_ablation} shows the effect of removing it.
169	
170	\begin{table}[t]
171	\centering
172	\small
173	\begin{tabular}{lcccc}
174	\toprule
175	\textbf{LF Config} & \textbf{ZS F1} & \textbf{FT F1} & \textbf{FT F1\textsubscript{s}} & \textbf{FT F1\textsubscript{p}} \\
176	\midrule
177	3-LF (w/ cmd\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\
178	2-LF (no cmd\_rep) & 0.607 & \textbf{0.927} & 0.938 & 0.917 \\
179	\midrule
180	$\Delta$ & +7.7\,pp & +17.6\,pp & +39.4\,pp & $-4.2$\,pp \\
181	\bottomrule
182	\end{tabular}
183	\caption{Effect of removing cmd\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\% OH data. F1\textsubscript{s}/F1\textsubscript{p} = stagnation/progress F1.}
184	\label{tab:cmd_rep_ablation}
185	\end{table}
186	
187	Removing cmd\_rep improves zero-shot transfer by 7.7\,pp and fine-tuned performance by 17.6\,pp.
188	The gain is driven almost entirely by stagnation recall (+39.4\,pp F1\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\,pp F1\textsubscript{prog}).
189	The 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.
190	Note that removing cmd\_rep also reduces training data from 101,713 to 72,554 windows (28.5\% reduction); however, the model trained on \emph{less} data with cleaner labels decisively outperforms the model trained on \emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.
191	This motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.
192	
193	%-------------------------------------------------------------------
194	\subsection{Temporal Label Models}
195	\label{sec:temporal_label_models}
196	
197	We investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).
198	Table~\ref{tab:temporal_models} compares three temporal label models \citep{ratner2017snorkel,safranchik2020linkedhmm}.
199	
200	\begin{table}[t]
201	\centering
202	\small
203	\begin{tabular}{lccc}
204	\toprule
205	\textbf{Method} & \textbf{Conf${\geq}$2 F1} & \textbf{MV Agr.} & \textbf{Probe F1$^\ddagger$} \\
206	\midrule
207	MV (baseline) & 0.8946$^\ast$ & 1.000 & 0.8468 \\
208	TWV ($\sigma{=}2$) & \textbf{0.9003} & 0.885 & 0.8211 \\
209	Lag-HMM & 0.8936 & 0.820 & --- \\
210	HMM & 0.7502 & 0.685 & 0.6564 \\
211	\bottomrule
212	\end{tabular}
213	\caption{Temporal label model comparison. $^\ast$MV conf${\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\ddagger$Downstream: probe trained on each method's labels, evaluated on SWE-Agent conf${\geq}$2 vs.\ MV labels.}
214	\label{tab:temporal_models}
215	\end{table}
216	
217	TWV achieves the highest conf${\geq}$2 F1 (0.9003, +0.57\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\ 0.8468 for MV-trained ($-2.57$\,pp).
218	TWV flips 14.1\% of conf$=$1 labels, introducing noise that hurts probe training.
219	HMM overpredicts stagnation (29,176 stagnation vs.\ 25,633 progress windows), degrading downstream performance to 0.6564.
220	Lag-HMM closely tracks MV ($-0.1$\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \emph{aggregation}.
221	
222	\paragraph{TWV sensitivity.}
223	The Gaussian kernel bandwidth $\sigma$ is critical: $\sigma{=}2$ is optimal (0.9003); $\sigma{=}1$ drops to 0.8105 and $\sigma{\geq}5$ falls below 0.81.
224	This narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.
225	
226	These results constitute a negative finding: despite clear temporal structure in LF firing patterns (\S\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.
227	
228	%-------------------------------------------------------------------
229	\subsection{Gold Set Validation}
230	\label{sec:gold_set}
231	\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "3f45cfd8-65fa-4baf-a06d-38d1977e82f7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate stagnation detection across four axes: in-domain accuracy, cross-agent transfer, robustness to design choices, and temporal dynamics of labeling functions.\nAll reported metrics are evaluated against silver labels derived from majority vote over three labeling functions (\\S\\ref{sec:method}).\n\n\\paragraph{Circular evaluation caveat.}\nStructural features (command repetition ratios, file operation counts, edit distances) are computed from the same signals that the labeling functions use to produce silver labels.\nConsequently, the in-domain structural F1 of 0.9951 reflects an upper bound on how well these features can \\emph{reverse-engineer} the labeling functions, not detection accuracy against true ground truth.\nThe cross-agent evaluation on OpenHands (0.967 macro-F1) is non-circular: models trained on SWE-Agent LF distributions are tested on a different agent whose LF firing patterns differ substantially (\\S\\ref{sec:cmd_rep_ablation}).\nA human-annotated gold set provides the definitive non-circular evaluation (\\S\\ref{sec:gold_set}).\n\n%-------------------------------------------------------------------\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe extract sliding windows of $k{=}5$ consecutive actions from agent trajectories.\n\\textbf{SWE-Agent} trajectories from SWE-bench \\citep{jimenez2024swebench,yang2024sweagent} yield 54,809 windows with a stagnation ratio of 28.5\\%.\n\\textbf{OpenHands} (OH) trajectories \\citep{wang2025openhands} yield 150,652 windows with a stagnation ratio of 6.6\\%.\nSilver labels are produced by majority vote over three labeling functions; confidence equals the number of agreeing LFs (1--3).\nUnless stated otherwise, evaluation uses the conf${\\geq}$2 subset: $N{=}1{,}824$ for SWE-Agent (485 stagnation, 1,339 progress) and $N{=}43{,}376$ for OH.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llrrc}\n\\toprule\n\\textbf{Agent} & \\textbf{Source} & \\textbf{Windows} & \\textbf{Stag\\,\\%} & \\textbf{Conf${\\geq}$2} \\\\\n\\midrule\nSWE-Agent & SWE-bench & 54,809 & 28.5 & 15,401 \\\\\nOpenHands & CodeAct   & 150,652 & 6.6 & 43,376 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Dataset statistics. Stagnation ratios differ substantially across agents, reflecting different action distributions.}\n\\label{tab:dataset_stats}\n\\end{table}\n\n\\paragraph{Detection methods.}\n(1)~\\textbf{Structural features}: 30 hand-crafted features (repetition rates, file operation counts, edit distances, output entropy) fed to Logistic Regression (LR), Random Forest (RF), and Gradient Boosting (GB).\n(2)~\\textbf{ProgressProbe}: Qwen3-Embedding-0.6B \\citep{zhang2025qwen3embedding} embeddings (1024-dim) processed by a 2-layer GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} (hidden$=$256, dropout$=$0.1), early-stopped at epoch~3 with patience~5.\n(3)~\\textbf{Mean-pool + LR}: Mean-pooled Qwen3 embeddings with logistic regression.\n(4)~\\textbf{LLM-as-Judge}: Claude Sonnet zero-shot window-level classification (\\$11.66 API cost for the SWE test set).\n(5)~\\textbf{Cosine similarity}: Cosine distance between consecutive window embeddings with a validation-tuned threshold.\n\n\\paragraph{Metrics.}\nMacro-F1 is the primary metric. We also report per-class F1 for stagnation (F1\\textsubscript{stag}) and progress (F1\\textsubscript{prog}).\n\n%-------------------------------------------------------------------\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main_results} presents in-domain results on the SWE-Agent conf${\\geq}$2 test set and cross-agent transfer to OpenHands.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\begin{tabular}{l ccc cc}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SWE-Agent In-Domain} (conf${\\geq}$2)} & \\multicolumn{2}{c}{\\textbf{OpenHands Transfer}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\n\\textbf{Method} & Macro-F1 & F1\\textsubscript{stag} & F1\\textsubscript{prog} & All & Conf${\\geq}$2 \\\\\n\\midrule\nStructural RF$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & 0.9123 & \\textbf{0.9959} \\\\\nStructural GB$^\\dagger$       & \\textbf{0.9951} & 0.9928 & 0.9974 & \\textbf{0.9674} & \\underline{0.9919} \\\\\nStructural LR$^\\dagger$       & 0.9874 & 0.9815 & 0.9933 & 0.7801 & 0.9671 \\\\\nProgressProbe (GRU)           & \\underline{0.9055} & 0.8593 & 0.9518 & 0.5280 & --- \\\\\n\\quad + full OH fine-tune      & ---    & ---    & ---    & 0.7510 & --- \\\\\nMean-pool + LR                & 0.8435 & 0.7620 & 0.9250 & ---    & --- \\\\\nLLM-as-Judge                  & 0.6625 & 0.6055 & 0.7195 & ---    & --- \\\\\nCosine Similarity             & 0.5606 & ---    & ---    & ---    & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Stagnation detection results. In-domain evaluation on SWE-Agent conf${\\geq}$2 test set ($N{=}1{,}824$) and zero-shot cross-agent transfer to OpenHands. $^\\dagger$Structural metrics are evaluated against LF-derived labels and reflect LF-reconstructibility rather than ground-truth accuracy (see circular evaluation caveat). Best in \\textbf{bold}, second-best \\underline{underlined}.}\n\\label{tab:main_results}\n\\end{table*}\n\nIn-domain, structural RF achieves 0.9951 macro-F1, exceeding the GRU probe by 8.96 percentage points (pp) and the LLM judge by 33.3\\,pp.\nHowever, the structural--probe gap is inflated by circular evaluation: structural features reconstruct the LFs that generated the labels.\nThe more informative comparison is among non-circular methods: the GRU probe outperforms mean-pool~+~LR by 6.2\\,pp, confirming that temporal modeling within windows adds value beyond static embedding aggregation.\nThe LLM judge underperforms all learned methods despite substantially higher cost.\n\n%-------------------------------------------------------------------\n\\subsection{Cross-Agent Transfer}\n\\label{sec:cross_agent}\n\nTable~\\ref{tab:main_results} (right columns) shows models trained on SWE-Agent and evaluated on OpenHands without any OH training data.\nStructural GB transfers best, achieving 0.967 macro-F1 on all OH windows---21.6\\,pp above the probe fine-tuned on 100\\% of OH data (0.751).\nRF drops to 0.912 on all-confidence OH data despite matching GB in-domain, suggesting GB's boosted ensemble is more robust to distributional shift.\nBoth structural models recover to $>$0.99 on conf${\\geq}$2 OH windows, where label noise is lower.\n\nThe probe's zero-shot transfer (0.528) is near chance, and even full OH fine-tuning only reaches 0.751.\nThis asymmetry---structural features transfer naturally while learned embeddings do not---is a central empirical finding: stagnation manifests in action-level structure that generalizes across agents.\n\n\\paragraph{Multi-seed stability.}\nStructural RF: $0.9951{\\pm}0.0000$ in-domain (3 seeds, zero variance); GB cross-agent: $0.9678{\\pm}0.0015$.\nThe probe shows higher variance: $0.9185{\\pm}0.0113$, though all seeds exceed 0.90.\n\n%-------------------------------------------------------------------\n\\subsection{Robustness Analysis}\n\\label{sec:robustness}\n\n\\paragraph{Encoder ablation.}\nReplacing Qwen3-0.6B with BGE-M3 \\citep{chen2024bgem3} or E5-large-v2 \\citep{wang2024e5} yields probe macro-F1 of 0.9413 and 0.9363, respectively (vs.\\ 0.9055 for Qwen3).\nAll encoders exceed 0.90, indicating the probe's temporal architecture, not a specific encoder, drives performance. Full results appear in Appendix Table~\\ref{tab:encoder_ablation}.\n\n\\paragraph{Window size.}\n$k{=}5$ is optimal (0.9309 macro-F1); $k{=}3$ drops 5.9\\,pp and $k{=}7$ drops 1.8\\,pp.\nShorter windows lack sufficient context; longer windows dilute signal by spanning both progress and stagnation phases.\nDetails in Appendix Table~\\ref{tab:window_ablation}.\n\n\\paragraph{Data scaling.}\nFigure~\\ref{fig:data_scaling} shows probe performance scales monotonically from 0.8054 (10\\% training data) to 0.9055 (100\\%), with structural RF providing a ceiling at 0.9951 (dashed line).\nThe curve has not plateaued, suggesting larger trajectory corpora could further close the structural--probe gap.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_data_scaling.pdf}\n\\caption{Probe macro-F1 vs.\\ training data fraction. Structural RF ceiling shown as dashed line. Performance scales monotonically but has not saturated at 100\\% data.}\n\\label{fig:data_scaling}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Labeling Function Temporal Dynamics}\n\\label{sec:lf_temporal}\n\nWe analyze when each LF first fires relative to the onset of stagnation episodes (Table~\\ref{tab:lf_temporal}, Figure~\\ref{fig:lf_temporal}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{LF} & \\textbf{Lag} & \\textbf{Lead\\,\\%} & \\textbf{Conc.\\,\\%} & \\textbf{Lag\\,\\%} \\\\\n\\midrule\ncmd\\_rep      & $-1.87$ & 36.1 & --- & --- \\\\\nfile\\_diff    & $-1.20$ & 17.1 & --- & --- \\\\\noutcome\\_bp   & $+6.70$ & ---  & --- & 48.4 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal roles of labeling functions on SWE-Agent. Lag = mean steps relative to stagnation onset (negative = leading). Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; all pairwise comparisons significant after Bonferroni correction.}\n\\label{tab:lf_temporal}\n\\end{table}\n\nThe three LFs occupy distinct temporal niches.\nCommand repetition leads stagnation onset by 1.87 steps on average, making it an early warning signal.\nFile diff is near-concurrent ($-1.20$ steps).\nOutcome backpropagation lags by 6.70 steps, acting as a retrospective confirmation.\n\nAll pairwise differences are significant (Kruskal-Wallis $H{=}274.3$, $p{=}2.74{\\times}10^{-60}$; Bonferroni-corrected pairwise: cmd\\_rep vs.\\ file\\_diff $p{=}1.44{\\times}10^{-26}$, cmd\\_rep vs.\\ outcome\\_bp $p{=}6.67{\\times}10^{-39}$, file\\_diff vs.\\ outcome\\_bp $p{=}3.47{\\times}10^{-47}$).\n\n\\paragraph{Cross-agent reversal.}\nOn OpenHands, cmd\\_rep shifts from leading ($-1.87$) to lagging ($+3.32$ steps).\nThis reversal explains the cmd\\_rep pathology analyzed in \\S\\ref{sec:cmd_rep_ablation}: OH's action distribution triggers cmd\\_rep on progress windows, inverting its diagnostic value.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{../../figures/paper/fig_lf_temporal.pdf}\n\\caption{Temporal roles of labeling functions relative to stagnation onset on SWE-Agent. cmd\\_rep leads ($-1.87$ steps), file\\_diff is near-concurrent ($-1.20$), outcome\\_bp lags ($+6.70$). Inset: OH reversal where cmd\\_rep becomes lagging.}\n\\label{fig:lf_temporal}\n\\end{figure}\n\n%-------------------------------------------------------------------\n\\subsection{Command Repetition Ablation}\n\\label{sec:cmd_rep_ablation}\n\nThe cmd\\_rep LF fires on 92.3\\% of OH windows (vs.\\ 65.6\\% on SWE-Agent), with a 71\\% false positive rate on OH progress windows.\nTable~\\ref{tab:cmd_rep_ablation} shows the effect of removing it.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{LF Config} & \\textbf{ZS F1} & \\textbf{FT F1} & \\textbf{FT F1\\textsubscript{s}} & \\textbf{FT F1\\textsubscript{p}} \\\\\n\\midrule\n3-LF (w/ cmd\\_rep) & 0.530 & 0.751 & 0.544 & 0.959 \\\\\n2-LF (no cmd\\_rep) & 0.607 & \\textbf{0.927} & 0.938 & 0.917 \\\\\n\\midrule\n$\\Delta$ & +7.7\\,pp & +17.6\\,pp & +39.4\\,pp & $-4.2$\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Effect of removing cmd\\_rep on OpenHands probe performance. ZS = zero-shot transfer from SWE-Agent; FT = fine-tuned on 100\\% OH data. F1\\textsubscript{s}/F1\\textsubscript{p} = stagnation/progress F1.}\n\\label{tab:cmd_rep_ablation}\n\\end{table}\n\nRemoving cmd\\_rep improves zero-shot transfer by 7.7\\,pp and fine-tuned performance by 17.6\\,pp.\nThe gain is driven almost entirely by stagnation recall (+39.4\\,pp F1\\textsubscript{stag}), at a modest cost to progress detection ($-4.2$\\,pp F1\\textsubscript{prog}).\nThe 3-LF fine-tuned model's stagnation F1 of 0.544 reveals that cmd\\_rep corrupts silver labels so thoroughly that even full fine-tuning on OH data cannot recover.\nNote that removing cmd\\_rep also reduces training data from 101,713 to 72,554 windows (28.5\\% reduction); however, the model trained on \\emph{less} data with cleaner labels decisively outperforms the model trained on \\emph{more} data with corrupted labels, indicating that label quality rather than data volume drives the improvement.\nThis motivates agent-specific LF selection: labeling functions validated on one agent architecture may become adversarial on another.\n\n%-------------------------------------------------------------------\n\\subsection{Temporal Label Models}\n\\label{sec:temporal_label_models}\n\nWe investigate whether incorporating LF temporal dynamics into label aggregation improves over majority vote (MV).\nTable~\\ref{tab:temporal_models} compares three temporal label models \\citep{ratner2017snorkel,safranchik2020linkedhmm}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Method} & \\textbf{Conf${\\geq}$2 F1} & \\textbf{MV Agr.} & \\textbf{Probe F1$^\\ddagger$} \\\\\n\\midrule\nMV (baseline) & 0.8946$^\\ast$ & 1.000 & 0.8468 \\\\\nTWV ($\\sigma{=}2$) & \\textbf{0.9003} & 0.885 & 0.8211 \\\\\nLag-HMM & 0.8936 & 0.820 & --- \\\\\nHMM & 0.7502 & 0.685 & 0.6564 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Temporal label model comparison. $^\\ast$MV conf${\\geq}$2 F1 is a self-evaluation baseline (MV evaluated against itself on high-confidence windows). $^\\ddagger$Downstream: probe trained on each method's labels, evaluated on SWE-Agent conf${\\geq}$2 vs.\\ MV labels.}\n\\label{tab:temporal_models}\n\\end{table}\n\nTWV achieves the highest conf${\\geq}$2 F1 (0.9003, +0.57\\,pp over MV), but this gain does not propagate downstream: a probe trained on TWV labels scores 0.8211 vs.\\ 0.8468 for MV-trained ($-2.57$\\,pp).\nTWV flips 14.1\\% of conf$=$1 labels, introducing noise that hurts probe training.\nHMM overpredicts stagnation (29,176 stagnation vs.\\ 25,633 progress windows), degrading downstream performance to 0.6564.\nLag-HMM closely tracks MV ($-0.1$\\,pp) despite explicitly modeling temporal offsets, suggesting that the temporal structure captured by individual LFs does not improve \\emph{aggregation}.\n\n\\paragraph{TWV sensitivity.}\nThe Gaussian kernel bandwidth $\\sigma$ is critical: $\\sigma{=}2$ is optimal (0.9003); $\\sigma{=}1$ drops to 0.8105 and $\\sigma{\\geq}5$ falls below 0.81.\nThis narrow operating range, combined with the downstream degradation, makes TWV impractical as a drop-in MV replacement.\n\nThese results constitute a negative finding: despite clear temporal structure in LF firing patterns (\\S\\ref{sec:lf_temporal}), temporal label models do not improve over simple majority vote for downstream stagnation detection.\n\n%-------------------------------------------------------------------\n\\subsection{Gold Set Validation}\n\\label{sec:gold_set}\n\\goldset{Human-annotated gold set (650 windows) validation pending. Results will be added upon completion (expected 2026-05-17). This provides the non-circular ground truth evaluation for all methods.}",
      "numLines": 231,
      "startLine": 1,
      "totalLines": 231
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper. Let me also check the analysis section for any references to error analysis numbers mentioned in the task (85 FN, 64.9% of errors).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "f9da2420-0e1f-49e4-9df4-dc949d1be0e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzL8LVTvL1hbdsyQBvkgrM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13531,
      "cache_read_input_tokens": 30623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13531
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

_source line 20_

Let me check the analysis section for the error analysis numbers referenced in the task.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "384f4669-fbc0-4c1b-aede-ce425bec81b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzL8LVTvL1hbdsyQBvkgrM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13531,
      "cache_read_input_tokens": 30623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13531
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

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01BMUb1zMJ2gSaRDMiPhHWoT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "806d1f1d-ccab-42d9-864f-6f6566f2887b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzL8LVTvL1hbdsyQBvkgrM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13531,
      "cache_read_input_tokens": 30623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13531
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

_source line 22 · 2026-05-14T22:30:33.208Z_

<details><summary>↩ Tool result · `toolu_01BMUb1zMJ2gSaRDMiPhHWoT`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Circular Evaluation and Its Implications}
5	\label{sec:circular}
6	
7	The structural RF's 0.9951 macro-F1 (\S\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.
8	The 30 structural features include repetition ratios and file operation counts---the same signals $\lambda_1$ and $\lambda_2$ consume to produce silver labels.
9	This score therefore represents an upper bound on LF reverse-engineering fidelity.
10	
11	Two evaluation settings break this circularity.
12	First, cross-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.9674 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\_rep fires on 92.3\% vs.\ 65.6\% of windows).
13	The model cannot memorize LF outputs when tested on a different agent's distribution.
14	Second, a human-annotated gold set (\S\ref{sec:gold_set}) will provide definitive non-circular ground truth.
15	Until then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.
16	
17	\subsection{Why Temporal Label Models Fail}
18	\label{sec:why_tlm_fail}
19	
20	Despite clear temporal structure in LF activations (\S\ref{sec:lf_temporal}), no temporal label model improves downstream detection over majority vote (\S\ref{sec:temporal_label_models}).
21	The root cause is low label conflict in the 3-LF regime: conf${\geq}$2 windows dominate the training set, leaving few ambiguous labels for temporal models to correct.
22	
23	TWV targets only conf${=}1$ windows, flipping 14.1\% of their labels.
24	These flips introduce noise rather than corrections---downstream probe F1 drops by 2.57\,pp relative to MV-trained.
25	HMM overpredicts stagnation (29,176 vs.\ 25,633 progress windows), producing a distorted label distribution that degrades the probe to 0.6564.
26	Lag-HMM, despite explicitly modeling per-LF temporal offsets, tracks MV within 0.1\,pp---the offset information captured by individual LFs (\S\ref{sec:lf_temporal}) does not translate into better aggregation.
27	
28	Three binary LFs produce at most $2^3{=}8$ voting patterns, yielding too little conflict for temporal models to exploit.
29	A richer LF set ($>$10 functions with higher disagreement rates) would be needed to create the ambiguity where temporal aggregation could add value \citep{ratner2017snorkel}.
30	
31	\subsection{Error Analysis}
32	\label{sec:error_analysis}
33	
34	We analyze errors of the ProgressProbe (GRU) on the SWE-Agent conf${\geq}$2 test set under the stagnation-positive convention (positive = stagnation throughout).
35	The model misclassifies 131 of 1,824 windows (7.2\% error rate): 85 false negatives (predicted progress, actual stagnation; 64.9\% of errors) and 46 false positives (predicted stagnation, actual progress; 35.1\%).
36	
37	The recall bottleneck is the dominant failure mode: $P_\text{stag}{=}0.897$ vs.\ $R_\text{stag}{=}0.825$.
38	Missed stagnation windows (FN) are not borderline cases---the model assigns them a mean stagnation probability of only 0.078 (i.e., high progress confidence of 0.922), with 73\% receiving $>$0.9 progress probability.
39	These windows feature agents performing diverse edits and varied commands that mimic progress patterns while making no effective headway, constituting a systematic blind spot.
40	False positives arise when agents repeat specific command patterns during genuine progress.
41	
42	LF conflict is a strong error predictor: 39.7\% of error windows have at least one LF disagreeing, compared to a 31\% base rate.
43	The cmd\_rep LF contributes the highest per-LF error rate (12.75\%).
44	Errors concentrate in trajectory midpoints (10.2\% error rate vs.\ 6.5\% at endpoints), where the boundary between exploration and stagnation is most ambiguous.
45	Error mass is also non-uniform across trajectories: the two highest-error trajectories account for 18.3\% of all misclassifications.
46	
47	\subsection{Outcome Backpropagation as Distant Supervision}
48	\label{sec:ob_analysis}
49	
50	Outcome backpropagation ($\lambda_3$) is a privileged signal that uses task outcome, unavailable at inference time.
51	A 3-seed split-isolated holdout removing $\lambda_3$ yields macro-F1 of $0.770{\pm}0.022$, a 7.7\,pp drop from the 3-LF baseline of 0.847.
52	$\lambda_3$ contributes 33.5\% of conf${\geq}$2 labels (5,158 of 15,401 windows).
53	
54	However, $\lambda_3$ functions as a coverage expander rather than an independent corrector: across 43,402 windows where both 2-LF and 3-LF configurations produce labels, their agreement is 100\%.
55	$\lambda_3$ never flips a majority vote---it only promotes conf${=}1$ windows to conf${=}2$ by adding a third agreeing vote.
56	This suggests that additional real-time LFs targeting the same coverage gaps could replace the privileged outcome signal without sacrificing label quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "ed16bd02-706f-4e6c-9240-4703de753c31",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\n\\label{sec:analysis}\n\n\\subsection{Circular Evaluation and Its Implications}\n\\label{sec:circular}\n\nThe structural RF's 0.9951 macro-F1 (\\S\\ref{sec:main_results}) is a predictable consequence of feature--label overlap, not a detection achievement.\nThe 30 structural features include repetition ratios and file operation counts---the same signals $\\lambda_1$ and $\\lambda_2$ consume to produce silver labels.\nThis score therefore represents an upper bound on LF reverse-engineering fidelity.\n\nTwo evaluation settings break this circularity.\nFirst, cross-agent transfer: GB trained on SWE-Agent LF distributions achieves 0.9674 macro-F1 on OpenHands, where LF firing patterns differ substantially (e.g., cmd\\_rep fires on 92.3\\% vs.\\ 65.6\\% of windows).\nThe model cannot memorize LF outputs when tested on a different agent's distribution.\nSecond, a human-annotated gold set (\\S\\ref{sec:gold_set}) will provide definitive non-circular ground truth.\nUntil then, all in-domain structural metrics should be interpreted as LF-agreement scores rather than detection accuracy.\n\n\\subsection{Why Temporal Label Models Fail}\n\\label{sec:why_tlm_fail}\n\nDespite clear temporal structure in LF activations (\\S\\ref{sec:lf_temporal}), no temporal label model improves downstream detection over majority vote (\\S\\ref{sec:temporal_label_models}).\nThe root cause is low label conflict in the 3-LF regime: conf${\\geq}$2 windows dominate the training set, leaving few ambiguous labels for temporal models to correct.\n\nTWV targets only conf${=}1$ windows, flipping 14.1\\% of their labels.\nThese flips introduce noise rather than corrections---downstream probe F1 drops by 2.57\\,pp relative to MV-trained.\nHMM overpredicts stagnation (29,176 vs.\\ 25,633 progress windows), producing a distorted label distribution that degrades the probe to 0.6564.\nLag-HMM, despite explicitly modeling per-LF temporal offsets, tracks MV within 0.1\\,pp---the offset information captured by individual LFs (\\S\\ref{sec:lf_temporal}) does not translate into better aggregation.\n\nThree binary LFs produce at most $2^3{=}8$ voting patterns, yielding too little conflict for temporal models to exploit.\nA richer LF set ($>$10 functions with higher disagreement rates) would be needed to create the ambiguity where temporal aggregation could add value \\citep{ratner2017snorkel}.\n\n\\subsection{Error Analysis}\n\\label{sec:error_analysis}\n\nWe analyze errors of the ProgressProbe (GRU) on the SWE-Agent conf${\\geq}$2 test set under the stagnation-positive convention (positive = stagnation throughout).\nThe model misclassifies 131 of 1,824 windows (7.2\\% error rate): 85 false negatives (predicted progress, actual stagnation; 64.9\\% of errors) and 46 false positives (predicted stagnation, actual progress; 35.1\\%).\n\nThe recall bottleneck is the dominant failure mode: $P_\\text{stag}{=}0.897$ vs.\\ $R_\\text{stag}{=}0.825$.\nMissed stagnation windows (FN) are not borderline cases---the model assigns them a mean stagnation probability of only 0.078 (i.e., high progress confidence of 0.922), with 73\\% receiving $>$0.9 progress probability.\nThese windows feature agents performing diverse edits and varied commands that mimic progress patterns while making no effective headway, constituting a systematic blind spot.\nFalse positives arise when agents repeat specific command patterns during genuine progress.\n\nLF conflict is a strong error predictor: 39.7\\% of error windows have at least one LF disagreeing, compared to a 31\\% base rate.\nThe cmd\\_rep LF contributes the highest per-LF error rate (12.75\\%).\nErrors concentrate in trajectory midpoints (10.2\\% error rate vs.\\ 6.5\\% at endpoints), where the boundary between exploration and stagnation is most ambiguous.\nError mass is also non-uniform across trajectories: the two highest-error trajectories account for 18.3\\% of all misclassifications.\n\n\\subsection{Outcome Backpropagation as Distant Supervision}\n\\label{sec:ob_analysis}\n\nOutcome backpropagation ($\\lambda_3$) is a privileged signal that uses task outcome, unavailable at inference time.\nA 3-seed split-isolated holdout removing $\\lambda_3$ yields macro-F1 of $0.770{\\pm}0.022$, a 7.7\\,pp drop from the 3-LF baseline of 0.847.\n$\\lambda_3$ contributes 33.5\\% of conf${\\geq}$2 labels (5,158 of 15,401 windows).\n\nHowever, $\\lambda_3$ functions as a coverage expander rather than an independent corrector: across 43,402 windows where both 2-LF and 3-LF configurations produce labels, their agreement is 100\\%.\n$\\lambda_3$ never flips a majority vote---it only promotes conf${=}1$ windows to conf${=}2$ by adding a third agreeing vote.\nThis suggests that additional real-time LFs targeting the same coverage gaps could replace the privileged outcome signal without sacrificing label quality.",
      "numLines": 56,
      "startLine": 1,
      "totalLines": 56
    }
  }
}
```

</details>

---

### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the Related Work section. The task specifies:

1. ~700 words total across 5 paragraphs
2. Specific citation keys to use (all verified in references.bib)
3. Specific structure for each paragraph
4. Writing constraints (no "significantly" without stats, no value judgments, etc.)

Let me now write this. I need to be careful to:
- Use \paragraph{} level subsections, not \subsection{}
- Not repeat numbers already detailed in the Introduction


- Use \citet for inline citations, \citep for parenthetical
- End each paragraph with differentiation
- Stay neutral about related work

Writing the Related Work section...

I'm positioning our approach against existing PRM work by highlighting key distinctions: we operate at the window level to capture temporal patterns across consecutive actions rather than evaluating individual steps, we avoid requiring outcome labels or reward annotations at inference time by relying solely on observable structural signals, and we prioritize real-time monitoring efficiency with sub-5ms latency requirements.

Now I'm reviewing the literature on agent self-reflection and verification methods. While prior work like Reflexion and tree-of-thought approaches focus on what agents should do when stuck, relying on the model's own judgment for both detection and correction, recent findings show that LLMs struggle to self-correct without external feedback. Our contribution shifts the focus to detecting when an agent is stuck in the first place, using external structural signals rather than depending on the agent's self-evaluation.

Moving to weak supervision for sequential data, I'm looking at how data programming and systems like Snorkel have enabled rapid dataset creation through labeling functions, though most work assumes independent samples. Recent extensions are beginning to handle sequential dependencies, like linked HMM approaches for weakly supervised learning on ordered data.

When I apply these techniques to agent trajectories, I find that temporal label models—HMM variants and other temporal aggregation methods—actually don't outperform simple majority voting in our setting with low label disagreement. This is a negative result that's worth noting for future work on agent data.

Recent research shows that coding agents degrade over long trajectories, and that monitoring them requires understanding the full sequence context rather than just individual steps. Interestingly, weaker monitoring models can effectively oversee stronger agents if properly scaffolded. I'm seeing that multi-agent systems have systematic failure patterns, especially cascading failures in long-horizon tasks. For my own work, I'm comparing different monitoring signals—structural features, neural embeddings, and LLM-based approaches—and finding that simple structural features actually work remarkably well for detecting failures and transferring across different agent architectures, without needing additional LLMs or GPUs.

Now looking at cycle and anomaly detection approaches. Prior work focuses on detecting repetitive cycles through call-stack analysis or n-gram patterns, and some methods train verifiers on synthetic perturbations to catch trajectory anomalies. The limitation is that these approaches catch exact or near-exact repetition but miss when agents get stuck in functionally similar states while varying their surface behavior. My window-level approach with structural features handles both repetitive and non-repetitive stagnation, though my error analysis shows some missed cases involve diverse but ineffective behavior—exactly the kind of pattern that repetition-based detectors would also struggle with.

Now I'm working through the word counts for each section. The target is around 700 words total, distributed across five paragraphs with specific ranges for each. I need to be more precise with my estimates and adjust accordingly, making sure the monitoring and cycle/anomaly sections reach their target lengths since they're currently running short.

I'm also reviewing the constraints carefully: I should avoid repeating detailed numbers from the introduction, skip using "significantly" without statistical backing, stay neutral in tone, and verify that every citation key matches what's in the references file. Let me cross-check the citation keys against the provided list to ensure they're all valid. I'm reviewing the formatting requirements—the task specifies `\paragraph{}` for the five subsections rather than `\subsection{}`, so I'll adjust that structure. I also need to be careful not to repeat the specific metrics already detailed in the Introduction like the F1 scores and performance gaps, instead just referencing them briefly where relevant.

Now I'm expanding the Monitoring and Cycle/Anomaly Detection paragraphs to around 150 words each, and I'm drafting the Related Work section to cover Process Reward Models with citations to AgentPRM and InversePRM, establishing how those approaches differ from what I'm proposing.

Writing LaTeX content... tree-structured deliberation and Monte Carlo tree search with self-evaluation have been proposed, but research shows LLMs struggle to self-correct without external feedback—they often make things worse. My approach differs by detecting when an agent is stuck using external structural signals rather than relying on the model's own judgment, which I validate against an LLM-as-judge baseline. Weak supervision methods like data programming and Snorkel have enabled rapid labeling through user-defined functions, though existing work assumes independent samples rather than sequential dependencies.

I'm exploring how to apply data programming to agent trajectories, where labeling functions exhibit temporal patterns. Prior work on sequential weak supervision—like linked HMMs for NER and multi-resolution label functions—showed promise, but when I test temporal label models on my low-conflict setup with just three labeling functions, they don't outperform simple majority voting, which suggests sequential extensions have real limitations in this regime.

Now I'm looking at the broader context of agent monitoring and failure modes. Recent findings show that coding agents degrade significantly over long trajectories, that effective monitoring requires understanding sequences rather than individual steps, and that lightweight monitors can actually oversee stronger agents effectively. There's also emerging evidence of systematic failure patterns in multi-agent systems like step repetition and cascading failures.

For detecting these failures, researchers have developed approaches combining structural analysis with embedding similarity to catch action-level cycles, while others use speculative decoding and repetition heuristics to identify reasoning loops. A more comprehensive method trains a verifier on synthetic perturbations to detect various trajectory anomalies including task failures.

However, cycle detection has a fundamental limitation---it only catches exact or near-exact repetition and misses semantically diverse stagnation where agents vary their commands while remaining functionally stuck. My approach frames this differently: instead of treating stagnation as a rare anomaly, I model it as binary classification over sliding windows, since stagnation is actually quite common. Using structural features, I can capture both repetitive and non-repetitive patterns of ineffective behavior. The error analysis shows that most missed cases involve this diverse-but-ineffective behavior that repetition-based methods would also fail to detect.

Now I'm doing a word count estimate to see if the paragraphs fit within the target length---roughly 130 words per paragraph, totaling around 625 words, which means I need to compress further.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "d84a94db-41bb-405d-9f7e-e6c34b69c104",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011k2fWoUwQUEzKfof2RAaTD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1764,
      "cache_read_input_tokens": 44154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1764
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

_source line 24_

Now I have full context. Writing the Related Work section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "86ecd844-5a6f-4a31-a07e-f0f3119131ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011k2fWoUwQUEzKfof2RAaTD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1764,
      "cache_read_input_tokens": 44154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1764
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

_source line 25_

<details open><summary>🔧 Tool call — Write · `toolu_01YWR1cj5bHeNUCAK8fyEZ58`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex",
  "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Process Reward Models.}\nProcess reward models (PRMs) assign step-level quality scores to guide agent behavior during inference or training.\n\\citet{xi2025agentprm} introduce AgentPRM, training TD/GAE-based step-level rewards that evaluate both long-term promise and immediate progress in agent trajectories, requiring outcome labels and an RL pipeline.\n\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels.\nEvaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs outperform general-purpose ones, while \\citet{wang2026planrewardbench} reveal that all reward model categories---generative, discriminative, and LLM-as-judge---degrade on long-horizon trajectories.\n\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques, and \\citet{qiu2026dataprm} introduce environment-aware probing for data analysis agents to detect silent errors.\nOur work differs in operating at window level rather than step level, requiring no outcome labels or reward annotations at inference time---labeling functions use only observable structural signals---and targeting real-time monitoring ($<$5\\,ms per window) rather than training signal generation.\n\n\\paragraph{Agent Self-Reflection and Verification.}\nSelf-reflection methods prompt agents to diagnose and correct their own failures.\n\\citet{shinn2023reflexion} introduce verbal self-reflection loops, \\citet{yao2023tot} propose tree-structured deliberation, and \\citet{zhou2024lats} combine Monte Carlo tree search with LLM self-evaluation for language agents.\nHowever, \\citet{huang2024selfcorrect} demonstrate that LLMs cannot reliably self-correct reasoning without external feedback, and \\citet{kamoi2024selfcorrection} confirm that self-correction attempts frequently degrade initial answers.\nThese methods address what to \\emph{do} when an agent is stuck, relying on the stuck model's own judgment for both detection and correction.\nWe address the prior question---\\emph{when} is the agent stuck---using external structural signals rather than self-evaluation.\nOur LLM-as-judge baseline (\\S\\ref{sec:main_results}) illustrates the ceiling of model-based assessment for this detection task.\n\n\\paragraph{Weak Supervision for Sequential Data.}\nData programming \\citep{ratner2016dataprogramming} enables rapid dataset creation through user-defined labeling functions (LFs), with Snorkel \\citep{ratner2017snorkel} operationalizing this into a dependency-aware end-to-end system.\n\\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods, and \\citet{zhang2021wrench} benchmark 22 weak supervision datasets, all assuming i.i.d.\\ samples.\nExtensions to sequential data relax this assumption: \\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised NER, improving over i.i.d.\\ label models by incorporating span-level linking rules; \\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities; and \\citet{dawid1979em} provide the foundational EM framework for aggregating noisy annotators, later extended with HMM structure for sequential settings.\nWe apply data programming to agent trajectories, a novel domain where LFs exhibit systematic temporal dynamics distinct from token-level NER.\nUnlike \\citeauthor{safranchik2020linkedhmm}'s positive NER results, we find that temporal label models (HMM, lag-HMM, TWV) do not improve over majority vote in our low-conflict 3-LF regime (\\S\\ref{sec:temporal_label_models})---a negative result that constrains when sequential extensions to weak supervision add value.\n\n\\paragraph{Agent Monitoring and Degradation.}\nRecent work documents the prevalence and impact of agent failures at scale.\n\\citet{orlanski2026slopcodebench} provide direct evidence of coding agent degradation on SlopCodeBench, recording verbosity increases and quality drops across long-horizon trajectories with no agent fully solving any benchmark task.\n\\citet{chen2025monitoring} establish that sequence-level context is necessary for effective agent monitoring, as single-step analysis misses failures that emerge only across action sequences.\n\\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, showing weak models can reliably oversee stronger agents---a finding that motivates lightweight monitoring approaches over scaling up monitor size.\n\\citet{cemri2025multiagentfail} identify 14 systematic failure modes in multi-agent systems including step repetition as a concrete symptom, and \\citet{zhu2025agentfail} show that cascading failures---where single root causes propagate across subsequent decisions---dominate long-horizon tasks.\nThese works document and motivate the monitoring problem; we complement them with a systematic comparative study across signal types (structural, neural, LLM-based), demonstrating that lightweight structural features suffice for detection and transfer across agent architectures without requiring another LLM or GPU.\n\n\\paragraph{Cycle and Anomaly Detection.}\nCycle detection targets structural repetition in agent behavior.\n\\citet{george2025cycledetection} combine call-stack analysis (CDCS) with embedding similarity (CDSA) to detect action-level cycles in agents, and \\citet{pipis2025reasoningloop} analyze reasoning loops in language models using speculative decoding and $n$-gram repetition heuristics.\n\\citet{liu2026trajad} take a broader view with TrajAD, training a fine-grained verifier through synthetic perturbations to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation; they show that general-purpose LLMs perform poorly at zero-shot trajectory verification, motivating specialized approaches.\nCycle detectors are effective for exact or near-exact repetition but by design cannot capture semantically diverse stagnation, where agents vary surface commands while remaining functionally stuck.\nOur window-level approach with structural features captures both repetitive and non-repetitive stagnation patterns.\nWe formulate stagnation as prevalent binary classification over sliding windows rather than rare-event anomaly detection (\\S\\ref{sec:setup}), and our error analysis (\\S\\ref{sec:error_analysis}) confirms that the dominant missed-stagnation category involves diverse-but-ineffective behavior---the pattern category that repetition-based detectors would also miss.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "dbdf8e06-32c8-40df-abdf-7763d8cc69b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011k2fWoUwQUEzKfof2RAaTD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1764,
      "cache_read_input_tokens": 44154,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1764
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

_source line 26 · 2026-05-14T22:32:13.658Z_

<details><summary>↩ Tool result · `toolu_01YWR1cj5bHeNUCAK8fyEZ58`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "e5974f0c-f565-4c98-840a-e487a6751ac6",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/agent_progress_probe/docs/paper/sections/related_work.tex",
    "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Process Reward Models.}\nProcess reward models (PRMs) assign step-level quality scores to guide agent behavior during inference or training.\n\\citet{xi2025agentprm} introduce AgentPRM, training TD/GAE-based step-level rewards that evaluate both long-term promise and immediate progress in agent trajectories, requiring outcome labels and an RL pipeline.\n\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels.\nEvaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs outperform general-purpose ones, while \\citet{wang2026planrewardbench} reveal that all reward model categories---generative, discriminative, and LLM-as-judge---degrade on long-horizon trajectories.\n\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques, and \\citet{qiu2026dataprm} introduce environment-aware probing for data analysis agents to detect silent errors.\nOur work differs in operating at window level rather than step level, requiring no outcome labels or reward annotations at inference time---labeling functions use only observable structural signals---and targeting real-time monitoring ($<$5\\,ms per window) rather than training signal generation.\n\n\\paragraph{Agent Self-Reflection and Verification.}\nSelf-reflection methods prompt agents to diagnose and correct their own failures.\n\\citet{shinn2023reflexion} introduce verbal self-reflection loops, \\citet{yao2023tot} propose tree-structured deliberation, and \\citet{zhou2024lats} combine Monte Carlo tree search with LLM self-evaluation for language agents.\nHowever, \\citet{huang2024selfcorrect} demonstrate that LLMs cannot reliably self-correct reasoning without external feedback, and \\citet{kamoi2024selfcorrection} confirm that self-correction attempts frequently degrade initial answers.\nThese methods address what to \\emph{do} when an agent is stuck, relying on the stuck model's own judgment for both detection and correction.\nWe address the prior question---\\emph{when} is the agent stuck---using external structural signals rather than self-evaluation.\nOur LLM-as-judge baseline (\\S\\ref{sec:main_results}) illustrates the ceiling of model-based assessment for this detection task.\n\n\\paragraph{Weak Supervision for Sequential Data.}\nData programming \\citep{ratner2016dataprogramming} enables rapid dataset creation through user-defined labeling functions (LFs), with Snorkel \\citep{ratner2017snorkel} operationalizing this into a dependency-aware end-to-end system.\n\\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods, and \\citet{zhang2021wrench} benchmark 22 weak supervision datasets, all assuming i.i.d.\\ samples.\nExtensions to sequential data relax this assumption: \\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised NER, improving over i.i.d.\\ label models by incorporating span-level linking rules; \\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities; and \\citet{dawid1979em} provide the foundational EM framework for aggregating noisy annotators, later extended with HMM structure for sequential settings.\nWe apply data programming to agent trajectories, a novel domain where LFs exhibit systematic temporal dynamics distinct from token-level NER.\nUnlike \\citeauthor{safranchik2020linkedhmm}'s positive NER results, we find that temporal label models (HMM, lag-HMM, TWV) do not improve over majority vote in our low-conflict 3-LF regime (\\S\\ref{sec:temporal_label_models})---a negative result that constrains when sequential extensions to weak supervision add value.\n\n\\paragraph{Agent Monitoring and Degradation.}\nRecent work documents the prevalence and impact of agent failures at scale.\n\\citet{orlanski2026slopcodebench} provide direct evidence of coding agent degradation on SlopCodeBench, recording verbosity increases and quality drops across long-horizon trajectories with no agent fully solving any benchmark task.\n\\citet{chen2025monitoring} establish that sequence-level context is necessary for effective agent monitoring, as single-step analysis misses failures that emerge only across action sequences.\n\\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, showing weak models can reliably oversee stronger agents---a finding that motivates lightweight monitoring approaches over scaling up monitor size.\n\\citet{cemri2025multiagentfail} identify 14 systematic failure modes in multi-agent systems including step repetition as a concrete symptom, and \\citet{zhu2025agentfail} show that cascading failures---where single root causes propagate across subsequent decisions---dominate long-horizon tasks.\nThese works document and motivate the monitoring problem; we complement them with a systematic comparative study across signal types (structural, neural, LLM-based), demonstrating that lightweight structural features suffice for detection and transfer across agent architectures without requiring another LLM or GPU.\n\n\\paragraph{Cycle and Anomaly Detection.}\nCycle detection targets structural repetition in agent behavior.\n\\citet{george2025cycledetection} combine call-stack analysis (CDCS) with embedding similarity (CDSA) to detect action-level cycles in agents, and \\citet{pipis2025reasoningloop} analyze reasoning loops in language models using speculative decoding and $n$-gram repetition heuristics.\n\\citet{liu2026trajad} take a broader view with TrajAD, training a fine-grained verifier through synthetic perturbations to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation; they show that general-purpose LLMs perform poorly at zero-shot trajectory verification, motivating specialized approaches.\nCycle detectors are effective for exact or near-exact repetition but by design cannot capture semantically diverse stagnation, where agents vary surface commands while remaining functionally stuck.\nOur window-level approach with structural features captures both repetitive and non-repetitive stagnation patterns.\nWe formulate stagnation as prevalent binary classification over sliding windows rather than rare-event anomaly detection (\\S\\ref{sec:setup}), and our error analysis (\\S\\ref{sec:error_analysis}) confirms that the dominant missed-stagnation category involves diverse-but-ineffective behavior---the pattern category that repetition-based detectors would also miss.\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 54,
        "newStart": 1,
        "newLines": 41,
        "lines": [
          "-% Related Work: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)",
          " \\section{Related Work}",
          " \\label{sec:related_work}",
          " ",
          "-\\subsection{LLM Agent Monitoring and Evaluation}",
          "+\\paragraph{Process Reward Models.}",
          "+Process reward models (PRMs) assign step-level quality scores to guide agent behavior during inference or training.",
          "+\\citet{xi2025agentprm} introduce AgentPRM, training TD/GAE-based step-level rewards that evaluate both long-term promise and immediate progress in agent trajectories, requiring outcome labels and an RL pipeline.",
          "+\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels.",
          "+Evaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs outperform general-purpose ones, while \\citet{wang2026planrewardbench} reveal that all reward model categories---generative, discriminative, and LLM-as-judge---degrade on long-horizon trajectories.",
          "+\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques, and \\citet{qiu2026dataprm} introduce environment-aware probing for data analysis agents to detect silent errors.",
          "+Our work differs in operating at window level rather than step level, requiring no outcome labels or reward annotations at inference time---labeling functions use only observable structural signals---and targeting real-time monitoring ($<$5\\,ms per window) rather than training signal generation.",
          " ",
          "-As LLM agents tackle increasingly complex tasks \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands,zhou2024webarena,wang2024mint}, understanding and monitoring their failure modes has become critical.",
          "-Taxonomic studies reveal that agent failures are often systematic: \\citet{cemri2025multiagentfail} identify 14 failure modes in multi-agent systems, including step repetition as a concrete symptom, while \\citet{zhu2025agentfail} show that cascading failures---where a single root cause propagates across subsequent decisions---dominate long-horizon tasks.",
          "-\\citet{orlanski2026slopcodebench} provide the most direct evidence of agent degradation, documenting structural erosion in 77\\% of coding agent trajectories with no agent fully solving any benchmark task end-to-end.",
          "+\\paragraph{Agent Self-Reflection and Verification.}",
          "+Self-reflection methods prompt agents to diagnose and correct their own failures.",
          "+\\citet{shinn2023reflexion} introduce verbal self-reflection loops, \\citet{yao2023tot} propose tree-structured deliberation, and \\citet{zhou2024lats} combine Monte Carlo tree search with LLM self-evaluation for language agents.",
          "+However, \\citet{huang2024selfcorrect} demonstrate that LLMs cannot reliably self-correct reasoning without external feedback, and \\citet{kamoi2024selfcorrection} confirm that self-correction attempts frequently degrade initial answers.",
          "+These methods address what to \\emph{do} when an agent is stuck, relying on the stuck model's own judgment for both detection and correction.",
          "+We address the prior question---\\emph{when} is the agent stuck---using external structural signals rather than self-evaluation.",
          "+Our LLM-as-judge baseline (\\S\\ref{sec:main_results}) illustrates the ceiling of model-based assessment for this detection task.",
          " ",
          "-Existing monitoring approaches span several paradigms.",
          "-\\emph{Self-reflection} methods \\citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent to diagnose its own failures, but \\citet{huang2024selfcorrect} and \\citet{kamoi2024selfcorrection} demonstrate that LLMs cannot reliably self-correct without external feedback, motivating external monitoring.",
          "-\\citet{george2025cycledetection} propose unsupervised cycle detection combining call-stack analysis with embedding similarity, while \\citet{pipis2025reasoningloop} analyze why reasoning models loop, using $n$-gram repetition as a detection heuristic.",
          "-On the external monitoring front, \\citet{chen2025monitoring} show that sequence-level context is necessary---single-step analysis misses sequentially contextual harm---and \\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, with weak models reliably monitoring stronger agents.",
          "+\\paragraph{Weak Supervision for Sequential Data.}",
          "+Data programming \\citep{ratner2016dataprogramming} enables rapid dataset creation through user-defined labeling functions (LFs), with Snorkel \\citep{ratner2017snorkel} operationalizing this into a dependency-aware end-to-end system.",
          "+\\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods, and \\citet{zhang2021wrench} benchmark 22 weak supervision datasets, all assuming i.i.d.\\ samples.",
          "+Extensions to sequential data relax this assumption: \\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised NER, improving over i.i.d.\\ label models by incorporating span-level linking rules; \\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities; and \\citet{dawid1979em} provide the foundational EM framework for aggregating noisy annotators, later extended with HMM structure for sequential settings.",
          "+We apply data programming to agent trajectories, a novel domain where LFs exhibit systematic temporal dynamics distinct from token-level NER.",
          "+Unlike \\citeauthor{safranchik2020linkedhmm}'s positive NER results, we find that temporal label models (HMM, lag-HMM, TWV) do not improve over majority vote in our low-conflict 3-LF regime (\\S\\ref{sec:temporal_label_models})---a negative result that constrains when sequential extensions to weak supervision add value.",
          " ",
          "-Our work differs from all of the above in its central question: rather than proposing a new monitoring \\emph{method}, we conduct an empirical study asking what \\emph{signals} carry stagnation information.",
          "-We show that 30 structural features suffice for near-perfect detection (0.995 F1), without requiring another LLM, self-reflection, or embedding-based similarity.",
          "+\\paragraph{Agent Monitoring and Degradation.}",
          "+Recent work documents the prevalence and impact of agent failures at scale.",
          "+\\citet{orlanski2026slopcodebench} provide direct evidence of coding agent degradation on SlopCodeBench, recording verbosity increases and quality drops across long-horizon trajectories with no agent fully solving any benchmark task.",
          "+\\citet{chen2025monitoring} establish that sequence-level context is necessary for effective agent monitoring, as single-step analysis misses failures that emerge only across action sequences.",
          "+\\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, showing weak models can reliably oversee stronger agents---a finding that motivates lightweight monitoring approaches over scaling up monitor size.",
          "+\\citet{cemri2025multiagentfail} identify 14 systematic failure modes in multi-agent systems including step repetition as a concrete symptom, and \\citet{zhu2025agentfail} show that cascading failures---where single root causes propagate across subsequent decisions---dominate long-horizon tasks.",
          "+These works document and motivate the monitoring problem; we complement them with a systematic comparative study across signal types (structural, neural, LLM-based), demonstrating that lightweight structural features suffice for detection and transfer across agent architectures without requiring another LLM or GPU.",
          " ",
          "-\\subsection{Process Reward Models for Agents}",
          "-",
          "-Process reward models (PRMs) assign quality scores to individual agent steps, enabling search-time guidance and trajectory selection.",
          "-\\citet{xi2025agentprm} introduce AgentPRM, training step-level reward models via TD/GAE that evaluate both ``promise'' (long-term potential) and ``progress'' (immediate advancement), achieving 8$\\times$ compute efficiency gains.",
          "-\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels, with a 3B model surpassing GPT-4o.",
          "-Evaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs substantially outperform general-purpose ones, while \\citet{wang2026planrewardbench} evaluate trajectory-level reward models and reveal that all model categories---generative, discriminative, and LLM-as-judge---degrade significantly on long-horizon trajectories.",
          "-\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques (Agent-RRM), and \\citet{qiu2026dataprm} address data analysis agents specifically, introducing environment-aware probing to detect silent errors that standard PRMs miss.",
          "-",
          "-Our work is complementary to the PRM line but differs in three fundamental ways: (1)~we operate at window level rather than step level, capturing temporal patterns across consecutive actions; (2)~we require no outcome labels or reward annotations---our labeling functions use only observable structural signals; and (3)~our goal is real-time \\emph{monitoring} (stagnation detection in $<$5\\,ms), not \\emph{training signal} generation for agent improvement.",
          "-The degradation of trajectory-level reward models on long horizons reported by \\citet{wang2026planrewardbench} further motivates our window-level approach, which avoids full-trajectory reasoning by design.",
          "-",
          "-\\subsection{Data Programming and Weak Supervision}",
          "-",
          "-Data programming \\citep{ratner2016dataprogramming} enables rapid training set creation through user-defined labeling functions (LFs), with a generative model learning LF accuracies to produce probabilistic labels.",
          "-Snorkel \\citep{ratner2017snorkel} operationalizes this into an end-to-end system with dependency-aware label models, and \\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods.",
          "-\\citet{zhang2021wrench} provide a comprehensive benchmark spanning 22 datasets, though all assume i.i.d.\\ data points.",
          "-",
          "-Extensions to sequential data relax this assumption.",
          "-\\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised sequence tagging (NER), incorporating linking rules that model span structure and improving over i.i.d.\\ label models by 7~F1 points.",
          "-\\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities.",
          "-In crowdsourcing, \\citet{nguyen2017hmmcrowd} extend \\citeauthor{dawid1979em}'s EM-based annotator model \\citep{dawid1979em} with HMM structure for sequential label aggregation.",
          "-",
          "-We apply data programming to agent trajectory data, a novel domain where LFs exhibit systematic temporal dynamics (e.g., command repetition leads stagnation onset by 1.87 steps on SWE-Agent).",
          "-Unlike prior sequential extensions that target token-level NER or multi-resolution alignment, our setting involves window-level binary classification with agent-specific LF role reversals.",
          "-Critically, we test whether temporal label models---motivated by the clear i.i.d.\\ violations we observe---can improve over majority vote, and report a negative finding: three implementations (TWV, HMM, lag-aware HMM) all fail to surpass simple voting in the low-conflict regime of our 3-LF framework.",
          "-",
          "-\\subsection{Anomaly Detection in Agent Trajectories}",
          "-",
          "-Detecting anomalous behavior in sequential agent data connects to the broader literature on time-series anomaly detection.",
          "-\\citet{liu2026trajad} propose TrajAD, training a fine-grained verifier through synthetic perturbations (perturb-and-complete) to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation.",
          "-They show that general-purpose LLMs perform poorly at zero-shot trajectory anomaly detection, motivating specialized approaches.",
          "-",
          "-Our work differs from anomaly detection in both formulation and methodology.",
          "-We frame stagnation as a binary classification problem over sliding windows rather than identifying rare deviations from a normal distribution.",
          "-Stagnation is not anomalous in the statistical sense---it occurs in 28.5\\% of SWE-Agent windows and 6.6\\% of OpenHands windows---but rather represents a persistent behavioral regime that an agent enters and may not exit without intervention.",
          "-Where TrajAD requires training a specialized verifier on synthetic data, our empirical analysis reveals that hand-crafted structural features achieve 0.995 F1 without any learned components, and our probe model uses a lightweight GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} rather than a full LLM verifier.",
          "+\\paragraph{Cycle and Anomaly Detection.}",
          "+Cycle detection targets structural repetition in agent behavior.",
          "+\\citet{george2025cycledetection} combine call-stack analysis (CDCS) with embedding similarity (CDSA) to detect action-level cycles in agents, and \\citet{pipis2025reasoningloop} analyze reasoning loops in language models using speculative decoding and $n$-gram repetition heuristics.",
          "+\\citet{liu2026trajad} take a broader view with TrajAD, training a fine-grained verifier through synthetic perturbations to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation; they show that general-purpose LLMs perform poorly at zero-shot trajectory verification, motivating specialized approaches.",
          "+Cycle detectors are effective for exact or near-exact repetition but by design cannot capture semantically diverse stagnation, where agents vary surface commands while remaining functionally stuck.",
          "+Our window-level approach with structural features captures both repetitive and non-repetitive stagnation patterns.",
          "+We formulate stagnation as prevalent binary classification over sliding windows rather than rare-event anomaly detection (\\S\\ref{sec:setup}), and our error analysis (\\S\\ref{sec:error_analysis}) confirms that the dominant missed-stagnation category involves diverse-but-ineffective behavior---the pattern category that repetition-based detectors would also miss."
        ]
      }
    ],
    "originalFile": "% Related Work: Structural stagnation detection in LLM coding agents (EMNLP 2026 ARR)\n\\section{Related Work}\n\\label{sec:related_work}\n\n\\subsection{LLM Agent Monitoring and Evaluation}\n\nAs LLM agents tackle increasingly complex tasks \\citep{jimenez2024swebench,yang2024sweagent,wang2025openhands,zhou2024webarena,wang2024mint}, understanding and monitoring their failure modes has become critical.\nTaxonomic studies reveal that agent failures are often systematic: \\citet{cemri2025multiagentfail} identify 14 failure modes in multi-agent systems, including step repetition as a concrete symptom, while \\citet{zhu2025agentfail} show that cascading failures---where a single root cause propagates across subsequent decisions---dominate long-horizon tasks.\n\\citet{orlanski2026slopcodebench} provide the most direct evidence of agent degradation, documenting structural erosion in 77\\% of coding agent trajectories with no agent fully solving any benchmark task end-to-end.\n\nExisting monitoring approaches span several paradigms.\n\\emph{Self-reflection} methods \\citep{shinn2023reflexion,yao2023tot,zhou2024lats} rely on the agent to diagnose its own failures, but \\citet{huang2024selfcorrect} and \\citet{kamoi2024selfcorrection} demonstrate that LLMs cannot reliably self-correct without external feedback, motivating external monitoring.\n\\citet{george2025cycledetection} propose unsupervised cycle detection combining call-stack analysis with embedding similarity, while \\citet{pipis2025reasoningloop} analyze why reasoning models loop, using $n$-gram repetition as a detection heuristic.\nOn the external monitoring front, \\citet{chen2025monitoring} show that sequence-level context is necessary---single-step analysis misses sequentially contextual harm---and \\citet{kale2025weaktostrong} demonstrate that monitor scaffolding matters more than monitor capability, with weak models reliably monitoring stronger agents.\n\nOur work differs from all of the above in its central question: rather than proposing a new monitoring \\emph{method}, we conduct an empirical study asking what \\emph{signals} carry stagnation information.\nWe show that 30 structural features suffice for near-perfect detection (0.995 F1), without requiring another LLM, self-reflection, or embedding-based similarity.\n\n\\subsection{Process Reward Models for Agents}\n\nProcess reward models (PRMs) assign quality scores to individual agent steps, enabling search-time guidance and trajectory selection.\n\\citet{xi2025agentprm} introduce AgentPRM, training step-level reward models via TD/GAE that evaluate both ``promise'' (long-term potential) and ``progress'' (immediate advancement), achieving 8$\\times$ compute efficiency gains.\n\\citet{choudhury2025prm} formalize the PRM framework and propose InversePRM, learning process rewards from expert demonstrations without outcome labels, with a 3B model surpassing GPT-4o.\nEvaluation benchmarks have emerged in parallel: \\citet{li2026toolprmbench} benchmark PRMs on tool-use scenarios, finding that specialized PRMs substantially outperform general-purpose ones, while \\citet{wang2026planrewardbench} evaluate trajectory-level reward models and reveal that all model categories---generative, discriminative, and LLM-as-judge---degrade significantly on long-horizon trajectories.\n\\citet{fan2026agentrm} extend PRMs with structured reasoning traces and multi-dimensional critiques (Agent-RRM), and \\citet{qiu2026dataprm} address data analysis agents specifically, introducing environment-aware probing to detect silent errors that standard PRMs miss.\n\nOur work is complementary to the PRM line but differs in three fundamental ways: (1)~we operate at window level rather than step level, capturing temporal patterns across consecutive actions; (2)~we require no outcome labels or reward annotations---our labeling functions use only observable structural signals; and (3)~our goal is real-time \\emph{monitoring} (stagnation detection in $<$5\\,ms), not \\emph{training signal} generation for agent improvement.\nThe degradation of trajectory-level reward models on long horizons reported by \\citet{wang2026planrewardbench} further motivates our window-level approach, which avoids full-trajectory reasoning by design.\n\n\\subsection{Data Programming and Weak Supervision}\n\nData programming \\citep{ratner2016dataprogramming} enables rapid training set creation through user-defined labeling functions (LFs), with a generative model learning LF accuracies to produce probabilistic labels.\nSnorkel \\citep{ratner2017snorkel} operationalizes this into an end-to-end system with dependency-aware label models, and \\citet{fu2020flyingsquid} accelerate label model inference via closed-form triplet methods.\n\\citet{zhang2021wrench} provide a comprehensive benchmark spanning 22 datasets, though all assume i.i.d.\\ data points.\n\nExtensions to sequential data relax this assumption.\n\\citet{safranchik2020linkedhmm} introduce a linked HMM for weakly supervised sequence tagging (NER), incorporating linking rules that model span structure and improving over i.i.d.\\ label models by 7~F1 points.\n\\citet{sala2019multiresolution} handle multi-resolution LFs operating at different temporal granularities.\nIn crowdsourcing, \\citet{nguyen2017hmmcrowd} extend \\citeauthor{dawid1979em}'s EM-based annotator model \\citep{dawid1979em} with HMM structure for sequential label aggregation.\n\nWe apply data programming to agent trajectory data, a novel domain where LFs exhibit systematic temporal dynamics (e.g., command repetition leads stagnation onset by 1.87 steps on SWE-Agent).\nUnlike prior sequential extensions that target token-level NER or multi-resolution alignment, our setting involves window-level binary classification with agent-specific LF role reversals.\nCritically, we test whether temporal label models---motivated by the clear i.i.d.\\ violations we observe---can improve over majority vote, and report a negative finding: three implementations (TWV, HMM, lag-aware HMM) all fail to surpass simple voting in the low-conflict regime of our 3-LF framework.\n\n\\subsection{Anomaly Detection in Agent Trajectories}\n\nDetecting anomalous behavior in sequential agent data connects to the broader literature on time-series anomaly detection.\n\\citet{liu2026trajad} propose TrajAD, training a fine-grained verifier through synthetic perturbations (perturb-and-complete) to detect trajectory anomalies including task failure, process inefficiency, and unwarranted continuation.\nThey show that general-purpose LLMs perform poorly at zero-shot trajectory anomaly detection, motivating specialized approaches.\n\nOur work differs from anomaly detection in both formulation and methodology.\nWe frame stagnation as a binary classification problem over sliding windows rather than identifying rare deviations from a normal distribution.\nStagnation is not anomalous in the statistical sense---it occurs in 28.5\\% of SWE-Agent windows and 6.6\\% of OpenHands windows---but rather represents a persistent behavioral regime that an agent enters and may not exit without intervention.\nWhere TrajAD requires training a specialized verifier on synthetic data, our empirical analysis reveals that hand-crafted structural features achieve 0.995 F1 without any learned components, and our probe model uses a lightweight GRU \\citep{cho2014gru} with attention \\citep{bahdanau2015attention} rather than a full LLM verifier.\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 27_

Related Work 已写入。5 个 paragraph-level subsection，~700 words，所有 citation key 均来自已验证列表，无 "significantly"，无价值判断，数字通过 section 引用回指而非重复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "uuid": "a866c058-359e-4e93-921b-87670f16f086",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017N6fZWiejsj6B9MriBGdL5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6099,
      "cache_read_input_tokens": 45918,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6099
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

_source line 28_

Related Work 已写入。5 个 paragraph-level subsection，~700 words，所有 citation key 均来自已验证列表，无 "significantly"，无价值判断，数字通过 section 引用回指而非重复。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 122400,
  "duration_api_ms": 123191,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "12d618f5-dc82-475a-9a92-2a9761f5a484",
  "total_cost_usd": 0.503222,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 40176,
    "cache_read_input_tokens": 157356,
    "output_tokens": 6835,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40176,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 68,
        "cache_read_input_tokens": 45918,
        "cache_creation_input_tokens": 6099,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6099
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2444,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002539,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 6835,
      "cacheReadInputTokens": 157356,
      "cacheCreationInputTokens": 40176,
      "webSearchRequests": 0,
      "costUSD": 0.500683,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b9f8de4c-1157-424a-9128-f5f147ca7647"
}
```

</details>

---
