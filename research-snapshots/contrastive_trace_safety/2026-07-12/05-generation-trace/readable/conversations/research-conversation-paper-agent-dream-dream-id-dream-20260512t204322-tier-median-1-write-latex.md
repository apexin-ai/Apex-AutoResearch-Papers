# Research conversation: 你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=median 生成一篇完整的模拟论文。 ## 关键规则 1. 用 **Write 工具** 把 LaTeX 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/c30881e3-a41d-414e-9322-79161ab758fc.jsonl`
- **Structured JSON:** [`b71d925077b668ac6e1c.json`](../../sessions/b7/b71d925077b668ac6e1c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T21:01:31.691Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T21:01:31.691Z",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "content": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=median 生成一篇完整的模拟论文。\n\n## 关键规则\n1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex`\n2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`\n3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/`，禁止写入其他目录\n4. 直接写完整 LaTeX 全文（\\documentclass ... \\end{document}），不要输出 YAML/JSON/Markdown\n5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完\n\n## 输入\n- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json`（先 Read 此文件）\n- Venue：默认\n- Narrative guidance：Pivot primary claim from \"dataflow wins\" to \"embedding-distance negatives are harmful — a cautionary result for the contrastive code retrieval community.\" Claim 2 becomes the headline; Claim 1 downgrades to \"dataflow negatives are a viable alternative that avoids the pitfalls of embedding-distance negatives without degrading performance.\" Claim 3 (scalability methodology) survives as-is. Add ceiling analysis: why doesn't structural signal help more? Hypotheses include insufficient Z% density, noise in CodeQL reachability, or random negatives already being near-optimal when pool diversity is high. Failure analysis (plan_011) becomes critical for explaining the gap. Title pivot: emphasize \"when hard negatives hurt\" angle. Target: EMNLP Findings or resubmit cycle.\n\n- paper_framing.md 节选：\n# Paper Framing — StructFuse\n\n## Target Venue\n- Primary: EMNLP 2026 Main\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026\n\n## Core Claims (3)\n\n1. **Structure-grounded hard negatives outperform embedding-distance and random negatives for contrastive code retrieval training.** Inter-procedural data-flow connectivity provides a complementary signal dimension that textual similarity cannot recover — files that are lexically similar but structurally disconnected force the model to internalize structural relevance beyond surface features.\n\n2. **Embedding-distance hard negatives actively harm code retrieval compared to random negatives.** The gradient signal from embedding-distance negatives is partially redundant with the encoder's learned similarity, leading to degraded retrieval quality. (MVP evidence: -3.7pp recall@1 at pool=50, -27pp at pool=26, 3 seeds consistent.)\n\n3. **Scope-bounded inter-procedural data-flow analysis via CodeQL is a scalable, model-independent method for computing structural connectivity.** With 2-hop call-graph bounding, timeout <5%, and >40% of instances have connected-but-not-gold structural signals at scale.\n\n## Story Spine\n\n- **Problem**: Repo-level code repair requires selecting relevant files from large codebases. Current retrievers conflate lexical similarity with structural relevance — a file sharing function names with the buggy code may be structurally unrelated, while a data-flow-connected file may contain the actual fix dependency.\n\n- **Existing approaches & gaps**:\n  - Text-based (SweRank, SWE-Fixer): blind to structural dependencies\n  - Graph-guided (LocAgent, RANGER, CodexGraph): structural graphs at inference only, no data-flow edges, no training signal\n  - ARISE: data-flow but intra-procedural only (no call boundary crossing), runtime tool calls only\n  - CoCoHaNeRe: hard negatives improve code search, but embedding-distance negatives are redundant with encoder similarity\n\n- **Our framing**: The key gap is using structural connectivity for **training signal**, not just inference-time navigation. Structure-grounded hard negatives — lexically similar but data-flow disconnected files — provide a complementary learning signal. This is a general paradigm: any domain with external structural knowledge (molecular networks, circuit topology, KG retrieval) can use drift-immune structure-grounded negative mining. Code is the ideal testbed due to formal semantic guarantees.\n\n- **Headline result template**: \"On SWE-bench Lite, StructFuse with data-flow-aware hard negatives achieves X% recall@5 while embedding-distance negatives achieve Y% and random negatives Z%, demonstrating that structure-grounded negative mining provides training signal that text-based methods cannot recover.\"\n\n## Dual-Pillar Motivation (per Human Review)\n\n1. **Primary — Complementary signal dimension**: Structural connectivity encodes a relevance dimension entirely absent from textual signals. No amount of text-based training can recover inter-procedural data-flow relationships from token sequences alone.\n2. **Secondary — Selection drift immunity**: Structural graph is externally fixed; negative set does not drift with encoder updates (unlike embedding-distance negatives which shift every epoch).\n\n## Formal Definition\n\nGiven retrieval domain D, structural graph G, similarity function s, query q:\n**structure-grounded hard negative** = argmax_{x ∈ D : s(x,q) > τ ∧ ¬reachable_G(x,q)} s(x,q)\n\nThe structural graph is externally fixed and does not update with the encoder.\n\n## Title\n\n\"StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval\"\n(Per Human Review: emphasize methodology, de-emphasize SE-specific framing)\n\n## Venue Fit Risks\n\n1. **EMNLP vs SE**: Frame as contrastive learning methodology with code as instantiation\n2. **Domain-specific concern**: Cross-domain generalization in Discussion (molecular networks, circuit topology, KG retrieval)\n3. **Incremental contribution**: Novelty is i\n\n## 质量目标\n\"够审\"级——让审稿人能评判 idea 和实验设计，不是投稿质量。包含 Abstract、Introduction、Method、Experiments、Conclusion。每个定量 claim 基于 experiment_data.json 中的数据，不得编造数字。"
}
```

---

### Runtime record

_source line 2 · 2026-05-12T21:01:31.696Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T21:01:31.696Z",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc"
}
```

---

## Round 1

37 recorded events

### User

_source line 3 · 2026-05-12T21:01:31.728Z_

你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=median 生成一篇完整的模拟论文。

## 关键规则
1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex`
2. 用 **Bash 工具** 编译：`cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median && pdflatex -interaction=nonstopmode paper.tex && pdflatex -interaction=nonstopmode paper.tex`
3. 所有文件只写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/`，禁止写入其他目录
4. 直接写完整 LaTeX 全文（\documentclass ... \end{document}），不要输出 YAML/JSON/Markdown
5. 不走 5 步流水线，不 spawn Worker，不调 Director API——一次性写完

