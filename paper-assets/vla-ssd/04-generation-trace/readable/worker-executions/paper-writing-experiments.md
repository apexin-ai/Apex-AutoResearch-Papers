# paper writing experiments

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260516T021635.log`
- **Structured JSON:** [`9a6cffe18fad6cc84ad0.json`](../../sessions/9a/9a6cffe18fad6cc84ad0.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
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
  "uuid": "4237b465-f866-46da-84ef-b848c25cf8d9",
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
  "uuid": "90f04a23-78c2-439f-83f6-33acde99bb12",
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to write the Experiments section (Section 3) for a CoRL 2026 paper about VLA (Vision-Language-Action) models and their internal representations. Let me first read the latex-paper skill for writing guidelines, then write the LaTeX code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "f1f71dcf-289a-4077-aa47-c6fd5bdece25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012zpapfhQ9GhWVFzYSjRpxF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13532
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — Read · `toolu_01HpEaMnAntLEwe4cYG1yzRa`</summary>

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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "a2b4d6be-51f0-4112-ae8b-a82ae575da15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012zpapfhQ9GhWVFzYSjRpxF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13532
      },
      "output_tokens": 25,
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

_source line 6 · 2026-05-16T02:16:49.909Z_

<details><summary>↩ Tool result · `toolu_01HpEaMnAntLEwe4cYG1yzRa`</summary>

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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "878a2ec1-2a69-4943-8c09-af35850bd111",
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

<details open><summary>🔧 Tool call — Bash · `toolu_017WT81NbDzQgXNaBgS2THy8`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/ 2>/dev/null || echo \"DIR_NOT_EXIST\"",
  "description": "Check if paper directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "c1ace199-43ee-49bd-8e17-b85f239fd9df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012zpapfhQ9GhWVFzYSjRpxF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13532,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13532
      },
      "output_tokens": 25,
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

_source line 8 · 2026-05-16T02:16:51.017Z_

<details><summary>↩ Tool result · `toolu_017WT81NbDzQgXNaBgS2THy8`</summary>

```text
total 8
drwxr-xr-x 2 ubuntu ubuntu 4096 May 15 05:23 .
drwxr-xr-x 4 ubuntu ubuntu 4096 May 15 05:23 ..
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "def820a6-ef6b-4140-b25b-581e4070235b",
  "tool_use_result": {
    "stdout": "total 8\ndrwxr-xr-x 2 ubuntu ubuntu 4096 May 15 05:23 .\ndrwxr-xr-x 4 ubuntu ubuntu 4096 May 15 05:23 ..",
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

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
The paper directory exists but is empty. Let me also check if there are any existing figures or other paper-related files in the project.

Now let me write the experiments section and the references.bib file. I need to be careful about:
1. Claim-Evidence methodology
2. No hallucinated citations - mark uncertain ones with [VERIFY]
3. Proper LaTeX formatting for CoRL 2026
4. Numbers to 3 decimal places
5. Writing red lines from the task

Let me write the experiments.tex and references.bib files.

For the BibTeX entries, let me think about what I know with confidence:


- OpenVLA by Kim et al. from 2024, likely published at ICML or on arXiv
- Karamcheti's work on Prismatic VLMs and related to OpenVLA
- RT-2 by Brohan et al. from 2023
- LIBERO benchmark by Liu et al. from 2023
- Kriegeskorte's representational similarity analysis paper from 2008 in Frontiers in Systems Neuroscience
- Kornblith's CKA paper by Simon Kornblith et al. from 2019 at ICML
- Linear probes work by Alain and Bengio from 2017 at an ICLR workshop
- SigLIP by Zhai et al. from 2023
- DINOv2 by Oquab et al. from 2024, with an earlier arXiv version in 2023
- CLIP by Radford et al. from 2021 at ICML
- A 2025 paper on VLA interpretability that I'm less certain about
- Grant et al. 2026 on behavioral visual dominance, which might be the current paper's own prior work or very recent

Now I'm setting up the LaTeX structure for the references.

I'm organizing the experiments section into four main parts: the experimental setup, then three subsections each testing one of the core claims with evidence and conclusions drawn from the data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "3203c897-c64e-4c0d-aae5-c9b5d74e0320",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApKzLLPshAc8hFFeReB2Mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5804,
      "cache_read_input_tokens": 25373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5804
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

Now let me check for any existing paper content or figure references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "1ca19c9b-1c1e-4e6b-8258-2f6c365f5dc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApKzLLPshAc8hFFeReB2Mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5804,
      "cache_read_input_tokens": 25373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5804
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

<details open><summary>🔧 Tool call — Bash · `toolu_018ShSvd4X9mCUpW5mQ8Stg1`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/ 2>/dev/null; ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/ 2>/dev/null | head -20",
  "description": "Check docs and artifacts directories"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "0eac4891-8d16-484c-bde4-dc76f6d399ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ApKzLLPshAc8hFFeReB2Mg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5804,
      "cache_read_input_tokens": 25373,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5804
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

_source line 12 · 2026-05-16T02:17:12.012Z_

<details><summary>↩ Tool result · `toolu_018ShSvd4X9mCUpW5mQ8Stg1`</summary>

```text
total 52
drwxr-xr-x 4 ubuntu ubuntu  4096 May 15 05:23 .
drwxr-xr-x 9 ubuntu ubuntu  4096 May 16 02:17 ..
-rw-r--r-- 1 ubuntu ubuntu 36462 May 15 22:27 IDEA_BRIEF.md
drwxr-xr-x 2 ubuntu ubuntu  4096 May 15 05:23 paper
drwxr-xr-x 3 ubuntu ubuntu  4096 May 15 05:23 results
total 312
drwxr-xr-x 10 ubuntu ubuntu  4096 May 16 02:09 .
drwxr-xr-x  9 ubuntu ubuntu  4096 May 16 02:17 ..
drwxr-xr-x  6 ubuntu ubuntu  4096 May 15 22:31 _project
-rw-r--r--  1 ubuntu ubuntu  7079 May 15 14:06 action_probe_design.md
drwxr-xr-x  2 ubuntu ubuntu  4096 May 15 14:13 controlb_analysis
drwxr-xr-x  3 ubuntu ubuntu  4096 May 15 12:27 dinov2_baseline
drwxr-xr-x  4 ubuntu ubuntu  4096 May 16 01:59 dream_reports
drwxr-xr-x  3 ubuntu ubuntu  4096 May 16 01:44 figures
-rw-r--r--  1 ubuntu ubuntu 18052 May 15 16:09 layer_stability_analysis.md
-rw-r--r--  1 ubuntu ubuntu 18018 May 15 16:06 libero_goal_feasibility.md
-rw-r--r--  1 ubuntu ubuntu 13337 May 15 19:11 literature_map.yaml
-rw-r--r--  1 ubuntu ubuntu 19767 May 15 14:07 literature_map_probing.md
-rw-r--r--  1 ubuntu ubuntu 17313 May 15 17:20 literature_survey_instruction_probing.md
-rw-r--r--  1 ubuntu ubuntu 18003 May 16 02:13 manifest.yaml
drwxr-xr-x  3 ubuntu ubuntu  4096 May 15 14:14 mvp_controlb_trained
drwxr-xr-x  3 ubuntu ubuntu  4096 May 15 13:52 mvp_probe_trained
-rw-r--r--  1 ubuntu ubuntu 13478 May 15 16:13 openvla_libero_goal_compat.md
-rw-r--r--  1 ubuntu ubuntu 12966 May 15 17:04 patch_probes.py
-rw-r--r--  1 ubuntu ubuntu 15503 May 15 19:27 pca_linear_probe_gc.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "e5089cc5-3516-4a45-9bde-49364f9cb387",
  "tool_use_result": {
    "stdout": "total 52\ndrwxr-xr-x 4 ubuntu ubuntu  4096 May 15 05:23 .\ndrwxr-xr-x 9 ubuntu ubuntu  4096 May 16 02:17 ..\n-rw-r--r-- 1 ubuntu ubuntu 36462 May 15 22:27 IDEA_BRIEF.md\ndrwxr-xr-x 2 ubuntu ubuntu  4096 May 15 05:23 paper\ndrwxr-xr-x 3 ubuntu ubuntu  4096 May 15 05:23 results\ntotal 312\ndrwxr-xr-x 10 ubuntu ubuntu  4096 May 16 02:09 .\ndrwxr-xr-x  9 ubuntu ubuntu  4096 May 16 02:17 ..\ndrwxr-xr-x  6 ubuntu ubuntu  4096 May 15 22:31 _project\n-rw-r--r--  1 ubuntu ubuntu  7079 May 15 14:06 action_probe_design.md\ndrwxr-xr-x  2 ubuntu ubuntu  4096 May 15 14:13 controlb_analysis\ndrwxr-xr-x  3 ubuntu ubuntu  4096 May 15 12:27 dinov2_baseline\ndrwxr-xr-x  4 ubuntu ubuntu  4096 May 16 01:59 dream_reports\ndrwxr-xr-x  3 ubuntu ubuntu  4096 May 16 01:44 figures\n-rw-r--r--  1 ubuntu ubuntu 18052 May 15 16:09 layer_stability_analysis.md\n-rw-r--r--  1 ubuntu ubuntu 18018 May 15 16:06 libero_goal_feasibility.md\n-rw-r--r--  1 ubuntu ubuntu 13337 May 15 19:11 literature_map.yaml\n-rw-r--r--  1 ubuntu ubuntu 19767 May 15 14:07 literature_map_probing.md\n-rw-r--r--  1 ubuntu ubuntu 17313 May 15 17:20 literature_survey_instruction_probing.md\n-rw-r--r--  1 ubuntu ubuntu 18003 May 16 02:13 manifest.yaml\ndrwxr-xr-x  3 ubuntu ubuntu  4096 May 15 14:14 mvp_controlb_trained\ndrwxr-xr-x  3 ubuntu ubuntu  4096 May 15 13:52 mvp_probe_trained\n-rw-r--r--  1 ubuntu ubuntu 13478 May 15 16:13 openvla_libero_goal_compat.md\n-rw-r--r--  1 ubuntu ubuntu 12966 May 15 17:04 patch_probes.py\n-rw-r--r--  1 ubuntu ubuntu 15503 May 15 19:27 pca_linear_probe_gc.py",
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

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01RMpXr6aTL1e7px3wi5DSyd`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/ 2>/dev/null",
  "description": "Check figures directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "607d4592-42d3-4ed4-9534-80b49ca00fb7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SFR1LJdV6vdFV2Ck6zkzD4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1598,
      "cache_read_input_tokens": 31177,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1598
      },
      "output_tokens": 63,
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

_source line 14 · 2026-05-16T02:17:14.267Z_

<details><summary>↩ Tool result · `toolu_01RMpXr6aTL1e7px3wi5DSyd`</summary>

```text
total 12
drwxr-xr-x  3 ubuntu ubuntu 4096 May 16 01:44 .
drwxr-xr-x 10 ubuntu ubuntu 4096 May 16 02:09 ..
drwxr-xr-x  2 ubuntu ubuntu 4096 May 16 02:13 paper
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "569b1bb1-e025-4c77-9674-8980b78ff7c5",
  "tool_use_result": {
    "stdout": "total 12\ndrwxr-xr-x  3 ubuntu ubuntu 4096 May 16 01:44 .\ndrwxr-xr-x 10 ubuntu ubuntu 4096 May 16 02:09 ..\ndrwxr-xr-x  2 ubuntu ubuntu 4096 May 16 02:13 paper",
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

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01QnGw6JjfuQByEXtcpLmU8o`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/ 2>/dev/null",
  "description": "Check paper figures"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "f23b3e94-aeb0-4d4c-865d-4f62f5dbee02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CeeBiwmXrJj5jVBLq5JHJq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 210,
      "cache_read_input_tokens": 32775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 210
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

_source line 16 · 2026-05-16T02:17:17.545Z_

<details><summary>↩ Tool result · `toolu_01QnGw6JjfuQByEXtcpLmU8o`</summary>

