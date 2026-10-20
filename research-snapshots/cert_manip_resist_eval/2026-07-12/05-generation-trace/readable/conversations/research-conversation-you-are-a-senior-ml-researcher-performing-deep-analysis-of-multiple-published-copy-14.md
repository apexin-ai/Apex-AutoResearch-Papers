# Research conversation: You are a senior ML researcher performing deep analysis of multiple published papers. **Today's date: 2026-05-30 (UTC).*

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/dddbbea0-aee9-49cc-be74-8741d74f3ef2.jsonl`
- **Structured JSON:** [`fe3b2a44f74614c9f5e6.json`](../../sessions/fe/fe3b2a44f74614c9f5e6.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:27:42.241Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:27:42.241Z",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "content": "You are a senior ML researcher performing deep analysis of multiple published papers.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: Information Retrieval and Knowledge Management\n\nDirection: Train a learned reward model that evaluates whether retrieved documents improve multi-step reasoning chain quality (not just final answer correctness), then use this reasoning-utility reward model as a training signal for dense retrievers via RL or contrastive learning. Evaluate on reasoning-intensive retrieval benchmarks (BRIGHT) where existing utility-based retrievers have not been tested.\n\nSeed Papers:\n- BRIGHT (ICLR 2025) — Established the 40.7-point gap for reasoning-intensive retrieval; defines the evaluation target\n- SCARLet (EMNLP 2025) — Demonstrated utility-based retriever training via perturbation attribution, but uses heuristic utility estimation, not a learned reward model\n- Agentic-R (arXiv Jan 2026) — Trained retrievers on downstream answer correctness (binary EM) as utility signal; closest existing work but uses heuristic signal, not learned reasoning quality\n- ReasonIR (arXiv Apr 2025) — SOTA retriever-only baseline on BRIGHT (29.9 nDCG@10); uses synthetic contrastive data, not reward-based training\n\nKnown Gaps:\n- No existing work uses a LEARNED reward model (as opposed to heuristic EM or perturbation) to evaluate document utility for reasoning-intensive retrieval\n- No utility-based retriever training method has been evaluated on BRIGHT; all evaluations are on standard QA benchmarks\n- The distinction between 'document helps answer' vs 'document helps reasoning process' is unformalized — Agentic-R's binary EM conflates documents containing answers with documents that aid reasoning\n\nTheoretical Anchor: Information-theoretic utility: a document's value for reasoning is the mutual information between the document and the reasoning chain conditioned on the query, not the mutual information between the document and the answer. This distinction predicts that utility-based training with reasoning-quality rewards should preferentially retrieve tutorial/explanation documents over answer-containing documents for reasoning-intensive queries.\n\nConstraints:\n- Compute: ≤200 H100-hours\n\nQuality Self-Checks:\n- [ ] Core insight: Documents that help reasoning are different from documents that contain answers, and a learned reward model can distinguish them where binary EM cannot.\n- [ ] Why not obvious: Agentic-R and SCARLet show utility-based training works, but their heuristic signals (EM, perturbation) cannot distinguish reasoning-helpful from answer-containing documents. A learned reward model is needed because reasoning utility is a latent property requiring inference.\n- [ ] Baseline fear test: YES — Agentic-R's simple binary EM baseline achieves strong results on QA benchmarks. The key bet is that learned reasoning-quality rewards provide gains specifically on reasoning-INTENSIVE tasks (BRIGHT) where EM-based utility training would fail because relevant documents don't contain answers.\n- [ ] Information exploited: Reasoning chain quality signals (intermediate step correctness, coherence, faithfulness) that heuristic utility measures ignore.\n\nAvoid:\n- Conflating this with training the LLM/generator (the vast majority of RL-for-RAG work trains the LLM, not the retriever — we must train the retriever)\n- Claiming the utility-vs-relevance insight is novel (SCARLet and Agentic-R have already demonstrated it; our contribution is the LEARNED REWARD MODEL and REASONING-INTENSIVE evaluation)**\n\n## Your task (Batch 3)\n\nAnalyze the following 5 papers. For EACH paper:\n1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.\n2. If on OpenReview, also read reviewer comments.\n3. Write a concise analysis focusing on HOW the paper innovates.\n\n## Papers to analyze\n\n[\n  {\n    \"title\": \"ReasonIR: Training Retrievers for Reasoning Tasks\",\n    \"authors\": \"Rulin Shao et al.\",\n    \"venue\": \"arXiv 2025\",\n    \"url\": \"https://arxiv.org/abs/2504.20595\",\n    \"why_important\": \"SOTA retriever-only baseline on BRIGHT (29.9 nDCG@10); introduced the first synthetic data generation pipeline specifically for reasoning-intensive retrieval training. Key baseline your method must beat.\",\n    \"one_line_summary\": \"Introduces ReasonIR-8B, a bi-encoder retriever trained on synthetically generated reasoning-intensive queries and hard negatives, achieving state-of-the-art on BRIGHT without reranking.\"\n  },\n  {\n    \"title\": \"RaDeR: Reasoning-aware Dense Retrieval Models\",\n    \"authors\": \"Debrup Das et al.\",\n    \"venue\": \"EMNLP 2025 (Main)\",\n    \"url\": \"https://arxiv.org/abs/2505.18405\",\n    \"why_important\": \"First dense retriever to outperform BM25 on chain-of-thought queries; demonstrates that MCTS-derived reasoning trajectories produce highly sample-efficient retriever training data (2.5% of ReasonIR's data).\",\n    \"one_line_summary\": \"Trains dense retrievers on MCTS-based mathematical reasoning trajectories with self-reflective relevance evaluation, producing the first bi-encoder that beats BM25 when queries are CoT reasoning steps.\"\n  },\n  {\n    \"title\": \"CoSearch: Joint Training of Reasoning and Document Ranking via Reinforcement Learning for Agentic Search\",\n    \"authors\": \"Hansi Zeng et al.\",\n    \"venue\": \"arXiv 2026\",\n    \"url\": \"https://arxiv.org/abs/2604.17555\",\n    \"why_important\": \"First to jointly train both the reasoning agent AND the document ranker via GRPO — demonstrates that fixed retrieval is a 26.8% bottleneck and that ranker training with answer-correctness rewards helps.\",\n    \"one_line_summary\": \"Jointly optimizes a multi-step reasoning agent and a generative document ranker via GRPO with semantic query grouping and composite ranking-quality + answer-correctness rewards across 7 QA benchmarks.\"\n  },\n  {\n    \"title\": \"RAG-RewardBench: Benchmarking Reward Models in Retrieval Augmented Generation for Preference Alignment\",\n    \"authors\": \"Zichen Chen et al.\",\n    \"venue\": \"ACL 2025 (Findings)\",\n    \"url\": \"https://arxiv.org/abs/2412.13746\",\n    \"why_important\": \"First benchmark specifically for evaluating reward models in RAG settings; evaluates 45 RMs across 4 RAG-specific scenarios — provides the evaluation methodology for your learned reasoning-utility reward model.\",\n    \"one_line_summary\": \"Introduces the first benchmark for reward models in RAG with 18 subsets across multi-hop reasoning, citation, abstention, and conflict robustness scenarios, revealing that existing RALMs show almost no improvement from preference alignment.\"\n  },\n  {\n    \"title\": \"Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection\",\n    \"authors\": \"Akari Asai et al.\",\n    \"venue\": \"ICLR 2024 (Oral, top 1%)\",\n    \"url\": \"https://arxiv.org/abs/2310.11511\",\n    \"why_important\": \"ICLR 2024 Oral; highly cited foundational work that introduced learned reflection tokens for adaptive retrieval decisions — established the paradigm of learned self-evaluation signals in RAG systems.\",\n    \"one_line_summary\": \"Trains an LM to adaptively retrieve passages on-demand and self-critique generations using learned reflection tokens, enabling controllable RAG behavior that outperforms ChatGPT on QA, reasoning, and fact verification.\"\n  }\n]\n\n## Analysis requirements\n\nFor each paper, analyze:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- If reviewer comments are available: what was praised, what was criticized?\n\n## CRITICAL: Length constraint\n\n**Each paper's analysis MUST be under 2000 characters.** Be concise and analytical — no filler, no generic praise, no redundant descriptions. Every sentence must carry information.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem? How found? (1-2 sentences)\",\n  \"key_insight\": \"Core intellectual contribution (1 sentence)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach (2-3 sentences)\",\n  \"limitations_and_open_questions\": \"Gaps + follow-up questions (1-2 sentences)\",\n  \"building_blocks\": [\"Reusable methods/tools/datasets\"],\n  \"relevance_to_seed\": \"Relation to our research area (1 sentence)\"\n}\n\nYou MUST output exactly 5 analyses in the JSON array. IMPORTANT: End your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:27:42.245Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:27:42.245Z",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-30T06:27:42.397Z_

You are a senior ML researcher performing deep analysis of multiple published papers.

**Today's date: 2026-05-30 (UTC).**

## Research context

We are generating ideas in the area of: **Target: AAAI 2026
Track: Information Retrieval and Knowledge Management

Direction: Train a learned reward model that evaluates whether retrieved documents improve multi-step reasoning chain quality (not just final answer correctness), then use this reasoning-utility reward model as a training signal for dense retrievers via RL or contrastive learning. Evaluate on reasoning-intensive retrieval benchmarks (BRIGHT) where existing utility-based retrievers have not been tested.

Seed Papers:
- BRIGHT (ICLR 2025) — Established the 40.7-point gap for reasoning-intensive retrieval; defines the evaluation target
- SCARLet (EMNLP 2025) — Demonstrated utility-based retriever training via perturbation attribution, but uses heuristic utility estimation, not a learned reward model
- Agentic-R (arXiv Jan 2026) — Trained retrievers on downstream answer correctness (binary EM) as utility signal; closest existing work but uses heuristic signal, not learned reasoning quality
- ReasonIR (arXiv Apr 2025) — SOTA retriever-only baseline on BRIGHT (29.9 nDCG@10); uses synthetic contrastive data, not reward-based training

Known Gaps:
- No existing work uses a LEARNED reward model (as opposed to heuristic EM or perturbation) to evaluate document utility for reasoning-intensive retrieval
- No utility-based retriever training method has been evaluated on BRIGHT; all evaluations are on standard QA benchmarks
- The distinction between 'document helps answer' vs 'document helps reasoning process' is unformalized — Agentic-R's binary EM conflates documents containing answers with documents that aid reasoning

Theoretical Anchor: Information-theoretic utility: a document's value for reasoning is the mutual information between the document and the reasoning chain conditioned on the query, not the mutual information between the document and the answer. This distinction predicts that utility-based training with reasoning-quality rewards should preferentially retrieve tutorial/explanation documents over answer-containing documents for reasoning-intensive queries.

Constraints:
- Compute: ≤200 H100-hours

Quality Self-Checks:
- [ ] Core insight: Documents that help reasoning are different from documents that contain answers, and a learned reward model can distinguish them where binary EM cannot.
- [ ] Why not obvious: Agentic-R and SCARLet show utility-based training works, but their heuristic signals (EM, perturbation) cannot distinguish reasoning-helpful from answer-containing documents. A learned reward model is needed because reasoning utility is a latent property requiring inference.
- [ ] Baseline fear test: YES — Agentic-R's simple binary EM baseline achieves strong results on QA benchmarks. The key bet is that learned reasoning-quality rewards provide gains specifically on reasoning-INTENSIVE tasks (BRIGHT) where EM-based utility training would fail because relevant documents don't contain answers.
- [ ] Information exploited: Reasoning chain quality signals (intermediate step correctness, coherence, faithfulness) that heuristic utility measures ignore.

Avoid:
- Conflating this with training the LLM/generator (the vast majority of RL-for-RAG work trains the LLM, not the retriever — we must train the retriever)
- Claiming the utility-vs-relevance insight is novel (SCARLet and Agentic-R have already demonstrated it; our contribution is the LEARNED REWARD MODEL and REASONING-INTENSIVE evaluation)**

## Your task (Batch 3)

Analyze the following 5 papers. For EACH paper:
1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.
2. If on OpenReview, also read reviewer comments.
3. Write a concise analysis focusing on HOW the paper innovates.

## Papers to analyze

[
  {
    "title": "ReasonIR: Training Retrievers for Reasoning Tasks",
    "authors": "Rulin Shao et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2504.20595",
    "why_important": "SOTA retriever-only baseline on BRIGHT (29.9 nDCG@10); introduced the first synthetic data generation pipeline specifically for reasoning-intensive retrieval training. Key baseline your method must beat.",
    "one_line_summary": "Introduces ReasonIR-8B, a bi-encoder retriever trained on synthetically generated reasoning-intensive queries and hard negatives, achieving state-of-the-art on BRIGHT without reranking."
  },
  {
    "title": "RaDeR: Reasoning-aware Dense Retrieval Models",
    "authors": "Debrup Das et al.",
    "venue": "EMNLP 2025 (Main)",
    "url": "https://arxiv.org/abs/2505.18405",
    "why_important": "First dense retriever to outperform BM25 on chain-of-thought queries; demonstrates that MCTS-derived reasoning trajectories produce highly sample-efficient retriever training data (2.5% of ReasonIR's data).",
    "one_line_summary": "Trains dense retrievers on MCTS-based mathematical reasoning trajectories with self-reflective relevance evaluation, producing the first bi-encoder that beats BM25 when queries are CoT reasoning steps."
  },
  {
    "title": "CoSearch: Joint Training of Reasoning and Document Ranking via Reinforcement Learning for Agentic Search",
    "authors": "Hansi Zeng et al.",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2604.17555",
    "why_important": "First to jointly train both the reasoning agent AND the document ranker via GRPO — demonstrates that fixed retrieval is a 26.8% bottleneck and that ranker training with answer-correctness rewards helps.",
    "one_line_summary": "Jointly optimizes a multi-step reasoning agent and a generative document ranker via GRPO with semantic query grouping and composite ranking-quality + answer-correctness rewards across 7 QA benchmarks."
  },
  {
    "title": "RAG-RewardBench: Benchmarking Reward Models in Retrieval Augmented Generation for Preference Alignment",
    "authors": "Zichen Chen et al.",
    "venue": "ACL 2025 (Findings)",
    "url": "https://arxiv.org/abs/2412.13746",
    "why_important": "First benchmark specifically for evaluating reward models in RAG settings; evaluates 45 RMs across 4 RAG-specific scenarios — provides the evaluation methodology for your learned reasoning-utility reward model.",
    "one_line_summary": "Introduces the first benchmark for reward models in RAG with 18 subsets across multi-hop reasoning, citation, abstention, and conflict robustness scenarios, revealing that existing RALMs show almost no improvement from preference alignment."
  },
  {
    "title": "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection",
    "authors": "Akari Asai et al.",
    "venue": "ICLR 2024 (Oral, top 1%)",
    "url": "https://arxiv.org/abs/2310.11511",
    "why_important": "ICLR 2024 Oral; highly cited foundational work that introduced learned reflection tokens for adaptive retrieval decisions — established the paradigm of learned self-evaluation signals in RAG systems.",
    "one_line_summary": "Trains an LM to adaptively retrieve passages on-demand and self-critique generations using learned reflection tokens, enabling controllable RAG behavior that outperforms ChatGPT on QA, reasoning, and fact verification."
  }
]

## Analysis requirements

For each paper, analyze:
- What gap did they identify and HOW?
- What was the key insight others missed?
- How did they formulate the problem differently?
- What existing technique did they adapt/combine/simplify?
- If reviewer comments are available: what was praised, what was criticized?

## CRITICAL: Length constraint

**Each paper's analysis MUST be under 2000 characters.** Be concise and analytical — no filler, no generic praise, no redundant descriptions. Every sentence must carry information.

## Output format

Output a JSON array. Each element:
{
  "title": "Paper title",
  "venue": "Where published",
  "problem_identification": "What gap/problem? How found? (1-2 sentences)",
  "key_insight": "Core intellectual contribution (1 sentence)",
  "innovation_type": "new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis",
  "method_summary": "Technical approach (2-3 sentences)",
  "limitations_and_open_questions": "Gaps + follow-up questions (1-2 sentences)",
  "building_blocks": ["Reusable methods/tools/datasets"],
  "relevance_to_seed": "Relation to our research area (1 sentence)"
}

You MUST output exactly 5 analyses in the JSON array. IMPORTANT: End your response with the JSON array.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "509b9e27-9338-43ac-a97b-3de5e1bfe6b5",
  "type": "user",
  "uuid": "58356568-78cb-4494-84f9-428a9e1b6dab",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:27:42.396Z_

```json
{
  "parentUuid": "58356568-78cb-4494-84f9-428a9e1b6dab",
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
  "uuid": "ffacd32a-3c8c-4961-8dae-fd4b481597a2",
  "timestamp": "2026-05-30T06:27:42.396Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:27:42.396Z_

```json
{
  "parentUuid": "ffacd32a-3c8c-4961-8dae-fd4b481597a2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e8944d34-3479-46ef-8c51-a7dc266fd7b0",
  "timestamp": "2026-05-30T06:27:42.396Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
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
  "aiTitle": "Analyze ML papers on reasoning-aware retrievers",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Assistant

_source line 7 · 2026-05-30T06:27:45.989Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze 5 papers in detail. Let me search for and read each paper, then provide a structured JSON analysis. I'll launch multiple agents to research these papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8944d34-3479-46ef-8c51-a7dc266fd7b0",
  "isSidechain": false,
  "requestId": "req_011CbYH9N8SVbJxRjBC8L2Sa",
  "type": "assistant",
  "uuid": "a5dbc905-9a18-4b71-ab14-4d01c229ff48",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jbYaCCeNbMXBFR1RhABZe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3607,
      "cache_read_input_tokens": 11014,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 153,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3607
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

_source line 8 · 2026-05-30T06:27:47.174Z_

I'll research all 5 papers in parallel to gather their details efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5dbc905-9a18-4b71-ab14-4d01c229ff48",
  "isSidechain": false,
  "requestId": "req_011CbYH9N8SVbJxRjBC8L2Sa",
  "type": "assistant",
  "uuid": "25d04519-9bf5-42e4-ad6f-217602812e06",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jbYaCCeNbMXBFR1RhABZe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3607,
      "cache_read_input_tokens": 11014,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 153,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3607
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

_source line 9 · 2026-05-30T06:27:47.838Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019h8GhLANdMhsoV8SKb2waM`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "25d04519-9bf5-42e4-ad6f-217602812e06",
  "isSidechain": false,
  "requestId": "req_011CbYH9N8SVbJxRjBC8L2Sa",
  "type": "assistant",
  "uuid": "16127477-34b6-4cf1-bd2e-1e0bce9adeb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014jbYaCCeNbMXBFR1RhABZe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3607,
      "cache_read_input_tokens": 11014,
      "output_tokens": 153,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 153,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3607
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

_source line 10 · 2026-05-30T06:27:47.847Z_

<details><summary>↩ Tool result · `toolu_019h8GhLANdMhsoV8SKb2waM`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16127477-34b6-4cf1-bd2e-1e0bce9adeb2",
  "isSidechain": false,
  "promptId": "509b9e27-9338-43ac-a97b-3de5e1bfe6b5",
  "type": "user",
  "uuid": "3674fef2-0940-4b1b-ac2a-43f79acd4065",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "16127477-34b6-4cf1-bd2e-1e0bce9adeb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-30T06:27:50.687Z_

<details><summary>Logged reasoning block</summary>

```text
Now I'll launch 5 parallel agents to research each paper simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3674fef2-0940-4b1b-ac2a-43f79acd4065",
  "isSidechain": false,
  "requestId": "req_011CbYH9mnESpG5gmDmBKiru",
  "type": "assistant",
  "uuid": "e90a1aed-4198-4d1e-b2c6-db87c291aed6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCYe2BnksVDiqEyuMHiZ4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 14621,
      "output_tokens": 1723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1723,
          "cache_read_input_tokens": 14621,
          "cache_creation_input_tokens": 1173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1173
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

_source line 12 · 2026-05-30T06:27:51.309Z_

Now I'll research all 5 papers in parallel using agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e90a1aed-4198-4d1e-b2c6-db87c291aed6",
  "isSidechain": false,
  "requestId": "req_011CbYH9mnESpG5gmDmBKiru",
  "type": "assistant",
  "uuid": "5d4e8059-2288-47d3-929f-7bc197364a50",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCYe2BnksVDiqEyuMHiZ4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 14621,
      "output_tokens": 1723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1723,
          "cache_read_input_tokens": 14621,
          "cache_creation_input_tokens": 1173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1173
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

_source line 13 · 2026-05-30T06:27:59.269Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UfLfspkSa1E6NsgrbEH5oJ`</summary>

```json
{
  "description": "Research ReasonIR paper",
  "prompt": "You are researching the paper \"ReasonIR: Training Retrievers for Reasoning Tasks\" by Rulin Shao et al. (arXiv 2025, https://arxiv.org/abs/2504.20595).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also try to find if it has an OpenReview page with reviewer comments.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined/simplified\n5. Their core technical method in detail (data generation pipeline, training procedure, model architecture)\n6. Their main results on BRIGHT benchmark specifically\n7. Limitations acknowledged or apparent\n8. Any reviewer comments if available on OpenReview\n\nPlease be thorough and precise. Report all findings in detail.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d4e8059-2288-47d3-929f-7bc197364a50",
  "isSidechain": false,
  "requestId": "req_011CbYH9mnESpG5gmDmBKiru",
  "type": "assistant",
  "uuid": "57a05ed6-2706-4197-83de-a8c69adc95c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCYe2BnksVDiqEyuMHiZ4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 14621,
      "output_tokens": 1723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1723,
          "cache_read_input_tokens": 14621,
          "cache_creation_input_tokens": 1173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1173
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

_source line 14 · 2026-05-30T06:28:04.185Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SjR8WE5XbuuczSA7DGMMhU`</summary>

```json
{
  "description": "Research RaDeR paper",
  "prompt": "You are researching the paper \"RaDeR: Reasoning-aware Dense Retrieval Models\" by Debrup Das et al. (EMNLP 2025, https://arxiv.org/abs/2505.18405).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also try searching for any OpenReview page with reviewer comments.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined/simplified (especially MCTS usage)\n5. Their core technical method in detail (MCTS-based reasoning trajectories, self-reflective relevance evaluation, training procedure)\n6. Their main results, especially comparison with BM25 on CoT queries and comparison with ReasonIR\n7. The claim about sample efficiency (2.5% of ReasonIR's data)\n8. Limitations acknowledged or apparent\n9. Any reviewer comments if available\n\nPlease be thorough and precise. Report all findings in detail.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57a05ed6-2706-4197-83de-a8c69adc95c9",
  "isSidechain": false,
  "requestId": "req_011CbYH9mnESpG5gmDmBKiru",
  "type": "assistant",
  "uuid": "cd9bec28-2868-4757-8abb-b2eed2b46b26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCYe2BnksVDiqEyuMHiZ4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 14621,
      "output_tokens": 1723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1723,
          "cache_read_input_tokens": 14621,
          "cache_creation_input_tokens": 1173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1173
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

_source line 15 · 2026-05-30T06:28:08.623Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Wmn2JdsdHqjoQbsgaYSKCA`</summary>

```json
{
  "description": "Research CoSearch paper",
  "prompt": "You are researching the paper \"CoSearch: Joint Training of Reasoning and Document Ranking via Reinforcement Learning for Agentic Search\" by Hansi Zeng et al. (arXiv 2026, https://arxiv.org/abs/2604.17555).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also try searching for any OpenReview page with reviewer comments.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined (especially GRPO, semantic query grouping, composite rewards)\n5. Their core technical method in detail (joint training of reasoning agent and document ranker, reward structure)\n6. Their main results - especially the 26.8% bottleneck claim about fixed retrieval\n7. Benchmarks used and performance numbers\n8. Limitations acknowledged or apparent\n9. Any reviewer comments if available\n\nPlease be thorough and precise. Report all findings in detail.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd9bec28-2868-4757-8abb-b2eed2b46b26",
  "isSidechain": false,
  "requestId": "req_011CbYH9mnESpG5gmDmBKiru",
  "type": "assistant",
  "uuid": "fcbad8eb-2b9e-4dd1-bb39-5ce8f5814dc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCYe2BnksVDiqEyuMHiZ4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 14621,
      "output_tokens": 1723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1723,
          "cache_read_input_tokens": 14621,
          "cache_creation_input_tokens": 1173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1173
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

_source line 16 · 2026-05-30T06:28:14.399Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013KNDhzRKVEnwEUfXoKQrrC`</summary>

```json
{
  "description": "Research RAG-RewardBench paper",
  "prompt": "You are researching the paper \"RAG-RewardBench: Benchmarking Reward Models in Retrieval Augmented Generation for Preference Alignment\" by Zichen Chen et al. (ACL 2025 Findings, https://arxiv.org/abs/2412.13746).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also try searching for any OpenReview page or ACL 2025 reviewer comments.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined\n5. Their core technical method in detail (benchmark construction, 18 subsets, 4 RAG-specific scenarios, evaluation methodology)\n6. Key findings about the 45 reward models evaluated\n7. The finding about RALMs showing almost no improvement from preference alignment\n8. Limitations acknowledged or apparent\n9. Any reviewer comments if available\n\nPlease be thorough and precise. Report all findings in detail.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcbad8eb-2b9e-4dd1-bb39-5ce8f5814dc8",
  "isSidechain": false,
  "requestId": "req_011CbYH9mnESpG5gmDmBKiru",
  "type": "assistant",
  "uuid": "15ac4ac2-0a94-464e-b939-4805a7a07b02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCYe2BnksVDiqEyuMHiZ4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 14621,
      "output_tokens": 1723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1723,
          "cache_read_input_tokens": 14621,
          "cache_creation_input_tokens": 1173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1173
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

_source line 17 · 2026-05-30T06:28:19.056Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DAf6w3i6p9zis7mDvzoMGA`</summary>

```json
{
  "description": "Research Self-RAG paper",
  "prompt": "You are researching the paper \"Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection\" by Akari Asai et al. (ICLR 2024 Oral, https://arxiv.org/abs/2310.11511).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also search for the ICLR 2024 OpenReview page to get reviewer comments. Try: https://openreview.net/forum?id=hSyW5go0v8 or search for it.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined (reflection tokens, critic model, adaptive retrieval)\n5. Their core technical method in detail (reflection token types, training procedure, inference-time control)\n6. Main results across tasks (QA, reasoning, fact verification)\n7. Limitations acknowledged or apparent\n8. Reviewer comments from ICLR 2024 OpenReview - what was praised and criticized\n\nPlease be thorough and precise. Report all findings in detail.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15ac4ac2-0a94-464e-b939-4805a7a07b02",
  "isSidechain": false,
  "requestId": "req_011CbYH9mnESpG5gmDmBKiru",
  "type": "assistant",
  "uuid": "e72223a6-e6d9-40db-afae-b3c85ab62168",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SCYe2BnksVDiqEyuMHiZ4Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1173,
      "cache_read_input_tokens": 14621,
      "output_tokens": 1723,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1173,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1723,
          "cache_read_input_tokens": 14621,
          "cache_creation_input_tokens": 1173,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1173
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "e72223a6-e6d9-40db-afae-b3c85ab62168",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on reasoning-aware retrievers",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Tool result

_source line 20 · 2026-05-30T06:31:16.664Z_

<details><summary>↩ Tool result · `toolu_01Wmn2JdsdHqjoQbsgaYSKCA`</summary>

```text
Now I have comprehensive information. Let me compile the full detailed report.

---

Here is a thorough extraction of all requested information from the CoSearch paper (arXiv:2604.17555).

---

## 1. The Exact Gap/Problem Identified and How They Identified It

The authors identified that existing agentic search systems (like Search-R1) treat the retrieval component as a **fixed, frozen tool**, optimizing only the reasoning agent via RL while the retrieval system remains unchanged. They hypothesized that retrieval quality itself is a major bottleneck.

**How they identified it:** They designed an **oracle retrieval experiment**. For every sub-query issued by a trained reasoning agent, they promoted all documents containing the gold answer to the top positions in the ranking. For sub-queries where no retrieved document contained the gold answer, the ranking was left unchanged. The results were striking:

- **7B agent (Qwen2.5-7B-Instruct):** Single-hop average improved from 0.600 to 0.709 (+18.2% relative), multi-hop from 0.506 to 0.564 (+11.5%), overall **+14.7% relative F1**
- **3B agent (Qwen2.5-3B-Instruct):** Single-hop improved from 0.531 to 0.636 (+19.8%), multi-hop from 0.371 to 0.499 (+34.5%), overall **+26.8% relative F1**

The smaller model showed a larger gap, indicating weaker models are even more dependent on retrieval quality. The authors concluded: "the retrieval system is a key bottleneck in scaling agentic search performance."

---

## 2. Their Key Insight That Others Missed

Two main insights:

**Insight 1:** Prior work (Search-R1, Agentic-R, etc.) optimized only one side of the agentic search pipeline. Search-R1 trains only the reasoning agent; Agentic-R trains a dense retriever using LLM-annotated labels but does so offline/separately, not jointly. CoSearch's insight is that the reasoning agent and retrieval system are **interdependent** and must be **co-optimized** -- the agent's sub-queries shape what the ranker sees, and the ranker's outputs shape what the agent reasons over.

**Insight 2:** The non-trivial technical challenge of applying GRPO to a **ranker** within an agentic pipeline. GRPO requires multiple responses generated from **identical input prompts** to compute group-relative advantages. For the main agent, this is straightforward (same initial query q0 produces G trajectories). But for the ranker, different trajectories produce **different sub-queries** at each step, meaning the ranker never sees identical inputs across rollouts. The authors recognized this as a fundamental obstacle and solved it with semantic query grouping.

---

## 3. How They Formulated the Problem Differently from Prior Work

Prior work treats agentic search as a single-agent RL problem where the retrieval system is an environment component. CoSearch formulates it as a **joint optimization** of two policies:

- **Main agent policy** `π_θmain`: Generates reasoning traces, sub-queries, and final answers
- **Generative ranker policy** `π_θgr`: Takes N candidate documents from a fixed dense retriever and selects/reorders the top K

The trajectory is formalized as: `y = (q0, τ1, q1, o1, τ2, q2, o2, ..., τm, qm, om, τm+1, a)` where τt are reasoning thoughts, qt are sub-queries, and ot are observations (retrieved documents).

The optimization objective is: `max_{θmain, θgr} E[r(T)]`

The key architectural decomposition: retrieval is split into a **fixed dense retriever** (E5 base producing N=50 candidates) and a **trainable generative listwise ranker** (selecting K=5 documents). This decomposition is critical because it makes the ranker amenable to RL training (generating permutation sequences as text) while keeping first-stage retrieval efficient.

---

## 4. Existing Techniques They Adapted/Combined

**GRPO (Group Relative Policy Optimization):** Originally from DeepSeek-R1 and related work. CoSearch applies GRPO to both the main agent (standard application) and the ranker (novel application requiring semantic grouping). The GRPO objective uses importance sampling ratios and group-normalized advantages with clipping: `1/G Σ Σ m(i,t) min(ρ(i,t) * Â(i), clip(ρ(i,t), 1-ε, 1+ε) * Â(i))`

**Semantic Query Grouping:** A novel technique that clusters sub-queries using token-level F1 similarity with threshold δ=0.8. A sub-query q enters group gm if `F1_token(q, q_m_rep) ≥ δ`. Groups with fewer than kmin=3 members are discarded. This has **zero additional sampling cost** -- it reuses trajectories already generated for the main agent, avoiding the exponential rollout explosion that would occur if you tried to separately sample G ranker outputs for each unique sub-query.

**Composite Rewards:** The ranker reward combines:
- **Relevance reward (r_rel):** Average Hit@k over k ∈ {1, 3, 5}, using pseudo-relevant labels (documents containing the gold answer string)
- **Main agent reward (r_main):** Token-level F1 between predicted and gold answers (trajectory-level signal)
- Three-case composite structure based on whether answer-containing documents exist among candidates (I_ans) and a relevance threshold γ=0.5:
  - When I_ans=1 and r_rel ≤ γ: use r_rel alone (ranker needs to focus on precision)
  - When I_ans=1 and r_rel > γ: use r_rel + r_main (ranking is sufficient, add trajectory signal)
  - When I_ans=0: use r_main alone (no relevant document to rank, so use trajectory-level feedback only)
  - Format violation: -0.2 penalty

**ReAct-style prompting:** The agent uses a structured format with reasoning and tool-use steps.

**Generative listwise ranking:** The ranker generates a permutation of document identifiers as text output (rather than pointwise scoring), adapted from prior work on LLMs as listwise rankers.

---

## 5. Core Technical Method in Detail

**Architecture:**
- Main agent: Qwen2.5-7B-Instruct (or 3B)
- Generative ranker: Separate Qwen2.5-7B-Instruct model (separate parameters from agent)
- Dense retriever: E5 base (frozen), retrieves N=50 candidates from 18M-passage Wikipedia 2018 corpus via FAISS GPU index
- The ranker takes the 50 candidates and produces a ranked list, from which the top K=5 are shown to the agent

**Training Loop:**
1. Sample G=8 trajectories per initial query q0 using the current main agent policy
2. At each search step, the agent issues a sub-query; the dense retriever returns N=50 candidates; the ranker selects K=5
3. After trajectory completion, compute main agent rewards (token-level F1 with gold answer, or -0.2 for format violations)
4. For ranker training: apply semantic grouping to cluster sub-queries across the G trajectories; compute composite rewards; apply GRPO
5. Update both policies simultaneously

**Main Agent Reward:**
- Token-level F1 between predicted answer and gold answer (if format-compliant)
- -α (α=0.2) penalty for format violations

**Ranker Reward (the composite structure described above):**
The key design choice is the three-case structure. When relevant documents exist but ranking is poor (r_rel ≤ γ), only the ranking quality signal is used -- this focuses the ranker on getting the right documents to the top. When ranking is already good (r_rel > γ), the trajectory-level signal is added to encourage rankings that not only have relevant documents but also help the downstream reasoning agent. When no relevant documents exist in the candidate set, only the trajectory-level signal is used since the ranker can't be blamed for missing documents.

**Why Hit@k over nDCG@k:** Ablations show Hit@k outperforms nDCG@k by 2.1% -- the authors explain this is because Hit@k provides a clearer binary signal about whether relevant documents appear in top positions.

**Why not shared backbone:** Using a shared model for both agent and ranker degraded performance by 1.6%, attributed to conflicting gradient signals between the two tasks.

**Why not cross-encoder ranker:** Cross-encoders perform pointwise scoring, which is unsuitable for direct RL optimization via GRPO. The generative listwise approach (-2.9% with cross-encoder) allows the ranker to produce sequences that can be treated as policy outputs.

---

## 6. Main Results -- The 26.8% Bottleneck Claim

The 26.8% figure comes specifically from the **oracle retrieval experiment** on the **3B agent**, representing the relative F1 improvement when answer-containing documents are promoted to top positions. This is NOT a result of CoSearch itself, but rather the motivation experiment showing **how much room exists for improvement** if retrieval were perfect.

CoSearch itself achieves:
- **7B: 0.568 avg F1** vs Search-R1's 0.533 (+6.6% relative improvement)
- **3B: 0.471 avg F1** vs Search-R1's 0.428 (+10.0% relative improvement)
- Oracle upper bound for 7B: 0.626

CoSearch closes approximately **27% of the gap** between Search-R1 and the oracle upper bound across both scales.

---

## 7. Benchmarks Used and Performance Numbers

**Seven QA benchmarks:**
- Single-hop: NQ (Natural Questions), TriviaQA, PopQA
- Multi-hop: HotpotQA, 2WikiMultiHopQA, Musique, Bamboogle

**Full per-dataset results (7B, token-level F1):**

| Method | NQ | TriviaQA | PopQA | HotpotQA | 2Wiki | Musique | Bamboogle | Avg |
|---|---|---|---|---|---|---|---|---|
| Direct Inference | - | - | - | - | - | - | - | 0.298 |
| RAG | - | - | - | - | - | - | - | 0.365 |
| Search-R1 | 0.556 | 0.681 | 0.539 | 0.576 | 0.547 | 0.272 | 0.558 | 0.533 |
| Retrieval Only | 0.564 | 0.728 | 0.508 | 0.572 | 0.556 | 0.320 | 0.574 | 0.546 |
| Fixed Ranker | 0.578 | 0.735 | 0.514 | 0.578 | 0.560 | 0.315 | 0.588 | 0.553 |
| **CoSearch** | **0.582** | **0.747** | **0.527** | **0.595** | **0.587** | **0.334** | **0.601** | **0.568** |
| Oracle | - | - | - | - | - | - | - | 0.626 |

**3B results:**

| Method | NQ | TriviaQA | PopQA | HotpotQA | 2Wiki | Musique | Bamboogle | Avg |
|---|---|---|---|---|---|---|---|---|
| Search-R1 | 0.458 | 0.637 | 0.460 | 0.450 | 0.397 | 0.179 | 0.414 | 0.428 |
| Fixed Ranker | 0.515 | 0.697 | 0.483 | 0.474 | 0.411 | 0.195 | 0.448 | 0.460 |
| **CoSearch** | **0.538** | **0.714** | **0.489** | **0.478** | **0.428** | **0.193** | **0.457** | **0.471** |

**Effect of K (number of documents shown to agent, Table 4):**
- K=1: CoSearch degrades 5.3% vs K=5
- K=3: CoSearch achieves 0.561, surpassing Fixed Ranker at K=10 (0.559) -- demonstrating quality gains translate to efficiency
- K >= 10: diminishing returns (+0.5-1.6%)

**Ablation results (Table 3, 7B avg F1):**
- Full model: 0.568
- Without r_main: 0.560 (-1.4%)
- Without r_rel: 0.552 (-2.8%)
- Hit@k replaced with nDCG@k: 0.556 (-2.1%)
- Composite replaced with LLM-as-judge: 0.558 (-1.8%)
- Without semantic grouping: 0.549 (-3.3%) -- **largest single-component degradation**
- Shared backbone: 0.559 (-1.6%)
- Cross-encoder ranker: 0.551 (-2.9%)
- 3B ranker: training diverged

---

## 8. Limitations Acknowledged or Apparent

**Acknowledged/implicit:**
- The paper does NOT have a dedicated limitations section
- The 3B ranker caused training divergence, suggesting a minimum model capacity is needed for the generative listwise ranking task over 50 candidates
- The first-stage dense retriever (E5 base) is frozen -- the paper does not train it, meaning the candidate set quality is still bounded by E5's recall

**Apparent limitations not explicitly discussed:**
- **Corpus scope:** All evaluation uses the 2018 Wikipedia corpus, not open-web search. Generalization to heterogeneous web corpora is untested
- **Task scope:** Only question-answering benchmarks are evaluated; no evaluation on summarization, fact verification, or other knowledge-intensive tasks
- **Scale:** Only tested with 3B and 7B models; behavior with larger models (70B+) is unknown
- **Pseudo-relevance labels:** The relevance reward uses string matching (whether document contains gold answer) as a proxy for relevance -- this is noisy and could misattribute relevance
- **Training cost:** Joint training of two 7B models with G=8 trajectories per query, rollout batch of 512, is computationally expensive, but no training cost analysis is provided
- **Fixed retriever recall ceiling:** If the dense retriever fails to include any relevant document in the top-50, the ranker cannot help -- the paper partially addresses this with the I_ans=0 case but doesn't quantify how often this occurs
- **License:** The code is CC BY-NC 4.0 (non-commercial only), limiting practical adoption

---

## 9. Reviewer Comments

**No reviewer comments were found.** The paper is listed as "In Submission" on the first author's homepage (Hansi Zeng at UMass Amherst). It was posted to arXiv on April 19, 2026 (v2: April 21, 2026). No OpenReview page for this specific paper exists in search results. The paper has not yet appeared at any conference. The venue it has been submitted to is not publicly disclosed.

For context, the first author's prior work Search-R1 was accepted at COLM 2025, which may suggest a similar top venue target for CoSearch.

---

**Key sources:**
- [arXiv abstract page](https://arxiv.org/abs/2604.17555)
- [arXiv HTML full paper](https://arxiv.org/html/2604.17555v2)
- [GitHub repository](https://github.com/snap-research/CoSearch)
- [Hansi Zeng's homepage](https://hansizeng.github.io/)

agentId: a957f5be43da189c5 (use SendMessage with to: 'a957f5be43da189c5' to continue this agent)
&lt;usage>total_tokens: 24547
tool_uses: 12
duration_ms: 188036&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcbad8eb-2b9e-4dd1-bb39-5ce8f5814dc8",
  "isSidechain": false,
  "promptId": "509b9e27-9338-43ac-a97b-3de5e1bfe6b5",
  "type": "user",
  "uuid": "50235bc6-e4c7-45dc-84f0-42c793888362",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"CoSearch: Joint Training of Reasoning and Document Ranking via Reinforcement Learning for Agentic Search\" by Hansi Zeng et al. (arXiv 2026, https://arxiv.org/abs/2604.17555).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also try searching for any OpenReview page with reviewer comments.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined (especially GRPO, semantic query grouping, composite rewards)\n5. Their core technical method in detail (joint training of reasoning agent and document ranker, reward structure)\n6. Their main results - especially the 26.8% bottleneck claim about fixed retrieval\n7. Benchmarks used and performance numbers\n8. Limitations acknowledged or apparent\n9. Any reviewer comments if available\n\nPlease be thorough and precise. Report all findings in detail.",
    "agentId": "a957f5be43da189c5",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the full detailed report.\n\n---\n\nHere is a thorough extraction of all requested information from the CoSearch paper (arXiv:2604.17555).\n\n---\n\n## 1. The Exact Gap/Problem Identified and How They Identified It\n\nThe authors identified that existing agentic search systems (like Search-R1) treat the retrieval component as a **fixed, frozen tool**, optimizing only the reasoning agent via RL while the retrieval system remains unchanged. They hypothesized that retrieval quality itself is a major bottleneck.\n\n**How they identified it:** They designed an **oracle retrieval experiment**. For every sub-query issued by a trained reasoning agent, they promoted all documents containing the gold answer to the top positions in the ranking. For sub-queries where no retrieved document contained the gold answer, the ranking was left unchanged. The results were striking:\n\n- **7B agent (Qwen2.5-7B-Instruct):** Single-hop average improved from 0.600 to 0.709 (+18.2% relative), multi-hop from 0.506 to 0.564 (+11.5%), overall **+14.7% relative F1**\n- **3B agent (Qwen2.5-3B-Instruct):** Single-hop improved from 0.531 to 0.636 (+19.8%), multi-hop from 0.371 to 0.499 (+34.5%), overall **+26.8% relative F1**\n\nThe smaller model showed a larger gap, indicating weaker models are even more dependent on retrieval quality. The authors concluded: \"the retrieval system is a key bottleneck in scaling agentic search performance.\"\n\n---\n\n## 2. Their Key Insight That Others Missed\n\nTwo main insights:\n\n**Insight 1:** Prior work (Search-R1, Agentic-R, etc.) optimized only one side of the agentic search pipeline. Search-R1 trains only the reasoning agent; Agentic-R trains a dense retriever using LLM-annotated labels but does so offline/separately, not jointly. CoSearch's insight is that the reasoning agent and retrieval system are **interdependent** and must be **co-optimized** -- the agent's sub-queries shape what the ranker sees, and the ranker's outputs shape what the agent reasons over.\n\n**Insight 2:** The non-trivial technical challenge of applying GRPO to a **ranker** within an agentic pipeline. GRPO requires multiple responses generated from **identical input prompts** to compute group-relative advantages. For the main agent, this is straightforward (same initial query q0 produces G trajectories). But for the ranker, different trajectories produce **different sub-queries** at each step, meaning the ranker never sees identical inputs across rollouts. The authors recognized this as a fundamental obstacle and solved it with semantic query grouping.\n\n---\n\n## 3. How They Formulated the Problem Differently from Prior Work\n\nPrior work treats agentic search as a single-agent RL problem where the retrieval system is an environment component. CoSearch formulates it as a **joint optimization** of two policies:\n\n- **Main agent policy** `π_θmain`: Generates reasoning traces, sub-queries, and final answers\n- **Generative ranker policy** `π_θgr`: Takes N candidate documents from a fixed dense retriever and selects/reorders the top K\n\nThe trajectory is formalized as: `y = (q0, τ1, q1, o1, τ2, q2, o2, ..., τm, qm, om, τm+1, a)` where τt are reasoning thoughts, qt are sub-queries, and ot are observations (retrieved documents).\n\nThe optimization objective is: `max_{θmain, θgr} E[r(T)]`\n\nThe key architectural decomposition: retrieval is split into a **fixed dense retriever** (E5 base producing N=50 candidates) and a **trainable generative listwise ranker** (selecting K=5 documents). This decomposition is critical because it makes the ranker amenable to RL training (generating permutation sequences as text) while keeping first-stage retrieval efficient.\n\n---\n\n## 4. Existing Techniques They Adapted/Combined\n\n**GRPO (Group Relative Policy Optimization):** Originally from DeepSeek-R1 and related work. CoSearch applies GRPO to both the main agent (standard application) and the ranker (novel application requiring semantic grouping). The GRPO objective uses importance sampling ratios and group-normalized advantages with clipping: `1/G Σ Σ m(i,t) min(ρ(i,t) * Â(i), clip(ρ(i,t), 1-ε, 1+ε) * Â(i))`\n\n**Semantic Query Grouping:** A novel technique that clusters sub-queries using token-level F1 similarity with threshold δ=0.8. A sub-query q enters group gm if `F1_token(q, q_m_rep) ≥ δ`. Groups with fewer than kmin=3 members are discarded. This has **zero additional sampling cost** -- it reuses trajectories already generated for the main agent, avoiding the exponential rollout explosion that would occur if you tried to separately sample G ranker outputs for each unique sub-query.\n\n**Composite Rewards:** The ranker reward combines:\n- **Relevance reward (r_rel):** Average Hit@k over k ∈ {1, 3, 5}, using pseudo-relevant labels (documents containing the gold answer string)\n- **Main agent reward (r_main):** Token-level F1 between predicted and gold answers (trajectory-level signal)\n- Three-case composite structure based on whether answer-containing documents exist among candidates (I_ans) and a relevance threshold γ=0.5:\n  - When I_ans=1 and r_rel ≤ γ: use r_rel alone (ranker needs to focus on precision)\n  - When I_ans=1 and r_rel > γ: use r_rel + r_main (ranking is sufficient, add trajectory signal)\n  - When I_ans=0: use r_main alone (no relevant document to rank, so use trajectory-level feedback only)\n  - Format violation: -0.2 penalty\n\n**ReAct-style prompting:** The agent uses a structured format with reasoning and tool-use steps.\n\n**Generative listwise ranking:** The ranker generates a permutation of document identifiers as text output (rather than pointwise scoring), adapted from prior work on LLMs as listwise rankers.\n\n---\n\n## 5. Core Technical Method in Detail\n\n**Architecture:**\n- Main agent: Qwen2.5-7B-Instruct (or 3B)\n- Generative ranker: Separate Qwen2.5-7B-Instruct model (separate parameters from agent)\n- Dense retriever: E5 base (frozen), retrieves N=50 candidates from 18M-passage Wikipedia 2018 corpus via FAISS GPU index\n- The ranker takes the 50 candidates and produces a ranked list, from which the top K=5 are shown to the agent\n\n**Training Loop:**\n1. Sample G=8 trajectories per initial query q0 using the current main agent policy\n2. At each search step, the agent issues a sub-query; the dense retriever returns N=50 candidates; the ranker selects K=5\n3. After trajectory completion, compute main agent rewards (token-level F1 with gold answer, or -0.2 for format violations)\n4. For ranker training: apply semantic grouping to cluster sub-queries across the G trajectories; compute composite rewards; apply GRPO\n5. Update both policies simultaneously\n\n**Main Agent Reward:**\n- Token-level F1 between predicted answer and gold answer (if format-compliant)\n- -α (α=0.2) penalty for format violations\n\n**Ranker Reward (the composite structure described above):**\nThe key design choice is the three-case structure. When relevant documents exist but ranking is poor (r_rel ≤ γ), only the ranking quality signal is used -- this focuses the ranker on getting the right documents to the top. When ranking is already good (r_rel > γ), the trajectory-level signal is added to encourage rankings that not only have relevant documents but also help the downstream reasoning agent. When no relevant documents exist in the candidate set, only the trajectory-level signal is used since the ranker can't be blamed for missing documents.\n\n**Why Hit@k over nDCG@k:** Ablations show Hit@k outperforms nDCG@k by 2.1% -- the authors explain this is because Hit@k provides a clearer binary signal about whether relevant documents appear in top positions.\n\n**Why not shared backbone:** Using a shared model for both agent and ranker degraded performance by 1.6%, attributed to conflicting gradient signals between the two tasks.\n\n**Why not cross-encoder ranker:** Cross-encoders perform pointwise scoring, which is unsuitable for direct RL optimization via GRPO. The generative listwise approach (-2.9% with cross-encoder) allows the ranker to produce sequences that can be treated as policy outputs.\n\n---\n\n## 6. Main Results -- The 26.8% Bottleneck Claim\n\nThe 26.8% figure comes specifically from the **oracle retrieval experiment** on the **3B agent**, representing the relative F1 improvement when answer-containing documents are promoted to top positions. This is NOT a result of CoSearch itself, but rather the motivation experiment showing **how much room exists for improvement** if retrieval were perfect.\n\nCoSearch itself achieves:\n- **7B: 0.568 avg F1** vs Search-R1's 0.533 (+6.6% relative improvement)\n- **3B: 0.471 avg F1** vs Search-R1's 0.428 (+10.0% relative improvement)\n- Oracle upper bound for 7B: 0.626\n\nCoSearch closes approximately **27% of the gap** between Search-R1 and the oracle upper bound across both scales.\n\n---\n\n## 7. Benchmarks Used and Performance Numbers\n\n**Seven QA benchmarks:**\n- Single-hop: NQ (Natural Questions), TriviaQA, PopQA\n- Multi-hop: HotpotQA, 2WikiMultiHopQA, Musique, Bamboogle\n\n**Full per-dataset results (7B, token-level F1):**\n\n| Method | NQ | TriviaQA | PopQA | HotpotQA | 2Wiki | Musique | Bamboogle | Avg |\n|---|---|---|---|---|---|---|---|---|\n| Direct Inference | - | - | - | - | - | - | - | 0.298 |\n| RAG | - | - | - | - | - | - | - | 0.365 |\n| Search-R1 | 0.556 | 0.681 | 0.539 | 0.576 | 0.547 | 0.272 | 0.558 | 0.533 |\n| Retrieval Only | 0.564 | 0.728 | 0.508 | 0.572 | 0.556 | 0.320 | 0.574 | 0.546 |\n| Fixed Ranker | 0.578 | 0.735 | 0.514 | 0.578 | 0.560 | 0.315 | 0.588 | 0.553 |\n| **CoSearch** | **0.582** | **0.747** | **0.527** | **0.595** | **0.587** | **0.334** | **0.601** | **0.568** |\n| Oracle | - | - | - | - | - | - | - | 0.626 |\n\n**3B results:**\n\n| Method | NQ | TriviaQA | PopQA | HotpotQA | 2Wiki | Musique | Bamboogle | Avg |\n|---|---|---|---|---|---|---|---|---|\n| Search-R1 | 0.458 | 0.637 | 0.460 | 0.450 | 0.397 | 0.179 | 0.414 | 0.428 |\n| Fixed Ranker | 0.515 | 0.697 | 0.483 | 0.474 | 0.411 | 0.195 | 0.448 | 0.460 |\n| **CoSearch** | **0.538** | **0.714** | **0.489** | **0.478** | **0.428** | **0.193** | **0.457** | **0.471** |\n\n**Effect of K (number of documents shown to agent, Table 4):**\n- K=1: CoSearch degrades 5.3% vs K=5\n- K=3: CoSearch achieves 0.561, surpassing Fixed Ranker at K=10 (0.559) -- demonstrating quality gains translate to efficiency\n- K >= 10: diminishing returns (+0.5-1.6%)\n\n**Ablation results (Table 3, 7B avg F1):**\n- Full model: 0.568\n- Without r_main: 0.560 (-1.4%)\n- Without r_rel: 0.552 (-2.8%)\n- Hit@k replaced with nDCG@k: 0.556 (-2.1%)\n- Composite replaced with LLM-as-judge: 0.558 (-1.8%)\n- Without semantic grouping: 0.549 (-3.3%) -- **largest single-component degradation**\n- Shared backbone: 0.559 (-1.6%)\n- Cross-encoder ranker: 0.551 (-2.9%)\n- 3B ranker: training diverged\n\n---\n\n## 8. Limitations Acknowledged or Apparent\n\n**Acknowledged/implicit:**\n- The paper does NOT have a dedicated limitations section\n- The 3B ranker caused training divergence, suggesting a minimum model capacity is needed for the generative listwise ranking task over 50 candidates\n- The first-stage dense retriever (E5 base) is frozen -- the paper does not train it, meaning the candidate set quality is still bounded by E5's recall\n\n**Apparent limitations not explicitly discussed:**\n- **Corpus scope:** All evaluation uses the 2018 Wikipedia corpus, not open-web search. Generalization to heterogeneous web corpora is untested\n- **Task scope:** Only question-answering benchmarks are evaluated; no evaluation on summarization, fact verification, or other knowledge-intensive tasks\n- **Scale:** Only tested with 3B and 7B models; behavior with larger models (70B+) is unknown\n- **Pseudo-relevance labels:** The relevance reward uses string matching (whether document contains gold answer) as a proxy for relevance -- this is noisy and could misattribute relevance\n- **Training cost:** Joint training of two 7B models with G=8 trajectories per query, rollout batch of 512, is computationally expensive, but no training cost analysis is provided\n- **Fixed retriever recall ceiling:** If the dense retriever fails to include any relevant document in the top-50, the ranker cannot help -- the paper partially addresses this with the I_ans=0 case but doesn't quantify how often this occurs\n- **License:** The code is CC BY-NC 4.0 (non-commercial only), limiting practical adoption\n\n---\n\n## 9. Reviewer Comments\n\n**No reviewer comments were found.** The paper is listed as \"In Submission\" on the first author's homepage (Hansi Zeng at UMass Amherst). It was posted to arXiv on April 19, 2026 (v2: April 21, 2026). No OpenReview page for this specific paper exists in search results. The paper has not yet appeared at any conference. The venue it has been submitted to is not publicly disclosed.\n\nFor context, the first author's prior work Search-R1 was accepted at COLM 2025, which may suggest a similar top venue target for CoSearch.\n\n---\n\n**Key sources:**\n- [arXiv abstract page](https://arxiv.org/abs/2604.17555)\n- [arXiv HTML full paper](https://arxiv.org/html/2604.17555v2)\n- [GitHub repository](https://github.com/snap-research/CoSearch)\n- [Hansi Zeng's homepage](https://hansizeng.github.io/)"
      }
    ],
    "totalDurationMs": 188036,
    "totalTokens": 24547,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 18554,
      "output_tokens": 3939,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3939,
          "cache_read_input_tokens": 18554,
          "cache_creation_input_tokens": 2053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2053,
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
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "fcbad8eb-2b9e-4dd1-bb39-5ce8f5814dc8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T06:31:53.875Z_

<details><summary>↩ Tool result · `toolu_01SjR8WE5XbuuczSA7DGMMhU`</summary>

```text
The OpenReview page requires authentication and the reviewer comments are not publicly indexed. I now have comprehensive information from the full paper. Let me compile the detailed findings.

Here is my thorough analysis of the paper "RaDeR: Reasoning-aware Dense Retrieval Models" by Debrup Das, Sam O'Nuallain, and Razieh Rahimi (UMass Amherst), published at EMNLP 2025 Main Conference.

---

## 1. The Exact Gap/Problem They Identified

**The core problem:** Retrieval models for LLM augmentation perform well at lexical and semantic term matching, but they fail when *reasoning* is needed to determine relevance. The paper cites Su et al. (2024) and the BRIGHT benchmark as evidence of this gap.

**How they identified it:** They use a concrete motivating example (Figure 1 in the paper) from the TheoremQA/pigeonhole3 split of BRIGHT. A question about cookies and shapes requires retrieving the *Pigeonhole Principle*, but there is **no lexical or semantic overlap** between the question and the relevant theorem. Furthermore, when GPT-4 generates Chain-of-Thought (CoT) reasoning steps as queries, those steps merely outline the *application* of the Pigeonhole Principle rather than describing the principle itself -- so CoT does not simplify retrieval either.

**Two specific sub-gaps identified:**
- (a) Prior work on interleaving reasoning with retrieval (IRCoT, ITER-RETGEN, ReAct) uses *off-the-shelf* retrievers -- the reasoning helps query formulation but the retriever itself has no reasoning capability.
- (b) Reasoning-based re-rankers (RANK-1, InteRank) are inherently limited by the candidate set from the first-stage retriever, which is typically lexical/semantic-matching-based.

**Their key claim:** "To the best of our knowledge, there are *no first-stage reasoning-based retrieval models*." This is the gap they aim to fill.

---

## 2. Their Key Insight That Others Missed

The central insight is **dual-purpose exploitation of MCTS-based mathematical problem solving for retrieval training data generation**:

1. **Reasoning trajectories as natural training queries:** When an LLM solves math problems using retrieval-augmented MCTS, the intermediate reasoning steps (partial CoT solutions) at the point where a retrieval action occurs naturally form queries that require reasoning to connect to the retrieved theorem. These are *organically diverse* in format, length, and reasoning complexity.

2. **Answer correctness as a proxy for relevance evaluation:** Verifying whether the LLM's final answer matches the gold answer provides a *scalar reward signal* that can be backpropagated to evaluate whether retrieved theorems were useful -- without needing explicit human relevance labels.

3. **Self-reflection as hard negative generation:** Theorems retrieved during MCTS that are judged "non-relevant" by the LLM's self-reflection become hard negatives. These are challenging negatives because they were surfaced by a retriever in a plausible reasoning context.

4. **Mathematical reasoning generalizes to other reasoning domains.** Despite training exclusively on math problems, the resulting retrievers generalize to coding, biology, earth science, economics, psychology, and other domains in BRIGHT/RAR-b. They hypothesize this is because many tasks (especially coding) have underlying mathematical substructure.

---

## 3. How They Formulated the Problem Differently from Prior Work

**Prior formulation (interleaved reasoning + retrieval):** The retriever is fixed; the innovation is in how the LLM generates queries or sequences retrieval calls (Search-R1, R1-Searcher use RL for query generation).

**Prior formulation (reasoning re-rankers):** RANK-1 distills reasoning from DeepSeek-R1 into a re-ranker; InteRank uses RL. But re-rankers are second-stage and depend on the first-stage retriever's recall.

**Prior formulation (data augmentation for IR):** Methods like Promptagator generate queries from documents using LLMs, but this limits diversity and makes it hard to verify that generated queries genuinely require reasoning for retrieval.

**RaDeR's reformulation:** They frame the problem as *training a first-stage dense retriever to perform reasoning for relevance prediction*. The key difference is they don't just generate queries from passages -- they generate queries from the *reasoning process of solving problems that require those passages*. The MCTS framework provides:
- Natural diversity in query types (CoT steps at different depths)
- Automatic relevance labels (correct answer = relevant retrieval)
- Hard negatives (retrieved-but-non-relevant theorems)
- No need for human annotations or LLM-as-judge scalar scores

This contrasts specifically with **ReasonIR** (Shao et al., 2025), which also trains reasoning-based first-stage retrievers but generates queries without labeled scalar rewards and uses a much larger dataset (1.73M samples vs. RaDeR's 43K-121K).

---

## 4. Existing Techniques They Adapted/Combined/Simplified

**MCTS (Monte Carlo Tree Search):** They extend the rStar framework (Qi et al., 2025) by adding two new actions to the standard MCTS action space: *Generate Query (QG)* and *Retrieve Theorem (RT)*. The standard rStar actions they keep are *One Step Thought (OST)* and *Complete Remaining Solution (CRS)*. The MCTS uses UCT (Upper Confidence Bounds applied to Trees) for node selection:

UCT(s,a) = Q(s,a)/N(s,a) + c * sqrt(ln(N_parent(s)) / N(s,a))

The reward function R(t) is binary: R(t) = 1 if the trajectory reaches the correct answer, R(t) = 0 otherwise.

**Self-reflection (from Self-RAG, Asai et al., 2023; Xia et al., 2025):** Used to evaluate whether retrieved theorems are relevant. The LLM generates both a relevance label ("relevant" or "non-relevant") and a supporting explanation. Only theorems labeled relevant are added to the MCTS tree; non-relevant ones are pruned and become hard negatives.

**Self-summarization:** After a theorem passes self-reflection, the LLM generates a concise natural-language summary to facilitate integration into subsequent reasoning steps.

**Contrastive learning (InfoNCE loss):** Standard for dense retriever training. The retriever uses a uni-embedding bi-encoder architecture (Lei et al., 2023). The re-ranker uses a pointwise cross-attention architecture.

**Promptagator-style round-trip consistency (Dai et al., 2023):** Used specifically for generating lexical queries -- only queries for which BM25 retrieves the positive theorem in top-20 are kept, ensuring high term overlap.

**RepLLaMA (Ma et al., 2023):** Used as the retriever within the MCTS process itself. The retrieval corpus is ProofWiki (20K+ formal theorems).

---

## 5. Core Technical Method in Detail

### 5.1 Retrieval-Augmented MCTS Framework

**Input:** A math problem M from MATH or NuminaMath datasets, with a gold answer G.

**Action space A with 4 actions:**

- **A1: One Step Thought (OST):** LLM generates a single CoT reasoning step s_i given context M + s_1 + ... + s_{i-1}. Can be a terminal node if it contains a boxed answer.

- **A2: Complete Remaining Solution (CRS):** LLM generates the complete remaining solution from the current state. Always a terminal node.

- **A3: Generate Query (QG):** LLM generates a retrieval query s_QG based on the current context. Always followed by a Retrieve Theorem action. Uses few-shot prompting to produce a hypothetical theorem description (to help term-matching retrievers find it).

- **A4: Retrieve Theorem (RT):** Uses RepLLaMA to retrieve top-k theorems from ProofWiki using query s_QG. Each retrieved theorem undergoes self-reflection. Those passing are added as child nodes.

**MCTS parameters (Table 8):**
- 5 RT nodes per action (top-k=5)
- 2 OST nodes added per action
- 1 QG node added per action
- 16 rollouts
- Max depth 6
- Exploration weight C = 2
- LLM_gen temperature 0.8, top-k 40, top-p 0.95
- 2 A100 GPUs

### 5.2 Training Data Synthesis

From completed MCTS rollouts, they extract high-reward solution trajectories S = M + s_1 + ... + s_QG + s_RT + ... + s_t that contain at least one retrieval node. The retrieved theorem s_RT becomes the positive document p.

**Three types of reasoning-intensive queries are generated per (positive, negative) pair:**

1. **MCTS CoT reasoning queries (q_CoT):** The partial solution up to the query node: M + s_1 + ... + s_{parent(QG)}. These are the actual reasoning steps the LLM was performing when it needed retrieval.

2. **LLM reasoning queries (q_llmq):** Generated by prompting LLM_gen with M, the reasoning context, and the theorem s_RT. The LLM produces a concise query reflecting the information need. Unlike QG queries (which are designed for term-matching retrievers), q_llmq is designed to have low lexical/semantic overlap with the positive theorem.

3. **Question queries (q_question):** Simply the math question M itself.

**One type of term-matching query:**

4. **Lexical queries (q_lexical):** Generated by prompting the LLM using only the theorem s_RT (no problem context). Filtered with round-trip consistency: only kept if BM25 retrieves s_RT in top-20.

**Hard negatives:** Theorems retrieved during MCTS but labeled non-relevant by self-reflection.

### 5.3 Dataset Statistics (Table 9)

| Dataset | q_llmq | q_CoT | q_question | q_lexical | Total |
|---------|--------|-------|------------|-----------|-------|
| MATH | 18,586 | 7,312 | 7,312 | 9,910 | 43,120 |
| NuminaMath | 39,639 | 24,280 | 10,241 | 4,158 | 78,318 |
| Combined | - | - | - | - | 121,438 |

### 5.4 Model Training

**Retriever:** Uni-embedding bi-encoder. Embedding = last token (EOS) representation from the decoder LLM. Relevance = cosine similarity. Trained with InfoNCE contrastive loss using 12 hard negatives per query + in-batch negatives. Base models: Qwen2.5-instruct variants (3B, 7B, 14B), gte-Qwen2-7B, Llama-3.1-8B-Instruct.

Training hyperparameters: batch size 12 (train group size), 28 warmup steps, per-device batch size 2, gradient accumulation 16, temperature 0.01, learning rate 1e-4, linear scheduler, 1 epoch, BF16, 2 A100s.

**Re-ranker:** Pointwise cross-attention model. Input = "query: {q} document: {d} &lt;eos>". Score = Linear(Decoder(input)[-1]). Same contrastive loss but no in-batch negatives. Also trained on the same synthesized data.

---

## 6. Main Results

### 6.1 BRIGHT Benchmark (Tables 1 and 2)

**With original questions as queries (Table 1):**
- RaDeR gte-Qwen2-7B achieves **25.5 avg nDCG@10** (best among all models)
- This outperforms BM25 (14.5), Qwen* (22.5), GritLM* (21.0), Inst-XL* (18.9), Google* (20.0), Voyage* (17.9)
- The improvement is at least **2 points** over the best baseline
- **Math splits:** TheoQ improved by **12.1 points** over best baseline; TheoT by large margins
- **Coding splits:** LeetCode at 37.0-38.6 (best), surpassing baselines by **8+ points**

**With GPT-4 CoT reasoning as queries (Table 2):**
- RaDeR achieves **27.3-29.2 avg** depending on configuration
- **This is where the BM25 comparison is critical:** BM25 on CoT queries scores 27.0 avg, while BM25 on original questions scores only 14.5. CoT queries actually *help* BM25 significantly due to added terms.
- RaDeR is stated to be the **first dense retriever that outperforms BM25 when queries are CoT reasoning steps**. In Table 2, RaDeR gte-Qwen2-7B with MATH dataset achieves 29.2 avg vs BM25's 27.0 on CoT queries.
- Notably, most dense baselines (Qwen*, E5*, etc.) score well below BM25 on CoT queries.

### 6.2 RAR-b / MMTEB (Table 3)

On the Math and Coding splits of RAR-b:
- RaDeR gte-Qwen2-7B-instruct: Math **0.852**, Coding **0.835**
- This is comparable to OpenAI-3-large (Math 0.877, Coding 0.894) and significantly outperforms all open-source models
- GritLM (previously best open-source): Math 0.824, Coding 0.838

### 6.3 MS MARCO (Table 4)

RaDeR achieves competitive performance (MRR@10 34.4, DL19 71.2, DL20 70.7) compared to RepLLaMA (41.2/74.3/72.1) and SimLM (41.1/71.4/69.7). The point is that reasoning training does **not hurt** standard term-matching retrieval significantly.

### 6.4 Comparison with ReasonIR

- RaDeR achieves a **1.1 point increase in nDCG@10** over ReasonIR, corresponding to a **4.5% relative gain**
- This is despite using only **43,120 samples** (MATH only) vs ReasonIR's **1,729,368 samples**
- That ratio is approximately **2.5%** of ReasonIR's training data

### 6.5 Re-ranking Results (Tables 5 and 6)

- RaDeR re-rankers outperform GPT-4 in re-ranking by **+2.5** and **+2.1** nDCG points in the top-100 setting
- Most significant improvements on LeetCode (+20.3 points) and TheoremQA (+20.4 points)
- RANK-1 (Weller et al., 2025), trained on 635K MS MARCO examples with test-time compute reasoning, is the strongest baseline at 27.5 avg; RaDeR achieves 25.7-26.7 avg (competitive but not always better)

### 6.6 RAG Performance (Table 7)

On TheoremQA (BRIGHT), Qwen-2.5-7B-Instruct:
- No retrieval: 71.0%
- In-context RAG with RaDeR: 75.0%
- In-context RAG with RepLLaMA: 72.6%
- In-context RAG with gold theorems: 77.6%
- MCTS with OST + RaDeR retrieval: 80.2%
- MCTS with OST + gold theorems: 81.5%

---

## 7. The Sample Efficiency Claim (2.5% of ReasonIR's Data)

**Exact numbers:**
- RaDeR trained on MATH only: **43,120 samples**
- ReasonIR: **1,729,368 samples**
- Ratio: 43,120 / 1,729,368 = approximately **2.49%**, rounded to **2.5%**

**The comparison is fair in that** both are first-stage reasoning-based retrieval models. RaDeR achieves 1.1 nDCG@10 points higher (4.5% relative improvement) on BRIGHT.

**Why the efficiency:** The authors attribute this to the quality of their synthesized data. The MCTS framework with self-reflection produces training samples where: (a) relevance is verified through answer correctness, (b) hard negatives are naturally generated from the retrieval process, and (c) query diversity comes from different stages of the reasoning tree. ReasonIR, by contrast, generates queries "without labeled scalar rewards."

---

## 8. Limitations (Acknowledged and Apparent)

### Explicitly Acknowledged (Section 8):

1. **Single-document reasoning only:** The training approach focuses on retrieving one relevant document at a time. It cannot handle multi-hop QA tasks where relevance of one document depends on the content of others.

2. **No explanations for retrieval decisions:** RaDeR produces relevance scores but not explanations. Future work could explore generating reasoning explanations while maintaining first-stage efficiency.

3. **Noisy training data from reward signals:** The reward is based on final answer correctness, but an incorrect CoT reasoning path can still lead to a correct final answer, making some training data noisy.

### Apparent/Implicit Limitations:

4. **Dependency on math domain for data generation:** The entire data generation pipeline requires math problems with verifiable answers and a theorem corpus (ProofWiki). Extending to other domains would require analogous structured knowledge bases and verification mechanisms.

5. **MS MARCO performance regression:** Table 4 shows RaDeR underperforms RepLLaMA and SimLM on standard term-matching benchmarks (MRR@10: 34.4 vs 41.2 for RepLLaMA), suggesting some trade-off between reasoning and standard retrieval capabilities.

6. **Failure on certain reasoning types:** Figure 5 shows a failure case where both RaDeR and Qwen2 fail on a family tree / graph theory question about acyclicity, retrieving a theorem about arborescences instead of the gold theorem about girth. Surface-level similarity still misleads the model.

7. **Computational cost of data generation:** MCTS with 16 rollouts, max depth 6, and retrieval at each step is expensive. The paper uses 2 A100 GPUs and processes MATH + NuminaMath datasets.

8. **Limited re-ranker comparison:** The re-ranker does not consistently beat RANK-1 (which uses 635K samples from MS MARCO), and RANK-1 uses test-time compute for reasoning while RaDeR does not.

---

## 9. Reviewer Comments

The OpenReview page (id=mH2r897uSZ) requires authentication and the reviewer comments are not publicly accessible through web search or unauthenticated access. The paper was accepted at EMNLP 2025 Main Conference (pages 19970-19997), indicating it passed peer review. No specific reviewer scores, strengths/weaknesses lists, or discussion threads could be retrieved.

---

**Key sources consulted:**
- [arXiv page](https://arxiv.org/abs/2505.18405)
- [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1011/)
- [Project website](https://debrup-61.github.io/RaDeR.github.io/)
- [GitHub repository](https://github.com/debrup-61/rader)
- [Full PDF](https://arxiv.org/pdf/2505.18405) (26 pages, all read)

agentId: a93d481c353d6f824 (use SendMessage with to: 'a93d481c353d6f824' to continue this agent)
&lt;usage>total_tokens: 46450
tool_uses: 14
duration_ms: 229686&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cd9bec28-2868-4757-8abb-b2eed2b46b26",
  "isSidechain": false,
  "promptId": "509b9e27-9338-43ac-a97b-3de5e1bfe6b5",
  "type": "user",
  "uuid": "e5a01c22-786e-4c4f-8dd5-78ac1983e559",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"RaDeR: Reasoning-aware Dense Retrieval Models\" by Debrup Das et al. (EMNLP 2025, https://arxiv.org/abs/2505.18405).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also try searching for any OpenReview page with reviewer comments.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined/simplified (especially MCTS usage)\n5. Their core technical method in detail (MCTS-based reasoning trajectories, self-reflective relevance evaluation, training procedure)\n6. Their main results, especially comparison with BM25 on CoT queries and comparison with ReasonIR\n7. The claim about sample efficiency (2.5% of ReasonIR's data)\n8. Limitations acknowledged or apparent\n9. Any reviewer comments if available\n\nPlease be thorough and precise. Report all findings in detail.",
    "agentId": "a93d481c353d6f824",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "The OpenReview page requires authentication and the reviewer comments are not publicly indexed. I now have comprehensive information from the full paper. Let me compile the detailed findings.\n\nHere is my thorough analysis of the paper \"RaDeR: Reasoning-aware Dense Retrieval Models\" by Debrup Das, Sam O'Nuallain, and Razieh Rahimi (UMass Amherst), published at EMNLP 2025 Main Conference.\n\n---\n\n## 1. The Exact Gap/Problem They Identified\n\n**The core problem:** Retrieval models for LLM augmentation perform well at lexical and semantic term matching, but they fail when *reasoning* is needed to determine relevance. The paper cites Su et al. (2024) and the BRIGHT benchmark as evidence of this gap.\n\n**How they identified it:** They use a concrete motivating example (Figure 1 in the paper) from the TheoremQA/pigeonhole3 split of BRIGHT. A question about cookies and shapes requires retrieving the *Pigeonhole Principle*, but there is **no lexical or semantic overlap** between the question and the relevant theorem. Furthermore, when GPT-4 generates Chain-of-Thought (CoT) reasoning steps as queries, those steps merely outline the *application* of the Pigeonhole Principle rather than describing the principle itself -- so CoT does not simplify retrieval either.\n\n**Two specific sub-gaps identified:**\n- (a) Prior work on interleaving reasoning with retrieval (IRCoT, ITER-RETGEN, ReAct) uses *off-the-shelf* retrievers -- the reasoning helps query formulation but the retriever itself has no reasoning capability.\n- (b) Reasoning-based re-rankers (RANK-1, InteRank) are inherently limited by the candidate set from the first-stage retriever, which is typically lexical/semantic-matching-based.\n\n**Their key claim:** \"To the best of our knowledge, there are *no first-stage reasoning-based retrieval models*.\" This is the gap they aim to fill.\n\n---\n\n## 2. Their Key Insight That Others Missed\n\nThe central insight is **dual-purpose exploitation of MCTS-based mathematical problem solving for retrieval training data generation**:\n\n1. **Reasoning trajectories as natural training queries:** When an LLM solves math problems using retrieval-augmented MCTS, the intermediate reasoning steps (partial CoT solutions) at the point where a retrieval action occurs naturally form queries that require reasoning to connect to the retrieved theorem. These are *organically diverse* in format, length, and reasoning complexity.\n\n2. **Answer correctness as a proxy for relevance evaluation:** Verifying whether the LLM's final answer matches the gold answer provides a *scalar reward signal* that can be backpropagated to evaluate whether retrieved theorems were useful -- without needing explicit human relevance labels.\n\n3. **Self-reflection as hard negative generation:** Theorems retrieved during MCTS that are judged \"non-relevant\" by the LLM's self-reflection become hard negatives. These are challenging negatives because they were surfaced by a retriever in a plausible reasoning context.\n\n4. **Mathematical reasoning generalizes to other reasoning domains.** Despite training exclusively on math problems, the resulting retrievers generalize to coding, biology, earth science, economics, psychology, and other domains in BRIGHT/RAR-b. They hypothesize this is because many tasks (especially coding) have underlying mathematical substructure.\n\n---\n\n## 3. How They Formulated the Problem Differently from Prior Work\n\n**Prior formulation (interleaved reasoning + retrieval):** The retriever is fixed; the innovation is in how the LLM generates queries or sequences retrieval calls (Search-R1, R1-Searcher use RL for query generation).\n\n**Prior formulation (reasoning re-rankers):** RANK-1 distills reasoning from DeepSeek-R1 into a re-ranker; InteRank uses RL. But re-rankers are second-stage and depend on the first-stage retriever's recall.\n\n**Prior formulation (data augmentation for IR):** Methods like Promptagator generate queries from documents using LLMs, but this limits diversity and makes it hard to verify that generated queries genuinely require reasoning for retrieval.\n\n**RaDeR's reformulation:** They frame the problem as *training a first-stage dense retriever to perform reasoning for relevance prediction*. The key difference is they don't just generate queries from passages -- they generate queries from the *reasoning process of solving problems that require those passages*. The MCTS framework provides:\n- Natural diversity in query types (CoT steps at different depths)\n- Automatic relevance labels (correct answer = relevant retrieval)\n- Hard negatives (retrieved-but-non-relevant theorems)\n- No need for human annotations or LLM-as-judge scalar scores\n\nThis contrasts specifically with **ReasonIR** (Shao et al., 2025), which also trains reasoning-based first-stage retrievers but generates queries without labeled scalar rewards and uses a much larger dataset (1.73M samples vs. RaDeR's 43K-121K).\n\n---\n\n## 4. Existing Techniques They Adapted/Combined/Simplified\n\n**MCTS (Monte Carlo Tree Search):** They extend the rStar framework (Qi et al., 2025) by adding two new actions to the standard MCTS action space: *Generate Query (QG)* and *Retrieve Theorem (RT)*. The standard rStar actions they keep are *One Step Thought (OST)* and *Complete Remaining Solution (CRS)*. The MCTS uses UCT (Upper Confidence Bounds applied to Trees) for node selection:\n\nUCT(s,a) = Q(s,a)/N(s,a) + c * sqrt(ln(N_parent(s)) / N(s,a))\n\nThe reward function R(t) is binary: R(t) = 1 if the trajectory reaches the correct answer, R(t) = 0 otherwise.\n\n**Self-reflection (from Self-RAG, Asai et al., 2023; Xia et al., 2025):** Used to evaluate whether retrieved theorems are relevant. The LLM generates both a relevance label (\"relevant\" or \"non-relevant\") and a supporting explanation. Only theorems labeled relevant are added to the MCTS tree; non-relevant ones are pruned and become hard negatives.\n\n**Self-summarization:** After a theorem passes self-reflection, the LLM generates a concise natural-language summary to facilitate integration into subsequent reasoning steps.\n\n**Contrastive learning (InfoNCE loss):** Standard for dense retriever training. The retriever uses a uni-embedding bi-encoder architecture (Lei et al., 2023). The re-ranker uses a pointwise cross-attention architecture.\n\n**Promptagator-style round-trip consistency (Dai et al., 2023):** Used specifically for generating lexical queries -- only queries for which BM25 retrieves the positive theorem in top-20 are kept, ensuring high term overlap.\n\n**RepLLaMA (Ma et al., 2023):** Used as the retriever within the MCTS process itself. The retrieval corpus is ProofWiki (20K+ formal theorems).\n\n---\n\n## 5. Core Technical Method in Detail\n\n### 5.1 Retrieval-Augmented MCTS Framework\n\n**Input:** A math problem M from MATH or NuminaMath datasets, with a gold answer G.\n\n**Action space A with 4 actions:**\n\n- **A1: One Step Thought (OST):** LLM generates a single CoT reasoning step s_i given context M + s_1 + ... + s_{i-1}. Can be a terminal node if it contains a boxed answer.\n\n- **A2: Complete Remaining Solution (CRS):** LLM generates the complete remaining solution from the current state. Always a terminal node.\n\n- **A3: Generate Query (QG):** LLM generates a retrieval query s_QG based on the current context. Always followed by a Retrieve Theorem action. Uses few-shot prompting to produce a hypothetical theorem description (to help term-matching retrievers find it).\n\n- **A4: Retrieve Theorem (RT):** Uses RepLLaMA to retrieve top-k theorems from ProofWiki using query s_QG. Each retrieved theorem undergoes self-reflection. Those passing are added as child nodes.\n\n**MCTS parameters (Table 8):**\n- 5 RT nodes per action (top-k=5)\n- 2 OST nodes added per action\n- 1 QG node added per action\n- 16 rollouts\n- Max depth 6\n- Exploration weight C = 2\n- LLM_gen temperature 0.8, top-k 40, top-p 0.95\n- 2 A100 GPUs\n\n### 5.2 Training Data Synthesis\n\nFrom completed MCTS rollouts, they extract high-reward solution trajectories S = M + s_1 + ... + s_QG + s_RT + ... + s_t that contain at least one retrieval node. The retrieved theorem s_RT becomes the positive document p.\n\n**Three types of reasoning-intensive queries are generated per (positive, negative) pair:**\n\n1. **MCTS CoT reasoning queries (q_CoT):** The partial solution up to the query node: M + s_1 + ... + s_{parent(QG)}. These are the actual reasoning steps the LLM was performing when it needed retrieval.\n\n2. **LLM reasoning queries (q_llmq):** Generated by prompting LLM_gen with M, the reasoning context, and the theorem s_RT. The LLM produces a concise query reflecting the information need. Unlike QG queries (which are designed for term-matching retrievers), q_llmq is designed to have low lexical/semantic overlap with the positive theorem.\n\n3. **Question queries (q_question):** Simply the math question M itself.\n\n**One type of term-matching query:**\n\n4. **Lexical queries (q_lexical):** Generated by prompting the LLM using only the theorem s_RT (no problem context). Filtered with round-trip consistency: only kept if BM25 retrieves s_RT in top-20.\n\n**Hard negatives:** Theorems retrieved during MCTS but labeled non-relevant by self-reflection.\n\n### 5.3 Dataset Statistics (Table 9)\n\n| Dataset | q_llmq | q_CoT | q_question | q_lexical | Total |\n|---------|--------|-------|------------|-----------|-------|\n| MATH | 18,586 | 7,312 | 7,312 | 9,910 | 43,120 |\n| NuminaMath | 39,639 | 24,280 | 10,241 | 4,158 | 78,318 |\n| Combined | - | - | - | - | 121,438 |\n\n### 5.4 Model Training\n\n**Retriever:** Uni-embedding bi-encoder. Embedding = last token (EOS) representation from the decoder LLM. Relevance = cosine similarity. Trained with InfoNCE contrastive loss using 12 hard negatives per query + in-batch negatives. Base models: Qwen2.5-instruct variants (3B, 7B, 14B), gte-Qwen2-7B, Llama-3.1-8B-Instruct.\n\nTraining hyperparameters: batch size 12 (train group size), 28 warmup steps, per-device batch size 2, gradient accumulation 16, temperature 0.01, learning rate 1e-4, linear scheduler, 1 epoch, BF16, 2 A100s.\n\n**Re-ranker:** Pointwise cross-attention model. Input = \"query: {q} document: {d} &lt;eos>\". Score = Linear(Decoder(input)[-1]). Same contrastive loss but no in-batch negatives. Also trained on the same synthesized data.\n\n---\n\n## 6. Main Results\n\n### 6.1 BRIGHT Benchmark (Tables 1 and 2)\n\n**With original questions as queries (Table 1):**\n- RaDeR gte-Qwen2-7B achieves **25.5 avg nDCG@10** (best among all models)\n- This outperforms BM25 (14.5), Qwen* (22.5), GritLM* (21.0), Inst-XL* (18.9), Google* (20.0), Voyage* (17.9)\n- The improvement is at least **2 points** over the best baseline\n- **Math splits:** TheoQ improved by **12.1 points** over best baseline; TheoT by large margins\n- **Coding splits:** LeetCode at 37.0-38.6 (best), surpassing baselines by **8+ points**\n\n**With GPT-4 CoT reasoning as queries (Table 2):**\n- RaDeR achieves **27.3-29.2 avg** depending on configuration\n- **This is where the BM25 comparison is critical:** BM25 on CoT queries scores 27.0 avg, while BM25 on original questions scores only 14.5. CoT queries actually *help* BM25 significantly due to added terms.\n- RaDeR is stated to be the **first dense retriever that outperforms BM25 when queries are CoT reasoning steps**. In Table 2, RaDeR gte-Qwen2-7B with MATH dataset achieves 29.2 avg vs BM25's 27.0 on CoT queries.\n- Notably, most dense baselines (Qwen*, E5*, etc.) score well below BM25 on CoT queries.\n\n### 6.2 RAR-b / MMTEB (Table 3)\n\nOn the Math and Coding splits of RAR-b:\n- RaDeR gte-Qwen2-7B-instruct: Math **0.852**, Coding **0.835**\n- This is comparable to OpenAI-3-large (Math 0.877, Coding 0.894) and significantly outperforms all open-source models\n- GritLM (previously best open-source): Math 0.824, Coding 0.838\n\n### 6.3 MS MARCO (Table 4)\n\nRaDeR achieves competitive performance (MRR@10 34.4, DL19 71.2, DL20 70.7) compared to RepLLaMA (41.2/74.3/72.1) and SimLM (41.1/71.4/69.7). The point is that reasoning training does **not hurt** standard term-matching retrieval significantly.\n\n### 6.4 Comparison with ReasonIR\n\n- RaDeR achieves a **1.1 point increase in nDCG@10** over ReasonIR, corresponding to a **4.5% relative gain**\n- This is despite using only **43,120 samples** (MATH only) vs ReasonIR's **1,729,368 samples**\n- That ratio is approximately **2.5%** of ReasonIR's training data\n\n### 6.5 Re-ranking Results (Tables 5 and 6)\n\n- RaDeR re-rankers outperform GPT-4 in re-ranking by **+2.5** and **+2.1** nDCG points in the top-100 setting\n- Most significant improvements on LeetCode (+20.3 points) and TheoremQA (+20.4 points)\n- RANK-1 (Weller et al., 2025), trained on 635K MS MARCO examples with test-time compute reasoning, is the strongest baseline at 27.5 avg; RaDeR achieves 25.7-26.7 avg (competitive but not always better)\n\n### 6.6 RAG Performance (Table 7)\n\nOn TheoremQA (BRIGHT), Qwen-2.5-7B-Instruct:\n- No retrieval: 71.0%\n- In-context RAG with RaDeR: 75.0%\n- In-context RAG with RepLLaMA: 72.6%\n- In-context RAG with gold theorems: 77.6%\n- MCTS with OST + RaDeR retrieval: 80.2%\n- MCTS with OST + gold theorems: 81.5%\n\n---\n\n## 7. The Sample Efficiency Claim (2.5% of ReasonIR's Data)\n\n**Exact numbers:**\n- RaDeR trained on MATH only: **43,120 samples**\n- ReasonIR: **1,729,368 samples**\n- Ratio: 43,120 / 1,729,368 = approximately **2.49%**, rounded to **2.5%**\n\n**The comparison is fair in that** both are first-stage reasoning-based retrieval models. RaDeR achieves 1.1 nDCG@10 points higher (4.5% relative improvement) on BRIGHT.\n\n**Why the efficiency:** The authors attribute this to the quality of their synthesized data. The MCTS framework with self-reflection produces training samples where: (a) relevance is verified through answer correctness, (b) hard negatives are naturally generated from the retrieval process, and (c) query diversity comes from different stages of the reasoning tree. ReasonIR, by contrast, generates queries \"without labeled scalar rewards.\"\n\n---\n\n## 8. Limitations (Acknowledged and Apparent)\n\n### Explicitly Acknowledged (Section 8):\n\n1. **Single-document reasoning only:** The training approach focuses on retrieving one relevant document at a time. It cannot handle multi-hop QA tasks where relevance of one document depends on the content of others.\n\n2. **No explanations for retrieval decisions:** RaDeR produces relevance scores but not explanations. Future work could explore generating reasoning explanations while maintaining first-stage efficiency.\n\n3. **Noisy training data from reward signals:** The reward is based on final answer correctness, but an incorrect CoT reasoning path can still lead to a correct final answer, making some training data noisy.\n\n### Apparent/Implicit Limitations:\n\n4. **Dependency on math domain for data generation:** The entire data generation pipeline requires math problems with verifiable answers and a theorem corpus (ProofWiki). Extending to other domains would require analogous structured knowledge bases and verification mechanisms.\n\n5. **MS MARCO performance regression:** Table 4 shows RaDeR underperforms RepLLaMA and SimLM on standard term-matching benchmarks (MRR@10: 34.4 vs 41.2 for RepLLaMA), suggesting some trade-off between reasoning and standard retrieval capabilities.\n\n6. **Failure on certain reasoning types:** Figure 5 shows a failure case where both RaDeR and Qwen2 fail on a family tree / graph theory question about acyclicity, retrieving a theorem about arborescences instead of the gold theorem about girth. Surface-level similarity still misleads the model.\n\n7. **Computational cost of data generation:** MCTS with 16 rollouts, max depth 6, and retrieval at each step is expensive. The paper uses 2 A100 GPUs and processes MATH + NuminaMath datasets.\n\n8. **Limited re-ranker comparison:** The re-ranker does not consistently beat RANK-1 (which uses 635K samples from MS MARCO), and RANK-1 uses test-time compute for reasoning while RaDeR does not.\n\n---\n\n## 9. Reviewer Comments\n\nThe OpenReview page (id=mH2r897uSZ) requires authentication and the reviewer comments are not publicly accessible through web search or unauthenticated access. The paper was accepted at EMNLP 2025 Main Conference (pages 19970-19997), indicating it passed peer review. No specific reviewer scores, strengths/weaknesses lists, or discussion threads could be retrieved.\n\n---\n\n**Key sources consulted:**\n- [arXiv page](https://arxiv.org/abs/2505.18405)\n- [ACL Anthology](https://aclanthology.org/2025.emnlp-main.1011/)\n- [Project website](https://debrup-61.github.io/RaDeR.github.io/)\n- [GitHub repository](https://github.com/debrup-61/rader)\n- [Full PDF](https://arxiv.org/pdf/2505.18405) (26 pages, all read)"
      }
    ],
    "totalDurationMs": 229686,
    "totalTokens": 46450,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1264,
      "cache_read_input_tokens": 40293,
      "output_tokens": 4892,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1264
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4892,
          "cache_read_input_tokens": 40293,
          "cache_creation_input_tokens": 1264,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1264,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 12
    }
  },
  "sourceToolAssistantUUID": "cd9bec28-2868-4757-8abb-b2eed2b46b26",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
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
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "e5a01c22-786e-4c4f-8dd5-78ac1983e559",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on reasoning-aware retrievers",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Tool result

_source line 24 · 2026-05-30T06:32:00.789Z_

<details><summary>↩ Tool result · `toolu_01UfLfspkSa1E6NsgrbEH5oJ`</summary>

```text
Now I have comprehensive information. Let me compile the full report.

---

## ReasonIR: Training Retrievers for Reasoning Tasks -- Detailed Analysis

### 1. The Exact Gap/Problem Identified and How They Identified It

**The gap:** Existing retrievers perform poorly on reasoning-intensive information retrieval tasks. The authors identified this through a **pilot study (Section 3)** examining two specific issues:

**A) Training data mismatch:** Public retrieval training datasets (MS MARCO, Natural Questions, etc.) are dominated by short factual queries -- averaging only ~20 tokens -- paired with documents that straightforwardly answer them. In contrast, reasoning-intensive queries (e.g., on the BRIGHT benchmark) average ~194 tokens and require complex, multi-step reasoning to match queries to relevant documents. Existing retrievers were never trained on data that reflects this reasoning structure.

**B) Query length scaling failure:** Through experiments varying query length (by rewriting queries with LLMs), they discovered that existing retrievers like GRIT-7B and Nomic plateau or degrade at ~256 tokens. Even Nomic, which was trained to handle 10K+ token contexts, showed no benefit from longer queries -- because its training data still consisted of short factual pairs. This demonstrated that raw context-window length is insufficient; the model must be *trained* on long, reasoning-intensive query-document pairs to benefit from them.

### 2. Their Key Insight That Others Missed

The central insight is twofold:

**First**, the bottleneck for reasoning-intensive retrieval is not model architecture or context length -- it is the *training data*. Prior work focused on architectural improvements (better encoders, cross-encoders, rerankers) but neglected that training data fundamentally shapes what a retriever can learn to match. If training data only contains "What is the capital of France?" -> "Paris is the capital of France" pairs, the retriever learns lexical/semantic overlap matching, not reasoning-based matching.

**Second**, query length can serve as a new axis for test-time compute scaling in retrieval. By rewriting short queries into longer, reasoning-rich queries (using an LLM), a retriever trained on varied-length data can continuously improve -- unlike standard retrievers that plateau. This is analogous to how chain-of-thought improves LLM reasoning: more "thinking" in the query leads to better retrieval, but only if the retriever was trained to handle such inputs.

### 3. How They Formulated the Problem Differently from Prior Work

Prior work treated retrieval training as learning query-document similarity from factual question-answer pairs, with improvements coming from better negative mining (BM25 hard negatives), better architectures, or more data of the same kind.

ReasonIR reframes the problem as: **the retrieval training data itself must embody reasoning**. Specifically:
- Queries should require higher-order thinking (analysis, evaluation, synthesis) rather than simple fact recall
- Positive documents should be ones that are *helpful for reasoning* about a problem, not just ones that directly answer it
- Hard negatives should be documents that are *superficially relevant* (share topic/terminology) but *actually unhelpful* for reasoning -- a fundamentally different notion than standard hard negatives

This reframing shifts from "find documents that contain the answer" to "find documents that help reason toward a solution."

### 4. Existing Techniques They Adapted/Combined/Simplified

- **Contrastive learning with InfoNCE loss** -- standard in retrieval training, not novel
- **Bi-directional attention on a causal LLM backbone** (Llama 3.1-8B with attention mask changed from causal to bidirectional) -- adapted from GritLM and similar work
- **Synthetic data generation using LLMs** -- adapted from prior work on synthetic retrieval data, but with novel prompting strategies specific to reasoning
- **Hard negative mining** -- adapted from existing practice but replaced BM25-based mining with LLM-based multi-turn generation (because existing retrievers perform too poorly on reasoning tasks to mine reliable hard negatives)
- **GradCache and cross-device negatives** -- standard training efficiency techniques
- **Hybrid retrieval with BM25** -- standard technique, but they showed it is particularly effective here because BM25 and dense retrieval have only 28.2% overlap in top-100 documents on reasoning tasks
- **Reranker score interpolation** -- simple but effective: instead of complex reasoning-based rerankers (like Rank1), they interpolate a standard reranker's relevance score with the base retriever score to break ties, achieving comparable performance at 200x less compute

### 5. Core Technical Method in Detail

#### 5A. Data Generation Pipeline (REASONIR-SYNTHESIZER)

The pipeline uses Llama 3.1-70B-Instruct and produces two types of synthetic data:

**Varied-Length (VL) Data (244,970 samples):**
- Purpose: Train the retriever to handle queries of 300-2,000 words (vs. the 20-token average in standard data)
- Process: (1) Generate instruction templates from reasoning tasks (e.g., "Given a document supporting a debatable argument, find another with opposing arguments"); (2) Generate long queries and positive documents from these templates; (3) Generate hard negatives using multi-turn prompting
- This extends the retriever's effective context length for reasoning queries

**Hard Query (HQ) Data (100,521 samples):**
- Purpose: Create reasoning-intensive query-document pairs
- Seed document selection: Use documents from the BRIGHT corpus, filtered by FineWeb-Edu classifier (score >= 2) to ensure educational quality, removing gibberish/subjective content
- Query generation: A "human-like brainstorming" prompt instructs the LLM to generate queries that:
  - Present complete, self-contained scenarios
  - Are answerable through logical reasoning
  - Target higher-order thinking (analysis, evaluation, synthesis)
  - Incorporate domain-specific terminology
  - Must NOT directly reference the source document, be answerable through simple fact recall, or be reading comprehension questions
- Domain alignment: 3-step process -- (1) identify primary domain, (2) extract key concepts/principles, (3) list common problem-solving patterns

**Multi-Turn Hard Negative Generation (for both VL and HQ):**
- Standard BM25-based hard negative mining fails because existing retrievers perform poorly on reasoning queries, and there is high risk of mining false negatives
- Their approach: In turn 1, generate query + positive document; in turn 2, generate a hard negative *conditioned on both*, ensuring the negative is superficially relevant but genuinely unhelpful
- Hard negatives must: contain superficial overlap, NOT be helpful for the query, be less relevant than the positive, be long (>=300 words), and avoid substantial word overlap with the positive

#### 5B. Training Procedure

- **Base model:** Llama 3.1-8B with causal attention mask changed to bidirectional
- **Training data:** 1,383,877 public samples + 244,970 VL + 100,521 HQ = ~1.73M total
- **Loss:** Standard InfoNCE contrastive loss with temperature tau=0.02, using cosine similarity between query and document embeddings
- **Negatives:** In-batch negatives + hard negatives from the synthetic pipeline
- **Hyperparameters:** Batch size 2,048; 1,000 training steps; learning rate 2e-5; warmup ratio 0.06
- **Techniques:** GradCache (for memory efficiency with large batch), cross-device negatives

#### 5C. Model Architecture

The model is a standard bi-encoder. It encodes queries and documents independently into dense embeddings, then computes cosine similarity for ranking. No cross-attention or interaction between query and document at inference time. This makes it highly efficient compared to cross-encoder rerankers.

#### 5D. REASONIR-Rerank

A simple reranking approach that interpolates scores:
- `score = 0.5 * S_reranker + 0.5 * S_retriever` (using QwenRerank + ReasonIR scores)
- This breaks ties that naive LLM rerankers produce
- Training-free; no reasoning token generation
- Achieves comparable or better performance than Rank1 (a reasoning-based reranker) at 200x less compute

### 6. Main Results on BRIGHT Benchmark

| Configuration | nDCG@10 |
|---|---|
| ReasonIR-8B (original query) | **24.4** |
| ReasonIR-8B (GPT-4 REASON-QUERY rewrite) | **29.9** |
| ReasonIR-8B + BM25 hybrid | **32.0** |
| ReasonIR-8B + QwenRerank + Retriever interpolation | **36.9** |

Comparisons with baselines (original query):
- GRIT-7B: 20.9
- Rank1: 21.0
- ReasonIR-8B: 24.4 (outperforms all)

Subject-wise performance (original / GPT-4 rewrite):
- Biology: 26.2 / 43.6
- Economics: 23.3 / 32.7
- Psychology: 30.0 / 38.8
- Robotics: 18.0 / 20.9
- Coding (LeetCode): 10.5 / 19.6
- Theorem-based: 27.2 / 35.7

Ablation on data composition (nDCG@10 with original query / GPT-4 rewrite):
- Public only: 19.6 / 27.1
- Public + HQ: 20.9 / 27.1
- Public + VL: 23.2 / 28.0
- Public + HQ + VL: **24.4 / 29.9** (synergistic -- gains are super-additive)

RAG downstream results:
- MMLU: 75.6% (vs. 71.1% closed-book baseline, +6.4% relative improvement)
- GPQA: 38.4% (vs. 31.3% closed-book baseline, +22.6% relative improvement)

### 7. Limitations (Acknowledged or Apparent)

**Acknowledged limitations:**
1. **Query rewriting can hurt on some tasks:** On GPQA, query rewriting with a small reader model actually decreased performance (from 38.4% to 35.4%). Hypothesis: smaller models write poor reasoning queries.
2. **Distribution shift in reranking:** Rank1-7B performs better with BM25 candidates than with ReasonIR/GRIT candidates, suggesting rerankers trained on one retriever's output distribution degrade when applied to another's.
3. **English only:** No multilingual or multimodal evaluation.
4. **Scaling laws unexplored:** Optimal ratio of VL to HQ to public data is not determined; the specific composition lacks principled justification.

**Apparent limitations (from reviewer analysis):**
5. **Domain dependence of seed documents:** HQ data uses BRIGHT corpus documents as seeds. Heavy reliance on BRIGHT-aligned seed documents makes generalization to entirely different domains uncertain.
6. **Requires large LLMs for data generation:** Llama 3.1-8B produces significantly lower-quality hard queries than 70B (BM25 error rate of 21.0 vs. 53.0), making the approach expensive to scale.
7. **Coding and theorem proving remain weak:** Even with GPT-4 rewriting, coding (19.6 nDCG@10) and robotics (20.9) performance is relatively low, suggesting fundamental difficulty in these domains.
8. **Potential knowledge leakage concern:** Although authors argued against it by showing easy-query data from the same documents doesn't help, the use of BRIGHT corpus documents as seeds for synthetic training data raised reviewer concern.

### 8. OpenReview Reviewer Comments (COLM 2025)

**Decision: ACCEPTED**

**Reviewer EF6c (Rating: 8/10, Confidence: 4/5):**
- Strengths: Excels at reasoning-intensive tasks through carefully generated synthetic data; best performance under different test-time compute scenarios; ablations validate importance of each component
- Weaknesses: Lacks training scaling law analysis; unclear optimal ratios between data types
- Questions: Would ReasonIR hurt on simpler retrieval tasks (MS-MARCO, NQ)?

**Reviewer MLfg (Rating: 6/10, Confidence: 4/5):**
- Strengths: Spearheads LLM-based representation learning for reasoning-intensive retrieval
- Weaknesses: Performance relies on in-domain high-quality synthetic data; out-of-distribution generalization not examined
- Questions: Knowledge leakage from BRIGHT corpus? Why does performance degrade on Coding/Theorem with GPT-4 rewriting?

**Reviewer P7d1 (Rating: 7/10, Confidence: 3/5):**
- Strengths: Good motivation experiments in Section 3; interesting hard negative generation idea; thorough appendix
- Weaknesses: Presentation clarity issues (missing examples, undefined baselines/terms); lacks analysis on why sparse retriever combination helps

**Reviewer 4Dkf (Rating: 7/10, Confidence: 4/5):**
- Strengths: Directly addresses training data limitation; clear gains; potential impact for RAG in limited-data domains
- Weaknesses: Impact of synthetic data quality unclear without manual verification; no dataset size impact measurement

**Meta-review:** Acknowledged reviewers' concerns about scaling, OOD generalization, and data quality. Authors provided satisfactory preliminary scaling studies (50% data reduction: 24.4 -> 20.8 nDCG), noise injection experiments (10% noise: 24.4 -> 24.0), and OOD evaluation on RAG tasks. The work was deemed to establish "a solid foundation for future research in reasoning intensive retrieval and RAG."

**Key author rebuttals:**
- Noise injection: 10% corrupted data caused minimal degradation (24.4 -> 24.0)
- Scaling: 50% data subsampling dropped from 24.4 to 20.8, confirming data volume matters
- Knowledge leakage ruled out: Easy-query (EQ) data from the same documents showed no improvement
- Small LLM data generation: Llama-8B produces much lower quality than 70B
- Qualitative failure analysis: Rare specialized terms (e.g., "kinetic synesthesia") where BM25 keyword matching outperforms dense retrieval

Sources:
- [ReasonIR on arXiv](https://arxiv.org/abs/2504.20595)
- [ReasonIR on OpenReview (COLM 2025)](https://openreview.net/forum?id=kkBCNLMbGj)
- [ReasonIR on Hugging Face](https://huggingface.co/papers/2504.20595)
- [ReasonIR GitHub Repository](https://github.com/facebookresearch/ReasonIR)

agentId: aa0c5101724298ec8 (use SendMessage with to: 'aa0c5101724298ec8' to continue this agent)
&lt;usage>total_tokens: 25019
tool_uses: 16
duration_ms: 241514&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57a05ed6-2706-4197-83de-a8c69adc95c9",
  "isSidechain": false,
  "promptId": "509b9e27-9338-43ac-a97b-3de5e1bfe6b5",
  "type": "user",
  "uuid": "9a708401-cbd6-4ebc-8703-974484d9b22c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"ReasonIR: Training Retrievers for Reasoning Tasks\" by Rulin Shao et al. (arXiv 2025, https://arxiv.org/abs/2504.20595).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also try to find if it has an OpenReview page with reviewer comments.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined/simplified\n5. Their core technical method in detail (data generation pipeline, training procedure, model architecture)\n6. Their main results on BRIGHT benchmark specifically\n7. Limitations acknowledged or apparent\n8. Any reviewer comments if available on OpenReview\n\nPlease be thorough and precise. Report all findings in detail.",
    "agentId": "aa0c5101724298ec8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the full report.\n\n---\n\n## ReasonIR: Training Retrievers for Reasoning Tasks -- Detailed Analysis\n\n### 1. The Exact Gap/Problem Identified and How They Identified It\n\n**The gap:** Existing retrievers perform poorly on reasoning-intensive information retrieval tasks. The authors identified this through a **pilot study (Section 3)** examining two specific issues:\n\n**A) Training data mismatch:** Public retrieval training datasets (MS MARCO, Natural Questions, etc.) are dominated by short factual queries -- averaging only ~20 tokens -- paired with documents that straightforwardly answer them. In contrast, reasoning-intensive queries (e.g., on the BRIGHT benchmark) average ~194 tokens and require complex, multi-step reasoning to match queries to relevant documents. Existing retrievers were never trained on data that reflects this reasoning structure.\n\n**B) Query length scaling failure:** Through experiments varying query length (by rewriting queries with LLMs), they discovered that existing retrievers like GRIT-7B and Nomic plateau or degrade at ~256 tokens. Even Nomic, which was trained to handle 10K+ token contexts, showed no benefit from longer queries -- because its training data still consisted of short factual pairs. This demonstrated that raw context-window length is insufficient; the model must be *trained* on long, reasoning-intensive query-document pairs to benefit from them.\n\n### 2. Their Key Insight That Others Missed\n\nThe central insight is twofold:\n\n**First**, the bottleneck for reasoning-intensive retrieval is not model architecture or context length -- it is the *training data*. Prior work focused on architectural improvements (better encoders, cross-encoders, rerankers) but neglected that training data fundamentally shapes what a retriever can learn to match. If training data only contains \"What is the capital of France?\" -> \"Paris is the capital of France\" pairs, the retriever learns lexical/semantic overlap matching, not reasoning-based matching.\n\n**Second**, query length can serve as a new axis for test-time compute scaling in retrieval. By rewriting short queries into longer, reasoning-rich queries (using an LLM), a retriever trained on varied-length data can continuously improve -- unlike standard retrievers that plateau. This is analogous to how chain-of-thought improves LLM reasoning: more \"thinking\" in the query leads to better retrieval, but only if the retriever was trained to handle such inputs.\n\n### 3. How They Formulated the Problem Differently from Prior Work\n\nPrior work treated retrieval training as learning query-document similarity from factual question-answer pairs, with improvements coming from better negative mining (BM25 hard negatives), better architectures, or more data of the same kind.\n\nReasonIR reframes the problem as: **the retrieval training data itself must embody reasoning**. Specifically:\n- Queries should require higher-order thinking (analysis, evaluation, synthesis) rather than simple fact recall\n- Positive documents should be ones that are *helpful for reasoning* about a problem, not just ones that directly answer it\n- Hard negatives should be documents that are *superficially relevant* (share topic/terminology) but *actually unhelpful* for reasoning -- a fundamentally different notion than standard hard negatives\n\nThis reframing shifts from \"find documents that contain the answer\" to \"find documents that help reason toward a solution.\"\n\n### 4. Existing Techniques They Adapted/Combined/Simplified\n\n- **Contrastive learning with InfoNCE loss** -- standard in retrieval training, not novel\n- **Bi-directional attention on a causal LLM backbone** (Llama 3.1-8B with attention mask changed from causal to bidirectional) -- adapted from GritLM and similar work\n- **Synthetic data generation using LLMs** -- adapted from prior work on synthetic retrieval data, but with novel prompting strategies specific to reasoning\n- **Hard negative mining** -- adapted from existing practice but replaced BM25-based mining with LLM-based multi-turn generation (because existing retrievers perform too poorly on reasoning tasks to mine reliable hard negatives)\n- **GradCache and cross-device negatives** -- standard training efficiency techniques\n- **Hybrid retrieval with BM25** -- standard technique, but they showed it is particularly effective here because BM25 and dense retrieval have only 28.2% overlap in top-100 documents on reasoning tasks\n- **Reranker score interpolation** -- simple but effective: instead of complex reasoning-based rerankers (like Rank1), they interpolate a standard reranker's relevance score with the base retriever score to break ties, achieving comparable performance at 200x less compute\n\n### 5. Core Technical Method in Detail\n\n#### 5A. Data Generation Pipeline (REASONIR-SYNTHESIZER)\n\nThe pipeline uses Llama 3.1-70B-Instruct and produces two types of synthetic data:\n\n**Varied-Length (VL) Data (244,970 samples):**\n- Purpose: Train the retriever to handle queries of 300-2,000 words (vs. the 20-token average in standard data)\n- Process: (1) Generate instruction templates from reasoning tasks (e.g., \"Given a document supporting a debatable argument, find another with opposing arguments\"); (2) Generate long queries and positive documents from these templates; (3) Generate hard negatives using multi-turn prompting\n- This extends the retriever's effective context length for reasoning queries\n\n**Hard Query (HQ) Data (100,521 samples):**\n- Purpose: Create reasoning-intensive query-document pairs\n- Seed document selection: Use documents from the BRIGHT corpus, filtered by FineWeb-Edu classifier (score >= 2) to ensure educational quality, removing gibberish/subjective content\n- Query generation: A \"human-like brainstorming\" prompt instructs the LLM to generate queries that:\n  - Present complete, self-contained scenarios\n  - Are answerable through logical reasoning\n  - Target higher-order thinking (analysis, evaluation, synthesis)\n  - Incorporate domain-specific terminology\n  - Must NOT directly reference the source document, be answerable through simple fact recall, or be reading comprehension questions\n- Domain alignment: 3-step process -- (1) identify primary domain, (2) extract key concepts/principles, (3) list common problem-solving patterns\n\n**Multi-Turn Hard Negative Generation (for both VL and HQ):**\n- Standard BM25-based hard negative mining fails because existing retrievers perform poorly on reasoning queries, and there is high risk of mining false negatives\n- Their approach: In turn 1, generate query + positive document; in turn 2, generate a hard negative *conditioned on both*, ensuring the negative is superficially relevant but genuinely unhelpful\n- Hard negatives must: contain superficial overlap, NOT be helpful for the query, be less relevant than the positive, be long (>=300 words), and avoid substantial word overlap with the positive\n\n#### 5B. Training Procedure\n\n- **Base model:** Llama 3.1-8B with causal attention mask changed to bidirectional\n- **Training data:** 1,383,877 public samples + 244,970 VL + 100,521 HQ = ~1.73M total\n- **Loss:** Standard InfoNCE contrastive loss with temperature tau=0.02, using cosine similarity between query and document embeddings\n- **Negatives:** In-batch negatives + hard negatives from the synthetic pipeline\n- **Hyperparameters:** Batch size 2,048; 1,000 training steps; learning rate 2e-5; warmup ratio 0.06\n- **Techniques:** GradCache (for memory efficiency with large batch), cross-device negatives\n\n#### 5C. Model Architecture\n\nThe model is a standard bi-encoder. It encodes queries and documents independently into dense embeddings, then computes cosine similarity for ranking. No cross-attention or interaction between query and document at inference time. This makes it highly efficient compared to cross-encoder rerankers.\n\n#### 5D. REASONIR-Rerank\n\nA simple reranking approach that interpolates scores:\n- `score = 0.5 * S_reranker + 0.5 * S_retriever` (using QwenRerank + ReasonIR scores)\n- This breaks ties that naive LLM rerankers produce\n- Training-free; no reasoning token generation\n- Achieves comparable or better performance than Rank1 (a reasoning-based reranker) at 200x less compute\n\n### 6. Main Results on BRIGHT Benchmark\n\n| Configuration | nDCG@10 |\n|---|---|\n| ReasonIR-8B (original query) | **24.4** |\n| ReasonIR-8B (GPT-4 REASON-QUERY rewrite) | **29.9** |\n| ReasonIR-8B + BM25 hybrid | **32.0** |\n| ReasonIR-8B + QwenRerank + Retriever interpolation | **36.9** |\n\nComparisons with baselines (original query):\n- GRIT-7B: 20.9\n- Rank1: 21.0\n- ReasonIR-8B: 24.4 (outperforms all)\n\nSubject-wise performance (original / GPT-4 rewrite):\n- Biology: 26.2 / 43.6\n- Economics: 23.3 / 32.7\n- Psychology: 30.0 / 38.8\n- Robotics: 18.0 / 20.9\n- Coding (LeetCode): 10.5 / 19.6\n- Theorem-based: 27.2 / 35.7\n\nAblation on data composition (nDCG@10 with original query / GPT-4 rewrite):\n- Public only: 19.6 / 27.1\n- Public + HQ: 20.9 / 27.1\n- Public + VL: 23.2 / 28.0\n- Public + HQ + VL: **24.4 / 29.9** (synergistic -- gains are super-additive)\n\nRAG downstream results:\n- MMLU: 75.6% (vs. 71.1% closed-book baseline, +6.4% relative improvement)\n- GPQA: 38.4% (vs. 31.3% closed-book baseline, +22.6% relative improvement)\n\n### 7. Limitations (Acknowledged or Apparent)\n\n**Acknowledged limitations:**\n1. **Query rewriting can hurt on some tasks:** On GPQA, query rewriting with a small reader model actually decreased performance (from 38.4% to 35.4%). Hypothesis: smaller models write poor reasoning queries.\n2. **Distribution shift in reranking:** Rank1-7B performs better with BM25 candidates than with ReasonIR/GRIT candidates, suggesting rerankers trained on one retriever's output distribution degrade when applied to another's.\n3. **English only:** No multilingual or multimodal evaluation.\n4. **Scaling laws unexplored:** Optimal ratio of VL to HQ to public data is not determined; the specific composition lacks principled justification.\n\n**Apparent limitations (from reviewer analysis):**\n5. **Domain dependence of seed documents:** HQ data uses BRIGHT corpus documents as seeds. Heavy reliance on BRIGHT-aligned seed documents makes generalization to entirely different domains uncertain.\n6. **Requires large LLMs for data generation:** Llama 3.1-8B produces significantly lower-quality hard queries than 70B (BM25 error rate of 21.0 vs. 53.0), making the approach expensive to scale.\n7. **Coding and theorem proving remain weak:** Even with GPT-4 rewriting, coding (19.6 nDCG@10) and robotics (20.9) performance is relatively low, suggesting fundamental difficulty in these domains.\n8. **Potential knowledge leakage concern:** Although authors argued against it by showing easy-query data from the same documents doesn't help, the use of BRIGHT corpus documents as seeds for synthetic training data raised reviewer concern.\n\n### 8. OpenReview Reviewer Comments (COLM 2025)\n\n**Decision: ACCEPTED**\n\n**Reviewer EF6c (Rating: 8/10, Confidence: 4/5):**\n- Strengths: Excels at reasoning-intensive tasks through carefully generated synthetic data; best performance under different test-time compute scenarios; ablations validate importance of each component\n- Weaknesses: Lacks training scaling law analysis; unclear optimal ratios between data types\n- Questions: Would ReasonIR hurt on simpler retrieval tasks (MS-MARCO, NQ)?\n\n**Reviewer MLfg (Rating: 6/10, Confidence: 4/5):**\n- Strengths: Spearheads LLM-based representation learning for reasoning-intensive retrieval\n- Weaknesses: Performance relies on in-domain high-quality synthetic data; out-of-distribution generalization not examined\n- Questions: Knowledge leakage from BRIGHT corpus? Why does performance degrade on Coding/Theorem with GPT-4 rewriting?\n\n**Reviewer P7d1 (Rating: 7/10, Confidence: 3/5):**\n- Strengths: Good motivation experiments in Section 3; interesting hard negative generation idea; thorough appendix\n- Weaknesses: Presentation clarity issues (missing examples, undefined baselines/terms); lacks analysis on why sparse retriever combination helps\n\n**Reviewer 4Dkf (Rating: 7/10, Confidence: 4/5):**\n- Strengths: Directly addresses training data limitation; clear gains; potential impact for RAG in limited-data domains\n- Weaknesses: Impact of synthetic data quality unclear without manual verification; no dataset size impact measurement\n\n**Meta-review:** Acknowledged reviewers' concerns about scaling, OOD generalization, and data quality. Authors provided satisfactory preliminary scaling studies (50% data reduction: 24.4 -> 20.8 nDCG), noise injection experiments (10% noise: 24.4 -> 24.0), and OOD evaluation on RAG tasks. The work was deemed to establish \"a solid foundation for future research in reasoning intensive retrieval and RAG.\"\n\n**Key author rebuttals:**\n- Noise injection: 10% corrupted data caused minimal degradation (24.4 -> 24.0)\n- Scaling: 50% data subsampling dropped from 24.4 to 20.8, confirming data volume matters\n- Knowledge leakage ruled out: Easy-query (EQ) data from the same documents showed no improvement\n- Small LLM data generation: Llama-8B produces much lower quality than 70B\n- Qualitative failure analysis: Rare specialized terms (e.g., \"kinetic synesthesia\") where BM25 keyword matching outperforms dense retrieval\n\nSources:\n- [ReasonIR on arXiv](https://arxiv.org/abs/2504.20595)\n- [ReasonIR on OpenReview (COLM 2025)](https://openreview.net/forum?id=kkBCNLMbGj)\n- [ReasonIR on Hugging Face](https://huggingface.co/papers/2504.20595)\n- [ReasonIR GitHub Repository](https://github.com/facebookresearch/ReasonIR)"
      }
    ],
    "totalDurationMs": 241514,
    "totalTokens": 25019,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1638,
      "cache_read_input_tokens": 19774,
      "output_tokens": 3606,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1638
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3606,
          "cache_read_input_tokens": 19774,
          "cache_creation_input_tokens": 1638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1638,
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
  "sourceToolAssistantUUID": "57a05ed6-2706-4197-83de-a8c69adc95c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-30T06:32:22.524Z_

<details><summary>↩ Tool result · `toolu_01DAf6w3i6p9zis7mDvzoMGA`</summary>

````text
I now have comprehensive information from both the paper and the reviews. Let me compile the complete analysis.

---

## Comprehensive Analysis of Self-RAG (Asai et al., ICLR 2024 Oral)

### 1. EXACT GAP/PROBLEM IDENTIFIED

The authors identified a fundamental tension in retrieval-augmented generation. Their diagnosis has two layers:

**Problem with vanilla LLMs:** Large language models "often struggle with factual errors" because they rely solely on parametric knowledge encoded during pre-training. Scaling alone does not resolve this.

**Problem with existing RAG approaches:** Prior RAG methods (Lewis et al., Guu et al.) introduced a *different* set of problems while trying to fix the first:
- They "retrieve passages indiscriminately regardless of whether the factual grounding is helpful" -- retrieval happens for every query with a fixed number of passages, even when the model already knows the answer or when no retrieved passage is relevant.
- The generated "output is not guaranteed to be consistent with retrieved relevant passages" -- even when relevant passages are retrieved, there is no mechanism ensuring the model actually uses them faithfully.
- RAG improvements come "at the expense of runtime efficiency, robustness to irrelevant context, and lack of attributions."

**How they identified this:** The authors observed empirically that indiscriminate retrieval can *hurt* performance. For example, ChatGPT with retrieval augmentation actually performs *worse* than ChatGPT alone on several tasks (Table 2), because irrelevant passages confuse the model. They cite concurrent work by Mallen et al. (2023) documenting this phenomenon. They also noted the absence of any mechanism for LLMs to self-assess whether their own generations are factually grounded in evidence.

---

### 2. KEY INSIGHT THAT OTHERS MISSED

The central insight is that retrieval decisions and output quality assessment should be made *by the LM itself* as part of generation, not by external components. Specifically:

1. **Retrieval should be adaptive and on-demand**, triggered by the model's own assessment of whether it needs external knowledge for the current generation step -- not applied uniformly to every input.

2. **Self-critique should happen inline**, with the model evaluating its own outputs for relevance, factual support, and utility using special tokens that are part of the generation vocabulary.

3. **These capabilities can be distilled into a single model** through offline training data augmentation (using a critic trained on GPT-4 labels), rather than requiring expensive online reinforcement learning (RLHF/PPO) or a separate runtime critic model.

The combination is what others missed: prior work either (a) always retrieved, (b) used external filtering/critic models at runtime adding latency, or (c) used RL-based training which is expensive and unstable. Self-RAG showed you could get all three benefits (adaptive retrieval + self-critique + controllability) through a training-time data augmentation approach with special tokens.

---

### 3. PROBLEM FORMULATION DIFFERENCES FROM PRIOR WORK

**Traditional RAG formulation:** Given input x, retrieve documents D, generate y = M(x, D). Retrieval is a fixed preprocessing step.

**Self-RAG reformulation:** Generate segmented output y = [y_1, ..., y_T] where each segment y_t can trigger:
- A **Retrieve** token deciding whether to fetch passages
- **Critique** tokens evaluating the passage and generation quality
- The actual text continuation

The model's vocabulary V is expanded to include reflection tokens as first-class tokens. The generation objective becomes:

```
max_M E log p_M(y, r | x)
```

where r represents reflection tokens interleaved with the output y. This is critically different from prior work because:
- Reflection tokens and text tokens are predicted using the *same* next-token prediction objective -- no separate critic head or reward model needed at inference time
- Retrieved passages are **masked during loss computation** -- the model never learns to memorize or reconstruct evidence, only to use it and evaluate it
- The framework enables **segment-level beam search** at inference, where different retrieved passages produce competing continuations that are ranked by critique token scores

---

### 4. EXISTING TECHNIQUES ADAPTED/COMBINED

Self-RAG is a synthesis of several existing ideas, recombined in a novel way:

**(a) Reflection/Critique Tokens:** Inspired by control tokens in conditional text generation (e.g., Keskar et al.'s CTRL, Lu et al.'s Quark), but repurposed. Unlike control tokens that condition generation on desired attributes, Self-RAG's reflection tokens are generated *after* output segments for self-evaluation. They serve as both training signals and inference-time quality indicators.

**(b) Critic Model / Knowledge Distillation from GPT-4:** The critic model C is trained via distillation from GPT-4 judgments. For each reflection token type, 4k-20k examples are labeled by GPT-4 using type-specific prompts with few-shot demonstrations. This critic achieves >90% agreement with GPT-4. The approach adapts the "LLM-as-judge" paradigm (used in RLHF data collection) but applies it to generate structured token-level annotations rather than scalar rewards.

**(c) Adaptive/Active Retrieval:** The idea of deciding when to retrieve draws from FLARE (Jiang et al., 2023) and similar active retrieval methods. However, Self-RAG integrates this decision into the model itself rather than using heuristics (like low-confidence token detection in FLARE).

**(d) Off-the-shelf Dense Retrieval:** Uses Contriever-MS MARCO without modification as the retrieval backbone, showing the framework is retriever-agnostic.

**(e) Segment-Level Beam Search:** Adapts standard beam search from token-level to segment-level, processing multiple retrieved passages in parallel and ranking them by a composite score of generation probability and critique token scores.

---

### 5. CORE TECHNICAL METHOD IN DETAIL

#### Reflection Token Types (Table 1 in the paper):

| Token | Input | Values | Purpose |
|-------|-------|--------|---------|
| **Retrieve** | x or (x, y_{&lt;t}) | {yes, no, continue} | Should the model retrieve at this step? |
| **IsRel** | (x, passage d) | {relevant, irrelevant} | Is the retrieved passage useful? |
| **IsSup** | (x, d, y_t) | {fully supported, partially supported, no support} | Is the generated segment grounded in evidence? |
| **IsUse** | (x, y) | {5, 4, 3, 2, 1} | Overall utility of the complete response |

#### Training Procedure -- Two Stages:

**Stage 1: Critic Model Training (C)**
- Base model: Llama 2-7B
- For each of the 4 reflection token types, sample instances from training data
- Prompt GPT-4 with type-specific instructions + few-shot examples to label each instance
  - Example for Retrieve: "Given an instruction, make a judgment on whether finding some external documents from the web helps to generate a better response"
- Collect 4k-20k labeled examples per token type
- Train C via standard conditional language modeling: `max_C E log p_C(r | x, y)`
- Validation: >90% agreement with GPT-4 on most token categories

**Stage 2: Generator Model Training (M)**
- Base models: Llama 2-7B and Llama 2-13B
- Data augmentation process for each training example (x, y):
  1. For each segment y_t: run critic C to predict Retrieve token
  2. If Retrieve=Yes: use retriever R to fetch top-K passages
  3. For each passage d: critic evaluates IsRel(x, d)
  4. If relevant: generate segment, then critic evaluates IsSup(x, d, y_t)
  5. At end of full output: critic evaluates IsUse(x, y)
  6. Insert all reflection tokens inline into the training sequence
- Generator training: standard next-token prediction on augmented data
  - `max_M E log p_M(y, r | x)`
  - **Retrieved passages are masked** in loss computation -- the model does NOT learn to reproduce evidence
- Training data: 150k instruction-output pairs from Open-Instruct + knowledge-intensive datasets
- Vocabulary expanded with special reflection tokens

#### Inference Algorithm:

**Step 1 -- Retrieval Decision:**
- At each segment boundary, model predicts Retrieve token
- If P(Retrieve=Yes) > threshold (default 0.2; set to 0 for tasks like ASQA that always need retrieval): trigger retrieval
- "continue" means keep generating without new retrieval

**Step 2 -- Parallel Generation:**
- Retrieve top K=5 passages via Contriever-MS MARCO
- Generate K candidate segments y_t, one conditioned on each passage, in parallel

**Step 3 -- Scoring:**
Each candidate is scored by:
```
f(y_t, d, Critique) = p(y_t | x, d, y_{&lt;t}) + S(Critique)
```
where:
```
S(Critique) = sum over G in {IsRel, IsSup, IsUse} of: w^G * s_t^G
```
- s_t^G = normalized probability of the most desirable token value for group G (e.g., P(IsRel=relevant) normalized)
- w^G = user-adjustable weights (defaults: IsRel=1.0, IsSup=1.0, IsUse=0.5)

**Step 4 -- Selection:**
- Segment-level beam search with beam width = 2
- Token-level decoding within segments is greedy
- Best complete sequence returned

**Inference-Time Controllability:**
- **Soft control:** Adjust w^G weights to prioritize different aspects (e.g., increase w^IsSup for citation-heavy tasks)
- **Hard control:** Filter out segments producing undesirable tokens (e.g., reject any segment with IsSup=NoSupport)
- This is a key advantage: behavior can be customized per-task *without retraining*

---

### 6. MAIN RESULTS ACROSS TASKS

#### Short-Form QA:
- **PopQA** (long-tail entities): Self-RAG 13B achieves 55.8% accuracy, vs. ChatGPT 29.3%, Ret-ChatGPT 50.8%, Llama2-FT 48.7%
- **TriviaQA**: Self-RAG 13B achieves 69.3%, vs. ChatGPT 74.3% (one of the few tasks where ChatGPT is stronger)

#### Reasoning & Fact Verification:
- **PubHealth** (fact verification): Self-RAG 13B achieves 74.5%, vs. ChatGPT 70.1%, Ret-ChatGPT 54.7%
- **ARC-Challenge** (science reasoning): Self-RAG 13B achieves 73.1%, vs. ChatGPT 75.3%, Ret-ChatGPT 75.3%

#### Long-Form Generation:
- **Biography Generation (FactScore):** Self-RAG 7B achieves 81.2 (best overall), vs. ChatGPT 71.8, Ret-ChatGPT 71.2, Perplexity.ai 71.4
- **ASQA (long-form QA):**
  - Str-EM: Self-RAG 13B achieves 31.7, vs. ChatGPT 35.3, Ret-ChatGPT 40.7
  - Citation Precision: Self-RAG 13B achieves 70.3%, vs. Ret-ChatGPT 65.1%
  - Citation Recall: Self-RAG 13B achieves 71.3%, vs. Ret-ChatGPT 76.6%

#### Key Comparative Findings:
- Self-RAG 7B/13B outperforms all non-proprietary models across all six tasks
- Outperforms ChatGPT on 4 of 6 tasks, and nearly matches on the other 2
- **Llama2-FT** (same training data, no reflection tokens) consistently underperforms Self-RAG, proving gains come from the framework itself, not just the training data
- Self-RAG adaptively retrieves 30-50% of the time depending on the task, improving efficiency over always-retrieve approaches

#### Ablation Highlights:
- Removing the critic C causes the largest drops: PopQA 45.5 -> 42.6, ASQA 32.1 -> 18.1
- No retrieval at test time: PopQA drops from 45.5 to 24.7
- Hard constraints only (vs. soft weighting): PopQA drops to 28.3
- Using only top-1 passage: PopQA drops from 45.5 to 41.8
- Scaling training data from 50k to 150k yields "notable improvements"

---

### 7. LIMITATIONS (ACKNOWLEDGED AND APPARENT)

**Acknowledged by the authors:**
1. **Computational overhead:** Segment-level beam search with multiple passages requires more compute than standard greedy decoding, though they implement optimizations (parallel batch decoding, paged attention)
2. **Retriever dependency:** Uses off-the-shelf Contriever-MS MARCO; performance is bounded by retriever quality
3. **GPT-4 dependency for critic training:** Initial data collection requires proprietary GPT-4 API (though this is a one-time cost, distilled into the local critic)
4. **Segment granularity:** Framework operates at sentence-level segments; adapting to other granularities requires modification

**Apparent but not deeply discussed:**
5. **Does not outperform ChatGPT on all tasks:** TriviaQA and ARC-Challenge show Self-RAG 13B still below ChatGPT, suggesting the method works best for knowledge-intensive tasks where retrieval provides the most value
6. **No cross-passage synthesis:** The model evaluates and selects passages independently; it cannot synthesize information spanning multiple passages (noted by Reviewer 4MCy)
7. **Potential data leakage concerns:** Some retrieval baselines perform worse than expected, which Reviewer quEF flagged as potentially suspicious
8. **Impact on non-factuality tasks unknown:** No evaluation on creativity, instruction-following quality, or reasoning tasks where retrieval might not help
9. **Reflection token accuracy:** No systematic evaluation of how accurate the model's own reflection token predictions are at inference time (vs. critic predictions during training)
10. **Precision-recall tradeoff in citations:** Self-RAG 7B sometimes outperforms 13B on citation precision because smaller models generate shorter, more precisely grounded outputs -- suggesting the framework hasn't fully resolved the completeness-vs-precision tension

---

### 8. ICLR 2024 OPENREVIEW REVIEWS

The paper received an **Oral** designation (top ~1% of submissions). Four reviewers evaluated it.

#### Reviewer uRop -- Rating: 8/10 (Confidence: 3/5)
**Strengths praised:**
- "Addresses two key problems including relevance and grounding by simply adding special tokens"
- Novel framework for controllable text generation
- Does not heavily rely on human annotation

**Criticisms:**
- Reflection tokens function post-hoc and cannot guide *initial* generation quality
- Cost efficiency unclear versus just using GPT-4 directly for the task
- GPT-4's knowledge patterns may not align with smaller models' retrieval needs

**Questions:** Purpose of masking retrieved text during training? Do reflection tokens actually influence generation or just selection?

#### Reviewer 4MCy -- Rating: 8/10 (Confidence: 4/5)
**Strengths praised:**
- "Novel framework that enables dynamic, on-demand retrieval and self-reflection"
- Controllability and interpretability advantages over RLHF approaches
- Sound experiments and ablation studies

**Criticisms:**
- Lacks comparison with prompt-based active retrieval methods (like FLARE)
- Unclear impact on reasoning, creativity, and instruction-following capabilities
- Cannot synthesize information across multiple passages

**Questions:** Retrieval frequency distribution across tasks? Training data requirements? Effects on non-factuality dimensions?

#### Reviewer 3ScW -- Rating: 8/10 (Confidence: 4/5)
**Strengths praised:**
- Well-written and clearly presented paper
- Novel integration of critique model at training time rather than inference time
- Significant improvements over baselines

**Criticisms:**
- Missing systematic evaluation of reflection token prediction accuracy
- Limited ablation studies on individual token types
- No analysis of how retrieval threshold affects token distribution

#### Reviewer quEF -- Rating: 6/10 (Confidence: 2/5) -- Most Critical
**Strengths praised:**
- Addresses important RAG limitations
- Integrates self-reflection and retrieval effectively

**Major concerns:**
- Insufficient ablations separating self-reflection contributions from RAG contributions
- Abstract claims of "outperforming ChatGPT" don't fully align with Table 2 (ChatGPT wins on TriviaQA and ARC)
- Performance deterioration for retrieval baselines is suspicious, suggesting potential data leakage or unfair comparison
- No analysis of computational overhead / latency
- "High agreement" with human evaluations claimed but supporting data insufficient

#### Author Responses (Key Points):
- Conducted additional ablations showing individual token contributions: IsRel, IsSup, IsUse each contribute to performance (PopQA ranges from 0.416 to 0.538 depending on token ablation)
- Showed optimal performance with 7-10 retrieved passages (tested range 2-20)
- Explained ChatGPT retrieval degradation by citing concurrent work on irrelevant passage interference
- Provided GPT-4 agreement evaluation: manual assessment on 50 examples per token type
- Described computational optimizations: parallel batch decoding, beam search, paged attention
- Noted Self-RAG can skip retrievals entirely, sometimes requiring fewer than 3 total retrieval calls per query

**Final outcome:** All four reviewers were satisfied with responses; consensus Accept as Oral.

---

### Summary of What Makes This Paper Distinctive

Self-RAG's contribution is best understood as a **systems-level integration** that combines adaptive retrieval, inline self-critique, and inference-time controllability into a single unified framework, trained through an efficient offline distillation process. The key architectural decision -- treating reflection tokens as part of the vocabulary and training them with standard next-token prediction -- eliminates the need for separate runtime components (critic models, reward models, or retrieval decision heuristics) while maintaining the ability to customize behavior per-task through weight adjustment at inference time. The paper was recognized as an ICLR 2024 Oral for this novel synthesis and its strong empirical results across diverse tasks.

agentId: a913870cabf3d3787 (use SendMessage with to: 'a913870cabf3d3787' to continue this agent)
&lt;usage>total_tokens: 26138
tool_uses: 14
duration_ms: 243464&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "e72223a6-e6d9-40db-afae-b3c85ab62168",
  "isSidechain": false,
  "promptId": "509b9e27-9338-43ac-a97b-3de5e1bfe6b5",
  "type": "user",
  "uuid": "4e7fd5e0-77ca-4efa-ad27-8bca4988f429",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection\" by Akari Asai et al. (ICLR 2024 Oral, https://arxiv.org/abs/2310.11511).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also search for the ICLR 2024 OpenReview page to get reviewer comments. Try: https://openreview.net/forum?id=hSyW5go0v8 or search for it.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined (reflection tokens, critic model, adaptive retrieval)\n5. Their core technical method in detail (reflection token types, training procedure, inference-time control)\n6. Main results across tasks (QA, reasoning, fact verification)\n7. Limitations acknowledged or apparent\n8. Reviewer comments from ICLR 2024 OpenReview - what was praised and criticized\n\nPlease be thorough and precise. Report all findings in detail.",
    "agentId": "a913870cabf3d3787",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information from both the paper and the reviews. Let me compile the complete analysis.\n\n---\n\n## Comprehensive Analysis of Self-RAG (Asai et al., ICLR 2024 Oral)\n\n### 1. EXACT GAP/PROBLEM IDENTIFIED\n\nThe authors identified a fundamental tension in retrieval-augmented generation. Their diagnosis has two layers:\n\n**Problem with vanilla LLMs:** Large language models \"often struggle with factual errors\" because they rely solely on parametric knowledge encoded during pre-training. Scaling alone does not resolve this.\n\n**Problem with existing RAG approaches:** Prior RAG methods (Lewis et al., Guu et al.) introduced a *different* set of problems while trying to fix the first:\n- They \"retrieve passages indiscriminately regardless of whether the factual grounding is helpful\" -- retrieval happens for every query with a fixed number of passages, even when the model already knows the answer or when no retrieved passage is relevant.\n- The generated \"output is not guaranteed to be consistent with retrieved relevant passages\" -- even when relevant passages are retrieved, there is no mechanism ensuring the model actually uses them faithfully.\n- RAG improvements come \"at the expense of runtime efficiency, robustness to irrelevant context, and lack of attributions.\"\n\n**How they identified this:** The authors observed empirically that indiscriminate retrieval can *hurt* performance. For example, ChatGPT with retrieval augmentation actually performs *worse* than ChatGPT alone on several tasks (Table 2), because irrelevant passages confuse the model. They cite concurrent work by Mallen et al. (2023) documenting this phenomenon. They also noted the absence of any mechanism for LLMs to self-assess whether their own generations are factually grounded in evidence.\n\n---\n\n### 2. KEY INSIGHT THAT OTHERS MISSED\n\nThe central insight is that retrieval decisions and output quality assessment should be made *by the LM itself* as part of generation, not by external components. Specifically:\n\n1. **Retrieval should be adaptive and on-demand**, triggered by the model's own assessment of whether it needs external knowledge for the current generation step -- not applied uniformly to every input.\n\n2. **Self-critique should happen inline**, with the model evaluating its own outputs for relevance, factual support, and utility using special tokens that are part of the generation vocabulary.\n\n3. **These capabilities can be distilled into a single model** through offline training data augmentation (using a critic trained on GPT-4 labels), rather than requiring expensive online reinforcement learning (RLHF/PPO) or a separate runtime critic model.\n\nThe combination is what others missed: prior work either (a) always retrieved, (b) used external filtering/critic models at runtime adding latency, or (c) used RL-based training which is expensive and unstable. Self-RAG showed you could get all three benefits (adaptive retrieval + self-critique + controllability) through a training-time data augmentation approach with special tokens.\n\n---\n\n### 3. PROBLEM FORMULATION DIFFERENCES FROM PRIOR WORK\n\n**Traditional RAG formulation:** Given input x, retrieve documents D, generate y = M(x, D). Retrieval is a fixed preprocessing step.\n\n**Self-RAG reformulation:** Generate segmented output y = [y_1, ..., y_T] where each segment y_t can trigger:\n- A **Retrieve** token deciding whether to fetch passages\n- **Critique** tokens evaluating the passage and generation quality\n- The actual text continuation\n\nThe model's vocabulary V is expanded to include reflection tokens as first-class tokens. The generation objective becomes:\n\n```\nmax_M E log p_M(y, r | x)\n```\n\nwhere r represents reflection tokens interleaved with the output y. This is critically different from prior work because:\n- Reflection tokens and text tokens are predicted using the *same* next-token prediction objective -- no separate critic head or reward model needed at inference time\n- Retrieved passages are **masked during loss computation** -- the model never learns to memorize or reconstruct evidence, only to use it and evaluate it\n- The framework enables **segment-level beam search** at inference, where different retrieved passages produce competing continuations that are ranked by critique token scores\n\n---\n\n### 4. EXISTING TECHNIQUES ADAPTED/COMBINED\n\nSelf-RAG is a synthesis of several existing ideas, recombined in a novel way:\n\n**(a) Reflection/Critique Tokens:** Inspired by control tokens in conditional text generation (e.g., Keskar et al.'s CTRL, Lu et al.'s Quark), but repurposed. Unlike control tokens that condition generation on desired attributes, Self-RAG's reflection tokens are generated *after* output segments for self-evaluation. They serve as both training signals and inference-time quality indicators.\n\n**(b) Critic Model / Knowledge Distillation from GPT-4:** The critic model C is trained via distillation from GPT-4 judgments. For each reflection token type, 4k-20k examples are labeled by GPT-4 using type-specific prompts with few-shot demonstrations. This critic achieves >90% agreement with GPT-4. The approach adapts the \"LLM-as-judge\" paradigm (used in RLHF data collection) but applies it to generate structured token-level annotations rather than scalar rewards.\n\n**(c) Adaptive/Active Retrieval:** The idea of deciding when to retrieve draws from FLARE (Jiang et al., 2023) and similar active retrieval methods. However, Self-RAG integrates this decision into the model itself rather than using heuristics (like low-confidence token detection in FLARE).\n\n**(d) Off-the-shelf Dense Retrieval:** Uses Contriever-MS MARCO without modification as the retrieval backbone, showing the framework is retriever-agnostic.\n\n**(e) Segment-Level Beam Search:** Adapts standard beam search from token-level to segment-level, processing multiple retrieved passages in parallel and ranking them by a composite score of generation probability and critique token scores.\n\n---\n\n### 5. CORE TECHNICAL METHOD IN DETAIL\n\n#### Reflection Token Types (Table 1 in the paper):\n\n| Token | Input | Values | Purpose |\n|-------|-------|--------|---------|\n| **Retrieve** | x or (x, y_{&lt;t}) | {yes, no, continue} | Should the model retrieve at this step? |\n| **IsRel** | (x, passage d) | {relevant, irrelevant} | Is the retrieved passage useful? |\n| **IsSup** | (x, d, y_t) | {fully supported, partially supported, no support} | Is the generated segment grounded in evidence? |\n| **IsUse** | (x, y) | {5, 4, 3, 2, 1} | Overall utility of the complete response |\n\n#### Training Procedure -- Two Stages:\n\n**Stage 1: Critic Model Training (C)**\n- Base model: Llama 2-7B\n- For each of the 4 reflection token types, sample instances from training data\n- Prompt GPT-4 with type-specific instructions + few-shot examples to label each instance\n  - Example for Retrieve: \"Given an instruction, make a judgment on whether finding some external documents from the web helps to generate a better response\"\n- Collect 4k-20k labeled examples per token type\n- Train C via standard conditional language modeling: `max_C E log p_C(r | x, y)`\n- Validation: >90% agreement with GPT-4 on most token categories\n\n**Stage 2: Generator Model Training (M)**\n- Base models: Llama 2-7B and Llama 2-13B\n- Data augmentation process for each training example (x, y):\n  1. For each segment y_t: run critic C to predict Retrieve token\n  2. If Retrieve=Yes: use retriever R to fetch top-K passages\n  3. For each passage d: critic evaluates IsRel(x, d)\n  4. If relevant: generate segment, then critic evaluates IsSup(x, d, y_t)\n  5. At end of full output: critic evaluates IsUse(x, y)\n  6. Insert all reflection tokens inline into the training sequence\n- Generator training: standard next-token prediction on augmented data\n  - `max_M E log p_M(y, r | x)`\n  - **Retrieved passages are masked** in loss computation -- the model does NOT learn to reproduce evidence\n- Training data: 150k instruction-output pairs from Open-Instruct + knowledge-intensive datasets\n- Vocabulary expanded with special reflection tokens\n\n#### Inference Algorithm:\n\n**Step 1 -- Retrieval Decision:**\n- At each segment boundary, model predicts Retrieve token\n- If P(Retrieve=Yes) > threshold (default 0.2; set to 0 for tasks like ASQA that always need retrieval): trigger retrieval\n- \"continue\" means keep generating without new retrieval\n\n**Step 2 -- Parallel Generation:**\n- Retrieve top K=5 passages via Contriever-MS MARCO\n- Generate K candidate segments y_t, one conditioned on each passage, in parallel\n\n**Step 3 -- Scoring:**\nEach candidate is scored by:\n```\nf(y_t, d, Critique) = p(y_t | x, d, y_{&lt;t}) + S(Critique)\n```\nwhere:\n```\nS(Critique) = sum over G in {IsRel, IsSup, IsUse} of: w^G * s_t^G\n```\n- s_t^G = normalized probability of the most desirable token value for group G (e.g., P(IsRel=relevant) normalized)\n- w^G = user-adjustable weights (defaults: IsRel=1.0, IsSup=1.0, IsUse=0.5)\n\n**Step 4 -- Selection:**\n- Segment-level beam search with beam width = 2\n- Token-level decoding within segments is greedy\n- Best complete sequence returned\n\n**Inference-Time Controllability:**\n- **Soft control:** Adjust w^G weights to prioritize different aspects (e.g., increase w^IsSup for citation-heavy tasks)\n- **Hard control:** Filter out segments producing undesirable tokens (e.g., reject any segment with IsSup=NoSupport)\n- This is a key advantage: behavior can be customized per-task *without retraining*\n\n---\n\n### 6. MAIN RESULTS ACROSS TASKS\n\n#### Short-Form QA:\n- **PopQA** (long-tail entities): Self-RAG 13B achieves 55.8% accuracy, vs. ChatGPT 29.3%, Ret-ChatGPT 50.8%, Llama2-FT 48.7%\n- **TriviaQA**: Self-RAG 13B achieves 69.3%, vs. ChatGPT 74.3% (one of the few tasks where ChatGPT is stronger)\n\n#### Reasoning & Fact Verification:\n- **PubHealth** (fact verification): Self-RAG 13B achieves 74.5%, vs. ChatGPT 70.1%, Ret-ChatGPT 54.7%\n- **ARC-Challenge** (science reasoning): Self-RAG 13B achieves 73.1%, vs. ChatGPT 75.3%, Ret-ChatGPT 75.3%\n\n#### Long-Form Generation:\n- **Biography Generation (FactScore):** Self-RAG 7B achieves 81.2 (best overall), vs. ChatGPT 71.8, Ret-ChatGPT 71.2, Perplexity.ai 71.4\n- **ASQA (long-form QA):**\n  - Str-EM: Self-RAG 13B achieves 31.7, vs. ChatGPT 35.3, Ret-ChatGPT 40.7\n  - Citation Precision: Self-RAG 13B achieves 70.3%, vs. Ret-ChatGPT 65.1%\n  - Citation Recall: Self-RAG 13B achieves 71.3%, vs. Ret-ChatGPT 76.6%\n\n#### Key Comparative Findings:\n- Self-RAG 7B/13B outperforms all non-proprietary models across all six tasks\n- Outperforms ChatGPT on 4 of 6 tasks, and nearly matches on the other 2\n- **Llama2-FT** (same training data, no reflection tokens) consistently underperforms Self-RAG, proving gains come from the framework itself, not just the training data\n- Self-RAG adaptively retrieves 30-50% of the time depending on the task, improving efficiency over always-retrieve approaches\n\n#### Ablation Highlights:\n- Removing the critic C causes the largest drops: PopQA 45.5 -> 42.6, ASQA 32.1 -> 18.1\n- No retrieval at test time: PopQA drops from 45.5 to 24.7\n- Hard constraints only (vs. soft weighting): PopQA drops to 28.3\n- Using only top-1 passage: PopQA drops from 45.5 to 41.8\n- Scaling training data from 50k to 150k yields \"notable improvements\"\n\n---\n\n### 7. LIMITATIONS (ACKNOWLEDGED AND APPARENT)\n\n**Acknowledged by the authors:**\n1. **Computational overhead:** Segment-level beam search with multiple passages requires more compute than standard greedy decoding, though they implement optimizations (parallel batch decoding, paged attention)\n2. **Retriever dependency:** Uses off-the-shelf Contriever-MS MARCO; performance is bounded by retriever quality\n3. **GPT-4 dependency for critic training:** Initial data collection requires proprietary GPT-4 API (though this is a one-time cost, distilled into the local critic)\n4. **Segment granularity:** Framework operates at sentence-level segments; adapting to other granularities requires modification\n\n**Apparent but not deeply discussed:**\n5. **Does not outperform ChatGPT on all tasks:** TriviaQA and ARC-Challenge show Self-RAG 13B still below ChatGPT, suggesting the method works best for knowledge-intensive tasks where retrieval provides the most value\n6. **No cross-passage synthesis:** The model evaluates and selects passages independently; it cannot synthesize information spanning multiple passages (noted by Reviewer 4MCy)\n7. **Potential data leakage concerns:** Some retrieval baselines perform worse than expected, which Reviewer quEF flagged as potentially suspicious\n8. **Impact on non-factuality tasks unknown:** No evaluation on creativity, instruction-following quality, or reasoning tasks where retrieval might not help\n9. **Reflection token accuracy:** No systematic evaluation of how accurate the model's own reflection token predictions are at inference time (vs. critic predictions during training)\n10. **Precision-recall tradeoff in citations:** Self-RAG 7B sometimes outperforms 13B on citation precision because smaller models generate shorter, more precisely grounded outputs -- suggesting the framework hasn't fully resolved the completeness-vs-precision tension\n\n---\n\n### 8. ICLR 2024 OPENREVIEW REVIEWS\n\nThe paper received an **Oral** designation (top ~1% of submissions). Four reviewers evaluated it.\n\n#### Reviewer uRop -- Rating: 8/10 (Confidence: 3/5)\n**Strengths praised:**\n- \"Addresses two key problems including relevance and grounding by simply adding special tokens\"\n- Novel framework for controllable text generation\n- Does not heavily rely on human annotation\n\n**Criticisms:**\n- Reflection tokens function post-hoc and cannot guide *initial* generation quality\n- Cost efficiency unclear versus just using GPT-4 directly for the task\n- GPT-4's knowledge patterns may not align with smaller models' retrieval needs\n\n**Questions:** Purpose of masking retrieved text during training? Do reflection tokens actually influence generation or just selection?\n\n#### Reviewer 4MCy -- Rating: 8/10 (Confidence: 4/5)\n**Strengths praised:**\n- \"Novel framework that enables dynamic, on-demand retrieval and self-reflection\"\n- Controllability and interpretability advantages over RLHF approaches\n- Sound experiments and ablation studies\n\n**Criticisms:**\n- Lacks comparison with prompt-based active retrieval methods (like FLARE)\n- Unclear impact on reasoning, creativity, and instruction-following capabilities\n- Cannot synthesize information across multiple passages\n\n**Questions:** Retrieval frequency distribution across tasks? Training data requirements? Effects on non-factuality dimensions?\n\n#### Reviewer 3ScW -- Rating: 8/10 (Confidence: 4/5)\n**Strengths praised:**\n- Well-written and clearly presented paper\n- Novel integration of critique model at training time rather than inference time\n- Significant improvements over baselines\n\n**Criticisms:**\n- Missing systematic evaluation of reflection token prediction accuracy\n- Limited ablation studies on individual token types\n- No analysis of how retrieval threshold affects token distribution\n\n#### Reviewer quEF -- Rating: 6/10 (Confidence: 2/5) -- Most Critical\n**Strengths praised:**\n- Addresses important RAG limitations\n- Integrates self-reflection and retrieval effectively\n\n**Major concerns:**\n- Insufficient ablations separating self-reflection contributions from RAG contributions\n- Abstract claims of \"outperforming ChatGPT\" don't fully align with Table 2 (ChatGPT wins on TriviaQA and ARC)\n- Performance deterioration for retrieval baselines is suspicious, suggesting potential data leakage or unfair comparison\n- No analysis of computational overhead / latency\n- \"High agreement\" with human evaluations claimed but supporting data insufficient\n\n#### Author Responses (Key Points):\n- Conducted additional ablations showing individual token contributions: IsRel, IsSup, IsUse each contribute to performance (PopQA ranges from 0.416 to 0.538 depending on token ablation)\n- Showed optimal performance with 7-10 retrieved passages (tested range 2-20)\n- Explained ChatGPT retrieval degradation by citing concurrent work on irrelevant passage interference\n- Provided GPT-4 agreement evaluation: manual assessment on 50 examples per token type\n- Described computational optimizations: parallel batch decoding, beam search, paged attention\n- Noted Self-RAG can skip retrievals entirely, sometimes requiring fewer than 3 total retrieval calls per query\n\n**Final outcome:** All four reviewers were satisfied with responses; consensus Accept as Oral.\n\n---\n\n### Summary of What Makes This Paper Distinctive\n\nSelf-RAG's contribution is best understood as a **systems-level integration** that combines adaptive retrieval, inline self-critique, and inference-time controllability into a single unified framework, trained through an efficient offline distillation process. The key architectural decision -- treating reflection tokens as part of the vocabulary and training them with standard next-token prediction -- eliminates the need for separate runtime components (critic models, reward models, or retrieval decision heuristics) while maintaining the ability to customize behavior per-task through weight adjustment at inference time. The paper was recognized as an ICLR 2024 Oral for this novel synthesis and its strong empirical results across diverse tasks."
      }
    ],
    "totalDurationMs": 243464,
    "totalTokens": 26138,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 380,
      "cache_creation_input_tokens": 3005,
      "cache_read_input_tokens": 18219,
      "output_tokens": 4534,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3005
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 380,
          "output_tokens": 4534,
          "cache_read_input_tokens": 18219,
          "cache_creation_input_tokens": 3005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3005,
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
  "sourceToolAssistantUUID": "e72223a6-e6d9-40db-afae-b3c85ab62168",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "4e7fd5e0-77ca-4efa-ad27-8bca4988f429",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on reasoning-aware retrievers",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Tool result

_source line 28 · 2026-05-30T06:33:43.132Z_

<details><summary>↩ Tool result · `toolu_013KNDhzRKVEnwEUfXoKQrrC`</summary>

```text
Now I have comprehensive information. Let me compile the complete findings.

---

Here is a thorough and detailed analysis of the paper "RAG-RewardBench: Benchmarking Reward Models in Retrieval Augmented Generation for Preference Alignment" (ACL 2025 Findings).

**Note on authorship:** The first author is **Zhuoran Jin** (not Zichen Chen). The full author list is: Zhuoran Jin, Hongbang Yuan, Tianyi Men, Pengfei Cao, Yubo Chen, Kang Liu, and Jun Zhao.

---

## 1. The Exact Gap/Problem Identified

The authors identified a critical disconnect: while existing Retrieval Augmented Language Models (RALMs) have made significant progress in providing factual, grounded responses, they **"often overlook effective alignment with human preferences."** Specifically:

- RAG systems rely almost exclusively on supervised fine-tuning (SFT) and lack mechanisms for capturing nuanced human preferences.
- Existing reward model benchmarks (e.g., RewardBench) focus entirely on **general scenarios** (helpfulness, harmlessness in non-RAG contexts) and have an average prompt length of only 47 tokens -- they completely miss RAG-specific alignment requirements like citation quality, multi-document reasoning, abstention behavior, and robustness to conflicting information.
- **"It remains unclear how to evaluate and select a reliable RM for preference alignment in RALMs."** No benchmark existed to assess whether reward models could handle the distinct challenges posed by RAG settings.

They identified this gap by observing that reward models scoring above 90% on general benchmarks like RewardBench performed dramatically worse (top model only 78.3%) on RAG-specific scenarios, revealing that general-purpose evaluations do not transfer to RAG contexts.

---

## 2. Key Insight That Others Missed

The core insight was twofold:

**First**, RAG introduces fundamentally distinct preference alignment challenges that are absent from standard LLM alignment. These include: (a) whether the model reasons correctly across multiple retrieved documents, (b) whether it cites sources at the appropriate granularity (sentence-level, not just document-level), (c) whether it appropriately abstains when retrieved documents lack sufficient information rather than hallucinating, and (d) whether it resists misleading information in conflicting documents.

**Second**, and perhaps more striking: **existing trained RALMs (like SelfRAG, ChatQA, FgCite, RetRobust) show almost no improvement in preference alignment despite achieving significant improvements on standard RAG accuracy benchmarks.** This reveals that current RALM training paradigms optimize for task accuracy but not for human preference alignment -- the two are decoupled problems that require different training approaches.

---

## 3. How They Formulated the Problem Differently From Prior Work

Prior reward model benchmarks (RewardBench, M-RewardBench, RMB, RM-Bench, VL-RewardBench) evaluated RMs on general scenarios with short prompts. RAG-RewardBench reformulated the problem in three key ways:

- **RAG-specific scenario design:** Instead of generic helpfulness/harmlessness, they defined four RAG-native evaluation scenarios: multi-hop reasoning, fine-grained citation, appropriate abstention, and conflict robustness.
- **Long-context evaluation:** RAG prompts include retrieved documents, making them far longer than RewardBench's average 47-token prompts. This fundamentally changes the evaluation difficulty and necessitated a different annotation methodology (LLM-as-judge instead of human annotation).
- **Evaluation tuple formulation:** The evaluation uses preference tuples (x, y_c, y_r) where x is the prompt including retrieved documents, y_c is the chosen response, and y_r is the rejected response. The RM must predict whether y_c is better than y_r. Accuracy (random baseline = 50%) is the metric. For generative RMs, positions of y_c and y_r are swapped and evaluation is run twice to mitigate positional bias.

---

## 4. Existing Techniques They Adapted/Combined

- **LLM-as-a-Judge** (adapted from prior work on LLM evaluation): Used four commercial judge models (GPT-4o, GPT-4o-mini, Claude-3.5-Haiku, Gemini-1.5-Flash) scoring on five dimensions with five-point scales, with consistency filtering and averaging.
- **Counterfactual document synthesis** (for conflict robustness): Used GPT-4o-2024-08-06 to generate counterfactual documents based on existing datasets, a technique borrowed from robustness evaluation literature.
- **Multiple retriever diversity**: Used 6 different retrievers (BM25, DPR, E5, BGE, GTR, Google Search) spanning sparse and dense approaches to avoid retriever-specific biases.
- **Difficulty control via score gaps**: Selected preference pairs with score differences between 1-2 points, allowing controllable difficulty calibration.
- **Best-of-N (BoN) sampling**: Used as a downstream validation to check if benchmark performance correlates with practical utility.
- **Position swapping for generative RMs**: Standard debiasing technique to handle positional preference in generative evaluators.

---

## 5. Core Technical Method in Detail

### Benchmark Construction Pipeline

**Step 1 - Query Collection:** Queries sampled from 18 datasets across diverse domains.

**Step 2 - Document Retrieval:** Each query processed through 6 retrievers (BM25, DPR, E5, BGE, GTR, Google Search).

**Step 3 - Response Generation:** 24 RALMs (ranging from 3B to 70B parameters, including o1-mini, GPT-4o, Gemini-1.5-Pro, Claude 3.5, Command R, and various open-source models) generate responses given queries and retrieved documents.

**Step 4 - LLM-as-Judge Annotation:** Four commercial judges score responses on five dimensions: response clarity, response accuracy, citation appropriateness, citation correctness, and citation granularity. Each on a five-point scale.

**Step 5 - Consistency Filtering:** Prompts with low cross-judge consistency are filtered out (inter-judge Pearson r = 0.79).

**Step 6 - Pair Selection:** Average scores computed; response pairs with score differences between 1-2 selected as chosen-rejected pairs for moderate difficulty.

**Step 7 - Human Validation:** 50 pairs sampled from each of the 6 subsets; graduate-level annotators perform preference labeling; achieved Pearson correlation of 0.84 with LLM-judge annotations.

### The 18 Subsets Organized by Category

**Helpful (7 datasets, 262 samples):**
MultiFieldQA, NQ, ExpertQA, ASQA, SimpleQA, BioASQ, FreshQA -- spanning open-domain QA, biomedical QA, time-sensitive QA, domain-specific QA, long-form QA.

**Multi-hop Reasoning (3 datasets, 306 samples):**
HotpotQA, MultiHop-RAG, MuSiQue -- testing logical consistency across multiple documents.

**Fine-grained Citation (4 datasets, 361 samples):**
ASQA, ELI5, RobustQA-Science, RobustQA-Technology -- evaluating sentence-level citation accuracy and granularity.

**Harmless (2 datasets, 155 samples):**
XSTest (safety against harmful requests), Privacy (resistance to private data leakage from RAG knowledge bases susceptible to poisoning attacks).

**Appropriate Abstain (3 datasets, 217 samples):**
PopQA-Noise, NQ-Noise, CRAG-False-Premise -- testing whether models refuse to answer when retrieved content lacks sufficient information.

**Conflict Robustness (3 datasets, 184 samples):**
TriviaQA-Counterfactual, PopQA-Counterfactual, NQ-Counterfactual -- using GPT-4o-synthesized counterfactual documents to test resistance to misleading information.

**Total: 1,485 high-quality preference pairs.**

### The 4 RAG-Specific Scenarios

1. **Multi-hop Reasoning:** Tests whether RMs detect logical errors and inconsistent reasoning paths when synthesizing information across multiple retrieved documents.

2. **Fine-grained Citation:** Tests whether RMs evaluate sentence-level citation quality (not just coarse document attribution), penalizing both over-citation and under-citation.

3. **Appropriate Abstention:** Tests whether RMs prefer responses that abstain when retrieved content is insufficient, rather than rewarding fabricated answers.

4. **Conflict Robustness:** Tests whether RMs distinguish between responses that use correct facts versus those misled by counterfactual/conflicting documents injected into the retrieval results.

### Evaluation Methodology

- **Metric:** Accuracy (binary classification: does RM correctly rank y_c above y_r?), random baseline = 50%.
- **Discriminative RMs:** Assign scalar reward scores; higher score for y_c = correct.
- **Generative RMs:** Output text-based preferences; tested twice with swapped positions to handle positional bias; average accuracy reported.
- **Implicit RMs:** DPO-trained models where log-probability ratios serve as implicit rewards.

---

## 6. Key Findings About the 45 Reward Models

### Overall Performance
- **Best model:** Skywork-Critic-Llama-3.1-70B achieved only **78.3%** accuracy -- proving the benchmark is genuinely challenging.
- Models that exceed 90% on general benchmarks like RewardBench drop significantly on RAG-RewardBench.
- Average performance drops ~10% on fine-grained citation compared to general helpfulness.

### By Model Type
- **Generative RMs** (e.g., Skywork-Critic-Llama-3.1-70B at 78.3%) and **discriminative RMs** (e.g., INF-ORM-Llama3.1-70B at 76.6%) with 27B-70B parameters performed best.
- **Implicit RMs** (DPO-trained policy models) consistently underperformed, with models like Mixtral-8x7B-Instruct at 54.4% barely above random.

### Top Models by Subset
| Subset | Best Model | Score |
|--------|-----------|-------|
| Helpfulness | Skywork-Critic-Llama-3.1-70B | 85.9% |
| Reasoning | INF-ORM-Llama3.1-70B | 76.5% |
| Citation | Self-taught-Evaluator-Llama3.1-70B | 76.5% |
| Harmlessness | Skywork-Critic-Llama-3.1-70B | 91.6% |
| Abstention | INF-ORM-Llama3.1-70B | 84.8% |
| Conflict | Llama-3.1-Nemotron-70B-Reward | 84.8% |

### Selected Models Across the Performance Spectrum
| Model | Type | Average |
|-------|------|---------|
| Skywork-Critic-Llama-3.1-70B | Generative | 78.3% |
| INF-ORM-Llama3.1-70B | Discriminative | 76.6% |
| Skywork-Reward-Gemma-2-27B-v0.2 | Discriminative | 74.5% |
| Self-taught-Evaluator-Llama3.1-70B | Generative | 72.3% |
| GRM-Llama3.1-8B-rewardmodel-ft | Discriminative | 71.9% |
| Skywork-Reward-Gemma-2-27B | Discriminative | 71.2% |
| Skywork-Critic-Llama-3.1-8B | Generative | 71.0% |
| Llama-3.1-70B-Instruct | Implicit | 65.0% |
| Gemini-1.5-Flash | Generative | 64.4% |
| GPT-4-Turbo | Generative | 61.9% |
| Command R | Implicit | 57.8% |
| Llama-3.1-8B-Instruct | Implicit | 55.2% |
| Mixtral-8x7B-Instruct-v0.1 | Implicit | 54.4% |

### Notable observation
Self-taught-Evaluator-Llama3.1-70B was highlighted for its ability to **autonomously generate RAG-appropriate evaluation metrics** rather than relying on predefined criteria, achieving the top citation subset score.

---

## 7. Finding About RALMs Showing Almost No Improvement

This is one of the paper's most impactful findings. The authors tested trained RALMs (models specifically fine-tuned for RAG tasks) against their base models on RAG-RewardBench:

| Trained RALM | Base Model | Overall Score | Improvement |
|-------------|------------|---------------|-------------|
| ChatQA-1.5-8B | Llama-3-8B | 54.8% | +2.8% |
| ChatQA-2-8B | Llama-3-8B | 54.1% | +2.1% |
| FgCite-RS+RL | Llama-2-7B | 51.4% | +0.8% |
| Self-RAG-7B | -- | 51.0% | +0.4% |

The key quote: **"Despite achieving significant improvements on various RAG datasets, these models show only marginal gains compared to the base models on RAG-RewardBench"** -- with improvements as low as 0.6% on average and a maximum of only 2.8%.

These RALMs performed particularly poorly on harmlessness subsets. The authors conclude: **"The RALM training paradigm needs to shift towards preference-aligned RAG training."** Current approaches optimize for task accuracy (answering questions correctly) but completely fail to align with human preferences in the RAG context (proper citation, abstention, conflict handling, etc.).

---

## 8. Limitations -- Acknowledged and Apparent

### Explicitly Acknowledged
- The paper focuses on **benchmark construction rather than developing specialized RAG reward models** -- it identifies the problem but does not solve it.
- **Process-level or fine-grained reward signals** for RAG remain an open challenge (the benchmark only evaluates outcome-level preferences).
- Future work is needed to design **specialized generative models for long-context RAG understanding**.
- The dataset may contain **offensive content**; ethical guidelines should be applied in sensitive contexts.

### Apparent/Implicit Limitations
- **LLM-as-judge dependency:** The entire benchmark annotation relies on four commercial LLMs. While they achieve 0.84 correlation with humans on 300 sampled pairs, this validation is limited in scale and the judges themselves may have systematic biases.
- **Difficulty is artificially constrained:** By selecting only pairs with 1-2 point score differences, they create moderate difficulty but may miss easy or very hard cases that also matter for practical deployment.
- **English-only:** All 18 datasets appear to be English-language, limiting cross-lingual generalizability.
- **Static benchmark:** RAG systems evolve rapidly; a fixed benchmark of 1,485 pairs may become saturated or outdated.
- **Limited RALM diversity in alignment evaluation:** Only ~6-9 trained RALMs were tested for the alignment finding; the conclusion about RALM training paradigms is based on a relatively small sample.
- **No process reward evaluation:** The benchmark only assesses final output preferences, not intermediate reasoning steps, which are critical in multi-hop RAG scenarios.

---

## 9. Reviewer Comments

Unfortunately, the ACL Rolling Review (ARR) peer review comments for this paper are **not publicly accessible**. The OpenReview forum page exists at `https://openreview.net/forum?id=OLMB1Ir89T`, but the reviews are not exposed through the API or publicly indexed. ACL/ARR reviews are typically visible only to authors and reviewers, not made public. The paper was accepted to **ACL 2025 Findings** (pages 17061-17090), indicating it received sufficiently positive reviews for acceptance but not for the main conference track (Findings is the second tier).

---

### Key Resources
- **ArXiv:** https://arxiv.org/abs/2412.13746
- **ACL Anthology:** https://aclanthology.org/2025.findings-acl.877/
- **OpenReview:** https://openreview.net/forum?id=OLMB1Ir89T
- **Dataset:** https://huggingface.co/datasets/jinzhuoran/RAG-RewardBench/
- **Code:** https://github.com/jinzhuoran/RAG-RewardBench/

agentId: ae3d0a51cae992a81 (use SendMessage with to: 'ae3d0a51cae992a81' to continue this agent)
&lt;usage>total_tokens: 34617
tool_uses: 30
duration_ms: 328729&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15ac4ac2-0a94-464e-b939-4805a7a07b02",
  "isSidechain": false,
  "promptId": "509b9e27-9338-43ac-a97b-3de5e1bfe6b5",
  "type": "user",
  "uuid": "ed844840-abd4-43a1-943a-fdeb57162f5b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"RAG-RewardBench: Benchmarking Reward Models in Retrieval Augmented Generation for Preference Alignment\" by Zichen Chen et al. (ACL 2025 Findings, https://arxiv.org/abs/2412.13746).\n\nUse WebFetch to read the paper's abstract and full content from the arxiv page. Also try searching for any OpenReview page or ACL 2025 reviewer comments.\n\nFor this paper, I need you to extract:\n1. The exact gap/problem they identified and how they identified it\n2. Their key insight that others missed\n3. How they formulated the problem differently from prior work\n4. What existing techniques they adapted/combined\n5. Their core technical method in detail (benchmark construction, 18 subsets, 4 RAG-specific scenarios, evaluation methodology)\n6. Key findings about the 45 reward models evaluated\n7. The finding about RALMs showing almost no improvement from preference alignment\n8. Limitations acknowledged or apparent\n9. Any reviewer comments if available\n\nPlease be thorough and precise. Report all findings in detail.",
    "agentId": "ae3d0a51cae992a81",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the complete findings.\n\n---\n\nHere is a thorough and detailed analysis of the paper \"RAG-RewardBench: Benchmarking Reward Models in Retrieval Augmented Generation for Preference Alignment\" (ACL 2025 Findings).\n\n**Note on authorship:** The first author is **Zhuoran Jin** (not Zichen Chen). The full author list is: Zhuoran Jin, Hongbang Yuan, Tianyi Men, Pengfei Cao, Yubo Chen, Kang Liu, and Jun Zhao.\n\n---\n\n## 1. The Exact Gap/Problem Identified\n\nThe authors identified a critical disconnect: while existing Retrieval Augmented Language Models (RALMs) have made significant progress in providing factual, grounded responses, they **\"often overlook effective alignment with human preferences.\"** Specifically:\n\n- RAG systems rely almost exclusively on supervised fine-tuning (SFT) and lack mechanisms for capturing nuanced human preferences.\n- Existing reward model benchmarks (e.g., RewardBench) focus entirely on **general scenarios** (helpfulness, harmlessness in non-RAG contexts) and have an average prompt length of only 47 tokens -- they completely miss RAG-specific alignment requirements like citation quality, multi-document reasoning, abstention behavior, and robustness to conflicting information.\n- **\"It remains unclear how to evaluate and select a reliable RM for preference alignment in RALMs.\"** No benchmark existed to assess whether reward models could handle the distinct challenges posed by RAG settings.\n\nThey identified this gap by observing that reward models scoring above 90% on general benchmarks like RewardBench performed dramatically worse (top model only 78.3%) on RAG-specific scenarios, revealing that general-purpose evaluations do not transfer to RAG contexts.\n\n---\n\n## 2. Key Insight That Others Missed\n\nThe core insight was twofold:\n\n**First**, RAG introduces fundamentally distinct preference alignment challenges that are absent from standard LLM alignment. These include: (a) whether the model reasons correctly across multiple retrieved documents, (b) whether it cites sources at the appropriate granularity (sentence-level, not just document-level), (c) whether it appropriately abstains when retrieved documents lack sufficient information rather than hallucinating, and (d) whether it resists misleading information in conflicting documents.\n\n**Second**, and perhaps more striking: **existing trained RALMs (like SelfRAG, ChatQA, FgCite, RetRobust) show almost no improvement in preference alignment despite achieving significant improvements on standard RAG accuracy benchmarks.** This reveals that current RALM training paradigms optimize for task accuracy but not for human preference alignment -- the two are decoupled problems that require different training approaches.\n\n---\n\n## 3. How They Formulated the Problem Differently From Prior Work\n\nPrior reward model benchmarks (RewardBench, M-RewardBench, RMB, RM-Bench, VL-RewardBench) evaluated RMs on general scenarios with short prompts. RAG-RewardBench reformulated the problem in three key ways:\n\n- **RAG-specific scenario design:** Instead of generic helpfulness/harmlessness, they defined four RAG-native evaluation scenarios: multi-hop reasoning, fine-grained citation, appropriate abstention, and conflict robustness.\n- **Long-context evaluation:** RAG prompts include retrieved documents, making them far longer than RewardBench's average 47-token prompts. This fundamentally changes the evaluation difficulty and necessitated a different annotation methodology (LLM-as-judge instead of human annotation).\n- **Evaluation tuple formulation:** The evaluation uses preference tuples (x, y_c, y_r) where x is the prompt including retrieved documents, y_c is the chosen response, and y_r is the rejected response. The RM must predict whether y_c is better than y_r. Accuracy (random baseline = 50%) is the metric. For generative RMs, positions of y_c and y_r are swapped and evaluation is run twice to mitigate positional bias.\n\n---\n\n## 4. Existing Techniques They Adapted/Combined\n\n- **LLM-as-a-Judge** (adapted from prior work on LLM evaluation): Used four commercial judge models (GPT-4o, GPT-4o-mini, Claude-3.5-Haiku, Gemini-1.5-Flash) scoring on five dimensions with five-point scales, with consistency filtering and averaging.\n- **Counterfactual document synthesis** (for conflict robustness): Used GPT-4o-2024-08-06 to generate counterfactual documents based on existing datasets, a technique borrowed from robustness evaluation literature.\n- **Multiple retriever diversity**: Used 6 different retrievers (BM25, DPR, E5, BGE, GTR, Google Search) spanning sparse and dense approaches to avoid retriever-specific biases.\n- **Difficulty control via score gaps**: Selected preference pairs with score differences between 1-2 points, allowing controllable difficulty calibration.\n- **Best-of-N (BoN) sampling**: Used as a downstream validation to check if benchmark performance correlates with practical utility.\n- **Position swapping for generative RMs**: Standard debiasing technique to handle positional preference in generative evaluators.\n\n---\n\n## 5. Core Technical Method in Detail\n\n### Benchmark Construction Pipeline\n\n**Step 1 - Query Collection:** Queries sampled from 18 datasets across diverse domains.\n\n**Step 2 - Document Retrieval:** Each query processed through 6 retrievers (BM25, DPR, E5, BGE, GTR, Google Search).\n\n**Step 3 - Response Generation:** 24 RALMs (ranging from 3B to 70B parameters, including o1-mini, GPT-4o, Gemini-1.5-Pro, Claude 3.5, Command R, and various open-source models) generate responses given queries and retrieved documents.\n\n**Step 4 - LLM-as-Judge Annotation:** Four commercial judges score responses on five dimensions: response clarity, response accuracy, citation appropriateness, citation correctness, and citation granularity. Each on a five-point scale.\n\n**Step 5 - Consistency Filtering:** Prompts with low cross-judge consistency are filtered out (inter-judge Pearson r = 0.79).\n\n**Step 6 - Pair Selection:** Average scores computed; response pairs with score differences between 1-2 selected as chosen-rejected pairs for moderate difficulty.\n\n**Step 7 - Human Validation:** 50 pairs sampled from each of the 6 subsets; graduate-level annotators perform preference labeling; achieved Pearson correlation of 0.84 with LLM-judge annotations.\n\n### The 18 Subsets Organized by Category\n\n**Helpful (7 datasets, 262 samples):**\nMultiFieldQA, NQ, ExpertQA, ASQA, SimpleQA, BioASQ, FreshQA -- spanning open-domain QA, biomedical QA, time-sensitive QA, domain-specific QA, long-form QA.\n\n**Multi-hop Reasoning (3 datasets, 306 samples):**\nHotpotQA, MultiHop-RAG, MuSiQue -- testing logical consistency across multiple documents.\n\n**Fine-grained Citation (4 datasets, 361 samples):**\nASQA, ELI5, RobustQA-Science, RobustQA-Technology -- evaluating sentence-level citation accuracy and granularity.\n\n**Harmless (2 datasets, 155 samples):**\nXSTest (safety against harmful requests), Privacy (resistance to private data leakage from RAG knowledge bases susceptible to poisoning attacks).\n\n**Appropriate Abstain (3 datasets, 217 samples):**\nPopQA-Noise, NQ-Noise, CRAG-False-Premise -- testing whether models refuse to answer when retrieved content lacks sufficient information.\n\n**Conflict Robustness (3 datasets, 184 samples):**\nTriviaQA-Counterfactual, PopQA-Counterfactual, NQ-Counterfactual -- using GPT-4o-synthesized counterfactual documents to test resistance to misleading information.\n\n**Total: 1,485 high-quality preference pairs.**\n\n### The 4 RAG-Specific Scenarios\n\n1. **Multi-hop Reasoning:** Tests whether RMs detect logical errors and inconsistent reasoning paths when synthesizing information across multiple retrieved documents.\n\n2. **Fine-grained Citation:** Tests whether RMs evaluate sentence-level citation quality (not just coarse document attribution), penalizing both over-citation and under-citation.\n\n3. **Appropriate Abstention:** Tests whether RMs prefer responses that abstain when retrieved content is insufficient, rather than rewarding fabricated answers.\n\n4. **Conflict Robustness:** Tests whether RMs distinguish between responses that use correct facts versus those misled by counterfactual/conflicting documents injected into the retrieval results.\n\n### Evaluation Methodology\n\n- **Metric:** Accuracy (binary classification: does RM correctly rank y_c above y_r?), random baseline = 50%.\n- **Discriminative RMs:** Assign scalar reward scores; higher score for y_c = correct.\n- **Generative RMs:** Output text-based preferences; tested twice with swapped positions to handle positional bias; average accuracy reported.\n- **Implicit RMs:** DPO-trained models where log-probability ratios serve as implicit rewards.\n\n---\n\n## 6. Key Findings About the 45 Reward Models\n\n### Overall Performance\n- **Best model:** Skywork-Critic-Llama-3.1-70B achieved only **78.3%** accuracy -- proving the benchmark is genuinely challenging.\n- Models that exceed 90% on general benchmarks like RewardBench drop significantly on RAG-RewardBench.\n- Average performance drops ~10% on fine-grained citation compared to general helpfulness.\n\n### By Model Type\n- **Generative RMs** (e.g., Skywork-Critic-Llama-3.1-70B at 78.3%) and **discriminative RMs** (e.g., INF-ORM-Llama3.1-70B at 76.6%) with 27B-70B parameters performed best.\n- **Implicit RMs** (DPO-trained policy models) consistently underperformed, with models like Mixtral-8x7B-Instruct at 54.4% barely above random.\n\n### Top Models by Subset\n| Subset | Best Model | Score |\n|--------|-----------|-------|\n| Helpfulness | Skywork-Critic-Llama-3.1-70B | 85.9% |\n| Reasoning | INF-ORM-Llama3.1-70B | 76.5% |\n| Citation | Self-taught-Evaluator-Llama3.1-70B | 76.5% |\n| Harmlessness | Skywork-Critic-Llama-3.1-70B | 91.6% |\n| Abstention | INF-ORM-Llama3.1-70B | 84.8% |\n| Conflict | Llama-3.1-Nemotron-70B-Reward | 84.8% |\n\n### Selected Models Across the Performance Spectrum\n| Model | Type | Average |\n|-------|------|---------|\n| Skywork-Critic-Llama-3.1-70B | Generative | 78.3% |\n| INF-ORM-Llama3.1-70B | Discriminative | 76.6% |\n| Skywork-Reward-Gemma-2-27B-v0.2 | Discriminative | 74.5% |\n| Self-taught-Evaluator-Llama3.1-70B | Generative | 72.3% |\n| GRM-Llama3.1-8B-rewardmodel-ft | Discriminative | 71.9% |\n| Skywork-Reward-Gemma-2-27B | Discriminative | 71.2% |\n| Skywork-Critic-Llama-3.1-8B | Generative | 71.0% |\n| Llama-3.1-70B-Instruct | Implicit | 65.0% |\n| Gemini-1.5-Flash | Generative | 64.4% |\n| GPT-4-Turbo | Generative | 61.9% |\n| Command R | Implicit | 57.8% |\n| Llama-3.1-8B-Instruct | Implicit | 55.2% |\n| Mixtral-8x7B-Instruct-v0.1 | Implicit | 54.4% |\n\n### Notable observation\nSelf-taught-Evaluator-Llama3.1-70B was highlighted for its ability to **autonomously generate RAG-appropriate evaluation metrics** rather than relying on predefined criteria, achieving the top citation subset score.\n\n---\n\n## 7. Finding About RALMs Showing Almost No Improvement\n\nThis is one of the paper's most impactful findings. The authors tested trained RALMs (models specifically fine-tuned for RAG tasks) against their base models on RAG-RewardBench:\n\n| Trained RALM | Base Model | Overall Score | Improvement |\n|-------------|------------|---------------|-------------|\n| ChatQA-1.5-8B | Llama-3-8B | 54.8% | +2.8% |\n| ChatQA-2-8B | Llama-3-8B | 54.1% | +2.1% |\n| FgCite-RS+RL | Llama-2-7B | 51.4% | +0.8% |\n| Self-RAG-7B | -- | 51.0% | +0.4% |\n\nThe key quote: **\"Despite achieving significant improvements on various RAG datasets, these models show only marginal gains compared to the base models on RAG-RewardBench\"** -- with improvements as low as 0.6% on average and a maximum of only 2.8%.\n\nThese RALMs performed particularly poorly on harmlessness subsets. The authors conclude: **\"The RALM training paradigm needs to shift towards preference-aligned RAG training.\"** Current approaches optimize for task accuracy (answering questions correctly) but completely fail to align with human preferences in the RAG context (proper citation, abstention, conflict handling, etc.).\n\n---\n\n## 8. Limitations -- Acknowledged and Apparent\n\n### Explicitly Acknowledged\n- The paper focuses on **benchmark construction rather than developing specialized RAG reward models** -- it identifies the problem but does not solve it.\n- **Process-level or fine-grained reward signals** for RAG remain an open challenge (the benchmark only evaluates outcome-level preferences).\n- Future work is needed to design **specialized generative models for long-context RAG understanding**.\n- The dataset may contain **offensive content**; ethical guidelines should be applied in sensitive contexts.\n\n### Apparent/Implicit Limitations\n- **LLM-as-judge dependency:** The entire benchmark annotation relies on four commercial LLMs. While they achieve 0.84 correlation with humans on 300 sampled pairs, this validation is limited in scale and the judges themselves may have systematic biases.\n- **Difficulty is artificially constrained:** By selecting only pairs with 1-2 point score differences, they create moderate difficulty but may miss easy or very hard cases that also matter for practical deployment.\n- **English-only:** All 18 datasets appear to be English-language, limiting cross-lingual generalizability.\n- **Static benchmark:** RAG systems evolve rapidly; a fixed benchmark of 1,485 pairs may become saturated or outdated.\n- **Limited RALM diversity in alignment evaluation:** Only ~6-9 trained RALMs were tested for the alignment finding; the conclusion about RALM training paradigms is based on a relatively small sample.\n- **No process reward evaluation:** The benchmark only assesses final output preferences, not intermediate reasoning steps, which are critical in multi-hop RAG scenarios.\n\n---\n\n## 9. Reviewer Comments\n\nUnfortunately, the ACL Rolling Review (ARR) peer review comments for this paper are **not publicly accessible**. The OpenReview forum page exists at `https://openreview.net/forum?id=OLMB1Ir89T`, but the reviews are not exposed through the API or publicly indexed. ACL/ARR reviews are typically visible only to authors and reviewers, not made public. The paper was accepted to **ACL 2025 Findings** (pages 17061-17090), indicating it received sufficiently positive reviews for acceptance but not for the main conference track (Findings is the second tier).\n\n---\n\n### Key Resources\n- **ArXiv:** https://arxiv.org/abs/2412.13746\n- **ACL Anthology:** https://aclanthology.org/2025.findings-acl.877/\n- **OpenReview:** https://openreview.net/forum?id=OLMB1Ir89T\n- **Dataset:** https://huggingface.co/datasets/jinzhuoran/RAG-RewardBench/\n- **Code:** https://github.com/jinzhuoran/RAG-RewardBench/"
      }
    ],
    "totalDurationMs": 328729,
    "totalTokens": 34617,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 29357,
      "output_tokens": 4116,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1143
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4116,
          "cache_read_input_tokens": 29357,
          "cache_creation_input_tokens": 1143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1143,
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
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 27
    }
  },
  "sourceToolAssistantUUID": "15ac4ac2-0a94-464e-b939-4805a7a07b02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-30T06:33:51.613Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research on all 5 papers. Let me synthesize this into the required JSON format, keeping each analysis under 2000 characters. Let me craft concise, analytical summaries for each paper.

