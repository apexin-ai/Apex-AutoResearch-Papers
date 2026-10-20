# Research conversation: You are a senior ML researcher performing deep analysis of multiple published papers. **Today's date: 2026-05-30 (UTC).*

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/458a2eed-0834-465b-87af-c8668736149f.jsonl`
- **Structured JSON:** [`bfb59e9eed08a6c6655d.json`](../../sessions/bf/bfb59e9eed08a6c6655d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:27:23.044Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:27:23.044Z",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "content": "You are a senior ML researcher performing deep analysis of multiple published papers.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: Safe, Robust and Responsible AI (SRRAI)\n\nDirection: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.\n\nSeed Papers:\n- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval\n- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG\n- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative\n- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on\n- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition\n\nKnown Gaps:\n- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)\n- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails\n- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis\n\nTheoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must compare against RobustRAG and ReliabilityRAG baselines\n- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols\n- AAAI 2026 submission deadline: August 2026\n\nQuality Self-Checks:\n- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.\n- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.\n- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.\n- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.\n\nAvoid:\n- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this\n- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead\n- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates**\n\n## Your task (Batch 2)\n\nAnalyze the following 5 papers. For EACH paper:\n1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.\n2. If on OpenReview, also read reviewer comments.\n3. Write a concise analysis focusing on HOW the paper innovates.\n\n## Papers to analyze\n\n[\n  {\n    \"title\": \"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models\",\n    \"authors\": \"Mintong Kang, Nezihe Merve Gurel, Ning Yu, Dawn Song, Bo Li\",\n    \"venue\": \"ICML 2024\",\n    \"url\": \"https://arxiv.org/abs/2402.03181\",\n    \"why_important\": \"Seed paper — first theoretical framework certifying RAG generation risks via conformal risk analysis; proves RAG achieves lower conformal generation risk than standalone LLMs\",\n    \"one_line_summary\": \"Provides conformal risk bounds showing RAG reduces generation risks compared to standalone LLMs when retrieval quality is non-trivial, with extensions to distribution shift, but does not address adversarial retrieval corruption.\"\n  },\n  {\n    \"title\": \"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search\",\n    \"authors\": \"Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova\",\n    \"venue\": \"NeurIPS 2025\",\n    \"url\": \"https://arxiv.org/abs/2509.23519\",\n    \"why_important\": \"Primary competition — latest certified RAG defense using graph-theoretic methods (MIS) for document agreement; from Princeton/USC group, improves upon RobustRAG on extended generation tasks\",\n    \"one_line_summary\": \"Leverages document reliability signals and Maximum Independent Set computation to identify a consistent majority among retrieved documents, providing provable robustness guarantees with a weighted-sampling variant for long-form generation.\"\n  },\n  {\n    \"title\": \"Large Language Model Validity via Enhanced Conformal Prediction Methods\",\n    \"authors\": \"John J. Cherian, Isaac Gibbs, Emmanuel J. Candès\",\n    \"venue\": \"NeurIPS 2024\",\n    \"url\": \"https://arxiv.org/abs/2406.09714\",\n    \"why_important\": \"Addresses conditional validity — proposes adaptive conformal guarantees for LLMs that vary by topic/domain, directly relevant to group-conditional coverage under retrieval corruption\",\n    \"one_line_summary\": \"Introduces conditional validity guarantees and differentiable scoring function optimization for conformal factuality, addressing the limitation that trustworthiness varies by topic in prior conformal LLM methods.\"\n  },\n  {\n    \"title\": \"Conformal Risk Control\",\n    \"authors\": \"Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, Tal Schuster\",\n    \"venue\": \"ICLR 2024\",\n    \"url\": \"https://arxiv.org/abs/2208.02814\",\n    \"why_important\": \"Foundational framework — generalizes split CP to control any monotone loss with extensions to distribution shift; theoretical building block for the proposed risk control guarantees\",\n    \"one_line_summary\": \"Extends conformal prediction beyond coverage to control the expected value of any monotone loss function, with theoretical extensions to distribution shift and multiple simultaneous risk control.\"\n  },\n  {\n    \"title\": \"Conformal Language Modeling\",\n    \"authors\": \"Victor Quach, Adam Fisch, Tal Schuster, Adam Yala, Jae Ho Sohn, Tommi S. Jaakkola, Regina Barzilay\",\n    \"venue\": \"ICLR 2024\",\n    \"url\": \"https://arxiv.org/abs/2306.10193\",\n    \"why_important\": \"Foundational — first to extend conformal prediction to free-text LLM generation with calibrated stopping/rejection rules; the methodological ancestor of conformal factuality for RAG\",\n    \"one_line_summary\": \"Extends conformal prediction to generative language models by calibrating sampling stopping rules and rejection rules to ensure at least one acceptable answer with high probability across QA, summarization, and report generation.\"\n  }\n]\n\n## Analysis requirements\n\nFor each paper, analyze:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- If reviewer comments are available: what was praised, what was criticized?\n\n## CRITICAL: Length constraint\n\n**Each paper's analysis MUST be under 2000 characters.** Be concise and analytical — no filler, no generic praise, no redundant descriptions. Every sentence must carry information.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem? How found? (1-2 sentences)\",\n  \"key_insight\": \"Core intellectual contribution (1 sentence)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach (2-3 sentences)\",\n  \"limitations_and_open_questions\": \"Gaps + follow-up questions (1-2 sentences)\",\n  \"building_blocks\": [\"Reusable methods/tools/datasets\"],\n  \"relevance_to_seed\": \"Relation to our research area (1 sentence)\"\n}\n\nYou MUST output exactly 5 analyses in the JSON array. IMPORTANT: End your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:27:23.056Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:27:23.056Z",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-30T06:27:23.167Z_

You are a senior ML researcher performing deep analysis of multiple published papers.

**Today's date: 2026-05-30 (UTC).**

## Research context

We are generating ideas in the area of: **Target: AAAI 2026
Track: Safe, Robust and Responsible AI (SRRAI)

Direction: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.

Seed Papers:
- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval
- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG
- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism
- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative
- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on
- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition

Known Gaps:
- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)
- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails
- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis

Theoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.

Constraints:
- Compute: ≤200 H100-hours
- Must compare against RobustRAG and ReliabilityRAG baselines
- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols
- AAAI 2026 submission deadline: August 2026

Quality Self-Checks:
- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.
- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.
- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.
- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.

Avoid:
- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this
- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead
- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates**

## Your task (Batch 2)

Analyze the following 5 papers. For EACH paper:
1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.
2. If on OpenReview, also read reviewer comments.
3. Write a concise analysis focusing on HOW the paper innovates.

## Papers to analyze

[
  {
    "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
    "authors": "Mintong Kang, Nezihe Merve Gurel, Ning Yu, Dawn Song, Bo Li",
    "venue": "ICML 2024",
    "url": "https://arxiv.org/abs/2402.03181",
    "why_important": "Seed paper — first theoretical framework certifying RAG generation risks via conformal risk analysis; proves RAG achieves lower conformal generation risk than standalone LLMs",
    "one_line_summary": "Provides conformal risk bounds showing RAG reduces generation risks compared to standalone LLMs when retrieval quality is non-trivial, with extensions to distribution shift, but does not address adversarial retrieval corruption."
  },
  {
    "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
    "authors": "Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova",
    "venue": "NeurIPS 2025",
    "url": "https://arxiv.org/abs/2509.23519",
    "why_important": "Primary competition — latest certified RAG defense using graph-theoretic methods (MIS) for document agreement; from Princeton/USC group, improves upon RobustRAG on extended generation tasks",
    "one_line_summary": "Leverages document reliability signals and Maximum Independent Set computation to identify a consistent majority among retrieved documents, providing provable robustness guarantees with a weighted-sampling variant for long-form generation."
  },
  {
    "title": "Large Language Model Validity via Enhanced Conformal Prediction Methods",
    "authors": "John J. Cherian, Isaac Gibbs, Emmanuel J. Candès",
    "venue": "NeurIPS 2024",
    "url": "https://arxiv.org/abs/2406.09714",
    "why_important": "Addresses conditional validity — proposes adaptive conformal guarantees for LLMs that vary by topic/domain, directly relevant to group-conditional coverage under retrieval corruption",
    "one_line_summary": "Introduces conditional validity guarantees and differentiable scoring function optimization for conformal factuality, addressing the limitation that trustworthiness varies by topic in prior conformal LLM methods."
  },
  {
    "title": "Conformal Risk Control",
    "authors": "Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, Tal Schuster",
    "venue": "ICLR 2024",
    "url": "https://arxiv.org/abs/2208.02814",
    "why_important": "Foundational framework — generalizes split CP to control any monotone loss with extensions to distribution shift; theoretical building block for the proposed risk control guarantees",
    "one_line_summary": "Extends conformal prediction beyond coverage to control the expected value of any monotone loss function, with theoretical extensions to distribution shift and multiple simultaneous risk control."
  },
  {
    "title": "Conformal Language Modeling",
    "authors": "Victor Quach, Adam Fisch, Tal Schuster, Adam Yala, Jae Ho Sohn, Tommi S. Jaakkola, Regina Barzilay",
    "venue": "ICLR 2024",
    "url": "https://arxiv.org/abs/2306.10193",
    "why_important": "Foundational — first to extend conformal prediction to free-text LLM generation with calibrated stopping/rejection rules; the methodological ancestor of conformal factuality for RAG",
    "one_line_summary": "Extends conformal prediction to generative language models by calibrating sampling stopping rules and rejection rules to ensure at least one acceptable answer with high probability across QA, summarization, and report generation."
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
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "type": "user",
  "uuid": "a716be7a-1f21-4e73-970c-6bec8d9b5eb9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:27:23.166Z_

```json
{
  "parentUuid": "a716be7a-1f21-4e73-970c-6bec8d9b5eb9",
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
  "uuid": "063b7007-84dd-4a2f-99df-d5bd99d388a6",
  "timestamp": "2026-05-30T06:27:23.166Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:27:23.166Z_

```json
{
  "parentUuid": "063b7007-84dd-4a2f-99df-d5bd99d388a6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "38649833-1680-44d7-9d9e-dfffe9227035",
  "timestamp": "2026-05-30T06:27:23.166Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
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
  "aiTitle": "Analyze poisoning-robust conformal prediction for RAG systems",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Assistant

_source line 7 · 2026-05-30T06:27:26.039Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze these 5 papers by searching for and reading their content. I'll launch parallel searches for all 5 papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38649833-1680-44d7-9d9e-dfffe9227035",
  "isSidechain": false,
  "requestId": "req_011CbYH7wybkvPUybxMzWsnD",
  "type": "assistant",
  "uuid": "9fea4d8a-9b11-4980-9ee3-8b8c37bdd22a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6CA3y1M21KXwr4T6GbGbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1965,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
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

_source line 8 · 2026-05-30T06:27:27.133Z_

I'll research all 5 papers in parallel to gather their abstracts, methods, and any reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fea4d8a-9b11-4980-9ee3-8b8c37bdd22a",
  "isSidechain": false,
  "requestId": "req_011CbYH7wybkvPUybxMzWsnD",
  "type": "assistant",
  "uuid": "fbf17685-46ea-4361-bb47-8f5a5d899b0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6CA3y1M21KXwr4T6GbGbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1965,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
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

_source line 9 · 2026-05-30T06:27:34.978Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012Wp5f9xiRfTwnUDrGUL7hK`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze C-RAG paper",
  "prompt": "You are helping analyze a research paper for an ML research project. \n\nPaper: \"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models\" by Mintong Kang et al., ICML 2024, https://arxiv.org/abs/2402.03181\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2402.03181\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2402.03181\n3. Search for OpenReview reviews of this paper (it was at ICML 2024, so try https://openreview.net searching for \"C-RAG Certified Generation Risks\")\n4. Search the web for any discussion/reviews of this paper\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified\n- Their key insight and how they formulated the problem\n- Technical method details (score functions, theoretical results, algorithms)\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n- How they handle distribution shift (if at all)\n\nBe thorough and specific about the technical details. Report back everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbf17685-46ea-4361-bb47-8f5a5d899b0f",
  "isSidechain": false,
  "requestId": "req_011CbYH7wybkvPUybxMzWsnD",
  "type": "assistant",
  "uuid": "5151bdc8-a054-4ec1-a012-2dbedb6ab8c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6CA3y1M21KXwr4T6GbGbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1965,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
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

_source line 10 · 2026-05-30T06:27:40.155Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019J4uxNUrvFVekRZpcz4i3P`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze ReliabilityRAG paper",
  "prompt": "You are helping analyze a research paper for an ML research project.\n\nPaper: \"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search\" by Zeyu Shen et al., NeurIPS 2025 (listed as from Princeton/USC group), https://arxiv.org/abs/2509.23519\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2509.23519\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2509.23519\n3. Search for OpenReview reviews of this paper (try searching OpenReview for \"ReliabilityRAG\" or the title)\n4. Search the web for any discussion/reviews\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified (especially vs RobustRAG)\n- Their key insight about document reliability and MIS computation\n- Technical method details (graph construction, MIS algorithm, weighted sampling for long-form generation)\n- Certified robustness guarantees — what exactly do they prove?\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n\nBe thorough and specific about the technical details. Report back everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5151bdc8-a054-4ec1-a012-2dbedb6ab8c8",
  "isSidechain": false,
  "requestId": "req_011CbYH7wybkvPUybxMzWsnD",
  "type": "assistant",
  "uuid": "cb17e87d-d4db-4b07-aaf1-825abc50ffd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6CA3y1M21KXwr4T6GbGbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1965,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
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

_source line 11 · 2026-05-30T06:27:43.871Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CHyrbt7KZRHa9MPkWsHhua`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze Cherian et al. CP paper",
  "prompt": "You are helping analyze a research paper for an ML research project.\n\nPaper: \"Large Language Model Validity via Enhanced Conformal Prediction Methods\" by John J. Cherian, Isaac Gibbs, Emmanuel J. Candès, NeurIPS 2024, https://arxiv.org/abs/2406.09714\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2406.09714\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2406.09714\n3. Search for OpenReview reviews of this paper (NeurIPS 2024, search OpenReview for the title)\n4. Search the web for any discussion/reviews\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified (especially re: conditional validity varying by topic)\n- Their key insight about conditional conformal guarantees for LLMs\n- Technical method details (how they achieve conditional validity, differentiable scoring function optimization, what scores they use)\n- Connection to conformal factuality (Mohri & Hashimoto)\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n\nBe thorough and specific about the technical details. Report back everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb17e87d-d4db-4b07-aaf1-825abc50ffd7",
  "isSidechain": false,
  "requestId": "req_011CbYH7wybkvPUybxMzWsnD",
  "type": "assistant",
  "uuid": "d1ef539d-6fa7-4fc2-ae81-840465ef1ce0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6CA3y1M21KXwr4T6GbGbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1965,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
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

_source line 12 · 2026-05-30T06:27:47.768Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NZfqpJNpkoEtB9LbvDvwLC`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze Conformal Risk Control",
  "prompt": "You are helping analyze a research paper for an ML research project.\n\nPaper: \"Conformal Risk Control\" by Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, Tal Schuster, ICLR 2024, https://arxiv.org/abs/2208.02814\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2208.02814\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2208.02814\n3. Search for OpenReview reviews of this paper (ICLR 2024, search OpenReview for \"Conformal Risk Control\")\n4. Search the web for any discussion/reviews\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified (going beyond coverage to arbitrary loss functions)\n- Their key insight about monotone loss functions and how this generalizes CP\n- Technical method details (the risk control algorithm, how they handle multiple risks, distribution shift extensions)\n- The theoretical guarantees — what exactly do they prove?\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n- How the distribution shift extension works\n\nBe thorough and specific about the technical details. Report back everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d1ef539d-6fa7-4fc2-ae81-840465ef1ce0",
  "isSidechain": false,
  "requestId": "req_011CbYH7wybkvPUybxMzWsnD",
  "type": "assistant",
  "uuid": "5c15396b-d880-4a34-b4e1-5e8708f3487b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6CA3y1M21KXwr4T6GbGbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1965,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
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

_source line 13 · 2026-05-30T06:27:51.442Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017FGZPJnxzztF5qSD4xtA4D`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze Conformal Language Modeling",
  "prompt": "You are helping analyze a research paper for an ML research project.\n\nPaper: \"Conformal Language Modeling\" by Victor Quach, Adam Fisch, Tal Schuster, Adam Yala, Jae Ho Sohn, Tommi S. Jaakkola, Regina Barzilay, ICLR 2024, https://arxiv.org/abs/2306.10193\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2306.10193\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2306.10193\n3. Search for OpenReview reviews of this paper (ICLR 2024, search OpenReview for \"Conformal Language Modeling\")\n4. Search the web for any discussion/reviews\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified (extending CP to free-text generation)\n- Their key insight about stopping/rejection rules for generative models\n- Technical method details (how they calibrate stopping rules, rejection rules, the admissibility function, how they handle the combinatorial output space)\n- The theoretical guarantees — what exactly do they prove?\n- Applications they demonstrate (QA, summarization, radiology)\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n\nBe thorough and specific about the technical details. Report back everything you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c15396b-d880-4a34-b4e1-5e8708f3487b",
  "isSidechain": false,
  "requestId": "req_011CbYH7wybkvPUybxMzWsnD",
  "type": "assistant",
  "uuid": "8af694dc-a40a-408d-8d68-e53a31f016c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6CA3y1M21KXwr4T6GbGbr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3933,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1965,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3933
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
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "8af694dc-a40a-408d-8d68-e53a31f016c8",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze poisoning-robust conformal prediction for RAG systems",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Tool result

_source line 16 · 2026-05-30T06:31:22.540Z_

<details><summary>↩ Tool result · `toolu_019J4uxNUrvFVekRZpcz4i3P`</summary>

````text
Excellent -- I got the OpenReview reviews from the API. Now I have a comprehensive picture. Let me compile everything.

Here is a thorough summary of the ReliabilityRAG paper:

---

## ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search

**Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova (Princeton/USC)
**Venue:** NeurIPS 2025 (accepted as poster), presented December 4, 2025 in San Diego
**ArXiv:** https://arxiv.org/abs/2509.23519 (v1: Sep 27, 2025; v2: Feb 15, 2026)
**OpenReview:** https://openreview.net/forum?id=D9JeNTs5Bu

---

### 1. Problem and Gap Identified (Especially vs. RobustRAG)

The paper targets the vulnerability of RAG-based web-search systems (e.g., Google's Search AI Overview) to corpus poisoning and prompt injection attacks, where adversaries inject malicious documents into the retrieval corpus.

**Specific limitations of RobustRAG (Xiang et al.) they identify:**

- **Information loss:** RobustRAG uses majority voting via keywords or next-token probabilities, which "necessarily comes with significant information loss" in benign scenarios. It decomposes responses into atomic units (keywords or tokens) and aggregates via voting, which destroys contextual coherence.
- **Struggles with complex/long-form generation:** The keyword/token-level voting mechanism fundamentally cannot handle biography generation, multi-paragraph answers, or other long-form tasks. Their experiments show RobustRAG scoring ~61 vs. ReliabilityRAG's ~80 on biography generation.
- **Ignores reliability signals:** RobustRAG treats all retrieved documents "as an unordered set," completely ignoring the retrieval ranking, PageRank scores, and other reliability signals that web search engines already provide. These signals are the product of decades of SEO defense development and are genuinely informative about document trustworthiness.
- **Limited scalability:** RobustRAG's approach does not scale well to large retrieval sets.

**Key insight:** RAG-based web-search systems have built-in reliability metrics (document ranking, domain authority) that are "difficult for adversaries to circumvent." The paper argues these should be explicitly leveraged rather than discarded.

---

### 2. Key Insight: Document Reliability and MIS Computation

The central idea is to reframe robust document selection as a **graph-theoretic problem**:

- Model retrieved documents as vertices in a graph
- Connect contradictory document pairs with edges (using NLI)
- Finding the largest set of mutually non-contradictory documents = finding the **Maximum Independent Set (MIS)**
- Incorporate reliability/ranking information through **lexicographic tie-breaking** -- when multiple MIS of equal size exist, prefer the one containing higher-ranked (more reliable) documents

The insight is that adversarial documents will typically contradict the majority of benign documents, so they will be densely connected in the contradiction graph and naturally excluded from the MIS.

---

### 3. Technical Method Details

#### Stage 1: Isolated Answering
For each retrieved document x_i, the LLM generates an individual answer in isolation:
`y_i = LLM(q, {x_i})`

This prevents cross-contamination between documents during generation.

#### Stage 2: Contradiction Graph Construction
- Use a pairwise NLI model (**DeBERTa-v3-large-mnli-fever-anli-ling-wanli**) to test all answer pairs (y_i, y_j)
- An edge is added between documents i and j if `NLI_contradiction(y_i, y_j) >= beta` where beta = 0.5
- Result: undirected contradiction graph G = (V, E)

#### Stage 3: MIS Selection (Algorithm 1)
The optimization objective:
```
S* = argmax_S independent { (|S|, -lex(S)) }
```
This is a **two-criteria optimization**: first maximize the cardinality of the independent set, then among all maximum independent sets, choose the one that is lexicographically smallest (i.e., containing the highest-ranked documents).

**NP-hardness handling:** For k <= 20 documents (standard in current RAG pipelines), they use **brute-force enumeration** over all 2^|V| subsets via bit-masking. This is feasible -- runs "in milliseconds" for k=10.

Note: This is NOT weighted MIS. Reliability is incorporated through lexicographic ordering, not edge/vertex weights.

#### Stage 4: Weighted Sample-and-Aggregate for Scalability (Algorithm 2)
For larger document sets (k >> 20), exact MIS is infeasible. The scalable alternative:

1. **T = 20 rounds of sampling**, each drawing m = 2 documents with replacement
2. **Sampling weights:** `w(x_i) proportional to gamma^(i-1)` with gamma = 0.9 (exponential decay by rank). Higher-ranked documents have higher sampling probability.
3. In each round t, the LLM generates an answer a_t from the sampled context S_t
4. **Meta-aggregation:** Treat the T intermediate answers as new "isolated answers" and the T contexts as new "documents." Rank contexts lexicographically based on their constituent documents. Apply the MIS algorithm to aggregate these T intermediate answers.

This reduces the MIS problem from k documents to T intermediate results while preserving reliability information through the sampling weights.

---

### 4. Certified Robustness Guarantees

#### Theorem 1 (Main Result):
**Setting:** k total retrieved documents, adversary corrupts at most k' of them, m = k - k' benign documents remain.

**Conditions (natural assumptions):**
- k' <= (1/5)k (adversary controls at most 20% of documents)
- NLI error rate epsilon_1 between benign-benign document pairs (false contradiction rate)
- NLI error rate epsilon_2 between benign-malicious pairs (false non-contradiction rate)
- epsilon_1 < mu/m for some 0 < mu < 1/2
- epsilon_2 < ((1-mu)m - 1) / ((1+delta)em) for some 0 < delta < 1

**Conclusion:** The probability that the MIS contains any malicious document is at most e^(-Omega(k)). That is, the algorithm is **(1 - e^(-Omega(k)))-robust** -- the contamination probability vanishes exponentially as k grows.

**Intuition:** With a good NLI model, benign documents form a large clique-free cluster (low contradiction among themselves), while malicious documents contradict most benign ones (high connectivity in the graph). The MIS naturally selects the benign cluster.

#### Perfect NLI Case (Appendix B.2):
When epsilon_1 = epsilon_2 = 0 (perfect contradiction detection), the MIS **exactly** identifies all benign documents with perfect robustness and utility, provided k' < k/2 (adversary is a strict minority).

#### Weighted Sampling Guarantee (Appendix B.3):
The robustness guarantees are preserved with high probability through the weighted sampling framework, with bounds depending on T and the sampling weight distribution.

---

### 5. Threat Model

- Adversary can inject k' corrupted documents into the k retrieved results
- Documents can be placed at specific ranking positions S subset of {1,...,k}
- **Key structural assumption:** Injecting documents at higher-ranked positions is harder (requires more adversarial effort due to search engine ranking defenses)
- Two attack types evaluated: **corpus poisoning** (false/misleading facts) and **prompt injection** (jailbreak/control prompts)
- Out of scope: direct infrastructure attacks on the search provider
- Defense goal: sub-select only unmanipulated documents

---

### 6. Experimental Results

**Datasets:** RealtimeQA (RQA), Natural Questions (NQ), TriviaQA (TQA), Biography generation (Bio)

**LLMs tested:** Mistral-7B-Instruct-v0.2, Llama3.2-3B-Instruct, GPT-4o-mini (temperature=0)

**Baselines:** Vanilla RAG, RobustRAG (Keyword variant), AstuteRAG, InstructRAG

**Configurations:**
- MIS: k=10 documents
- Sampling+MIS: k=50 documents, T=20, m=2

**Key results (Table 1, k=10, prompt injection attack):**

| Setting | Method | Benign | Pos 1 Attack | Pos 10 Attack |
|---------|--------|--------|-------------|---------------|
| Mistral/RQA | MIS | 70% | 68% | 60% |
| Mistral/RQA | RobustRAG | 56% | 53% | 55% |
| Bio/GPT-4o-mini | MIS | 80.1 | 77.9 | 79.0 |
| Bio/GPT-4o-mini | RobustRAG | 61.2 | 60.4 | 61.4 |

**Key results (Table 2, k=50, sampling+MIS):**

| Setting | Method | Benign | Pos 1 | Pos 25 | Pos 50 |
|---------|--------|--------|-------|--------|--------|
| GPT-4o-mini/NQ | S+MIS | 68.6% | 60.8% | 67.4% | 68.6% |
| GPT-4o-mini/NQ | RobustRAG | 63.4% | 60.6% | 63.4% | 63.0% |

**Multi-position attacks (Figure 2, NQ, k=50):** With 40% document corruption at lower ranks, Sampling+MIS "shows decent performance, whereas RobustRAG collapses much faster."

The long-form biography generation results are particularly striking -- nearly 20 points better than RobustRAG, confirming the information-loss critique.

---

### 7. OpenReview Reviews (NeurIPS 2025)

**Decision:** Accept (poster). All four reviewers gave positive assessments after discussion.

**Reviewer praise:**
- "Translating document consistency into a rank-aware MIS problem is a novel, intuitive insight" -- considered a genuine methodological advance
- Good theory-practice balance: provides formal lambda-robustness guarantees while addressing computational barriers through scalable sampling
- Strong empirical performance: maintains high benign accuracy while outperforming baselines across attack types
- Defense-in-depth: combining NLI-based detection with ranking signals viewed favorably

**Reviewer criticisms / concerns:**
1. **NLI dependency:** Performance degrades in non-English or technical domains. Authors responded with experiments showing "graceful degradation" even with 50% NLI error probability.
2. **Multi-position attacks:** Initially underexplored in the main text; comprehensive analysis was relegated to the appendix. Reviewers wanted this more prominent.
3. **Computational overhead:** Sub-1-second latency acknowledged as unoptimized; authors proposed parallelization improvements.
4. **Parameter tuning:** Sampling parameters (gamma, T, m) are set heuristically without full theoretical justification for specific values.

**Author responses addressed:**
- NLI robustness experiments showing graceful performance drops
- Lexical matching experiments demonstrating its insufficiency (less than 4.31% attack failure rate even at optimal threshold -- justifying the NLI-based approach over simpler lexical methods)
- Multiple-choice dataset validation confirming LLM-judge reliability
- Latency analysis and optimization pathways

No unresolved fatal flaws were identified; all reviewers affirmed positive assessments.

---

### 8. Acknowledged Limitations

1. **Ambiguous queries:** Assumes a "consistent majority" exists among benign documents. Fails on queries where legitimate documents genuinely disagree or the question is subjective.
2. **Scalability:** Exact MIS requires exponential time (2^Omega(|V|) under ETH). The sampling heuristic is needed for k >> 20, but trades exact optimality for feasibility.
3. **Domain specificity of reliability signals:** Framework is designed for web search where ranking signals exist. Applicability to other RAG domains (e.g., enterprise document stores without ranking) is unclear.
4. **NLI model quality:** Performance degrades with weaker contradiction detection models. Domain-specific or multilingual NLI may be needed.
5. **Long-form generation beyond tested tasks:** Applicability to more complex generation tasks than those evaluated remains uncertain.
6. **Assumes consistent malicious behavior:** Adversarial documents are assumed to produce outputs that consistently contradict benign ones. Sophisticated adversaries crafting subtly aligned-but-wrong content might evade detection.

---

### 9. Key Takeaways for Your Research

- The paper's core contribution is showing that **reliability signals from search engines** (which existing defenses ignore) can be leveraged through a principled graph-theoretic framework
- The MIS formulation is elegant but the practical applicability hinges on NLI quality and the assumption that adversarial documents contradict benign ones
- The certified guarantee (1 - e^(-Omega(k))) is strong but requires the 20% corruption bound (k' <= k/5) and bounded NLI error rates
- The sampling+aggregation extension for scalability is practical but the theoretical guarantees become probabilistic rather than deterministic
- The 14-19 point improvement over RobustRAG on long-form generation is the most compelling empirical result, directly validating the information-loss critique

agentId: a620a8dbf50fd8bc7 (use SendMessage with to: 'a620a8dbf50fd8bc7' to continue this agent)
&lt;usage>total_tokens: 27261
tool_uses: 20
duration_ms: 222381&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "cb17e87d-d4db-4b07-aaf1-825abc50ffd7",
  "isSidechain": false,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "type": "user",
  "uuid": "42d5ca70-fcdc-45fa-b18a-c91977b56be6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping analyze a research paper for an ML research project.\n\nPaper: \"ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search\" by Zeyu Shen et al., NeurIPS 2025 (listed as from Princeton/USC group), https://arxiv.org/abs/2509.23519\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2509.23519\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2509.23519\n3. Search for OpenReview reviews of this paper (try searching OpenReview for \"ReliabilityRAG\" or the title)\n4. Search the web for any discussion/reviews\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified (especially vs RobustRAG)\n- Their key insight about document reliability and MIS computation\n- Technical method details (graph construction, MIS algorithm, weighted sampling for long-form generation)\n- Certified robustness guarantees — what exactly do they prove?\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n\nBe thorough and specific about the technical details. Report back everything you find.",
    "agentId": "a620a8dbf50fd8bc7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent -- I got the OpenReview reviews from the API. Now I have a comprehensive picture. Let me compile everything.\n\nHere is a thorough summary of the ReliabilityRAG paper:\n\n---\n\n## ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search\n\n**Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova (Princeton/USC)\n**Venue:** NeurIPS 2025 (accepted as poster), presented December 4, 2025 in San Diego\n**ArXiv:** https://arxiv.org/abs/2509.23519 (v1: Sep 27, 2025; v2: Feb 15, 2026)\n**OpenReview:** https://openreview.net/forum?id=D9JeNTs5Bu\n\n---\n\n### 1. Problem and Gap Identified (Especially vs. RobustRAG)\n\nThe paper targets the vulnerability of RAG-based web-search systems (e.g., Google's Search AI Overview) to corpus poisoning and prompt injection attacks, where adversaries inject malicious documents into the retrieval corpus.\n\n**Specific limitations of RobustRAG (Xiang et al.) they identify:**\n\n- **Information loss:** RobustRAG uses majority voting via keywords or next-token probabilities, which \"necessarily comes with significant information loss\" in benign scenarios. It decomposes responses into atomic units (keywords or tokens) and aggregates via voting, which destroys contextual coherence.\n- **Struggles with complex/long-form generation:** The keyword/token-level voting mechanism fundamentally cannot handle biography generation, multi-paragraph answers, or other long-form tasks. Their experiments show RobustRAG scoring ~61 vs. ReliabilityRAG's ~80 on biography generation.\n- **Ignores reliability signals:** RobustRAG treats all retrieved documents \"as an unordered set,\" completely ignoring the retrieval ranking, PageRank scores, and other reliability signals that web search engines already provide. These signals are the product of decades of SEO defense development and are genuinely informative about document trustworthiness.\n- **Limited scalability:** RobustRAG's approach does not scale well to large retrieval sets.\n\n**Key insight:** RAG-based web-search systems have built-in reliability metrics (document ranking, domain authority) that are \"difficult for adversaries to circumvent.\" The paper argues these should be explicitly leveraged rather than discarded.\n\n---\n\n### 2. Key Insight: Document Reliability and MIS Computation\n\nThe central idea is to reframe robust document selection as a **graph-theoretic problem**:\n\n- Model retrieved documents as vertices in a graph\n- Connect contradictory document pairs with edges (using NLI)\n- Finding the largest set of mutually non-contradictory documents = finding the **Maximum Independent Set (MIS)**\n- Incorporate reliability/ranking information through **lexicographic tie-breaking** -- when multiple MIS of equal size exist, prefer the one containing higher-ranked (more reliable) documents\n\nThe insight is that adversarial documents will typically contradict the majority of benign documents, so they will be densely connected in the contradiction graph and naturally excluded from the MIS.\n\n---\n\n### 3. Technical Method Details\n\n#### Stage 1: Isolated Answering\nFor each retrieved document x_i, the LLM generates an individual answer in isolation:\n`y_i = LLM(q, {x_i})`\n\nThis prevents cross-contamination between documents during generation.\n\n#### Stage 2: Contradiction Graph Construction\n- Use a pairwise NLI model (**DeBERTa-v3-large-mnli-fever-anli-ling-wanli**) to test all answer pairs (y_i, y_j)\n- An edge is added between documents i and j if `NLI_contradiction(y_i, y_j) >= beta` where beta = 0.5\n- Result: undirected contradiction graph G = (V, E)\n\n#### Stage 3: MIS Selection (Algorithm 1)\nThe optimization objective:\n```\nS* = argmax_S independent { (|S|, -lex(S)) }\n```\nThis is a **two-criteria optimization**: first maximize the cardinality of the independent set, then among all maximum independent sets, choose the one that is lexicographically smallest (i.e., containing the highest-ranked documents).\n\n**NP-hardness handling:** For k <= 20 documents (standard in current RAG pipelines), they use **brute-force enumeration** over all 2^|V| subsets via bit-masking. This is feasible -- runs \"in milliseconds\" for k=10.\n\nNote: This is NOT weighted MIS. Reliability is incorporated through lexicographic ordering, not edge/vertex weights.\n\n#### Stage 4: Weighted Sample-and-Aggregate for Scalability (Algorithm 2)\nFor larger document sets (k >> 20), exact MIS is infeasible. The scalable alternative:\n\n1. **T = 20 rounds of sampling**, each drawing m = 2 documents with replacement\n2. **Sampling weights:** `w(x_i) proportional to gamma^(i-1)` with gamma = 0.9 (exponential decay by rank). Higher-ranked documents have higher sampling probability.\n3. In each round t, the LLM generates an answer a_t from the sampled context S_t\n4. **Meta-aggregation:** Treat the T intermediate answers as new \"isolated answers\" and the T contexts as new \"documents.\" Rank contexts lexicographically based on their constituent documents. Apply the MIS algorithm to aggregate these T intermediate answers.\n\nThis reduces the MIS problem from k documents to T intermediate results while preserving reliability information through the sampling weights.\n\n---\n\n### 4. Certified Robustness Guarantees\n\n#### Theorem 1 (Main Result):\n**Setting:** k total retrieved documents, adversary corrupts at most k' of them, m = k - k' benign documents remain.\n\n**Conditions (natural assumptions):**\n- k' <= (1/5)k (adversary controls at most 20% of documents)\n- NLI error rate epsilon_1 between benign-benign document pairs (false contradiction rate)\n- NLI error rate epsilon_2 between benign-malicious pairs (false non-contradiction rate)\n- epsilon_1 < mu/m for some 0 < mu < 1/2\n- epsilon_2 < ((1-mu)m - 1) / ((1+delta)em) for some 0 < delta < 1\n\n**Conclusion:** The probability that the MIS contains any malicious document is at most e^(-Omega(k)). That is, the algorithm is **(1 - e^(-Omega(k)))-robust** -- the contamination probability vanishes exponentially as k grows.\n\n**Intuition:** With a good NLI model, benign documents form a large clique-free cluster (low contradiction among themselves), while malicious documents contradict most benign ones (high connectivity in the graph). The MIS naturally selects the benign cluster.\n\n#### Perfect NLI Case (Appendix B.2):\nWhen epsilon_1 = epsilon_2 = 0 (perfect contradiction detection), the MIS **exactly** identifies all benign documents with perfect robustness and utility, provided k' < k/2 (adversary is a strict minority).\n\n#### Weighted Sampling Guarantee (Appendix B.3):\nThe robustness guarantees are preserved with high probability through the weighted sampling framework, with bounds depending on T and the sampling weight distribution.\n\n---\n\n### 5. Threat Model\n\n- Adversary can inject k' corrupted documents into the k retrieved results\n- Documents can be placed at specific ranking positions S subset of {1,...,k}\n- **Key structural assumption:** Injecting documents at higher-ranked positions is harder (requires more adversarial effort due to search engine ranking defenses)\n- Two attack types evaluated: **corpus poisoning** (false/misleading facts) and **prompt injection** (jailbreak/control prompts)\n- Out of scope: direct infrastructure attacks on the search provider\n- Defense goal: sub-select only unmanipulated documents\n\n---\n\n### 6. Experimental Results\n\n**Datasets:** RealtimeQA (RQA), Natural Questions (NQ), TriviaQA (TQA), Biography generation (Bio)\n\n**LLMs tested:** Mistral-7B-Instruct-v0.2, Llama3.2-3B-Instruct, GPT-4o-mini (temperature=0)\n\n**Baselines:** Vanilla RAG, RobustRAG (Keyword variant), AstuteRAG, InstructRAG\n\n**Configurations:**\n- MIS: k=10 documents\n- Sampling+MIS: k=50 documents, T=20, m=2\n\n**Key results (Table 1, k=10, prompt injection attack):**\n\n| Setting | Method | Benign | Pos 1 Attack | Pos 10 Attack |\n|---------|--------|--------|-------------|---------------|\n| Mistral/RQA | MIS | 70% | 68% | 60% |\n| Mistral/RQA | RobustRAG | 56% | 53% | 55% |\n| Bio/GPT-4o-mini | MIS | 80.1 | 77.9 | 79.0 |\n| Bio/GPT-4o-mini | RobustRAG | 61.2 | 60.4 | 61.4 |\n\n**Key results (Table 2, k=50, sampling+MIS):**\n\n| Setting | Method | Benign | Pos 1 | Pos 25 | Pos 50 |\n|---------|--------|--------|-------|--------|--------|\n| GPT-4o-mini/NQ | S+MIS | 68.6% | 60.8% | 67.4% | 68.6% |\n| GPT-4o-mini/NQ | RobustRAG | 63.4% | 60.6% | 63.4% | 63.0% |\n\n**Multi-position attacks (Figure 2, NQ, k=50):** With 40% document corruption at lower ranks, Sampling+MIS \"shows decent performance, whereas RobustRAG collapses much faster.\"\n\nThe long-form biography generation results are particularly striking -- nearly 20 points better than RobustRAG, confirming the information-loss critique.\n\n---\n\n### 7. OpenReview Reviews (NeurIPS 2025)\n\n**Decision:** Accept (poster). All four reviewers gave positive assessments after discussion.\n\n**Reviewer praise:**\n- \"Translating document consistency into a rank-aware MIS problem is a novel, intuitive insight\" -- considered a genuine methodological advance\n- Good theory-practice balance: provides formal lambda-robustness guarantees while addressing computational barriers through scalable sampling\n- Strong empirical performance: maintains high benign accuracy while outperforming baselines across attack types\n- Defense-in-depth: combining NLI-based detection with ranking signals viewed favorably\n\n**Reviewer criticisms / concerns:**\n1. **NLI dependency:** Performance degrades in non-English or technical domains. Authors responded with experiments showing \"graceful degradation\" even with 50% NLI error probability.\n2. **Multi-position attacks:** Initially underexplored in the main text; comprehensive analysis was relegated to the appendix. Reviewers wanted this more prominent.\n3. **Computational overhead:** Sub-1-second latency acknowledged as unoptimized; authors proposed parallelization improvements.\n4. **Parameter tuning:** Sampling parameters (gamma, T, m) are set heuristically without full theoretical justification for specific values.\n\n**Author responses addressed:**\n- NLI robustness experiments showing graceful performance drops\n- Lexical matching experiments demonstrating its insufficiency (less than 4.31% attack failure rate even at optimal threshold -- justifying the NLI-based approach over simpler lexical methods)\n- Multiple-choice dataset validation confirming LLM-judge reliability\n- Latency analysis and optimization pathways\n\nNo unresolved fatal flaws were identified; all reviewers affirmed positive assessments.\n\n---\n\n### 8. Acknowledged Limitations\n\n1. **Ambiguous queries:** Assumes a \"consistent majority\" exists among benign documents. Fails on queries where legitimate documents genuinely disagree or the question is subjective.\n2. **Scalability:** Exact MIS requires exponential time (2^Omega(|V|) under ETH). The sampling heuristic is needed for k >> 20, but trades exact optimality for feasibility.\n3. **Domain specificity of reliability signals:** Framework is designed for web search where ranking signals exist. Applicability to other RAG domains (e.g., enterprise document stores without ranking) is unclear.\n4. **NLI model quality:** Performance degrades with weaker contradiction detection models. Domain-specific or multilingual NLI may be needed.\n5. **Long-form generation beyond tested tasks:** Applicability to more complex generation tasks than those evaluated remains uncertain.\n6. **Assumes consistent malicious behavior:** Adversarial documents are assumed to produce outputs that consistently contradict benign ones. Sophisticated adversaries crafting subtly aligned-but-wrong content might evade detection.\n\n---\n\n### 9. Key Takeaways for Your Research\n\n- The paper's core contribution is showing that **reliability signals from search engines** (which existing defenses ignore) can be leveraged through a principled graph-theoretic framework\n- The MIS formulation is elegant but the practical applicability hinges on NLI quality and the assumption that adversarial documents contradict benign ones\n- The certified guarantee (1 - e^(-Omega(k))) is strong but requires the 20% corruption bound (k' <= k/5) and bounded NLI error rates\n- The sampling+aggregation extension for scalability is practical but the theoretical guarantees become probabilistic rather than deterministic\n- The 14-19 point improvement over RobustRAG on long-form generation is the most compelling empirical result, directly validating the information-loss critique"
      }
    ],
    "totalDurationMs": 222381,
    "totalTokens": 27261,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1153,
      "cache_read_input_tokens": 22753,
      "output_tokens": 3354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3354,
          "cache_read_input_tokens": 22753,
          "cache_creation_input_tokens": 1153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1153,
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
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "cb17e87d-d4db-4b07-aaf1-825abc50ffd7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 17 · 2026-05-30T06:31:42.813Z_

<details><summary>↩ Tool result · `toolu_012Wp5f9xiRfTwnUDrGUL7hK`</summary>

```text
Now I have a comprehensive picture. Let me compile the complete analysis.

Here is a detailed analysis of the C-RAG paper.

---

## C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models

**Authors:** Mintong Kang, Nezihe Merve Gürel, Ning Yu, Dawn Song, Bo Li
**Venue:** ICML 2024 (Poster), PMLR 235:22963-23000
**arXiv:** 2402.03181 (v1: Feb 5, 2024; v5: Jul 30, 2024)

---

### 1. Problem/Gap Identified

The paper identifies a fundamental theoretical gap: while RAG systems are widely used to mitigate LLM hallucinations and misalignments by grounding generation in retrieved external knowledge, there were **no provable guarantees** about whether RAG actually reduces generation risk compared to vanilla LLMs. The field lacked:

- A formal framework to certify upper bounds on generation risk for RAG models
- Theoretical conditions under which RAG provably outperforms standalone LLMs
- Risk guarantees that hold under test-time distribution shifts for general bounded risk functions (prior conformal prediction work required monotonic risk functions)

The authors frame four core research questions: (1) Can RAG demonstrably achieve low generation risks? (2) How to provide provable guarantees? (3) What sufficient conditions enable RAG to reduce risk? (4) Can generation risks be certifiably controlled below desired levels?

---

### 2. Key Insight and Formulation

The key insight is to apply **conformal risk control** (from the conformal prediction literature, building on Bates et al., 2021 and Angelopoulos et al., 2021/2022) to RAG systems, but extended in two crucial ways:

1. **From classification to generation**: Prior conformal risk control applied to classification/set prediction. C-RAG extends it to text generation by introducing a "constrained generation protocol" that produces a **set** of candidate generations rather than a single output, enabling set-based risk analysis.

2. **From monotonic to general bounded risk functions**: Prior distribution-shift guarantees required monotonic risk functions. C-RAG provides the first guarantees under distribution shifts for arbitrary bounded risk functions in [0,1].

---

### 3. Technical Method Details

#### 3.1 Constrained Generation Protocol

The protocol is parameterized by **lambda = [N_rag, lambda_g, lambda_s]** where:
- **N_rag**: number of retrieved examples from the knowledge base via KNN in embedding space
- **lambda_g**: size of the generation set (number of candidate outputs)
- **lambda_s**: similarity threshold for diversity control (reject candidates too similar to already-generated ones)

Steps: (1) Retrieve N_rag examples using embedding similarity s_{theta_r}; (2) Arrange retrieved examples with the test query into augmented input X^(rag); (3) Sample lambda_g generations from p_{theta_l}(.|X^(rag)), rejecting duplicates exceeding similarity lambda_s; (4) Output the generation set T_{lambda, p_{theta_l}}(x).

#### 3.2 Risk and Score Functions

- **Risk function**: R(T_{lambda}(x), y) : 2^Y x Y -> [0,1]. The concrete instantiation used is: R = 1 - max_{y' in T} ROUGE(y', y), measuring worst-case generation failure.
- **Similarity function**: s_{theta_r}(.,.) : X x X -> R for retrieval scoring.
- **Conformal generation risk** alpha_hat_lambda = min{h^{-1}(ln(1/delta)/N_cal; R_hat(D_cal)), Phi_bin^{-1}(delta/e; N_cal, R_hat(D_cal))} where h(a,b) is the KL divergence and Phi_bin is the binomial CDF inverse.

#### 3.3 Key Definitions

**Definition 1 (V_rag-Retrieval Model):** A retrieval model is V_rag-qualified if: (a) Non-trivial utility: expected contrastive loss L_tau < ln 2; and (b) Bounded variance: V_rag := sqrt(Var[s_theta(x,x+) - s_theta(x,x-)]) / log(exp(L_tau) - 1) < 1. Low V_rag indicates stable, generalizable retrieval.

**Definition 2 ((d+, Phi_M)-Transformer):** A single-layer self-attention transformer qualifies if: (a) Non-trivial self-attention: attention scores >= d+ > 0 for semantically identical pairs; (b) Better-than-random prediction: integral from -1 to 1 of Phi_M(v)dv > 1, where M is the negative prediction margin and Phi_M its CDF.

#### 3.4 Main Theoretical Results

**Proposition 1 (Risk Guarantee, Type 1):** Given configuration lambda, C-RAG guarantees with confidence 1-delta: P[R(T_{lambda}(x), y) <= alpha_hat_lambda] >= 1 - delta. This provides a sound upper bound.

**Proposition 2 (Risk Guarantee, Type 2):** Given desired risk level alpha, C-RAG computes a valid configuration set Lambda_hat_alpha = {lambda_j : p_j <= delta/|Lambda|} with guarantee: P[sup_{lambda in Lambda_hat_alpha} R(T_{lambda}(x), y) <= alpha] >= 1 - delta. Uses Bonferroni correction over the finite parameter space.

**Proposition 3 (Retrieval Quality):** For a V_rag-retrieval model with knowledge base size N_ext, provides a lower bound on expected positive (relevant) retrievals that improves **exponentially** with N_ext: E[N_pos] >= (9/10) N_rag (1 - sum_c r^(c)_cal (N_ext - r^(c)_ext N_ext + 2ln10) V_rag^{0.5(r^(c)_ext N_ext - 2ln10)}).

**Theorem 1 (RAG Reduces Conformal Generation Risk):** Under the V_rag-retrieval model and (d+, Phi_M)-transformer assumptions, P[alpha_hat_rag < alpha_hat] >= 1 - p_t - p_r, where:
- p_t = exp{-2 N_cal [Phi_M(0.5 d+ (integral Phi_M(v)dv - 1) N_rag) - Phi_M(0)]^2} captures transformer quality uncertainty
- p_r = (25/N_rag)(4 - 9 sum_c r^(c)_cal (1.5 N_ext - r^(c)_ext N_ext) V_rag^{0.25 r^(c)_ext N_ext})^{-2} captures retrieval quality uncertainty

Three conditions must hold: (1) N_ext > 2 sqrt(2 ln 10) / min_c r_ext^(c); (2) N_rag > 2/d+; (3) N_ext V_rag^{0.25 min_c r_ext^(c) N_ext} < 4/9.

**Theorem 2 (Conformal Risk Under Distribution Shifts):** For test distribution Q with Hellinger distance H(D, Q) <= rho from calibration distribution D: P_{(X,Y)~Q}[R(T_lambda(X), Y) <= alpha_hat(rho)] >= 1 - delta, where alpha_hat(rho) = R_hat + sqrt(V_hat / N_cal) * q_delta + 2*rho + 2*rho^2. This is the **first** generation risk guarantee under distribution shifts for general bounded risk functions (not requiring monotonicity).

**Theorem 3:** Extends the "RAG reduces risk" result (Theorem 1) to hold under distribution shifts as well.

#### 3.5 Two-Phase Framework

The framework operates in two phases:
1. **Estimation phase**: Compute conformal risks on a calibration dataset
2. **Inference phase**: Deliver risk-controlled generations based on user-specified parameters or risk thresholds

---

### 4. Experimental Results

**Datasets:** AESLC, CommonGen, DART, E2E (four standard NLP generation benchmarks)

**Retrieval Models:** BM25 (sparse), BAAI/BGE embeddings, OpenAI text-embedding-ada-002, and a supervised fine-tuned biencoder (LLM-R)

**Key Findings:**
- **Soundness**: Empirical risks consistently fell below the certified conformal generation risk bounds across all datasets and retrieval models.
- **Tightness**: Gaps between theoretical bounds and empirical risks narrowed to as small as 1e-3, demonstrating practical utility.
- **RAG vs. vanilla LLM**: RAG consistently achieved lower conformal generation risk. The supervised fine-tuned biencoder achieved the lowest risk values. Risk reduction scaled monotonically with increasing N_rag.
- **Distribution shift robustness**: Bounds remained valid under natural domain shifts while maintaining reasonable tightness.
- **Configuration discovery**: The system successfully identified valid RAG configurations achieving desired risk levels.

---

### 5. Reviewer Feedback

Unfortunately, the OpenReview reviews for this paper (forum ID: FMa4c5NhOe) are not publicly accessible through the API -- the notes/reviews endpoint returns empty results. The paper was accepted as a poster at ICML 2024 (submission #4813). No detailed reviewer scores or commentary could be retrieved.

From the Liner.com quick review and the aimodels.fyi analysis, the general assessment is positive, highlighting the paper as the **first** to provide certified risk guarantees for RAG systems. No specific numerical reviewer scores were found publicly.

A follow-up paper ("Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction," arXiv:2511.17908) positions C-RAG as operating **post-generation** (bounding risk after generation), whereas their own work applies conformal prediction **pre-generation** (filtering retrieved context before it enters the generator). This is an implicit critique: C-RAG's guarantees are about the output quality after generation rather than preventing noisy context from entering the generator in the first place.

---

### 6. Limitations Acknowledged

The authors discuss limitations in Appendix A:

1. **Single-layer transformer assumption**: The theoretical analysis is restricted to a one-layer self-attention transformer, not the multi-layer architectures used in practice. Extending to multi-layer analysis is listed as future work.

2. **Token-level simplification**: Each instance is treated approximately as a single token, oversimplifying real text generation complexity.

3. **Contrastive loss assumption for retrieval**: The retrieval model quality is defined through contrastive loss, which is not universally applicable to all retrieval paradigms.

4. **Finite parameter space**: The framework requires a finite parameter space Lambda with N parameters, discretizing what is naturally a continuous space.

5. **Calibration data dependency**: Risk guarantees depend on having sufficient calibration samples from the target distribution, which may be expensive.

6. **Knowledge base requirements**: The theoretical results require an adequate external knowledge base size (specific lower bounds in terms of class proportions).

7. **Semantic equivalence simplification**: The definition of "positive pairs" for retrieval analysis uses a simplistic semantic equivalence notion.

---

### 7. Distribution Shift Handling

This is one of the paper's major contributions. The approach:

1. **Assumes bounded Hellinger distance**: The test distribution Q must satisfy H(D, Q) <= rho relative to the calibration distribution D. The Hellinger distance is a standard statistical divergence measure.

2. **Adjusts the risk bound**: The conformal generation risk under shift is alpha_hat(rho) = R_hat + sqrt(V_hat / N_cal) * q_delta + 2*rho + 2*rho^2. The terms 2*rho + 2*rho^2 are the "price" of distribution shift. V_hat is an unbiased variance estimator from calibration pairwise differences.

3. **Key advantage over prior work**: Previous conformal prediction guarantees under distribution shift (e.g., Angelopoulos et al.) required **monotonic** risk functions. C-RAG provides guarantees for **any bounded** risk function in [0,1], which is essential for text generation where risk functions like 1-ROUGE are not monotonic in the traditional conformal prediction sense.

4. **Practical evaluation**: Tested on natural domain shifts (different question types, document sources) and bounds remained valid.

5. **Limitation**: The practitioner must specify or estimate the Hellinger distance bound rho. If the actual shift exceeds rho, guarantees are void. The paper does not provide a method for estimating rho from data.

---

### Key References

- Paper: `/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-adversarial/458a2eed-0834-465b-87af-c8668736149f/tool-results/webfetch-1780122465820-c41haj.pdf` (downloaded PDF)
- OpenReview: https://openreview.net/forum?id=FMa4c5NhOe
- GitHub implementation: https://github.com/kangmintong/C-RAG
- PMLR proceedings: https://proceedings.mlr.press/v235/kang24a.html
- arXiv HTML: https://arxiv.org/html/2402.03181v5

agentId: a318fe01058cd510b (use SendMessage with to: 'a318fe01058cd510b' to continue this agent)
&lt;usage>total_tokens: 29501
tool_uses: 23
duration_ms: 247817&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5151bdc8-a054-4ec1-a012-2dbedb6ab8c8",
  "isSidechain": false,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "type": "user",
  "uuid": "ef5243b5-eaca-42fb-aeee-2096bd5ad419",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping analyze a research paper for an ML research project. \n\nPaper: \"C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models\" by Mintong Kang et al., ICML 2024, https://arxiv.org/abs/2402.03181\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2402.03181\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2402.03181\n3. Search for OpenReview reviews of this paper (it was at ICML 2024, so try https://openreview.net searching for \"C-RAG Certified Generation Risks\")\n4. Search the web for any discussion/reviews of this paper\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified\n- Their key insight and how they formulated the problem\n- Technical method details (score functions, theoretical results, algorithms)\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n- How they handle distribution shift (if at all)\n\nBe thorough and specific about the technical details. Report back everything you find.",
    "agentId": "a318fe01058cd510b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Let me compile the complete analysis.\n\nHere is a detailed analysis of the C-RAG paper.\n\n---\n\n## C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models\n\n**Authors:** Mintong Kang, Nezihe Merve Gürel, Ning Yu, Dawn Song, Bo Li\n**Venue:** ICML 2024 (Poster), PMLR 235:22963-23000\n**arXiv:** 2402.03181 (v1: Feb 5, 2024; v5: Jul 30, 2024)\n\n---\n\n### 1. Problem/Gap Identified\n\nThe paper identifies a fundamental theoretical gap: while RAG systems are widely used to mitigate LLM hallucinations and misalignments by grounding generation in retrieved external knowledge, there were **no provable guarantees** about whether RAG actually reduces generation risk compared to vanilla LLMs. The field lacked:\n\n- A formal framework to certify upper bounds on generation risk for RAG models\n- Theoretical conditions under which RAG provably outperforms standalone LLMs\n- Risk guarantees that hold under test-time distribution shifts for general bounded risk functions (prior conformal prediction work required monotonic risk functions)\n\nThe authors frame four core research questions: (1) Can RAG demonstrably achieve low generation risks? (2) How to provide provable guarantees? (3) What sufficient conditions enable RAG to reduce risk? (4) Can generation risks be certifiably controlled below desired levels?\n\n---\n\n### 2. Key Insight and Formulation\n\nThe key insight is to apply **conformal risk control** (from the conformal prediction literature, building on Bates et al., 2021 and Angelopoulos et al., 2021/2022) to RAG systems, but extended in two crucial ways:\n\n1. **From classification to generation**: Prior conformal risk control applied to classification/set prediction. C-RAG extends it to text generation by introducing a \"constrained generation protocol\" that produces a **set** of candidate generations rather than a single output, enabling set-based risk analysis.\n\n2. **From monotonic to general bounded risk functions**: Prior distribution-shift guarantees required monotonic risk functions. C-RAG provides the first guarantees under distribution shifts for arbitrary bounded risk functions in [0,1].\n\n---\n\n### 3. Technical Method Details\n\n#### 3.1 Constrained Generation Protocol\n\nThe protocol is parameterized by **lambda = [N_rag, lambda_g, lambda_s]** where:\n- **N_rag**: number of retrieved examples from the knowledge base via KNN in embedding space\n- **lambda_g**: size of the generation set (number of candidate outputs)\n- **lambda_s**: similarity threshold for diversity control (reject candidates too similar to already-generated ones)\n\nSteps: (1) Retrieve N_rag examples using embedding similarity s_{theta_r}; (2) Arrange retrieved examples with the test query into augmented input X^(rag); (3) Sample lambda_g generations from p_{theta_l}(.|X^(rag)), rejecting duplicates exceeding similarity lambda_s; (4) Output the generation set T_{lambda, p_{theta_l}}(x).\n\n#### 3.2 Risk and Score Functions\n\n- **Risk function**: R(T_{lambda}(x), y) : 2^Y x Y -> [0,1]. The concrete instantiation used is: R = 1 - max_{y' in T} ROUGE(y', y), measuring worst-case generation failure.\n- **Similarity function**: s_{theta_r}(.,.) : X x X -> R for retrieval scoring.\n- **Conformal generation risk** alpha_hat_lambda = min{h^{-1}(ln(1/delta)/N_cal; R_hat(D_cal)), Phi_bin^{-1}(delta/e; N_cal, R_hat(D_cal))} where h(a,b) is the KL divergence and Phi_bin is the binomial CDF inverse.\n\n#### 3.3 Key Definitions\n\n**Definition 1 (V_rag-Retrieval Model):** A retrieval model is V_rag-qualified if: (a) Non-trivial utility: expected contrastive loss L_tau < ln 2; and (b) Bounded variance: V_rag := sqrt(Var[s_theta(x,x+) - s_theta(x,x-)]) / log(exp(L_tau) - 1) < 1. Low V_rag indicates stable, generalizable retrieval.\n\n**Definition 2 ((d+, Phi_M)-Transformer):** A single-layer self-attention transformer qualifies if: (a) Non-trivial self-attention: attention scores >= d+ > 0 for semantically identical pairs; (b) Better-than-random prediction: integral from -1 to 1 of Phi_M(v)dv > 1, where M is the negative prediction margin and Phi_M its CDF.\n\n#### 3.4 Main Theoretical Results\n\n**Proposition 1 (Risk Guarantee, Type 1):** Given configuration lambda, C-RAG guarantees with confidence 1-delta: P[R(T_{lambda}(x), y) <= alpha_hat_lambda] >= 1 - delta. This provides a sound upper bound.\n\n**Proposition 2 (Risk Guarantee, Type 2):** Given desired risk level alpha, C-RAG computes a valid configuration set Lambda_hat_alpha = {lambda_j : p_j <= delta/|Lambda|} with guarantee: P[sup_{lambda in Lambda_hat_alpha} R(T_{lambda}(x), y) <= alpha] >= 1 - delta. Uses Bonferroni correction over the finite parameter space.\n\n**Proposition 3 (Retrieval Quality):** For a V_rag-retrieval model with knowledge base size N_ext, provides a lower bound on expected positive (relevant) retrievals that improves **exponentially** with N_ext: E[N_pos] >= (9/10) N_rag (1 - sum_c r^(c)_cal (N_ext - r^(c)_ext N_ext + 2ln10) V_rag^{0.5(r^(c)_ext N_ext - 2ln10)}).\n\n**Theorem 1 (RAG Reduces Conformal Generation Risk):** Under the V_rag-retrieval model and (d+, Phi_M)-transformer assumptions, P[alpha_hat_rag < alpha_hat] >= 1 - p_t - p_r, where:\n- p_t = exp{-2 N_cal [Phi_M(0.5 d+ (integral Phi_M(v)dv - 1) N_rag) - Phi_M(0)]^2} captures transformer quality uncertainty\n- p_r = (25/N_rag)(4 - 9 sum_c r^(c)_cal (1.5 N_ext - r^(c)_ext N_ext) V_rag^{0.25 r^(c)_ext N_ext})^{-2} captures retrieval quality uncertainty\n\nThree conditions must hold: (1) N_ext > 2 sqrt(2 ln 10) / min_c r_ext^(c); (2) N_rag > 2/d+; (3) N_ext V_rag^{0.25 min_c r_ext^(c) N_ext} < 4/9.\n\n**Theorem 2 (Conformal Risk Under Distribution Shifts):** For test distribution Q with Hellinger distance H(D, Q) <= rho from calibration distribution D: P_{(X,Y)~Q}[R(T_lambda(X), Y) <= alpha_hat(rho)] >= 1 - delta, where alpha_hat(rho) = R_hat + sqrt(V_hat / N_cal) * q_delta + 2*rho + 2*rho^2. This is the **first** generation risk guarantee under distribution shifts for general bounded risk functions (not requiring monotonicity).\n\n**Theorem 3:** Extends the \"RAG reduces risk\" result (Theorem 1) to hold under distribution shifts as well.\n\n#### 3.5 Two-Phase Framework\n\nThe framework operates in two phases:\n1. **Estimation phase**: Compute conformal risks on a calibration dataset\n2. **Inference phase**: Deliver risk-controlled generations based on user-specified parameters or risk thresholds\n\n---\n\n### 4. Experimental Results\n\n**Datasets:** AESLC, CommonGen, DART, E2E (four standard NLP generation benchmarks)\n\n**Retrieval Models:** BM25 (sparse), BAAI/BGE embeddings, OpenAI text-embedding-ada-002, and a supervised fine-tuned biencoder (LLM-R)\n\n**Key Findings:**\n- **Soundness**: Empirical risks consistently fell below the certified conformal generation risk bounds across all datasets and retrieval models.\n- **Tightness**: Gaps between theoretical bounds and empirical risks narrowed to as small as 1e-3, demonstrating practical utility.\n- **RAG vs. vanilla LLM**: RAG consistently achieved lower conformal generation risk. The supervised fine-tuned biencoder achieved the lowest risk values. Risk reduction scaled monotonically with increasing N_rag.\n- **Distribution shift robustness**: Bounds remained valid under natural domain shifts while maintaining reasonable tightness.\n- **Configuration discovery**: The system successfully identified valid RAG configurations achieving desired risk levels.\n\n---\n\n### 5. Reviewer Feedback\n\nUnfortunately, the OpenReview reviews for this paper (forum ID: FMa4c5NhOe) are not publicly accessible through the API -- the notes/reviews endpoint returns empty results. The paper was accepted as a poster at ICML 2024 (submission #4813). No detailed reviewer scores or commentary could be retrieved.\n\nFrom the Liner.com quick review and the aimodels.fyi analysis, the general assessment is positive, highlighting the paper as the **first** to provide certified risk guarantees for RAG systems. No specific numerical reviewer scores were found publicly.\n\nA follow-up paper (\"Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction,\" arXiv:2511.17908) positions C-RAG as operating **post-generation** (bounding risk after generation), whereas their own work applies conformal prediction **pre-generation** (filtering retrieved context before it enters the generator). This is an implicit critique: C-RAG's guarantees are about the output quality after generation rather than preventing noisy context from entering the generator in the first place.\n\n---\n\n### 6. Limitations Acknowledged\n\nThe authors discuss limitations in Appendix A:\n\n1. **Single-layer transformer assumption**: The theoretical analysis is restricted to a one-layer self-attention transformer, not the multi-layer architectures used in practice. Extending to multi-layer analysis is listed as future work.\n\n2. **Token-level simplification**: Each instance is treated approximately as a single token, oversimplifying real text generation complexity.\n\n3. **Contrastive loss assumption for retrieval**: The retrieval model quality is defined through contrastive loss, which is not universally applicable to all retrieval paradigms.\n\n4. **Finite parameter space**: The framework requires a finite parameter space Lambda with N parameters, discretizing what is naturally a continuous space.\n\n5. **Calibration data dependency**: Risk guarantees depend on having sufficient calibration samples from the target distribution, which may be expensive.\n\n6. **Knowledge base requirements**: The theoretical results require an adequate external knowledge base size (specific lower bounds in terms of class proportions).\n\n7. **Semantic equivalence simplification**: The definition of \"positive pairs\" for retrieval analysis uses a simplistic semantic equivalence notion.\n\n---\n\n### 7. Distribution Shift Handling\n\nThis is one of the paper's major contributions. The approach:\n\n1. **Assumes bounded Hellinger distance**: The test distribution Q must satisfy H(D, Q) <= rho relative to the calibration distribution D. The Hellinger distance is a standard statistical divergence measure.\n\n2. **Adjusts the risk bound**: The conformal generation risk under shift is alpha_hat(rho) = R_hat + sqrt(V_hat / N_cal) * q_delta + 2*rho + 2*rho^2. The terms 2*rho + 2*rho^2 are the \"price\" of distribution shift. V_hat is an unbiased variance estimator from calibration pairwise differences.\n\n3. **Key advantage over prior work**: Previous conformal prediction guarantees under distribution shift (e.g., Angelopoulos et al.) required **monotonic** risk functions. C-RAG provides guarantees for **any bounded** risk function in [0,1], which is essential for text generation where risk functions like 1-ROUGE are not monotonic in the traditional conformal prediction sense.\n\n4. **Practical evaluation**: Tested on natural domain shifts (different question types, document sources) and bounds remained valid.\n\n5. **Limitation**: The practitioner must specify or estimate the Hellinger distance bound rho. If the actual shift exceeds rho, guarantees are void. The paper does not provide a method for estimating rho from data.\n\n---\n\n### Key References\n\n- Paper: `/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-adversarial/458a2eed-0834-465b-87af-c8668736149f/tool-results/webfetch-1780122465820-c41haj.pdf` (downloaded PDF)\n- OpenReview: https://openreview.net/forum?id=FMa4c5NhOe\n- GitHub implementation: https://github.com/kangmintong/C-RAG\n- PMLR proceedings: https://proceedings.mlr.press/v235/kang24a.html\n- arXiv HTML: https://arxiv.org/html/2402.03181v5"
      }
    ],
    "totalDurationMs": 247817,
    "totalTokens": 29501,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 268,
      "cache_creation_input_tokens": 1629,
      "cache_read_input_tokens": 24284,
      "output_tokens": 3320,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1629
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 268,
          "output_tokens": 3320,
          "cache_read_input_tokens": 24284,
          "cache_creation_input_tokens": 1629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1629,
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
      "otherToolCount": 23
    }
  },
  "sourceToolAssistantUUID": "5151bdc8-a054-4ec1-a012-2dbedb6ab8c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
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
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "ef5243b5-eaca-42fb-aeee-2096bd5ad419",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze poisoning-robust conformal prediction for RAG systems",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Tool result

_source line 20 · 2026-05-30T06:31:45.036Z_

<details><summary>↩ Tool result · `toolu_01NZfqpJNpkoEtB9LbvDvwLC`</summary>

```text
Excellent -- I got all the reviews. Now I have comprehensive information. Let me compile the full analysis.

---

Here is a detailed analysis of **"Conformal Risk Control"** by Angelopoulos, Bates, Fisch, Lei, and Schuster (ICLR 2024, spotlight).

---

## 1. The Problem and Gap Identified

Standard conformal prediction provides a single type of guarantee: **marginal coverage** -- the probability that the true label Y falls inside the prediction set C(X) is at least 1-alpha. The authors identify that this coverage guarantee is too narrow for many practical applications. Real-world tasks often care about controlling richer notions of risk beyond binary "in or out" membership:

- In **tumor segmentation**, you want to control the false negative rate (missing cancerous pixels), not just whether the entire segmentation is "correct."
- In **multilabel classification**, you want to bound the fraction of missed labels.
- In **hierarchical classification**, you want to control how far (in graph distance) your predictions are from the true label.
- In **question answering**, you want to control token-level F1-score loss.

None of these fit cleanly into the standard conformal prediction framework, which only handles the indicator loss L = 1{Y not in C(X)}.

## 2. Key Insight: Monotone Loss Functions

The central insight is that what makes conformal prediction work is not specific to coverage -- it is the **monotonicity** of the loss in a tuning parameter lambda. In standard CP, as lambda increases, the prediction set C_lambda(X) grows, and the miscoverage loss 1{Y not in C_lambda(X)} is non-increasing in lambda. The authors realize this monotonicity structure is the essential ingredient, and it generalizes far beyond coverage.

**Definition of the setup:** Given calibration data {(X_i, Y_i)}_{i=1}^n drawn exchangeably, define loss functions L_i(lambda) = L(C_lambda(X_i), Y_i) parameterized by lambda in Lambda (a totally ordered set). The losses must satisfy:
- **Monotonicity (non-increasing):** L_i(lambda) is non-increasing in lambda for all i
- **Right-continuity:** Technical condition for well-definedness
- **Boundedness:** L_i(lambda) in (-inf, B] for some finite B

As lambda increases, the prediction sets get larger/more conservative, and losses decrease. The goal is to find the smallest lambda-hat such that the expected loss on a new test point is controlled: E[L_{n+1}(lambda-hat)] <= alpha.

## 3. Technical Method: The Risk Control Algorithm

The core algorithm is remarkably simple (5 lines of code):

**Input:** Calibration losses L_1(lambda), ..., L_n(lambda), target level alpha, upper bound B.

**Algorithm:**
1. Compute empirical risk: R-hat_n(lambda) = (1/n) sum_{i=1}^n L_i(lambda)
2. Find lambda-hat = inf{lambda : [n/(n+1)] R-hat_n(lambda) + B/(n+1) <= alpha}
3. If no such lambda exists, set lambda-hat = lambda_max
4. Deploy C_{lambda-hat} on test points

**Interpretation as an Upper Confidence Bound:** The threshold condition [n/(n+1)] R-hat_n(lambda) + B/(n+1) <= alpha can be rewritten as: (1/(n+1)) [sum L_i(lambda) + B] <= alpha. Since the unknown test loss L_{n+1}(lambda) <= B, this is a worst-case upper bound on the leave-one-out average risk including the test point. The B/(n+1) term is a finite-sample correction that accounts for the unobserved test point.

## 4. Theoretical Guarantees

### Theorem 2.1 (Main Risk Control Guarantee)
Under the monotonicity, right-continuity, and boundedness assumptions, with exchangeable data, the algorithm guarantees:

**E[L_{n+1}(lambda-hat)] <= alpha**

This is an exact finite-sample guarantee -- no asymptotic approximation.

**Proof sketch:** Define lambda-hat' as the infimum computed using all n+1 data points (including the test point). By exchangeability, the average (1/(n+1)) sum_{i=1}^{n+1} L_i(lambda-hat') <= alpha. By monotonicity, lambda-hat >= lambda-hat' (since we replaced the test loss with B >= L_{n+1}), so L_{n+1}(lambda-hat) <= L_{n+1}(lambda-hat'), which inherits the bound.

