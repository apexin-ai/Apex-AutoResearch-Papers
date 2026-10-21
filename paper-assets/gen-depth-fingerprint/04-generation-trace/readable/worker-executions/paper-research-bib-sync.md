# paper research bib sync

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 0
- **Tool calls:** 4
- **Original source:** `logs/workers/worker_paper_research_bib_sync_20260515T041855.log`
- **Structured JSON:** [`20a1830c48c2cbf04ff3.json`](../../sessions/20/20a1830c48c2cbf04ff3.json)

## Before a recorded user message

16 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
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
  "uuid": "b19e8251-c6b4-49d7-9ed6-3cdba746ce5a",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/memory/"
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
    "resetsAt": 1778824800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "7e9e285e-26be-4d60-8205-894de00c20a7",
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672"
}
```

---

### Assistant

_source line 4_

Reading the literature map first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "cd14d9e2-d1b8-48f4-9b30-d40ce03cd84d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHUbuEs7NDw29wfWRoT1Fv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12634,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12634
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

<details open><summary>🔧 Tool call — Read · `toolu_018zJgc7SxtVnPtCasyfPjCw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "8573f50a-6202-4118-94ca-fd961314b1d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHUbuEs7NDw29wfWRoT1Fv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12634,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12634
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

_source line 6 · 2026-05-15T04:19:05.307Z_

<details><summary>↩ Tool result · `toolu_018zJgc7SxtVnPtCasyfPjCw`</summary>

