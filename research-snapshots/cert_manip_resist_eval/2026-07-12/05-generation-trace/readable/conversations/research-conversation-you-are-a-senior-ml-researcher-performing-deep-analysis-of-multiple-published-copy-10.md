# Research conversation: You are a senior ML researcher performing deep analysis of multiple published papers. **Today's date: 2026-05-30 (UTC).*

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/27d805b7-0ea1-4632-9635-35f016c03b5a.jsonl`
- **Structured JSON:** [`eb85debf9b0d7536ec13.json`](../../sessions/eb/eb85debf9b0d7536ec13.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:27:41.483Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:27:41.483Z",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "content": "You are a senior ML researcher performing deep analysis of multiple published papers.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: Information Retrieval and Knowledge Management\n\nDirection: Train a learned reward model that evaluates whether retrieved documents improve multi-step reasoning chain quality (not just final answer correctness), then use this reasoning-utility reward model as a training signal for dense retrievers via RL or contrastive learning. Evaluate on reasoning-intensive retrieval benchmarks (BRIGHT) where existing utility-based retrievers have not been tested.\n\nSeed Papers:\n- BRIGHT (ICLR 2025) — Established the 40.7-point gap for reasoning-intensive retrieval; defines the evaluation target\n- SCARLet (EMNLP 2025) — Demonstrated utility-based retriever training via perturbation attribution, but uses heuristic utility estimation, not a learned reward model\n- Agentic-R (arXiv Jan 2026) — Trained retrievers on downstream answer correctness (binary EM) as utility signal; closest existing work but uses heuristic signal, not learned reasoning quality\n- ReasonIR (arXiv Apr 2025) — SOTA retriever-only baseline on BRIGHT (29.9 nDCG@10); uses synthetic contrastive data, not reward-based training\n\nKnown Gaps:\n- No existing work uses a LEARNED reward model (as opposed to heuristic EM or perturbation) to evaluate document utility for reasoning-intensive retrieval\n- No utility-based retriever training method has been evaluated on BRIGHT; all evaluations are on standard QA benchmarks\n- The distinction between 'document helps answer' vs 'document helps reasoning process' is unformalized — Agentic-R's binary EM conflates documents containing answers with documents that aid reasoning\n\nTheoretical Anchor: Information-theoretic utility: a document's value for reasoning is the mutual information between the document and the reasoning chain conditioned on the query, not the mutual information between the document and the answer. This distinction predicts that utility-based training with reasoning-quality rewards should preferentially retrieve tutorial/explanation documents over answer-containing documents for reasoning-intensive queries.\n\nConstraints:\n- Compute: ≤200 H100-hours\n\nQuality Self-Checks:\n- [ ] Core insight: Documents that help reasoning are different from documents that contain answers, and a learned reward model can distinguish them where binary EM cannot.\n- [ ] Why not obvious: Agentic-R and SCARLet show utility-based training works, but their heuristic signals (EM, perturbation) cannot distinguish reasoning-helpful from answer-containing documents. A learned reward model is needed because reasoning utility is a latent property requiring inference.\n- [ ] Baseline fear test: YES — Agentic-R's simple binary EM baseline achieves strong results on QA benchmarks. The key bet is that learned reasoning-quality rewards provide gains specifically on reasoning-INTENSIVE tasks (BRIGHT) where EM-based utility training would fail because relevant documents don't contain answers.\n- [ ] Information exploited: Reasoning chain quality signals (intermediate step correctness, coherence, faithfulness) that heuristic utility measures ignore.\n\nAvoid:\n- Conflating this with training the LLM/generator (the vast majority of RL-for-RAG work trains the LLM, not the retriever — we must train the retriever)\n- Claiming the utility-vs-relevance insight is novel (SCARLet and Agentic-R have already demonstrated it; our contribution is the LEARNED REWARD MODEL and REASONING-INTENSIVE evaluation)**\n\n## Your task (Batch 1)\n\nAnalyze the following 5 papers. For EACH paper:\n1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.\n2. If on OpenReview, also read reviewer comments.\n3. Write a concise analysis focusing on HOW the paper innovates.\n\n## Papers to analyze\n\n[\n  {\n    \"title\": \"BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval\",\n    \"authors\": \"Hongjin Su et al.\",\n    \"venue\": \"ICLR 2025 (Spotlight)\",\n    \"url\": \"https://arxiv.org/abs/2407.12883\",\n    \"why_important\": \"Spotlight at ICLR 2025; defines the evaluation target — established the 40.7-point gap between LLM rerankers and standard retrievers on reasoning-intensive queries, creating the benchmark that your work directly targets.\",\n    \"one_line_summary\": \"Introduces the first benchmark of 1,398 real-world queries requiring intensive reasoning for retrieval, revealing that even SOTA retrievers fail catastrophically when surface-level similarity doesn't indicate relevance.\"\n  },\n  {\n    \"title\": \"SCARLet: Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models\",\n    \"authors\": \"Yilong Xu et al.\",\n    \"venue\": \"EMNLP 2025 (Main)\",\n    \"url\": \"https://arxiv.org/abs/2504.00573\",\n    \"why_important\": \"First principled demonstration of utility-based (vs. relevance-based) retriever training using perturbation attribution; directly motivates the shift from heuristic to learned utility estimation.\",\n    \"one_line_summary\": \"Trains retrievers by estimating passage-level utility via perturbation-based attribution on shared context, capturing inter-passage interactions to improve downstream RALM performance across 10 diverse datasets.\"\n  },\n  {\n    \"title\": \"Process Reward Models That Think (ThinkPRM)\",\n    \"authors\": \"Mahmoud Khalil et al.\",\n    \"venue\": \"arXiv 2025 (ICLR 2026 submission)\",\n    \"url\": \"https://arxiv.org/abs/2504.16828\",\n    \"why_important\": \"Demonstrates that generative PRMs fine-tuned on only 8K step labels can outperform discriminative PRMs and generalize across domains — shows learned reasoning quality evaluation is feasible with minimal supervision.\",\n    \"one_line_summary\": \"Introduces a generative process reward model that verifies reasoning steps via long chain-of-thought verification, achieving SOTA on math reasoning benchmarks with orders of magnitude fewer process labels than discriminative PRMs.\"\n  },\n  {\n    \"title\": \"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning (ReasonRAG)\",\n    \"authors\": \"Wenlin Zhang et al.\",\n    \"venue\": \"arXiv 2025\",\n    \"url\": \"https://arxiv.org/abs/2505.14069\",\n    \"why_important\": \"Directly compares process vs. outcome rewards for RAG RL; shows process-level rewards achieve 18× data efficiency — provides empirical evidence that fine-grained reasoning rewards outperform binary EM signals.\",\n    \"one_line_summary\": \"Introduces RAG-ProGuide with fine-grained process-level rewards for query generation, evidence extraction, and answer generation, demonstrating 18× data efficiency over outcome-only approaches like Search-R1.\"\n  },\n  {\n    \"title\": \"Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval Paradigm (LREM)\",\n    \"authors\": \"Jianting Tang et al.\",\n    \"venue\": \"arXiv 2025\",\n    \"url\": \"https://arxiv.org/abs/2510.14321\",\n    \"why_important\": \"Deployed at scale on China's largest e-commerce platform since Aug 2025; demonstrates the full pipeline of reasoning-augmented embeddings trained via SFT + RL with real-world validation.\",\n    \"one_line_summary\": \"Integrates chain-of-thought reasoning into query embedding generation with two-stage SFT+RL training, deployed on Alibaba's e-commerce platform to bridge semantic gaps between complex queries and product documents.\"\n  }\n]\n\n## Analysis requirements\n\nFor each paper, analyze:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- If reviewer comments are available: what was praised, what was criticized?\n\n## CRITICAL: Length constraint\n\n**Each paper's analysis MUST be under 2000 characters.** Be concise and analytical — no filler, no generic praise, no redundant descriptions. Every sentence must carry information.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem? How found? (1-2 sentences)\",\n  \"key_insight\": \"Core intellectual contribution (1 sentence)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach (2-3 sentences)\",\n  \"limitations_and_open_questions\": \"Gaps + follow-up questions (1-2 sentences)\",\n  \"building_blocks\": [\"Reusable methods/tools/datasets\"],\n  \"relevance_to_seed\": \"Relation to our research area (1 sentence)\"\n}\n\nYou MUST output exactly 5 analyses in the JSON array. IMPORTANT: End your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:27:41.504Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:27:41.504Z",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-30T06:27:41.745Z_

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

## Your task (Batch 1)

Analyze the following 5 papers. For EACH paper:
1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.
2. If on OpenReview, also read reviewer comments.
3. Write a concise analysis focusing on HOW the paper innovates.

## Papers to analyze

[
  {
    "title": "BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval",
    "authors": "Hongjin Su et al.",
    "venue": "ICLR 2025 (Spotlight)",
    "url": "https://arxiv.org/abs/2407.12883",
    "why_important": "Spotlight at ICLR 2025; defines the evaluation target — established the 40.7-point gap between LLM rerankers and standard retrievers on reasoning-intensive queries, creating the benchmark that your work directly targets.",
    "one_line_summary": "Introduces the first benchmark of 1,398 real-world queries requiring intensive reasoning for retrieval, revealing that even SOTA retrievers fail catastrophically when surface-level similarity doesn't indicate relevance."
  },
  {
    "title": "SCARLet: Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models",
    "authors": "Yilong Xu et al.",
    "venue": "EMNLP 2025 (Main)",
    "url": "https://arxiv.org/abs/2504.00573",
    "why_important": "First principled demonstration of utility-based (vs. relevance-based) retriever training using perturbation attribution; directly motivates the shift from heuristic to learned utility estimation.",
    "one_line_summary": "Trains retrievers by estimating passage-level utility via perturbation-based attribution on shared context, capturing inter-passage interactions to improve downstream RALM performance across 10 diverse datasets."
  },
  {
    "title": "Process Reward Models That Think (ThinkPRM)",
    "authors": "Mahmoud Khalil et al.",
    "venue": "arXiv 2025 (ICLR 2026 submission)",
    "url": "https://arxiv.org/abs/2504.16828",
    "why_important": "Demonstrates that generative PRMs fine-tuned on only 8K step labels can outperform discriminative PRMs and generalize across domains — shows learned reasoning quality evaluation is feasible with minimal supervision.",
    "one_line_summary": "Introduces a generative process reward model that verifies reasoning steps via long chain-of-thought verification, achieving SOTA on math reasoning benchmarks with orders of magnitude fewer process labels than discriminative PRMs."
  },
  {
    "title": "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning (ReasonRAG)",
    "authors": "Wenlin Zhang et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2505.14069",
    "why_important": "Directly compares process vs. outcome rewards for RAG RL; shows process-level rewards achieve 18× data efficiency — provides empirical evidence that fine-grained reasoning rewards outperform binary EM signals.",
    "one_line_summary": "Introduces RAG-ProGuide with fine-grained process-level rewards for query generation, evidence extraction, and answer generation, demonstrating 18× data efficiency over outcome-only approaches like Search-R1."
  },
  {
    "title": "Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval Paradigm (LREM)",
    "authors": "Jianting Tang et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2510.14321",
    "why_important": "Deployed at scale on China's largest e-commerce platform since Aug 2025; demonstrates the full pipeline of reasoning-augmented embeddings trained via SFT + RL with real-world validation.",
    "one_line_summary": "Integrates chain-of-thought reasoning into query embedding generation with two-stage SFT+RL training, deployed on Alibaba's e-commerce platform to bridge semantic gaps between complex queries and product documents."
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
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "type": "user",
  "uuid": "7691ac98-6b4a-4e08-b785-7134fafe3e98",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:27:41.743Z_

```json
{
  "parentUuid": "7691ac98-6b4a-4e08-b785-7134fafe3e98",
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
  "uuid": "29343e85-c6ab-4e2a-a26c-ea4a3f8c40de",
  "timestamp": "2026-05-30T06:27:41.743Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:27:41.743Z_

```json
{
  "parentUuid": "29343e85-c6ab-4e2a-a26c-ea4a3f8c40de",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "563b255b-eeb3-4e82-8d20-226ce5f94080",
  "timestamp": "2026-05-30T06:27:41.743Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
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
  "aiTitle": "Analyze papers for AAAI 2026 reasoning-intensive retrieval",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Assistant

_source line 7 · 2026-05-30T06:27:44.726Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze 5 papers in detail. Let me search for and read each paper, then provide structured analyses. I'll launch multiple agents to research these papers in parallel for efficiency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "563b255b-eeb3-4e82-8d20-226ce5f94080",
  "isSidechain": false,
  "requestId": "req_011CbYH9KMzsDwuWV1HzovgT",
  "type": "assistant",
  "uuid": "ee0d4ee0-ca87-47ae-b4fa-f546a5857810",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmDDzs27cwE5PgHMJpP58G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 11014,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3602
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

_source line 8 · 2026-05-30T06:27:45.843Z_

I'll research all 5 papers in parallel to gather their abstracts, methods, and any reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee0d4ee0-ca87-47ae-b4fa-f546a5857810",
  "isSidechain": false,
  "requestId": "req_011CbYH9KMzsDwuWV1HzovgT",
  "type": "assistant",
  "uuid": "7fbb2c7e-36fd-4568-9630-ac89cda94317",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmDDzs27cwE5PgHMJpP58G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 11014,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3602
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

_source line 9 · 2026-05-30T06:27:46.412Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Lv6A7yD4MkMw36xuda63BM`</summary>

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
  "parentUuid": "7fbb2c7e-36fd-4568-9630-ac89cda94317",
  "isSidechain": false,
  "requestId": "req_011CbYH9KMzsDwuWV1HzovgT",
  "type": "assistant",
  "uuid": "283d2619-db98-43ee-894e-7f31a098197e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SmDDzs27cwE5PgHMJpP58G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3602,
      "cache_read_input_tokens": 11014,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 160,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3602
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

_source line 10 · 2026-05-30T06:27:46.423Z_

<details><summary>↩ Tool result · `toolu_01Lv6A7yD4MkMw36xuda63BM`</summary>

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
  "parentUuid": "283d2619-db98-43ee-894e-7f31a098197e",
  "isSidechain": false,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "type": "user",
  "uuid": "e8d205e7-c2be-47c8-bad6-bbceb522ccb8",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "283d2619-db98-43ee-894e-7f31a098197e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-30T06:27:48.178Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the WebSearch and WebFetch tools available. Let me research all 5 papers in parallel using agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d205e7-c2be-47c8-bad6-bbceb522ccb8",
  "isSidechain": false,
  "requestId": "req_011CbYH9fPmBXtfYbZy22kF4",
  "type": "assistant",
  "uuid": "24c5253d-012b-4654-8d86-122d6a17fad6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175iVYouCFsjzfAdbLAdSwh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 14616,
      "output_tokens": 1755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1755,
          "cache_read_input_tokens": 14616,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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

_source line 12 · 2026-05-30T06:27:48.830Z_

Now let me research all 5 papers in parallel using agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24c5253d-012b-4654-8d86-122d6a17fad6",
  "isSidechain": false,
  "requestId": "req_011CbYH9fPmBXtfYbZy22kF4",
  "type": "assistant",
  "uuid": "d98c8d88-4813-47dc-9a34-62aff38337d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175iVYouCFsjzfAdbLAdSwh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 14616,
      "output_tokens": 1755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1755,
          "cache_read_input_tokens": 14616,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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

_source line 13 · 2026-05-30T06:27:56.619Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YMWVmxfmq3dP9jEMEjTMqb`</summary>

```json
{
  "description": "Research BRIGHT paper",
  "prompt": "Research the paper \"BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval\" by Hongjin Su et al. (ICLR 2025 Spotlight), arxiv URL: https://arxiv.org/abs/2407.12883\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF on arxiv (https://arxiv.org/pdf/2407.12883)\n3. Search for and read OpenReview reviews for this paper (it's ICLR 2025 spotlight)\n\nFor each, extract:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- Reviewer praise and criticism (from OpenReview)\n- Technical method details (how they constructed the benchmark, what evaluation protocol)\n- Key quantitative results (especially the 40.7-point gap)\n\nBe thorough and specific. Return all findings in a structured format.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d98c8d88-4813-47dc-9a34-62aff38337d2",
  "isSidechain": false,
  "requestId": "req_011CbYH9fPmBXtfYbZy22kF4",
  "type": "assistant",
  "uuid": "767d7aed-a40e-4a0a-b18d-308a63c5dc27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175iVYouCFsjzfAdbLAdSwh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 14616,
      "output_tokens": 1755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1755,
          "cache_read_input_tokens": 14616,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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

_source line 14 · 2026-05-30T06:28:01.161Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KQMvHoLi1mUjLqstzybp7K`</summary>

```json
{
  "description": "Research SCARLet paper",
  "prompt": "Research the paper \"SCARLet: Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models\" by Yilong Xu et al. (EMNLP 2025 Main), arxiv URL: https://arxiv.org/abs/2504.00573\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF (https://arxiv.org/pdf/2504.00573)\n3. Search for OpenReview reviews if available\n\nFor each, extract:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently? (especially the utility vs relevance distinction)\n- What existing technique did they adapt/combine/simplify? (perturbation attribution details)\n- Technical method details (shared context attribution, how they estimate utility)\n- Key quantitative results\n- Limitations\n\nBe thorough and specific. Return all findings in a structured format.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "767d7aed-a40e-4a0a-b18d-308a63c5dc27",
  "isSidechain": false,
  "requestId": "req_011CbYH9fPmBXtfYbZy22kF4",
  "type": "assistant",
  "uuid": "cbdc5c65-35d7-4b33-a85a-1b02a0aaad4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175iVYouCFsjzfAdbLAdSwh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 14616,
      "output_tokens": 1755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1755,
          "cache_read_input_tokens": 14616,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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

_source line 15 · 2026-05-30T06:28:06.023Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016yJa5G8aRY4yuQWVAvDe9N`</summary>

```json
{
  "description": "Research ThinkPRM paper",
  "prompt": "Research the paper \"Process Reward Models That Think (ThinkPRM)\" by Mahmoud Khalil et al. (arXiv 2025, ICLR 2026 submission), arxiv URL: https://arxiv.org/abs/2504.16828\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF (https://arxiv.org/pdf/2504.16828)\n3. Search for OpenReview reviews for ICLR 2026 if available\n\nFor each, extract:\n- What gap did they identify and HOW? (discriminative vs generative PRMs)\n- What was the key insight others missed? (using long CoT for verification)\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- Technical method details (how they fine-tune, what data they use, the 8K step labels claim)\n- Key quantitative results (performance vs discriminative PRMs, generalization)\n- Limitations\n\nBe thorough and specific. Return all findings in a structured format.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbdc5c65-35d7-4b33-a85a-1b02a0aaad4d",
  "isSidechain": false,
  "requestId": "req_011CbYH9fPmBXtfYbZy22kF4",
  "type": "assistant",
  "uuid": "f2124f8d-f8ef-46fe-84ee-db9317ef4de8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175iVYouCFsjzfAdbLAdSwh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 14616,
      "output_tokens": 1755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1755,
          "cache_read_input_tokens": 14616,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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

_source line 16 · 2026-05-30T06:28:12.204Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017SMqKJjubQWz4o3b8AJ2oR`</summary>

```json
{
  "description": "Research ReasonRAG paper",
  "prompt": "Research the paper \"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning\" (ReasonRAG / RAG-ProGuide) by Wenlin Zhang et al. (arXiv 2025), arxiv URL: https://arxiv.org/abs/2505.14069\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF (https://arxiv.org/pdf/2505.14069)\n3. Search for any reviews or discussion about this paper\n\nFor each, extract:\n- What gap did they identify and HOW? (process vs outcome rewards for RAG)\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- Technical method details (RAG-ProGuide, the process-level rewards for query generation, evidence extraction, answer generation)\n- Key quantitative results (18× data efficiency claim)\n- Limitations\n- Whether this trains the retriever or the LLM (critical distinction for our research)\n\nBe thorough and specific. Return all findings in a structured format.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2124f8d-f8ef-46fe-84ee-db9317ef4de8",
  "isSidechain": false,
  "requestId": "req_011CbYH9fPmBXtfYbZy22kF4",
  "type": "assistant",
  "uuid": "3ea9a5f9-0938-4df7-8a24-ba18381283d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175iVYouCFsjzfAdbLAdSwh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 14616,
      "output_tokens": 1755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1755,
          "cache_read_input_tokens": 14616,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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

_source line 17 · 2026-05-30T06:28:17.015Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01EGDgJTbqJ6i3Z1DAYCuDoH`</summary>

```json
{
  "description": "Research LREM paper",
  "prompt": "Research the paper \"Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval Paradigm (LREM)\" by Jianting Tang et al. (arXiv 2025), arxiv URL: https://arxiv.org/abs/2510.14321\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF (https://arxiv.org/pdf/2510.14321)\n3. Search for any reviews or discussion about this paper\n\nFor each, extract:\n- What gap did they identify and HOW? (semantic gaps in complex queries)\n- What was the key insight others missed? (reasoning-augmented embeddings)\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify? (SFT + RL training pipeline)\n- Technical method details (how CoT reasoning is integrated into embedding generation, two-stage training)\n- Key quantitative results (deployment on Alibaba platform)\n- Limitations\n- The arxiv ID 2510.14321 suggests October 2025 posting - confirm the actual date\n\nBe thorough and specific. Return all findings in a structured format.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ea9a5f9-0938-4df7-8a24-ba18381283d8",
  "isSidechain": false,
  "requestId": "req_011CbYH9fPmBXtfYbZy22kF4",
  "type": "assistant",
  "uuid": "eed77995-32e7-41a2-8e74-cbbc95c85183",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0175iVYouCFsjzfAdbLAdSwh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1180,
      "cache_read_input_tokens": 14616,
      "output_tokens": 1755,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1180,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1755,
          "cache_read_input_tokens": 14616,
          "cache_creation_input_tokens": 1180,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1180
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
  "leafUuid": "eed77995-32e7-41a2-8e74-cbbc95c85183",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze papers for AAAI 2026 reasoning-intensive retrieval",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Tool result

_source line 20 · 2026-05-30T06:31:43.819Z_

<details><summary>↩ Tool result · `toolu_01EGDgJTbqJ6i3Z1DAYCuDoH`</summary>

```text
Now I have comprehensive information. Here is the full structured analysis:

---

## LREM: "Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval Paradigm"

**arXiv ID:** 2510.14321
**Authors:** Jianting Tang, Dongshuai Li, Tao Wen, Fuyu Lv, Dan Ou, Linli Xu (Taobao & Tmall Group, Alibaba)
**Submission Date:** v1 posted October 16, 2025; v2 (current) posted October 17, 2025. PDF metadata says October 20, 2025. The ID prefix "2510" confirms October 2025.
**Length:** 12 pages
**Categories:** cs.IR (Information Retrieval)

---

### 1. GAP IDENTIFIED AND HOW

**The gap:** Current dense retrieval models (including LLM-based ones) use a "direct-embedding" paradigm -- they encode queries in a single forward pass via contrastive learning. This causes them to capture **statistical co-occurrence patterns** rather than deep semantics, biasing toward **shallow lexical and semantic matching**. They fail systematically on "difficult queries" that have significant lexical disparity from target items.

**How they identified it:** They use a concrete motivating example from e-commerce: the query "Drinks That Are More Invigorating Than Tea" returns tea-based drinks instead of Coffee or Red Bull, because the model matches on surface-level "tea" co-occurrence rather than reasoning about the comparative/alternative intent. They categorize four types of hard queries where this fails: Q&A queries, Alternative queries, Negative queries, and Knowledge-intensive queries.

**Key observation:** LLMs already possess the reasoning capability needed to bridge these semantic gaps (via CoT), but this capability is "largely underexplored" in the embedding/retrieval context. Prior LLM-based embedding models (RepLLaMA, Llama2Vec, NV-Embed, ICL-Embedder) all still follow the direct-embedding paradigm.

---

### 2. KEY INSIGHT OTHERS MISSED

The critical insight is that **reasoning and embedding can be unified into a single process** rather than treated as separate pipeline stages. Instead of first rewriting a query (traditional query rewriting) and then embedding it, LREM generates chain-of-thought reasoning tokens that are directly consumed by the same model to produce the final embedding vector. The CoT acts as a **"semantic bridge"** between the surface-form query and the target items.

This differs from:
- **Query rewriting** approaches (which rewrite the query text, then feed it to a separate embedding model -- a disconnected pipeline)
- **Prior reasoning retrieval** work like RaDeR, ReasonIR, TongSearch-QR, DeepRetrieval (which either use reasoning for reranking or treat reasoning and embedding as separate modules)

LREM "seamlessly integrates reasoning and embedding into a unified process" within a single model.

---

### 3. PROBLEM FORMULATION

They formulate retrieval as a two-step inference process within one model:

1. **Reasoning step:** Given query q_i, generate CoT c_i = f^gen_theta(q_i) = (t_1, t_2, ..., t_l_i)
2. **Embedding step:** Produce query embedding from the concatenated [q_i; c_i] sequence: q_i = f^emb_theta([q_i; c_i])

Item embeddings are computed directly (no reasoning needed): d_j = f_theta(d_j)

This is fundamentally different from prior formulations where embedding = single forward pass on the raw query text.

---

### 4. EXISTING TECHNIQUES ADAPTED/COMBINED

LREM combines several existing techniques in a novel configuration:

- **InfoNCE contrastive loss** (standard in dense retrieval) -- used for embedding training in both stages
- **SFT on CoT data** (from reasoning LLM literature) -- used to bootstrap reasoning capability
- **GRPO (Group Relative Policy Optimization)** -- a critic-free RL algorithm from the DeepSeek-R1 lineage, adapted here with a custom retrieval-specific reward function
- **Special token architecture** -- `&lt;think>`, `&lt;/think>`, and `&lt;emb>` tokens (inspired by reasoning models like DeepSeek-R1's thinking format)
- **Teacher model distillation** -- Qwen3-30B-A3B-Instruct generates initial CoT training data

The novelty is not any single component but the integration: using RL with a retrieval accuracy reward to refine CoT that directly feeds into embedding generation.

---

### 5. TECHNICAL METHOD DETAILS

#### Base Model
**Qwen2.5-3B-Instruct** with three new special tokens: `&lt;think>`, `&lt;/think>`, `&lt;emb>`

#### Data Construction Pipeline (4 steps)
1. **CoT Generation:** Qwen3-30B-A3B-Instruct generates unconstrained reasoning for queries, then keywords are extracted (removing duplicates, query-overlapping terms, and prohibited keywords)
2. **Item Filtering via Differential Retrieval:**
   - Set A = top-k items retrieved with original query
   - Set B = top-k items retrieved with [query + CoT keywords]
   - Keep only items in B \ A (items found ONLY when CoT is added)
   - If the difference set is empty, discard the query (CoT adds no value)
3. **Relevance Verification:** TaoSR1 (a 42B MoE LLM trained with RL) judges item relevance; only relevant items retained
4. **Final dataset:** 75.06 million Query-CoT-Item triplets; 4 million reserved for RL

**Critical design choice:** CoT is constrained to **keywords only** (max 16 tokens), not natural language reasoning -- this is for latency efficiency in production.

#### Stage 1: Cold Start Training

**SFT Loss** (teaches reasoning format):
L_SFT = -1/N * sum over sequences of log P(t_j | q_i, t_&lt;j)

**InfoNCE Loss** (teaches embedding quality):
- Query embedding = last hidden state of `&lt;emb>` token after processing `[q_i &lt;think> c_i &lt;/think> &lt;emb>]`
- Item embedding = last hidden state of `&lt;emb>` token appended to product title
- Cosine similarity with temperature tau

**Combined:** L = 0.1 * L_SFT + 1.0 * L_InfoNCE

**Hyperparameters:** Per-GPU batch 128, LR 1e-5, cosine schedule, warmup ratio 0.03, 1 epoch, 128 GPUs

#### Stage 2: Reinforcement Learning

**GRPO-based optimization:** For each query, G=8 CoTs are sampled, and advantages are computed relative to the group mean.

**Three reward dimensions:**
- **Format reward** (beta_1=0.5): Binary -- does output match `&lt;think>...&lt;/think>&lt;emb>` format?
- **Length reward** (beta_2=0.2): Binary -- is CoT <= 16 tokens?
- **Retrieval accuracy reward** (beta_3=1.0): r_accuracy = 1 - log(rank(d_i)) / log(N), where rank is computed from cosine similarities within the batch

**Combined RL loss:** L = 1.0 * L_GRPO + 0.1 * L_InfoNCE

**Hyperparameters:** Per-GPU batch 256, LR 1e-6, cosine schedule, warmup 0.03, 1 epoch, G=8 samples per query

---

### 6. KEY QUANTITATIVE RESULTS

#### Test Setup
- 7,209 queries across 4 hard categories (Q&A, Alternative, Negative, Knowledge-intensive)
- Candidate pool: 76.63 million items
- Metrics: HitRate@6000, Precision@100

#### Main Offline Results (vs. baselines)

| Method | HR@6000 | P@100 |
|--------|---------|-------|
| BERT | 24.96% | 51.09% |
| Query-Rewrite | 28.24% | 58.37% |
| Qwen2.5 (Uni-Attn Last) | 32.52% | 65.38% |
| Qwen2.5 (Bi-Attn Last) | 32.89% | 65.66% |
| **LREM (Cold Start only)** | 32.45% | 64.83% |
| **LREM (Cold Start + RL)** | **34.78%** | **68.22%** |

**LREM vs. strongest baseline (Bi-Attn Last):** +5.75% HR@6000, +3.90% P@100

#### Per-Category Gains (LREM vs. best baseline)
- Q&A: +19.20% HR@6000, +4.19% P@100
- Alternative: +5.81% HR@6000, +9.01% P@100
- Negative: +4.18% HR@6000, +3.76% P@100
- Knowledge: +1.60% HR@6000, -2.74% P@100 (slight precision drop on knowledge queries)

#### RL Contribution
- Cold Start alone: 32.45% HR / 64.83% P@100
- After RL: 34.78% HR / 68.22% P@100
- RL adds: +7.18% HR@6000, +5.23% P@100

#### Ablation on CoT Content
- Full LREM: 34.78% HR / 68.22% P@100
- Empty-CoT: 31.59% HR / 64.25% P@100 (drop of -9.17% HR)
- Random-CoT: 30.16% HR / 62.32% P@100 (drop of -13.03% HR -- worse than empty, showing bad reasoning hurts)
- Query-CoT (repeat query as CoT): 32.54% HR / 65.63% P@100

#### CoT Length Analysis
- l=16 (default): baseline
- l=32: notable improvement
- l=48, l=64: declining -- longer CoTs introduce noise/divergent reasoning

#### Online A/B Test Results (GSB metric, 2000 live queries)
- Q&A: +7.39%
- Alternative: +7.27%
- Negative: **+15.7%**
- Knowledge: +4.94%
- **Latency:** Average retrieval time increased from 15ms to 50ms (+35ms)

**Deployment:** Live on Taobao (China's largest e-commerce platform) since August 2025.

---

### 7. LIMITATIONS

**Acknowledged by authors:**
1. **Latency overhead:** 35ms additional processing time (15ms to 50ms), a 3.3x increase
2. **Keyword-only CoT:** Reasoning is constrained to keyword format rather than full natural language CoT, sacrificing reasoning expressiveness for production speed
3. **Teacher model dependency:** Quality of training data depends on Qwen3-30B teacher model's reasoning quality
4. **Unidirectional attention:** Must use causal (unidirectional) attention because the model generates CoT autoregressively before embedding, blocking use of potentially more effective bidirectional attention for the embedding step

**Identified by external analysis (EmergentMind):**
5. **Computational overhead from RL loops** creates concerns for real-time/high-throughput settings
6. **Domain adaptation** remains an open question -- unclear how well this transfers beyond e-commerce
7. **Dynamic gating** (selectively invoking reasoning only for hard queries) is suggested as a needed future improvement

**Additional observations:**
8. Knowledge-intensive queries showed a slight precision drop (-2.74% P@100), suggesting the approach doesn't uniformly improve all query types
9. The evaluation is entirely within e-commerce search on Taobao -- no evaluation on standard academic benchmarks (BEIR, MTEB, BRIGHT), making cross-domain comparison difficult

---

### 8. POSITIONING IN THE BROADER LANDSCAPE

LREM is part of a 2025 wave of reasoning-augmented embedding models:

- **Search-R3** (arxiv 2510.07048, also Oct 2025): Unifies reasoning and embedding in LLMs with SFT + RL; similar philosophy but different architecture
- **RITE** (arxiv 2509.00276, Sep 2025): Reasoning-Infused Text Embedding -- performs reasoning in token space before embedding extraction; zero-shot focus
- **RaDeR** (EMNLP 2025): Reasoning-aware Dense Retrieval; reasoning for reranking rather than embedding
- **ReasonEmbed**: Achieves 38.1 nDCG@10 on BRIGHT benchmark via synthetic reasoning data
- **TaoSearchEmb** (2025): Follow-up from the same Alibaba team -- a multi-objective RL framework for dense retrieval in Taobao Search, suggesting continued iteration on this line of work

LREM distinguishes itself as the **first commercially deployed** reasoning embedding model at scale, and the only one with production A/B test results from a major platform.

---

### 9. DATE CONFIRMATION

The arxiv ID 2510.14321 confirms an **October 2025** posting. Specifically:
- v1 submitted: October 16, 2025
- v2 (current): October 17, 2025
- PDF creation date: October 20, 2025

This is consistent with the "2510" prefix (YYMM format: 25 = 2025, 10 = October).

agentId: a29f068acfd6317d7 (use SendMessage with to: 'a29f068acfd6317d7' to continue this agent)
&lt;usage>total_tokens: 24700
tool_uses: 14
duration_ms: 206799&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eed77995-32e7-41a2-8e74-cbbc95c85183",
  "isSidechain": false,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "type": "user",
  "uuid": "35791e19-cfdf-456f-96b1-f86ad39e4c6b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval Paradigm (LREM)\" by Jianting Tang et al. (arXiv 2025), arxiv URL: https://arxiv.org/abs/2510.14321\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF (https://arxiv.org/pdf/2510.14321)\n3. Search for any reviews or discussion about this paper\n\nFor each, extract:\n- What gap did they identify and HOW? (semantic gaps in complex queries)\n- What was the key insight others missed? (reasoning-augmented embeddings)\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify? (SFT + RL training pipeline)\n- Technical method details (how CoT reasoning is integrated into embedding generation, two-stage training)\n- Key quantitative results (deployment on Alibaba platform)\n- Limitations\n- The arxiv ID 2510.14321 suggests October 2025 posting - confirm the actual date\n\nBe thorough and specific. Return all findings in a structured format.",
    "agentId": "a29f068acfd6317d7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Here is the full structured analysis:\n\n---\n\n## LREM: \"Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval Paradigm\"\n\n**arXiv ID:** 2510.14321\n**Authors:** Jianting Tang, Dongshuai Li, Tao Wen, Fuyu Lv, Dan Ou, Linli Xu (Taobao & Tmall Group, Alibaba)\n**Submission Date:** v1 posted October 16, 2025; v2 (current) posted October 17, 2025. PDF metadata says October 20, 2025. The ID prefix \"2510\" confirms October 2025.\n**Length:** 12 pages\n**Categories:** cs.IR (Information Retrieval)\n\n---\n\n### 1. GAP IDENTIFIED AND HOW\n\n**The gap:** Current dense retrieval models (including LLM-based ones) use a \"direct-embedding\" paradigm -- they encode queries in a single forward pass via contrastive learning. This causes them to capture **statistical co-occurrence patterns** rather than deep semantics, biasing toward **shallow lexical and semantic matching**. They fail systematically on \"difficult queries\" that have significant lexical disparity from target items.\n\n**How they identified it:** They use a concrete motivating example from e-commerce: the query \"Drinks That Are More Invigorating Than Tea\" returns tea-based drinks instead of Coffee or Red Bull, because the model matches on surface-level \"tea\" co-occurrence rather than reasoning about the comparative/alternative intent. They categorize four types of hard queries where this fails: Q&A queries, Alternative queries, Negative queries, and Knowledge-intensive queries.\n\n**Key observation:** LLMs already possess the reasoning capability needed to bridge these semantic gaps (via CoT), but this capability is \"largely underexplored\" in the embedding/retrieval context. Prior LLM-based embedding models (RepLLaMA, Llama2Vec, NV-Embed, ICL-Embedder) all still follow the direct-embedding paradigm.\n\n---\n\n### 2. KEY INSIGHT OTHERS MISSED\n\nThe critical insight is that **reasoning and embedding can be unified into a single process** rather than treated as separate pipeline stages. Instead of first rewriting a query (traditional query rewriting) and then embedding it, LREM generates chain-of-thought reasoning tokens that are directly consumed by the same model to produce the final embedding vector. The CoT acts as a **\"semantic bridge\"** between the surface-form query and the target items.\n\nThis differs from:\n- **Query rewriting** approaches (which rewrite the query text, then feed it to a separate embedding model -- a disconnected pipeline)\n- **Prior reasoning retrieval** work like RaDeR, ReasonIR, TongSearch-QR, DeepRetrieval (which either use reasoning for reranking or treat reasoning and embedding as separate modules)\n\nLREM \"seamlessly integrates reasoning and embedding into a unified process\" within a single model.\n\n---\n\n### 3. PROBLEM FORMULATION\n\nThey formulate retrieval as a two-step inference process within one model:\n\n1. **Reasoning step:** Given query q_i, generate CoT c_i = f^gen_theta(q_i) = (t_1, t_2, ..., t_l_i)\n2. **Embedding step:** Produce query embedding from the concatenated [q_i; c_i] sequence: q_i = f^emb_theta([q_i; c_i])\n\nItem embeddings are computed directly (no reasoning needed): d_j = f_theta(d_j)\n\nThis is fundamentally different from prior formulations where embedding = single forward pass on the raw query text.\n\n---\n\n### 4. EXISTING TECHNIQUES ADAPTED/COMBINED\n\nLREM combines several existing techniques in a novel configuration:\n\n- **InfoNCE contrastive loss** (standard in dense retrieval) -- used for embedding training in both stages\n- **SFT on CoT data** (from reasoning LLM literature) -- used to bootstrap reasoning capability\n- **GRPO (Group Relative Policy Optimization)** -- a critic-free RL algorithm from the DeepSeek-R1 lineage, adapted here with a custom retrieval-specific reward function\n- **Special token architecture** -- `&lt;think>`, `&lt;/think>`, and `&lt;emb>` tokens (inspired by reasoning models like DeepSeek-R1's thinking format)\n- **Teacher model distillation** -- Qwen3-30B-A3B-Instruct generates initial CoT training data\n\nThe novelty is not any single component but the integration: using RL with a retrieval accuracy reward to refine CoT that directly feeds into embedding generation.\n\n---\n\n### 5. TECHNICAL METHOD DETAILS\n\n#### Base Model\n**Qwen2.5-3B-Instruct** with three new special tokens: `&lt;think>`, `&lt;/think>`, `&lt;emb>`\n\n#### Data Construction Pipeline (4 steps)\n1. **CoT Generation:** Qwen3-30B-A3B-Instruct generates unconstrained reasoning for queries, then keywords are extracted (removing duplicates, query-overlapping terms, and prohibited keywords)\n2. **Item Filtering via Differential Retrieval:**\n   - Set A = top-k items retrieved with original query\n   - Set B = top-k items retrieved with [query + CoT keywords]\n   - Keep only items in B \\ A (items found ONLY when CoT is added)\n   - If the difference set is empty, discard the query (CoT adds no value)\n3. **Relevance Verification:** TaoSR1 (a 42B MoE LLM trained with RL) judges item relevance; only relevant items retained\n4. **Final dataset:** 75.06 million Query-CoT-Item triplets; 4 million reserved for RL\n\n**Critical design choice:** CoT is constrained to **keywords only** (max 16 tokens), not natural language reasoning -- this is for latency efficiency in production.\n\n#### Stage 1: Cold Start Training\n\n**SFT Loss** (teaches reasoning format):\nL_SFT = -1/N * sum over sequences of log P(t_j | q_i, t_&lt;j)\n\n**InfoNCE Loss** (teaches embedding quality):\n- Query embedding = last hidden state of `&lt;emb>` token after processing `[q_i &lt;think> c_i &lt;/think> &lt;emb>]`\n- Item embedding = last hidden state of `&lt;emb>` token appended to product title\n- Cosine similarity with temperature tau\n\n**Combined:** L = 0.1 * L_SFT + 1.0 * L_InfoNCE\n\n**Hyperparameters:** Per-GPU batch 128, LR 1e-5, cosine schedule, warmup ratio 0.03, 1 epoch, 128 GPUs\n\n#### Stage 2: Reinforcement Learning\n\n**GRPO-based optimization:** For each query, G=8 CoTs are sampled, and advantages are computed relative to the group mean.\n\n**Three reward dimensions:**\n- **Format reward** (beta_1=0.5): Binary -- does output match `&lt;think>...&lt;/think>&lt;emb>` format?\n- **Length reward** (beta_2=0.2): Binary -- is CoT <= 16 tokens?\n- **Retrieval accuracy reward** (beta_3=1.0): r_accuracy = 1 - log(rank(d_i)) / log(N), where rank is computed from cosine similarities within the batch\n\n**Combined RL loss:** L = 1.0 * L_GRPO + 0.1 * L_InfoNCE\n\n**Hyperparameters:** Per-GPU batch 256, LR 1e-6, cosine schedule, warmup 0.03, 1 epoch, G=8 samples per query\n\n---\n\n### 6. KEY QUANTITATIVE RESULTS\n\n#### Test Setup\n- 7,209 queries across 4 hard categories (Q&A, Alternative, Negative, Knowledge-intensive)\n- Candidate pool: 76.63 million items\n- Metrics: HitRate@6000, Precision@100\n\n#### Main Offline Results (vs. baselines)\n\n| Method | HR@6000 | P@100 |\n|--------|---------|-------|\n| BERT | 24.96% | 51.09% |\n| Query-Rewrite | 28.24% | 58.37% |\n| Qwen2.5 (Uni-Attn Last) | 32.52% | 65.38% |\n| Qwen2.5 (Bi-Attn Last) | 32.89% | 65.66% |\n| **LREM (Cold Start only)** | 32.45% | 64.83% |\n| **LREM (Cold Start + RL)** | **34.78%** | **68.22%** |\n\n**LREM vs. strongest baseline (Bi-Attn Last):** +5.75% HR@6000, +3.90% P@100\n\n#### Per-Category Gains (LREM vs. best baseline)\n- Q&A: +19.20% HR@6000, +4.19% P@100\n- Alternative: +5.81% HR@6000, +9.01% P@100\n- Negative: +4.18% HR@6000, +3.76% P@100\n- Knowledge: +1.60% HR@6000, -2.74% P@100 (slight precision drop on knowledge queries)\n\n#### RL Contribution\n- Cold Start alone: 32.45% HR / 64.83% P@100\n- After RL: 34.78% HR / 68.22% P@100\n- RL adds: +7.18% HR@6000, +5.23% P@100\n\n#### Ablation on CoT Content\n- Full LREM: 34.78% HR / 68.22% P@100\n- Empty-CoT: 31.59% HR / 64.25% P@100 (drop of -9.17% HR)\n- Random-CoT: 30.16% HR / 62.32% P@100 (drop of -13.03% HR -- worse than empty, showing bad reasoning hurts)\n- Query-CoT (repeat query as CoT): 32.54% HR / 65.63% P@100\n\n#### CoT Length Analysis\n- l=16 (default): baseline\n- l=32: notable improvement\n- l=48, l=64: declining -- longer CoTs introduce noise/divergent reasoning\n\n#### Online A/B Test Results (GSB metric, 2000 live queries)\n- Q&A: +7.39%\n- Alternative: +7.27%\n- Negative: **+15.7%**\n- Knowledge: +4.94%\n- **Latency:** Average retrieval time increased from 15ms to 50ms (+35ms)\n\n**Deployment:** Live on Taobao (China's largest e-commerce platform) since August 2025.\n\n---\n\n### 7. LIMITATIONS\n\n**Acknowledged by authors:**\n1. **Latency overhead:** 35ms additional processing time (15ms to 50ms), a 3.3x increase\n2. **Keyword-only CoT:** Reasoning is constrained to keyword format rather than full natural language CoT, sacrificing reasoning expressiveness for production speed\n3. **Teacher model dependency:** Quality of training data depends on Qwen3-30B teacher model's reasoning quality\n4. **Unidirectional attention:** Must use causal (unidirectional) attention because the model generates CoT autoregressively before embedding, blocking use of potentially more effective bidirectional attention for the embedding step\n\n**Identified by external analysis (EmergentMind):**\n5. **Computational overhead from RL loops** creates concerns for real-time/high-throughput settings\n6. **Domain adaptation** remains an open question -- unclear how well this transfers beyond e-commerce\n7. **Dynamic gating** (selectively invoking reasoning only for hard queries) is suggested as a needed future improvement\n\n**Additional observations:**\n8. Knowledge-intensive queries showed a slight precision drop (-2.74% P@100), suggesting the approach doesn't uniformly improve all query types\n9. The evaluation is entirely within e-commerce search on Taobao -- no evaluation on standard academic benchmarks (BEIR, MTEB, BRIGHT), making cross-domain comparison difficult\n\n---\n\n### 8. POSITIONING IN THE BROADER LANDSCAPE\n\nLREM is part of a 2025 wave of reasoning-augmented embedding models:\n\n- **Search-R3** (arxiv 2510.07048, also Oct 2025): Unifies reasoning and embedding in LLMs with SFT + RL; similar philosophy but different architecture\n- **RITE** (arxiv 2509.00276, Sep 2025): Reasoning-Infused Text Embedding -- performs reasoning in token space before embedding extraction; zero-shot focus\n- **RaDeR** (EMNLP 2025): Reasoning-aware Dense Retrieval; reasoning for reranking rather than embedding\n- **ReasonEmbed**: Achieves 38.1 nDCG@10 on BRIGHT benchmark via synthetic reasoning data\n- **TaoSearchEmb** (2025): Follow-up from the same Alibaba team -- a multi-objective RL framework for dense retrieval in Taobao Search, suggesting continued iteration on this line of work\n\nLREM distinguishes itself as the **first commercially deployed** reasoning embedding model at scale, and the only one with production A/B test results from a major platform.\n\n---\n\n### 9. DATE CONFIRMATION\n\nThe arxiv ID 2510.14321 confirms an **October 2025** posting. Specifically:\n- v1 submitted: October 16, 2025\n- v2 (current): October 17, 2025\n- PDF creation date: October 20, 2025\n\nThis is consistent with the \"2510\" prefix (YYMM format: 25 = 2025, 10 = October)."
      }
    ],
    "totalDurationMs": 206799,
    "totalTokens": 24700,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1395,
      "cache_read_input_tokens": 19958,
      "output_tokens": 3346,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1395
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3346,
          "cache_read_input_tokens": 19958,
          "cache_creation_input_tokens": 1395,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1395,
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
  "sourceToolAssistantUUID": "eed77995-32e7-41a2-8e74-cbbc95c85183",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T06:31:55.213Z_

<details><summary>↩ Tool result · `toolu_01KQMvHoLi1mUjLqstzybp7K`</summary>

````text
Excellent. Now I have comprehensive information. Let me compile the complete structured analysis.

---

## SCARLet: Comprehensive Research Analysis

**Full Title:** Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models
**Authors:** Yilong Xu, Jinhua Gao, Xiaoming Yu, Yuanhai Xue, Baolong Bi, Huawei Shen, Xueqi Cheng
**Venue:** EMNLP 2025 Main Conference (Long paper), pages 629-648, Suzhou, China
**ACL Anthology ID:** 2025.emnlp-main.33
**arXiv:** 2504.00573

---

### 1. WHAT GAP DID THEY IDENTIFY AND HOW?

The authors identified **two overlooked factors** in utility-based retriever training for RALMs:

**Gap A -- Multi-task Generalization Failure:** Prior methods (AAR, RePlug, etc.) use a "pooling strategy" that mixes training data from different tasks, each with different contexts. The authors argued this introduces **semantic interference** -- the retriever learns to capture semantic relevance signals from the varied contexts rather than task-specific utility features. The key observation: when training data from multiple tasks have different contexts, a retriever cannot disentangle whether a passage is "good" because it is semantically similar to the query or because it actually helps the downstream task. This conflation is especially damaging for weaker retrievers.

**Gap B -- Inter-passage Interaction Neglect:** Existing approaches evaluate passages independently (one at a time), completely missing synergistic effects. The authors highlighted multi-hop QA as the clearest illustration: a bridge passage connecting two entities has zero utility in isolation but becomes essential when combined with the passage containing the first-hop answer. No prior utility-based retriever captured these inter-passage dependencies.

**How they identified these gaps:** Through systematic analysis of why existing utility-based retrievers (AAR, RePlug, ARES) underperform expectations. They categorized existing RALM optimization into three streams (overall, generator-only, retriever-only) and identified that retriever-only approaches either (a) lacked passage-level feedback entirely, (b) evaluated passages independently ignoring interactions, or (c) relied on LLM self-reflection prone to hallucination.

---

### 2. WHAT WAS THE KEY INSIGHT OTHERS MISSED?

The central insight was **"single-variable control"**: to learn utility rather than relevance, you must eliminate contextual variation as a confound. If every task's training data is synthesized from the *same* shared context, then the only signal differentiating positive from negative passages is their actual contribution to the downstream task -- not their semantic similarity to a particular query.

Others missed that the **pooling strategy itself was the source of semantic bias**. Prior work (Asai et al., 2023; ARES) noticed the multi-task nature of retriever training but ignored the training biases introduced by contextual differences across tasks.

A second missed insight: **LIME-style attribution needs modification for utility estimation**. The authors deliberately removed the semantic distance weighting term from LIME because "utility features cannot be directly measured by semantic relevance." Standard LIME weights perturbations by proximity to the original input in feature space, but for utility estimation, a semantically distant perturbation (removing a seemingly unrelated passage) can be just as informative.

---

### 3. HOW DID THEY FORMULATE THE PROBLEM DIFFERENTLY? (Utility vs. Relevance)

**Relevance** (standard formulation): `score(q, d) = Enc(q) . Enc(d)` -- dot-product similarity between query and passage embeddings. This measures semantic closeness.

**Utility** (their formulation): The valid gain a passage contributes to downstream generation. Formally, given a generator LM_theta, instruction I, input x, and context D (set of passages), the output is `y_hat = LM_theta(I + x + D)`. A passage's utility is measured by the **logit fluctuation** when that passage is removed from D:

```
z_i = sum_t logit(y_t^(i))
```

where z_i quantifies the change in ground-truth token logits under perturbation vector v_i. This is fundamentally different from relevance because:
- A passage can be semantically relevant but useless (e.g., contains the right entities but wrong facts)
- A passage can be semantically distant but highly useful (e.g., a bridge entity in multi-hop reasoning)
- Utility depends on what OTHER passages are present (interaction effects)

The training loss is contrastive:
```
L = sum_x sum_{d+ in D+} sum_{d- in D-} l(score(x, d+), score(x, d-))
```
where positive/negative labels come from utility attribution, not relevance annotation.

---

### 4. WHAT EXISTING TECHNIQUE DID THEY ADAPT/COMBINE/SIMPLIFY?

They adapted **LIME (Local Interpretable Model-agnostic Explanations)** -- specifically the perturbation-based attribution component -- but with two critical modifications:

**Modification 1 -- Removed semantic distance weighting:** Standard LIME weights each perturbation sample by its distance from the original input in feature space. SCARLet removes this weighting because semantic distance does not correspond to utility distance.

**Modification 2 -- Ridge regression surrogate instead of linear model:** They fit a ridge regression model to map perturbation vectors to utility scores:
```
alpha_hat = argmin_{alpha in R^{k+1}} { sum(z_i - alpha^T v_i)^2 + lambda||alpha||^2 }
```
where v_i is a binary perturbation vector in {0,1}^k indicating passage inclusion/exclusion, and lambda is a regularization hyperparameter.

They also combined this with:
- **Wikidata entity expansion** (one-hop knowledge graph traversal) for shared context construction
- **1D clustering** to dynamically partition passages into positive/negative training samples based on utility scores
- **GPT-4o** as a synthetic data generator for multi-task training data
- **SpaCy** for entity extraction from seed instances

---

### 5. TECHNICAL METHOD DETAILS

#### 5A. Shared Context Construction Pipeline

1. **Seed Data Collection:** Sample 1,000 instances per dataset from 6 in-domain tasks (NQ, HotpotQA, ELI5, FEVER, WoW, T-REx)
2. **Entity Extraction:** Use SpaCy to extract named entities from both inputs and ground-truth answers; discard instances without extractable entities
3. **Entity Expansion:** Query Wikidata for one-hop related entities to enhance diversity and strengthen relational connections
4. **Passage Retrieval:** Retrieve top-10 passages per entity from Wikipedia corpus (28,773,800 passages, 100-word segments from 2019-08-01 dump); aggregate into shared context
5. **Synthetic Data Generation:** Use GPT-4o-2024-11-20 (temperature=0.5) with task instructions, descriptions, examples, and shared context to generate input-output pairs for each task
6. **Quality Filtering:** LLM-based verification checking logical consistency and format correctness
7. **Noise Injection:** Synthesize semantically relevant but task-useless passages and add to shared context for robustness

#### 5B. Utility Attribution via Perturbation

- Sample n=64 perturbation vectors randomly (each passage removed with 50% probability)
- For each perturbation, run the generator and record summed logit values of ground-truth tokens
- Fit ridge regression surrogate model mapping perturbation vectors to utility scores
- The resulting coefficients alpha are the passage-level utility estimates
- Use 1D clustering to partition passages into positive set D+ and negative set D-

#### 5C. Training

- Base retrievers: Contriever and BGE (tested both)
- Generators: LLaMA-3-8B-Instruct and Qwen2.5-3B-Instruct
- Learning rate: 6e-5
- Training epochs: 1
- Top-k retrieval: 3 passages per query
- Contrastive loss on utility-labeled passage pairs

---

### 6. KEY QUANTITATIVE RESULTS

#### Main Results (LLaMA-3-8B-Instruct generator)

**In-domain (6 datasets):**

| Dataset | Contriever | BGE | AAR | RePlug | SCARLet_BGE |
|---------|-----------|-----|-----|--------|------------|
| NQ | 43.8 | 47.5 | 44.9 | 43.3 | **49.2** |
| HotpotQA | 36.7 | 41.6 | 39.9 | 38.9 | **47.0** |
| ELI5 | 14.5 | 15.2 | 15.0 | 13.8 | **16.3** |
| FEVER | 78.5 | 83.5 | 77.2 | 80.0 | **81.3** |
| WoW | 8.6 | 8.7 | 8.3 | 9.4 | **12.2** |
| T-REx | 33.6 | 36.4 | 34.4 | 33.1 | **37.0** |

SCARLet_BGE achieved best performance on all 6 in-domain datasets. Notable: +5.4 points on HotpotQA (multi-hop), +3.5 on WoW (dialogue).

**Out-of-domain (4 datasets):** Also showed improvements, particularly on zs-RE and SciFact.

#### Utility Attribution Quality (GTI Benchmark)

| Method | HotpotQA nDCG@1 | NQ nDCG@1 | MSMARCO nDCG@1 |
|--------|-----------------|-----------|-----------------|
| Attention-based | 31.54 | 29.14 | 29.92 |
| Gradient-based | 49.90 | 50.58 | 59.09 |
| LLM-based | 76.34 | 28.35 | 31.88 |
| **Perturbation (theirs)** | **93.28** | **78.16** | **91.65** |

Perturbation-based attribution outperformed all alternatives by >20 percentage points on nDCG@5 across all three datasets.

#### Reasoning-Intensive Retrieval (BRIGHT Benchmark)

Gains on StackExchange (+2.8 for Contriever, +1.3 for BGE) and Theorem-based tasks (+1.8, +1.1), but **declines on coding tasks** (-0.4, -1.6).

#### Multi-task (X^2-Retrieval)

Strong gains on AMB (+0.7/+1.0), WQA (+5.1/+2.1), GAT (-1.6/+0.4), but significant **declines on code-related tasks** LSO (-7.1/-2.6) and CSP (-11.9/-3.3).

---

### 7. LIMITATIONS

The authors explicitly acknowledge:

1. **Dataset scope is narrow:** Only covers several classic downstream datasets; broader evaluation needed
2. **Code domain failure:** "Noticeable decline in retrieval performance in the code domain" -- the synthesized shared context from Wikipedia does not transfer to code tasks
3. **Scale not tested:** Does not evaluate larger-scale retrievers or generators beyond 8B parameters
4. **Strong synthesizer required:** The framework requires GPT-4o-level reasoning capability for data synthesis; GPT-4o-mini failed to produce adequate training data
5. **Corpus structure ignored:** Future work needs to integrate corpus-level structural information
6. **Computational cost of perturbation:** Running 64 perturbation forward passes per training instance through the generator is expensive (though they don't discuss this explicitly as a limitation)

---

### OPENREVIEW REVIEWS

The paper's OpenReview page was located at `https://openreview.net/forum?id=VNam6izoMG`, but the reviews are **not publicly accessible**. EMNLP 2025 does not appear to make peer reviews publicly visible on OpenReview. No reviewer scores, strengths/weaknesses, or discussion content could be retrieved.

---

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2504.00573)
- [arXiv HTML Full Paper](https://arxiv.org/html/2504.00573v2)
- [ACL Anthology](https://aclanthology.org/2025.emnlp-main.33/)
- [OpenReview Forum](https://openreview.net/forum?id=VNam6izoMG)
- [Yilong Xu OpenReview Profile](https://openreview.net/profile?id=%7EYilong_Xu2)
- [EMNLP 2025 Accepted Papers](https://2025.emnlp.org/program/main_papers/)

agentId: a2d93bfe2d78db8ef (use SendMessage with to: 'a2d93bfe2d78db8ef' to continue this agent)
&lt;usage>total_tokens: 25824
tool_uses: 18
duration_ms: 234048&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "cbdc5c65-35d7-4b33-a85a-1b02a0aaad4d",
  "isSidechain": false,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "type": "user",
  "uuid": "c524adb5-501f-4a04-bddf-0e0f3a15e419",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"SCARLet: Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models\" by Yilong Xu et al. (EMNLP 2025 Main), arxiv URL: https://arxiv.org/abs/2504.00573\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF (https://arxiv.org/pdf/2504.00573)\n3. Search for OpenReview reviews if available\n\nFor each, extract:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently? (especially the utility vs relevance distinction)\n- What existing technique did they adapt/combine/simplify? (perturbation attribution details)\n- Technical method details (shared context attribution, how they estimate utility)\n- Key quantitative results\n- Limitations\n\nBe thorough and specific. Return all findings in a structured format.",
    "agentId": "a2d93bfe2d78db8ef",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent. Now I have comprehensive information. Let me compile the complete structured analysis.\n\n---\n\n## SCARLet: Comprehensive Research Analysis\n\n**Full Title:** Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models\n**Authors:** Yilong Xu, Jinhua Gao, Xiaoming Yu, Yuanhai Xue, Baolong Bi, Huawei Shen, Xueqi Cheng\n**Venue:** EMNLP 2025 Main Conference (Long paper), pages 629-648, Suzhou, China\n**ACL Anthology ID:** 2025.emnlp-main.33\n**arXiv:** 2504.00573\n\n---\n\n### 1. WHAT GAP DID THEY IDENTIFY AND HOW?\n\nThe authors identified **two overlooked factors** in utility-based retriever training for RALMs:\n\n**Gap A -- Multi-task Generalization Failure:** Prior methods (AAR, RePlug, etc.) use a \"pooling strategy\" that mixes training data from different tasks, each with different contexts. The authors argued this introduces **semantic interference** -- the retriever learns to capture semantic relevance signals from the varied contexts rather than task-specific utility features. The key observation: when training data from multiple tasks have different contexts, a retriever cannot disentangle whether a passage is \"good\" because it is semantically similar to the query or because it actually helps the downstream task. This conflation is especially damaging for weaker retrievers.\n\n**Gap B -- Inter-passage Interaction Neglect:** Existing approaches evaluate passages independently (one at a time), completely missing synergistic effects. The authors highlighted multi-hop QA as the clearest illustration: a bridge passage connecting two entities has zero utility in isolation but becomes essential when combined with the passage containing the first-hop answer. No prior utility-based retriever captured these inter-passage dependencies.\n\n**How they identified these gaps:** Through systematic analysis of why existing utility-based retrievers (AAR, RePlug, ARES) underperform expectations. They categorized existing RALM optimization into three streams (overall, generator-only, retriever-only) and identified that retriever-only approaches either (a) lacked passage-level feedback entirely, (b) evaluated passages independently ignoring interactions, or (c) relied on LLM self-reflection prone to hallucination.\n\n---\n\n### 2. WHAT WAS THE KEY INSIGHT OTHERS MISSED?\n\nThe central insight was **\"single-variable control\"**: to learn utility rather than relevance, you must eliminate contextual variation as a confound. If every task's training data is synthesized from the *same* shared context, then the only signal differentiating positive from negative passages is their actual contribution to the downstream task -- not their semantic similarity to a particular query.\n\nOthers missed that the **pooling strategy itself was the source of semantic bias**. Prior work (Asai et al., 2023; ARES) noticed the multi-task nature of retriever training but ignored the training biases introduced by contextual differences across tasks.\n\nA second missed insight: **LIME-style attribution needs modification for utility estimation**. The authors deliberately removed the semantic distance weighting term from LIME because \"utility features cannot be directly measured by semantic relevance.\" Standard LIME weights perturbations by proximity to the original input in feature space, but for utility estimation, a semantically distant perturbation (removing a seemingly unrelated passage) can be just as informative.\n\n---\n\n### 3. HOW DID THEY FORMULATE THE PROBLEM DIFFERENTLY? (Utility vs. Relevance)\n\n**Relevance** (standard formulation): `score(q, d) = Enc(q) . Enc(d)` -- dot-product similarity between query and passage embeddings. This measures semantic closeness.\n\n**Utility** (their formulation): The valid gain a passage contributes to downstream generation. Formally, given a generator LM_theta, instruction I, input x, and context D (set of passages), the output is `y_hat = LM_theta(I + x + D)`. A passage's utility is measured by the **logit fluctuation** when that passage is removed from D:\n\n```\nz_i = sum_t logit(y_t^(i))\n```\n\nwhere z_i quantifies the change in ground-truth token logits under perturbation vector v_i. This is fundamentally different from relevance because:\n- A passage can be semantically relevant but useless (e.g., contains the right entities but wrong facts)\n- A passage can be semantically distant but highly useful (e.g., a bridge entity in multi-hop reasoning)\n- Utility depends on what OTHER passages are present (interaction effects)\n\nThe training loss is contrastive:\n```\nL = sum_x sum_{d+ in D+} sum_{d- in D-} l(score(x, d+), score(x, d-))\n```\nwhere positive/negative labels come from utility attribution, not relevance annotation.\n\n---\n\n### 4. WHAT EXISTING TECHNIQUE DID THEY ADAPT/COMBINE/SIMPLIFY?\n\nThey adapted **LIME (Local Interpretable Model-agnostic Explanations)** -- specifically the perturbation-based attribution component -- but with two critical modifications:\n\n**Modification 1 -- Removed semantic distance weighting:** Standard LIME weights each perturbation sample by its distance from the original input in feature space. SCARLet removes this weighting because semantic distance does not correspond to utility distance.\n\n**Modification 2 -- Ridge regression surrogate instead of linear model:** They fit a ridge regression model to map perturbation vectors to utility scores:\n```\nalpha_hat = argmin_{alpha in R^{k+1}} { sum(z_i - alpha^T v_i)^2 + lambda||alpha||^2 }\n```\nwhere v_i is a binary perturbation vector in {0,1}^k indicating passage inclusion/exclusion, and lambda is a regularization hyperparameter.\n\nThey also combined this with:\n- **Wikidata entity expansion** (one-hop knowledge graph traversal) for shared context construction\n- **1D clustering** to dynamically partition passages into positive/negative training samples based on utility scores\n- **GPT-4o** as a synthetic data generator for multi-task training data\n- **SpaCy** for entity extraction from seed instances\n\n---\n\n### 5. TECHNICAL METHOD DETAILS\n\n#### 5A. Shared Context Construction Pipeline\n\n1. **Seed Data Collection:** Sample 1,000 instances per dataset from 6 in-domain tasks (NQ, HotpotQA, ELI5, FEVER, WoW, T-REx)\n2. **Entity Extraction:** Use SpaCy to extract named entities from both inputs and ground-truth answers; discard instances without extractable entities\n3. **Entity Expansion:** Query Wikidata for one-hop related entities to enhance diversity and strengthen relational connections\n4. **Passage Retrieval:** Retrieve top-10 passages per entity from Wikipedia corpus (28,773,800 passages, 100-word segments from 2019-08-01 dump); aggregate into shared context\n5. **Synthetic Data Generation:** Use GPT-4o-2024-11-20 (temperature=0.5) with task instructions, descriptions, examples, and shared context to generate input-output pairs for each task\n6. **Quality Filtering:** LLM-based verification checking logical consistency and format correctness\n7. **Noise Injection:** Synthesize semantically relevant but task-useless passages and add to shared context for robustness\n\n#### 5B. Utility Attribution via Perturbation\n\n- Sample n=64 perturbation vectors randomly (each passage removed with 50% probability)\n- For each perturbation, run the generator and record summed logit values of ground-truth tokens\n- Fit ridge regression surrogate model mapping perturbation vectors to utility scores\n- The resulting coefficients alpha are the passage-level utility estimates\n- Use 1D clustering to partition passages into positive set D+ and negative set D-\n\n#### 5C. Training\n\n- Base retrievers: Contriever and BGE (tested both)\n- Generators: LLaMA-3-8B-Instruct and Qwen2.5-3B-Instruct\n- Learning rate: 6e-5\n- Training epochs: 1\n- Top-k retrieval: 3 passages per query\n- Contrastive loss on utility-labeled passage pairs\n\n---\n\n### 6. KEY QUANTITATIVE RESULTS\n\n#### Main Results (LLaMA-3-8B-Instruct generator)\n\n**In-domain (6 datasets):**\n\n| Dataset | Contriever | BGE | AAR | RePlug | SCARLet_BGE |\n|---------|-----------|-----|-----|--------|------------|\n| NQ | 43.8 | 47.5 | 44.9 | 43.3 | **49.2** |\n| HotpotQA | 36.7 | 41.6 | 39.9 | 38.9 | **47.0** |\n| ELI5 | 14.5 | 15.2 | 15.0 | 13.8 | **16.3** |\n| FEVER | 78.5 | 83.5 | 77.2 | 80.0 | **81.3** |\n| WoW | 8.6 | 8.7 | 8.3 | 9.4 | **12.2** |\n| T-REx | 33.6 | 36.4 | 34.4 | 33.1 | **37.0** |\n\nSCARLet_BGE achieved best performance on all 6 in-domain datasets. Notable: +5.4 points on HotpotQA (multi-hop), +3.5 on WoW (dialogue).\n\n**Out-of-domain (4 datasets):** Also showed improvements, particularly on zs-RE and SciFact.\n\n#### Utility Attribution Quality (GTI Benchmark)\n\n| Method | HotpotQA nDCG@1 | NQ nDCG@1 | MSMARCO nDCG@1 |\n|--------|-----------------|-----------|-----------------|\n| Attention-based | 31.54 | 29.14 | 29.92 |\n| Gradient-based | 49.90 | 50.58 | 59.09 |\n| LLM-based | 76.34 | 28.35 | 31.88 |\n| **Perturbation (theirs)** | **93.28** | **78.16** | **91.65** |\n\nPerturbation-based attribution outperformed all alternatives by >20 percentage points on nDCG@5 across all three datasets.\n\n#### Reasoning-Intensive Retrieval (BRIGHT Benchmark)\n\nGains on StackExchange (+2.8 for Contriever, +1.3 for BGE) and Theorem-based tasks (+1.8, +1.1), but **declines on coding tasks** (-0.4, -1.6).\n\n#### Multi-task (X^2-Retrieval)\n\nStrong gains on AMB (+0.7/+1.0), WQA (+5.1/+2.1), GAT (-1.6/+0.4), but significant **declines on code-related tasks** LSO (-7.1/-2.6) and CSP (-11.9/-3.3).\n\n---\n\n### 7. LIMITATIONS\n\nThe authors explicitly acknowledge:\n\n1. **Dataset scope is narrow:** Only covers several classic downstream datasets; broader evaluation needed\n2. **Code domain failure:** \"Noticeable decline in retrieval performance in the code domain\" -- the synthesized shared context from Wikipedia does not transfer to code tasks\n3. **Scale not tested:** Does not evaluate larger-scale retrievers or generators beyond 8B parameters\n4. **Strong synthesizer required:** The framework requires GPT-4o-level reasoning capability for data synthesis; GPT-4o-mini failed to produce adequate training data\n5. **Corpus structure ignored:** Future work needs to integrate corpus-level structural information\n6. **Computational cost of perturbation:** Running 64 perturbation forward passes per training instance through the generator is expensive (though they don't discuss this explicitly as a limitation)\n\n---\n\n### OPENREVIEW REVIEWS\n\nThe paper's OpenReview page was located at `https://openreview.net/forum?id=VNam6izoMG`, but the reviews are **not publicly accessible**. EMNLP 2025 does not appear to make peer reviews publicly visible on OpenReview. No reviewer scores, strengths/weaknesses, or discussion content could be retrieved.\n\n---\n\nSources:\n- [arXiv Abstract Page](https://arxiv.org/abs/2504.00573)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2504.00573v2)\n- [ACL Anthology](https://aclanthology.org/2025.emnlp-main.33/)\n- [OpenReview Forum](https://openreview.net/forum?id=VNam6izoMG)\n- [Yilong Xu OpenReview Profile](https://openreview.net/profile?id=%7EYilong_Xu2)\n- [EMNLP 2025 Accepted Papers](https://2025.emnlp.org/program/main_papers/)"
      }
    ],
    "totalDurationMs": 234048,
    "totalTokens": 25824,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1942,
      "cache_read_input_tokens": 20683,
      "output_tokens": 3198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1942
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3198,
          "cache_read_input_tokens": 20683,
          "cache_creation_input_tokens": 1942,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1942,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "cbdc5c65-35d7-4b33-a85a-1b02a0aaad4d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "c524adb5-501f-4a04-bddf-0e0f3a15e419",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze papers for AAAI 2026 reasoning-intensive retrieval",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Tool result

_source line 24 · 2026-05-30T06:32:16.587Z_

<details><summary>↩ Tool result · `toolu_016yJa5G8aRY4yuQWVAvDe9N`</summary>

```text
Now I have comprehensive information. Let me compile the complete structured findings.

---

# ThinkPRM: "Process Reward Models That Think" -- Comprehensive Research Analysis

**Paper**: "Process Reward Models That Think" by Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang
**ArXiv**: 2504.16828 (v1: April 23, 2025; latest v5: December 8, 2025)
**Venue**: Submitted to ICLR 2026 but **withdrawn** (OpenReview ID: V727xqBYIW). No public reviews are available.
**Code**: https://github.com/mukhal/ThinkPRM
**Models**: ThinkPRM-1.5B, 7B, 14B released on HuggingFace

---

## 1. What Gap Did They Identify, and How?

The authors identified a fundamental gap in how process reward models (PRMs) are built, drawing a sharp distinction between two existing paradigms:

**Discriminative PRMs** (e.g., Math-Shepherd, RLHFFlow-Deepseek-PRM, Qwen2.5-Math-PRM): Train classifiers with binary cross-entropy to predict step-level correctness. They require **massive amounts of step-level labels** -- either via expensive human annotation (PRM800K uses ~800K human-annotated step labels from Lightman et al. 2023), gold step-by-step solutions, or compute-intensive Monte Carlo rollouts. They also use **fixed compute** at inference time and provide no interpretability into why a step is judged correct or incorrect.

**Generative verification (GenRM / LLM-as-a-Judge)**: Frames verification as text generation -- produce a rationale followed by a binary decision. However, prior generative approaches (like GenRM from Zhang et al. 2024) are limited to **outcome-level verification with short CoTs** (a few hundred tokens). This fundamentally limits their ability to scale test-time compute and to perform fine-grained step-level verification.

The gap: **No one had combined long chain-of-thought reasoning with step-level process verification in a data-efficient generative framework.** Discriminative PRMs had the process-level granularity but at enormous data cost and no interpretability. GenRM had the generative approach but only at the outcome level with short reasoning.

---

## 2. Key Insight Others Missed

The core insight is that **modern reasoning models (like DeepSeek-R1, QwQ) already possess strong verification capabilities through long CoT, and this can be unlocked for step-level process verification with minimal fine-tuning.**

Specifically:
- Reasoning models can generate extended verification chains (1K-5K tokens) that critique each step of a solution, but they need to be steered to produce reliable, well-formatted verification rather than attempting to re-solve the problem or producing invalid outputs.
- **Only ~1K carefully filtered synthetic verification CoTs** (corresponding to ~8K step-level labels) suffice to transform a reasoning model into a reliable process verifier -- achieving performance that matches or exceeds discriminative PRMs trained on **100x more data**.
- Verification compute can be **scaled** at test time -- both in parallel (sampling K independent verification chains and aggregating) and sequentially (budget forcing to think longer) -- unlike discriminative PRMs which use fixed compute.

---

## 3. How They Formulated the Problem Differently

**Prior discriminative PRMs**: Given a problem and a solution step, output a scalar correctness score via a classification head. This is a standard binary classification task.

**Prior GenRM**: Given a problem and a full solution, generate a short rationale and an outcome-level verdict (correct/incorrect). This is outcome-level, not step-level.

**ThinkPRM's formulation**: Given a problem and a solution (with step boundaries), generate an **extended verification chain-of-thought** that critiques **each step individually**, producing per-step judgments in the format `\boxed{correct}` or `\boxed{incorrect}`. For overall solution scoring, after generating the verification CoT, they **force-decode** the string "Is the solution correct?" and compute the score as:

**Score = P("yes") / [P("yes") + P("no")]**

This formulation turns step-level verification into a **text generation task** that leverages the full reasoning capabilities of the language model, produces interpretable verification traces, and naturally supports compute scaling.

---

## 4. Existing Techniques Adapted/Combined/Simplified

ThinkPRM is a synthesis of several existing ideas, combined in a novel way:

1. **GenRM's generative verification framing** (Zhang et al. 2024) -- but extended from outcome-level to step-level, and from short CoT to long CoT.

2. **Reasoning model distillation** (DeepSeek-R1-Distill) -- using models already trained for long CoT reasoning as the base, rather than standard LLMs.

3. **Process-based filtering from PRM800K** -- using a small subset of existing human annotations (8K step labels) not for training a classifier, but for **filtering synthetic data quality**. Only verification chains where all step-level judgments match the gold labels are retained.

4. **LoRA fine-tuning** (Hu et al. 2022) -- efficient adaptation with rank=32, alpha=16 for larger models.

5. **Budget forcing** (from reasoning scaling literature) -- controlling sequential compute by allowing the model to think longer or shorter during verification.

The simplification: instead of training a complex discriminative classifier on hundreds of thousands of labels, they generate 1K synthetic verification examples, filter them against 8K gold labels, and fine-tune with standard supervised learning. Training takes **30 minutes to 4.5 hours** on a single A100 GPU.

---

## 5. Technical Method Details

### Synthetic Data Pipeline

1. Sample problem-prefix pairs from PRM800K
2. Prompt QwQ-32B-Preview to generate verification CoTs for each pair
3. Sample 4 verification chains per prefix until 1K chains are obtained
4. **Filter** chains based on three criteria:
   - CoT follows expected format (extractable `\boxed{correct/incorrect}` labels)
   - Generated step judgments **match gold step labels** from PRM800K (process-based filtering)
   - CoT length within maximum budget (4096 tokens, to avoid overthinking)
5. Roughly **20% of initial samples** pass filtering

### Training Data Statistics
- 1,000 verification chains total
- 486 correct solutions (48.6%), 514 incorrect (51.4%)
- 7,474 correct step labels (92.3%), 625 incorrect step labels (7.7%)
- 869 unique questions
- Average 9.5 steps per prefix
- Average verification chain: 1,037 tokens (range: 207-3,669)

### The "8K Step Labels" Claim
The 1,000 verification chains cover ~8,099 total step labels (7,474 + 625). These are the only gold annotations needed -- about **1% of PRM800K's full ~800K labels**. The labels are used solely for filtering, not for direct training supervision.

### Fine-tuning
- **Base models**: R1-Distill-Qwen-1.5B, 7B, 14B (full fine-tuning for 1.5B/7B); QwQ-32B-Preview (LoRA)
- **LoRA config**: rank=32, alpha=16 for 14B and 32B models
- **Learning rates**: 4e-4 to 6e-5
- **Training time**: 30 min (1.5B) to 4.5 hours (QwQ-32B) on single A100 80GB
- **Max verification tokens at inference**: 8,192

### Inference
- Generate verification CoT for each step
- Extract per-step `\boxed{correct/incorrect}` labels
- For solution-level scoring: force-decode "Is the solution correct?" and compute P("yes")/[P("yes")+P("no")]
- **Parallel scaling**: sample K independent verification chains, average scores
- **Sequential scaling**: budget forcing to allow longer verification chains

---

## 6. Key Quantitative Results

### ProcessBench (Step-Level Error Detection, F1 Scores)

| Model | LLM-as-Judge F1 (OlympiadBench / OmniMath) | ThinkPRM F1 (OlympiadBench / OmniMath) | Invalid Output % (Judge vs ThinkPRM) |
|-------|---------------------------------------------|----------------------------------------|--------------------------------------|
| R1-Qwen-1.5B | 5.0 / 5.4 | **76.3 / 75.7** | 51.4% vs 1.4% |
| R1-Qwen-7B | 44.8 / 45.7 | **73.4 / 74.0** | 18.2% vs 1.1% |
| R1-Qwen-14B | 72.8 / 67.8 | **87.3 / 85.7** | 13.3% vs 2.3% |
| QwQ-32B | 50.6 / 55.5 | 73.1 / 73.2 | 7.9% vs 7.9-15.1% |

Key observation: Fine-tuning dramatically reduces invalid output rates (from 51% to 1.4% for the 1.5B model) and boosts F1 enormously, especially for smaller models.

### Long CoT vs Short CoT Ablation (ProcessBench F1)

| Model | Long CoT (OlympiadBench / OmniMath) | Short CoT (OlympiadBench / OmniMath) |
|-------|--------------------------------------|---------------------------------------|
| R1-Qwen-1.5B | **87.3 / 75.7** | 64.8 / 66.7 |
| R1-Qwen-14B | **87.3 / 85.7** | 55.3 / 60.8 |

Long CoT provides 20-30 F1 point improvement over short CoT, validating the core thesis.

### Best-of-N Selection and Beam Search
- **MATH-500**: ThinkPRM-14B outperforms discriminative PRMs and LLM-as-Judge across all sampling budgets
- **ThinkPRM-1.5B@4** (parallel scaling with 4 chains): >5% accuracy improvement over @1 on MATH-500
- ThinkPRM-1.5B surpasses **RLHFFlow-Deepseek-PRM by >7%** across all beam sizes despite ~100x fewer training labels

### Out-of-Domain Generalization (trained on math only)
- **GPQA-Diamond (Physics, 86 PhD-level questions)**: ThinkPRM outperforms discriminative PRM by **8%** at N=32
- **LiveCodeBench (200 problems)**: ThinkPRM exceeds discriminative PRM by **4.5%**
- Qwen2.5-7B-Math-PRM (discriminative, math-specific) struggles heavily out-of-domain

### Compute Scaling
- At matched token budget, ThinkPRM outperforms LLM-as-Judge by **7.2%** on ProcessBench
- LLM-as-Judge performance **degrades** after ~16K tokens (overthinking/looping); ThinkPRM outperforms discriminative PRM by **15 F1 points** at similar budgets
- ThinkPRM exhibits monotonically improving scaling behavior up to ~24K tokens

### Data Efficiency
- **Process-based filtering** substantially outperforms outcome-based filtering despite producing fewer examples (65K vs 128K chains before final selection)
- Automatic Monte Carlo rollout labels yield "very comparable performance" to manual human labels -- suggesting the method can be made fully automatic

---

## 7. Limitations

The authors explicitly acknowledge:

1. **Overconfidence**: Predicted PRM scores cluster near extremes (0 or 1) due to the token probability extraction mechanism. The model lacks proper calibration.

2. **Step Label Interference**: Due to autoregressive generation, if the PRM judges an early step as incorrect, it becomes biased toward labeling subsequent steps as incorrect regardless of their actual correctness. Earlier verification errors propagate forward.

3. **Inference Overhead**: Generating verification CoTs (1K-5K+ tokens per solution) introduces significant computational overhead compared to discriminative PRMs which produce a single scalar score per step. This is the fundamental cost of the generative approach.

4. **QwQ-32B Difficulty**: QwQ-32B-Preview was hard to train with LoRA and generates a relatively high percentage of invalid judgments after training (7.9-15.1%), suggesting the approach works best with R1-distilled models.

5. **LLM-as-Judge Baseline Fragility**: The unfinetuned LLM-as-Judge baseline showed high sensitivity to prompt wording (3-4 F1 point variance), frequent invalid output formats (models attempting to re-solve problems rather than verify), and overthinking/infinite looping (spike at 7K-8K tokens).

6. **Math-centric training**: While generalization to GPQA and LiveCodeBench is demonstrated, the training data is entirely math-based, and performance on truly distant domains is unknown.

---

## 8. Venue Status and Reviews

The paper was submitted to **ICLR 2026** (OpenReview ID: V727xqBYIW, submitted September 18, 2025, modified November 15, 2025) but was **withdrawn** by the authors. **No public reviews, scores, or meta-reviews are available** on OpenReview -- the review content appears to have been removed or never made public upon withdrawal. The reason for withdrawal is not stated publicly; a common reason for withdrawing strong arxiv papers is concurrent acceptance elsewhere or plans to resubmit to a different venue.

---

## Summary of What Makes This Paper Notable

The paper's contribution is a **surprisingly simple recipe**: take a reasoning model already capable of long CoT, generate ~1K synthetic verification chains filtered against ~8K gold step labels, fine-tune for a few hours on one GPU, and obtain a process verifier that (a) outperforms discriminative PRMs trained on 100x more data, (b) generalizes out-of-domain, (c) scales with test-time compute, and (d) produces interpretable verification traces. The key conceptual move is recognizing that **verification is itself a reasoning task** that benefits from extended thinking, not just a classification task.

Sources:
- [ArXiv Abstract](https://arxiv.org/abs/2504.16828)
- [ArXiv HTML Full Paper](https://arxiv.org/html/2504.16828v5)
- [OpenReview Submission](https://openreview.net/forum?id=V727xqBYIW)
- [GitHub Repository](https://github.com/mukhal/ThinkPRM)
- [Project Page](https://mukhal.github.io/projects/thinkprm/)
- [Medium Analysis by Sachin Kumar](https://medium.com/@techsachin/thinkprm-generative-process-reward-model-for-solution-verification-via-long-cot-reasoning-2016f1e1387d)
- [MarkTechPost Summary](https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/)

agentId: a82887db8327dee27 (use SendMessage with to: 'a82887db8327dee27' to continue this agent)
&lt;usage>total_tokens: 26456
tool_uses: 16
duration_ms: 250559&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2124f8d-f8ef-46fe-84ee-db9317ef4de8",
  "isSidechain": false,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "type": "user",
  "uuid": "02582a43-cd2b-42cd-b838-66aeef10543c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Process Reward Models That Think (ThinkPRM)\" by Mahmoud Khalil et al. (arXiv 2025, ICLR 2026 submission), arxiv URL: https://arxiv.org/abs/2504.16828\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF (https://arxiv.org/pdf/2504.16828)\n3. Search for OpenReview reviews for ICLR 2026 if available\n\nFor each, extract:\n- What gap did they identify and HOW? (discriminative vs generative PRMs)\n- What was the key insight others missed? (using long CoT for verification)\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- Technical method details (how they fine-tune, what data they use, the 8K step labels claim)\n- Key quantitative results (performance vs discriminative PRMs, generalization)\n- Limitations\n\nBe thorough and specific. Return all findings in a structured format.",
    "agentId": "a82887db8327dee27",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the complete structured findings.\n\n---\n\n# ThinkPRM: \"Process Reward Models That Think\" -- Comprehensive Research Analysis\n\n**Paper**: \"Process Reward Models That Think\" by Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang\n**ArXiv**: 2504.16828 (v1: April 23, 2025; latest v5: December 8, 2025)\n**Venue**: Submitted to ICLR 2026 but **withdrawn** (OpenReview ID: V727xqBYIW). No public reviews are available.\n**Code**: https://github.com/mukhal/ThinkPRM\n**Models**: ThinkPRM-1.5B, 7B, 14B released on HuggingFace\n\n---\n\n## 1. What Gap Did They Identify, and How?\n\nThe authors identified a fundamental gap in how process reward models (PRMs) are built, drawing a sharp distinction between two existing paradigms:\n\n**Discriminative PRMs** (e.g., Math-Shepherd, RLHFFlow-Deepseek-PRM, Qwen2.5-Math-PRM): Train classifiers with binary cross-entropy to predict step-level correctness. They require **massive amounts of step-level labels** -- either via expensive human annotation (PRM800K uses ~800K human-annotated step labels from Lightman et al. 2023), gold step-by-step solutions, or compute-intensive Monte Carlo rollouts. They also use **fixed compute** at inference time and provide no interpretability into why a step is judged correct or incorrect.\n\n**Generative verification (GenRM / LLM-as-a-Judge)**: Frames verification as text generation -- produce a rationale followed by a binary decision. However, prior generative approaches (like GenRM from Zhang et al. 2024) are limited to **outcome-level verification with short CoTs** (a few hundred tokens). This fundamentally limits their ability to scale test-time compute and to perform fine-grained step-level verification.\n\nThe gap: **No one had combined long chain-of-thought reasoning with step-level process verification in a data-efficient generative framework.** Discriminative PRMs had the process-level granularity but at enormous data cost and no interpretability. GenRM had the generative approach but only at the outcome level with short reasoning.\n\n---\n\n## 2. Key Insight Others Missed\n\nThe core insight is that **modern reasoning models (like DeepSeek-R1, QwQ) already possess strong verification capabilities through long CoT, and this can be unlocked for step-level process verification with minimal fine-tuning.**\n\nSpecifically:\n- Reasoning models can generate extended verification chains (1K-5K tokens) that critique each step of a solution, but they need to be steered to produce reliable, well-formatted verification rather than attempting to re-solve the problem or producing invalid outputs.\n- **Only ~1K carefully filtered synthetic verification CoTs** (corresponding to ~8K step-level labels) suffice to transform a reasoning model into a reliable process verifier -- achieving performance that matches or exceeds discriminative PRMs trained on **100x more data**.\n- Verification compute can be **scaled** at test time -- both in parallel (sampling K independent verification chains and aggregating) and sequentially (budget forcing to think longer) -- unlike discriminative PRMs which use fixed compute.\n\n---\n\n## 3. How They Formulated the Problem Differently\n\n**Prior discriminative PRMs**: Given a problem and a solution step, output a scalar correctness score via a classification head. This is a standard binary classification task.\n\n**Prior GenRM**: Given a problem and a full solution, generate a short rationale and an outcome-level verdict (correct/incorrect). This is outcome-level, not step-level.\n\n**ThinkPRM's formulation**: Given a problem and a solution (with step boundaries), generate an **extended verification chain-of-thought** that critiques **each step individually**, producing per-step judgments in the format `\\boxed{correct}` or `\\boxed{incorrect}`. For overall solution scoring, after generating the verification CoT, they **force-decode** the string \"Is the solution correct?\" and compute the score as:\n\n**Score = P(\"yes\") / [P(\"yes\") + P(\"no\")]**\n\nThis formulation turns step-level verification into a **text generation task** that leverages the full reasoning capabilities of the language model, produces interpretable verification traces, and naturally supports compute scaling.\n\n---\n\n## 4. Existing Techniques Adapted/Combined/Simplified\n\nThinkPRM is a synthesis of several existing ideas, combined in a novel way:\n\n1. **GenRM's generative verification framing** (Zhang et al. 2024) -- but extended from outcome-level to step-level, and from short CoT to long CoT.\n\n2. **Reasoning model distillation** (DeepSeek-R1-Distill) -- using models already trained for long CoT reasoning as the base, rather than standard LLMs.\n\n3. **Process-based filtering from PRM800K** -- using a small subset of existing human annotations (8K step labels) not for training a classifier, but for **filtering synthetic data quality**. Only verification chains where all step-level judgments match the gold labels are retained.\n\n4. **LoRA fine-tuning** (Hu et al. 2022) -- efficient adaptation with rank=32, alpha=16 for larger models.\n\n5. **Budget forcing** (from reasoning scaling literature) -- controlling sequential compute by allowing the model to think longer or shorter during verification.\n\nThe simplification: instead of training a complex discriminative classifier on hundreds of thousands of labels, they generate 1K synthetic verification examples, filter them against 8K gold labels, and fine-tune with standard supervised learning. Training takes **30 minutes to 4.5 hours** on a single A100 GPU.\n\n---\n\n## 5. Technical Method Details\n\n### Synthetic Data Pipeline\n\n1. Sample problem-prefix pairs from PRM800K\n2. Prompt QwQ-32B-Preview to generate verification CoTs for each pair\n3. Sample 4 verification chains per prefix until 1K chains are obtained\n4. **Filter** chains based on three criteria:\n   - CoT follows expected format (extractable `\\boxed{correct/incorrect}` labels)\n   - Generated step judgments **match gold step labels** from PRM800K (process-based filtering)\n   - CoT length within maximum budget (4096 tokens, to avoid overthinking)\n5. Roughly **20% of initial samples** pass filtering\n\n### Training Data Statistics\n- 1,000 verification chains total\n- 486 correct solutions (48.6%), 514 incorrect (51.4%)\n- 7,474 correct step labels (92.3%), 625 incorrect step labels (7.7%)\n- 869 unique questions\n- Average 9.5 steps per prefix\n- Average verification chain: 1,037 tokens (range: 207-3,669)\n\n### The \"8K Step Labels\" Claim\nThe 1,000 verification chains cover ~8,099 total step labels (7,474 + 625). These are the only gold annotations needed -- about **1% of PRM800K's full ~800K labels**. The labels are used solely for filtering, not for direct training supervision.\n\n### Fine-tuning\n- **Base models**: R1-Distill-Qwen-1.5B, 7B, 14B (full fine-tuning for 1.5B/7B); QwQ-32B-Preview (LoRA)\n- **LoRA config**: rank=32, alpha=16 for 14B and 32B models\n- **Learning rates**: 4e-4 to 6e-5\n- **Training time**: 30 min (1.5B) to 4.5 hours (QwQ-32B) on single A100 80GB\n- **Max verification tokens at inference**: 8,192\n\n### Inference\n- Generate verification CoT for each step\n- Extract per-step `\\boxed{correct/incorrect}` labels\n- For solution-level scoring: force-decode \"Is the solution correct?\" and compute P(\"yes\")/[P(\"yes\")+P(\"no\")]\n- **Parallel scaling**: sample K independent verification chains, average scores\n- **Sequential scaling**: budget forcing to allow longer verification chains\n\n---\n\n## 6. Key Quantitative Results\n\n### ProcessBench (Step-Level Error Detection, F1 Scores)\n\n| Model | LLM-as-Judge F1 (OlympiadBench / OmniMath) | ThinkPRM F1 (OlympiadBench / OmniMath) | Invalid Output % (Judge vs ThinkPRM) |\n|-------|---------------------------------------------|----------------------------------------|--------------------------------------|\n| R1-Qwen-1.5B | 5.0 / 5.4 | **76.3 / 75.7** | 51.4% vs 1.4% |\n| R1-Qwen-7B | 44.8 / 45.7 | **73.4 / 74.0** | 18.2% vs 1.1% |\n| R1-Qwen-14B | 72.8 / 67.8 | **87.3 / 85.7** | 13.3% vs 2.3% |\n| QwQ-32B | 50.6 / 55.5 | 73.1 / 73.2 | 7.9% vs 7.9-15.1% |\n\nKey observation: Fine-tuning dramatically reduces invalid output rates (from 51% to 1.4% for the 1.5B model) and boosts F1 enormously, especially for smaller models.\n\n### Long CoT vs Short CoT Ablation (ProcessBench F1)\n\n| Model | Long CoT (OlympiadBench / OmniMath) | Short CoT (OlympiadBench / OmniMath) |\n|-------|--------------------------------------|---------------------------------------|\n| R1-Qwen-1.5B | **87.3 / 75.7** | 64.8 / 66.7 |\n| R1-Qwen-14B | **87.3 / 85.7** | 55.3 / 60.8 |\n\nLong CoT provides 20-30 F1 point improvement over short CoT, validating the core thesis.\n\n### Best-of-N Selection and Beam Search\n- **MATH-500**: ThinkPRM-14B outperforms discriminative PRMs and LLM-as-Judge across all sampling budgets\n- **ThinkPRM-1.5B@4** (parallel scaling with 4 chains): >5% accuracy improvement over @1 on MATH-500\n- ThinkPRM-1.5B surpasses **RLHFFlow-Deepseek-PRM by >7%** across all beam sizes despite ~100x fewer training labels\n\n### Out-of-Domain Generalization (trained on math only)\n- **GPQA-Diamond (Physics, 86 PhD-level questions)**: ThinkPRM outperforms discriminative PRM by **8%** at N=32\n- **LiveCodeBench (200 problems)**: ThinkPRM exceeds discriminative PRM by **4.5%**\n- Qwen2.5-7B-Math-PRM (discriminative, math-specific) struggles heavily out-of-domain\n\n### Compute Scaling\n- At matched token budget, ThinkPRM outperforms LLM-as-Judge by **7.2%** on ProcessBench\n- LLM-as-Judge performance **degrades** after ~16K tokens (overthinking/looping); ThinkPRM outperforms discriminative PRM by **15 F1 points** at similar budgets\n- ThinkPRM exhibits monotonically improving scaling behavior up to ~24K tokens\n\n### Data Efficiency\n- **Process-based filtering** substantially outperforms outcome-based filtering despite producing fewer examples (65K vs 128K chains before final selection)\n- Automatic Monte Carlo rollout labels yield \"very comparable performance\" to manual human labels -- suggesting the method can be made fully automatic\n\n---\n\n## 7. Limitations\n\nThe authors explicitly acknowledge:\n\n1. **Overconfidence**: Predicted PRM scores cluster near extremes (0 or 1) due to the token probability extraction mechanism. The model lacks proper calibration.\n\n2. **Step Label Interference**: Due to autoregressive generation, if the PRM judges an early step as incorrect, it becomes biased toward labeling subsequent steps as incorrect regardless of their actual correctness. Earlier verification errors propagate forward.\n\n3. **Inference Overhead**: Generating verification CoTs (1K-5K+ tokens per solution) introduces significant computational overhead compared to discriminative PRMs which produce a single scalar score per step. This is the fundamental cost of the generative approach.\n\n4. **QwQ-32B Difficulty**: QwQ-32B-Preview was hard to train with LoRA and generates a relatively high percentage of invalid judgments after training (7.9-15.1%), suggesting the approach works best with R1-distilled models.\n\n5. **LLM-as-Judge Baseline Fragility**: The unfinetuned LLM-as-Judge baseline showed high sensitivity to prompt wording (3-4 F1 point variance), frequent invalid output formats (models attempting to re-solve problems rather than verify), and overthinking/infinite looping (spike at 7K-8K tokens).\n\n6. **Math-centric training**: While generalization to GPQA and LiveCodeBench is demonstrated, the training data is entirely math-based, and performance on truly distant domains is unknown.\n\n---\n\n## 8. Venue Status and Reviews\n\nThe paper was submitted to **ICLR 2026** (OpenReview ID: V727xqBYIW, submitted September 18, 2025, modified November 15, 2025) but was **withdrawn** by the authors. **No public reviews, scores, or meta-reviews are available** on OpenReview -- the review content appears to have been removed or never made public upon withdrawal. The reason for withdrawal is not stated publicly; a common reason for withdrawing strong arxiv papers is concurrent acceptance elsewhere or plans to resubmit to a different venue.\n\n---\n\n## Summary of What Makes This Paper Notable\n\nThe paper's contribution is a **surprisingly simple recipe**: take a reasoning model already capable of long CoT, generate ~1K synthetic verification chains filtered against ~8K gold step labels, fine-tune for a few hours on one GPU, and obtain a process verifier that (a) outperforms discriminative PRMs trained on 100x more data, (b) generalizes out-of-domain, (c) scales with test-time compute, and (d) produces interpretable verification traces. The key conceptual move is recognizing that **verification is itself a reasoning task** that benefits from extended thinking, not just a classification task.\n\nSources:\n- [ArXiv Abstract](https://arxiv.org/abs/2504.16828)\n- [ArXiv HTML Full Paper](https://arxiv.org/html/2504.16828v5)\n- [OpenReview Submission](https://openreview.net/forum?id=V727xqBYIW)\n- [GitHub Repository](https://github.com/mukhal/ThinkPRM)\n- [Project Page](https://mukhal.github.io/projects/thinkprm/)\n- [Medium Analysis by Sachin Kumar](https://medium.com/@techsachin/thinkprm-generative-process-reward-model-for-solution-verification-via-long-cot-reasoning-2016f1e1387d)\n- [MarkTechPost Summary](https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/)"
      }
    ],
    "totalDurationMs": 250559,
    "totalTokens": 26456,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1444,
      "cache_read_input_tokens": 21217,
      "output_tokens": 3794,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1444
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3794,
          "cache_read_input_tokens": 21217,
          "cache_creation_input_tokens": 1444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1444,
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
  "sourceToolAssistantUUID": "f2124f8d-f8ef-46fe-84ee-db9317ef4de8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-30T06:32:32.027Z_

<details><summary>↩ Tool result · `toolu_017SMqKJjubQWz4o3b8AJ2oR`</summary>

````text
Now I have comprehensive information. Let me compile the complete structured research summary.

---

# Research Deep-Dive: "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning"

**Paper:** ReasonRAG / RAG-ProGuide
**Authors:** Wenlin Zhang, Xiangyang Li, Kuicai Dong, Yichao Wang, Pengyue Jia, Xiaopeng Li, Yingyi Zhang, Derong Xu, Zhaocheng Du, Huifeng Guo, Ruiming Tang, Xiangyu Zhao
**Affiliations:** City University of Hong Kong, Noah's Ark Lab (Huawei)
**Venue:** NeurIPS 2025 (Poster), presented December 4, 2025, San Diego
**arXiv:** 2505.14069 (v1: May 20, 2025; v3: December 8, 2025)
**Code:** https://github.com/Applied-Machine-Learning-Lab/ReasonRAG (MIT license)
**Dataset:** RAG-ProGuide on HuggingFace

---

## 1. Gap Identified and HOW They Identified It

**The gap:** Prior agentic RAG systems (notably Search-R1) used **outcome-supervised RL** where only the final answer correctness provides the reward signal. Nobody had systematically applied **process-supervised RL** to agentic RAG.

**How they identified it:** They analyzed three specific failure modes of outcome-supervised RL in the RAG setting:

1. **Low exploration efficiency** -- the model must generate an entire reasoning chain (query, retrieve, extract, answer -- potentially multi-hop) before receiving ANY reward signal. This makes the search space enormous and learning slow.
2. **Gradient conflict** -- when a mistake occurs late in the reasoning chain, the entire sequence (including correct early steps like good query formulation) gets penalized equally. Correct intermediate actions are punished alongside incorrect ones.
3. **Sparse rewards** -- outcome supervision only provides feedback at the terminal state (final answer), creating a credit assignment problem across the multi-step RAG pipeline.

They positioned this against the broader RL literature where process reward models (PRMs) had shown success in math reasoning (e.g., in the PRM800K / Let's Verify Step by Step line of work) but had NOT been applied to the retrieval-augmented generation setting.

---

## 2. Key Insight Others Missed

The central insight: **the RAG pipeline has natural decomposition points where process-level rewards can be meaningfully defined** -- specifically at three stages: (i) query generation quality, (ii) evidence extraction quality, and (iii) answer generation quality. Unlike math reasoning where step verification is more ambiguous, RAG has observable intermediate artifacts (the query sent to the retriever, the evidence spans selected from documents, the final answer) that can each be evaluated.

The second insight: **you can use MCTS + a Shortest Path Reward Estimation (SPRE) to automatically construct process-level preference data** without expensive human annotation. The SPRE formulation specifically encourages the shortest correct path via an exponential decay factor alpha^{steps}, encoding the bias that fewer retrieval rounds are preferable when they lead to correct answers. This is domain-specific to RAG and wouldn't apply straightforwardly to other reasoning tasks.

---

## 3. Problem Formulation -- How It Differs

They formulate agentic RAG as a **three-stage state machine** with explicit states:
- **Reasoning stage:** The model decides whether to generate a search query or produce a final answer
- **Grounding stage:** Given retrieved documents, the model extracts evidence spans
- **Terminal stage:** The model has produced an answer; episode ends

This is formalized as a state `s = (x, y_{&lt;i}, stage)` where stage in {Reasoning, Grounding, Terminal}. The policy is:

```
pi(a|s) = LLM(a|x, y_{&lt;i}, p_stage)  [Reasoning]
pi(a|s) = LLM(a|x, y_{&lt;i}, docs, p_stage)  [Grounding]
```

This differs from Search-R1 which treats the entire generation as a single monolithic RL problem with a binary reward at the end. ReasonRAG's formulation enables reward assignment at each state transition.

---

## 4. Existing Techniques Adapted/Combined/Simplified

ReasonRAG combines several existing techniques in a novel way:

1. **Monte Carlo Tree Search (MCTS)** -- adapted from AlphaGo/AlphaZero and recent LLM reasoning work. Used here specifically to explore the RAG decision space (query vs. answer, which evidence to extract) rather than math/code reasoning.

2. **Shortest Path Reward Estimation (SPRE)** -- a novel reward formulation:
   ```
   Q_t = (1/k) * sum_{i=1}^{k} v(rollout_i) * alpha^{step(rollout_i)}
   ```
   This adapts Monte Carlo value estimation with a **step-decay penalty** (alpha in (0,1]) that specifically rewards shorter correct trajectories. This is their novel contribution -- encoding the RAG-specific prior that fewer retrieval iterations are better.

3. **Direct Preference Optimization (DPO)** -- used instead of PPO/GRPO for the actual policy optimization. The preference pairs come from the MCTS exploration, comparing high-reward vs. low-reward actions at each intermediate step:
   ```
   L(theta) = -E[log sigma(beta * log(p_theta(y_w|x,y_{&lt;t}) / p_theta(y_l|x,y_{&lt;t})))]
   ```

4. **UCB-based tree exploration** -- standard UCB formula for node selection in MCTS:
   ```
   s* = argmax [Q(s_i) + c_uct * sqrt(sum N(s_i)) / (1+N(s_i))]
   ```

The combination is: MCTS explores the RAG decision tree -> SPRE evaluates nodes with shortest-path bias -> preference pairs are extracted -> DPO trains the LLM. This is a pipeline combination rather than a single algorithmic innovation.

---

## 5. Technical Method Details

### RAG-ProGuide Dataset Construction

- **Source questions:** 3,000 each from PopQA, HotpotQA, 2WikiMultiHopQA
- **After processing:** 4,603 questions total
- **MCTS exploration:** For each question, MCTS explores multiple trajectories through the RAG state machine
- **Reward computation:** F1 score between predicted and ground-truth answers, propagated through tree via SPRE
- **Preference pair extraction:** At each tree node, children with higher SPRE scores become "preferred" and lower become "dispreferred"
- **Filtering:** Pairs with identical responses or reward difference < 0.01 are removed

**Final dataset statistics:**
- 4,603 questions
- 13,289 preference pairs total
- Action type distribution: Query Generation 24.8%, Evidence Extraction 32.4%, Answer Generation 42.8%
- Retrieval iterations: 1-5 (median 3, avg 2.7)
- Token length per action: 9-625 (median 60, avg 65.5)

### Training

- **Base model:** Qwen2.5-7B-Instruct
- **Method:** DPO using LLaMA Factory
- **Retriever:** BGE (bge-base-en-v1.5) -- STATIC, not trained
- **Knowledge source:** Wikidump 2018 + dataset-specific corpora
- **Retrieval:** Top-3 documents per query

### Inference (Algorithm 1)

Structured loop with explicit tags: `&lt;query>`, `&lt;evidence>`, `&lt;answer>` control state transitions. The model autonomously decides when to search vs. when to answer, what query to formulate, which evidence to extract, all via the trained policy.

---

## 6. Key Quantitative Results

### Main results (5 benchmarks, Avg EM / Avg F1):

| Method | Training Data | Avg EM | Avg F1 |
|--------|--------------|--------|--------|
| Naive Generation | 0 | 11.5 | 19.4 |
| Standard RAG | 0 | 24.3 | 32.0 |
| Search-R1 | 90k | 32.8 | 40.7 |
| AutoRAG | 10k | 29.5 | 36.9 |
| **ReasonRAG** | **5k** | **34.4** | **42.3** |

### Data efficiency claim (the "18x" number):

ReasonRAG uses 5k training instances vs. Search-R1's 90k = **18x fewer training instances** while achieving **+1.6 points higher Avg EM** and **+1.6 points higher Avg F1**.

More precisely: ReasonRAG has 13k process-level preference pairs from 5k questions. Search-R1 has ~270k intermediate steps from 90k questions. So in terms of step-level data, ReasonRAG uses ~20x less.

### Per-dataset highlights:
- **PopQA** (single-hop): 41.5 EM / 46.2 F1 vs. Search-R1's 39.7/44.8
- **HotpotQA** (multi-hop): 38.4 EM / 48.9 F1 vs. Search-R1's 37.0/47.0
- **2WikiMultiHopQA** (multi-hop): 43.6 EM / 50.4 F1 vs. Search-R1's 41.4/48.0
- **Bamboogle** (out-of-domain): 36.0 EM / 45.5 F1 vs. Search-R1's 32.0/43.8
- **MuSiQue** (out-of-domain): 12.8 EM / 20.6 F1 vs. Search-R1's 14.6/19.9

Note: ReasonRAG loses to Search-R1 on MuSiQue EM (12.8 vs 14.6) but wins on F1 (20.6 vs 19.9).

### Ablation (optimization strategy, Table 3):
- Base model: 22.0 Avg EM / 32.8 Avg F1
- SFT on process data: 23.9 / 32.0 (overfits on multi-hop, hurts single-hop)
- RL-ORL with 5k data (outcome reward): 21.3 / 28.9 (WORSE than base -- outcome reward with small data fails)
- RL-ORL with 10k data: 32.0 / 39.9 (competitive but still below)
- **RL-PRL (ReasonRAG):** 34.5 / 42.3

This ablation is the strongest evidence: with the SAME 5k data, outcome RL completely fails (21.3 EM) while process RL succeeds (34.5 EM). Outcome RL needs 10k+ data to even approach process RL's results.

### Training efficiency:
ReasonRAG converges faster in GPU hours than Search-R1, especially on multi-hop tasks.

---

## 7. Limitations

**Explicitly stated by the authors (Appendix H):**
1. **Higher per-sample annotation cost:** Process-level data rollout via MCTS is more time-consuming per sample than outcome-level data collection (though fewer samples are needed overall).
2. **Safety concerns:** Potential risk of generating harmful content if external knowledge sources are not properly curated.

**Implicit/unstated limitations I identify:**
3. **Only tested at 7B scale** -- scalability to larger models (70B+) is undemonstrated.
4. **Static retriever** -- the retriever (BGE) is never trained. The system only improves the LLM's ability to USE retrieval, not the retrieval quality itself.
5. **Wikipedia-only knowledge base** -- Wikidump 2018 is the knowledge source; performance on domain-specific or more current corpora is unknown.
6. **Closed-book QA benchmarks only** -- all five benchmarks are factoid QA. No evaluation on long-form generation, summarization, or open-ended tasks.
7. **DPO rather than online RL** -- they use offline preference optimization (DPO) rather than online RL (PPO/GRPO). This means the policy cannot improve beyond the quality of the MCTS-generated preference data.
8. **MCTS requires a capable base model** -- the MCTS exploration uses the base Qwen2.5-7B model to generate rollouts. If the base model is weak, the exploration quality will be poor, creating a bootstrapping problem.
9. **The "18x" claim is about instance count, not compute** -- MCTS data generation is expensive. The total compute (data generation + training) comparison is not clearly presented.
10. **MuSiQue underperformance** -- ReasonRAG loses to Search-R1 on MuSiQue EM, suggesting the process reward may not generalize equally well to all multi-hop reasoning patterns.

---

## 8. CRITICAL DISTINCTION: What Gets Trained?

**ReasonRAG trains ONLY the LLM (Qwen2.5-7B-Instruct). The retriever is NOT trained.**

Evidence:
- The retriever is BGE (bge-base-en-v1.5), used as a static component across ALL methods
- The DPO objective (Equation 3) optimizes p_theta -- the LLM's parameters
- Algorithm 1 shows the retriever R is called as a black-box: `docs <- R(q)`
- No gradient flows through the retriever at any point
- The LLM is trained to: (a) decide WHEN to retrieve, (b) formulate WHAT query to send, (c) extract WHICH evidence from retrieved docs, and (d) generate the final answer

**This is a critical distinction for your research:** The retriever remains frozen. All improvements come from teaching the LLM to be a better "user" of the retriever -- better query formulation, better evidence selection, better answer synthesis. The retrieval quality itself is unchanged.

---

## 9. Related/Follow-up Work

Two notable follow-ups that address similar themes:

- **HiPRAG** (arXiv 2510.07794): Also uses process rewards for agentic RAG but with a "hierarchical" reward structure. Focuses on over-search and under-search behaviors. Reports 65.4% (3B) and 67.2% (7B) average accuracy.

- **Search-P1** (arXiv 2602.22576): Introduces "path-centric reward shaping" -- evaluates structural quality of reasoning trajectories via order-agnostic step coverage and dual-track scoring. Claims +7.7 average accuracy gain. Takes a different approach to intermediate rewards than ReasonRAG.

---

## 10. Assessment for Your Research

**Strengths relevant to your work:**
- Clean demonstration that process rewards >> outcome rewards for RAG (the 5k vs. 90k comparison is compelling)
- The three-stage decomposition (query/evidence/answer) is a natural and reusable framework
- MCTS for automatic preference data construction avoids human annotation costs
- The SPRE shortest-path bias is a simple but effective inductive bias for RAG

**Weaknesses to be aware of:**
- The absolute performance improvements over Search-R1 are modest (+1.6 EM/F1 on average)
- The "18x data efficiency" headline obscures that MCTS data generation is computationally expensive
- DPO is a one-shot offline method -- no iterative online improvement
- Retriever is frozen -- a joint LLM+retriever training approach could potentially do better
- Only factoid QA benchmarks; unclear how this transfers to more complex RAG tasks

Sources:
- [arXiv Paper](https://arxiv.org/abs/2505.14069)
- [OpenReview](https://openreview.net/forum?id=h3LlJ6Bh4S)
- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/116682)
- [GitHub Repository](https://github.com/Applied-Machine-Learning-Lab/ReasonRAG)
- [Moonlight Literature Review](https://www.themoonlight.io/en/review/process-vs-outcome-reward-which-is-better-for-agentic-rag-reinforcement-learning)
- [HiPRAG (follow-up)](https://arxiv.org/abs/2510.07794)
- [Search-P1 (follow-up)](https://arxiv.org/abs/2602.22576)

agentId: aa34d3135a3369818 (use SendMessage with to: 'aa34d3135a3369818' to continue this agent)
&lt;usage>total_tokens: 30608
tool_uses: 18
duration_ms: 259811&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "3ea9a5f9-0938-4df7-8a24-ba18381283d8",
  "isSidechain": false,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "type": "user",
  "uuid": "172fe256-2afe-418b-b5c5-f692b1595825",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning\" (ReasonRAG / RAG-ProGuide) by Wenlin Zhang et al. (arXiv 2025), arxiv URL: https://arxiv.org/abs/2505.14069\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF (https://arxiv.org/pdf/2505.14069)\n3. Search for any reviews or discussion about this paper\n\nFor each, extract:\n- What gap did they identify and HOW? (process vs outcome rewards for RAG)\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- Technical method details (RAG-ProGuide, the process-level rewards for query generation, evidence extraction, answer generation)\n- Key quantitative results (18× data efficiency claim)\n- Limitations\n- Whether this trains the retriever or the LLM (critical distinction for our research)\n\nBe thorough and specific. Return all findings in a structured format.",
    "agentId": "aa34d3135a3369818",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the complete structured research summary.\n\n---\n\n# Research Deep-Dive: \"Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning\"\n\n**Paper:** ReasonRAG / RAG-ProGuide\n**Authors:** Wenlin Zhang, Xiangyang Li, Kuicai Dong, Yichao Wang, Pengyue Jia, Xiaopeng Li, Yingyi Zhang, Derong Xu, Zhaocheng Du, Huifeng Guo, Ruiming Tang, Xiangyu Zhao\n**Affiliations:** City University of Hong Kong, Noah's Ark Lab (Huawei)\n**Venue:** NeurIPS 2025 (Poster), presented December 4, 2025, San Diego\n**arXiv:** 2505.14069 (v1: May 20, 2025; v3: December 8, 2025)\n**Code:** https://github.com/Applied-Machine-Learning-Lab/ReasonRAG (MIT license)\n**Dataset:** RAG-ProGuide on HuggingFace\n\n---\n\n## 1. Gap Identified and HOW They Identified It\n\n**The gap:** Prior agentic RAG systems (notably Search-R1) used **outcome-supervised RL** where only the final answer correctness provides the reward signal. Nobody had systematically applied **process-supervised RL** to agentic RAG.\n\n**How they identified it:** They analyzed three specific failure modes of outcome-supervised RL in the RAG setting:\n\n1. **Low exploration efficiency** -- the model must generate an entire reasoning chain (query, retrieve, extract, answer -- potentially multi-hop) before receiving ANY reward signal. This makes the search space enormous and learning slow.\n2. **Gradient conflict** -- when a mistake occurs late in the reasoning chain, the entire sequence (including correct early steps like good query formulation) gets penalized equally. Correct intermediate actions are punished alongside incorrect ones.\n3. **Sparse rewards** -- outcome supervision only provides feedback at the terminal state (final answer), creating a credit assignment problem across the multi-step RAG pipeline.\n\nThey positioned this against the broader RL literature where process reward models (PRMs) had shown success in math reasoning (e.g., in the PRM800K / Let's Verify Step by Step line of work) but had NOT been applied to the retrieval-augmented generation setting.\n\n---\n\n## 2. Key Insight Others Missed\n\nThe central insight: **the RAG pipeline has natural decomposition points where process-level rewards can be meaningfully defined** -- specifically at three stages: (i) query generation quality, (ii) evidence extraction quality, and (iii) answer generation quality. Unlike math reasoning where step verification is more ambiguous, RAG has observable intermediate artifacts (the query sent to the retriever, the evidence spans selected from documents, the final answer) that can each be evaluated.\n\nThe second insight: **you can use MCTS + a Shortest Path Reward Estimation (SPRE) to automatically construct process-level preference data** without expensive human annotation. The SPRE formulation specifically encourages the shortest correct path via an exponential decay factor alpha^{steps}, encoding the bias that fewer retrieval rounds are preferable when they lead to correct answers. This is domain-specific to RAG and wouldn't apply straightforwardly to other reasoning tasks.\n\n---\n\n## 3. Problem Formulation -- How It Differs\n\nThey formulate agentic RAG as a **three-stage state machine** with explicit states:\n- **Reasoning stage:** The model decides whether to generate a search query or produce a final answer\n- **Grounding stage:** Given retrieved documents, the model extracts evidence spans\n- **Terminal stage:** The model has produced an answer; episode ends\n\nThis is formalized as a state `s = (x, y_{&lt;i}, stage)` where stage in {Reasoning, Grounding, Terminal}. The policy is:\n\n```\npi(a|s) = LLM(a|x, y_{&lt;i}, p_stage)  [Reasoning]\npi(a|s) = LLM(a|x, y_{&lt;i}, docs, p_stage)  [Grounding]\n```\n\nThis differs from Search-R1 which treats the entire generation as a single monolithic RL problem with a binary reward at the end. ReasonRAG's formulation enables reward assignment at each state transition.\n\n---\n\n## 4. Existing Techniques Adapted/Combined/Simplified\n\nReasonRAG combines several existing techniques in a novel way:\n\n1. **Monte Carlo Tree Search (MCTS)** -- adapted from AlphaGo/AlphaZero and recent LLM reasoning work. Used here specifically to explore the RAG decision space (query vs. answer, which evidence to extract) rather than math/code reasoning.\n\n2. **Shortest Path Reward Estimation (SPRE)** -- a novel reward formulation:\n   ```\n   Q_t = (1/k) * sum_{i=1}^{k} v(rollout_i) * alpha^{step(rollout_i)}\n   ```\n   This adapts Monte Carlo value estimation with a **step-decay penalty** (alpha in (0,1]) that specifically rewards shorter correct trajectories. This is their novel contribution -- encoding the RAG-specific prior that fewer retrieval iterations are better.\n\n3. **Direct Preference Optimization (DPO)** -- used instead of PPO/GRPO for the actual policy optimization. The preference pairs come from the MCTS exploration, comparing high-reward vs. low-reward actions at each intermediate step:\n   ```\n   L(theta) = -E[log sigma(beta * log(p_theta(y_w|x,y_{&lt;t}) / p_theta(y_l|x,y_{&lt;t})))]\n   ```\n\n4. **UCB-based tree exploration** -- standard UCB formula for node selection in MCTS:\n   ```\n   s* = argmax [Q(s_i) + c_uct * sqrt(sum N(s_i)) / (1+N(s_i))]\n   ```\n\nThe combination is: MCTS explores the RAG decision tree -> SPRE evaluates nodes with shortest-path bias -> preference pairs are extracted -> DPO trains the LLM. This is a pipeline combination rather than a single algorithmic innovation.\n\n---\n\n## 5. Technical Method Details\n\n### RAG-ProGuide Dataset Construction\n\n- **Source questions:** 3,000 each from PopQA, HotpotQA, 2WikiMultiHopQA\n- **After processing:** 4,603 questions total\n- **MCTS exploration:** For each question, MCTS explores multiple trajectories through the RAG state machine\n- **Reward computation:** F1 score between predicted and ground-truth answers, propagated through tree via SPRE\n- **Preference pair extraction:** At each tree node, children with higher SPRE scores become \"preferred\" and lower become \"dispreferred\"\n- **Filtering:** Pairs with identical responses or reward difference < 0.01 are removed\n\n**Final dataset statistics:**\n- 4,603 questions\n- 13,289 preference pairs total\n- Action type distribution: Query Generation 24.8%, Evidence Extraction 32.4%, Answer Generation 42.8%\n- Retrieval iterations: 1-5 (median 3, avg 2.7)\n- Token length per action: 9-625 (median 60, avg 65.5)\n\n### Training\n\n- **Base model:** Qwen2.5-7B-Instruct\n- **Method:** DPO using LLaMA Factory\n- **Retriever:** BGE (bge-base-en-v1.5) -- STATIC, not trained\n- **Knowledge source:** Wikidump 2018 + dataset-specific corpora\n- **Retrieval:** Top-3 documents per query\n\n### Inference (Algorithm 1)\n\nStructured loop with explicit tags: `&lt;query>`, `&lt;evidence>`, `&lt;answer>` control state transitions. The model autonomously decides when to search vs. when to answer, what query to formulate, which evidence to extract, all via the trained policy.\n\n---\n\n## 6. Key Quantitative Results\n\n### Main results (5 benchmarks, Avg EM / Avg F1):\n\n| Method | Training Data | Avg EM | Avg F1 |\n|--------|--------------|--------|--------|\n| Naive Generation | 0 | 11.5 | 19.4 |\n| Standard RAG | 0 | 24.3 | 32.0 |\n| Search-R1 | 90k | 32.8 | 40.7 |\n| AutoRAG | 10k | 29.5 | 36.9 |\n| **ReasonRAG** | **5k** | **34.4** | **42.3** |\n\n### Data efficiency claim (the \"18x\" number):\n\nReasonRAG uses 5k training instances vs. Search-R1's 90k = **18x fewer training instances** while achieving **+1.6 points higher Avg EM** and **+1.6 points higher Avg F1**.\n\nMore precisely: ReasonRAG has 13k process-level preference pairs from 5k questions. Search-R1 has ~270k intermediate steps from 90k questions. So in terms of step-level data, ReasonRAG uses ~20x less.\n\n### Per-dataset highlights:\n- **PopQA** (single-hop): 41.5 EM / 46.2 F1 vs. Search-R1's 39.7/44.8\n- **HotpotQA** (multi-hop): 38.4 EM / 48.9 F1 vs. Search-R1's 37.0/47.0\n- **2WikiMultiHopQA** (multi-hop): 43.6 EM / 50.4 F1 vs. Search-R1's 41.4/48.0\n- **Bamboogle** (out-of-domain): 36.0 EM / 45.5 F1 vs. Search-R1's 32.0/43.8\n- **MuSiQue** (out-of-domain): 12.8 EM / 20.6 F1 vs. Search-R1's 14.6/19.9\n\nNote: ReasonRAG loses to Search-R1 on MuSiQue EM (12.8 vs 14.6) but wins on F1 (20.6 vs 19.9).\n\n### Ablation (optimization strategy, Table 3):\n- Base model: 22.0 Avg EM / 32.8 Avg F1\n- SFT on process data: 23.9 / 32.0 (overfits on multi-hop, hurts single-hop)\n- RL-ORL with 5k data (outcome reward): 21.3 / 28.9 (WORSE than base -- outcome reward with small data fails)\n- RL-ORL with 10k data: 32.0 / 39.9 (competitive but still below)\n- **RL-PRL (ReasonRAG):** 34.5 / 42.3\n\nThis ablation is the strongest evidence: with the SAME 5k data, outcome RL completely fails (21.3 EM) while process RL succeeds (34.5 EM). Outcome RL needs 10k+ data to even approach process RL's results.\n\n### Training efficiency:\nReasonRAG converges faster in GPU hours than Search-R1, especially on multi-hop tasks.\n\n---\n\n## 7. Limitations\n\n**Explicitly stated by the authors (Appendix H):**\n1. **Higher per-sample annotation cost:** Process-level data rollout via MCTS is more time-consuming per sample than outcome-level data collection (though fewer samples are needed overall).\n2. **Safety concerns:** Potential risk of generating harmful content if external knowledge sources are not properly curated.\n\n**Implicit/unstated limitations I identify:**\n3. **Only tested at 7B scale** -- scalability to larger models (70B+) is undemonstrated.\n4. **Static retriever** -- the retriever (BGE) is never trained. The system only improves the LLM's ability to USE retrieval, not the retrieval quality itself.\n5. **Wikipedia-only knowledge base** -- Wikidump 2018 is the knowledge source; performance on domain-specific or more current corpora is unknown.\n6. **Closed-book QA benchmarks only** -- all five benchmarks are factoid QA. No evaluation on long-form generation, summarization, or open-ended tasks.\n7. **DPO rather than online RL** -- they use offline preference optimization (DPO) rather than online RL (PPO/GRPO). This means the policy cannot improve beyond the quality of the MCTS-generated preference data.\n8. **MCTS requires a capable base model** -- the MCTS exploration uses the base Qwen2.5-7B model to generate rollouts. If the base model is weak, the exploration quality will be poor, creating a bootstrapping problem.\n9. **The \"18x\" claim is about instance count, not compute** -- MCTS data generation is expensive. The total compute (data generation + training) comparison is not clearly presented.\n10. **MuSiQue underperformance** -- ReasonRAG loses to Search-R1 on MuSiQue EM, suggesting the process reward may not generalize equally well to all multi-hop reasoning patterns.\n\n---\n\n## 8. CRITICAL DISTINCTION: What Gets Trained?\n\n**ReasonRAG trains ONLY the LLM (Qwen2.5-7B-Instruct). The retriever is NOT trained.**\n\nEvidence:\n- The retriever is BGE (bge-base-en-v1.5), used as a static component across ALL methods\n- The DPO objective (Equation 3) optimizes p_theta -- the LLM's parameters\n- Algorithm 1 shows the retriever R is called as a black-box: `docs <- R(q)`\n- No gradient flows through the retriever at any point\n- The LLM is trained to: (a) decide WHEN to retrieve, (b) formulate WHAT query to send, (c) extract WHICH evidence from retrieved docs, and (d) generate the final answer\n\n**This is a critical distinction for your research:** The retriever remains frozen. All improvements come from teaching the LLM to be a better \"user\" of the retriever -- better query formulation, better evidence selection, better answer synthesis. The retrieval quality itself is unchanged.\n\n---\n\n## 9. Related/Follow-up Work\n\nTwo notable follow-ups that address similar themes:\n\n- **HiPRAG** (arXiv 2510.07794): Also uses process rewards for agentic RAG but with a \"hierarchical\" reward structure. Focuses on over-search and under-search behaviors. Reports 65.4% (3B) and 67.2% (7B) average accuracy.\n\n- **Search-P1** (arXiv 2602.22576): Introduces \"path-centric reward shaping\" -- evaluates structural quality of reasoning trajectories via order-agnostic step coverage and dual-track scoring. Claims +7.7 average accuracy gain. Takes a different approach to intermediate rewards than ReasonRAG.\n\n---\n\n## 10. Assessment for Your Research\n\n**Strengths relevant to your work:**\n- Clean demonstration that process rewards >> outcome rewards for RAG (the 5k vs. 90k comparison is compelling)\n- The three-stage decomposition (query/evidence/answer) is a natural and reusable framework\n- MCTS for automatic preference data construction avoids human annotation costs\n- The SPRE shortest-path bias is a simple but effective inductive bias for RAG\n\n**Weaknesses to be aware of:**\n- The absolute performance improvements over Search-R1 are modest (+1.6 EM/F1 on average)\n- The \"18x data efficiency\" headline obscures that MCTS data generation is computationally expensive\n- DPO is a one-shot offline method -- no iterative online improvement\n- Retriever is frozen -- a joint LLM+retriever training approach could potentially do better\n- Only factoid QA benchmarks; unclear how this transfers to more complex RAG tasks\n\nSources:\n- [arXiv Paper](https://arxiv.org/abs/2505.14069)\n- [OpenReview](https://openreview.net/forum?id=h3LlJ6Bh4S)\n- [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/116682)\n- [GitHub Repository](https://github.com/Applied-Machine-Learning-Lab/ReasonRAG)\n- [Moonlight Literature Review](https://www.themoonlight.io/en/review/process-vs-outcome-reward-which-is-better-for-agentic-rag-reinforcement-learning)\n- [HiPRAG (follow-up)](https://arxiv.org/abs/2510.07794)\n- [Search-P1 (follow-up)](https://arxiv.org/abs/2602.22576)"
      }
    ],
    "totalDurationMs": 259811,
    "totalTokens": 30608,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1101,
      "cache_read_input_tokens": 25398,
      "output_tokens": 4108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1101
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4108,
          "cache_read_input_tokens": 25398,
          "cache_creation_input_tokens": 1101,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1101,
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
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "3ea9a5f9-0938-4df7-8a24-ba18381283d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
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
  "leafUuid": "172fe256-2afe-418b-b5c5-f692b1595825",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze papers for AAAI 2026 reasoning-intensive retrieval",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Tool result

_source line 28 · 2026-05-30T06:32:58.231Z_

<details><summary>↩ Tool result · `toolu_01YMWVmxfmq3dP9jEMEjTMqb`</summary>

```text
I now have comprehensive information from multiple sources. Here is the complete structured analysis:

---

# BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval

**Authors:** Hongjin Su, Howard Yen, Mengzhou Xia, Weijia Shi, Niklas Muennighoff, Han-yu Wang, Haisu Liu, Quan Shi, Zachary S. Siegel, Michael Tang, Ruoxi Sun, Jinsung Yoon, Sercan O. Arik, Danqi Chen, Tao Yu

**Venue:** ICLR 2025 (Spotlight). arXiv: 2407.12883. OpenReview ID: ykuc5q381b.

---

## 1. THE GAP THEY IDENTIFIED AND HOW

**The Gap:** Existing retrieval benchmarks (BEIR, MTEB) primarily consist of information-seeking queries where keyword or semantic-based retrieval is sufficient. These benchmarks do not test whether retrieval systems can handle queries that require deep analytical reasoning to identify relevant documents -- situations where the connection between query and document is not detectable through surface-level lexical or semantic matching.

**How They Identified It:** They observed that the leading model on the MTEB leaderboard (SFR-Embedding-Mistral) achieves 59.0 nDCG@10 on standard benchmarks but plummets to only 18.3 nDCG@10 on BRIGHT -- a **40.7-point drop** (59.0 - 18.3 = 40.7). This gap is not an explicit "human vs. model" gap but rather a **cross-benchmark transfer gap** that reveals the fundamental inability of current retrievers to handle reasoning-intensive queries. The best model overall (Qwen) achieved only 22.1 nDCG@10 on BRIGHT.

**Concrete Observation:** Many complex real-world queries require understanding underlying algorithms, theoretical principles, or syntactical nuances to identify that a document is relevant. For example, a math competition problem might require recognizing that a specific theorem applies, even though there is zero keyword overlap between the problem statement and the theorem.

---

## 2. KEY INSIGHT OTHERS MISSED

**Core Insight:** The retrieval community had been optimizing for and evaluating on benchmarks where relevance can be determined by keyword overlap or semantic similarity. But a large class of real-world retrieval needs -- connecting a bug description to niche documentation, linking a math problem to the applicable theorem, translating observational phenomena to scientific concepts -- requires **multi-step reasoning** that current embedding models and sparse retrievers fundamentally cannot perform.

**Secondary Insight:** Incorporating explicit chain-of-thought reasoning into the retrieval query (by prompting an LLM to reason about the query before retrieval) improves performance by up to 12.2 nDCG@10 points, demonstrating that the bottleneck is reasoning, not representation capacity.

---

## 3. PROBLEM FORMULATION -- HOW IT DIFFERS FROM PRIOR WORK

BRIGHT introduces a **three-level retrieval taxonomy**:
- **Level 1:** Keyword matching (lexical overlap only)
- **Level 2:** Semantic query-document matching (what BEIR/MTEB test)
- **Level 3:** "Reasoning-Intensive Retrieval" -- requires deduced reasoning chains not explicitly stated in either query or document

Unlike BEIR and MTEB, which define relevance via topical similarity or factual containment, BRIGHT defines relevance through **reasoning connection**: a document is relevant if and only if reasoning about it provides the information needed to address the query, even when there is minimal surface-level similarity.

**Distinction from RAR-b:** The authors differentiate from RAR-b (another reasoning benchmark) by noting BRIGHT uses naturally occurring human data, has longer and more realistic queries (averaging ~498 tokens), and covers more diverse domains.

---

## 4. EXISTING TECHNIQUES ADAPTED/COMBINED

**Technique 1 -- LLM Query Augmentation (Chain-of-Thought Retrieval):** They adapted chain-of-thought prompting from the reasoning literature and applied it to retrieval. Instead of using the raw query, they prompt LLMs (GPT-4, Llama-3-70B, Claude-3-Opus, Gemini-1.0) to:
1. Articulate the core problem in the query
2. Enumerate required information elements
3. Draft concise reasoning rationales

The LLM-generated reasoning then **replaces** the original query for retrieval. This is conceptually related to traditional query expansion but uses generative reasoning rather than keyword expansion.

**Technique 2 -- LLM-based Reranking:** After initial retrieval, they use LLMs (GPT-4, Gemini) to rerank candidate documents, yielding up to 3.1 additional nDCG@10 points.

**Technique 3 -- Continued Pre-training:** They attempted fine-tuning retrievers on BRIGHT-like data from StackExchange, but this "fails to improve the performance," validating that the benchmark tests reasoning capability rather than domain familiarity.

---

## 5. TECHNICAL METHOD -- BENCHMARK CONSTRUCTION

### Data Sources and the 12 Datasets

| Domain | Source | # Queries | Category |
|--------|--------|-----------|----------|
| Biology | StackExchange | 103 | Natural Science |
| Earth Science | StackExchange | 116 | Natural Science |
| Economics | StackExchange | 103 | Social Science |
| Psychology | StackExchange | 101 | Social Science |
| Robotics | StackExchange | 101 | Engineering |
| StackOverflow | StackExchange | 117 | Programming |
| Sustainable Living | StackExchange | 108 | Interdisciplinary |
| LeetCode | LeetCode | 142 | Programming/Algorithms |
| Pony | Pony language docs | 112 | Programming |
| AoPS | Art of Problem Solving | 111 | Mathematics |
| TheoremQA (questions) | TheoremQA | 194 | Mathematics |
| TheoremQA (theorems) | TheoremQA | 76 | Mathematics |
| **Total** | | **~1,384** | |

### Construction Pipeline

**For StackExchange datasets (7 datasets):**
- Queries are real user questions from StackExchange communities
- Relevant documents are **web pages linked in accepted/highly-voted answers** -- this is the key: the answer cites a URL, and the content at that URL is the relevant document
- Web pages were split into passages for the short-document corpus
- Relevance was validated through a **rigorous multi-annotator process** -- only documents unanimously agreed upon by annotators were retained as positives
- Hard negatives were generated via Google keyword search, then verified by humans to ensure semantic similarity without actual relevance

**For Coding/Math datasets (5 datasets):**
- Relevance is inherently defined: LeetCode problems map to the algorithms/data structures needed to solve them; math competition problems (AoPS) map to the theorems required
- Pony language queries require identifying relevant documentation for a rare programming language
- TheoremQA links math questions to applicable theorems

### Document Corpus
- Short documents: ~1.33M documents (passages split from web pages)
- Long documents: ~5,650 full web pages/articles (averaging up to 40K tokens)
- Documents include blogs, news articles, reports, documentation

### Quality Control
- Gold reasoning annotations accompany each query (human-written explanations of why the document is relevant)
- The `excluded_ids` field prevents data leakage for coding/math datasets
- Multiple gold documents per query (1-19 for short docs, 1-4 for long docs)

---

## 6. EVALUATION PROTOCOL

**Primary Metrics:**
- Short documents: **nDCG@10** (normalized Discounted Cumulative Gain at rank 10), averaged across 12 datasets
- Long documents: **Recall@1**, averaged across 8 datasets

**Models Evaluated (13 retrieval models):**
Including BM25 (sparse), SBERT, E5, GritLM, Instructor-XL, Qwen, OpenAI embeddings, Cohere, SFR-Embedding-Mistral, and others of varying sizes and architectures.

**Reasoning Augmentation Variants:**
- Each query is augmented with reasoning from 5 different LLMs: GPT-4, Claude-3-Opus, Gemini-1.0, Llama-3-70B, and GritLM
- These are stored as separate dataset subsets (1,380 rows each)

**LLM Evaluator for QA:**
- Downstream QA evaluation using LLM assessors, though this was found to have 40-48% deviation from human judgment

---

## 7. KEY QUANTITATIVE RESULTS

### The 40.7-Point Gap
- SFR-Embedding-Mistral: **59.0 nDCG@10 on MTEB** vs. **18.3 nDCG@10 on BRIGHT** = **40.7-point drop**
- This demonstrates that BRIGHT tests a fundamentally different retrieval capability

### Model Performance Comparison (nDCG@10 on BRIGHT)

| Model | BRIGHT nDCG@10 | MTEB nDCG@10 |
|-------|---------------|--------------|
| SFR-Embedding-Mistral | 18.3 (or 18.0) | 59.0 |
| Qwen (best baseline) | 22.1 | 56.2 |
| BM25 | 14.3-14.8 | 41.6 |
| Instructor-XL | 18.9 | -- |
| Best model overall | ~22.1 | -- |

### Reasoning Augmentation Results
- BM25 with GPT-4 reasoning: **14.8 --> 26.5 nDCG@10** (+11.7 points)
- Maximum improvement from reasoning: **+12.2 points**
- LLM reranking on top of reasoning: additional **+3.1 points**
- Even with reasoning augmentation, the best model stays **below 30 nDCG@10**

### Long-Document Retrieval (Recall@1)
- Best model: 27.8

### Downstream QA
- Incorporating retrieved documents from the top-performing retriever boosts QA performance by over **6.6 points**

### Current Leaderboard (as of 2026, post-publication)
Top submissions now reach much higher with specialized reasoning retrieval:
- Mira-Reasoning-Retrieval: 66.9 nDCG@10
- INF-X-Retriever: 63.4
- RakanEmbed4B: 52.4

---

## 8. REVIEWER FEEDBACK (OpenReview, ICLR 2025)

### Decision: **Accept (Spotlight)** -- January 22, 2025

### Reviewer Scores

| Reviewer | Rating | Confidence |
|----------|--------|------------|
| Reviewer 8SYb | 10 | 4 |
| Reviewer XNdW | 8 | 4 |
| Reviewer aDWB | 6 | 4 |
| Reviewer v2W5 | 6 --> 8 (raised after discussion) | 3 |
| Reviewer 2e76 | 6 | 4 |

### PRAISE (Strengths identified by reviewers)

1. **"Solid, non-trivial, original, and a timely contribution"** (aDWB) -- The benchmark addresses a genuine gap that the community needs.

2. **"Challenging and diverse benchmark with potential to drive research"** (XNdW) -- Thorough data collection pipeline with domain-expert verification. The diversity across 12 domains is valuable.

3. **High-quality construction:** Multi-annotator validation, expert verification, human-collected authentic data (multiple reviewers).

4. **Comprehensive experiments:** 13 retrieval models evaluated with extensive ablations. Well-organized presentation with detailed appendices.

5. **Practical relevance:** Reflects realistic retrieval scenarios requiring reasoning, unlike synthetic benchmarks.

6. **Downstream validation:** Chain-of-thought reasoning demonstrably improves performance, proving the benchmark tests what it claims to test.

7. **Resistance to gaming:** Continued pre-training on benchmark-similar data fails to improve performance, validating that BRIGHT tests reasoning capability, not domain knowledge.

### CRITICISM (Weaknesses identified by reviewers)

1. **Non-unified definition of reasoning** (2e76, primary concern): The definition of "relevance" varies across domains. Reviewer 2e76 felt the benchmark "feels stretched" without shared reasoning properties. Without a common thread, improvements are "quite vague" rather than interpretable. Authors responded by categorizing four reasoning types (deductive, analogical, causal, analytical), which partially addressed but did not fully resolve this concern.

2. **Small dataset size** (multiple reviewers): Only 1,384 test instances across 12 domains was "relatively small." However, reviewers acknowledged that 30-50 queries per domain is typical in IR evaluation.

3. **Limited novelty in approaches** (multiple reviewers): LLM-based query expansion resembles traditional query expansion methods. The methodological contribution beyond benchmark construction was questioned.

4. **Missing analyses** (XNdW): Lacks quantitative error analysis of where gold documents rank. Missing qualitative failure analysis with oracle documents. Insufficient explanation of why strong LLMs fail at ranking.

5. **Annotation concerns** (aDWB): Unclear annotator guidelines, recruitment procedures, and compensation details. Quality variance between StackExchange and coding/math components.

6. **Licensing concerns** (aDWB): Questions about fair use compliance for LeetCode and AoPS data.

7. **Metric concerns** (aDWB): nDCG-based metrics may not suit RAG evaluation settings. LLM evaluator has 40-48% deviation from human judgment.

8. **Inconsistent results** (v2W5): High QA performance despite poor retrieval seems contradictory. Inconsistent performance on coding/theorem datasets.

9. **Missing comparison** (v2W5): Should compare more explicitly to RAR-b benchmark.

### META-REVIEW (Area Chair)
- **Assessment:** "Generally strong" work that enables new solutions. Timely core idea advancing existing datasets in interesting ways.
- **Key acknowledgment:** "Nobody in the field really has good definitions for 'reasoning'" -- the definition issue is a field-wide limitation, not a flaw unique to BRIGHT.
- **Verdict:** Work is strong on enabling new retrieval solutions, even if the reasoning taxonomy could be sharper.

---

## 9. FOUR REASONING TYPES (from Author Rebuttal)

1. **Deductive Reasoning:** Applying general principles to specific problems (e.g., connecting a math problem to the theorem it requires)
2. **Analogical Reasoning:** Identifying parallel underlying logic across different scenarios (e.g., recognizing structural similarity between a StackExchange question and an article about a different but analogous topic)
3. **Causal Reasoning:** Identifying cause-and-effect relationships between query and document
4. **Analytical Reasoning:** Applying critical knowledge to explain confusion in the query

---

## 10. KEY DIFFERENTIATORS FROM BEIR/MTEB

| Aspect | BEIR/MTEB | BRIGHT |
|--------|-----------|--------|
| Query type | Information-seeking | Reasoning-intensive |
| Relevance signal | Keyword/semantic overlap | Reasoning connection |
| Query length | Short (~10-30 tokens) | Long (~498 tokens avg) |
| Retrieval level | Level 1-2 (keyword/semantic) | Level 3 (reasoning) |
| Data source | Curated/synthetic | Naturally occurring human data |
| Best model performance | ~59 nDCG@10 | ~22 nDCG@10 |
| Reasoning augmentation benefit | Minimal | Up to +12.2 points |

---

## SUMMARY OF FINDINGS

The BRIGHT paper makes its core contribution as a **benchmark, not a method**. The key findings are:

1. There is a massive (40.7-point) performance gap when SOTA retrievers move from standard benchmarks to reasoning-intensive queries.
2. The gap is caused by a fundamental limitation: current retrieval models match surface patterns, not reasoning connections.
3. Reasoning augmentation (prompting LLMs to reason about queries before retrieval) partially closes the gap (+12.2 points) but does not solve it (best score still under 30 at time of publication).
4. Fine-tuning on similar data does not help, confirming the benchmark tests reasoning capability.
5. The benchmark has already catalyzed significant progress: the leaderboard now shows models reaching 66.9 nDCG@10, driven by specialized reasoning-retrieval architectures developed after the benchmark's release.

agentId: a8ac74896900c2f74 (use SendMessage with to: 'a8ac74896900c2f74' to continue this agent)
&lt;usage>total_tokens: 33259
tool_uses: 26
duration_ms: 301601&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "767d7aed-a40e-4a0a-b18d-308a63c5dc27",
  "isSidechain": false,
  "promptId": "bbbe4bf2-b0a9-43d5-8f54-a157f509f7eb",
  "type": "user",
  "uuid": "92ed4536-ae66-483c-884f-f5ef33dea93b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval\" by Hongjin Su et al. (ICLR 2025 Spotlight), arxiv URL: https://arxiv.org/abs/2407.12883\n\nSteps:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full paper PDF on arxiv (https://arxiv.org/pdf/2407.12883)\n3. Search for and read OpenReview reviews for this paper (it's ICLR 2025 spotlight)\n\nFor each, extract:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- Reviewer praise and criticism (from OpenReview)\n- Technical method details (how they constructed the benchmark, what evaluation protocol)\n- Key quantitative results (especially the 40.7-point gap)\n\nBe thorough and specific. Return all findings in a structured format.",
    "agentId": "a8ac74896900c2f74",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information from multiple sources. Here is the complete structured analysis:\n\n---\n\n# BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval\n\n**Authors:** Hongjin Su, Howard Yen, Mengzhou Xia, Weijia Shi, Niklas Muennighoff, Han-yu Wang, Haisu Liu, Quan Shi, Zachary S. Siegel, Michael Tang, Ruoxi Sun, Jinsung Yoon, Sercan O. Arik, Danqi Chen, Tao Yu\n\n**Venue:** ICLR 2025 (Spotlight). arXiv: 2407.12883. OpenReview ID: ykuc5q381b.\n\n---\n\n## 1. THE GAP THEY IDENTIFIED AND HOW\n\n**The Gap:** Existing retrieval benchmarks (BEIR, MTEB) primarily consist of information-seeking queries where keyword or semantic-based retrieval is sufficient. These benchmarks do not test whether retrieval systems can handle queries that require deep analytical reasoning to identify relevant documents -- situations where the connection between query and document is not detectable through surface-level lexical or semantic matching.\n\n**How They Identified It:** They observed that the leading model on the MTEB leaderboard (SFR-Embedding-Mistral) achieves 59.0 nDCG@10 on standard benchmarks but plummets to only 18.3 nDCG@10 on BRIGHT -- a **40.7-point drop** (59.0 - 18.3 = 40.7). This gap is not an explicit \"human vs. model\" gap but rather a **cross-benchmark transfer gap** that reveals the fundamental inability of current retrievers to handle reasoning-intensive queries. The best model overall (Qwen) achieved only 22.1 nDCG@10 on BRIGHT.\n\n**Concrete Observation:** Many complex real-world queries require understanding underlying algorithms, theoretical principles, or syntactical nuances to identify that a document is relevant. For example, a math competition problem might require recognizing that a specific theorem applies, even though there is zero keyword overlap between the problem statement and the theorem.\n\n---\n\n## 2. KEY INSIGHT OTHERS MISSED\n\n**Core Insight:** The retrieval community had been optimizing for and evaluating on benchmarks where relevance can be determined by keyword overlap or semantic similarity. But a large class of real-world retrieval needs -- connecting a bug description to niche documentation, linking a math problem to the applicable theorem, translating observational phenomena to scientific concepts -- requires **multi-step reasoning** that current embedding models and sparse retrievers fundamentally cannot perform.\n\n**Secondary Insight:** Incorporating explicit chain-of-thought reasoning into the retrieval query (by prompting an LLM to reason about the query before retrieval) improves performance by up to 12.2 nDCG@10 points, demonstrating that the bottleneck is reasoning, not representation capacity.\n\n---\n\n## 3. PROBLEM FORMULATION -- HOW IT DIFFERS FROM PRIOR WORK\n\nBRIGHT introduces a **three-level retrieval taxonomy**:\n- **Level 1:** Keyword matching (lexical overlap only)\n- **Level 2:** Semantic query-document matching (what BEIR/MTEB test)\n- **Level 3:** \"Reasoning-Intensive Retrieval\" -- requires deduced reasoning chains not explicitly stated in either query or document\n\nUnlike BEIR and MTEB, which define relevance via topical similarity or factual containment, BRIGHT defines relevance through **reasoning connection**: a document is relevant if and only if reasoning about it provides the information needed to address the query, even when there is minimal surface-level similarity.\n\n**Distinction from RAR-b:** The authors differentiate from RAR-b (another reasoning benchmark) by noting BRIGHT uses naturally occurring human data, has longer and more realistic queries (averaging ~498 tokens), and covers more diverse domains.\n\n---\n\n## 4. EXISTING TECHNIQUES ADAPTED/COMBINED\n\n**Technique 1 -- LLM Query Augmentation (Chain-of-Thought Retrieval):** They adapted chain-of-thought prompting from the reasoning literature and applied it to retrieval. Instead of using the raw query, they prompt LLMs (GPT-4, Llama-3-70B, Claude-3-Opus, Gemini-1.0) to:\n1. Articulate the core problem in the query\n2. Enumerate required information elements\n3. Draft concise reasoning rationales\n\nThe LLM-generated reasoning then **replaces** the original query for retrieval. This is conceptually related to traditional query expansion but uses generative reasoning rather than keyword expansion.\n\n**Technique 2 -- LLM-based Reranking:** After initial retrieval, they use LLMs (GPT-4, Gemini) to rerank candidate documents, yielding up to 3.1 additional nDCG@10 points.\n\n**Technique 3 -- Continued Pre-training:** They attempted fine-tuning retrievers on BRIGHT-like data from StackExchange, but this \"fails to improve the performance,\" validating that the benchmark tests reasoning capability rather than domain familiarity.\n\n---\n\n## 5. TECHNICAL METHOD -- BENCHMARK CONSTRUCTION\n\n### Data Sources and the 12 Datasets\n\n| Domain | Source | # Queries | Category |\n|--------|--------|-----------|----------|\n| Biology | StackExchange | 103 | Natural Science |\n| Earth Science | StackExchange | 116 | Natural Science |\n| Economics | StackExchange | 103 | Social Science |\n| Psychology | StackExchange | 101 | Social Science |\n| Robotics | StackExchange | 101 | Engineering |\n| StackOverflow | StackExchange | 117 | Programming |\n| Sustainable Living | StackExchange | 108 | Interdisciplinary |\n| LeetCode | LeetCode | 142 | Programming/Algorithms |\n| Pony | Pony language docs | 112 | Programming |\n| AoPS | Art of Problem Solving | 111 | Mathematics |\n| TheoremQA (questions) | TheoremQA | 194 | Mathematics |\n| TheoremQA (theorems) | TheoremQA | 76 | Mathematics |\n| **Total** | | **~1,384** | |\n\n### Construction Pipeline\n\n**For StackExchange datasets (7 datasets):**\n- Queries are real user questions from StackExchange communities\n- Relevant documents are **web pages linked in accepted/highly-voted answers** -- this is the key: the answer cites a URL, and the content at that URL is the relevant document\n- Web pages were split into passages for the short-document corpus\n- Relevance was validated through a **rigorous multi-annotator process** -- only documents unanimously agreed upon by annotators were retained as positives\n- Hard negatives were generated via Google keyword search, then verified by humans to ensure semantic similarity without actual relevance\n\n**For Coding/Math datasets (5 datasets):**\n- Relevance is inherently defined: LeetCode problems map to the algorithms/data structures needed to solve them; math competition problems (AoPS) map to the theorems required\n- Pony language queries require identifying relevant documentation for a rare programming language\n- TheoremQA links math questions to applicable theorems\n\n### Document Corpus\n- Short documents: ~1.33M documents (passages split from web pages)\n- Long documents: ~5,650 full web pages/articles (averaging up to 40K tokens)\n- Documents include blogs, news articles, reports, documentation\n\n### Quality Control\n- Gold reasoning annotations accompany each query (human-written explanations of why the document is relevant)\n- The `excluded_ids` field prevents data leakage for coding/math datasets\n- Multiple gold documents per query (1-19 for short docs, 1-4 for long docs)\n\n---\n\n## 6. EVALUATION PROTOCOL\n\n**Primary Metrics:**\n- Short documents: **nDCG@10** (normalized Discounted Cumulative Gain at rank 10), averaged across 12 datasets\n- Long documents: **Recall@1**, averaged across 8 datasets\n\n**Models Evaluated (13 retrieval models):**\nIncluding BM25 (sparse), SBERT, E5, GritLM, Instructor-XL, Qwen, OpenAI embeddings, Cohere, SFR-Embedding-Mistral, and others of varying sizes and architectures.\n\n**Reasoning Augmentation Variants:**\n- Each query is augmented with reasoning from 5 different LLMs: GPT-4, Claude-3-Opus, Gemini-1.0, Llama-3-70B, and GritLM\n- These are stored as separate dataset subsets (1,380 rows each)\n\n**LLM Evaluator for QA:**\n- Downstream QA evaluation using LLM assessors, though this was found to have 40-48% deviation from human judgment\n\n---\n\n## 7. KEY QUANTITATIVE RESULTS\n\n### The 40.7-Point Gap\n- SFR-Embedding-Mistral: **59.0 nDCG@10 on MTEB** vs. **18.3 nDCG@10 on BRIGHT** = **40.7-point drop**\n- This demonstrates that BRIGHT tests a fundamentally different retrieval capability\n\n### Model Performance Comparison (nDCG@10 on BRIGHT)\n\n| Model | BRIGHT nDCG@10 | MTEB nDCG@10 |\n|-------|---------------|--------------|\n| SFR-Embedding-Mistral | 18.3 (or 18.0) | 59.0 |\n| Qwen (best baseline) | 22.1 | 56.2 |\n| BM25 | 14.3-14.8 | 41.6 |\n| Instructor-XL | 18.9 | -- |\n| Best model overall | ~22.1 | -- |\n\n### Reasoning Augmentation Results\n- BM25 with GPT-4 reasoning: **14.8 --> 26.5 nDCG@10** (+11.7 points)\n- Maximum improvement from reasoning: **+12.2 points**\n- LLM reranking on top of reasoning: additional **+3.1 points**\n- Even with reasoning augmentation, the best model stays **below 30 nDCG@10**\n\n### Long-Document Retrieval (Recall@1)\n- Best model: 27.8\n\n### Downstream QA\n- Incorporating retrieved documents from the top-performing retriever boosts QA performance by over **6.6 points**\n\n### Current Leaderboard (as of 2026, post-publication)\nTop submissions now reach much higher with specialized reasoning retrieval:\n- Mira-Reasoning-Retrieval: 66.9 nDCG@10\n- INF-X-Retriever: 63.4\n- RakanEmbed4B: 52.4\n\n---\n\n## 8. REVIEWER FEEDBACK (OpenReview, ICLR 2025)\n\n### Decision: **Accept (Spotlight)** -- January 22, 2025\n\n### Reviewer Scores\n\n| Reviewer | Rating | Confidence |\n|----------|--------|------------|\n| Reviewer 8SYb | 10 | 4 |\n| Reviewer XNdW | 8 | 4 |\n| Reviewer aDWB | 6 | 4 |\n| Reviewer v2W5 | 6 --> 8 (raised after discussion) | 3 |\n| Reviewer 2e76 | 6 | 4 |\n\n### PRAISE (Strengths identified by reviewers)\n\n1. **\"Solid, non-trivial, original, and a timely contribution\"** (aDWB) -- The benchmark addresses a genuine gap that the community needs.\n\n2. **\"Challenging and diverse benchmark with potential to drive research\"** (XNdW) -- Thorough data collection pipeline with domain-expert verification. The diversity across 12 domains is valuable.\n\n3. **High-quality construction:** Multi-annotator validation, expert verification, human-collected authentic data (multiple reviewers).\n\n4. **Comprehensive experiments:** 13 retrieval models evaluated with extensive ablations. Well-organized presentation with detailed appendices.\n\n5. **Practical relevance:** Reflects realistic retrieval scenarios requiring reasoning, unlike synthetic benchmarks.\n\n6. **Downstream validation:** Chain-of-thought reasoning demonstrably improves performance, proving the benchmark tests what it claims to test.\n\n7. **Resistance to gaming:** Continued pre-training on benchmark-similar data fails to improve performance, validating that BRIGHT tests reasoning capability, not domain knowledge.\n\n### CRITICISM (Weaknesses identified by reviewers)\n\n1. **Non-unified definition of reasoning** (2e76, primary concern): The definition of \"relevance\" varies across domains. Reviewer 2e76 felt the benchmark \"feels stretched\" without shared reasoning properties. Without a common thread, improvements are \"quite vague\" rather than interpretable. Authors responded by categorizing four reasoning types (deductive, analogical, causal, analytical), which partially addressed but did not fully resolve this concern.\n\n2. **Small dataset size** (multiple reviewers): Only 1,384 test instances across 12 domains was \"relatively small.\" However, reviewers acknowledged that 30-50 queries per domain is typical in IR evaluation.\n\n3. **Limited novelty in approaches** (multiple reviewers): LLM-based query expansion resembles traditional query expansion methods. The methodological contribution beyond benchmark construction was questioned.\n\n4. **Missing analyses** (XNdW): Lacks quantitative error analysis of where gold documents rank. Missing qualitative failure analysis with oracle documents. Insufficient explanation of why strong LLMs fail at ranking.\n\n5. **Annotation concerns** (aDWB): Unclear annotator guidelines, recruitment procedures, and compensation details. Quality variance between StackExchange and coding/math components.\n\n6. **Licensing concerns** (aDWB): Questions about fair use compliance for LeetCode and AoPS data.\n\n7. **Metric concerns** (aDWB): nDCG-based metrics may not suit RAG evaluation settings. LLM evaluator has 40-48% deviation from human judgment.\n\n8. **Inconsistent results** (v2W5): High QA performance despite poor retrieval seems contradictory. Inconsistent performance on coding/theorem datasets.\n\n9. **Missing comparison** (v2W5): Should compare more explicitly to RAR-b benchmark.\n\n### META-REVIEW (Area Chair)\n- **Assessment:** \"Generally strong\" work that enables new solutions. Timely core idea advancing existing datasets in interesting ways.\n- **Key acknowledgment:** \"Nobody in the field really has good definitions for 'reasoning'\" -- the definition issue is a field-wide limitation, not a flaw unique to BRIGHT.\n- **Verdict:** Work is strong on enabling new retrieval solutions, even if the reasoning taxonomy could be sharper.\n\n---\n\n## 9. FOUR REASONING TYPES (from Author Rebuttal)\n\n1. **Deductive Reasoning:** Applying general principles to specific problems (e.g., connecting a math problem to the theorem it requires)\n2. **Analogical Reasoning:** Identifying parallel underlying logic across different scenarios (e.g., recognizing structural similarity between a StackExchange question and an article about a different but analogous topic)\n3. **Causal Reasoning:** Identifying cause-and-effect relationships between query and document\n4. **Analytical Reasoning:** Applying critical knowledge to explain confusion in the query\n\n---\n\n## 10. KEY DIFFERENTIATORS FROM BEIR/MTEB\n\n| Aspect | BEIR/MTEB | BRIGHT |\n|--------|-----------|--------|\n| Query type | Information-seeking | Reasoning-intensive |\n| Relevance signal | Keyword/semantic overlap | Reasoning connection |\n| Query length | Short (~10-30 tokens) | Long (~498 tokens avg) |\n| Retrieval level | Level 1-2 (keyword/semantic) | Level 3 (reasoning) |\n| Data source | Curated/synthetic | Naturally occurring human data |\n| Best model performance | ~59 nDCG@10 | ~22 nDCG@10 |\n| Reasoning augmentation benefit | Minimal | Up to +12.2 points |\n\n---\n\n## SUMMARY OF FINDINGS\n\nThe BRIGHT paper makes its core contribution as a **benchmark, not a method**. The key findings are:\n\n1. There is a massive (40.7-point) performance gap when SOTA retrievers move from standard benchmarks to reasoning-intensive queries.\n2. The gap is caused by a fundamental limitation: current retrieval models match surface patterns, not reasoning connections.\n3. Reasoning augmentation (prompting LLMs to reason about queries before retrieval) partially closes the gap (+12.2 points) but does not solve it (best score still under 30 at time of publication).\n4. Fine-tuning on similar data does not help, confirming the benchmark tests reasoning capability.\n5. The benchmark has already catalyzed significant progress: the leaderboard now shows models reaching 66.9 nDCG@10, driven by specialized reasoning-retrieval architectures developed after the benchmark's release."
      }
    ],
    "totalDurationMs": 301601,
    "totalTokens": 33259,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 290,
      "cache_read_input_tokens": 28874,
      "output_tokens": 4094,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 290
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4094,
          "cache_read_input_tokens": 28874,
          "cache_creation_input_tokens": 290,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 290,
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
      "otherToolCount": 26
    }
  },
  "sourceToolAssistantUUID": "767d7aed-a40e-4a0a-b18d-308a63c5dc27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "92ed4536-ae66-483c-884f-f5ef33dea93b",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze papers for AAAI 2026 reasoning-intensive retrieval",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Assistant

_source line 31 · 2026-05-30T06:33:05.398Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research on all 5 papers. Let me synthesize the findings into the required JSON format, ensuring each analysis is under 2000 characters.

Let me draft each analysis:

1. **BRIGHT** - Benchmark paper establishing the 40.7-point gap
2. **SCARLet** - Utility-based retriever training via perturbation attribution
3. **ThinkPRM** - Generative process reward models with long CoT
4. **ReasonRAG** - Process vs outcome rewards for agentic RAG RL


5. **LREM** - Reasoning-augmented embeddings for dense retrieval

I'll carefully craft each entry to be under 2000 characters while maximizing information density.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92ed4536-ae66-483c-884f-f5ef33dea93b",
  "isSidechain": false,
  "requestId": "req_011CbYHYeM9CsX2bgnQpL6Ln",
  "type": "assistant",
  "uuid": "ad91f23e-f03e-4064-b3fb-e4d9ca0aa7e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvA7A2rSY4Qof92g52Z4Hu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 14829,
      "cache_creation_input_tokens": 5951,
      "cache_read_input_tokens": 15796,
      "output_tokens": 3318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 14829,
          "output_tokens": 3318,
          "cache_read_input_tokens": 15796,
          "cache_creation_input_tokens": 5951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5951
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

_source line 32 · 2026-05-30T06:34:33.325Z_

Now I have comprehensive research on all 5 papers. Let me synthesize the findings into the required JSON format with concise, analytical entries under 2000 characters each.

```json
[
  {
    "title": "BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval",
    "venue": "ICLR 2025 (Spotlight)",
    "problem_identification": "Existing retrieval benchmarks (BEIR, MTEB) only test surface-level semantic matching, not reasoning-intensive retrieval where query-document connections require multi-step inference. Identified via observing that SOTA retrievers scoring 59.0 nDCG@10 on MTEB collapse to 18.3 on reasoning-intensive queries — a 40.7-point gap.",
    "key_insight": "Relevance in many real-world retrieval scenarios is mediated by reasoning chains (deductive, analogical, causal, analytical) invisible to embedding similarity, creating a fundamentally different retrieval problem than what current benchmarks measure.",
    "innovation_type": "new_benchmark",
    "method_summary": "Constructed 1,398 queries across 12 domains (StackExchange, LeetCode, AoPS, TheoremQA) where relevant documents are linked in accepted answers but share minimal surface overlap with queries. Gold reasoning annotations explain relevance. Evaluated 13 retrievers plus LLM-based query augmentation (CoT prepended to queries, yielding +12.2 nDCG@10) and reranking (+3.1 additional). Continued pre-training on similar domain data fails to improve performance, validating that the benchmark tests reasoning capability, not domain knowledge.",
    "limitations_and_open_questions": "Non-unified definition of 'reasoning' across domains (reviewer criticism); small size (1,398 queries); LLM evaluator for downstream QA has 40-48% deviation from human judgment. Open question: what retriever architectures can close the gap without LLM-in-the-loop reranking?",
    "building_blocks": ["BRIGHT benchmark (12 datasets, 1.33M short docs, 5.6K long docs)", "Three-level retrieval taxonomy (keyword/semantic/reasoning)", "CoT query augmentation protocol", "Gold reasoning annotations per query", "Leaderboard now showing models reaching 66.9 nDCG@10"],
    "relevance_to_seed": "Defines the exact evaluation target — BRIGHT is where our learned reward model approach must demonstrate gains over heuristic utility-based retrievers, specifically on queries where document relevance requires reasoning rather than semantic similarity."
  },
  {
    "title": "SCARLet: Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models",
    "venue": "EMNLP 2025 (Main)",
    "problem_identification": "Utility-based retriever training suffers from two unaddressed issues: (1) pooling training data across tasks introduces semantic interference that conflates relevance with utility, and (2) evaluating passages independently misses inter-passage synergies critical for multi-hop reasoning. Identified through systematic analysis of why AAR/RePlug underperform expectations.",
    "key_insight": "Single-variable control — training all tasks from a shared context eliminates contextual variation as a confound, ensuring the only differentiating signal between positive/negative passages is their actual downstream utility, not semantic similarity to any particular query.",
    "innovation_type": "new_technique",
    "method_summary": "Constructs shared context via Wikidata entity expansion, then generates multi-task training data from this shared context using GPT-4o. Estimates passage-level utility via modified LIME perturbation attribution: samples 64 binary perturbation vectors (passage inclusion/exclusion), measures generator logit fluctuations on ground-truth tokens, fits ridge regression surrogate to obtain per-passage utility coefficients. Critically removes LIME's semantic distance weighting since utility ≠ semantic proximity. Uses 1D clustering to partition passages into positive/negative sets for contrastive training.",
    "limitations_and_open_questions": "Fails on code domain (up to -11.9 point drops on code retrieval tasks) because Wikipedia-based shared context doesn't transfer. Requires GPT-4o-level synthesizer; GPT-4o-mini fails. 64 perturbation forward passes per instance is computationally expensive. Open question: can the perturbation-based utility estimation be replaced by a learned model that generalizes across domains?",
    "building_blocks": ["Perturbation-based utility attribution (modified LIME)", "Shared context construction via entity expansion", "Utility vs. relevance distinction formalized via logit fluctuation", "Contrastive training on utility-labeled passages"],
    "relevance_to_seed": "Directly motivates our work — SCARLet demonstrates utility-based retriever training works but uses heuristic perturbation attribution; replacing this with a learned reward model that evaluates reasoning chain quality is our core contribution."
  },
  {
    "title": "Process Reward Models That Think (ThinkPRM)",
    "venue": "arXiv 2025 (ICLR 2026 submission, withdrawn)",
    "problem_identification": "Discriminative PRMs require massive step-level labels (~800K in PRM800K), use fixed inference compute, and provide no interpretability. Generative verification (GenRM) existed only for outcome-level assessment with short CoTs. No one had combined long chain-of-thought reasoning with step-level process verification. Identified by observing that reasoning models already possess verification capabilities locked behind formatting/steering issues.",
    "key_insight": "Verification is itself a reasoning task that benefits from extended thinking — fine-tuning reasoning models on just ~1K filtered synthetic verification chains (covering ~8K step labels) unlocks process-level verification that outperforms discriminative PRMs trained on 100× more data.",
    "innovation_type": "combination",
    "method_summary": "Prompts QwQ-32B to generate long verification CoTs for problem-solution pairs from PRM800K. Filters chains requiring: correct format (extractable per-step boxed judgments), alignment with gold step labels, and bounded length (≤4096 tokens). ~20% pass filtering, yielding ~1K chains. Fine-tunes R1-Distill models (1.5B–14B) via full fine-tuning or LoRA. At inference, generates verification CoT then force-decodes 'Is the solution correct?' to extract P(yes)/(P(yes)+P(no)) score. Supports parallel scaling (K independent chains) and sequential scaling (budget forcing).",
    "limitations_and_open_questions": "Overconfident scores clustering near 0/1; autoregressive error propagation (early incorrect judgments bias subsequent steps); significant inference overhead (1K-5K tokens per verification). Math-centric training — cross-domain generalization demonstrated on GPQA/LiveCodeBench but untested on retrieval. Can this verification paradigm be adapted to evaluate document utility for reasoning chains?",
    "building_blocks": ["Generative process verification via long CoT", "Data-efficient PRM training recipe (~1K examples)", "Process-based filtering of synthetic data", "Test-time compute scaling for verification", "Force-decode scoring mechanism"],
    "relevance_to_seed": "Provides the architectural template for our reasoning-utility reward model — ThinkPRM shows that generative PRMs with minimal supervision can evaluate reasoning step quality, which we can adapt to evaluate whether retrieved documents improve reasoning chain quality rather than just final answer correctness."
  },
  {
    "title": "Process vs. Outcome Reward: Which is Better for Agentic RAG Reinforcement Learning (ReasonRAG)",
    "venue": "NeurIPS 2025 (Poster)",
    "problem_identification": "Outcome-supervised RL for agentic RAG (e.g., Search-R1) suffers from low exploration efficiency, gradient conflict (correct early steps penalized alongside late errors), and sparse rewards. Nobody had applied process-level rewards to RAG despite their success in math reasoning. Identified by analyzing three failure modes of outcome RL when applied to multi-step retrieve-reason-answer pipelines.",
    "key_insight": "The RAG pipeline has natural decomposition points (query generation, evidence extraction, answer generation) where process-level rewards can be meaningfully defined, and MCTS with shortest-path reward estimation can automatically construct process-level preference data without human annotation.",
    "innovation_type": "cross_domain",
    "method_summary": "Formulates agentic RAG as a three-stage state machine (Reasoning/Grounding/Terminal). Uses MCTS to explore the RAG decision tree, evaluates nodes via Shortest Path Reward Estimation (SPRE: r = F1 × α^steps, rewarding shorter correct paths). Extracts preference pairs at each stage from MCTS children with differing SPRE scores. Trains Qwen2.5-7B via DPO on 13K preference pairs from 5K questions. Achieves 34.4 Avg EM vs. Search-R1's 32.8 with 18× less training data (5K vs. 90K instances).",
    "limitations_and_open_questions": "CRITICAL: trains only the LLM, NOT the retriever (BGE is frozen). The 18× efficiency claim counts instances, not compute — MCTS data generation is expensive. Only tested on factoid QA benchmarks with Wikipedia; no reasoning-intensive evaluation. Modest absolute gains (+1.6 EM over Search-R1). Can process rewards be redirected to train the retriever itself rather than the LLM's retrieval usage?",
    "building_blocks": ["Three-stage RAG decomposition with per-stage rewards", "MCTS-based automatic preference data construction", "Shortest Path Reward Estimation (SPRE)", "Process vs. outcome reward comparison methodology", "RAG-ProGuide dataset (4.6K questions, 13K preference pairs)"],
    "relevance_to_seed": "Provides strong empirical evidence that process-level rewards outperform outcome-level (binary EM) signals for RAG — directly supporting our thesis that learned reasoning-quality rewards should outperform Agentic-R's binary EM. However, ReasonRAG trains the LLM not the retriever; our work must adapt these process reward insights to retriever training."
  },
  {
    "title": "Large Reasoning Embedding Models: Towards Next-Generation Dense Retrieval Paradigm (LREM)",
    "venue": "arXiv October 2025",
    "problem_identification": "Dense retrievers using direct-embedding paradigm capture statistical co-occurrence rather than deep semantics, failing on queries with significant lexical disparity from targets (alternative queries, negation queries, Q&A-style queries). Identified via e-commerce failure analysis: 'drinks more invigorating than tea' retrieves tea products instead of coffee/Red Bull because the model matches surface 'tea' co-occurrence.",
    "key_insight": "Reasoning and embedding can be unified in a single model — instead of pipeline query-rewriting then separate embedding, the model generates CoT reasoning tokens that are directly consumed by the same model to produce the final embedding vector, creating an end-to-end semantic bridge.",
    "innovation_type": "combination",
    "method_summary": "Built on Qwen2.5-3B with special tokens (&lt;think>, &lt;/think>, &lt;emb>). Stage 1 (Cold Start): joint SFT on CoT generation + InfoNCE contrastive loss on embeddings. Stage 2 (RL): GRPO with three reward signals — format compliance (0.5), length constraint (0.2, CoT ≤16 keyword tokens), and retrieval accuracy (1.0, based on rank of target item in cosine similarity). Training data: 75M query-CoT-item triplets constructed via differential retrieval (keep items found ONLY with CoT-augmented query). Deployed on Taobao since August 2025 with +7-16% improvement in online A/B tests across query categories, at cost of +35ms latency.",
    "limitations_and_open_questions": "CoT constrained to ≤16 keyword tokens for latency (not full natural language reasoning). No evaluation on academic benchmarks (BEIR/MTEB/BRIGHT). Knowledge-intensive queries show slight precision drop (-2.74%). Causal attention required for generation prevents bidirectional attention for embedding. How would full natural-language CoT perform if latency weren't a constraint?",
    "building_blocks": ["Unified reasoning-embedding architecture", "Differential retrieval for training data construction", "GRPO with retrieval-accuracy reward for embedding models", "Two-stage SFT+RL training pipeline", "Production deployment methodology with A/B testing"],
    "relevance_to_seed": "Demonstrates the full SFT+RL pipeline for training reasoning-augmented retrievers at scale, validating that RL with retrieval-specific rewards can improve dense retriever quality. The retrieval-accuracy reward (rank-based) is an outcome reward — our learned reasoning-quality reward model would provide richer signal specifically for reasoning-intensive queries where LREM's keyword CoT may be insufficient."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ad91f23e-f03e-4064-b3fb-e4d9ca0aa7e9",
  "isSidechain": false,
  "requestId": "req_011CbYHYeM9CsX2bgnQpL6Ln",
  "type": "assistant",
  "uuid": "52bd0f00-8951-4d27-8cdc-babbf7009601",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LvA7A2rSY4Qof92g52Z4Hu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 14829,
      "cache_creation_input_tokens": 5951,
      "cache_read_input_tokens": 15796,
      "output_tokens": 3318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 14829,
          "output_tokens": 3318,
          "cache_read_input_tokens": 15796,
          "cache_creation_input_tokens": 5951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5951
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "52bd0f00-8951-4d27-8cdc-babbf7009601",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze papers for AAAI 2026 reasoning-intensive retrieval",
  "sessionId": "27d805b7-0ea1-4632-9635-35f016c03b5a"
}
```

---
