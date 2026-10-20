# Research conversation: 【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。 【原始 pro

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 100
- **Recorded user turns:** 5
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/a05c62ff-bff7-4813-ae79-89cefb9808a3.jsonl`
- **Structured JSON:** [`afc9ab1d4195e56bff98.json`](../../sessions/af/afc9ab1d4195e56bff98.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:02:14.521Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:02:14.521Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "content": "【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。\n\n【原始 proposal】:\n# Formally-Routed Process Reward Models for Miracle Step Detection\n\n## Core Problem\n\nNo existing PRM exploits the formalizability structure of reasoning steps — systems are either formal-only (FoVer, PRoSFI) or neural-only (GenPRM, ARES), leaving the per-step routing decision between formal derivability checking and neural verification entirely unaddressed. Can a learned formalizability router that dispatches each step to the appropriate verifier catch miracle steps (unjustified logical leaps) that pure neural PRMs miss?\n\n## Research Opportunity\n\nThree converging gaps create a unique opening: (1) VERGE demonstrates 18.7% uplift from routing between Z3 and neural verifiers but uses hand-crafted rules, not learned routing — the field guide explicitly notes learned routing as the open next step; (2) RRM's neural rubric approach to miracle steps was withdrawn from ICLR 2026, leaving formal derivability from predecessors (testing whether step S_i follows from {S_1,...,S_{i-1}} via Z3) completely untried for miracle step detection; (3) FoVer's public codebase, GenPRM's open models, and the Risk-Controlled paper's honest quantification of autoformalization limits (43% faithfulness, 28-79% coverage) now provide both infrastructure and calibration data that make a hybrid system tractable at academic compute budgets.\n\n## Research Landscape\n\nFoVer (ACL 2026) achieves 85.8 AUROC on ProcessBench by training 7B PRMs on Z3/Isabelle-verified labels, but trains exclusively on formally verifiable data, producing documented overly-strict behavior on informal reasoning steps. GenPRM (AAAI 2026) represents neural PRM SOTA with 7B surpassing Qwen2.5-Math-PRM-72B on ProcessBench via generative CoT and code verification, yet provides no formal derivability guarantees. ARES (2025) achieves 72.1% Macro-F1 on PRMBench through autoregressive neural entailment checking — elegant but entirely dependent on LLM judgment quality, with the authors acknowledging performance is tied to entailment model calibration. LogicReward (ICLR 2026) is the closest work, using Isabelle step verification with token-probability fallback, but lacks a trained neural verifier branch, an explicit formalizability classifier, and miracle step targeting. The autoformalization bottleneck is now precisely characterized: Risk-Controlled Lean-as-Judge (May 2026) shows onl...\n\n## Proposed Approach\n\nTrain Qwen3-8B formalizability classifier on FoVer Z3 labels + autoformalization success signals. Route formalizable steps to Z3 predecessor-derivability checking; others to GenPRM-7B with ARES-style calibrated entailment. Target miracle steps via the formal derivability gap. Evaluate on ProcessBench, PRMBench, and RRM miracle taxonomy with honest coverage reporting.\n\n## Detailed Description\n\nFormalRoute-PRM introduces a learned formalizability router dispatching each reasoning step to Z3 formal verification or GenPRM-7B neural scoring. A Qwen3-8B classifier trained on FoVer's Z3 verification labels and autoformalization success signals predicts per-step formalizability. Formalizable steps undergo Z3 derivability checking from predecessor steps with guaranteed correctness; non-formalizable steps receive GenPRM scoring with ARES-style calibrated entailment. The system targets miracle steps—unjustified logical leaps that pure neural PRMs accept. Concurrent work search confirms no existing system combines learned formalizability routing with miracle step detection: VERGE routes via hand-crafted rules, LogicReward lacks a trained router, and RRM (withdrawn from ICLR 2026) never tested formal derivability. We evaluate on ProcessBench, PRMBench, and RRM's miracle step taxonomy, reporting honest autoformalization coverage limits per Risk-Controlled Lean-as-Judge methodology. FoVer's public codebase and GenPRM's open weights enable single-node H100 experimentation within academic compute budgets.\n\n## Key References\n\n- FoVer: PRM Data Synthesis via Formal Verification (ACL 2026)\n- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026)\n- LogicReward: Step-Wise Logical Supervision (ICLR 2026)\n- VERGE: Formal Refinement and Guidance Engine (arXiv 2026)\n- Curing Miracle Steps with Rubric Rewards (arXiv 2025)\n- Risk-Controlled Lean-as-Judge (arXiv 2026)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:02:14.537Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:02:14.537Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-29T06:02:14.561Z_

【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。

【原始 proposal】:
# Formally-Routed Process Reward Models for Miracle Step Detection

## Core Problem

No existing PRM exploits the formalizability structure of reasoning steps — systems are either formal-only (FoVer, PRoSFI) or neural-only (GenPRM, ARES), leaving the per-step routing decision between formal derivability checking and neural verification entirely unaddressed. Can a learned formalizability router that dispatches each step to the appropriate verifier catch miracle steps (unjustified logical leaps) that pure neural PRMs miss?

## Research Opportunity

Three converging gaps create a unique opening: (1) VERGE demonstrates 18.7% uplift from routing between Z3 and neural verifiers but uses hand-crafted rules, not learned routing — the field guide explicitly notes learned routing as the open next step; (2) RRM's neural rubric approach to miracle steps was withdrawn from ICLR 2026, leaving formal derivability from predecessors (testing whether step S_i follows from {S_1,...,S_{i-1}} via Z3) completely untried for miracle step detection; (3) FoVer's public codebase, GenPRM's open models, and the Risk-Controlled paper's honest quantification of autoformalization limits (43% faithfulness, 28-79% coverage) now provide both infrastructure and calibration data that make a hybrid system tractable at academic compute budgets.

## Research Landscape

FoVer (ACL 2026) achieves 85.8 AUROC on ProcessBench by training 7B PRMs on Z3/Isabelle-verified labels, but trains exclusively on formally verifiable data, producing documented overly-strict behavior on informal reasoning steps. GenPRM (AAAI 2026) represents neural PRM SOTA with 7B surpassing Qwen2.5-Math-PRM-72B on ProcessBench via generative CoT and code verification, yet provides no formal derivability guarantees. ARES (2025) achieves 72.1% Macro-F1 on PRMBench through autoregressive neural entailment checking — elegant but entirely dependent on LLM judgment quality, with the authors acknowledging performance is tied to entailment model calibration. LogicReward (ICLR 2026) is the closest work, using Isabelle step verification with token-probability fallback, but lacks a trained neural verifier branch, an explicit formalizability classifier, and miracle step targeting. The autoformalization bottleneck is now precisely characterized: Risk-Controlled Lean-as-Judge (May 2026) shows onl...

## Proposed Approach

Train Qwen3-8B formalizability classifier on FoVer Z3 labels + autoformalization success signals. Route formalizable steps to Z3 predecessor-derivability checking; others to GenPRM-7B with ARES-style calibrated entailment. Target miracle steps via the formal derivability gap. Evaluate on ProcessBench, PRMBench, and RRM miracle taxonomy with honest coverage reporting.

## Detailed Description

FormalRoute-PRM introduces a learned formalizability router dispatching each reasoning step to Z3 formal verification or GenPRM-7B neural scoring. A Qwen3-8B classifier trained on FoVer's Z3 verification labels and autoformalization success signals predicts per-step formalizability. Formalizable steps undergo Z3 derivability checking from predecessor steps with guaranteed correctness; non-formalizable steps receive GenPRM scoring with ARES-style calibrated entailment. The system targets miracle steps—unjustified logical leaps that pure neural PRMs accept. Concurrent work search confirms no existing system combines learned formalizability routing with miracle step detection: VERGE routes via hand-crafted rules, LogicReward lacks a trained router, and RRM (withdrawn from ICLR 2026) never tested formal derivability. We evaluate on ProcessBench, PRMBench, and RRM's miracle step taxonomy, reporting honest autoformalization coverage limits per Risk-Controlled Lean-as-Judge methodology. FoVer's public codebase and GenPRM's open weights enable single-node H100 experimentation within academic compute budgets.

## Key References

- FoVer: PRM Data Synthesis via Formal Verification (ACL 2026)
- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026)
- LogicReward: Step-Wise Logical Supervision (ICLR 2026)
- VERGE: Formal Refinement and Guidance Engine (arXiv 2026)
- Curing Miracle Steps with Rubric Rewards (arXiv 2025)
- Risk-Controlled Lean-as-Judge (arXiv 2026)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1291ff03-bb85-4dab-aeac-02e19ae9567f",
  "type": "user",
  "uuid": "e8e10c88-6640-4bbe-8e54-489472dd7fc0",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:02:14.560Z_

```json
{
  "parentUuid": "e8e10c88-6640-4bbe-8e54-489472dd7fc0",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "9015f333-7240-4ec7-ac79-b87a8b1247f6",
  "timestamp": "2026-05-29T06:02:14.560Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:02:14.560Z_

```json
{
  "parentUuid": "9015f333-7240-4ec7-ac79-b87a8b1247f6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5d57a085-fcfe-43c4-b24d-d659c5daae96",
  "timestamp": "2026-05-29T06:02:14.560Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Assistant

_source line 7 · 2026-05-29T06:02:22.541Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the 终审 agent (Meta Judge) for the initial triage phase. However, looking at the message more carefully, they say this proposal has already passed triple-consensus triage and is confirmed GO. They want me to remember this proposal for subsequent iterations where I'll act as 角色 B (迭代中).

So the user is just giving me the original proposal to remember, and will next send me the outputs from the 发掘 agent and 补救 agent for the first iteration round.

Let me acknowledge that I've received and stored the original proposal, and I'm ready to receive the worker outputs for the first iteration round.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d57a085-fcfe-43c4-b24d-d659c5daae96",
  "isSidechain": false,
  "requestId": "req_011CbWMPpx5gp6emiHwVRojj",
  "type": "assistant",
  "uuid": "09a979ad-3389-48ac-817b-6e265f2f4280",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VJfoMagxkpyvGRr6iyRy9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8086,
      "cache_read_input_tokens": 11014,
      "output_tokens": 630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 630,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8086
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

_source line 8 · 2026-05-29T06:02:30.285Z_

收到。我已完整记录原始 proposal「Formally-Routed Process Reward Models for Miracle Step Detection」，包括所有关键引用：

**已记录引用清单（用于后续重写时逐条核对）：**
1. FoVer (ACL 2026) — PRM Data Synthesis via Formal Verification
2. GenPRM (AAAI 2026) — Scaling Test-Time Compute of PRMs
3. LogicReward (ICLR 2026) — Step-Wise Logical Supervision
4. VERGE (arXiv 2026) — Formal Refinement and Guidance Engine
5. Curing Miracle Steps with Rubric Rewards (arXiv 2025) — RRM
6. Risk-Controlled Lean-as-Judge (arXiv 2026)
7. ARES (2025) — Autoregressive neural entailment checking
8. PRMBench, ProcessBench — 评测基准
9. Qwen3-8B, GenPRM-7B, Qwen2.5-Math-PRM-72B — 模型引用
10. Z3, Isabelle — 形式化工具

**关键数据点已记录：**
- FoVer: 85.8 AUROC on ProcessBench
- GenPRM: 7B surpassing 72B on ProcessBench
- ARES: 72.1% Macro-F1 on PRMBench
- VERGE: 18.7% uplift from routing
- Risk-Controlled: 43% faithfulness, 28-79% coverage

我现在以「角色 B：迭代中」待命，准备接收第一轮发掘 agent 和补救 agent 的输出进行整合。请发送 worker 输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09a979ad-3389-48ac-817b-6e265f2f4280",
  "isSidechain": false,
  "requestId": "req_011CbWMPpx5gp6emiHwVRojj",
  "type": "assistant",
  "uuid": "3acaf4d1-5601-43e6-8323-7d910becf692",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013VJfoMagxkpyvGRr6iyRy9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8086,
      "cache_read_input_tokens": 11014,
      "output_tokens": 630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8086,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 630,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 8086,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8086
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

_source line 9_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。  【原始 proposal】: # Formally-Routed Process Reward Models for Miracle Step Detection  ##…",
  "leafUuid": "3acaf4d1-5601-43e6-8323-7d910becf692",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 12 · 2026-05-29T06:08:14.189Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:08:14.189Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "content": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have sufficient background to provide my analysis. Let me synthesize my findings.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960) (ACL 2026 Findings): 使用 Z3/Isabelle 自动标注 step-level error labels 训练 PRM，但仅在 formally verifiable data 上训练，对 informal reasoning 存在 documented overly-strict behavior。核心 insight：formal verification 可以提供高质量 PRM 训练信号，但覆盖面有限。\n- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891) (AAAI 2026): 7B 模型通过 generative CoT + code verification 超越 72B 模型。核心 insight：PRM 可以通过 generative reasoning 而非纯 scalar scoring 大幅提升性能。\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 使用 semantic routing 将 claims 分派到 SMT solver 或 LLM ensemble——但路由基于 rule-based claim type classification，非 learned routing。明确提出 Minimal Correction Subsets (MCS) 做 error localization。\n- [LogicReward: Step-Wise Logical Supervision](https://openreview.net/forum?id=A3FhAVfcJI) (ICLR 2026): 用 Isabelle 做 step-level formal verification + token-probability fallback，但无 trained neural verifier branch，无 explicit formalizability classifier。\n- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774) (arXiv 2025, ICLR 2026 under review): 定义 miracle step taxonomy，RRM 减少 71% miracle steps，但方法是 outcome-oriented rubric scoring，未尝试 formal derivability checking。\n- [PRoSFI / Structured Formal Intermediaries](https://arxiv.org/pdf/2603.29500) (2026): 模型输出 structured intermediate steps aligned with natural language reasoning，由 formal prover 验证——接近本 proposal 的 formalization pipeline 但方向不同（generation-side 而非 verification-side）。\n- 调研总结：当前领域的研究者主要在两条路线上突破——(1) 用 formal verification 提供更精确的 training signal（FoVer, LogicReward），(2) 增强 neural PRM 的 generative reasoning 能力（GenPRM, ARES）。**将这两条路线通过 learned routing 动态结合是一个已被 VERGE 识别但未被实现的 open problem**，本 proposal 正好定位在这个缺口上。\n\n---\n\n【发掘点 1】\n- 维度: 核心 claim 强化\n- 内容: Proposal 当前的核心 claim 是\"learned router + hybrid verification → catch miracle steps\"。但这个 claim 的逻辑链条有一个未被充分阐述的关键环节：**为什么 formal derivability checking 对 miracle steps 特别有效？** Miracle steps 的定义是\"unjustified logical leaps\"——如果将 step S_i 的 predecessors {S_1,...,S_{i-1}} formalize 后送入 Z3 检查 S_i 是否可推导，那么 miracle step 本质上是 Z3 返回 UNSAT（不可推导）的步骤。这意味着 formal derivability checking 与 miracle step detection 之间存在一个**近乎 definitional 的对应关系**——这不是\"可能有效\"，而是\"在 formalizability 成立的条件下，是 theoretically guaranteed 的检测机制\"。建议将此提升为核心理论贡献的第一支柱：在 formalizable steps 子集上，miracle step detection 等价于 Z3 derivability failure，这提供了 neural PRM 无法提供的 soundness guarantee。\n- 价值: 将核心 claim 从 empirical（\"我们的系统表现更好\"）提升到 semi-formal guarantee（\"在 coverage 范围内，detection 是 sound 的\"），直接命中 Novelty 和 Significance。审稿人看到的不再只是\"又一个 hybrid system\"，而是\"第一个能对 miracle step detection 提供部分 formal guarantee 的 PRM\"。\n- 调研依据: FoVer 已证明 Z3 derivability labels 的高精度但未将其与 miracle step taxonomy 对接；RRM 定义了 miracle steps 但用 neural rubric 而非 formal methods；两者的 gap 恰好是本 proposal 的理论贡献空间。\n\n【发掘点 2】\n- 维度: novelty 锐化\n- 内容: 当前 proposal 将自身定位为 \"VERGE 的 learned routing 升级\"，这有将 novelty 矮化为 incremental improvement 的风险。实际上，VERGE 的 routing 是在 **claim type** 层面（logical claim vs. commonsense claim）做 rule-based 分类，而本 proposal 的 router 是在 **formal derivability potential** 层面做 learned prediction——这是两个完全不同的分类任务。VERGE 的 router 不需要考虑 predecessors，因为它只看单个 claim 的 type；而本 proposal 的 formalizability 判断是 context-dependent 的（同一个 step 在不同 predecessor context 下可能有不同的 formalizability）。建议明确区分：VERGE 做的是 static type routing（与上下文无关），本 proposal 做的是 dynamic derivability routing（依赖推理链上下文），这是一个 fundamentally harder 且 more informative 的分类问题。\n- 价值: 防止审稿人将本工作简单归类为\"VERGE + better router\"，锐化 novelty 为\"context-dependent formalizability prediction 是一个新的研究问题，且其 positive outcome 直接 enables sound miracle step detection\"。命中 Novelty 和 Related Work 差异化。\n- 调研依据: VERGE paper 的 semantic routing 描述明确表明其 routing 仅基于 claim type taxonomy（verifiable logic vs. ambiguous/commonsense），不考虑推理链上下文。\n\n【发掘点 3】\n- 维度: significance 提升\n- 内容: Proposal 当前将 significance 定位在\"catch miracle steps that neural PRMs miss\"——这是 correct 但 narrow 的 framing。更有影响力的 framing 是：**FormalRoute-PRM 提供了一个 principled framework 来量化 PRM 的 verification coverage gap**。具体来说，formalizability router 的输出本身就是一个 per-step \"verification confidence\" signal——formalizable steps 获得 guaranteed verification，non-formalizable steps 获得 best-effort neural verification，这自然产生了一个 **calibrated confidence hierarchy**。这意味着 FormalRoute-PRM 不仅是一个 better PRM，而是一个能 tell you where it's uncertain 的 PRM——这对 downstream applications（如 RLHF、test-time compute allocation）具有 broader impact。\n- 价值: 将 significance 从\"detect more errors\"提升到\"provide principled verification uncertainty quantification\"，扩大了 paper 的影响面。Risk-Controlled Lean-as-Judge 已经在做类似的 honest coverage reporting，本 proposal 可以将其发展为 contribution 而非仅仅是 evaluation protocol。命中 Significance。\n- 调研依据: Risk-Controlled Lean-as-Judge 的 honest coverage quantification 思路 + GenPRM 的 test-time compute scaling 逻辑——如果你知道哪些 steps 有 formal guarantee，你可以将额外 compute 集中在 uncertain steps 上。\n\n【发掘点 4】\n- 维度: 前提假设质疑\n- 内容: Proposal 的核心逻辑链有一个关键假设需要预先 address：**formalizability router 的准确率如何影响整体系统的 soundness？** 如果 router 将一个 non-formalizable step 错误路由到 Z3（autoformalization 失败或不忠实），系统会产生 false negative（Z3 无法证明推导 → 错误标记为 miracle step）。如果将一个 formalizable step 错误路由到 neural verifier，系统退化为 neural-only（false negative 在 miracle step detection 上）。这两种错误的 cost 是不对称的：前者产生 false alarm（overly strict），后者遗漏 miracle step。建议在 proposal 中明确 formalize 这个 asymmetric cost structure，并讨论 router threshold 的设计应当 favor recall（宁可多送 Z3 也不能遗漏 miracle steps），这同时也是一个 contribution——提供了 router design 的 principled guideline。\n- 价值: 预先回答审稿人最可能的质疑（\"router 错了怎么办？\"），将 potential weakness 转化为 contribution（asymmetric cost-aware routing）。命中 Novelty（cost-aware routing as contribution）和核心 claim 的 logical soundness。\n- 调研依据: Risk-Controlled Lean-as-Judge 的核心贡献之一就是量化 autoformalization 的 faithfulness 限制（43% faithfulness），这直接暗示 router 错误是实际问题而非理论顾虑；FoVer 的 overly-strict behavior 文档也佐证了 false alarm 问题的真实性。\n\n【发掘点 5】\n- 维度: trivial alternative 威胁\n- 内容: 需要预先 address 一个 trivial alternative：**为什么不直接对所有 steps 尝试 autoformalization + Z3，失败了再 fallback 到 neural？** 这个 \"try-formal-first\" baseline 不需要 learned router，也能实现类似的 hybrid coverage。LogicReward 的 Isabelle + token-probability fallback 本质上就是这个策略。本 proposal 的 learned router 相对于这个 trivial baseline 的增量价值需要明确阐述：(1) 避免对必然失败的 steps 浪费 autoformalization compute（efficiency argument），(2) router 的 confidence score 提供 verification uncertainty signal（前述 significance 提升），(3) 更重要的是——直接尝试 formalization 后失败并不等于\"step is non-formalizable\"（可能只是 autoformalization 能力不足），而 learned router 可以学到比 \"autoformalization success/failure\" 更 nuanced 的 formalizability signal。\n- 价值: 如果不 address 这个 trivial alternative，审稿人必然会问\"为什么不直接 try and fallback\"。明确阐述差异化可以预防 reject 理由，同时 point (3) 本身是一个 subtle 且有深度的观察——它暗示 formalizability 是 step 的 intrinsic property 而非 autoformalization system 的 extrinsic capability，这可以成为一个 interesting conceptual contribution。命中 Novelty 和 Related Work 差异化（vs. LogicReward）。\n- 调研依据: LogicReward (ICLR 2026) 使用的正是 Isabelle verification + fallback 策略但无 learned router；VERGE 也用 rule-based routing 而非 learned prediction。\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models](https://arxiv.org/abs/2504.00891)\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)\n- [LogicReward: Step-Wise Logical Supervision](https://openreview.net/forum?id=A3FhAVfcJI)\n- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774)\n- [PRMBench: Fine-grained Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)\n- [Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning](https://arxiv.org/pdf/2603.29500)\n- [Neuro-Symbolic Routing (EmergentMind)](https://www.emergentmind.com/topics/neuro-symbolic-routing)\n\n【补救 agent 本轮输出】:\nNow I have a comprehensive understanding of the experimental landscape. Let me compile my analysis.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **FoVer (ACL 2026 Findings, arXiv 2505.15960)**: 在 ProcessBench 上报告 AUROC，并在 12 个推理 benchmark 上做 Best-of-K 评估。Baseline 包括 Qwen2.5-Math-PRM-72B、Math-Shepherd、多个 LLM-as-Judge。Ablation 包括不同 formal verifier（Z3 vs Isabelle）、训练数据量、不同 base model。\n- **GenPRM (AAAI 2026, arXiv 2504.00891)**: 在 ProcessBench 上做 step-level verification（F1），在 MATH-500、AMC23、AIME24、Minerva Math 上做 Best-of-N reranking。Baseline 包括 Math-Shepherd、Qwen2.5-Math-PRM、ReasoVerify 等。模型规模扩展实验（1.5B/7B/32B）。\n- **ThinkPRM (arXiv 2504.16828)**: 在 ProcessBench、MATH-500、AIME'24 上做 Best-of-N 和 reward-guided search。OOD 评估 GPQA-Diamond 和 LiveCodeBench。关键 ablation：process labels vs outcome-only filtering，compute scaling analysis（同 token budget 下 vs LLM-as-Judge）。\n- **R-PRM (EMNLP 2025, arXiv 2503.21295)**: 在 ProcessBench 和 PRMBench 上达到 SOTA（分别 +13.9 和 +8.5 F1）。三阶段框架：supervised cold-start → DPO self-evolving → inference-time scaling。6 个下游 math benchmark。\n- **LogicReward (ICLR 2026, arXiv 2512.18196)**: 使用 Isabelle 做 step-level 验证，token-probability fallback。在 8 个 logical reasoning / NLI benchmark 上评估。无 ProcessBench/PRMBench 评估，无 learned router，无 miracle step 专门评测。\n- **VERGE (arXiv 2601.20055)**: 手工 Semantic Routing 将 claims 分给 Z3 或 soft verifier。报告 18.7% uplift。无 learned routing，无 PRM-specific benchmark 评估。\n- **RRM / \"Curing Miracle Steps\" (arXiv 2510.07774)**: Rubric-based reward model。Verified Pass@1024 从 26.7% 升至 62.6%，Miracle Step 减少 71%。代码和数据在 GitHub 公开。论文在 OpenReview 上有记录但从 ICLR 2026 withdrawn。\n- **PRMBench (ACL 2025, arXiv 2501.03124)**: 6,216 问题、83,456 step-level labels。PRMScore 作为主评估指标。25 个模型上做了 extensive 评估。含多种 error type 分类维度。\n\n**调研总结**: 当前 PRM 领域的实验标准要求至少两类评估：(1) step-level error detection（ProcessBench F1/AUROC, PRMBench PRMScore），和 (2) Best-of-N downstream reranking（MATH-500, AIME24 等）。强 baseline 必须包含 GenPRM、ThinkPRM、R-PRM、Qwen2.5-Math-PRM 等。对于涉及 routing/hybrid 的系统，审稿人普遍期望 oracle routing upper bound、compute-normalized comparison、以及各 component 的 ablation。\n\n---\n\n【缺陷 1】\n- 类别: baseline 不足或过时\n- 问题: Proposal 仅隐含提及 GenPRM-7B 和 FoVer 作为对比，但未明确列出完整 baseline 列表。缺少以下在 2025-2026 PRM 文献中被广泛使用的强 baseline：**ThinkPRM**（2025，在 ProcessBench 上 SOTA 级表现，且同为 generative verifier）、**R-PRM**（EMNLP 2025，ProcessBench/PRMBench 双 SOTA）、**Qwen2.5-Math-PRM-72B**（几乎所有 PRM 论文的标配 baseline）、**VERGE**（hand-crafted routing baseline，作为 learned routing 的直接对照）、**LogicReward**（ICLR 2026，最近的 formal verification PRM）。尤其是 ThinkPRM 和 R-PRM，如果缺失，审稿人几乎必然要求补实验。\n- 严重度: 可补救\n- 补救方案: 明确构建 baseline 矩阵：(a) 纯 neural PRMs: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B; (b) 纯 formal: FoVer-7B; (c) hybrid: VERGE (hand-crafted routing), LogicReward (Isabelle + fallback); (d) LLM-as-Judge: GPT-4o, QwQ-32B。所有这些模型要么有开源权重，要么有公开 API，可行性无障碍。\n- 调研依据: GenPRM、ThinkPRM、R-PRM 论文均互相作为 baseline，已形成领域标准 baseline 集。\n\n【缺陷 2】\n- 类别: 实验设计不足\n- 问题: Proposal 仅提到在 ProcessBench、PRMBench 和 RRM miracle taxonomy 上做评估，但**完全缺失 Best-of-N downstream reranking 评估**。调研显示，GenPRM 在 MATH-500/AMC23/AIME24/Minerva Math 上做 Best-of-N，FoVer 在 12 个 reasoning benchmark 上做 Best-of-K，ThinkPRM 在 MATH-500/AIME'24 上做 Best-of-N 和 reward-guided search。这是当前 PRM 论文的**标配评估维度**，用于回答\"这个 PRM 在实际使用场景（solution reranking）中有多好\"。仅有 step-level error detection 不够，审稿人会质问 PRM 的实际下游效用。\n- 严重度: 可补救\n- 补救方案: 增加 Best-of-N reranking 评估，至少覆盖 MATH-500 和 AIME24（领域标配）。使用 Qwen2.5-Math-7B-Instruct 作为 generation model（与 GenPRM 一致以便公平比较）。如有 compute 余量，增加 AMC23 和 Minerva Math。报告 Pass@1、majority voting、和 PRM reranking 的对比。此评估仅需对 existing solutions 做 inference-time scoring，compute 需求远低于训练。\n- 调研依据: GenPRM、FoVer、ThinkPRM、R-PRM 全部包含此评估，是 PRM 领域 2025-2026 的强制性实验规范。\n\n【缺陷 3】\n- 类别: ablation 不完整\n- 问题: Proposal 未描述任何 ablation study。对于一个核心贡献是\"learned routing\"的系统，缺少 ablation 是致命的实验设计缺陷。审稿人需要看到每个组件的独立贡献被隔离验证。\n- 严重度: 可补救\n- 补救方案: 设计以下 ablation 矩阵：\n  1. **Formal-only baseline**: 对所有 step 做 Z3 verification（展示低 coverage 导致的性能降低）\n  2. **Neural-only baseline**: 对所有 step 用 GenPRM（展示无 formal verification 时 miracle step 漏检）\n  3. **Random routing**: 随机以 50% 概率分配 formal/neural（控制路由本身的贡献 vs. 仅仅 ensemble 效果）\n  4. **Oracle routing**: 使用 ground-truth formalizability label（performance ceiling，衡量 router 质量瓶颈）\n  5. **Router threshold sweep**: 在 formalizability score 的不同阈值下画 coverage-accuracy trade-off 曲线\n  6. **Router architecture ablation**: Qwen3-8B vs 更小模型（如 Qwen3-1.5B）作为 router，衡量 router 规模对整体系统的影响\n  7. **ARES calibration 的贡献**: 有 vs 无 calibration 的 neural branch\n- 调研依据: VERGE 论文中展示了 routing vs no-routing 的对比；ThinkPRM 做了 process labels vs outcome-only filtering 的 ablation；GenPRM 做了 model scaling ablation。routing-based system 的 ablation 标准参照 mixture-of-experts 文献的实验规范。\n\n【缺陷 4】\n- 类别: compute 公平性问题\n- 问题: Proposal 未讨论 compute-normalized comparison。FormalRoute-PRM 的推理管线涉及三个模型/系统的串联调用：(1) Qwen3-8B router 推理，(2) 对 formalizable steps 做 autoformalization + Z3 求解，(3) 对 non-formalizable steps 做 GenPRM-7B 推理。这比单一 GenPRM-7B 推理的 compute cost 高出数倍。如果不做 compute-normalized comparison，审稿人会质疑：\"同样的 compute budget 下，是不是直接多跑几轮 GenPRM majority voting / ThinkPRM 就能达到同样效果？\"ThinkPRM 论文已经明确做了同 token budget 下的对比。\n- 严重度: 可补救\n- 补救方案: (1) 报告 FormalRoute-PRM 和所有 baseline 在每个 test case 上的**平均推理时间**和 **FLOPs/token count**；(2) 在同等 compute budget 下，用 GenPRM 做 majority voting（sample N 次取多数）作为 compute-matched baseline；(3) 画 accuracy vs. compute 的 Pareto 曲线，展示 FormalRoute-PRM 在 Pareto front 上的位置。这在 test-time compute scaling 文献中是标准做法。\n- 调研依据: ThinkPRM 明确做了 \"under the same token budget\" 的对比（outperforming LLM-as-Judge by 7.2%），GenPRM 也做了 test-time compute scaling 分析。\n\n【缺陷 5】\n- 类别: 可行性问题\n- 问题: Proposal 提到在 \"RRM miracle step taxonomy\" 上做评估，但 RRM 论文从 ICLR 2026 withdrawn。虽然 RRM 的代码和数据在 GitHub 公开（github.com/YouliangYuan/rrm-cure-miracle-steps），但需要验证：(a) miracle step taxonomy 的标注数据是否包含在 repo 中且可直接使用，(b) taxonomy 的标注质量和规模是否足以作为 evaluation benchmark，(c) 作为 withdrawn paper 的评估标准是否会被审稿人接受。\n- 严重度: 可补救\n- 补救方案: (1) 立即检查 RRM GitHub repo 确认数据可用性和规模；(2) 如果数据充分，可以使用但需要在论文中明确说明来源和质量（不要称其为\"RRM benchmark\"，而是描述为\"miracle step annotations from [Yuan et al., 2025]\"）；(3) 作为补充，可以用 **PRMBench 中的对应 error type categories** 做 miracle step 相关的 fine-grained 分析，因为 PRMBench 是 ACL 2025 正式发表的 benchmark，审稿人接受度更高；(4) 考虑构建小规模的 **human-annotated miracle step test set**（50-100 examples），由作者团队标注，作为最可信的 gold standard。\n- 调研依据: RRM 在 OpenReview 有记录但 withdrawn；PRMBench (ACL 2025) 包含 fine-grained error type 分类，是更稳健的评估来源。\n\n【缺陷 6】\n- 类别: 实验设计不足\n- 问题: Proposal 提到 router 训练用 \"FoVer Z3 labels + autoformalization success signals\"，但未讨论**训练数据的域偏移问题**。FoVer 的训练数据来源是 formal logic 和 theorem proving tasks，但 ProcessBench/PRMBench 的测试数据是 general mathematical reasoning（competition math, Olympiad problems）。Router 在 formal reasoning tasks 上训练，但在 general math reasoning 上测试，存在显著的 distribution shift。此外，\"autoformalization success signals\" 的具体定义不清：是 Z3 编译成功？还是语义保真验证通过？前者容易获得但不可靠，后者可靠但难以大规模标注。\n- 严重度: 可补救\n- 补救方案: (1) 明确 formalizability label 的定义和标注流程——建议定义为\"autoformalization 后 Z3 编译通过 AND 语义等价验证通过（roundtrip verification）\"，参考 Faithful Autoformalization via Roundtrip Verification (arXiv 2604.25031)；(2) 报告 router 在 in-domain（formal reasoning）和 out-of-domain（general math）上的分类准确率、precision、recall；(3) 在 ablation 中加入 **domain adaptation** 对比：用少量 ProcessBench/PRMBench 样本做 router 的 few-shot adaptation 或 continued fine-tuning，量化域偏移的影响；(4) 作为 upper bound，用 oracle formalizability labels（人工标注 100-200 examples）衡量 router quality 对整体系统的瓶颈程度。\n- 调研依据: Risk-Controlled Lean-as-Judge 报告的 43% faithfulness 数据表明 autoformalization 质量仍是瓶颈；Faithful Autoformalization via Roundtrip Verification (2026) 提供了 roundtrip 验证方法论。\n\n【缺陷 7】\n- 类别: 评估方案缺陷\n- 问题: Proposal 未明确定义**各 benchmark 上使用的评估指标**。调研显示不同 benchmark 使用不同指标：ProcessBench 通常报告 F1 和 AUROC，PRMBench 使用 PRMScore，Best-of-N 报告 accuracy。不同 baseline 论文使用的指标也有差异（GenPRM 用 F1，FoVer 用 AUROC）。此外，对于 miracle step detection 这个特定 claim，需要专门报告 **miracle step 类别上的 precision/recall/F1**，而不仅是整体指标。\n- 严重度: 可补救\n- 补救方案: 明确指标体系：(1) ProcessBench: F1（与 GenPRM/R-PRM 对齐）+ AUROC（与 FoVer 对齐），两个都报以确保可比性；(2) PRMBench: PRMScore + 各 error type 的 breakdown；(3) Best-of-N: Pass@1, Pass@N (N=8,16,64), majority voting 和 PRM reranking 对比；(4) Miracle step detection: 在 RRM/PRMBench 相关子集上报告 miracle step specific 的 precision、recall、F1，以及 false negative rate（漏检的 miracle step 比例，这是 proposal 的核心 claim）；(5) 路由统计: formalizability positive rate、routing accuracy、formal branch coverage。\n- 调研依据: GenPRM 用 F1，FoVer 用 AUROC，R-PRM 用 F1 score，ThinkPRM 用 accuracy@N；指标需要对齐以确保与每个 baseline 的可比性。\n\n【缺陷 8】\n- 类别: 可行性问题\n- 问题: Proposal 声称 \"single-node H100 experimentation\"，但未给出具体的 compute budget 估算。需要训练的组件包括：(1) Qwen3-8B formalizability classifier 的 fine-tuning，(2) 可能需要对 GenPRM-7B 做 ARES-style calibration。此外，推理时需要对每个 test step 做 autoformalization（调用 LLM） + Z3 求解（对 formalizable steps）或 GenPRM inference。在 ProcessBench 3,400 cases × 每个 case 多个 steps 的规模下，需要估算总推理时间。\n- 严重度: 可补救（实际 compute 需求在学术预算内，但需要明确估算）\n- 补救方案: 给出 compute breakdown：(1) Router training: Qwen3-8B LoRA fine-tuning ≈ 4-8 GPU-hours on single H100（基于调研数据，FoVer 训练集约 80K 样本，LoRA fine-tuning 8B 模型在此规模下 2-4 小时可完成）；(2) Autoformalization inference: 估算 ProcessBench + PRMBench 总 step 数 × 每 step autoformalization 的 token cost；(3) Z3 solve time: Z3 单个 formula 求解通常在毫秒级，不构成瓶颈；(4) GenPRM-7B inference: 标准 7B 推理，单 H100 可处理；(5) 总计预估：training < 1 天，full evaluation pipeline < 2-3 天，在学术 compute budget 内完全可行。论文中加入 compute cost table 增加可信度。\n- 调研依据: 调研显示 Qwen3-8B LoRA fine-tuning 在 A100 上 2-4 小时，H100 更快；Z3 求解在 consumer CPU 上 150 rules < 10 分钟。\n\n---\n\n**总结**: Proposal 的实验设计有 8 个可补救缺陷，无不可补救的致命缺陷。最严重的 3 个问题是：**(1) 缺少 Best-of-N downstream 评估**（PRM 论文硬性要求）、**(2) baseline 列表不完整**（缺 ThinkPRM、R-PRM 等强 baseline）、**(3) 无 ablation 设计**（routing system 必须有 component isolation）。这些都是完全可补救的，且 compute/data 可行性均无障碍。补全后实验设计可达 AAAI 主会门槛。\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models](https://arxiv.org/abs/2504.00891)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)\n- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)\n- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774)\n- [PRMBench: Fine-grained Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)\n- [ProcessBench: Identifying Process Errors in Mathematical Reasoning](https://huggingface.co/papers/2412.06559)\n- [Faithful Autoformalization via Roundtrip Verification and Repair](https://arxiv.org/html/2604.25031)"
}
```

---

### Runtime record

_source line 13 · 2026-05-29T06:08:14.189Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:08:14.189Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

## Round 2

35 recorded events

### User

_source line 14 · 2026-05-29T06:08:14.224Z_

【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have sufficient background to provide my analysis. Let me synthesize my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960) (ACL 2026 Findings): 使用 Z3/Isabelle 自动标注 step-level error labels 训练 PRM，但仅在 formally verifiable data 上训练，对 informal reasoning 存在 documented overly-strict behavior。核心 insight：formal verification 可以提供高质量 PRM 训练信号，但覆盖面有限。
- [GenPRM: Scaling Test-Time Compute of PRMs](https://arxiv.org/abs/2504.00891) (AAAI 2026): 7B 模型通过 generative CoT + code verification 超越 72B 模型。核心 insight：PRM 可以通过 generative reasoning 而非纯 scalar scoring 大幅提升性能。
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 使用 semantic routing 将 claims 分派到 SMT solver 或 LLM ensemble——但路由基于 rule-based claim type classification，非 learned routing。明确提出 Minimal Correction Subsets (MCS) 做 error localization。
- [LogicReward: Step-Wise Logical Supervision](https://openreview.net/forum?id=A3FhAVfcJI) (ICLR 2026): 用 Isabelle 做 step-level formal verification + token-probability fallback，但无 trained neural verifier branch，无 explicit formalizability classifier。
- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774) (arXiv 2025, ICLR 2026 under review): 定义 miracle step taxonomy，RRM 减少 71% miracle steps，但方法是 outcome-oriented rubric scoring，未尝试 formal derivability checking。
- [PRoSFI / Structured Formal Intermediaries](https://arxiv.org/pdf/2603.29500) (2026): 模型输出 structured intermediate steps aligned with natural language reasoning，由 formal prover 验证——接近本 proposal 的 formalization pipeline 但方向不同（generation-side 而非 verification-side）。
- 调研总结：当前领域的研究者主要在两条路线上突破——(1) 用 formal verification 提供更精确的 training signal（FoVer, LogicReward），(2) 增强 neural PRM 的 generative reasoning 能力（GenPRM, ARES）。**将这两条路线通过 learned routing 动态结合是一个已被 VERGE 识别但未被实现的 open problem**，本 proposal 正好定位在这个缺口上。

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: Proposal 当前的核心 claim 是"learned router + hybrid verification → catch miracle steps"。但这个 claim 的逻辑链条有一个未被充分阐述的关键环节：**为什么 formal derivability checking 对 miracle steps 特别有效？** Miracle steps 的定义是"unjustified logical leaps"——如果将 step S_i 的 predecessors {S_1,...,S_{i-1}} formalize 后送入 Z3 检查 S_i 是否可推导，那么 miracle step 本质上是 Z3 返回 UNSAT（不可推导）的步骤。这意味着 formal derivability checking 与 miracle step detection 之间存在一个**近乎 definitional 的对应关系**——这不是"可能有效"，而是"在 formalizability 成立的条件下，是 theoretically guaranteed 的检测机制"。建议将此提升为核心理论贡献的第一支柱：在 formalizable steps 子集上，miracle step detection 等价于 Z3 derivability failure，这提供了 neural PRM 无法提供的 soundness guarantee。
- 价值: 将核心 claim 从 empirical（"我们的系统表现更好"）提升到 semi-formal guarantee（"在 coverage 范围内，detection 是 sound 的"），直接命中 Novelty 和 Significance。审稿人看到的不再只是"又一个 hybrid system"，而是"第一个能对 miracle step detection 提供部分 formal guarantee 的 PRM"。
- 调研依据: FoVer 已证明 Z3 derivability labels 的高精度但未将其与 miracle step taxonomy 对接；RRM 定义了 miracle steps 但用 neural rubric 而非 formal methods；两者的 gap 恰好是本 proposal 的理论贡献空间。

【发掘点 2】
- 维度: novelty 锐化
- 内容: 当前 proposal 将自身定位为 "VERGE 的 learned routing 升级"，这有将 novelty 矮化为 incremental improvement 的风险。实际上，VERGE 的 routing 是在 **claim type** 层面（logical claim vs. commonsense claim）做 rule-based 分类，而本 proposal 的 router 是在 **formal derivability potential** 层面做 learned prediction——这是两个完全不同的分类任务。VERGE 的 router 不需要考虑 predecessors，因为它只看单个 claim 的 type；而本 proposal 的 formalizability 判断是 context-dependent 的（同一个 step 在不同 predecessor context 下可能有不同的 formalizability）。建议明确区分：VERGE 做的是 static type routing（与上下文无关），本 proposal 做的是 dynamic derivability routing（依赖推理链上下文），这是一个 fundamentally harder 且 more informative 的分类问题。
- 价值: 防止审稿人将本工作简单归类为"VERGE + better router"，锐化 novelty 为"context-dependent formalizability prediction 是一个新的研究问题，且其 positive outcome 直接 enables sound miracle step detection"。命中 Novelty 和 Related Work 差异化。
- 调研依据: VERGE paper 的 semantic routing 描述明确表明其 routing 仅基于 claim type taxonomy（verifiable logic vs. ambiguous/commonsense），不考虑推理链上下文。

【发掘点 3】
- 维度: significance 提升
- 内容: Proposal 当前将 significance 定位在"catch miracle steps that neural PRMs miss"——这是 correct 但 narrow 的 framing。更有影响力的 framing 是：**FormalRoute-PRM 提供了一个 principled framework 来量化 PRM 的 verification coverage gap**。具体来说，formalizability router 的输出本身就是一个 per-step "verification confidence" signal——formalizable steps 获得 guaranteed verification，non-formalizable steps 获得 best-effort neural verification，这自然产生了一个 **calibrated confidence hierarchy**。这意味着 FormalRoute-PRM 不仅是一个 better PRM，而是一个能 tell you where it's uncertain 的 PRM——这对 downstream applications（如 RLHF、test-time compute allocation）具有 broader impact。
- 价值: 将 significance 从"detect more errors"提升到"provide principled verification uncertainty quantification"，扩大了 paper 的影响面。Risk-Controlled Lean-as-Judge 已经在做类似的 honest coverage reporting，本 proposal 可以将其发展为 contribution 而非仅仅是 evaluation protocol。命中 Significance。
- 调研依据: Risk-Controlled Lean-as-Judge 的 honest coverage quantification 思路 + GenPRM 的 test-time compute scaling 逻辑——如果你知道哪些 steps 有 formal guarantee，你可以将额外 compute 集中在 uncertain steps 上。

【发掘点 4】
- 维度: 前提假设质疑
- 内容: Proposal 的核心逻辑链有一个关键假设需要预先 address：**formalizability router 的准确率如何影响整体系统的 soundness？** 如果 router 将一个 non-formalizable step 错误路由到 Z3（autoformalization 失败或不忠实），系统会产生 false negative（Z3 无法证明推导 → 错误标记为 miracle step）。如果将一个 formalizable step 错误路由到 neural verifier，系统退化为 neural-only（false negative 在 miracle step detection 上）。这两种错误的 cost 是不对称的：前者产生 false alarm（overly strict），后者遗漏 miracle step。建议在 proposal 中明确 formalize 这个 asymmetric cost structure，并讨论 router threshold 的设计应当 favor recall（宁可多送 Z3 也不能遗漏 miracle steps），这同时也是一个 contribution——提供了 router design 的 principled guideline。
- 价值: 预先回答审稿人最可能的质疑（"router 错了怎么办？"），将 potential weakness 转化为 contribution（asymmetric cost-aware routing）。命中 Novelty（cost-aware routing as contribution）和核心 claim 的 logical soundness。
- 调研依据: Risk-Controlled Lean-as-Judge 的核心贡献之一就是量化 autoformalization 的 faithfulness 限制（43% faithfulness），这直接暗示 router 错误是实际问题而非理论顾虑；FoVer 的 overly-strict behavior 文档也佐证了 false alarm 问题的真实性。

【发掘点 5】
- 维度: trivial alternative 威胁
- 内容: 需要预先 address 一个 trivial alternative：**为什么不直接对所有 steps 尝试 autoformalization + Z3，失败了再 fallback 到 neural？** 这个 "try-formal-first" baseline 不需要 learned router，也能实现类似的 hybrid coverage。LogicReward 的 Isabelle + token-probability fallback 本质上就是这个策略。本 proposal 的 learned router 相对于这个 trivial baseline 的增量价值需要明确阐述：(1) 避免对必然失败的 steps 浪费 autoformalization compute（efficiency argument），(2) router 的 confidence score 提供 verification uncertainty signal（前述 significance 提升），(3) 更重要的是——直接尝试 formalization 后失败并不等于"step is non-formalizable"（可能只是 autoformalization 能力不足），而 learned router 可以学到比 "autoformalization success/failure" 更 nuanced 的 formalizability signal。
- 价值: 如果不 address 这个 trivial alternative，审稿人必然会问"为什么不直接 try and fallback"。明确阐述差异化可以预防 reject 理由，同时 point (3) 本身是一个 subtle 且有深度的观察——它暗示 formalizability 是 step 的 intrinsic property 而非 autoformalization system 的 extrinsic capability，这可以成为一个 interesting conceptual contribution。命中 Novelty 和 Related Work 差异化（vs. LogicReward）。
- 调研依据: LogicReward (ICLR 2026) 使用的正是 Isabelle verification + fallback 策略但无 learned router；VERGE 也用 rule-based routing 而非 learned prediction。

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models](https://arxiv.org/abs/2504.00891)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [LogicReward: Step-Wise Logical Supervision](https://openreview.net/forum?id=A3FhAVfcJI)
- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774)
- [PRMBench: Fine-grained Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)
- [Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning](https://arxiv.org/pdf/2603.29500)
- [Neuro-Symbolic Routing (EmergentMind)](https://www.emergentmind.com/topics/neuro-symbolic-routing)

【补救 agent 本轮输出】:
Now I have a comprehensive understanding of the experimental landscape. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **FoVer (ACL 2026 Findings, arXiv 2505.15960)**: 在 ProcessBench 上报告 AUROC，并在 12 个推理 benchmark 上做 Best-of-K 评估。Baseline 包括 Qwen2.5-Math-PRM-72B、Math-Shepherd、多个 LLM-as-Judge。Ablation 包括不同 formal verifier（Z3 vs Isabelle）、训练数据量、不同 base model。
- **GenPRM (AAAI 2026, arXiv 2504.00891)**: 在 ProcessBench 上做 step-level verification（F1），在 MATH-500、AMC23、AIME24、Minerva Math 上做 Best-of-N reranking。Baseline 包括 Math-Shepherd、Qwen2.5-Math-PRM、ReasoVerify 等。模型规模扩展实验（1.5B/7B/32B）。
- **ThinkPRM (arXiv 2504.16828)**: 在 ProcessBench、MATH-500、AIME'24 上做 Best-of-N 和 reward-guided search。OOD 评估 GPQA-Diamond 和 LiveCodeBench。关键 ablation：process labels vs outcome-only filtering，compute scaling analysis（同 token budget 下 vs LLM-as-Judge）。
- **R-PRM (EMNLP 2025, arXiv 2503.21295)**: 在 ProcessBench 和 PRMBench 上达到 SOTA（分别 +13.9 和 +8.5 F1）。三阶段框架：supervised cold-start → DPO self-evolving → inference-time scaling。6 个下游 math benchmark。
- **LogicReward (ICLR 2026, arXiv 2512.18196)**: 使用 Isabelle 做 step-level 验证，token-probability fallback。在 8 个 logical reasoning / NLI benchmark 上评估。无 ProcessBench/PRMBench 评估，无 learned router，无 miracle step 专门评测。
- **VERGE (arXiv 2601.20055)**: 手工 Semantic Routing 将 claims 分给 Z3 或 soft verifier。报告 18.7% uplift。无 learned routing，无 PRM-specific benchmark 评估。
- **RRM / "Curing Miracle Steps" (arXiv 2510.07774)**: Rubric-based reward model。Verified Pass@1024 从 26.7% 升至 62.6%，Miracle Step 减少 71%。代码和数据在 GitHub 公开。论文在 OpenReview 上有记录但从 ICLR 2026 withdrawn。
- **PRMBench (ACL 2025, arXiv 2501.03124)**: 6,216 问题、83,456 step-level labels。PRMScore 作为主评估指标。25 个模型上做了 extensive 评估。含多种 error type 分类维度。

**调研总结**: 当前 PRM 领域的实验标准要求至少两类评估：(1) step-level error detection（ProcessBench F1/AUROC, PRMBench PRMScore），和 (2) Best-of-N downstream reranking（MATH-500, AIME24 等）。强 baseline 必须包含 GenPRM、ThinkPRM、R-PRM、Qwen2.5-Math-PRM 等。对于涉及 routing/hybrid 的系统，审稿人普遍期望 oracle routing upper bound、compute-normalized comparison、以及各 component 的 ablation。

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: Proposal 仅隐含提及 GenPRM-7B 和 FoVer 作为对比，但未明确列出完整 baseline 列表。缺少以下在 2025-2026 PRM 文献中被广泛使用的强 baseline：**ThinkPRM**（2025，在 ProcessBench 上 SOTA 级表现，且同为 generative verifier）、**R-PRM**（EMNLP 2025，ProcessBench/PRMBench 双 SOTA）、**Qwen2.5-Math-PRM-72B**（几乎所有 PRM 论文的标配 baseline）、**VERGE**（hand-crafted routing baseline，作为 learned routing 的直接对照）、**LogicReward**（ICLR 2026，最近的 formal verification PRM）。尤其是 ThinkPRM 和 R-PRM，如果缺失，审稿人几乎必然要求补实验。
- 严重度: 可补救
- 补救方案: 明确构建 baseline 矩阵：(a) 纯 neural PRMs: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B; (b) 纯 formal: FoVer-7B; (c) hybrid: VERGE (hand-crafted routing), LogicReward (Isabelle + fallback); (d) LLM-as-Judge: GPT-4o, QwQ-32B。所有这些模型要么有开源权重，要么有公开 API，可行性无障碍。
- 调研依据: GenPRM、ThinkPRM、R-PRM 论文均互相作为 baseline，已形成领域标准 baseline 集。

【缺陷 2】
- 类别: 实验设计不足
- 问题: Proposal 仅提到在 ProcessBench、PRMBench 和 RRM miracle taxonomy 上做评估，但**完全缺失 Best-of-N downstream reranking 评估**。调研显示，GenPRM 在 MATH-500/AMC23/AIME24/Minerva Math 上做 Best-of-N，FoVer 在 12 个 reasoning benchmark 上做 Best-of-K，ThinkPRM 在 MATH-500/AIME'24 上做 Best-of-N 和 reward-guided search。这是当前 PRM 论文的**标配评估维度**，用于回答"这个 PRM 在实际使用场景（solution reranking）中有多好"。仅有 step-level error detection 不够，审稿人会质问 PRM 的实际下游效用。
- 严重度: 可补救
- 补救方案: 增加 Best-of-N reranking 评估，至少覆盖 MATH-500 和 AIME24（领域标配）。使用 Qwen2.5-Math-7B-Instruct 作为 generation model（与 GenPRM 一致以便公平比较）。如有 compute 余量，增加 AMC23 和 Minerva Math。报告 Pass@1、majority voting、和 PRM reranking 的对比。此评估仅需对 existing solutions 做 inference-time scoring，compute 需求远低于训练。
- 调研依据: GenPRM、FoVer、ThinkPRM、R-PRM 全部包含此评估，是 PRM 领域 2025-2026 的强制性实验规范。

【缺陷 3】
- 类别: ablation 不完整
- 问题: Proposal 未描述任何 ablation study。对于一个核心贡献是"learned routing"的系统，缺少 ablation 是致命的实验设计缺陷。审稿人需要看到每个组件的独立贡献被隔离验证。
- 严重度: 可补救
- 补救方案: 设计以下 ablation 矩阵：
  1. **Formal-only baseline**: 对所有 step 做 Z3 verification（展示低 coverage 导致的性能降低）
  2. **Neural-only baseline**: 对所有 step 用 GenPRM（展示无 formal verification 时 miracle step 漏检）
  3. **Random routing**: 随机以 50% 概率分配 formal/neural（控制路由本身的贡献 vs. 仅仅 ensemble 效果）
  4. **Oracle routing**: 使用 ground-truth formalizability label（performance ceiling，衡量 router 质量瓶颈）
  5. **Router threshold sweep**: 在 formalizability score 的不同阈值下画 coverage-accuracy trade-off 曲线
  6. **Router architecture ablation**: Qwen3-8B vs 更小模型（如 Qwen3-1.5B）作为 router，衡量 router 规模对整体系统的影响
  7. **ARES calibration 的贡献**: 有 vs 无 calibration 的 neural branch
- 调研依据: VERGE 论文中展示了 routing vs no-routing 的对比；ThinkPRM 做了 process labels vs outcome-only filtering 的 ablation；GenPRM 做了 model scaling ablation。routing-based system 的 ablation 标准参照 mixture-of-experts 文献的实验规范。

【缺陷 4】
- 类别: compute 公平性问题
- 问题: Proposal 未讨论 compute-normalized comparison。FormalRoute-PRM 的推理管线涉及三个模型/系统的串联调用：(1) Qwen3-8B router 推理，(2) 对 formalizable steps 做 autoformalization + Z3 求解，(3) 对 non-formalizable steps 做 GenPRM-7B 推理。这比单一 GenPRM-7B 推理的 compute cost 高出数倍。如果不做 compute-normalized comparison，审稿人会质疑："同样的 compute budget 下，是不是直接多跑几轮 GenPRM majority voting / ThinkPRM 就能达到同样效果？"ThinkPRM 论文已经明确做了同 token budget 下的对比。
- 严重度: 可补救
- 补救方案: (1) 报告 FormalRoute-PRM 和所有 baseline 在每个 test case 上的**平均推理时间**和 **FLOPs/token count**；(2) 在同等 compute budget 下，用 GenPRM 做 majority voting（sample N 次取多数）作为 compute-matched baseline；(3) 画 accuracy vs. compute 的 Pareto 曲线，展示 FormalRoute-PRM 在 Pareto front 上的位置。这在 test-time compute scaling 文献中是标准做法。
- 调研依据: ThinkPRM 明确做了 "under the same token budget" 的对比（outperforming LLM-as-Judge by 7.2%），GenPRM 也做了 test-time compute scaling 分析。

【缺陷 5】
- 类别: 可行性问题
- 问题: Proposal 提到在 "RRM miracle step taxonomy" 上做评估，但 RRM 论文从 ICLR 2026 withdrawn。虽然 RRM 的代码和数据在 GitHub 公开（github.com/YouliangYuan/rrm-cure-miracle-steps），但需要验证：(a) miracle step taxonomy 的标注数据是否包含在 repo 中且可直接使用，(b) taxonomy 的标注质量和规模是否足以作为 evaluation benchmark，(c) 作为 withdrawn paper 的评估标准是否会被审稿人接受。
- 严重度: 可补救
- 补救方案: (1) 立即检查 RRM GitHub repo 确认数据可用性和规模；(2) 如果数据充分，可以使用但需要在论文中明确说明来源和质量（不要称其为"RRM benchmark"，而是描述为"miracle step annotations from [Yuan et al., 2025]"）；(3) 作为补充，可以用 **PRMBench 中的对应 error type categories** 做 miracle step 相关的 fine-grained 分析，因为 PRMBench 是 ACL 2025 正式发表的 benchmark，审稿人接受度更高；(4) 考虑构建小规模的 **human-annotated miracle step test set**（50-100 examples），由作者团队标注，作为最可信的 gold standard。
- 调研依据: RRM 在 OpenReview 有记录但 withdrawn；PRMBench (ACL 2025) 包含 fine-grained error type 分类，是更稳健的评估来源。

【缺陷 6】
- 类别: 实验设计不足
- 问题: Proposal 提到 router 训练用 "FoVer Z3 labels + autoformalization success signals"，但未讨论**训练数据的域偏移问题**。FoVer 的训练数据来源是 formal logic 和 theorem proving tasks，但 ProcessBench/PRMBench 的测试数据是 general mathematical reasoning（competition math, Olympiad problems）。Router 在 formal reasoning tasks 上训练，但在 general math reasoning 上测试，存在显著的 distribution shift。此外，"autoformalization success signals" 的具体定义不清：是 Z3 编译成功？还是语义保真验证通过？前者容易获得但不可靠，后者可靠但难以大规模标注。
- 严重度: 可补救
- 补救方案: (1) 明确 formalizability label 的定义和标注流程——建议定义为"autoformalization 后 Z3 编译通过 AND 语义等价验证通过（roundtrip verification）"，参考 Faithful Autoformalization via Roundtrip Verification (arXiv 2604.25031)；(2) 报告 router 在 in-domain（formal reasoning）和 out-of-domain（general math）上的分类准确率、precision、recall；(3) 在 ablation 中加入 **domain adaptation** 对比：用少量 ProcessBench/PRMBench 样本做 router 的 few-shot adaptation 或 continued fine-tuning，量化域偏移的影响；(4) 作为 upper bound，用 oracle formalizability labels（人工标注 100-200 examples）衡量 router quality 对整体系统的瓶颈程度。
- 调研依据: Risk-Controlled Lean-as-Judge 报告的 43% faithfulness 数据表明 autoformalization 质量仍是瓶颈；Faithful Autoformalization via Roundtrip Verification (2026) 提供了 roundtrip 验证方法论。

【缺陷 7】
- 类别: 评估方案缺陷
- 问题: Proposal 未明确定义**各 benchmark 上使用的评估指标**。调研显示不同 benchmark 使用不同指标：ProcessBench 通常报告 F1 和 AUROC，PRMBench 使用 PRMScore，Best-of-N 报告 accuracy。不同 baseline 论文使用的指标也有差异（GenPRM 用 F1，FoVer 用 AUROC）。此外，对于 miracle step detection 这个特定 claim，需要专门报告 **miracle step 类别上的 precision/recall/F1**，而不仅是整体指标。
- 严重度: 可补救
- 补救方案: 明确指标体系：(1) ProcessBench: F1（与 GenPRM/R-PRM 对齐）+ AUROC（与 FoVer 对齐），两个都报以确保可比性；(2) PRMBench: PRMScore + 各 error type 的 breakdown；(3) Best-of-N: Pass@1, Pass@N (N=8,16,64), majority voting 和 PRM reranking 对比；(4) Miracle step detection: 在 RRM/PRMBench 相关子集上报告 miracle step specific 的 precision、recall、F1，以及 false negative rate（漏检的 miracle step 比例，这是 proposal 的核心 claim）；(5) 路由统计: formalizability positive rate、routing accuracy、formal branch coverage。
- 调研依据: GenPRM 用 F1，FoVer 用 AUROC，R-PRM 用 F1 score，ThinkPRM 用 accuracy@N；指标需要对齐以确保与每个 baseline 的可比性。

【缺陷 8】
- 类别: 可行性问题
- 问题: Proposal 声称 "single-node H100 experimentation"，但未给出具体的 compute budget 估算。需要训练的组件包括：(1) Qwen3-8B formalizability classifier 的 fine-tuning，(2) 可能需要对 GenPRM-7B 做 ARES-style calibration。此外，推理时需要对每个 test step 做 autoformalization（调用 LLM） + Z3 求解（对 formalizable steps）或 GenPRM inference。在 ProcessBench 3,400 cases × 每个 case 多个 steps 的规模下，需要估算总推理时间。
- 严重度: 可补救（实际 compute 需求在学术预算内，但需要明确估算）
- 补救方案: 给出 compute breakdown：(1) Router training: Qwen3-8B LoRA fine-tuning ≈ 4-8 GPU-hours on single H100（基于调研数据，FoVer 训练集约 80K 样本，LoRA fine-tuning 8B 模型在此规模下 2-4 小时可完成）；(2) Autoformalization inference: 估算 ProcessBench + PRMBench 总 step 数 × 每 step autoformalization 的 token cost；(3) Z3 solve time: Z3 单个 formula 求解通常在毫秒级，不构成瓶颈；(4) GenPRM-7B inference: 标准 7B 推理，单 H100 可处理；(5) 总计预估：training < 1 天，full evaluation pipeline < 2-3 天，在学术 compute budget 内完全可行。论文中加入 compute cost table 增加可信度。
- 调研依据: 调研显示 Qwen3-8B LoRA fine-tuning 在 A100 上 2-4 小时，H100 更快；Z3 求解在 consumer CPU 上 150 rules < 10 分钟。

---

**总结**: Proposal 的实验设计有 8 个可补救缺陷，无不可补救的致命缺陷。最严重的 3 个问题是：**(1) 缺少 Best-of-N downstream 评估**（PRM 论文硬性要求）、**(2) baseline 列表不完整**（缺 ThinkPRM、R-PRM 等强 baseline）、**(3) 无 ablation 设计**（routing system 必须有 component isolation）。这些都是完全可补救的，且 compute/data 可行性均无障碍。补全后实验设计可达 AAAI 主会门槛。

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models](https://arxiv.org/abs/2504.00891)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774)
- [PRMBench: Fine-grained Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)
- [ProcessBench: Identifying Process Errors in Mathematical Reasoning](https://huggingface.co/papers/2412.06559)
- [Faithful Autoformalization via Roundtrip Verification and Repair](https://arxiv.org/html/2604.25031)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3acaf4d1-5601-43e6-8323-7d910becf692",
  "isSidechain": false,
  "promptId": "ddf771f7-002d-42e7-9636-95691e6cb81d",
  "type": "user",
  "uuid": "5d3c9d04-27d2-47f1-b0a8-d5775cf37cca",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient background to provide my analysis. Let me synthesize my findings.  ---  【状态】: 有发掘空间…",
  "leafUuid": "5d3c9d04-27d2-47f1-b0a8-d5775cf37cca",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Assistant

_source line 17 · 2026-05-29T06:08:29.484Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the outputs from both the 发掘 agent and 补救 agent, then perform cross-validation research before integrating their suggestions.

**发掘 agent summary:**
- Status: 有发掘空间
- 5 points identified:
  1. Strengthen core claim: Z3 derivability failure ≡ miracle step detection on formalizable subset (semi-formal guarantee)
  2. Sharpen novelty: VERGE does static type routing vs. this proposal's dynamic derivability routing (context-dependent)
  3. Elevate significance: calibrated confidence hierarchy, verification uncertainty quantification
  4. Address router accuracy assumption: asymmetric cost structure, threshold design
  5. Address trivial alternative threat: "try-formal-first" baseline vs. learned router

**补救 agent summary:**
- Status: 有缺陷待补救
- 8 defects identified:
  1. Incomplete baselines (missing ThinkPRM, R-PRM, etc.)
  2. Missing Best-of-N downstream evaluation
  3. No ablation study designed
  4. No compute-normalized comparison
  5. RRM data availability uncertainty
  6. Router training domain shift issue
  7. Unclear evaluation metrics
  8. No compute budget estimation

Now I need to cross-validate these findings and identify which improvements would have the most impact on the paper's contribution.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d3c9d04-27d2-47f1-b0a8-d5775cf37cca",
  "isSidechain": false,
  "requestId": "req_011CbWMrLQrDEZdHFukjW37u",
  "type": "assistant",
  "uuid": "0f790de4-7f72-4c56-895e-a9519e500348",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STCkUfCp6SuZnk3UCYJVeV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9956,
      "cache_read_input_tokens": 19100,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 591,
          "cache_read_input_tokens": 19100,
          "cache_creation_input_tokens": 9956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9956
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

_source line 18 · 2026-05-29T06:08:29.815Z_

我需要对两个 worker 的关键建议进行交叉验证。让我先做几轮 WebSearch。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f790de4-7f72-4c56-895e-a9519e500348",
  "isSidechain": false,
  "requestId": "req_011CbWMrLQrDEZdHFukjW37u",
  "type": "assistant",
  "uuid": "a0df3b60-2841-4640-b60b-473971390493",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STCkUfCp6SuZnk3UCYJVeV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9956,
      "cache_read_input_tokens": 19100,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 591,
          "cache_read_input_tokens": 19100,
          "cache_creation_input_tokens": 9956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9956
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

_source line 19 · 2026-05-29T06:08:30.236Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PxWxJaKQDPBMG12EWB8RMY`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0df3b60-2841-4640-b60b-473971390493",
  "isSidechain": false,
  "requestId": "req_011CbWMrLQrDEZdHFukjW37u",
  "type": "assistant",
  "uuid": "b2c5ecbf-bd4c-4d97-8f21-738901de7489",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01STCkUfCp6SuZnk3UCYJVeV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9956,
      "cache_read_input_tokens": 19100,
      "output_tokens": 591,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 591,
          "cache_read_input_tokens": 19100,
          "cache_creation_input_tokens": 9956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9956
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

_source line 20 · 2026-05-29T06:08:30.246Z_

<details><summary>↩ Tool result · `toolu_01PxWxJaKQDPBMG12EWB8RMY`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b2c5ecbf-bd4c-4d97-8f21-738901de7489",
  "isSidechain": false,
  "promptId": "ddf771f7-002d-42e7-9636-95691e6cb81d",
  "type": "user",
  "uuid": "c27c70f8-6a4d-49c0-8265-ad6d7135e248",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "b2c5ecbf-bd4c-4d97-8f21-738901de7489",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-29T06:08:33.444Z_

现在让我进行交叉验证搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c27c70f8-6a4d-49c0-8265-ad6d7135e248",
  "isSidechain": false,
  "requestId": "req_011CbWMsX9Yc3rS3xK5sCcrV",
  "type": "assistant",
  "uuid": "355a3c18-73c2-4b86-8619-cf0851abb912",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RgLNBSwCovc8sxbD7T2ZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 29056,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 198,
          "cache_read_input_tokens": 29056,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 22 · 2026-05-29T06:08:34.384Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TvECViKwPyTrzLTXj8x8GD`</summary>

```json
{
  "query": "ThinkPRM process reward model 2025 ProcessBench benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "355a3c18-73c2-4b86-8619-cf0851abb912",
  "isSidechain": false,
  "requestId": "req_011CbWMsX9Yc3rS3xK5sCcrV",
  "type": "assistant",
  "uuid": "d9c1696c-9bb3-4390-abc8-c5e4be304257",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RgLNBSwCovc8sxbD7T2ZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 29056,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 198,
          "cache_read_input_tokens": 29056,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 23 · 2026-05-29T06:08:34.856Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DTNE87AVKdftWYpkzNsxBq`</summary>

```json
{
  "query": "R-PRM reasoning-driven process reward model EMNLP 2025 ProcessBench PRMBench SOTA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9c1696c-9bb3-4390-abc8-c5e4be304257",
  "isSidechain": false,
  "requestId": "req_011CbWMsX9Yc3rS3xK5sCcrV",
  "type": "assistant",
  "uuid": "98ab27f8-7afe-4f4f-b84f-358f18990a38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RgLNBSwCovc8sxbD7T2ZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 29056,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 198,
          "cache_read_input_tokens": 29056,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 24 · 2026-05-29T06:08:35.417Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011iwDask6hd3n8U45tN8oR6`</summary>

```json
{
  "query": "VERGE formal refinement guidance engine routing mechanism rule-based vs learned 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ab27f8-7afe-4f4f-b84f-358f18990a38",
  "isSidechain": false,
  "requestId": "req_011CbWMsX9Yc3rS3xK5sCcrV",
  "type": "assistant",
  "uuid": "6c6f9be1-8223-4d5c-b12c-e78e850d6c29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RgLNBSwCovc8sxbD7T2ZA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 29056,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1119,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 198,
          "cache_read_input_tokens": 29056,
          "cache_creation_input_tokens": 1119,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1119
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

_source line 25 · 2026-05-29T06:08:41.467Z_

<details><summary>↩ Tool result · `toolu_01TvECViKwPyTrzLTXj8x8GD`</summary>

```text
Web search results for query: "ThinkPRM process reward model 2025 ProcessBench benchmark results"

Links: [{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"ThinkPRM: Process Reward Models That Think","url":"https://mukhal.github.io/projects/thinkprm/"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"Process Reward Models That Think | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.16828v5"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"GitHub - mukhal/ThinkPRM: Process Reward Models That Think","url":"https://github.com/mukhal/thinkprm"}]

Based on the search results, here's what I found about ThinkPRM and its ProcessBench benchmark results:

## Overview

ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. It verifies reasoning via long chain-of-thought and allows effective scaling of test-time compute with minimal supervision.

## ProcessBench Benchmark Results

ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search. 

More specifically on ProcessBench: ThinkPRM demonstrates remarkable data efficiency on ProcessBench—THINKPRM-14B, trained on only 8K process labels, significantly outperforms discriminative PRMs trained on approximately 100 times more data (700K labels from PRM800K).

## Additional Performance Highlights

Under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench. ThinkPRM consistently outperforms both LLM-as-a-judge and discriminative PRM baselines on ProcessBench, with performance improving as more computation is allowed, while LLM-as-a-judge shows inconsistent performance with increased compute.

The paper was first posted in April 2025 and has been updated as recently as December 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9c1696c-9bb3-4390-abc8-c5e4be304257",
  "isSidechain": false,
  "promptId": "ddf771f7-002d-42e7-9636-95691e6cb81d",
  "type": "user",
  "uuid": "3b5815d5-c183-4b68-b746-c8c3d2ee7a01",
  "toolUseResult": {
    "query": "ThinkPRM process reward model 2025 ProcessBench benchmark results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RvTugYKohhLgUkvN8RQ9u4",
        "content": [
          {
            "title": "[2504.16828] Process Reward Models That Think",
            "url": "https://arxiv.org/abs/2504.16828"
          },
          {
            "title": "Process Reward Models That Think | OpenReview",
            "url": "https://openreview.net/forum?id=V727xqBYIW"
          },
          {
            "title": "Paper page - Process Reward Models That Think",
            "url": "https://huggingface.co/papers/2504.16828"
          },
          {
            "title": "ThinkPRM: Process Reward Models That Think",
            "url": "https://mukhal.github.io/projects/thinkprm/"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "Process Reward Models That Think | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2504.16828v5"
          },
          {
            "title": "Process Reward Models: Step-Level Feedback for LLMs",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prm"
          },
          {
            "title": "GitHub - mukhal/ThinkPRM: Process Reward Models That Think",
            "url": "https://github.com/mukhal/thinkprm"
          }
        ]
      },
      "Based on the search results, here's what I found about ThinkPRM and its ProcessBench benchmark results:\n\n## Overview\n\nThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. It verifies reasoning via long chain-of-thought and allows effective scaling of test-time compute with minimal supervision.\n\n## ProcessBench Benchmark Results\n\nThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search. \n\nMore specifically on ProcessBench: ThinkPRM demonstrates remarkable data efficiency on ProcessBench—THINKPRM-14B, trained on only 8K process labels, significantly outperforms discriminative PRMs trained on approximately 100 times more data (700K labels from PRM800K).\n\n## Additional Performance Highlights\n\nUnder the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench. ThinkPRM consistently outperforms both LLM-as-a-judge and discriminative PRM baselines on ProcessBench, with performance improving as more computation is allowed, while LLM-as-a-judge shows inconsistent performance with increased compute.\n\nThe paper was first posted in April 2025 and has been updated as recently as December 2025."
    ],
    "durationSeconds": 7.073851937,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d9c1696c-9bb3-4390-abc8-c5e4be304257",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-29T06:08:41.802Z_

<details><summary>↩ Tool result · `toolu_011iwDask6hd3n8U45tN8oR6`</summary>

```text
Web search results for query: "VERGE formal refinement guidance engine routing mechanism rule-based vs learned 2026"

Links: [{"title":"[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/abs/2601.20055"},{"title":"[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"},{"title":"Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://huggingface.co/papers/2601.20055"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning","url":"https://arxiv.org/pdf/2601.20055"},{"title":"dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.","url":"https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"},{"title":"VERGE: Formal Refinement and Guidance Engine for Verifiable ...","url":"https://ubos.tech/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning-2/"},{"title":"Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News","url":"https://news.ycombinator.com/item?id=46813257"}]

Based on the search results, here's what I found about VERGE:

## Overview

VERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement.

## Routing Mechanism: Rule-Based vs Learned

Regarding the routing mechanism specifically, VERGE uses semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning. This represents a hybrid approach where verification routes claims to SMT, Soft, or Hybrid verifiers based on semantic type.

## Key Components

The framework includes three main innovations:

1. Multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, eliminating the syntactic bias of surface-form metrics

2. Semantic routing that directs different claim types to appropriate verification strategies

3. Precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise

The routing appears to be primarily **rule-based**, using semantic classification of claim types to determine which verification approach to apply, rather than a learned routing mechanism.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6c6f9be1-8223-4d5c-b12c-e78e850d6c29",
  "isSidechain": false,
  "promptId": "ddf771f7-002d-42e7-9636-95691e6cb81d",
  "type": "user",
  "uuid": "7c83284e-286d-41df-9ad6-12c84c150ce4",
  "toolUseResult": {
    "query": "VERGE formal refinement guidance engine routing mechanism rule-based vs learned 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Cqgd6bDwcRXojVomz31KB8",
        "content": [
          {
            "title": "[2601.20055] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/abs/2601.20055"
          },
          {
            "title": "[Literature Review] VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://www.themoonlight.io/en/review/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning"
          },
          {
            "title": "Paper page - VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://huggingface.co/papers/2601.20055"
          },
          {
            "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
            "url": "https://arxiv.org/pdf/2601.20055"
          },
          {
            "title": "dblp: VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning.",
            "url": "https://dblp.uni-trier.de/rec/journals/corr/abs-2601-20055.html"
          },
          {
            "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable ...",
            "url": "https://ubos.tech/verge-formal-refinement-and-guidance-engine-for-verifiable-llm-reasoning-2/"
          },
          {
            "title": "Verge: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning | Hacker News",
            "url": "https://news.ycombinator.com/item?id=46813257"
          }
        ]
      },
      "Based on the search results, here's what I found about VERGE:\n\n## Overview\n\nVERGE is a neurosymbolic framework that combines LLMs with SMT solvers to produce verification-guided answers through iterative refinement.\n\n## Routing Mechanism: Rule-Based vs Learned\n\nRegarding the routing mechanism specifically, VERGE uses semantic routing that directs different claim types to appropriate verification strategies: symbolic solvers for logical claims and LLM ensembles for commonsense reasoning. This represents a hybrid approach where verification routes claims to SMT, Soft, or Hybrid verifiers based on semantic type.\n\n## Key Components\n\nThe framework includes three main innovations:\n\n1. Multi-model consensus via formal semantic equivalence checking to ensure logic-level alignment between candidates, eliminating the syntactic bias of surface-form metrics\n\n2. Semantic routing that directs different claim types to appropriate verification strategies\n\n3. Precise logical error localization via Minimal Correction Subsets (MCS), which pinpoint the exact subset of claims to revise\n\nThe routing appears to be primarily **rule-based**, using semantic classification of claim types to determine which verification approach to apply, rather than a learned routing mechanism."
    ],
    "durationSeconds": 6.381251616999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6c6f9be1-8223-4d5c-b12c-e78e850d6c29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-29T06:08:43.292Z_

<details><summary>↩ Tool result · `toolu_01DTNE87AVKdftWYpkzNsxBq`</summary>

```text
Web search results for query: "R-PRM reasoning-driven process reward model EMNLP 2025 ProcessBench PRMBench SOTA"

Links: [{"title":"R-PRM: Reasoning-Driven Process Reward Modeling - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.679/"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/2025.emnlp-main.679@ACL"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/pdf/2503.21295"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://github.com/NJUNLP/R-PRM"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"},{"title":"[2503.21295v1] R-PRM: Reasoning-Driven Process Reward Modeling","url":"http://arxiv.org/abs/2503.21295v1"},{"title":"[2503.21295] R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/abs/2503.21295"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://aclanthology.org/2025.emnlp-main.679.pdf"},{"title":"R-PRM: Reasoning-Driven Process Reward Modeling","url":"https://arxiv.org/html/2503.21295v1"}]

Based on the search results, here's what I found about R-PRM:

## R-PRM: Reasoning-Driven Process Reward Modeling

R-PRM is a paper by Shuaijie She, Junxiao Liu, Yifeng Liu, Jiajun Chen, Xin Huang, and Shujian Huang, presented at EMNLP 2025.

### Key Approach

R-PRM is a novel approach that enhances LLMs' ability to evaluate mathematical reasoning step-by-step, consisting of three parts: supervised cold-start, further meta-optimization in a self-evolving style, and finally inference-time-scaling.

### Performance Results

On ProcessBench and PRMBench, R-PRM surpasses strong baselines by 13.9 and 8.5 F1 scores. When applied to guide mathematical reasoning, R-PRM achieves consistent accuracy improvements of over 8.6 points across six challenging datasets.

### Capabilities

R-PRM exhibits more comprehensive evaluation and robust generalization, indicating its broader potential. The paper addresses challenges in Process Reward Model (PRM) development by leveraging stronger LLMs to generate seed data from limited annotations, exploring self-improvement through preference optimization without requiring additional annotated data, and introducing inference time scaling.

The paper was published in the proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing in Suzhou, China.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98ab27f8-7afe-4f4f-b84f-358f18990a38",
  "isSidechain": false,
  "promptId": "ddf771f7-002d-42e7-9636-95691e6cb81d",
  "type": "user",
  "uuid": "84a11740-67e3-4619-9c4c-96f278e1c65d",
  "toolUseResult": {
    "query": "R-PRM reasoning-driven process reward model EMNLP 2025 ProcessBench PRMBench SOTA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DqNxJGnLZnc73dSeqmasTj",
        "content": [
          {
            "title": "R-PRM: Reasoning-Driven Process Reward Modeling - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.679/"
          },
          {
            "title": "R-PRM: Reasoning-Driven Process Reward Modeling | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/venue/2025.emnlp-main.679@ACL"
          },
          {
            "title": "R-PRM: Reasoning-Driven Process Reward Modeling",
            "url": "https://arxiv.org/pdf/2503.21295"
          },
          {
            "title": "R-PRM: Reasoning-Driven Process Reward Modeling",
            "url": "https://github.com/NJUNLP/R-PRM"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          },
          {
            "title": "[2503.21295v1] R-PRM: Reasoning-Driven Process Reward Modeling",
            "url": "http://arxiv.org/abs/2503.21295v1"
          },
          {
            "title": "[2503.21295] R-PRM: Reasoning-Driven Process Reward Modeling",
            "url": "https://arxiv.org/abs/2503.21295"
          },
          {
            "title": "R-PRM: Reasoning-Driven Process Reward Modeling",
            "url": "https://aclanthology.org/2025.emnlp-main.679.pdf"
          },
          {
            "title": "R-PRM: Reasoning-Driven Process Reward Modeling",
            "url": "https://arxiv.org/html/2503.21295v1"
          }
        ]
      },
      "Based on the search results, here's what I found about R-PRM:\n\n## R-PRM: Reasoning-Driven Process Reward Modeling\n\nR-PRM is a paper by Shuaijie She, Junxiao Liu, Yifeng Liu, Jiajun Chen, Xin Huang, and Shujian Huang, presented at EMNLP 2025.\n\n### Key Approach\n\nR-PRM is a novel approach that enhances LLMs' ability to evaluate mathematical reasoning step-by-step, consisting of three parts: supervised cold-start, further meta-optimization in a self-evolving style, and finally inference-time-scaling.\n\n### Performance Results\n\nOn ProcessBench and PRMBench, R-PRM surpasses strong baselines by 13.9 and 8.5 F1 scores. When applied to guide mathematical reasoning, R-PRM achieves consistent accuracy improvements of over 8.6 points across six challenging datasets.\n\n### Capabilities\n\nR-PRM exhibits more comprehensive evaluation and robust generalization, indicating its broader potential. The paper addresses challenges in Process Reward Model (PRM) development by leveraging stronger LLMs to generate seed data from limited annotations, exploring self-improvement through preference optimization without requiring additional annotated data, and introducing inference time scaling.\n\nThe paper was published in the proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing in Suzhou, China."
    ],
    "durationSeconds": 8.432419611000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "98ab27f8-7afe-4f4f-b84f-358f18990a38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-29T06:08:52.101Z_

<details><summary>Logged reasoning block</summary>

```text
Good. All three searches confirm the worker claims:

1. **ThinkPRM** - Confirmed as a strong baseline. Beats discriminative PRMs on ProcessBench with only 8K labels. Published April 2025, active. Clearly a necessary baseline.

2. **R-PRM** - Confirmed EMNLP 2025, ProcessBench +13.9 F1 and PRMBench +8.5 F1 over strong baselines. Clearly a necessary baseline.

3. **VERGE routing** - Confirmed as rule-based semantic routing based on claim type classification, not learned. This validates the 发掘 agent's point about novelty differentiation.
 
Let me check one more thing about LogicReward's fallback mechanism to see if it really is the trivial alternative they're claiming.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84a11740-67e3-4619-9c4c-96f278e1c65d",
  "isSidechain": false,
  "requestId": "req_011CbWMtUgz2iJqtMxVYQUpW",
  "type": "assistant",
  "uuid": "14619c15-e61a-4678-a88d-71d91d5c6179",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PoULezW1ykx1zakQ8zhLHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 30175,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 730,
          "output_tokens": 326,
          "cache_read_input_tokens": 30175,
          "cache_creation_input_tokens": 1714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1714
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

_source line 29 · 2026-05-29T06:08:52.104Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016DBnpjppdxu4u8PchVgxtC`</summary>

```json
{
  "query": "LogicReward ICLR 2026 Isabelle verification token probability fallback mechanism step-wise"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14619c15-e61a-4678-a88d-71d91d5c6179",
  "isSidechain": false,
  "requestId": "req_011CbWMtUgz2iJqtMxVYQUpW",
  "type": "assistant",
  "uuid": "b546dbb4-a807-485f-9ad5-06c85dca75f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PoULezW1ykx1zakQ8zhLHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 30175,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 730,
          "output_tokens": 326,
          "cache_read_input_tokens": 30175,
          "cache_creation_input_tokens": 1714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1714
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

_source line 30 · 2026-05-29T06:08:52.739Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017hiDtSZCmDryJZGkrLNs7v`</summary>

```json
{
  "query": "formalizability prediction learned classifier autoformalization routing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b546dbb4-a807-485f-9ad5-06c85dca75f2",
  "isSidechain": false,
  "requestId": "req_011CbWMtUgz2iJqtMxVYQUpW",
  "type": "assistant",
  "uuid": "a817c35f-d8cb-4c1b-9e82-56ec8fd06699",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PoULezW1ykx1zakQ8zhLHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 730,
      "cache_creation_input_tokens": 1714,
      "cache_read_input_tokens": 30175,
      "output_tokens": 326,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 730,
          "output_tokens": 326,
          "cache_read_input_tokens": 30175,
          "cache_creation_input_tokens": 1714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1714
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

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient background to provide my analysis. Let me synthesize my findings.  ---  【状态】: 有发掘空间…",
  "leafUuid": "a817c35f-d8cb-4c1b-9e82-56ec8fd06699",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Tool result

_source line 33 · 2026-05-29T06:08:58.868Z_

<details><summary>↩ Tool result · `toolu_016DBnpjppdxu4u8PchVgxtC`</summary>

```text
Web search results for query: "LogicReward ICLR 2026 Isabelle verification token probability fallback mechanism step-wise"

Links: [{"title":"Publiced as a conference paper at ICLR 2026 LOGICREWARD:","url":"https://openreview.net/pdf/de9ac22503a1fd3b541e09e4ff9021f87fc357c3.pdf"},{"title":"GitHub - Aiden0526/Logic-Reward: Codes and Data for ICLR 2026 paper \"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\" · GitHub","url":"https://github.com/Aiden0526/Logic-Reward"},{"title":"LogicReward - a Aiden0526 Collection","url":"https://huggingface.co/collections/Aiden0526/logicreward"},{"title":"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision [Quick Review]","url":"https://liner.com/review/logicreward-incentivizing-llm-reasoning-via-stepwise-logical-supervision"},{"title":"Formally Verified Solution Methods for Infinite-Horizon Markov Decision   Processes","url":"https://arxiv.org/pdf/2206.02169"},{"title":"Verifying Probabilistic Correctness in Isabelle with pGCL","url":"https://arxiv.org/pdf/1211.6197"},{"title":"A Verified Compiler for Probability Density Functions","url":"https://arxiv.org/pdf/1707.06901"}]

Based on the search results, I found information about the LogicReward ICLR 2026 paper and its mechanisms:

## LogicReward: ICLR 2026 Paper

LogicReward is a reward function that evaluates unstructured natural language reasoning and provides step-level, symbolically guided rewards, published at ICLR 2026.

## Token Probability Fallback Mechanism

When syntax is invalid, LogicReward falls back to the confidence of the inference, defined as the average token probability. This fallback occurs during the verification process when Isabelle cannot successfully parse the formalized logic.

## Step-Wise Logical Supervision

The system incorporates Autoformalization with Soft Unification to translate natural language into formal logic, and utilizes LogicScore to assess reasoning quality by verifying premise grounding and logical validity, employing the Isabelle theorem prover for formal checks.

## Verification Process

The system parses reasoning with Soft Unification into neo-davidsonian event semantics form and then converts to Isabelle/HOL theory using an LLM. Isabelle evaluates syntactic and semantic validity, checking whether the converted theory satisfies grammar rules and whether the inference is logically valid.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b546dbb4-a807-485f-9ad5-06c85dca75f2",
  "isSidechain": false,
  "promptId": "ddf771f7-002d-42e7-9636-95691e6cb81d",
  "type": "user",
  "uuid": "d0c3a4b4-ff32-4499-ac8a-95604e7b6a87",
  "toolUseResult": {
    "query": "LogicReward ICLR 2026 Isabelle verification token probability fallback mechanism step-wise",
    "results": [
      {
        "tool_use_id": "srvtoolu_013nKjyBkbxG7MMv27vvYaGw",
        "content": [
          {
            "title": "Publiced as a conference paper at ICLR 2026 LOGICREWARD:",
            "url": "https://openreview.net/pdf/de9ac22503a1fd3b541e09e4ff9021f87fc357c3.pdf"
          },
          {
            "title": "GitHub - Aiden0526/Logic-Reward: Codes and Data for ICLR 2026 paper \"LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision\" · GitHub",
            "url": "https://github.com/Aiden0526/Logic-Reward"
          },
          {
            "title": "LogicReward - a Aiden0526 Collection",
            "url": "https://huggingface.co/collections/Aiden0526/logicreward"
          },
          {
            "title": "LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision [Quick Review]",
            "url": "https://liner.com/review/logicreward-incentivizing-llm-reasoning-via-stepwise-logical-supervision"
          },
          {
            "title": "Formally Verified Solution Methods for Infinite-Horizon Markov Decision   Processes",
            "url": "https://arxiv.org/pdf/2206.02169"
          },
          {
            "title": "Verifying Probabilistic Correctness in Isabelle with pGCL",
            "url": "https://arxiv.org/pdf/1211.6197"
          },
          {
            "title": "A Verified Compiler for Probability Density Functions",
            "url": "https://arxiv.org/pdf/1707.06901"
          }
        ]
      },
      "Based on the search results, I found information about the LogicReward ICLR 2026 paper and its mechanisms:\n\n## LogicReward: ICLR 2026 Paper\n\nLogicReward is a reward function that evaluates unstructured natural language reasoning and provides step-level, symbolically guided rewards, published at ICLR 2026.\n\n## Token Probability Fallback Mechanism\n\nWhen syntax is invalid, LogicReward falls back to the confidence of the inference, defined as the average token probability. This fallback occurs during the verification process when Isabelle cannot successfully parse the formalized logic.\n\n## Step-Wise Logical Supervision\n\nThe system incorporates Autoformalization with Soft Unification to translate natural language into formal logic, and utilizes LogicScore to assess reasoning quality by verifying premise grounding and logical validity, employing the Isabelle theorem prover for formal checks.\n\n## Verification Process\n\nThe system parses reasoning with Soft Unification into neo-davidsonian event semantics form and then converts to Isabelle/HOL theory using an LLM. Isabelle evaluates syntactic and semantic validity, checking whether the converted theory satisfies grammar rules and whether the inference is logically valid."
    ],
    "durationSeconds": 6.754438387999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b546dbb4-a807-485f-9ad5-06c85dca75f2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-29T06:09:00.018Z_

<details><summary>↩ Tool result · `toolu_017hiDtSZCmDryJZGkrLNs7v`</summary>

```text
Web search results for query: "formalizability prediction learned classifier autoformalization routing 2025 2026"

Links: [{"title":"[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data","url":"https://arxiv.org/abs/2508.18914"},{"title":"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach | OpenReview","url":"https://openreview.net/forum?id=hUb2At2DsQ"},{"title":"StepFun-Formalizer: Unlocking the Autoformalization Potential","url":"https://arxiv.org/pdf/2508.04440"},{"title":"A Promising Path Towards Autoformalization and General Artificial Intelligence | Intelligent Computer Mathematics","url":"https://dl.acm.org/doi/abs/10.1007/978-3-030-53518-6_1"},{"title":"130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?","url":"https://arxiv.org/pdf/2601.03298"},{"title":"A Promising Path Towards Autoformalization and General Artificial Intelligence","url":"https://research.google/pubs/a-promising-path-towards-autoformalization-and-general-artificial-intelligence/"},{"title":"LTRAG: Enhancing Autoformalization and Self-refinement ...","url":"https://aclanthology.org/2025.findings-acl.126.pdf"}]

Based on the search results, here's what I found regarding formalizability prediction, learned classifiers, autoformalization routing in 2025-2026:

## Recent Autoformalization Research (2025-2026)

The search reveals several active projects in autoformalization, though specific work on "formalizability prediction" as a routing mechanism isn't explicitly detailed. However, there are related advances:

**Key Projects:**

FormaRL is a reinforcement learning framework for autoformalization that integrates syntax checking from Lean compiler and consistency checking from large language models to calculate rewards, showing progress in improving autoformalization success rates.

RAutoformalizer augments statement autoformalization by Dependency Retrieval, retrieving potentially dependent objects from formal libraries, which represents a routing approach to improve autoformalization.

Neuro-symbolic methods like Logic-LM and LINC integrate formalization with LLMs and symbolic solvers, and possibly refinement with LLMs, addressing autoformalization challenges.

**Recent Scale-Up:**

A project running since November 21, 2025 has produced 160k lines of formalized topology, with about 130k lines completed in two weeks from December 22 to January 4, 2026 for about $100 in LLM subscription cost.

The research appears focused on improving autoformalization accuracy and efficiency rather than explicitly routing based on formalizability prediction, though retrieval-based and learned routing mechanisms are emerging as part of the broader autoformalization pipeline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a817c35f-d8cb-4c1b-9e82-56ec8fd06699",
  "isSidechain": false,
  "promptId": "ddf771f7-002d-42e7-9636-95691e6cb81d",
  "type": "user",
  "uuid": "4de62a22-2f80-4e16-9d6d-2aec54519a6a",
  "toolUseResult": {
    "query": "formalizability prediction learned classifier autoformalization routing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019RPVsi8BK6hZbUXzJLyVWf",
        "content": [
          {
            "title": "[2508.18914] FormaRL: Enhancing Autoformalization with no Labeled Data",
            "url": "https://arxiv.org/abs/2508.18914"
          },
          {
            "title": "Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach | OpenReview",
            "url": "https://openreview.net/forum?id=hUb2At2DsQ"
          },
          {
            "title": "StepFun-Formalizer: Unlocking the Autoformalization Potential",
            "url": "https://arxiv.org/pdf/2508.04440"
          },
          {
            "title": "A Promising Path Towards Autoformalization and General Artificial Intelligence | Intelligent Computer Mathematics",
            "url": "https://dl.acm.org/doi/abs/10.1007/978-3-030-53518-6_1"
          },
          {
            "title": "130k Lines of Formal Topology in Two Weeks: Simple and Cheap Autoformalization for Everyone?",
            "url": "https://arxiv.org/pdf/2601.03298"
          },
          {
            "title": "A Promising Path Towards Autoformalization and General Artificial Intelligence",
            "url": "https://research.google/pubs/a-promising-path-towards-autoformalization-and-general-artificial-intelligence/"
          },
          {
            "title": "LTRAG: Enhancing Autoformalization and Self-refinement ...",
            "url": "https://aclanthology.org/2025.findings-acl.126.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found regarding formalizability prediction, learned classifiers, autoformalization routing in 2025-2026:\n\n## Recent Autoformalization Research (2025-2026)\n\nThe search reveals several active projects in autoformalization, though specific work on \"formalizability prediction\" as a routing mechanism isn't explicitly detailed. However, there are related advances:\n\n**Key Projects:**\n\nFormaRL is a reinforcement learning framework for autoformalization that integrates syntax checking from Lean compiler and consistency checking from large language models to calculate rewards, showing progress in improving autoformalization success rates.\n\nRAutoformalizer augments statement autoformalization by Dependency Retrieval, retrieving potentially dependent objects from formal libraries, which represents a routing approach to improve autoformalization.\n\nNeuro-symbolic methods like Logic-LM and LINC integrate formalization with LLMs and symbolic solvers, and possibly refinement with LLMs, addressing autoformalization challenges.\n\n**Recent Scale-Up:**\n\nA project running since November 21, 2025 has produced 160k lines of formalized topology, with about 130k lines completed in two weeks from December 22 to January 4, 2026 for about $100 in LLM subscription cost.\n\nThe research appears focused on improving autoformalization accuracy and efficiency rather than explicitly routing based on formalizability prediction, though retrieval-based and learned routing mechanisms are emerging as part of the broader autoformalization pipeline."
    ],
    "durationSeconds": 7.275681050999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a817c35f-d8cb-4c1b-9e82-56ec8fd06699",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-29T06:09:49.429Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now summarize what I've verified:

1. **ThinkPRM** ✅ Confirmed as strong PRM baseline, ProcessBench SOTA-level, published April 2025.补救 agent's suggestion to add it is validated.

2. **R-PRM** ✅ Confirmed EMNLP 2025, ProcessBench +13.9 F1, PRMBench +8.5 F1.补救 agent's suggestion validated.

3. **VERGE routing is rule-based** ✅ Confirmed as semantic routing based on claim type classification, not learned. 

4. **LogicReward fallback** ✅ Confirmed - when Isabelle can't parse, falls back to token probability. This IS a "try-formal-first, fallback" approach. 发掘 agent's point about the trivial alternative is validated - LogicReward does essentially do "try formal first, fallback to neural."

5. **Formalizability prediction as a routing mechanism** - No existing work found that does learned formalizability prediction for routing. This confirms the novelty angle.

The 发掘 agent's differentiation point between static type routing and dynamic derivability routing holds up, and their insight about formalizability prediction as a learned routing mechanism appears genuinely novel—no prior work uses this approach. All 5 points are well-grounded and validated:
- Point 1 (formal guarantee on formalizable subset): Strong theoretical strengthening. Validated by the logical argument + FoVer/RRM gap.
- Point 2 (VERGE static vs. this dynamic routing): Confirmed by VERGE paper search. Strong novelty sharpening.
- Point 3 (calibrated confidence hierarchy): Reasonable extension, somewhat speculative but adds significance.
- Point 4 (asymmetric cost structure): Practical and theoretically sound. Pre-empts reviewer concern.
- Point 5 (trivial alternative - try formal first): Confirmed by LogicReward's actual mechanism. Critical to address.

Now checking the defect assessment—all 8 issues are legitimate and well-researched, from mandatory baselines like ThinkPRM and R-PRM through essential ablations, compute fairness comparisons, and practical concerns around RRM data and domain shift. The metrics and compute estimation points are also valid. I'm adopting all 5 novelty points since they're theoretically grounded and empirically verified, starting with the semi-formal guarantee framing and the static versus dynamic routing differentiation against VERGE, then moving forward with the calibrated confidence hierarchy. restraint (good framing but don't oversell)
4. Asymmetric cost structure → Adopt (pre-empts reviewer concern)
5. Trivial alternative address → Adopt (critical, verified against LogicReward)

**补救 agent - adopt all 8:**
1. Baseline matrix → Adopt (all verified as current)
2. Best-of-N evaluation → Adopt (standard requirement)
3. Ablation matrix → Adopt (essential)
4. Compute-normalized comparison → Adopt
5. RRM data handling → Adopt (practical guidance)
6. Domain shift discussion → Adopt (important)
7. Metrics specification → Adopt
8. Compute estimation → Adopt (minor but builds credibility)

### Probability assessment:

**Idea quality (from 发掘):**
- Novelty: The learned formalizability router is genuinely novel—nothing in existing work does context-dependent routing like this, and the semi-formal guarantee angle really sets it apart. Strong novelty.
- Significance: Miracle step detection with partial formal guarantees and calibrated confidence hierarchy has real practical impact on PRM quality. Solid significance.
- Related work positioning: Clear differentiation from FoVer, GenPRM, VERGE, LogicReward, and RRM.

Idea ceiling sits around 45-50%. After incorporating all the fixes, technical soundness improves from the current 25-35% gap up to a solid middle ground, though the proposal as it stands still has those experiment gaps to address.

The core idea is strong and fills a genuine gap. Once the experimental design is fixed, it becomes comprehensive. The real risks are whether autoformalization's 43% faithfulness becomes a bottleneck, whether the router actually performs well in practice, and whether the improvement over strong baselines like R-PRM and ThinkPRM is substantial enough. The semi-formal guarantee framing is compelling, but the empirical results remain unknown.

After these improvements, I'm looking at a lower bound of 32% if results disappoint or the autoformalization bottleneck proves severe, an upper bound of 48% if miracle step detection clearly outperforms with practical efficiency gains, and a median estimate of 40%.

The path forward is clear: iterate and incorporate these fixes.

Both worker analyses were comprehensive—one surfaced five strong conceptual points, the other identified eight concrete experimental gaps, all of which are addressable. After integrating everything, there's likely still room for refinement in another round, but we're probably approaching convergence given the quality of feedback. I'll now revise the proposal by weaving in all five conceptual improvements and all eight experimental fixes while preserving the original references and structure. Now I'm compiling the complete reference list, making sure to integrate the new citations alongside the existing ones while maintaining the proposal's conciseness and clarity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4de62a22-2f80-4e16-9d6d-2aec54519a6a",
  "isSidechain": false,
  "requestId": "req_011CbWMuiTjykukqkUfFqXWY",
  "type": "assistant",
  "uuid": "deac9747-e4bc-43c0-beb2-c8c9ac389297",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBu19iheSG2rAgQ8Gw7NSe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 31889,
      "output_tokens": 1957,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1957,
          "cache_read_input_tokens": 31889,
          "cache_creation_input_tokens": 2535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2535
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

_source line 36 · 2026-05-29T06:09:49.436Z_

Now let me verify one more critical point - whether "learned formalizability prediction for routing" has been done by anyone else:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "deac9747-e4bc-43c0-beb2-c8c9ac389297",
  "isSidechain": false,
  "requestId": "req_011CbWMuiTjykukqkUfFqXWY",
  "type": "assistant",
  "uuid": "2a43ed55-62b4-4967-8bb1-24d4c5721716",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBu19iheSG2rAgQ8Gw7NSe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 31889,
      "output_tokens": 1957,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1957,
          "cache_read_input_tokens": 31889,
          "cache_creation_input_tokens": 2535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2535
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

_source line 37 · 2026-05-29T06:09:50.135Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RJQExhS63fTAHGyH6CNKtq`</summary>

```json
{
  "query": "\"formalizability classifier\" OR \"formalizability prediction\" OR \"learned routing formal neural verification\" process reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a43ed55-62b4-4967-8bb1-24d4c5721716",
  "isSidechain": false,
  "requestId": "req_011CbWMuiTjykukqkUfFqXWY",
  "type": "assistant",
  "uuid": "d8fe0530-83be-4ca4-ae95-0c7ca88966fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VBu19iheSG2rAgQ8Gw7NSe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2535,
      "cache_read_input_tokens": 31889,
      "output_tokens": 1957,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2535,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1957,
          "cache_read_input_tokens": 31889,
          "cache_creation_input_tokens": 2535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2535
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

_source line 38 · 2026-05-29T06:09:56.103Z_

<details><summary>↩ Tool result · `toolu_01RJQExhS63fTAHGyH6CNKtq`</summary>

```text
Web search results for query: ""formalizability classifier" OR "formalizability prediction" OR "learned routing formal neural verification" process reward model 2025 2026"

Links: [{"title":"Generalizable Process Reward Models via Formally Verified Training Data","url":"https://arxiv.org/pdf/2505.15960"},{"title":"Training Verification-Friendly Neural Networks via Neuron Behavior   Consistency","url":"https://arxiv.org/pdf/2412.13229"},{"title":"Out of the Shadows: Exploring a Latent Space for Neural Network Verification","url":"https://arxiv.org/pdf/2505.17854"},{"title":"Provable Fairness for Neural Network Models using Formal Verification","url":"https://arxiv.org/pdf/2212.08578"},{"title":"A Deep Reinforcement Learning Framework with Formal Verification | Formal Aspects of Computing","url":"https://dl.acm.org/doi/10.1145/3577204"},{"title":"Incremental Neural Network Verification via Learned Conflicts","url":"https://arxiv.org/pdf/2603.12232"},{"title":"Formal verification result prediction","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10366330"},{"title":"Formal Verification of Piece-Wise Linear Feed-Forward Neural Networks","url":"https://arxiv.org/pdf/1705.01320"}]

Based on the search results, here's what I found:

The most relevant result is FOVER, a novel approach to create process reward model (PRM) training data using formal verification tools, such as Z3 and Isabelle. This appears in a 2025 paper titled "Generalizable Process Reward Models via Formally Verified Training Data."

The work advances the state-of-the-art of PRMs in two directions: (1) automatic, accurate creation of training data for PRMs, and (2) generalization of PRMs to diverse reasoning tasks.

Key context: Prior work on process reward models has employed costly human annotation or noisy step-level error labels to create training data, and PRMs have often been studied only on mathematical reasoning.

The search results also include other related papers on formal verification of neural networks from 2025-2026, but they focus on different aspects like robustness verification and fairness properties rather than the specific "formalizability classifier" or "learned routing" concepts mentioned in your query. The FOVER paper appears to be the most directly relevant to your search terms regarding process reward models combined with formal verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d8fe0530-83be-4ca4-ae95-0c7ca88966fc",
  "isSidechain": false,
  "promptId": "ddf771f7-002d-42e7-9636-95691e6cb81d",
  "type": "user",
  "uuid": "8fe7ab98-5116-43d1-bc77-49b9ee3fea7c",
  "toolUseResult": {
    "query": "\"formalizability classifier\" OR \"formalizability prediction\" OR \"learned routing formal neural verification\" process reward model 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TJBAhU3w1ZqHrA961jke84",
        "content": [
          {
            "title": "Generalizable Process Reward Models via Formally Verified Training Data",
            "url": "https://arxiv.org/pdf/2505.15960"
          },
          {
            "title": "Training Verification-Friendly Neural Networks via Neuron Behavior   Consistency",
            "url": "https://arxiv.org/pdf/2412.13229"
          },
          {
            "title": "Out of the Shadows: Exploring a Latent Space for Neural Network Verification",
            "url": "https://arxiv.org/pdf/2505.17854"
          },
          {
            "title": "Provable Fairness for Neural Network Models using Formal Verification",
            "url": "https://arxiv.org/pdf/2212.08578"
          },
          {
            "title": "A Deep Reinforcement Learning Framework with Formal Verification | Formal Aspects of Computing",
            "url": "https://dl.acm.org/doi/10.1145/3577204"
          },
          {
            "title": "Incremental Neural Network Verification via Learned Conflicts",
            "url": "https://arxiv.org/pdf/2603.12232"
          },
          {
            "title": "Formal verification result prediction",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10366330"
          },
          {
            "title": "Formal Verification of Piece-Wise Linear Feed-Forward Neural Networks",
            "url": "https://arxiv.org/pdf/1705.01320"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nThe most relevant result is FOVER, a novel approach to create process reward model (PRM) training data using formal verification tools, such as Z3 and Isabelle. This appears in a 2025 paper titled \"Generalizable Process Reward Models via Formally Verified Training Data.\"\n\nThe work advances the state-of-the-art of PRMs in two directions: (1) automatic, accurate creation of training data for PRMs, and (2) generalization of PRMs to diverse reasoning tasks.\n\nKey context: Prior work on process reward models has employed costly human annotation or noisy step-level error labels to create training data, and PRMs have often been studied only on mathematical reasoning.\n\nThe search results also include other related papers on formal verification of neural networks from 2025-2026, but they focus on different aspects like robustness verification and fairness properties rather than the specific \"formalizability classifier\" or \"learned routing\" concepts mentioned in your query. The FOVER paper appears to be the most directly relevant to your search terms regarding process reward models combined with formal verification."
    ],
    "durationSeconds": 5.961673186,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d8fe0530-83be-4ca4-ae95-0c7ca88966fc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39 · 2026-05-29T06:09:56.109Z_

```json
{
  "parentUuid": "8fe7ab98-5116-43d1-bc77-49b9ee3fea7c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8b4fd1f7-3f97-4f09-944a-ddfcb0c98bf2",
  "timestamp": "2026-05-29T06:09:56.109Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient background to provide my analysis. Let me synthesize my findings.  ---  【状态】: 有发掘空间…",
  "leafUuid": "8b4fd1f7-3f97-4f09-944a-ddfcb0c98bf2",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Assistant

_source line 42 · 2026-05-29T06:10:19.367Z_

<details><summary>Logged reasoning block</summary>

```text
The search confirms that no existing work does "learned formalizability prediction for routing" in the PRM context. The novelty is confirmed.

Now I have all the information I need. Let me compile my analysis and produce the output.

Let me also think about the references checklist before writing the clean proposal:

**Original references to preserve:**
1. FoVer: PRM Data Synthesis via Formal Verification (ACL 2026) - arXiv:2505.15960
2. GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026) - arXiv:2504.00891


3. LogicReward: Step-Wise Logical Supervision (ICLR 2026) - arXiv:2512.18196
4. VERGE: Formal Refinement and Guidance Engine (arXiv 2026) - arXiv:2601.20055
5. Curing Miracle Steps with Rubric Rewards (arXiv 2025) - arXiv:2510.07774
6. Risk-Controlled Lean-as-Judge (arXiv 2026)
7. ARES (2025) - autoregressive neural entailment, 72.1% Macro-F1 on PR

I'm also noting several benchmarks and models in this space like PRMBench and ProcessBench, along with tools like Z3 and Isabelle for formal verification. There are a couple of other papers that came up in related research—PRoSFI and a work on faithful autoformalization through roundtrip verification. I should add ThinkPRM and R-PRM as well, which focus on process reward models with reasoning capabilities.

Now I need to think through how to integrate the feedback from both agents. The calibrated confidence hierarchy idea from the 发掘 agent is solid but I should present it carefully—the router's formalizability score works as a confidence signal, though it's not a complete uncertainty quantification. The asymmetric cost framing is a good defensive point to include. For the ablation study, the 7-point matrix is thorough, so I'll keep most of it without oversimplifying. And I should remember to reference the PRMBench error type breakdown as a practical supplement when working with RRM data.

Before finalizing, let me lock in the key metrics I'm preserving: FoVer's 85.8 AUROC on ProcessBench, GenPRM's 7B model outperforming the 72B Qwen baseline, ARES at 72.1% Macro-F1, VERGE's 18.7% routing uplift, Risk-Controlled's 43% faithfulness with 28-79% coverage range, R-PRM's +13.9 and +8.5 F1 improvements, and ThinkPRM's efficiency with just 8K labels. Now I'll structure the complete response.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b4fd1f7-3f97-4f09-944a-ddfcb0c98bf2",
  "isSidechain": false,
  "requestId": "req_011CbWMyr9xjD9zZddaC1cLp",
  "type": "assistant",
  "uuid": "a22c45c2-65de-4816-9239-46b41055d3da",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Azj4y1eK9ecvUFAvEuurW3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 34424,
      "output_tokens": 6889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6889,
          "cache_read_input_tokens": 34424,
          "cache_creation_input_tokens": 2679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2679
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

_source line 43 · 2026-05-29T06:12:30.018Z_

Good — all cross-validation searches are complete. Now I have solid evidence to assess each worker suggestion. Let me compile the full integration.

【阶段】: 迭代第 1 轮

【交叉验证调研】:
1. **ThinkPRM 是否为必需 baseline**（补救 defect 1）→ 已验证 ✅。arXiv:2504.16828，ProcessBench 上仅用 8K labels 显著超越 100x 数据量的 discriminative PRMs，是 generative PRM 的代表性工作，必须作为 baseline。
2. **R-PRM 是否为 EMNLP 2025 发表且 SOTA**（补救 defect 1）→ 已验证 ✅。ACL Anthology 确认 EMNLP 2025 main，ProcessBench +13.9 F1，PRMBench +8.5 F1，是当前最强 discriminative PRM baseline 之一。
3. **VERGE routing 是否为 rule-based**（发掘 point 2）→ 已验证 ✅。搜索确认 VERGE 使用基于 claim type 的 semantic routing（logical vs. commonsense），是 rule-based 分类，非 learned。发掘 agent 关于 "static type routing vs. dynamic derivability routing" 的差异化论述成立。
4. **LogicReward 是否为 "try-formal-first + fallback"**（发掘 point 5）→ 已验证 ✅。ICLR 2026 论文确认：Isabelle 验证失败时 fallback 到 token probability。这就是发掘 agent 所指的 trivial alternative baseline，proposal 必须明确区分。
5. **"Learned formalizability prediction for routing" 是否已有人做**（novelty 验证）→ 搜索未发现任何现有工作 ✅。FoVer 用 formal verification 做标签但不做 routing；无人做 learned formalizability classifier。novelty 确认成立。

【发掘 agent 有效建议采纳】:
- **Point 1（semi-formal guarantee framing）**: 已验证，采纳。Z3 derivability failure ≡ miracle step detection 在 formalizable subset 上是 definitional 对应关系，提升核心 claim 从 empirical 到 semi-formal guarantee。这是最有价值的理论强化。
- **Point 2（static vs dynamic routing 差异化）**: 已验证（VERGE 确实是 rule-based claim-type routing），采纳。明确区分 VERGE 的 context-free type routing 和本 proposal 的 context-dependent derivability routing。
- **Point 3（calibrated confidence hierarchy）**: 部分采纳。作为 significance framing 的辅助论述纳入，但不作为独立 contribution 声称（尚无实验验证其实际校准质量）。标注：合理推断，无直接文献支撑具体 claim，降权处理。
- **Point 4（asymmetric cost structure）**: 采纳。预防性回答 reviewer "router 出错怎么办"的质疑，将其转化为 design principle（favor recall → 宁可多送 Z3）。有 Risk-Controlled 43% faithfulness 和 FoVer overly-strict behavior 作为调研依据。
- **Point 5（trivial alternative — try formal first）**: 已验证（LogicReward 正是此策略），采纳。必须在 proposal 中明确阐述 learned router 相对于 try-and-fallback 的三重增量价值：efficiency、uncertainty signal、intrinsic formalizability vs. extrinsic capability 区分。

【补救 agent 有效建议采纳】:
- **Defect 1（baseline 不足）**: 已验证，采纳。新增 ThinkPRM（arXiv:2504.16828）、R-PRM（EMNLP 2025, arXiv:2503.21295）到 baseline 矩阵。完整 baseline 矩阵构建。
- **Defect 2（缺失 Best-of-N）**: 采纳。PRM 领域 2025-2026 标配评估，GenPRM/FoVer/ThinkPRM/R-PRM 全部包含。加入 MATH-500 + AIME24 的 Best-of-N reranking。
- **Defect 3（无 ablation）**: 采纳。核心 ablation 保留 5 项（formal-only, neural-only, random routing, oracle routing, router threshold sweep），合并部分冗余项以保持精炼。
- **Defect 4（compute 公平性）**: 采纳。ThinkPRM 已明确做同 token budget 对比。加入 compute-normalized comparison + Pareto 曲线。
- **Defect 5（RRM 数据可用性）**: 采纳。双轨策略：使用 RRM 公开数据 + PRMBench error type breakdown 作为互补。
- **Defect 6（domain shift）**: 采纳。加入 in-domain vs. out-of-domain router 准确率报告 + few-shot adaptation ablation。引入 Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031) 方法论。
- **Defect 7（评估指标）**: 采纳。明确指标体系：ProcessBench F1+AUROC，PRMBench PRMScore + error type breakdown，Best-of-N Pass@K，miracle-specific precision/recall/F1。
- **Defect 8（compute 估算）**: 采纳。加入 compute breakdown 表增加可信度。

【本轮 proposal 主要变更】:

**Idea 层面变更:**
- 核心 claim 从 "hybrid system catches miracle steps" 提升为 "在 formalizable subset 上提供 sound miracle step detection guarantee + 在全集上提供 calibrated verification"
- 新增与 VERGE 的 crisp 差异化：static type routing (context-free) vs. dynamic derivability routing (context-dependent)
- 新增与 LogicReward 的 crisp 差异化：try-and-fallback (no routing) vs. learned routing (efficiency + uncertainty signal + intrinsic formalizability)
- 新增 asymmetric cost-aware routing 作为 design principle
- Contribution list 重构为三支柱：(1) semi-formal guarantee on formalizable subset, (2) learned context-dependent formalizability routing, (3) asymmetric cost-aware threshold design

**实验层面变更:**
- Baseline 矩阵扩展：新增 ThinkPRM, R-PRM, compute-matched GenPRM majority voting
- 新增 Best-of-N downstream reranking 评估（MATH-500, AIME24）
- 新增 5 项核心 ablation study
- 新增 compute-normalized comparison + Pareto 曲线
- 明确评估指标体系
- 新增 router domain shift 分析
- 新增 compute breakdown 估算

【idea 质量评估】: Novelty=强（learned context-dependent formalizability routing 无人做过，已搜索确认；semi-formal guarantee framing 提供理论深度；与 VERGE/LogicReward 有 crisp 差异化） Significance=中-强（miracle step detection 是实际痛点；但 practical impact 受限于 autoformalization coverage ~28-79%） → idea 天花板约 50%

【实验完备性评估】: Technical Soundness=中（本轮大幅补全了 baseline、ablation、downstream evaluation、compute fairness、metrics；但 domain shift 和 autoformalization bottleneck 仍需实验验证） → 地板从原始的 ~20% 补到 ~33%

【当前概率估计】: [33% - 48%] 中位 40%

【决策】: 继续

【决策理由】: 第 1 轮改动幅度大（idea framing 重构 + 实验设计从几乎空白到基本完整），两个 worker 都给出了高质量的实质性建议且全部已验证采纳。但 proposal 在以下方面仍可能有优化空间：(1) 发掘 agent 可能在修订版中发现新的 positioning angle（如 test-time compute scaling 与 routing 的交叉）；(2) 补救 agent 可能在修订版的实验设计中发现更细粒度的漏洞。值得再做一轮精炼。但预期第 2 轮变化幅度将显著缩小，可能接近收敛。

**引用核对清单（重写前逐条确认）：**
1. FoVer (ACL 2026) — arXiv:2505.15960 ✅
2. GenPRM (AAAI 2026) — arXiv:2504.00891 ✅
3. LogicReward (ICLR 2026) — arXiv:2512.18196 ✅
4. VERGE (arXiv 2026) — arXiv:2601.20055 ✅
5. RRM / Curing Miracle Steps (arXiv 2025) — arXiv:2510.07774 ✅
6. Risk-Controlled Lean-as-Judge (arXiv 2026) ✅
7. ARES (2025) — 72.1% Macro-F1 on PRMBench ✅
8. PRMBench (ACL 2025) — arXiv:2501.03124 ✅
9. ProcessBench ✅
10. Qwen3-8B, GenPRM-7B, Qwen2.5-Math-PRM-72B ✅
11. Z3, Isabelle ✅
12. PRoSFI (arXiv:2603.29500) ✅
13. Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031) — 新增 ✅
14. ThinkPRM (arXiv:2504.16828) — 新增 ✅
15. R-PRM (EMNLP 2025, arXiv:2503.21295) — 新增 ✅

全部 15 条已确认包含于下方纯净版。

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
# Formally-Routed Process Reward Models for Sound Miracle Step Detection

## Core Problem

No existing PRM exploits the formalizability structure of reasoning steps. Systems are either formal-only (FoVer, PRoSFI) or neural-only (GenPRM, ARES), and hybrid systems use either hand-crafted routing (VERGE) or unlearned fallback (LogicReward). The per-step routing decision between formal derivability checking and neural verification—based on a learned, context-dependent formalizability prediction—remains entirely unaddressed. Can a learned formalizability router that dispatches each step to the appropriate verifier provide sound miracle step detection on formalizable steps while maintaining strong coverage on non-formalizable steps?

## Research Opportunity

Three converging gaps create a unique opening:

(1) VERGE (arXiv:2601.20055) demonstrates 18.7% uplift from routing between Z3 and neural verifiers but uses rule-based routing over static claim types (logical vs. commonsense)—context-free and not learned. The field guide explicitly notes learned routing as the open next step.

(2) LogicReward (ICLR 2026, arXiv:2512.18196) uses Isabelle step verification with token-probability fallback, implementing a "try-formal-first" strategy. However, this lacks a trained router, a trained neural verifier branch, and any formalizability prediction—it cannot distinguish "step is not formalizable" from "autoformalization failed on a formalizable step."

(3) RRM's neural rubric approach to miracle steps (arXiv:2510.07774) was withdrawn from ICLR 2026, leaving formal derivability from predecessors completely untried for miracle step detection. FoVer's public codebase (arXiv:2505.15960), GenPRM's open models (arXiv:2504.00891), and Risk-Controlled Lean-as-Judge's honest quantification of autoformalization limits (43% faithfulness, 28–79% coverage, arXiv 2026) provide both infrastructure and calibration data for a hybrid system at academic compute budgets.

## Key Insight: Formal Derivability as Sound Miracle Detection

A miracle step is an unjustified logical leap—step S_i that does not follow from predecessors {S_1,...,S_{i-1}}. When a step is successfully formalized and submitted to Z3 for predecessor-derivability checking, a miracle step produces Z3 UNSAT (not derivable). This is not merely empirical correlation—it is a near-definitional correspondence: on the formalizable subset, miracle step detection reduces to Z3 derivability failure, providing a soundness guarantee that no neural PRM can offer. The challenge is that not all steps are formalizable. FormalRoute-PRM addresses this via a learned formalizability router that identifies which steps can receive this formal guarantee and which require neural verification.

## Contributions

1. **Sound miracle detection on formalizable subset.** On steps the router identifies as formalizable, Z3 predecessor-derivability checking provides guaranteed miracle step detection—the first PRM offering formal soundness guarantees for a subset of reasoning steps.

2. **Learned context-dependent formalizability routing.** Unlike VERGE's static claim-type routing (context-free) and LogicReward's unlearned try-and-fallback, our Qwen3-8B router predicts formalizability conditioned on the full predecessor chain {S_1,...,S_{i-1}}, a fundamentally harder and more informative classification problem. Versus try-and-fallback, learned routing provides three advantages: (a) avoids wasting autoformalization compute on steps predicted to fail, (b) produces per-step verification confidence signals (formal guarantee vs. neural best-effort), and (c) distinguishes intrinsic step formalizability from extrinsic autoformalization capability.

3. **Asymmetric cost-aware routing design.** Router errors have asymmetric costs: routing a non-formalizable step to Z3 produces false alarms (overly strict—as documented in FoVer's behavior); routing a formalizable step to neural verification risks missing a miracle step. We design the router threshold to favor recall (prefer sending to Z3), with a threshold sweep analyzing this trade-off. This principled cost asymmetry is a design contribution informed by FoVer's documented overly-strict behavior and Risk-Controlled Lean-as-Judge's 43% faithfulness quantification.

## Research Landscape

**Formal-only PRMs.** FoVer (ACL 2026, arXiv:2505.15960) achieves 85.8 AUROC on ProcessBench by training 7B PRMs on Z3/Isabelle-verified labels, but trains exclusively on formally verifiable data, producing documented overly-strict behavior on informal reasoning. PRoSFI (arXiv:2603.29500) generates structured formal intermediaries for prover verification but operates on the generation side, not verification-side routing.

**Neural PRMs.** GenPRM (AAAI 2026, arXiv:2504.00891) achieves neural SOTA with 7B surpassing Qwen2.5-Math-PRM-72B on ProcessBench via generative CoT and code verification. ThinkPRM (arXiv:2504.16828) demonstrates remarkable data efficiency—14B trained on 8K process labels outperforms discriminative PRMs trained on 100× more data, and scales verification compute effectively under fixed token budgets. R-PRM (EMNLP 2025, arXiv:2503.21295) achieves +13.9 F1 on ProcessBench and +8.5 F1 on PRMBench through three-stage supervised cold-start, DPO self-evolving, and inference-time scaling. ARES (2025) reaches 72.1% Macro-F1 on PRMBench via autoregressive entailment, entirely dependent on LLM judgment calibration.

**Hybrid systems.** VERGE (arXiv:2601.20055) routes claims to Z3 or LLM ensemble via rule-based semantic type classification (logical vs. commonsense), achieving 18.7% uplift—but routing is static, context-free, and not learned. LogicReward (ICLR 2026, arXiv:2512.18196) uses Isabelle step verification with token-probability fallback—a try-and-fail strategy that cannot distinguish intrinsic non-formalizability from autoformalization failure.

**Miracle step detection.** RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, but uses neural rubric scoring without formal derivability checking. No existing system has tested formal derivability from predecessors as a miracle step detection mechanism.

**Autoformalization limits.** Risk-Controlled Lean-as-Judge (arXiv 2026) provides honest quantification: 43% faithfulness, 28–79% coverage. Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031) provides roundtrip verification methodology for improving faithfulness. These calibration data inform our honest coverage reporting and router training signal design.

## Proposed Approach

**Router.** Train Qwen3-8B formalizability classifier on FoVer Z3 verification labels + autoformalization success signals (defined as Z3 compilation success AND roundtrip semantic verification, following arXiv:2604.25031). Router takes as input step S_i and predecessor context {S_1,...,S_{i-1}}, outputs formalizability probability. Threshold set via asymmetric cost-aware optimization favoring recall.

**Formal branch.** Formalizable steps undergo autoformalization → Z3 predecessor-derivability checking. Z3 UNSAT → miracle step detected (sound on successful formalization). Z3 SAT → step verified with formal guarantee.

**Neural branch.** Non-formalizable steps receive GenPRM-7B scoring with ARES-style calibrated entailment. This branch provides best-effort verification without formal guarantees.

**Integration.** Final per-step score combines branch outputs with router confidence, producing a calibrated verification signal: formally verified steps carry higher confidence than neurally scored steps.

## Evaluation Design

**Benchmarks and metrics.**
- ProcessBench: F1 (aligned with GenPRM, R-PRM) + AUROC (aligned with FoVer)
- PRMBench (ACL 2025, arXiv:2501.03124): PRMScore + error-type breakdown
- Best-of-N reranking: MATH-500, AIME24 using Qwen2.5-Math-7B-Instruct as generator; report Pass@1, majority voting, PRM reranking (N=8,16,64)
- Miracle step detection: precision/recall/F1 on RRM miracle taxonomy annotations (Yuan et al., 2025) + PRMBench relevant error categories

**Baseline matrix.**
- Pure neural: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B
- Pure formal: FoVer-7B
- Hybrid: VERGE (hand-crafted routing), LogicReward (Isabelle + fallback)
- LLM-as-Judge: GPT-4o, QwQ-32B
- Compute-matched: GenPRM majority voting under equivalent token budget

**Ablation studies.**
1. Formal-only: all steps → Z3 (demonstrates low coverage penalty)
2. Neural-only: all steps → GenPRM (demonstrates miracle step leakage)
3. Random routing: 50/50 formal/neural (isolates routing contribution from ensemble effect)
4. Oracle routing: ground-truth formalizability labels (performance ceiling, quantifies router quality gap)
5. Router threshold sweep: coverage-accuracy trade-off curve across formalizability thresholds, visualizing asymmetric cost impact

**Compute fairness.** Report per-step average inference time and FLOPs for FormalRoute-PRM and all baselines. Plot accuracy vs. compute Pareto curve. Include compute-matched GenPRM majority voting as explicit comparison.

**Router analysis.** Report router classification accuracy, precision, recall on in-domain (formal reasoning) and out-of-domain (general math) splits. Include few-shot domain adaptation ablation with ProcessBench/PRMBench samples. Use oracle formalizability labels (human-annotated, 100–200 examples) to quantify router quality ceiling. Report formalizability positive rate and formal branch coverage statistics.

**Honest coverage reporting.** Following Risk-Controlled Lean-as-Judge methodology, report autoformalization coverage, faithfulness rate, and formal branch activation rate per benchmark. Acknowledge and quantify the gap between theoretical soundness and practical coverage.

## Compute Budget

- Router training: Qwen3-8B LoRA fine-tuning on ~80K FoVer-derived labels, ≈4–8 GPU-hours on single H100
- Z3 solving: millisecond-scale per formula, negligible
- GenPRM-7B inference: standard 7B inference on single H100
- Autoformalization: LLM calls for formalizable steps (estimated 30–50% of total steps)
- Total: training <1 day, full evaluation pipeline <3 days on single-node H100

## Key References

- FoVer: PRM Data Synthesis via Formal Verification (ACL 2026, arXiv:2505.15960)
- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026, arXiv:2504.00891)
- LogicReward: Step-Wise Logical Supervision (ICLR 2026, arXiv:2512.18196)
- VERGE: Formal Refinement and Guidance Engine (arXiv 2026, arXiv:2601.20055)
- Curing Miracle Steps with Rubric Rewards (arXiv 2025, arXiv:2510.07774)
- Risk-Controlled Lean-as-Judge (arXiv 2026)
- ARES: Autoregressive Entailment Scoring (2025)
- ThinkPRM: Process Reward Models That Think (arXiv:2504.16828)
- R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, arXiv:2503.21295)
- PRMBench: Fine-grained PRM Benchmark (ACL 2025, arXiv:2501.03124)
- PRoSFI: Structured Formal Intermediaries (arXiv:2603.29500)
- Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031)
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a22c45c2-65de-4816-9239-46b41055d3da",
  "isSidechain": false,
  "requestId": "req_011CbWMyr9xjD9zZddaC1cLp",
  "type": "assistant",
  "uuid": "a299d4b1-17f8-48b5-981e-9589ab1d8d5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Azj4y1eK9ecvUFAvEuurW3",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2679,
      "cache_read_input_tokens": 34424,
      "output_tokens": 6889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6889,
          "cache_read_input_tokens": 34424,
          "cache_creation_input_tokens": 2679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2679
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient background to provide my analysis. Let me synthesize my findings.  ---  【状态】: 有发掘空间…",
  "leafUuid": "a299d4b1-17f8-48b5-981e-9589ab1d8d5b",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 47 · 2026-05-29T06:16:45.809Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:16:45.809Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "content": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have sufficient research to make an informed evaluation. Let me synthesize my findings.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- **FoVer** (ACL 2026, arXiv:2505.15960): 用 Z3/Isabelle 合成 PRM 训练数据，ProcessBench 上 85.8 AUROC，但只在形式化数据上训练，导致 documented 的\"过严\"行为——对非形式化推理步骤产生假阳性。本 proposal 正确识别了这个局限。\n- **VERGE** (arXiv:2601.20055): 将 claims 分为 logical 和 commonsense，rule-based 路由到 Z3 或 LLM ensemble，获得 18.7% uplift。路由是静态的、context-free 的、非学习的。论文本身明确指出 learned routing 是 open next step。\n- **LogicReward** (ICLR 2026, arXiv:2512.18196): Isabelle 步骤验证 + token-probability fallback。8B 模型在逻辑推理上超过 GPT-4o 11.6%。核心局限：try-and-fail 策略无法区分\"步骤本身不可形式化\"与\"autoformalization 能力不足\"。\n- **GenPRM** (AAAI 2026, arXiv:2504.00891): 生成式 PRM，CoT + 代码验证，仅 23K 训练数据即超越前代 PRM。7B 模型超过 Qwen2.5-Math-PRM-72B。\n- **ThinkPRM** (arXiv:2504.16828): 仅用 PRM800K 1% 的 process labels 训练，在 ProcessBench 上比 LLM-as-Judge 高 7.2%，在 GPQA-Diamond 上比判别式 PRM 高 8%。展示了 generative PRM 极强的 data efficiency 和 test-time compute scaling。\n- **RRM** (arXiv:2510.07774, withdrawn ICLR 2026): 定义 miracle step 分类学，通过 rubric rewards 减少 71% miracle steps。纯神经方法，未尝试形式化可导性检查。\n- **FIRMA** (MathNLP 2025): 双向 formal-informal 数学语言对齐，包含 complexity router 和 proof-preserving attention。在 formal-informal routing 概念上与本 proposal 有重叠，但操作层级不同（翻译质量 vs. 验证路由）。\n- **Risk-Controlled Lean-as-Judge** (arXiv 2026): 43% faithfulness, 28-79% coverage。这是本 proposal soundness claim 的关键约束条件。\n- **Faithful Autoformalization via Roundtrip Verification** (arXiv:2604.25031): 提供 roundtrip verification 方法论提升 faithfulness。\n\n- **调研总结**: 当前 PRM 领域正在经历从判别式→生成式（GenPRM, ThinkPRM）和从纯神经→hybrid formal-neural（FoVer, VERGE, LogicReward）两个平行趋势。在 hybrid 方向上，如何智能地决定何时使用 formal verification 是公认的 open problem（VERGE 明确指出），但同时 autoformalization 的可靠性问题（43% faithfulness）对 formal 方法的实际价值构成了严重约束。\n\n---\n\n【发掘点 1】\n- **维度**: trivial alternative 威胁\n- **内容**: 本 proposal 最大的 trivial alternative 是 **\"always-try-Z3 + neural fallback\"**——即不训练 router，对每个步骤直接尝试 autoformalize + Z3 验证，Z3 失败（编译失败或超时）时 fallback 到 GenPRM。这本质上是 LogicReward 的改进版（用更强的 neural branch 替换 token-probability fallback）。Proposal 目前给出的 router 价值论证有三条：(a) 节省 autoformalization 计算，(b) 产生 per-step verification confidence signal，(c) 区分 intrinsic non-formalizability 和 extrinsic autoformalization failure。但 (a) 的 compute saving 在实际中有限（autoformalization 是一次 LLM call，不是 catastrophically expensive）；(b) 和 (c) 才是真正的差异化价值，但当前 proposal 对这两点的论证不够深入。**建议**：必须在 proposal 中正面处理这个 trivial alternative，最好在 ablation 中加入 \"always-try-Z3 + neural fallback\" 作为显式 baseline（当前的 ablation 列表中没有这个），并清晰论证 learned router 在减少 formal branch false alarms（因 non-formalizable 步骤被错误送入 Z3 而产生的假阳性）方面的不可替代价值。Router 的核心价值不是\"节省计算\"，而是\"减少 formal branch 对 non-formalizable 步骤的系统性假阳性\"——这个 framing 比当前的论述更锐利、更defensible。\n- **价值**: 直接关系 novelty——如果审稿人认为 trivial alternative 能达到类似效果，整个 learned router 的贡献将被大幅削弱。正面应对 trivial alternative 是保住核心 novelty claim 的关键。\n- **调研依据**: FoVer 文档中记录的 \"overly-strict behavior\" 正是 non-formalizable 步骤被送入 formal verification 的后果；VERGE 的 rule-based routing 也正是为了避免这个问题。LogicReward 的 try-and-fail 策略实际上就是这个 trivial alternative 的一个实例。\n\n【发掘点 2】\n- **维度**: 核心 claim 强化 / 前提假设质疑\n- **内容**: Proposal 声称 \"formal soundness guarantees for a subset of reasoning steps\"，但这个 soundness guarantee 有一个关键的、当前被低估的条件依赖：**autoformalization 的 faithfulness**。根据 Risk-Controlled Lean-as-Judge 的数据，autoformalization 仅有 43% faithfulness。这意味着即使 router 正确识别了 formalizable 步骤，且 Z3 返回 SAT，如果 autoformalization 不 faithful（即形式化表达不忠实于原始自然语言步骤），这个\"verified\"结果是 vacuously correct——验证的是一个与原始步骤语义不同的形式化命题。因此，**实际的 soundness guarantee 仅在 \"router 正确 × autoformalization faithful × Z3 correct\" 的交集上成立**。按照当前数据粗略估算，如果 30-50% 的步骤被路由到 formal branch，其中 43% faithfully formalized，实际享受 soundness guarantee 的步骤可能仅占全部步骤的 13-22%。**建议**：(1) 将 soundness claim 精确限定为 \"conditional on faithful autoformalization\"，避免审稿人挑战 overclaiming；(2) 将 roundtrip verification（arXiv:2604.25031，proposal 已引用但未深度整合）作为 autoformalization 质量的 gatekeeper——只有通过 roundtrip verification 的形式化步骤才进入 Z3 验证，未通过的 fallback 到 neural branch。这实际上将 pipeline 从两层（router → formal/neural）变为三层（router → roundtrip check → formal/neural），显著增强 soundness claim 的可信度。\n- **价值**: 直接决定核心 contribution #1 的可信度。Soundness guarantee 是本 proposal 区别于所有纯神经 PRM 的最核心 selling point，但如果审稿人指出这个 guarantee 建立在 43% faithfulness 的脆弱基础上，整个 contribution 会被严重打折。精确限定 + roundtrip verification gatekeeper 可以将这个弱点转化为成熟可信的 contribution。\n- **调研依据**: Risk-Controlled Lean-as-Judge 的 43% faithfulness 数据；arXiv:2604.25031 的 roundtrip verification 方法论。\n\n【发掘点 3】\n- **维度**: significance 提升 / novelty 锐化\n- **内容**: 当前 proposal 将自己的贡献 frame 为 \"routing\"——一个二元的分发决策。但更深层地看，本 proposal 实际上在构建的是一个 **分层验证置信度体系 (verification confidence hierarchy)**：(a) 通过 roundtrip verification 的 Z3 verified 步骤 → 最高置信度（formal guarantee），(b) 未通过 roundtrip verification 但 Z3 编译成功的步骤 → 中等置信度（formal but potentially unfaithful），(c) 被 router 识别为 non-formalizable 的步骤 → neural verification 置信度，(d) router 不确定的步骤 → 最低置信度。这个 **从二元路由到连续置信度谱** 的 reframing 将贡献从 \"engineering design\"（怎么路由）提升为 \"scientific contribution\"（怎么为每个步骤的验证结果赋予有意义的校准置信度）。这种 verification confidence hierarchy 对下游 Best-of-N reranking 和 RL reward shaping 都有直接价值——不同置信度层级的验证信号应被赋予不同的 reward weight。目前 PRM 文献中没有任何工作提出这种分层置信度框架。\n- **价值**: 显著提升 significance 和 novelty。\"Learned routing\" 容易被审稿人视为 incremental engineering（VERGE 已经有 routing，你只是把 rule-based 换成 learned）。\"Calibrated verification confidence hierarchy\" 是一个更 fundamental 的框架贡献，对 PRM 领域的认知方式有推动作用——从 \"每步给一个 score\" 到 \"每步给一个 score + 该 score 的可信度来源标注\"。\n- **调研依据**: 基于领域整体趋势判断。当前所有 PRM（GenPRM, ThinkPRM, R-PRM, FoVer）都输出一个 scalar score 或 binary label，没有任何工作区分\"这个 score 是怎么得到的、有多可信\"。这是一个 genuine gap。\n\n【发掘点 4】\n- **维度**: related work 差异化\n- **内容**: Proposal 遗漏了 **FIRMA** (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5) 的讨论。FIRMA 提出了一个 \"complexity router\" 用于 formal-informal 数学语言的双向对齐，虽然它操作在翻译质量层面而非验证层面，但一个 well-informed 的审稿人可能会指出概念上的相似性：都是用一个 router 来决定 formal vs. informal 处理路径。**建议**：在 related work 中明确讨论 FIRMA，指出关键差异——FIRMA 的 complexity router 是为翻译质量服务（formal-informal alignment），本 proposal 的 formalizability router 是为验证正确性服务（derivability checking），目标函数和训练信号完全不同。这种主动的差异化定位比让审稿人自己发现这个遗漏要好得多。\n- **价值**: 保护 novelty claim 免受审稿人的\"这不是已经有人做了吗\"质疑。Related work 的完整性直接影响审稿人对 novelty 判断的信任度。\n- **调研依据**: FIRMA (ACL Anthology 2025.mathnlp-main.5)，其 complexity router 架构与本 proposal 的 formalizability router 在概念层面有表面相似性。\n\n【发掘点 5】\n- **维度**: novelty 锐化\n- **内容**: 当前 proposal 将 learned router 的 novelty 主要对标 VERGE（rule-based → learned）和 LogicReward（try-and-fail → learned prediction）。但这个差异化 framing 有一个潜在弱点：审稿人可能认为 \"把 rule-based 替换成 learned classifier 是 2015 年的想法，不构成 2026 年的 novelty\"。Proposal 需要更锐利地阐述 **为什么 formalizability 的 context-dependent 预测本身是一个 non-trivial 的学习问题**。具体来说：一个步骤是否可形式化不仅取决于步骤本身的语义内容（VERGE 的 rule-based 能处理的部分），还取决于 (1) predecessor chain 建立的 formal context（前面的步骤已经引入了哪些形式化定义和变量），(2) autoformalization 工具的当前能力边界（不同的步骤类型有不同的 formalization 成功率），(3) 步骤在证明中的位置（early steps 往往更 declarative/formalizable，later steps 可能涉及更多 heuristic reasoning）。这些 context dependencies 使得 formalizability prediction 不可还原为 static claim-type classification——必须是 learned 和 context-dependent 的。当前 proposal 提到了 \"conditioned on the full predecessor chain\" 但没有充分展开这一点的 non-triviality。\n- **价值**: 直接强化核心 novelty claim。将 \"learned router\" 从 \"obvious engineering improvement\" 提升为 \"solving a genuinely non-trivial prediction problem that rule-based approaches cannot address in principle\"。\n- **调研依据**: VERGE 的 rule-based routing 仅基于 static claim types（logical vs. commonsense），完全不考虑 predecessor context。LogicReward 的 try-and-fail 策略同样不做任何预测。这说明 context-dependent formalizability prediction 确实是一个未被解决的问题，但 proposal 需要更好地论证其 non-triviality。\n\n---\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055)\n- [LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)\n- [Process Reward Models That Think (ThinkPRM)](https://arxiv.org/abs/2504.16828)\n- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)\n- [Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards](https://arxiv.org/abs/2510.07774)\n- [FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment](https://aclanthology.org/2025.mathnlp-main.5/)\n- [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](https://arxiv.org/html/2605.28365)\n- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031)\n- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research context. Let me compile my assessment.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **GenPRM (AAAI 2026, arXiv:2504.00891)**: 实验用 ProcessBench F1 + PRMBench F1 + Best-of-N (MATH-500, AIME24, OlympiadBench, Omni-MATH)；baseline 包括 Math-Shepherd, RLHFlow, Skywork-PRM, Qwen2.5-Math-PRM-72B 等；ablation 包括 data scaling、RPE vs. ORM labels、code verification 贡献隔离。Majority voting 在 token budget 控制下作为核心对照。\n- **FoVer (ACL 2026 Findings, arXiv:2505.15960)**: 评测覆盖 12 个推理 benchmark（含 NLI、BBH 等 OOD 任务）；用 Best-of-K 评价 PRM 泛化性；ablation 拆分 formal logic data vs. formal theorem proof data 的贡献；baseline 对比 base LLM 及 human/strong-model-annotated PRMs。AUROC 为其主要指标。\n- **ThinkPRM (arXiv:2504.16828, submitted ICLR 2026)**: 强调 token-budget-normalized 对比——在相同 token 预算下 ThinkPRM 超 LLM-as-Judge 7.2%；评测 ProcessBench、MATH-500、AIME'24、GPQA-Diamond、LiveCodeBench（OOD）；ablation 拆分 process-label filtering vs. answer-only filtering。\n- **R-PRM (EMNLP 2025, arXiv:2503.21295)**: 三阶段方法（cold-start → DPO → inference scaling），评测 ProcessBench + PRMBench + 6 个数学数据集；baseline 包括 Math-Shepherd, Math-PSA, RLHFlow, Skywork-PRM, ReasonEval, Llemma-PRM800K, Qwen2.5-Math-PRM；ablation 逐阶段贡献分析。\n- **VERGE (arXiv:2601.20055)**: 核心是 Semantic Routing（rule-based），claim 分类为 logical vs. commonsense，分别送 Z3 和 LLM ensemble；用 Minimal Correction Subsets 做 error localization；报告 18.7% uplift，但未做 learned routing 对照。\n- **LogicReward (ICLR 2026, arXiv:2512.18196)**: 用 Isabelle 做 step-level verification + Autoformalization with Soft Unification；评测 8 个 logical reasoning / NLI benchmark；结果显示 8B 模型超 GPT-4o 11.6%。但其是 RL 训练框架而非独立 PRM，直接对比需注意 apples-to-oranges 问题。\n- **RRM / Miracle Steps (arXiv:2510.07774)**: 定义 miracle step taxonomy，报告 RRM 将 miracle step 发生率降低 71%（Verified Pass@1024 on AIME2024: 26.7% → 62.6%），但该论文已从 ICLR 2026 撤稿，其 annotations 的公开可用性存疑。\n- **调研总结**: 当前 PRM 领域的实验标准要求：(1) ProcessBench F1/AUROC + PRMBench PRMScore 作为核心 step-level 评测；(2) Best-of-N (N=8/16/64) 在 MATH-500/AIME24 上作为下游任务评测；(3) token-budget / compute-normalized 公平对比已成为审稿人标准要求（ThinkPRM 开创先例）；(4) ablation 需隔离各核心组件贡献；(5) OOD 泛化评测被多数高分论文包含。\n\n---\n\n【缺陷 1】\n- 类别: 可行性问题\n- 问题: Proposal 的核心 claim 之一——\"sound miracle step detection\"——其评测依赖 \"RRM miracle taxonomy annotations (Yuan et al., 2025)\"。但 RRM 论文已从 ICLR 2026 撤稿（proposal 自己也承认这一点），其 miracle step taxonomy annotations 的**公开可用性未确认**。如果这些标注数据不可获取，Miracle step detection 的 precision/recall/F1 评测将无法执行，而这正是该 proposal 三个 contribution 中第一个的直接实验支撑。\n- 严重度: 可补救\n- 补救方案: 三层保障策略——(1) **立即确认数据可用性**：检查 RRM 的 GitHub repo 或联系作者确认标注数据是否公开，撤稿不一定意味着数据不可用；(2) **自建 miracle step 标注**：在 ProcessBench 或 PRMBench 中抽取 200–300 个 step，请 2–3 名标注者按 RRM 的 miracle step 定义（\"unjustified logical leap\"）进行标注并报告 inter-annotator agreement（Cohen's kappa），这在学术 budget 内可行；(3) **利用 PRMBench 已有错误分类**：PRMBench 包含 fine-grained error type breakdown（83,456 step-level labels），其中部分错误类别（如 \"logical gap\"、\"unjustified step\"）可作为 miracle step 的 proxy 指标，proposal 中已提到这一点但应将其从 \"supplementary\" 升级为 \"primary evaluation（if RRM data unavailable）\"。\n- 调研依据: PRMBench (ACL 2025, arXiv:2501.03124) 提供 6,216 problems + 83,456 step labels 的 fine-grained 错误分类；RRM 论文确认已从 ICLR 2026 撤稿。\n\n【缺陷 2】\n- 类别: compute 公平性问题\n- 问题: Proposal 在 Compute Budget 中将 autoformalization 描述为 \"LLM calls for formalizable steps (estimated 30–50% of total steps)\"，但**未明确指定用哪个 LLM 做 autoformalization，也未将 autoformalization 的 compute 纳入 per-step 推理成本计算**。Autoformalization 通常需要强 LLM（至少 7B+，实践中常用 70B+ 或 API models），这可能是整个 pipeline 中 compute 开销最大的部分。如果 compute Pareto 曲线不包含 autoformalization 开销，与 GenPRM majority voting 等 baseline 的 compute-matched 对比将不公平——审稿人极有可能质疑这一点。\n- 严重度: 可补救\n- 补救方案: (1) **明确 autoformalization 模型**：指定使用哪个 LLM 进行 autoformalization（例如 Qwen2.5-Math-72B-Instruct 或 GPT-4o），并报告其 per-step 推理成本（tokens/step, latency, FLOPs）；(2) **将 autoformalization 开销纳入 total compute**：在 accuracy vs. compute Pareto 曲线中，FormalRoute-PRM 的 compute 必须包含 router inference + autoformalization + Z3 solving + neural branch（对分到该 branch 的 step）；(3) **增加一个 compute ablation**：对比使用不同规模 autoformalization 模型（如 7B vs. 72B）时的 accuracy-cost tradeoff，这也能展示系统对 autoformalization 质量的敏感性；(4) **考虑 autoformalization caching**：对于 evaluation benchmark 中重复出现的公式模式，是否可以 cache autoformalization 结果以降低实际推理开销。\n- 调研依据: ThinkPRM (arXiv:2504.16828) 确立了 token-budget-normalized 对比范式，在同等 token 预算下展示优势是审稿人标准期望；GenPRM 的 majority voting 在控制 compute 下作为对照也是这一范式的体现。\n\n【缺陷 3】\n- 类别: 实验设计不足\n- 问题: Router 的训练标签构建方案存在 **label noise 问题未被讨论**。Proposal 称 router 训练于 \"FoVer Z3 verification labels + autoformalization success signals\"，但这些标签将三类不同情况混为一谈：(a) step 本身不可形式化（true negative）；(b) step 可形式化但 autoformalization 失败（false negative）；(c) Z3 超时或内存溢出（indeterminate）。Proposal 提到用 roundtrip verification (arXiv:2604.25031) 来提高 faithfulness，但**未讨论如何处理 (b) 和 (c) 导致的 label noise 对 router 训练的影响**，也未给出 label quality 的估计。审稿人极可能质疑 router 的训练信号质量。\n- 严重度: 可补救\n- 补救方案: (1) **在 router analysis 中增加 label quality 评估**：从训练数据中抽样 200–300 个 \"non-formalizable\" label，人工验证其中有多少是 true non-formalizable vs. autoformalization failure，报告 label precision；(2) **在 ablation 中增加 label noise robustness 实验**：人工清洗一小批标签（如 500–1000 条）训练一个 \"clean-label router\"，对比使用 noisy label 的 router，量化 label noise 的影响；(3) **明确 label 构建 pipeline**：详述从 FoVer 数据到 router 训练标签的完整流程——哪些 step 标为 formalizable（Z3 编译成功 AND roundtrip 通过）、哪些标为 non-formalizable（autoformalization 失败 OR roundtrip 失败 OR Z3 超时），以及如何处理 ambiguous cases；(4) **讨论 coverage of formal verification 工具的局限**：引用已有的 autoformalization faithfulness 数据（约 43% faithfulness in literature），诚实估算 router 训练标签中 false negative 的比例。\n- 调研依据: FoVer (arXiv:2505.15960) 的 ablation 显示 formal logic 和 theorem proof data 的贡献不完全累加，暗示数据质量/一致性问题；autoformalization faithfulness 研究 (arXiv:2604.19459 等) 指出 syntactic correctness ≠ semantic faithfulness 是普遍问题。\n\n【缺陷 4】\n- 类别: 实验设计不足\n- 问题: Proposal 缺少 **OOD (out-of-distribution) 泛化评测**。Router 训练于 FoVer 衍生的数学/逻辑推理数据，但 proposal 的评测全部集中在数学推理 benchmark（ProcessBench, PRMBench, MATH-500, AIME24）。高水平 PRM 论文（如 FoVer 在 NLI/BBH 上评测、ThinkPRM 在 GPQA-Diamond/LiveCodeBench 上评测）均包含 OOD 评测来验证泛化性。审稿人会质疑：router 和整体系统在 **非数学推理任务**（如科学推理、代码推理、commonsense 推理）上表现如何？router 是否会在 OOD 场景下将不可形式化的 step 错误路由到 Z3？\n- 严重度: 可补救\n- 补救方案: (1) 增加 1–2 个 OOD benchmark：**GPQA-Diamond**（科学推理，ThinkPRM 用过）和 **BBH**（多样化推理任务，FoVer 用过）是最自然的选择，已有 PRM 评测先例；(2) 在 router analysis 中，单独报告 OOD 场景下的 router classification accuracy——预期 router 在 OOD 场景下会更多地将 step 路由到 neural branch（因为 OOD step 大多不可形式化），这本身是系统正确行为的体现，应显式验证并报告；(3) 如果 OOD 评测显示性能下降，这不一定是负面结果——可以解读为\"系统在 OOD 场景下 graceful degrade 到 neural-only baseline\"，只要不比 neural-only baseline 差即可。\n- 调研依据: FoVer (arXiv:2505.15960) 在 NLI、BBH 等 OOD 任务上评测泛化性是其被接受的重要因素；ThinkPRM (arXiv:2504.16828) 在 GPQA-Diamond 和 LiveCodeBench 上做 OOD 评测，超 discriminative PRM 8% / 4.5%。\n\n【缺陷 5】\n- 类别: baseline 不足或过时\n- 问题: Proposal 的 baseline matrix 中 **LogicReward 的对比存在 apples-to-oranges 风险**。LogicReward 是一个 RL 训练框架（用 Isabelle 验证生成 reward signal 来训练 LLM），而非独立的 step-level PRM。直接将其作为 \"hybrid PRM baseline\" 与 FormalRoute-PRM 在 ProcessBench/PRMBench 上对比可能不公平或不可行——LogicReward 的输出是一个训练好的 LLM，而非一个 step-level verifier score。此外，LogicReward 使用 **Isabelle** 而 FormalRoute-PRM 使用 **Z3**，formal backend 不同也增加对比的复杂性。\n- 严重度: 可补救\n- 补救方案: (1) **明确 LogicReward 的对比方式**：如果将 LogicReward 作为 baseline，需说明如何从 LogicReward 的框架中提取 step-level score（例如使用 LogicReward 训练后的 LLM 的 per-step logprob 或 rubric score）；(2) **区分两种对比维度**：LogicReward 可作为 \"hybrid formal+neural approach\" 的 conceptual comparison（方法论层面），而在 quantitative benchmark 对比中应标注其不同性质，避免审稿人认为对比不公平；(3) **考虑补充一个更直接可比的 baseline**：例如用 FoVer 的 Z3 verification + 简单 try-and-fallback（Z3 失败则用 neural PRM）作为 \"naive hybrid\" baseline，这比 LogicReward 更直接地对照 learned routing vs. try-and-fallback 的差异。这个 baseline 实际上就是 contribution 2 想要超越的直接对手，且实现成本极低。\n- 调研依据: LogicReward (ICLR 2026) 的实验设计是在 8 个 logical reasoning/NLI benchmark 上评测 RL 训练后的 LLM，而非 step-level PRM evaluation；FoVer 使用 Z3+Isabelle 双后端但也只对比 PRM 框架内的 baseline。\n\n【缺陷 6】\n- 类别: ablation 不完整\n- 问题: 当前 ablation 设计覆盖了 routing 策略的对比（formal-only / neural-only / random / oracle / threshold sweep），但**缺少对 neural branch 选择的 ablation**。Proposal 选择 GenPRM-7B + ARES-style calibrated entailment 作为 neural branch，但未验证这个选择的贡献。具体来说，缺少两个对照：(a) 将 neural branch 替换为更简单的 discriminative PRM（如 FoVer-7B 自身的 PRM score），验证 GenPRM 作为 neural branch 的必要性；(b) 将 neural branch 替换为 ThinkPRM-style long CoT verification，验证 generative vs. discriminative neural branch 的差异。此外，**ARES-style calibrated entailment 的具体集成方式未详述**——这是附加在 GenPRM 输出上的 calibration layer 还是独立模块？\n- 严重度: 可补救\n- 补救方案: (1) 增加 ablation：**FormalRoute-PRM (GenPRM neural branch) vs. FormalRoute-PRM (discriminative PRM neural branch)**，隔离 neural branch 选择的贡献；(2) 明确 ARES-style calibration 的具体实现和集成方式——是 temperature scaling、Platt scaling 还是其他方法？在 router 的 formal confidence vs. neural confidence 整合中，calibration 的实现直接影响最终 score 的质量；(3) 如果时间/compute 有限，至少在 related work 或 discussion 中讨论 neural branch 选择的设计理由并承认这是一个可探索的 axis。\n- 调研依据: GenPRM (AAAI 2026) 和 ThinkPRM (arXiv:2504.16828) 代表 generative PRM 的两种不同范式（RPE+code verification vs. long CoT），在 PRM 论文中 neural component 的选择通常需要 justify。\n\n【缺陷 7】\n- 类别: 可行性问题\n- 问题: Proposal 引用 \"Risk-Controlled Lean-as-Judge (arXiv 2026)\" 的 \"43% faithfulness, 28–79% coverage\" 数据作为多处论证的关键依据（router threshold 设计、honest coverage reporting 方法论、asymmetric cost 论证），但**未提供 arXiv ID**，我的调研也未找到这篇具体论文。如果这篇论文不存在、尚未公开、或其数据被误引，相关论证的基础将被审稿人质疑。\n- 严重度: 可补救\n- 补救方案: (1) **提供完整引用**：补全 arXiv ID 或 URL，确保论文可查证；(2) **如果论文确实存在但尚未公开**：改为引用其他已公开的 autoformalization faithfulness 数据——例如 \"Do LLMs Game Formalization?\" (arXiv:2604.19459) 和 \"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing\" (arXiv:2511.12784) 都讨论了 autoformalization 的 faithfulness 限制；(3) **自行量化 faithfulness**：在 FoVer 数据上运行 autoformalization pipeline，对 200–300 个 step 人工验证 autoformalization 的 semantic faithfulness，得到自己的 faithfulness 估计。这既加强论证的可信度，也是对 router 训练标签质量的直接验证（与缺陷 3 的补救方案互补）。\n- 调研依据: 多篇 autoformalization 评测论文 (arXiv:2604.19459, arXiv:2510.15981, arXiv:2511.12784) 均指出 faithfulness 是核心瓶颈，但具体数字因实验设置而异，需确保引用数据有可追溯来源。\n\nSources:\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)\n- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055)\n- [LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision](https://openreview.net/forum?id=A3FhAVfcJI)\n- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)\n- [Curing \"Miracle Steps\" in LLM Mathematical Reasoning with Rubric Rewards](https://arxiv.org/abs/2510.07774)\n- [PRoSFI: Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries](https://arxiv.org/abs/2603.29500)\n- [Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning](https://arxiv.org/html/2604.19459)\n- [Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing](https://arxiv.org/pdf/2511.12784)\n- [PRISM: Pushing the Frontier of Deep Think via Process Reward Model-Guided Inference](https://arxiv.org/html/2603.02479)\n- [GenPRM GitHub Repository](https://github.com/RyanLiu112/GenPRM)\n- [FoVer GitHub Repository](https://github.com/psunlpgroup/FoVer)"
}
```

---

### Runtime record

_source line 48 · 2026-05-29T06:16:45.810Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:16:45.810Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

## Round 3

24 recorded events

### User

_source line 49 · 2026-05-29T06:16:45.858Z_

【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have sufficient research to make an informed evaluation. Let me synthesize my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- **FoVer** (ACL 2026, arXiv:2505.15960): 用 Z3/Isabelle 合成 PRM 训练数据，ProcessBench 上 85.8 AUROC，但只在形式化数据上训练，导致 documented 的"过严"行为——对非形式化推理步骤产生假阳性。本 proposal 正确识别了这个局限。
- **VERGE** (arXiv:2601.20055): 将 claims 分为 logical 和 commonsense，rule-based 路由到 Z3 或 LLM ensemble，获得 18.7% uplift。路由是静态的、context-free 的、非学习的。论文本身明确指出 learned routing 是 open next step。
- **LogicReward** (ICLR 2026, arXiv:2512.18196): Isabelle 步骤验证 + token-probability fallback。8B 模型在逻辑推理上超过 GPT-4o 11.6%。核心局限：try-and-fail 策略无法区分"步骤本身不可形式化"与"autoformalization 能力不足"。
- **GenPRM** (AAAI 2026, arXiv:2504.00891): 生成式 PRM，CoT + 代码验证，仅 23K 训练数据即超越前代 PRM。7B 模型超过 Qwen2.5-Math-PRM-72B。
- **ThinkPRM** (arXiv:2504.16828): 仅用 PRM800K 1% 的 process labels 训练，在 ProcessBench 上比 LLM-as-Judge 高 7.2%，在 GPQA-Diamond 上比判别式 PRM 高 8%。展示了 generative PRM 极强的 data efficiency 和 test-time compute scaling。
- **RRM** (arXiv:2510.07774, withdrawn ICLR 2026): 定义 miracle step 分类学，通过 rubric rewards 减少 71% miracle steps。纯神经方法，未尝试形式化可导性检查。
- **FIRMA** (MathNLP 2025): 双向 formal-informal 数学语言对齐，包含 complexity router 和 proof-preserving attention。在 formal-informal routing 概念上与本 proposal 有重叠，但操作层级不同（翻译质量 vs. 验证路由）。
- **Risk-Controlled Lean-as-Judge** (arXiv 2026): 43% faithfulness, 28-79% coverage。这是本 proposal soundness claim 的关键约束条件。
- **Faithful Autoformalization via Roundtrip Verification** (arXiv:2604.25031): 提供 roundtrip verification 方法论提升 faithfulness。

- **调研总结**: 当前 PRM 领域正在经历从判别式→生成式（GenPRM, ThinkPRM）和从纯神经→hybrid formal-neural（FoVer, VERGE, LogicReward）两个平行趋势。在 hybrid 方向上，如何智能地决定何时使用 formal verification 是公认的 open problem（VERGE 明确指出），但同时 autoformalization 的可靠性问题（43% faithfulness）对 formal 方法的实际价值构成了严重约束。

---

【发掘点 1】
- **维度**: trivial alternative 威胁
- **内容**: 本 proposal 最大的 trivial alternative 是 **"always-try-Z3 + neural fallback"**——即不训练 router，对每个步骤直接尝试 autoformalize + Z3 验证，Z3 失败（编译失败或超时）时 fallback 到 GenPRM。这本质上是 LogicReward 的改进版（用更强的 neural branch 替换 token-probability fallback）。Proposal 目前给出的 router 价值论证有三条：(a) 节省 autoformalization 计算，(b) 产生 per-step verification confidence signal，(c) 区分 intrinsic non-formalizability 和 extrinsic autoformalization failure。但 (a) 的 compute saving 在实际中有限（autoformalization 是一次 LLM call，不是 catastrophically expensive）；(b) 和 (c) 才是真正的差异化价值，但当前 proposal 对这两点的论证不够深入。**建议**：必须在 proposal 中正面处理这个 trivial alternative，最好在 ablation 中加入 "always-try-Z3 + neural fallback" 作为显式 baseline（当前的 ablation 列表中没有这个），并清晰论证 learned router 在减少 formal branch false alarms（因 non-formalizable 步骤被错误送入 Z3 而产生的假阳性）方面的不可替代价值。Router 的核心价值不是"节省计算"，而是"减少 formal branch 对 non-formalizable 步骤的系统性假阳性"——这个 framing 比当前的论述更锐利、更defensible。
- **价值**: 直接关系 novelty——如果审稿人认为 trivial alternative 能达到类似效果，整个 learned router 的贡献将被大幅削弱。正面应对 trivial alternative 是保住核心 novelty claim 的关键。
- **调研依据**: FoVer 文档中记录的 "overly-strict behavior" 正是 non-formalizable 步骤被送入 formal verification 的后果；VERGE 的 rule-based routing 也正是为了避免这个问题。LogicReward 的 try-and-fail 策略实际上就是这个 trivial alternative 的一个实例。

【发掘点 2】
- **维度**: 核心 claim 强化 / 前提假设质疑
- **内容**: Proposal 声称 "formal soundness guarantees for a subset of reasoning steps"，但这个 soundness guarantee 有一个关键的、当前被低估的条件依赖：**autoformalization 的 faithfulness**。根据 Risk-Controlled Lean-as-Judge 的数据，autoformalization 仅有 43% faithfulness。这意味着即使 router 正确识别了 formalizable 步骤，且 Z3 返回 SAT，如果 autoformalization 不 faithful（即形式化表达不忠实于原始自然语言步骤），这个"verified"结果是 vacuously correct——验证的是一个与原始步骤语义不同的形式化命题。因此，**实际的 soundness guarantee 仅在 "router 正确 × autoformalization faithful × Z3 correct" 的交集上成立**。按照当前数据粗略估算，如果 30-50% 的步骤被路由到 formal branch，其中 43% faithfully formalized，实际享受 soundness guarantee 的步骤可能仅占全部步骤的 13-22%。**建议**：(1) 将 soundness claim 精确限定为 "conditional on faithful autoformalization"，避免审稿人挑战 overclaiming；(2) 将 roundtrip verification（arXiv:2604.25031，proposal 已引用但未深度整合）作为 autoformalization 质量的 gatekeeper——只有通过 roundtrip verification 的形式化步骤才进入 Z3 验证，未通过的 fallback 到 neural branch。这实际上将 pipeline 从两层（router → formal/neural）变为三层（router → roundtrip check → formal/neural），显著增强 soundness claim 的可信度。
- **价值**: 直接决定核心 contribution #1 的可信度。Soundness guarantee 是本 proposal 区别于所有纯神经 PRM 的最核心 selling point，但如果审稿人指出这个 guarantee 建立在 43% faithfulness 的脆弱基础上，整个 contribution 会被严重打折。精确限定 + roundtrip verification gatekeeper 可以将这个弱点转化为成熟可信的 contribution。
- **调研依据**: Risk-Controlled Lean-as-Judge 的 43% faithfulness 数据；arXiv:2604.25031 的 roundtrip verification 方法论。

【发掘点 3】
- **维度**: significance 提升 / novelty 锐化
- **内容**: 当前 proposal 将自己的贡献 frame 为 "routing"——一个二元的分发决策。但更深层地看，本 proposal 实际上在构建的是一个 **分层验证置信度体系 (verification confidence hierarchy)**：(a) 通过 roundtrip verification 的 Z3 verified 步骤 → 最高置信度（formal guarantee），(b) 未通过 roundtrip verification 但 Z3 编译成功的步骤 → 中等置信度（formal but potentially unfaithful），(c) 被 router 识别为 non-formalizable 的步骤 → neural verification 置信度，(d) router 不确定的步骤 → 最低置信度。这个 **从二元路由到连续置信度谱** 的 reframing 将贡献从 "engineering design"（怎么路由）提升为 "scientific contribution"（怎么为每个步骤的验证结果赋予有意义的校准置信度）。这种 verification confidence hierarchy 对下游 Best-of-N reranking 和 RL reward shaping 都有直接价值——不同置信度层级的验证信号应被赋予不同的 reward weight。目前 PRM 文献中没有任何工作提出这种分层置信度框架。
- **价值**: 显著提升 significance 和 novelty。"Learned routing" 容易被审稿人视为 incremental engineering（VERGE 已经有 routing，你只是把 rule-based 换成 learned）。"Calibrated verification confidence hierarchy" 是一个更 fundamental 的框架贡献，对 PRM 领域的认知方式有推动作用——从 "每步给一个 score" 到 "每步给一个 score + 该 score 的可信度来源标注"。
- **调研依据**: 基于领域整体趋势判断。当前所有 PRM（GenPRM, ThinkPRM, R-PRM, FoVer）都输出一个 scalar score 或 binary label，没有任何工作区分"这个 score 是怎么得到的、有多可信"。这是一个 genuine gap。

【发掘点 4】
- **维度**: related work 差异化
- **内容**: Proposal 遗漏了 **FIRMA** (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5) 的讨论。FIRMA 提出了一个 "complexity router" 用于 formal-informal 数学语言的双向对齐，虽然它操作在翻译质量层面而非验证层面，但一个 well-informed 的审稿人可能会指出概念上的相似性：都是用一个 router 来决定 formal vs. informal 处理路径。**建议**：在 related work 中明确讨论 FIRMA，指出关键差异——FIRMA 的 complexity router 是为翻译质量服务（formal-informal alignment），本 proposal 的 formalizability router 是为验证正确性服务（derivability checking），目标函数和训练信号完全不同。这种主动的差异化定位比让审稿人自己发现这个遗漏要好得多。
- **价值**: 保护 novelty claim 免受审稿人的"这不是已经有人做了吗"质疑。Related work 的完整性直接影响审稿人对 novelty 判断的信任度。
- **调研依据**: FIRMA (ACL Anthology 2025.mathnlp-main.5)，其 complexity router 架构与本 proposal 的 formalizability router 在概念层面有表面相似性。

【发掘点 5】
- **维度**: novelty 锐化
- **内容**: 当前 proposal 将 learned router 的 novelty 主要对标 VERGE（rule-based → learned）和 LogicReward（try-and-fail → learned prediction）。但这个差异化 framing 有一个潜在弱点：审稿人可能认为 "把 rule-based 替换成 learned classifier 是 2015 年的想法，不构成 2026 年的 novelty"。Proposal 需要更锐利地阐述 **为什么 formalizability 的 context-dependent 预测本身是一个 non-trivial 的学习问题**。具体来说：一个步骤是否可形式化不仅取决于步骤本身的语义内容（VERGE 的 rule-based 能处理的部分），还取决于 (1) predecessor chain 建立的 formal context（前面的步骤已经引入了哪些形式化定义和变量），(2) autoformalization 工具的当前能力边界（不同的步骤类型有不同的 formalization 成功率），(3) 步骤在证明中的位置（early steps 往往更 declarative/formalizable，later steps 可能涉及更多 heuristic reasoning）。这些 context dependencies 使得 formalizability prediction 不可还原为 static claim-type classification——必须是 learned 和 context-dependent 的。当前 proposal 提到了 "conditioned on the full predecessor chain" 但没有充分展开这一点的 non-triviality。
- **价值**: 直接强化核心 novelty claim。将 "learned router" 从 "obvious engineering improvement" 提升为 "solving a genuinely non-trivial prediction problem that rule-based approaches cannot address in principle"。
- **调研依据**: VERGE 的 rule-based routing 仅基于 static claim types（logical vs. commonsense），完全不考虑 predecessor context。LogicReward 的 try-and-fail 策略同样不做任何预测。这说明 context-dependent formalizability prediction 确实是一个未被解决的问题，但 proposal 需要更好地论证其 non-triviality。

---

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055)
- [LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)
- [Process Reward Models That Think (ThinkPRM)](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards](https://arxiv.org/abs/2510.07774)
- [FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment](https://aclanthology.org/2025.mathnlp-main.5/)
- [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](https://arxiv.org/html/2605.28365)
- [Faithful Autoformalization via Roundtrip Verification](https://arxiv.org/abs/2604.25031)
- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)

【补救 agent 本轮输出】:
Now I have sufficient research context. Let me compile my assessment.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **GenPRM (AAAI 2026, arXiv:2504.00891)**: 实验用 ProcessBench F1 + PRMBench F1 + Best-of-N (MATH-500, AIME24, OlympiadBench, Omni-MATH)；baseline 包括 Math-Shepherd, RLHFlow, Skywork-PRM, Qwen2.5-Math-PRM-72B 等；ablation 包括 data scaling、RPE vs. ORM labels、code verification 贡献隔离。Majority voting 在 token budget 控制下作为核心对照。
- **FoVer (ACL 2026 Findings, arXiv:2505.15960)**: 评测覆盖 12 个推理 benchmark（含 NLI、BBH 等 OOD 任务）；用 Best-of-K 评价 PRM 泛化性；ablation 拆分 formal logic data vs. formal theorem proof data 的贡献；baseline 对比 base LLM 及 human/strong-model-annotated PRMs。AUROC 为其主要指标。
- **ThinkPRM (arXiv:2504.16828, submitted ICLR 2026)**: 强调 token-budget-normalized 对比——在相同 token 预算下 ThinkPRM 超 LLM-as-Judge 7.2%；评测 ProcessBench、MATH-500、AIME'24、GPQA-Diamond、LiveCodeBench（OOD）；ablation 拆分 process-label filtering vs. answer-only filtering。
- **R-PRM (EMNLP 2025, arXiv:2503.21295)**: 三阶段方法（cold-start → DPO → inference scaling），评测 ProcessBench + PRMBench + 6 个数学数据集；baseline 包括 Math-Shepherd, Math-PSA, RLHFlow, Skywork-PRM, ReasonEval, Llemma-PRM800K, Qwen2.5-Math-PRM；ablation 逐阶段贡献分析。
- **VERGE (arXiv:2601.20055)**: 核心是 Semantic Routing（rule-based），claim 分类为 logical vs. commonsense，分别送 Z3 和 LLM ensemble；用 Minimal Correction Subsets 做 error localization；报告 18.7% uplift，但未做 learned routing 对照。
- **LogicReward (ICLR 2026, arXiv:2512.18196)**: 用 Isabelle 做 step-level verification + Autoformalization with Soft Unification；评测 8 个 logical reasoning / NLI benchmark；结果显示 8B 模型超 GPT-4o 11.6%。但其是 RL 训练框架而非独立 PRM，直接对比需注意 apples-to-oranges 问题。
- **RRM / Miracle Steps (arXiv:2510.07774)**: 定义 miracle step taxonomy，报告 RRM 将 miracle step 发生率降低 71%（Verified Pass@1024 on AIME2024: 26.7% → 62.6%），但该论文已从 ICLR 2026 撤稿，其 annotations 的公开可用性存疑。
- **调研总结**: 当前 PRM 领域的实验标准要求：(1) ProcessBench F1/AUROC + PRMBench PRMScore 作为核心 step-level 评测；(2) Best-of-N (N=8/16/64) 在 MATH-500/AIME24 上作为下游任务评测；(3) token-budget / compute-normalized 公平对比已成为审稿人标准要求（ThinkPRM 开创先例）；(4) ablation 需隔离各核心组件贡献；(5) OOD 泛化评测被多数高分论文包含。

---

【缺陷 1】
- 类别: 可行性问题
- 问题: Proposal 的核心 claim 之一——"sound miracle step detection"——其评测依赖 "RRM miracle taxonomy annotations (Yuan et al., 2025)"。但 RRM 论文已从 ICLR 2026 撤稿（proposal 自己也承认这一点），其 miracle step taxonomy annotations 的**公开可用性未确认**。如果这些标注数据不可获取，Miracle step detection 的 precision/recall/F1 评测将无法执行，而这正是该 proposal 三个 contribution 中第一个的直接实验支撑。
- 严重度: 可补救
- 补救方案: 三层保障策略——(1) **立即确认数据可用性**：检查 RRM 的 GitHub repo 或联系作者确认标注数据是否公开，撤稿不一定意味着数据不可用；(2) **自建 miracle step 标注**：在 ProcessBench 或 PRMBench 中抽取 200–300 个 step，请 2–3 名标注者按 RRM 的 miracle step 定义（"unjustified logical leap"）进行标注并报告 inter-annotator agreement（Cohen's kappa），这在学术 budget 内可行；(3) **利用 PRMBench 已有错误分类**：PRMBench 包含 fine-grained error type breakdown（83,456 step-level labels），其中部分错误类别（如 "logical gap"、"unjustified step"）可作为 miracle step 的 proxy 指标，proposal 中已提到这一点但应将其从 "supplementary" 升级为 "primary evaluation（if RRM data unavailable）"。
- 调研依据: PRMBench (ACL 2025, arXiv:2501.03124) 提供 6,216 problems + 83,456 step labels 的 fine-grained 错误分类；RRM 论文确认已从 ICLR 2026 撤稿。

【缺陷 2】
- 类别: compute 公平性问题
- 问题: Proposal 在 Compute Budget 中将 autoformalization 描述为 "LLM calls for formalizable steps (estimated 30–50% of total steps)"，但**未明确指定用哪个 LLM 做 autoformalization，也未将 autoformalization 的 compute 纳入 per-step 推理成本计算**。Autoformalization 通常需要强 LLM（至少 7B+，实践中常用 70B+ 或 API models），这可能是整个 pipeline 中 compute 开销最大的部分。如果 compute Pareto 曲线不包含 autoformalization 开销，与 GenPRM majority voting 等 baseline 的 compute-matched 对比将不公平——审稿人极有可能质疑这一点。
- 严重度: 可补救
- 补救方案: (1) **明确 autoformalization 模型**：指定使用哪个 LLM 进行 autoformalization（例如 Qwen2.5-Math-72B-Instruct 或 GPT-4o），并报告其 per-step 推理成本（tokens/step, latency, FLOPs）；(2) **将 autoformalization 开销纳入 total compute**：在 accuracy vs. compute Pareto 曲线中，FormalRoute-PRM 的 compute 必须包含 router inference + autoformalization + Z3 solving + neural branch（对分到该 branch 的 step）；(3) **增加一个 compute ablation**：对比使用不同规模 autoformalization 模型（如 7B vs. 72B）时的 accuracy-cost tradeoff，这也能展示系统对 autoformalization 质量的敏感性；(4) **考虑 autoformalization caching**：对于 evaluation benchmark 中重复出现的公式模式，是否可以 cache autoformalization 结果以降低实际推理开销。
- 调研依据: ThinkPRM (arXiv:2504.16828) 确立了 token-budget-normalized 对比范式，在同等 token 预算下展示优势是审稿人标准期望；GenPRM 的 majority voting 在控制 compute 下作为对照也是这一范式的体现。

【缺陷 3】
- 类别: 实验设计不足
- 问题: Router 的训练标签构建方案存在 **label noise 问题未被讨论**。Proposal 称 router 训练于 "FoVer Z3 verification labels + autoformalization success signals"，但这些标签将三类不同情况混为一谈：(a) step 本身不可形式化（true negative）；(b) step 可形式化但 autoformalization 失败（false negative）；(c) Z3 超时或内存溢出（indeterminate）。Proposal 提到用 roundtrip verification (arXiv:2604.25031) 来提高 faithfulness，但**未讨论如何处理 (b) 和 (c) 导致的 label noise 对 router 训练的影响**，也未给出 label quality 的估计。审稿人极可能质疑 router 的训练信号质量。
- 严重度: 可补救
- 补救方案: (1) **在 router analysis 中增加 label quality 评估**：从训练数据中抽样 200–300 个 "non-formalizable" label，人工验证其中有多少是 true non-formalizable vs. autoformalization failure，报告 label precision；(2) **在 ablation 中增加 label noise robustness 实验**：人工清洗一小批标签（如 500–1000 条）训练一个 "clean-label router"，对比使用 noisy label 的 router，量化 label noise 的影响；(3) **明确 label 构建 pipeline**：详述从 FoVer 数据到 router 训练标签的完整流程——哪些 step 标为 formalizable（Z3 编译成功 AND roundtrip 通过）、哪些标为 non-formalizable（autoformalization 失败 OR roundtrip 失败 OR Z3 超时），以及如何处理 ambiguous cases；(4) **讨论 coverage of formal verification 工具的局限**：引用已有的 autoformalization faithfulness 数据（约 43% faithfulness in literature），诚实估算 router 训练标签中 false negative 的比例。
- 调研依据: FoVer (arXiv:2505.15960) 的 ablation 显示 formal logic 和 theorem proof data 的贡献不完全累加，暗示数据质量/一致性问题；autoformalization faithfulness 研究 (arXiv:2604.19459 等) 指出 syntactic correctness ≠ semantic faithfulness 是普遍问题。

【缺陷 4】
- 类别: 实验设计不足
- 问题: Proposal 缺少 **OOD (out-of-distribution) 泛化评测**。Router 训练于 FoVer 衍生的数学/逻辑推理数据，但 proposal 的评测全部集中在数学推理 benchmark（ProcessBench, PRMBench, MATH-500, AIME24）。高水平 PRM 论文（如 FoVer 在 NLI/BBH 上评测、ThinkPRM 在 GPQA-Diamond/LiveCodeBench 上评测）均包含 OOD 评测来验证泛化性。审稿人会质疑：router 和整体系统在 **非数学推理任务**（如科学推理、代码推理、commonsense 推理）上表现如何？router 是否会在 OOD 场景下将不可形式化的 step 错误路由到 Z3？
- 严重度: 可补救
- 补救方案: (1) 增加 1–2 个 OOD benchmark：**GPQA-Diamond**（科学推理，ThinkPRM 用过）和 **BBH**（多样化推理任务，FoVer 用过）是最自然的选择，已有 PRM 评测先例；(2) 在 router analysis 中，单独报告 OOD 场景下的 router classification accuracy——预期 router 在 OOD 场景下会更多地将 step 路由到 neural branch（因为 OOD step 大多不可形式化），这本身是系统正确行为的体现，应显式验证并报告；(3) 如果 OOD 评测显示性能下降，这不一定是负面结果——可以解读为"系统在 OOD 场景下 graceful degrade 到 neural-only baseline"，只要不比 neural-only baseline 差即可。
- 调研依据: FoVer (arXiv:2505.15960) 在 NLI、BBH 等 OOD 任务上评测泛化性是其被接受的重要因素；ThinkPRM (arXiv:2504.16828) 在 GPQA-Diamond 和 LiveCodeBench 上做 OOD 评测，超 discriminative PRM 8% / 4.5%。

【缺陷 5】
- 类别: baseline 不足或过时
- 问题: Proposal 的 baseline matrix 中 **LogicReward 的对比存在 apples-to-oranges 风险**。LogicReward 是一个 RL 训练框架（用 Isabelle 验证生成 reward signal 来训练 LLM），而非独立的 step-level PRM。直接将其作为 "hybrid PRM baseline" 与 FormalRoute-PRM 在 ProcessBench/PRMBench 上对比可能不公平或不可行——LogicReward 的输出是一个训练好的 LLM，而非一个 step-level verifier score。此外，LogicReward 使用 **Isabelle** 而 FormalRoute-PRM 使用 **Z3**，formal backend 不同也增加对比的复杂性。
- 严重度: 可补救
- 补救方案: (1) **明确 LogicReward 的对比方式**：如果将 LogicReward 作为 baseline，需说明如何从 LogicReward 的框架中提取 step-level score（例如使用 LogicReward 训练后的 LLM 的 per-step logprob 或 rubric score）；(2) **区分两种对比维度**：LogicReward 可作为 "hybrid formal+neural approach" 的 conceptual comparison（方法论层面），而在 quantitative benchmark 对比中应标注其不同性质，避免审稿人认为对比不公平；(3) **考虑补充一个更直接可比的 baseline**：例如用 FoVer 的 Z3 verification + 简单 try-and-fallback（Z3 失败则用 neural PRM）作为 "naive hybrid" baseline，这比 LogicReward 更直接地对照 learned routing vs. try-and-fallback 的差异。这个 baseline 实际上就是 contribution 2 想要超越的直接对手，且实现成本极低。
- 调研依据: LogicReward (ICLR 2026) 的实验设计是在 8 个 logical reasoning/NLI benchmark 上评测 RL 训练后的 LLM，而非 step-level PRM evaluation；FoVer 使用 Z3+Isabelle 双后端但也只对比 PRM 框架内的 baseline。

【缺陷 6】
- 类别: ablation 不完整
- 问题: 当前 ablation 设计覆盖了 routing 策略的对比（formal-only / neural-only / random / oracle / threshold sweep），但**缺少对 neural branch 选择的 ablation**。Proposal 选择 GenPRM-7B + ARES-style calibrated entailment 作为 neural branch，但未验证这个选择的贡献。具体来说，缺少两个对照：(a) 将 neural branch 替换为更简单的 discriminative PRM（如 FoVer-7B 自身的 PRM score），验证 GenPRM 作为 neural branch 的必要性；(b) 将 neural branch 替换为 ThinkPRM-style long CoT verification，验证 generative vs. discriminative neural branch 的差异。此外，**ARES-style calibrated entailment 的具体集成方式未详述**——这是附加在 GenPRM 输出上的 calibration layer 还是独立模块？
- 严重度: 可补救
- 补救方案: (1) 增加 ablation：**FormalRoute-PRM (GenPRM neural branch) vs. FormalRoute-PRM (discriminative PRM neural branch)**，隔离 neural branch 选择的贡献；(2) 明确 ARES-style calibration 的具体实现和集成方式——是 temperature scaling、Platt scaling 还是其他方法？在 router 的 formal confidence vs. neural confidence 整合中，calibration 的实现直接影响最终 score 的质量；(3) 如果时间/compute 有限，至少在 related work 或 discussion 中讨论 neural branch 选择的设计理由并承认这是一个可探索的 axis。
- 调研依据: GenPRM (AAAI 2026) 和 ThinkPRM (arXiv:2504.16828) 代表 generative PRM 的两种不同范式（RPE+code verification vs. long CoT），在 PRM 论文中 neural component 的选择通常需要 justify。

【缺陷 7】
- 类别: 可行性问题
- 问题: Proposal 引用 "Risk-Controlled Lean-as-Judge (arXiv 2026)" 的 "43% faithfulness, 28–79% coverage" 数据作为多处论证的关键依据（router threshold 设计、honest coverage reporting 方法论、asymmetric cost 论证），但**未提供 arXiv ID**，我的调研也未找到这篇具体论文。如果这篇论文不存在、尚未公开、或其数据被误引，相关论证的基础将被审稿人质疑。
- 严重度: 可补救
- 补救方案: (1) **提供完整引用**：补全 arXiv ID 或 URL，确保论文可查证；(2) **如果论文确实存在但尚未公开**：改为引用其他已公开的 autoformalization faithfulness 数据——例如 "Do LLMs Game Formalization?" (arXiv:2604.19459) 和 "Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing" (arXiv:2511.12784) 都讨论了 autoformalization 的 faithfulness 限制；(3) **自行量化 faithfulness**：在 FoVer 数据上运行 autoformalization pipeline，对 200–300 个 step 人工验证 autoformalization 的 semantic faithfulness，得到自己的 faithfulness 估计。这既加强论证的可信度，也是对 router 训练标签质量的直接验证（与缺陷 3 的补救方案互补）。
- 调研依据: 多篇 autoformalization 评测论文 (arXiv:2604.19459, arXiv:2510.15981, arXiv:2511.12784) 均指出 faithfulness 是核心瓶颈，但具体数字因实验设置而异，需确保引用数据有可追溯来源。

Sources:
- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/abs/2601.20055)
- [LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision](https://openreview.net/forum?id=A3FhAVfcJI)
- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)
- [Curing "Miracle Steps" in LLM Mathematical Reasoning with Rubric Rewards](https://arxiv.org/abs/2510.07774)
- [PRoSFI: Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries](https://arxiv.org/abs/2603.29500)
- [Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning](https://arxiv.org/html/2604.19459)
- [Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing](https://arxiv.org/pdf/2511.12784)
- [PRISM: Pushing the Frontier of Deep Think via Process Reward Model-Guided Inference](https://arxiv.org/html/2603.02479)
- [GenPRM GitHub Repository](https://github.com/RyanLiu112/GenPRM)
- [FoVer GitHub Repository](https://github.com/psunlpgroup/FoVer)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a299d4b1-17f8-48b5-981e-9589ab1d8d5b",
  "isSidechain": false,
  "promptId": "381e9bf1-a558-40a2-a586-041a6e2d16a9",
  "type": "user",
  "uuid": "eaa3466b-d882-4968-878a-eea6c29d16a4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to make an informed evaluation. Let me synthesize my findings.  ---  【状态】: 有…",
  "leafUuid": "eaa3466b-d882-4968-878a-eea6c29d16a4",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Assistant

_source line 52 · 2026-05-29T06:17:04.008Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the second round outputs from both workers and cross-validate their key suggestions.

**发掘 agent Round 2 summary:**
- Status: 有发掘空间
- 5 points:
  1. Trivial alternative "always-try-Z3 + neural fallback" needs explicit ablation baseline; router value = reducing formal branch false alarms, not just saving compute
  2. Soundness claim needs conditioning on faithful autoformalization; suggest roundtrip verification as gatekeeper (three-layer pipeline)
  3. Verification confidence hierarchy framing (from binary routing to continuous confidence spectrum)
  4. Missing FIRMA (MathNLP 2025) in related work
  5. Need to argue non-triviality of context-dependent formalizability prediction

**补救 agent Round 2 summary:**
- Status: 有缺陷待补救
- 7 defects:
  1. RRM miracle step annotation data availability uncertain
  2. Autoformalization compute not included in cost comparison; no specified autoformalization model
  3. Router training label noise problem (three types of failures mixed)
  4. Missing OOD evaluation (GPQA-Diamond, BBH)
  5. LogicReward comparison is apples-to-oranges; need "naive" baseline clarification
  6. Missing neural branch ablation; ARES calibration details unclear
  7. Risk-Controlled Lean-as-Judge paper citation lacks arXiv ID

Now I'm cross-checking several key claims: whether FIRMA actually has a complexity router, if the Risk-Controlled Lean-as-Judge paper exists with a proper citation, whether always-trying Z3 with fallback is standard practice, and if GPQA-Diamond and BBH are typical OOD benchmarks for PRM papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eaa3466b-d882-4968-878a-eea6c29d16a4",
  "isSidechain": false,
  "requestId": "req_011CbWNW3zC4ZCPm7m4EYYjt",
  "type": "assistant",
  "uuid": "41978410-66c8-4a73-bcca-9d19ed19e912",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AN8ZULQLEbAPvJSRZZANHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17481,
      "cache_read_input_tokens": 37103,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 37103,
          "cache_creation_input_tokens": 17481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17481
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

_source line 53 · 2026-05-29T06:17:04.013Z_

让我对第 2 轮 worker 的关键建议做交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41978410-66c8-4a73-bcca-9d19ed19e912",
  "isSidechain": false,
  "requestId": "req_011CbWNW3zC4ZCPm7m4EYYjt",
  "type": "assistant",
  "uuid": "d8314ae6-a6ce-43ee-9afb-f108d4362b10",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AN8ZULQLEbAPvJSRZZANHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17481,
      "cache_read_input_tokens": 37103,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 37103,
          "cache_creation_input_tokens": 17481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17481
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

_source line 54 · 2026-05-29T06:17:04.464Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K7pghVRUqhpY1skB3XrniJ`</summary>

```json
{
  "query": "FIRMA bidirectional formal informal mathematical language alignment MathNLP 2025 complexity router"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8314ae6-a6ce-43ee-9afb-f108d4362b10",
  "isSidechain": false,
  "requestId": "req_011CbWNW3zC4ZCPm7m4EYYjt",
  "type": "assistant",
  "uuid": "15cf445c-1ff9-4a2a-a8d1-5f6e8662c9d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AN8ZULQLEbAPvJSRZZANHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17481,
      "cache_read_input_tokens": 37103,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 37103,
          "cache_creation_input_tokens": 17481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17481
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

_source line 55 · 2026-05-29T06:17:04.922Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N6nu4dpNfRdaJ9Qc8qmDeQ`</summary>

```json
{
  "query": "\"Risk-Controlled\" \"Lean-as-Judge\" autoformalization faithfulness arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15cf445c-1ff9-4a2a-a8d1-5f6e8662c9d9",
  "isSidechain": false,
  "requestId": "req_011CbWNW3zC4ZCPm7m4EYYjt",
  "type": "assistant",
  "uuid": "5fbd3d84-ad0a-44e7-b0fd-21362ae02f14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AN8ZULQLEbAPvJSRZZANHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17481,
      "cache_read_input_tokens": 37103,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 37103,
          "cache_creation_input_tokens": 17481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17481
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

_source line 56 · 2026-05-29T06:17:05.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UfCoQXM8uJDF9dc4HFwMhT`</summary>

```json
{
  "query": "GPQA-Diamond BBH out-of-distribution evaluation process reward model PRM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fbd3d84-ad0a-44e7-b0fd-21362ae02f14",
  "isSidechain": false,
  "requestId": "req_011CbWNW3zC4ZCPm7m4EYYjt",
  "type": "assistant",
  "uuid": "bb7b95ef-4b3f-43c1-b21a-f9ab9cb3676d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AN8ZULQLEbAPvJSRZZANHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17481,
      "cache_read_input_tokens": 37103,
      "output_tokens": 738,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17481,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 738,
          "cache_read_input_tokens": 37103,
          "cache_creation_input_tokens": 17481,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17481
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

_source line 57 · 2026-05-29T06:17:11.308Z_

<details><summary>↩ Tool result · `toolu_01K7pghVRUqhpY1skB3XrniJ`</summary>

```text
Web search results for query: "FIRMA bidirectional formal informal mathematical language alignment MathNLP 2025 complexity router"

Links: [{"title":"FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding - ACL Anthology","url":"https://aclanthology.org/2025.mathnlp-main.5/"},{"title":"Proceedings of The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.mathnlp-main/"},{"title":"Workshop on Mathematical Natural Language Processing (2025) - ACL Anthology","url":"https://aclanthology.org/events/mathnlp-2025/"},{"title":"MathNLP 2025 MathNLP 2025: The 3rd Workshop on Mathematical Natural","url":"https://aclanthology.org/2025.mathnlp-main.0.pdf"},{"title":"GitHub - smfatima3/FIRMA: The official codebase of the paper \"FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding\"","url":"https://github.com/smfatima3/FIRMA"},{"title":"FIRMA: Bidirectional Formal-Informal Mathematical ...","url":"https://aclanthology.org/2025.mathnlp-main.5.pdf"},{"title":"Alignment Methods for Formal Logical Reasoning","url":"https://aclanthology.org/2025.mathnlp-main.8.pdf"},{"title":"Contrastive Alignment for LLM Mathematics with Lean","url":"https://aclanthology.org/2025.mathnlp-main.15.pdf"},{"title":"First Experiments with Neural Translation of Informal to Formal   Mathematics","url":"https://arxiv.org/pdf/1805.06502"},{"title":"Developing Corpus-based Translation Methods between Informal and Formal   Mathematics: Project Description","url":"https://arxiv.org/pdf/1405.3451"}]

Based on the search results, I found comprehensive information about FIRMA:

## FIRMA Overview

FIRMA (Formal-Informal Reasoning in Mathematical Alignment) is a bidirectional translation system between formal and informal mathematical language that leverages proof-theoretic interpretability hierarchies and specialized architectural components for proof preservation.

## Key Architecture Components

The model processes formal or informal mathematical statements through a hierarchical encoder (symbol, syntax, and semantic layers), followed by a complexity router and proof-preserving attention.

## Publication Details

FIRMA was presented by Maryam Fatima at the Proceedings of The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) in Suzhou, China.

## Problem it Addresses

While large language models excel at generating plausible mathematical text, they often produce subtly incorrect formal translations that violate proof-theoretic constraints.

The system represents a significant advancement in handling the translation between formal mathematical language (such as Lean 4 syntax) and informal mathematical writing, with specific architectural innovations like the complexity router to handle varying levels of mathematical sophistication.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15cf445c-1ff9-4a2a-a8d1-5f6e8662c9d9",
  "isSidechain": false,
  "promptId": "381e9bf1-a558-40a2-a586-041a6e2d16a9",
  "type": "user",
  "uuid": "e7f3796c-f3b6-417e-a677-919e5a47ae7b",
  "toolUseResult": {
    "query": "FIRMA bidirectional formal informal mathematical language alignment MathNLP 2025 complexity router",
    "results": [
      {
        "tool_use_id": "srvtoolu_011FQvH4kC9ZzQyt2BC7R95F",
        "content": [
          {
            "title": "FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding - ACL Anthology",
            "url": "https://aclanthology.org/2025.mathnlp-main.5/"
          },
          {
            "title": "Proceedings of The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) - ACL Anthology",
            "url": "https://aclanthology.org/volumes/2025.mathnlp-main/"
          },
          {
            "title": "Workshop on Mathematical Natural Language Processing (2025) - ACL Anthology",
            "url": "https://aclanthology.org/events/mathnlp-2025/"
          },
          {
            "title": "MathNLP 2025 MathNLP 2025: The 3rd Workshop on Mathematical Natural",
            "url": "https://aclanthology.org/2025.mathnlp-main.0.pdf"
          },
          {
            "title": "GitHub - smfatima3/FIRMA: The official codebase of the paper \"FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment with Proof-Theoretic Grounding\"",
            "url": "https://github.com/smfatima3/FIRMA"
          },
          {
            "title": "FIRMA: Bidirectional Formal-Informal Mathematical ...",
            "url": "https://aclanthology.org/2025.mathnlp-main.5.pdf"
          },
          {
            "title": "Alignment Methods for Formal Logical Reasoning",
            "url": "https://aclanthology.org/2025.mathnlp-main.8.pdf"
          },
          {
            "title": "Contrastive Alignment for LLM Mathematics with Lean",
            "url": "https://aclanthology.org/2025.mathnlp-main.15.pdf"
          },
          {
            "title": "First Experiments with Neural Translation of Informal to Formal   Mathematics",
            "url": "https://arxiv.org/pdf/1805.06502"
          },
          {
            "title": "Developing Corpus-based Translation Methods between Informal and Formal   Mathematics: Project Description",
            "url": "https://arxiv.org/pdf/1405.3451"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about FIRMA:\n\n## FIRMA Overview\n\nFIRMA (Formal-Informal Reasoning in Mathematical Alignment) is a bidirectional translation system between formal and informal mathematical language that leverages proof-theoretic interpretability hierarchies and specialized architectural components for proof preservation.\n\n## Key Architecture Components\n\nThe model processes formal or informal mathematical statements through a hierarchical encoder (symbol, syntax, and semantic layers), followed by a complexity router and proof-preserving attention.\n\n## Publication Details\n\nFIRMA was presented by Maryam Fatima at the Proceedings of The 3rd Workshop on Mathematical Natural Language Processing (MathNLP 2025) in Suzhou, China.\n\n## Problem it Addresses\n\nWhile large language models excel at generating plausible mathematical text, they often produce subtly incorrect formal translations that violate proof-theoretic constraints.\n\nThe system represents a significant advancement in handling the translation between formal mathematical language (such as Lean 4 syntax) and informal mathematical writing, with specific architectural innovations like the complexity router to handle varying levels of mathematical sophistication."
    ],
    "durationSeconds": 6.833859636999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "15cf445c-1ff9-4a2a-a8d1-5f6e8662c9d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-29T06:17:12.203Z_

<details><summary>↩ Tool result · `toolu_01UfCoQXM8uJDF9dc4HFwMhT`</summary>

```text
Web search results for query: "GPQA-Diamond BBH out-of-distribution evaluation process reward model PRM 2025 2026"

Links: [{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"The Bidirectional Process Reward Model","url":"https://arxiv.org/pdf/2508.01682"},{"title":"The Lessons of Developing Process Reward Models in Mathematical Reasoning","url":"https://arxiv.org/pdf/2501.07301"},{"title":"GPQA Diamond | Epoch AI","url":"https://epoch.ai/benchmarks/gpqa-diamond"},{"title":"AI developers accurately report GPQA Diamond scores for recent models | Epoch AI","url":"https://epoch.ai/data-insights/self-reported-gpqa"},{"title":"GPQA-Diamond Benchmark: Scores, Leaderboard & How AI Models Compare | IntuitionLabs","url":"https://intuitionlabs.ai/articles/gpqa-diamond-ai-benchmark"},{"title":"Retrieval-Augmented Process Reward Model for Generalizable Mathematical   Reasoning","url":"https://arxiv.org/pdf/2502.14361"}]

Based on the web search results, here's what I found regarding your query about GPQA-Diamond, BBH, out-of-distribution evaluation, and process reward models:

## Key Findings:

**Process Reward Models and Out-of-Distribution Evaluation:**

A recent study evaluated PRMs on out-of-domain subsets of GPQA-Diamond and LiveCodeBench, with PRMs surpassing discriminative verifiers trained on full datasets.

Existing PRM approaches still face out-of-distribution challenges, which may occur due to different processes generated by different models.

**PRM Training and Benchmarking:**

ProcessBench has emerged as a benchmark to evaluate the capability of PRMs in identifying step-wise correctness.

Process Reward Models have been developed to rigorously evaluate the logical validity of intermediate steps.

**GPQA-Diamond Evaluation (2025-2026):**

AI developers accurately report GPQA Diamond scores for their recent top models, with independent standardized evaluations testing models on expert-level science questions.

In May 2025, an analysis of GPQA-Diamond found that roughly 2–3 questions might be invalid, concluding approximately 90–95% of the questions are valid.

The search results show active research in this area during 2025-2026, with focus on improving PRM generalization and addressing out-of-distribution challenges in benchmarks like GPQA-Diamond.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb7b95ef-4b3f-43c1-b21a-f9ab9cb3676d",
  "isSidechain": false,
  "promptId": "381e9bf1-a558-40a2-a586-041a6e2d16a9",
  "type": "user",
  "uuid": "7c226761-af23-47d8-8791-83cef0196a76",
  "toolUseResult": {
    "query": "GPQA-Diamond BBH out-of-distribution evaluation process reward model PRM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JXNAfZcsWiyN3Ymn71Deyp",
        "content": [
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "The Bidirectional Process Reward Model",
            "url": "https://arxiv.org/pdf/2508.01682"
          },
          {
            "title": "The Lessons of Developing Process Reward Models in Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2501.07301"
          },
          {
            "title": "GPQA Diamond | Epoch AI",
            "url": "https://epoch.ai/benchmarks/gpqa-diamond"
          },
          {
            "title": "AI developers accurately report GPQA Diamond scores for recent models | Epoch AI",
            "url": "https://epoch.ai/data-insights/self-reported-gpqa"
          },
          {
            "title": "GPQA-Diamond Benchmark: Scores, Leaderboard & How AI Models Compare | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/gpqa-diamond-ai-benchmark"
          },
          {
            "title": "Retrieval-Augmented Process Reward Model for Generalizable Mathematical   Reasoning",
            "url": "https://arxiv.org/pdf/2502.14361"
          }
        ]
      },
      "Based on the web search results, here's what I found regarding your query about GPQA-Diamond, BBH, out-of-distribution evaluation, and process reward models:\n\n## Key Findings:\n\n**Process Reward Models and Out-of-Distribution Evaluation:**\n\nA recent study evaluated PRMs on out-of-domain subsets of GPQA-Diamond and LiveCodeBench, with PRMs surpassing discriminative verifiers trained on full datasets.\n\nExisting PRM approaches still face out-of-distribution challenges, which may occur due to different processes generated by different models.\n\n**PRM Training and Benchmarking:**\n\nProcessBench has emerged as a benchmark to evaluate the capability of PRMs in identifying step-wise correctness.\n\nProcess Reward Models have been developed to rigorously evaluate the logical validity of intermediate steps.\n\n**GPQA-Diamond Evaluation (2025-2026):**\n\nAI developers accurately report GPQA Diamond scores for their recent top models, with independent standardized evaluations testing models on expert-level science questions.\n\nIn May 2025, an analysis of GPQA-Diamond found that roughly 2–3 questions might be invalid, concluding approximately 90–95% of the questions are valid.\n\nThe search results show active research in this area during 2025-2026, with focus on improving PRM generalization and addressing out-of-distribution challenges in benchmarks like GPQA-Diamond."
    ],
    "durationSeconds": 6.790157024,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bb7b95ef-4b3f-43c1-b21a-f9ab9cb3676d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-29T06:17:12.607Z_

<details><summary>↩ Tool result · `toolu_01N6nu4dpNfRdaJ9Qc8qmDeQ`</summary>

```text
Web search results for query: ""Risk-Controlled" "Lean-as-Judge" autoformalization faithfulness arXiv 2026"

Links: [{"title":"Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning","url":"https://arxiv.org/html/2605.28365"},{"title":"[2605.28365] Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning","url":"https://arxiv.org/abs/2605.28365"},{"title":"Conjecturing: An Overlooked Step in Formal Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.11986"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/pdf/2510.15981"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/pdf/2510.06857"},{"title":"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization","url":"https://arxiv.org/pdf/2510.24592"},{"title":"Reliable Evaluation and Benchmarks for Statement Autoformalization","url":"https://arxiv.org/pdf/2406.07222"},{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"}]

I found the paper you're looking for! Here are the key details about the search results:

## Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning

The paper addresses the challenge that Lean's signal is partial: many answers never formalize, and a failed proof may reflect an ill-typed statement or a missing library fact, not a wrong answer.

**Key Findings:**

On MATH-500, the signal is sharply coverage-dependent, with the proof-winning answer being correct 96% of the time at high proved coverage but 20% at low, and sparse and often unfaithful: a 7B autoformalizer proves a class for only 28% of problems, and a manual audit finds only approximately 43% of those proofs faithful.

**The Proposed Method:**

The authors propose COVCAL, a selector over Lean-trace diagnostics that certifies a finite-sample selective-risk bound on accepted answers or abstains, under two regimes (a conservative Bonferroni bound and a tighter dev-then-cal rule).

The contribution is described as a risk-controlled wrapper, using Qwen2.5-Math for generation and Qwen2.5-Coder for autoformalization.

The paper appears to have been published to arXiv very recently (2 days ago based on the metadata) with identifier 2605.28365.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5fbd3d84-ad0a-44e7-b0fd-21362ae02f14",
  "isSidechain": false,
  "promptId": "381e9bf1-a558-40a2-a586-041a6e2d16a9",
  "type": "user",
  "uuid": "7d901981-bfe6-4044-86ee-7ffb7b6d50dc",
  "toolUseResult": {
    "query": "\"Risk-Controlled\" \"Lean-as-Judge\" autoformalization faithfulness arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HtHbVYssarFuFFbdvSiC27",
        "content": [
          {
            "title": "Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning",
            "url": "https://arxiv.org/html/2605.28365"
          },
          {
            "title": "[2605.28365] Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2605.28365"
          },
          {
            "title": "Conjecturing: An Overlooked Step in Formal Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2510.11986"
          },
          {
            "title": "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://arxiv.org/pdf/2510.15981"
          },
          {
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/pdf/2510.06857"
          },
          {
            "title": "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization",
            "url": "https://arxiv.org/pdf/2510.24592"
          },
          {
            "title": "Reliable Evaluation and Benchmarks for Statement Autoformalization",
            "url": "https://arxiv.org/pdf/2406.07222"
          },
          {
            "title": "Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing",
            "url": "https://arxiv.org/pdf/2511.12784"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about the search results:\n\n## Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning\n\nThe paper addresses the challenge that Lean's signal is partial: many answers never formalize, and a failed proof may reflect an ill-typed statement or a missing library fact, not a wrong answer.\n\n**Key Findings:**\n\nOn MATH-500, the signal is sharply coverage-dependent, with the proof-winning answer being correct 96% of the time at high proved coverage but 20% at low, and sparse and often unfaithful: a 7B autoformalizer proves a class for only 28% of problems, and a manual audit finds only approximately 43% of those proofs faithful.\n\n**The Proposed Method:**\n\nThe authors propose COVCAL, a selector over Lean-trace diagnostics that certifies a finite-sample selective-risk bound on accepted answers or abstains, under two regimes (a conservative Bonferroni bound and a tighter dev-then-cal rule).\n\nThe contribution is described as a risk-controlled wrapper, using Qwen2.5-Math for generation and Qwen2.5-Coder for autoformalization.\n\nThe paper appears to have been published to arXiv very recently (2 days ago based on the metadata) with identifier 2605.28365."
    ],
    "durationSeconds": 7.679062904000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5fbd3d84-ad0a-44e7-b0fd-21362ae02f14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 60 · 2026-05-29T06:18:37.717Z_

<details><summary>Logged reasoning block</summary>

```text
Good, all three searches provide important validation:

1. **FIRMA** ✅ Confirmed. MathNLP 2025, ACL Anthology 2025.mathnlp-main.5. Has a "complexity router" for handling varying levels of mathematical sophistication. It's a workshop paper, not a main conference paper, but it does exist and has conceptual overlap with formalizability routing. 发掘 agent's suggestion to discuss it is valid.

2. **Risk-Controlled Lean-as-Judge** ✅ Confirmed! arXiv:2605.28365, published very recently (May 2026). 

The 7B autoformalizer achieves 43% faithfulness and 28% coverage on MATH-500, which matches the paper's reported numbers. The arXiv ID is now confirmed, so 补救 agent's concern about the missing identifier is resolved.

3. **GPQA-Diamond OOD for PRM** ✅ Confirmed. ThinkPRM uses GPQA-Diamond and LiveCodeBench for OOD evaluation, which is becoming standard practice. 补救 agent's suggestion is validated.

Now I'm assessing all the suggestions from the 发掘 agent's second round: The "always-try-Z3 + fallback" baseline is a critical gap in the ablations—the current list covers formal-only, neural-only, random routing, oracle routing, and threshold sweep, but misses this obvious "try-formal-first, fallback-to-neural" variant. Reframing the router's value as reducing false alarms rather than saving compute is also sharper. The conditional soundness point with roundtrip verification as a gatekeeper is the most important suggestion—adding this three-layer pipeline (router → roundtrip check → formal/neural) significantly strengthens the soundness claim and honestly addresses that only 13-22% of steps get true formal guarantees when 30-50% go to the formal branch with 43% faithfulness.

The four-level verification confidence hierarchy (roundtrip-verified Z3 → Z3-only → neural → uncertain) is a genuine conceptual contribution, though I should frame it as a contribution to the paper's structure rather than claiming it as a standalone empirical finding. FIRMA does exist at MathNLP 2025 with a complexity router, but it's a workshop paper focused on translation quality rather than verification routing, so it deserves a brief mention in related work. The point about context-dependent formalizability being non-trivial—why learned routing isn't just recycling 2015's ideas—is worth developing further.

Now looking at the remediation strategy: the three-tier approach for RRM data (confirm availability → self-annotate → use PRMBench as proxy) is concrete and actionable. The autoformalization component is the critical gap—I need to specify which model and include its compute costs. The label noise concern is valid too; the three failure modes and the proposed label quality evaluation plus clean-label ablation should be adopted. Still evaluating the OOD evaluation point... ation variant. **Partially adopt.**

**Defect 7 (Risk-Controlled arXiv ID)**: Confirmed as arXiv:2605.28365—straightforward correction. **Adopt.**

### Integration decisions:

The feedback from both reviewers actually points toward the same solutions in several places. The suggestion to add a "always-try-Z3 plus neural fallback" baseline directly addresses both the trivial alternative concern and the apples-to-oranges comparison issue. The soundness and gatekeeper ideas align with the label noise discussion—both are really about ensuring autoformalization reliability. And the verification confidence hierarchy ties together the compute concerns with the broader verification strategy.

The formal branch's complexity is more substantial than I initially presented it.

### Probability reassessment:

After incorporating these improvements, the novelty looks solid—the context-dependent routing with conditional soundness and roundtrip verification is genuinely novel, and FIRMA fills a gap in related work. Significance is medium-strong; the verification confidence hierarchy is a real conceptual contribution, though practical impact remains constrained by autoformalization coverage limits around 13-22% with formal guarantees. The honest treatment of these limitations actually strengthens the paper's credibility.

Idea ceiling: ~48-50%

**Experiment completeness after Round 2 improvements:**

The baseline suite is now comprehensive: pure neural, pure formal, and hybrid approaches including VERGE.

Adding more baselines and ablations...

Technical soundness sits at medium-strong. The probability range has tightened to 35-48% with a median around 42%, suggesting we're approaching convergence. Both agents identified legitimate improvements, though the 发掘 agent refined existing framing while the 补救 agent filled remaining experimental gaps like OOD evaluation and compute fairness.

The core framework feels solid now—semi-formal guarantees with conditional soundness and a verification confidence hierarchy—and the experimental design covers baselines, ablations, out-of-distribution cases, and fairness considerations. I'm leaning toward one final round since the three-layer pipeline and label noise handling are substantive enough to warrant a last review, though I expect only minor refinements after that.

Now I'm assembling the clean proposal, integrating all the adopted suggestions while keeping it tight. Let me pull together the reference checklist from both rounds to make sure nothing falls through the cracks. Continuing through the rest of the papers and models on my list, including ProcessBench, various PRM implementations like ThinkPRM and R-PRM, and recent work like FIRMA on mathematical reasoning verification.

Now I've got my 17 references compiled. Time to draft the proposal itself, though I need to be disciplined about scope—each sentence has to earn its place, no padding with background material, and the experiment design should stay in tight lists rather than sprawling prose. I'm aiming for precision over length.

For this round, I'm restructuring around three key ideas: a routing layer that decides which verification approach to use, roundtrip verification to check faithfulness, and then either formal or neural methods depending on what the router selects. I'll frame the soundness claim conditionally based on what gets verified, use the verification confidence hierarchy as an organizing principle rather than a separate contribution, and make sure to address why a naive try-and-fallback approach wouldn't work as well.

The contributions are shaping up as: sound miracle detection on the subset that's both formalizable and faithfully formalized, learned routing that predicts context-dependent formalizability non-trivially, and cost-aware design that balances different verification methods. I'm keeping the verification hierarchy as part of the framing rather than splitting it into its own contribution—it naturally flows from the pipeline structure.

Now I'm ready to start writing the actual proposal document with tight organization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d901981-bfe6-4044-86ee-7ffb7b6d50dc",
  "isSidechain": false,
  "requestId": "req_011CbWNY2FKdDjzbq8KJwRfr",
  "type": "assistant",
  "uuid": "2379b3d9-a83c-4713-8e05-e8315cb4e8ed",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gZeodYMz3cGymEChxT14e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 657,
      "cache_creation_input_tokens": 2241,
      "cache_read_input_tokens": 54584,
      "output_tokens": 3122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 657,
          "output_tokens": 3122,
          "cache_read_input_tokens": 54584,
          "cache_creation_input_tokens": 2241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2241
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

_source line 61 · 2026-05-29T06:18:37.723Z_

Good — now let me verify one more thing the 补救 agent flagged about autoformalization faithfulness data:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2379b3d9-a83c-4713-8e05-e8315cb4e8ed",
  "isSidechain": false,
  "requestId": "req_011CbWNY2FKdDjzbq8KJwRfr",
  "type": "assistant",
  "uuid": "8c179819-e96e-4032-9bd7-ad7ea7aae691",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gZeodYMz3cGymEChxT14e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 657,
      "cache_creation_input_tokens": 2241,
      "cache_read_input_tokens": 54584,
      "output_tokens": 3122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 657,
          "output_tokens": 3122,
          "cache_read_input_tokens": 54584,
          "cache_creation_input_tokens": 2241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2241
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

_source line 62 · 2026-05-29T06:18:37.724Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SdGLhJSHSQKU9aBiLBGLYP`</summary>

```json
{
  "query": "\"Do LLMs Game Formalization\" autoformalization faithfulness evaluation arXiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c179819-e96e-4032-9bd7-ad7ea7aae691",
  "isSidechain": false,
  "requestId": "req_011CbWNY2FKdDjzbq8KJwRfr",
  "type": "assistant",
  "uuid": "a4f167e6-9c24-4e3f-a430-974bd1872ddf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gZeodYMz3cGymEChxT14e",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 657,
      "cache_creation_input_tokens": 2241,
      "cache_read_input_tokens": 54584,
      "output_tokens": 3122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2241,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 657,
          "output_tokens": 3122,
          "cache_read_input_tokens": 54584,
          "cache_creation_input_tokens": 2241,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2241
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

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to make an informed evaluation. Let me synthesize my findings.  ---  【状态】: 有…",
  "leafUuid": "a4f167e6-9c24-4e3f-a430-974bd1872ddf",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Tool result

_source line 65 · 2026-05-29T06:18:47.554Z_

<details><summary>↩ Tool result · `toolu_01SdGLhJSHSQKU9aBiLBGLYP`</summary>

```text
Web search results for query: ""Do LLMs Game Formalization" autoformalization faithfulness evaluation arXiv 2604"

Links: [{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"Can Large Language Models Autoformalize Kinematics?","url":"https://arxiv.org/pdf/2509.21840"},{"title":"Autoformalization of Game Descriptions using Large Language Models","url":"https://arxiv.org/pdf/2409.12300"},{"title":"Autoformalization of Game Descriptions using Large Language Models","url":"https://arxiv.org/html/2409.12300"},{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"},{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/html/2511.12784"},{"title":"Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/html/2604.25031"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"

**arXiv:** 2604.19459 (uploaded April 21, 2026)

**Authors:** Kyuhee Kim and 2 other authors

**Summary:**

The paper investigates whether large language models exploit a gap between proof validity and formalization faithfulness when generating Lean 4 proofs. The researchers evaluated GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.

Despite compilation rates of 87-99%, they found no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it. However, the two-stage pipeline revealed two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.

The paper includes code and data available on GitHub, as noted in the paper's abstract.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4f167e6-9c24-4e3f-a430-974bd1872ddf",
  "isSidechain": false,
  "promptId": "381e9bf1-a558-40a2-a586-041a6e2d16a9",
  "type": "user",
  "uuid": "0d605414-0c50-429a-b9ab-1e38dd6b446e",
  "toolUseResult": {
    "query": "\"Do LLMs Game Formalization\" autoformalization faithfulness evaluation arXiv 2604",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K9iGpHrM5CArRdeZNuX4fu",
        "content": [
          {
            "title": "[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/abs/2604.19459"
          },
          {
            "title": "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/html/2604.19459"
          },
          {
            "title": "Can Large Language Models Autoformalize Kinematics?",
            "url": "https://arxiv.org/pdf/2509.21840"
          },
          {
            "title": "Autoformalization of Game Descriptions using Large Language Models",
            "url": "https://arxiv.org/pdf/2409.12300"
          },
          {
            "title": "Autoformalization of Game Descriptions using Large Language Models",
            "url": "https://arxiv.org/html/2409.12300"
          },
          {
            "title": "Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing",
            "url": "https://arxiv.org/pdf/2511.12784"
          },
          {
            "title": "Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing",
            "url": "https://arxiv.org/html/2511.12784"
          },
          {
            "title": "Faithful Autoformalization via Roundtrip Verification and Repair",
            "url": "https://arxiv.org/html/2604.25031"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Paper:** \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning\"\n\n**arXiv:** 2604.19459 (uploaded April 21, 2026)\n\n**Authors:** Kyuhee Kim and 2 other authors\n\n**Summary:**\n\nThe paper investigates whether large language models exploit a gap between proof validity and formalization faithfulness when generating Lean 4 proofs. The researchers evaluated GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.\n\nDespite compilation rates of 87-99%, they found no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it. However, the two-stage pipeline revealed two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.\n\nThe paper includes code and data available on GitHub, as noted in the paper's abstract."
    ],
    "durationSeconds": 9.818900813,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a4f167e6-9c24-4e3f-a430-974bd1872ddf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-29T06:18:55.218Z_

<details><summary>Logged reasoning block</summary>

```text
This confirms the paper exists and provides relevant data about autoformalization faithfulness issues. The key finding is that even with 87-99% compilation rates, there are unfaithfulness issues (axiom fabrication, premise mistranslation). This supports the need for roundtrip verification as a gatekeeper.

Now I have all the information I need. Let me write the full Round 2 integration output.

Let me be very careful about:
1. All references preserved and new ones added
2. Proposal kept concise
3. Clean proposal block with no meta-information
4. Proper format


5. Now drafting the complete response...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d605414-0c50-429a-b9ab-1e38dd6b446e",
  "isSidechain": false,
  "requestId": "req_011CbWNf2GWDVu5xoJeKE1ji",
  "type": "assistant",
  "uuid": "401f1b83-6a13-4a9e-b934-b789ca56a88a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Efv3VKXjbggiwupraaQpKk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4447,
      "cache_read_input_tokens": 56825,
      "output_tokens": 7214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7214,
          "cache_read_input_tokens": 56825,
          "cache_creation_input_tokens": 4447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4447
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

_source line 67 · 2026-05-29T06:21:39.173Z_

All cross-validation complete. Now let me compile the full Round 2 integration.

【阶段】: 迭代第 2 轮

【交叉验证调研】:
1. **FIRMA (MathNLP 2025) 是否存在且有 complexity router**（发掘 point 4）→ 已验证 ✅。ACL Anthology 2025.mathnlp-main.5 确认，包含 complexity router 用于 formal-informal 翻译质量路由。与本 proposal 有概念层面的表面相似性但目标函数不同（翻译质量 vs. 验证正确性）。应在 related work 中讨论以防审稿人质疑。
2. **Risk-Controlled Lean-as-Judge arXiv ID**（补救 defect 7）→ 已验证 ✅。arXiv:2605.28365，2026 年 5 月发表。关键数据确认：7B autoformalizer 在 MATH-500 上仅 28% coverage，手动审计仅 ~43% 证明 faithful，但 proved answer 正确率高达 96%。数据来源可靠，可完整引用。
3. **GPQA-Diamond 作为 PRM OOD 评测是否标准**（补救 defect 4）→ 已验证 ✅。ThinkPRM 在 GPQA-Diamond 上做 OOD 评测，超 discriminative PRM 8%。确认为合适的 OOD benchmark。
4. **Do LLMs Game Formalization? faithfulness 数据**（补救 defect 7 补充引用）→ 已验证 ✅。arXiv:2604.19459，评估 GPT-5/DeepSeek-R1 在 Lean 4 证明中的 faithfulness。关键发现：编译率 87-99% 但存在 axiom fabrication 和 premise mistranslation 两种 unfaithfulness 模式。支持 roundtrip verification 作为 gatekeeper 的必要性。

【发掘 agent 有效建议采纳】:
- **Point 1（trivial alternative "always-try-Z3 + fallback" 需显式 ablation）**: 已验证（LogicReward 正是此策略），采纳。在 ablation 中新增 "try-formal-first + neural fallback" 作为第 6 个 baseline。同时采纳 reframing：router 核心价值 = 减少 formal branch 对 non-formalizable 步骤的系统性假阳性（FoVer documented overly-strict behavior），而非仅节省计算。
- **Point 2（conditional soundness + roundtrip verification gatekeeper）**: 采纳，这是本轮最重要的改进。Soundness claim 精确限定为 "conditional on faithful autoformalization"；增加 roundtrip verification（arXiv:2604.25031）作为 gatekeeper——pipeline 从两层变为三层（router → roundtrip check → formal/neural）。Risk-Controlled (arXiv:2605.28365) 的 43% faithfulness 数据和 Do LLMs Game Formalization (arXiv:2604.19459) 的 unfaithfulness 模式分析均已验证，支撑此设计。
- **Point 3（verification confidence hierarchy）**: 部分采纳。四级置信度体系（roundtrip-verified Z3 > Z3-only > neural > uncertain）作为 framing 整合进方法论，但不作为独立 contribution 声称——缺少实验验证其校准质量。标注：合理推断，作为 framing 纳入。
- **Point 4（FIRMA related work）**: 已验证，采纳。在 related work 中简要讨论 FIRMA 的 complexity router 并明确差异化（翻译质量 vs. 验证正确性）。
- **Point 5（context-dependent formalizability 的 non-triviality 论证）**: 采纳。展开三个 context dependencies：predecessor formal context、autoformalization capability boundary、proof position effect。强化 "为什么 rule-based 不够" 的论证深度。

【补救 agent 有效建议采纳】:
- **Defect 1（RRM 数据可用性）**: 采纳三层保障策略。升级 PRMBench error type breakdown 为 primary evaluation if RRM data unavailable。增加自建 200-300 example human annotation 选项。
- **Defect 2（autoformalization compute 未纳入）**: 采纳。明确 autoformalization 使用 Qwen2.5-Math-72B-Instruct（或同级 API model）。将 autoformalization 开销纳入 Pareto 曲线。
- **Defect 3（router label noise）**: 采纳。增加 label quality audit（抽样 200-300 non-formalizable labels 人工验证）+ clean-label router ablation。明确 label 构建 pipeline 三分类。
- **Defect 4（OOD 评测）**: 已验证，采纳。增加 GPQA-Diamond 作为 OOD benchmark，报告 OOD 下 router behavior。
- **Defect 5（LogicReward 对比方式）**: 采纳。明确 LogicReward 作为 conceptual comparison（方法论层面），quantitative 对比中标注不同性质。新增 "naive hybrid"（FoVer Z3 + try-and-fallback to GenPRM）作为更直接的 baseline——与发掘 Point 1 convergent。
- **Defect 6（neural branch ablation）**: 部分采纳。增加 design rationale 讨论，明确 ARES-style calibration 的实现方式（Platt scaling on held-out set），但不增加完整的 neural branch swap ablation 以避免 scope creep。标注：合理但优先级低于核心 ablation。
- **Defect 7（Risk-Controlled arXiv ID）**: 已验证，采纳。补全 arXiv:2605.28365。

【本轮 proposal 主要变更】:

**Idea 层面变更:**
- Soundness claim 精确限定为 "conditional on faithful autoformalization"，增加 roundtrip verification gatekeeper（三层 pipeline）
- Router 核心价值 reframing：从 "节省计算" 到 "减少 formal branch 假阳性"
- 新增 verification confidence hierarchy 作为方法论 framing（四级置信度）
- 新增 FIRMA (MathNLP 2025) 的 related work 差异化讨论
- 展开 context-dependent formalizability 的 non-triviality 论证
- 新增 Do LLMs Game Formalization (arXiv:2604.19459) 引用

**实验层面变更:**
- Ablation 新增 "try-formal-first + neural fallback" baseline
- Ablation 新增 router label noise analysis（label quality audit + clean-label ablation）
- 明确 autoformalization 模型 = Qwen2.5-Math-72B-Instruct，纳入 compute Pareto 曲线
- 新增 GPQA-Diamond OOD evaluation
- Miracle step evaluation 三层保障策略
- LogicReward 对比方式明确化
- 明确 ARES-style calibration = Platt scaling

【idea 质量评估】: Novelty=强（learned context-dependent formalizability routing 无先例；三层 pipeline 含 roundtrip gatekeeper 是新设计；与 VERGE/LogicReward/FIRMA 均有 crisp 差异化） Significance=中-强（conditional soundness guarantee 诚实且有深度；实际 coverage 受限于 autoformalization faithfulness ~43% 但诚实报告本身增加 credibility） → idea 天花板约 50%

【实验完备性评估】: Technical Soundness=中-强（baseline 完整含 naive hybrid、ablation 覆盖 routing + label noise + threshold、OOD 评测、compute fairness 含 autoformalization、miracle step 三层保障；主要残余风险：autoformalization model 的实际性能和 router 在 OOD 上的 degradation 程度） → 地板约 35%

【当前概率估计】: [35% - 48%] 中位 42%

【决策】: 继续

【决策理由】: 本轮改动幅度中等（三层 pipeline 是实质性架构变化，trivial alternative ablation + OOD evaluation + label noise analysis 是重要实验补充），proposal 质量显著提升。但以下原因支持再做一轮：(1) 三层 pipeline（router → roundtrip → formal/neural）是本轮引入的新架构，worker 尚未评审此版本；(2) conditional soundness claim 和 verification confidence hierarchy 的 framing 需要检验是否过度 claim；(3) 预期第 3 轮变化幅度将显著缩小，大概率收敛。

**引用核对清单（重写前逐条确认）：**
1. FoVer (ACL 2026, arXiv:2505.15960) ✅
2. GenPRM (AAAI 2026, arXiv:2504.00891) ✅
3. LogicReward (ICLR 2026, arXiv:2512.18196) ✅
4. VERGE (arXiv 2026, arXiv:2601.20055) ✅
5. RRM / Curing Miracle Steps (arXiv 2025, arXiv:2510.07774) ✅
6. Risk-Controlled Lean-as-Judge (arXiv 2026, arXiv:2605.28365) ✅ — arXiv ID 已补全
7. ARES (2025) ✅
8. PRMBench (ACL 2025, arXiv:2501.03124) ✅
9. ProcessBench ✅
10. Qwen3-8B, GenPRM-7B, Qwen2.5-Math-PRM-72B, Qwen2.5-Math-7B-Instruct ✅
11. Z3, Isabelle ✅
12. PRoSFI (arXiv:2603.29500) ✅
13. Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031) ✅
14. ThinkPRM (arXiv:2504.16828) ✅
15. R-PRM (EMNLP 2025, arXiv:2503.21295) ✅
16. FIRMA (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5) ✅ — 新增
17. Do LLMs Game Formalization? (arXiv:2604.19459) ✅ — 新增

全部 17 条已确认包含于下方纯净版。

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
# Formally-Routed Process Reward Models for Sound Miracle Step Detection

## Core Problem

No existing PRM exploits the formalizability structure of reasoning steps. Formal-only PRMs (FoVer, PRoSFI) provide high precision but suffer documented overly-strict behavior on informal steps. Neural-only PRMs (GenPRM, ThinkPRM, R-PRM, ARES) provide broad coverage but no formal derivability guarantees. Hybrid systems use either hand-crafted routing (VERGE) or unlearned try-and-fallback (LogicReward). The critical gap: a learned, context-dependent formalizability router that dispatches each step to the appropriate verifier—with roundtrip-verified formal checking providing sound miracle step detection on formalizable steps while neural verification covers the rest.

## Research Opportunity

Three converging gaps create a unique opening:

(1) VERGE (arXiv:2601.20055) demonstrates 18.7% uplift from routing between Z3 and neural verifiers but uses rule-based routing over static claim types (logical vs. commonsense)—context-free and not learned. The paper explicitly identifies learned routing as the open next step.

(2) LogicReward (ICLR 2026, arXiv:2512.18196) implements Isabelle step verification with token-probability fallback—a "try-formal-first" strategy. This cannot distinguish "step is intrinsically non-formalizable" from "autoformalization failed on a formalizable step," producing systematic false alarms on non-formalizable steps (the same overly-strict behavior documented in FoVer).

(3) RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, but never tested formal derivability from predecessors. FoVer's public codebase (arXiv:2505.15960), GenPRM's open weights (arXiv:2504.00891), and Risk-Controlled Lean-as-Judge (arXiv:2605.28365) with its honest quantification of autoformalization limits (43% faithfulness, 28% coverage for 7B autoformalizer on MATH-500) provide infrastructure and calibration data for a hybrid system at academic compute budgets.

## Key Insight: Conditional Formal Soundness for Miracle Detection

A miracle step is an unjustified logical leap—step S_i that does not follow from predecessors {S_1,...,S_{i-1}}. When a step is faithfully formalized and submitted to Z3 for predecessor-derivability checking, miracle steps produce Z3 UNSAT (not derivable). This is near-definitional: on the faithfully-formalized subset, miracle step detection reduces to Z3 derivability failure.

The critical qualifier is "faithfully formalized." Autoformalization is unreliable: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) reports only 43% faithfulness, and Do LLMs Game Formalization? (arXiv:2604.19459) identifies two unfaithfulness modes—axiom fabrication and premise mistranslation—that evade compilation-based detection. Therefore, the soundness guarantee is conditional: it holds only for steps that pass both formalizability routing AND roundtrip verification of autoformalization faithfulness (arXiv:2604.25031).

FormalRoute-PRM makes this conditionality explicit and operationalizable through a three-layer pipeline: learned formalizability routing → roundtrip faithfulness verification → formal or neural verification.

## Contributions

1. **Conditional sound miracle detection.** On steps that the router identifies as formalizable AND that pass roundtrip faithfulness verification, Z3 predecessor-derivability checking provides guaranteed miracle step detection. This is the first PRM offering formal soundness guarantees for any subset of reasoning steps, with honest coverage reporting following Risk-Controlled methodology.

2. **Learned context-dependent formalizability routing.** Unlike VERGE's static claim-type routing (context-free) and LogicReward's unlearned try-and-fallback, our Qwen3-8B router predicts formalizability conditioned on the full predecessor chain {S_1,...,S_{i-1}}. Context-dependent formalizability prediction is a non-trivial learning problem because a step's formalizability depends on: (a) the formal context established by predecessors (which definitions and variables are already formalized), (b) the autoformalization tool's capability boundary for this step type, and (c) the step's position in the proof (early declarative steps are more formalizable than later heuristic steps). Rule-based approaches cannot capture these context dependencies. Compared to try-and-fallback, learned routing provides three advantages: (i) avoids systematic false alarms from formal verification on non-formalizable steps (FoVer's documented overly-strict behavior), (ii) produces per-step verification confidence signals distinguishing formally guaranteed vs. neurally estimated scores, and (iii) distinguishes intrinsic step formalizability from extrinsic autoformalization capability.

3. **Asymmetric cost-aware routing threshold.** Router errors have asymmetric costs: routing non-formalizable steps to Z3 produces false alarms (overly strict); routing formalizable steps to neural verification risks missing miracle steps. The router threshold is optimized to favor recall (prefer sending to Z3), with explicit cost-asymmetry analysis. This design is informed by FoVer's documented overly-strict behavior and Risk-Controlled Lean-as-Judge's faithfulness quantification.

## Research Landscape

**Formal-only PRMs.** FoVer (ACL 2026, arXiv:2505.15960) achieves 85.8 AUROC on ProcessBench via Z3/Isabelle-verified training labels, but produces overly-strict scores on informal reasoning steps. PRoSFI (arXiv:2603.29500) generates structured formal intermediaries for prover verification on the generation side.

**Neural PRMs.** GenPRM (AAAI 2026, arXiv:2504.00891): 7B surpasses Qwen2.5-Math-PRM-72B on ProcessBench via generative CoT and code verification. ThinkPRM (arXiv:2504.16828): 14B trained on only 8K process labels outperforms discriminative PRMs trained on 100× more data; establishes token-budget-normalized comparison paradigm (+7.2% over LLM-as-Judge at same budget). R-PRM (EMNLP 2025, arXiv:2503.21295): +13.9 F1 on ProcessBench and +8.5 F1 on PRMBench via three-stage cold-start, DPO, inference-time scaling. ARES (2025): 72.1% Macro-F1 on PRMBench via autoregressive entailment, entirely dependent on LLM calibration.

**Hybrid systems.** VERGE (arXiv:2601.20055): rule-based semantic routing (logical vs. commonsense claim types) to Z3 or LLM ensemble, 18.7% uplift—routing is static, context-free, not learned. LogicReward (ICLR 2026, arXiv:2512.18196): Isabelle step verification with token-probability fallback; 8B model surpasses GPT-4o by 11.6% on logical reasoning but is an RL training framework, not a standalone PRM. FIRMA (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5): bidirectional formal-informal mathematical language alignment with a complexity router—but this routes for translation quality, not verification correctness; the target function and training signal are fundamentally different from formalizability routing for verification.

**Miracle step detection.** RRM (arXiv:2510.07774, withdrawn from ICLR 2026) defines the miracle step taxonomy and reduces miracle steps by 71% via rubric rewards, without formal derivability checking.

**Autoformalization limits.** Risk-Controlled Lean-as-Judge (arXiv:2605.28365): 43% faithfulness, 28% coverage for 7B autoformalizer. Do LLMs Game Formalization? (arXiv:2604.19459): identifies axiom fabrication and premise mistranslation as unfaithfulness modes evading compilation checks. Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031): provides roundtrip verification methodology for detecting unfaithful formalizations.

## Proposed Approach

**Three-layer pipeline:**

**Layer 1: Formalizability Router.** Qwen3-8B classifier trained on FoVer Z3 verification labels + autoformalization success signals. Labels defined as: formalizable = Z3 compilation success AND roundtrip semantic verification pass; non-formalizable = autoformalization failure OR roundtrip failure OR Z3 timeout. Input: step S_i + predecessor context {S_1,...,S_{i-1}}. Output: formalizability probability. Threshold set via asymmetric cost-aware optimization favoring recall.

**Layer 2: Roundtrip Faithfulness Verification.** Steps routed to formal branch undergo autoformalization (via Qwen2.5-Math-72B-Instruct) → roundtrip verification (arXiv:2604.25031): back-translate the formal statement to natural language and check semantic equivalence with the original step. Steps failing roundtrip verification are redirected to neural branch. This layer gates the soundness guarantee.

**Layer 3: Verification.**
- Formal branch (roundtrip-verified): Z3 predecessor-derivability checking. Z3 UNSAT → miracle step detected (sound). Z3 SAT → step verified with formal guarantee.
- Neural branch (non-formalizable or roundtrip-failed): GenPRM-7B scoring with ARES-style calibrated entailment (Platt scaling on held-out validation set). Best-effort verification without formal guarantees.

**Output.** Per-step score with verification confidence tier: (a) roundtrip-verified + Z3-verified (highest confidence), (b) roundtrip-failed but router-formalizable (medium—formal attempt inconclusive), (c) router-non-formalizable + neurally scored (neural confidence), (d) router uncertain (lowest confidence).

## Evaluation Design

**Benchmarks and metrics.**
- ProcessBench: F1 (aligned with GenPRM, R-PRM) + AUROC (aligned with FoVer)
- PRMBench (ACL 2025, arXiv:2501.03124): PRMScore + error-type breakdown
- Best-of-N reranking: MATH-500, AIME24 using Qwen2.5-Math-7B-Instruct as generator; report Pass@1, majority voting, PRM reranking (N=8,16,64)
- OOD generalization: GPQA-Diamond (scientific reasoning, following ThinkPRM)
- Miracle step detection: precision/recall/F1 on (a) RRM miracle taxonomy annotations (Yuan et al., 2025) if publicly available, (b) PRMBench error-type categories as primary proxy if RRM data unavailable, (c) self-constructed human-annotated set (200–300 steps, 2–3 annotators, inter-annotator agreement via Cohen's kappa)

**Baseline matrix.**
- Pure neural: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B
- Pure formal: FoVer-7B
- Hybrid: VERGE (hand-crafted routing), Naive Hybrid (FoVer Z3 try-and-fallback to GenPRM, no learned router)
- LLM-as-Judge: GPT-4o, QwQ-32B
- Compute-matched: GenPRM majority voting under equivalent total token budget (including autoformalization cost)
- LogicReward (ICLR 2026): conceptual comparison on method design; quantitative comparison where applicable with methodology differences noted (RL framework vs. standalone PRM)

**Ablation studies.**
1. Formal-only: all steps → Z3 (low coverage penalty)
2. Neural-only: all steps → GenPRM (miracle step leakage)
3. Random routing: 50/50 formal/neural (isolates routing from ensemble)
4. Oracle routing: ground-truth formalizability labels (performance ceiling)
5. Router threshold sweep: coverage-accuracy trade-off across formalizability thresholds, visualizing asymmetric cost impact
6. Try-formal-first + neural fallback: no router, attempt Z3 on all steps, fallback on failure (trivial alternative baseline—directly tests whether learned routing outperforms unlearned try-and-fallback)
7. Router label noise analysis: compare router trained on noisy auto-labels vs. router trained on human-cleaned labels (500–1000 examples); report label precision via human audit of 200–300 "non-formalizable" training labels

**Compute fairness.** Report per-step average inference time and total FLOPs for all systems, explicitly including autoformalization cost (Qwen2.5-Math-72B-Instruct inference) in FormalRoute-PRM's compute. Plot accuracy vs. compute Pareto curve. Compute-matched GenPRM majority voting as explicit comparison following ThinkPRM's token-budget-normalized paradigm.

**Router analysis.** Classification accuracy, precision, recall on in-domain (formal reasoning) and out-of-domain (general math, GPQA-Diamond) splits. Few-shot domain adaptation ablation with ProcessBench/PRMBench samples. Oracle formalizability labels (human-annotated, 100–200 examples) to quantify router quality ceiling. Formalizability positive rate, formal branch coverage, roundtrip verification pass rate per benchmark.

**Honest coverage reporting.** Following Risk-Controlled Lean-as-Judge (arXiv:2605.28365) methodology: report autoformalization coverage, roundtrip faithfulness rate, formal branch activation rate, and effective soundness coverage (= steps receiving formal guarantee / total steps) per benchmark.

## Compute Budget

- Router training: Qwen3-8B LoRA fine-tuning on ~80K FoVer-derived labels, ≈4–8 GPU-hours on single H100
- Autoformalization: Qwen2.5-Math-72B-Instruct inference for formalizable steps (est. 30–50% of total); dominant compute cost
- Z3 solving: millisecond-scale per formula, negligible
- GenPRM-7B inference: standard 7B inference for neural branch steps
- Roundtrip verification: one additional LLM call per formal-branch step for back-translation + semantic equivalence check
- Total: training <1 day, full evaluation pipeline <5 days on single-node 8×H100 (dominated by autoformalization inference)

## Key References

- FoVer: PRM Data Synthesis via Formal Verification (ACL 2026, arXiv:2505.15960)
- GenPRM: Scaling Test-Time Compute of PRMs (AAAI 2026, arXiv:2504.00891)
- LogicReward: Step-Wise Logical Supervision (ICLR 2026, arXiv:2512.18196)
- VERGE: Formal Refinement and Guidance Engine (arXiv 2026, arXiv:2601.20055)
- Curing Miracle Steps with Rubric Rewards (arXiv 2025, arXiv:2510.07774)
- Risk-Controlled Lean-as-Judge (arXiv 2026, arXiv:2605.28365)
- ARES: Autoregressive Entailment Scoring (2025)
- ThinkPRM: Process Reward Models That Think (arXiv:2504.16828)
- R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, arXiv:2503.21295)
- PRMBench: Fine-grained PRM Benchmark (ACL 2025, arXiv:2501.03124)
- PRoSFI: Structured Formal Intermediaries (arXiv:2603.29500)
- Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031)
- FIRMA: Formal-Informal Mathematical Language Alignment (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5)
- Do LLMs Game Formalization? (arXiv:2604.19459)
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "401f1b83-6a13-4a9e-b934-b789ca56a88a",
  "isSidechain": false,
  "requestId": "req_011CbWNf2GWDVu5xoJeKE1ji",
  "type": "assistant",
  "uuid": "15273721-d625-47db-9fb2-42df4d38f6f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Efv3VKXjbggiwupraaQpKk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4447,
      "cache_read_input_tokens": 56825,
      "output_tokens": 7214,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4447,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7214,
          "cache_read_input_tokens": 56825,
          "cache_creation_input_tokens": 4447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4447
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

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to make an informed evaluation. Let me synthesize my findings.  ---  【状态】: 有…",
  "leafUuid": "15273721-d625-47db-9fb2-42df4d38f6f7",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 71 · 2026-05-29T06:27:21.022Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:27:21.022Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "content": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have sufficient research to provide a thorough assessment. Let me synthesize my findings.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- **Risk-Controlled Lean-as-Judge (arXiv:2605.28365, May 2026)**: Reports 28% problem coverage and only 43% proof faithfulness for a 7B autoformalizer on MATH-500. Proposes COVCAL for risk-controlled selective verification. This paper is the most critical calibration reference — it quantifies exactly how thin the \"formal guarantee\" layer can be in practice.\n- **FoVer (arXiv:2505.15960, ACL 2026 Findings)**: Uses Z3/Isabelle to synthesize PRM training labels. Generalizes well across 12 benchmarks including non-formal tasks. The \"overly strict\" claim from the proposal needs to be verified against FoVer's actual reporting — FoVer frames its limitation as limited formal coverage, not necessarily false alarms on informal steps.\n- **VERGE (arXiv:2601.20055)**: Rule-based semantic routing (logical vs. commonsense claims) to Z3 or LLM ensemble. 18.7% uplift. Explicitly identifies \"learned routing\" as future work. Validates the routing-matters hypothesis.\n- **LogicReward (arXiv:2512.18196, ICLR 2026)**: Isabelle-based step verification with fallback. Primarily an RL training framework. Its \"try-formal-first\" approach is indeed the natural baseline for the routing idea.\n- **FIRMA (MathNLP 2025)**: Complexity-aware routing for formal-informal translation. Has a complexity router, but targets translation quality, not verification correctness. The proposal correctly differentiates, but FIRMA's router architecture and training methodology may provide useful technical parallels.\n- **RRM (arXiv:2510.07774)**: Defines miracle step taxonomy. Reduces miracle steps 71% via rubric rewards. Never attempts formal derivability checking. Withdrawn from ICLR 2026, which may affect its credibility as a foundation for the miracle step concept.\n- **Autoformalization landscape (StepFun-Formalizer, FormaRL, etc.)**: Autoformalization is improving rapidly (130k lines of topology in 2 weeks at ~$100 cost), but step-level faithfulness remains a major bottleneck. No prior work explicitly frames \"formalizability\" as a learnable, context-dependent property for verification routing.\n- 调研总结: 领域当前在两个轴上推进——(1) 提升 autoformalization 的覆盖率和忠实度 (Risk-Controlled, roundtrip verification, StepFun)，(2) 构建更强的 neural PRM (GenPRM, ThinkPRM, R-PRM)。将两者通过学习路由桥接的工作尚无人做，但核心瓶颈在于 autoformalization 的有效覆盖率可能太低，导致形式化分支的实际价值存疑。\n\n---\n\n【发掘点 1】\n- 维度: significance 提升\n- 内容: **有效形式化覆盖率是 significance 的生死线，proposal 必须正面回应而非仅\"honest reporting\"。** 根据 Risk-Controlled Lean-as-Judge 的数据，7B autoformalizer 在 MATH-500 上 28% coverage × 43% faithfulness ≈ 12% 有效覆盖。即使用 72B autoformalizer 并假设覆盖率翻倍、忠实度提升到 60%，有效覆盖也仅约 56% × 60% ≈ 34%，再乘以 router 准确率（假设 85%），最终约 29% 的 steps 获得形式化保证。一个对 ~29% steps 提供 soundness guarantee、其余 ~71% 只有 neural scoring 的 PRM，审稿人会问：这比 pure neural PRM 好多少？当前 proposal 的策略是\"honest coverage reporting\"，但这是防守姿态。更有力的 framing 应该是：**argue that formal coverage is disproportionately concentrated on the steps where it matters most**——即 miracle steps 往往发生在明确的逻辑推导环节（代数变换、方程求解、不等式推导），而这些恰好是 autoformalization 最擅长处理的 step 类型。如果能论证\"形式化覆盖率虽低，但精准覆盖了 miracle step 高发区\"，significance 会大幅提升。建议在 proposal 中增加一个分析维度：formal branch coverage 与 miracle step occurrence 的相关性假设及预实验验证计划。\n- 价值: 直接决定审稿人是否认为这个 conditional soundness guarantee 在实践中有意义（Significance 维度）。一个\"覆盖 12% 但精准命中高风险 steps\"的故事远比\"覆盖 12%，剩下全靠 neural\"有说服力。\n- 调研依据: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 提供的 43% faithfulness / 28% coverage 数据，以及 RRM (arXiv:2510.07774) 对 miracle step 发生场景的分析（miracle steps 集中在明确的推理跳跃环节）。\n\n【发掘点 2】\n- 维度: novelty 锐化\n- 内容: **\"条件性 soundness\"的 framing 有被审稿人视为 tautological 的风险，需要重新定位 novelty 的核心承载点。** 当前 Contribution 1 说\"on steps that pass routing AND roundtrip verification, Z3 provides guaranteed miracle detection\"——一个严格的审稿人可能反应为\"if you can formally verify a step, of course you know whether it's correct; the hard part is getting there reliably, not the guarantee itself.\" 真正的 novelty 不是\"形式验证是 sound 的\"（这是 Z3 的固有属性），而是：**构建了一个实用系统，能可靠地识别哪些 steps 可以信赖地送入形式验证管道，并通过 roundtrip verification 确保 formalization 的忠实度**。建议将 Contribution 1 的叙事从\"we provide formal soundness guarantees\"转向\"we solve the practical problem of reliably routing steps to the right verifier, making conditional formal soundness achievable at scale for the first time\"。这样 novelty 的重心从 Z3（已知）转移到 routing + roundtrip gating pipeline（新的）。\n- 价值: 防止审稿人将核心贡献归因于 Z3 的已有能力而非本文的系统设计（Novelty 维度）。\n- 调研依据: FoVer 已经使用 Z3 做 step-level verification；VERGE 已经做了 Z3 routing；本文的真正增量在 routing 的学习化和 roundtrip gating，而非 Z3 验证本身。\n\n【发掘点 3】\n- 维度: trivial alternative 威胁\n- 内容: **Ablation #6（try-formal-first + neural fallback）是最严重的 trivial alternative 威胁，当前 proposal 对其的回应不够有力。** Proposal 列出三个 learned routing 的优势：(i) 避免 false alarms, (ii) 提供 per-step confidence tier, (iii) 区分 intrinsic formalizability vs extrinsic autoformalization capability。但 (ii) 是 output format 设计，不依赖 learned routing；(iii) 在概念上有趣但不清楚如何在实验中验证。唯一的硬优势是 (i)——避免 non-formalizable steps 被送入 formal pipeline 后产生 false alarms。但如果 Layer 2（roundtrip verification）已经能过滤掉大部分 unfaithful formalizations，那 try-and-fallback + roundtrip verification 可能也能避免大部分 false alarms，只是多花了 autoformalization 的 compute。**建议明确回答：在有 roundtrip verification 作为安全网的情况下，learned router 相比 try-and-fallback 的增量到底在哪里？** 可能的强答案是：(a) roundtrip verification 并非完美——Do LLMs Game Formalization (arXiv:2604.19459) 指出 axiom fabrication 和 premise mistranslation 可以逃过 compilation 检查，也可能逃过 roundtrip verification；learned router 作为第一道防线可以在这些情况下避免错误。(b) compute savings：避免对 ~50-70% non-formalizable steps 做 72B 模型 autoformalization 推理，这是非平凡的 cost reduction。需要在 proposal 中将这两点论证做实。\n- 价值: 如果审稿人认为 try-and-fallback 就够了，整个 learned routing 贡献就被消解（Novelty 维度核心威胁）。\n- 调研依据: Do LLMs Game Formalization (arXiv:2604.19459) 关于 unfaithfulness 逃过 compilation 检查的发现；LogicReward (arXiv:2512.18196) 的 try-formal-first 设计作为直接 baseline。\n\n【发掘点 4】\n- 维度: 前提假设质疑\n- 内容: **\"Formalizability\"作为步骤的内禀属性的假设需要更严谨的论证。** 当前 proposal 将 formalizability label 定义为 \"Z3 compilation success AND roundtrip semantic verification pass\"——这意味着 formalizability 是相对于特定 autoformalizer（Qwen2.5-Math-72B-Instruct）和特定 formal system（Z3 的 SMT-LIB 片段）的操作性定义，而非步骤的内禀语义属性。随着 autoformalizer 能力提升（2025-2026 autoformalization 进展迅速，如 130k lines of topology in two weeks），今天\"non-formalizable\"的步骤明天可能变成 formalizable。这产生两个问题：(a) router 的训练标签有时效性，模型可能学到的是当前 autoformalizer 的能力边界而非步骤的内禀属性；(b) 审稿人可能质疑\"formalizability\"概念的稳定性。**建议在 proposal 中明确区分两个层面：intrinsic formalizability（步骤在原则上是否可以用一阶逻辑/SMT 表达）和 operational formalizability（给定当前 autoformalization 工具链，步骤是否能被可靠地形式化）。Router 学习的是后者，但 contribution 的价值论证应该建立在前者之上——因为 intrinsically formalizable 的步骤恰好是 miracle step 最不应该出现、出现后最值得被形式化检测的地方。** 这个区分不仅让概念更严谨，还能回应\"autoformalizer 变好了 router 就没用了\"的质疑：即使 autoformalizer 完美了，routing 仍然有价值，因为 intrinsically non-formalizable 的步骤（如直觉判断、heuristic arguments）送入形式验证仍然会产生无意义结果。\n- 价值: 概念基础的严谨性直接影响审稿人对整个技术方案的信任度（Novelty + Significance 维度）。\n- 调研依据: Autoformalization 快速进展（130k lines of topology, StepFun-Formalizer 等）表明 operational formalizability 边界在快速移动；FIRMA (MathNLP 2025) 的 complexity router 面临类似的\"复杂度是相对于什么定义的\"问题。\n\n【发掘点 5】\n- 维度: 核心 claim 强化\n- 内容: **Contribution 3（asymmetric cost-aware routing threshold）不够撑一个独立贡献，建议将其合并或替换。** 非对称代价感知阈值是 cost-sensitive classification 的标准技术（dating back to Elkan 2001），在此场景中应用虽合理，但缺乏技术深度作为独立贡献。建议两种替代方案：(a) 将其降级为 Contribution 2 的实现细节，然后提升一个新贡献——例如\"formalizability-guided confidence calibration\"：利用 routing decision 和 roundtrip verification 结果，为每个 step 的 PRM score 提供 calibrated uncertainty estimate，formal-verified steps 和 neural-scored steps 的 score 有不同的 reliability interpretation，这对下游 Best-of-N reranking 可能有实际影响（formal-verified positive 的权重应该高于 neural-scored positive）；或 (b) 将重心放在 router 作为\"tool competence meta-learner\"的角度——router 本质上在学习 autoformalization 工具的能力边界，这是一个更有趣的 framing，可以连接到 tool-use 和 meta-learning 的文献。\n- 价值: 三个 contributions 应该每个都有足够的 novelty 承载力。当前 C3 太弱会拉低整体 perceived contribution（Novelty 维度）。\n- 调研依据: 基于领域整体趋势判断——asymmetric thresholds 在 ML 中是基础技术；FIRMA 的 complexity router 和 Router-R1 的动态 LLM 选择提供了更有 novelty 的 routing 相关贡献模式。\n\nSources:\n- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)\n- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)\n- [FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment](https://aclanthology.org/2025.mathnlp-main.5/)\n- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774)\n- [Do LLMs Game Formalization?](https://arxiv.org/html/2604.19459)\n- [StepFun-Formalizer](https://arxiv.org/pdf/2508.04440)\n- [Router-R1: Multi-Round Routing via RL](https://openreview.net/forum?id=DWf4vroKWJ)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research context. Let me compile my assessment.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **GenPRM (AAAI 2026, arXiv:2504.00891)**: 在 ProcessBench 上用 F1 评测 step-level verification，在 MATH/AMC23/AIME24/OlympiadBench/Omni-MATH 上用 Best-of-N reranking (Maj@8)。Baseline 覆盖 1.5B–72B 多个规模的 discriminative 和 generative PRM。代码开源。\n- **FoVer (ACL 2026, arXiv:2505.15960)**: 用 Z3+Isabelle 标注 80K 训练数据，在 12 个推理 benchmark 上评测 (含 ProcessBench, MATH, AIME, ANLI, MMLU-PRO, BBH)，用 Best-of-K + AUROC 报告结果。公开代码。关键发现：formal-only 方法在 informal reasoning step 上有 overly-strict 行为。\n- **ThinkPRM (arXiv:2504.16828)**: 确立了 token-budget-normalized comparison 范式——在相同 token 预算下比较不同方法的性能。OOD 评测用 GPQA-Diamond 和 LiveCodeBench。仅用 8K process labels 超越了 100× 数据量训练的 discriminative PRM。\n- **R-PRM (EMNLP 2025, arXiv:2503.21295)**: 三阶段训练 (cold-start → DPO → inference scaling)，在 ProcessBench 和 PRMBench 上分别 +13.9 F1 和 +8.5 F1。Best-of-N 在 6 个数据集上平均 +8.6。F1 是核心指标。\n- **RRM (arXiv:2510.07774, withdrawn from ICLR 2026)**: 定义 miracle step 分类体系，通过 rubric reward 减少 71% miracle steps。评测用 Verified Pass@1024 on AIME2024（从 26.7%→62.6%）。**公开了 miracle step 标注 taxonomy 但未见独立的 miracle step detection benchmark**。\n- **Roundtrip Verification (arXiv:2604.25031)**: 在 150 条交通规则 (traffic rules) 上评测，将 formal equivalence 从 45-61% 提升到 83-85%。**评测域是交通规则，非数学推理步骤**。\n- **Risk-Controlled Lean-as-Judge (arXiv:2605.28365)**: 7B autoformalizer 在 MATH-500 上 43% faithfulness, 28% coverage。提出 CovCal 风险控制方法。\n- **GR-Ben (arXiv:2605.01203, May 2025)**: 新提出的 general reasoning PRM benchmark，覆盖科学和逻辑推理 9 个子域，发现现有 PRM 在数学以外域显著更弱。\n- **PRMBench (ACL 2025, arXiv:2501.03124)**: 6,216 题 + 83,456 step-level 标签，按 simplicity/soundness/sensitivity 维度评测。F1 为核心指标。\n\n**调研总结**: 当前 PRM 领域的实验标准要求：(1) 在 ProcessBench + PRMBench 上用 F1 (部分加 AUROC) 报告 step-level accuracy；(2) Best-of-N reranking 在 MATH-500/AIME24 上报告 downstream 任务效果；(3) 至少一个 OOD benchmark (GPQA-Diamond 已成标配)；(4) token-budget-normalized 或 compute-matched comparison (ThinkPRM 范式)；(5) 审稿人普遍关注 compute fairness 和 ablation completeness。\n\n---\n\n【缺陷 1】\n- 类别: 实验设计不足\n- 问题: **Miracle step detection 是核心 claim (Contribution 1: \"conditional sound miracle detection\")，但直接评测方案最弱。** Proposal 计划的评测依赖三重 fallback：(a) RRM miracle taxonomy annotations \"if publicly available\"——调研显示 RRM 有 taxonomy 但无独立 detection benchmark 且论文已从 ICLR 撤稿，数据可获得性存疑；(b) PRMBench error-type categories \"as primary proxy\"——PRMBench 的 error 分类 (simplicity/soundness/sensitivity) 与 miracle step (unjustified logical leap from predecessors) 并非一一对应，soundness error 包含但不等价于 miracle step；(c) 自建 200-300 step 标注集——作为论文核心 claim 的主要评测，规模偏小且统计检验力不足。审稿人大概率会质疑：your flagship contribution lacks a direct, adequate evaluation。\n- 严重度: 可补救\n- 补救方案:\n  1. **必须将自建 miracle step 标注集升级为主要评测**，而非第三选项。规模建议至少 500-800 step (来自 MATH-500 + AIME24 的 LLM 生成解题过程)，标注 schema 严格对齐 RRM 的 miracle step 定义 (step S_i 不可从 {S_1,...,S_{i-1}} 推导)。3 名标注者，报告 Fleiss' kappa (非 Cohen's kappa，因为 >2 标注者)。\n  2. **构造 synthetic miracle step 测试用例作为补充**：在已知正确的推理链中，人为替换某一步为 unjustified leap (如直接跳到答案、跳过关键推导步骤)，构造 positive cases；保留原始正确推理链作为 negative cases。这种 adversarial evaluation 不依赖外部数据，可控且可复现。\n  3. 将 PRMBench 的 soundness 错误子集作为辅助参考，但明确说明 coverage gap，不能声称它等同于 miracle step evaluation。\n- 调研依据: RRM (arXiv:2510.07774) 定义了 miracle step taxonomy 但未提供独立的 detection benchmark 数据集；PRMBench (arXiv:2501.03124) 的 error 分类与 miracle step 定义有 overlap 但非等价。\n\n【缺陷 2】\n- 类别: ablation 不完整\n- 问题: **7 个 ablation 中缺少对 roundtrip verification 的单独 ablation。** Roundtrip faithfulness verification 是 Layer 2，是连接 formalizability routing 和 formal soundness guarantee 的关键环节，也是论文 technical contribution 的核心组件之一。当前 ablation 覆盖了 routing (ablation 1-4, 6)、threshold (ablation 5)、label noise (ablation 7)，但没有隔离 roundtrip verification 的贡献。审稿人会问：如果去掉 roundtrip verification 直接送 Z3，性能/soundness 下降多少？roundtrip verification 的 error filtering rate 是多少？\n- 严重度: 可补救\n- 补救方案:\n  添加 **Ablation 8: No roundtrip verification** — 路由到 formal branch 的 step 直接送 Z3 autoformalize + verify，跳过 roundtrip faithfulness check。对比指标：(a) miracle step detection precision/recall (roundtrip filter 应能过滤掉 unfaithful formalization 导致的 false alarm)；(b) effective soundness coverage 变化。同时报告 roundtrip verification 的 pass/fail rate 和典型 failure mode (参考 arXiv:2604.19459 的 axiom fabrication 和 premise mistranslation 分类)。\n- 调研依据: Do LLMs Game Formalization? (arXiv:2604.19459) 识别了 compilation-based check 无法检测的 unfaithfulness modes；Roundtrip Verification (arXiv:2604.25031) 在交通规则上将 faithfulness 从 45-61% 提升到 83-85%，表明 roundtrip check 贡献显著——但该贡献需要在数学域上被独立验证和度量。\n\n【缺陷 3】\n- 类别: compute 公平性问题\n- 问题: **Autoformalization 使用 Qwen2.5-Math-72B-Instruct，而所有对比 baseline (GenPRM-7B, R-PRM-7B, FoVer-7B, ThinkPRM-14B) 最大不超过 14B (排除 Qwen2.5-Math-PRM-72B 这个 discriminative PRM)。** 虽然 proposal 已提出 compute-matched GenPRM majority voting 对比和 Pareto curve，但 72B autoformalization model 的引入使得实际计算量远超 7B baseline。审稿人可能质疑：性能提升是来自 learned routing 和 formal verification，还是来自额外的 72B model capacity？\n- 严重度: 可补救\n- 补救方案:\n  1. 添加 **7B autoformalization ablation**：用 Qwen2.5-Math-7B-Instruct (或 Qwen3-8B) 替换 72B 作为 autoformalizer，报告 autoformalization success rate、roundtrip pass rate、formal branch coverage 的变化，以及最终 PRM 性能。这直接隔离了 72B model capacity 的贡献。\n  2. 在 compute Pareto curve 中明确标注 FormalRoute-PRM@7B-autoformalizer 和 FormalRoute-PRM@72B-autoformalizer 两个点。\n  3. 如果 7B autoformalizer 性能显著下降，这反而是一个 insight：可以讨论 autoformalization quality 作为 hybrid PRM 的瓶颈，呼应 Risk-Controlled Lean-as-Judge 的发现 (7B 只有 43% faithfulness)。\n- 调研依据: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 报告 7B autoformalizer 仅 43% faithfulness/28% coverage，表明 model scale 对 autoformalization 质量有重大影响；ThinkPRM 确立的 token-budget-normalized comparison 范式要求在相同计算量下比较——当前方案中 72B 的隐性计算成本是 compute fairness 的主要漏洞。\n\n【缺陷 4】\n- 类别: 可行性问题\n- 问题: **Roundtrip verification 在数学推理域的可行性未经验证。** Proposal 引用的 roundtrip verification 方法 (arXiv:2604.25031) 仅在 150 条交通规则上评测 (将 faithfulness 从 45-61% 提升到 83-85%)。数学推理步骤与交通规则在结构上有本质差异：数学步骤涉及更复杂的符号操作、隐式引理调用和多步依赖关系。Roundtrip verification 在数学推理步骤上的 pass rate 和 error filtering effectiveness 未知，存在可行性风险。\n- 严重度: 可补救\n- 补救方案:\n  1. 在正式实验之前，用 FoVer 的公开数据（已有 Z3 formalization 的步骤）做一个 **roundtrip verification pilot study**：随机抽取 200-500 个 formalizable step，执行完整的 autoformalize → back-translate → semantic equivalence check pipeline，报告 pass rate、failure modes、与 Z3 ground truth 的一致性。\n  2. 在论文中明确报告 roundtrip verification 在数学域的实际 pass rate（作为 honest coverage reporting 的一部分），并讨论与交通规则域的 gap。\n  3. 如果数学域 roundtrip pass rate 显著低于交通规则域 (如 <50%)，需要讨论替代或补充的 faithfulness check 方法（如 back-translation + entailment model 代替 strict equivalence check）。\n- 调研依据: Roundtrip Verification (arXiv:2604.25031) 仅在交通规则域 (150 examples) 评测；Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 量化了数学域 autoformalization 的低 faithfulness (43%)，暗示数学域的 roundtrip verification 可能面临更大挑战。\n\n【缺陷 5】\n- 类别: 实验设计不足\n- 问题: **Effective soundness coverage 可能过低，需要预估和 contingency plan。** 根据调研数据粗略估算：若 router 将 ~40-50% 的 step 路由到 formal branch，roundtrip verification pass rate 在数学域可能只有 ~50-60% (乐观估计，参考 arXiv:2604.25031 在交通规则域的 base rate 45-61%)，则最终 effective soundness coverage ≈ 20-30%。如果这个数字在某些 benchmark 上更低 (如 GPQA-Diamond 的科学推理步骤)，审稿人会质疑：formal soundness guarantee 只覆盖 ~20% 的 step，是否足以支撑 \"conditional sound miracle detection\" 的 claim？\n- 严重度: 可补救\n- 补救方案:\n  1. 在论文中 **预先设定 meaningful coverage threshold**（如 >15%），并讨论不同 coverage level 下 formal guarantee 的实际价值。即使 coverage 只有 20%，如果这 20% 恰好是 high-stakes step (如关键推导步骤)，formal guarantee 仍有意义。\n  2. 添加 **per-benchmark coverage breakdown**：在每个 benchmark 上分别报告 formal branch activation rate、roundtrip pass rate、effective soundness coverage，让审稿人看到 coverage 在不同任务类型上的分布。\n  3. 添加 **coverage-conditioned analysis**：在 formal guarantee 覆盖的 step 子集上单独报告 miracle detection precision/recall，与全量 step 上的性能对比，展示 formal branch 在其覆盖范围内的优势。\n  4. 如果某些 benchmark 上 coverage 过低 (<10%)，主动承认并讨论作为 limitation，这比被审稿人发现后被动辩解更有利。\n- 调研依据: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 的 28% coverage (7B autoformalizer on MATH-500) 提供了一个参考下界；该论文本身采用了 honest coverage reporting 作为方法论，proposal 应效仿其量化风格。\n\n【缺陷 6】\n- 类别: baseline 不足或过时\n- 问题: **缺少近期新发布的 general reasoning PRM benchmark (GR-Ben)。** GR-Ben (arXiv:2605.01203, May 2025) 覆盖科学和逻辑推理 9 个子域，调研发现现有 PRM 在数学以外域显著更弱。Proposal 声称的 formalizability routing 方法理论上在逻辑推理域应有更强优势（更多 step 可 formalize），但当前评测计划完全集中在数学推理 + GPQA-Diamond，缺少对逻辑推理这一 formal verification 天然优势域的评测。\n- 严重度: 可补救\n- 补救方案:\n  建议在评测中考虑加入 GR-Ben 的逻辑推理子集 (logic subdomain)，或者 FoVer 评测中使用的 ANLI/BBH 中的逻辑推理部分，作为 \"formal-friendly domain\" 的评测。这不仅增加 benchmark 覆盖度，更能展示 FormalRoute-PRM 在 formal verification 天然适用域上的优势放大效应——如果 formal branch coverage 在逻辑推理域显著高于数学域，这本身就是一个有意义的 finding。这条建议优先级低于前 5 条，属于 nice-to-have。\n- 调研依据: GR-Ben (arXiv:2605.01203) 的调研结论显示 PRM 在数学以外域更弱；FoVer (arXiv:2505.15960) 已在 ANLI/BBH 等逻辑推理 benchmark 上验证了 formal verification 训练数据的跨域 transfer 能力。\n\n---\n\n**总结**: 该 proposal 的实验设计**基础扎实**——baseline 矩阵覆盖广泛、ablation 设计丰富（7 个）、compute fairness 有显式考量、honest coverage reporting 设计合理。上述 6 个缺陷中：**缺陷 1 (miracle step 直接评测不足) 和缺陷 3 (72B compute fairness) 是审稿人最可能提出的 major concern**；缺陷 2 (roundtrip ablation) 和缺陷 4 (roundtrip 在数学域的可行性) 是容易补的中等缺陷；缺陷 5 和 6 是加分项。所有缺陷均可补救，无方向性致命问题。\n\nSources:\n- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)\n- [RRM: Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards](https://arxiv.org/abs/2510.07774)\n- [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](https://arxiv.org/html/2605.28365)\n- [Faithful Autoformalization via Roundtrip Verification and Repair](https://arxiv.org/abs/2604.25031)\n- [Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning](https://arxiv.org/html/2604.19459)\n- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)\n- [GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models](https://arxiv.org/abs/2605.01203)\n- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/pdf/2601.20055)\n- [LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision](https://openreview.net/forum?id=A3FhAVfcJI)"
}
```

---

### Runtime record

_source line 72 · 2026-05-29T06:27:21.024Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:27:21.024Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

## Round 4

24 recorded events

### User

_source line 73 · 2026-05-29T06:27:21.066Z_

【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have sufficient research to provide a thorough assessment. Let me synthesize my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- **Risk-Controlled Lean-as-Judge (arXiv:2605.28365, May 2026)**: Reports 28% problem coverage and only 43% proof faithfulness for a 7B autoformalizer on MATH-500. Proposes COVCAL for risk-controlled selective verification. This paper is the most critical calibration reference — it quantifies exactly how thin the "formal guarantee" layer can be in practice.
- **FoVer (arXiv:2505.15960, ACL 2026 Findings)**: Uses Z3/Isabelle to synthesize PRM training labels. Generalizes well across 12 benchmarks including non-formal tasks. The "overly strict" claim from the proposal needs to be verified against FoVer's actual reporting — FoVer frames its limitation as limited formal coverage, not necessarily false alarms on informal steps.
- **VERGE (arXiv:2601.20055)**: Rule-based semantic routing (logical vs. commonsense claims) to Z3 or LLM ensemble. 18.7% uplift. Explicitly identifies "learned routing" as future work. Validates the routing-matters hypothesis.
- **LogicReward (arXiv:2512.18196, ICLR 2026)**: Isabelle-based step verification with fallback. Primarily an RL training framework. Its "try-formal-first" approach is indeed the natural baseline for the routing idea.
- **FIRMA (MathNLP 2025)**: Complexity-aware routing for formal-informal translation. Has a complexity router, but targets translation quality, not verification correctness. The proposal correctly differentiates, but FIRMA's router architecture and training methodology may provide useful technical parallels.
- **RRM (arXiv:2510.07774)**: Defines miracle step taxonomy. Reduces miracle steps 71% via rubric rewards. Never attempts formal derivability checking. Withdrawn from ICLR 2026, which may affect its credibility as a foundation for the miracle step concept.
- **Autoformalization landscape (StepFun-Formalizer, FormaRL, etc.)**: Autoformalization is improving rapidly (130k lines of topology in 2 weeks at ~$100 cost), but step-level faithfulness remains a major bottleneck. No prior work explicitly frames "formalizability" as a learnable, context-dependent property for verification routing.
- 调研总结: 领域当前在两个轴上推进——(1) 提升 autoformalization 的覆盖率和忠实度 (Risk-Controlled, roundtrip verification, StepFun)，(2) 构建更强的 neural PRM (GenPRM, ThinkPRM, R-PRM)。将两者通过学习路由桥接的工作尚无人做，但核心瓶颈在于 autoformalization 的有效覆盖率可能太低，导致形式化分支的实际价值存疑。

---

【发掘点 1】
- 维度: significance 提升
- 内容: **有效形式化覆盖率是 significance 的生死线，proposal 必须正面回应而非仅"honest reporting"。** 根据 Risk-Controlled Lean-as-Judge 的数据，7B autoformalizer 在 MATH-500 上 28% coverage × 43% faithfulness ≈ 12% 有效覆盖。即使用 72B autoformalizer 并假设覆盖率翻倍、忠实度提升到 60%，有效覆盖也仅约 56% × 60% ≈ 34%，再乘以 router 准确率（假设 85%），最终约 29% 的 steps 获得形式化保证。一个对 ~29% steps 提供 soundness guarantee、其余 ~71% 只有 neural scoring 的 PRM，审稿人会问：这比 pure neural PRM 好多少？当前 proposal 的策略是"honest coverage reporting"，但这是防守姿态。更有力的 framing 应该是：**argue that formal coverage is disproportionately concentrated on the steps where it matters most**——即 miracle steps 往往发生在明确的逻辑推导环节（代数变换、方程求解、不等式推导），而这些恰好是 autoformalization 最擅长处理的 step 类型。如果能论证"形式化覆盖率虽低，但精准覆盖了 miracle step 高发区"，significance 会大幅提升。建议在 proposal 中增加一个分析维度：formal branch coverage 与 miracle step occurrence 的相关性假设及预实验验证计划。
- 价值: 直接决定审稿人是否认为这个 conditional soundness guarantee 在实践中有意义（Significance 维度）。一个"覆盖 12% 但精准命中高风险 steps"的故事远比"覆盖 12%，剩下全靠 neural"有说服力。
- 调研依据: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 提供的 43% faithfulness / 28% coverage 数据，以及 RRM (arXiv:2510.07774) 对 miracle step 发生场景的分析（miracle steps 集中在明确的推理跳跃环节）。

【发掘点 2】
- 维度: novelty 锐化
- 内容: **"条件性 soundness"的 framing 有被审稿人视为 tautological 的风险，需要重新定位 novelty 的核心承载点。** 当前 Contribution 1 说"on steps that pass routing AND roundtrip verification, Z3 provides guaranteed miracle detection"——一个严格的审稿人可能反应为"if you can formally verify a step, of course you know whether it's correct; the hard part is getting there reliably, not the guarantee itself." 真正的 novelty 不是"形式验证是 sound 的"（这是 Z3 的固有属性），而是：**构建了一个实用系统，能可靠地识别哪些 steps 可以信赖地送入形式验证管道，并通过 roundtrip verification 确保 formalization 的忠实度**。建议将 Contribution 1 的叙事从"we provide formal soundness guarantees"转向"we solve the practical problem of reliably routing steps to the right verifier, making conditional formal soundness achievable at scale for the first time"。这样 novelty 的重心从 Z3（已知）转移到 routing + roundtrip gating pipeline（新的）。
- 价值: 防止审稿人将核心贡献归因于 Z3 的已有能力而非本文的系统设计（Novelty 维度）。
- 调研依据: FoVer 已经使用 Z3 做 step-level verification；VERGE 已经做了 Z3 routing；本文的真正增量在 routing 的学习化和 roundtrip gating，而非 Z3 验证本身。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: **Ablation #6（try-formal-first + neural fallback）是最严重的 trivial alternative 威胁，当前 proposal 对其的回应不够有力。** Proposal 列出三个 learned routing 的优势：(i) 避免 false alarms, (ii) 提供 per-step confidence tier, (iii) 区分 intrinsic formalizability vs extrinsic autoformalization capability。但 (ii) 是 output format 设计，不依赖 learned routing；(iii) 在概念上有趣但不清楚如何在实验中验证。唯一的硬优势是 (i)——避免 non-formalizable steps 被送入 formal pipeline 后产生 false alarms。但如果 Layer 2（roundtrip verification）已经能过滤掉大部分 unfaithful formalizations，那 try-and-fallback + roundtrip verification 可能也能避免大部分 false alarms，只是多花了 autoformalization 的 compute。**建议明确回答：在有 roundtrip verification 作为安全网的情况下，learned router 相比 try-and-fallback 的增量到底在哪里？** 可能的强答案是：(a) roundtrip verification 并非完美——Do LLMs Game Formalization (arXiv:2604.19459) 指出 axiom fabrication 和 premise mistranslation 可以逃过 compilation 检查，也可能逃过 roundtrip verification；learned router 作为第一道防线可以在这些情况下避免错误。(b) compute savings：避免对 ~50-70% non-formalizable steps 做 72B 模型 autoformalization 推理，这是非平凡的 cost reduction。需要在 proposal 中将这两点论证做实。
- 价值: 如果审稿人认为 try-and-fallback 就够了，整个 learned routing 贡献就被消解（Novelty 维度核心威胁）。
- 调研依据: Do LLMs Game Formalization (arXiv:2604.19459) 关于 unfaithfulness 逃过 compilation 检查的发现；LogicReward (arXiv:2512.18196) 的 try-formal-first 设计作为直接 baseline。

【发掘点 4】
- 维度: 前提假设质疑
- 内容: **"Formalizability"作为步骤的内禀属性的假设需要更严谨的论证。** 当前 proposal 将 formalizability label 定义为 "Z3 compilation success AND roundtrip semantic verification pass"——这意味着 formalizability 是相对于特定 autoformalizer（Qwen2.5-Math-72B-Instruct）和特定 formal system（Z3 的 SMT-LIB 片段）的操作性定义，而非步骤的内禀语义属性。随着 autoformalizer 能力提升（2025-2026 autoformalization 进展迅速，如 130k lines of topology in two weeks），今天"non-formalizable"的步骤明天可能变成 formalizable。这产生两个问题：(a) router 的训练标签有时效性，模型可能学到的是当前 autoformalizer 的能力边界而非步骤的内禀属性；(b) 审稿人可能质疑"formalizability"概念的稳定性。**建议在 proposal 中明确区分两个层面：intrinsic formalizability（步骤在原则上是否可以用一阶逻辑/SMT 表达）和 operational formalizability（给定当前 autoformalization 工具链，步骤是否能被可靠地形式化）。Router 学习的是后者，但 contribution 的价值论证应该建立在前者之上——因为 intrinsically formalizable 的步骤恰好是 miracle step 最不应该出现、出现后最值得被形式化检测的地方。** 这个区分不仅让概念更严谨，还能回应"autoformalizer 变好了 router 就没用了"的质疑：即使 autoformalizer 完美了，routing 仍然有价值，因为 intrinsically non-formalizable 的步骤（如直觉判断、heuristic arguments）送入形式验证仍然会产生无意义结果。
- 价值: 概念基础的严谨性直接影响审稿人对整个技术方案的信任度（Novelty + Significance 维度）。
- 调研依据: Autoformalization 快速进展（130k lines of topology, StepFun-Formalizer 等）表明 operational formalizability 边界在快速移动；FIRMA (MathNLP 2025) 的 complexity router 面临类似的"复杂度是相对于什么定义的"问题。

【发掘点 5】
- 维度: 核心 claim 强化
- 内容: **Contribution 3（asymmetric cost-aware routing threshold）不够撑一个独立贡献，建议将其合并或替换。** 非对称代价感知阈值是 cost-sensitive classification 的标准技术（dating back to Elkan 2001），在此场景中应用虽合理，但缺乏技术深度作为独立贡献。建议两种替代方案：(a) 将其降级为 Contribution 2 的实现细节，然后提升一个新贡献——例如"formalizability-guided confidence calibration"：利用 routing decision 和 roundtrip verification 结果，为每个 step 的 PRM score 提供 calibrated uncertainty estimate，formal-verified steps 和 neural-scored steps 的 score 有不同的 reliability interpretation，这对下游 Best-of-N reranking 可能有实际影响（formal-verified positive 的权重应该高于 neural-scored positive）；或 (b) 将重心放在 router 作为"tool competence meta-learner"的角度——router 本质上在学习 autoformalization 工具的能力边界，这是一个更有趣的 framing，可以连接到 tool-use 和 meta-learning 的文献。
- 价值: 三个 contributions 应该每个都有足够的 novelty 承载力。当前 C3 太弱会拉低整体 perceived contribution（Novelty 维度）。
- 调研依据: 基于领域整体趋势判断——asymmetric thresholds 在 ML 中是基础技术；FIRMA 的 complexity router 和 Router-R1 的动态 LLM 选择提供了更有 novelty 的 routing 相关贡献模式。

Sources:
- [Risk-Controlled Lean-as-Judge](https://arxiv.org/abs/2605.28365)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [LogicReward: Step-Wise Logical Supervision](https://arxiv.org/abs/2512.18196)
- [FIRMA: Bidirectional Formal-Informal Mathematical Language Alignment](https://aclanthology.org/2025.mathnlp-main.5/)
- [Curing Miracle Steps with Rubric Rewards](https://arxiv.org/abs/2510.07774)
- [Do LLMs Game Formalization?](https://arxiv.org/html/2604.19459)
- [StepFun-Formalizer](https://arxiv.org/pdf/2508.04440)
- [Router-R1: Multi-Round Routing via RL](https://openreview.net/forum?id=DWf4vroKWJ)

【补救 agent 本轮输出】:
Now I have sufficient research context. Let me compile my assessment.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **GenPRM (AAAI 2026, arXiv:2504.00891)**: 在 ProcessBench 上用 F1 评测 step-level verification，在 MATH/AMC23/AIME24/OlympiadBench/Omni-MATH 上用 Best-of-N reranking (Maj@8)。Baseline 覆盖 1.5B–72B 多个规模的 discriminative 和 generative PRM。代码开源。
- **FoVer (ACL 2026, arXiv:2505.15960)**: 用 Z3+Isabelle 标注 80K 训练数据，在 12 个推理 benchmark 上评测 (含 ProcessBench, MATH, AIME, ANLI, MMLU-PRO, BBH)，用 Best-of-K + AUROC 报告结果。公开代码。关键发现：formal-only 方法在 informal reasoning step 上有 overly-strict 行为。
- **ThinkPRM (arXiv:2504.16828)**: 确立了 token-budget-normalized comparison 范式——在相同 token 预算下比较不同方法的性能。OOD 评测用 GPQA-Diamond 和 LiveCodeBench。仅用 8K process labels 超越了 100× 数据量训练的 discriminative PRM。
- **R-PRM (EMNLP 2025, arXiv:2503.21295)**: 三阶段训练 (cold-start → DPO → inference scaling)，在 ProcessBench 和 PRMBench 上分别 +13.9 F1 和 +8.5 F1。Best-of-N 在 6 个数据集上平均 +8.6。F1 是核心指标。
- **RRM (arXiv:2510.07774, withdrawn from ICLR 2026)**: 定义 miracle step 分类体系，通过 rubric reward 减少 71% miracle steps。评测用 Verified Pass@1024 on AIME2024（从 26.7%→62.6%）。**公开了 miracle step 标注 taxonomy 但未见独立的 miracle step detection benchmark**。
- **Roundtrip Verification (arXiv:2604.25031)**: 在 150 条交通规则 (traffic rules) 上评测，将 formal equivalence 从 45-61% 提升到 83-85%。**评测域是交通规则，非数学推理步骤**。
- **Risk-Controlled Lean-as-Judge (arXiv:2605.28365)**: 7B autoformalizer 在 MATH-500 上 43% faithfulness, 28% coverage。提出 CovCal 风险控制方法。
- **GR-Ben (arXiv:2605.01203, May 2025)**: 新提出的 general reasoning PRM benchmark，覆盖科学和逻辑推理 9 个子域，发现现有 PRM 在数学以外域显著更弱。
- **PRMBench (ACL 2025, arXiv:2501.03124)**: 6,216 题 + 83,456 step-level 标签，按 simplicity/soundness/sensitivity 维度评测。F1 为核心指标。

**调研总结**: 当前 PRM 领域的实验标准要求：(1) 在 ProcessBench + PRMBench 上用 F1 (部分加 AUROC) 报告 step-level accuracy；(2) Best-of-N reranking 在 MATH-500/AIME24 上报告 downstream 任务效果；(3) 至少一个 OOD benchmark (GPQA-Diamond 已成标配)；(4) token-budget-normalized 或 compute-matched comparison (ThinkPRM 范式)；(5) 审稿人普遍关注 compute fairness 和 ablation completeness。

---

【缺陷 1】
- 类别: 实验设计不足
- 问题: **Miracle step detection 是核心 claim (Contribution 1: "conditional sound miracle detection")，但直接评测方案最弱。** Proposal 计划的评测依赖三重 fallback：(a) RRM miracle taxonomy annotations "if publicly available"——调研显示 RRM 有 taxonomy 但无独立 detection benchmark 且论文已从 ICLR 撤稿，数据可获得性存疑；(b) PRMBench error-type categories "as primary proxy"——PRMBench 的 error 分类 (simplicity/soundness/sensitivity) 与 miracle step (unjustified logical leap from predecessors) 并非一一对应，soundness error 包含但不等价于 miracle step；(c) 自建 200-300 step 标注集——作为论文核心 claim 的主要评测，规模偏小且统计检验力不足。审稿人大概率会质疑：your flagship contribution lacks a direct, adequate evaluation。
- 严重度: 可补救
- 补救方案:
  1. **必须将自建 miracle step 标注集升级为主要评测**，而非第三选项。规模建议至少 500-800 step (来自 MATH-500 + AIME24 的 LLM 生成解题过程)，标注 schema 严格对齐 RRM 的 miracle step 定义 (step S_i 不可从 {S_1,...,S_{i-1}} 推导)。3 名标注者，报告 Fleiss' kappa (非 Cohen's kappa，因为 >2 标注者)。
  2. **构造 synthetic miracle step 测试用例作为补充**：在已知正确的推理链中，人为替换某一步为 unjustified leap (如直接跳到答案、跳过关键推导步骤)，构造 positive cases；保留原始正确推理链作为 negative cases。这种 adversarial evaluation 不依赖外部数据，可控且可复现。
  3. 将 PRMBench 的 soundness 错误子集作为辅助参考，但明确说明 coverage gap，不能声称它等同于 miracle step evaluation。
- 调研依据: RRM (arXiv:2510.07774) 定义了 miracle step taxonomy 但未提供独立的 detection benchmark 数据集；PRMBench (arXiv:2501.03124) 的 error 分类与 miracle step 定义有 overlap 但非等价。

【缺陷 2】
- 类别: ablation 不完整
- 问题: **7 个 ablation 中缺少对 roundtrip verification 的单独 ablation。** Roundtrip faithfulness verification 是 Layer 2，是连接 formalizability routing 和 formal soundness guarantee 的关键环节，也是论文 technical contribution 的核心组件之一。当前 ablation 覆盖了 routing (ablation 1-4, 6)、threshold (ablation 5)、label noise (ablation 7)，但没有隔离 roundtrip verification 的贡献。审稿人会问：如果去掉 roundtrip verification 直接送 Z3，性能/soundness 下降多少？roundtrip verification 的 error filtering rate 是多少？
- 严重度: 可补救
- 补救方案:
  添加 **Ablation 8: No roundtrip verification** — 路由到 formal branch 的 step 直接送 Z3 autoformalize + verify，跳过 roundtrip faithfulness check。对比指标：(a) miracle step detection precision/recall (roundtrip filter 应能过滤掉 unfaithful formalization 导致的 false alarm)；(b) effective soundness coverage 变化。同时报告 roundtrip verification 的 pass/fail rate 和典型 failure mode (参考 arXiv:2604.19459 的 axiom fabrication 和 premise mistranslation 分类)。
- 调研依据: Do LLMs Game Formalization? (arXiv:2604.19459) 识别了 compilation-based check 无法检测的 unfaithfulness modes；Roundtrip Verification (arXiv:2604.25031) 在交通规则上将 faithfulness 从 45-61% 提升到 83-85%，表明 roundtrip check 贡献显著——但该贡献需要在数学域上被独立验证和度量。

【缺陷 3】
- 类别: compute 公平性问题
- 问题: **Autoformalization 使用 Qwen2.5-Math-72B-Instruct，而所有对比 baseline (GenPRM-7B, R-PRM-7B, FoVer-7B, ThinkPRM-14B) 最大不超过 14B (排除 Qwen2.5-Math-PRM-72B 这个 discriminative PRM)。** 虽然 proposal 已提出 compute-matched GenPRM majority voting 对比和 Pareto curve，但 72B autoformalization model 的引入使得实际计算量远超 7B baseline。审稿人可能质疑：性能提升是来自 learned routing 和 formal verification，还是来自额外的 72B model capacity？
- 严重度: 可补救
- 补救方案:
  1. 添加 **7B autoformalization ablation**：用 Qwen2.5-Math-7B-Instruct (或 Qwen3-8B) 替换 72B 作为 autoformalizer，报告 autoformalization success rate、roundtrip pass rate、formal branch coverage 的变化，以及最终 PRM 性能。这直接隔离了 72B model capacity 的贡献。
  2. 在 compute Pareto curve 中明确标注 FormalRoute-PRM@7B-autoformalizer 和 FormalRoute-PRM@72B-autoformalizer 两个点。
  3. 如果 7B autoformalizer 性能显著下降，这反而是一个 insight：可以讨论 autoformalization quality 作为 hybrid PRM 的瓶颈，呼应 Risk-Controlled Lean-as-Judge 的发现 (7B 只有 43% faithfulness)。
- 调研依据: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 报告 7B autoformalizer 仅 43% faithfulness/28% coverage，表明 model scale 对 autoformalization 质量有重大影响；ThinkPRM 确立的 token-budget-normalized comparison 范式要求在相同计算量下比较——当前方案中 72B 的隐性计算成本是 compute fairness 的主要漏洞。

【缺陷 4】
- 类别: 可行性问题
- 问题: **Roundtrip verification 在数学推理域的可行性未经验证。** Proposal 引用的 roundtrip verification 方法 (arXiv:2604.25031) 仅在 150 条交通规则上评测 (将 faithfulness 从 45-61% 提升到 83-85%)。数学推理步骤与交通规则在结构上有本质差异：数学步骤涉及更复杂的符号操作、隐式引理调用和多步依赖关系。Roundtrip verification 在数学推理步骤上的 pass rate 和 error filtering effectiveness 未知，存在可行性风险。
- 严重度: 可补救
- 补救方案:
  1. 在正式实验之前，用 FoVer 的公开数据（已有 Z3 formalization 的步骤）做一个 **roundtrip verification pilot study**：随机抽取 200-500 个 formalizable step，执行完整的 autoformalize → back-translate → semantic equivalence check pipeline，报告 pass rate、failure modes、与 Z3 ground truth 的一致性。
  2. 在论文中明确报告 roundtrip verification 在数学域的实际 pass rate（作为 honest coverage reporting 的一部分），并讨论与交通规则域的 gap。
  3. 如果数学域 roundtrip pass rate 显著低于交通规则域 (如 <50%)，需要讨论替代或补充的 faithfulness check 方法（如 back-translation + entailment model 代替 strict equivalence check）。
- 调研依据: Roundtrip Verification (arXiv:2604.25031) 仅在交通规则域 (150 examples) 评测；Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 量化了数学域 autoformalization 的低 faithfulness (43%)，暗示数学域的 roundtrip verification 可能面临更大挑战。

【缺陷 5】
- 类别: 实验设计不足
- 问题: **Effective soundness coverage 可能过低，需要预估和 contingency plan。** 根据调研数据粗略估算：若 router 将 ~40-50% 的 step 路由到 formal branch，roundtrip verification pass rate 在数学域可能只有 ~50-60% (乐观估计，参考 arXiv:2604.25031 在交通规则域的 base rate 45-61%)，则最终 effective soundness coverage ≈ 20-30%。如果这个数字在某些 benchmark 上更低 (如 GPQA-Diamond 的科学推理步骤)，审稿人会质疑：formal soundness guarantee 只覆盖 ~20% 的 step，是否足以支撑 "conditional sound miracle detection" 的 claim？
- 严重度: 可补救
- 补救方案:
  1. 在论文中 **预先设定 meaningful coverage threshold**（如 >15%），并讨论不同 coverage level 下 formal guarantee 的实际价值。即使 coverage 只有 20%，如果这 20% 恰好是 high-stakes step (如关键推导步骤)，formal guarantee 仍有意义。
  2. 添加 **per-benchmark coverage breakdown**：在每个 benchmark 上分别报告 formal branch activation rate、roundtrip pass rate、effective soundness coverage，让审稿人看到 coverage 在不同任务类型上的分布。
  3. 添加 **coverage-conditioned analysis**：在 formal guarantee 覆盖的 step 子集上单独报告 miracle detection precision/recall，与全量 step 上的性能对比，展示 formal branch 在其覆盖范围内的优势。
  4. 如果某些 benchmark 上 coverage 过低 (<10%)，主动承认并讨论作为 limitation，这比被审稿人发现后被动辩解更有利。
- 调研依据: Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 的 28% coverage (7B autoformalizer on MATH-500) 提供了一个参考下界；该论文本身采用了 honest coverage reporting 作为方法论，proposal 应效仿其量化风格。

【缺陷 6】
- 类别: baseline 不足或过时
- 问题: **缺少近期新发布的 general reasoning PRM benchmark (GR-Ben)。** GR-Ben (arXiv:2605.01203, May 2025) 覆盖科学和逻辑推理 9 个子域，调研发现现有 PRM 在数学以外域显著更弱。Proposal 声称的 formalizability routing 方法理论上在逻辑推理域应有更强优势（更多 step 可 formalize），但当前评测计划完全集中在数学推理 + GPQA-Diamond，缺少对逻辑推理这一 formal verification 天然优势域的评测。
- 严重度: 可补救
- 补救方案:
  建议在评测中考虑加入 GR-Ben 的逻辑推理子集 (logic subdomain)，或者 FoVer 评测中使用的 ANLI/BBH 中的逻辑推理部分，作为 "formal-friendly domain" 的评测。这不仅增加 benchmark 覆盖度，更能展示 FormalRoute-PRM 在 formal verification 天然适用域上的优势放大效应——如果 formal branch coverage 在逻辑推理域显著高于数学域，这本身就是一个有意义的 finding。这条建议优先级低于前 5 条，属于 nice-to-have。
- 调研依据: GR-Ben (arXiv:2605.01203) 的调研结论显示 PRM 在数学以外域更弱；FoVer (arXiv:2505.15960) 已在 ANLI/BBH 等逻辑推理 benchmark 上验证了 formal verification 训练数据的跨域 transfer 能力。

---

**总结**: 该 proposal 的实验设计**基础扎实**——baseline 矩阵覆盖广泛、ablation 设计丰富（7 个）、compute fairness 有显式考量、honest coverage reporting 设计合理。上述 6 个缺陷中：**缺陷 1 (miracle step 直接评测不足) 和缺陷 3 (72B compute fairness) 是审稿人最可能提出的 major concern**；缺陷 2 (roundtrip ablation) 和缺陷 4 (roundtrip 在数学域的可行性) 是容易补的中等缺陷；缺陷 5 和 6 是加分项。所有缺陷均可补救，无方向性致命问题。

Sources:
- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [RRM: Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards](https://arxiv.org/abs/2510.07774)
- [Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning](https://arxiv.org/html/2605.28365)
- [Faithful Autoformalization via Roundtrip Verification and Repair](https://arxiv.org/abs/2604.25031)
- [Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning](https://arxiv.org/html/2604.19459)
- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)
- [GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models](https://arxiv.org/abs/2605.01203)
- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/pdf/2601.20055)
- [LogicReward: Incentivizing LLM Reasoning via Step-Wise Logical Supervision](https://openreview.net/forum?id=A3FhAVfcJI)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15273721-d625-47db-9fb2-42df4d38f6f7",
  "isSidechain": false,
  "promptId": "d00ce7f4-5327-4e89-9fa4-f4d847cd112f",
  "type": "user",
  "uuid": "275ebbd6-ae4e-4afb-8ab5-893aa277930c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 74_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide a thorough assessment. Let me synthesize my findings.  ---  【状态】:…",
  "leafUuid": "275ebbd6-ae4e-4afb-8ab5-893aa277930c",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Assistant

_source line 76 · 2026-05-29T06:27:55.741Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the Round 3 outputs from both workers and determine whether to converge, continue, or stop.

**发掘 agent Round 3 summary:**
- Status: 有发掘空间 (but the points are getting more refined/defensive rather than discovering new angles)
- 5 points:
  1. Significance: Formal coverage may be ~12-29%; need to argue coverage is disproportionately concentrated on miracle-step-prone steps
  2. Novelty: "Conditional soundness" risks being tautological; reframe contribution from "Z3 is sound" to "we built a reliable pipeline to get steps to Z3"
  3. The learned router's incremental value over roundtrip verification needs a stronger case—roundtrip has limitations and there are compute savings to emphasize
  4. Should clarify the distinction between intrinsic and operational formalizability
  5. The asymmetric cost contribution feels underdeveloped as a standalone point; might need to consolidate or replace it

**补救 agent Round 3 summary:**
- Status: 有缺陷待补救
- The miracle step detection evaluation is the weakest component—should elevate the self-built annotation set to primary status and incorporate synthetic adversarial examples, while the roundtrip verification ablation remains incomplete
- The 72B autoformalization model introduces a compute fairness problem that requires a 7B variant for comparison
- Roundtrip verification has only been validated on traffic rules, not mathematical domains
- Effective soundness coverage is likely only 20-30%, so I need a backup plan
- GR-Ben and logic-domain evaluation would be nice additions but aren't critical

Looking at the convergence pattern across rounds, the changes from Round 1 to Round 2 were substantial structural shifts, but now in Round 3 the work is becoming more incremental—mostly defensive refinements and addressing anticipated reviewer concerns rather than uncovering fundamentally new angles. The remaining gaps I'm identifying are real but secondary in nature, focused on tightening the evaluation and scaling ablations.

The substantive moves from this round are worth considering: reframing the first contribution as a reliable routing pipeline rather than formal soundness itself, using the concentration of formal coverage on miracle-prone steps as a significance argument, distinguishing between intrinsic and operational formalizability, potentially merging or replacing the third contribution, upgrading the miracle step evaluation to use primarily self-built and synthetic data, adding the roundtrip verification ablation, and including the 7B autoformalizer ablation for fairness—while acknowledging that roundtrip verification hasn't been tested on mathematical content yet.

I should also add the domain risk acknowledgment as an honesty point, incorporate the coverage-conditioned analysis, and note GR-Ben as a lower-priority addition. These are all refinements that tighten the framing and strengthen the evaluation without restructuring the core argument, which suggests we're converging and should finalize after this round.

Before I integrate these suggestions, I need to verify a few things: whether GR-Ben actually exists and fits the narrative, whether there's real evidence that miracle steps cluster in formalizable step types rather than heuristic ones, and whether the roundtrip verification across different domains holds up under scrutiny. Let me run some targeted checks on these key claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "275ebbd6-ae4e-4afb-8ab5-893aa277930c",
  "isSidechain": false,
  "requestId": "req_011CbWPJsjcECeoQEjRx2cQv",
  "type": "assistant",
  "uuid": "006805d2-9dc9-469a-8aab-7c17b78fdad7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgYPCBiTDFcyx8UroW6LRv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16796,
      "cache_read_input_tokens": 61272,
      "output_tokens": 1235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1235,
          "cache_read_input_tokens": 61272,
          "cache_creation_input_tokens": 16796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16796
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

_source line 77 · 2026-05-29T06:27:55.746Z_

让我对第 3 轮的关键建议做交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "006805d2-9dc9-469a-8aab-7c17b78fdad7",
  "isSidechain": false,
  "requestId": "req_011CbWPJsjcECeoQEjRx2cQv",
  "type": "assistant",
  "uuid": "116bcfba-f769-4604-b0f2-c7c410494a8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgYPCBiTDFcyx8UroW6LRv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16796,
      "cache_read_input_tokens": 61272,
      "output_tokens": 1235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1235,
          "cache_read_input_tokens": 61272,
          "cache_creation_input_tokens": 16796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16796
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

_source line 78 · 2026-05-29T06:27:55.821Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YNXUCYbLr717uShqM3mpKW`</summary>

```json
{
  "query": "GR-Ben general reasoning benchmark process reward model arXiv 2605.01203 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "116bcfba-f769-4604-b0f2-c7c410494a8a",
  "isSidechain": false,
  "requestId": "req_011CbWPJsjcECeoQEjRx2cQv",
  "type": "assistant",
  "uuid": "4facf65b-9c4b-483f-936c-928d5e178e72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgYPCBiTDFcyx8UroW6LRv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16796,
      "cache_read_input_tokens": 61272,
      "output_tokens": 1235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1235,
          "cache_read_input_tokens": 61272,
          "cache_creation_input_tokens": 16796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16796
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

_source line 79 · 2026-05-29T06:27:56.135Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UFMgisNWgzCm1CRqi3cPNM`</summary>

```json
{
  "query": "miracle steps mathematical reasoning where do they occur algebraic logical steps unjustified leaps taxonomy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4facf65b-9c4b-483f-936c-928d5e178e72",
  "isSidechain": false,
  "requestId": "req_011CbWPJsjcECeoQEjRx2cQv",
  "type": "assistant",
  "uuid": "36163438-91d0-4a8c-a4a8-2daddc31e41e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KgYPCBiTDFcyx8UroW6LRv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16796,
      "cache_read_input_tokens": 61272,
      "output_tokens": 1235,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1235,
          "cache_read_input_tokens": 61272,
          "cache_creation_input_tokens": 16796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16796
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

_source line 80 · 2026-05-29T06:28:02.947Z_

<details><summary>↩ Tool result · `toolu_01UFMgisNWgzCm1CRqi3cPNM`</summary>

```text
Web search results for query: "miracle steps mathematical reasoning where do they occur algebraic logical steps unjustified leaps taxonomy"

Links: [{"title":"Curing “Miracle Steps” in LLM Mathematical Reasoning with Rubric Rewards","url":"https://arxiv.org/html/2510.07774v3"},{"title":"Curing Miracle Steps in LLM Mathematical Reasoning with ...","url":"https://arxiv.org/pdf/2510.07774"},{"title":"CURING “MIRACLE STEPS” IN LLM MATHEMATICAL ...","url":"https://openreview.net/pdf/365c5050a2ce26e04b0f1c843f16e9a72f9c704f.pdf"},{"title":"Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.07774v2"},{"title":"(PDF) Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://www.researchgate.net/publication/396372877_Curing_Miracle_Steps_in_LLM_Mathematical_Reasoning_with_Rubric_Rewards"},{"title":"[Literature Review] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://www.themoonlight.io/en/review/curing-miracle-steps-in-llm-mathematical-reasoning-with-rubric-rewards"},{"title":"Curing \"Miracle Steps'' in LLM Math Reasoning with Rubric Rewards | OpenReview","url":"https://openreview.net/forum?id=FGkknrhv09"},{"title":"[2510.07774] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards","url":"https://arxiv.org/abs/2510.07774"},{"title":"[PDF] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Curing-Miracle-Steps-in-LLM-Mathematical-Reasoning-Yuan-Mang/b46e76e1d1a71619a4d2d388f63b80da893575b9"}]

Based on the search results, here's what I found about "miracle steps" in mathematical reasoning:

## Definition and Nature

"Miracle Steps" are abrupt jumps to a correct output without a valid preceding derivation. More specifically, the model often successfully completes a crucial step or arrives at the final answer through a process that appears logically disconnected or incomprehensible to annotators, as if miraculously bypassing the required reasoning.

## Where They Occur

Such patterns enable the model to bypass the challenging steps of proof or computation and arrive at the correct answer through an unjustified reasoning process. The "Miracle Steps" category is highlighted as particularly pervasive in large language model outputs.

## Taxonomy Context

Through manual analysis by four annotators across four benchmarks, researchers established a taxonomy of six distinct failure modes. Within this taxonomy, the rubric mandates explicit logical linkage between steps, and any jump from confusion to an answer—without a valid derivation—fails this criterion.

## Root Cause

The model successfully recalls the final answer but fails to reconstruct a coherent and valid reasoning path to justify it, and this failure in post-hoc rationalization manifests as a logical leap that appears miraculous to human evaluators.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36163438-91d0-4a8c-a4a8-2daddc31e41e",
  "isSidechain": false,
  "promptId": "d00ce7f4-5327-4e89-9fa4-f4d847cd112f",
  "type": "user",
  "uuid": "53d7e6e6-965d-40bc-9ca7-186e856cbc71",
  "toolUseResult": {
    "query": "miracle steps mathematical reasoning where do they occur algebraic logical steps unjustified leaps taxonomy",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QtfaojYvui7CAuXJMSibmj",
        "content": [
          {
            "title": "Curing “Miracle Steps” in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://arxiv.org/html/2510.07774v3"
          },
          {
            "title": "Curing Miracle Steps in LLM Mathematical Reasoning with ...",
            "url": "https://arxiv.org/pdf/2510.07774"
          },
          {
            "title": "CURING “MIRACLE STEPS” IN LLM MATHEMATICAL ...",
            "url": "https://openreview.net/pdf/365c5050a2ce26e04b0f1c843f16e9a72f9c704f.pdf"
          },
          {
            "title": "Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2510.07774v2"
          },
          {
            "title": "(PDF) Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://www.researchgate.net/publication/396372877_Curing_Miracle_Steps_in_LLM_Mathematical_Reasoning_with_Rubric_Rewards"
          },
          {
            "title": "[Literature Review] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://www.themoonlight.io/en/review/curing-miracle-steps-in-llm-mathematical-reasoning-with-rubric-rewards"
          },
          {
            "title": "Curing \"Miracle Steps'' in LLM Math Reasoning with Rubric Rewards | OpenReview",
            "url": "https://openreview.net/forum?id=FGkknrhv09"
          },
          {
            "title": "[2510.07774] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
            "url": "https://arxiv.org/abs/2510.07774"
          },
          {
            "title": "[PDF] Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Curing-Miracle-Steps-in-LLM-Mathematical-Reasoning-Yuan-Mang/b46e76e1d1a71619a4d2d388f63b80da893575b9"
          }
        ]
      },
      "Based on the search results, here's what I found about \"miracle steps\" in mathematical reasoning:\n\n## Definition and Nature\n\n\"Miracle Steps\" are abrupt jumps to a correct output without a valid preceding derivation. More specifically, the model often successfully completes a crucial step or arrives at the final answer through a process that appears logically disconnected or incomprehensible to annotators, as if miraculously bypassing the required reasoning.\n\n## Where They Occur\n\nSuch patterns enable the model to bypass the challenging steps of proof or computation and arrive at the correct answer through an unjustified reasoning process. The \"Miracle Steps\" category is highlighted as particularly pervasive in large language model outputs.\n\n## Taxonomy Context\n\nThrough manual analysis by four annotators across four benchmarks, researchers established a taxonomy of six distinct failure modes. Within this taxonomy, the rubric mandates explicit logical linkage between steps, and any jump from confusion to an answer—without a valid derivation—fails this criterion.\n\n## Root Cause\n\nThe model successfully recalls the final answer but fails to reconstruct a coherent and valid reasoning path to justify it, and this failure in post-hoc rationalization manifests as a logical leap that appears miraculous to human evaluators."
    ],
    "durationSeconds": 6.804638730999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "36163438-91d0-4a8c-a4a8-2daddc31e41e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-29T06:28:03.406Z_

<details><summary>↩ Tool result · `toolu_01YNXUCYbLr717uShqM3mpKW`</summary>

```text
Web search results for query: "GR-Ben general reasoning benchmark process reward model arXiv 2605.01203 2025"

Links: [{"title":"[2605.01203] GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models","url":"https://arxiv.org/abs/2605.01203"},{"title":"GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models","url":"https://arxiv.org/html/2605.01203"},{"title":"[2605.10158] Unsupervised Process Reward Models","url":"https://arxiv.org/abs/2605.10158"},{"title":"[2605.10158v1] Unsupervised Process Reward Models","url":"https://arxiv.org/abs/2605.10158v1"},{"title":"Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/pdf/2507.23317"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"Reward Reasoning Model","url":"https://arxiv.org/pdf/2505.14674"}]

Based on the search results, here's what I found about the GR-Ben paper (arXiv 2605.01203):

## GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models

The paper was submitted on May 7, 2026, with authors including Zhouhao Sun, Xuan Zhang, Xiao Ding, and others.

**Overview:**
Process reward models (PRMs) have exhibited remarkable potential for test-time scaling. However, existing benchmarks primarily focus on mathematical reasoning, thereby failing to comprehensively evaluate the error detection ability of PRMs across diverse reasoning scenarios.

**The GR-Ben Benchmark:**
GR-Ben is a process-level benchmark specifically designed for assessing PRM's performance across two primary reasoning domains (science and logic) and nine subdomains. 

**Motivation:**
Since large language models (LLMs) regularly generate flawed intermediate reasoning steps when tackling a broad spectrum of reasoning and decision-making tasks, PRMs are required to possess capabilities for detecting process-level errors in real-world scenarios.

The paper addresses a critical gap in current PRM evaluation by expanding beyond mathematical reasoning to cover a broader range of reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4facf65b-9c4b-483f-936c-928d5e178e72",
  "isSidechain": false,
  "promptId": "d00ce7f4-5327-4e89-9fa4-f4d847cd112f",
  "type": "user",
  "uuid": "41929922-a4e4-463f-9376-a74c204fe03c",
  "toolUseResult": {
    "query": "GR-Ben general reasoning benchmark process reward model arXiv 2605.01203 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HYjkdGmc22hd54BDsKwMgR",
        "content": [
          {
            "title": "[2605.01203] GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models",
            "url": "https://arxiv.org/abs/2605.01203"
          },
          {
            "title": "GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models",
            "url": "https://arxiv.org/html/2605.01203"
          },
          {
            "title": "[2605.10158] Unsupervised Process Reward Models",
            "url": "https://arxiv.org/abs/2605.10158"
          },
          {
            "title": "[2605.10158v1] Unsupervised Process Reward Models",
            "url": "https://arxiv.org/abs/2605.10158v1"
          },
          {
            "title": "Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner",
            "url": "https://arxiv.org/pdf/2507.23317"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/pdf/2501.03124"
          },
          {
            "title": "Reward Reasoning Model",
            "url": "https://arxiv.org/pdf/2505.14674"
          }
        ]
      },
      "Based on the search results, here's what I found about the GR-Ben paper (arXiv 2605.01203):\n\n## GR-Ben: A General Reasoning Benchmark for Evaluating Process Reward Models\n\nThe paper was submitted on May 7, 2026, with authors including Zhouhao Sun, Xuan Zhang, Xiao Ding, and others.\n\n**Overview:**\nProcess reward models (PRMs) have exhibited remarkable potential for test-time scaling. However, existing benchmarks primarily focus on mathematical reasoning, thereby failing to comprehensively evaluate the error detection ability of PRMs across diverse reasoning scenarios.\n\n**The GR-Ben Benchmark:**\nGR-Ben is a process-level benchmark specifically designed for assessing PRM's performance across two primary reasoning domains (science and logic) and nine subdomains. \n\n**Motivation:**\nSince large language models (LLMs) regularly generate flawed intermediate reasoning steps when tackling a broad spectrum of reasoning and decision-making tasks, PRMs are required to possess capabilities for detecting process-level errors in real-world scenarios.\n\nThe paper addresses a critical gap in current PRM evaluation by expanding beyond mathematical reasoning to cover a broader range of reasoning tasks."
    ],
    "durationSeconds": 7.551846752999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4facf65b-9c4b-483f-936c-928d5e178e72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 82 · 2026-05-29T06:28:03.413Z_

```json
{
  "parentUuid": "41929922-a4e4-463f-9376-a74c204fe03c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "2b2766d8-a55f-4de5-91de-1b9c173b3e55",
  "timestamp": "2026-05-29T06:28:03.413Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 83 · 2026-05-29T06:29:49.977Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me assess the search results:

1. **GR-Ben** ✅ Confirmed. arXiv:2605.01203, May 2026. Covers science and logic reasoning, 9 subdomains. Relevant as a complementary benchmark, but it's very new (May 2026) and may not be widely adopted yet. I'll consider adding it as a nice-to-have, but not make it mandatory.

2. **Miracle steps taxonomy** ✅ The RRM paper confirms miracle steps are "abrupt jumps to correct output without valid preceding derivation" and that they're about "bypassing challenging steps of proof or computation." The key insight for 发掘 Point 1 is that miracle steps tend to occur at the "challenging steps" - these are exactly the steps where formal derivation matters most. 

The search doesn't directly confirm that miracle steps concentrate in algebraic or logical step types specifically. The RRM taxonomy suggests miracle steps bypass challenging steps, but those challenging steps might actually be the hardest ones to formalize rather than the most formalizable ones. So my hypothesis that formal coverage concentrates on miracle-step-prone steps needs validation rather than being treated as established fact.

Now I'm working through my integration decisions. For the first point about formal coverage, I'll treat it as a testable hypothesis in my experimental plan rather than a stated claim—that's more scientifically honest. For the second point, reframing Contribution 1 from "Z3 is sound" to "reliable pipeline for routing" is a strong move since reviewers will dismiss the soundness claim as obvious. I'll adopt that. The third point about a trivial alternative with roundtrip verification is worth exploring further.

Both arguments hold weight—roundtrip verification isn't perfect, and there are real compute savings from avoiding the 72B autoformalization step on non-formalizable problems. I'll strengthen this argument. The intrinsic versus operational formalizability distinction adds rigor without major novelty, so I'll include it briefly in the approach section. For Contribution 3, merging it into Contribution 2 seems like the safest path since the alternatives like "formalizability-guided confidence calibration" are too speculative without experimental validation.

On the agent evaluation front, the three-tier fallback from Round 2 was too weak. The upgrade to self-built evaluation with 500-800 steps and multiple annotators using Fleiss' kappa, plus synthetic adversarial miracle steps and PRMBench as backup, is substantially stronger. The roundtrip verification ablation is essential since it's a core component, and I need to address the 72B compute fairness concern properly.

The roundtrip verification paper only covers traffic rules, so I should either run a pilot study on math domains or be transparent about that limitation. The coverage-conditioned analysis and per-benchmark breakdowns will help with the soundness coverage question. GR-Ben is too new to require, but I can mention it as a potential addition.

Both reviewers are clearly in refinement mode now—their feedback is converging on hardening the experimental rigor rather than fundamental restructuring.

The core proposal structure remains solid, and the changes we're making (merging contributions, adding synthetic ablations, testing the 7B autoformalization) are incremental improvements. I think we've reached convergence and should move toward execution rather than another round of iteration.

On the quality side, the three core novelties are holding up well: the reliable pipeline for routing steps to formal verification, the learned context-dependent formalizability routing, and the clear differentiation from VERGE, LogicReward, and FIRMA. Now I need to assess the significance of the work.

The conditional soundness guarantee is honest and well-framed, and the coverage-concentration hypothesis—that formal coverage correlates with steps prone to miracle-step generation—could add real significance if the experiments validate it. The intrinsic versus operational formalizability distinction also brings conceptual depth. That said, the fundamental constraint remains: autoformalization faithfulness sits around 43%, which limits effective coverage to roughly 20-30%, capping the idea's potential around 48-50%.

For the experimental side, I'm confident in the coverage: comprehensive baselines across neural, formal, hybrid, and compute-matched approaches, eight ablations covering routing, roundtrip validation, label noise, and autoformalizer scaling, and evaluation across ProcessBench, PRMBench, Best-of-N, OOD testing on GPQA-Diamond, plus our miracle-step analysis using both self-built and synthetic data.

On fairness, I've addressed it through Pareto curves that include autoformalization cost and compared 7B versus 72B autoformalizers. Coverage reporting is honest with per-benchmark breakdowns and coverage-conditioned analysis. The main remaining gap is that roundtrip verification in the math domain hasn't been tested yet, though the planned pilot study should address that.

The probability hasn't actually shifted much from Round 2—still sitting at 35-48% with a median of 42%. That convergence is telling: the improvements are solidifying the proposal but not materially expanding the ceiling. The autoformalization coverage limitation is the hard constraint keeping the effective soundness capped at 20-30%.

Now I'm checking whether I've actually hit convergence. The discovery and remediation phases are still finding things, so that criterion isn't met. Round 2 had substantive changes with the three-layer pipeline, while Round 3 is mostly refinement—borderline on that front. The median probability has been flat from Round 2 to Round 3 at 42%, which is one signal of stabilization. I haven't reached Round 5 yet, so that threshold doesn't apply. The lower bound ticked up slightly because the experimental design is more robust now, but it's marginal movement.

The clearest indicator is that Round 3's suggestions are all about hardening and refinement rather than structural changes, and both workers are finding increasingly marginal items. I think convergence is justified. Let me write out the final clean proposal now, then I'll need to clarify the output format—whether I submit this as an iteration or wait for the system to call me as 角色 C for the final consolidated output. I need to clarify the flow here—when convergence happens, I should output the 角色 B summary with 决策=收敛 and the clean proposal version. The 角色 C final output with the optimization plan comparing to the original proposal gets triggered only when the system explicitly tells me the process is complete, so for now I'll stick with the 角色 B format and let the system guide what comes next. I need to decide whether to include the final proposal version when converging. The instructions say "若继续" (if continuing) for the clean proposal block, which suggests I shouldn't output it when deciding to converge. So I'll output 角色 B's decision as 收敛, then transition directly to 角色 C to provide the optimization plan comparing against the original proposal with specific modifications, risk analysis, and implementation assessment. state to this original and list specific modifications.

OK let me write this out. This will be a long but important output.

Let me organize the modifications relative to the original:

**Title change**: "Miracle Step Detection" → "Sound Miracle Step Detection"

**Core Problem**: 
- Added explicit mention of LogicReward's try-and-fallback limitation
- Added roundtrip verification as part of the solution

**Research Opportunity**: 
- Significantly expanded with precise citations and data points
- Added Risk-Controlled Lean-as-Judge data (43% faithfulness, 28% coverage)

**Key Insight section**: NEW - conditional formal soundness framing

**Contributions**: Restructured from implicit to explicit three (now two) contributions:
1. Conditional sound miracle detection via three-layer pipeline
2. Learned context-dependent formalizability routing (subsuming asymmetric cost design)

**Research Landscape**: Massively expanded with ThinkPRM, R-PRM, FIRMA, autoformalization limits

**Proposed Approach**: From single paragraph to detailed three-layer pipeline

**Evaluation Design**: From bare-bones to comprehensive (baselines, ablations, metrics, compute fairness, OOD, honest coverage)

**Compute Budget**: NEW section

**Key References**: Expanded from 6 to 14+

Now I'm working through the implementation details—I need to estimate the computational requirements, which looks like a single-node setup with 8 H100s running training in under a day and evaluation in about five days. For data, I'm pulling from publicly available sources like FoVer, GenPRM, and various benchmarks, plus I'll need to annotate around 500 to 800 miracle steps with multiple annotators to establish ground truth.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b2766d8-a55f-4de5-91de-1b9c173b3e55",
  "isSidechain": false,
  "requestId": "req_011CbWPMzgejQ5AcVgUVv8Qw",
  "type": "assistant",
  "uuid": "b4547087-654d-4efb-b30f-6698ee48390c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAdfoDjZ7q4oD7VRBhqPZr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 879,
      "cache_creation_input_tokens": 1973,
      "cache_read_input_tokens": 78068,
      "output_tokens": 3644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 879,
          "output_tokens": 3644,
          "cache_read_input_tokens": 78068,
          "cache_creation_input_tokens": 1973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1973
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

_source line 84 · 2026-05-29T06:29:50.120Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019rm4cH4XwnFpjMTMf71KLb`</summary>

```json
{
  "query": "roundtrip verification autoformalization mathematics domain Lean Z3 faithfulness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4547087-654d-4efb-b30f-6698ee48390c",
  "isSidechain": false,
  "requestId": "req_011CbWPMzgejQ5AcVgUVv8Qw",
  "type": "assistant",
  "uuid": "1b3a4e15-32e3-46ea-952a-d02f5f83c44d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NAdfoDjZ7q4oD7VRBhqPZr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 879,
      "cache_creation_input_tokens": 1973,
      "cache_read_input_tokens": 78068,
      "output_tokens": 3644,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 879,
          "output_tokens": 3644,
          "cache_read_input_tokens": 78068,
          "cache_creation_input_tokens": 1973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1973
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

_source line 85_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide a thorough assessment. Let me synthesize my findings.  ---  【状态】:…",
  "leafUuid": "1b3a4e15-32e3-46ea-952a-d02f5f83c44d",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 86_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Tool result

_source line 87 · 2026-05-29T06:30:01.330Z_

<details><summary>↩ Tool result · `toolu_019rm4cH4XwnFpjMTMf71KLb`</summary>

```text
Web search results for query: "roundtrip verification autoformalization mathematics domain Lean Z3 faithfulness 2025 2026"

Links: [{"title":"Faithful Autoformalization via Roundtrip Verification and Repair","url":"https://arxiv.org/html/2604.25031"},{"title":"3rd AI for Math Workshop @ ICML 2026","url":"https://ai4math2026.github.io/"},{"title":"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings","url":"https://arxiv.org/html/2510.15681v1"},{"title":"RLMEval: Evaluating Autoformalization on Research-Level Mathematics","url":"http://aitp-conference.org/2025/abstract/AITP_2025_paper_8.pdf"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"arXiv:2505.18492v3 [cs.AI] 3 Jun 2025","url":"https://arxiv.org/pdf/2505.18492"},{"title":"Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics","url":"https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"}]

Based on the search results, I found several highly relevant papers and resources on autoformalization with roundtrip verification and faithfulness evaluation in mathematics using Lean and related tools:

## Key Findings:

**Roundtrip Verification and Faithfulness:**

Recent systems like ProofBridge iteratively repair Lean proofs from type-checker feedback, though traditional approaches treat verifier feedback as binary accept/reject signals without diagnosing which pipeline stage introduced errors. Round-trip correctness has been used as an evaluation signal in code generation when checking equivalence via test suites.

**Autoformalization Evaluation Challenges:**

A statement can type-check but not correspond to the intended theorem, making faithfulness evaluation more subtle than simple type-correctness checks. Existing autoformalization evaluation methods like BLEU, compiler typecheck, and bidirectional equivalence checking assume a reference formalization exists for comparison.

**Recent Advances (2025-2026):**

In 2025, multiple independent systems achieved gold-medal equivalent performance with formally verified Lean 4 proofs, offering the crucial advantage that no human verification is required. Recent work in autoformalization uses re-informalization combined with consistency checks, ranking candidates using symbolic equivalence and embedding similarity over re-informalized text.

The search results include papers from April-June 2026 addressing the gap between formal and informal mathematical reasoning through various verification and faithfulness evaluation approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b3a4e15-32e3-46ea-952a-d02f5f83c44d",
  "isSidechain": false,
  "promptId": "d00ce7f4-5327-4e89-9fa4-f4d847cd112f",
  "type": "user",
  "uuid": "ef261ad3-bb5e-4ddd-a4b7-825e3b068d17",
  "toolUseResult": {
    "query": "roundtrip verification autoformalization mathematics domain Lean Z3 faithfulness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013TKzQdUEGNhqyLdyUWvt58",
        "content": [
          {
            "title": "Faithful Autoformalization via Roundtrip Verification and Repair",
            "url": "https://arxiv.org/html/2604.25031"
          },
          {
            "title": "3rd AI for Math Workshop @ ICML 2026",
            "url": "https://ai4math2026.github.io/"
          },
          {
            "title": "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings",
            "url": "https://arxiv.org/html/2510.15681v1"
          },
          {
            "title": "RLMEval: Evaluating Autoformalization on Research-Level Mathematics",
            "url": "http://aitp-conference.org/2025/abstract/AITP_2025_paper_8.pdf"
          },
          {
            "title": "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning",
            "url": "https://arxiv.org/html/2604.19459"
          },
          {
            "title": "arXiv:2505.18492v3 [cs.AI] 3 Jun 2025",
            "url": "https://arxiv.org/pdf/2505.18492"
          },
          {
            "title": "Major Breakthroughs in Lean 4-Based Auto-Formalized Mathematics",
            "url": "https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Major%20Breakthroughs%20in%20Lean%204-Based%20Auto-Formalized%20Mathematics.html"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers and resources on autoformalization with roundtrip verification and faithfulness evaluation in mathematics using Lean and related tools:\n\n## Key Findings:\n\n**Roundtrip Verification and Faithfulness:**\n\nRecent systems like ProofBridge iteratively repair Lean proofs from type-checker feedback, though traditional approaches treat verifier feedback as binary accept/reject signals without diagnosing which pipeline stage introduced errors. Round-trip correctness has been used as an evaluation signal in code generation when checking equivalence via test suites.\n\n**Autoformalization Evaluation Challenges:**\n\nA statement can type-check but not correspond to the intended theorem, making faithfulness evaluation more subtle than simple type-correctness checks. Existing autoformalization evaluation methods like BLEU, compiler typecheck, and bidirectional equivalence checking assume a reference formalization exists for comparison.\n\n**Recent Advances (2025-2026):**\n\nIn 2025, multiple independent systems achieved gold-medal equivalent performance with formally verified Lean 4 proofs, offering the crucial advantage that no human verification is required. Recent work in autoformalization uses re-informalization combined with consistency checks, ranking candidates using symbolic equivalence and embedding similarity over re-informalized text.\n\nThe search results include papers from April-June 2026 addressing the gap between formal and informal mathematical reasoning through various verification and faithfulness evaluation approaches."
    ],
    "durationSeconds": 11.204701005999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1b3a4e15-32e3-46ea-952a-d02f5f83c44d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 88 · 2026-05-29T06:30:46.670Z_

<details><summary>Logged reasoning block</summary>

```text
Good. The search confirms that roundtrip verification in math is still nascent - most work is on simple type-checking or binary accept/reject signals. The math domain roundtrip verification challenge is real and acknowledged. This supports the 补救 agent's concern (defect 4) about roundtrip verification feasibility in math domain.

Now I have all the information I need. Let me write the final integration output.

Let me also think about whether to include GR-Ben. It's May 2026, very recent. Adding it as a nice-to-have / optional extension is fine but I shouldn't make it a core requirement. 

The logic reasoning domain is where FormalRoute-PRM should really excel, so it makes sense as an optional addition. Now I need to decide which suggestions to actually adopt versus defer. Since the goal is convergence, I should focus on changes that materially strengthen the proposal rather than incorporating every suggestion. The key ones to adopt are the ones with real impact on the review outcome - like reframing Contribution 1 as a pipeline contribution rather than just a Z3 contribution.

Looking at what needs to change: I should merge Contribution 3 into Contribution 2 to keep the list tight, upgrade the miracle step evaluation to use primary self-built and synthetic data, add the roundtrip verification ablation for component isolation, include a 7B autoformalizer ablation to address compute fairness concerns, and acknowledge the math-domain risk with a pilot study. These are the essential changes. Beyond that, I can adopt the intrinsic versus operational formalizability distinction for added rigor, and the coverage-concentration hypothesis, but those are secondary strengthening moves rather than must-haves. I've reviewed the checklist of improvements and confirmed which ones are essential versus optional. Now I'm ready to structure the output: first, I'll provide the 角色 B iteration summary with a convergence decision, then move directly into the 角色 C final deliverable since we've reached the median threshold. I'll organize the optimization plan by comparing it against the original proposal and detailing the specific changes section by section, starting with the title refinement. Step Detection"
2. **Core Problem**: Expanded to include LogicReward's limitation, roundtrip verification need
3. **Research Opportunity**: Expanded with precise data (43% faithfulness, 28% coverage)
4. **NEW: Key Insight section** (conditional formal soundness)
5. **NEW: Contributions section** (2 explicit contributions)
6. **Research Landscape**: Expanded with ThinkPRM, R-PRM, FIRMA, autoformalization limits, ARES, Do LLMs Game Formalization
7. **Proposed Approach**: From single paragraph → three-layer pipeline with detailed specification
8. **NEW: Evaluation Design** (comprehensive benchmarks, baselines, 8 ablations, metrics, compute fairness, OOD, honest coverage, miracle step evaluation strategy)
9. **NEW: Compute Budget section**
10. **Key References**: 6 → 14+

The main risks I'm concerned about are the autoformalization bottleneck potentially dropping effective coverage to 20-30%, whether roundtrip verification actually works in the math domain, and whether we'll see meaningful gains over pure neural PRMs. For the implementation, I'm planning a single-node setup with 8 H100s, where autoformalization inference dominates the cost at around 72B model inference, with the full pipeline taking less than a day for training and under five days for evaluation. I'll use public datasets like FoVer, ProcessBench, and MATH-500, plus I need to annotate 500-800 miracle steps for human evaluation. steps, 3 annotators, ~2-3 person-weeks
  - Router label quality audit: 200-300 samples, 1-2 person-days
  - Oracle formalizability labels: 100-200 examples, ~1 person-week
- Training: Qwen3-8B LoRA fine-tuning
- New Benchmark: Self-built miracle step test set (500-800 steps) + synthetic adversarial examples
- Timeline: ~10-14 weeks
  - Weeks 1-3: Infrastructure setup, data preparation, autoformalization pipeline
  - Weeks 3-5: Router training, pilot studies (roundtrip verification, label quality)
  - Weeks 5-8: Main experiments (benchmarks, baselines, ablations)
  - Weeks 8-10: Human annotation, miracle step evaluation
  - Weeks 10-12: Analysis and paper writing
  - Weeks 12-14: Buffer and revisions

I think I have the full plan mapped out now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef261ad3-bb5e-4ddd-a4b7-825e3b068d17",
  "isSidechain": false,
  "requestId": "req_011CbWPWhSZtDcENxCeSTFcT",
  "type": "assistant",
  "uuid": "c39983f6-242f-4079-be32-72380c82b001",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsQ2PM94q5yAh8adejPQD9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5238,
      "cache_read_input_tokens": 80041,
      "output_tokens": 6932,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6932,
          "cache_read_input_tokens": 80041,
          "cache_creation_input_tokens": 5238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5238
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

_source line 89 · 2026-05-29T06:32:51.149Z_

All cross-validation complete. Let me compile the full Round 3 integration and convergence decision.

【阶段】: 迭代第 3 轮

【交叉验证调研】:
1. **GR-Ben (arXiv:2605.01203) 是否存在且相关**（补救 defect 6）→ 已验证 ✅。May 2026 发表，覆盖科学+逻辑推理 9 个子域的 PRM benchmark。现有 PRM 在数学以外域显著更弱。相关但非常新，作为 optional 纳入。
2. **Miracle steps 是否集中在 formalizable 步骤类型**（发掘 point 1）→ 部分验证。RRM (arXiv:2510.07774) 定义 miracle steps 为"bypassing the challenging steps of proof or computation"——但"challenging steps"并不必然等同于"formalizable steps"。此论点是合理假设而非已证事实。**标注：作为 hypothesis + validation plan 纳入，不作为 stated fact。**
3. **Roundtrip verification 在数学域的适用性**（补救 defect 4）→ 搜索确认 roundtrip verification (arXiv:2604.25031) 仅在交通规则域评测。数学域 autoformalization faithfulness 挑战更大（复杂符号操作、隐式引理）。数学域适用性是实际风险。**标注：需 pilot study。**

【发掘 agent 有效建议采纳】:
- **Point 1（formal coverage 集中在 miracle-step-prone steps）**: 部分采纳。论点合理但无直接文献支撑——miracle steps 是"bypassing challenging steps"不等于"bypassing formalizable steps"。采纳为 **hypothesis + experimental validation plan**（在 miracle step 标注集上分析 formal branch coverage 与 miracle step 的 overlap），不作为 proposal 的 stated claim。已验证/作为假设纳入。
- **Point 2（reframe Contribution 1：pipeline 贡献而非 Z3 贡献）**: 采纳。"Z3 is sound"是已知事实，本文贡献在于构建了可靠的 routing + roundtrip gating pipeline 使 conditional soundness 在 PRM 场景下首次 achievable。防止审稿人将贡献归因于 Z3。已验证。
- **Point 3（trivial alternative 的更强回应）**: 采纳。两层论证：(a) roundtrip verification 非完美——Do LLMs Game Formalization (arXiv:2604.19459) 显示 axiom fabrication 和 premise mistranslation 可逃过检查；learned router 作为第一道防线捕获这些。(b) 避免对 ~50-70% non-formalizable steps 做 72B autoformalization 的 compute savings 是非平凡的。已验证。
- **Point 4（intrinsic vs. operational formalizability）**: 采纳。简要区分两个概念层面，router 学 operational formalizability，但 contribution 论证建立在 intrinsic formalizability 之上。增加概念严谨性，不大量展开。已验证/合理推断。
- **Point 5（merge Contribution 3 into Contribution 2）**: 采纳。Asymmetric cost-aware threshold 是 cost-sensitive classification 标准技术，不够撑独立贡献。降级为 Contribution 2 的实现细节。Contributions 精简为 2 个强贡献。已验证。

【补救 agent 有效建议采纳】:
- **Defect 1（miracle step evaluation 不足）**: 采纳。升级方案：(a) 自建 500-800 step 标注集为 **primary evaluation**，3 标注者 + Fleiss' kappa；(b) 新增 **synthetic adversarial miracle steps**（在正确推理链中人为替换步骤为 unjustified leaps）；(c) PRMBench soundness 子集降为 supplementary reference。已验证。
- **Defect 2（roundtrip verification ablation 缺失）**: 采纳。新增 ablation: with vs. without roundtrip verification，量化 roundtrip gating 对 false alarm filtering 和 effective soundness 的贡献。已验证。
- **Defect 3（72B autoformalization compute fairness）**: 采纳。新增 7B vs. 72B autoformalizer ablation，在 Pareto curve 上标注两个配置。Risk-Controlled (arXiv:2605.28365) 已报告 7B 仅 43% faithfulness，此 ablation 直接量化 model scale 的影响。已验证。
- **Defect 4（roundtrip verification 数学域可行性）**: 采纳。增加 pilot study 计划（200-500 steps from FoVer data），明确报告数学域 pass rate 并讨论与交通规则域的 gap。已验证（roundtrip paper 确实仅在交通规则域评测）。
- **Defect 5（effective coverage 可能过低）**: 采纳。增加 per-benchmark coverage breakdown + coverage-conditioned miracle detection analysis。预设 meaningful coverage threshold（>15%）。已验证。
- **Defect 6（GR-Ben）**: 部分采纳。作为 optional 扩展提及（逻辑推理子域可能是 formal verification 的天然优势域），但不作为必需 benchmark。标注：Very new (May 2026)，优先级低。

【本轮 proposal 主要变更】:

**Idea 层面变更:**
- Contribution 1 reframing：从 "formal soundness guarantee" 到 "first practical pipeline making conditional formal soundness achievable in PRM verification"
- Contribution 3 merged into Contribution 2：asymmetric threshold 降为 C2 实现细节，contributions 精简为 2 个
- 新增 intrinsic vs. operational formalizability 概念区分
- 新增 coverage-concentration hypothesis 作为待验证的 significance argument
- 强化 trivial alternative 防御（roundtrip imperfection + compute savings 双论证）

**实验层面变更:**
- Miracle step evaluation 从三层 fallback 升级为 primary self-built (500-800 steps) + synthetic adversarial
- 新增 roundtrip verification ablation (Ablation 8)
- 新增 7B vs. 72B autoformalizer ablation (Ablation 9)
- 新增 roundtrip verification 数学域 pilot study
- 新增 coverage-conditioned miracle detection analysis
- Ablation 总数从 7 增至 9

【idea 质量评估】: Novelty=强（learned context-dependent formalizability routing 无先例确认；三层 pipeline 设计含 roundtrip gating 是新架构；贡献精简为 2 个，每个都有足够 novelty 承载力；与 VERGE/LogicReward/FIRMA 差异化清晰） Significance=中-强（conditional soundness + coverage-concentration hypothesis 如果验证成立则推向强，但 effective coverage ~20-30% 构成 significance 天花板；honest reporting 增加 credibility） → idea 天花板约 48-50%

【实验完备性评估】: Technical Soundness=中-强（9 个 ablation 覆盖全面；miracle step 评测方案 robust；compute fairness 含 7B/72B ablation；roundtrip pilot study 主动应对可行性风险；主要残余风险：数学域 roundtrip verification 的实际效果和 effective coverage 的具体数值） → 地板约 36%

【当前概率估计】: [36% - 48%] 中位 42%

【决策】: 收敛

【决策理由】: 三轮迭代的收敛信号明确：(1) 连续两轮（Round 2→3）中位概率持平于 42%，无上升空间；(2) 两个 worker 均已转入"硬化/精炼"模式——发掘 agent 的 5 点全部是 framing refinement 和 defensive positioning，无新 angle 发现；补救 agent 的 6 点全部是 secondary gaps 和 nice-to-haves；(3) 核心 idea 结构（三层 pipeline + 两个 contribution）和实验框架（baseline matrix + 9 ablations + 多层 evaluation）已稳定，第 4 轮大概率只产出 cosmetic 调整。Proposal 已达到足够的质量和完整度进入实验执行阶段。

---

## 角色 C：最终输出

【优化方案】

以下为对比**原始 proposal**的完整修改建议列表：

1. **[标题]** — "Miracle Step Detection" → "Sound Miracle Step Detection" — 体现 conditional soundness guarantee 的核心差异化，命中 Novelty
   
2. **[Core Problem / 问题定位]** — 扩展问题描述，明确纳入 LogicReward 的 try-and-fallback 局限性和 roundtrip verification 需求，将问题从 "routing is unaddressed" 锐化为 "reliable routing + faithfulness gating is unaddressed" — 命中 Novelty + Significance

3. **[新增 Key Insight 章节]** — 新增独立章节阐述核心洞察：miracle step detection ≡ Z3 derivability failure（在 faithfully-formalized subset 上的 near-definitional correspondence）。明确 conditional qualifier（soundness 仅在 "router 正确 × roundtrip 通过 × Z3 correct" 的交集上成立），引用 Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 的 43% faithfulness / 28% coverage 和 Do LLMs Game Formalization (arXiv:2604.19459) 的 unfaithfulness 模式分析。将诚实的 limitation 转化为成熟的 contribution — 命中 Novelty + Significance + Technical Soundness

4. **[Contributions 重构]** — 原始 proposal 无显式 contribution list。重构为 2 个精简强贡献：
   - C1: "First practical pipeline making conditional formal soundness achievable in PRM verification"（强调 pipeline 贡献而非 Z3 已知属性）
   - C2: "Learned context-dependent formalizability routing"（subsumes asymmetric cost-aware threshold as implementation detail；展开 non-triviality 论证：predecessor context, autoformalization capability boundary, proof position effect；区分 intrinsic vs. operational formalizability）
   — 命中 Novelty

5. **[Research Landscape 大幅扩展]** — 原始 proposal 仅简要提及 5 个 related works。扩展为结构化的 5 类讨论：
   - 新增 ThinkPRM (arXiv:2504.16828)、R-PRM (EMNLP 2025, arXiv:2503.21295) 作为 neural PRM SOTA
   - 新增 FIRMA (MathNLP 2025) 的 complexity router 差异化讨论
   - 新增 autoformalization limits 小节（Risk-Controlled, Do LLMs Game Formalization, Roundtrip Verification）
   - 明确 LogicReward 作为 RL framework（非独立 PRM）的性质，避免 apples-to-oranges comparison
   — 命中 Related Work 完整性 + Novelty 差异化

6. **[Proposed Approach 从段落到三层 pipeline]** — 原始 proposal 仅有一段概述。重构为详细的三层 pipeline 设计：
   - Layer 1: Formalizability Router（Qwen3-8B classifier，明确 label 定义三分类，context-dependent input）
   - Layer 2: Roundtrip Faithfulness Verification（gatekeeper，使用 Qwen2.5-Math-72B-Instruct autoformalization + roundtrip check，引用 arXiv:2604.25031）
   - Layer 3: Verification（formal branch: Z3 predecessor-derivability; neural branch: GenPRM-7B + Platt scaling calibration）
   - Output: 四级 verification confidence tier
   — 命中 Technical Soundness + Novelty

7. **[新增完整 Evaluation Design 章节]** — 原始 proposal 仅有一句 "Evaluate on ProcessBench, PRMBench, and RRM miracle taxonomy"。扩展为：
   - **Benchmarks + metrics**: ProcessBench (F1 + AUROC), PRMBench (PRMScore + error-type breakdown), Best-of-N (MATH-500, AIME24, N=8/16/64), GPQA-Diamond (OOD), miracle step detection (self-built 500-800 step primary + synthetic adversarial + PRMBench supplementary)
   - **Baseline matrix**: 10+ baselines 分 5 类（pure neural, pure formal, hybrid including naive try-and-fallback, LLM-as-Judge, compute-matched）
   - **9 ablation studies**: routing variants (formal-only, neural-only, random, oracle, threshold sweep, try-formal-first), label noise analysis, roundtrip verification ablation, 7B vs. 72B autoformalizer ablation
   - **Compute fairness**: Pareto curve including autoformalization cost, token-budget-normalized comparison following ThinkPRM paradigm
   - **Router analysis**: in-domain vs. OOD accuracy, few-shot adaptation, oracle ceiling, coverage statistics
   - **Honest coverage reporting**: per-benchmark effective soundness coverage + coverage-conditioned miracle detection analysis
   - **Pilot study**: roundtrip verification 数学域可行性验证（200-500 FoVer steps）
   — 命中 Technical Soundness（从致命缺陷到接近完备）

8. **[新增 Compute Budget 章节]** — 原始 proposal 仅说 "single-node H100"。新增详细估算：router training (4-8 GPU-hours), autoformalization (72B inference, dominant cost), Z3 (negligible), total (<5 days on 8×H100) — 命中 Feasibility

9. **[Key References 扩展]** — 从 6 条扩展至 14+ 条，新增 ThinkPRM, R-PRM, FIRMA, Risk-Controlled (with arXiv:2605.28365), Do LLMs Game Formalization (arXiv:2604.19459), Roundtrip Verification (arXiv:2604.25031), PRoSFI (arXiv:2603.29500), PRMBench (arXiv:2501.03124) — 命中 Related Work 完整性

10. **[Significance framing]** — 新增 coverage-concentration hypothesis（formal branch coverage 可能 disproportionately 覆盖 miracle-step-prone 步骤）作为待验证假设 + 实验验证计划 — 命中 Significance

11. **[Trivial alternative 防御]** — 原始 proposal 未 address。新增三重防御论证：(a) router 减少 formal branch 对 non-formalizable 步骤的系统性假阳性（FoVer documented overly-strict behavior），(b) roundtrip verification 非完美，learned router 作为第一道防线捕获逃过 roundtrip 的 unfaithfulness，(c) 避免对 50-70% non-formalizable 步骤做 72B autoformalization 的 compute savings — 命中 Novelty 防御

【主要风险】:
1. **Autoformalization bottleneck 导致 effective soundness coverage 过低**（~20-30%）。如果覆盖率低于 15%，"conditional soundness" 的实际价值会被审稿人严重质疑。缓解策略：coverage-conditioned analysis 展示 formal branch 在覆盖范围内的高精度 + coverage-concentration hypothesis 验证 + 诚实报告。
2. **Try-and-fallback baseline 可能表现接近 learned routing**。如果 ablation 6 显示 trivial alternative 与 FormalRoute-PRM 差距不大，核心 contribution (C2) 的增量价值将被削弱。缓解策略：compute savings 论证 + false alarm reduction 的定量比较 + roundtrip imperfection 的定量分析。

【实施评估】:
- **计算资源**: 单节点 8×H100（或等价）。Router 训练 ≈4-8 GPU-hours（Qwen3-8B LoRA）。主要推理开销为 Qwen2.5-Math-72B-Instruct autoformalization（占总 compute ~60-70%）。GenPRM-7B 推理为标准 7B inference。Z3 求解毫秒级，可忽略。总训练 <1 天，全量评估 pipeline <5 天。
- **数据需求**: FoVer 公开数据（~80K Z3-verified labels）用于 router 训练；ProcessBench、PRMBench（ACL 2025）、MATH-500、AIME24 均公开可得；GPQA-Diamond 公开可得。RRM miracle step annotations 需确认可用性（备选方案已设计）。
- **人工介入**: (1) Miracle step 标注集构建：500-800 步骤，3 名标注者，Fleiss' kappa，约 2-3 人周；(2) Router label quality audit：200-300 样本人工验证，约 1-2 人天；(3) Oracle formalizability labels：100-200 examples，约 1 人周；(4) Synthetic adversarial miracle steps 构造：需领域专家设计模板，约 1 人周。总人工约 5-6 人周。
- **训练需求**: (1) Qwen3-8B formalizability classifier LoRA fine-tuning（~80K 样本，4-8 GPU-hours）；(2) 不需要训练 GenPRM-7B（使用开源权重）；(3) 不需要训练 autoformalization model（使用 Qwen2.5-Math-72B-Instruct 预训练权重）。训练需求轻量。
- **新 Benchmark**: 需构建 miracle step detection test set（500-800 步骤 + synthetic adversarial examples）。这是唯一需要自建的评测资源，其余全部使用现有公开 benchmark。
- **预估周期**: 10-14 周。
  - Weeks 1-3: 基础设施搭建、autoformalization pipeline 开发、FoVer 数据处理
  - Weeks 3-5: Router 训练、roundtrip verification 数学域 pilot study（200-500 steps）、label quality audit
  - Weeks 5-8: 主实验（benchmarks × baselines × ablations）
  - Weeks 8-10: 人工标注（miracle step test set）、miracle step 评测
  - Weeks 10-12: 分析、撰写
  - Weeks 12-14: 缓冲、修订
  
  关键路径：autoformalization pipeline 开发 + roundtrip verification pilot study 是最早需要完成的，因为 pilot study 结果可能影响 Layer 2 的具体设计（如数学域 pass rate 过低则需调整 faithfulness check 方法）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c39983f6-242f-4079-be32-72380c82b001",
  "isSidechain": false,
  "requestId": "req_011CbWPWhSZtDcENxCeSTFcT",
  "type": "assistant",
  "uuid": "f8c778ce-63c1-4e53-bdb0-e21039c1a7d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NsQ2PM94q5yAh8adejPQD9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5238,
      "cache_read_input_tokens": 80041,
      "output_tokens": 6932,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6932,
          "cache_read_input_tokens": 80041,
          "cache_creation_input_tokens": 5238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5238
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

_source line 90_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide a thorough assessment. Let me synthesize my findings.  ---  【状态】:…",
  "leafUuid": "f8c778ce-63c1-4e53-bdb0-e21039c1a7d5",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 91_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 92_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide a thorough assessment. Let me synthesize my findings.  ---  【状态】:…",
  "leafUuid": "f8c778ce-63c1-4e53-bdb0-e21039c1a7d5",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 93_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 94_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 95 · 2026-05-29T06:32:52.856Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:32:52.856Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "content": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。"
}
```

---

### Runtime record

_source line 96 · 2026-05-29T06:32:52.856Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:32:52.856Z",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

## Round 5

4 recorded events

### User

_source line 97 · 2026-05-29T06:32:52.890Z_

【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8c778ce-63c1-4e53-bdb0-e21039c1a7d5",
  "isSidechain": false,
  "promptId": "15a4ef18-8bfc-4d91-afec-8c60649d1677",
  "type": "user",
  "uuid": "cdbbedff-904a-4c9e-8290-ffc576f08af8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 98 · 2026-05-29T06:35:05.135Z_

【优化方案】

1. **[标题]** — "Formally-Routed Process Reward Models for Miracle Step Detection" → "Formally-Routed Process Reward Models for **Sound** Miracle Step Detection" — 一词之差精确传达 conditional formal guarantee 的核心差异化，命中 Novelty 第一印象

2. **[Core Problem / 问题定位]** — 原始仅列举 formal-only vs. neural-only 的二分，新版增加对 hybrid 现有方案的精准批判：VERGE 的 rule-based routing 是 context-free 且非 learned；LogicReward 的 try-and-fallback 无法区分"步骤不可形式化"与"autoformalization 能力不足"。将问题从"routing unaddressed"锐化为"reliable routing + faithfulness gating unaddressed" — 命中 Novelty（问题定义的精确性）

3. **[新增 Key Insight 章节]** — 原始 proposal 无此章节。新增核心理论洞察：在 faithfully-formalized subset 上，miracle step detection ≡ Z3 derivability failure（near-definitional correspondence）。同时明确 conditional qualifier：soundness 仅在 "router 正确 × autoformalization faithful × Z3 correct" 交集上成立。引用 Risk-Controlled Lean-as-Judge (arXiv:2605.28365) 的 43% faithfulness / 28% coverage 数据和 Do LLMs Game Formalization (arXiv:2604.19459) 的 axiom fabrication / premise mistranslation 两种 unfaithfulness 模式，将诚实的 limitation 量化为成熟的 contribution boundary — 命中 Novelty + Significance + Technical Soundness

4. **[Contributions 重构]** — 原始 proposal 无显式 contribution list，核心主张散落在描述中。重构为 2 个精简强贡献：
   - **C1**: "First practical pipeline making conditional formal soundness achievable in PRM verification" — 三层 pipeline（router → roundtrip gating → formal/neural verification）是系统设计贡献，而非简单声称"Z3 is sound"（已知事实）。强调 pipeline 本身是 novelty 承载点
   - **C2**: "Learned context-dependent formalizability routing" — 展开 non-triviality 论证（predecessor formal context、autoformalization capability boundary、proof position effect 三重 context dependency 使 rule-based 方法在原理上不可行）；区分 intrinsic formalizability（步骤是否原则上可用一阶逻辑表达）与 operational formalizability（当前工具链能否可靠形式化）；subsume asymmetric cost-aware threshold 作为 C2 的实现细节（非独立贡献——cost-sensitive classification 是标准技术）
   - 原始 proposal 若保持 3 个 contribution（含 asymmetric threshold），第 3 个太弱会拉低整体 perceived contribution。精简为 2 个确保每个都有足够 novelty 承载力 — 命中 Novelty

5. **[Research Landscape 大幅扩展]** — 原始仅简要提及 FoVer / GenPRM / ARES / LogicReward / VERGE / RRM 共 6 个工作。扩展为结构化 5 类讨论并新增关键 related works：
   - **新增 neural PRM SOTA**: ThinkPRM (arXiv:2504.16828) — 仅 8K labels 超越 100× 数据的 discriminative PRMs，确立 token-budget-normalized comparison 范式；R-PRM (EMNLP 2025, arXiv:2503.21295) — ProcessBench +13.9 F1 / PRMBench +8.5 F1，当前最强 discriminative PRM
   - **新增 FIRMA (MathNLP 2025, ACL Anthology 2025.mathnlp-main.5)**: complexity router 用于 formal-informal 翻译质量路由，明确差异化——FIRMA 路由为翻译质量服务，本文路由为验证正确性服务，目标函数和训练信号完全不同
   - **新增 autoformalization limits 小节**: Risk-Controlled (arXiv:2605.28365)、Do LLMs Game Formalization (arXiv:2604.19459)、Faithful Autoformalization via Roundtrip Verification (arXiv:2604.25031) — 提供 autoformalization 瓶颈的精确量化和缓解方法论
   - **明确 LogicReward 性质**: 标注为 RL training framework（非独立 PRM），避免 quantitative comparison 中的 apples-to-oranges 问题
   — 命中 Related Work 完整性 + Novelty 差异化防御

6. **[Proposed Approach: 从一段话到三层 pipeline]** — 原始仅有 ~80 字概述（"Train Qwen3-8B...Route...Evaluate"）。重构为详细的三层 pipeline：
   - **Layer 1 — Formalizability Router**: Qwen3-8B classifier，训练标签三分类定义明确（formalizable = Z3 编译成功 AND roundtrip 通过；non-formalizable = autoformalization 失败 OR roundtrip 失败 OR Z3 超时），input = step S_i + predecessor context {S_1,...,S_{i-1}}，threshold 通过 asymmetric cost optimization 设定（favor recall）
   - **Layer 2 — Roundtrip Faithfulness Verification**（全新组件）: 使用 Qwen2.5-Math-72B-Instruct autoformalization → back-translate → semantic equivalence check（arXiv:2604.25031）。未通过 roundtrip 的步骤重定向到 neural branch。此层 gate 住 soundness guarantee
   - **Layer 3 — Verification**: formal branch（roundtrip-verified → Z3 predecessor-derivability）; neural branch（GenPRM-7B + Platt scaling calibration）
   - **Output**: 四级 verification confidence tier（roundtrip-verified Z3 > Z3-only > neural > uncertain）
   — 命中 Technical Soundness（从模糊概述到可执行设计）

7. **[新增完整 Evaluation Design 章节]** — 原始仅一句 "Evaluate on ProcessBench, PRMBench, and RRM miracle taxonomy with honest coverage reporting"。扩展为完整的实验设计：

   **7a. Benchmarks + Metrics（从 3 benchmark 到 5+ 且每个有明确指标）**:
   - ProcessBench: F1（对齐 GenPRM/R-PRM）+ AUROC（对齐 FoVer）
   - PRMBench (ACL 2025, arXiv:2501.03124): PRMScore + error-type breakdown
   - Best-of-N reranking（全新）: MATH-500 + AIME24，Qwen2.5-Math-7B-Instruct 生成，N=8/16/64
   - OOD（全新）: GPQA-Diamond（following ThinkPRM）
   - Miracle step detection（大幅升级）: 自建 500-800 step 标注集（3 标注者，Fleiss' kappa）为 primary evaluation + synthetic adversarial miracle steps（在正确推理链中人为替换步骤为 unjustified leaps）+ PRMBench soundness 子集为 supplementary
   
   **7b. Baseline matrix（从隐含 ~2 个到显式 10+）**:
   - Pure neural: GenPRM-7B, ThinkPRM-14B, R-PRM-7B, Qwen2.5-Math-PRM-72B
   - Pure formal: FoVer-7B
   - Hybrid: VERGE（hand-crafted routing）, **Naive Hybrid**（FoVer Z3 try-and-fallback to GenPRM，无 learned router——最关键的 trivial alternative baseline）
   - LLM-as-Judge: GPT-4o, QwQ-32B
   - Compute-matched: GenPRM majority voting（等价 token budget，含 autoformalization 开销）
   - LogicReward: conceptual comparison（标注方法论差异）
   
   **7c. Ablation studies（从 0 个到 9 个）**:
   1. Formal-only（all → Z3，展示 low coverage penalty）
   2. Neural-only（all → GenPRM，展示 miracle step leakage）
   3. Random routing（50/50，隔离 routing 贡献 vs. ensemble effect）
   4. Oracle routing（ground-truth formalizability labels，performance ceiling）
   5. Router threshold sweep（coverage-accuracy trade-off curve，visualize asymmetric cost）
   6. Try-formal-first + neural fallback（trivial alternative——直接测 learned routing vs. unlearned try-and-fallback）
   7. Router label noise analysis（noisy auto-labels vs. human-cleaned labels 500-1000 条；含 200-300 "non-formalizable" label 的 human audit 报告 label precision）
   8. Roundtrip verification ablation（with vs. without Layer 2，量化 roundtrip gating 对 false alarm filtering 和 effective soundness 的贡献）
   9. 7B vs. 72B autoformalizer ablation（Qwen2.5-Math-7B vs. 72B，隔离 model capacity 对 formalization 质量和系统性能的影响，在 Pareto curve 上标注两个配置）
   
   **7d. Compute fairness（全新）**: 报告所有系统的 per-step FLOPs / tokens / wall-time（FormalRoute-PRM 的 compute 显式包含 autoformalization 开销），绘制 accuracy vs. compute Pareto curve，following ThinkPRM 的 token-budget-normalized comparison 范式
   
   **7e. Router analysis（全新）**: in-domain vs. OOD classification accuracy/precision/recall；few-shot domain adaptation ablation；oracle formalizability labels (human-annotated 100-200 examples) 量化 router quality ceiling；formalizability positive rate + formal branch coverage + roundtrip pass rate 统计
   
   **7f. Honest coverage reporting（全新）**: following Risk-Controlled (arXiv:2605.28365) 方法论，per-benchmark 报告 autoformalization coverage、roundtrip faithfulness rate、formal branch activation rate、effective soundness coverage (= formal-guarantee steps / total steps)；coverage-conditioned miracle detection analysis（formal branch 覆盖范围内 vs. 全量的 precision/recall 对比）
   
   **7g. Roundtrip verification pilot study（全新）**: 正式实验前在 FoVer 公开数据上抽取 200-500 formalizable steps，执行完整 autoformalize → back-translate → semantic equivalence pipeline，报告数学域 pass rate 和 failure modes，如 pass rate < 50% 需调整 faithfulness check 方法
   
   — 命中 Technical Soundness（从致命缺陷到接近完备）

8. **[新增 Compute Budget 章节]** — 原始仅说 "single-node H100"。新增 breakdown：router training ≈4-8 GPU-hours（Qwen3-8B LoRA on ~80K labels）；autoformalization 为 dominant cost（72B inference）；Z3 毫秒级；总训练 <1 天，全量评估 <5 天 on 8×H100 — 命中 Feasibility

9. **[Key References]** — 从 6 条扩展至 14 条。新增：ThinkPRM (arXiv:2504.16828)、R-PRM (EMNLP 2025, arXiv:2503.21295)、PRMBench (ACL 2025, arXiv:2501.03124)、FIRMA (MathNLP 2025)、Risk-Controlled Lean-as-Judge (arXiv:2605.28365)、Do LLMs Game Formalization (arXiv:2604.19459)、Roundtrip Verification (arXiv:2604.25031)、PRoSFI (arXiv:2603.29500)。原始 6 条全部保留（FoVer, GenPRM, LogicReward, VERGE, RRM, Risk-Controlled——后者补全了 arXiv ID）— 命中 Related Work 完整性

10. **[Trivial alternative 防御]** — 原始完全未 address。新增三重防御论证：(a) learned router 避免 formal branch 对 non-formalizable 步骤的系统性假阳性（FoVer documented overly-strict behavior 的根因），(b) roundtrip verification 非完美——Do LLMs Game Formalization 显示 axiom fabrication 和 premise mistranslation 可逃过 compilation 和 roundtrip 检查，learned router 作为第一道防线补充拦截，(c) 避免对 ~50-70% non-formalizable 步骤做 72B autoformalization 的 compute savings 是非平凡的成本降低。配合 Ablation 6（try-formal-first baseline）提供定量验证 — 命中 Novelty 防御

11. **[Coverage-concentration hypothesis]** — 原始未提及。新增作为 significance 加分的待验证假设：formal branch coverage 可能 disproportionately 覆盖 miracle-step-prone 步骤（代数变换、方程求解等明确逻辑推导环节既是 miracle step 高发区又是 autoformalization 最擅长的 step 类型）。设计实验验证计划：在 miracle step 标注集上分析 formal branch coverage 与 miracle step occurrence 的 overlap — 命中 Significance（若验证成立则从中-强推向强）

【主要风险】:

1. **Autoformalization bottleneck 导致 effective soundness coverage 过低**。按 Risk-Controlled 数据估算，72B autoformalizer 的有效覆盖可能仅 ~20-30%（coverage × faithfulness × router accuracy）。如果低于 15%，"conditional soundness" 的实际价值将被审稿人严重质疑——"you have formal guarantees on only 1/7 of the steps, how is this meaningfully better than pure neural?" 缓解策略：(a) coverage-conditioned analysis 证明 formal branch 在覆盖范围内有显著高于 neural 的 precision，(b) coverage-concentration hypothesis 验证 formal branch 精准覆盖高风险步骤，(c) 诚实报告 + pre-set meaningful threshold (>15%)。这是 **reviewer 最可能攻击的点**。

2. **Try-and-fallback baseline 表现接近 learned routing**。Ablation 6 如果显示 naive hybrid（无 router，直接尝试 Z3 + fallback）与 FormalRoute-PRM 差距 <2% F1，则 Contribution 2（learned routing）的增量价值被严重削弱——审稿人会建议"just use the simpler approach"。缓解策略：(a) 量化 false alarm reduction（formal branch 假阳性率的降低），(b) 量化 compute savings（避免 50-70% 步骤的 72B inference），(c) 如果 metric 差距确实小，pivot framing 到 efficiency contribution。这是 **第二大风险**。

【实施评估】:
- **计算资源**: 单节点 8×H100（或等价云实例）。Router 训练 ≈4-8 GPU-hours（Qwen3-8B LoRA on ~80K FoVer-derived labels）。Autoformalization 推理（Qwen2.5-Math-72B-Instruct）是 dominant cost，占总 compute ~60-70%。GenPRM-7B inference 为标准 7B 推理。Z3 求解毫秒级可忽略。Roundtrip verification 每个 formal-branch step 增加一次 LLM back-translation + semantic equivalence check。总训练 <1 天，全量评估 pipeline（含所有 baselines + 9 ablations + pilot study）<5 天。
- **数据需求**: FoVer 公开数据（~80K Z3-verified labels）用于 router 训练，公开可得。ProcessBench、PRMBench (ACL 2025)、MATH-500、AIME24、GPQA-Diamond 均公开可得。GenPRM-7B 开源权重可得。RRM miracle step annotations 需确认可用性（GitHub repo 已存在，但数据完整性待验证；自建标注集作为 primary fallback 已设计）。
- **人工介入**: (1) Miracle step 标注集构建：500-800 步骤（从 MATH-500 + AIME24 的 LLM 生成解题过程中抽取），3 名标注者按 RRM miracle step 定义标注，报告 Fleiss' kappa，约 2-3 人周；(2) Synthetic adversarial miracle step 构造：领域专家在正确推理链中设计 unjustified leap 替换模板，约 1 人周；(3) Router label quality audit：200-300 "non-formalizable" training labels 人工验证，约 1-2 人天；(4) Oracle formalizability labels：100-200 examples 人工标注，约 1 人周。总人工约 5-6 人周。
- **训练需求**: 仅 Qwen3-8B formalizability classifier 需 LoRA fine-tuning（~80K 样本，4-8 GPU-hours）。GenPRM-7B 使用开源权重无需训练。Autoformalization 使用 Qwen2.5-Math-72B-Instruct 预训练权重无需训练。训练需求轻量，远低于 PRM 领域典型训练成本。
- **新 Benchmark**: 需构建 miracle step detection test set（500-800 human-annotated steps + synthetic adversarial examples）。这是唯一需要自建的评测资源。构建成本可控（人工 3-4 人周 + 标注质量验证），且对 PRM 社区有独立贡献价值。
- **预估周期**: 10-14 周（从启动到可投稿）。
  - Weeks 1-3: 基础设施搭建（autoformalization pipeline 开发、FoVer 数据处理、Z3 derivability checking 集成）+ roundtrip verification 数学域 pilot study（200-500 steps，关键路径——结果可能影响 Layer 2 设计）
  - Weeks 3-5: Router 训练 + label quality audit + pilot study 分析与设计调整
  - Weeks 5-8: 主实验（5 benchmarks × 10+ baselines × 9 ablations）
  - Weeks 8-10: 人工标注（miracle step test set 构建）+ miracle step 评测 + coverage-conditioned analysis
  - Weeks 10-12: 全量分析、论文撰写
  - Weeks 12-14: 缓冲、内部 review、修订
  - **关键路径**: Weeks 1-3 的 roundtrip verification pilot study 最优先——如果数学域 pass rate < 50%，需要调整 Layer 2 设计（如用 entailment model 替代 strict equivalence check），这会影响后续所有实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdbbedff-904a-4c9e-8290-ffc576f08af8",
  "isSidechain": false,
  "requestId": "req_011CbWPjLaZBWNgJLJGzGBWq",
  "type": "assistant",
  "uuid": "1c9f389d-0342-414e-9d06-4df5a7fbdc39",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L28X4mEQSUHfYCR5zLeqa9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7009,
      "cache_read_input_tokens": 85279,
      "output_tokens": 5361,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7009,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5361,
          "cache_read_input_tokens": 85279,
          "cache_creation_input_tokens": 7009,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7009
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

_source line 99_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。",
  "leafUuid": "1c9f389d-0342-414e-9d06-4df5a7fbdc39",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---

### Runtime record

_source line 100_

```json
{
  "type": "ai-title",
  "aiTitle": "Formally-routed PRM for miracle step detection",
  "sessionId": "a05c62ff-bff7-4813-ae79-89cefb9808a3"
}
```

---
