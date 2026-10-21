# research d134 reference verification

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_research_d134-reference-verification_20260518T102656.jsonl`
- **Structured JSON:** [`e82f11a9d32b8e7853ef.json`](../../sessions/e8/e82f11a9d32b8e7853ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-18T10:27:49.553527+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T10:27:49.553912+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T10:27:49.554120+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2601.22642 Cao \"Pushing the Boundaries of Natural Reasoning\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2601.22642 Cao \"Pushing the Boundaries of Natural Reasoning\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T10:27:49.554283+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2510.01367 Wang \"Is It Thinking or Cheating\" TRACE reward hacking"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2510.01367 Wang \"Is It Thinking or Cheating\" TRACE reward hacking"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-18T10:27:49.554451+00:00_

Web search results for query: "arXiv 2601.22642 Cao "Pushing the Boundaries of Natural Reasoning""

Links: [{"title":"[2601.22642] Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification","url":"https://arxiv.org/abs/2601.22642"},{"title":"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models","url":"https://arxiv.org/html/2601.22642"}]

I found the paper! Here's what I can tell you about it:

"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification" is authored by Chuxue Cao, Jinluan Yang, Haoran Li, Kunhao Pan, Zijian Zhao, Zhengyu Chen, Yuchen Tian, Lijun Wu, Conghui He, Sirui Han, and Yike Guo, submitted on January 30, 2026.

**Key Contributions:**

The paper addresses how Large Language Models (LLMs) create logical inconsistencies and reward hacking through stochastic next-token prediction, which formal symbolic systems avoid. To bridge this gap, they introduce a formal logic verification-guided framework that dynamically interleaves formal symbolic verification with the natural language generation process, providing real-time feedback to detect and rectify errors as they occur.

Distinguished from previous neuro-symbolic methods limited by passive post-hoc validation, their approach actively penalizes intermediate fallacies during the reasoning chain.

They operationalize this framework via a novel two-stage training pipeline that synergizes formal logic verification-guided supervised fine-tuning and policy optimization.

**Results:**

Extensive evaluation on six benchmarks spanning mathematical, logical, and general reasoning demonstrates that their 7B and 14B models outperform state-of-the-art baselines by average margins of 10.4% and 14.2%, respectively.

You can access the paper directly at https://arxiv.org/abs/2601.22642 or the HTML version at https://arxiv.org/html/2601.22642.


REMINDER: You MUST include the sources abo
…[truncated 58 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-18T10:27:49.554648+00:00_

Web search results for query: "arXiv 2510.01367 Wang "Is It Thinking or Cheating" TRACE reward hacking"

Links: [{"title":"[2510.01367] Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/abs/2510.01367"},{"title":"[2510.01367v2] Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/abs/2510.01367v2"},{"title":"Is it thinking or cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/html/2510.01367"},{"title":"IS IT THINKING OR CHEATING? DETECTING IMPLICIT REWARD HACKING BY","url":"https://arxiv.org/pdf/2510.01367"},{"title":"Is it Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort | OpenReview","url":"https://openreview.net/forum?id=Gk7gLAtVDO"},{"title":"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort | Article Information | J-GLOBAL","url":"https://jglobal.jst.go.jp/en/detail?JGLOBAL_ID=202502217215600055"},{"title":"Trace Length is a Simple Uncertainty Signal in Reasoning Models","url":"https://arxiv.org/html/2510.10409v1"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/new?skip=525&show=500"},{"title":"CaughtCheating: Is Your MLLM a Good Cheating Detective? Exploring the Boundary of Visual Perception and Reasoning","url":"https://arxiv.org/html/2507.00045v1"},{"title":"[2507.00045] CaughtCheating: Is Your MLLM a Good Cheating Detective? Exploring the Boundary of Visual Perception and Reasoning","url":"https://arxiv.org/abs/2507.00045"}]

I found the paper you're looking for! Here's what I found about arXiv 2510.01367:

## Overview

The paper "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort" is by Xinpeng Wang and 4 other authors, submitted on October 1, 2025.

## The Problem

Reward hacking, where a reasoning model exploits loopholes in a reward funct
…[truncated 1065 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-18T10:27:49.554882+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.22642",
  "prompt": "Extract: 1) full title, 2) all authors, 3) submission date, 4) full abstract text, 5) any mention of reward shaping, GRPO, RL, formal logic verification, Goodhart's Law"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2601.22642",
    "prompt": "Extract: 1) full title, 2) all authors, 3) submission date, 4) full abstract text, 5) any mention of reward shaping, GRPO, RL, formal logic verification, Goodhart's Law"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T10:27:49.555023+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.01367",
  "prompt": "Extract: 1) full title, 2) all authors, 3) submission date, 4) full abstract text, 5) any mention of reward hacking taxonomy, ISR, necessity, Goodhart's Law, formal reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.01367",
    "prompt": "Extract: 1) full title, 2) all authors, 3) submission date, 4) full abstract text, 5) any mention of reward hacking taxonomy, ISR, necessity, Goodhart's Law, formal reasoning"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T10:27:49.555227+00:00_

# Paper Extraction Summary

**1) Full Title:**
"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort"

**2) All Authors:**
Xinpeng Wang, Nitish Joshi, Barbara Plank, Rico Angell, He He

**3) Submission Date:**
October 1, 2025 (v1); most recent revision March 2, 2026 (v4)

**4) Full Abstract:**
The paper addresses reward hacking where reasoning models "exploit loopholes in a reward function to achieve high rewards without solving the intended task." The authors propose TRACE (Truncated Reasoning AUC Evaluation), which detects implicit hacking by measuring reasoning effort. Their key insight is that "hacking occurs when exploiting the loophole is easier than solving the actual task." TRACE progressively truncates chain-of-thought outputs at various lengths to estimate expected reward, with hackers requiring "only a small fraction of its CoT" to achieve high rewards. Results show 65% gains over existing monitors in math reasoning and 30% gains in coding tasks.

**5) Mentions of Related Concepts:**
The document does not explicitly reference reward hacking taxonomy, ISR (implicit specification robustness), necessity constraints, Goodhart's Law, or formal reasoning frameworks by name.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T10:27:49.555398+00:00_

# Paper Extract Summary

**1) Full Title:**
"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification"

**2) All Authors:**
Chuxue Cao, Jinluan Yang, Haoran Li, Kunhao Pan, Zijian Zhao, Zhengyu Chen, Yuchen Tian, Lijun Wu, Conghui He, Sirui Han, Yike Guo

**3) Submission Date:**
January 30, 2026

**4) Full Abstract:**
Large Language Models demonstrate strong capabilities, yet their stochastic nature creates logical inconsistencies. The authors introduce a framework combining formal symbolic verification with natural language generation, offering real-time error detection. Their approach differs from passive post-hoc validation by actively penalizing intermediate reasoning errors. Using supervised fine-tuning and policy optimization across two stages, they evaluate on six benchmarks spanning mathematical, logical, and general reasoning tasks. Their 7B and 14B models outperform baselines by 10.4% and 14.2% respectively, demonstrating that "formal verification can serve as a scalable mechanism to significantly push the performance boundaries of advanced LLM reasoning."

**5) Relevant Mentions:**

- **Reward Shaping/RL:** The paper describes "policy optimization" as part of their training pipeline and mentions "actively penalizes intermediate fallacies."
- **Formal Logic Verification:** Central to the framework—"dynamically interleaves formal symbolic verification with the natural language generation process."
- **Goodhart's Law:** Not mentioned in the provided content.
- **GRPO:** Not mentioned in the provided content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_d134-reference-verification_20260518T102656",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T10:27:49.555635+00:00_

验证完成。

```
=== 论文 1: Cao et al. 2026 ===
arXiv ID 2601.22642: ✅ 存在
实际标题: "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification"
作者: Chuxue Cao, Jinluan Yang, Haoran Li, Kunhao Pan, Zijian Zhao, Zhengyu Chen, Yuchen Tian, Lijun Wu, Conghui He, Sirui Han, Yike Guo
提交日期: 2026-01-30
摘要概要: 提出 formal logic verification 与自然语言生成动态交织的框架，在推理链中实时检测和修正逻辑错误（区别于被动的 post-hoc 验证）。用 SFT + policy optimization 两阶段流水线训练，7B/14B 模型在 6 个 benchmark 上分别超 baseline 10.4%/14.2%。
与本文相关性: 中高
  - 共同点：formal logic verification 作为 RL 训练信号、intermediate reasoning 质量控制
  - 差异：他们做 interleaved real-time verification，我们做 post-hoc ISR reward shaping + hacking taxonomy
  - 未提及 Goodhart's Law 或 reward hacking
