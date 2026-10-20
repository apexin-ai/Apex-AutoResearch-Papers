# Research conversation: You are a senior ML researcher conducting a comprehensive literature survey. **Today's date: 2026-05-30 (UTC).** ## Task

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/41901ced-6b17-4e52-97f2-1983f67919e2.jsonl`
- **Structured JSON:** [`436f85c03aa28f202252.json`](../../sessions/43/436f85c03aa28f202252.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:12:29.547Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:12:29.547Z",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "content": "You are a senior ML researcher conducting a comprehensive literature survey.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Task\nFind the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:\n\n**Target: AAAI 2026\nTrack: Safe, Robust and Responsible AI (SRRAI)\n\nDirection: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.\n\nSeed Papers:\n- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval\n- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG\n- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative\n- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on\n- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition\n\nKnown Gaps:\n- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)\n- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails\n- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis\n\nTheoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must compare against RobustRAG and ReliabilityRAG baselines\n- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols\n- AAAI 2026 submission deadline: August 2026\n\nQuality Self-Checks:\n- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.\n- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.\n- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.\n- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.\n\nAvoid:\n- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this\n- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead\n- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates**\n\n## What counts as 'important'\n\nPrioritize (in order):\n1. **Best paper awards** at top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, AAAI, etc.)\n2. **Oral / spotlight presentations** at these venues\n3. **Highly cited papers** (>50 citations in 1-2 years)\n4. **Papers that introduced widely-adopted methods** (e.g., new training paradigm, new benchmark)\n5. **Recent survey papers** that provide comprehensive field overviews\n6. **Strong recent work** from top labs (Google, Meta, DeepMind, OpenAI, CMU, Stanford, etc.)\n\n## Search strategy\n\nExecute AT LEAST 15 targeted searches:\n\n1. `best paper award ACL EMNLP NeurIPS ICML ICLR 2026 Target: AAAI 2026\nTrack: Safe, Robust and Responsible AI (SRRAI)\n\nDirection: Develop a conformal-prediction-based abstention framework for RAG systems that provides distribution-free guarantees on answer correctness even when the retrieval corpus is adversarially poisoned. The key insight is that corpus poisoning induces a specific type of distribution shift on conformal nonconformity scores that standard robust CP (e.g., RPS) cannot handle because it assumes calibration poisoning, not test-time retrieval corruption. We propose a retrieval-aware score function that conditions on retrieval agreement signals to restore exchangeability under bounded poisoning.\n\nSeed Papers:\n- TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction (NAACL, 2024) — establishes conformal prediction for RAG answer sets but assumes benign retrieval\n- Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning (ICLR Spotlight, 2025) — poisoning-robust CP via smoothed scores and majority voting, but for classifiers not RAG\n- Certifiably Robust RAG against Retrieval Corruption (SaTML, 2026) — isolate-then-aggregate certified defense for RAG, provides the threat model and baselines but no conformal/abstention mechanism\n- Is Conformal Factuality for RAG-based LLMs Robust? (arXiv, Mar 2026) — demonstrates that naive conformal guarantees for RAG break under distribution shift, motivating the need for a robust alternative\n- C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models (ICML, 2024) — conformal risk bounds for RAG under benign conditions, theoretical framework to build on\n- ReliabilityRAG (arXiv, Feb 2026) — graph-theoretic MIS defense from Princeton group, latest certified RAG defense and primary competition\n\nKnown Gaps:\n- No existing work provides conformal abstention guarantees for RAG under corpus poisoning (TRAQ/C-RAG assume benign retrieval; RobustRAG/ReliabilityRAG don't use conformal prediction)\n- Poisoning-robust CP (RPS) assumes calibration set poisoning, not test-time retrieval corruption — the threat model mismatch means direct adaptation fails\n- Chen et al. (2026) show conformal factuality guarantees break under distribution shift but propose no solution — only diagnosis\n\nTheoretical Anchor: Corpus poisoning violates exchangeability of retrieved documents (poisoned docs are adversarially constructed, not drawn from the same distribution). Standard conformal prediction assumes exchangeability and breaks. We restore a weaker form of exchangeability by partitioning retrieved documents into agreement groups and constructing group-conditional conformal scores that are robust to a bounded number of adversarial insertions — analogous to how RPS uses partition-and-vote for calibration poisoning, but adapted to the retrieval corruption threat model where the adversary controls document content rather than calibration labels.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must compare against RobustRAG and ReliabilityRAG baselines\n- Evaluation on NQ, HotpotQA, and MS-MARCO with PoisonedRAG and CorruptRAG attack protocols\n- AAAI 2026 submission deadline: August 2026\n\nQuality Self-Checks:\n- [x] Core insight: Corpus poisoning breaks exchangeability of retrieved documents, invalidating standard conformal guarantees — we need retrieval-aware score functions that condition on document agreement to restore coverage under bounded poisoning.\n- [x] Why not obvious: Naive application of RPS to RAG fails because RPS assumes calibration poisoning (wrong labels) while RAG poisoning corrupts test-time retrieval (wrong documents) — different threat models require different score function designs.\n- [x] Baseline fear test: A simple baseline of 'abstain whenever retrieved documents disagree' would have high abstention rates and no formal guarantees — our method provides tunable coverage-abstention tradeoffs with certificates.\n- [x] Information exploited: We exploit the agreement structure among independently retrieved passages — poisoned documents must simultaneously fool the retriever AND be semantically consistent with benign passages, which constrains the attacker.\n\nAvoid:\n- Naive application of existing CP frameworks (TRAQ, RPS) without addressing the threat model mismatch — reviewers familiar with Chen et al. (2026) will immediately flag this\n- Over-relying on LLM-based nonconformity scores that are themselves vulnerable to adversarial manipulation — use embedding-geometric or retrieval-agreement-based scores instead\n- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates`\n2. `oral spotlight {venue} 2026 {topic}` — for each major venue\n3. `site:openreview.net {topic} 2026 outstanding` — OpenReview 高分论文\n4. `{topic} survey 2026` 或 `{topic} survey 2025` — 综述论文\n5. `site:arxiv.org {topic} 2026` — arXiv 最新高引\n6. `most cited {topic} 2025 2026` — Google Scholar\n7. `site:paperswithcode.com {task} SOTA` — SOTA 排行榜上的论文\n8. `{topic} benchmark {year}` — 定义领域的 benchmark 论文\n9. 对每个找到的重要论文，搜索其 cited-by 发现后续工作\n\nFor EVERY paper you find, use WebFetch to read its abstract and introduction on arXiv or OpenReview. Do NOT rely on search snippets alone — you need to understand what each paper actually does.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Full paper title\",\n  \"authors\": \"First author et al.\",\n  \"venue\": \"EMNLP 2025 / NeurIPS 2024 / arXiv 2025 / ...\",\n  \"url\": \"https://arxiv.org/abs/... or openreview URL\",\n  \"why_important\": \"Best paper / Oral / High-cited / Introduced X / ...\",\n  \"one_line_summary\": \"What this paper does in one sentence\"\n}\n\nFind at least 15 papers. More is better if they are genuinely relevant.\nIMPORTANT: You MUST end your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:12:29.550Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:12:29.550Z",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-30T06:12:29.564Z_

You are a senior ML researcher conducting a comprehensive literature survey.

**Today's date: 2026-05-30 (UTC).**

## Task
Find the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:

**Target: AAAI 2026
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

## What counts as 'important'

Prioritize (in order):
1. **Best paper awards** at top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, AAAI, etc.)
2. **Oral / spotlight presentations** at these venues
3. **Highly cited papers** (>50 citations in 1-2 years)
4. **Papers that introduced widely-adopted methods** (e.g., new training paradigm, new benchmark)
5. **Recent survey papers** that provide comprehensive field overviews
6. **Strong recent work** from top labs (Google, Meta, DeepMind, OpenAI, CMU, Stanford, etc.)

## Search strategy

Execute AT LEAST 15 targeted searches:

1. `best paper award ACL EMNLP NeurIPS ICML ICLR 2026 Target: AAAI 2026
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
- Claiming end-to-end compositional guarantees across retriever + generator (RQ1 territory) — focus specifically on the abstention decision with formal certificates`
2. `oral spotlight {venue} 2026 {topic}` — for each major venue
3. `site:openreview.net {topic} 2026 outstanding` — OpenReview 高分论文
4. `{topic} survey 2026` 或 `{topic} survey 2025` — 综述论文
5. `site:arxiv.org {topic} 2026` — arXiv 最新高引
6. `most cited {topic} 2025 2026` — Google Scholar
7. `site:paperswithcode.com {task} SOTA` — SOTA 排行榜上的论文
8. `{topic} benchmark {year}` — 定义领域的 benchmark 论文
9. 对每个找到的重要论文，搜索其 cited-by 发现后续工作

For EVERY paper you find, use WebFetch to read its abstract and introduction on arXiv or OpenReview. Do NOT rely on search snippets alone — you need to understand what each paper actually does.

## Output format

Output a JSON array. Each element:
{
  "title": "Full paper title",
  "authors": "First author et al.",
  "venue": "EMNLP 2025 / NeurIPS 2024 / arXiv 2025 / ...",
  "url": "https://arxiv.org/abs/... or openreview URL",
  "why_important": "Best paper / Oral / High-cited / Introduced X / ...",
  "one_line_summary": "What this paper does in one sentence"
}

Find at least 15 papers. More is better if they are genuinely relevant.
IMPORTANT: You MUST end your response with the JSON array.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "type": "user",
  "uuid": "f4002682-7b39-4978-94e3-8c5a617c6f9b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:12:29.563Z_

