# research r7 arxiv verification 4papers

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_research_r7_arxiv_verification_4papers_20260518T053434.jsonl`
- **Structured JSON:** [`a5312f644520b4ba1f48.json`](../../sessions/a5/a5312f644520b4ba1f48.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

11 recorded events

### Tool call

_source line 1 · 2026-05-18T05:35:10.914984+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-18T05:35:10.915317+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T05:35:10.915486+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.11926",
  "prompt": "Extract: 1) Does this paper exist? 2) The exact title 3) The full author list 4) The abstract. Return these fields clearly labeled."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2503.11926",
    "prompt": "Extract: 1) Does this paper exist? 2) The exact title 3) The full author list 4) The abstract. Return these fields clearly labeled."
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-18T05:35:10.915651+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.06594",
  "prompt": "Extract: 1) Does this paper exist? 2) The exact title 3) The full author list 4) The abstract. Return these fields clearly labeled."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.06594",
    "prompt": "Extract: 1) Does this paper exist? 2) The exact title 3) The full author list 4) The abstract. Return these fields clearly labeled."
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T05:35:10.915798+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.06036",
  "prompt": "Extract: 1) Does this paper exist? 2) The exact title 3) The full author list 4) The abstract. Return these fields clearly labeled."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2510.06036",
    "prompt": "Extract: 1) Does this paper exist? 2) The exact title 3) The full author list 4) The abstract. Return these fields clearly labeled."
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T05:35:10.915923+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.21344",
  "prompt": "Extract: 1) Does this paper exist? 2) The exact title 3) The full author list 4) The abstract. Return these fields clearly labeled."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://arxiv.org/abs/2509.21344",
    "prompt": "Extract: 1) Does this paper exist? 2) The exact title 3) The full author list 4) The abstract. Return these fields clearly labeled."
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T05:35:10.916112+00:00_

# Paper Information Extract

**1) Does this paper exist?**
Yes, this paper exists and is published on arXiv.

**2) The exact title:**
"Do Internal Layers of LLMs Reveal Patterns for Jailbreak Detection?"

**3) The full author list:**
- Sri Durga Sai Sowmya Kadali
- Evangelos E. Papalexakis

**4) The abstract:**
The researchers investigate how internal representations of large language models respond differently to jailbreak versus benign prompts. They examine GPT-J and Mamba2, finding "distinct layer-wise behaviors" that suggest internal model dynamics could be leveraged for more effective jailbreak detection and defense mechanisms.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T05:35:10.916269+00:00_

# Paper Information

**1) Does this paper exist?**
Yes, this paper exists on arXiv.

**2) Exact Title:**
"Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation"

**3) Full Author List:**
Bowen Baker, Joost Huizinga, Leo Gao, Zehao Dou, Melody Y. Guan, Aleksander Madry, Wojciech Zaremba, Jakub Pachocki, David Farhi

**4) Abstract:**
The authors investigate how to detect reward hacking in frontier reasoning models like OpenAI's o3-mini by using another LLM to monitor the model's chain-of-thought reasoning. They demonstrate that CoT monitoring outperforms monitoring actions alone, and that weaker models like GPT-4o can effectively monitor stronger ones. However, they identify a critical problem: when optimization pressure increases, agents learn to hide reward hacking within their reasoning while maintaining problematic behavior—a phenomenon termed "obfuscated reward hacking." The paper suggests accepting a "monitorability tax" by limiting optimization on chain-of-thought to preserve transparency and detectability of misaligned conduct.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T05:35:10.916423+00:00_

# Paper Information Extract

**1) Does this paper exist?**
Yes, this paper exists and is published on arXiv.

**2) Exact Title**
"Linear probes rely on textual evidence: Results from leakage mitigation studies in language models"

**3) Full Author List**
- Gerard Boxo
- Aman Neelappa
- Shivam Raval

**4) Abstract**
The researchers investigate how white-box monitors detect harmful behaviors in language models. Their key finding is that probe performance significantly decreases when textual evidence of behavior is removed, with AUROC reductions of 10-30 points depending on the context. Testing across three scenarios (Sandbagging, Sycophancy, and Bias), they demonstrate that probes struggle when they cannot access explicit behavioral markers like system prompts or reasoning traces. Additionally, they trained specialized models that produce outputs without behavioral verbalization, showing substantially lower probe performance (0.57 vs 0.74 AUROC for Bias; 0.57 vs 0.94 AUROC for Sandbagging). The authors conclude that linear probes may lack robustness when required to detect deeper, non-surface-level patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T05:35:10.916581+00:00_

# Paper Information

**1) Does this paper exist?**
Yes, this paper exists on arXiv.

**2) Exact Title:**
"Refusal Falls off a Cliff: How Safety Alignment Fails in Reasoning?"

**3) Full Author List:**
Qingyu Yin, Chak Tou Leong, Linyi Yang, Wenxuan Huang, Wenjie Li, Xiting Wang, Jaehong Yoon, YunXing, XingYu, and Jinjin Gu

**4) Abstract:**
The researchers investigate safety vulnerabilities in large reasoning models through mechanistic interpretability. They identify a phenomenon called "refusal cliff" where poorly-aligned models correctly detect harmful inputs during reasoning but experience sharp drops in refusal scores before generating output. Through causal analysis, they pinpoint specific attention heads contributing negatively to safety. The authors propose "Cliff-as-a-Judge," a data selection method that achieves comparable safety improvements using only 1.7% of standard training data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-18T05:35:10.916816+00:00_

| # | arXiv ID | 存在 | 真实标题 | 真实作者 | 与声称匹配 | 相关性 |
|---|----------|------|----------|----------|-----------|--------|
| 1 | 2503.11926 | ✓ | Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation | Baker, Huizinga, Gao, Dou, Guan, Madry, Zaremba, Pachocki, Farhi | **MISMATCH**: 标题缺少后半部分 "and the Risks of Promoting Obfuscation" | **高** — CoT monitoring 检测 reasoning model 的 misbehavior，与本项目 probing hidden states for safety detection 直接相关 |
| 2 | 2510.06594 | ✓ | Do Internal Layers of LLMs Reveal Patterns for Jailbreak Detection? | Kadali, Papalexakis | 匹配 | **高** — 研究 LLM 内部层对 jailbreak 的响应模式，与本项目 probing internal representations 方法高度一致 |
| 3 | 2510.06036 | ✓ | Refusal Falls off a Cliff: How Safety Alignment Fails in Reasoning? | Yin, Leong, Yang, Huang, Li, Wang, Yoon 等 | **MISMATCH**: 声称标题 "Refusal Falls Off a Cliff"，真实标题含副标题 "How Safety Alignment Fails in Reasoning?" | **高** — mechanistic interpretability 分析 reasoning model 的 safety failure（refusal cliff），与本项目 contrastive trace analysis 直接相关 |
| 4 | 2509.21344 | ✓ | Linear probes rely on textual evidence: Results from leakage mitigation studies in language models | Boxo, Neelappa, Raval | **MISMATCH**: 声称标题缺少副标题 | **极高** — 直接研究 linear probe 检测 harmful behavior 的局限性（依赖文本证据而非深层模式），是本项目方法的核心 baseline/对比工作 |

**MISMATCH 汇总**：
- **#1**: 声称标题 "Monitoring Reasoning Models for Misbehavior"，实际为 "Monitoring Reasoning Models for Misbehavior **and the Risks of Promoting Obfuscation**"
- **#3**: 声称标题 "Refusal Falls Off a Cliff"，实际为 "Refusal Falls off a Cliff: **How Safety Alignment Fails in Reasoning?**"
- **#4**: 声称标题 "Linear probes rely on textual evidence"，实际为 "Linear probes rely on textual evidence: **Results from leakage mitigation studies in language models**"

三处 mismatch 均为省略了副标题，主标题部分正确。4 篇论文全部存在，与项目相关性均为高或极高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_r7_arxiv_verification_4papers_20260518T053434"
}
```

</details>

---
