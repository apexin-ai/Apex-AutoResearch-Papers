# Research conversation: Complete the research direction below with implementation details. **Today's date: 2026-05-18 (UTC).** Only recommend ve

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/ee74ae46-033d-42d9-90c8-f7218628900f.jsonl`
- **Structured JSON:** [`d972a250393b36a4a48d.json`](../../sessions/d9/d972a250393b36a4a48d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-18T18:26:42.498Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-18T18:26:42.498Z",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "content": "Complete the research direction below with implementation details.\n\n**Today's date: 2026-05-18 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.\n\n{\n  \"title\": \"Open-Vocabulary Affordance Reasoning Tokens for Autoregressive VLA\",\n  \"core_problem\": \"Can we extend the chain-of-affordance reasoning paradigm from fixed structured types to an open-vocabulary token space, generating dynamic affordance reasoning tokens conditioned on free-form language before predicting action tokens in a unified autoregressive VLA?\",\n  \"opportunity\": \"CoT-VLA (arXiv 2503.22020) demonstrates that generating visual subgoal tokens before action tokens improves real-world manipulation by 17%, proving intermediate reasoning tokens are highly effective. SeqAfford (CVPR 2025, arXiv 2412.01550) shows MLLMs can generate sequential affordance reasoning for complex multi-step instructions — but only for perception. The VLA survey (arXiv 2507.01925) explicitly identifies affordance as one of the valid action token categories alongside trajectory, goal state, and reasoning tokens, and notes the synergy between affordance (what-to-do) and trajectory (how-to-do). The gap: no work generates open-vocabulary affordance tokens that condition action generation in a unified VLA.\",\n  \"landscape\": \"CoA-VLA (ICCV 2025) generates structured affordance text (4 types) before action prediction — effective but vocabulary-limited. CoT-VLA (arXiv 2503.22020) generates visual subgoal images as reasoning before actions — achieves 17% real-world improvement but uses generic visual reasoning, not affordance-specific. Diffusion-VLA (ICML 2025, arXiv 2412.03293) generates reasoning text before diffusion action head but not affordance-structured. SeqAfford (CVPR 2025) generates sequential affordance reasoning with 180K instruction-point cloud pairs but has no action generation. 3D-AffordanceLLM (ICLR 2025, arXiv 2502.20041) reformulates affordance detection as instruction reasoning affordance segmentation with ~8% mIoU improvement, but only perception. The key insight from the context-dependent affordance study (arXiv 2603.04419) is that affordance must be dynamically determined by the task instruction, not pre-categorized — supporting open-vocabulary tokens over fixed types.\"\n}\n\nADD these fields (keep all existing fields):\n{\n  \"approach\": \"Proposed method or research direction — what you would actually do (3-5 sentences)\",\n  \"resource_estimate\": {\n      \"manual\": {\n          \"gpu_hours\": \"e.g. ~200h A100\",\n          \"gpu_utilization\": \"describe GPU idle rate (human waits cause high idle)\",\n          \"timeline\": \"e.g. 3-6 months\",\n          \"team\": \"e.g. 1-2 researchers\",\n          \"estimated_gpu_cost\": \"GPU rental cost only (do NOT include salary)\"\n      },\n      \"human_in_loop\": {\n          \"gpu_hours\": \"e.g. ~300h A100\",\n          \"gpu_utilization\": \"describe GPU utilization improvement vs manual\",\n          \"timeline\": \"e.g. 1-2 months\",\n          \"team\": \"e.g. 1 researcher, ~30min/day check-in (do NOT include salary)\",\n          \"claude_api_cost\": \"e.g. $100-300\",\n          \"estimated_gpu_cost\": \"GPU rental cost\",\n          \"risk_note\": \"Key bottleneck or risk\"\n      },\n      \"auto_research\": {\n          \"gpu_hours\": \"e.g. ~500h A100 (more exploration, but near-zero idle)\",\n          \"gpu_utilization\": \"describe why GPU idle rate is minimal\",\n          \"timeline\": \"e.g. days to 2 weeks if resources are sufficient\",\n          \"team\": \"0 (only initial setup)\",\n          \"claude_api_cost\": \"e.g. $200-500\",\n          \"estimated_gpu_cost\": \"GPU rental cost\",\n          \"speed_bottleneck\": \"what limits speed (GPU count, API key quota, etc.)\",\n          \"risk_note\": \"Key risk factor\"\n      }\n  },\n  \"target_venues\": [\"Only list venues with deadlines after 2026-05-18; always target the highest-tier venue the contribution level supports — do NOT downgrade venue due to timeline concerns (AI team runs 7x24)\"],\n  \"level\": \"top-tier | solid | incremental\",\n  \"key_references\": [\"Paper title (VENUE YEAR)\", ...],\n  \"description\": \"Executive summary combining all above into 150-200 words\",\n  \"project_name\": \"snake_case_identifier (valid Python id, max 30 chars)\",\n  \"source\": \"web_research\"\n}\n\nFor key_references, verify with WebSearch that cited paper titles and venues are real. Drop any reference you cannot verify.\n\n**Model freshness rule**: When the approach involves pretrained models (LLM, vision model, etc.), use WebSearch to find the current top-performing open-source models for the task (e.g., search \"best open source LLM 2026\", \"SOTA open source language model\"). Use models that represent the current frontier — do NOT default to models from your training data. Entire model families may be outdated (e.g., LLaMA), not just version numbers. Exception: skip this if the idea specifically requires older models (reproduction, model evolution analysis, backward compatibility) or the user explicitly specified a model in the seed topic.\n\n## 竞争论文 & Concurrent Work 搜索\n\n在设计 approach 之前，必须确认没有人正在做同样的事情：\n- 搜索 `{core_problem} 2026` 和 `{approach_keyword} {task} 2026`\n- 在 arXiv 上搜索过去 3 个月的相关提交\n- 在 OpenReview 上搜索即将举行的会议（ICML, NeurIPS, ICLR）的提交\n- 如果发现高度相似的 concurrent work，必须在 landscape 中明确提及，并在 approach 中说明与之的差异化\n\n## 非常仔细地思考和验证\n\n在设计具体 approach 时，你必须深入思考并充分调研：\n\n1. **可行性验证**（不是猜测，而是基于证据）：\n   - 搜索类似方法的已有实现（检查 GitHub）\n   - 查找需要打败的具体 baseline 数字\n   - 了解类似实验的硬件/数据需求\n   - 查找相关工作中已识别的潜在失败模式\n\n2. **成本估算必须基于真实数据**：\n   - 找到类似实验的实际成本（不是拍脑袋）\n   - 考虑不同研究模式下的成本差异\n\n3. **内部一致性自查**：\n   - approach 是否直接解决 Round 1 识别的 core_problem？\n   - resource estimate 与 approach 复杂度是否匹配？\n   - target venues 与贡献级别是否相称？\n\nFor feasibility grounding:\n- Search \"github.com {method_name} {task}\" to check if building blocks or reference implementations exist.\n  If nothing similar exists, note this in resource_estimate but do NOT use it as a reason to target a lower venue.\n- Search \"huggingface.co/datasets {dataset_name}\" or \"paperswithcode.com {task} datasets\" to verify\n  that required datasets are actually accessible. If the dataset is proprietary or hard to obtain, flag it.\n- Timeline estimates should reflect AI Agent team speed (7x24, parallel Workers, near-zero idle), not human pace.\n\nWhen estimating costs for the three research modes (ordered from most to least human involvement):\n\n1. **Manual (纯人工)**: Human writes code, designs experiments, analyzes results. GPU idle rate is HIGH because GPU waits for humans. Do NOT include salary — only estimate GPU cost.\n\n2. **Human-in-Loop (人机协作)**: Agent executes, human approves key decisions. GPU utilization is moderate. Do NOT include salary — only estimate GPU cost + API cost. Team field describes required check-in frequency.\n\n3. **Auto Research (全自动)**: Agent runs 24/7, explores more experiments but GPU idle rate is near ZERO. Speed bottleneck is GPU count and API key quota — with sufficient resources, a paper can be completed in DAYS. Only estimate GPU cost + API cost. Do NOT factor in agent operational overhead.\n\nKey principles:\n- Auto Research uses MORE total GPU hours but has MUCH LOWER GPU idle rate\n- Claude API cost: ~$0.05-0.15 per conversation turn (Opus), estimate total turns needed\n- Auto mode typically runs 3-5x more experiments than manual (exploration + failed attempts)\n- Human-in-Loop reduces auto mode waste by ~40-60% through approval gates\n\nOutput ONLY a single JSON object with ALL fields merged. No markdown fences."
}
```

---

### Runtime record

_source line 2 · 2026-05-18T18:26:42.504Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-18T18:26:42.504Z",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-18T18:26:42.541Z_

Complete the research direction below with implementation details.

**Today's date: 2026-05-18 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.

