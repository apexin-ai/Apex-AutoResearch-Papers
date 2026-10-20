# Research conversation: You are a senior ML researcher performing deep analysis of multiple published papers. **Today's date: 2026-05-30 (UTC).*

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/4b88536a-9d82-410d-a6db-a241b9b697ad.jsonl`
- **Structured JSON:** [`5e435eba8da40cda75b2.json`](../../sessions/5e/5e435eba8da40cda75b2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:27:22.999Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:27:22.999Z",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "content": "You are a senior ML researcher performing deep analysis of multiple published papers.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: Safe, Robust and Responsible AI (SRRAI)\n\nDirection: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.\n\nSeed Papers:\n- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval\n- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG\n- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative\n- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on\n- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition\n\nKnown Gaps:\n- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)\n- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails\n- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis\n\nTheoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must compare against RobustRAG and ReliabilityRAG baselines\n- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols\n- AAAI 2026 submission deadline: August 2026\n\nQuality Self-Checks:\n- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.\n- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.\n- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.\n- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.\n\nAvoid:\n- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this\n- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead\n- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates**\n\n## Your task (Batch 3)\n\nAnalyze the following 5 papers. For EACH paper:\n1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.\n2. If on OpenReview, also read reviewer comments.\n3. Write a concise analysis focusing on HOW the paper innovates.\n\n## Papers to analyze\n\n[\n  {\n    \"title\": \"Language Models with Conformal Factuality Guarantees\",\n    \"authors\": \"Christopher Mohri, Tatsunori Hashimoto\",\n    \"venue\": \"ICML 2024\",\n    \"url\": \"https://arxiv.org/abs/2402.10978\",\n    \"why_important\": \"Highly cited — introduced 'conformal factuality,' the key paradigm connecting conformal prediction to LLM correctness guarantees that downstream RAG work builds upon\",\n    \"one_line_summary\": \"Frames LLM factual correctness as an uncertainty quantification problem using conformal prediction over entailment sets, implementing a back-off algorithm that progressively makes outputs less specific to achieve 80-90% correctness guarantees.\"\n  },\n  {\n    \"title\": \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\",\n    \"authors\": \"Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak\",\n    \"venue\": \"arXiv 2026\",\n    \"url\": \"https://arxiv.org/abs/2603.16817\",\n    \"why_important\": \"Directly motivates the proposed work — demonstrates that conformal factuality guarantees for RAG break under distribution shifts and distractors, but proposes no solution\",\n    \"one_line_summary\": \"Shows that conformal factuality filtering for RAG produces vacuous outputs at high factuality levels, lacks robustness to distribution shifts, and that lightweight entailment verifiers match LLM-based scorers at 100x fewer FLOPs.\"\n  },\n  {\n    \"title\": \"Conformal Prediction as Bayesian Quadrature\",\n    \"authors\": \"Jake C. Snell, Thomas L. Griffiths\",\n    \"venue\": \"ICML 2025 (Outstanding Paper Award, Oral)\",\n    \"url\": \"https://arxiv.org/abs/2502.13228\",\n    \"why_important\": \"Outstanding Paper Award — state-of-the-art CP theory; reframes CP as Bayesian quadrature, unifying Split CP and Conformal Risk Control and yielding significantly lower failure rates\",\n    \"one_line_summary\": \"Reformulates conformal prediction as prior-agnostic Bayesian quadrature that computes the full posterior over a provable upper bound on expected loss, unifying Split CP and Conformal Risk Control as special cases.\"\n  },\n  {\n    \"title\": \"Conformal Prediction for Natural Language Processing: A Survey\",\n    \"authors\": \"Margarida M. Campos, Antonio Farinhas, Chrysoula Zerva, Mario A.T. Figueiredo, Andre F.T. Martins\",\n    \"venue\": \"TACL 2024\",\n    \"url\": \"https://arxiv.org/abs/2405.01976\",\n    \"why_important\": \"Comprehensive survey — covers CP guarantees, extensions, and applications across all NLP tasks; essential reference for positioning the proposed work\",\n    \"one_line_summary\": \"Surveys conformal prediction techniques for NLP including classification, structured prediction, and generation, covering theoretical guarantees, practical extensions, and open challenges for LLMs.\"\n  },\n  {\n    \"title\": \"Conformal Selective Prediction with General Risk Control (SCoRE)\",\n    \"authors\": \"Tian Bai, Ying Jin\",\n    \"venue\": \"arXiv 2026\",\n    \"url\": \"https://arxiv.org/abs/2603.24704\",\n    \"why_important\": \"Directly relevant method — constructs e-values for selective conformal prediction enabling binary trust/abstain decisions with finite-sample error guarantees under distribution shift\",\n    \"one_line_summary\": \"Uses e-values from conformal inference for selective prediction with finite-sample error guarantees that hold under distribution shift, applicable to drug discovery, health risk, and LLM evaluation.\"\n  }\n]\n\n## Analysis requirements\n\nFor each paper, analyze:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- If reviewer comments are available: what was praised, what was criticized?\n\n## CRITICAL: Length constraint\n\n**Each paper's analysis MUST be under 2000 characters.** Be concise and analytical — no filler, no generic praise, no redundant descriptions. Every sentence must carry information.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem? How found? (1-2 sentences)\",\n  \"key_insight\": \"Core intellectual contribution (1 sentence)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach (2-3 sentences)\",\n  \"limitations_and_open_questions\": \"Gaps + follow-up questions (1-2 sentences)\",\n  \"building_blocks\": [\"Reusable methods/tools/datasets\"],\n  \"relevance_to_seed\": \"Relation to our research area (1 sentence)\"\n}\n\nYou MUST output exactly 5 analyses in the JSON array. IMPORTANT: End your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:27:23.016Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:27:23.016Z",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-30T06:27:23.247Z_

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

## Your task (Batch 3)

Analyze the following 5 papers. For EACH paper:
1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.
2. If on OpenReview, also read reviewer comments.
3. Write a concise analysis focusing on HOW the paper innovates.

## Papers to analyze

[
  {
    "title": "Language Models with Conformal Factuality Guarantees",
    "authors": "Christopher Mohri, Tatsunori Hashimoto",
    "venue": "ICML 2024",
    "url": "https://arxiv.org/abs/2402.10978",
    "why_important": "Highly cited — introduced 'conformal factuality,' the key paradigm connecting conformal prediction to LLM correctness guarantees that downstream RAG work builds upon",
    "one_line_summary": "Frames LLM factual correctness as an uncertainty quantification problem using conformal prediction over entailment sets, implementing a back-off algorithm that progressively makes outputs less specific to achieve 80-90% correctness guarantees."
  },
  {
    "title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
    "authors": "Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2603.16817",
    "why_important": "Directly motivates the proposed work — demonstrates that conformal factuality guarantees for RAG break under distribution shifts and distractors, but proposes no solution",
    "one_line_summary": "Shows that conformal factuality filtering for RAG produces vacuous outputs at high factuality levels, lacks robustness to distribution shifts, and that lightweight entailment verifiers match LLM-based scorers at 100x fewer FLOPs."
  },
  {
    "title": "Conformal Prediction as Bayesian Quadrature",
    "authors": "Jake C. Snell, Thomas L. Griffiths",
    "venue": "ICML 2025 (Outstanding Paper Award, Oral)",
    "url": "https://arxiv.org/abs/2502.13228",
    "why_important": "Outstanding Paper Award — state-of-the-art CP theory; reframes CP as Bayesian quadrature, unifying Split CP and Conformal Risk Control and yielding significantly lower failure rates",
    "one_line_summary": "Reformulates conformal prediction as prior-agnostic Bayesian quadrature that computes the full posterior over a provable upper bound on expected loss, unifying Split CP and Conformal Risk Control as special cases."
  },
  {
    "title": "Conformal Prediction for Natural Language Processing: A Survey",
    "authors": "Margarida M. Campos, Antonio Farinhas, Chrysoula Zerva, Mario A.T. Figueiredo, Andre F.T. Martins",
    "venue": "TACL 2024",
    "url": "https://arxiv.org/abs/2405.01976",
    "why_important": "Comprehensive survey — covers CP guarantees, extensions, and applications across all NLP tasks; essential reference for positioning the proposed work",
    "one_line_summary": "Surveys conformal prediction techniques for NLP including classification, structured prediction, and generation, covering theoretical guarantees, practical extensions, and open challenges for LLMs."
  },
  {
    "title": "Conformal Selective Prediction with General Risk Control (SCoRE)",
    "authors": "Tian Bai, Ying Jin",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2603.24704",
    "why_important": "Directly relevant method — constructs e-values for selective conformal prediction enabling binary trust/abstain decisions with finite-sample error guarantees under distribution shift",
    "one_line_summary": "Uses e-values from conformal inference for selective prediction with finite-sample error guarantees that hold under distribution shift, applicable to drug discovery, health risk, and LLM evaluation."
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
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "type": "user",
  "uuid": "d4cc891f-4ecf-4e2c-a2a0-88dc418d6927",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:27:23.245Z_

```json
{
  "parentUuid": "d4cc891f-4ecf-4e2c-a2a0-88dc418d6927",
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
  "uuid": "998f2657-b0d6-4bd7-99a3-2a49a8faf91f",
  "timestamp": "2026-05-30T06:27:23.245Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:27:23.246Z_

```json
{
  "parentUuid": "998f2657-b0d6-4bd7-99a3-2a49a8faf91f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "41d3a1d8-ab44-44c0-ad67-bdcb3bc4f9c6",
  "timestamp": "2026-05-30T06:27:23.246Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
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
  "aiTitle": "Analyze conformal prediction papers for poisoning-robust RAG",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---

### Assistant

_source line 7 · 2026-05-30T06:27:25.247Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze each of the 5 papers systematically. I'll search for and read each paper's content, then compile the analyses.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41d3a1d8-ab44-44c0-ad67-bdcb3bc4f9c6",
  "isSidechain": false,
  "requestId": "req_011CbYH7x6nerZoFRDFEX3d4",
  "type": "assistant",
  "uuid": "dc494339-5f80-40fd-b44d-03fc8c5d94f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VEEMqs8HMKvfnZXrTYaht",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3930,
      "cache_read_input_tokens": 11014,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3930
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

_source line 8 · 2026-05-30T06:27:26.258Z_

I'll research all 5 papers in parallel to gather their abstracts, methods, and any reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc494339-5f80-40fd-b44d-03fc8c5d94f6",
  "isSidechain": false,
  "requestId": "req_011CbYH7x6nerZoFRDFEX3d4",
  "type": "assistant",
  "uuid": "8b400352-0612-4367-8b6b-858dd616aeff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VEEMqs8HMKvfnZXrTYaht",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3930,
      "cache_read_input_tokens": 11014,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3930
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

_source line 9 · 2026-05-30T06:27:31.521Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MDqyrhYQCsHWQk87fqxpMf`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Paper 1: Conformal Factuality",
  "prompt": "Research the paper \"Language Models with Conformal Factuality Guarantees\" by Christopher Mohri and Tatsunori Hashimoto (ICML 2024, https://arxiv.org/abs/2402.10978).\n\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebSearch to find OpenReview reviews or any detailed discussion of this paper\n3. Use WebFetch to read the full paper PDF if possible, or at least the abstract and introduction\n\nI need to understand:\n- What gap did they identify?\n- What was their key insight?\n- How did they formulate the problem?\n- What techniques did they adapt/combine?\n- Any reviewer feedback\n\nReport back all findings in detail. Include direct quotes where helpful."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b400352-0612-4367-8b6b-858dd616aeff",
  "isSidechain": false,
  "requestId": "req_011CbYH7x6nerZoFRDFEX3d4",
  "type": "assistant",
  "uuid": "fcbf6498-e37b-4cef-b55c-837ed5d47c59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VEEMqs8HMKvfnZXrTYaht",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3930,
      "cache_read_input_tokens": 11014,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3930,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 340,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3930
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

_source line 10 · 2026-05-30T06:31:09.604Z_

<details><summary>↩ Tool result · `toolu_01MDqyrhYQCsHWQk87fqxpMf`</summary>

```text
Now I have comprehensive information. Here is the full research report.

---

## Research Report: "Language Models with Conformal Factuality Guarantees"

**Authors:** Christopher Mohri, Tatsunori Hashimoto  
**Venue:** ICML 2024 (Proceedings of Machine Learning Research, Volume 235, pp. 36029-36047)  
**ArXiv:** [2402.10978](https://arxiv.org/abs/2402.10978)  
**Code:** [github.com/tatsu-lab/conformal-factual-lm](https://github.com/tatsu-lab/conformal-factual-lm)

---

### 1. The Gap They Identified

The paper identifies a fundamental disconnect between two problems: (a) LLM hallucination/factuality failures that make deployment risky in high-stakes domains (healthcare, law, robotics), and (b) the rich statistical toolkit of conformal prediction, which had not been meaningfully applied to open-ended language generation.

Prior approaches to conformal prediction in LMs were limited to:
- **Token-level methods** that return sets of tokens (not interpretable natural language)
- **Multiple-choice reductions** constrained to QA with fixed answer sets
- **Sequence-space approximations** that produce sets of complete sequences which are "difficult to interpret and act upon"

None of these produced a single, interpretable natural-language output with formal correctness guarantees. Meanwhile, factuality methods (retrieval augmentation, training modifications, decoding adjustments) lacked any formal probabilistic guarantees.

---

### 2. The Key Insight

The central insight is an elegant correspondence: **the correctness of an LM output is equivalent to an uncertainty quantification problem, where uncertainty sets are defined through entailment.**

Specifically, each possible LM output y defines an **entailment set** E(y) := {y' in Y : y' => y} -- the set of all ground-truth statements that would entail y. If the true answer y* is in E(y), then y is necessarily correct. This means:

- Checking factuality = checking whether y* falls in the entailment set E(y)
- Conformal prediction's goal of ensuring P(Y* in C(X)) >= 1-alpha maps directly to ensuring P(Y* in E(output)) >= 1-alpha

The second key insight is that conformal prediction in this setting **corresponds to a back-off algorithm**: you progressively make the LM output less specific (removing claims), which expands the entailment set, until you reach a level of specificity where coverage is guaranteed with high probability.

---

### 3. Problem Formulation

**Formal objective:** For user-specified alpha in (0,1), ensure:

P(Y_{n+1}* in E(L-bar(X_{n+1}))) >= 1 - alpha

where L-bar is the conformally-adjusted model.

**Definition (alpha-Conformal Factuality):** A model L-bar is alpha-conformally factual if for exchangeable (X_i, Y_i*), the above probability bound holds.

The framework uses **split conformal prediction** with:
- A **back-off function** F_t(x, L(x)) that removes sub-claims from the LM output as threshold t increases, eventually outputting nothing (the "soundness" requirement)
- A **score function** r(x, y*) := inf{t in T : for all j >= t, y* in E(F_j(x))} -- the minimum threshold at which the ground truth is entailed by all subsequent outputs
- A **calibration quantile** q-hat_alpha computed as the ceil((n+1)(1-alpha))/n-th quantile of calibration scores

The final output is: L-bar(x) := F_{q-hat_alpha}(x, L(x))

---

### 4. Techniques Adapted and Combined

The paper combines several techniques:

**From Conformal Prediction:**
- Split conformal prediction (Vovk et al., Papadopoulos et al.) -- the core statistical machinery providing distribution-free coverage guarantees under exchangeability
- Nested confidence sets -- the back-off function creates a nested family of sets indexed by threshold t

**From NLP/LLM Infrastructure:**
- **Sub-claim decomposition** (S): Breaking LM outputs into atomic factual claims (implemented via GPT-4 prompting)
- **Claim scoring** (s): Multiple scoring functions tested -- confidence scoring (querying the model), frequency scoring (sampling 5 alternate outputs and counting claim occurrences), random, ordinal, and oracle scoring
- **Claim merging** (M): Reassembling filtered claims into coherent text

**Critical bridging assumption (Assumption 5.1):** The merger function must preserve entailment decomposability:

E(M({c_i})) = intersection of E(c_i) for all i

This means the merged output is entailed if and only if each individual sub-claim is entailed. Under this assumption, the score computation simplifies dramatically (Proposition 5.2) -- you only need to check entailment on individual sub-claims rather than all possible combinations.

**From the hierarchical classification literature:** The closest prior work is Angelopoulos et al. (2023) on hierarchical label classification, though the authors differentiate their approach in set construction, hierarchy representation, and application setting.

---

### 5. Main Theoretical Result (Theorem 4.1)

Under exchangeability and soundness of F_t:

**Lower bound:** P(Y_{n+1}* in E(F_{q-hat_alpha}(X_{n+1}))) >= 1 - alpha

**Upper bound (with nesting):** The same probability is at most 1 - alpha + 1/(n+1)

The proof leverages the exchangeability of scores: since all (n+1) scores are exchangeable, the probability that the test score falls below the ceil((1-alpha)(n+1))-th order statistic is exactly ceil((1-alpha)(n+1))/(n+1) >= 1-alpha.

**Extension -- Partial Factuality (Corollary 5.3):** The framework also supports guaranteeing that at least a fraction "a" of accepted sub-claims are factual, rather than requiring all to be correct.

---

### 6. Experimental Results

**Setup:** GPT-4 for all components; 50 inputs per dataset with manual 4-way annotation (Factual/Subjective/Unverifiable/False).

**Datasets and performance:**

| Dataset | Baseline Factuality | After Conformal Factuality | Claims Retained |
|---------|---------------------|---------------------------|-----------------|
| FActScore (biography generation) | ~25% | ~80% | ~50% |
| Natural Questions (long-form QA) | ~78% | ~93% | ~75% |
| MATH (reasoning) | ~75% | ~95% | ~90% |

Frequency scoring consistently performed best. Validation over 1000 random dataset splits confirmed marginal coverage with standard deviation ~0.09.

---

### 7. Reviewer Feedback and Community Reception

The OpenReview reviews for ICML 2024 were not publicly accessible in their full form. However, substantial critique has emerged through follow-up work:

**Critique 1 -- Marginal vs. Conditional Coverage:**  
The guarantees hold only marginally (averaged over random test prompts), not conditionally per-input. Follow-up work by the enhanced conformal prediction paper (NeurIPS 2024, [arxiv 2406.09714](https://arxiv.org/html/2406.09714v1)) demonstrated empirically that "the probability of output correctness (even after applying the conformal factuality method) is substantially lower for responses whose subjects are likely to be underrepresented in the model's training corpus." Global thresholding "fails to achieve conditional coverage, resulting in over-coverage for complex categories and under-coverage for easier ones."

**Critique 2 -- Excessive Claim Removal:**  
The same follow-up work observed: "Because the scoring function is imperfect, the filtering step can remove many valuable and accurate claims." Achieving 90% factuality guarantees required "near-complete censorship" of responses in some settings.

**Critique 3 -- Context-Independence of Claims:**  
A 2025 paper on "Conformal Language Model Reasoning with Coherent Factuality" ([arxiv 2505.17126](https://arxiv.org/abs/2505.17126)) noted that evaluating claims in isolation "is not appropriate for reasoning tasks, as steps of a logical argument can be evaluated for correctness only within the context of the claims that precede them." They propose "coherent factuality" with a "deducibility graph" to track logical dependencies.

**Positive reception from quick reviews** (e.g., [Liner review](https://liner.com/review/language-models-with-conformal-factuality-guarantees)) praised:
- Theoretical rigor: Algorithm 1 empirically validates Theorem 4.1's guarantees with tight correspondence
- Substantial performance gains across all three benchmarks
- Practical utility preservation: "Frequency scoring on FActScore increases factuality to 80% while keeping about half of the original sub-claims"

**Follow-up work addressing limitations:**
- **Level-Adaptive Conformal Prediction** (NeurIPS 2024): Adapts the confidence level per-prompt rather than using a global threshold; achieves 39% vs. 24% claim retention while maintaining calibrated guarantees
- **Conditional Factuality Control (CFC)** ([arxiv 2603.27403](https://arxiv.org/abs/2603.27403)): Provides conditional coverage guarantees with set-valued outputs
- **Adaptive Conformal Prediction** ([arxiv 2604.13991](https://arxiv.org/html/2604.13991)): Addresses the uniform quantile problem across prompts of varying difficulty
- **CoFact** (ICLR 2026): Extends conformal factuality under covariate shift

The paper's own acknowledged limitations include: non-conditional coverage, sensitivity to distribution shift, marginal guarantees over calibration set draws, and potential coverage deviations with small calibration sets.

---

### Summary Assessment

This paper made a foundational contribution by establishing the first clean theoretical bridge between conformal prediction and open-ended LM generation through the entailment-set correspondence. The formulation is elegant and the experimental validation is solid, albeit on small datasets (50 examples each). The work spawned a productive line of follow-up research, with at least 4-5 papers directly extending it to address the marginal-vs-conditional coverage gap, the claim retention problem, and the context-independence limitation. The core idea -- that making outputs less specific expands entailment sets and thus corresponds to conformal back-off -- is the lasting contribution.

---

Sources:
- [ArXiv Abstract Page](https://arxiv.org/abs/2402.10978)
- [ArXiv HTML Full Text](https://arxiv.org/html/2402.10978)
- [ICML Proceedings](https://proceedings.mlr.press/v235/mohri24a.html)
- [OpenReview Forum](https://openreview.net/forum?id=uYISs2tpwP)
- [ICML Virtual Poster](https://icml.cc/virtual/2024/poster/32822)
- [GitHub Repository](https://github.com/tatsu-lab/conformal-factual-lm)
- [Liner Quick Review](https://liner.com/review/language-models-with-conformal-factuality-guarantees)
- [Enhanced Conformal Prediction (NeurIPS 2024)](https://arxiv.org/html/2406.09714v1)
- [Coherent Factuality (2025)](https://arxiv.org/abs/2505.17126)
- [Conditional Factuality Control](https://arxiv.org/abs/2603.27403)
- [Adaptive Conformal Prediction](https://arxiv.org/html/2604.13991)
- [Semantic Scholar](https://www.semanticscholar.org/paper/Language-Models-with-Conformal-Factuality-Mohri-Hashimoto/2495700b4303512784fbdbfccc58c6c4f7771ac2)

agentId: aa326b1377f68b4ba (use SendMessage with to: 'aa326b1377f68b4ba' to continue this agent)
&lt;usage>total_tokens: 26814
tool_uses: 19
duration_ms: 218076&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fcbf6498-e37b-4cef-b55c-837ed5d47c59",
  "isSidechain": false,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "type": "user",
  "uuid": "096fd340-561d-4352-8e9a-828c0c94a80a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Language Models with Conformal Factuality Guarantees\" by Christopher Mohri and Tatsunori Hashimoto (ICML 2024, https://arxiv.org/abs/2402.10978).\n\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebSearch to find OpenReview reviews or any detailed discussion of this paper\n3. Use WebFetch to read the full paper PDF if possible, or at least the abstract and introduction\n\nI need to understand:\n- What gap did they identify?\n- What was their key insight?\n- How did they formulate the problem?\n- What techniques did they adapt/combine?\n- Any reviewer feedback\n\nReport back all findings in detail. Include direct quotes where helpful.",
    "agentId": "aa326b1377f68b4ba",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Here is the full research report.\n\n---\n\n## Research Report: \"Language Models with Conformal Factuality Guarantees\"\n\n**Authors:** Christopher Mohri, Tatsunori Hashimoto  \n**Venue:** ICML 2024 (Proceedings of Machine Learning Research, Volume 235, pp. 36029-36047)  \n**ArXiv:** [2402.10978](https://arxiv.org/abs/2402.10978)  \n**Code:** [github.com/tatsu-lab/conformal-factual-lm](https://github.com/tatsu-lab/conformal-factual-lm)\n\n---\n\n### 1. The Gap They Identified\n\nThe paper identifies a fundamental disconnect between two problems: (a) LLM hallucination/factuality failures that make deployment risky in high-stakes domains (healthcare, law, robotics), and (b) the rich statistical toolkit of conformal prediction, which had not been meaningfully applied to open-ended language generation.\n\nPrior approaches to conformal prediction in LMs were limited to:\n- **Token-level methods** that return sets of tokens (not interpretable natural language)\n- **Multiple-choice reductions** constrained to QA with fixed answer sets\n- **Sequence-space approximations** that produce sets of complete sequences which are \"difficult to interpret and act upon\"\n\nNone of these produced a single, interpretable natural-language output with formal correctness guarantees. Meanwhile, factuality methods (retrieval augmentation, training modifications, decoding adjustments) lacked any formal probabilistic guarantees.\n\n---\n\n### 2. The Key Insight\n\nThe central insight is an elegant correspondence: **the correctness of an LM output is equivalent to an uncertainty quantification problem, where uncertainty sets are defined through entailment.**\n\nSpecifically, each possible LM output y defines an **entailment set** E(y) := {y' in Y : y' => y} -- the set of all ground-truth statements that would entail y. If the true answer y* is in E(y), then y is necessarily correct. This means:\n\n- Checking factuality = checking whether y* falls in the entailment set E(y)\n- Conformal prediction's goal of ensuring P(Y* in C(X)) >= 1-alpha maps directly to ensuring P(Y* in E(output)) >= 1-alpha\n\nThe second key insight is that conformal prediction in this setting **corresponds to a back-off algorithm**: you progressively make the LM output less specific (removing claims), which expands the entailment set, until you reach a level of specificity where coverage is guaranteed with high probability.\n\n---\n\n### 3. Problem Formulation\n\n**Formal objective:** For user-specified alpha in (0,1), ensure:\n\nP(Y_{n+1}* in E(L-bar(X_{n+1}))) >= 1 - alpha\n\nwhere L-bar is the conformally-adjusted model.\n\n**Definition (alpha-Conformal Factuality):** A model L-bar is alpha-conformally factual if for exchangeable (X_i, Y_i*), the above probability bound holds.\n\nThe framework uses **split conformal prediction** with:\n- A **back-off function** F_t(x, L(x)) that removes sub-claims from the LM output as threshold t increases, eventually outputting nothing (the \"soundness\" requirement)\n- A **score function** r(x, y*) := inf{t in T : for all j >= t, y* in E(F_j(x))} -- the minimum threshold at which the ground truth is entailed by all subsequent outputs\n- A **calibration quantile** q-hat_alpha computed as the ceil((n+1)(1-alpha))/n-th quantile of calibration scores\n\nThe final output is: L-bar(x) := F_{q-hat_alpha}(x, L(x))\n\n---\n\n### 4. Techniques Adapted and Combined\n\nThe paper combines several techniques:\n\n**From Conformal Prediction:**\n- Split conformal prediction (Vovk et al., Papadopoulos et al.) -- the core statistical machinery providing distribution-free coverage guarantees under exchangeability\n- Nested confidence sets -- the back-off function creates a nested family of sets indexed by threshold t\n\n**From NLP/LLM Infrastructure:**\n- **Sub-claim decomposition** (S): Breaking LM outputs into atomic factual claims (implemented via GPT-4 prompting)\n- **Claim scoring** (s): Multiple scoring functions tested -- confidence scoring (querying the model), frequency scoring (sampling 5 alternate outputs and counting claim occurrences), random, ordinal, and oracle scoring\n- **Claim merging** (M): Reassembling filtered claims into coherent text\n\n**Critical bridging assumption (Assumption 5.1):** The merger function must preserve entailment decomposability:\n\nE(M({c_i})) = intersection of E(c_i) for all i\n\nThis means the merged output is entailed if and only if each individual sub-claim is entailed. Under this assumption, the score computation simplifies dramatically (Proposition 5.2) -- you only need to check entailment on individual sub-claims rather than all possible combinations.\n\n**From the hierarchical classification literature:** The closest prior work is Angelopoulos et al. (2023) on hierarchical label classification, though the authors differentiate their approach in set construction, hierarchy representation, and application setting.\n\n---\n\n### 5. Main Theoretical Result (Theorem 4.1)\n\nUnder exchangeability and soundness of F_t:\n\n**Lower bound:** P(Y_{n+1}* in E(F_{q-hat_alpha}(X_{n+1}))) >= 1 - alpha\n\n**Upper bound (with nesting):** The same probability is at most 1 - alpha + 1/(n+1)\n\nThe proof leverages the exchangeability of scores: since all (n+1) scores are exchangeable, the probability that the test score falls below the ceil((1-alpha)(n+1))-th order statistic is exactly ceil((1-alpha)(n+1))/(n+1) >= 1-alpha.\n\n**Extension -- Partial Factuality (Corollary 5.3):** The framework also supports guaranteeing that at least a fraction \"a\" of accepted sub-claims are factual, rather than requiring all to be correct.\n\n---\n\n### 6. Experimental Results\n\n**Setup:** GPT-4 for all components; 50 inputs per dataset with manual 4-way annotation (Factual/Subjective/Unverifiable/False).\n\n**Datasets and performance:**\n\n| Dataset | Baseline Factuality | After Conformal Factuality | Claims Retained |\n|---------|---------------------|---------------------------|-----------------|\n| FActScore (biography generation) | ~25% | ~80% | ~50% |\n| Natural Questions (long-form QA) | ~78% | ~93% | ~75% |\n| MATH (reasoning) | ~75% | ~95% | ~90% |\n\nFrequency scoring consistently performed best. Validation over 1000 random dataset splits confirmed marginal coverage with standard deviation ~0.09.\n\n---\n\n### 7. Reviewer Feedback and Community Reception\n\nThe OpenReview reviews for ICML 2024 were not publicly accessible in their full form. However, substantial critique has emerged through follow-up work:\n\n**Critique 1 -- Marginal vs. Conditional Coverage:**  \nThe guarantees hold only marginally (averaged over random test prompts), not conditionally per-input. Follow-up work by the enhanced conformal prediction paper (NeurIPS 2024, [arxiv 2406.09714](https://arxiv.org/html/2406.09714v1)) demonstrated empirically that \"the probability of output correctness (even after applying the conformal factuality method) is substantially lower for responses whose subjects are likely to be underrepresented in the model's training corpus.\" Global thresholding \"fails to achieve conditional coverage, resulting in over-coverage for complex categories and under-coverage for easier ones.\"\n\n**Critique 2 -- Excessive Claim Removal:**  \nThe same follow-up work observed: \"Because the scoring function is imperfect, the filtering step can remove many valuable and accurate claims.\" Achieving 90% factuality guarantees required \"near-complete censorship\" of responses in some settings.\n\n**Critique 3 -- Context-Independence of Claims:**  \nA 2025 paper on \"Conformal Language Model Reasoning with Coherent Factuality\" ([arxiv 2505.17126](https://arxiv.org/abs/2505.17126)) noted that evaluating claims in isolation \"is not appropriate for reasoning tasks, as steps of a logical argument can be evaluated for correctness only within the context of the claims that precede them.\" They propose \"coherent factuality\" with a \"deducibility graph\" to track logical dependencies.\n\n**Positive reception from quick reviews** (e.g., [Liner review](https://liner.com/review/language-models-with-conformal-factuality-guarantees)) praised:\n- Theoretical rigor: Algorithm 1 empirically validates Theorem 4.1's guarantees with tight correspondence\n- Substantial performance gains across all three benchmarks\n- Practical utility preservation: \"Frequency scoring on FActScore increases factuality to 80% while keeping about half of the original sub-claims\"\n\n**Follow-up work addressing limitations:**\n- **Level-Adaptive Conformal Prediction** (NeurIPS 2024): Adapts the confidence level per-prompt rather than using a global threshold; achieves 39% vs. 24% claim retention while maintaining calibrated guarantees\n- **Conditional Factuality Control (CFC)** ([arxiv 2603.27403](https://arxiv.org/abs/2603.27403)): Provides conditional coverage guarantees with set-valued outputs\n- **Adaptive Conformal Prediction** ([arxiv 2604.13991](https://arxiv.org/html/2604.13991)): Addresses the uniform quantile problem across prompts of varying difficulty\n- **CoFact** (ICLR 2026): Extends conformal factuality under covariate shift\n\nThe paper's own acknowledged limitations include: non-conditional coverage, sensitivity to distribution shift, marginal guarantees over calibration set draws, and potential coverage deviations with small calibration sets.\n\n---\n\n### Summary Assessment\n\nThis paper made a foundational contribution by establishing the first clean theoretical bridge between conformal prediction and open-ended LM generation through the entailment-set correspondence. The formulation is elegant and the experimental validation is solid, albeit on small datasets (50 examples each). The work spawned a productive line of follow-up research, with at least 4-5 papers directly extending it to address the marginal-vs-conditional coverage gap, the claim retention problem, and the context-independence limitation. The core idea -- that making outputs less specific expands entailment sets and thus corresponds to conformal back-off -- is the lasting contribution.\n\n---\n\nSources:\n- [ArXiv Abstract Page](https://arxiv.org/abs/2402.10978)\n- [ArXiv HTML Full Text](https://arxiv.org/html/2402.10978)\n- [ICML Proceedings](https://proceedings.mlr.press/v235/mohri24a.html)\n- [OpenReview Forum](https://openreview.net/forum?id=uYISs2tpwP)\n- [ICML Virtual Poster](https://icml.cc/virtual/2024/poster/32822)\n- [GitHub Repository](https://github.com/tatsu-lab/conformal-factual-lm)\n- [Liner Quick Review](https://liner.com/review/language-models-with-conformal-factuality-guarantees)\n- [Enhanced Conformal Prediction (NeurIPS 2024)](https://arxiv.org/html/2406.09714v1)\n- [Coherent Factuality (2025)](https://arxiv.org/abs/2505.17126)\n- [Conditional Factuality Control](https://arxiv.org/abs/2603.27403)\n- [Adaptive Conformal Prediction](https://arxiv.org/html/2604.13991)\n- [Semantic Scholar](https://www.semanticscholar.org/paper/Language-Models-with-Conformal-Factuality-Mohri-Hashimoto/2495700b4303512784fbdbfccc58c6c4f7771ac2)"
      }
    ],
    "totalDurationMs": 218076,
    "totalTokens": 26814,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 330,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 22862,
      "output_tokens": 2950,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 672
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 330,
          "output_tokens": 2950,
          "cache_read_input_tokens": 22862,
          "cache_creation_input_tokens": 672,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 672,
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
  "sourceToolAssistantUUID": "fcbf6498-e37b-4cef-b55c-837ed5d47c59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
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
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "096fd340-561d-4352-8e9a-828c0c94a80a",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze conformal prediction papers for poisoning-robust RAG",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---

### Tool call

_source line 13 · 2026-05-30T06:31:21.843Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01QcWpmRhuD6SuFBJHbC5sEo`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Paper 2: Conformal Factuality RAG Robustness",
  "prompt": "Research the paper \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\" by Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak (arXiv 2026, https://arxiv.org/abs/2603.16817).\n\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebSearch to find any reviews, blog posts, or discussions about this paper\n3. Try to access the full paper content\n\nI need to understand:\n- What gap did they identify?\n- What was their key insight?\n- How did they formulate the problem?\n- What techniques did they use?\n- What were their main findings/conclusions?\n- Any reviewer feedback if available\n\nReport back all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "096fd340-561d-4352-8e9a-828c0c94a80a",
  "isSidechain": false,
  "requestId": "req_011CbYHQrMEeUQPpDEfJoADe",
  "type": "assistant",
  "uuid": "ee89dd5b-2885-45d5-8128-fb778e3cc66d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jn2xmUJTmxmodroKU4uyqw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 14944,
      "output_tokens": 312,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3367,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 312,
          "cache_read_input_tokens": 14944,
          "cache_creation_input_tokens": 3367,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3367
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

_source line 14 · 2026-05-30T06:34:34.296Z_

<details><summary>↩ Tool result · `toolu_01QcWpmRhuD6SuFBJHbC5sEo`</summary>

```text
Now I have gathered comprehensive information. Here is my detailed report.

---

## Detailed Research Report: "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights"

### Paper Metadata
- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak (University of Wisconsin-Madison)
- **ArXiv ID:** 2603.16817, submitted March 17, 2026
- **Length:** 56 pages
- **Venue:** Submitted to ICLR 2026 (OpenReview ID: OKnM5rEUbg, submitted September 15, 2025, modified February 11, 2026)
- **Subject areas:** cs.AI, cs.CL, cs.LG
- **License:** CC BY 4.0

---

### 1. The Gap They Identified

The paper identifies a critical gap at the intersection of two popular approaches for addressing LLM hallucinations:

- **Retrieval-Augmented Generation (RAG):** Grounds LLM responses in retrieved evidence, reducing hallucinations, but provides **no statistical guarantee** that the final output is correct.
- **Conformal Factuality** (introduced by Mohri & Hashimoto, ICML 2024): Provides **distribution-free statistical guarantees** on factuality by decomposing LLM outputs into atomic claims, scoring each claim, and filtering claims below a calibrated threshold. However, it does **not guarantee informativeness** of the final output.

The core gap: **no prior work had systematically studied what happens when these two approaches are combined, and whether the resulting pipeline is actually useful and robust in practice.** Existing evaluation metrics (particularly "empirical factuality") were misleading because they treat empty outputs -- where all claims are filtered out -- as trivially "factual," artificially inflating reported performance.

---

### 2. Their Key Insight

The central insight is the **factuality-informativeness trade-off**: as conformal filtering becomes more aggressive (higher confidence levels), it removes more claims, producing outputs that are technically "factual" but **vacuous** -- containing little to no useful information. Standard metrics completely miss this problem because empty outputs are counted as factually correct by convention.

A secondary key insight is that conformal factuality guarantees are **fragile under distribution shift**: when the test-time data distribution diverges from the calibration data (e.g., different topic domains, or the presence of distractor documents in retrieval), the statistical guarantees break down.

---

### 3. Problem Formulation

The paper formulates the conformal factuality pipeline as a multi-stage process:

1. **Query + Retrieval:** Given a query, retrieve relevant documents from a knowledge base.
2. **Generation:** An LLM generates a response grounded in the retrieved documents.
3. **Decomposition:** The response is parsed into a set of **atomic claims** -- minimal, independently verifiable factual statements.
4. **Scoring:** Each atomic claim is assigned a factuality/uncertainty score using a scoring function (e.g., LLM-based confidence, entailment-based verification).
5. **Calibration:** Using held-out calibration data with known ground truth, a threshold is determined such that retained claims are factual with probability at least (1 - alpha), where alpha is a user-specified error rate.
6. **Filtering:** At test time, claims with scores below the calibrated threshold are removed. The retained claims form the final output.

The paper then systematically analyzes each stage -- generation, scoring, calibration, robustness, and efficiency -- to identify failure modes.

---

### 4. Techniques and Novel Metrics

**Three novel informativeness-aware metrics proposed:**

1. **Non-Empty Rate:** The fraction of outputs that are non-empty after filtering. This directly measures how often the pipeline produces any useful output at all, exposing the vacuous output problem.

2. **Non-Vacuous Empirical Factuality:** Empirical factuality computed **only over non-empty outputs**, removing the artificial inflation caused by counting empty outputs as "factual." This gives a more honest assessment of the pipeline's actual factuality performance.

3. **Sufficient Correctness:** A metric that captures whether the retained claims are not only factual but also **sufficient to answer the original query** -- measuring whether the output retains enough information to be practically useful.

Together, these three metrics jointly capture both correctness and information retention, providing a much more complete picture of pipeline utility than standard factuality measures alone.

**Scoring approaches compared:**
- **LLM-based model confidence scorers:** Use the LLM itself (e.g., GPT-4 confidence, frequency scoring) to estimate claim reliability.
- **Entailment-based verifiers:** Lightweight NLI models that check whether retrieved documents entail each claim.

**Robustness analysis techniques:**
- **Distribution shift experiments:** Calibrating on one topic domain and testing on another.
- **Distractor injection:** Adding irrelevant or misleading documents to the retrieval set to test whether the pipeline degrades gracefully.

---

### 5. Main Findings and Conclusions

The paper presents findings across **three benchmarks** (FActScore, MATH, Natural Questions) and **multiple model families**:

**(i) Low Usefulness at High Factuality Levels:**
Conformal filtering suffers from the vacuous output problem. As the desired factuality guarantee increases (lower alpha), more claims are filtered out, and a large fraction of outputs become completely empty. Standard empirical factuality metrics mask this by treating empty outputs as trivially factual, inflating the reported numbers. The proposed non-empty rate and non-vacuous empirical factuality metrics reveal the true picture: the pipeline often achieves high factuality only by producing uninformative outputs.

**(ii) Fragility Under Distribution Shifts and Distractors:**
The conformal factuality guarantee is **not robust** when calibration data does not closely match deployment conditions. Distribution shifts (different topic domains between calibration and test) and the presence of distractor documents in the retrieved context both cause the statistical guarantees to break down. This is a fundamental limitation of the conformal prediction framework, which assumes exchangeability between calibration and test data.

**(iii) Lightweight Verifiers are Competitive and Efficient:**
Lightweight entailment-based verifiers (small NLI models) **match or outperform** LLM-based model confidence scorers as factuality scoring functions, while requiring **over 100x fewer FLOPs**. This is a significant practical finding: using a small, specialized verifier rather than querying a large LLM for confidence scores can dramatically reduce computational cost without sacrificing accuracy.

**Overall conclusions:**
- The factuality-informativeness trade-off is a fundamental challenge that existing conformal filtering frameworks do not adequately address.
- Robustness to distribution shift and retrieval noise (distractors) must be a first-class concern, not an afterthought.
- New approaches are needed that provide reliability guarantees while maintaining robustness and usefulness as key metrics.
- The paper provides actionable guidance for building RAG pipelines that are both reliable and computationally efficient.

---

### 6. Reviewer Feedback

The paper was submitted to **ICLR 2026** under the title "Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights" (OpenReview ID: OKnM5rEUbg). Unfortunately, **the actual reviewer scores, detailed reviews, and decision are not publicly visible** on the OpenReview page at this time. The page shows only the submission metadata and abstract. ICLR 2026 had an acceptance rate of 27.4% (5,355 accepted out of 13,763 submissions).

The paper was also **presented at the UW-Madison Machine Learning Lunch Meetings** on April 7, 2026, by Ramya Vinayak, indicating it has been actively disseminated within the research community.

No blog posts, Twitter discussions, or third-party reviews were found in the search results.

---

### Context: The Foundational Work This Paper Critiques

The paper builds upon and critically evaluates the conformal factuality framework introduced by **Mohri & Hashimoto (ICML 2024)** in "Language Models with Conformal Factuality Guarantees" (arXiv:2402.10978). That original work showed that conformal prediction could boost factuality from ~25% to ~80% on FActScore while retaining roughly half the original claims. The Chen et al. paper essentially asks: "Does this actually work well in practice when combined with RAG, and is it robust?" -- and finds significant limitations.

A related concurrent work is **"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality"** (arXiv:2506.20978), which takes a complementary approach using conditional conformal prediction for RAG quality assessment, claiming to retain up to 60% more high-quality sub-claims.

---

### Sources
- [arXiv Abstract Page](https://arxiv.org/abs/2603.16817)
- [OpenReview Submission](https://openreview.net/forum?id=OKnM5rEUbg)
- [Mohri & Hashimoto, ICML 2024 - Foundational Conformal Factuality Paper](https://proceedings.mlr.press/v235/mohri24a.html)
- [Related Work: Conditional Conformal Factuality for RAG](https://arxiv.org/abs/2506.20978)
- [ICLR 2026 Review Process Retrospective](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/)
- [Conformal Factuality Code Repository (Mohri & Hashimoto)](https://github.com/tatsu-lab/conformal-factual-lm)

agentId: a281e1bad1eeba58b (use SendMessage with to: 'a281e1bad1eeba58b' to continue this agent)
&lt;usage>total_tokens: 25956
tool_uses: 23
duration_ms: 192447&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee89dd5b-2885-45d5-8128-fb778e3cc66d",
  "isSidechain": false,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "type": "user",
  "uuid": "897b607e-bb0c-4879-bb0c-43a2e83d5ca0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\" by Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak (arXiv 2026, https://arxiv.org/abs/2603.16817).\n\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebSearch to find any reviews, blog posts, or discussions about this paper\n3. Try to access the full paper content\n\nI need to understand:\n- What gap did they identify?\n- What was their key insight?\n- How did they formulate the problem?\n- What techniques did they use?\n- What were their main findings/conclusions?\n- Any reviewer feedback if available\n\nReport back all findings in detail.",
    "agentId": "a281e1bad1eeba58b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have gathered comprehensive information. Here is my detailed report.\n\n---\n\n## Detailed Research Report: \"Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights\"\n\n### Paper Metadata\n- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak (University of Wisconsin-Madison)\n- **ArXiv ID:** 2603.16817, submitted March 17, 2026\n- **Length:** 56 pages\n- **Venue:** Submitted to ICLR 2026 (OpenReview ID: OKnM5rEUbg, submitted September 15, 2025, modified February 11, 2026)\n- **Subject areas:** cs.AI, cs.CL, cs.LG\n- **License:** CC BY 4.0\n\n---\n\n### 1. The Gap They Identified\n\nThe paper identifies a critical gap at the intersection of two popular approaches for addressing LLM hallucinations:\n\n- **Retrieval-Augmented Generation (RAG):** Grounds LLM responses in retrieved evidence, reducing hallucinations, but provides **no statistical guarantee** that the final output is correct.\n- **Conformal Factuality** (introduced by Mohri & Hashimoto, ICML 2024): Provides **distribution-free statistical guarantees** on factuality by decomposing LLM outputs into atomic claims, scoring each claim, and filtering claims below a calibrated threshold. However, it does **not guarantee informativeness** of the final output.\n\nThe core gap: **no prior work had systematically studied what happens when these two approaches are combined, and whether the resulting pipeline is actually useful and robust in practice.** Existing evaluation metrics (particularly \"empirical factuality\") were misleading because they treat empty outputs -- where all claims are filtered out -- as trivially \"factual,\" artificially inflating reported performance.\n\n---\n\n### 2. Their Key Insight\n\nThe central insight is the **factuality-informativeness trade-off**: as conformal filtering becomes more aggressive (higher confidence levels), it removes more claims, producing outputs that are technically \"factual\" but **vacuous** -- containing little to no useful information. Standard metrics completely miss this problem because empty outputs are counted as factually correct by convention.\n\nA secondary key insight is that conformal factuality guarantees are **fragile under distribution shift**: when the test-time data distribution diverges from the calibration data (e.g., different topic domains, or the presence of distractor documents in retrieval), the statistical guarantees break down.\n\n---\n\n### 3. Problem Formulation\n\nThe paper formulates the conformal factuality pipeline as a multi-stage process:\n\n1. **Query + Retrieval:** Given a query, retrieve relevant documents from a knowledge base.\n2. **Generation:** An LLM generates a response grounded in the retrieved documents.\n3. **Decomposition:** The response is parsed into a set of **atomic claims** -- minimal, independently verifiable factual statements.\n4. **Scoring:** Each atomic claim is assigned a factuality/uncertainty score using a scoring function (e.g., LLM-based confidence, entailment-based verification).\n5. **Calibration:** Using held-out calibration data with known ground truth, a threshold is determined such that retained claims are factual with probability at least (1 - alpha), where alpha is a user-specified error rate.\n6. **Filtering:** At test time, claims with scores below the calibrated threshold are removed. The retained claims form the final output.\n\nThe paper then systematically analyzes each stage -- generation, scoring, calibration, robustness, and efficiency -- to identify failure modes.\n\n---\n\n### 4. Techniques and Novel Metrics\n\n**Three novel informativeness-aware metrics proposed:**\n\n1. **Non-Empty Rate:** The fraction of outputs that are non-empty after filtering. This directly measures how often the pipeline produces any useful output at all, exposing the vacuous output problem.\n\n2. **Non-Vacuous Empirical Factuality:** Empirical factuality computed **only over non-empty outputs**, removing the artificial inflation caused by counting empty outputs as \"factual.\" This gives a more honest assessment of the pipeline's actual factuality performance.\n\n3. **Sufficient Correctness:** A metric that captures whether the retained claims are not only factual but also **sufficient to answer the original query** -- measuring whether the output retains enough information to be practically useful.\n\nTogether, these three metrics jointly capture both correctness and information retention, providing a much more complete picture of pipeline utility than standard factuality measures alone.\n\n**Scoring approaches compared:**\n- **LLM-based model confidence scorers:** Use the LLM itself (e.g., GPT-4 confidence, frequency scoring) to estimate claim reliability.\n- **Entailment-based verifiers:** Lightweight NLI models that check whether retrieved documents entail each claim.\n\n**Robustness analysis techniques:**\n- **Distribution shift experiments:** Calibrating on one topic domain and testing on another.\n- **Distractor injection:** Adding irrelevant or misleading documents to the retrieval set to test whether the pipeline degrades gracefully.\n\n---\n\n### 5. Main Findings and Conclusions\n\nThe paper presents findings across **three benchmarks** (FActScore, MATH, Natural Questions) and **multiple model families**:\n\n**(i) Low Usefulness at High Factuality Levels:**\nConformal filtering suffers from the vacuous output problem. As the desired factuality guarantee increases (lower alpha), more claims are filtered out, and a large fraction of outputs become completely empty. Standard empirical factuality metrics mask this by treating empty outputs as trivially factual, inflating the reported numbers. The proposed non-empty rate and non-vacuous empirical factuality metrics reveal the true picture: the pipeline often achieves high factuality only by producing uninformative outputs.\n\n**(ii) Fragility Under Distribution Shifts and Distractors:**\nThe conformal factuality guarantee is **not robust** when calibration data does not closely match deployment conditions. Distribution shifts (different topic domains between calibration and test) and the presence of distractor documents in the retrieved context both cause the statistical guarantees to break down. This is a fundamental limitation of the conformal prediction framework, which assumes exchangeability between calibration and test data.\n\n**(iii) Lightweight Verifiers are Competitive and Efficient:**\nLightweight entailment-based verifiers (small NLI models) **match or outperform** LLM-based model confidence scorers as factuality scoring functions, while requiring **over 100x fewer FLOPs**. This is a significant practical finding: using a small, specialized verifier rather than querying a large LLM for confidence scores can dramatically reduce computational cost without sacrificing accuracy.\n\n**Overall conclusions:**\n- The factuality-informativeness trade-off is a fundamental challenge that existing conformal filtering frameworks do not adequately address.\n- Robustness to distribution shift and retrieval noise (distractors) must be a first-class concern, not an afterthought.\n- New approaches are needed that provide reliability guarantees while maintaining robustness and usefulness as key metrics.\n- The paper provides actionable guidance for building RAG pipelines that are both reliable and computationally efficient.\n\n---\n\n### 6. Reviewer Feedback\n\nThe paper was submitted to **ICLR 2026** under the title \"Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights\" (OpenReview ID: OKnM5rEUbg). Unfortunately, **the actual reviewer scores, detailed reviews, and decision are not publicly visible** on the OpenReview page at this time. The page shows only the submission metadata and abstract. ICLR 2026 had an acceptance rate of 27.4% (5,355 accepted out of 13,763 submissions).\n\nThe paper was also **presented at the UW-Madison Machine Learning Lunch Meetings** on April 7, 2026, by Ramya Vinayak, indicating it has been actively disseminated within the research community.\n\nNo blog posts, Twitter discussions, or third-party reviews were found in the search results.\n\n---\n\n### Context: The Foundational Work This Paper Critiques\n\nThe paper builds upon and critically evaluates the conformal factuality framework introduced by **Mohri & Hashimoto (ICML 2024)** in \"Language Models with Conformal Factuality Guarantees\" (arXiv:2402.10978). That original work showed that conformal prediction could boost factuality from ~25% to ~80% on FActScore while retaining roughly half the original claims. The Chen et al. paper essentially asks: \"Does this actually work well in practice when combined with RAG, and is it robust?\" -- and finds significant limitations.\n\nA related concurrent work is **\"Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality\"** (arXiv:2506.20978), which takes a complementary approach using conditional conformal prediction for RAG quality assessment, claiming to retain up to 60% more high-quality sub-claims.\n\n---\n\n### Sources\n- [arXiv Abstract Page](https://arxiv.org/abs/2603.16817)\n- [OpenReview Submission](https://openreview.net/forum?id=OKnM5rEUbg)\n- [Mohri & Hashimoto, ICML 2024 - Foundational Conformal Factuality Paper](https://proceedings.mlr.press/v235/mohri24a.html)\n- [Related Work: Conditional Conformal Factuality for RAG](https://arxiv.org/abs/2506.20978)\n- [ICLR 2026 Review Process Retrospective](https://blog.iclr.cc/2026/03/31/a-retrospective-on-the-iclr-2026-review-process/)\n- [Conformal Factuality Code Repository (Mohri & Hashimoto)](https://github.com/tatsu-lab/conformal-factual-lm)"
      }
    ],
    "totalDurationMs": 192447,
    "totalTokens": 25956,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 168,
      "cache_creation_input_tokens": 648,
      "cache_read_input_tokens": 22787,
      "output_tokens": 2353,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 648
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 168,
          "output_tokens": 2353,
          "cache_read_input_tokens": 22787,
          "cache_creation_input_tokens": 648,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 648,
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
  "sourceToolAssistantUUID": "ee89dd5b-2885-45d5-8128-fb778e3cc66d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-30T06:34:41.998Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JQptpJ1pM6X1LvNcBQ5XkC`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Paper 3: CP as Bayesian Quadrature",
  "prompt": "Research the paper \"Conformal Prediction as Bayesian Quadrature\" by Jake C. Snell and Thomas L. Griffiths (ICML 2025, Outstanding Paper Award, https://arxiv.org/abs/2502.13228).\n\n1. Use WebFetch to read the arxiv abstract page and HTML version\n2. Use WebSearch to find OpenReview reviews and any discussion of this paper (it won Outstanding Paper Award at ICML 2025)\n3. Try to find the full paper content\n\nI need to understand:\n- What gap did they identify?\n- What was their key insight?\n- How did they formulate the problem differently from standard CP?\n- What techniques did they adapt/combine?\n- Any reviewer feedback or award discussion\n\nReport back all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "897b607e-bb0c-4879-bb0c-43a2e83d5ca0",
  "isSidechain": false,
  "requestId": "req_011CbYHfiyQ4jtdUePBprRUY",
  "type": "assistant",
  "uuid": "82426a6f-6edc-4652-bc9a-a026db95d21e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPYwT7vtHDzGziQmU6WxJr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2741,
      "cache_read_input_tokens": 18311,
      "output_tokens": 283,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2741,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 283,
          "cache_read_input_tokens": 18311,
          "cache_creation_input_tokens": 2741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2741
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

_source line 16 · 2026-05-30T06:37:50.670Z_

<details><summary>↩ Tool result · `toolu_01JQptpJ1pM6X1LvNcBQ5XkC`</summary>

```text
I now have the reviewer scores and feedback. Let me compile all findings into a comprehensive report.

---

Here is the comprehensive research report on **"Conformal Prediction as Bayesian Quadrature"** by Jake C. Snell and Thomas L. Griffiths (Princeton University).

---

## Paper Metadata

- **arXiv**: 2502.13228 (submitted Feb 18, 2025; revised June 11, 2025)
- **Venue**: ICML 2025 (Oral Presentation), published in PMLR Volume 267, Pages 56068-56084
- **Award**: One of 6 Outstanding Paper Awards from 3,260 accepted / 12,107 submitted papers
- **Code**: https://github.com/jakesnell/conformal-as-bayes-quad
- **Subjects**: cs.LG, cs.AI, stat.ML

---

## 1. The Gap They Identified

The authors identified a fundamental disconnect between the theoretical guarantees of conformal prediction and their practical utility:

**Marginal vs. data-conditional guarantees.** Standard conformal prediction (and its extension, Conformal Risk Control / CRC) provides *marginal* guarantees -- they control expected loss *averaged over many hypothetical unobserved datasets*. But practitioners care about whether the method works *on their specific calibration dataset*. The marginal guarantee can be frequently violated for individual datasets while still holding on average.

They demonstrated this empirically: CRC exceeded its target risk threshold in **21.2% of trials** on synthetic binomial data and **45.0% of trials** on MS-COCO multilabel classification, despite maintaining valid average guarantees. The gap exists because the frequentist guarantee averages over randomness in the calibration data itself, which is already observed at deployment time.

Additionally, frequentist conformal methods **cannot incorporate prior knowledge** about deployment conditions and produce only a **single point estimate** (a threshold), providing no information about the full range of plausible losses.

---

## 2. The Key Insight

The central insight is that **bounding the expected loss of a model can be reformulated as a numerical integration problem** -- specifically, integrating the quantile function of the loss distribution over [0,1]. This transforms the problem into one amenable to **Bayesian quadrature**, a well-studied technique for probabilistic numerical integration.

The second critical insight is that **the quantile spacings of i.i.d. samples follow a symmetric Dirichlet distribution, regardless of the underlying loss distribution**. This classical result from distribution-free statistics means you get a known distribution over the "evaluation points" of the integral without assuming anything about the loss distribution itself -- preserving the distribution-free property while enabling a Bayesian treatment.

---

## 3. How They Reformulated the Problem

### Standard CP formulation
Standard conformal prediction works in a frequentist decision-theoretic framework: choose a control parameter lambda to minimize worst-case risk R_bar(lambda) = sup_theta R(theta, lambda), where theta represents the unknown state of nature.

### Their Bayesian reformulation (3 steps)

**Step 1 -- Decision-theoretic framing:** They showed that both split conformal prediction and conformal risk control are special cases of choosing lambda to make R_bar(lambda) <= alpha. They proved this equivalence formally (recovering both SCP and CRC as propositions).

**Step 2 -- Bayes risk equivalence:** They introduced a prior pi over theta and the integrated risk r(pi, lambda) = integral of R(theta, lambda) pi(theta) d(theta). A crucial result: the supremum over all priors of the integrated risk equals the maximum risk:

> sup_pi r(pi, lambda) = sup_theta R(theta, lambda) = R_bar(lambda)

This means controlling the worst-case Bayes risk is equivalent to controlling the frequentist maximum risk.

**Step 3 -- Quadrature reformulation:** The posterior risk (expected loss given calibration data) can be written as E[L | data] = integral from 0 to 1 of K(t) dt, where K is the quantile function of the loss distribution. The calibration losses are observations of K at unknown quantile locations t_i. This is exactly a Bayesian quadrature problem -- estimating an integral given noisy/uncertain function evaluations -- but with the unique twist that the evaluation sites t_i are also unknown.

---

## 4. Techniques They Adapted and Combined

The paper elegantly combines ideas from three areas:

### (a) Bayesian Quadrature
Classical Bayesian quadrature places a prior over the integrand (here, the quantile function K) and computes a posterior distribution over the integral value. The authors use this framework but crucially **eliminate the need for an explicit prior** by taking a supremum over all priors.

### (b) Distribution-Free Tolerance Regions
The classical result (Lemma 4.4) that quantile spacings (u_1, ..., u_{n+1}) of n i.i.d. samples from any continuous distribution follow Dir(1, 1, ..., 1) -- a uniform Dirichlet distribution. This provides the distribution over the unknown evaluation sites without any distributional assumptions.

### (c) Right Rectangular Integration
By using a conservative (right-endpoint) rectangular rule for integration and the monotonicity of the quantile function, they construct an upper bound that avoids specifying any prior.

### Key Theorems

**Theorem 4.3 (Prior-free upper bound):** sup_pi E[L | t_{1:n}, l_{1:n}] <= sum_{i=1}^{n+1} u_i * l_{(i)}, where u_i are quantile spacings and l_{(i)} are order statistics of losses (with l_{(n+1)} = B, the loss bound).

**Theorem 4.5 (Stochastic dominance):** The random variable L+ = sum_{i=1}^{n+1} U_i * l_{(i)}, where (U_1,...,U_{n+1}) ~ Dir(1,...,1), stochastically dominates the posterior risk under any prior. That is: inf_pi Pr(L <= b | data) >= Pr(L+ <= b).

This means L+ provides a **full posterior distribution** over a provable upper bound on expected loss, from which one can extract any desired credible interval.

### Recovery of Existing Methods

The expected value E[L+] = (1/(n+1)) * (sum of losses + B), which is exactly the CRC statistic. So CRC uses only the mean of L+, discarding all distributional information. The full distribution enables much tighter, data-conditional control.

---

## 5. Experimental Results

Three experimental settings validated the approach:

| Setting | Method | Violation Rate | Interval/Set Size |
|---|---|---|---|
| Synthetic Binomial | CRC | 21.20% | -- |
| Synthetic Binomial | Bayesian HPD | **0.03%** | -- |
| Heteroskedastic Regression | CRC (RCPS) | -- | 13.99 |
| Heteroskedastic Regression | Bayesian | **3.42% violation** | **9.14** |
| MS-COCO (FNR @ 5%) | CRC | 45.0% failure | 2.9 |
| MS-COCO (FNR @ 5%) | Bayesian | **5.4% failure** | 3.0 |

The method consistently achieved dramatically lower violation rates while maintaining competitive or smaller prediction sets.

---

## 6. Reviewer Feedback (ICML 2025 OpenReview)

The paper received 4 reviews with scores: **4/5, 4/5, 5/5, 3/5**.

### Strengths identified by reviewers:
- **"Entirely novel"** combination of Bayesian quadrature with distribution-free quantile spacing analysis
- Practical advantages: avoids explicit prior specification while producing shorter prediction intervals than baselines
- **"Proofs are well-written and easy to follow"**
- The framework unifies existing methods (SCP and CRC) as special cases

### Primary concerns raised:
1. **Conditional vs. marginal coverage**: Reviewers questioned whether the guarantees were truly "conditional." The authors clarified these are "data-conditional" (conditioned on observed calibration losses), not input-conditional guarantees -- an important distinction.
2. **Limited experimental scope**: The original submission focused mainly on conformal risk control scenarios. The authors responded by adding heteroskedastic prediction interval experiments showing competitive performance.
3. **Figure 1 clarity**: Reviewers flagged that Figure 1 needed clarification regarding the step function's role; authors acknowledged and revised.

### Decision
**Accept (Oral Presentation)**, with the program chairs noting: *"This is a refreshingly novel paper and I recommend accepting this paper with an oral presentation."*

---

## 7. Award Context and Significance

The paper was one of 6 Outstanding Papers at ICML 2025 (acceptance rate for this award: ~0.05% of submissions). Commentary from the Gonzo ML newsletter described it as a **"Brilliant reframing"** that shifts from aggregate-level guarantees to personalized, dataset-specific ones. The significance for high-stakes applications (medical diagnosis, criminal justice, finance) was particularly emphasized -- having confidence bounds calibrated to particular data instances rather than population statistics reduces the gap between theoretical guarantees and real-world deployment.

The other 5 Outstanding Papers were: CollabLLM, Train for the Worst/Plan for the Best (masked diffusions), Roll the dice & look before you leap (next-token prediction), Score Matching with Missing Data, and The Value of Prediction in Identifying the Worst-Off.

---

## Summary of the Intellectual Contribution

The paper's core move is deceptively simple but profound: instead of asking "does my method control risk on average across all possible calibration sets?" (the frequentist question), it asks "given the calibration losses I actually observed, what is the distribution of plausible expected losses I might face?" (the Bayesian question). By reformulating expected loss as an integral, leveraging distribution-free properties of quantile spacings, and constructing a stochastic upper bound L+, they obtain a full posterior distribution over risk that is both distribution-free and data-conditional. Existing conformal methods emerge as special cases that use only the mean of this distribution, explaining why they can have high violation rates -- they throw away the distributional information that would enable tighter control.

Sources:
- [arXiv Abstract](https://arxiv.org/abs/2502.13228)
- [arXiv HTML Full Paper](https://arxiv.org/html/2502.13228)
- [PMLR Proceedings](https://proceedings.mlr.press/v267/snell25a.html)
- [OpenReview Forum](https://openreview.net/forum?id=PNmkjIzHB7)
- [Project Page (Jake Snell)](https://jakesnell.com/projects/conformal-as-bayes-quad/)
- [GitHub Repository](https://github.com/jakesnell/conformal-as-bayes-quad)
- [ICML Virtual Poster](https://icml.cc/virtual/2025/poster/45390)
- [Gonzo ML - ICML 2025 Outstanding Papers](https://gonzoml.substack.com/p/the-icml-2025-outstanding-papers)
- [ArXivIQ Analysis](https://arxiviq.substack.com/p/icml-2025-conformal-prediction-as)
- [Moonlight Literature Review](https://www.themoonlight.io/en/review/conformal-prediction-as-bayesian-quadrature)

agentId: abdc426c0379504b8 (use SendMessage with to: 'abdc426c0379504b8' to continue this agent)
&lt;usage>total_tokens: 27033
tool_uses: 22
duration_ms: 188667&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82426a6f-6edc-4652-bc9a-a026db95d21e",
  "isSidechain": false,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "type": "user",
  "uuid": "9e25054f-9293-4af5-9dde-eb2899e735b2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Conformal Prediction as Bayesian Quadrature\" by Jake C. Snell and Thomas L. Griffiths (ICML 2025, Outstanding Paper Award, https://arxiv.org/abs/2502.13228).\n\n1. Use WebFetch to read the arxiv abstract page and HTML version\n2. Use WebSearch to find OpenReview reviews and any discussion of this paper (it won Outstanding Paper Award at ICML 2025)\n3. Try to find the full paper content\n\nI need to understand:\n- What gap did they identify?\n- What was their key insight?\n- How did they formulate the problem differently from standard CP?\n- What techniques did they adapt/combine?\n- Any reviewer feedback or award discussion\n\nReport back all findings in detail.",
    "agentId": "abdc426c0379504b8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have the reviewer scores and feedback. Let me compile all findings into a comprehensive report.\n\n---\n\nHere is the comprehensive research report on **\"Conformal Prediction as Bayesian Quadrature\"** by Jake C. Snell and Thomas L. Griffiths (Princeton University).\n\n---\n\n## Paper Metadata\n\n- **arXiv**: 2502.13228 (submitted Feb 18, 2025; revised June 11, 2025)\n- **Venue**: ICML 2025 (Oral Presentation), published in PMLR Volume 267, Pages 56068-56084\n- **Award**: One of 6 Outstanding Paper Awards from 3,260 accepted / 12,107 submitted papers\n- **Code**: https://github.com/jakesnell/conformal-as-bayes-quad\n- **Subjects**: cs.LG, cs.AI, stat.ML\n\n---\n\n## 1. The Gap They Identified\n\nThe authors identified a fundamental disconnect between the theoretical guarantees of conformal prediction and their practical utility:\n\n**Marginal vs. data-conditional guarantees.** Standard conformal prediction (and its extension, Conformal Risk Control / CRC) provides *marginal* guarantees -- they control expected loss *averaged over many hypothetical unobserved datasets*. But practitioners care about whether the method works *on their specific calibration dataset*. The marginal guarantee can be frequently violated for individual datasets while still holding on average.\n\nThey demonstrated this empirically: CRC exceeded its target risk threshold in **21.2% of trials** on synthetic binomial data and **45.0% of trials** on MS-COCO multilabel classification, despite maintaining valid average guarantees. The gap exists because the frequentist guarantee averages over randomness in the calibration data itself, which is already observed at deployment time.\n\nAdditionally, frequentist conformal methods **cannot incorporate prior knowledge** about deployment conditions and produce only a **single point estimate** (a threshold), providing no information about the full range of plausible losses.\n\n---\n\n## 2. The Key Insight\n\nThe central insight is that **bounding the expected loss of a model can be reformulated as a numerical integration problem** -- specifically, integrating the quantile function of the loss distribution over [0,1]. This transforms the problem into one amenable to **Bayesian quadrature**, a well-studied technique for probabilistic numerical integration.\n\nThe second critical insight is that **the quantile spacings of i.i.d. samples follow a symmetric Dirichlet distribution, regardless of the underlying loss distribution**. This classical result from distribution-free statistics means you get a known distribution over the \"evaluation points\" of the integral without assuming anything about the loss distribution itself -- preserving the distribution-free property while enabling a Bayesian treatment.\n\n---\n\n## 3. How They Reformulated the Problem\n\n### Standard CP formulation\nStandard conformal prediction works in a frequentist decision-theoretic framework: choose a control parameter lambda to minimize worst-case risk R_bar(lambda) = sup_theta R(theta, lambda), where theta represents the unknown state of nature.\n\n### Their Bayesian reformulation (3 steps)\n\n**Step 1 -- Decision-theoretic framing:** They showed that both split conformal prediction and conformal risk control are special cases of choosing lambda to make R_bar(lambda) <= alpha. They proved this equivalence formally (recovering both SCP and CRC as propositions).\n\n**Step 2 -- Bayes risk equivalence:** They introduced a prior pi over theta and the integrated risk r(pi, lambda) = integral of R(theta, lambda) pi(theta) d(theta). A crucial result: the supremum over all priors of the integrated risk equals the maximum risk:\n\n> sup_pi r(pi, lambda) = sup_theta R(theta, lambda) = R_bar(lambda)\n\nThis means controlling the worst-case Bayes risk is equivalent to controlling the frequentist maximum risk.\n\n**Step 3 -- Quadrature reformulation:** The posterior risk (expected loss given calibration data) can be written as E[L | data] = integral from 0 to 1 of K(t) dt, where K is the quantile function of the loss distribution. The calibration losses are observations of K at unknown quantile locations t_i. This is exactly a Bayesian quadrature problem -- estimating an integral given noisy/uncertain function evaluations -- but with the unique twist that the evaluation sites t_i are also unknown.\n\n---\n\n## 4. Techniques They Adapted and Combined\n\nThe paper elegantly combines ideas from three areas:\n\n### (a) Bayesian Quadrature\nClassical Bayesian quadrature places a prior over the integrand (here, the quantile function K) and computes a posterior distribution over the integral value. The authors use this framework but crucially **eliminate the need for an explicit prior** by taking a supremum over all priors.\n\n### (b) Distribution-Free Tolerance Regions\nThe classical result (Lemma 4.4) that quantile spacings (u_1, ..., u_{n+1}) of n i.i.d. samples from any continuous distribution follow Dir(1, 1, ..., 1) -- a uniform Dirichlet distribution. This provides the distribution over the unknown evaluation sites without any distributional assumptions.\n\n### (c) Right Rectangular Integration\nBy using a conservative (right-endpoint) rectangular rule for integration and the monotonicity of the quantile function, they construct an upper bound that avoids specifying any prior.\n\n### Key Theorems\n\n**Theorem 4.3 (Prior-free upper bound):** sup_pi E[L | t_{1:n}, l_{1:n}] <= sum_{i=1}^{n+1} u_i * l_{(i)}, where u_i are quantile spacings and l_{(i)} are order statistics of losses (with l_{(n+1)} = B, the loss bound).\n\n**Theorem 4.5 (Stochastic dominance):** The random variable L+ = sum_{i=1}^{n+1} U_i * l_{(i)}, where (U_1,...,U_{n+1}) ~ Dir(1,...,1), stochastically dominates the posterior risk under any prior. That is: inf_pi Pr(L <= b | data) >= Pr(L+ <= b).\n\nThis means L+ provides a **full posterior distribution** over a provable upper bound on expected loss, from which one can extract any desired credible interval.\n\n### Recovery of Existing Methods\n\nThe expected value E[L+] = (1/(n+1)) * (sum of losses + B), which is exactly the CRC statistic. So CRC uses only the mean of L+, discarding all distributional information. The full distribution enables much tighter, data-conditional control.\n\n---\n\n## 5. Experimental Results\n\nThree experimental settings validated the approach:\n\n| Setting | Method | Violation Rate | Interval/Set Size |\n|---|---|---|---|\n| Synthetic Binomial | CRC | 21.20% | -- |\n| Synthetic Binomial | Bayesian HPD | **0.03%** | -- |\n| Heteroskedastic Regression | CRC (RCPS) | -- | 13.99 |\n| Heteroskedastic Regression | Bayesian | **3.42% violation** | **9.14** |\n| MS-COCO (FNR @ 5%) | CRC | 45.0% failure | 2.9 |\n| MS-COCO (FNR @ 5%) | Bayesian | **5.4% failure** | 3.0 |\n\nThe method consistently achieved dramatically lower violation rates while maintaining competitive or smaller prediction sets.\n\n---\n\n## 6. Reviewer Feedback (ICML 2025 OpenReview)\n\nThe paper received 4 reviews with scores: **4/5, 4/5, 5/5, 3/5**.\n\n### Strengths identified by reviewers:\n- **\"Entirely novel\"** combination of Bayesian quadrature with distribution-free quantile spacing analysis\n- Practical advantages: avoids explicit prior specification while producing shorter prediction intervals than baselines\n- **\"Proofs are well-written and easy to follow\"**\n- The framework unifies existing methods (SCP and CRC) as special cases\n\n### Primary concerns raised:\n1. **Conditional vs. marginal coverage**: Reviewers questioned whether the guarantees were truly \"conditional.\" The authors clarified these are \"data-conditional\" (conditioned on observed calibration losses), not input-conditional guarantees -- an important distinction.\n2. **Limited experimental scope**: The original submission focused mainly on conformal risk control scenarios. The authors responded by adding heteroskedastic prediction interval experiments showing competitive performance.\n3. **Figure 1 clarity**: Reviewers flagged that Figure 1 needed clarification regarding the step function's role; authors acknowledged and revised.\n\n### Decision\n**Accept (Oral Presentation)**, with the program chairs noting: *\"This is a refreshingly novel paper and I recommend accepting this paper with an oral presentation.\"*\n\n---\n\n## 7. Award Context and Significance\n\nThe paper was one of 6 Outstanding Papers at ICML 2025 (acceptance rate for this award: ~0.05% of submissions). Commentary from the Gonzo ML newsletter described it as a **\"Brilliant reframing\"** that shifts from aggregate-level guarantees to personalized, dataset-specific ones. The significance for high-stakes applications (medical diagnosis, criminal justice, finance) was particularly emphasized -- having confidence bounds calibrated to particular data instances rather than population statistics reduces the gap between theoretical guarantees and real-world deployment.\n\nThe other 5 Outstanding Papers were: CollabLLM, Train for the Worst/Plan for the Best (masked diffusions), Roll the dice & look before you leap (next-token prediction), Score Matching with Missing Data, and The Value of Prediction in Identifying the Worst-Off.\n\n---\n\n## Summary of the Intellectual Contribution\n\nThe paper's core move is deceptively simple but profound: instead of asking \"does my method control risk on average across all possible calibration sets?\" (the frequentist question), it asks \"given the calibration losses I actually observed, what is the distribution of plausible expected losses I might face?\" (the Bayesian question). By reformulating expected loss as an integral, leveraging distribution-free properties of quantile spacings, and constructing a stochastic upper bound L+, they obtain a full posterior distribution over risk that is both distribution-free and data-conditional. Existing conformal methods emerge as special cases that use only the mean of this distribution, explaining why they can have high violation rates -- they throw away the distributional information that would enable tighter control.\n\nSources:\n- [arXiv Abstract](https://arxiv.org/abs/2502.13228)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2502.13228)\n- [PMLR Proceedings](https://proceedings.mlr.press/v267/snell25a.html)\n- [OpenReview Forum](https://openreview.net/forum?id=PNmkjIzHB7)\n- [Project Page (Jake Snell)](https://jakesnell.com/projects/conformal-as-bayes-quad/)\n- [GitHub Repository](https://github.com/jakesnell/conformal-as-bayes-quad)\n- [ICML Virtual Poster](https://icml.cc/virtual/2025/poster/45390)\n- [Gonzo ML - ICML 2025 Outstanding Papers](https://gonzoml.substack.com/p/the-icml-2025-outstanding-papers)\n- [ArXivIQ Analysis](https://arxiviq.substack.com/p/icml-2025-conformal-prediction-as)\n- [Moonlight Literature Review](https://www.themoonlight.io/en/review/conformal-prediction-as-bayesian-quadrature)"
      }
    ],
    "totalDurationMs": 188667,
    "totalTokens": 27033,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1060,
      "cache_read_input_tokens": 23181,
      "output_tokens": 2791,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1060
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2791,
          "cache_read_input_tokens": 23181,
          "cache_creation_input_tokens": 1060,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1060,
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
      "otherToolCount": 22
    }
  },
  "sourceToolAssistantUUID": "82426a6f-6edc-4652-bc9a-a026db95d21e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "9e25054f-9293-4af5-9dde-eb2899e735b2",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze conformal prediction papers for poisoning-robust RAG",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---

### Tool call

_source line 19 · 2026-05-30T06:37:58.390Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0168ecpF1gLBG5RUNGipjoy6`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Paper 4: CP for NLP Survey",
  "prompt": "Research the paper \"Conformal Prediction for Natural Language Processing: A Survey\" by Margarida M. Campos, Antonio Farinhas, Chrysoula Zerva, Mario A.T. Figueiredo, Andre F.T. Martins (TACL 2024, https://arxiv.org/abs/2405.01976).\n\n1. Use WebFetch to read the arxiv abstract page and HTML version\n2. Use WebSearch to find any reviews, discussions, or citations of this paper\n3. Try to access the full paper content\n\nI need to understand:\n- What gap did they identify in the literature?\n- How did they organize/categorize CP for NLP?\n- What open challenges did they highlight?\n- What techniques and applications did they cover?\n- Any reviewer feedback if available (TACL reviews are sometimes public)\n\nReport back all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e25054f-9293-4af5-9dde-eb2899e735b2",
  "isSidechain": false,
  "requestId": "req_011CbYHvCXVQbmJ1TsvZ3EY2",
  "type": "assistant",
  "uuid": "be00c54b-58e5-4a7d-aec0-05208c333f90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177HdVqSxrcaN34MnMXMhT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3149,
      "cache_read_input_tokens": 21052,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3149,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 21052,
          "cache_creation_input_tokens": 3149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3149
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

_source line 20 · 2026-05-30T06:41:26.141Z_

<details><summary>↩ Tool result · `toolu_0168ecpF1gLBG5RUNGipjoy6`</summary>

```text
Now I have comprehensive information. Let me compile my detailed report.

---

Here is a detailed research report on **"Conformal Prediction for Natural Language Processing: A Survey"** by Campos, Farinhas, Zerva, Figueiredo, and Martins.

---

## Publication Details

- **Venue:** Transactions of the Association for Computational Linguistics (TACL), Volume 12, pages 1497--1516, 2024
- **Action Editor:** Roi Reichart
- **Timeline:** Submitted May 2024 on arXiv; revision batch July 2024; published November 2024
- **DOI:** 10.1162/tacl_a_00715
- **ArXiv:** 2405.01976
- **License:** CC BY 4.0
- **Available at:** [ACL Anthology](https://aclanthology.org/2024.tacl-1.82/), [MIT Press](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language), [arXiv](https://arxiv.org/abs/2405.01976)

---

## 1. Gap Identified in the Literature

The authors identify several interrelated gaps:

1. **Most NLP systems return only point estimates** without reliable confidence information. When systems do attempt uncertainty quantification, they often make incorrect distributional assumptions, are poorly calibrated, or are computationally too demanding for large-scale use.

2. **LLM hallucinations are frequent** and models lack mechanisms to signal when they are uncertain, making them unreliable in high-stakes applications (medical, legal, etc.).

3. **No prior survey existed at the intersection of conformal prediction and NLP.** General CP surveys existed (Angelopoulos & Bates 2023; Shafer & Vovk 2008), and general uncertainty quantification surveys for NLP existed (Baan et al. 2023; Hu et al. 2023), but none specifically bridged CP techniques to NLP applications.

The authors explicitly scope the paper: **"This is not a general survey on uncertainty quantification and does not include techniques not based on CP."** They focus exclusively on conformal prediction methods and their NLP applications.

---

## 2. How They Organized/Categorized CP for NLP

The paper follows a structure that moves from theory to practice to future vision:

### Section 1: Introduction
- Motivation, scope, and what the survey is NOT about

### Section 2: Conformal Predictors (Foundations)
- **Core definition:** For a test input, CP yields a prediction set C_alpha(x_test) that includes the true target y_test with probability at least 1-alpha, where alpha is user-chosen
- **Non-conformity scores:** Functions s: X x Y -> R measuring how unlikely an input-output pair is relative to calibration data
- **Split CP procedure:** Three steps -- (1) compute calibration scores, (2) set quantile threshold, (3) output prediction set containing all y where s(x_test, y) <= q-hat
- **Theoretical guarantees:** The foundational coverage guarantee P[Y_test in C_alpha(X_test)] >= 1-alpha under only the exchangeability assumption
- **Hypothesis testing connection**
- **Efficiency metrics and pointwise metrics** for evaluating CP quality

### Section 3: Extending Conformal Prediction (CP Variants)

This is a major organizational contribution. The variants covered:

- **Mondrian Conformal Predictors:** Provide class-conditional coverage guarantees by computing class-specific quantiles. Critical for tasks with class imbalance.

- **Beyond Exchangeability:** Handles covariate shift, label shift, and time series via weighted approaches. Uses total variation distance bounds (Barber et al. 2023) where weights are chosen so calibration samples have distributions similar to test data. Key insight: the coverage gap can be bounded but involves computing TV distance between unknown distributions, which is hard.

- **Conformal Risk Control:** Extends CP beyond simple set coverage to control arbitrary loss functions. Angelopoulos et al. (2024) handle monotone losses; Bates et al. (2021) handle non-monotone losses via "Learn-Then-Test." Farinhas et al. (2024) extend to non-exchangeable conformal risk control.

- **Full Conformal Prediction:** The original Vovk et al. (2005) variant that uses the entire training set and involves model refitting for each possible label -- high computational cost but useful with limited data.

- **Cross-Validation and Jackknife variants:** Cross-conformal predictors and jackknife+ (Barber et al. 2021) with leave-one-out schemes.

- **Density-Based CP:** Uses p(x|y) instead of p(y|x) to build cautious predictors that output the null set when underconfident, useful for outlier detection.

- **Venn-Abers Predictors:** Produce one probability distribution per possible label with guarantees that one is perfectly calibrated, serving as a calibration tool.

### Section 4: Applications in NLP

Organized into four major application categories:

**A. Text Classification & Tagging:**
- Binary sentiment classification with BERT
- Density-based CP for handling outliers
- Part-of-speech tagging (tight prediction sets at 99% confidence)
- Multilabel classification using label powerset approach
- Few-shot learning with meta-learned non-conformity measures
- Data cleaning using small calibrated sets

**B. Natural Language Generation:**
- *Sentence-level:* Robot planning with formal task completion guarantees; sampling with coverage guarantees; controlling word error rates in speech recognition
- *Token-level:* Conformal nucleus sampling calibrating LLM overconfidence; dynamic calibration for machine translation

**C. Uncertainty-Based Evaluation:**
- Benchmarking LLM performance with uncertainty quantification
- Machine translation quality estimation using k-NN distances
- Reference-based MT evaluation with equalized coverage

**D. Faster Inference:**
- Early exiting transformers with consistency guarantees
- Zero-shot classification efficiency via label reduction
- Decoder early exiting with quality guarantees
- Optimization of model complexity/accuracy trade-offs

### Section 5: Future Directions
### Section 6: Conclusion

---

## 3. Open Challenges Highlighted

The paper identifies challenges at multiple levels:

### Token-Level Challenges:
- **Quantifying coverage gaps:** The non-exchangeability bounds involve computing total variation distance between unknown distributions, which is hard to estimate in practice
- **Choosing appropriate weights:** No clear strategies exist for selecting weights for non-exchangeable data in autoregressive generation

### Sentence-Level Challenges:
- **High cardinality of output spaces:** In generation tasks, the output space is combinatorially large, making standard CP difficult to apply
- **Impact of finite sampling:** Open questions about how sampling a finite set of possible outputs affects coverage guarantees

### Broader Future Directions:

1. **Human-Computer Interaction:** Prediction sets naturally fit recommendation systems and interactive MT; CP can improve efficiency and quality of human-in-the-loop systems, including preference data collection for LLM alignment.

2. **Label Variation:** Distinguishing model uncertainty from valid human label disagreement. The complexity of natural language means multiple valid outputs are common (e.g., ChaosNLI shows valid disagreements in textual inference). CP prediction sets can provide "a more faithful representation of label variation" compared to methods that focus only on majority labels.

3. **Fairness:** CP can achieve equalized coverage for different population groups (Romano et al. 2020), correcting biases without expensive retraining. Conditional guarantees (Gibbs et al. 2023) for pointwise error bounds can also contribute to fairness.

4. **Data Limitations:** CP can guide active learning by selecting points with larger prediction sets for manual labeling. CP can also reduce label spaces in high-cardinality tasks and serve as a data filtering/cleaning tool for LLMs.

5. **Uncertainty-Aware Evaluation:** Using conformal predictors to more reliably assess model performance, especially in the context of LLM-as-judge evaluation where confidence in evaluations is uncertain. Different non-conformity scores can be compared to evaluate uncertainty heuristics.

---

## 4. Techniques and Applications Summary

**Core CP Techniques Covered:**
| Category | Techniques |
|---|---|
| Standard | Split CP, Full CP, Cross-conformal, Jackknife+ |
| Conditional | Mondrian CP (class-conditional guarantees) |
| Non-exchangeable | Weighted CP (Barber et al. 2023), covariate/label shift |
| Risk control | Conformal Risk Control, Learn-Then-Test |
| Specialized | Density-based CP, Venn-Abers Predictors |

**NLP Applications Covered:**
| Application | Example Methods |
|---|---|
| Sentiment classification | BERT + split CP |
| POS tagging | CP with 99% coverage |
| Multilabel classification | Label powerset + CP |
| Few-shot learning | Meta-learned non-conformity scores |
| Machine translation | Dynamic calibration, quality estimation |
| Text generation | Conformal nucleus sampling |
| Speech recognition | Word error rate control |
| Robot planning | Formal task completion guarantees |
| Model evaluation | Equalized coverage evaluation |
| Efficient inference | Early exiting with CP guarantees |

**Key technical contribution of the survey:** Demonstrating that CP transforms standard NLP systems into uncertainty-aware systems with formal guarantees, requiring only a small calibration dataset and no model retraining. The framework is model-agnostic and distribution-free, requiring only data exchangeability (or weighted extensions for non-exchangeable settings).

---

## 5. Reviewer Feedback

**TACL reviews are unfortunately not publicly available** for this paper. TACL uses a non-public review process (unlike venues that use OpenReview with public reviews). I searched the ACL Anthology page, MIT Press page, OpenReview, and general web -- no reviewer comments are visible anywhere. The only editorial information available is:

- **Action Editor:** Roi Reichart
- The paper was accepted and published in TACL Volume 12 (2024)

The fact that it was accepted at TACL (a highly selective journal with approximately 25-30% acceptance rate) and handled by Roi Reichart (a prominent researcher in NLP uncertainty and learning) suggests favorable reviews.

---

## 6. Impact and Citing Work

The paper has been generating citations since its publication. Notable related/citing work includes:

- **ConU (EMNLP 2024 Findings):** "Conformal Uncertainty in Large Language Models with Correctness Coverage Guarantees" -- applies CP to black-box LLMs for open-ended NLG with self-consistency-based uncertainty measures
- **"Mitigating LLM Hallucinations via Conformal Abstention" (2024):** Uses CP to determine when LLMs should abstain from responding, with guarantees on hallucination rate
- **"An Empirical Study of Conformal Prediction in LLM with ASP Scaffolds for Robust Reasoning" (2025):** Extends CP to LLM reasoning
- **"Conformal Prediction: A Data Perspective" (Zhou et al. 2024):** A broader CP survey that cites Campos et al. for its NLP coverage
- **"Conformal Prediction and Trustworthy AI" (Springer, 2024):** Book chapter citing this survey

The paper appears on the EMNLP 2024 accepted TACL papers list, indicating it was presented at EMNLP 2024.

---

## Key Takeaway

This survey fills a clear gap as the first dedicated treatment of conformal prediction for NLP. Its primary value is the systematic organization of CP variants (standard, conditional, non-exchangeable, risk-controlling) mapped onto NLP application categories (classification, generation, evaluation, efficiency). The most significant open challenges it identifies center on the fundamental tension between CP's exchangeability requirement and the autoregressive, high-cardinality nature of language generation -- particularly the difficulty of estimating coverage gaps in non-exchangeable settings and handling combinatorially large output spaces.

agentId: a627efcf8e59e205b (use SendMessage with to: 'a627efcf8e59e205b' to continue this agent)
&lt;usage>total_tokens: 30046
tool_uses: 22
duration_ms: 207745&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be00c54b-58e5-4a7d-aec0-05208c333f90",
  "isSidechain": false,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "type": "user",
  "uuid": "7f4de65a-8f33-4cf3-a6f7-49da3091299a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Conformal Prediction for Natural Language Processing: A Survey\" by Margarida M. Campos, Antonio Farinhas, Chrysoula Zerva, Mario A.T. Figueiredo, Andre F.T. Martins (TACL 2024, https://arxiv.org/abs/2405.01976).\n\n1. Use WebFetch to read the arxiv abstract page and HTML version\n2. Use WebSearch to find any reviews, discussions, or citations of this paper\n3. Try to access the full paper content\n\nI need to understand:\n- What gap did they identify in the literature?\n- How did they organize/categorize CP for NLP?\n- What open challenges did they highlight?\n- What techniques and applications did they cover?\n- Any reviewer feedback if available (TACL reviews are sometimes public)\n\nReport back all findings in detail.",
    "agentId": "a627efcf8e59e205b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile my detailed report.\n\n---\n\nHere is a detailed research report on **\"Conformal Prediction for Natural Language Processing: A Survey\"** by Campos, Farinhas, Zerva, Figueiredo, and Martins.\n\n---\n\n## Publication Details\n\n- **Venue:** Transactions of the Association for Computational Linguistics (TACL), Volume 12, pages 1497--1516, 2024\n- **Action Editor:** Roi Reichart\n- **Timeline:** Submitted May 2024 on arXiv; revision batch July 2024; published November 2024\n- **DOI:** 10.1162/tacl_a_00715\n- **ArXiv:** 2405.01976\n- **License:** CC BY 4.0\n- **Available at:** [ACL Anthology](https://aclanthology.org/2024.tacl-1.82/), [MIT Press](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language), [arXiv](https://arxiv.org/abs/2405.01976)\n\n---\n\n## 1. Gap Identified in the Literature\n\nThe authors identify several interrelated gaps:\n\n1. **Most NLP systems return only point estimates** without reliable confidence information. When systems do attempt uncertainty quantification, they often make incorrect distributional assumptions, are poorly calibrated, or are computationally too demanding for large-scale use.\n\n2. **LLM hallucinations are frequent** and models lack mechanisms to signal when they are uncertain, making them unreliable in high-stakes applications (medical, legal, etc.).\n\n3. **No prior survey existed at the intersection of conformal prediction and NLP.** General CP surveys existed (Angelopoulos & Bates 2023; Shafer & Vovk 2008), and general uncertainty quantification surveys for NLP existed (Baan et al. 2023; Hu et al. 2023), but none specifically bridged CP techniques to NLP applications.\n\nThe authors explicitly scope the paper: **\"This is not a general survey on uncertainty quantification and does not include techniques not based on CP.\"** They focus exclusively on conformal prediction methods and their NLP applications.\n\n---\n\n## 2. How They Organized/Categorized CP for NLP\n\nThe paper follows a structure that moves from theory to practice to future vision:\n\n### Section 1: Introduction\n- Motivation, scope, and what the survey is NOT about\n\n### Section 2: Conformal Predictors (Foundations)\n- **Core definition:** For a test input, CP yields a prediction set C_alpha(x_test) that includes the true target y_test with probability at least 1-alpha, where alpha is user-chosen\n- **Non-conformity scores:** Functions s: X x Y -> R measuring how unlikely an input-output pair is relative to calibration data\n- **Split CP procedure:** Three steps -- (1) compute calibration scores, (2) set quantile threshold, (3) output prediction set containing all y where s(x_test, y) <= q-hat\n- **Theoretical guarantees:** The foundational coverage guarantee P[Y_test in C_alpha(X_test)] >= 1-alpha under only the exchangeability assumption\n- **Hypothesis testing connection**\n- **Efficiency metrics and pointwise metrics** for evaluating CP quality\n\n### Section 3: Extending Conformal Prediction (CP Variants)\n\nThis is a major organizational contribution. The variants covered:\n\n- **Mondrian Conformal Predictors:** Provide class-conditional coverage guarantees by computing class-specific quantiles. Critical for tasks with class imbalance.\n\n- **Beyond Exchangeability:** Handles covariate shift, label shift, and time series via weighted approaches. Uses total variation distance bounds (Barber et al. 2023) where weights are chosen so calibration samples have distributions similar to test data. Key insight: the coverage gap can be bounded but involves computing TV distance between unknown distributions, which is hard.\n\n- **Conformal Risk Control:** Extends CP beyond simple set coverage to control arbitrary loss functions. Angelopoulos et al. (2024) handle monotone losses; Bates et al. (2021) handle non-monotone losses via \"Learn-Then-Test.\" Farinhas et al. (2024) extend to non-exchangeable conformal risk control.\n\n- **Full Conformal Prediction:** The original Vovk et al. (2005) variant that uses the entire training set and involves model refitting for each possible label -- high computational cost but useful with limited data.\n\n- **Cross-Validation and Jackknife variants:** Cross-conformal predictors and jackknife+ (Barber et al. 2021) with leave-one-out schemes.\n\n- **Density-Based CP:** Uses p(x|y) instead of p(y|x) to build cautious predictors that output the null set when underconfident, useful for outlier detection.\n\n- **Venn-Abers Predictors:** Produce one probability distribution per possible label with guarantees that one is perfectly calibrated, serving as a calibration tool.\n\n### Section 4: Applications in NLP\n\nOrganized into four major application categories:\n\n**A. Text Classification & Tagging:**\n- Binary sentiment classification with BERT\n- Density-based CP for handling outliers\n- Part-of-speech tagging (tight prediction sets at 99% confidence)\n- Multilabel classification using label powerset approach\n- Few-shot learning with meta-learned non-conformity measures\n- Data cleaning using small calibrated sets\n\n**B. Natural Language Generation:**\n- *Sentence-level:* Robot planning with formal task completion guarantees; sampling with coverage guarantees; controlling word error rates in speech recognition\n- *Token-level:* Conformal nucleus sampling calibrating LLM overconfidence; dynamic calibration for machine translation\n\n**C. Uncertainty-Based Evaluation:**\n- Benchmarking LLM performance with uncertainty quantification\n- Machine translation quality estimation using k-NN distances\n- Reference-based MT evaluation with equalized coverage\n\n**D. Faster Inference:**\n- Early exiting transformers with consistency guarantees\n- Zero-shot classification efficiency via label reduction\n- Decoder early exiting with quality guarantees\n- Optimization of model complexity/accuracy trade-offs\n\n### Section 5: Future Directions\n### Section 6: Conclusion\n\n---\n\n## 3. Open Challenges Highlighted\n\nThe paper identifies challenges at multiple levels:\n\n### Token-Level Challenges:\n- **Quantifying coverage gaps:** The non-exchangeability bounds involve computing total variation distance between unknown distributions, which is hard to estimate in practice\n- **Choosing appropriate weights:** No clear strategies exist for selecting weights for non-exchangeable data in autoregressive generation\n\n### Sentence-Level Challenges:\n- **High cardinality of output spaces:** In generation tasks, the output space is combinatorially large, making standard CP difficult to apply\n- **Impact of finite sampling:** Open questions about how sampling a finite set of possible outputs affects coverage guarantees\n\n### Broader Future Directions:\n\n1. **Human-Computer Interaction:** Prediction sets naturally fit recommendation systems and interactive MT; CP can improve efficiency and quality of human-in-the-loop systems, including preference data collection for LLM alignment.\n\n2. **Label Variation:** Distinguishing model uncertainty from valid human label disagreement. The complexity of natural language means multiple valid outputs are common (e.g., ChaosNLI shows valid disagreements in textual inference). CP prediction sets can provide \"a more faithful representation of label variation\" compared to methods that focus only on majority labels.\n\n3. **Fairness:** CP can achieve equalized coverage for different population groups (Romano et al. 2020), correcting biases without expensive retraining. Conditional guarantees (Gibbs et al. 2023) for pointwise error bounds can also contribute to fairness.\n\n4. **Data Limitations:** CP can guide active learning by selecting points with larger prediction sets for manual labeling. CP can also reduce label spaces in high-cardinality tasks and serve as a data filtering/cleaning tool for LLMs.\n\n5. **Uncertainty-Aware Evaluation:** Using conformal predictors to more reliably assess model performance, especially in the context of LLM-as-judge evaluation where confidence in evaluations is uncertain. Different non-conformity scores can be compared to evaluate uncertainty heuristics.\n\n---\n\n## 4. Techniques and Applications Summary\n\n**Core CP Techniques Covered:**\n| Category | Techniques |\n|---|---|\n| Standard | Split CP, Full CP, Cross-conformal, Jackknife+ |\n| Conditional | Mondrian CP (class-conditional guarantees) |\n| Non-exchangeable | Weighted CP (Barber et al. 2023), covariate/label shift |\n| Risk control | Conformal Risk Control, Learn-Then-Test |\n| Specialized | Density-based CP, Venn-Abers Predictors |\n\n**NLP Applications Covered:**\n| Application | Example Methods |\n|---|---|\n| Sentiment classification | BERT + split CP |\n| POS tagging | CP with 99% coverage |\n| Multilabel classification | Label powerset + CP |\n| Few-shot learning | Meta-learned non-conformity scores |\n| Machine translation | Dynamic calibration, quality estimation |\n| Text generation | Conformal nucleus sampling |\n| Speech recognition | Word error rate control |\n| Robot planning | Formal task completion guarantees |\n| Model evaluation | Equalized coverage evaluation |\n| Efficient inference | Early exiting with CP guarantees |\n\n**Key technical contribution of the survey:** Demonstrating that CP transforms standard NLP systems into uncertainty-aware systems with formal guarantees, requiring only a small calibration dataset and no model retraining. The framework is model-agnostic and distribution-free, requiring only data exchangeability (or weighted extensions for non-exchangeable settings).\n\n---\n\n## 5. Reviewer Feedback\n\n**TACL reviews are unfortunately not publicly available** for this paper. TACL uses a non-public review process (unlike venues that use OpenReview with public reviews). I searched the ACL Anthology page, MIT Press page, OpenReview, and general web -- no reviewer comments are visible anywhere. The only editorial information available is:\n\n- **Action Editor:** Roi Reichart\n- The paper was accepted and published in TACL Volume 12 (2024)\n\nThe fact that it was accepted at TACL (a highly selective journal with approximately 25-30% acceptance rate) and handled by Roi Reichart (a prominent researcher in NLP uncertainty and learning) suggests favorable reviews.\n\n---\n\n## 6. Impact and Citing Work\n\nThe paper has been generating citations since its publication. Notable related/citing work includes:\n\n- **ConU (EMNLP 2024 Findings):** \"Conformal Uncertainty in Large Language Models with Correctness Coverage Guarantees\" -- applies CP to black-box LLMs for open-ended NLG with self-consistency-based uncertainty measures\n- **\"Mitigating LLM Hallucinations via Conformal Abstention\" (2024):** Uses CP to determine when LLMs should abstain from responding, with guarantees on hallucination rate\n- **\"An Empirical Study of Conformal Prediction in LLM with ASP Scaffolds for Robust Reasoning\" (2025):** Extends CP to LLM reasoning\n- **\"Conformal Prediction: A Data Perspective\" (Zhou et al. 2024):** A broader CP survey that cites Campos et al. for its NLP coverage\n- **\"Conformal Prediction and Trustworthy AI\" (Springer, 2024):** Book chapter citing this survey\n\nThe paper appears on the EMNLP 2024 accepted TACL papers list, indicating it was presented at EMNLP 2024.\n\n---\n\n## Key Takeaway\n\nThis survey fills a clear gap as the first dedicated treatment of conformal prediction for NLP. Its primary value is the systematic organization of CP variants (standard, conditional, non-exchangeable, risk-controlling) mapped onto NLP application categories (classification, generation, evaluation, efficiency). The most significant open challenges it identifies center on the fundamental tension between CP's exchangeability requirement and the autoregressive, high-cardinality nature of language generation -- particularly the difficulty of estimating coverage gaps in non-exchangeable settings and handling combinatorially large output spaces."
      }
    ],
    "totalDurationMs": 207745,
    "totalTokens": 30046,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 666,
      "cache_read_input_tokens": 26482,
      "output_tokens": 2897,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 666
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2897,
          "cache_read_input_tokens": 26482,
          "cache_creation_input_tokens": 666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 666,
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
      "otherToolCount": 22
    }
  },
  "sourceToolAssistantUUID": "be00c54b-58e5-4a7d-aec0-05208c333f90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-30T06:41:33.884Z_

<details open><summary>🔧 Tool call — Agent · `toolu_0111VbN6u4wZygqcmZ47BLaN`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Paper 5: SCoRE selective prediction",
  "prompt": "Research the paper \"Conformal Selective Prediction with General Risk Control (SCoRE)\" by Tian Bai and Ying Jin (arXiv 2026, https://arxiv.org/abs/2603.24704).\n\n1. Use WebFetch to read the arxiv abstract page and HTML version\n2. Use WebSearch to find any reviews, discussions, or related papers\n3. Try to access the full paper content\n\nI need to understand:\n- What gap did they identify?\n- What was their key insight?\n- How did they formulate the problem?\n- What techniques did they adapt/combine (especially e-values)?\n- What were their main theoretical results?\n- Applications and experiments\n- Any reviewer feedback if available\n\nReport back all findings in detail."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f4de65a-8f33-4cf3-a6f7-49da3091299a",
  "isSidechain": false,
  "requestId": "req_011CbYJC5o8CNGrDjSvAjDVD",
  "type": "assistant",
  "uuid": "906de6ea-7850-4dd5-aa10-b135920c902f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CYZKoCf1VoSst5sECBjCKn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3275,
      "cache_read_input_tokens": 24201,
      "output_tokens": 274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3275,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 274,
          "cache_read_input_tokens": 24201,
          "cache_creation_input_tokens": 3275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3275
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

_source line 22 · 2026-05-30T06:44:18.929Z_

<details><summary>↩ Tool result · `toolu_0111VbN6u4wZygqcmZ47BLaN`</summary>

```text
I now have comprehensive information. Here is my detailed report.

---

## Detailed Research Report: "Conformal Selective Prediction with General Risk Control (SCoRE)"

**Authors:** Tian Bai (Stanford University) and Ying Jin (University of Pennsylvania, Wharton School)
**Posted:** March 25, 2026, arXiv:2603.24704
**Subject areas:** stat.ME (primary), cs.LG, stat.AP, stat.ML

---

### 1. The Gap They Identified

The authors identified a fundamental mismatch between what existing selective prediction methods can handle and what real-world AI deployment demands:

**Prior work was limited to binary risks.** Existing conformal selective prediction methods (notably Jin & Candes 2023) addressed only binary risk -- either a prediction is correct or incorrect (0/1 loss). However, many high-stakes applications demand control of *continuously-valued* risks. For example, in drug discovery the cost of pursuing an inactive compound is not binary; in clinical prediction, the error magnitude (MSE) matters, not just whether an error occurred; and for LLMs, semantic error has degrees of severity.

**Tail probability is the wrong tool for continuous risks.** The authors made the critical observation that p-values and tail probability bounds -- the standard instruments in conformal prediction -- are "not a natural instrument for quantifying and controlling the expectation of continuous risks." P-values control the probability of an event, but when risks are continuous-valued, what matters is the *expected magnitude* of the risk, which is fundamentally an expectation-based quantity.

**Reliance on uniform concentration.** Existing selective prediction methods that do handle non-binary losses typically rely on uniform concentration arguments (e.g., uniform convergence of empirical risk over threshold classes), which are restrictive, can be loose in finite samples, and do not extend gracefully to dependent data or distribution shift.

**No distinction between total vs. per-instance risk.** Prior frameworks lacked the flexibility to distinguish between controlling the *total* deployment risk across all instances versus the *average* risk *per deployed instance* -- two practically distinct objectives.

---

### 2. The Key Insight

The central insight is a conceptual bridge: **selective prediction can be recast as hypothesis testing with unknown, random weights, and e-values (rather than p-values) are the natural currency for this reformulation when risks are continuous.**

Specifically:
- For each test instance, the decision "should we trust the model?" is framed as a hypothesis test.
- The unknown continuous risk L(n+j) plays the role of an unknown, random weight in this testing problem.
- E-values -- non-negative random variables defined through an *expectation* condition -- naturally accommodate the expectation-based nature of continuous risk control, whereas p-values (defined through tail probabilities) do not.

This leads to the invention of **risk-adjusted e-values**: random variables E(n+j) satisfying E[E(n+j) * L(n+j)] <= 1, where L(n+j) is the unknown future risk. The product structure between the e-value and the risk is what makes continuous risk control possible through simple thresholding.

---

### 3. Problem Formulation

**Setup:**
- Calibration data: D_calib = {(X_i, Y_i)} for i=1..n (labeled)
- Test data: D_test = {X(n+j)} for j=1..m (unlabeled; outcomes Y(n+j) unknown)
- A pre-trained model f producing predictions
- A bounded risk function: L(n+j) = L(f, X(n+j), Y(n+j)) in [0,1]
- A score function s: X -> [0,1] estimating risk (pre-trained)
- Goal: produce binary trust decisions psi_hat(n+j) in {0,1}

**Two deployment risk metrics:**

**(a) Marginal Deployment Risk (MDR):** For a single test point,
E[L(n+1) * psi_hat(n+1)] <= alpha.
This implies Total Deployment Risk (TDR) control across m instances: E[sum_j L(n+j)*psi_hat(n+j)] <= alpha*m.

**(b) Selective Deployment Risk (SDR):** The average risk per deployed unit,
E[sum_j L(n+j)*1{j in R} / (1 v |R|)] <= alpha,
where R = {j : psi_hat(n+j) = 1} is the deployed set. This generalizes False Discovery Rate (FDR) from binary to continuous risks.

---

### 4. Techniques Adapted and Combined

**E-values from hypothesis testing literature.** E-values (Vovk & Wang 2021, and the broader safe testing literature) are non-negative random variables with expectation at most 1 under the null. The authors generalize this concept by defining "risk-adjusted e-values" where the product E*L (rather than E alone) has expectation at most 1. This is a novel generalization because L is an unknown random variable, not a fixed quantity.

**Conformal inference / exchangeability.** The validity of the e-value constructions relies on exchangeability of the data (calibration + test), the same assumption underpinning conformal prediction. No modeling assumptions about the distribution of (X,Y) are needed.

**E-BH procedure from multiple testing.** For SDR control (the FDR analog), the authors plug their risk-adjusted e-values into the e-Benjamini-Hochberg procedure, which was originally designed for standard e-values. They show it continues to provide valid SDR control with their generalized e-values.

**Conformal selection (Jin & Candes 2023).** The e-value constructions (Equations 4.1 and 5.1) draw structural inspiration from conformal selection methods but replace p-value-based thresholding with e-value-based thresholding, and replace binary risk indicators with continuous risk values in the calibration.

**Neyman-Pearson optimality theory.** The asymptotic optimality analysis (Theorem 4.6) adapts Neyman-Pearson-type reasoning to characterize the optimal score function.

---

### 5. Main Theoretical Results

**Definition 3.1 (Risk-adjusted e-value):** E(n+j) >= 0 a.s. and E[E(n+j) * L(n+j)] <= 1.

**Theorem 3.2 (MDR control):** If E(n+j) is a risk-adjusted e-value, then setting psi_hat(n+j) = 1{E(n+j) >= 1/alpha} achieves E[L(n+j) * psi_hat(n+j)] <= alpha. (A Markov-inequality-type argument on the product.)

**Theorem 3.3 (SDR control via e-BH):** Applying the e-Benjamini-Hochberg procedure to risk-adjusted e-values controls SDR at level alpha.

**Theorem 4.2 (Validity of MDR e-value construction):** Under exchangeability of {(X_i,Y_i)} for i=1..n+1, the constructed e-value (Equation 4.1) satisfies E[L(n+1) * E_gamma(n+1)] <= 1 for any fixed gamma in (0,1). This is the core finite-sample, distribution-free validity result.

**Proposition 4.4 (Computational shortcut):** For gamma <= alpha, the decision 1{E_gamma(n+1) >= 1/alpha} simplifies to checking whether the weighted empirical CDF of calibration risks at the test point's score is below gamma. This avoids explicit e-value computation or grid search over ell.

**Theorem 4.6 (Neyman-Pearson optimality):** Under i.i.d. sampling and regularity conditions:
- (i) The data-dependent threshold t_gamma(ell) converges a.s. to the population-level threshold t*.
- (ii) Setting gamma = alpha is asymptotically optimal; gamma > alpha yields zero power asymptotically.
- (iii) The asymptotically optimal score function s(x) should be monotone increasing in the risk-to-reward ratio l(x)/r(x), where l(x) = E[L|X=x] is the conditional risk and r(x) = E[reward|X=x] is the conditional reward. This characterizes exactly which instances to deploy: those with the best risk-to-reward tradeoff.

**Theorem 5.1 (Validity of SDR e-value construction):** Under exchangeability of {(X_i,Y_i)} for i=1..n+m, the SDR e-values (Equation 5.1) satisfy E[L(n+j) * E_gamma(n+j)] <= 1.

**Proposition 5.2 (Efficient SDR algorithm):** Computational complexity O((n+m)*m + (n+m)*log(n+m)), avoiding continuous search over ell.

**Section 6 (Covariate shift extension):** The framework extends to non-exchangeable data under covariate shift via importance-weighted calibration with density ratio weights w_i = p_test(X_i)/p_train(X_i). Finite-sample validity is maintained even with certain weight model misspecification.

---

### 6. Applications and Experiments

**Drug Discovery (Section 7.1):**
- Setting: Compound screening where binding affinity predictions are continuous.
- Risk: Expected cost/waste from pursuing inactive compounds (a continuous quantity, not binary).
- SCoRE controls the average cost among selected candidates while maximizing the number of deployed candidates.
- Connection to TxConformal, a framework Jin co-developed with Genentech for controlling false discoveries in AI-driven therapeutic discovery.

**Clinical / Health Risk Prediction (Section 7.2):**
- Setting: Predicting health outcomes for patients.
- Risk: Mean squared error of predictions among deployed cases.
- Demonstrated tight SDR control on MSE predictions in a semi-synthetic dataset with 50 patients per day.

**Large Language Models (Section 7.3):**
- Setting: LLM abstention on question-answering tasks.
- Risk: Semantic error (continuous measure of answer quality).
- Demonstrated that SCoRE can control when to trust LLM outputs versus abstain, with different risk definitions yielding different selection behaviors.

**Simulations (Section 8):**
- Compared SCoRE against conformal risk control baselines and selective prediction methods.
- All SCoRE procedures maintained valid risk control in finite samples.
- Methods controlling selective risk (SDR) showed superior per-instance performance.
- Power comparisons demonstrated efficiency of the e-value construction.
- Robustness under covariate shift was verified.

---

### 7. Reviewer Feedback and Community Reception

**No formal peer review is publicly available.** The paper appears to be a preprint (posted March 2026) that has not yet appeared at a venue with public reviews (ICML, NeurIPS, or OpenReview). The alphaXiv discussion page returned a 403 error, so any comments there are inaccessible.

**Seminar activity indicates strong interest:**
- Ying Jin presented this work at the **University of Illinois Statistics Seminar** on April 23, 2026.
- She also gave a **BSR Seminar at the University of Maryland** on this topic.
- Jin was a discussant at the **Selective Inference Seminar** in January 2026.

**Follow-up and related work:**
- **Xu, Guo & Wei (arXiv:2512.12844, Dec 2025):** "Selective Conformal Risk Control" -- a contemporaneous but distinct paper combining conformal prediction with selective classification via a two-stage approach (select confident samples, then apply conformal risk control). This uses a different methodology than SCoRE.
- **Khosravi & Huo (arXiv:2605.20270, May 2026):** "Conformal Selective Acting" -- extends conformal selective ideas to online/anytime-valid settings for RLVR-trained LLMs, using e-processes. This appears to be influenced by the same intellectual currents as SCoRE but targets a different (online, sequential) setting.

---

### 8. Summary of Contributions

| Aspect | What SCoRE provides |
|---|---|
| **Risk type** | Any bounded, continuous-valued risk (not just binary) |
| **Guarantees** | Two: MDR (total risk) and SDR (per-instance average risk, FDR analog) |
| **Assumptions** | Only exchangeability -- no distributional/modeling assumptions |
| **Sample regime** | Finite-sample validity (no asymptotics needed) |
| **Key tool** | Risk-adjusted e-values: E[E*L] <= 1 |
| **Optimality** | Neyman-Pearson characterization: optimal score = monotone in l(x)/r(x) |
| **Concentration** | No uniform concentration needed |
| **Shift** | Extends to covariate shift with importance weighting |
| **Computation** | Efficient closed-form decision rules avoid grid search |

The paper represents a significant conceptual advance by identifying that the right mathematical object for continuous-risk selective prediction is not a p-value but a risk-adjusted e-value, and that the exchangeability principle from conformal inference is exactly what validates these objects without distributional assumptions.

---

Sources:
- [arXiv Abstract: Conformal Selective Prediction with General Risk Control](https://arxiv.org/abs/2603.24704)
- [arXiv HTML: Full Paper](https://arxiv.org/html/2603.24704)
- [Ying Jin's Homepage](https://ying531.github.io/)
- [Statistics Seminar - Ying Jin at UIUC](https://calendars.illinois.edu/detail/7604?eventId=33545051)
- [Related: Selective Conformal Risk Control (Xu et al.)](https://arxiv.org/abs/2512.12844)
- [Related: Conformal Selective Acting (Khosravi & Huo)](https://arxiv.org/abs/2605.20270)
- [TxConformal on bioRxiv](https://www.biorxiv.org/content/10.64898/2026.04.27.721076v1.full)
- [Conformal Risk Control (Angelopoulos et al.)](https://arxiv.org/abs/2208.02814)

agentId: a1b5047d9996f3931 (use SendMessage with to: 'a1b5047d9996f3931' to continue this agent)
&lt;usage>total_tokens: 26821
tool_uses: 18
duration_ms: 165039&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "906de6ea-7850-4dd5-aa10-b135920c902f",
  "isSidechain": false,
  "promptId": "f4874006-0899-46cb-9bfb-2a8678a3e824",
  "type": "user",
  "uuid": "72e43295-bc2e-4fa5-80d5-c14af1e130ae",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Conformal Selective Prediction with General Risk Control (SCoRE)\" by Tian Bai and Ying Jin (arXiv 2026, https://arxiv.org/abs/2603.24704).\n\n1. Use WebFetch to read the arxiv abstract page and HTML version\n2. Use WebSearch to find any reviews, discussions, or related papers\n3. Try to access the full paper content\n\nI need to understand:\n- What gap did they identify?\n- What was their key insight?\n- How did they formulate the problem?\n- What techniques did they adapt/combine (especially e-values)?\n- What were their main theoretical results?\n- Applications and experiments\n- Any reviewer feedback if available\n\nReport back all findings in detail.",
    "agentId": "a1b5047d9996f3931",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is my detailed report.\n\n---\n\n## Detailed Research Report: \"Conformal Selective Prediction with General Risk Control (SCoRE)\"\n\n**Authors:** Tian Bai (Stanford University) and Ying Jin (University of Pennsylvania, Wharton School)\n**Posted:** March 25, 2026, arXiv:2603.24704\n**Subject areas:** stat.ME (primary), cs.LG, stat.AP, stat.ML\n\n---\n\n### 1. The Gap They Identified\n\nThe authors identified a fundamental mismatch between what existing selective prediction methods can handle and what real-world AI deployment demands:\n\n**Prior work was limited to binary risks.** Existing conformal selective prediction methods (notably Jin & Candes 2023) addressed only binary risk -- either a prediction is correct or incorrect (0/1 loss). However, many high-stakes applications demand control of *continuously-valued* risks. For example, in drug discovery the cost of pursuing an inactive compound is not binary; in clinical prediction, the error magnitude (MSE) matters, not just whether an error occurred; and for LLMs, semantic error has degrees of severity.\n\n**Tail probability is the wrong tool for continuous risks.** The authors made the critical observation that p-values and tail probability bounds -- the standard instruments in conformal prediction -- are \"not a natural instrument for quantifying and controlling the expectation of continuous risks.\" P-values control the probability of an event, but when risks are continuous-valued, what matters is the *expected magnitude* of the risk, which is fundamentally an expectation-based quantity.\n\n**Reliance on uniform concentration.** Existing selective prediction methods that do handle non-binary losses typically rely on uniform concentration arguments (e.g., uniform convergence of empirical risk over threshold classes), which are restrictive, can be loose in finite samples, and do not extend gracefully to dependent data or distribution shift.\n\n**No distinction between total vs. per-instance risk.** Prior frameworks lacked the flexibility to distinguish between controlling the *total* deployment risk across all instances versus the *average* risk *per deployed instance* -- two practically distinct objectives.\n\n---\n\n### 2. The Key Insight\n\nThe central insight is a conceptual bridge: **selective prediction can be recast as hypothesis testing with unknown, random weights, and e-values (rather than p-values) are the natural currency for this reformulation when risks are continuous.**\n\nSpecifically:\n- For each test instance, the decision \"should we trust the model?\" is framed as a hypothesis test.\n- The unknown continuous risk L(n+j) plays the role of an unknown, random weight in this testing problem.\n- E-values -- non-negative random variables defined through an *expectation* condition -- naturally accommodate the expectation-based nature of continuous risk control, whereas p-values (defined through tail probabilities) do not.\n\nThis leads to the invention of **risk-adjusted e-values**: random variables E(n+j) satisfying E[E(n+j) * L(n+j)] <= 1, where L(n+j) is the unknown future risk. The product structure between the e-value and the risk is what makes continuous risk control possible through simple thresholding.\n\n---\n\n### 3. Problem Formulation\n\n**Setup:**\n- Calibration data: D_calib = {(X_i, Y_i)} for i=1..n (labeled)\n- Test data: D_test = {X(n+j)} for j=1..m (unlabeled; outcomes Y(n+j) unknown)\n- A pre-trained model f producing predictions\n- A bounded risk function: L(n+j) = L(f, X(n+j), Y(n+j)) in [0,1]\n- A score function s: X -> [0,1] estimating risk (pre-trained)\n- Goal: produce binary trust decisions psi_hat(n+j) in {0,1}\n\n**Two deployment risk metrics:**\n\n**(a) Marginal Deployment Risk (MDR):** For a single test point,\nE[L(n+1) * psi_hat(n+1)] <= alpha.\nThis implies Total Deployment Risk (TDR) control across m instances: E[sum_j L(n+j)*psi_hat(n+j)] <= alpha*m.\n\n**(b) Selective Deployment Risk (SDR):** The average risk per deployed unit,\nE[sum_j L(n+j)*1{j in R} / (1 v |R|)] <= alpha,\nwhere R = {j : psi_hat(n+j) = 1} is the deployed set. This generalizes False Discovery Rate (FDR) from binary to continuous risks.\n\n---\n\n### 4. Techniques Adapted and Combined\n\n**E-values from hypothesis testing literature.** E-values (Vovk & Wang 2021, and the broader safe testing literature) are non-negative random variables with expectation at most 1 under the null. The authors generalize this concept by defining \"risk-adjusted e-values\" where the product E*L (rather than E alone) has expectation at most 1. This is a novel generalization because L is an unknown random variable, not a fixed quantity.\n\n**Conformal inference / exchangeability.** The validity of the e-value constructions relies on exchangeability of the data (calibration + test), the same assumption underpinning conformal prediction. No modeling assumptions about the distribution of (X,Y) are needed.\n\n**E-BH procedure from multiple testing.** For SDR control (the FDR analog), the authors plug their risk-adjusted e-values into the e-Benjamini-Hochberg procedure, which was originally designed for standard e-values. They show it continues to provide valid SDR control with their generalized e-values.\n\n**Conformal selection (Jin & Candes 2023).** The e-value constructions (Equations 4.1 and 5.1) draw structural inspiration from conformal selection methods but replace p-value-based thresholding with e-value-based thresholding, and replace binary risk indicators with continuous risk values in the calibration.\n\n**Neyman-Pearson optimality theory.** The asymptotic optimality analysis (Theorem 4.6) adapts Neyman-Pearson-type reasoning to characterize the optimal score function.\n\n---\n\n### 5. Main Theoretical Results\n\n**Definition 3.1 (Risk-adjusted e-value):** E(n+j) >= 0 a.s. and E[E(n+j) * L(n+j)] <= 1.\n\n**Theorem 3.2 (MDR control):** If E(n+j) is a risk-adjusted e-value, then setting psi_hat(n+j) = 1{E(n+j) >= 1/alpha} achieves E[L(n+j) * psi_hat(n+j)] <= alpha. (A Markov-inequality-type argument on the product.)\n\n**Theorem 3.3 (SDR control via e-BH):** Applying the e-Benjamini-Hochberg procedure to risk-adjusted e-values controls SDR at level alpha.\n\n**Theorem 4.2 (Validity of MDR e-value construction):** Under exchangeability of {(X_i,Y_i)} for i=1..n+1, the constructed e-value (Equation 4.1) satisfies E[L(n+1) * E_gamma(n+1)] <= 1 for any fixed gamma in (0,1). This is the core finite-sample, distribution-free validity result.\n\n**Proposition 4.4 (Computational shortcut):** For gamma <= alpha, the decision 1{E_gamma(n+1) >= 1/alpha} simplifies to checking whether the weighted empirical CDF of calibration risks at the test point's score is below gamma. This avoids explicit e-value computation or grid search over ell.\n\n**Theorem 4.6 (Neyman-Pearson optimality):** Under i.i.d. sampling and regularity conditions:\n- (i) The data-dependent threshold t_gamma(ell) converges a.s. to the population-level threshold t*.\n- (ii) Setting gamma = alpha is asymptotically optimal; gamma > alpha yields zero power asymptotically.\n- (iii) The asymptotically optimal score function s(x) should be monotone increasing in the risk-to-reward ratio l(x)/r(x), where l(x) = E[L|X=x] is the conditional risk and r(x) = E[reward|X=x] is the conditional reward. This characterizes exactly which instances to deploy: those with the best risk-to-reward tradeoff.\n\n**Theorem 5.1 (Validity of SDR e-value construction):** Under exchangeability of {(X_i,Y_i)} for i=1..n+m, the SDR e-values (Equation 5.1) satisfy E[L(n+j) * E_gamma(n+j)] <= 1.\n\n**Proposition 5.2 (Efficient SDR algorithm):** Computational complexity O((n+m)*m + (n+m)*log(n+m)), avoiding continuous search over ell.\n\n**Section 6 (Covariate shift extension):** The framework extends to non-exchangeable data under covariate shift via importance-weighted calibration with density ratio weights w_i = p_test(X_i)/p_train(X_i). Finite-sample validity is maintained even with certain weight model misspecification.\n\n---\n\n### 6. Applications and Experiments\n\n**Drug Discovery (Section 7.1):**\n- Setting: Compound screening where binding affinity predictions are continuous.\n- Risk: Expected cost/waste from pursuing inactive compounds (a continuous quantity, not binary).\n- SCoRE controls the average cost among selected candidates while maximizing the number of deployed candidates.\n- Connection to TxConformal, a framework Jin co-developed with Genentech for controlling false discoveries in AI-driven therapeutic discovery.\n\n**Clinical / Health Risk Prediction (Section 7.2):**\n- Setting: Predicting health outcomes for patients.\n- Risk: Mean squared error of predictions among deployed cases.\n- Demonstrated tight SDR control on MSE predictions in a semi-synthetic dataset with 50 patients per day.\n\n**Large Language Models (Section 7.3):**\n- Setting: LLM abstention on question-answering tasks.\n- Risk: Semantic error (continuous measure of answer quality).\n- Demonstrated that SCoRE can control when to trust LLM outputs versus abstain, with different risk definitions yielding different selection behaviors.\n\n**Simulations (Section 8):**\n- Compared SCoRE against conformal risk control baselines and selective prediction methods.\n- All SCoRE procedures maintained valid risk control in finite samples.\n- Methods controlling selective risk (SDR) showed superior per-instance performance.\n- Power comparisons demonstrated efficiency of the e-value construction.\n- Robustness under covariate shift was verified.\n\n---\n\n### 7. Reviewer Feedback and Community Reception\n\n**No formal peer review is publicly available.** The paper appears to be a preprint (posted March 2026) that has not yet appeared at a venue with public reviews (ICML, NeurIPS, or OpenReview). The alphaXiv discussion page returned a 403 error, so any comments there are inaccessible.\n\n**Seminar activity indicates strong interest:**\n- Ying Jin presented this work at the **University of Illinois Statistics Seminar** on April 23, 2026.\n- She also gave a **BSR Seminar at the University of Maryland** on this topic.\n- Jin was a discussant at the **Selective Inference Seminar** in January 2026.\n\n**Follow-up and related work:**\n- **Xu, Guo & Wei (arXiv:2512.12844, Dec 2025):** \"Selective Conformal Risk Control\" -- a contemporaneous but distinct paper combining conformal prediction with selective classification via a two-stage approach (select confident samples, then apply conformal risk control). This uses a different methodology than SCoRE.\n- **Khosravi & Huo (arXiv:2605.20270, May 2026):** \"Conformal Selective Acting\" -- extends conformal selective ideas to online/anytime-valid settings for RLVR-trained LLMs, using e-processes. This appears to be influenced by the same intellectual currents as SCoRE but targets a different (online, sequential) setting.\n\n---\n\n### 8. Summary of Contributions\n\n| Aspect | What SCoRE provides |\n|---|---|\n| **Risk type** | Any bounded, continuous-valued risk (not just binary) |\n| **Guarantees** | Two: MDR (total risk) and SDR (per-instance average risk, FDR analog) |\n| **Assumptions** | Only exchangeability -- no distributional/modeling assumptions |\n| **Sample regime** | Finite-sample validity (no asymptotics needed) |\n| **Key tool** | Risk-adjusted e-values: E[E*L] <= 1 |\n| **Optimality** | Neyman-Pearson characterization: optimal score = monotone in l(x)/r(x) |\n| **Concentration** | No uniform concentration needed |\n| **Shift** | Extends to covariate shift with importance weighting |\n| **Computation** | Efficient closed-form decision rules avoid grid search |\n\nThe paper represents a significant conceptual advance by identifying that the right mathematical object for continuous-risk selective prediction is not a p-value but a risk-adjusted e-value, and that the exchangeability principle from conformal inference is exactly what validates these objects without distributional assumptions.\n\n---\n\nSources:\n- [arXiv Abstract: Conformal Selective Prediction with General Risk Control](https://arxiv.org/abs/2603.24704)\n- [arXiv HTML: Full Paper](https://arxiv.org/html/2603.24704)\n- [Ying Jin's Homepage](https://ying531.github.io/)\n- [Statistics Seminar - Ying Jin at UIUC](https://calendars.illinois.edu/detail/7604?eventId=33545051)\n- [Related: Selective Conformal Risk Control (Xu et al.)](https://arxiv.org/abs/2512.12844)\n- [Related: Conformal Selective Acting (Khosravi & Huo)](https://arxiv.org/abs/2605.20270)\n- [TxConformal on bioRxiv](https://www.biorxiv.org/content/10.64898/2026.04.27.721076v1.full)\n- [Conformal Risk Control (Angelopoulos et al.)](https://arxiv.org/abs/2208.02814)"
      }
    ],
    "totalDurationMs": 165039,
    "totalTokens": 26821,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 525,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 21709,
      "output_tokens": 3517,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1070
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 525,
          "output_tokens": 3517,
          "cache_read_input_tokens": 21709,
          "cache_creation_input_tokens": 1070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1070,
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
  "sourceToolAssistantUUID": "906de6ea-7850-4dd5-aa10-b135920c902f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
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
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "72e43295-bc2e-4fa5-80d5-c14af1e130ae",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze conformal prediction papers for poisoning-robust RAG",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---

### Assistant

_source line 25 · 2026-05-30T06:44:29.990Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have detailed research on all 5 papers. Let me compile the analysis into the required JSON format, keeping each paper's analysis under 2000 characters.

Let me carefully craft each analysis:

1. **Language Models with Conformal Factuality Guarantees** (Mohri & Hashimoto, ICML 2024)
2. **Is Conformal Factuality for RAG-based LLMs Robust?** (Chen et al., arXiv 2026)
3. **Conformal Prediction as Bayesian Quadrature** (Snell & Griffiths, ICML 2025)


4. **Conformal Prediction for NLP: A Survey** (Campos et al., TACL 2024)
5. **SCoRE** (Bai & Jin, arXiv 2026)

Now I'll structure this as a JSON array with all five papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72e43295-bc2e-4fa5-80d5-c14af1e130ae",
  "isSidechain": false,
  "requestId": "req_011CbYJQpYTrFX6LjHUTnhwB",
  "type": "assistant",
  "uuid": "d777a6e4-8c46-4350-94fd-165740032f36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2xx52jdLtmGGQobWXvyLT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3870,
      "cache_read_input_tokens": 27476,
      "output_tokens": 2877,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2877,
          "cache_read_input_tokens": 27476,
          "cache_creation_input_tokens": 3870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3870
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

_source line 26 · 2026-05-30T06:45:34.350Z_

Now I have comprehensive research on all 5 papers. Let me compile the analysis into the required JSON format.

```json
[
  {
    "title": "Language Models with Conformal Factuality Guarantees",
    "venue": "ICML 2024",
    "problem_identification": "No existing method provided formal statistical guarantees on open-ended LLM factuality — prior CP work for LMs was limited to token-level sets or multiple-choice reductions, none producing interpretable single outputs with coverage certificates.",
    "key_insight": "LLM factuality maps to uncertainty quantification via entailment sets: output y is correct iff the ground truth y* lies in E(y) = {y' : y' ⊨ y}, so conformal coverage over entailment sets directly translates to factuality guarantees through a back-off algorithm that progressively removes sub-claims.",
    "innovation_type": "new_formulation",
    "method_summary": "Decomposes LLM outputs into atomic sub-claims, scores each (via frequency/confidence), and applies split CP with a nested back-off function F_t that removes low-scoring claims to expand entailment sets. The calibration quantile q̂_α determines how many claims to retain. An entailment decomposability assumption (Assumption 5.1) ensures claim-level filtering preserves coverage. Achieves ~80% factuality on FActScore (up from 25%) while retaining ~50% of claims.",
    "limitations_and_open_questions": "Guarantees are marginal (averaged over calibration draws), not conditional per-input — follow-up work showed under-coverage for underrepresented topics and near-complete censorship at high factuality levels. Claims are evaluated independently, ignoring logical dependencies.",
    "building_blocks": ["Entailment-set formulation of factuality as CP coverage", "Sub-claim decomposition + scoring + filtering pipeline", "Back-off algorithm framework for nested conformal sets", "Frequency scoring as nonconformity measure"],
    "relevance_to_seed": "Foundational paradigm our work extends — we must handle the case where retrieved documents (which ground the entailment sets) are adversarially poisoned, invalidating the exchangeability assumption this method relies on."
  },
  {
    "title": "Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights",
    "venue": "arXiv 2026",
    "problem_identification": "No prior work systematically studied whether conformal factuality guarantees survive when combined with RAG — existing metrics (empirical factuality) masked failures by treating empty outputs as trivially factual, hiding a critical factuality-informativeness tradeoff.",
    "key_insight": "Standard conformal factuality for RAG produces vacuous outputs at high confidence levels and its guarantees break under distribution shift and distractor injection — the problem is diagnosed but unsolved, creating a clear gap for robust alternatives.",
    "innovation_type": "analysis",
    "method_summary": "Introduces three metrics — Non-Empty Rate, Non-Vacuous Empirical Factuality, and Sufficient Correctness — that jointly capture both correctness and informativeness. Systematically evaluates the conformal factuality pipeline across FActScore/MATH/NQ, testing robustness to calibration-test domain mismatch and distractor documents in retrieval. Shows lightweight NLI-based entailment verifiers match LLM-based scorers at 100× fewer FLOPs.",
    "limitations_and_open_questions": "Purely diagnostic — proposes no solution to the robustness failures identified. Does not consider adversarial/poisoning attacks (only natural distribution shift and distractors). The sufficient correctness metric lacks formal definition tied to conformal guarantees.",
    "building_blocks": ["Non-Empty Rate and Non-Vacuous Factuality metrics", "Empirical evidence that CP guarantees break under RAG distribution shift", "Finding that lightweight NLI verifiers are competitive scorers", "Systematic failure mode taxonomy for conformal RAG pipelines"],
    "relevance_to_seed": "Directly motivates our work — demonstrates the problem (CP breaks under RAG distribution shift) without providing a solution; our retrieval-aware score function and poisoning-robust abstention framework addresses exactly this diagnosed gap."
  },
  {
    "title": "Conformal Prediction as Bayesian Quadrature",
    "venue": "ICML 2025 (Outstanding Paper Award)",
    "problem_identification": "Standard CP provides marginal guarantees averaged over hypothetical calibration sets, but practitioners need data-conditional guarantees for their specific observed data — CRC violated its target risk in 21% (synthetic) to 45% (MS-COCO) of trials despite valid average guarantees.",
    "key_insight": "Bounding expected loss equals integrating the quantile function over [0,1], a Bayesian quadrature problem where the distribution-free Dirichlet property of quantile spacings provides the prior over evaluation sites without any distributional assumptions.",
    "innovation_type": "new_formulation",
    "method_summary": "Constructs a stochastic upper bound L⁺ = Σ Uᵢ·l₍ᵢ₎ where Uᵢ ~ Dir(1,...,1) are quantile spacings and l₍ᵢ₎ are ordered calibration losses. L⁺ stochastically dominates the posterior risk under any prior (Theorem 4.5), yielding a full posterior distribution over a provable loss upper bound. Recovers CRC as using only E[L⁺], explaining why CRC is loose — it discards all distributional information. Reduces violation rates from 45% to 5.4% on MS-COCO.",
    "limitations_and_open_questions": "Provides data-conditional (conditioned on calibration losses) not input-conditional guarantees — still averages over test inputs. Computational cost of sampling from the Dirichlet posterior for large calibration sets not fully characterized. Extension to non-exchangeable settings unexplored.",
    "building_blocks": ["Data-conditional CP guarantees via Bayesian quadrature", "L⁺ stochastic dominance bound as a richer alternative to CRC's point estimate", "Dirichlet quantile spacing property for distribution-free Bayesian inference", "Unification showing SCP and CRC as special cases"],
    "relevance_to_seed": "Offers a strictly stronger CP framework we could adopt — replacing CRC-style point thresholds with full posterior bounds over risk could yield tighter abstention decisions; the data-conditional guarantees are especially valuable when calibration sets are small or heterogeneous."
  },
  {
    "title": "Conformal Prediction for Natural Language Processing: A Survey",
    "venue": "TACL 2024",
    "problem_identification": "No prior survey bridged conformal prediction theory to NLP applications — general CP surveys existed and NLP uncertainty surveys existed, but neither systematically mapped CP variants (Mondrian, non-exchangeable, risk-controlling) onto NLP task categories.",
    "key_insight": "CP's model-agnostic, distribution-free guarantees requiring only exchangeability and a small calibration set make it uniquely suited to NLP's black-box LLM era — but the autoregressive, high-cardinality nature of language generation creates fundamental tensions with CP's assumptions.",
    "innovation_type": "new_benchmark",
    "method_summary": "Organizes CP for NLP along two axes: CP variants (split, full, cross-conformal, Mondrian, weighted/non-exchangeable, conformal risk control, density-based, Venn-Abers) and NLP applications (classification/tagging, generation at sentence/token level, uncertainty-based evaluation, efficient inference). Identifies that non-exchangeability bounds require estimating TV distance between unknown distributions, a key open problem for autoregressive generation.",
    "limitations_and_open_questions": "Published mid-2024, so misses the conformal factuality line (Mohri & Hashimoto), RAG-specific CP work, and poisoning-robust CP developments. Does not cover adversarial robustness of CP guarantees at all. Token-level CP for autoregressive generation remains an open problem.",
    "building_blocks": ["Taxonomy of CP variants applicable to NLP", "Identification of exchangeability violations in autoregressive generation", "Catalog of nonconformity score designs for text", "Open challenge list including fairness, label variation, and conditional coverage"],
    "relevance_to_seed": "Essential positioning reference — our work sits at the intersection of several categories (generation-level CP, non-exchangeable extensions, risk control) and addresses the survey's identified open challenge of CP under distribution shift, specifically adversarial shift from corpus poisoning."
  },
  {
    "title": "Conformal Selective Prediction with General Risk Control (SCoRE)",
    "venue": "arXiv 2026",
    "problem_identification": "Existing conformal selective prediction handled only binary risk (correct/incorrect), but high-stakes deployments require controlling continuous-valued risks (MSE, semantic error magnitude) — p-values are the wrong instrument for expectation-based continuous risk control.",
    "key_insight": "Selective prediction under continuous risk is hypothesis testing with unknown random weights, and risk-adjusted e-values (satisfying E[E·L] ≤ 1 rather than E[E] ≤ 1) are the natural currency — they accommodate expectation-based risk control through simple Markov-inequality thresholding.",
    "innovation_type": "new_technique",
    "method_summary": "Defines risk-adjusted e-values where the product E(n+j)·L(n+j) has expectation ≤ 1 under exchangeability. Thresholding at 1/α controls Marginal Deployment Risk; plugging into e-BH controls Selective Deployment Risk (continuous FDR analog). Proves Neyman-Pearson optimality: the optimal score is monotone in l(x)/r(x) (conditional risk-to-reward ratio). Extends to covariate shift via importance weighting. Demonstrated on drug discovery, clinical prediction, and LLM abstention.",
    "limitations_and_open_questions": "Requires bounded loss in [0,1] — unbounded risks need truncation or alternative constructions. The covariate shift extension requires density ratio estimation, which is hard in high dimensions. Power analysis under finite samples and comparison to concentration-based alternatives not fully explored.",
    "building_blocks": ["Risk-adjusted e-values for continuous risk control", "MDR and SDR as two distinct deployment risk objectives", "E-BH procedure for selective deployment with FDR-analog guarantees", "Finite-sample, distribution-free trust/abstain decisions under exchangeability"],
    "relevance_to_seed": "Directly applicable to our abstention mechanism — SCoRE's e-value framework could replace or complement our conformal abstention layer, providing trust/abstain decisions with continuous risk control (e.g., semantic error magnitude) rather than binary correctness, and its covariate shift extension addresses part of the distribution shift from poisoning."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d777a6e4-8c46-4350-94fd-165740032f36",
  "isSidechain": false,
  "requestId": "req_011CbYJQpYTrFX6LjHUTnhwB",
  "type": "assistant",
  "uuid": "050cf72e-6b05-4456-9de0-9d3fcabc6b28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2xx52jdLtmGGQobWXvyLT",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3870,
      "cache_read_input_tokens": 27476,
      "output_tokens": 2877,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3870,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2877,
          "cache_read_input_tokens": 27476,
          "cache_creation_input_tokens": 3870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3870
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
  "leafUuid": "050cf72e-6b05-4456-9de0-9d3fcabc6b28",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze conformal prediction papers for poisoning-robust RAG",
  "sessionId": "4b88536a-9d82-410d-a6db-a241b9b697ad"
}
```

---
