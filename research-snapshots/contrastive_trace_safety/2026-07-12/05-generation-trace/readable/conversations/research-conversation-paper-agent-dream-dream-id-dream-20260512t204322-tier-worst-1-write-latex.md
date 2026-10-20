# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=worst 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-1/fd10c3cc-8799-4c51-b4c9-12c6ea6a406f.jsonl`
- **Structured JSON:** [`e802fa35ad385aec8f89.json`](../../sessions/e8/e802fa35ad385aec8f89.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T21:05:17.906Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T21:05:17.906Z",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=worst 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Restructure as analysis/negative-result paper: \"Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet).\" Core contribution becomes empirical analysis of three negative mining strategies with deep failure taxonomy. Key findings: (1) all hard negatives underperform random when pool diversity is sufficient; (2) CodeQL 2-hop reachability is too coarse to capture fine-grained repair relevance; (3) connected≠gold signal is necessary but not sufficient. Target: workshop paper (NLP4SE, ML4Code) or analysis/Findings track.\n\n- paper_framing.md 节选：\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Structure-grounded hard negatives outperform embedding-distance and random negatives for contrastive code retrieval training.** Inter-procedural data-flow connectivity provides a complementary signal dimension that textual similarity cannot recover — files that are lexically similar but structurally disconnected force the model to internalize structural relevance beyond surface features.\n\n2. **Embedding-distance hard negatives actively harm code retrieval compared to random negatives.** The gradient signal from embedding-distance negatives is partially redundant with the encoder's learned similarity, leading to degraded retrieval quality. (MVP evidence: -3.7pp recall@1 at pool=50, -27pp at pool=26, 3 seeds consistent.)\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** With 2-hop call-graph bounding, timeout <5%, and >40% of instances have connected-but-not-gold structural signals at scale.\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers conflate lexical similarity with structural relevance — a file sharing function names with the buggy code may be structurally unrelated, while a data-flow-connected file may contain the actual fix dependency.\n\n- **Existing approaches & gaps**:\n  - Text-based (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no data-flow edges, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: hard negatives improve code search, but embedding-distance negatives are redundant with encoder similarity\n\n- **Our framing**: The key gap is using structural connectivity for **training signal**, not just inference-time navigation. Structure-grounded hard negatives — lexically similar but data-flow disconnected files — provide a complementary learning signal. This is a general paradigm: any domain with external structural knowledge (molecular networks, circuit topology, KG retrieval) can use drift-immune structure-grounded negative mining. Code is the ideal testbed due to formal semantic guarantees.\n\n- **Headline result template**: \"On SWE-bench Lite, StructFuse with data-flow-aware hard negatives achieves X% recall@5 while embedding-distance negatives achieve Y% and random negatives Z%, demonstrating that structure-grounded negative mining provides training signal that text-based methods cannot recover.\"\n\n## Dual-Pillar Motivation (per Human Review)\n\n1. **Primary — Complementary signal dimension**: Structural connectivity encodes a relevance dimension entirely absent from textual signals. No amount of text-based training can recover inter-procedural data-flow relationships from token sequences alone.\n2. **Secondary — Selection drift immunity**: Structural graph is externally fixed; negative set does not drift with encoder updates (unlike embedding-distance negatives which shift every epoch).\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder.\n\n## Title\n\n\"StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval\"\n(Per Human Review: emphasize methodology, de-emphasize SE-specific framing)\n\n## Venue Fit Risks\n\n1. **EMNLP vs SE**: Frame as contrastive learning methodology with code as instantiation\n2. **Domain-specific concern**: Cross-domain generalization in Discussion (molecular networks, circuit topology, KG retrieval)\n3. **Incremental contribution**: Novelty is i\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-12T21:05:17.909Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T21:05:17.909Z",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-12T21:05:17.930Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=worst 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Restructure as analysis/negative-result paper: "Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet)." Core contribution becomes empirical analysis of three negative mining strategies with deep failure taxonomy. Key findings: (1) all hard negatives underperform random when pool diversity is sufficient; (2) CodeQL 2-hop reachability is too coarse to capture fine-grained repair relevance; (3) connected≠gold signal is necessary but not sufficient. Target: workshop paper (NLP4SE, ML4Code) or analysis/Findings track.

- paper_framing.md 节选：
# Paper Framing — StructFuse

## Target Venue
- Primary: EMNLP 2026 Main
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026

## Core Claims (3)

1. **Structure-grounded hard negatives outperform embedding-distance and random negatives for contrastive code retrieval training.** Inter-procedural data-flow connectivity provides a complementary signal dimension that textual similarity cannot recover — files that are lexically similar but structurally disconnected force the model to internalize structural relevance beyond surface features.

2. **Embedding-distance hard negatives actively harm code retrieval compared to random negatives.** The gradient signal from embedding-distance negatives is partially redundant with the encoder's learned similarity, leading to degraded retrieval quality. (MVP evidence: -3.7pp recall@1 at pool=50, -27pp at pool=26, 3 seeds consistent.)

3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** With 2-hop call-graph bounding, timeout <5%, and >40% of instances have connected-but-not-gold structural signals at scale.

## Story Spine

- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers conflate lexical similarity with structural relevance — a file sharing function names with the buggy code may be structurally unrelated, while a data-flow-connected file may contain the actual fix dependency.

- **Existing approaches & gaps**:
  - Text-based (SweRank, SWE-Fixer): blind to structural dependencies
  - Graph-guided (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no data-flow edges, no training signal
  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only
  - CoCoHaNeRe: hard negatives improve code search, but embedding-distance negatives are redundant with encoder similarity

- **Our framing**: The key gap is using structural connectivity for **training signal**, not just inference-time navigation. Structure-grounded hard negatives — lexically similar but data-flow disconnected files — provide a complementary learning signal. This is a general paradigm: any domain with external structural knowledge (molecular networks, circuit topology, KG retrieval) can use drift-immune structure-grounded negative mining. Code is the ideal testbed due to formal semantic guarantees.

- **Headline result template**: "On SWE-bench Lite, StructFuse with data-flow-aware hard negatives achieves X% recall@5 while embedding-distance negatives achieve Y% and random negatives Z%, demonstrating that structure-grounded negative mining provides training signal that text-based methods cannot recover."

## Dual-Pillar Motivation (per Human Review)

1. **Primary — Complementary signal dimension**: Structural connectivity encodes a relevance dimension entirely absent from textual signals. No amount of text-based training can recover inter-procedural data-flow relationships from token sequences alone.
2. **Secondary — Selection drift immunity**: Structural graph is externally fixed; negative set does not drift with encoder updates (unlike embedding-distance negatives which shift every epoch).

## Formal Definition

Given retrieval domain D, structural graph G, similarity function s, query q:
**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)

The structural graph is externally fixed and does not update with the encoder.

## Title

"StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval"
(Per Human Review: emphasize methodology, de-emphasize SE-specific framing)

## Venue Fit Risks

1. **EMNLP vs SE**: Frame as contrastive learning methodology with code as instantiation
2. **Domain-specific concern**: Cross-domain generalization in Discussion (molecular networks, circuit topology, KG retrieval)
3. **Incremental contribution**: Novelty is i

## 质量目标
"够审"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1df62460-115c-45a2-bbc0-229713b8aae0",
  "type": "user",
  "uuid": "434498a5-6cdb-4811-982b-22b77e628b0e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T21:05:17.929Z_

```json
{
  "parentUuid": "434498a5-6cdb-4811-982b-22b77e628b0e",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "9067a9b7-d088-4624-8910-0ae641ec940a",
  "timestamp": "2026-05-12T21:05:17.929Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T21:05:17.930Z_

```json
{
  "parentUuid": "9067a9b7-d088-4624-8910-0ae641ec940a",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "93bafadc-ff36-4a64-9c51-d63ca8cac5e2",
  "timestamp": "2026-05-12T21:05:17.930Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-12T21:05:17.930Z_

```json
{
  "parentUuid": "93bafadc-ff36-4a64-9c51-d63ca8cac5e2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d2979d46-1d32-44a0-a933-6254ddc9bab8",
  "timestamp": "2026-05-12T21:05:17.930Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier negative results paper on code retrieval",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---

### Assistant

_source line 8 · 2026-05-12T21:05:21.051Z_

Let me start by reading the experiment data and understanding the project context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2979d46-1d32-44a0-a933-6254ddc9bab8",
  "isSidechain": false,
  "requestId": "req_011CayMWM7bCymQXoM39TEX1",
  "type": "assistant",
  "uuid": "c2a84d59-30b7-4b49-9af9-705546ad631e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169tJRYpFHJx6NhoGgtMSfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12418,
      "cache_read_input_tokens": 11447,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12418
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-12T21:05:23.182Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Q3Dxotmrme927K2MHmvaJW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2a84d59-30b7-4b49-9af9-705546ad631e",
  "isSidechain": false,
  "requestId": "req_011CayMWM7bCymQXoM39TEX1",
  "type": "assistant",
  "uuid": "bef9feca-0230-4c62-a808-df13ad467076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169tJRYpFHJx6NhoGgtMSfp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12418,
      "cache_read_input_tokens": 11447,
      "output_tokens": 118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 118,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12418
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-12T21:05:23.467Z_

<details><summary>↩ Tool result · `toolu_01Q3Dxotmrme927K2MHmvaJW`</summary>

```text
1	[
2	  {
3	    "name": "M1 全量 CodeQL 提取",
4	    "description": "5K SWE-smith repos data-flow extraction + connected vs gold statistics",
5	    "results": {
6	      "repos_attempted": 5000,
7	      "repos_successful": 3850,
8	      "repos_skipped_no_python": 420,
9	      "repos_failed_codeql_error": 310,
10	      "repos_timeout": 420,
11	      "total_instances": 18200,
12	      "instances_with_extra_connected": 2550,
13	      "Z_pct_overall": 14.0,
14	      "Z_pct_small_lt50": 9.2,
15	      "Z_pct_medium_50_200": 24.8,
16	      "Z_pct_large_gt200": 5.1,
17	      "gold_in_connected_ratio": 0.72,
18	      "avg_connected_minus_gold_small": 1.1,
19	      "avg_connected_minus_gold_medium": 5.3,
20	      "avg_connected_minus_gold_large": 2.8,
21	      "cg_mean_s": 48.7,
22	      "cg_median_s": 22.1,
23	      "cg_p95_s": 210.5,
24	      "df_mean_s": 71.3,
25	      "df_median_s": 35.8,
26	      "df_p95_s": 340.2
27	    },
28	    "tables": [
29	      {
30	        "name": "Table 1: CodeQL Extraction Statistics by Repo Size",
31	        "columns": [
32	          "Repo Size",
33	          "N repos",
34	          "N instances",
35	          "Z%",
36	          "Avg Extra Connected",
37	          "Timeout%"
38	        ],
39	        "rows": [
40	          [
41	            "Small (<50 files)",
42	            2310,
43	            10920,
44	            9.2,
45	            1.1,
46	            5.8
47	          ],
48	          [
49	            "Medium (50-200)",
50	            963,
51	            4550,
52	            24.8,
53	            5.3,
54	            8.2
55	          ],
56	          [
57	            "Large (>200)",
58	            577,
59	            2730,
60	            5.1,
61	            2.8,
62	            22.1
63	          ],
64	          [
65	            "Overall",
66	            3850,
67	            18200,
68	            14.0,
69	            2.4,
70	            10.9
71	          ]
72	        ]
73	      }
74	    ],
75	    "figures": [],
76	    "analysis": "Z=14% 低于 20% 阈值，意味着 86% 的训练实例中 dataflow negatives 退化为与 random 等价 （connected set = gold set，无额外结构信号）。medium-repo 偏差假设得到验证：50-repo pilot 中 medium 占 55.7% 且 Z=55.7%，但 5K 自然分布下 medium 仅占 25%。large repos 的 Z 仅 5.1% 因为 2-hop 可达集过大（数百文件），反而无法提供有区分度的负例。scalability claim 需要根本性修改。\n\n\n50-repo Z=40.8% 被 medium-repo 偏差严重膨胀（medium 占比 55.7%，Z=55.7%）。 5K 规模下 repo size 分布回归自然分布：small 占 ~60%，medium ~25%，large ~15%。 small repos 文件少，call-graph 稀疏，connected set 几乎等于 gold set，Z 降至 ~9%。 large repos CodeQL 分析超时率高且 2-hop 边界内可达文件爆炸，但大多数可达文件与 bug 无关， gold_in_connected_ratio 下降到 0.72（pilot 时为 1.0），说明 path normalization 在 大规模异构 repo 中不够鲁棒。整体 Z=14% < 20% 阈值，核心 scalability claim 失败。\n"
77	  },
78	  {
79	    "name": "M2 全量 3-strategy 对比训练",
80	    "description": "random vs embedding_distance vs dataflow_aware, 3 seeds each, Qwen2.5-Coder-3B LoRA, ~15K training instances",
81	    "results": {
82	      "training_instances": 15400,
83	      "random_s42": {
84	        "val_loss": 0.082,
85	        "retrieval_R1": 0.412,
86	        "retrieval_R5": 0.783,
87	        "retrieval_R10": 0.871
88	      },
89	      "random_s123": {
90	        "val_loss": 0.079,
91	        "retrieval_R1": 0.425,
92	        "retrieval_R5": 0.791,
93	        "retrieval_R10": 0.878
94	      },
95	      "random_s456": {
96	        "val_loss": 0.085,
97	        "retrieval_R1": 0.408,
98	        "retrieval_R5": 0.776,
99	        "retrieval_R10": 0.865
100	      },
101	      "random_mean": {
102	        "retrieval_R1": 0.415,
103	        "retrieval_R5": 0.783,
104	        "retrieval_R10": 0.871
105	      },
106	      "emb_dist_s42": {
107	        "val_loss": 0.121,
108	        "retrieval_R1": 0.378,
109	        "retrieval_R5": 0.748,
110	        "retrieval_R10": 0.842
111	      },
112	      "emb_dist_s123": {
113	        "val_loss": 0.118,
114	        "retrieval_R1": 0.385,
115	        "retrieval_R5": 0.755,
116	        "retrieval_R10": 0.849
117	      },
118	      "emb_dist_s456": {
119	        "val_loss": 0.125,
120	        "retrieval_R1": 0.371,
121	        "retrieval_R5": 0.741,
122	        "retrieval_R10": 0.836
123	      },
124	      "emb_dist_mean": {
125	        "retrieval_R1": 0.378,
126	        "retrieval_R5": 0.748,
127	        "retrieval_R10": 0.842
128	      },
129	      "dataflow_s42": {
130	        "val_loss": 0.115,
131	        "retrieval_R1": 0.382,
132	        "retrieval_R5": 0.752,
133	        "retrieval_R10": 0.845
134	      },
135	      "dataflow_s123": {
136	        "val_loss": 0.112,
137	        "retrieval_R1": 0.39,
138	        "retrieval_R5": 0.758,
139	        "retrieval_R10": 0.851
140	      },
141	      "dataflow_s456": {
142	        "val_loss": 0.119,
143	        "retrieval_R1": 0.375,
144	        "retrieval_R5": 0.745,
145	        "retrieval_R10": 0.838
146	      },
147	      "dataflow_mean": {
148	        "retrieval_R1": 0.382,
149	        "retrieval_R5": 0.752,
150	        "retrieval_R10": 0.845
151	      },
152	      "delta_dataflow_vs_random_R5": -0.031,
153	      "delta_emb_vs_random_R5": -0.035,
154	      "delta_dataflow_vs_emb_R5": 0.004,
155	      "eval_pool_size": 200,
156	      "eval_n_samples": 2400
157	    },
158	    "tables": [
159	      {
160	        "name": "Table 2: Retrieval Performance by Negative Mining Strategy (pool=200)",
161	        "columns": [
162	          "Strategy",
163	          "R@1",
164	          "R@5",
165	          "R@10",
166	          "Δ vs Random R@5"
167	        ],
168	        "rows": [
169	          [
170	            "Random (3 seeds)",
171	            "0.415±0.009",
172	            "0.783±0.008",
173	            "0.871±0.007",
174	            "—"
175	          ],
176	          [
177	            "Embedding-distance",
178	            "0.378±0.007",
179	            "0.748±0.007",
180	            "0.842±0.007",
181	            "-0.035"
182	          ],
183	          [
184	            "Dataflow-aware",
185	            "0.382±0.008",
186	            "0.752±0.007",
187	            "0.845±0.007",
188	            "-0.031"
189	          ]
190	        ]
191	      }
192	    ],
193	    "figures": [],
194	    "analysis": "Dataflow negatives 表现与 embedding-distance 几乎不可区分，两者都劣于 random。 这支持核心假设：当 Z% 过低时，structure-grounded signal 被淹没在无差别负例中。 Random negatives 在大池中自然采样到足够多样性的负例，隐式包含了结构多样性。 这是论文的核心负面发现，也是 restructure 的关键证据。\n\n\nZ=14% 意味着 86% 的 dataflow training instances 实际上选取的负例与 random 无异 （connected=gold，disconnected set 就是全集减 gold）。仅 14% 的实例提供了真正的 structure-grounded signal，这不足以让模型学到结构特征。同时 dataflow negatives 在这 14% 的实例上选取的是\"lexically similar but disconnected\"文件，但 2-hop call-graph 的 disconnected 判定过于粗糙——很多被标记为 disconnected 的文件实际上 通过 3-hop 或间接数据流相连，导致假阴性噪声。embedding-distance negatives 的 harm effect 从 MVP 的 -3.7pp R@1 (pool=50) 缩小到 -3.7pp R@1 (pool=200)， 但因训练数据量增大（15K vs 127），redundancy 问题被更多样化的数据部分稀释。 dataflow 与 embedding_distance 的差异仅 0.4pp R@5，统计不显著（p>0.3）， 两者都不如 random。\n"
195	  },
196	  {
197	    "name": "M3a SWE-bench Lite end-to-end evaluation",
198	    "description": "3 strategies x best checkpoint, SWE-bench Lite 300 instances, Qwen3.6-27B agent",
199	    "results": {
200	      "n_instances": 300,
201	      "random_best": {
202	        "resolve_rate": 0.243,
203	        "recall_R5_file": 0.68,
204	        "avg_patches_generated": 2.1
205	      },
206	      "emb_dist_best": {
207	        "resolve_rate": 0.233,
208	        "recall_R5_file": 0.66,
209	        "avg_patches_generated": 2.0
210	      },
211	      "dataflow_best": {
212	        "resolve_rate": 0.237,
213	        "recall_R5_file": 0.67,
214	        "avg_patches_generated": 2.0
215	      },
216	      "baseline_swerank": {
217	        "resolve_rate": 0.247,
218	        "recall_R5_file": 0.71
219	      },
220	      "delta_dataflow_vs_random_resolve_pp": -0.6,
221	      "delta_dataflow_vs_swerank_resolve_pp": -1.0,
222	      "delta_emb_vs_random_resolve_pp": -1.0,
223	      "confidence_interval_95_resolve": 0.025
224	    },
225	    "tables": [
226	      {
227	        "name": "Table 3: SWE-bench Lite End-to-End Results",
228	        "columns": [
229	          "Retriever",
230	          "Resolve%",
231	          "File R@5",
232	          "Δ Resolve vs Random"
233	        ],
234	        "rows": [
235	          [
236	            "Random negatives",
237	            24.3,
238	            0.68,
239	            "—"
240	          ],
241	          [
242	            "Embedding-distance",
243	            23.3,
244	            0.66,
245	            "-1.0pp"
246	          ],
247	          [
248	            "Dataflow-aware",
249	            23.7,
250	            0.67,
251	            "-0.6pp"
252	          ],
253	          [
254	            "SweRank (baseline)",
255	            24.7,
256	            0.71,
257	            "+0.4pp"
258	          ]
259	        ]
260	      }
261	    ],
262	    "figures": [],
263	    "analysis": "End-to-end 结果是决定性的负面证据：structure-grounded negatives 在下游任务中 没有产生任何可测量的改进。SweRank baseline 的轻微优势表明，更多预训练数据 比更精巧的负例选择更有效——这本身是一个值得在分析论文中讨论的发现。\n\n\nRetrieval 阶段 dataflow 已经落后 random 3.1pp R@5，这个差距在 end-to-end pipeline 中 被 agent 的修复能力部分缓冲（agent 能通过多轮交互弥补检索遗漏），但无法反转。 resolve rate 差异在 confidence interval 内（±2.5pp），统计上三者不可区分。 SweRank baseline 因为在更大语料上预训练，甚至略优于我们所有策略，进一步削弱 structure-grounded training 的增量价值叙事。这意味着 end-to-end 结果无法支撑 任何正面 claim——最多只能说 \"no improvement or regression\"。\n"
264	  },
265	  {
266	    "name": "M3b RepoBench-R cross-file retrieval evaluation",
267	    "description": "RepoBench-R retrieval-only evaluation, no LLM agent, 3 strategies x best checkpoint",
268	    "results": {
269	      "n_samples": 1200,
270	      "random_best": {
271	        "MRR": 0.534,
272	        "recall_R5": 0.712,
273	        "recall_R10": 0.801
274	      },
275	      "emb_dist_best": {
276	        "MRR": 0.498,
277	        "recall_R5": 0.683,
278	        "recall_R10": 0.775
279	      },
280	      "dataflow_best": {
281	        "MRR": 0.507,
282	        "recall_R5": 0.691,
283	        "recall_R10": 0.782
284	      },
285	      "delta_dataflow_vs_random_R5_pp": -2.1,
286	      "delta_emb_vs_random_R5_pp": -2.9,
287	      "repobench_R_improvement_pp": -2.1
288	    },
289	    "tables": [
290	      {
291	        "name": "Table 4: RepoBench-R Retrieval Results",
292	        "columns": [
293	          "Strategy",
294	          "MRR",
295	          "R@5",
296	          "R@10",
297	          "Δ R@5 vs Random"
298	        ],
299	        "rows": [
300	          [
301	            "Random",
302	            0.534,
303	            0.712,
304	            0.801,
305	            "—"
306	          ],
307	          [
308	            "Embedding-distance",
309	            0.498,
310	            0.683,
311	            0.775,
312	            "-2.9pp"
313	          ],
314	          [
315	            "Dataflow-aware",
316	            0.507,
317	            0.691,
318	            0.782,
319	            "-2.1pp"
320	          ]
321	        ]
322	      }
323	    ],
324	    "figures": [],
325	    "analysis": "RepoBench-R 证实了 M2 的结论在 out-of-distribution 设置下也成立。 Dataflow training signal 不仅在 in-distribution 上无效，在 cross-repo transfer 上更差，因为 structural connectivity 是 repo-specific 的，不迁移到新 repo。 这是分析论文中 \"generalization failure\" 章节的关键证据。\n\n\nRepoBench-R 评估的是 cross-file code completion retrieval，与 SWE-bench 的 bug-fix retrieval 不同但相关。Random negatives 在此任务上也优于两种 hard negative 策略， 原因相同：大规模训练集中 random negatives 已经提供了足够的负例多样性。 Dataflow negatives 略优于 embedding-distance（delta 0.8pp），但仍显著低于 random。 在 RepoBench 的 cross-repo 设置下，我们训练时使用的 repo-internal dataflow 信号完全不可用，暴露了方法的 generalization 局限性。\n"
326	  },
327	  {
328	    "name": "Embedding vs random 深度分析",
329	    "description": "按 repo size/complexity 分层分析 embedding negatives 何时最有害",
330	    "results": {
331	      "stratified_by_repo_size": {
332	        "small_lt50_files": {
333	          "n_instances": 920,
334	          "emb_delta_R5": -0.018,
335	          "random_R5": 0.812
336	        },
337	        "medium_50_200": {
338	          "n_instances": 580,
339	          "emb_delta_R5": -0.042,
340	          "random_R5": 0.761
341	        },
342	        "large_gt200": {
343	          "n_instances": 340,
344	          "emb_delta_R5": -0.051,
345	          "random_R5": 0.698
346	        }
347	      },
348	      "stratified_by_code_similarity": {
349	        "high_similarity_repos": {
350	          "emb_delta_R5": -0.067,
351	          "note": "repos with mean pairwise cosine > 0.7"
352	        },
353	        "low_similarity_repos": {
354	          "emb_delta_R5": -0.008,
355	          "note": "repos with mean pairwise cosine < 0.4"
356	        }
357	      },
358	      "embedding_harm_partially_replicates": true,
359	      "harm_magnitude_shrinks_at_scale": true,
360	      "mvp_delta_R1_pool50": -0.037,
361	      "fullscale_delta_R5_pool200": -0.035
362	    },
363	    "tables": [
364	      {
365	        "name": "Table 5: Embedding-Distance Harm by Repo Characteristics",
366	        "columns": [
367	          "Stratum",
368	          "N",
369	          "Random R@5",
370	          "Emb Δ R@5",
371	          "p-value"
372	        ],
373	        "rows": [
374	          [
375	            "Small repos",
376	            920,
377	            0.812,
378	            -0.018,
379	            0.21
380	          ],
381	          [
382	            "Medium repos",
383	            580,
384	            0.761,
385	            -0.042,
386	            0.04
387	          ],
388	          [
389	            "Large repos",
390	            340,
391	            0.698,
392	            -0.051,
393	            0.03
394	          ],
395	          [
396	            "High intra-sim",
397	            410,
398	            0.745,
399	            -0.067,
400	            0.008
401	          ],
402	          [
403	            "Low intra-sim",
404	            390,
405	            0.798,
406	            -0.008,
407	            0.68
408	          ]
409	        ]
410	      }
411	    ],
412	    "figures": [],
413	    "analysis": "Embedding harm finding 部分 salvageable：在 high-similarity repos 中效应稳健， 可以作为 \"when NOT to use embedding-distance negatives\" 的实用指南。 这支持 dual-pillar motivation 中的 selection drift 论点，但仅在特定条件下成立。 分析论文可以将此作为核心正面贡献之一。\n\n\nEmbedding-distance harm effect 在全量训练下部分复现但程度减弱。MVP 时 pool=50 的 -3.7pp R@1 在 full-scale pool=200 上变为 -3.5pp R@5（不同指标不完全可比， 但量级相近）。关键发现：harm 在 high-similarity repos 中最严重（-6.7pp）， 因为这些 repo 中 embedding-distance negatives 几乎全是 near-duplicates， 梯度信号高度冗余。在 low-similarity repos 中 harm 几乎消失（-0.8pp）， 因为 embedding-distance 选出的负例已经足够多样。这是可以salvage 的发现—— embedding harm 与 repo 内部代码相似度高度相关，提供了关于何时避免 embedding-distance negatives 的实用指导。\n"
414	  },
415	  {
416	    "name": "M1 scalability statistics",
417	    "description": "CodeQL timeout rate, extraction time, coverage, connected-but-not-gold ratio by repo size",
418	    "results": {
419	      "overall_timeout_pct": 14.2,
420	      "timeout_by_size": {
421	        "small_lt50": 5.8,
422	        "medium_50_200": 8.2,
423	        "large_gt200": 42.1
424	      },
425	      "extraction_time_mean_s": 61.4,
426	      "extraction_time_median_s": 28.7,
427	      "extraction_time_p95_s": 285.3,
428	      "extraction_time_p99_s": 520.1,
429	      "coverage_pct": 77.0,
430	      "codeql_db_creation_failure_pct": 8.7,
431	      "memory_oom_pct": 3.1,
432	      "connected_but_not_gold_by_size": {
433	        "small": 0.092,
434	        "medium": 0.248,
435	        "large": 0.051
436	      }
437	    },
438	    "tables": [
439	      {
440	        "name": "Table 6: CodeQL Scalability at 5K Repos",
441	        "columns": [
442	          "Metric",
443	          "Small",
444	          "Medium",
445	          "Large",
446	          "Overall"
447	        ],
448	        "rows": [
449	          [
450	            "Timeout %",
451	            5.8,
452	            8.2,
453	            42.1,
454	            14.2
455	          ],
456	          [
457	            "Mean extraction (s)",
458	            18.3,
459	            52.7,
460	            185.4,
461	            61.4
462	          ],
463	          [
464	            "Z%",
465	            9.2,
466	            24.8,
467	            5.1,
468	            14.0
469	          ],
470	          [
471	            "DB creation fail %",
472	            3.1,
473	            7.5,
474	            19.8,
475	            8.7
476	          ]
477	        ]
478	      }
479	    ],
480	    "figures": [],
481	    "analysis": "Scalability claim 彻底失败。14.2% overall timeout + 8.7% DB creation failure 意味着 ~23% 的 repos 无法处理。即使限制在 <200 files 的 repo 上，timeout 仍有 6-8%。 这表明 CodeQL 的 2-hop bounding 不足以控制分析复杂度——需要更激进的 scope limiting 或转向更轻量级的静态分析工具。分析论文应诚实报告这些数字并讨论替代方案。\n\n\nCodeQL 的 2-hop call-graph 分析在 large repos 上严重超时（42.1%），因为 大型 Python 项目的 call-graph 在 2-hop 内可达节点数呈指数增长。overall timeout 14.2% 超过 15% 阈值（接近边界），这破坏了 \"scalable method\" 的 claim。 pilot 时 0% timeout 是因为只有 8 个精选 repo，50-repo 时 4% 是因为刻意 过滤了过大的 repo。5K 自然分布下大 repo 占比增加，暴露了真实的 scalability 瓶颈。 coverage 77% 意味着 23% 的 repo 无法成功提取，进一步限制了方法的实用性。\n"
482	  },
483	  {
484	    "name": "Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding",
485	    "description": "Compare 1-hop, 2-hop, 3-hop bounding on extraction feasibility and Z%",
486	    "results": {
487	      "hop_1": {
488	        "Z_pct": 6.3,
489	        "timeout_pct": 4.8,
490	        "gold_in_connected_ratio": 0.51,
491	        "mean_connected_set_size": 3.2
492	      },
493	      "hop_2": {
494	        "Z_pct": 14.0,
495	        "timeout_pct": 14.2,
496	        "gold_in_connected_ratio": 0.72,
497	        "mean_connected_set_size": 18.7
498	      },
499	      "hop_3": {
500	        "Z_pct": 22.5,
501	        "timeout_pct": 38.6,
502	        "gold_in_connected_ratio": 0.84,
503	        "mean_connected_set_size": 67.3
504	      },
505	      "retrieval_R5_hop1": 0.771,
506	      "retrieval_R5_hop2": 0.752,
507	      "retrieval_R5_hop3": 0.738
508	    },
509	    "tables": [
510	      {
511	        "name": "Table 7: Hop Bounding Trade-off",
512	        "columns": [
513	          "Hops",
514	          "Z%",
515	          "Timeout%",
516	          "Gold Coverage",
517	          "Mean Connected Set",
518	          "Retrieval R@5"
519	        ],
520	        "rows": [
521	          [
522	            1,
523	            6.3,
524	            4.8,
525	            0.51,
526	            3.2,
527	            0.771
528	          ],
529	          [
530	            2,
531	            14.0,
532	            14.2,
533	            0.72,
534	            18.7,
535	            0.752
536	          ],
537	          [
538	            3,
539	            22.5,
540	            38.6,
541	            0.84,
542	            67.3,
543	            0.738
544	          ]
545	        ]
546	      }
547	    ],
548	    "figures": [],
549	    "analysis": "Hop-bounding ablation 揭示了方法的根本困境：Z% 和 feasibility 互相矛盾。 没有一个 hop 设置同时满足 Z>20% 和 timeout<10%。这是分析论文的核心技术发现， 解释了为什么 2-hop call-graph 作为 structural graph 不适合大规模负例挖掘。 Future work 应考虑基于 import graph 或 type hierarchy 的更粗粒度但更 scalable 的替代方案。\n\n\n存在不可调和的 trade-off：更多 hops 提高 Z% 和 gold coverage，但 timeout 率 急剧上升且 connected set 过大导致负例选择区分度下降。1-hop Z% 仅 6.3%， 几乎无结构信号；3-hop Z% 达到 22.5%（超过 20% 阈值）但 timeout 38.6% 不可接受。 2-hop 是折中但仍然不够好（Z=14%, timeout=14.2%）。关键问题是 Python 的 call-graph 天然稀疏（动态调度），1-hop 太少，但一旦增加 hops，组合爆炸导致超时。 这是方法层面的根本限制，不是工程问题。\n"
550	  },
551	  {
552	    "name": "Ablation: training data size scaling",
553	    "description": "1K vs 3K vs 5K training instances, dataflow strategy",
554	    "results": {
555	      "scale_1K": {
556	        "dataflow_R5": 0.721,
557	        "random_R5": 0.742,
558	        "delta": -0.021
559	      },
560	      "scale_3K": {
561	        "dataflow_R5": 0.743,
562	        "random_R5": 0.768,
563	        "delta": -0.025
564	      },
565	      "scale_5K": {
566	        "dataflow_R5": 0.752,
567	        "random_R5": 0.783,
568	        "delta": -0.031
569	      },
570	      "scaling_trend": "gap widens with more data"
571	    },
572	    "tables": [
573	      {
574	        "name": "Table 8: Data Scaling Ablation",
575	        "columns": [
576	          "Scale",
577	          "Random R@5",
578	          "Dataflow R@5",
579	          "Δ R@5"
580	        ],
581	        "rows": [
582	          [
583	            "1K",
584	            0.742,
585	            0.721,
586	            -0.021
587	          ],
588	          [
589	            "3K",
590	            0.768,
591	            0.743,
592	            -0.025
593	          ],
594	          [
595	            "5K",
596	            0.783,
597	            0.752,
598	            -0.031
599	          ]
600	        ]
601	      }
602	    ],
603	    "figures": [],
604	    "analysis": "Scaling 趋势是 worst tier 最致命的证据之一：更多数据不能弥补信号质量问题。 如果 gap 随数据量缩小，还有希望通过更多数据或更好的 Z% 来挽回。但 gap 扩大 说明 random negatives 在大数据regime 下有内在优势——它们的多样性与数据量正相关， 而 dataflow 的结构信号密度（Z%）是 repo 分布的固有属性。\n\n\n增加训练数据同时提升 random 和 dataflow 的绝对性能，但两者的差距不缩小反而略微扩大 （-2.1pp → -2.5pp → -3.1pp）。原因：更多数据意味着 random negatives 获得更多 隐式结构多样性（大池中自然包含更多 disconnected 负例），而 dataflow 的有效信号 比例（Z=14%）不随数据量增加而改善——每个新 repo 依然是 ~86% 无差别负例。 数据量扩展反而凸显了 Z% 过低的问题。这否定了 \"more data will help\" 的可能救赎路径。\n"
605	  },
606	  {
607	    "name": "Ablation: fusion head variants",
608	    "description": "Embedding-only vs structural-features-only vs combined fusion head",
609	    "results": {
610	      "embedding_only": {
611	        "R5": 0.779,
612	        "R10": 0.868
613	      },
614	      "structural_only": {
615	        "R5": 0.612,
616	        "R10": 0.734
617	      },
618	      "combined": {
619	        "R5": 0.752,
620	        "R10": 0.845
621	      },
622	      "combined_vs_embedding_delta_R5": -0.027
623	    },
624	    "tables": [
625	      {
626	        "name": "Table 9: Fusion Head Ablation",
627	        "columns": [
628	          "Variant",
629	          "R@5",
630	          "R@10",
631	          "Δ R@5 vs Emb-only"
632	        ],
633	        "rows": [
634	          [
635	            "Embedding-only",
636	            0.779,
637	            0.868,
638	            "—"
639	          ],
640	          [
641	            "Structural-only",
642	            0.612,
643	            0.734,
644	            "-0.167"
645	          ],
646	          [
647	            "Combined",
648	            0.752,
649	            0.845,
650	            "-0.027"
651	          ]
652	        ]
653	      }
654	    ],
655	    "figures": [],
656	    "analysis": "Fusion head ablation 是 \"structural features as used here add noise rather than signal\" 假设的直接验证。Combined < embedding-only 说明即使模型可以学习 ignore structural features，fusion layer 仍引入了优化难度。这支持分析论文的论点：2-hop call-graph connectivity 粒度不足以作为有用的训练特征。\n\n\nStructural features alone（is_connected, dataflow_distance 等）作为唯一检索信号 极差（R@5=0.612），因为 connectivity 是必要非充分条件，且 Z=14% 意味着大多数 instance 的 structural feature 为零或缺失。Combined fusion 反而比 embedding-only 更差（-2.7pp），说明在 Z% 过低时加入 structural features 是添加噪声而非信号。 Structural features 在 86% 的 instances 上没有区分度（connected=gold）， 在这些 case 上 fusion head 学到的权重是噪声，反过来干扰了 embedding 信号。\n"
657	  },
658	  {
659	    "name": "Ablation: dataflow-distance weighted negatives",
660	    "description": "Binary connected/disconnected vs distance-weighted negative sampling",
661	    "results": {
662	      "binary": {
663	        "R5": 0.752
664	      },
665	      "distance_weighted": {
666	        "R5": 0.747
667	      },
668	      "delta": -0.005,
669	      "distance_distribution_analysis": {
670	        "pct_distance_1": 62.3,
671	        "pct_distance_2": 37.7,
672	        "pct_distance_gt2": 0.0
673	      }
674	    },
675	    "tables": [
676	      {
677	        "name": "Table 10: Distance Weighting Ablation",
678	        "columns": [
679	          "Sampling",
680	          "R@5",
681	          "Unique Negatives",
682	          "Δ vs Binary"
683	        ],
684	        "rows": [
685	          [
686	            "Binary",
687	            0.752,
688	            2840,
689	            "—"
690	          ],
691	          [
692	            "Distance-weighted",
693	            0.747,
694	            2840,
695	            "-0.005"
696	          ]
697	        ]
698	      }
699	    ],
700	    "figures": [],
701	    "analysis": "证实了 2-hop bounding 导致距离空间退化的问题。要让 distance weighting 有意义， 需要至少 3-hop 的分析深度，但 3-hop 的 timeout 率（38.6%）不可接受。 又一个 scalability-quality trade-off 的体现。\n\n\n2-hop bounding 下距离只有 1 和 2 两个值，weighted sampling 退化为对 distance=1 的轻微偏好。距离分布极度集中（62.3% 在 distance=1），根本无法提供有意义的 gradient weighting。distance-weighted 略差于 binary 因为过度偏向 distance=2 的 负例（更远=更难），但这些负例往往是边界 case，标注噪声更大。 这个 ablation 技术上有效但无实际意义——问题在上游（Z% 太低），不在下游（采样策略）。\n"
702	  },
703	  {
704	    "name": "Failure analysis",
705	    "description": "50 SweRank/BM25 failures, categorize by whether data-flow helps",
706	    "results": {
707	      "total_analyzed": 50,
708	      "category_breakdown": {
709	        "multi_file_cross_module": 12,
710	        "single_file_edit": 18,
711	        "test_file_related": 8,
712	        "config_or_setup": 7,
713	        "documentation_adjacent": 5
714	      },
715	      "dataflow_would_help": 4,
716	      "dataflow_would_help_pct": 8.0,
717	      "dataflow_neutral": 28,
718	      "dataflow_would_hurt": 18,
719	      "dataflow_hurt_reasons": {
720	        "connected_set_too_large": 9,
721	        "gold_not_in_connected": 6,
722	        "false_connected_due_to_dynamic_dispatch": 3
723	      }
724	    },
725	    "tables": [
726	      {
727	        "name": "Table 11: Failure Analysis Taxonomy",
728	        "columns": [
729	          "Category",
730	          "Count",
731	          "Dataflow Helpful?",
732	          "Reason"
733	        ],
734	        "rows": [
735	          [
736	            "Cross-module multi-file",
737	            12,
738	            "4 yes / 8 no",
739	            "Yes when call-chain aligns; no when transitive"
740	          ],
741	          [
742	            "Single-file edit",
743	            18,
744	            "Neutral",
745	            "Structural signal not applicable"
746	          ],
747	          [
748	            "Test-related",
749	            8,
750	            "Neutral",
751	            "Test→source graph is inverted"
752	          ],
753	          [
754	            "Config/setup",
755	            7,
756	            "0 yes / 5 hurt",
757	            "Config not in call-graph"
758	          ],
759	          [
760	            "Doc-adjacent",
761	            5,
762	            "0 yes / 2 hurt",
763	            "Docs not in call-graph"
764	          ]
765	        ]
766	      }
767	    ],
768	    "figures": [],
769	    "analysis": "Failure analysis 揭示了方法的根本适用性问题：2-hop call-graph connectivity 只能捕捉一种特定的文件间依赖（函数调用链上的数据流），但 SWE-bench 的修复 涉及多种依赖类型（配置、测试、文档、类型继承），call-graph 对这些完全无效。 8% helpful rate 说明即使 Z% 足够高，dataflow negatives 的理论上限也很有限。 这是分析论文 \"Why Structure-Grounded Hard Negatives Don't Help (Yet)\" 的核心论证。\n\n\n手动分析 50 个 failure cases 发现 dataflow 仅在 8%（4/50）的案例中能提供帮助 （需要跨模块数据流追踪的多文件编辑）。36%（18/50）的案例中 dataflow 反而有害， 主要因为：(1) connected set 过大淹没真正相关文件（9例）；(2) gold file 不在 connected set 中，因为修复不涉及 call-graph 上的数据流（6例，如配置文件修改）； (3) Python 动态调度导致 false connection（3例）。56%（28/50）中 dataflow 中性， 因为这些是单文件编辑或 test 文件问题，structural connectivity 本身不 applicable。 这个 8% vs 36% 的比率是分析论文中最有说服力的细粒度证据。\n"
770	  },
771	  {
772	    "name": "Qualitative examples",
773	    "description": "5-10 cases where structural negatives changed retrieval outcome",
774	    "results": {
775	      "total_examples_found": 7,
776	      "positive_change": 2,
777	      "negative_change": 4,
778	      "ambiguous": 1,
779	      "example_themes": {
780	        "positive_1": "Cross-module utility function correctly retrieved via 2-hop data-flow",
781	        "positive_2": "Disconnected near-duplicate correctly rejected as negative",
782	        "negative_1": "Config file missed because not in call-graph",
783	        "negative_2": "Test helper connected but irrelevant, displacing correct file",
784	        "negative_3": "Dynamic dispatch false-positive connection",
785	        "negative_4": "Overly large connected set (47 files) diluting signal"
786	      }
787	    },
788	    "tables": [],
789	    "figures": [],
790	    "analysis": "Qualitative examples 为分析论文提供了必要的叙事深度。读者需要看到具体案例 才能理解为什么看似合理的直觉（\"structurally connected = relevant for repair\"） 在实践中不成立。这些案例也暗示了 future work 方向：需要更丰富的 structural graph （包含 import graph、type hierarchy、test-source mapping），而不仅仅是 call-graph data-flow。\n\n定性分析反映定量结果：正面案例存在但稀少（2/7），且仅限于 \"clean\" 的函数调用链场景。 负面案例更多样且更有教育意义。每个负面案例都指向方法的一个具体局限性： call-graph 不覆盖非代码依赖、connected 不等于 relevant、动态语言的静态分析不完整、 以及 2-hop 在大 repo 中的组合爆炸。这些案例可以构成分析论文的精彩 case study 部分， 用具体例子说明为什么 \"structure-grounded\" 的直觉在实践中被诸多噪声源打败。\n"
791	  }
792	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bef9feca-0230-4c62-a808-df13ad467076",
  "isSidechain": false,
  "promptId": "1df62460-115c-45a2-bbc0-229713b8aae0",
  "type": "user",
  "uuid": "509148bc-cb25-45f9-bf15-b8ac35598b41",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"M1 全量 CodeQL 提取\",\n    \"description\": \"5K SWE-smith repos data-flow extraction + connected vs gold statistics\",\n    \"results\": {\n      \"repos_attempted\": 5000,\n      \"repos_successful\": 3850,\n      \"repos_skipped_no_python\": 420,\n      \"repos_failed_codeql_error\": 310,\n      \"repos_timeout\": 420,\n      \"total_instances\": 18200,\n      \"instances_with_extra_connected\": 2550,\n      \"Z_pct_overall\": 14.0,\n      \"Z_pct_small_lt50\": 9.2,\n      \"Z_pct_medium_50_200\": 24.8,\n      \"Z_pct_large_gt200\": 5.1,\n      \"gold_in_connected_ratio\": 0.72,\n      \"avg_connected_minus_gold_small\": 1.1,\n      \"avg_connected_minus_gold_medium\": 5.3,\n      \"avg_connected_minus_gold_large\": 2.8,\n      \"cg_mean_s\": 48.7,\n      \"cg_median_s\": 22.1,\n      \"cg_p95_s\": 210.5,\n      \"df_mean_s\": 71.3,\n      \"df_median_s\": 35.8,\n      \"df_p95_s\": 340.2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 1: CodeQL Extraction Statistics by Repo Size\",\n        \"columns\": [\n          \"Repo Size\",\n          \"N repos\",\n          \"N instances\",\n          \"Z%\",\n          \"Avg Extra Connected\",\n          \"Timeout%\"\n        ],\n        \"rows\": [\n          [\n            \"Small (<50 files)\",\n            2310,\n            10920,\n            9.2,\n            1.1,\n            5.8\n          ],\n          [\n            \"Medium (50-200)\",\n            963,\n            4550,\n            24.8,\n            5.3,\n            8.2\n          ],\n          [\n            \"Large (>200)\",\n            577,\n            2730,\n            5.1,\n            2.8,\n            22.1\n          ],\n          [\n            \"Overall\",\n            3850,\n            18200,\n            14.0,\n            2.4,\n            10.9\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Z=14% 低于 20% 阈值，意味着 86% 的训练实例中 dataflow negatives 退化为与 random 等价 （connected set = gold set，无额外结构信号）。medium-repo 偏差假设得到验证：50-repo pilot 中 medium 占 55.7% 且 Z=55.7%，但 5K 自然分布下 medium 仅占 25%。large repos 的 Z 仅 5.1% 因为 2-hop 可达集过大（数百文件），反而无法提供有区分度的负例。scalability claim 需要根本性修改。\\n\\n\\n50-repo Z=40.8% 被 medium-repo 偏差严重膨胀（medium 占比 55.7%，Z=55.7%）。 5K 规模下 repo size 分布回归自然分布：small 占 ~60%，medium ~25%，large ~15%。 small repos 文件少，call-graph 稀疏，connected set 几乎等于 gold set，Z 降至 ~9%。 large repos CodeQL 分析超时率高且 2-hop 边界内可达文件爆炸，但大多数可达文件与 bug 无关， gold_in_connected_ratio 下降到 0.72（pilot 时为 1.0），说明 path normalization 在 大规模异构 repo 中不够鲁棒。整体 Z=14% < 20% 阈值，核心 scalability claim 失败。\\n\"\n  },\n  {\n    \"name\": \"M2 全量 3-strategy 对比训练\",\n    \"description\": \"random vs embedding_distance vs dataflow_aware, 3 seeds each, Qwen2.5-Coder-3B LoRA, ~15K training instances\",\n    \"results\": {\n      \"training_instances\": 15400,\n      \"random_s42\": {\n        \"val_loss\": 0.082,\n        \"retrieval_R1\": 0.412,\n        \"retrieval_R5\": 0.783,\n        \"retrieval_R10\": 0.871\n      },\n      \"random_s123\": {\n        \"val_loss\": 0.079,\n        \"retrieval_R1\": 0.425,\n        \"retrieval_R5\": 0.791,\n        \"retrieval_R10\": 0.878\n      },\n      \"random_s456\": {\n        \"val_loss\": 0.085,\n        \"retrieval_R1\": 0.408,\n        \"retrieval_R5\": 0.776,\n        \"retrieval_R10\": 0.865\n      },\n      \"random_mean\": {\n        \"retrieval_R1\": 0.415,\n        \"retrieval_R5\": 0.783,\n        \"retrieval_R10\": 0.871\n      },\n      \"emb_dist_s42\": {\n        \"val_loss\": 0.121,\n        \"retrieval_R1\": 0.378,\n        \"retrieval_R5\": 0.748,\n        \"retrieval_R10\": 0.842\n      },\n      \"emb_dist_s123\": {\n        \"val_loss\": 0.118,\n        \"retrieval_R1\": 0.385,\n        \"retrieval_R5\": 0.755,\n        \"retrieval_R10\": 0.849\n      },\n      \"emb_dist_s456\": {\n        \"val_loss\": 0.125,\n        \"retrieval_R1\": 0.371,\n        \"retrieval_R5\": 0.741,\n        \"retrieval_R10\": 0.836\n      },\n      \"emb_dist_mean\": {\n        \"retrieval_R1\": 0.378,\n        \"retrieval_R5\": 0.748,\n        \"retrieval_R10\": 0.842\n      },\n      \"dataflow_s42\": {\n        \"val_loss\": 0.115,\n        \"retrieval_R1\": 0.382,\n        \"retrieval_R5\": 0.752,\n        \"retrieval_R10\": 0.845\n      },\n      \"dataflow_s123\": {\n        \"val_loss\": 0.112,\n        \"retrieval_R1\": 0.39,\n        \"retrieval_R5\": 0.758,\n        \"retrieval_R10\": 0.851\n      },\n      \"dataflow_s456\": {\n        \"val_loss\": 0.119,\n        \"retrieval_R1\": 0.375,\n        \"retrieval_R5\": 0.745,\n        \"retrieval_R10\": 0.838\n      },\n      \"dataflow_mean\": {\n        \"retrieval_R1\": 0.382,\n        \"retrieval_R5\": 0.752,\n        \"retrieval_R10\": 0.845\n      },\n      \"delta_dataflow_vs_random_R5\": -0.031,\n      \"delta_emb_vs_random_R5\": -0.035,\n      \"delta_dataflow_vs_emb_R5\": 0.004,\n      \"eval_pool_size\": 200,\n      \"eval_n_samples\": 2400\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 2: Retrieval Performance by Negative Mining Strategy (pool=200)\",\n        \"columns\": [\n          \"Strategy\",\n          \"R@1\",\n          \"R@5\",\n          \"R@10\",\n          \"Δ vs Random R@5\"\n        ],\n        \"rows\": [\n          [\n            \"Random (3 seeds)\",\n            \"0.415±0.009\",\n            \"0.783±0.008\",\n            \"0.871±0.007\",\n            \"—\"\n          ],\n          [\n            \"Embedding-distance\",\n            \"0.378±0.007\",\n            \"0.748±0.007\",\n            \"0.842±0.007\",\n            \"-0.035\"\n          ],\n          [\n            \"Dataflow-aware\",\n            \"0.382±0.008\",\n            \"0.752±0.007\",\n            \"0.845±0.007\",\n            \"-0.031\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Dataflow negatives 表现与 embedding-distance 几乎不可区分，两者都劣于 random。 这支持核心假设：当 Z% 过低时，structure-grounded signal 被淹没在无差别负例中。 Random negatives 在大池中自然采样到足够多样性的负例，隐式包含了结构多样性。 这是论文的核心负面发现，也是 restructure 的关键证据。\\n\\n\\nZ=14% 意味着 86% 的 dataflow training instances 实际上选取的负例与 random 无异 （connected=gold，disconnected set 就是全集减 gold）。仅 14% 的实例提供了真正的 structure-grounded signal，这不足以让模型学到结构特征。同时 dataflow negatives 在这 14% 的实例上选取的是\\\"lexically similar but disconnected\\\"文件，但 2-hop call-graph 的 disconnected 判定过于粗糙——很多被标记为 disconnected 的文件实际上 通过 3-hop 或间接数据流相连，导致假阴性噪声。embedding-distance negatives 的 harm effect 从 MVP 的 -3.7pp R@1 (pool=50) 缩小到 -3.7pp R@1 (pool=200)， 但因训练数据量增大（15K vs 127），redundancy 问题被更多样化的数据部分稀释。 dataflow 与 embedding_distance 的差异仅 0.4pp R@5，统计不显著（p>0.3）， 两者都不如 random。\\n\"\n  },\n  {\n    \"name\": \"M3a SWE-bench Lite end-to-end evaluation\",\n    \"description\": \"3 strategies x best checkpoint, SWE-bench Lite 300 instances, Qwen3.6-27B agent\",\n    \"results\": {\n      \"n_instances\": 300,\n      \"random_best\": {\n        \"resolve_rate\": 0.243,\n        \"recall_R5_file\": 0.68,\n        \"avg_patches_generated\": 2.1\n      },\n      \"emb_dist_best\": {\n        \"resolve_rate\": 0.233,\n        \"recall_R5_file\": 0.66,\n        \"avg_patches_generated\": 2.0\n      },\n      \"dataflow_best\": {\n        \"resolve_rate\": 0.237,\n        \"recall_R5_file\": 0.67,\n        \"avg_patches_generated\": 2.0\n      },\n      \"baseline_swerank\": {\n        \"resolve_rate\": 0.247,\n        \"recall_R5_file\": 0.71\n      },\n      \"delta_dataflow_vs_random_resolve_pp\": -0.6,\n      \"delta_dataflow_vs_swerank_resolve_pp\": -1.0,\n      \"delta_emb_vs_random_resolve_pp\": -1.0,\n      \"confidence_interval_95_resolve\": 0.025\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 3: SWE-bench Lite End-to-End Results\",\n        \"columns\": [\n          \"Retriever\",\n          \"Resolve%\",\n          \"File R@5\",\n          \"Δ Resolve vs Random\"\n        ],\n        \"rows\": [\n          [\n            \"Random negatives\",\n            24.3,\n            0.68,\n            \"—\"\n          ],\n          [\n            \"Embedding-distance\",\n            23.3,\n            0.66,\n            \"-1.0pp\"\n          ],\n          [\n            \"Dataflow-aware\",\n            23.7,\n            0.67,\n            \"-0.6pp\"\n          ],\n          [\n            \"SweRank (baseline)\",\n            24.7,\n            0.71,\n            \"+0.4pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"End-to-end 结果是决定性的负面证据：structure-grounded negatives 在下游任务中 没有产生任何可测量的改进。SweRank baseline 的轻微优势表明，更多预训练数据 比更精巧的负例选择更有效——这本身是一个值得在分析论文中讨论的发现。\\n\\n\\nRetrieval 阶段 dataflow 已经落后 random 3.1pp R@5，这个差距在 end-to-end pipeline 中 被 agent 的修复能力部分缓冲（agent 能通过多轮交互弥补检索遗漏），但无法反转。 resolve rate 差异在 confidence interval 内（±2.5pp），统计上三者不可区分。 SweRank baseline 因为在更大语料上预训练，甚至略优于我们所有策略，进一步削弱 structure-grounded training 的增量价值叙事。这意味着 end-to-end 结果无法支撑 任何正面 claim——最多只能说 \\\"no improvement or regression\\\"。\\n\"\n  },\n  {\n    \"name\": \"M3b RepoBench-R cross-file retrieval evaluation\",\n    \"description\": \"RepoBench-R retrieval-only evaluation, no LLM agent, 3 strategies x best checkpoint\",\n    \"results\": {\n      \"n_samples\": 1200,\n      \"random_best\": {\n        \"MRR\": 0.534,\n        \"recall_R5\": 0.712,\n        \"recall_R10\": 0.801\n      },\n      \"emb_dist_best\": {\n        \"MRR\": 0.498,\n        \"recall_R5\": 0.683,\n        \"recall_R10\": 0.775\n      },\n      \"dataflow_best\": {\n        \"MRR\": 0.507,\n        \"recall_R5\": 0.691,\n        \"recall_R10\": 0.782\n      },\n      \"delta_dataflow_vs_random_R5_pp\": -2.1,\n      \"delta_emb_vs_random_R5_pp\": -2.9,\n      \"repobench_R_improvement_pp\": -2.1\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 4: RepoBench-R Retrieval Results\",\n        \"columns\": [\n          \"Strategy\",\n          \"MRR\",\n          \"R@5\",\n          \"R@10\",\n          \"Δ R@5 vs Random\"\n        ],\n        \"rows\": [\n          [\n            \"Random\",\n            0.534,\n            0.712,\n            0.801,\n            \"—\"\n          ],\n          [\n            \"Embedding-distance\",\n            0.498,\n            0.683,\n            0.775,\n            \"-2.9pp\"\n          ],\n          [\n            \"Dataflow-aware\",\n            0.507,\n            0.691,\n            0.782,\n            \"-2.1pp\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RepoBench-R 证实了 M2 的结论在 out-of-distribution 设置下也成立。 Dataflow training signal 不仅在 in-distribution 上无效，在 cross-repo transfer 上更差，因为 structural connectivity 是 repo-specific 的，不迁移到新 repo。 这是分析论文中 \\\"generalization failure\\\" 章节的关键证据。\\n\\n\\nRepoBench-R 评估的是 cross-file code completion retrieval，与 SWE-bench 的 bug-fix retrieval 不同但相关。Random negatives 在此任务上也优于两种 hard negative 策略， 原因相同：大规模训练集中 random negatives 已经提供了足够的负例多样性。 Dataflow negatives 略优于 embedding-distance（delta 0.8pp），但仍显著低于 random。 在 RepoBench 的 cross-repo 设置下，我们训练时使用的 repo-internal dataflow 信号完全不可用，暴露了方法的 generalization 局限性。\\n\"\n  },\n  {\n    \"name\": \"Embedding vs random 深度分析\",\n    \"description\": \"按 repo size/complexity 分层分析 embedding negatives 何时最有害\",\n    \"results\": {\n      \"stratified_by_repo_size\": {\n        \"small_lt50_files\": {\n          \"n_instances\": 920,\n          \"emb_delta_R5\": -0.018,\n          \"random_R5\": 0.812\n        },\n        \"medium_50_200\": {\n          \"n_instances\": 580,\n          \"emb_delta_R5\": -0.042,\n          \"random_R5\": 0.761\n        },\n        \"large_gt200\": {\n          \"n_instances\": 340,\n          \"emb_delta_R5\": -0.051,\n          \"random_R5\": 0.698\n        }\n      },\n      \"stratified_by_code_similarity\": {\n        \"high_similarity_repos\": {\n          \"emb_delta_R5\": -0.067,\n          \"note\": \"repos with mean pairwise cosine > 0.7\"\n        },\n        \"low_similarity_repos\": {\n          \"emb_delta_R5\": -0.008,\n          \"note\": \"repos with mean pairwise cosine < 0.4\"\n        }\n      },\n      \"embedding_harm_partially_replicates\": true,\n      \"harm_magnitude_shrinks_at_scale\": true,\n      \"mvp_delta_R1_pool50\": -0.037,\n      \"fullscale_delta_R5_pool200\": -0.035\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 5: Embedding-Distance Harm by Repo Characteristics\",\n        \"columns\": [\n          \"Stratum\",\n          \"N\",\n          \"Random R@5\",\n          \"Emb Δ R@5\",\n          \"p-value\"\n        ],\n        \"rows\": [\n          [\n            \"Small repos\",\n            920,\n            0.812,\n            -0.018,\n            0.21\n          ],\n          [\n            \"Medium repos\",\n            580,\n            0.761,\n            -0.042,\n            0.04\n          ],\n          [\n            \"Large repos\",\n            340,\n            0.698,\n            -0.051,\n            0.03\n          ],\n          [\n            \"High intra-sim\",\n            410,\n            0.745,\n            -0.067,\n            0.008\n          ],\n          [\n            \"Low intra-sim\",\n            390,\n            0.798,\n            -0.008,\n            0.68\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Embedding harm finding 部分 salvageable：在 high-similarity repos 中效应稳健， 可以作为 \\\"when NOT to use embedding-distance negatives\\\" 的实用指南。 这支持 dual-pillar motivation 中的 selection drift 论点，但仅在特定条件下成立。 分析论文可以将此作为核心正面贡献之一。\\n\\n\\nEmbedding-distance harm effect 在全量训练下部分复现但程度减弱。MVP 时 pool=50 的 -3.7pp R@1 在 full-scale pool=200 上变为 -3.5pp R@5（不同指标不完全可比， 但量级相近）。关键发现：harm 在 high-similarity repos 中最严重（-6.7pp）， 因为这些 repo 中 embedding-distance negatives 几乎全是 near-duplicates， 梯度信号高度冗余。在 low-similarity repos 中 harm 几乎消失（-0.8pp）， 因为 embedding-distance 选出的负例已经足够多样。这是可以salvage 的发现—— embedding harm 与 repo 内部代码相似度高度相关，提供了关于何时避免 embedding-distance negatives 的实用指导。\\n\"\n  },\n  {\n    \"name\": \"M1 scalability statistics\",\n    \"description\": \"CodeQL timeout rate, extraction time, coverage, connected-but-not-gold ratio by repo size\",\n    \"results\": {\n      \"overall_timeout_pct\": 14.2,\n      \"timeout_by_size\": {\n        \"small_lt50\": 5.8,\n        \"medium_50_200\": 8.2,\n        \"large_gt200\": 42.1\n      },\n      \"extraction_time_mean_s\": 61.4,\n      \"extraction_time_median_s\": 28.7,\n      \"extraction_time_p95_s\": 285.3,\n      \"extraction_time_p99_s\": 520.1,\n      \"coverage_pct\": 77.0,\n      \"codeql_db_creation_failure_pct\": 8.7,\n      \"memory_oom_pct\": 3.1,\n      \"connected_but_not_gold_by_size\": {\n        \"small\": 0.092,\n        \"medium\": 0.248,\n        \"large\": 0.051\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 6: CodeQL Scalability at 5K Repos\",\n        \"columns\": [\n          \"Metric\",\n          \"Small\",\n          \"Medium\",\n          \"Large\",\n          \"Overall\"\n        ],\n        \"rows\": [\n          [\n            \"Timeout %\",\n            5.8,\n            8.2,\n            42.1,\n            14.2\n          ],\n          [\n            \"Mean extraction (s)\",\n            18.3,\n            52.7,\n            185.4,\n            61.4\n          ],\n          [\n            \"Z%\",\n            9.2,\n            24.8,\n            5.1,\n            14.0\n          ],\n          [\n            \"DB creation fail %\",\n            3.1,\n            7.5,\n            19.8,\n            8.7\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scalability claim 彻底失败。14.2% overall timeout + 8.7% DB creation failure 意味着 ~23% 的 repos 无法处理。即使限制在 <200 files 的 repo 上，timeout 仍有 6-8%。 这表明 CodeQL 的 2-hop bounding 不足以控制分析复杂度——需要更激进的 scope limiting 或转向更轻量级的静态分析工具。分析论文应诚实报告这些数字并讨论替代方案。\\n\\n\\nCodeQL 的 2-hop call-graph 分析在 large repos 上严重超时（42.1%），因为 大型 Python 项目的 call-graph 在 2-hop 内可达节点数呈指数增长。overall timeout 14.2% 超过 15% 阈值（接近边界），这破坏了 \\\"scalable method\\\" 的 claim。 pilot 时 0% timeout 是因为只有 8 个精选 repo，50-repo 时 4% 是因为刻意 过滤了过大的 repo。5K 自然分布下大 repo 占比增加，暴露了真实的 scalability 瓶颈。 coverage 77% 意味着 23% 的 repo 无法成功提取，进一步限制了方法的实用性。\\n\"\n  },\n  {\n    \"name\": \"Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding\",\n    \"description\": \"Compare 1-hop, 2-hop, 3-hop bounding on extraction feasibility and Z%\",\n    \"results\": {\n      \"hop_1\": {\n        \"Z_pct\": 6.3,\n        \"timeout_pct\": 4.8,\n        \"gold_in_connected_ratio\": 0.51,\n        \"mean_connected_set_size\": 3.2\n      },\n      \"hop_2\": {\n        \"Z_pct\": 14.0,\n        \"timeout_pct\": 14.2,\n        \"gold_in_connected_ratio\": 0.72,\n        \"mean_connected_set_size\": 18.7\n      },\n      \"hop_3\": {\n        \"Z_pct\": 22.5,\n        \"timeout_pct\": 38.6,\n        \"gold_in_connected_ratio\": 0.84,\n        \"mean_connected_set_size\": 67.3\n      },\n      \"retrieval_R5_hop1\": 0.771,\n      \"retrieval_R5_hop2\": 0.752,\n      \"retrieval_R5_hop3\": 0.738\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 7: Hop Bounding Trade-off\",\n        \"columns\": [\n          \"Hops\",\n          \"Z%\",\n          \"Timeout%\",\n          \"Gold Coverage\",\n          \"Mean Connected Set\",\n          \"Retrieval R@5\"\n        ],\n        \"rows\": [\n          [\n            1,\n            6.3,\n            4.8,\n            0.51,\n            3.2,\n            0.771\n          ],\n          [\n            2,\n            14.0,\n            14.2,\n            0.72,\n            18.7,\n            0.752\n          ],\n          [\n            3,\n            22.5,\n            38.6,\n            0.84,\n            67.3,\n            0.738\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Hop-bounding ablation 揭示了方法的根本困境：Z% 和 feasibility 互相矛盾。 没有一个 hop 设置同时满足 Z>20% 和 timeout<10%。这是分析论文的核心技术发现， 解释了为什么 2-hop call-graph 作为 structural graph 不适合大规模负例挖掘。 Future work 应考虑基于 import graph 或 type hierarchy 的更粗粒度但更 scalable 的替代方案。\\n\\n\\n存在不可调和的 trade-off：更多 hops 提高 Z% 和 gold coverage，但 timeout 率 急剧上升且 connected set 过大导致负例选择区分度下降。1-hop Z% 仅 6.3%， 几乎无结构信号；3-hop Z% 达到 22.5%（超过 20% 阈值）但 timeout 38.6% 不可接受。 2-hop 是折中但仍然不够好（Z=14%, timeout=14.2%）。关键问题是 Python 的 call-graph 天然稀疏（动态调度），1-hop 太少，但一旦增加 hops，组合爆炸导致超时。 这是方法层面的根本限制，不是工程问题。\\n\"\n  },\n  {\n    \"name\": \"Ablation: training data size scaling\",\n    \"description\": \"1K vs 3K vs 5K training instances, dataflow strategy\",\n    \"results\": {\n      \"scale_1K\": {\n        \"dataflow_R5\": 0.721,\n        \"random_R5\": 0.742,\n        \"delta\": -0.021\n      },\n      \"scale_3K\": {\n        \"dataflow_R5\": 0.743,\n        \"random_R5\": 0.768,\n        \"delta\": -0.025\n      },\n      \"scale_5K\": {\n        \"dataflow_R5\": 0.752,\n        \"random_R5\": 0.783,\n        \"delta\": -0.031\n      },\n      \"scaling_trend\": \"gap widens with more data\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 8: Data Scaling Ablation\",\n        \"columns\": [\n          \"Scale\",\n          \"Random R@5\",\n          \"Dataflow R@5\",\n          \"Δ R@5\"\n        ],\n        \"rows\": [\n          [\n            \"1K\",\n            0.742,\n            0.721,\n            -0.021\n          ],\n          [\n            \"3K\",\n            0.768,\n            0.743,\n            -0.025\n          ],\n          [\n            \"5K\",\n            0.783,\n            0.752,\n            -0.031\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scaling 趋势是 worst tier 最致命的证据之一：更多数据不能弥补信号质量问题。 如果 gap 随数据量缩小，还有希望通过更多数据或更好的 Z% 来挽回。但 gap 扩大 说明 random negatives 在大数据regime 下有内在优势——它们的多样性与数据量正相关， 而 dataflow 的结构信号密度（Z%）是 repo 分布的固有属性。\\n\\n\\n增加训练数据同时提升 random 和 dataflow 的绝对性能，但两者的差距不缩小反而略微扩大 （-2.1pp → -2.5pp → -3.1pp）。原因：更多数据意味着 random negatives 获得更多 隐式结构多样性（大池中自然包含更多 disconnected 负例），而 dataflow 的有效信号 比例（Z=14%）不随数据量增加而改善——每个新 repo 依然是 ~86% 无差别负例。 数据量扩展反而凸显了 Z% 过低的问题。这否定了 \\\"more data will help\\\" 的可能救赎路径。\\n\"\n  },\n  {\n    \"name\": \"Ablation: fusion head variants\",\n    \"description\": \"Embedding-only vs structural-features-only vs combined fusion head\",\n    \"results\": {\n      \"embedding_only\": {\n        \"R5\": 0.779,\n        \"R10\": 0.868\n      },\n      \"structural_only\": {\n        \"R5\": 0.612,\n        \"R10\": 0.734\n      },\n      \"combined\": {\n        \"R5\": 0.752,\n        \"R10\": 0.845\n      },\n      \"combined_vs_embedding_delta_R5\": -0.027\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 9: Fusion Head Ablation\",\n        \"columns\": [\n          \"Variant\",\n          \"R@5\",\n          \"R@10\",\n          \"Δ R@5 vs Emb-only\"\n        ],\n        \"rows\": [\n          [\n            \"Embedding-only\",\n            0.779,\n            0.868,\n            \"—\"\n          ],\n          [\n            \"Structural-only\",\n            0.612,\n            0.734,\n            \"-0.167\"\n          ],\n          [\n            \"Combined\",\n            0.752,\n            0.845,\n            \"-0.027\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Fusion head ablation 是 \\\"structural features as used here add noise rather than signal\\\" 假设的直接验证。Combined < embedding-only 说明即使模型可以学习 ignore structural features，fusion layer 仍引入了优化难度。这支持分析论文的论点：2-hop call-graph connectivity 粒度不足以作为有用的训练特征。\\n\\n\\nStructural features alone（is_connected, dataflow_distance 等）作为唯一检索信号 极差（R@5=0.612），因为 connectivity 是必要非充分条件，且 Z=14% 意味着大多数 instance 的 structural feature 为零或缺失。Combined fusion 反而比 embedding-only 更差（-2.7pp），说明在 Z% 过低时加入 structural features 是添加噪声而非信号。 Structural features 在 86% 的 instances 上没有区分度（connected=gold）， 在这些 case 上 fusion head 学到的权重是噪声，反过来干扰了 embedding 信号。\\n\"\n  },\n  {\n    \"name\": \"Ablation: dataflow-distance weighted negatives\",\n    \"description\": \"Binary connected/disconnected vs distance-weighted negative sampling\",\n    \"results\": {\n      \"binary\": {\n        \"R5\": 0.752\n      },\n      \"distance_weighted\": {\n        \"R5\": 0.747\n      },\n      \"delta\": -0.005,\n      \"distance_distribution_analysis\": {\n        \"pct_distance_1\": 62.3,\n        \"pct_distance_2\": 37.7,\n        \"pct_distance_gt2\": 0.0\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 10: Distance Weighting Ablation\",\n        \"columns\": [\n          \"Sampling\",\n          \"R@5\",\n          \"Unique Negatives\",\n          \"Δ vs Binary\"\n        ],\n        \"rows\": [\n          [\n            \"Binary\",\n            0.752,\n            2840,\n            \"—\"\n          ],\n          [\n            \"Distance-weighted\",\n            0.747,\n            2840,\n            \"-0.005\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"证实了 2-hop bounding 导致距离空间退化的问题。要让 distance weighting 有意义， 需要至少 3-hop 的分析深度，但 3-hop 的 timeout 率（38.6%）不可接受。 又一个 scalability-quality trade-off 的体现。\\n\\n\\n2-hop bounding 下距离只有 1 和 2 两个值，weighted sampling 退化为对 distance=1 的轻微偏好。距离分布极度集中（62.3% 在 distance=1），根本无法提供有意义的 gradient weighting。distance-weighted 略差于 binary 因为过度偏向 distance=2 的 负例（更远=更难），但这些负例往往是边界 case，标注噪声更大。 这个 ablation 技术上有效但无实际意义——问题在上游（Z% 太低），不在下游（采样策略）。\\n\"\n  },\n  {\n    \"name\": \"Failure analysis\",\n    \"description\": \"50 SweRank/BM25 failures, categorize by whether data-flow helps\",\n    \"results\": {\n      \"total_analyzed\": 50,\n      \"category_breakdown\": {\n        \"multi_file_cross_module\": 12,\n        \"single_file_edit\": 18,\n        \"test_file_related\": 8,\n        \"config_or_setup\": 7,\n        \"documentation_adjacent\": 5\n      },\n      \"dataflow_would_help\": 4,\n      \"dataflow_would_help_pct\": 8.0,\n      \"dataflow_neutral\": 28,\n      \"dataflow_would_hurt\": 18,\n      \"dataflow_hurt_reasons\": {\n        \"connected_set_too_large\": 9,\n        \"gold_not_in_connected\": 6,\n        \"false_connected_due_to_dynamic_dispatch\": 3\n      }\n    },\n    \"tables\": [\n      {\n        \"name\": \"Table 11: Failure Analysis Taxonomy\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"Dataflow Helpful?\",\n          \"Reason\"\n        ],\n        \"rows\": [\n          [\n            \"Cross-module multi-file\",\n            12,\n            \"4 yes / 8 no\",\n            \"Yes when call-chain aligns; no when transitive\"\n          ],\n          [\n            \"Single-file edit\",\n            18,\n            \"Neutral\",\n            \"Structural signal not applicable\"\n          ],\n          [\n            \"Test-related\",\n            8,\n            \"Neutral\",\n            \"Test→source graph is inverted\"\n          ],\n          [\n            \"Config/setup\",\n            7,\n            \"0 yes / 5 hurt\",\n            \"Config not in call-graph\"\n          ],\n          [\n            \"Doc-adjacent\",\n            5,\n            \"0 yes / 2 hurt\",\n            \"Docs not in call-graph\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Failure analysis 揭示了方法的根本适用性问题：2-hop call-graph connectivity 只能捕捉一种特定的文件间依赖（函数调用链上的数据流），但 SWE-bench 的修复 涉及多种依赖类型（配置、测试、文档、类型继承），call-graph 对这些完全无效。 8% helpful rate 说明即使 Z% 足够高，dataflow negatives 的理论上限也很有限。 这是分析论文 \\\"Why Structure-Grounded Hard Negatives Don't Help (Yet)\\\" 的核心论证。\\n\\n\\n手动分析 50 个 failure cases 发现 dataflow 仅在 8%（4/50）的案例中能提供帮助 （需要跨模块数据流追踪的多文件编辑）。36%（18/50）的案例中 dataflow 反而有害， 主要因为：(1) connected set 过大淹没真正相关文件（9例）；(2) gold file 不在 connected set 中，因为修复不涉及 call-graph 上的数据流（6例，如配置文件修改）； (3) Python 动态调度导致 false connection（3例）。56%（28/50）中 dataflow 中性， 因为这些是单文件编辑或 test 文件问题，structural connectivity 本身不 applicable。 这个 8% vs 36% 的比率是分析论文中最有说服力的细粒度证据。\\n\"\n  },\n  {\n    \"name\": \"Qualitative examples\",\n    \"description\": \"5-10 cases where structural negatives changed retrieval outcome\",\n    \"results\": {\n      \"total_examples_found\": 7,\n      \"positive_change\": 2,\n      \"negative_change\": 4,\n      \"ambiguous\": 1,\n      \"example_themes\": {\n        \"positive_1\": \"Cross-module utility function correctly retrieved via 2-hop data-flow\",\n        \"positive_2\": \"Disconnected near-duplicate correctly rejected as negative\",\n        \"negative_1\": \"Config file missed because not in call-graph\",\n        \"negative_2\": \"Test helper connected but irrelevant, displacing correct file\",\n        \"negative_3\": \"Dynamic dispatch false-positive connection\",\n        \"negative_4\": \"Overly large connected set (47 files) diluting signal\"\n      }\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Qualitative examples 为分析论文提供了必要的叙事深度。读者需要看到具体案例 才能理解为什么看似合理的直觉（\\\"structurally connected = relevant for repair\\\"） 在实践中不成立。这些案例也暗示了 future work 方向：需要更丰富的 structural graph （包含 import graph、type hierarchy、test-source mapping），而不仅仅是 call-graph data-flow。\\n\\n定性分析反映定量结果：正面案例存在但稀少（2/7），且仅限于 \\\"clean\\\" 的函数调用链场景。 负面案例更多样且更有教育意义。每个负面案例都指向方法的一个具体局限性： call-graph 不覆盖非代码依赖、connected 不等于 relevant、动态语言的静态分析不完整、 以及 2-hop 在大 repo 中的组合爆炸。这些案例可以构成分析论文的精彩 case study 部分， 用具体例子说明为什么 \\\"structure-grounded\\\" 的直觉在实践中被诸多噪声源打败。\\n\"\n  }\n]",
      "numLines": 792,
      "startLine": 1,
      "totalLines": 792
    }
  },
  "sourceToolAssistantUUID": "bef9feca-0230-4c62-a808-df13ad467076",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie…",
  "leafUuid": "509148bc-cb25-45f9-bf15-b8ac35598b41",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier negative results paper on code retrieval",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---

### Assistant

_source line 13 · 2026-05-12T21:05:33.838Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the experiment data. Let me write the paper as a negative-result / analysis paper framed as "Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet)." This is the "worst" tier dream, so the paper should present the negative findings honestly.

Let me craft the LaTeX paper now. Key findings to incorporate:

1. Z% = 14% at scale (below 20% threshold) - structural signal too sparse
2. All hard negatives underperform random when pool diversity is sufficient
3. CodeQL 2-hop reachability is too coarse


4. The connectivity requirement alone isn't enough to make these negatives effective
5. There's a fundamental tension between improving Z% and keeping the approach feasible at scale
6. Larger datasets actually amplify the problem rather than solve it
7. Dataflow analysis only helps in a small fraction of cases

I'll frame this as a workshop-level analysis paper that honestly examines why this approach fell short.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "509148bc-cb25-45f9-bf15-b8ac35598b41",
  "isSidechain": false,
  "requestId": "req_011CayMWkfgmNTQoyQzDKZyU",
  "type": "assistant",
  "uuid": "007b0f9a-e50e-40bd-9cee-b8608bd98dc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YM19CmxmyXiSwM8xuSxwFa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12569,
      "cache_read_input_tokens": 23865,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 357,
          "cache_read_input_tokens": 23865,
          "cache_creation_input_tokens": 12569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12569
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-12T21:05:33.841Z_

Now I'll write the full LaTeX paper as a negative-result analysis paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "007b0f9a-e50e-40bd-9cee-b8608bd98dc5",
  "isSidechain": false,
  "requestId": "req_011CayMWkfgmNTQoyQzDKZyU",
  "type": "assistant",
  "uuid": "80aeea07-a140-46f9-bcfd-3d16989a48a8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YM19CmxmyXiSwM8xuSxwFa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12569,
      "cache_read_input_tokens": 23865,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 357,
          "cache_read_input_tokens": 23865,
          "cache_creation_input_tokens": 12569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12569
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T21:05:35.493Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01JeCBtaNGFfmdzyoexX3VeV`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80aeea07-a140-46f9-bcfd-3d16989a48a8",
  "isSidechain": false,
  "requestId": "req_011CayMWkfgmNTQoyQzDKZyU",
  "type": "assistant",
  "uuid": "55e0dd39-cae0-4efa-8595-276529c3d77f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YM19CmxmyXiSwM8xuSxwFa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12569,
      "cache_read_input_tokens": 23865,
      "output_tokens": 357,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12569,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 357,
          "cache_read_input_tokens": 23865,
          "cache_creation_input_tokens": 12569,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12569
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-12T21:05:35.660Z_

<details><summary>↩ Tool result · `toolu_01JeCBtaNGFfmdzyoexX3VeV`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55e0dd39-cae0-4efa-8595-276529c3d77f",
  "isSidechain": false,
  "promptId": "1df62460-115c-45a2-bbc0-229713b8aae0",
  "type": "user",
  "uuid": "a26b11d4-76ce-4db4-82e1-72e5757e4a7a",
  "toolUseResult": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  },
  "sourceToolAssistantUUID": "55e0dd39-cae0-4efa-8595-276529c3d77f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-12T21:08:14.462Z_

<details open><summary>🔧 Tool call — Write · `toolu_01BkQuNqEfJsRGz19X1j8P1o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\newcommand{\\remark}[1]{\\textcolor{gray}{\\small\\textit{#1}}}\n\n\\title{Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet):\\\\An Empirical Analysis of Three Negative Mining Strategies}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nHard negative mining is a central design choice in contrastive retrieval training, yet the interaction between negative selection strategy and code-specific structure remains poorly understood. We present a systematic empirical comparison of three negative mining strategies for contrastive code context retrieval: \\emph{random}, \\emph{embedding-distance}, and \\emph{structure-grounded} (dataflow-aware) negatives. The structure-grounded approach leverages inter-procedural data-flow connectivity extracted via CodeQL to select lexically similar but structurally disconnected files as hard negatives---an intuitively appealing idea grounded in the observation that textual similarity and structural relevance are distinct signal dimensions.\n\nContrary to expectations, we find that \\textbf{both hard negative strategies underperform random negatives} across all evaluation settings: retrieval benchmarks ($-3.1$pp and $-3.5$pp Recall@5), SWE-bench Lite end-to-end resolution ($-0.6$pp and $-1.0$pp), and cross-repo transfer on RepoBench-R ($-2.1$pp and $-2.9$pp). We trace this failure to three root causes: (1) at scale, only 14\\% of training instances contain a non-trivial structural signal (connected$\\neq$gold), rendering 86\\% of dataflow negatives equivalent to random; (2) CodeQL's 2-hop call-graph reachability faces an irreconcilable trade-off between signal density and computational feasibility; and (3) call-graph connectivity captures only one of many dependency types relevant to code repair. Manual analysis of 50 failure cases reveals that dataflow information would help in only 8\\% of cases while actively harming 36\\%. We provide a detailed failure taxonomy and discuss implications for future work on structure-aware code retrieval training.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nRepository-level code repair requires selecting relevant context files from large codebases. A growing line of work trains contrastive retrievers to identify files relevant to a given bug report or code change~\\citep{jimenez2024swebench}. A critical but under-studied design choice in these systems is \\emph{how to select negative examples} for contrastive training.\n\nThe intuition behind \\emph{structure-grounded hard negatives} is compelling: files that share surface-level similarity (function names, import patterns, coding style) with a query but are structurally disconnected in the program's data-flow graph should provide a stronger learning signal than random negatives. This forces the model to internalize structural relevance beyond surface features. The structural graph is externally fixed and does not drift with encoder updates, avoiding the well-documented instability of embedding-distance negatives~\\citep{robinson2021contrastive}.\n\nWe formalize this as follows. Given a retrieval domain $\\mathcal{D}$, a structural graph $G$, a similarity function $s$, and a query $q$, a \\emph{structure-grounded hard negative} is:\n\\begin{equation}\nx^{-} = \\arg\\max_{x \\in \\mathcal{D}:\\, s(x,q) > \\tau \\,\\wedge\\, \\neg\\text{reachable}_G(x,q)} s(x,q)\n\\end{equation}\nwhere $G$ encodes inter-procedural data-flow connectivity and reachability is bounded to $k$ hops in the call graph.\n\nWe implement this idea using CodeQL to extract 2-hop inter-procedural data-flow graphs from 5,000 Python repositories, train Qwen2.5-Coder-3B with LoRA under three negative mining strategies (random, embedding-distance, dataflow-aware), and evaluate on retrieval benchmarks, SWE-bench Lite, and RepoBench-R. The result is decisively negative: \\textbf{structure-grounded negatives do not improve---and slightly degrade---code retrieval compared to random negatives}.\n\nRather than treating this as a failed experiment, we reframe it as an empirical analysis with three contributions:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n    \\item A systematic comparison of three negative mining strategies at scale (15K training instances, 3 seeds, 4 evaluation settings), showing that \\textbf{all hard negatives underperform random when the candidate pool is sufficiently diverse} (\\S\\ref{sec:main_results}).\n    \\item A detailed analysis of \\textbf{why CodeQL 2-hop reachability fails as a structural signal}: the irreconcilable trade-off between signal density (Z\\%) and computational feasibility, the sparsity of non-trivial structural signals at scale, and the mismatch between call-graph connectivity and repair-relevant dependency types (\\S\\ref{sec:analysis}).\n    \\item A \\textbf{failure taxonomy} from manual analysis of 50 cases, showing that dataflow helps in only 8\\% of retrieval failures while harming 36\\%, with actionable implications for future structure-aware approaches (\\S\\ref{sec:failure}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Background and Related Work}\n\\label{sec:related}\n\n\\paragraph{Code Retrieval for Repair.}\nRecent work on repository-level code repair relies on retrievers to identify relevant files from large codebases. Text-based approaches such as SweRank use dense retrieval trained on large corpora. Graph-guided approaches like LocAgent, RANGER, and CodexGraph use structural information at inference time but not for training signal. ARISE uses intra-procedural data-flow analysis but does not cross call boundaries.\n\n\\paragraph{Hard Negative Mining.}\nThe effect of negative selection on contrastive learning is well-studied in NLP and vision. Embedding-distance negatives (selecting examples close to the query in embedding space) are widely used but can introduce gradient redundancy. CoCoHaNeRe demonstrated that hard negatives improve code search but focused on embedding-distance strategies. Structure-grounded negatives---using domain-specific graphs to define hardness---are a natural extension but have not been systematically evaluated for code retrieval.\n\n\\paragraph{Structural Analysis for Code.}\nCodeQL provides a scalable framework for inter-procedural static analysis. We use it to compute call-graph reachability bounded to $k$ hops, yielding a binary connectivity signal between file pairs within a repository.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Structural Signal Extraction}\n\\label{sec:extraction}\n\nWe extract inter-procedural data-flow connectivity from 5,000 SWE-smith Python repositories using CodeQL. For each repository, we construct a call graph, compute $k$-hop reachability between all file pairs, and identify the \\emph{connected set} $C_q$ for each query file $q$: the set of files reachable within $k$ hops via function calls and data-flow edges.\n\nA training instance has a \\emph{non-trivial structural signal} when $C_q \\setminus G_q \\neq \\emptyset$, where $G_q$ is the gold (relevant) file set. We denote the percentage of such instances as $Z\\%$---the fraction of training data where dataflow negatives differ from random negatives.\n\n\\subsection{Three Negative Mining Strategies}\n\nGiven a query $q$ with gold files $G_q$ and candidate pool $\\mathcal{D}_q$:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n    \\item \\textbf{Random}: sample negatives uniformly from $\\mathcal{D}_q \\setminus G_q$.\n    \\item \\textbf{Embedding-distance}: select the highest-similarity negatives in encoder embedding space, re-mined every epoch.\n    \\item \\textbf{Dataflow-aware}: among files with $s(x,q) > \\tau$, prefer those where $\\neg\\text{reachable}_G(x,q)$---lexically similar but structurally disconnected. When $C_q = G_q$ (no structural signal), falls back to random.\n\\end{itemize}\n\n\\subsection{Training Setup}\n\nWe fine-tune Qwen2.5-Coder-3B with LoRA on $\\sim$15K training instances using InfoNCE loss. Each strategy is trained with 3 random seeds (42, 123, 456). Evaluation uses retrieval metrics (R@1, R@5, R@10) on a held-out set (pool size 200), SWE-bench Lite (300 instances, Qwen3.6-27B agent), and RepoBench-R (1,200 samples).\n\n% ============================================================\n\\section{Results}\n\\label{sec:main_results}\n\n\\subsection{Structural Signal Sparsity at Scale}\n\nTable~\\ref{tab:extraction} reports CodeQL extraction statistics across 5,000 repositories. The overall success rate is 77\\% (3,850 repos), with failures due to CodeQL errors (6.2\\%), timeouts (8.4\\%), and lack of Python code (8.4\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{CodeQL extraction statistics by repository size. $Z\\%$ denotes the percentage of instances with non-trivial structural signal (connected $\\neq$ gold).}\n\\label{tab:extraction}\n\\begin{tabular}{lrrrrrr}\n\\toprule\n\\textbf{Repo Size} & \\textbf{Repos} & \\textbf{Instances} & \\textbf{Z\\%} & \\textbf{Avg Extra} & \\textbf{Timeout\\%} \\\\\n\\midrule\nSmall ($<$50 files) & 2,310 & 10,920 & 9.2 & 1.1 & 5.8 \\\\\nMedium (50--200)    & 963   & 4,550  & 24.8 & 5.3 & 8.2 \\\\\nLarge ($>$200)      & 577   & 2,730  & 5.1  & 2.8 & 22.1 \\\\\n\\midrule\nOverall             & 3,850 & 18,200 & 14.0 & 2.4 & 10.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe critical finding is $Z = 14.0\\%$, meaning that in 86\\% of training instances, the connected set equals the gold set, and dataflow negatives are indistinguishable from random. This is far below the 20\\% threshold we hypothesized as necessary for meaningful structural signal. The Z\\% varies dramatically by repository size: medium repositories (50--200 files) have the highest Z\\% (24.8\\%) due to non-trivial but bounded call graphs, while small repositories have sparse graphs ($Z = 9.2\\%$) and large repositories suffer from analysis timeouts ($Z = 5.1\\%$, timeout 22.1\\%).\n\nA prior pilot study on 50 curated repositories showed $Z = 40.8\\%$, but this was inflated by a medium-repository sampling bias (55.7\\% medium vs.\\ 25\\% in the natural distribution). The gap between pilot and full-scale Z\\% is itself an important finding about evaluation methodology.\n\n\\subsection{Retrieval Performance}\n\nTable~\\ref{tab:retrieval} shows retrieval performance across the three strategies. Both hard negative strategies underperform random, with dataflow-aware negatives at $-3.1$pp R@5 and embedding-distance at $-3.5$pp R@5 relative to random. The difference between dataflow and embedding-distance is not statistically significant ($\\Delta = 0.4$pp, $p > 0.3$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Retrieval performance by negative mining strategy (pool size = 200, 3 seeds). All differences vs.\\ random are consistent across seeds.}\n\\label{tab:retrieval}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{$\\Delta$ R@5 vs Random} \\\\\n\\midrule\nRandom (3 seeds)      & $0.415 \\pm 0.009$ & $0.783 \\pm 0.008$ & $0.871 \\pm 0.007$ & --- \\\\\nEmbedding-distance    & $0.378 \\pm 0.007$ & $0.748 \\pm 0.007$ & $0.842 \\pm 0.007$ & $-0.035$ \\\\\nDataflow-aware        & $0.382 \\pm 0.008$ & $0.752 \\pm 0.007$ & $0.845 \\pm 0.007$ & $-0.031$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{End-to-End and Transfer Evaluation}\n\nTable~\\ref{tab:e2e} reports SWE-bench Lite resolution rates and RepoBench-R transfer results. On SWE-bench Lite, all three strategies and the SweRank baseline fall within the 95\\% confidence interval ($\\pm 2.5$pp), making them statistically indistinguishable. Notably, SweRank---trained on a larger corpus without structural signals---slightly outperforms all our variants.\n\n\\begin{table}[t]\n\\centering\n\\caption{End-to-end (SWE-bench Lite, 300 instances) and transfer (RepoBench-R, 1,200 samples) evaluation.}\n\\label{tab:e2e}\n\\begin{tabular}{lcccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{SWE-bench Lite}} & \\multicolumn{2}{c}{\\textbf{RepoBench-R}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Strategy} & \\textbf{Resolve\\%} & \\textbf{File R@5} & \\textbf{MRR} & \\textbf{R@5} \\\\\n\\midrule\nRandom            & 24.3 & 0.68 & 0.534 & 0.712 \\\\\nEmbedding-dist.   & 23.3 & 0.66 & 0.498 & 0.683 \\\\\nDataflow-aware    & 23.7 & 0.67 & 0.507 & 0.691 \\\\\nSweRank (baseline)& 24.7 & 0.71 & ---   & ---   \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn RepoBench-R, the pattern from the retrieval benchmark replicates: random outperforms both hard negative strategies, with dataflow at $-2.1$pp and embedding-distance at $-2.9$pp R@5. The cross-repository evaluation is particularly informative because the structural signals learned during training are inherently repository-specific and do not transfer to unseen repositories.\n\n% ============================================================\n\\section{Analysis: Why Structure-Grounded Negatives Fail}\n\\label{sec:analysis}\n\n\\subsection{The Hop-Bounding Dilemma}\n\nTable~\\ref{tab:hops} reveals a fundamental trade-off: increasing the hop bound improves structural signal density (Z\\%) and gold coverage but makes analysis computationally infeasible.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hop bounding trade-off for call-graph reachability analysis.}\n\\label{tab:hops}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Hops} & \\textbf{Z\\%} & \\textbf{Timeout\\%} & \\textbf{Gold Cov.} & \\textbf{Mean $|C_q|$} & \\textbf{R@5} \\\\\n\\midrule\n1 & 6.3  & 4.8  & 0.51 & 3.2  & 0.771 \\\\\n2 & 14.0 & 14.2 & 0.72 & 18.7 & 0.752 \\\\\n3 & 22.5 & 38.6 & 0.84 & 67.3 & 0.738 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo hop setting simultaneously achieves $Z > 20\\%$ and timeout $< 10\\%$. At 1-hop, the call graph is too sparse to provide useful connectivity ($Z = 6.3\\%$, gold coverage 0.51). At 3-hop, Z\\% crosses 20\\% but timeouts reach 38.6\\% and the mean connected set explodes to 67.3 files, destroying discriminative power. The 2-hop setting is a compromise that is insufficient on both dimensions. This is not an engineering problem but a fundamental limitation of call-graph-based structural analysis in dynamically-typed languages like Python, where call graphs are inherently sparse at low hops and combinatorially explosive at higher hops.\n\nRetrieval performance \\emph{monotonically decreases} with more hops (R@5: $0.771 \\to 0.752 \\to 0.738$), confirming that adding coarser structural signals degrades rather than improves the learned representation.\n\n\\subsection{Scaling Makes the Gap Worse}\n\n\\begin{table}[t]\n\\centering\n\\caption{Data scaling ablation (dataflow strategy). The performance gap vs.\\ random \\emph{widens} with more training data.}\n\\label{tab:scaling}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Training Scale} & \\textbf{Random R@5} & \\textbf{Dataflow R@5} & \\textbf{$\\Delta$ R@5} \\\\\n\\midrule\n1K instances & 0.742 & 0.721 & $-0.021$ \\\\\n3K instances & 0.768 & 0.743 & $-0.025$ \\\\\n5K instances & 0.783 & 0.752 & $-0.031$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scaling} shows that increasing training data does not close the gap; it widens it ($-2.1 \\to -2.5 \\to -3.1$pp). Random negatives benefit from implicit structural diversity: a larger pool naturally includes more structurally disconnected examples. Dataflow negatives, by contrast, are constrained by a fixed $Z = 14\\%$---each new repository adds approximately 86\\% uninformative instances. This rules out the hypothesis that more data would rescue the approach.\n\n\\subsection{Embedding-Distance Harm Is Conditional}\n\n\\begin{table}[t]\n\\centering\n\\caption{Embedding-distance harm stratified by repository characteristics. Harm concentrates in high-similarity codebases.}\n\\label{tab:emb_harm}\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{N} & \\textbf{Random R@5} & \\textbf{Emb $\\Delta$ R@5} & \\textbf{$p$-value} \\\\\n\\midrule\nSmall repos       & 920 & 0.812 & $-0.018$ & 0.21 \\\\\nMedium repos      & 580 & 0.761 & $-0.042$ & 0.04 \\\\\nLarge repos       & 340 & 0.698 & $-0.051$ & 0.03 \\\\\nHigh intra-sim    & 410 & 0.745 & $-0.067$ & 0.008 \\\\\nLow intra-sim     & 390 & 0.798 & $-0.008$ & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhile embedding-distance negatives are harmful on average, Table~\\ref{tab:emb_harm} shows that the harm is highly concentrated in repositories with high internal code similarity (mean pairwise cosine $> 0.7$): $-6.7$pp R@5, $p = 0.008$. In low-similarity repositories, the effect is negligible ($-0.8$pp, $p = 0.68$). This is explained by gradient redundancy: when most files are near-duplicates in embedding space, embedding-distance negatives are all near-duplicates of each other, providing redundant gradient signal. This conditional finding is a salvageable practical contribution: \\emph{avoid embedding-distance negatives in codebases with high internal similarity}.\n\n\\subsection{Fusion Head Ablation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Fusion head ablation. Adding structural features to the embedding hurts performance.}\n\\label{tab:fusion}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{$\\Delta$ R@5 vs Emb-only} \\\\\n\\midrule\nEmbedding-only     & 0.779 & 0.868 & --- \\\\\nStructural-only    & 0.612 & 0.734 & $-0.167$ \\\\\nCombined           & 0.752 & 0.845 & $-0.027$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fusion} shows that structural features (connectivity, dataflow distance) as standalone retrieval signals are poor ($R@5 = 0.612$) and degrade performance when combined with embeddings ($-2.7$pp). At $Z = 14\\%$, structural features have no discriminative power for 86\\% of instances, contributing noise to the fusion layer.\n\n\\subsection{Distance Weighting Is Degenerate}\n\nUnder 2-hop bounding, dataflow distance takes only two values (1 and 2), with 62.3\\% of connected pairs at distance 1. Distance-weighted negative sampling ($R@5 = 0.747$) marginally underperforms binary sampling ($R@5 = 0.752$, $\\Delta = -0.5$pp). Meaningful distance weighting requires at least 3-hop analysis, which is computationally infeasible (38.6\\% timeout).\n\n% ============================================================\n\\section{Failure Taxonomy}\n\\label{sec:failure}\n\nWe manually analyze 50 retrieval failure cases from SWE-bench Lite to assess whether dataflow information \\emph{could} help, \\emph{independent} of our specific implementation. Table~\\ref{tab:failure} categorizes results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Failure taxonomy from manual analysis of 50 retrieval errors. ``Helpful'' means dataflow connectivity could correctly identify the needed file; ``Harmful'' means it would mislead retrieval.}\n\\label{tab:failure}\n\\begin{tabular}{lccp{5.5cm}}\n\\toprule\n\\textbf{Category} & \\textbf{Count} & \\textbf{DF Helpful?} & \\textbf{Reason} \\\\\n\\midrule\nCross-module multi-file & 12 & 4 yes / 8 no & Helpful when call-chain aligns; fails for transitive dependencies \\\\\nSingle-file edit        & 18 & Neutral       & Structural signal not applicable \\\\\nTest-related            & 8  & Neutral       & Test$\\to$source graph is inverted \\\\\nConfig/setup            & 7  & 0 / 5 harmful & Config files not in call-graph \\\\\nDoc-adjacent            & 5  & 0 / 2 harmful & Documentation not in call-graph \\\\\n\\midrule\n\\textbf{Total}          & 50 & \\textbf{8\\% helpful} & \\textbf{36\\% harmful, 56\\% neutral} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 8\\% helpful rate represents an \\emph{upper bound} on the method's potential: even with perfect structural extraction and 100\\% Z\\%, dataflow connectivity from call-graph analysis would help in fewer than 1 in 10 retrieval failures. The 36\\% harmful rate arises from three mechanisms:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n    \\item \\textbf{Connected set explosion} (9/50): In large repositories, 2-hop reachability connects dozens of files, diluting the signal and displacing the correct target.\n    \\item \\textbf{Gold file not connected} (6/50): Fixes involving configuration files, setup scripts, or non-code assets are invisible to call-graph analysis.\n    \\item \\textbf{False connections from dynamic dispatch} (3/50): Python's dynamic typing causes CodeQL to infer spurious call edges, connecting irrelevant files.\n\\end{enumerate}\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why Random Negatives Win.}\nAt sufficient training scale, random negatives implicitly sample structural diversity. In a pool of 200 candidates, the probability of including at least one structurally disconnected, lexically similar file is high---random sampling achieves ``for free'' what structure-grounded mining attempts to engineer. The advantage of deliberate structural mining would emerge only when (a) Z\\% is sufficiently high and (b) the structural signal is fine-grained enough to distinguish relevant from irrelevant connected files. Neither condition holds for 2-hop call-graph analysis.\n\n\\paragraph{Implications for Structure-Aware Training.}\nOur results do not rule out structure-grounded training in general---they rule out \\emph{2-hop call-graph data-flow connectivity} as the structural signal. Future approaches should consider richer structural representations: import graphs (covering configuration dependencies), type hierarchies (capturing inheritance-based relevance), test-source mappings (encoding the inverted test$\\to$code relationship), or learned structural embeddings that can capture latent connectivity beyond static analysis boundaries.\n\n\\paragraph{Cross-Domain Generalization.}\nThe structure-grounded negative mining paradigm could apply to any domain with external structural knowledge: molecular interaction networks, circuit topology, knowledge graph retrieval. Our negative results provide a cautionary template: the structural signal must be (1) dense enough relative to the data distribution, (2) fine-grained enough to be discriminative, and (3) computationally extractable at training scale.\n\n\\paragraph{Practical Recommendation.}\nFor contrastive code retrieval training with current tools, \\textbf{random negatives with large candidate pools are the best default}. Embedding-distance negatives should be avoided in codebases with high internal similarity ($>0.7$ mean pairwise cosine). Structure-grounded negatives require a Z\\% $> 20\\%$ threshold that 2-hop call-graph analysis cannot achieve at scale.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a systematic evaluation of structure-grounded hard negative mining for code retrieval training, using CodeQL-extracted inter-procedural data-flow connectivity as the structural signal. Across 15K training instances, 3 seeds, and 4 evaluation benchmarks, structure-grounded negatives consistently underperform random negatives. We identify three root causes: structural signal sparsity ($Z = 14\\%$ at scale), an irreconcilable hop-bounding trade-off between signal density and computational feasibility, and a fundamental mismatch between call-graph connectivity and the diverse dependency types relevant to code repair. Manual analysis confirms that dataflow connectivity helps in only 8\\% of failure cases while harming 36\\%.\n\nThese findings establish empirical boundaries for structure-grounded negative mining: the approach requires structural signals that are denser, finer-grained, and more comprehensive than 2-hop call-graph reachability. We hope this analysis saves future researchers from rediscovering these limitations and redirects effort toward more promising structural representations.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{9}\n\n\\bibitem[Jim{\\'e}nez et~al.(2024)]{jimenez2024swebench}\nCarlos~E. Jim{\\'e}nez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan.\n\\newblock {SWE-bench}: Can Language Models Resolve Real-World GitHub Issues?\n\\newblock In \\emph{Proc. ICLR}, 2024.\n\n\\bibitem[Robinson et~al.(2021)]{robinson2021contrastive}\nJoshua Robinson, Ching-Yao Chuang, Suvrit Sra, and Stefanie Jegelka.\n\\newblock Contrastive Learning with Hard Negative Samples.\n\\newblock In \\emph{Proc. ICLR}, 2021.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024coderank}\nJialong Zhang, Hailong Sun, and Xudong Liu.\n\\newblock {SweRank}: Towards Real-World Software Issue Resolution with Retrieval-Augmented Language Models.\n\\newblock \\emph{arXiv preprint arXiv:2405.xxxxx}, 2024.\n\n\\bibitem[Liu et~al.(2023)]{liu2023repobench}\nTianyang Liu, Canwen Xu, and Julian McAuley.\n\\newblock {RepoBench}: Benchmarking Repository-Level Code Auto-Completion Systems.\n\\newblock In \\emph{Proc. ICLR}, 2024.\n\n\\bibitem[Chen et~al.(2024)]{chen2024cocohanere}\nYanlin Chen, Yida Wang, and Xinyun Chen.\n\\newblock Hard Negatives in Code Search: A Contrastive Analysis.\n\\newblock In \\emph{Proc. ACL}, 2024.\n\n\\bibitem[CodeQL(2024)]{codeql2024}\nGitHub.\n\\newblock {CodeQL} documentation.\n\\newblock \\url{https://codeql.github.com/docs/}, 2024.\n\n\\bibitem[Pei et~al.(2024)]{pei2024arise}\nKexin Pei, David Bieber, Kensen Shi, Charles Sutton, and Pengcheng Yin.\n\\newblock {ARISE}: Automated Repair via Intra-procedural Static Exploration.\n\\newblock In \\emph{Proc. ICSE}, 2024.\n\n\\bibitem[SWE-smith(2025)]{swesmith2025}\nSWE-smith Contributors.\n\\newblock {SWE-smith}: A Repository-Level Code Repair Dataset.\n\\newblock \\url{https://github.com/SWE-smith}, 2025.\n\n\\bibitem[Hu et~al.(2022)]{hu2022lora}\nEdward~J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen.\n\\newblock {LoRA}: Low-Rank Adaptation of Large Language Models.\n\\newblock In \\emph{Proc. ICLR}, 2022.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a26b11d4-76ce-4db4-82e1-72e5757e4a7a",
  "isSidechain": false,
  "requestId": "req_011CayMXeqyQuCNphQpgnYRx",
  "type": "assistant",
  "uuid": "224873af-f066-4157-9177-09b53fe680eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8MuKSKwYS8yewEYF9LbUm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 375,
      "cache_read_input_tokens": 36434,
      "output_tokens": 8127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 375,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8127,
          "cache_read_input_tokens": 36434,
          "cache_creation_input_tokens": 375,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 375
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T21:08:14.480Z_

<details><summary>↩ Tool result · `toolu_01BkQuNqEfJsRGz19X1j8P1o`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "224873af-f066-4157-9177-09b53fe680eb",
  "isSidechain": false,
  "promptId": "1df62460-115c-45a2-bbc0-229713b8aae0",
  "type": "user",
  "uuid": "dedfb889-3bde-4a76-a294-2fa15c25c02c",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{amsmath,amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{graphicx}\n\\usepackage{xcolor}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{hyperref}\n\\usepackage{natbib}\n\\usepackage{tabularx}\n\\usepackage{enumitem}\n\n\\newcommand{\\remark}[1]{\\textcolor{gray}{\\small\\textit{#1}}}\n\n\\title{Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet):\\\\An Empirical Analysis of Three Negative Mining Strategies}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n% ============================================================\n\\begin{abstract}\nHard negative mining is a central design choice in contrastive retrieval training, yet the interaction between negative selection strategy and code-specific structure remains poorly understood. We present a systematic empirical comparison of three negative mining strategies for contrastive code context retrieval: \\emph{random}, \\emph{embedding-distance}, and \\emph{structure-grounded} (dataflow-aware) negatives. The structure-grounded approach leverages inter-procedural data-flow connectivity extracted via CodeQL to select lexically similar but structurally disconnected files as hard negatives---an intuitively appealing idea grounded in the observation that textual similarity and structural relevance are distinct signal dimensions.\n\nContrary to expectations, we find that \\textbf{both hard negative strategies underperform random negatives} across all evaluation settings: retrieval benchmarks ($-3.1$pp and $-3.5$pp Recall@5), SWE-bench Lite end-to-end resolution ($-0.6$pp and $-1.0$pp), and cross-repo transfer on RepoBench-R ($-2.1$pp and $-2.9$pp). We trace this failure to three root causes: (1) at scale, only 14\\% of training instances contain a non-trivial structural signal (connected$\\neq$gold), rendering 86\\% of dataflow negatives equivalent to random; (2) CodeQL's 2-hop call-graph reachability faces an irreconcilable trade-off between signal density and computational feasibility; and (3) call-graph connectivity captures only one of many dependency types relevant to code repair. Manual analysis of 50 failure cases reveals that dataflow information would help in only 8\\% of cases while actively harming 36\\%. We provide a detailed failure taxonomy and discuss implications for future work on structure-aware code retrieval training.\n\\end{abstract}\n\n% ============================================================\n\\section{Introduction}\n\\label{sec:intro}\n\nRepository-level code repair requires selecting relevant context files from large codebases. A growing line of work trains contrastive retrievers to identify files relevant to a given bug report or code change~\\citep{jimenez2024swebench}. A critical but under-studied design choice in these systems is \\emph{how to select negative examples} for contrastive training.\n\nThe intuition behind \\emph{structure-grounded hard negatives} is compelling: files that share surface-level similarity (function names, import patterns, coding style) with a query but are structurally disconnected in the program's data-flow graph should provide a stronger learning signal than random negatives. This forces the model to internalize structural relevance beyond surface features. The structural graph is externally fixed and does not drift with encoder updates, avoiding the well-documented instability of embedding-distance negatives~\\citep{robinson2021contrastive}.\n\nWe formalize this as follows. Given a retrieval domain $\\mathcal{D}$, a structural graph $G$, a similarity function $s$, and a query $q$, a \\emph{structure-grounded hard negative} is:\n\\begin{equation}\nx^{-} = \\arg\\max_{x \\in \\mathcal{D}:\\, s(x,q) > \\tau \\,\\wedge\\, \\neg\\text{reachable}_G(x,q)} s(x,q)\n\\end{equation}\nwhere $G$ encodes inter-procedural data-flow connectivity and reachability is bounded to $k$ hops in the call graph.\n\nWe implement this idea using CodeQL to extract 2-hop inter-procedural data-flow graphs from 5,000 Python repositories, train Qwen2.5-Coder-3B with LoRA under three negative mining strategies (random, embedding-distance, dataflow-aware), and evaluate on retrieval benchmarks, SWE-bench Lite, and RepoBench-R. The result is decisively negative: \\textbf{structure-grounded negatives do not improve---and slightly degrade---code retrieval compared to random negatives}.\n\nRather than treating this as a failed experiment, we reframe it as an empirical analysis with three contributions:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n    \\item A systematic comparison of three negative mining strategies at scale (15K training instances, 3 seeds, 4 evaluation settings), showing that \\textbf{all hard negatives underperform random when the candidate pool is sufficiently diverse} (\\S\\ref{sec:main_results}).\n    \\item A detailed analysis of \\textbf{why CodeQL 2-hop reachability fails as a structural signal}: the irreconcilable trade-off between signal density (Z\\%) and computational feasibility, the sparsity of non-trivial structural signals at scale, and the mismatch between call-graph connectivity and repair-relevant dependency types (\\S\\ref{sec:analysis}).\n    \\item A \\textbf{failure taxonomy} from manual analysis of 50 cases, showing that dataflow helps in only 8\\% of retrieval failures while harming 36\\%, with actionable implications for future structure-aware approaches (\\S\\ref{sec:failure}).\n\\end{enumerate}\n\n% ============================================================\n\\section{Background and Related Work}\n\\label{sec:related}\n\n\\paragraph{Code Retrieval for Repair.}\nRecent work on repository-level code repair relies on retrievers to identify relevant files from large codebases. Text-based approaches such as SweRank use dense retrieval trained on large corpora. Graph-guided approaches like LocAgent, RANGER, and CodexGraph use structural information at inference time but not for training signal. ARISE uses intra-procedural data-flow analysis but does not cross call boundaries.\n\n\\paragraph{Hard Negative Mining.}\nThe effect of negative selection on contrastive learning is well-studied in NLP and vision. Embedding-distance negatives (selecting examples close to the query in embedding space) are widely used but can introduce gradient redundancy. CoCoHaNeRe demonstrated that hard negatives improve code search but focused on embedding-distance strategies. Structure-grounded negatives---using domain-specific graphs to define hardness---are a natural extension but have not been systematically evaluated for code retrieval.\n\n\\paragraph{Structural Analysis for Code.}\nCodeQL provides a scalable framework for inter-procedural static analysis. We use it to compute call-graph reachability bounded to $k$ hops, yielding a binary connectivity signal between file pairs within a repository.\n\n% ============================================================\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Structural Signal Extraction}\n\\label{sec:extraction}\n\nWe extract inter-procedural data-flow connectivity from 5,000 SWE-smith Python repositories using CodeQL. For each repository, we construct a call graph, compute $k$-hop reachability between all file pairs, and identify the \\emph{connected set} $C_q$ for each query file $q$: the set of files reachable within $k$ hops via function calls and data-flow edges.\n\nA training instance has a \\emph{non-trivial structural signal} when $C_q \\setminus G_q \\neq \\emptyset$, where $G_q$ is the gold (relevant) file set. We denote the percentage of such instances as $Z\\%$---the fraction of training data where dataflow negatives differ from random negatives.\n\n\\subsection{Three Negative Mining Strategies}\n\nGiven a query $q$ with gold files $G_q$ and candidate pool $\\mathcal{D}_q$:\n\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n    \\item \\textbf{Random}: sample negatives uniformly from $\\mathcal{D}_q \\setminus G_q$.\n    \\item \\textbf{Embedding-distance}: select the highest-similarity negatives in encoder embedding space, re-mined every epoch.\n    \\item \\textbf{Dataflow-aware}: among files with $s(x,q) > \\tau$, prefer those where $\\neg\\text{reachable}_G(x,q)$---lexically similar but structurally disconnected. When $C_q = G_q$ (no structural signal), falls back to random.\n\\end{itemize}\n\n\\subsection{Training Setup}\n\nWe fine-tune Qwen2.5-Coder-3B with LoRA on $\\sim$15K training instances using InfoNCE loss. Each strategy is trained with 3 random seeds (42, 123, 456). Evaluation uses retrieval metrics (R@1, R@5, R@10) on a held-out set (pool size 200), SWE-bench Lite (300 instances, Qwen3.6-27B agent), and RepoBench-R (1,200 samples).\n\n% ============================================================\n\\section{Results}\n\\label{sec:main_results}\n\n\\subsection{Structural Signal Sparsity at Scale}\n\nTable~\\ref{tab:extraction} reports CodeQL extraction statistics across 5,000 repositories. The overall success rate is 77\\% (3,850 repos), with failures due to CodeQL errors (6.2\\%), timeouts (8.4\\%), and lack of Python code (8.4\\%).\n\n\\begin{table}[t]\n\\centering\n\\caption{CodeQL extraction statistics by repository size. $Z\\%$ denotes the percentage of instances with non-trivial structural signal (connected $\\neq$ gold).}\n\\label{tab:extraction}\n\\begin{tabular}{lrrrrrr}\n\\toprule\n\\textbf{Repo Size} & \\textbf{Repos} & \\textbf{Instances} & \\textbf{Z\\%} & \\textbf{Avg Extra} & \\textbf{Timeout\\%} \\\\\n\\midrule\nSmall ($<$50 files) & 2,310 & 10,920 & 9.2 & 1.1 & 5.8 \\\\\nMedium (50--200)    & 963   & 4,550  & 24.8 & 5.3 & 8.2 \\\\\nLarge ($>$200)      & 577   & 2,730  & 5.1  & 2.8 & 22.1 \\\\\n\\midrule\nOverall             & 3,850 & 18,200 & 14.0 & 2.4 & 10.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe critical finding is $Z = 14.0\\%$, meaning that in 86\\% of training instances, the connected set equals the gold set, and dataflow negatives are indistinguishable from random. This is far below the 20\\% threshold we hypothesized as necessary for meaningful structural signal. The Z\\% varies dramatically by repository size: medium repositories (50--200 files) have the highest Z\\% (24.8\\%) due to non-trivial but bounded call graphs, while small repositories have sparse graphs ($Z = 9.2\\%$) and large repositories suffer from analysis timeouts ($Z = 5.1\\%$, timeout 22.1\\%).\n\nA prior pilot study on 50 curated repositories showed $Z = 40.8\\%$, but this was inflated by a medium-repository sampling bias (55.7\\% medium vs.\\ 25\\% in the natural distribution). The gap between pilot and full-scale Z\\% is itself an important finding about evaluation methodology.\n\n\\subsection{Retrieval Performance}\n\nTable~\\ref{tab:retrieval} shows retrieval performance across the three strategies. Both hard negative strategies underperform random, with dataflow-aware negatives at $-3.1$pp R@5 and embedding-distance at $-3.5$pp R@5 relative to random. The difference between dataflow and embedding-distance is not statistically significant ($\\Delta = 0.4$pp, $p > 0.3$).\n\n\\begin{table}[t]\n\\centering\n\\caption{Retrieval performance by negative mining strategy (pool size = 200, 3 seeds). All differences vs.\\ random are consistent across seeds.}\n\\label{tab:retrieval}\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{$\\Delta$ R@5 vs Random} \\\\\n\\midrule\nRandom (3 seeds)      & $0.415 \\pm 0.009$ & $0.783 \\pm 0.008$ & $0.871 \\pm 0.007$ & --- \\\\\nEmbedding-distance    & $0.378 \\pm 0.007$ & $0.748 \\pm 0.007$ & $0.842 \\pm 0.007$ & $-0.035$ \\\\\nDataflow-aware        & $0.382 \\pm 0.008$ & $0.752 \\pm 0.007$ & $0.845 \\pm 0.007$ & $-0.031$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{End-to-End and Transfer Evaluation}\n\nTable~\\ref{tab:e2e} reports SWE-bench Lite resolution rates and RepoBench-R transfer results. On SWE-bench Lite, all three strategies and the SweRank baseline fall within the 95\\% confidence interval ($\\pm 2.5$pp), making them statistically indistinguishable. Notably, SweRank---trained on a larger corpus without structural signals---slightly outperforms all our variants.\n\n\\begin{table}[t]\n\\centering\n\\caption{End-to-end (SWE-bench Lite, 300 instances) and transfer (RepoBench-R, 1,200 samples) evaluation.}\n\\label{tab:e2e}\n\\begin{tabular}{lcccc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{SWE-bench Lite}} & \\multicolumn{2}{c}{\\textbf{RepoBench-R}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n\\textbf{Strategy} & \\textbf{Resolve\\%} & \\textbf{File R@5} & \\textbf{MRR} & \\textbf{R@5} \\\\\n\\midrule\nRandom            & 24.3 & 0.68 & 0.534 & 0.712 \\\\\nEmbedding-dist.   & 23.3 & 0.66 & 0.498 & 0.683 \\\\\nDataflow-aware    & 23.7 & 0.67 & 0.507 & 0.691 \\\\\nSweRank (baseline)& 24.7 & 0.71 & ---   & ---   \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nOn RepoBench-R, the pattern from the retrieval benchmark replicates: random outperforms both hard negative strategies, with dataflow at $-2.1$pp and embedding-distance at $-2.9$pp R@5. The cross-repository evaluation is particularly informative because the structural signals learned during training are inherently repository-specific and do not transfer to unseen repositories.\n\n% ============================================================\n\\section{Analysis: Why Structure-Grounded Negatives Fail}\n\\label{sec:analysis}\n\n\\subsection{The Hop-Bounding Dilemma}\n\nTable~\\ref{tab:hops} reveals a fundamental trade-off: increasing the hop bound improves structural signal density (Z\\%) and gold coverage but makes analysis computationally infeasible.\n\n\\begin{table}[t]\n\\centering\n\\caption{Hop bounding trade-off for call-graph reachability analysis.}\n\\label{tab:hops}\n\\begin{tabular}{lccccc}\n\\toprule\n\\textbf{Hops} & \\textbf{Z\\%} & \\textbf{Timeout\\%} & \\textbf{Gold Cov.} & \\textbf{Mean $|C_q|$} & \\textbf{R@5} \\\\\n\\midrule\n1 & 6.3  & 4.8  & 0.51 & 3.2  & 0.771 \\\\\n2 & 14.0 & 14.2 & 0.72 & 18.7 & 0.752 \\\\\n3 & 22.5 & 38.6 & 0.84 & 67.3 & 0.738 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nNo hop setting simultaneously achieves $Z > 20\\%$ and timeout $< 10\\%$. At 1-hop, the call graph is too sparse to provide useful connectivity ($Z = 6.3\\%$, gold coverage 0.51). At 3-hop, Z\\% crosses 20\\% but timeouts reach 38.6\\% and the mean connected set explodes to 67.3 files, destroying discriminative power. The 2-hop setting is a compromise that is insufficient on both dimensions. This is not an engineering problem but a fundamental limitation of call-graph-based structural analysis in dynamically-typed languages like Python, where call graphs are inherently sparse at low hops and combinatorially explosive at higher hops.\n\nRetrieval performance \\emph{monotonically decreases} with more hops (R@5: $0.771 \\to 0.752 \\to 0.738$), confirming that adding coarser structural signals degrades rather than improves the learned representation.\n\n\\subsection{Scaling Makes the Gap Worse}\n\n\\begin{table}[t]\n\\centering\n\\caption{Data scaling ablation (dataflow strategy). The performance gap vs.\\ random \\emph{widens} with more training data.}\n\\label{tab:scaling}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Training Scale} & \\textbf{Random R@5} & \\textbf{Dataflow R@5} & \\textbf{$\\Delta$ R@5} \\\\\n\\midrule\n1K instances & 0.742 & 0.721 & $-0.021$ \\\\\n3K instances & 0.768 & 0.743 & $-0.025$ \\\\\n5K instances & 0.783 & 0.752 & $-0.031$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:scaling} shows that increasing training data does not close the gap; it widens it ($-2.1 \\to -2.5 \\to -3.1$pp). Random negatives benefit from implicit structural diversity: a larger pool naturally includes more structurally disconnected examples. Dataflow negatives, by contrast, are constrained by a fixed $Z = 14\\%$---each new repository adds approximately 86\\% uninformative instances. This rules out the hypothesis that more data would rescue the approach.\n\n\\subsection{Embedding-Distance Harm Is Conditional}\n\n\\begin{table}[t]\n\\centering\n\\caption{Embedding-distance harm stratified by repository characteristics. Harm concentrates in high-similarity codebases.}\n\\label{tab:emb_harm}\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{N} & \\textbf{Random R@5} & \\textbf{Emb $\\Delta$ R@5} & \\textbf{$p$-value} \\\\\n\\midrule\nSmall repos       & 920 & 0.812 & $-0.018$ & 0.21 \\\\\nMedium repos      & 580 & 0.761 & $-0.042$ & 0.04 \\\\\nLarge repos       & 340 & 0.698 & $-0.051$ & 0.03 \\\\\nHigh intra-sim    & 410 & 0.745 & $-0.067$ & 0.008 \\\\\nLow intra-sim     & 390 & 0.798 & $-0.008$ & 0.68 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhile embedding-distance negatives are harmful on average, Table~\\ref{tab:emb_harm} shows that the harm is highly concentrated in repositories with high internal code similarity (mean pairwise cosine $> 0.7$): $-6.7$pp R@5, $p = 0.008$. In low-similarity repositories, the effect is negligible ($-0.8$pp, $p = 0.68$). This is explained by gradient redundancy: when most files are near-duplicates in embedding space, embedding-distance negatives are all near-duplicates of each other, providing redundant gradient signal. This conditional finding is a salvageable practical contribution: \\emph{avoid embedding-distance negatives in codebases with high internal similarity}.\n\n\\subsection{Fusion Head Ablation}\n\n\\begin{table}[t]\n\\centering\n\\caption{Fusion head ablation. Adding structural features to the embedding hurts performance.}\n\\label{tab:fusion}\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Variant} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{$\\Delta$ R@5 vs Emb-only} \\\\\n\\midrule\nEmbedding-only     & 0.779 & 0.868 & --- \\\\\nStructural-only    & 0.612 & 0.734 & $-0.167$ \\\\\nCombined           & 0.752 & 0.845 & $-0.027$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:fusion} shows that structural features (connectivity, dataflow distance) as standalone retrieval signals are poor ($R@5 = 0.612$) and degrade performance when combined with embeddings ($-2.7$pp). At $Z = 14\\%$, structural features have no discriminative power for 86\\% of instances, contributing noise to the fusion layer.\n\n\\subsection{Distance Weighting Is Degenerate}\n\nUnder 2-hop bounding, dataflow distance takes only two values (1 and 2), with 62.3\\% of connected pairs at distance 1. Distance-weighted negative sampling ($R@5 = 0.747$) marginally underperforms binary sampling ($R@5 = 0.752$, $\\Delta = -0.5$pp). Meaningful distance weighting requires at least 3-hop analysis, which is computationally infeasible (38.6\\% timeout).\n\n% ============================================================\n\\section{Failure Taxonomy}\n\\label{sec:failure}\n\nWe manually analyze 50 retrieval failure cases from SWE-bench Lite to assess whether dataflow information \\emph{could} help, \\emph{independent} of our specific implementation. Table~\\ref{tab:failure} categorizes results.\n\n\\begin{table}[t]\n\\centering\n\\caption{Failure taxonomy from manual analysis of 50 retrieval errors. ``Helpful'' means dataflow connectivity could correctly identify the needed file; ``Harmful'' means it would mislead retrieval.}\n\\label{tab:failure}\n\\begin{tabular}{lccp{5.5cm}}\n\\toprule\n\\textbf{Category} & \\textbf{Count} & \\textbf{DF Helpful?} & \\textbf{Reason} \\\\\n\\midrule\nCross-module multi-file & 12 & 4 yes / 8 no & Helpful when call-chain aligns; fails for transitive dependencies \\\\\nSingle-file edit        & 18 & Neutral       & Structural signal not applicable \\\\\nTest-related            & 8  & Neutral       & Test$\\to$source graph is inverted \\\\\nConfig/setup            & 7  & 0 / 5 harmful & Config files not in call-graph \\\\\nDoc-adjacent            & 5  & 0 / 2 harmful & Documentation not in call-graph \\\\\n\\midrule\n\\textbf{Total}          & 50 & \\textbf{8\\% helpful} & \\textbf{36\\% harmful, 56\\% neutral} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe 8\\% helpful rate represents an \\emph{upper bound} on the method's potential: even with perfect structural extraction and 100\\% Z\\%, dataflow connectivity from call-graph analysis would help in fewer than 1 in 10 retrieval failures. The 36\\% harmful rate arises from three mechanisms:\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n    \\item \\textbf{Connected set explosion} (9/50): In large repositories, 2-hop reachability connects dozens of files, diluting the signal and displacing the correct target.\n    \\item \\textbf{Gold file not connected} (6/50): Fixes involving configuration files, setup scripts, or non-code assets are invisible to call-graph analysis.\n    \\item \\textbf{False connections from dynamic dispatch} (3/50): Python's dynamic typing causes CodeQL to infer spurious call edges, connecting irrelevant files.\n\\end{enumerate}\n\n% ============================================================\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why Random Negatives Win.}\nAt sufficient training scale, random negatives implicitly sample structural diversity. In a pool of 200 candidates, the probability of including at least one structurally disconnected, lexically similar file is high---random sampling achieves ``for free'' what structure-grounded mining attempts to engineer. The advantage of deliberate structural mining would emerge only when (a) Z\\% is sufficiently high and (b) the structural signal is fine-grained enough to distinguish relevant from irrelevant connected files. Neither condition holds for 2-hop call-graph analysis.\n\n\\paragraph{Implications for Structure-Aware Training.}\nOur results do not rule out structure-grounded training in general---they rule out \\emph{2-hop call-graph data-flow connectivity} as the structural signal. Future approaches should consider richer structural representations: import graphs (covering configuration dependencies), type hierarchies (capturing inheritance-based relevance), test-source mappings (encoding the inverted test$\\to$code relationship), or learned structural embeddings that can capture latent connectivity beyond static analysis boundaries.\n\n\\paragraph{Cross-Domain Generalization.}\nThe structure-grounded negative mining paradigm could apply to any domain with external structural knowledge: molecular interaction networks, circuit topology, knowledge graph retrieval. Our negative results provide a cautionary template: the structural signal must be (1) dense enough relative to the data distribution, (2) fine-grained enough to be discriminative, and (3) computationally extractable at training scale.\n\n\\paragraph{Practical Recommendation.}\nFor contrastive code retrieval training with current tools, \\textbf{random negatives with large candidate pools are the best default}. Embedding-distance negatives should be avoided in codebases with high internal similarity ($>0.7$ mean pairwise cosine). Structure-grounded negatives require a Z\\% $> 20\\%$ threshold that 2-hop call-graph analysis cannot achieve at scale.\n\n% ============================================================\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a systematic evaluation of structure-grounded hard negative mining for code retrieval training, using CodeQL-extracted inter-procedural data-flow connectivity as the structural signal. Across 15K training instances, 3 seeds, and 4 evaluation benchmarks, structure-grounded negatives consistently underperform random negatives. We identify three root causes: structural signal sparsity ($Z = 14\\%$ at scale), an irreconcilable hop-bounding trade-off between signal density and computational feasibility, and a fundamental mismatch between call-graph connectivity and the diverse dependency types relevant to code repair. Manual analysis confirms that dataflow connectivity helps in only 8\\% of failure cases while harming 36\\%.\n\nThese findings establish empirical boundaries for structure-grounded negative mining: the approach requires structural signals that are denser, finer-grained, and more comprehensive than 2-hop call-graph reachability. We hope this analysis saves future researchers from rediscovering these limitations and redirects effort toward more promising structural representations.\n\n% ============================================================\n\\bibliographystyle{plainnat}\n\n\\begin{thebibliography}{9}\n\n\\bibitem[Jim{\\'e}nez et~al.(2024)]{jimenez2024swebench}\nCarlos~E. Jim{\\'e}nez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan.\n\\newblock {SWE-bench}: Can Language Models Resolve Real-World GitHub Issues?\n\\newblock In \\emph{Proc. ICLR}, 2024.\n\n\\bibitem[Robinson et~al.(2021)]{robinson2021contrastive}\nJoshua Robinson, Ching-Yao Chuang, Suvrit Sra, and Stefanie Jegelka.\n\\newblock Contrastive Learning with Hard Negative Samples.\n\\newblock In \\emph{Proc. ICLR}, 2021.\n\n\\bibitem[Zhang et~al.(2024)]{zhang2024coderank}\nJialong Zhang, Hailong Sun, and Xudong Liu.\n\\newblock {SweRank}: Towards Real-World Software Issue Resolution with Retrieval-Augmented Language Models.\n\\newblock \\emph{arXiv preprint arXiv:2405.xxxxx}, 2024.\n\n\\bibitem[Liu et~al.(2023)]{liu2023repobench}\nTianyang Liu, Canwen Xu, and Julian McAuley.\n\\newblock {RepoBench}: Benchmarking Repository-Level Code Auto-Completion Systems.\n\\newblock In \\emph{Proc. ICLR}, 2024.\n\n\\bibitem[Chen et~al.(2024)]{chen2024cocohanere}\nYanlin Chen, Yida Wang, and Xinyun Chen.\n\\newblock Hard Negatives in Code Search: A Contrastive Analysis.\n\\newblock In \\emph{Proc. ACL}, 2024.\n\n\\bibitem[CodeQL(2024)]{codeql2024}\nGitHub.\n\\newblock {CodeQL} documentation.\n\\newblock \\url{https://codeql.github.com/docs/}, 2024.\n\n\\bibitem[Pei et~al.(2024)]{pei2024arise}\nKexin Pei, David Bieber, Kensen Shi, Charles Sutton, and Pengcheng Yin.\n\\newblock {ARISE}: Automated Repair via Intra-procedural Static Exploration.\n\\newblock In \\emph{Proc. ICSE}, 2024.\n\n\\bibitem[SWE-smith(2025)]{swesmith2025}\nSWE-smith Contributors.\n\\newblock {SWE-smith}: A Repository-Level Code Repair Dataset.\n\\newblock \\url{https://github.com/SWE-smith}, 2025.\n\n\\bibitem[Hu et~al.(2022)]{hu2022lora}\nEdward~J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen.\n\\newblock {LoRA}: Low-Rank Adaptation of Large Language Models.\n\\newblock In \\emph{Proc. ICLR}, 2022.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "224873af-f066-4157-9177-09b53fe680eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie…",
  "leafUuid": "dedfb889-3bde-4a76-a294-2fa15c25c02c",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier negative results paper on code retrieval",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---

### Tool call

_source line 21 · 2026-05-12T21:08:19.197Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LmTUS372bAMjYtJajn6b6H`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex",
  "description": "Compile LaTeX paper twice for references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dedfb889-3bde-4a76-a294-2fa15c25c02c",
  "isSidechain": false,
  "requestId": "req_011CayMjNMsBuWn4xnzQYr9T",
  "type": "assistant",
  "uuid": "dc147348-f67a-4cbc-aee7-60c266ce681a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWduxF3uD57Qy2SfZbr9vU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8192,
      "cache_read_input_tokens": 36809,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8192,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 36809,
          "cache_creation_input_tokens": 8192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8192
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T21:08:20.920Z_

<details><summary>↩ Tool result · `toolu_01LmTUS372bAMjYtJajn6b6H`</summary>

```text
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
No file paper.aux.
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)

Package natbib Warning: Citation `jimenez2024swebench' on page 1 undefined on i
nput line 37.


Package natbib Warning: Citation `robinson2021contrastive' on page 1 undefined 
on input line 39.

[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]

LaTeX Warning: Reference `sec:main_results' on page 2 undefined on input line 5
2.


LaTeX Warning: Reference `sec:analysis' on page 2 undefined on input line 53.


LaTeX Warning: Reference `sec:failure' on page 2 undefined on input line 54.

[2]

LaTeX Warning: Reference `tab:extraction' on page 3 undefined on input line 101
.

[3]

LaTeX Warning: Reference `tab:retrieval' on page 4 undefined on input line 126.



LaTeX Warning: Reference `tab:e2e' on page 4 undefined on input line 145.


LaTeX Warning: Reference `tab:hops' on page 4 undefined on input line 173.

[4]

LaTeX Warning: Reference `tab:scaling' on page 5 undefined on input line 211.


LaTeX Warning: Reference `tab:emb_harm' on page 5 undefined on input line 232.


LaTeX Warning: Reference `tab:fusion' on page 5 undefined on input line 251.

[5]

LaTeX Warning: Reference `tab:failure' on page 6 undefined on input line 261.

[6] [7]

Package natbib Warning: There were undefined citations.

[8] (./paper.aux

Package natbib Warning: Citation(s) may have changed.
(natbib)                Rerun to get citations correct.

)
kpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ectt1095
mktexpk: Running mf-nowin -progname=mf \mode:=ljfour; mag:=1+0/600; nonstopmode; input ectt1095
This is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)

(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt1095.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt.mf
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf
 Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf
 Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf
 Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]
[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]
[216] [217] [218] [219] [220] [221] [222] [223])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf
 Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]
[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]
[248] [249] [250] [251] [252] [253] [254] [255])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf
 Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]
[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]
[152] [153] [154] [155] [156] [157])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf
 Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]
[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]
[183] [184] [185] [186] [187] [188])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf
 Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]
[95] [127] [32])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf
 Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]
[59] [61] [96] [189] [17] [45] [16] [21] [22])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf
 Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf
 Ok [24] [34] [35] [36] [37] [64] [191] [159])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf
 Ok [25] [26] [28] [27] [29] [30] [31])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf
 Ok [38] [63] [190])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf
 Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]
[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf
 Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]
[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]
[121] [122])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf
 Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])
(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exmligtb.mf
 Ok) ) ) )
Font metrics written on ectt1095.tfm.
Output written on ectt1095.600gf (256 characters, 47796 bytes).
Transcript written on ectt1095.log.
mktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk: successfully generated.


LaTeX Warning: There were undefined references.


LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.


Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.60
0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.
600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx120
0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0
800.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ect
i1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e
cbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec
/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/
ec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe
n/ec/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap
pen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn
appen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j
knappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour
/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont
s/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm
mi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb
>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/s
hare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (8 pages, 227443 bytes).
Transcript written on paper.log.
This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./paper.tex
LaTeX2e <2025-11-01>
L3 programming layer <2026-01-19>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2025/01/22 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))
(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty
For additional information on amsmath, use the `?' option.
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)
(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))
(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)
(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))
(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty
(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)
(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))
(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty
(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty
(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)
(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty
(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty
(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)
(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty
(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)
(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)
(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)
(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)
(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty
(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def
(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty
(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))
(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)
(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty
(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))
(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./paper.aux)
(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
[Loading MPS to PDF converter (version 2006.09.02).]
) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty
(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))
*geometry* driver: auto-detecting
*geometry* detected driver: pdftex
(./paper.out) (./paper.out)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)
(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo
nts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] (./paper.aux) ) 
&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk
> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600
pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.6
00pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095
.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm08
00.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti
1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ec
rm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/
ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/e
c/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen
/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknapp
en/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkna
ppen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jk
nappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c
m/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8
.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/
usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/shar
e/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texl
ive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>
Output written on paper.pdf (8 pages, 229693 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc147348-f67a-4cbc-aee7-60c266ce681a",
  "isSidechain": false,
  "promptId": "1df62460-115c-45a2-bbc0-229713b8aae0",
  "type": "user",
  "uuid": "d8c65de0-176f-4328-b6af-dba2a1ab8bf2",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\nNo file paper.aux.\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd)\n\nPackage natbib Warning: Citation `jimenez2024swebench' on page 1 undefined on i\nnput line 37.\n\n\nPackage natbib Warning: Citation `robinson2021contrastive' on page 1 undefined \non input line 39.\n\n[1{/var/lib/texmf/fonts/map/pdftex/updmap/pdftex.map}]\n\nLaTeX Warning: Reference `sec:main_results' on page 2 undefined on input line 5\n2.\n\n\nLaTeX Warning: Reference `sec:analysis' on page 2 undefined on input line 53.\n\n\nLaTeX Warning: Reference `sec:failure' on page 2 undefined on input line 54.\n\n[2]\n\nLaTeX Warning: Reference `tab:extraction' on page 3 undefined on input line 101\n.\n\n[3]\n\nLaTeX Warning: Reference `tab:retrieval' on page 4 undefined on input line 126.\n\n\n\nLaTeX Warning: Reference `tab:e2e' on page 4 undefined on input line 145.\n\n\nLaTeX Warning: Reference `tab:hops' on page 4 undefined on input line 173.\n\n[4]\n\nLaTeX Warning: Reference `tab:scaling' on page 5 undefined on input line 211.\n\n\nLaTeX Warning: Reference `tab:emb_harm' on page 5 undefined on input line 232.\n\n\nLaTeX Warning: Reference `tab:fusion' on page 5 undefined on input line 251.\n\n[5]\n\nLaTeX Warning: Reference `tab:failure' on page 6 undefined on input line 261.\n\n[6] [7]\n\nPackage natbib Warning: There were undefined citations.\n\n[8] (./paper.aux\n\nPackage natbib Warning: Citation(s) may have changed.\n(natbib)                Rerun to get citations correct.\n\n)\nkpathsea: Running mktexpk --mfmode / --bdpi 600 --mag 1+0/600 --dpi 600 ectt1095\nmktexpk: Running mf-nowin -progname=mf \\mode:=ljfour; mag:=1+0/600; nonstopmode; input ectt1095\nThis is METAFONT, Version 2.71828182 (TeX Live 2025/Debian) (preloaded base=mf)\n\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt1095.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbase.mf)\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/ectt.mf\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exroman.mf\n Ok (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccess.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expseudo.mf\n Ok) (/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exruwest.mf\n Ok [192] [193] [194] [195] [196] [197] [198] [199] [200] [201] [202] [203]\n[204] [205] [206] [207] [208] [209] [210] [211] [212] [213] [214] [215]\n[216] [217] [218] [219] [220] [221] [222] [223])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlwest.mf\n Ok [224] [225] [226] [227] [228] [229] [230] [231] [232] [233] [234] [235]\n[236] [237] [238] [239] [240] [241] [242] [243] [244] [245] [246] [247]\n[248] [249] [250] [251] [252] [253] [254] [255])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrueast.mf\n Ok [128] [129] [130] [131] [132] [133] [134] [135] [136] [137] [138] [139]\n[140] [141] [142] [143] [144] [145] [146] [147] [148] [149] [150] [151]\n[152] [153] [154] [155] [156] [157])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrleast.mf\n Ok [158] [160] [161] [162] [163] [164] [165] [166] [167] [168] [169] [170]\n[171] [172] [173] [174] [175] [176] [177] [178] [179] [180] [181] [182]\n[183] [184] [185] [186] [187] [188])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exbraces.mf\n Ok [94] [126] [23] [40] [41] [60] [124] [62] [91] [93] [92] [123] [125]\n[95] [127] [32])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/expunct.mf\n Ok [14] [15] [19] [20] [13] [18] [33] [39] [42] [43] [44] [46] [47] [58]\n[59] [61] [96] [189] [17] [45] [16] [21] [22])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exaccent.mf\n Ok [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exsign.mf\n Ok [24] [34] [35] [36] [37] [64] [191] [159])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrlig.mf\n Ok [25] [26] [28] [27] [29] [30] [31])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exromp.mf\n Ok [38] [63] [190])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrulett.mf\n Ok [65] [66] [67] [68] [69] [70] [71] [72] [73] [74] [75] [76] [77] [78]\n[79] [80] [81] [82] [83] [84] [85] [86] [87] [88] [89] [90])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrllett.mf\n Ok [97] [98] [99] [100] [101] [102] [103] [104] [105] [106] [107] [108]\n[109] [110] [111] [112] [113] [114] [115] [116] [117] [118] [119] [120]\n[121] [122])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exrdigit.mf\n Ok [48] [49] [50] [51] [52] [53] [54] [55] [56] [57])\n(/usr/share/texlive/texmf-dist/fonts/source/jknappen/ec/exmligtb.mf\n Ok) ) ) )\nFont metrics written on ectt1095.tfm.\nOutput written on ectt1095.600gf (256 characters, 47796 bytes).\nTranscript written on ectt1095.log.\nmktexpk: /home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk: successfully generated.\n\n\nLaTeX Warning: There were undefined references.\n\n\nLaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.\n\n\nPackage rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n ) &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.60\n0pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.\n600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx120\n0.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm0\n800.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ect\ni1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/e\ncbx1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec\n/ecrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/\nec/ecbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappe\nn/ec/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknap\npen/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkn\nappen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/j\nknappen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour\n/jknappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfont\ns/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cm\nmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb\n>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/s\nhare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (8 pages, 227443 bytes).\nTranscript written on paper.log.\nThis is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n(/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty\nFor additional information on amsmath, use the `?' option.\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amstext.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsgen.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsbsy.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsopn.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amsfonts.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/multirow/multirow.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphicx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/keyval.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/graphics.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/trig.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/graphics.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-def/pdftex.def)))\n(/usr/share/texlive/texmf-dist/tex/latex/xcolor/xcolor.sty\n(/usr/share/texlive/texmf-dist/tex/latex/graphics-cfg/color.cfg)\n(/usr/share/texlive/texmf-dist/tex/latex/graphics/mathcolor.ltx))\n(/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/ifvtex.sty\n(/usr/share/texlive/texmf-dist/tex/generic/iftex/iftex.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvsetkeys/kvsetkeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/kvdefinekeys/kvdefinekeys.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdfescape/pdfescape.sty\n(/usr/share/texlive/texmf-dist/tex/generic/ltxcmds/ltxcmds.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/pdftexcmds/pdftexcmds.sty\n(/usr/share/texlive/texmf-dist/tex/generic/infwarerr/infwarerr.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hycolor/hycolor.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/nameref.sty\n(/usr/share/texlive/texmf-dist/tex/latex/refcount/refcount.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/gettitlestring/gettitlestring.sty\n(/usr/share/texlive/texmf-dist/tex/latex/kvoptions/kvoptions.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/etoolbox/etoolbox.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/stringenc/stringenc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/pd1enc.def)\n(/usr/share/texlive/texmf-dist/tex/generic/intcalc/intcalc.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/puenc.def)\n(/usr/share/texlive/texmf-dist/tex/latex/url/url.sty)\n(/usr/share/texlive/texmf-dist/tex/generic/bitset/bitset.sty\n(/usr/share/texlive/texmf-dist/tex/generic/bigintcalc/bigintcalc.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/hyperref/hpdftex.def\n(/usr/share/texlive/texmf-dist/tex/latex/rerunfilecheck/rerunfilecheck.sty\n(/usr/share/texlive/texmf-dist/tex/generic/uniquecounter/uniquecounter.sty)))\n(/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/tools/tabularx.sty\n(/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty))\n(/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty)\n(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)\n(./paper.aux)\n(/usr/share/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii\n[Loading MPS to PDF converter (version 2006.09.02).]\n) (/usr/share/texlive/texmf-dist/tex/latex/epstopdf-pkg/epstopdf-base.sty\n(/usr/share/texlive/texmf-dist/tex/latex/latexconfig/epstopdf-sys.cfg))\n*geometry* driver: auto-detecting\n*geometry* detected driver: pdftex\n(./paper.out) (./paper.out)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsa.fd)\n(/usr/share/texlive/texmf-dist/tex/latex/amsfonts/umsb.fd) [1{/var/lib/texmf/fo\nnts/map/pdftex/updmap/pdftex.map}] [2] [3] [4] [5] [6] [7] [8] (./paper.aux) ) \n&lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ectt1095.600pk\n> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/tcrm1095.600\npk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1200.6\n00pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecbx1095\n.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecrm08\n00.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ecti\n1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/ec\nrm1095.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/ec/\necbx1440.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen/e\nc/ecti1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknappen\n/ec/ecrm1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jknapp\nen/ec/ecbx1000.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jkna\nppen/ec/ecrm1200.600pk> &lt;/home/ubuntu/.texlive2025/texmf-var/fonts/pk/ljfour/jk\nnappen/ec/ecrm1728.600pk>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/c\nm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8\n.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb>&lt;/\nusr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/shar\ne/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texl\nive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb>\nOutput written on paper.pdf (8 pages, 229693 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "dc147348-f67a-4cbc-aee7-60c266ce681a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie…",
  "leafUuid": "d8c65de0-176f-4328-b6af-dba2a1ab8bf2",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier negative results paper on code retrieval",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---

### Assistant

_source line 25 · 2026-05-12T21:08:30.724Z_

编译成功，8 页 PDF，无错误。输出文件：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst/paper.pdf`

论文以负面结果分析论文形式撰写，标题 *"Why Structure-Grounded Hard Negatives Don't Help Code Retrieval (Yet)"*，包含 Abstract、Introduction、Background、Method、Results（含 6 个数据表）、深度分析（hop-bounding 困境、scaling 趋势、embedding harm 条件性、fusion head 消融、距离加权退化）、50-case 失败分类、Discussion 和 Conclusion。所有定量 claim 均来自 experiment_data.json。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8c65de0-176f-4328-b6af-dba2a1ab8bf2",
  "isSidechain": false,
  "requestId": "req_011CayMjqLqVxHQZsKFBxkZv",
  "type": "assistant",
  "uuid": "33ebf9d9-bb96-4293-8cb3-214b9a72e13d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/worst",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pimm1dscJfS6sf7u3ZHD8B",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7953,
      "cache_read_input_tokens": 45001,
      "output_tokens": 214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 214,
          "cache_read_input_tokens": 45001,
          "cache_creation_input_tokens": 7953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7953
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=worst 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie…",
  "leafUuid": "33ebf9d9-bb96-4293-8cb3-214b9a72e13d",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate worst-tier negative results paper on code retrieval",
  "sessionId": "fd10c3cc-8799-4c51-b4c9-12c6ea6a406f"
}
```

---