```text
1	# Literature Map for gen-depth-fingerprint
2	# 递归 LLM 生成链深度指纹识别
3	# Updated: 2026-05-15
4	# Categories: detection, model-collapse, data-quality, stylometry,
5	#             iterative-generation, watermarking, vocabulary-diversity,
6	#             membership-inference, ood-detection, survey
7	# Total: 39 papers
8	
9	##############################################################################
10	# 1. Perplexity-based / Zero-shot Detection
11	##############################################################################
12	
13	- id: detectgpt
14	  title: "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature"
15	  authors: "Mitchell et al."
16	  year: 2023
17	  venue: "ICML 2023"
18	  arxiv: "2301.11305"
19	  category: detection
20	  role: background
21	  relevance: "基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补"
22	  key_finding: "机器生成文本倾向于占据模型 log-probability 函数的负曲率区域"
23	
24	- id: gltr
25	  title: "GLTR: Statistical Detection and Visualization of Generated Text"
26	  authors: "Gehrmann et al."
27	  year: 2019
28	  venue: "ACL 2019"
29	  arxiv: "1906.04043"
30	  category: detection
31	  role: background
32	  relevance: "早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化"
33	  key_finding: "使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%"
34	
35	- id: dna_gpt
36	  title: "DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text"
37	  authors: "Yang et al."
38	  year: 2024
39	  venue: "ICLR 2024"
40	  arxiv: "2305.17359"
41	  category: detection
42	  role: background
43	  relevance: "通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析"
44	  key_finding: "截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测"
45	
46	- id: binoculars
47	  title: "Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text"
48	  authors: "Hans et al."
49	  year: 2024
50	  venue: "ICML 2024"
51	  arxiv: "2401.12070"
52	  category: detection
53	  role: background
54	  relevance: "双模型对比打分检测法；depth fingerprint 需要验证与 Binoculars score 在不同深度下的相关性"
55	  key_finding: "对比两个近似 LLM 的 perplexity 比值可在 0.01% FPR 下检测 90%+ 的 ChatGPT 输出"
56	
57	- id: fast_detectgpt
58	  title: "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature"
59	  authors: "Bao et al."
60	  year: 2024
61	  venue: "ICLR 2024"
62	  arxiv: "2310.05130"
63	  category: detection
64	  role: background
65	  relevance: "DetectGPT 加速版，用采样替代扰动；可作为 depth fingerprint pipeline 中的快速 baseline"
66	  key_finding: "用条件概率曲率替代扰动步骤，检测速度提升 340 倍，性能相对提升 75%"
67	
68	- id: ld_score
69	  title: "Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection"
70	  authors: "Narayanasamy et al."
71	  year: 2026
72	  venue: "arXiv preprint"
73	  arxiv: "2605.01647"
74	  category: detection
75	  role: method-component
76	  relevance: "字符级分布特征 (LD-Score) 与 perplexity 正交（r=0.08-0.13）；可作为 depth fingerprint 的互补信号"
77	  key_finding: "LLM 近似全局字符分布而人类展示领域特化分布，形成可检测的 Wall of Separation"
78	
79	- id: intrinsic_dimension
80	  title: "Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts"
81	  authors: "Tulchinskii et al."
82	  year: 2023
83	  venue: "NeurIPS 2023"
84	  arxiv: "2306.04723"
85	  category: detection
86	  role: method-component
87	  relevance: "用嵌入空间内在维度做检测；depth fingerprint 可探索内在维度随生成深度的变化趋势"
88	  key_finding: "人类文本嵌入的内在维度约 9（字母语言），AI 文本约低 1.5；跨域/跨模型稳定"
89	
90	- id: diveye
91	  title: "Diversity Boosts AI-Generated Text Detection"
92	  authors: "Basani & Chen"
93	  year: 2026
94	  venue: "TMLR 2026"
95	  arxiv: "2509.18880"
96	  category: detection
97	  role: method-component
98	  relevance: "用 surprisal diversity 特征检测 AI 文本——人类文本 surprisal 分布离散度更高、尾部更重；与本项目 shape 特征（entropy_std, tail_decay）直接可比"
99	  key_finding: "DivEye 框架捕捉 token surprisal 的波动模式，zero-shot 检测超现有方法最多 33.2%，对改写鲁棒"
100	
101	- id: generator_barrier
102	  title: "Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection"
103	  authors: "Pu et al."
104	  year: 2026
105	  venue: "arXiv preprint"
106	  arxiv: "2604.13692"
107	  category: detection
108	  role: background
109	  relevance: "通过解耦表征实现跨生成器泛化检测（MAGE 20 个 LLM），与本项目 LOGO 跨生成器评估目标一致；不同方法论（表征学习 vs 特征工程）"
110	  key_finding: "解耦 AI 检测语义与生成器特有伪影，在未见生成器上准确率提升 24.2%、F1 提升 26.2%"
111	
112	- id: feat_aug_transformer
113	  title: "Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators"
114	  authors: "Mady et al."
115	  year: 2026
116	  venue: "arXiv preprint"
117	  arxiv: "2605.03969"
118	  category: detection
119	  role: background
120	  relevance: "语言特征增强 Transformer 做跨域/跨生成器检测（DeBERTa+FeatAttn 85.9% bal-acc on M4）；验证了语言特征对泛化性的价值，支撑本项目特征工程路线"
121	  key_finding: "基模型域内近满分但迁移脆弱；attention-based 语言特征融合显著提升跨分布迁移能力"
122	
123	##############################################################################
124	# 2. Model Collapse Theory
125	##############################################################################
126	
127	- id: self_consuming_mad
128	  title: "Self-Consuming Generative Models Go MAD"
129	  authors: "Alemohammad et al."
130	  year: 2023
131	  venue: "arXiv preprint"
132	  arxiv: "2307.01850"
133	  category: model-collapse
134	  role: background
135	  relevance: "定义 autophagous loop 三种模式并证明精度/多样性递减；本项目的 depth fingerprint 可量化此递减"
136	  key_finding: "无足够新鲜真实数据时，自噬循环导致生成质量（精度）或多样性（召回）逐步下降"
137	
138	- id: curse_of_recursion
139	  title: "The Curse of Recursion: Training on Generated Data Makes Models Forget"
140	  authors: "Shumailov et al."
141	  year: 2024
142	  venue: "Nature 2024"
143	  arxiv: "2305.17493"
144	  category: model-collapse
145	  role: background
146	  relevance: "Nature 发表的 model collapse 里程碑论文；本项目关注推理链（非训练循环）的类似退化现象"
147	  key_finding: "递归训练导致不可逆缺陷——原始分布的尾部消失，在 VAE/GMM/LLM 中普遍存在"
148	
149	- id: strong_model_collapse
150	  title: "Strong Model Collapse"
151	  authors: "Dohmatob et al."
152	  year: 2024
153	  venue: "ICLR 2025"
154	  arxiv: "2410.04840"
155	  category: model-collapse
156	  role: background
157	  relevance: "证明即使 1% 合成数据也会导致 collapse，更大模型可能放大效应；支撑 depth fingerprint 的理论动机"
158	  key_finding: "最小比例合成数据即可导致 strong collapse；更大模型在简化体制下可放大此效应"
159	
160	- id: model_collapse_avoidable
161	  title: "Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data"
162	  authors: "Gerstgrasser et al."
163	  year: 2024
164	  venue: "arXiv preprint"
165	  arxiv: "2404.01413"
166	  category: model-collapse
167	  role: background
168	  relevance: "证明累积数据时 collapse 可避免；本项目的生成链场景是纯推理无累积，collapse 更难避免"
169	  key_finding: "当数据累积而非替换时，混合真实与合成数据可避免 model collapse"
170	
171	##############################################################################
172	# 3. OOD Detection
173	##############################################################################
174	
175	- id: ood_baseline
176	  title: "A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks"
177	  authors: "Hendrycks & Gimpel"
178	  year: 2017
179	  venue: "ICLR 2017"
180	  arxiv: "1610.02136"
181	  category: ood-detection
182	  role: background
183	  relevance: "OOD 检测基线方法；depth fingerprint 可视为 OOD scoring 的一种特殊形式——检测偏离人类分布的程度"
184	  key_finding: "正确分类样本的最大 softmax 概率高于错误分类和 OOD 样本"
185	
186	##############################################################################
187	# 4. Data Quality Scoring
188	##############################################################################
189	
190	- id: dsir
191	  title: "Data Selection for Language Models via Importance Resampling"
192	  authors: "Xie et al."
193	  year: 2023
194	  venue: "NeurIPS 2023"
195	  arxiv: "2302.03169"
196	  category: data-quality
197	  role: background
198	  relevance: "数据质量筛选框架；depth fingerprint 可作为 DSIR 类 pipeline 中合成数据污染度的质量信号"
199	  key_finding: "用 n-gram 特征空间的重要性权重做数据选择，100M 文档 4.5 小时处理"
200	
201	- id: qurating
202	  title: "QuRating: Selecting High-Quality Data for Training Language Models"
203	  authors: "Wettig et al."
204	  year: 2024
205	  venue: "ICML 2024"
206	  arxiv: "2402.09739"
207	  category: data-quality
208	  role: background
209	  relevance: "LLM 成对判断的数据质量评分；depth fingerprint 类似地为文本分配生成深度分数"
210	  key_finding: "LLM 可准确判断文本的写作风格/专业性/教育价值等质量维度，用于预训练数据选择"
211	
212	- id: ccnet
213	  title: "CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data"
214	  authors: "Wenzek et al."
215	  year: 2020
216	  venue: "LREC 2020"
217	  arxiv: "1911.00359"
218	  category: data-quality
219	  role: background
220	  relevance: "基于 perplexity 的 web 数据过滤 pipeline；depth fingerprint 可集成为额外的质量过滤维度"
221	  key_finding: "用语言模型 perplexity 过滤 Common Crawl 数据，接近维基百科质量水平"
222	
223	##############################################################################
224	# 5. Watermarking
225	##############################################################################
226	
227	- id: watermark_llm
228	  title: "A Watermark for Large Language Models"
229	  authors: "Kirchenbauer et al."
230	  year: 2023
231	  venue: "ICML 2023"
232	  arxiv: "2301.10226"
233	  category: watermarking
234	  role: background
235	  relevance: "绿色 token 列表 watermark 方案；depth fingerprint 检测非水印场景下的生成痕迹，形成互补"
236	  key_finding: "通过在采样前划分 green/red token 列表实现不可见水印，短文本即可检测"
237	
238	- id: synthid_text
239	  title: "Scalable Watermarking for Identifying Large Language Model Outputs"
240	  authors: "Dathathri et al."
241	  year: 2024
242	  venue: "Nature 2024"
243	  arxiv: ""
244	  category: watermarking
245	  role: background
246	  relevance: "生产级 LLM 水印方案（Google Gemini 部署）；depth fingerprint 面向无水印的 post-hoc 检测"
247	  key_finding: "Tournament Sampling 算法实现生产级文本水印，Google Gemini 实际部署"
248	
249	- id: aaronson_watermark
250	  title: "Watermarking GPT Outputs"
251	  authors: "Aaronson & Kirchner"
252	  year: 2022
253	  venue: "Technical Talk"
254	  arxiv: ""
255	  category: watermarking
256	  role: background
257	  relevance: "LLM 文本水印的原始提案；depth fingerprint 定位为不依赖水印的被动检测方案"
258	  key_finding: "用伪随机函数选择 next token，对短文本即可检测，对轻微编辑鲁棒"
259	
260	- id: chainwash
261	  title: "Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks"
262	  authors: "Ameen et al."
263	  year: 2026
264	  venue: "arXiv preprint"
265	  arxiv: "2605.05503"
266	  category: watermarking
267	  role: background
268	  relevance: "多步重写链攻击水印（5 hop 后检测率从 87.9% 降到 4.86%）；证明生成链深度影响水印信号，支撑 depth fingerprint 的动机——被动检测不依赖水印"
269	  key_finding: "链式重写（chainwash）通过生成式多步改写有效消除扩散语言模型水印，5 步后 94.76% 原可检测文本不再被标记"
270	
271	##############################################################################
272	# 6. Vocabulary Diversity
273	##############################################################################
274	
275	- id: curious_decline
276	  title: "The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text"
277	  authors: "Guo et al."
278	  year: 2024
279	  venue: "NAACL 2024 Findings"
280	  arxiv: "2311.09807"
281	  category: vocabulary-diversity
282	  role: direct-competitor
283	  relevance: "直接相关：量化递归微调导致的词汇/句法/语义多样性下降；本项目扩展到推理链场景"
284	  key_finding: "递归微调导致词汇/句法/语义多样性持续下降，创意任务尤为显著"
285	
286	- id: writing_diversity
287	  title: "Does Writing with Language Models Reduce Content Diversity?"
288	  authors: "Padmakumar & He"
289	  year: 2024
290	  venue: "ICLR 2024"
291	  arxiv: "2309.05196"
292	  category: vocabulary-diversity
293	  role: background
294	  relevance: "实验证明 InstructGPT 协写降低多样性；支撑 depth fingerprint 中 diversity 随深度递减的假设"
295	  key_finding: "InstructGPT 协写显著降低不同作者间的文本相似度和词汇多样性"
296	
297	- id: nucleus_sampling
298	  title: "The Curious Case of Neural Text Degeneration"
299	  authors: "Holtzman et al."
300	  year: 2020
301	  venue: "ICLR 2020"
302	  arxiv: "1904.09751"
303	  category: vocabulary-diversity
304	  role: background
305	  relevance: "定义了 neural text degeneration 和 nucleus sampling；depth fingerprint 中的 shape 特征与采样策略相关"
306	  key_finding: "最大化解码导致退化；Nucleus Sampling 截断不可靠尾部，生成质量接近人类"
307	
308	- id: mapping_llm_science
309	  title: "Mapping the Increasing Use of LLMs in Scientific Papers"
310	  authors: "Liang et al."
311	  year: 2024
312	  venue: "arXiv preprint"
313	  arxiv: "2404.01268"
314	  category: vocabulary-diversity
315	  role: background
316	  relevance: "大规模量化科学论文中 LLM 修改内容的比例；depth fingerprint 可检测多轮修改的深度"
317	  key_finding: "95 万篇论文分析显示 CS 领域 LLM 修改率最高达 17.5%"
318	
319	- id: monitoring_ai_review
320	  title: "Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews"
321	  authors: "Liang et al."
322	  year: 2024
323	  venue: "ICML 2024"
324	  arxiv: "2403.07183"
325	  category: vocabulary-diversity
326	  role: background
327	  relevance: "检测同行评审中 LLM 修改内容；depth fingerprint 提供互补的深度维度信号"
328	  key_finding: "6.5-16.9% 的 AI 会议 peer review 可能被 LLM 实质性修改"
329	
330	##############################################################################
331	# 7. Stylometry / Authorship Attribution
332	##############################################################################
333	
334	- id: stamatatos_survey
335	  title: "A Survey of Modern Authorship Attribution Methods"
336	  authors: "Stamatatos"
337	  year: 2009
338	  venue: "JASIST 2009"
339	  arxiv: ""
340	  category: stylometry
341	  role: background
342	  relevance: "风格计量学经典综述；depth fingerprint 的特征工程可借鉴 stylometric 特征体系"
343	  key_finding: "综述词汇/字符/句法等多层次文体特征在作者归属中的应用"
344	
345	- id: koppel_authorship
346	  title: "Computational Methods in Authorship Attribution"
347	  authors: "Koppel et al."
348	  year: 2009
349	  venue: "JASIST 2009"
350	  arxiv: ""
351	  category: stylometry
352	  role: background
353	  relevance: "开放集作者归属方法；depth fingerprint 可视为 LLM 生成深度的归属问题"
354	  key_finding: "解决大规模候选集和开放集场景下的作者归属问题"
355	
356	- id: uchendu_attribution
357	  title: "Authorship Attribution for Neural Text Generation"
358	  authors: "Uchendu et al."
359	  year: 2020
360	  venue: "EMNLP 2020"
361	  arxiv: ""
362	  category: stylometry
363	  role: background
364	  relevance: "将作者归属扩展到 neural text 生成源识别；depth fingerprint 进一步细化到生成深度维度"
365	  key_finding: "可区分不同神经文本生成器的多类归属，超越二分类人/机检测"
366	
367	##############################################################################
368	# 8. Iterative Generation
369	##############################################################################
370	
371	- id: broken_telephone
372	  title: "LLM as a Broken Telephone: Iterative Generation Distorts Information"
373	  authors: "Mohamed et al."
374	  year: 2025
375	  venue: "ACL 2025"
376	  arxiv: "2502.20258"
377	  category: iterative-generation
378	  role: direct-competitor
379	  relevance: "最直接相关：通过翻译链研究 LLM 迭代生成的信息失真；本项目扩展到非改写式生成链"
380	  key_finding: "LLM 迭代翻译链中失真随深度累积，语言相似度和提示策略影响退化速率"
381	
382	- id: markovian_chains
383	  title: "Markovian Generation Chains in Large Language Models"
384	  authors: "Geng et al."
385	  year: 2026
386	  venue: "arXiv preprint"
387	  arxiv: "2603.11228"
388	  category: iterative-generation
389	  role: direct-competitor
390	  relevance: "定义 Markovian generation chains 并研究收敛/发散行为；本项目关注非改写链的 depth fingerprint"
391	  key_finding: "迭代重述/翻译中输出或收敛到小循环集，或继续产生新句子，取决于温度和初始输入"
392	
393	##############################################################################
394	# 9. Membership Inference
395	##############################################################################
396	
397	- id: min_k_percent
398	  title: "Detecting Pretraining Data from Large Language Models"
399	  authors: "Shi et al."
400	  year: 2024
401	  venue: "ICLR 2024"
402	  arxiv: "2310.16789"
403	  category: membership-inference
404	  role: method-component
405	  relevance: "Min-K% 用最低概率 token 做成员推断；depth fingerprint 可借鉴其概率分布分析思路"
406	  key_finding: "未见过的文本更可能包含低概率离群 token；Min-K% Prob 在 WikiMIA 上提升 7.4%"
407	
408	##############################################################################
409	# 10. Robustness / Adversarial / Theoretical
410	##############################################################################
411	
412	- id: reliable_detection
413	  title: "Can AI-Generated Text be Reliably Detected?"
414	  authors: "Sadasivan et al."
415	  year: 2024
416	  venue: "ICLR 2024"
417	  arxiv: "2303.11156"
418	  category: detection
419	  role: background
420	  relevance: "递归改写攻击显著降低检测率；depth fingerprint 面向非改写链，攻击面不同"
421	  key_finding: "递归改写可将 DetectGPT 从 70.3% 降到 4.6%；检测上界与分布 TV 距离相关"
422	
423	- id: paraphrase_evades
424	  title: "Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense"
425	  authors: "Krishna et al."
426	  year: 2023
427	  venue: "NeurIPS 2023"
428	  arxiv: "2303.13408"
429	  category: detection
430	  role: background
431	  relevance: "改写攻击 vs 检索防御；depth fingerprint 检测非改写链，与此正交但需考虑改写鲁棒性"
432	  key_finding: "DIPPER 改写器将 DetectGPT 准确率从 70.3% 降到 4.6%；检索方法是有效防御"
433	
434	- id: detection_possibilities
435	  title: "Position: On the Possibilities of AI-Generated Text Detection"
436	  authors: "Chakraborty et al."
437	  year: 2024
438	  venue: "ICML 2024"
439	  arxiv: "2304.04736"
440	  category: detection
441	  role: background
442	  relevance: "理论证明 AI 文本检测在分布可区分时始终可行；支撑 depth fingerprint 的可行性"
443	  key_finding: "信息论证明：除非人/机分布完全不可分，检测始终可行；给出样本复杂度下界"
444	
445	##############################################################################
446	# 11. Surveys / Early Detection
447	##############################################################################
448	
449	- id: jawahar_survey
450	  title: "Automatic Detection of Machine Generated Text: A Critical Survey"
451	  authors: "Jawahar et al."
452	  year: 2020
453	  venue: "COLING 2020"
454	  arxiv: "2011.01314"
455	  category: survey
456	  role: background
457	  relevance: "机器文本检测早期综述；depth fingerprint 定位在该领域的新维度"
458	  key_finding: "系统梳理统计方法和神经方法在机器文本检测中的应用与局限"
459	
460	- id: grover
461	  title: "Defending Against Neural Fake News"
462	  authors: "Zellers et al."
463	  year: 2019
464	  venue: "NeurIPS 2019"
465	  arxiv: "1905.12616"
466	  category: detection
467	  role: background
468	  relevance: "生成器即最佳检测器的早期发现；depth fingerprint 不依赖生成器 access"
469	  key_finding: "Grover 自身是检测 Grover 生成假新闻的最佳检测器（92% vs 73% baseline）"
470	
471	- id: release_strategies
472	  title: "Release Strategies and the Social Impacts of Language Models"
473	  authors: "Solaiman et al."
474	  year: 2019
475	  venue: "arXiv preprint"
476	  arxiv: "1908.09203"
477	  category: detection
478	  role: background
479	  relevance: "GPT-2 分阶段发布策略和检测工具；depth fingerprint 面向更复杂的生成链场景"
480	  key_finding: "分阶段发布 GPT-2 允许在模型升级间进行风险/收益分析和检测器开发"
481	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "0a686c2c-8867-4af8-89d1-509aceaf4ad8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/literature_map.yaml",
      "content": "# Literature Map for gen-depth-fingerprint\n# 递归 LLM 生成链深度指纹识别\n# Updated: 2026-05-15\n# Categories: detection, model-collapse, data-quality, stylometry,\n#             iterative-generation, watermarking, vocabulary-diversity,\n#             membership-inference, ood-detection, survey\n# Total: 39 papers\n\n##############################################################################\n# 1. Perplexity-based / Zero-shot Detection\n##############################################################################\n\n- id: detectgpt\n  title: \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\"\n  authors: \"Mitchell et al.\"\n  year: 2023\n  venue: \"ICML 2023\"\n  arxiv: \"2301.11305\"\n  category: detection\n  role: background\n  relevance: \"基础检测方法，用 log-probability curvature 区分人/机文本；本项目的 depth fingerprint 可与之互补\"\n  key_finding: \"机器生成文本倾向于占据模型 log-probability 函数的负曲率区域\"\n\n- id: gltr\n  title: \"GLTR: Statistical Detection and Visualization of Generated Text\"\n  authors: \"Gehrmann et al.\"\n  year: 2019\n  venue: \"ACL 2019\"\n  arxiv: \"1906.04043\"\n  category: detection\n  role: background\n  relevance: \"早期统计检测工具，使用 token rank/entropy 等特征；本项目可对比其特征在不同生成深度下的变化\"\n  key_finding: \"使用 token 概率排名和熵的可视化方案将人类检测准确率从 54% 提升到 72%\"\n\n- id: dna_gpt\n  title: \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\"\n  authors: \"Yang et al.\"\n  year: 2024\n  venue: \"ICLR 2024\"\n  arxiv: \"2305.17359\"\n  category: detection\n  role: background\n  relevance: \"通过 n-gram 发散度做 zero-shot 检测；本项目 depth fingerprint 中的 diversity 指标可借鉴其 n-gram 分析\"\n  key_finding: \"截断文本后让 LLM 重新生成，通过 n-gram 差异实现零样本检测\"\n\n- id: binoculars\n  title: \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\"\n  authors: \"Hans et al.\"\n  year: 2024\n  venue: \"ICML 2024\"\n  arxiv: \"2401.12070\"\n  category: detection\n  role: background\n  relevance: \"双模型对比打分检测法；depth fingerprint 需要验证与 Binoculars score 在不同深度下的相关性\"\n  key_finding: \"对比两个近似 LLM 的 perplexity 比值可在 0.01% FPR 下检测 90%+ 的 ChatGPT 输出\"\n\n- id: fast_detectgpt\n  title: \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\"\n  authors: \"Bao et al.\"\n  year: 2024\n  venue: \"ICLR 2024\"\n  arxiv: \"2310.05130\"\n  category: detection\n  role: background\n  relevance: \"DetectGPT 加速版，用采样替代扰动；可作为 depth fingerprint pipeline 中的快速 baseline\"\n  key_finding: \"用条件概率曲率替代扰动步骤，检测速度提升 340 倍，性能相对提升 75%\"\n\n- id: ld_score\n  title: \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\"\n  authors: \"Narayanasamy et al.\"\n  year: 2026\n  venue: \"arXiv preprint\"\n  arxiv: \"2605.01647\"\n  category: detection\n  role: method-component\n  relevance: \"字符级分布特征 (LD-Score) 与 perplexity 正交（r=0.08-0.13）；可作为 depth fingerprint 的互补信号\"\n  key_finding: \"LLM 近似全局字符分布而人类展示领域特化分布，形成可检测的 Wall of Separation\"\n\n- id: intrinsic_dimension\n  title: \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\"\n  authors: \"Tulchinskii et al.\"\n  year: 2023\n  venue: \"NeurIPS 2023\"\n  arxiv: \"2306.04723\"\n  category: detection\n  role: method-component\n  relevance: \"用嵌入空间内在维度做检测；depth fingerprint 可探索内在维度随生成深度的变化趋势\"\n  key_finding: \"人类文本嵌入的内在维度约 9（字母语言），AI 文本约低 1.5；跨域/跨模型稳定\"\n\n- id: diveye\n  title: \"Diversity Boosts AI-Generated Text Detection\"\n  authors: \"Basani & Chen\"\n  year: 2026\n  venue: \"TMLR 2026\"\n  arxiv: \"2509.18880\"\n  category: detection\n  role: method-component\n  relevance: \"用 surprisal diversity 特征检测 AI 文本——人类文本 surprisal 分布离散度更高、尾部更重；与本项目 shape 特征（entropy_std, tail_decay）直接可比\"\n  key_finding: \"DivEye 框架捕捉 token surprisal 的波动模式，zero-shot 检测超现有方法最多 33.2%，对改写鲁棒\"\n\n- id: generator_barrier\n  title: \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\"\n  authors: \"Pu et al.\"\n  year: 2026\n  venue: \"arXiv preprint\"\n  arxiv: \"2604.13692\"\n  category: detection\n  role: background\n  relevance: \"通过解耦表征实现跨生成器泛化检测（MAGE 20 个 LLM），与本项目 LOGO 跨生成器评估目标一致；不同方法论（表征学习 vs 特征工程）\"\n  key_finding: \"解耦 AI 检测语义与生成器特有伪影，在未见生成器上准确率提升 24.2%、F1 提升 26.2%\"\n\n- id: feat_aug_transformer\n  title: \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\"\n  authors: \"Mady et al.\"\n  year: 2026\n  venue: \"arXiv preprint\"\n  arxiv: \"2605.03969\"\n  category: detection\n  role: background\n  relevance: \"语言特征增强 Transformer 做跨域/跨生成器检测（DeBERTa+FeatAttn 85.9% bal-acc on M4）；验证了语言特征对泛化性的价值，支撑本项目特征工程路线\"\n  key_finding: \"基模型域内近满分但迁移脆弱；attention-based 语言特征融合显著提升跨分布迁移能力\"\n\n##############################################################################\n# 2. Model Collapse Theory\n##############################################################################\n\n- id: self_consuming_mad\n  title: \"Self-Consuming Generative Models Go MAD\"\n  authors: \"Alemohammad et al.\"\n  year: 2023\n  venue: \"arXiv preprint\"\n  arxiv: \"2307.01850\"\n  category: model-collapse\n  role: background\n  relevance: \"定义 autophagous loop 三种模式并证明精度/多样性递减；本项目的 depth fingerprint 可量化此递减\"\n  key_finding: \"无足够新鲜真实数据时，自噬循环导致生成质量（精度）或多样性（召回）逐步下降\"\n\n- id: curse_of_recursion\n  title: \"The Curse of Recursion: Training on Generated Data Makes Models Forget\"\n  authors: \"Shumailov et al.\"\n  year: 2024\n  venue: \"Nature 2024\"\n  arxiv: \"2305.17493\"\n  category: model-collapse\n  role: background\n  relevance: \"Nature 发表的 model collapse 里程碑论文；本项目关注推理链（非训练循环）的类似退化现象\"\n  key_finding: \"递归训练导致不可逆缺陷——原始分布的尾部消失，在 VAE/GMM/LLM 中普遍存在\"\n\n- id: strong_model_collapse\n  title: \"Strong Model Collapse\"\n  authors: \"Dohmatob et al.\"\n  year: 2024\n  venue: \"ICLR 2025\"\n  arxiv: \"2410.04840\"\n  category: model-collapse\n  role: background\n  relevance: \"证明即使 1% 合成数据也会导致 collapse，更大模型可能放大效应；支撑 depth fingerprint 的理论动机\"\n  key_finding: \"最小比例合成数据即可导致 strong collapse；更大模型在简化体制下可放大此效应\"\n\n- id: model_collapse_avoidable\n  title: \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\"\n  authors: \"Gerstgrasser et al.\"\n  year: 2024\n  venue: \"arXiv preprint\"\n  arxiv: \"2404.01413\"\n  category: model-collapse\n  role: background\n  relevance: \"证明累积数据时 collapse 可避免；本项目的生成链场景是纯推理无累积，collapse 更难避免\"\n  key_finding: \"当数据累积而非替换时，混合真实与合成数据可避免 model collapse\"\n\n##############################################################################\n# 3. OOD Detection\n##############################################################################\n\n- id: ood_baseline\n  title: \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\"\n  authors: \"Hendrycks & Gimpel\"\n  year: 2017\n  venue: \"ICLR 2017\"\n  arxiv: \"1610.02136\"\n  category: ood-detection\n  role: background\n  relevance: \"OOD 检测基线方法；depth fingerprint 可视为 OOD scoring 的一种特殊形式——检测偏离人类分布的程度\"\n  key_finding: \"正确分类样本的最大 softmax 概率高于错误分类和 OOD 样本\"\n\n##############################################################################\n# 4. Data Quality Scoring\n##############################################################################\n\n- id: dsir\n  title: \"Data Selection for Language Models via Importance Resampling\"\n  authors: \"Xie et al.\"\n  year: 2023\n  venue: \"NeurIPS 2023\"\n  arxiv: \"2302.03169\"\n  category: data-quality\n  role: background\n  relevance: \"数据质量筛选框架；depth fingerprint 可作为 DSIR 类 pipeline 中合成数据污染度的质量信号\"\n  key_finding: \"用 n-gram 特征空间的重要性权重做数据选择，100M 文档 4.5 小时处理\"\n\n- id: qurating\n  title: \"QuRating: Selecting High-Quality Data for Training Language Models\"\n  authors: \"Wettig et al.\"\n  year: 2024\n  venue: \"ICML 2024\"\n  arxiv: \"2402.09739\"\n  category: data-quality\n  role: background\n  relevance: \"LLM 成对判断的数据质量评分；depth fingerprint 类似地为文本分配生成深度分数\"\n  key_finding: \"LLM 可准确判断文本的写作风格/专业性/教育价值等质量维度，用于预训练数据选择\"\n\n- id: ccnet\n  title: \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\"\n  authors: \"Wenzek et al.\"\n  year: 2020\n  venue: \"LREC 2020\"\n  arxiv: \"1911.00359\"\n  category: data-quality\n  role: background\n  relevance: \"基于 perplexity 的 web 数据过滤 pipeline；depth fingerprint 可集成为额外的质量过滤维度\"\n  key_finding: \"用语言模型 perplexity 过滤 Common Crawl 数据，接近维基百科质量水平\"\n\n##############################################################################\n# 5. Watermarking\n##############################################################################\n\n- id: watermark_llm\n  title: \"A Watermark for Large Language Models\"\n  authors: \"Kirchenbauer et al.\"\n  year: 2023\n  venue: \"ICML 2023\"\n  arxiv: \"2301.10226\"\n  category: watermarking\n  role: background\n  relevance: \"绿色 token 列表 watermark 方案；depth fingerprint 检测非水印场景下的生成痕迹，形成互补\"\n  key_finding: \"通过在采样前划分 green/red token 列表实现不可见水印，短文本即可检测\"\n\n- id: synthid_text\n  title: \"Scalable Watermarking for Identifying Large Language Model Outputs\"\n  authors: \"Dathathri et al.\"\n  year: 2024\n  venue: \"Nature 2024\"\n  arxiv: \"\"\n  category: watermarking\n  role: background\n  relevance: \"生产级 LLM 水印方案（Google Gemini 部署）；depth fingerprint 面向无水印的 post-hoc 检测\"\n  key_finding: \"Tournament Sampling 算法实现生产级文本水印，Google Gemini 实际部署\"\n\n- id: aaronson_watermark\n  title: \"Watermarking GPT Outputs\"\n  authors: \"Aaronson & Kirchner\"\n  year: 2022\n  venue: \"Technical Talk\"\n  arxiv: \"\"\n  category: watermarking\n  role: background\n  relevance: \"LLM 文本水印的原始提案；depth fingerprint 定位为不依赖水印的被动检测方案\"\n  key_finding: \"用伪随机函数选择 next token，对短文本即可检测，对轻微编辑鲁棒\"\n\n- id: chainwash\n  title: \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\"\n  authors: \"Ameen et al.\"\n  year: 2026\n  venue: \"arXiv preprint\"\n  arxiv: \"2605.05503\"\n  category: watermarking\n  role: background\n  relevance: \"多步重写链攻击水印（5 hop 后检测率从 87.9% 降到 4.86%）；证明生成链深度影响水印信号，支撑 depth fingerprint 的动机——被动检测不依赖水印\"\n  key_finding: \"链式重写（chainwash）通过生成式多步改写有效消除扩散语言模型水印，5 步后 94.76% 原可检测文本不再被标记\"\n\n##############################################################################\n# 6. Vocabulary Diversity\n##############################################################################\n\n- id: curious_decline\n  title: \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\"\n  authors: \"Guo et al.\"\n  year: 2024\n  venue: \"NAACL 2024 Findings\"\n  arxiv: \"2311.09807\"\n  category: vocabulary-diversity\n  role: direct-competitor\n  relevance: \"直接相关：量化递归微调导致的词汇/句法/语义多样性下降；本项目扩展到推理链场景\"\n  key_finding: \"递归微调导致词汇/句法/语义多样性持续下降，创意任务尤为显著\"\n\n- id: writing_diversity\n  title: \"Does Writing with Language Models Reduce Content Diversity?\"\n  authors: \"Padmakumar & He\"\n  year: 2024\n  venue: \"ICLR 2024\"\n  arxiv: \"2309.05196\"\n  category: vocabulary-diversity\n  role: background\n  relevance: \"实验证明 InstructGPT 协写降低多样性；支撑 depth fingerprint 中 diversity 随深度递减的假设\"\n  key_finding: \"InstructGPT 协写显著降低不同作者间的文本相似度和词汇多样性\"\n\n- id: nucleus_sampling\n  title: \"The Curious Case of Neural Text Degeneration\"\n  authors: \"Holtzman et al.\"\n  year: 2020\n  venue: \"ICLR 2020\"\n  arxiv: \"1904.09751\"\n  category: vocabulary-diversity\n  role: background\n  relevance: \"定义了 neural text degeneration 和 nucleus sampling；depth fingerprint 中的 shape 特征与采样策略相关\"\n  key_finding: \"最大化解码导致退化；Nucleus Sampling 截断不可靠尾部，生成质量接近人类\"\n\n- id: mapping_llm_science\n  title: \"Mapping the Increasing Use of LLMs in Scientific Papers\"\n  authors: \"Liang et al.\"\n  year: 2024\n  venue: \"arXiv preprint\"\n  arxiv: \"2404.01268\"\n  category: vocabulary-diversity\n  role: background\n  relevance: \"大规模量化科学论文中 LLM 修改内容的比例；depth fingerprint 可检测多轮修改的深度\"\n  key_finding: \"95 万篇论文分析显示 CS 领域 LLM 修改率最高达 17.5%\"\n\n- id: monitoring_ai_review\n  title: \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\"\n  authors: \"Liang et al.\"\n  year: 2024\n  venue: \"ICML 2024\"\n  arxiv: \"2403.07183\"\n  category: vocabulary-diversity\n  role: background\n  relevance: \"检测同行评审中 LLM 修改内容；depth fingerprint 提供互补的深度维度信号\"\n  key_finding: \"6.5-16.9% 的 AI 会议 peer review 可能被 LLM 实质性修改\"\n\n##############################################################################\n# 7. Stylometry / Authorship Attribution\n##############################################################################\n\n- id: stamatatos_survey\n  title: \"A Survey of Modern Authorship Attribution Methods\"\n  authors: \"Stamatatos\"\n  year: 2009\n  venue: \"JASIST 2009\"\n  arxiv: \"\"\n  category: stylometry\n  role: background\n  relevance: \"风格计量学经典综述；depth fingerprint 的特征工程可借鉴 stylometric 特征体系\"\n  key_finding: \"综述词汇/字符/句法等多层次文体特征在作者归属中的应用\"\n\n- id: koppel_authorship\n  title: \"Computational Methods in Authorship Attribution\"\n  authors: \"Koppel et al.\"\n  year: 2009\n  venue: \"JASIST 2009\"\n  arxiv: \"\"\n  category: stylometry\n  role: background\n  relevance: \"开放集作者归属方法；depth fingerprint 可视为 LLM 生成深度的归属问题\"\n  key_finding: \"解决大规模候选集和开放集场景下的作者归属问题\"\n\n- id: uchendu_attribution\n  title: \"Authorship Attribution for Neural Text Generation\"\n  authors: \"Uchendu et al.\"\n  year: 2020\n  venue: \"EMNLP 2020\"\n  arxiv: \"\"\n  category: stylometry\n  role: background\n  relevance: \"将作者归属扩展到 neural text 生成源识别；depth fingerprint 进一步细化到生成深度维度\"\n  key_finding: \"可区分不同神经文本生成器的多类归属，超越二分类人/机检测\"\n\n##############################################################################\n# 8. Iterative Generation\n##############################################################################\n\n- id: broken_telephone\n  title: \"LLM as a Broken Telephone: Iterative Generation Distorts Information\"\n  authors: \"Mohamed et al.\"\n  year: 2025\n  venue: \"ACL 2025\"\n  arxiv: \"2502.20258\"\n  category: iterative-generation\n  role: direct-competitor\n  relevance: \"最直接相关：通过翻译链研究 LLM 迭代生成的信息失真；本项目扩展到非改写式生成链\"\n  key_finding: \"LLM 迭代翻译链中失真随深度累积，语言相似度和提示策略影响退化速率\"\n\n- id: markovian_chains\n  title: \"Markovian Generation Chains in Large Language Models\"\n  authors: \"Geng et al.\"\n  year: 2026\n  venue: \"arXiv preprint\"\n  arxiv: \"2603.11228\"\n  category: iterative-generation\n  role: direct-competitor\n  relevance: \"定义 Markovian generation chains 并研究收敛/发散行为；本项目关注非改写链的 depth fingerprint\"\n  key_finding: \"迭代重述/翻译中输出或收敛到小循环集，或继续产生新句子，取决于温度和初始输入\"\n\n##############################################################################\n# 9. Membership Inference\n##############################################################################\n\n- id: min_k_percent\n  title: \"Detecting Pretraining Data from Large Language Models\"\n  authors: \"Shi et al.\"\n  year: 2024\n  venue: \"ICLR 2024\"\n  arxiv: \"2310.16789\"\n  category: membership-inference\n  role: method-component\n  relevance: \"Min-K% 用最低概率 token 做成员推断；depth fingerprint 可借鉴其概率分布分析思路\"\n  key_finding: \"未见过的文本更可能包含低概率离群 token；Min-K% Prob 在 WikiMIA 上提升 7.4%\"\n\n##############################################################################\n# 10. Robustness / Adversarial / Theoretical\n##############################################################################\n\n- id: reliable_detection\n  title: \"Can AI-Generated Text be Reliably Detected?\"\n  authors: \"Sadasivan et al.\"\n  year: 2024\n  venue: \"ICLR 2024\"\n  arxiv: \"2303.11156\"\n  category: detection\n  role: background\n  relevance: \"递归改写攻击显著降低检测率；depth fingerprint 面向非改写链，攻击面不同\"\n  key_finding: \"递归改写可将 DetectGPT 从 70.3% 降到 4.6%；检测上界与分布 TV 距离相关\"\n\n- id: paraphrase_evades\n  title: \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\"\n  authors: \"Krishna et al.\"\n  year: 2023\n  venue: \"NeurIPS 2023\"\n  arxiv: \"2303.13408\"\n  category: detection\n  role: background\n  relevance: \"改写攻击 vs 检索防御；depth fingerprint 检测非改写链，与此正交但需考虑改写鲁棒性\"\n  key_finding: \"DIPPER 改写器将 DetectGPT 准确率从 70.3% 降到 4.6%；检索方法是有效防御\"\n\n- id: detection_possibilities\n  title: \"Position: On the Possibilities of AI-Generated Text Detection\"\n  authors: \"Chakraborty et al.\"\n  year: 2024\n  venue: \"ICML 2024\"\n  arxiv: \"2304.04736\"\n  category: detection\n  role: background\n  relevance: \"理论证明 AI 文本检测在分布可区分时始终可行；支撑 depth fingerprint 的可行性\"\n  key_finding: \"信息论证明：除非人/机分布完全不可分，检测始终可行；给出样本复杂度下界\"\n\n##############################################################################\n# 11. Surveys / Early Detection\n##############################################################################\n\n- id: jawahar_survey\n  title: \"Automatic Detection of Machine Generated Text: A Critical Survey\"\n  authors: \"Jawahar et al.\"\n  year: 2020\n  venue: \"COLING 2020\"\n  arxiv: \"2011.01314\"\n  category: survey\n  role: background\n  relevance: \"机器文本检测早期综述；depth fingerprint 定位在该领域的新维度\"\n  key_finding: \"系统梳理统计方法和神经方法在机器文本检测中的应用与局限\"\n\n- id: grover\n  title: \"Defending Against Neural Fake News\"\n  authors: \"Zellers et al.\"\n  year: 2019\n  venue: \"NeurIPS 2019\"\n  arxiv: \"1905.12616\"\n  category: detection\n  role: background\n  relevance: \"生成器即最佳检测器的早期发现；depth fingerprint 不依赖生成器 access\"\n  key_finding: \"Grover 自身是检测 Grover 生成假新闻的最佳检测器（92% vs 73% baseline）\"\n\n- id: release_strategies\n  title: \"Release Strategies and the Social Impacts of Language Models\"\n  authors: \"Solaiman et al.\"\n  year: 2019\n  venue: \"arXiv preprint\"\n  arxiv: \"1908.09203\"\n  category: detection\n  role: background\n  relevance: \"GPT-2 分阶段发布策略和检测工具；depth fingerprint 面向更复杂的生成链场景\"\n  key_finding: \"分阶段发布 GPT-2 允许在模型升级间进行风险/收益分析和检测器开发\"\n",
      "numLines": 481,
      "startLine": 1,
      "totalLines": 481
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_011EKoLz6joa9DBu4HER7LGM`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "Check if output directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "f84dcf7a-ce71-49d7-8edf-780554fb7fb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MHUbuEs7NDw29wfWRoT1Fv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12634,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12634
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