### Theorem 2.2 (Tightness)
When losses are i.i.d. from continuous distributions:

**E[L_{n+1}(lambda-hat)] >= alpha - 2B/(n+1)**

This shows the guarantee is tight up to O(1/n). For comparison, standard conformal prediction achieves tightness up to 1/(n+1), so there is a factor-of-2 overhead.

### Proposition 2.1 (Necessity of Monotonicity)
For any epsilon > 0, there exists a non-monotone loss function such that E[L_{n+1}(lambda-hat)] >= B - epsilon, regardless of alpha. This means non-monotone losses can make risk control fail completely -- the expected loss can be pushed arbitrarily close to the maximum possible value B.

### Connection to Standard Conformal Prediction
When L_i(lambda) = 1{Y_i not in C_lambda(X_i)} (the coverage loss), the risk control algorithm exactly recovers the standard split conformal prediction quantile selection: lambda-hat equals the ceil((n+1)(1-alpha))/n empirical quantile of conformity scores. Coverage is literally a special case.

## 5. Extensions (Section 4)

### 5.1 Distribution Shift (Covariate Shift)
When P(Y|X) is invariant but P(X) differs between train and test, define importance weights w(x) = dP_test(x)/dP_train(x). The modified algorithm:

**lambda-hat(x) = inf{lambda : [sum_i w(X_i) L_i(lambda) + w(x) B] / [sum_i w(X_i) + w(x)] <= alpha}**

