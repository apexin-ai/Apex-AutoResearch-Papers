# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_paper_writing_20260516T024157.log`
- **Structured JSON:** [`a134d211a82558bd2b5f.json`](../../sessions/a1/a134d211a82558bd2b5f.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
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
  "uuid": "0bf69bee-dec6-4bf9-b1f2-cdcf825c7205",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1778904000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "11457d27-22b2-4b99-a1c6-10f9412392b3",
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d"
}
```

---

### Assistant

_source line 4_

I'll start by reading the required skill files and the experiments.tex for context consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "33195732-65b1-4af0-a02c-82d38ba4f896",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HszTtooXiCXPj49kdppvqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12782,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12782
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

<details open><summary>🔧 Tool call — Read · `toolu_01UtNVCZNbJevT3BvQiBtYJQ`</summary>

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
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "d412ba05-0dd1-4d5a-b52a-bd2cfc97f8a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HszTtooXiCXPj49kdppvqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12782,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12782
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

_source line 6 · 2026-05-16T02:42:09.830Z_

<details><summary>↩ Tool result · `toolu_01UtNVCZNbJevT3BvQiBtYJQ`</summary>

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
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "e3189961-bcc8-473d-8c00-c155b40aaf3e",
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

<details open><summary>🔧 Tool call — Read · `toolu_01GZYf5NudyHHAYH1F3NNh24`</summary>

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
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "c6e8cb13-c394-437f-b805-4a23a33b909d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HszTtooXiCXPj49kdppvqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12782,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12782
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

_source line 8 · 2026-05-16T02:42:13.212Z_

<details><summary>↩ Tool result · `toolu_01GZYf5NudyHHAYH1F3NNh24`</summary>

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
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "ec51161b-d489-4874-8e28-fc552eed36ca",
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

<details open><summary>🔧 Tool call — Read · `toolu_01RJ5MzLfFbmwxUu1kSVxsYG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "b73c7f45-2f74-4d6a-a229-17a3d32d9dfa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HszTtooXiCXPj49kdppvqS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12782,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12782
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

_source line 10 · 2026-05-16T02:42:13.326Z_

