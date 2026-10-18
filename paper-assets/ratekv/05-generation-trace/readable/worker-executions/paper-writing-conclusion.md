# paper writing conclusion

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/workers/worker_paper_writing_conclusion_20260514T110127.log`
- **Structured JSON:** [`81bd19028a865932fdda.json`](../../sessions/81/81bd19028a865932fdda.json)

## Before a recorded user message

8 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
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
  "uuid": "48085adf-114c-41e7-b39f-a75071797e58",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-ratekv/memory/"
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
    "resetsAt": 1778796000,
    "rateLimitType": "seven_day",
    "utilization": 0.77,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "1c9c3d2e-2f58-477d-a159-e646a2105fb2",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

### Assistant

_source line 4_

I'll start by reading the latex-paper skill and the existing paper sections to ensure consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "f519fd23-eda9-416c-be6f-e230a3c774f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEbFSd3R35VFYTQRsYDVGy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11894
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

<details open><summary>🔧 Tool call — Read · `toolu_01DYJfSQ5xjTNRfcDnodaK2h`</summary>

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
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "a23029fd-f1da-476c-9ce4-e08e76842525",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEbFSd3R35VFYTQRsYDVGy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11894
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

_source line 6 · 2026-05-14T11:01:39.667Z_

<details><summary>↩ Tool result · `toolu_01DYJfSQ5xjTNRfcDnodaK2h`</summary>

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
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "5e0df707-ee05-4419-ac63-0e69d34bd505",
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

<details open><summary>🔧 Tool call — Agent · `toolu_01WZ9WJ3Vzm1RWepwWtNp6ri`</summary>

```json
{
  "description": "Read existing paper sections",
  "subagent_type": "Explore",
  "prompt": "Read the following files to extract key claims, numbers, and terminology used in the paper so far. I need to ensure the Conclusion section is consistent with them.\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/ — list all files in this directory\n2. Read the abstract and introduction files if they exist (likely abstract.tex, introduction.tex or similar)\n3. Read any results/experiments section if it exists\n\nFor each file, extract:\n- Exact numbers cited (percentages, improvements, specific values)\n- Key terminology and how concepts are named\n- Any claims about the method\n\nReport all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "a0546b74-ed31-477b-b4bf-40af90a9ba52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MEbFSd3R35VFYTQRsYDVGy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11894,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11894
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

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aa1bc34633d90da83",
  "tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "description": "Read existing paper sections",
  "task_type": "local_agent",
  "prompt": "Read the following files to extract key claims, numbers, and terminology used in the paper so far. I need to ensure the Conclusion section is consistent with them.\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/ — list all files in this directory\n2. Read the abstract and introduction files if they exist (likely abstract.tex, introduction.tex or similar)\n3. Read any results/experiments section if it exists\n\nFor each file, extract:\n- Exact numbers cited (percentages, improvements, specific values)\n- Key terminology and how concepts are named\n- Any claims about the method\n\nReport all findings in detail.",
  "uuid": "105055d2-4f28-4bb5-a2a7-8b244f0f07c0",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

## Round 1

30 recorded events

### User

_source line 9 · 2026-05-14T11:01:44.373Z_

Read the following files to extract key claims, numbers, and terminology used in the paper so far. I need to ensure the Conclusion section is consistent with them.

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/ — list all files in this directory
2. Read the abstract and introduction files if they exist (likely abstract.tex, introduction.tex or similar)
3. Read any results/experiments section if it exists

For each file, extract:
- Exact numbers cited (percentages, improvements, specific values)
- Key terminology and how concepts are named
- Any claims about the method

Report all findings in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "3053d5d2-8a55-4684-ab0a-c30d18aaa17c"
}
```

</details>

---

### System

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa1bc34633d90da83",
  "tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 27300,
    "tool_uses": 1,
    "duration_ms": 1693
  },
  "last_tool_name": "Bash",
  "uuid": "303ed0a2-3da6-4ba9-9b9f-7c6d0e17625e",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_01TtiaJQxkntg6FCMmS26rDu`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "6a3bb667-3cb1-445a-bcdb-4df1140cd09e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BmR94aHhdcBXNRFkrywe1t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27291,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27291,
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

_source line 12 · 2026-05-14T11:01:46.224Z_

<details><summary>↩ Tool result · `toolu_01TtiaJQxkntg6FCMmS26rDu`</summary>

```text
total 136
drwxr-xr-x 3 ubuntu ubuntu  4096 May 14 10:47 .
drwxr-xr-x 4 ubuntu ubuntu  4096 May 13 17:17 ..
-rw-r--r-- 1 ubuntu ubuntu  1519 May 14 11:01 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu 11615 May 14 07:32 acl.sty
-rw-r--r-- 1 ubuntu ubuntu 45186 May 14 07:32 acl_natbib.bst
-rw-r--r-- 1 ubuntu ubuntu  7337 May 14 10:13 analysis.tex
-rw-r--r-- 1 ubuntu ubuntu  9849 May 14 11:00 experiments.tex
drwxr-xr-x 2 ubuntu ubuntu  4096 May 14 07:43 figures
-rw-r--r-- 1 ubuntu ubuntu  5673 May 14 10:20 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  8563 May 14 10:44 method.tex
-rw-r--r-- 1 ubuntu ubuntu  6092 May 14 09:14 references.bib
-rw-r--r-- 1 ubuntu ubuntu  2071 May 14 09:02 references.bib.prev
-rw-r--r-- 1 ubuntu ubuntu  4793 May 14 10:45 related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "b2797ef5-798a-4a2b-9b37-b4eb1b155202"
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
  "task_id": "aa1bc34633d90da83",
  "tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "description": "Reading docs/paper/abstract.tex",
  "usage": {
    "total_tokens": 28659,
    "tool_uses": 2,
    "duration_ms": 3941
  },
  "last_tool_name": "Read",
  "uuid": "c74c0b8b-a261-462c-9016-c774756e693c",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01Qm4RxMBTb2TEBTBuAEZdGJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "c3053c4e-916a-401f-ba8b-d4b0a031d527",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1355,
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

_source line 15 · 2026-05-14T11:01:48.322Z_

<details><summary>↩ Tool result · `toolu_01Qm4RxMBTb2TEBTBuAEZdGJ`</summary>

```text
1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce identical bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm.
6	However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
7	We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that predicts, before any allocation, whether a given architecture will benefit from non-uniform quantization.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "89755190-e845-4eef-b2bb-409fdc466bdd"
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
  "task_id": "aa1bc34633d90da83",
  "tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "description": "Reading docs/paper/introduction.tex",
  "usage": {
    "total_tokens": 28660,
    "tool_uses": 3,
    "duration_ms": 4769
  },
  "last_tool_name": "Read",
  "uuid": "f3133ddb-5edd-4ef7-a26e-3fdc8ffbcf15",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01Vxnq9dGUAbeVBuu1QA1Pf2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "38453094-5692-4e36-bb37-bbff909b9d07",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1355,
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

_source line 18 · 2026-05-14T11:01:49.153Z_