**Proposition 4.1** proves this achieves E[L_{n+1}(lambda-hat)] <= alpha under covariate shift. Note this produces test-point-dependent lambda-hat(x) since the weight w(x) depends on the test input.

**Proposition 4.2 (Total Variation Bound):** Under arbitrary (not just covariate) shift: E[L_{n+1}(lambda-hat)] <= alpha + B * sum_i TV(Z_i, Z_{n+1}), bounding the degradation by total variation distance.

### 5.2 Quantile Risk Control
Instead of controlling E[L_{n+1}], control the beta-quantile: P(L_{n+1}(lambda-hat) > alpha) <= 1-beta. This is achieved by defining a new indicator loss L-tilde_i(lambda) = 1{L_i(lambda) > alpha} and applying the standard algorithm. No new machinery needed.

### 5.3 Multiple/Worst-Case Risks
For a family of losses {L_i(lambda; gamma)}_{gamma in Gamma}, control all simultaneously:

**sup_{gamma} E[L_{n+1}(lambda-hat; gamma)] / alpha(gamma) <= 1**

**Method (Proposition 4.4):** Compute lambda-hat_gamma separately for each gamma, then take lambda-hat = sup_gamma lambda-hat_gamma. Crucially, **no Bonferroni correction is needed** because the supremum is taken over calibration data, preserving exchangeability.

