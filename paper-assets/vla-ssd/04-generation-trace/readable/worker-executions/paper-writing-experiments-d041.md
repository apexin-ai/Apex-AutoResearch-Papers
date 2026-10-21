# paper writing experiments d041

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_paper_writing_experiments_d041_20260516T043441.log`
- **Structured JSON:** [`831f52fba233f8f683c5.json`](../../sessions/83/831f52fba233f8f683c5.json)

## Before a recorded user message

18 recorded events

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
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
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
  "uuid": "ee3f33df-127d-4517-b5da-7fdac762e19a",
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
    "resetsAt": 1778922000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "e0b50696-993e-43f4-b503-3b0cc783a93e",
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to fully rewrite the experiments.tex file for their VLA-SSD paper. Let me first read the relevant files to understand the context:
1. The LaTeX paper writing skill
2. The current method.tex for style reference
3. The current experiments.tex (if it exists)

Let me start by reading these files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "7b7cf60d-7aed-4812-b853-5589b198bce7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUktARJKpbHgE43L24CzGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13858,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13858
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

### Assistant

_source line 5_

Let me read the writing skill and the existing method.tex for style reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "fb26cce2-89aa-4874-8780-bc2b6ed9e5bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUktARJKpbHgE43L24CzGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13858,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13858
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

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_014X1vA63d8i4FohrSzrXt9s`</summary>

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
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "92805a86-cdb9-45aa-bd27-34f9a1069fa8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUktARJKpbHgE43L24CzGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13858,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13858
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

_source line 7 · 2026-05-16T04:34:52.712Z_

<details><summary>↩ Tool result · `toolu_014X1vA63d8i4FohrSzrXt9s`</summary>

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
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "645be92d-8a41-4821-b8a1-29c9df71d362",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01LqYDb5tfttQktcx1DJTAJC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "6d7cdf6c-c3dd-45c4-b805-31a233fdcc73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YUktARJKpbHgE43L24CzGT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13858,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13858
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

_source line 9 · 2026-05-16T04:34:52.923Z_

<details><summary>↩ Tool result · `toolu_01LqYDb5tfttQktcx1DJTAJC`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across the components of a vision-language-action model by combining geometric analysis (RSA, CKA) with functional probes.
5	This section formalizes the model, data, representation extraction procedure, and the three complementary analysis tools.
6	
7	%------------------------------------------------------------------
8	\subsection{Model and Data}
9	\label{sec:model_data}
10	
11	\paragraph{Architecture.}
12	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy that chains three components: a DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M, frozen during training), an MLP projector that maps fused vision features into the language model's embedding space, and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions (6 DoF end-effector pose $+$ gripper opening).
13	
14	\paragraph{Model checkpoint.}
15	We use the base OpenVLA-7B checkpoint, pretrained on the Open X-Embodiment dataset.
16	No task-specific fine-tuning is applied; the ``trained'' condition refers to the standard OpenVLA weights, while the ``untrained'' condition reinitializes the LLM parameters (\S\ref{sec:setup}).
17	
18	\paragraph{Evaluation benchmark.}
19	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
20	
21	\paragraph{Untrained control.}
22	To isolate the contribution of LLM fine-tuning, we construct an untrained control by reinitializing the LLM parameters via \texttt{from\_config()}, yielding 6.74B random weights while preserving the frozen DinoSigLIP encoder and the MLP projector architecture.
23	Any difference between trained and untrained conditions is therefore attributable to LLM training, not to the vision encoder.
24	
25	%------------------------------------------------------------------
26	\subsection{Representation Extraction}
27	\label{sec:repr_extraction}
28	
29	We extract representations from six sources that span the VLA processing pipeline and two external baselines:
30	
31	\begin{enumerate}[label=(\alph*),leftmargin=*,nosep]
32	  \item \textbf{DinoSigLIP+Projector}: the output of the MLP projector applied to the fused DinoSigLIP vision features (2{,}176-D $\to$ 4{,}096-D), i.e., the representation immediately before LLM processing.
33	  \item \textbf{LLM image\_mean}: the mean activation across image token positions at each of the 32 LLM layers, capturing how distributed visual information evolves through the language backbone.
34	  \item \textbf{LLM last\_preaction}: the activation at the final token position before action decoding (the readout token) at each LLM layer, capturing how the model concentrates information for action prediction.
35	  \item \textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2}: \texttt{cls\_token} and \texttt{patch\_mean} from a vision-only self-supervised encoder, serving as a baseline without language grounding.
36	  \item \textbf{CLIP ViT-L/14}~\cite{radford2021_clip}: the mean of patch token activations (\texttt{patch\_mean}) from a vision-language contrastive model, serving as an external VL-pretrained baseline with no VLA training signal.
37	  \item \textbf{Branch-split}: to disentangle the contributions of the two encoder streams within DinoSigLIP, we extract the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) separately before fusion, as well as the fused 2{,}176-D representation before projection.
38	\end{enumerate}
39	
40	\paragraph{Experimental conditions.}
41	We cross two factors in a $2 \times 2$ factorial design: \emph{training status} (trained vs.\ untrained LLM) and \emph{instruction presence} (with vs.\ without language instruction).
42	Sources (a)--(c) are extracted under all four conditions; sources (d) and (e) are condition-independent external baselines.
43	For the instruction factor, the with-instruction condition uses the LIBERO-Goal task description; the without-instruction condition provides an empty string.
44	
45	%------------------------------------------------------------------
46	\subsection{Representational Similarity Analysis}
47	\label{sec:rsa}
48	
49	We adopt Representational Similarity Analysis (RSA)~\cite{kriegeskorte2008} to quantify geometric alignment between neural representations and the action space.
50	
51	\paragraph{RDM construction.}
52	For each task, we pair all time steps from 50 demonstrations within that task ($N$ observations per task).
53	We compute the $N \times N$ representational dissimilarity matrix (RDM) for each representation source using pairwise Euclidean distances across the full trajectory.
54	An analogous RDM is computed for the 7-dimensional action vectors using Euclidean distance.
55	
56	\paragraph{RSA statistic.}
57	We measure the alignment between a representation RDM and the action RDM via Spearman rank correlation $\rho$ over the upper-triangular entries of each matrix.
58	Higher $\rho$ indicates that observations that are nearby in representation space also tend to require similar actions.
59	
60	\paragraph{Task-level analysis.}
61	We compute RSA separately for each of the 10 LIBERO-Goal tasks using within-task observation pairs, then report the mean $\rho$ across tasks.
62	This within-task procedure ensures that RSA reflects how well representations capture the action structure \emph{within} a task, avoiding conflation with between-task variation.
63	
64	\paragraph{Statistical inference.}
65	We construct 95\% confidence intervals via bootstrap resampling (10{,}000 resamples) over the observation pairs.
66	Pairwise comparisons between representation sources use bootstrap differences with the same resampling scheme.
67	
68	%------------------------------------------------------------------
69	\subsection{Functional Action Probes}
70	\label{sec:probes}
71	
72	RSA captures geometric alignment but does not assess whether action-relevant information is decodable.
73	We complement RSA with functional probes following~\cite{alain2017}.
74	
75	\paragraph{Probe architecture.}
76	We train two-layer MLP probes (Linear $\to$ ReLU $\to$ Linear; $d_\text{in} \to 256 \to 7$) to predict the next-step 7-D action vector $a_{t+1}$ from frozen representations at time $t$.
77	All representation weights are fixed; only the probe parameters are optimized.
78	
79	\paragraph{Training protocol.}
80	Probes are trained with the Adam optimizer (learning rate $10^{-3}$, batch size 256) for up to 50 epochs with early stopping (patience $= 5$, monitoring validation loss).
81	Each task's data is split into training and validation sets.
82	
83	\paragraph{Evaluation metric.}
84	We report mean $R^2$ across the 7 action dimensions, providing a normalized measure of variance explained that is comparable across representation sources with different dimensionalities.
85	
86	\paragraph{Statistical comparison.}
87	We use bootstrap paired comparisons (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant, reporting $p$-values and 95\% confidence intervals for all pairwise contrasts.
88	
89	%------------------------------------------------------------------
90	\subsection{CKA Analysis}
91	\label{sec:cka}
92	
93	As a complementary perspective, we employ Centered Kernel Alignment (CKA)~\cite{kornblith2019} alongside RSA.
94	While RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.
95	
96	\paragraph{Two CKA variants.}
97	We compute both \emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.
98	Using both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.
99	
100	\paragraph{Dimension mismatch caveat.}
101	Linear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.
102	RDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality, providing a more reliable cross-dimensional comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "c337f975-132c-43a6-8d38-f3786bb92553",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant structure is distributed across the components of a vision-language-action model by combining geometric analysis (RSA, CKA) with functional probes.\nThis section formalizes the model, data, representation extraction procedure, and the three complementary analysis tools.\n\n%------------------------------------------------------------------\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a generalist robot policy that chains three components: a DinoSigLIP fused vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M, frozen during training), an MLP projector that maps fused vision features into the language model's embedding space, and a Llama-2 7B language backbone (6.74B parameters) that autoregressively decodes 7-dimensional actions (6 DoF end-effector pose $+$ gripper opening).\n\n\\paragraph{Model checkpoint.}\nWe use the base OpenVLA-7B checkpoint, pretrained on the Open X-Embodiment dataset.\nNo task-specific fine-tuning is applied; the ``trained'' condition refers to the standard OpenVLA weights, while the ``untrained'' condition reinitializes the LLM parameters (\\S\\ref{sec:setup}).\n\n\\paragraph{Evaluation benchmark.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\n\n\\paragraph{Untrained control.}\nTo isolate the contribution of LLM fine-tuning, we construct an untrained control by reinitializing the LLM parameters via \\texttt{from\\_config()}, yielding 6.74B random weights while preserving the frozen DinoSigLIP encoder and the MLP projector architecture.\nAny difference between trained and untrained conditions is therefore attributable to LLM training, not to the vision encoder.\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nWe extract representations from six sources that span the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),leftmargin=*,nosep]\n  \\item \\textbf{DinoSigLIP+Projector}: the output of the MLP projector applied to the fused DinoSigLIP vision features (2{,}176-D $\\to$ 4{,}096-D), i.e., the representation immediately before LLM processing.\n  \\item \\textbf{LLM image\\_mean}: the mean activation across image token positions at each of the 32 LLM layers, capturing how distributed visual information evolves through the language backbone.\n  \\item \\textbf{LLM last\\_preaction}: the activation at the final token position before action decoding (the readout token) at each LLM layer, capturing how the model concentrates information for action prediction.\n  \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2}: \\texttt{cls\\_token} and \\texttt{patch\\_mean} from a vision-only self-supervised encoder, serving as a baseline without language grounding.\n  \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip}: the mean of patch token activations (\\texttt{patch\\_mean}) from a vision-language contrastive model, serving as an external VL-pretrained baseline with no VLA training signal.\n  \\item \\textbf{Branch-split}: to disentangle the contributions of the two encoder streams within DinoSigLIP, we extract the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) separately before fusion, as well as the fused 2{,}176-D representation before projection.\n\\end{enumerate}\n\n\\paragraph{Experimental conditions.}\nWe cross two factors in a $2 \\times 2$ factorial design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nSources (a)--(c) are extracted under all four conditions; sources (d) and (e) are condition-independent external baselines.\nFor the instruction factor, the with-instruction condition uses the LIBERO-Goal task description; the without-instruction condition provides an empty string.\n\n%------------------------------------------------------------------\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify geometric alignment between neural representations and the action space.\n\n\\paragraph{RDM construction.}\nFor each task, we pair all time steps from 50 demonstrations within that task ($N$ observations per task).\nWe compute the $N \\times N$ representational dissimilarity matrix (RDM) for each representation source using pairwise Euclidean distances across the full trajectory.\nAn analogous RDM is computed for the 7-dimensional action vectors using Euclidean distance.\n\n\\paragraph{RSA statistic.}\nWe measure the alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ over the upper-triangular entries of each matrix.\nHigher $\\rho$ indicates that observations that are nearby in representation space also tend to require similar actions.\n\n\\paragraph{Task-level analysis.}\nWe compute RSA separately for each of the 10 LIBERO-Goal tasks using within-task observation pairs, then report the mean $\\rho$ across tasks.\nThis within-task procedure ensures that RSA reflects how well representations capture the action structure \\emph{within} a task, avoiding conflation with between-task variation.\n\n\\paragraph{Statistical inference.}\nWe construct 95\\% confidence intervals via bootstrap resampling (10{,}000 resamples) over the observation pairs.\nPairwise comparisons between representation sources use bootstrap differences with the same resampling scheme.\n\n%------------------------------------------------------------------\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA captures geometric alignment but does not assess whether action-relevant information is decodable.\nWe complement RSA with functional probes following~\\cite{alain2017}.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear; $d_\\text{in} \\to 256 \\to 7$) to predict the next-step 7-D action vector $a_{t+1}$ from frozen representations at time $t$.\nAll representation weights are fixed; only the probe parameters are optimized.\n\n\\paragraph{Training protocol.}\nProbes are trained with the Adam optimizer (learning rate $10^{-3}$, batch size 256) for up to 50 epochs with early stopping (patience $= 5$, monitoring validation loss).\nEach task's data is split into training and validation sets.\n\n\\paragraph{Evaluation metric.}\nWe report mean $R^2$ across the 7 action dimensions, providing a normalized measure of variance explained that is comparable across representation sources with different dimensionalities.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparisons (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant, reporting $p$-values and 95\\% confidence intervals for all pairwise contrasts.\n\n%------------------------------------------------------------------\n\\subsection{CKA Analysis}\n\\label{sec:cka}\n\nAs a complementary perspective, we employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} alongside RSA.\nWhile RSA captures local geometric alignment via rank-order preservation, CKA measures global representational similarity through kernel-based comparisons.\n\n\\paragraph{Two CKA variants.}\nWe compute both \\emph{linear CKA}, which uses a linear kernel and is sensitive to second-order statistics, and \\emph{RDM kernel CKA}, which operates on the same distance matrices as RSA but aggregates them differently.\nUsing both variants tests whether conclusions about representation structure are robust to the choice of similarity metric.\n\n\\paragraph{Dimension mismatch caveat.}\nLinear CKA between high-dimensional representations (4{,}096-D for LLM layers) and the 7-D action space is subject to a known dimension mismatch: the linear kernel in the low-dimensional space may not capture the same structure as in the high-dimensional space.\nRDM kernel CKA avoids this issue by operating on distance matrices of equal size regardless of the original feature dimensionality, providing a more reliable cross-dimensional comparison.",
      "numLines": 102,
      "startLine": 1,
      "totalLines": 102
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