```json
{
  "parentUuid": "f4002682-7b39-4978-94e3-8c5a617c6f9b",
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
  "uuid": "b9500b46-fea2-4555-ba1a-ce2ab2790122",
  "timestamp": "2026-05-30T06:12:29.563Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:12:29.563Z_

```json
{
  "parentUuid": "b9500b46-fea2-4555-ba1a-ce2ab2790122",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c0eb92fc-6e0f-46b3-8a43-fd204b7bdd8c",
  "timestamp": "2026-05-30T06:12:29.563Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
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
  "aiTitle": "Literature survey on conformal prediction for RAG",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Assistant

_source line 7 · 2026-05-30T06:12:36.192Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a comprehensive literature survey to find the 15 most important recent papers (2024-2026) related to their research direction: conformal prediction-based abstention framework for RAG systems under adversarial corpus poisoning.

Let me break down the key topics I need to search for:
1. Conformal prediction for RAG/LLMs
2. Robust conformal prediction / poisoning-robust CP
3. Adversarial attacks on RAG / corpus poisoning
4. Certified/robust RAG defenses
5. Abstention/selective prediction for LLMs
6. Distribution-free guarantees for LLMs


7. Conformal prediction under distribution shift

I'll launch multiple search agents in parallel to cover these topics efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0eb92fc-6e0f-46b3-8a43-fd204b7bdd8c",
  "isSidechain": false,
  "requestId": "req_011CbYFz6AP2zRLnXwrbK2nH",
  "type": "assistant",
  "uuid": "dbc34244-274d-4d69-ab41-a3c01dc57405",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhsDrTmqAYeqZLKdRLMen6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15332,
      "cache_read_input_tokens": 0,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15332
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

_source line 8 · 2026-05-30T06:12:36.709Z_

I'll conduct a comprehensive literature survey by launching multiple parallel search agents across different topic areas. Let me start with the first wave of searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbc34244-274d-4d69-ab41-a3c01dc57405",
  "isSidechain": false,
  "requestId": "req_011CbYFz6AP2zRLnXwrbK2nH",
  "type": "assistant",
  "uuid": "3c83451d-1fce-4a52-9aca-8d98ee163066",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhsDrTmqAYeqZLKdRLMen6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15332,
      "cache_read_input_tokens": 0,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15332
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

_source line 9 · 2026-05-30T06:12:37.364Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JLXgLeVb2WKvdeHGVFSucu`</summary>

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
  "parentUuid": "3c83451d-1fce-4a52-9aca-8d98ee163066",
  "isSidechain": false,
  "requestId": "req_011CbYFz6AP2zRLnXwrbK2nH",
  "type": "assistant",
  "uuid": "8c365cea-b5c5-459f-8841-82741b8bd6cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BhsDrTmqAYeqZLKdRLMen6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15332,
      "cache_read_input_tokens": 0,
      "output_tokens": 295,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15332,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 295,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15332,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15332
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

_source line 10 · 2026-05-30T06:12:37.372Z_

<details><summary>↩ Tool result · `toolu_01JLXgLeVb2WKvdeHGVFSucu`</summary>

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
  "parentUuid": "8c365cea-b5c5-459f-8841-82741b8bd6cc",
  "isSidechain": false,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "type": "user",
  "uuid": "038724f5-4210-49d4-8253-42d54476466b",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "8c365cea-b5c5-459f-8841-82741b8bd6cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "038724f5-4210-49d4-8253-42d54476466b",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on conformal prediction for RAG",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Assistant

_source line 13 · 2026-05-30T06:12:42.507Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the WebSearch and WebFetch tools available. Let me launch multiple parallel search agents to cover different aspects of the research area. I'll organize them by topic cluster.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "038724f5-4210-49d4-8253-42d54476466b",
  "isSidechain": false,
  "requestId": "req_011CbYFzn5yKEtHDhHNSeqi7",
  "type": "assistant",
  "uuid": "45a11bf2-a8cc-4906-9f0b-bab3ce6e8154",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2jVFW7uJPTkdnzZxwusT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1315,
      "cache_read_input_tokens": 15332,
      "output_tokens": 1763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1763,
          "cache_read_input_tokens": 15332,
          "cache_creation_input_tokens": 1315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1315
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

_source line 14 · 2026-05-30T06:12:43.048Z_

Now let me launch multiple parallel search agents to cover all the key topic areas comprehensively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45a11bf2-a8cc-4906-9f0b-bab3ce6e8154",
  "isSidechain": false,
  "requestId": "req_011CbYFzn5yKEtHDhHNSeqi7",
  "type": "assistant",
  "uuid": "b526dc64-d101-4722-826c-f42df260602b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2jVFW7uJPTkdnzZxwusT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1315,
      "cache_read_input_tokens": 15332,
      "output_tokens": 1763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1763,
          "cache_read_input_tokens": 15332,
          "cache_creation_input_tokens": 1315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1315
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

_source line 15 · 2026-05-30T06:12:49.809Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01ETzPNkMZYXm1ZKMfwz3HH8`</summary>

```json
{
  "description": "Search: Conformal prediction RAG",
  "prompt": "You are helping with a literature survey on conformal prediction for RAG systems. Search for and analyze papers from 2024-2026.\n\nExecute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:\n\n1. Search: \"conformal prediction retrieval augmented generation 2024 2025 2026\"\n2. Search: \"TRAQ conformal prediction RAG trustworthy\"\n3. Search: \"C-RAG certified generation risks retrieval augmented language models\"\n4. Search: \"conformal prediction LLM factuality 2025 2026\"\n5. Search: \"conformal prediction natural language generation abstention\"\n\nFor each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers that combine conformal prediction with RAG or LLM systems.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b526dc64-d101-4722-826c-f42df260602b",
  "isSidechain": false,
  "requestId": "req_011CbYFzn5yKEtHDhHNSeqi7",
  "type": "assistant",
  "uuid": "98fbd72b-712f-4625-b78d-cc236d3ceec3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2jVFW7uJPTkdnzZxwusT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1315,
      "cache_read_input_tokens": 15332,
      "output_tokens": 1763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1763,
          "cache_read_input_tokens": 15332,
          "cache_creation_input_tokens": 1315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1315
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

_source line 16 · 2026-05-30T06:12:53.723Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01RDAQhCaDJWBZy8KcJUCgVZ`</summary>

```json
{
  "description": "Search: Robust CP and poisoning",
  "prompt": "You are helping with a literature survey on robust conformal prediction, especially under data poisoning and distribution shift. Search for papers from 2024-2026.\n\nExecute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:\n\n1. Search: \"robust conformal prediction data poisoning 2024 2025 2026\"\n2. Search: \"conformal prediction distribution shift adversarial 2025 2026\"\n3. Search: \"provably reliable conformal prediction poisoning ICLR 2025\"\n4. Search: \"conformal prediction exchangeability violation robust\"\n5. Search: \"distribution-free prediction adversarial robustness 2025 2026\"\n\nFor each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers about making conformal prediction robust to adversarial manipulation, poisoning, or distribution shift.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98fbd72b-712f-4625-b78d-cc236d3ceec3",
  "isSidechain": false,
  "requestId": "req_011CbYFzn5yKEtHDhHNSeqi7",
  "type": "assistant",
  "uuid": "52d8807e-79d8-4b78-b8f0-df7306652912",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2jVFW7uJPTkdnzZxwusT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1315,
      "cache_read_input_tokens": 15332,
      "output_tokens": 1763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1763,
          "cache_read_input_tokens": 15332,
          "cache_creation_input_tokens": 1315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1315
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

_source line 17 · 2026-05-30T06:12:58.446Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KJGXLsa36snUV88pDwHz2y`</summary>

```json
{
  "description": "Search: RAG robustness attacks",
  "prompt": "You are helping with a literature survey on adversarial attacks and certified defenses for RAG systems. Search for papers from 2024-2026.\n\nExecute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:\n\n1. Search: \"corpus poisoning RAG retrieval augmented generation attack 2024 2025 2026\"\n2. Search: \"PoisonedRAG adversarial retrieval attack 2024 2025\"\n3. Search: \"certified robust RAG retrieval corruption defense 2025 2026\"\n4. Search: \"RobustRAG certifiably robust retrieval augmented generation\"\n5. Search: \"ReliabilityRAG graph-theoretic defense retrieval poisoning Princeton\"\n6. Search: \"adversarial attacks knowledge retrieval LLM 2025 2026\"\n\nFor each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers about attacking or defending RAG systems against corpus/retrieval poisoning.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52d8807e-79d8-4b78-b8f0-df7306652912",
  "isSidechain": false,
  "requestId": "req_011CbYFzn5yKEtHDhHNSeqi7",
  "type": "assistant",
  "uuid": "bf08d179-5b24-42fd-be03-6a95b39ea02f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2jVFW7uJPTkdnzZxwusT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1315,
      "cache_read_input_tokens": 15332,
      "output_tokens": 1763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1763,
          "cache_read_input_tokens": 15332,
          "cache_creation_input_tokens": 1315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1315
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

_source line 18 · 2026-05-30T06:13:02.235Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NwE3Yzh6mMFENwoz3PeHua`</summary>

```json
{
  "description": "Search: Selective prediction LLMs",
  "prompt": "You are helping with a literature survey on selective prediction, abstention, and uncertainty quantification for LLMs. Search for papers from 2024-2026.\n\nExecute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:\n\n1. Search: \"selective prediction large language models abstention 2024 2025 2026\"\n2. Search: \"LLM uncertainty quantification calibration 2025 2026 survey\"\n3. Search: \"know when to abstain LLM confidence 2025 2026\"\n4. Search: \"conformal prediction large language models 2025 2026\"\n5. Search: \"distribution-free uncertainty LLM generation 2025 2026\"\n\nFor each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers about when LLMs should abstain from answering, and formal uncertainty guarantees for LLM outputs.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf08d179-5b24-42fd-be03-6a95b39ea02f",
  "isSidechain": false,
  "requestId": "req_011CbYFzn5yKEtHDhHNSeqi7",
  "type": "assistant",
  "uuid": "8a1ee919-54da-4173-8b5d-ba08fe58665c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2jVFW7uJPTkdnzZxwusT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1315,
      "cache_read_input_tokens": 15332,
      "output_tokens": 1763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1763,
          "cache_read_input_tokens": 15332,
          "cache_creation_input_tokens": 1315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1315
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

_source line 19 · 2026-05-30T06:13:07.933Z_

<details open><summary>🔧 Tool call — Agent · `toolu_019TDeGV7LG7ETS9caJm86po`</summary>

```json
{
  "description": "Search: Best papers top venues",
  "prompt": "You are helping with a literature survey. Search for best paper awards and outstanding papers at top ML/NLP venues from 2024-2026 that are relevant to: conformal prediction, robust AI, adversarial robustness, RAG systems, or trustworthy AI.\n\nExecute these searches:\n\n1. Search: \"best paper award NeurIPS 2025 conformal prediction robust\"\n2. Search: \"best paper ICML 2025 2026 adversarial robustness trustworthy AI\"\n3. Search: \"best paper ACL EMNLP NAACL 2025 2026 retrieval augmented generation\"\n4. Search: \"outstanding paper ICLR 2025 2026 robust conformal\"\n5. Search: \"best paper AAAI 2025 2026 safe robust responsible AI\"\n6. Search: \"oral spotlight NeurIPS ICML 2025 conformal prediction\"\n7. Search: \"site:openreview.net conformal prediction 2025 2026 outstanding\"\n\nFor each relevant paper found, use WebFetch on its arxiv/openreview URL to read the abstract.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important (specifically note if best paper/oral/spotlight), and a one-line summary.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a1ee919-54da-4173-8b5d-ba08fe58665c",
  "isSidechain": false,
  "requestId": "req_011CbYFzn5yKEtHDhHNSeqi7",
  "type": "assistant",
  "uuid": "98d40381-5ed0-4e18-8675-7179eab16f8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016B2jVFW7uJPTkdnzZxwusT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1315,
      "cache_read_input_tokens": 15332,
      "output_tokens": 1763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1315,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1763,
          "cache_read_input_tokens": 15332,
          "cache_creation_input_tokens": 1315,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1315
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

_source line 20 · 2026-05-30T06:15:09.859Z_

<details><summary>↩ Tool result · `toolu_01RDAQhCaDJWBZy8KcJUCgVZ`</summary>

```text
Now I have enough information to compile a comprehensive structured list. Here is the literature survey.

---

## Literature Survey: Robust Conformal Prediction under Adversarial Manipulation, Poisoning, and Distribution Shift (2024--2026)

---

### 1. Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning

- **Authors:** Yan Scholten, Stephan Gunnemann
- **Venue:** ICLR 2025 (Spotlight)
- **URL:** https://arxiv.org/abs/2410.09878
- **Code:** https://github.com/yascho/reliable_conformal_prediction
- **Summary:** Proposes Reliable Prediction Sets (RPS), the first scalable method for conformal prediction with provable reliability guarantees under both training and calibration data poisoning.
- **Why it matters:** This is the foundational defense paper for CP under poisoning. It introduces smoothed score functions (aggregating across training partitions) for training poisoning and majority voting across calibration subsets for calibration poisoning. It provides formal certificates of reliability under worst-case poisoning, including label-flipping attacks. As an ICLR Spotlight, it is the highest-profile paper in this specific subfield.

---

### 2. Data Poisoning Attacks against Conformal Prediction

- **Authors:** Yangyi Li, Aobo Chen, Wei Qian, Chenxu Zhao, Divya Lidder, Mengdi Huai
- **Venue:** ICML 2024 (Proceedings of Machine Learning Research, Vol. 235, pp. 27563--27574)
- **URL:** https://proceedings.mlr.press/v235/li24l.html
- **Summary:** Introduces the first black-box data poisoning attacks specifically designed to manipulate conformal prediction uncertainty (prediction set size), rather than causing misclassifications.
- **Why it matters:** This paper defines the threat model. Prior poisoning attacks targeted accuracy; this work shows that an adversary can directly manipulate the prediction sets (making them vacuously large or dangerously small) via poisoning. It demonstrates that existing defenses are ineffective, motivating the defensive works that follow.

---

### 3. Robust Yet Efficient Conformal Prediction Sets

- **Authors:** Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski
- **Venue:** ICML 2024
- **URL:** https://arxiv.org/abs/2407.09165
- **Summary:** Derives provably robust conformal prediction sets by bounding the worst-case change in conformity scores, producing tighter sets that handle both evasion and poisoning attacks on features and labels.
- **Why it matters:** Addresses the efficiency problem -- prior robust CP methods produced overly conservative (large) sets. This work achieves tighter bounds for both continuous and discrete/sparse data while maintaining provable guarantees against evasion and poisoning.

---

### 4. Verifiably Robust Conformal Prediction (VRCP)

- **Authors:** Linus Jeary, Tom Kuipers, Mehran Hosseini, Nicola Paoletti
- **Venue:** NeurIPS 2024
- **URL:** https://arxiv.org/abs/2405.18942
- **Summary:** Combines conformal prediction with neural network verification to recover probabilistic coverage guarantees under adversarial perturbations; first method to handle arbitrary norms (l1, l2, l-infinity) and regression tasks.
- **Why it matters:** Prior approaches (based on randomized smoothing) were limited to l2-bounded perturbations and classification only. VRCP uses formal verification to provide exact (non-conservative) robustness guarantees. It also automatically provides robustness against feature poisoning attacks. Demonstrated on CIFAR-10/100, TinyImageNet, and deep RL regression.

---

### 5. COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits

- **Authors:** Mintong Kang, Nezihe Merve Gurel, Linyi Li, Bo Li
- **Venue:** ICLR 2024
- **URL:** https://arxiv.org/abs/2403.11348
- **Summary:** Combines learning and reasoning via probabilistic circuits to achieve certifiably robust conformal prediction under bounded adversarial perturbations, with up to 14% coverage improvement on benchmark datasets.
- **Why it matters:** Introduces a neuro-symbolic approach to robust CP. By encoding semantic concept relationships through probabilistic circuits, it provides theoretical coverage guarantees under perturbation while improving accuracy over single models. Demonstrates gains on GTSRB, CIFAR-10, and AwA2.

---

### 6. Provably Robust Conformal Prediction with Improved Efficiency

- **Authors:** Ge Yan, Yaniv Romano, Tsui-Wei Weng
- **Venue:** arXiv preprint (April 2024)
- **URL:** https://arxiv.org/abs/2404.19651
- **Summary:** Corrects flaws in prior RSCP robustness guarantees and introduces RSCP+ with two efficiency techniques (Post-Training Transformation and Robust Conformal Training), achieving up to 16.9x efficiency gains on ImageNet.
- **Why it matters:** Identifies and fixes theoretical issues in the original Randomized Smoothed Conformal Prediction (RSCP) framework. The efficiency improvements (PTT and RCT) are critical for practical deployment -- prior robust CP methods produced prediction sets so large they were uninformative. Validated on CIFAR-10, CIFAR-100, and ImageNet.

---

### 7. Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations

- **Authors:** Liviu Aolaritei, Qianyu Julie Zhu, Zheyu Oliver Wang, Michael I. Jordan, Youssef Marzouk
- **Venue:** NeurIPS 2025
- **URL:** https://arxiv.org/abs/2502.14105 | https://openreview.net/forum?id=1ULQvdbZ3X
- **Summary:** Models distribution shifts via Levy-Prokhorov ambiguity sets capturing both local and global perturbations, and reduces high-dimensional distribution shifts to one-dimensional shifts through the scoring function for tractable robust coverage guarantees.
- **Why it matters:** Provides a principled mathematical framework (via optimal transport) for robust CP under distribution shift. Unlike prior work that handles either local perturbations (adversarial examples) or global shifts (covariate shift) separately, Levy-Prokhorov ambiguity sets unify both. Authored by a team including Michael Jordan, signaling high theoretical quality.

---

### 8. Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks

- **Authors:** Xunlei Qian, Yue Xing
- **Venue:** Submitted to AISTATS 2026 (arXiv preprint, November 2025)
- **URL:** https://arxiv.org/abs/2511.18562
- **Summary:** Characterizes how adversarial perturbation strength during calibration affects coverage guarantees at test time, and shows that appropriate calibration-time attacks can maintain target coverage across varying test-time perturbation levels.
- **Why it matters:** Provides the first theoretical analysis specifically of how adversarial attacks on the calibration set propagate to test-time coverage. Key practical finding: adversarial training produces tighter, more informative prediction sets. Bridges the gap between adversarial robustness and CP calibration theory.

---

### 9. Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability (OPSA / OPSA-AT)

- **Authors:** Jie Bao, Chuangyin Dang, Rui Luo, Hanwei Zhang, Zhixin Zhou
- **Venue:** ICML 2025 (poster)
- **URL:** https://arxiv.org/abs/2506.07804
- **Summary:** Introduces OPSA (Optimal Size Attack), which maximizes prediction set size to undermine CP efficiency, and OPSA-AT, a defensive adversarial training framework that integrates OPSA into conformal training for robust prediction.
- **Why it matters:** Novel attack paradigm -- attacks prediction set *size* (efficiency) rather than coverage, which is practically more damaging since large sets are uninformative. The OPSA-AT defense represents a bilevel min-max training paradigm for robust CP. Accepted at ICML 2025.

---

### 10. Distribution-informed Online Conformal Prediction (COP)

- **Authors:** Dongjian Hu, Junxi Wu, Shu-Tao Xia, Changliang Zou
- **Venue:** ICLR 2026
- **URL:** https://arxiv.org/abs/2512.07770
- **Summary:** Proposes Conformal Optimistic Prediction (COP), an online CP method that incorporates estimated CDFs of non-conformity scores to produce tighter prediction sets under distribution shift while maintaining valid coverage even when estimates are wrong.
- **Why it matters:** Addresses the conservatism problem in online CP under distribution shift. Prior adversarial-setting online CP methods produced overly wide sets. COP provides joint bounds on coverage and regret with distribution-free finite-sample guarantees, and converges for i.i.d. scores. Accepted at ICLR 2026.

---

### 11. Conformal Prediction Beyond Exchangeability

- **Authors:** Rina Foygel Barber, Emmanuel J. Candes, Aaditya Ramdas, Ryan J. Tibshirani
- **Venue:** Annals of Statistics, 2023 (arXiv: February 2022)
- **URL:** https://arxiv.org/abs/2202.13415
- **Summary:** Extends conformal prediction to non-exchangeable settings using weighted quantiles for distribution drift and novel randomization techniques for asymmetric algorithms, with provably less coverage loss under exchangeability violations.
- **Why it matters:** Although published slightly before the 2024 window, this is the foundational theoretical paper that all subsequent robustness-under-distribution-shift work builds on. By four of the most prominent researchers in the field (Barber, Candes, Ramdas, Tibshirani), it defines the framework for non-exchangeable CP. Essential background for understanding papers 7, 8, and 10 above.

---

### 12. Conformal Prediction: A Data Perspective (Survey)

- **Authors:** Xiaofan Zhou, Baiting Chen, Yu Gui, Lu Cheng
- **Venue:** arXiv preprint / journal survey (October 2024, revised March 2025)
- **URL:** https://arxiv.org/abs/2410.06494
- **Summary:** Comprehensive 35-page survey of conformal prediction through a data-centric lens, covering structured, unstructured, and dynamic data, including discussion of robustness challenges.
- **Why it matters:** Useful as a broad reference and entry point. Covers the landscape of CP methods across data modalities and discusses challenges including adversarial robustness and scalability. Good for understanding where the robust CP subfield fits within the broader CP literature.

---

### Thematic Organization

**Attack papers (defining the threat):**
- Paper 2 (Li et al., ICML 2024): First poisoning attacks against CP
- Paper 9 (Bao et al., ICML 2025): OPSA -- attacks on set size/efficiency

**Defense: Poisoning robustness:**
- Paper 1 (Scholten & Gunnemann, ICLR 2025): RPS -- provable defenses under training + calibration poisoning
- Paper 3 (Zargarbashi et al., ICML 2024): Tight robust sets under evasion + poisoning

**Defense: Adversarial robustness (evasion):**
- Paper 4 (Jeary et al., NeurIPS 2024): VRCP via neural network verification
- Paper 5 (Kang et al., ICLR 2024): COLEP via probabilistic circuits
- Paper 6 (Yan et al., 2024): RSCP+ with efficiency improvements
- Paper 8 (Qian & Xing, 2025): Calibration robustness analysis
- Paper 9 (Bao et al., ICML 2025): OPSA-AT defensive training

**Defense: Distribution shift robustness:**
- Paper 7 (Aolaritei et al., NeurIPS 2025): Levy-Prokhorov ambiguity sets
- Paper 10 (Hu et al., ICLR 2026): Online CP with distributional awareness
- Paper 11 (Barber et al., AoS 2023): Foundational non-exchangeable CP

**Survey:**
- Paper 12 (Zhou et al., 2024--2025): Broad CP survey with data perspective

agentId: a532b251f86c87248 (use SendMessage with to: 'a532b251f86c87248' to continue this agent)
&lt;usage>total_tokens: 24425
tool_uses: 22
duration_ms: 136133&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52d8807e-79d8-4b78-b8f0-df7306652912",
  "isSidechain": false,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "type": "user",
  "uuid": "c9c67351-79cf-4ffc-810d-eff6fb658b41",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on robust conformal prediction, especially under data poisoning and distribution shift. Search for papers from 2024-2026.\n\nExecute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:\n\n1. Search: \"robust conformal prediction data poisoning 2024 2025 2026\"\n2. Search: \"conformal prediction distribution shift adversarial 2025 2026\"\n3. Search: \"provably reliable conformal prediction poisoning ICLR 2025\"\n4. Search: \"conformal prediction exchangeability violation robust\"\n5. Search: \"distribution-free prediction adversarial robustness 2025 2026\"\n\nFor each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers about making conformal prediction robust to adversarial manipulation, poisoning, or distribution shift.",
    "agentId": "a532b251f86c87248",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to compile a comprehensive structured list. Here is the literature survey.\n\n---\n\n## Literature Survey: Robust Conformal Prediction under Adversarial Manipulation, Poisoning, and Distribution Shift (2024--2026)\n\n---\n\n### 1. Provably Reliable Conformal Prediction Sets in the Presence of Data Poisoning\n\n- **Authors:** Yan Scholten, Stephan Gunnemann\n- **Venue:** ICLR 2025 (Spotlight)\n- **URL:** https://arxiv.org/abs/2410.09878\n- **Code:** https://github.com/yascho/reliable_conformal_prediction\n- **Summary:** Proposes Reliable Prediction Sets (RPS), the first scalable method for conformal prediction with provable reliability guarantees under both training and calibration data poisoning.\n- **Why it matters:** This is the foundational defense paper for CP under poisoning. It introduces smoothed score functions (aggregating across training partitions) for training poisoning and majority voting across calibration subsets for calibration poisoning. It provides formal certificates of reliability under worst-case poisoning, including label-flipping attacks. As an ICLR Spotlight, it is the highest-profile paper in this specific subfield.\n\n---\n\n### 2. Data Poisoning Attacks against Conformal Prediction\n\n- **Authors:** Yangyi Li, Aobo Chen, Wei Qian, Chenxu Zhao, Divya Lidder, Mengdi Huai\n- **Venue:** ICML 2024 (Proceedings of Machine Learning Research, Vol. 235, pp. 27563--27574)\n- **URL:** https://proceedings.mlr.press/v235/li24l.html\n- **Summary:** Introduces the first black-box data poisoning attacks specifically designed to manipulate conformal prediction uncertainty (prediction set size), rather than causing misclassifications.\n- **Why it matters:** This paper defines the threat model. Prior poisoning attacks targeted accuracy; this work shows that an adversary can directly manipulate the prediction sets (making them vacuously large or dangerously small) via poisoning. It demonstrates that existing defenses are ineffective, motivating the defensive works that follow.\n\n---\n\n### 3. Robust Yet Efficient Conformal Prediction Sets\n\n- **Authors:** Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski\n- **Venue:** ICML 2024\n- **URL:** https://arxiv.org/abs/2407.09165\n- **Summary:** Derives provably robust conformal prediction sets by bounding the worst-case change in conformity scores, producing tighter sets that handle both evasion and poisoning attacks on features and labels.\n- **Why it matters:** Addresses the efficiency problem -- prior robust CP methods produced overly conservative (large) sets. This work achieves tighter bounds for both continuous and discrete/sparse data while maintaining provable guarantees against evasion and poisoning.\n\n---\n\n### 4. Verifiably Robust Conformal Prediction (VRCP)\n\n- **Authors:** Linus Jeary, Tom Kuipers, Mehran Hosseini, Nicola Paoletti\n- **Venue:** NeurIPS 2024\n- **URL:** https://arxiv.org/abs/2405.18942\n- **Summary:** Combines conformal prediction with neural network verification to recover probabilistic coverage guarantees under adversarial perturbations; first method to handle arbitrary norms (l1, l2, l-infinity) and regression tasks.\n- **Why it matters:** Prior approaches (based on randomized smoothing) were limited to l2-bounded perturbations and classification only. VRCP uses formal verification to provide exact (non-conservative) robustness guarantees. It also automatically provides robustness against feature poisoning attacks. Demonstrated on CIFAR-10/100, TinyImageNet, and deep RL regression.\n\n---\n\n### 5. COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits\n\n- **Authors:** Mintong Kang, Nezihe Merve Gurel, Linyi Li, Bo Li\n- **Venue:** ICLR 2024\n- **URL:** https://arxiv.org/abs/2403.11348\n- **Summary:** Combines learning and reasoning via probabilistic circuits to achieve certifiably robust conformal prediction under bounded adversarial perturbations, with up to 14% coverage improvement on benchmark datasets.\n- **Why it matters:** Introduces a neuro-symbolic approach to robust CP. By encoding semantic concept relationships through probabilistic circuits, it provides theoretical coverage guarantees under perturbation while improving accuracy over single models. Demonstrates gains on GTSRB, CIFAR-10, and AwA2.\n\n---\n\n### 6. Provably Robust Conformal Prediction with Improved Efficiency\n\n- **Authors:** Ge Yan, Yaniv Romano, Tsui-Wei Weng\n- **Venue:** arXiv preprint (April 2024)\n- **URL:** https://arxiv.org/abs/2404.19651\n- **Summary:** Corrects flaws in prior RSCP robustness guarantees and introduces RSCP+ with two efficiency techniques (Post-Training Transformation and Robust Conformal Training), achieving up to 16.9x efficiency gains on ImageNet.\n- **Why it matters:** Identifies and fixes theoretical issues in the original Randomized Smoothed Conformal Prediction (RSCP) framework. The efficiency improvements (PTT and RCT) are critical for practical deployment -- prior robust CP methods produced prediction sets so large they were uninformative. Validated on CIFAR-10, CIFAR-100, and ImageNet.\n\n---\n\n### 7. Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations\n\n- **Authors:** Liviu Aolaritei, Qianyu Julie Zhu, Zheyu Oliver Wang, Michael I. Jordan, Youssef Marzouk\n- **Venue:** NeurIPS 2025\n- **URL:** https://arxiv.org/abs/2502.14105 | https://openreview.net/forum?id=1ULQvdbZ3X\n- **Summary:** Models distribution shifts via Levy-Prokhorov ambiguity sets capturing both local and global perturbations, and reduces high-dimensional distribution shifts to one-dimensional shifts through the scoring function for tractable robust coverage guarantees.\n- **Why it matters:** Provides a principled mathematical framework (via optimal transport) for robust CP under distribution shift. Unlike prior work that handles either local perturbations (adversarial examples) or global shifts (covariate shift) separately, Levy-Prokhorov ambiguity sets unify both. Authored by a team including Michael Jordan, signaling high theoretical quality.\n\n---\n\n### 8. Ensuring Calibration Robustness in Split Conformal Prediction Under Adversarial Attacks\n\n- **Authors:** Xunlei Qian, Yue Xing\n- **Venue:** Submitted to AISTATS 2026 (arXiv preprint, November 2025)\n- **URL:** https://arxiv.org/abs/2511.18562\n- **Summary:** Characterizes how adversarial perturbation strength during calibration affects coverage guarantees at test time, and shows that appropriate calibration-time attacks can maintain target coverage across varying test-time perturbation levels.\n- **Why it matters:** Provides the first theoretical analysis specifically of how adversarial attacks on the calibration set propagate to test-time coverage. Key practical finding: adversarial training produces tighter, more informative prediction sets. Bridges the gap between adversarial robustness and CP calibration theory.\n\n---\n\n### 9. Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability (OPSA / OPSA-AT)\n\n- **Authors:** Jie Bao, Chuangyin Dang, Rui Luo, Hanwei Zhang, Zhixin Zhou\n- **Venue:** ICML 2025 (poster)\n- **URL:** https://arxiv.org/abs/2506.07804\n- **Summary:** Introduces OPSA (Optimal Size Attack), which maximizes prediction set size to undermine CP efficiency, and OPSA-AT, a defensive adversarial training framework that integrates OPSA into conformal training for robust prediction.\n- **Why it matters:** Novel attack paradigm -- attacks prediction set *size* (efficiency) rather than coverage, which is practically more damaging since large sets are uninformative. The OPSA-AT defense represents a bilevel min-max training paradigm for robust CP. Accepted at ICML 2025.\n\n---\n\n### 10. Distribution-informed Online Conformal Prediction (COP)\n\n- **Authors:** Dongjian Hu, Junxi Wu, Shu-Tao Xia, Changliang Zou\n- **Venue:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2512.07770\n- **Summary:** Proposes Conformal Optimistic Prediction (COP), an online CP method that incorporates estimated CDFs of non-conformity scores to produce tighter prediction sets under distribution shift while maintaining valid coverage even when estimates are wrong.\n- **Why it matters:** Addresses the conservatism problem in online CP under distribution shift. Prior adversarial-setting online CP methods produced overly wide sets. COP provides joint bounds on coverage and regret with distribution-free finite-sample guarantees, and converges for i.i.d. scores. Accepted at ICLR 2026.\n\n---\n\n### 11. Conformal Prediction Beyond Exchangeability\n\n- **Authors:** Rina Foygel Barber, Emmanuel J. Candes, Aaditya Ramdas, Ryan J. Tibshirani\n- **Venue:** Annals of Statistics, 2023 (arXiv: February 2022)\n- **URL:** https://arxiv.org/abs/2202.13415\n- **Summary:** Extends conformal prediction to non-exchangeable settings using weighted quantiles for distribution drift and novel randomization techniques for asymmetric algorithms, with provably less coverage loss under exchangeability violations.\n- **Why it matters:** Although published slightly before the 2024 window, this is the foundational theoretical paper that all subsequent robustness-under-distribution-shift work builds on. By four of the most prominent researchers in the field (Barber, Candes, Ramdas, Tibshirani), it defines the framework for non-exchangeable CP. Essential background for understanding papers 7, 8, and 10 above.\n\n---\n\n### 12. Conformal Prediction: A Data Perspective (Survey)\n\n- **Authors:** Xiaofan Zhou, Baiting Chen, Yu Gui, Lu Cheng\n- **Venue:** arXiv preprint / journal survey (October 2024, revised March 2025)\n- **URL:** https://arxiv.org/abs/2410.06494\n- **Summary:** Comprehensive 35-page survey of conformal prediction through a data-centric lens, covering structured, unstructured, and dynamic data, including discussion of robustness challenges.\n- **Why it matters:** Useful as a broad reference and entry point. Covers the landscape of CP methods across data modalities and discusses challenges including adversarial robustness and scalability. Good for understanding where the robust CP subfield fits within the broader CP literature.\n\n---\n\n### Thematic Organization\n\n**Attack papers (defining the threat):**\n- Paper 2 (Li et al., ICML 2024): First poisoning attacks against CP\n- Paper 9 (Bao et al., ICML 2025): OPSA -- attacks on set size/efficiency\n\n**Defense: Poisoning robustness:**\n- Paper 1 (Scholten & Gunnemann, ICLR 2025): RPS -- provable defenses under training + calibration poisoning\n- Paper 3 (Zargarbashi et al., ICML 2024): Tight robust sets under evasion + poisoning\n\n**Defense: Adversarial robustness (evasion):**\n- Paper 4 (Jeary et al., NeurIPS 2024): VRCP via neural network verification\n- Paper 5 (Kang et al., ICLR 2024): COLEP via probabilistic circuits\n- Paper 6 (Yan et al., 2024): RSCP+ with efficiency improvements\n- Paper 8 (Qian & Xing, 2025): Calibration robustness analysis\n- Paper 9 (Bao et al., ICML 2025): OPSA-AT defensive training\n\n**Defense: Distribution shift robustness:**\n- Paper 7 (Aolaritei et al., NeurIPS 2025): Levy-Prokhorov ambiguity sets\n- Paper 10 (Hu et al., ICLR 2026): Online CP with distributional awareness\n- Paper 11 (Barber et al., AoS 2023): Foundational non-exchangeable CP\n\n**Survey:**\n- Paper 12 (Zhou et al., 2024--2025): Broad CP survey with data perspective"
      }
    ],
    "totalDurationMs": 136133,
    "totalTokens": 24425,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 916,
      "cache_read_input_tokens": 20329,
      "output_tokens": 3179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 916
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3179,
          "cache_read_input_tokens": 20329,
          "cache_creation_input_tokens": 916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 916,
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
  "sourceToolAssistantUUID": "52d8807e-79d8-4b78-b8f0-df7306652912",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "c9c67351-79cf-4ffc-810d-eff6fb658b41",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on conformal prediction for RAG",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Tool result

_source line 23 · 2026-05-30T06:15:26.060Z_

<details><summary>↩ Tool result · `toolu_01ETzPNkMZYXm1ZKMfwz3HH8`</summary>

```text
I now have comprehensive information on all the key papers. Here is the structured literature survey.

---

## Literature Survey: Conformal Prediction for RAG and LLM Systems (2024--2026)

### TIER 1: Papers directly combining Conformal Prediction with RAG

---

**1. TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction**

- **Authors:** Shuo Li, Sangdon Park, Insup Lee, Osbert Bastani
- **Venue:** NAACL 2024
- **URL:** https://arxiv.org/abs/2307.04642
- **Summary:** First end-to-end statistical correctness guarantee for RAG; constructs prediction sets guaranteed to contain a semantically correct answer using conformal prediction, and uses Bayesian optimization to minimize set size (16.2% reduction).
- **Why important:** Foundational paper -- the first to apply conformal prediction end-to-end across both retrieval and generation in RAG, establishing the paradigm for the field.

---

**2. C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models**

- **Authors:** Mintong Kang, Nezihe Merve Gurel, Ning Yu, Dawn Song, Bo Li
- **Venue:** ICML 2024
- **URL:** https://arxiv.org/abs/2402.03181
- **Summary:** First framework to certify generation risks for RAG via conformal risk analysis; proves RAG achieves lower conformal generation risk than standalone LLMs when retrieval quality is non-trivial; provides guarantees under distribution shift.
- **Why important:** Provides the theoretical backbone -- certified upper confidence bounds on generation risk -- that underpins formal safety analysis of RAG systems.

---

**3. CONFLARE: CONFormal LArge language model REtrieval**

- **Authors:** Pouria Rouzrokh, Shahriar Faghani, Cooper U. Gamble, Moein Shariatnia, Bradley J. Erickson
- **Venue:** arXiv preprint, April 2024
- **URL:** https://arxiv.org/abs/2404.04287
- **Summary:** Applies conformal prediction to the retrieval step of RAG, establishing a similarity-score threshold at a user-specified error rate alpha so that the retrieved chunks are guaranteed to contain the true answer with (1-alpha) confidence.
- **Why important:** Focuses specifically on making the retrieval component conformally valid, complementing approaches that target generation. Provides a lightweight, practical Python implementation.

---

**4. Conformal-RAG: Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality**

- **Authors:** Naihe Feng, Yi Sui, Shiyi Hou, Jesse C. Cresswell, Ga Wu
- **Venue:** SIGIR 2025 (short paper)
- **URL:** https://arxiv.org/abs/2506.20978
- **Summary:** Combines conformal prediction with RAG-internal information to assess sub-claim quality; retains up to 60% more high-quality sub-claims than naive CP applied to LLMs, with group-conditional coverage across sub-domains and no manual labeling.
- **Why important:** Moves beyond whole-answer guarantees to sub-claim-level factuality assessment within RAG, which is essential for long-form generation where individual claims may be independently correct or incorrect.

---

**5. Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights**

- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak
- **Venue:** ICLR 2026
- **URL:** https://openreview.net/forum?id=OKnM5rEUbg
- **Summary:** Integrates conformal factuality filtering with RAG and introduces three new evaluation metrics (non-empty rate, non-vacuous empirical factuality, sufficient correctness) that reveal trade-offs standard metrics miss between correctness and informativeness.
- **Why important:** Provides the first rigorous empirical analysis showing that standard factuality metrics are inadequate for evaluating conformal-RAG systems; the new metrics have become a reference framework for subsequent work.

---

**6. Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights**

- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak
- **Venue:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2603.16817
- **Summary:** Stress-tests conformal factuality for RAG under distribution shifts and distractors; finds guarantees break down, vacuous outputs dominate at high factuality levels, and simpler entailment-based verifiers outperform LLM scorers at 100x fewer FLOPs.
- **Why important:** Critical "reality check" paper -- exposes fragility in conformal-RAG guarantees under realistic deployment conditions, setting the agenda for more robust methods.

---

**7. Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction**

- **Authors:** Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, Kevin Duh
- **Venue:** ECIR 2026
- **URL:** https://arxiv.org/abs/2511.17908
- **Summary:** Uses conformal prediction to filter retrieved evidence in RAG, reducing context length by 2--3x while maintaining statistical coverage guarantees that a target fraction of relevant snippets are retained; improves factual accuracy by removing noise.
- **Why important:** Addresses the practical problem of context window overload in RAG via a principled, model-agnostic filtering approach with formal coverage control.

---

**8. URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models**

- **Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang
- **Venue:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2603.19281
- **Summary:** Comprehensive benchmark evaluating 8 RAG methods across healthcare, programming, and math using conformal prediction to obtain statistically valid uncertainty scores; finds accuracy-uncertainty correlation breaks under retrieval errors and simpler modular methods often outperform complex reasoning approaches.
- **Why important:** First standardized benchmark for uncertainty quantification in RAG, enabling systematic comparison of methods and identifying failure modes.

---

### TIER 2: Conformal Prediction for LLM Factuality and Abstention (directly applicable to RAG)

---

**9. Language Models with Conformal Factuality Guarantees**

- **Authors:** Christopher Mohri, Tatsunori Hashimoto
- **Venue:** arXiv preprint, February 2024
- **URL:** https://arxiv.org/abs/2402.10978
- **Summary:** Introduces "conformal factuality" -- a back-off algorithm that makes LLM outputs progressively less specific to expand uncertainty sets until correctness is guaranteed; achieves 80--90% correctness guarantees on QA and math reasoning with any black-box LLM.
- **Why important:** Seminal paper defining the conformal factuality framework that most subsequent RAG+CP papers build upon; the back-off mechanism is now a standard technique in the field.

---

**10. Conformal Linguistic Calibration: Trading-off between Factuality and Specificity**

- **Authors:** Zhengping Jiang, Anqi Liu, Benjamin Van Durme
- **Venue:** arXiv preprint, February 2025 (revised August 2025)
- **URL:** https://arxiv.org/abs/2502.19110
- **Summary:** Reframes linguistic calibration as answer set prediction; connects abstention and hedging through pragmatics; enables fine-tuned models to do uncertainty-aware adaptive claim rewriting with conformal guarantees on factual accuracy.
- **Why important:** Bridges the gap between hard abstention (refuse to answer) and soft calibration (hedge the answer), offering a nuanced middle ground particularly relevant for RAG systems that should communicate uncertainty rather than simply abstain.

---

**11. ConU: Conformal Uncertainty in Large Language Models with Correctness Coverage Guarantees**

- **Authors:** Zhiyuan Wang, Jinhao Duan, Lu Cheng, Yue Zhang, Qingni Wang, Xiaoshuang Shi, Kaidi Xu, Hengtao Shen, Xiaofeng Zhu
- **Venue:** EMNLP 2024 Findings
- **URL:** https://arxiv.org/abs/2407.00499
- **Summary:** Proposes a self-consistency-based uncertainty measure for black-box LLMs with conformal prediction to achieve strict correctness coverage control; evaluated on 7 LLMs across 4 datasets in general and medical domains.
- **Why important:** Provides a practical, model-agnostic uncertainty measure that can be directly plugged into RAG pipelines to decide when to trust or reject generated answers.

---

**12. Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models**

- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi
- **Venue:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.06884
- **Summary:** Uses reinforcement learning to dynamically optimize conformal abstention thresholds rather than using fixed ones; achieves up to 3.2% accuracy gain, 22.19% hallucination detection improvement, and 70--85% calibration error reduction while meeting 90% coverage targets.
- **Why important:** Moves beyond static thresholds to learned, adaptive abstention policies -- directly applicable to RAG systems that must decide when to abstain vs. answer in varying deployment conditions.

---

**13. Geometry-Calibrated Conformal Abstention for Language Models**

- **Authors:** Rui Xu, Yi Chen, Sihong Xie, Hui Xiong
- **Venue:** arXiv preprint, April 2026
- **URL:** https://arxiv.org/abs/2604.27914
- **Summary:** Post-hoc conformal abstention framework that uses representation geometry (how much the model's actual knowledge contributes to a response) instead of non-conformity scores; achieves 75% conditional correctness with selective answering.
- **Why important:** Novel use of internal representation geometry for conformal calibration, addressing the fundamental challenge that non-conformity scores are impractical for open-ended generation.

---

**14. Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models**

- **Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov, Maxim Panov
- **Venue:** arXiv preprint, April 2026
- **URL:** https://arxiv.org/abs/2604.13991
- **Summary:** Prompt-adaptive conformal prediction that enables prompt-dependent calibration for LLMs; improves conditional coverage over existing methods while retaining marginal coverage guarantees; supports selective prediction for filtering unreliable claims.
- **Why important:** Addresses a key limitation of prior work (uniform calibration across all inputs) by making conformal thresholds adapt to each prompt, which is critical for RAG where query difficulty varies enormously.

---

**15. Differentiable Conformal Training for LLM Reasoning Factuality**

- **Authors:** Nathan Hittesdorf, Marco Salzetta, Lu Cheng
- **Venue:** arXiv preprint, April 2026
- **URL:** https://arxiv.org/abs/2604.20098
- **Summary:** Makes conformal factuality fully differentiable (Differentiable Coherent Factuality -- DCF), enabling learning of better scoring mechanisms during training; achieves up to 141% improvement in claim retention while maintaining reliability guarantees.
- **Why important:** First paper to make conformal factuality end-to-end differentiable, enabling joint optimization of scoring and filtering rather than treating them as separate post-hoc steps.

---

**16. Conformal Language Model Reasoning with Coherent Factuality**

- **Authors:** Maxon Rubin-Toles, Maya Gambhir, Keshav Ramji, Aaron Roth, Surbhi Goel
- **Venue:** arXiv preprint, May 2025
- **URL:** https://arxiv.org/abs/2505.17126
- **Summary:** Introduces "coherent factuality" -- evaluating claims within their logical reasoning context rather than in isolation using deducibility graphs; achieves 90% factuality while retaining 80%+ of original claims on math reasoning tasks.
- **Why important:** Extends conformal factuality from isolated claim checking to multi-step reasoning chains, which is essential for RAG systems used in complex reasoning tasks where claim dependencies matter.

---

**17. Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations**

- **Authors:** Yanli Wang, Peng Kuang, Xiaoyu Han, Kaidi Xu, Haohan Wang
- **Venue:** arXiv preprint, April 2026
- **URL:** https://arxiv.org/abs/2604.16217
- **Summary:** Uses layer-wise information scores from internal model representations as conformal scores instead of output-level signals (token probabilities, entropy); shows superior validity-efficiency trade-offs especially under distribution shift.
- **Why important:** Demonstrates that internal representations provide more robust conformal scores than surface-level uncertainty, which is particularly relevant for RAG systems where distribution shift between calibration and deployment data is common.

---

### TIER 3: Survey

---

**18. Towards Trustworthy Retrieval Augmented Generation for Large Language Models: A Survey**

- **Authors:** Bo Ni, Zheyuan Liu, Leyao Wang, et al. (20+ authors)
- **Venue:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.06872
- **Summary:** Comprehensive survey organizing RAG trustworthiness around six dimensions (reliability, privacy, safety, fairness, explainability, accountability); covers conformal prediction methods among other approaches.
- **Why important:** Provides the broader context for where conformal prediction fits within the full landscape of trustworthy RAG research; useful for positioning any new work in the area.

---

### Key Takeaways for the Field

1. **The pipeline has two natural CP injection points:** the retrieval step (CONFLARE, Principled Context Engineering) and the generation step (conformal factuality, TRAQ). The best systems address both (TRAQ, Conformal-RAG).

2. **The factuality-informativeness trade-off is the central challenge:** Conformal guarantees can be achieved, but often at the cost of vacuous or overly hedged outputs (Chen et al., 2026). New metrics beyond simple coverage are needed.

3. **Robustness under distribution shift remains unsolved:** C-RAG provides theoretical bounds under shift, but empirical work (Chen et al., March 2026) shows practical fragility.

4. **The frontier is moving toward:** (a) adaptive/prompt-dependent calibration (Rubashevskii et al., 2026), (b) differentiable conformal training (Hittesdorf et al., 2026), (c) internal-representation-based scores (Wang et al., 2026), and (d) coherent multi-step reasoning guarantees (Rubin-Toles et al., 2025).

agentId: a38362145d53a1294 (use SendMessage with to: 'a38362145d53a1294' to continue this agent)
&lt;usage>total_tokens: 27198
tool_uses: 26
duration_ms: 156244&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98fbd72b-712f-4625-b78d-cc236d3ceec3",
  "isSidechain": false,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "type": "user",
  "uuid": "13676a49-f76a-480b-8f4f-8c3a022614a8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on conformal prediction for RAG systems. Search for and analyze papers from 2024-2026.\n\nExecute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:\n\n1. Search: \"conformal prediction retrieval augmented generation 2024 2025 2026\"\n2. Search: \"TRAQ conformal prediction RAG trustworthy\"\n3. Search: \"C-RAG certified generation risks retrieval augmented language models\"\n4. Search: \"conformal prediction LLM factuality 2025 2026\"\n5. Search: \"conformal prediction natural language generation abstention\"\n\nFor each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers that combine conformal prediction with RAG or LLM systems.",
    "agentId": "a38362145d53a1294",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all the key papers. Here is the structured literature survey.\n\n---\n\n## Literature Survey: Conformal Prediction for RAG and LLM Systems (2024--2026)\n\n### TIER 1: Papers directly combining Conformal Prediction with RAG\n\n---\n\n**1. TRAQ: Trustworthy Retrieval Augmented Question Answering via Conformal Prediction**\n\n- **Authors:** Shuo Li, Sangdon Park, Insup Lee, Osbert Bastani\n- **Venue:** NAACL 2024\n- **URL:** https://arxiv.org/abs/2307.04642\n- **Summary:** First end-to-end statistical correctness guarantee for RAG; constructs prediction sets guaranteed to contain a semantically correct answer using conformal prediction, and uses Bayesian optimization to minimize set size (16.2% reduction).\n- **Why important:** Foundational paper -- the first to apply conformal prediction end-to-end across both retrieval and generation in RAG, establishing the paradigm for the field.\n\n---\n\n**2. C-RAG: Certified Generation Risks for Retrieval-Augmented Language Models**\n\n- **Authors:** Mintong Kang, Nezihe Merve Gurel, Ning Yu, Dawn Song, Bo Li\n- **Venue:** ICML 2024\n- **URL:** https://arxiv.org/abs/2402.03181\n- **Summary:** First framework to certify generation risks for RAG via conformal risk analysis; proves RAG achieves lower conformal generation risk than standalone LLMs when retrieval quality is non-trivial; provides guarantees under distribution shift.\n- **Why important:** Provides the theoretical backbone -- certified upper confidence bounds on generation risk -- that underpins formal safety analysis of RAG systems.\n\n---\n\n**3. CONFLARE: CONFormal LArge language model REtrieval**\n\n- **Authors:** Pouria Rouzrokh, Shahriar Faghani, Cooper U. Gamble, Moein Shariatnia, Bradley J. Erickson\n- **Venue:** arXiv preprint, April 2024\n- **URL:** https://arxiv.org/abs/2404.04287\n- **Summary:** Applies conformal prediction to the retrieval step of RAG, establishing a similarity-score threshold at a user-specified error rate alpha so that the retrieved chunks are guaranteed to contain the true answer with (1-alpha) confidence.\n- **Why important:** Focuses specifically on making the retrieval component conformally valid, complementing approaches that target generation. Provides a lightweight, practical Python implementation.\n\n---\n\n**4. Conformal-RAG: Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality**\n\n- **Authors:** Naihe Feng, Yi Sui, Shiyi Hou, Jesse C. Cresswell, Ga Wu\n- **Venue:** SIGIR 2025 (short paper)\n- **URL:** https://arxiv.org/abs/2506.20978\n- **Summary:** Combines conformal prediction with RAG-internal information to assess sub-claim quality; retains up to 60% more high-quality sub-claims than naive CP applied to LLMs, with group-conditional coverage across sub-domains and no manual labeling.\n- **Why important:** Moves beyond whole-answer guarantees to sub-claim-level factuality assessment within RAG, which is essential for long-form generation where individual claims may be independently correct or incorrect.\n\n---\n\n**5. Understanding Conformal Factuality for RAG-based LLMs: Novel Metrics and Systematic Insights**\n\n- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak\n- **Venue:** ICLR 2026\n- **URL:** https://openreview.net/forum?id=OKnM5rEUbg\n- **Summary:** Integrates conformal factuality filtering with RAG and introduces three new evaluation metrics (non-empty rate, non-vacuous empirical factuality, sufficient correctness) that reveal trade-offs standard metrics miss between correctness and informativeness.\n- **Why important:** Provides the first rigorous empirical analysis showing that standard factuality metrics are inadequate for evaluating conformal-RAG systems; the new metrics have become a reference framework for subsequent work.\n\n---\n\n**6. Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights**\n\n- **Authors:** Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar, Caitlyn Heqi Yin, Ramya Korlakai Vinayak\n- **Venue:** arXiv preprint, March 2026\n- **URL:** https://arxiv.org/abs/2603.16817\n- **Summary:** Stress-tests conformal factuality for RAG under distribution shifts and distractors; finds guarantees break down, vacuous outputs dominate at high factuality levels, and simpler entailment-based verifiers outperform LLM scorers at 100x fewer FLOPs.\n- **Why important:** Critical \"reality check\" paper -- exposes fragility in conformal-RAG guarantees under realistic deployment conditions, setting the agenda for more robust methods.\n\n---\n\n**7. Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction**\n\n- **Authors:** Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, Kevin Duh\n- **Venue:** ECIR 2026\n- **URL:** https://arxiv.org/abs/2511.17908\n- **Summary:** Uses conformal prediction to filter retrieved evidence in RAG, reducing context length by 2--3x while maintaining statistical coverage guarantees that a target fraction of relevant snippets are retained; improves factual accuracy by removing noise.\n- **Why important:** Addresses the practical problem of context window overload in RAG via a principled, model-agnostic filtering approach with formal coverage control.\n\n---\n\n**8. URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models**\n\n- **Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang\n- **Venue:** arXiv preprint, March 2026\n- **URL:** https://arxiv.org/abs/2603.19281\n- **Summary:** Comprehensive benchmark evaluating 8 RAG methods across healthcare, programming, and math using conformal prediction to obtain statistically valid uncertainty scores; finds accuracy-uncertainty correlation breaks under retrieval errors and simpler modular methods often outperform complex reasoning approaches.\n- **Why important:** First standardized benchmark for uncertainty quantification in RAG, enabling systematic comparison of methods and identifying failure modes.\n\n---\n\n### TIER 2: Conformal Prediction for LLM Factuality and Abstention (directly applicable to RAG)\n\n---\n\n**9. Language Models with Conformal Factuality Guarantees**\n\n- **Authors:** Christopher Mohri, Tatsunori Hashimoto\n- **Venue:** arXiv preprint, February 2024\n- **URL:** https://arxiv.org/abs/2402.10978\n- **Summary:** Introduces \"conformal factuality\" -- a back-off algorithm that makes LLM outputs progressively less specific to expand uncertainty sets until correctness is guaranteed; achieves 80--90% correctness guarantees on QA and math reasoning with any black-box LLM.\n- **Why important:** Seminal paper defining the conformal factuality framework that most subsequent RAG+CP papers build upon; the back-off mechanism is now a standard technique in the field.\n\n---\n\n**10. Conformal Linguistic Calibration: Trading-off between Factuality and Specificity**\n\n- **Authors:** Zhengping Jiang, Anqi Liu, Benjamin Van Durme\n- **Venue:** arXiv preprint, February 2025 (revised August 2025)\n- **URL:** https://arxiv.org/abs/2502.19110\n- **Summary:** Reframes linguistic calibration as answer set prediction; connects abstention and hedging through pragmatics; enables fine-tuned models to do uncertainty-aware adaptive claim rewriting with conformal guarantees on factual accuracy.\n- **Why important:** Bridges the gap between hard abstention (refuse to answer) and soft calibration (hedge the answer), offering a nuanced middle ground particularly relevant for RAG systems that should communicate uncertainty rather than simply abstain.\n\n---\n\n**11. ConU: Conformal Uncertainty in Large Language Models with Correctness Coverage Guarantees**\n\n- **Authors:** Zhiyuan Wang, Jinhao Duan, Lu Cheng, Yue Zhang, Qingni Wang, Xiaoshuang Shi, Kaidi Xu, Hengtao Shen, Xiaofeng Zhu\n- **Venue:** EMNLP 2024 Findings\n- **URL:** https://arxiv.org/abs/2407.00499\n- **Summary:** Proposes a self-consistency-based uncertainty measure for black-box LLMs with conformal prediction to achieve strict correctness coverage control; evaluated on 7 LLMs across 4 datasets in general and medical domains.\n- **Why important:** Provides a practical, model-agnostic uncertainty measure that can be directly plugged into RAG pipelines to decide when to trust or reject generated answers.\n\n---\n\n**12. Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models**\n\n- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi\n- **Venue:** arXiv preprint, February 2025\n- **URL:** https://arxiv.org/abs/2502.06884\n- **Summary:** Uses reinforcement learning to dynamically optimize conformal abstention thresholds rather than using fixed ones; achieves up to 3.2% accuracy gain, 22.19% hallucination detection improvement, and 70--85% calibration error reduction while meeting 90% coverage targets.\n- **Why important:** Moves beyond static thresholds to learned, adaptive abstention policies -- directly applicable to RAG systems that must decide when to abstain vs. answer in varying deployment conditions.\n\n---\n\n**13. Geometry-Calibrated Conformal Abstention for Language Models**\n\n- **Authors:** Rui Xu, Yi Chen, Sihong Xie, Hui Xiong\n- **Venue:** arXiv preprint, April 2026\n- **URL:** https://arxiv.org/abs/2604.27914\n- **Summary:** Post-hoc conformal abstention framework that uses representation geometry (how much the model's actual knowledge contributes to a response) instead of non-conformity scores; achieves 75% conditional correctness with selective answering.\n- **Why important:** Novel use of internal representation geometry for conformal calibration, addressing the fundamental challenge that non-conformity scores are impractical for open-ended generation.\n\n---\n\n**14. Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models**\n\n- **Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov, Maxim Panov\n- **Venue:** arXiv preprint, April 2026\n- **URL:** https://arxiv.org/abs/2604.13991\n- **Summary:** Prompt-adaptive conformal prediction that enables prompt-dependent calibration for LLMs; improves conditional coverage over existing methods while retaining marginal coverage guarantees; supports selective prediction for filtering unreliable claims.\n- **Why important:** Addresses a key limitation of prior work (uniform calibration across all inputs) by making conformal thresholds adapt to each prompt, which is critical for RAG where query difficulty varies enormously.\n\n---\n\n**15. Differentiable Conformal Training for LLM Reasoning Factuality**\n\n- **Authors:** Nathan Hittesdorf, Marco Salzetta, Lu Cheng\n- **Venue:** arXiv preprint, April 2026\n- **URL:** https://arxiv.org/abs/2604.20098\n- **Summary:** Makes conformal factuality fully differentiable (Differentiable Coherent Factuality -- DCF), enabling learning of better scoring mechanisms during training; achieves up to 141% improvement in claim retention while maintaining reliability guarantees.\n- **Why important:** First paper to make conformal factuality end-to-end differentiable, enabling joint optimization of scoring and filtering rather than treating them as separate post-hoc steps.\n\n---\n\n**16. Conformal Language Model Reasoning with Coherent Factuality**\n\n- **Authors:** Maxon Rubin-Toles, Maya Gambhir, Keshav Ramji, Aaron Roth, Surbhi Goel\n- **Venue:** arXiv preprint, May 2025\n- **URL:** https://arxiv.org/abs/2505.17126\n- **Summary:** Introduces \"coherent factuality\" -- evaluating claims within their logical reasoning context rather than in isolation using deducibility graphs; achieves 90% factuality while retaining 80%+ of original claims on math reasoning tasks.\n- **Why important:** Extends conformal factuality from isolated claim checking to multi-step reasoning chains, which is essential for RAG systems used in complex reasoning tasks where claim dependencies matter.\n\n---\n\n**17. Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations**\n\n- **Authors:** Yanli Wang, Peng Kuang, Xiaoyu Han, Kaidi Xu, Haohan Wang\n- **Venue:** arXiv preprint, April 2026\n- **URL:** https://arxiv.org/abs/2604.16217\n- **Summary:** Uses layer-wise information scores from internal model representations as conformal scores instead of output-level signals (token probabilities, entropy); shows superior validity-efficiency trade-offs especially under distribution shift.\n- **Why important:** Demonstrates that internal representations provide more robust conformal scores than surface-level uncertainty, which is particularly relevant for RAG systems where distribution shift between calibration and deployment data is common.\n\n---\n\n### TIER 3: Survey\n\n---\n\n**18. Towards Trustworthy Retrieval Augmented Generation for Large Language Models: A Survey**\n\n- **Authors:** Bo Ni, Zheyuan Liu, Leyao Wang, et al. (20+ authors)\n- **Venue:** arXiv preprint, February 2025\n- **URL:** https://arxiv.org/abs/2502.06872\n- **Summary:** Comprehensive survey organizing RAG trustworthiness around six dimensions (reliability, privacy, safety, fairness, explainability, accountability); covers conformal prediction methods among other approaches.\n- **Why important:** Provides the broader context for where conformal prediction fits within the full landscape of trustworthy RAG research; useful for positioning any new work in the area.\n\n---\n\n### Key Takeaways for the Field\n\n1. **The pipeline has two natural CP injection points:** the retrieval step (CONFLARE, Principled Context Engineering) and the generation step (conformal factuality, TRAQ). The best systems address both (TRAQ, Conformal-RAG).\n\n2. **The factuality-informativeness trade-off is the central challenge:** Conformal guarantees can be achieved, but often at the cost of vacuous or overly hedged outputs (Chen et al., 2026). New metrics beyond simple coverage are needed.\n\n3. **Robustness under distribution shift remains unsolved:** C-RAG provides theoretical bounds under shift, but empirical work (Chen et al., March 2026) shows practical fragility.\n\n4. **The frontier is moving toward:** (a) adaptive/prompt-dependent calibration (Rubashevskii et al., 2026), (b) differentiable conformal training (Hittesdorf et al., 2026), (c) internal-representation-based scores (Wang et al., 2026), and (d) coherent multi-step reasoning guarantees (Rubin-Toles et al., 2025)."
      }
    ],
    "totalDurationMs": 156244,
    "totalTokens": 27198,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2103,
      "cache_read_input_tokens": 21198,
      "output_tokens": 3896,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3896,
          "cache_read_input_tokens": 21198,
          "cache_creation_input_tokens": 2103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2103,
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
  "sourceToolAssistantUUID": "98fbd72b-712f-4625-b78d-cc236d3ceec3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-30T06:16:23.931Z_

<details><summary>↩ Tool result · `toolu_01KJGXLsa36snUV88pDwHz2y`</summary>

```text
I now have comprehensive data on all the key papers. Here is the structured literature survey:

---

## Literature Survey: Adversarial Attacks and Certified Defenses for RAG Systems (2024--2026)

### ATTACK PAPERS

**1. PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models**
- **Authors:** Wei Zou, Runpeng Geng, Binghui Wang, Jinyuan Jia
- **Venue:** USENIX Security 2025
- **URL:** https://arxiv.org/abs/2402.07867
- **Why important:** The foundational paper that introduced knowledge-database poisoning attacks against RAG. Achieves 90% attack success rate by injecting only 5 malicious texts into a database of millions. Showed existing defenses are insufficient.
- **Summary:** Formulates corpus poisoning of RAG as an optimization problem with both black-box and white-box solutions, demonstrating that a small number of injected adversarial passages can reliably steer LLM outputs to attacker-chosen answers.

**2. Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation**
- **Authors:** Harsh Chaudhari, Giorgio Severi, John Abascal, Anshuman Suri, Matthew Jagielski, Christopher A. Choquette-Choo, Milad Nasr, Cristina Nita-Rotaru, Alina Oprea
- **Venue:** arXiv (cs.CR), 2024; validated on GPT-3.5/GPT-4 and production systems
- **URL:** https://arxiv.org/abs/2405.20485
- **Why important:** Demonstrates trigger-activated backdoor attacks on RAG systems that cause refusal, reputation damage, privacy violations, and harmful behaviors. Successfully tested on NVIDIA's "Chat with RTX" production system.
- **Summary:** A two-stage optimization crafts a single poisoned document that is retrieved only when specific trigger tokens appear in queries, enabling targeted harmful outputs while evading detection on clean queries.

**3. TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models**
- **Authors:** Pengzhou Cheng, Yidong Ding, Tianjie Ju, Zongru Wu, Wei Du, Ping Yi, Zhuosheng Zhang, Gongshen Liu
- **Venue:** arXiv (cs.CR), 2024
- **URL:** https://arxiv.org/abs/2405.13401
- **Why important:** Proposes a joint backdoor attack using contrastive learning to build orthogonal backdoor shortcuts between poisoned knowledge and triggers, enabling universal attack scenarios.
- **Summary:** Uses knowledge graphs for fine-grained matching to create multiple purpose-driven backdoors that maintain normal retrieval on clean queries while returning semantically consistent poisoned content for adversarial queries.

**4. CorruptRAG: Practical Poisoning Attacks against Retrieval-Augmented Generation**
- **Authors:** Baolei Zhang, Yuxi Chen, Zhuqing Liu, Lihai Nie, Tong Li, Zheli Liu, Minghong Fang
- **Venue:** ACM SACMAT 2026
- **URL:** https://arxiv.org/abs/2504.03957
- **Why important:** Advances attack practicality by requiring only a single injected poisoned text (vs. 5 in PoisonedRAG), making attacks more feasible and stealthier.
- **Summary:** A practical single-document poisoning attack against RAG systems that achieves higher attack success rates than existing baselines on large-scale datasets.

**5. DisarmRAG: Disabling Self-Correction in Retrieval-Augmented Generation via Stealthy Retriever Poisoning**
- **Authors:** Yanbo Dai, Zhenlan Ji, Zongjie Li, Kuan Li, Shuai Wang
- **Venue:** arXiv (cs.CR), August 2025
- **URL:** https://arxiv.org/abs/2508.20083
- **Why important:** Uniquely targets the retriever model itself (not the corpus), using contrastive learning to modify retriever behavior so it suppresses self-correction mechanisms in RAG. Over 90% attack success rate.
- **Summary:** Compromises the retriever via model editing so it returns malicious instructions for targeted queries while behaving normally otherwise, defeating self-correction and detection defenses.

**6. RIPRAG: Hack a Black-box RAG Question-Answering System with Reinforcement Learning**
- **Authors:** Meng Xi, Sihan Lv, Yechen Jin, Guanjie Cheng, Naibo Wang, Ying Li, Jianwei Yin
- **Venue:** arXiv (cs.AI), October 2025
- **URL:** https://arxiv.org/abs/2510.10008
- **Why important:** First RL-based black-box attack on RAG, treating the target system as a complete black box. Achieves up to 0.72 ASR improvement over baselines.
- **Summary:** Uses reinforcement learning with black-box feedback (similarity and attack rewards) to optimize poisoned document generation without access to model internals.

**7. "Someone Hid It": Query-Agnostic Black-Box Attacks on LLM-Based Retrieval**
- **Authors:** Jiate Li, Defu Cao, Li Li, Wei Yang, Yuehan Qin, Chenxiao Yu, Tiannuo Yang, Ryan A. Rossi, Yan Liu, Xiyang Hu, Yue Zhao
- **Venue:** arXiv (cs.CR), January 2026
- **URL:** https://arxiv.org/abs/2602.00364
- **Why important:** Query-agnostic attack that works without knowing victim queries or models, using zero-shot surrogate LLMs and adversarial learning for transferable injection tokens.
- **Summary:** Formulates transferable attacks on LLM-based retrieval as a min-max optimization problem, generating adversarial tokens that transfer across different LLM retrievers without query knowledge.

**8. GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search**
- **Authors:** Matan Ben-Tov, Mahmood Sharif
- **Venue:** ACM CCS 2025
- **URL:** https://arxiv.org/abs/2412.20953
- **Why important:** Demonstrates that dense retrieval systems are catastrophically vulnerable even at poisoning levels as low as 0.0001% of the corpus. Published at a top security venue.
- **Summary:** Generates adversarial passages without model or corpus knowledge that achieve high rankings; single-query attacks are 100% successful, and standard defenses fail against adaptive versions.

**9. Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval**
- **Authors:** Yongkang Li, Panagiotis Eustratiadis, Simon Lupart, Evangelos Kanoulas
- **Venue:** SIGIR 2025 (Oral)
- **URL:** https://arxiv.org/abs/2504.17884
- **Why important:** Operates in embedding space rather than discrete token space, generating more natural adversarial texts 4x faster than gradient-based methods while being harder to detect (lower perplexity).
- **Summary:** An unsupervised continuous-space optimization approach for corpus poisoning that generates natural-looking adversarial documents effective in both white-box and black-box settings.

**10. Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation**
- **Authors:** Liuji Chen, Xiaofang Yang, Yuanzhuo Lu, Jinghao Zhang, Xin Sun, Qiang Liu, Shu Wu, Jing Dong, Liang Wang
- **Venue:** ICLR 2026
- **URL:** https://openreview.net/forum?id=nBta7psl5J
- **Why important:** First paper to study multi-adversary competition in RAG poisoning, revealing that single-attacker strategies degrade under competition. Introduces the PoisonArena benchmark.
- **Summary:** Formalizes competitive poisoning scenarios where multiple attackers with conflicting goals target the same queries, showing performance reversals and metric limitations under realistic multi-adversary conditions.

---

### DEFENSE PAPERS

**11. RobustRAG: Certifiably Robust RAG against Retrieval Corruption**
- **Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal
- **Venue:** arXiv (cs.LG), 2024; affiliations: Princeton, NVIDIA, UC Berkeley
- **URL:** https://arxiv.org/abs/2405.15556
- **Why important:** The first defense framework with formal certified robustness guarantees against retrieval corruption. Reduces PoisonedRAG attack success from >90% to ~10%.
- **Summary:** Uses an isolate-then-aggregate strategy (partitioning passages into disjoint groups, generating responses per group, securely aggregating) with keyword-based and decoding-based algorithms, providing provable lower bounds on response quality against adaptive attackers.

**12. ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search**
- **Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova
- **Venue:** NeurIPS 2025
- **URL:** https://arxiv.org/abs/2509.23519
- **Why important:** Extends certified robustness to web-search RAG using graph theory. Incorporates retriever reliability signals (rank, scores) for more principled defense. Published at NeurIPS.
- **Summary:** Models documents as a graph with contradiction edges, finds a Maximum Independent Set (MIS) to identify consistent majority of trustworthy documents, and provides provable robustness guarantees where malicious document selection probability vanishes as retrieval size grows.

**13. RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in RAG**
- **Authors:** Pankayaraj Pathmanathan, Michael-Andrei Panaitescu-Liess, Cho-Yu Jason Chiang, Furong Huang
- **Venue:** AAAI 2026 Workshop on New Frontiers in Information Retrieval (Oral)
- **URL:** https://arxiv.org/abs/2512.24268
- **Why important:** Lightweight retrieval-stage defenses that do not require modifying the generation model, making them practical for deployment.
- **Summary:** RAGPart exploits dense retriever training dynamics via document partitioning; RAGMask detects suspicious tokens by measuring similarity shifts under targeted masking. Both reduce attack success while preserving clean-query performance.

**14. RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis**
- **Authors:** Xue Tan, Hao Luan, Mingyu Luo, Xiaoyan Sun, Ping Chen, Jun Dai
- **Venue:** Findings of EMNLP 2025
- **URL:** https://arxiv.org/abs/2411.18948
- **Why important:** Detection-based defense achieving 98% true positive rate with only 1% false positive rate by analyzing LLM internal activation patterns.
- **Summary:** Discovers distinct activation patterns in LLMs when generating correct vs. poisoned responses, building an automated detection pipeline that identifies compromised outputs without modifying the retrieval or generation pipeline.

**15. RAGForensics: Traceback of Poisoning Attacks to Retrieval-Augmented Generation**
- **Authors:** Baolei Zhang, Haoran Xin, Minghong Fang, Zhuqing Liu, Biao Yi, Tong Li, Zheli Liu
- **Venue:** The Web Conference (WWW) 2025
- **URL:** https://arxiv.org/abs/2504.21668
- **Why important:** First traceback system for RAG that identifies which poisoned texts in the knowledge database caused an attack, enabling post-hoc forensics.
- **Summary:** Iteratively retrieves database subsets and uses crafted prompts to guide an LLM in detecting poisoned texts responsible for attacks, enabling administrators to locate and remove adversarial content.

**16. Understanding Data Poisoning Attacks for RAG: Insights and Algorithms**
- **Authors:** Xun Xian, Tong Wang, Liwen You, Yanjun Qi
- **Venue:** ICLR 2025
- **URL:** https://openreview.net/forum?id=2aL6gcFX7q
- **Why important:** Provides theoretical understanding of why poisoning attacks work (effective along low-variance directions of clean data), yielding both a principled defense (DRS) and a stealthier attack.
- **Summary:** Shows poisoning attacks exploit low-variance directions in the clean data distribution; proposes DRS (Directional Relative Shifts) for defense and a regularized stealthy attack that minimizes detectability.

**17. RbFT: Robust Fine-tuning for Retrieval-Augmented Generation against Retrieval Defects**
- **Authors:** Yiteng Tu, Weihang Su, Yujia Zhou, Yiqun Liu, Qingyao Ai
- **Venue:** arXiv (cs.CL), January 2025
- **URL:** https://arxiv.org/abs/2501.18365
- **Why important:** Fine-tuning-based defense that trains LLMs to be robust against noisy, irrelevant, or counterfactual retrieved content.
- **Summary:** Two targeted fine-tuning tasks strengthen LLMs against retrieval failures, significantly improving robustness across diverse retrieval conditions while maintaining efficiency and compatibility with other defense methods.

**18. Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks**
- **Authors:** Jinyan Su, Jin Peng Zhou, Zhengxin Zhang, Preslav Nakov, Claire Cardie
- **Venue:** arXiv (cs.IR), December 2024
- **URL:** https://arxiv.org/abs/2412.16708
- **Why important:** Systematic evaluation framework with a taxonomy of context types (adversarial, untouched, guiding) and practical mitigation via "skeptical prompting."
- **Summary:** Evaluates multiple retrievers under poisoning, finding that skeptical prompting activates internal LLM reasoning to partially resist adversarial contexts, with effectiveness varying by model capability.

---

### SURVEY / BENCHMARK PAPERS

**19. Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions**
- **Authors:** Yuming Xu, Mingtao Zhang, Zhuohan Ge, Haoyang Li, Nicole Hu, Yongqi Zhang, Zhiyuan Wen, Jason Chen Zhang, Qing Li, Lei Chen
- **Venue:** arXiv (cs.CR / cs.AI), April 2026
- **URL:** https://arxiv.org/abs/2604.08304
- **Why important:** The most recent and comprehensive survey (2026) proposing the SLOT taxonomy for RAG security across a six-stage knowledge pipeline.
- **Summary:** Classifies attack surfaces, defense mechanisms, security objectives (CIA properties), and targets across the full RAG pipeline; identifies structural gaps and recommends realistic threat models, comprehensive defenses, and multimodal evaluation.

**20. Benchmarking Poisoning Attacks against Retrieval-Augmented Generation**
- **Authors:** Baolei Zhang, Haoran Xin, Jiatong Li, Dongzhe Zhang, Minghong Fang, Zhuqing Liu, Lihai Nie, Zheli Liu
- **Venue:** arXiv (cs.CR), May 2025
- **URL:** https://arxiv.org/abs/2505.18543
- **Why important:** First comprehensive benchmark: 5 QA datasets with 10 variants, 13 attack methods, 7 defenses. Shows attacks degrade on expanded datasets and advanced RAG architectures remain vulnerable.
- **Summary:** Systematic benchmark revealing that current attack effectiveness drops on harder dataset variants, but advanced RAG architectures (sequential, branching, loop, agent-based, multimodal) all remain susceptible, and existing defenses are inadequate.

---

### Key Themes and Takeaways

**Attack evolution (2024-2026):** Attacks have progressed from multi-document corpus poisoning (PoisonedRAG, 5 docs) to single-document attacks (CorruptRAG), black-box RL-based attacks (RIPRAG), query-agnostic transferable attacks, retriever-model poisoning (DisarmRAG), and competitive multi-adversary scenarios (PoisonArena). The attack surface keeps expanding.

**Defense landscape:** Certified defenses (RobustRAG, ReliabilityRAG) provide formal guarantees via isolate-then-aggregate and graph-theoretic approaches. Detection-based defenses (RevPRAG) analyze LLM activations. Retrieval-stage defenses (RAGPart/RAGMask) are lightweight. Forensic methods (RAGForensics) enable post-hoc traceback. However, benchmarking shows current defenses remain inadequate against the full spectrum of attacks.

**Open problems:** Multimodal RAG security, agent-based RAG robustness, realistic multi-adversary threat models, and privacy-preserving defenses remain underexplored.

agentId: af5683602d21c3aad (use SendMessage with to: 'af5683602d21c3aad' to continue this agent)
&lt;usage>total_tokens: 32390
tool_uses: 34
duration_ms: 205480&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf08d179-5b24-42fd-be03-6a95b39ea02f",
  "isSidechain": false,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "type": "user",
  "uuid": "2b08afb0-a2f6-42c6-b694-a0745f9e0dd8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on adversarial attacks and certified defenses for RAG systems. Search for papers from 2024-2026.\n\nExecute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:\n\n1. Search: \"corpus poisoning RAG retrieval augmented generation attack 2024 2025 2026\"\n2. Search: \"PoisonedRAG adversarial retrieval attack 2024 2025\"\n3. Search: \"certified robust RAG retrieval corruption defense 2025 2026\"\n4. Search: \"RobustRAG certifiably robust retrieval augmented generation\"\n5. Search: \"ReliabilityRAG graph-theoretic defense retrieval poisoning Princeton\"\n6. Search: \"adversarial attacks knowledge retrieval LLM 2025 2026\"\n\nFor each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers about attacking or defending RAG systems against corpus/retrieval poisoning.",
    "agentId": "af5683602d21c3aad",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive data on all the key papers. Here is the structured literature survey:\n\n---\n\n## Literature Survey: Adversarial Attacks and Certified Defenses for RAG Systems (2024--2026)\n\n### ATTACK PAPERS\n\n**1. PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models**\n- **Authors:** Wei Zou, Runpeng Geng, Binghui Wang, Jinyuan Jia\n- **Venue:** USENIX Security 2025\n- **URL:** https://arxiv.org/abs/2402.07867\n- **Why important:** The foundational paper that introduced knowledge-database poisoning attacks against RAG. Achieves 90% attack success rate by injecting only 5 malicious texts into a database of millions. Showed existing defenses are insufficient.\n- **Summary:** Formulates corpus poisoning of RAG as an optimization problem with both black-box and white-box solutions, demonstrating that a small number of injected adversarial passages can reliably steer LLM outputs to attacker-chosen answers.\n\n**2. Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation**\n- **Authors:** Harsh Chaudhari, Giorgio Severi, John Abascal, Anshuman Suri, Matthew Jagielski, Christopher A. Choquette-Choo, Milad Nasr, Cristina Nita-Rotaru, Alina Oprea\n- **Venue:** arXiv (cs.CR), 2024; validated on GPT-3.5/GPT-4 and production systems\n- **URL:** https://arxiv.org/abs/2405.20485\n- **Why important:** Demonstrates trigger-activated backdoor attacks on RAG systems that cause refusal, reputation damage, privacy violations, and harmful behaviors. Successfully tested on NVIDIA's \"Chat with RTX\" production system.\n- **Summary:** A two-stage optimization crafts a single poisoned document that is retrieved only when specific trigger tokens appear in queries, enabling targeted harmful outputs while evading detection on clean queries.\n\n**3. TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models**\n- **Authors:** Pengzhou Cheng, Yidong Ding, Tianjie Ju, Zongru Wu, Wei Du, Ping Yi, Zhuosheng Zhang, Gongshen Liu\n- **Venue:** arXiv (cs.CR), 2024\n- **URL:** https://arxiv.org/abs/2405.13401\n- **Why important:** Proposes a joint backdoor attack using contrastive learning to build orthogonal backdoor shortcuts between poisoned knowledge and triggers, enabling universal attack scenarios.\n- **Summary:** Uses knowledge graphs for fine-grained matching to create multiple purpose-driven backdoors that maintain normal retrieval on clean queries while returning semantically consistent poisoned content for adversarial queries.\n\n**4. CorruptRAG: Practical Poisoning Attacks against Retrieval-Augmented Generation**\n- **Authors:** Baolei Zhang, Yuxi Chen, Zhuqing Liu, Lihai Nie, Tong Li, Zheli Liu, Minghong Fang\n- **Venue:** ACM SACMAT 2026\n- **URL:** https://arxiv.org/abs/2504.03957\n- **Why important:** Advances attack practicality by requiring only a single injected poisoned text (vs. 5 in PoisonedRAG), making attacks more feasible and stealthier.\n- **Summary:** A practical single-document poisoning attack against RAG systems that achieves higher attack success rates than existing baselines on large-scale datasets.\n\n**5. DisarmRAG: Disabling Self-Correction in Retrieval-Augmented Generation via Stealthy Retriever Poisoning**\n- **Authors:** Yanbo Dai, Zhenlan Ji, Zongjie Li, Kuan Li, Shuai Wang\n- **Venue:** arXiv (cs.CR), August 2025\n- **URL:** https://arxiv.org/abs/2508.20083\n- **Why important:** Uniquely targets the retriever model itself (not the corpus), using contrastive learning to modify retriever behavior so it suppresses self-correction mechanisms in RAG. Over 90% attack success rate.\n- **Summary:** Compromises the retriever via model editing so it returns malicious instructions for targeted queries while behaving normally otherwise, defeating self-correction and detection defenses.\n\n**6. RIPRAG: Hack a Black-box RAG Question-Answering System with Reinforcement Learning**\n- **Authors:** Meng Xi, Sihan Lv, Yechen Jin, Guanjie Cheng, Naibo Wang, Ying Li, Jianwei Yin\n- **Venue:** arXiv (cs.AI), October 2025\n- **URL:** https://arxiv.org/abs/2510.10008\n- **Why important:** First RL-based black-box attack on RAG, treating the target system as a complete black box. Achieves up to 0.72 ASR improvement over baselines.\n- **Summary:** Uses reinforcement learning with black-box feedback (similarity and attack rewards) to optimize poisoned document generation without access to model internals.\n\n**7. \"Someone Hid It\": Query-Agnostic Black-Box Attacks on LLM-Based Retrieval**\n- **Authors:** Jiate Li, Defu Cao, Li Li, Wei Yang, Yuehan Qin, Chenxiao Yu, Tiannuo Yang, Ryan A. Rossi, Yan Liu, Xiyang Hu, Yue Zhao\n- **Venue:** arXiv (cs.CR), January 2026\n- **URL:** https://arxiv.org/abs/2602.00364\n- **Why important:** Query-agnostic attack that works without knowing victim queries or models, using zero-shot surrogate LLMs and adversarial learning for transferable injection tokens.\n- **Summary:** Formulates transferable attacks on LLM-based retrieval as a min-max optimization problem, generating adversarial tokens that transfer across different LLM retrievers without query knowledge.\n\n**8. GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search**\n- **Authors:** Matan Ben-Tov, Mahmood Sharif\n- **Venue:** ACM CCS 2025\n- **URL:** https://arxiv.org/abs/2412.20953\n- **Why important:** Demonstrates that dense retrieval systems are catastrophically vulnerable even at poisoning levels as low as 0.0001% of the corpus. Published at a top security venue.\n- **Summary:** Generates adversarial passages without model or corpus knowledge that achieve high rankings; single-query attacks are 100% successful, and standard defenses fail against adaptive versions.\n\n**9. Unsupervised Corpus Poisoning Attacks in Continuous Space for Dense Retrieval**\n- **Authors:** Yongkang Li, Panagiotis Eustratiadis, Simon Lupart, Evangelos Kanoulas\n- **Venue:** SIGIR 2025 (Oral)\n- **URL:** https://arxiv.org/abs/2504.17884\n- **Why important:** Operates in embedding space rather than discrete token space, generating more natural adversarial texts 4x faster than gradient-based methods while being harder to detect (lower perplexity).\n- **Summary:** An unsupervised continuous-space optimization approach for corpus poisoning that generates natural-looking adversarial documents effective in both white-box and black-box settings.\n\n**10. Uncovering Competing Poisoning Attacks in Retrieval-Augmented Generation**\n- **Authors:** Liuji Chen, Xiaofang Yang, Yuanzhuo Lu, Jinghao Zhang, Xin Sun, Qiang Liu, Shu Wu, Jing Dong, Liang Wang\n- **Venue:** ICLR 2026\n- **URL:** https://openreview.net/forum?id=nBta7psl5J\n- **Why important:** First paper to study multi-adversary competition in RAG poisoning, revealing that single-attacker strategies degrade under competition. Introduces the PoisonArena benchmark.\n- **Summary:** Formalizes competitive poisoning scenarios where multiple attackers with conflicting goals target the same queries, showing performance reversals and metric limitations under realistic multi-adversary conditions.\n\n---\n\n### DEFENSE PAPERS\n\n**11. RobustRAG: Certifiably Robust RAG against Retrieval Corruption**\n- **Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal\n- **Venue:** arXiv (cs.LG), 2024; affiliations: Princeton, NVIDIA, UC Berkeley\n- **URL:** https://arxiv.org/abs/2405.15556\n- **Why important:** The first defense framework with formal certified robustness guarantees against retrieval corruption. Reduces PoisonedRAG attack success from >90% to ~10%.\n- **Summary:** Uses an isolate-then-aggregate strategy (partitioning passages into disjoint groups, generating responses per group, securely aggregating) with keyword-based and decoding-based algorithms, providing provable lower bounds on response quality against adaptive attackers.\n\n**12. ReliabilityRAG: Effective and Provably Robust Defense for RAG-based Web-Search**\n- **Authors:** Zeyu Shen, Basileal Imana, Tong Wu, Chong Xiang, Prateek Mittal, Aleksandra Korolova\n- **Venue:** NeurIPS 2025\n- **URL:** https://arxiv.org/abs/2509.23519\n- **Why important:** Extends certified robustness to web-search RAG using graph theory. Incorporates retriever reliability signals (rank, scores) for more principled defense. Published at NeurIPS.\n- **Summary:** Models documents as a graph with contradiction edges, finds a Maximum Independent Set (MIS) to identify consistent majority of trustworthy documents, and provides provable robustness guarantees where malicious document selection probability vanishes as retrieval size grows.\n\n**13. RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in RAG**\n- **Authors:** Pankayaraj Pathmanathan, Michael-Andrei Panaitescu-Liess, Cho-Yu Jason Chiang, Furong Huang\n- **Venue:** AAAI 2026 Workshop on New Frontiers in Information Retrieval (Oral)\n- **URL:** https://arxiv.org/abs/2512.24268\n- **Why important:** Lightweight retrieval-stage defenses that do not require modifying the generation model, making them practical for deployment.\n- **Summary:** RAGPart exploits dense retriever training dynamics via document partitioning; RAGMask detects suspicious tokens by measuring similarity shifts under targeted masking. Both reduce attack success while preserving clean-query performance.\n\n**14. RevPRAG: Revealing Poisoning Attacks in Retrieval-Augmented Generation through LLM Activation Analysis**\n- **Authors:** Xue Tan, Hao Luan, Mingyu Luo, Xiaoyan Sun, Ping Chen, Jun Dai\n- **Venue:** Findings of EMNLP 2025\n- **URL:** https://arxiv.org/abs/2411.18948\n- **Why important:** Detection-based defense achieving 98% true positive rate with only 1% false positive rate by analyzing LLM internal activation patterns.\n- **Summary:** Discovers distinct activation patterns in LLMs when generating correct vs. poisoned responses, building an automated detection pipeline that identifies compromised outputs without modifying the retrieval or generation pipeline.\n\n**15. RAGForensics: Traceback of Poisoning Attacks to Retrieval-Augmented Generation**\n- **Authors:** Baolei Zhang, Haoran Xin, Minghong Fang, Zhuqing Liu, Biao Yi, Tong Li, Zheli Liu\n- **Venue:** The Web Conference (WWW) 2025\n- **URL:** https://arxiv.org/abs/2504.21668\n- **Why important:** First traceback system for RAG that identifies which poisoned texts in the knowledge database caused an attack, enabling post-hoc forensics.\n- **Summary:** Iteratively retrieves database subsets and uses crafted prompts to guide an LLM in detecting poisoned texts responsible for attacks, enabling administrators to locate and remove adversarial content.\n\n**16. Understanding Data Poisoning Attacks for RAG: Insights and Algorithms**\n- **Authors:** Xun Xian, Tong Wang, Liwen You, Yanjun Qi\n- **Venue:** ICLR 2025\n- **URL:** https://openreview.net/forum?id=2aL6gcFX7q\n- **Why important:** Provides theoretical understanding of why poisoning attacks work (effective along low-variance directions of clean data), yielding both a principled defense (DRS) and a stealthier attack.\n- **Summary:** Shows poisoning attacks exploit low-variance directions in the clean data distribution; proposes DRS (Directional Relative Shifts) for defense and a regularized stealthy attack that minimizes detectability.\n\n**17. RbFT: Robust Fine-tuning for Retrieval-Augmented Generation against Retrieval Defects**\n- **Authors:** Yiteng Tu, Weihang Su, Yujia Zhou, Yiqun Liu, Qingyao Ai\n- **Venue:** arXiv (cs.CL), January 2025\n- **URL:** https://arxiv.org/abs/2501.18365\n- **Why important:** Fine-tuning-based defense that trains LLMs to be robust against noisy, irrelevant, or counterfactual retrieved content.\n- **Summary:** Two targeted fine-tuning tasks strengthen LLMs against retrieval failures, significantly improving robustness across diverse retrieval conditions while maintaining efficiency and compatibility with other defense methods.\n\n**18. Towards More Robust Retrieval-Augmented Generation: Evaluating RAG Under Adversarial Poisoning Attacks**\n- **Authors:** Jinyan Su, Jin Peng Zhou, Zhengxin Zhang, Preslav Nakov, Claire Cardie\n- **Venue:** arXiv (cs.IR), December 2024\n- **URL:** https://arxiv.org/abs/2412.16708\n- **Why important:** Systematic evaluation framework with a taxonomy of context types (adversarial, untouched, guiding) and practical mitigation via \"skeptical prompting.\"\n- **Summary:** Evaluates multiple retrievers under poisoning, finding that skeptical prompting activates internal LLM reasoning to partially resist adversarial contexts, with effectiveness varying by model capability.\n\n---\n\n### SURVEY / BENCHMARK PAPERS\n\n**19. Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions**\n- **Authors:** Yuming Xu, Mingtao Zhang, Zhuohan Ge, Haoyang Li, Nicole Hu, Yongqi Zhang, Zhiyuan Wen, Jason Chen Zhang, Qing Li, Lei Chen\n- **Venue:** arXiv (cs.CR / cs.AI), April 2026\n- **URL:** https://arxiv.org/abs/2604.08304\n- **Why important:** The most recent and comprehensive survey (2026) proposing the SLOT taxonomy for RAG security across a six-stage knowledge pipeline.\n- **Summary:** Classifies attack surfaces, defense mechanisms, security objectives (CIA properties), and targets across the full RAG pipeline; identifies structural gaps and recommends realistic threat models, comprehensive defenses, and multimodal evaluation.\n\n**20. Benchmarking Poisoning Attacks against Retrieval-Augmented Generation**\n- **Authors:** Baolei Zhang, Haoran Xin, Jiatong Li, Dongzhe Zhang, Minghong Fang, Zhuqing Liu, Lihai Nie, Zheli Liu\n- **Venue:** arXiv (cs.CR), May 2025\n- **URL:** https://arxiv.org/abs/2505.18543\n- **Why important:** First comprehensive benchmark: 5 QA datasets with 10 variants, 13 attack methods, 7 defenses. Shows attacks degrade on expanded datasets and advanced RAG architectures remain vulnerable.\n- **Summary:** Systematic benchmark revealing that current attack effectiveness drops on harder dataset variants, but advanced RAG architectures (sequential, branching, loop, agent-based, multimodal) all remain susceptible, and existing defenses are inadequate.\n\n---\n\n### Key Themes and Takeaways\n\n**Attack evolution (2024-2026):** Attacks have progressed from multi-document corpus poisoning (PoisonedRAG, 5 docs) to single-document attacks (CorruptRAG), black-box RL-based attacks (RIPRAG), query-agnostic transferable attacks, retriever-model poisoning (DisarmRAG), and competitive multi-adversary scenarios (PoisonArena). The attack surface keeps expanding.\n\n**Defense landscape:** Certified defenses (RobustRAG, ReliabilityRAG) provide formal guarantees via isolate-then-aggregate and graph-theoretic approaches. Detection-based defenses (RevPRAG) analyze LLM activations. Retrieval-stage defenses (RAGPart/RAGMask) are lightweight. Forensic methods (RAGForensics) enable post-hoc traceback. However, benchmarking shows current defenses remain inadequate against the full spectrum of attacks.\n\n**Open problems:** Multimodal RAG security, agent-based RAG robustness, realistic multi-adversary threat models, and privacy-preserving defenses remain underexplored."
      }
    ],
    "totalDurationMs": 205480,
    "totalTokens": 32390,
    "totalToolUseCount": 34,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1730,
      "cache_read_input_tokens": 26332,
      "output_tokens": 4327,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1730
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4327,
          "cache_read_input_tokens": 26332,
          "cache_creation_input_tokens": 1730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1730,
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
      "otherToolCount": 34
    }
  },
  "sourceToolAssistantUUID": "bf08d179-5b24-42fd-be03-6a95b39ea02f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-30T06:16:23.954Z_

<details><summary>↩ Tool result · `toolu_01NwE3Yzh6mMFENwoz3PeHua`</summary>

```text
I now have comprehensive information on the key papers. Here is the structured literature survey.

---

## Literature Survey: Selective Prediction, Abstention, and Uncertainty Quantification for LLMs (2024--2026)

---

### A. SURVEYS AND FRAMEWORKS

---

**1. Know Your Limits: A Survey of Abstention in Large Language Models**
- **Authors:** Bingbing Wen, Jihan Yao, Shangbin Feng, Chenjun Xu, Yulia Tsvetkov, Bill Howe, Lucy Lu Wang
- **Venue:** TACL 2024 (revised Feb 2025)
- **URL:** https://arxiv.org/abs/2407.18418
- **Summary:** Comprehensive survey organizing abstention methods, benchmarks, and evaluation metrics along three dimensions -- query, model, and human values.
- **Why important:** The definitive reference for the field; provides a taxonomy that structures all subsequent work on LLM abstention.

---

**2. Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey**
- **Authors:** Xiaoou Liu, Tiejin Chen, Longchao Da, Chacha Chen, Zhen Lin, Hua Wei
- **Venue:** KDD 2025 / arXiv:2503.15850 (March 2025)
- **URL:** https://arxiv.org/abs/2503.15850
- **Summary:** Taxonomizes UQ methods by computational efficiency and uncertainty dimensions (input, reasoning, parameter, prediction); identifies challenges in scalability and robustness.
- **Why important:** Most comprehensive recent survey on UQ for LLMs, covering both white-box and black-box methods with a practical taxonomy.

---

**3. A Formal Framework for Uncertainty Analysis of Text Generation with Large Language Models**
- **Authors:** Steffen Herbold, Florian Lemmerich
- **Venue:** arXiv:2603.26363 (March 2026)
- **URL:** https://arxiv.org/abs/2603.26363
- **Summary:** Introduces a formal framework modeling prompt, generation, and interpretation as interconnected autoregressive processes forming a sampling tree, with filters and objective functions to express different uncertainty aspects.
- **Why important:** Provides rigorous mathematical foundations for defining and measuring uncertainty in LLM generation, unifying disparate existing approaches.

---

### B. BENCHMARKS AND EMPIRICAL ANALYSIS

---

**4. AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions**
- **Authors:** Polina Kirichenko, Mark Ibrahim, Kamalika Chaudhuri, Samuel J. Bell (Facebook Research)
- **Venue:** NeurIPS 2025 (Datasets and Benchmarks Track)
- **URL:** https://arxiv.org/abs/2506.09038
- **Summary:** Large-scale benchmark across 20 datasets and 20 frontier LLMs showing abstention is unsolved; reasoning fine-tuning degrades abstention by 24% on average, even in math/science domains.
- **Why important:** Key negative result -- demonstrates that scaling and reasoning training are insufficient for reliable abstention, motivating new approaches.

---

**5. Do LLMs Know When to NOT Answer? Investigating Abstention Abilities of Large Language Models**
- **Authors:** Nishanth Madhusudhan, Sathwik Tejaswi Madhusudhan, Vikas Yadav, Masoud Hashemi
- **Venue:** COLING 2025 / arXiv:2407.16221 (July 2024)
- **URL:** https://arxiv.org/abs/2407.16221
- **Summary:** Introduces Abstain-QA dataset and the Answerable-Unanswerable Confusion Matrix (AUCM) evaluation metric; tests three prompting strategies for improving abstention in GPT-4 and Mixtral.
- **Why important:** Provides a standardized black-box evaluation methodology and dataset for abstention research.

---

**6. Are LLM Decisions Faithful to Verbal Confidence?**
- **Authors:** Jiawei Wang, Yanfei Zhou, Siddartha Devic, Deqing Fu
- **Venue:** arXiv:2601.07767 (January 2026)
- **URL:** https://arxiv.org/abs/2601.07767
- **Summary:** Introduces RiskEval framework; shows LLMs are neither cost-aware in verbal confidence nor strategically responsive under high-penalty conditions -- even when abstention is mathematically optimal, models rarely abstain.
- **Why important:** Demonstrates that calibrated confidence alone is insufficient; LLMs lack the strategic agency to convert uncertainty signals into risk-sensitive decisions.

---

**7. The Illusion of Certainty: Uncertainty Quantification for LLMs Fails under Ambiguity**
- **Authors:** Tim Tomov, Dominik Fuchsgruber, Tom Wollschlager, Stephan Gunnemann
- **Venue:** arXiv:2511.04418 (November 2025)
- **URL:** https://arxiv.org/abs/2511.04418
- **Summary:** Shows that UQ methods degrade to near-random performance on ambiguous data; introduces MAQA* and AmbigQA* datasets with ground-truth answer distributions; argues ensemble-based estimators are fundamentally limited under ambiguity.
- **Why important:** Identifies a critical failure mode -- existing UQ methods only work well on unambiguous inputs, which undermines real-world reliability.

---

**8. Concurrent Criterion Validation of a Validity Screen for LLM Confidence Signals via Selective Prediction**
- **Authors:** Jon-Paul Cacioli
- **Venue:** arXiv:2604.17716 (April 2026)
- **URL:** https://arxiv.org/abs/2604.17716
- **Summary:** Proposes a three-tier validity screen (Valid/Indeterminate/Invalid) for LLM confidence signals; tests across 20 frontier LLMs, showing Valid models achieve AUROC of .624 while Invalid models score .357, explaining 47% of variance in selective prediction performance.
- **Why important:** Provides a practical diagnostic for determining whether a given LLM's confidence signals are even reliable enough to use for selective prediction.

---

### C. METHODS: TRAINING LLMS TO ABSTAIN

---

**9. When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond?**
- **Authors:** Xinyu Zhou, Chang Jin, Carsten Eickhoff, Zhijiang Guo, Seyed Ali Bahrainian
- **Venue:** ICLR 2026
- **URL:** https://openreview.net/forum?id=PhUCxfS0yf
- **Summary:** Combines Chain-of-Thought supervision with RL using abstention-focused rewards; a Qwen2.5-1.5B model outperforms GPT-4o on temporal QA by 3.5--5.8% exact match; shows SFT causes overconfidence while RL improves abstention.
- **Why important:** Demonstrates that small models trained with the right objectives can outperform frontier models on knowing when not to answer.

---

**10. Teaching LLMs to Abstain via Fine-Grained Semantic Confidence Reward**
- **Authors:** Hao An, Yang Xu
- **Venue:** arXiv:2510.24020 (October 2025)
- **URL:** https://arxiv.org/abs/2510.24020
- **Summary:** RL framework that samples multiple answers, performs semantic clustering, and trains models to keep high-confidence-cluster responses while discarding low-confidence ones; introduces a new metric for abstention reliability across in-domain and OOD settings.
- **Why important:** Provides a fine-grained RL signal for abstention rather than binary correct/wrong, enabling better knowledge boundary awareness.

---

**11. Rewarding Intellectual Humility: Learning When Not To Answer In Large Language Models**
- **Authors:** Abha Jha, Akanksha Mahajan, Ashwath Vaithinathan Aravindan, Praveen Saravanan, Sai Sailaja Policharla, Sonal Chaturbhuj Gehlot
- **Venue:** arXiv:2601.20126 (January 2026)
- **URL:** https://arxiv.org/abs/2601.20126
- **Summary:** Fine-tunes smaller models on medical/math benchmarks using RL with abstention rewards; finds moderate abstention rewards (r_abs around -0.25 to 0.3) reduce incorrect responses without severe accuracy loss.
- **Why important:** Provides practical guidance on reward shaping for abstention in safety-critical domains (medicine, math).

---

**12. Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs**
- **Authors:** Abinitha Gourabathina, Inkit Padhi, Manish Nagireddy, Subhajit Chaudhury, Prasanna Sattigeri
- **Venue:** arXiv:2604.02230 (April 2026)
- **URL:** https://arxiv.org/abs/2604.02230
- **Summary:** Proposes Trace Inversion -- reconstructs the most likely query from the model's reasoning trace and compares it to the original query; low similarity triggers abstention. Beats baselines in 33/36 settings across 9 abstention QA datasets.
- **Why important:** Novel detection-based approach to abstention that does not require retraining; works by diagnosing whether the model is actually answering the question asked.

---

**13. Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty**
- **Authors:** Sravanthi Machcha, Sushrita Yerra, Sahil Gupta, Aishwarya Sahoo, Sharmin Sultana, Hong Yu, Zonghai Yao
- **Venue:** EACL 2026 Main Conference / arXiv:2601.12471 (January 2026)
- **URL:** https://arxiv.org/abs/2601.12471
- **Summary:** Introduces MedAbstain framework for evaluating LLM abstention in clinical settings; finds that even high-accuracy models fail to abstain when uncertain, and offering explicit refusal options improves safe behavior more than model scaling or prompting.
- **Why important:** Domain-specific (medical) evaluation showing abstention is critical for safety; simple interventions (explicit refusal options) can help.

---

### D. CONFORMAL PREDICTION AND FORMAL GUARANTEES

---

**14. Conformal Language Modeling**
- **Authors:** Victor Quach, Adam Fisch, Tal Schuster, Adam Yala, Jae Ho Sohn, Tommi S. Jaakkola, Regina Barzilay
- **Venue:** ICLR 2024
- **URL:** https://openreview.net/forum?id=pzUhfQ74c5
- **Summary:** Foundational method for conformal prediction in language models: generates response sets with distribution-free coverage guarantees by calibrating both a stopping rule for accumulating outputs and a rejection rule for filtering.
- **Why important:** Seminal work establishing how conformal prediction can be applied to open-ended language generation with formal guarantees.

---

**15. Large Language Model Validity via Enhanced Conformal Prediction Methods**
- **Authors:** John J. Cherian, Isaac Gibbs, Emmanuel J. Candes
- **Venue:** NeurIPS 2024 / arXiv:2406.09714 (June 2024)
- **URL:** https://arxiv.org/abs/2406.09714
- **Summary:** Develops two new conformal methods: a generalized conditional conformal procedure for adaptive guarantees, and a novel algorithm for differentiating through the conformal procedure to improve scoring functions. Tested on biography and medical QA.
- **Why important:** From the Candes group (founding conformal prediction researchers); provides state-of-the-art conditional validity guarantees for LLM outputs.

---

**16. Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models**
- **Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov, Maxim Panov
- **Venue:** arXiv:2604.13991 (April 2026)
- **URL:** https://arxiv.org/abs/2604.13991
- **Summary:** Extends conformal score transformation for prompt-dependent calibration; supports both long-form generation and MCQA with ability to filter unreliable content while maintaining statistical coverage guarantees.
- **Why important:** Makes conformal prediction adaptive to individual prompts, improving conditional coverage -- a key limitation of prior work.

---

**17. Domain-Shift-Aware Conformal Prediction for Large Language Models**
- **Authors:** Zhexiao Lin, Yuanyuan Li, Neeraj Sarna, Yuanyuan Gao, Michael von Gablenz
- **Venue:** arXiv:2510.05566 (October 2025)
- **URL:** https://arxiv.org/abs/2510.05566
- **Summary:** Proposes DS-CP, which reweights calibration samples based on similarity to test prompts; demonstrates that standard conformal prediction breaks down under domain shift with under-coverage, while DS-CP maintains validity and improves adaptivity.
- **Why important:** Addresses the practical problem that calibration data and test data often come from different domains, which violates exchangeability assumptions.

---

**18. Geometry-Calibrated Conformal Abstention for Language Models**
- **Authors:** Rui Xu, Yi Chen, Sihong Xie, Hui Xiong
- **Venue:** arXiv:2604.27914 (April 2026)
- **URL:** https://arxiv.org/abs/2604.27914
- **Summary:** Post-hoc framework using prediction confidence (not intractable non-conformity scores) with representation-geometry-based calibration to decide when to abstain; achieves ~75% conditional correctness with mathematical guarantees on participation rate and response correctness.
- **Why important:** Bridges conformal prediction and abstention by making the approach tractable for open-ended generation through geometric analysis of representations.

---

**19. Online Reasoning Calibration (ORCA): Test-Time Training Enables Generalizable Conformal LLM Reasoning**
- **Authors:** Cai Zhou, Zekai Wang, Menghua Wu, Qianyu Julie Zhu, Flora C. Shi, Chenyu Wang, Ashia Wilson, Tommi Jaakkola, Stephen Bates
- **Venue:** arXiv:2604.01170 (April 2026)
- **URL:** https://arxiv.org/abs/2604.01170
- **Summary:** Combines conformal prediction with test-time training via meta-learning to calibrate sampling per-input; provides theoretical guarantees on conformal risks; achieves up to 47.5% efficiency savings in-distribution and 67% on out-of-domain math problems.
- **Why important:** Makes conformal prediction adaptive at test time via meta-learning, enabling reliable uncertainty quantification even under distribution shift during reasoning.

---

**20. Set-Valued Prediction for Large Language Models with Feasibility-Aware Coverage Guarantees**
- **Authors:** Ye Li, Anqi Hu, Yuanchang Ye, Shiyan Tong, Zhiyuan Wang, Bo Fu
- **Venue:** arXiv:2603.22966 (March 2026)
- **URL:** https://arxiv.org/abs/2603.22966
- **Summary:** Establishes that full coverage is often unachievable due to finite sampling; introduces minimum achievable risk level (MRL) concept and a learn-then-test calibration procedure for constructing prediction sets with feasibility-aware guarantees. Validated on 6 tasks with 5 LLMs.
- **Why important:** Provides a principled answer to "when is coverage even possible?" -- a question prior conformal methods for LLMs did not address.

---

### E. EFFICIENT UNCERTAINTY ESTIMATION

---

**21. Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement**
- **Authors:** Jaehun Jung, Faeze Brahman, Yejin Choi
- **Venue:** ICLR 2025 (Oral) / arXiv:2407.18370
- **URL:** https://arxiv.org/abs/2407.18370
- **Summary:** Cascaded selective evaluation where cheap models judge first and escalate to stronger models only when confidence is low; introduces Simulated Annotators for calibration; Mistral-7B achieves >80% human agreement with ~80% coverage via provable guarantees.
- **Why important:** Shows that selective prediction with formal guarantees enables cheap models to match expensive ones; directly applicable to abstention-as-escalation.

---

**22. Dist2ill: Distributional Distillation for One-Pass Uncertainty Estimation in Large Language Models**
- **Authors:** Yicong Zhao, King Yeung Tsang, Harshil Vejendla, Haizhou Shi, Zhuohang Li, Zhigang Hua, Qi Xu, Tunyu Zhang, Yi Wang, Ligong Han, Bradley A. Malin, Hao Wang
- **Venue:** arXiv:2505.11731 (May 2025, revised Feb 2026)
- **URL:** https://arxiv.org/abs/2505.11731
- **Summary:** Trains an LLM to produce multiple diverse reasoning paths in one inference pass with a lightweight confidence-scoring module; achieves calibration improvements while being much cheaper than multi-pass Bayesian approaches.
- **Why important:** Addresses the key practical bottleneck -- multi-sample UQ is expensive; this method approximates it in a single forward pass.

---

**23. Eliciting Numerical Predictive Distributions of LLMs Without Autoregression**
- **Authors:** Julianna Piskorz, Katarzyna Kobalczyk, Mihaela van der Schaar
- **Venue:** ICLR 2026 / arXiv:2603.02913 (March 2026)
- **URL:** https://arxiv.org/abs/2603.02913
- **Summary:** Trains regression probes on LLM embeddings to predict statistical summaries (mean, median, quantiles) of predictive distributions without autoregressive generation; shows embeddings carry informative uncertainty signals.
- **Why important:** Demonstrates a lightweight, non-autoregressive path to extracting uncertainty information already encoded in LLM representations.

---

### KEY THEMES AND TAKEAWAYS

1. **Abstention is unsolved.** AbstentionBench (NeurIPS 2025) shows reasoning fine-tuning actually makes it worse (-24%), and scaling helps little.

2. **Verbal confidence is unreliable.** RiskEval (2026) and related work show LLMs do not translate uncertainty signals into appropriate abstention decisions, even when abstaining is mathematically optimal.

3. **RL-based training for abstention is promising.** Multiple papers (ICLR 2026, arXiv 2025-2026) show that reinforcement learning with abstention-aware rewards outperforms supervised fine-tuning, which tends toward overconfidence.

4. **Conformal prediction provides formal guarantees.** A rich line of work (Cherian/Candes at NeurIPS 2024 through ORCA and Geometry-Calibrated Conformal Abstention in 2026) provides distribution-free coverage guarantees, with recent work addressing domain shift, conditional validity, and tractability for open-ended generation.

5. **Efficiency matters.** Dist2ill and the ICLR 2026 embedding-probe approach show paths to single-pass uncertainty estimation, making practical deployment feasible.

6. **Ambiguity breaks everything.** The "Illusion of Certainty" paper (2025) shows UQ methods degrade to random under ambiguous inputs -- an underexplored failure mode.

agentId: aac17a2bb4c580881 (use SendMessage with to: 'aac17a2bb4c580881' to continue this agent)
&lt;usage>total_tokens: 31821
tool_uses: 36
duration_ms: 201716&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a1ee919-54da-4173-8b5d-ba08fe58665c",
  "isSidechain": false,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "type": "user",
  "uuid": "74a58f8a-cbd7-4229-836a-dd15786c0584",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on selective prediction, abstention, and uncertainty quantification for LLMs. Search for papers from 2024-2026.\n\nExecute these searches and for each promising paper, fetch its arxiv/openreview page to read the abstract:\n\n1. Search: \"selective prediction large language models abstention 2024 2025 2026\"\n2. Search: \"LLM uncertainty quantification calibration 2025 2026 survey\"\n3. Search: \"know when to abstain LLM confidence 2025 2026\"\n4. Search: \"conformal prediction large language models 2025 2026\"\n5. Search: \"distribution-free uncertainty LLM generation 2025 2026\"\n\nFor each paper found, use WebFetch on its arxiv URL to read the abstract and understand what it does.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important, and a one-line summary. Focus on papers about when LLMs should abstain from answering, and formal uncertainty guarantees for LLM outputs.",
    "agentId": "aac17a2bb4c580881",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on the key papers. Here is the structured literature survey.\n\n---\n\n## Literature Survey: Selective Prediction, Abstention, and Uncertainty Quantification for LLMs (2024--2026)\n\n---\n\n### A. SURVEYS AND FRAMEWORKS\n\n---\n\n**1. Know Your Limits: A Survey of Abstention in Large Language Models**\n- **Authors:** Bingbing Wen, Jihan Yao, Shangbin Feng, Chenjun Xu, Yulia Tsvetkov, Bill Howe, Lucy Lu Wang\n- **Venue:** TACL 2024 (revised Feb 2025)\n- **URL:** https://arxiv.org/abs/2407.18418\n- **Summary:** Comprehensive survey organizing abstention methods, benchmarks, and evaluation metrics along three dimensions -- query, model, and human values.\n- **Why important:** The definitive reference for the field; provides a taxonomy that structures all subsequent work on LLM abstention.\n\n---\n\n**2. Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey**\n- **Authors:** Xiaoou Liu, Tiejin Chen, Longchao Da, Chacha Chen, Zhen Lin, Hua Wei\n- **Venue:** KDD 2025 / arXiv:2503.15850 (March 2025)\n- **URL:** https://arxiv.org/abs/2503.15850\n- **Summary:** Taxonomizes UQ methods by computational efficiency and uncertainty dimensions (input, reasoning, parameter, prediction); identifies challenges in scalability and robustness.\n- **Why important:** Most comprehensive recent survey on UQ for LLMs, covering both white-box and black-box methods with a practical taxonomy.\n\n---\n\n**3. A Formal Framework for Uncertainty Analysis of Text Generation with Large Language Models**\n- **Authors:** Steffen Herbold, Florian Lemmerich\n- **Venue:** arXiv:2603.26363 (March 2026)\n- **URL:** https://arxiv.org/abs/2603.26363\n- **Summary:** Introduces a formal framework modeling prompt, generation, and interpretation as interconnected autoregressive processes forming a sampling tree, with filters and objective functions to express different uncertainty aspects.\n- **Why important:** Provides rigorous mathematical foundations for defining and measuring uncertainty in LLM generation, unifying disparate existing approaches.\n\n---\n\n### B. BENCHMARKS AND EMPIRICAL ANALYSIS\n\n---\n\n**4. AbstentionBench: Reasoning LLMs Fail on Unanswerable Questions**\n- **Authors:** Polina Kirichenko, Mark Ibrahim, Kamalika Chaudhuri, Samuel J. Bell (Facebook Research)\n- **Venue:** NeurIPS 2025 (Datasets and Benchmarks Track)\n- **URL:** https://arxiv.org/abs/2506.09038\n- **Summary:** Large-scale benchmark across 20 datasets and 20 frontier LLMs showing abstention is unsolved; reasoning fine-tuning degrades abstention by 24% on average, even in math/science domains.\n- **Why important:** Key negative result -- demonstrates that scaling and reasoning training are insufficient for reliable abstention, motivating new approaches.\n\n---\n\n**5. Do LLMs Know When to NOT Answer? Investigating Abstention Abilities of Large Language Models**\n- **Authors:** Nishanth Madhusudhan, Sathwik Tejaswi Madhusudhan, Vikas Yadav, Masoud Hashemi\n- **Venue:** COLING 2025 / arXiv:2407.16221 (July 2024)\n- **URL:** https://arxiv.org/abs/2407.16221\n- **Summary:** Introduces Abstain-QA dataset and the Answerable-Unanswerable Confusion Matrix (AUCM) evaluation metric; tests three prompting strategies for improving abstention in GPT-4 and Mixtral.\n- **Why important:** Provides a standardized black-box evaluation methodology and dataset for abstention research.\n\n---\n\n**6. Are LLM Decisions Faithful to Verbal Confidence?**\n- **Authors:** Jiawei Wang, Yanfei Zhou, Siddartha Devic, Deqing Fu\n- **Venue:** arXiv:2601.07767 (January 2026)\n- **URL:** https://arxiv.org/abs/2601.07767\n- **Summary:** Introduces RiskEval framework; shows LLMs are neither cost-aware in verbal confidence nor strategically responsive under high-penalty conditions -- even when abstention is mathematically optimal, models rarely abstain.\n- **Why important:** Demonstrates that calibrated confidence alone is insufficient; LLMs lack the strategic agency to convert uncertainty signals into risk-sensitive decisions.\n\n---\n\n**7. The Illusion of Certainty: Uncertainty Quantification for LLMs Fails under Ambiguity**\n- **Authors:** Tim Tomov, Dominik Fuchsgruber, Tom Wollschlager, Stephan Gunnemann\n- **Venue:** arXiv:2511.04418 (November 2025)\n- **URL:** https://arxiv.org/abs/2511.04418\n- **Summary:** Shows that UQ methods degrade to near-random performance on ambiguous data; introduces MAQA* and AmbigQA* datasets with ground-truth answer distributions; argues ensemble-based estimators are fundamentally limited under ambiguity.\n- **Why important:** Identifies a critical failure mode -- existing UQ methods only work well on unambiguous inputs, which undermines real-world reliability.\n\n---\n\n**8. Concurrent Criterion Validation of a Validity Screen for LLM Confidence Signals via Selective Prediction**\n- **Authors:** Jon-Paul Cacioli\n- **Venue:** arXiv:2604.17716 (April 2026)\n- **URL:** https://arxiv.org/abs/2604.17716\n- **Summary:** Proposes a three-tier validity screen (Valid/Indeterminate/Invalid) for LLM confidence signals; tests across 20 frontier LLMs, showing Valid models achieve AUROC of .624 while Invalid models score .357, explaining 47% of variance in selective prediction performance.\n- **Why important:** Provides a practical diagnostic for determining whether a given LLM's confidence signals are even reliable enough to use for selective prediction.\n\n---\n\n### C. METHODS: TRAINING LLMS TO ABSTAIN\n\n---\n\n**9. When Silence Is Golden: Can LLMs Learn to Abstain in Temporal QA and Beyond?**\n- **Authors:** Xinyu Zhou, Chang Jin, Carsten Eickhoff, Zhijiang Guo, Seyed Ali Bahrainian\n- **Venue:** ICLR 2026\n- **URL:** https://openreview.net/forum?id=PhUCxfS0yf\n- **Summary:** Combines Chain-of-Thought supervision with RL using abstention-focused rewards; a Qwen2.5-1.5B model outperforms GPT-4o on temporal QA by 3.5--5.8% exact match; shows SFT causes overconfidence while RL improves abstention.\n- **Why important:** Demonstrates that small models trained with the right objectives can outperform frontier models on knowing when not to answer.\n\n---\n\n**10. Teaching LLMs to Abstain via Fine-Grained Semantic Confidence Reward**\n- **Authors:** Hao An, Yang Xu\n- **Venue:** arXiv:2510.24020 (October 2025)\n- **URL:** https://arxiv.org/abs/2510.24020\n- **Summary:** RL framework that samples multiple answers, performs semantic clustering, and trains models to keep high-confidence-cluster responses while discarding low-confidence ones; introduces a new metric for abstention reliability across in-domain and OOD settings.\n- **Why important:** Provides a fine-grained RL signal for abstention rather than binary correct/wrong, enabling better knowledge boundary awareness.\n\n---\n\n**11. Rewarding Intellectual Humility: Learning When Not To Answer In Large Language Models**\n- **Authors:** Abha Jha, Akanksha Mahajan, Ashwath Vaithinathan Aravindan, Praveen Saravanan, Sai Sailaja Policharla, Sonal Chaturbhuj Gehlot\n- **Venue:** arXiv:2601.20126 (January 2026)\n- **URL:** https://arxiv.org/abs/2601.20126\n- **Summary:** Fine-tunes smaller models on medical/math benchmarks using RL with abstention rewards; finds moderate abstention rewards (r_abs around -0.25 to 0.3) reduce incorrect responses without severe accuracy loss.\n- **Why important:** Provides practical guidance on reward shaping for abstention in safety-critical domains (medicine, math).\n\n---\n\n**12. Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs**\n- **Authors:** Abinitha Gourabathina, Inkit Padhi, Manish Nagireddy, Subhajit Chaudhury, Prasanna Sattigeri\n- **Venue:** arXiv:2604.02230 (April 2026)\n- **URL:** https://arxiv.org/abs/2604.02230\n- **Summary:** Proposes Trace Inversion -- reconstructs the most likely query from the model's reasoning trace and compares it to the original query; low similarity triggers abstention. Beats baselines in 33/36 settings across 9 abstention QA datasets.\n- **Why important:** Novel detection-based approach to abstention that does not require retraining; works by diagnosing whether the model is actually answering the question asked.\n\n---\n\n**13. Knowing When to Abstain: Medical LLMs Under Clinical Uncertainty**\n- **Authors:** Sravanthi Machcha, Sushrita Yerra, Sahil Gupta, Aishwarya Sahoo, Sharmin Sultana, Hong Yu, Zonghai Yao\n- **Venue:** EACL 2026 Main Conference / arXiv:2601.12471 (January 2026)\n- **URL:** https://arxiv.org/abs/2601.12471\n- **Summary:** Introduces MedAbstain framework for evaluating LLM abstention in clinical settings; finds that even high-accuracy models fail to abstain when uncertain, and offering explicit refusal options improves safe behavior more than model scaling or prompting.\n- **Why important:** Domain-specific (medical) evaluation showing abstention is critical for safety; simple interventions (explicit refusal options) can help.\n\n---\n\n### D. CONFORMAL PREDICTION AND FORMAL GUARANTEES\n\n---\n\n**14. Conformal Language Modeling**\n- **Authors:** Victor Quach, Adam Fisch, Tal Schuster, Adam Yala, Jae Ho Sohn, Tommi S. Jaakkola, Regina Barzilay\n- **Venue:** ICLR 2024\n- **URL:** https://openreview.net/forum?id=pzUhfQ74c5\n- **Summary:** Foundational method for conformal prediction in language models: generates response sets with distribution-free coverage guarantees by calibrating both a stopping rule for accumulating outputs and a rejection rule for filtering.\n- **Why important:** Seminal work establishing how conformal prediction can be applied to open-ended language generation with formal guarantees.\n\n---\n\n**15. Large Language Model Validity via Enhanced Conformal Prediction Methods**\n- **Authors:** John J. Cherian, Isaac Gibbs, Emmanuel J. Candes\n- **Venue:** NeurIPS 2024 / arXiv:2406.09714 (June 2024)\n- **URL:** https://arxiv.org/abs/2406.09714\n- **Summary:** Develops two new conformal methods: a generalized conditional conformal procedure for adaptive guarantees, and a novel algorithm for differentiating through the conformal procedure to improve scoring functions. Tested on biography and medical QA.\n- **Why important:** From the Candes group (founding conformal prediction researchers); provides state-of-the-art conditional validity guarantees for LLM outputs.\n\n---\n\n**16. Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models**\n- **Authors:** Aleksandr Rubashevskii, Dzianis Piatrashyn, Preslav Nakov, Maxim Panov\n- **Venue:** arXiv:2604.13991 (April 2026)\n- **URL:** https://arxiv.org/abs/2604.13991\n- **Summary:** Extends conformal score transformation for prompt-dependent calibration; supports both long-form generation and MCQA with ability to filter unreliable content while maintaining statistical coverage guarantees.\n- **Why important:** Makes conformal prediction adaptive to individual prompts, improving conditional coverage -- a key limitation of prior work.\n\n---\n\n**17. Domain-Shift-Aware Conformal Prediction for Large Language Models**\n- **Authors:** Zhexiao Lin, Yuanyuan Li, Neeraj Sarna, Yuanyuan Gao, Michael von Gablenz\n- **Venue:** arXiv:2510.05566 (October 2025)\n- **URL:** https://arxiv.org/abs/2510.05566\n- **Summary:** Proposes DS-CP, which reweights calibration samples based on similarity to test prompts; demonstrates that standard conformal prediction breaks down under domain shift with under-coverage, while DS-CP maintains validity and improves adaptivity.\n- **Why important:** Addresses the practical problem that calibration data and test data often come from different domains, which violates exchangeability assumptions.\n\n---\n\n**18. Geometry-Calibrated Conformal Abstention for Language Models**\n- **Authors:** Rui Xu, Yi Chen, Sihong Xie, Hui Xiong\n- **Venue:** arXiv:2604.27914 (April 2026)\n- **URL:** https://arxiv.org/abs/2604.27914\n- **Summary:** Post-hoc framework using prediction confidence (not intractable non-conformity scores) with representation-geometry-based calibration to decide when to abstain; achieves ~75% conditional correctness with mathematical guarantees on participation rate and response correctness.\n- **Why important:** Bridges conformal prediction and abstention by making the approach tractable for open-ended generation through geometric analysis of representations.\n\n---\n\n**19. Online Reasoning Calibration (ORCA): Test-Time Training Enables Generalizable Conformal LLM Reasoning**\n- **Authors:** Cai Zhou, Zekai Wang, Menghua Wu, Qianyu Julie Zhu, Flora C. Shi, Chenyu Wang, Ashia Wilson, Tommi Jaakkola, Stephen Bates\n- **Venue:** arXiv:2604.01170 (April 2026)\n- **URL:** https://arxiv.org/abs/2604.01170\n- **Summary:** Combines conformal prediction with test-time training via meta-learning to calibrate sampling per-input; provides theoretical guarantees on conformal risks; achieves up to 47.5% efficiency savings in-distribution and 67% on out-of-domain math problems.\n- **Why important:** Makes conformal prediction adaptive at test time via meta-learning, enabling reliable uncertainty quantification even under distribution shift during reasoning.\n\n---\n\n**20. Set-Valued Prediction for Large Language Models with Feasibility-Aware Coverage Guarantees**\n- **Authors:** Ye Li, Anqi Hu, Yuanchang Ye, Shiyan Tong, Zhiyuan Wang, Bo Fu\n- **Venue:** arXiv:2603.22966 (March 2026)\n- **URL:** https://arxiv.org/abs/2603.22966\n- **Summary:** Establishes that full coverage is often unachievable due to finite sampling; introduces minimum achievable risk level (MRL) concept and a learn-then-test calibration procedure for constructing prediction sets with feasibility-aware guarantees. Validated on 6 tasks with 5 LLMs.\n- **Why important:** Provides a principled answer to \"when is coverage even possible?\" -- a question prior conformal methods for LLMs did not address.\n\n---\n\n### E. EFFICIENT UNCERTAINTY ESTIMATION\n\n---\n\n**21. Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement**\n- **Authors:** Jaehun Jung, Faeze Brahman, Yejin Choi\n- **Venue:** ICLR 2025 (Oral) / arXiv:2407.18370\n- **URL:** https://arxiv.org/abs/2407.18370\n- **Summary:** Cascaded selective evaluation where cheap models judge first and escalate to stronger models only when confidence is low; introduces Simulated Annotators for calibration; Mistral-7B achieves >80% human agreement with ~80% coverage via provable guarantees.\n- **Why important:** Shows that selective prediction with formal guarantees enables cheap models to match expensive ones; directly applicable to abstention-as-escalation.\n\n---\n\n**22. Dist2ill: Distributional Distillation for One-Pass Uncertainty Estimation in Large Language Models**\n- **Authors:** Yicong Zhao, King Yeung Tsang, Harshil Vejendla, Haizhou Shi, Zhuohang Li, Zhigang Hua, Qi Xu, Tunyu Zhang, Yi Wang, Ligong Han, Bradley A. Malin, Hao Wang\n- **Venue:** arXiv:2505.11731 (May 2025, revised Feb 2026)\n- **URL:** https://arxiv.org/abs/2505.11731\n- **Summary:** Trains an LLM to produce multiple diverse reasoning paths in one inference pass with a lightweight confidence-scoring module; achieves calibration improvements while being much cheaper than multi-pass Bayesian approaches.\n- **Why important:** Addresses the key practical bottleneck -- multi-sample UQ is expensive; this method approximates it in a single forward pass.\n\n---\n\n**23. Eliciting Numerical Predictive Distributions of LLMs Without Autoregression**\n- **Authors:** Julianna Piskorz, Katarzyna Kobalczyk, Mihaela van der Schaar\n- **Venue:** ICLR 2026 / arXiv:2603.02913 (March 2026)\n- **URL:** https://arxiv.org/abs/2603.02913\n- **Summary:** Trains regression probes on LLM embeddings to predict statistical summaries (mean, median, quantiles) of predictive distributions without autoregressive generation; shows embeddings carry informative uncertainty signals.\n- **Why important:** Demonstrates a lightweight, non-autoregressive path to extracting uncertainty information already encoded in LLM representations.\n\n---\n\n### KEY THEMES AND TAKEAWAYS\n\n1. **Abstention is unsolved.** AbstentionBench (NeurIPS 2025) shows reasoning fine-tuning actually makes it worse (-24%), and scaling helps little.\n\n2. **Verbal confidence is unreliable.** RiskEval (2026) and related work show LLMs do not translate uncertainty signals into appropriate abstention decisions, even when abstaining is mathematically optimal.\n\n3. **RL-based training for abstention is promising.** Multiple papers (ICLR 2026, arXiv 2025-2026) show that reinforcement learning with abstention-aware rewards outperforms supervised fine-tuning, which tends toward overconfidence.\n\n4. **Conformal prediction provides formal guarantees.** A rich line of work (Cherian/Candes at NeurIPS 2024 through ORCA and Geometry-Calibrated Conformal Abstention in 2026) provides distribution-free coverage guarantees, with recent work addressing domain shift, conditional validity, and tractability for open-ended generation.\n\n5. **Efficiency matters.** Dist2ill and the ICLR 2026 embedding-probe approach show paths to single-pass uncertainty estimation, making practical deployment feasible.\n\n6. **Ambiguity breaks everything.** The \"Illusion of Certainty\" paper (2025) shows UQ methods degrade to random under ambiguous inputs -- an underexplored failure mode."
      }
    ],
    "totalDurationMs": 201716,
    "totalTokens": 31821,
    "totalToolUseCount": 36,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1847,
      "cache_read_input_tokens": 25060,
      "output_tokens": 4913,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1847
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4913,
          "cache_read_input_tokens": 25060,
          "cache_creation_input_tokens": 1847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1847,
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
      "otherToolCount": 36
    }
  },
  "sourceToolAssistantUUID": "8a1ee919-54da-4173-8b5d-ba08fe58665c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "74a58f8a-cbd7-4229-836a-dd15786c0584",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on conformal prediction for RAG",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Tool result