### 5.4 Adversarial Risk Control
Control E[sup_gamma L(lambda; gamma)] <= alpha by defining L-tilde(lambda) = sup_gamma L(lambda; gamma) and applying the main algorithm (Proposition 4.5). This controls the worst-case loss rather than the worst-case expected loss.

### 5.5 U-Statistic Risks
For losses depending on k > 1 test points simultaneously (e.g., pairwise metrics):

**lambda-hat_k = inf{lambda : [k!n!/(n+k)!] sum_{|S|=k} L_S(lambda) + B(1 - (n!)^2 / ((n+k)!(n-k)!)) <= alpha}**

Uses combinatorial weighting to correct for U-statistic bias.

## 6. Experiments

Four applications, all validated over 1000 random calibration/test splits:

| Application | Loss Function | Dataset/Model | Target alpha | Achieved Mean (Std) |
|---|---|---|---|---|
| Tumor Segmentation | False Negative Rate | PraNet, n=1000 | 0.1 | 0.0987 (0.0114) |
| Multilabel Classification | FNR | MS-COCO/TResNet, n=4000 | 0.1 | 0.0996 (0.0052) |
| Hierarchical Classification | Graph Distance | ImageNet+WordNet/ResNet152, n=30000 | 0.05 | 0.0499 (0.0011) |
| Question Answering | 1 - F1 Score | Natural Questions/DPR, n=2500 | 0.3 | 0.2996 (0.0150) |