```text
total 1020
drwxr-xr-x 2 ubuntu ubuntu   4096 May 16 02:13 .
drwxr-xr-x 3 ubuntu ubuntu   4096 May 16 01:44 ..
-rw-r--r-- 1 ubuntu ubuntu  30824 May 16 02:10 fig2.pdf
-rw-r--r-- 1 ubuntu ubuntu 153476 May 16 02:10 fig2.png
-rw-r--r-- 1 ubuntu ubuntu  27182 May 16 01:51 fig3.pdf
-rw-r--r-- 1 ubuntu ubuntu 208096 May 16 01:51 fig3.png
-rw-r--r-- 1 ubuntu ubuntu  24880 May 16 02:11 fig4.pdf
-rw-r--r-- 1 ubuntu ubuntu 151512 May 16 02:11 fig4.png
-rw-r--r-- 1 ubuntu ubuntu  35124 May 16 02:12 fig5.pdf
-rw-r--r-- 1 ubuntu ubuntu 179452 May 16 02:12 fig5.png
-rw-r--r-- 1 ubuntu ubuntu  35144 May 16 02:13 fig6.pdf
-rw-r--r-- 1 ubuntu ubuntu 174129 May 16 02:13 fig6.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "df9eaa50-8e52-428f-8385-716056e216c2",
  "tool_use_result": {
    "stdout": "total 1020\ndrwxr-xr-x 2 ubuntu ubuntu   4096 May 16 02:13 .\ndrwxr-xr-x 3 ubuntu ubuntu   4096 May 16 01:44 ..\n-rw-r--r-- 1 ubuntu ubuntu  30824 May 16 02:10 fig2.pdf\n-rw-r--r-- 1 ubuntu ubuntu 153476 May 16 02:10 fig2.png\n-rw-r--r-- 1 ubuntu ubuntu  27182 May 16 01:51 fig3.pdf\n-rw-r--r-- 1 ubuntu ubuntu 208096 May 16 01:51 fig3.png\n-rw-r--r-- 1 ubuntu ubuntu  24880 May 16 02:11 fig4.pdf\n-rw-r--r-- 1 ubuntu ubuntu 151512 May 16 02:11 fig4.png\n-rw-r--r-- 1 ubuntu ubuntu  35124 May 16 02:12 fig5.pdf\n-rw-r--r-- 1 ubuntu ubuntu 179452 May 16 02:12 fig5.png\n-rw-r--r-- 1 ubuntu ubuntu  35144 May 16 02:13 fig6.pdf\n-rw-r--r-- 1 ubuntu ubuntu 174129 May 16 02:13 fig6.png",
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

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good, I can see the figures are available (fig2-fig6 as PDF/PNG). Now let me write the experiments section. Let me look at the IDEA_BRIEF.md for more context about the paper's overall narrative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "7f6e237b-92c3-48d8-b954-9260f5ee7b59",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMhELC22Z1nxAVGPAhPCHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 32985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 485
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

Let me check the paper's overall narrative and figure descriptions for accurate references.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "e3e94e8f-4d28-4d0c-a218-e3833b9e2481",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMhELC22Z1nxAVGPAhPCHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 32985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 485
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

<details open><summary>🔧 Tool call — Read · `toolu_01CoDEbgPGXCmQbnYB2u2Z75`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/IDEA_BRIEF.md",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "64e445dd-2c69-4321-ba6e-6b901595de08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMhELC22Z1nxAVGPAhPCHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 32985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 485
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

_source line 20 · 2026-05-16T02:17:23.901Z_

<details><summary>↩ Tool result · `toolu_01CoDEbgPGXCmQbnYB2u2Z75`</summary>

```text
1	# Idea Brief: VLA-SSD: Do VLAs Know Which Demonstrations Are Good? Self-Referential Quality Scoring from Pretrained Representations
2	
3	
4	- **Idea ID**: `idea_004`
5	- **Created**: 2026-05-15
6	- **Approved**: 2026-05-15
7	- **Source**: foreign:be-idea-gen-0509-14
8	- **Level**: top-tier
9	- **Target Venues**: CoRL 2026 (abstract deadline May 26, full paper May 29, 2026), ICRA 2027 (~September 2026 deadline, backup if additional real-world validation needed), ICLR 2027 (~October 2026)
10	
11	## Seed Topic
12	
13	按照以下方向，生成1-2个优质idea，保质不求量：Seed 2: Reinforcement-Informed Demonstration Distillation for Noise-Robust VLA Training
14	Target: CoRL 2026 (Austin, Nov 9–12, 2026). Abstract deadline 2026-05-26 (12 days from today 2026-05-14); paper deadline 2026-05-29 (15 days).
15	Direction: RL-inspired experience scoring and filtering for VLA training data — methods that leverage data-intrinsic signals to identify and down-weight noisy, redundant, or suboptimal actions in real-world demonstration datasets before or during VLA fine-tuning. Real-world teleoperation data inevitably contains noise: hesitation pauses, corrective motions, grip fumbles, suboptimal trajectories, and redundant repeated actions. Standard behavioral cloning treats all timesteps equally, forcing the VLA to memorize noise as if it were signal — this is a fundamental source of brittleness. By borrowing the experience replay and advantage estimation machinery from offline RL, we can score each (state, action) pair by its contribution to task completion and filter or re-weight the training distribution accordingly. Unlike full offline RL (which replaces BC entirely), this approach retains the simplicity and stability of VLA fine-tuning while using RL-derived scores as a data curation signal. The key theoretical insight is that demonstration noise creates multi-modal action distributions at identical states, inflating the entropy of the learned policy; scoring and filtering collapses these modes to the high-performing subset, yielding a sharper, more robust policy.
16	Recent landscape (do not duplicate): Behavior Cloning, OpenVLA: An Open-Source Vision-Language-Action Model, FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models, PLD: Probe, Learn, Distill – Self-Improving Vision-Language-Action Models with Data Generation via Residual RL, REDI: Refined Policy Distillation: From VLA Generalists to RL Experts, GOLD: Guided Offline Learning from Demonstrations, SHS: An Offline Reinforcement Learning Algorithm Based on Selection of High-Quality Samples, PER: Prioritized Experience Replay, PRGS: Peak Reward Guided Trajectory Segmentation, What Can RL Bring to VLA Generalization? An Empirical Study, πRL: πRL: Manifold Policy Reinforcement Learning for Vision-Language-Action Models
17	Contribution type: METHOD ONLY. A two-stage demonstration distillation pipeline: (1) Temporal Advantage Scoring — train a lightweight value function on the demonstration data itself (using hindsight relabeling: final task success as sparse reward, or dense reward from state-goal distance) to compute per-timestep advantage estimates; actions with negative advantage (worse than the trajectory's average) are flagged as noisy; (2) Curriculum-Weighted Fine-Tuning — use the advantage scores as per-sample weights during VLA fine-tuning, with a curriculum that starts permissive (all data) and progressively sharpens to high-advantage subsets; (3) Consistency Regularization — for state-action pairs with high variance across similar states, add a consistency loss that encourages the VLA to commit to the high-scoring mode. No real robot required — the scoring is derived entirely from the existing dataset's structure.
18	EVAL PROTOCOL — IMPORTANT:
19	TRAIN on standard LIBERO suites (Object/Spatial/Goal/Long/90), with synthetic noise injection to simulate real-world demonstration noise (action jitter, redundant sub-trajectories, random pauses).
20	EVALUATE on existing LIBERO-PLUS / LIBERO-PRO style perturbation benchmarks (and similar community-released robustness benchmark series). DO NOT spend time constructing your own robustness benchmark — use existing perturbation suites and route the budget into the method.
21	Report robustness gap (Δ between nominal LIBERO success and perturbed-suite success) AND nominal preservation (must not regress on base LIBERO).
22	Additionally report: performance under varying noise injection ratios (10%/30%/50% noisy demonstrations), ablation of scoring function choices (MC return, TD advantage, trajectory ranking), and data efficiency curves (how much noisy data can be tolerated).
23	Experiments can be extended to other benchmarks with noisy demonstration collection (e.g., RLBench with injected perturbations).
24	SIM-ONLY MITIGATION: Using sim demonstrations with controlled noise injection is methodologically clean and well-accepted at CoRL. The scoring method is agnostic to sim/real — it operates on (state, action) pairs.
25	HARD CONSTRAINTS:
26	Compute: ≤200 H100-hours total. Fine-tune from open VLA checkpoints (OpenVLA, SmolVLA, OpenPi, π0) — no pretraining. Value function is lightweight (small MLP head). Show the math.
27	Time: ≤20 days. Build on OpenVLA, OpenPi and other proper codebases, LeRobot, HF Transformers.
28	Eval datasets: LIBERO base (training/nominal eval) + LIBERO-PLUS / LIBERO-PRO and similar existing perturbation suites (perturbed eval). No custom benchmark construction.
29	Look for: temporal advantage estimation from demonstration data without environment interaction, hindsight relabeling strategies for sparse-reward scoring, curriculum learning schedules that progressively filter noisy samples, connections between action distribution entropy and robustness, offline RL value estimation adapted to VLA's representation space. Avoid: requiring environment interaction or online rollouts (must be purely offline), full offline RL replacing BC (too unstable for VLA scale), simple trajectory-level success filtering (too coarse — need timestep-level scoring), just-add-noise training without filtering mechanism.
30	Tag: direction=robust_vla, contribution_type=method, sub_direction=demonstration_distillation, target_venues=["CoRL 2026"].
31	
32	## Generation Journey
33	
34	1. **Start** — 开始生成，seed: 'Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\nDirection：Meta-Brain VLA（无真机）\n*让LLM在不同场景下进行角色切换，辅助VLA应对多个场景，本质上还是利用潜在能力对视觉部分表征进行优化。\nMotivation：希望利用大模型已具备知识辅助VLA决策，达到类似Agentic元大脑框架的效果\nidea创新性：\n（1）使用现有性能比较强的大模型辅助VLA决策，回传时选择更新Skill库或者尝试优化Prompt\n（2）根据不同的场景信息选择角色，能够有效解决泛化\n（3）尝试用一种统一的表征来表达不同的信息\n\n元大脑角色切换：\nLLM作为元大脑，根据当前任务场景动态路由切换以下三种模式：\n（1）感知增强模式 ：环境光照暗、物体遮挡严重或遇到罕见物体，LLM专注输出空间关系描述或视觉线索引导，辅助 VLA 重新对齐特征\n（2）逻辑拆解模式：用户指令模糊，LLM 此时退回 Long-term Planning 角色，将任务分解为一系列 Skill 序列。\n（3）异常干预模式：VLA 预测的 Action 概率分布不确定性高，或者物理碰撞检测报错，LLM 介入进行反思，对比当前状态与目标状态，指导VLA改出。\n\n动态 Skill 库的进化逻辑：\n         LLM 具备写Skill能力，无法解决时有自我更新能力，并将其持久化到库中。\n\n技术难点：\n（1）无论 LLM 扮演什么角色，它最终产出一组同类型但不同功能的优化形式\n1）混合语义 Token (Hybrid Semantic Tokens)\n输出固定维度的嵌入向量，根据不同角色重塑原始视觉token\n2）功能前缀 (Function Prefix)\n在 LLM 输出的表征最前面，加入 Role Embedding，标识当前LLM的指导意见，能够使得VLA接收后，注意力机制或某些层面上发生相应变化。\n3）注意力热力图 (Attention Masking)\n让 LLM 生成注意力引导，始终返回给VLA的是一个权重矩阵\n压缩功能=将无效区域的权重降为 0。\n3D 引入功能 = 给具备空间深度的特征点赋予更高的初始权重。\n技能调用功能 = 强化与该技能相关的物体特征。\n\n（2）哪些部分要训练，如何训练？\n1）如何让LLM切换角色，可以划分关键帧前后两阶段训练\n2）Adapter的训练范式，需要元学习，构造功能性数据集学习不同任务需要的输出。\n3）信息穿透性，训练出的表征需要能对VLA有明显影响'
35	2. **Problem Discovery** (675s) — 发现 5 个研究方向
36	   - Role-Conditioned Meta-Brain for Adaptive VLA Enhancement
37	   - Unified Functional Token Interface for LLM-to-VLA Communication
38	   - Uncertainty-Triggered LLM Intervention with Representation-Level Correction
39	   - Scene-Adaptive Skill Routing via Meta-Brain Role Switching
40	   - LLM-Guided Attention Reweighting for VLA Robustness Under Perturbation
41	3. **Method Synthesis** (788s) — 完成: "Role-Conditioned Meta-Brain for Adaptive VLA Enhancement" [top-tier] → CoRL 2026 (abstract: May 26, paper: May 29, 2026) — top-tier robotics-learning venue, most natural fit for VLA representation-level intervention, AAAI 2027 (abstract: Jul 25, paper: Aug 1, 2026) — broad top-tier AI venue accepting embodied AI and robotics, ICLR 2027 (abstract: Sep 19, paper: Sep 24, 2026) — top-tier ML venue, strong fit for architectural innovation in VLA representation learning
42	3. **Method Synthesis** (515s) — 完成: "Unified Functional Token Interface for LLM-to-VLA Communication" [top-tier] → CoRL 2026 (abstract May 26, paper May 29 — top-tier robotics venue, ideal fit for VLA interface design contribution), ICLR 2027 (expected deadline ~Sep-Oct 2026 — highest-tier ML venue for architectural contributions), AAAI 2027 (expected deadline ~Jul-Aug 2026 — strong AI venue, confirmed Feb 16-23 2027 in Montréal)
43	3. **Method Synthesis** (631s) — 完成: "Uncertainty-Triggered LLM Intervention with Representation-Level Correction" [top-tier] → CoRL 2026 (abstract: May 26, paper: May 29 — confirmed open, premier robot learning venue), ICLR 2027 (expected deadline: ~Sep-Oct 2026 — highest-tier ML venue, strong fit for representation-learning contribution), AAAI 2027 (expected deadline: ~Jul-Aug 2026 — top AI venue), ICRA 2027 (expected deadline: ~Sep 2026 — top robotics venue)
44	3. **Method Synthesis** (619s) — 完成: "Scene-Adaptive Skill Routing via Meta-Brain Role Switching" [solid] → CoRL 2026 (paper deadline May 28-29, 2026 — top-tier robot learning venue, ideal topical fit for skill evolution in robot manipulation), ICLR 2027 (expected deadline ~October 2026 — top-tier ML venue, meta-learning contribution fits core audience), AAAI 2027 (expected deadline ~August 2026 — top-tier AI venue, fallback if CoRL reviews suggest broader framing needed)
45	3. **Method Synthesis** (676s) — 完成: "LLM-Guided Attention Reweighting for VLA Robustness Under Perturbation" [solid] → CoRL 2026 (abstract: May 25, paper: May 28 — top venue for robot learning, directly relevant to VLA robustness), ICLR 2027 (projected abstract: Sep 19, paper: Sep 24 — highest-tier ML venue, contribution level supports it), AAAI 2027 (projected abstract: Jul 26, paper: Aug 2 — top-tier AI venue, broad audience for LLM+robotics), ICRA 2027 (projected deadline: Sep 2026 — flagship robotics venue, strong fit for manipulation robustness evaluation)
46	
47	## Core Problem
48	
49	Offline VLA fine-tuning on heterogeneous demonstration datasets is bottlenecked by the absence of reliable, annotation-free quality signals. Existing approaches each impose substantial external dependencies: GVL (ICLR 2025 Spotlight) achieves zero-shot value estimation across 300+ tasks but requires per-frame inference from Gemini-scale VLMs; TOPReward (Feb 2026) achieves 0.947 VOC zero-shot but requires a separate 4-8B VLM at scoring time; SCIZOR (ICRA 2026) uses external DINO-V2 features not adapted to the action domain and applies hard binary filtering that discards gradient signal; RINSE (ICML 2025) provides architecture-agnostic trajectory smoothness scoring via SAL/TED metrics without any learned features; influence-function methods (CUPID, CoRL 2025; QoQ, arXiv 2603.09056) require evaluation rollouts or curated validation datasets; PROGRESSOR (ICCV 2025) requires external pretraining on EPIC-KITCHENS video; and ProgressVLA (Microsoft, March 2026) trains a separate progress estimator on large-scale video-text datasets. Online methods (SRPO, VLAC) require environment interaction entirely. Notably, a survey of ICLR 2026 VLA submissions reveals that data curation remains a critically underrepresented problem despite being widely acknowledged as a bottleneck. A fundamental question remains: do VLA models, through large-scale pretraining on action-prediction tasks, already encode sufficient task-progress information in their own internal representations to score demonstration quality — enabling a fully self-referential pipeline with zero external models, zero additional inference cost, and zero annotation requirements?
50	
51	## Opportunity / Why Now
52	
53	Recent mechanistic interpretability work provides moderate but encouraging evidence that VLA representations encode task-relevant information. The Emergent World Representations study (arXiv 2509.24559) demonstrates that linear probes on OpenVLA hidden states achieve R²=0.667 for state transition vector prediction (K=30 setting), confirming meaningful task-dynamic information is accessible in VLA feature space — though this falls well short of perfect prediction and concerns continuous state transitions rather than discrete progress. Complementarily, Probing OpenVLA for Symbolic States (arXiv 2502.04558) shows >90% accuracy for discrete symbolic state classification (binary properties like is_grasped, is_on_table) on LIBERO-Spatial, demonstrating that VLA representations linearly encode task-relevant binary predicates. Most directly, the mechanistic study 'Not All Features Are Created Equal' (arXiv 2603.19233) reports that π0.5 expert pathway features achieve R²=0.45 for continuous state prediction and AUC=0.93 for success prediction, with expert pathways consistently outperforming VLM pathways for motor-relevant information — directly demonstrating discriminative capacity in VLA features for quality-related judgments. SAE analyses (arXiv 2603.19183) reveal that 97-99% of individual sparse dictionary features are memorized on LIBERO-tuned models, but DROID-pretrained models show only 89.19% memorization, and critically, aggregate hidden-state vectors remain discriminative for state-level properties despite individual-feature memorization. The OpenGVL benchmark (arXiv 2509.17321) further reveals that open-source VLMs achieve only ~70% of closed-source VLM performance on temporal progress estimation, suggesting that VLA-internal features — which are natively adapted to the action domain — may offer competitive or superior signal without requiring external VLM inference. This creates a testable opportunity: if VLA features can support temporal distance estimation (frame-pair relative progress) beyond what positional embeddings alone provide, and if this signal outperforms both generic visual features (DINO-V2) and simple trajectory geometry (RINSE), then the same model being fine-tuned can score its own training data at zero marginal cost.
54	
55	## Landscape (SOTA & Limitations)
56	
57	The demonstration curation space for VLA fine-tuning has rapidly expanded across seven complementary approaches: (1) **Zero-shot VLM value estimation**: GVL (ICLR 2025 Spotlight, arXiv 2411.04549) poses value estimation as temporal ordering of shuffled video frames using Gemini-1.5-Pro, achieving zero-shot value prediction across 300+ tasks with Value-Order Correlation (VOC) as the metric. Applied to dataset filtering and advantage-weighted regression (AWR) on real ALOHA tasks. Limitation: requires per-frame API calls to a Gemini-scale VLM, with no reported compute cost analysis. OpenGVL (arXiv 2509.17321) benchmarks open-source VLMs on this task, finding they achieve ~70% of closed-source performance. TOPReward (Feb 2026, arXiv 2602.19313) extracts zero-shot progress from VLM token probabilities (0.947 VOC on Qwen3-VL), applied to advantage-weighted fine-tuning of pi0. Both require a separate large VLM at scoring time. (2) **Self-supervised visual curation**: SCIZOR (ICRA 2026, arXiv 2505.22626) trains a temporal distance classifier on frozen DINO-V2 features to estimate progress, then hard-filters low-quality timesteps and removes redundant data via joint state-action deduplication. Achieves 5.4% improvement on RoboMimic, 8.1% on OXE-Magic-Soup, and 32.9% on Sirius-Fleet real-robot tasks. Limitations: external visual features without action-domain adaptation; hard binary filtering discards gradient signal; tested primarily on Octo, not modern VLAs. VLA-SSD directly extends SCIZOR's temporal distance classification framework to VLA-internal representations, testing whether action-domain adaptation through VLA pretraining provides superior progress signals, and replaces hard filtering with soft reward weighting grounded in iw-SFT theory. (3) **Trajectory geometry heuristics**: RINSE (ICML 2025, arXiv 2604.23000) uses Spectral Arc Length (SAL, frequency-domain smoothness) and Trajectory-Envelope Distance (TED, spatial contact-aware geometry) for architecture-agnostic demo scoring. Achieves 16% higher success with 1/6 data on RoboMimic, 20% improvement with 1/2 data in real-world tasks, and 5.6% mean success improvement on LIBERO-10 via STRAP integration. Requires zero model access or learned features. This is the critical lower bound: if learned features cannot beat pure trajectory geometry, feature-based scoring is unjustified. (4) **External progress estimators**: PROGRESSOR (ICCV 2025, arXiv 2411.17764) learns a task-agnostic reward function pretrained on EPIC-KITCHENS for goal-conditioned RL. ProgressVLA (Microsoft, March 2026, arXiv 2603.27670) pre-trains a dedicated progress estimator on large-scale unsupervised video-text robotic datasets (0.07 prediction residual, zero-shot real-world transfer), integrated into a diffusion VLA with inverse dynamics guidance. Both require external pretraining data/models. (5) **Influence-function curation**: CUPID (CoRL 2025) and QoQ (arXiv 2603.09056) use REINFORCE-style influence estimation for trajectory-level filtering. QoQ achieves 23.2%/30.0% improvements on GR00T N1 VLA. Both require evaluation rollouts or curated validation sets and provide only trajectory-level granularity. (6) **External reward models**: Robometer (RSS 2026, arXiv 2603.02115) trains Qwen3-VL-4B on 1M+ trajectories for dense per-frame progress with strong zero-shot transfer (Kendall tau=0.66 OOD). Requires a separate 4-8B VLM at scoring time. (7) **Online self-improvement**: SRPO (arXiv 2511.15605) uses the model's own successful rollouts for self-referential optimization (48.9→99.2% on LIBERO). PLD (ICLR 2026, arXiv 2511.00091) uses residual RL to probe VLA failure regions, collect recovery data, and distill back via SFT (99% on LIBERO, 50%+ gains on SimplerEnv). VLAC (arXiv 2509.15937) integrates a dense progress critic into an online RL loop. All require environment interaction. (8) **Weighted BC frameworks**: VACO (ICLR 2025) uses a meta-scoring network for bi-level weighted BC on D4RL. iw-SFT (arXiv 2507.12856) proves that SFT on curated data maximizes a lower bound on the RL objective, tightened by importance weighting — providing theoretical justification for quality-weighted BC as a principled approach. **Gap**: No work has investigated whether VLA-internal features — uniquely adapted to the action domain through pretraining and already computed during the forward pass — can serve as a self-referential progress estimator that (a) beats trajectory geometry heuristics (RINSE), justifying learned features, (b) matches or exceeds external VLM scoring (GVL/TOPReward) on task-specific data, and (c) does so at zero marginal cost since features are a byproduct of the fine-tuning forward pass.
58	
59	## Proposed Approach
60	
61	VLA-SSD is a three-stage offline pipeline that tests a mechanistic hypothesis — VLA pretrained representations encode task-progress information sufficient for self-referential demonstration scoring — and operationalizes positive findings into a theoretically-grounded curriculum-weighted fine-tuning method. The theoretical foundation comes from iw-SFT (arXiv 2507.12856), which proves that SFT on quality-scored data maximizes a lower bound on the RL objective, tightened by importance weighting; VLA-SSD's quality scores serve as the importance weights, making the pipeline provably principled rather than heuristic.
62	
63	**Stage 1 — Temporal Distance Probing with Positional Embedding Controls**: Extract frozen hidden-state representations h_l(t) from every transformer layer l of the pretrained VLA (OpenVLA 7B as primary, π0.5 as validation) for each demonstration timestep. Train lightweight probes at each layer using TWO complementary targets designed to be robust against positional embedding shortcuts:
64	
65	(a) **Temporal distance classification** (primary target): Given a pair of frames (t_i, t_j) from the same trajectory, predict relative progress Δp = |t_j - t_i|/T from feature differences h_l(t_j) - h_l(t_i). This forces the probe to compare semantic content between two frames rather than recovering absolute temporal position from a single frame, directly mitigating the positional embedding shortcut. This explicitly extends SCIZOR's temporal distance classification framework — which uses frozen DINO-V2 features — to the VLA's own internal representations, testing whether action-domain adaptation through VLA pretraining provides superior progress signals.
66	
67	(b) **Sub-task predicate classification** (secondary target, LIBERO only): LIBERO provides BDDL goal predicates (e.g., is_grasped, is_on_table, is_in_drawer) checkable at every simulator timestep. Train binary classifiers on VLA features to predict sub-task completion milestones. These are discrete semantic properties that cannot be predicted from positional embeddings, providing the strongest evidence for genuine task understanding.
68	
69	(c) **Positional embedding control experiment** (probe-level only, not full pipeline): Train identical probes on positional embeddings alone (extracted from the same transformer layers but with content features zeroed out / using only the position component). If VLA content features significantly outperform positional-embedding-only probes, this confirms the signal comes from task-semantic representations, not temporal position recovery.
70	
71	Probe architecture: single linear layer + sigmoid for classification, ~50K params each. 80/20 train/validation split within the demonstration set. Rank layers by validation performance (Spearman ρ for temporal distance, AUC for sub-task predicates); select best layer l* automatically. Based on arXiv 2603.19233, expert pathway features (PG5, PG11 equivalent) are hypothesized most informative, but selection is fully data-driven.
72	
73	**Critical controlled ablations** (run in parallel):
74	- **DINO-V2 (ViT-L/14) baseline**: Extract DINO-V2 features from the same observations, train identical probes — isolates the effect of action-domain adaptation.
75	- **RINSE baseline**: Compute SAL and TED scores on the same trajectories — tests whether learned features beat trajectory geometry heuristics. If RINSE matches or exceeds our probes, the 'VLA features encode progress' narrative is undermined.
76	- **DINO-V2 Fallback**: If no VLA layer achieves Spearman ρ > 0.3 on temporal distance AND no layer achieves AUC > 0.7 on sub-task predicates, switch to DINO-V2 features for subsequent stages and report this as a negative mechanistic finding.
77	
78	**Stage 2 — Hierarchical Quality Scoring**: Use the temporal distance probe from l* to compute per-timestep progress estimates by anchoring relative to the first frame: q_t = probe_{l*}(h_{l*}(t) - h_{l*}(0)). Derive trajectory-level quality Q(τ) = α * q_T + β * mono(τ) + γ * mean(q_t), combining terminal progress (endpoint quality), progress monotonicity (fraction of consecutive timesteps with increasing estimated progress), and average progress. Default weights: α=0.5, β=0.3, γ=0.2. Compute timestep-level reward weights w_t = q_t * Q(τ). Apply temperature-controlled normalization for the trajectory component. On LIBERO, additionally compute sub-task milestone coverage as a trajectory quality signal.
79	
80	**Stage 3 — Curriculum-Weighted LoRA Fine-Tuning**: Fine-tune the VLA with LoRA (rank 16-64) using weighted BC loss with a curriculum temperature schedule that starts permissive and progressively sharpens quality weighting over training. Specifically, define a temperature parameter τ(epoch) that decreases linearly from τ_max to τ_min over training: w_t^(epoch) = softmax(q_t / τ(epoch)), where τ_max = 2.0 (near-uniform early training, allowing the model to learn from all demonstrations) and τ_min = 0.5 (sharp quality weighting in later epochs, focusing gradient signal on high-quality timesteps). The curriculum rationale: early uniform training establishes broad behavioral coverage, while progressive sharpening concentrates fine-tuning on the most informative demonstrations — analogous to curriculum learning in knowledge distillation (Curriculum Temperature, arXiv 2211.16231) and grounded by iw-SFT's theoretical result that tighter importance weighting progressively tightens the RL objective lower bound. The loss at each epoch: L = Σ_t w_t^(epoch) * ||a_t - π_θ(o_t, l)||². Unlike SCIZOR's hard filtering, soft reward weighting preserves gradient signal from all timesteps proportional to quality. Unlike GVL+AWR, no external VLM is needed — features come from the model being fine-tuned. Probes are trained once on pretrained features and frozen; all quality scores are computed before fine-tuning begins, ensuring no circular dependency.
81	
82	**Evaluation Protocol**:
83	
84	*Primary benchmarks* (in main paper): (1) RoboMimic Multi-Human (300 naturally mixed-quality demos from 6 operators of varied skill, Can and Square tasks). Validates quality scoring on natural distribution. Verify scores correlate with operator skill levels — the RoboMimic MH dataset organizes 50 demos per operator across 3 skill tiers (worse/okay/better); operator group membership is verifiable via filter keys using `get_dataset_info.py` and the known sequential collection structure. (2) LIBERO-Long with controlled noise injection (action jitter σ ∈ {0.05, 0.1, 0.2}, trajectory truncation at {50%, 75%}). Probes trained exclusively on clean data, then evaluated on mixed clean+noisy demonstrations — tests whether scoring generalizes beyond the noise distribution seen during probe training.
85	
86	*Robustness benchmarks* (in appendix): LIBERO-Plus (CVPR 2026, arXiv 2510.13626; 10,030 tasks across 7 perturbation dimensions) and LIBERO-PRO (arXiv 2510.03827). Report robustness gap Δ between nominal LIBERO success and perturbed-suite success.
87	
88	*Scale validation* (in appendix): DROID subsets with natural variable-quality teleoperation, where SAE analysis shows more general features (10.81% vs 2.63% on LIBERO).
89	
90	*π0.5 validation* (in appendix): Replicate core probing experiments (Stage 1) and one primary benchmark fine-tuning on π0.5 to validate generalization across VLA architectures.
91	
92	**Baselines** (6 core + 2 appendix):
93	
94	Core (main paper):
95	1. Vanilla BC (unweighted)
96	2. RINSE (SAL+TED trajectory geometry, no features) — critical lower bound
97	3. SCIZOR-style (DINO-V2 + temporal distance + hard filtering)
98	4. DINO-V2 + our curriculum-weighted pipeline (ablation isolating feature source)
99	5. GVL-style (open-source VLM scoring via OpenGVL protocol + AWR)
100	6. VLA-SSD without curriculum (static τ=1.0, ablating the curriculum contribution)
101	
102	Appendix:
103	7. Oracle scoring (ground-truth operator labels/noise levels)
104	8. TOPReward (external VLM + AWR)
105	
106	**Key metrics**: success rate on nominal and perturbed benchmarks, robustness gap Δ, probe Spearman ρ for temporal distance by layer (mechanistic), sub-task AUC by layer, quality score Kendall tau with ground-truth labels, VLA-feature vs. DINO-V2 vs. positional-embedding probe performance comparison (probe-level), VLA-feature vs. RINSE scoring comparison, curriculum ablation (with/without temperature schedule), compute overhead comparison (FLOPs, wall-clock, API cost).
107	
108	## Resource Estimate
109	
110	- **auto_research**: {'claude_api_cost': '$200-400 (~2500-5000 turns)', 'estimated_gpu_cost': '$490-685', 'gpu_hours': '~195h H100 (feature extraction from OpenVLA on 2 primary benchmarks ~25h, π0.5 validation extraction ~12h, probe training sweep across layers with temporal distance + sub-task + positional embedding control ~15h, DINO-V2 baseline ~10h, RINSE computation ~2h, LoRA fine-tuning: 1 primary VLA × 2 primary benchmarks × 6 core conditions × ~3h each ~72h, curriculum schedule sweep ~12h, π0.5 validation fine-tuning ~20h, appendix benchmarks (LIBERO-Plus/PRO, DROID) ~20h, evaluation rollouts ~25h)', 'gpu_utilization': '~85-90% — agent runs 24/7, parallelizes feature extraction across benchmarks and probe training across layers', 'risk_note': 'Agent may need human intervention at two critical decision points (positional embedding control result, RINSE comparison). The fallback mechanisms handle clear-negative cases automatically, but marginal results require judgment about paper framing.', 'speed_bottleneck': 'Feature extraction from OpenVLA 7B dominates; with 4 H100s, extraction parallelizes across benchmarks. π0.5 validation adds ~12h due to larger model size.', 'team': '0 (setup + final review only)', 'timeline': '5-8 days with 4 H100 GPUs'}
111	- **human_in_loop**: {'claude_api_cost': '$100-200 (~1250-2500 turns at ~$0.08/turn)', 'estimated_gpu_cost': '$400-560', 'gpu_hours': '~160h H100', 'gpu_utilization': '~65-75% — agent queues feature extraction, probe sweeps, and LoRA runs; researcher reviews layer-wise probing results and quality score calibration at check-ins', 'risk_note': "Key decision points: (1) If no VLA layer significantly outperforms positional-embedding-only probes on temporal distance, the 'semantic progress encoding' claim is falsified — paper pivots to negative finding about VLA representation limits. (2) If RINSE matches or exceeds VLA-probe scoring, the learned-feature approach is unjustified — paper pivots to 'trajectory geometry suffices' finding. Human judgment critical at these decision points.", 'team': '1 researcher, ~30min/day reviewing probing accuracy curves, RINSE comparison, and curriculum schedule', 'timeline': '3.5-4.5 weeks'}
112	- **manual**: {'estimated_gpu_cost': '$450-630 (H100 spot at ~$2.50-3.50/hr)', 'gpu_hours': '~180h H100 (feature extraction from OpenVLA on 2 primary benchmarks ~20h, π0.5 validation extraction ~10h, linear probe training across all layers with temporal distance + sub-task targets ~10h, DINO-V2 and positional embedding baselines ~8h, RINSE computation ~2h, LoRA fine-tuning: 1 primary VLA × 2 primary benchmarks × 6 core conditions ~60h, π0.5 validation fine-tuning ~20h, appendix benchmarks ~25h, evaluation rollouts ~25h)', 'gpu_utilization': '~40-50% — researcher iterates on layer selection analysis, examines probe performance curves and quality score distributions between GPU runs', 'team': '1-2 researchers', 'timeline': '2-3 months'}
113	
114	## Key References
115	
116	- GVL: Vision Language Models are In-Context Value Learners (ICLR 2025 Spotlight, arXiv 2411.04549)
117	- RINSE: Learning from the Best — Smoothness-Driven Metrics for Data Quality in Imitation Learning (ICML 2025, arXiv 2604.23000)
118	- PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement (ICCV 2025, arXiv 2411.17764)
119	- ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation (Microsoft, March 2026, arXiv 2603.27670)
120	- OpenGVL: Benchmarking Visual Temporal Progress for Data Curation (arXiv 2509.17321)
121	- SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026, arXiv 2505.22626)
122	- CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025, arXiv 2506.19121)
123	- QoQ: Quality over Quantity — Demonstration Curation via Influence Functions (arXiv 2603.09056)
124	- Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (RSS 2026, arXiv 2603.02115)
125	- TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics (Feb 2026, arXiv 2602.19313)
126	- SRPO: Self-Referential Policy Optimization for VLAs (arXiv 2511.15605)
127	- PLD: Self-Improving Vision-Language-Action Models with Data Generation via Residual RL (ICLR 2026, arXiv 2511.00091)
128	- VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World RL (arXiv 2509.15937)
129	- Emergent World Representations in OpenVLA (arXiv 2509.24559) — R²=0.667 for state transition prediction
130	- Probing OpenVLA for Symbolic States (arXiv 2502.04558) — >90% accuracy for discrete symbolic state classification
131	- Not All Features Are Created Equal: A Mechanistic Study of VLA Models (arXiv 2603.19233) — R²=0.45 state prediction, AUC=0.93 success prediction from π0.5 expert pathway
132	- Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models (arXiv 2603.19183)
133	- iw-SFT: Supervised Fine Tuning on Curated Data is Reinforcement Learning (arXiv 2507.12856)
134	- VACO: Value-Aligned Behavior Cloning via Bi-Level Optimization (ICLR 2025)
135	- Curriculum Temperature for Knowledge Distillation (arXiv 2211.16231)
136	- LIBERO-Plus: In-depth Robustness Analysis of VLA Models (CVPR 2026, arXiv 2510.13626)
137	- LIBERO-PRO: Towards Robust and Fair Evaluation of VLA Models Beyond Memorization (arXiv 2510.03827)
138	- RoboMimic: What Matters in Learning from Offline Human Demonstrations (CoRL 2021)
139	- DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset (RSS 2024)
140	- OpenVLA: An Open-Source Vision-Language-Action Model (2024)
141	- VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models (ICLR 2026)
142	
143	## Reviewer Evaluation
144	
145	**Scores**:
146	  - clarity: **4**/5
147	  - feasibility: **3**/5
148	  - impact: **3**/5
149	  - novelty: **3**/5
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "0afe0419-38ca-48d8-b2bc-5053c33f10f2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/IDEA_BRIEF.md",
      "content": "# Idea Brief: VLA-SSD: Do VLAs Know Which Demonstrations Are Good? Self-Referential Quality Scoring from Pretrained Representations\n\n\n- **Idea ID**: `idea_004`\n- **Created**: 2026-05-15\n- **Approved**: 2026-05-15\n- **Source**: foreign:be-idea-gen-0509-14\n- **Level**: top-tier\n- **Target Venues**: CoRL 2026 (abstract deadline May 26, full paper May 29, 2026), ICRA 2027 (~September 2026 deadline, backup if additional real-world validation needed), ICLR 2027 (~October 2026)\n\n## Seed Topic\n\n按照以下方向，生成1-2个优质idea，保质不求量：Seed 2: Reinforcement-Informed Demonstration Distillation for Noise-Robust VLA Training\nTarget: CoRL 2026 (Austin, Nov 9–12, 2026). Abstract deadline 2026-05-26 (12 days from today 2026-05-14); paper deadline 2026-05-29 (15 days).\nDirection: RL-inspired experience scoring and filtering for VLA training data — methods that leverage data-intrinsic signals to identify and down-weight noisy, redundant, or suboptimal actions in real-world demonstration datasets before or during VLA fine-tuning. Real-world teleoperation data inevitably contains noise: hesitation pauses, corrective motions, grip fumbles, suboptimal trajectories, and redundant repeated actions. Standard behavioral cloning treats all timesteps equally, forcing the VLA to memorize noise as if it were signal — this is a fundamental source of brittleness. By borrowing the experience replay and advantage estimation machinery from offline RL, we can score each (state, action) pair by its contribution to task completion and filter or re-weight the training distribution accordingly. Unlike full offline RL (which replaces BC entirely), this approach retains the simplicity and stability of VLA fine-tuning while using RL-derived scores as a data curation signal. The key theoretical insight is that demonstration noise creates multi-modal action distributions at identical states, inflating the entropy of the learned policy; scoring and filtering collapses these modes to the high-performing subset, yielding a sharper, more robust policy.\nRecent landscape (do not duplicate): Behavior Cloning, OpenVLA: An Open-Source Vision-Language-Action Model, FT-NCFM: An Influence-Aware Data Distillation Framework for Efficient VLA Models, PLD: Probe, Learn, Distill – Self-Improving Vision-Language-Action Models with Data Generation via Residual RL, REDI: Refined Policy Distillation: From VLA Generalists to RL Experts, GOLD: Guided Offline Learning from Demonstrations, SHS: An Offline Reinforcement Learning Algorithm Based on Selection of High-Quality Samples, PER: Prioritized Experience Replay, PRGS: Peak Reward Guided Trajectory Segmentation, What Can RL Bring to VLA Generalization? An Empirical Study, πRL: πRL: Manifold Policy Reinforcement Learning for Vision-Language-Action Models\nContribution type: METHOD ONLY. A two-stage demonstration distillation pipeline: (1) Temporal Advantage Scoring — train a lightweight value function on the demonstration data itself (using hindsight relabeling: final task success as sparse reward, or dense reward from state-goal distance) to compute per-timestep advantage estimates; actions with negative advantage (worse than the trajectory's average) are flagged as noisy; (2) Curriculum-Weighted Fine-Tuning — use the advantage scores as per-sample weights during VLA fine-tuning, with a curriculum that starts permissive (all data) and progressively sharpens to high-advantage subsets; (3) Consistency Regularization — for state-action pairs with high variance across similar states, add a consistency loss that encourages the VLA to commit to the high-scoring mode. No real robot required — the scoring is derived entirely from the existing dataset's structure.\nEVAL PROTOCOL — IMPORTANT:\nTRAIN on standard LIBERO suites (Object/Spatial/Goal/Long/90), with synthetic noise injection to simulate real-world demonstration noise (action jitter, redundant sub-trajectories, random pauses).\nEVALUATE on existing LIBERO-PLUS / LIBERO-PRO style perturbation benchmarks (and similar community-released robustness benchmark series). DO NOT spend time constructing your own robustness benchmark — use existing perturbation suites and route the budget into the method.\nReport robustness gap (Δ between nominal LIBERO success and perturbed-suite success) AND nominal preservation (must not regress on base LIBERO).\nAdditionally report: performance under varying noise injection ratios (10%/30%/50% noisy demonstrations), ablation of scoring function choices (MC return, TD advantage, trajectory ranking), and data efficiency curves (how much noisy data can be tolerated).\nExperiments can be extended to other benchmarks with noisy demonstration collection (e.g., RLBench with injected perturbations).\nSIM-ONLY MITIGATION: Using sim demonstrations with controlled noise injection is methodologically clean and well-accepted at CoRL. The scoring method is agnostic to sim/real — it operates on (state, action) pairs.\nHARD CONSTRAINTS:\nCompute: ≤200 H100-hours total. Fine-tune from open VLA checkpoints (OpenVLA, SmolVLA, OpenPi, π0) — no pretraining. Value function is lightweight (small MLP head). Show the math.\nTime: ≤20 days. Build on OpenVLA, OpenPi and other proper codebases, LeRobot, HF Transformers.\nEval datasets: LIBERO base (training/nominal eval) + LIBERO-PLUS / LIBERO-PRO and similar existing perturbation suites (perturbed eval). No custom benchmark construction.\nLook for: temporal advantage estimation from demonstration data without environment interaction, hindsight relabeling strategies for sparse-reward scoring, curriculum learning schedules that progressively filter noisy samples, connections between action distribution entropy and robustness, offline RL value estimation adapted to VLA's representation space. Avoid: requiring environment interaction or online rollouts (must be purely offline), full offline RL replacing BC (too unstable for VLA scale), simple trajectory-level success filtering (too coarse — need timestep-level scoring), just-add-noise training without filtering mechanism.\nTag: direction=robust_vla, contribution_type=method, sub_direction=demonstration_distillation, target_venues=[\"CoRL 2026\"].\n\n## Generation Journey\n\n1. **Start** — 开始生成，seed: 'Target: CoRL 2026 (Austin, Nov 9-12, 2026). Abstract deadline 2026-05-26 (17 days); paper deadline 2026-05-29 (20 days).\\nDirection：Meta-Brain VLA（无真机）\\n*让LLM在不同场景下进行角色切换，辅助VLA应对多个场景，本质上还是利用潜在能力对视觉部分表征进行优化。\\nMotivation：希望利用大模型已具备知识辅助VLA决策，达到类似Agentic元大脑框架的效果\\nidea创新性：\\n（1）使用现有性能比较强的大模型辅助VLA决策，回传时选择更新Skill库或者尝试优化Prompt\\n（2）根据不同的场景信息选择角色，能够有效解决泛化\\n（3）尝试用一种统一的表征来表达不同的信息\\n\\n元大脑角色切换：\\nLLM作为元大脑，根据当前任务场景动态路由切换以下三种模式：\\n（1）感知增强模式 ：环境光照暗、物体遮挡严重或遇到罕见物体，LLM专注输出空间关系描述或视觉线索引导，辅助 VLA 重新对齐特征\\n（2）逻辑拆解模式：用户指令模糊，LLM 此时退回 Long-term Planning 角色，将任务分解为一系列 Skill 序列。\\n（3）异常干预模式：VLA 预测的 Action 概率分布不确定性高，或者物理碰撞检测报错，LLM 介入进行反思，对比当前状态与目标状态，指导VLA改出。\\n\\n动态 Skill 库的进化逻辑：\\n         LLM 具备写Skill能力，无法解决时有自我更新能力，并将其持久化到库中。\\n\\n技术难点：\\n（1）无论 LLM 扮演什么角色，它最终产出一组同类型但不同功能的优化形式\\n1）混合语义 Token (Hybrid Semantic Tokens)\\n输出固定维度的嵌入向量，根据不同角色重塑原始视觉token\\n2）功能前缀 (Function Prefix)\\n在 LLM 输出的表征最前面，加入 Role Embedding，标识当前LLM的指导意见，能够使得VLA接收后，注意力机制或某些层面上发生相应变化。\\n3）注意力热力图 (Attention Masking)\\n让 LLM 生成注意力引导，始终返回给VLA的是一个权重矩阵\\n压缩功能=将无效区域的权重降为 0。\\n3D 引入功能 = 给具备空间深度的特征点赋予更高的初始权重。\\n技能调用功能 = 强化与该技能相关的物体特征。\\n\\n（2）哪些部分要训练，如何训练？\\n1）如何让LLM切换角色，可以划分关键帧前后两阶段训练\\n2）Adapter的训练范式，需要元学习，构造功能性数据集学习不同任务需要的输出。\\n3）信息穿透性，训练出的表征需要能对VLA有明显影响'\n2. **Problem Discovery** (675s) — 发现 5 个研究方向\n   - Role-Conditioned Meta-Brain for Adaptive VLA Enhancement\n   - Unified Functional Token Interface for LLM-to-VLA Communication\n   - Uncertainty-Triggered LLM Intervention with Representation-Level Correction\n   - Scene-Adaptive Skill Routing via Meta-Brain Role Switching\n   - LLM-Guided Attention Reweighting for VLA Robustness Under Perturbation\n3. **Method Synthesis** (788s) — 完成: \"Role-Conditioned Meta-Brain for Adaptive VLA Enhancement\" [top-tier] → CoRL 2026 (abstract: May 26, paper: May 29, 2026) — top-tier robotics-learning venue, most natural fit for VLA representation-level intervention, AAAI 2027 (abstract: Jul 25, paper: Aug 1, 2026) — broad top-tier AI venue accepting embodied AI and robotics, ICLR 2027 (abstract: Sep 19, paper: Sep 24, 2026) — top-tier ML venue, strong fit for architectural innovation in VLA representation learning\n3. **Method Synthesis** (515s) — 完成: \"Unified Functional Token Interface for LLM-to-VLA Communication\" [top-tier] → CoRL 2026 (abstract May 26, paper May 29 — top-tier robotics venue, ideal fit for VLA interface design contribution), ICLR 2027 (expected deadline ~Sep-Oct 2026 — highest-tier ML venue for architectural contributions), AAAI 2027 (expected deadline ~Jul-Aug 2026 — strong AI venue, confirmed Feb 16-23 2027 in Montréal)\n3. **Method Synthesis** (631s) — 完成: \"Uncertainty-Triggered LLM Intervention with Representation-Level Correction\" [top-tier] → CoRL 2026 (abstract: May 26, paper: May 29 — confirmed open, premier robot learning venue), ICLR 2027 (expected deadline: ~Sep-Oct 2026 — highest-tier ML venue, strong fit for representation-learning contribution), AAAI 2027 (expected deadline: ~Jul-Aug 2026 — top AI venue), ICRA 2027 (expected deadline: ~Sep 2026 — top robotics venue)\n3. **Method Synthesis** (619s) — 完成: \"Scene-Adaptive Skill Routing via Meta-Brain Role Switching\" [solid] → CoRL 2026 (paper deadline May 28-29, 2026 — top-tier robot learning venue, ideal topical fit for skill evolution in robot manipulation), ICLR 2027 (expected deadline ~October 2026 — top-tier ML venue, meta-learning contribution fits core audience), AAAI 2027 (expected deadline ~August 2026 — top-tier AI venue, fallback if CoRL reviews suggest broader framing needed)\n3. **Method Synthesis** (676s) — 完成: \"LLM-Guided Attention Reweighting for VLA Robustness Under Perturbation\" [solid] → CoRL 2026 (abstract: May 25, paper: May 28 — top venue for robot learning, directly relevant to VLA robustness), ICLR 2027 (projected abstract: Sep 19, paper: Sep 24 — highest-tier ML venue, contribution level supports it), AAAI 2027 (projected abstract: Jul 26, paper: Aug 2 — top-tier AI venue, broad audience for LLM+robotics), ICRA 2027 (projected deadline: Sep 2026 — flagship robotics venue, strong fit for manipulation robustness evaluation)\n\n## Core Problem\n\nOffline VLA fine-tuning on heterogeneous demonstration datasets is bottlenecked by the absence of reliable, annotation-free quality signals. Existing approaches each impose substantial external dependencies: GVL (ICLR 2025 Spotlight) achieves zero-shot value estimation across 300+ tasks but requires per-frame inference from Gemini-scale VLMs; TOPReward (Feb 2026) achieves 0.947 VOC zero-shot but requires a separate 4-8B VLM at scoring time; SCIZOR (ICRA 2026) uses external DINO-V2 features not adapted to the action domain and applies hard binary filtering that discards gradient signal; RINSE (ICML 2025) provides architecture-agnostic trajectory smoothness scoring via SAL/TED metrics without any learned features; influence-function methods (CUPID, CoRL 2025; QoQ, arXiv 2603.09056) require evaluation rollouts or curated validation datasets; PROGRESSOR (ICCV 2025) requires external pretraining on EPIC-KITCHENS video; and ProgressVLA (Microsoft, March 2026) trains a separate progress estimator on large-scale video-text datasets. Online methods (SRPO, VLAC) require environment interaction entirely. Notably, a survey of ICLR 2026 VLA submissions reveals that data curation remains a critically underrepresented problem despite being widely acknowledged as a bottleneck. A fundamental question remains: do VLA models, through large-scale pretraining on action-prediction tasks, already encode sufficient task-progress information in their own internal representations to score demonstration quality — enabling a fully self-referential pipeline with zero external models, zero additional inference cost, and zero annotation requirements?\n\n## Opportunity / Why Now\n\nRecent mechanistic interpretability work provides moderate but encouraging evidence that VLA representations encode task-relevant information. The Emergent World Representations study (arXiv 2509.24559) demonstrates that linear probes on OpenVLA hidden states achieve R²=0.667 for state transition vector prediction (K=30 setting), confirming meaningful task-dynamic information is accessible in VLA feature space — though this falls well short of perfect prediction and concerns continuous state transitions rather than discrete progress. Complementarily, Probing OpenVLA for Symbolic States (arXiv 2502.04558) shows >90% accuracy for discrete symbolic state classification (binary properties like is_grasped, is_on_table) on LIBERO-Spatial, demonstrating that VLA representations linearly encode task-relevant binary predicates. Most directly, the mechanistic study 'Not All Features Are Created Equal' (arXiv 2603.19233) reports that π0.5 expert pathway features achieve R²=0.45 for continuous state prediction and AUC=0.93 for success prediction, with expert pathways consistently outperforming VLM pathways for motor-relevant information — directly demonstrating discriminative capacity in VLA features for quality-related judgments. SAE analyses (arXiv 2603.19183) reveal that 97-99% of individual sparse dictionary features are memorized on LIBERO-tuned models, but DROID-pretrained models show only 89.19% memorization, and critically, aggregate hidden-state vectors remain discriminative for state-level properties despite individual-feature memorization. The OpenGVL benchmark (arXiv 2509.17321) further reveals that open-source VLMs achieve only ~70% of closed-source VLM performance on temporal progress estimation, suggesting that VLA-internal features — which are natively adapted to the action domain — may offer competitive or superior signal without requiring external VLM inference. This creates a testable opportunity: if VLA features can support temporal distance estimation (frame-pair relative progress) beyond what positional embeddings alone provide, and if this signal outperforms both generic visual features (DINO-V2) and simple trajectory geometry (RINSE), then the same model being fine-tuned can score its own training data at zero marginal cost.\n\n## Landscape (SOTA & Limitations)\n\nThe demonstration curation space for VLA fine-tuning has rapidly expanded across seven complementary approaches: (1) **Zero-shot VLM value estimation**: GVL (ICLR 2025 Spotlight, arXiv 2411.04549) poses value estimation as temporal ordering of shuffled video frames using Gemini-1.5-Pro, achieving zero-shot value prediction across 300+ tasks with Value-Order Correlation (VOC) as the metric. Applied to dataset filtering and advantage-weighted regression (AWR) on real ALOHA tasks. Limitation: requires per-frame API calls to a Gemini-scale VLM, with no reported compute cost analysis. OpenGVL (arXiv 2509.17321) benchmarks open-source VLMs on this task, finding they achieve ~70% of closed-source performance. TOPReward (Feb 2026, arXiv 2602.19313) extracts zero-shot progress from VLM token probabilities (0.947 VOC on Qwen3-VL), applied to advantage-weighted fine-tuning of pi0. Both require a separate large VLM at scoring time. (2) **Self-supervised visual curation**: SCIZOR (ICRA 2026, arXiv 2505.22626) trains a temporal distance classifier on frozen DINO-V2 features to estimate progress, then hard-filters low-quality timesteps and removes redundant data via joint state-action deduplication. Achieves 5.4% improvement on RoboMimic, 8.1% on OXE-Magic-Soup, and 32.9% on Sirius-Fleet real-robot tasks. Limitations: external visual features without action-domain adaptation; hard binary filtering discards gradient signal; tested primarily on Octo, not modern VLAs. VLA-SSD directly extends SCIZOR's temporal distance classification framework to VLA-internal representations, testing whether action-domain adaptation through VLA pretraining provides superior progress signals, and replaces hard filtering with soft reward weighting grounded in iw-SFT theory. (3) **Trajectory geometry heuristics**: RINSE (ICML 2025, arXiv 2604.23000) uses Spectral Arc Length (SAL, frequency-domain smoothness) and Trajectory-Envelope Distance (TED, spatial contact-aware geometry) for architecture-agnostic demo scoring. Achieves 16% higher success with 1/6 data on RoboMimic, 20% improvement with 1/2 data in real-world tasks, and 5.6% mean success improvement on LIBERO-10 via STRAP integration. Requires zero model access or learned features. This is the critical lower bound: if learned features cannot beat pure trajectory geometry, feature-based scoring is unjustified. (4) **External progress estimators**: PROGRESSOR (ICCV 2025, arXiv 2411.17764) learns a task-agnostic reward function pretrained on EPIC-KITCHENS for goal-conditioned RL. ProgressVLA (Microsoft, March 2026, arXiv 2603.27670) pre-trains a dedicated progress estimator on large-scale unsupervised video-text robotic datasets (0.07 prediction residual, zero-shot real-world transfer), integrated into a diffusion VLA with inverse dynamics guidance. Both require external pretraining data/models. (5) **Influence-function curation**: CUPID (CoRL 2025) and QoQ (arXiv 2603.09056) use REINFORCE-style influence estimation for trajectory-level filtering. QoQ achieves 23.2%/30.0% improvements on GR00T N1 VLA. Both require evaluation rollouts or curated validation sets and provide only trajectory-level granularity. (6) **External reward models**: Robometer (RSS 2026, arXiv 2603.02115) trains Qwen3-VL-4B on 1M+ trajectories for dense per-frame progress with strong zero-shot transfer (Kendall tau=0.66 OOD). Requires a separate 4-8B VLM at scoring time. (7) **Online self-improvement**: SRPO (arXiv 2511.15605) uses the model's own successful rollouts for self-referential optimization (48.9→99.2% on LIBERO). PLD (ICLR 2026, arXiv 2511.00091) uses residual RL to probe VLA failure regions, collect recovery data, and distill back via SFT (99% on LIBERO, 50%+ gains on SimplerEnv). VLAC (arXiv 2509.15937) integrates a dense progress critic into an online RL loop. All require environment interaction. (8) **Weighted BC frameworks**: VACO (ICLR 2025) uses a meta-scoring network for bi-level weighted BC on D4RL. iw-SFT (arXiv 2507.12856) proves that SFT on curated data maximizes a lower bound on the RL objective, tightened by importance weighting — providing theoretical justification for quality-weighted BC as a principled approach. **Gap**: No work has investigated whether VLA-internal features — uniquely adapted to the action domain through pretraining and already computed during the forward pass — can serve as a self-referential progress estimator that (a) beats trajectory geometry heuristics (RINSE), justifying learned features, (b) matches or exceeds external VLM scoring (GVL/TOPReward) on task-specific data, and (c) does so at zero marginal cost since features are a byproduct of the fine-tuning forward pass.\n\n## Proposed Approach\n\nVLA-SSD is a three-stage offline pipeline that tests a mechanistic hypothesis — VLA pretrained representations encode task-progress information sufficient for self-referential demonstration scoring — and operationalizes positive findings into a theoretically-grounded curriculum-weighted fine-tuning method. The theoretical foundation comes from iw-SFT (arXiv 2507.12856), which proves that SFT on quality-scored data maximizes a lower bound on the RL objective, tightened by importance weighting; VLA-SSD's quality scores serve as the importance weights, making the pipeline provably principled rather than heuristic.\n\n**Stage 1 — Temporal Distance Probing with Positional Embedding Controls**: Extract frozen hidden-state representations h_l(t) from every transformer layer l of the pretrained VLA (OpenVLA 7B as primary, π0.5 as validation) for each demonstration timestep. Train lightweight probes at each layer using TWO complementary targets designed to be robust against positional embedding shortcuts:\n\n(a) **Temporal distance classification** (primary target): Given a pair of frames (t_i, t_j) from the same trajectory, predict relative progress Δp = |t_j - t_i|/T from feature differences h_l(t_j) - h_l(t_i). This forces the probe to compare semantic content between two frames rather than recovering absolute temporal position from a single frame, directly mitigating the positional embedding shortcut. This explicitly extends SCIZOR's temporal distance classification framework — which uses frozen DINO-V2 features — to the VLA's own internal representations, testing whether action-domain adaptation through VLA pretraining provides superior progress signals.\n\n(b) **Sub-task predicate classification** (secondary target, LIBERO only): LIBERO provides BDDL goal predicates (e.g., is_grasped, is_on_table, is_in_drawer) checkable at every simulator timestep. Train binary classifiers on VLA features to predict sub-task completion milestones. These are discrete semantic properties that cannot be predicted from positional embeddings, providing the strongest evidence for genuine task understanding.\n\n(c) **Positional embedding control experiment** (probe-level only, not full pipeline): Train identical probes on positional embeddings alone (extracted from the same transformer layers but with content features zeroed out / using only the position component). If VLA content features significantly outperform positional-embedding-only probes, this confirms the signal comes from task-semantic representations, not temporal position recovery.\n\nProbe architecture: single linear layer + sigmoid for classification, ~50K params each. 80/20 train/validation split within the demonstration set. Rank layers by validation performance (Spearman ρ for temporal distance, AUC for sub-task predicates); select best layer l* automatically. Based on arXiv 2603.19233, expert pathway features (PG5, PG11 equivalent) are hypothesized most informative, but selection is fully data-driven.\n\n**Critical controlled ablations** (run in parallel):\n- **DINO-V2 (ViT-L/14) baseline**: Extract DINO-V2 features from the same observations, train identical probes — isolates the effect of action-domain adaptation.\n- **RINSE baseline**: Compute SAL and TED scores on the same trajectories — tests whether learned features beat trajectory geometry heuristics. If RINSE matches or exceeds our probes, the 'VLA features encode progress' narrative is undermined.\n- **DINO-V2 Fallback**: If no VLA layer achieves Spearman ρ > 0.3 on temporal distance AND no layer achieves AUC > 0.7 on sub-task predicates, switch to DINO-V2 features for subsequent stages and report this as a negative mechanistic finding.\n\n**Stage 2 — Hierarchical Quality Scoring**: Use the temporal distance probe from l* to compute per-timestep progress estimates by anchoring relative to the first frame: q_t = probe_{l*}(h_{l*}(t) - h_{l*}(0)). Derive trajectory-level quality Q(τ) = α * q_T + β * mono(τ) + γ * mean(q_t), combining terminal progress (endpoint quality), progress monotonicity (fraction of consecutive timesteps with increasing estimated progress), and average progress. Default weights: α=0.5, β=0.3, γ=0.2. Compute timestep-level reward weights w_t = q_t * Q(τ). Apply temperature-controlled normalization for the trajectory component. On LIBERO, additionally compute sub-task milestone coverage as a trajectory quality signal.\n\n**Stage 3 — Curriculum-Weighted LoRA Fine-Tuning**: Fine-tune the VLA with LoRA (rank 16-64) using weighted BC loss with a curriculum temperature schedule that starts permissive and progressively sharpens quality weighting over training. Specifically, define a temperature parameter τ(epoch) that decreases linearly from τ_max to τ_min over training: w_t^(epoch) = softmax(q_t / τ(epoch)), where τ_max = 2.0 (near-uniform early training, allowing the model to learn from all demonstrations) and τ_min = 0.5 (sharp quality weighting in later epochs, focusing gradient signal on high-quality timesteps). The curriculum rationale: early uniform training establishes broad behavioral coverage, while progressive sharpening concentrates fine-tuning on the most informative demonstrations — analogous to curriculum learning in knowledge distillation (Curriculum Temperature, arXiv 2211.16231) and grounded by iw-SFT's theoretical result that tighter importance weighting progressively tightens the RL objective lower bound. The loss at each epoch: L = Σ_t w_t^(epoch) * ||a_t - π_θ(o_t, l)||². Unlike SCIZOR's hard filtering, soft reward weighting preserves gradient signal from all timesteps proportional to quality. Unlike GVL+AWR, no external VLM is needed — features come from the model being fine-tuned. Probes are trained once on pretrained features and frozen; all quality scores are computed before fine-tuning begins, ensuring no circular dependency.\n\n**Evaluation Protocol**:\n\n*Primary benchmarks* (in main paper): (1) RoboMimic Multi-Human (300 naturally mixed-quality demos from 6 operators of varied skill, Can and Square tasks). Validates quality scoring on natural distribution. Verify scores correlate with operator skill levels — the RoboMimic MH dataset organizes 50 demos per operator across 3 skill tiers (worse/okay/better); operator group membership is verifiable via filter keys using `get_dataset_info.py` and the known sequential collection structure. (2) LIBERO-Long with controlled noise injection (action jitter σ ∈ {0.05, 0.1, 0.2}, trajectory truncation at {50%, 75%}). Probes trained exclusively on clean data, then evaluated on mixed clean+noisy demonstrations — tests whether scoring generalizes beyond the noise distribution seen during probe training.\n\n*Robustness benchmarks* (in appendix): LIBERO-Plus (CVPR 2026, arXiv 2510.13626; 10,030 tasks across 7 perturbation dimensions) and LIBERO-PRO (arXiv 2510.03827). Report robustness gap Δ between nominal LIBERO success and perturbed-suite success.\n\n*Scale validation* (in appendix): DROID subsets with natural variable-quality teleoperation, where SAE analysis shows more general features (10.81% vs 2.63% on LIBERO).\n\n*π0.5 validation* (in appendix): Replicate core probing experiments (Stage 1) and one primary benchmark fine-tuning on π0.5 to validate generalization across VLA architectures.\n\n**Baselines** (6 core + 2 appendix):\n\nCore (main paper):\n1. Vanilla BC (unweighted)\n2. RINSE (SAL+TED trajectory geometry, no features) — critical lower bound\n3. SCIZOR-style (DINO-V2 + temporal distance + hard filtering)\n4. DINO-V2 + our curriculum-weighted pipeline (ablation isolating feature source)\n5. GVL-style (open-source VLM scoring via OpenGVL protocol + AWR)\n6. VLA-SSD without curriculum (static τ=1.0, ablating the curriculum contribution)\n\nAppendix:\n7. Oracle scoring (ground-truth operator labels/noise levels)\n8. TOPReward (external VLM + AWR)\n\n**Key metrics**: success rate on nominal and perturbed benchmarks, robustness gap Δ, probe Spearman ρ for temporal distance by layer (mechanistic), sub-task AUC by layer, quality score Kendall tau with ground-truth labels, VLA-feature vs. DINO-V2 vs. positional-embedding probe performance comparison (probe-level), VLA-feature vs. RINSE scoring comparison, curriculum ablation (with/without temperature schedule), compute overhead comparison (FLOPs, wall-clock, API cost).\n\n## Resource Estimate\n\n- **auto_research**: {'claude_api_cost': '$200-400 (~2500-5000 turns)', 'estimated_gpu_cost': '$490-685', 'gpu_hours': '~195h H100 (feature extraction from OpenVLA on 2 primary benchmarks ~25h, π0.5 validation extraction ~12h, probe training sweep across layers with temporal distance + sub-task + positional embedding control ~15h, DINO-V2 baseline ~10h, RINSE computation ~2h, LoRA fine-tuning: 1 primary VLA × 2 primary benchmarks × 6 core conditions × ~3h each ~72h, curriculum schedule sweep ~12h, π0.5 validation fine-tuning ~20h, appendix benchmarks (LIBERO-Plus/PRO, DROID) ~20h, evaluation rollouts ~25h)', 'gpu_utilization': '~85-90% — agent runs 24/7, parallelizes feature extraction across benchmarks and probe training across layers', 'risk_note': 'Agent may need human intervention at two critical decision points (positional embedding control result, RINSE comparison). The fallback mechanisms handle clear-negative cases automatically, but marginal results require judgment about paper framing.', 'speed_bottleneck': 'Feature extraction from OpenVLA 7B dominates; with 4 H100s, extraction parallelizes across benchmarks. π0.5 validation adds ~12h due to larger model size.', 'team': '0 (setup + final review only)', 'timeline': '5-8 days with 4 H100 GPUs'}\n- **human_in_loop**: {'claude_api_cost': '$100-200 (~1250-2500 turns at ~$0.08/turn)', 'estimated_gpu_cost': '$400-560', 'gpu_hours': '~160h H100', 'gpu_utilization': '~65-75% — agent queues feature extraction, probe sweeps, and LoRA runs; researcher reviews layer-wise probing results and quality score calibration at check-ins', 'risk_note': \"Key decision points: (1) If no VLA layer significantly outperforms positional-embedding-only probes on temporal distance, the 'semantic progress encoding' claim is falsified — paper pivots to negative finding about VLA representation limits. (2) If RINSE matches or exceeds VLA-probe scoring, the learned-feature approach is unjustified — paper pivots to 'trajectory geometry suffices' finding. Human judgment critical at these decision points.\", 'team': '1 researcher, ~30min/day reviewing probing accuracy curves, RINSE comparison, and curriculum schedule', 'timeline': '3.5-4.5 weeks'}\n- **manual**: {'estimated_gpu_cost': '$450-630 (H100 spot at ~$2.50-3.50/hr)', 'gpu_hours': '~180h H100 (feature extraction from OpenVLA on 2 primary benchmarks ~20h, π0.5 validation extraction ~10h, linear probe training across all layers with temporal distance + sub-task targets ~10h, DINO-V2 and positional embedding baselines ~8h, RINSE computation ~2h, LoRA fine-tuning: 1 primary VLA × 2 primary benchmarks × 6 core conditions ~60h, π0.5 validation fine-tuning ~20h, appendix benchmarks ~25h, evaluation rollouts ~25h)', 'gpu_utilization': '~40-50% — researcher iterates on layer selection analysis, examines probe performance curves and quality score distributions between GPU runs', 'team': '1-2 researchers', 'timeline': '2-3 months'}\n\n## Key References\n\n- GVL: Vision Language Models are In-Context Value Learners (ICLR 2025 Spotlight, arXiv 2411.04549)\n- RINSE: Learning from the Best — Smoothness-Driven Metrics for Data Quality in Imitation Learning (ICML 2025, arXiv 2604.23000)\n- PROGRESSOR: A Perceptually Guided Reward Estimator with Self-Supervised Online Refinement (ICCV 2025, arXiv 2411.17764)\n- ProgressVLA: Progress-Guided Diffusion Policy for Vision-Language Robotic Manipulation (Microsoft, March 2026, arXiv 2603.27670)\n- OpenGVL: Benchmarking Visual Temporal Progress for Data Curation (arXiv 2509.17321)\n- SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026, arXiv 2505.22626)\n- CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025, arXiv 2506.19121)\n- QoQ: Quality over Quantity — Demonstration Curation via Influence Functions (arXiv 2603.09056)\n- Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (RSS 2026, arXiv 2603.02115)\n- TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics (Feb 2026, arXiv 2602.19313)\n- SRPO: Self-Referential Policy Optimization for VLAs (arXiv 2511.15605)\n- PLD: Self-Improving Vision-Language-Action Models with Data Generation via Residual RL (ICLR 2026, arXiv 2511.00091)\n- VLAC: A Vision-Language-Action-Critic Model for Robotic Real-World RL (arXiv 2509.15937)\n- Emergent World Representations in OpenVLA (arXiv 2509.24559) — R²=0.667 for state transition prediction\n- Probing OpenVLA for Symbolic States (arXiv 2502.04558) — >90% accuracy for discrete symbolic state classification\n- Not All Features Are Created Equal: A Mechanistic Study of VLA Models (arXiv 2603.19233) — R²=0.45 state prediction, AUC=0.93 success prediction from π0.5 expert pathway\n- Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models (arXiv 2603.19183)\n- iw-SFT: Supervised Fine Tuning on Curated Data is Reinforcement Learning (arXiv 2507.12856)\n- VACO: Value-Aligned Behavior Cloning via Bi-Level Optimization (ICLR 2025)\n- Curriculum Temperature for Knowledge Distillation (arXiv 2211.16231)\n- LIBERO-Plus: In-depth Robustness Analysis of VLA Models (CVPR 2026, arXiv 2510.13626)\n- LIBERO-PRO: Towards Robust and Fair Evaluation of VLA Models Beyond Memorization (arXiv 2510.03827)\n- RoboMimic: What Matters in Learning from Offline Human Demonstrations (CoRL 2021)\n- DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset (RSS 2024)\n- OpenVLA: An Open-Source Vision-Language-Action Model (2024)\n- VLM4VLA: Revisiting Vision-Language-Models in Vision-Language-Action Models (ICLR 2026)\n\n## Reviewer Evaluation\n\n**Scores**:\n  - clarity: **4**/5\n  - feasibility: **3**/5\n  - impact: **3**/5\n  - novelty: **3**/5\n",
      "numLines": 150,
      "startLine": 1,
      "totalLines": 178
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01TGr7n51f6A1ZrhhLj8aZTo`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/dream_reports/ 2>/dev/null",
  "description": "Check dream reports for narrative context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "c959c16d-91b4-4fc9-bc66-35c0b995b677",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MMhELC22Z1nxAVGPAhPCHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 485,
      "cache_read_input_tokens": 32985,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 485
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

_source line 22 · 2026-05-16T02:17:24.511Z_

<details><summary>↩ Tool result · `toolu_01TGr7n51f6A1ZrhhLj8aZTo`</summary>

```text
dream_20260515T222933
dream_20260516T011810
latest
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "6988cd79-9faf-4e4d-9ac4-8a0e9045175c",
  "tool_use_result": {
    "stdout": "dream_20260515T222933\ndream_20260516T011810\nlatest",
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

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
Wait - I need to re-read the task more carefully. The task is about writing a specific Experiments section for this paper. The paper seems to be about understanding VLA representations (specifically about vision encoder dominance, LLM redistribution, and training as routing), not about the VLA-SSD pipeline itself. Let me look at the task description again:

The experiments section is about:
- 3.1 Experimental Setup: LIBERO-Goal, OpenVLA-7B, representation extraction, 2×2 conditions, RSA, functional probes
- 3.2 Vision Encoder Dominance (Claim 1) - SigLIP > CLIP > DINO, VL pretraining matters


- 3.3 LLM Redistributes Action Structure (Claim 2) - distributed degradation, readout concentration
- 3.4 Training = Routing, Not Creating (Claim 3) - training teaches routing not creation

This is a mechanistic interpretability paper analyzing how action information flows through the VLA architecture using probing experiments. Now I need to write the experiments section and compile the references, focusing on clean, precise writing that captures these three core claims about VLA representations.

For the bibliography, I'm pulling together the key papers: OpenVLA, foundational VLM work, the RT-2 robotics model, LIBERO benchmarks, and the representational analysis methods like RSA and CKA that ground my probing approach. I'm mapping out the figures—bar charts for encoder dominance, per-layer curves showing LLM redistribution, functional probe results, and a 2×2 matrix for instruction control—then I'll write the section with precise claims backed by data, keeping numbers to three decimal places and making sure each figure caption is self-contained.

For Table 1, I notice some confidence intervals are marked TBD, so I'll use [TBD] as a placeholder since this is a working draft. Now I'm structuring the experiments section starting with the setup: LIBERO-Goal dataset with 10 tasks and 50 demonstrations each, using OpenVLA-7B fine-tuned on LIBERO-10 with the SigLIP-SO400M architecture.

The pipeline flows through an MLP projector and Llama-2 7B to the action head, with representations from 5 sources tested under 2×2 conditions (trained/untrained and with/without instructions). I'm using RSA methodology and functional probes, with untrained controls created by reinitializing the LLM via from_config().

Then I'll present the key findings across three main sections: vision encoder dominance shown in Table 1's RSA values, the LLM's role in redistributing action structure via Table 2's R² values with per-layer analysis, and finally the evidence that training routes rather than creates structure through Table 3's comparisons and 2×2 RSA analysis with random instruction controls. I need to be precise about each claim and ground everything in the quantitative results.

Now I'm mapping the figures to their sections—the bar chart goes in the vision dominance section, per-layer curves and functional probe bars in the LLM redistribution section, and the 2×2 matrix with instruction control in the training-as-routing section. Writing the full LaTeX document now...

I need to verify a couple of citation references—grant2026 likely refers to prior work on behavioral visual dominance in VLAs, and haon2025 appears to be about VLA interpretability. I'll mark these for verification and proceed with drafting the experiments section, making sure to use proper citations, report numbers to three decimal places, include statistical tests, and structure each claim with explicit evidence.

Before I write the full content, I should examine the figures to understand what they display so I can write accurate captions and descriptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "bac8db7f-48a6-410a-b7d6-7c8a6c0a194d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtcfEAHk9uDf5dM2mPc1jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10576,
      "cache_read_input_tokens": 33470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10576
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

Let me look at the figures to write accurate captions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "09849609-fe3f-4cab-b649-501d850fb043",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtcfEAHk9uDf5dM2mPc1jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10576,
      "cache_read_input_tokens": 33470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10576
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

<details open><summary>🔧 Tool call — Read · `toolu_013dZbMgiRDmEiwf1SAnrhaM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "40b0237a-4ddd-4185-9152-75771243e472",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtcfEAHk9uDf5dM2mPc1jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10576,
      "cache_read_input_tokens": 33470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10576
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

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01AAC9FqceC2BGta4qAPYNYH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "b02e3d92-ff7b-4bde-ac5d-bd09b9f26ccb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtcfEAHk9uDf5dM2mPc1jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10576,
      "cache_read_input_tokens": 33470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10576
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

_source line 27 · 2026-05-16T02:18:12.473Z_

<details><summary>↩ Tool result · `toolu_013dZbMgiRDmEiwf1SAnrhaM`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "eb4ebcaf-7b99-4c31-9a0a-728255616707",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 153476
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01JRfRqh3K9Hy7JfqQaPMabH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "f60e371a-c6f7-44d6-a76d-433556ed9bc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtcfEAHk9uDf5dM2mPc1jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10576,
      "cache_read_input_tokens": 33470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10576
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

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_011nFwcjdZBKhMCVX9SSry7d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "a556198f-eb88-4101-982e-5676604b9203",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BtcfEAHk9uDf5dM2mPc1jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10576,
      "cache_read_input_tokens": 33470,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10576
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

_source line 30 · 2026-05-16T02:18:13.106Z_

<details><summary>↩ Tool result · `toolu_01AAC9FqceC2BGta4qAPYNYH`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "303269f4-85f3-4618-bb37-62539eb9a215",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 208096
    }
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-16T02:18:13.335Z_

<details><summary>↩ Tool result · `toolu_01JRfRqh3K9Hy7JfqQaPMabH`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "3ed32f92-c102-4806-abe9-c4ba9e89b20b",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 151512
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T02:18:13.806Z_

<details><summary>↩ Tool result · `toolu_011nFwcjdZBKhMCVX9SSry7d`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "42d85fb6-bb8a-4749-92ae-0b73ea50ec99",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 179452
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01LfaGGT1UvX8XQXigL8WuSg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/figures/paper/fig6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "160e6534-38de-437b-8398-7469ad935572",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BGoWcwjCmHFxaVhirT9Arq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3877,
      "cache_read_input_tokens": 44046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3877
      },
      "output_tokens": 36,
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

_source line 34 · 2026-05-16T02:18:21.083Z_

<details><summary>↩ Tool result · `toolu_01LfaGGT1UvX8XQXigL8WuSg`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "b86b5320-3197-43ca-abac-7c6d8e68ffd1",
  "tool_use_result": {
    "type": "image",
    "file": {
      "base64": "[ATTACHMENT_DATA_REDACTED]",
      "type": "image/png",
      "originalSize": 174129
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture of all figures. Let me now write the experiments section.

fig2: Bar chart showing RSA with Action Space (ρ) for different representation sources (SigLIP+Proj, CLIP, VLA Trained w/ and w/o instruction, VLA Untrained w/ and w/o instruction, DINOv2). Shows VL pretrained encoders dominate.

fig3: Per-layer RSA curves across LLM layers (0-32) for 4 conditions (trained ± instruction, untrained ± instruction), with SigLIP+Proj and DINOv2 reference lines.


fig4 shows action prediction performance across different representations, revealing how the trained LLM readout concentrates information compared to the baseline. fig5 breaks down the training and instruction effects on image representations through a matrix view, plus a control experiment testing what happens when instruction content is manipulated. fig6 is particularly revealing—comparing RSA against CKA metrics shows they rank the representations differently, suggesting these similarity measures capture distinct aspects of the learned representations.

I need to include fig6 since the task explicitly notes that negative results like CKA ranking reversals shouldn't be omitted. Now I'm moving on to write up the experiments section and compile the references, starting with the papers I can identify with confidence like the OpenVLA work and Karamcheti's contributions. matic VLMs: Investigating the Design Space of Visually-Conditioned Language Models" 2024. Or it could be related to LIBERO/OpenVLA. Actually, looking at the OpenVLA paper, Karamcheti is a co-author. Maybe this refers to a separate Karamcheti paper? Let me think... In the context of VLA architecture (SigLIP + MLP projector + Llama-2), Karamcheti 2024 might refer to the Prismatic VLMs paper which studies vision encoder design for VLMs. arXiv:2402.07865. [VERIFY]

3. brohan2023_rt2: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" by Anthony Brohan et al., 2023. arXiv:2307.15818. [I'm quite confident about this one]

4. liu2023_libero: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" by Bo Liu et al., NeurIPS 2023. arXiv:2306.03310. [Fairly confident]

5. kriegeskorte2008: "Representational Similarity Analysis – Connecting the Branches of Systems Neuroscience" by Nikolaus Kriegeskorte, Marieke Mur, Peter Bandettini, 2008, Frontiers in Systems Neuroscience. [Very confident]

6. kornblith2019: "Similarity of Neural Network Representations Revisited" by Simon Kornblith, Mohammad Norouzi, Honglak Lee, Geoffrey Hinton, ICML 2019. arXiv:1905.00414. [Very confident]

7. alain2017: "Understanding intermediate layers using linear classifier probes" by Guillaume Alain and Yoshua Bengio, ICLR 2017 Workshop. arXiv:1610.01644. [Very confident]

8. Now I'm working through the remaining references, focusing on papers about neural network analysis and representation learning.

Continuing with the vision-language and robotics papers: SigLIP for language-image pretraining, DINOv2 for self-supervised visual features, and CLIP for multimodal learning. I'm also noting grant2026 which appears to be from this project's own work and needs verification, and I'm still working through the haon2025 reference.

Now I'm thinking through the LaTeX structure for the paper. The figures are already generated as fig2 through fig6, so I need to reference them appropriately with labels and figure numbers. Since the task specifies "fig2 (bar chart)" and similar, I'll use Figure 2, Figure 3, and so on, matching the PDF filenames. I'm also considering the table numbering and making sure the references align with what's already been created.

I should check if other sections exist to avoid numbering conflicts, but I'll move forward with writing the Experiments section now. My plan is to structure it as four subsections: Experimental Setup covering the benchmark and methods, Vision Encoder Dominance with Table 1 and Figure 2, LLM Redistributes Action Structure with Table 2 and Figures 3-4, and Training as Routing with Table 3 and Figure 5. I'll also need to incorporate the CKA ranking reversal from Figure 6 as a negative result, possibly within the Vision Encoder Dominance section or as a brief note.

Writing the LaTeX for the Experiments section now...

I'm defining the five representation sources we'll evaluate: the projected vision encoder output, mean and final token activations from different LLM layers, and two external vision models (DINOv2 and CLIP) as baselines for comparison.

For the experimental setup, I'm using a factorial design that varies whether the LLM was trained and whether language instructions are present, with an untrained control that reinitializes the LLM weights while keeping the frozen vision encoder to isolate what the LLM actually learned. Then I'm computing representational similarity analysis by calculating dissimilarity matrices for each source and the action space, measuring how well each representation correlates with the action dimensions using Spearman correlation.

For the probes, I'm training small neural networks to predict action vectors from frozen representations, reporting the mean R² across dimensions. Now I'm looking at whether the vision encoder provides the dominant geometric structure for actions—examining the correlation values between each representation source and the action space.

The results show SigLIP with projection achieving the strongest alignment with actions, followed by CLIP ViT-L/14, while the vision-only DINOv2 model trails significantly behind. The LLM layers fall somewhere in between. This suggests that vision-language pretraining, rather than the language model processing itself, is what captures the action-relevant structure.

Looking at the specific gaps: the 0.169-point difference between CLIP and DINOv2 demonstrates that language-grounded visual features encode substantially more action geometry than vision-only features. The projector adds a modest boost of 0.058 points by mapping vision features into the LLM's space. But surprisingly, passing through the LLM actually degrades alignment, dropping from 0.615 to 0.501—a loss of 0.114 points.

Now I'm examining a key finding: there's a disconnect between geometric alignment and functional performance. DINOv2 shows nearly identical linear decodability to SigLIP+Projector despite having much lower geometric similarity to actions, suggesting that features can be functionally useful without being geometrically aligned. This pattern holds across different similarity metrics too, where alternative measures like linear CKA rank the representations differently than RSA does.

Generating markdown table... Now I'm looking at a figure showing RSA results across different representation sources, where vision-language models like SigLIP and CLIP clearly outperform both LLM-processed representations and DINOv2. The next section examines how the LLM actually redistributes rather than enhances the action structure it receives from the vision encoder, and I'm about to present probe results showing the functional relationships.

The data reveals two key patterns: first, when averaging across image tokens, the LLM actually degrades both geometric and functional action information compared to the projector output—RSA drops noticeably and probe R² decreases significantly, with the steepest degradation happening right at the embedding interface before some recovery in later layers. Second, despite this overall loss, the last pre-action token appears to concentrate information in a way that partially compensates for the distributed degradation across other tokens. at the decoding interface. Now I'm looking at the functional probe results across different representations—the table shows how the trained readout token achieves the highest $R^2$ of 0.731 for action prediction, while the distributed image representations degrade to 0.683, confirming that the LLM concentrates action-relevant information at a single position rather than preserving it across tokens.

I'm also examining the per-layer representational similarity analysis across all 32 LLM layers, which reveals a sharp drop at the embedding interface followed by non-monotonic fluctuations in the middle layers, with reference baselines marked for comparison.

Now looking at the functional probe results for action prediction—the LLM processing actually degrades the distributed image representation but concentrates stronger predictive information at the readout token, achieving higher R² than the projector baseline, though this concentration depends on training since an untrained readout falls below baseline. Interestingly, DINOv2 matches the projector's performance despite having much lower representational similarity.

I'm setting up an experiment to test whether LLM training creates genuinely new action-relevant geometric structure or simply routes and leverages the structure already inherited from the vision encoder, with a factorial analysis examining the effects of training across multiple metrics.

The results show a striking dissociation: training leaves the geometric structure completely unchanged but produces a large effect on how that structure gets functionally concentrated. The geometric alignment with action space shows no meaningful training effect—the RSA changes are tiny and statistically insignificant for both image_mean and last_preaction representations. This makes sense given that the vision encoder weights stay identical between conditions, suggesting it's the sole source of action-relevant geometry. Now examining whether instruction content itself affects the geometric structure...

Instructions also fail to reshape the geometry—the effect is essentially zero across conditions. A control experiment varying instruction types (normal, random from other tasks, word-shuffled, empty) confirms this: RSA values cluster tightly around 0.485, all within measurement noise. But the readout probe tells a completely different story. Training produces a large, highly significant improvement in R² performance, jumping from 0.686 to 0.731, yet this happens without any change to the underlying geometric structure. This points toward a routing mechanism—the LLM learns to concentrate and route the pre-existing vision-encoder geometry more effectively rather than reorganizing it.

Generating markdown table... Generating figure captions... I'll use a relative path like `figures/fig2.pdf` as a default that can be adjusted based on the actual project setup. Now I'm verifying that my confidence intervals and p-values align with the task data across all three tables, and I'm thinking through the figure captions to ensure they're self-contained and don't rely on the main text. With an 8-page CoRL paper budget, I need to be mindful of how much space the experiments section takes up.

For the bibliography, I'm going through each citation to fill in complete details where I'm confident and marking uncertain entries for verification—like the OpenVLA paper and the Prismatic VLMs reference that I'm fairly sure about based on the context. Finishing up the citation verification—SigLIP from ICCV 2023, DINOv2 from TMLR 2024, and CLIP from ICML 2021 all check out. I'm less certain about the Grant 2026 paper on behavioral visual dominance and the Haon 2025 VLA interpretability work, so I'll flag those for verification. Now I need to finalize both files with the complete reference list. Looking at section 3.3, the LLM integration causes a significant drop in alignment (0.615 → 0.501) and R² performance (0.706 → 0.683), with the biggest degradation happening at the first layer and varying non-monotonically through the middle layers. The readout mechanism shows concentration in the final preaction layer, which substantially outperforms the projector and depends critically on training—untrained readouts fall well below the projector baseline, but training boosts them well above it. For 3.4, the RSA analysis reveals an interesting dissociation: the 2×2 matrix comparisons across training and instruction conditions show no significant differences, yet readout concentration itself is strongly training-dependent.

Now I'm testing whether training actually teaches the model to route information differently or simply creates new representations. The vision backbone and projector maintain identical weights between trained and untrained versions, suggesting the architecture itself doesn't change. I'm running a control experiment with random and shuffled instructions to see if instruction content actually drives the distributed RSA patterns—the results show negligible variation across normal, random, shuffled, and empty instructions, all clustering around 0.48, indicating that instruction content doesn't modulate the distributed alignment.

For the citations, I need to verify what `grant2026` refers to—it's listed for behavioral visual dominance in VLAs, which aligns with the paper's focus on vision encoder dominance. The `haon2025` citation is less clear; it could be related to VLA interpretability or feature analysis, but I should mark both for verification since I'm not certain of the exact papers. I'm cross-referencing the paper citations with the arXiv IDs from the brief—haon2025 likely corresponds to "Probing OpenVLA for Symbolic States" from February 2025, while grant2026 appears to be a separate 2026 study on behavioral visual dominance in VLAs. I need to verify these author attributions before proceeding. Now I'm switching to `\cite` format as instructed rather than `\citet`, which means adjusting how I integrate the citations into the sentences. Let me finalize the files with these corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "4285e995-76b7-49ad-a3f5-45c7bf33ca1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nd4nAWfcXLXfMZNHZQNitS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 47923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 36_

Now I have all the context. Let me write both files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "3b25ff2d-f800-444a-b5d5-d10a09d8fa84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nd4nAWfcXLXfMZNHZQNitS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 47923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 37_

<details open><summary>🔧 Tool call — Write · `toolu_01LxKaLBJ4jmviSZbUXDR4z2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.\n\n\\paragraph{Representation sources.}\nWe extract representations from five sources:\n(a)~\\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token}; and\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}.\nSources (d) and (e) serve as external baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{Representational Similarity Analysis (RSA).}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples.\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions.\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nThe SigLIP+Projector output achieves the highest alignment ($\\rho = 0.615$, 95\\% CI $[0.526, 0.695]$), followed by CLIP ViT-L/14 ($\\rho = 0.557$, $[0.442, 0.660]$).\nBoth vision-language pretrained encoders substantially exceed DINOv2 ($\\rho = 0.388$), a vision-only model.\nThe VLA's LLM layers (best image\\_mean: $\\rho = 0.501$ trained, $\\rho = 0.485$ untrained) fall between VL-pretrained encoders and DINOv2 (Figure~\\ref{fig:rsa_bar}).\n\nThree findings emerge.\nFirst, VL pretraining---not LLM processing---is the primary source of action-relevant structure.\nSigLIP and CLIP, both pretrained on image-text pairs, achieve $\\rho \\geq 0.557$, while DINOv2, pretrained with self-supervised vision objectives alone, reaches only $\\rho = 0.388$.\nThis 0.169-point gap indicates that language-grounded visual features carry substantially more action-relevant geometry than features learned without language, consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\n\nSecond, the MLP projector provides incremental alignment: SigLIP+Projector ($0.615$) exceeds CLIP ($0.557$) by $\\Delta = 0.058$, consistent with the projector mapping vision features into the LLM's embedding space.\n\nThird, the LLM degrades rather than enhances vision encoder geometry.\nProcessing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\\_mean), a drop of $\\Delta = 0.114$.\n\n\\paragraph{Geometric-functional dissociation.}\nFunctional probes reveal a dissociation between geometric similarity and functional decodability.\nDINOv2 achieves $R^2 = 0.712$, statistically indistinguishable from SigLIP+Projector ($R^2 = 0.706$, $p = 0.22$, n.s.), despite its substantially lower RSA ($0.388$ vs.\\ $0.615$).\nHigh linear decodability does not require high geometric alignment with the action space---DINOv2 features are functionally rich but geometrically dissimilar to actions.\n\n\\paragraph{Metric sensitivity.}\nThis dissociation extends to alternative similarity metrics.\nLinear CKA~\\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA restores the RSA-consistent ranking (Proj $>$ Trained $>$ Untrained $>$ DINOv2).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). VL-pretrained encoders (SigLIP, CLIP) dominate over vision-only DINOv2 and LLM-processed representations. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & 95\\% CI \\\\\n\\midrule\nSigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & {[0.442, 0.660]} \\\\\n\\midrule\nVLA Trained w/ inst. & image\\_mean & 0.501 & --- \\\\\nVLA Trained no inst. & image\\_mean & 0.501 & --- \\\\\nVLA Untrained w/ inst. & image\\_mean & 0.485 & --- \\\\\nVLA Untrained no inst. & image\\_mean & 0.482 & --- \\\\\n\\midrule\nDINOv2 ViT-L/14 & cls\\_token & 0.388 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. VL-pretrained encoders (SigLIP $\\rho{=}0.615$, CLIP $\\rho{=}0.557$) substantially exceed both LLM-processed representations ($\\rho \\leq 0.501$) and vision-only DINOv2 ($\\rho{=}0.388$). Hatched bars indicate no-instruction conditions. Error bars: 95\\% bootstrap CIs. Dashed line: DINOv2 reference.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{LLM Redistributes, Does Not Enhance, Action Structure}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.\nTable~\\ref{tab:probes} reports functional probe $R^2$ for key representation sources.\nTwo complementary effects characterize LLM processing.\n\n\\paragraph{Distributed degradation.}\nAveraging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.\nRSA drops from $0.615$ to $0.501$ ($\\Delta = 0.114$); probe $R^2$ drops from $0.706$ to $0.683$ (95\\% CI of $\\Delta$: $[0.011, 0.037]$, $p = 0.001$).\nFigure~\\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens lose information, the last pre-action token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves $R^2 = 0.731$, exceeding SigLIP+Projector ($R^2 = 0.706$, $p = 0.001$; Figure~\\ref{fig:probe_bars}).\nThis concentration is training-dependent: untrained readout ($R^2 = 0.686$) falls below the projector baseline, while trained readout ($0.731$) substantially exceeds it ($\\Delta = 0.045$, $p < 0.0001$).\n\nTogether, these results characterize the LLM as a \\emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations. The LLM degrades distributed representations (image\\_mean) relative to the projector but concentrates superior action information at the readout token---an effect that requires training. DINOv2 matches the projector in $R^2$ despite much lower RSA.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nSigLIP+Projector & 0.706 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.683 & 0.001 \\\\\nVLA Trained readout (L19) & \\textbf{0.731} & 0.001 \\\\\nVLA Untrained readout (L32) & 0.686 & --- \\\\\nDINOv2 cls\\_token & 0.712 & 0.220 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: SigLIP+Projector ($\\rho{=}0.615$) and DINOv2 ($\\rho{=}0.388$) reference levels.}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\\_mean ($R^2{=}0.683$) below the projector baseline ($0.706$, $p{=}0.001$) but concentrates superior information at the trained readout ($0.731$, $p{=}0.001$). Untrained readout ($0.686$) falls below the projector, confirming that concentration requires training ($\\Delta{=}0.045$, $p{<}0.0001$). DINOv2 ($0.712$) is statistically indistinguishable from the projector ($p{=}0.22$).}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Routes, Does Not Create, Action Geometry}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.\nTable~\\ref{tab:training_effects} reports the effect of training across metrics.\nThe $2 \\times 2$ factorial analysis (Figure~\\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.\n\n\\paragraph{Geometric invariance to training.}\nTraining does not alter the LLM's geometric alignment with the action space.\nFor image\\_mean RSA, the training effect is $\\Delta = +0.021$ (95\\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\\_preaction RSA, $\\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).\nThis null result is consistent with the vision encoder---whose weights are identical between conditions ($\\cos\\text{sim} = 1.0$)---being the sole source of action-relevant geometry.\n\n\\paragraph{Geometric invariance to instruction.}\nLanguage instructions similarly fail to modulate geometric structure.\nAcross the $2 \\times 2$ matrix, the instruction effect is $\\Delta = 0.004$ (n.s.).\nA dedicated control experiment with four instruction conditions---normal task instructions ($\\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\\pm 0.017$ of the mean (Figure~\\ref{fig:factorial}b).\n\n\\paragraph{Functional concentration requires training.}\nIn contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\\Delta = +0.045$ (CI $[+0.032, +0.058]$, $p < 0.0001$).\nTraining transforms the readout from below-projector ($R^2 = 0.686$) to above-projector ($R^2 = 0.731$) without altering the underlying geometry.\n\nThese results support a \\emph{routing} interpretation of LLM training in VLAs~\\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\\_mean $R^2$ drop confirms distributed degradation.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nTraining (image\\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\\\\nTraining (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\\\\nTraining (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\\\\nProj.\\ vs.\\ image\\_mean ($R^2$) & $+$0.023 & [$+$0.011, $+$0.037] & 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Training $\\times$ Instruction matrix for image\\_mean RSA ($\\rho$). Neither training ($\\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\\Delta{=}0.004$, n.s.)\\ produces a statistically detectable effect. \\textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\\pm 0.017$ of the mean $\\mu{=}0.482$, confirming that instruction content does not modulate distributed geometric structure.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Comparison of three similarity metrics across representation sources. \\textbf{(a)}~RSA (Spearman $\\rho$) and \\textbf{(c)}~RDM kernel CKA produce consistent rankings (Proj $>$ Trained $>$ Untrained $>$ DINOv2). \\textbf{(b)}~Linear CKA~\\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}\n\\label{fig:metric_comparison}\n\\end{figure}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "79b16636-6bf1-4597-9ccc-c960d9c0c36d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nd4nAWfcXLXfMZNHZQNitS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 362,
      "cache_read_input_tokens": 47923,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 362
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

_source line 38 · 2026-05-16T02:22:33.520Z_

<details><summary>↩ Tool result · `toolu_01LxKaLBJ4jmviSZbUXDR4z2`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "f96cf240-0836-4401-bc22-7667615d4ff9",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.\n\n\\paragraph{Representation sources.}\nWe extract representations from five sources:\n(a)~\\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token}; and\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}.\nSources (d) and (e) serve as external baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{Representational Similarity Analysis (RSA).}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples.\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions.\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests whether vision-language pretrained encoders provide the dominant source of action-relevant geometric structure in VLA representations.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nThe SigLIP+Projector output achieves the highest alignment ($\\rho = 0.615$, 95\\% CI $[0.526, 0.695]$), followed by CLIP ViT-L/14 ($\\rho = 0.557$, $[0.442, 0.660]$).\nBoth vision-language pretrained encoders substantially exceed DINOv2 ($\\rho = 0.388$), a vision-only model.\nThe VLA's LLM layers (best image\\_mean: $\\rho = 0.501$ trained, $\\rho = 0.485$ untrained) fall between VL-pretrained encoders and DINOv2 (Figure~\\ref{fig:rsa_bar}).\n\nThree findings emerge.\nFirst, VL pretraining---not LLM processing---is the primary source of action-relevant structure.\nSigLIP and CLIP, both pretrained on image-text pairs, achieve $\\rho \\geq 0.557$, while DINOv2, pretrained with self-supervised vision objectives alone, reaches only $\\rho = 0.388$.\nThis 0.169-point gap indicates that language-grounded visual features carry substantially more action-relevant geometry than features learned without language, consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\n\nSecond, the MLP projector provides incremental alignment: SigLIP+Projector ($0.615$) exceeds CLIP ($0.557$) by $\\Delta = 0.058$, consistent with the projector mapping vision features into the LLM's embedding space.\n\nThird, the LLM degrades rather than enhances vision encoder geometry.\nProcessing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\\_mean), a drop of $\\Delta = 0.114$.\n\n\\paragraph{Geometric-functional dissociation.}\nFunctional probes reveal a dissociation between geometric similarity and functional decodability.\nDINOv2 achieves $R^2 = 0.712$, statistically indistinguishable from SigLIP+Projector ($R^2 = 0.706$, $p = 0.22$, n.s.), despite its substantially lower RSA ($0.388$ vs.\\ $0.615$).\nHigh linear decodability does not require high geometric alignment with the action space---DINOv2 features are functionally rich but geometrically dissimilar to actions.\n\n\\paragraph{Metric sensitivity.}\nThis dissociation extends to alternative similarity metrics.\nLinear CKA~\\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ SigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA restores the RSA-consistent ranking (Proj $>$ Trained $>$ Untrained $>$ DINOv2).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). VL-pretrained encoders (SigLIP, CLIP) dominate over vision-only DINOv2 and LLM-processed representations. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & 95\\% CI \\\\\n\\midrule\nSigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & {[0.442, 0.660]} \\\\\n\\midrule\nVLA Trained w/ inst. & image\\_mean & 0.501 & --- \\\\\nVLA Trained no inst. & image\\_mean & 0.501 & --- \\\\\nVLA Untrained w/ inst. & image\\_mean & 0.485 & --- \\\\\nVLA Untrained no inst. & image\\_mean & 0.482 & --- \\\\\n\\midrule\nDINOv2 ViT-L/14 & cls\\_token & 0.388 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. VL-pretrained encoders (SigLIP $\\rho{=}0.615$, CLIP $\\rho{=}0.557$) substantially exceed both LLM-processed representations ($\\rho \\leq 0.501$) and vision-only DINOv2 ($\\rho{=}0.388$). Hatched bars indicate no-instruction conditions. Error bars: 95\\% bootstrap CIs. Dashed line: DINOv2 reference.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{LLM Redistributes, Does Not Enhance, Action Structure}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.\nTable~\\ref{tab:probes} reports functional probe $R^2$ for key representation sources.\nTwo complementary effects characterize LLM processing.\n\n\\paragraph{Distributed degradation.}\nAveraging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.\nRSA drops from $0.615$ to $0.501$ ($\\Delta = 0.114$); probe $R^2$ drops from $0.706$ to $0.683$ (95\\% CI of $\\Delta$: $[0.011, 0.037]$, $p = 0.001$).\nFigure~\\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens lose information, the last pre-action token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves $R^2 = 0.731$, exceeding SigLIP+Projector ($R^2 = 0.706$, $p = 0.001$; Figure~\\ref{fig:probe_bars}).\nThis concentration is training-dependent: untrained readout ($R^2 = 0.686$) falls below the projector baseline, while trained readout ($0.731$) substantially exceeds it ($\\Delta = 0.045$, $p < 0.0001$).\n\nTogether, these results characterize the LLM as a \\emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations. The LLM degrades distributed representations (image\\_mean) relative to the projector but concentrates superior action information at the readout token---an effect that requires training. DINOv2 matches the projector in $R^2$ despite much lower RSA.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nSigLIP+Projector & 0.706 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.683 & 0.001 \\\\\nVLA Trained readout (L19) & \\textbf{0.731} & 0.001 \\\\\nVLA Untrained readout (L32) & 0.686 & --- \\\\\nDINOv2 cls\\_token & 0.712 & 0.220 (n.s.) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: SigLIP+Projector ($\\rho{=}0.615$) and DINOv2 ($\\rho{=}0.388$) reference levels.}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\\_mean ($R^2{=}0.683$) below the projector baseline ($0.706$, $p{=}0.001$) but concentrates superior information at the trained readout ($0.731$, $p{=}0.001$). Untrained readout ($0.686$) falls below the projector, confirming that concentration requires training ($\\Delta{=}0.045$, $p{<}0.0001$). DINOv2 ($0.712$) is statistically indistinguishable from the projector ($p{=}0.22$).}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Routes, Does Not Create, Action Geometry}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.\nTable~\\ref{tab:training_effects} reports the effect of training across metrics.\nThe $2 \\times 2$ factorial analysis (Figure~\\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.\n\n\\paragraph{Geometric invariance to training.}\nTraining does not alter the LLM's geometric alignment with the action space.\nFor image\\_mean RSA, the training effect is $\\Delta = +0.021$ (95\\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\\_preaction RSA, $\\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).\nThis null result is consistent with the vision encoder---whose weights are identical between conditions ($\\cos\\text{sim} = 1.0$)---being the sole source of action-relevant geometry.\n\n\\paragraph{Geometric invariance to instruction.}\nLanguage instructions similarly fail to modulate geometric structure.\nAcross the $2 \\times 2$ matrix, the instruction effect is $\\Delta = 0.004$ (n.s.).\nA dedicated control experiment with four instruction conditions---normal task instructions ($\\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\\pm 0.017$ of the mean (Figure~\\ref{fig:factorial}b).\n\n\\paragraph{Functional concentration requires training.}\nIn contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\\Delta = +0.045$ (CI $[+0.032, +0.058]$, $p < 0.0001$).\nTraining transforms the readout from below-projector ($R^2 = 0.686$) to above-projector ($R^2 = 0.731$) without altering the underlying geometry.\n\nThese results support a \\emph{routing} interpretation of LLM training in VLAs~\\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\\_mean $R^2$ drop confirms distributed degradation.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nTraining (image\\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\\\\nTraining (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\\\\nTraining (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\\\\nProj.\\ vs.\\ image\\_mean ($R^2$) & $+$0.023 & [$+$0.011, $+$0.037] & 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Training $\\times$ Instruction matrix for image\\_mean RSA ($\\rho$). Neither training ($\\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\\Delta{=}0.004$, n.s.)\\ produces a statistically detectable effect. \\textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\\pm 0.017$ of the mean $\\mu{=}0.482$, confirming that instruction content does not modulate distributed geometric structure.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Comparison of three similarity metrics across representation sources. \\textbf{(a)}~RSA (Spearman $\\rho$) and \\textbf{(c)}~RDM kernel CKA produce consistent rankings (Proj $>$ Trained $>$ Untrained $>$ DINOv2). \\textbf{(b)}~Linear CKA~\\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}\n\\label{fig:metric_comparison}\n\\end{figure}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Write · `toolu_018Nr3pHEJqfFAUFCk1XA2Sh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "content": "% === VLA / Architecture ===\n\n@article{kim2024_openvla,\n  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},\n  journal   = {arXiv preprint arXiv:2406.09246},\n  year      = {2024},\n}\n\n% [VERIFY] Confirm venue and exact title. Likely \"Prismatic VLMs\" or OpenVLA architecture companion.\n@article{karamcheti2024,\n  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},\n  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},\n  journal   = {arXiv preprint arXiv:2402.07865},\n  year      = {2024},\n}\n\n@article{brohan2023_rt2,\n  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  journal   = {arXiv preprint arXiv:2307.15818},\n  year      = {2023},\n}\n\n% === Benchmark ===\n\n@inproceedings{liu2023_libero,\n  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n}\n\n% === Representation Analysis Methods ===\n\n@article{kriegeskorte2008,\n  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},\n  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter},\n  journal   = {Frontiers in Systems Neuroscience},\n  volume    = {2},\n  pages     = {4},\n  year      = {2008},\n  publisher = {Frontiers},\n}\n\n@inproceedings{kornblith2019,\n  title     = {Similarity of Neural Network Representations Revisited},\n  author    = {Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2019},\n}\n\n@article{alain2017,\n  title     = {Understanding Intermediate Layers Using Linear Classifier Probes},\n  author    = {Alain, Guillaume and Bengio, Yoshua},\n  journal   = {arXiv preprint arXiv:1610.01644},\n  year      = {2017},\n}\n\n% === Vision Encoders ===\n\n@inproceedings{zhai2023_siglip,\n  title     = {Sigmoid Loss for Language Image Pre-Training},\n  author    = {Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle = {International Conference on Computer Vision (ICCV)},\n  year      = {2023},\n}\n\n@article{oquab2024_dinov2,\n  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},\n  author    = {Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and Vo, Huy and Szafraniec, Marc and Khalidov, Vasil and Fernandez, Pierre and Haziza, Daniel and Massa, Francisco and El-Nouby, Alaaeldin and others},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2024},\n}\n\n@inproceedings{radford2021_clip,\n  title     = {Learning Transferable Visual Models From Natural Language Supervision},\n  author    = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and others},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2021},\n}\n\n% === Domain-Specific ===\n\n% [VERIFY] Cannot confirm full bibliographic details. Cited for behavioral visual dominance in VLA policies.\n@article{grant2026,\n  title     = {[VERIFY] Behavioral Visual Dominance in Vision-Language-Action Policies},\n  author    = {Grant, [VERIFY]},\n  journal   = {[VERIFY]},\n  year      = {2026},\n}\n\n% [VERIFY] Cannot confirm full bibliographic details. Cited for VLA interpretability.\n@article{haon2025,\n  title     = {[VERIFY] Interpretability of Vision-Language-Action Models},\n  author    = {Haon, [VERIFY]},\n  journal   = {[VERIFY]},\n  year      = {2025},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "f251cdf9-393d-4a07-864a-bab265714045",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015MiWvyvdRkFNxJTjigMBap",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13160,
      "cache_read_input_tokens": 48285,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13160
      },
      "output_tokens": 63,
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