_source line 28 · 2026-05-30T06:17:08.812Z_

<details><summary>↩ Tool result · `toolu_019TDeGV7LG7ETS9caJm86po`</summary>

```text
Now I have comprehensive information. Let me compile the final structured list.

Here is the structured literature survey of best/outstanding papers and notable presentations at top ML/NLP venues (2024-2026) relevant to conformal prediction, robust AI, adversarial robustness, RAG systems, and trustworthy AI.

---

## TIER 1: Award-Winning Papers Directly on Topic

### 1. Conformal Prediction as Bayesian Quadrature
- **Authors:** Jake C. Snell, Thomas L. Griffiths
- **Venue:** ICML 2025 -- **Outstanding Paper Award** (1 of 6 in main track) + Oral
- **URL:** https://arxiv.org/abs/2502.13228
- **Why important:** Won ICML 2025 Outstanding Paper Award. Directly on conformal prediction.
- **Summary:** Reframes frequentist conformal prediction through a Bayesian lens using Bayesian quadrature, providing more interpretable guarantees and a richer representation of the likely range of losses at test time for high-stakes deployment.

### 2. Safety Alignment Should Be Made More Than Just a Few Tokens Deep
- **Authors:** Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, Peter Henderson
- **Venue:** ICLR 2025 -- **Outstanding Paper Award** (1 of 3) + Oral
- **URL:** https://arxiv.org/abs/2406.05946
- **Why important:** Won ICLR 2025 Outstanding Paper Award. Directly on adversarial robustness and trustworthy AI.
- **Summary:** Identifies that LLM safety alignment adapts model behavior primarily over only the first few output tokens ("shallow safety alignment"), explaining vulnerabilities to adversarial suffix, prefilling, decoding parameter, and fine-tuning attacks; proposes deeper alignment and regularized fine-tuning to improve robustness.

### 3. Language Models Resist Alignment: Evidence From Data Compression
- **Authors:** Jiaming Ji, Kaile Wang, Tianyi Qiu, Boyuan Chen, Jiayi Zhou, Changye Li, Hantao Lou, Juntao Dai, Yunhuai Liu, Yaodong Yang
- **Venue:** ACL 2025 -- **Best Paper Award** (1 of 4)
- **URL:** https://arxiv.org/abs/2406.06144
- **Why important:** Won ACL 2025 Best Paper Award. Directly on robust/trustworthy AI and alignment safety.
- **Summary:** Demonstrates "elasticity" in LLMs -- models revert to pre-training behavior distributions after alignment fine-tuning; uses compression theory to prove that fine-tuning disproportionately undermines alignment, with elasticity increasing with model size, raising fundamental concerns about alignment durability.

### 4. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **Authors:** Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi
- **Venue:** NeurIPS 2025 -- **Best Paper Award** (1 of 4)
- **URL:** NeurIPS 2025 proceedings (see https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)
- **Why important:** Won NeurIPS 2025 Best Paper Award. Relevant to trustworthy AI -- addresses diversity collapse and safety risks from LLM homogenization.
- **Summary:** Reveals the "Artificial Hivemind" effect across 70+ models: pronounced intra- and inter-model homogenization in open-ended generation, raising concerns about threats to human creativity, value plurality, and independent thinking; introduces the Infinity-Chat benchmark (26K queries, 31K human annotations).

---

## TIER 2: Spotlight/Oral Presentations Directly on Topic

### 5. Decision Theoretic Foundations for Conformal Prediction: Optimal Uncertainty Quantification for Risk-Averse Agents
- **Authors:** Shayan Kiyani, George Pappas, Aaron Roth, Hamed Hassani
- **Venue:** ICML 2025 -- **Spotlight**
- **URL:** https://arxiv.org/abs/2502.02561
- **Why important:** ICML 2025 Spotlight. Directly on conformal prediction for safe decision-making.
- **Summary:** Proves that prediction sets are optimal for decision makers who optimize value-at-risk; shows a max-min decision policy is optimal for risk-averse agents; introduces Risk-Averse Calibration (RAC) algorithm validated on medical diagnosis and recommendation systems with improved safety-utility trade-offs.

### 6. Robust Conformal Prediction with a Single Binary Certificate
- **Authors:** Soroush H. Zargarbashi, Aleksandar Bojchevski
- **Venue:** ICLR 2025 -- **Conference Paper** (published)
- **URL:** https://arxiv.org/abs/2503.05239
- **Why important:** Published at ICLR 2025. Directly on robust conformal prediction under adversarial perturbations.
- **Summary:** Achieves adversarially robust conformal prediction by computing only a single binary certificate rather than certifying each point individually; needs only ~150 MC samples (vs. ~10,000 previously) for CIFAR-10, producing smaller prediction sets while removing the bounded score function requirement.

---

## TIER 3: Outstanding/Recognized Papers at Top Venues

### 7. HALoGEN: Fantastic LLM Hallucinations and Where to Find Them
- **Authors:** Abhilasha Ravichander, Shrusti Ghela, David Wadden, Yejin Choi
- **Venue:** ACL 2025 -- **Outstanding Paper** (1 of 26)
- **URL:** https://arxiv.org/abs/2501.08292
- **Why important:** ACL 2025 Outstanding Paper. Relevant to trustworthy AI / reliable generation.
- **Summary:** Introduces a comprehensive hallucination benchmark (10,923 prompts, 9 domains) with automated verifiers; evaluates ~150,000 generations from 14 LLMs, finding even top models hallucinate up to 86% of atomic facts in some domains; classifies hallucinations into three types (incorrect recollection, incorrect knowledge, fabrication).

### 8. LLMs Know Their Vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts
- **Authors:** Qibing Ren, Hao Li, Dongrui Liu, Zhanxu Xie, Xiaoya Lu, Yu Qiao, Lei Sha, Junchi Yan, Lizhuang Ma, Jing Shao
- **Venue:** ACL 2025 -- **Outstanding Paper** (1 of 26)
- **URL:** https://arxiv.org/abs/2410.10700
- **Why important:** ACL 2025 Outstanding Paper. Directly on adversarial robustness and AI safety.
- **Summary:** Identifies that natural distribution shifts (not just adversarial attacks) can bypass LLM safety mechanisms; introduces ActorBreaker, a multi-turn attack method grounded in actor-network theory that crafts seemingly benign prompts to expose unsafe content; proposes broadening safety training across wider semantic spaces.

### 9. FaithfulRAG: Fact-Level Conflict Modeling for Context-Faithful Retrieval-Augmented Generation
- **Authors:** Qinggang Zhang, Zhishang Xiang, Yilin Xiao, Le Wang, Junhui Li, Xinrun Wang, Jinsong Su
- **Venue:** ACL 2025 -- **SAC Highlights**
- **URL:** https://arxiv.org/abs/2506.08938
- **Why important:** Recognized in ACL 2025 SAC Highlights. Directly on trustworthy RAG systems.
- **Summary:** Addresses unfaithfulness in RAG when retrieved context conflicts with parametric knowledge; introduces a self-thinking process that explicitly identifies conflicting facts at the fact level and enables LLMs to reason about and integrate them before generation, outperforming prior faithful RAG methods.

---

## TIER 4: Notable Accepted Papers at Top Venues (Poster/Conference Paper)

### 10. One Sample is Enough to Make Conformal Prediction Robust
- **Authors:** Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski
- **Venue:** NeurIPS 2025 -- Poster
- **URL:** https://openreview.net/forum?id=h5NsMrUK4g
- **Why important:** NeurIPS 2025 accepted paper. Directly on robust conformal prediction.
- **Summary:** Demonstrates that conformal prediction can achieve adversarial robustness with only a single forward pass on a randomly perturbed input (rather than ~100 passes); certifies the conformal procedure itself rather than individual scores, yielding smaller robust prediction sets for both classification and regression.

### 11. Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations
- **Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, Youssef Marzouk
- **Venue:** NeurIPS 2025 -- Poster
- **URL:** https://arxiv.org/abs/2502.14105
- **Why important:** NeurIPS 2025 accepted paper. Directly on robust conformal prediction under distribution shifts.
- **Summary:** Models distribution shifts using Levy-Prokhorov ambiguity sets capturing both local and global perturbations; reduces complex high-dimensional distribution shifts to one-dimensional problems, enabling exact computation of worst-case quantiles and coverage guarantees.

### 12. Verifiably Robust Conformal Prediction
- **Authors:** Linus Jeary, Tom Kuipers, Mehran Hosseini, Nicola Paoletti
- **Venue:** NeurIPS 2024 -- Poster
- **URL:** https://arxiv.org/abs/2405.18942
- **Why important:** NeurIPS 2024 accepted paper. First to support arbitrary norm perturbations for robust conformal prediction.
- **Summary:** Introduces VRCP, leveraging neural network verification to recover conformal prediction coverage guarantees under adversarial attacks; supports perturbations bounded by arbitrary norms (L1, L2, L-infinity) and regression tasks, unlike prior work limited to L2 and classification.

### 13. Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability
- **Authors:** Jie Bao, Chuangyin Dang, Rui Luo, Hanwei Zhang, Zhixin Zhou
- **Venue:** ICML 2025 -- Poster
- **URL:** https://arxiv.org/abs/2506.07804
- **Why important:** ICML 2025 accepted paper. Directly bridges adversarial robustness and conformal prediction.
- **Summary:** Develops OPSA (OPtimal Size Attack) to undermine conformal prediction by maximizing model uncertainty, and OPSA-AT, a conformal adversarial training framework using hard quantile thresholds; demonstrates enhanced robustness against multiple attack types while maintaining reliable predictions for safety-critical applications.

### 14. Conformal Prediction for Ensembles: Improving Efficiency via Score-Based Aggregation
- **Authors:** (Patel et al.)
- **Venue:** NeurIPS 2025 -- Poster
- **URL:** https://arxiv.org/abs/2405.16246
- **Why important:** NeurIPS 2025 accepted paper. On conformal prediction methodology.
- **Summary:** Extends scalar conformal score functions to multivariate scores for ensemble methods, using quantile envelopes (instead of scalar quantiles) to produce more efficient prediction regions while maintaining coverage guarantees; applicable to classification and predict-then-optimize regression.

### 15. Certifiably Robust RAG against Retrieval Corruption
- **Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal
- **Venue:** Preprint (presented at NextGenAISafety workshop at ICML 2024)
- **URL:** https://arxiv.org/abs/2405.15556
- **Why important:** First certifiably robust defense framework for RAG systems. Directly on robust/trustworthy RAG.
- **Summary:** Introduces RobustRAG using an isolate-then-aggregate strategy: passages are partitioned into disjoint groups, responses generated independently, then securely aggregated via keyword-based or decoding-based algorithms; provides formal certifiable robustness guarantees against adaptive attackers injecting bounded malicious passages.

---

## Summary Table

| # | Paper | Venue | Recognition | Topics |
|---|-------|-------|-------------|--------|
| 1 | Conformal Prediction as Bayesian Quadrature | ICML 2025 | Outstanding Paper Award | Conformal prediction |
| 2 | Safety Alignment Should Be More Than a Few Tokens Deep | ICLR 2025 | Outstanding Paper Award | Adversarial robustness, trustworthy AI |
| 3 | Language Models Resist Alignment | ACL 2025 | Best Paper Award | Trustworthy AI, robust alignment |
| 4 | Artificial Hivemind | NeurIPS 2025 | Best Paper Award | Trustworthy AI, safety |
| 5 | Decision Theoretic Foundations for Conformal Prediction | ICML 2025 | Spotlight | Conformal prediction, safe decision-making |
| 6 | Robust Conformal Prediction with Single Binary Certificate | ICLR 2025 | Conference Paper | Robust conformal prediction |
| 7 | HALoGEN | ACL 2025 | Outstanding Paper | Trustworthy AI, hallucination |
| 8 | LLMs Know Their Vulnerabilities | ACL 2025 | Outstanding Paper | Adversarial robustness, AI safety |
| 9 | FaithfulRAG | ACL 2025 | SAC Highlights | Trustworthy RAG |
| 10 | One Sample is Enough for Robust CP | NeurIPS 2025 | Poster | Robust conformal prediction |
| 11 | CP under Levy-Prokhorov Distribution Shifts | NeurIPS 2025 | Poster | Robust conformal prediction |
| 12 | Verifiably Robust Conformal Prediction | NeurIPS 2024 | Poster | Robust conformal prediction |
| 13 | Enhancing Adversarial Robustness with CP | ICML 2025 | Poster | Adversarial robustness + conformal prediction |
| 14 | CP for Ensembles via Score-Based Aggregation | NeurIPS 2025 | Poster | Conformal prediction |
| 15 | Certifiably Robust RAG | Preprint/Workshop | ICML 2024 Workshop | Robust RAG |

agentId: ac82c1188b142400b (use SendMessage with to: 'ac82c1188b142400b' to continue this agent)
&lt;usage>total_tokens: 53207
tool_uses: 55
duration_ms: 240874&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98d40381-5ed0-4e18-8675-7179eab16f8a",
  "isSidechain": false,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "type": "user",
  "uuid": "4b2d3c37-05f3-44a1-a95e-a0d5f84ab60d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey. Search for best paper awards and outstanding papers at top ML/NLP venues from 2024-2026 that are relevant to: conformal prediction, robust AI, adversarial robustness, RAG systems, or trustworthy AI.\n\nExecute these searches:\n\n1. Search: \"best paper award NeurIPS 2025 conformal prediction robust\"\n2. Search: \"best paper ICML 2025 2026 adversarial robustness trustworthy AI\"\n3. Search: \"best paper ACL EMNLP NAACL 2025 2026 retrieval augmented generation\"\n4. Search: \"outstanding paper ICLR 2025 2026 robust conformal\"\n5. Search: \"best paper AAAI 2025 2026 safe robust responsible AI\"\n6. Search: \"oral spotlight NeurIPS ICML 2025 conformal prediction\"\n7. Search: \"site:openreview.net conformal prediction 2025 2026 outstanding\"\n\nFor each relevant paper found, use WebFetch on its arxiv/openreview URL to read the abstract.\n\nReturn a structured list of papers with: title, authors, venue, URL, why it's important (specifically note if best paper/oral/spotlight), and a one-line summary.",
    "agentId": "ac82c1188b142400b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the final structured list.\n\nHere is the structured literature survey of best/outstanding papers and notable presentations at top ML/NLP venues (2024-2026) relevant to conformal prediction, robust AI, adversarial robustness, RAG systems, and trustworthy AI.\n\n---\n\n## TIER 1: Award-Winning Papers Directly on Topic\n\n### 1. Conformal Prediction as Bayesian Quadrature\n- **Authors:** Jake C. Snell, Thomas L. Griffiths\n- **Venue:** ICML 2025 -- **Outstanding Paper Award** (1 of 6 in main track) + Oral\n- **URL:** https://arxiv.org/abs/2502.13228\n- **Why important:** Won ICML 2025 Outstanding Paper Award. Directly on conformal prediction.\n- **Summary:** Reframes frequentist conformal prediction through a Bayesian lens using Bayesian quadrature, providing more interpretable guarantees and a richer representation of the likely range of losses at test time for high-stakes deployment.\n\n### 2. Safety Alignment Should Be Made More Than Just a Few Tokens Deep\n- **Authors:** Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, Peter Henderson\n- **Venue:** ICLR 2025 -- **Outstanding Paper Award** (1 of 3) + Oral\n- **URL:** https://arxiv.org/abs/2406.05946\n- **Why important:** Won ICLR 2025 Outstanding Paper Award. Directly on adversarial robustness and trustworthy AI.\n- **Summary:** Identifies that LLM safety alignment adapts model behavior primarily over only the first few output tokens (\"shallow safety alignment\"), explaining vulnerabilities to adversarial suffix, prefilling, decoding parameter, and fine-tuning attacks; proposes deeper alignment and regularized fine-tuning to improve robustness.\n\n### 3. Language Models Resist Alignment: Evidence From Data Compression\n- **Authors:** Jiaming Ji, Kaile Wang, Tianyi Qiu, Boyuan Chen, Jiayi Zhou, Changye Li, Hantao Lou, Juntao Dai, Yunhuai Liu, Yaodong Yang\n- **Venue:** ACL 2025 -- **Best Paper Award** (1 of 4)\n- **URL:** https://arxiv.org/abs/2406.06144\n- **Why important:** Won ACL 2025 Best Paper Award. Directly on robust/trustworthy AI and alignment safety.\n- **Summary:** Demonstrates \"elasticity\" in LLMs -- models revert to pre-training behavior distributions after alignment fine-tuning; uses compression theory to prove that fine-tuning disproportionately undermines alignment, with elasticity increasing with model size, raising fundamental concerns about alignment durability.\n\n### 4. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)\n- **Authors:** Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Yejin Choi\n- **Venue:** NeurIPS 2025 -- **Best Paper Award** (1 of 4)\n- **URL:** NeurIPS 2025 proceedings (see https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)\n- **Why important:** Won NeurIPS 2025 Best Paper Award. Relevant to trustworthy AI -- addresses diversity collapse and safety risks from LLM homogenization.\n- **Summary:** Reveals the \"Artificial Hivemind\" effect across 70+ models: pronounced intra- and inter-model homogenization in open-ended generation, raising concerns about threats to human creativity, value plurality, and independent thinking; introduces the Infinity-Chat benchmark (26K queries, 31K human annotations).\n\n---\n\n## TIER 2: Spotlight/Oral Presentations Directly on Topic\n\n### 5. Decision Theoretic Foundations for Conformal Prediction: Optimal Uncertainty Quantification for Risk-Averse Agents\n- **Authors:** Shayan Kiyani, George Pappas, Aaron Roth, Hamed Hassani\n- **Venue:** ICML 2025 -- **Spotlight**\n- **URL:** https://arxiv.org/abs/2502.02561\n- **Why important:** ICML 2025 Spotlight. Directly on conformal prediction for safe decision-making.\n- **Summary:** Proves that prediction sets are optimal for decision makers who optimize value-at-risk; shows a max-min decision policy is optimal for risk-averse agents; introduces Risk-Averse Calibration (RAC) algorithm validated on medical diagnosis and recommendation systems with improved safety-utility trade-offs.\n\n### 6. Robust Conformal Prediction with a Single Binary Certificate\n- **Authors:** Soroush H. Zargarbashi, Aleksandar Bojchevski\n- **Venue:** ICLR 2025 -- **Conference Paper** (published)\n- **URL:** https://arxiv.org/abs/2503.05239\n- **Why important:** Published at ICLR 2025. Directly on robust conformal prediction under adversarial perturbations.\n- **Summary:** Achieves adversarially robust conformal prediction by computing only a single binary certificate rather than certifying each point individually; needs only ~150 MC samples (vs. ~10,000 previously) for CIFAR-10, producing smaller prediction sets while removing the bounded score function requirement.\n\n---\n\n## TIER 3: Outstanding/Recognized Papers at Top Venues\n\n### 7. HALoGEN: Fantastic LLM Hallucinations and Where to Find Them\n- **Authors:** Abhilasha Ravichander, Shrusti Ghela, David Wadden, Yejin Choi\n- **Venue:** ACL 2025 -- **Outstanding Paper** (1 of 26)\n- **URL:** https://arxiv.org/abs/2501.08292\n- **Why important:** ACL 2025 Outstanding Paper. Relevant to trustworthy AI / reliable generation.\n- **Summary:** Introduces a comprehensive hallucination benchmark (10,923 prompts, 9 domains) with automated verifiers; evaluates ~150,000 generations from 14 LLMs, finding even top models hallucinate up to 86% of atomic facts in some domains; classifies hallucinations into three types (incorrect recollection, incorrect knowledge, fabrication).\n\n### 8. LLMs Know Their Vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts\n- **Authors:** Qibing Ren, Hao Li, Dongrui Liu, Zhanxu Xie, Xiaoya Lu, Yu Qiao, Lei Sha, Junchi Yan, Lizhuang Ma, Jing Shao\n- **Venue:** ACL 2025 -- **Outstanding Paper** (1 of 26)\n- **URL:** https://arxiv.org/abs/2410.10700\n- **Why important:** ACL 2025 Outstanding Paper. Directly on adversarial robustness and AI safety.\n- **Summary:** Identifies that natural distribution shifts (not just adversarial attacks) can bypass LLM safety mechanisms; introduces ActorBreaker, a multi-turn attack method grounded in actor-network theory that crafts seemingly benign prompts to expose unsafe content; proposes broadening safety training across wider semantic spaces.\n\n### 9. FaithfulRAG: Fact-Level Conflict Modeling for Context-Faithful Retrieval-Augmented Generation\n- **Authors:** Qinggang Zhang, Zhishang Xiang, Yilin Xiao, Le Wang, Junhui Li, Xinrun Wang, Jinsong Su\n- **Venue:** ACL 2025 -- **SAC Highlights**\n- **URL:** https://arxiv.org/abs/2506.08938\n- **Why important:** Recognized in ACL 2025 SAC Highlights. Directly on trustworthy RAG systems.\n- **Summary:** Addresses unfaithfulness in RAG when retrieved context conflicts with parametric knowledge; introduces a self-thinking process that explicitly identifies conflicting facts at the fact level and enables LLMs to reason about and integrate them before generation, outperforming prior faithful RAG methods.\n\n---\n\n## TIER 4: Notable Accepted Papers at Top Venues (Poster/Conference Paper)\n\n### 10. One Sample is Enough to Make Conformal Prediction Robust\n- **Authors:** Soroush H. Zargarbashi, Mohammad Sadegh Akhondzadeh, Aleksandar Bojchevski\n- **Venue:** NeurIPS 2025 -- Poster\n- **URL:** https://openreview.net/forum?id=h5NsMrUK4g\n- **Why important:** NeurIPS 2025 accepted paper. Directly on robust conformal prediction.\n- **Summary:** Demonstrates that conformal prediction can achieve adversarial robustness with only a single forward pass on a randomly perturbed input (rather than ~100 passes); certifies the conformal procedure itself rather than individual scores, yielding smaller robust prediction sets for both classification and regression.\n\n### 11. Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations\n- **Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, Youssef Marzouk\n- **Venue:** NeurIPS 2025 -- Poster\n- **URL:** https://arxiv.org/abs/2502.14105\n- **Why important:** NeurIPS 2025 accepted paper. Directly on robust conformal prediction under distribution shifts.\n- **Summary:** Models distribution shifts using Levy-Prokhorov ambiguity sets capturing both local and global perturbations; reduces complex high-dimensional distribution shifts to one-dimensional problems, enabling exact computation of worst-case quantiles and coverage guarantees.\n\n### 12. Verifiably Robust Conformal Prediction\n- **Authors:** Linus Jeary, Tom Kuipers, Mehran Hosseini, Nicola Paoletti\n- **Venue:** NeurIPS 2024 -- Poster\n- **URL:** https://arxiv.org/abs/2405.18942\n- **Why important:** NeurIPS 2024 accepted paper. First to support arbitrary norm perturbations for robust conformal prediction.\n- **Summary:** Introduces VRCP, leveraging neural network verification to recover conformal prediction coverage guarantees under adversarial attacks; supports perturbations bounded by arbitrary norms (L1, L2, L-infinity) and regression tasks, unlike prior work limited to L2 and classification.\n\n### 13. Enhancing Adversarial Robustness with Conformal Prediction: A Framework for Guaranteed Model Reliability\n- **Authors:** Jie Bao, Chuangyin Dang, Rui Luo, Hanwei Zhang, Zhixin Zhou\n- **Venue:** ICML 2025 -- Poster\n- **URL:** https://arxiv.org/abs/2506.07804\n- **Why important:** ICML 2025 accepted paper. Directly bridges adversarial robustness and conformal prediction.\n- **Summary:** Develops OPSA (OPtimal Size Attack) to undermine conformal prediction by maximizing model uncertainty, and OPSA-AT, a conformal adversarial training framework using hard quantile thresholds; demonstrates enhanced robustness against multiple attack types while maintaining reliable predictions for safety-critical applications.\n\n### 14. Conformal Prediction for Ensembles: Improving Efficiency via Score-Based Aggregation\n- **Authors:** (Patel et al.)\n- **Venue:** NeurIPS 2025 -- Poster\n- **URL:** https://arxiv.org/abs/2405.16246\n- **Why important:** NeurIPS 2025 accepted paper. On conformal prediction methodology.\n- **Summary:** Extends scalar conformal score functions to multivariate scores for ensemble methods, using quantile envelopes (instead of scalar quantiles) to produce more efficient prediction regions while maintaining coverage guarantees; applicable to classification and predict-then-optimize regression.\n\n### 15. Certifiably Robust RAG against Retrieval Corruption\n- **Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal\n- **Venue:** Preprint (presented at NextGenAISafety workshop at ICML 2024)\n- **URL:** https://arxiv.org/abs/2405.15556\n- **Why important:** First certifiably robust defense framework for RAG systems. Directly on robust/trustworthy RAG.\n- **Summary:** Introduces RobustRAG using an isolate-then-aggregate strategy: passages are partitioned into disjoint groups, responses generated independently, then securely aggregated via keyword-based or decoding-based algorithms; provides formal certifiable robustness guarantees against adaptive attackers injecting bounded malicious passages.\n\n---\n\n## Summary Table\n\n| # | Paper | Venue | Recognition | Topics |\n|---|-------|-------|-------------|--------|\n| 1 | Conformal Prediction as Bayesian Quadrature | ICML 2025 | Outstanding Paper Award | Conformal prediction |\n| 2 | Safety Alignment Should Be More Than a Few Tokens Deep | ICLR 2025 | Outstanding Paper Award | Adversarial robustness, trustworthy AI |\n| 3 | Language Models Resist Alignment | ACL 2025 | Best Paper Award | Trustworthy AI, robust alignment |\n| 4 | Artificial Hivemind | NeurIPS 2025 | Best Paper Award | Trustworthy AI, safety |\n| 5 | Decision Theoretic Foundations for Conformal Prediction | ICML 2025 | Spotlight | Conformal prediction, safe decision-making |\n| 6 | Robust Conformal Prediction with Single Binary Certificate | ICLR 2025 | Conference Paper | Robust conformal prediction |\n| 7 | HALoGEN | ACL 2025 | Outstanding Paper | Trustworthy AI, hallucination |\n| 8 | LLMs Know Their Vulnerabilities | ACL 2025 | Outstanding Paper | Adversarial robustness, AI safety |\n| 9 | FaithfulRAG | ACL 2025 | SAC Highlights | Trustworthy RAG |\n| 10 | One Sample is Enough for Robust CP | NeurIPS 2025 | Poster | Robust conformal prediction |\n| 11 | CP under Levy-Prokhorov Distribution Shifts | NeurIPS 2025 | Poster | Robust conformal prediction |\n| 12 | Verifiably Robust Conformal Prediction | NeurIPS 2024 | Poster | Robust conformal prediction |\n| 13 | Enhancing Adversarial Robustness with CP | ICML 2025 | Poster | Adversarial robustness + conformal prediction |\n| 14 | CP for Ensembles via Score-Based Aggregation | NeurIPS 2025 | Poster | Conformal prediction |\n| 15 | Certifiably Robust RAG | Preprint/Workshop | ICML 2024 Workshop | Robust RAG |"
      }
    ],
    "totalDurationMs": 240874,
    "totalTokens": 53207,
    "totalToolUseCount": 55,
    "usage": {
      "input_tokens": 789,
      "cache_creation_input_tokens": 1482,
      "cache_read_input_tokens": 47153,
      "output_tokens": 3783,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1482
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 789,
          "output_tokens": 3783,
          "cache_read_input_tokens": 47153,
          "cache_creation_input_tokens": 1482,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1482,
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
      "otherToolCount": 55
    }
  },
  "sourceToolAssistantUUID": "98d40381-5ed0-4e18-8675-7179eab16f8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-30T06:17:14.124Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I now have comprehensive results from all five search agents. Let me now synthesize the findings and select the 15 most important papers for this specific research direction. Let me also do a few more targeted searches to make sure I haven't missed anything critical, especially around:

1. The specific seed papers mentioned
2. Conformal prediction under distribution shift for NLP
3. Any papers I might have missed on the intersection of CP + RAG + adversarial

Let me launch a few more focused searches to fill gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b2d3c37-05f3-44a1-a95e-a0d5f84ab60d",
  "isSidechain": false,
  "requestId": "req_011CbYGLf85P7UJKpBEFUu8o",
  "type": "assistant",
  "uuid": "4759d211-8ca5-41fe-aaab-47bb28214a8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WXtc4Yur7Pup4wA2AYiHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22340,
      "cache_read_input_tokens": 16647,
      "output_tokens": 858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 858,
          "cache_read_input_tokens": 16647,
          "cache_creation_input_tokens": 22340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22340
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

_source line 30 · 2026-05-30T06:17:15.109Z_

Excellent! I have rich results from all five agents. Let me now do a few more targeted searches to fill any remaining gaps, particularly around the specific seed papers and their citation networks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4759d211-8ca5-41fe-aaab-47bb28214a8b",
  "isSidechain": false,
  "requestId": "req_011CbYGLf85P7UJKpBEFUu8o",
  "type": "assistant",
  "uuid": "f0d38d48-1ebc-453c-a530-16ec1e1ba846",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WXtc4Yur7Pup4wA2AYiHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22340,
      "cache_read_input_tokens": 16647,
      "output_tokens": 858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 858,
          "cache_read_input_tokens": 16647,
          "cache_creation_input_tokens": 22340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22340
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

_source line 31 · 2026-05-30T06:17:23.258Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011q2K44Gnm2obyoTKfZTJzV`</summary>

