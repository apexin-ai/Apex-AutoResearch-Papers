# paper writing limitations

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_paper_writing_limitations_20260517T001728.jsonl`
- **Structured JSON:** [`2d0b3e50c957c73b111e.json`](../../sessions/2d/2d0b3e50c957c73b111e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-17T00:18:11.550476+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_limitations_20260517T001728",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T00:18:11.551270+00:00_

1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **
…[truncated 4866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_limitations_20260517T001728",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T00:18:11.551570+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/",
  "description": "List existing paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_limitations_20260517T001728",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/",
    "description": "List existing paper sections"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T00:18:11.551828+00:00_

discussion.tex
experiments.tex
method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_limitations_20260517T001728",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T00:18:11.552013+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex",
  "content": "\\section{Limitations}\n\n\\paragraph{Statistical power for hidden-state probing.}\nOnly DeepSeek-R1-8B shows a statistically significant advantage of hidden-state (HS) probes over text-based probes ($p = 0.044$), and this result does not survive Bonferroni correction across three model comparisons. With 43 test traces per model, statistical power is limited for detecting moderate effect sizes. Larger evaluation sets are needed to determine whether the R1-8B advantage reflects a genuine modality difference or sampling noise.\n\n\\paragraph{Correlation, not causation.}\nOur probing methodology establishes that safety commitment is \\emph{decodable} from intermediate hidden states. It does not demonstrate that these representations causally drive the model's safe or unsafe behavior. Causal intervention studies, such as activation patching at the identified commitment point, would be necessary to verify that the probed features are mechanistically load-bearing rather than epiphenomenal.\n\n\\paragraph{Commitment point definition.}\nThe commitment point (CP) annotation relies on detecting the presence or absence of explicit safety reasoning in the chain-of-thought. Edge cases exist where models oscillate between safe and unsafe reasoning within a single trace, or embed safety-relevant considerations inside otherwise harmful text. We have not yet conducted inter-annotator agreement studies or sensitivity analyses over alternative CP definitions; these remain important directions for future work.\n\n\\paragraph{Dataset scale and diversity.}\nEach model is evaluated on 209 traces drawn from the HarmThoughts dataset, covering a specific set of jailbreak categories. We have not tested generalization to other attack types (e.g., multi-turn persuasion, encoded prompts), other languages, or substantially different prompt formats. Broader evaluation is needed before drawing conclusions about the universality of the commitment point phenomenon.\n\n\\paragraph{High false positive rate on safe traces.}\nAll probing methods produce false positive rates between 39\\% and 62\\% when applied to entirely safe traces. This level of specificity makes the current probes suitable as diagnostic research tools but unsuitable for deployment as production safety monitors without substantial improvements in precision.\n\n\\paragraph{Limited architectural diversity.}\nThree of the four tested model variants (DeepSeek-R1-Distill-Qwen-32B, QwQ-32B, DeepSeek-R1-Distill-Qwen-14B) share the Qwen base architecture. The sole Llama-based model (DeepSeek-R1-Distill-Llama-8B) is also the only one exhibiting a clear HS probing advantage. This confound makes it difficult to disentangle whether the observed differences arise from architecture, model scale, or distillation procedure. Evaluation on a wider range of base architectures (e.g., Mistral, Gemma, LLaMA-3) is needed to resolve this ambiguity.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_limitations_20260517T001728",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex",
    "content": "\\section{Limitations}\n\n\\paragraph{Statistical power for hidden-state probing.}\nOnly DeepSeek-R1-8B shows a statistically significant advantage of hidden-state (HS) probes over text-based probes ($p = 0.044$), and this result does not survive Bonferroni correction across three model comparisons. With 43 test traces per model, statistical power is limited for detecting moderate effect sizes. Larger evaluation sets are needed to determine whether the R1-8B advantage reflects a genuine modality difference or sampling noise.\n\n\\paragraph{Correlation, not causation.}\nOur probing methodology establishes that safety commitment is \\emph{decodable} from intermediate hidden states. It does not demonstrate that these representations causally drive the model's safe or unsafe behavior. Causal intervention studies, such as activation patching at the identified commitment point, would be necessary to verify that the probed features are mechanistically load-bearing rather than epiphenomenal.\n\n\\paragraph{Commitment point definition.}\nThe commitment point (CP) annotation relies on detecting the presence or absence of explicit safety reasoning in the chain-of-thought. Edge cases exist where models oscillate between safe and unsafe reasoning within a single trace, or embed safety-relevant considerations inside otherwise harmful text. We have not yet conducted inter-annotator agreement studies or sensitivity analyses over alternative CP definitions; these remain important directions for future work.\n\n\\paragraph{Dataset scale and diversity.}\nEach model is evaluated on 209 traces drawn from the HarmThoughts dataset, covering a specific set of jailbreak categories. We have not tested generalization to other attack types (e.g., multi-turn persuasion, encoded prompts), other languages, or substantially different prompt formats. Broader evaluation is needed before drawing conclusions about the universality of the commitment point phenomenon.\n\n\\paragraph{High false positive rate on safe traces.}\nAll probing methods produce false positive rates between 39\\% and 62\\% when applied to entirely safe traces. This level of specificity makes the current probes suitable as diagnostic research tools but unsuitable for deployment as production safety monitors without substantial improvements in precision.\n\n\\paragraph{Limited architectural diversity.}\nThree of the four tested model variants (DeepSeek-R1-Distill-Qwen-32B, QwQ-32B, DeepSeek-R1-Distill-Qwen-14B) share the Qwen base architecture. The sole Llama-based model (DeepSeek-R1-Distill-Llama-8B) is also the only one exhibiting a clear HS probing advantage. This confound makes it difficult to disentangle whether the observed differences arise from architecture, model scale, or distillation procedure. Evaluation on a wider range of base architectures (e.g., Mistral, Gemma, LLaMA-3) is needed to resolve this ambiguity.\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T00:18:11.552177+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_limitations_20260517T001728",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-17T00:18:11.552343+00:00_

已写入 `limitations.tex`。6 个 limitation 覆盖了统计力不足、因果性、CP 定义、数据规模、高 FPR、架构多样性。无 em-dash、无 -ing 短语结尾、无 AI 风格标志词。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_limitations_20260517T001728"
}
```

</details>

---