<details><summary>↩ Tool result · `toolu_01Vxnq9dGUAbeVBuu1QA1Pf2`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Per-head mixed-precision quantization of the KV cache is a natural strategy for reducing memory during LLM inference: assign fewer bits to insensitive heads and more bits to sensitive ones, achieving lower perplexity than uniform quantization at the same average bit-width.
5	Recent work on KV cache quantization explores both uniform schemes~\cite{liu2024kivi,hooper2024kvquant,lin2024qserve,he2024zipcache} and token-level mixed-precision approaches~\cite{ge2024fastgen,lei2026arkv}, while complementary methods reduce cache size through eviction~\cite{zhang2023h2o,li2024snapkv}.
6	RateQuant~\cite{zuo2026ratequant} formalizes per-head allocation as a rate-distortion optimization and shows that greedy allocation is optimal when bit-widths are consecutive integers $\{2,3,4,5,6\}$, exploiting the polymatroid structure of the feasible set (their Proposition~6).
7	
8	In practice, hardware-efficient inference requires bit-widths drawn from $\{2, 4, 8, 16\}$---the formats natively supported by modern accelerators.
9	On this non-consecutive set, the polymatroid structure breaks down, and greedy is no longer provably optimal.
10	One might expect that exact MCKP solvers would fill this gap.
11	They do not.
12	On Qwen2.5-7B at $4\times$ compression, unconstrained greedy achieves 32.45 PPL and unconstrained MCKP achieves 36.92---both \emph{far worse} than uniform 4-bit (15.45).
13	The optimization does not merely underperform; it fails catastrophically.
14	
15	The root cause is not solver suboptimality but a violation of the objective's additive distortion assumption.
16	Both solvers assign 68--75 of 112 KV heads to 2-bit, where per-head quantization errors are large enough to compound through the residual stream.
17	The additive model predicts $\sim$11 PPL for these allocations; the actual PPL is $3$--$4\times$ higher.
18	At 4-bit and above, per-head distortions are small and compound negligibly---uniform 4-bit achieves close to its additive prediction---but 2-bit distortions are orders of magnitude larger.
19	When most heads are quantized to 2-bit simultaneously, cumulative truncation errors exceed the network's capacity to compensate, and perplexity degrades super-linearly.
20	
21	This observation points to a minimal intervention: cap the number of 2-bit assignments.
22	We add a single cardinality constraint $\sum_h \mathbb{1}[b_h{=}2] \leq k$ to the standard MCKP formulation (\S\ref{sec:method}).
23	On Qwen2.5-7B, setting $k{=}8$ (7\% of heads) yields 11.23 PPL---a 27.3\% reduction over uniform 4-bit.
24	The constraint works by forcing the solver to use 2-bit only on the least-sensitive heads, while redistributing the freed budget to protect sensitive heads at 8-bit or 16-bit.
25	This is not a heuristic patch: the constraint directly addresses the identified failure mode and is compatible with any solver.
26	
27	A surprising consequence is that, under the cardinality constraint, the choice of solver becomes irrelevant.
28	Constrained greedy and constrained MCKP produce identical allocations---not approximately, but exactly: all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3 (the single difference is a zero-distortion tie with no PPL impact).
29	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal (\S\ref{sec:solver_equiv}), enabling practitioners to use the simpler $O(H \log H)$ greedy algorithm without sacrificing solution quality.
30	
31	However, non-uniform allocation does not help universally.
32	On Llama-3.1-8B, constrained MCKP achieves 8.45 PPL vs.\ uniform 8.47---a marginal 0.2\% improvement.
33	On Mistral-7B-v0.3, it is slightly \emph{worse}: 7.16 vs.\ 7.13.
34	The difference across architectures traces to head sensitivity heterogeneity: Qwen's KV heads vary widely in 2-bit distortion, with Layer-0 heads contributing a disproportionate share, while Mistral's heads are nearly uniform in sensitivity.
35	When there is no heterogeneity to exploit, non-uniform allocation adds noise without benefit.
36	
37	This motivates a diagnostic question that prior work does not address: \emph{when} should a practitioner use per-head mixed-precision quantization?
38	We propose a heterogeneity diagnostic based on the top-5\% concentration of per-head distortion (\S\ref{sec:heterogeneity}).
39	On our three architectures, the metric cleanly separates the beneficial case (Qwen, concentration 0.59--0.66, 27.3\% PPL improvement) from the neutral case (Llama, 0.34--0.59, marginal) and the counterproductive case (Mistral, 0.42, slightly worse than uniform).
40	The diagnostic reuses profiling data already required by the solver and adds no computational overhead.
41	
42	Our contributions are:
43	\begin{enumerate}[nosep]
44	\item We identify 2-bit distortion compounding as the cause of catastrophic failure in unconstrained per-head KV cache quantization on hardware-aligned bit-widths, and show that a cardinality constraint on 2-bit assignments is a minimal sufficient fix, reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23 (constrained) at $4\times$ compression (\S\ref{sec:compounding}, \S\ref{sec:experiments}).
45	
46	\item We demonstrate that the cardinality constraint makes solver choice irrelevant: constrained greedy and constrained MCKP produce identical per-head allocations across three architectures, enabling use of a simple greedy algorithm (\S\ref{sec:solver_equiv}).
47	
48	\item We propose a heterogeneity-based diagnostic framework that predicts whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes (\S\ref{sec:heterogeneity}).
49	\end{enumerate}
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "59566ccf-c132-4ad6-bc93-3821e58efecf"
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
  "task_id": "aa1bc34633d90da83",
  "tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 28661,
    "tool_uses": 4,
    "duration_ms": 5009
  },
  "last_tool_name": "Read",
  "uuid": "62faaeb7-b3d5-4504-8dde-0e71502bdc71",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01L6u1GL6AViS9geT31Ftapq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "70e3d0e7-0eb2-4e58-acc5-8744ea9d160d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1355,
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

_source line 21 · 2026-05-14T11:01:49.400Z_

<details><summary>↩ Tool result · `toolu_01L6u1GL6AViS9geT31Ftapq`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Problem Formulation}
5	\label{sec:formulation}
6	
7	We formulate per-head KV cache quantization as a constrained optimization problem.
8	Let $h \in \{1,\ldots,H\}$ index the KV heads across all layers, $b_h \in \mathcal{B}$ the bit-width assigned to head $h$, and $\mathcal{B} = \{2, 4, 8, 16\}$ the set of hardware-aligned bit-widths.
9	Each head $h$ has a profiled distortion function $d_h(b)$, the PPL increase when head $h$ is quantized to $b$ bits.
10	Given a memory budget ratio $R$ (e.g., $R = 0.25$ for $4\times$ compression), we seek the allocation that minimizes total distortion:
11	\begin{equation}
12	\label{eq:objective}
13	\min_{\{b_h\}} \sum_{h=1}^{H} d_h(b_h) \quad \text{s.t.} \quad \frac{1}{H \cdot 16}\sum_{h=1}^{H} b_h \leq R.
14	\end{equation}
15	
16	This is a multiple-choice knapsack problem (MCKP): each head selects one bit-width from $\mathcal{B}$ to minimize total distortion under a budget.
17	RateQuant~\cite{zuo2026ratequant} solves this for consecutive bit-widths $\{2,3,4,5,6\}$, where the polymatroid structure of the feasible set guarantees that greedy allocation is optimal (their Proposition 6).
18	Hardware-aligned bit-widths $\{2,4,8,16\}$ are non-consecutive; the gaps break this structure, and greedy is no longer guaranteed to match the MCKP optimum.
19	Moreover, as we show in \S\ref{sec:compounding}, the objective itself is not well-behaved: distortions from 2-bit heads compound non-additively, making unconstrained optimization unreliable.
20	
21	\subsection{PPL-based Per-Head Profiling}
22	\label{sec:profiling}
23	
24	We profile each KV head independently by quantizing it to each $b \in \mathcal{B}$ while keeping all other heads at bf16, and measuring the resulting PPL increase $d_h(b)$ on a calibration set of 64 sequences $\times$ 2048 tokens from WikiText-2 train.
25	This yields a distortion table of $H \times |\mathcal{B}|$ entries that serves as input to the solver.
26	
27	The optimization in Eq.~\eqref{eq:objective} relies on an additive distortion assumption: the total PPL degradation from a mixed-precision allocation is approximately $\sum_h d_h(b_h)$.
28	This holds when per-head distortions are small and independent---a reasonable approximation for 4-bit and 8-bit quantization, where individual head distortions are typically below 0.1 PPL.
29	At 2-bit, however, individual distortions are orders of magnitude larger, and the additive assumption breaks down.
30	
31	\subsection{Compounding Effect}
32	\label{sec:compounding}
33	
34	When many heads are simultaneously quantized to 2-bit, per-head distortions compound non-additively.
35	The mechanism is straightforward: each head's quantized output feeds into the residual stream, and truncation errors from multiple 2-bit heads accumulate through subsequent layers.
36	When the number of 2-bit heads is small, these errors are absorbed by the remaining high-precision heads.
37	As the count grows, cumulative errors exceed the capacity of the residual stream to compensate, and PPL degrades super-linearly.
38	
39	\begin{figure}[t]
40	\centering
41	\includegraphics[width=\columnwidth]{figures/fig2_compounding_curve.pdf}
42	\caption{PPL on Qwen2.5-7B ($4\times$ compression) as a function of $k$, the maximum number of 2-bit heads. Too few 2-bit heads waste budget on 4-bit; too many trigger compounding. The minimum occurs at $k{=}8$.}
43	\label{fig:compounding}
44	\end{figure}
45	
46	Unconstrained solvers are blind to this effect because the additive objective underestimates the cost of large-scale 2-bit assignment.
47	On Qwen2.5-7B, unconstrained greedy assigns 68 heads to 2-bit and achieves 32.45 PPL; unconstrained MCKP assigns 75 heads and achieves 36.92---both far worse than uniform 4-bit (15.45).
48	Standard-resolution profiling detects non-zero $d_h(2)$ for only 37 of 112 heads; the remaining 75 heads have $d_h(2) \approx 0$, so most 2-bit assignments appear free to the additive objective.
49	The resulting additive prediction is $\sum_h d_h(b_h) + \text{baseline} \approx 11$ PPL---$3\text{--}4\times$ lower than the actual 32--37 PPL, because the compounding interaction between simultaneously quantized heads is invisible to per-head profiling.
50	
51	This compounding is specific to 2-bit quantization.
52	At 4-bit and above, per-head distortions are small enough that additivity holds even when all heads share the same bit-width (uniform 4-bit achieves 15.45 PPL, close to the sum-of-distortions prediction).
53	The qualitative difference arises because 2-bit quantization has far larger per-head distortion, saturating the error tolerance of the residual stream.
54	
55	Figure~\ref{fig:compounding} shows the relationship between $k$ (the maximum number of 2-bit heads) and PPL on Qwen2.5-7B at $4\times$ compression.
56	The curve is U-shaped: at $k{=}0$ (uniform 4-bit), PPL is 15.45; allowing a few 2-bit heads reduces PPL by freeing budget for 8-bit heads on sensitive positions, reaching a minimum of 11.23 at $k{=}8$; beyond this point, compounding drives PPL upward, reaching 35.35 at $k{=}75$.
57	
58	\subsection{Cardinality Constraint}
59	\label{sec:cardinality}
60	
61	The compounding effect motivates a simple addition to Eq.~\eqref{eq:objective}: a cardinality constraint on 2-bit assignments.
62	\begin{equation}
63	\label{eq:constraint}
64	\sum_{h=1}^{H} \mathbb{1}[b_h = 2] \leq k.
65	\end{equation}
66	
67	The constraint parameter $k$ is selected by a small-scale sweep on calibration data: solve the constrained problem for each candidate $k$, evaluate calibration PPL, and pick the value at the minimum of the U-shaped curve (Figure~\ref{fig:compounding}).
68	For Qwen2.5-7B with 112 KV heads, $k{=}8$ ($\sim$7\% of heads).
69	
70	The constraint is a single linear inequality, compatible with any solver---greedy, MCKP, or integer linear programming---and adds negligible overhead to the optimization.
71	
72	A natural question is whether Layer-0 heads require explicit protection, since attention heads in the first layer are known to carry disproportionate importance.
73	On Qwen2.5-7B, the profiler assigns very high distortion to Layer-0 heads at 2-bit: L0H0 increases PPL by 31.9\% relative to the bf16 baseline (9.81 $\to$ 12.94), L0H2 by 23.2\% (9.81 $\to$ 12.09), L0H3 by 11.7\% (9.81 $\to$ 10.96).
74	These values are large enough that no solver would assign 2-bit to Layer-0 under any reasonable budget.
75	We verify this empirically: running the solver with and without manual Layer-0 exclusion produces identical allocations across all 112 heads.
76	No manual exclusion rule is needed; the profiler signal is sufficient.
77	
78	\subsection{Solver Equivalence}
79	\label{sec:solver_equiv}
80	
81	\begin{table}[t]
82	\centering
83	\small
84	\caption{Solver comparison on Qwen2.5-7B at $4\times$ compression. Unconstrained solvers over-allocate 2-bit heads and fail catastrophically. The cardinality constraint ($k{\leq}8$) makes greedy and MCKP produce identical allocations.\footnotemark}
85	\label{tab:solver_equiv}
86	\begin{tabular}{llcccc}
87	\toprule
88	Solver & Constraint & PPL & \multicolumn{3}{c}{Bit distribution} \\
89	 & & & 2-bit & 4-bit & 8/16-bit \\
90	\midrule
91	Greedy & None & 32.45 & 68 & 30 & 14 \\
92	MCKP & None & 36.92 & 75 & 33 & 4 \\
93	Greedy & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
94	MCKP & $k{\leq}8$ & 11.23 & 8 & 100 & 4 \\
95	Uniform & --- & 15.45 & 0 & 112 & 0 \\
96	\bottomrule
97	\end{tabular}
98	\end{table}
99	\footnotetext{Standard-resolution profiling; hires profiling (64 seq $\times$ 2048 tok) achieves 10.91 (\S\ref{sec:profiling_resolution}).}
100	
101	With the cardinality constraint in place, greedy and MCKP produce identical results---not approximately, but exactly.
102	Table~\ref{tab:solver_equiv} shows that constrained greedy and constrained MCKP achieve the same PPL (11.23) with the same bit distribution on Qwen2.5-7B.
103	We verify this at the per-head level across three models:
104	
105	\begin{itemize}[nosep]
106	\item \textbf{Qwen2.5-7B:} 112/112 heads receive identical bit-widths.
107	\item \textbf{Llama-3.1-8B:} 256/256 heads identical.
108	\item \textbf{Mistral-7B-v0.3:} 255/256 heads identical. The single difference is a zero-distortion tie between two heads at 4-bit and 8-bit, with no PPL impact.
109	\end{itemize}
110	
111	The constraint narrows the feasible set enough that greedy's locally optimal decisions are globally optimal.
112	Without it, greedy cascades into excessive 2-bit allocation: each additional 2-bit head looks locally beneficial (freeing budget) but contributes to the compounding effect that degrades global PPL.
113	The cardinality constraint breaks this cascade by capping the number of 2-bit heads, aligning local and global optima.
114	
115	The practical implication is that practitioners can use the simpler $O(H \log H)$ greedy algorithm instead of MCKP without sacrificing optimality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "0d7452ef-1495-43f1-8a76-8cd4ed4e9325"
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
  "task_id": "aa1bc34633d90da83",
  "tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "description": "Reading docs/paper/experiments.tex",
  "usage": {
    "total_tokens": 28662,
    "tool_uses": 5,
    "duration_ms": 5039
  },
  "last_tool_name": "Read",
  "uuid": "a0e7e6d4-8d79-40f4-b5ab-db3e041cfa96",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01Rayi36ucuj8b198puWLjsz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "aa38fc59-5611-47d6-8a2b-e20db404f8ae",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1355,
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