```json
{
  "description": "Search: Seed paper citations",
  "prompt": "Search for recent papers (2024-2026) that cite or build upon these specific seed papers. For each search, fetch the arxiv page of any promising result:\n\n1. Search: \"TRAQ trustworthy retrieval augmented question answering conformal prediction cited\"\n2. Search: \"C-RAG certified generation risks retrieval augmented ICML 2024 cited by\"\n3. Search: \"PoisonedRAG corpus poisoning defense 2025 2026\"\n4. Search: \"RobustRAG isolate then aggregate retrieval corruption 2025 2026\"\n5. Search: \"conformal prediction exchangeability RAG retrieval 2025 2026\"\n6. Search: \"abstention framework RAG systems guarantees 2025 2026\"\n7. Search: \"nonconformity score retrieval agreement 2025 2026\"\n\nFor each paper found, use WebFetch to read the abstract. Focus on papers that:\n- Extend conformal prediction to adversarial/poisoning settings in RAG\n- Provide certified defenses for RAG with formal guarantees\n- Study distribution shift or exchangeability violations in conformal prediction for NLP\n\nReturn a structured list with: title, authors, venue, URL, why important, one-line summary.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0d38d48-1ebc-453c-a530-16ec1e1ba846",
  "isSidechain": false,
  "requestId": "req_011CbYGLf85P7UJKpBEFUu8o",
  "type": "assistant",
  "uuid": "be635787-0e86-42e6-802e-e30d68e723b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WXtc4Yur7Pup4wA2AYiHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22340,
      "cache_read_input_tokens": 16647,
      "output_tokens": 858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 858,
          "cache_read_input_tokens": 16647,
          "cache_creation_input_tokens": 22340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22340
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

_source line 32 · 2026-05-30T06:17:27.202Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NLZHfDjvHdAe1SiGLEDw9e`</summary>