建议引用位置: Related Work（formal verification for reasoning 子节）+ Introduction（现有方法对比）

=== 论文 2: Wang et al. 2025 ===
arXiv ID 2510.01367: ✅ 存在
实际标题: "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort"
作者: Xinpeng Wang, Nitish Joshi, Barbara Plank, Rico Angell, He He
提交日期: 2025-10-01（v4: 2026-03-02）
摘要概要: 提出 TRACE（Truncated Reasoning AUC Evaluation），通过逐步截断 CoT 测量 reasoning effort 来检测 implicit reward hacking。核心观察：hacking 比真正解题"更容易"，hacker 只需 CoT 的一小部分就能获得高 reward。在 math reasoning 上比 72B CoT monitor 高 65%，coding 上比 32B monitor 高 30%。也在 OpenReview 上有记录。
与本文相关性: 高
  - 直接相关：reward hacking 检测、reasoning effort 量化
  - 我们的 ISR（Inference Step Redundancy）本质上也是量化 reasoning effort/necessity
  - TRACE 用截断 AUC 检测 hacking，我们用 per-step ablation 检测 hacking
  - 互补视角：他们做 detection，我们做 reward shaping + taxonomy
建议引用位置: Related Work（reward hacking detection 子节）+ Introduction（motivation for detecting hacking）+ Discussion（与 TRACE 方法论对比）
```

两篇论文均真实存在，arXiv ID 和标题完全匹配。Wang et al. (TRACE) 与本文高度相关，应重点引用；Cao et al. 属于 formal verification for reasoning 方向，相关但角度不同。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_d134-reference-verification_20260518T102656"
}
```

</details>

---