Now let me check if there's an existing experiments.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "3f4c9c23-d699-4c1b-bc7a-c6f8de085c8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeggdY61F52dSLKQv9tzo8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8088,
      "cache_read_input_tokens": 25699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8088
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_01Hx732ciCeqXipiunKPwwd5`</summary>

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
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "95d44d79-8454-4404-8d26-3efd55d516e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AeggdY61F52dSLKQv9tzo8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8088,
      "cache_read_input_tokens": 25699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8088
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

_source line 12 · 2026-05-16T04:34:57.993Z_

<details><summary>↩ Tool result · `toolu_01Hx732ciCeqXipiunKPwwd5`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Benchmark and model.}
8	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
9	We use OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.
10	
11	\paragraph{Representation sources.}
12	We extract representations from five sources:
13	(a)~\textbf{DinoSigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;
14	(b)~\textbf{LLM image\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;
15	(c)~\textbf{LLM last\_preaction}---the final token position before action decoding (readout token) at each LLM layer;
16	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token}; and
17	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean}.
18	Sources (d) and (e) serve as external baselines with no VLA training signal.
19	
20	\paragraph{Experimental conditions.}
21	We use a $2 \times 2$ factorial design crossing \emph{training status} (trained vs.\ untrained) with \emph{instruction presence} (with vs.\ without language instruction).
22	The untrained control applies \texttt{from\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.
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
35	This experiment tests which pretrained vision encoders provide the strongest source of action-relevant geometric structure in VLA representations.
36	
37	Table~\ref{tab:rsa_overview} reports RSA $\rho$ between each representation source and the action space.
38	Standalone DINOv2 achieves the highest alignment ($\rho = 0.631$), followed by DinoSigLIP+Projector ($\rho = 0.615$, 95\% CI $[0.526, 0.695]$) and CLIP ViT-L/14 ($\rho = 0.557$, $[0.442, 0.660]$).
39	All pretrained encoders substantially exceed the VLA's LLM layers (best image\_mean: $\rho = 0.501$; Figure~\ref{fig:rsa_bar}).
40	
41	Three findings emerge.
42	First, self-supervised pretraining provides action-relevant geometric structure at least as strong as vision-language pretraining.
43	DINOv2, pretrained with self-supervised objectives alone, achieves $\rho = 0.631$---the highest RSA of any representation source, numerically exceeding the DinoSigLIP+Projector ($\rho = 0.615$), which combines DINOv2 with SigLIP features.
44	Vision-language contrastive pretraining (CLIP, $\rho = 0.557$) yields the weakest geometry among pretrained encoders, consistent with behavioral evidence of visual dominance in VLA policies~\cite{grant2026}.
45	
46	Second, fusing with SigLIP and projecting into LLM space does not improve geometric alignment over standalone DINOv2: DinoSigLIP+Projector ($0.615$) is numerically below standalone DINOv2 ($0.631$), indicating that the projector maps features into LLM space without enhancing the self-supervised geometry already present.
47	
48	Third, the LLM degrades rather than enhances vision encoder geometry.
49	Processing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\_mean), a drop of $\Delta = 0.114$.
50	
51	\paragraph{Convergent rankings across metrics.}
52	Functional probes corroborate the RSA ordering.
53	Under unified probe hyperparameters, DINOv2 achieves $R^2 = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$, $p = 0.557$, n.s.), while CLIP achieves the lowest $R^2$ ($0.587$, $p < 0.001$ vs.\ DINOv2).
54	Both RSA and probe $R^2$ rank DINOv2 $\geq$ DinoSigLIP+Projector $>$ CLIP, indicating that self-supervised features provide at least as much action-relevant structure as VL-pretrained features on both geometric and functional dimensions.
55	
56	\paragraph{Metric sensitivity.}
57	However, the choice of similarity metric matters.
58	Linear CKA~\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\ref{fig:metric_comparison}).
59	RDM kernel CKA yields a near-identical ordering (Trained $\approx$ Proj $>$ Untrained $>$ DINOv2), with the Trained--Projector gap negligible ($\Delta = 0.003$).
60	This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.
61	
62	\begin{table}[t]
63	\centering
64	\caption{RSA between representation and action RDMs ($\rho$ $\uparrow$). Self-supervised DINOv2 achieves the highest geometric alignment, followed by the DinoSigLIP+Projector and VL-pretrained CLIP. All pretrained encoders exceed LLM-processed representations. 95\% CIs from 10{,}000 bootstrap resamples.}
65	\label{tab:rsa_overview}
66	\small
67	\begin{tabular}{llcc}
68	\toprule
69	Source & Aggregation & RSA $\rho$ & 95\% CI \\
70	\midrule
71	DINOv2 ViT-L/14 & patch\_mean & 0.631 & --- \\
72	DinoSigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\
73	CLIP ViT-L/14 & patch\_mean & 0.557 & {[0.442, 0.660]} \\
74	\midrule
75	VLA Trained w/ inst. & image\_mean & 0.501 & --- \\
76	VLA Trained no inst. & image\_mean & 0.501 & --- \\
77	VLA Untrained w/ inst. & image\_mean & 0.485 & --- \\
78	VLA Untrained no inst. & image\_mean & 0.482 & --- \\
79	\bottomrule
80	\end{tabular}
81	\end{table}
82	
83	\begin{figure}[t]
84	\centering
85	\includegraphics[width=\columnwidth]{figures/fig2.pdf}
86	\caption{RSA with the action space ($\rho$) across representation sources. Self-supervised DINOv2 ($\rho{=}0.631$) achieves the highest geometric alignment, followed by DinoSigLIP+Projector ($\rho{=}0.615$) and CLIP ($\rho{=}0.557$). All pretrained encoders exceed LLM-processed representations ($\rho \leq 0.501$). Hatched bars indicate no-instruction conditions. Error bars: 95\% bootstrap CIs.}
87	\label{fig:rsa_bar}
88	\end{figure}
89	
90	%------------------------------------------------------------------
91	\subsection{LLM Redistributes, Does Not Enhance, Action Structure}
92	\label{sec:llm_redistribution}
93	
94	This experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.
95	Table~\ref{tab:probes} reports functional probe $R^2$ for key representation sources.
96	Two complementary effects characterize LLM processing.
97	
98	\paragraph{Distributed degradation.}
99	Averaging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.
100	RSA drops from $0.615$ to $0.501$ ($\Delta = 0.114$); probe $R^2$ drops from $0.630$ to $0.599$ ($\Delta = 0.031$, $p < 0.001$).
101	Figure~\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.
102	
103	\paragraph{Readout concentration.}
104	While distributed image tokens lose information, the last pre-action token (\texttt{last\_preaction}) concentrates action-relevant information beyond the projector baseline.
105	Trained readout achieves $R^2 = 0.671$, exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $\Delta = 0.041$; Figure~\ref{fig:probe_bars}).
106	This concentration is training-dependent: under internally consistent probes, trained readout substantially exceeds untrained readout ($\Delta R^2 = 0.045$, $p < 0.0001$; \S\ref{sec:training_routing}).
107	
108	Together, these results characterize the LLM as a \emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\cite{haon2025}.
109	
110	\begin{table}[t]
111	\centering
112	\caption{Functional probe $R^2$ ($\uparrow$) for action prediction from frozen representations (unified D036 hyperparameters). The LLM degrades distributed representations (image\_mean) relative to the projector but concentrates superior action information at the readout token. RSA and $R^2$ rankings run in opposite directions: CLIP shows the strongest geometric alignment among external encoders but the lowest $R^2$. $^\dagger$Untrained readout uses p0 probes with internally consistent hyperparameters.}
113	\label{tab:probes}
114	\small
115	\begin{tabular}{lcc}
116	\toprule
117	Representation & $R^2$ & $p$ vs.\ Proj. \\
118	\midrule
119	DinoSigLIP+Projector & 0.630 & --- \\
120	VLA Trained image\_mean (L19) & 0.599 & $<$0.001 \\
121	VLA Trained readout (L19) & \textbf{0.671} & $<$0.001 \\
122	VLA Untrained readout (L32) & 0.686$^\dagger$ & --- \\
123	\midrule
124	DINOv2 cls\_token & 0.634 & 0.557 (n.s.) \\
125	CLIP ViT-L/14 cls & 0.587 & $<$0.001 \\
126	\bottomrule
127	\end{tabular}
128	\end{table}
129	
130	\begin{figure}[t]
131	\centering
132	\includegraphics[width=\columnwidth]{figures/fig3.pdf}
133	\caption{Per-layer RSA ($\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: DINOv2 ($\rho{=}0.631$) and DinoSigLIP+Projector ($\rho{=}0.615$) reference levels.}
134	\label{fig:layer_curves}
135	\end{figure}
136	
137	\begin{figure}[t]
138	\centering
139	\includegraphics[width=\columnwidth]{figures/fig4.pdf}
140	\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\_mean ($R^2{=}0.599$) below the projector baseline ($0.630$) but concentrates superior information at the trained readout ($0.671$). DINOv2 ($0.634$) is statistically indistinguishable from the projector ($p{=}0.557$). Rankings are consistent with RSA: DINOv2 $\geq$ Projector $>$ CLIP ($0.587$), reinforcing the convergent ordering across geometric and functional metrics.}
141	\label{fig:probe_bars}
142	\end{figure}
143	
144	%------------------------------------------------------------------
145	\subsection{Training Routes, Does Not Create, Action Geometry}
146	\label{sec:training_routing}
147	
148	This experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.
149	Table~\ref{tab:training_effects} reports the effect of training across metrics.
150	The $2 \times 2$ factorial analysis (Figure~\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.
151	
152	\paragraph{Geometric invariance to training.}
153	Training does not alter the LLM's geometric alignment with the action space.
154	For image\_mean RSA, the training effect is $\Delta = +0.021$ (95\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\_preaction RSA, $\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).
155	This null result is consistent with the vision encoder---whose weights are identical between conditions ($\cos\text{sim} = 1.0$)---being the sole source of action-relevant geometry.
156	
157	\paragraph{Geometric invariance to instruction.}
158	Language instructions similarly fail to modulate geometric structure.
159	Across the $2 \times 2$ matrix, the instruction effect is $\Delta = 0.004$ (n.s.).
160	A dedicated control experiment with four instruction conditions---normal task instructions ($\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\pm 0.017$ of the normal-instruction condition ($\rho = 0.489$; Figure~\ref{fig:factorial}b).
161	
162	\paragraph{Functional concentration requires training.}
163	In contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\Delta = +0.045$ ($p < 0.0001$).\footnote{The training effect comparison uses internally consistent p0 probes (trained readout $R^2 = 0.731$, untrained $0.686$) to ensure valid within-condition comparison; absolute values differ from the cross-representation comparison in Table~\ref{tab:probes}, which uses unified hyperparameters.}
164	Training concentrates action-relevant information at the readout without altering the underlying geometry.
165	
166	These results support a \emph{routing} interpretation of LLM training in VLAs~\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.
167	
168	\begin{table}[t]
169	\centering
170	\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\_mean $R^2$ drop confirms distributed degradation.}
171	\label{tab:training_effects}
172	\small
173	\begin{tabular}{lccc}
174	\toprule
175	Comparison & $\Delta$ & 95\% CI & $p$ \\
176	\midrule
177	Training (image\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\
178	Training (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\
179	Training (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\
180	Proj.\ vs.\ image\_mean ($R^2$) & $+$0.031 & --- & $<$0.001 \\
181	\bottomrule
182	\end{tabular}
183	\end{table}
184	
185	\begin{figure}[t]
186	\centering
187	\includegraphics[width=\columnwidth]{figures/fig5.pdf}
188	\caption{\textbf{(a)}~Training $\times$ Instruction matrix for image\_mean RSA ($\rho$). Neither training ($\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\Delta{=}0.004$, n.s.)\ produces a statistically detectable effect. \textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\pm 0.017$ of the normal-instruction condition ($\rho{=}0.489$), confirming that instruction content does not modulate distributed geometric structure.}
189	\label{fig:factorial}
190	\end{figure}
191	
192	\begin{figure}[t]
193	\centering
194	\includegraphics[width=\columnwidth]{figures/fig6.pdf}
195	\caption{Comparison of three similarity metrics across representation sources. \textbf{(a)}~RSA (Spearman $\rho$) ranks Proj $>$ Trained; \textbf{(c)}~RDM kernel CKA yields Trained $\approx$ Proj ($\Delta{=}0.003$) $>$ Untrained $>$ DINOv2. \textbf{(b)}~Linear CKA~\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}
196	\label{fig:metric_comparison}
197	\end{figure}
198	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "13cd7faf-733e-474f-8658-ea1bf03dabd3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.\n\n\\paragraph{Representation sources.}\nWe extract representations from five sources:\n(a)~\\textbf{DinoSigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token}; and\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}.\nSources (d) and (e) serve as external baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{Representational Similarity Analysis (RSA).}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples.\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions.\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests which pretrained vision encoders provide the strongest source of action-relevant geometric structure in VLA representations.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nStandalone DINOv2 achieves the highest alignment ($\\rho = 0.631$), followed by DinoSigLIP+Projector ($\\rho = 0.615$, 95\\% CI $[0.526, 0.695]$) and CLIP ViT-L/14 ($\\rho = 0.557$, $[0.442, 0.660]$).\nAll pretrained encoders substantially exceed the VLA's LLM layers (best image\\_mean: $\\rho = 0.501$; Figure~\\ref{fig:rsa_bar}).\n\nThree findings emerge.\nFirst, self-supervised pretraining provides action-relevant geometric structure at least as strong as vision-language pretraining.\nDINOv2, pretrained with self-supervised objectives alone, achieves $\\rho = 0.631$---the highest RSA of any representation source, numerically exceeding the DinoSigLIP+Projector ($\\rho = 0.615$), which combines DINOv2 with SigLIP features.\nVision-language contrastive pretraining (CLIP, $\\rho = 0.557$) yields the weakest geometry among pretrained encoders, consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\n\nSecond, fusing with SigLIP and projecting into LLM space does not improve geometric alignment over standalone DINOv2: DinoSigLIP+Projector ($0.615$) is numerically below standalone DINOv2 ($0.631$), indicating that the projector maps features into LLM space without enhancing the self-supervised geometry already present.\n\nThird, the LLM degrades rather than enhances vision encoder geometry.\nProcessing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\\_mean), a drop of $\\Delta = 0.114$.\n\n\\paragraph{Convergent rankings across metrics.}\nFunctional probes corroborate the RSA ordering.\nUnder unified probe hyperparameters, DINOv2 achieves $R^2 = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$, $p = 0.557$, n.s.), while CLIP achieves the lowest $R^2$ ($0.587$, $p < 0.001$ vs.\\ DINOv2).\nBoth RSA and probe $R^2$ rank DINOv2 $\\geq$ DinoSigLIP+Projector $>$ CLIP, indicating that self-supervised features provide at least as much action-relevant structure as VL-pretrained features on both geometric and functional dimensions.\n\n\\paragraph{Metric sensitivity.}\nHowever, the choice of similarity metric matters.\nLinear CKA~\\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA yields a near-identical ordering (Trained $\\approx$ Proj $>$ Untrained $>$ DINOv2), with the Trained--Projector gap negligible ($\\Delta = 0.003$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). Self-supervised DINOv2 achieves the highest geometric alignment, followed by the DinoSigLIP+Projector and VL-pretrained CLIP. All pretrained encoders exceed LLM-processed representations. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & 95\\% CI \\\\\n\\midrule\nDINOv2 ViT-L/14 & patch\\_mean & 0.631 & --- \\\\\nDinoSigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & {[0.442, 0.660]} \\\\\n\\midrule\nVLA Trained w/ inst. & image\\_mean & 0.501 & --- \\\\\nVLA Trained no inst. & image\\_mean & 0.501 & --- \\\\\nVLA Untrained w/ inst. & image\\_mean & 0.485 & --- \\\\\nVLA Untrained no inst. & image\\_mean & 0.482 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 ($\\rho{=}0.631$) achieves the highest geometric alignment, followed by DinoSigLIP+Projector ($\\rho{=}0.615$) and CLIP ($\\rho{=}0.557$). All pretrained encoders exceed LLM-processed representations ($\\rho \\leq 0.501$). Hatched bars indicate no-instruction conditions. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{LLM Redistributes, Does Not Enhance, Action Structure}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.\nTable~\\ref{tab:probes} reports functional probe $R^2$ for key representation sources.\nTwo complementary effects characterize LLM processing.\n\n\\paragraph{Distributed degradation.}\nAveraging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.\nRSA drops from $0.615$ to $0.501$ ($\\Delta = 0.114$); probe $R^2$ drops from $0.630$ to $0.599$ ($\\Delta = 0.031$, $p < 0.001$).\nFigure~\\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens lose information, the last pre-action token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves $R^2 = 0.671$, exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $\\Delta = 0.041$; Figure~\\ref{fig:probe_bars}).\nThis concentration is training-dependent: under internally consistent probes, trained readout substantially exceeds untrained readout ($\\Delta R^2 = 0.045$, $p < 0.0001$; \\S\\ref{sec:training_routing}).\n\nTogether, these results characterize the LLM as a \\emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations (unified D036 hyperparameters). The LLM degrades distributed representations (image\\_mean) relative to the projector but concentrates superior action information at the readout token. RSA and $R^2$ rankings run in opposite directions: CLIP shows the strongest geometric alignment among external encoders but the lowest $R^2$. $^\\dagger$Untrained readout uses p0 probes with internally consistent hyperparameters.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nDinoSigLIP+Projector & 0.630 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.599 & $<$0.001 \\\\\nVLA Trained readout (L19) & \\textbf{0.671} & $<$0.001 \\\\\nVLA Untrained readout (L32) & 0.686$^\\dagger$ & --- \\\\\n\\midrule\nDINOv2 cls\\_token & 0.634 & 0.557 (n.s.) \\\\\nCLIP ViT-L/14 cls & 0.587 & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: DINOv2 ($\\rho{=}0.631$) and DinoSigLIP+Projector ($\\rho{=}0.615$) reference levels.}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\\_mean ($R^2{=}0.599$) below the projector baseline ($0.630$) but concentrates superior information at the trained readout ($0.671$). DINOv2 ($0.634$) is statistically indistinguishable from the projector ($p{=}0.557$). Rankings are consistent with RSA: DINOv2 $\\geq$ Projector $>$ CLIP ($0.587$), reinforcing the convergent ordering across geometric and functional metrics.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Routes, Does Not Create, Action Geometry}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.\nTable~\\ref{tab:training_effects} reports the effect of training across metrics.\nThe $2 \\times 2$ factorial analysis (Figure~\\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.\n\n\\paragraph{Geometric invariance to training.}\nTraining does not alter the LLM's geometric alignment with the action space.\nFor image\\_mean RSA, the training effect is $\\Delta = +0.021$ (95\\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\\_preaction RSA, $\\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).\nThis null result is consistent with the vision encoder---whose weights are identical between conditions ($\\cos\\text{sim} = 1.0$)---being the sole source of action-relevant geometry.\n\n\\paragraph{Geometric invariance to instruction.}\nLanguage instructions similarly fail to modulate geometric structure.\nAcross the $2 \\times 2$ matrix, the instruction effect is $\\Delta = 0.004$ (n.s.).\nA dedicated control experiment with four instruction conditions---normal task instructions ($\\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\\pm 0.017$ of the normal-instruction condition ($\\rho = 0.489$; Figure~\\ref{fig:factorial}b).\n\n\\paragraph{Functional concentration requires training.}\nIn contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\\Delta = +0.045$ ($p < 0.0001$).\\footnote{The training effect comparison uses internally consistent p0 probes (trained readout $R^2 = 0.731$, untrained $0.686$) to ensure valid within-condition comparison; absolute values differ from the cross-representation comparison in Table~\\ref{tab:probes}, which uses unified hyperparameters.}\nTraining concentrates action-relevant information at the readout without altering the underlying geometry.\n\nThese results support a \\emph{routing} interpretation of LLM training in VLAs~\\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\\_mean $R^2$ drop confirms distributed degradation.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nTraining (image\\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\\\\nTraining (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\\\\nTraining (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\\\\nProj.\\ vs.\\ image\\_mean ($R^2$) & $+$0.031 & --- & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Training $\\times$ Instruction matrix for image\\_mean RSA ($\\rho$). Neither training ($\\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\\Delta{=}0.004$, n.s.)\\ produces a statistically detectable effect. \\textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\\pm 0.017$ of the normal-instruction condition ($\\rho{=}0.489$), confirming that instruction content does not modulate distributed geometric structure.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Comparison of three similarity metrics across representation sources. \\textbf{(a)}~RSA (Spearman $\\rho$) ranks Proj $>$ Trained; \\textbf{(c)}~RDM kernel CKA yields Trained $\\approx$ Proj ($\\Delta{=}0.003$) $>$ Untrained $>$ DINOv2. \\textbf{(b)}~Linear CKA~\\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}\n\\label{fig:metric_comparison}\n\\end{figure}\n",
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

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the full experiments.tex based on the new data (Method B RSA numbers) and the specified structure. Let me carefully construct this following the user's detailed instructions.

Key changes from old to new:
1. RSA numbers are all different (Method B recalculation)
2. DINO cls_token = 0.692 (was patch_mean 0.631)
3. Branch-split experiment is NEW
4. §4.3 narrative changes from "LLM Redistributes, Does Not Enhance" to "Non-Monotonic LLM Transformation" — the LLM DOES enhance in early layers


5. Training section reframed as "redistributes, doesn't create"
6. New per-layer curves showing inverted-U pattern

Now I'm writing out the full LaTeX document with all sections, tables, and figures integrated according to the new structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "464be0cb-4c73-4cf9-b87b-9416c3645b88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdjjcEuCF8qN7ptNCNzrCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5475,
      "cache_read_input_tokens": 33787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5475
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

_source line 14_

Now I have all the context. Writing the full experiments.tex with the updated Method B numbers and new narrative structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "86f10e26-8492-4601-8390-a9ee71969a9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdjjcEuCF8qN7ptNCNzrCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5475,
      "cache_read_input_tokens": 33787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5475
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

_source line 15_

<details open><summary>🔧 Tool call — Write · `toolu_013gRxhfz4cvA6KW1HSZcJfS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.\n\n\\paragraph{Representation sources.}\nWe extract representations from six sources:\n(a)~\\textbf{DinoSigLIP+Projector}---the fused vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} and \\texttt{patch\\_mean};\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}; and\n(f)~\\textbf{Branch-split}---the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) extracted separately before fusion, plus the fused 2{,}176-D representation before projection.\nSources (d)--(f) serve as external or ablation baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder and the projector architecture, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{RSA.}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) using Euclidean distance for each representation source and for the 7-dimensional action space, with within-task pairing across 50 demonstrations per task.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples (\\S\\ref{sec:rsa}).\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions (\\S\\ref{sec:probes}).\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests which pretrained vision encoders provide the strongest action-relevant geometric structure.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nThe standalone DINOv2 \\texttt{cls\\_token} achieves the highest alignment of any representation source ($\\rho = 0.692$), followed by the fused DinoSigLIP 2{,}176-D representation before projection ($\\rho = 0.634$) and the DINOv2 \\texttt{patch\\_mean} ($\\rho = 0.631$).\nCLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment among pretrained encoders ($\\rho = 0.557$; Figure~\\ref{fig:rsa_bar}).\n\n\\paragraph{Self-supervised pretraining dominates.}\nDINOv2, pretrained with self-supervised objectives alone, achieves $\\rho = 0.692$---exceeding not only CLIP ($\\rho = 0.557$) but also the VLA's own internal representations at their peaks (trained image\\_mean: $0.628$; trained readout: $0.643$).\nThis ordering---self-supervised $>$ VL-pretrained---is consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\nFunctional probes corroborate the ranking: DINOv2 \\texttt{cls\\_token} achieves $R^2 = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$, $p = 0.557$, n.s.), while CLIP yields the lowest probe $R^2$ ($0.587$, $p < 0.001$ vs.\\ DINOv2).\n\n\\paragraph{Branch-split analysis.}\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone, indicating that concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\nThe projector thus maps features into LLM-compatible dimensionality at the cost of modest geometric degradation.\n\n\\paragraph{Metric sensitivity.}\nThe choice of similarity metric matters.\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties~\\cite{kornblith2019} and underscores the importance of multi-metric evaluation.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). Self-supervised DINOv2 \\texttt{cls\\_token} achieves the highest geometric alignment ($0.692$). Fusion of both branches ($0.634$) exceeds either branch alone; the projector introduces modest compression loss ($0.634 \\to 0.615$). VLA peaks refer to the best layer for each token type. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & Notes \\\\\n\\midrule\nDINOv2 ViT-L/14 & cls\\_token & 0.692 & Standalone, highest \\\\\nFused DinoSigLIP & 2{,}176-D & 0.634 & Before projection \\\\\nDINOv2 ViT-L/14 & patch\\_mean & 0.631 & Standalone \\\\\nVLA Trained & image\\_mean (L12) & 0.628 & Peak layer \\\\\nVLA Untrained & last\\_preaction (L1) & 0.626 & Peak layer \\\\\nSigLIP branch & 1{,}088-D & 0.621 & Branch-split \\\\\nDINOv2 branch & 1{,}088-D & 0.619 & Branch-split \\\\\nDinoSigLIP+Projector & --- & 0.615 & After MLP \\\\\nVLA Untrained & image\\_mean (L0) & 0.612 & Peak layer \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & VL-pretrained \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment, followed by fused DinoSigLIP ($0.634$) and the VLA trained image\\_mean peak ($0.628$). CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic LLM Transformation}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder across its 32 layers.\n\n\\paragraph{Inverted-U pattern.}\nFigure~\\ref{fig:layer_curves} reveals a non-monotonic trajectory for trained image\\_mean RSA: $\\rho$ begins at $0.612$ (L0, equal to the projector input), rises to a peak of $0.628$ at L12---\\emph{above} the DinoSigLIP+Projector baseline ($0.615$)---then declines monotonically to $0.422$ at L32.\nThe first 12 layers thus \\emph{enhance} geometric alignment with the action space beyond the vision encoder input, while the remaining 20 layers progressively degrade it below the initial level.\nThis non-monotonic profile contrasts sharply with the untrained control, which peaks at L0 ($\\rho = 0.612$) and decays monotonically to $0.545$ at L32.\n\n\\paragraph{Peak above projector.}\nThe trained image\\_mean peak at L12 ($\\rho = 0.628$) exceeds the DinoSigLIP+Projector ($0.615$) by $\\Delta = 0.013$.\nThe LLM's middle layers contain representations more geometrically aligned with actions than the raw vision encoder output---refining, not merely preserving, the inherited structure.\n\n\\paragraph{RSA--CKA dissociation.}\nLinear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens follow the inverted-U trajectory, the readout token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves peak RSA $\\rho = 0.643$ at L12 and probe $R^2 = 0.671$ (L19), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $\\Delta = 0.041$; Table~\\ref{tab:probes}, Figure~\\ref{fig:probe_bars}).\n\n\\paragraph{Late-layer degradation.}\nThe decline from L12 to L32 ($\\rho$: $0.628 \\to 0.422$, $\\Delta = -0.206$) represents distributed degradation as the LLM repurposes image token representations for language modeling objectives.\nThis degradation exceeds the untrained decay ($0.612 \\to 0.545$, $\\Delta = -0.067$), suggesting that training actively redirects later layers away from action geometry preservation.\n\nTogether, these results characterize LLM processing as a three-phase transformation: early-layer geometric refinement, mid-layer peak, and late-layer degradation with concurrent concentration at the readout position~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations. The trained readout concentrates action information ($0.671$) beyond the projector ($0.630$), while distributed image\\_mean loses information ($0.599$). $^\\dagger$Untrained readout uses internally consistent probe hyperparameters.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nVLA Trained readout (L19) & \\textbf{0.671} & $<$0.001 \\\\\nDINOv2 cls\\_token & 0.634 & 0.557 (n.s.) \\\\\nDinoSigLIP+Projector & 0.630 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.599 & $<$0.001 \\\\\nCLIP ViT-L/14 cls & 0.587 & $<$0.001 \\\\\n\\midrule\nVLA Untrained readout (L32) & 0.686$^\\dagger$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers. Trained image\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\to$ L12 $= 0.628$ (peak, above Projector $0.615$) $\\to$ L32 $= 0.422$. Untrained image\\_mean (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2 cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The trained readout ($R^2{=}0.671$) exceeds the projector baseline ($0.630$) and all external encoders, while trained image\\_mean ($0.599$) falls below the projector. DINOv2 cls ($0.634$) is statistically indistinguishable from the projector ($p{=}0.557$).}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Redistributes, Does Not Create}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant structure or redistributes pre-existing geometry inherited from the vision encoder.\nFigure~\\ref{fig:factorial} shows the $2 \\times 2$ factorial analysis; Table~\\ref{tab:training_effects} reports bootstrap comparisons.\n\n\\paragraph{Peak shift without peak gain.}\nTraining moves the image\\_mean RSA peak from L0 to L12.\nThe trained model peaks at L12 ($\\rho = 0.628$); the untrained model peaks at L0 ($\\rho = 0.612$).\nComparing best-versus-best: $\\Delta = +0.017$, 95\\% CI includes zero, not statistically significant.\nTraining does not create geometric structure that exceeds what the vision encoder already provides---it relocates the peak deeper into the network.\n\n\\paragraph{Same-layer effect.}\nAt the same layer (L12), training produces a large effect: $\\Delta = +0.079$, $p < 0.0001$.\nThe trained model at L12 ($0.628$) far exceeds the untrained model at L12 ($0.549$).\nTraining thus has a dramatic effect on \\emph{where} action geometry peaks, but a negligible effect on \\emph{how high} it peaks.\n\n\\paragraph{Interpretation.}\nThese two results together support a routing interpretation: training teaches the LLM \\emph{where to concentrate} action-relevant structure (moving the peak from L0 to L12), not \\emph{what structure to create} (the peak value does not increase beyond the untrained best).\nThe vision encoder provides the ceiling; training determines the depth profile.\n\n\\paragraph{Instruction invariance.}\nLanguage instructions do not modulate geometric structure.\nAcross all conditions, instruction presence produces a maximum $|\\Delta| = 0.006$ in RSA, well within noise.\nThis confirms that the action geometry is visually grounded and instruction-independent~\\cite{grant2026}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training effects on action-relevant structure (bootstrap, 10{,}000 resamples). Best-vs-best comparison shows training does not create new geometry ($\\Delta{=}+0.017$, n.s.), while the same-layer comparison reveals training's large routing effect ($\\Delta{=}+0.079$, $p{<}0.0001$).}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$) without increasing the peak value beyond the untrained maximum (best-vs-best $\\Delta{=}+0.017$, n.s.). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$, confirming visually grounded action geometry.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "d609e6d6-38b0-4952-9e4e-4f1e1b5690ab",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdjjcEuCF8qN7ptNCNzrCR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5475,
      "cache_read_input_tokens": 33787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5475
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