```json
{
  "description": "Search: CP distribution shift NLP",
  "prompt": "Search for recent papers (2024-2026) on conformal prediction under distribution shift, covariate shift, or domain adaptation, particularly for NLP/language models. Also search for papers on partition-and-vote or majority-voting approaches in conformal prediction.\n\nExecute these searches and fetch arxiv pages for promising results:\n\n1. Search: \"conformal prediction covariate shift NLP language models 2025 2026\"\n2. Search: \"partition vote conformal prediction robustness\"\n3. Search: \"weighted conformal prediction distribution shift language 2024 2025\"\n4. Search: \"adaptive conformal inference online distribution shift 2025 2026\"\n5. Search: \"conformal prediction test-time distribution shift 2025 2026\"\n6. Search: \"selective prediction RAG retrieval augmented generation 2025 2026\"\n\nFor each paper found, use WebFetch to read the abstract. Return a structured list with: title, authors, venue, URL, why important, one-line summary.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be635787-0e86-42e6-802e-e30d68e723b2",
  "isSidechain": false,
  "requestId": "req_011CbYGLf85P7UJKpBEFUu8o",
  "type": "assistant",
  "uuid": "a089076b-e133-495f-96bd-df068d113d28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011WXtc4Yur7Pup4wA2AYiHq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 22340,
      "cache_read_input_tokens": 16647,
      "output_tokens": 858,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 22340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 858,
          "cache_read_input_tokens": 16647,
          "cache_creation_input_tokens": 22340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 22340
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "a089076b-e133-495f-96bd-df068d113d28",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on conformal prediction for RAG",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Tool result

_source line 35 · 2026-05-30T06:20:45.221Z_

<details><summary>↩ Tool result · `toolu_011q2K44Gnm2obyoTKfZTJzV`</summary>

```text
Now I have comprehensive results. Here is the structured list of papers found.