Let me count characters carefully for each entry.

1. **ReasonIR** - SOTA retriever on BRIGHT, synthetic data pipeline for reasoning-intensive retrieval
2. **RaDeR** - MCTS-based reasoning trajectories for retriever training, sample-efficient
3. **CoSearch** - Joint training of reasoning agent and document ranker via GRPO
4. **RAG-RewardBench** - Benchmark for reward models in RAG settings


5. **Self-RAG** - Learned reflection tokens for adaptive retrieval and self-critique

Now I'll generate the JSON output with detailed analyses for each paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed844840-abd4-43a1-943a-fdeb57162f5b",
  "isSidechain": false,
  "requestId": "req_011CbYHbxFFX4875nsmR8ExB",
  "type": "assistant",
  "uuid": "d86b7685-c426-4c0b-8831-f28da0bdf315",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5UET68KWPjZc7KwknucyT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4633,
      "cache_creation_input_tokens": 18662,
      "cache_read_input_tokens": 15794,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4633,
          "output_tokens": 3148,
          "cache_read_input_tokens": 15794,
          "cache_creation_input_tokens": 18662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18662
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

_source line 30 · 2026-05-30T06:35:14.464Z_

Now I have comprehensive research on all 5 papers. Let me synthesize the findings into the required JSON format with concise analyses under 2000 characters each.

