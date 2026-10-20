# research baseline code survey

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/chats/worker_research_baseline_code_survey_20260521T205234.jsonl`
- **Structured JSON:** [`af995017f2f68395f567.json`](../../sessions/af/af995017f2f68395f567.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

12 recorded events

### Tool call

_source line 1 · 2026-05-21T20:55:16.968251+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T20:55:16.968597+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T20:55:16.968787+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search CyclicJudge code",
  "prompt": "Search for the open-source code availability of \"CyclicJudge\", a method for mitigating judge bias in LLM evaluation. \n\nPerform these web searches and report findings:\n1. Search \"CyclicJudge github\"\n2. Search \"CyclicJudge mitigating judge bias LLM evaluation\"\n3. Search \"CyclicJudge LLM judge bias code\"\n\nFor each search, report the top results. I need to know:\n- Is there an open-source repo? If so, what's the URL?\n- What license does it use?\n- How is the code quality (well-documented, clean, etc.)?\n- How complex would it be to integrate into an evaluation pipeline?\n- If no code exists, how complex would reimplementation be based on the paper?\n\nBe thorough - check arxiv pages for code links too. Report all URLs you find.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "Agent",
  "tool_args": {
    "description": "Search CyclicJudge code",
    "prompt": "Search for the open-source code availability of \"CyclicJudge\", a method for mitigating judge bias in LLM evaluation. \n\nPerform these web searches and report findings:\n1. Search \"CyclicJudge github\"\n2. Search \"CyclicJudge mitigating judge bias LLM evaluation\"\n3. Search \"CyclicJudge LLM judge bias code\"\n\nFor each search, report the top results. I need to know:\n- Is there an open-source repo? If so, what's the URL?\n- What license does it use?\n- How is the code quality (well-documented, clean, etc.)?\n- How complex would it be to integrate into an evaluation pipeline?\n- If no code exists, how complex would reimplementation be based on the paper?\n\nBe thorough - check arxiv pages for code links too. Report all URLs you find.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T20:55:16.968953+00:00_

Async agent launched successfully.
agentId: a8f134abb4d185e98 (internal ID - do not mention to user. Use SendMessage with to: 'a8f134abb4d185e98' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias/4909b84a-fc3b-4b99-94f5-cd6cd3d00579/tasks/a8f134abb4d185e98.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T20:55:16.969096+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search UDA debiasing code",
  "prompt": "Search for the open-source code availability of \"UDA\" (Unsupervised Debiasing Alignment), a method for debiasing LLM judges.\n\nPerform these web searches and report findings:\n1. Search \"UDA unsupervised debiasing alignment LLM judge github\"\n2. Search \"UDA AAAI 2026 LLM judge\"\n3. Search \"unsupervised debiasing alignment LLM evaluation code\"\n\nFor each search, report the top results. I need to know:\n- Is there an open-source repo? If so, what's the URL?\n- What license does it use?\n- How is the code quality (well-documented, clean, etc.)?\n- How complex would it be to integrate into an evaluation pipeline?\n- If no code exists, how complex would reimplementation be based on the paper?\n\nBe thorough - check arxiv pages for code links too. Report all URLs you find.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "Agent",
  "tool_args": {
    "description": "Search UDA debiasing code",
    "prompt": "Search for the open-source code availability of \"UDA\" (Unsupervised Debiasing Alignment), a method for debiasing LLM judges.\n\nPerform these web searches and report findings:\n1. Search \"UDA unsupervised debiasing alignment LLM judge github\"\n2. Search \"UDA AAAI 2026 LLM judge\"\n3. Search \"unsupervised debiasing alignment LLM evaluation code\"\n\nFor each search, report the top results. I need to know:\n- Is there an open-source repo? If so, what's the URL?\n- What license does it use?\n- How is the code quality (well-documented, clean, etc.)?\n- How complex would it be to integrate into an evaluation pipeline?\n- If no code exists, how complex would reimplementation be based on the paper?\n\nBe thorough - check arxiv pages for code links too. Report all URLs you find.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T20:55:16.969244+00:00_

Async agent launched successfully.
agentId: af7bbaae6de608256 (internal ID - do not mention to user. Use SendMessage with to: 'af7bbaae6de608256' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias/4909b84a-fc3b-4b99-94f5-cd6cd3d00579/tasks/af7bbaae6de608256.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T20:55:16.969393+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search DCR contamination code",
  "prompt": "Search for the open-source code availability of \"DCR\" (Data Contamination Ratio), a method for quantifying data contamination in LLM benchmarks.\n\nPerform these web searches and report findings:\n1. Search \"DCR data contamination ratio LLM github\"\n2. Search \"DCR quantifying data contamination EMNLP 2025\"\n3. Search \"DCR factor benchmark contamination code\"\n4. Search \"data contamination ratio benchmark LLM evaluation github\"\n\nFor each search, report the top results. I need to know:\n- Is there an open-source repo? If so, what's the URL?\n- What license does it use?\n- How is the code quality (well-documented, clean, etc.)?\n- How complex would it be to integrate into an evaluation pipeline?\n- If no code exists, how complex would reimplementation be based on the paper?\n\nBe thorough - check arxiv pages for code links too. Report all URLs you find.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "Agent",
  "tool_args": {
    "description": "Search DCR contamination code",
    "prompt": "Search for the open-source code availability of \"DCR\" (Data Contamination Ratio), a method for quantifying data contamination in LLM benchmarks.\n\nPerform these web searches and report findings:\n1. Search \"DCR data contamination ratio LLM github\"\n2. Search \"DCR quantifying data contamination EMNLP 2025\"\n3. Search \"DCR factor benchmark contamination code\"\n4. Search \"data contamination ratio benchmark LLM evaluation github\"\n\nFor each search, report the top results. I need to know:\n- Is there an open-source repo? If so, what's the URL?\n- What license does it use?\n- How is the code quality (well-documented, clean, etc.)?\n- How complex would it be to integrate into an evaluation pipeline?\n- If no code exists, how complex would reimplementation be based on the paper?\n\nBe thorough - check arxiv pages for code links too. Report all URLs you find.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T20:55:16.969590+00:00_

Async agent launched successfully.
agentId: a187aff206deccdee (internal ID - do not mention to user. Use SendMessage with to: 'a187aff206deccdee' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias/4909b84a-fc3b-4b99-94f5-cd6cd3d00579/tasks/a187aff206deccdee.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T20:55:16.969754+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Search Preference Leakage code",
  "prompt": "Search for the open-source code availability of \"Preference Leakage\", a method related to LLM judge contamination.\n\nPerform these web searches and report findings:\n1. Search \"preference leakage LLM judge github\"\n2. Search \"preference leakage contamination ICLR 2026\"\n3. Search \"preference leakage benchmark contamination LLM code\"\n4. Search \"preference leakage evaluation bias open source\"\n\nFor each search, report the top results. I need to know:\n- Is there an open-source repo? If so, what's the URL?\n- What license does it use?\n- How is the code quality (well-documented, clean, etc.)?\n- How complex would it be to integrate into an evaluation pipeline?\n- If no code exists, how complex would reimplementation be based on the paper?\n\nBe thorough - check arxiv pages for code links too. Report all URLs you find.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "Agent",
  "tool_args": {
    "description": "Search Preference Leakage code",
    "prompt": "Search for the open-source code availability of \"Preference Leakage\", a method related to LLM judge contamination.\n\nPerform these web searches and report findings:\n1. Search \"preference leakage LLM judge github\"\n2. Search \"preference leakage contamination ICLR 2026\"\n3. Search \"preference leakage benchmark contamination LLM code\"\n4. Search \"preference leakage evaluation bias open source\"\n\nFor each search, report the top results. I need to know:\n- Is there an open-source repo? If so, what's the URL?\n- What license does it use?\n- How is the code quality (well-documented, clean, etc.)?\n- How complex would it be to integrate into an evaluation pipeline?\n- If no code exists, how complex would reimplementation be based on the paper?\n\nBe thorough - check arxiv pages for code links too. Report all URLs you find.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T20:55:16.969903+00:00_

Async agent launched successfully.
agentId: a66baf991dc2e0c2b (internal ID - do not mention to user. Use SendMessage with to: 'a66baf991dc2e0c2b' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias/4909b84a-fc3b-4b99-94f5-cd6cd3d00579/tasks/a66baf991dc2e0c2b.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_baseline_code_survey_20260521T205234",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T20:55:16.970526+00:00_

UDA 完成，代码链接已失效，无可用 repo。等待最后一个 Preference Leakage。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_baseline_code_survey_20260521T205234"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-21T20:55:16.970743+00:00_

4 个 agent 全部返回，汇总如下：

---

### 1. CyclicJudge
- **公开代码**: 无
- **Repo URL**: N/A
- **License**: N/A
- **代码质量**: N/A
- **适配难度**: N/A
- **重实现复杂度**: **简单** — 核心算法是 round-robin judge 分配，~50-100 行 Python。给 K 个 judge、N 个 scenario，按 `i % K` 分配即可，无需训练或特殊库。
- **备注**: 论文 arXiv [2603.01865](https://arxiv.org/abs/2603.01865)，作者来自 Slingshot AI / Cambridge。作者 GitHub 和机构 org 均无相关 repo，论文中无 code availability 声明。

---

### 2. UDA (Unsupervised Debiasing Alignment)
- **公开代码**: 无（匿名审稿 repo 已 403）
- **Repo URL**: `https://anonymous.4open.science/r/62AB93CD-23B4`（已失效）
- **License**: N/A
- **代码质量**: N/A
- **适配难度**: N/A
- **重实现复杂度**: **中等** — 核心是 3 层 MLP（输入 6D+9 维特征，输出 K-factor + soft labels），配合三项无监督 loss（anchor alignment / rank fidelity / collective consensus）。模型本身简单，主要工作量在数据管线（多 judge pairwise 评测 + embedding 特征提取）和训练流程。估计 2-4 天。
- **备注**: AAAI 2026，作者来自 ZhipuAI / PKU / Tsinghua / Westlake。论文 arXiv [2508.09724](https://arxiv.org/abs/2508.09724)。方法是 post-hoc 的，不修改 judge prompt，只调整 Elo 更新。

---

### 3. DCR (Data Contamination Ratio)
- **公开代码**: 有
- **Repo URL**: [https://github.com/chengxuphd/dcr](https://github.com/chengxuphd/dcr)
- **License**: Apache-2.0
- **代码质量**: **中**（结构清晰、有 README 和示例，但仅 4 commits、1 star，学术发布级别）
- **适配难度**: **中等** — 提供 CLI 和 Python API，模块化设计（core/utils）。需将数据转为其 CSV 格式，阈值 θ₁-θ₄ 需针对新 benchmark 调参。依赖 `skfuzzy` 做模糊推理。
- **重实现复杂度**: 中等（如不用原 repo）— 四级污染检测（语义/信息/数据/标签）+ 模糊推理系统，估计 2-4 天。
- **备注**: EMNLP 2025 Main。arXiv [2507.11405](https://arxiv.org/abs/2507.11405)。方法需要访问训练数据（或代理），对闭源 LLM 适用性受限。

---

### 4. Preference Leakage
- **公开代码**: 有
- **Repo URL**: [https://github.com/David-Li0406/Preference-Leakage](https://github.com/David-Li0406/Preference-Leakage)
- **License**: **未标注**（论文 CC-BY 4.0，repo 无 LICENSE 文件）
- **代码质量**: **中偏差** — 82% Jupyter Notebook，无 docstring，无测试，是实验复现脚本而非可复用库。但包含预计算数据和模型输出（Google Drive），有参考价值。
- **适配难度**: **困难**（集成完整管线）/ **中等**（仅用 leakage score 度量）— 完整管线依赖 LLaMA-Factory + DeepSpeed + vLLM + 多商业 API。度量本身是 win-rate 差值，计算简单。
- **重实现复杂度**: 仅度量部分 **简单**；含训练管线 **中等**。
- **备注**: ICLR 2026 poster。arXiv [2502.01534](https://arxiv.org/abs/2502.01534)，55 stars。作者来自 ASU / UCLA / Notre Dame / UIUC。

---

**总结**:

| Baseline | 有代码 | 可直接用 | 重实现难度 |
|---|---|---|---|
| CyclicJudge | 无 | — | 简单（~100行） |
| UDA | 无（失效） | — | 中等（2-4天） |
| DCR | 有 | 需适配 | 中等 |
| Preference Leakage | 有 | 需大幅重构 | 度量简单/管线中等 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_baseline_code_survey_20260521T205234"
}
```

</details>

---