<details><summary>↩ Tool result · `toolu_01RJ5MzLfFbmwxUu1kSVxsYG`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Benchmark and model.}
8	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
9	We use OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.
10	
11	\paragraph{Representation sources.}
12	We extract representations from five sources:
13	(a)~\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;
14	(b)~\textbf{LLM image\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;
15	(c)~\textbf{LLM last\_preaction}---the final token position before action decoding (readout token) at each LLM layer;
16	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token}; and
17	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean}.
18	Sources (d) and (e) serve as external baselines with no VLA training signal.
19	
20	\paragraph{Experimental conditions.}
21	We use a $2 \times 2$ factorial design crossing \emph{training status} (trained vs.\ untrained) with \emph{instruction presence} (with vs.\ without language instruction).
22	The untrained control applies \texttt{from\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.
23	
24	\paragraph{Representational Similarity Analysis (RSA).}
25	Following~\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.
26	We report Spearman rank correlation $\rho$ between representation and action RDMs, with 95\% confidence intervals from 10{,}000 bootstrap resamples.
27	
28	\paragraph{Functional probes.}
29	We train MLP probes (input $\to$ 256 $\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\cite{alain2017}. We report mean $R^2$ across action dimensions.
30	
31	%------------------------------------------------------------------
32	\subsection{Vision Encoder Dominance}
33	\label{sec:vision_dominance}
34	
35	This experiment tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations.
36	
37	Table~\ref{tab:rsa_overview} reports RSA $\rho$ between each representation source and the action space.
38	The SigLIP+Projector output achieves the highest alignment ($\rho = 0.615$, 95\% CI $[0.526, 0.695]$), followed by CLIP ViT-L/14 ($\rho = 0.557$, $[0.442, 0.660]$).
39	Both vision-language pretrained encoders substantially exceed DINOv2 ($\rho = 0.388$), a vision-only model.
40	The VLA's LLM layers (best image\_mean: $\rho = 0.501$ trained, $\rho = 0.485$ untrained) fall between VL-pretrained encoders and DINOv2 (Figure~\ref{fig:rsa_bar}).
41	
42	Three findings emerge.
43	First, VL pretraining---not LLM processing---is the primary source of action-relevant structure.
44	SigLIP and CLIP, both pretrained on image-text pairs, achieve $\rho \geq 0.557$, while DINOv2, pretrained with self-supervised vision objectives alone, reaches only $\rho = 0.388$.
45	This 0.169-point gap indicates that language-grounded visual features carry substantially more action-relevant geometry than features learned without language, consistent with behavioral evidence of visual dominance in VLA policies~\cite{grant2026}.
46	
47	Second, the MLP projector provides incremental alignment: SigLIP+Projector ($0.615$) exceeds CLIP ($0.557$) by $\Delta = 0.058$, consistent with the projector mapping vision features into the LLM's embedding space.
48	
49	Third, the LLM degrades rather than enhances vision encoder geometry.
50	Processing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\_mean), a drop of $\Delta = 0.114$.
51	
52	\paragraph{Geometric-functional dissociation.}
53	Functional probes reveal a dissociation between geometric similarity and functional decodability.
54	DINOv2 achieves $R^2 = 0.712$, statistically indistinguishable from SigLIP+Projector ($R^2 = 0.706$, $p = 0.22$, n.s.), despite its substantially lower RSA ($0.388$ vs.\ $0.615$).
55	This dissociation extends to the VL-pretrained encoders: in a within-experiment comparison,\footnote{CLIP and DINOv2 probes use matched training protocols; absolute $R^2$ values differ from the projector/LLM probes due to separate probe code, so cross-experiment comparisons of raw $R^2$ are not valid.} CLIP achieves $R^2 = 0.805$, indistinguishable from DINOv2 ($R^2 = 0.814$, $p = 0.10$, n.s.)---yet CLIP's RSA ($0.557$) far exceeds DINOv2's ($0.388$).
56	VL pretraining thus provides geometric alignment with the action space, not additional predictive content.
57	
58	\paragraph{Metric sensitivity.}
59	This dissociation extends to alternative similarity metrics.
60	Linear CKA~\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\ref{fig:metric_comparison}).
61	RDM kernel CKA restores the RSA-consistent ranking (Proj $>$ Trained $>$ Untrained $>$ DINOv2).
62	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.
63	
64	\begin{table}[t]
65	\centering
66	\caption{RSA between representation and action RDMs ($\rho$ $\uparrow$). VL-pretrained encoders (SigLIP, CLIP) dominate over vision-only DINOv2 and LLM-processed representations. 95\% CIs from 10{,}000 bootstrap resamples.}
67	\label{tab:rsa_overview}
68	\small
69	\begin{tabular}{llcc}
70	\toprule
71	Source & Aggregation & RSA $\rho$ & 95\% CI \\
72	\midrule
73	SigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\
74	CLIP ViT-L/14 & patch\_mean & 0.557 & {[0.442, 0.660]} \\
75	\midrule
76	VLA Trained w/ inst. & image\_mean & 0.501 & --- \\
77	VLA Trained no inst. & image\_mean & 0.501 & --- \\
78	VLA Untrained w/ inst. & image\_mean & 0.485 & --- \\
79	VLA Untrained no inst. & image\_mean & 0.482 & --- \\
80	\midrule
81	DINOv2 ViT-L/14 & cls\_token & 0.388 & --- \\
82	\bottomrule
83	\end{tabular}
84	\end{table}
85	
86	\begin{figure}[t]
87	\centering
88	\includegraphics[width=\columnwidth]{figures/fig2.pdf}
89	\caption{RSA with the action space ($\rho$) across representation sources. VL-pretrained encoders (SigLIP $\rho{=}0.615$, CLIP $\rho{=}0.557$) substantially exceed both LLM-processed representations ($\rho \leq 0.501$) and vision-only DINOv2 ($\rho{=}0.388$). Hatched bars indicate no-instruction conditions. Error bars: 95\% bootstrap CIs. Dashed line: DINOv2 reference.}
90	\label{fig:rsa_bar}
91	\end{figure}
92	
93	%------------------------------------------------------------------
94	\subsection{LLM Redistributes, Does Not Enhance, Action Structure}
95	\label{sec:llm_redistribution}
96	
97	This experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.
98	Table~\ref{tab:probes} reports functional probe $R^2$ for key representation sources.
99	Two complementary effects characterize LLM processing.
100	
101	\paragraph{Distributed degradation.}
102	Averaging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.
103	RSA drops from $0.615$ to $0.501$ ($\Delta = 0.114$); probe $R^2$ drops from $0.706$ to $0.683$ (95\% CI of $\Delta$: $[0.011, 0.037]$, $p = 0.001$).
104	Figure~\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.
105	
106	\paragraph{Readout concentration.}
107	While distributed image tokens lose information, the last pre-action token (\texttt{last\_preaction}) concentrates action-relevant information beyond the projector baseline.
108	Trained readout achieves $R^2 = 0.731$, exceeding SigLIP+Projector ($R^2 = 0.706$, $p = 0.001$; Figure~\ref{fig:probe_bars}).
109	This concentration is training-dependent: untrained readout ($R^2 = 0.686$) falls below the projector baseline, while trained readout ($0.731$) substantially exceeds it ($\Delta = 0.045$, $p < 0.0001$).
110	
111	Together, these results characterize the LLM as a \emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\cite{haon2025}.
112	
113	\begin{table}[t]
114	\centering
115	\caption{Functional probe $R^2$ ($\uparrow$) for action prediction from frozen representations. The LLM degrades distributed representations (image\_mean) relative to the projector but concentrates superior action information at the readout token---an effect that requires training. DINOv2 matches the projector in $R^2$ despite much lower RSA.}
116	\label{tab:probes}
117	\small
118	\begin{tabular}{lcc}
119	\toprule
120	Representation & $R^2$ & $p$ vs.\ Proj. \\
121	\midrule
122	SigLIP+Projector & 0.706 & --- \\
123	VLA Trained image\_mean (L19) & 0.683 & 0.001 \\
124	VLA Trained readout (L19) & \textbf{0.731} & 0.001 \\
125	VLA Untrained readout (L32) & 0.686 & --- \\
126	DINOv2 cls\_token & 0.712 & 0.220 (n.s.) \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=\columnwidth]{figures/fig3.pdf}
134	\caption{Per-layer RSA ($\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: SigLIP+Projector ($\rho{=}0.615$) and DINOv2 ($\rho{=}0.388$) reference levels.}
135	\label{fig:layer_curves}
136	\end{figure}
137	
138	\begin{figure}[t]
139	\centering
140	\includegraphics[width=\columnwidth]{figures/fig4.pdf}
141	\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\_mean ($R^2{=}0.683$) below the projector baseline ($0.706$, $p{=}0.001$) but concentrates superior information at the trained readout ($0.731$, $p{=}0.001$). Untrained readout ($0.686$) falls below the projector, confirming that concentration requires training ($\Delta{=}0.045$, $p{<}0.0001$). DINOv2 ($0.712$) is statistically indistinguishable from the projector ($p{=}0.22$).}
142	\label{fig:probe_bars}
143	\end{figure}
144	
145	%------------------------------------------------------------------
146	\subsection{Training Routes, Does Not Create, Action Geometry}
147	\label{sec:training_routing}
148	
149	This experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.
150	Table~\ref{tab:training_effects} reports the effect of training across metrics.
151	The $2 \times 2$ factorial analysis (Figure~\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.
152	
153	\paragraph{Geometric invariance to training.}
154	Training does not alter the LLM's geometric alignment with the action space.
155	For image\_mean RSA, the training effect is $\Delta = +0.021$ (95\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\_preaction RSA, $\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).
156	This null result is consistent with the vision encoder---whose weights are identical between conditions ($\cos\text{sim} = 1.0$)---being the sole source of action-relevant geometry.
157	
158	\paragraph{Geometric invariance to instruction.}
159	Language instructions similarly fail to modulate geometric structure.
160	Across the $2 \times 2$ matrix, the instruction effect is $\Delta = 0.004$ (n.s.).
161	A dedicated control experiment with four instruction conditions---normal task instructions ($\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\pm 0.017$ of the mean (Figure~\ref{fig:factorial}b).
162	
163	\paragraph{Functional concentration requires training.}
164	In contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\Delta = +0.045$ (CI $[+0.032, +0.058]$, $p < 0.0001$).
165	Training transforms the readout from below-projector ($R^2 = 0.686$) to above-projector ($R^2 = 0.731$) without altering the underlying geometry.
166	
167	These results support a \emph{routing} interpretation of LLM training in VLAs~\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.
168	
169	\begin{table}[t]
170	\centering
171	\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\_mean $R^2$ drop confirms distributed degradation.}
172	\label{tab:training_effects}
173	\small
174	\begin{tabular}{lccc}
175	\toprule
176	Comparison & $\Delta$ & 95\% CI & $p$ \\
177	\midrule
178	Training (image\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\
179	Training (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\
180	Training (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\
181	Proj.\ vs.\ image\_mean ($R^2$) & $+$0.023 & [$+$0.011, $+$0.037] & 0.001 \\
182	\bottomrule
183	\end{tabular}
184	\end{table}
185	
186	\begin{figure}[t]
187	\centering
188	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
189	\caption{\textbf{(a)}~Training $\times$ Instruction matrix for image\_mean RSA ($\rho$). Neither training ($\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\Delta{=}0.004$, n.s.)\ produces a statistically detectable effect. \textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\pm 0.017$ of the mean $\mu{=}0.482$, confirming that instruction content does not modulate distributed geometric structure.}
190	\label{fig:factorial}
191	\end{figure}
192	
193	\begin{figure}[t]
194	\centering
195	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
196	\caption{Comparison of three similarity metrics across representation sources. \textbf{(a)}~RSA (Spearman $\rho$) and \textbf{(c)}~RDM kernel CKA produce consistent rankings (Proj $>$ Trained $>$ Untrained $>$ DINOv2). \textbf{(b)}~Linear CKA~\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}
197	\label{fig:metric_comparison}
198	\end{figure}
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "6ce7f680-a930-43c0-98bd-677e23634641",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.\n\n\\paragraph{Representation sources.}\nWe extract representations from five sources:\n(a)~\\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token}; and\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}.\nSources (d) and (e) serve as external baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{Representational Similarity Analysis (RSA).}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples.\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions.\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nThe SigLIP+Projector output achieves the highest alignment ($\\rho = 0.615$, 95\\% CI $[0.526, 0.695]$), followed by CLIP ViT-L/14 ($\\rho = 0.557$, $[0.442, 0.660]$).\nBoth vision-language pretrained encoders substantially exceed DINOv2 ($\\rho = 0.388$), a vision-only model.\nThe VLA's LLM layers (best image\\_mean: $\\rho = 0.501$ trained, $\\rho = 0.485$ untrained) fall between VL-pretrained encoders and DINOv2 (Figure~\\ref{fig:rsa_bar}).\n\nThree findings emerge.\nFirst, VL pretraining---not LLM processing---is the primary source of action-relevant structure.\nSigLIP and CLIP, both pretrained on image-text pairs, achieve $\\rho \\geq 0.557$, while DINOv2, pretrained with self-supervised vision objectives alone, reaches only $\\rho = 0.388$.\nThis 0.169-point gap indicates that language-grounded visual features carry substantially more action-relevant geometry than features learned without language, consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\n\nSecond, the MLP projector provides incremental alignment: SigLIP+Projector ($0.615$) exceeds CLIP ($0.557$) by $\\Delta = 0.058$, consistent with the projector mapping vision features into the LLM's embedding space.\n\nThird, the LLM degrades rather than enhances vision encoder geometry.\nProcessing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\\_mean), a drop of $\\Delta = 0.114$.\n\n\\paragraph{Geometric-functional dissociation.}\nFunctional probes reveal a dissociation between geometric similarity and functional decodability.\nDINOv2 achieves $R^2 = 0.712$, statistically indistinguishable from SigLIP+Projector ($R^2 = 0.706$, $p = 0.22$, n.s.), despite its substantially lower RSA ($0.388$ vs.\\ $0.615$).\nThis dissociation extends to the VL-pretrained encoders: in a within-experiment comparison,\\footnote{CLIP and DINOv2 probes use matched training protocols; absolute $R^2$ values differ from the projector/LLM probes due to separate probe code, so cross-experiment comparisons of raw $R^2$ are not valid.} CLIP achieves $R^2 = 0.805$, indistinguishable from DINOv2 ($R^2 = 0.814$, $p = 0.10$, n.s.)---yet CLIP's RSA ($0.557$) far exceeds DINOv2's ($0.388$).\nVL pretraining thus provides geometric alignment with the action space, not additional predictive content.\n\n\\paragraph{Metric sensitivity.}\nThis dissociation extends to alternative similarity metrics.\nLinear CKA~\\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA restores the RSA-consistent ranking (Proj $>$ Trained $>$ Untrained $>$ DINOv2).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). VL-pretrained encoders (SigLIP, CLIP) dominate over vision-only DINOv2 and LLM-processed representations. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & 95\\% CI \\\\\n\\midrule\nSigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & {[0.442, 0.660]} \\\\\n\\midrule\nVLA Trained w/ inst. & image\\_mean & 0.501 & --- \\\\\nVLA Trained no inst. & image\\_mean & 0.501 & --- \\\\\nVLA Untrained w/ inst. & image\\_mean & 0.485 & --- \\\\\nVLA Untrained no inst. & image\\_mean & 0.482 & --- \\\\\n\\midrule\nDINOv2 ViT-L/14 & cls\\_token & 0.388 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. VL-pretrained encoders (SigLIP $\\rho{=}0.615$, CLIP $\\rho{=}0.557$) substantially exceed both LLM-processed representations ($\\rho \\leq 0.501$) and vision-only DINOv2 ($\\rho{=}0.388$). Hatched bars indicate no-instruction conditions. Error bars: 95\\% bootstrap CIs. Dashed line: DINOv2 reference.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{LLM Redistributes, Does Not Enhance, Action Structure}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.\nTable~\\ref{tab:probes} reports functional probe $R^2$ for key representation sources.\nTwo complementary effects characterize LLM processing.\n\n\\paragraph{Distributed degradation.}\nAveraging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.\nRSA drops from $0.615$ to $0.501$ ($\\Delta = 0.114$); probe $R^2$ drops from $0.706$ to $0.683$ (95\\% CI of $\\Delta$: $[0.011, 0.037]$, $p = 0.001$).\nFigure~\\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens lose information, the last pre-action token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves $R^2 = 0.731$, exceeding SigLIP+Projector ($R^2 = 0.706$, $p = 0.001$; Figure~\\ref{fig:probe_bars}).\nThis concentration is training-dependent: untrained readout ($R^2 = 0.686$) falls below the projector baseline, while trained readout ($0.731$) substantially exceeds it ($\\Delta = 0.045$, $p < 0.0001$).\n\nTogether, these results characterize the LLM as a \\emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations. The LLM degrades distributed representations (image\\_mean) relative to the projector but concentrates superior action information at the readout token---an effect that requires training. DINOv2 matches the projector in $R^2$ despite much lower RSA.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nSigLIP+Projector & 0.706 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.683 & 0.001 \\\\\nVLA Trained readout (L19) & \\textbf{0.731} & 0.001 \\\\\nVLA Untrained readout (L32) & 0.686 & --- \\\\\nDINOv2 cls\\_token & 0.712 & 0.220 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: SigLIP+Projector ($\\rho{=}0.615$) and DINOv2 ($\\rho{=}0.388$) reference levels.}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\\_mean ($R^2{=}0.683$) below the projector baseline ($0.706$, $p{=}0.001$) but concentrates superior information at the trained readout ($0.731$, $p{=}0.001$). Untrained readout ($0.686$) falls below the projector, confirming that concentration requires training ($\\Delta{=}0.045$, $p{<}0.0001$). DINOv2 ($0.712$) is statistically indistinguishable from the projector ($p{=}0.22$).}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Routes, Does Not Create, Action Geometry}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.\nTable~\\ref{tab:training_effects} reports the effect of training across metrics.\nThe $2 \\times 2$ factorial analysis (Figure~\\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.\n\n\\paragraph{Geometric invariance to training.}\nTraining does not alter the LLM's geometric alignment with the action space.\nFor image\\_mean RSA, the training effect is $\\Delta = +0.021$ (95\\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\\_preaction RSA, $\\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).\nThis null result is consistent with the vision encoder---whose weights are identical between conditions ($\\cos\\text{sim} = 1.0$)---being the sole source of action-relevant geometry.\n\n\\paragraph{Geometric invariance to instruction.}\nLanguage instructions similarly fail to modulate geometric structure.\nAcross the $2 \\times 2$ matrix, the instruction effect is $\\Delta = 0.004$ (n.s.).\nA dedicated control experiment with four instruction conditions---normal task instructions ($\\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\\pm 0.017$ of the mean (Figure~\\ref{fig:factorial}b).\n\n\\paragraph{Functional concentration requires training.}\nIn contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\\Delta = +0.045$ (CI $[+0.032, +0.058]$, $p < 0.0001$).\nTraining transforms the readout from below-projector ($R^2 = 0.686$) to above-projector ($R^2 = 0.731$) without altering the underlying geometry.\n\nThese results support a \\emph{routing} interpretation of LLM training in VLAs~\\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\\_mean $R^2$ drop confirms distributed degradation.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nTraining (image\\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\\\\nTraining (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\\\\nTraining (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\\\\nProj.\\ vs.\\ image\\_mean ($R^2$) & $+$0.023 & [$+$0.011, $+$0.037] & 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Training $\\times$ Instruction matrix for image\\_mean RSA ($\\rho$). Neither training ($\\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\\Delta{=}0.004$, n.s.)\\ produces a statistically detectable effect. \\textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\\pm 0.017$ of the mean $\\mu{=}0.482$, confirming that instruction content does not modulate distributed geometric structure.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Comparison of three similarity metrics across representation sources. \\textbf{(a)}~RSA (Spearman $\\rho$) and \\textbf{(c)}~RDM kernel CKA produce consistent rankings (Proj $>$ Trained $>$ Untrained $>$ DINOv2). \\textbf{(b)}~Linear CKA~\\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}\n\\label{fig:metric_comparison}\n\\end{figure}\n",
      "numLines": 199,
      "startLine": 1,
      "totalLines": 199
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
Now I have all the context I need. Let me also check if there's an existing method.tex file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "91bd0db0-c1f5-45b7-88e5-86b04472b5c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbcajVkYjRvuHqYcdbfZz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11793,
      "cache_read_input_tokens": 24623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11793
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

Now let me check if there's an existing method.tex and look at the docs/paper directory structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "9cf21a2a-334d-4cfa-b41d-d20169b85b7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbcajVkYjRvuHqYcdbfZz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11793,
      "cache_read_input_tokens": 24623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11793
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

<details open><summary>🔧 Tool call — Glob · `toolu_01YCU1zA9nkAvW4E4Tf12Pj3`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "af6ef98f-81c4-4931-b5e3-0e12e33816d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LbcajVkYjRvuHqYcdbfZz5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11793,
      "cache_read_input_tokens": 24623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11793
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

_source line 14 · 2026-05-16T02:42:18.624Z_

<details><summary>↩ Tool result · `toolu_01YCU1zA9nkAvW4E4Tf12Pj3`</summary>

```text
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "bdd3e67e-2e63-49e2-9d90-b5fc65e3bab7",
  "tool_use_result": {
    "filenames": [
      "docs/paper/experiments.tex"
    ],
    "durationMs": 15,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
No existing method.tex. I need to create it. Let me also check if there's a main.tex that includes sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "b04c2441-4f87-4b66-94ee-7dd5a70fd4bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4RXkSe8CbeponxDR1aDLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 181,
      "cache_read_input_tokens": 36416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 181
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

Let me check the main paper structure and any existing files for context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "6167f569-a603-45b2-a4a1-cb0d4d7069ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4RXkSe8CbeponxDR1aDLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 181,
      "cache_read_input_tokens": 36416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 181
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

<details open><summary>🔧 Tool call — Glob · `toolu_01BbhpFZco2faqS3mdw5FCDT`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "ddbfc6e9-dc82-494b-bdda-beff4f218057",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4RXkSe8CbeponxDR1aDLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 181,
      "cache_read_input_tokens": 36416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 181
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

_source line 18 · 2026-05-16T02:42:22.291Z_

<details><summary>↩ Tool result · `toolu_01BbhpFZco2faqS3mdw5FCDT`</summary>

```text
docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "427fc386-f68a-41fe-96ae-cc06269535e9",
  "tool_use_result": {
    "filenames": [
      "docs/paper/experiments.tex"
    ],
    "durationMs": 9,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_011tdXZSgVLXetBWU8VFDv66`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "ba0188b2-b125-486e-9696-3cce7d780edc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4RXkSe8CbeponxDR1aDLx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 181,
      "cache_read_input_tokens": 36416,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 181
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

_source line 20 · 2026-05-16T02:42:22.979Z_

<details><summary>↩ Tool result · `toolu_011tdXZSgVLXetBWU8VFDv66`</summary>

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
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "a0b5c4ee-a08e-4ebd-8fe1-a3c20e40c497",
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

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now I have everything I need. Let me write the method.tex. Key things to ensure:

1. Consistent terminology with experiments.tex
2. Follow red-section skill (no cherry-picking, strength matches evidence, etc.)
3. Follow latex-paper skill (claim-evidence, clear writing)
4. Only use provided bibtex keys
5. ~1.5-2 pages CoRL format
6. 5 subsections as specified

Let me carefully match terminology from experiments.tex:
- "SigLIP+Projector" (not just SigLIP)
- "image_mean" (with underscore in text)


- "last_preaction" as the readout token
- "7-dimensional action space" or "7-D action vectors"
- "$2 \times 2$ factorial design" with trained vs. untrained and language instruction conditions
- "from_config()" for model reinitialization
- "6.74B random weights" for the untrained LLM baseline
- "0.80B pretrained weights" for the frozen SigLIP encoder
- "RDMs" for representational dissimilarity matrices
- "Spearman rank correlation $\rho$" for statistical measures
- "10,000 bootstrap resamples" for significance testing
- MLP probes that map from representations to action dimensions through a hidden layer of 256 units
- Adam optimizer with learning rate 1e-3, batch size 256, 50 epochs, and early stopping with patience 5
- "mean $R^2$ across action dimensions" as the primary metric
- "Linear CKA" and "RDM kernel CKA" for representational similarity
- DINOv2 ViT-L/14 cls_token and CLIP ViT-L/14 patch_mean as the vision model features

Now I'm structuring the methods section to be detailed but concise, covering model architecture, data, representation extraction, similarity analysis, and the probing approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "823ef1a2-6d34-4ed7-83e9-c9bbe67044c4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmPnqmu8bKWxt4V3ACR7mv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 36597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
      },
      "output_tokens": 10,
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

Writing method.tex now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "63430756-844b-49cb-a291-29ed8e4d09ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmPnqmu8bKWxt4V3ACR7mv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 36597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
      },
      "output_tokens": 10,
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

<details open><summary>🔧 Tool call — Write · `toolu_01QYgiGU28CewY6jdd8BgWtZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant structure is distributed across the components of a vision-language-action model by combining geometric analysis (RSA, CKA) with functional probes.\nThis section formalizes the model, data, representation extraction procedure, and the three complementary analysis tools.\n\n%------------------------------------------------------------------\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy that chains three components: a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip} (0.80B parameters, frozen during fine-tuning), an MLP projector that maps vision features into the language model's embedding space, and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions (6 DoF end-effector pose $+$ gripper opening).\n\n\\paragraph{Fine-tuning data.}\nWe use a checkpoint fine-tuned on the LIBERO-10 split~\\cite{liu2023_libero}, which provides 10 tabletop manipulation tasks with 50 human demonstrations per task.\n\n\\paragraph{Evaluation benchmark.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, which shares initial states with LIBERO-10 but pairs them with different language-specified goals.\nThis separation ensures that the evaluation tasks test generalization to novel goals rather than memorization of training trajectories.\n\n\\paragraph{Untrained control.}\nTo isolate the contribution of LLM fine-tuning, we construct an untrained control by reinitializing the LLM parameters via \\texttt{from\\_config()}, yielding 6.74B random weights while preserving the frozen SigLIP encoder (0.80B pretrained weights) and the MLP projector architecture.\nAny difference between trained and untrained conditions is therefore attributable to LLM training, not to the vision encoder.\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nWe extract representations from five sources that span the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),leftmargin=*,nosep]\n  \\item \\textbf{SigLIP+Projector}: the output of the MLP projector applied to SigLIP vision features, i.e., the representation immediately before LLM processing.\n  \\item \\textbf{LLM image\\_mean}: the mean activation across image token positions at each of the 32 LLM layers, capturing how distributed visual information evolves through the language backbone.\n  \\item \\textbf{LLM last\\_preaction}: the activation at the final token position before action decoding (the readout token) at each LLM layer, capturing how the model concentrates information for action prediction.\n  \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2}: the \\texttt{cls\\_token} from a vision-only self-supervised encoder, serving as a baseline without language grounding.\n  \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip}: the mean of patch token activations (\\texttt{patch\\_mean}) from a vision-language contrastive model, serving as an external VL-pretrained baseline with no VLA training signal.\n\\end{enumerate}\n\n\\paragraph{Experimental conditions.}\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nSources (a)--(c) are extracted under all four conditions; sources (d) and (e) are condition-independent external baselines.\nFor the instruction factor, the with-instruction condition uses the LIBERO-Goal task description; the without-instruction condition provides an empty string.\n\n%------------------------------------------------------------------\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify geometric alignment between neural representations and the action space.\n\n\\paragraph{RDM construction.}\nFor a set of $N$ observations, we compute the $N \\times N$ representational dissimilarity matrix (RDM) for each representation source using pairwise Euclidean distances.\nAn analogous RDM is computed for the 7-dimensional action vectors.\n\n\\paragraph{RSA statistic.}\nWe measure the alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ over the upper-triangular entries of each matrix.\nHigher $\\rho$ indicates that observations that are nearby in representation space also tend to require similar actions.\n\n\\paragraph{Task-level analysis.}\nWe compute RSA separately for each of the 10 LIBERO-Goal tasks, then aggregate across tasks.\nThis per-task procedure avoids conflating within-task structure with between-task variation.\n\n\\paragraph{Statistical inference.}\nWe construct 95\\% confidence intervals via bootstrap resampling (10{,}000 resamples) over the observation pairs.\nPairwise comparisons between representation sources use bootstrap differences with the same resampling scheme.\n\n%------------------------------------------------------------------\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA captures geometric alignment but does not assess whether action-relevant information is linearly decodable.\nWe complement RSA with functional probes following~\\cite{alain2017}.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear; $d_\\text{in} \\to 256 \\to 7$) to predict 7-D action vectors from frozen representations.\nAll representation weights are fixed; only the probe parameters are optimized.\n\n\\paragraph{Training protocol.}\nProbes are trained with the Adam optimizer (learning rate $10^{-3}$, batch size 256) for up to 50 epochs with early stopping (patience $= 5$, monitoring validation loss).\nEach task's data is split into training and validation sets.\n\n\\paragraph{Evaluation metric.}\nWe report mean $R^2$ across the 7 action dimensions, providing a normalized measure of variance explained that is comparable across representation sources with different dimensionalities.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparisons (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant, reporting $p$-values and 95\\% confidence intervals for all pairwise contrasts.\n\n%------------------------------------------------------------------\n\\subsection{CKA Analysis}\n\\label{sec:cka}\n\nAs a complementary perspective, we employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\n\\paragraph{Two CKA variants.}\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\n\\paragraph{Dimension mismatch caveat.}\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality, providing a more reliable cross-dimensional comparison.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "29a8acfc-57ae-4598-b5c2-f521fa1007e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmPnqmu8bKWxt4V3ACR7mv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 36597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
      },
      "output_tokens": 10,
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

_source line 24 · 2026-05-16T02:43:18.395Z_

<details><summary>↩ Tool result · `toolu_01QYgiGU28CewY6jdd8BgWtZ`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "2cf089d1-3348-46c9-9351-dc7a0335a6f5",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant structure is distributed across the components of a vision-language-action model by combining geometric analysis (RSA, CKA) with functional probes.\nThis section formalizes the model, data, representation extraction procedure, and the three complementary analysis tools.\n\n%------------------------------------------------------------------\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy that chains three components: a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip} (0.80B parameters, frozen during fine-tuning), an MLP projector that maps vision features into the language model's embedding space, and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions (6 DoF end-effector pose $+$ gripper opening).\n\n\\paragraph{Fine-tuning data.}\nWe use a checkpoint fine-tuned on the LIBERO-10 split~\\cite{liu2023_libero}, which provides 10 tabletop manipulation tasks with 50 human demonstrations per task.\n\n\\paragraph{Evaluation benchmark.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, which shares initial states with LIBERO-10 but pairs them with different language-specified goals.\nThis separation ensures that the evaluation tasks test generalization to novel goals rather than memorization of training trajectories.\n\n\\paragraph{Untrained control.}\nTo isolate the contribution of LLM fine-tuning, we construct an untrained control by reinitializing the LLM parameters via \\texttt{from\\_config()}, yielding 6.74B random weights while preserving the frozen SigLIP encoder (0.80B pretrained weights) and the MLP projector architecture.\nAny difference between trained and untrained conditions is therefore attributable to LLM training, not to the vision encoder.\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nWe extract representations from five sources that span the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),leftmargin=*,nosep]\n  \\item \\textbf{SigLIP+Projector}: the output of the MLP projector applied to SigLIP vision features, i.e., the representation immediately before LLM processing.\n  \\item \\textbf{LLM image\\_mean}: the mean activation across image token positions at each of the 32 LLM layers, capturing how distributed visual information evolves through the language backbone.\n  \\item \\textbf{LLM last\\_preaction}: the activation at the final token position before action decoding (the readout token) at each LLM layer, capturing how the model concentrates information for action prediction.\n  \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2}: the \\texttt{cls\\_token} from a vision-only self-supervised encoder, serving as a baseline without language grounding.\n  \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip}: the mean of patch token activations (\\texttt{patch\\_mean}) from a vision-language contrastive model, serving as an external VL-pretrained baseline with no VLA training signal.\n\\end{enumerate}\n\n\\paragraph{Experimental conditions.}\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nSources (a)--(c) are extracted under all four conditions; sources (d) and (e) are condition-independent external baselines.\nFor the instruction factor, the with-instruction condition uses the LIBERO-Goal task description; the without-instruction condition provides an empty string.\n\n%------------------------------------------------------------------\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify geometric alignment between neural representations and the action space.\n\n\\paragraph{RDM construction.}\nFor a set of $N$ observations, we compute the $N \\times N$ representational dissimilarity matrix (RDM) for each representation source using pairwise Euclidean distances.\nAn analogous RDM is computed for the 7-dimensional action vectors.\n\n\\paragraph{RSA statistic.}\nWe measure the alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ over the upper-triangular entries of each matrix.\nHigher $\\rho$ indicates that observations that are nearby in representation space also tend to require similar actions.\n\n\\paragraph{Task-level analysis.}\nWe compute RSA separately for each of the 10 LIBERO-Goal tasks, then aggregate across tasks.\nThis per-task procedure avoids conflating within-task structure with between-task variation.\n\n\\paragraph{Statistical inference.}\nWe construct 95\\% confidence intervals via bootstrap resampling (10{,}000 resamples) over the observation pairs.\nPairwise comparisons between representation sources use bootstrap differences with the same resampling scheme.\n\n%------------------------------------------------------------------\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA captures geometric alignment but does not assess whether action-relevant information is linearly decodable.\nWe complement RSA with functional probes following~\\cite{alain2017}.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear; $d_\\text{in} \\to 256 \\to 7$) to predict 7-D action vectors from frozen representations.\nAll representation weights are fixed; only the probe parameters are optimized.\n\n\\paragraph{Training protocol.}\nProbes are trained with the Adam optimizer (learning rate $10^{-3}$, batch size 256) for up to 50 epochs with early stopping (patience $= 5$, monitoring validation loss).\nEach task's data is split into training and validation sets.\n\n\\paragraph{Evaluation metric.}\nWe report mean $R^2$ across the 7 action dimensions, providing a normalized measure of variance explained that is comparable across representation sources with different dimensionalities.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparisons (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant, reporting $p$-values and 95\\% confidence intervals for all pairwise contrasts.\n\n%------------------------------------------------------------------\n\\subsection{CKA Analysis}\n\\label{sec:cka}\n\nAs a complementary perspective, we employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\n\\paragraph{Two CKA variants.}\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\n\\paragraph{Dimension mismatch caveat.}\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality, providing a more reliable cross-dimensional comparison.\n",
    "structuredPatch": [],
    "originalFile": null,
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
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "fcf87d3e-3a65-4102-8d38-1a0c3534a0ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ph2FNgNi5tDejJfSyJJsTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2726,
      "cache_read_input_tokens": 36915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2726
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013inCDLMSCECUZ1HgeL3PdU`</summary>

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
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "f2b0d89e-1727-4c25-a118-f7a7af7d24de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ph2FNgNi5tDejJfSyJJsTZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2726,
      "cache_read_input_tokens": 36915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2726
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

_source line 27 · 2026-05-16T02:43:21.065Z_

<details><summary>↩ Tool result · `toolu_013inCDLMSCECUZ1HgeL3PdU`</summary>

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
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "d5bef069-3fcf-4491-b649-dc8de57515e4",
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_018gKNTU3MCbYSmhWKGUeXok`</summary>

```json
{
  "name": "method.tex",
  "type": "paper",
  "description": "Method section (Section 2) of the VLA-SSD paper: 5 subsections covering model/data, representation extraction, RSA, functional probes, and CKA analysis.",
  "project": "vla-ssd",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
  "tags": [
    "paper",
    "method",
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
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "5e07d18e-a94e-4409-9a83-8ab7838bba38",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BvUSd67wfYqnHufsETDym",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 39641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
      },
      "output_tokens": 58,
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

_source line 29 · 2026-05-16T02:43:25.342Z_

<details><summary>↩ Tool result · `toolu_018gKNTU3MCbYSmhWKGUeXok`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_a6c062\", \"name\": \"method.tex\", \"type\": \"paper\", \"description\": \"Method section (Section 2) of the VLA-SSD paper: 5 subsections covering model/data, representation extraction, RSA, functional probes, and CKA analysis.\", \"path\": \"projects/vla-ssd/artifacts/_project/paper/method_a6c062.tex\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:43:25.266418+00:00\", \"tags\": [\"paper\", \"method\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "183aebfd-67dd-45c3-a017-eb838d5b6181",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_a6c062\\\", \\\"name\\\": \\\"method.tex\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"Method section (Section 2) of the VLA-SSD paper: 5 subsections covering model/data, representation extraction, RSA, functional probes, and CKA analysis.\\\", \\\"path\\\": \\\"projects/vla-ssd/artifacts/_project/paper/method_a6c062.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"vla-ssd\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T02:43:25.266418+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"method\\\", \\\"latex\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_a6c062\", \"name\": \"method.tex\", \"type\": \"paper\", \"description\": \"Method section (Section 2) of the VLA-SSD paper: 5 subsections covering model/data, representation extraction, RSA, functional probes, and CKA analysis.\", \"path\": \"projects/vla-ssd/artifacts/_project/paper/method_a6c062.tex\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:43:25.266418+00:00\", \"tags\": [\"paper\", \"method\", \"latex\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

Method 章节已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex`。

内容概要：
- **2.1 Model and Data**: OpenVLA-7B 架构（SigLIP → Projector → Llama-2 7B → action head）、LIBERO-10 微调、LIBERO-Goal 评估、untrained control 设计
- **2.2 Representation Extraction**: 五个表征来源 (a)-(e) 的定义，$2\times2$ factorial design（trained/untrained × with/without instruction）
- **2.3 RSA**: RDM 构建、Spearman $\rho$、per-task 分析、bootstrap CI (10,000 resamples)
- **2.4 Functional Action Probes**: MLP probe 架构（$d_\text{in} \to 256 \to 7$）、训练协议（Adam, lr=$10^{-3}$, batch 256, 50 epochs, patience 5）、mean $R^2$ 指标、bootstrap paired comparison
- **2.5 CKA Analysis**: Linear CKA 与 RDM kernel CKA 两种变体，dimension mismatch caveat

所有术语、符号、数字与 experiments.tex 保持一致。仅使用指定的 bibtex keys。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "uuid": "a1b157b0-2c39-4664-885c-f6b130500e37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QAY3FYEiDUDA4iF4eTSDeK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 515,
      "cache_read_input_tokens": 40361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 515
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

Method 章节已写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex`。

内容概要：
- **2.1 Model and Data**: OpenVLA-7B 架构（SigLIP → Projector → Llama-2 7B → action head）、LIBERO-10 微调、LIBERO-Goal 评估、untrained control 设计
- **2.2 Representation Extraction**: 五个表征来源 (a)-(e) 的定义，$2\times2$ factorial design（trained/untrained × with/without instruction）
- **2.3 RSA**: RDM 构建、Spearman $\rho$、per-task 分析、bootstrap CI (10,000 resamples)
- **2.4 Functional Action Probes**: MLP probe 架构（$d_\text{in} \to 256 \to 7$）、训练协议（Adam, lr=$10^{-3}$, batch 256, 50 epochs, patience 5）、mean $R^2$ 指标、bootstrap paired comparison
- **2.5 CKA Analysis**: Linear CKA 与 RDM kernel CKA 两种变体，dimension mismatch caveat

所有术语、符号、数字与 experiments.tex 保持一致。仅使用指定的 bibtex keys。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 87177,
  "duration_api_ms": 87914,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "40ecd7cc-40d4-49fc-8c2e-85aa24dd794d",
  "total_cost_usd": 0.39462175000000005,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 29035,
    "cache_read_input_tokens": 226394,
    "output_tokens": 3903,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29035,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 374,
        "cache_read_input_tokens": 40361,
        "cache_creation_input_tokens": 515,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 515
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2236,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002326,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 3903,
      "cacheReadInputTokens": 226394,
      "cacheCreationInputTokens": 29035,
      "webSearchRequests": 0,
      "costUSD": 0.39229575000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7dd736d9-a7bc-4ae7-a81c-170242187cab"
}
```

</details>

---
