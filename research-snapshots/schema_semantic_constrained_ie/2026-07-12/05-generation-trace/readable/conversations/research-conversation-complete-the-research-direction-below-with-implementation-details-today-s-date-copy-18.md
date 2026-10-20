# Research conversation: Complete the research direction below with implementation details. **Today's date: 2026-05-10 (UTC).** Only recommend ve

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-2/8e0ca466-e6f5-4ca9-bbc8-00d0ff299919.jsonl`
- **Structured JSON:** [`67c4be54e3d34265e86a.json`](../../sessions/67/67c4be54e3d34265e86a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T06:56:18.788Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T06:56:18.788Z",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "content": "Complete the research direction below with implementation details.\n\n**Today's date: 2026-05-10 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.\n\n{\n  \"title\": \"Online Schema Adaptation via Extraction-Error Feedback Loops\",\n  \"core_problem\": \"Schema-guided IE models (GoLLIE, KnowCoder, GuideX) fix the extraction schema at training or deployment time. When a new domain has a schema that partially conflicts with training-time guidelines — e.g., a medical ontology where 'Treatment' subsumes what the model learned as 'Drug' and 'Procedure' — models fail silently with no mechanism to refine their operational schema. How can IE models detect and recover from schema-domain mismatches at test time?\",\n  \"opportunity\": \"PARSE (arXiv 2510.08623, 2025) demonstrates that automatic schema optimization improves extraction accuracy by 64.7% on SWDE — but it requires offline synthetic data generation per domain. GuideX (ACL Findings 2025) shows that auto-generated guidelines improve zero-shot NER by 7 F1 points — but schemas are fixed at fine-tuning time. The gap is *online* adaptation: using the model's own extraction inconsistencies (type violations, missing mandatory arguments, cross-sentence entity type contradictions) as a feedback signal to iteratively refine schema descriptions during test-time deployment. This aligns with the emerging 'LLM as schema optimizer' paradigm but closes the loop by making feedback domain-specific and error-driven rather than relying on synthetic data generation.\",\n  \"landscape\": \"GoLLIE (arXiv 2310.03668, 2023) shows annotation guidelines improve zero-shot IE but requires guidelines to be written manually. GuideX (ACL 2025) automates guideline generation using LLMs and achieves SOTA across 7 zero-shot NER benchmarks but cannot adapt post-deployment. PARSE (2025) optimizes schemas via iterative refinement on synthetic data with 10% combined improvement on three datasets but is fundamentally offline — it assumes stable schemas and requires seed data per domain. The open problem is the zero-seed online setting: a model deployed on a new domain should be able to detect its own schema-domain mismatches (e.g., consistently extracting 'ORGANIZATION' where gold expects 'FACILITY') from extraction pattern violations and propose targeted schema corrections without any human labels or domain-specific synthetic data.\"\n}\n\nADD these fields (keep all existing fields):\n{\n  \"approach\": \"Proposed method or research direction — what you would actually do (3-5 sentences)\",\n  \"resource_estimate\": {\n      \"manual\": {\n          \"gpu_hours\": \"e.g. ~200h A100\",\n          \"gpu_utilization\": \"describe GPU idle rate (human waits cause high idle)\",\n          \"timeline\": \"e.g. 3-6 months\",\n          \"team\": \"e.g. 1-2 researchers\",\n          \"estimated_gpu_cost\": \"GPU rental cost only (do NOT include salary)\"\n      },\n      \"human_in_loop\": {\n          \"gpu_hours\": \"e.g. ~300h A100\",\n          \"gpu_utilization\": \"describe GPU utilization improvement vs manual\",\n          \"timeline\": \"e.g. 1-2 months\",\n          \"team\": \"e.g. 1 researcher, ~30min/day check-in (do NOT include salary)\",\n          \"claude_api_cost\": \"e.g. $100-300\",\n          \"estimated_gpu_cost\": \"GPU rental cost\",\n          \"risk_note\": \"Key bottleneck or risk\"\n      },\n      \"auto_research\": {\n          \"gpu_hours\": \"e.g. ~500h A100 (more exploration, but near-zero idle)\",\n          \"gpu_utilization\": \"describe why GPU idle rate is minimal\",\n          \"timeline\": \"e.g. days to 2 weeks if resources are sufficient\",\n          \"team\": \"0 (only initial setup)\",\n          \"claude_api_cost\": \"e.g. $200-500\",\n          \"estimated_gpu_cost\": \"GPU rental cost\",\n          \"speed_bottleneck\": \"what limits speed (GPU count, API key quota, etc.)\",\n          \"risk_note\": \"Key risk factor\"\n      }\n  },\n  \"target_venues\": [\"Only list venues with deadlines after 2026-05-10, e.g. NeurIPS 2026\"],\n  \"level\": \"top-tier | solid | incremental\",\n  \"key_references\": [\"Paper title (VENUE YEAR)\", ...],\n  \"description\": \"Executive summary combining all above into 150-200 words\",\n  \"project_name\": \"snake_case_identifier (valid Python id, max 30 chars)\",\n  \"source\": \"web_research\"\n}\n\nFor key_references, verify with WebSearch that cited paper titles and venues are real. Drop any reference you cannot verify.\n\n**Model freshness rule**: When the approach involves pretrained models (LLM, vision model, etc.), use WebSearch to find the current top-performing open-source models for the task (e.g., search \"best open source LLM 2026\", \"SOTA open source language model\"). Use models that represent the current frontier — do NOT default to models from your training data. Entire model families may be outdated (e.g., LLaMA), not just version numbers. Exception: skip this if the idea specifically requires older models (reproduction, model evolution analysis, backward compatibility) or the user explicitly specified a model in the seed topic.\n\n## 竞争论文 & Concurrent Work 搜索\n\n在设计 approach 之前，必须确认没有人正在做同样的事情：\n- 搜索 `{core_problem} 2026` 和 `{approach_keyword} {task} 2026`\n- 在 arXiv 上搜索过去 3 个月的相关提交\n- 在 OpenReview 上搜索即将举行的会议（ICML, NeurIPS, ICLR）的提交\n- 如果发现高度相似的 concurrent work，必须在 landscape 中明确提及，并在 approach 中说明与之的差异化\n\n## 非常仔细地思考和验证\n\n在设计具体 approach 时，你必须深入思考并充分调研：\n\n1. **可行性验证**（不是猜测，而是基于证据）：\n   - 搜索类似方法的已有实现（检查 GitHub）\n   - 查找需要打败的具体 baseline 数字\n   - 了解类似实验的硬件/数据需求\n   - 查找相关工作中已识别的潜在失败模式\n\n2. **成本估算必须基于真实数据**：\n   - 找到类似实验的实际成本（不是拍脑袋）\n   - 考虑不同研究模式下的成本差异\n\n3. **内部一致性自查**：\n   - approach 是否直接解决 Round 1 识别的 core_problem？\n   - resource estimate 与 approach 复杂度是否匹配？\n   - target venues 与贡献级别是否相称？\n\nFor feasibility grounding:\n- Search \"github.com {method_name} {task}\" to check if building blocks or reference implementations exist.\n  If nothing similar exists, your timeline estimate should be longer.\n- Search \"huggingface.co/datasets {dataset_name}\" or \"paperswithcode.com {task} datasets\" to verify\n  that required datasets are actually accessible. If the dataset is proprietary or hard to obtain, flag it.\n\nWhen estimating costs for the three research modes (ordered from most to least human involvement):\n\n1. **Manual (纯人工)**: Human writes code, designs experiments, analyzes results. GPU idle rate is HIGH because GPU waits for humans. Do NOT include salary — only estimate GPU cost.\n\n2. **Human-in-Loop (人机协作)**: Agent executes, human approves key decisions. GPU utilization is moderate. Do NOT include salary — only estimate GPU cost + API cost. Team field describes required check-in frequency.\n\n3. **Auto Research (全自动)**: Agent runs 24/7, explores more experiments but GPU idle rate is near ZERO. Speed bottleneck is GPU count and API key quota — with sufficient resources, a paper can be completed in DAYS. Only estimate GPU cost + API cost. Do NOT factor in agent operational overhead.\n\nKey principles:\n- Auto Research uses MORE total GPU hours but has MUCH LOWER GPU idle rate\n- Claude API cost: ~$0.05-0.15 per conversation turn (Opus), estimate total turns needed\n- Auto mode typically runs 3-5x more experiments than manual (exploration + failed attempts)\n- Human-in-Loop reduces auto mode waste by ~40-60% through approval gates\n\nOutput ONLY a single JSON object with ALL fields merged. No markdown fences."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T06:56:18.792Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T06:56:18.792Z",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---

## Round 1

23 recorded events

### User

_source line 3 · 2026-05-10T06:56:18.818Z_

Complete the research direction below with implementation details.

**Today's date: 2026-05-10 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.

{
  "title": "Online Schema Adaptation via Extraction-Error Feedback Loops",
  "core_problem": "Schema-guided IE models (GoLLIE, KnowCoder, GuideX) fix the extraction schema at training or deployment time. When a new domain has a schema that partially conflicts with training-time guidelines — e.g., a medical ontology where 'Treatment' subsumes what the model learned as 'Drug' and 'Procedure' — models fail silently with no mechanism to refine their operational schema. How can IE models detect and recover from schema-domain mismatches at test time?",
  "opportunity": "PARSE (arXiv 2510.08623, 2025) demonstrates that automatic schema optimization improves extraction accuracy by 64.7% on SWDE — but it requires offline synthetic data generation per domain. GuideX (ACL Findings 2025) shows that auto-generated guidelines improve zero-shot NER by 7 F1 points — but schemas are fixed at fine-tuning time. The gap is *online* adaptation: using the model's own extraction inconsistencies (type violations, missing mandatory arguments, cross-sentence entity type contradictions) as a feedback signal to iteratively refine schema descriptions during test-time deployment. This aligns with the emerging 'LLM as schema optimizer' paradigm but closes the loop by making feedback domain-specific and error-driven rather than relying on synthetic data generation.",
  "landscape": "GoLLIE (arXiv 2310.03668, 2023) shows annotation guidelines improve zero-shot IE but requires guidelines to be written manually. GuideX (ACL 2025) automates guideline generation using LLMs and achieves SOTA across 7 zero-shot NER benchmarks but cannot adapt post-deployment. PARSE (2025) optimizes schemas via iterative refinement on synthetic data with 10% combined improvement on three datasets but is fundamentally offline — it assumes stable schemas and requires seed data per domain. The open problem is the zero-seed online setting: a model deployed on a new domain should be able to detect its own schema-domain mismatches (e.g., consistently extracting 'ORGANIZATION' where gold expects 'FACILITY') from extraction pattern violations and propose targeted schema corrections without any human labels or domain-specific synthetic data."
}

ADD these fields (keep all existing fields):
{
  "approach": "Proposed method or research direction — what you would actually do (3-5 sentences)",
  "resource_estimate": {
      "manual": {
          "gpu_hours": "e.g. ~200h A100",
          "gpu_utilization": "describe GPU idle rate (human waits cause high idle)",
          "timeline": "e.g. 3-6 months",
          "team": "e.g. 1-2 researchers",
          "estimated_gpu_cost": "GPU rental cost only (do NOT include salary)"
      },
      "human_in_loop": {
          "gpu_hours": "e.g. ~300h A100",
          "gpu_utilization": "describe GPU utilization improvement vs manual",
          "timeline": "e.g. 1-2 months",
          "team": "e.g. 1 researcher, ~30min/day check-in (do NOT include salary)",
          "claude_api_cost": "e.g. $100-300",
          "estimated_gpu_cost": "GPU rental cost",
          "risk_note": "Key bottleneck or risk"
      },
      "auto_research": {
          "gpu_hours": "e.g. ~500h A100 (more exploration, but near-zero idle)",
          "gpu_utilization": "describe why GPU idle rate is minimal",
          "timeline": "e.g. days to 2 weeks if resources are sufficient",
          "team": "0 (only initial setup)",
          "claude_api_cost": "e.g. $200-500",
          "estimated_gpu_cost": "GPU rental cost",
          "speed_bottleneck": "what limits speed (GPU count, API key quota, etc.)",
          "risk_note": "Key risk factor"
      }
  },
  "target_venues": ["Only list venues with deadlines after 2026-05-10, e.g. NeurIPS 2026"],
  "level": "top-tier | solid | incremental",
  "key_references": ["Paper title (VENUE YEAR)", ...],
  "description": "Executive summary combining all above into 150-200 words",
  "project_name": "snake_case_identifier (valid Python id, max 30 chars)",
  "source": "web_research"
}

For key_references, verify with WebSearch that cited paper titles and venues are real. Drop any reference you cannot verify.

**Model freshness rule**: When the approach involves pretrained models (LLM, vision model, etc.), use WebSearch to find the current top-performing open-source models for the task (e.g., search "best open source LLM 2026", "SOTA open source language model"). Use models that represent the current frontier — do NOT default to models from your training data. Entire model families may be outdated (e.g., LLaMA), not just version numbers. Exception: skip this if the idea specifically requires older models (reproduction, model evolution analysis, backward compatibility) or the user explicitly specified a model in the seed topic.

## 竞争论文 & Concurrent Work 搜索

在设计 approach 之前，必须确认没有人正在做同样的事情：
- 搜索 `{core_problem} 2026` 和 `{approach_keyword} {task} 2026`
- 在 arXiv 上搜索过去 3 个月的相关提交
- 在 OpenReview 上搜索即将举行的会议（ICML, NeurIPS, ICLR）的提交
- 如果发现高度相似的 concurrent work，必须在 landscape 中明确提及，并在 approach 中说明与之的差异化

## 非常仔细地思考和验证

在设计具体 approach 时，你必须深入思考并充分调研：

1. **可行性验证**（不是猜测，而是基于证据）：
   - 搜索类似方法的已有实现（检查 GitHub）
   - 查找需要打败的具体 baseline 数字
   - 了解类似实验的硬件/数据需求
   - 查找相关工作中已识别的潜在失败模式

2. **成本估算必须基于真实数据**：
   - 找到类似实验的实际成本（不是拍脑袋）
   - 考虑不同研究模式下的成本差异

3. **内部一致性自查**：
   - approach 是否直接解决 Round 1 识别的 core_problem？
   - resource estimate 与 approach 复杂度是否匹配？
   - target venues 与贡献级别是否相称？

For feasibility grounding:
- Search "github.com {method_name} {task}" to check if building blocks or reference implementations exist.
  If nothing similar exists, your timeline estimate should be longer.
- Search "huggingface.co/datasets {dataset_name}" or "paperswithcode.com {task} datasets" to verify
  that required datasets are actually accessible. If the dataset is proprietary or hard to obtain, flag it.

When estimating costs for the three research modes (ordered from most to least human involvement):

1. **Manual (纯人工)**: Human writes code, designs experiments, analyzes results. GPU idle rate is HIGH because GPU waits for humans. Do NOT include salary — only estimate GPU cost.

2. **Human-in-Loop (人机协作)**: Agent executes, human approves key decisions. GPU utilization is moderate. Do NOT include salary — only estimate GPU cost + API cost. Team field describes required check-in frequency.

3. **Auto Research (全自动)**: Agent runs 24/7, explores more experiments but GPU idle rate is near ZERO. Speed bottleneck is GPU count and API key quota — with sufficient resources, a paper can be completed in DAYS. Only estimate GPU cost + API cost. Do NOT factor in agent operational overhead.

Key principles:
- Auto Research uses MORE total GPU hours but has MUCH LOWER GPU idle rate
- Claude API cost: ~$0.05-0.15 per conversation turn (Opus), estimate total turns needed
- Auto mode typically runs 3-5x more experiments than manual (exploration + failed attempts)
- Human-in-Loop reduces auto mode waste by ~40-60% through approval gates

Output ONLY a single JSON object with ALL fields merged. No markdown fences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "type": "user",
  "uuid": "95b615a1-9fbc-40b0-b9a0-0a56807eec80",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T06:56:18.817Z_

```json
{
  "parentUuid": "95b615a1-9fbc-40b0-b9a0-0a56807eec80",
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
  "uuid": "1240f1a5-e1c1-4610-a202-a338e16fbb4a",
  "timestamp": "2026-05-10T06:56:18.817Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T06:56:18.818Z_

```json
{
  "parentUuid": "1240f1a5-e1c1-4610-a202-a338e16fbb4a",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
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
  "uuid": "a082b0e1-408f-4243-b8e3-fb3acfeb8c14",
  "timestamp": "2026-05-10T06:56:18.818Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-10T06:56:18.818Z_

```json
{
  "parentUuid": "a082b0e1-408f-4243-b8e3-fb3acfeb8c14",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "982946bb-eb77-4a31-93bd-949657eff0b6",
  "timestamp": "2026-05-10T06:56:18.818Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
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
  "aiTitle": "Online schema adaptation via extraction-error feedback loops",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---

### Assistant

_source line 8 · 2026-05-10T06:56:25.366Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to research and complete a research direction about "Online Schema Adaptation via Extraction-Error Feedback Loops" for Information Extraction (IE) models. I need to:

1. Search for concurrent work and verify there's no one doing the exact same thing
2. Find current top-performing open-source LLMs
3. Verify key references are real
4. Find target venues with deadlines after 2026-05-10
5. Complete all the missing fields

Let me start by launching parallel searches for:
1. Concurrent work on online schema adaptation for IE


2. Current top open-source LLMs
3. Venue deadlines for NLP/ML conferences
4. Verify key references

I'll run multiple web searches simultaneously to gather this information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "982946bb-eb77-4a31-93bd-949657eff0b6",
  "isSidechain": false,
  "requestId": "req_011CatT9aJh7MF9cgdqzEo2t",
  "type": "assistant",
  "uuid": "c6d6ab59-85cf-4479-8b22-95155fcb11a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NaeuYmddEinTb9W2JcECYv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7657,
      "cache_read_input_tokens": 11278,
      "output_tokens": 1242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1242,
          "cache_read_input_tokens": 11278,
          "cache_creation_input_tokens": 7657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7657
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T06:56:25.427Z_

I'll research this thoroughly with parallel searches covering concurrent work, current models, venues, and reference verification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6d6ab59-85cf-4479-8b22-95155fcb11a1",
  "isSidechain": false,
  "requestId": "req_011CatT9aJh7MF9cgdqzEo2t",
  "type": "assistant",
  "uuid": "65754474-77b3-48b5-9493-234dac1de4b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NaeuYmddEinTb9W2JcECYv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7657,
      "cache_read_input_tokens": 11278,
      "output_tokens": 1242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1242,
          "cache_read_input_tokens": 11278,
          "cache_creation_input_tokens": 7657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7657
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T06:56:29.795Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YQ8BPPCjQRzwq4AEj9spzL`</summary>

```json
{
  "description": "Search for concurrent work on online schema adaptation for IE",
  "subagent_type": "general-purpose",
  "prompt": "Search for concurrent and recent work (2025-2026) on online schema adaptation for information extraction, test-time schema refinement, and schema-domain mismatch detection. Use WebSearch for these queries:\n\n1. \"online schema adaptation information extraction 2026\"\n2. \"test-time schema refinement information extraction LLM 2025 2026\"\n3. \"schema mismatch detection named entity recognition feedback loop\"\n4. \"arXiv schema optimization information extraction 2026\"\n5. Search OpenReview for ICML 2026 or NeurIPS 2026 submissions on schema adaptation IE\n\nReport all relevant papers found including titles, venues, years, and brief descriptions of their approaches. Be specific about what each paper does vs what the proposed approach does.",
  "run_in_background": false
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65754474-77b3-48b5-9493-234dac1de4b3",
  "isSidechain": false,
  "requestId": "req_011CatT9aJh7MF9cgdqzEo2t",
  "type": "assistant",
  "uuid": "ab131271-7338-450d-854b-d13c2119c8bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NaeuYmddEinTb9W2JcECYv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7657,
      "cache_read_input_tokens": 11278,
      "output_tokens": 1242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1242,
          "cache_read_input_tokens": 11278,
          "cache_creation_input_tokens": 7657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7657
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-10T06:56:35.834Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01V7fj8cyPbVDiLfx5icaLue`</summary>

```json
{
  "description": "Verify key references and find venue deadlines",
  "subagent_type": "general-purpose",
  "prompt": "I need you to do two things:\n\n1. Verify these papers exist with correct titles and venues using WebSearch:\n   - \"GoLLIE arXiv 2310.03668 2023\" - search to confirm title and authors\n   - \"PARSE arXiv 2510.08623 2025\" - search to confirm title and authors\n   - \"GuideX ACL Findings 2025\" - search to confirm title and venue\n   - \"KnowCoder information extraction\" - search to confirm paper and venue\n   - Also search for any other key papers on: schema-guided IE, zero-shot NER, test-time adaptation LLM\n\n2. Find NLP/ML conference submission deadlines after 2026-05-10. Search for:\n   - \"EMNLP 2026 submission deadline\"\n   - \"COLING 2026 submission deadline\"\n   - \"ACL 2027 submission deadline\"\n   - \"NeurIPS 2026 submission deadline\"\n   - \"ICLR 2027 submission deadline\"\n   - \"NAACL 2026 submission deadline\"\n   - \"EACL 2026 submission deadline\"\n\nReport exact paper titles, venues, and exact deadline dates for conferences. Today is 2026-05-10.",
  "run_in_background": false
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab131271-7338-450d-854b-d13c2119c8bd",
  "isSidechain": false,
  "requestId": "req_011CatT9aJh7MF9cgdqzEo2t",
  "type": "assistant",
  "uuid": "d3d64ba8-6008-4942-bff3-d76427782ed8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NaeuYmddEinTb9W2JcECYv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7657,
      "cache_read_input_tokens": 11278,
      "output_tokens": 1242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1242,
          "cache_read_input_tokens": 11278,
          "cache_creation_input_tokens": 7657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7657
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T06:56:40.937Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01V6BFtuMbiadB3LVsoxvUX9`</summary>

```json
{
  "description": "Find current top open-source LLMs and GPU cost estimates",
  "subagent_type": "general-purpose",
  "prompt": "I need two things for a research paper planning exercise:\n\n1. Find the current best open-source LLMs as of 2026 using WebSearch:\n   - Search \"best open source LLM 2026\"\n   - Search \"SOTA open source language model 2026\"\n   - Search \"top open source instruction following model 2026 huggingface\"\n   - Find models suitable for information extraction / named entity recognition tasks\n   - Note which model families are considered current frontier (e.g., Llama 4, Qwen3, etc.)\n\n2. Find GPU rental costs and experiment cost estimates:\n   - Search \"A100 GPU rental cost 2026 per hour\"\n   - Search \"H100 GPU rental cost 2026\"\n   - Look for costs from Lambda Labs, vast.ai, RunPod\n   - Find examples of LLM fine-tuning experiment costs (hours needed for 7B-70B parameter models)\n\nReport specific model names, versions, benchmark scores if available, and GPU hourly costs.",
  "run_in_background": false
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3d64ba8-6008-4942-bff3-d76427782ed8",
  "isSidechain": false,
  "requestId": "req_011CatT9aJh7MF9cgdqzEo2t",
  "type": "assistant",
  "uuid": "1d280c0a-53ce-4f21-95a7-a9ca1b5ede75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01NaeuYmddEinTb9W2JcECYv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7657,
      "cache_read_input_tokens": 11278,
      "output_tokens": 1242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1242,
          "cache_read_input_tokens": 11278,
          "cache_creation_input_tokens": 7657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7657
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-10 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.  {   \"title\": \"Online Schema…",
  "leafUuid": "1d280c0a-53ce-4f21-95a7-a9ca1b5ede75",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Online schema adaptation via extraction-error feedback loops",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---

### Tool result

_source line 15 · 2026-05-10T06:57:52.357Z_

<details><summary>↩ Tool result · `toolu_01V7fj8cyPbVDiLfx5icaLue`</summary>

```text
Here is the full verified report.

---

## Part 1: Paper Verification

### 1. GoLLIE — arXiv:2310.03668
- **Exact Title:** "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction"
- **Authors:** Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre (HiTZ Basque Center for Language Technology)
- **Venue:** Published as a conference paper at **ICLR 2024** (Vienna, Austria, May 7-11, 2024)
- **arXiv submitted:** October 5, 2023; last revised March 6, 2024 (v5)
- **Status:** CONFIRMED. The arXiv ID, title, and venue are all correct.

---

### 2. PARSE — arXiv:2510.08623
- **Exact Title:** "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction"
- **Authors:** Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla
- **Venue:** **EMNLP 2025 Industry Track**
- **arXiv submitted:** October 8, 2025
- **Status:** CONFIRMED. The arXiv ID and title are verified.

---

### 3. GuideX — ACL Findings 2025
- **Exact Title:** "GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction"
- **Venue:** **Findings of ACL 2025** (ACL Anthology: 2025.findings-acl.1245)
- **Status:** CONFIRMED. The title and venue are correct. The paper also has a companion arXiv preprint at arXiv:2506.00649. Fine-tunes Llama 3.1 and sets state-of-the-art across 7 zero-shot NER benchmarks.

---

### 4. KnowCoder — Information Extraction
- **Exact Title:** "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction"
- **Authors:** Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng
- **Venue:** **ACL 2024** (Proceedings of the 62nd Annual Meeting of the ACL, Bangkok, Thailand, August 2024) — Long paper track
- **ACL Anthology:** 2024.acl-long.475
- **Status:** CONFIRMED.

---

### Additional Key Papers Found

**Schema-Guided IE / Zero-Shot NER:**
- **GPT-NER: Named Entity Recognition via Large Language Models** — NAACL 2025 Findings (2025.findings-naacl.239). Proposes self-verification for LLM-based NER; strong in few-shot/low-resource settings.
- **UniversalNER** — ICLR 2024. Targeted distillation from large LLMs for open named entity recognition.
- **llmNER** (arXiv:2406.04528, 2024) — Zero/few-shot NER exploiting LLMs with multiple prompting strategies.

**Test-Time Adaptation for LLMs:**
- No single landmark "test-time adaptation for IE/NER" paper dominates the 2024-2025 literature. The closest trend is **inference-time prompting and self-verification** (e.g., GPT-NER's self-verification, GuideX's pipeline-driven schema inference). The GitHub repo [Awesome_Test_Time_LLMs](https://github.com/Dereck0602/Awesome_Test_Time_LLMs) aggregates this line of work but no single definitive venue paper emerged from the search.

---

## Part 2: Conference Submission Deadlines (after 2026-05-10)

| Conference | Key Deadline | Notes |
|---|---|---|
| **EMNLP 2026** | ARR Submission: **May 25, 2026** | Budapest, Hungary, Oct 24-29, 2026. Authors must select EMNLP vs. AACL at submission time (binding). |
| **NeurIPS 2026** | Abstract: **May 4, 2026** (PAST); Full paper: **May 6, 2026** (PAST) | Both deadlines are before today (May 10, 2026) — already closed. |
| **EACL 2026** | ARR submission: **Oct 6, 2025** (PAST); Commitment: **Dec 14, 2025** (PAST) | Rabat, Morocco, March 24-29, 2026. Conference already occurred. |
| **COLING 2026** | No official CFP or dates found yet | COLING runs on a biennial schedule; no 2026 edition has been announced. |
| **NAACL 2026** | No official CFP published yet | Albuquerque, USA. Will use ARR; specific cycle deadlines not yet announced. |
| **ACL 2027** | Not yet announced | Will use ARR rolling system; no CFP released. |
| **ICLR 2027** | Not yet announced | No CFP released; typically announced ~Sep-Oct of prior year. |

### Summary of upcoming actionable deadlines (after today, 2026-05-10):
- **EMNLP 2026**: ARR submission deadline **May 25, 2026** — this is the only confirmed upcoming deadline you can still hit.
- All other searched conferences either have deadlines already passed or have not yet published their 2026/2027 CFPs.

---

Sources:
- [GoLLIE arXiv:2310.03668](https://arxiv.org/abs/2310.03668)
- [GoLLIE at ICLR 2024 (OpenReview)](https://openreview.net/forum?id=Y3wpuxd7u9)
- [PARSE arXiv:2510.08623](https://arxiv.org/abs/2510.08623)
- [GUIDEX — ACL Anthology 2025.findings-acl.1245](https://aclanthology.org/2025.findings-acl.1245/)
- [GuideX arXiv:2506.00649](https://arxiv.org/abs/2506.00649)
- [KnowCoder — ACL Anthology 2024.acl-long.475](https://aclanthology.org/2024.acl-long.475/)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [NeurIPS 2026 Dates and Deadlines](https://neurips.cc/Conferences/2026/Dates)
- [EACL 2026 Call for Main Conference Papers](https://2026.eacl.org/calls/papers/)
- [ACL Rolling Review Dates and Venues](http://aclrollingreview.org/dates)
- [GPT-NER at NAACL 2025 Findings](https://aclanthology.org/2025.findings-naacl.239/)

agentId: a7c580bbb8a65e0c4 (use SendMessage with to: 'a7c580bbb8a65e0c4' to continue this agent)
&lt;usage>total_tokens: 25824
tool_uses: 17
duration_ms: 76521&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d3d64ba8-6008-4942-bff3-d76427782ed8",
  "isSidechain": false,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "type": "user",
  "uuid": "d90820a6-7116-4369-a082-0f3ec0b51260",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to do two things:\n\n1. Verify these papers exist with correct titles and venues using WebSearch:\n   - \"GoLLIE arXiv 2310.03668 2023\" - search to confirm title and authors\n   - \"PARSE arXiv 2510.08623 2025\" - search to confirm title and authors\n   - \"GuideX ACL Findings 2025\" - search to confirm title and venue\n   - \"KnowCoder information extraction\" - search to confirm paper and venue\n   - Also search for any other key papers on: schema-guided IE, zero-shot NER, test-time adaptation LLM\n\n2. Find NLP/ML conference submission deadlines after 2026-05-10. Search for:\n   - \"EMNLP 2026 submission deadline\"\n   - \"COLING 2026 submission deadline\"\n   - \"ACL 2027 submission deadline\"\n   - \"NeurIPS 2026 submission deadline\"\n   - \"ICLR 2027 submission deadline\"\n   - \"NAACL 2026 submission deadline\"\n   - \"EACL 2026 submission deadline\"\n\nReport exact paper titles, venues, and exact deadline dates for conferences. Today is 2026-05-10.",
    "agentId": "a7c580bbb8a65e0c4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the full verified report.\n\n---\n\n## Part 1: Paper Verification\n\n### 1. GoLLIE — arXiv:2310.03668\n- **Exact Title:** \"GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction\"\n- **Authors:** Oscar Sainz, Iker Garcia-Ferrero, Rodrigo Agerri, Oier Lopez de Lacalle, German Rigau, Eneko Agirre (HiTZ Basque Center for Language Technology)\n- **Venue:** Published as a conference paper at **ICLR 2024** (Vienna, Austria, May 7-11, 2024)\n- **arXiv submitted:** October 5, 2023; last revised March 6, 2024 (v5)\n- **Status:** CONFIRMED. The arXiv ID, title, and venue are all correct.\n\n---\n\n### 2. PARSE — arXiv:2510.08623\n- **Exact Title:** \"PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\"\n- **Authors:** Anubhav Shrimal, Aryan Jain, Soumyajit Chowdhury, Promod Yenigalla\n- **Venue:** **EMNLP 2025 Industry Track**\n- **arXiv submitted:** October 8, 2025\n- **Status:** CONFIRMED. The arXiv ID and title are verified.\n\n---\n\n### 3. GuideX — ACL Findings 2025\n- **Exact Title:** \"GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction\"\n- **Venue:** **Findings of ACL 2025** (ACL Anthology: 2025.findings-acl.1245)\n- **Status:** CONFIRMED. The title and venue are correct. The paper also has a companion arXiv preprint at arXiv:2506.00649. Fine-tunes Llama 3.1 and sets state-of-the-art across 7 zero-shot NER benchmarks.\n\n---\n\n### 4. KnowCoder — Information Extraction\n- **Exact Title:** \"KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction\"\n- **Authors:** Zixuan Li, Yutao Zeng, Yuxin Zuo, Weicheng Ren, Wenxuan Liu, Miao Su, Yucan Guo, Yantao Liu, Xiang Li, Zhilei Hu, Long Bai, Wei Li, Yidan Liu, Pan Yang, Xiaolong Jin, Jiafeng Guo, Xueqi Cheng\n- **Venue:** **ACL 2024** (Proceedings of the 62nd Annual Meeting of the ACL, Bangkok, Thailand, August 2024) — Long paper track\n- **ACL Anthology:** 2024.acl-long.475\n- **Status:** CONFIRMED.\n\n---\n\n### Additional Key Papers Found\n\n**Schema-Guided IE / Zero-Shot NER:**\n- **GPT-NER: Named Entity Recognition via Large Language Models** — NAACL 2025 Findings (2025.findings-naacl.239). Proposes self-verification for LLM-based NER; strong in few-shot/low-resource settings.\n- **UniversalNER** — ICLR 2024. Targeted distillation from large LLMs for open named entity recognition.\n- **llmNER** (arXiv:2406.04528, 2024) — Zero/few-shot NER exploiting LLMs with multiple prompting strategies.\n\n**Test-Time Adaptation for LLMs:**\n- No single landmark \"test-time adaptation for IE/NER\" paper dominates the 2024-2025 literature. The closest trend is **inference-time prompting and self-verification** (e.g., GPT-NER's self-verification, GuideX's pipeline-driven schema inference). The GitHub repo [Awesome_Test_Time_LLMs](https://github.com/Dereck0602/Awesome_Test_Time_LLMs) aggregates this line of work but no single definitive venue paper emerged from the search.\n\n---\n\n## Part 2: Conference Submission Deadlines (after 2026-05-10)\n\n| Conference | Key Deadline | Notes |\n|---|---|---|\n| **EMNLP 2026** | ARR Submission: **May 25, 2026** | Budapest, Hungary, Oct 24-29, 2026. Authors must select EMNLP vs. AACL at submission time (binding). |\n| **NeurIPS 2026** | Abstract: **May 4, 2026** (PAST); Full paper: **May 6, 2026** (PAST) | Both deadlines are before today (May 10, 2026) — already closed. |\n| **EACL 2026** | ARR submission: **Oct 6, 2025** (PAST); Commitment: **Dec 14, 2025** (PAST) | Rabat, Morocco, March 24-29, 2026. Conference already occurred. |\n| **COLING 2026** | No official CFP or dates found yet | COLING runs on a biennial schedule; no 2026 edition has been announced. |\n| **NAACL 2026** | No official CFP published yet | Albuquerque, USA. Will use ARR; specific cycle deadlines not yet announced. |\n| **ACL 2027** | Not yet announced | Will use ARR rolling system; no CFP released. |\n| **ICLR 2027** | Not yet announced | No CFP released; typically announced ~Sep-Oct of prior year. |\n\n### Summary of upcoming actionable deadlines (after today, 2026-05-10):\n- **EMNLP 2026**: ARR submission deadline **May 25, 2026** — this is the only confirmed upcoming deadline you can still hit.\n- All other searched conferences either have deadlines already passed or have not yet published their 2026/2027 CFPs.\n\n---\n\nSources:\n- [GoLLIE arXiv:2310.03668](https://arxiv.org/abs/2310.03668)\n- [GoLLIE at ICLR 2024 (OpenReview)](https://openreview.net/forum?id=Y3wpuxd7u9)\n- [PARSE arXiv:2510.08623](https://arxiv.org/abs/2510.08623)\n- [GUIDEX — ACL Anthology 2025.findings-acl.1245](https://aclanthology.org/2025.findings-acl.1245/)\n- [GuideX arXiv:2506.00649](https://arxiv.org/abs/2506.00649)\n- [KnowCoder — ACL Anthology 2024.acl-long.475](https://aclanthology.org/2024.acl-long.475/)\n- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [NeurIPS 2026 Dates and Deadlines](https://neurips.cc/Conferences/2026/Dates)\n- [EACL 2026 Call for Main Conference Papers](https://2026.eacl.org/calls/papers/)\n- [ACL Rolling Review Dates and Venues](http://aclrollingreview.org/dates)\n- [GPT-NER at NAACL 2025 Findings](https://aclanthology.org/2025.findings-naacl.239/)"
      }
    ],
    "totalDurationMs": 76521,
    "totalTokens": 25824,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1386,
      "cache_creation_input_tokens": 894,
      "cache_read_input_tokens": 21665,
      "output_tokens": 1879,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 894
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1386,
          "output_tokens": 1879,
          "cache_read_input_tokens": 21665,
          "cache_creation_input_tokens": 894,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 894,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "d3d64ba8-6008-4942-bff3-d76427782ed8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T06:58:05.675Z_

<details><summary>↩ Tool result · `toolu_01V6BFtuMbiadB3LVsoxvUX9`</summary>

```text
Here is a comprehensive report for your research paper planning exercise:

---

## Part 1: Best Open-Source LLMs as of May 2026

### Current Frontier Model Families

**Frontier / Best-in-Class (MoE and Large Dense)**

| Model | Parameters (Total / Active) | License | Key Benchmarks |
|---|---|---|---|
| Kimi K2.6 | 1T / 32B active | MIT | SWE-bench 76.8%, GPQA Diamond 87.6%, AIME 2025 96.1%, HumanEval 99.0% |
| GLM-5 | 744B / 40B active | MIT | SWE-bench 77.8%, GPQA Diamond 86.0%, AIME 2025 84.0%, HumanEval 90.0% |
| DeepSeek-V4-Pro | 1.6T / 49B active | DeepSeek License | Top for long-context reasoning, coding, agentic workflows |
| Qwen3.5 | Various sizes | Apache 2.0 | Competitive with GPT-5.2 / Claude 4.5 Opus on reasoning, coding, multilingual |
| Qwen3.6-27B | 27B | Apache 2.0 | Strong instruction following, coding stability; first model after Qwen3.5 series |

**Notable smaller/efficient models**

| Model | Parameters | Key Strength |
|---|---|---|
| GLM-4.7 | ~9B | Code generation, reasoning |
| Phi-4-mini-instruct | 3.8B | Instruction following / reasoning, comparable to 7B-9B class models |
| SmolLM3-3B (Hugging Face) | 3.4B | Instruction + vision, fits in 8 GB VRAM; outperforms Llama-3.2-3B and Qwen2.5-3B |
| Llama 3.1 405B | 405B dense | Broad general knowledge, multilingual, long context |

**Macro trend:** Open-weight models now lag frontier proprietary models by approximately 3 months on average. The dominant model families are **Qwen (Alibaba)**, **Kimi / Moonshot**, **GLM (Zhipu AI)**, **DeepSeek**, and **Meta Llama**. The majority of top-trending new models originate from Chinese organizations or are derivatives of Chinese-developed base models.

---

### Models Suitable for Information Extraction / Named Entity Recognition

Based on benchmarks and community reports:

- **Qwen3-235B-A22B** — best for multilingual NER/IE, structured output generation, and agentic extraction pipelines
- **DeepSeek-R1** — strongest for reasoning-intensive extraction; largest context window among open models
- **GLM-4.5 / GLM-5** — purpose-built agent architecture; good for autonomous knowledge extraction workflows
- **Llama-3.3-70B** — highest utility score (0.760) in clinical/medical IE benchmarks (JAMIA Open 2026 study)
- **Phi-4-14B** — utility score 0.751 in the same medical IE benchmark; efficient for constrained environments
- **Qwen-2.5-14B** — utility score 0.748; strong multilingual IE
- **Mistral 7B Instruct** — practical for local/private deployments where privacy is a constraint

For structured NER pipelines, the **spaCy-LLM** framework (explosion/spacy-llm) integrates these models into production-grade NLP pipelines.

---

## Part 2: GPU Rental Costs (May 2026)

### A100 80GB — Per-Hour Pricing

| Provider | On-Demand Price/hr | Notes |
|---|---|---|
| Vast.ai (marketplace) | ~$0.53 – $0.72 | Cheapest; P2P marketplace; variable uptime |
| Lambda Labs | $1.29 | Owned hardware; most consistent |
| RunPod | $1.39 | Good balance of cost and reliability |
| Vast.ai (spot) | ~$0.96 – $1.29 | Budget option |
| Hyperstack | $1.35 | On-demand |
| Jarvis Labs | $1.49 | Per-minute billing, no commitment |
| AWS / GCP / Azure | $3.43 – $5.04+ | Premium managed; not recommended for research budgets |

On-demand A100 pricing has dropped ~17% since May 2025 (from ~$2.39 to ~$1.98/hr average).

### H100 80GB — Per-Hour Pricing

| Provider | Price/hr | Notes |
|---|---|---|
| RunPod (spot) | $1.49 | Interruptible |
| RunPod (on-demand) | $1.99 – $2.49 | Reliable; recommended for production |
| Lambda Labs | $2.49 | Owned hardware; consistent |
| Google Cloud | ~$3.00 | On-demand |
| AWS | ~$3.90 | Post-discount mid-2025 rate |
| Vast.ai | $3.29 | Marketplace variability |
| Azure NC H100 v5 | $6.98 | Most expensive mainstream option |

H100 1-year contract prices surged ~40% from $1.70/hr (Oct 2025) to $2.35/hr (Mar 2026) due to supply tightening.

### RTX 4090 (Budget Fine-Tuning Option)

| Provider | Price/hr |
|---|---|
| Vast.ai | $0.27 |
| RunPod | $0.34 |
| Lambda Labs | $0.50 |

---

### Fine-Tuning Experiment Cost Estimates

**Technique note:** QLoRA (4-bit quantized LoRA) is the standard cost-efficient approach; full fine-tuning costs are 5–20x higher.

| Model Size | Method | GPU Required | Training Time | Est. Cost (marketplace rates) |
|---|---|---|---|---|
| 7B | QLoRA | 1x RTX 4090 (24 GB VRAM) | 2–8 hours | $0.50 – $2.00 |
| 7B | LoRA | 1x A100 | 2–4 hours | $10 – $100 |
| 13B–14B | QLoRA | 1x A100 80GB | 4–10 hours | $5 – $15 |
| 70B | QLoRA | 1x A100/H100 80GB | 12–20 hours | $6 – $30 |
| 70B | LoRA (full precision adapters) | 2–4x A100/H100 | 20–48 hours | $50 – $500 |

**Practical rules of thumb:**
- A 65B parameter model fits on a single 48 GB GPU with QLoRA
- For NER/IE fine-tuning (typically small focused datasets), expect the lower end of these ranges
- Multi-GPU parallelism (DeepSpeed / FSDP) can cut wall-clock time proportionally but multiplies per-run cost

---

**Key takeaways for your research paper:**
- The two most cost-effective providers for research experiments are **Lambda Labs** (A100) and **RunPod** (H100 and L40S)
- A full 70B-model fine-tuning experiment with QLoRA can be run for under **$30** on marketplace GPUs
- For NER/IE at 7B scale, total experiment costs are well under **$5** per run on Vast.ai or RunPod spot

---

Sources:
- [Best Open Source LLMs in 2026: Rankings and Licensing Comparison | Onyx AI](https://onyx.app/insights/best-open-source-llms-2026)
- [The Best Open-Source LLMs in 2026 | BentoML](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)
- [Top 7 open source LLMs for 2026 | Instaclustr](https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/)
- [SOTA AI Models: Benchmarks, Metrics & Deployment Guide | Hugging Face](https://huggingface.co/blog/daya-shankar/sota-ai-models)
- [State of Open Source on Hugging Face: Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)
- [Qwen/Qwen3.6-27B · Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)
- [Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv](https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full)
- [Ultimate Guide - Best Open Source LLMs for Knowledge Graph Construction | SiliconFlow](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-Knowledge-Graph-Construction)
- [Locally hosted LLMs for entity and relationship extraction | Medium/Kineviz](https://medium.com/kineviz/locally-hosted-llms-for-entity-and-relationship-extraction-7628bb5efa72)
- [NVIDIA A100 Pricing (May 2026): Cheapest On-demand GPU Instances | ThunderCompute](https://www.thundercompute.com/blog/nvidia-a100-pricing)
- [Rent A100 PCIE GPUs on Vast.ai for $0.53/hr](https://vast.ai/pricing/gpu/A100-PCIE)
- [H100 Rental Prices Compared: $1.49-$6.98/hr Across 15+ Cloud Providers (2026) | IntuitionLabs](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison)
- [2026 Cost of Renting or Buying NVIDIA H100 GPUs | GMI Cloud](https://www.gmicloud.ai/en/blog/2026-cost-of-renting-or-uying-nvidia-h100-gpus-for-data-centers)
- [Lambda Labs vs RunPod vs Vast.ai: Complete Comparison 2026 | GPUCloudList](https://www.gpucloudlist.com/en/blog/lambda-labs-vs-runpod-vs-vast-ai)
- [Cloud GPU Pricing (2026): RTX 4090 $0.29, A100 $1.29, H100 $2.49 | SynpixCloud](https://www.synpixcloud.com/blog/cloud-gpu-pricing-comparison-2026)
- [How to Fine-Tune LLMs in 2026: Costs, GPUs, and Code | Spheron](https://www.spheron.network/blog/how-to-fine-tune-llm-2026/)
- [The Complete Guide to GPU Requirements for LLM Fine-Tuning | RunPod](https://www.runpod.io/blog/llm-fine-tuning-gpu-guide)

agentId: a0c0537b100d7fd7b (use SendMessage with to: 'a0c0537b100d7fd7b' to continue this agent)
&lt;usage>total_tokens: 21606
tool_uses: 9
duration_ms: 84735&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1d280c0a-53ce-4f21-95a7-a9ca1b5ede75",
  "isSidechain": false,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "type": "user",
  "uuid": "52d2b4cc-763b-4dc8-979c-1d18891ebb99",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need two things for a research paper planning exercise:\n\n1. Find the current best open-source LLMs as of 2026 using WebSearch:\n   - Search \"best open source LLM 2026\"\n   - Search \"SOTA open source language model 2026\"\n   - Search \"top open source instruction following model 2026 huggingface\"\n   - Find models suitable for information extraction / named entity recognition tasks\n   - Note which model families are considered current frontier (e.g., Llama 4, Qwen3, etc.)\n\n2. Find GPU rental costs and experiment cost estimates:\n   - Search \"A100 GPU rental cost 2026 per hour\"\n   - Search \"H100 GPU rental cost 2026\"\n   - Look for costs from Lambda Labs, vast.ai, RunPod\n   - Find examples of LLM fine-tuning experiment costs (hours needed for 7B-70B parameter models)\n\nReport specific model names, versions, benchmark scores if available, and GPU hourly costs.",
    "agentId": "a0c0537b100d7fd7b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report for your research paper planning exercise:\n\n---\n\n## Part 1: Best Open-Source LLMs as of May 2026\n\n### Current Frontier Model Families\n\n**Frontier / Best-in-Class (MoE and Large Dense)**\n\n| Model | Parameters (Total / Active) | License | Key Benchmarks |\n|---|---|---|---|\n| Kimi K2.6 | 1T / 32B active | MIT | SWE-bench 76.8%, GPQA Diamond 87.6%, AIME 2025 96.1%, HumanEval 99.0% |\n| GLM-5 | 744B / 40B active | MIT | SWE-bench 77.8%, GPQA Diamond 86.0%, AIME 2025 84.0%, HumanEval 90.0% |\n| DeepSeek-V4-Pro | 1.6T / 49B active | DeepSeek License | Top for long-context reasoning, coding, agentic workflows |\n| Qwen3.5 | Various sizes | Apache 2.0 | Competitive with GPT-5.2 / Claude 4.5 Opus on reasoning, coding, multilingual |\n| Qwen3.6-27B | 27B | Apache 2.0 | Strong instruction following, coding stability; first model after Qwen3.5 series |\n\n**Notable smaller/efficient models**\n\n| Model | Parameters | Key Strength |\n|---|---|---|\n| GLM-4.7 | ~9B | Code generation, reasoning |\n| Phi-4-mini-instruct | 3.8B | Instruction following / reasoning, comparable to 7B-9B class models |\n| SmolLM3-3B (Hugging Face) | 3.4B | Instruction + vision, fits in 8 GB VRAM; outperforms Llama-3.2-3B and Qwen2.5-3B |\n| Llama 3.1 405B | 405B dense | Broad general knowledge, multilingual, long context |\n\n**Macro trend:** Open-weight models now lag frontier proprietary models by approximately 3 months on average. The dominant model families are **Qwen (Alibaba)**, **Kimi / Moonshot**, **GLM (Zhipu AI)**, **DeepSeek**, and **Meta Llama**. The majority of top-trending new models originate from Chinese organizations or are derivatives of Chinese-developed base models.\n\n---\n\n### Models Suitable for Information Extraction / Named Entity Recognition\n\nBased on benchmarks and community reports:\n\n- **Qwen3-235B-A22B** — best for multilingual NER/IE, structured output generation, and agentic extraction pipelines\n- **DeepSeek-R1** — strongest for reasoning-intensive extraction; largest context window among open models\n- **GLM-4.5 / GLM-5** — purpose-built agent architecture; good for autonomous knowledge extraction workflows\n- **Llama-3.3-70B** — highest utility score (0.760) in clinical/medical IE benchmarks (JAMIA Open 2026 study)\n- **Phi-4-14B** — utility score 0.751 in the same medical IE benchmark; efficient for constrained environments\n- **Qwen-2.5-14B** — utility score 0.748; strong multilingual IE\n- **Mistral 7B Instruct** — practical for local/private deployments where privacy is a constraint\n\nFor structured NER pipelines, the **spaCy-LLM** framework (explosion/spacy-llm) integrates these models into production-grade NLP pipelines.\n\n---\n\n## Part 2: GPU Rental Costs (May 2026)\n\n### A100 80GB — Per-Hour Pricing\n\n| Provider | On-Demand Price/hr | Notes |\n|---|---|---|\n| Vast.ai (marketplace) | ~$0.53 – $0.72 | Cheapest; P2P marketplace; variable uptime |\n| Lambda Labs | $1.29 | Owned hardware; most consistent |\n| RunPod | $1.39 | Good balance of cost and reliability |\n| Vast.ai (spot) | ~$0.96 – $1.29 | Budget option |\n| Hyperstack | $1.35 | On-demand |\n| Jarvis Labs | $1.49 | Per-minute billing, no commitment |\n| AWS / GCP / Azure | $3.43 – $5.04+ | Premium managed; not recommended for research budgets |\n\nOn-demand A100 pricing has dropped ~17% since May 2025 (from ~$2.39 to ~$1.98/hr average).\n\n### H100 80GB — Per-Hour Pricing\n\n| Provider | Price/hr | Notes |\n|---|---|---|\n| RunPod (spot) | $1.49 | Interruptible |\n| RunPod (on-demand) | $1.99 – $2.49 | Reliable; recommended for production |\n| Lambda Labs | $2.49 | Owned hardware; consistent |\n| Google Cloud | ~$3.00 | On-demand |\n| AWS | ~$3.90 | Post-discount mid-2025 rate |\n| Vast.ai | $3.29 | Marketplace variability |\n| Azure NC H100 v5 | $6.98 | Most expensive mainstream option |\n\nH100 1-year contract prices surged ~40% from $1.70/hr (Oct 2025) to $2.35/hr (Mar 2026) due to supply tightening.\n\n### RTX 4090 (Budget Fine-Tuning Option)\n\n| Provider | Price/hr |\n|---|---|\n| Vast.ai | $0.27 |\n| RunPod | $0.34 |\n| Lambda Labs | $0.50 |\n\n---\n\n### Fine-Tuning Experiment Cost Estimates\n\n**Technique note:** QLoRA (4-bit quantized LoRA) is the standard cost-efficient approach; full fine-tuning costs are 5–20x higher.\n\n| Model Size | Method | GPU Required | Training Time | Est. Cost (marketplace rates) |\n|---|---|---|---|---|\n| 7B | QLoRA | 1x RTX 4090 (24 GB VRAM) | 2–8 hours | $0.50 – $2.00 |\n| 7B | LoRA | 1x A100 | 2–4 hours | $10 – $100 |\n| 13B–14B | QLoRA | 1x A100 80GB | 4–10 hours | $5 – $15 |\n| 70B | QLoRA | 1x A100/H100 80GB | 12–20 hours | $6 – $30 |\n| 70B | LoRA (full precision adapters) | 2–4x A100/H100 | 20–48 hours | $50 – $500 |\n\n**Practical rules of thumb:**\n- A 65B parameter model fits on a single 48 GB GPU with QLoRA\n- For NER/IE fine-tuning (typically small focused datasets), expect the lower end of these ranges\n- Multi-GPU parallelism (DeepSpeed / FSDP) can cut wall-clock time proportionally but multiplies per-run cost\n\n---\n\n**Key takeaways for your research paper:**\n- The two most cost-effective providers for research experiments are **Lambda Labs** (A100) and **RunPod** (H100 and L40S)\n- A full 70B-model fine-tuning experiment with QLoRA can be run for under **$30** on marketplace GPUs\n- For NER/IE at 7B scale, total experiment costs are well under **$5** per run on Vast.ai or RunPod spot\n\n---\n\nSources:\n- [Best Open Source LLMs in 2026: Rankings and Licensing Comparison | Onyx AI](https://onyx.app/insights/best-open-source-llms-2026)\n- [The Best Open-Source LLMs in 2026 | BentoML](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)\n- [Top 7 open source LLMs for 2026 | Instaclustr](https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/)\n- [SOTA AI Models: Benchmarks, Metrics & Deployment Guide | Hugging Face](https://huggingface.co/blog/daya-shankar/sota-ai-models)\n- [State of Open Source on Hugging Face: Spring 2026](https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026)\n- [Qwen/Qwen3.6-27B · Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B)\n- [Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv](https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full)\n- [Ultimate Guide - Best Open Source LLMs for Knowledge Graph Construction | SiliconFlow](https://www.siliconflow.com/articles/en/best-open-source-LLM-for-Knowledge-Graph-Construction)\n- [Locally hosted LLMs for entity and relationship extraction | Medium/Kineviz](https://medium.com/kineviz/locally-hosted-llms-for-entity-and-relationship-extraction-7628bb5efa72)\n- [NVIDIA A100 Pricing (May 2026): Cheapest On-demand GPU Instances | ThunderCompute](https://www.thundercompute.com/blog/nvidia-a100-pricing)\n- [Rent A100 PCIE GPUs on Vast.ai for $0.53/hr](https://vast.ai/pricing/gpu/A100-PCIE)\n- [H100 Rental Prices Compared: $1.49-$6.98/hr Across 15+ Cloud Providers (2026) | IntuitionLabs](https://intuitionlabs.ai/articles/h100-rental-prices-cloud-comparison)\n- [2026 Cost of Renting or Buying NVIDIA H100 GPUs | GMI Cloud](https://www.gmicloud.ai/en/blog/2026-cost-of-renting-or-uying-nvidia-h100-gpus-for-data-centers)\n- [Lambda Labs vs RunPod vs Vast.ai: Complete Comparison 2026 | GPUCloudList](https://www.gpucloudlist.com/en/blog/lambda-labs-vs-runpod-vs-vast-ai)\n- [Cloud GPU Pricing (2026): RTX 4090 $0.29, A100 $1.29, H100 $2.49 | SynpixCloud](https://www.synpixcloud.com/blog/cloud-gpu-pricing-comparison-2026)\n- [How to Fine-Tune LLMs in 2026: Costs, GPUs, and Code | Spheron](https://www.spheron.network/blog/how-to-fine-tune-llm-2026/)\n- [The Complete Guide to GPU Requirements for LLM Fine-Tuning | RunPod](https://www.runpod.io/blog/llm-fine-tuning-gpu-guide)"
      }
    ],
    "totalDurationMs": 84735,
    "totalTokens": 21606,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4331,
      "cache_read_input_tokens": 14437,
      "output_tokens": 2837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4331
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2837,
          "cache_read_input_tokens": 14437,
          "cache_creation_input_tokens": 4331,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4331,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "1d280c0a-53ce-4f21-95a7-a9ca1b5ede75",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T06:58:48.453Z_

<details><summary>↩ Tool result · `toolu_01YQ8BPPCjQRzwq4AEj9spzL`</summary>

```text
I now have comprehensive results across all five search dimensions. Here is the full report:

---

## Survey of Concurrent and Recent Work (2025-2026): Online Schema Adaptation, Test-Time Schema Refinement, and Schema-Domain Mismatch for Information Extraction

---

### 1. PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction
- **Venue/Year:** EMNLP 2025 (Industry Track); arXiv:2510.08623 (October 2025); also published at Amazon Science
- **Approach:** PARSE has two main sub-systems. ARCHITECT autonomously optimizes JSON schemas for LLM consumption — it analyzes extraction failures, adds entity descriptions, inserts validation rules, and restructures schemas for clarity, iterating offline on held-out examples. RELAY is an integrated code-generation system that maintains backward compatibility during schema evolution. SCOPE then implements reflection-based extraction at inference time, combining static and LLM-based guardrails. Errors trigger automatic retries with revised prompts.
- **Key results:** Up to 64.7% improvement in extraction accuracy on SWDE; 92% reduction in extraction errors within the first retry.
- **Distinction from purely "online" adaptation:** PARSE's schema optimization (ARCHITECT) is an offline process run before deployment. SCOPE handles test-time correction through retries, but schema structure itself is pre-optimized, not adapted in real time to incoming data distribution shifts.

---

### 2. SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema
- **Venue/Year:** AAAI 2026 (accepted); arXiv:2512.12337 (December 2025)
- **Approach:** A four-component pipeline: (1) an IE module for initial extraction; (2) an iterative pruning module that removes low-quality candidates; (3) a Dual-Path Self-Correcting module that checks for both redundancy (over-extraction) and missing entities (under-extraction) in two parallel streams; (4) a Feedback-Driven Optimization module that converts detection signals into three types of specialized adaptive prompts — Redundancy Prompt, Missing Prompt, and FormatError Prompt — which are injected into a context-learning loop for re-extraction. Ships with a Multi-task Bilingual (Chinese-English) Self-Correcting dataset of 100k+ entries.
- **Key results:** +5.27% average F1 across 11 multilingual zero-shot benchmarks; plug-and-play compatible with any LLM; no fine-tuning required at inference.
- **Distinction:** SCIR operates at test time through schema-conditioned feedback, but its feedback loop targets extraction quality (redundancy/missing), not schema-level concept mismatch or domain drift. It refines predictions, not the schema itself.

---

### 3. Schema as Parameterized Tools (SPT) for Universal Information Extraction
- **Venue/Year:** arXiv:2506.01276 (June 2025); also on OpenReview
- **Approach:** SPT reframes schemas as parameterized tool definitions compatible with LLM tool-calling APIs. The framework unifies three IE modes: (a) Schema Retrieval — selecting the right schema from a predefined pool via retrieval; (b) Schema Filling — extracting information by filling schema slots like tool parameters; (c) Schema Generation — synthesizing new schemas on demand for cases not covered by the pool. This makes the system adaptive between closed-IE, open-IE, and on-demand IE tasks within a single framework.
- **Key results:** Robust schema retrieval and selection performance; comparable extraction to LoRA fine-tuned baselines with far fewer trainable parameters.
- **Distinction:** SPT supports dynamic schema selection and on-the-fly schema generation, which is closer to online adaptation than PARSE. However, it does not explicitly detect domain-schema mismatch or learn from extraction errors over time.

---

### 4. DLISC: Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models
- **Venue/Year:** arXiv:2505.14992 (May 2025); also on OpenReview
- **Approach:** A two-stage Dual-LoRA with Incremental Schema Caching architecture. An Identification LoRA first retrieves the most relevant schema(s) from a large schema pool for a given query. An Extraction LoRA then performs the actual extraction using the matched schema. Incremental Schema Caching stores intermediate KV-cache results per schema, avoiding redundant computation when the same schemas appear repeatedly across queries.
- **Key results:** Improved effectiveness and efficiency across multiple IE benchmarks; specifically designed for resource-constrained on-device deployment.
- **Distinction:** The primary contribution is efficient schema selection and caching for edge LLMs. The system selects among pre-defined schemas adaptively, but does not refine or modify schemas based on extraction feedback or domain mismatch signals.

---

### 5. ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images
- **Venue/Year:** EACL 2026 (Long paper); arXiv:2602.12203 (February 2026)
- **Approach:** A new benchmark of 304 closed and on-demand IE query-answer pairs spanning 110 multi-page documents (forms, financial reports, slide decks, webpage screenshots). It unifies Key Entity Extraction (KEE), Relation Extraction (RE), and Visual Question Answering (VQA) into a single schema-variable task. Construction used a pipeline combining human annotation with LLM-generated, human-validated synthetic samples. The benchmark explicitly evaluates schema adaptation capability, query under-specification handling, and answer localization.
- **Key results:** Analysis of open and closed VLMs reveals that current models systematically fail on schema adaptation and underspecified queries — providing a diagnostic framework rather than a solution.
- **Distinction:** This is a benchmark/evaluation contribution, not an adaptive system. It quantifies the problem of schema variability and mismatch in document IE but does not propose an online adaptation mechanism.

---

### 6. ScrapeGraphAI-100k: Large-Scale Dataset for LLM-Based Web Information Extraction
- **Venue/Year:** arXiv:2602.15189 (February 2026)
- **Approach:** A large dataset pairing web content with prompts, schemas, and model outputs. Includes schema-centric diagnostics that identify empirical failure thresholds (e.g., schema depth > 7 levels, key count > 200). Supports stratified evaluation of extraction robustness under increasing schema complexity.
- **Distinction:** Primarily a dataset/benchmark contribution. Does not propose adaptive schema mechanisms but does characterize schema-domain mismatch failure modes quantitatively.

---

### 7. LOGOS: LLM-Driven End-to-End Grounded Theory Development and Schema Induction
- **Venue/Year:** arXiv:2509.24294 (September 2025); also on OpenReview
- **Approach:** Integrates LLM-driven qualitative coding, semantic clustering, graph reasoning, and iterative refinement to build reusable schema/codebook structures from raw text. Oriented toward grounded theory / qualitative research schema induction rather than IE per se, but directly addresses the problem of schema emergence from data.
- **Distinction:** Targets schema induction from scratch via iterative LLM reasoning, not adaptation of an existing schema to a new domain. No extraction feedback loop or mismatch detection.

---

### 8. Schema-Grounded Memory via Iterative Schema-Aware Extraction
- **Venue/Year:** arXiv:2604.27906 (April 2026)
- **Approach:** Focuses on converting unstructured AI memory/conversation history into schema-grounded structured records via iterative, schema-aware extraction. Applies iterative refinement to ensure extracted memory entries conform to a target schema.
- **Distinction:** Domain is AI memory management, not general IE. Schema is fixed; the iterative process refines extraction fidelity, not the schema itself.

---

### 9. NER with Feedback Loops / Human-in-the-Loop (Background Context)
- **Venue/Year:** NeurIPS 2021 Workshop (User-in-the-Loop NER by Counterfactual Learning); EDBT 2019 (Human-in-the-Loop NER with Deep Learning)
- **Approach:** These older works address feedback-driven NER model updates based on user corrections, including handling of selection bias (non-displayed entities). Relevant to schema-mismatch detection in that they recognize systematic entity-type boundary ambiguity as a schema-level problem.
- **Distinction:** These are not 2025-2026 works but remain the primary prior art on feedback loop NER. No 2025-2026 paper specifically framing schema mismatch detection as a first-class problem for NER was found.

---

### 10. OpenReview / ICML 2026 / NeurIPS 2026 Submissions
- **Finding:** The ICML 2026 and NeurIPS 2026 OpenReview portals are live but do not yet surface accepted or public paper lists specifically on schema adaptation for IE. ICML 2026 submissions are still in review as of May 2026. No specific paper on online schema adaptation for IE was found via OpenReview search. The SPT paper (item 3 above) has an OpenReview entry, suggesting it may be under review for a conference.

---

### Summary Table

| Paper | Year | Venue | Schema Adaptation Type | Online/Test-Time | Mismatch Detection |
|---|---|---|---|---|---|
| PARSE | Oct 2025 | EMNLP 2025 | Offline schema optimization + test-time retry | Partial (retry) | No — error-rate proxy |
| SCIR | Dec 2025 | AAAI 2026 | Test-time extraction refinement via feedback | Yes (extraction loop) | Partial (redundancy/missing) |
| SPT | Jun 2025 | arXiv/OpenReview | Dynamic schema selection + on-demand generation | Yes (schema selection) | No |
| DLISC | May 2025 | arXiv/OpenReview | Schema selection for on-device LLMs | No (selection only) | No |
| ExStrucTiny | Feb 2026 | EACL 2026 | Benchmark: schema-variable IE evaluation | N/A | Implicit (benchmark) |
| ScrapeGraphAI-100k | Feb 2026 | arXiv | Dataset: schema complexity diagnostics | N/A | Partial (failure thresholds) |
| LOGOS | Sep 2025 | arXiv/OpenReview | Schema induction from scratch | No | No |

---

### Key Gap Identified

None of the found papers fully addresses all three components simultaneously: (1) detecting that an existing schema is mismatched to the incoming data domain at test time, (2) automatically refining the schema in response, and (3) doing so in an online loop without human intervention or offline re-optimization. SCIR comes closest to a feedback loop but targets extraction quality, not schema-concept alignment. PARSE optimizes schemas offline. SPT generates schemas on demand but without a mismatch signal. This gap represents the clearest area of novelty for a proposed approach combining schema-domain mismatch detection with online schema refinement.

---

Sources:
- [PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (arXiv:2510.08623)](https://arxiv.org/abs/2510.08623)
- [PARSE at EMNLP 2025 Industry Track](https://aclanthology.org/2025.emnlp-industry.184.pdf)
- [PARSE at Amazon Science](https://www.amazon.science/publications/parse-llm-driven-schema-optimization-for-reliable-entity-extraction)
- [SCIR: A Self-Correcting Iterative Refinement Framework (arXiv:2512.12337)](https://arxiv.org/abs/2512.12337)
- [SCIR at AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40326)
- [Schema as Parameterized Tools for Universal IE (arXiv:2506.01276)](https://arxiv.org/abs/2506.01276)
- [SPT on OpenReview](https://openreview.net/forum?id=yoPtjKVtoX)
- [DLISC: Effective and Efficient Schema-aware IE on On-Device LLMs (arXiv:2505.14992)](https://arxiv.org/abs/2505.14992)
- [DLISC on OpenReview](https://openreview.net/pdf?id=lW7nJDWWz4)
- [ExStrucTiny: Schema-Variable Structured IE Benchmark (arXiv:2602.12203)](https://arxiv.org/abs/2602.12203)
- [ExStrucTiny at EACL 2026](https://aclanthology.org/2026.eacl-long.265/)
- [ScrapeGraphAI-100k (arXiv:2602.15189)](https://arxiv.org/html/2602.15189v1)
- [LOGOS: LLM-Driven Schema Induction (arXiv:2509.24294)](https://arxiv.org/pdf/2509.24294)
- [Schema-Grounded Memory via Iterative Extraction (arXiv:2604.27906)](https://arxiv.org/html/2604.27906)
- [ICML 2026 on OpenReview](https://openreview.net/group?id=ICML.cc%2F2026%2FConference)
- [NeurIPS 2026 on OpenReview](https://openreview.net/group?id=NeurIPS.cc%2F2026)
- [User-in-the-Loop NER by Counterfactual Learning (NeurIPS 2021 Workshop)](https://neurips2021-nlp.github.io/papers/29/CameraReady/camera_User_in_the_Loop_Named_Entity_Recognition.pdf)
- [Frontiers: NER with domain schemas in geoscience (2025)](https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2025.1530004/full)

agentId: a5ed62ae593f18051 (use SendMessage with to: 'a5ed62ae593f18051' to continue this agent)
&lt;usage>total_tokens: 25412
tool_uses: 13
duration_ms: 138651&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab131271-7338-450d-854b-d13c2119c8bd",
  "isSidechain": false,
  "promptId": "b10c7a27-afb3-4a1d-87a3-e31570bb9b5c",
  "type": "user",
  "uuid": "b9242ffc-984f-4ed6-bd02-375ce9e4a7d2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for concurrent and recent work (2025-2026) on online schema adaptation for information extraction, test-time schema refinement, and schema-domain mismatch detection. Use WebSearch for these queries:\n\n1. \"online schema adaptation information extraction 2026\"\n2. \"test-time schema refinement information extraction LLM 2025 2026\"\n3. \"schema mismatch detection named entity recognition feedback loop\"\n4. \"arXiv schema optimization information extraction 2026\"\n5. Search OpenReview for ICML 2026 or NeurIPS 2026 submissions on schema adaptation IE\n\nReport all relevant papers found including titles, venues, years, and brief descriptions of their approaches. Be specific about what each paper does vs what the proposed approach does.",
    "agentId": "a5ed62ae593f18051",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive results across all five search dimensions. Here is the full report:\n\n---\n\n## Survey of Concurrent and Recent Work (2025-2026): Online Schema Adaptation, Test-Time Schema Refinement, and Schema-Domain Mismatch for Information Extraction\n\n---\n\n### 1. PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction\n- **Venue/Year:** EMNLP 2025 (Industry Track); arXiv:2510.08623 (October 2025); also published at Amazon Science\n- **Approach:** PARSE has two main sub-systems. ARCHITECT autonomously optimizes JSON schemas for LLM consumption — it analyzes extraction failures, adds entity descriptions, inserts validation rules, and restructures schemas for clarity, iterating offline on held-out examples. RELAY is an integrated code-generation system that maintains backward compatibility during schema evolution. SCOPE then implements reflection-based extraction at inference time, combining static and LLM-based guardrails. Errors trigger automatic retries with revised prompts.\n- **Key results:** Up to 64.7% improvement in extraction accuracy on SWDE; 92% reduction in extraction errors within the first retry.\n- **Distinction from purely \"online\" adaptation:** PARSE's schema optimization (ARCHITECT) is an offline process run before deployment. SCOPE handles test-time correction through retries, but schema structure itself is pre-optimized, not adapted in real time to incoming data distribution shifts.\n\n---\n\n### 2. SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema\n- **Venue/Year:** AAAI 2026 (accepted); arXiv:2512.12337 (December 2025)\n- **Approach:** A four-component pipeline: (1) an IE module for initial extraction; (2) an iterative pruning module that removes low-quality candidates; (3) a Dual-Path Self-Correcting module that checks for both redundancy (over-extraction) and missing entities (under-extraction) in two parallel streams; (4) a Feedback-Driven Optimization module that converts detection signals into three types of specialized adaptive prompts — Redundancy Prompt, Missing Prompt, and FormatError Prompt — which are injected into a context-learning loop for re-extraction. Ships with a Multi-task Bilingual (Chinese-English) Self-Correcting dataset of 100k+ entries.\n- **Key results:** +5.27% average F1 across 11 multilingual zero-shot benchmarks; plug-and-play compatible with any LLM; no fine-tuning required at inference.\n- **Distinction:** SCIR operates at test time through schema-conditioned feedback, but its feedback loop targets extraction quality (redundancy/missing), not schema-level concept mismatch or domain drift. It refines predictions, not the schema itself.\n\n---\n\n### 3. Schema as Parameterized Tools (SPT) for Universal Information Extraction\n- **Venue/Year:** arXiv:2506.01276 (June 2025); also on OpenReview\n- **Approach:** SPT reframes schemas as parameterized tool definitions compatible with LLM tool-calling APIs. The framework unifies three IE modes: (a) Schema Retrieval — selecting the right schema from a predefined pool via retrieval; (b) Schema Filling — extracting information by filling schema slots like tool parameters; (c) Schema Generation — synthesizing new schemas on demand for cases not covered by the pool. This makes the system adaptive between closed-IE, open-IE, and on-demand IE tasks within a single framework.\n- **Key results:** Robust schema retrieval and selection performance; comparable extraction to LoRA fine-tuned baselines with far fewer trainable parameters.\n- **Distinction:** SPT supports dynamic schema selection and on-the-fly schema generation, which is closer to online adaptation than PARSE. However, it does not explicitly detect domain-schema mismatch or learn from extraction errors over time.\n\n---\n\n### 4. DLISC: Effective and Efficient Schema-aware Information Extraction Using On-Device Large Language Models\n- **Venue/Year:** arXiv:2505.14992 (May 2025); also on OpenReview\n- **Approach:** A two-stage Dual-LoRA with Incremental Schema Caching architecture. An Identification LoRA first retrieves the most relevant schema(s) from a large schema pool for a given query. An Extraction LoRA then performs the actual extraction using the matched schema. Incremental Schema Caching stores intermediate KV-cache results per schema, avoiding redundant computation when the same schemas appear repeatedly across queries.\n- **Key results:** Improved effectiveness and efficiency across multiple IE benchmarks; specifically designed for resource-constrained on-device deployment.\n- **Distinction:** The primary contribution is efficient schema selection and caching for edge LLMs. The system selects among pre-defined schemas adaptively, but does not refine or modify schemas based on extraction feedback or domain mismatch signals.\n\n---\n\n### 5. ExStrucTiny: A Benchmark for Schema-Variable Structured Information Extraction from Document Images\n- **Venue/Year:** EACL 2026 (Long paper); arXiv:2602.12203 (February 2026)\n- **Approach:** A new benchmark of 304 closed and on-demand IE query-answer pairs spanning 110 multi-page documents (forms, financial reports, slide decks, webpage screenshots). It unifies Key Entity Extraction (KEE), Relation Extraction (RE), and Visual Question Answering (VQA) into a single schema-variable task. Construction used a pipeline combining human annotation with LLM-generated, human-validated synthetic samples. The benchmark explicitly evaluates schema adaptation capability, query under-specification handling, and answer localization.\n- **Key results:** Analysis of open and closed VLMs reveals that current models systematically fail on schema adaptation and underspecified queries — providing a diagnostic framework rather than a solution.\n- **Distinction:** This is a benchmark/evaluation contribution, not an adaptive system. It quantifies the problem of schema variability and mismatch in document IE but does not propose an online adaptation mechanism.\n\n---\n\n### 6. ScrapeGraphAI-100k: Large-Scale Dataset for LLM-Based Web Information Extraction\n- **Venue/Year:** arXiv:2602.15189 (February 2026)\n- **Approach:** A large dataset pairing web content with prompts, schemas, and model outputs. Includes schema-centric diagnostics that identify empirical failure thresholds (e.g., schema depth > 7 levels, key count > 200). Supports stratified evaluation of extraction robustness under increasing schema complexity.\n- **Distinction:** Primarily a dataset/benchmark contribution. Does not propose adaptive schema mechanisms but does characterize schema-domain mismatch failure modes quantitatively.\n\n---\n\n### 7. LOGOS: LLM-Driven End-to-End Grounded Theory Development and Schema Induction\n- **Venue/Year:** arXiv:2509.24294 (September 2025); also on OpenReview\n- **Approach:** Integrates LLM-driven qualitative coding, semantic clustering, graph reasoning, and iterative refinement to build reusable schema/codebook structures from raw text. Oriented toward grounded theory / qualitative research schema induction rather than IE per se, but directly addresses the problem of schema emergence from data.\n- **Distinction:** Targets schema induction from scratch via iterative LLM reasoning, not adaptation of an existing schema to a new domain. No extraction feedback loop or mismatch detection.\n\n---\n\n### 8. Schema-Grounded Memory via Iterative Schema-Aware Extraction\n- **Venue/Year:** arXiv:2604.27906 (April 2026)\n- **Approach:** Focuses on converting unstructured AI memory/conversation history into schema-grounded structured records via iterative, schema-aware extraction. Applies iterative refinement to ensure extracted memory entries conform to a target schema.\n- **Distinction:** Domain is AI memory management, not general IE. Schema is fixed; the iterative process refines extraction fidelity, not the schema itself.\n\n---\n\n### 9. NER with Feedback Loops / Human-in-the-Loop (Background Context)\n- **Venue/Year:** NeurIPS 2021 Workshop (User-in-the-Loop NER by Counterfactual Learning); EDBT 2019 (Human-in-the-Loop NER with Deep Learning)\n- **Approach:** These older works address feedback-driven NER model updates based on user corrections, including handling of selection bias (non-displayed entities). Relevant to schema-mismatch detection in that they recognize systematic entity-type boundary ambiguity as a schema-level problem.\n- **Distinction:** These are not 2025-2026 works but remain the primary prior art on feedback loop NER. No 2025-2026 paper specifically framing schema mismatch detection as a first-class problem for NER was found.\n\n---\n\n### 10. OpenReview / ICML 2026 / NeurIPS 2026 Submissions\n- **Finding:** The ICML 2026 and NeurIPS 2026 OpenReview portals are live but do not yet surface accepted or public paper lists specifically on schema adaptation for IE. ICML 2026 submissions are still in review as of May 2026. No specific paper on online schema adaptation for IE was found via OpenReview search. The SPT paper (item 3 above) has an OpenReview entry, suggesting it may be under review for a conference.\n\n---\n\n### Summary Table\n\n| Paper | Year | Venue | Schema Adaptation Type | Online/Test-Time | Mismatch Detection |\n|---|---|---|---|---|---|\n| PARSE | Oct 2025 | EMNLP 2025 | Offline schema optimization + test-time retry | Partial (retry) | No — error-rate proxy |\n| SCIR | Dec 2025 | AAAI 2026 | Test-time extraction refinement via feedback | Yes (extraction loop) | Partial (redundancy/missing) |\n| SPT | Jun 2025 | arXiv/OpenReview | Dynamic schema selection + on-demand generation | Yes (schema selection) | No |\n| DLISC | May 2025 | arXiv/OpenReview | Schema selection for on-device LLMs | No (selection only) | No |\n| ExStrucTiny | Feb 2026 | EACL 2026 | Benchmark: schema-variable IE evaluation | N/A | Implicit (benchmark) |\n| ScrapeGraphAI-100k | Feb 2026 | arXiv | Dataset: schema complexity diagnostics | N/A | Partial (failure thresholds) |\n| LOGOS | Sep 2025 | arXiv/OpenReview | Schema induction from scratch | No | No |\n\n---\n\n### Key Gap Identified\n\nNone of the found papers fully addresses all three components simultaneously: (1) detecting that an existing schema is mismatched to the incoming data domain at test time, (2) automatically refining the schema in response, and (3) doing so in an online loop without human intervention or offline re-optimization. SCIR comes closest to a feedback loop but targets extraction quality, not schema-concept alignment. PARSE optimizes schemas offline. SPT generates schemas on demand but without a mismatch signal. This gap represents the clearest area of novelty for a proposed approach combining schema-domain mismatch detection with online schema refinement.\n\n---\n\nSources:\n- [PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (arXiv:2510.08623)](https://arxiv.org/abs/2510.08623)\n- [PARSE at EMNLP 2025 Industry Track](https://aclanthology.org/2025.emnlp-industry.184.pdf)\n- [PARSE at Amazon Science](https://www.amazon.science/publications/parse-llm-driven-schema-optimization-for-reliable-entity-extraction)\n- [SCIR: A Self-Correcting Iterative Refinement Framework (arXiv:2512.12337)](https://arxiv.org/abs/2512.12337)\n- [SCIR at AAAI 2026](https://ojs.aaai.org/index.php/AAAI/article/view/40326)\n- [Schema as Parameterized Tools for Universal IE (arXiv:2506.01276)](https://arxiv.org/abs/2506.01276)\n- [SPT on OpenReview](https://openreview.net/forum?id=yoPtjKVtoX)\n- [DLISC: Effective and Efficient Schema-aware IE on On-Device LLMs (arXiv:2505.14992)](https://arxiv.org/abs/2505.14992)\n- [DLISC on OpenReview](https://openreview.net/pdf?id=lW7nJDWWz4)\n- [ExStrucTiny: Schema-Variable Structured IE Benchmark (arXiv:2602.12203)](https://arxiv.org/abs/2602.12203)\n- [ExStrucTiny at EACL 2026](https://aclanthology.org/2026.eacl-long.265/)\n- [ScrapeGraphAI-100k (arXiv:2602.15189)](https://arxiv.org/html/2602.15189v1)\n- [LOGOS: LLM-Driven Schema Induction (arXiv:2509.24294)](https://arxiv.org/pdf/2509.24294)\n- [Schema-Grounded Memory via Iterative Extraction (arXiv:2604.27906)](https://arxiv.org/html/2604.27906)\n- [ICML 2026 on OpenReview](https://openreview.net/group?id=ICML.cc%2F2026%2FConference)\n- [NeurIPS 2026 on OpenReview](https://openreview.net/group?id=NeurIPS.cc%2F2026)\n- [User-in-the-Loop NER by Counterfactual Learning (NeurIPS 2021 Workshop)](https://neurips2021-nlp.github.io/papers/29/CameraReady/camera_User_in_the_Loop_Named_Entity_Recognition.pdf)\n- [Frontiers: NER with domain schemas in geoscience (2025)](https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2025.1530004/full)"
      }
    ],
    "totalDurationMs": 138651,
    "totalTokens": 25412,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1938,
      "cache_read_input_tokens": 19987,
      "output_tokens": 3486,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1938
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3486,
          "cache_read_input_tokens": 19987,
          "cache_creation_input_tokens": 1938,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1938,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "ab131271-7338-450d-854b-d13c2119c8bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-10 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.  {   \"title\": \"Online Schema…",
  "leafUuid": "b9242ffc-984f-4ed6-bd02-375ce9e4a7d2",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Online schema adaptation via extraction-error feedback loops",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---

### Assistant

_source line 20 · 2026-05-10T07:00:48.180Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to compile the complete research direction. Let me synthesize everything:

**Key findings:**

1. **Concurrent Work:**
   - SCIR (AAAI 2026): Self-correcting IE via feedback, but targets extraction quality not schema concept mismatch
   - PARSE (EMNLP 2025): Offline schema optimization + test-time retry
   - SPT: Dynamic schema selection but no mismatch signal
   - No paper found that does: online schema-domain mismatch detection + schema refinement + zero-seed setting
   
2. **Verified References:**
   - GoLLIE is from ICLR 2024, not ACL as initially stated
   - PARSE appears in EMNLP 2025 Industry Track with arXiv identifier 2510.08623
   - GuideX was published in Findings of ACL 2025
   - KnowCoder reference appears incomplete but represents another relevant approach from ACL 2024
   - SCIR is a self-correcting framework scheduled for AAAI 2026

3. **Target Venues with open deadlines (after 2026-05-10):**
   - EMNLP 2026 has an ARR submission deadline of May 25, 2026, which is the most immediately relevant opportunity
   - NAACL 2026 and ICLR 2027 don't have official calls for papers yet

4. **Current Open-Source Models:**
   - Qwen3-235B-A22B is suitable for production information extraction tasks
   - Qwen3.5 and DeepSeek-R1 handle more complex reasoning-intensive extraction scenarios
   - Evaluating smaller model options in the 7B-14B range for efficiency

, including Qwen2.5-14B, Phi-4-14B, and Llama-3.3-70B

5. **GPU Costs:**
   - A100 GPUs run around $1.29-1.39 per hour, while H100s are $1.99-2.49 per hour
   - Running QLoRA fine-tuning on 7B models costs roughly $0.50-2 per run, scaling up to $6-30 for 70B models

Now I'm designing the core approach: "Online Schema Adaptation via Extraction-Error Feedback Loops". The system needs an error detection layer that identifies when extracted information violates the schema — catching type mismatches, missing required fields, and inconsistencies where the same entity gets assigned different types across sentences.

Beyond detection, I'm aggregating these error patterns across a sliding window of documents to compute alignment scores per entity type, then triggering schema refinement when alignment drops below threshold. A frontier model like Qwen3-72B or DeepSeek-R1 acts as the schema optimizer, taking the current type description, concrete extraction failures, and neighboring type definitions to propose refined descriptions or suggest splitting/merging types. The refined schema gets deployed immediately into the extraction prompt without needing retraining, then the extractor is re-evaluated on a holdout set to measure improvement.

For evaluation, I'm testing on cross-domain benchmarks like FewNERD, CrossNER, and MultiNERD with intentional schema contamination—starting with a source domain schema and measuring baseline F1, F1 after adaptation steps, and comparing against offline baselines like PARSE and SCIR. The core insight here is that unlike SCIR which fixes the schema and refines extractions, I'm flipping that: fixing the extractions to refine the schema itself, which targets the fundamental concept alignment problem rather than just extraction quality. And unlike PARSE which requires offline data, this runs online during deployment with zero seed data.

For resources, I'm estimating 2-3 weeks to build the framework, then roughly 100-150 A100 hours to run experiments across the 7B model and multiple datasets, followed by analysis.

Now I'm breaking down the cost and timeline across three different execution modes. In manual mode, it's 3-6 months with 1-2 researchers and about $200 in GPU costs. Human-in-loop mode where an agent designs experiments and a researcher approves schemas would take 1-2 months with roughly $260-300 total costs. Auto research mode explores 3-5x more experiments in just 1-2 weeks but requires 500-750 A100 hours and $650-1000 in GPU costs, though API rate limits become the bottleneck.

This is genuinely novel work—no existing paper tackles online zero-shot schema adaptation through error feedback. While the individual components like error detection and LLM-based optimization aren't new, the combination is. If I can demonstrate a 10-15% F1 improvement over non-adaptive baselines and match or beat PARSE on cross-domain tasks, this becomes a solid ACL/EMNLP paper, potentially top-tier with strong results and theoretical grounding. I'm rating it as solid given the benchmarking requirements and somewhat incremental nature of individual components.

I'll call the project `schema_adapt_feedback`—21 characters, valid as a Python identifier. Now I'm putting together the complete JSON response.

For the key references, I'm pulling verified papers: GoLLIE and KnowCoder from ACL 2024, PARSE from EMNLP 2025, GUIDEX from ACL Findings 2025, and SCIR from AAAI 2026. I can also include UniversalNER from ICLR 2024 for additional context.

Now I'm outlining the OSAFE framework—a three-stage test-time approach where an error-detection layer first identifies schema misalignments like cross-sentence contradictions and type confusions across a rolling document buffer. When a type's alignment score drops below threshold, a frozen language model receives the current type definition, mismatch examples, and neighboring types to propose schema revisions through splitting, merging, or refinement.

The refined schema then gets swapped directly into the extraction prompt without any fine-tuning, and we validate the improvement on held-out data before full deployment. I'm planning to evaluate this on FewNERD and CrossNER under deliberate schema contamination scenarios, comparing against PARSE, SCIR, and GuideX baselines.

For venues, EMNLP 2026 has a confirmed ARR deadline of May 25, 2026, though I should also track NAACL 2026 and other options once their deadlines are announced. Now I'm drafting a 150-200 word description of the core problem—schema-guided IE models struggle with silent failures when schemas don't align with actual data distributions. failures when deployed on domains whose entity type ontologies partially conflict with training-time schemas — for example, when a medical ontology's 'Treatment' subsumes what the model learned as separate 'Drug' and 'Procedure' types. OSAFE (Online Schema Adaptation via Feedback Errors) addresses this with a three-stage, zero-seed test-time framework: (1) an error-detection layer accumulates schema-domain mismatch signals — cross-sentence entity-type contradictions, persistent type confusions, and missing mandatory arguments — over a rolling document buffer; (2) when a type's alignment score drops below a threshold, a frozen Qwen3-72B schema optimizer proposes targeted revisions to type descriptions (splits, merges, or clarifications) given only the mismatch examples and neighboring schema definitions; (3) the revised schema is hot-swapped into the extraction prompt with no fine-tuning, then validated on a held-out buffer before full deployment. Unlike PARSE, which requires offline synthetic data per domain, and SCIR, which refines extractions but not schema definitions, OSAFE operates in the true zero-seed online setting. On FewNERD and CrossNER under deliberate schema contamination, it achieves 10-15% F1 recovery over non-adaptive baselines across cross-domain schema shift scenarios.

Now I'm working through the resource estimates — GPU hours, utilization rates, timeline, and team size for both manual and human-in-loop approaches. hours: ~200h A100 (agent runs more ablations than manual)
  - GPU utilization: ~60-70% (agent runs experiments while human reviews)
  - Timeline: 4-6 weeks
  - Team: 1 researcher, ~30min/day check-in
  - Claude API cost: $150-250
  - Estimated GPU cost: ~$270
  - Risk note: Schema optimizer prompt design requires careful human review to avoid hallucinated schema revisions

- Auto research:
  - GPU hours: ~500h A100 (3-4x more experiments, hyperparameter sweeps, cross-dataset ablations)
  - GPU utilization: near-zero idle (24/7 execution)
  - Timeline: 1-2 weeks with 4-8 GPUs
  - Team: 0 (only initial setup)
  - Claude API cost: $300-600
  - Estimated GPU cost: ~$675
  - Speed bottleneck: Number of A100 GPUs available; API rate limits for schema optimizer calls
  - Risk note: Without human oversight, auto mode may converge on a locally optimal but meaningless schema (trivial type merging that inflates F1 on buffer but degrades on full test set)

The core contribution feels solid—individual components are validated in prior work, and the novelty lies in the online feedback loop design with zero seed data. This could reach top-tier if results demonstrate clear F1 recovery across multiple benchmarks. Actually, reconsidering: the gap is genuinely novel since no existing work does online schema adaptation without seed data, SCIR only adapts extractions not schemas, and the approach is feasible with existing components. If the results are strong against solid baselines, this has real top-tier potential.

The main risk is that reviewers might dismiss it as "just prompt engineering"—swapping schema descriptions. To push into top-tier territory, I need to formalize the mismatch detection as a rigorous signal, demonstrate that online adaptation generalizes across diverse domains, and provide a thorough analysis of failure modes compared to PARSE. I'll rate this as solid with genuine potential to reach top-tier depending on how strong the empirical results are.

Generating the paper structure... data generation. Looking at the existing landscape, GoLLIE, GuideX, and PARSE each solve pieces of the problem—automated guidelines, schema optimization, iterative refinement—but they're all constrained by either manual effort, offline processing, or fixed schemas post-deployment. SCIR gets closer with self-correcting feedback but still refines predictions rather than the schema itself. The real gap is handling a completely new domain at deployment time with zero seed data, where the model needs to learn and adapt its schema on the fly.

Our approach is OSAFE, which tackles this in three stages. First, we monitor extraction outputs for red flags: when the same entity keeps getting labeled differently across documents, when certain type pairs consistently swap with each other, or when required fields go missing. Once we detect these misalignment signals, we trigger the second stage where a frozen LLM takes the problematic type definition and the error patterns we've observed, then generates targeted schema corrections. the human-in-loop approach runs more experiments with the schema optimizer, requiring about 220 GPU hours with better utilization since the agent works continuously while a researcher spends roughly 30 minutes daily reviewing revisions—completing in 4-6 weeks with Claude API costs around $150-250 for the orchestration and optimizer calls.

The fully automated approach scales up dramatically to 600 GPU hours across 3-4 times more experiments, testing hyperparameter sweeps and cross-domain schema transfers in parallel, completing in just 1-2 weeks with 4-8 A100s running simultaneously and Claude API costs between $350-600, though it requires careful setup of the experiment harness upfront.

The main constraints are GPU availability and API rate limits, and there's a real risk of overfitting schema changes to the validation buffer without human review — the held-out test set becomes the true measure of whether revisions actually generalize rather than just patch narrow cases.

The target is EMNLP 2026 with an ARR submission deadline in May.

Looking at the key references in this space, the work builds on recent advances in schema-guided extraction and synthetic data generation, particularly around handling domain shift and ontology mismatches. The core problem OSAFE tackles is that these models break down when deployed to domains where entity type hierarchies conflict with what they learned during training — like when a medical system's 'Treatment' category encompasses both 'Drug' and 'Procedure' as separate types in the original schema.

The approach uses a three-stage test-time adaptation pipeline: first, an error detection layer monitors for schema-domain conflicts by tracking cross-sentence contradictions and type confusions across a rolling buffer of documents; when a type's alignment score falls below a threshold, a frozen language model proposes targeted schema modifications like splitting or merging types based only on the mismatch examples; finally, the updated schema gets swapped into the extraction prompt without any fine-tuning and validated before going live. This differs from prior work like PARSE, which needs offline synthetic data generation per domain, and SCIR, which refines predictions rather than the schema itself — OSAFE operates purely in a zero-seed online setting. Early results on FewNERD, CrossNER, and MultiNERD with intentional schema conflicts show potential for 10-15% F1 improvements.

Now I'm validating the project metadata and checking the description length...

The approach breaks down into three key stages: first, detecting schema mismatches through accumulated signals like cross-sentence contradictions and type confusions; second, using a frozen language model to propose targeted schema revisions when alignment scores drop; and third, applying these revisions iteratively during test-time inference to recover performance on shifted domains. I'm checking whether Qwen3-72B is the right model reference here, or if I should pivot to something like DeepSeek-R1 based on what the research actually found. The agent identified Qwen3-235B-A22B as a top performer, so I could use that instead, but Qwen3-72B feels like a reasonable representative of the frontier open-source family.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9242ffc-984f-4ed6-bd02-375ce9e4a7d2",
  "isSidechain": false,
  "requestId": "req_011CatTLbvUp5QbdparbSvCF",
  "type": "assistant",
  "uuid": "635d8e28-497a-4c1f-978d-fff5ecd0664f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014THe4XbjKU5ZSUupaVJLsZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4921,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 18935,
      "output_tokens": 8438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4921,
          "output_tokens": 8438,
          "cache_read_input_tokens": 18935,
          "cache_creation_input_tokens": 4829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4829
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-10T07:01:06.940Z_

Now I have everything I need. Let me compile the complete JSON.

{
  "title": "Online Schema Adaptation via Extraction-Error Feedback Loops",
  "core_problem": "Schema-guided IE models (GoLLIE, KnowCoder, GuideX) fix the extraction schema at training or deployment time. When a new domain has a schema that partially conflicts with training-time guidelines — e.g., a medical ontology where 'Treatment' subsumes what the model learned as 'Drug' and 'Procedure' — models fail silently with no mechanism to refine their operational schema. How can IE models detect and recover from schema-domain mismatches at test time?",
  "opportunity": "PARSE (arXiv 2510.08623, 2025) demonstrates that automatic schema optimization improves extraction accuracy by 64.7% on SWDE — but it requires offline synthetic data generation per domain. GuideX (ACL Findings 2025) shows that auto-generated guidelines improve zero-shot NER by 7 F1 points — but schemas are fixed at fine-tuning time. The gap is *online* adaptation: using the model's own extraction inconsistencies (type violations, missing mandatory arguments, cross-sentence entity type contradictions) as a feedback signal to iteratively refine schema descriptions during test-time deployment. This aligns with the emerging 'LLM as schema optimizer' paradigm but closes the loop by making feedback domain-specific and error-driven rather than relying on synthetic data generation.",
  "landscape": "GoLLIE (ICLR 2024) shows annotation guidelines improve zero-shot IE but requires manually written guidelines. GuideX (ACL Findings 2025) automates guideline generation and achieves SOTA across 7 zero-shot NER benchmarks but cannot adapt post-deployment. PARSE (EMNLP 2025) optimizes schemas via iterative refinement on synthetic data — 64.7% improvement on SWDE — but is fundamentally offline, requiring seed data per domain. SCIR (AAAI 2026), the most concurrent relevant work, introduces a self-correcting iterative refinement framework with dual-path feedback for detecting redundancy and missing entities in IE; however, it refines extraction predictions given a fixed schema rather than refining the schema definitions themselves in response to concept-level mismatches. The open problem is the zero-seed online setting: a model deployed on a new domain should be able to detect its own schema-domain mismatches (e.g., consistently extracting 'ORGANIZATION' where gold expects 'FACILITY') from extraction pattern violations and propose targeted schema corrections without any human labels or domain-specific synthetic data.",
  "approach": "We propose OSAFE (Online Schema Adaptation via Feedback Errors), a three-stage, zero-seed, test-time framework. In Stage 1, an error-detection layer monitors rolling extraction outputs for schema-domain mismatch signals: cross-sentence entity-type contradictions (the same surface form assigned conflicting types across documents), systematic type confusion patterns (persistent pairwise type swaps accumulating above a confidence threshold), and structurally invalid extractions (missing mandatory arguments). In Stage 2, when a type's alignment score drops below an adaptive threshold, a frozen Qwen3-72B or DeepSeek-R1 schema optimizer receives the current type description, concrete mismatch examples, and neighboring type definitions, then generates a targeted schema revision — type split, merge, or refined boundary description — without accessing any gold labels. In Stage 3, the revised schema description is hot-swapped into the extraction prompt (no fine-tuning required since schema descriptions are prompt-level components), validated on a held-out document buffer to confirm F1 improvement, and committed only if validation passes. We evaluate under deliberate schema contamination on FewNERD, CrossNER, and MultiNERD, comparing against PARSE, SCIR, and GuideX baselines to measure F1 recovery from schema-domain mismatch.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~150h A100 80GB (baseline runs + ablations across 3 datasets × 5 schema contamination severity levels + schema optimizer LLM inference calls)",
      "gpu_utilization": "~30-40% — high idle rate while researcher implements error-detection layer, manually inspects schema revision quality, and writes paper",
      "timeline": "3-5 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$200 (150h × $1.35/hr on Lambda Labs)"
    },
    "human_in_loop": {
      "gpu_hours": "~220h A100 80GB (agent explores more schema optimizer prompt variants and dataset cross-transfer combinations than manual mode)",
      "gpu_utilization": "~60-70% — agent runs experiments continuously between human approval gates; human checks schema revision quality and signs off on threshold hyperparameters",
      "timeline": "4-6 weeks",
      "team": "1 researcher, ~30min/day check-in",
      "claude_api_cost": "$150-250 (Opus 4.7 for schema optimizer calls + agent orchestration; ~1500-2500 turns)",
      "estimated_gpu_cost": "~$300 (220h × $1.35/hr on Lambda Labs)",
      "risk_note": "Schema optimizer may generate plausible-sounding but semantically vacuous revisions (trivial type merges that inflate validation-buffer F1 while degrading held-out test F1); human approval gate is critical to catch this failure mode before it propagates"
    },
    "auto_research": {
      "gpu_hours": "~600h A100 80GB (3-4x more experiments: full sweep over alignment-score thresholds, rolling window sizes, optimizer model choices, and all cross-domain schema transfer permutations across 5 datasets)",
      "gpu_utilization": "Near-zero idle — agent orchestrates experiment queue 24/7 with parallel GPU jobs; no human bottleneck between successive runs",
      "timeline": "1-2 weeks with 4-8 A100s running in parallel",
      "team": "0 (only initial setup of experiment harness and API keys)",
      "claude_api_cost": "$350-600 (Opus 4.7; ~3500-6000 turns for schema optimizer calls + agent orchestration + automated result analysis)",
      "estimated_gpu_cost": "~$810 (600h × $1.35/hr on Lambda Labs)",
      "speed_bottleneck": "Number of A100 GPUs available for parallel experiment runs; Anthropic API rate limits on Opus 4.7 schema optimizer calls",
      "risk_note": "Without human oversight, auto mode risks committing schema revisions that overfit the held-out buffer (narrow patches rather than principled generalizations) — final evaluation must use a fully sequestered test split never touched during adaptation"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; conference Oct 24-29, 2026, Budapest, Hungary)"
  ],
  "level": "solid",
  "key_references": [
    "GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction (ICLR 2024)",
    "PARSE: LLM Driven Schema Optimization for Reliable Entity Extraction (EMNLP 2025)",
    "GUIDEX: Guided Synthetic Data Generation for Zero-Shot Information Extraction (ACL Findings 2025)",
    "KnowCoder: Coding Structured Knowledge into LLMs for Universal Information Extraction (ACL 2024)",
    "SCIR: A Self-Correcting Iterative Refinement Framework for Enhanced Information Extraction Based on Schema (AAAI 2026)"
  ],
  "description": "Schema-guided information extraction models fail silently when deployed on domains whose entity type ontologies partially conflict with training-time schemas — for example, when a medical ontology's 'Treatment' subsumes what the model learned as separate 'Drug' and 'Procedure' types. OSAFE (Online Schema Adaptation via Feedback Errors) addresses this with a three-stage, zero-seed test-time framework: (1) an error-detection layer accumulates schema-domain mismatch signals — cross-sentence entity-type contradictions, persistent type confusions, and structurally invalid extractions — over a rolling document buffer; (2) when a type's alignment score drops below an adaptive threshold, a frozen Qwen3-72B schema optimizer proposes targeted schema revisions (type splits, merges, or boundary clarifications) given only mismatch examples and neighboring type definitions; (3) the revised schema is hot-swapped into the extraction prompt with no fine-tuning, then validated on a held-out buffer before deployment. Unlike PARSE, which requires offline synthetic data per domain, and SCIR, which refines extraction predictions but not schema definitions, OSAFE operates in the true zero-seed online setting. Evaluated on FewNERD, CrossNER, and MultiNERD under deliberate schema contamination, it targets 10-15% F1 recovery over non-adaptive baselines across cross-domain schema shift scenarios.",
  "project_name": "schema_adapt_feedback",
  "source": "web_research"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "635d8e28-497a-4c1f-978d-fff5ecd0664f",
  "isSidechain": false,
  "requestId": "req_011CatTLbvUp5QbdparbSvCF",
  "type": "assistant",
  "uuid": "d7a7e4f8-9dda-4f55-8114-133fa4d647a2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014THe4XbjKU5ZSUupaVJLsZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4921,
      "cache_creation_input_tokens": 4829,
      "cache_read_input_tokens": 18935,
      "output_tokens": 8438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4921,
          "output_tokens": 8438,
          "cache_read_input_tokens": 18935,
          "cache_creation_input_tokens": 4829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4829
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-10 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.  {   \"title\": \"Online Schema…",
  "leafUuid": "d7a7e4f8-9dda-4f55-8114-133fa4d647a2",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Online schema adaptation via extraction-error feedback loops",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-10 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.  {   \"title\": \"Online Schema…",
  "leafUuid": "d7a7e4f8-9dda-4f55-8114-133fa4d647a2",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Online schema adaptation via extraction-error feedback loops",
  "sessionId": "8e0ca466-e6f5-4ca9-bbc8-00d0ff299919"
}
```

---
