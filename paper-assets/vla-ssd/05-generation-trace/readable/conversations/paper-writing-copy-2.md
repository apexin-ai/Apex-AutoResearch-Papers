# paper writing

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_paper_writing_20260516T030955.jsonl`
- **Structured JSON:** [`115aca6a38093876c366.json`](../../sessions/11/115aca6a38093876c366.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-16T03:11:32.182390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T03:11:32.183020+00:00_

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
94	4. CHECK   → 确认
…[truncated 7201 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T03:11:32.183292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/red-section.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T03:11:32.183749+00:00_

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T03:11:32.183915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T03:11:32.184127+00:00_

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
16	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA that chains a frozen SigLIP vision encoder~\cite{zhai2023_s
…[truncated 3421 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T03:11:32.184284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T03:11:32.184441+00:00_

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
17	\paragraph{Geo
…[truncated 5220 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T03:11:32.184581+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/literature_map.yaml"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T03:11:32.184878+00:00_

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
28	      Action Atlas interactive exploration
…[truncated 29499 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T03:11:32.185163+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

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
  "recorded_role": "tool",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstration data to produce action-conditioned policies.\nRT-2~\\cite{brohan2023_rt2} pioneered this paradigm by co-fine-tuning PaLM-E on robotic trajectories; OpenVLA~\\cite{kim2024_openvla} extended it with open-source weights and 970K demonstrations, built on the Prismatic VLM architecture~\\cite{karamcheti2024} that chains frozen vision encoders with a Llama-2 backbone.\nThese architectures share a core design assumption---that LLM fine-tuning injects action-relevant knowledge---that our work tests at the representational level.\n\n\\paragraph{Behavioral analysis of VLAs.}\nA growing body of work reveals that VLAs rely disproportionately on visual input.\n\\cite{grant2026} showed across six architectures that visual pathways dominate action generation, with language instructions ``encoded but not used'' when visual context uniquely specifies the task.\nHou and Zhao~(2026) and Fei et al.~(2025) corroborated this through semantic perturbations and controlled robustness tests on LIBERO, finding that models largely ignore language instructions.\nThese studies establish the behavioral phenomenon; we provide a representational account showing that action-relevant geometric structure originates in the frozen vision encoder and is invariant to both LLM training and instruction content.\n\n\\paragraph{Mechanistic interpretability of VLAs.}\nRecent work has probed VLA internals from several angles.\n\\cite{haon2025} identified sparse semantic directions in OpenVLA causally linked to action selection, enabling activation steering without fine-tuning.\nSwann et al.~(2026) applied sparse autoencoders, finding features dominated by memorized sequences with some interpretable motion primitives; Rizzardo et al.~(2026) introduced feature-observability and controllability concepts for VLA steering.\nLu et al.~(2025) and Molinari et al.~(2025) probed OpenVLA layers, extracting symbolic states and world-model representations respectively.\nThese studies analyze individual features or single components; we complement them with a systematic decomposition quantifying each architectural component's contribution to action structure, with trained-versus-untrained controls absent from all prior work.\n\n\\paragraph{Vision encoder representations.}\nOur analysis leverages three encoders spanning different pretraining objectives: SigLIP~\\cite{zhai2023_siglip} (OpenVLA's frozen VL encoder), CLIP~\\cite{radford2021_clip} (independent VL baseline), and DINOv2~\\cite{oquab2024_dinov2} (vision-only control), all at ViT-L/14 scale.\nComparing VL-pretrained and vision-only encoders at matched architecture isolates the contribution of language grounding to action-relevant structure.\nRelatedly, Fang et al.~(2025) showed that VLA fine-tuning erodes original VLM reasoning abilities, consistent with our finding that fine-tuning does not improve the geometric structure inherited from the vision encoder.\n\n\\paragraph{Representational similarity analysis.}\nWe adopt RSA~\\cite{kriegeskorte2008} and CKA~\\cite{kornblith2019} as complementary geometric metrics, paired with linear probes~\\cite{alain2017} for functional evaluation.\nThis multi-metric approach proves essential: we show that geometric alignment and functional decodability can dissociate (e.g., DINOv2 matches VL encoders on probe $R^2$ but not RSA), revealing distinct aspects of representation quality relevant to VLA design.\n\n\\paragraph{Positioning.}\nOur work is distinguished from prior VLA analyses by three features.\nFirst, we perform a \\emph{component-level} representational decomposition---separately quantifying vision encoder, projector, and each LLM layer---rather than analyzing individual features or the model as a whole.\nSecond, we introduce trained-versus-untrained controls that isolate the effect of VLA fine-tuning, revealing that geometric structure is training-invariant while functional routing requires it.\nThird, we combine geometric and functional metrics with instruction ablation, providing converging evidence that the vision encoder is the \\emph{source} and the LLM is the \\emph{router} of action-relevant structure---complementing the behavioral evidence of \\cite{grant2026}, the mechanistic directions of \\cite{haon2025}, and the feature-level analyses of Swann et al.~(2026).\n"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T03:11:32.185350+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_20260516T030955",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-16T03:11:32.185534+00:00_

Related Work 已写入 `docs/paper/related_work.tex`。

结构：6 个 `\paragraph{}`——5 个分类 + 1 个 Positioning 收尾段。12 个已有 bib key 通过 `\cite{}` 引用；Swann、Rizzardo、Lu、Molinari、Hou、Fei、Fang 等不在 `.bib` 中的论文用自然语言提及，无 `\cite{}`。核心定位：与 Grant (behavioral)、Haon (mechanistic directions)、Swann (feature-level SAE) 互补，我们的独特贡献在 component-level decomposition + trained-vs-untrained controls + geometric/functional dual metrics。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_20260516T030955"
}
```

</details>

---
