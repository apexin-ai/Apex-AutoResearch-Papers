# paper writing abstract bn specific reframe

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_paper_writing_abstract_bn_specific_reframe_20260527T193857.jsonl`
- **Structured JSON:** [`580621a8c6b8f74ae6a8.json`](../../sessions/58/580621a8c6b8f74ae6a8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-27T19:40:22.342631+00:00_

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
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T19:40:22.343216+00:00_

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
…[truncated 5709 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T19:40:22.343414+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\begin\\{abstract\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\begin\\{abstract\\}",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T19:40:22.343556+00:00_

24:\begin{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T19:40:22.343725+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
  "offset": "22",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
    "offset": "22",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T19:40:22.343893+00:00_

22	\maketitle
23	
24	\begin{abstract}
25	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates substantially lagging task completion on safety-critical benchmarks.
26	We present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance, with twelve conditions varying gradient flow, label content, normalization type, spatial reference frame, and temporal extent.
27	Our central finding is that \textbf{gradient flow through the auxiliary head into the vision encoders is the dominant source of safety degradation among the factors tested}. In the cleanest comparison---BatchNorm conditions trained under the same v2 codebase---enabling gradient flow is associated with a reduction in Collision Avoidance Rate of 4.2 percentage points (Full OCC 0.725 vs.\ Detach OCC 0.767; $n{=}3$ and $n{=}4$). Detach OCC is statistically indistinguishable from the no-auxiliary-head Vanilla baseline ($p{=}0.28$), confirming that the auxiliary head itself is harmless when gradients are blocked. The BatchNorm + gradient flow cell is both the worst-performing and most unstable configuration ($\sigma{=}0.064$, ${>}2.5{\times}$ other cells). Effect sizes are large but the small-sample design ($n{\leq}4$ per cell) limits pairwise power; the consistent directional pattern across conditions provides converging evidence.
28	Gradient analysis confirms orthogonality between action and auxiliary gradients (cosine similarity near zero), ruling out direct gradient conflict. Spatial label content (ground-truth occupancy, random binary labels, egocentric depth maps) showed no detectable effect on safety outcomes in our experiments, indicating that the gradient pathway, not the spatial information, determines the result.
29	Practical guidelines: do not add auxiliary spatial heads for safety purposes. If an auxiliary head is required by other objectives, use de
…[truncated 710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T19:40:22.344115+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
  "old_string": "\\begin{abstract}\nFine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates substantially lagging task completion on safety-critical benchmarks.\nWe present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance, with twelve conditions varying gradient flow, label content, normalization type, spatial reference frame, and temporal extent.\nOur central finding is that \\textbf{gradient flow through the auxiliary head into the vision encoders is the dominant source of safety degradation among the factors tested}. In the cleanest comparison---BatchNorm conditions trained under the same v2 codebase---enabling gradient flow is associated with a reduction in Collision Avoidance Rate of 4.2 percentage points (Full OCC 0.725 vs.\\ Detach OCC 0.767; $n{=}3$ and $n{=}4$). Detach OCC is statistically indistinguishable from the no-auxiliary-head Vanilla baseline ($p{=}0.28$), confirming that the auxiliary head itself is harmless when gradients are blocked. The BatchNorm + gradient flow cell is both the worst-performing and most unstable configuration ($\\sigma{=}0.064$, ${>}2.5{\\times}$ other cells). Effect sizes are large but the small-sample design ($n{\\leq}4$ per cell) limits pairwise power; the consistent directional pattern across conditions provides converging evidence.\nGradient analysis confirms orthogonality between action and auxiliary gradients (cosine similarity near zero), ruling out direct gradient conflict. Spatial label content (ground-truth occupancy, random binary labels, egocentric depth maps) showed no detectable effect on safety outcomes in our experiments, indicating that the gradient pathway, not the spatial information, determines the result.\nPractical guidelines: do not add auxiliary spatial heads for safety purposes. If an auxiliary head is required by other objectives, use detached gradients with LayerNorm (Detach+LN)---which normalizes per-token without running statistics, avoiding the distributional coupling that makes BatchNorm sensitive to gradient flow---and never combine BatchNorm with gradient flow. The auxiliary head is discarded after training at zero inference cost.\n\\end{abstract}",
  "new_string": "\\begin{abstract}\nFine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates lagging task completion on safety-critical benchmarks.\nWe present a factorial study of twelve conditions varying five factors (gradient flow, label content, normalization type, spatial reference frame, and temporal extent) to isolate how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.\nOur central finding is a \\textbf{crossover interaction between gradient flow and normalization type}, not a universal effect of gradient flow. Under Batch Normalization (BN), gradient flow degrades safety: Full OCC BN achieves a 0.725 Collision Avoidance Rate versus 0.767 for Detach BN (Cohen's $d = -0.94$, large). Under Layer Normalization (LN), the pattern reverses: Full OCC LN reaches 0.777, above the no-auxiliary-head Vanilla baseline of 0.745 (Cohen's $d = +1.11$, large). The gradient flow main effect is non-significant ($p = 0.396$), the classic signature of a crossover interaction. The BN + gradient flow cell is both the worst-performing and most unstable configuration ($\\sigma{=}0.064$, ${>}2.5{\\times}$ other cells). Spatial label content (ground-truth occupancy, random binary labels, egocentric depth maps) shows no detectable effect on safety; the gradient pathway, not the spatial information, determines the outcome.\nWe attribute this interaction to BN's running statistics: gradient flow through auxiliary heads shifts batch statistics in the shared encoder, a coupling absent in LN's per-token computation. Practical guidelines: detach auxiliary gradients under BN architectures; gradient flow is safe under LN; never combine BN with gradient flow.\n\\end{abstract}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
    "old_string": "\\begin{abstract}\nFine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates substantially lagging task completion on safety-critical benchmarks.\nWe present a systematic factorial study isolating how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance, with twelve conditions varying gradient flow, label content, normalization type, spatial reference frame, and temporal extent.\nOur central finding is that \\textbf{gradient flow through the auxiliary head into the vision encoders is the dominant source of safety degradation among the factors tested}. In the cleanest comparison---BatchNorm conditions trained under the same v2 codebase---enabling gradient flow is associated with a reduction in Collision Avoidance Rate of 4.2 percentage points (Full OCC 0.725 vs.\\ Detach OCC 0.767; $n{=}3$ and $n{=}4$). Detach OCC is statistically indistinguishable from the no-auxiliary-head Vanilla baseline ($p{=}0.28$), confirming that the auxiliary head itself is harmless when gradients are blocked. The BatchNorm + gradient flow cell is both the worst-performing and most unstable configuration ($\\sigma{=}0.064$, ${>}2.5{\\times}$ other cells). Effect sizes are large but the small-sample design ($n{\\leq}4$ per cell) limits pairwise power; the consistent directional pattern across conditions provides converging evidence.\nGradient analysis confirms orthogonality between action and auxiliary gradients (cosine similarity near zero), ruling out direct gradient conflict. Spatial label content (ground-truth occupancy, random binary labels, egocentric depth maps) showed no detectable effect on safety outcomes in our experiments, indicating that the gradient pathway, not the spatial information, determines the result.\nPractical guidelines: do not add auxiliary spatial heads for safety purposes. If an auxiliary head is required by other objectives, use detached gradients with LayerNorm (Detach+LN)---which normalizes per-token without running statistics, avoiding the distributional coupling that makes BatchNorm sensitive to gradient flow---and never combine BatchNorm with gradient flow. The auxiliary head is discarded after training at zero inference cost.\n\\end{abstract}",
    "new_string": "\\begin{abstract}\nFine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates lagging task completion on safety-critical benchmarks.\nWe present a factorial study of twelve conditions varying five factors (gradient flow, label content, normalization type, spatial reference frame, and temporal extent) to isolate how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.\nOur central finding is a \\textbf{crossover interaction between gradient flow and normalization type}, not a universal effect of gradient flow. Under Batch Normalization (BN), gradient flow degrades safety: Full OCC BN achieves a 0.725 Collision Avoidance Rate versus 0.767 for Detach BN (Cohen's $d = -0.94$, large). Under Layer Normalization (LN), the pattern reverses: Full OCC LN reaches 0.777, above the no-auxiliary-head Vanilla baseline of 0.745 (Cohen's $d = +1.11$, large). The gradient flow main effect is non-significant ($p = 0.396$), the classic signature of a crossover interaction. The BN + gradient flow cell is both the worst-performing and most unstable configuration ($\\sigma{=}0.064$, ${>}2.5{\\times}$ other cells). Spatial label content (ground-truth occupancy, random binary labels, egocentric depth maps) shows no detectable effect on safety; the gradient pathway, not the spatial information, determines the outcome.\nWe attribute this interaction to BN's running statistics: gradient flow through auxiliary heads shifts batch statistics in the shared encoder, a coupling absent in LN's per-token computation. Practical guidelines: detach auxiliary gradients under BN architectures; gradient flow is safe under LN; never combine BN with gradient flow.\n\\end{abstract}"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T19:40:22.344320+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T19:40:22.344450+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
  "offset": "22",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/docs/paper/main.tex",
    "offset": "22",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T19:40:22.344592+00:00_

22	\maketitle
23	
24	\begin{abstract}
25	Fine-tuned Vision-Language-Action (VLA) models can achieve high task success yet remain behaviorally unsafe, with collision avoidance rates lagging task completion on safety-critical benchmarks.
26	We present a factorial study of twelve conditions varying five factors (gradient flow, label content, normalization type, spatial reference frame, and temporal extent) to isolate how auxiliary spatial supervision during VLA fine-tuning affects collision avoidance.
27	Our central finding is a \textbf{crossover interaction between gradient flow and normalization type}, not a universal effect of gradient flow. Under Batch Normalization (BN), gradient flow degrades safety: Full OCC BN achieves a 0.725 Collision Avoidance Rate versus 0.767 for Detach BN (Cohen's $d = -0.94$, large). Under Layer Normalization (LN), the pattern reverses: Full OCC LN reaches 0.777, above the no-auxiliary-head Vanilla baseline of 0.745 (Cohen's $d = +1.11$, large). The gradient flow main effect is non-significant ($p = 0.396$), the classic signature of a crossover interaction. The BN + gradient flow cell is both the worst-performing and most unstable configuration ($\sigma{=}0.064$, ${>}2.5{\times}$ other cells). Spatial label content (ground-truth occupancy, random binary labels, egocentric depth maps) shows no detectable effect on safety; the gradient pathway, not the spatial information, determines the outcome.
28	We attribute this interaction to BN's running statistics: gradient flow through auxiliary heads shifts batch statistics in the shared encoder, a coupling absent in LN's per-token computation. Practical guidelines: detach auxiliary gradients under BN architectures; gradient flow is safe under LN; never combine BN with gradient flow.
29	\end{abstract}
30	
31	\keywords{Vision-Language-Action Models, Robot Safety, Auxiliary Supervision, Collision Avoidance}
32	
33	\input{introduction}
34	
35	\input{related_work}
36	
37	\input{method}
38	
39	\input{
…[truncated 34 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-27T19:40:22.344798+00:00_

Abstract 替换完成。核心变更：

- **旧 claim** "gradient flow is the dominant source of safety degradation" → **新 claim** "crossover interaction between gradient flow and normalization type"
- 加入 BN 行（d = −0.94）和 LN 行（d = +1.11）双向证据
- 报告 main effect p = 0.396 作为交互效应信号
- 保留 BN + gradient flow 最不稳定的描述
- 机制归因于 BN running statistics vs LN per-token computation
- 实用建议按 normalization type 分条件给出
- ~230 words，无 em-dash，无 -ing 尾句，无 "significantly"/"dominant source"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_abstract_bn_specific_reframe_20260527T193857"
}
```

</details>

---