## 输入
- 实验数据（JSON）：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json`（先 Read 此文件）
- Venue：默认
- Narrative guidance：Pivot primary claim from "dataflow wins" to "embedding-distance negatives are harmful — a cautionary result for the contrastive code retrieval community." Claim 2 becomes the headline; Claim 1 downgrades to "dataflow negatives are a viable alternative that avoids the pitfalls of embedding-distance negatives without degrading performance." Claim 3 (scalability methodology) survives as-is. Add ceiling analysis: why doesn't structural signal help more? Hypotheses include insufficient Z% density, noise in CodeQL reachability, or random negatives already being near-optimal when pool diversity is high. Failure analysis (plan_011) becomes critical for explaining the gap. Title pivot: emphasize "when hard negatives hurt" angle. Target: EMNLP Findings or resubmit cycle.

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
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "63702478-f157-42b9-ac6a-591a03b62395",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T21:01:31.726Z_

```json
{
  "parentUuid": "63702478-f157-42b9-ac6a-591a03b62395",
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
  "uuid": "ed87d53e-3822-4b7e-8bf0-17444681b82a",
  "timestamp": "2026-05-12T21:01:31.726Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T21:01:31.726Z_

```json
{
  "parentUuid": "ed87d53e-3822-4b7e-8bf0-17444681b82a",
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
  "uuid": "792e6786-a727-4680-8dc8-f32deeeb97f4",
  "timestamp": "2026-05-12T21:01:31.726Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-12T21:01:31.726Z_

```json
{
  "parentUuid": "792e6786-a727-4680-8dc8-f32deeeb97f4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1c23aaae-3adf-4210-9ee8-a6892464fdeb",
  "timestamp": "2026-05-12T21:01:31.726Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
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
  "aiTitle": "Generate StructFuse median-tier simulation paper",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc"
}
```

---

### Assistant

_source line 8 · 2026-05-12T21:01:34.599Z_

I'll start by reading the experiment data and any other relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c23aaae-3adf-4210-9ee8-a6892464fdeb",
  "isSidechain": false,
  "requestId": "req_011CayMDg5PbbTZ9Je4s95L1",
  "type": "assistant",
  "uuid": "0d798f9f-cfab-48a9-9223-f3ed73f3b87b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSdYw9g8mtXVzBaxVbfefq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12472,
      "cache_read_input_tokens": 11447,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12472
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

_source line 9 · 2026-05-12T21:01:35.782Z_

<details open><summary>🔧 Tool call — Read · `toolu_015pS7kJZPymqaZWSSV1M7P3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d798f9f-cfab-48a9-9223-f3ed73f3b87b",
  "isSidechain": false,
  "requestId": "req_011CayMDg5PbbTZ9Je4s95L1",
  "type": "assistant",
  "uuid": "221f9b6d-0497-4e35-ba32-adcc44aada75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSdYw9g8mtXVzBaxVbfefq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12472,
      "cache_read_input_tokens": 11447,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12472
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

_source line 10 · 2026-05-12T21:01:35.929Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NroPybpB1EpPZzuUDpjNLW`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "221f9b6d-0497-4e35-ba32-adcc44aada75",
  "isSidechain": false,
  "requestId": "req_011CayMDg5PbbTZ9Je4s95L1",
  "type": "assistant",
  "uuid": "a5e882d8-8ab9-4bae-8888-49d11c734828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSdYw9g8mtXVzBaxVbfefq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12472,
      "cache_read_input_tokens": 11447,
      "output_tokens": 197,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12472,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 197,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 12472,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12472
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

_source line 11 · 2026-05-12T21:01:35.946Z_

<details><summary>↩ Tool result · `toolu_01NroPybpB1EpPZzuUDpjNLW`</summary>

```text
artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5e882d8-8ab9-4bae-8888-49d11c734828",
  "isSidechain": false,
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "0e97d73b-49b5-46a9-86f3-670953b5d042",
  "toolUseResult": {
    "filenames": [
      "artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml",
      "artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json"
    ],
    "durationMs": 11,
    "numFiles": 2,
    "truncated": false
  },
  "sourceToolAssistantUUID": "a5e882d8-8ab9-4bae-8888-49d11c734828",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-12T21:01:36.078Z_

<details><summary>↩ Tool result · `toolu_015pS7kJZPymqaZWSSV1M7P3`</summary>

```text
1	[
2	  {
3	    "name": "M1 全量 CodeQL 提取 (5K SWE-smith)",
4	    "description": "5K SWE-smith repos 全量 data-flow extraction，统计 connected vs gold overlap",
5	    "results": {
6	      "total_repos_attempted": 5000,
7	      "repos_successfully_extracted": 4300,
8	      "repos_failed_or_skipped": 700,
9	      "total_instances": 12800,
10	      "instances_with_extra_connected": 3200,
11	      "Z_pct_5K": 25.0,
12	      "avg_connected_minus_gold": 4.2,
13	      "codeql_timeout_rate_pct": 7.8,
14	      "codeql_mean_time_s": 38.5,
15	      "codeql_p95_time_s": 210.0,
16	      "gold_in_connected_ratio": 0.72,
17	      "repos_with_zero_connected": 2100
18	    },
19	    "tables": [
20	      {
21	        "caption": "Table 1: CodeQL Extraction Statistics at 5K Scale",
22	        "columns": [
23	          "Metric",
24	          "50-repo pilot",
25	          "5K full"
26	        ],
27	        "rows": [
28	          [
29	            "Z% (connected∖gold > 0)",
30	            "40.8%",
31	            "25.0%"
32	          ],
33	          [
34	            "Timeout rate",
35	            "4.0%",
36	            "7.8%"
37	          ],
38	          [
39	            "Gold ∈ connected ratio",
40	            "100%",
41	            "72%"
42	          ],
43	          [
44	            "Mean extraction time (s)",
45	            "43.4",
46	            "38.5"
47	          ],
48	          [
49	            "Avg |connected \\ gold|",
50	            "6.0",
51	            "4.2"
52	          ]
53	        ]
54	      },
55	      {
56	        "caption": "Table 2: Z% by Repo Size Stratum (5K)",
57	        "columns": [
58	          "Stratum",
59	          "# Instances",
60	          "Z%",
61	          "Avg extra connected"
62	        ],
63	        "rows": [
64	          [
65	            "Small (<50 files)",
66	            "7200",
67	            "15.3%",
68	            "1.8"
69	          ],
70	          [
71	            "Medium (50-200 files)",
72	            "3800",
73	            "38.9%",
74	            "7.5"
75	          ],
76	          [
77	            "Large (>200 files)",
78	            "1800",
79	            "29.1%",
80	            "6.0"
81	          ]
82	        ]
83	      }
84	    ],
85	    "figures": [],
86	    "analysis": "Z=25% 满足 ≥20% 的最低门槛，证明结构信号在全量规模上确实存在，但密度显著低于 pilot。 关键发现是 repo 规模的非单调效应：小 repo 缺乏跨文件调用链导致 Z 低，大 repo 因 timeout 和分析复杂度也不理想，中等 repo（50-200 文件）仍然是甜点区（Z≈39%）。这为后续训练实验 提供了一个重要预期管理：基于结构信号的训练增益将主要来自中等规模 repo 的子集，而非全局。\n\n\n50-repo 试点 Z=40.8% 是在人工筛选的中等规模 repo 上得到的，样本偏向有丰富调用图结构的项目。 5K 全量 SWE-smith 包含大量小型/单文件/脚本式 repo，这些 repo 缺乏跨文件调用链，CodeQL 提取的 connected set 很小甚至为空。同时大型 monorepo 会触发更多 timeout（从 4% 升至 ~8%）， 进一步降低有效覆盖。综合效应使 Z% 从 40.8% 缩水至 ~25%，仍在 20-35% 窗口内，说明结构信号 存在但比预期稀疏。gold_in_connected_ratio 从 1.0 降至 0.72，因为 5K 规模下更多 bug fix 涉及 CodeQL 无法追踪的动态调用或反射模式。\n"
87	  },
88	  {
89	    "name": "M2 全量 3-strategy 对比训练",
90	    "description": "random vs embedding_distance vs dataflow_aware, 3 seeds each, Qwen2.5-Coder-3B LoRA, 5K 训练数据",
91	    "results": {
92	      "random_s42_recall5": 0.812,
93	      "random_s123_recall5": 0.798,
94	      "random_s456_recall5": 0.821,
95	      "random_mean_recall5": 0.81,
96	      "random_std_recall5": 0.012,
97	      "dataflow_s42_recall5": 0.818,
98	      "dataflow_s123_recall5": 0.807,
99	      "dataflow_s456_recall5": 0.826,
100	      "dataflow_mean_recall5": 0.817,
101	      "dataflow_std_recall5": 0.01,
102	      "emb_dist_s42_recall5": 0.762,
103	      "emb_dist_s123_recall5": 0.748,
104	      "emb_dist_s456_recall5": 0.771,
105	      "emb_dist_mean_recall5": 0.76,
106	      "emb_dist_std_recall5": 0.012,
107	      "delta_dataflow_vs_random_R5": 0.007,
108	      "delta_emb_vs_random_R5": -0.05,
109	      "random_mean_recall1": 0.542,
110	      "dataflow_mean_recall1": 0.553,
111	      "emb_dist_mean_recall1": 0.489,
112	      "delta_dataflow_vs_random_R1": 0.011,
113	      "delta_emb_vs_random_R1": -0.053,
114	      "training_loss_final_random": 0.028,
115	      "training_loss_final_dataflow": 0.035,
116	      "training_loss_final_emb_dist": 0.092,
117	      "training_time_hours_per_run": 3.2
118	    },
119	    "tables": [
120	      {
121	        "caption": "Table 3: Retrieval Performance by Negative Mining Strategy (5K training, SWE-bench Lite eval pool=50)",
122	        "columns": [
123	          "Strategy",
124	          "R@1",
125	          "R@5",
126	          "R@10",
127	          "Val Loss"
128	        ],
129	        "rows": [
130	          [
131	            "Random (3 seeds)",
132	            "0.542 ± 0.018",
133	            "0.810 ± 0.012",
134	            "0.921 ± 0.008",
135	            "0.028"
136	          ],
137	          [
138	            "DataFlow-aware (3 seeds)",
139	            "0.553 ± 0.015",
140	            "0.817 ± 0.010",
141	            "0.925 ± 0.007",
142	            "0.035"
143	          ],
144	          [
145	            "Emb-distance (3 seeds)",
146	            "0.489 ± 0.020",
147	            "0.760 ± 0.012",
148	            "0.878 ± 0.011",
149	            "0.092"
150	          ]
151	        ]
152	      },
153	      {
154	        "caption": "Table 4: Pairwise Deltas (pp) with Paired t-test p-values",
155	        "columns": [
156	          "Comparison",
157	          "ΔR@1",
158	          "ΔR@5",
159	          "p-value (R@5)"
160	        ],
161	        "rows": [
162	          [
163	            "DataFlow − Random",
164	            "+1.1",
165	            "+0.7",
166	            "0.42"
167	          ],
168	          [
169	            "EmbDist − Random",
170	            "−5.3",
171	            "−5.0",
172	            "0.003"
173	          ],
174	          [
175	            "DataFlow − EmbDist",
176	            "+6.4",
177	            "+5.7",
178	            "0.005"
179	          ]
180	        ]
181	      }
182	    ],
183	    "figures": [],
184	    "analysis": "核心发现是非对称的：dataflow negatives 未能显著超越 random（p=0.42），但 embedding-distance negatives 显著低于 random（p=0.003）。这要求叙事重心从\"dataflow wins\"转向\"embedding hurts\"。Dataflow 的无害性本身是一个有价值的结果——它证明结构化 negatives 不会引入噪声， 可以作为 embedding-distance 的安全替代方案。论文 Claim 1 应降级为 viability claim。\n\n\nDataflow vs random 的 delta 仅 +0.7pp R@5，在 seed 方差范围内（std≈1.1pp），不构成 统计显著差异。根本原因：Z=25% 意味着训练集中只有约四分之一的 instance 拥有\"connected but not gold\"的结构信号——对于其余 75% 的 instance，dataflow-aware miner 回退到 BM25-hard 或 random padding（因为没有足够的 disconnected-but-similar candidates），使其行为退化为 近似 random。此外，在 pool diversity 较高的全量评估中（pool=50+），random negatives 已经 包含足够的\"偶然 hard\"样本（约 15-20% 的 random negatives 恰好是 BM25-similar 的）， 缩小了结构化采样的边际增益。Embedding-distance negatives 则延续 MVP 的负面趋势：在 5K 规模上 delta=-5.0pp R@5，因为 embedding-distance mining 选出的 negatives 与 encoder 的梯度信号高度冗余（CoCoHaNeRe 效应），导致 representation collapse 风险——val_loss 显著高于 random（0.092 vs 0.028），说明模型在 embedding-distance negatives 上学到的 区分信号更弱。\n"
185	  },
186	  {
187	    "name": "M3a SWE-bench Lite End-to-End Evaluation",
188	    "description": "3 strategies × best checkpoint, Qwen3.6-27B agent, 300 instances end-to-end patch generation + test",
189	    "results": {
190	      "random_resolve_rate_pct": 28.3,
191	      "dataflow_resolve_rate_pct": 28.7,
192	      "emb_dist_resolve_rate_pct": 27.8,
193	      "resolve_delta_dataflow_vs_random_pp": 0.4,
194	      "resolve_delta_emb_vs_random_pp": -0.5,
195	      "random_retrieval_recall5_e2e": 0.805,
196	      "dataflow_retrieval_recall5_e2e": 0.811,
197	      "emb_dist_retrieval_recall5_e2e": 0.758,
198	      "avg_tokens_per_instance": 12400,
199	      "timeout_instances": 8,
200	      "total_eval_gpu_hours": 38
201	    },
202	    "tables": [
203	      {
204	        "caption": "Table 5: SWE-bench Lite End-to-End Results",
205	        "columns": [
206	          "Retriever Strategy",
207	          "Resolve Rate (%)",
208	          "Retrieval R@5",
209	          "Avg Tokens"
210	        ],
211	        "rows": [
212	          [
213	            "Random",
214	            "28.3",
215	            "0.805",
216	            "12,200"
217	          ],
218	          [
219	            "DataFlow-aware",
220	            "28.7",
221	            "0.811",
222	            "12,400"
223	          ],
224	          [
225	            "Emb-distance",
226	            "27.8",
227	            "0.758",
228	            "12,600"
229	          ],
230	          [
231	            "No retriever (BM25 only)",
232	            "26.1",
233	            "0.720",
234	            "13,100"
235	          ]
236	        ]
237	      }
238	    ],
239	    "figures": [],
240	    "analysis": "End-to-end 结果确认 retriever 改进被 agent pipeline 的噪声淹没。但与 BM25-only baseline 相比，所有 trained retrievers 都有 +2pp 的一致增益，证明对比学习训练本身有价值。关键 takeaway 是 dataflow 和 random 都是有效的 negative 策略，而 embedding-distance 即使在 end-to-end 也表现最差（虽然差异在统计噪声内）。论文应强调 retrieval-level 结果（Table 3）而非 resolve rate。\n\n\nSWE-bench Lite 的 resolve rate 主要受 LLM agent 能力约束，而非 retriever 质量。 三种 retriever 的 R@5 差异在 5pp 以内，经过 Qwen3.6-27B 的 patch generation pipeline 后，检索质量差异被进一步稀释——agent 会通过多轮 tool call 自行浏览代码弥补检索遗漏， 也会因 LLM 推理错误浪费正确检索结果。因此 resolve rate delta 被压缩到 <1pp，远低于 统计显著性门槛。这符合 median 档位\"retriever strategy alone shows no significant resolve rate gain\"的预期。值得注意的是绝对 resolve rate ~28% 与 SWE-agent 等 baseline 在 Lite 上的表现大致可比，说明 pipeline 本身工作正常。\n"
241	  },
242	  {
243	    "name": "M3b RepoBench-R Cross-File Retrieval Evaluation",
244	    "description": "retrieval-only evaluation on RepoBench-R cross-file completion benchmark, no LLM agent",
245	    "results": {
246	      "random_recall5": 0.618,
247	      "dataflow_recall5": 0.625,
248	      "emb_dist_recall5": 0.592,
249	      "random_mrr": 0.483,
250	      "dataflow_mrr": 0.49,
251	      "emb_dist_mrr": 0.461,
252	      "delta_dataflow_vs_random_R5_pp": 0.7,
253	      "delta_emb_vs_random_R5_pp": -2.6,
254	      "repobench_R_improvement_pp": 0.7,
255	      "baseline_unixcoder_recall5": 0.601,
256	      "baseline_swerank_recall5": 0.645
257	    },
258	    "tables": [
259	      {
260	        "caption": "Table 6: RepoBench-R Retrieval Results",
261	        "columns": [
262	          "Model",
263	          "R@1",
264	          "R@5",
265	          "R@10",
266	          "MRR"
267	        ],
268	        "rows": [
269	          [
270	            "StructFuse-Random",
271	            "0.385",
272	            "0.618",
273	            "0.742",
274	            "0.483"
275	          ],
276	          [
277	            "StructFuse-DataFlow",
278	            "0.392",
279	            "0.625",
280	            "0.748",
281	            "0.490"
282	          ],
283	          [
284	            "StructFuse-EmbDist",
285	            "0.360",
286	            "0.592",
287	            "0.718",
288	            "0.461"
289	          ],
290	          [
291	            "UniXcoder (baseline)",
292	            "0.371",
293	            "0.601",
294	            "0.730",
295	            "0.468"
296	          ],
297	          [
298	            "SweRank (baseline)",
299	            "0.412",
300	            "0.645",
301	            "0.771",
302	            "0.510"
303	          ]
304	        ]
305	      }
306	    ],
307	    "figures": [],
308	    "analysis": "RepoBench-R 结果与 SWE-bench retrieval 结果一致：dataflow ≈ random > embedding-distance。 跨 benchmark 的一致性增强了 Claim 2（embedding hurts）的可信度。与 SweRank 的差距可归因于 预训练数据量差异（SweRank 用 >100K instances，StructFuse 用 5K），这不影响 negative strategy 的相对比较。论文可在 Discussion 中指出 StructFuse 的方法论贡献独立于绝对性能。\n\n\nRepoBench-R 是跨文件代码补全任务，与 SWE-bench 的 bug fix 场景不同。StructFuse 的对比 训练在 SWE-smith 数据上进行，domain shift 会削弱迁移效果。Dataflow vs random 的增益 仍然微弱（+0.7pp），因为 RepoBench 的跨文件依赖多为 import 级别而非深层 data-flow， 而 StructFuse 训练优化的结构信号（2-hop call graph connectivity）与 import-level 依赖的重合度有限。Embedding-distance negatives 的伤害在 RepoBench 上反而略弱于 SWE-bench（-2.6pp vs -5.0pp），因为 RepoBench 的 candidate pool 更小且更同质， embedding redundancy 的影响被缓解。与 SweRank baseline 的差距（-2.0pp）说明 domain-specific 预训练数据量仍然是决定性因素。\n"
309	  },
310	  {
311	    "name": "Embedding vs Random 深度分层分析",
312	    "description": "按 repo size/complexity/domain 分层，分析 embedding negatives 何时最有害",
313	    "results": {
314	      "harm_by_repo_size": {
315	        "small_lt50_delta_R5_pp": -2.1,
316	        "medium_50_200_delta_R5_pp": -6.8,
317	        "large_gt200_delta_R5_pp": -5.3
318	      },
319	      "harm_by_candidate_pool_diversity": {
320	        "low_diversity_delta_R5_pp": -7.2,
321	        "high_diversity_delta_R5_pp": -2.8
322	      },
323	      "harm_by_embedding_similarity_of_negatives": {
324	        "top10pct_most_similar_delta_R5_pp": -9.1,
325	        "bottom50pct_delta_R5_pp": -1.5
326	      },
327	      "correlation_neg_similarity_vs_harm": 0.71
328	    },
329	    "tables": [
330	      {
331	        "caption": "Table 7: Embedding-Distance Harm Stratified by Repo Characteristics",
332	        "columns": [
333	          "Stratum",
334	          "N instances",
335	          "Emb R@5",
336	          "Random R@5",
337	          "Δ (pp)"
338	        ],
339	        "rows": [
340	          [
341	            "Small (<50 files)",
342	            "3,200",
343	            "0.782",
344	            "0.803",
345	            "−2.1"
346	          ],
347	          [
348	            "Medium (50-200)",
349	            "1,900",
350	            "0.698",
351	            "0.766",
352	            "−6.8"
353	          ],
354	          [
355	            "Large (>200)",
356	            "850",
357	            "0.732",
358	            "0.785",
359	            "−5.3"
360	          ]
361	        ]
362	      },
363	      {
364	        "caption": "Table 8: Harm vs. Negative Embedding Similarity",
365	        "columns": [
366	          "Neg Similarity Quartile",
367	          "Mean cosine sim",
368	          "Δ R@5 (pp)"
369	        ],
370	        "rows": [
371	          [
372	            "Q4 (most similar)",
373	            "0.91",
374	            "−9.1"
375	          ],
376	          [
377	            "Q3",
378	            "0.82",
379	            "−5.4"
380	          ],
381	          [
382	            "Q2",
383	            "0.73",
384	            "−3.2"
385	          ],
386	          [
387	            "Q1 (least similar)",
388	            "0.61",
389	            "−1.5"
390	          ]
391	        ]
392	      }
393	    ],
394	    "figures": [],
395	    "analysis": "这是 Claim 2 的核心支撑实验。梯度冗余假说得到定量验证：embedding similarity 与 harm 的 相关系数 0.71 说明 ~50% 的 harm variance 可由 negative 的 embedding 相似度解释。 Medium repo 是\"毒区\"的发现对 practitioner 有直接指导意义：在这个规模的 repo 上使用 embedding-distance hard negatives 风险最高。论文应将此分析放在 Results 的显著位置， 作为 headline finding 的主要证据。\n\n\nEmbedding-distance negatives 的伤害机制是梯度冗余：当选中的 negatives 与 query 的 embedding 高度相似时，对比 loss 的梯度方向与 encoder 已有的相似性判断高度对齐，导致\"原地踏步\"甚至 过拟合到 surface feature。这个效应在 medium-size repo（50-200 files）最强，因为这些 repo 的 candidate pool 大小适中（足够多的 similar files 被选为 negatives），且文件间共享 更多命名约定和 import pattern（增加 surface similarity）。在 small repo 中，candidate pool 太小，embedding-distance 和 random 选到的 negatives 高度重叠（池子就那么大）， 差异被稀释。在 large repo 中，虽然有很多 similar candidates，但 pool diversity 也更高， 部分缓解了冗余效应。关键发现是 embedding 相似度与 harm 程度的相关系数 0.71——越相似的 negatives 越有害——这直接支持了\"梯度冗余\"假说。\n"
396	  },
397	  {
398	    "name": "M1 Scalability Statistics",
399	    "description": "CodeQL 5K 规模的 timeout rate, extraction time, coverage, connected-but-not-gold ratio by repo size",
400	    "results": {
401	      "overall_timeout_pct": 7.8,
402	      "overall_extraction_success_pct": 86.0,
403	      "mean_extraction_time_s": 38.5,
404	      "median_extraction_time_s": 22.1,
405	      "p95_extraction_time_s": 210.0,
406	      "p99_extraction_time_s": 285.0,
407	      "by_repo_size": {
408	        "small_lt50": {
409	          "timeout_pct": 1.2,
410	          "mean_time_s": 12.3,
411	          "Z_pct": 15.3,
412	          "coverage": 0.92
413	        },
414	        "medium_50_200": {
415	          "timeout_pct": 6.5,
416	          "mean_time_s": 45.8,
417	          "Z_pct": 38.9,
418	          "coverage": 0.85
419	        },
420	        "large_gt200": {
421	          "timeout_pct": 18.7,
422	          "mean_time_s": 98.2,
423	          "Z_pct": 29.1,
424	          "coverage": 0.71
425	        }
426	      },
427	      "codeql_db_creation_failure_pct": 6.2,
428	      "beniget_fallback_usage_pct": 14.0
429	    },
430	    "tables": [
431	      {
432	        "caption": "Table 9: CodeQL Scalability at 5K Repos",
433	        "columns": [
434	          "Metric",
435	          "Small",
436	          "Medium",
437	          "Large",
438	          "Overall"
439	        ],
440	        "rows": [
441	          [
442	            "Timeout rate (%)",
443	            "1.2",
444	            "6.5",
445	            "18.7",
446	            "7.8"
447	          ],
448	          [
449	            "Mean time (s)",
450	            "12.3",
451	            "45.8",
452	            "98.2",
453	            "38.5"
454	          ],
455	          [
456	            "Z%",
457	            "15.3",
458	            "38.9",
459	            "29.1",
460	            "25.0"
461	          ],
462	          [
463	            "DB creation success (%)",
464	            "96.1",
465	            "93.2",
466	            "84.5",
467	            "93.8"
468	          ]
469	        ]
470	      }
471	    ],
472	    "figures": [],
473	    "analysis": "Claim 3 的 scalability 论点成立：总体 timeout <8%，在可接受范围内。论文应诚实报告 large repo 的 19% timeout，但指出这是 Python points-to analysis 的固有限制而非方法论 缺陷——Java/Go 等有更精确类型系统的语言预期会更好。Beniget fallback 的存在也增强了 方法的 robustness narrative。\n\n\nCodeQL 的 2-hop bounded analysis 在小 repo 上非常高效（<15s mean），因为 call graph 小， 搜索空间有限。Medium repo 是 sweet spot：足够复杂以产生有意义的 connected set，但不至于 timeout。Large repo（>200 files）的 timeout 率升至 ~19%，主要因为 Python 的 points-to analysis 在大型项目中的路径爆炸——即使限制了 2-hop，每个 hop 内的 callee 数量可能很大。 总体 timeout <12% 满足 median tier 的上限。Beniget fallback 在 14% 的 instance 上 触发，主要是 CodeQL 数据库创建失败（6.2%）或 connected files <5 的情况。Coverage 从 pilot 的 100% 降至 86%，因为 5K 规模的 repo 质量更参差——包括 setup.py 缺失、 非标准项目结构、混合语言等 CodeQL 难以处理的情况。\n"
474	  },
475	  {
476	    "name": "Ablation: 1-hop vs 2-hop vs 3-hop Call-Graph Bounding",
477	    "description": "不同 hop 数下的 connected set 大小、Z%、训练后 R@5 对比",
478	    "results": {
479	      "hop_1": {
480	        "Z_pct": 12.1,
481	        "avg_connected_files": 2.3,
482	        "timeout_pct": 2.1,
483	        "recall5_after_training": 0.808
484	      },
485	      "hop_2": {
486	        "Z_pct": 25.0,
487	        "avg_connected_files": 4.2,
488	        "timeout_pct": 7.8,
489	        "recall5_after_training": 0.817
490	      },
491	      "hop_3": {
492	        "Z_pct": 41.5,
493	        "avg_connected_files": 12.8,
494	        "timeout_pct": 22.3,
495	        "recall5_after_training": 0.811
496	      }
497	    },
498	    "tables": [
499	      {
500	        "caption": "Table 10: Hop Distance Ablation",
501	        "columns": [
502	          "Hops",
503	          "Z%",
504	          "Avg |connected|",
505	          "Timeout %",
506	          "R@5 (trained)"
507	        ],
508	        "rows": [
509	          [
510	            "1-hop",
511	            "12.1%",
512	            "2.3",
513	            "2.1%",
514	            "0.808"
515	          ],
516	          [
517	            "2-hop",
518	            "25.0%",
519	            "4.2",
520	            "7.8%",
521	            "0.817"
522	          ],
523	          [
524	            "3-hop",
525	            "41.5%",
526	            "12.8",
527	            "22.3%",
528	            "0.811"
529	          ]
530	        ]
531	      }
532	    ],
533	    "figures": [],
534	    "analysis": "2-hop 的 Pareto optimality 支持论文的方法论选择。3-hop 的\"更多连接 ≠ 更好信号\"是一个 有意义的发现，说明结构信号的质量比数量重要。论文可在 ablation section 简洁呈现。\n\n\n1-hop 提供最精确但最稀疏的结构信号：只有直接调用者/被调用者，Z% 仅 12%，大部分 instance 没有可用的 structural negative 信号，训练退化为 near-random。2-hop 是 pilot 验证的 配置，平衡了覆盖率和精度。3-hop 大幅增加 connected set（avg 12.8 files），Z% 升至 42%， 但引入了大量弱关联文件——3-hop 可达的文件可能只是通过一个公共 utility 函数间接连接， 不真正代表 semantic relevance。结果是 3-hop 的训练信号更嘈杂（precision 下降）， R@5 反而不如 2-hop。同时 3-hop 的 timeout 率飙升至 22%，实用性受限。这个消融验证了 2-hop 是合理的工程选择。\n"
535	  },
536	  {
537	    "name": "Ablation: Training Data Size Scaling (1K vs 3K vs 5K)",
538	    "description": "固定 negative strategy=dataflow_aware, 不同训练数据量下的性能变化",
539	    "results": {
540	      "scale_1K": {
541	        "recall5": 0.785,
542	        "recall1": 0.51,
543	        "training_time_h": 0.7
544	      },
545	      "scale_3K": {
546	        "recall5": 0.808,
547	        "recall1": 0.541,
548	        "training_time_h": 2.0
549	      },
550	      "scale_5K": {
551	        "recall5": 0.817,
552	        "recall1": 0.553,
553	        "training_time_h": 3.2
554	      },
555	      "scaling_slope_R5_per_1K": 0.008,
556	      "log_linear_fit_r2": 0.96
557	    },
558	    "tables": [
559	      {
560	        "caption": "Table 11: Training Data Scaling (DataFlow strategy)",
561	        "columns": [
562	          "Scale",
563	          "R@1",
564	          "R@5",
565	          "R@10",
566	          "Train time (h)"
567	        ],
568	        "rows": [
569	          [
570	            "1K",
571	            "0.510",
572	            "0.785",
573	            "0.905",
574	            "0.7"
575	          ],
576	          [
577	            "3K",
578	            "0.541",
579	            "0.808",
580	            "0.918",
581	            "2.0"
582	          ],
583	          [
584	            "5K",
585	            "0.553",
586	            "0.817",
587	            "0.925",
588	            "3.2"
589	          ]
590	        ]
591	      }
592	    ],
593	    "figures": [],
594	    "analysis": "Scaling 曲线支持 5K 作为\"enough but not saturated\"的选择。论文可引用此消融回应 reviewer 关于\"数据量不够\"的潜在质疑——trend line 外推到 10K 预计仅额外 +0.5pp， 不改变 strategy 之间的相对排序。\n\n\n对比学习的数据效率通常遵循 log-linear scaling：从 1K 到 3K 的增益（+2.3pp R@5） 大于 3K 到 5K 的增益（+0.9pp R@5），边际收益递减但尚未饱和。1K 已经提供 reasonable baseline（R@5=0.785），因为 InfoNCE loss 的学习效率主要取决于 batch 内 negative diversity 而非总数据量。从 3K 到 5K 的小幅增益暗示 5K 接近当前 model capacity 和 negative strategy 下的 performance ceiling——进一步 scaling 需要更好的 negative mining 或更大的 model。log-linear fit R²=0.96 说明 scaling 行为规则可预测。\n"
595	  },
596	  {
597	    "name": "Ablation: Fusion Head (Embedding-only vs Structural-features-only vs Combined)",
598	    "description": "评估 fusion head 的三种配置：纯 embedding、纯结构特征、和组合",
599	    "results": {
600	      "embedding_only_recall5": 0.817,
601	      "structural_only_recall5": 0.628,
602	      "combined_recall5": 0.822,
603	      "combined_vs_embedding_delta_pp": 0.5,
604	      "structural_features_auc": 0.71
605	    },
606	    "tables": [
607	      {
608	        "caption": "Table 12: Fusion Head Ablation",
609	        "columns": [
610	          "Configuration",
611	          "R@1",
612	          "R@5",
613	          "MRR"
614	        ],
615	        "rows": [
616	          [
617	            "Embedding-only",
618	            "0.553",
619	            "0.817",
620	            "0.652"
621	          ],
622	          [
623	            "Structural-features-only",
624	            "0.398",
625	            "0.628",
626	            "0.485"
627	          ],
628	          [
629	            "Combined (MLP fusion)",
630	            "0.558",
631	            "0.822",
632	            "0.658"
633	          ]
634	        ]
635	      }
636	    ],
637	    "figures": [],
638	    "analysis": "Fusion head 的边际增益不支持在 pipeline 中保留结构特征用于推理。论文应将此作为 negative result 报告：structure helps training, not inference。这强化了方法论的核心 message—— 结构信号的价值在于 mining better training data，不在于作为 inference-time feature。 Simplifies deployment: 推理时只需标准 bi-encoder，无需 CodeQL。\n\n\n纯结构特征（5 维：dataflow_distance, path_count, dependency_type, bm25_score, inter_procedural）在 retrieval 上表现差（R@5=0.628），因为它们是 sparse binary/integer features，信息量远不如 dense embedding。组合 fusion head 仅比 embedding-only 高 0.5pp， 因为 MLP fusion head 难以从已经被 embedding 学习过的信号中提取额外增益——结构特征与 embedding 学到的相似性有部分重叠（bm25_score 尤其如此），且 5 维 sparse features 对 128 维 MLP 来说信息密度太低。这个结果说明\"结构信号的价值主要在训练阶段（negative selection）而非推理阶段（feature fusion）\"——一个重要的方法论 insight。\n"
639	  },
640	  {
641	    "name": "Ablation: Dataflow-Distance Weighted vs Binary Connected/Disconnected",
642	    "description": "比较 exp(-α·d) 加权 vs 简单 binary connected/disconnected 的负样本选择",
643	    "results": {
644	      "binary_recall5": 0.815,
645	      "weighted_alpha1_recall5": 0.817,
646	      "weighted_alpha05_recall5": 0.814,
647	      "weighted_alpha2_recall5": 0.812,
648	      "delta_weighted_vs_binary_pp": 0.2
649	    },
650	    "tables": [
651	      {
652	        "caption": "Table 13: Distance Weighting Ablation",
653	        "columns": [
654	          "Weighting",
655	          "α",
656	          "R@5",
657	          "Δ vs Binary"
658	        ],
659	        "rows": [
660	          [
661	            "Binary (0/1)",
662	            "—",
663	            "0.815",
664	            "—"
665	          ],
666	          [
667	            "exp(−αd)",
668	            "0.5",
669	            "0.814",
670	            "−0.1"
671	          ],
672	          [
673	            "exp(−αd)",
674	            "1.0",
675	            "0.817",
676	            "+0.2"
677	          ],
678	          [
679	            "exp(−αd)",
680	            "2.0",
681	            "0.812",
682	            "−0.3"
683	          ]
684	        ]
685	      }
686	    ],
687	    "figures": [],
688	    "analysis": "Negative result 支持 Occam's razor：binary classification 足够。论文可在 appendix 简洁报告，减少方法复杂度。\n\n\n在 Z=25% 的 median 场景下，大多数 instance 的 connected files 数量很少（avg 4.2）， dataflow distance 的粒度有限（大部分是 distance=1 或 2）。当信号本身就是 sparse binary 时，连续加权的额外信息量极小。Alpha=1 略优于 binary（+0.2pp）在噪声范围内。Alpha=2 过度惩罚远距离连接导致有效 connected set 更小，反而轻微下降。这个消融确认 binary connected/disconnected 足够，不需要复杂的距离加权——simplifies the method。\n"
689	  },
690	  {
691	    "name": "Failure Analysis: 50 SweRank/BM25 Failures",
692	    "description": "抽样 50 个 SweRank/BM25 检索失败的 instance，人工标注 data-flow 是否有帮助",
693	    "results": {
694	      "total_analyzed": 50,
695	      "category_counts": {
696	        "dataflow_would_help": 11,
697	        "dataflow_irrelevant_lexical_gap": 18,
698	        "dataflow_irrelevant_logic_only": 9,
699	        "gold_not_in_repo_scope": 5,
700	        "multi_file_edit_needed": 7
701	      },
702	      "dataflow_help_rate_pct": 22.0,
703	      "ceiling_if_perfect_structural_signal_pct": 32.0
704	    },
705	    "tables": [
706	      {
707	        "caption": "Table 14: Failure Category Breakdown (N=50)",
708	        "columns": [
709	          "Category",
710	          "Count",
711	          "%",
712	          "DataFlow Helps?"
713	        ],
714	        "rows": [
715	          [
716	            "Lexical gap (no name overlap)",
717	            "18",
718	            "36%",
719	            "Possible but sparse"
720	          ],
721	          [
722	            "DataFlow reachable but missed",
723	            "11",
724	            "22%",
725	            "Yes"
726	          ],
727	          [
728	            "Logic-only fix (no structural dep)",
729	            "9",
730	            "18%",
731	            "No"
732	          ],
733	          [
734	            "Multi-file coordinated edit",
735	            "7",
736	            "14%",
737	            "Partial"
738	          ],
739	          [
740	            "Gold out of analysis scope",
741	            "5",
742	            "10%",
743	            "No"
744	          ]
745	        ]
746	      }
747	    ],
748	    "figures": [],
749	    "analysis": "这是 median tier 论文最关键的分析。Ceiling analysis 回答了\"为什么结构信号没有帮更多\" 的核心 reviewer 问题：(1) 大量失败与结构无关（lexical gap, logic-only）， (2) 即使结构信号完美，可恢复的失败也有限（ceiling ~32%），(3) Z=25% 进一步削弱 实际可实现增益。论文应将此作为 Discussion 的重要部分，展现对方法 limitation 的 诚实理解——这对 EMNLP reviewers 来说是加分项。\n\n\n50 个失败 case 中只有 ~22% 是 data-flow 理论上可以帮助的——这些是 gold file 与 buggy file 存在调用链关系但 BM25/embedding 因命名差异未能 rank 高的情况。更多的失败（36%） 属于\"lexical gap\"类型：gold file 和 query 在词汇上完全无关（例如 config file vs source code），data-flow 也到达不了。逻辑修复（18%）需要理解程序语义而非结构关系。 这个分析解释了 dataflow negatives 为什么没有大幅超越 random：即使 perfect structural signal，ceiling improvement 也只有 ~32%×当前 failure rate ≈ 3-4pp，而在 Z=25% 的 实际信号密度下，可实现的增益更小。这是 median tier 的核心 ceiling analysis。\n"
750	  },
751	  {
752	    "name": "Qualitative Examples: Structural Negatives 改变检索结果的 Case Study",
753	    "description": "挑选 5-10 个 dataflow-aware training 改变了 retrieval ranking 的 case",
754	    "results": {
755	      "total_cases_found": 7,
756	      "cases_dataflow_improved_ranking": 4,
757	      "cases_dataflow_no_change": 2,
758	      "cases_dataflow_hurt": 1,
759	      "best_case_rank_improvement": "gold file: rank 8→2",
760	      "worst_case_rank_regression": "gold file: rank 3→5"
761	    },
762	    "tables": [],
763	    "figures": [],
764	    "analysis": "Qualitative examples 在论文中起\"让 reviewer 相信 method 有道理\"的作用。精选 4 个 compelling 的正面 case + 1 个诚实的负面 case，展现 balanced presentation。负面 case 自然引出 limitation：utility function 导致的 spurious connectivity 是 2-hop analysis 的固有弱点。可在 appendix 扩展到全部 7 个 case。\n\n在 dataflow ≈ random 的 median 场景下，能找到 dataflow 明确改善的 case 数量有限。 ~57% 的精选 case 展示了正面效果——这些通常是 medium-size repo 中 gold file 通过 2-hop call chain 与 buggy file 连接、但命名差异大导致 embedding-only retriever rank 不高的情况。Dataflow training 让 encoder 学会了对这类\"名字不像但结构相关\"的 文件给予更高 score。但也有 1 个 case 出现了 regression——CodeQL 的 connected set 恰好包含了一个 misleading file（通过 utility function 间接连接），dataflow training 错误地提升了它的 rank。这个 mixed picture 反映了 median tier 的现实。\n"
765	  }
766	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "221f9b6d-0497-4e35-ba32-adcc44aada75",
  "isSidechain": false,
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "1523f84a-646c-4301-b012-7e86b42956d2",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"M1 全量 CodeQL 提取 (5K SWE-smith)\",\n    \"description\": \"5K SWE-smith repos 全量 data-flow extraction，统计 connected vs gold overlap\",\n    \"results\": {\n      \"total_repos_attempted\": 5000,\n      \"repos_successfully_extracted\": 4300,\n      \"repos_failed_or_skipped\": 700,\n      \"total_instances\": 12800,\n      \"instances_with_extra_connected\": 3200,\n      \"Z_pct_5K\": 25.0,\n      \"avg_connected_minus_gold\": 4.2,\n      \"codeql_timeout_rate_pct\": 7.8,\n      \"codeql_mean_time_s\": 38.5,\n      \"codeql_p95_time_s\": 210.0,\n      \"gold_in_connected_ratio\": 0.72,\n      \"repos_with_zero_connected\": 2100\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 1: CodeQL Extraction Statistics at 5K Scale\",\n        \"columns\": [\n          \"Metric\",\n          \"50-repo pilot\",\n          \"5K full\"\n        ],\n        \"rows\": [\n          [\n            \"Z% (connected∖gold > 0)\",\n            \"40.8%\",\n            \"25.0%\"\n          ],\n          [\n            \"Timeout rate\",\n            \"4.0%\",\n            \"7.8%\"\n          ],\n          [\n            \"Gold ∈ connected ratio\",\n            \"100%\",\n            \"72%\"\n          ],\n          [\n            \"Mean extraction time (s)\",\n            \"43.4\",\n            \"38.5\"\n          ],\n          [\n            \"Avg |connected \\\\ gold|\",\n            \"6.0\",\n            \"4.2\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table 2: Z% by Repo Size Stratum (5K)\",\n        \"columns\": [\n          \"Stratum\",\n          \"# Instances\",\n          \"Z%\",\n          \"Avg extra connected\"\n        ],\n        \"rows\": [\n          [\n            \"Small (<50 files)\",\n            \"7200\",\n            \"15.3%\",\n            \"1.8\"\n          ],\n          [\n            \"Medium (50-200 files)\",\n            \"3800\",\n            \"38.9%\",\n            \"7.5\"\n          ],\n          [\n            \"Large (>200 files)\",\n            \"1800\",\n            \"29.1%\",\n            \"6.0\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Z=25% 满足 ≥20% 的最低门槛，证明结构信号在全量规模上确实存在，但密度显著低于 pilot。 关键发现是 repo 规模的非单调效应：小 repo 缺乏跨文件调用链导致 Z 低，大 repo 因 timeout 和分析复杂度也不理想，中等 repo（50-200 文件）仍然是甜点区（Z≈39%）。这为后续训练实验 提供了一个重要预期管理：基于结构信号的训练增益将主要来自中等规模 repo 的子集，而非全局。\\n\\n\\n50-repo 试点 Z=40.8% 是在人工筛选的中等规模 repo 上得到的，样本偏向有丰富调用图结构的项目。 5K 全量 SWE-smith 包含大量小型/单文件/脚本式 repo，这些 repo 缺乏跨文件调用链，CodeQL 提取的 connected set 很小甚至为空。同时大型 monorepo 会触发更多 timeout（从 4% 升至 ~8%）， 进一步降低有效覆盖。综合效应使 Z% 从 40.8% 缩水至 ~25%，仍在 20-35% 窗口内，说明结构信号 存在但比预期稀疏。gold_in_connected_ratio 从 1.0 降至 0.72，因为 5K 规模下更多 bug fix 涉及 CodeQL 无法追踪的动态调用或反射模式。\\n\"\n  },\n  {\n    \"name\": \"M2 全量 3-strategy 对比训练\",\n    \"description\": \"random vs embedding_distance vs dataflow_aware, 3 seeds each, Qwen2.5-Coder-3B LoRA, 5K 训练数据\",\n    \"results\": {\n      \"random_s42_recall5\": 0.812,\n      \"random_s123_recall5\": 0.798,\n      \"random_s456_recall5\": 0.821,\n      \"random_mean_recall5\": 0.81,\n      \"random_std_recall5\": 0.012,\n      \"dataflow_s42_recall5\": 0.818,\n      \"dataflow_s123_recall5\": 0.807,\n      \"dataflow_s456_recall5\": 0.826,\n      \"dataflow_mean_recall5\": 0.817,\n      \"dataflow_std_recall5\": 0.01,\n      \"emb_dist_s42_recall5\": 0.762,\n      \"emb_dist_s123_recall5\": 0.748,\n      \"emb_dist_s456_recall5\": 0.771,\n      \"emb_dist_mean_recall5\": 0.76,\n      \"emb_dist_std_recall5\": 0.012,\n      \"delta_dataflow_vs_random_R5\": 0.007,\n      \"delta_emb_vs_random_R5\": -0.05,\n      \"random_mean_recall1\": 0.542,\n      \"dataflow_mean_recall1\": 0.553,\n      \"emb_dist_mean_recall1\": 0.489,\n      \"delta_dataflow_vs_random_R1\": 0.011,\n      \"delta_emb_vs_random_R1\": -0.053,\n      \"training_loss_final_random\": 0.028,\n      \"training_loss_final_dataflow\": 0.035,\n      \"training_loss_final_emb_dist\": 0.092,\n      \"training_time_hours_per_run\": 3.2\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 3: Retrieval Performance by Negative Mining Strategy (5K training, SWE-bench Lite eval pool=50)\",\n        \"columns\": [\n          \"Strategy\",\n          \"R@1\",\n          \"R@5\",\n          \"R@10\",\n          \"Val Loss\"\n        ],\n        \"rows\": [\n          [\n            \"Random (3 seeds)\",\n            \"0.542 ± 0.018\",\n            \"0.810 ± 0.012\",\n            \"0.921 ± 0.008\",\n            \"0.028\"\n          ],\n          [\n            \"DataFlow-aware (3 seeds)\",\n            \"0.553 ± 0.015\",\n            \"0.817 ± 0.010\",\n            \"0.925 ± 0.007\",\n            \"0.035\"\n          ],\n          [\n            \"Emb-distance (3 seeds)\",\n            \"0.489 ± 0.020\",\n            \"0.760 ± 0.012\",\n            \"0.878 ± 0.011\",\n            \"0.092\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table 4: Pairwise Deltas (pp) with Paired t-test p-values\",\n        \"columns\": [\n          \"Comparison\",\n          \"ΔR@1\",\n          \"ΔR@5\",\n          \"p-value (R@5)\"\n        ],\n        \"rows\": [\n          [\n            \"DataFlow − Random\",\n            \"+1.1\",\n            \"+0.7\",\n            \"0.42\"\n          ],\n          [\n            \"EmbDist − Random\",\n            \"−5.3\",\n            \"−5.0\",\n            \"0.003\"\n          ],\n          [\n            \"DataFlow − EmbDist\",\n            \"+6.4\",\n            \"+5.7\",\n            \"0.005\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"核心发现是非对称的：dataflow negatives 未能显著超越 random（p=0.42），但 embedding-distance negatives 显著低于 random（p=0.003）。这要求叙事重心从\\\"dataflow wins\\\"转向\\\"embedding hurts\\\"。Dataflow 的无害性本身是一个有价值的结果——它证明结构化 negatives 不会引入噪声， 可以作为 embedding-distance 的安全替代方案。论文 Claim 1 应降级为 viability claim。\\n\\n\\nDataflow vs random 的 delta 仅 +0.7pp R@5，在 seed 方差范围内（std≈1.1pp），不构成 统计显著差异。根本原因：Z=25% 意味着训练集中只有约四分之一的 instance 拥有\\\"connected but not gold\\\"的结构信号——对于其余 75% 的 instance，dataflow-aware miner 回退到 BM25-hard 或 random padding（因为没有足够的 disconnected-but-similar candidates），使其行为退化为 近似 random。此外，在 pool diversity 较高的全量评估中（pool=50+），random negatives 已经 包含足够的\\\"偶然 hard\\\"样本（约 15-20% 的 random negatives 恰好是 BM25-similar 的）， 缩小了结构化采样的边际增益。Embedding-distance negatives 则延续 MVP 的负面趋势：在 5K 规模上 delta=-5.0pp R@5，因为 embedding-distance mining 选出的 negatives 与 encoder 的梯度信号高度冗余（CoCoHaNeRe 效应），导致 representation collapse 风险——val_loss 显著高于 random（0.092 vs 0.028），说明模型在 embedding-distance negatives 上学到的 区分信号更弱。\\n\"\n  },\n  {\n    \"name\": \"M3a SWE-bench Lite End-to-End Evaluation\",\n    \"description\": \"3 strategies × best checkpoint, Qwen3.6-27B agent, 300 instances end-to-end patch generation + test\",\n    \"results\": {\n      \"random_resolve_rate_pct\": 28.3,\n      \"dataflow_resolve_rate_pct\": 28.7,\n      \"emb_dist_resolve_rate_pct\": 27.8,\n      \"resolve_delta_dataflow_vs_random_pp\": 0.4,\n      \"resolve_delta_emb_vs_random_pp\": -0.5,\n      \"random_retrieval_recall5_e2e\": 0.805,\n      \"dataflow_retrieval_recall5_e2e\": 0.811,\n      \"emb_dist_retrieval_recall5_e2e\": 0.758,\n      \"avg_tokens_per_instance\": 12400,\n      \"timeout_instances\": 8,\n      \"total_eval_gpu_hours\": 38\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 5: SWE-bench Lite End-to-End Results\",\n        \"columns\": [\n          \"Retriever Strategy\",\n          \"Resolve Rate (%)\",\n          \"Retrieval R@5\",\n          \"Avg Tokens\"\n        ],\n        \"rows\": [\n          [\n            \"Random\",\n            \"28.3\",\n            \"0.805\",\n            \"12,200\"\n          ],\n          [\n            \"DataFlow-aware\",\n            \"28.7\",\n            \"0.811\",\n            \"12,400\"\n          ],\n          [\n            \"Emb-distance\",\n            \"27.8\",\n            \"0.758\",\n            \"12,600\"\n          ],\n          [\n            \"No retriever (BM25 only)\",\n            \"26.1\",\n            \"0.720\",\n            \"13,100\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"End-to-end 结果确认 retriever 改进被 agent pipeline 的噪声淹没。但与 BM25-only baseline 相比，所有 trained retrievers 都有 +2pp 的一致增益，证明对比学习训练本身有价值。关键 takeaway 是 dataflow 和 random 都是有效的 negative 策略，而 embedding-distance 即使在 end-to-end 也表现最差（虽然差异在统计噪声内）。论文应强调 retrieval-level 结果（Table 3）而非 resolve rate。\\n\\n\\nSWE-bench Lite 的 resolve rate 主要受 LLM agent 能力约束，而非 retriever 质量。 三种 retriever 的 R@5 差异在 5pp 以内，经过 Qwen3.6-27B 的 patch generation pipeline 后，检索质量差异被进一步稀释——agent 会通过多轮 tool call 自行浏览代码弥补检索遗漏， 也会因 LLM 推理错误浪费正确检索结果。因此 resolve rate delta 被压缩到 <1pp，远低于 统计显著性门槛。这符合 median 档位\\\"retriever strategy alone shows no significant resolve rate gain\\\"的预期。值得注意的是绝对 resolve rate ~28% 与 SWE-agent 等 baseline 在 Lite 上的表现大致可比，说明 pipeline 本身工作正常。\\n\"\n  },\n  {\n    \"name\": \"M3b RepoBench-R Cross-File Retrieval Evaluation\",\n    \"description\": \"retrieval-only evaluation on RepoBench-R cross-file completion benchmark, no LLM agent\",\n    \"results\": {\n      \"random_recall5\": 0.618,\n      \"dataflow_recall5\": 0.625,\n      \"emb_dist_recall5\": 0.592,\n      \"random_mrr\": 0.483,\n      \"dataflow_mrr\": 0.49,\n      \"emb_dist_mrr\": 0.461,\n      \"delta_dataflow_vs_random_R5_pp\": 0.7,\n      \"delta_emb_vs_random_R5_pp\": -2.6,\n      \"repobench_R_improvement_pp\": 0.7,\n      \"baseline_unixcoder_recall5\": 0.601,\n      \"baseline_swerank_recall5\": 0.645\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 6: RepoBench-R Retrieval Results\",\n        \"columns\": [\n          \"Model\",\n          \"R@1\",\n          \"R@5\",\n          \"R@10\",\n          \"MRR\"\n        ],\n        \"rows\": [\n          [\n            \"StructFuse-Random\",\n            \"0.385\",\n            \"0.618\",\n            \"0.742\",\n            \"0.483\"\n          ],\n          [\n            \"StructFuse-DataFlow\",\n            \"0.392\",\n            \"0.625\",\n            \"0.748\",\n            \"0.490\"\n          ],\n          [\n            \"StructFuse-EmbDist\",\n            \"0.360\",\n            \"0.592\",\n            \"0.718\",\n            \"0.461\"\n          ],\n          [\n            \"UniXcoder (baseline)\",\n            \"0.371\",\n            \"0.601\",\n            \"0.730\",\n            \"0.468\"\n          ],\n          [\n            \"SweRank (baseline)\",\n            \"0.412\",\n            \"0.645\",\n            \"0.771\",\n            \"0.510\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"RepoBench-R 结果与 SWE-bench retrieval 结果一致：dataflow ≈ random > embedding-distance。 跨 benchmark 的一致性增强了 Claim 2（embedding hurts）的可信度。与 SweRank 的差距可归因于 预训练数据量差异（SweRank 用 >100K instances，StructFuse 用 5K），这不影响 negative strategy 的相对比较。论文可在 Discussion 中指出 StructFuse 的方法论贡献独立于绝对性能。\\n\\n\\nRepoBench-R 是跨文件代码补全任务，与 SWE-bench 的 bug fix 场景不同。StructFuse 的对比 训练在 SWE-smith 数据上进行，domain shift 会削弱迁移效果。Dataflow vs random 的增益 仍然微弱（+0.7pp），因为 RepoBench 的跨文件依赖多为 import 级别而非深层 data-flow， 而 StructFuse 训练优化的结构信号（2-hop call graph connectivity）与 import-level 依赖的重合度有限。Embedding-distance negatives 的伤害在 RepoBench 上反而略弱于 SWE-bench（-2.6pp vs -5.0pp），因为 RepoBench 的 candidate pool 更小且更同质， embedding redundancy 的影响被缓解。与 SweRank baseline 的差距（-2.0pp）说明 domain-specific 预训练数据量仍然是决定性因素。\\n\"\n  },\n  {\n    \"name\": \"Embedding vs Random 深度分层分析\",\n    \"description\": \"按 repo size/complexity/domain 分层，分析 embedding negatives 何时最有害\",\n    \"results\": {\n      \"harm_by_repo_size\": {\n        \"small_lt50_delta_R5_pp\": -2.1,\n        \"medium_50_200_delta_R5_pp\": -6.8,\n        \"large_gt200_delta_R5_pp\": -5.3\n      },\n      \"harm_by_candidate_pool_diversity\": {\n        \"low_diversity_delta_R5_pp\": -7.2,\n        \"high_diversity_delta_R5_pp\": -2.8\n      },\n      \"harm_by_embedding_similarity_of_negatives\": {\n        \"top10pct_most_similar_delta_R5_pp\": -9.1,\n        \"bottom50pct_delta_R5_pp\": -1.5\n      },\n      \"correlation_neg_similarity_vs_harm\": 0.71\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 7: Embedding-Distance Harm Stratified by Repo Characteristics\",\n        \"columns\": [\n          \"Stratum\",\n          \"N instances\",\n          \"Emb R@5\",\n          \"Random R@5\",\n          \"Δ (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Small (<50 files)\",\n            \"3,200\",\n            \"0.782\",\n            \"0.803\",\n            \"−2.1\"\n          ],\n          [\n            \"Medium (50-200)\",\n            \"1,900\",\n            \"0.698\",\n            \"0.766\",\n            \"−6.8\"\n          ],\n          [\n            \"Large (>200)\",\n            \"850\",\n            \"0.732\",\n            \"0.785\",\n            \"−5.3\"\n          ]\n        ]\n      },\n      {\n        \"caption\": \"Table 8: Harm vs. Negative Embedding Similarity\",\n        \"columns\": [\n          \"Neg Similarity Quartile\",\n          \"Mean cosine sim\",\n          \"Δ R@5 (pp)\"\n        ],\n        \"rows\": [\n          [\n            \"Q4 (most similar)\",\n            \"0.91\",\n            \"−9.1\"\n          ],\n          [\n            \"Q3\",\n            \"0.82\",\n            \"−5.4\"\n          ],\n          [\n            \"Q2\",\n            \"0.73\",\n            \"−3.2\"\n          ],\n          [\n            \"Q1 (least similar)\",\n            \"0.61\",\n            \"−1.5\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 Claim 2 的核心支撑实验。梯度冗余假说得到定量验证：embedding similarity 与 harm 的 相关系数 0.71 说明 ~50% 的 harm variance 可由 negative 的 embedding 相似度解释。 Medium repo 是\\\"毒区\\\"的发现对 practitioner 有直接指导意义：在这个规模的 repo 上使用 embedding-distance hard negatives 风险最高。论文应将此分析放在 Results 的显著位置， 作为 headline finding 的主要证据。\\n\\n\\nEmbedding-distance negatives 的伤害机制是梯度冗余：当选中的 negatives 与 query 的 embedding 高度相似时，对比 loss 的梯度方向与 encoder 已有的相似性判断高度对齐，导致\\\"原地踏步\\\"甚至 过拟合到 surface feature。这个效应在 medium-size repo（50-200 files）最强，因为这些 repo 的 candidate pool 大小适中（足够多的 similar files 被选为 negatives），且文件间共享 更多命名约定和 import pattern（增加 surface similarity）。在 small repo 中，candidate pool 太小，embedding-distance 和 random 选到的 negatives 高度重叠（池子就那么大）， 差异被稀释。在 large repo 中，虽然有很多 similar candidates，但 pool diversity 也更高， 部分缓解了冗余效应。关键发现是 embedding 相似度与 harm 程度的相关系数 0.71——越相似的 negatives 越有害——这直接支持了\\\"梯度冗余\\\"假说。\\n\"\n  },\n  {\n    \"name\": \"M1 Scalability Statistics\",\n    \"description\": \"CodeQL 5K 规模的 timeout rate, extraction time, coverage, connected-but-not-gold ratio by repo size\",\n    \"results\": {\n      \"overall_timeout_pct\": 7.8,\n      \"overall_extraction_success_pct\": 86.0,\n      \"mean_extraction_time_s\": 38.5,\n      \"median_extraction_time_s\": 22.1,\n      \"p95_extraction_time_s\": 210.0,\n      \"p99_extraction_time_s\": 285.0,\n      \"by_repo_size\": {\n        \"small_lt50\": {\n          \"timeout_pct\": 1.2,\n          \"mean_time_s\": 12.3,\n          \"Z_pct\": 15.3,\n          \"coverage\": 0.92\n        },\n        \"medium_50_200\": {\n          \"timeout_pct\": 6.5,\n          \"mean_time_s\": 45.8,\n          \"Z_pct\": 38.9,\n          \"coverage\": 0.85\n        },\n        \"large_gt200\": {\n          \"timeout_pct\": 18.7,\n          \"mean_time_s\": 98.2,\n          \"Z_pct\": 29.1,\n          \"coverage\": 0.71\n        }\n      },\n      \"codeql_db_creation_failure_pct\": 6.2,\n      \"beniget_fallback_usage_pct\": 14.0\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 9: CodeQL Scalability at 5K Repos\",\n        \"columns\": [\n          \"Metric\",\n          \"Small\",\n          \"Medium\",\n          \"Large\",\n          \"Overall\"\n        ],\n        \"rows\": [\n          [\n            \"Timeout rate (%)\",\n            \"1.2\",\n            \"6.5\",\n            \"18.7\",\n            \"7.8\"\n          ],\n          [\n            \"Mean time (s)\",\n            \"12.3\",\n            \"45.8\",\n            \"98.2\",\n            \"38.5\"\n          ],\n          [\n            \"Z%\",\n            \"15.3\",\n            \"38.9\",\n            \"29.1\",\n            \"25.0\"\n          ],\n          [\n            \"DB creation success (%)\",\n            \"96.1\",\n            \"93.2\",\n            \"84.5\",\n            \"93.8\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claim 3 的 scalability 论点成立：总体 timeout <8%，在可接受范围内。论文应诚实报告 large repo 的 19% timeout，但指出这是 Python points-to analysis 的固有限制而非方法论 缺陷——Java/Go 等有更精确类型系统的语言预期会更好。Beniget fallback 的存在也增强了 方法的 robustness narrative。\\n\\n\\nCodeQL 的 2-hop bounded analysis 在小 repo 上非常高效（<15s mean），因为 call graph 小， 搜索空间有限。Medium repo 是 sweet spot：足够复杂以产生有意义的 connected set，但不至于 timeout。Large repo（>200 files）的 timeout 率升至 ~19%，主要因为 Python 的 points-to analysis 在大型项目中的路径爆炸——即使限制了 2-hop，每个 hop 内的 callee 数量可能很大。 总体 timeout <12% 满足 median tier 的上限。Beniget fallback 在 14% 的 instance 上 触发，主要是 CodeQL 数据库创建失败（6.2%）或 connected files <5 的情况。Coverage 从 pilot 的 100% 降至 86%，因为 5K 规模的 repo 质量更参差——包括 setup.py 缺失、 非标准项目结构、混合语言等 CodeQL 难以处理的情况。\\n\"\n  },\n  {\n    \"name\": \"Ablation: 1-hop vs 2-hop vs 3-hop Call-Graph Bounding\",\n    \"description\": \"不同 hop 数下的 connected set 大小、Z%、训练后 R@5 对比\",\n    \"results\": {\n      \"hop_1\": {\n        \"Z_pct\": 12.1,\n        \"avg_connected_files\": 2.3,\n        \"timeout_pct\": 2.1,\n        \"recall5_after_training\": 0.808\n      },\n      \"hop_2\": {\n        \"Z_pct\": 25.0,\n        \"avg_connected_files\": 4.2,\n        \"timeout_pct\": 7.8,\n        \"recall5_after_training\": 0.817\n      },\n      \"hop_3\": {\n        \"Z_pct\": 41.5,\n        \"avg_connected_files\": 12.8,\n        \"timeout_pct\": 22.3,\n        \"recall5_after_training\": 0.811\n      }\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 10: Hop Distance Ablation\",\n        \"columns\": [\n          \"Hops\",\n          \"Z%\",\n          \"Avg |connected|\",\n          \"Timeout %\",\n          \"R@5 (trained)\"\n        ],\n        \"rows\": [\n          [\n            \"1-hop\",\n            \"12.1%\",\n            \"2.3\",\n            \"2.1%\",\n            \"0.808\"\n          ],\n          [\n            \"2-hop\",\n            \"25.0%\",\n            \"4.2\",\n            \"7.8%\",\n            \"0.817\"\n          ],\n          [\n            \"3-hop\",\n            \"41.5%\",\n            \"12.8\",\n            \"22.3%\",\n            \"0.811\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"2-hop 的 Pareto optimality 支持论文的方法论选择。3-hop 的\\\"更多连接 ≠ 更好信号\\\"是一个 有意义的发现，说明结构信号的质量比数量重要。论文可在 ablation section 简洁呈现。\\n\\n\\n1-hop 提供最精确但最稀疏的结构信号：只有直接调用者/被调用者，Z% 仅 12%，大部分 instance 没有可用的 structural negative 信号，训练退化为 near-random。2-hop 是 pilot 验证的 配置，平衡了覆盖率和精度。3-hop 大幅增加 connected set（avg 12.8 files），Z% 升至 42%， 但引入了大量弱关联文件——3-hop 可达的文件可能只是通过一个公共 utility 函数间接连接， 不真正代表 semantic relevance。结果是 3-hop 的训练信号更嘈杂（precision 下降）， R@5 反而不如 2-hop。同时 3-hop 的 timeout 率飙升至 22%，实用性受限。这个消融验证了 2-hop 是合理的工程选择。\\n\"\n  },\n  {\n    \"name\": \"Ablation: Training Data Size Scaling (1K vs 3K vs 5K)\",\n    \"description\": \"固定 negative strategy=dataflow_aware, 不同训练数据量下的性能变化\",\n    \"results\": {\n      \"scale_1K\": {\n        \"recall5\": 0.785,\n        \"recall1\": 0.51,\n        \"training_time_h\": 0.7\n      },\n      \"scale_3K\": {\n        \"recall5\": 0.808,\n        \"recall1\": 0.541,\n        \"training_time_h\": 2.0\n      },\n      \"scale_5K\": {\n        \"recall5\": 0.817,\n        \"recall1\": 0.553,\n        \"training_time_h\": 3.2\n      },\n      \"scaling_slope_R5_per_1K\": 0.008,\n      \"log_linear_fit_r2\": 0.96\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 11: Training Data Scaling (DataFlow strategy)\",\n        \"columns\": [\n          \"Scale\",\n          \"R@1\",\n          \"R@5\",\n          \"R@10\",\n          \"Train time (h)\"\n        ],\n        \"rows\": [\n          [\n            \"1K\",\n            \"0.510\",\n            \"0.785\",\n            \"0.905\",\n            \"0.7\"\n          ],\n          [\n            \"3K\",\n            \"0.541\",\n            \"0.808\",\n            \"0.918\",\n            \"2.0\"\n          ],\n          [\n            \"5K\",\n            \"0.553\",\n            \"0.817\",\n            \"0.925\",\n            \"3.2\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Scaling 曲线支持 5K 作为\\\"enough but not saturated\\\"的选择。论文可引用此消融回应 reviewer 关于\\\"数据量不够\\\"的潜在质疑——trend line 外推到 10K 预计仅额外 +0.5pp， 不改变 strategy 之间的相对排序。\\n\\n\\n对比学习的数据效率通常遵循 log-linear scaling：从 1K 到 3K 的增益（+2.3pp R@5） 大于 3K 到 5K 的增益（+0.9pp R@5），边际收益递减但尚未饱和。1K 已经提供 reasonable baseline（R@5=0.785），因为 InfoNCE loss 的学习效率主要取决于 batch 内 negative diversity 而非总数据量。从 3K 到 5K 的小幅增益暗示 5K 接近当前 model capacity 和 negative strategy 下的 performance ceiling——进一步 scaling 需要更好的 negative mining 或更大的 model。log-linear fit R²=0.96 说明 scaling 行为规则可预测。\\n\"\n  },\n  {\n    \"name\": \"Ablation: Fusion Head (Embedding-only vs Structural-features-only vs Combined)\",\n    \"description\": \"评估 fusion head 的三种配置：纯 embedding、纯结构特征、和组合\",\n    \"results\": {\n      \"embedding_only_recall5\": 0.817,\n      \"structural_only_recall5\": 0.628,\n      \"combined_recall5\": 0.822,\n      \"combined_vs_embedding_delta_pp\": 0.5,\n      \"structural_features_auc\": 0.71\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 12: Fusion Head Ablation\",\n        \"columns\": [\n          \"Configuration\",\n          \"R@1\",\n          \"R@5\",\n          \"MRR\"\n        ],\n        \"rows\": [\n          [\n            \"Embedding-only\",\n            \"0.553\",\n            \"0.817\",\n            \"0.652\"\n          ],\n          [\n            \"Structural-features-only\",\n            \"0.398\",\n            \"0.628\",\n            \"0.485\"\n          ],\n          [\n            \"Combined (MLP fusion)\",\n            \"0.558\",\n            \"0.822\",\n            \"0.658\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Fusion head 的边际增益不支持在 pipeline 中保留结构特征用于推理。论文应将此作为 negative result 报告：structure helps training, not inference。这强化了方法论的核心 message—— 结构信号的价值在于 mining better training data，不在于作为 inference-time feature。 Simplifies deployment: 推理时只需标准 bi-encoder，无需 CodeQL。\\n\\n\\n纯结构特征（5 维：dataflow_distance, path_count, dependency_type, bm25_score, inter_procedural）在 retrieval 上表现差（R@5=0.628），因为它们是 sparse binary/integer features，信息量远不如 dense embedding。组合 fusion head 仅比 embedding-only 高 0.5pp， 因为 MLP fusion head 难以从已经被 embedding 学习过的信号中提取额外增益——结构特征与 embedding 学到的相似性有部分重叠（bm25_score 尤其如此），且 5 维 sparse features 对 128 维 MLP 来说信息密度太低。这个结果说明\\\"结构信号的价值主要在训练阶段（negative selection）而非推理阶段（feature fusion）\\\"——一个重要的方法论 insight。\\n\"\n  },\n  {\n    \"name\": \"Ablation: Dataflow-Distance Weighted vs Binary Connected/Disconnected\",\n    \"description\": \"比较 exp(-α·d) 加权 vs 简单 binary connected/disconnected 的负样本选择\",\n    \"results\": {\n      \"binary_recall5\": 0.815,\n      \"weighted_alpha1_recall5\": 0.817,\n      \"weighted_alpha05_recall5\": 0.814,\n      \"weighted_alpha2_recall5\": 0.812,\n      \"delta_weighted_vs_binary_pp\": 0.2\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 13: Distance Weighting Ablation\",\n        \"columns\": [\n          \"Weighting\",\n          \"α\",\n          \"R@5\",\n          \"Δ vs Binary\"\n        ],\n        \"rows\": [\n          [\n            \"Binary (0/1)\",\n            \"—\",\n            \"0.815\",\n            \"—\"\n          ],\n          [\n            \"exp(−αd)\",\n            \"0.5\",\n            \"0.814\",\n            \"−0.1\"\n          ],\n          [\n            \"exp(−αd)\",\n            \"1.0\",\n            \"0.817\",\n            \"+0.2\"\n          ],\n          [\n            \"exp(−αd)\",\n            \"2.0\",\n            \"0.812\",\n            \"−0.3\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Negative result 支持 Occam's razor：binary classification 足够。论文可在 appendix 简洁报告，减少方法复杂度。\\n\\n\\n在 Z=25% 的 median 场景下，大多数 instance 的 connected files 数量很少（avg 4.2）， dataflow distance 的粒度有限（大部分是 distance=1 或 2）。当信号本身就是 sparse binary 时，连续加权的额外信息量极小。Alpha=1 略优于 binary（+0.2pp）在噪声范围内。Alpha=2 过度惩罚远距离连接导致有效 connected set 更小，反而轻微下降。这个消融确认 binary connected/disconnected 足够，不需要复杂的距离加权——simplifies the method。\\n\"\n  },\n  {\n    \"name\": \"Failure Analysis: 50 SweRank/BM25 Failures\",\n    \"description\": \"抽样 50 个 SweRank/BM25 检索失败的 instance，人工标注 data-flow 是否有帮助\",\n    \"results\": {\n      \"total_analyzed\": 50,\n      \"category_counts\": {\n        \"dataflow_would_help\": 11,\n        \"dataflow_irrelevant_lexical_gap\": 18,\n        \"dataflow_irrelevant_logic_only\": 9,\n        \"gold_not_in_repo_scope\": 5,\n        \"multi_file_edit_needed\": 7\n      },\n      \"dataflow_help_rate_pct\": 22.0,\n      \"ceiling_if_perfect_structural_signal_pct\": 32.0\n    },\n    \"tables\": [\n      {\n        \"caption\": \"Table 14: Failure Category Breakdown (N=50)\",\n        \"columns\": [\n          \"Category\",\n          \"Count\",\n          \"%\",\n          \"DataFlow Helps?\"\n        ],\n        \"rows\": [\n          [\n            \"Lexical gap (no name overlap)\",\n            \"18\",\n            \"36%\",\n            \"Possible but sparse\"\n          ],\n          [\n            \"DataFlow reachable but missed\",\n            \"11\",\n            \"22%\",\n            \"Yes\"\n          ],\n          [\n            \"Logic-only fix (no structural dep)\",\n            \"9\",\n            \"18%\",\n            \"No\"\n          ],\n          [\n            \"Multi-file coordinated edit\",\n            \"7\",\n            \"14%\",\n            \"Partial\"\n          ],\n          [\n            \"Gold out of analysis scope\",\n            \"5\",\n            \"10%\",\n            \"No\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"这是 median tier 论文最关键的分析。Ceiling analysis 回答了\\\"为什么结构信号没有帮更多\\\" 的核心 reviewer 问题：(1) 大量失败与结构无关（lexical gap, logic-only）， (2) 即使结构信号完美，可恢复的失败也有限（ceiling ~32%），(3) Z=25% 进一步削弱 实际可实现增益。论文应将此作为 Discussion 的重要部分，展现对方法 limitation 的 诚实理解——这对 EMNLP reviewers 来说是加分项。\\n\\n\\n50 个失败 case 中只有 ~22% 是 data-flow 理论上可以帮助的——这些是 gold file 与 buggy file 存在调用链关系但 BM25/embedding 因命名差异未能 rank 高的情况。更多的失败（36%） 属于\\\"lexical gap\\\"类型：gold file 和 query 在词汇上完全无关（例如 config file vs source code），data-flow 也到达不了。逻辑修复（18%）需要理解程序语义而非结构关系。 这个分析解释了 dataflow negatives 为什么没有大幅超越 random：即使 perfect structural signal，ceiling improvement 也只有 ~32%×当前 failure rate ≈ 3-4pp，而在 Z=25% 的 实际信号密度下，可实现的增益更小。这是 median tier 的核心 ceiling analysis。\\n\"\n  },\n  {\n    \"name\": \"Qualitative Examples: Structural Negatives 改变检索结果的 Case Study\",\n    \"description\": \"挑选 5-10 个 dataflow-aware training 改变了 retrieval ranking 的 case\",\n    \"results\": {\n      \"total_cases_found\": 7,\n      \"cases_dataflow_improved_ranking\": 4,\n      \"cases_dataflow_no_change\": 2,\n      \"cases_dataflow_hurt\": 1,\n      \"best_case_rank_improvement\": \"gold file: rank 8→2\",\n      \"worst_case_rank_regression\": \"gold file: rank 3→5\"\n    },\n    \"tables\": [],\n    \"figures\": [],\n    \"analysis\": \"Qualitative examples 在论文中起\\\"让 reviewer 相信 method 有道理\\\"的作用。精选 4 个 compelling 的正面 case + 1 个诚实的负面 case，展现 balanced presentation。负面 case 自然引出 limitation：utility function 导致的 spurious connectivity 是 2-hop analysis 的固有弱点。可在 appendix 扩展到全部 7 个 case。\\n\\n在 dataflow ≈ random 的 median 场景下，能找到 dataflow 明确改善的 case 数量有限。 ~57% 的精选 case 展示了正面效果——这些通常是 medium-size repo 中 gold file 通过 2-hop call chain 与 buggy file 连接、但命名差异大导致 embedding-only retriever rank 不高的情况。Dataflow training 让 encoder 学会了对这类\\\"名字不像但结构相关\\\"的 文件给予更高 score。但也有 1 个 case 出现了 regression——CodeQL 的 connected set 恰好包含了一个 misleading file（通过 utility function 间接连接），dataflow training 错误地提升了它的 rank。这个 mixed picture 反映了 median tier 的现实。\\n\"\n  }\n]",
      "numLines": 766,
      "startLine": 1,
      "totalLines": 766
    }
  },
  "sourceToolAssistantUUID": "221f9b6d-0497-4e35-ba32-adcc44aada75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-i…",
  "leafUuid": "1523f84a-646c-4301-b012-7e86b42956d2",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate StructFuse median-tier simulation paper",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc"
}
```

---

### Assistant

_source line 15 · 2026-05-12T21:01:47.867Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the experiment data. Let me write the full LaTeX paper based on this data and the narrative guidance. The key pivot points are:

1. **Headline claim**: Embedding-distance negatives are harmful (Claim 2 becomes primary)
2. **Claim 1 downgrades**: Dataflow negatives are a viable alternative that avoids pitfalls
3. **Claim 3 survives**: Scalability methodology
4. **Ceiling analysis**: Why doesn't structural signal help more?
5. **Title pivot**: Emphasize "when hard negatives hurt"


6. **Key metrics**: DataFlow achieves R@5 of 0.817 ± 0.010 and R@1 of 0.553 ± 0.015, substantially outperforming embedding-distance negatives at 0.760 ± 0.012 and 0.489 ± 0.020 respectively, while random negatives fall in between at 0.810 ± 0.012 and 0.542 ± 0.018.

Now I'm generating the LaTeX document with these results and narrative structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1523f84a-646c-4301-b012-7e86b42956d2",
  "isSidechain": false,
  "requestId": "req_011CayMDzXQCUKN3xT4XfNzv",
  "type": "assistant",
  "uuid": "852814bc-c9d2-4349-9600-607397b94d35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Dw9oCC3huUihPpX6fTXDz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 77,
      "cache_creation_input_tokens": 13209,
      "cache_read_input_tokens": 23919,
      "output_tokens": 594,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 77,
          "output_tokens": 594,
          "cache_read_input_tokens": 23919,
          "cache_creation_input_tokens": 13209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13209
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

_source line 16 · 2026-05-12T21:01:48.215Z_

Now I have all the data. Let me write the full paper with the pivoted framing: "when hard negatives hurt."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "852814bc-c9d2-4349-9600-607397b94d35",
  "isSidechain": false,
  "requestId": "req_011CayMDzXQCUKN3xT4XfNzv",
  "type": "assistant",
  "uuid": "04fa05a8-37b9-415a-9bdd-96f9d86e3314",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Dw9oCC3huUihPpX6fTXDz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 77,
      "cache_creation_input_tokens": 13209,
      "cache_read_input_tokens": 23919,
      "output_tokens": 594,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 77,
          "output_tokens": 594,
          "cache_read_input_tokens": 23919,
          "cache_creation_input_tokens": 13209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13209
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

_source line 17 · 2026-05-12T21:01:49.966Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RfySnCAmYcjumYNXXSwLd4`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median && which pdflatex",
  "description": "Check output directory exists and pdflatex availability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04fa05a8-37b9-415a-9bdd-96f9d86e3314",
  "isSidechain": false,
  "requestId": "req_011CayMDzXQCUKN3xT4XfNzv",
  "type": "assistant",
  "uuid": "f4ad0742-8e73-4a02-b090-835a85405c63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Dw9oCC3huUihPpX6fTXDz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 77,
      "cache_creation_input_tokens": 13209,
      "cache_read_input_tokens": 23919,
      "output_tokens": 594,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13209,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 77,
          "output_tokens": 594,
          "cache_read_input_tokens": 23919,
          "cache_creation_input_tokens": 13209,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13209
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

_source line 18 · 2026-05-12T21:01:50.163Z_

<details><summary>↩ Tool result · `toolu_01RfySnCAmYcjumYNXXSwLd4`</summary>

```text
/usr/bin/pdflatex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4ad0742-8e73-4a02-b090-835a85405c63",
  "isSidechain": false,
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "a96db20f-69df-4473-81df-f9cb6b9c0da9",
  "toolUseResult": {
    "stdout": "/usr/bin/pdflatex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "f4ad0742-8e73-4a02-b090-835a85405c63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-12T21:04:39.439Z_

<details open><summary>🔧 Tool call — Write · `toolu_01AoyLhNMFYE5DwhFaWHqnif`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex",
  "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\aclfinalcopy\n\n\\title{When Hard Negatives Hurt: Embedding-Distance Negative Mining\\\\Degrades Contrastive Code Retrieval}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nHard negative mining is widely assumed to improve contrastive learning for code retrieval.\nWe challenge this assumption by showing that \\emph{embedding-distance} hard negatives---the most popular strategy---\\emph{actively degrade} retrieval quality compared to random negatives.\nOn SWE-bench Lite, embedding-distance negatives reduce Recall@5 by 5.0 percentage points relative to random negatives ($p{=}0.003$, 3 seeds), with harm concentrated in repositories where selected negatives have high cosine similarity to the query (Pearson $r{=}0.71$ between negative similarity and performance degradation).\nWe trace the cause to \\emph{gradient redundancy}: negatives that are already close in embedding space provide learning signal that overlaps with the encoder's existing similarity judgments, leading to representation stagnation.\nAs a safe alternative, we propose \\emph{structure-grounded} negative mining using inter-procedural data-flow connectivity extracted via CodeQL.\nData-flow negatives perform on par with random negatives ($\\Delta$R@5 $= +0.7$pp, $p{=}0.42$) while avoiding the pitfalls of embedding-distance selection.\nWe further demonstrate that scope-bounded CodeQL analysis scales to 5,000 repositories with $<$8\\% timeout rate.\nA ceiling analysis on 50 retrieval failures reveals that only 22\\% are addressable by structural signal, explaining the modest gains and providing a roadmap for future work.\nOur findings serve as a cautionary result for the contrastive code retrieval community: harder negatives are not always better.\n\\end{abstract}\n\n\\section{Introduction}\n\nContrastive learning has become the dominant paradigm for training code retrieval models \\cite{guo2022unixcoder,jimenez2024swebench}.\nA central design choice is \\emph{negative mining}: selecting negative examples that maximize learning signal.\nThe prevailing wisdom, inherited from vision and NLP, is that ``harder'' negatives---those closest to the query in embedding space---yield faster convergence and better representations.\n\nWe present evidence that this wisdom does not transfer straightforwardly to code retrieval.\nIn a controlled comparison across three negative mining strategies---random, embedding-distance, and structure-grounded (data-flow-aware)---we find that embedding-distance negatives \\emph{consistently underperform random negatives} on two benchmarks (SWE-bench Lite and RepoBench-R) across three random seeds.\nThe degradation is statistically significant ($-5.0$pp Recall@5, $p{=}0.003$) and practically meaningful.\n\nThe mechanism we identify is \\emph{gradient redundancy}.\nEmbedding-distance mining selects negatives that are already similar to the query in the encoder's representation space.\nThe resulting gradients reinforce the model's existing similarity judgments rather than teaching new distinctions, leading to representation stagnation.\nWe provide quantitative evidence: harm correlates with the cosine similarity of selected negatives ($r{=}0.71$), and the training loss for embedding-distance negatives (0.092) is substantially higher than for random (0.028), indicating the model fails to learn meaningful distinctions.\n\nAs an alternative, we explore \\emph{structure-grounded} negative mining.\nGiven a code repository with a formal structural graph (here, inter-procedural data-flow connectivity computed via CodeQL), we define a structure-grounded hard negative as:\n\\begin{equation}\n\\arg\\max_{x \\in D:\\, s(x,q) > \\tau \\,\\wedge\\, \\neg\\text{reach}_G(x,q)} s(x,q)\n\\label{eq:struct-neg}\n\\end{equation}\nwhere $D$ is the retrieval domain, $G$ the structural graph, $s$ a text similarity function, and $q$ the query.\nThis selects files that are textually similar to the query but structurally disconnected---a complementary signal dimension that embedding similarity cannot recover.\nCrucially, the structural graph is externally fixed and does not drift with encoder updates, unlike embedding-distance negatives that shift every training epoch.\n\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{Cautionary finding}: Embedding-distance hard negatives significantly harm contrastive code retrieval ($-5.0$pp R@5 on SWE-bench Lite, $-2.6$pp on RepoBench-R), with harm driven by gradient redundancy (Section~\\ref{sec:main-results}, \\ref{sec:stratified}).\n\n\\item \\textbf{Safe alternative}: Data-flow-grounded negatives match random-negative performance without introducing the pathologies of embedding-distance selection, providing a viable drop-in replacement (Section~\\ref{sec:main-results}).\n\n\\item \\textbf{Scalability}: Scope-bounded inter-procedural data-flow analysis via CodeQL scales to 5,000 repositories with 7.8\\% overall timeout rate and 86\\% extraction success (Section~\\ref{sec:scalability}).\n\n\\item \\textbf{Ceiling analysis}: A failure taxonomy explains why structural signal does not help more: only 22\\% of retrieval failures are addressable by data-flow connectivity, bounding the achievable gain to $\\sim$3--4pp even with perfect structural signal (Section~\\ref{sec:ceiling}).\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Hard negative mining in contrastive learning.}\nHard negative mining has a long history in metric learning \\cite{schroff2015facenet}.\nIn NLP, methods such as DPR \\cite{karpukhin2020dense} and ANCE \\cite{xiong2021approximate} use embedding-distance or in-batch negatives to improve dense retrieval.\nCoCoHaNeRe \\cite{shi2023cochanere} studies hard negatives for code search and finds that embedding-distance negatives can be redundant with the encoder's learned similarity---a finding our work extends with controlled experiments and a mechanistic explanation.\n\n\\paragraph{Code retrieval for software engineering.}\nSweRank \\cite{zhang2025swerank} trains a code retriever on large-scale SWE data.\nSWE-Fixer \\cite{xie2025swefixer} combines retrieval with LLM-based repair.\nLocAgent \\cite{muhammad2024locagent}, RANGER, and CodexGraph use structural information at inference time but not for training signal.\nARISE \\cite{wu2024arise} leverages intra-procedural data-flow but is limited to single-function scope.\nOur work is the first to use inter-procedural data-flow connectivity as a \\emph{training signal} for negative mining.\n\n\\paragraph{Structural analysis in code understanding.}\nCodeQL \\cite{codeql} provides a declarative framework for semantic code analysis.\nPrior work uses call graphs for bug detection and program understanding but not for contrastive learning data curation.\nWe show that 2-hop bounded CodeQL analysis provides a practical, model-independent method for computing structural connectivity at scale.\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nWe consider file-level code retrieval for repository-level bug repair.\nGiven a bug report (issue description and stack trace) as query $q$ and a repository with files $\\{f_1, \\ldots, f_n\\}$, the retriever ranks files by relevance.\nGold files are those modified in the ground-truth patch.\nWe train a bi-encoder retriever using InfoNCE contrastive loss with different negative mining strategies.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare three strategies, holding all other variables constant (model architecture, training data, hyperparameters, positive examples):\n\n\\paragraph{Random negatives.} For each query, sample $k$ negatives uniformly at random from non-gold files in the same repository.\n\n\\paragraph{Embedding-distance negatives.} Encode all repository files with the current encoder checkpoint. Select the $k$ non-gold files with highest cosine similarity to the query embedding. Re-mine every epoch to track encoder updates.\n\n\\paragraph{Data-flow-aware negatives.} Using the structural graph $G$ from CodeQL, partition non-gold files into \\emph{connected} ($\\text{reach}_G(f, q^*)$ for any gold file $q^*$) and \\emph{disconnected}.\nSelect negatives that are textually similar (BM25 score $> \\tau$) but structurally disconnected (Eq.~\\ref{eq:struct-neg}).\nWhen fewer than $k$ candidates satisfy both criteria, backfill with random negatives.\n\n\\subsection{Structural Graph Construction}\n\nWe extract inter-procedural data-flow connectivity using CodeQL with 2-hop call-graph bounding.\nFor each instance, we:\n(1) create a CodeQL database from the repository snapshot,\n(2) run a custom QL query that computes 2-hop reachability from functions in gold files,\n(3) collect all files containing reachable functions as the \\emph{connected set}.\nFiles in the connected set but not in the gold set provide structure-grounded hard negative candidates (the ``connected$\\setminus$gold'' set).\n\nWe define $Z\\%$ as the fraction of instances where $|\\text{connected} \\setminus \\text{gold}| > 0$, measuring structural signal availability.\n\n\\subsection{Model and Training}\n\nWe fine-tune Qwen2.5-Coder-3B with LoRA adapters as a bi-encoder.\nTraining uses InfoNCE loss with temperature 0.05, batch size 32, learning rate 2e-5 with cosine schedule, for 3 epochs.\nEach strategy is trained on the same 5,000 SWE-smith instances with 3 random seeds (42, 123, 456).\n\n\\section{Experiments}\n\n\\subsection{CodeQL Extraction at Scale}\n\\label{sec:scalability}\n\nTable~\\ref{tab:codeql-scale} reports CodeQL extraction statistics at 5,000-repository scale compared to a 50-repository pilot.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{50-repo pilot} & \\textbf{5K full} \\\\\n\\midrule\n$Z\\%$ (connected$\\setminus$gold $> 0$) & 40.8\\% & 25.0\\% \\\\\nTimeout rate & 4.0\\% & 7.8\\% \\\\\nGold $\\in$ connected ratio & 100\\% & 72\\% \\\\\nMean extraction time (s) & 43.4 & 38.5 \\\\\nAvg $|$connected $\\setminus$ gold$|$ & 6.0 & 4.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CodeQL extraction statistics. The pilot over-estimated $Z\\%$ due to curation bias toward medium-size repos with rich call graphs.}\n\\label{tab:codeql-scale}\n\\end{table}\n\n$Z\\%$ drops from 40.8\\% (pilot) to 25.0\\% (full scale) because the 5K corpus includes many small/script-style repositories lacking cross-file call chains.\nTable~\\ref{tab:codeql-strata} reveals a non-monotonic relationship with repository size: medium repositories (50--200 files) are the ``sweet spot'' with $Z\\%{=}38.9\\%$, while small repos lack call structure ($Z\\%{=}15.3\\%$) and large repos suffer from higher timeouts ($18.7\\%$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{\\# Inst.} & \\textbf{$Z\\%$} & \\textbf{Avg extra conn.} \\\\\n\\midrule\nSmall ($<$50 files) & 7,200 & 15.3\\% & 1.8 \\\\\nMedium (50--200) & 3,800 & 38.9\\% & 7.5 \\\\\nLarge ($>$200) & 1,800 & 29.1\\% & 6.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$Z\\%$ by repository size stratum. Medium repositories provide the richest structural signal.}\n\\label{tab:codeql-strata}\n\\end{table}\n\nOverall timeout rate of 7.8\\% and extraction success of 86\\% demonstrate that scope-bounded CodeQL analysis is practical at scale.\nThe beniget fallback triggers for 14\\% of instances where CodeQL database creation fails (6.2\\%) or produces insufficient connected files.\n\n\\subsection{Main Results: Three-Strategy Comparison}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main-results} presents retrieval performance on SWE-bench Lite (pool size 50) across three seeds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{Val Loss} \\\\\n\\midrule\nRandom & .542{\\scriptsize$\\pm$.018} & .810{\\scriptsize$\\pm$.012} & .921{\\scriptsize$\\pm$.008} & 0.028 \\\\\nDataFlow & .553{\\scriptsize$\\pm$.015} & .817{\\scriptsize$\\pm$.010} & .925{\\scriptsize$\\pm$.007} & 0.035 \\\\\nEmbDist & .489{\\scriptsize$\\pm$.020} & .760{\\scriptsize$\\pm$.012} & .878{\\scriptsize$\\pm$.011} & 0.092 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Retrieval performance by negative mining strategy (SWE-bench Lite, 3 seeds). EmbDist significantly underperforms Random.}\n\\label{tab:main-results}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\Delta$R@1} & \\textbf{$\\Delta$R@5} & \\textbf{$p$ (R@5)} \\\\\n\\midrule\nDataFlow $-$ Random & +1.1 & +0.7 & 0.42 \\\\\nEmbDist $-$ Random & $-$5.3 & $-$5.0 & 0.003 \\\\\nDataFlow $-$ EmbDist & +6.4 & +5.7 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise deltas (pp) with paired $t$-test $p$-values. Embedding-distance negatives significantly degrade performance.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe results reveal an asymmetric pattern.\n\\textbf{Embedding-distance negatives significantly harm retrieval}: $-5.0$pp R@5 vs.\\ random ($p{=}0.003$), consistent across all three seeds.\nThe elevated validation loss (0.092 vs.\\ 0.028) indicates the model fails to learn useful distinctions from these negatives.\n\\textbf{Data-flow negatives match random performance}: $+0.7$pp R@5 ($p{=}0.42$), within seed variance.\nThis makes data-flow negatives a safe alternative that avoids embedding-distance pathologies without degrading performance.\n\n\\paragraph{Cross-benchmark validation.}\nTable~\\ref{tab:repobench} confirms these findings on RepoBench-R, a cross-file code completion benchmark.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{MRR} \\\\\n\\midrule\nStructFuse-Random & .385 & .618 & .742 & .483 \\\\\nStructFuse-DataFlow & .392 & .625 & .748 & .490 \\\\\nStructFuse-EmbDist & .360 & .592 & .718 & .461 \\\\\n\\midrule\nUniXcoder & .371 & .601 & .730 & .468 \\\\\nSweRank & .412 & .645 & .771 & .510 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{RepoBench-R retrieval results. The embedding-distance harm pattern replicates ($-2.6$pp R@5 vs.\\ Random). Gap to SweRank reflects training data scale (5K vs.\\ $>$100K).}\n\\label{tab:repobench}\n\\end{table}\n\nEmbedding-distance harm replicates on RepoBench-R ($-2.6$pp R@5), though attenuated due to smaller, more homogeneous candidate pools.\nThe gap to SweRank ($-2.0$pp R@5) reflects training data volume differences (5K vs.\\ $>$100K instances), not negative strategy.\n\n\\paragraph{End-to-end evaluation.}\nTable~\\ref{tab:e2e} reports SWE-bench Lite resolve rates using Qwen3.6-27B as the downstream agent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Retriever} & \\textbf{Resolve (\\%)} & \\textbf{R@5} & \\textbf{Avg Tokens} \\\\\n\\midrule\nRandom & 28.3 & 0.805 & 12,200 \\\\\nDataFlow & 28.7 & 0.811 & 12,400 \\\\\nEmbDist & 27.8 & 0.758 & 12,600 \\\\\nBM25 only & 26.1 & 0.720 & 13,100 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SWE-bench Lite end-to-end results. Retrieval differences are attenuated by the LLM agent's ability to compensate via tool calls. All trained retrievers improve over BM25-only.}\n\\label{tab:e2e}\n\\end{table}\n\nResolve rate differences are compressed to $<$1pp, as the LLM agent compensates for retrieval gaps through multi-turn code browsing.\nHowever, all trained retrievers show a consistent $+$2pp gain over BM25-only, validating the value of contrastive training itself.\n\n\\subsection{Why Embedding-Distance Negatives Hurt: Stratified Analysis}\n\\label{sec:stratified}\n\nTo understand the mechanism behind embedding-distance harm, we stratify results by repository characteristics and negative similarity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{$N$} & \\textbf{Emb R@5} & \\textbf{Rand R@5} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nSmall ($<$50) & 3,200 & .782 & .803 & $-$2.1 \\\\\nMedium (50--200) & 1,900 & .698 & .766 & $-$6.8 \\\\\nLarge ($>$200) & 850 & .732 & .785 & $-$5.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Embedding-distance harm by repository size. Medium repos are the ``harm zone'' ($-6.8$pp).}\n\\label{tab:harm-strata}\n\\end{table}\n\nMedium-size repositories exhibit the greatest harm ($-6.8$pp), because they have enough similar files for embedding-distance mining to exploit, yet files share naming conventions that inflate surface similarity.\nSmall repos show muted harm ($-2.1$pp) because the candidate pool is too small for embedding-distance and random to diverge substantially.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Neg Similarity Quartile} & \\textbf{Mean cos sim} & \\textbf{$\\Delta$ R@5 (pp)} \\\\\n\\midrule\nQ4 (most similar) & 0.91 & $-$9.1 \\\\\nQ3 & 0.82 & $-$5.4 \\\\\nQ2 & 0.73 & $-$3.2 \\\\\nQ1 (least similar) & 0.61 & $-$1.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Harm as a function of negative embedding similarity. Pearson $r{=}0.71$ confirms gradient redundancy.}\n\\label{tab:harm-similarity}\n\\end{table}\n\nTable~\\ref{tab:harm-similarity} provides direct evidence for the gradient redundancy hypothesis.\nPerformance degradation scales monotonically with the cosine similarity of selected negatives ($r{=}0.71$).\nThe most similar negatives (Q4, mean similarity 0.91) cause $-9.1$pp harm, while the least similar (Q1, 0.61) cause only $-1.5$pp.\nThis suggests that embedding-distance mining concentrates the negative set in a region where the encoder already has strong opinions, yielding gradients that reinforce existing representations rather than teaching new distinctions.\n\n\\subsection{Ceiling Analysis: Why Doesn't Structural Signal Help More?}\n\\label{sec:ceiling}\n\nA natural question is why data-flow negatives do not \\emph{substantially outperform} random negatives.\nWe address this through a failure analysis of 50 instances where BM25/SweRank retrieval fails.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Failure Category} & \\textbf{$N$} & \\textbf{\\%} & \\textbf{DF Helps?} \\\\\n\\midrule\nLexical gap (no name overlap) & 18 & 36 & Sparse \\\\\nDataFlow reachable but missed & 11 & 22 & Yes \\\\\nLogic-only fix (no struct.\\ dep) & 9 & 18 & No \\\\\nMulti-file coordinated edit & 7 & 14 & Partial \\\\\nGold out of analysis scope & 5 & 10 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure category breakdown ($N{=}50$). Only 22\\% of failures are directly addressable by structural signal.}\n\\label{tab:failure}\n\\end{table}\n\nThree factors bound the achievable gain from structural signal:\n\n\\paragraph{(1) Low signal density ($Z\\%{=}25\\%$).}\nOnly one quarter of training instances have connected-but-not-gold structural negatives.\nFor the remaining 75\\%, the data-flow miner falls back to BM25-hard or random padding, making its behavior approximate random.\n\n\\paragraph{(2) Limited addressable failures.}\nOnly 22\\% of retrieval failures involve gold files reachable via data-flow that text-based methods miss (Table~\\ref{tab:failure}).\nThe largest failure category (36\\%) is lexical gap---gold files with no naming overlap with the query---which structural connectivity also cannot bridge.\n\n\\paragraph{(3) Random negatives are already near-optimal at high pool diversity.}\nAt pool sizes $\\geq$50, approximately 15--20\\% of randomly sampled negatives happen to be BM25-similar, providing ``accidental hard negatives'' that narrow the margin for structured selection.\n\nCombining these factors, even with perfect structural signal, the ceiling improvement is approximately $32\\%$ of the current failure rate, yielding $\\sim$3--4pp maximum achievable gain.\nAt $Z\\%{=}25\\%$, the realized gain is further attenuated, explaining the observed $+0.7$pp.\n\n\\subsection{Ablation Studies}\n\n\\paragraph{Call-graph hop distance.}\nTable~\\ref{tab:hop} compares 1-hop, 2-hop, and 3-hop bounding for connected set computation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Hops} & \\textbf{$Z\\%$} & \\textbf{Avg $|$conn$|$} & \\textbf{Timeout \\%} & \\textbf{R@5} \\\\\n\\midrule\n1 & 12.1 & 2.3 & 2.1 & .808 \\\\\n2 & 25.0 & 4.2 & 7.8 & .817 \\\\\n3 & 41.5 & 12.8 & 22.3 & .811 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hop distance ablation. 2-hop is Pareto-optimal: more signal than 1-hop without the noise and timeouts of 3-hop.}\n\\label{tab:hop}\n\\end{table}\n\n2-hop is Pareto-optimal: it provides sufficient $Z\\%$ (25\\%) with manageable timeouts (7.8\\%).\n3-hop increases $Z\\%$ to 41.5\\% but introduces noisy connections through shared utility functions, degrading R@5 to 0.811 while tripling the timeout rate.\n\n\\paragraph{Training data scale.}\nTable~\\ref{tab:scaling} shows performance scaling with training data size under the data-flow strategy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Scale} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{Time (h)} \\\\\n\\midrule\n1K & .510 & .785 & .905 & 0.7 \\\\\n3K & .541 & .808 & .918 & 2.0 \\\\\n5K & .553 & .817 & .925 & 3.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Training data scaling. Log-linear fit $R^2{=}0.96$; diminishing returns suggest 5K is near-saturated for this model capacity.}\n\\label{tab:scaling}\n\\end{table}\n\nPerformance follows a log-linear scaling law ($R^2{=}0.96$), with diminishing returns from 3K to 5K ($+0.9$pp vs.\\ $+2.3$pp from 1K to 3K).\nExtrapolation suggests $\\sim$10K instances would yield only $\\sim$$+0.5$pp additional gain, indicating that negative strategy comparisons at 5K reflect stable relative rankings.\n\n\\paragraph{Fusion head.}\nTable~\\ref{tab:fusion} ablates inference-time structural features.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{MRR} \\\\\n\\midrule\nEmbedding-only & .553 & .817 & .652 \\\\\nStructural-only & .398 & .628 & .485 \\\\\nCombined (MLP) & .558 & .822 & .658 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Fusion head ablation. Structural features add only $+0.5$pp at inference time, confirming that structure helps training, not inference.}\n\\label{tab:fusion}\n\\end{table}\n\nThe combined fusion head adds only $+0.5$pp over embedding-only, confirming that the value of structural information lies in training data curation (negative mining), not inference-time features.\nThis simplifies deployment: the retriever is a standard bi-encoder at inference time with no CodeQL dependency.\n\n\\paragraph{Distance weighting.}\nBinary connected/disconnected labeling ($R@5{=}0.815$) performs comparably to exponential distance weighting ($R@5{=}0.817$ at $\\alpha{=}1.0$, $\\Delta{=}+0.2$pp).\nSince most instances have sparse connectivity (avg.\\ 4.2 connected files), continuous weighting adds negligible information.\nWe adopt binary classification for simplicity.\n\n\\section{Discussion}\n\n\\paragraph{Implications for practitioners.}\nOur results suggest that the common practice of using embedding-distance hard negatives for code retrieval should be reconsidered, particularly for medium-size repositories (50--200 files) where harm is most pronounced ($-6.8$pp).\nRandom negatives are a surprisingly strong baseline, and structure-grounded negatives offer a safe alternative without the gradient redundancy risk.\n\n\\paragraph{Why not stronger gains from structure?}\nThe ceiling analysis identifies three bottlenecks: (1) $Z\\%{=}25\\%$ means structural signal is sparse across the training set, (2) the majority of retrieval failures (lexical gap, logic-only) are not addressable by structural connectivity, and (3) random negatives at high pool diversity already provide near-sufficient contrastive signal.\nImproving $Z\\%$ through richer static analysis (e.g., type-based connectivity, import graph augmentation) or targeting medium-size repos where $Z\\%{=}38.9\\%$ are promising directions.\n\n\\paragraph{Generalizability.}\nThe gradient redundancy phenomenon is not specific to code.\nAny domain where embedding-distance mining selects negatives that overlap with the encoder's learned similarity is susceptible.\nStructure-grounded negative mining generalizes to domains with external structural knowledge: molecular interaction networks for drug discovery, circuit topology for hardware retrieval, and knowledge graph connectivity for entity linking.\nCode is an ideal testbed due to the formal semantic guarantees of static analysis.\n\n\\paragraph{Limitations.}\n(1)~We evaluate a single encoder architecture (Qwen2.5-Coder-3B); the magnitude of embedding-distance harm may vary with model capacity.\n(2)~CodeQL extraction is limited to Python repositories; languages with richer type systems may yield higher $Z\\%$ and stronger structural signal.\n(3)~The ceiling analysis is based on 50 manually annotated instances; a larger study could refine the category proportions.\n(4)~End-to-end resolve rates show $<$1pp differences, meaning the retrieval findings have limited downstream impact in the presence of a capable LLM agent.\n\n\\section{Conclusion}\n\nWe present a cautionary result for the contrastive code retrieval community: embedding-distance hard negatives, the most popular mining strategy, significantly degrade retrieval quality compared to random negatives.\nThe mechanism---gradient redundancy from selecting negatives already close in embedding space---is quantitatively confirmed by a strong correlation ($r{=}0.71$) between negative similarity and performance harm.\nStructure-grounded negatives using inter-procedural data-flow connectivity offer a safe alternative that matches random-negative performance while avoiding embedding-distance pathologies.\nA ceiling analysis explains the modest gains and provides actionable hypotheses for future work: increasing structural signal density, enriching connectivity with type information, and focusing on medium-size repositories where structural signal is richest.\n\n\\bibliography{paper}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Guo et~al.(2022)]{guo2022unixcoder}\nDaya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, and Jian Yin.\n\\newblock UniXcoder: Unified cross-modal pre-training for code representation.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Jimenez et~al.(2024)]{jimenez2024swebench}\nCarlos~E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan.\n\\newblock {SWE}-bench: Can language models resolve real-world {GitHub} issues?\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Schroff et~al.(2015)]{schroff2015facenet}\nFlorian Schroff, Dmitry Kalenichenko, and James Philbin.\n\\newblock FaceNet: A unified embedding for face recognition and clustering.\n\\newblock In \\emph{CVPR}, 2015.\n\n\\bibitem[Karpukhin et~al.(2020)]{karpukhin2020dense}\nVladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih.\n\\newblock Dense passage retrieval for open-domain question answering.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Xiong et~al.(2021)]{xiong2021approximate}\nLee Xiong, Chenyan Xiong, Ye~Li, Kwok-Fung Tang, Jialin Liu, Paul~N. Bennett, Junaid Ahmed, and Arnold Overwijk.\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Shi et~al.(2023)]{shi2023cochanere}\nJian Shi, Daya Guo, Shuai Lu, and Duyu Tang.\n\\newblock CoCoHaNeRe: Contrastive code hard negative retrieval.\n\\newblock \\emph{arXiv preprint arXiv:2305.XXXXX}, 2023.\n\n\\bibitem[Zhang et~al.(2025)]{zhang2025swerank}\nFan Zhang et~al.\n\\newblock SweRank: Training code retrievers for software engineering tasks.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Xie et~al.(2025)]{xie2025swefixer}\nYuntao Xie et~al.\n\\newblock SWE-Fixer: Training open-source LLMs for effective and efficient GitHub issue resolution.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Muhammad et~al.(2024)]{muhammad2024locagent}\nAli Muhammad et~al.\n\\newblock LocAgent: Graph-guided LLM agents for code localization.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Wu et~al.(2024)]{wu2024arise}\nSiru Wu et~al.\n\\newblock ARISE: Automated runtime information-guided SE.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[{CodeQL}(2024)]{codeql}\n{GitHub}.\n\\newblock {CodeQL} documentation.\n\\newblock \\url{https://codeql.github.com/docs/}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a96db20f-69df-4473-81df-f9cb6b9c0da9",
  "isSidechain": false,
  "requestId": "req_011CayMF2ie9goJkgAP8wDYv",
  "type": "assistant",
  "uuid": "388485ff-9bf5-490c-83a6-bd56208bccb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0193XnnbWdUm8d9LQ7D8Gr4E",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 37128,
      "output_tokens": 9085,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9085,
          "cache_read_input_tokens": 37128,
          "cache_creation_input_tokens": 689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 689
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

_source line 20 · 2026-05-12T21:04:39.461Z_

<details><summary>↩ Tool result · `toolu_01AoyLhNMFYE5DwhFaWHqnif`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "388485ff-9bf5-490c-83a6-bd56208bccb5",
  "isSidechain": false,
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "7924fbcd-63e1-46f1-bac9-791d90172577",
  "toolUseResult": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex",
    "content": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\aclfinalcopy\n\n\\title{When Hard Negatives Hurt: Embedding-Distance Negative Mining\\\\Degrades Contrastive Code Retrieval}\n\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nHard negative mining is widely assumed to improve contrastive learning for code retrieval.\nWe challenge this assumption by showing that \\emph{embedding-distance} hard negatives---the most popular strategy---\\emph{actively degrade} retrieval quality compared to random negatives.\nOn SWE-bench Lite, embedding-distance negatives reduce Recall@5 by 5.0 percentage points relative to random negatives ($p{=}0.003$, 3 seeds), with harm concentrated in repositories where selected negatives have high cosine similarity to the query (Pearson $r{=}0.71$ between negative similarity and performance degradation).\nWe trace the cause to \\emph{gradient redundancy}: negatives that are already close in embedding space provide learning signal that overlaps with the encoder's existing similarity judgments, leading to representation stagnation.\nAs a safe alternative, we propose \\emph{structure-grounded} negative mining using inter-procedural data-flow connectivity extracted via CodeQL.\nData-flow negatives perform on par with random negatives ($\\Delta$R@5 $= +0.7$pp, $p{=}0.42$) while avoiding the pitfalls of embedding-distance selection.\nWe further demonstrate that scope-bounded CodeQL analysis scales to 5,000 repositories with $<$8\\% timeout rate.\nA ceiling analysis on 50 retrieval failures reveals that only 22\\% are addressable by structural signal, explaining the modest gains and providing a roadmap for future work.\nOur findings serve as a cautionary result for the contrastive code retrieval community: harder negatives are not always better.\n\\end{abstract}\n\n\\section{Introduction}\n\nContrastive learning has become the dominant paradigm for training code retrieval models \\cite{guo2022unixcoder,jimenez2024swebench}.\nA central design choice is \\emph{negative mining}: selecting negative examples that maximize learning signal.\nThe prevailing wisdom, inherited from vision and NLP, is that ``harder'' negatives---those closest to the query in embedding space---yield faster convergence and better representations.\n\nWe present evidence that this wisdom does not transfer straightforwardly to code retrieval.\nIn a controlled comparison across three negative mining strategies---random, embedding-distance, and structure-grounded (data-flow-aware)---we find that embedding-distance negatives \\emph{consistently underperform random negatives} on two benchmarks (SWE-bench Lite and RepoBench-R) across three random seeds.\nThe degradation is statistically significant ($-5.0$pp Recall@5, $p{=}0.003$) and practically meaningful.\n\nThe mechanism we identify is \\emph{gradient redundancy}.\nEmbedding-distance mining selects negatives that are already similar to the query in the encoder's representation space.\nThe resulting gradients reinforce the model's existing similarity judgments rather than teaching new distinctions, leading to representation stagnation.\nWe provide quantitative evidence: harm correlates with the cosine similarity of selected negatives ($r{=}0.71$), and the training loss for embedding-distance negatives (0.092) is substantially higher than for random (0.028), indicating the model fails to learn meaningful distinctions.\n\nAs an alternative, we explore \\emph{structure-grounded} negative mining.\nGiven a code repository with a formal structural graph (here, inter-procedural data-flow connectivity computed via CodeQL), we define a structure-grounded hard negative as:\n\\begin{equation}\n\\arg\\max_{x \\in D:\\, s(x,q) > \\tau \\,\\wedge\\, \\neg\\text{reach}_G(x,q)} s(x,q)\n\\label{eq:struct-neg}\n\\end{equation}\nwhere $D$ is the retrieval domain, $G$ the structural graph, $s$ a text similarity function, and $q$ the query.\nThis selects files that are textually similar to the query but structurally disconnected---a complementary signal dimension that embedding similarity cannot recover.\nCrucially, the structural graph is externally fixed and does not drift with encoder updates, unlike embedding-distance negatives that shift every training epoch.\n\nOur contributions are:\n\n\\begin{enumerate}\n\\item \\textbf{Cautionary finding}: Embedding-distance hard negatives significantly harm contrastive code retrieval ($-5.0$pp R@5 on SWE-bench Lite, $-2.6$pp on RepoBench-R), with harm driven by gradient redundancy (Section~\\ref{sec:main-results}, \\ref{sec:stratified}).\n\n\\item \\textbf{Safe alternative}: Data-flow-grounded negatives match random-negative performance without introducing the pathologies of embedding-distance selection, providing a viable drop-in replacement (Section~\\ref{sec:main-results}).\n\n\\item \\textbf{Scalability}: Scope-bounded inter-procedural data-flow analysis via CodeQL scales to 5,000 repositories with 7.8\\% overall timeout rate and 86\\% extraction success (Section~\\ref{sec:scalability}).\n\n\\item \\textbf{Ceiling analysis}: A failure taxonomy explains why structural signal does not help more: only 22\\% of retrieval failures are addressable by data-flow connectivity, bounding the achievable gain to $\\sim$3--4pp even with perfect structural signal (Section~\\ref{sec:ceiling}).\n\\end{enumerate}\n\n\\section{Related Work}\n\n\\paragraph{Hard negative mining in contrastive learning.}\nHard negative mining has a long history in metric learning \\cite{schroff2015facenet}.\nIn NLP, methods such as DPR \\cite{karpukhin2020dense} and ANCE \\cite{xiong2021approximate} use embedding-distance or in-batch negatives to improve dense retrieval.\nCoCoHaNeRe \\cite{shi2023cochanere} studies hard negatives for code search and finds that embedding-distance negatives can be redundant with the encoder's learned similarity---a finding our work extends with controlled experiments and a mechanistic explanation.\n\n\\paragraph{Code retrieval for software engineering.}\nSweRank \\cite{zhang2025swerank} trains a code retriever on large-scale SWE data.\nSWE-Fixer \\cite{xie2025swefixer} combines retrieval with LLM-based repair.\nLocAgent \\cite{muhammad2024locagent}, RANGER, and CodexGraph use structural information at inference time but not for training signal.\nARISE \\cite{wu2024arise} leverages intra-procedural data-flow but is limited to single-function scope.\nOur work is the first to use inter-procedural data-flow connectivity as a \\emph{training signal} for negative mining.\n\n\\paragraph{Structural analysis in code understanding.}\nCodeQL \\cite{codeql} provides a declarative framework for semantic code analysis.\nPrior work uses call graphs for bug detection and program understanding but not for contrastive learning data curation.\nWe show that 2-hop bounded CodeQL analysis provides a practical, model-independent method for computing structural connectivity at scale.\n\n\\section{Method}\n\\label{sec:method}\n\n\\subsection{Problem Setup}\n\nWe consider file-level code retrieval for repository-level bug repair.\nGiven a bug report (issue description and stack trace) as query $q$ and a repository with files $\\{f_1, \\ldots, f_n\\}$, the retriever ranks files by relevance.\nGold files are those modified in the ground-truth patch.\nWe train a bi-encoder retriever using InfoNCE contrastive loss with different negative mining strategies.\n\n\\subsection{Negative Mining Strategies}\n\nWe compare three strategies, holding all other variables constant (model architecture, training data, hyperparameters, positive examples):\n\n\\paragraph{Random negatives.} For each query, sample $k$ negatives uniformly at random from non-gold files in the same repository.\n\n\\paragraph{Embedding-distance negatives.} Encode all repository files with the current encoder checkpoint. Select the $k$ non-gold files with highest cosine similarity to the query embedding. Re-mine every epoch to track encoder updates.\n\n\\paragraph{Data-flow-aware negatives.} Using the structural graph $G$ from CodeQL, partition non-gold files into \\emph{connected} ($\\text{reach}_G(f, q^*)$ for any gold file $q^*$) and \\emph{disconnected}.\nSelect negatives that are textually similar (BM25 score $> \\tau$) but structurally disconnected (Eq.~\\ref{eq:struct-neg}).\nWhen fewer than $k$ candidates satisfy both criteria, backfill with random negatives.\n\n\\subsection{Structural Graph Construction}\n\nWe extract inter-procedural data-flow connectivity using CodeQL with 2-hop call-graph bounding.\nFor each instance, we:\n(1) create a CodeQL database from the repository snapshot,\n(2) run a custom QL query that computes 2-hop reachability from functions in gold files,\n(3) collect all files containing reachable functions as the \\emph{connected set}.\nFiles in the connected set but not in the gold set provide structure-grounded hard negative candidates (the ``connected$\\setminus$gold'' set).\n\nWe define $Z\\%$ as the fraction of instances where $|\\text{connected} \\setminus \\text{gold}| > 0$, measuring structural signal availability.\n\n\\subsection{Model and Training}\n\nWe fine-tune Qwen2.5-Coder-3B with LoRA adapters as a bi-encoder.\nTraining uses InfoNCE loss with temperature 0.05, batch size 32, learning rate 2e-5 with cosine schedule, for 3 epochs.\nEach strategy is trained on the same 5,000 SWE-smith instances with 3 random seeds (42, 123, 456).\n\n\\section{Experiments}\n\n\\subsection{CodeQL Extraction at Scale}\n\\label{sec:scalability}\n\nTable~\\ref{tab:codeql-scale} reports CodeQL extraction statistics at 5,000-repository scale compared to a 50-repository pilot.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Metric} & \\textbf{50-repo pilot} & \\textbf{5K full} \\\\\n\\midrule\n$Z\\%$ (connected$\\setminus$gold $> 0$) & 40.8\\% & 25.0\\% \\\\\nTimeout rate & 4.0\\% & 7.8\\% \\\\\nGold $\\in$ connected ratio & 100\\% & 72\\% \\\\\nMean extraction time (s) & 43.4 & 38.5 \\\\\nAvg $|$connected $\\setminus$ gold$|$ & 6.0 & 4.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{CodeQL extraction statistics. The pilot over-estimated $Z\\%$ due to curation bias toward medium-size repos with rich call graphs.}\n\\label{tab:codeql-scale}\n\\end{table}\n\n$Z\\%$ drops from 40.8\\% (pilot) to 25.0\\% (full scale) because the 5K corpus includes many small/script-style repositories lacking cross-file call chains.\nTable~\\ref{tab:codeql-strata} reveals a non-monotonic relationship with repository size: medium repositories (50--200 files) are the ``sweet spot'' with $Z\\%{=}38.9\\%$, while small repos lack call structure ($Z\\%{=}15.3\\%$) and large repos suffer from higher timeouts ($18.7\\%$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{\\# Inst.} & \\textbf{$Z\\%$} & \\textbf{Avg extra conn.} \\\\\n\\midrule\nSmall ($<$50 files) & 7,200 & 15.3\\% & 1.8 \\\\\nMedium (50--200) & 3,800 & 38.9\\% & 7.5 \\\\\nLarge ($>$200) & 1,800 & 29.1\\% & 6.0 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{$Z\\%$ by repository size stratum. Medium repositories provide the richest structural signal.}\n\\label{tab:codeql-strata}\n\\end{table}\n\nOverall timeout rate of 7.8\\% and extraction success of 86\\% demonstrate that scope-bounded CodeQL analysis is practical at scale.\nThe beniget fallback triggers for 14\\% of instances where CodeQL database creation fails (6.2\\%) or produces insufficient connected files.\n\n\\subsection{Main Results: Three-Strategy Comparison}\n\\label{sec:main-results}\n\nTable~\\ref{tab:main-results} presents retrieval performance on SWE-bench Lite (pool size 50) across three seeds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Strategy} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{Val Loss} \\\\\n\\midrule\nRandom & .542{\\scriptsize$\\pm$.018} & .810{\\scriptsize$\\pm$.012} & .921{\\scriptsize$\\pm$.008} & 0.028 \\\\\nDataFlow & .553{\\scriptsize$\\pm$.015} & .817{\\scriptsize$\\pm$.010} & .925{\\scriptsize$\\pm$.007} & 0.035 \\\\\nEmbDist & .489{\\scriptsize$\\pm$.020} & .760{\\scriptsize$\\pm$.012} & .878{\\scriptsize$\\pm$.011} & 0.092 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Retrieval performance by negative mining strategy (SWE-bench Lite, 3 seeds). EmbDist significantly underperforms Random.}\n\\label{tab:main-results}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Comparison} & \\textbf{$\\Delta$R@1} & \\textbf{$\\Delta$R@5} & \\textbf{$p$ (R@5)} \\\\\n\\midrule\nDataFlow $-$ Random & +1.1 & +0.7 & 0.42 \\\\\nEmbDist $-$ Random & $-$5.3 & $-$5.0 & 0.003 \\\\\nDataFlow $-$ EmbDist & +6.4 & +5.7 & 0.005 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Pairwise deltas (pp) with paired $t$-test $p$-values. Embedding-distance negatives significantly degrade performance.}\n\\label{tab:pairwise}\n\\end{table}\n\nThe results reveal an asymmetric pattern.\n\\textbf{Embedding-distance negatives significantly harm retrieval}: $-5.0$pp R@5 vs.\\ random ($p{=}0.003$), consistent across all three seeds.\nThe elevated validation loss (0.092 vs.\\ 0.028) indicates the model fails to learn useful distinctions from these negatives.\n\\textbf{Data-flow negatives match random performance}: $+0.7$pp R@5 ($p{=}0.42$), within seed variance.\nThis makes data-flow negatives a safe alternative that avoids embedding-distance pathologies without degrading performance.\n\n\\paragraph{Cross-benchmark validation.}\nTable~\\ref{tab:repobench} confirms these findings on RepoBench-R, a cross-file code completion benchmark.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Model} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{MRR} \\\\\n\\midrule\nStructFuse-Random & .385 & .618 & .742 & .483 \\\\\nStructFuse-DataFlow & .392 & .625 & .748 & .490 \\\\\nStructFuse-EmbDist & .360 & .592 & .718 & .461 \\\\\n\\midrule\nUniXcoder & .371 & .601 & .730 & .468 \\\\\nSweRank & .412 & .645 & .771 & .510 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{RepoBench-R retrieval results. The embedding-distance harm pattern replicates ($-2.6$pp R@5 vs.\\ Random). Gap to SweRank reflects training data scale (5K vs.\\ $>$100K).}\n\\label{tab:repobench}\n\\end{table}\n\nEmbedding-distance harm replicates on RepoBench-R ($-2.6$pp R@5), though attenuated due to smaller, more homogeneous candidate pools.\nThe gap to SweRank ($-2.0$pp R@5) reflects training data volume differences (5K vs.\\ $>$100K instances), not negative strategy.\n\n\\paragraph{End-to-end evaluation.}\nTable~\\ref{tab:e2e} reports SWE-bench Lite resolve rates using Qwen3.6-27B as the downstream agent.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Retriever} & \\textbf{Resolve (\\%)} & \\textbf{R@5} & \\textbf{Avg Tokens} \\\\\n\\midrule\nRandom & 28.3 & 0.805 & 12,200 \\\\\nDataFlow & 28.7 & 0.811 & 12,400 \\\\\nEmbDist & 27.8 & 0.758 & 12,600 \\\\\nBM25 only & 26.1 & 0.720 & 13,100 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{SWE-bench Lite end-to-end results. Retrieval differences are attenuated by the LLM agent's ability to compensate via tool calls. All trained retrievers improve over BM25-only.}\n\\label{tab:e2e}\n\\end{table}\n\nResolve rate differences are compressed to $<$1pp, as the LLM agent compensates for retrieval gaps through multi-turn code browsing.\nHowever, all trained retrievers show a consistent $+$2pp gain over BM25-only, validating the value of contrastive training itself.\n\n\\subsection{Why Embedding-Distance Negatives Hurt: Stratified Analysis}\n\\label{sec:stratified}\n\nTo understand the mechanism behind embedding-distance harm, we stratify results by repository characteristics and negative similarity.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Stratum} & \\textbf{$N$} & \\textbf{Emb R@5} & \\textbf{Rand R@5} & \\textbf{$\\Delta$ (pp)} \\\\\n\\midrule\nSmall ($<$50) & 3,200 & .782 & .803 & $-$2.1 \\\\\nMedium (50--200) & 1,900 & .698 & .766 & $-$6.8 \\\\\nLarge ($>$200) & 850 & .732 & .785 & $-$5.3 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Embedding-distance harm by repository size. Medium repos are the ``harm zone'' ($-6.8$pp).}\n\\label{tab:harm-strata}\n\\end{table}\n\nMedium-size repositories exhibit the greatest harm ($-6.8$pp), because they have enough similar files for embedding-distance mining to exploit, yet files share naming conventions that inflate surface similarity.\nSmall repos show muted harm ($-2.1$pp) because the candidate pool is too small for embedding-distance and random to diverge substantially.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Neg Similarity Quartile} & \\textbf{Mean cos sim} & \\textbf{$\\Delta$ R@5 (pp)} \\\\\n\\midrule\nQ4 (most similar) & 0.91 & $-$9.1 \\\\\nQ3 & 0.82 & $-$5.4 \\\\\nQ2 & 0.73 & $-$3.2 \\\\\nQ1 (least similar) & 0.61 & $-$1.5 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Harm as a function of negative embedding similarity. Pearson $r{=}0.71$ confirms gradient redundancy.}\n\\label{tab:harm-similarity}\n\\end{table}\n\nTable~\\ref{tab:harm-similarity} provides direct evidence for the gradient redundancy hypothesis.\nPerformance degradation scales monotonically with the cosine similarity of selected negatives ($r{=}0.71$).\nThe most similar negatives (Q4, mean similarity 0.91) cause $-9.1$pp harm, while the least similar (Q1, 0.61) cause only $-1.5$pp.\nThis suggests that embedding-distance mining concentrates the negative set in a region where the encoder already has strong opinions, yielding gradients that reinforce existing representations rather than teaching new distinctions.\n\n\\subsection{Ceiling Analysis: Why Doesn't Structural Signal Help More?}\n\\label{sec:ceiling}\n\nA natural question is why data-flow negatives do not \\emph{substantially outperform} random negatives.\nWe address this through a failure analysis of 50 instances where BM25/SweRank retrieval fails.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Failure Category} & \\textbf{$N$} & \\textbf{\\%} & \\textbf{DF Helps?} \\\\\n\\midrule\nLexical gap (no name overlap) & 18 & 36 & Sparse \\\\\nDataFlow reachable but missed & 11 & 22 & Yes \\\\\nLogic-only fix (no struct.\\ dep) & 9 & 18 & No \\\\\nMulti-file coordinated edit & 7 & 14 & Partial \\\\\nGold out of analysis scope & 5 & 10 & No \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Failure category breakdown ($N{=}50$). Only 22\\% of failures are directly addressable by structural signal.}\n\\label{tab:failure}\n\\end{table}\n\nThree factors bound the achievable gain from structural signal:\n\n\\paragraph{(1) Low signal density ($Z\\%{=}25\\%$).}\nOnly one quarter of training instances have connected-but-not-gold structural negatives.\nFor the remaining 75\\%, the data-flow miner falls back to BM25-hard or random padding, making its behavior approximate random.\n\n\\paragraph{(2) Limited addressable failures.}\nOnly 22\\% of retrieval failures involve gold files reachable via data-flow that text-based methods miss (Table~\\ref{tab:failure}).\nThe largest failure category (36\\%) is lexical gap---gold files with no naming overlap with the query---which structural connectivity also cannot bridge.\n\n\\paragraph{(3) Random negatives are already near-optimal at high pool diversity.}\nAt pool sizes $\\geq$50, approximately 15--20\\% of randomly sampled negatives happen to be BM25-similar, providing ``accidental hard negatives'' that narrow the margin for structured selection.\n\nCombining these factors, even with perfect structural signal, the ceiling improvement is approximately $32\\%$ of the current failure rate, yielding $\\sim$3--4pp maximum achievable gain.\nAt $Z\\%{=}25\\%$, the realized gain is further attenuated, explaining the observed $+0.7$pp.\n\n\\subsection{Ablation Studies}\n\n\\paragraph{Call-graph hop distance.}\nTable~\\ref{tab:hop} compares 1-hop, 2-hop, and 3-hop bounding for connected set computation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Hops} & \\textbf{$Z\\%$} & \\textbf{Avg $|$conn$|$} & \\textbf{Timeout \\%} & \\textbf{R@5} \\\\\n\\midrule\n1 & 12.1 & 2.3 & 2.1 & .808 \\\\\n2 & 25.0 & 4.2 & 7.8 & .817 \\\\\n3 & 41.5 & 12.8 & 22.3 & .811 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Hop distance ablation. 2-hop is Pareto-optimal: more signal than 1-hop without the noise and timeouts of 3-hop.}\n\\label{tab:hop}\n\\end{table}\n\n2-hop is Pareto-optimal: it provides sufficient $Z\\%$ (25\\%) with manageable timeouts (7.8\\%).\n3-hop increases $Z\\%$ to 41.5\\% but introduces noisy connections through shared utility functions, degrading R@5 to 0.811 while tripling the timeout rate.\n\n\\paragraph{Training data scale.}\nTable~\\ref{tab:scaling} shows performance scaling with training data size under the data-flow strategy.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Scale} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{R@10} & \\textbf{Time (h)} \\\\\n\\midrule\n1K & .510 & .785 & .905 & 0.7 \\\\\n3K & .541 & .808 & .918 & 2.0 \\\\\n5K & .553 & .817 & .925 & 3.2 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Training data scaling. Log-linear fit $R^2{=}0.96$; diminishing returns suggest 5K is near-saturated for this model capacity.}\n\\label{tab:scaling}\n\\end{table}\n\nPerformance follows a log-linear scaling law ($R^2{=}0.96$), with diminishing returns from 3K to 5K ($+0.9$pp vs.\\ $+2.3$pp from 1K to 3K).\nExtrapolation suggests $\\sim$10K instances would yield only $\\sim$$+0.5$pp additional gain, indicating that negative strategy comparisons at 5K reflect stable relative rankings.\n\n\\paragraph{Fusion head.}\nTable~\\ref{tab:fusion} ablates inference-time structural features.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lccc}\n\\toprule\n\\textbf{Configuration} & \\textbf{R@1} & \\textbf{R@5} & \\textbf{MRR} \\\\\n\\midrule\nEmbedding-only & .553 & .817 & .652 \\\\\nStructural-only & .398 & .628 & .485 \\\\\nCombined (MLP) & .558 & .822 & .658 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Fusion head ablation. Structural features add only $+0.5$pp at inference time, confirming that structure helps training, not inference.}\n\\label{tab:fusion}\n\\end{table}\n\nThe combined fusion head adds only $+0.5$pp over embedding-only, confirming that the value of structural information lies in training data curation (negative mining), not inference-time features.\nThis simplifies deployment: the retriever is a standard bi-encoder at inference time with no CodeQL dependency.\n\n\\paragraph{Distance weighting.}\nBinary connected/disconnected labeling ($R@5{=}0.815$) performs comparably to exponential distance weighting ($R@5{=}0.817$ at $\\alpha{=}1.0$, $\\Delta{=}+0.2$pp).\nSince most instances have sparse connectivity (avg.\\ 4.2 connected files), continuous weighting adds negligible information.\nWe adopt binary classification for simplicity.\n\n\\section{Discussion}\n\n\\paragraph{Implications for practitioners.}\nOur results suggest that the common practice of using embedding-distance hard negatives for code retrieval should be reconsidered, particularly for medium-size repositories (50--200 files) where harm is most pronounced ($-6.8$pp).\nRandom negatives are a surprisingly strong baseline, and structure-grounded negatives offer a safe alternative without the gradient redundancy risk.\n\n\\paragraph{Why not stronger gains from structure?}\nThe ceiling analysis identifies three bottlenecks: (1) $Z\\%{=}25\\%$ means structural signal is sparse across the training set, (2) the majority of retrieval failures (lexical gap, logic-only) are not addressable by structural connectivity, and (3) random negatives at high pool diversity already provide near-sufficient contrastive signal.\nImproving $Z\\%$ through richer static analysis (e.g., type-based connectivity, import graph augmentation) or targeting medium-size repos where $Z\\%{=}38.9\\%$ are promising directions.\n\n\\paragraph{Generalizability.}\nThe gradient redundancy phenomenon is not specific to code.\nAny domain where embedding-distance mining selects negatives that overlap with the encoder's learned similarity is susceptible.\nStructure-grounded negative mining generalizes to domains with external structural knowledge: molecular interaction networks for drug discovery, circuit topology for hardware retrieval, and knowledge graph connectivity for entity linking.\nCode is an ideal testbed due to the formal semantic guarantees of static analysis.\n\n\\paragraph{Limitations.}\n(1)~We evaluate a single encoder architecture (Qwen2.5-Coder-3B); the magnitude of embedding-distance harm may vary with model capacity.\n(2)~CodeQL extraction is limited to Python repositories; languages with richer type systems may yield higher $Z\\%$ and stronger structural signal.\n(3)~The ceiling analysis is based on 50 manually annotated instances; a larger study could refine the category proportions.\n(4)~End-to-end resolve rates show $<$1pp differences, meaning the retrieval findings have limited downstream impact in the presence of a capable LLM agent.\n\n\\section{Conclusion}\n\nWe present a cautionary result for the contrastive code retrieval community: embedding-distance hard negatives, the most popular mining strategy, significantly degrade retrieval quality compared to random negatives.\nThe mechanism---gradient redundancy from selecting negatives already close in embedding space---is quantitatively confirmed by a strong correlation ($r{=}0.71$) between negative similarity and performance harm.\nStructure-grounded negatives using inter-procedural data-flow connectivity offer a safe alternative that matches random-negative performance while avoiding embedding-distance pathologies.\nA ceiling analysis explains the modest gains and provides actionable hypotheses for future work: increasing structural signal density, enriching connectivity with type information, and focusing on medium-size repositories where structural signal is richest.\n\n\\bibliography{paper}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}\n\n\\bibitem[Guo et~al.(2022)]{guo2022unixcoder}\nDaya Guo, Shuai Lu, Nan Duan, Yanlin Wang, Ming Zhou, and Jian Yin.\n\\newblock UniXcoder: Unified cross-modal pre-training for code representation.\n\\newblock In \\emph{ACL}, 2022.\n\n\\bibitem[Jimenez et~al.(2024)]{jimenez2024swebench}\nCarlos~E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik Narasimhan.\n\\newblock {SWE}-bench: Can language models resolve real-world {GitHub} issues?\n\\newblock In \\emph{ICLR}, 2024.\n\n\\bibitem[Schroff et~al.(2015)]{schroff2015facenet}\nFlorian Schroff, Dmitry Kalenichenko, and James Philbin.\n\\newblock FaceNet: A unified embedding for face recognition and clustering.\n\\newblock In \\emph{CVPR}, 2015.\n\n\\bibitem[Karpukhin et~al.(2020)]{karpukhin2020dense}\nVladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and Wen-tau Yih.\n\\newblock Dense passage retrieval for open-domain question answering.\n\\newblock In \\emph{EMNLP}, 2020.\n\n\\bibitem[Xiong et~al.(2021)]{xiong2021approximate}\nLee Xiong, Chenyan Xiong, Ye~Li, Kwok-Fung Tang, Jialin Liu, Paul~N. Bennett, Junaid Ahmed, and Arnold Overwijk.\n\\newblock Approximate nearest neighbor negative contrastive learning for dense text retrieval.\n\\newblock In \\emph{ICLR}, 2021.\n\n\\bibitem[Shi et~al.(2023)]{shi2023cochanere}\nJian Shi, Daya Guo, Shuai Lu, and Duyu Tang.\n\\newblock CoCoHaNeRe: Contrastive code hard negative retrieval.\n\\newblock \\emph{arXiv preprint arXiv:2305.XXXXX}, 2023.\n\n\\bibitem[Zhang et~al.(2025)]{zhang2025swerank}\nFan Zhang et~al.\n\\newblock SweRank: Training code retrievers for software engineering tasks.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Xie et~al.(2025)]{xie2025swefixer}\nYuntao Xie et~al.\n\\newblock SWE-Fixer: Training open-source LLMs for effective and efficient GitHub issue resolution.\n\\newblock \\emph{arXiv preprint}, 2025.\n\n\\bibitem[Muhammad et~al.(2024)]{muhammad2024locagent}\nAli Muhammad et~al.\n\\newblock LocAgent: Graph-guided LLM agents for code localization.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[Wu et~al.(2024)]{wu2024arise}\nSiru Wu et~al.\n\\newblock ARISE: Automated runtime information-guided SE.\n\\newblock \\emph{arXiv preprint}, 2024.\n\n\\bibitem[{CodeQL}(2024)]{codeql}\n{GitHub}.\n\\newblock {CodeQL} documentation.\n\\newblock \\url{https://codeql.github.com/docs/}, 2024.\n\n\\end{thebibliography}\n\n\\end{document}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  },
  "sourceToolAssistantUUID": "388485ff-9bf5-490c-83a6-bd56208bccb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-i…",
  "leafUuid": "7924fbcd-63e1-46f1-bac9-791d90172577",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate StructFuse median-tier simulation paper",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc"
}
```

---

### Tool call

_source line 23 · 2026-05-12T21:04:43.225Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01PD6JwpAvvfRZ7D6nryqzhT`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median && pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -30",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7924fbcd-63e1-46f1-bac9-791d90172577",
  "isSidechain": false,
  "requestId": "req_011CayMTWXJgPtrd8QjpaBjn",
  "type": "assistant",
  "uuid": "a853caec-ccff-40be-ad6a-cd4993ffb4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UkAo8itY1WZKU1AFiGt5F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9150,
      "cache_read_input_tokens": 37817,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9150,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 37817,
          "cache_creation_input_tokens": 9150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9150
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

_source line 24 · 2026-05-12T21:04:43.376Z_

<details><summary>↩ Tool result · `toolu_01PD6JwpAvvfRZ7D6nryqzhT`</summary>

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

! LaTeX Error: File `acl.sty' not found.

Type X to quit or &lt;RETURN> to proceed,
or enter new name. (Default extension: sty)

Enter file name: 
! Emergency stop.
&lt;read *> 
         
l.3 \usepackage
               {times}^^M
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a853caec-ccff-40be-ad6a-cd4993ffb4b3",
  "isSidechain": false,
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "2ecadfc6-e5fb-4204-8629-e49357321bc6",
  "toolUseResult": {
    "stdout": "This is pdfTeX, Version 3.141592653-2.6-1.40.28 (TeX Live 2025/Debian) (preloaded format=pdflatex)\n restricted \\write18 enabled.\nentering extended mode\n(./paper.tex\nLaTeX2e <2025-11-01>\nL3 programming layer <2026-01-19>\n(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls\nDocument Class: article 2025/01/22 v1.4n Standard LaTeX document class\n(/usr/share/texlive/texmf-dist/tex/latex/base/size11.clo))\n\n! LaTeX Error: File `acl.sty' not found.\n\nType X to quit or &lt;RETURN> to proceed,\nor enter new name. (Default extension: sty)\n\nEnter file name: \n! Emergency stop.\n&lt;read *> \n         \nl.3 \\usepackage\n               {times}^^M\n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "a853caec-ccff-40be-ad6a-cd4993ffb4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-12T21:04:46.951Z_

<details><summary>Logged reasoning block</summary>

```text
ACL style file not found. Let me switch to a simpler document class that's available, or find if there's an ACL style file available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ecadfc6-e5fb-4204-8629-e49357321bc6",
  "isSidechain": false,
  "requestId": "req_011CayMToEdyPUa22shGWxu6",
  "type": "assistant",
  "uuid": "96f9fa47-3a2c-4848-9acc-6cc790135463",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EauHSfP7NHciiWWi88ZJQh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 441,
      "cache_read_input_tokens": 46967,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 46967,
          "cache_creation_input_tokens": 441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 441
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

_source line 26 · 2026-05-12T21:04:47.481Z_

ACL style not available. Let me switch to a standard article class with similar formatting.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96f9fa47-3a2c-4848-9acc-6cc790135463",
  "isSidechain": false,
  "requestId": "req_011CayMToEdyPUa22shGWxu6",
  "type": "assistant",
  "uuid": "8d5c967f-f3b9-4814-8f73-97cf2189d37b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EauHSfP7NHciiWWi88ZJQh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 441,
      "cache_read_input_tokens": 46967,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 46967,
          "cache_creation_input_tokens": 441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 441
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

_source line 27 · 2026-05-12T21:04:51.123Z_

<details open><summary>🔧 Tool call — Edit · `toolu_012z9j2yG9voshddz3ucSco5`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex",
  "old_string": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\aclfinalcopy",
  "new_string": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{natbib}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d5c967f-f3b9-4814-8f73-97cf2189d37b",
  "isSidechain": false,
  "requestId": "req_011CayMToEdyPUa22shGWxu6",
  "type": "assistant",
  "uuid": "86d3437b-267c-4fa5-87bd-3136b3614017",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EauHSfP7NHciiWWi88ZJQh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 441,
      "cache_read_input_tokens": 46967,
      "output_tokens": 462,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 441,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 462,
          "cache_read_input_tokens": 46967,
          "cache_creation_input_tokens": 441,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 441
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

_source line 28 · 2026-05-12T21:04:51.147Z_

<details><summary>↩ Tool result · `toolu_012z9j2yG9voshddz3ucSco5`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86d3437b-267c-4fa5-87bd-3136b3614017",
  "isSidechain": false,
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "ce7ff0f5-17ce-4b1e-a572-a85004ae3b3f",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex",
    "oldString": "\\documentclass[11pt]{article}\n\\usepackage[hyperref]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\n\\aclfinalcopy",
    "newString": "\\documentclass[11pt,a4paper]{article}\n\\usepackage[margin=1in]{geometry}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{booktabs}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{url}\n\\usepackage{natbib}\n\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 5,
        "newStart": 1,
        "newLines": 5,
        "lines": [
          "-\\documentclass[11pt]{article}",
          "-\\usepackage[hyperref]{acl}",
          "+\\documentclass[11pt,a4paper]{article}",
          "+\\usepackage[margin=1in]{geometry}",
          " \\usepackage{times}",
          " \\usepackage{latexsym}",
          " \\usepackage{graphicx}"
        ]
      },
      {
        "oldStart": 9,
        "oldLines": 9,
        "newStart": 9,
        "newLines": 9,
        "lines": [
          " \\usepackage{multirow}",
          " \\usepackage{xcolor}",
          " \\usepackage{url}",
          "+\\usepackage{natbib}",
          "+\\usepackage[colorlinks=true,citecolor=blue,urlcolor=blue]{hyperref}",
          " ",
          "-\\aclfinalcopy",
          "-",
          " \\title{When Hard Negatives Hurt: Embedding-Distance Negative Mining\\\\Degrades Contrastive Code Retrieval}",
          " ",
          " \\author{Anonymous}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "86d3437b-267c-4fa5-87bd-3136b3614017",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-12T21:04:54.140Z_

Also need to fix the bibliography section since we're using inline thebibliography now, and remove the `\bibliography{paper}` line.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce7ff0f5-17ce-4b1e-a572-a85004ae3b3f",
  "isSidechain": false,
  "requestId": "req_011CayMUNVPYbMS5dasHLs9q",
  "type": "assistant",
  "uuid": "63ace0ed-b581-4d6d-9bb3-8cdd1fe2cc75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDSLy2mxWmXaibidcaizk1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 47408,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 547,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 47408,
          "cache_creation_input_tokens": 547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 547
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

_source line 30 · 2026-05-12T21:04:55.460Z_

<details open><summary>🔧 Tool call — Edit · `toolu_01CCqw5V6hDeT3bAA4bJ3fHk`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex",
  "old_string": "\\bibliography{paper}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}",
  "new_string": "\\begin{thebibliography}{20}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63ace0ed-b581-4d6d-9bb3-8cdd1fe2cc75",
  "isSidechain": false,
  "requestId": "req_011CayMUNVPYbMS5dasHLs9q",
  "type": "assistant",
  "uuid": "b92fa0fa-25da-402d-83d2-96df9e3b2057",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PDSLy2mxWmXaibidcaizk1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 47408,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 547,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 47408,
          "cache_creation_input_tokens": 547,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 547
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

_source line 31 · 2026-05-12T21:04:55.471Z_

<details><summary>↩ Tool result · `toolu_01CCqw5V6hDeT3bAA4bJ3fHk`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b92fa0fa-25da-402d-83d2-96df9e3b2057",
  "isSidechain": false,
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "e79b686d-58ef-4185-a957-ddab677574c6",
  "toolUseResult": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median/paper.tex",
    "oldString": "\\bibliography{paper}\n\\bibliographystyle{acl_natbib}\n\n\\begin{thebibliography}{20}",
    "newString": "\\begin{thebibliography}{20}",
    "originalFile": null,
    "structuredPatch": [
      {
        "oldStart": 454,
        "oldLines": 9,
        "newStart": 454,
        "newLines": 6,
        "lines": [
          " Structure-grounded negatives using inter-procedural data-flow connectivity offer a safe alternative that matches random-negative performance while avoiding embedding-distance pathologies.",
          " A ceiling analysis explains the modest gains and provides actionable hypotheses for future work: increasing structural signal density, enriching connectivity with type information, and focusing on medium-size repositories where structural signal is richest.",
          " ",
          "-\\bibliography{paper}",
          "-\\bibliographystyle{acl_natbib}",
          "-",
          " \\begin{thebibliography}{20}",
          " ",
          " \\bibitem[Guo et~al.(2022)]{guo2022unixcoder}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  },
  "sourceToolAssistantUUID": "b92fa0fa-25da-402d-83d2-96df9e3b2057",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-12T21:04:55.478Z_

```json
{
  "parentUuid": "e79b686d-58ef-4185-a957-ddab677574c6",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f79feba3-275c-451b-9415-69f56406e91a",
  "timestamp": "2026-05-12T21:04:55.478Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-12T21:04:58.976Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Wj7yosMmvcAm9xsvhRNsfs`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -20",
  "description": "First pdflatex pass",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f79feba3-275c-451b-9415-69f56406e91a",
  "isSidechain": false,
  "requestId": "req_011CayMUgyNuryZPMvAvjQAP",
  "type": "assistant",
  "uuid": "089a77ba-11b9-4ee4-b854-72b1d12bc3eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hi8v1DbWS255xKwqB4vb14",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 397,
      "cache_read_input_tokens": 47955,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 397,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 47955,
          "cache_creation_input_tokens": 397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 397
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

_source line 34 · 2026-05-12T21:04:59.509Z_

<details><summary>↩ Tool result · `toolu_01Wj7yosMmvcAm9xsvhRNsfs`</summary>

```text
Package rerunfilecheck Warning: File `paper.out' has changed.
(rerunfilecheck)                Rerun to get outlines right
(rerunfilecheck)                or use package `bookmark'.

 )
(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo
nts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ
e1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ
ic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf
onts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.
pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 159546 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "089a77ba-11b9-4ee4-b854-72b1d12bc3eb",
  "isSidechain": false,
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "eb9a099a-08cf-4f6f-93df-f8d07b9b3d99",
  "toolUseResult": {
    "stdout": "Package rerunfilecheck Warning: File `paper.out' has changed.\n(rerunfilecheck)                Rerun to get outlines right\n(rerunfilecheck)                or use package `bookmark'.\n\n )\n(see the transcript file for additional information)&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fo\nnts/type1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/typ\ne1/public/amsfonts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publ\nic/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsf\nonts/cm/cmr8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.\npfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 159546 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "089a77ba-11b9-4ee4-b854-72b1d12bc3eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-12T21:05:03.141Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015grgt6aMJKX9zegACt9KMm`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode paper.tex 2>&1 | tail -5",
  "description": "Second pdflatex pass for cross-references",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb9a099a-08cf-4f6f-93df-f8d07b9b3d99",
  "isSidechain": false,
  "requestId": "req_011CayMUzDTgLFmEAU8eHrrr",
  "type": "assistant",
  "uuid": "de6c946a-ef95-4e56-b651-546bd2527b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DK4A1A6JdzXyYnpxLUuwW6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 48352,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 164,
          "cache_read_input_tokens": 48352,
          "cache_creation_input_tokens": 607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 607
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

_source line 36 · 2026-05-12T21:05:03.655Z_

<details><summary>↩ Tool result · `toolu_015grgt6aMJKX9zegACt9KMm`</summary>

```text
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on paper.pdf (9 pages, 162755 bytes).
Transcript written on paper.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de6c946a-ef95-4e56-b651-546bd2527b88",
  "isSidechain": false,
  "promptId": "3b7cd649-f6a3-4635-aa8d-8f0beb25204b",
  "type": "user",
  "uuid": "8c2f19c6-57b0-46b0-b2b3-dd3dc252127a",
  "toolUseResult": {
    "stdout": "re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on paper.pdf (9 pages, 162755 bytes).\nTranscript written on paper.log.",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "de6c946a-ef95-4e56-b651-546bd2527b88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-12T21:05:15.118Z_

编译成功，生成 9 页 PDF。

论文已写入 `artifacts/dream_reports/dream_20260512T204322/median/paper.tex` 并编译为 `paper.pdf`。

核心叙事按指导做了 pivot：
- **Headline claim**: Embedding-distance negatives 显著有害（$-5.0$pp R@5, $p=0.003$），通过梯度冗余机制解释（$r=0.71$），分层分析（按 repo size、negative similarity quartile）作为主要证据
- **Claim 1 降级**: Dataflow negatives 是安全替代方案（$+0.7$pp, $p=0.42$，与 random 无显著差异）
- **Claim 3 保留**: CodeQL 可扩展性（5K repos, 7.8% timeout）
- **Ceiling analysis**: 50 个 failure case 分析解释为什么结构信号帮助有限（仅 22% 可寻址，$Z\%=25\%$ 信号稀疏，random 已近最优）
- **标题**: "When Hard Negatives Hurt" 角度

所有定量数字均来自 `experiment_data.json`，无编造。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c2f19c6-57b0-46b0-b2b3-dd3dc252127a",
  "isSidechain": false,
  "requestId": "req_011CayMVHy3zDdh83JTD9YZx",
  "type": "assistant",
  "uuid": "0e351052-f63f-415e-a393-99b7e9fd7368",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-ie/artifacts/dream_reports/dream_20260512T204322/median",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016aRyafLDeP2e2NKTNcBsfp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 256,
      "cache_read_input_tokens": 48959,
      "output_tokens": 342,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 256,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 342,
          "cache_read_input_tokens": 48959,
          "cache_creation_input_tokens": 256,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 256
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是 Paper Agent（Dream 模式）。任务：为 dream_id=dream_20260512T204322 tier=median 生成一篇完整的模拟论文。  ## 关键规则 1. 用 **Write 工具** 把 LaTeX 源码写入 `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/faith-evidence-i…",
  "leafUuid": "0e351052-f63f-415e-a393-99b7e9fd7368",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Generate StructFuse median-tier simulation paper",
  "sessionId": "c30881e3-a41d-414e-9322-79161ab758fc"
}
```

---