_source line 24 · 2026-05-14T11:01:49.422Z_

<details><summary>↩ Tool result · `toolu_01Rayi36ucuj8b198puWLjsz`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate on three architectures spanning different grouped-query attention (GQA) configurations:
9	\textbf{Qwen2.5-7B} (GQA ratio 7:1, 28 layers $\times$ 4 KV heads = 112 KV heads),
10	\textbf{Llama-3.1-8B} (4:1, 32 $\times$ 8 = 256 KV heads),
11	and \textbf{Mistral-7B-v0.3} (4:1, 32 $\times$ 8 = 256 KV heads, sliding window attention).
12	This selection covers the two dominant KV head counts (112 vs.\ 256) and both standard and sliding-window attention.
13	
14	\paragraph{Evaluation.}
15	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
16	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
17	
18	\paragraph{Profiling.}
19	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
20	Calibration uses 64 sequences of 2048 tokens from WikiText-2 train.
21	
22	\paragraph{Compression and constraint.}
23	The default target is 4$\times$ compression (average 4 bits, budget ratio 0.25).
24	The cardinality constraint limits 2-bit assignments to at most $k$ heads, where $k$ is selected via the compounding sweep described in \S\ref{sec:method} ($k{=}8$ for Qwen's 112 heads; analogous sweeps determine $k$ for Llama and Mistral).
25	
26	\paragraph{Baselines.}
27	We compare against:
28	(1)~uniform 4-bit quantization;
29	(2)~unconstrained greedy allocation (RateQuant-style~\cite{zuo2026ratequant});
30	(3)~unconstrained MCKP allocation;
31	(4)~an L0-random heuristic that assigns Layer-0 heads to 8-bit and $k$ random non-Layer-0 heads to 2-bit, with remaining heads at 4-bit (5 seeds; we report mean$\pm$std and median);
32	and (5)~a naive positional heuristic that assigns Layer-0 to 8-bit and the $k$ deepest heads to 2-bit.
33	
34	\subsection{Main Results}
35	\label{sec:main_results}
36	
37	\begin{table}[t]
38	\centering
39	\small
40	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained allocation fails catastrophically on $\{2,4,8,16\}$; our cardinality constraint restores performance. Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\ddagger$Best $k$ from ablation ($k{=}4$); Table~\ref{tab:heuristic} uses $k{=}16$ for fair comparison with heuristic baselines under the same constraint.}
41	\label{tab:main_results}
42	\begin{tabular}{lcccccc}
43	\toprule
44	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
45	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
46	\midrule
47	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23} \\
48	Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \textbf{8.45}$^\dagger$ \\
49	Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\
50	\bottomrule
51	\end{tabular}
52	\end{table}
53	
54	Table~\ref{tab:main_results} summarizes the main results.
55	On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
56	Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in \S\ref{sec:profiling_resolution}.
57	Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
58	The constraint eliminates this failure mode entirely.
59	
60	On Llama-3.1-8B, the improvement is marginal: 8.45 vs.\ 8.47 (0.2\%).
61	The profiler finds low sensitivity heterogeneity across Llama's 256 KV heads, leaving little room for non-uniform allocation to improve over uniform.
62	
63	On Mistral-7B-v0.3, constrained MCKP (7.16) is slightly worse than uniform (7.13, $+$0.4\%).
64	This is a genuine negative result: the profiler reports near-zero sensitivity differences across heads, meaning the optimization has no reliable signal to exploit.
65	Mistral's sliding-window attention may contribute to this uniformity by limiting head-level variation in effective context length.
66	
67	Unconstrained results for Llama and Mistral are omitted (---) as those experiments were conducted only on Qwen, where the failure mode is most pronounced.
68	Figure~\ref{fig:allocation} visualizes the bit-width allocation on Qwen, showing how constrained MCKP protects Layer-0 heads at 8-bit while selectively assigning only the 8 least-sensitive heads to 2-bit.
69	
70	\begin{figure}[t]
71	\centering
72	\includegraphics[width=\columnwidth]{figures/fig3_allocation_comparison.pdf}
73	\caption{Bit-width allocation on Qwen2.5-7B at 4$\times$ compression. Uniform assigns all heads to 4-bit. Constrained MCKP protects Layer-0 heads at 8-bit and assigns the 8 least-sensitive heads to 2-bit.}
74	\label{fig:allocation}
75	\end{figure}
76	
77	\subsection{Budget Sweep}
78	\label{sec:budget_sweep}
79	
80	\begin{table}[t]
81	\centering
82	\small
83	\caption{Effect of compression ratio on Qwen2.5-7B. Constrained MCKP provides meaningful gains at moderate-to-aggressive compression ($\geq$4$\times$). Standard-resolution profiling; hires results in \S\ref{sec:profiling_resolution}.}
84	\label{tab:budget_sweep}
85	\begin{tabular}{cccc}
86	\toprule
87	Compression & Uniform PPL & Constr.\ MCKP PPL & $\Delta$ PPL \\
88	\midrule
89	2$\times$ & 10.10 & 10.66 & $-$0.56 \\
90	4$\times$ & 15.45 & 11.23 & $+$4.21 \\
91	8$\times$ & 14{,}759 & 907 & $+$13{,}852 \\
92	\bottomrule
93	\end{tabular}
94	\end{table}
95	
96	Table~\ref{tab:budget_sweep} shows how the benefit of constrained allocation varies with compression ratio on Qwen2.5-7B.
97	
98	At 2$\times$ compression, uniform 8-bit quantization is near-lossless (10.10 PPL vs.\ 9.81 bf16, $+$0.29).
99	Per-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.
100	
101	At 4$\times$, the gap is substantial: constrained MCKP reduces PPL from 15.45 to 11.23, a 27.3\% improvement.
102	Hires profiling further reduces this to 10.91 (\S\ref{sec:profiling_resolution}).
103	
104	At 8$\times$, both methods degrade catastrophically---the budget is too aggressive for any allocation to preserve model quality.
105	However, constrained MCKP (907) is an order of magnitude better than uniform (14{,}759) because the constraint still protects Layer-0 heads at 8-bit, preventing total representational collapse.
106	Neither result is practically usable, but the gap demonstrates the protection mechanism at work.
107	
108	\subsection{Heuristic Baselines}
109	\label{sec:heuristic}
110	
111	\begin{table}[t]
112	\centering
113	\small
114	\caption{Constrained MCKP vs.\ heuristic baselines at 4$\times$ compression. L0-random reports median and mean$\pm$std over 5 seeds. All methods use the same $k$ per model ($k{=}8$ for Qwen, $k{=}16$ for Llama/Mistral).}
115	\label{tab:heuristic}
116	\begin{tabular}{lcccc}
117	\toprule
118	Model & MCKP & \multicolumn{2}{c}{L0-random} & Naive \\
119	 & & Median & Mean$\pm$Std & Positional \\
120	\midrule
121	Qwen2.5-7B      & 11.23 & 11.52 & 11.69$\pm$0.47 & 12.23 \\
122	Llama-3.1-8B    & 8.45  & 10.04 & 10.48$\pm$1.03 & 9.94 \\
123	Mistral-7B-v0.3 & 7.32  & 7.59  & 7.56$\pm$0.09  & 7.48 \\
124	\bottomrule
125	\end{tabular}
126	\end{table}
127	
128	Table~\ref{tab:heuristic} compares profiling-guided MCKP against heuristic baselines that use the same Layer-0 protection but assign 2-bit heads without profiling.
129	
130	On Qwen, MCKP (11.23) beats the L0-random median (11.52) by 0.29 PPL and the naive positional heuristic (12.23) by 1.00 PPL, confirming that profiling-guided selection outperforms both random and depth-based assignment.
131	
132	On Llama, the gap is larger: MCKP achieves 8.45 vs.\ L0-random median 10.04.
133	The high variance of L0-random on this architecture (std$=$1.03) indicates that 2-bit assignment is position-sensitive on 256-head models, making random selection unreliable.
134	The naive positional heuristic (9.94) performs better than random but still 1.49 PPL worse than MCKP, confirming that depth alone is an imperfect proxy for head sensitivity.
135	
136	On Mistral, the gap is small (7.32 vs.\ 7.59), consistent with the low heterogeneity observed in \S\ref{sec:main_results}.
137	The low L0-random variance (std$=$0.09) further confirms that head sensitivities are nearly uniform, so the choice of which heads receive 2-bit has little impact.
138	All non-uniform strategies (MCKP 7.32, naive 7.48, L0-random 7.56) are worse than uniform 4-bit (7.13) on this architecture, reinforcing that non-uniform allocation is counterproductive when heterogeneity is low.
139	
140	\subsection{Downstream Evaluation}
141	\label{sec:downstream}
142	
143	\begin{table}[t]
144	\centering
145	\small
146	\caption{0-shot accuracy on Qwen2.5-7B at 4$\times$ compression. Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization.}
147	\label{tab:downstream}
148	\begin{tabular}{lcccc}
149	\toprule
150	Task & Baseline & Uniform & MCKP & $\Delta$ vs \\
151	 & (bf16) & (4-bit) & (Ours) & Uniform \\
152	\midrule
153	ARC-C      & ---   & 0.482 & 0.514 & $+$3.2 pts \\
154	HellaSwag  & ---   & 0.728 & 0.768 & $+$4.0 pts \\
155	PIQA       & ---   & 0.766 & 0.779 & $+$1.3 pts \\
156	WinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\
157	\midrule
158	Average    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\
159	\bottomrule
160	\end{tabular}
161	\end{table}
162	
163	Table~\ref{tab:downstream} shows that the PPL improvements transfer to downstream tasks on Qwen2.5-7B.
164	Constrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\ 0.660), with gains on all four benchmarks.
165	The largest gain appears on HellaSwag ($+$4.0 pts), where language modeling quality is most directly reflected.
166	
167	Constrained MCKP recovers approximately 73\% of the accuracy lost by uniform 4-bit quantization, indicating that per-head bit allocation addresses much of the degradation, though a gap to bf16 remains.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "3400b8f0-e77a-4cf9-a189-502cc5a18244"
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
  "task_id": "aa1bc34633d90da83",
  "tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "description": "Reading docs/paper/analysis.tex",
  "usage": {
    "total_tokens": 28663,
    "tool_uses": 6,
    "duration_ms": 5115
  },
  "last_tool_name": "Read",
  "uuid": "0268abf0-17b9-4a4f-964d-0346c7812511",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_014pfFpvbHYSEYdGJE9rSvtk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "22d832db-6140-4c2f-b22e-61947ca564a2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015opkiwFHUVfvnJa5mVASXF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 27291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1355,
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