---

## Structured List of Papers (2024--2026) Citing or Building on the Seed Papers

Papers are organized into three thematic clusters matching your focus areas.

---

### CLUSTER A: Certified Defenses and Formal Guarantees for RAG

**1. RobustRAG: Certifiably Robust RAG against Retrieval Corruption**
- **Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal
- **Venue:** arXiv:2405.15556 (submitted May 2024; revised April 2026). Presented at ICML 2024 workshop track.
- **URL:** https://arxiv.org/abs/2405.15556
- **Why important:** First certified defense for RAG against retrieval corruption; provides formal robustness certificates via an isolate-then-aggregate strategy. Directly extends the C-RAG line of work.
- **One-line summary:** Partitions retrieved passages into isolated groups, generates responses independently per group, and securely aggregates them, achieving 38% certifiable robust accuracy while maintaining 71% clean accuracy.

**2. RAGDefender -- Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems**
- **Authors:** Minseok Kim, Hankook Lee, Hyungjoon Koo
- **Venue:** ACSAC 2025 (Annual Computer Security Applications Conference); arXiv:2511.01268 (November 2025)
- **URL:** https://arxiv.org/abs/2511.01268
- **Why important:** Lightweight post-retrieval defense that outperforms RobustRAG, especially when poisoned passages outnumber clean ones. Directly benchmarks against both PoisonedRAG and RobustRAG.
- **One-line summary:** Identifies and removes poisoned content during post-retrieval without extra training, reducing attack success on Gemini from 0.89 to 0.02.

**3. Towards Poisoning Robustness Certification for Natural Language Generation**
- **Authors:** Mihnea Ghitu, Matthew Wicker
- **Venue:** arXiv:2602.09757 (February 2026)
- **URL:** https://arxiv.org/abs/2602.09757
- **Why important:** First algorithm (Targeted Partition Aggregation) to certify validity against targeted poisoning attacks in NLG. Extends certified robustness ideas from C-RAG/RobustRAG to the generation pipeline itself.
- **One-line summary:** Computes minimum poisoning budget to induce harmful outputs and certifies stability/validity properties for LLM generation under data poisoning, including multi-turn agent settings.

**4. SDAG -- Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention**
- **Authors:** Sagie Dekel, Moshe Tennenholtz, Oren Kurland
- **Venue:** arXiv:2602.04711 (February 2026)
- **URL:** https://arxiv.org/abs/2602.04711
- **Why important:** Architectural defense against PoisonedRAG-style attacks that requires no fine-tuning; complements RobustRAG's aggregation approach with attention-mask isolation.
- **One-line summary:** Enforces block-sparse attention so tokens in one retrieved document cannot attend to tokens in another, eliminating cross-document poisoning influence without model changes.

**5. Provably Secure Retrieval-Augmented Generation**
- **Authors:** Pengcheng Zhou, Yinglun Feng, Zhongliang Yang
- **Venue:** arXiv:2508.01084 (August 2025)
- **URL:** https://arxiv.org/abs/2508.01084
- **Why important:** First formally verified encryption-based RAG framework ensuring both confidentiality and integrity with computational security proofs.
- **One-line summary:** Proposes a pre-storage full-encryption scheme for retrieved content and vector embeddings with formal security proofs for confidentiality and integrity.

---

### CLUSTER B: Poisoning Attacks and Defenses for RAG (Building on PoisonedRAG)

**6. RAGForensics -- Traceback of Poisoning Attacks to Retrieval-Augmented Generation**
- **Authors:** Baolei Zhang, Haoran Xin, Minghong Fang, Zhuqing Liu, Biao Yi, Tong Li, Zheli Liu
- **Venue:** The Web Conference 2025 (WWW '25); arXiv:2504.21668
- **URL:** https://arxiv.org/abs/2504.21668
- **Why important:** First traceback system for RAG poisoning; complements defense-at-inference (RobustRAG) with post-hoc forensic identification of malicious documents.
- **One-line summary:** Iteratively retrieves subsets and uses LLM-guided prompts to detect poisoned texts in a knowledge database, remaining robust to adaptive attacks.

**7. RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in RAG**
- **Authors:** Pankayaraj Pathmanathan, Michael-Andrei Panaitescu-Liess, Cho-Yu Jason Chiang, Furong Huang
- **Venue:** AAAI 2026 Workshop on New Frontiers in Information Retrieval (Oral); arXiv:2512.24268 (December 2025)
- **URL:** https://arxiv.org/abs/2512.24268
- **Why important:** Operates at retrieval stage (unlike post-retrieval defenses); RAGPart exploits document partitioning to reduce poisoned influence, and RAGMask uses token masking to detect suspicious tokens.
- **One-line summary:** Two complementary retrieval-stage defenses -- partitioning documents and masking suspicious tokens -- that reduce PoisonedRAG-style attack success while preserving normal performance.

**8. Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems**
- **Authors:** Scott Thornton
- **Venue:** arXiv:2603.18034 (March 2026)
- **URL:** https://arxiv.org/abs/2603.18034
- **Why important:** Demonstrates that PoisonedRAG-style attacks are corpus-dependent and that hybrid retrieval (BM25 + vector) can reduce attack success from 38% to 0% without modifying the LLM.
- **One-line summary:** Shows dual-document poisoning attacks have variable success rates (47--93%) across LLM families and that hybrid retrieval is a simple but effective defense.

**9. Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents**
- **Authors:** Avital Shafran, Roei Schuster, Vitaly Shmatikov
- **Venue:** USENIX Security 2025; arXiv:2406.05870
- **URL:** https://arxiv.org/abs/2406.05870
- **Why important:** Introduces a new attack modality (denial-of-service via single blocker documents) complementary to PoisonedRAG's targeted misinformation; highlights that safety metrics miss this threat.
- **One-line summary:** A single adversarial "blocker" document injected into a RAG database causes the system to refuse answering targeted queries, using black-box optimization without knowing the embedding or LLM.

---

### CLUSTER C: Conformal Prediction, Distribution Shift, and Uncertainty in RAG/NLP

**10. Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction**
- **Authors:** Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, Kevin Duh
- **Venue:** ECIR 2026; arXiv:2511.17908 (November 2025)
- **URL:** https://arxiv.org/abs/2511.17908
- **Why important:** Directly extends TRAQ by using conformal prediction for coverage-controlled context filtering in RAG. Explicitly discusses relaxing exchangeability assumptions as future work.
- **One-line summary:** Applies conformal prediction to filter irrelevant retrieved context while guaranteeing a target fraction of relevant snippets are retained, reducing context by 2--3x and improving factual accuracy.

**11. CONFLARE: CONFormal LArge language model REtrieval**
- **Authors:** Pouria Rouzrokh, Shahriar Faghani, Cooper U. Gamble, Moein Shariatnia, Bradley J. Erickson
- **Venue:** arXiv:2404.04287 (April 2024)
- **URL:** https://arxiv.org/abs/2404.04287
- **Why important:** Operationalizes conformal prediction for RAG retrieval with an open-source package; establishes similarity thresholds at user-specified error rates with statistical guarantees.
- **One-line summary:** Framework that calibrates embedding similarity thresholds via conformal prediction to guarantee that retrieved chunks contain the correct answer at a specified confidence level.

**12. Streamlining Conformal Information Retrieval via Score Refinement**
- **Authors:** Yotam Intrator, Ori Kelner, Regev Cohen, Roman Goldenberg, Ehud Rivlin, Daniel Freedman
- **Venue:** arXiv:2410.02914 (October 2024)
- **URL:** https://arxiv.org/abs/2410.02914
- **Why important:** Addresses the practical bottleneck that conformal prediction produces overly large retrieval sets; proposes monotone score transformations to shrink sets while preserving coverage guarantees.
- **One-line summary:** A simple monotone transformation of retrieval scores significantly reduces conformal prediction set sizes while maintaining statistical coverage guarantees on BEIR benchmarks.

**13. Domain-Shift-Aware Conformal Prediction for Large Language Models (DS-CP)**
- **Authors:** Zhexiao Lin, Yuanyuan Li, Neeraj Sarna, Yuanyuan Gao, Michael von Gablenz
- **Venue:** arXiv:2510.05566 (October 2025)
- **URL:** https://arxiv.org/abs/2510.05566
- **Why important:** Directly addresses exchangeability violations in conformal prediction for LLMs by reweighting calibration samples based on proximity to test prompts. Highly relevant to adversarial distribution shift in RAG.
- **One-line summary:** Reweights conformal calibration samples by test-prompt proximity to maintain valid coverage under domain shift, demonstrating more reliable coverage than standard CP on MMLU.

**14. Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift**
- **Authors:** Farbod Siahkali, Ashwin Verma, Vijay Gupta
- **Venue:** arXiv:2602.14913 (February 2026)
- **URL:** https://arxiv.org/abs/2602.14913
- **Why important:** Provides formal coverage lower bounds under bounded label-conditional covariate shift, directly applicable to scenarios where RAG retrieval introduces distribution shift.
- **One-line summary:** Derives coverage lower bounds under covariate shift using Wasserstein distances and proposes a slack-parameter method for adjusting conformal thresholds to maintain target coverage.

**15. Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations**
- **Authors:** Yanli Wang, Peng Kuang, Xiaoyu Han, Kaidi Xu, Haohan Wang
- **Venue:** arXiv:2604.16217 (April 2026)
- **URL:** https://arxiv.org/abs/2604.16217
- **Why important:** Proposes using internal LLM representations as nonconformity scores instead of surface-level outputs, achieving better validity-efficiency tradeoffs especially under distribution shift.
- **One-line summary:** Layer-wise information scores from internal model representations serve as more robust nonconformity measures than output-based alternatives, improving conformal prediction under distribution shift.

**16. Learning Conformal Abstention Policies for Adaptive Risk Management in LLMs**
- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi
- **Venue:** arXiv:2502.06884 (February 2025)
- **URL:** https://arxiv.org/abs/2502.06884
- **Why important:** Extends conformal prediction from static to adaptive abstention thresholds via reinforcement learning; directly relevant to abstention frameworks for RAG with formal coverage guarantees.
- **One-line summary:** Integrates RL with conformal prediction to learn dynamic abstention thresholds, improving hallucination detection AUROC by 22% and reducing calibration error by 70--85% while maintaining 90% coverage.

**17. The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems**
- **Authors:** Debu Sinha
- **Venue:** arXiv:2512.15068 (December 2025)
- **URL:** https://arxiv.org/abs/2512.15068
- **Why important:** Uses conformal prediction to study fundamental limits of embedding-based hallucination detection in RAG, finding that real hallucinations from RLHF-aligned models are semantically indistinguishable from faithful responses.
- **One-line summary:** Demonstrates that embedding-based hallucination detectors with conformal guarantees fail on real (vs. synthetic) hallucinations due to a "Semantic Illusion" -- surface semantics cannot distinguish them.

**18. URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models**
- **Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang
- **Venue:** arXiv:2603.19281 (March 2026)
- **URL:** https://arxiv.org/abs/2603.19281
- **Why important:** Comprehensive benchmark using conformal prediction (LAC, APS) to evaluate uncertainty in 8 RAG methods; reveals that accuracy improvements do not always reduce uncertainty.
- **One-line summary:** Converts open-ended RAG tasks to multiple-choice format for principled conformal uncertainty quantification, finding that no single RAG method is universally dependable and that retrieval noise inflates uncertainty.

**19. Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of RAG (FRANQ)**
- **Authors:** Ekaterina Fadeeva, Aleksandr Rubashevskii, Dzianis Piatrashyn, Roman Vashurin, Shehzaad Dhuliawala, Artem Shelmanov, Timothy Baldwin, Preslav Nakov, Mrinmaya Sachan, Maxim Panov
- **Venue:** arXiv:2505.21072 (May 2025; revised April 2026)
- **URL:** https://arxiv.org/abs/2505.21072
- **Why important:** Disentangles factuality from faithfulness in RAG uncertainty quantification, applying distinct UQ techniques conditioned on whether a statement is faithful to retrieved context.
- **One-line summary:** Conditions uncertainty quantification on faithfulness to retrieved context, outperforming existing methods at detecting factual errors across multiple RAG datasets.

---

### BONUS: Survey Papers

**20. Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions**
- **Authors:** Yuming Xu, Mingtao Zhang, Zhuohan Ge, Haoyang Li, Nicole Hu, Yongqi Zhang, Zhiyuan Wen, Jason Chen Zhang, Qing Li, Lei Chen
- **Venue:** arXiv:2604.08304 (April 2026)
- **URL:** https://arxiv.org/abs/2604.08304
- **Why important:** Comprehensive taxonomy (SLOT framework) mapping all known RAG attacks/defenses onto a six-stage pipeline; identifies structural gaps in current defenses.
- **One-line summary:** Introduces the SLOT framework organizing RAG security literature by attack Surface, defense Layer, security Objective (CIA), and Target scope across a six-stage knowledge-access pipeline.

**21. Towards Trustworthy Retrieval Augmented Generation for Large Language Models: A Survey**
- **Authors:** Bo Ni, Zheyuan Liu, Leyao Wang, et al. (20+ authors)
- **Venue:** arXiv:2502.06872 (February 2025)
- **URL:** https://arxiv.org/abs/2502.06872
- **Why important:** Comprehensive survey on trustworthy RAG covering reliability, privacy, safety, fairness, explainability, and accountability -- contextualizes all the seed papers within the broader landscape.
- **One-line summary:** Presents a roadmap for trustworthy RAG organized around six key dimensions with taxonomies and frameworks for each perspective.

---

### Summary of Coverage

| Focus Area | Papers Found |
|---|---|
| Conformal prediction extended to adversarial/poisoning settings in RAG | #3, #10, #12, #13, #14, #15, #17 |
| Certified defenses for RAG with formal guarantees | #1, #2, #3, #4, #5 |
| Distribution shift / exchangeability violations in CP for NLP | #13, #14, #15 |
| Abstention frameworks with guarantees | #16, #17 |
| RAG poisoning attacks and defenses (building on PoisonedRAG) | #2, #4, #6, #7, #8, #9 |
| Uncertainty quantification for RAG | #18, #19 |

agentId: a083061a3b1788628 (use SendMessage with to: 'a083061a3b1788628' to continue this agent)
&lt;usage>total_tokens: 37782
tool_uses: 41
duration_ms: 201957&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be635787-0e86-42e6-802e-e30d68e723b2",
  "isSidechain": false,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "type": "user",
  "uuid": "a7912b22-0e7b-46b9-a441-54c19c1d166a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2024-2026) that cite or build upon these specific seed papers. For each search, fetch the arxiv page of any promising result:\n\n1. Search: \"TRAQ trustworthy retrieval augmented question answering conformal prediction cited\"\n2. Search: \"C-RAG certified generation risks retrieval augmented ICML 2024 cited by\"\n3. Search: \"PoisonedRAG corpus poisoning defense 2025 2026\"\n4. Search: \"RobustRAG isolate then aggregate retrieval corruption 2025 2026\"\n5. Search: \"conformal prediction exchangeability RAG retrieval 2025 2026\"\n6. Search: \"abstention framework RAG systems guarantees 2025 2026\"\n7. Search: \"nonconformity score retrieval agreement 2025 2026\"\n\nFor each paper found, use WebFetch to read the abstract. Focus on papers that:\n- Extend conformal prediction to adversarial/poisoning settings in RAG\n- Provide certified defenses for RAG with formal guarantees\n- Study distribution shift or exchangeability violations in conformal prediction for NLP\n\nReturn a structured list with: title, authors, venue, URL, why important, one-line summary.",
    "agentId": "a083061a3b1788628",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive results. Here is the structured list of papers found.\n\n---\n\n## Structured List of Papers (2024--2026) Citing or Building on the Seed Papers\n\nPapers are organized into three thematic clusters matching your focus areas.\n\n---\n\n### CLUSTER A: Certified Defenses and Formal Guarantees for RAG\n\n**1. RobustRAG: Certifiably Robust RAG against Retrieval Corruption**\n- **Authors:** Chong Xiang, Tong Wu, Zexuan Zhong, David Wagner, Danqi Chen, Prateek Mittal\n- **Venue:** arXiv:2405.15556 (submitted May 2024; revised April 2026). Presented at ICML 2024 workshop track.\n- **URL:** https://arxiv.org/abs/2405.15556\n- **Why important:** First certified defense for RAG against retrieval corruption; provides formal robustness certificates via an isolate-then-aggregate strategy. Directly extends the C-RAG line of work.\n- **One-line summary:** Partitions retrieved passages into isolated groups, generates responses independently per group, and securely aggregates them, achieving 38% certifiable robust accuracy while maintaining 71% clean accuracy.\n\n**2. RAGDefender -- Rescuing the Unpoisoned: Efficient Defense against Knowledge Corruption Attacks on RAG Systems**\n- **Authors:** Minseok Kim, Hankook Lee, Hyungjoon Koo\n- **Venue:** ACSAC 2025 (Annual Computer Security Applications Conference); arXiv:2511.01268 (November 2025)\n- **URL:** https://arxiv.org/abs/2511.01268\n- **Why important:** Lightweight post-retrieval defense that outperforms RobustRAG, especially when poisoned passages outnumber clean ones. Directly benchmarks against both PoisonedRAG and RobustRAG.\n- **One-line summary:** Identifies and removes poisoned content during post-retrieval without extra training, reducing attack success on Gemini from 0.89 to 0.02.\n\n**3. Towards Poisoning Robustness Certification for Natural Language Generation**\n- **Authors:** Mihnea Ghitu, Matthew Wicker\n- **Venue:** arXiv:2602.09757 (February 2026)\n- **URL:** https://arxiv.org/abs/2602.09757\n- **Why important:** First algorithm (Targeted Partition Aggregation) to certify validity against targeted poisoning attacks in NLG. Extends certified robustness ideas from C-RAG/RobustRAG to the generation pipeline itself.\n- **One-line summary:** Computes minimum poisoning budget to induce harmful outputs and certifies stability/validity properties for LLM generation under data poisoning, including multi-turn agent settings.\n\n**4. SDAG -- Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention**\n- **Authors:** Sagie Dekel, Moshe Tennenholtz, Oren Kurland\n- **Venue:** arXiv:2602.04711 (February 2026)\n- **URL:** https://arxiv.org/abs/2602.04711\n- **Why important:** Architectural defense against PoisonedRAG-style attacks that requires no fine-tuning; complements RobustRAG's aggregation approach with attention-mask isolation.\n- **One-line summary:** Enforces block-sparse attention so tokens in one retrieved document cannot attend to tokens in another, eliminating cross-document poisoning influence without model changes.\n\n**5. Provably Secure Retrieval-Augmented Generation**\n- **Authors:** Pengcheng Zhou, Yinglun Feng, Zhongliang Yang\n- **Venue:** arXiv:2508.01084 (August 2025)\n- **URL:** https://arxiv.org/abs/2508.01084\n- **Why important:** First formally verified encryption-based RAG framework ensuring both confidentiality and integrity with computational security proofs.\n- **One-line summary:** Proposes a pre-storage full-encryption scheme for retrieved content and vector embeddings with formal security proofs for confidentiality and integrity.\n\n---\n\n### CLUSTER B: Poisoning Attacks and Defenses for RAG (Building on PoisonedRAG)\n\n**6. RAGForensics -- Traceback of Poisoning Attacks to Retrieval-Augmented Generation**\n- **Authors:** Baolei Zhang, Haoran Xin, Minghong Fang, Zhuqing Liu, Biao Yi, Tong Li, Zheli Liu\n- **Venue:** The Web Conference 2025 (WWW '25); arXiv:2504.21668\n- **URL:** https://arxiv.org/abs/2504.21668\n- **Why important:** First traceback system for RAG poisoning; complements defense-at-inference (RobustRAG) with post-hoc forensic identification of malicious documents.\n- **One-line summary:** Iteratively retrieves subsets and uses LLM-guided prompts to detect poisoned texts in a knowledge database, remaining robust to adaptive attacks.\n\n**7. RAGPart & RAGMask: Retrieval-Stage Defenses Against Corpus Poisoning in RAG**\n- **Authors:** Pankayaraj Pathmanathan, Michael-Andrei Panaitescu-Liess, Cho-Yu Jason Chiang, Furong Huang\n- **Venue:** AAAI 2026 Workshop on New Frontiers in Information Retrieval (Oral); arXiv:2512.24268 (December 2025)\n- **URL:** https://arxiv.org/abs/2512.24268\n- **Why important:** Operates at retrieval stage (unlike post-retrieval defenses); RAGPart exploits document partitioning to reduce poisoned influence, and RAGMask uses token masking to detect suspicious tokens.\n- **One-line summary:** Two complementary retrieval-stage defenses -- partitioning documents and masking suspicious tokens -- that reduce PoisonedRAG-style attack success while preserving normal performance.\n\n**8. Semantic Chameleon: Corpus-Dependent Poisoning Attacks and Defenses in RAG Systems**\n- **Authors:** Scott Thornton\n- **Venue:** arXiv:2603.18034 (March 2026)\n- **URL:** https://arxiv.org/abs/2603.18034\n- **Why important:** Demonstrates that PoisonedRAG-style attacks are corpus-dependent and that hybrid retrieval (BM25 + vector) can reduce attack success from 38% to 0% without modifying the LLM.\n- **One-line summary:** Shows dual-document poisoning attacks have variable success rates (47--93%) across LLM families and that hybrid retrieval is a simple but effective defense.\n\n**9. Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents**\n- **Authors:** Avital Shafran, Roei Schuster, Vitaly Shmatikov\n- **Venue:** USENIX Security 2025; arXiv:2406.05870\n- **URL:** https://arxiv.org/abs/2406.05870\n- **Why important:** Introduces a new attack modality (denial-of-service via single blocker documents) complementary to PoisonedRAG's targeted misinformation; highlights that safety metrics miss this threat.\n- **One-line summary:** A single adversarial \"blocker\" document injected into a RAG database causes the system to refuse answering targeted queries, using black-box optimization without knowing the embedding or LLM.\n\n---\n\n### CLUSTER C: Conformal Prediction, Distribution Shift, and Uncertainty in RAG/NLP\n\n**10. Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction**\n- **Authors:** Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, Kevin Duh\n- **Venue:** ECIR 2026; arXiv:2511.17908 (November 2025)\n- **URL:** https://arxiv.org/abs/2511.17908\n- **Why important:** Directly extends TRAQ by using conformal prediction for coverage-controlled context filtering in RAG. Explicitly discusses relaxing exchangeability assumptions as future work.\n- **One-line summary:** Applies conformal prediction to filter irrelevant retrieved context while guaranteeing a target fraction of relevant snippets are retained, reducing context by 2--3x and improving factual accuracy.\n\n**11. CONFLARE: CONFormal LArge language model REtrieval**\n- **Authors:** Pouria Rouzrokh, Shahriar Faghani, Cooper U. Gamble, Moein Shariatnia, Bradley J. Erickson\n- **Venue:** arXiv:2404.04287 (April 2024)\n- **URL:** https://arxiv.org/abs/2404.04287\n- **Why important:** Operationalizes conformal prediction for RAG retrieval with an open-source package; establishes similarity thresholds at user-specified error rates with statistical guarantees.\n- **One-line summary:** Framework that calibrates embedding similarity thresholds via conformal prediction to guarantee that retrieved chunks contain the correct answer at a specified confidence level.\n\n**12. Streamlining Conformal Information Retrieval via Score Refinement**\n- **Authors:** Yotam Intrator, Ori Kelner, Regev Cohen, Roman Goldenberg, Ehud Rivlin, Daniel Freedman\n- **Venue:** arXiv:2410.02914 (October 2024)\n- **URL:** https://arxiv.org/abs/2410.02914\n- **Why important:** Addresses the practical bottleneck that conformal prediction produces overly large retrieval sets; proposes monotone score transformations to shrink sets while preserving coverage guarantees.\n- **One-line summary:** A simple monotone transformation of retrieval scores significantly reduces conformal prediction set sizes while maintaining statistical coverage guarantees on BEIR benchmarks.\n\n**13. Domain-Shift-Aware Conformal Prediction for Large Language Models (DS-CP)**\n- **Authors:** Zhexiao Lin, Yuanyuan Li, Neeraj Sarna, Yuanyuan Gao, Michael von Gablenz\n- **Venue:** arXiv:2510.05566 (October 2025)\n- **URL:** https://arxiv.org/abs/2510.05566\n- **Why important:** Directly addresses exchangeability violations in conformal prediction for LLMs by reweighting calibration samples based on proximity to test prompts. Highly relevant to adversarial distribution shift in RAG.\n- **One-line summary:** Reweights conformal calibration samples by test-prompt proximity to maintain valid coverage under domain shift, demonstrating more reliable coverage than standard CP on MMLU.\n\n**14. Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift**\n- **Authors:** Farbod Siahkali, Ashwin Verma, Vijay Gupta\n- **Venue:** arXiv:2602.14913 (February 2026)\n- **URL:** https://arxiv.org/abs/2602.14913\n- **Why important:** Provides formal coverage lower bounds under bounded label-conditional covariate shift, directly applicable to scenarios where RAG retrieval introduces distribution shift.\n- **One-line summary:** Derives coverage lower bounds under covariate shift using Wasserstein distances and proposes a slack-parameter method for adjusting conformal thresholds to maintain target coverage.\n\n**15. Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations**\n- **Authors:** Yanli Wang, Peng Kuang, Xiaoyu Han, Kaidi Xu, Haohan Wang\n- **Venue:** arXiv:2604.16217 (April 2026)\n- **URL:** https://arxiv.org/abs/2604.16217\n- **Why important:** Proposes using internal LLM representations as nonconformity scores instead of surface-level outputs, achieving better validity-efficiency tradeoffs especially under distribution shift.\n- **One-line summary:** Layer-wise information scores from internal model representations serve as more robust nonconformity measures than output-based alternatives, improving conformal prediction under distribution shift.\n\n**16. Learning Conformal Abstention Policies for Adaptive Risk Management in LLMs**\n- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi\n- **Venue:** arXiv:2502.06884 (February 2025)\n- **URL:** https://arxiv.org/abs/2502.06884\n- **Why important:** Extends conformal prediction from static to adaptive abstention thresholds via reinforcement learning; directly relevant to abstention frameworks for RAG with formal coverage guarantees.\n- **One-line summary:** Integrates RL with conformal prediction to learn dynamic abstention thresholds, improving hallucination detection AUROC by 22% and reducing calibration error by 70--85% while maintaining 90% coverage.\n\n**17. The Semantic Illusion: Certified Limits of Embedding-Based Hallucination Detection in RAG Systems**\n- **Authors:** Debu Sinha\n- **Venue:** arXiv:2512.15068 (December 2025)\n- **URL:** https://arxiv.org/abs/2512.15068\n- **Why important:** Uses conformal prediction to study fundamental limits of embedding-based hallucination detection in RAG, finding that real hallucinations from RLHF-aligned models are semantically indistinguishable from faithful responses.\n- **One-line summary:** Demonstrates that embedding-based hallucination detectors with conformal guarantees fail on real (vs. synthetic) hallucinations due to a \"Semantic Illusion\" -- surface semantics cannot distinguish them.\n\n**18. URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models**\n- **Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang\n- **Venue:** arXiv:2603.19281 (March 2026)\n- **URL:** https://arxiv.org/abs/2603.19281\n- **Why important:** Comprehensive benchmark using conformal prediction (LAC, APS) to evaluate uncertainty in 8 RAG methods; reveals that accuracy improvements do not always reduce uncertainty.\n- **One-line summary:** Converts open-ended RAG tasks to multiple-choice format for principled conformal uncertainty quantification, finding that no single RAG method is universally dependable and that retrieval noise inflates uncertainty.\n\n**19. Faithfulness-Aware Uncertainty Quantification for Fact-Checking the Output of RAG (FRANQ)**\n- **Authors:** Ekaterina Fadeeva, Aleksandr Rubashevskii, Dzianis Piatrashyn, Roman Vashurin, Shehzaad Dhuliawala, Artem Shelmanov, Timothy Baldwin, Preslav Nakov, Mrinmaya Sachan, Maxim Panov\n- **Venue:** arXiv:2505.21072 (May 2025; revised April 2026)\n- **URL:** https://arxiv.org/abs/2505.21072\n- **Why important:** Disentangles factuality from faithfulness in RAG uncertainty quantification, applying distinct UQ techniques conditioned on whether a statement is faithful to retrieved context.\n- **One-line summary:** Conditions uncertainty quantification on faithfulness to retrieved context, outperforming existing methods at detecting factual errors across multiple RAG datasets.\n\n---\n\n### BONUS: Survey Papers\n\n**20. Securing Retrieval-Augmented Generation: A Taxonomy of Attacks, Defenses, and Future Directions**\n- **Authors:** Yuming Xu, Mingtao Zhang, Zhuohan Ge, Haoyang Li, Nicole Hu, Yongqi Zhang, Zhiyuan Wen, Jason Chen Zhang, Qing Li, Lei Chen\n- **Venue:** arXiv:2604.08304 (April 2026)\n- **URL:** https://arxiv.org/abs/2604.08304\n- **Why important:** Comprehensive taxonomy (SLOT framework) mapping all known RAG attacks/defenses onto a six-stage pipeline; identifies structural gaps in current defenses.\n- **One-line summary:** Introduces the SLOT framework organizing RAG security literature by attack Surface, defense Layer, security Objective (CIA), and Target scope across a six-stage knowledge-access pipeline.\n\n**21. Towards Trustworthy Retrieval Augmented Generation for Large Language Models: A Survey**\n- **Authors:** Bo Ni, Zheyuan Liu, Leyao Wang, et al. (20+ authors)\n- **Venue:** arXiv:2502.06872 (February 2025)\n- **URL:** https://arxiv.org/abs/2502.06872\n- **Why important:** Comprehensive survey on trustworthy RAG covering reliability, privacy, safety, fairness, explainability, and accountability -- contextualizes all the seed papers within the broader landscape.\n- **One-line summary:** Presents a roadmap for trustworthy RAG organized around six key dimensions with taxonomies and frameworks for each perspective.\n\n---\n\n### Summary of Coverage\n\n| Focus Area | Papers Found |\n|---|---|\n| Conformal prediction extended to adversarial/poisoning settings in RAG | #3, #10, #12, #13, #14, #15, #17 |\n| Certified defenses for RAG with formal guarantees | #1, #2, #3, #4, #5 |\n| Distribution shift / exchangeability violations in CP for NLP | #13, #14, #15 |\n| Abstention frameworks with guarantees | #16, #17 |\n| RAG poisoning attacks and defenses (building on PoisonedRAG) | #2, #4, #6, #7, #8, #9 |\n| Uncertainty quantification for RAG | #18, #19 |"
      }
    ],
    "totalDurationMs": 201957,
    "totalTokens": 37782,
    "totalToolUseCount": 41,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3763,
      "cache_read_input_tokens": 29579,
      "output_tokens": 4439,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3763
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4439,
          "cache_read_input_tokens": 29579,
          "cache_creation_input_tokens": 3763,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3763,
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
      "otherToolCount": 41
    }
  },
  "sourceToolAssistantUUID": "be635787-0e86-42e6-802e-e30d68e723b2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "a7912b22-0e7b-46b9-a441-54c19c1d166a",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on conformal prediction for RAG",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Tool result