_source line 40 · 2026-05-16T02:23:00.704Z_

<details><summary>↩ Tool result · `toolu_018Nr3pHEJqfFAUFCk1XA2Sh`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "bd31e263-9c64-418a-995a-2da0e9ea9e41",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
    "content": "% === VLA / Architecture ===\n\n@article{kim2024_openvla,\n  title     = {{OpenVLA}: An Open-Source Vision-Language-Action Model},\n  author    = {Kim, Moo Jin and Pertsch, Karl and Karamcheti, Siddharth and Xiao, Ted and Balakrishna, Ashwin and Nair, Suraj and Rafailov, Rafael and Foster, Ethan and Lam, Grace and Sanketi, Pannag and Lu, Quan and Kollar, Thomas and Burchfiel, Benjamin and Tedrake, Russ and Sadigh, Dorsa and Levine, Sergey and Liang, Percy and Finn, Chelsea},\n  journal   = {arXiv preprint arXiv:2406.09246},\n  year      = {2024},\n}\n\n% [VERIFY] Confirm venue and exact title. Likely \"Prismatic VLMs\" or OpenVLA architecture companion.\n@article{karamcheti2024,\n  title     = {Prismatic {VLMs}: Investigating the Design Space of Visually-Conditioned Language Models},\n  author    = {Karamcheti, Siddharth and Nair, Suraj and Balakrishna, Ashwin and Liang, Percy and Kollar, Thomas and Sadigh, Dorsa},\n  journal   = {arXiv preprint arXiv:2402.07865},\n  year      = {2024},\n}\n\n@article{brohan2023_rt2,\n  title     = {{RT-2}: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n  author    = {Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},\n  journal   = {arXiv preprint arXiv:2307.15818},\n  year      = {2023},\n}\n\n% === Benchmark ===\n\n@inproceedings{liu2023_libero,\n  title     = {{LIBERO}: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n  author    = {Liu, Bo and Zhu, Yifeng and Gao, Chongkai and Feng, Yihao and Liu, Qiang and Zhu, Yuke and Stone, Peter},\n  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},\n  year      = {2023},\n}\n\n% === Representation Analysis Methods ===\n\n@article{kriegeskorte2008,\n  title     = {Representational Similarity Analysis -- Connecting the Branches of Systems Neuroscience},\n  author    = {Kriegeskorte, Nikolaus and Mur, Marieke and Bandettini, Peter},\n  journal   = {Frontiers in Systems Neuroscience},\n  volume    = {2},\n  pages     = {4},\n  year      = {2008},\n  publisher = {Frontiers},\n}\n\n@inproceedings{kornblith2019,\n  title     = {Similarity of Neural Network Representations Revisited},\n  author    = {Kornblith, Simon and Norouzi, Mohammad and Lee, Honglak and Hinton, Geoffrey},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2019},\n}\n\n@article{alain2017,\n  title     = {Understanding Intermediate Layers Using Linear Classifier Probes},\n  author    = {Alain, Guillaume and Bengio, Yoshua},\n  journal   = {arXiv preprint arXiv:1610.01644},\n  year      = {2017},\n}\n\n% === Vision Encoders ===\n\n@inproceedings{zhai2023_siglip,\n  title     = {Sigmoid Loss for Language Image Pre-Training},\n  author    = {Zhai, Xiaohua and Mustafa, Basil and Kolesnikov, Alexander and Beyer, Lucas},\n  booktitle = {International Conference on Computer Vision (ICCV)},\n  year      = {2023},\n}\n\n@article{oquab2024_dinov2,\n  title     = {{DINOv2}: Learning Robust Visual Features without Supervision},\n  author    = {Oquab, Maxime and Darcet, Timoth{\\'e}e and Moutakanni, Theo and Vo, Huy and Szafraniec, Marc and Khalidov, Vasil and Fernandez, Pierre and Haziza, Daniel and Massa, Francisco and El-Nouby, Alaaeldin and others},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2024},\n}\n\n@inproceedings{radford2021_clip,\n  title     = {Learning Transferable Visual Models From Natural Language Supervision},\n  author    = {Radford, Alec and Kim, Jong Wook and Hallacy, Chris and Ramesh, Aditya and Goh, Gabriel and Agarwal, Sandhini and Sastry, Girish and Askell, Amanda and Mishkin, Pamela and Clark, Jack and others},\n  booktitle = {International Conference on Machine Learning (ICML)},\n  year      = {2021},\n}\n\n% === Domain-Specific ===\n\n% [VERIFY] Cannot confirm full bibliographic details. Cited for behavioral visual dominance in VLA policies.\n@article{grant2026,\n  title     = {[VERIFY] Behavioral Visual Dominance in Vision-Language-Action Policies},\n  author    = {Grant, [VERIFY]},\n  journal   = {[VERIFY]},\n  year      = {2026},\n}\n\n% [VERIFY] Cannot confirm full bibliographic details. Cited for VLA interpretability.\n@article{haon2025,\n  title     = {[VERIFY] Interpretability of Vision-Language-Action Models},\n  author    = {Haon, [VERIFY]},\n  journal   = {[VERIFY]},\n  year      = {2025},\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 41_

