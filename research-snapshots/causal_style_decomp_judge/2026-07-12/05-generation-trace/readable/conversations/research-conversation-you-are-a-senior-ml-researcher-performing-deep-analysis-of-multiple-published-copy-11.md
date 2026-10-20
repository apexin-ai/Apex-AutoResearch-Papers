# Research conversation: You are a senior ML researcher performing deep analysis of multiple published papers. **Today's date: 2026-05-30 (UTC).*

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/8ee4913b-30ba-4fac-800b-6164c595a9ea.jsonl`
- **Structured JSON:** [`8a47934e87b4b72b09d7.json`](../../sessions/8a/8a47934e87b4b72b09d7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:24:48.710Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:24:48.710Z",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "content": "You are a senior ML researcher performing deep analysis of multiple published papers.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: Safe, Robust and Responsible AI (SRRAI)\n\nDirection: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.\n\nSeed Papers:\n- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval\n- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG\n- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative\n- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on\n- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition\n\nKnown Gaps:\n- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)\n- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails\n- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis\n\nTheoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must compare against RobustRAG and ReliabilityRAG baselines\n- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols\n- AAAI 2026 submission deadline: August 2026\n\nQuality Self-Checks:\n- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.\n- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.\n- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.\n- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.\n\nAvoid:\n- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this\n- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead\n- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates**\n\n## Your task (Batch 3)\n\nAnalyze the following 5 papers. For EACH paper:\n1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.\n2. If on OpenReview, also read reviewer comments.\n3. Write a concise analysis focusing on HOW the paper innovates.\n\n## Papers to analyze\n\n[\n  {\n    \"title\": \"Mitigating LLM Hallucinations via Conformal Abstention\",\n    \"authors\": \"Yasin Abbasi-Yadkori, Ilja Kuzborskij, David Stutz, Andras Gyorgy, Adam Fisch, Arnaud Doucet, Iuliya Beloshapka, Wei-Hung Weng, Yao-Yuan Yang, Csaba Szepesvari, Ali Taylan Cemgil, Nenad Tomasev\",\n    \"venue\": \"NeurIPS 2024\",\n    \"url\": \"https://arxiv.org/abs/2405.01563\",\n    \"why_important\": \"Foundational work from Google DeepMind on conformal abstention for LLMs; uses self-consistency-based similarity scoring with CP to bound hallucination rates. Directly establishes the conformal abstention paradigm the proposed work extends to adversarial settings.\",\n    \"one_line_summary\": \"Uses self-consistency-based nonconformity scores with conformal prediction to provide distribution-free statistical upper bounds on LLM hallucination rates, determining when to abstain from answering.\"\n  },\n  {\n    \"title\": \"Robust Yet Efficient Conformal Prediction Sets\",\n    \"authors\": \"Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski\",\n    \"venue\": \"ICML 2024\",\n    \"url\": \"https://arxiv.org/abs/2407.09165\",\n    \"why_important\": \"Derives provably robust CP sets by bounding worst-case conformity score changes under adversarial perturbation, producing tighter sets than prior robust CP. Addresses the efficiency problem that makes naive robust CP impractical.\",\n    \"one_line_summary\": \"Provides provably robust conformal prediction sets that handle both evasion and poisoning attacks while maintaining tight (non-vacuous) set sizes through worst-case score bounding.\"\n  },\n  {\n    \"title\": \"Towards Poisoning Robustness Certification for Natural Language Generation\",\n    \"authors\": \"Mihnea Ghitu, Matthew Wicker\",\n    \"venue\": \"arXiv 2026\",\n    \"url\": \"https://arxiv.org/abs/2602.09757\",\n    \"why_important\": \"Closest existing work to the proposed direction: introduces Targeted Partition Aggregation (TPA) to certify NLG validity against poisoning attacks. Extends certified robustness ideas from RobustRAG to the generation pipeline, but does not use conformal prediction — leaving the gap the proposed work fills.\",\n    \"one_line_summary\": \"Proposes the first algorithm to certify that LLM generation outputs remain valid under bounded data poisoning, computing minimum poisoning budgets needed to induce harmful outputs.\"\n  },\n  {\n    \"title\": \"Understanding Data Poisoning Attacks for RAG: Insights and Algorithms\",\n    \"authors\": \"Xun Xian, Tong Wang, Liwen You, Yanjun Qi\",\n    \"venue\": \"ICLR 2025\",\n    \"url\": \"https://openreview.net/forum?id=2aL6gcFX7q\",\n    \"why_important\": \"Provides theoretical understanding of why RAG poisoning works (attacks exploit low-variance directions of clean data distribution); proposes the DRS defense and a stealthier regularized attack. ICLR 2025 paper directly analyzing the poisoning mechanism the proposed work must defend against.\",\n    \"one_line_summary\": \"Shows RAG poisoning attacks succeed by exploiting low-variance directions in the clean data distribution, and proposes Directional Relative Shift (DRS) detection as a principled defense.\"\n  },\n  {\n    \"title\": \"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search\",\n    \"authors\": \"Matan Ben-Tov, Mahmood Sharif\",\n    \"venue\": \"ACM CCS 2025\",\n    \"url\": \"https://arxiv.org/abs/2412.20953\",\n    \"why_important\": \"Published at a top security venue; demonstrates that dense retrieval is catastrophically vulnerable even at 0.0001% corpus poisoning. Shows that even minimal adversarial insertion fundamentally disrupts retrieval — supporting the argument that retrieval-level defenses alone are insufficient and abstention mechanisms are needed.\",\n    \"one_line_summary\": \"Generates adversarial passages without model or corpus knowledge that achieve high rankings in dense retrieval; single-query attacks are 100% successful and standard defenses fail against adaptive versions.\"\n  }\n]\n\n## Analysis requirements\n\nFor each paper, analyze:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- If reviewer comments are available: what was praised, what was criticized?\n\n## CRITICAL: Length constraint\n\n**Each paper's analysis MUST be under 2000 characters.** Be concise and analytical — no filler, no generic praise, no redundant descriptions. Every sentence must carry information.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem? How found? (1-2 sentences)\",\n  \"key_insight\": \"Core intellectual contribution (1 sentence)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach (2-3 sentences)\",\n  \"limitations_and_open_questions\": \"Gaps + follow-up questions (1-2 sentences)\",\n  \"building_blocks\": [\"Reusable methods/tools/datasets\"],\n  \"relevance_to_seed\": \"Relation to our research area (1 sentence)\"\n}\n\nYou MUST output exactly 5 analyses in the JSON array. IMPORTANT: End your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:24:48.730Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:24:48.730Z",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-30T06:24:48.980Z_

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
    "title": "Mitigating LLM Hallucinations via Conformal Abstention",
    "authors": "Yasin Abbasi-Yadkori, Ilja Kuzborskij, David Stutz, Andras Gyorgy, Adam Fisch, Arnaud Doucet, Iuliya Beloshapka, Wei-Hung Weng, Yao-Yuan Yang, Csaba Szepesvari, Ali Taylan Cemgil, Nenad Tomasev",
    "venue": "NeurIPS 2024",
    "url": "https://arxiv.org/abs/2405.01563",
    "why_important": "Foundational work from Google DeepMind on conformal abstention for LLMs; uses self-consistency-based similarity scoring with CP to bound hallucination rates. Directly establishes the conformal abstention paradigm the proposed work extends to adversarial settings.",
    "one_line_summary": "Uses self-consistency-based nonconformity scores with conformal prediction to provide distribution-free statistical upper bounds on LLM hallucination rates, determining when to abstain from answering."
  },
  {
    "title": "Robust Yet Efficient Conformal Prediction Sets",
    "authors": "Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski",
    "venue": "ICML 2024",
    "url": "https://arxiv.org/abs/2407.09165",
    "why_important": "Derives provably robust CP sets by bounding worst-case conformity score changes under adversarial perturbation, producing tighter sets than prior robust CP. Addresses the efficiency problem that makes naive robust CP impractical.",
    "one_line_summary": "Provides provably robust conformal prediction sets that handle both evasion and poisoning attacks while maintaining tight (non-vacuous) set sizes through worst-case score bounding."
  },
  {
    "title": "Towards Poisoning Robustness Certification for Natural Language Generation",
    "authors": "Mihnea Ghitu, Matthew Wicker",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2602.09757",
    "why_important": "Closest existing work to the proposed direction: introduces Targeted Partition Aggregation (TPA) to certify NLG validity against poisoning attacks. Extends certified robustness ideas from RobustRAG to the generation pipeline, but does not use conformal prediction — leaving the gap the proposed work fills.",
    "one_line_summary": "Proposes the first algorithm to certify that LLM generation outputs remain valid under bounded data poisoning, computing minimum poisoning budgets needed to induce harmful outputs."
  },
  {
    "title": "Understanding Data Poisoning Attacks for RAG: Insights and Algorithms",
    "authors": "Xun Xian, Tong Wang, Liwen You, Yanjun Qi",
    "venue": "ICLR 2025",
    "url": "https://openreview.net/forum?id=2aL6gcFX7q",
    "why_important": "Provides theoretical understanding of why RAG poisoning works (attacks exploit low-variance directions of clean data distribution); proposes the DRS defense and a stealthier regularized attack. ICLR 2025 paper directly analyzing the poisoning mechanism the proposed work must defend against.",
    "one_line_summary": "Shows RAG poisoning attacks succeed by exploiting low-variance directions in the clean data distribution, and proposes Directional Relative Shift (DRS) detection as a principled defense."
  },
  {
    "title": "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search",
    "authors": "Matan Ben-Tov, Mahmood Sharif",
    "venue": "ACM CCS 2025",
    "url": "https://arxiv.org/abs/2412.20953",
    "why_important": "Published at a top security venue; demonstrates that dense retrieval is catastrophically vulnerable even at 0.0001% corpus poisoning. Shows that even minimal adversarial insertion fundamentally disrupts retrieval — supporting the argument that retrieval-level defenses alone are insufficient and abstention mechanisms are needed.",
    "one_line_summary": "Generates adversarial passages without model or corpus knowledge that achieve high rankings in dense retrieval; single-query attacks are 100% successful and standard defenses fail against adaptive versions."
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
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "type": "user",
  "uuid": "72ecb91f-4f5f-4853-b1f8-eac8491cc014",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:24:48.969Z_

```json
{
  "parentUuid": "72ecb91f-4f5f-4853-b1f8-eac8491cc014",
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
  "uuid": "4dfa233a-8819-4a5c-91bf-3a0a947669d9",
  "timestamp": "2026-05-30T06:24:48.969Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:24:48.970Z_

```json
{
  "parentUuid": "4dfa233a-8819-4a5c-91bf-3a0a947669d9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "912ac0ec-4fc4-4d44-a87b-232a0d424693",
  "timestamp": "2026-05-30T06:24:48.970Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
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
  "aiTitle": "Analyze conformal prediction for adversarial RAG systems",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Assistant

_source line 7 · 2026-05-30T06:24:51.469Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze each of the 5 papers systematically. I'll search for and read each paper's content, then compile the analysis.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "912ac0ec-4fc4-4d44-a87b-232a0d424693",
  "isSidechain": false,
  "requestId": "req_011CbYGvav1w4eJMghhdu7pA",
  "type": "assistant",
  "uuid": "d2b6cd65-9992-43e8-be4e-73344b3c13c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZ7dQpELkesez3yQD5oof2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4084,
      "cache_read_input_tokens": 11014,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4084,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 379,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4084
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

_source line 8 · 2026-05-30T06:24:52.537Z_

I'll research all 5 papers in parallel to gather their abstracts, methods, and any reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2b6cd65-9992-43e8-be4e-73344b3c13c6",
  "isSidechain": false,
  "requestId": "req_011CbYGvav1w4eJMghhdu7pA",
  "type": "assistant",
  "uuid": "1ee6e9cf-38ef-47f7-b050-d5c62cdac458",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZ7dQpELkesez3yQD5oof2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4084,
      "cache_read_input_tokens": 11014,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4084,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 379,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4084
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

_source line 9 · 2026-05-30T06:24:58.981Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01K2W6rF743CQYtyb4hGjBES`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze paper 1: Conformal Abstention",
  "prompt": "Research the paper \"Mitigating LLM Hallucinations via Conformal Abstention\" by Yasin Abbasi-Yadkori et al. (NeurIPS 2024). URL: https://arxiv.org/abs/2405.01563\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full PDF or HTML version if available\n3. Search for any OpenReview or NeurIPS reviewer comments\n4. Search the web for discussions or reviews of this paper\n\nReport back with:\n- The full abstract\n- Key method details (how they define nonconformity scores, how they use conformal prediction for abstention, what self-consistency scoring means in their context)\n- The theoretical guarantees they provide\n- Any reviewer feedback found\n- Limitations acknowledged by the authors\n\nBe thorough — I need enough detail to write a precise technical analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee6e9cf-38ef-47f7-b050-d5c62cdac458",
  "isSidechain": false,
  "requestId": "req_011CbYGvav1w4eJMghhdu7pA",
  "type": "assistant",
  "uuid": "f05d748c-954a-41fc-b42b-17b708647805",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HZ7dQpELkesez3yQD5oof2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4084,
      "cache_read_input_tokens": 11014,
      "output_tokens": 379,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4084,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 379,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4084
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

_source line 10 · 2026-05-30T06:28:42.946Z_

<details><summary>↩ Tool result · `toolu_01K2W6rF743CQYtyb4hGjBES`</summary>

```text
I now have comprehensive information to provide a thorough report. Here is my findings:

---

## Research Report: "Mitigating LLM Hallucinations via Conformal Abstention"

**Authors:** Yasin Abbasi-Yadkori, Ilja Kuzborskij, David Stutz, Andras Gyorgy, Adam Fisch, Arnaud Doucet, Iuliya Beloshapka, Wei-Hung Weng, Yao-Yuan Yang, Csaba Szepesvari, Ali Taylan Cemgil, Nenad Tomasev (Google DeepMind)

**Venue:** NeurIPS 2024 -- Workshop on Statistical Frontiers in LLMs and Foundation Models (Poster, Submission ID 94176). Also available on OpenReview under IDs `E7Cr9uNSNU` and `vlo4JF27Xx`.

**arXiv:** 2405.01563 (submitted April 4, 2024; published May 6, 2024)

---

### Full Abstract

"We develop a principled procedure for determining when a large language model (LLM) should abstain from responding (e.g., by saying 'I don't know') in a general domain, instead of resorting to possibly 'hallucinating' a non-sensical or incorrect answer." The approach builds on self-consistency as a reliable measure of model confidence, proposing that the LLM itself self-evaluate the similarity between each of its sampled responses for a given query, and then leverages conformal prediction techniques to develop an abstention procedure with rigorous theoretical guarantees on the hallucination rate (error rate). The method is lightweight, based only on prompting (no fine-tuning required). It was evaluated on closed-book, open-domain generative question answering tasks using Gemini Pro, and reliably bounds the hallucination rate while maintaining significantly less conservative abstention rates than baselines using log-probability scores, especially on datasets with long responses.

---

### Key Method Details

#### Problem Formulation

The framework is cast as **selective classification**: given a query X, the system either produces a response f(X) or abstains. The components are:

- **Match function** m(X; Y', Y) in {0,1}: Determines if two responses are semantically equivalent given query X
- **Classifier** f: X -> Y: Maps queries to responses
- **Score function** g(X): Quantifies model confidence
- **Loss function**: l(X,Y; lambda) = (1 - a_lambda(X))(1 - m(X; f(X), Y)), penalizing incorrect non-abstention
- **Abstention policy**: a_lambda(X) = 1 if g(X) < lambda, else 0

The optimization minimizes abstention rate T(lambda) subject to risk constraint R(lambda) <= alpha.

#### Nonconformity Scores / Score Functions

Three scoring mechanisms are proposed:

1. **Match Count (MC):** For each sampled response Y^i, count how many of k other sampled responses are similar: g(Y^i) = |{j != i : s(X; Y^i, Y^j) > beta}|. The similarity function s: X x Y x Y -> R is implemented via LLM prompting, where the LLM is asked to compare two texts given the original query. The paper emphasizes that "the self-evaluation prompt depends on the query itself, making it explicit that similarity of two responses depends on the question." This requires O(k^2) LLM calls for pairwise comparison.

2. **Expected Match Count (EMC):** Instead of pairwise comparison, the LLM is asked in a single query how many of the alternative responses match a reference response. Using the log-probabilities over token outputs, the expected count is computed as: g(X) = sum_{i=1}^{k} q("i"|X) * i, where q represents the LLM's token probability for numeric responses indicating match counts. This reduces computational cost substantially.

3. **Log-Probability (LP) Baseline:** Uses the greedy response's normalized or unnormalized token-level log-probability as a confidence score. The paper demonstrates this degrades substantially for longer responses because "these probabilities heavily depend on the length of the output sequence, and the likelihood of an answer becomes non-indicative of its correctness as the sequence length grows."

#### Self-Consistency Scoring in Context

"Self-consistency" here means: sample k responses from the LLM for the same query, then measure how much these responses agree with each other. High agreement (many responses matching) indicates the model is confident and likely correct; low agreement (diverse, contradictory responses) indicates uncertainty and potential hallucination. The key innovation is using the LLM itself (rather than surface-level string matching) to judge semantic similarity between sampled responses, making the approach work for long, complex answers where exact string matching would fail.

#### Match Function Calibration

The similarity threshold beta for the match function m_beta(X,Y',Y) = I{s(X,Y,Y') >= beta} is itself calibrated using conformal prediction:

beta_hat = inf{beta : (n/(n+1)) * sum(1 - m_beta(X_i, Y'_i, Y_i)) + 1/(n+1) <= alpha}

This bounds false negatives (L1 errors: mismatches incorrectly classified as matches). The guarantee ensures: E[C] <= E[L2] + alpha, where C is the true error rate and L2 represents errors detected by the calibrated match function. This requires a small manually-labeled calibration set (~100 question-answer pairs).

---

### Theoretical Guarantees

#### Conformal Risk Control (CRC) -- Main Result

The CRC procedure determines the abstention threshold via:

**lambda_hat_n = inf{lambda : (n/(n+1)) * L_n(lambda) + 1/(n+1) <= alpha}**

where L_n(lambda) is the empirical loss on calibration data. This guarantees:

**E[R(lambda_hat_n)] <= alpha**

The guarantee holds in expectation over both calibration data and test points, assuming only exchangeability (not strict i.i.d.). The O(1/n) correction term is tighter than standard confidence intervals using O(1/sqrt(n)) padding.

#### High-Probability Amplification (Proposition 3.1)

Given non-increasing, right-continuous, bounded loss function lambda -> l(z;lambda) in [0,B], i.i.d. calibration data partitioned into K = ceil(ln(1/delta)) subsets, selecting lambda_hat* = max_{i in [K]} lambda_hat_i ensures:

**P(R(lambda_hat*) <= e * alpha) >= 1 - delta**

The factor e (Euler's number) accounts for the trade-off between data efficiency and high-probability guarantees.

#### Risk-Controlling Prediction Sets (RCPS)

The paper also provides RCPS variants using upper confidence bounds:

lambda_hat_n = inf{lambda : L_n(lambda) + u(delta,n) <= alpha + c(delta,alpha,n)}

Three UCB variants are compared:
1. **Empirical Bernstein**: Uses sample variance estimation
2. **Hoeffding-Bentkus**: Specialized tight bound for binary losses
3. **Bernoulli KL**: Solves sup{p in [0,1] : KL(L_n(lambda), p) <= ln(sqrt(n)/delta)/n}

These provide guarantees that hold with probability 1-delta over the calibration data (rather than in expectation).

---

### Experimental Results

**Datasets:** Temporal Sequences (BIG-bench, predominantly long answers) and TriviaQA (short factual answers).

**Model:** Gemini Pro.

**Key findings:**
- On Temporal Sequences (alpha=0.05): MC and EMC scores significantly outperform LP scoring; all calibrated conformal methods maintain risk bounds while achieving lower abstention rates than baselines
- On TriviaQA: Performance differences between scoring methods are smaller (since answers are short, LP is more competitive)
- Empirical Bernstein bounds are more conservative; Hoeffding-Bentkus and Bernoulli KL perform similarly
- Calibration used 20% held-out test data, 10 random subsamples with replacement of increasing calibration sizes

---

### Reviewer Feedback

Unfortunately, the OpenReview pages for both submission IDs (`E7Cr9uNSNU` for the main listing, `vlo4JF27Xx` from the NeurIPS virtual site) did not expose reviewer comments through web fetching -- the reviews appear to be behind authentication or dynamically loaded. No public reviewer scores or detailed reviewer feedback were found.

**Note on venue:** The paper was accepted as a **workshop poster** at NeurIPS 2024 (Workshop on Statistical Frontiers in LLMs and Foundation Models), not as a main conference paper. This is a relevant distinction for assessing the level of peer review it received -- workshop papers typically undergo lighter review than main conference submissions.

**External commentary** from literature review sites (themoonlight.io) and tech press (TechXplore) was uniformly positive but surface-level, praising the non-invasive approach, statistical rigor, and empirical validation without raising specific technical criticisms.

---

### Limitations Acknowledged by the Authors

1. **Computational cost:** MC scoring requires O(k^2) LLM queries for k sampled responses per query; EMC and greedy variants reduce this but still require multiple inference calls.

2. **Match function dependency:** The quality of abstention depends heavily on the LLM's ability to accurately judge semantic similarity between responses. Conformal calibration of similarity thresholds requires manually labeled data.

3. **Log-probability degradation for long responses:** While this motivates the self-consistency approach, it also means the method is most needed (and most advantageous) precisely where evaluation is hardest.

4. **Calibration data requirements:** Requires a small calibration set. For match function calibration, manual labeling of ~100 question-answer pairs is needed. The exchangeability assumption must hold between calibration and test data.

5. **Exchangeability assumption:** Theoretical guarantees require exchangeability rather than strict i.i.d., but any distribution shift between calibration and deployment would violate this assumption and invalidate the guarantees.

6. **Assumption that similarity correlates with correctness:** The fundamental premise -- that self-consistent responses are more likely to be correct -- can fail when the model is confidently wrong (systematic hallucinations where the model consistently produces the same incorrect answer).

7. **Scope limited to closed-book QA:** Experiments were conducted only on closed-book, open-domain question answering tasks with Gemini Pro. Generalization to other tasks (summarization, reasoning, code generation) and other models is not empirically demonstrated.

---

### Sources

- [arXiv Abstract Page](https://arxiv.org/abs/2405.01563)
- [arXiv HTML Full Paper](https://arxiv.org/html/2405.01563v1)
- [OpenReview Forum](https://openreview.net/forum?id=E7Cr9uNSNU)
- [NeurIPS 2024 Virtual Poster](https://neurips.cc/virtual/2024/105548)
- [TechXplore Coverage](https://techxplore.com/news/2024-05/method-mitigate-hallucinations-large-language.html)
- [Moonlight Literature Review](https://www.themoonlight.io/en/review/mitigating-llm-hallucinations-via-conformal-abstention)
- [Semantic Scholar Entry](https://www.semanticscholar.org/paper/Mitigating-LLM-Hallucinations-via-Conformal-Abbasi-Yadkori-Kuzborskij/b5cd6bc53343f2ad8a7c7830555d8c744e626245)

agentId: aaba58fc2ff26163a (use SendMessage with to: 'aaba58fc2ff26163a' to continue this agent)
&lt;usage>total_tokens: 30129
tool_uses: 24
duration_ms: 223956&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f05d748c-954a-41fc-b42b-17b708647805",
  "isSidechain": false,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "type": "user",
  "uuid": "54c9ffc4-d8f5-4dd5-9476-12d19bcc9529",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Mitigating LLM Hallucinations via Conformal Abstention\" by Yasin Abbasi-Yadkori et al. (NeurIPS 2024). URL: https://arxiv.org/abs/2405.01563\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full PDF or HTML version if available\n3. Search for any OpenReview or NeurIPS reviewer comments\n4. Search the web for discussions or reviews of this paper\n\nReport back with:\n- The full abstract\n- Key method details (how they define nonconformity scores, how they use conformal prediction for abstention, what self-consistency scoring means in their context)\n- The theoretical guarantees they provide\n- Any reviewer feedback found\n- Limitations acknowledged by the authors\n\nBe thorough — I need enough detail to write a precise technical analysis.",
    "agentId": "aaba58fc2ff26163a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to provide a thorough report. Here is my findings:\n\n---\n\n## Research Report: \"Mitigating LLM Hallucinations via Conformal Abstention\"\n\n**Authors:** Yasin Abbasi-Yadkori, Ilja Kuzborskij, David Stutz, Andras Gyorgy, Adam Fisch, Arnaud Doucet, Iuliya Beloshapka, Wei-Hung Weng, Yao-Yuan Yang, Csaba Szepesvari, Ali Taylan Cemgil, Nenad Tomasev (Google DeepMind)\n\n**Venue:** NeurIPS 2024 -- Workshop on Statistical Frontiers in LLMs and Foundation Models (Poster, Submission ID 94176). Also available on OpenReview under IDs `E7Cr9uNSNU` and `vlo4JF27Xx`.\n\n**arXiv:** 2405.01563 (submitted April 4, 2024; published May 6, 2024)\n\n---\n\n### Full Abstract\n\n\"We develop a principled procedure for determining when a large language model (LLM) should abstain from responding (e.g., by saying 'I don't know') in a general domain, instead of resorting to possibly 'hallucinating' a non-sensical or incorrect answer.\" The approach builds on self-consistency as a reliable measure of model confidence, proposing that the LLM itself self-evaluate the similarity between each of its sampled responses for a given query, and then leverages conformal prediction techniques to develop an abstention procedure with rigorous theoretical guarantees on the hallucination rate (error rate). The method is lightweight, based only on prompting (no fine-tuning required). It was evaluated on closed-book, open-domain generative question answering tasks using Gemini Pro, and reliably bounds the hallucination rate while maintaining significantly less conservative abstention rates than baselines using log-probability scores, especially on datasets with long responses.\n\n---\n\n### Key Method Details\n\n#### Problem Formulation\n\nThe framework is cast as **selective classification**: given a query X, the system either produces a response f(X) or abstains. The components are:\n\n- **Match function** m(X; Y', Y) in {0,1}: Determines if two responses are semantically equivalent given query X\n- **Classifier** f: X -> Y: Maps queries to responses\n- **Score function** g(X): Quantifies model confidence\n- **Loss function**: l(X,Y; lambda) = (1 - a_lambda(X))(1 - m(X; f(X), Y)), penalizing incorrect non-abstention\n- **Abstention policy**: a_lambda(X) = 1 if g(X) < lambda, else 0\n\nThe optimization minimizes abstention rate T(lambda) subject to risk constraint R(lambda) <= alpha.\n\n#### Nonconformity Scores / Score Functions\n\nThree scoring mechanisms are proposed:\n\n1. **Match Count (MC):** For each sampled response Y^i, count how many of k other sampled responses are similar: g(Y^i) = |{j != i : s(X; Y^i, Y^j) > beta}|. The similarity function s: X x Y x Y -> R is implemented via LLM prompting, where the LLM is asked to compare two texts given the original query. The paper emphasizes that \"the self-evaluation prompt depends on the query itself, making it explicit that similarity of two responses depends on the question.\" This requires O(k^2) LLM calls for pairwise comparison.\n\n2. **Expected Match Count (EMC):** Instead of pairwise comparison, the LLM is asked in a single query how many of the alternative responses match a reference response. Using the log-probabilities over token outputs, the expected count is computed as: g(X) = sum_{i=1}^{k} q(\"i\"|X) * i, where q represents the LLM's token probability for numeric responses indicating match counts. This reduces computational cost substantially.\n\n3. **Log-Probability (LP) Baseline:** Uses the greedy response's normalized or unnormalized token-level log-probability as a confidence score. The paper demonstrates this degrades substantially for longer responses because \"these probabilities heavily depend on the length of the output sequence, and the likelihood of an answer becomes non-indicative of its correctness as the sequence length grows.\"\n\n#### Self-Consistency Scoring in Context\n\n\"Self-consistency\" here means: sample k responses from the LLM for the same query, then measure how much these responses agree with each other. High agreement (many responses matching) indicates the model is confident and likely correct; low agreement (diverse, contradictory responses) indicates uncertainty and potential hallucination. The key innovation is using the LLM itself (rather than surface-level string matching) to judge semantic similarity between sampled responses, making the approach work for long, complex answers where exact string matching would fail.\n\n#### Match Function Calibration\n\nThe similarity threshold beta for the match function m_beta(X,Y',Y) = I{s(X,Y,Y') >= beta} is itself calibrated using conformal prediction:\n\nbeta_hat = inf{beta : (n/(n+1)) * sum(1 - m_beta(X_i, Y'_i, Y_i)) + 1/(n+1) <= alpha}\n\nThis bounds false negatives (L1 errors: mismatches incorrectly classified as matches). The guarantee ensures: E[C] <= E[L2] + alpha, where C is the true error rate and L2 represents errors detected by the calibrated match function. This requires a small manually-labeled calibration set (~100 question-answer pairs).\n\n---\n\n### Theoretical Guarantees\n\n#### Conformal Risk Control (CRC) -- Main Result\n\nThe CRC procedure determines the abstention threshold via:\n\n**lambda_hat_n = inf{lambda : (n/(n+1)) * L_n(lambda) + 1/(n+1) <= alpha}**\n\nwhere L_n(lambda) is the empirical loss on calibration data. This guarantees:\n\n**E[R(lambda_hat_n)] <= alpha**\n\nThe guarantee holds in expectation over both calibration data and test points, assuming only exchangeability (not strict i.i.d.). The O(1/n) correction term is tighter than standard confidence intervals using O(1/sqrt(n)) padding.\n\n#### High-Probability Amplification (Proposition 3.1)\n\nGiven non-increasing, right-continuous, bounded loss function lambda -> l(z;lambda) in [0,B], i.i.d. calibration data partitioned into K = ceil(ln(1/delta)) subsets, selecting lambda_hat* = max_{i in [K]} lambda_hat_i ensures:\n\n**P(R(lambda_hat*) <= e * alpha) >= 1 - delta**\n\nThe factor e (Euler's number) accounts for the trade-off between data efficiency and high-probability guarantees.\n\n#### Risk-Controlling Prediction Sets (RCPS)\n\nThe paper also provides RCPS variants using upper confidence bounds:\n\nlambda_hat_n = inf{lambda : L_n(lambda) + u(delta,n) <= alpha + c(delta,alpha,n)}\n\nThree UCB variants are compared:\n1. **Empirical Bernstein**: Uses sample variance estimation\n2. **Hoeffding-Bentkus**: Specialized tight bound for binary losses\n3. **Bernoulli KL**: Solves sup{p in [0,1] : KL(L_n(lambda), p) <= ln(sqrt(n)/delta)/n}\n\nThese provide guarantees that hold with probability 1-delta over the calibration data (rather than in expectation).\n\n---\n\n### Experimental Results\n\n**Datasets:** Temporal Sequences (BIG-bench, predominantly long answers) and TriviaQA (short factual answers).\n\n**Model:** Gemini Pro.\n\n**Key findings:**\n- On Temporal Sequences (alpha=0.05): MC and EMC scores significantly outperform LP scoring; all calibrated conformal methods maintain risk bounds while achieving lower abstention rates than baselines\n- On TriviaQA: Performance differences between scoring methods are smaller (since answers are short, LP is more competitive)\n- Empirical Bernstein bounds are more conservative; Hoeffding-Bentkus and Bernoulli KL perform similarly\n- Calibration used 20% held-out test data, 10 random subsamples with replacement of increasing calibration sizes\n\n---\n\n### Reviewer Feedback\n\nUnfortunately, the OpenReview pages for both submission IDs (`E7Cr9uNSNU` for the main listing, `vlo4JF27Xx` from the NeurIPS virtual site) did not expose reviewer comments through web fetching -- the reviews appear to be behind authentication or dynamically loaded. No public reviewer scores or detailed reviewer feedback were found.\n\n**Note on venue:** The paper was accepted as a **workshop poster** at NeurIPS 2024 (Workshop on Statistical Frontiers in LLMs and Foundation Models), not as a main conference paper. This is a relevant distinction for assessing the level of peer review it received -- workshop papers typically undergo lighter review than main conference submissions.\n\n**External commentary** from literature review sites (themoonlight.io) and tech press (TechXplore) was uniformly positive but surface-level, praising the non-invasive approach, statistical rigor, and empirical validation without raising specific technical criticisms.\n\n---\n\n### Limitations Acknowledged by the Authors\n\n1. **Computational cost:** MC scoring requires O(k^2) LLM queries for k sampled responses per query; EMC and greedy variants reduce this but still require multiple inference calls.\n\n2. **Match function dependency:** The quality of abstention depends heavily on the LLM's ability to accurately judge semantic similarity between responses. Conformal calibration of similarity thresholds requires manually labeled data.\n\n3. **Log-probability degradation for long responses:** While this motivates the self-consistency approach, it also means the method is most needed (and most advantageous) precisely where evaluation is hardest.\n\n4. **Calibration data requirements:** Requires a small calibration set. For match function calibration, manual labeling of ~100 question-answer pairs is needed. The exchangeability assumption must hold between calibration and test data.\n\n5. **Exchangeability assumption:** Theoretical guarantees require exchangeability rather than strict i.i.d., but any distribution shift between calibration and deployment would violate this assumption and invalidate the guarantees.\n\n6. **Assumption that similarity correlates with correctness:** The fundamental premise -- that self-consistent responses are more likely to be correct -- can fail when the model is confidently wrong (systematic hallucinations where the model consistently produces the same incorrect answer).\n\n7. **Scope limited to closed-book QA:** Experiments were conducted only on closed-book, open-domain question answering tasks with Gemini Pro. Generalization to other tasks (summarization, reasoning, code generation) and other models is not empirically demonstrated.\n\n---\n\n### Sources\n\n- [arXiv Abstract Page](https://arxiv.org/abs/2405.01563)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2405.01563v1)\n- [OpenReview Forum](https://openreview.net/forum?id=E7Cr9uNSNU)\n- [NeurIPS 2024 Virtual Poster](https://neurips.cc/virtual/2024/105548)\n- [TechXplore Coverage](https://techxplore.com/news/2024-05/method-mitigate-hallucinations-large-language.html)\n- [Moonlight Literature Review](https://www.themoonlight.io/en/review/mitigating-llm-hallucinations-via-conformal-abstention)\n- [Semantic Scholar Entry](https://www.semanticscholar.org/paper/Mitigating-LLM-Hallucinations-via-Conformal-Abbasi-Yadkori-Kuzborskij/b5cd6bc53343f2ad8a7c7830555d8c744e626245)"
      }
    ],
    "totalDurationMs": 223956,
    "totalTokens": 30129,
    "totalToolUseCount": 24,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1146,
      "cache_read_input_tokens": 26120,
      "output_tokens": 2862,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1146
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2862,
          "cache_read_input_tokens": 26120,
          "cache_creation_input_tokens": 1146,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1146,
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
      "otherToolCount": 24
    }
  },
  "sourceToolAssistantUUID": "f05d748c-954a-41fc-b42b-17b708647805",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
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
  "leafUuid": "54c9ffc4-d8f5-4dd5-9476-12d19bcc9529",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze conformal prediction for adversarial RAG systems",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Tool call

_source line 13 · 2026-05-30T06:28:51.614Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01CUxAKfEUxGqkVFvha5fD9j`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze paper 2: Robust CP Sets",
  "prompt": "Research the paper \"Robust Yet Efficient Conformal Prediction Sets\" by Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski (ICML 2024). URL: https://arxiv.org/abs/2407.09165\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full PDF or HTML version if available\n3. Search for OpenReview or ICML reviewer comments\n4. Search the web for any technical discussions\n\nReport back with:\n- The full abstract\n- Key method details: how they bound worst-case conformity score changes under adversarial perturbation, how they handle both evasion and poisoning attacks, what makes their sets \"efficient\" (tight)\n- The theoretical guarantees and how they differ from prior robust CP work\n- Any reviewer feedback found\n- Limitations acknowledged\n\nBe thorough — I need enough detail to write a precise technical analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54c9ffc4-d8f5-4dd5-9476-12d19bcc9529",
  "isSidechain": false,
  "requestId": "req_011CbYHDpq9kgbWNExnpy35V",
  "type": "assistant",
  "uuid": "dad52b1c-1051-4c57-8692-37f3e44290d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011pKMP21MxFthQHvfgFxLFL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3316,
      "cache_read_input_tokens": 15098,
      "output_tokens": 328,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 328,
          "cache_read_input_tokens": 15098,
          "cache_creation_input_tokens": 3316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3316
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

_source line 14 · 2026-05-30T06:33:40.413Z_

<details><summary>↩ Tool result · `toolu_01CUxAKfEUxGqkVFvha5fD9j`</summary>

```text
Now I have comprehensive information. Let me compile the full report.

---

## Research Report: "Robust Yet Efficient Conformal Prediction Sets" (ICML 2024)

**Authors:** Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski  
**Venue:** 41st International Conference on Machine Learning (ICML 2024), Poster  
**Published in:** PMLR 235, pp. 17123-17147  
**arXiv:** [2407.09165](https://arxiv.org/abs/2407.09165)  
**Code:** [github.com/soroushzargar/CAS](https://github.com/soroushzargar/CAS)  
**OpenReview:** [MrNq6rbcUi](https://openreview.net/forum?id=MrNq6rbcUi)

---

### Full Abstract

"Conformal prediction (CP) can convert any model's output into prediction sets guaranteed to include the true label with any user-specified probability. However, same as the model itself, CP is vulnerable to adversarial test examples (evasion) and perturbed calibration data (poisoning). We derive provably robust sets by bounding the worst-case change in conformity scores. Our tighter bounds lead to more efficient sets. We cover both continuous and discrete (sparse) data and our guarantees work both for evasion and poisoning attacks (on both features and labels)."

---

### Key Method Details

**Core Idea: CDF-Aware Smoothed Prediction Sets (CAS)**

The central contribution is replacing mean-based bounds on smoothed conformity scores (as used in prior work RSCP) with CDF-based bounds, which capture more distributional information and yield tighter worst-case estimates.

**1. Randomized Smoothing of Conformity Scores**

The method begins by defining smoothed conformity scores:
- For continuous data: Gaussian smoothing -- s_hat(x, y) = E_delta[s(x + delta, y)] where delta ~ N(0, sigma^2 I)
- For discrete/sparse data: XOR with Bernoulli noise -- s_hat(x, y) = E[s(x XOR delta, y)]

**2. Bounding Worst-Case Score Changes**

The key technical challenge is computing max_{x_tilde in B(x)} E[s(xi(x_tilde), y)], which is intractable for arbitrary score functions. The paper relaxes this by optimizing over a function class H that encodes constraints about the true score function s.

- **RSCP's approach (mean-only bound):** Constrains only E[h(xi(x), y)] = p (the mean of the smoothed score). This yields s_bar_mean = Phi_sigma(Phi_sigma^{-1}(p) + r) for L2 perturbations, where Phi_sigma is the Gaussian CDF and r is the perturbation radius.

- **CAS's approach (CDF-based bound):** Constrains the full CDF -- for all thresholds b_i: Pr[h(xi(x), y) <= b_i] = p_i. The resulting bound is:
  s_bar_cdf = b_m - sum_{j=2}^{m-1} Phi_sigma(Phi_sigma^{-1}(p_j) - r) * (b_{j+1} - b_j)

This is strictly tighter because using the full CDF rather than just the mean provides more constraints on the optimization, shrinking the feasible set and producing a lower upper bound on the worst-case score.

**3. Handling Evasion Attacks**

For evasion (adversarial test examples in ball B(x)):
- Proposition 3.1: If s_bar(x, y) is an upper bound for {s(x_tilde, y) : x_tilde in B(x)}, then the conservative prediction set C_bar_alpha(x) = {y : s_bar(x, y) >= q_alpha} maintains Pr[y_{n+1} in C_bar_alpha(x_tilde)] >= 1 - alpha for all x_tilde in B(x).
- The clean calibration quantile q_alpha is computed on unperturbed data; only the test-time score uses the upper bound.
- Threat models supported: L2-bounded (continuous) and binary sparse perturbations (additions/deletions for graph data).

**4. Handling Poisoning Attacks**

This is a novel contribution -- no prior robust CP work addressed poisoning.

- **Feature poisoning:** The adversary corrupts up to k calibration features within perturbation balls. The paper finds the worst-case quantile by solving: q_alpha = min over feasible perturbations of Quant(alpha; {s(z_i, y_i)}), subject to each z_i in B(x_tilde_i) and at most k samples perturbed. This is formulated as a mixed-integer linear program (MILP).

- **Label poisoning:** The adversary flips up to k calibration labels. Similarly formulated as a constrained quantile minimization over label perturbation sets.

**5. Calibration-Time Variant (Proposition 5.1)**

Instead of computing the expensive upper bound s_bar at test time for every candidate label, the paper proposes computing lower bounds on calibration scores offline. The adjusted quantile q_bar_alpha = Quant(alpha; {s_bar(x_i, y_i)}) absorbs the robustness cost into calibration. At test time, only the standard smooth score s_hat needs to be evaluated -- a major speedup, especially for datasets with many classes (e.g., ImageNet with 1000 classes).

**6. Finite-Sample Corrections**

Since the CDF values p_j are estimated via Monte Carlo sampling, the paper uses:
- Dvoretzky-Kiefer-Wolfowitz (DKW) inequality for CDF confidence bands on calibration scores
- Bernstein inequality for test-time score concentration
- These are tighter than the Hoeffding bounds used in RSCP+ (Yan et al., 2024)
- The miscoverage budget alpha is split: alpha' = alpha - eta, where eta accounts for estimation uncertainty.

---

### Theoretical Guarantees and Comparison with Prior Work

**vs. RSCP (Gendler et al., 2021):**

| Aspect | RSCP | CAS |
|--------|------|-----|
| Bound type | Mean-only: Phi(Phi^{-1}(p) + r/sigma) | CDF-based (Eq. 10), strictly tighter |
| Evasion | L2 continuous only | L2 continuous + sparse/discrete |
| Poisoning | Not addressed | Feature poisoning + label poisoning |
| Finite-sample | Asymptotic only | Rigorous DKW/Bernstein corrections |
| Score functions | Requires Phi^{-1} transform | Direct optimization on s |
| Test-time cost | Upper bound for all classes | Calibration-time variant available |

RSCP is shown to be a special case of the CAS framework: s_bar_mean(x, y) = s_rscp(x, y) + r/sigma (Appendix F.1).

**vs. RSCP+ (Yan et al., 2024, ICLR 2024):**

RSCP+ identified that the original RSCP's guarantee was flawed in practice and proposed Hoeffding-based finite-sample corrections plus post-training transformations (PTT) and robust conformal training (RCT). CAS addresses the same finite-sample issue but uses DKW/Bernstein bounds, which are tighter. CAS also fundamentally improves the bound itself (CDF vs. mean), whereas RSCP+ focuses on training-time interventions to reduce score sensitivity.

**Key formal guarantee:** For the evasion setting with finite-sample correction, CAS achieves:
Pr[y_{n+1} in C_bar_{alpha+}(x_tilde_{n+1})] >= 1 - alpha
for all x_tilde in B(x_{n+1}), where the set is constructed using CDF-aware bounds with DKW/Bernstein corrections.

---

### Experimental Results

**Datasets:** CIFAR-10, ImageNet (continuous), Cora-ML (discrete/graph)  
**Score functions:** TPS (Threshold Prediction Sets) and APS (Adaptive Prediction Sets)  
**Smoothing parameters:** sigma in {0.12, 0.25}

**Key findings:**
- CAS consistently produces smaller prediction sets than RSCP across all datasets and perturbation radii
- On CIFAR-10 (r=0.125), CAS coverage is closer to the nominal 1-alpha level (less conservative) while still maintaining the guarantee
- The efficiency gap between CAS and RSCP grows with perturbation radius
- CAS achieves larger "size-preserving radius" -- the maximum radius at which the robust prediction set is the same size as the clean vanilla CP set
- The DKW-based finite-sample correction is tighter than Hoeffding-based alternatives
- For poisoning: CAS provides the first certifications (no baselines exist for comparison)
- Set-size reductions of 2x-10x compared to prior robust CP methods with negligible empirical coverage loss

---

### Reviewer Feedback

ICML 2024 reviews for this paper are **not publicly accessible** through the OpenReview API or web interface. The paper was accepted as a **Poster** at ICML 2024. The OpenReview page exists at `https://openreview.net/forum?id=MrNq6rbcUi` but the review content appears to be restricted/not publicly released for this ICML cycle. No cached review scores or reviewer comments were found through web search.

From third-party summaries (liner.com, emergentmind.com), the paper is characterized as making "meaningful contributions to robust machine learning by balancing theoretical guarantees with practical efficiency." It is positioned alongside subsequent work (RCP1, BinCP, VRCP) as part of a wave of methods achieving significant set-size reductions over earlier robust CP approaches.

---

### Acknowledged Limitations

1. **Poisoning scalability:** The MILP formulation for poisoning robustness becomes expensive for very large calibration sets. The paper reports "a few minutes" for modest-sized calibration sets, implying it does not scale gracefully.

2. **Monte Carlo overhead:** Estimating the smoothed scores and their CDFs requires a large number of MC samples per input, adding computational cost.

3. **Exchangeability assumption retained:** The method still requires exchangeability between calibration and test data -- a weaker assumption than i.i.d., but still a meaningful constraint the paper cannot remove.

4. **Threat model specificity:** Separate certification is needed per threat model type (L2 vs. sparse). Extensions to other threat models are described as "simple" but are not experimentally validated.

5. **Attacker goal assumption:** The paper assumes the attacker's goal is to reduce empirical coverage. Other adversarial objectives (e.g., inflating set size to degrade utility, or targeting specific classes) are not addressed.

6. **Fairness intersection unaddressed:** The authors note that robustness can interact with fairness (e.g., different groups may see different set sizes under perturbation), and studying this intersection is flagged as future work.

7. **Smoothing-induced accuracy loss:** The base classifier accuracy degrades under randomized smoothing (a well-known cost), which the paper inherits but does not mitigate.

Sources:
- [arXiv Abstract](https://arxiv.org/abs/2407.09165)
- [PMLR Proceedings](https://proceedings.mlr.press/v235/h-zargarbashi24a.html)
- [ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2407.09165)
- [OpenReview](https://openreview.net/forum?id=MrNq6rbcUi)
- [GitHub CAS Implementation](https://github.com/soroushzargar/CAS)
- [Emergent Mind Topic Page](https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction)
- [RSCP+ (Yan et al., ICLR 2024)](https://arxiv.org/abs/2404.19651)

agentId: aefc4c91881d637b9 (use SendMessage with to: 'aefc4c91881d637b9' to continue this agent)
&lt;usage>total_tokens: 35640
tool_uses: 29
duration_ms: 288794&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dad52b1c-1051-4c57-8692-37f3e44290d5",
  "isSidechain": false,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "type": "user",
  "uuid": "80735533-9085-4dff-a631-4a24e0f8e0b6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Robust Yet Efficient Conformal Prediction Sets\" by Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski (ICML 2024). URL: https://arxiv.org/abs/2407.09165\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full PDF or HTML version if available\n3. Search for OpenReview or ICML reviewer comments\n4. Search the web for any technical discussions\n\nReport back with:\n- The full abstract\n- Key method details: how they bound worst-case conformity score changes under adversarial perturbation, how they handle both evasion and poisoning attacks, what makes their sets \"efficient\" (tight)\n- The theoretical guarantees and how they differ from prior robust CP work\n- Any reviewer feedback found\n- Limitations acknowledged\n\nBe thorough — I need enough detail to write a precise technical analysis.",
    "agentId": "aefc4c91881d637b9",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the full report.\n\n---\n\n## Research Report: \"Robust Yet Efficient Conformal Prediction Sets\" (ICML 2024)\n\n**Authors:** Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski  \n**Venue:** 41st International Conference on Machine Learning (ICML 2024), Poster  \n**Published in:** PMLR 235, pp. 17123-17147  \n**arXiv:** [2407.09165](https://arxiv.org/abs/2407.09165)  \n**Code:** [github.com/soroushzargar/CAS](https://github.com/soroushzargar/CAS)  \n**OpenReview:** [MrNq6rbcUi](https://openreview.net/forum?id=MrNq6rbcUi)\n\n---\n\n### Full Abstract\n\n\"Conformal prediction (CP) can convert any model's output into prediction sets guaranteed to include the true label with any user-specified probability. However, same as the model itself, CP is vulnerable to adversarial test examples (evasion) and perturbed calibration data (poisoning). We derive provably robust sets by bounding the worst-case change in conformity scores. Our tighter bounds lead to more efficient sets. We cover both continuous and discrete (sparse) data and our guarantees work both for evasion and poisoning attacks (on both features and labels).\"\n\n---\n\n### Key Method Details\n\n**Core Idea: CDF-Aware Smoothed Prediction Sets (CAS)**\n\nThe central contribution is replacing mean-based bounds on smoothed conformity scores (as used in prior work RSCP) with CDF-based bounds, which capture more distributional information and yield tighter worst-case estimates.\n\n**1. Randomized Smoothing of Conformity Scores**\n\nThe method begins by defining smoothed conformity scores:\n- For continuous data: Gaussian smoothing -- s_hat(x, y) = E_delta[s(x + delta, y)] where delta ~ N(0, sigma^2 I)\n- For discrete/sparse data: XOR with Bernoulli noise -- s_hat(x, y) = E[s(x XOR delta, y)]\n\n**2. Bounding Worst-Case Score Changes**\n\nThe key technical challenge is computing max_{x_tilde in B(x)} E[s(xi(x_tilde), y)], which is intractable for arbitrary score functions. The paper relaxes this by optimizing over a function class H that encodes constraints about the true score function s.\n\n- **RSCP's approach (mean-only bound):** Constrains only E[h(xi(x), y)] = p (the mean of the smoothed score). This yields s_bar_mean = Phi_sigma(Phi_sigma^{-1}(p) + r) for L2 perturbations, where Phi_sigma is the Gaussian CDF and r is the perturbation radius.\n\n- **CAS's approach (CDF-based bound):** Constrains the full CDF -- for all thresholds b_i: Pr[h(xi(x), y) <= b_i] = p_i. The resulting bound is:\n  s_bar_cdf = b_m - sum_{j=2}^{m-1} Phi_sigma(Phi_sigma^{-1}(p_j) - r) * (b_{j+1} - b_j)\n\nThis is strictly tighter because using the full CDF rather than just the mean provides more constraints on the optimization, shrinking the feasible set and producing a lower upper bound on the worst-case score.\n\n**3. Handling Evasion Attacks**\n\nFor evasion (adversarial test examples in ball B(x)):\n- Proposition 3.1: If s_bar(x, y) is an upper bound for {s(x_tilde, y) : x_tilde in B(x)}, then the conservative prediction set C_bar_alpha(x) = {y : s_bar(x, y) >= q_alpha} maintains Pr[y_{n+1} in C_bar_alpha(x_tilde)] >= 1 - alpha for all x_tilde in B(x).\n- The clean calibration quantile q_alpha is computed on unperturbed data; only the test-time score uses the upper bound.\n- Threat models supported: L2-bounded (continuous) and binary sparse perturbations (additions/deletions for graph data).\n\n**4. Handling Poisoning Attacks**\n\nThis is a novel contribution -- no prior robust CP work addressed poisoning.\n\n- **Feature poisoning:** The adversary corrupts up to k calibration features within perturbation balls. The paper finds the worst-case quantile by solving: q_alpha = min over feasible perturbations of Quant(alpha; {s(z_i, y_i)}), subject to each z_i in B(x_tilde_i) and at most k samples perturbed. This is formulated as a mixed-integer linear program (MILP).\n\n- **Label poisoning:** The adversary flips up to k calibration labels. Similarly formulated as a constrained quantile minimization over label perturbation sets.\n\n**5. Calibration-Time Variant (Proposition 5.1)**\n\nInstead of computing the expensive upper bound s_bar at test time for every candidate label, the paper proposes computing lower bounds on calibration scores offline. The adjusted quantile q_bar_alpha = Quant(alpha; {s_bar(x_i, y_i)}) absorbs the robustness cost into calibration. At test time, only the standard smooth score s_hat needs to be evaluated -- a major speedup, especially for datasets with many classes (e.g., ImageNet with 1000 classes).\n\n**6. Finite-Sample Corrections**\n\nSince the CDF values p_j are estimated via Monte Carlo sampling, the paper uses:\n- Dvoretzky-Kiefer-Wolfowitz (DKW) inequality for CDF confidence bands on calibration scores\n- Bernstein inequality for test-time score concentration\n- These are tighter than the Hoeffding bounds used in RSCP+ (Yan et al., 2024)\n- The miscoverage budget alpha is split: alpha' = alpha - eta, where eta accounts for estimation uncertainty.\n\n---\n\n### Theoretical Guarantees and Comparison with Prior Work\n\n**vs. RSCP (Gendler et al., 2021):**\n\n| Aspect | RSCP | CAS |\n|--------|------|-----|\n| Bound type | Mean-only: Phi(Phi^{-1}(p) + r/sigma) | CDF-based (Eq. 10), strictly tighter |\n| Evasion | L2 continuous only | L2 continuous + sparse/discrete |\n| Poisoning | Not addressed | Feature poisoning + label poisoning |\n| Finite-sample | Asymptotic only | Rigorous DKW/Bernstein corrections |\n| Score functions | Requires Phi^{-1} transform | Direct optimization on s |\n| Test-time cost | Upper bound for all classes | Calibration-time variant available |\n\nRSCP is shown to be a special case of the CAS framework: s_bar_mean(x, y) = s_rscp(x, y) + r/sigma (Appendix F.1).\n\n**vs. RSCP+ (Yan et al., 2024, ICLR 2024):**\n\nRSCP+ identified that the original RSCP's guarantee was flawed in practice and proposed Hoeffding-based finite-sample corrections plus post-training transformations (PTT) and robust conformal training (RCT). CAS addresses the same finite-sample issue but uses DKW/Bernstein bounds, which are tighter. CAS also fundamentally improves the bound itself (CDF vs. mean), whereas RSCP+ focuses on training-time interventions to reduce score sensitivity.\n\n**Key formal guarantee:** For the evasion setting with finite-sample correction, CAS achieves:\nPr[y_{n+1} in C_bar_{alpha+}(x_tilde_{n+1})] >= 1 - alpha\nfor all x_tilde in B(x_{n+1}), where the set is constructed using CDF-aware bounds with DKW/Bernstein corrections.\n\n---\n\n### Experimental Results\n\n**Datasets:** CIFAR-10, ImageNet (continuous), Cora-ML (discrete/graph)  \n**Score functions:** TPS (Threshold Prediction Sets) and APS (Adaptive Prediction Sets)  \n**Smoothing parameters:** sigma in {0.12, 0.25}\n\n**Key findings:**\n- CAS consistently produces smaller prediction sets than RSCP across all datasets and perturbation radii\n- On CIFAR-10 (r=0.125), CAS coverage is closer to the nominal 1-alpha level (less conservative) while still maintaining the guarantee\n- The efficiency gap between CAS and RSCP grows with perturbation radius\n- CAS achieves larger \"size-preserving radius\" -- the maximum radius at which the robust prediction set is the same size as the clean vanilla CP set\n- The DKW-based finite-sample correction is tighter than Hoeffding-based alternatives\n- For poisoning: CAS provides the first certifications (no baselines exist for comparison)\n- Set-size reductions of 2x-10x compared to prior robust CP methods with negligible empirical coverage loss\n\n---\n\n### Reviewer Feedback\n\nICML 2024 reviews for this paper are **not publicly accessible** through the OpenReview API or web interface. The paper was accepted as a **Poster** at ICML 2024. The OpenReview page exists at `https://openreview.net/forum?id=MrNq6rbcUi` but the review content appears to be restricted/not publicly released for this ICML cycle. No cached review scores or reviewer comments were found through web search.\n\nFrom third-party summaries (liner.com, emergentmind.com), the paper is characterized as making \"meaningful contributions to robust machine learning by balancing theoretical guarantees with practical efficiency.\" It is positioned alongside subsequent work (RCP1, BinCP, VRCP) as part of a wave of methods achieving significant set-size reductions over earlier robust CP approaches.\n\n---\n\n### Acknowledged Limitations\n\n1. **Poisoning scalability:** The MILP formulation for poisoning robustness becomes expensive for very large calibration sets. The paper reports \"a few minutes\" for modest-sized calibration sets, implying it does not scale gracefully.\n\n2. **Monte Carlo overhead:** Estimating the smoothed scores and their CDFs requires a large number of MC samples per input, adding computational cost.\n\n3. **Exchangeability assumption retained:** The method still requires exchangeability between calibration and test data -- a weaker assumption than i.i.d., but still a meaningful constraint the paper cannot remove.\n\n4. **Threat model specificity:** Separate certification is needed per threat model type (L2 vs. sparse). Extensions to other threat models are described as \"simple\" but are not experimentally validated.\n\n5. **Attacker goal assumption:** The paper assumes the attacker's goal is to reduce empirical coverage. Other adversarial objectives (e.g., inflating set size to degrade utility, or targeting specific classes) are not addressed.\n\n6. **Fairness intersection unaddressed:** The authors note that robustness can interact with fairness (e.g., different groups may see different set sizes under perturbation), and studying this intersection is flagged as future work.\n\n7. **Smoothing-induced accuracy loss:** The base classifier accuracy degrades under randomized smoothing (a well-known cost), which the paper inherits but does not mitigate.\n\nSources:\n- [arXiv Abstract](https://arxiv.org/abs/2407.09165)\n- [PMLR Proceedings](https://proceedings.mlr.press/v235/h-zargarbashi24a.html)\n- [ar5iv HTML](https://ar5iv.labs.arxiv.org/html/2407.09165)\n- [OpenReview](https://openreview.net/forum?id=MrNq6rbcUi)\n- [GitHub CAS Implementation](https://github.com/soroushzargar/CAS)\n- [Emergent Mind Topic Page](https://www.emergentmind.com/topics/adversarially-robust-conformal-prediction)\n- [RSCP+ (Yan et al., ICLR 2024)](https://arxiv.org/abs/2404.19651)"
      }
    ],
    "totalDurationMs": 288794,
    "totalTokens": 35640,
    "totalToolUseCount": 29,
    "usage": {
      "input_tokens": 343,
      "cache_creation_input_tokens": 1930,
      "cache_read_input_tokens": 30349,
      "output_tokens": 3018,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1930
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 343,
          "output_tokens": 3018,
          "cache_read_input_tokens": 30349,
          "cache_creation_input_tokens": 1930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1930,
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
      "otherToolCount": 29
    }
  },
  "sourceToolAssistantUUID": "dad52b1c-1051-4c57-8692-37f3e44290d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-30T06:33:49.540Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01L9dSpU1DmTPqKBWt5FeCD2`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze paper 3: Poisoning NLG cert",
  "prompt": "Research the paper \"Towards Poisoning Robustness Certification for Natural Language Generation\" by Mihnea Ghitu, Matthew Wicker (arXiv 2026). URL: https://arxiv.org/abs/2602.09757\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full PDF or HTML version if available\n3. Search the web for any discussions or reviews of this paper\n\nReport back with:\n- The full abstract\n- Key method details: what is Targeted Partition Aggregation (TPA), how they certify NLG validity against poisoning, how they compute minimum poisoning budgets, what validity functions they use\n- The theoretical guarantees\n- How it relates to RobustRAG\n- Limitations acknowledged\n\nBe thorough — I need enough detail to write a precise technical analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80735533-9085-4dff-a631-4a24e0f8e0b6",
  "isSidechain": false,
  "requestId": "req_011CbYHbkckynmHVraey7kGJ",
  "type": "assistant",
  "uuid": "00de3b18-8d28-4b6d-aa29-906224d51656",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UcYjUcjgo5jPQLuPdVjG5o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3425,
      "cache_read_input_tokens": 18414,
      "output_tokens": 299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3425,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 299,
          "cache_read_input_tokens": 18414,
          "cache_creation_input_tokens": 3425,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3425
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

_source line 16 · 2026-05-30T06:36:49.637Z_

<details><summary>↩ Tool result · `toolu_01L9dSpU1DmTPqKBWt5FeCD2`</summary>

```text
Here is a thorough technical summary of the paper.

---

## "Towards Poisoning Robustness Certification for Natural Language Generation"
**Authors:** Mihnea Ghitu, Matthew Wicker
**arXiv:** 2602.09757, submitted February 10, 2026
**Category:** cs.LG

---

### Full Abstract

The paper addresses the reliability of language generation systems deployed in security-sensitive domains. While certified poisoning defenses provide provable robustness bounds for classification tasks, they are fundamentally ill-equipped for autoregressive generation because they cannot handle sequential predictions or the exponentially large output space of language models. The authors formalize two security properties -- **stability** (robustness to any change in generation) and **validity** (robustness to targeted, harmful changes in generation) -- and introduce **Targeted Partition Aggregation (TPA)**, described as "the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase." They extend TPA using mixed integer linear programming (MILP) for multi-turn generations and demonstrate effectiveness in certifying agent tool-calling robustness and preference-based alignment, achieving >90% validity certification at k=9 poisoning budget with 20+ token horizons.

---

### Key Method Details

#### 1. Targeted Partition Aggregation (TPA)

TPA builds on the **shard-and-aggregate** framework:
1. Partition training dataset D into S disjoint shards {D_s}
2. Train independent base models {f_s} on each shard
3. At test time, ensemble generates via majority voting: F(x) = argmax_{y in V} V[y], where V[t] counts votes for token t

**Algorithm 1 (Core TPA):** Given token index i, vote counts V (sorted descending), and target token t with v_t votes:
- For each phase s, compute Delta[j] = V[j] - V[j+1] (gap between consecutive vote counts)
- Compute Phi[s] = v_t + sum of first s gaps (cumulative votes reassigned to t)
- Find s* = min{s | Phi[s] > V[s] or s = |V|-1}
- Return r_i^t = Phi[s*-1] + floor(((V_{s*} - Phi[s*-1] + 1) * s*) / (s*+1))

The intuition: TPA iteratively reallocates votes from top-ranked classes to the target harmful token t until achieving plurality. At each phase s, the top s classes are equalized and jointly reduced to the next vote level, with removed votes reassigned to t. This computes the **minimum number of shard poisonings** needed to make t win the vote.

#### 2. Stability vs. Validity Definitions

**Definition 4.1 (i-th token stability):** For prompt x, the i-th token generation is k-stable if:
max_{D_tilde in B_k(D)} I(f(x)[i] != f_tilde(x)[i]) = 0

The stability radius is the minimum r where a poisoned dataset can cause any token change.

**Definition 4.2 (i-th token validity):** Given harmful sentence s_h = {t_1,...,t_T}, generation is i-th token valid at x if:
max_{D_tilde in B_k(D)} I(f_tilde(x + {t_1,...,t_{i-1}})[0] = t_i) = 0

The validity radius r_i^t is the minimum poisoning budget needed to make target token t_i the next generated token. This is the key conceptual innovation: validity asks whether a **specific harmful output** can be induced, rather than whether **any** change occurs.

**Definition 4.4 (Finite-horizon stability/validity):**
r_{1:L}(x) = min_{i in [L]} {r_i(x)}

#### 3. Handling the Autoregressive Dependency Problem

Two soundness concerns arise: (i) the i-th token certificate assumes the prefix f(x)[1:i-1] is fixed, but if an adversary changes token j&lt;i, this assumption is violated; (ii) harmful phrases comprise multiple tokens. Solutions:

**Proposition 4.5 (Sequential certificate):** r_min(x; 1:L) = min_{i in {1,...,L}} r_i(x) <= r_{1:L}(x). Any attack on the full prefix requires at least r_min poisoned samples. This is a sound lower bound because changing any prefix token requires at least as many poisoned points as the weakest position.

**Proposition 4.6 (Phrase-level certificate):** Treat length-m token sequences as atomic units. Each shard generates m tokens autoregressively, then majority voting occurs over the expanded space V^m. For m=1, this reduces to token-level certification (tight but high latency). For moderate m in [5,20], it certifies moderate-length phrases directly with tighter bounds than sequential min. For m=L (full sequence), latency minimizes but "votes diffuse over the |V|^L classes" making margins weak.

#### 4. Multi-Turn Collective Certification (MILP)

**Definition 4.7 (Collective TPA Certificate):** For N test prompts with global budget K and M shards, the MILP maximizes:
(1/N) sum_{i=1}^N I[tau_i <= sum_{j=1}^M psi_j^(i)]

Subject to:
- psi_j^(i) encodes poisonable votes from shard j for prompt i
- tau_i is the aggregation margin to flip the ensemble prediction
- sum_{j=1}^M a_j = K (global budget constraint distributes K across M shards)

**Theorem 4.8:** The solution A(K) guarantees at least floor(N * A(K)) prompts maintain their original (safe) predictions under any attack within budget K.

#### 5. Validity Functions

Validity is defined relative to a specific harmful target. The paper does not propose separate "validity functions" as modular components; rather, validity is formalized directly in Definition 4.2 as the impossibility of inducing a specific target token/phrase given a poisoning budget. The key distinction is that stability measures robustness to **any** output change (untargeted), while validity measures robustness to a **specific harmful** output change (targeted).

---

### Theoretical Guarantees

1. **Theorem 4.3 (Token-Level Validity Certificate):** "The value r_i^t computed by Algorithm 1 is a sound lower bound on the i-th token validity radius. For any poisoning budget k <= r_i^t, the adversary cannot make target token t the plurality prediction."

2. **Proposition 4.5 (Sequential certificate):** The minimum per-position radius is a sound lower bound on the full-sequence radius.

3. **Proposition 4.6 (Phrase-level certificate):** Certification algorithms remain sound when applied to phrase-level (m-token) voting over the transformed space V^m.

4. **Theorem 4.8 (Collective certificate):** For any attack within global budget K, at least floor(N * A(K)) prompts maintain safe predictions.

The threat model assumes an **unbounded, white-box adversary** with access to architecture, dataset, training order, and hyperparameters, who can perform general poisoning of features, labels, or both, constrained only by |D symmetric_difference D_tilde| <= r.

---

### Relationship to RobustRAG

The paper explicitly distinguishes itself from RobustRAG (Xiang et al., 2024, "Certifiably robust RAG against retrieval corruption"). The authors state: **"Unlike our focus on post-training poisoning, this research addresses retrieval corruption in Retrieval-Augmented Generation (RAG), where attackers corrupt retrieved documents rather than the model's (post-)training data."**

Key differences:
- **Threat model:** RobustRAG addresses **inference-time retrieval corruption** (adversary corrupts retrieved documents at test time). This paper addresses **training-time data poisoning** (adversary corrupts the training data before/during fine-tuning).
- **Defense mechanism:** Both use isolate-then-aggregate strategies, but RobustRAG isolates retrieved passages and aggregates LLM responses, while this paper partitions training data into shards, trains independent models, and aggregates via majority voting.
- **Certification target:** RobustRAG certifies that retrieval corruption cannot change outputs. This paper certifies that training data poisoning cannot induce specific harmful outputs (validity) or any output change (stability).

---

### Experimental Results

**Models used:** OLMo-1B, OLMo-2-1B-Instruct, Gemma2-2B, Qwen1.5-4B

**Datasets and settings:**

1. **Agent Tool-Calling (MCP):** Toucan dataset (50K training instances, top 150 tools from real-world MCP environments), 500 shards.
   - Full LoRA: median certified robustness r=249 (resists 0.5% dataset poisoning), accuracy 67% vs 40% zero-shot baseline, latency ~150s
   - Last-3 LoRA: r=163, 5.9x speedup (latency ~25s)

2. **Preference Alignment (HH-RLHF):** 20 shards across three models.
   - DPA+ROE (stability): 42-54% First Token Stability at k=9
   - TPA+MSC (validity): >90% First Token Validity at k=9, validity horizons of 21+ tokens
   - Stability Horizon: 0.25-8.31 tokens depending on model and method

3. **Empirical Attack Robustness:** Ensemble defense reduces backdoor attack success from 40-48% (single model) to <6%, with stealth scores >95%

**Evaluation Metrics:**
- First-Token Stability (FTS@k): fraction of prompts with unchanged first token under k-poisoning
- First-Token Validity (FTV@k): fraction where first token cannot be changed to target harmful token
- Stability Horizon (SH@k): average length of longest certified stable prefix
- Validity Horizon (VH@k): average length before harmful sequence can be induced

---

### Limitations Acknowledged

1. **Inference-time latency** remains "an open challenge" -- running hundreds of shard models is expensive (150s for Full LoRA with 500 shards).
2. **Conservative bounds:** "Although our certificates provide rigorous lower bounds, they are inherently conservative. We posit that partition-based defenses perform significantly better against practical adversaries than the theoretical worst-case suggests." The empirical results substantially exceed certified guarantees.
3. **Narrow threat model:** "Our certification framework addresses a specific threat model: training-time poisoning under worst-case assumptions. Other important threat modes -- such as test-time evasion, prompt-based attacks, and triggered backdoors -- remain critical open challenges."
4. **Bounds do not eliminate vulnerabilities** from alternative attack surfaces.
5. The stability-validity trade-off and the phrase-length trade-off (tight bounds vs. computational cost) are inherent tensions in the framework.

---

### Discussion/Reviews

No external reviews, blog posts, or social media discussions of this paper were found. The paper appears to be a recent preprint (February 2026) without yet appearing at a major venue. It is positioned in the lineage of Deep Partition Aggregation (DPA) by Levine & Feizi and Finite Aggregation by Rezaei et al., extending these classification-oriented certified defenses to the autoregressive NLG setting for the first time.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2602.09757)
- [arXiv HTML Version](https://arxiv.org/html/2602.09757)
- [arXiv PDF](https://arxiv.org/pdf/2602.09757)
- [Deep Partition Aggregation (Levine & Feizi)](https://arxiv.org/pdf/2006.14768)
- [RobustRAG (Xiang et al.)](https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption)

agentId: a8858d54dfffc89c6 (use SendMessage with to: 'a8858d54dfffc89c6' to continue this agent)
&lt;usage>total_tokens: 23761
tool_uses: 12
duration_ms: 180091&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00de3b18-8d28-4b6d-aa29-906224d51656",
  "isSidechain": false,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "type": "user",
  "uuid": "3ffa570e-c813-4856-82b1-28da5958d571",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Towards Poisoning Robustness Certification for Natural Language Generation\" by Mihnea Ghitu, Matthew Wicker (arXiv 2026). URL: https://arxiv.org/abs/2602.09757\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full PDF or HTML version if available\n3. Search the web for any discussions or reviews of this paper\n\nReport back with:\n- The full abstract\n- Key method details: what is Targeted Partition Aggregation (TPA), how they certify NLG validity against poisoning, how they compute minimum poisoning budgets, what validity functions they use\n- The theoretical guarantees\n- How it relates to RobustRAG\n- Limitations acknowledged\n\nBe thorough — I need enough detail to write a precise technical analysis.",
    "agentId": "a8858d54dfffc89c6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a thorough technical summary of the paper.\n\n---\n\n## \"Towards Poisoning Robustness Certification for Natural Language Generation\"\n**Authors:** Mihnea Ghitu, Matthew Wicker\n**arXiv:** 2602.09757, submitted February 10, 2026\n**Category:** cs.LG\n\n---\n\n### Full Abstract\n\nThe paper addresses the reliability of language generation systems deployed in security-sensitive domains. While certified poisoning defenses provide provable robustness bounds for classification tasks, they are fundamentally ill-equipped for autoregressive generation because they cannot handle sequential predictions or the exponentially large output space of language models. The authors formalize two security properties -- **stability** (robustness to any change in generation) and **validity** (robustness to targeted, harmful changes in generation) -- and introduce **Targeted Partition Aggregation (TPA)**, described as \"the first algorithm to certify validity/targeted attacks by computing the minimum poisoning budget needed to induce a specific harmful class, token, or phrase.\" They extend TPA using mixed integer linear programming (MILP) for multi-turn generations and demonstrate effectiveness in certifying agent tool-calling robustness and preference-based alignment, achieving >90% validity certification at k=9 poisoning budget with 20+ token horizons.\n\n---\n\n### Key Method Details\n\n#### 1. Targeted Partition Aggregation (TPA)\n\nTPA builds on the **shard-and-aggregate** framework:\n1. Partition training dataset D into S disjoint shards {D_s}\n2. Train independent base models {f_s} on each shard\n3. At test time, ensemble generates via majority voting: F(x) = argmax_{y in V} V[y], where V[t] counts votes for token t\n\n**Algorithm 1 (Core TPA):** Given token index i, vote counts V (sorted descending), and target token t with v_t votes:\n- For each phase s, compute Delta[j] = V[j] - V[j+1] (gap between consecutive vote counts)\n- Compute Phi[s] = v_t + sum of first s gaps (cumulative votes reassigned to t)\n- Find s* = min{s | Phi[s] > V[s] or s = |V|-1}\n- Return r_i^t = Phi[s*-1] + floor(((V_{s*} - Phi[s*-1] + 1) * s*) / (s*+1))\n\nThe intuition: TPA iteratively reallocates votes from top-ranked classes to the target harmful token t until achieving plurality. At each phase s, the top s classes are equalized and jointly reduced to the next vote level, with removed votes reassigned to t. This computes the **minimum number of shard poisonings** needed to make t win the vote.\n\n#### 2. Stability vs. Validity Definitions\n\n**Definition 4.1 (i-th token stability):** For prompt x, the i-th token generation is k-stable if:\nmax_{D_tilde in B_k(D)} I(f(x)[i] != f_tilde(x)[i]) = 0\n\nThe stability radius is the minimum r where a poisoned dataset can cause any token change.\n\n**Definition 4.2 (i-th token validity):** Given harmful sentence s_h = {t_1,...,t_T}, generation is i-th token valid at x if:\nmax_{D_tilde in B_k(D)} I(f_tilde(x + {t_1,...,t_{i-1}})[0] = t_i) = 0\n\nThe validity radius r_i^t is the minimum poisoning budget needed to make target token t_i the next generated token. This is the key conceptual innovation: validity asks whether a **specific harmful output** can be induced, rather than whether **any** change occurs.\n\n**Definition 4.4 (Finite-horizon stability/validity):**\nr_{1:L}(x) = min_{i in [L]} {r_i(x)}\n\n#### 3. Handling the Autoregressive Dependency Problem\n\nTwo soundness concerns arise: (i) the i-th token certificate assumes the prefix f(x)[1:i-1] is fixed, but if an adversary changes token j&lt;i, this assumption is violated; (ii) harmful phrases comprise multiple tokens. Solutions:\n\n**Proposition 4.5 (Sequential certificate):** r_min(x; 1:L) = min_{i in {1,...,L}} r_i(x) <= r_{1:L}(x). Any attack on the full prefix requires at least r_min poisoned samples. This is a sound lower bound because changing any prefix token requires at least as many poisoned points as the weakest position.\n\n**Proposition 4.6 (Phrase-level certificate):** Treat length-m token sequences as atomic units. Each shard generates m tokens autoregressively, then majority voting occurs over the expanded space V^m. For m=1, this reduces to token-level certification (tight but high latency). For moderate m in [5,20], it certifies moderate-length phrases directly with tighter bounds than sequential min. For m=L (full sequence), latency minimizes but \"votes diffuse over the |V|^L classes\" making margins weak.\n\n#### 4. Multi-Turn Collective Certification (MILP)\n\n**Definition 4.7 (Collective TPA Certificate):** For N test prompts with global budget K and M shards, the MILP maximizes:\n(1/N) sum_{i=1}^N I[tau_i <= sum_{j=1}^M psi_j^(i)]\n\nSubject to:\n- psi_j^(i) encodes poisonable votes from shard j for prompt i\n- tau_i is the aggregation margin to flip the ensemble prediction\n- sum_{j=1}^M a_j = K (global budget constraint distributes K across M shards)\n\n**Theorem 4.8:** The solution A(K) guarantees at least floor(N * A(K)) prompts maintain their original (safe) predictions under any attack within budget K.\n\n#### 5. Validity Functions\n\nValidity is defined relative to a specific harmful target. The paper does not propose separate \"validity functions\" as modular components; rather, validity is formalized directly in Definition 4.2 as the impossibility of inducing a specific target token/phrase given a poisoning budget. The key distinction is that stability measures robustness to **any** output change (untargeted), while validity measures robustness to a **specific harmful** output change (targeted).\n\n---\n\n### Theoretical Guarantees\n\n1. **Theorem 4.3 (Token-Level Validity Certificate):** \"The value r_i^t computed by Algorithm 1 is a sound lower bound on the i-th token validity radius. For any poisoning budget k <= r_i^t, the adversary cannot make target token t the plurality prediction.\"\n\n2. **Proposition 4.5 (Sequential certificate):** The minimum per-position radius is a sound lower bound on the full-sequence radius.\n\n3. **Proposition 4.6 (Phrase-level certificate):** Certification algorithms remain sound when applied to phrase-level (m-token) voting over the transformed space V^m.\n\n4. **Theorem 4.8 (Collective certificate):** For any attack within global budget K, at least floor(N * A(K)) prompts maintain safe predictions.\n\nThe threat model assumes an **unbounded, white-box adversary** with access to architecture, dataset, training order, and hyperparameters, who can perform general poisoning of features, labels, or both, constrained only by |D symmetric_difference D_tilde| <= r.\n\n---\n\n### Relationship to RobustRAG\n\nThe paper explicitly distinguishes itself from RobustRAG (Xiang et al., 2024, \"Certifiably robust RAG against retrieval corruption\"). The authors state: **\"Unlike our focus on post-training poisoning, this research addresses retrieval corruption in Retrieval-Augmented Generation (RAG), where attackers corrupt retrieved documents rather than the model's (post-)training data.\"**\n\nKey differences:\n- **Threat model:** RobustRAG addresses **inference-time retrieval corruption** (adversary corrupts retrieved documents at test time). This paper addresses **training-time data poisoning** (adversary corrupts the training data before/during fine-tuning).\n- **Defense mechanism:** Both use isolate-then-aggregate strategies, but RobustRAG isolates retrieved passages and aggregates LLM responses, while this paper partitions training data into shards, trains independent models, and aggregates via majority voting.\n- **Certification target:** RobustRAG certifies that retrieval corruption cannot change outputs. This paper certifies that training data poisoning cannot induce specific harmful outputs (validity) or any output change (stability).\n\n---\n\n### Experimental Results\n\n**Models used:** OLMo-1B, OLMo-2-1B-Instruct, Gemma2-2B, Qwen1.5-4B\n\n**Datasets and settings:**\n\n1. **Agent Tool-Calling (MCP):** Toucan dataset (50K training instances, top 150 tools from real-world MCP environments), 500 shards.\n   - Full LoRA: median certified robustness r=249 (resists 0.5% dataset poisoning), accuracy 67% vs 40% zero-shot baseline, latency ~150s\n   - Last-3 LoRA: r=163, 5.9x speedup (latency ~25s)\n\n2. **Preference Alignment (HH-RLHF):** 20 shards across three models.\n   - DPA+ROE (stability): 42-54% First Token Stability at k=9\n   - TPA+MSC (validity): >90% First Token Validity at k=9, validity horizons of 21+ tokens\n   - Stability Horizon: 0.25-8.31 tokens depending on model and method\n\n3. **Empirical Attack Robustness:** Ensemble defense reduces backdoor attack success from 40-48% (single model) to <6%, with stealth scores >95%\n\n**Evaluation Metrics:**\n- First-Token Stability (FTS@k): fraction of prompts with unchanged first token under k-poisoning\n- First-Token Validity (FTV@k): fraction where first token cannot be changed to target harmful token\n- Stability Horizon (SH@k): average length of longest certified stable prefix\n- Validity Horizon (VH@k): average length before harmful sequence can be induced\n\n---\n\n### Limitations Acknowledged\n\n1. **Inference-time latency** remains \"an open challenge\" -- running hundreds of shard models is expensive (150s for Full LoRA with 500 shards).\n2. **Conservative bounds:** \"Although our certificates provide rigorous lower bounds, they are inherently conservative. We posit that partition-based defenses perform significantly better against practical adversaries than the theoretical worst-case suggests.\" The empirical results substantially exceed certified guarantees.\n3. **Narrow threat model:** \"Our certification framework addresses a specific threat model: training-time poisoning under worst-case assumptions. Other important threat modes -- such as test-time evasion, prompt-based attacks, and triggered backdoors -- remain critical open challenges.\"\n4. **Bounds do not eliminate vulnerabilities** from alternative attack surfaces.\n5. The stability-validity trade-off and the phrase-length trade-off (tight bounds vs. computational cost) are inherent tensions in the framework.\n\n---\n\n### Discussion/Reviews\n\nNo external reviews, blog posts, or social media discussions of this paper were found. The paper appears to be a recent preprint (February 2026) without yet appearing at a major venue. It is positioned in the lineage of Deep Partition Aggregation (DPA) by Levine & Feizi and Finite Aggregation by Rezaei et al., extending these classification-oriented certified defenses to the autoregressive NLG setting for the first time.\n\nSources:\n- [arXiv Abstract Page](https://arxiv.org/abs/2602.09757)\n- [arXiv HTML Version](https://arxiv.org/html/2602.09757)\n- [arXiv PDF](https://arxiv.org/pdf/2602.09757)\n- [Deep Partition Aggregation (Levine & Feizi)](https://arxiv.org/pdf/2006.14768)\n- [RobustRAG (Xiang et al.)](https://www.researchgate.net/publication/380895542_Certifiably_Robust_RAG_against_Retrieval_Corruption)"
      }
    ],
    "totalDurationMs": 180091,
    "totalTokens": 23761,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 682,
      "cache_creation_input_tokens": 1946,
      "cache_read_input_tokens": 18144,
      "output_tokens": 2989,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1946
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 682,
          "output_tokens": 2989,
          "cache_read_input_tokens": 18144,
          "cache_creation_input_tokens": 1946,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1946,
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
  "sourceToolAssistantUUID": "00de3b18-8d28-4b6d-aa29-906224d51656",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
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
  "leafUuid": "3ffa570e-c813-4856-82b1-28da5958d571",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze conformal prediction for adversarial RAG systems",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Tool call

_source line 19 · 2026-05-30T06:36:59.427Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01E5UFDryUc7njxfhLB4zF6Q`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze paper 4: RAG poisoning ICLR",
  "prompt": "Research the paper \"Understanding Data Poisoning Attacks for RAG: Insights and Algorithms\" by Xun Xian, Tong Wang, Liwen You, Yanjun Qi (ICLR 2025). URL: https://openreview.net/forum?id=2aL6gcFX7q\n\nTasks:\n1. Use WebFetch to read the OpenReview page (abstract, paper details, and reviewer comments)\n2. Use WebSearch to find the arxiv version if available\n3. Use WebFetch to read the full paper if available in HTML\n4. Collect all reviewer comments and scores\n\nReport back with:\n- The full abstract\n- Key method details: how they analyze why RAG poisoning works, what \"low-variance directions\" means, how the DRS (Directional Relative Shift) defense works, what the regularized attack is\n- Theoretical contributions\n- ALL reviewer comments, scores, and author responses\n- Limitations\n\nBe thorough — I need enough detail to write a precise technical analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ffa570e-c813-4856-82b1-28da5958d571",
  "isSidechain": false,
  "requestId": "req_011CbYHqhdZTXonJSdahodTd",
  "type": "assistant",
  "uuid": "d388f48a-ea7f-47df-a501-ace1ce141f0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012toh5aSJgJBjv38FDWHS1A",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3367,
      "cache_read_input_tokens": 21839,
      "output_tokens": 339,
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
          "output_tokens": 339,
          "cache_read_input_tokens": 21839,
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

_source line 20 · 2026-05-30T06:41:51.574Z_

<details><summary>↩ Tool result · `toolu_01E5UFDryUc7njxfhLB4zF6Q`</summary>

```text
Now I have all the information needed. Here is the comprehensive report.

---

## Full Report: "Understanding Data Poisoning Attacks for RAG: Insights and Algorithms"

**Authors:** Xun Xian, Tong Wang, Liwen You, Yanjun Qi
**Venue:** Submitted to ICLR 2025 Conference (Submission #12614)
**Final Decision:** **Rejected** (January 22, 2025)
**Arxiv version:** No separate arxiv posting was found. The paper appears to exist only on OpenReview.

---

### FULL ABSTRACT

Large Language Models (LLMs) have achieved success across various domains but also exhibit problematic issues, such as hallucinations. Retrieval-Augmented Generation (RAG) effectively alleviates these problems by incorporating external information to improve the factual accuracy of LLM-generated content. However, recent studies reveal that RAG systems are vulnerable to adversarial poisoning attacks, where attackers manipulate retrieval systems by poisoning the data corpus used for retrieval. These attacks raise serious safety concerns, as they can easily bypass existing defenses. In this work, we address these safety issues by first providing insights into the factors contributing to successful attacks. In particular, we show that more effective poisoning attacks tend to occur along directions where the clean data distribution exhibits small variances. Based on these insights, we propose two strategies. First, we introduce a new defense, named DRS (Directional Relative Shifts), which examines shifts along those directions where effective attacks are likely to occur. Second, we develop a new attack algorithm to generate more stealthy poisoning data (i.e., less detectable) by regularizing the poisoning data's DRS. We conducted extensive experiments across multiple application scenarios, including RAG Agent and dense passage retrieval for Q&A, to demonstrate the effectiveness of our proposed methods.

---

### KEY METHOD DETAILS

#### 1. Why RAG Poisoning Works: Theoretical Analysis

The paper frames all existing RAG attacks as **targeted data poisoning attacks against retrieval systems**. The attacker has two goals:
- **(a)** For adversarial queries, the retrieved documents should come from the poisoned corpus (so the LLM generates attacker-prescribed adversarial outputs).
- **(b)** For normal/clean queries, retrieval should exclude poisoned data (preserving normal utility).

These goals are formalized as two optimization objectives (Eq. 1 and Eq. 2 in the paper).

**Assumption 1 (Closeness):** The poisoned documents stay close to adversarial queries in embedding space. This is realistic -- e.g., PoisonedRAG appends poisoned text directly to adversarial queries.

**Theorem 1:** Under sub-Gaussian distributional assumptions on the clean corpus, the attackers' dual goals can be met by using adversarial queries that are sufficiently different from the normal query distribution.

**Corollary 1 (The Most Effective Directions for Attacks):** The most effective directions for attacks -- those that maximize both attacker objectives -- are the directions where the clean data distribution density decays fastest, i.e., the **low-variance directions**.

#### 2. What "Low-Variance Directions" Means

The paper performs eigendecomposition of the covariance matrix of clean document embeddings. Directions corresponding to **small eigenvalues** are the "low-variance directions." The key insight is:

- Low variance in a direction means probability mass is tightly concentrated around the mean in that direction.
- Even a small perturbation along such a direction greatly reduces the probability of clean documents being nearby.
- Therefore, adversarial queries placed along these directions will preferentially retrieve poisoned documents (not clean ones), achieving the attacker's goal.

This is empirically verified in **Figure 1**: they plot "relative distances" (relative mean divided by standard deviation) along the top-100 smallest-variance directions for three attacks (AgentPoison, BadChain, AutoDan) and clean documents. More effective attacks (AgentPoison) show larger relative shifts in these low-variance directions.

#### 3. DRS (Directional Relative Shifts) Defense

**Algorithm 1 -- Computing DRS Score:**
1. Eigendecompose the covariance matrix **S** of the standardized clean data matrix **X**: S = V Lambda V^T
2. Sort eigenvalues in ascending order (smallest first).
3. For a test document with embedding **z**, compute:

   DRS(z; X) = sum_{i=1}^{M} |z^T v_{sigma(i)}| / sqrt(lambda_{sigma(i)})

   where M is the number of low-variance directions to consider, v_{sigma(i)} is the eigenvector for the i-th smallest eigenvalue.

**Algorithm 2 -- Detection with DRS:**
1. For each protected query in set Q, retrieve top-K clean documents.
2. Compute DRS scores for all clean documents.
3. Set threshold tau as the q-th quantile (e.g., 99th percentile) of clean DRS scores.
4. Flag any future test document as adversarial if DRS(z; X_clean) > tau.

The defense assumes the defender has access to the retriever and a clean data corpus, and knows a set of queries to protect. The false positive rate is approximately 1% (by setting the threshold at the 99th percentile of clean scores).

#### 4. The Regularized Attack

When the attacker is aware of the DRS defense, they can add a DRS-regularization term to the original attack objective:

   min -O_1 + lambda_1 * O_2 + lambda_2 * **DRS scores on poisoned data**

where O_1 is the distance between clean and poisoned documents, O_2 is the within-poisoned-set distance, and lambda_2 > 0 controls the penalty for large DRS values. Since DRS computation involves only differentiable operations, gradient-based optimization still works.

The result is a trade-off: increasing lambda_2 makes poisoned data stealthier (lower DRS detection rate) but reduces attack success rate:

| lambda_2 | ASR | DRS Detection Rate |
|----------|------|-------------------|
| 0.1 | 0.78 | 0.99 |
| 0.5 | 0.76 | 0.85 |
| 1.0 | 0.70 | 0.72 |
| 5.0 | 0.51 | 0.51 |
| 10.0 | 0.42 | 0.29 |

---

### THEORETICAL CONTRIBUTIONS

1. **Theorem 1:** Under sub-Gaussian distributional assumptions on the clean data, the attacker's dual goals (retrieve poisoned data for adversarial queries, avoid retrieving poisoned data for clean queries) can be satisfied when adversarial queries are sufficiently different from the normal query distribution.

2. **Corollary 1:** The most effective attack directions are those with the fastest decaying density of the clean data distribution -- i.e., the low-variance directions (smallest eigenvalues of the covariance matrix).

3. **Remark 3 (Intuition):** Low variance means probability mass is concentrated around the mean. Any perturbation along such a direction drastically reduces the probability of clean documents being near the adversarial query, making poisoned documents dominate retrieval.

---

### EXPERIMENTAL RESULTS

**Defense evaluation (DRS vs. baselines)** across three scenarios:

**Attack I: RAG Agent (AgentPoison setup)**
- Tasks: Autonomous Driver, ReAct-StrategyQA
- DRS achieves 0.99 filtering rate across ALL attacks (AgentPoison, BadChain, AutoDan, GCG) vs. baselines (perplexity filter: 0.01-0.03, L2-norm filter: 0.02-0.34, L2-distance filter: 0.01-0.10)

**Attack II: Dense Passage Retrieval Q&A (BadDPR setup)**
- Backdoor ratios: 1%, 5%, 10%, 20%
- DRS achieves 0.49-0.65 (lower than RAG Agent scenario due to subtle grammatical-error-based poisoning) vs. baselines maxing at 0.36

**Attack III: Medical Q&A RAG (PoisonedRAG setup)**
- Retrievers: Contriever, MedCPT
- Datasets: MedQAUS, MedMCQA, PubMedQA
- DRS achieves 0.95-0.96 vs. baselines maxing at 0.90

**Proposed Attack evaluation:**
- AgentPoison detection rate drops from 0.99 to 0.85 with DRS regularization
- Applied to Backdoor DPR: detection drops from 0.65 to 0.52

---

### ALL REVIEWER COMMENTS, SCORES, AND AUTHOR RESPONSES

#### REVIEW 1: Reviewer_NLx3
- **Rating:** 5/10 | **Confidence:** 3/5

**Strengths:**
- Novel analysis and observations of poisoning attacks on RAG systems
- Comprehensive evaluation across four attack settings
- Thorough experimental assessment

**Weaknesses:**
1. Reliability concern: uncertain DRS effectiveness for semantically similar documents (e.g., "CEO is Sam Altman" vs. "CEO is Elon Musk")
2. Clarity issues: Figure 1 Y-axis undefined; Section 2.1 describes "only injecting poisoned data" but Section 5.1.2 involves backdoored retrievers; Section 5.1.1 lacks adversarial query descriptions; terminology unclear ("poisoned data samples" vs. "poisoned documents")
3. Unclear how large/diverse the clean dataset must be for DRS threshold computation

**Post-rebuttal:** Increased to 5 but maintained major concern that detection method is fundamentally challenged by semantically similar poisoned documents.

---

#### REVIEW 2: Reviewer_F894
- **Rating:** 5/10 (raised from initial score) | **Confidence:** 4/5

**Strengths:**
- Innovative DRS approach for detecting shifts in low-variance directions
- Extensive experiments across diverse applications
- Valuable theoretical insights connecting attack effectiveness to data distribution

**Weaknesses:**
1. Sparse theory: limited explanation for why specific dimensions are more vulnerable
2. Unrealistic assumptions: requires prior knowledge of queries needing protection; real-world defenders lack this knowledge
3. Unrealistic examples: food knowledge base attacked with mathematics queries doesn't reflect typical adversary behavior
4. Figure 1 claims about attack success rates not clearly shown in figure
5. Limited attack innovation: essentially adds regularization term to existing methods (incremental)
6. Incomplete evaluation: new attack's detection rates under DRS shown, but attack success rate comparisons missing

**Post-rebuttal:** Acknowledged rebuttal addressed "part of concerns."

---

#### REVIEW 3: Reviewer_bSEM
- **Rating:** 6/10 (raised after rebuttal) | **Confidence:** 3/5

**Strengths:**
- Deep understanding of existing attacks
- Well-written
- Simple yet effective defense

**Weaknesses:**
1. Missing references for perplexity-based filters and existing attacks
2. DRS similar to "Spectral Signatures in Backdoor Attacks" [Tran et al.] -- needs technical comparison beyond threat model differences
3. Limited evaluation: only AgentPoison tested for proposed attack
4. Modest performance: 14% detection rate reduction insufficient for escaping DRS
5. Limited attack diversity: should test against other RAG poisoning methods

**Questions:**
- Why not incorporate trigger designs from existing backdoor attacks?
- Can more diverse attack types be evaluated?

**Post-rebuttal:** Increased score, partly satisfied by additional Backdoor DPR experiments and technical differentiation from spectral signatures.

---

#### REVIEW 4: Reviewer_pzSQ
- **Rating:** 3/10 | **Confidence:** 4/5

**Strengths:**
- DRS metric is novel and effective for detecting poisoning
- Clear, well-structured presentation
- Theoretical and empirical results provided

**Weaknesses:**
1. Critical gap: missing attack success rates in experimental results
2. Insufficient detail on DRS computational costs
3. Weak justification for requiring access to clean documents
4. Insufficient detail on how low-variance features manifest in real-world documents; Figure 2 experimental settings unspecified
5. Missing sensitivity analysis for hyperparameters lambda_1 and lambda_2

**Questions:**
- How does RAG poisoning defense differ from jailbreak/prompt injection defenses?
- How many clean documents required for guarantees?
- What is the computational overhead?

---

#### AUTHOR REBUTTALS (Key Points)

**On DRS computation:** Lightweight -- SVD performed once offline; at test time requires only matrix-vector multiplications.

**On clean document access:** Framed as hypothesis testing -- without knowledge of clean distribution, optimal detector becomes random guessing. Analogy: "identifying red apples requires knowing what red looks like."

**On clean dataset size ablation:**
| Size | Detection Rate |
|------|----------------|
| 500 | 0.91 |
| 1000 | 0.97 |
| 1500 | 0.99 |

**On the "semantically similar documents" attack (key weakness):** Authors argued this creates a "fundamentally infeasible" detection problem. When clean and poisoned distributions overlap, Bayes Risk approaches 0.5. They empirically verified attack success rate drops to ~40% in such scenarios, contradicting the attacker's goals. "While such cases theoretically exist, they are unlikely to have significant impact on real implementations."

**On comparison to Spectral Signatures [Tran et al.]:** Different threat model -- DRS uses "localization property of KNN algorithm" without access to backdoor data (harder setting), while spectral signatures uses robust statistics with access to both clean and poisoned data.

**On attack diversity:** Applied DRS regularization to Backdoor DPR, reducing detection from 0.65 to 0.52.

---

#### META-REVIEW: Area Chair KySE
- **Decision:** Reject (December 20, 2024)
- Three negative reviews, one positive review (6/10).
- Major weakness: "Strong assumption that malicious and normal queries are fundamentally different, limiting defense against easily crafted attacks."
- Authors' rebuttal acknowledged theoretical limitations but didn't adequately resolve concerns.
- No reviewer championed the paper for acceptance.
- Suggestion to authors: "incorporate attacker's knowledge assumptions into threat model to justify the core assumption."

---

### LIMITATIONS

1. **Fundamental assumption vulnerability:** The defense assumes adversarial and normal queries are sufficiently different in embedding space. When poisoned documents are semantically similar to clean ones (differing only in factual content, e.g., entity substitution), DRS cannot distinguish them. This was the primary reason for rejection.

2. **Requires pre-specified protected query set:** The defender must know which queries to protect in advance, reducing practical applicability to scenarios where targeted queries can be anticipated.

3. **Requires access to clean corpus:** The defender needs a trusted set of clean documents to compute DRS thresholds.

4. **Attack algorithm novelty is limited:** The regularized attack simply adds a penalty term to existing objectives -- it's incremental rather than introducing fundamentally new attack techniques.

5. **Modest attack evasion:** The DRS-regularized attack only reduces detection by ~15% while maintaining comparable attack success rates. At higher regularization strengths, attack success rate degrades substantially.

6. **Lower performance on subtle attacks:** For attacks that only introduce minor grammatical changes (Backdoor DPR), DRS performance drops to 0.49-0.65 (vs. 0.99 for more aggressive attacks), suggesting the method is most effective against attacks that significantly shift embedding distributions.

7. **No arxiv version found:** The paper does not appear to have a public arxiv posting; it exists only as an OpenReview submission, suggesting limited dissemination.

8. **Missing from paper:** No sensitivity analysis for hyperparameters; no detailed computational cost analysis; no formal guarantee on minimum clean corpus size; attack success rates not reported alongside detection rates in all tables.

Sources:
- [OpenReview Forum](https://openreview.net/forum?id=2aL6gcFX7q)
- [OpenReview PDF](https://openreview.net/pdf?id=2aL6gcFX7q)
- [Related paper by Xun Xian: On the Vulnerability of Applying RAG](https://arxiv.org/abs/2409.17275)

agentId: a0896d6bdbbe1f13a (use SendMessage with to: 'a0896d6bdbbe1f13a' to continue this agent)
&lt;usage>total_tokens: 45314
tool_uses: 31
duration_ms: 292141&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d388f48a-ea7f-47df-a501-ace1ce141f0b",
  "isSidechain": false,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "type": "user",
  "uuid": "1ee12569-6f36-40f5-9a49-2c0cf862c51e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Understanding Data Poisoning Attacks for RAG: Insights and Algorithms\" by Xun Xian, Tong Wang, Liwen You, Yanjun Qi (ICLR 2025). URL: https://openreview.net/forum?id=2aL6gcFX7q\n\nTasks:\n1. Use WebFetch to read the OpenReview page (abstract, paper details, and reviewer comments)\n2. Use WebSearch to find the arxiv version if available\n3. Use WebFetch to read the full paper if available in HTML\n4. Collect all reviewer comments and scores\n\nReport back with:\n- The full abstract\n- Key method details: how they analyze why RAG poisoning works, what \"low-variance directions\" means, how the DRS (Directional Relative Shift) defense works, what the regularized attack is\n- Theoretical contributions\n- ALL reviewer comments, scores, and author responses\n- Limitations\n\nBe thorough — I need enough detail to write a precise technical analysis.",
    "agentId": "a0896d6bdbbe1f13a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information needed. Here is the comprehensive report.\n\n---\n\n## Full Report: \"Understanding Data Poisoning Attacks for RAG: Insights and Algorithms\"\n\n**Authors:** Xun Xian, Tong Wang, Liwen You, Yanjun Qi\n**Venue:** Submitted to ICLR 2025 Conference (Submission #12614)\n**Final Decision:** **Rejected** (January 22, 2025)\n**Arxiv version:** No separate arxiv posting was found. The paper appears to exist only on OpenReview.\n\n---\n\n### FULL ABSTRACT\n\nLarge Language Models (LLMs) have achieved success across various domains but also exhibit problematic issues, such as hallucinations. Retrieval-Augmented Generation (RAG) effectively alleviates these problems by incorporating external information to improve the factual accuracy of LLM-generated content. However, recent studies reveal that RAG systems are vulnerable to adversarial poisoning attacks, where attackers manipulate retrieval systems by poisoning the data corpus used for retrieval. These attacks raise serious safety concerns, as they can easily bypass existing defenses. In this work, we address these safety issues by first providing insights into the factors contributing to successful attacks. In particular, we show that more effective poisoning attacks tend to occur along directions where the clean data distribution exhibits small variances. Based on these insights, we propose two strategies. First, we introduce a new defense, named DRS (Directional Relative Shifts), which examines shifts along those directions where effective attacks are likely to occur. Second, we develop a new attack algorithm to generate more stealthy poisoning data (i.e., less detectable) by regularizing the poisoning data's DRS. We conducted extensive experiments across multiple application scenarios, including RAG Agent and dense passage retrieval for Q&A, to demonstrate the effectiveness of our proposed methods.\n\n---\n\n### KEY METHOD DETAILS\n\n#### 1. Why RAG Poisoning Works: Theoretical Analysis\n\nThe paper frames all existing RAG attacks as **targeted data poisoning attacks against retrieval systems**. The attacker has two goals:\n- **(a)** For adversarial queries, the retrieved documents should come from the poisoned corpus (so the LLM generates attacker-prescribed adversarial outputs).\n- **(b)** For normal/clean queries, retrieval should exclude poisoned data (preserving normal utility).\n\nThese goals are formalized as two optimization objectives (Eq. 1 and Eq. 2 in the paper).\n\n**Assumption 1 (Closeness):** The poisoned documents stay close to adversarial queries in embedding space. This is realistic -- e.g., PoisonedRAG appends poisoned text directly to adversarial queries.\n\n**Theorem 1:** Under sub-Gaussian distributional assumptions on the clean corpus, the attackers' dual goals can be met by using adversarial queries that are sufficiently different from the normal query distribution.\n\n**Corollary 1 (The Most Effective Directions for Attacks):** The most effective directions for attacks -- those that maximize both attacker objectives -- are the directions where the clean data distribution density decays fastest, i.e., the **low-variance directions**.\n\n#### 2. What \"Low-Variance Directions\" Means\n\nThe paper performs eigendecomposition of the covariance matrix of clean document embeddings. Directions corresponding to **small eigenvalues** are the \"low-variance directions.\" The key insight is:\n\n- Low variance in a direction means probability mass is tightly concentrated around the mean in that direction.\n- Even a small perturbation along such a direction greatly reduces the probability of clean documents being nearby.\n- Therefore, adversarial queries placed along these directions will preferentially retrieve poisoned documents (not clean ones), achieving the attacker's goal.\n\nThis is empirically verified in **Figure 1**: they plot \"relative distances\" (relative mean divided by standard deviation) along the top-100 smallest-variance directions for three attacks (AgentPoison, BadChain, AutoDan) and clean documents. More effective attacks (AgentPoison) show larger relative shifts in these low-variance directions.\n\n#### 3. DRS (Directional Relative Shifts) Defense\n\n**Algorithm 1 -- Computing DRS Score:**\n1. Eigendecompose the covariance matrix **S** of the standardized clean data matrix **X**: S = V Lambda V^T\n2. Sort eigenvalues in ascending order (smallest first).\n3. For a test document with embedding **z**, compute:\n\n   DRS(z; X) = sum_{i=1}^{M} |z^T v_{sigma(i)}| / sqrt(lambda_{sigma(i)})\n\n   where M is the number of low-variance directions to consider, v_{sigma(i)} is the eigenvector for the i-th smallest eigenvalue.\n\n**Algorithm 2 -- Detection with DRS:**\n1. For each protected query in set Q, retrieve top-K clean documents.\n2. Compute DRS scores for all clean documents.\n3. Set threshold tau as the q-th quantile (e.g., 99th percentile) of clean DRS scores.\n4. Flag any future test document as adversarial if DRS(z; X_clean) > tau.\n\nThe defense assumes the defender has access to the retriever and a clean data corpus, and knows a set of queries to protect. The false positive rate is approximately 1% (by setting the threshold at the 99th percentile of clean scores).\n\n#### 4. The Regularized Attack\n\nWhen the attacker is aware of the DRS defense, they can add a DRS-regularization term to the original attack objective:\n\n   min -O_1 + lambda_1 * O_2 + lambda_2 * **DRS scores on poisoned data**\n\nwhere O_1 is the distance between clean and poisoned documents, O_2 is the within-poisoned-set distance, and lambda_2 > 0 controls the penalty for large DRS values. Since DRS computation involves only differentiable operations, gradient-based optimization still works.\n\nThe result is a trade-off: increasing lambda_2 makes poisoned data stealthier (lower DRS detection rate) but reduces attack success rate:\n\n| lambda_2 | ASR | DRS Detection Rate |\n|----------|------|-------------------|\n| 0.1 | 0.78 | 0.99 |\n| 0.5 | 0.76 | 0.85 |\n| 1.0 | 0.70 | 0.72 |\n| 5.0 | 0.51 | 0.51 |\n| 10.0 | 0.42 | 0.29 |\n\n---\n\n### THEORETICAL CONTRIBUTIONS\n\n1. **Theorem 1:** Under sub-Gaussian distributional assumptions on the clean data, the attacker's dual goals (retrieve poisoned data for adversarial queries, avoid retrieving poisoned data for clean queries) can be satisfied when adversarial queries are sufficiently different from the normal query distribution.\n\n2. **Corollary 1:** The most effective attack directions are those with the fastest decaying density of the clean data distribution -- i.e., the low-variance directions (smallest eigenvalues of the covariance matrix).\n\n3. **Remark 3 (Intuition):** Low variance means probability mass is concentrated around the mean. Any perturbation along such a direction drastically reduces the probability of clean documents being near the adversarial query, making poisoned documents dominate retrieval.\n\n---\n\n### EXPERIMENTAL RESULTS\n\n**Defense evaluation (DRS vs. baselines)** across three scenarios:\n\n**Attack I: RAG Agent (AgentPoison setup)**\n- Tasks: Autonomous Driver, ReAct-StrategyQA\n- DRS achieves 0.99 filtering rate across ALL attacks (AgentPoison, BadChain, AutoDan, GCG) vs. baselines (perplexity filter: 0.01-0.03, L2-norm filter: 0.02-0.34, L2-distance filter: 0.01-0.10)\n\n**Attack II: Dense Passage Retrieval Q&A (BadDPR setup)**\n- Backdoor ratios: 1%, 5%, 10%, 20%\n- DRS achieves 0.49-0.65 (lower than RAG Agent scenario due to subtle grammatical-error-based poisoning) vs. baselines maxing at 0.36\n\n**Attack III: Medical Q&A RAG (PoisonedRAG setup)**\n- Retrievers: Contriever, MedCPT\n- Datasets: MedQAUS, MedMCQA, PubMedQA\n- DRS achieves 0.95-0.96 vs. baselines maxing at 0.90\n\n**Proposed Attack evaluation:**\n- AgentPoison detection rate drops from 0.99 to 0.85 with DRS regularization\n- Applied to Backdoor DPR: detection drops from 0.65 to 0.52\n\n---\n\n### ALL REVIEWER COMMENTS, SCORES, AND AUTHOR RESPONSES\n\n#### REVIEW 1: Reviewer_NLx3\n- **Rating:** 5/10 | **Confidence:** 3/5\n\n**Strengths:**\n- Novel analysis and observations of poisoning attacks on RAG systems\n- Comprehensive evaluation across four attack settings\n- Thorough experimental assessment\n\n**Weaknesses:**\n1. Reliability concern: uncertain DRS effectiveness for semantically similar documents (e.g., \"CEO is Sam Altman\" vs. \"CEO is Elon Musk\")\n2. Clarity issues: Figure 1 Y-axis undefined; Section 2.1 describes \"only injecting poisoned data\" but Section 5.1.2 involves backdoored retrievers; Section 5.1.1 lacks adversarial query descriptions; terminology unclear (\"poisoned data samples\" vs. \"poisoned documents\")\n3. Unclear how large/diverse the clean dataset must be for DRS threshold computation\n\n**Post-rebuttal:** Increased to 5 but maintained major concern that detection method is fundamentally challenged by semantically similar poisoned documents.\n\n---\n\n#### REVIEW 2: Reviewer_F894\n- **Rating:** 5/10 (raised from initial score) | **Confidence:** 4/5\n\n**Strengths:**\n- Innovative DRS approach for detecting shifts in low-variance directions\n- Extensive experiments across diverse applications\n- Valuable theoretical insights connecting attack effectiveness to data distribution\n\n**Weaknesses:**\n1. Sparse theory: limited explanation for why specific dimensions are more vulnerable\n2. Unrealistic assumptions: requires prior knowledge of queries needing protection; real-world defenders lack this knowledge\n3. Unrealistic examples: food knowledge base attacked with mathematics queries doesn't reflect typical adversary behavior\n4. Figure 1 claims about attack success rates not clearly shown in figure\n5. Limited attack innovation: essentially adds regularization term to existing methods (incremental)\n6. Incomplete evaluation: new attack's detection rates under DRS shown, but attack success rate comparisons missing\n\n**Post-rebuttal:** Acknowledged rebuttal addressed \"part of concerns.\"\n\n---\n\n#### REVIEW 3: Reviewer_bSEM\n- **Rating:** 6/10 (raised after rebuttal) | **Confidence:** 3/5\n\n**Strengths:**\n- Deep understanding of existing attacks\n- Well-written\n- Simple yet effective defense\n\n**Weaknesses:**\n1. Missing references for perplexity-based filters and existing attacks\n2. DRS similar to \"Spectral Signatures in Backdoor Attacks\" [Tran et al.] -- needs technical comparison beyond threat model differences\n3. Limited evaluation: only AgentPoison tested for proposed attack\n4. Modest performance: 14% detection rate reduction insufficient for escaping DRS\n5. Limited attack diversity: should test against other RAG poisoning methods\n\n**Questions:**\n- Why not incorporate trigger designs from existing backdoor attacks?\n- Can more diverse attack types be evaluated?\n\n**Post-rebuttal:** Increased score, partly satisfied by additional Backdoor DPR experiments and technical differentiation from spectral signatures.\n\n---\n\n#### REVIEW 4: Reviewer_pzSQ\n- **Rating:** 3/10 | **Confidence:** 4/5\n\n**Strengths:**\n- DRS metric is novel and effective for detecting poisoning\n- Clear, well-structured presentation\n- Theoretical and empirical results provided\n\n**Weaknesses:**\n1. Critical gap: missing attack success rates in experimental results\n2. Insufficient detail on DRS computational costs\n3. Weak justification for requiring access to clean documents\n4. Insufficient detail on how low-variance features manifest in real-world documents; Figure 2 experimental settings unspecified\n5. Missing sensitivity analysis for hyperparameters lambda_1 and lambda_2\n\n**Questions:**\n- How does RAG poisoning defense differ from jailbreak/prompt injection defenses?\n- How many clean documents required for guarantees?\n- What is the computational overhead?\n\n---\n\n#### AUTHOR REBUTTALS (Key Points)\n\n**On DRS computation:** Lightweight -- SVD performed once offline; at test time requires only matrix-vector multiplications.\n\n**On clean document access:** Framed as hypothesis testing -- without knowledge of clean distribution, optimal detector becomes random guessing. Analogy: \"identifying red apples requires knowing what red looks like.\"\n\n**On clean dataset size ablation:**\n| Size | Detection Rate |\n|------|----------------|\n| 500 | 0.91 |\n| 1000 | 0.97 |\n| 1500 | 0.99 |\n\n**On the \"semantically similar documents\" attack (key weakness):** Authors argued this creates a \"fundamentally infeasible\" detection problem. When clean and poisoned distributions overlap, Bayes Risk approaches 0.5. They empirically verified attack success rate drops to ~40% in such scenarios, contradicting the attacker's goals. \"While such cases theoretically exist, they are unlikely to have significant impact on real implementations.\"\n\n**On comparison to Spectral Signatures [Tran et al.]:** Different threat model -- DRS uses \"localization property of KNN algorithm\" without access to backdoor data (harder setting), while spectral signatures uses robust statistics with access to both clean and poisoned data.\n\n**On attack diversity:** Applied DRS regularization to Backdoor DPR, reducing detection from 0.65 to 0.52.\n\n---\n\n#### META-REVIEW: Area Chair KySE\n- **Decision:** Reject (December 20, 2024)\n- Three negative reviews, one positive review (6/10).\n- Major weakness: \"Strong assumption that malicious and normal queries are fundamentally different, limiting defense against easily crafted attacks.\"\n- Authors' rebuttal acknowledged theoretical limitations but didn't adequately resolve concerns.\n- No reviewer championed the paper for acceptance.\n- Suggestion to authors: \"incorporate attacker's knowledge assumptions into threat model to justify the core assumption.\"\n\n---\n\n### LIMITATIONS\n\n1. **Fundamental assumption vulnerability:** The defense assumes adversarial and normal queries are sufficiently different in embedding space. When poisoned documents are semantically similar to clean ones (differing only in factual content, e.g., entity substitution), DRS cannot distinguish them. This was the primary reason for rejection.\n\n2. **Requires pre-specified protected query set:** The defender must know which queries to protect in advance, reducing practical applicability to scenarios where targeted queries can be anticipated.\n\n3. **Requires access to clean corpus:** The defender needs a trusted set of clean documents to compute DRS thresholds.\n\n4. **Attack algorithm novelty is limited:** The regularized attack simply adds a penalty term to existing objectives -- it's incremental rather than introducing fundamentally new attack techniques.\n\n5. **Modest attack evasion:** The DRS-regularized attack only reduces detection by ~15% while maintaining comparable attack success rates. At higher regularization strengths, attack success rate degrades substantially.\n\n6. **Lower performance on subtle attacks:** For attacks that only introduce minor grammatical changes (Backdoor DPR), DRS performance drops to 0.49-0.65 (vs. 0.99 for more aggressive attacks), suggesting the method is most effective against attacks that significantly shift embedding distributions.\n\n7. **No arxiv version found:** The paper does not appear to have a public arxiv posting; it exists only as an OpenReview submission, suggesting limited dissemination.\n\n8. **Missing from paper:** No sensitivity analysis for hyperparameters; no detailed computational cost analysis; no formal guarantee on minimum clean corpus size; attack success rates not reported alongside detection rates in all tables.\n\nSources:\n- [OpenReview Forum](https://openreview.net/forum?id=2aL6gcFX7q)\n- [OpenReview PDF](https://openreview.net/pdf?id=2aL6gcFX7q)\n- [Related paper by Xun Xian: On the Vulnerability of Applying RAG](https://arxiv.org/abs/2409.17275)"
      }
    ],
    "totalDurationMs": 292141,
    "totalTokens": 45314,
    "totalToolUseCount": 31,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 40654,
      "output_tokens": 3960,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 699
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3960,
          "cache_read_input_tokens": 40654,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 699,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 6,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "d388f48a-ea7f-47df-a501-ace1ce141f0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
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
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "1ee12569-6f36-40f5-9a49-2c0cf862c51e",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze conformal prediction for adversarial RAG systems",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Tool call

_source line 23 · 2026-05-30T06:42:02.529Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TpFDBwv47GhYKmY7v2KH3r`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Analyze paper 5: GASLITE attack",
  "prompt": "Research the paper \"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search\" by Matan Ben-Tov, Mahmood Sharif (ACM CCS 2025). URL: https://arxiv.org/abs/2412.20953\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full PDF or HTML version if available\n3. Search the web for any reviews, discussions, or conference proceedings info\n\nReport back with:\n- The full abstract\n- Key method details: how GASLITE generates adversarial passages without model/corpus knowledge, how single-query attacks achieve 100% success, what makes standard defenses fail against adaptive versions, what the 0.0001% corpus poisoning rate means\n- The threat model and assumptions\n- Experimental results and key findings\n- Limitations acknowledged\n\nBe thorough — I need enough detail to write a precise technical analysis."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ee12569-6f36-40f5-9a49-2c0cf862c51e",
  "isSidechain": false,
  "requestId": "req_011CbYJDxZMd7EjFabybPxk5",
  "type": "assistant",
  "uuid": "0e8cdb64-440b-4512-90fb-5e9f49aa2895",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018cW1bXtvaSG74do4JRq5pU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4377,
      "cache_read_input_tokens": 25206,
      "output_tokens": 321,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4377,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 321,
          "cache_read_input_tokens": 25206,
          "cache_creation_input_tokens": 4377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4377
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

_source line 24 · 2026-05-30T06:45:57.114Z_

<details><summary>↩ Tool result · `toolu_01TpFDBwv47GhYKmY7v2KH3r`</summary>

````text
I now have comprehensive information to provide a thorough technical analysis. Here is my detailed report.

---

## GASLITE: Full Technical Research Summary

**Paper:** "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search"
**Authors:** Matan Ben-Tov, Mahmood Sharif (Tel Aviv University)
**Venue:** ACM CCS 2025 (Conference on Computer and Communications Security)
**DOI:** 10.1145/3719027.3765095
**arXiv:** 2412.20953 (v1: Dec 30, 2024; v2: Sep 18, 2025)
**Code:** https://github.com/matanbt/gaslite

---

### Full Abstract

Dense embedding-based text retrieval -- retrieving relevant passages from corpora via deep learning encodings -- has become powerful for achieving state-of-the-art search and popularizing Retrieval Augmented Generation (RAG). However, embedding-based retrieval may face search-engine optimization (SEO) attacks where adversaries introduce malicious passages to promote harmful content. Prior work demonstrated such vulnerabilities but employed relaxed threat models, baseline methods, and limited evaluations. This research provides a comprehensive robustness assessment of retrievers to uncover susceptibility factors. The authors propose GASLITE, an attack generating adversarial passages that embed adversary-chosen information without corpus content reliance or model modification, consistently outperforming prior approaches. Extensive evaluation of nine advanced models across varied threat models reveals retrievers face high vulnerability to SEO attacks targeting concept-specific queries, even with negligible poisoning rates (>=0.0001% of corpus), generalizing across corpora and query distributions. Single-query SEO is fully solved by GASLITE, while adaptive attacks bypass common defenses.

---

### Threat Model and Assumptions

**Attacker Goals (dual objective):**
1. **Visibility:** Maximize probability that adversarial passages appear in top-k retrieval results.
2. **Informativeness:** Ensure crafted passages convey attacker-chosen content (e.g., misinformation, promotional material).

**Attacker Capabilities:**
- Can insert adversarial text passages into the retrieval corpus (e.g., via public wikis, web crawling targets, open forums).
- Controls passage text content but not tokenization directly.
- Poisoning budget is negligible: |P_adv| << |P| (e.g., 10 passages in an 8.8M passage corpus = 0.0001%).
- **White-box access** to model weights -- justified by the prevalence of open-source embedding models (Contriever, E5, etc. are all publicly available on HuggingFace).
- **Cannot** modify model weights, access the existing corpus content, or read ground-truth relevance labels.

**Three Query Distribution Settings:**

1. **"Knows All":** Attacker targets a known finite query set Q (often |Q|=1). This is the classic single-query SEO setting. Represents the easiest attack scenario.

2. **"Knows What" (primary focus):** Attacker targets a specific concept (e.g., "Harry Potter") with infinite possible query support but only a finite sample Q available for optimization. Reflects realistic SEO where the attacker knows the topic domain but not the exact queries users will issue. This is the paper's central contribution.

3. **"Knows [Almost] Nothing":** Indiscriminate targeting across diverse, unrelated query distributions. The hardest setting, requiring broad generalization.

---

### Method: How GASLITE Works

**Core Mathematical Objective (Eq. 2):**

```
arg max_{p_adv}  (1/|Q| * sum_{q in Q} Emb_R(q)) . Emb_R(p_adv)
```

This maximizes the dot product between the adversarial passage embedding and the centroid of the target query embeddings. The key insight: optimal adversarial passages should align with the "average" semantic direction of the targeted query cluster.

**Passage Structure:**
Each adversarial passage is constructed as `p_adv := info || trigger`, where:
- `info` is a fixed prefix containing the attacker's chosen malicious information (exploiting the primacy effect -- readers attend more to early content).
- `trigger` is a suffix of 100 tokens that GASLITE optimizes to maximize retrieval ranking.

**Algorithm (multi-coordinate gradient-based discrete optimization):**

Hyperparameters: n_iter=100, n_grad=50, n_cand=128, n_flip=20, trigger length=100 tokens.

Per iteration:
1. Sample n_grad=50 random single-token flip variants of the current trigger.
2. Average the linear approximations (gradients) across these samples per token position -- this is a refined gradient approximation superior to single-point HotFlip.
3. Randomly select n_flip=20 token positions for simultaneous substitution.
4. For each position, use gradient information to identify n_cand=128 promising token candidates.
5. Filter candidates that cause tokenization irreversibilities (the "ReTokenize" step -- see below).
6. Greedily select the best substitution that maximizes the objective.
7. Update the trigger.

**Three Key Engineering Innovations Over Prior Work (HotFlip/Cor.Pois.):**

1. **Multi-token greedy search:** Flips multiple tokens per iteration rather than one, reducing backward passes by ~20x compared to standard HotFlip.

2. **Refined gradient approximation:** Averages linear approximations across n_grad=50 random token-substitution samples, yielding more reliable gradients in the discrete token space.

3. **Text coherence maintenance (ReTokenize):** This is the critical practical contribution. Different token sequences can decode to identical text strings. Prior work (Cor.Pois./Zhong et al. 2023) optimized in token space but inserted text into the corpus -- the re-tokenization of decoded text could produce different tokens than what was optimized, causing substantial objective degradation. GASLITE explicitly filters out token substitutions that would be inconsistent after a text-to-tokens-to-text round trip. This is identified as the primary reason Cor.Pois. underperforms.

**Multi-Budget Extension (B > 1 adversarial passages):**
Finding the optimal partition of queries into B subsets is NP-Hard (proven via reduction to Set Cover). GASLITE uses k-means clustering on query embeddings to partition the target query set into B clusters, then optimizes one adversarial passage per cluster centroid. K-means was empirically superior to greedy set-cover approximation.

**Runtime:** GASLITE converges in ~2-3 minutes per passage, versus 30-45 minutes for Cor.Pois. -- a 10-15x speedup while achieving 40%+ better success rates.

---

### How Single-Query Attacks Achieve 100% Success

In the "Knows All" setting with |Q|=1, the optimization objective reduces to maximizing the dot product between one query embedding and the adversarial passage embedding. The discrete nature of a single target query means the optimization can achieve near-perfect alignment in embedding space. GASLITE achieves **100% appeared@1** (top-1 result) across all nine evaluated models. This is described as "fully solved" -- the adversarial passage consistently becomes the single highest-ranked result for the target query.

Comparative performance for single-query:
- Info Only (no optimization): 0% success
- Stuffing (repeat the query text): 30-96% appeared@10, model-dependent
- Cor.Pois. (prior SOTA): sometimes worse than stuffing due to tokenization issues
- GASLITE: 100% appeared@1, all models

For dot-product models like Contriever, GASLITE achieves similarity scores of 3.453 +/- 0.350, roughly 2x what baseline methods achieve.

---

### What the 0.0001% Corpus Poisoning Rate Means

The primary corpus is MSMARCO with 8.8 million passages. A budget of 10 adversarial passages represents 10/8,800,000 = ~0.0001% of the corpus. At this poisoning rate:

- GASLITE achieves >50% appeared@10 on 6 out of 9 models for unseen concept-specific queries.
- Appeared@10 ranges from 61-100% on most models (the 61-100% figure cited in the abstract).
- This represents an astronomically small injection that is practically undetectable by volume-based monitoring.

Scaling with budget (concept-specific, averaged across models):
- 1 passage: ~30% appeared@10
- 5 passages: ~48% appeared@10
- 10 passages: ~62% appeared@10
- 100% appeared@100 achieved on all models with just 10 passages

---

### What Makes Standard Defenses Fail Against Adaptive Versions

**Defense 1 -- Perplexity Filtering:**
- Rationale: GASLITE triggers are syntactically incoherent (e.g., "So wizard tickets ideally ages Radcliffe trilogy typically 194 movies"), so they exhibit high perplexity (~100-150 bits vs. normal ~50-80).
- Defense: Filter passages exceeding a perplexity threshold (>10 bits).
- **Adaptive bypass:** GASLITE integrates a perplexity penalty term into its optimization objective, constraining the trigger to remain within natural perplexity ranges.
- Result: Adaptive variant achieves 58% appeared@10 vs. 62% baseline -- only a 4 percentage-point drop. Defense is effectively neutralized.

**Defense 2 -- Embedding L2-Norm Filtering:**
- Rationale: Adversarial passages may have abnormal embedding norms.
- Defense: Filter passages with L2 norm exceeding a threshold (>0.8).
- **Adaptive bypass:** GASLITE adds an L2-norm constraint to optimization, keeping embeddings within natural norm distributions.
- Result: 60% appeared@10 vs. 62% baseline -- only 2 percentage-point drop.

The fundamental problem: both defenses rely on statistical anomaly detection (perplexity, norm), which can be incorporated as constraints in the attacker's optimization without significant performance loss. The paper concludes that "deeper defenses are needed" beyond surface-level filtering.

---

### Experimental Results and Key Findings

**Models Evaluated (9 total):**
- Cosine-similarity models: E5, MiniLM, GTR-T5, aMPNet, Arctic
- Dot-product models: Contriever, Contriever-MS, ANCE, mMPNet

**Key Quantitative Results:**

| Setting | Budget | GASLITE appeared@10 | Best Baseline | Improvement |
|---------|--------|---------------------|---------------|-------------|
| Knows All (single query) | 1 | 100% (@1) | 30-96% (@10) | Fully solved |
| Knows What (concept) | 10 | 61-100% | ~25% (Cor.Pois.) | >140% |
| Knows Nothing (diverse) | 100 | 5-20% | <6% (Cor.Pois.) | Significant |

**Model Vulnerability Variance (concept-specific, 1 passage):**
- Contriever (dot-product, high anisotropy): ~100% appeared@10
- E5 (cosine, moderate anisotropy): ~70%
- Arctic (cosine, low anisotropy): ~20%
- 5-fold difference in susceptibility across models

**Vulnerability Factors Identified:**
1. **Similarity metric:** Dot-product models are significantly more vulnerable than cosine-similarity models. Dot-product doesn't normalize embedding magnitudes, allowing adversarial passages to achieve disproportionately high scores.
2. **Embedding space anisotropy:** Models with higher anisotropy (embeddings concentrated in narrow directional subspaces) are more exploitable. Anisotropy is measured via eigenvalue distributions of embedding matrices. In anisotropic spaces, adversarial passages can achieve high similarity without semantic naturalness.

**Cross-Dataset Generalization:**
- GASLITE passages optimized on MSMARCO queries generalize to NQ, SciFact, FiQA2018, and Quora queries.
- Topic-specific datasets see higher transfer success (30-40%) than generic evaluation sets (5-15%).

**Cross-Architecture Generalization:**
- Successfully attacks LLM-based embeddings (Stella-1.5B with ~1.5B parameters), indicating broad applicability beyond BERT-scale models.

**Black-Box Transferability:**
- Limited: attacks trained on one model transfer with only 25-60% relative effectiveness to other models.
- White-box access substantially improves attack success -- this is why the white-box threat model is important.

**RAG Case Study:**
- Tested on an actual RAG pipeline (OpenWebUI + Chroma vector store).
- With 10 adversarial passages targeting Harry Potter queries:
  - 73% of queries returned adversarial passages in top-3 retrieved context.
  - LLM generated misleading responses in 58% of cases.
  - 100% appearance rate in top-10 retrieval without defenses.

---

### Limitations Acknowledged

1. **White-box assumption:** While justified by open-source prevalence, real deployments may use proprietary models (OpenAI, Cohere) where white-box access is unavailable. Black-box transferability is limited.
2. **Concept knowledge required:** "Knows What" attacks require a sample of concept-related queries. Fully unknown attack distributions ("Knows Nothing") remain significantly harder (5-20% vs. 61-100%).
3. **Static corpus assumption:** Real corpora are constantly updated; adversarial passages could be diluted or removed over time.
4. **No corpus read-access:** Attacker cannot verify insertion success or monitor detection.
5. **Trigger naturalness:** Despite perplexity-constrained variants, triggers remain syntactically odd. Future content moderation systems might flag them on other grounds.
6. **English only:** Multilingual robustness is unexplored.
7. **Trigger length:** 100 tokens is somewhat arbitrary; the sensitivity to this parameter is not exhaustively studied.
8. **Model evolution:** Techniques may become less effective as embedding models improve and potentially incorporate adversarial training.

---

### Additional Context

**Why Cor.Pois. (Zhong et al. 2023) Underperforms:**
The prior state-of-the-art (1) assumed access to corpus content and ground-truth passages (more relaxed threat model), (2) used single-token HotFlip without multi-coordinate optimization, and (3) critically, did not handle the token-to-text irreversibility problem. When optimized token sequences are decoded to text and re-tokenized for corpus insertion, the resulting tokens can differ from what was optimized, causing substantial degradation. This single issue accounts for much of the performance gap.

**The paper's core contribution** is framed not as a novel mathematical formulation (the objective is straightforward dot-product maximization) but as a principled engineering solution: correctly solving discrete optimization in text space while maintaining token-text consistency, combined with the first comprehensive evaluation across realistic threat models and diverse models.

**Subsequent citing work** includes "Semantic Chameleon" (2025), "SilentRetrieval" (2025), and "Unsupervised Corpus Poisoning Attacks in Continuous Space" (SIGIR 2025), indicating the paper has catalyzed follow-up research in RAG security.

---

Sources:
- [arXiv Abstract](https://arxiv.org/abs/2412.20953)
- [arXiv HTML Full Paper](https://arxiv.org/html/2412.20953v2)
- [ACM DL Proceedings](https://dl.acm.org/doi/10.1145/3719027.3765095)
- [GitHub Repository](https://github.com/matanbt/gaslite)
- [MarkTechPost Coverage](https://www.marktechpost.com/2025/01/06/this-ai-paper-from-tel-aviv-university-introduces-gaslite-a-gradient-based-method-to-expose-vulnerabilities-in-dense-embedding-based-text-retrieval-systems/)
- [Mahmood Sharif's Faculty Page](https://mahmoods01.github.io/authors/matan-ben-tov/)

agentId: aee0facf533f0579b (use SendMessage with to: 'aee0facf533f0579b' to continue this agent)
&lt;usage>total_tokens: 26401
tool_uses: 12
duration_ms: 234579&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "0e8cdb64-440b-4512-90fb-5e9f49aa2895",
  "isSidechain": false,
  "promptId": "8bb76d2c-f20e-4763-b7f2-50f9ed2a1a5e",
  "type": "user",
  "uuid": "b3331ac4-664b-4eb3-bfb4-f2d8ff35b04e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search\" by Matan Ben-Tov, Mahmood Sharif (ACM CCS 2025). URL: https://arxiv.org/abs/2412.20953\n\nTasks:\n1. Use WebFetch to read the arxiv abstract page\n2. Use WebFetch to read the full PDF or HTML version if available\n3. Search the web for any reviews, discussions, or conference proceedings info\n\nReport back with:\n- The full abstract\n- Key method details: how GASLITE generates adversarial passages without model/corpus knowledge, how single-query attacks achieve 100% success, what makes standard defenses fail against adaptive versions, what the 0.0001% corpus poisoning rate means\n- The threat model and assumptions\n- Experimental results and key findings\n- Limitations acknowledged\n\nBe thorough — I need enough detail to write a precise technical analysis.",
    "agentId": "aee0facf533f0579b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information to provide a thorough technical analysis. Here is my detailed report.\n\n---\n\n## GASLITE: Full Technical Research Summary\n\n**Paper:** \"GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search\"\n**Authors:** Matan Ben-Tov, Mahmood Sharif (Tel Aviv University)\n**Venue:** ACM CCS 2025 (Conference on Computer and Communications Security)\n**DOI:** 10.1145/3719027.3765095\n**arXiv:** 2412.20953 (v1: Dec 30, 2024; v2: Sep 18, 2025)\n**Code:** https://github.com/matanbt/gaslite\n\n---\n\n### Full Abstract\n\nDense embedding-based text retrieval -- retrieving relevant passages from corpora via deep learning encodings -- has become powerful for achieving state-of-the-art search and popularizing Retrieval Augmented Generation (RAG). However, embedding-based retrieval may face search-engine optimization (SEO) attacks where adversaries introduce malicious passages to promote harmful content. Prior work demonstrated such vulnerabilities but employed relaxed threat models, baseline methods, and limited evaluations. This research provides a comprehensive robustness assessment of retrievers to uncover susceptibility factors. The authors propose GASLITE, an attack generating adversarial passages that embed adversary-chosen information without corpus content reliance or model modification, consistently outperforming prior approaches. Extensive evaluation of nine advanced models across varied threat models reveals retrievers face high vulnerability to SEO attacks targeting concept-specific queries, even with negligible poisoning rates (>=0.0001% of corpus), generalizing across corpora and query distributions. Single-query SEO is fully solved by GASLITE, while adaptive attacks bypass common defenses.\n\n---\n\n### Threat Model and Assumptions\n\n**Attacker Goals (dual objective):**\n1. **Visibility:** Maximize probability that adversarial passages appear in top-k retrieval results.\n2. **Informativeness:** Ensure crafted passages convey attacker-chosen content (e.g., misinformation, promotional material).\n\n**Attacker Capabilities:**\n- Can insert adversarial text passages into the retrieval corpus (e.g., via public wikis, web crawling targets, open forums).\n- Controls passage text content but not tokenization directly.\n- Poisoning budget is negligible: |P_adv| << |P| (e.g., 10 passages in an 8.8M passage corpus = 0.0001%).\n- **White-box access** to model weights -- justified by the prevalence of open-source embedding models (Contriever, E5, etc. are all publicly available on HuggingFace).\n- **Cannot** modify model weights, access the existing corpus content, or read ground-truth relevance labels.\n\n**Three Query Distribution Settings:**\n\n1. **\"Knows All\":** Attacker targets a known finite query set Q (often |Q|=1). This is the classic single-query SEO setting. Represents the easiest attack scenario.\n\n2. **\"Knows What\" (primary focus):** Attacker targets a specific concept (e.g., \"Harry Potter\") with infinite possible query support but only a finite sample Q available for optimization. Reflects realistic SEO where the attacker knows the topic domain but not the exact queries users will issue. This is the paper's central contribution.\n\n3. **\"Knows [Almost] Nothing\":** Indiscriminate targeting across diverse, unrelated query distributions. The hardest setting, requiring broad generalization.\n\n---\n\n### Method: How GASLITE Works\n\n**Core Mathematical Objective (Eq. 2):**\n\n```\narg max_{p_adv}  (1/|Q| * sum_{q in Q} Emb_R(q)) . Emb_R(p_adv)\n```\n\nThis maximizes the dot product between the adversarial passage embedding and the centroid of the target query embeddings. The key insight: optimal adversarial passages should align with the \"average\" semantic direction of the targeted query cluster.\n\n**Passage Structure:**\nEach adversarial passage is constructed as `p_adv := info || trigger`, where:\n- `info` is a fixed prefix containing the attacker's chosen malicious information (exploiting the primacy effect -- readers attend more to early content).\n- `trigger` is a suffix of 100 tokens that GASLITE optimizes to maximize retrieval ranking.\n\n**Algorithm (multi-coordinate gradient-based discrete optimization):**\n\nHyperparameters: n_iter=100, n_grad=50, n_cand=128, n_flip=20, trigger length=100 tokens.\n\nPer iteration:\n1. Sample n_grad=50 random single-token flip variants of the current trigger.\n2. Average the linear approximations (gradients) across these samples per token position -- this is a refined gradient approximation superior to single-point HotFlip.\n3. Randomly select n_flip=20 token positions for simultaneous substitution.\n4. For each position, use gradient information to identify n_cand=128 promising token candidates.\n5. Filter candidates that cause tokenization irreversibilities (the \"ReTokenize\" step -- see below).\n6. Greedily select the best substitution that maximizes the objective.\n7. Update the trigger.\n\n**Three Key Engineering Innovations Over Prior Work (HotFlip/Cor.Pois.):**\n\n1. **Multi-token greedy search:** Flips multiple tokens per iteration rather than one, reducing backward passes by ~20x compared to standard HotFlip.\n\n2. **Refined gradient approximation:** Averages linear approximations across n_grad=50 random token-substitution samples, yielding more reliable gradients in the discrete token space.\n\n3. **Text coherence maintenance (ReTokenize):** This is the critical practical contribution. Different token sequences can decode to identical text strings. Prior work (Cor.Pois./Zhong et al. 2023) optimized in token space but inserted text into the corpus -- the re-tokenization of decoded text could produce different tokens than what was optimized, causing substantial objective degradation. GASLITE explicitly filters out token substitutions that would be inconsistent after a text-to-tokens-to-text round trip. This is identified as the primary reason Cor.Pois. underperforms.\n\n**Multi-Budget Extension (B > 1 adversarial passages):**\nFinding the optimal partition of queries into B subsets is NP-Hard (proven via reduction to Set Cover). GASLITE uses k-means clustering on query embeddings to partition the target query set into B clusters, then optimizes one adversarial passage per cluster centroid. K-means was empirically superior to greedy set-cover approximation.\n\n**Runtime:** GASLITE converges in ~2-3 minutes per passage, versus 30-45 minutes for Cor.Pois. -- a 10-15x speedup while achieving 40%+ better success rates.\n\n---\n\n### How Single-Query Attacks Achieve 100% Success\n\nIn the \"Knows All\" setting with |Q|=1, the optimization objective reduces to maximizing the dot product between one query embedding and the adversarial passage embedding. The discrete nature of a single target query means the optimization can achieve near-perfect alignment in embedding space. GASLITE achieves **100% appeared@1** (top-1 result) across all nine evaluated models. This is described as \"fully solved\" -- the adversarial passage consistently becomes the single highest-ranked result for the target query.\n\nComparative performance for single-query:\n- Info Only (no optimization): 0% success\n- Stuffing (repeat the query text): 30-96% appeared@10, model-dependent\n- Cor.Pois. (prior SOTA): sometimes worse than stuffing due to tokenization issues\n- GASLITE: 100% appeared@1, all models\n\nFor dot-product models like Contriever, GASLITE achieves similarity scores of 3.453 +/- 0.350, roughly 2x what baseline methods achieve.\n\n---\n\n### What the 0.0001% Corpus Poisoning Rate Means\n\nThe primary corpus is MSMARCO with 8.8 million passages. A budget of 10 adversarial passages represents 10/8,800,000 = ~0.0001% of the corpus. At this poisoning rate:\n\n- GASLITE achieves >50% appeared@10 on 6 out of 9 models for unseen concept-specific queries.\n- Appeared@10 ranges from 61-100% on most models (the 61-100% figure cited in the abstract).\n- This represents an astronomically small injection that is practically undetectable by volume-based monitoring.\n\nScaling with budget (concept-specific, averaged across models):\n- 1 passage: ~30% appeared@10\n- 5 passages: ~48% appeared@10\n- 10 passages: ~62% appeared@10\n- 100% appeared@100 achieved on all models with just 10 passages\n\n---\n\n### What Makes Standard Defenses Fail Against Adaptive Versions\n\n**Defense 1 -- Perplexity Filtering:**\n- Rationale: GASLITE triggers are syntactically incoherent (e.g., \"So wizard tickets ideally ages Radcliffe trilogy typically 194 movies\"), so they exhibit high perplexity (~100-150 bits vs. normal ~50-80).\n- Defense: Filter passages exceeding a perplexity threshold (>10 bits).\n- **Adaptive bypass:** GASLITE integrates a perplexity penalty term into its optimization objective, constraining the trigger to remain within natural perplexity ranges.\n- Result: Adaptive variant achieves 58% appeared@10 vs. 62% baseline -- only a 4 percentage-point drop. Defense is effectively neutralized.\n\n**Defense 2 -- Embedding L2-Norm Filtering:**\n- Rationale: Adversarial passages may have abnormal embedding norms.\n- Defense: Filter passages with L2 norm exceeding a threshold (>0.8).\n- **Adaptive bypass:** GASLITE adds an L2-norm constraint to optimization, keeping embeddings within natural norm distributions.\n- Result: 60% appeared@10 vs. 62% baseline -- only 2 percentage-point drop.\n\nThe fundamental problem: both defenses rely on statistical anomaly detection (perplexity, norm), which can be incorporated as constraints in the attacker's optimization without significant performance loss. The paper concludes that \"deeper defenses are needed\" beyond surface-level filtering.\n\n---\n\n### Experimental Results and Key Findings\n\n**Models Evaluated (9 total):**\n- Cosine-similarity models: E5, MiniLM, GTR-T5, aMPNet, Arctic\n- Dot-product models: Contriever, Contriever-MS, ANCE, mMPNet\n\n**Key Quantitative Results:**\n\n| Setting | Budget | GASLITE appeared@10 | Best Baseline | Improvement |\n|---------|--------|---------------------|---------------|-------------|\n| Knows All (single query) | 1 | 100% (@1) | 30-96% (@10) | Fully solved |\n| Knows What (concept) | 10 | 61-100% | ~25% (Cor.Pois.) | >140% |\n| Knows Nothing (diverse) | 100 | 5-20% | <6% (Cor.Pois.) | Significant |\n\n**Model Vulnerability Variance (concept-specific, 1 passage):**\n- Contriever (dot-product, high anisotropy): ~100% appeared@10\n- E5 (cosine, moderate anisotropy): ~70%\n- Arctic (cosine, low anisotropy): ~20%\n- 5-fold difference in susceptibility across models\n\n**Vulnerability Factors Identified:**\n1. **Similarity metric:** Dot-product models are significantly more vulnerable than cosine-similarity models. Dot-product doesn't normalize embedding magnitudes, allowing adversarial passages to achieve disproportionately high scores.\n2. **Embedding space anisotropy:** Models with higher anisotropy (embeddings concentrated in narrow directional subspaces) are more exploitable. Anisotropy is measured via eigenvalue distributions of embedding matrices. In anisotropic spaces, adversarial passages can achieve high similarity without semantic naturalness.\n\n**Cross-Dataset Generalization:**\n- GASLITE passages optimized on MSMARCO queries generalize to NQ, SciFact, FiQA2018, and Quora queries.\n- Topic-specific datasets see higher transfer success (30-40%) than generic evaluation sets (5-15%).\n\n**Cross-Architecture Generalization:**\n- Successfully attacks LLM-based embeddings (Stella-1.5B with ~1.5B parameters), indicating broad applicability beyond BERT-scale models.\n\n**Black-Box Transferability:**\n- Limited: attacks trained on one model transfer with only 25-60% relative effectiveness to other models.\n- White-box access substantially improves attack success -- this is why the white-box threat model is important.\n\n**RAG Case Study:**\n- Tested on an actual RAG pipeline (OpenWebUI + Chroma vector store).\n- With 10 adversarial passages targeting Harry Potter queries:\n  - 73% of queries returned adversarial passages in top-3 retrieved context.\n  - LLM generated misleading responses in 58% of cases.\n  - 100% appearance rate in top-10 retrieval without defenses.\n\n---\n\n### Limitations Acknowledged\n\n1. **White-box assumption:** While justified by open-source prevalence, real deployments may use proprietary models (OpenAI, Cohere) where white-box access is unavailable. Black-box transferability is limited.\n2. **Concept knowledge required:** \"Knows What\" attacks require a sample of concept-related queries. Fully unknown attack distributions (\"Knows Nothing\") remain significantly harder (5-20% vs. 61-100%).\n3. **Static corpus assumption:** Real corpora are constantly updated; adversarial passages could be diluted or removed over time.\n4. **No corpus read-access:** Attacker cannot verify insertion success or monitor detection.\n5. **Trigger naturalness:** Despite perplexity-constrained variants, triggers remain syntactically odd. Future content moderation systems might flag them on other grounds.\n6. **English only:** Multilingual robustness is unexplored.\n7. **Trigger length:** 100 tokens is somewhat arbitrary; the sensitivity to this parameter is not exhaustively studied.\n8. **Model evolution:** Techniques may become less effective as embedding models improve and potentially incorporate adversarial training.\n\n---\n\n### Additional Context\n\n**Why Cor.Pois. (Zhong et al. 2023) Underperforms:**\nThe prior state-of-the-art (1) assumed access to corpus content and ground-truth passages (more relaxed threat model), (2) used single-token HotFlip without multi-coordinate optimization, and (3) critically, did not handle the token-to-text irreversibility problem. When optimized token sequences are decoded to text and re-tokenized for corpus insertion, the resulting tokens can differ from what was optimized, causing substantial degradation. This single issue accounts for much of the performance gap.\n\n**The paper's core contribution** is framed not as a novel mathematical formulation (the objective is straightforward dot-product maximization) but as a principled engineering solution: correctly solving discrete optimization in text space while maintaining token-text consistency, combined with the first comprehensive evaluation across realistic threat models and diverse models.\n\n**Subsequent citing work** includes \"Semantic Chameleon\" (2025), \"SilentRetrieval\" (2025), and \"Unsupervised Corpus Poisoning Attacks in Continuous Space\" (SIGIR 2025), indicating the paper has catalyzed follow-up research in RAG security.\n\n---\n\nSources:\n- [arXiv Abstract](https://arxiv.org/abs/2412.20953)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2412.20953v2)\n- [ACM DL Proceedings](https://dl.acm.org/doi/10.1145/3719027.3765095)\n- [GitHub Repository](https://github.com/matanbt/gaslite)\n- [MarkTechPost Coverage](https://www.marktechpost.com/2025/01/06/this-ai-paper-from-tel-aviv-university-introduces-gaslite-a-gradient-based-method-to-expose-vulnerabilities-in-dense-embedding-based-text-retrieval-systems/)\n- [Mahmood Sharif's Faculty Page](https://mahmoods01.github.io/authors/matan-ben-tov/)"
      }
    ],
    "totalDurationMs": 234579,
    "totalTokens": 26401,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1461,
      "cache_read_input_tokens": 20972,
      "output_tokens": 3967,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1461
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3967,
          "cache_read_input_tokens": 20972,
          "cache_creation_input_tokens": 1461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1461,
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
  "sourceToolAssistantUUID": "0e8cdb64-440b-4512-90fb-5e9f49aa2895",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "b3331ac4-664b-4eb3-bfb4-f2d8ff35b04e",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze conformal prediction for adversarial RAG systems",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Assistant

_source line 27 · 2026-05-30T06:46:08.470Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have detailed information on all 5 papers. Let me also note that paper 4 (the ICLR 2025 paper) was actually rejected. Let me verify this from the agent's report - yes, the meta-review says "Decision: Reject (December 20, 2024)". This is important context.

Now let me compile the JSON array with analyses for all 5 papers. Let me be careful about the 2000 character limit per paper.

Let me now write the analyses:

1. **Mitigating LLM Hallucinations via Conformal Abstention** (NeurIPS 2024 Workshop)


2. **Robust Yet Efficient Conformal Prediction Sets** (ICML 2024)
3. **Towards Poisoning Robustness Certification for Natural Language Generation** (arXiv 2026)
4. **Understanding Data Poisoning Attacks for RAG** (ICLR 2025 - Rejected)
5. **GASLITEing the Retrieval** (ACM CCS 2025)

Now I'll craft precise analyses for each, keeping within the character limits.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3331ac4-664b-4eb3-bfb4-f2d8ff35b04e",
  "isSidechain": false,
  "requestId": "req_011CbYJY4RL82YvP45uNWa6p",
  "type": "assistant",
  "uuid": "0f12db64-0ba0-4b27-b5ae-e49363af5f1e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tq2vRSbABpSvf3z5csT6N5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4364,
      "cache_read_input_tokens": 29583,
      "output_tokens": 2775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4364,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2775,
          "cache_read_input_tokens": 29583,
          "cache_creation_input_tokens": 4364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4364
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

_source line 28 · 2026-05-30T06:47:13.441Z_

Now I have comprehensive information on all 5 papers. Let me synthesize the analyses into the required JSON format.

```json
[
  {
    "title": "Mitigating LLM Hallucinations via Conformal Abstention",
    "venue": "NeurIPS 2024 Workshop (Statistical Frontiers in LLMs and Foundation Models)",
    "problem_identification": "Standard LLM confidence signals (log-probabilities) degrade for long-form responses, making hallucination detection unreliable. The authors identified that token-level probability scores become non-indicative of correctness as sequence length grows, leaving no principled abstention mechanism with formal guarantees.",
    "key_insight": "Self-consistency among multiple sampled LLM responses, evaluated by the LLM itself as a semantic similarity judge, provides a query-dependent nonconformity score that is far more robust to output length than token log-probabilities.",
    "innovation_type": "combination",
    "method_summary": "Sample k responses per query, compute pairwise semantic similarity via LLM self-evaluation (Match Count) or expected match count via token probabilities (EMC), then apply Conformal Risk Control to calibrate an abstention threshold λ such that E[R(λ)] ≤ α. The match function threshold β is itself calibrated via CP to bound false negative matches. A high-probability amplification variant partitions calibration data into K subsets to achieve P(R ≤ eα) ≥ 1−δ.",
    "limitations_and_open_questions": "Assumes exchangeability between calibration and deployment — any distribution shift (including adversarial retrieval corruption) invalidates guarantees. Self-consistency fails when the model is systematically wrong (confidently hallucinating the same incorrect answer across samples).",
    "building_blocks": ["Self-consistency nonconformity scores", "Conformal Risk Control (CRC) for abstention threshold calibration", "LLM-as-judge similarity scoring", "Match function calibration via CP"],
    "relevance_to_seed": "Establishes the conformal abstention paradigm we extend; its exchangeability assumption is precisely what corpus poisoning violates, making it the starting point our retrieval-aware score function must fix."
  },
  {
    "title": "Robust Yet Efficient Conformal Prediction Sets",
    "venue": "ICML 2024",
    "problem_identification": "Prior robust CP (RSCP) produced vacuously large prediction sets because it bounded worst-case score changes using only the mean of smoothed scores, discarding distributional information. This made robust CP impractical for real deployment.",
    "key_insight": "Replacing mean-only bounds on smoothed conformity scores with CDF-based bounds captures full distributional information about score behavior under perturbation, yielding strictly tighter worst-case estimates that produce 2-10x smaller prediction sets.",
    "innovation_type": "new_technique",
    "method_summary": "CAS (CDF-Aware Smoothed prediction sets) applies randomized smoothing to conformity scores (Gaussian for continuous, XOR-Bernoulli for discrete data), then optimizes worst-case scores over a function class constrained by the full empirical CDF rather than just the mean. For poisoning, the method formulates worst-case quantile computation as a MILP over feasible calibration perturbations. DKW/Bernstein finite-sample corrections replace Hoeffding bounds for tighter guarantees.",
    "limitations_and_open_questions": "MILP poisoning certification doesn't scale to large calibration sets. Exchangeability still assumed — the method handles bounded perturbations to calibration data but not the fundamentally different threat model of test-time retrieval corruption where the adversary controls which documents are seen.",
    "building_blocks": ["CDF-based worst-case score bounding", "MILP for poisoning-robust quantile computation", "Calibration-time variant (precompute lower bounds offline)", "DKW finite-sample corrections"],
    "relevance_to_seed": "Demonstrates how to achieve tight robust CP sets under poisoning, but its threat model assumes calibration-set corruption — adapting CDF-aware bounding to retrieval-time corruption (where poisoned documents affect test scores, not calibration) is a key technical challenge for our work."
  },
  {
    "title": "Towards Poisoning Robustness Certification for Natural Language Generation",
    "venue": "arXiv 2026 (preprint)",
    "problem_identification": "Certified poisoning defenses exist only for classification; the autoregressive nature of NLG (sequential predictions, exponential output space) makes direct adaptation impossible. No prior work could certify that generation outputs remain valid under bounded training-data poisoning.",
    "key_insight": "Decomposing robustness into stability (no output change) vs. validity (no specific harmful output), and certifying validity via Targeted Partition Aggregation that computes the minimum poisoning budget to induce a specific harmful token — validity is much more certifiable than stability because the attacker's target constrains the certification problem.",
    "innovation_type": "cross_domain",
    "method_summary": "TPA extends shard-and-aggregate to NLG: partition training data into S shards, train independent models per shard, aggregate via majority voting over tokens. For validity certification, TPA iteratively reallocates votes from top-ranked tokens to a target harmful token to compute the minimum number of shard poisonings needed. Multi-turn certification uses MILP to distribute a global poisoning budget K across shards optimally. Phrase-level voting over V^m extends token-level certificates to sequences.",
    "limitations_and_open_questions": "Addresses training-time poisoning, not test-time retrieval corruption — orthogonal threat model to our work. Inference latency with hundreds of shard models (150s) remains impractical. Certificates are conservative: empirical robustness substantially exceeds certified bounds.",
    "building_blocks": ["Stability vs. validity decomposition", "Targeted Partition Aggregation algorithm", "MILP collective certification across prompts", "Phrase-level majority voting"],
    "relevance_to_seed": "Closest existing work to our direction but in a different threat model (training poisoning vs. retrieval corruption) and without conformal prediction — demonstrates the partition-and-aggregate paradigm we adapt, and the validity concept maps to our abstention decision."
  },
  {
    "title": "Understanding Data Poisoning Attacks for RAG: Insights and Algorithms",
    "venue": "ICLR 2025 (Rejected)",
    "problem_identification": "RAG poisoning attacks succeed empirically but lack theoretical explanation of why. The authors identified that understanding the geometric structure of embedding spaces reveals which attack directions are most effective, enabling principled defense design.",
    "key_insight": "Effective poisoning attacks exploit low-variance directions of the clean embedding distribution — directions where probability mass is tightly concentrated — because small perturbations along these directions rapidly move away from clean document density, making poisoned documents dominate retrieval.",
    "innovation_type": "analysis",
    "method_summary": "Eigendecompose the clean corpus covariance matrix; low-variance directions (small eigenvalues) are where attacks are most effective. DRS defense projects test documents onto these low-variance eigenvectors and flags documents with high directional relative shift. The regularized attack adds a DRS penalty to the poisoning objective, trading attack success for stealthiness. Detection threshold set at 99th percentile of clean DRS scores.",
    "limitations_and_open_questions": "Rejected at ICLR due to a fundamental assumption that adversarial and normal queries are geometrically separable — entity-substitution attacks (semantically similar poisoned docs) defeat this. Requires pre-specified protected query set and trusted clean corpus. DRS performance drops to 49-65% on subtle grammatical-perturbation attacks.",
    "building_blocks": ["Low-variance direction analysis of embedding spaces", "Eigendecomposition-based anomaly detection", "Attack-defense co-optimization framework", "Directional Relative Shift metric"],
    "relevance_to_seed": "The low-variance direction analysis explains why poisoned documents can fool retrievers, supporting our argument that retrieval-level defenses alone are insufficient — but the DRS defense's fragility to semantic poisoning reinforces the need for our abstention-based approach rather than detection-based filtering."
  },
  {
    "title": "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search",
    "venue": "ACM CCS 2025",
    "problem_identification": "Prior corpus poisoning attacks used relaxed threat models (corpus access, ground-truth labels) and underperformed due to a token-to-text irreversibility bug — optimized token sequences produce different tokens when decoded to text and re-tokenized for corpus insertion.",
    "key_insight": "The ReTokenize consistency check — filtering token substitutions that would change after a text→tokens→text round trip — eliminates the primary failure mode of prior discrete optimization attacks, enabling a simple dot-product maximization objective to achieve near-perfect attack success.",
    "innovation_type": "new_technique",
    "method_summary": "Construct adversarial passages as info||trigger, where info carries attacker content and trigger (100 tokens) is optimized via multi-coordinate greedy search. Each iteration averages gradient approximations across 50 random single-token substitutions, selects 20 positions simultaneously, filters candidates through ReTokenize consistency, and greedily picks the best. For multi-passage budgets, k-means clusters target query embeddings and optimizes one passage per centroid.",
    "limitations_and_open_questions": "Requires white-box model access (limited black-box transferability at 25-60%). 'Knows Nothing' attacks remain hard (5-20% vs 61-100% for concept-specific). Trigger text remains syntactically odd despite perplexity constraints, potentially flaggable by future content moderation.",
    "building_blocks": ["ReTokenize consistency filtering", "Multi-coordinate discrete optimization", "Vulnerability factors: dot-product models and anisotropic embeddings more exploitable", "Adaptive attacks bypassing perplexity and L2-norm defenses"],
    "relevance_to_seed": "Demonstrates that dense retrieval is catastrophically vulnerable at 0.0001% poisoning — even 10 adversarial passages in 8.8M suffice. This proves retrieval-level defenses are fundamentally insufficient, directly motivating our conformal abstention framework as a necessary last line of defense."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f12db64-0ba0-4b27-b5ae-e49363af5f1e",
  "isSidechain": false,
  "requestId": "req_011CbYJY4RL82YvP45uNWa6p",
  "type": "assistant",
  "uuid": "21704a6b-6add-4763-a377-0c63d0504526",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tq2vRSbABpSvf3z5csT6N5",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4364,
      "cache_read_input_tokens": 29583,
      "output_tokens": 2775,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4364,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2775,
          "cache_read_input_tokens": 29583,
          "cache_creation_input_tokens": 4364,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4364
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "21704a6b-6add-4763-a377-0c63d0504526",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze conformal prediction for adversarial RAG systems",
  "sessionId": "8ee4913b-30ba-4fac-800b-6164c595a9ea"
}
```

---