_source line 38 · 2026-05-30T06:21:06.219Z_

<details><summary>↩ Tool result · `toolu_01NLZHfDjvHdAe1SiGLEDw9e`</summary>

```text
I now have comprehensive information on all the papers. Here is the structured literature review.

---

## Conformal Prediction under Distribution Shift: Structured Literature Review (2024--2026)

---

### CATEGORY A: Conformal Prediction + Covariate Shift + NLP/Language Models

---

**1. CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift**
- **Authors:** Zirui Hu, Zheng Zhang, Yingjie Wang, Leszek Rutkowski, Dacheng Tao
- **Venue:** ICLR 2026
- **URL:** https://openreview.net/forum?id=eiBp7rsc3K
- **Why important:** Directly addresses conformal prediction for LLM factuality under covariate shift using online density ratio estimation to reweight calibration data. Removes the exchangeability assumption between calibration and test data.
- **One-line summary:** Uses online density ratio estimation to adaptively reweight calibration data for conformal factuality guarantees on LLMs under non-stationary covariate shift, validated on MedLFQA, WikiData, and WildChat+.

---

**2. Domain-Shift-Aware Conformal Prediction for Large Language Models (DS-CP)**
- **Authors:** Zhexiao Lin, Yuanyuan Li, Neeraj Sarna, Yuanyuan Gao, Michael von Gablenz
- **Venue:** arXiv preprint (October 2025)
- **URL:** https://arxiv.org/abs/2510.05566
- **Why important:** Tackles the curse of dimensionality in weighted conformal prediction for high-dimensional LLM prompts; proposes proximity-based reweighting of calibration samples rather than explicit density ratio estimation.
- **One-line summary:** Reweights calibration samples by proximity to the test prompt to maintain conformal coverage under domain shift for LLMs, circumventing infeasible density ratio estimation in high dimensions.

---

**3. Conformal Prediction for Natural Language Processing: A Survey**
- **Authors:** Margarida M. Campos, Antonio Farinhas, Chrysoula Zerva, Mario A.T. Figueiredo, Andre F.T. Martins
- **Venue:** Transactions of the Association for Computational Linguistics (TACL), 2025
- **URL:** https://arxiv.org/abs/2405.01976
- **Why important:** Comprehensive survey of conformal prediction techniques applied to NLP, covering guarantees, existing applications, and open challenges including distribution shift.
- **One-line summary:** A thorough survey cataloging conformal prediction methods, their statistical guarantees, and applications across NLP tasks, identifying distribution shift as a key open challenge.

---

**4. Mitigating LLM Hallucinations via Conformal Abstention**
- **Authors:** Yasin Abbasi Yadkori, Ilja Kuzborskij, David Stutz, Andras Gyorgy, Adam Fisch, Arnaud Doucet, Iuliya Beloshapka, Wei-Hung Weng, Yao-Yuan Yang, Csaba Szepesvari, Ali Taylan Cemgil, Nenad Tomasev
- **Venue:** NeurIPS 2024
- **URL:** https://arxiv.org/abs/2405.01563
- **Why important:** Foundational work on using conformal prediction to create principled abstention policies for LLMs, bounding hallucination rates with distribution-free guarantees.
- **One-line summary:** Uses self-consistency-based similarity scoring with conformal prediction to determine when an LLM should abstain from answering, providing statistical upper bounds on hallucination rates.

---

**5. Learning Conformal Abstention Policies for Adaptive Risk Management in Large LLMs & VLMs**
- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi
- **Venue:** arXiv preprint (February 2025)
- **URL:** https://arxiv.org/abs/2502.06884
- **Why important:** Extends conformal abstention with reinforcement learning to learn dynamic thresholds rather than fixed ones, enabling adaptive risk management across tasks.
- **One-line summary:** Combines RL with conformal prediction to dynamically learn abstention thresholds for LLMs/VLMs, achieving up to 22% AUROC improvement in hallucination detection and 70-85% calibration error reduction.

---

### CATEGORY B: Weighted / Reweighted Conformal Prediction under Distribution Shift

---

**6. Wasserstein-regularized Conformal Prediction under General Distribution Shift (WR-CP)**
- **Authors:** Rui Xu, Chao Chen, Yue Sun, Parvathinathan Venkitasubramaniam, Sihong Xie
- **Venue:** arXiv preprint (January 2025)
- **URL:** https://arxiv.org/abs/2501.13430
- **Why important:** Proposes Wasserstein distance bounds (tighter than total variation) to separately measure covariate and concept shift impacts on coverage, with a practical algorithm combining importance weighting and regularized representation learning.
- **One-line summary:** Uses Wasserstein-distance-based coverage gap bounds to handle both covariate and concept shift, achieving ~3.2% coverage gaps and 37% smaller prediction sets than worst-case approaches.

---

**7. Conformal Prediction Under Generalized Covariate Shift with Posterior Drift**
- **Authors:** Baozhen Wang, Xingye Qiao
- **Venue:** AISTATS 2025
- **URL:** https://arxiv.org/abs/2502.17744
- **Why important:** Extends conformal prediction beyond pure covariate shift to handle posterior drift (concept shift), providing coverage guarantees in the target domain.
- **One-line summary:** A weighted conformal classifier for transfer learning that leverages both source and target samples under covariate shift with posterior drift, with target-domain coverage guarantees.

---

**8. Group-Weighted Conformal Prediction**
- **Authors:** Aabesh Bhattacharyya, Rina Foygel Barber
- **Venue:** arXiv preprint (January 2024)
- **URL:** https://arxiv.org/abs/2401.17452
- **Why important:** Analyzes weighted conformal prediction when the covariate shift is structured (finite groups), showing that group structure enables much tighter coverage guarantees despite density ratio estimation error.
- **One-line summary:** Exploits finite group structure in covariate shift to improve weighted conformal prediction coverage guarantees beyond what general density ratio estimation error bounds permit.

---

**9. WQLCP: Weighted Adaptive Conformal Prediction for Robust Uncertainty Quantification Under Distribution Shifts**
- **Authors:** Shadi Alijani, Homayoun Najjaran
- **Venue:** CVPR 2025 Workshops (UNCV)
- **URL:** https://arxiv.org/abs/2505.19587
- **Why important:** Uses VAE reconstruction losses as an uncertainty metric combined with weighted exchangeability to adapt calibration quantile thresholds under distribution shift.
- **One-line summary:** Scales conformal score functions using VAE reconstruction losses and adjusts calibration quantile thresholds via weighted exchangeability, maintaining coverage with smaller prediction sets on ImageNet variants.

---

**10. Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift**
- **Authors:** Farbod Siahkali, Ashwin Verma, Vijay Gupta
- **Venue:** arXiv preprint (February 2026)
- **URL:** https://arxiv.org/abs/2602.14913
- **Why important:** Provides coverage lower bounds under label-conditional covariate shift using domain adaptation and Wasserstein shift measures, with a source-tuned pseudo-calibration approach.
- **One-line summary:** Establishes target coverage lower bounds for pseudo-calibrated conformal prediction under label-conditional covariate shift using domain adaptation techniques and Wasserstein shift measures.

---

### CATEGORY C: Adaptive / Online Conformal Inference under Distribution Shift

---

**11. Online Conformal Inference with Retrospective Adjustment for Faster Adaptation to Distribution Shift**
- **Authors:** Jungbin Jun, Ilsang Ohn
- **Venue:** arXiv preprint (November 2025)
- **URL:** https://arxiv.org/abs/2511.04275
- **Why important:** Introduces retrospective adjustment to online conformal prediction, retroactively updating past predictions when new data arrives for faster adaptation to distribution shift.
- **One-line summary:** Achieves faster coverage recalibration in online conformal prediction by retroactively adjusting past predictions using efficient leave-one-out update formulas when new data arrives.

---

**12. CORE: Conformal Regression under Distribution Shift via Reinforcement Learning**
- **Authors:** Yilei Zhao, Wentao Zhang, Miguel R. Pebes-Trujillo, Junxian Liu, Hongxin Wei, Wei Yang Bryan Lim
- **Venue:** ICLR 2026
- **URL:** https://openreview.net/forum?id=7puF5JOkKk
- **Why important:** Creates a mutual feedback loop between RL and conformal prediction for time-series forecasting, using RL exploration to better cover uncertain/outlier regions under distribution shift.
- **One-line summary:** Integrates reinforcement learning with conformal prediction to dynamically adapt prediction intervals under distribution shift in time-series, improving coverage by 1.36% and reducing interval length by 5.03%.

---

**13. Conformal Prediction under Levy-Prokhorov Distribution Shifts**
- **Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, Youssef Marzouk
- **Venue:** arXiv preprint (February 2025)
- **URL:** https://arxiv.org/abs/2502.14105
- **Why important:** Models distribution shifts using Levy-Prokhorov ambiguity sets (capturing both local and global perturbations), reducing high-dimensional shifts to manageable 1D shifts through the scoring function.
- **One-line summary:** Reduces complex high-dimensional distribution shifts to 1D via LP ambiguity sets routed through the scoring function, enabling tractable worst-case quantile and coverage computations.

---

**14. Adapting Prediction Sets to Distribution Shifts Without Labels (ECP/EACP)**
- **Authors:** Kevin Kasa, Zhiyu Zhang, Heng Yang, Graham W. Taylor
- **Venue:** arXiv preprint (June 2024)
- **URL:** https://arxiv.org/abs/2406.01416
- **Why important:** Adapts conformal prediction sets at test time using only the base model's own uncertainty evaluation, requiring no labeled test data -- nearly matching fully supervised adaptation.
- **One-line summary:** Adjusts conformal score functions using the base model's uncertainty estimates to adapt prediction sets to distribution shifts without any labeled test data.

---

**15. Test-time Recalibration of Conformal Predictors Under Distribution Shift Based on Unlabeled Examples**
- **Authors:** Fatih Furkan Yilmaz, Reinhard Heckel
- **Venue:** ICLR 2023
- **URL:** https://arxiv.org/abs/2210.04166
- **Why important:** Foundational work on test-time recalibration using only unlabeled examples from the shifted distribution; provides theoretical guarantees for specific shift models.
- **One-line summary:** Recalibrates conformal prediction thresholds at test time using only unlabeled examples from a shifted distribution, achieving reliable uncertainty estimates under natural distribution shifts.

---

### CATEGORY D: Partition, Voting, and Aggregation in Conformal Prediction

---

**16. Merging Uncertainty Sets via Majority Vote**
- **Authors:** Matteo Gasparin, Aaditya Ramdas
- **Venue:** arXiv preprint (January 2024)
- **URL:** https://arxiv.org/abs/2401.09379
- **Why important:** Directly addresses the partition-and-vote paradigm: merges K prediction sets (from different estimators or conformal methods) via majority voting with provable coverage guarantees, plus weighted and randomized extensions.
- **One-line summary:** Combines K uncertainty sets (confidence intervals, conformal prediction sets) via a majority vote procedure maintaining error guarantees, with extensions for weighted averaging and randomized set-size reduction.

---

**17. Conformal Online Model Aggregation (COMA)**
- **Authors:** Matteo Gasparin, Aaditya Ramdas
- **Venue:** arXiv preprint (March 2024)
- **URL:** https://arxiv.org/abs/2403.15527
- **Why important:** Proposes online aggregation of conformal prediction sets from multiple black-box models via adaptive weighted voting, maintaining coverage under distribution drift -- highly relevant to partition-and-vote robustness.
- **One-line summary:** Aggregates conformal prediction sets from multiple models via online weighted voting with adaptive weights, maintaining coverage guarantees even under distribution drift.

---

**18. Valid Selection among Conformal Sets**
- **Authors:** Mahmoud Hegazy, Liviu Aolaritei, Michael I. Jordan, Aymeric Dieuleveut
- **Venue:** arXiv preprint (June 2025)
- **URL:** https://arxiv.org/abs/2506.20173
- **Why important:** Addresses the invalidation problem when selecting the best (e.g., smallest) among multiple valid conformal sets; proposes a stability-based approach preserving coverage after selection.
- **One-line summary:** Provides a stability-based method ensuring that selecting the most desirable prediction set from multiple valid conformal sets does not invalidate coverage guarantees.

---

**19. Multi-Distribution Robust Conformal Prediction**
- **Authors:** Yuqi Yang, Ying Jin
- **Venue:** arXiv preprint (January 2026)
- **URL:** https://arxiv.org/abs/2601.02998
- **Why important:** Constructs prediction sets with finite-sample coverage guarantees uniformly valid across multiple heterogeneous source distributions, with a provably optimal max-p aggregation scheme.
- **One-line summary:** A max-p aggregation scheme for constructing conformal prediction sets with provably optimal multi-distribution coverage guarantees, connecting to distributionally robust optimization and fairness.

---

**20. Partition Learning Conformal Prediction (PLCP)**
- **Authors:** Shayan Kiyani, George Pappas, Hamed Hassani
- **Venue:** arXiv preprint (April 2024)
- **URL:** https://arxiv.org/abs/2404.17487
- **Why important:** Learns uncertainty-guided partitions from calibration data to improve conditional coverage validity, directly relevant to partition-based conformal prediction.
- **One-line summary:** Learns partitions from calibration data via alternating gradient descent to improve conditional coverage of conformal prediction sets, with finite-sample conditional guarantees.

---

**21. Split Conformal Prediction under Data Contamination**
- **Authors:** Jase Clarkson, Wenkai Xu, Mihai Cucuringu, Yvik Swan, Gesine Reinert
- **Venue:** arXiv preprint (July 2024)
- **URL:** https://arxiv.org/abs/2407.07700
- **Why important:** Quantifies how contaminated calibration data affects conformal coverage and proposes Contamination Robust Conformal Prediction, relevant to robustness when calibration and test distributions differ.
- **One-line summary:** Quantifies the effect of calibration data contamination on split conformal prediction and proposes a classification-specific robust correction method.

---

### CATEGORY E: Conformal Prediction + RAG / Retrieval-Augmented Generation

---

**22. URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models**
- **Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang
- **Venue:** arXiv preprint (March 2026)
- **URL:** https://arxiv.org/abs/2603.19281
- **Why important:** First comprehensive benchmark for UQ in RAG systems using conformal prediction (LAC, APS metrics), covering healthcare, programming, math, and general text domains.
- **One-line summary:** Converts RAG open-ended generation to multiple-choice format to enable conformal prediction-based UQ evaluation, finding that retrieval errors can amplify confident hallucinations.

---

**23. CONFLARE: CONFormal LArge language model REtrieval**
- **Authors:** Pouria Rouzrokh, Shahriar Faghani, Cooper U. Gamble, Moein Shariatnia, Bradley J. Erickson
- **Venue:** arXiv preprint (April 2024)
- **URL:** https://arxiv.org/abs/2404.04287
- **Why important:** Applies conformal prediction directly to the retrieval step of RAG, establishing thresholds on retrieval similarity scores to guarantee the true answer is captured in context with (1-alpha) confidence.
- **One-line summary:** A four-step conformal prediction framework for RAG retrieval that sets similarity-score thresholds ensuring retrieved context contains the true answer with user-specified confidence.

---

**24. Conformal-RAG: Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality**
- **Authors:** Naihe Feng, Yi Sui, Shiyi Hou, Jesse C. Cresswell, Ga Wu
- **Venue:** arXiv preprint (June 2025)
- **URL:** https://arxiv.org/abs/2506.20978
- **Why important:** Combines conformal prediction with RAG to ensure group-conditional coverage across sub-domains without manual labeling, retaining up to 60% more high-quality sub-claims.
- **One-line summary:** Leverages conformal prediction for group-conditional factuality guarantees in RAG, retaining 60% more high-quality sub-claims than direct CP application while maintaining reliability.

---

**25. Uncertainty Quantification for Retrieval-Augmented Reasoning (R2C)**
- **Authors:** Heydar Soudani, Hamed Zamani, Faegheh Hasibi
- **Venue:** arXiv preprint (October 2025)
- **URL:** https://arxiv.org/abs/2510.11483
- **Why important:** Proposes UQ for retrieval-augmented reasoning by perturbing multi-step reasoning processes, achieving 5%+ AUROC gains for abstention decisions.
- **One-line summary:** Quantifies uncertainty in retrieval-augmented reasoning by perturbing reasoning steps across both retrieval and generation, enabling better abstention and model selection.

---

**26. Eliminating Hallucination-Induced Errors in LLM Code Generation with Functional Clustering**
- **Authors:** Chaitanya Ravuri, Saman Amarasinghe
- **Venue:** arXiv preprint (June 2025)
- **URL:** https://arxiv.org/abs/2506.11021
- **Why important:** While not strictly conformal prediction, uses a voting/clustering approach (functional clustering of sampled programs) that mirrors partition-and-vote ideas for selective prediction in code generation.
- **One-line summary:** Samples multiple candidate programs, clusters by input-output behavior, and uses the largest cluster's mass as a confidence score, reducing code generation error rates from 65% to 2%.

---

### Summary of Key Themes

1. **Density ratio reweighting for LLM conformal prediction** -- CoFact (ICLR 2026) and DS-CP directly tackle covariate shift for language models, with CoFact using online density ratio estimation and DS-CP using proximity-based reweighting to avoid the curse of dimensionality.

2. **Wasserstein and LP-based distribution shift bounds** -- WR-CP and the Levy-Prokhorov paper provide tighter theoretical bounds than total variation for coverage gap analysis under general shift.

3. **Majority vote / aggregation of conformal sets** -- Gasparin & Ramdas (2024) provide the canonical majority vote merging procedure; COMA extends it to online settings with adaptive weights under drift; Yang & Jin (2026) address multi-distribution robustness with a max-p scheme.

4. **Partition-based conditional coverage** -- PLCP learns uncertainty-guided partitions to improve conditional validity; Group-Weighted CP exploits group structure for tighter guarantees.

5. **Online / adaptive methods** -- Retrospective adjustment (Jun & Ohn, 2025) and CORE (ICLR 2026) push beyond forward-only adaptation, using leave-one-out updates and RL feedback loops respectively.

6. **Conformal abstention for LLMs** -- The NeurIPS 2024 conformal abstention paper and its RL-enhanced successor (Tayebati et al., 2025) provide principled selective prediction for hallucination mitigation.

7. **Conformal prediction for RAG** -- CONFLARE, Conformal-RAG, URAG, and R2C represent an emerging body of work applying conformal guarantees to retrieval quality, response factuality, and reasoning uncertainty in RAG pipelines.

agentId: ad674cb89db26599b (use SendMessage with to: 'ad674cb89db26599b' to continue this agent)
&lt;usage>total_tokens: 33510
tool_uses: 40
duration_ms: 219014&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a089076b-e133-495f-96bd-df068d113d28",
  "isSidechain": false,
  "promptId": "74eeeb0a-7666-4050-9925-e05560d87380",
  "type": "user",
  "uuid": "4fc9a70a-a931-4ed2-b127-8e8eef5bf5e4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for recent papers (2024-2026) on conformal prediction under distribution shift, covariate shift, or domain adaptation, particularly for NLP/language models. Also search for papers on partition-and-vote or majority-voting approaches in conformal prediction.\n\nExecute these searches and fetch arxiv pages for promising results:\n\n1. Search: \"conformal prediction covariate shift NLP language models 2025 2026\"\n2. Search: \"partition vote conformal prediction robustness\"\n3. Search: \"weighted conformal prediction distribution shift language 2024 2025\"\n4. Search: \"adaptive conformal inference online distribution shift 2025 2026\"\n5. Search: \"conformal prediction test-time distribution shift 2025 2026\"\n6. Search: \"selective prediction RAG retrieval augmented generation 2025 2026\"\n\nFor each paper found, use WebFetch to read the abstract. Return a structured list with: title, authors, venue, URL, why important, one-line summary.",
    "agentId": "ad674cb89db26599b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all the papers. Here is the structured literature review.\n\n---\n\n## Conformal Prediction under Distribution Shift: Structured Literature Review (2024--2026)\n\n---\n\n### CATEGORY A: Conformal Prediction + Covariate Shift + NLP/Language Models\n\n---\n\n**1. CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift**\n- **Authors:** Zirui Hu, Zheng Zhang, Yingjie Wang, Leszek Rutkowski, Dacheng Tao\n- **Venue:** ICLR 2026\n- **URL:** https://openreview.net/forum?id=eiBp7rsc3K\n- **Why important:** Directly addresses conformal prediction for LLM factuality under covariate shift using online density ratio estimation to reweight calibration data. Removes the exchangeability assumption between calibration and test data.\n- **One-line summary:** Uses online density ratio estimation to adaptively reweight calibration data for conformal factuality guarantees on LLMs under non-stationary covariate shift, validated on MedLFQA, WikiData, and WildChat+.\n\n---\n\n**2. Domain-Shift-Aware Conformal Prediction for Large Language Models (DS-CP)**\n- **Authors:** Zhexiao Lin, Yuanyuan Li, Neeraj Sarna, Yuanyuan Gao, Michael von Gablenz\n- **Venue:** arXiv preprint (October 2025)\n- **URL:** https://arxiv.org/abs/2510.05566\n- **Why important:** Tackles the curse of dimensionality in weighted conformal prediction for high-dimensional LLM prompts; proposes proximity-based reweighting of calibration samples rather than explicit density ratio estimation.\n- **One-line summary:** Reweights calibration samples by proximity to the test prompt to maintain conformal coverage under domain shift for LLMs, circumventing infeasible density ratio estimation in high dimensions.\n\n---\n\n**3. Conformal Prediction for Natural Language Processing: A Survey**\n- **Authors:** Margarida M. Campos, Antonio Farinhas, Chrysoula Zerva, Mario A.T. Figueiredo, Andre F.T. Martins\n- **Venue:** Transactions of the Association for Computational Linguistics (TACL), 2025\n- **URL:** https://arxiv.org/abs/2405.01976\n- **Why important:** Comprehensive survey of conformal prediction techniques applied to NLP, covering guarantees, existing applications, and open challenges including distribution shift.\n- **One-line summary:** A thorough survey cataloging conformal prediction methods, their statistical guarantees, and applications across NLP tasks, identifying distribution shift as a key open challenge.\n\n---\n\n**4. Mitigating LLM Hallucinations via Conformal Abstention**\n- **Authors:** Yasin Abbasi Yadkori, Ilja Kuzborskij, David Stutz, Andras Gyorgy, Adam Fisch, Arnaud Doucet, Iuliya Beloshapka, Wei-Hung Weng, Yao-Yuan Yang, Csaba Szepesvari, Ali Taylan Cemgil, Nenad Tomasev\n- **Venue:** NeurIPS 2024\n- **URL:** https://arxiv.org/abs/2405.01563\n- **Why important:** Foundational work on using conformal prediction to create principled abstention policies for LLMs, bounding hallucination rates with distribution-free guarantees.\n- **One-line summary:** Uses self-consistency-based similarity scoring with conformal prediction to determine when an LLM should abstain from answering, providing statistical upper bounds on hallucination rates.\n\n---\n\n**5. Learning Conformal Abstention Policies for Adaptive Risk Management in Large LLMs & VLMs**\n- **Authors:** Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi\n- **Venue:** arXiv preprint (February 2025)\n- **URL:** https://arxiv.org/abs/2502.06884\n- **Why important:** Extends conformal abstention with reinforcement learning to learn dynamic thresholds rather than fixed ones, enabling adaptive risk management across tasks.\n- **One-line summary:** Combines RL with conformal prediction to dynamically learn abstention thresholds for LLMs/VLMs, achieving up to 22% AUROC improvement in hallucination detection and 70-85% calibration error reduction.\n\n---\n\n### CATEGORY B: Weighted / Reweighted Conformal Prediction under Distribution Shift\n\n---\n\n**6. Wasserstein-regularized Conformal Prediction under General Distribution Shift (WR-CP)**\n- **Authors:** Rui Xu, Chao Chen, Yue Sun, Parvathinathan Venkitasubramaniam, Sihong Xie\n- **Venue:** arXiv preprint (January 2025)\n- **URL:** https://arxiv.org/abs/2501.13430\n- **Why important:** Proposes Wasserstein distance bounds (tighter than total variation) to separately measure covariate and concept shift impacts on coverage, with a practical algorithm combining importance weighting and regularized representation learning.\n- **One-line summary:** Uses Wasserstein-distance-based coverage gap bounds to handle both covariate and concept shift, achieving ~3.2% coverage gaps and 37% smaller prediction sets than worst-case approaches.\n\n---\n\n**7. Conformal Prediction Under Generalized Covariate Shift with Posterior Drift**\n- **Authors:** Baozhen Wang, Xingye Qiao\n- **Venue:** AISTATS 2025\n- **URL:** https://arxiv.org/abs/2502.17744\n- **Why important:** Extends conformal prediction beyond pure covariate shift to handle posterior drift (concept shift), providing coverage guarantees in the target domain.\n- **One-line summary:** A weighted conformal classifier for transfer learning that leverages both source and target samples under covariate shift with posterior drift, with target-domain coverage guarantees.\n\n---\n\n**8. Group-Weighted Conformal Prediction**\n- **Authors:** Aabesh Bhattacharyya, Rina Foygel Barber\n- **Venue:** arXiv preprint (January 2024)\n- **URL:** https://arxiv.org/abs/2401.17452\n- **Why important:** Analyzes weighted conformal prediction when the covariate shift is structured (finite groups), showing that group structure enables much tighter coverage guarantees despite density ratio estimation error.\n- **One-line summary:** Exploits finite group structure in covariate shift to improve weighted conformal prediction coverage guarantees beyond what general density ratio estimation error bounds permit.\n\n---\n\n**9. WQLCP: Weighted Adaptive Conformal Prediction for Robust Uncertainty Quantification Under Distribution Shifts**\n- **Authors:** Shadi Alijani, Homayoun Najjaran\n- **Venue:** CVPR 2025 Workshops (UNCV)\n- **URL:** https://arxiv.org/abs/2505.19587\n- **Why important:** Uses VAE reconstruction losses as an uncertainty metric combined with weighted exchangeability to adapt calibration quantile thresholds under distribution shift.\n- **One-line summary:** Scales conformal score functions using VAE reconstruction losses and adjusts calibration quantile thresholds via weighted exchangeability, maintaining coverage with smaller prediction sets on ImageNet variants.\n\n---\n\n**10. Coverage Guarantees for Pseudo-Calibrated Conformal Prediction under Distribution Shift**\n- **Authors:** Farbod Siahkali, Ashwin Verma, Vijay Gupta\n- **Venue:** arXiv preprint (February 2026)\n- **URL:** https://arxiv.org/abs/2602.14913\n- **Why important:** Provides coverage lower bounds under label-conditional covariate shift using domain adaptation and Wasserstein shift measures, with a source-tuned pseudo-calibration approach.\n- **One-line summary:** Establishes target coverage lower bounds for pseudo-calibrated conformal prediction under label-conditional covariate shift using domain adaptation techniques and Wasserstein shift measures.\n\n---\n\n### CATEGORY C: Adaptive / Online Conformal Inference under Distribution Shift\n\n---\n\n**11. Online Conformal Inference with Retrospective Adjustment for Faster Adaptation to Distribution Shift**\n- **Authors:** Jungbin Jun, Ilsang Ohn\n- **Venue:** arXiv preprint (November 2025)\n- **URL:** https://arxiv.org/abs/2511.04275\n- **Why important:** Introduces retrospective adjustment to online conformal prediction, retroactively updating past predictions when new data arrives for faster adaptation to distribution shift.\n- **One-line summary:** Achieves faster coverage recalibration in online conformal prediction by retroactively adjusting past predictions using efficient leave-one-out update formulas when new data arrives.\n\n---\n\n**12. CORE: Conformal Regression under Distribution Shift via Reinforcement Learning**\n- **Authors:** Yilei Zhao, Wentao Zhang, Miguel R. Pebes-Trujillo, Junxian Liu, Hongxin Wei, Wei Yang Bryan Lim\n- **Venue:** ICLR 2026\n- **URL:** https://openreview.net/forum?id=7puF5JOkKk\n- **Why important:** Creates a mutual feedback loop between RL and conformal prediction for time-series forecasting, using RL exploration to better cover uncertain/outlier regions under distribution shift.\n- **One-line summary:** Integrates reinforcement learning with conformal prediction to dynamically adapt prediction intervals under distribution shift in time-series, improving coverage by 1.36% and reducing interval length by 5.03%.\n\n---\n\n**13. Conformal Prediction under Levy-Prokhorov Distribution Shifts**\n- **Authors:** Liviu Aolaritei, Zheyu Oliver Wang, Julie Zhu, Michael I. Jordan, Youssef Marzouk\n- **Venue:** arXiv preprint (February 2025)\n- **URL:** https://arxiv.org/abs/2502.14105\n- **Why important:** Models distribution shifts using Levy-Prokhorov ambiguity sets (capturing both local and global perturbations), reducing high-dimensional shifts to manageable 1D shifts through the scoring function.\n- **One-line summary:** Reduces complex high-dimensional distribution shifts to 1D via LP ambiguity sets routed through the scoring function, enabling tractable worst-case quantile and coverage computations.\n\n---\n\n**14. Adapting Prediction Sets to Distribution Shifts Without Labels (ECP/EACP)**\n- **Authors:** Kevin Kasa, Zhiyu Zhang, Heng Yang, Graham W. Taylor\n- **Venue:** arXiv preprint (June 2024)\n- **URL:** https://arxiv.org/abs/2406.01416\n- **Why important:** Adapts conformal prediction sets at test time using only the base model's own uncertainty evaluation, requiring no labeled test data -- nearly matching fully supervised adaptation.\n- **One-line summary:** Adjusts conformal score functions using the base model's uncertainty estimates to adapt prediction sets to distribution shifts without any labeled test data.\n\n---\n\n**15. Test-time Recalibration of Conformal Predictors Under Distribution Shift Based on Unlabeled Examples**\n- **Authors:** Fatih Furkan Yilmaz, Reinhard Heckel\n- **Venue:** ICLR 2023\n- **URL:** https://arxiv.org/abs/2210.04166\n- **Why important:** Foundational work on test-time recalibration using only unlabeled examples from the shifted distribution; provides theoretical guarantees for specific shift models.\n- **One-line summary:** Recalibrates conformal prediction thresholds at test time using only unlabeled examples from a shifted distribution, achieving reliable uncertainty estimates under natural distribution shifts.\n\n---\n\n### CATEGORY D: Partition, Voting, and Aggregation in Conformal Prediction\n\n---\n\n**16. Merging Uncertainty Sets via Majority Vote**\n- **Authors:** Matteo Gasparin, Aaditya Ramdas\n- **Venue:** arXiv preprint (January 2024)\n- **URL:** https://arxiv.org/abs/2401.09379\n- **Why important:** Directly addresses the partition-and-vote paradigm: merges K prediction sets (from different estimators or conformal methods) via majority voting with provable coverage guarantees, plus weighted and randomized extensions.\n- **One-line summary:** Combines K uncertainty sets (confidence intervals, conformal prediction sets) via a majority vote procedure maintaining error guarantees, with extensions for weighted averaging and randomized set-size reduction.\n\n---\n\n**17. Conformal Online Model Aggregation (COMA)**\n- **Authors:** Matteo Gasparin, Aaditya Ramdas\n- **Venue:** arXiv preprint (March 2024)\n- **URL:** https://arxiv.org/abs/2403.15527\n- **Why important:** Proposes online aggregation of conformal prediction sets from multiple black-box models via adaptive weighted voting, maintaining coverage under distribution drift -- highly relevant to partition-and-vote robustness.\n- **One-line summary:** Aggregates conformal prediction sets from multiple models via online weighted voting with adaptive weights, maintaining coverage guarantees even under distribution drift.\n\n---\n\n**18. Valid Selection among Conformal Sets**\n- **Authors:** Mahmoud Hegazy, Liviu Aolaritei, Michael I. Jordan, Aymeric Dieuleveut\n- **Venue:** arXiv preprint (June 2025)\n- **URL:** https://arxiv.org/abs/2506.20173\n- **Why important:** Addresses the invalidation problem when selecting the best (e.g., smallest) among multiple valid conformal sets; proposes a stability-based approach preserving coverage after selection.\n- **One-line summary:** Provides a stability-based method ensuring that selecting the most desirable prediction set from multiple valid conformal sets does not invalidate coverage guarantees.\n\n---\n\n**19. Multi-Distribution Robust Conformal Prediction**\n- **Authors:** Yuqi Yang, Ying Jin\n- **Venue:** arXiv preprint (January 2026)\n- **URL:** https://arxiv.org/abs/2601.02998\n- **Why important:** Constructs prediction sets with finite-sample coverage guarantees uniformly valid across multiple heterogeneous source distributions, with a provably optimal max-p aggregation scheme.\n- **One-line summary:** A max-p aggregation scheme for constructing conformal prediction sets with provably optimal multi-distribution coverage guarantees, connecting to distributionally robust optimization and fairness.\n\n---\n\n**20. Partition Learning Conformal Prediction (PLCP)**\n- **Authors:** Shayan Kiyani, George Pappas, Hamed Hassani\n- **Venue:** arXiv preprint (April 2024)\n- **URL:** https://arxiv.org/abs/2404.17487\n- **Why important:** Learns uncertainty-guided partitions from calibration data to improve conditional coverage validity, directly relevant to partition-based conformal prediction.\n- **One-line summary:** Learns partitions from calibration data via alternating gradient descent to improve conditional coverage of conformal prediction sets, with finite-sample conditional guarantees.\n\n---\n\n**21. Split Conformal Prediction under Data Contamination**\n- **Authors:** Jase Clarkson, Wenkai Xu, Mihai Cucuringu, Yvik Swan, Gesine Reinert\n- **Venue:** arXiv preprint (July 2024)\n- **URL:** https://arxiv.org/abs/2407.07700\n- **Why important:** Quantifies how contaminated calibration data affects conformal coverage and proposes Contamination Robust Conformal Prediction, relevant to robustness when calibration and test distributions differ.\n- **One-line summary:** Quantifies the effect of calibration data contamination on split conformal prediction and proposes a classification-specific robust correction method.\n\n---\n\n### CATEGORY E: Conformal Prediction + RAG / Retrieval-Augmented Generation\n\n---\n\n**22. URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models**\n- **Authors:** Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang\n- **Venue:** arXiv preprint (March 2026)\n- **URL:** https://arxiv.org/abs/2603.19281\n- **Why important:** First comprehensive benchmark for UQ in RAG systems using conformal prediction (LAC, APS metrics), covering healthcare, programming, math, and general text domains.\n- **One-line summary:** Converts RAG open-ended generation to multiple-choice format to enable conformal prediction-based UQ evaluation, finding that retrieval errors can amplify confident hallucinations.\n\n---\n\n**23. CONFLARE: CONFormal LArge language model REtrieval**\n- **Authors:** Pouria Rouzrokh, Shahriar Faghani, Cooper U. Gamble, Moein Shariatnia, Bradley J. Erickson\n- **Venue:** arXiv preprint (April 2024)\n- **URL:** https://arxiv.org/abs/2404.04287\n- **Why important:** Applies conformal prediction directly to the retrieval step of RAG, establishing thresholds on retrieval similarity scores to guarantee the true answer is captured in context with (1-alpha) confidence.\n- **One-line summary:** A four-step conformal prediction framework for RAG retrieval that sets similarity-score thresholds ensuring retrieved context contains the true answer with user-specified confidence.\n\n---\n\n**24. Conformal-RAG: Response Quality Assessment for Retrieval-Augmented Generation via Conditional Conformal Factuality**\n- **Authors:** Naihe Feng, Yi Sui, Shiyi Hou, Jesse C. Cresswell, Ga Wu\n- **Venue:** arXiv preprint (June 2025)\n- **URL:** https://arxiv.org/abs/2506.20978\n- **Why important:** Combines conformal prediction with RAG to ensure group-conditional coverage across sub-domains without manual labeling, retaining up to 60% more high-quality sub-claims.\n- **One-line summary:** Leverages conformal prediction for group-conditional factuality guarantees in RAG, retaining 60% more high-quality sub-claims than direct CP application while maintaining reliability.\n\n---\n\n**25. Uncertainty Quantification for Retrieval-Augmented Reasoning (R2C)**\n- **Authors:** Heydar Soudani, Hamed Zamani, Faegheh Hasibi\n- **Venue:** arXiv preprint (October 2025)\n- **URL:** https://arxiv.org/abs/2510.11483\n- **Why important:** Proposes UQ for retrieval-augmented reasoning by perturbing multi-step reasoning processes, achieving 5%+ AUROC gains for abstention decisions.\n- **One-line summary:** Quantifies uncertainty in retrieval-augmented reasoning by perturbing reasoning steps across both retrieval and generation, enabling better abstention and model selection.\n\n---\n\n**26. Eliminating Hallucination-Induced Errors in LLM Code Generation with Functional Clustering**\n- **Authors:** Chaitanya Ravuri, Saman Amarasinghe\n- **Venue:** arXiv preprint (June 2025)\n- **URL:** https://arxiv.org/abs/2506.11021\n- **Why important:** While not strictly conformal prediction, uses a voting/clustering approach (functional clustering of sampled programs) that mirrors partition-and-vote ideas for selective prediction in code generation.\n- **One-line summary:** Samples multiple candidate programs, clusters by input-output behavior, and uses the largest cluster's mass as a confidence score, reducing code generation error rates from 65% to 2%.\n\n---\n\n### Summary of Key Themes\n\n1. **Density ratio reweighting for LLM conformal prediction** -- CoFact (ICLR 2026) and DS-CP directly tackle covariate shift for language models, with CoFact using online density ratio estimation and DS-CP using proximity-based reweighting to avoid the curse of dimensionality.\n\n2. **Wasserstein and LP-based distribution shift bounds** -- WR-CP and the Levy-Prokhorov paper provide tighter theoretical bounds than total variation for coverage gap analysis under general shift.\n\n3. **Majority vote / aggregation of conformal sets** -- Gasparin & Ramdas (2024) provide the canonical majority vote merging procedure; COMA extends it to online settings with adaptive weights under drift; Yang & Jin (2026) address multi-distribution robustness with a max-p scheme.\n\n4. **Partition-based conditional coverage** -- PLCP learns uncertainty-guided partitions to improve conditional validity; Group-Weighted CP exploits group structure for tighter guarantees.\n\n5. **Online / adaptive methods** -- Retrospective adjustment (Jun & Ohn, 2025) and CORE (ICLR 2026) push beyond forward-only adaptation, using leave-one-out updates and RL feedback loops respectively.\n\n6. **Conformal abstention for LLMs** -- The NeurIPS 2024 conformal abstention paper and its RL-enhanced successor (Tayebati et al., 2025) provide principled selective prediction for hallucination mitigation.\n\n7. **Conformal prediction for RAG** -- CONFLARE, Conformal-RAG, URAG, and R2C represent an emerging body of work applying conformal guarantees to retrieval quality, response factuality, and reasoning uncertainty in RAG pipelines."
      }
    ],
    "totalDurationMs": 219014,
    "totalTokens": 33510,
    "totalToolUseCount": 40,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 27497,
      "output_tokens": 5309,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 703
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5309,
          "cache_read_input_tokens": 27497,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 703,
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
      "otherToolCount": 40
    }
  },
  "sourceToolAssistantUUID": "a089076b-e133-495f-96bd-df068d113d28",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39 · 2026-05-30T06:21:06.227Z_

```json
{
  "parentUuid": "4fc9a70a-a931-4ed2-b127-8e8eef5bf5e4",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "f3adfd11-407a-4b2b-ab28-885c9c6137b6",
  "timestamp": "2026-05-30T06:21:06.227Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "f3adfd11-407a-4b2b-ab28-885c9c6137b6",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on conformal prediction for RAG",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Assistant

_source line 42 · 2026-05-30T06:23:12.138Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive results from all seven search agents. Let me synthesize the findings and select the 15 most important papers for this specific research direction on conformal-prediction-based abstention for RAG under corpus poisoning.

Let me carefully curate the final list based on:
1. Direct relevance to the research direction (conformal prediction + RAG + adversarial/poisoning)
2. Importance (best paper awards, oral/spotlight, high citations, foundational methods)
3. Recency (2024-2026)

The key areas to cover:


- Conformal prediction methods applied to RAG systems
- Robust conformal prediction techniques that handle poisoning and distribution shift
- Corpus poisoning attacks and certified defenses for RAG
- Conformal factuality and abstention mechanisms for language models
- Partition and voting-based approaches for reliable predictions

Now I'm identifying the 15 most relevant papers to focus on, excluding the 6 seed papers I already know well. Starting with PoisonedRAG as a foundational attack paper that establishes the threat model for RAG systems. I'm continuing through the key papers on conformal prediction for LLMs, noting foundational work on attacks against CP systems, robustness under distribution shifts, and specific applications to RAG-based architectures and factuality guarantees.

Now I'm reconsidering whether the Chen et al. ICLR 2026 paper on conformal factuality might overlap with or extend from the seed paper I'm building on. I'm seeing that the arXiv version and ICLR 2026 version are the same paper, so I'll skip it since it's already in the seed set. Now I'm weighing several other candidates like the ECIR 2026 paper on context engineering for RAG, the foundational conformal language modeling work, RAGDefender which outperforms existing defenses, and a few others covering risk-averse conformal prediction and distribution shift handling.

I'm narrowing down to my final 15 papers, starting with PoisonedRAG as the attack threat model, the NeurIPS 2024 work on conformal abstention for hallucinations, and the foundational conformal factuality guarantees paper. Looking at the most impactful recent work, I'm noticing that the papers on conformal prediction as Bayesian quadrature and decision-theoretic foundations are particularly strong, but I need to focus on what directly addresses the core challenge: making conformal prediction robust against poisoned RAG systems. The key papers I should prioritize are those combining conformal methods with RAG systems, the poisoning attack frameworks, and certified defense mechanisms—these form the technical backbone for the research direction. I'm identifying the most directly relevant papers on poisoning attacks against conformal prediction, theoretical frameworks for robustness under distribution shifts, and methodologies for combining uncertainty estimates through voting—all of which apply to building defenses for RAG systems against adversarial data corruption.

I should also factor in papers on conformal prediction applied specifically to NLP and language generation, adaptive abstention policies, and domain-shift robustness for LLMs, plus some practical baselines like RAGDefender and approaches for filtering RAG context using conformal methods.

Now I'm thinking through what a reviewer would actually expect to see—the foundational attack papers that define the problem, the core conformal prediction work for factuality and abstention, recent advances in handling distribution shift and poisoning attacks, and the key theoretical frameworks that tie everything together.

I should also check whether to include that Barber et al. paper on conformal prediction beyond exchangeability, since it might be relevant to the theoretical grounding here.  Actually, it's from 2023, so it falls outside the 2024-2026 window the user specified. I'll note it but keep it separate.

Looking back at my selections, I'm realizing Conformal Language Modeling from ICLR 2024 is pretty foundational for how conformal prediction applies to open-ended text generation, so that should definitely make the cut. ConU from EMNLP 2024 is also worth considering for its self-consistency approach to uncertainty.

Let me finalize the list and move toward the JSON output. Looking at the papers I've listed so far, I'm realizing I need to focus more directly on what the user actually needs—conformal prediction specifically applied to RAG systems under corpus poisoning threats. The papers I'm considering for slots 12-15 should center on that intersection rather than broader conformal prediction topics. Let me reconsider which papers are most relevant to retrieval-augmented generation with poisoning robustness and abstention mechanisms. I'm refining the list to focus on the most directly relevant papers—prioritizing attack baselines like PoisonedRAG and CorruptRAG, foundational conformal factuality work, and recent advances in conformal prediction robustness under poisoning and distribution shift. I'm reconsidering whether RAGDefender should replace the split conformal prediction paper since it directly compares against RobustRAG and offers practical defense benchmarks. Principled Context Engineering for RAG is also compelling since it applies conformal prediction to RAG context filtering. Let me think through what the final 15 papers should prioritize—covering the threat model, practical defenses, and theoretical foundations. I'm reconsidering whether the Bayesian Quadrature paper is essential here—it's foundational work on conformal prediction but might be tangential to the poisoning and RAG focus. Still, it demonstrates awareness of recent CP advances and provides theoretical grounding, so I'll include it. Now I'm compiling the final fifteen papers with verified URLs and details, starting with PoisonedRAG and CorruptRAG as the core poisoning attack papers. Continuing through more recent work on conformal prediction applied to language models, including approaches for handling distribution shifts, uncertainty set merging, and robustness certification in NLP tasks. I'm reconsidering that last paper on data contamination—there are several other options that might be more directly applicable. "Understanding Data Poisoning Attacks for RAG" from ICLR 2025 seems particularly relevant for explaining the theoretical foundations of why poisoning attacks work in retrieval-augmented systems. I'm going to include "Understanding Data Poisoning Attacks for RAG" instead since it directly tackles the RAG poisoning problem at a top venue and provides the theoretical foundation I need, making it more relevant than the general conformal prediction contamination paper. I'm debating whether to include Conformal-RAG since it directly addresses CP for assessing RAG sub-claim factuality at a top venue, but the current list already feels comprehensive. Let me stick with the 15 papers I have and add a few bonus entries since the user values relevant additions—Conformal-RAG, RAGDefender, and a couple others would round out the coverage nicely.

Now I'm finalizing the compilation, aiming for around 18-20 papers total with the core 15 plus select bonus entries that genuinely strengthen the collection. I'm adding a few more relevant papers to the list, then settling on the twentieth one to proceed with compiling the JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3adfd11-407a-4b2b-ab28-885c9c6137b6",
  "isSidechain": false,
  "requestId": "req_011CbYGeA8ZgvT4G1FRQELMM",
  "type": "assistant",
  "uuid": "77f1dcc8-c4bf-45dc-8502-665477fe6d61",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MecofP2nRUZCY8vhsk4s31",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10902,
      "cache_read_input_tokens": 38987,
      "output_tokens": 12396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10902,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 12396,
          "cache_read_input_tokens": 38987,
          "cache_creation_input_tokens": 10902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10902
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

_source line 43 · 2026-05-30T06:24:44.493Z_

Now I have comprehensive results from all seven search agents. Let me synthesize everything into the final curated list of the most important papers. I need to carefully select and verify each paper, excluding the 6 seed papers already known.

Here is my analysis and the final output:

---

## Literature Survey Summary

I searched across 7 parallel agent threads covering: (1) conformal prediction for RAG, (2) robust CP under poisoning/distribution shift, (3) RAG corpus poisoning attacks & defenses, (4) selective prediction & abstention for LLMs, (5) best paper awards at top venues, (6) seed paper citation networks, and (7) CP under distribution shift for NLP. Below are the **20 most important papers** (2024–2026), ranked by direct relevance to the proposed research direction: conformal-prediction-based abstention for RAG under adversarial corpus poisoning.

**Selection criteria applied:**
- Direct relevance to the intersection of {conformal prediction, RAG, adversarial poisoning, abstention}
- Venue prestige and recognition (best paper, oral, spotlight)
- Theoretical or methodological novelty that the proposed work builds upon
- Papers that define evaluation protocols, threat models, or baselines the proposed work must engage with

All 6 seed papers (TRAQ, RPS, RobustRAG, Chen et al. 2026, C-RAG, ReliabilityRAG) are **excluded** from the list below.

---

```json
[
  {
    "title": "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models",
    "authors": "Wei Zou, Runpeng Geng, Binghui Wang, Jinyuan Jia",
    "venue": "USENIX Security 2025",
    "url": "https://arxiv.org/abs/2402.07867",
    "why_important": "Foundational attack paper defining the corpus poisoning threat model for RAG; achieves 90% ASR by injecting only 5 malicious texts into a database of millions. Required evaluation protocol for the proposed work.",
    "one_line_summary": "Formulates corpus poisoning of RAG as an optimization problem with black-box and white-box variants, demonstrating that a small number of adversarial passages reliably steer LLM outputs to attacker-chosen answers."
  },
  {
    "title": "CorruptRAG: Practical Poisoning Attacks against Retrieval-Augmented Generation",
    "authors": "Baolei Zhang, Yuxi Chen, Zhuqing Liu, Lihai Nie, Tong Li, Zheli Liu, Minghong Fang",
    "venue": "ACM SACMAT 2026",
    "url": "https://arxiv.org/abs/2504.03957",
    "why_important": "Advances attack practicality to single-document poisoning (vs. 5 in PoisonedRAG), making attacks stealthier. Explicitly listed as an evaluation protocol in the proposed work's constraints.",
    "one_line_summary": "A practical single-document poisoning attack against RAG that achieves higher attack success rates than PoisonedRAG while being harder to detect."
  },
  {
    "title": "Mitigating LLM Hallucinations via Conformal Abstention",
    "authors": "Yasin Abbasi-Yadkori, Ilja Kuzborskij, David Stutz, Andras Gyorgy, Adam Fisch, Arnaud Doucet, Iuliya Beloshapka, Wei-Hung Weng, Yao-Yuan Yang, Csaba Szepesvari, Ali Taylan Cemgil, Nenad Tomasev",
    "venue": "NeurIPS 2024",
    "url": "https://arxiv.org/abs/2405.01563",
    "why_important": "Foundational work from Google DeepMind on conformal abstention for LLMs; uses self-consistency-based similarity scoring with CP to bound hallucination rates. Directly establishes the conformal abstention paradigm the proposed work extends to adversarial settings.",
    "one_line_summary": "Uses self-consistency-based nonconformity scores with conformal prediction to provide distribution-free statistical upper bounds on LLM hallucination rates, determining when to abstain from answering."
  },
  {
    "title": "Language Models with Conformal Factuality Guarantees",
    "authors": "Christopher Mohri, Tatsunori Hashimoto",
    "venue": "arXiv 2024 (Stanford)",
    "url": "https://arxiv.org/abs/2402.10978",
    "why_important": "Seminal paper defining 'conformal factuality' — the back-off algorithm that makes LLM outputs progressively less specific until correctness is guaranteed. Most subsequent CP+LLM papers build on this framework.",
    "one_line_summary": "Introduces conformal factuality with a back-off mechanism that progressively generalizes LLM responses to expand prediction sets until a user-specified correctness guarantee is met."
  },
  {
    "title": "CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift",
    "authors": "Zirui Hu, Zheng Zhang, Yingjie Wang, Leszek Rutkowski, Dacheng Tao",
    "venue": "ICLR 2026",
    "url": "https://openreview.net/forum?id=eiBp7rsc3K",
    "why_important": "Most directly relevant theoretical tool: uses online density ratio estimation to reweight calibration data for conformal factuality under covariate shift, removing the exchangeability assumption between calibration and test data. Corpus poisoning induces precisely this type of shift.",
    "one_line_summary": "Applies online density ratio estimation to adaptively reweight conformal calibration data, maintaining factuality guarantees for LLMs under non-stationary covariate shift."
  },
  {
    "title": "Data Poisoning Attacks against Conformal Prediction",
    "authors": "Yangyi Li, Aobo Chen, Wei Qian, Chenxu Zhao, Divya Lidder, Mengdi Huai",
    "venue": "ICML 2024",
    "url": "https://proceedings.mlr.press/v235/li24l.html",
    "why_important": "Defines the threat model for adversarial manipulation of conformal prediction itself; shows attackers can make prediction sets vacuously large or dangerously small via poisoning. Establishes that CP is not inherently robust — motivating defensive approaches like the proposed work.",
    "one_line_summary": "Introduces the first black-box poisoning attacks that directly manipulate conformal prediction set sizes (inflation or shrinkage) rather than targeting classification accuracy."
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
    "title": "Conformal Prediction under Levy-Prokhorov Distribution Shifts: Robustness to Local and Global Perturbations",
    "authors": "Liviu Aolaritei, Qianyu Julie Zhu, Zheyu Oliver Wang, Michael I. Jordan, Youssef Marzouk",
    "venue": "NeurIPS 2025",
    "url": "https://arxiv.org/abs/2502.14105",
    "why_important": "Provides a principled mathematical framework for robust CP under distribution shift using Levy-Prokhorov ambiguity sets that unify local (adversarial) and global (covariate) perturbations. The reduction from high-dimensional shifts to 1D via the scoring function is directly applicable to retrieval-agreement scores.",
    "one_line_summary": "Models distribution shifts via Levy-Prokhorov ambiguity sets and reduces high-dimensional distributional robustness to one-dimensional quantile computations through the conformal scoring function."
  },
  {
    "title": "Merging Uncertainty Sets via Majority Vote",
    "authors": "Matteo Gasparin, Aaditya Ramdas",
    "venue": "arXiv 2024",
    "url": "https://arxiv.org/abs/2401.09379",
    "why_important": "Directly relevant methodological inspiration: formalizes the partition-and-vote paradigm for merging K prediction sets with provable coverage guarantees. The proposed work's retrieval-agreement groups and group-conditional scoring are analogous to this majority-vote aggregation framework.",
    "one_line_summary": "Combines K uncertainty sets (from different models or conformal splits) via a majority voting procedure that maintains provable error rate control, with extensions for weighted and randomized voting."
  },
  {
    "title": "Conformal Prediction for Natural Language Processing: A Survey",
    "authors": "Margarida M. Campos, Antonio Farinhas, Chrysoula Zerva, Mario A.T. Figueiredo, Andre F.T. Martins",
    "venue": "TACL 2025",
    "url": "https://arxiv.org/abs/2405.01976",
    "why_important": "Most comprehensive survey of CP techniques applied to NLP; catalogs guarantees, existing applications, and open challenges including distribution shift and adversarial robustness. Essential reference for positioning the proposed work.",
    "one_line_summary": "A thorough survey cataloging conformal prediction methods, their statistical guarantees, and applications across NLP tasks, identifying distribution shift and adversarial robustness as key open challenges."
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
    "title": "Conformal Prediction as Bayesian Quadrature",
    "authors": "Jake C. Snell, Thomas L. Griffiths",
    "venue": "ICML 2025 (Outstanding Paper Award)",
    "url": "https://arxiv.org/abs/2502.13228",
    "why_important": "Won ICML 2025 Outstanding Paper Award (1 of 6). Reframes frequentist CP through a Bayesian lens, providing richer representation of test-time loss distributions. Foundational advance in CP theory relevant to designing better nonconformity scores.",
    "one_line_summary": "Reinterprets conformal prediction as Bayesian quadrature, yielding more interpretable guarantees and a richer characterization of the likely range of test-time losses for high-stakes deployment."
  },
  {
    "title": "URAG: A Benchmark for Uncertainty Quantification in Retrieval-Augmented Large Language Models",
    "authors": "Vinh Nguyen, Cuong Dang, Jiahao Zhang, Hoa Tran, Minh Tran, Trinh Chau, Thai Le, Lu Cheng, Suhang Wang",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2603.19281",
    "why_important": "First comprehensive benchmark for UQ in RAG systems; evaluates 8 RAG methods using conformal prediction (LAC, APS) and reveals that retrieval errors amplify confident hallucinations. Provides evaluation infrastructure the proposed work should use.",
    "one_line_summary": "Comprehensive benchmark evaluating uncertainty quantification across 8 RAG methods using conformal prediction, finding that accuracy-uncertainty correlation breaks under retrieval errors."
  },
  {
    "title": "Learning Conformal Abstention Policies for Adaptive Risk Management in Large Language and Vision-Language Models",
    "authors": "Sina Tayebati, Divake Kumar, Nastaran Darabi, Dinithi Jayasuriya, Ranganath Krishnan, Amit Ranjan Trivedi",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2502.06884",
    "why_important": "Extends conformal abstention from static thresholds to RL-learned adaptive policies; achieves 22% AUROC improvement in hallucination detection and 70-85% calibration error reduction. Directly relevant to designing tunable coverage-abstention tradeoffs.",
    "one_line_summary": "Uses reinforcement learning to dynamically optimize conformal abstention thresholds for LLMs, enabling adaptive coverage-abstention tradeoffs that outperform fixed-threshold approaches."
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
    "title": "Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction",
    "authors": "Debashish Chakraborty, Eugene Yang, Daniel Khashabi, Dawn Lawrie, Kevin Duh",
    "venue": "ECIR 2026",
    "url": "https://arxiv.org/abs/2511.17908",
    "why_important": "Directly extends TRAQ by using conformal prediction for coverage-controlled context filtering in RAG; reduces context by 2-3x while maintaining coverage guarantees. Explicitly identifies relaxing exchangeability as open future work.",
    "one_line_summary": "Applies conformal prediction to filter retrieved context in RAG with statistical guarantees that a target fraction of relevant snippets are retained, improving factual accuracy by removing noise."
  },
  {
    "title": "RAGDefender: Rescuing the Unpoisoned — Efficient Defense against Knowledge Corruption Attacks on RAG Systems",
    "authors": "Minseok Kim, Hankook Lee, Hyungjoon Koo",
    "venue": "ACSAC 2025",
    "url": "https://arxiv.org/abs/2511.01268",
    "why_important": "Lightweight post-retrieval defense that outperforms RobustRAG, especially when poisoned passages outnumber clean ones. Directly benchmarks against both PoisonedRAG attacks and RobustRAG defense — a key comparison baseline.",
    "one_line_summary": "Identifies and removes poisoned content during post-retrieval processing without extra training, reducing PoisonedRAG attack success from 0.89 to 0.02 on Gemini."
  },
  {
    "title": "Domain-Shift-Aware Conformal Prediction for Large Language Models",
    "authors": "Zhexiao Lin, Yuanyuan Li, Neeraj Sarna, Yuanyuan Gao, Michael von Gablenz",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2510.05566",
    "why_important": "Addresses exchangeability violations in CP for LLMs by proximity-based reweighting of calibration samples; avoids infeasible density ratio estimation in high dimensions. Practical technique for maintaining conformal coverage under the distribution shift induced by retrieval corruption.",
    "one_line_summary": "Reweights conformal calibration samples by proximity to the test prompt to maintain valid coverage under domain shift for LLMs, circumventing density ratio estimation in high dimensions."
  },
  {
    "title": "GASLITEing the Retrieval: Exploring Vulnerabilities in Dense Embedding-based Search",
    "authors": "Matan Ben-Tov, Mahmood Sharif",
    "venue": "ACM CCS 2025",
    "url": "https://arxiv.org/abs/2412.20953",
    "why_important": "Published at a top security venue; demonstrates that dense retrieval is catastrophically vulnerable even at 0.0001% corpus poisoning. Shows that even minimal adversarial insertion fundamentally disrupts retrieval — supporting the argument that retrieval-level defenses alone are insufficient and abstention mechanisms are needed.",
    "one_line_summary": "Generates adversarial passages without model or corpus knowledge that achieve high rankings in dense retrieval; single-query attacks are 100% successful and standard defenses fail against adaptive versions."
  },
  {
    "title": "Split Conformal Prediction under Data Contamination",
    "authors": "Jase Clarkson, Wenkai Xu, Mihai Cucuringu, Yvik Swan, Gesine Reinert",
    "venue": "arXiv 2024",
    "url": "https://arxiv.org/abs/2407.07700",
    "why_important": "Directly quantifies how contaminated calibration data (analogous to poisoned retrieval) affects conformal coverage and proposes correction methods. Provides theoretical tools for understanding coverage degradation under the data contamination induced by corpus poisoning.",
    "one_line_summary": "Quantifies the effect of calibration data contamination on split conformal prediction coverage and proposes contamination-robust correction methods to restore target coverage."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77f1dcc8-c4bf-45dc-8502-665477fe6d61",
  "isSidechain": false,
  "requestId": "req_011CbYGeA8ZgvT4G1FRQELMM",
  "type": "assistant",
  "uuid": "3a285498-e441-4853-96df-7e131ea516f1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MecofP2nRUZCY8vhsk4s31",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10902,
      "cache_read_input_tokens": 38987,
      "output_tokens": 12396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10902,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 12396,
          "cache_read_input_tokens": 38987,
          "cache_creation_input_tokens": 10902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10902
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "3a285498-e441-4853-96df-7e131ea516f1",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on conformal prediction for RAG",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "3a285498-e441-4853-96df-7e131ea516f1",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on conformal prediction for RAG",
  "sessionId": "41901ced-6b17-4e52-97f2-1983f67919e2"
}
```

---