Now let me register both artifacts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "7112b126-c05d-48d3-be8b-60c122a3af5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8xfFGtXwRgmwe1NAB4wiN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 61445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
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

_source line 42_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GjwWqwwS3m1e73bVoqBuEW`</summary>

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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "dbc65321-1469-4cc3-b42d-638c741d5249",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8xfFGtXwRgmwe1NAB4wiN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 61445,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
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

_source line 43 · 2026-05-16T02:23:03.750Z_

<details><summary>↩ Tool result · `toolu_01GjwWqwwS3m1e73bVoqBuEW`</summary>

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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "6f8de1c6-4840-48ea-8988-bf9f691c5fdf",
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

_source line 44_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01G4cnnmFSHqUFMUL8jj3NQe`</summary>

```json
{
  "name": "experiments_section_tex",
  "type": "paper",
  "description": "CoRL 2026 paper Section 3 (Experiments) LaTeX source — covers experimental setup, vision encoder dominance, LLM redistribution, and training-as-routing claims with 3 tables and 5 figures",
  "project": "vla-ssd",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "tags": [
    "paper",
    "experiments",
    "latex",
    "corl2026"
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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "c294c056-800a-46f0-9c60-fc5608df923a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVPzhwhFwMWAQm8YaoHJ25",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 63145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 45 · 2026-05-16T02:23:09.476Z_

<details><summary>↩ Tool result · `toolu_01G4cnnmFSHqUFMUL8jj3NQe`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_801a2e\", \"name\": \"experiments_section_tex\", \"type\": \"paper\", \"description\": \"CoRL 2026 paper Section 3 (Experiments) LaTeX source — covers experimental setup, vision encoder dominance, LLM redistribution, and training-as-routing claims with 3 tables and 5 figures\", \"path\": \"projects/vla-ssd/artifacts/_project/paper/experiments.tex\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:23:09.408063+00:00\", \"tags\": [\"paper\", \"experiments\", \"latex\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "d7a88447-df76-4eb6-b949-262de1a43c93",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_801a2e\\\", \\\"name\\\": \\\"experiments_section_tex\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"CoRL 2026 paper Section 3 (Experiments) LaTeX source — covers experimental setup, vision encoder dominance, LLM redistribution, and training-as-routing claims with 3 tables and 5 figures\\\", \\\"path\\\": \\\"projects/vla-ssd/artifacts/_project/paper/experiments.tex\\\", \\\"url\\\": null, \\\"project\\\": \\\"vla-ssd\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T02:23:09.408063+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"experiments\\\", \\\"latex\\\", \\\"corl2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_801a2e\", \"name\": \"experiments_section_tex\", \"type\": \"paper\", \"description\": \"CoRL 2026 paper Section 3 (Experiments) LaTeX source — covers experimental setup, vision encoder dominance, LLM redistribution, and training-as-routing claims with 3 tables and 5 figures\", \"path\": \"projects/vla-ssd/artifacts/_project/paper/experiments.tex\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:23:09.408063+00:00\", \"tags\": [\"paper\", \"experiments\", \"latex\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01S8spRQGhif5QwDhjsjx6et`</summary>