```json
[
  {
    "title": "ReasonIR: Training Retrievers for Reasoning Tasks",
    "venue": "arXiv 2025 (accepted COLM 2025)",
    "problem_identification": "Existing retrievers fail on reasoning-intensive queries because training data consists of short factual QA pairs (~20 tokens), while reasoning queries average ~194 tokens and require multi-step inference to match documents. A pilot study showed retrievers plateau or degrade beyond ~256 token queries despite supporting longer contexts.",
    "key_insight": "The bottleneck for reasoning-intensive retrieval is training data distribution, not model architecture or context length — retrievers must be trained on long, reasoning-structured query-document pairs where relevance requires inference, not lexical overlap.",
    "innovation_type": "new_technique",
    "method_summary": "Builds a synthetic data pipeline using Llama-3.1-70B producing two data types: Varied-Length (VL) data with 300–2000 word queries and Hard Query (HQ) data targeting higher-order thinking (analysis, synthesis). Hard negatives are generated via multi-turn prompting conditioned on both query and positive, avoiding false negatives from failed BM25 mining. Trains a bi-encoder (Llama-3.1-8B with bidirectional attention) on ~1.73M samples using InfoNCE loss. A simple score interpolation reranker (0.5*reranker + 0.5*retriever) achieves near-SOTA at 200x less compute than reasoning rerankers.",
    "limitations_and_open_questions": "HQ seed documents drawn from BRIGHT corpus raise domain leakage concerns (reviewers flagged this). Coding/theorem domains remain weak (10.5–19.6 nDCG@10). Requires 70B LLM for quality data generation — 8B produces significantly worse negatives. No utility-based or reward-model-based training signal; purely contrastive.",
    "building_blocks": ["Synthetic reasoning-intensive query generation pipeline", "Multi-turn hard negative generation", "Score interpolation reranking", "BRIGHT benchmark (29.9 nDCG@10 baseline)", "Query rewriting as test-time compute scaling"],
    "relevance_to_seed": "Primary baseline to beat on BRIGHT; demonstrates contrastive training ceiling without reward-based utility signals — our learned reward model targets exactly the gap where synthetic contrastive data cannot distinguish reasoning-helpful from answer-containing documents."
  },
  {
    "title": "RaDeR: Reasoning-aware Dense Retrieval Models",
    "venue": "EMNLP 2025 (Main)",
    "problem_identification": "No first-stage dense retriever performs reasoning for relevance judgment — prior work either uses off-the-shelf retrievers with reasoning-augmented queries (IRCoT, ReAct) or reasoning rerankers (RANK-1) limited by first-stage recall. CoT query augmentation helps BM25 via added terms but fails for dense retrievers lacking reasoning training.",
    "key_insight": "MCTS-based math problem solving naturally generates reasoning-intensive retriever training data: partial solution trajectories become queries, retrieved theorems verified by answer correctness become positives, and self-reflection-rejected theorems become hard negatives — all with automatic relevance labels requiring no human annotation.",
    "innovation_type": "combination",
    "method_summary": "Extends the rStar MCTS framework with Generate-Query and Retrieve-Theorem actions over ProofWiki. High-reward trajectories yield (partial-CoT-query, theorem) training pairs; theorems rejected by LLM self-reflection become hard negatives. Generates three reasoning query types (MCTS-CoT, LLM-reasoning, question) plus lexical queries filtered by round-trip BM25 consistency. Trains bi-encoder retrievers (Qwen2.5 variants) with InfoNCE on only 43K–121K samples.",
    "limitations_and_open_questions": "Single-document reasoning only — cannot handle multi-hop where relevance is interdependent. Math-domain data pipeline requires verifiable answers and structured knowledge bases; extension to other domains is non-trivial. MS MARCO MRR drops from 41.2 to 34.4 vs RepLLaMA, suggesting reasoning-standard retrieval tradeoff.",
    "building_blocks": ["MCTS-derived retrieval training data", "Self-reflective relevance evaluation as automatic labeling", "Answer correctness as proxy relevance signal", "Sample-efficient training (2.5% of ReasonIR's data, +1.1 nDCG@10)"],
    "relevance_to_seed": "Demonstrates that answer-correctness reward signals from reasoning trajectories can train effective retrievers with extreme sample efficiency — validates the principle that downstream task performance can supervise retriever training, but uses binary answer correctness rather than a learned reasoning-quality reward model."
  },
  {
    "title": "CoSearch: Joint Training of Reasoning and Document Ranking via Reinforcement Learning for Agentic Search",
    "venue": "arXiv 2026 (in submission)",
    "problem_identification": "Existing agentic search systems (Search-R1) treat retrieval as a frozen tool, optimizing only the reasoning agent. An oracle experiment promoting answer-containing documents to top positions showed 26.8% relative F1 improvement for a 3B agent, proving retrieval quality is a major bottleneck.",
    "key_insight": "The reasoning agent and document ranker are interdependent and must be co-optimized — the agent's sub-queries shape ranker inputs while ranker outputs shape agent reasoning, creating a feedback loop that fixed-retriever training cannot exploit.",
    "innovation_type": "new_formulation",
    "method_summary": "Jointly optimizes a reasoning agent and a generative listwise ranker (both Qwen2.5-7B) via GRPO. The ranker reranks 50 E5-retrieved candidates to top-5. A novel semantic query grouping technique (token-F1 threshold δ=0.8) clusters sub-queries across rollouts to satisfy GRPO's identical-input requirement for the ranker — at zero additional sampling cost. Composite rewards combine Hit@k relevance (when answer-containing docs exist) with trajectory-level F1 (always), with a threshold γ=0.5 governing the mixture.",
    "limitations_and_open_questions": "First-stage retriever (E5) remains frozen, capping recall. Evaluated only on QA benchmarks with Wikipedia corpus — no reasoning-intensive benchmarks like BRIGHT. Pseudo-relevance labels (string match for answer) conflate answer-containing with reasoning-helpful documents. 3B ranker caused training divergence, suggesting minimum capacity requirements.",
    "building_blocks": ["Semantic query grouping for GRPO on rankers", "Composite relevance + trajectory rewards", "Oracle retrieval experiments to quantify retrieval bottleneck", "Joint agent-ranker RL framework"],
    "relevance_to_seed": "Closest architectural parallel to our proposal — applies RL rewards to train a retrieval component — but uses answer-correctness rewards (binary F1) rather than learned reasoning-quality rewards, and trains a reranker rather than the dense retriever itself. Validates that RL-based retrieval training improves agentic search but does not address the reasoning-utility distinction."
  },
  {
    "title": "RAG-RewardBench: Benchmarking Reward Models in Retrieval Augmented Generation for Preference Alignment",
    "venue": "ACL 2025 (Findings)",
    "problem_identification": "Existing RM benchmarks (RewardBench) evaluate only general scenarios with ~47-token prompts, completely missing RAG-specific challenges. Models scoring 90%+ on RewardBench drop to 78.3% on RAG tasks. No benchmark existed to assess RMs on multi-hop reasoning, citation quality, abstention, or conflict robustness in RAG contexts.",
    "key_insight": "Trained RALMs (Self-RAG, ChatQA, FgCite) show almost no preference alignment improvement over base models (0.4–2.8%) despite large accuracy gains on RAG tasks — current RALM training optimizes task accuracy but completely fails to align with human preferences for citation, abstention, and robustness.",
    "innovation_type": "new_benchmark",
    "method_summary": "Constructs 1,485 preference pairs across 18 datasets in 4 RAG-specific scenarios (multi-hop reasoning, fine-grained citation, appropriate abstention, conflict robustness). Uses 24 RALMs for response generation, 6 diverse retrievers, and 4 commercial LLM judges scoring 5 dimensions. Consistency filtering and difficulty calibration (1–2 point score gaps) ensure quality. Evaluates 45 RMs spanning discriminative, generative, and implicit (DPO) types.",
    "limitations_and_open_questions": "Evaluates only outcome-level preferences, not process-level reasoning quality. LLM-as-judge dependency may introduce systematic biases. Static benchmark of 1,485 pairs risks saturation. The benchmark identifies the RM gap for RAG but proposes no solution — designing RAG-specialized RMs remains open.",
    "building_blocks": ["RAG-specific RM evaluation taxonomy (4 scenarios, 18 subsets)", "LLM-as-judge annotation pipeline with consistency filtering", "Evidence that implicit RMs (DPO) fail in RAG contexts", "Baseline RM performance data for RAG reward modeling"],
    "relevance_to_seed": "Directly validates our premise that existing RMs are inadequate for RAG-specific evaluation and that a specialized learned reward model is needed. The multi-hop reasoning and citation scenarios provide evaluation methodology for our reasoning-utility reward model, and the finding that RALMs fail at preference alignment motivates reward-model-driven training."
  },
  {
    "title": "Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection",
    "venue": "ICLR 2024 (Oral, top 1%)",
    "problem_identification": "Indiscriminate retrieval in RAG systems hurts performance — ChatGPT with retrieval scores worse than without on several tasks. Additionally, no mechanism ensures generated text is faithful to retrieved evidence. The gap is both when-to-retrieve and how-to-verify-grounding.",
    "key_insight": "Retrieval decisions and output quality assessment can be distilled into the LM itself as special reflection tokens (Retrieve, IsRel, IsSup, IsUse), trained via standard next-token prediction on critic-augmented data — eliminating the need for separate runtime components or expensive online RL.",
    "innovation_type": "new_formulation",
    "method_summary": "Trains a critic model (Llama2-7B) on GPT-4-labeled examples to predict 4 reflection token types. Uses this critic offline to augment 150K training examples with inline reflection tokens. Trains the generator on augmented sequences where retrieved passages are masked in loss computation. At inference, segment-level beam search scores candidates using both generation probability and reflection token probabilities, with user-adjustable weights enabling per-task controllability without retraining.",
    "limitations_and_open_questions": "Evaluates single-passage selection only — no cross-passage synthesis (reviewer 4MCy). Reflection tokens are post-hoc selectors, not generation guides. Computational overhead of segment-level beam search with multiple passages. Retriever (Contriever) remains frozen and off-the-shelf, bounding recall quality.",
    "building_blocks": ["Reflection token paradigm for learned self-evaluation in RAG", "Critic-based offline data augmentation (avoiding online RL)", "Inference-time controllability via reflection token weights", "Segment-level beam search with critique scoring"],
    "relevance_to_seed": "Foundational paradigm for learned evaluation signals in RAG — our reasoning-utility reward model extends the reflection token concept from generation-quality evaluation to document-utility evaluation for retriever training. Self-RAG's IsRel/IsSup tokens evaluate 'does this passage support generation' while our reward model would evaluate 'does this document improve reasoning chain quality' — a complementary but distinct signal."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d86b7685-c426-4c0b-8831-f28da0bdf315",
  "isSidechain": false,
  "requestId": "req_011CbYHbxFFX4875nsmR8ExB",
  "type": "assistant",
  "uuid": "0b95e2d4-ef93-4b72-8210-750dc062af70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V5UET68KWPjZc7KwknucyT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4633,
      "cache_creation_input_tokens": 18662,
      "cache_read_input_tokens": 15794,
      "output_tokens": 3148,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4633,
          "output_tokens": 3148,
          "cache_read_input_tokens": 15794,
          "cache_creation_input_tokens": 18662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18662
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
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "0b95e2d4-ef93-4b72-8210-750dc062af70",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on reasoning-aware retrievers",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "0b95e2d4-ef93-4b72-8210-750dc062af70",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on reasoning-aware retrievers",
  "sessionId": "dddbbea0-aee9-49cc-be74-8741d74f3ef2"
}
```

---