All empirical risks are tightly controlled just below the target levels.

## 7. Reviewer Feedback (ICLR 2024)

The paper received 6 reviews with ratings: **8, 6, 8, 8, 6, 6** and was accepted as a **spotlight** paper.

### Praise
- "Exciting work" generalizing CP to arbitrary monotone losses (Reviewer nYbV)
- "Very well written and easy to follow" (Reviewer fQpV)
- "Cleanly formulated and executed" experiments, "pleasantly written" (Reviewer pT4W)
- "Theorems 1 and 2 are significant," proofs are "transparent" (Area Chair)
- Strong breadth of extensions and immediate practical impact (Reviewer GsY4)
- "Clear accept" from the Area Chair

### Criticism
- **Lack of baselines:** No comparison to Learn-then-Test (LTT), which handles arbitrary losses via concentration inequalities. Multiple reviewers flagged this.
- **Section 4 extensions lack experiments:** The distribution shift, adversarial, and U-statistic extensions are purely theoretical with no empirical validation.
- **Experimental results "not analyzed at all"** -- results are stated but not discussed in depth (Reviewer fQpV).
- **"More a collection of lots of theoretical results"** than a tightly focused contribution (Reviewer fQpV).
- **Theorem 1 presentation:** Multiple reviewers found the statement hard to parse, with undefined notation (lambda_max, L_i) in the theorem.
- **Monotonicity assumption:** Reviewers wanted more discussion of when real losses are/aren't monotone.
- **Limited NLP depth:** The QA experiment was called "simplistic" (Reviewer pT4W).
- **Data-splitting requirement:** The Area Chair noted this as a limitation, suggesting cross-validated extensions.

### Area Chair Assessment
"The core contribution -- Theorems 1 and 2 -- is significant and the benchmarks are valuable." Recommended acceptance despite concerns, noting that confidence sets on the loss might be "more informative" than expectation bounds.

## 8. Limitations Acknowledged

- **Monotonicity is essential:** The method completely fails for non-monotone losses (Proposition 2.1). Many practical losses (e.g., in object detection where false positive/true detection rates trade off) are non-monotone.
- **Bounded losses required:** The algorithm needs a finite upper bound B. Unbounded losses require modifications.
- **Factor-of-2 tightness overhead:** The lower bound is alpha - 2B/(n+1) vs standard CP's alpha - 1/(n+1).
- **Data splitting:** Requires a held-out calibration set, reducing training data.
- **Appendix A monotonization:** For non-monotone losses, they propose monotonizing via L-tilde(lambda) = sup_{lambda' >= lambda} L(lambda'), but this only yields **asymptotic** guarantees (Theorem A.1), losing the finite-sample property.
- **Distribution shift weights must be known:** The covariate shift extension requires knowing or estimating the importance weights w(x) = dP_test/dP_train.

## 9. Relation to Other Work

- **Learn then Test (Angelopoulos et al., 2021):** Provides high-probability (concentration-based) bounds for arbitrary losses, but CRC's expectation-based guarantees are tighter in finite samples (O(1/n) vs union bound overhead). CRC is also simpler.
- **Standard Conformal Prediction:** CRC strictly generalizes it; coverage is the special case with indicator loss.
- **Follow-up work:** A 2025 paper by Angelopoulos extends CRC to non-monotonic losses with multidimensional parameters, where guarantees depend on algorithmic stability.

## 10. Key Takeaway for Your Project

The paper's core contribution is showing that the exchangeability argument underlying conformal prediction extends far beyond coverage to any monotone loss, with a procedure that is (a) finite-sample valid, (b) tight to O(1/n), (c) trivial to implement (5 lines), and (d) generalizable to distribution shift, multiple risks, quantile control, and U-statistics. The main limitation is the monotonicity requirement, which subsequent work has begun to address.

agentId: aa97db618cccbc2fe (use SendMessage with to: 'aa97db618cccbc2fe' to continue this agent)
&lt;usage>total_tokens: 29798
tool_uses: 24
duration_ms: 237264&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c15396b-d880-4a34-b4e1-5e8708f3487b",
  "isSidechain": false,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "type": "user",
  "uuid": "c710a920-1415-45c6-a67e-454c26c246a1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping analyze a research paper for an ML research project.\n\nPaper: \"Conformal Risk Control\" by Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, Tal Schuster, ICLR 2024, https://arxiv.org/abs/2208.02814\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2208.02814\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2208.02814\n3. Search for OpenReview reviews of this paper (ICLR 2024, search OpenReview for \"Conformal Risk Control\")\n4. Search the web for any discussion/reviews\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified (going beyond coverage to arbitrary loss functions)\n- Their key insight about monotone loss functions and how this generalizes CP\n- Technical method details (the risk control algorithm, how they handle multiple risks, distribution shift extensions)\n- The theoretical guarantees — what exactly do they prove?\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n- How the distribution shift extension works\n\nBe thorough and specific about the technical details. Report back everything you find.",
    "agentId": "aa97db618cccbc2fe",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent -- I got all the reviews. Now I have comprehensive information. Let me compile the full analysis.\n\n---\n\nHere is a detailed analysis of **\"Conformal Risk Control\"** by Angelopoulos, Bates, Fisch, Lei, and Schuster (ICLR 2024, spotlight).\n\n---\n\n## 1. The Problem and Gap Identified\n\nStandard conformal prediction provides a single type of guarantee: **marginal coverage** -- the probability that the true label Y falls inside the prediction set C(X) is at least 1-alpha. The authors identify that this coverage guarantee is too narrow for many practical applications. Real-world tasks often care about controlling richer notions of risk beyond binary \"in or out\" membership:\n\n- In **tumor segmentation**, you want to control the false negative rate (missing cancerous pixels), not just whether the entire segmentation is \"correct.\"\n- In **multilabel classification**, you want to bound the fraction of missed labels.\n- In **hierarchical classification**, you want to control how far (in graph distance) your predictions are from the true label.\n- In **question answering**, you want to control token-level F1-score loss.\n\nNone of these fit cleanly into the standard conformal prediction framework, which only handles the indicator loss L = 1{Y not in C(X)}.\n\n## 2. Key Insight: Monotone Loss Functions\n\nThe central insight is that what makes conformal prediction work is not specific to coverage -- it is the **monotonicity** of the loss in a tuning parameter lambda. In standard CP, as lambda increases, the prediction set C_lambda(X) grows, and the miscoverage loss 1{Y not in C_lambda(X)} is non-increasing in lambda. The authors realize this monotonicity structure is the essential ingredient, and it generalizes far beyond coverage.\n\n**Definition of the setup:** Given calibration data {(X_i, Y_i)}_{i=1}^n drawn exchangeably, define loss functions L_i(lambda) = L(C_lambda(X_i), Y_i) parameterized by lambda in Lambda (a totally ordered set). The losses must satisfy:\n- **Monotonicity (non-increasing):** L_i(lambda) is non-increasing in lambda for all i\n- **Right-continuity:** Technical condition for well-definedness\n- **Boundedness:** L_i(lambda) in (-inf, B] for some finite B\n\nAs lambda increases, the prediction sets get larger/more conservative, and losses decrease. The goal is to find the smallest lambda-hat such that the expected loss on a new test point is controlled: E[L_{n+1}(lambda-hat)] <= alpha.\n\n## 3. Technical Method: The Risk Control Algorithm\n\nThe core algorithm is remarkably simple (5 lines of code):\n\n**Input:** Calibration losses L_1(lambda), ..., L_n(lambda), target level alpha, upper bound B.\n\n**Algorithm:**\n1. Compute empirical risk: R-hat_n(lambda) = (1/n) sum_{i=1}^n L_i(lambda)\n2. Find lambda-hat = inf{lambda : [n/(n+1)] R-hat_n(lambda) + B/(n+1) <= alpha}\n3. If no such lambda exists, set lambda-hat = lambda_max\n4. Deploy C_{lambda-hat} on test points\n\n**Interpretation as an Upper Confidence Bound:** The threshold condition [n/(n+1)] R-hat_n(lambda) + B/(n+1) <= alpha can be rewritten as: (1/(n+1)) [sum L_i(lambda) + B] <= alpha. Since the unknown test loss L_{n+1}(lambda) <= B, this is a worst-case upper bound on the leave-one-out average risk including the test point. The B/(n+1) term is a finite-sample correction that accounts for the unobserved test point.\n\n## 4. Theoretical Guarantees\n\n### Theorem 2.1 (Main Risk Control Guarantee)\nUnder the monotonicity, right-continuity, and boundedness assumptions, with exchangeable data, the algorithm guarantees:\n\n**E[L_{n+1}(lambda-hat)] <= alpha**\n\nThis is an exact finite-sample guarantee -- no asymptotic approximation.\n\n**Proof sketch:** Define lambda-hat' as the infimum computed using all n+1 data points (including the test point). By exchangeability, the average (1/(n+1)) sum_{i=1}^{n+1} L_i(lambda-hat') <= alpha. By monotonicity, lambda-hat >= lambda-hat' (since we replaced the test loss with B >= L_{n+1}), so L_{n+1}(lambda-hat) <= L_{n+1}(lambda-hat'), which inherits the bound.\n\n### Theorem 2.2 (Tightness)\nWhen losses are i.i.d. from continuous distributions:\n\n**E[L_{n+1}(lambda-hat)] >= alpha - 2B/(n+1)**\n\nThis shows the guarantee is tight up to O(1/n). For comparison, standard conformal prediction achieves tightness up to 1/(n+1), so there is a factor-of-2 overhead.\n\n### Proposition 2.1 (Necessity of Monotonicity)\nFor any epsilon > 0, there exists a non-monotone loss function such that E[L_{n+1}(lambda-hat)] >= B - epsilon, regardless of alpha. This means non-monotone losses can make risk control fail completely -- the expected loss can be pushed arbitrarily close to the maximum possible value B.\n\n### Connection to Standard Conformal Prediction\nWhen L_i(lambda) = 1{Y_i not in C_lambda(X_i)} (the coverage loss), the risk control algorithm exactly recovers the standard split conformal prediction quantile selection: lambda-hat equals the ceil((n+1)(1-alpha))/n empirical quantile of conformity scores. Coverage is literally a special case.\n\n## 5. Extensions (Section 4)\n\n### 5.1 Distribution Shift (Covariate Shift)\nWhen P(Y|X) is invariant but P(X) differs between train and test, define importance weights w(x) = dP_test(x)/dP_train(x). The modified algorithm:\n\n**lambda-hat(x) = inf{lambda : [sum_i w(X_i) L_i(lambda) + w(x) B] / [sum_i w(X_i) + w(x)] <= alpha}**\n\n**Proposition 4.1** proves this achieves E[L_{n+1}(lambda-hat)] <= alpha under covariate shift. Note this produces test-point-dependent lambda-hat(x) since the weight w(x) depends on the test input.\n\n**Proposition 4.2 (Total Variation Bound):** Under arbitrary (not just covariate) shift: E[L_{n+1}(lambda-hat)] <= alpha + B * sum_i TV(Z_i, Z_{n+1}), bounding the degradation by total variation distance.\n\n### 5.2 Quantile Risk Control\nInstead of controlling E[L_{n+1}], control the beta-quantile: P(L_{n+1}(lambda-hat) > alpha) <= 1-beta. This is achieved by defining a new indicator loss L-tilde_i(lambda) = 1{L_i(lambda) > alpha} and applying the standard algorithm. No new machinery needed.\n\n### 5.3 Multiple/Worst-Case Risks\nFor a family of losses {L_i(lambda; gamma)}_{gamma in Gamma}, control all simultaneously:\n\n**sup_{gamma} E[L_{n+1}(lambda-hat; gamma)] / alpha(gamma) <= 1**\n\n**Method (Proposition 4.4):** Compute lambda-hat_gamma separately for each gamma, then take lambda-hat = sup_gamma lambda-hat_gamma. Crucially, **no Bonferroni correction is needed** because the supremum is taken over calibration data, preserving exchangeability.\n\n### 5.4 Adversarial Risk Control\nControl E[sup_gamma L(lambda; gamma)] <= alpha by defining L-tilde(lambda) = sup_gamma L(lambda; gamma) and applying the main algorithm (Proposition 4.5). This controls the worst-case loss rather than the worst-case expected loss.\n\n### 5.5 U-Statistic Risks\nFor losses depending on k > 1 test points simultaneously (e.g., pairwise metrics):\n\n**lambda-hat_k = inf{lambda : [k!n!/(n+k)!] sum_{|S|=k} L_S(lambda) + B(1 - (n!)^2 / ((n+k)!(n-k)!)) <= alpha}**\n\nUses combinatorial weighting to correct for U-statistic bias.\n\n## 6. Experiments\n\nFour applications, all validated over 1000 random calibration/test splits:\n\n| Application | Loss Function | Dataset/Model | Target alpha | Achieved Mean (Std) |\n|---|---|---|---|---|\n| Tumor Segmentation | False Negative Rate | PraNet, n=1000 | 0.1 | 0.0987 (0.0114) |\n| Multilabel Classification | FNR | MS-COCO/TResNet, n=4000 | 0.1 | 0.0996 (0.0052) |\n| Hierarchical Classification | Graph Distance | ImageNet+WordNet/ResNet152, n=30000 | 0.05 | 0.0499 (0.0011) |\n| Question Answering | 1 - F1 Score | Natural Questions/DPR, n=2500 | 0.3 | 0.2996 (0.0150) |\n\nAll empirical risks are tightly controlled just below the target levels.\n\n## 7. Reviewer Feedback (ICLR 2024)\n\nThe paper received 6 reviews with ratings: **8, 6, 8, 8, 6, 6** and was accepted as a **spotlight** paper.\n\n### Praise\n- \"Exciting work\" generalizing CP to arbitrary monotone losses (Reviewer nYbV)\n- \"Very well written and easy to follow\" (Reviewer fQpV)\n- \"Cleanly formulated and executed\" experiments, \"pleasantly written\" (Reviewer pT4W)\n- \"Theorems 1 and 2 are significant,\" proofs are \"transparent\" (Area Chair)\n- Strong breadth of extensions and immediate practical impact (Reviewer GsY4)\n- \"Clear accept\" from the Area Chair\n\n### Criticism\n- **Lack of baselines:** No comparison to Learn-then-Test (LTT), which handles arbitrary losses via concentration inequalities. Multiple reviewers flagged this.\n- **Section 4 extensions lack experiments:** The distribution shift, adversarial, and U-statistic extensions are purely theoretical with no empirical validation.\n- **Experimental results \"not analyzed at all\"** -- results are stated but not discussed in depth (Reviewer fQpV).\n- **\"More a collection of lots of theoretical results\"** than a tightly focused contribution (Reviewer fQpV).\n- **Theorem 1 presentation:** Multiple reviewers found the statement hard to parse, with undefined notation (lambda_max, L_i) in the theorem.\n- **Monotonicity assumption:** Reviewers wanted more discussion of when real losses are/aren't monotone.\n- **Limited NLP depth:** The QA experiment was called \"simplistic\" (Reviewer pT4W).\n- **Data-splitting requirement:** The Area Chair noted this as a limitation, suggesting cross-validated extensions.\n\n### Area Chair Assessment\n\"The core contribution -- Theorems 1 and 2 -- is significant and the benchmarks are valuable.\" Recommended acceptance despite concerns, noting that confidence sets on the loss might be \"more informative\" than expectation bounds.\n\n## 8. Limitations Acknowledged\n\n- **Monotonicity is essential:** The method completely fails for non-monotone losses (Proposition 2.1). Many practical losses (e.g., in object detection where false positive/true detection rates trade off) are non-monotone.\n- **Bounded losses required:** The algorithm needs a finite upper bound B. Unbounded losses require modifications.\n- **Factor-of-2 tightness overhead:** The lower bound is alpha - 2B/(n+1) vs standard CP's alpha - 1/(n+1).\n- **Data splitting:** Requires a held-out calibration set, reducing training data.\n- **Appendix A monotonization:** For non-monotone losses, they propose monotonizing via L-tilde(lambda) = sup_{lambda' >= lambda} L(lambda'), but this only yields **asymptotic** guarantees (Theorem A.1), losing the finite-sample property.\n- **Distribution shift weights must be known:** The covariate shift extension requires knowing or estimating the importance weights w(x) = dP_test/dP_train.\n\n## 9. Relation to Other Work\n\n- **Learn then Test (Angelopoulos et al., 2021):** Provides high-probability (concentration-based) bounds for arbitrary losses, but CRC's expectation-based guarantees are tighter in finite samples (O(1/n) vs union bound overhead). CRC is also simpler.\n- **Standard Conformal Prediction:** CRC strictly generalizes it; coverage is the special case with indicator loss.\n- **Follow-up work:** A 2025 paper by Angelopoulos extends CRC to non-monotonic losses with multidimensional parameters, where guarantees depend on algorithmic stability.\n\n## 10. Key Takeaway for Your Project\n\nThe paper's core contribution is showing that the exchangeability argument underlying conformal prediction extends far beyond coverage to any monotone loss, with a procedure that is (a) finite-sample valid, (b) tight to O(1/n), (c) trivial to implement (5 lines), and (d) generalizable to distribution shift, multiple risks, quantile control, and U-statistics. The main limitation is the monotonicity requirement, which subsequent work has begun to address."
      }
    ],
    "totalDurationMs": 237264,
    "totalTokens": 29798,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1626,
      "cache_read_input_tokens": 24807,
      "output_tokens": 3364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1626
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3364,
          "cache_read_input_tokens": 24807,
          "cache_creation_input_tokens": 1626,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1626,
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
      "bashCount": 4,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "5c15396b-d880-4a34-b4e1-5e8708f3487b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-30T06:31:59.263Z_

<details><summary>↩ Tool result · `toolu_01CHyrbt7KZRHa9MPkWsHhua`</summary>