_source line 8 · 2026-05-15T04:19:06.253Z_

<details><summary>↩ Tool result · `toolu_011EKoLz6joa9DBu4HER7LGM`</summary>

```text
figures
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "6a48c778-6b5d-45fd-8992-43cd74519570",
  "tool_use_result": {
    "stdout": "figures",
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
Now I have the full literature map. Let me parse all 39 entries and generate the BibTeX file. Let me also create the `docs/paper/` directory if needed.

Let me count the entries:
1. detectgpt
2. gltr
3. dna_gpt
4. binoculars
5. fast_detectgpt
6. ld_score
7. intrinsic_dimension
8. diveye
9. generator_barrier
10. feat_aug_transformer
11. self_consuming_mad


12. curse_of_recursion
13. strong_model_collapse
14. model_collapse_avoidable
15. ood_baseline
16. dsir
17. qurating
18. ccnet
19. watermark_llm
20. synthid_text
21. aaronson_watermark
22. chainwash
23. curious_decline
24. writing_diversity
25. nucleus_sampling
26. mapping_llm_science
27. monitoring_ai_review
28. stamatatos_survey
29. koppel_authorship
30. uchendu_attribution
31. broken_telephone
32. markovian_chains
33. min_k_percent

That's 33 entries so far, and I need to continue through all 39 to complete the bibliography.

34. reliable_detection
35. paraphrase_evades
36. detection_possibilities
37. jawahar_survey
38. grover
39. release_strategies

Now I'm mapping each paper to its publication venue and corresponding BibTeX entry format. Starting with the conference proceedings—detectgpt from ICML 2023, gltr from ACL 2019, dna_gpt from ICLR 2024, binoculars and fast_detectgpt both from ICML and ICLR 2024 respectively—and then handling the arXiv preprints and other sources. Continuing through the bibliography entries, mapping the remaining papers to their appropriate BibTeX types and publication venues—strong_model_collapse goes to ICLR 2025, followed by several more conference proceedings from ICLR, NeurIPS, and ICML, a couple Nature articles, and some arXiv preprints to finish out the list. Continuing through the bibliography entries, I'm cataloging papers on detection evasion techniques, paraphrase attacks, and foundational work on synthetic text detection like GROVER, along with conference venues and their proper citations.

Now I'm working through the BibTeX formatting for author names—converting ampersands to "and" for proper BibTeX syntax, handling "et al." cases as "{LastName and others}", and preserving single author names as-is.

I'm checking the titles for special characters that need escaping, and they all look clean. Now I'll organize the entries by their detection categories and write out the complete BibTeX file. I'm organizing these entries into their respective categories—detection methods, model collapse issues, out-of-distribution detection, data quality approaches, watermarking techniques, vocabulary diversity strategies, stylometry research, iterative generation patterns, membership inference, and survey work. Let me count how many papers fall into each category to get a sense of the distribution.

Now I'm tallying up the entries: that gives me 39 papers total. I need to write out the file content next, making sure to handle the formatting carefully—using double braces to preserve capitalization in titles and escaping any special characters like the percent sign in "Min-K%". Looking through the titles, they appear clean overall without problematic special characters.

I should also remember that BibTeX uses `and` to separate authors, not `&`, so I'll need to convert that when I encounter author names like "Basani & Chen".
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "f57df335-bc1e-4a5c-a710-33c76feaa655",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMNkjVwiaz2sEWkWfKLgVo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8373,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8373
      },
      "output_tokens": 12,
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

Output directory exists. Now generating the BibTeX file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "0ea81ad8-a456-4cdf-a45d-b07d1d5dd3e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMNkjVwiaz2sEWkWfKLgVo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8373,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8373
      },
      "output_tokens": 12,
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

<details open><summary>🔧 Tool call — Write · `toolu_01Ceb49A8HBwPaoPuD8hWfhT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "content": "% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann and others},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy and others},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{intrinsic_dimension,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@article{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani and Chen},\n  journal = {Transactions on Machine Learning Research},\n  year = {2026},\n}\n\n@article{generator_barrier,\n  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  author = {Pu and others},\n  journal = {arXiv preprint arXiv:2604.13692},\n  year = {2026},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady and others},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@inproceedings{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected?}},\n  author = {Sadasivan and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman and others},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n% ===== Model Collapse =====\n\n@article{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad and others},\n  journal = {arXiv preprint arXiv:2307.01850},\n  year = {2023},\n}\n\n@article{curse_of_recursion,\n  title = {{The Curse of Recursion: Training on Generated Data Makes Models Forget}},\n  author = {Shumailov and others},\n  journal = {Nature},\n  year = {2024},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser and others},\n  journal = {arXiv preprint arXiv:2404.01413},\n  year = {2024},\n}\n\n% ===== OOD Detection =====\n\n@inproceedings{ood_baseline,\n  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},\n  author = {Hendrycks and Gimpel},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2017},\n}\n\n% ===== Data Quality =====\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek and others},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri and others},\n  journal = {Nature},\n  year = {2024},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson and Kirchner},\n  year = {2022},\n  howpublished = {Technical Talk},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen and others},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo and others},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar and He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n@article{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang and others},\n  journal = {arXiv preprint arXiv:2404.01268},\n  year = {2024},\n}\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel and others},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu and others},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed and others},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng and others},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n% ===== Survey =====\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar and others},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "29fec1f7-3426-467b-93e8-6a96f31ea7f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TMNkjVwiaz2sEWkWfKLgVo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8373,
      "cache_read_input_tokens": 24475,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8373
      },
      "output_tokens": 12,
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