{
  "title": "Open-Vocabulary Affordance Reasoning Tokens for Autoregressive VLA",
  "core_problem": "Can we extend the chain-of-affordance reasoning paradigm from fixed structured types to an open-vocabulary token space, generating dynamic affordance reasoning tokens conditioned on free-form language before predicting action tokens in a unified autoregressive VLA?",
  "opportunity": "CoT-VLA (arXiv 2503.22020) demonstrates that generating visual subgoal tokens before action tokens improves real-world manipulation by 17%, proving intermediate reasoning tokens are highly effective. SeqAfford (CVPR 2025, arXiv 2412.01550) shows MLLMs can generate sequential affordance reasoning for complex multi-step instructions — but only for perception. The VLA survey (arXiv 2507.01925) explicitly identifies affordance as one of the valid action token categories alongside trajectory, goal state, and reasoning tokens, and notes the synergy between affordance (what-to-do) and trajectory (how-to-do). The gap: no work generates open-vocabulary affordance tokens that condition action generation in a unified VLA.",
  "landscape": "CoA-VLA (ICCV 2025) generates structured affordance text (4 types) before action prediction — effective but vocabulary-limited. CoT-VLA (arXiv 2503.22020) generates visual subgoal images as reasoning before actions — achieves 17% real-world improvement but uses generic visual reasoning, not affordance-specific. Diffusion-VLA (ICML 2025, arXiv 2412.03293) generates reasoning text before diffusion action head but not affordance-structured. SeqAfford (CVPR 2025) generates sequential affordance reasoning with 180K instruction-point cloud pairs but has no action generation. 3D-AffordanceLLM (ICLR 2025, arXiv 2502.20041) reformulates affordance detection as instruction reasoning affordance segmentation with ~8% mIoU improvement, but only perception. The key insight from the context-dependent affordance study (arXiv 2603.04419) is that affordance must be dynamically determined by the task instruction, not pre-categorized — supporting open-vocabulary tokens over fixed types."
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
  "target_venues": ["Only list venues with deadlines after 2026-05-18; always target the highest-tier venue the contribution level supports — do NOT downgrade venue due to timeline concerns (AI team runs 7x24)"],
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
  If nothing similar exists, note this in resource_estimate but do NOT use it as a reason to target a lower venue.
- Search "huggingface.co/datasets {dataset_name}" or "paperswithcode.com {task} datasets" to verify
  that required datasets are actually accessible. If the dataset is proprietary or hard to obtain, flag it.
- Timeline estimates should reflect AI Agent team speed (7x24, parallel Workers, near-zero idle), not human pace.

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
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "type": "user",
  "uuid": "8fae9630-82f2-46a2-936b-155eeef42f6f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-18T18:26:42.540Z_

```json
{
  "parentUuid": "8fae9630-82f2-46a2-936b-155eeef42f6f",
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
  "uuid": "91e2c61a-bcae-4a8d-8558-2ce558d14b00",
  "timestamp": "2026-05-18T18:26:42.540Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-18T18:26:42.540Z_

```json
{
  "parentUuid": "91e2c61a-bcae-4a8d-8558-2ce558d14b00",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "24050a9f-486f-4f72-b781-a3ad4d56635a",
  "timestamp": "2026-05-18T18:26:42.540Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Open-vocabulary affordance tokens in autoregressive VLA",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Assistant

_source line 7 · 2026-05-18T18:26:47.450Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to complete a research direction with detailed implementation fields. This requires significant web research to:

1. Verify references and find real paper titles/venues
2. Search for concurrent work in 2026
3. Find current top-performing open-source models
4. Check feasibility (GitHub implementations, datasets)
5. Find venue deadlines after 2026-05-18
6. Ground cost estimates in real data

Let me start by launching multiple parallel research agents to gather all the information I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24050a9f-486f-4f72-b781-a3ad4d56635a",
  "isSidechain": false,
  "requestId": "req_011CbAWGRTjbuESQe4T8vjGo",
  "type": "assistant",
  "uuid": "c1b902d0-0af8-405e-a27d-33fed47acc14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRg96kz25BCfDvdF8A4Acd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7350,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2033,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 7350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7350
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

_source line 8 · 2026-05-18T18:26:48.408Z_

I'll research this thoroughly across multiple dimensions in parallel. Let me launch several agents to gather the needed information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1b902d0-0af8-405e-a27d-33fed47acc14",
  "isSidechain": false,
  "requestId": "req_011CbAWGRTjbuESQe4T8vjGo",
  "type": "assistant",
  "uuid": "1bc0716e-6d55-4699-ae50-d572a8725e00",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRg96kz25BCfDvdF8A4Acd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7350,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2033,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 7350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7350
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

_source line 9 · 2026-05-18T18:26:54.756Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LCgQhDqzj3Gs3gT3AoQbGC`</summary>

```json
{
  "description": "Search concurrent work 2026",
  "subagent_type": "general-purpose",
  "prompt": "Search the web for concurrent and recent work (2025-2026) on open-vocabulary affordance reasoning in Vision-Language-Action models (VLAs). I need to know if anyone is already doing this or something very similar.\n\nPerform these searches:\n1. WebSearch: \"open-vocabulary affordance reasoning VLA 2026\"\n2. WebSearch: \"affordance tokens autoregressive VLA 2026\"\n3. WebSearch: \"chain of affordance VLA open vocabulary 2025 2026\"\n4. WebSearch: \"arXiv affordance VLA reasoning tokens 2025 2026\"\n5. WebSearch: \"openreview affordance VLA reasoning ICML NeurIPS ICLR 2026\"\n6. WebSearch: \"CoA-VLA open vocabulary affordance\"\n7. WebSearch: \"CoT-VLA affordance reasoning extension 2025 2026\"\n\nFor each result, note: title, authors, venue/date, and how it relates to \"generating open-vocabulary affordance reasoning tokens before action tokens in a unified autoregressive VLA.\" Report any highly similar concurrent work clearly. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1bc0716e-6d55-4699-ae50-d572a8725e00",
  "isSidechain": false,
  "requestId": "req_011CbAWGRTjbuESQe4T8vjGo",
  "type": "assistant",
  "uuid": "f9300e5b-7096-4a07-b0fe-a39b1a78e474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRg96kz25BCfDvdF8A4Acd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7350,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2033,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 7350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7350
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

_source line 10 · 2026-05-18T18:26:59.968Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016umvJmm2HcLEEfnZfPZC23`</summary>

```json
{
  "description": "Verify key references",
  "subagent_type": "general-purpose",
  "prompt": "I need to verify that the following paper references are real (correct titles, venues, and arXiv IDs). For each one, do a WebSearch to confirm. Report the verified title, venue, year, and whether the arXiv ID is correct.\n\nPapers to verify:\n1. \"CoT-VLA\" - arXiv 2503.22020 - claims visual subgoal tokens before action tokens, 17% real-world improvement\n2. \"SeqAfford\" - CVPR 2025 - arXiv 2412.01550 - sequential affordance reasoning for complex multi-step instructions, 180K instruction-point cloud pairs\n3. \"CoA-VLA\" - ICCV 2025 - structured affordance text (4 types) before action prediction\n4. \"Diffusion-VLA\" - ICML 2025 - arXiv 2412.03293 - reasoning text before diffusion action head\n5. \"3D-AffordanceLLM\" - ICLR 2025 - arXiv 2502.20041 - affordance detection as instruction reasoning\n6. VLA survey - arXiv 2507.01925 - identifies affordance as action token category\n7. Context-dependent affordance study - arXiv 2603.04419\n\nSearch for each one individually. Be precise about whether the title, venue, and year match. If any are wrong, provide the correct information."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9300e5b-7096-4a07-b0fe-a39b1a78e474",
  "isSidechain": false,
  "requestId": "req_011CbAWGRTjbuESQe4T8vjGo",
  "type": "assistant",
  "uuid": "c177b3a6-b843-46a2-ba89-c9526a1f1c80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRg96kz25BCfDvdF8A4Acd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7350,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2033,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 7350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7350
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

_source line 11 · 2026-05-18T18:27:05.179Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01764BogW93ipEokmerX2id5`</summary>

```json
{
  "description": "Find SOTA open-source VLA models",
  "subagent_type": "general-purpose",
  "prompt": "I need to find the current state-of-the-art open-source models for building a Vision-Language-Action (VLA) system in 2026. Search for:\n\n1. WebSearch: \"best open source VLA model 2026 robot manipulation\"\n2. WebSearch: \"state of the art vision language action model 2026 open source\"\n3. WebSearch: \"best open source multimodal LLM 2026\" (for the language backbone)\n4. WebSearch: \"top open source vision language model 2026 robotics\"\n5. WebSearch: \"OpenVLA pi0 octo 2026 successor best VLA\"\n6. WebSearch: \"best open source LLM 2026 code generation reasoning\"\n\nReport:\n- The current top open-source VLA models (name, parameters, key capabilities)\n- The current top open-source multimodal LLMs suitable as backbones (name, parameters)\n- Which models have available weights on HuggingFace\n- Any VLA models that already support chain-of-thought or reasoning tokens"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c177b3a6-b843-46a2-ba89-c9526a1f1c80",
  "isSidechain": false,
  "requestId": "req_011CbAWGRTjbuESQe4T8vjGo",
  "type": "assistant",
  "uuid": "584602c5-b78f-4595-a351-5a303c8cec65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRg96kz25BCfDvdF8A4Acd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7350,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2033,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 7350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7350
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

_source line 12 · 2026-05-18T18:27:09.955Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JYk2Mt1CNnAiE354ntFwsV`</summary>

```json
{
  "description": "Find venue deadlines post May 2026",
  "subagent_type": "general-purpose",
  "prompt": "I need to find top-tier AI/ML conference submission deadlines that are AFTER 2026-05-18. Search for:\n\n1. WebSearch: \"NeurIPS 2026 submission deadline\"\n2. WebSearch: \"ICLR 2027 submission deadline\"\n3. WebSearch: \"ICML 2026 submission deadline\"\n4. WebSearch: \"CVPR 2027 submission deadline\"\n5. WebSearch: \"ICCV 2027 submission deadline\"\n6. WebSearch: \"CoRL 2026 submission deadline\"\n7. WebSearch: \"AAAI 2027 submission deadline\"\n8. WebSearch: \"ECCV 2026 submission deadline\"\n9. WebSearch: \"RSS 2026 submission deadline\"\n10. WebSearch: \"top AI conference deadlines 2026 2027\"\n\nFor each venue, report:\n- Full conference name\n- Submission deadline (exact date)\n- Whether the deadline is AFTER May 18, 2026\n- Conference tier (top-tier like NeurIPS/ICML/ICLR/CVPR, or solid like CoRL/RSS/ECCV)\n\nOnly include venues where the deadline has NOT yet passed as of 2026-05-18."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "584602c5-b78f-4595-a351-5a303c8cec65",
  "isSidechain": false,
  "requestId": "req_011CbAWGRTjbuESQe4T8vjGo",
  "type": "assistant",
  "uuid": "720aa6c8-b9e5-4afa-a3df-c47a0d2fd400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRg96kz25BCfDvdF8A4Acd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7350,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2033,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 7350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7350
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

_source line 13 · 2026-05-18T18:27:17.029Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01M4QPxPcoFzmooMzy2D6HET`</summary>

```json
{
  "description": "Check feasibility and costs",
  "subagent_type": "general-purpose",
  "prompt": "I need to ground the feasibility and cost estimates for a research project that:\n- Fine-tunes a VLA (Vision-Language-Action) model to generate open-vocabulary affordance reasoning tokens before action tokens\n- Uses a multimodal LLM backbone (7B-13B parameters)\n- Trains on robot manipulation datasets (Open X-Embodiment, DROID, etc.)\n\nSearch for:\n\n1. WebSearch: \"github.com VLA training code affordance\"\n2. WebSearch: \"github.com CoT-VLA implementation code\"\n3. WebSearch: \"github.com CoA-VLA implementation\"\n4. WebSearch: \"OpenVLA training cost GPU hours A100\"\n5. WebSearch: \"VLA fine-tuning cost GPU hours 2025 2026\"\n6. WebSearch: \"Open X-Embodiment dataset huggingface download\"\n7. WebSearch: \"DROID robot dataset access download\"\n8. WebSearch: \"huggingface datasets robot manipulation affordance\"\n9. WebSearch: \"A100 GPU rental cost per hour 2026\"\n10. WebSearch: \"VLA training 7B parameters GPU hours\"\n\nReport:\n- Available open-source VLA codebases on GitHub\n- Typical GPU hours for VLA training (7B-13B scale)\n- Available robot manipulation datasets and their accessibility\n- Current A100 GPU rental costs (per hour)\n- Any known failure modes or challenges in VLA training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "720aa6c8-b9e5-4afa-a3df-c47a0d2fd400",
  "isSidechain": false,
  "requestId": "req_011CbAWGRTjbuESQe4T8vjGo",
  "type": "assistant",
  "uuid": "b2f23a13-d214-4365-839c-9f2b3b56daf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XRg96kz25BCfDvdF8A4Acd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7350,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7350,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2033,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 7350,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7350
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

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-18 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.  {   \"title\": \"Open-Vocabula…",
  "leafUuid": "b2f23a13-d214-4365-839c-9f2b3b56daf7",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Open-vocabulary affordance tokens in autoregressive VLA",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Tool result

_source line 16 · 2026-05-18T18:28:18.286Z_

<details><summary>↩ Tool result · `toolu_01JYk2Mt1CNnAiE354ntFwsV`</summary>

```text
Here is a comprehensive report of top-tier AI/ML conference submission deadlines relative to May 18, 2026.

---

## CONFIRMED DEADLINES -- STILL OPEN (after May 18, 2026)

### 1. CoRL 2026 -- Conference on Robot Learning
- **Full name:** Conference on Robot Learning 2026
- **Abstract deadline:** May 26, 2026 (11:59 UTC)
- **Paper submission deadline:** May 28-29, 2026 (11:59 UTC)
- **Conference dates:** November 9-12, 2026, Austin, TX
- **After May 18, 2026?** YES -- about 10 days away
- **Tier:** Solid (top venue for robot learning)
- Sources: [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers), [CoRL 2026 OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)

### 2. AAAI 2027 -- Association for the Advancement of Artificial Intelligence
- **Full name:** The 41st AAAI Conference on Artificial Intelligence (AAAI-27)
- **Abstract deadline:** July 21, 2026 (11:59 PM AoE)
- **Paper submission deadline:** July 28, 2026 (11:59 PM AoE)
- **Supplementary material deadline:** July 31, 2026
- **Conference dates:** February 16-23, 2027, Montreal, Canada
- **After May 18, 2026?** YES -- about 2 months away
- **Tier:** Top-tier
- Sources: [AAAI-27 Official Page](https://aaai.org/conference/aaai/aaai-27/), [AI Deadlines - AAAI 2027](http://aideadlines.org/conference/?id=aaai27)

---

## CONFIRMED DEADLINES -- ALREADY PASSED (before May 18, 2026)

### 3. NeurIPS 2026 -- Neural Information Processing Systems
- **Full name:** Conference on Neural Information Processing Systems 2026
- **Abstract deadline:** May 4, 2026 (AoE) -- PASSED
- **Paper submission deadline:** May 6, 2026 (AoE) -- PASSED (12 days ago)
- **Conference dates:** December 6-12, 2026, Sydney, Australia
- **After May 18, 2026?** NO -- deadline already passed
- **Tier:** Top-tier
- Sources: [NeurIPS 2026 Call for Papers](https://neurips.cc/Conferences/2026/CallForPapers), [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)

### 4. ICML 2026 -- International Conference on Machine Learning
- **Paper submission deadline:** January 28, 2026 -- PASSED
- **Conference dates:** July 6-12, 2026, Seoul, Korea
- **After May 18, 2026?** NO
- **Tier:** Top-tier
- Sources: [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates), [ICML 2026 Call for Papers](https://icml.cc/Conferences/2026/CallForPapers)

### 5. ECCV 2026 -- European Conference on Computer Vision
- **Paper submission deadline:** March 5, 2026 (11:00 PM CET) -- PASSED
- **Conference dates:** September 8-12, 2026, Malmo, Sweden
- **After May 18, 2026?** NO
- **Tier:** Solid (top vision venue, biennial)
- Sources: [ECCV 2026 Dates](https://eccv.ecva.net/Conferences/2026/Dates), [ECCV 2026 Call for Papers](https://eccv.ecva.net/Conferences/2026/CallForPapers)

### 6. RSS 2026 -- Robotics: Science and Systems
- **Paper submission deadline:** January 30, 2026 (AoE) -- PASSED
- **Conference dates:** July 13-17, 2026, Sydney, Australia
- **After May 18, 2026?** NO
- **Tier:** Solid (top robotics venue)
- Sources: [RSS 2026 Call for Papers](https://roboticsconference.org/information/cfp/)

---

## DEADLINES NOT YET ANNOUNCED (expected after May 18, 2026)

### 7. CVPR 2027 -- Computer Vision and Pattern Recognition
- **Full name:** IEEE/CVF Conference on Computer Vision and Pattern Recognition 2027
- **Expected submission deadline:** ~November 2026 (based on historical pattern; CVPR 2026 was November 13, 2025)
- **Conference dates:** June 19-26, 2027, Seattle, WA
- **After May 18, 2026?** YES (expected)
- **Tier:** Top-tier
- Sources: [CVPR 2027 on HuggingFace AI Deadlines](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/9d3c5404835da9e75af6f42d683290ceb23d374f), [AI Conference Deadlines](https://trybibby.com/conference-deadlines)

### 8. ICLR 2027 -- International Conference on Learning Representations
- **Expected submission deadline:** ~September-October 2026 (based on ICLR 2026 deadline of September 20, 2025)
- **Conference dates:** TBA (likely mid-2027)
- **After May 18, 2026?** YES (expected)
- **Tier:** Top-tier
- Sources: [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates), [AI & ML Conference Deadlines](https://trybibby.com/conference-deadlines)

### 9. ICML 2027 -- International Conference on Machine Learning
- **Expected submission deadline:** ~January 2027 (based on ICML 2026 deadline of January 28, 2026)
- **Conference dates:** May 16-21, 2027, Toronto, Canada
- **After May 18, 2026?** YES (expected)
- **Tier:** Top-tier
- Sources: [ICML Future Meetings](https://icml.cc/Conferences/FutureMeetings), [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)

### 10. ICCV 2027 -- International Conference on Computer Vision
- **Expected submission deadline:** ~March 2027 (based on historical biennial pattern)
- **Conference dates:** October 2027, Hong Kong
- **After May 18, 2026?** YES (expected)
- **Tier:** Top-tier
- Sources: [AI Conference Deadlines](https://mlciv.com/ai-deadlines/), [AI & ML Conference Deadlines](https://trybibby.com/conference-deadlines)

---

## SUMMARY: Actionable deadlines you can still submit to

| Conference | Tier | Submission Deadline | Days from Now |
|---|---|---|---|
| **CoRL 2026** | Solid | May 26-29, 2026 | ~8-11 days |
| **AAAI 2027** | Top-tier | July 28, 2026 | ~71 days |
| **ICLR 2027** | Top-tier | ~Sep-Oct 2026 (TBA) | ~4-5 months |
| **CVPR 2027** | Top-tier | ~Nov 2026 (TBA) | ~6 months |
| **ICML 2027** | Top-tier | ~Jan 2027 (TBA) | ~8 months |
| **ICCV 2027** | Top-tier | ~Mar 2027 (TBA) | ~10 months |

**Most urgent:** CoRL 2026 (days away) and AAAI 2027 (about 2 months). NeurIPS 2026 just closed 12 days ago. The remaining top-tier venues (ICLR/CVPR/ICML/ICCV) for 2027 have not yet announced official deadlines but are all expected to fall after today's date.

agentId: ad2d4e81156154f42 (use SendMessage with to: 'ad2d4e81156154f42' to continue this agent)
&lt;usage>total_tokens: 24815
tool_uses: 16
duration_ms: 68328&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "720aa6c8-b9e5-4afa-a3df-c47a0d2fd400",
  "isSidechain": false,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "type": "user",
  "uuid": "0a475eac-82be-498e-aaca-eb60fb2f06da",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find top-tier AI/ML conference submission deadlines that are AFTER 2026-05-18. Search for:\n\n1. WebSearch: \"NeurIPS 2026 submission deadline\"\n2. WebSearch: \"ICLR 2027 submission deadline\"\n3. WebSearch: \"ICML 2026 submission deadline\"\n4. WebSearch: \"CVPR 2027 submission deadline\"\n5. WebSearch: \"ICCV 2027 submission deadline\"\n6. WebSearch: \"CoRL 2026 submission deadline\"\n7. WebSearch: \"AAAI 2027 submission deadline\"\n8. WebSearch: \"ECCV 2026 submission deadline\"\n9. WebSearch: \"RSS 2026 submission deadline\"\n10. WebSearch: \"top AI conference deadlines 2026 2027\"\n\nFor each venue, report:\n- Full conference name\n- Submission deadline (exact date)\n- Whether the deadline is AFTER May 18, 2026\n- Conference tier (top-tier like NeurIPS/ICML/ICLR/CVPR, or solid like CoRL/RSS/ECCV)\n\nOnly include venues where the deadline has NOT yet passed as of 2026-05-18.",
    "agentId": "ad2d4e81156154f42",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report of top-tier AI/ML conference submission deadlines relative to May 18, 2026.\n\n---\n\n## CONFIRMED DEADLINES -- STILL OPEN (after May 18, 2026)\n\n### 1. CoRL 2026 -- Conference on Robot Learning\n- **Full name:** Conference on Robot Learning 2026\n- **Abstract deadline:** May 26, 2026 (11:59 UTC)\n- **Paper submission deadline:** May 28-29, 2026 (11:59 UTC)\n- **Conference dates:** November 9-12, 2026, Austin, TX\n- **After May 18, 2026?** YES -- about 10 days away\n- **Tier:** Solid (top venue for robot learning)\n- Sources: [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers), [CoRL 2026 OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)\n\n### 2. AAAI 2027 -- Association for the Advancement of Artificial Intelligence\n- **Full name:** The 41st AAAI Conference on Artificial Intelligence (AAAI-27)\n- **Abstract deadline:** July 21, 2026 (11:59 PM AoE)\n- **Paper submission deadline:** July 28, 2026 (11:59 PM AoE)\n- **Supplementary material deadline:** July 31, 2026\n- **Conference dates:** February 16-23, 2027, Montreal, Canada\n- **After May 18, 2026?** YES -- about 2 months away\n- **Tier:** Top-tier\n- Sources: [AAAI-27 Official Page](https://aaai.org/conference/aaai/aaai-27/), [AI Deadlines - AAAI 2027](http://aideadlines.org/conference/?id=aaai27)\n\n---\n\n## CONFIRMED DEADLINES -- ALREADY PASSED (before May 18, 2026)\n\n### 3. NeurIPS 2026 -- Neural Information Processing Systems\n- **Full name:** Conference on Neural Information Processing Systems 2026\n- **Abstract deadline:** May 4, 2026 (AoE) -- PASSED\n- **Paper submission deadline:** May 6, 2026 (AoE) -- PASSED (12 days ago)\n- **Conference dates:** December 6-12, 2026, Sydney, Australia\n- **After May 18, 2026?** NO -- deadline already passed\n- **Tier:** Top-tier\n- Sources: [NeurIPS 2026 Call for Papers](https://neurips.cc/Conferences/2026/CallForPapers), [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates)\n\n### 4. ICML 2026 -- International Conference on Machine Learning\n- **Paper submission deadline:** January 28, 2026 -- PASSED\n- **Conference dates:** July 6-12, 2026, Seoul, Korea\n- **After May 18, 2026?** NO\n- **Tier:** Top-tier\n- Sources: [ICML 2026 Dates](https://icml.cc/Conferences/2026/Dates), [ICML 2026 Call for Papers](https://icml.cc/Conferences/2026/CallForPapers)\n\n### 5. ECCV 2026 -- European Conference on Computer Vision\n- **Paper submission deadline:** March 5, 2026 (11:00 PM CET) -- PASSED\n- **Conference dates:** September 8-12, 2026, Malmo, Sweden\n- **After May 18, 2026?** NO\n- **Tier:** Solid (top vision venue, biennial)\n- Sources: [ECCV 2026 Dates](https://eccv.ecva.net/Conferences/2026/Dates), [ECCV 2026 Call for Papers](https://eccv.ecva.net/Conferences/2026/CallForPapers)\n\n### 6. RSS 2026 -- Robotics: Science and Systems\n- **Paper submission deadline:** January 30, 2026 (AoE) -- PASSED\n- **Conference dates:** July 13-17, 2026, Sydney, Australia\n- **After May 18, 2026?** NO\n- **Tier:** Solid (top robotics venue)\n- Sources: [RSS 2026 Call for Papers](https://roboticsconference.org/information/cfp/)\n\n---\n\n## DEADLINES NOT YET ANNOUNCED (expected after May 18, 2026)\n\n### 7. CVPR 2027 -- Computer Vision and Pattern Recognition\n- **Full name:** IEEE/CVF Conference on Computer Vision and Pattern Recognition 2027\n- **Expected submission deadline:** ~November 2026 (based on historical pattern; CVPR 2026 was November 13, 2025)\n- **Conference dates:** June 19-26, 2027, Seattle, WA\n- **After May 18, 2026?** YES (expected)\n- **Tier:** Top-tier\n- Sources: [CVPR 2027 on HuggingFace AI Deadlines](https://huggingface.co/spaces/huggingface/ai-deadlines/commit/9d3c5404835da9e75af6f42d683290ceb23d374f), [AI Conference Deadlines](https://trybibby.com/conference-deadlines)\n\n### 8. ICLR 2027 -- International Conference on Learning Representations\n- **Expected submission deadline:** ~September-October 2026 (based on ICLR 2026 deadline of September 20, 2025)\n- **Conference dates:** TBA (likely mid-2027)\n- **After May 18, 2026?** YES (expected)\n- **Tier:** Top-tier\n- Sources: [ICLR 2026 Dates](https://iclr.cc/Conferences/2026/Dates), [AI & ML Conference Deadlines](https://trybibby.com/conference-deadlines)\n\n### 9. ICML 2027 -- International Conference on Machine Learning\n- **Expected submission deadline:** ~January 2027 (based on ICML 2026 deadline of January 28, 2026)\n- **Conference dates:** May 16-21, 2027, Toronto, Canada\n- **After May 18, 2026?** YES (expected)\n- **Tier:** Top-tier\n- Sources: [ICML Future Meetings](https://icml.cc/Conferences/FutureMeetings), [AI Conference Deadlines](https://mlciv.com/ai-deadlines/)\n\n### 10. ICCV 2027 -- International Conference on Computer Vision\n- **Expected submission deadline:** ~March 2027 (based on historical biennial pattern)\n- **Conference dates:** October 2027, Hong Kong\n- **After May 18, 2026?** YES (expected)\n- **Tier:** Top-tier\n- Sources: [AI Conference Deadlines](https://mlciv.com/ai-deadlines/), [AI & ML Conference Deadlines](https://trybibby.com/conference-deadlines)\n\n---\n\n## SUMMARY: Actionable deadlines you can still submit to\n\n| Conference | Tier | Submission Deadline | Days from Now |\n|---|---|---|---|\n| **CoRL 2026** | Solid | May 26-29, 2026 | ~8-11 days |\n| **AAAI 2027** | Top-tier | July 28, 2026 | ~71 days |\n| **ICLR 2027** | Top-tier | ~Sep-Oct 2026 (TBA) | ~4-5 months |\n| **CVPR 2027** | Top-tier | ~Nov 2026 (TBA) | ~6 months |\n| **ICML 2027** | Top-tier | ~Jan 2027 (TBA) | ~8 months |\n| **ICCV 2027** | Top-tier | ~Mar 2027 (TBA) | ~10 months |\n\n**Most urgent:** CoRL 2026 (days away) and AAAI 2027 (about 2 months). NeurIPS 2026 just closed 12 days ago. The remaining top-tier venues (ICLR/CVPR/ICML/ICCV) for 2027 have not yet announced official deadlines but are all expected to fall after today's date."
      }
    ],
    "totalDurationMs": 68328,
    "totalTokens": 24815,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 690,
      "cache_creation_input_tokens": 4297,
      "cache_read_input_tokens": 17715,
      "output_tokens": 2113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4297
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 690,
          "output_tokens": 2113,
          "cache_read_input_tokens": 17715,
          "cache_creation_input_tokens": 4297,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4297,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "720aa6c8-b9e5-4afa-a3df-c47a0d2fd400",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-18T18:28:59.187Z_

<details><summary>↩ Tool result · `toolu_01764BogW93ipEokmerX2id5`</summary>

```text
Here is my comprehensive report on the current state-of-the-art open-source models for building a VLA system in 2026.

---

## 1. Top Open-Source VLA Models

| Model | Parameters | Key Capabilities | HuggingFace Weights |
|---|---|---|---|
| **OpenVLA** | 7B | The foundational open-source VLA. Trained on 970K real-world robot demos from the Open X-Embodiment dataset (21 institutions, 22 embodiments). Outperforms closed RT-2-X (55B) by 16.5% absolute success rate. Apache 2.0 license. Supports language-conditioned control. | Yes (`openvla/openvla-7b`) |
| **SmolVLA** | 450M | Hugging Face's compact VLA. Achieves 82-90% success on LIBERO (within 5% of OpenVLA despite 16x fewer params). Runs at 15-30 Hz on a single RTX 4090. Built on SmolVLM2 backbone. Trained on fewer than 30K episodes of community-collected data. | Yes (`lerobot/smolvla_base`) |
| **A1** | Not precisely stated (VLM-backbone scale) | Fully transparent VLA with budget-aware adaptive inference. Up to 72% lower per-episode latency and 76.6% backbone computation reduction. Achieves 29.00% on RoboChallenge, outperforming pi0 (28.33%) and X-VLA (21.33%). Full training stack released. | Yes (code + checkpoints on GitHub, April 2026) |
| **LingBot-VLA** | 4B | Built on Qwen2.5-VL-3B backbone with Mixture-of-Transformers architecture. Trained on ~20K hours of teleoperated data across 9 robot embodiments. Designed for dual-arm manipulation. | Yes (`robbyant/lingbot-vla-4b`) |
| **X-VLA** | 0.9B | ICLR 2026 paper. Uses soft-prompt approach for cross-embodiment learning -- only 1% of parameters (9M) need tuning per new embodiment. Integrated natively into Hugging Face's LeRobot platform. | Yes (`2toINF/X-VLA-Pt`, `2toINF/X-VLA-SoftFold`, etc.) |
| **HiMoE-VLA** | Not publicly specified | Hierarchical Mixture-of-Experts action module. Improves upon pi0 across experiments via adaptive handling of multi-embodiment heterogeneity. | Yes (code + models on GitHub) |
| **Octo** | 27M / 93M | Lightweight generalist policy from UC Berkeley. Best for small datasets (20-50 demos) and rapid fine-tuning on single embodiments. | Yes |
| **Dexbotic** | Toolbox (multiple models) | An open-source VLA toolbox providing a one-stop research service for embodied intelligence. | Yes (arXiv + code) |

**pi0 (Physical Intelligence)** is state-of-the-art for dexterity but is NOT open-source -- it requires partnership access and cannot be self-hosted.

---

## 2. Top Open-Source Multimodal LLMs Suitable as VLA Backbones

These are the vision-language models you would use as the "brain" if building a custom VLA:

| Model | Parameters | Why It Matters for VLA |
|---|---|---|
| **Qwen2.5-VL** | 3B / 7B / 32B / 72B | Already used as the backbone for LingBot-VLA-4B. Strong visual reasoning, 128K context. Apache 2.0. |
| **GLM-4.6V** | Not specified | Native multimodal tool use, strong visual reasoning, 128K context. Closes the loop between perception, reasoning, and action. |
| **GLM-4.1V-9B-Thinking** | 9B | Specifically designed for visual reasoning with thinking/chain-of-thought capabilities. |
| **Gemma 3** | 4B / 12B / 27B | Multimodal (text+image), 128K context, 140+ languages. DocVQA 85.6%. Efficient enough to run on limited hardware. |
| **Llama 4 Scout / Maverick** | 17B active (109B-400B total MoE) | Meta's first natively multimodal family. Strong general capabilities. |
| **SmolVLM2** | Sub-1B | Used as the encoder-decoder backbone for SmolVLA. Extremely efficient for edge deployment. |

For the general-purpose LLM backbone (reasoning/code generation for agentic VLA pipelines):

| Model | Parameters | Strengths |
|---|---|---|
| **DeepSeek-V3.2** | 671B total / 37B active (MoE) | Best overall open-source LLM. 94.2% MMLU. MIT license. |
| **Qwen 3** | Up to 235B (22B active MoE) | Top-tier reasoning + coding + multilingual. Apache 2.0. |
| **DeepSeek-R1** | Various | Best for pure reasoning tasks. |
| **Kimi K2.6 Thinking** | Not specified | Leading open-source model for agentic coding (78.57 Coding Avg on LiveBench May 2026). |

---

## 3. HuggingFace Availability Summary

Models with **confirmed weights on HuggingFace**:
- `openvla/openvla-7b` -- OpenVLA
- `lerobot/smolvla_base` -- SmolVLA
- `robbyant/lingbot-vla-4b` -- LingBot-VLA
- `2toINF/X-VLA-Pt`, `2toINF/X-VLA-SoftFold`, `2toINF/X-VLA-WidowX` -- X-VLA
- `bazaar-research/lingbot-vla` -- LingBot-VLA variant
- Octo -- available via HuggingFace/GitHub
- A1 -- intermediate checkpoints released (GitHub)
- HiMoE-VLA -- code + models on GitHub

All major multimodal LLMs (Qwen2.5-VL, Gemma 3, Llama 4, GLM-4.6V, DeepSeek-V3.2, Qwen 3) have weights on HuggingFace.

---

## 4. VLA Models with Chain-of-Thought / Reasoning Tokens

This is a rapidly evolving area. The following models explicitly support CoT or reasoning in the VLA context:

| Model | Approach | Key Result |
|---|---|---|
| **ECoT-OpenVLA** (Embodied CoT) | Annotates OpenVLA training data with explicit reasoning steps. Weights available on HuggingFace (`ecot-openvla-7b-bridge`). | +28% absolute success rate on generalization tasks over base OpenVLA. |
| **CoT-VLA** | Predicts future image frames autoregressively as visual goals before generating actions. | +17% over SOTA VLAs in real-world manipulation; +6% in simulation. |
| **DualCoT-VLA** | Parallel visual-linguistic CoT in continuous latent space. Visual CoT extracts 3D spatial cues; linguistic CoT formulates high-level plans. | SOTA on LIBERO and RoboCasa GR1 benchmarks. |
| **LaRA-VLA** (Latent Reasoning VLA) | Latent thinking and prediction -- reasoning happens in latent space rather than explicit text tokens. | Up to 90% inference latency reduction vs. explicit CoT approaches, with improved performance. |
| **LaST0** | Latent spatio-temporal chain-of-thought. Addresses the inference speed bottleneck of explicit CoT. | Efficient latent-space reasoning for real-time control. |
| **dVLA** | Diffusion VLA with multimodal CoT. Grounds high-level instructions into low-level sub-steps. | Improved action prediction through sub-step reasoning. |

**Key takeaway on reasoning**: The field is splitting into two camps -- (1) explicit CoT (like ECoT-OpenVLA, CoT-VLA) that generates text/visual reasoning tokens but is slower, and (2) latent reasoning (like LaRA-VLA, LaST0, DualCoT-VLA) that performs reasoning in continuous latent space for much faster inference. If you need real-time control, the latent approaches are preferred; if you need interpretability, explicit CoT is better.

---

## Practical Recommendations

- **Best starting point**: OpenVLA (7B) with ECoT fine-tuning if you want reasoning, or SmolVLA (450M) if you need real-time inference on consumer hardware.
- **Best efficiency**: X-VLA (0.9B) with soft-prompt tuning -- only 9M parameters need training per new robot embodiment.
- **Best for dual-arm**: LingBot-VLA (4B) trained specifically on dual-arm manipulation data.
- **Best for custom backbone**: Use Qwen2.5-VL (proven in LingBot-VLA) or GLM-4.1V-9B-Thinking (built-in visual reasoning).
- **Most transparent/reproducible**: A1 -- full training stack, data pipeline, and intermediate checkpoints released.

Sources:
- [Top 10 Physical AI Models Powering Real-World Robots in 2026](https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/)
- [VLA Models Compared: OpenVLA vs pi0 vs SmolVLA vs RT-2 (2026 Guide)](https://www.roboticscenter.ai/learn/vla-models-comparison)
- [A1: A Fully Transparent Open-Source VLA Model (arXiv)](https://arxiv.org/abs/2604.05672)
- [SmolVLA: HuggingFace Release](https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/)
- [SmolVLA on HuggingFace](https://huggingface.co/lerobot/smolvla_base)
- [OpenVLA on HuggingFace](https://huggingface.co/openvla/openvla-7b)
- [LingBot-VLA on HuggingFace](https://huggingface.co/robbyant/lingbot-vla-4b)
- [X-VLA (ICLR 2026) on HuggingFace](https://huggingface.co/2toINF/X-VLA-Pt)
- [X-VLA in LeRobot](https://huggingface.co/docs/lerobot/xvla)
- [Embodied Chain-of-Thought Reasoning (GitHub)](https://github.com/MichalZawalski/embodied-CoT)
- [CoT-VLA: Visual Chain-of-Thought Reasoning (arXiv)](https://arxiv.org/html/2503.22020v1)
- [DualCoT-VLA (arXiv)](https://arxiv.org/pdf/2603.22280)
- [LaRA-VLA: Latent Reasoning VLA (arXiv)](https://arxiv.org/pdf/2602.01166)
- [LaST0: Latent Spatio-Temporal CoT (arXiv)](https://arxiv.org/pdf/2601.05248)
- [HiMoE-VLA (arXiv)](https://arxiv.org/pdf/2512.05693)
- [Robbyant Open-Sources LingBot-VLA](https://www.roboticstomorrow.com/news/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/26071/)
- [Physical Intelligence pi0 vs OpenVLA](https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla)
- [Best Open-Source Multimodal Vision Language Models in 2026](https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models)
- [Best Open Source LLMs in 2026](https://www.miniloop.ai/blog/best-open-source-llms-2026)
- [Dexbotic VLA Toolbox (arXiv)](https://arxiv.org/pdf/2510.23511)
- [WholebodyVLA (ICLR 2026)](https://github.com/OpenDriveLab/WholebodyVLA)
- [VLA Foundry: Unified Framework (arXiv)](https://arxiv.org/abs/2604.19728)

agentId: a882ea2155c47ecea (use SendMessage with to: 'a882ea2155c47ecea' to continue this agent)
&lt;usage>total_tokens: 25052
tool_uses: 14
duration_ms: 114005&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "584602c5-b78f-4595-a351-5a303c8cec65",
  "isSidechain": false,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "type": "user",
  "uuid": "3c89e95d-5d1b-4046-b060-d7352fe91529",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find the current state-of-the-art open-source models for building a Vision-Language-Action (VLA) system in 2026. Search for:\n\n1. WebSearch: \"best open source VLA model 2026 robot manipulation\"\n2. WebSearch: \"state of the art vision language action model 2026 open source\"\n3. WebSearch: \"best open source multimodal LLM 2026\" (for the language backbone)\n4. WebSearch: \"top open source vision language model 2026 robotics\"\n5. WebSearch: \"OpenVLA pi0 octo 2026 successor best VLA\"\n6. WebSearch: \"best open source LLM 2026 code generation reasoning\"\n\nReport:\n- The current top open-source VLA models (name, parameters, key capabilities)\n- The current top open-source multimodal LLMs suitable as backbones (name, parameters)\n- Which models have available weights on HuggingFace\n- Any VLA models that already support chain-of-thought or reasoning tokens",
    "agentId": "a882ea2155c47ecea",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive report on the current state-of-the-art open-source models for building a VLA system in 2026.\n\n---\n\n## 1. Top Open-Source VLA Models\n\n| Model | Parameters | Key Capabilities | HuggingFace Weights |\n|---|---|---|---|\n| **OpenVLA** | 7B | The foundational open-source VLA. Trained on 970K real-world robot demos from the Open X-Embodiment dataset (21 institutions, 22 embodiments). Outperforms closed RT-2-X (55B) by 16.5% absolute success rate. Apache 2.0 license. Supports language-conditioned control. | Yes (`openvla/openvla-7b`) |\n| **SmolVLA** | 450M | Hugging Face's compact VLA. Achieves 82-90% success on LIBERO (within 5% of OpenVLA despite 16x fewer params). Runs at 15-30 Hz on a single RTX 4090. Built on SmolVLM2 backbone. Trained on fewer than 30K episodes of community-collected data. | Yes (`lerobot/smolvla_base`) |\n| **A1** | Not precisely stated (VLM-backbone scale) | Fully transparent VLA with budget-aware adaptive inference. Up to 72% lower per-episode latency and 76.6% backbone computation reduction. Achieves 29.00% on RoboChallenge, outperforming pi0 (28.33%) and X-VLA (21.33%). Full training stack released. | Yes (code + checkpoints on GitHub, April 2026) |\n| **LingBot-VLA** | 4B | Built on Qwen2.5-VL-3B backbone with Mixture-of-Transformers architecture. Trained on ~20K hours of teleoperated data across 9 robot embodiments. Designed for dual-arm manipulation. | Yes (`robbyant/lingbot-vla-4b`) |\n| **X-VLA** | 0.9B | ICLR 2026 paper. Uses soft-prompt approach for cross-embodiment learning -- only 1% of parameters (9M) need tuning per new embodiment. Integrated natively into Hugging Face's LeRobot platform. | Yes (`2toINF/X-VLA-Pt`, `2toINF/X-VLA-SoftFold`, etc.) |\n| **HiMoE-VLA** | Not publicly specified | Hierarchical Mixture-of-Experts action module. Improves upon pi0 across experiments via adaptive handling of multi-embodiment heterogeneity. | Yes (code + models on GitHub) |\n| **Octo** | 27M / 93M | Lightweight generalist policy from UC Berkeley. Best for small datasets (20-50 demos) and rapid fine-tuning on single embodiments. | Yes |\n| **Dexbotic** | Toolbox (multiple models) | An open-source VLA toolbox providing a one-stop research service for embodied intelligence. | Yes (arXiv + code) |\n\n**pi0 (Physical Intelligence)** is state-of-the-art for dexterity but is NOT open-source -- it requires partnership access and cannot be self-hosted.\n\n---\n\n## 2. Top Open-Source Multimodal LLMs Suitable as VLA Backbones\n\nThese are the vision-language models you would use as the \"brain\" if building a custom VLA:\n\n| Model | Parameters | Why It Matters for VLA |\n|---|---|---|\n| **Qwen2.5-VL** | 3B / 7B / 32B / 72B | Already used as the backbone for LingBot-VLA-4B. Strong visual reasoning, 128K context. Apache 2.0. |\n| **GLM-4.6V** | Not specified | Native multimodal tool use, strong visual reasoning, 128K context. Closes the loop between perception, reasoning, and action. |\n| **GLM-4.1V-9B-Thinking** | 9B | Specifically designed for visual reasoning with thinking/chain-of-thought capabilities. |\n| **Gemma 3** | 4B / 12B / 27B | Multimodal (text+image), 128K context, 140+ languages. DocVQA 85.6%. Efficient enough to run on limited hardware. |\n| **Llama 4 Scout / Maverick** | 17B active (109B-400B total MoE) | Meta's first natively multimodal family. Strong general capabilities. |\n| **SmolVLM2** | Sub-1B | Used as the encoder-decoder backbone for SmolVLA. Extremely efficient for edge deployment. |\n\nFor the general-purpose LLM backbone (reasoning/code generation for agentic VLA pipelines):\n\n| Model | Parameters | Strengths |\n|---|---|---|\n| **DeepSeek-V3.2** | 671B total / 37B active (MoE) | Best overall open-source LLM. 94.2% MMLU. MIT license. |\n| **Qwen 3** | Up to 235B (22B active MoE) | Top-tier reasoning + coding + multilingual. Apache 2.0. |\n| **DeepSeek-R1** | Various | Best for pure reasoning tasks. |\n| **Kimi K2.6 Thinking** | Not specified | Leading open-source model for agentic coding (78.57 Coding Avg on LiveBench May 2026). |\n\n---\n\n## 3. HuggingFace Availability Summary\n\nModels with **confirmed weights on HuggingFace**:\n- `openvla/openvla-7b` -- OpenVLA\n- `lerobot/smolvla_base` -- SmolVLA\n- `robbyant/lingbot-vla-4b` -- LingBot-VLA\n- `2toINF/X-VLA-Pt`, `2toINF/X-VLA-SoftFold`, `2toINF/X-VLA-WidowX` -- X-VLA\n- `bazaar-research/lingbot-vla` -- LingBot-VLA variant\n- Octo -- available via HuggingFace/GitHub\n- A1 -- intermediate checkpoints released (GitHub)\n- HiMoE-VLA -- code + models on GitHub\n\nAll major multimodal LLMs (Qwen2.5-VL, Gemma 3, Llama 4, GLM-4.6V, DeepSeek-V3.2, Qwen 3) have weights on HuggingFace.\n\n---\n\n## 4. VLA Models with Chain-of-Thought / Reasoning Tokens\n\nThis is a rapidly evolving area. The following models explicitly support CoT or reasoning in the VLA context:\n\n| Model | Approach | Key Result |\n|---|---|---|\n| **ECoT-OpenVLA** (Embodied CoT) | Annotates OpenVLA training data with explicit reasoning steps. Weights available on HuggingFace (`ecot-openvla-7b-bridge`). | +28% absolute success rate on generalization tasks over base OpenVLA. |\n| **CoT-VLA** | Predicts future image frames autoregressively as visual goals before generating actions. | +17% over SOTA VLAs in real-world manipulation; +6% in simulation. |\n| **DualCoT-VLA** | Parallel visual-linguistic CoT in continuous latent space. Visual CoT extracts 3D spatial cues; linguistic CoT formulates high-level plans. | SOTA on LIBERO and RoboCasa GR1 benchmarks. |\n| **LaRA-VLA** (Latent Reasoning VLA) | Latent thinking and prediction -- reasoning happens in latent space rather than explicit text tokens. | Up to 90% inference latency reduction vs. explicit CoT approaches, with improved performance. |\n| **LaST0** | Latent spatio-temporal chain-of-thought. Addresses the inference speed bottleneck of explicit CoT. | Efficient latent-space reasoning for real-time control. |\n| **dVLA** | Diffusion VLA with multimodal CoT. Grounds high-level instructions into low-level sub-steps. | Improved action prediction through sub-step reasoning. |\n\n**Key takeaway on reasoning**: The field is splitting into two camps -- (1) explicit CoT (like ECoT-OpenVLA, CoT-VLA) that generates text/visual reasoning tokens but is slower, and (2) latent reasoning (like LaRA-VLA, LaST0, DualCoT-VLA) that performs reasoning in continuous latent space for much faster inference. If you need real-time control, the latent approaches are preferred; if you need interpretability, explicit CoT is better.\n\n---\n\n## Practical Recommendations\n\n- **Best starting point**: OpenVLA (7B) with ECoT fine-tuning if you want reasoning, or SmolVLA (450M) if you need real-time inference on consumer hardware.\n- **Best efficiency**: X-VLA (0.9B) with soft-prompt tuning -- only 9M parameters need training per new robot embodiment.\n- **Best for dual-arm**: LingBot-VLA (4B) trained specifically on dual-arm manipulation data.\n- **Best for custom backbone**: Use Qwen2.5-VL (proven in LingBot-VLA) or GLM-4.1V-9B-Thinking (built-in visual reasoning).\n- **Most transparent/reproducible**: A1 -- full training stack, data pipeline, and intermediate checkpoints released.\n\nSources:\n- [Top 10 Physical AI Models Powering Real-World Robots in 2026](https://www.marktechpost.com/2026/04/28/top-10-physical-ai-models-powering-real-world-robots-in-2026/)\n- [VLA Models Compared: OpenVLA vs pi0 vs SmolVLA vs RT-2 (2026 Guide)](https://www.roboticscenter.ai/learn/vla-models-comparison)\n- [A1: A Fully Transparent Open-Source VLA Model (arXiv)](https://arxiv.org/abs/2604.05672)\n- [SmolVLA: HuggingFace Release](https://www.marktechpost.com/2025/06/03/hugging-face-releases-smolvla-a-compact-vision-language-action-model-for-affordable-and-efficient-robotics/)\n- [SmolVLA on HuggingFace](https://huggingface.co/lerobot/smolvla_base)\n- [OpenVLA on HuggingFace](https://huggingface.co/openvla/openvla-7b)\n- [LingBot-VLA on HuggingFace](https://huggingface.co/robbyant/lingbot-vla-4b)\n- [X-VLA (ICLR 2026) on HuggingFace](https://huggingface.co/2toINF/X-VLA-Pt)\n- [X-VLA in LeRobot](https://huggingface.co/docs/lerobot/xvla)\n- [Embodied Chain-of-Thought Reasoning (GitHub)](https://github.com/MichalZawalski/embodied-CoT)\n- [CoT-VLA: Visual Chain-of-Thought Reasoning (arXiv)](https://arxiv.org/html/2503.22020v1)\n- [DualCoT-VLA (arXiv)](https://arxiv.org/pdf/2603.22280)\n- [LaRA-VLA: Latent Reasoning VLA (arXiv)](https://arxiv.org/pdf/2602.01166)\n- [LaST0: Latent Spatio-Temporal CoT (arXiv)](https://arxiv.org/pdf/2601.05248)\n- [HiMoE-VLA (arXiv)](https://arxiv.org/pdf/2512.05693)\n- [Robbyant Open-Sources LingBot-VLA](https://www.roboticstomorrow.com/news/2026/01/28/robbyant-open-sources-lingbot-vla-as-a-universal-brain-for-robots/26071/)\n- [Physical Intelligence pi0 vs OpenVLA](https://www.roboticscenter.ai/physical-intelligence-pi0-vs-openvla)\n- [Best Open-Source Multimodal Vision Language Models in 2026](https://www.bentoml.com/blog/multimodal-ai-a-guide-to-open-source-vision-language-models)\n- [Best Open Source LLMs in 2026](https://www.miniloop.ai/blog/best-open-source-llms-2026)\n- [Dexbotic VLA Toolbox (arXiv)](https://arxiv.org/pdf/2510.23511)\n- [WholebodyVLA (ICLR 2026)](https://github.com/OpenDriveLab/WholebodyVLA)\n- [VLA Foundry: Unified Framework (arXiv)](https://arxiv.org/abs/2604.19728)"
      }
    ],
    "totalDurationMs": 114005,
    "totalTokens": 25052,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 818,
      "cache_creation_input_tokens": 2239,
      "cache_read_input_tokens": 18732,
      "output_tokens": 3263,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2239
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 818,
          "output_tokens": 3263,
          "cache_read_input_tokens": 18732,
          "cache_creation_input_tokens": 2239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2239,
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
      "otherToolCount": 14
    }
  },
  "sourceToolAssistantUUID": "584602c5-b78f-4595-a351-5a303c8cec65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
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
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-18 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.  {   \"title\": \"Open-Vocabula…",
  "leafUuid": "3c89e95d-5d1b-4046-b060-d7352fe91529",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Open-vocabulary affordance tokens in autoregressive VLA",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Tool result

_source line 20 · 2026-05-18T18:29:03.639Z_

<details><summary>↩ Tool result · `toolu_016umvJmm2HcLEEfnZfPZC23`</summary>

```text
Here is the verification report for all seven papers:

---

## Paper 1: CoT-VLA (arXiv 2503.22020)

- **Verified title:** "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models"
- **arXiv ID:** 2503.22020 -- **CORRECT**
- **Venue/Year:** The arXiv preprint was posted March 2025. I did not find confirmation of acceptance at a specific conference in the search results (no venue was claimed in your query either).
- **Claims check:** The paper does predict visual subgoal tokens (future image frames) before action tokens -- **CORRECT**. It reports a 17% improvement in real-world manipulation -- **CORRECT**.
- **Verdict: ALL CLAIMS VERIFIED**

---

## Paper 2: SeqAfford (arXiv 2412.01550, CVPR 2025)

- **Verified title:** "SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model"
- **arXiv ID:** 2412.01550 -- **CORRECT**
- **Venue/Year:** CVPR 2025 -- **CORRECT** (confirmed via the CVPR 2025 virtual site and the CVF open access repository)
- **Claims check:** Sequential affordance reasoning for complex multi-step instructions -- **CORRECT**. 180K instruction-point cloud pairs -- **CORRECT**.
- **Verdict: ALL CLAIMS VERIFIED**

---

## Paper 3: CoA-VLA (ICCV 2025)

- **Verified title:** "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance"
- **arXiv ID:** 2412.20451 (not provided in the original query, but confirmed)
- **Venue/Year:** ICCV 2025 -- **CORRECT** (confirmed via the ICCV 2025 virtual site and CVF open access repository)
- **Claims check:** Structured affordance text with 4 types (object, grasp, spatial, movement affordance) before action prediction -- **CORRECT**.
- **Verdict: ALL CLAIMS VERIFIED**

---

## Paper 4: Diffusion-VLA (arXiv 2412.03293, ICML 2025)

- **Verified title:** "Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning"
- **arXiv ID:** 2412.03293 -- **CORRECT**
- **Venue/Year:** ICML 2025 -- **CORRECT** (confirmed via the ICML 2025 virtual poster listing)
- **Claims check:** Reasoning text before diffusion action head -- **CORRECT**. The model uses autoregressive reasoning (next-token prediction) followed by a diffusion model to generate actions.
- **Note:** There is a separate paper called "DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression" also at ICML 2025. The arXiv ID 2412.03293 corresponds to the one with subtitle "Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning" -- make sure you are referencing the correct one.
- **Verdict: ALL CLAIMS VERIFIED**

---

## Paper 5: 3D-AffordanceLLM (arXiv 2502.20041, ICLR 2025)

- **Verified title:** "3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds"
- **arXiv ID:** 2502.20041 -- **CORRECT**
- **Venue/Year:** ICLR 2025 -- **CORRECT** (confirmed via the ICLR 2025 poster listing and the PDF header stating "Published as a conference paper at ICLR 2025")
- **Claims check:** Affordance detection reformulated as instruction reasoning (the "IRAS" task -- Instruction Reasoning Affordance Segmentation) -- **CORRECT**.
- **Verdict: ALL CLAIMS VERIFIED**

---

## Paper 6: VLA Survey (arXiv 2507.01925)

- **Verified title:** "A Survey on Vision-Language-Action Models: An Action Tokenization Perspective"
- **arXiv ID:** 2507.01925 -- **CORRECT**
- **Venue/Year:** arXiv preprint, July 2025. No specific conference venue claimed.
- **Claims check:** The survey categorizes action tokens into types including: language description, code, **affordance**, trajectory, goal state, latent representation, raw action, and reasoning. So yes, it identifies affordance as an action token category -- **CORRECT**.
- **Verdict: ALL CLAIMS VERIFIED**

---

## Paper 7: Context-Dependent Affordance Study (arXiv 2603.04419)

- **Verified title:** "Context-Dependent Affordance Computation in Vision-Language Models"
- **arXiv ID:** 2603.04419 -- **CORRECT**
- **Venue/Year:** arXiv preprint, January 2026 (the 2603 prefix corresponds to March 2026 submission). No specific conference venue claimed.
- **Claims check:** The paper studies context-dependent affordance computation in VLMs, demonstrating over 90% of lexical scene description is context-dependent ("affordance drift"). Author: Murad Farzulla (Dissensus AI / King's College London).
- **Verdict: arXiv ID AND TITLE VERIFIED**

---

## Summary

| # | Paper | Title Correct? | arXiv ID Correct? | Venue/Year Correct? | Key Claims Correct? |
|---|-------|---------------|-------------------|---------------------|-------------------|
| 1 | CoT-VLA | Yes | Yes (2503.22020) | No venue claimed | Yes (visual subgoal tokens, 17% improvement) |
| 2 | SeqAfford | Yes | Yes (2412.01550) | Yes (CVPR 2025) | Yes (180K pairs, sequential reasoning) |
| 3 | CoA-VLA | Yes | Not provided; actual ID is 2412.20451 | Yes (ICCV 2025) | Yes (4 affordance types) |
| 4 | Diffusion-VLA | Yes | Yes (2412.03293) | Yes (ICML 2025) | Yes (reasoning then diffusion) |
| 5 | 3D-AffordanceLLM | Yes | Yes (2502.20041) | Yes (ICLR 2025) | Yes (affordance as instruction reasoning) |
| 6 | VLA Survey | Yes | Yes (2507.01925) | arXiv only (no venue) | Yes (affordance as token category) |
| 7 | Context-dep. affordance | Yes | Yes (2603.04419) | arXiv only (no venue) | Yes |

**All seven references are real papers with correct titles and arXiv IDs.** All claimed venues and years are confirmed accurate.

Sources:
- [CoT-VLA (arXiv 2503.22020)](https://arxiv.org/abs/2503.22020)
- [SeqAfford (arXiv 2412.01550)](https://arxiv.org/abs/2412.01550)
- [SeqAfford CVPR 2025 poster](https://cvpr.thecvf.com/virtual/2025/poster/32496)
- [CoA-VLA (arXiv 2412.20451)](https://arxiv.org/abs/2412.20451)
- [CoA-VLA ICCV 2025 open access](https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html)
- [Diffusion-VLA (arXiv 2412.03293)](https://arxiv.org/abs/2412.03293)
- [Diffusion-VLA ICML 2025 poster](https://icml.cc/virtual/2025/poster/45061)
- [3D-AffordanceLLM (arXiv 2502.20041)](https://arxiv.org/abs/2502.20041)
- [3D-AffordanceLLM ICLR 2025 poster](https://iclr.cc/virtual/2025/poster/30275)
- [VLA Survey (arXiv 2507.01925)](https://arxiv.org/abs/2507.01925)
- [Context-Dependent Affordance (arXiv 2603.04419)](https://arxiv.org/abs/2603.04419)

agentId: a66259fb0faebd7b8 (use SendMessage with to: 'a66259fb0faebd7b8' to continue this agent)
&lt;usage>total_tokens: 19966
tool_uses: 9
duration_ms: 123669&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c177b3a6-b843-46a2-ba89-c9526a1f1c80",
  "isSidechain": false,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "type": "user",
  "uuid": "13db53e8-73fe-48c8-867e-79208db0a90a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify that the following paper references are real (correct titles, venues, and arXiv IDs). For each one, do a WebSearch to confirm. Report the verified title, venue, year, and whether the arXiv ID is correct.\n\nPapers to verify:\n1. \"CoT-VLA\" - arXiv 2503.22020 - claims visual subgoal tokens before action tokens, 17% real-world improvement\n2. \"SeqAfford\" - CVPR 2025 - arXiv 2412.01550 - sequential affordance reasoning for complex multi-step instructions, 180K instruction-point cloud pairs\n3. \"CoA-VLA\" - ICCV 2025 - structured affordance text (4 types) before action prediction\n4. \"Diffusion-VLA\" - ICML 2025 - arXiv 2412.03293 - reasoning text before diffusion action head\n5. \"3D-AffordanceLLM\" - ICLR 2025 - arXiv 2502.20041 - affordance detection as instruction reasoning\n6. VLA survey - arXiv 2507.01925 - identifies affordance as action token category\n7. Context-dependent affordance study - arXiv 2603.04419\n\nSearch for each one individually. Be precise about whether the title, venue, and year match. If any are wrong, provide the correct information.",
    "agentId": "a66259fb0faebd7b8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the verification report for all seven papers:\n\n---\n\n## Paper 1: CoT-VLA (arXiv 2503.22020)\n\n- **Verified title:** \"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models\"\n- **arXiv ID:** 2503.22020 -- **CORRECT**\n- **Venue/Year:** The arXiv preprint was posted March 2025. I did not find confirmation of acceptance at a specific conference in the search results (no venue was claimed in your query either).\n- **Claims check:** The paper does predict visual subgoal tokens (future image frames) before action tokens -- **CORRECT**. It reports a 17% improvement in real-world manipulation -- **CORRECT**.\n- **Verdict: ALL CLAIMS VERIFIED**\n\n---\n\n## Paper 2: SeqAfford (arXiv 2412.01550, CVPR 2025)\n\n- **Verified title:** \"SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model\"\n- **arXiv ID:** 2412.01550 -- **CORRECT**\n- **Venue/Year:** CVPR 2025 -- **CORRECT** (confirmed via the CVPR 2025 virtual site and the CVF open access repository)\n- **Claims check:** Sequential affordance reasoning for complex multi-step instructions -- **CORRECT**. 180K instruction-point cloud pairs -- **CORRECT**.\n- **Verdict: ALL CLAIMS VERIFIED**\n\n---\n\n## Paper 3: CoA-VLA (ICCV 2025)\n\n- **Verified title:** \"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance\"\n- **arXiv ID:** 2412.20451 (not provided in the original query, but confirmed)\n- **Venue/Year:** ICCV 2025 -- **CORRECT** (confirmed via the ICCV 2025 virtual site and CVF open access repository)\n- **Claims check:** Structured affordance text with 4 types (object, grasp, spatial, movement affordance) before action prediction -- **CORRECT**.\n- **Verdict: ALL CLAIMS VERIFIED**\n\n---\n\n## Paper 4: Diffusion-VLA (arXiv 2412.03293, ICML 2025)\n\n- **Verified title:** \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n- **arXiv ID:** 2412.03293 -- **CORRECT**\n- **Venue/Year:** ICML 2025 -- **CORRECT** (confirmed via the ICML 2025 virtual poster listing)\n- **Claims check:** Reasoning text before diffusion action head -- **CORRECT**. The model uses autoregressive reasoning (next-token prediction) followed by a diffusion model to generate actions.\n- **Note:** There is a separate paper called \"DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression\" also at ICML 2025. The arXiv ID 2412.03293 corresponds to the one with subtitle \"Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\" -- make sure you are referencing the correct one.\n- **Verdict: ALL CLAIMS VERIFIED**\n\n---\n\n## Paper 5: 3D-AffordanceLLM (arXiv 2502.20041, ICLR 2025)\n\n- **Verified title:** \"3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds\"\n- **arXiv ID:** 2502.20041 -- **CORRECT**\n- **Venue/Year:** ICLR 2025 -- **CORRECT** (confirmed via the ICLR 2025 poster listing and the PDF header stating \"Published as a conference paper at ICLR 2025\")\n- **Claims check:** Affordance detection reformulated as instruction reasoning (the \"IRAS\" task -- Instruction Reasoning Affordance Segmentation) -- **CORRECT**.\n- **Verdict: ALL CLAIMS VERIFIED**\n\n---\n\n## Paper 6: VLA Survey (arXiv 2507.01925)\n\n- **Verified title:** \"A Survey on Vision-Language-Action Models: An Action Tokenization Perspective\"\n- **arXiv ID:** 2507.01925 -- **CORRECT**\n- **Venue/Year:** arXiv preprint, July 2025. No specific conference venue claimed.\n- **Claims check:** The survey categorizes action tokens into types including: language description, code, **affordance**, trajectory, goal state, latent representation, raw action, and reasoning. So yes, it identifies affordance as an action token category -- **CORRECT**.\n- **Verdict: ALL CLAIMS VERIFIED**\n\n---\n\n## Paper 7: Context-Dependent Affordance Study (arXiv 2603.04419)\n\n- **Verified title:** \"Context-Dependent Affordance Computation in Vision-Language Models\"\n- **arXiv ID:** 2603.04419 -- **CORRECT**\n- **Venue/Year:** arXiv preprint, January 2026 (the 2603 prefix corresponds to March 2026 submission). No specific conference venue claimed.\n- **Claims check:** The paper studies context-dependent affordance computation in VLMs, demonstrating over 90% of lexical scene description is context-dependent (\"affordance drift\"). Author: Murad Farzulla (Dissensus AI / King's College London).\n- **Verdict: arXiv ID AND TITLE VERIFIED**\n\n---\n\n## Summary\n\n| # | Paper | Title Correct? | arXiv ID Correct? | Venue/Year Correct? | Key Claims Correct? |\n|---|-------|---------------|-------------------|---------------------|-------------------|\n| 1 | CoT-VLA | Yes | Yes (2503.22020) | No venue claimed | Yes (visual subgoal tokens, 17% improvement) |\n| 2 | SeqAfford | Yes | Yes (2412.01550) | Yes (CVPR 2025) | Yes (180K pairs, sequential reasoning) |\n| 3 | CoA-VLA | Yes | Not provided; actual ID is 2412.20451 | Yes (ICCV 2025) | Yes (4 affordance types) |\n| 4 | Diffusion-VLA | Yes | Yes (2412.03293) | Yes (ICML 2025) | Yes (reasoning then diffusion) |\n| 5 | 3D-AffordanceLLM | Yes | Yes (2502.20041) | Yes (ICLR 2025) | Yes (affordance as instruction reasoning) |\n| 6 | VLA Survey | Yes | Yes (2507.01925) | arXiv only (no venue) | Yes (affordance as token category) |\n| 7 | Context-dep. affordance | Yes | Yes (2603.04419) | arXiv only (no venue) | Yes |\n\n**All seven references are real papers with correct titles and arXiv IDs.** All claimed venues and years are confirmed accurate.\n\nSources:\n- [CoT-VLA (arXiv 2503.22020)](https://arxiv.org/abs/2503.22020)\n- [SeqAfford (arXiv 2412.01550)](https://arxiv.org/abs/2412.01550)\n- [SeqAfford CVPR 2025 poster](https://cvpr.thecvf.com/virtual/2025/poster/32496)\n- [CoA-VLA (arXiv 2412.20451)](https://arxiv.org/abs/2412.20451)\n- [CoA-VLA ICCV 2025 open access](https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html)\n- [Diffusion-VLA (arXiv 2412.03293)](https://arxiv.org/abs/2412.03293)\n- [Diffusion-VLA ICML 2025 poster](https://icml.cc/virtual/2025/poster/45061)\n- [3D-AffordanceLLM (arXiv 2502.20041)](https://arxiv.org/abs/2502.20041)\n- [3D-AffordanceLLM ICLR 2025 poster](https://iclr.cc/virtual/2025/poster/30275)\n- [VLA Survey (arXiv 2507.01925)](https://arxiv.org/abs/2507.01925)\n- [Context-Dependent Affordance (arXiv 2603.04419)](https://arxiv.org/abs/2603.04419)"
      }
    ],
    "totalDurationMs": 123669,
    "totalTokens": 19966,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1000,
      "cache_read_input_tokens": 16788,
      "output_tokens": 2177,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1000
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2177,
          "cache_read_input_tokens": 16788,
          "cache_creation_input_tokens": 1000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1000,
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
  "sourceToolAssistantUUID": "c177b3a6-b843-46a2-ba89-c9526a1f1c80",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T18:29:03.776Z_

<details><summary>↩ Tool result · `toolu_01LCgQhDqzj3Gs3gT3AoQbGC`</summary>

```text
Here is my comprehensive report on concurrent and recent work (2025-2026) on open-vocabulary affordance reasoning in Vision-Language-Action models.

---

## Landscape Analysis: Open-Vocabulary Affordance Reasoning in VLAs (2025-2026)

### MOST CLOSELY RELATED WORK (Highest Overlap)

#### 1. CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance
- **Authors:** Jinming Li, Yichen Zhu, Zhibin Tang, Junjie Wen, Minjie Zhu, Xiaoyu Liu, Chengmeng Li, Ran Cheng, Yaxin Peng, Yan Peng, Feifei Feng (Midea Group, Shanghai University, East China Normal University)
- **Venue/Date:** ICCV 2025 (arXiv Dec 2024)
- **Relevance: HIGH -- this is the most directly comparable work.** CoA-VLA generates a structured "chain of affordance" before action prediction, covering four affordance types: (1) object affordance, (2) grasp affordance, (3) spatial affordance, (4) movement affordance. Each affordance is represented in both visual and textual form and injected via a co-injection module. However, the affordance vocabulary is structured around four predefined categories rather than being truly open-vocabulary/free-form. The affordances also do not appear to be generated as autoregressive tokens in a unified sequence with action tokens -- they are injected via a separate module. This is a key architectural difference from a unified autoregressive approach.

#### 2. VLA-R1: Enhancing Reasoning in Vision-Language-Action Models
- **Authors:** GigaAI Research (project page: gigaai-research.github.io/VLA-R1)
- **Venue/Date:** arXiv October 2025
- **Relevance: HIGH.** VLA-R1 creates VLA-CoT-13K, a dataset with chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. It uses RLVR (Reinforcement Learning from Verifiable Rewards) with GRPO to optimize both reasoning and execution. The chain-of-thought includes affordance reasoning before actions. This is conceptually similar to generating affordance reasoning tokens before action tokens, though it uses RL-based post-training rather than a purely autoregressive generation approach, and its affordance reasoning is trained through supervised CoT + RL rather than emerging from a unified autoregressive objective.

#### 3. GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models
- **Authors:** Md Selim Sarowar, Omer Tariq, Sungho Kim
- **Venue/Date:** arXiv March 2026
- **Relevance: HIGH.** GST-VLA introduces a "Depth-Aware Chain-of-Thought" (DA-CoT) where the model explicitly generates four structured spatial reasoning steps before action generation: 3D object grounding, grasp affordance contact geometry, pairwise metric distances, and SE(3) motion plan waypoints. This is very close to the idea of generating intermediate affordance reasoning tokens before action tokens in an autoregressive sequence, but is specifically structured around 3D geometric affordances (not open-vocabulary), and uses 3D Gaussian spatial tokens rather than language tokens.

#### 4. ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models
- **Authors:** AgibotTech
- **Venue/Date:** CVPR 2026 (arXiv January 2026)
- **Relevance: HIGH.** ACoT-VLA formulates reasoning as a structured sequence of coarse action intents (explicit action reasoning) that guide the final policy. It has two components: an Explicit Action Reasoner (EAR) that proposes coarse reference trajectories as reasoning steps, and an Implicit Action Reasoner (IAR) that extracts latent action priors. The "chain of thought" here is action-level rather than affordance-level, and it is not open-vocabulary text reasoning -- it is structured trajectory-level reasoning.

---

### MODERATELY RELATED WORK

#### 5. CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models
- **Authors:** Zhao, Lu et al.
- **Venue/Date:** arXiv March 2025
- **Relevance: MODERATE.** Predicts future image frames autoregressively as visual goals before generating action sequences. The "reasoning" is visual (future frames) rather than affordance-based or language-based. Not open-vocabulary affordance reasoning.

#### 6. ST4VLA: Spatially Guided Training for Vision-Language-Action Models
- **Authors:** Jinhui Ye, Fangjing Wang (SUSTech), Ning Gao (Shanghai AI Lab)
- **Venue/Date:** arXiv February 2026
- **Relevance: MODERATE.** Uses spatial priors (point, box, trajectory) including affordance grounding to align the VLM planner, then conditions the action expert on these spatial priors. The affordance component is part of spatial training rather than being open-vocabulary affordance tokens in the autoregressive stream.

#### 7. ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning
- **Authors:** NVIDIA, National Taiwan University
- **Venue/Date:** arXiv July 2025
- **Relevance: MODERATE.** Generates embodied reasoning plans that are compressed into a visual plan latent before action execution. The reasoning is visual/latent rather than explicit open-vocabulary affordance tokens.

#### 8. LITEN: Learning Affordances at Inference-Time for VLAs
- **Authors:** UC Berkeley, Physical Intelligence
- **Venue/Date:** arXiv October 2025
- **Relevance: MODERATE.** Uses a high-level VLM to learn affordances of a low-level VLA at inference time through in-context learning from past execution experiences. This is about learning which instructions are high-affordance (achievable) rather than generating affordance reasoning tokens in-line.

#### 9. Affordance Field Intervention (AFI)
- **Authors:** (arXiv December 2025)
- **Venue/Date:** arXiv December 2025
- **Relevance: MODERATE.** A plug-in module that uses 3D Spatial Affordance Fields to guide VLA behavior under distribution shift. Not about generating affordance tokens autoregressively.

#### 10. AR-VLA: True Autoregressive Action Expert for VLA Models
- **Authors:** INSAIT (Sofia University), KU Leuven (Yutong Hu, Jan-Nico Zaech, et al.)
- **Venue/Date:** arXiv March 2026
- **Relevance: LOW-MODERATE.** Focuses on making the action generation truly autoregressive with a standalone action expert maintaining temporal context. No affordance reasoning component -- the contribution is about temporal autoregressive action consistency.

---

### PERIPHERAL WORK (Lower Overlap but Relevant Context)

#### 11. SG-VLA: Spatially-Grounded VLA Models for Mobile Manipulation
- **Venue/Date:** arXiv March 2026
- Co-trains auxiliary decoders for grasp affordances, target-object pose, and segmentation from shared features. Not autoregressive affordance token generation.

#### 12. GLOVER: Generalizable Open-Vocabulary Affordance Reasoning for Task-Oriented Grasping
- **Venue/Date:** 2025
- Open-vocabulary affordance but for grasping only, not a VLA with autoregressive token generation.

#### 13. 3D-AffordanceLLM: Open-Vocabulary Affordance Detection in 3D Worlds
- **Venue/Date:** arXiv February 2025
- Uses LLMs for open-vocabulary 3D affordance segmentation. Not a VLA or action generation model.

#### 14. Survey: A Survey on VLA Models: An Action Tokenization Perspective (arXiv July 2025)
- Categorizes VLA action token types including "affordance" as one distinct token category alongside language, code, trajectory, goal state, latent, raw action, and reasoning tokens. Useful framing paper.

---

### KEY FINDINGS AND GAP ANALYSIS

**No one is doing exactly what you describe.** The specific idea of "generating open-vocabulary affordance reasoning tokens before action tokens in a unified autoregressive VLA" has no exact match in the literature. Here is why:

1. **CoA-VLA** (the closest) uses structured affordance reasoning but with (a) a fixed taxonomy of 4 affordance types rather than open-vocabulary, and (b) a separate co-injection module rather than a unified autoregressive token sequence.

2. **VLA-R1** uses affordance-aligned CoT supervision but trains with RL post-training, not a purely unified autoregressive objective.

3. **GST-VLA** generates structured spatial reasoning (including affordance) before actions, but the affordance types are fixed (3D geometric) and the tokens are spatial Gaussian tokens, not open-vocabulary language tokens.

4. **ACoT-VLA** generates reasoning before actions autoregressively, but the reasoning is coarse action trajectories, not open-vocabulary affordance descriptions.

5. **No paper combines all three of:** (a) open-vocabulary/free-form affordance descriptions, (b) generated as autoregressive tokens in the same sequence, (c) preceding action tokens in a unified VLA architecture.

**The gap your idea fills:** Existing work either uses fixed affordance taxonomies (CoA-VLA), or generates non-affordance reasoning (CoT-VLA generates future frames, ACoT-VLA generates coarse trajectories), or uses separate modules for affordance injection rather than unifying it in the autoregressive stream. A truly open-vocabulary, autoregressive, in-stream affordance reasoning approach before action token generation appears to be novel.

**Caution:** The field is moving extremely fast (multiple new *-VLA papers per month in early 2026). CoA-VLA at ICCV 2025 and ACoT-VLA at CVPR 2026 establish the "reason before acting" paradigm for VLAs, so the conceptual foundation is clearly in the air. Differentiating on the "open-vocabulary" and "unified autoregressive" aspects will be critical.

---

Sources:
- [CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance (ICCV 2025)](https://arxiv.org/abs/2412.20451)
- [CoA-VLA Project Page](https://chain-of-affordance.github.io/)
- [VLA-R1: Enhancing Reasoning in Vision-Language-Action Models](https://arxiv.org/abs/2510.01623)
- [GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models](https://arxiv.org/abs/2603.09079)
- [ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models (CVPR 2026)](https://arxiv.org/abs/2601.11404)
- [CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](https://arxiv.org/pdf/2503.22020)
- [ST4VLA: Spatially Guided Training for Vision-Language-Action Models](https://arxiv.org/abs/2602.10109)
- [ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (NVIDIA)](https://arxiv.org/abs/2507.16815)
- [LITEN: Learning Affordances at Inference-Time for VLA Models](https://arxiv.org/abs/2510.19752)
- [Affordance Field Intervention: Enabling VLAs to Escape Memory Traps](https://arxiv.org/pdf/2512.07472)
- [AR-VLA: True Autoregressive Action Expert for VLA Models](https://arxiv.org/abs/2603.10126)
- [SG-VLA: Learning Spatially-Grounded VLA Models for Mobile Manipulation](https://arxiv.org/abs/2603.22760)
- [A Survey on VLA Models: An Action Tokenization Perspective](https://arxiv.org/abs/2507.01925)
- [3D-AffordanceLLM: Open-Vocabulary Affordance Detection in 3D Worlds](https://arxiv.org/pdf/2502.20041)
- [FASTer: Toward Efficient Autoregressive VLA Models](https://openreview.net/forum?id=k6nTUFoqeT)
- [GLOVER: Generalizable Open-Vocabulary Affordance Reasoning for Task-Oriented Grasping](https://corl25-genpriors.github.io/Papers/22_GLOVER_Generalizable_Open_V.pdf)
- [Awesome Embodied VLA Collection (GitHub)](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)

agentId: a479979600018ba92 (use SendMessage with to: 'a479979600018ba92' to continue this agent)
&lt;usage>total_tokens: 28507
tool_uses: 19
duration_ms: 129015&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9300e5b-7096-4a07-b0fe-a39b1a78e474",
  "isSidechain": false,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "type": "user",
  "uuid": "78a5d6c6-b388-42d7-a6c6-1da61af226e1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the web for concurrent and recent work (2025-2026) on open-vocabulary affordance reasoning in Vision-Language-Action models (VLAs). I need to know if anyone is already doing this or something very similar.\n\nPerform these searches:\n1. WebSearch: \"open-vocabulary affordance reasoning VLA 2026\"\n2. WebSearch: \"affordance tokens autoregressive VLA 2026\"\n3. WebSearch: \"chain of affordance VLA open vocabulary 2025 2026\"\n4. WebSearch: \"arXiv affordance VLA reasoning tokens 2025 2026\"\n5. WebSearch: \"openreview affordance VLA reasoning ICML NeurIPS ICLR 2026\"\n6. WebSearch: \"CoA-VLA open vocabulary affordance\"\n7. WebSearch: \"CoT-VLA affordance reasoning extension 2025 2026\"\n\nFor each result, note: title, authors, venue/date, and how it relates to \"generating open-vocabulary affordance reasoning tokens before action tokens in a unified autoregressive VLA.\" Report any highly similar concurrent work clearly. Be thorough.",
    "agentId": "a479979600018ba92",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my comprehensive report on concurrent and recent work (2025-2026) on open-vocabulary affordance reasoning in Vision-Language-Action models.\n\n---\n\n## Landscape Analysis: Open-Vocabulary Affordance Reasoning in VLAs (2025-2026)\n\n### MOST CLOSELY RELATED WORK (Highest Overlap)\n\n#### 1. CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance\n- **Authors:** Jinming Li, Yichen Zhu, Zhibin Tang, Junjie Wen, Minjie Zhu, Xiaoyu Liu, Chengmeng Li, Ran Cheng, Yaxin Peng, Yan Peng, Feifei Feng (Midea Group, Shanghai University, East China Normal University)\n- **Venue/Date:** ICCV 2025 (arXiv Dec 2024)\n- **Relevance: HIGH -- this is the most directly comparable work.** CoA-VLA generates a structured \"chain of affordance\" before action prediction, covering four affordance types: (1) object affordance, (2) grasp affordance, (3) spatial affordance, (4) movement affordance. Each affordance is represented in both visual and textual form and injected via a co-injection module. However, the affordance vocabulary is structured around four predefined categories rather than being truly open-vocabulary/free-form. The affordances also do not appear to be generated as autoregressive tokens in a unified sequence with action tokens -- they are injected via a separate module. This is a key architectural difference from a unified autoregressive approach.\n\n#### 2. VLA-R1: Enhancing Reasoning in Vision-Language-Action Models\n- **Authors:** GigaAI Research (project page: gigaai-research.github.io/VLA-R1)\n- **Venue/Date:** arXiv October 2025\n- **Relevance: HIGH.** VLA-R1 creates VLA-CoT-13K, a dataset with chain-of-thought supervision explicitly aligned with affordance and trajectory annotations. It uses RLVR (Reinforcement Learning from Verifiable Rewards) with GRPO to optimize both reasoning and execution. The chain-of-thought includes affordance reasoning before actions. This is conceptually similar to generating affordance reasoning tokens before action tokens, though it uses RL-based post-training rather than a purely autoregressive generation approach, and its affordance reasoning is trained through supervised CoT + RL rather than emerging from a unified autoregressive objective.\n\n#### 3. GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models\n- **Authors:** Md Selim Sarowar, Omer Tariq, Sungho Kim\n- **Venue/Date:** arXiv March 2026\n- **Relevance: HIGH.** GST-VLA introduces a \"Depth-Aware Chain-of-Thought\" (DA-CoT) where the model explicitly generates four structured spatial reasoning steps before action generation: 3D object grounding, grasp affordance contact geometry, pairwise metric distances, and SE(3) motion plan waypoints. This is very close to the idea of generating intermediate affordance reasoning tokens before action tokens in an autoregressive sequence, but is specifically structured around 3D geometric affordances (not open-vocabulary), and uses 3D Gaussian spatial tokens rather than language tokens.\n\n#### 4. ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\n- **Authors:** AgibotTech\n- **Venue/Date:** CVPR 2026 (arXiv January 2026)\n- **Relevance: HIGH.** ACoT-VLA formulates reasoning as a structured sequence of coarse action intents (explicit action reasoning) that guide the final policy. It has two components: an Explicit Action Reasoner (EAR) that proposes coarse reference trajectories as reasoning steps, and an Implicit Action Reasoner (IAR) that extracts latent action priors. The \"chain of thought\" here is action-level rather than affordance-level, and it is not open-vocabulary text reasoning -- it is structured trajectory-level reasoning.\n\n---\n\n### MODERATELY RELATED WORK\n\n#### 5. CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models\n- **Authors:** Zhao, Lu et al.\n- **Venue/Date:** arXiv March 2025\n- **Relevance: MODERATE.** Predicts future image frames autoregressively as visual goals before generating action sequences. The \"reasoning\" is visual (future frames) rather than affordance-based or language-based. Not open-vocabulary affordance reasoning.\n\n#### 6. ST4VLA: Spatially Guided Training for Vision-Language-Action Models\n- **Authors:** Jinhui Ye, Fangjing Wang (SUSTech), Ning Gao (Shanghai AI Lab)\n- **Venue/Date:** arXiv February 2026\n- **Relevance: MODERATE.** Uses spatial priors (point, box, trajectory) including affordance grounding to align the VLM planner, then conditions the action expert on these spatial priors. The affordance component is part of spatial training rather than being open-vocabulary affordance tokens in the autoregressive stream.\n\n#### 7. ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning\n- **Authors:** NVIDIA, National Taiwan University\n- **Venue/Date:** arXiv July 2025\n- **Relevance: MODERATE.** Generates embodied reasoning plans that are compressed into a visual plan latent before action execution. The reasoning is visual/latent rather than explicit open-vocabulary affordance tokens.\n\n#### 8. LITEN: Learning Affordances at Inference-Time for VLAs\n- **Authors:** UC Berkeley, Physical Intelligence\n- **Venue/Date:** arXiv October 2025\n- **Relevance: MODERATE.** Uses a high-level VLM to learn affordances of a low-level VLA at inference time through in-context learning from past execution experiences. This is about learning which instructions are high-affordance (achievable) rather than generating affordance reasoning tokens in-line.\n\n#### 9. Affordance Field Intervention (AFI)\n- **Authors:** (arXiv December 2025)\n- **Venue/Date:** arXiv December 2025\n- **Relevance: MODERATE.** A plug-in module that uses 3D Spatial Affordance Fields to guide VLA behavior under distribution shift. Not about generating affordance tokens autoregressively.\n\n#### 10. AR-VLA: True Autoregressive Action Expert for VLA Models\n- **Authors:** INSAIT (Sofia University), KU Leuven (Yutong Hu, Jan-Nico Zaech, et al.)\n- **Venue/Date:** arXiv March 2026\n- **Relevance: LOW-MODERATE.** Focuses on making the action generation truly autoregressive with a standalone action expert maintaining temporal context. No affordance reasoning component -- the contribution is about temporal autoregressive action consistency.\n\n---\n\n### PERIPHERAL WORK (Lower Overlap but Relevant Context)\n\n#### 11. SG-VLA: Spatially-Grounded VLA Models for Mobile Manipulation\n- **Venue/Date:** arXiv March 2026\n- Co-trains auxiliary decoders for grasp affordances, target-object pose, and segmentation from shared features. Not autoregressive affordance token generation.\n\n#### 12. GLOVER: Generalizable Open-Vocabulary Affordance Reasoning for Task-Oriented Grasping\n- **Venue/Date:** 2025\n- Open-vocabulary affordance but for grasping only, not a VLA with autoregressive token generation.\n\n#### 13. 3D-AffordanceLLM: Open-Vocabulary Affordance Detection in 3D Worlds\n- **Venue/Date:** arXiv February 2025\n- Uses LLMs for open-vocabulary 3D affordance segmentation. Not a VLA or action generation model.\n\n#### 14. Survey: A Survey on VLA Models: An Action Tokenization Perspective (arXiv July 2025)\n- Categorizes VLA action token types including \"affordance\" as one distinct token category alongside language, code, trajectory, goal state, latent, raw action, and reasoning tokens. Useful framing paper.\n\n---\n\n### KEY FINDINGS AND GAP ANALYSIS\n\n**No one is doing exactly what you describe.** The specific idea of \"generating open-vocabulary affordance reasoning tokens before action tokens in a unified autoregressive VLA\" has no exact match in the literature. Here is why:\n\n1. **CoA-VLA** (the closest) uses structured affordance reasoning but with (a) a fixed taxonomy of 4 affordance types rather than open-vocabulary, and (b) a separate co-injection module rather than a unified autoregressive token sequence.\n\n2. **VLA-R1** uses affordance-aligned CoT supervision but trains with RL post-training, not a purely unified autoregressive objective.\n\n3. **GST-VLA** generates structured spatial reasoning (including affordance) before actions, but the affordance types are fixed (3D geometric) and the tokens are spatial Gaussian tokens, not open-vocabulary language tokens.\n\n4. **ACoT-VLA** generates reasoning before actions autoregressively, but the reasoning is coarse action trajectories, not open-vocabulary affordance descriptions.\n\n5. **No paper combines all three of:** (a) open-vocabulary/free-form affordance descriptions, (b) generated as autoregressive tokens in the same sequence, (c) preceding action tokens in a unified VLA architecture.\n\n**The gap your idea fills:** Existing work either uses fixed affordance taxonomies (CoA-VLA), or generates non-affordance reasoning (CoT-VLA generates future frames, ACoT-VLA generates coarse trajectories), or uses separate modules for affordance injection rather than unifying it in the autoregressive stream. A truly open-vocabulary, autoregressive, in-stream affordance reasoning approach before action token generation appears to be novel.\n\n**Caution:** The field is moving extremely fast (multiple new *-VLA papers per month in early 2026). CoA-VLA at ICCV 2025 and ACoT-VLA at CVPR 2026 establish the \"reason before acting\" paradigm for VLAs, so the conceptual foundation is clearly in the air. Differentiating on the \"open-vocabulary\" and \"unified autoregressive\" aspects will be critical.\n\n---\n\nSources:\n- [CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance (ICCV 2025)](https://arxiv.org/abs/2412.20451)\n- [CoA-VLA Project Page](https://chain-of-affordance.github.io/)\n- [VLA-R1: Enhancing Reasoning in Vision-Language-Action Models](https://arxiv.org/abs/2510.01623)\n- [GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models](https://arxiv.org/abs/2603.09079)\n- [ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models (CVPR 2026)](https://arxiv.org/abs/2601.11404)\n- [CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models](https://arxiv.org/pdf/2503.22020)\n- [ST4VLA: Spatially Guided Training for Vision-Language-Action Models](https://arxiv.org/abs/2602.10109)\n- [ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (NVIDIA)](https://arxiv.org/abs/2507.16815)\n- [LITEN: Learning Affordances at Inference-Time for VLA Models](https://arxiv.org/abs/2510.19752)\n- [Affordance Field Intervention: Enabling VLAs to Escape Memory Traps](https://arxiv.org/pdf/2512.07472)\n- [AR-VLA: True Autoregressive Action Expert for VLA Models](https://arxiv.org/abs/2603.10126)\n- [SG-VLA: Learning Spatially-Grounded VLA Models for Mobile Manipulation](https://arxiv.org/abs/2603.22760)\n- [A Survey on VLA Models: An Action Tokenization Perspective](https://arxiv.org/abs/2507.01925)\n- [3D-AffordanceLLM: Open-Vocabulary Affordance Detection in 3D Worlds](https://arxiv.org/pdf/2502.20041)\n- [FASTer: Toward Efficient Autoregressive VLA Models](https://openreview.net/forum?id=k6nTUFoqeT)\n- [GLOVER: Generalizable Open-Vocabulary Affordance Reasoning for Task-Oriented Grasping](https://corl25-genpriors.github.io/Papers/22_GLOVER_Generalizable_Open_V.pdf)\n- [Awesome Embodied VLA Collection (GitHub)](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln)"
      }
    ],
    "totalDurationMs": 129015,
    "totalTokens": 28507,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1484,
      "cache_creation_input_tokens": 1111,
      "cache_read_input_tokens": 22705,
      "output_tokens": 3207,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1111
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1484,
          "output_tokens": 3207,
          "cache_read_input_tokens": 22705,
          "cache_creation_input_tokens": 1111,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1111,
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
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "f9300e5b-7096-4a07-b0fe-a39b1a78e474",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-18 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.  {   \"title\": \"Open-Vocabula…",
  "leafUuid": "78a5d6c6-b388-42d7-a6c6-1da61af226e1",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Open-vocabulary affordance tokens in autoregressive VLA",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Tool result

_source line 24 · 2026-05-18T18:29:33.563Z_

<details><summary>↩ Tool result · `toolu_01M4QPxPcoFzmooMzy2D6HET`</summary>

```text
Here is the consolidated feasibility and cost report for your VLA research project.

---

## 1. Available Open-Source VLA Codebases

**Primary codebases to build on:**

| Repository | Description | Scale | Status |
|---|---|---|---|
| [OpenVLA](https://github.com/openvla/openvla) | The canonical open-source 7B VLA (Prismatic VLM + action tokenization). Fully open weights on HuggingFace, PyTorch training pipeline. | 7B | Mature, actively maintained |
| [OpenVLA-OFT](https://github.com/moojink/openvla-oft) | Optimized fine-tuning variant of OpenVLA with improved speed and success rates. | 7B | Mature |
| [ACoT-VLA](https://github.com/AgibotTech/ACoT-VLA) | Action Chain-of-Thought for VLAs (CVPR 2026). Introduces Explicit Action Reasoner (coarse reference trajectories) and Implicit Action Reasoner. | 7B | Recent release |
| [Embodied CoT (ECoT)](https://github.com/MichalZawalski/embodied-CoT) | Chain-of-thought reasoning injected into a robotic policy. | 7B | Available |
| [OpenPi (pi0)](https://github.com/Physical-Intelligence/openpi) | Physical Intelligence's open implementation. Flow-based diffusion VLA. | 450M (base) | Open weights on HF |
| [open-pi-zero](https://github.com/allenzren/open-pi-zero) | Community re-implementation of pi0. | 450M | Community maintained |
| [SimpleVLA-RL](https://github.com/PRIME-RL/SimpleVLA-RL) | ICLR 2026. RL-based post-training for VLAs, builds on veRL. Achieves 97.6 on LIBERO-Long. | 7B | Recent release |
| [VLA-RL](https://github.com/GuanxingLu/vlarl) | Single-file RL implementation for advancing VLAs. | Various | Available |
| [VLA-R1](https://github.com/GigaAI-research/VLA-R1) | Enhanced reasoning in VLAs. | 7B | Available |
| [Affordance Flow Matching](https://github.com/HRI-EU/flow_matching) | Affordance-based robot manipulation with flow matching. | Smaller | Available |

**CoA-VLA (Chain-of-Affordance):** This is the closest prior art to your proposed approach (prompting four affordance types -- object, grasp, spatial, movement -- before acting). The paper was published at ICCV 2025 with a [project page](https://chain-of-affordance.github.io/) and [arXiv paper](https://arxiv.org/abs/2412.20451). However, no public GitHub repository for CoA-VLA was found in the search results. This means your project would likely need to reimplement the affordance reasoning module or build it from scratch on top of OpenVLA/OpenVLA-OFT.

**Recommendation:** OpenVLA or OpenVLA-OFT is the strongest starting point. They provide a 7B VLM backbone with an established action tokenization pipeline, and the community has accumulated 100+ fine-tuning experiments worth of practical knowledge.

---

## 2. Typical GPU Hours for VLA Training (7B-13B Scale)

**Pre-training from scratch (7B):**
- OpenVLA was trained on **64 A100 GPUs for 14 days**, totaling approximately **21,500 A100-hours**.
- This is prohibitively expensive for most research labs. The consensus is to start from an existing checkpoint.

**Full fine-tuning (7B):**
- **8 A100 GPUs for 5-15 hours per task**, depending on dataset size.
- Approximately **40-120 A100-hours per task domain**.

**LoRA fine-tuning (7B) -- recommended approach:**
- **1 A100 GPU for 10-15 hours** (LoRA rank 32, alpha 64).
- **4-6 GPU-hours on an H100 80GB** for a 10,000-step dataset.
- Cost: **$50-200 per training run** in cloud compute.
- 8x compute reduction vs. full fine-tuning.

**General LLM fine-tuning benchmarks (7B):**
- A 7B parameter model typically consumes **40-80 GPU hours on A100** for comprehensive fine-tuning, translating to **$100-$256 per iteration**.

**For your project specifically (affordance reasoning tokens + action tokens):**
- Adding an affordance reasoning prefix before action tokens increases sequence length, which increases compute roughly linearly with the added token count.
- Expect approximately **1.5-2x the standard fine-tuning cost** due to the longer output sequences.
- Budget estimate: **20-40 A100-hours for LoRA fine-tuning**, **80-200 A100-hours for full fine-tuning** per task domain.

---

## 3. Available Robot Manipulation Datasets

| Dataset | Size | Format | Access |
|---|---|---|---|
| [Open X-Embodiment](https://huggingface.co/datasets/jxu124/OpenX-Embodiment) | **1M+ trajectories**, 22 robot embodiments | RLDS (TF) / HuggingFace | Free. HuggingFace streaming supported. Also at [google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment). |
| [OpenX-LeRobot](https://huggingface.co/collections/lerobot/open-x-embodiment) | Same data, LeRobot-compatible format | LeRobot | Free. HuggingFace collection. |
| [DROID](https://droid-dataset.github.io/) | **76k trajectories / 350 hours**, 564 scenes, 86 tasks | RLDS (1.7TB) or raw MP4 (8.7TB) | Free via `gsutil`. Also [lerobot/droid_100](https://huggingface.co/datasets/lerobot/droid_100) (100-episode subset, 2GB). |
| [ShareRobot (BAAI)](https://huggingface.co/datasets/BAAI/ShareRobot) | 6,522 images with affordance labels, 6,870 images with coordinate annotations | HuggingFace | Free. Includes affordance area annotations aligned with instructions. |
| [RoboInter-Data](https://huggingface.co/datasets/InternRobotics/RoboInter-Data) | Comprehensive multi-annotation dataset | HuggingFace | Free. Includes affordance bounding boxes, gripper poses, trajectory traces. |
| [RoboBrain Affordance LoRA](https://huggingface.co/BAAI/RoboBrain-LoRA-Affordance) | LoRA adapter for affordance prediction | HuggingFace model | Free. Pre-trained affordance LoRA. |
| [NVIDIA PhysicalAI Manipulation](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Manipulation-Augmented) | 1,000 demos (synthetic, Franka Panda) | HuggingFace | Free. |
| [NVIDIA GR00T X-Embodiment Sim](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim) | Simulated cross-embodiment data | HuggingFace | Free. |

**Key note for your project:** ShareRobot and RoboInter-Data are particularly relevant because they include explicit affordance annotations (object affordance areas, grasp points, spatial coordinates), which you will need for training the affordance reasoning tokens. Open X-Embodiment and DROID provide the scale but will require you to generate affordance labels (likely via a VLM annotation pipeline or manual annotation).

---

## 4. Current A100 GPU Rental Costs (May 2026)

| Tier | Provider Examples | A100 80GB Price/hr |
|---|---|---|
| Budget marketplace | Vast.ai | **$0.72-0.78/hr** |
| Decentralized/specialized | ThunderCompute, others | **$0.96-1.29/hr** |
| Mid-range | Jarvislabs, RunPod | **$1.35-1.49/hr** |
| Established cloud | Lambda Labs | **$2.06/hr** |
| Hyperscalers | AWS, Azure (8-GPU instances only) | **$3.40-3.43/GPU/hr** |

**H100 pricing for comparison:** $2.85-3.50/hr (dropped from $8/hr at launch), with AWS P5 instances cut by 44% in June 2025.

**Budget projections for your project:**

| Scenario | GPU Hours | Cost (budget tier) | Cost (mid-range) |
|---|---|---|---|
| LoRA fine-tune, single task | 15-30 hrs | $11-23 | $20-45 |
| LoRA fine-tune, multi-task (5 domains) | 75-150 hrs | $54-117 | $101-224 |
| Full fine-tune, single task | 80-200 hrs | $58-156 | $108-298 |
| Full fine-tune + hyperparameter search | 400-1000 hrs | $288-780 | $540-1,490 |
| Pre-training from scratch (NOT recommended) | ~21,500 hrs | $15,480+ | $29,025+ |

---

## 5. Known Failure Modes and Challenges in VLA Training

**Action tokenization failures:**
- Standard per-dimension, per-timestep binning **fails completely** on high-frequency or dexterous tasks. The FAST tokenization method (DCT-based, compression-inspired) addresses this but adds implementation complexity.

**LoRA overfitting:**
- LoRA adapters overfit quickly on small datasets. Early stopping on held-out *success rate* (not loss) is critical. LoRA rank 16-32 works for most tasks; rank 8 underfits on bimanual tasks, rank 64 overfits on small datasets.

**Action normalization mismatches:**
- Policies can look good on paper metrics but fail on hardware due to normalization mismatches between training and deployment.

**Camera calibration drift:**
- Extrinsic camera calibration wanders over months, requiring re-calibration before every major data collection run.

**Episode segmentation errors:**
- Mis-segmented episodes in datasets cause the model to learn incorrect transition boundaries. Real time must be spent on boundary review.

**Long-horizon performance:**
- Long-horizon household manipulation achieves only ~26% success even with extensive engineering.

**Depth and 3D reasoning:**
- Most VLAs ignore explicit depth information. Approximating depth from visual frames loses sensitivity with object size, distance, and fine movement.

**Smaller model training failure:**
- Attempts to train smaller VLA models from scratch have **failed completely**. Pre-trained backbones (7B+) are essential.

**Recovery data scarcity:**
- Pure learning struggles with lack of recovery data. Failures during deployment are poorly represented in demonstration-only datasets.

**Affordance-specific challenge for your project:**
- CoA-VLA's four affordance types (object, grasp, spatial, movement) in both visual and textual formats required a novel "vision-language co-injection module." Generating high-quality affordance supervision labels at scale is a bottleneck -- you will likely need a VLM-in-the-loop annotation pipeline to label Open X-Embodiment/DROID data with affordance reasoning chains.

---

## Summary Assessment

**Feasibility:** High. The ecosystem is mature enough that fine-tuning a 7B VLA with affordance reasoning tokens is tractable. OpenVLA/OpenVLA-OFT provides a solid base, and ACoT-VLA/ECoT demonstrate that chain-of-thought reasoning integration works in VLAs. The main novel contribution would be the open-vocabulary affordance token generation, for which CoA-VLA provides conceptual grounding but no open code.

**Estimated total cost for a research project:** $500-3,000 in GPU compute (using mid-range providers with LoRA fine-tuning, multiple experimental runs, hyperparameter search). This assumes starting from OpenVLA checkpoints, not training from scratch.

**Biggest risk:** Generating high-quality affordance reasoning supervision data at scale for the Open X-Embodiment/DROID datasets, and ensuring the affordance tokens actually improve downstream action quality rather than just adding latency.

Sources:
- [OpenVLA GitHub](https://github.com/openvla/openvla)
- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)
- [ACoT-VLA GitHub (CVPR 2026)](https://github.com/AgibotTech/ACoT-VLA)
- [Embodied CoT GitHub](https://github.com/MichalZawalski/embodied-CoT)
- [SimpleVLA-RL GitHub (ICLR 2026)](https://github.com/PRIME-RL/SimpleVLA-RL)
- [VLA-R1 GitHub](https://github.com/GigaAI-research/VLA-R1)
- [OpenPi GitHub](https://github.com/Physical-Intelligence/openpi)
- [CoA-VLA Project Page](https://chain-of-affordance.github.io/)
- [CoA-VLA Paper](https://arxiv.org/abs/2412.20451)
- [Open X-Embodiment on HuggingFace](https://huggingface.co/datasets/jxu124/OpenX-Embodiment)
- [Open X-Embodiment GitHub](https://github.com/google-deepmind/open_x_embodiment)
- [DROID Dataset](https://droid-dataset.github.io/)
- [ShareRobot Dataset](https://huggingface.co/datasets/BAAI/ShareRobot)
- [RoboInter-Data](https://huggingface.co/datasets/InternRobotics/RoboInter-Data)
- [RoboBrain Affordance LoRA](https://huggingface.co/BAAI/RoboBrain-LoRA-Affordance)
- [FAST Action Tokenization Paper](https://arxiv.org/pdf/2501.09747)
- [10 Open Challenges for VLAs](https://arxiv.org/pdf/2511.05936)
- [Scaling VLA Training on a Budget](https://www.roboticscenter.ai/blog/scaling-vla-training-on-a-budget)
- [A100 Pricing Comparison (2026)](https://getdeploying.com/gpus/nvidia-a100)
- [A100 Price Guide (Jarvislabs)](https://jarvislabs.ai/blog/a100-price)
- [A100 Pricing (ThunderCompute)](https://www.thundercompute.com/blog/nvidia-a100-pricing)
- [OpenVLA Paper](https://arxiv.org/html/2406.09246v3)
- [Awesome VLA Post-Training](https://github.com/AoqunJin/Awesome-VLA-Post-Training)
- [VLA Survey Paper](https://arxiv.org/abs/2505.04769)
- [OpenVLA Deployment Guide (Spheron)](https://www.spheron.network/blog/deploy-openvla-gpu-cloud/)

agentId: ace4ac5c5fdd44b54 (use SendMessage with to: 'ace4ac5c5fdd44b54' to continue this agent)
&lt;usage>total_tokens: 28198
tool_uses: 17
duration_ms: 136530&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2f23a13-d214-4365-839c-9f2b3b56daf7",
  "isSidechain": false,
  "promptId": "d55f5b67-f828-48f6-8580-f2cc71e420b6",
  "type": "user",
  "uuid": "cb6356e5-60c6-461a-829a-cd7cc47e41cd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to ground the feasibility and cost estimates for a research project that:\n- Fine-tunes a VLA (Vision-Language-Action) model to generate open-vocabulary affordance reasoning tokens before action tokens\n- Uses a multimodal LLM backbone (7B-13B parameters)\n- Trains on robot manipulation datasets (Open X-Embodiment, DROID, etc.)\n\nSearch for:\n\n1. WebSearch: \"github.com VLA training code affordance\"\n2. WebSearch: \"github.com CoT-VLA implementation code\"\n3. WebSearch: \"github.com CoA-VLA implementation\"\n4. WebSearch: \"OpenVLA training cost GPU hours A100\"\n5. WebSearch: \"VLA fine-tuning cost GPU hours 2025 2026\"\n6. WebSearch: \"Open X-Embodiment dataset huggingface download\"\n7. WebSearch: \"DROID robot dataset access download\"\n8. WebSearch: \"huggingface datasets robot manipulation affordance\"\n9. WebSearch: \"A100 GPU rental cost per hour 2026\"\n10. WebSearch: \"VLA training 7B parameters GPU hours\"\n\nReport:\n- Available open-source VLA codebases on GitHub\n- Typical GPU hours for VLA training (7B-13B scale)\n- Available robot manipulation datasets and their accessibility\n- Current A100 GPU rental costs (per hour)\n- Any known failure modes or challenges in VLA training",
    "agentId": "ace4ac5c5fdd44b54",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the consolidated feasibility and cost report for your VLA research project.\n\n---\n\n## 1. Available Open-Source VLA Codebases\n\n**Primary codebases to build on:**\n\n| Repository | Description | Scale | Status |\n|---|---|---|---|\n| [OpenVLA](https://github.com/openvla/openvla) | The canonical open-source 7B VLA (Prismatic VLM + action tokenization). Fully open weights on HuggingFace, PyTorch training pipeline. | 7B | Mature, actively maintained |\n| [OpenVLA-OFT](https://github.com/moojink/openvla-oft) | Optimized fine-tuning variant of OpenVLA with improved speed and success rates. | 7B | Mature |\n| [ACoT-VLA](https://github.com/AgibotTech/ACoT-VLA) | Action Chain-of-Thought for VLAs (CVPR 2026). Introduces Explicit Action Reasoner (coarse reference trajectories) and Implicit Action Reasoner. | 7B | Recent release |\n| [Embodied CoT (ECoT)](https://github.com/MichalZawalski/embodied-CoT) | Chain-of-thought reasoning injected into a robotic policy. | 7B | Available |\n| [OpenPi (pi0)](https://github.com/Physical-Intelligence/openpi) | Physical Intelligence's open implementation. Flow-based diffusion VLA. | 450M (base) | Open weights on HF |\n| [open-pi-zero](https://github.com/allenzren/open-pi-zero) | Community re-implementation of pi0. | 450M | Community maintained |\n| [SimpleVLA-RL](https://github.com/PRIME-RL/SimpleVLA-RL) | ICLR 2026. RL-based post-training for VLAs, builds on veRL. Achieves 97.6 on LIBERO-Long. | 7B | Recent release |\n| [VLA-RL](https://github.com/GuanxingLu/vlarl) | Single-file RL implementation for advancing VLAs. | Various | Available |\n| [VLA-R1](https://github.com/GigaAI-research/VLA-R1) | Enhanced reasoning in VLAs. | 7B | Available |\n| [Affordance Flow Matching](https://github.com/HRI-EU/flow_matching) | Affordance-based robot manipulation with flow matching. | Smaller | Available |\n\n**CoA-VLA (Chain-of-Affordance):** This is the closest prior art to your proposed approach (prompting four affordance types -- object, grasp, spatial, movement -- before acting). The paper was published at ICCV 2025 with a [project page](https://chain-of-affordance.github.io/) and [arXiv paper](https://arxiv.org/abs/2412.20451). However, no public GitHub repository for CoA-VLA was found in the search results. This means your project would likely need to reimplement the affordance reasoning module or build it from scratch on top of OpenVLA/OpenVLA-OFT.\n\n**Recommendation:** OpenVLA or OpenVLA-OFT is the strongest starting point. They provide a 7B VLM backbone with an established action tokenization pipeline, and the community has accumulated 100+ fine-tuning experiments worth of practical knowledge.\n\n---\n\n## 2. Typical GPU Hours for VLA Training (7B-13B Scale)\n\n**Pre-training from scratch (7B):**\n- OpenVLA was trained on **64 A100 GPUs for 14 days**, totaling approximately **21,500 A100-hours**.\n- This is prohibitively expensive for most research labs. The consensus is to start from an existing checkpoint.\n\n**Full fine-tuning (7B):**\n- **8 A100 GPUs for 5-15 hours per task**, depending on dataset size.\n- Approximately **40-120 A100-hours per task domain**.\n\n**LoRA fine-tuning (7B) -- recommended approach:**\n- **1 A100 GPU for 10-15 hours** (LoRA rank 32, alpha 64).\n- **4-6 GPU-hours on an H100 80GB** for a 10,000-step dataset.\n- Cost: **$50-200 per training run** in cloud compute.\n- 8x compute reduction vs. full fine-tuning.\n\n**General LLM fine-tuning benchmarks (7B):**\n- A 7B parameter model typically consumes **40-80 GPU hours on A100** for comprehensive fine-tuning, translating to **$100-$256 per iteration**.\n\n**For your project specifically (affordance reasoning tokens + action tokens):**\n- Adding an affordance reasoning prefix before action tokens increases sequence length, which increases compute roughly linearly with the added token count.\n- Expect approximately **1.5-2x the standard fine-tuning cost** due to the longer output sequences.\n- Budget estimate: **20-40 A100-hours for LoRA fine-tuning**, **80-200 A100-hours for full fine-tuning** per task domain.\n\n---\n\n## 3. Available Robot Manipulation Datasets\n\n| Dataset | Size | Format | Access |\n|---|---|---|---|\n| [Open X-Embodiment](https://huggingface.co/datasets/jxu124/OpenX-Embodiment) | **1M+ trajectories**, 22 robot embodiments | RLDS (TF) / HuggingFace | Free. HuggingFace streaming supported. Also at [google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment). |\n| [OpenX-LeRobot](https://huggingface.co/collections/lerobot/open-x-embodiment) | Same data, LeRobot-compatible format | LeRobot | Free. HuggingFace collection. |\n| [DROID](https://droid-dataset.github.io/) | **76k trajectories / 350 hours**, 564 scenes, 86 tasks | RLDS (1.7TB) or raw MP4 (8.7TB) | Free via `gsutil`. Also [lerobot/droid_100](https://huggingface.co/datasets/lerobot/droid_100) (100-episode subset, 2GB). |\n| [ShareRobot (BAAI)](https://huggingface.co/datasets/BAAI/ShareRobot) | 6,522 images with affordance labels, 6,870 images with coordinate annotations | HuggingFace | Free. Includes affordance area annotations aligned with instructions. |\n| [RoboInter-Data](https://huggingface.co/datasets/InternRobotics/RoboInter-Data) | Comprehensive multi-annotation dataset | HuggingFace | Free. Includes affordance bounding boxes, gripper poses, trajectory traces. |\n| [RoboBrain Affordance LoRA](https://huggingface.co/BAAI/RoboBrain-LoRA-Affordance) | LoRA adapter for affordance prediction | HuggingFace model | Free. Pre-trained affordance LoRA. |\n| [NVIDIA PhysicalAI Manipulation](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-Manipulation-Augmented) | 1,000 demos (synthetic, Franka Panda) | HuggingFace | Free. |\n| [NVIDIA GR00T X-Embodiment Sim](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim) | Simulated cross-embodiment data | HuggingFace | Free. |\n\n**Key note for your project:** ShareRobot and RoboInter-Data are particularly relevant because they include explicit affordance annotations (object affordance areas, grasp points, spatial coordinates), which you will need for training the affordance reasoning tokens. Open X-Embodiment and DROID provide the scale but will require you to generate affordance labels (likely via a VLM annotation pipeline or manual annotation).\n\n---\n\n## 4. Current A100 GPU Rental Costs (May 2026)\n\n| Tier | Provider Examples | A100 80GB Price/hr |\n|---|---|---|\n| Budget marketplace | Vast.ai | **$0.72-0.78/hr** |\n| Decentralized/specialized | ThunderCompute, others | **$0.96-1.29/hr** |\n| Mid-range | Jarvislabs, RunPod | **$1.35-1.49/hr** |\n| Established cloud | Lambda Labs | **$2.06/hr** |\n| Hyperscalers | AWS, Azure (8-GPU instances only) | **$3.40-3.43/GPU/hr** |\n\n**H100 pricing for comparison:** $2.85-3.50/hr (dropped from $8/hr at launch), with AWS P5 instances cut by 44% in June 2025.\n\n**Budget projections for your project:**\n\n| Scenario | GPU Hours | Cost (budget tier) | Cost (mid-range) |\n|---|---|---|---|\n| LoRA fine-tune, single task | 15-30 hrs | $11-23 | $20-45 |\n| LoRA fine-tune, multi-task (5 domains) | 75-150 hrs | $54-117 | $101-224 |\n| Full fine-tune, single task | 80-200 hrs | $58-156 | $108-298 |\n| Full fine-tune + hyperparameter search | 400-1000 hrs | $288-780 | $540-1,490 |\n| Pre-training from scratch (NOT recommended) | ~21,500 hrs | $15,480+ | $29,025+ |\n\n---\n\n## 5. Known Failure Modes and Challenges in VLA Training\n\n**Action tokenization failures:**\n- Standard per-dimension, per-timestep binning **fails completely** on high-frequency or dexterous tasks. The FAST tokenization method (DCT-based, compression-inspired) addresses this but adds implementation complexity.\n\n**LoRA overfitting:**\n- LoRA adapters overfit quickly on small datasets. Early stopping on held-out *success rate* (not loss) is critical. LoRA rank 16-32 works for most tasks; rank 8 underfits on bimanual tasks, rank 64 overfits on small datasets.\n\n**Action normalization mismatches:**\n- Policies can look good on paper metrics but fail on hardware due to normalization mismatches between training and deployment.\n\n**Camera calibration drift:**\n- Extrinsic camera calibration wanders over months, requiring re-calibration before every major data collection run.\n\n**Episode segmentation errors:**\n- Mis-segmented episodes in datasets cause the model to learn incorrect transition boundaries. Real time must be spent on boundary review.\n\n**Long-horizon performance:**\n- Long-horizon household manipulation achieves only ~26% success even with extensive engineering.\n\n**Depth and 3D reasoning:**\n- Most VLAs ignore explicit depth information. Approximating depth from visual frames loses sensitivity with object size, distance, and fine movement.\n\n**Smaller model training failure:**\n- Attempts to train smaller VLA models from scratch have **failed completely**. Pre-trained backbones (7B+) are essential.\n\n**Recovery data scarcity:**\n- Pure learning struggles with lack of recovery data. Failures during deployment are poorly represented in demonstration-only datasets.\n\n**Affordance-specific challenge for your project:**\n- CoA-VLA's four affordance types (object, grasp, spatial, movement) in both visual and textual formats required a novel \"vision-language co-injection module.\" Generating high-quality affordance supervision labels at scale is a bottleneck -- you will likely need a VLM-in-the-loop annotation pipeline to label Open X-Embodiment/DROID data with affordance reasoning chains.\n\n---\n\n## Summary Assessment\n\n**Feasibility:** High. The ecosystem is mature enough that fine-tuning a 7B VLA with affordance reasoning tokens is tractable. OpenVLA/OpenVLA-OFT provides a solid base, and ACoT-VLA/ECoT demonstrate that chain-of-thought reasoning integration works in VLAs. The main novel contribution would be the open-vocabulary affordance token generation, for which CoA-VLA provides conceptual grounding but no open code.\n\n**Estimated total cost for a research project:** $500-3,000 in GPU compute (using mid-range providers with LoRA fine-tuning, multiple experimental runs, hyperparameter search). This assumes starting from OpenVLA checkpoints, not training from scratch.\n\n**Biggest risk:** Generating high-quality affordance reasoning supervision data at scale for the Open X-Embodiment/DROID datasets, and ensuring the affordance tokens actually improve downstream action quality rather than just adding latency.\n\nSources:\n- [OpenVLA GitHub](https://github.com/openvla/openvla)\n- [OpenVLA-OFT GitHub](https://github.com/moojink/openvla-oft)\n- [ACoT-VLA GitHub (CVPR 2026)](https://github.com/AgibotTech/ACoT-VLA)\n- [Embodied CoT GitHub](https://github.com/MichalZawalski/embodied-CoT)\n- [SimpleVLA-RL GitHub (ICLR 2026)](https://github.com/PRIME-RL/SimpleVLA-RL)\n- [VLA-R1 GitHub](https://github.com/GigaAI-research/VLA-R1)\n- [OpenPi GitHub](https://github.com/Physical-Intelligence/openpi)\n- [CoA-VLA Project Page](https://chain-of-affordance.github.io/)\n- [CoA-VLA Paper](https://arxiv.org/abs/2412.20451)\n- [Open X-Embodiment on HuggingFace](https://huggingface.co/datasets/jxu124/OpenX-Embodiment)\n- [Open X-Embodiment GitHub](https://github.com/google-deepmind/open_x_embodiment)\n- [DROID Dataset](https://droid-dataset.github.io/)\n- [ShareRobot Dataset](https://huggingface.co/datasets/BAAI/ShareRobot)\n- [RoboInter-Data](https://huggingface.co/datasets/InternRobotics/RoboInter-Data)\n- [RoboBrain Affordance LoRA](https://huggingface.co/BAAI/RoboBrain-LoRA-Affordance)\n- [FAST Action Tokenization Paper](https://arxiv.org/pdf/2501.09747)\n- [10 Open Challenges for VLAs](https://arxiv.org/pdf/2511.05936)\n- [Scaling VLA Training on a Budget](https://www.roboticscenter.ai/blog/scaling-vla-training-on-a-budget)\n- [A100 Pricing Comparison (2026)](https://getdeploying.com/gpus/nvidia-a100)\n- [A100 Price Guide (Jarvislabs)](https://jarvislabs.ai/blog/a100-price)\n- [A100 Pricing (ThunderCompute)](https://www.thundercompute.com/blog/nvidia-a100-pricing)\n- [OpenVLA Paper](https://arxiv.org/html/2406.09246v3)\n- [Awesome VLA Post-Training](https://github.com/AoqunJin/Awesome-VLA-Post-Training)\n- [VLA Survey Paper](https://arxiv.org/abs/2505.04769)\n- [OpenVLA Deployment Guide (Spheron)](https://www.spheron.network/blog/deploy-openvla-gpu-cloud/)"
      }
    ],
    "totalDurationMs": 136530,
    "totalTokens": 28198,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 906,
      "cache_creation_input_tokens": 3112,
      "cache_read_input_tokens": 20253,
      "output_tokens": 3927,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 906,
          "output_tokens": 3927,
          "cache_read_input_tokens": 20253,
          "cache_creation_input_tokens": 3112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3112,
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
  "sourceToolAssistantUUID": "b2f23a13-d214-4365-839c-9f2b3b56daf7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-18T18:31:25.163Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent, I now have comprehensive research from all five agents. Let me synthesize everything into the final JSON output.

Key findings:

**Concurrent work:**
- CoA-VLA (ICCV 2025): Fixed 4-type affordance, separate injection module, NOT open-vocabulary, NOT unified autoregressive
- VLA-R1 (arXiv Oct 2025): Affordance-aligned CoT but uses RL post-training, not purely autoregressive
- GST-VLA (arXiv Mar 2026): Depth-Aware CoT with affordance but fixed 3D geometric types, Gaussian spatial tokens


- ACoT-VLA (CVPR 2026): Action chain-of-thought with coarse trajectory reasoning, but not affordance-specific
- No existing model combines open-vocabulary affordance tokens with unified autoregressive VLA architecture

**References verified:** All 7 references checked out correctly.

**SOTA models:** OpenVLA (7B) with ECoT remains the strongest VLA backbone, though Qwen2.5-VL (3B/7B) and GLM-4.1V-9B-Thinking represent the current best open-source multimodal LLMs for this task. For reasoning capabilities, I'm evaluating the latest models to determine the optimal foundation.

**Venue deadlines:** CoRL 2026 is too tight at just 8 days away, but AAAI 2027 gives about 71 days, with ICLR 2027 around 4-5 months out and subsequent major conferences stretching to 10 months.

**Cost estimates:** A100 rentals run $0.72-1.49 per hour depending on provider, and I'm calculating LoRA fine-tuning expenses.

Now I'm thinking through the core approach: extend OpenVLA or Qwen2.5-VL to generate open-vocabulary affordance reasoning tokens—natural language descriptions of what to interact with, how to grasp, and where to move—before the action tokens in a single sequence. This is different from CoA-VLA's fixed taxonomy since I'd use free-form language affordances conditioned on the task instruction. The plan is to first build an annotation pipeline using a strong VLM like Qwen2.5-VL-72B or GPT-4o to auto-label trajectories from Open X-Embodiment or DROID with these affordance descriptions, then fine-tune a 7B model on the annotated data.

For training, I'd use LoRA for efficiency and treat the affordance tokens as intermediate supervision signals. Evaluation would compare against CoA-VLA and CoT-VLA baselines on LIBERO, SimplerEnv, and real-world tasks.

Looking at the contribution level, this feels like a meaningful synthesis rather than just an incremental tweak—the combination of open-vocabulary affordances, unified autoregressive generation, and affordance-specific reasoning creates a clear differentiation from existing work.

For venues, ICLR 2027 is the ideal target with its timeline around September-October 2026, though AAAI 2027 could work if real-world experiments move quickly. CVPR 2027 serves as a backup option.

Now I'm identifying the concurrent work in this space—there's VLA-R1 combining affordance-aligned reasoning with reinforcement learning, GST-VLA incorporating 3D Gaussian spatial tokens, and ACoT-VLA focusing on action chain-of-thought. I should also pull together the key references across recent venues like ICCV, CVPR, ICML, and ICLR from 2025-2026 that establish the foundation for this research direction.

Let me reconsider the cost breakdown for a manual implementation approach. The main bottleneck is GPU utilization—when a human is writing code or analyzing results, the GPUs sit idle, which inflates the timeline to 3-6 months even though actual compute time is relatively modest. The project breaks down into building the affordance annotation pipeline first, which itself requires significant development time before any training can begin.

For a human-in-loop setup, I can run experiments continuously while the researcher sleeps or works on other tasks, which compresses the timeline to 1-2 months and improves GPU utilization to 300-500 hours of actual work. The key difference is that the agent handles the experimental loop autonomously rather than waiting for human decisions between runs.

With full automation, I'd need 500-800 hours of A100 time across 3-5x more experiments, but the timeline shrinks dramatically to 1-3 weeks since there's virtually no idle time—the main constraint becomes GPU availability and API quotas for annotation.

Now I'm refining the cost breakdown for the manual approach: roughly 300 hours of productive GPU time, but accounting for idle periods when waiting on human input or debugging, the actual rental time could stretch to 600 hours or more over 3-5 months. The cost calculation depends on whether we're counting just active compute hours or total rental duration.

For clarity, I'm settling on: manual research needs about 300 productive A100 hours with 40-50% utilization across 3-5 months with 1-2 researchers, costing $450-900 depending on instance management. The human-in-loop approach would use around 400 hours with higher utilization around 70%.

Now I'm looking at the fully automated approach—it would consume roughly 800 A100 hours with 95% utilization, running 3-5x more experiments in just 1-3 weeks across 4-8 GPUs with no team overhead. The Claude API costs scale up to $300-800 for orchestrating thousands of turns, and GPU costs hit $600-1,200.

But I'm realizing I also need to account for the annotation costs—labeling 100K trajectories from Open X-Embodiment with affordance information through a VLM API would require around 500K API calls, which adds another layer to the budget calculation.

Actually, I can optimize this significantly by either working with a smaller subset of trajectories or running an open-source VLM like Qwen2.5-VL-72B directly on GPU instead of paying per API call. If I go the open-source route, I'd need 4 A100s to process 50K trajectories in roughly 560 GPU-hours total, or I could use a smaller 7B model for initial filtering followed by the larger model for final annotation. This fundamentally changes the cost structure I need to factor in.

For the actual model architecture, I'm leaning toward using OpenVLA-7B or Qwen2.5-VL-7B as the backbone since they're well-established VLA options, then leveraging Qwen2.5-VL-72B for the affordance annotation step—there's already existing work with ECoT-OpenVLA that incorporates chain-of-thought reasoning which could be valuable here.

Now I need to finalize the project structure and decide on the venue. AAAI 2027 is tight at around 71 days out, but with focused compute time and writing it's doable. ICLR 2027 gives more breathing room at 4-5 months, and the guidance is clear about targeting the highest-tier venue the work supports, so I should aim for ICLR unless the timeline becomes genuinely infeasible. due to timeline concerns"

ICLR is higher tier than AAAI, so my primary target should be ICLR 2027. Though AAAI 2027 could work as an earlier alternative. But the instruction says not to downgrade venues due to timeline concerns, and since the AI team runs 24/7, if this contribution is truly top-tier, I should aim for ICLR 2027 or NeurIPS 2026 if the deadline were still open. Since NeurIPS 2026 just closed, ICLR 2027 becomes the next top-tier option. AAAI 2027 is also top-tier with an earlier deadline, so I'll target ICLR 2027, AAAI 2027, and CVPR 2027.

Now I'm drafting the executive summary. The key idea is that OVA-VLA treats affordance reasoning as dynamic, instruction-conditioned natural language tokens within a single autoregressive sequence, rather than using a fixed taxonomy like CoA-VLA does. This lets the model express arbitrary affordance concepts—contact surfaces, force directions, functional regions, spatial constraints—based on what the task requires. I'm building on Qwen2.5-VL-7B and using the larger 72B version to automatically annotate 50K+ trajectories from Open X-Embodiment with open-vocabulary affordance chains, then training end-to-end with LoRA to generate affordance descriptions before action tokens. The experiments look strong across simulation and real-world settings, showing clear improvements over the fixed-taxonomy baseline, so this feels like a solid top-tier contribution. It's not revolutionary—more of a well-motivated synthesis combining open-vocabulary affordances with unified autoregressive generation—but the empirical validation should carry it. Now I'm finalizing the JSON with the key references, making sure I only include papers I can verify. I'm considering whether to include OpenVLA and ECoT as references, but since the verification agent didn't check them and I'm uncertain about their exact venues, I'll stick with the ten verified papers. Now I need to update the landscape field with the concurrent work I've discovered and then generate the complete JSON output.

For the GPU cost estimates, I'm using mid-range A100 pricing at around $1.50 per hour—manual approaches need roughly 300 hours, human-in-loop around 400 hours, and fully automated methods closer to 800 hours, translating to costs between $450-700, $500-800, and $900-1,500 respectively.

For the approach description, I'm condensing it to explain how OVA-VLA extends the CoA-VLA paradigm to handle open-vocabulary affordance reasoning within a unified autoregressive architecture, starting from a Qwen2.5-VL-7B backbone with an automated annotation pipeline using the larger 72B model to generate affordance descriptions. I'm verifying the arXiv submission dates against the timeline—the July 2025 prefix for the VLA survey checks out, and the March 2026 date for the affordance paper aligns with the expected submission window. The conference deadlines I noted are accurate relative to today's date, so I can now compile the final JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb6356e5-60c6-461a-829a-cd7cc47e41cd",
  "isSidechain": false,
  "requestId": "req_011CbAWV2WxfBoBus6nTkZfG",
  "type": "assistant",
  "uuid": "e09f9db6-22a6-4baf-97eb-a10c3e8a2b3c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXLhxhbrUE4TtdhuPN5Fer",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17200,
      "cache_read_input_tokens": 19191,
      "output_tokens": 8033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8033,
          "cache_read_input_tokens": 19191,
          "cache_creation_input_tokens": 17200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17200
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

_source line 26 · 2026-05-18T18:32:22.649Z_

Now I have comprehensive data from all five research threads. Let me synthesize the final output.

Key findings:
- **No exact concurrent work** does open-vocabulary affordance tokens in a unified autoregressive VLA (gap confirmed)
- All 7 original references verified correct
- New concurrent work discovered: VLA-R1, GST-VLA, ACoT-VLA (all differentiated)
- Best current backbone: Qwen2.5-VL-7B; annotation VLM: Qwen2.5-VL-72B
- Venues open: AAAI 2027 (Jul 28), ICLR 2027 (~Sep-Oct), CVPR 2027 (~Nov)
- A100 rental: $0.72-1.50/hr; LoRA fine-tune: 20-40h/task; full fine-tune: 80-200h/task

{
  "title": "Open-Vocabulary Affordance Reasoning Tokens for Autoregressive VLA",
  "core_problem": "Can we extend the chain-of-affordance reasoning paradigm from fixed structured types to an open-vocabulary token space, generating dynamic affordance reasoning tokens conditioned on free-form language before predicting action tokens in a unified autoregressive VLA?",
  "opportunity": "CoT-VLA (arXiv 2503.22020) demonstrates that generating visual subgoal tokens before action tokens improves real-world manipulation by 17%, proving intermediate reasoning tokens are highly effective. SeqAfford (CVPR 2025, arXiv 2412.01550) shows MLLMs can generate sequential affordance reasoning for complex multi-step instructions — but only for perception. The VLA survey (arXiv 2507.01925) explicitly identifies affordance as one of the valid action token categories alongside trajectory, goal state, and reasoning tokens, and notes the synergy between affordance (what-to-do) and trajectory (how-to-do). The gap: no work generates open-vocabulary affordance tokens that condition action generation in a unified VLA.",
  "landscape": "CoA-VLA (ICCV 2025, arXiv 2412.20451) generates structured affordance text (4 types: object, grasp, spatial, movement) before action prediction via a separate co-injection module — effective but vocabulary-limited and architecturally decoupled. CoT-VLA (arXiv 2503.22020) generates visual subgoal images as reasoning before actions — achieves 17% real-world improvement but uses generic visual reasoning, not affordance-specific. ACoT-VLA (CVPR 2026, arXiv 2601.11404) generates coarse action trajectory reasoning as chain-of-thought but reasons at the action level, not affordance level. VLA-R1 (arXiv 2510.01623) creates affordance-aligned CoT via RL post-training (GRPO), but uses RL-based optimization rather than unified autoregressive generation. GST-VLA (arXiv 2603.09079, Mar 2026) introduces Depth-Aware CoT with structured 3D geometric affordance steps using Gaussian spatial tokens — close conceptually but limited to fixed 3D geometric affordance types, not open-vocabulary language. Diffusion-VLA (ICML 2025, arXiv 2412.03293) generates reasoning text before diffusion action head but not affordance-structured. SeqAfford (CVPR 2025) generates sequential affordance reasoning with 180K instruction-point cloud pairs but has no action generation. 3D-AffordanceLLM (ICLR 2025, arXiv 2502.20041) reformulates affordance detection as instruction reasoning affordance segmentation with ~8% mIoU improvement, but only perception. The context-dependent affordance study (arXiv 2603.04419) shows affordance must be dynamically determined by task instruction, not pre-categorized — supporting open-vocabulary tokens over fixed types. No existing work combines all three of: (a) open-vocabulary free-form affordance descriptions, (b) generated as autoregressive tokens in the same sequence as actions, and (c) conditioning action generation through causal attention in a unified VLA.",
  "approach": "We propose OVA-VLA, which extends the CoA-VLA paradigm from fixed affordance types to open-vocabulary affordance reasoning tokens within a unified autoregressive architecture built on a Qwen2.5-VL-7B backbone. We first construct an automated annotation pipeline using Qwen2.5-VL-72B to generate open-vocabulary affordance descriptions (contact regions, grasp strategies, force directions, spatial constraints, functional affordances) for 50K+ trajectories from Open X-Embodiment and DROID, leveraging ShareRobot and RoboInter-Data affordance labels as seed examples. The model is LoRA-fine-tuned to autoregressively generate instruction-conditioned affordance tokens followed by action tokens in a single sequence, where affordance reasoning conditions action generation through causal attention — eliminating CoA-VLA's separate co-injection module. We introduce an affordance token curriculum that progresses from structured (CoA-VLA-style 4-type) to fully open-vocabulary descriptions during training to stabilize learning. Evaluation spans LIBERO, SimplerEnv, and real-robot manipulation against CoA-VLA, CoT-VLA, ECoT, and ACoT-VLA baselines to isolate the contribution of open-vocabulary affordance reasoning, with particular focus on novel-object generalization, compositional instructions, and cross-embodiment transfer where fixed taxonomies are expected to fail.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~400h A100 (annotation pipeline ~150h on 4xA100 for 72B VLM, LoRA training ~100h across 5-8 runs, evaluation ~50h, debugging/iteration ~100h)",
      "gpu_utilization": "Low (~35-45% effective utilization). GPU sits idle while researchers design annotation prompts, debug training pipelines, analyze failure cases, and iterate on affordance token formats. Significant overnight/weekend idle time.",
      "timeline": "4-6 months",
      "team": "1-2 researchers (1 lead with VLA experience, 1 supporting data/eval)",
      "estimated_gpu_cost": "$500-900 (at $1.25-2.00/hr mid-range A100 rental; actual rental hours higher than productive hours due to idle)"
    },
    "human_in_loop": {
      "gpu_hours": "~500h A100 (annotation ~150h, training ~200h across 10-15 runs with more ablations, evaluation ~80h, agent-driven hyperparameter search ~70h)",
      "gpu_utilization": "Moderate (~65-75%). Agent queues next experiment immediately after each run completes, runs overnight batches, and performs automated analysis. Human idle time reduced to approval gates only.",
      "timeline": "6-10 weeks",
      "team": "1 researcher, ~45min/day review (approve annotation quality, validate affordance token samples, select ablation directions)",
      "claude_api_cost": "$200-500 (~3000-6000 agent turns for experiment orchestration, result analysis, code iteration, and paper drafting)",
      "estimated_gpu_cost": "$600-1,000 (higher productive hours but less rental waste from idle)",
      "risk_note": "Affordance annotation quality is the key bottleneck — the VLM-generated affordance descriptions must be physically grounded and task-relevant. Human approval gates on annotation samples are critical; poor affordance labels degrade action prediction rather than help it."
    },
    "auto_research": {
      "gpu_hours": "~900h A100 (annotation ~200h with more thorough multi-VLM consensus, training ~400h across 25-40 experimental runs including architecture variants and token format ablations, evaluation ~150h with comprehensive benchmarking, automated hyperparameter sweeps ~150h)",
      "gpu_utilization": "High (~90-95%). Agent runs 24/7 with near-zero idle: queues experiments in parallel across available GPUs, immediately analyzes results and launches next batch, performs automated error diagnosis and re-runs.",
      "timeline": "10-18 days with 4-8 A100 GPUs available concurrently",
      "team": "0 (initial 2-3 hour setup: repo clone, dataset access, evaluation environment, base model download)",
      "claude_api_cost": "$400-900 (~6000-12000 agent turns for full experiment lifecycle: code development, annotation pipeline, training orchestration, result analysis, ablation design, paper writing)",
      "estimated_gpu_cost": "$1,000-1,800 (more total compute but near-zero waste; explores 3-5x more configurations than manual)",
      "speed_bottleneck": "GPU count is primary bottleneck — with 4 GPUs, annotation and training must be serialized (~18 days); with 8 GPUs, annotation and early training runs can overlap (~10 days). Secondary: Qwen2.5-VL-72B annotation throughput (~10 trajectories/minute on 4xA100).",
      "risk_note": "Automated affordance quality assessment may miss subtle physical grounding errors (e.g., describing a grasp affordance that is kinematically infeasible). Risk mitigation: include automated consistency checks comparing affordance descriptions against actual gripper contact points in the trajectory data."
    }
  },
  "target_venues": [
    "ICLR 2027 (expected deadline Sep-Oct 2026; top-tier, ideal fit for representation learning + robotics contribution)",
    "AAAI 2027 (deadline Jul 28, 2026; top-tier, feasible with auto-research timeline)",
    "CVPR 2027 (expected deadline Nov 2026; top-tier, strong fit for vision-language-action work)"
  ],
  "level": "top-tier",
  "key_references": [
    "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance (ICCV 2025)",
    "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models (arXiv 2025)",
    "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models (CVPR 2026)",
    "VLA-R1: Enhancing Reasoning in Vision-Language-Action Models (arXiv 2025)",
    "GST-VLA: Structured Gaussian Spatial Tokens for 3D Depth-Aware VLA Models (arXiv 2026)",
    "SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model (CVPR 2025)",
    "Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning (ICML 2025)",
    "3D-AffordanceLLM: Harnessing Large Language Models for Open-Vocabulary Affordance Detection in 3D Worlds (ICLR 2025)",
    "A Survey on Vision-Language-Action Models: An Action Tokenization Perspective (arXiv 2025)",
    "Context-Dependent Affordance Computation in Vision-Language Models (arXiv 2026)"
  ],
  "description": "We propose OVA-VLA, a unified autoregressive Vision-Language-Action model that generates open-vocabulary affordance reasoning tokens conditioned on free-form language instructions before predicting action tokens. Unlike CoA-VLA's fixed 4-type affordance taxonomy with a separate co-injection module, our approach treats affordance reasoning as dynamic, instruction-conditioned natural language within a single autoregressive sequence — enabling the model to express arbitrary affordance concepts (contact surfaces, grasp strategies, force directions, functional regions) as the task demands. Built on a Qwen2.5-VL-7B backbone, we construct an automated annotation pipeline using Qwen2.5-VL-72B to label 50K+ trajectories from Open X-Embodiment and DROID with open-vocabulary affordance chains, bootstrapped from ShareRobot and RoboInter-Data affordance labels. A curriculum strategy transitions from structured to open-vocabulary affordance tokens during training. We evaluate on LIBERO, SimplerEnv, and real-robot benchmarks against CoA-VLA, CoT-VLA, ECoT, and ACoT-VLA, targeting novel-object generalization and compositional instruction following where fixed taxonomies are expected to fail. The work fills a verified gap: no existing system combines open-vocabulary affordance reasoning with unified autoregressive action generation.",
  "project_name": "open_vocab_afford_vla",
  "source": "web_research"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e09f9db6-22a6-4baf-97eb-a10c3e8a2b3c",
  "isSidechain": false,
  "requestId": "req_011CbAWV2WxfBoBus6nTkZfG",
  "type": "assistant",
  "uuid": "9e910483-1a15-4944-af07-c064ff0cebb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXLhxhbrUE4TtdhuPN5Fer",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17200,
      "cache_read_input_tokens": 19191,
      "output_tokens": 8033,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17200,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8033,
          "cache_read_input_tokens": 19191,
          "cache_creation_input_tokens": 17200,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17200
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-18 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.  {   \"title\": \"Open-Vocabula…",
  "leafUuid": "9e910483-1a15-4944-af07-c064ff0cebb0",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Open-vocabulary affordance tokens in autoregressive VLA",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "Complete the research direction below with implementation details.  **Today's date: 2026-05-18 (UTC).** Only recommend venues whose submission deadline has NOT yet passed.  {   \"title\": \"Open-Vocabula…",
  "leafUuid": "9e910483-1a15-4944-af07-c064ff0cebb0",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Open-vocabulary affordance tokens in autoregressive VLA",
  "sessionId": "ee74ae46-033d-42d9-90c8-f7218628900f"
}
```

---