```text
Excellent -- I now have the full OpenReview reviews. Let me compile all findings into a comprehensive report.

---

## Detailed Analysis: "Large Language Model Validity via Enhanced Conformal Prediction Methods"

**Authors:** John J. Cherian, Isaac Gibbs, Emmanuel J. Candes
**Venue:** NeurIPS 2024 (poster)
**ArXiv:** 2406.09714 (v1: June 14, 2024; v2: October 31, 2024)

---

### 1. THE PROBLEM / GAP IDENTIFIED

The paper identifies two critical deficiencies in existing conformal factuality methods (specifically Mohri & Hashimoto's conformal factuality framework):

**Deficiency 1 -- Lack of Conditional Validity:** Prior methods provide only *marginal* guarantees averaged over random test prompts. The authors demonstrate empirically that the probability of output correctness varies substantially based on the prompt's characteristics. Specifically, correctness probability is "substantially lower for responses whose subjects are likely to be underrepresented in the model's training corpus." Their Wikipedia biography experiments show this concretely: marginal conformal achieves 90% nominal coverage overall, but conditional coverage drops to approximately 70% for low-popularity articles (those with fewer than 100 Wikipedia page views), precisely the cases where errors are most dangerous. High-traffic articles (>1M views) achieve near-perfect coverage.

**Deficiency 2 -- Over-Filtering / Utility Destruction:** Because scoring functions are imperfect, the filtering step removes far too many accurate claims. When calibrated for a 90% factuality guarantee, practical filtering becomes nearly complete -- retaining only ~24% of claims -- rendering outputs useless despite the high accuracy guarantee.

---

### 2. KEY INSIGHT: CONDITIONAL CONFORMAL GUARANTEES FOR LLMS

The core insight is that marginal conformal prediction guarantees are insufficient for LLM safety because they average over all prompts, hiding dangerous variation across topics/groups. The authors propose replacing marginal guarantees with *function-class conditional guarantees* that hold uniformly over user-specified subgroups.

Their secondary insight is equally important: when conditional guarantees require too much filtering, the method should *adaptively weaken the guarantee* (lower the confidence level) for specific prompts rather than uniformly demanding 90% factuality everywhere. This produces "self-aware" outputs that explicitly report their factuality probability, enabling end-users to decide whether a weaker guarantee is acceptable.

---

### 3. TECHNICAL METHOD DETAILS

#### 3.1 Foundation: Conditional Conformal Prediction (Gibbs et al. 2023)

They build on Gibbs et al.'s framework, which replaces exact conditional coverage (impossible without strong assumptions) with guarantees holding over a user-specified linear function class F. The key property: for all f in F,

> E[f(X_{n+1}) * (1{Y_{n+1} in C_hat(X_{n+1})} - (1-alpha))] = 0

This is implemented via *augmented quantile regression* using the pinball loss l_alpha(r) = (1-alpha)[r]_+ + alpha[r]_-. The test point's conformity score is imputed and included in the regression, yielding a data-dependent threshold g_S(X) for each input.

#### 3.2 Generalization to Monotone Losses (Theorem 3.1)

The paper's first theoretical contribution generalizes conditional conformal from set coverage to arbitrary monotone losses L(.,.). They define a conformity score:

> S(C_i, W_i) := inf{tau | L(F(C_i; tau), W_i) <= lambda}

This is the minimum threshold tau ensuring the loss on the filtered claims stays below tolerance lambda. Key assumptions: (1) abstention yields zero loss: L(empty, .) = 0; (2) loss is monotone in filtered set size; (3) exchangeability of calibration data.

**Theorem 3.1** guarantees: for linear function class F = {Phi(X)^T beta | beta in R^d}, the procedure achieves group-conditional control: P(L <= lambda | X in G) = 1-alpha for all groups G in the class.

#### 3.3 Level-Adaptive Conformal Prediction (Theorem 3.2)

This is the paper's most novel contribution. Instead of a fixed error level alpha, they allow alpha(X) to vary per test point. The modified quantile regression uses data-dependent pinball losses l_{alpha(X_i)} for each calibration point.

**Theorem 3.2** guarantees group-conditional calibration:

> P(F_hat(C_{n+1}) factual | alpha_{n+1} in I, P_{n+1} in G) = E[alpha_{n+1} | alpha_{n+1} in I, P_{n+1} in G]

This means: among prompts where the method issues a 70-80% factuality probability, the outputs are actually factual 70-80% of the time.

**Learning alpha(.):** Uses a two-fold data split. Fold 1 estimates alpha(.) via regression targeting a specific claim retention rate (e.g., 70%). Fold 2 runs level-adaptive conformal with the estimated alpha(.).

#### 3.4 Conditional Boosting: Differentiable Score Optimization

The optimization problem: find score parameters theta maximizing retained claims:

> theta* = argmax_theta sum_i sum_j 1{p_theta(P_{n+i}, C_{(n+i)j}) >= tau_hat_i}

The challenge is that tau_hat_i(theta) depends on theta through the quantile regression, creating a non-differentiable dependency.

**Proposition 3.1** provides the key technical result: for linear function classes, the quantile regression is a linear program. The optimal basis B (active constraints) can be explicitly identified, yielding:

> tau_hat_i(theta) = Phi(X_{n+i})^T (Phi(X)_B^{-1} S_B(theta))

The derivative is:

> d/d_theta tau_hat_i(theta) = Phi(X_{n+i})^T (Phi(X)_B^{-1} d/d_theta S_B(theta))

The indicator function is replaced with a sigmoid approximation, and standard optimizers (Adam, lr=0.001, 500 steps) are used. This critically differs from Stutz et al.'s ConfTr (which optimizes through *marginal* conformal and can violate conditional guarantees).

#### 3.5 Scoring Functions

Four candidate scores are combined linearly:
1. **Frequency score** -- how often a claim appears across multiple LLM generations
2. **Self-evaluation score** -- the LLM's own probability/classification of claim truth
3. **Ordinal score** -- ranking position within response claims
4. **Token-probability score** -- log-probability assigned to single-token self-evaluation

The optimized linear combination p_theta(P,C) = theta_1*freq + theta_2*self_eval + theta_3*ordinal + theta_4*token_prob is learned via conditional boosting.

---

### 4. CONNECTION TO CONFORMAL FACTUALITY (MOHRI & HASHIMOTO)

The paper directly builds on and extends Mohri & Hashimoto's conformal factuality framework. In that baseline:
- An LLM generates a response to a prompt
- The response is decomposed into atomic claims
- Each claim is scored by a scoring function p(P, C)
- Claims with scores below a threshold tau (calibrated via split conformal prediction) are filtered out
- The conformity score is S(C_i, W_i) = inf{tau | all retained claims are true}

The authors generalize this in three ways:
1. Replace the *marginal* guarantee with *conditional* guarantees (holding across subgroups)
2. Generalize from binary loss (0 false claims) to arbitrary monotone losses (e.g., at most 3 false claims for biographies where scoring is weaker)
3. Add level-adaptive calibration so the guarantee strength varies by prompt difficulty

The authors use Mohri & Hashimoto's biography dataset setup as one of their experimental testbeds and demonstrate that the marginal approach shows systematically biased coverage across Wikipedia article popularity levels.

---

### 5. EXPERIMENTAL RESULTS

**Synthetic data:** Heteroscedastic regression demonstrating that ConfTr (marginal boosting) achieves shorter intervals but with degraded conditional validity, while conditional boosting maintains near-perfect conditional coverage.

**MedLFQA (Medical QA):** 5,851 questions from HealthSearchQA, K-QA, LiveQA, MedicationQA. Uses GPT-3.5-Turbo for generation, GPT-4o for claim parsing, GPT-3.5-Turbo for evaluation. At fixed alpha=0.1 (90% guarantee): unboosted scores retain 24% of claims; conditional boosting retains 39%. Level-adaptive (70% retention target): issued probabilities range 50-85%, verified well-calibrated.

**Wikipedia Biographies:** 8,516 biographies using FActScore-style evaluation. Loss = count of false claims, target lambda=3. Marginal conformal achieves 90% nominal but coverage drops to ~70% for low-popularity articles. Conditional conformal maintains calibration across all view count groups. Boosting improves retention from ~35% to ~50%.

---

### 6. REVIEWER FEEDBACK (OpenReview)

**Decision:** Accept (poster)

**Ratings:** Reviewer 1: 5->6 (confidence 5), Reviewer 2: 7 (confidence 3), Reviewer 3: 7 (confidence 4), Reviewer 4: 6 (confidence 4)

**Praise:**
- Originality and soundness of conditional boosting procedure commended
- "Non-trivial generalization of Gibbs et al. (2023) incorporating general losses"
- Addresses critical gaps in current approaches; technically sound
- Well-structured and clearly written paper
- Important problem (LLM hallucination) with practical relevance

**Criticisms:**
- **Reviewer 1 (tBPp):** Figure 1 makes unfair comparison (90% baseline vs. 76% proposed); questioned practicality of "at most 3 wrong claims" guarantee ("can still not point to which one is wrong"); exchangeability assumption severely limits applicability; insufficient experimental validation ("single toy experiment with Wiki dataset")
- **Reviewer 3 (9DaN):** Lack of ablations comparing level-adaptive vs. fixed conditional conformal; difficult to understand experimental setup and variations; missing comparisons with alternative frameworks
- **Reviewer 4 (CDbE):** "Rigorous proof lacking about why prediction set leads to conformal guarantee"; limited discussion of conformal risk control frameworks; missing related work on LLM risk control (Kang et al., Quach et al.); questioned whether different alpha_i values in pinball loss break the original formulation

**Program Chairs' Camera-Ready Requirements:** Acknowledge limitations more explicitly; provide more examples of useful scenarios; include more details on advantages/disadvantages vs. conformal risk control; consider ablation and experiment organization improvements.

---

### 7. LIMITATIONS ACKNOWLEDGED

1. **Function class size trade-off:** Large function classes F (for stronger conditional guarantees) slow computation and reduce claim retention. The paper explores insufficient function classes in Appendix B.2.
2. **Basis stability:** Proposition 3.1 requires the LP basis B to remain locally invariant under theta perturbation; requires dithering (adding noise) if violated.
3. **Annotation quality:** The biography experiment uses FActScore approximation rather than human annotation. Scoring is less correlated with actual factuality than in the medical domain, necessitating the weaker guarantee (<=3 errors vs. 0 errors).
4. **Data splitting:** Level-adaptive procedure requires a two-fold split, reducing effective sample size.
5. **Exchangeability assumption:** All guarantees assume exchangeability of calibration data; real deployment may violate this.
6. **Score dependence:** Methods depend on quality of underlying score function; without good base scores, even boosting provides limited improvement.

---

### Key Files/Resources

- Paper: https://arxiv.org/abs/2406.09714
- OpenReview: https://openreview.net/forum?id=JD3NYpeQ3R
- NeurIPS proceedings: https://proceedings.neurips.cc/paper_files/paper/2024/hash/d02ff1aeaa5c268dc34790dd1ad21526-Abstract-Conference.html
- Code repositories: conformal-safety and conditional-conformal on GitHub
- External analysis by Davide Beltrame (Feb 2026): https://bsmachinelearning.com/projects/llm-validity/ -- proposes "response-level conformalization under dependent claims" as an extension

agentId: a7659e1f80804e6cb (use SendMessage with to: 'a7659e1f80804e6cb' to continue this agent)
&lt;usage>total_tokens: 30576
tool_uses: 19
duration_ms: 255389&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d1ef539d-6fa7-4fc2-ae81-840465ef1ce0",
  "isSidechain": false,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "type": "user",
  "uuid": "28b8b7cd-f92d-4b29-80e1-7e6d5f57b34c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping analyze a research paper for an ML research project.\n\nPaper: \"Large Language Model Validity via Enhanced Conformal Prediction Methods\" by John J. Cherian, Isaac Gibbs, Emmanuel J. Candès, NeurIPS 2024, https://arxiv.org/abs/2406.09714\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2406.09714\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2406.09714\n3. Search for OpenReview reviews of this paper (NeurIPS 2024, search OpenReview for the title)\n4. Search the web for any discussion/reviews\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified (especially re: conditional validity varying by topic)\n- Their key insight about conditional conformal guarantees for LLMs\n- Technical method details (how they achieve conditional validity, differentiable scoring function optimization, what scores they use)\n- Connection to conformal factuality (Mohri & Hashimoto)\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n\nBe thorough and specific about the technical details. Report back everything you find.",
    "agentId": "a7659e1f80804e6cb",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Excellent -- I now have the full OpenReview reviews. Let me compile all findings into a comprehensive report.\n\n---\n\n## Detailed Analysis: \"Large Language Model Validity via Enhanced Conformal Prediction Methods\"\n\n**Authors:** John J. Cherian, Isaac Gibbs, Emmanuel J. Candes\n**Venue:** NeurIPS 2024 (poster)\n**ArXiv:** 2406.09714 (v1: June 14, 2024; v2: October 31, 2024)\n\n---\n\n### 1. THE PROBLEM / GAP IDENTIFIED\n\nThe paper identifies two critical deficiencies in existing conformal factuality methods (specifically Mohri & Hashimoto's conformal factuality framework):\n\n**Deficiency 1 -- Lack of Conditional Validity:** Prior methods provide only *marginal* guarantees averaged over random test prompts. The authors demonstrate empirically that the probability of output correctness varies substantially based on the prompt's characteristics. Specifically, correctness probability is \"substantially lower for responses whose subjects are likely to be underrepresented in the model's training corpus.\" Their Wikipedia biography experiments show this concretely: marginal conformal achieves 90% nominal coverage overall, but conditional coverage drops to approximately 70% for low-popularity articles (those with fewer than 100 Wikipedia page views), precisely the cases where errors are most dangerous. High-traffic articles (>1M views) achieve near-perfect coverage.\n\n**Deficiency 2 -- Over-Filtering / Utility Destruction:** Because scoring functions are imperfect, the filtering step removes far too many accurate claims. When calibrated for a 90% factuality guarantee, practical filtering becomes nearly complete -- retaining only ~24% of claims -- rendering outputs useless despite the high accuracy guarantee.\n\n---\n\n### 2. KEY INSIGHT: CONDITIONAL CONFORMAL GUARANTEES FOR LLMS\n\nThe core insight is that marginal conformal prediction guarantees are insufficient for LLM safety because they average over all prompts, hiding dangerous variation across topics/groups. The authors propose replacing marginal guarantees with *function-class conditional guarantees* that hold uniformly over user-specified subgroups.\n\nTheir secondary insight is equally important: when conditional guarantees require too much filtering, the method should *adaptively weaken the guarantee* (lower the confidence level) for specific prompts rather than uniformly demanding 90% factuality everywhere. This produces \"self-aware\" outputs that explicitly report their factuality probability, enabling end-users to decide whether a weaker guarantee is acceptable.\n\n---\n\n### 3. TECHNICAL METHOD DETAILS\n\n#### 3.1 Foundation: Conditional Conformal Prediction (Gibbs et al. 2023)\n\nThey build on Gibbs et al.'s framework, which replaces exact conditional coverage (impossible without strong assumptions) with guarantees holding over a user-specified linear function class F. The key property: for all f in F,\n\n> E[f(X_{n+1}) * (1{Y_{n+1} in C_hat(X_{n+1})} - (1-alpha))] = 0\n\nThis is implemented via *augmented quantile regression* using the pinball loss l_alpha(r) = (1-alpha)[r]_+ + alpha[r]_-. The test point's conformity score is imputed and included in the regression, yielding a data-dependent threshold g_S(X) for each input.\n\n#### 3.2 Generalization to Monotone Losses (Theorem 3.1)\n\nThe paper's first theoretical contribution generalizes conditional conformal from set coverage to arbitrary monotone losses L(.,.). They define a conformity score:\n\n> S(C_i, W_i) := inf{tau | L(F(C_i; tau), W_i) <= lambda}\n\nThis is the minimum threshold tau ensuring the loss on the filtered claims stays below tolerance lambda. Key assumptions: (1) abstention yields zero loss: L(empty, .) = 0; (2) loss is monotone in filtered set size; (3) exchangeability of calibration data.\n\n**Theorem 3.1** guarantees: for linear function class F = {Phi(X)^T beta | beta in R^d}, the procedure achieves group-conditional control: P(L <= lambda | X in G) = 1-alpha for all groups G in the class.\n\n#### 3.3 Level-Adaptive Conformal Prediction (Theorem 3.2)\n\nThis is the paper's most novel contribution. Instead of a fixed error level alpha, they allow alpha(X) to vary per test point. The modified quantile regression uses data-dependent pinball losses l_{alpha(X_i)} for each calibration point.\n\n**Theorem 3.2** guarantees group-conditional calibration:\n\n> P(F_hat(C_{n+1}) factual | alpha_{n+1} in I, P_{n+1} in G) = E[alpha_{n+1} | alpha_{n+1} in I, P_{n+1} in G]\n\nThis means: among prompts where the method issues a 70-80% factuality probability, the outputs are actually factual 70-80% of the time.\n\n**Learning alpha(.):** Uses a two-fold data split. Fold 1 estimates alpha(.) via regression targeting a specific claim retention rate (e.g., 70%). Fold 2 runs level-adaptive conformal with the estimated alpha(.).\n\n#### 3.4 Conditional Boosting: Differentiable Score Optimization\n\nThe optimization problem: find score parameters theta maximizing retained claims:\n\n> theta* = argmax_theta sum_i sum_j 1{p_theta(P_{n+i}, C_{(n+i)j}) >= tau_hat_i}\n\nThe challenge is that tau_hat_i(theta) depends on theta through the quantile regression, creating a non-differentiable dependency.\n\n**Proposition 3.1** provides the key technical result: for linear function classes, the quantile regression is a linear program. The optimal basis B (active constraints) can be explicitly identified, yielding:\n\n> tau_hat_i(theta) = Phi(X_{n+i})^T (Phi(X)_B^{-1} S_B(theta))\n\nThe derivative is:\n\n> d/d_theta tau_hat_i(theta) = Phi(X_{n+i})^T (Phi(X)_B^{-1} d/d_theta S_B(theta))\n\nThe indicator function is replaced with a sigmoid approximation, and standard optimizers (Adam, lr=0.001, 500 steps) are used. This critically differs from Stutz et al.'s ConfTr (which optimizes through *marginal* conformal and can violate conditional guarantees).\n\n#### 3.5 Scoring Functions\n\nFour candidate scores are combined linearly:\n1. **Frequency score** -- how often a claim appears across multiple LLM generations\n2. **Self-evaluation score** -- the LLM's own probability/classification of claim truth\n3. **Ordinal score** -- ranking position within response claims\n4. **Token-probability score** -- log-probability assigned to single-token self-evaluation\n\nThe optimized linear combination p_theta(P,C) = theta_1*freq + theta_2*self_eval + theta_3*ordinal + theta_4*token_prob is learned via conditional boosting.\n\n---\n\n### 4. CONNECTION TO CONFORMAL FACTUALITY (MOHRI & HASHIMOTO)\n\nThe paper directly builds on and extends Mohri & Hashimoto's conformal factuality framework. In that baseline:\n- An LLM generates a response to a prompt\n- The response is decomposed into atomic claims\n- Each claim is scored by a scoring function p(P, C)\n- Claims with scores below a threshold tau (calibrated via split conformal prediction) are filtered out\n- The conformity score is S(C_i, W_i) = inf{tau | all retained claims are true}\n\nThe authors generalize this in three ways:\n1. Replace the *marginal* guarantee with *conditional* guarantees (holding across subgroups)\n2. Generalize from binary loss (0 false claims) to arbitrary monotone losses (e.g., at most 3 false claims for biographies where scoring is weaker)\n3. Add level-adaptive calibration so the guarantee strength varies by prompt difficulty\n\nThe authors use Mohri & Hashimoto's biography dataset setup as one of their experimental testbeds and demonstrate that the marginal approach shows systematically biased coverage across Wikipedia article popularity levels.\n\n---\n\n### 5. EXPERIMENTAL RESULTS\n\n**Synthetic data:** Heteroscedastic regression demonstrating that ConfTr (marginal boosting) achieves shorter intervals but with degraded conditional validity, while conditional boosting maintains near-perfect conditional coverage.\n\n**MedLFQA (Medical QA):** 5,851 questions from HealthSearchQA, K-QA, LiveQA, MedicationQA. Uses GPT-3.5-Turbo for generation, GPT-4o for claim parsing, GPT-3.5-Turbo for evaluation. At fixed alpha=0.1 (90% guarantee): unboosted scores retain 24% of claims; conditional boosting retains 39%. Level-adaptive (70% retention target): issued probabilities range 50-85%, verified well-calibrated.\n\n**Wikipedia Biographies:** 8,516 biographies using FActScore-style evaluation. Loss = count of false claims, target lambda=3. Marginal conformal achieves 90% nominal but coverage drops to ~70% for low-popularity articles. Conditional conformal maintains calibration across all view count groups. Boosting improves retention from ~35% to ~50%.\n\n---\n\n### 6. REVIEWER FEEDBACK (OpenReview)\n\n**Decision:** Accept (poster)\n\n**Ratings:** Reviewer 1: 5->6 (confidence 5), Reviewer 2: 7 (confidence 3), Reviewer 3: 7 (confidence 4), Reviewer 4: 6 (confidence 4)\n\n**Praise:**\n- Originality and soundness of conditional boosting procedure commended\n- \"Non-trivial generalization of Gibbs et al. (2023) incorporating general losses\"\n- Addresses critical gaps in current approaches; technically sound\n- Well-structured and clearly written paper\n- Important problem (LLM hallucination) with practical relevance\n\n**Criticisms:**\n- **Reviewer 1 (tBPp):** Figure 1 makes unfair comparison (90% baseline vs. 76% proposed); questioned practicality of \"at most 3 wrong claims\" guarantee (\"can still not point to which one is wrong\"); exchangeability assumption severely limits applicability; insufficient experimental validation (\"single toy experiment with Wiki dataset\")\n- **Reviewer 3 (9DaN):** Lack of ablations comparing level-adaptive vs. fixed conditional conformal; difficult to understand experimental setup and variations; missing comparisons with alternative frameworks\n- **Reviewer 4 (CDbE):** \"Rigorous proof lacking about why prediction set leads to conformal guarantee\"; limited discussion of conformal risk control frameworks; missing related work on LLM risk control (Kang et al., Quach et al.); questioned whether different alpha_i values in pinball loss break the original formulation\n\n**Program Chairs' Camera-Ready Requirements:** Acknowledge limitations more explicitly; provide more examples of useful scenarios; include more details on advantages/disadvantages vs. conformal risk control; consider ablation and experiment organization improvements.\n\n---\n\n### 7. LIMITATIONS ACKNOWLEDGED\n\n1. **Function class size trade-off:** Large function classes F (for stronger conditional guarantees) slow computation and reduce claim retention. The paper explores insufficient function classes in Appendix B.2.\n2. **Basis stability:** Proposition 3.1 requires the LP basis B to remain locally invariant under theta perturbation; requires dithering (adding noise) if violated.\n3. **Annotation quality:** The biography experiment uses FActScore approximation rather than human annotation. Scoring is less correlated with actual factuality than in the medical domain, necessitating the weaker guarantee (<=3 errors vs. 0 errors).\n4. **Data splitting:** Level-adaptive procedure requires a two-fold split, reducing effective sample size.\n5. **Exchangeability assumption:** All guarantees assume exchangeability of calibration data; real deployment may violate this.\n6. **Score dependence:** Methods depend on quality of underlying score function; without good base scores, even boosting provides limited improvement.\n\n---\n\n### Key Files/Resources\n\n- Paper: https://arxiv.org/abs/2406.09714\n- OpenReview: https://openreview.net/forum?id=JD3NYpeQ3R\n- NeurIPS proceedings: https://proceedings.neurips.cc/paper_files/paper/2024/hash/d02ff1aeaa5c268dc34790dd1ad21526-Abstract-Conference.html\n- Code repositories: conformal-safety and conditional-conformal on GitHub\n- External analysis by Davide Beltrame (Feb 2026): https://bsmachinelearning.com/projects/llm-validity/ -- proposes \"response-level conformalization under dependent claims\" as an extension"
      }
    ],
    "totalDurationMs": 255389,
    "totalTokens": 30576,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1906,
      "cache_read_input_tokens": 25580,
      "output_tokens": 3089,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1906
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3089,
          "cache_read_input_tokens": 25580,
          "cache_creation_input_tokens": 1906,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1906,
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
  "sourceToolAssistantUUID": "d1ef539d-6fa7-4fc2-ae81-840465ef1ce0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
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
  "leafUuid": "28b8b7cd-f92d-4b29-80e1-7e6d5f57b34c",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze poisoning-robust conformal prediction for RAG systems",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Tool result

_source line 24 · 2026-05-30T06:32:03.462Z_

<details><summary>↩ Tool result · `toolu_017FGZPJnxzztF5qSD4xtA4D`</summary>

```text
Now I have comprehensive information from all sources. Here is my detailed summary:

---

## Detailed Analysis: "Conformal Language Modeling" (Quach, Fisch, Schuster, Yala, Sohn, Jaakkola, Barzilay -- ICLR 2024)

### 1. The Problem/Gap Identified

The paper addresses a fundamental barrier in applying conformal prediction (CP) to generative language models. Standard CP works by constructing prediction sets from a finite, enumerable output space -- you score each possible output and include those above a threshold. For language models, the output space is combinatorially explosive (all possible text sequences), making exhaustive enumeration intractable. Prior CP methods were limited to classification tasks or settings with bounded output spaces. No existing framework could provide distribution-free statistical guarantees for free-text generation from LMs.

The authors frame this as: how do you construct a prediction set with coverage guarantees when you cannot even enumerate the candidate outputs?

### 2. Key Insight: Sampling-Based Conformal Prediction via Stopping and Rejection Rules

The central insight is to replace exhaustive enumeration with a **calibrated sampling procedure**. Instead of scoring all possible outputs, they:

1. **Sample** outputs from the LM sequentially
2. Apply a **rejection rule** to filter out low-quality or redundant samples
3. Apply a **stopping rule** to determine when enough diverse, high-quality samples have been collected to guarantee coverage

This transforms the intractable problem of conformal prediction over an infinite space into a tractable one: calibrating when to stop sampling and what to keep/reject.

### 3. Technical Method Details

**Formal Setting:**
- Input: X in X (prompt)
- Output space: Y (all possible text sequences -- unbounded)
- Admissibility function: A: Y -> {0,1} -- binary ground truth for whether a generated text is "acceptable"
- Language model: p_theta(y|x) -- can only sample from, not enumerate

**Algorithm 1 (Conformal Sampling with Rejection):**
The procedure is parameterized by lambda = (lambda_1, lambda_2, lambda_3):

For each sample y_k drawn from p_theta(y|x):
1. **Quality check**: reject if Q(x, y_k) < lambda_2 (where Q is a quality scoring function, e.g., LM log-likelihood)
2. **Diversity check**: reject if max similarity to existing samples exceeds lambda_1 (similarity measured by ROUGE-L via function S)
3. If both checks pass, add to candidate set C_lambda
4. **Stop** when confidence function F(C_lambda) >= lambda_3 or budget k_max is exhausted

**Confidence Functions Tested (four variants):**
- **First-K**: F(C) = |C| -- just use set size as a proxy
- **First-K + reject**: Same but with rejection enabled
- **Max**: F(C) = max{Q(y) : y in C} -- best single item's quality score
- **Sum**: F(C) = sum of Q(y) over y in C -- aggregate confidence

**Calibration via Learn Then Test (LTT) Framework:**

The three-dimensional lambda is calibrated using the LTT framework of Angelopoulos et al. For each candidate lambda configuration:

- Compute empirical risk on calibration data: R_hat_n(lambda) = (1/n) * sum_i 1{no y in C_lambda(X_i) has A_i(y)=1}
- Compute p-values using binomial tails: p_lambda^BT = P(Binom(n, epsilon) <= n * R_hat_n(lambda))
- This tests H_lambda: E[L_test(lambda)] > epsilon (null = the configuration is bad)
- Apply FWER-controlling multiple testing (Bonferroni/Holm) at level delta across all lambda in the grid Lambda
- Valid configurations Lambda_valid = those whose nulls are rejected

**Selection among valid configurations (Equation 7):**
lambda_hat = argmin over Lambda_valid of: (1/n) * sum_i [rho_1 * |C_lambda(X_i)| + rho_2 * (S_lambda(X_i) - S*(X_i))+ / S_lambda(X_i)]

This balances two competing objectives: (1) small prediction set size and (2) sampling efficiency (not drawing too many excess samples that get rejected). They use rho_1 = rho_2 = 0.5.

**Pareto Testing** is used to efficiently search the 3D lambda space by exploiting monotonicity properties (e.g., higher lambda_3 means more stringent stopping, which generally increases set size and coverage).

**Component-Level Analysis (Inner Conformal Procedure):**
For verbose outputs (radiology reports, summaries), they extend to component selection:

C_gamma^inner(x) = {e in union of E(y) for y in C_lambda(x) : F^c(e) >= gamma}

Where E: Y -> 2^Y decomposes text into components (sentences), F^c scores component confidence, and A^c judges individual component correctness. The gamma threshold is calibrated separately.

### 4. Theoretical Guarantees

**Theorem 4.2 (Main Result -- Sampling-based coverage):**
The prediction set C_lambda_hat(X_test) satisfies:

P(P(exists y in C_lambda_hat(X_test): A_test(y) = 1 | D_cal) >= 1 - epsilon) >= 1 - delta

- Outer probability: over draws of calibration set D_cal
- Inner probability: over test inputs
- epsilon: error tolerance (target risk level)
- delta: confidence parameter

This is **distribution-free** and **finite-sample valid**. It guarantees that with high probability over calibration data, the returned set contains at least one admissible answer with probability at least 1 - epsilon.

**Theorem 4.4 (Component-level coverage):**
P(P(A^c_test(e) = 1, for all e in C_gamma^inner(X_test) | D_cal) >= 1 - alpha) >= 1 - delta

This guarantees that every component in the filtered inner set is correct with high probability.

By union bound, both theorems hold simultaneously with probability >= 1 - 2*delta.

The proof relies on Lemma 4.1 establishing that the binomial tail p-values are valid for the risk-control hypothesis testing, which in turn inherits from the LTT framework.

### 5. Applications Demonstrated

**Radiology Report Generation (MIMIC-CXR):**
- Model: ViT encoder + GPT2 decoder
- Full admissibility: Clinical Efficacy metric -- 14 CheXbert-extracted labels must exactly match reference
- Component admissibility: ROUGE-L >= 0.4 vs. reference findings (sentence-level)

**News Summarization (CNN/DailyMail):**
- Model: Fine-tuned T5-XL
- Full admissibility: ROUGE-L >= 0.35 vs. human summaries
- Component admissibility: ROUGE-L >= 0.4 per sentence

**Open-Domain QA (TriviaQA):**
- Model: LLaMA-13B (32-shot prompting, no fine-tuning)
- Admissibility: Exact match after normalization
- No component-level evaluation (answers are atomic)

**Key Results:**
- All methods achieve valid coverage (loss <= target epsilon), confirming theoretical guarantees hold empirically
- Likelihood-based approaches (Max, Sum) produce set sizes less than 50% of First-K baseline for QA
- Max outperforms Sum on excess samples metric across all tasks
- Component-level selection with application-specific classifiers outperforms model logits alone
- k_max = 20 was used as the sampling budget

### 6. Reviewer Feedback (ICLR 2024 OpenReview)

The paper received four reviews with ratings: **8, 8, 3, 6** and was accepted as a **poster**.

**Strengths praised by reviewers:**
- First extension of conformal prediction to LM generation with rigorous guarantees (novel)
- Practical framework giving acceptance/rejection/sampling rules with risk control guarantees
- Generally well-written with clear technical detail
- Comprehensive experiments across three diverse tasks
- Component-level guarantees for identifying correct sub-parts

**Weaknesses and criticisms:**
- **Dense notation** in first 7.5 pages limits accessibility to broader audience
- **ROUGE-L dependency**: Using lexical similarity as the admission function is problematic and may conflict with human judgment
- **Circular logic concern**: ROUGE used both for duplicate detection and quality assessment
- **Calibration data requirement**: Method assumes access to labeled calibration set with known admission functions
- **Practicality questioned**: One reviewer (3/10) questioned "what problem this is solving" and whether it would outperform simpler baselines
- **High achievable risk on MIMIC-CXR**: Questioning practical utility
- **Scalability concern**: Benefits may diminish with larger, better-calibrated models
- **Pareto Testing only described at high level**; Proposition 4.4 lacked experimental validation initially

**Author responses addressed:**
- Clarified that test set answers are NOT used in the stopping rule (only for calibration/evaluation)
- Defended ROUGE consistency via transitive arguments
- Added First-K with rejection for fairer baseline comparison
- Added experimental validation for Proposition 4.4 (Figure G.1)
- Enhanced Pareto Testing explanation

**Area Chair** found the work "well executed" with "broadly useful" contributions.

### 7. Limitations Acknowledged

From the paper (Appendix B) and subsequent analysis:

1. **Calibration data dependency**: Results depend heavily on calibration set quality and size; requires ground-truth admission labels
2. **Exchangeability assumption**: Calibration data must be exchangeable with test data
3. **Finite sampling budget**: With k_max = 20, achievable error tolerance ranges are limited; very low epsilon may be unachievable
4. **Admission function design**: Requires reliable, potentially expensive or subjective admission functions for each task
5. **Black-box LM assumption**: Method requires sampling capability but cannot guarantee coverage for poorly-calibrated models
6. **Algorithm termination**: Not formally guaranteed for infinite k_max
7. **Interpretability**: Follow-up work (Mohri & Hashimoto, "Language Models with Conformal Factuality Guarantees," 2024) noted that the approach returns opaque sets of sequences that are "difficult to interpret and act upon," and that the space of all sequences necessitates approximations that limit practical utility
8. **Conditional validity**: The guarantees are marginal, not conditional -- trustworthiness may vary by topic/domain
9. **Independent claims assumption**: Does not generalize to reasoning tasks where correctness of each step depends on preceding steps (addressed by follow-up "Conformal Language Model Reasoning" at ICLR 2025)

### 8. Code and Reproducibility

The authors released code at `github.com/Varal7/conformal-language-modeling` (95% Jupyter notebooks, 5% Python). All datasets are publicly accessible, and hyperparameters are specified in the paper and appendices.