_source line 12 · 2026-05-15T04:20:26.744Z_

<details><summary>↩ Tool result · `toolu_01Ceb49A8HBwPaoPuD8hWfhT`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "92dcc42c-599d-4ca6-bade-90dc245b9e85",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
    "content": "% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann and others},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy and others},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{intrinsic_dimension,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@article{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani and Chen},\n  journal = {Transactions on Machine Learning Research},\n  year = {2026},\n}\n\n@article{generator_barrier,\n  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  author = {Pu and others},\n  journal = {arXiv preprint arXiv:2604.13692},\n  year = {2026},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady and others},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@inproceedings{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected?}},\n  author = {Sadasivan and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman and others},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n% ===== Model Collapse =====\n\n@article{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad and others},\n  journal = {arXiv preprint arXiv:2307.01850},\n  year = {2023},\n}\n\n@article{curse_of_recursion,\n  title = {{The Curse of Recursion: Training on Generated Data Makes Models Forget}},\n  author = {Shumailov and others},\n  journal = {Nature},\n  year = {2024},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser and others},\n  journal = {arXiv preprint arXiv:2404.01413},\n  year = {2024},\n}\n\n% ===== OOD Detection =====\n\n@inproceedings{ood_baseline,\n  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},\n  author = {Hendrycks and Gimpel},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2017},\n}\n\n% ===== Data Quality =====\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie and others},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek and others},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri and others},\n  journal = {Nature},\n  year = {2024},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson and Kirchner},\n  year = {2022},\n  howpublished = {Technical Talk},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen and others},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo and others},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar and He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n@article{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang and others},\n  journal = {arXiv preprint arXiv:2404.01268},\n  year = {2024},\n}\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang and others},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel and others},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu and others},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed and others},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng and others},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi and others},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n% ===== Survey =====\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar and others},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_01R5nJjPnyKqVR9L7LFRBe7S`</summary>

