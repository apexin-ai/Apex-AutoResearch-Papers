# research related work v2

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_research_related_work_v2_20260520T203349.jsonl`
- **Structured JSON:** [`f50d5e21050a2b0fddcd.json`](../../sessions/f5/f50d5e21050a2b0fddcd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-20T20:35:32.447634+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-research.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T20:35:32.448058+00:00_

1	---
2	name: LLM Evaluation Variance — Research Patterns
3	description: Experimental consensus on variance sources, decomposition methods, and gaps in LLM evaluation reproducibility (10 papers, 2024-2026)
4	type: research
5	source_papers: 10
6	---
7	
8	## Variance Source Taxonomy
9	
10	**Infrastructure variance** (4/10; high confidence):
11	- Numerical precision: BF16→9% accuracy std; FP32→~0% (Yuan 2025). Reasoning models most affected.
12	- Batch-size dependence: 80/1000 unique completions at T=0 from batch-invariance failure in RMSNorm/GEMM/attention (ThinkingMachines 2025).
13	- Background randomness at T=0: GPT~0.075, Gemini~0.065, Claude~0 effective temperature (Messina TMLR 2026).
14	
15	**Methodological variance** (6/10; high confidence):
16	- Judge choice dominates safety eval (43.8% variance); prompt~50% in open models, ~25% commercial (Mesting 2026, Brittlebench 2026).
17	- Much apparent prompt sensitivity is evaluation artifact — LLM-judge raises rank correlation 0.30→0.95 (Hua EMNLP 2025).
18	- Standard CIs omit 40-60% uncertainty; naive 95% CIs→79% coverage at scale (Mesting 2026).
19	
20	## Decomposition Frameworks
21	
22	| Framework | Paper | Method |
23	|-----------|-------|--------|
24	| TEE (G-theory) | Mesting 2026 | REML + D-study, facets: item/prompt/judge/temp |
25	| Total Variance | Brittlebench 2026 | V_data + V_brittleness via ANOVA |
26	| Intent Decomp | Kunievsky 2025 | intent/articulation/model uncertainty |
27	| Background Temp | Messina 2026 | Reference calibration→single T_bg scalar |
28	
29	G-theory adaptation is the most rigorous approach (Mesting). 4/10 papers use variance decomposition. **High confidence.**
30	
31	## Benchmarks & Models
32	
33	Top benchmarks: MMLU (3), GPQA (3), MATH (3), ARC (2), TruthfulQA (2). Models: Llama/Qwen/GPT families (5 papers each); 7B-8B open-weight as standard testbed. 10-100 runs per config is norm. **High confidence.**
34	
35	## Mitigations
36	
37	- LayerCast (BF16 store+FP32 compute): <3.4% diver
…[truncated 732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T20:35:32.448219+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/skills/projects/nlp_variance_gtheory/distilled-writing.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T20:35:32.448513+00:00_

1	---
2	name: LLM Evaluation Variance — Writing Patterns
3	description: Narrative strategies, figure/table conventions from LLM evaluation variance papers (8 deep-read, 2024-2026)
4	type: writing
5	source_papers: 8
6	---
7	
8	## Story Types
9	
10	- **Breaking limitations** (3/8): Brittlebench, Yuan, ThinkingMachines. "Everyone assumed X, we show it fails." High.
11	- **Simplification** (2/8): Hua, GeneralizIT. "Complex problem, simpler real answer." Medium.
12	- **Unifying framework** (2/8): Kunievsky, Messina. "Scattered observations, one formalism." Medium.
13	- **Cross-domain transfer** (1/8): Mesting (psychometrics→ML). Our paper fits this type — study Mesting's structure. Low but critical.
14	
15	## Hook: Counter-Intuitive Claim Dominates (4/8, high)
16	
17	"Greedy≠deterministic" (Yuan), "80/1000 unique at T=0" (ThinkingMachines), "sensitivity is artifact" (Hua), "95% CIs→79% coverage" (Mesting). **Pattern**: open with a concrete number violating expectations. Avoid vague "X is important."
18	
19	## Tension: "Everyone's Doing It Wrong" (4/8, high)
20	
21	(1) Cite widespread practice, (2) quantified evidence it fails, (3) identify overlooked factor. ThinkingMachines adds a twist: debunk the accepted explanation before presenting the correct one.
22	
23	## Intro: 4 Paragraphs + 3 Contributions (mode)
24	
25	(1) Context, (2) existing approaches + limitation, (3) gap/surprise, (4) contributions. 3 contributions standard: framework + empirical finding + practical tool. **Support: 5/8, high.**
26	
27	## Figure Conventions
28	
29	**Figure 1**: problem_illustration (4/8) — show problem exists before solution. Concrete examples with before/after or divergence visualization. **High.**
30	
31	**Result figures**: bar charts primary (5/8); stacked bars for variance decomposition (2/8, Mesting/Brittlebench — expected idiom for our paper); line plots for trends (3/8); heatmaps for divergence (2/8). **High.**
32	
33	**Figure count**: 4-6 total. **Flow**: problem illustration →
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T20:35:32.448667+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T20:35:32.448813+00:00_

1	# Related Work — Structured Notes
2	
3	> 用于论文 Related Work 章节起草。按 3 个子类组织。基于 10 篇蒸馏论文 + ROADMAP 定位。
4	
5	## (a) G-theory & Variance Decomposition in NLP/ML
6	
7	### [Mesting et al., 2026] — TEE: Generalizability Theory for NLG Evaluation
8	- **核心发现**: 将心理测量学的 G-theory（REML + D-study）引入 NLG 评估；发现 judge 选择贡献 43.8% 方差，prompt 在开源模型中贡献~50%、商用模型~25%；标准 95% CI 实际覆盖率仅 79%
9	- **与本工作关系**: extends — 我们直接继承其 TEE 框架和 REML 方法，将其扩展到 infrastructure facets
10	- **差异化**: Mesting 只分解方法论 facets（item/prompt/judge/temp），未纳入硬件/精度等基础设施因素；我们的 G-theory 框架联合分解 infrastructure × methodology
11	
12	### [Kunievsky et al., 2025] — Prompt Sensitivity Variance Decomposition
13	- **核心发现**: 将 prompt sensitivity 分解为 intent（意图）、articulation（表述）、model uncertainty（模型不确定性）三个独立分量
14	- **与本工作关系**: complements — 提供了 prompt 方差的细粒度分解视角，其 articulation 分量对应我们框架中 prompt paraphrase facet
15	- **差异化**: 专注 prompt 单一维度的语义分解，未涉及基础设施方差，也未采用 G-theory 的交叉设计
16	
17	### [Nalisnick et al.] — GeneralizIT: Software for G-theory in ML
18	- **核心发现**: 为 ML 场景提供 G-theory 计算工具包，简化 REML 估计和 D-study 设计流程
19	- **与本工作关系**: complements — 提供可复用的计算基础设施，我们的实验可能使用或参考其实现
20	- **差异化**: 是通用工具而非针对特定方差源的实证研究；我们提供具体的 LLM 评估方差分解实证结果和 reproducibility budget
21	
22	## (b) Infrastructure Variance
23	
24	### [Yuan et al., 2025] — LayerCast: Mixed-Precision Inference Variance
25	- **核心发现**: BF16 推理导致 9% 的 accuracy 标准差，FP32 接近 0%；提出 LayerCast（BF16 存储 + FP32 计算），将 divergence 控制在 <3.4% 同时节省 34% 显存；推理模型受影响最大
26	- **与本工作关系**: addresses limitation of — 量化了精度对推理结果的影响，但未将其纳入统一的方差分解框架
27	- **差异化**: Yuan 只刻画精度这一个 infrastructure 因素并提出缓解方案；我们将精度作为 G-theory 框架中的一个 facet，与方法论因素联合分解
28	
29	### [Messina et al., 2026 (TMLR)] — Background Temperature Effects on GPU Computation
30	- **核心发现**: 即使 T=0，API 模型仍存在 "背景随机性"：GPT~0.075、Gemini~0.065、Claude~0 有效温度；提出 reference calibration 方法量化为单一标量 T_bg
31	- **与本工作关系**: complements — 揭示了一类此前被忽视的 infrastructure 方差源（硬件层面的非确定性），为我们纳入硬件 facet 提供实证依据
32	- **差异化**: Messina 聚焦 API 层面的背景温度刻画，未进行多因素交叉分解；我们将此类硬件非确定性纳入 G-theory 的交叉设计
33	
3
…[truncated 1826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T20:35:32.448958+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T20:35:32.449074+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T20:35:32.449195+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "nlp_variance_gtheory",
  "file": "literature_map.yaml",
  "max_chars": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "nlp_variance_gtheory",
    "file": "literature_map.yaml",
    "max_chars": "0"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T20:35:32.449421+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: \\\"2026-05-20T14:00:00Z\\\"\\n  total_papers: 10\\n\\ncategories:\\n  - key: \\\"gtheory_evaluation\\\"\\n    name: \\\"G-Theory & Evaluation Variance\\\"\\n    narrative: \\\"Applying Generalizability Theory and variance decomposition to LLM evaluation reliability\\\"\\n  - key: \\\"infrastructure_variance\\\"\\n    name: \\\"Infrastructure-Induced Variance\\\"\\n    narrative: \\\"Hardware, precision, and CUDA-level nondeterminism as variance sources in LLM inference\\\"\\n  - key: \\\"prompt_sensitivity\\\"\\n    name: \\\"Prompt Sensitivity & Methodological Variance\\\"\\n    narrative: \\\"Prompt phrasing, seed, temperature, and ordering as variance sources\\\"\\n  - key: \\\"evaluation_methodology\\\"\\n    name: \\\"Evaluation Methodology\\\"\\n    narrative: \\\"Scoring artifacts, benchmark design, and evaluation protocol considerations\\\"\\n\\npapers:\\n  mesting2026hidden:\\n    title: \\\"Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking\\\"\\n    authors:\\n      - \\\"Mesting, F.\\\"\\n    year: 2026\\n    venue: \\\"arXiv\\\"\\n    url: \\\"https://arxiv.org/abs/2604.11581\\\"\\n    category: \\\"gtheory_evaluation\\\"\\n    role: \\\"direct-competitor\\\"\\n    relevance: \\\"Closest methodological precedent: G-theory decomposition of 5 facets (item, prompt, temperature, judge model, replication) on AILuminate/MMLU/Chatbot Arena. Found judge model=43.8%, prompt×judge=12.4%. Critically excludes infrastructure factors — our work extends this by crossing infrastructure with methodology.\\\"\\n    verified: false\\n    added_by: \\\"director\\\"\\n    added_at: \\\"2026-05-20T14:00:00Z\\\"\\n\\n  brittlebench2026:\\n    title: \\\"Brittlebench: Quantifying LLM Robustness via Prompt Sensitivity\\\"\\n    authors: []\\n    ye
…[truncated 5880 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T20:35:32.449629+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md",
  "content": "# Related Work — Structured Notes\n\n> 用于论文 Related Work 章节起草。按 3 个子类组织。基于 10 篇蒸馏论文 + ROADMAP 定位。\n\n## (a) G-theory & Variance Decomposition in NLP/ML\n\n### [Mesting et al., 2026] — Hidden Measurement Error in LLM Pipelines\n- **核心发现**: 将心理测量学的 G-theory（REML + D-study）引入 NLG 评估，交叉分解 5 个 facets（item/prompt/temperature/judge model/replication）；发现 judge 选择贡献 43.8% 方差，prompt×judge 交互贡献 12.4%；标准 95% CI 实际覆盖率仅 79%，标准 CI 遗漏 40-60% 不确定性\n- **方法**: 在 AILuminate、MMLU、Chatbot Arena 上对多个 LLM 进行全交叉 G-study，用 REML 估计方差分量，D-study 指导评估设计优化（如 3 个 judge 可降低 38% SE）\n- **与本工作的关系**: extends — 我们直接继承其 TEE 框架和 REML 方法论，是最近的方法论前驱；但其 facets 完全限于方法论层面，未涉及 infrastructure\n- **我们的差异化**: 我们将 G-theory 框架扩展到 infrastructure facets（precision/hardware/batch），实现 infrastructure × methodology 的联合交叉分解，这是 Mesting 未触及的维度\n\n### [Kunievsky et al., 2025] — Prompt Sensitivity Variance Decomposition\n- **核心发现**: 将 prompt sensitivity 分解为 intent（意图）、articulation（表述）、model uncertainty（模型不确定性）三个独立分量\n- **方法**: 提出基于语义层次的方差分解框架，将 prompt 变异按语义保持程度分级\n- **与本工作的关系**: complements — 提供了 prompt 方差的细粒度语义分解，其 articulation 分量对应我们框架中 prompt paraphrase facet\n- **我们的差异化**: Kunievsky 专注 prompt 单一维度的语义分解，未涉及基础设施方差，也未采用 G-theory 的全交叉设计；我们的框架同时容纳 prompt 和 infrastructure facets\n\n### [Nalisnick et al., 2024] — GeneralizIT: G-theory Software for ML\n- **核心发现**: 为 ML 场景提供 G-theory 计算工具包（Python），简化 REML 估计和 D-study 设计流程\n- **方法**: Python 实现 G-theory 核心计算，包括方差分量估计和 D-study 投影\n- **与本工作的关系**: complements — 提供可复用的计算基础设施，我们的实验可能使用或参考其实现\n- **我们的差异化**: GeneralizIT 是通用工具而非针对特定方差源的实证研究；我们提供具体的 LLM 评估方差分解实证结果和 reproducibility budget\n\n## (b) Infrastructure Variance\n\n### [Yuan et al., 2025] — LayerCast: Mixed-Precision Inference Variance\n- **核心发现**: BF16 推理导致高达 9% 的 accuracy 标准差和 9,000-token 的回复长度偏移，FP32 接近 0%；推理模型（reasoning models）受影响最大；提出 LayerCast（BF16 存储 + FP32 计算），将 divergence 控制在 <3.4% 同时节省 34% 显存\n- **方法**: 系统性测试不同 GPU 数量、类型、精度配置下的 LLM 推理输出变异，对比 FP32/BF16/FP16 的准确率和生成长度差异\n- **与本工作的关系**: addresses limitation of — 提供了 precision 作为 infrastructure 方差源的关键经验证据，但未将其纳入多因素统一分解框架，止步于单因素刻画+工程缓解\n- **我们的差异化**: 我们将 precision 作为 G-theory 框架中的一个 facet，与 prompt/judge/temperature 等方法论因素联合交叉分解，可量化 precision × methodology 交互效应\n\n### [Messina et al., 2026 (TMLR)] — Background Temperature Effects on GPU Computation\n- **核心发现**: 即使名义温度 T=0，API 模型仍存在\"背景随机性\"：GPT 有效温度~0.075、Gemini~0.065、Claude~0；根因是 BF16/FP16 浮点运算的非结合性（floating-point non-associativity）导致的隐式随机性\n- **方法**: 提出 reference calibration 方法，将背景非确定性量化为单一标量 T_bg；在多个 API 模型上系统测量 T=0 下的输出变异分布\n- **与本工作的关系**: complements — 为 infrastructure 层面的非确定性提供了理论解释（浮点非结合性）和量化方法（T_bg），为我们纳入 hardware facet 提供实证和理论依据；precision × temperature 交互在 text_match 下可能显著\n- **我们的差异化**: Messina 聚焦 API 层面的 T_bg 刻画，是单因素描述性研究；我们将此类硬件非确定性纳入 G-theory 的多因素交叉设计，检验其与方法论因素的交互\n\n### [ThinkingMachines, 2025] — Batch Invariance Failure in LLM Inference\n- **核心发现**: T=0 下 Qwen3-8B 在默认 vLLM 设置下 1000 次推理产生 80 种不同输出；根因不是随机种子，而是 RMSNorm/GEMM/attention 算子的 batch-size 依赖性；提出确定性内核方案，代价为 1.6-2.1× 延迟\n- **方法**: 在 vLLM 框架下系统性测试 batch size 对 T=0 推理的影响，逐层定位非确定性来源（RMSNorm → GEMM → attention），提出并验证 batch-invariant 内核\n- **与本工作的关系**: addresses limitation of — 发现并定位了 batch 非确定性这一关键 infrastructure 方差源，但止步于工程诊断和修复，未进行跨因素归因\n- **我们的差异化**: 我们使用默认设置（不启用确定性内核）以反映从业者真实条件，用 text_exact_match 指标捕获类似的 infrastructure 非确定性，并将 batch 因素与其他 infrastructure/methodology 因素一起纳入 G-theory 分解\n\n## (c) Prompt Sensitivity & Methodological Variance\n\n### [Brittlebench, 2026] — Prompt Brittleness Benchmark\n- **核心发现**: 系统性评估 prompt 脆弱性，prompt 措辞贡献约 50% 方差（开源模型）、商用模型约 25%；63% 的情况下单一扰动即导致排名反转\n- **方法**: 通过 ANOVA 分解 V_data + V_brittleness，设计标准化 prompt 扰动协议，在多模型多基准上评估\n- **与本工作的关系**: complements — 提供了大规模 prompt 脆弱性的实证基准和扰动协议（我们的 prompt paraphrase 生成参考其方法）；其 V_brittleness 分量对应我们框架中 prompt facet 的方差\n- **我们的差异化**: Brittlebench 使用传统 ANOVA 只分解 data vs. brittleness 两个分量；我们的 G-theory 框架不仅量化 prompt sensitivity，还分解其与 judge/temperature/precision 等因素的交互效应\n\n### [Hua et al., 2025 (EMNLP)] — Scoring Artifacts in LLM Evaluation\n- **核心发现**: 大量表观的 prompt sensitivity 实际上是评估方法的 artifact——使用 LLM-judge 替代 log-likelihood 评估后 rank correlation 从 0.30 跃升至 0.95\n- **方法**: 对比 log-likelihood 和 generation-based 评估方式下的 prompt sensitivity 表现，揭示评分方法对方差估计的系统性偏差\n- **与本工作的关系**: complements — 警示区分\"真实方差\"与\"评估 artifact\"的重要性；为我们选择 generation-based 评估协议（而非 log-likelihood）提供方法论依据\n- **我们的差异化**: Hua 聚焦揭示 artifact 现象而非系统性分解方差来源；我们的 G-theory 框架可将 scoring method 作为 facet 纳入，从而量化其贡献\n\n### [Same Prompt, Different Outcomes, 2026] — LLM Reproducibility\n- **核心发现**: 在 2 策略 × 6 模型 × 4 温度 × 10 重复的设计下确认了方法论层面的方差，但排除了硬件/精度因素\n- **方法**: 多温度多模型重复实验设计 [需补充：具体评估任务和指标]\n- **与本工作的关系**: complements — 确认 methodology-layer 方差的存在，但缺乏 infrastructure 交叉\n- **我们的差异化**: 我们同时纳入 infrastructure 和 methodology 因素进行联合分解\n\n### [Bui et al., 2025] — Seed Sensitivity in LLM Fine-Tuning\n- **核心发现**: 微调阶段种子敏感性极端（RTES variance=18.22），是单因素研究\n- **方法**: [需补充：具体微调设置、模型、数据集]\n- **与本工作的关系**: complements — 预期与我们框架中 seed facet 直接相关；为微调阶段 G-study 扩展提供动机\n- **我们的差异化**: Bui 只考察 seed 这一单一因素，未进行 infrastructure 交叉；我们的框架支持将 seed 与其他因素联合分解\n\n## 定位总结\n\n本项目是首个用 Generalizability Theory 联合分解 infrastructure（硬件类型、数值精度、batch 非确定性）与 methodology（prompt 措辞、随机种子、温度、few-shot 顺序）方差的工作。现有研究要么只用 G-theory 分解方法论 facets（Mesting），要么只刻画单一 infrastructure 因素并提出工程修复（Yuan、ThinkingMachines、Messina），没有工作在一个统一的交叉设计中同时容纳两类因素并检验其 separability。我们的 D-study 产出可量化的 reproducibility budget，为社区提供实验设计的决策依据。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md",
    "content": "# Related Work — Structured Notes\n\n> 用于论文 Related Work 章节起草。按 3 个子类组织。基于 10 篇蒸馏论文 + ROADMAP 定位。\n\n## (a) G-theory & Variance Decomposition in NLP/ML\n\n### [Mesting et al., 2026] — Hidden Measurement Error in LLM Pipelines\n- **核心发现**: 将心理测量学的 G-theory（REML + D-study）引入 NLG 评估，交叉分解 5 个 facets（item/prompt/temperature/judge model/replication）；发现 judge 选择贡献 43.8% 方差，prompt×judge 交互贡献 12.4%；标准 95% CI 实际覆盖率仅 79%，标准 CI 遗漏 40-60% 不确定性\n- **方法**: 在 AILuminate、MMLU、Chatbot Arena 上对多个 LLM 进行全交叉 G-study，用 REML 估计方差分量，D-study 指导评估设计优化（如 3 个 judge 可降低 38% SE）\n- **与本工作的关系**: extends — 我们直接继承其 TEE 框架和 REML 方法论，是最近的方法论前驱；但其 facets 完全限于方法论层面，未涉及 infrastructure\n- **我们的差异化**: 我们将 G-theory 框架扩展到 infrastructure facets（precision/hardware/batch），实现 infrastructure × methodology 的联合交叉分解，这是 Mesting 未触及的维度\n\n### [Kunievsky et al., 2025] — Prompt Sensitivity Variance Decomposition\n- **核心发现**: 将 prompt sensitivity 分解为 intent（意图）、articulation（表述）、model uncertainty（模型不确定性）三个独立分量\n- **方法**: 提出基于语义层次的方差分解框架，将 prompt 变异按语义保持程度分级\n- **与本工作的关系**: complements — 提供了 prompt 方差的细粒度语义分解，其 articulation 分量对应我们框架中 prompt paraphrase facet\n- **我们的差异化**: Kunievsky 专注 prompt 单一维度的语义分解，未涉及基础设施方差，也未采用 G-theory 的全交叉设计；我们的框架同时容纳 prompt 和 infrastructure facets\n\n### [Nalisnick et al., 2024] — GeneralizIT: G-theory Software for ML\n- **核心发现**: 为 ML 场景提供 G-theory 计算工具包（Python），简化 REML 估计和 D-study 设计流程\n- **方法**: Python 实现 G-theory 核心计算，包括方差分量估计和 D-study 投影\n- **与本工作的关系**: complements — 提供可复用的计算基础设施，我们的实验可能使用或参考其实现\n- **我们的差异化**: GeneralizIT 是通用工具而非针对特定方差源的实证研究；我们提供具体的 LLM 评估方差分解实证结果和 reproducibility budget\n\n## (b) Infrastructure Variance\n\n### [Yuan et al., 2025] — LayerCast: Mixed-Precision Inference Variance\n- **核心发现**: BF16 推理导致高达 9% 的 accuracy 标准差和 9,000-token 的回复长度偏移，FP32 接近 0%；推理模型（reasoning models）受影响最大；提出 LayerCast（BF16 存储 + FP32 计算），将 divergence 控制在 <3.4% 同时节省 34% 显存\n- **方法**: 系统性测试不同 GPU 数量、类型、精度配置下的 LLM 推理输出变异，对比 FP32/BF16/FP16 的准确率和生成长度差异\n- **与本工作的关系**: addresses limitation of — 提供了 precision 作为 infrastructure 方差源的关键经验证据，但未将其纳入多因素统一分解框架，止步于单因素刻画+工程缓解\n- **我们的差异化**: 我们将 precision 作为 G-theory 框架中的一个 facet，与 prompt/judge/temperature 等方法论因素联合交叉分解，可量化 precision × methodology 交互效应\n\n### [Messina et al., 2026 (TMLR)] — Background Temperature Effects on GPU Computation\n- **核心发现**: 即使名义温度 T=0，API 模型仍存在\"背景随机性\"：GPT 有效温度~0.075、Gemini~0.065、Claude~0；根因是 BF16/FP16 浮点运算的非结合性（floating-point non-associativity）导致的隐式随机性\n- **方法**: 提出 reference calibration 方法，将背景非确定性量化为单一标量 T_bg；在多个 API 模型上系统测量 T=0 下的输出变异分布\n- **与本工作的关系**: complements — 为 infrastructure 层面的非确定性提供了理论解释（浮点非结合性）和量化方法（T_bg），为我们纳入 hardware facet 提供实证和理论依据；precision × temperature 交互在 text_match 下可能显著\n- **我们的差异化**: Messina 聚焦 API 层面的 T_bg 刻画，是单因素描述性研究；我们将此类硬件非确定性纳入 G-theory 的多因素交叉设计，检验其与方法论因素的交互\n\n### [ThinkingMachines, 2025] — Batch Invariance Failure in LLM Inference\n- **核心发现**: T=0 下 Qwen3-8B 在默认 vLLM 设置下 1000 次推理产生 80 种不同输出；根因不是随机种子，而是 RMSNorm/GEMM/attention 算子的 batch-size 依赖性；提出确定性内核方案，代价为 1.6-2.1× 延迟\n- **方法**: 在 vLLM 框架下系统性测试 batch size 对 T=0 推理的影响，逐层定位非确定性来源（RMSNorm → GEMM → attention），提出并验证 batch-invariant 内核\n- **与本工作的关系**: addresses limitation of — 发现并定位了 batch 非确定性这一关键 infrastructure 方差源，但止步于工程诊断和修复，未进行跨因素归因\n- **我们的差异化**: 我们使用默认设置（不启用确定性内核）以反映从业者真实条件，用 text_exact_match 指标捕获类似的 infrastructure 非确定性，并将 batch 因素与其他 infrastructure/methodology 因素一起纳入 G-theory 分解\n\n## (c) Prompt Sensitivity & Methodological Variance\n\n### [Brittlebench, 2026] — Prompt Brittleness Benchmark\n- **核心发现**: 系统性评估 prompt 脆弱性，prompt 措辞贡献约 50% 方差（开源模型）、商用模型约 25%；63% 的情况下单一扰动即导致排名反转\n- **方法**: 通过 ANOVA 分解 V_data + V_brittleness，设计标准化 prompt 扰动协议，在多模型多基准上评估\n- **与本工作的关系**: complements — 提供了大规模 prompt 脆弱性的实证基准和扰动协议（我们的 prompt paraphrase 生成参考其方法）；其 V_brittleness 分量对应我们框架中 prompt facet 的方差\n- **我们的差异化**: Brittlebench 使用传统 ANOVA 只分解 data vs. brittleness 两个分量；我们的 G-theory 框架不仅量化 prompt sensitivity，还分解其与 judge/temperature/precision 等因素的交互效应\n\n### [Hua et al., 2025 (EMNLP)] — Scoring Artifacts in LLM Evaluation\n- **核心发现**: 大量表观的 prompt sensitivity 实际上是评估方法的 artifact——使用 LLM-judge 替代 log-likelihood 评估后 rank correlation 从 0.30 跃升至 0.95\n- **方法**: 对比 log-likelihood 和 generation-based 评估方式下的 prompt sensitivity 表现，揭示评分方法对方差估计的系统性偏差\n- **与本工作的关系**: complements — 警示区分\"真实方差\"与\"评估 artifact\"的重要性；为我们选择 generation-based 评估协议（而非 log-likelihood）提供方法论依据\n- **我们的差异化**: Hua 聚焦揭示 artifact 现象而非系统性分解方差来源；我们的 G-theory 框架可将 scoring method 作为 facet 纳入，从而量化其贡献\n\n### [Same Prompt, Different Outcomes, 2026] — LLM Reproducibility\n- **核心发现**: 在 2 策略 × 6 模型 × 4 温度 × 10 重复的设计下确认了方法论层面的方差，但排除了硬件/精度因素\n- **方法**: 多温度多模型重复实验设计 [需补充：具体评估任务和指标]\n- **与本工作的关系**: complements — 确认 methodology-layer 方差的存在，但缺乏 infrastructure 交叉\n- **我们的差异化**: 我们同时纳入 infrastructure 和 methodology 因素进行联合分解\n\n### [Bui et al., 2025] — Seed Sensitivity in LLM Fine-Tuning\n- **核心发现**: 微调阶段种子敏感性极端（RTES variance=18.22），是单因素研究\n- **方法**: [需补充：具体微调设置、模型、数据集]\n- **与本工作的关系**: complements — 预期与我们框架中 seed facet 直接相关；为微调阶段 G-study 扩展提供动机\n- **我们的差异化**: Bui 只考察 seed 这一单一因素，未进行 infrastructure 交叉；我们的框架支持将 seed 与其他因素联合分解\n\n## 定位总结\n\n本项目是首个用 Generalizability Theory 联合分解 infrastructure（硬件类型、数值精度、batch 非确定性）与 methodology（prompt 措辞、随机种子、温度、few-shot 顺序）方差的工作。现有研究要么只用 G-theory 分解方法论 facets（Mesting），要么只刻画单一 infrastructure 因素并提出工程修复（Yuan、ThinkingMachines、Messina），没有工作在一个统一的交叉设计中同时容纳两类因素并检验其 separability。我们的 D-study 产出可量化的 reproducibility budget，为社区提供实验设计的决策依据。\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T20:35:32.449869+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/related_work_notes.md has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_related_work_v2_20260520T203349",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T20:35:32.450095+00:00_

更新完成。5 篇重点论文的主要补充：

- **Mesting 2026**：补充了具体 5 个 facets 名称、测试基准（AILuminate/MMLU/Chatbot Arena）、prompt×judge 交互 12.4%、D-study 实用结果（3 judges→38% SE reduction）
- **Yuan 2025**：补充了 9,000-token 回复长度偏移、reasoning models 最受影响、GPU 数量/类型也是变异源
- **Brittlebench 2026**：补充了 63% 排名反转数据、我们参考其扰动协议生成 prompt paraphrase
- **ThinkingMachines 2025**：补充了具体模型（Qwen3-8B）、框架（vLLM）、非确定性逐层定位（RMSNorm→GEMM→attention）、我们使用默认设置反映真实条件
- **Messina 2026**：补充了浮点非结合性作为理论根因、precision × temperature 交互预期

所有条目统一为 4 字段格式（核心发现/方法/与本工作的关系/我们的差异化）。Bui 和 Same Prompt 两篇信息不足处已标注 `[需补充]`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_related_work_v2_20260520T203349"
}
```

</details>

---