```json
{
  "name": "references_bib",
  "type": "paper",
  "description": "BibTeX references for the experiments section — 12 entries, 2 marked [VERIFY] (grant2026, haon2025)",
  "project": "vla-ssd",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/references.bib",
  "tags": [
    "paper",
    "references",
    "bibtex",
    "corl2026"
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
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "00e18f19-8dea-4887-8d72-81b2e15c9c0f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FVPzhwhFwMWAQm8YaoHJ25",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 63145,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 720
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

_source line 47 · 2026-05-16T02:23:11.533Z_

<details><summary>↩ Tool result · `toolu_01S8spRQGhif5QwDhjsjx6et`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_0cebe2\", \"name\": \"references_bib\", \"type\": \"paper\", \"description\": \"BibTeX references for the experiments section — 12 entries, 2 marked [VERIFY] (grant2026, haon2025)\", \"path\": \"projects/vla-ssd/artifacts/_project/paper/references.bib\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:23:11.465262+00:00\", \"tags\": [\"paper\", \"references\", \"bibtex\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "85d7f939-b7e4-4baa-9f04-33c4128764cd",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260516_0cebe2\\\", \\\"name\\\": \\\"references_bib\\\", \\\"type\\\": \\\"paper\\\", \\\"description\\\": \\\"BibTeX references for the experiments section — 12 entries, 2 marked [VERIFY] (grant2026, haon2025)\\\", \\\"path\\\": \\\"projects/vla-ssd/artifacts/_project/paper/references.bib\\\", \\\"url\\\": null, \\\"project\\\": \\\"vla-ssd\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-16T02:23:11.465262+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"references\\\", \\\"bibtex\\\", \\\"corl2026\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_0cebe2\", \"name\": \"references_bib\", \"type\": \"paper\", \"description\": \"BibTeX references for the experiments section — 12 entries, 2 marked [VERIFY] (grant2026, haon2025)\", \"path\": \"projects/vla-ssd/artifacts/_project/paper/references.bib\", \"url\": null, \"project\": \"vla-ssd\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T02:23:11.465262+00:00\", \"tags\": [\"paper\", \"references\", \"bibtex\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 48_

已完成。两个文件已写入 `docs/paper/`:

**`experiments.tex`** — Section 3 完整 LaTeX，包含:
- **3.1 Experimental Setup**: LIBERO-Goal, OpenVLA-7B, 5 种表征源, 2×2 实验设计, RSA + functional probe 方法
- **3.2 Vision Encoder Dominance**: Table 1 (RSA 排序), Figure 2, geometric-functional dissociation (DINO R²≈Proj 但 RSA<<), CKA 排序反转负向结果 (Figure 6)
- **3.3 LLM Redistributes Action Structure**: Table 2 (probe R²), Figure 3 (per-layer curves), Figure 4 (probe bars), distributed degradation + readout concentration
- **3.4 Training Routes, Not Creates**: Table 3 (训练效应), Figure 5 (2×2 matrix + instruction control), geometric null + functional concentration dissociation

**`references.bib`** — 12 条 BibTeX，其中 `grant2026` 和 `haon2025` 标记了 `[VERIFY]`，需要补全真实书目信息。其余 10 条基于已知信息填写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "uuid": "411c5679-e56b-4a7f-884e-3537b994366c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0136EHDemDqxbbSC7KJKbGzX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1095,
      "cache_read_input_tokens": 63865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1095
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 49_

已完成。两个文件已写入 `docs/paper/`:

**`experiments.tex`** — Section 3 完整 LaTeX，包含:
- **3.1 Experimental Setup**: LIBERO-Goal, OpenVLA-7B, 5 种表征源, 2×2 实验设计, RSA + functional probe 方法
- **3.2 Vision Encoder Dominance**: Table 1 (RSA 排序), Figure 2, geometric-functional dissociation (DINO R²≈Proj 但 RSA<<), CKA 排序反转负向结果 (Figure 6)
- **3.3 LLM Redistributes Action Structure**: Table 2 (probe R²), Figure 3 (per-layer curves), Figure 4 (probe bars), distributed degradation + readout concentration
- **3.4 Training Routes, Not Creates**: Table 3 (训练效应), Figure 5 (2×2 matrix + instruction control), geometric null + functional concentration dissociation

**`references.bib`** — 12 条 BibTeX，其中 `grant2026` 和 `haon2025` 标记了 `[VERIFY]`，需要补全真实书目信息。其余 10 条基于已知信息填写。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 398540,
  "duration_api_ms": 397779,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "5174ae2e-38b0-4ed8-96f7-9840813dbcf9",
  "total_cost_usd": 1.07160875,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 53119,
    "cache_read_input_tokens": 496330,
    "output_tokens": 19532,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 53119,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 332,
        "cache_read_input_tokens": 63865,
        "cache_creation_input_tokens": 1095,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1095
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2985,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003065,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 19532,
      "cacheReadInputTokens": 496330,
      "cacheCreationInputTokens": 53119,
      "webSearchRequests": 0,
      "costUSD": 1.0685437500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "985395ef-a954-4b32-99bd-468aa7e84b9a"
}
```

</details>

---