_source line 27 · 2026-05-14T11:01:49.501Z_

<details><summary>↩ Tool result · `toolu_014pfFpvbHYSEYdGJE9rSvtk`</summary>

```text
1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across three architectures at $4\times$ compression.
12	Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66), with Layer-0 heads contributing the majority of total 2-bit distortion.
13	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.42 PPL, a 27.3\% improvement over uniform 4-bit.
14	Llama-3.1-8B shows moderate heterogeneity (0.34--0.59), and the allocation benefit is marginal ($+$0.36 vs.\ $+$0.38).
15	Mistral-7B-v0.3 has a concentration of 0.42 but near-zero absolute distortion for most heads, leaving the profiler with no reliable signal.
16	Here, constrained MCKP is slightly \emph{worse} than uniform ($+$0.13 vs.\ $+$0.10), confirming that non-uniform allocation is counterproductive when heterogeneity is low.
17	
18	\begin{table}[t]
19	\centering
20	\small
21	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at 4$\times$ compression.}
22	\label{tab:heterogeneity}
23	\begin{tabular}{lccccc}
24	\toprule
25	Model & GQA & Top-5\% & $\Delta$ PPL & $\Delta$ PPL & Recommendation \\
26	 & Ratio & Conc. & (Uniform) & (Ours) & \\
27	\midrule
28	Qwen2.5-7B & 7:1 & 0.59--0.66 & $+$5.64 & $+$1.42 & Non-uniform \\
29	Llama-3.1-8B & 4:1 & 0.34--0.59 & $+$0.38 & $+$0.36 & Marginal \\
30	Mistral-7B-v0.3 & 4:1 & 0.42 & $+$0.10 & $+$0.13 & Uniform \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\begin{figure*}[t]
36	\centering
37	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
38	\caption{Per-head 2-bit quantization sensitivity across three models. Qwen2.5-7B (left) shows high concentration in Layer-0 heads; Llama-3.1-8B (center) shows moderate spread; Mistral-7B-v0.3 (right) shows near-zero sensitivity across all heads. Color intensity indicates PPL increase when the head is quantized to 2-bit.}
39	\label{fig:heatmap}
40	\end{figure*}
41	
42	Figure~\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.
43	The contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Mistral shows uniformly low distortion across all layers and heads.
44	
45	\subsection{Diagnostic Framework}
46	\label{sec:diagnostic}
47	
48	The heterogeneity characterization yields a practical decision procedure for practitioners:
49	
50	\begin{enumerate}[nosep]
51	\item Run per-head profiling as described in \S\ref{sec:profiling}.
52	\item Compute the top-5\% concentration from the resulting distortion table.
53	\item Select allocation strategy:
54	  \begin{itemize}[nosep]
55	  \item Concentration ${>}\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\% PPL improvement).
56	  \item Concentration $0.30$--$0.50$: marginal benefit; depends on target compression ratio (Llama case; 0.2\% at $4\times$).
57	  \item Near-zero absolute distortion for most heads: use uniform directly (Mistral case; non-uniform is counterproductive).
58	  \end{itemize}
59	\end{enumerate}
60	
61	The diagnostic adds no computational overhead: it reuses the profiling data already required for the allocation solver.
62	This avoids wasted optimization effort on architectures where non-uniform allocation provides no benefit.
63	
64	\subsection{Aggressive Compression Amplifies Benefit}
65	\label{sec:aggressive}
66	
67	At $4\times$ compression, Llama and Mistral show minimal benefit from non-uniform allocation.
68	At more aggressive compression ratios, the picture changes.
69	
70	At $5.3\times$ compression (budget ratio 0.1875, average 3 bits), constrained MCKP provides large improvements on both architectures.
71	On Llama, constrained MCKP achieves 57.60 PPL vs.\ uniform 2-bit at 2643.77---a $45\times$ reduction.
72	On Mistral, the gap is comparable: 11.91 vs.\ 519.11 ($44\times$).
73	The consistency of this ratio across architectures ($45\times$ vs.\ $44\times$) indicates that the constrained allocation's protection mechanism is architecture-independent.
74	
75	At $8\times$ compression (budget ratio 0.125), the benefit narrows.
76	Llama: 2372.33 vs.\ 2643.77 (both catastrophic).
77	Mistral: 399.90 vs.\ 519.11 ($1.3\times$ better, but neither is usable).
78	
79	The mechanism is clear: $5.3\times$ compression forces extensive use of 2-bit heads, and constrained allocation protects the sensitive heads from 2-bit assignment.
80	At $4\times$, the budget is generous enough that uniform 4-bit already works well for low-heterogeneity models.
81	At $8\times$, the budget is too constrained for any allocation to preserve quality.
82	The intermediate regime ($5.3\times$) is where constrained allocation provides the largest relative benefit.
83	
84	\subsection{Profiling Resolution}
85	\label{sec:profiling_resolution}
86	
87	We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
88	
89	High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
90	Relative to the bf16 baseline (9.81), this reduces the degradation from 1.42 to 1.10, a 22.5\% reduction.
91	The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
92	
93	The additional signal changes 8 of 112 head assignments.
94	High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
95	
96	\subsection{KV Separation Ablation}
97	\label{sec:kv_separation}
98	
99	We test whether treating K and V caches as independent items in the MCKP solver---allowing different bit-widths for K and V within the same head---improves over joint allocation where K and V share a bit-width.
100	
101	Joint allocation achieves 10.91 PPL; separated K/V allocation achieves 11.22 ($+$0.31 worse).
102	The degradation stems from K-side over-compression: the separated solver doubles the maximum number of 2-bit K items to 16 (vs.\ 8 in the joint formulation), since K and V are counted independently against the cardinality constraint.
103	Meanwhile, V-side distortion is near-zero for most heads, so the solver assigns all V items to 4-bit, concentrating compression entirely on K.
104	
105	Of the 112 heads, 21 show K$\neq$V asymmetry in the separated allocation, all with K receiving a lower bit-width than V.
106	This systematic asymmetry suggests that K caches are inherently more compressible than V caches, consistent with the observation that key vectors primarily encode positional information while value vectors carry content.
107	
108	Joint allocation is sufficient under the current constraint formulation.
109	Separated K/V allocation with per-side cardinality constraints---limiting 2-bit assignments independently for K and V---is a direction for future work.
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "2f57174a-7934-4fb2-b697-9ceb0a54326e"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aa1bc34633d90da83",
  "tool_use_id": "toolu_01WZ9WJ3Vzm1RWepwWtNp6ri",
  "status": "completed",
  "output_file": "",
  "summary": "Read existing paper sections",
  "usage": {
    "total_tokens": 40791,
    "tool_uses": 6,
    "duration_ms": 37595
  },
  "uuid": "1dc32463-c18d-4275-8b58-f80202a03910",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

### Tool result

_source line 29 · 2026-05-14T11:02:21.972Z_

<details><summary>↩ Tool result · `toolu_01WZ9WJ3Vzm1RWepwWtNp6ri`</summary>

```text
Perfect! I've extracted the key claims, numbers, and terminology from the paper. Here's a comprehensive report:

## EXTRACTED KEY CLAIMS, NUMBERS, AND TERMINOLOGY

### **ABSTRACT (abstract.tex)**

**Exact Numbers:**
- Unconstrained greedy: **32.45 PPL** (Qwen2.5-7B, 4× compression)
- Unconstrained MCKP: **36.92 PPL** (Qwen2.5-7B, 4× compression)
- Uniform 4-bit baseline: **15.45 PPL** (Qwen2.5-7B, 4× compression)
- Constrained allocation (OUR METHOD): **11.23 PPL** (Qwen2.5-7B, 4× compression)
- **27.3% reduction** over uniform 4-bit
- Cardinality constraint: **k=8** (7% of heads on Qwen2.5-7B's 112 KV heads)
- Llama-3.1-8B: **8.45 vs 8.47 PPL** (marginal 0.2% improvement)
- Mistral-7B-v0.3: **7.16 vs 7.13 PPL** (slightly counterproductive)
- Heterogeneity diagnostic: top-5% concentration **0.59–0.66** (beneficial, Qwen), **0.34–0.59** (marginal, Llama), **0.42** (counterproductive, Mistral)

**Key Terminology:**
- "2-bit distortion compounding"
- "Per-head mixed-precision quantization"
- "Hardware-aligned bit-widths {2, 4, 8, 16}"
- "Cardinality constraint"
- "Heterogeneity diagnostic"
- "Constrained greedy" and "constrained MCKP"

**Key Claims:**
1. Non-additivity of distortions when many 2-bit heads are used simultaneously
2. Cardinality constraint is "minimal sufficient fix"
3. Constraint makes solver choice irrelevant (identical allocations across solvers)
4. Simple O(H log H) greedy algorithm suffices when constrained

---

### **INTRODUCTION (introduction.tex)**

**Exact Numbers (same as abstract plus context):**
- Qwen2.5-7B at 4× compression: **68–75 heads assigned to 2-bit** (unconstrained)
- Layer-0 distortion on Qwen: L0H0 increases PPL by **31.9%** (9.81→12.94), L0H2 by **23.2%**, L0H3 by **11.7%**
- Additive model predicts **~11 PPL** but actual is **3–4× higher** (32–37 PPL)
- Unconstrained greedy: **32.45 PPL**; MCKP: **36.92 PPL**
- Constrained allocation: **11.23 PPL** with k=8 (7% of 112 heads)
- **27.3% reduction** compared to uniform 4-bit
- Per-head solvers across 3 architectures: **Δ=0.0000** (identical allocations)
- Llama-3.1-8B: **8.45 vs 8.47** (0.2% improvement)
- Mistral-7B-v0.3: **7.16 vs 7.13** (slightly worse)
- Top-5% concentration: Qwen **0.59–0.66**, Llama **0.34–0.59**, Mistral **0.42**

**Key Terminology:**
- "Per-head mixed-precision quantization"
- "Rate-distortion optimization"
- "Polymatroid structure"
- "Multiple-choice knapsack (MCKP)"
- "2-bit distortion compounding"
- "Additive distortion assumption"
- "Head sensitivity heterogeneity"
- "Concentration of per-head distortion"

**Key Claims:**
1. Greedy is optimal for consecutive bit-widths but fails for {2,4,8,16}
2. Root cause is "2-bit distortion compounding," not solver suboptimality
3. Distortion from 2-bit heads compounds **non-additively** through residual stream
4. Single cardinality constraint is sufficient remedy
5. Constraint makes greedy and MCKP equivalent (all 112 heads identical on Qwen, all 256 on Llama, 255/256 on Mistral)
6. Benefit depends on "head sensitivity heterogeneity"

---

### **METHOD (method.tex)**

**Exact Numbers:**
- Bit-widths: **{2, 4, 8, 16}**
- Qwen2.5-7B: **112 KV heads** (28 layers × 4 heads)
- Llama-3.1-8B: **256 KV heads** (32 layers × 8 heads)
- Mistral-7B-v0.3: **256 KV heads** (32 layers × 8 heads)
- Calibration: **64 sequences × 2048 tokens** from WikiText-2 train
- Per-head distortions at 4-bit and above: **typically below 0.1 PPL**
- Unconstrained greedy on Qwen: **68 heads to 2-bit**, achieves **32.45 PPL**
- Unconstrained MCKP on Qwen: **75 heads to 2-bit**, achieves **36.92 PPL**
- Uniform 4-bit baseline: **15.45 PPL**
- Standard-resolution profiling detects non-zero d_h(2) in **37 of 112 heads**
- Layer-0 head examples: L0H0 **31.9%** increase, L0H2 **23.2%**, L0H3 **11.7%**
- Constraint parameter k: **k=8** for Qwen2.5-7B (7% of 112 heads)
- U-shaped curve minimum: k=8 achieves **11.23 PPL**
- At k=75: **35.35 PPL** (compounding effect)
- At k=0 (uniform 4-bit): **15.45 PPL**

**Key Terminology:**
- "Multiple-choice knapsack (MCKP)"
- "Budget ratio R" (e.g., 0.25 for 4× compression)
- "Per-head distortion function d_h(b)"
- "Polymatroid structure"
- "Additive distortion assumption"
- "Cardinality constraint"
- "Compounding effect"
- "Residual stream"

**Key Claims:**
1. Profiling measures PPL increase when head is quantized to each bit-width
2. Additive assumption holds for 4-bit and 8-bit (distortions typically <0.1 PPL)
3. At 2-bit, distortions are "orders of magnitude larger"
4. When many 2-bit heads simultaneously quantize, errors accumulate through residual stream
5. Cardinality constraint is "single linear inequality, compatible with any solver"
6. Layer-0 heads don't require explicit protection—profiler signal is sufficient

---

### **EXPERIMENTS (experiments.tex)**

**Exact Numbers (Main Results Table):**
- **Qwen2.5-7B:**
  - Baseline (bf16): **9.81 PPL**
  - Uniform 4-bit: **15.45 PPL**
  - Unconstrained greedy: **32.45 PPL**
  - Unconstrained MCKP: **36.92 PPL**
  - Ours (constrained): **11.23 PPL** (standard profiling)
  - Hires profiling: **10.91 PPL**

- **Llama-3.1-8B:**
  - Baseline (bf16): **8.09 PPL**
  - Uniform 4-bit: **8.47 PPL**
  - Ours (constrained, hires): **8.45 PPL**

- **Mistral-7B-v0.3:**
  - Baseline (bf16): **7.04 PPL**
  - Uniform 4-bit: **7.13 PPL**
  - Ours (constrained, hires): **7.16 PPL**

**Budget Sweep (Qwen2.5-7B):**
- 2× compression: Uniform **10.10 PPL**, Constrained **10.66 PPL** (−0.56)
- 4× compression: Uniform **15.45 PPL**, Constrained **11.23 PPL** (+4.21)
- 8× compression: Uniform **14,759 PPL**, Constrained **907 PPL** (+13,852 gap)

**Heuristic Baselines (4× compression):**
- **Qwen2.5-7B:** MCKP **11.23**, L0-random median **11.52**, naive positional **12.23**
- **Llama-3.1-8B:** MCKP **8.45**, L0-random median **10.04**, naive positional **9.94**
- **Mistral-7B-v0.3:** MCKP **7.32**, L0-random median **7.59**, naive positional **7.48**

**Downstream Evaluation (Qwen2.5-7B, 4× compression):**
- ARC-Challenge: Uniform **0.482** → MCKP **0.514** (+3.2 pts)
- HellaSwag: Uniform **0.728** → MCKP **0.768** (+4.0 pts)
- PIQA: Uniform **0.766** → MCKP **0.779** (+1.3 pts)
- WinoGrande: Uniform **0.662** → MCKP **0.682** (+2.0 pts)
- Average: **0.660 → 0.686** (+2.6 pts, **73% of accuracy lost by uniform recovered**)

**Key Terminology:**
- "Grouped-query attention (GQA) ratio" (7:1 for Qwen, 4:1 for Llama/Mistral)
- "WikiText-2 test split" (298,938 tokens)
- "0-shot prompting"
- "Unconstrained allocation"
- "Layer-0 protection"

**Key Claims:**
1. On Qwen: constrained MCKP achieves **27.3% reduction** over uniform
2. Unconstrained methods fail "catastrophically"
3. On Llama/Mistral: unconstrained results omitted (only tested on Qwen)
4. Llama shows "low sensitivity heterogeneity"
5. Mistral's sliding-window attention may contribute to uniformity
6. Downstream gains transfer (73% accuracy recovery on downstream tasks)

---

### **ANALYSIS (analysis.tex)**

**Exact Numbers:**

**Heterogeneity Table:**
- **Qwen2.5-7B (7:1 GQA):** Top-5% concentration **0.59–0.66**, Δ PPL uniform **+5.64**, ours **+1.42** (27.3% improvement)
- **Llama-3.1-8B (4:1 GQA):** Top-5% concentration **0.34–0.59**, Δ PPL uniform **+0.38**, ours **+0.36** (marginal)
- **Mistral-7B-v0.3 (4:1 GQA):** Top-5% concentration **0.42**, Δ PPL uniform **+0.10**, ours **+0.13** (counterproductive)

**Aggressive Compression (5.3× compression, 3 bits average):**
- **Llama:** Constrained MCKP **57.60 PPL** vs. uniform 2-bit **2643.77** (**45× reduction**)
- **Mistral:** Constrained **11.91** vs. uniform 2-bit **519.11** (**44× reduction**)
- Consistency ratio: **45× vs 44×** across architectures

**8× Compression:**
- **Llama:** **2372.33 vs 2643.77** (both catastrophic)
- **Mistral:** **399.90 vs 519.11** (1.3× better, neither usable)

**Profiling Resolution:**
- Standard (16 seq × 512 tok): **11.23 PPL**
- High-res (64 seq × 2048 tok): **10.91 PPL** (−0.32 absolute, −1.10 relative to bf16)
- Standard detects non-zero d_h(2) in **37 of 112 heads**
- High-res detects **100 of 112** (2.7× more)
- Changes **8 of 112** head assignments

**K/V Separation Ablation:**
- Joint allocation: **10.91 PPL**
- Separated K/V: **11.22 PPL** (+0.31 worse)
- Heads with K≠V asymmetry: **21 of 112**
- All asymmetries: K receiving lower bit-width than V

**Key Terminology:**
- "Top-5% concentration metric"
- "Head sensitivity heterogeneity"
- "Per-head 2-bit distortions d_h(2)"
- "Layer-0 concentration"
- "Protection mechanism"
- "Diagnostic framework"
- "K cache" vs "V cache" (key vs value)

**Key Claims:**
1. High heterogeneity (>0.50) → non-uniform beneficial (27.3% Qwen)
2. Moderate (0.30–0.50) → marginal (0.2% Llama)
3. Low/near-zero → counterproductive (Mistral)
4. Diagnostic adds "no computational overhead"
5. At 5.3× compression, constraint provides "large improvements" (45–44× better)
6. At 4×: budget generous enough for low-heterogeneity models
7. At 8×: budget too constrained for any allocation
8. High-res profiling detects 2.7× more heads with non-zero distortion
9. K caches more compressible than V (K encodes position, V carries content)

---

## SUMMARY FOR CONCLUSION CONSISTENCY CHECK

**Critical Numbers to Maintain Consistency:**
- Main result: **11.23 PPL** (Qwen, 4×, constrained)
- Improvement: **27.3%** over uniform 4-bit (**15.45 PPL**)
- Unconstrained failure: **32.45 (greedy)** and **36.92 (MCKP) PPL**
- Cardinality constraint: **k≤8** (7% of 112 heads)
- Solver equivalence: **Δ=0.0000** exact match across architectures
- Downstream recovery: **73%** of accuracy lost

**Critical Terminology to Use Consistently:**
- "2-bit distortion compounding" (the core problem)
- "Cardinality constraint on 2-bit assignments" (the fix)
- "Per-head mixed-precision quantization"
- "Hardware-aligned bit-widths {2,4,8,16}"
- "Heterogeneity diagnostic" (top-5% concentration metric)
- "Architectures tested" (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3)

This comprehensive extraction should help ensure your Conclusion section aligns with all claims, numbers, and terminology throughout the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "71c3cb6a-39a2-4d8f-87b1-ff36e62e937b",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following files to extract key claims, numbers, and terminology used in the paper so far. I need to ensure the Conclusion section is consistent with them.\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/ — list all files in this directory\n2. Read the abstract and introduction files if they exist (likely abstract.tex, introduction.tex or similar)\n3. Read any results/experiments section if it exists\n\nFor each file, extract:\n- Exact numbers cited (percentages, improvements, specific values)\n- Key terminology and how concepts are named\n- Any claims about the method\n\nReport all findings in detail.",
    "agentId": "aa1bc34633d90da83",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I've extracted the key claims, numbers, and terminology from the paper. Here's a comprehensive report:\n\n## EXTRACTED KEY CLAIMS, NUMBERS, AND TERMINOLOGY\n\n### **ABSTRACT (abstract.tex)**\n\n**Exact Numbers:**\n- Unconstrained greedy: **32.45 PPL** (Qwen2.5-7B, 4× compression)\n- Unconstrained MCKP: **36.92 PPL** (Qwen2.5-7B, 4× compression)\n- Uniform 4-bit baseline: **15.45 PPL** (Qwen2.5-7B, 4× compression)\n- Constrained allocation (OUR METHOD): **11.23 PPL** (Qwen2.5-7B, 4× compression)\n- **27.3% reduction** over uniform 4-bit\n- Cardinality constraint: **k=8** (7% of heads on Qwen2.5-7B's 112 KV heads)\n- Llama-3.1-8B: **8.45 vs 8.47 PPL** (marginal 0.2% improvement)\n- Mistral-7B-v0.3: **7.16 vs 7.13 PPL** (slightly counterproductive)\n- Heterogeneity diagnostic: top-5% concentration **0.59–0.66** (beneficial, Qwen), **0.34–0.59** (marginal, Llama), **0.42** (counterproductive, Mistral)\n\n**Key Terminology:**\n- \"2-bit distortion compounding\"\n- \"Per-head mixed-precision quantization\"\n- \"Hardware-aligned bit-widths {2, 4, 8, 16}\"\n- \"Cardinality constraint\"\n- \"Heterogeneity diagnostic\"\n- \"Constrained greedy\" and \"constrained MCKP\"\n\n**Key Claims:**\n1. Non-additivity of distortions when many 2-bit heads are used simultaneously\n2. Cardinality constraint is \"minimal sufficient fix\"\n3. Constraint makes solver choice irrelevant (identical allocations across solvers)\n4. Simple O(H log H) greedy algorithm suffices when constrained\n\n---\n\n### **INTRODUCTION (introduction.tex)**\n\n**Exact Numbers (same as abstract plus context):**\n- Qwen2.5-7B at 4× compression: **68–75 heads assigned to 2-bit** (unconstrained)\n- Layer-0 distortion on Qwen: L0H0 increases PPL by **31.9%** (9.81→12.94), L0H2 by **23.2%**, L0H3 by **11.7%**\n- Additive model predicts **~11 PPL** but actual is **3–4× higher** (32–37 PPL)\n- Unconstrained greedy: **32.45 PPL**; MCKP: **36.92 PPL**\n- Constrained allocation: **11.23 PPL** with k=8 (7% of 112 heads)\n- **27.3% reduction** compared to uniform 4-bit\n- Per-head solvers across 3 architectures: **Δ=0.0000** (identical allocations)\n- Llama-3.1-8B: **8.45 vs 8.47** (0.2% improvement)\n- Mistral-7B-v0.3: **7.16 vs 7.13** (slightly worse)\n- Top-5% concentration: Qwen **0.59–0.66**, Llama **0.34–0.59**, Mistral **0.42**\n\n**Key Terminology:**\n- \"Per-head mixed-precision quantization\"\n- \"Rate-distortion optimization\"\n- \"Polymatroid structure\"\n- \"Multiple-choice knapsack (MCKP)\"\n- \"2-bit distortion compounding\"\n- \"Additive distortion assumption\"\n- \"Head sensitivity heterogeneity\"\n- \"Concentration of per-head distortion\"\n\n**Key Claims:**\n1. Greedy is optimal for consecutive bit-widths but fails for {2,4,8,16}\n2. Root cause is \"2-bit distortion compounding,\" not solver suboptimality\n3. Distortion from 2-bit heads compounds **non-additively** through residual stream\n4. Single cardinality constraint is sufficient remedy\n5. Constraint makes greedy and MCKP equivalent (all 112 heads identical on Qwen, all 256 on Llama, 255/256 on Mistral)\n6. Benefit depends on \"head sensitivity heterogeneity\"\n\n---\n\n### **METHOD (method.tex)**\n\n**Exact Numbers:**\n- Bit-widths: **{2, 4, 8, 16}**\n- Qwen2.5-7B: **112 KV heads** (28 layers × 4 heads)\n- Llama-3.1-8B: **256 KV heads** (32 layers × 8 heads)\n- Mistral-7B-v0.3: **256 KV heads** (32 layers × 8 heads)\n- Calibration: **64 sequences × 2048 tokens** from WikiText-2 train\n- Per-head distortions at 4-bit and above: **typically below 0.1 PPL**\n- Unconstrained greedy on Qwen: **68 heads to 2-bit**, achieves **32.45 PPL**\n- Unconstrained MCKP on Qwen: **75 heads to 2-bit**, achieves **36.92 PPL**\n- Uniform 4-bit baseline: **15.45 PPL**\n- Standard-resolution profiling detects non-zero d_h(2) in **37 of 112 heads**\n- Layer-0 head examples: L0H0 **31.9%** increase, L0H2 **23.2%**, L0H3 **11.7%**\n- Constraint parameter k: **k=8** for Qwen2.5-7B (7% of 112 heads)\n- U-shaped curve minimum: k=8 achieves **11.23 PPL**\n- At k=75: **35.35 PPL** (compounding effect)\n- At k=0 (uniform 4-bit): **15.45 PPL**\n\n**Key Terminology:**\n- \"Multiple-choice knapsack (MCKP)\"\n- \"Budget ratio R\" (e.g., 0.25 for 4× compression)\n- \"Per-head distortion function d_h(b)\"\n- \"Polymatroid structure\"\n- \"Additive distortion assumption\"\n- \"Cardinality constraint\"\n- \"Compounding effect\"\n- \"Residual stream\"\n\n**Key Claims:**\n1. Profiling measures PPL increase when head is quantized to each bit-width\n2. Additive assumption holds for 4-bit and 8-bit (distortions typically <0.1 PPL)\n3. At 2-bit, distortions are \"orders of magnitude larger\"\n4. When many 2-bit heads simultaneously quantize, errors accumulate through residual stream\n5. Cardinality constraint is \"single linear inequality, compatible with any solver\"\n6. Layer-0 heads don't require explicit protection—profiler signal is sufficient\n\n---\n\n### **EXPERIMENTS (experiments.tex)**\n\n**Exact Numbers (Main Results Table):**\n- **Qwen2.5-7B:**\n  - Baseline (bf16): **9.81 PPL**\n  - Uniform 4-bit: **15.45 PPL**\n  - Unconstrained greedy: **32.45 PPL**\n  - Unconstrained MCKP: **36.92 PPL**\n  - Ours (constrained): **11.23 PPL** (standard profiling)\n  - Hires profiling: **10.91 PPL**\n\n- **Llama-3.1-8B:**\n  - Baseline (bf16): **8.09 PPL**\n  - Uniform 4-bit: **8.47 PPL**\n  - Ours (constrained, hires): **8.45 PPL**\n\n- **Mistral-7B-v0.3:**\n  - Baseline (bf16): **7.04 PPL**\n  - Uniform 4-bit: **7.13 PPL**\n  - Ours (constrained, hires): **7.16 PPL**\n\n**Budget Sweep (Qwen2.5-7B):**\n- 2× compression: Uniform **10.10 PPL**, Constrained **10.66 PPL** (−0.56)\n- 4× compression: Uniform **15.45 PPL**, Constrained **11.23 PPL** (+4.21)\n- 8× compression: Uniform **14,759 PPL**, Constrained **907 PPL** (+13,852 gap)\n\n**Heuristic Baselines (4× compression):**\n- **Qwen2.5-7B:** MCKP **11.23**, L0-random median **11.52**, naive positional **12.23**\n- **Llama-3.1-8B:** MCKP **8.45**, L0-random median **10.04**, naive positional **9.94**\n- **Mistral-7B-v0.3:** MCKP **7.32**, L0-random median **7.59**, naive positional **7.48**\n\n**Downstream Evaluation (Qwen2.5-7B, 4× compression):**\n- ARC-Challenge: Uniform **0.482** → MCKP **0.514** (+3.2 pts)\n- HellaSwag: Uniform **0.728** → MCKP **0.768** (+4.0 pts)\n- PIQA: Uniform **0.766** → MCKP **0.779** (+1.3 pts)\n- WinoGrande: Uniform **0.662** → MCKP **0.682** (+2.0 pts)\n- Average: **0.660 → 0.686** (+2.6 pts, **73% of accuracy lost by uniform recovered**)\n\n**Key Terminology:**\n- \"Grouped-query attention (GQA) ratio\" (7:1 for Qwen, 4:1 for Llama/Mistral)\n- \"WikiText-2 test split\" (298,938 tokens)\n- \"0-shot prompting\"\n- \"Unconstrained allocation\"\n- \"Layer-0 protection\"\n\n**Key Claims:**\n1. On Qwen: constrained MCKP achieves **27.3% reduction** over uniform\n2. Unconstrained methods fail \"catastrophically\"\n3. On Llama/Mistral: unconstrained results omitted (only tested on Qwen)\n4. Llama shows \"low sensitivity heterogeneity\"\n5. Mistral's sliding-window attention may contribute to uniformity\n6. Downstream gains transfer (73% accuracy recovery on downstream tasks)\n\n---\n\n### **ANALYSIS (analysis.tex)**\n\n**Exact Numbers:**\n\n**Heterogeneity Table:**\n- **Qwen2.5-7B (7:1 GQA):** Top-5% concentration **0.59–0.66**, Δ PPL uniform **+5.64**, ours **+1.42** (27.3% improvement)\n- **Llama-3.1-8B (4:1 GQA):** Top-5% concentration **0.34–0.59**, Δ PPL uniform **+0.38**, ours **+0.36** (marginal)\n- **Mistral-7B-v0.3 (4:1 GQA):** Top-5% concentration **0.42**, Δ PPL uniform **+0.10**, ours **+0.13** (counterproductive)\n\n**Aggressive Compression (5.3× compression, 3 bits average):**\n- **Llama:** Constrained MCKP **57.60 PPL** vs. uniform 2-bit **2643.77** (**45× reduction**)\n- **Mistral:** Constrained **11.91** vs. uniform 2-bit **519.11** (**44× reduction**)\n- Consistency ratio: **45× vs 44×** across architectures\n\n**8× Compression:**\n- **Llama:** **2372.33 vs 2643.77** (both catastrophic)\n- **Mistral:** **399.90 vs 519.11** (1.3× better, neither usable)\n\n**Profiling Resolution:**\n- Standard (16 seq × 512 tok): **11.23 PPL**\n- High-res (64 seq × 2048 tok): **10.91 PPL** (−0.32 absolute, −1.10 relative to bf16)\n- Standard detects non-zero d_h(2) in **37 of 112 heads**\n- High-res detects **100 of 112** (2.7× more)\n- Changes **8 of 112** head assignments\n\n**K/V Separation Ablation:**\n- Joint allocation: **10.91 PPL**\n- Separated K/V: **11.22 PPL** (+0.31 worse)\n- Heads with K≠V asymmetry: **21 of 112**\n- All asymmetries: K receiving lower bit-width than V\n\n**Key Terminology:**\n- \"Top-5% concentration metric\"\n- \"Head sensitivity heterogeneity\"\n- \"Per-head 2-bit distortions d_h(2)\"\n- \"Layer-0 concentration\"\n- \"Protection mechanism\"\n- \"Diagnostic framework\"\n- \"K cache\" vs \"V cache\" (key vs value)\n\n**Key Claims:**\n1. High heterogeneity (>0.50) → non-uniform beneficial (27.3% Qwen)\n2. Moderate (0.30–0.50) → marginal (0.2% Llama)\n3. Low/near-zero → counterproductive (Mistral)\n4. Diagnostic adds \"no computational overhead\"\n5. At 5.3× compression, constraint provides \"large improvements\" (45–44× better)\n6. At 4×: budget generous enough for low-heterogeneity models\n7. At 8×: budget too constrained for any allocation\n8. High-res profiling detects 2.7× more heads with non-zero distortion\n9. K caches more compressible than V (K encodes position, V carries content)\n\n---\n\n## SUMMARY FOR CONCLUSION CONSISTENCY CHECK\n\n**Critical Numbers to Maintain Consistency:**\n- Main result: **11.23 PPL** (Qwen, 4×, constrained)\n- Improvement: **27.3%** over uniform 4-bit (**15.45 PPL**)\n- Unconstrained failure: **32.45 (greedy)** and **36.92 (MCKP) PPL**\n- Cardinality constraint: **k≤8** (7% of 112 heads)\n- Solver equivalence: **Δ=0.0000** exact match across architectures\n- Downstream recovery: **73%** of accuracy lost\n\n**Critical Terminology to Use Consistently:**\n- \"2-bit distortion compounding\" (the core problem)\n- \"Cardinality constraint on 2-bit assignments\" (the fix)\n- \"Per-head mixed-precision quantization\"\n- \"Hardware-aligned bit-widths {2,4,8,16}\"\n- \"Heterogeneity diagnostic\" (top-5% concentration metric)\n- \"Architectures tested\" (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3)\n\nThis comprehensive extraction should help ensure your Conclusion section aligns with all claims, numbers, and terminology throughout the paper."
      }
    ],
    "totalDurationMs": 37597,
    "totalTokens": 44714,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 12126,
      "cache_read_input_tokens": 28646,
      "output_tokens": 3936,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12126
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 3936,
          "cache_read_input_tokens": 28646,
          "cache_creation_input_tokens": 12126,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12126,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 5,
      "searchCount": 0,
      "bashCount": 1,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the Conclusion section. Key points to ensure consistency:

1. Numbers: 11.23 vs 15.45 (27.3%), Δ=0.0000, 8.45 vs 8.47 (Llama), 7.16 vs 7.13 (Mistral), top-5% concentration: Qwen 0.59-0.66, Llama 0.34-0.59, Mistral 0.42


2. Terminology: cardinality constraint, hardware-aligned bit-widths {2,4,8,16}, per-head mixed-precision quantization, 2-bit distortion compounding, heterogeneity diagnostic, top-5% concentration
3. Avoid: "significantly", "state-of-the-art", "consistently outperforms"
4. EMNLP requires Limitations section — but in this case the task says to include it within Conclusion

I also need to verify: the downstream recovery was 73% of accuracy lost by uniform, and the constraint parameter k=8 (7% of 112 heads). Now I'll draft the conclusion with around 350 words, making sure to weave in the limitations naturally and maintain technical precision throughout. The constraint limits 2-bit heads to at most 8 across all three models, which dramatically improves perplexity on Qwen2.5-7B while making solver choice irrelevant—greedy and MCKP produce identical results, so a simple greedy algorithm suffices. The gains from non-uniform allocation correlate directly with head sensitivity heterogeneity: Qwen2.5-7B shows substantial improvement, Llama-3.1-8B shows marginal gains, and Mistral-7B-v0.3 shows essentially no benefit.

