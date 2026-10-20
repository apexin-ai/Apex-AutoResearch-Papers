# fix doc d003

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_fix_doc-d003_20260514T103713.jsonl`
- **Structured JSON:** [`15e1644a6221903deb16.json`](../../sessions/15/15e1644a6221903deb16.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-14T10:38:11.817344+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T10:38:11.817641+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T10:38:11.817831+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T10:38:11.818029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# TaxEI vs. Related Methods: Differentiation & Positioning\\n\\n> **Date**: 2026-05-14\\n> **Sources**: arXiv, ACL Anthology, OpenReview, NeurIPS proceedings\\n> **Purpose**: Systematic comparison of TaxEI (Taxonomy-guided Error Injection) against representative agent robustness and training methods.\\n\\n---\\n\\n## 1. Comparison Table\\n\\n| Dimension | **TaxEI** (Ours) | **PALADIN** | **Agent-R** | **AgentRefine** | **ReAct** | **Reflexion** | **Trial-and-Error (ETO)** |\\n|---|---|---|---|---|---|---|---|\\n| **Error Types** | Planning errors (step-order swap, sub-goal deletion) + Context errors (context truncation, observation masking) | Tool errors (API timeout, exception, inconsistent output) | Execution errors (wrong actions in interactive environments) | Execution errors (wrong actions during trajectory generation) | None (no explicit error modeling) | Execution errors (task failure signals) | Execution errors (failed trajectory outcomes) |\\n| **Injection Method** | Synthetic injection via taxonomy-defined operators (P1, P2, C1, C4) | Synthetic injection via tool failure simulation (ToolScan taxonomy) | Natural failure from model exploration + MCTS tree search | LLM-generated errors during synthetic trajectory creation | None | Natural failure from trial episodes | Natural failure from agent exploration |\\n| **Recovery Signal** | Environment-grounded recovery: corrupted trajectory re-executed in environment, recovery generated from real environment feedback | Expert demonstration recovery + failure exemplar retrieval bank (55+ exemplars) | MCTS-guided trajectory splicing: erroneous path reconnected to correct branch at first divergence point | LLM self-refinement conditioned on environment observation feedback | N/A (no recovery mechanism) | Verbal self-reflection stored in episodic memory buffer | Contrastive failure-success trajectory pairs |\\n| **Training Framework** | SFT (LoRA on Qwen3-8B); inj
…[truncated 6311 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T10:38:11.818226+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cd /root/autodl-tmp/tax_error_inject_agent && cp docs/related_work_comparison.md docs/related_work_comparison.md.bak && sed -i \\\n  -e 's|Environment-grounded recovery: corrupted trajectory re-executed in environment, recovery generated from real environment feedback|Recovery conditioned on corrupted history and original observation; recovery generated from the corrupted trajectory context|' \\\n  -e 's|### Environment-Grounded Recovery with Structured Training Signal|### History-Conditioned Recovery with Structured Training Signal|' \\\n  -e 's|execute corrupted trajectories in the actual environment to observe realistic consequences, (3) generate recovery actions grounded in real environment feedback|construct corrupted trajectory context from the injection point, (3) generate recovery actions conditioned on the corrupted history and original observation|' \\\n  -e 's|it reflects how an agent should actually recover given the true environmental state after corruption|it reflects how an agent should recover given the corrupted trajectory context and original observation|' \\\n  docs/related_work_comparison.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cd /root/autodl-tmp/tax_error_inject_agent && cp docs/related_work_comparison.md docs/related_work_comparison.md.bak && sed -i \\\n  -e 's|Environment-grounded recovery: corrupted trajectory re-executed in environment, recovery generated from real environment feedback|Recovery conditioned on corrupted history and original observation; recovery generated from the corrupted trajectory context|' \\\n  -e 's|### Environment-Grounded Recovery with Structured Training Signal|### History-Conditioned Recovery with Structured Training Signal|' \\\n  -e 's|execute corrupted trajectories in the actual environment to observe realistic consequences, (3) generate recovery actions grounded in real environment feedback|construct corrupted trajectory context from the injection point, (3) generate recovery actions conditioned on the corrupted history and original observation|' \\\n  -e 's|it reflects how an agent should actually recover given the true environmental state after corruption|it reflects how an agent should recover given the corrupted trajectory context and original observation|' \\\n  docs/related_work_comparison.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T10:38:11.818374+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T10:38:11.818540+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -in \"environment.grounded\\|env.grounded\\|grounded in.*environment\\|real environment feedback\\|true environmental state\" /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -in \"environment.grounded\\|env.grounded\\|grounded in.*environment\\|real environment feedback\\|true environmental state\" /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T10:38:11.818679+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T10:38:11.818798+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "grep -inE \"environment.grounded|env.grounded|grounded in.*environment|real environment feedback|true environmental state\" /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "grep -inE \"environment.grounded|env.grounded|grounded in.*environment|real environment feedback|true environmental state\" /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T10:38:11.818920+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'grep -inE \\\"environment.grounded|env.grounded|grounded in.*environment|real environment feedback|true environmental state\\\" /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md'\\n\\nExit code: 1\\n\\nStdout:\\n\\n\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T10:38:11.819050+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "diff /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md.bak /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "diff /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md.bak /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T10:38:11.819195+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'diff /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md.bak /root/autodl-tmp/tax_error_inject_agent/docs/related_work_comparison.md'\\n\\nExit code: 1\\n\\nStdout:\\n\\n---\\n> | **Recovery Signal** | Recovery conditioned on corrupted history and original observation; recovery generated from the corrupted trajectory context | Expert demonstration recovery + failure exemplar retrieval bank (55+ exemplars) | MCTS-guided trajectory splicing: erroneous path reconnected to correct branch at first divergence point | LLM self-refinement conditioned on environment observation feedback | N/A (no recovery mechanism) | Verbal self-reflection stored in episodic memory buffer | Contrastive failure-success trajectory pairs |\\n61c61\\n< ### Environment-Grounded Recovery with Structured Training Signal\\n---\\n> ### History-Conditioned Recovery with Structured Training Signal\\n63c63\\n< TaxEI generates recovery training data through a three-stage pipeline: (1) inject taxonomy-defined errors into successful trajectories, (2) execute corrupted trajectories in the actual environment to observe realistic consequences, (3) generate recovery actions grounded in real environment feedback. This distinguishes TaxEI from methods that rely on LLM self-reflection (Reflexion, AgentRefine) or outcome-level contrastive signals (ETO). The recovery signal is neither hallucinated nor heuristic — it reflects how an agent should actually recover given the true environmental state after corruption. Combined with SFT training (without requiring RL infrastructure), this produces a practical and scalable training pipeline.\\n---\\n> TaxEI generates recovery training data through a three-stage pipeline: (1) inject taxonomy-defined errors into successful trajectories, (2) construct corrupted trajectory context from the injection point, (3) generate recovery actions conditione
…[truncated 553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_doc-d003_20260514T103713",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-14T10:38:11.819368+00:00_

完成。4 处修改：

| # | 位置 | 原文 | 替换为 |
|---|------|------|--------|
| 1 | 比较表 Recovery Signal 列 | `Environment-grounded recovery: corrupted trajectory re-executed in environment, recovery generated from real environment feedback` | `Recovery conditioned on corrupted history and original observation; recovery generated from the corrupted trajectory context` |
| 2 | §3 小节标题 | `Environment-Grounded Recovery with Structured Training Signal` | `History-Conditioned Recovery with Structured Training Signal` |
| 3 | §3 正文 pipeline 描述 | `execute corrupted trajectories in the actual environment to observe realistic consequences, (3) generate recovery actions grounded in real environment feedback` | `construct corrupted trajectory context from the injection point, (3) generate recovery actions conditioned on the corrupted history and original observation` |
| 4 | §3 正文总结句 | `it reflects how an agent should actually recover given the true environmental state after corruption` | `it reflects how an agent should recover given the corrupted trajectory context and original observation` |

grep 验证：`environment.grounded` / `env.grounded` / `real environment feedback` / `true environmental state` 均已清零。备份保留在 `related_work_comparison.md.bak`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_doc-d003_20260514T103713"
}
```

</details>

---