_source line 16 · 2026-05-16T04:36:39.325Z_

<details><summary>↩ Tool result · `toolu_013gRxhfz4cvA6KW1HSZcJfS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "53a05b8d-09f3-4899-80e6-bef6b396c471",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.\n\n\\paragraph{Representation sources.}\nWe extract representations from six sources:\n(a)~\\textbf{DinoSigLIP+Projector}---the fused vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} and \\texttt{patch\\_mean};\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}; and\n(f)~\\textbf{Branch-split}---the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) extracted separately before fusion, plus the fused 2{,}176-D representation before projection.\nSources (d)--(f) serve as external or ablation baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder and the projector architecture, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{RSA.}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) using Euclidean distance for each representation source and for the 7-dimensional action space, with within-task pairing across 50 demonstrations per task.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples (\\S\\ref{sec:rsa}).\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions (\\S\\ref{sec:probes}).\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests which pretrained vision encoders provide the strongest action-relevant geometric structure.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nThe standalone DINOv2 \\texttt{cls\\_token} achieves the highest alignment of any representation source ($\\rho = 0.692$), followed by the fused DinoSigLIP 2{,}176-D representation before projection ($\\rho = 0.634$) and the DINOv2 \\texttt{patch\\_mean} ($\\rho = 0.631$).\nCLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment among pretrained encoders ($\\rho = 0.557$; Figure~\\ref{fig:rsa_bar}).\n\n\\paragraph{Self-supervised pretraining dominates.}\nDINOv2, pretrained with self-supervised objectives alone, achieves $\\rho = 0.692$---exceeding not only CLIP ($\\rho = 0.557$) but also the VLA's own internal representations at their peaks (trained image\\_mean: $0.628$; trained readout: $0.643$).\nThis ordering---self-supervised $>$ VL-pretrained---is consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\nFunctional probes corroborate the ranking: DINOv2 \\texttt{cls\\_token} achieves $R^2 = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$, $p = 0.557$, n.s.), while CLIP yields the lowest probe $R^2$ ($0.587$, $p < 0.001$ vs.\\ DINOv2).\n\n\\paragraph{Branch-split analysis.}\nTo disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) separately before fusion.\nThe two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.\nFusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone, indicating that concatenation captures complementary structure.\nThe MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.\nThe projector thus maps features into LLM-compatible dimensionality at the cost of modest geometric degradation.\n\n\\paragraph{Metric sensitivity.}\nThe choice of similarity metric matters.\nLinear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties~\\cite{kornblith2019} and underscores the importance of multi-metric evaluation.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). Self-supervised DINOv2 \\texttt{cls\\_token} achieves the highest geometric alignment ($0.692$). Fusion of both branches ($0.634$) exceeds either branch alone; the projector introduces modest compression loss ($0.634 \\to 0.615$). VLA peaks refer to the best layer for each token type. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & Notes \\\\\n\\midrule\nDINOv2 ViT-L/14 & cls\\_token & 0.692 & Standalone, highest \\\\\nFused DinoSigLIP & 2{,}176-D & 0.634 & Before projection \\\\\nDINOv2 ViT-L/14 & patch\\_mean & 0.631 & Standalone \\\\\nVLA Trained & image\\_mean (L12) & 0.628 & Peak layer \\\\\nVLA Untrained & last\\_preaction (L1) & 0.626 & Peak layer \\\\\nSigLIP branch & 1{,}088-D & 0.621 & Branch-split \\\\\nDINOv2 branch & 1{,}088-D & 0.619 & Branch-split \\\\\nDinoSigLIP+Projector & --- & 0.615 & After MLP \\\\\nVLA Untrained & image\\_mean (L0) & 0.612 & Peak layer \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & VL-pretrained \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment, followed by fused DinoSigLIP ($0.634$) and the VLA trained image\\_mean peak ($0.628$). CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic LLM Transformation}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder across its 32 layers.\n\n\\paragraph{Inverted-U pattern.}\nFigure~\\ref{fig:layer_curves} reveals a non-monotonic trajectory for trained image\\_mean RSA: $\\rho$ begins at $0.612$ (L0, equal to the projector input), rises to a peak of $0.628$ at L12---\\emph{above} the DinoSigLIP+Projector baseline ($0.615$)---then declines monotonically to $0.422$ at L32.\nThe first 12 layers thus \\emph{enhance} geometric alignment with the action space beyond the vision encoder input, while the remaining 20 layers progressively degrade it below the initial level.\nThis non-monotonic profile contrasts sharply with the untrained control, which peaks at L0 ($\\rho = 0.612$) and decays monotonically to $0.545$ at L32.\n\n\\paragraph{Peak above projector.}\nThe trained image\\_mean peak at L12 ($\\rho = 0.628$) exceeds the DinoSigLIP+Projector ($0.615$) by $\\Delta = 0.013$.\nThe LLM's middle layers contain representations more geometrically aligned with actions than the raw vision encoder output---refining, not merely preserving, the inherited structure.\n\n\\paragraph{RSA--CKA dissociation.}\nLinear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.\nRSA captures rank-order geometric alignment; CKA captures global linear structure.\nThe dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens follow the inverted-U trajectory, the readout token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves peak RSA $\\rho = 0.643$ at L12 and probe $R^2 = 0.671$ (L19), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $\\Delta = 0.041$; Table~\\ref{tab:probes}, Figure~\\ref{fig:probe_bars}).\n\n\\paragraph{Late-layer degradation.}\nThe decline from L12 to L32 ($\\rho$: $0.628 \\to 0.422$, $\\Delta = -0.206$) represents distributed degradation as the LLM repurposes image token representations for language modeling objectives.\nThis degradation exceeds the untrained decay ($0.612 \\to 0.545$, $\\Delta = -0.067$), suggesting that training actively redirects later layers away from action geometry preservation.\n\nTogether, these results characterize LLM processing as a three-phase transformation: early-layer geometric refinement, mid-layer peak, and late-layer degradation with concurrent concentration at the readout position~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations. The trained readout concentrates action information ($0.671$) beyond the projector ($0.630$), while distributed image\\_mean loses information ($0.599$). $^\\dagger$Untrained readout uses internally consistent probe hyperparameters.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nVLA Trained readout (L19) & \\textbf{0.671} & $<$0.001 \\\\\nDINOv2 cls\\_token & 0.634 & 0.557 (n.s.) \\\\\nDinoSigLIP+Projector & 0.630 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.599 & $<$0.001 \\\\\nCLIP ViT-L/14 cls & 0.587 & $<$0.001 \\\\\n\\midrule\nVLA Untrained readout (L32) & 0.686$^\\dagger$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers. Trained image\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\to$ L12 $= 0.628$ (peak, above Projector $0.615$) $\\to$ L32 $= 0.422$. Untrained image\\_mean (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2 cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The trained readout ($R^2{=}0.671$) exceeds the projector baseline ($0.630$) and all external encoders, while trained image\\_mean ($0.599$) falls below the projector. DINOv2 cls ($0.634$) is statistically indistinguishable from the projector ($p{=}0.557$).}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Redistributes, Does Not Create}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant structure or redistributes pre-existing geometry inherited from the vision encoder.\nFigure~\\ref{fig:factorial} shows the $2 \\times 2$ factorial analysis; Table~\\ref{tab:training_effects} reports bootstrap comparisons.\n\n\\paragraph{Peak shift without peak gain.}\nTraining moves the image\\_mean RSA peak from L0 to L12.\nThe trained model peaks at L12 ($\\rho = 0.628$); the untrained model peaks at L0 ($\\rho = 0.612$).\nComparing best-versus-best: $\\Delta = +0.017$, 95\\% CI includes zero, not statistically significant.\nTraining does not create geometric structure that exceeds what the vision encoder already provides---it relocates the peak deeper into the network.\n\n\\paragraph{Same-layer effect.}\nAt the same layer (L12), training produces a large effect: $\\Delta = +0.079$, $p < 0.0001$.\nThe trained model at L12 ($0.628$) far exceeds the untrained model at L12 ($0.549$).\nTraining thus has a dramatic effect on \\emph{where} action geometry peaks, but a negligible effect on \\emph{how high} it peaks.\n\n\\paragraph{Interpretation.}\nThese two results together support a routing interpretation: training teaches the LLM \\emph{where to concentrate} action-relevant structure (moving the peak from L0 to L12), not \\emph{what structure to create} (the peak value does not increase beyond the untrained best).\nThe vision encoder provides the ceiling; training determines the depth profile.\n\n\\paragraph{Instruction invariance.}\nLanguage instructions do not modulate geometric structure.\nAcross all conditions, instruction presence produces a maximum $|\\Delta| = 0.006$ in RSA, well within noise.\nThis confirms that the action geometry is visually grounded and instruction-independent~\\cite{grant2026}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training effects on action-relevant structure (bootstrap, 10{,}000 resamples). Best-vs-best comparison shows training does not create new geometry ($\\Delta{=}+0.017$, n.s.), while the same-layer comparison reveals training's large routing effect ($\\Delta{=}+0.079$, $p{<}0.0001$).}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nBest-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\\n\\quad (trained L12 vs.\\ untrained L0) & & & \\\\\nSame-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\\n\\quad (trained vs.\\ untrained) & & & \\\\\nInstruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$) without increasing the peak value beyond the untrained maximum (best-vs-best $\\Delta{=}+0.017$, n.s.). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$, confirming visually grounded action geometry.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}\n\\label{fig:metric_comparison}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 6,
        "oldLines": 76,
        "newStart": 6,
        "newLines": 76,
        "lines": [
          " ",
          " \\paragraph{Benchmark and model.}",
          " We evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.",
          "-We use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.",
          "+We use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.",
          " ",
          " \\paragraph{Representation sources.}",
          "-We extract representations from five sources:",
          "-(a)~\\textbf{DinoSigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;",
          "-(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;",
          "+We extract representations from six sources:",
          "+(a)~\\textbf{DinoSigLIP+Projector}---the fused vision encoder output after MLP projection into LLM input space;",
          "+(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer;",
          " (c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;",
          "-(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token}; and",
          "-(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}.",
          "-Sources (d) and (e) serve as external baselines with no VLA training signal.",
          "+(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} and \\texttt{patch\\_mean};",
          "+(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}; and",
          "+(f)~\\textbf{Branch-split}---the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) extracted separately before fusion, plus the fused 2{,}176-D representation before projection.",
          "+Sources (d)--(f) serve as external or ablation baselines with no VLA training signal.",
          " ",
          " \\paragraph{Experimental conditions.}",
          " We use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).",
          "-The untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.",
          "+The untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder and the projector architecture, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.",
          " ",
          "-\\paragraph{Representational Similarity Analysis (RSA).}",
          "-Following~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.",
          "-We report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples.",
          "+\\paragraph{RSA.}",
          "+Following~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) using Euclidean distance for each representation source and for the 7-dimensional action space, with within-task pairing across 50 demonstrations per task.",
          "+We report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples (\\S\\ref{sec:rsa}).",
          " ",
          " \\paragraph{Functional probes.}",
          "-We train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions.",
          "+We train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions (\\S\\ref{sec:probes}).",
          " ",
          " %------------------------------------------------------------------",
          " \\subsection{Vision Encoder Dominance}",
          " \\label{sec:vision_dominance}",
          " ",
          "-This experiment tests which pretrained vision encoders provide the strongest source of action-relevant geometric structure in VLA representations.",
          "+This experiment tests which pretrained vision encoders provide the strongest action-relevant geometric structure.",
          " ",
          " Table~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.",
          "-Standalone DINOv2 achieves the highest alignment ($\\rho = 0.631$), followed by DinoSigLIP+Projector ($\\rho = 0.615$, 95\\% CI $[0.526, 0.695]$) and CLIP ViT-L/14 ($\\rho = 0.557$, $[0.442, 0.660]$).",
          "-All pretrained encoders substantially exceed the VLA's LLM layers (best image\\_mean: $\\rho = 0.501$; Figure~\\ref{fig:rsa_bar}).",
          "+The standalone DINOv2 \\texttt{cls\\_token} achieves the highest alignment of any representation source ($\\rho = 0.692$), followed by the fused DinoSigLIP 2{,}176-D representation before projection ($\\rho = 0.634$) and the DINOv2 \\texttt{patch\\_mean} ($\\rho = 0.631$).",
          "+CLIP ViT-L/14, a vision-language contrastive model, achieves the lowest alignment among pretrained encoders ($\\rho = 0.557$; Figure~\\ref{fig:rsa_bar}).",
          " ",
          "-Three findings emerge.",
          "-First, self-supervised pretraining provides action-relevant geometric structure at least as strong as vision-language pretraining.",
          "-DINOv2, pretrained with self-supervised objectives alone, achieves $\\rho = 0.631$---the highest RSA of any representation source, numerically exceeding the DinoSigLIP+Projector ($\\rho = 0.615$), which combines DINOv2 with SigLIP features.",
          "-Vision-language contrastive pretraining (CLIP, $\\rho = 0.557$) yields the weakest geometry among pretrained encoders, consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.",
          "+\\paragraph{Self-supervised pretraining dominates.}",
          "+DINOv2, pretrained with self-supervised objectives alone, achieves $\\rho = 0.692$---exceeding not only CLIP ($\\rho = 0.557$) but also the VLA's own internal representations at their peaks (trained image\\_mean: $0.628$; trained readout: $0.643$).",
          "+This ordering---self-supervised $>$ VL-pretrained---is consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.",
          "+Functional probes corroborate the ranking: DINOv2 \\texttt{cls\\_token} achieves $R^2 = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$, $p = 0.557$, n.s.), while CLIP yields the lowest probe $R^2$ ($0.587$, $p < 0.001$ vs.\\ DINOv2).",
          " ",
          "-Second, fusing with SigLIP and projecting into LLM space does not improve geometric alignment over standalone DINOv2: DinoSigLIP+Projector ($0.615$) is numerically below standalone DINOv2 ($0.631$), indicating that the projector maps features into LLM space without enhancing the self-supervised geometry already present.",
          "+\\paragraph{Branch-split analysis.}",
          "+To disentangle the contributions of the two encoder streams within DinoSigLIP, we extract representations from the DINOv2 branch (1{,}088-D) and SigLIP branch (1{,}088-D) separately before fusion.",
          "+The two branches yield near-identical RSA: DINOv2 branch $\\rho = 0.619$, SigLIP branch $\\rho = 0.621$.",
          "+Fusion produces a representation ($\\rho = 0.634$) that exceeds either branch alone, indicating that concatenation captures complementary structure.",
          "+The MLP projector then compresses this signal: DinoSigLIP+Projector achieves $\\rho = 0.615$, a drop of $\\Delta = 0.019$ from the fused 2{,}176-D input.",
          "+The projector thus maps features into LLM-compatible dimensionality at the cost of modest geometric degradation.",
          " ",
          "-Third, the LLM degrades rather than enhances vision encoder geometry.",
          "-Processing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\\_mean), a drop of $\\Delta = 0.114$.",
          "-",
          "-\\paragraph{Convergent rankings across metrics.}",
          "-Functional probes corroborate the RSA ordering.",
          "-Under unified probe hyperparameters, DINOv2 achieves $R^2 = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$, $p = 0.557$, n.s.), while CLIP achieves the lowest $R^2$ ($0.587$, $p < 0.001$ vs.\\ DINOv2).",
          "-Both RSA and probe $R^2$ rank DINOv2 $\\geq$ DinoSigLIP+Projector $>$ CLIP, indicating that self-supervised features provide at least as much action-relevant structure as VL-pretrained features on both geometric and functional dimensions.",
          "-",
          " \\paragraph{Metric sensitivity.}",
          "-However, the choice of similarity metric matters.",
          "-Linear CKA~\\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\\ref{fig:metric_comparison}).",
          "-RDM kernel CKA yields a near-identical ordering (Trained $\\approx$ Proj $>$ Untrained $>$ DINOv2), with the Trained--Projector gap negligible ($\\Delta = 0.003$).",
          "-This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.",
          "+The choice of similarity metric matters.",
          "+Linear CKA~\\cite{kornblith2019} reverses the RSA ordering: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially inverting the self-supervised advantage (Figure~\\ref{fig:metric_comparison}).",
          "+RDM kernel CKA partially resolves this discrepancy: trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ untrained ($0.246$) $>$ DINOv2 ($0.241$).",
          "+This divergence reflects the known sensitivity of representation similarity metrics to different geometric properties~\\cite{kornblith2019} and underscores the importance of multi-metric evaluation.",
          " ",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). Self-supervised DINOv2 achieves the highest geometric alignment, followed by the DinoSigLIP+Projector and VL-pretrained CLIP. All pretrained encoders exceed LLM-processed representations. 95\\% CIs from 10{,}000 bootstrap resamples.}",
          "+\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). Self-supervised DINOv2 \\texttt{cls\\_token} achieves the highest geometric alignment ($0.692$). Fusion of both branches ($0.634$) exceeds either branch alone; the projector introduces modest compression loss ($0.634 \\to 0.615$). VLA peaks refer to the best layer for each token type. 95\\% CIs from 10{,}000 bootstrap resamples.}",
          " \\label{tab:rsa_overview}",
          " \\small",
          " \\begin{tabular}{llcc}",
          " \\toprule",
          "-Source & Aggregation & RSA $\\rho$ & 95\\% CI \\\\",
          "+Source & Aggregation & RSA $\\rho$ & Notes \\\\",
          " \\midrule",
          "-DINOv2 ViT-L/14 & patch\\_mean & 0.631 & --- \\\\",
          "-DinoSigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\\\",
          "-CLIP ViT-L/14 & patch\\_mean & 0.557 & {[0.442, 0.660]} \\\\",
          "-\\midrule",
          "-VLA Trained w/ inst. & image\\_mean & 0.501 & --- \\\\",
          "-VLA Trained no inst. & image\\_mean & 0.501 & --- \\\\",
          "-VLA Untrained w/ inst. & image\\_mean & 0.485 & --- \\\\",
          "-VLA Untrained no inst. & image\\_mean & 0.482 & --- \\\\",
          "+DINOv2 ViT-L/14 & cls\\_token & 0.692 & Standalone, highest \\\\",
          "+Fused DinoSigLIP & 2{,}176-D & 0.634 & Before projection \\\\",
          "+DINOv2 ViT-L/14 & patch\\_mean & 0.631 & Standalone \\\\",
          "+VLA Trained & image\\_mean (L12) & 0.628 & Peak layer \\\\",
          "+VLA Untrained & last\\_preaction (L1) & 0.626 & Peak layer \\\\",
          "+SigLIP branch & 1{,}088-D & 0.621 & Branch-split \\\\",
          "+DINOv2 branch & 1{,}088-D & 0.619 & Branch-split \\\\",
          "+DinoSigLIP+Projector & --- & 0.615 & After MLP \\\\",
          "+VLA Untrained & image\\_mean (L0) & 0.612 & Peak layer \\\\",
          "+CLIP ViT-L/14 & patch\\_mean & 0.557 & VL-pretrained \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
        ]
      },
      {
        "oldStart": 83,
        "oldLines": 46,
        "newStart": 83,
        "newLines": 56,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{figures/fig2.pdf}",
          "-\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 ($\\rho{=}0.631$) achieves the highest geometric alignment, followed by DinoSigLIP+Projector ($\\rho{=}0.615$) and CLIP ($\\rho{=}0.557$). All pretrained encoders exceed LLM-processed representations ($\\rho \\leq 0.501$). Hatched bars indicate no-instruction conditions. Error bars: 95\\% bootstrap CIs.}",
          "+\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 \\texttt{cls\\_token} ($\\rho{=}0.692$) achieves the highest geometric alignment, followed by fused DinoSigLIP ($0.634$) and the VLA trained image\\_mean peak ($0.628$). CLIP ($0.557$) yields the weakest alignment among pretrained encoders. Error bars: 95\\% bootstrap CIs.}",
          " \\label{fig:rsa_bar}",
          " \\end{figure}",
          " ",
          " %------------------------------------------------------------------",
          "-\\subsection{LLM Redistributes, Does Not Enhance, Action Structure}",
          "+\\subsection{Non-Monotonic LLM Transformation}",
          " \\label{sec:llm_redistribution}",
          " ",
          "-This experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.",
          "-Table~\\ref{tab:probes} reports functional probe $R^2$ for key representation sources.",
          "-Two complementary effects characterize LLM processing.",
          "+This experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder across its 32 layers.",
          " ",
          "-\\paragraph{Distributed degradation.}",
          "-Averaging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.",
          "-RSA drops from $0.615$ to $0.501$ ($\\Delta = 0.114$); probe $R^2$ drops from $0.630$ to $0.599$ ($\\Delta = 0.031$, $p < 0.001$).",
          "-Figure~\\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.",
          "+\\paragraph{Inverted-U pattern.}",
          "+Figure~\\ref{fig:layer_curves} reveals a non-monotonic trajectory for trained image\\_mean RSA: $\\rho$ begins at $0.612$ (L0, equal to the projector input), rises to a peak of $0.628$ at L12---\\emph{above} the DinoSigLIP+Projector baseline ($0.615$)---then declines monotonically to $0.422$ at L32.",
          "+The first 12 layers thus \\emph{enhance} geometric alignment with the action space beyond the vision encoder input, while the remaining 20 layers progressively degrade it below the initial level.",
          "+This non-monotonic profile contrasts sharply with the untrained control, which peaks at L0 ($\\rho = 0.612$) and decays monotonically to $0.545$ at L32.",
          " ",
          "+\\paragraph{Peak above projector.}",
          "+The trained image\\_mean peak at L12 ($\\rho = 0.628$) exceeds the DinoSigLIP+Projector ($0.615$) by $\\Delta = 0.013$.",
          "+The LLM's middle layers contain representations more geometrically aligned with actions than the raw vision encoder output---refining, not merely preserving, the inherited structure.",
          "+",
          "+\\paragraph{RSA--CKA dissociation.}",
          "+Linear CKA between image\\_mean and the action space rises monotonically from L0 ($0.081$) to L32 ($0.098$), showing no inverted-U pattern.",
          "+RSA captures rank-order geometric alignment; CKA captures global linear structure.",
          "+The dissociation indicates that the geometric refinement in early layers operates on the relative arrangement of representations (affecting RSA) without altering the overall covariance structure (captured by CKA).",
          "+",
          " \\paragraph{Readout concentration.}",
          "-While distributed image tokens lose information, the last pre-action token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.",
          "-Trained readout achieves $R^2 = 0.671$, exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $\\Delta = 0.041$; Figure~\\ref{fig:probe_bars}).",
          "-This concentration is training-dependent: under internally consistent probes, trained readout substantially exceeds untrained readout ($\\Delta R^2 = 0.045$, $p < 0.0001$; \\S\\ref{sec:training_routing}).",
          "+While distributed image tokens follow the inverted-U trajectory, the readout token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.",
          "+Trained readout achieves peak RSA $\\rho = 0.643$ at L12 and probe $R^2 = 0.671$ (L19), both exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $\\Delta = 0.041$; Table~\\ref{tab:probes}, Figure~\\ref{fig:probe_bars}).",
          " ",
          "-Together, these results characterize the LLM as a \\emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\\cite{haon2025}.",
          "+\\paragraph{Late-layer degradation.}",
          "+The decline from L12 to L32 ($\\rho$: $0.628 \\to 0.422$, $\\Delta = -0.206$) represents distributed degradation as the LLM repurposes image token representations for language modeling objectives.",
          "+This degradation exceeds the untrained decay ($0.612 \\to 0.545$, $\\Delta = -0.067$), suggesting that training actively redirects later layers away from action geometry preservation.",
          " ",
          "+Together, these results characterize LLM processing as a three-phase transformation: early-layer geometric refinement, mid-layer peak, and late-layer degradation with concurrent concentration at the readout position~\\cite{haon2025}.",
          "+",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations (unified D036 hyperparameters). The LLM degrades distributed representations (image\\_mean) relative to the projector but concentrates superior action information at the readout token. RSA and $R^2$ rankings run in opposite directions: CLIP shows the strongest geometric alignment among external encoders but the lowest $R^2$. $^\\dagger$Untrained readout uses p0 probes with internally consistent hyperparameters.}",
          "+\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations. The trained readout concentrates action information ($0.671$) beyond the projector ($0.630$), while distributed image\\_mean loses information ($0.599$). $^\\dagger$Untrained readout uses internally consistent probe hyperparameters.}",
          " \\label{tab:probes}",
          " \\small",
          " \\begin{tabular}{lcc}",
          " \\toprule",
          " Representation & $R^2$ & $p$ vs.\\ Proj. \\\\",
          " \\midrule",
          "-DinoSigLIP+Projector & 0.630 & --- \\\\",
          "-VLA Trained image\\_mean (L19) & 0.599 & $<$0.001 \\\\",
          " VLA Trained readout (L19) & \\textbf{0.671} & $<$0.001 \\\\",
          "-VLA Untrained readout (L32) & 0.686$^\\dagger$ & --- \\\\",
          "-\\midrule",
          " DINOv2 cls\\_token & 0.634 & 0.557 (n.s.) \\\\",
          "+DinoSigLIP+Projector & 0.630 & --- \\\\",
          "+VLA Trained image\\_mean (L19) & 0.599 & $<$0.001 \\\\",
          " CLIP ViT-L/14 cls & 0.587 & $<$0.001 \\\\",
          "+\\midrule",
          "+VLA Untrained readout (L32) & 0.686$^\\dagger$ & --- \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
        ]
      },
      {
        "oldStart": 130,
        "oldLines": 54,
        "newStart": 140,
        "newLines": 58,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{figures/fig3.pdf}",
          "-\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: DINOv2 ($\\rho{=}0.631$) and DinoSigLIP+Projector ($\\rho{=}0.615$) reference levels.}",
          "+\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers. Trained image\\_mean (solid blue) follows an inverted-U: L0 $= 0.612 \\to$ L12 $= 0.628$ (peak, above Projector $0.615$) $\\to$ L32 $= 0.422$. Untrained image\\_mean (dashed blue) peaks at L0 and decays monotonically. Dashed horizontal lines: DINOv2 cls ($0.692$), Fused DinoSigLIP ($0.634$), Projector ($0.615$).}",
          " \\label{fig:layer_curves}",
          " \\end{figure}",
          " ",
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{figures/fig4.pdf}",
          "-\\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\\_mean ($R^2{=}0.599$) below the projector baseline ($0.630$) but concentrates superior information at the trained readout ($0.671$). DINOv2 ($0.634$) is statistically indistinguishable from the projector ($p{=}0.557$). Rankings are consistent with RSA: DINOv2 $\\geq$ Projector $>$ CLIP ($0.587$), reinforcing the convergent ordering across geometric and functional metrics.}",
          "+\\caption{Functional probe $R^2$ for action prediction. The trained readout ($R^2{=}0.671$) exceeds the projector baseline ($0.630$) and all external encoders, while trained image\\_mean ($0.599$) falls below the projector. DINOv2 cls ($0.634$) is statistically indistinguishable from the projector ($p{=}0.557$).}",
          " \\label{fig:probe_bars}",
          " \\end{figure}",
          " ",
          " %------------------------------------------------------------------",
          "-\\subsection{Training Routes, Does Not Create, Action Geometry}",
          "+\\subsection{Training Redistributes, Does Not Create}",
          " \\label{sec:training_routing}",
          " ",
          "-This experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.",
          "-Table~\\ref{tab:training_effects} reports the effect of training across metrics.",
          "-The $2 \\times 2$ factorial analysis (Figure~\\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.",
          "+This experiment tests whether LLM training creates new action-relevant structure or redistributes pre-existing geometry inherited from the vision encoder.",
          "+Figure~\\ref{fig:factorial} shows the $2 \\times 2$ factorial analysis; Table~\\ref{tab:training_effects} reports bootstrap comparisons.",
          " ",
          "-\\paragraph{Geometric invariance to training.}",
          "-Training does not alter the LLM's geometric alignment with the action space.",
          "-For image\\_mean RSA, the training effect is $\\Delta = +0.021$ (95\\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\\_preaction RSA, $\\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).",
          "-This null result is consistent with the vision encoder---whose weights are identical between conditions ($\\cos\\text{sim} = 1.0$)---being the sole source of action-relevant geometry.",
          "+\\paragraph{Peak shift without peak gain.}",
          "+Training moves the image\\_mean RSA peak from L0 to L12.",
          "+The trained model peaks at L12 ($\\rho = 0.628$); the untrained model peaks at L0 ($\\rho = 0.612$).",
          "+Comparing best-versus-best: $\\Delta = +0.017$, 95\\% CI includes zero, not statistically significant.",
          "+Training does not create geometric structure that exceeds what the vision encoder already provides---it relocates the peak deeper into the network.",
          " ",
          "-\\paragraph{Geometric invariance to instruction.}",
          "-Language instructions similarly fail to modulate geometric structure.",
          "-Across the $2 \\times 2$ matrix, the instruction effect is $\\Delta = 0.004$ (n.s.).",
          "-A dedicated control experiment with four instruction conditions---normal task instructions ($\\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\\pm 0.017$ of the normal-instruction condition ($\\rho = 0.489$; Figure~\\ref{fig:factorial}b).",
          "+\\paragraph{Same-layer effect.}",
          "+At the same layer (L12), training produces a large effect: $\\Delta = +0.079$, $p < 0.0001$.",
          "+The trained model at L12 ($0.628$) far exceeds the untrained model at L12 ($0.549$).",
          "+Training thus has a dramatic effect on \\emph{where} action geometry peaks, but a negligible effect on \\emph{how high} it peaks.",
          " ",
          "-\\paragraph{Functional concentration requires training.}",
          "-In contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\\Delta = +0.045$ ($p < 0.0001$).\\footnote{The training effect comparison uses internally consistent p0 probes (trained readout $R^2 = 0.731$, untrained $0.686$) to ensure valid within-condition comparison; absolute values differ from the cross-representation comparison in Table~\\ref{tab:probes}, which uses unified hyperparameters.}",
          "-Training concentrates action-relevant information at the readout without altering the underlying geometry.",
          "+\\paragraph{Interpretation.}",
          "+These two results together support a routing interpretation: training teaches the LLM \\emph{where to concentrate} action-relevant structure (moving the peak from L0 to L12), not \\emph{what structure to create} (the peak value does not increase beyond the untrained best).",
          "+The vision encoder provides the ceiling; training determines the depth profile.",
          " ",
          "-These results support a \\emph{routing} interpretation of LLM training in VLAs~\\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.",
          "+\\paragraph{Instruction invariance.}",
          "+Language instructions do not modulate geometric structure.",
          "+Across all conditions, instruction presence produces a maximum $|\\Delta| = 0.006$ in RSA, well within noise.",
          "+This confirms that the action geometry is visually grounded and instruction-independent~\\cite{grant2026}.",
          " ",
          " \\begin{table}[t]",
          " \\centering",
          "-\\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\\_mean $R^2$ drop confirms distributed degradation.}",
          "+\\caption{Training effects on action-relevant structure (bootstrap, 10{,}000 resamples). Best-vs-best comparison shows training does not create new geometry ($\\Delta{=}+0.017$, n.s.), while the same-layer comparison reveals training's large routing effect ($\\Delta{=}+0.079$, $p{<}0.0001$).}",
          " \\label{tab:training_effects}",
          " \\small",
          " \\begin{tabular}{lccc}",
          " \\toprule",
          " Comparison & $\\Delta$ & 95\\% CI & $p$ \\\\",
          " \\midrule",
          "-Training (image\\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\\\",
          "-Training (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\\\",
          "-Training (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\\\",
          "-Proj.\\ vs.\\ image\\_mean ($R^2$) & $+$0.031 & --- & $<$0.001 \\\\",
          "+Best-vs-best image\\_mean & $+$0.017 & incl.\\ 0 & n.s. \\\\",
          "+\\quad (trained L12 vs.\\ untrained L0) & & & \\\\",
          "+Same-layer L12 image\\_mean & $+$0.079 & excl.\\ 0 & $<$0.0001 \\\\",
          "+\\quad (trained vs.\\ untrained) & & & \\\\",
          "+Instruction effect (max $|\\Delta|$) & 0.006 & --- & n.s. \\\\",
          " \\bottomrule",
          " \\end{tabular}",
          " \\end{table}"
        ]
      },
      {
        "oldStart": 185,
        "oldLines": 13,
        "newStart": 199,
        "newLines": 13,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{figures/fig5.pdf}",
          "-\\caption{\\textbf{(a)}~Training $\\times$ Instruction matrix for image\\_mean RSA ($\\rho$). Neither training ($\\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\\Delta{=}0.004$, n.s.)\\ produces a statistically detectable effect. \\textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\\pm 0.017$ of the normal-instruction condition ($\\rho{=}0.489$), confirming that instruction content does not modulate distributed geometric structure.}",
          "+\\caption{\\textbf{(a)}~Trained vs.\\ untrained image\\_mean RSA profiles. Training shifts the peak from L0 ($0.612$) to L12 ($0.628$) without increasing the peak value beyond the untrained maximum (best-vs-best $\\Delta{=}+0.017$, n.s.). \\textbf{(b)}~Instruction invariance: all conditions within $|\\Delta|{<}0.006$, confirming visually grounded action geometry.}",
          " \\label{fig:factorial}",
          " \\end{figure}",
          " ",
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{figures/fig6.pdf}",
          "-\\caption{Comparison of three similarity metrics across representation sources. \\textbf{(a)}~RSA (Spearman $\\rho$) ranks Proj $>$ Trained; \\textbf{(c)}~RDM kernel CKA yields Trained $\\approx$ Proj ($\\Delta{=}0.003$) $>$ Untrained $>$ DINOv2. \\textbf{(b)}~Linear CKA~\\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}",
          "+\\caption{Three similarity metrics across representation sources. \\textbf{(a)}~RSA ranks DINOv2 cls ($0.692$) $>$ Fused ($0.634$) $>$ Projector ($0.615$). \\textbf{(b)}~Linear CKA reverses the ordering: Untrained ($0.089$) $>$ Trained ($0.083$) $>$ Projector ($0.081$) $>$ DINOv2 ($0.066$). \\textbf{(c)}~RDM kernel CKA: Trained ($0.260$) $\\approx$ Projector ($0.257$) $>$ Untrained ($0.246$) $>$ DINOv2 ($0.241$). The metric divergence underscores that RSA and CKA capture different aspects of representational structure.}",
          " \\label{fig:metric_comparison}",
          " \\end{figure}"
        ]
      }
    ],
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Benchmark and model.}\nWe evaluate on the LIBERO-Goal suite~\\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.\nWe use OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a DinoSigLIP fused vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector, and a Llama-2 7B language backbone, pretrained on the Open X-Embodiment dataset.\n\n\\paragraph{Representation sources.}\nWe extract representations from five sources:\n(a)~\\textbf{DinoSigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;\n(b)~\\textbf{LLM image\\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;\n(c)~\\textbf{LLM last\\_preaction}---the final token position before action decoding (readout token) at each LLM layer;\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token}; and\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean}.\nSources (d) and (e) serve as external baselines with no VLA training signal.\n\n\\paragraph{Experimental conditions.}\nWe use a $2 \\times 2$ factorial design crossing \\emph{training status} (trained vs.\\ untrained) with \\emph{instruction presence} (with vs.\\ without language instruction).\nThe untrained control applies \\texttt{from\\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen DinoSigLIP encoder, isolating the LLM's learned contribution from the vision encoder's pretrained geometry.\n\n\\paragraph{Representational Similarity Analysis (RSA).}\nFollowing~\\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.\nWe report Spearman rank correlation $\\rho$ between representation and action RDMs, with 95\\% confidence intervals from 10{,}000 bootstrap resamples.\n\n\\paragraph{Functional probes.}\nWe train MLP probes (input $\\to$ 256 $\\to$ 7) with Adam (lr${}=10^{-3}$, batch size 256, 50 epochs, early stopping patience 5) to predict 7-D action vectors from frozen representations~\\cite{alain2017}. We report mean $R^2$ across action dimensions.\n\n%------------------------------------------------------------------\n\\subsection{Vision Encoder Dominance}\n\\label{sec:vision_dominance}\n\nThis experiment tests which pretrained vision encoders provide the strongest source of action-relevant geometric structure in VLA representations.\n\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ between each representation source and the action space.\nStandalone DINOv2 achieves the highest alignment ($\\rho = 0.631$), followed by DinoSigLIP+Projector ($\\rho = 0.615$, 95\\% CI $[0.526, 0.695]$) and CLIP ViT-L/14 ($\\rho = 0.557$, $[0.442, 0.660]$).\nAll pretrained encoders substantially exceed the VLA's LLM layers (best image\\_mean: $\\rho = 0.501$; Figure~\\ref{fig:rsa_bar}).\n\nThree findings emerge.\nFirst, self-supervised pretraining provides action-relevant geometric structure at least as strong as vision-language pretraining.\nDINOv2, pretrained with self-supervised objectives alone, achieves $\\rho = 0.631$---the highest RSA of any representation source, numerically exceeding the DinoSigLIP+Projector ($\\rho = 0.615$), which combines DINOv2 with SigLIP features.\nVision-language contrastive pretraining (CLIP, $\\rho = 0.557$) yields the weakest geometry among pretrained encoders, consistent with behavioral evidence of visual dominance in VLA policies~\\cite{grant2026}.\n\nSecond, fusing with SigLIP and projecting into LLM space does not improve geometric alignment over standalone DINOv2: DinoSigLIP+Projector ($0.615$) is numerically below standalone DINOv2 ($0.631$), indicating that the projector maps features into LLM space without enhancing the self-supervised geometry already present.\n\nThird, the LLM degrades rather than enhances vision encoder geometry.\nProcessing through the LLM reduces RSA from $0.615$ (projector output) to $0.501$ (best LLM image\\_mean), a drop of $\\Delta = 0.114$.\n\n\\paragraph{Convergent rankings across metrics.}\nFunctional probes corroborate the RSA ordering.\nUnder unified probe hyperparameters, DINOv2 achieves $R^2 = 0.634$, statistically indistinguishable from DinoSigLIP+Projector ($R^2 = 0.630$, $p = 0.557$, n.s.), while CLIP achieves the lowest $R^2$ ($0.587$, $p < 0.001$ vs.\\ DINOv2).\nBoth RSA and probe $R^2$ rank DINOv2 $\\geq$ DinoSigLIP+Projector $>$ CLIP, indicating that self-supervised features provide at least as much action-relevant structure as VL-pretrained features on both geometric and functional dimensions.\n\n\\paragraph{Metric sensitivity.}\nHowever, the choice of similarity metric matters.\nLinear CKA~\\cite{kornblith2019} produces a different ranking from RSA: untrained LLM ($\\text{CKA} = 0.089$) $>$ trained LLM ($0.083$) $>$ DinoSigLIP+Projector ($0.081$) $>$ DINOv2 ($0.066$), partially reversing the RSA ordering (Figure~\\ref{fig:metric_comparison}).\nRDM kernel CKA yields a near-identical ordering (Trained $\\approx$ Proj $>$ Untrained $>$ DINOv2), with the Trained--Projector gap negligible ($\\Delta = 0.003$).\nThis divergence reflects the known sensitivity of representation similarity metrics to different geometric properties and underscores the importance of multi-metric evaluation in representation analysis.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA between representation and action RDMs ($\\rho$ $\\uparrow$). Self-supervised DINOv2 achieves the highest geometric alignment, followed by the DinoSigLIP+Projector and VL-pretrained CLIP. All pretrained encoders exceed LLM-processed representations. 95\\% CIs from 10{,}000 bootstrap resamples.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{llcc}\n\\toprule\nSource & Aggregation & RSA $\\rho$ & 95\\% CI \\\\\n\\midrule\nDINOv2 ViT-L/14 & patch\\_mean & 0.631 & --- \\\\\nDinoSigLIP+Projector & --- & 0.615 & {[0.526, 0.695]} \\\\\nCLIP ViT-L/14 & patch\\_mean & 0.557 & {[0.442, 0.660]} \\\\\n\\midrule\nVLA Trained w/ inst. & image\\_mean & 0.501 & --- \\\\\nVLA Trained no inst. & image\\_mean & 0.501 & --- \\\\\nVLA Untrained w/ inst. & image\\_mean & 0.485 & --- \\\\\nVLA Untrained no inst. & image\\_mean & 0.482 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig2.pdf}\n\\caption{RSA with the action space ($\\rho$) across representation sources. Self-supervised DINOv2 ($\\rho{=}0.631$) achieves the highest geometric alignment, followed by DinoSigLIP+Projector ($\\rho{=}0.615$) and CLIP ($\\rho{=}0.557$). All pretrained encoders exceed LLM-processed representations ($\\rho \\leq 0.501$). Hatched bars indicate no-instruction conditions. Error bars: 95\\% bootstrap CIs.}\n\\label{fig:rsa_bar}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{LLM Redistributes, Does Not Enhance, Action Structure}\n\\label{sec:llm_redistribution}\n\nThis experiment tests how the LLM transforms the action-relevant structure inherited from the vision encoder.\nTable~\\ref{tab:probes} reports functional probe $R^2$ for key representation sources.\nTwo complementary effects characterize LLM processing.\n\n\\paragraph{Distributed degradation.}\nAveraging across image tokens, the LLM degrades both geometric and functional action information relative to the projector.\nRSA drops from $0.615$ to $0.501$ ($\\Delta = 0.114$); probe $R^2$ drops from $0.630$ to $0.599$ ($\\Delta = 0.031$, $p < 0.001$).\nFigure~\\ref{fig:layer_curves} shows the per-layer trajectory: the sharpest drop occurs at the embedding interface (Projector $\\to$ Layer~1), with non-monotonic fluctuations through middle layers before partial recovery near the output layers.\n\n\\paragraph{Readout concentration.}\nWhile distributed image tokens lose information, the last pre-action token (\\texttt{last\\_preaction}) concentrates action-relevant information beyond the projector baseline.\nTrained readout achieves $R^2 = 0.671$, exceeding DinoSigLIP+Projector ($R^2 = 0.630$, $\\Delta = 0.041$; Figure~\\ref{fig:probe_bars}).\nThis concentration is training-dependent: under internally consistent probes, trained readout substantially exceeds untrained readout ($\\Delta R^2 = 0.045$, $p < 0.0001$; \\S\\ref{sec:training_routing}).\n\nTogether, these results characterize the LLM as a \\emph{redistribution} mechanism: training teaches the model to route action-relevant information from distributed image tokens to the readout position, sacrificing distributed fidelity to concentrate a functionally superior action representation at the decoding interface~\\cite{haon2025}.\n\n\\begin{table}[t]\n\\centering\n\\caption{Functional probe $R^2$ ($\\uparrow$) for action prediction from frozen representations (unified D036 hyperparameters). The LLM degrades distributed representations (image\\_mean) relative to the projector but concentrates superior action information at the readout token. RSA and $R^2$ rankings run in opposite directions: CLIP shows the strongest geometric alignment among external encoders but the lowest $R^2$. $^\\dagger$Untrained readout uses p0 probes with internally consistent hyperparameters.}\n\\label{tab:probes}\n\\small\n\\begin{tabular}{lcc}\n\\toprule\nRepresentation & $R^2$ & $p$ vs.\\ Proj. \\\\\n\\midrule\nDinoSigLIP+Projector & 0.630 & --- \\\\\nVLA Trained image\\_mean (L19) & 0.599 & $<$0.001 \\\\\nVLA Trained readout (L19) & \\textbf{0.671} & $<$0.001 \\\\\nVLA Untrained readout (L32) & 0.686$^\\dagger$ & --- \\\\\n\\midrule\nDINOv2 cls\\_token & 0.634 & 0.557 (n.s.) \\\\\nCLIP ViT-L/14 cls & 0.587 & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$) with the action space across all 32 LLM layers under four experimental conditions (trained/untrained $\\times$ with/without instruction). The sharpest drop occurs at the embedding interface (Proj $\\to$ L1). Middle layers show non-monotonic fluctuations. Dashed lines: DINOv2 ($\\rho{=}0.631$) and DinoSigLIP+Projector ($\\rho{=}0.615$) reference levels.}\n\\label{fig:layer_curves}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4.pdf}\n\\caption{Functional probe $R^2$ for action prediction. The LLM degrades distributed image\\_mean ($R^2{=}0.599$) below the projector baseline ($0.630$) but concentrates superior information at the trained readout ($0.671$). DINOv2 ($0.634$) is statistically indistinguishable from the projector ($p{=}0.557$). Rankings are consistent with RSA: DINOv2 $\\geq$ Projector $>$ CLIP ($0.587$), reinforcing the convergent ordering across geometric and functional metrics.}\n\\label{fig:probe_bars}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Training Routes, Does Not Create, Action Geometry}\n\\label{sec:training_routing}\n\nThis experiment tests whether LLM training creates new action-relevant geometric structure or merely routes pre-existing structure inherited from the vision encoder.\nTable~\\ref{tab:training_effects} reports the effect of training across metrics.\nThe $2 \\times 2$ factorial analysis (Figure~\\ref{fig:factorial}) reveals a striking dissociation: training has no detectable effect on geometric structure but a large effect on functional concentration.\n\n\\paragraph{Geometric invariance to training.}\nTraining does not alter the LLM's geometric alignment with the action space.\nFor image\\_mean RSA, the training effect is $\\Delta = +0.021$ (95\\% CI $[-0.031, +0.064]$, $p = 0.20$, n.s.); for last\\_preaction RSA, $\\Delta = +0.008$ ($[-0.040, +0.056]$, $p = 0.37$, n.s.).\nThis null result is consistent with the vision encoder---whose weights are identical between conditions ($\\cos\\text{sim} = 1.0$)---being the sole source of action-relevant geometry.\n\n\\paragraph{Geometric invariance to instruction.}\nLanguage instructions similarly fail to modulate geometric structure.\nAcross the $2 \\times 2$ matrix, the instruction effect is $\\Delta = 0.004$ (n.s.).\nA dedicated control experiment with four instruction conditions---normal task instructions ($\\rho = 0.489$), random instructions from other tasks ($0.484$), word-shuffled instructions ($0.483$), and empty strings ($0.472$)---confirms content invariance: all values fall within $\\pm 0.017$ of the normal-instruction condition ($\\rho = 0.489$; Figure~\\ref{fig:factorial}b).\n\n\\paragraph{Functional concentration requires training.}\nIn contrast to the geometric null results, readout probe $R^2$ shows a large training effect: $\\Delta = +0.045$ ($p < 0.0001$).\\footnote{The training effect comparison uses internally consistent p0 probes (trained readout $R^2 = 0.731$, untrained $0.686$) to ensure valid within-condition comparison; absolute values differ from the cross-representation comparison in Table~\\ref{tab:probes}, which uses unified hyperparameters.}\nTraining concentrates action-relevant information at the readout without altering the underlying geometry.\n\nThese results support a \\emph{routing} interpretation of LLM training in VLAs~\\cite{brohan2023_rt2}: the LLM learns to concentrate pre-existing vision-encoder geometry at the readout position for action decoding, rather than constructing new action-relevant representations.\n\n\\begin{table}[t]\n\\centering\n\\caption{Training and instruction effects on action-relevant structure. Training does not alter geometric alignment (RSA, both n.s.)\\ but enables functional concentration at the readout token ($R^2$, $p < 0.0001$). The projector-to-image\\_mean $R^2$ drop confirms distributed degradation.}\n\\label{tab:training_effects}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta$ & 95\\% CI & $p$ \\\\\n\\midrule\nTraining (image\\_mean RSA) & $+$0.021 & [$-$0.031, $+$0.064] & 0.20 \\\\\nTraining (readout RSA) & $+$0.008 & [$-$0.040, $+$0.056] & 0.37 \\\\\nTraining (readout $R^2$) & $+$0.045 & [$+$0.032, $+$0.058] & $<$0.0001 \\\\\nProj.\\ vs.\\ image\\_mean ($R^2$) & $+$0.031 & --- & $<$0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5.pdf}\n\\caption{\\textbf{(a)}~Training $\\times$ Instruction matrix for image\\_mean RSA ($\\rho$). Neither training ($\\Delta{=}0.021$, $p{=}0.20$) nor instruction ($\\Delta{=}0.004$, n.s.)\\ produces a statistically detectable effect. \\textbf{(b)}~Instruction content control: normal ($0.489$), random ($0.484$), shuffled ($0.483$), and empty ($0.472$) instructions all yield RSA within $\\pm 0.017$ of the normal-instruction condition ($\\rho{=}0.489$), confirming that instruction content does not modulate distributed geometric structure.}\n\\label{fig:factorial}\n\\end{figure}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig6.pdf}\n\\caption{Comparison of three similarity metrics across representation sources. \\textbf{(a)}~RSA (Spearman $\\rho$) ranks Proj $>$ Trained; \\textbf{(c)}~RDM kernel CKA yields Trained $\\approx$ Proj ($\\Delta{=}0.003$) $>$ Untrained $>$ DINOv2. \\textbf{(b)}~Linear CKA~\\cite{kornblith2019} partially reverses the ordering (Untrained $>$ Trained $>$ Proj), illustrating that metric choice affects conclusions about representation similarity.}\n\\label{fig:metric_comparison}\n\\end{figure}\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 17_

experiments.tex 已全量重写。主要变更：

- **§4.1**: 新增 source (f) branch-split，其余保持简洁
- **§4.2**: DINO cls_token 0.692 领先；新增 branch-split 段落（DINOv2=0.619 ≈ SigLIP=0.621，fusion=0.634 > 两者，projector 压缩 0.634→0.615）；CKA 反转讨论保留
- **§4.3**: 标题改为 "Non-Monotonic LLM Transformation"；核心叙事：inverted-U（L0=0.612→L12=0.628 peak ABOVE projector 0.615→L32=0.422）；RSA-CKA dissociation；readout concentration 保留
- **§4.4**: 标题改为 "Training Redistributes, Does Not Create"；best-vs-best Δ=+0.017 n.s.；same-layer L12 Δ=+0.079 p<0.0001；instruction invariance |Δ|<0.006

所有 \label 与旧版一致，数字均来自权威数据表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "uuid": "8547326a-1393-4162-940f-615a97e4f5ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Y3bXKH79VXkPz9eKjCNhC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5603,
      "cache_read_input_tokens": 39262,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5603
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

_source line 18_

experiments.tex 已全量重写。主要变更：

- **§4.1**: 新增 source (f) branch-split，其余保持简洁
- **§4.2**: DINO cls_token 0.692 领先；新增 branch-split 段落（DINOv2=0.619 ≈ SigLIP=0.621，fusion=0.634 > 两者，projector 压缩 0.634→0.615）；CKA 反转讨论保留
- **§4.3**: 标题改为 "Non-Monotonic LLM Transformation"；核心叙事：inverted-U（L0=0.612→L12=0.628 peak ABOVE projector 0.615→L32=0.422）；RSA-CKA dissociation；readout concentration 保留
- **§4.4**: 标题改为 "Training Redistributes, Does Not Create"；best-vs-best Δ=+0.017 n.s.；same-layer L12 Δ=+0.079 p<0.0001；instruction invariance |Δ|<0.006

所有 \label 与旧版一致，数字均来自权威数据表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 126617,
  "duration_api_ms": 127531,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "75b8212d-4ada-4661-a1d1-c2df2b2dbebe",
  "total_cost_usd": 0.42088050000000005,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 33024,
    "cache_read_input_tokens": 110589,
    "output_tokens": 6230,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 33024,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 327,
        "cache_read_input_tokens": 39262,
        "cache_creation_input_tokens": 5603,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5603
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3311,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003411,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 6230,
      "cacheReadInputTokens": 110589,
      "cacheCreationInputTokens": 33024,
      "webSearchRequests": 0,
      "costUSD": 0.41746950000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fff98142-f4a5-48bf-9271-6f3b6ff94f8e"
}
```

</details>

---