agentId: a5c534cc96025704b (use SendMessage with to: 'a5c534cc96025704b' to continue this agent)
&lt;usage>total_tokens: 30836
tool_uses: 25
duration_ms: 252015&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8af694dc-a40a-408d-8d68-e53a31f016c8",
  "isSidechain": false,
  "promptId": "36caf806-1dd2-4ab8-8ff6-fab47e1224b6",
  "type": "user",
  "uuid": "53262c44-e17d-445c-9fb3-775400972a4b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping analyze a research paper for an ML research project.\n\nPaper: \"Conformal Language Modeling\" by Victor Quach, Adam Fisch, Tal Schuster, Adam Yala, Jae Ho Sohn, Tommi S. Jaakkola, Regina Barzilay, ICLR 2024, https://arxiv.org/abs/2306.10193\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page at https://arxiv.org/abs/2306.10193\n2. Use WebFetch to read the full paper PDF at https://arxiv.org/pdf/2306.10193\n3. Search for OpenReview reviews of this paper (ICLR 2024, search OpenReview for \"Conformal Language Modeling\")\n4. Search the web for any discussion/reviews\n\nProvide a detailed summary covering:\n- The exact problem/gap they identified (extending CP to free-text generation)\n- Their key insight about stopping/rejection rules for generative models\n- Technical method details (how they calibrate stopping rules, rejection rules, the admissibility function, how they handle the combinatorial output space)\n- The theoretical guarantees — what exactly do they prove?\n- Applications they demonstrate (QA, summarization, radiology)\n- Any reviewer praise/criticism if found\n- Limitations they acknowledge\n\nBe thorough and specific about the technical details. Report back everything you find.",
    "agentId": "a5c534cc96025704b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information from all sources. Here is my detailed summary:\n\n---\n\n## Detailed Analysis: \"Conformal Language Modeling\" (Quach, Fisch, Schuster, Yala, Sohn, Jaakkola, Barzilay -- ICLR 2024)\n\n### 1. The Problem/Gap Identified\n\nThe paper addresses a fundamental barrier in applying conformal prediction (CP) to generative language models. Standard CP works by constructing prediction sets from a finite, enumerable output space -- you score each possible output and include those above a threshold. For language models, the output space is combinatorially explosive (all possible text sequences), making exhaustive enumeration intractable. Prior CP methods were limited to classification tasks or settings with bounded output spaces. No existing framework could provide distribution-free statistical guarantees for free-text generation from LMs.\n\nThe authors frame this as: how do you construct a prediction set with coverage guarantees when you cannot even enumerate the candidate outputs?\n\n### 2. Key Insight: Sampling-Based Conformal Prediction via Stopping and Rejection Rules\n\nThe central insight is to replace exhaustive enumeration with a **calibrated sampling procedure**. Instead of scoring all possible outputs, they:\n\n1. **Sample** outputs from the LM sequentially\n2. Apply a **rejection rule** to filter out low-quality or redundant samples\n3. Apply a **stopping rule** to determine when enough diverse, high-quality samples have been collected to guarantee coverage\n\nThis transforms the intractable problem of conformal prediction over an infinite space into a tractable one: calibrating when to stop sampling and what to keep/reject.\n\n### 3. Technical Method Details\n\n**Formal Setting:**\n- Input: X in X (prompt)\n- Output space: Y (all possible text sequences -- unbounded)\n- Admissibility function: A: Y -> {0,1} -- binary ground truth for whether a generated text is \"acceptable\"\n- Language model: p_theta(y|x) -- can only sample from, not enumerate\n\n**Algorithm 1 (Conformal Sampling with Rejection):**\nThe procedure is parameterized by lambda = (lambda_1, lambda_2, lambda_3):\n\nFor each sample y_k drawn from p_theta(y|x):\n1. **Quality check**: reject if Q(x, y_k) < lambda_2 (where Q is a quality scoring function, e.g., LM log-likelihood)\n2. **Diversity check**: reject if max similarity to existing samples exceeds lambda_1 (similarity measured by ROUGE-L via function S)\n3. If both checks pass, add to candidate set C_lambda\n4. **Stop** when confidence function F(C_lambda) >= lambda_3 or budget k_max is exhausted\n\n**Confidence Functions Tested (four variants):**\n- **First-K**: F(C) = |C| -- just use set size as a proxy\n- **First-K + reject**: Same but with rejection enabled\n- **Max**: F(C) = max{Q(y) : y in C} -- best single item's quality score\n- **Sum**: F(C) = sum of Q(y) over y in C -- aggregate confidence\n\n**Calibration via Learn Then Test (LTT) Framework:**\n\nThe three-dimensional lambda is calibrated using the LTT framework of Angelopoulos et al. For each candidate lambda configuration:\n\n- Compute empirical risk on calibration data: R_hat_n(lambda) = (1/n) * sum_i 1{no y in C_lambda(X_i) has A_i(y)=1}\n- Compute p-values using binomial tails: p_lambda^BT = P(Binom(n, epsilon) <= n * R_hat_n(lambda))\n- This tests H_lambda: E[L_test(lambda)] > epsilon (null = the configuration is bad)\n- Apply FWER-controlling multiple testing (Bonferroni/Holm) at level delta across all lambda in the grid Lambda\n- Valid configurations Lambda_valid = those whose nulls are rejected\n\n**Selection among valid configurations (Equation 7):**\nlambda_hat = argmin over Lambda_valid of: (1/n) * sum_i [rho_1 * |C_lambda(X_i)| + rho_2 * (S_lambda(X_i) - S*(X_i))+ / S_lambda(X_i)]\n\nThis balances two competing objectives: (1) small prediction set size and (2) sampling efficiency (not drawing too many excess samples that get rejected). They use rho_1 = rho_2 = 0.5.\n\n**Pareto Testing** is used to efficiently search the 3D lambda space by exploiting monotonicity properties (e.g., higher lambda_3 means more stringent stopping, which generally increases set size and coverage).\n\n**Component-Level Analysis (Inner Conformal Procedure):**\nFor verbose outputs (radiology reports, summaries), they extend to component selection:\n\nC_gamma^inner(x) = {e in union of E(y) for y in C_lambda(x) : F^c(e) >= gamma}\n\nWhere E: Y -> 2^Y decomposes text into components (sentences), F^c scores component confidence, and A^c judges individual component correctness. The gamma threshold is calibrated separately.\n\n### 4. Theoretical Guarantees\n\n**Theorem 4.2 (Main Result -- Sampling-based coverage):**\nThe prediction set C_lambda_hat(X_test) satisfies:\n\nP(P(exists y in C_lambda_hat(X_test): A_test(y) = 1 | D_cal) >= 1 - epsilon) >= 1 - delta\n\n- Outer probability: over draws of calibration set D_cal\n- Inner probability: over test inputs\n- epsilon: error tolerance (target risk level)\n- delta: confidence parameter\n\nThis is **distribution-free** and **finite-sample valid**. It guarantees that with high probability over calibration data, the returned set contains at least one admissible answer with probability at least 1 - epsilon.\n\n**Theorem 4.4 (Component-level coverage):**\nP(P(A^c_test(e) = 1, for all e in C_gamma^inner(X_test) | D_cal) >= 1 - alpha) >= 1 - delta\n\nThis guarantees that every component in the filtered inner set is correct with high probability.\n\nBy union bound, both theorems hold simultaneously with probability >= 1 - 2*delta.\n\nThe proof relies on Lemma 4.1 establishing that the binomial tail p-values are valid for the risk-control hypothesis testing, which in turn inherits from the LTT framework.\n\n### 5. Applications Demonstrated\n\n**Radiology Report Generation (MIMIC-CXR):**\n- Model: ViT encoder + GPT2 decoder\n- Full admissibility: Clinical Efficacy metric -- 14 CheXbert-extracted labels must exactly match reference\n- Component admissibility: ROUGE-L >= 0.4 vs. reference findings (sentence-level)\n\n**News Summarization (CNN/DailyMail):**\n- Model: Fine-tuned T5-XL\n- Full admissibility: ROUGE-L >= 0.35 vs. human summaries\n- Component admissibility: ROUGE-L >= 0.4 per sentence\n\n**Open-Domain QA (TriviaQA):**\n- Model: LLaMA-13B (32-shot prompting, no fine-tuning)\n- Admissibility: Exact match after normalization\n- No component-level evaluation (answers are atomic)\n\n**Key Results:**\n- All methods achieve valid coverage (loss <= target epsilon), confirming theoretical guarantees hold empirically\n- Likelihood-based approaches (Max, Sum) produce set sizes less than 50% of First-K baseline for QA\n- Max outperforms Sum on excess samples metric across all tasks\n- Component-level selection with application-specific classifiers outperforms model logits alone\n- k_max = 20 was used as the sampling budget\n\n### 6. Reviewer Feedback (ICLR 2024 OpenReview)\n\nThe paper received four reviews with ratings: **8, 8, 3, 6** and was accepted as a **poster**.\n\n**Strengths praised by reviewers:**\n- First extension of conformal prediction to LM generation with rigorous guarantees (novel)\n- Practical framework giving acceptance/rejection/sampling rules with risk control guarantees\n- Generally well-written with clear technical detail\n- Comprehensive experiments across three diverse tasks\n- Component-level guarantees for identifying correct sub-parts\n\n**Weaknesses and criticisms:**\n- **Dense notation** in first 7.5 pages limits accessibility to broader audience\n- **ROUGE-L dependency**: Using lexical similarity as the admission function is problematic and may conflict with human judgment\n- **Circular logic concern**: ROUGE used both for duplicate detection and quality assessment\n- **Calibration data requirement**: Method assumes access to labeled calibration set with known admission functions\n- **Practicality questioned**: One reviewer (3/10) questioned \"what problem this is solving\" and whether it would outperform simpler baselines\n- **High achievable risk on MIMIC-CXR**: Questioning practical utility\n- **Scalability concern**: Benefits may diminish with larger, better-calibrated models\n- **Pareto Testing only described at high level**; Proposition 4.4 lacked experimental validation initially\n\n**Author responses addressed:**\n- Clarified that test set answers are NOT used in the stopping rule (only for calibration/evaluation)\n- Defended ROUGE consistency via transitive arguments\n- Added First-K with rejection for fairer baseline comparison\n- Added experimental validation for Proposition 4.4 (Figure G.1)\n- Enhanced Pareto Testing explanation\n\n**Area Chair** found the work \"well executed\" with \"broadly useful\" contributions.\n\n### 7. Limitations Acknowledged\n\nFrom the paper (Appendix B) and subsequent analysis:\n\n1. **Calibration data dependency**: Results depend heavily on calibration set quality and size; requires ground-truth admission labels\n2. **Exchangeability assumption**: Calibration data must be exchangeable with test data\n3. **Finite sampling budget**: With k_max = 20, achievable error tolerance ranges are limited; very low epsilon may be unachievable\n4. **Admission function design**: Requires reliable, potentially expensive or subjective admission functions for each task\n5. **Black-box LM assumption**: Method requires sampling capability but cannot guarantee coverage for poorly-calibrated models\n6. **Algorithm termination**: Not formally guaranteed for infinite k_max\n7. **Interpretability**: Follow-up work (Mohri & Hashimoto, \"Language Models with Conformal Factuality Guarantees,\" 2024) noted that the approach returns opaque sets of sequences that are \"difficult to interpret and act upon,\" and that the space of all sequences necessitates approximations that limit practical utility\n8. **Conditional validity**: The guarantees are marginal, not conditional -- trustworthiness may vary by topic/domain\n9. **Independent claims assumption**: Does not generalize to reasoning tasks where correctness of each step depends on preceding steps (addressed by follow-up \"Conformal Language Model Reasoning\" at ICLR 2025)\n\n### 8. Code and Reproducibility\n\nThe authors released code at `github.com/Varal7/conformal-language-modeling` (95% Jupyter notebooks, 5% Python). All datasets are publicly accessible, and hyperparameters are specified in the paper and appendices."
      }
    ],
    "totalDurationMs": 252015,
    "totalTokens": 30836,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 506,
      "cache_read_input_tokens": 27613,
      "output_tokens": 2716,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 506
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2716,
          "cache_read_input_tokens": 27613,
          "cache_creation_input_tokens": 506,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 506,
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
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "8af694dc-a40a-408d-8d68-e53a31f016c8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-30T06:32:13.759Z_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive analyses of all 5 papers. Let me synthesize these into the required JSON format, keeping each analysis under 2000 characters while being concise and analytical.

Let me compose the JSON array:

1. **C-RAG** - ICML 2024
2. **ReliabilityRAG** - NeurIPS 2025
3. **Cherian et al.** - NeurIPS 2024
4. **Conformal Risk Control** - ICLR 2024


5. **Conformal Language Modeling** - ICLR 2024

Now I'm structuring the final JSON output with all five papers and their detailed analyses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53262c44-e17d-445c-9fb3-775400972a4b",
  "isSidechain": false,
  "requestId": "req_011CbYHUc76NibEpLAXHCnNA",
  "type": "assistant",
  "uuid": "eb4fe871-f05b-47b5-8df8-f37879042cc2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQ8PEWBfy7bwdw4JbuWn2w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18287,
      "cache_read_input_tokens": 14947,
      "output_tokens": 2944,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2944,
          "cache_read_input_tokens": 14947,
          "cache_creation_input_tokens": 18287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18287
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

_source line 26 · 2026-05-30T06:33:28.350Z_

Now I have comprehensive data on all 5 papers. Let me synthesize the analyses into the required JSON format.

```json
[
  {
    "title": "C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models",
    "venue": "ICML 2024",
    "problem_identification": "No provable guarantees existed that RAG actually reduces generation risk vs. standalone LLMs. Prior conformal prediction methods were limited to classification or required monotonic loss functions, excluding text generation risks.",
    "key_insight": "Conformal risk control can be extended to RAG generation with non-monotonic bounded losses by introducing a constrained generation protocol (parameterized by retrieval count, generation set size, diversity threshold) that produces candidate sets amenable to set-based risk analysis.",
    "innovation_type": "new_formulation",
    "method_summary": "Defines a constrained generation protocol parameterized by λ=(N_rag, λ_g, λ_s) producing candidate generation sets. Derives conformal risk bounds via KL-divergence and binomial CDF inversions on calibration data. Proves RAG reduces conformal generation risk under conditions on retriever quality (V_rag-qualified) and transformer architecture ((d+,Φ_M)-transformer). Extends to distribution shift via Hellinger distance bounds: α̂(ρ) = R̂ + √(V̂/N_cal)·q_δ + 2ρ + 2ρ², the first such guarantee for general bounded (not just monotone) risk functions.",
    "limitations_and_open_questions": "Theoretical analysis restricted to single-layer transformers with token-level simplification. Distribution shift extension requires knowing/estimating Hellinger distance bound ρ; adversarial retrieval corruption (where ρ is unbounded or unknown) is explicitly unaddressed.",
    "building_blocks": ["Conformal risk bound formulation for generation sets", "Distribution shift extension via Hellinger distance for bounded losses", "V_rag retriever quality metric", "Constrained generation protocol producing candidate sets"],
    "relevance_to_seed": "Provides the theoretical foundation for conformal risk guarantees in RAG but assumes benign retrieval — our work must handle the case where corpus poisoning makes ρ adversarially large or unknown, necessitating retrieval-aware score functions rather than distribution-distance assumptions."
  },
  {
    "title": "ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search",
    "venue": "NeurIPS 2025",
    "problem_identification": "RobustRAG's keyword/token-level majority voting causes severe information loss (~20-point degradation on long-form generation) and ignores reliability signals (document ranking, domain authority) that web search engines already provide and adversaries cannot easily manipulate.",
    "key_insight": "Framing robust document selection as Maximum Independent Set computation on an NLI-derived contradiction graph naturally excludes adversarial documents (which contradict benign majorities) while preserving full document content for generation, and lexicographic tie-breaking incorporates ranking reliability without modifying the MIS objective.",
    "innovation_type": "new_technique",
    "method_summary": "Generates isolated per-document answers, constructs a contradiction graph via pairwise NLI (DeBERTa), and computes MIS with lexicographic tie-breaking favoring higher-ranked documents. For k≤20, uses brute-force enumeration; for larger k, uses weighted sampling (γ=0.9 exponential decay by rank) drawing m=2 docs per round over T=20 rounds, then applies MIS to intermediate answers. Proves contamination probability vanishes as e^{-Ω(k)} under k'≤k/5 corruption and bounded NLI error rates.",
    "limitations_and_open_questions": "Assumes adversarial documents produce NLI-detectable contradictions with benign majority — subtle misinformation may evade detection. Provides certified robustness but no conformal/abstention mechanism — cannot quantify residual risk or guarantee answer correctness when the MIS itself is contaminated.",
    "building_blocks": ["NLI-based contradiction graph construction", "MIS formulation for document selection", "Weighted sampling with rank-based decay for scalability", "Isolated per-document answer generation"],
    "relevance_to_seed": "Primary baseline and complementary technique — ReliabilityRAG certifies document selection but cannot abstain or quantify residual risk; our conformal abstention framework fills exactly this gap by providing coverage guarantees on top of (or independent of) document selection defenses."
  },
  {
    "title": "Large Language Model Validity via Enhanced Conformal Prediction Methods",
    "venue": "NeurIPS 2024",
    "problem_identification": "Marginal conformal factuality guarantees hide dangerous variation across topics — empirically, coverage drops from ~95% for high-popularity Wikipedia articles to ~70% for low-popularity ones, precisely where errors are most harmful. Additionally, achieving 90% marginal factuality requires filtering ~76% of claims, destroying utility.",
    "key_insight": "Replacing marginal conformal guarantees with function-class conditional guarantees, and allowing the confidence level α(X) to vary per-prompt via level-adaptive calibration, produces self-aware outputs that report calibrated per-prompt factuality probabilities while retaining substantially more claims.",
    "innovation_type": "new_formulation",
    "method_summary": "Extends Gibbs et al.'s conditional conformal framework to monotone losses via score S(C,W)=inf{τ|L(F(C;τ),W)≤λ}, achieving group-conditional risk control for user-specified function classes. Introduces level-adaptive conformal prediction where α(X) is learned via two-fold splitting to target claim retention rates, with Theorem 3.2 proving calibration: P(factual|α∈I, P∈G)=E[α|α∈I, P∈G]. Proposes conditional boosting — differentiable optimization of scoring functions through the quantile regression LP using Proposition 3.1's explicit derivative of the threshold w.r.t. score parameters.",
    "limitations_and_open_questions": "Requires exchangeability assumption that deployment may violate. Conditional boosting depends on LP basis stability (requires dithering). Does not address adversarial settings where score functions themselves may be manipulated.",
    "building_blocks": ["Group-conditional conformal coverage for LLMs", "Level-adaptive conformal prediction with per-input α(X)", "Differentiable score optimization through quantile regression LP", "Conditional boosting avoiding marginal-only optimization pitfalls"],
    "relevance_to_seed": "Directly relevant to group-conditional coverage under retrieval corruption — our retrieval-agreement groups can serve as the conditioning function class, and level-adaptive calibration enables varying abstention thresholds based on retrieval quality signals."
  },
  {
    "title": "Conformal Risk Control",
    "venue": "ICLR 2024",
    "problem_identification": "Standard conformal prediction only controls coverage (indicator loss), but real applications need control over richer losses — false negative rates in segmentation, missed labels in multilabel classification, F1-score in QA. No unified framework existed for distribution-free finite-sample control of arbitrary loss functions.",
    "key_insight": "The essential ingredient making conformal prediction work is not coverage-specific — it is the monotonicity of the loss in a tuning parameter λ; any non-increasing, right-continuous, bounded loss inherits the same exchangeability-based finite-sample guarantee via a 5-line algorithm.",
    "innovation_type": "new_formulation",
    "method_summary": "Finds λ̂=inf{λ: [n/(n+1)]R̂_n(λ)+B/(n+1)≤α}, which is an upper confidence bound treating the unobserved test loss as its maximum B. Proves E[L_{n+1}(λ̂)]≤α (exact finite-sample) with matching lower bound α−2B/(n+1) (tight to O(1/n)). Extends to covariate shift via importance weighting, arbitrary shift via TV distance bounds, quantile risk control, simultaneous control of multiple risks (no Bonferroni needed), adversarial worst-case risk, and U-statistic risks for multi-sample losses.",
    "limitations_and_open_questions": "Monotonicity is provably necessary (Proposition 2.1 shows non-monotone losses can push risk to maximum B). Distribution shift extension requires known importance weights. Factor-of-2 tightness overhead vs. standard CP. Reviewers noted lack of experiments for the distribution shift and adversarial extensions.",
    "building_blocks": ["Monotone loss risk control algorithm (5-line procedure)", "Distribution shift extension via importance weighting and TV bounds", "Multiple simultaneous risk control without Bonferroni correction", "Adversarial worst-case risk control formulation"],
    "relevance_to_seed": "Core theoretical building block — our abstention loss is monotone in the abstention threshold, enabling direct application of CRC; the distribution shift extension via TV distance provides a template for bounding coverage degradation under corpus poisoning, though we need retrieval-specific bounds rather than generic TV distance."
  },
  {
    "title": "Conformal Language Modeling",
    "venue": "ICLR 2024",
    "problem_identification": "Conformal prediction requires enumerating or scoring all possible outputs to construct prediction sets, which is intractable for generative language models with combinatorially explosive output spaces. No framework existed for distribution-free coverage guarantees over free-text LM outputs.",
    "key_insight": "Replace exhaustive enumeration with calibrated sampling — define conformal prediction sets through stopping rules (when to stop sampling) and rejection rules (what to keep), calibrated via Learn-then-Test to guarantee at least one admissible answer exists in the retained set with high probability.",
    "innovation_type": "cross_domain",
    "method_summary": "Parameterizes sampling by λ=(λ₁,λ₂,λ₃) controlling diversity threshold (ROUGE-L similarity), quality threshold (LM log-likelihood), and stopping confidence. Calibrates λ via LTT framework with binomial tail p-values and FWER-controlling multiple testing across a 3D grid, optimizing for set size and sampling efficiency. Extends to component-level guarantees by decomposing outputs into sentences and applying an inner conformal procedure with separate threshold γ. Proves P(∃y∈C: A(y)=1)≥1−ε with probability ≥1−δ over calibration draws.",
    "limitations_and_open_questions": "Guarantees are marginal, not conditional (coverage varies by topic — addressed by Cherian et al.). Requires reliable admission functions and labeled calibration data. Sampling budget k_max=20 limits achievable ε. Follow-up work (Mohri & Hashimoto) criticized returned sets as opaque and hard to interpret for end users.",
    "building_blocks": ["Sampling-based conformal prediction for intractable output spaces", "Stopping and rejection rules as conformal parameters", "Component-level conformal guarantees via inner procedure", "LTT-based multi-parameter calibration with Pareto testing"],
    "relevance_to_seed": "Methodological ancestor — our abstention mechanism can be viewed as a rejection rule calibrated over RAG outputs, but we must handle the non-exchangeability introduced by adversarial retrieval rather than assuming i.i.d. sampling; the component-level guarantee concept maps to our per-claim factuality certificates."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb4fe871-f05b-47b5-8df8-f37879042cc2",
  "isSidechain": false,
  "requestId": "req_011CbYHUc76NibEpLAXHCnNA",
  "type": "assistant",
  "uuid": "d921092d-e912-4c3c-abe4-d1953f705065",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MQ8PEWBfy7bwdw4JbuWn2w",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18287,
      "cache_read_input_tokens": 14947,
      "output_tokens": 2944,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2944,
          "cache_read_input_tokens": 14947,
          "cache_creation_input_tokens": 18287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18287
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
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "d921092d-e912-4c3c-abe4-d1953f705065",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze poisoning-robust conformal prediction for RAG systems",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "d921092d-e912-4c3c-abe4-d1953f705065",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze poisoning-robust conformal prediction for RAG systems",
  "sessionId": "458a2eed-0834-465b-87af-c8668736149f"
}
```

---