I can compute a diagnostic metric from the same profiling pass that tells practitioners upfront whether non-uniform quantization is worth deploying for their model. However, I'm limited by evaluating only three 7B models—not enough to establish a robust statistical relationship between heterogeneity and quantization gains. I've also relied on a single sensitivity measure based on perplexity-based per-head distortion, leaving other approaches like gradient-based diagnostics unexplored. My evaluation focuses on perplexity and downstream accuracy without measuring actual runtime or latency improvements, so the practical speedup remains unclear. I haven't tested whether these findings generalize to larger model scales either.

For future work, I'd want to scale up to 70B+ models to see if the heterogeneity-benefit relationship holds, explore per-side cardinality constraints beyond the joint allocation approach I tested, and integrate with production inference engines to measure real latency. Dynamic per-request allocation that adapts bit-widths based on input characteristics at serving time could also push this beyond static profiling. I'm verifying the output file path is accessible.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "e0e6347b-a3f6-40e4-bb24-711ef03d8ddb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCUDUipRS7RasV35jcJsns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9743,
      "cache_read_input_tokens": 23735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9743
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

_source line 31_

Now I have all the numbers and terminology. Let me check the output directory exists and write the conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "e32621e9-2b67-4e4e-aed7-0a28ca361f1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCUDUipRS7RasV35jcJsns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9743,
      "cache_read_input_tokens": 23735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9743
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

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01N8BMt68Ttp7aWnSW1q7EYF`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/",
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
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "d03ba703-1dc4-4fd8-81a5-5954cbd783d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCUDUipRS7RasV35jcJsns",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9743,
      "cache_read_input_tokens": 23735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9743
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

_source line 33 · 2026-05-14T11:02:57.249Z_

<details><summary>↩ Tool result · `toolu_01N8BMt68Ttp7aWnSW1q7EYF`</summary>

```text
abstract.tex
acl.sty
acl_natbib.bst
analysis.tex
experiments.tex
figures
introduction.tex
method.tex
references.bib
references.bib.prev
related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "06b09e89-39ee-4973-9018-644b3ff444f6",
  "tool_use_result": {
    "stdout": "abstract.tex\nacl.sty\nacl_natbib.bst\nanalysis.tex\nexperiments.tex\nfigures\nintroduction.tex\nmethod.tex\nreferences.bib\nreferences.bib.prev\nrelated_work.tex",
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

_source line 34_

<details open><summary>🔧 Tool call — Write · `toolu_01RDPVZvcaPtGvevVto68W5r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
  "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.\nA single constraint---limiting simultaneously active 2-bit heads to $k \\leq 8$ (7\\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\\% improvement at $4\\times$ compression.\nUnder the constraint, solver choice becomes irrelevant: greedy and MCKP produce identical allocations across all three architectures ($\\Delta = 0.0000$), so a simple $O(H \\log H)$ greedy algorithm suffices.\nThe benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) shows no benefit (7.16 vs.\\ 7.13 PPL).\nThis diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile for a given model.\n\n\\paragraph{Limitations.}\nOur study has several limitations that temper the generality of the findings.\nFirst, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.\nSecond, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.\nThird, we report perplexity and downstream accuracy but no runtime or latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.\nFourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.\nFinally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).\n\n\\paragraph{Future Work.}\nExtending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.\nOur K/V separation ablation (\\S\\ref{sec:kv-separation}) showed that joint allocation outperforms independent K and V budgets under a shared cardinality constraint; investigating \\emph{per-side} cardinality constraints is a natural next step.\nIntegration with production inference engines such as vLLM and TensorRT-LLM would enable latency measurement and expose hardware-specific trade-offs in mixed-precision decoding.\nFinally, dynamic per-request allocation---adapting bit-width assignments based on input characteristics at serving time---could extend the framework beyond static profiling.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "35d4870d-5eec-4d48-854f-66ee13940465",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PLSXqb5fjs5JfsaPartw1P",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1566,
      "cache_read_input_tokens": 33478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1566
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

### Runtime record

_source line 35_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1778796000,
    "rateLimitType": "seven_day",
    "utilization": 0.77,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "9baf00b0-86d9-491c-9222-dea496cfbfc3",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8"
}
```

---

### Tool result

_source line 36 · 2026-05-14T11:03:10.178Z_

<details><summary>↩ Tool result · `toolu_01RDPVZvcaPtGvevVto68W5r`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "bbefad23-aeea-497e-a5cf-f6352e0a5bfc",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex",
    "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe showed that per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \\{2, 4, 8, 16\\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding through the residual stream.\nA single constraint---limiting simultaneously active 2-bit heads to $k \\leq 8$ (7\\% of heads)---reduces perplexity on Qwen2.5-7B from 15.45 (uniform 4-bit) to 11.23, a 27.3\\% improvement at $4\\times$ compression.\nUnder the constraint, solver choice becomes irrelevant: greedy and MCKP produce identical allocations across all three architectures ($\\Delta = 0.0000$), so a simple $O(H \\log H)$ greedy algorithm suffices.\nThe benefit of non-uniform allocation scales with head sensitivity heterogeneity, as measured by the top-5\\% concentration diagnostic: Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs.\\ 8.47 PPL), and Mistral-7B-v0.3 (0.42) shows no benefit (7.16 vs.\\ 7.13 PPL).\nThis diagnostic, computable from the same profiling pass used for allocation, lets practitioners decide \\emph{before deployment} whether non-uniform quantization is worthwhile for a given model.\n\n\\paragraph{Limitations.}\nOur study has several limitations that temper the generality of the findings.\nFirst, we evaluate only three 7B-scale models---too few to establish a statistically robust correlation between heterogeneity and quantization benefit; the observed trend is directional evidence, not a predictive law.\nSecond, profiling relies on a single sensitivity metric (perplexity-based per-head distortion); alternative measures such as gradient-based or activation-norm diagnostics remain unexplored and could yield different allocation decisions.\nThird, we report perplexity and downstream accuracy but no runtime or latency benchmarks, leaving the practical inference speedup from mixed-precision allocation unquantified.\nFourth, we have not verified whether these findings transfer to larger scales (70B+), where head counts and attention patterns differ substantially.\nFinally, although we validate on four downstream tasks, profiling and primary evaluation use a single dataset (WikiText-2).\n\n\\paragraph{Future Work.}\nExtending evaluation to 70B+ models would test whether the heterogeneity--benefit relationship holds at scale.\nOur K/V separation ablation (\\S\\ref{sec:kv-separation}) showed that joint allocation outperforms independent K and V budgets under a shared cardinality constraint; investigating \\emph{per-side} cardinality constraints is a natural next step.\nIntegration with production inference engines such as vLLM and TensorRT-LLM would enable latency measurement and expose hardware-specific trade-offs in mixed-precision decoding.\nFinally, dynamic per-request allocation---adapting bit-width assignments based on input characteristics at serving time---could extend the framework beyond static profiling.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 37_

写入完成。`conclusion.tex` 约 360 words，三部分结构：Summary (~155 words) 覆盖 cardinality constraint、solver equivalence、heterogeneity diagnostic；Limitations (~110 words) 诚实列举 n=3、单一 profiling metric、无 latency benchmark、未验证 70B+、WikiText-2 单数据集；Future Work (~95 words) 覆盖大模型扩展、per-side K/V constraint、推理引擎集成、dynamic allocation。所有数字与 abstract/introduction/experiments 完全一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "uuid": "1ede825d-0017-4f0b-8547-5a9a6d7251f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MsSGUziorS9pVoUd5EpWRq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 911,
      "cache_read_input_tokens": 35044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 911
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

_source line 38_

写入完成。`conclusion.tex` 约 360 words，三部分结构：Summary (~155 words) 覆盖 cardinality constraint、solver equivalence、heterogeneity diagnostic；Limitations (~110 words) 诚实列举 n=3、单一 profiling metric、无 latency benchmark、未验证 70B+、WikiText-2 单数据集；Future Work (~95 words) 覆盖大模型扩展、per-side K/V constraint、推理引擎集成、dynamic allocation。所有数字与 abstract/introduction/experiments 完全一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 101823,
  "duration_api_ms": 102510,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "78296db8-68a5-4938-ae8f-5ba39ba9e5c8",
  "total_cost_usd": 0.35406020000000005,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 24114,
    "cache_read_input_tokens": 104098,
    "output_tokens": 2841,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 24114,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 157,
        "cache_read_input_tokens": 35044,
        "cache_creation_input_tokens": 911,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 911
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1375,
      "outputTokens": 4463,
      "cacheReadInputTokens": 55937,
      "cacheCreationInputTokens": 40772,
      "webSearchRequests": 0,
      "costUSD": 0.0802487,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 2841,
      "cacheReadInputTokens": 104098,
      "cacheCreationInputTokens": 24114,
      "webSearchRequests": 0,
      "costUSD": 0.27381150000000004,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ab6095d8-2c0b-431b-bfb8-99304a2db3ab"
}
```

</details>

---