```json
{
  "command": "grep -c '^@' /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/references.bib",
  "description": "Count BibTeX entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "5417d2e4-04d9-40d4-9c1f-8089db59bec9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EkKEW9nvnsEnHZAPrbm8dq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5687,
      "cache_read_input_tokens": 32848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5687
      },
      "output_tokens": 49,
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

_source line 14 · 2026-05-15T04:20:30.042Z_

<details><summary>↩ Tool result · `toolu_01R5nJjPnyKqVR9L7LFRBe7S`</summary>

```text
39
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "73ec971e-1701-4864-8745-dcef012e8248",
  "tool_use_result": {
    "stdout": "39",
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

_source line 15_

39 个 BibTeX 条目已生成，写入 `docs/paper/references.bib`。按 10 个 category 分组，所有条目的 key 与 `literature_map.yaml` 的 id 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "uuid": "469a832b-e152-49a3-a096-2b711f6d8d73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SWwggTHL2j3RtJE4RvJ8XV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 38535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 129
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

_source line 16_

39 个 BibTeX 条目已生成，写入 `docs/paper/references.bib`。按 10 个 category 分组，所有条目的 key 与 `literature_map.yaml` 的 id 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 90882,
  "duration_api_ms": 91732,
  "num_turns": 5,
  "stop_reason": "end_turn",
  "session_id": "1338d892-7854-4661-9d9f-bbd3b78c3672",
  "total_cost_usd": 0.37431325000000004,
  "usage": {
    "input_tokens": 6,
    "cache_creation_input_tokens": 26823,
    "cache_read_input_tokens": 107699,
    "output_tokens": 6025,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26823,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 67,
        "cache_read_input_tokens": 38535,
        "cache_creation_input_tokens": 129,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 129
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2085,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021650000000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 6,
      "outputTokens": 6025,
      "cacheReadInputTokens": 107699,
      "cacheCreationInputTokens": 26823,
      "webSearchRequests": 0,
      "costUSD": 0.37214825000000007,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "057ab22f-209e-482c-8b01-bd28d160804b"
}
```

</details>

---
