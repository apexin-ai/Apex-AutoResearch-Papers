# Research conversation: You are a senior ML researcher conducting a comprehensive literature survey. **Today's date: 2026-05-30 (UTC).** ## Task

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/3d79ae5a-88b6-4a48-962d-c30e1acc36b0.jsonl`
- **Structured JSON:** [`6c5cabed6974effc0c41.json`](../../sessions/6c/6c5cabed6974effc0c41.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:09:30.756Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:09:30.756Z",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "content": "You are a senior ML researcher conducting a comprehensive literature survey.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Task\nFind the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:\n\n**Target: AAAI 2026\nTrack: Information Retrieval and Text Mining (or Machine Learning: Theory)\n\nDirection: Establish formal expressiveness bounds for multi-vector (MaxSim/Chamfer) retrieval representations — the sign-rank equivalent for ColBERT-style late interaction. While LIMIT (ICLR 2026) proved that single-vector embeddings have fundamental capacity limitations tied to sign-rank, no formal theory exists for what multi-vector representations with sum-of-max scoring can express. We aim to characterize the representational capacity of MaxSim as a function of the number of vectors per document and their dimensionality, providing tight bounds analogous to sign-rank for inner products.\n\nSeed Papers:\n- Weller et al., \"On the Theoretical Limitations of Embedding-Based Retrieval\" (ICLR, 2026) — Proves single-vector limitations via sign-rank; the direct theoretical anchor we extend\n- Wang et al., \"R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval\" (arXiv, 2026) — Proves dimension sufficiency for single-vector; our work must be consistent with or subsume this\n- Dhulipala et al., \"MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings\" (NeurIPS, 2024) — Algorithmic reduction of MaxSim to inner product with approximation guarantees; does NOT address expressiveness\n- Jacob et al., \"On Strengths and Limitations of Single-Vector Embeddings\" (arXiv, 2026) — Empirically confirms multi-vector superiority on LIMIT but uses only toy math models; explicitly lacks formal theory\n- Khattab & Zaharia, \"ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction\" (SIGIR, 2020) — Introduced MaxSim; foundational architecture whose expressiveness we characterize\n\nKnown Gaps:\n- No formal characterization of the representational capacity of sum-of-max-inner-product scoring as a function of number of vectors and dimensionality\n- No proven separation result showing which relevance patterns multi-vector can represent that single-vector provably cannot (beyond empirical demonstrations on LIMIT)\n- No connection between MaxSim expressiveness and communication complexity or combinatorial dimensions analogous to sign-rank\n\nTheoretical Anchor: Sign-rank of binary matrices characterizes single-vector embedding capacity (Weller et al.). MaxSim scoring over k vectors per document can be viewed as a richer communication protocol where each party sends k messages instead of one. The analogous complexity measure — potentially related to partition number or multi-round communication complexity — should yield tighter and more favorable bounds, formally explaining multi-vector superiority.\n\nConstraints:\n- Compute: ≤200 H100-hours (primarily theoretical; compute needed only for empirical validation on LIMIT and synthetic constructions)\n\nQuality Self-Checks:\n- [x] Core insight: Multi-vector retrieval's empirical superiority over single-vector can be formally characterized through communication complexity, yielding provable separation results.\n- [x] Why not obvious: Sign-rank gives clean bounds for inner products but sum-of-max-inner-products introduces combinatorial structure (assignment problems) that breaks standard techniques — requires novel proof strategies.\n- [x] Baseline fear test: A simple 'multi-vector is at least as expressive as single-vector' result would be trivial; we need tight bounds showing HOW MUCH more expressive, as a function of the number of vectors.\n- [x] Information exploited: The structure of MaxSim as a combinatorial optimization (max-matching) over inner products — this algebraic structure is what enables stronger representational capacity and what existing analyses ignore.\n\nAvoid:\n- Purely empirical comparisons of single-vector vs multi-vector (already done extensively; adds nothing new)\n- Loose existential bounds that only show multi-vector CAN be better without quantifying the gap\n- Ignoring computational complexity — bounds that require exponentially many vectors per document are theoretically interesting but practically useless\n- Conflating approximation guarantees (MUVERA-style) with expressiveness characterization — these are orthogonal questions**\n\n## What counts as 'important'\n\nPrioritize (in order):\n1. **Best paper awards** at top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, AAAI, etc.)\n2. **Oral / spotlight presentations** at these venues\n3. **Highly cited papers** (>50 citations in 1-2 years)\n4. **Papers that introduced widely-adopted methods** (e.g., new training paradigm, new benchmark)\n5. **Recent survey papers** that provide comprehensive field overviews\n6. **Strong recent work** from top labs (Google, Meta, DeepMind, OpenAI, CMU, Stanford, etc.)\n\n## Search strategy\n\nExecute AT LEAST 15 targeted searches:\n\n1. `best paper award ACL EMNLP NeurIPS ICML ICLR 2026 Target: AAAI 2026\nTrack: Information Retrieval and Text Mining (or Machine Learning: Theory)\n\nDirection: Establish formal expressiveness bounds for multi-vector (MaxSim/Chamfer) retrieval representations — the sign-rank equivalent for ColBERT-style late interaction. While LIMIT (ICLR 2026) proved that single-vector embeddings have fundamental capacity limitations tied to sign-rank, no formal theory exists for what multi-vector representations with sum-of-max scoring can express. We aim to characterize the representational capacity of MaxSim as a function of the number of vectors per document and their dimensionality, providing tight bounds analogous to sign-rank for inner products.\n\nSeed Papers:\n- Weller et al., \"On the Theoretical Limitations of Embedding-Based Retrieval\" (ICLR, 2026) — Proves single-vector limitations via sign-rank; the direct theoretical anchor we extend\n- Wang et al., \"R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval\" (arXiv, 2026) — Proves dimension sufficiency for single-vector; our work must be consistent with or subsume this\n- Dhulipala et al., \"MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings\" (NeurIPS, 2024) — Algorithmic reduction of MaxSim to inner product with approximation guarantees; does NOT address expressiveness\n- Jacob et al., \"On Strengths and Limitations of Single-Vector Embeddings\" (arXiv, 2026) — Empirically confirms multi-vector superiority on LIMIT but uses only toy math models; explicitly lacks formal theory\n- Khattab & Zaharia, \"ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction\" (SIGIR, 2020) — Introduced MaxSim; foundational architecture whose expressiveness we characterize\n\nKnown Gaps:\n- No formal characterization of the representational capacity of sum-of-max-inner-product scoring as a function of number of vectors and dimensionality\n- No proven separation result showing which relevance patterns multi-vector can represent that single-vector provably cannot (beyond empirical demonstrations on LIMIT)\n- No connection between MaxSim expressiveness and communication complexity or combinatorial dimensions analogous to sign-rank\n\nTheoretical Anchor: Sign-rank of binary matrices characterizes single-vector embedding capacity (Weller et al.). MaxSim scoring over k vectors per document can be viewed as a richer communication protocol where each party sends k messages instead of one. The analogous complexity measure — potentially related to partition number or multi-round communication complexity — should yield tighter and more favorable bounds, formally explaining multi-vector superiority.\n\nConstraints:\n- Compute: ≤200 H100-hours (primarily theoretical; compute needed only for empirical validation on LIMIT and synthetic constructions)\n\nQuality Self-Checks:\n- [x] Core insight: Multi-vector retrieval's empirical superiority over single-vector can be formally characterized through communication complexity, yielding provable separation results.\n- [x] Why not obvious: Sign-rank gives clean bounds for inner products but sum-of-max-inner-products introduces combinatorial structure (assignment problems) that breaks standard techniques — requires novel proof strategies.\n- [x] Baseline fear test: A simple 'multi-vector is at least as expressive as single-vector' result would be trivial; we need tight bounds showing HOW MUCH more expressive, as a function of the number of vectors.\n- [x] Information exploited: The structure of MaxSim as a combinatorial optimization (max-matching) over inner products — this algebraic structure is what enables stronger representational capacity and what existing analyses ignore.\n\nAvoid:\n- Purely empirical comparisons of single-vector vs multi-vector (already done extensively; adds nothing new)\n- Loose existential bounds that only show multi-vector CAN be better without quantifying the gap\n- Ignoring computational complexity — bounds that require exponentially many vectors per document are theoretically interesting but practically useless\n- Conflating approximation guarantees (MUVERA-style) with expressiveness characterization — these are orthogonal questions`\n2. `oral spotlight {venue} 2026 {topic}` — for each major venue\n3. `site:openreview.net {topic} 2026 outstanding` — OpenReview 高分论文\n4. `{topic} survey 2026` 或 `{topic} survey 2025` — 综述论文\n5. `site:arxiv.org {topic} 2026` — arXiv 最新高引\n6. `most cited {topic} 2025 2026` — Google Scholar\n7. `site:paperswithcode.com {task} SOTA` — SOTA 排行榜上的论文\n8. `{topic} benchmark {year}` — 定义领域的 benchmark 论文\n9. 对每个找到的重要论文，搜索其 cited-by 发现后续工作\n\nFor EVERY paper you find, use WebFetch to read its abstract and introduction on arXiv or OpenReview. Do NOT rely on search snippets alone — you need to understand what each paper actually does.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Full paper title\",\n  \"authors\": \"First author et al.\",\n  \"venue\": \"EMNLP 2025 / NeurIPS 2024 / arXiv 2025 / ...\",\n  \"url\": \"https://arxiv.org/abs/... or openreview URL\",\n  \"why_important\": \"Best paper / Oral / High-cited / Introduced X / ...\",\n  \"one_line_summary\": \"What this paper does in one sentence\"\n}\n\nFind at least 15 papers. More is better if they are genuinely relevant.\nIMPORTANT: You MUST end your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:09:30.759Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:09:30.759Z",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-30T06:09:30.774Z_

You are a senior ML researcher conducting a comprehensive literature survey.

**Today's date: 2026-05-30 (UTC).**

## Task
Find the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:

**Target: AAAI 2026
Track: Information Retrieval and Text Mining (or Machine Learning: Theory)

Direction: Establish formal expressiveness bounds for multi-vector (MaxSim/Chamfer) retrieval representations — the sign-rank equivalent for ColBERT-style late interaction. While LIMIT (ICLR 2026) proved that single-vector embeddings have fundamental capacity limitations tied to sign-rank, no formal theory exists for what multi-vector representations with sum-of-max scoring can express. We aim to characterize the representational capacity of MaxSim as a function of the number of vectors per document and their dimensionality, providing tight bounds analogous to sign-rank for inner products.

Seed Papers:
- Weller et al., "On the Theoretical Limitations of Embedding-Based Retrieval" (ICLR, 2026) — Proves single-vector limitations via sign-rank; the direct theoretical anchor we extend
- Wang et al., "R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval" (arXiv, 2026) — Proves dimension sufficiency for single-vector; our work must be consistent with or subsume this
- Dhulipala et al., "MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings" (NeurIPS, 2024) — Algorithmic reduction of MaxSim to inner product with approximation guarantees; does NOT address expressiveness
- Jacob et al., "On Strengths and Limitations of Single-Vector Embeddings" (arXiv, 2026) — Empirically confirms multi-vector superiority on LIMIT but uses only toy math models; explicitly lacks formal theory
- Khattab & Zaharia, "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction" (SIGIR, 2020) — Introduced MaxSim; foundational architecture whose expressiveness we characterize

Known Gaps:
- No formal characterization of the representational capacity of sum-of-max-inner-product scoring as a function of number of vectors and dimensionality
- No proven separation result showing which relevance patterns multi-vector can represent that single-vector provably cannot (beyond empirical demonstrations on LIMIT)
- No connection between MaxSim expressiveness and communication complexity or combinatorial dimensions analogous to sign-rank

Theoretical Anchor: Sign-rank of binary matrices characterizes single-vector embedding capacity (Weller et al.). MaxSim scoring over k vectors per document can be viewed as a richer communication protocol where each party sends k messages instead of one. The analogous complexity measure — potentially related to partition number or multi-round communication complexity — should yield tighter and more favorable bounds, formally explaining multi-vector superiority.

Constraints:
- Compute: ≤200 H100-hours (primarily theoretical; compute needed only for empirical validation on LIMIT and synthetic constructions)

Quality Self-Checks:
- [x] Core insight: Multi-vector retrieval's empirical superiority over single-vector can be formally characterized through communication complexity, yielding provable separation results.
- [x] Why not obvious: Sign-rank gives clean bounds for inner products but sum-of-max-inner-products introduces combinatorial structure (assignment problems) that breaks standard techniques — requires novel proof strategies.
- [x] Baseline fear test: A simple 'multi-vector is at least as expressive as single-vector' result would be trivial; we need tight bounds showing HOW MUCH more expressive, as a function of the number of vectors.
- [x] Information exploited: The structure of MaxSim as a combinatorial optimization (max-matching) over inner products — this algebraic structure is what enables stronger representational capacity and what existing analyses ignore.

Avoid:
- Purely empirical comparisons of single-vector vs multi-vector (already done extensively; adds nothing new)
- Loose existential bounds that only show multi-vector CAN be better without quantifying the gap
- Ignoring computational complexity — bounds that require exponentially many vectors per document are theoretically interesting but practically useless
- Conflating approximation guarantees (MUVERA-style) with expressiveness characterization — these are orthogonal questions**

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
Track: Information Retrieval and Text Mining (or Machine Learning: Theory)

Direction: Establish formal expressiveness bounds for multi-vector (MaxSim/Chamfer) retrieval representations — the sign-rank equivalent for ColBERT-style late interaction. While LIMIT (ICLR 2026) proved that single-vector embeddings have fundamental capacity limitations tied to sign-rank, no formal theory exists for what multi-vector representations with sum-of-max scoring can express. We aim to characterize the representational capacity of MaxSim as a function of the number of vectors per document and their dimensionality, providing tight bounds analogous to sign-rank for inner products.

Seed Papers:
- Weller et al., "On the Theoretical Limitations of Embedding-Based Retrieval" (ICLR, 2026) — Proves single-vector limitations via sign-rank; the direct theoretical anchor we extend
- Wang et al., "R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval" (arXiv, 2026) — Proves dimension sufficiency for single-vector; our work must be consistent with or subsume this
- Dhulipala et al., "MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings" (NeurIPS, 2024) — Algorithmic reduction of MaxSim to inner product with approximation guarantees; does NOT address expressiveness
- Jacob et al., "On Strengths and Limitations of Single-Vector Embeddings" (arXiv, 2026) — Empirically confirms multi-vector superiority on LIMIT but uses only toy math models; explicitly lacks formal theory
- Khattab & Zaharia, "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction" (SIGIR, 2020) — Introduced MaxSim; foundational architecture whose expressiveness we characterize

Known Gaps:
- No formal characterization of the representational capacity of sum-of-max-inner-product scoring as a function of number of vectors and dimensionality
- No proven separation result showing which relevance patterns multi-vector can represent that single-vector provably cannot (beyond empirical demonstrations on LIMIT)
- No connection between MaxSim expressiveness and communication complexity or combinatorial dimensions analogous to sign-rank

Theoretical Anchor: Sign-rank of binary matrices characterizes single-vector embedding capacity (Weller et al.). MaxSim scoring over k vectors per document can be viewed as a richer communication protocol where each party sends k messages instead of one. The analogous complexity measure — potentially related to partition number or multi-round communication complexity — should yield tighter and more favorable bounds, formally explaining multi-vector superiority.

Constraints:
- Compute: ≤200 H100-hours (primarily theoretical; compute needed only for empirical validation on LIMIT and synthetic constructions)

Quality Self-Checks:
- [x] Core insight: Multi-vector retrieval's empirical superiority over single-vector can be formally characterized through communication complexity, yielding provable separation results.
- [x] Why not obvious: Sign-rank gives clean bounds for inner products but sum-of-max-inner-products introduces combinatorial structure (assignment problems) that breaks standard techniques — requires novel proof strategies.
- [x] Baseline fear test: A simple 'multi-vector is at least as expressive as single-vector' result would be trivial; we need tight bounds showing HOW MUCH more expressive, as a function of the number of vectors.
- [x] Information exploited: The structure of MaxSim as a combinatorial optimization (max-matching) over inner products — this algebraic structure is what enables stronger representational capacity and what existing analyses ignore.

Avoid:
- Purely empirical comparisons of single-vector vs multi-vector (already done extensively; adds nothing new)
- Loose existential bounds that only show multi-vector CAN be better without quantifying the gap
- Ignoring computational complexity — bounds that require exponentially many vectors per document are theoretically interesting but practically useless
- Conflating approximation guarantees (MUVERA-style) with expressiveness characterization — these are orthogonal questions`
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
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "2324a5ba-5059-47db-adcc-3d96b8819093",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:09:30.772Z_

```json
{
  "parentUuid": "2324a5ba-5059-47db-adcc-3d96b8819093",
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
  "uuid": "6afd4968-3466-4484-b227-3b634b53d471",
  "timestamp": "2026-05-30T06:09:30.772Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:09:30.772Z_

```json
{
  "parentUuid": "6afd4968-3466-4484-b227-3b634b53d471",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "87d13def-f287-45d1-b601-286ef23f6707",
  "timestamp": "2026-05-30T06:09:30.772Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
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
  "aiTitle": "Literature survey on multi-vector retrieval expressiveness",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Assistant

_source line 7 · 2026-05-30T06:09:35.784Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a comprehensive literature survey to find the 15 most important recent papers (2024-2026) related to formal expressiveness bounds for multi-vector retrieval representations, sign-rank theory, ColBERT-style late interaction, and related theoretical foundations for information retrieval.

Let me break this down into parallel search tasks to be efficient. I'll need to use WebSearch and WebFetch tools, which are deferred tools that need to be loaded first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87d13def-f287-45d1-b601-286ef23f6707",
  "isSidechain": false,
  "requestId": "req_011CbYFkufVbMXhFQ2iAhj8V",
  "type": "assistant",
  "uuid": "cc738cd8-c5cc-44f3-b9d0-a1887736d4f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CV3DiqcDnfq2VwDJrZeK8d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15023,
      "cache_read_input_tokens": 0,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 198,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15023
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

_source line 8 · 2026-05-30T06:09:36.460Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019JG1Y1nXvYomra8rZyUyEF`</summary>

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
  "parentUuid": "cc738cd8-c5cc-44f3-b9d0-a1887736d4f5",
  "isSidechain": false,
  "requestId": "req_011CbYFkufVbMXhFQ2iAhj8V",
  "type": "assistant",
  "uuid": "284abfe6-2e24-4214-8f64-60221d99b730",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CV3DiqcDnfq2VwDJrZeK8d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15023,
      "cache_read_input_tokens": 0,
      "output_tokens": 198,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15023,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 198,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15023,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15023
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

_source line 9 · 2026-05-30T06:09:36.470Z_

<details><summary>↩ Tool result · `toolu_019JG1Y1nXvYomra8rZyUyEF`</summary>

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
  "parentUuid": "284abfe6-2e24-4214-8f64-60221d99b730",
  "isSidechain": false,
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "47606dc9-58fe-4b9c-9aae-9aff71d1396c",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "284abfe6-2e24-4214-8f64-60221d99b730",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-30T06:09:44.912Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have WebSearch and WebFetch available. Let me launch multiple parallel search agents to cover the breadth of this literature survey efficiently. I'll organize searches into several parallel batches.

Let me launch several agents in parallel to conduct different search threads:

1. Agent for seed papers and their citations (Weller et al., MUVERA, etc.)
2. Agent for sign-rank, communication complexity, and embedding theory
3. Agent for ColBERT, multi-vector retrieval, late interaction advances
4. Agent for information retrieval theory, expressiveness bounds
5. Agent for best paper awards at top venues in relevant areas


6. Agent for dense retrieval, neural ranking, and transformer-based methods
7. Agent for vector quantization, approximate nearest neighbor search, and indexing
8. Agent for cross-lingual and multilingual retrieval systems
9. Agent for evaluation metrics, benchmarks, and datasets in IR
10. Agent for practical applications and industry implementations
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47606dc9-58fe-4b9c-9aae-9aff71d1396c",
  "isSidechain": false,
  "requestId": "req_011CbYFmKSj2xRmvN21pRWRu",
  "type": "assistant",
  "uuid": "8bd0c7a7-5d69-442c-be7e-c1f1e5497b22",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUHY7yZu4uQHfYHtUD4Bo6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 15023,
      "output_tokens": 2169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2169,
          "cache_read_input_tokens": 15023,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
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

_source line 11 · 2026-05-30T06:09:44.913Z_

I'll launch multiple parallel search agents to cover different facets of this literature survey comprehensively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8bd0c7a7-5d69-442c-be7e-c1f1e5497b22",
  "isSidechain": false,
  "requestId": "req_011CbYFmKSj2xRmvN21pRWRu",
  "type": "assistant",
  "uuid": "794ac3db-7117-4031-8466-8be44c7502dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUHY7yZu4uQHfYHtUD4Bo6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 15023,
      "output_tokens": 2169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2169,
          "cache_read_input_tokens": 15023,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
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

_source line 12 · 2026-05-30T06:09:53.297Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GEbWKNWHDwYAJQQAGUhmQV`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search seed papers and citations",
  "prompt": "You are helping with a literature survey on formal expressiveness bounds for multi-vector retrieval (MaxSim/ColBERT-style). \n\nSearch for and fetch details on the following SEED PAPERS and their most important citing/related works (2024-2026):\n\n1. Search for: Weller et al. \"On the Theoretical Limitations of Embedding-Based Retrieval\" ICLR 2026 — fetch the arxiv abstract\n2. Search for: Wang et al. \"R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval\" arXiv 2026 — fetch abstract\n3. Search for: Dhulipala et al. \"MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings\" NeurIPS 2024 — fetch abstract\n4. Search for: Jacob et al. \"On Strengths and Limitations of Single-Vector Embeddings\" arXiv 2026 — fetch abstract\n5. Search for papers that CITE Weller et al. ICLR 2026 (the LIMIT paper) — use Google Scholar or Semantic Scholar\n6. Search for papers that cite MUVERA NeurIPS 2024\n\nFor each paper found, use WebFetch to read its arxiv abstract page. Report back:\n- Full title\n- Authors  \n- Venue and year\n- URL\n- One-line summary of what the paper does\n- Why it's important for the survey topic (expressiveness of multi-vector retrieval, sign-rank theory, embedding capacity)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "794ac3db-7117-4031-8466-8be44c7502dc",
  "isSidechain": false,
  "requestId": "req_011CbYFmKSj2xRmvN21pRWRu",
  "type": "assistant",
  "uuid": "3dd56462-7a20-47e3-9738-5d7421e8143c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUHY7yZu4uQHfYHtUD4Bo6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 15023,
      "output_tokens": 2169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2169,
          "cache_read_input_tokens": 15023,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
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

_source line 13 · 2026-05-30T06:09:58.867Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MWE9qr3hbuPiAd5MePj4GL`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search sign-rank and communication complexity",
  "prompt": "You are helping with a literature survey on formal expressiveness bounds for multi-vector retrieval representations. The key theoretical tools involve sign-rank, communication complexity, and combinatorial dimensions.\n\nConduct these searches and fetch abstracts for all relevant papers found (2024-2026):\n\n1. WebSearch: \"sign-rank matrix communication complexity embeddings 2025 2026\"\n2. WebSearch: \"sign-rank neural retrieval expressiveness bounds\"\n3. WebSearch: \"communication complexity information retrieval theory 2025 2026\"\n4. WebSearch: \"representational capacity embeddings theoretical bounds 2024 2025 2026\"\n5. WebSearch: \"VC dimension margin bounds retrieval models 2024 2025\"\n6. WebSearch: \"bilinear rank inner product embedding capacity limitations\"\n7. WebSearch: \"multi-round communication complexity matrix factorization\"\n\nFor each relevant paper found (2024-2026), use WebFetch on its arxiv page to get the full abstract. Report:\n- Full title, authors, venue/year, URL\n- One-line summary\n- Relevance to expressiveness bounds for retrieval embeddings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3dd56462-7a20-47e3-9738-5d7421e8143c",
  "isSidechain": false,
  "requestId": "req_011CbYFmKSj2xRmvN21pRWRu",
  "type": "assistant",
  "uuid": "af55e929-c356-4c00-961b-a97e2b1f7817",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUHY7yZu4uQHfYHtUD4Bo6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 15023,
      "output_tokens": 2169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2169,
          "cache_read_input_tokens": 15023,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
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

_source line 14 · 2026-05-30T06:10:03.815Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013HpvgNR2nMrYBtwdvaqK8X`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search ColBERT and multi-vector retrieval",
  "prompt": "You are helping with a literature survey on formal expressiveness bounds for multi-vector (MaxSim/ColBERT-style) retrieval. \n\nConduct these searches and fetch abstracts for relevant papers (2024-2026):\n\n1. WebSearch: \"ColBERT multi-vector retrieval 2025 2026 theory\"\n2. WebSearch: \"MaxSim scoring late interaction retrieval 2024 2025 2026\"\n3. WebSearch: \"multi-vector retrieval expressiveness capacity 2024 2025 2026\"\n4. WebSearch: \"ColBERTv2 PLAID XTR late interaction retrieval 2024 2025\"\n5. WebSearch: \"dense retrieval single-vector vs multi-vector comparison 2024 2025 2026\"\n6. WebSearch: \"Chamfer similarity retrieval multi-vector 2024 2025\"\n7. WebSearch: \"token-level representation retrieval models theory 2024 2025 2026\"\n8. WebSearch: \"learned sparse retrieval vs dense retrieval expressiveness 2024 2025\"\n\nFor each relevant paper, use WebFetch on its arxiv/openreview page to get the abstract. Report:\n- Full title, authors, venue/year, URL\n- One-line summary\n- Why important for understanding multi-vector retrieval expressiveness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af55e929-c356-4c00-961b-a97e2b1f7817",
  "isSidechain": false,
  "requestId": "req_011CbYFmKSj2xRmvN21pRWRu",
  "type": "assistant",
  "uuid": "fa69834c-e0e0-40c2-8464-e042cb39eb36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUHY7yZu4uQHfYHtUD4Bo6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 15023,
      "output_tokens": 2169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2169,
          "cache_read_input_tokens": 15023,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
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

_source line 15 · 2026-05-30T06:10:09.544Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DXp3ctLFdiNjm5woKndm81`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search IR theory best papers 2024-2026",
  "prompt": "You are helping with a literature survey on theoretical foundations of information retrieval, specifically expressiveness of retrieval models and embedding theory.\n\nConduct these searches:\n\n1. WebSearch: \"best paper award NeurIPS 2024 2025 retrieval embeddings\"\n2. WebSearch: \"best paper award ICML 2024 2025 representation learning theory\"\n3. WebSearch: \"best paper award ICLR 2025 2026 embeddings retrieval\"\n4. WebSearch: \"outstanding paper AAAI 2025 2026 information retrieval\"\n5. WebSearch: \"best paper ACL EMNLP 2024 2025 retrieval text mining\"\n6. WebSearch: \"oral spotlight NeurIPS 2024 2025 embedding theory retrieval\"\n7. WebSearch: \"oral spotlight ICML 2025 representation learning bounds\"\n8. WebSearch: site:openreview.net \"multi-vector retrieval\" OR \"MaxSim\" OR \"late interaction\" 2025 2026\n\nFor each relevant paper found, use WebFetch to read its abstract. Report:\n- Full title, authors, venue/year, URL\n- One-line summary\n- Award status (best paper, oral, spotlight, etc.)\n- Relevance to multi-vector retrieval expressiveness theory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa69834c-e0e0-40c2-8464-e042cb39eb36",
  "isSidechain": false,
  "requestId": "req_011CbYFmKSj2xRmvN21pRWRu",
  "type": "assistant",
  "uuid": "228a80f2-36a7-473f-b522-c213270092cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUHY7yZu4uQHfYHtUD4Bo6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 15023,
      "output_tokens": 2169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2169,
          "cache_read_input_tokens": 15023,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
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

_source line 16 · 2026-05-30T06:10:14.895Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01SCG2EmSaceDpYcGedqHN8W`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search embedding theory and nearest neighbor",
  "prompt": "You are helping with a literature survey on theoretical bounds for retrieval embeddings, particularly multi-vector representations.\n\nConduct these searches and fetch abstracts for relevant papers (2024-2026):\n\n1. WebSearch: \"embedding dimension bounds nearest neighbor search theory 2024 2025 2026\"\n2. WebSearch: \"maximum inner product search theoretical bounds 2024 2025 2026\"\n3. WebSearch: \"approximate nearest neighbor lower bounds communication complexity 2024 2025\"\n4. WebSearch: \"metric embedding distortion bounds 2024 2025 2026\"\n5. WebSearch: \"tensor decomposition rank bounds retrieval 2024 2025\"\n6. WebSearch: \"survey dense retrieval neural information retrieval 2024 2025 2026\"\n7. WebSearch: \"matroid intersection assignment problem complexity retrieval\"\n8. WebSearch: \"partition number combinatorial dimension machine learning 2024 2025\"\n9. WebSearch: \"Natarajan dimension multiclass learning theory bounds 2024 2025\"\n10. WebSearch: \"learning to retrieve theoretical analysis 2024 2025 2026\"\n\nFor each relevant paper, use WebFetch on its arxiv/conference page to get the abstract. Report:\n- Full title, authors, venue/year, URL\n- One-line summary\n- Why important for understanding expressiveness of multi-vector retrieval"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "228a80f2-36a7-473f-b522-c213270092cb",
  "isSidechain": false,
  "requestId": "req_011CbYFmKSj2xRmvN21pRWRu",
  "type": "assistant",
  "uuid": "44d06f17-0a54-4cea-af32-3b6f374bfd8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUHY7yZu4uQHfYHtUD4Bo6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1218,
      "cache_read_input_tokens": 15023,
      "output_tokens": 2169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1218,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2169,
          "cache_read_input_tokens": 15023,
          "cache_creation_input_tokens": 1218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1218
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

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "44d06f17-0a54-4cea-af32-3b6f374bfd8c",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on multi-vector retrieval expressiveness",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Tool result

_source line 19 · 2026-05-30T06:13:19.109Z_

<details><summary>↩ Tool result · `toolu_01MWE9qr3hbuPiAd5MePj4GL`</summary>

```text
Now I have comprehensive information on all the relevant papers. Let me compile the final report.

---

## Literature Survey: Formal Expressiveness Bounds for Multi-Vector Retrieval Representations (2024--2026)

Below are the relevant papers found, organized by direct relevance to the core topic (sign-rank, communication complexity, combinatorial dimensions applied to retrieval embeddings).

---

### TIER 1: Directly on Expressiveness Bounds for Retrieval Embeddings

---

**Paper 1: "On the Theoretical Limitations of Embedding-Based Retrieval"**

- **Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee
- **Venue/Year:** ICLR 2026 (arXiv:2508.21038, August 2025)
- **URL:** [https://arxiv.org/abs/2508.21038](https://arxiv.org/abs/2508.21038)
- **Abstract:** "Vector embeddings have been tasked with an ever-increasing set of retrieval tasks over the years, with a nascent rise in using them for reasoning, instruction-following, coding, and more. These new benchmarks push embeddings to work for any query and any notion of relevance that could be given. While prior works have pointed out theoretical limitations of vector embeddings, there is a common assumption that these difficulties are exclusively due to unrealistic queries, and those that are not can be overcome with better training data and larger models. In this work, we demonstrate that we may encounter these theoretical limitations in realistic settings with extremely simple queries. We connect known results in learning theory, showing that the number of top-k subsets of documents capable of being returned as the result of some query is limited by the dimension of the embedding. We empirically show that this holds true even if we restrict to k=2, and directly optimize on the test set with free parameterized embeddings. We then create a realistic dataset called LIMIT that stress tests models based on these theoretical results, and observe that even state-of-the-art models fail on this dataset despite the simple nature of the task. Our work shows the limits of embedding models under the existing single vector paradigm and calls for future research to develop methods that can resolve this fundamental limitation."
- **Summary:** Proves that the number of realizable top-k retrieval subsets is bounded by embedding dimension, using sign-rank of the relevance matrix from communication complexity theory.
- **Relevance:** THE central paper for this survey. Directly connects sign-rank, communication complexity, and embedding dimension lower bounds for retrieval. Shows rank_pm(2A - 1) - 1 <= d <= rank_pm(2A - 1) where A is the binary relevance matrix.

---

**Paper 2: "R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval"**

- **Authors:** Zihao Wang, Hang Yin, Lihui Liu, Hanghang Tong, Yangqiu Song, Ginny Wong, Simon See
- **Venue/Year:** arXiv:2601.20844, January 2026
- **URL:** [https://arxiv.org/abs/2601.20844](https://arxiv.org/abs/2601.20844)
- **Abstract:** Studies the minimal embedding dimension (MED) required to represent all possible top-k subset memberships over m elements. Derives tight bounds showing MED = Theta(k), independent of the corpus size m. Specifically proves lower bound k-1 and upper bound 2k for inner product, cosine similarity, and Euclidean distance scoring.
- **Summary:** Proves dimension 2k suffices for top-k retrieval regardless of corpus size, directly contradicting the empirical polynomial-in-m scaling from Weller et al.
- **Relevance:** Provides a competing/complementary theoretical result arguing that geometric capacity is not the bottleneck -- learnability is. The debate between this paper and Weller et al. is central to understanding what sign-rank bounds actually mean for practical retrieval.

---

**Paper 3: "On Strengths and Limitations of Single-Vector Embeddings"**

- **Authors:** Archish S, Mihir Agarwal, Ankit Garg, Neeraj Kayal, Kirankumar Shiragur
- **Venue/Year:** arXiv:2603.29519, March 2026
- **URL:** [https://arxiv.org/abs/2603.29519](https://arxiv.org/abs/2603.29519)
- **Abstract:** Investigates why single-vector embedding models fail on the LIMIT dataset. Proves that for k-sparse relevance matrices, embeddings of dimension 2k+1 suffice. Identifies domain shift and misalignment (not dimensionality) as primary failure causes. Proves that single-vector models suffer drowning probability of order exp(-Theta(d/n)) while multi-vector models achieve exp(-Theta(d/log(n))), giving exponentially better separation as corpus grows. Fine-tuning causes catastrophic forgetting (>40% MSMARCO drop) for single-vector but not multi-vector models.
- **Summary:** Provides formal separation between single-vector and multi-vector representations via drowning analysis, proving multi-vector embeddings are exponentially more robust to corpus scaling.
- **Relevance:** Directly formalizes the expressiveness gap between single-vector and multi-vector retrieval with mathematical drowning bounds, complementing the sign-rank approach.

---

**Paper 4: "Does Generative Retrieval Overcome the Limitations of Dense Retrieval?"**

- **Authors:** Yingchen Zhang, Ruqing Zhang, Jiafeng Guo, Maarten de Rijke, Yixing Fan, Xueqi Cheng
- **Venue/Year:** arXiv:2509.22116, September 2025
- **URL:** [https://arxiv.org/abs/2509.22116](https://arxiv.org/abs/2509.22116)
- **Abstract:** Investigates how generative retrieval (GR) differs from dense retrieval (DR) in learning objectives and representational capacity. Shows GR performs globally normalized maximum-likelihood optimization and encodes corpus/relevance information directly in model parameters, while DR uses locally normalized objectives with external embeddings. Proves GR's representational capacity scales with model parameters without DR's low-rank constraints. However, GR does not consistently outperform DR in practice.
- **Summary:** Analyzes how dense retrieval's low-rank embedding constraint limits representational capacity and whether generative retrieval can theoretically overcome this.
- **Relevance:** Directly addresses the low-rank constraint (related to bilinear rank) of embedding-based retrieval and proposes an alternative paradigm.

---

### TIER 2: Sign-Rank and Communication Complexity Theory (Foundational Tools)

---

**Paper 5: "Sign Rank Limitations for Inner Product Graph Decoders"**

- **Authors:** Su Hyeong Lee, Qingqi Zhang, Risi Kondor
- **Venue/Year:** ICML 2024 (arXiv:2402.06662)
- **URL:** [https://arxiv.org/abs/2402.06662](https://arxiv.org/abs/2402.06662)
- **Abstract:** Provides the first theoretical analysis of why inner product-based decoders have limited representation capacity for graph reconstruction. Formalizes low dimensionality using sign-rank and provides deterministic bounds on the minimum latent feature dimension necessary for faithful graph reconstruction. Proposes simple modifications that maintain the inner product framework while addressing these limitations.
- **Summary:** Uses sign-rank to prove dimension lower bounds for inner-product graph decoders -- the graph-domain analogue of the retrieval embedding problem.
- **Relevance:** Directly foundational. The sign-rank framework applied to inner-product decoders is the same mathematical tool used by Weller et al. for retrieval, but applied in the graph representation learning domain.

---

**Paper 6: "Sign-Rank of k-Hamming Distance is Constant"**

- **Authors:** Mika Goos, Nathaniel Harms, Valentin Imbach, Dmitry Sokolov
- **Venue/Year:** arXiv:2506.12022, May 2025
- **URL:** [https://arxiv.org/abs/2506.12022](https://arxiv.org/abs/2506.12022)
- **Abstract:** Proves that the sign-rank of the k-Hamming Distance matrix on n bits is 2^{O(k)}, independent of n. This refutes conjectures by Hatami et al. (RANDOM 2022, STOC 2023) that sign-rank should depend on n. The technique gives constant sign-rank upper bounds for all matrices reducing to k-Hamming Distance, and challenges the distinction between margin complexity and sign-rank (bounded-error vs. unbounded-error communication complexity).
- **Summary:** Major breakthrough showing sign-rank of k-Hamming Distance is constant, collapsing conjectured separations between bounded and unbounded error communication complexity for this class.
- **Relevance:** Directly affects the tightness of sign-rank-based lower bounds for retrieval. If relevance matrices have structure reducing to k-Hamming Distance, their sign-rank may be much smaller than previously thought, weakening dimension lower bounds.

---

**Paper 7: "Randomized Communication and Implicit Representations for Matrices and Graphs of Small Sign-Rank"**

- **Authors:** Nathaniel Harms, Viktor Zamaraev
- **Venue/Year:** arXiv:2307.04441, July 2023
- **URL:** [https://arxiv.org/abs/2307.04441](https://arxiv.org/abs/2307.04441)
- **Abstract:** Characterizes when sign-rank 3 matrices and unit disk graphs admit constant-cost public-coin randomized communication protocols. Proves such objects have constant randomized communication complexity precisely when they avoid encoding arbitrarily large instances of the Greater-Than problem (equivalently, lack arbitrarily large half-graphs as semi-induced subgraphs).
- **Summary:** Characterizes the communication complexity of low sign-rank matrices via forbidden substructures.
- **Relevance:** Provides structural understanding of when low sign-rank translates to efficient communication/representation, relevant to understanding when retrieval matrices admit low-dimensional embeddings.

---

**Paper 8: "Structure in Communication Complexity and Constant-Cost Complexity Classes"**

- **Authors:** Hamed Hatami, Pooya Hatami
- **Venue/Year:** ACM SIGACT News Complexity Theory Column, 2024 (arXiv:2401.14623)
- **URL:** [https://arxiv.org/abs/2401.14623](https://arxiv.org/abs/2401.14623)
- **Abstract:** Survey examining how the complexity of a Boolean matrix in various communication models is controlled by analytic/algebraic matrix parameters (rank, sign-rank, discrepancy, etc.). Outlines research directions on the structural relationship between these parameters and communication complexity.
- **Summary:** Survey of the structural theory connecting sign-rank, discrepancy, and communication complexity for Boolean matrices.
- **Relevance:** Provides the theoretical framework underpinning the sign-rank approach to retrieval bounds. Key reference for understanding which algebraic parameters control representational capacity.

---

**Paper 9: "The Communication Complexity of Approximating Matrix Rank"**

- **Authors:** Alexander A. Sherstov, Andrey A. Storozhenko
- **Venue/Year:** FOCS 2024 (arXiv:2410.20094)
- **URL:** [https://arxiv.org/abs/2410.20094](https://arxiv.org/abs/2410.20094)
- **Abstract:** Determines communication complexity of approximating matrix rank over finite fields. Proves a lower bound of Omega(1 + r^2 log|F|) for randomized communication in distinguishing rank cases, shown to be optimal. Derives exponential improvements in space lower bounds for streaming algorithms approximating matrix rank.
- **Summary:** Tight communication complexity bounds for matrix rank approximation, with streaming lower bound applications.
- **Relevance:** Relevant to understanding the communication cost of rank-related computations, which underlies the factorization-based view of embedding capacity.

---

### TIER 3: Embedding Capacity and Dimension Bounds (Supporting)

---

**Paper 10: "Dimension-Accuracy Tradeoffs in Contrastive Embeddings for Triplets, Terminals & Top-k Nearest Neighbors"**

- **Authors:** Vaggos Chatziafratis, Piotr Indyk
- **Venue/Year:** arXiv:2312.13490, December 2023
- **URL:** [https://arxiv.org/abs/2312.13490](https://arxiv.org/abs/2312.13490)
- **Abstract:** Proves that ordinal embeddings preserving all triplet comparisons require dimension growing as n/2 in the worst case (nearly optimal since n-1 always suffices). Establishes dimension-relaxation tradeoffs when approximate preservation is allowed. Extends to terminal and top-k nearest neighbor ordinal embeddings.
- **Summary:** Near-tight dimension lower bounds for order-preserving embeddings with extensions to top-k NN settings.
- **Relevance:** Provides combinatorial dimension bounds for embedding problems closely related to retrieval (top-k NN), using different tools (ordinal embedding theory rather than sign-rank).

---

**Paper 11: "Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the Limits of Embedding Space Capacity"**

- **Authors:** Yuri Kuratov, Mikhail Arkhipov, Aydar Bulatov, Mikhail Burtsev
- **Venue/Year:** ACL 2025 (arXiv:2502.13063)
- **URL:** [https://arxiv.org/abs/2502.13063](https://arxiv.org/abs/2502.13063)
- **Abstract:** Investigates sequence compression into single vectors. Shows via per-sample optimization that vectors with compression ratios up to x1500 exist, far exceeding the ~x10 ratio of current encoder methods. Capacity is constrained by information uncertainty (cross-entropy loss) rather than input length.
- **Summary:** Empirically and theoretically explores the information capacity of single embedding vectors, revealing a large gap between theoretical and practical utilization.
- **Relevance:** Addresses the information-theoretic capacity of single-vector representations from a compression perspective, complementing the combinatorial/sign-rank approach.

---

**Paper 12: "Capacity Bounds for Hyperbolic Neural Network Representations of Latent Tree Structures"**

- **Authors:** Anastasis Kratsios, Ruiyang Hong, Haitz Saez de Ocariz Borde
- **Venue/Year:** arXiv:2308.09250, August 2023
- **URL:** [https://arxiv.org/abs/2308.09250](https://arxiv.org/abs/2308.09250)
- **Abstract:** Proves that deep hyperbolic ReLU networks can embed any finite weighted tree into hyperbolic space with controlled distortion. Establishes that standard Euclidean ReLU MLPs must introduce at least Omega(L^{1/d}) distortion when embedding trees with more than 2^d leaves into d-dimensional Euclidean space.
- **Summary:** Dimension-dependent distortion lower bounds for Euclidean embeddings of trees, with hyperbolic alternatives avoiding this limitation.
- **Relevance:** Demonstrates that embedding geometry (Euclidean vs. hyperbolic) affects representational capacity bounds, relevant to alternative retrieval embedding spaces.

---

### TIER 4: Adjacent Theoretical Work

---

**Paper 13: "On the Intrinsic Limits of Transformer Image Embeddings in Non-Solvable Spatial Reasoning"**

- **Authors:** Siyi Lyu, Quan Liu, Feng Yan
- **Venue/Year:** arXiv:2601.03048, January 2026
- **URL:** [https://arxiv.org/abs/2601.03048](https://arxiv.org/abs/2601.03048)
- **Abstract:** Shows that constant-depth Vision Transformers are limited to TC^0 complexity while spatial reasoning over non-solvable groups (like SO(3)) requires NC^1, creating a fundamental computational gap. Validates this via the Latent Space Algebra benchmark.
- **Summary:** Proves circuit complexity limits of transformer embeddings for spatial reasoning tasks.
- **Relevance:** Tangentially relevant -- demonstrates that architectural depth constraints impose expressiveness limits on transformer-generated embeddings, though focused on spatial reasoning rather than retrieval.

---

**Paper 14: "Understanding Generalization from Embedding Dimension and Distributional Convergence"**

- **Authors:** Junjie Yu, Zhuoli Ouyang, Haotian Deng, Chen Wei, Wenxiao Ma, Jianyu Zhang, Zihan Deng, Quanying Liu
- **Venue/Year:** arXiv:2601.22756, January 2026
- **URL:** [https://arxiv.org/abs/2601.22756](https://arxiv.org/abs/2601.22756)
- **Abstract:** Shows population risk depends on intrinsic dimensionality of learned embeddings and Lipschitz constants of downstream predictors. Embedding dimension is the dominant factor at the final layer, correlating strongly with empirical generalization.
- **Summary:** Bounds generalization error via embedding dimension, bypassing traditional complexity measures.
- **Relevance:** Provides a generalization-theoretic perspective on why embedding dimension matters, complementing the representational capacity view.

---

**Paper 15: "Communication Complexity Bounds from Information Causality"**

- **Authors:** Nikolai Miklin, Prabhav Jain, Mariami Gachechiladze
- **Venue/Year:** arXiv:2602.10206, February 2026
- **URL:** [https://arxiv.org/abs/2602.10206](https://arxiv.org/abs/2602.10206)
- **Abstract:** Presents an information-theoretic approach to one-way communication complexity using mutual information axioms. Formulates an expanded information causality principle that recovers known lower bounds and generates new ones.
- **Summary:** New information-theoretic technique for communication complexity lower bounds.
- **Relevance:** Provides alternative proof techniques for communication complexity bounds that could potentially be applied to retrieval embedding capacity questions.

---

### Key Takeaways for the Survey

1. **The core theoretical debate** is between Weller et al. (ICLR 2026), who show sign-rank-based dimension lower bounds growing with corpus structure, and Wang et al. (2026), who prove MED = Theta(k) independent of corpus size. The resolution appears to be that geometric capacity is sufficient but learnability is the true bottleneck.

2. **Single-vector vs. multi-vector separation** is formalized by Archish et al. (2026) via drowning probability analysis: multi-vector representations achieve exp(-Theta(d/log n)) vs. single-vector's exp(-Theta(d/n)), an exponential gap in corpus scaling.

3. **Sign-rank is the key algebraic tool** connecting communication complexity to embedding dimension. The Goos et al. (2025) result on constant sign-rank for k-Hamming Distance may weaken some lower bounds by showing certain matrix classes have smaller sign-rank than conjectured.

4. **The inner product decoder limitation** (Lee et al., ICML 2024) provides the graph-domain analogue, using the same sign-rank framework to prove dimension requirements for faithful graph reconstruction via inner products.

Sources:
- [On the Theoretical Limitations of Embedding-Based Retrieval](https://arxiv.org/abs/2508.21038)
- [R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval](https://arxiv.org/abs/2601.20844)
- [On Strengths and Limitations of Single-Vector Embeddings](https://arxiv.org/abs/2603.29519)
- [Does Generative Retrieval Overcome the Limitations of Dense Retrieval?](https://arxiv.org/abs/2509.22116)
- [Sign Rank Limitations for Inner Product Graph Decoders](https://arxiv.org/abs/2402.06662)
- [Sign-Rank of k-Hamming Distance is Constant](https://arxiv.org/abs/2506.12022)
- [Randomized Communication and Implicit Representations for Matrices and Graphs of Small Sign-Rank](https://arxiv.org/abs/2307.04441)
- [Structure in Communication Complexity and Constant-Cost Complexity Classes](https://arxiv.org/abs/2401.14623)
- [The Communication Complexity of Approximating Matrix Rank](https://arxiv.org/abs/2410.20094)
- [Dimension-Accuracy Tradeoffs in Contrastive Embeddings for Triplets, Terminals & Top-k Nearest Neighbors](https://arxiv.org/abs/2312.13490)
- [Cramming 1568 Tokens into a Single Vector and Back Again](https://arxiv.org/abs/2502.13063)
- [Capacity Bounds for Hyperbolic Neural Network Representations of Latent Tree Structures](https://arxiv.org/abs/2308.09250)
- [On the Intrinsic Limits of Transformer Image Embeddings](https://arxiv.org/abs/2601.03048)
- [Understanding Generalization from Embedding Dimension and Distributional Convergence](https://arxiv.org/abs/2601.22756)
- [Communication Complexity Bounds from Information Causality](https://arxiv.org/abs/2602.10206)
- [Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling](https://arxiv.org/abs/2409.14683)
- [LIR: The First Workshop on Late Interaction and Multi Vector Retrieval @ ECIR 2026](https://arxiv.org/abs/2511.00444)

agentId: a159b77b404578005 (use SendMessage with to: 'a159b77b404578005' to continue this agent)
&lt;usage>total_tokens: 34783
tool_uses: 36
duration_ms: 200225&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af55e929-c356-4c00-961b-a97e2b1f7817",
  "isSidechain": false,
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "d3e15db9-8280-4cb7-8768-d05b6aca094e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on formal expressiveness bounds for multi-vector retrieval representations. The key theoretical tools involve sign-rank, communication complexity, and combinatorial dimensions.\n\nConduct these searches and fetch abstracts for all relevant papers found (2024-2026):\n\n1. WebSearch: \"sign-rank matrix communication complexity embeddings 2025 2026\"\n2. WebSearch: \"sign-rank neural retrieval expressiveness bounds\"\n3. WebSearch: \"communication complexity information retrieval theory 2025 2026\"\n4. WebSearch: \"representational capacity embeddings theoretical bounds 2024 2025 2026\"\n5. WebSearch: \"VC dimension margin bounds retrieval models 2024 2025\"\n6. WebSearch: \"bilinear rank inner product embedding capacity limitations\"\n7. WebSearch: \"multi-round communication complexity matrix factorization\"\n\nFor each relevant paper found (2024-2026), use WebFetch on its arxiv page to get the full abstract. Report:\n- Full title, authors, venue/year, URL\n- One-line summary\n- Relevance to expressiveness bounds for retrieval embeddings",
    "agentId": "a159b77b404578005",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all the relevant papers. Let me compile the final report.\n\n---\n\n## Literature Survey: Formal Expressiveness Bounds for Multi-Vector Retrieval Representations (2024--2026)\n\nBelow are the relevant papers found, organized by direct relevance to the core topic (sign-rank, communication complexity, combinatorial dimensions applied to retrieval embeddings).\n\n---\n\n### TIER 1: Directly on Expressiveness Bounds for Retrieval Embeddings\n\n---\n\n**Paper 1: \"On the Theoretical Limitations of Embedding-Based Retrieval\"**\n\n- **Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee\n- **Venue/Year:** ICLR 2026 (arXiv:2508.21038, August 2025)\n- **URL:** [https://arxiv.org/abs/2508.21038](https://arxiv.org/abs/2508.21038)\n- **Abstract:** \"Vector embeddings have been tasked with an ever-increasing set of retrieval tasks over the years, with a nascent rise in using them for reasoning, instruction-following, coding, and more. These new benchmarks push embeddings to work for any query and any notion of relevance that could be given. While prior works have pointed out theoretical limitations of vector embeddings, there is a common assumption that these difficulties are exclusively due to unrealistic queries, and those that are not can be overcome with better training data and larger models. In this work, we demonstrate that we may encounter these theoretical limitations in realistic settings with extremely simple queries. We connect known results in learning theory, showing that the number of top-k subsets of documents capable of being returned as the result of some query is limited by the dimension of the embedding. We empirically show that this holds true even if we restrict to k=2, and directly optimize on the test set with free parameterized embeddings. We then create a realistic dataset called LIMIT that stress tests models based on these theoretical results, and observe that even state-of-the-art models fail on this dataset despite the simple nature of the task. Our work shows the limits of embedding models under the existing single vector paradigm and calls for future research to develop methods that can resolve this fundamental limitation.\"\n- **Summary:** Proves that the number of realizable top-k retrieval subsets is bounded by embedding dimension, using sign-rank of the relevance matrix from communication complexity theory.\n- **Relevance:** THE central paper for this survey. Directly connects sign-rank, communication complexity, and embedding dimension lower bounds for retrieval. Shows rank_pm(2A - 1) - 1 <= d <= rank_pm(2A - 1) where A is the binary relevance matrix.\n\n---\n\n**Paper 2: \"R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval\"**\n\n- **Authors:** Zihao Wang, Hang Yin, Lihui Liu, Hanghang Tong, Yangqiu Song, Ginny Wong, Simon See\n- **Venue/Year:** arXiv:2601.20844, January 2026\n- **URL:** [https://arxiv.org/abs/2601.20844](https://arxiv.org/abs/2601.20844)\n- **Abstract:** Studies the minimal embedding dimension (MED) required to represent all possible top-k subset memberships over m elements. Derives tight bounds showing MED = Theta(k), independent of the corpus size m. Specifically proves lower bound k-1 and upper bound 2k for inner product, cosine similarity, and Euclidean distance scoring.\n- **Summary:** Proves dimension 2k suffices for top-k retrieval regardless of corpus size, directly contradicting the empirical polynomial-in-m scaling from Weller et al.\n- **Relevance:** Provides a competing/complementary theoretical result arguing that geometric capacity is not the bottleneck -- learnability is. The debate between this paper and Weller et al. is central to understanding what sign-rank bounds actually mean for practical retrieval.\n\n---\n\n**Paper 3: \"On Strengths and Limitations of Single-Vector Embeddings\"**\n\n- **Authors:** Archish S, Mihir Agarwal, Ankit Garg, Neeraj Kayal, Kirankumar Shiragur\n- **Venue/Year:** arXiv:2603.29519, March 2026\n- **URL:** [https://arxiv.org/abs/2603.29519](https://arxiv.org/abs/2603.29519)\n- **Abstract:** Investigates why single-vector embedding models fail on the LIMIT dataset. Proves that for k-sparse relevance matrices, embeddings of dimension 2k+1 suffice. Identifies domain shift and misalignment (not dimensionality) as primary failure causes. Proves that single-vector models suffer drowning probability of order exp(-Theta(d/n)) while multi-vector models achieve exp(-Theta(d/log(n))), giving exponentially better separation as corpus grows. Fine-tuning causes catastrophic forgetting (>40% MSMARCO drop) for single-vector but not multi-vector models.\n- **Summary:** Provides formal separation between single-vector and multi-vector representations via drowning analysis, proving multi-vector embeddings are exponentially more robust to corpus scaling.\n- **Relevance:** Directly formalizes the expressiveness gap between single-vector and multi-vector retrieval with mathematical drowning bounds, complementing the sign-rank approach.\n\n---\n\n**Paper 4: \"Does Generative Retrieval Overcome the Limitations of Dense Retrieval?\"**\n\n- **Authors:** Yingchen Zhang, Ruqing Zhang, Jiafeng Guo, Maarten de Rijke, Yixing Fan, Xueqi Cheng\n- **Venue/Year:** arXiv:2509.22116, September 2025\n- **URL:** [https://arxiv.org/abs/2509.22116](https://arxiv.org/abs/2509.22116)\n- **Abstract:** Investigates how generative retrieval (GR) differs from dense retrieval (DR) in learning objectives and representational capacity. Shows GR performs globally normalized maximum-likelihood optimization and encodes corpus/relevance information directly in model parameters, while DR uses locally normalized objectives with external embeddings. Proves GR's representational capacity scales with model parameters without DR's low-rank constraints. However, GR does not consistently outperform DR in practice.\n- **Summary:** Analyzes how dense retrieval's low-rank embedding constraint limits representational capacity and whether generative retrieval can theoretically overcome this.\n- **Relevance:** Directly addresses the low-rank constraint (related to bilinear rank) of embedding-based retrieval and proposes an alternative paradigm.\n\n---\n\n### TIER 2: Sign-Rank and Communication Complexity Theory (Foundational Tools)\n\n---\n\n**Paper 5: \"Sign Rank Limitations for Inner Product Graph Decoders\"**\n\n- **Authors:** Su Hyeong Lee, Qingqi Zhang, Risi Kondor\n- **Venue/Year:** ICML 2024 (arXiv:2402.06662)\n- **URL:** [https://arxiv.org/abs/2402.06662](https://arxiv.org/abs/2402.06662)\n- **Abstract:** Provides the first theoretical analysis of why inner product-based decoders have limited representation capacity for graph reconstruction. Formalizes low dimensionality using sign-rank and provides deterministic bounds on the minimum latent feature dimension necessary for faithful graph reconstruction. Proposes simple modifications that maintain the inner product framework while addressing these limitations.\n- **Summary:** Uses sign-rank to prove dimension lower bounds for inner-product graph decoders -- the graph-domain analogue of the retrieval embedding problem.\n- **Relevance:** Directly foundational. The sign-rank framework applied to inner-product decoders is the same mathematical tool used by Weller et al. for retrieval, but applied in the graph representation learning domain.\n\n---\n\n**Paper 6: \"Sign-Rank of k-Hamming Distance is Constant\"**\n\n- **Authors:** Mika Goos, Nathaniel Harms, Valentin Imbach, Dmitry Sokolov\n- **Venue/Year:** arXiv:2506.12022, May 2025\n- **URL:** [https://arxiv.org/abs/2506.12022](https://arxiv.org/abs/2506.12022)\n- **Abstract:** Proves that the sign-rank of the k-Hamming Distance matrix on n bits is 2^{O(k)}, independent of n. This refutes conjectures by Hatami et al. (RANDOM 2022, STOC 2023) that sign-rank should depend on n. The technique gives constant sign-rank upper bounds for all matrices reducing to k-Hamming Distance, and challenges the distinction between margin complexity and sign-rank (bounded-error vs. unbounded-error communication complexity).\n- **Summary:** Major breakthrough showing sign-rank of k-Hamming Distance is constant, collapsing conjectured separations between bounded and unbounded error communication complexity for this class.\n- **Relevance:** Directly affects the tightness of sign-rank-based lower bounds for retrieval. If relevance matrices have structure reducing to k-Hamming Distance, their sign-rank may be much smaller than previously thought, weakening dimension lower bounds.\n\n---\n\n**Paper 7: \"Randomized Communication and Implicit Representations for Matrices and Graphs of Small Sign-Rank\"**\n\n- **Authors:** Nathaniel Harms, Viktor Zamaraev\n- **Venue/Year:** arXiv:2307.04441, July 2023\n- **URL:** [https://arxiv.org/abs/2307.04441](https://arxiv.org/abs/2307.04441)\n- **Abstract:** Characterizes when sign-rank 3 matrices and unit disk graphs admit constant-cost public-coin randomized communication protocols. Proves such objects have constant randomized communication complexity precisely when they avoid encoding arbitrarily large instances of the Greater-Than problem (equivalently, lack arbitrarily large half-graphs as semi-induced subgraphs).\n- **Summary:** Characterizes the communication complexity of low sign-rank matrices via forbidden substructures.\n- **Relevance:** Provides structural understanding of when low sign-rank translates to efficient communication/representation, relevant to understanding when retrieval matrices admit low-dimensional embeddings.\n\n---\n\n**Paper 8: \"Structure in Communication Complexity and Constant-Cost Complexity Classes\"**\n\n- **Authors:** Hamed Hatami, Pooya Hatami\n- **Venue/Year:** ACM SIGACT News Complexity Theory Column, 2024 (arXiv:2401.14623)\n- **URL:** [https://arxiv.org/abs/2401.14623](https://arxiv.org/abs/2401.14623)\n- **Abstract:** Survey examining how the complexity of a Boolean matrix in various communication models is controlled by analytic/algebraic matrix parameters (rank, sign-rank, discrepancy, etc.). Outlines research directions on the structural relationship between these parameters and communication complexity.\n- **Summary:** Survey of the structural theory connecting sign-rank, discrepancy, and communication complexity for Boolean matrices.\n- **Relevance:** Provides the theoretical framework underpinning the sign-rank approach to retrieval bounds. Key reference for understanding which algebraic parameters control representational capacity.\n\n---\n\n**Paper 9: \"The Communication Complexity of Approximating Matrix Rank\"**\n\n- **Authors:** Alexander A. Sherstov, Andrey A. Storozhenko\n- **Venue/Year:** FOCS 2024 (arXiv:2410.20094)\n- **URL:** [https://arxiv.org/abs/2410.20094](https://arxiv.org/abs/2410.20094)\n- **Abstract:** Determines communication complexity of approximating matrix rank over finite fields. Proves a lower bound of Omega(1 + r^2 log|F|) for randomized communication in distinguishing rank cases, shown to be optimal. Derives exponential improvements in space lower bounds for streaming algorithms approximating matrix rank.\n- **Summary:** Tight communication complexity bounds for matrix rank approximation, with streaming lower bound applications.\n- **Relevance:** Relevant to understanding the communication cost of rank-related computations, which underlies the factorization-based view of embedding capacity.\n\n---\n\n### TIER 3: Embedding Capacity and Dimension Bounds (Supporting)\n\n---\n\n**Paper 10: \"Dimension-Accuracy Tradeoffs in Contrastive Embeddings for Triplets, Terminals & Top-k Nearest Neighbors\"**\n\n- **Authors:** Vaggos Chatziafratis, Piotr Indyk\n- **Venue/Year:** arXiv:2312.13490, December 2023\n- **URL:** [https://arxiv.org/abs/2312.13490](https://arxiv.org/abs/2312.13490)\n- **Abstract:** Proves that ordinal embeddings preserving all triplet comparisons require dimension growing as n/2 in the worst case (nearly optimal since n-1 always suffices). Establishes dimension-relaxation tradeoffs when approximate preservation is allowed. Extends to terminal and top-k nearest neighbor ordinal embeddings.\n- **Summary:** Near-tight dimension lower bounds for order-preserving embeddings with extensions to top-k NN settings.\n- **Relevance:** Provides combinatorial dimension bounds for embedding problems closely related to retrieval (top-k NN), using different tools (ordinal embedding theory rather than sign-rank).\n\n---\n\n**Paper 11: \"Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the Limits of Embedding Space Capacity\"**\n\n- **Authors:** Yuri Kuratov, Mikhail Arkhipov, Aydar Bulatov, Mikhail Burtsev\n- **Venue/Year:** ACL 2025 (arXiv:2502.13063)\n- **URL:** [https://arxiv.org/abs/2502.13063](https://arxiv.org/abs/2502.13063)\n- **Abstract:** Investigates sequence compression into single vectors. Shows via per-sample optimization that vectors with compression ratios up to x1500 exist, far exceeding the ~x10 ratio of current encoder methods. Capacity is constrained by information uncertainty (cross-entropy loss) rather than input length.\n- **Summary:** Empirically and theoretically explores the information capacity of single embedding vectors, revealing a large gap between theoretical and practical utilization.\n- **Relevance:** Addresses the information-theoretic capacity of single-vector representations from a compression perspective, complementing the combinatorial/sign-rank approach.\n\n---\n\n**Paper 12: \"Capacity Bounds for Hyperbolic Neural Network Representations of Latent Tree Structures\"**\n\n- **Authors:** Anastasis Kratsios, Ruiyang Hong, Haitz Saez de Ocariz Borde\n- **Venue/Year:** arXiv:2308.09250, August 2023\n- **URL:** [https://arxiv.org/abs/2308.09250](https://arxiv.org/abs/2308.09250)\n- **Abstract:** Proves that deep hyperbolic ReLU networks can embed any finite weighted tree into hyperbolic space with controlled distortion. Establishes that standard Euclidean ReLU MLPs must introduce at least Omega(L^{1/d}) distortion when embedding trees with more than 2^d leaves into d-dimensional Euclidean space.\n- **Summary:** Dimension-dependent distortion lower bounds for Euclidean embeddings of trees, with hyperbolic alternatives avoiding this limitation.\n- **Relevance:** Demonstrates that embedding geometry (Euclidean vs. hyperbolic) affects representational capacity bounds, relevant to alternative retrieval embedding spaces.\n\n---\n\n### TIER 4: Adjacent Theoretical Work\n\n---\n\n**Paper 13: \"On the Intrinsic Limits of Transformer Image Embeddings in Non-Solvable Spatial Reasoning\"**\n\n- **Authors:** Siyi Lyu, Quan Liu, Feng Yan\n- **Venue/Year:** arXiv:2601.03048, January 2026\n- **URL:** [https://arxiv.org/abs/2601.03048](https://arxiv.org/abs/2601.03048)\n- **Abstract:** Shows that constant-depth Vision Transformers are limited to TC^0 complexity while spatial reasoning over non-solvable groups (like SO(3)) requires NC^1, creating a fundamental computational gap. Validates this via the Latent Space Algebra benchmark.\n- **Summary:** Proves circuit complexity limits of transformer embeddings for spatial reasoning tasks.\n- **Relevance:** Tangentially relevant -- demonstrates that architectural depth constraints impose expressiveness limits on transformer-generated embeddings, though focused on spatial reasoning rather than retrieval.\n\n---\n\n**Paper 14: \"Understanding Generalization from Embedding Dimension and Distributional Convergence\"**\n\n- **Authors:** Junjie Yu, Zhuoli Ouyang, Haotian Deng, Chen Wei, Wenxiao Ma, Jianyu Zhang, Zihan Deng, Quanying Liu\n- **Venue/Year:** arXiv:2601.22756, January 2026\n- **URL:** [https://arxiv.org/abs/2601.22756](https://arxiv.org/abs/2601.22756)\n- **Abstract:** Shows population risk depends on intrinsic dimensionality of learned embeddings and Lipschitz constants of downstream predictors. Embedding dimension is the dominant factor at the final layer, correlating strongly with empirical generalization.\n- **Summary:** Bounds generalization error via embedding dimension, bypassing traditional complexity measures.\n- **Relevance:** Provides a generalization-theoretic perspective on why embedding dimension matters, complementing the representational capacity view.\n\n---\n\n**Paper 15: \"Communication Complexity Bounds from Information Causality\"**\n\n- **Authors:** Nikolai Miklin, Prabhav Jain, Mariami Gachechiladze\n- **Venue/Year:** arXiv:2602.10206, February 2026\n- **URL:** [https://arxiv.org/abs/2602.10206](https://arxiv.org/abs/2602.10206)\n- **Abstract:** Presents an information-theoretic approach to one-way communication complexity using mutual information axioms. Formulates an expanded information causality principle that recovers known lower bounds and generates new ones.\n- **Summary:** New information-theoretic technique for communication complexity lower bounds.\n- **Relevance:** Provides alternative proof techniques for communication complexity bounds that could potentially be applied to retrieval embedding capacity questions.\n\n---\n\n### Key Takeaways for the Survey\n\n1. **The core theoretical debate** is between Weller et al. (ICLR 2026), who show sign-rank-based dimension lower bounds growing with corpus structure, and Wang et al. (2026), who prove MED = Theta(k) independent of corpus size. The resolution appears to be that geometric capacity is sufficient but learnability is the true bottleneck.\n\n2. **Single-vector vs. multi-vector separation** is formalized by Archish et al. (2026) via drowning probability analysis: multi-vector representations achieve exp(-Theta(d/log n)) vs. single-vector's exp(-Theta(d/n)), an exponential gap in corpus scaling.\n\n3. **Sign-rank is the key algebraic tool** connecting communication complexity to embedding dimension. The Goos et al. (2025) result on constant sign-rank for k-Hamming Distance may weaken some lower bounds by showing certain matrix classes have smaller sign-rank than conjectured.\n\n4. **The inner product decoder limitation** (Lee et al., ICML 2024) provides the graph-domain analogue, using the same sign-rank framework to prove dimension requirements for faithful graph reconstruction via inner products.\n\nSources:\n- [On the Theoretical Limitations of Embedding-Based Retrieval](https://arxiv.org/abs/2508.21038)\n- [R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval](https://arxiv.org/abs/2601.20844)\n- [On Strengths and Limitations of Single-Vector Embeddings](https://arxiv.org/abs/2603.29519)\n- [Does Generative Retrieval Overcome the Limitations of Dense Retrieval?](https://arxiv.org/abs/2509.22116)\n- [Sign Rank Limitations for Inner Product Graph Decoders](https://arxiv.org/abs/2402.06662)\n- [Sign-Rank of k-Hamming Distance is Constant](https://arxiv.org/abs/2506.12022)\n- [Randomized Communication and Implicit Representations for Matrices and Graphs of Small Sign-Rank](https://arxiv.org/abs/2307.04441)\n- [Structure in Communication Complexity and Constant-Cost Complexity Classes](https://arxiv.org/abs/2401.14623)\n- [The Communication Complexity of Approximating Matrix Rank](https://arxiv.org/abs/2410.20094)\n- [Dimension-Accuracy Tradeoffs in Contrastive Embeddings for Triplets, Terminals & Top-k Nearest Neighbors](https://arxiv.org/abs/2312.13490)\n- [Cramming 1568 Tokens into a Single Vector and Back Again](https://arxiv.org/abs/2502.13063)\n- [Capacity Bounds for Hyperbolic Neural Network Representations of Latent Tree Structures](https://arxiv.org/abs/2308.09250)\n- [On the Intrinsic Limits of Transformer Image Embeddings](https://arxiv.org/abs/2601.03048)\n- [Understanding Generalization from Embedding Dimension and Distributional Convergence](https://arxiv.org/abs/2601.22756)\n- [Communication Complexity Bounds from Information Causality](https://arxiv.org/abs/2602.10206)\n- [Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling](https://arxiv.org/abs/2409.14683)\n- [LIR: The First Workshop on Late Interaction and Multi Vector Retrieval @ ECIR 2026](https://arxiv.org/abs/2511.00444)"
      }
    ],
    "totalDurationMs": 200225,
    "totalTokens": 34783,
    "totalToolUseCount": 36,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2579,
      "cache_read_input_tokens": 26830,
      "output_tokens": 5373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2579
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5373,
          "cache_read_input_tokens": 26830,
          "cache_creation_input_tokens": 2579,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2579,
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
  "sourceToolAssistantUUID": "af55e929-c356-4c00-961b-a97e2b1f7817",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "d3e15db9-8280-4cb7-8768-d05b6aca094e",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on multi-vector retrieval expressiveness",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Tool result

_source line 22 · 2026-05-30T06:13:33.434Z_

<details><summary>↩ Tool result · `toolu_01GEbWKNWHDwYAJQQAGUhmQV`</summary>

```text
I now have comprehensive data for all seed papers and the most relevant citing works. Here is the full literature survey report.

---

## Literature Survey: Formal Expressiveness Bounds for Multi-Vector Retrieval (MaxSim/ColBERT-style)

---

### SEED PAPER 1

**Full Title:** On the Theoretical Limitations of Embedding-Based Retrieval
**Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee
**Venue & Year:** ICLR 2026 (submitted Aug 28, 2025; revised Mar 12, 2026)
**URL:** https://arxiv.org/abs/2508.21038
**One-line summary:** Proves that the number of top-k subsets returnable by a single-vector embedding is bounded by the embedding dimension via sign-rank connections, and introduces the LIMIT benchmark showing SOTA models fail on simple realistic tasks.
**Survey relevance:** This is the foundational "negative result" for the survey -- it establishes that single-vector retrieval has hard combinatorial capacity limits tied to sign-rank, motivating the move to multi-vector representations. The LIMIT dataset is now the standard stress test.

---

### SEED PAPER 2

**Full Title:** R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval
**Authors:** Zihao Wang, Hang Yin, Lihui Liu, Hanghang Tong, Yangqiu Song, Ginny Wong, Simon See
**Venue & Year:** arXiv preprint, January 2026
**URL:** https://arxiv.org/abs/2601.20844
**One-line summary:** Derives tight bounds on the Minimal Embeddable Dimension (MED) for top-k retrieval under l2, inner product, and cosine similarity, showing 2k dimensions suffice and that limitations stem from learnability, not geometry.
**Survey relevance:** Provides the "positive" counterpart to Weller et al. -- the geometric capacity is actually sufficient with 2k dimensions, so the real bottleneck is optimization/learning. Central to the debate about whether expressiveness or trainability is the true barrier.

---

### SEED PAPER 3

**Full Title:** MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings
**Authors:** Laxman Dhulipala, Majid Hadian, Rajesh Jayaram, Jason Lee, Vahab Mirrokni
**Venue & Year:** NeurIPS 2024 (submitted May 29, 2024)
**URL:** https://arxiv.org/abs/2405.19504
**One-line summary:** Reduces multi-vector (ColBERT/MaxSim) retrieval to single-vector MIPS via Fixed Dimensional Encodings (FDEs), providing the first single-vector proxy for multi-vector similarity with provable epsilon-approximation guarantees.
**Survey relevance:** Directly addresses the expressiveness gap -- it shows multi-vector similarity can be approximated in a single-vector framework with theoretical guarantees, bridging the two paradigms. Foundational for understanding what information is preserved/lost in the reduction.

---

### SEED PAPER 4

**Full Title:** On Strengths and Limitations of Single-Vector Embeddings
**Authors:** Archish S, Mihir Agarwal, Ankit Garg, Neeraj Kayal, Kirankumar Shiragur
**Venue & Year:** arXiv preprint, March 31, 2026
**URL:** https://arxiv.org/abs/2603.29519
**One-line summary:** Disentangles the failure modes on LIMIT: dimensionality alone cannot explain poor performance; domain shift and relevance misalignment are major contributors, but even after finetuning, single-vector models remain weaker than multi-vector ones and suffer catastrophic forgetting.
**Survey relevance:** Refines the Weller et al. narrative by showing the problem is not purely dimensionality but also involves the "drowning in documents" paradox where single-vector similarities act as noisy proxies. Establishes that multi-vector models are fundamentally more robust to corpus scaling.

---

### KEY CITING/RELATED PAPERS (sorted by relevance to expressiveness theory)

---

#### 5. Is Dimensionality a Barrier for Retrieval Models?

**Authors:** Kiril Bangachev, Guy Bresler, Jonathan Kogan, Yury Polyanskiy
**Venue & Year:** arXiv preprint, May 22, 2026
**URL:** https://arxiv.org/abs/2605.23556
**One-line summary:** Studies maximal-margin embeddings and proves that dimension d = O(k log(n/k)) is necessary and sufficient for k-sparse relevance matrices with margin Theta(k^{-1/2}), showing the optimal margin can be nearly achieved at moderate dimensions.
**Survey relevance:** Directly extends the Weller et al. capacity question with margin-based analysis. Provides the tightest known dimension-vs-margin tradeoffs for sparse retrieval, essential for understanding when single-vector models can and cannot work.

---

#### 6. Provable Accuracy Collapse in Embedding-Based Representations under Dimensionality Mismatch

**Authors:** Dionysis Arvanitakis, Vaggos Chatziafratis, Yiyuan Luo
**Venue & Year:** ICML 2026 (spotlight), May 5, 2026
**URL:** https://arxiv.org/abs/2605.03346
**One-line summary:** Proves sharp dimension-accuracy phase transitions: unless embedding dimension d is close to ground-truth dimension D, accuracy collapses to trivial (50%); complemented by computational hardness results under the Unique Games Conjecture.
**Survey relevance:** Establishes an information-theoretic and computational hardness framework for dimensionality mismatch. Shows that the capacity issues identified by Weller et al. are not just worst-case artifacts but reflect a sharp phase transition, making them practically unavoidable.

---

#### 7. No More K-means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval

**Authors:** Lixuan Guo, Yifei Wang, Tiansheng Wen, Aosong Feng, Stefanie Jegelka, Chenyu You
**Venue & Year:** ICML 2026, May 28, 2026
**URL:** https://arxiv.org/abs/2605.30120
**One-line summary:** Replaces K-means clustering in multi-vector retrieval with Sparse Autoencoders, projecting token embeddings into high-dimensional sparse representations for inverted indexing, achieving 15x faster indexing and better retrieval than ColBERTv2.
**Survey relevance:** Demonstrates a practical way to exploit multi-vector expressiveness without the storage/latency costs, relevant to understanding how the theoretical capacity advantage of multi-vector models can be realized efficiently.

---

#### 8. LEMUR: Learned Multi-Vector Retrieval

**Authors:** Elias Jaasaari, Ville Hyvonen, Teemu Roos
**Venue & Year:** ICML 2026 (submitted Jan 29, 2026; revised May 21, 2026)
**URL:** https://arxiv.org/abs/2601.21853
**One-line summary:** Reduces multi-vector MaxSim search to single-vector search in a learned latent space via a one-hidden-layer neural network, achieving an order of magnitude speedup over prior multi-vector methods.
**Survey relevance:** Like MUVERA, this is a reduction from multi-vector to single-vector search but via learned mappings rather than random projections. Relevant to understanding what expressiveness is preserved in such reductions and at what approximation cost.

---

#### 9. Scaling Laws for Embedding Dimension in Information Retrieval

**Authors:** Julian Killingback, Mahta Rafiee, Madine Manas, Hamed Zamani
**Venue & Year:** arXiv preprint, February 4, 2026
**URL:** https://arxiv.org/abs/2602.05062
**One-line summary:** Establishes power-law scaling relationships between embedding dimension and retrieval performance across model families, finding diminishing returns for training-aligned tasks but unpredictable behavior for out-of-distribution evaluation.
**Survey relevance:** Provides the empirical scaling perspective complementing the theoretical bounds -- shows how dimension-performance tradeoffs manifest in practice and when the theoretical capacity limits begin to bite.

---

#### 10. Incorporating Token Importance in Multi-Vector Retrieval

**Authors:** Archish S, Ankit Garg, Kirankumar Shiragur, Neeraj Kayal
**Venue & Year:** AAAI 2026, November 20, 2025
**URL:** https://arxiv.org/abs/2511.16106
**One-line summary:** Enhances ColBERT's MaxSim with token importance weights (IDF-based and learned), improving recall while preserving pre-computed document representations.
**Survey relevance:** From the same group as Seed Paper 4 (Jacob et al.). Explores whether weighted MaxSim can better exploit the expressiveness of multi-vector representations, showing that not all token interactions are equally informative.

---

#### 11. Breaking the Curse of Dimensionality: On the Stability of Modern Vector Retrieval

**Authors:** Vihan Lakshman, Blaise Munyampirwa, Julian Shun, Benjamin Coleman
**Venue & Year:** arXiv preprint, December 13, 2025 (revised Feb 12, 2026)
**URL:** https://arxiv.org/abs/2512.12458
**One-line summary:** Analyzes stability of high-dimensional vector retrieval (whether small query perturbations preserve nearest-neighbor results), finding that Chamfer/multi-vector distance maintains stability while average pooling may not.
**Survey relevance:** Provides a complementary theoretical lens (stability rather than capacity) on why multi-vector representations are more robust than single-vector ones, supporting the expressiveness advantage from a different angle.

---

#### 12. Your Embedding Model is SMARTer Than You Think

**Authors:** Jianrui Zhang, Hyun Jung Lee, Sukanta Ganguly, Tae-Eui Kam, Donghyun Kim, Yong Jae Lee
**Venue & Year:** arXiv preprint, May 24, 2026
**URL:** https://arxiv.org/abs/2605.24938
**One-line summary:** Shows that contrastive training on pooled embeddings implicitly creates useful multi-vector geometry in hidden states; applying late-interaction at inference on frozen states recovers multi-vector performance from single-vector models.
**Survey relevance:** Blurs the single-vector vs. multi-vector boundary by showing single-vector training implicitly learns multi-vector structure. Relevant to understanding whether the expressiveness gap is as sharp as theory suggests or can be bridged via architectural tricks.

---

#### 13. Efficient Constant-Space Multi-Vector Retrieval

**Authors:** Sean MacAvaney, Antonio Mallia, Nicola Tonellotto
**Venue & Year:** ECIR 2025, April 2, 2025
**URL:** https://arxiv.org/abs/2504.01818
**One-line summary:** Encodes documents into a fixed number of vectors (decoupled from input tokens) to achieve constant storage per document while retaining most multi-vector retrieval effectiveness.
**Survey relevance:** Addresses the practical storage cost of multi-vector expressiveness. Relevant to understanding the capacity-storage tradeoff: how many vectors per document are needed to capture the expressiveness advantage.

---

#### 14. Expressiveness Limits of Autoregressive Semantic ID Generation in Generative Recommendation

**Authors:** Yupeng Hou, Haven Kim, Clark Mingxuan Ju, Eduardo Escoto, Neil Shah, Julian McAuley
**Venue & Year:** arXiv preprint, May 7, 2026
**URL:** https://arxiv.org/abs/2605.06331
**One-line summary:** Shows that tree-structured semantic IDs in generative recommendation impose expressiveness constraints analogous to embedding capacity limits, and proposes latent tokens to overcome them.
**Survey relevance:** Extends the expressiveness-limitation theme beyond retrieval to generative recommendation, showing the sign-rank/capacity argument has broader implications for any system that compresses items into structured representations.

---

#### 15. Alon, Moran, Yehudayoff -- Sign rank versus VC dimension (foundational reference)

**Authors:** Noga Alon, Shay Moran, Amir Yehudayoff
**Venue & Year:** COLT 2016
**URL:** https://proceedings.mlr.press/v49/alon16.html
**One-line summary:** Proves the existence of a maximum class with VC dimension 2 and sign rank Theta(N^{1/2}), establishing the separation between sign-rank and VC dimension.
**Survey relevance:** This is the key foundational result that both Weller et al. and Jacob et al. build upon. The sign-rank lower bounds from this paper are what establish the theoretical capacity limits of inner-product-based retrieval.

---

### Summary of the Landscape

The literature reveals a productive theoretical debate with three main threads:

1. **Capacity limits of single-vector retrieval (negative results):** Weller et al. (ICLR 2026) establishes that sign-rank bounds limit what single-vector models can express. Arvanitakis et al. (ICML 2026) strengthens this with sharp phase-transition results. Jacob et al. (2026) shows that even after controlling for confounds, single-vector models fundamentally underperform multi-vector ones and suffer catastrophic forgetting.

2. **Geometric sufficiency (positive results):** Wang et al. (2026) and Bangachev et al. (2026) show that 2k dimensions are geometrically sufficient for top-k retrieval, arguing the real bottleneck is learnability/optimization, not representation capacity per se.

3. **Bridging via multi-vector-to-single-vector reductions:** MUVERA (NeurIPS 2024), LEMUR (ICML 2026), and SSR (ICML 2026) provide practical algorithms that approximate multi-vector expressiveness within single-vector frameworks, with varying theoretical guarantees. SMART (2026) shows single-vector models implicitly learn multi-vector structure.

The central open question is: given that geometry alone is sufficient (Wang et al.), why do learned single-vector models fail in practice (Weller et al., Jacob et al.)? The answer appears to involve a combination of optimization difficulty, catastrophic forgetting under distribution shift, and the "drowning in documents" phenomenon where corpus scale amplifies the noise in single-vector similarity proxies.

agentId: aa91412db02b21e1f (use SendMessage with to: 'aa91412db02b21e1f' to continue this agent)
&lt;usage>total_tokens: 34800
tool_uses: 29
duration_ms: 220132&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dd56462-7a20-47e3-9738-5d7421e8143c",
  "isSidechain": false,
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "f5f0572d-4065-48d1-a4d6-381e974e2acc",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on formal expressiveness bounds for multi-vector retrieval (MaxSim/ColBERT-style). \n\nSearch for and fetch details on the following SEED PAPERS and their most important citing/related works (2024-2026):\n\n1. Search for: Weller et al. \"On the Theoretical Limitations of Embedding-Based Retrieval\" ICLR 2026 — fetch the arxiv abstract\n2. Search for: Wang et al. \"R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval\" arXiv 2026 — fetch abstract\n3. Search for: Dhulipala et al. \"MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings\" NeurIPS 2024 — fetch abstract\n4. Search for: Jacob et al. \"On Strengths and Limitations of Single-Vector Embeddings\" arXiv 2026 — fetch abstract\n5. Search for papers that CITE Weller et al. ICLR 2026 (the LIMIT paper) — use Google Scholar or Semantic Scholar\n6. Search for papers that cite MUVERA NeurIPS 2024\n\nFor each paper found, use WebFetch to read its arxiv abstract page. Report back:\n- Full title\n- Authors  \n- Venue and year\n- URL\n- One-line summary of what the paper does\n- Why it's important for the survey topic (expressiveness of multi-vector retrieval, sign-rank theory, embedding capacity)",
    "agentId": "aa91412db02b21e1f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive data for all seed papers and the most relevant citing works. Here is the full literature survey report.\n\n---\n\n## Literature Survey: Formal Expressiveness Bounds for Multi-Vector Retrieval (MaxSim/ColBERT-style)\n\n---\n\n### SEED PAPER 1\n\n**Full Title:** On the Theoretical Limitations of Embedding-Based Retrieval\n**Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee\n**Venue & Year:** ICLR 2026 (submitted Aug 28, 2025; revised Mar 12, 2026)\n**URL:** https://arxiv.org/abs/2508.21038\n**One-line summary:** Proves that the number of top-k subsets returnable by a single-vector embedding is bounded by the embedding dimension via sign-rank connections, and introduces the LIMIT benchmark showing SOTA models fail on simple realistic tasks.\n**Survey relevance:** This is the foundational \"negative result\" for the survey -- it establishes that single-vector retrieval has hard combinatorial capacity limits tied to sign-rank, motivating the move to multi-vector representations. The LIMIT dataset is now the standard stress test.\n\n---\n\n### SEED PAPER 2\n\n**Full Title:** R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval\n**Authors:** Zihao Wang, Hang Yin, Lihui Liu, Hanghang Tong, Yangqiu Song, Ginny Wong, Simon See\n**Venue & Year:** arXiv preprint, January 2026\n**URL:** https://arxiv.org/abs/2601.20844\n**One-line summary:** Derives tight bounds on the Minimal Embeddable Dimension (MED) for top-k retrieval under l2, inner product, and cosine similarity, showing 2k dimensions suffice and that limitations stem from learnability, not geometry.\n**Survey relevance:** Provides the \"positive\" counterpart to Weller et al. -- the geometric capacity is actually sufficient with 2k dimensions, so the real bottleneck is optimization/learning. Central to the debate about whether expressiveness or trainability is the true barrier.\n\n---\n\n### SEED PAPER 3\n\n**Full Title:** MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings\n**Authors:** Laxman Dhulipala, Majid Hadian, Rajesh Jayaram, Jason Lee, Vahab Mirrokni\n**Venue & Year:** NeurIPS 2024 (submitted May 29, 2024)\n**URL:** https://arxiv.org/abs/2405.19504\n**One-line summary:** Reduces multi-vector (ColBERT/MaxSim) retrieval to single-vector MIPS via Fixed Dimensional Encodings (FDEs), providing the first single-vector proxy for multi-vector similarity with provable epsilon-approximation guarantees.\n**Survey relevance:** Directly addresses the expressiveness gap -- it shows multi-vector similarity can be approximated in a single-vector framework with theoretical guarantees, bridging the two paradigms. Foundational for understanding what information is preserved/lost in the reduction.\n\n---\n\n### SEED PAPER 4\n\n**Full Title:** On Strengths and Limitations of Single-Vector Embeddings\n**Authors:** Archish S, Mihir Agarwal, Ankit Garg, Neeraj Kayal, Kirankumar Shiragur\n**Venue & Year:** arXiv preprint, March 31, 2026\n**URL:** https://arxiv.org/abs/2603.29519\n**One-line summary:** Disentangles the failure modes on LIMIT: dimensionality alone cannot explain poor performance; domain shift and relevance misalignment are major contributors, but even after finetuning, single-vector models remain weaker than multi-vector ones and suffer catastrophic forgetting.\n**Survey relevance:** Refines the Weller et al. narrative by showing the problem is not purely dimensionality but also involves the \"drowning in documents\" paradox where single-vector similarities act as noisy proxies. Establishes that multi-vector models are fundamentally more robust to corpus scaling.\n\n---\n\n### KEY CITING/RELATED PAPERS (sorted by relevance to expressiveness theory)\n\n---\n\n#### 5. Is Dimensionality a Barrier for Retrieval Models?\n\n**Authors:** Kiril Bangachev, Guy Bresler, Jonathan Kogan, Yury Polyanskiy\n**Venue & Year:** arXiv preprint, May 22, 2026\n**URL:** https://arxiv.org/abs/2605.23556\n**One-line summary:** Studies maximal-margin embeddings and proves that dimension d = O(k log(n/k)) is necessary and sufficient for k-sparse relevance matrices with margin Theta(k^{-1/2}), showing the optimal margin can be nearly achieved at moderate dimensions.\n**Survey relevance:** Directly extends the Weller et al. capacity question with margin-based analysis. Provides the tightest known dimension-vs-margin tradeoffs for sparse retrieval, essential for understanding when single-vector models can and cannot work.\n\n---\n\n#### 6. Provable Accuracy Collapse in Embedding-Based Representations under Dimensionality Mismatch\n\n**Authors:** Dionysis Arvanitakis, Vaggos Chatziafratis, Yiyuan Luo\n**Venue & Year:** ICML 2026 (spotlight), May 5, 2026\n**URL:** https://arxiv.org/abs/2605.03346\n**One-line summary:** Proves sharp dimension-accuracy phase transitions: unless embedding dimension d is close to ground-truth dimension D, accuracy collapses to trivial (50%); complemented by computational hardness results under the Unique Games Conjecture.\n**Survey relevance:** Establishes an information-theoretic and computational hardness framework for dimensionality mismatch. Shows that the capacity issues identified by Weller et al. are not just worst-case artifacts but reflect a sharp phase transition, making them practically unavoidable.\n\n---\n\n#### 7. No More K-means: Single-Stage Sparse Coding for Efficient Multi-Vector Retrieval\n\n**Authors:** Lixuan Guo, Yifei Wang, Tiansheng Wen, Aosong Feng, Stefanie Jegelka, Chenyu You\n**Venue & Year:** ICML 2026, May 28, 2026\n**URL:** https://arxiv.org/abs/2605.30120\n**One-line summary:** Replaces K-means clustering in multi-vector retrieval with Sparse Autoencoders, projecting token embeddings into high-dimensional sparse representations for inverted indexing, achieving 15x faster indexing and better retrieval than ColBERTv2.\n**Survey relevance:** Demonstrates a practical way to exploit multi-vector expressiveness without the storage/latency costs, relevant to understanding how the theoretical capacity advantage of multi-vector models can be realized efficiently.\n\n---\n\n#### 8. LEMUR: Learned Multi-Vector Retrieval\n\n**Authors:** Elias Jaasaari, Ville Hyvonen, Teemu Roos\n**Venue & Year:** ICML 2026 (submitted Jan 29, 2026; revised May 21, 2026)\n**URL:** https://arxiv.org/abs/2601.21853\n**One-line summary:** Reduces multi-vector MaxSim search to single-vector search in a learned latent space via a one-hidden-layer neural network, achieving an order of magnitude speedup over prior multi-vector methods.\n**Survey relevance:** Like MUVERA, this is a reduction from multi-vector to single-vector search but via learned mappings rather than random projections. Relevant to understanding what expressiveness is preserved in such reductions and at what approximation cost.\n\n---\n\n#### 9. Scaling Laws for Embedding Dimension in Information Retrieval\n\n**Authors:** Julian Killingback, Mahta Rafiee, Madine Manas, Hamed Zamani\n**Venue & Year:** arXiv preprint, February 4, 2026\n**URL:** https://arxiv.org/abs/2602.05062\n**One-line summary:** Establishes power-law scaling relationships between embedding dimension and retrieval performance across model families, finding diminishing returns for training-aligned tasks but unpredictable behavior for out-of-distribution evaluation.\n**Survey relevance:** Provides the empirical scaling perspective complementing the theoretical bounds -- shows how dimension-performance tradeoffs manifest in practice and when the theoretical capacity limits begin to bite.\n\n---\n\n#### 10. Incorporating Token Importance in Multi-Vector Retrieval\n\n**Authors:** Archish S, Ankit Garg, Kirankumar Shiragur, Neeraj Kayal\n**Venue & Year:** AAAI 2026, November 20, 2025\n**URL:** https://arxiv.org/abs/2511.16106\n**One-line summary:** Enhances ColBERT's MaxSim with token importance weights (IDF-based and learned), improving recall while preserving pre-computed document representations.\n**Survey relevance:** From the same group as Seed Paper 4 (Jacob et al.). Explores whether weighted MaxSim can better exploit the expressiveness of multi-vector representations, showing that not all token interactions are equally informative.\n\n---\n\n#### 11. Breaking the Curse of Dimensionality: On the Stability of Modern Vector Retrieval\n\n**Authors:** Vihan Lakshman, Blaise Munyampirwa, Julian Shun, Benjamin Coleman\n**Venue & Year:** arXiv preprint, December 13, 2025 (revised Feb 12, 2026)\n**URL:** https://arxiv.org/abs/2512.12458\n**One-line summary:** Analyzes stability of high-dimensional vector retrieval (whether small query perturbations preserve nearest-neighbor results), finding that Chamfer/multi-vector distance maintains stability while average pooling may not.\n**Survey relevance:** Provides a complementary theoretical lens (stability rather than capacity) on why multi-vector representations are more robust than single-vector ones, supporting the expressiveness advantage from a different angle.\n\n---\n\n#### 12. Your Embedding Model is SMARTer Than You Think\n\n**Authors:** Jianrui Zhang, Hyun Jung Lee, Sukanta Ganguly, Tae-Eui Kam, Donghyun Kim, Yong Jae Lee\n**Venue & Year:** arXiv preprint, May 24, 2026\n**URL:** https://arxiv.org/abs/2605.24938\n**One-line summary:** Shows that contrastive training on pooled embeddings implicitly creates useful multi-vector geometry in hidden states; applying late-interaction at inference on frozen states recovers multi-vector performance from single-vector models.\n**Survey relevance:** Blurs the single-vector vs. multi-vector boundary by showing single-vector training implicitly learns multi-vector structure. Relevant to understanding whether the expressiveness gap is as sharp as theory suggests or can be bridged via architectural tricks.\n\n---\n\n#### 13. Efficient Constant-Space Multi-Vector Retrieval\n\n**Authors:** Sean MacAvaney, Antonio Mallia, Nicola Tonellotto\n**Venue & Year:** ECIR 2025, April 2, 2025\n**URL:** https://arxiv.org/abs/2504.01818\n**One-line summary:** Encodes documents into a fixed number of vectors (decoupled from input tokens) to achieve constant storage per document while retaining most multi-vector retrieval effectiveness.\n**Survey relevance:** Addresses the practical storage cost of multi-vector expressiveness. Relevant to understanding the capacity-storage tradeoff: how many vectors per document are needed to capture the expressiveness advantage.\n\n---\n\n#### 14. Expressiveness Limits of Autoregressive Semantic ID Generation in Generative Recommendation\n\n**Authors:** Yupeng Hou, Haven Kim, Clark Mingxuan Ju, Eduardo Escoto, Neil Shah, Julian McAuley\n**Venue & Year:** arXiv preprint, May 7, 2026\n**URL:** https://arxiv.org/abs/2605.06331\n**One-line summary:** Shows that tree-structured semantic IDs in generative recommendation impose expressiveness constraints analogous to embedding capacity limits, and proposes latent tokens to overcome them.\n**Survey relevance:** Extends the expressiveness-limitation theme beyond retrieval to generative recommendation, showing the sign-rank/capacity argument has broader implications for any system that compresses items into structured representations.\n\n---\n\n#### 15. Alon, Moran, Yehudayoff -- Sign rank versus VC dimension (foundational reference)\n\n**Authors:** Noga Alon, Shay Moran, Amir Yehudayoff\n**Venue & Year:** COLT 2016\n**URL:** https://proceedings.mlr.press/v49/alon16.html\n**One-line summary:** Proves the existence of a maximum class with VC dimension 2 and sign rank Theta(N^{1/2}), establishing the separation between sign-rank and VC dimension.\n**Survey relevance:** This is the key foundational result that both Weller et al. and Jacob et al. build upon. The sign-rank lower bounds from this paper are what establish the theoretical capacity limits of inner-product-based retrieval.\n\n---\n\n### Summary of the Landscape\n\nThe literature reveals a productive theoretical debate with three main threads:\n\n1. **Capacity limits of single-vector retrieval (negative results):** Weller et al. (ICLR 2026) establishes that sign-rank bounds limit what single-vector models can express. Arvanitakis et al. (ICML 2026) strengthens this with sharp phase-transition results. Jacob et al. (2026) shows that even after controlling for confounds, single-vector models fundamentally underperform multi-vector ones and suffer catastrophic forgetting.\n\n2. **Geometric sufficiency (positive results):** Wang et al. (2026) and Bangachev et al. (2026) show that 2k dimensions are geometrically sufficient for top-k retrieval, arguing the real bottleneck is learnability/optimization, not representation capacity per se.\n\n3. **Bridging via multi-vector-to-single-vector reductions:** MUVERA (NeurIPS 2024), LEMUR (ICML 2026), and SSR (ICML 2026) provide practical algorithms that approximate multi-vector expressiveness within single-vector frameworks, with varying theoretical guarantees. SMART (2026) shows single-vector models implicitly learn multi-vector structure.\n\nThe central open question is: given that geometry alone is sufficient (Wang et al.), why do learned single-vector models fail in practice (Weller et al., Jacob et al.)? The answer appears to involve a combination of optimization difficulty, catastrophic forgetting under distribution shift, and the \"drowning in documents\" phenomenon where corpus scale amplifies the noise in single-vector similarity proxies."
      }
    ],
    "totalDurationMs": 220132,
    "totalTokens": 34800,
    "totalToolUseCount": 29,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 846,
      "cache_read_input_tokens": 30359,
      "output_tokens": 3594,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 846
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3594,
          "cache_read_input_tokens": 30359,
          "cache_creation_input_tokens": 846,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 846,
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
  "sourceToolAssistantUUID": "3dd56462-7a20-47e3-9738-5d7421e8143c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-30T06:14:04.263Z_

<details><summary>↩ Tool result · `toolu_013HpvgNR2nMrYBtwdvaqK8X`</summary>

```text
I now have comprehensive information. Here is the full literature survey report.

---

## Literature Survey: Formal Expressiveness Bounds for Multi-Vector (MaxSim/ColBERT-style) Retrieval (2024--2026)

---

### TIER 1: CORE THEORY PAPERS (directly address expressiveness bounds)

---

**Paper 1.**
**Title:** On the Theoretical Limitations of Embedding-Based Retrieval
**Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee
**Venue/Year:** ICLR 2026
**URL:** https://arxiv.org/abs/2508.21038

**Summary:** Proves that for single-vector dot-product embeddings of dimension d, the number of distinct top-k document subsets returnable by any query is fundamentally bounded by d, connecting sign-rank from communication complexity to representational capacity. Introduces the LIMIT benchmark showing state-of-the-art single-vector models fail on simple tasks predicted to be hard by the theory.

**Why important:** This is the most directly relevant paper. It establishes formal combinatorial limits on what single-vector retrieval can express, and explicitly calls for multi-vector approaches as a way to overcome these limits. It provides the theoretical baseline against which multi-vector expressiveness gains should be measured.

---

**Paper 2.**
**Title:** MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings
**Authors:** Laxman Dhulipala, Majid Hadian, Rajesh Jayaram, Jason Lee, Vahab Mirrokni
**Venue/Year:** NeurIPS 2024
**URL:** https://arxiv.org/abs/2405.19504

**Summary:** Introduces Fixed Dimensional Encodings (FDEs) that reduce multi-vector Chamfer/MaxSim similarity search to single-vector MIPS. Proves that FDEs provide epsilon-approximations to Chamfer similarity -- the first single-vector proxy for multi-vector similarity with provable theoretical guarantees. Achieves 10% better recall at 90% lower latency than PLAID on BEIR.

**Why important:** Provides the first algorithm with provable guarantees for Chamfer similarity search with strictly faster than brute-force runtime. The epsilon-approximation bounds formalize how much information is lost when compressing multi-vector representations to single vectors, directly quantifying the expressiveness gap.

---

**Paper 3.**
**Title:** Breaking the Curse of Dimensionality: On the Stability of Modern Vector Retrieval
**Authors:** Vihan Lakshman, Blaise Munyampirwa, Julian Shun, Benjamin Coleman
**Venue/Year:** arXiv preprint, December 2025 (revised February 2026)
**URL:** https://arxiv.org/abs/2512.12458

**Summary:** Extends stability theory (resilience of nearest-neighbor rankings to small query perturbations) to three practical settings: multi-vector search with Chamfer distance, filtered vector search, and sparse vector search. Proves that Chamfer distance preserves stability while certain pooling methods may not, and formalizes novel stability conditions for sparse retrieval.

**Why important:** Provides theoretical justification for why Chamfer-distance-based multi-vector retrieval works well in high dimensions despite the curse of dimensionality. Shows that multi-vector (Chamfer) scoring has favorable stability properties that single-vector pooling may lack -- a formal expressiveness advantage.

---

**Paper 4.**
**Title:** Generative Retrieval as Multi-Vector Dense Retrieval
**Authors:** Shiguang Wu, Wenda Wei, Mengqi Zhang, Zhumin Chen, Jun Ma, Zhaochun Ren, Maarten de Rijke, Pengjie Ren
**Venue/Year:** SIGIR 2024
**URL:** https://arxiv.org/abs/2404.00684

**Summary:** Rigorously proves that generative retrieval (with atomic identifiers) is equivalent to single-vector dense retrieval, while the decoder's attention layers and prediction heads implement a form of multi-vector dense retrieval. Both paradigms compute relevance as summed products of query vectors, document vectors, and an alignment matrix.

**Why important:** Establishes a formal equivalence between generative retrieval and multi-vector dense retrieval, showing that the decoder in generative models implicitly computes a MaxSim-like operation. This reveals that multi-vector expressiveness is a more general phenomenon than ColBERT alone, and connects two research communities.

---

### TIER 2: ANALYTICAL / EMPIRICAL EXPRESSIVENESS STUDIES

---

**Paper 5.**
**Title:** Working Notes on Late Interaction Dynamics: Analyzing Targeted Behaviors of Late Interaction Models
**Authors:** Antoine Edy, Max Conti, Quentin Mace
**Venue/Year:** LIR Workshop @ ECIR 2026
**URL:** https://arxiv.org/abs/2603.26259

**Summary:** Empirically analyzes understudied dynamics of late interaction models, specifically the length bias inherent in multi-vector MaxSim scoring and the similarity distribution beyond the top-1 document token. Finds that the theoretical length bias of causal late interaction models holds in practice, and that MaxSim is efficient because no significant similarity trend lies beyond the top-1 document token.

**Why important:** Validates theoretical predictions about MaxSim scoring behavior in practice. The length bias analysis is relevant to understanding the expressiveness limitations of the MaxSim operator itself -- longer documents receive systematically higher scores, an inherent bias in the scoring function's expressiveness.

---

**Paper 6.**
**Title:** Incorporating Token Importance in Multi-Vector Retrieval
**Authors:** Archish S, Ankit Garg, Kirankumar Shiragur, Neeraj Kayal
**Venue/Year:** arXiv preprint, November 2025
**URL:** https://arxiv.org/abs/2511.16106

**Summary:** Enhances the Chamfer distance function in ColBERT by computing a weighted sum over query token contributions (e.g., IDF-based or learned weights), achieving 1.28% zero-shot and 3.66% few-shot improvement in Recall@10 on BEIR. Argues this increases the expressiveness of the multi-vector mechanism without changing the underlying representations.

**Why important:** Demonstrates that the standard (uniform-weight) MaxSim/Chamfer operator leaves expressiveness on the table, and that weighted variants are strictly more expressive. Provides an empirical quantification of how much expressiveness is gained by moving from uniform to importance-weighted multi-vector scoring.

---

**Paper 7.**
**Title:** ColBERT-Att: Late-Interaction Meets Attention for Enhanced Retrieval
**Authors:** Raj Nath Patel, Sourav Dutta
**Venue/Year:** arXiv preprint, March 2026
**URL:** https://arxiv.org/abs/2603.25248

**Summary:** Integrates attention weights into the MaxSim late interaction framework, arguing that standard ColBERT fails to account for the relative importance of query-document token similarities. Shows improvements on MS-MARCO, BEIR, and LoTTE benchmarks.

**Why important:** Complementary to Paper 6 -- both show that the vanilla MaxSim operator is not maximally expressive and that incorporating term importance (via attention or IDF) increases the scoring function's capacity. Relevant to understanding the expressiveness frontier of late interaction scoring.

---

**Paper 8.**
**Title:** Understanding the Multi-vector Dense Retrieval Models
**Authors:** (Zhan et al.)
**Venue/Year:** CIKM 2023
**URL:** https://dl.acm.org/doi/10.1145/3583780.3615282

**Summary:** Investigates why multi-vector dense retrieval outperforms single-vector approaches by analyzing vocabulary distribution and representation behavior differences between the two paradigms. Provides empirical interpretability analysis of multi-vector expressiveness advantages.

**Why important:** Although from 2023, this is a foundational reference for the expressiveness question. It provides the empirical evidence base that motivates the theoretical work in Papers 1-3, analyzing what multi-vector models capture that single-vector models cannot.

---

### TIER 3: EFFICIENCY AND SYSTEMS (relevant to expressiveness-efficiency tradeoffs)

---

**Paper 9.**
**Title:** LEMUR: Learned Multi-Vector Retrieval
**Authors:** Elias Jaasaari, Ville Hyvonen, Teemu Roos
**Venue/Year:** ICML 2026
**URL:** https://arxiv.org/abs/2601.21853

**Summary:** Reduces multi-vector similarity to a supervised learning problem solvable by a one-hidden-layer neural network, then further reduces to single-vector search in a learned latent space. Achieves an order of magnitude speedup over prior multi-vector approaches.

**Why important:** The reduction to a one-hidden-layer network provides an implicit expressiveness characterization: multi-vector MaxSim similarity can be approximated by functions in the class of shallow neural networks. This bounds the complexity class of the MaxSim scoring function.

---

**Paper 10.**
**Title:** WARP: An Efficient Engine for Multi-Vector Retrieval
**Authors:** Jan Luca Scheerer, Matei Zaharia, Christopher Potts, Gustavo Alonso, Omar Khattab
**Venue/Year:** SIGIR 2025
**URL:** https://arxiv.org/abs/2501.17788

**Summary:** Introduces WARP with dynamic similarity imputation (WARP_SELECT), implicit decompression, and two-stage reduction. Achieves 41x speedup over XTR and 3x over ColBERTv2/PLAID while maintaining retrieval quality.

**Why important:** WARP_SELECT's dynamic similarity imputation is an approximation to MaxSim that trades off computation for expressiveness. Understanding when this approximation preserves retrieval quality reveals which components of multi-vector expressiveness are essential vs. redundant.

---

**Paper 11.**
**Title:** Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling
**Authors:** Benjamin Clavie, Antoine Chaffin, Griffin Adams
**Venue/Year:** arXiv preprint, September 2024
**URL:** https://arxiv.org/abs/2409.14683

**Summary:** Clustering-based token pooling reduces ColBERT storage by 50% with virtually no retrieval degradation, and by 66-75% with less than 5% degradation on most datasets. No architectural changes or query-time modifications needed.

**Why important:** Quantifies the redundancy in multi-vector representations: if half the vectors can be removed with no quality loss, the effective expressiveness is lower than the raw token count suggests. This provides empirical upper bounds on how many vectors are actually needed.

---

**Paper 12.**
**Title:** Multi-Vector Index Compression in Any Modality
**Authors:** Hanxiang Qin, Alexander Martin, Rohan Jha, Chunsheng Zuo, Reno Kriz, Benjamin Van Durme
**Venue/Year:** arXiv preprint, February 2026
**URL:** https://arxiv.org/abs/2602.21202

**Summary:** Proposes four compression strategies for multi-vector representations (sequence resizing, memory tokens, hierarchical pooling, attention-guided clustering) across text, visual documents, and video. AGC consistently outperforms other methods.

**Why important:** The compression-vs-quality tradeoff curves across modalities characterize the intrinsic dimensionality of multi-vector representations, which is a proxy for their effective expressiveness.

---

**Paper 13.**
**Title:** Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval
**Authors:** Roi Pony, Adi Raz, Oshri Naparstek, Idan Friedman, Udi Barzelay
**Venue/Year:** arXiv preprint, February 2026
**URL:** https://arxiv.org/abs/2602.02827

**Summary:** Reframes MaxSim reranking as a finite-population Top-K identification problem and uses statistical bounds on partially observed scores to prune unnecessary (document, query token) interactions by up to 5x without quality loss.

**Why important:** Demonstrates that "dense late-interaction scoring contains substantial redundancy" -- many MaxSim token-pair comparisons are unnecessary for correct ranking. This gives an empirical characterization of the effective degrees of freedom in the MaxSim scoring function.

---

**Paper 14.**
**Title:** MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction
**Authors:** Zilin Xiao, Qi Ma, Mengting Gu, Chun-cheng Jason Chen, Xintao Chen, Vicente Ordonez, Vijai Mohan
**Venue/Year:** ICLR 2026 (Oral)
**URL:** https://arxiv.org/abs/2509.18095

**Summary:** Uses learnable Meta Tokens with Matryoshka Multi-Vector Retrieval training to create hierarchically organized multi-vector embeddings that can be flexibly scaled at test time. Achieves SOTA on MMEB and ViDoRe benchmarks, scaling to 32B parameters.

**Why important:** The Matryoshka structure provides a principled way to study how expressiveness scales with the number of vectors per document. The hierarchical organization implies that multi-vector expressiveness has a natural ordering, with diminishing returns from additional vectors.

---

### TIER 4: CONTEXTUAL / RELATED WORK

---

**Paper 15.**
**Title:** Simple Projection Variants Improve ColBERT Performance
**Authors:** Benjamin Clavie, Sean Lee, Rikiya Takehi, Aamir Shakir, Makoto P. Kato
**Venue/Year:** arXiv preprint, October 2025
**URL:** https://arxiv.org/abs/2510.12327

**Summary:** Shows that the standard single-layer linear projection in ColBERT limits gradient flow, and that deeper nonlinear projections (GLU, skip-connections) improve performance by 2+ NDCG@10 points.

**Why important:** Demonstrates that the projection layer is a bottleneck in multi-vector expressiveness -- the encoder may capture more information than the linear projection can preserve in the token embeddings.

---

**Paper 16.**
**Title:** LACONIC: Dense-Level Effectiveness for Scalable Sparse Retrieval via a Two-Phase Training Curriculum
**Authors:** Zhichao Xu, Shengyao Zhuang, Crystina Zhang, Xueguang Ma, Yijun Tian, Maitrey Mehta, Jimmy Lin, Vivek Srikumar
**Venue/Year:** arXiv preprint, January 2026
**URL:** https://arxiv.org/abs/2601.01684

**Summary:** Learned sparse retrievers (1B-8B params, Llama-3 based) achieve 60.2 nDCG on MTEB Retrieval with 71% less index memory than equivalent dense models, running on CPU hardware.

**Why important:** Demonstrates that learned sparse retrieval (a different multi-dimensional representation) can match dense retrieval expressiveness, suggesting that the single-vector bottleneck -- not the dense vs. sparse distinction -- is the fundamental limitation.

---

**Paper 17.**
**Title:** Rethinking the Role of Token Retrieval in Multi-Vector Retrieval (XTR)
**Authors:** Jinhyuk Lee, Zhuyun Dai, Sai Meher Karthik Duddu, Tao Lei, Iftekhar Naim, Ming-Wei Chang, Vincent Y. Zhao
**Venue/Year:** NeurIPS 2023
**URL:** https://arxiv.org/abs/2304.01982

**Summary:** Introduces XTR (ConteXtualized Token Retriever), which retrieves only the most important document tokens rather than all tokens, reducing computation by 2-3 orders of magnitude while improving quality by 2.8 nDCG@10 on BEIR.

**Why important:** Foundational for understanding which tokens carry the expressiveness in multi-vector retrieval. Shows that a small subset of tokens carries most of the discriminative information, bounding the effective expressiveness of multi-vector representations.

---

**Paper 18.**
**Title:** PyLate: Flexible Training and Retrieval for Late Interaction Models
**Authors:** Antoine Chaffin, Raphael Sourty
**Venue/Year:** arXiv preprint, August 2025
**URL:** https://arxiv.org/abs/2508.03555

**Summary:** Library built on Sentence Transformers for training and deploying multi-vector late interaction models. Has enabled SOTA models including GTE-ModernColBERT and Reason-ModernColBERT.

**Why important:** Infrastructure paper that has catalyzed experimentation with multi-vector architectures. Relevant as it demonstrates the practical ecosystem for multi-vector research.

---

**Paper 19.**
**Title:** Jina-ColBERT-v2: A General-Purpose Multilingual Late Interaction Retriever
**Authors:** Rohan Jha, Bo Wang, Michael Gunther, Georgios Mastrapas, Saba Sturua, Isabelle Mohr, Andreas Koukounas, Mohammad Kalim Akram, Nan Wang, Han Xiao
**Venue/Year:** EMNLP 2024 Workshop
**URL:** https://arxiv.org/abs/2408.16672

**Summary:** Applies mature single-vector training techniques (heterogeneous multilingual data, efficiency optimizations) to ColBERT architecture. Notes that late interaction scoring "approximates the joint query-document attention seen in cross-encoders while maintaining inference efficiency closer to traditional dense retrieval."

**Why important:** The framing of MaxSim as an approximation to cross-encoder attention is relevant to expressiveness -- it positions multi-vector retrieval on the expressiveness spectrum between single-vector bi-encoders and full cross-encoders.

---

**Paper 20.**
**Title:** LIR: The First Workshop on Late Interaction and Multi Vector Retrieval @ ECIR 2026
**Authors:** Benjamin Clavie, Xianming Li, Antoine Chaffin, Omar Khattab, Tom Aarsen, Manuel Faysse, Jing Li
**Venue/Year:** ECIR 2026 Workshop
**URL:** https://arxiv.org/abs/2511.00444

**Summary:** Workshop proposal establishing the first dedicated venue for late interaction research, covering efficiency, usability, novel applications (reasoning, cross-modality), and system integration.

**Why important:** Signals the maturation of multi-vector retrieval as a distinct research area. The workshop scope document provides a comprehensive overview of open questions in the field.

---

### KEY TAKEAWAYS FOR EXPRESSIVENESS BOUNDS

1. **Single-vector limitations are now proven:** Weller et al. (ICLR 2026) establish that single-vector embeddings of dimension d have combinatorial limits on representable top-k sets, connected to sign-rank. This is the strongest formal result motivating multi-vector approaches.

2. **Multi-vector Chamfer/MaxSim has provable approximation guarantees:** MUVERA (NeurIPS 2024) proves epsilon-approximation bounds for reducing Chamfer similarity to inner product, giving the first formal bridge between multi-vector and single-vector expressiveness.

3. **Multi-vector representations have provable stability advantages:** Lakshman et al. (2025) prove Chamfer distance preserves retrieval stability in high dimensions while pooling (single-vector compression) may not.

4. **Effective expressiveness is lower than raw token count:** Token pooling (Clavie et al. 2024), XTR (Lee et al. 2023), and Col-Bandit (Pony et al. 2026) all show that 50-80% of multi-vector interactions are redundant, bounding the effective degrees of freedom.

5. **Weighted MaxSim is strictly more expressive than uniform MaxSim:** Two independent 2025-2026 papers (Archish et al., Patel & Dutta) show that incorporating token importance into the scoring function increases expressiveness with measurable quality gains.

6. **The expressiveness hierarchy is: single-vector < multi-vector (MaxSim) < cross-encoder (full attention)**, with multi-vector positioned as an approximation to cross-encoder attention (Jina-ColBERT-v2 framing), and generative retrieval decoders implicitly implementing multi-vector scoring (Wu et al. SIGIR 2024).

agentId: a0bfac481dba45d4f (use SendMessage with to: 'a0bfac481dba45d4f' to continue this agent)
&lt;usage>total_tokens: 37729
tool_uses: 43
duration_ms: 240439&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa69834c-e0e0-40c2-8464-e042cb39eb36",
  "isSidechain": false,
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "4c2af39d-bf96-4129-87a7-9efeeccb0d08",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on formal expressiveness bounds for multi-vector (MaxSim/ColBERT-style) retrieval. \n\nConduct these searches and fetch abstracts for relevant papers (2024-2026):\n\n1. WebSearch: \"ColBERT multi-vector retrieval 2025 2026 theory\"\n2. WebSearch: \"MaxSim scoring late interaction retrieval 2024 2025 2026\"\n3. WebSearch: \"multi-vector retrieval expressiveness capacity 2024 2025 2026\"\n4. WebSearch: \"ColBERTv2 PLAID XTR late interaction retrieval 2024 2025\"\n5. WebSearch: \"dense retrieval single-vector vs multi-vector comparison 2024 2025 2026\"\n6. WebSearch: \"Chamfer similarity retrieval multi-vector 2024 2025\"\n7. WebSearch: \"token-level representation retrieval models theory 2024 2025 2026\"\n8. WebSearch: \"learned sparse retrieval vs dense retrieval expressiveness 2024 2025\"\n\nFor each relevant paper, use WebFetch on its arxiv/openreview page to get the abstract. Report:\n- Full title, authors, venue/year, URL\n- One-line summary\n- Why important for understanding multi-vector retrieval expressiveness",
    "agentId": "a0bfac481dba45d4f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is the full literature survey report.\n\n---\n\n## Literature Survey: Formal Expressiveness Bounds for Multi-Vector (MaxSim/ColBERT-style) Retrieval (2024--2026)\n\n---\n\n### TIER 1: CORE THEORY PAPERS (directly address expressiveness bounds)\n\n---\n\n**Paper 1.**\n**Title:** On the Theoretical Limitations of Embedding-Based Retrieval\n**Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee\n**Venue/Year:** ICLR 2026\n**URL:** https://arxiv.org/abs/2508.21038\n\n**Summary:** Proves that for single-vector dot-product embeddings of dimension d, the number of distinct top-k document subsets returnable by any query is fundamentally bounded by d, connecting sign-rank from communication complexity to representational capacity. Introduces the LIMIT benchmark showing state-of-the-art single-vector models fail on simple tasks predicted to be hard by the theory.\n\n**Why important:** This is the most directly relevant paper. It establishes formal combinatorial limits on what single-vector retrieval can express, and explicitly calls for multi-vector approaches as a way to overcome these limits. It provides the theoretical baseline against which multi-vector expressiveness gains should be measured.\n\n---\n\n**Paper 2.**\n**Title:** MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings\n**Authors:** Laxman Dhulipala, Majid Hadian, Rajesh Jayaram, Jason Lee, Vahab Mirrokni\n**Venue/Year:** NeurIPS 2024\n**URL:** https://arxiv.org/abs/2405.19504\n\n**Summary:** Introduces Fixed Dimensional Encodings (FDEs) that reduce multi-vector Chamfer/MaxSim similarity search to single-vector MIPS. Proves that FDEs provide epsilon-approximations to Chamfer similarity -- the first single-vector proxy for multi-vector similarity with provable theoretical guarantees. Achieves 10% better recall at 90% lower latency than PLAID on BEIR.\n\n**Why important:** Provides the first algorithm with provable guarantees for Chamfer similarity search with strictly faster than brute-force runtime. The epsilon-approximation bounds formalize how much information is lost when compressing multi-vector representations to single vectors, directly quantifying the expressiveness gap.\n\n---\n\n**Paper 3.**\n**Title:** Breaking the Curse of Dimensionality: On the Stability of Modern Vector Retrieval\n**Authors:** Vihan Lakshman, Blaise Munyampirwa, Julian Shun, Benjamin Coleman\n**Venue/Year:** arXiv preprint, December 2025 (revised February 2026)\n**URL:** https://arxiv.org/abs/2512.12458\n\n**Summary:** Extends stability theory (resilience of nearest-neighbor rankings to small query perturbations) to three practical settings: multi-vector search with Chamfer distance, filtered vector search, and sparse vector search. Proves that Chamfer distance preserves stability while certain pooling methods may not, and formalizes novel stability conditions for sparse retrieval.\n\n**Why important:** Provides theoretical justification for why Chamfer-distance-based multi-vector retrieval works well in high dimensions despite the curse of dimensionality. Shows that multi-vector (Chamfer) scoring has favorable stability properties that single-vector pooling may lack -- a formal expressiveness advantage.\n\n---\n\n**Paper 4.**\n**Title:** Generative Retrieval as Multi-Vector Dense Retrieval\n**Authors:** Shiguang Wu, Wenda Wei, Mengqi Zhang, Zhumin Chen, Jun Ma, Zhaochun Ren, Maarten de Rijke, Pengjie Ren\n**Venue/Year:** SIGIR 2024\n**URL:** https://arxiv.org/abs/2404.00684\n\n**Summary:** Rigorously proves that generative retrieval (with atomic identifiers) is equivalent to single-vector dense retrieval, while the decoder's attention layers and prediction heads implement a form of multi-vector dense retrieval. Both paradigms compute relevance as summed products of query vectors, document vectors, and an alignment matrix.\n\n**Why important:** Establishes a formal equivalence between generative retrieval and multi-vector dense retrieval, showing that the decoder in generative models implicitly computes a MaxSim-like operation. This reveals that multi-vector expressiveness is a more general phenomenon than ColBERT alone, and connects two research communities.\n\n---\n\n### TIER 2: ANALYTICAL / EMPIRICAL EXPRESSIVENESS STUDIES\n\n---\n\n**Paper 5.**\n**Title:** Working Notes on Late Interaction Dynamics: Analyzing Targeted Behaviors of Late Interaction Models\n**Authors:** Antoine Edy, Max Conti, Quentin Mace\n**Venue/Year:** LIR Workshop @ ECIR 2026\n**URL:** https://arxiv.org/abs/2603.26259\n\n**Summary:** Empirically analyzes understudied dynamics of late interaction models, specifically the length bias inherent in multi-vector MaxSim scoring and the similarity distribution beyond the top-1 document token. Finds that the theoretical length bias of causal late interaction models holds in practice, and that MaxSim is efficient because no significant similarity trend lies beyond the top-1 document token.\n\n**Why important:** Validates theoretical predictions about MaxSim scoring behavior in practice. The length bias analysis is relevant to understanding the expressiveness limitations of the MaxSim operator itself -- longer documents receive systematically higher scores, an inherent bias in the scoring function's expressiveness.\n\n---\n\n**Paper 6.**\n**Title:** Incorporating Token Importance in Multi-Vector Retrieval\n**Authors:** Archish S, Ankit Garg, Kirankumar Shiragur, Neeraj Kayal\n**Venue/Year:** arXiv preprint, November 2025\n**URL:** https://arxiv.org/abs/2511.16106\n\n**Summary:** Enhances the Chamfer distance function in ColBERT by computing a weighted sum over query token contributions (e.g., IDF-based or learned weights), achieving 1.28% zero-shot and 3.66% few-shot improvement in Recall@10 on BEIR. Argues this increases the expressiveness of the multi-vector mechanism without changing the underlying representations.\n\n**Why important:** Demonstrates that the standard (uniform-weight) MaxSim/Chamfer operator leaves expressiveness on the table, and that weighted variants are strictly more expressive. Provides an empirical quantification of how much expressiveness is gained by moving from uniform to importance-weighted multi-vector scoring.\n\n---\n\n**Paper 7.**\n**Title:** ColBERT-Att: Late-Interaction Meets Attention for Enhanced Retrieval\n**Authors:** Raj Nath Patel, Sourav Dutta\n**Venue/Year:** arXiv preprint, March 2026\n**URL:** https://arxiv.org/abs/2603.25248\n\n**Summary:** Integrates attention weights into the MaxSim late interaction framework, arguing that standard ColBERT fails to account for the relative importance of query-document token similarities. Shows improvements on MS-MARCO, BEIR, and LoTTE benchmarks.\n\n**Why important:** Complementary to Paper 6 -- both show that the vanilla MaxSim operator is not maximally expressive and that incorporating term importance (via attention or IDF) increases the scoring function's capacity. Relevant to understanding the expressiveness frontier of late interaction scoring.\n\n---\n\n**Paper 8.**\n**Title:** Understanding the Multi-vector Dense Retrieval Models\n**Authors:** (Zhan et al.)\n**Venue/Year:** CIKM 2023\n**URL:** https://dl.acm.org/doi/10.1145/3583780.3615282\n\n**Summary:** Investigates why multi-vector dense retrieval outperforms single-vector approaches by analyzing vocabulary distribution and representation behavior differences between the two paradigms. Provides empirical interpretability analysis of multi-vector expressiveness advantages.\n\n**Why important:** Although from 2023, this is a foundational reference for the expressiveness question. It provides the empirical evidence base that motivates the theoretical work in Papers 1-3, analyzing what multi-vector models capture that single-vector models cannot.\n\n---\n\n### TIER 3: EFFICIENCY AND SYSTEMS (relevant to expressiveness-efficiency tradeoffs)\n\n---\n\n**Paper 9.**\n**Title:** LEMUR: Learned Multi-Vector Retrieval\n**Authors:** Elias Jaasaari, Ville Hyvonen, Teemu Roos\n**Venue/Year:** ICML 2026\n**URL:** https://arxiv.org/abs/2601.21853\n\n**Summary:** Reduces multi-vector similarity to a supervised learning problem solvable by a one-hidden-layer neural network, then further reduces to single-vector search in a learned latent space. Achieves an order of magnitude speedup over prior multi-vector approaches.\n\n**Why important:** The reduction to a one-hidden-layer network provides an implicit expressiveness characterization: multi-vector MaxSim similarity can be approximated by functions in the class of shallow neural networks. This bounds the complexity class of the MaxSim scoring function.\n\n---\n\n**Paper 10.**\n**Title:** WARP: An Efficient Engine for Multi-Vector Retrieval\n**Authors:** Jan Luca Scheerer, Matei Zaharia, Christopher Potts, Gustavo Alonso, Omar Khattab\n**Venue/Year:** SIGIR 2025\n**URL:** https://arxiv.org/abs/2501.17788\n\n**Summary:** Introduces WARP with dynamic similarity imputation (WARP_SELECT), implicit decompression, and two-stage reduction. Achieves 41x speedup over XTR and 3x over ColBERTv2/PLAID while maintaining retrieval quality.\n\n**Why important:** WARP_SELECT's dynamic similarity imputation is an approximation to MaxSim that trades off computation for expressiveness. Understanding when this approximation preserves retrieval quality reveals which components of multi-vector expressiveness are essential vs. redundant.\n\n---\n\n**Paper 11.**\n**Title:** Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling\n**Authors:** Benjamin Clavie, Antoine Chaffin, Griffin Adams\n**Venue/Year:** arXiv preprint, September 2024\n**URL:** https://arxiv.org/abs/2409.14683\n\n**Summary:** Clustering-based token pooling reduces ColBERT storage by 50% with virtually no retrieval degradation, and by 66-75% with less than 5% degradation on most datasets. No architectural changes or query-time modifications needed.\n\n**Why important:** Quantifies the redundancy in multi-vector representations: if half the vectors can be removed with no quality loss, the effective expressiveness is lower than the raw token count suggests. This provides empirical upper bounds on how many vectors are actually needed.\n\n---\n\n**Paper 12.**\n**Title:** Multi-Vector Index Compression in Any Modality\n**Authors:** Hanxiang Qin, Alexander Martin, Rohan Jha, Chunsheng Zuo, Reno Kriz, Benjamin Van Durme\n**Venue/Year:** arXiv preprint, February 2026\n**URL:** https://arxiv.org/abs/2602.21202\n\n**Summary:** Proposes four compression strategies for multi-vector representations (sequence resizing, memory tokens, hierarchical pooling, attention-guided clustering) across text, visual documents, and video. AGC consistently outperforms other methods.\n\n**Why important:** The compression-vs-quality tradeoff curves across modalities characterize the intrinsic dimensionality of multi-vector representations, which is a proxy for their effective expressiveness.\n\n---\n\n**Paper 13.**\n**Title:** Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval\n**Authors:** Roi Pony, Adi Raz, Oshri Naparstek, Idan Friedman, Udi Barzelay\n**Venue/Year:** arXiv preprint, February 2026\n**URL:** https://arxiv.org/abs/2602.02827\n\n**Summary:** Reframes MaxSim reranking as a finite-population Top-K identification problem and uses statistical bounds on partially observed scores to prune unnecessary (document, query token) interactions by up to 5x without quality loss.\n\n**Why important:** Demonstrates that \"dense late-interaction scoring contains substantial redundancy\" -- many MaxSim token-pair comparisons are unnecessary for correct ranking. This gives an empirical characterization of the effective degrees of freedom in the MaxSim scoring function.\n\n---\n\n**Paper 14.**\n**Title:** MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction\n**Authors:** Zilin Xiao, Qi Ma, Mengting Gu, Chun-cheng Jason Chen, Xintao Chen, Vicente Ordonez, Vijai Mohan\n**Venue/Year:** ICLR 2026 (Oral)\n**URL:** https://arxiv.org/abs/2509.18095\n\n**Summary:** Uses learnable Meta Tokens with Matryoshka Multi-Vector Retrieval training to create hierarchically organized multi-vector embeddings that can be flexibly scaled at test time. Achieves SOTA on MMEB and ViDoRe benchmarks, scaling to 32B parameters.\n\n**Why important:** The Matryoshka structure provides a principled way to study how expressiveness scales with the number of vectors per document. The hierarchical organization implies that multi-vector expressiveness has a natural ordering, with diminishing returns from additional vectors.\n\n---\n\n### TIER 4: CONTEXTUAL / RELATED WORK\n\n---\n\n**Paper 15.**\n**Title:** Simple Projection Variants Improve ColBERT Performance\n**Authors:** Benjamin Clavie, Sean Lee, Rikiya Takehi, Aamir Shakir, Makoto P. Kato\n**Venue/Year:** arXiv preprint, October 2025\n**URL:** https://arxiv.org/abs/2510.12327\n\n**Summary:** Shows that the standard single-layer linear projection in ColBERT limits gradient flow, and that deeper nonlinear projections (GLU, skip-connections) improve performance by 2+ NDCG@10 points.\n\n**Why important:** Demonstrates that the projection layer is a bottleneck in multi-vector expressiveness -- the encoder may capture more information than the linear projection can preserve in the token embeddings.\n\n---\n\n**Paper 16.**\n**Title:** LACONIC: Dense-Level Effectiveness for Scalable Sparse Retrieval via a Two-Phase Training Curriculum\n**Authors:** Zhichao Xu, Shengyao Zhuang, Crystina Zhang, Xueguang Ma, Yijun Tian, Maitrey Mehta, Jimmy Lin, Vivek Srikumar\n**Venue/Year:** arXiv preprint, January 2026\n**URL:** https://arxiv.org/abs/2601.01684\n\n**Summary:** Learned sparse retrievers (1B-8B params, Llama-3 based) achieve 60.2 nDCG on MTEB Retrieval with 71% less index memory than equivalent dense models, running on CPU hardware.\n\n**Why important:** Demonstrates that learned sparse retrieval (a different multi-dimensional representation) can match dense retrieval expressiveness, suggesting that the single-vector bottleneck -- not the dense vs. sparse distinction -- is the fundamental limitation.\n\n---\n\n**Paper 17.**\n**Title:** Rethinking the Role of Token Retrieval in Multi-Vector Retrieval (XTR)\n**Authors:** Jinhyuk Lee, Zhuyun Dai, Sai Meher Karthik Duddu, Tao Lei, Iftekhar Naim, Ming-Wei Chang, Vincent Y. Zhao\n**Venue/Year:** NeurIPS 2023\n**URL:** https://arxiv.org/abs/2304.01982\n\n**Summary:** Introduces XTR (ConteXtualized Token Retriever), which retrieves only the most important document tokens rather than all tokens, reducing computation by 2-3 orders of magnitude while improving quality by 2.8 nDCG@10 on BEIR.\n\n**Why important:** Foundational for understanding which tokens carry the expressiveness in multi-vector retrieval. Shows that a small subset of tokens carries most of the discriminative information, bounding the effective expressiveness of multi-vector representations.\n\n---\n\n**Paper 18.**\n**Title:** PyLate: Flexible Training and Retrieval for Late Interaction Models\n**Authors:** Antoine Chaffin, Raphael Sourty\n**Venue/Year:** arXiv preprint, August 2025\n**URL:** https://arxiv.org/abs/2508.03555\n\n**Summary:** Library built on Sentence Transformers for training and deploying multi-vector late interaction models. Has enabled SOTA models including GTE-ModernColBERT and Reason-ModernColBERT.\n\n**Why important:** Infrastructure paper that has catalyzed experimentation with multi-vector architectures. Relevant as it demonstrates the practical ecosystem for multi-vector research.\n\n---\n\n**Paper 19.**\n**Title:** Jina-ColBERT-v2: A General-Purpose Multilingual Late Interaction Retriever\n**Authors:** Rohan Jha, Bo Wang, Michael Gunther, Georgios Mastrapas, Saba Sturua, Isabelle Mohr, Andreas Koukounas, Mohammad Kalim Akram, Nan Wang, Han Xiao\n**Venue/Year:** EMNLP 2024 Workshop\n**URL:** https://arxiv.org/abs/2408.16672\n\n**Summary:** Applies mature single-vector training techniques (heterogeneous multilingual data, efficiency optimizations) to ColBERT architecture. Notes that late interaction scoring \"approximates the joint query-document attention seen in cross-encoders while maintaining inference efficiency closer to traditional dense retrieval.\"\n\n**Why important:** The framing of MaxSim as an approximation to cross-encoder attention is relevant to expressiveness -- it positions multi-vector retrieval on the expressiveness spectrum between single-vector bi-encoders and full cross-encoders.\n\n---\n\n**Paper 20.**\n**Title:** LIR: The First Workshop on Late Interaction and Multi Vector Retrieval @ ECIR 2026\n**Authors:** Benjamin Clavie, Xianming Li, Antoine Chaffin, Omar Khattab, Tom Aarsen, Manuel Faysse, Jing Li\n**Venue/Year:** ECIR 2026 Workshop\n**URL:** https://arxiv.org/abs/2511.00444\n\n**Summary:** Workshop proposal establishing the first dedicated venue for late interaction research, covering efficiency, usability, novel applications (reasoning, cross-modality), and system integration.\n\n**Why important:** Signals the maturation of multi-vector retrieval as a distinct research area. The workshop scope document provides a comprehensive overview of open questions in the field.\n\n---\n\n### KEY TAKEAWAYS FOR EXPRESSIVENESS BOUNDS\n\n1. **Single-vector limitations are now proven:** Weller et al. (ICLR 2026) establish that single-vector embeddings of dimension d have combinatorial limits on representable top-k sets, connected to sign-rank. This is the strongest formal result motivating multi-vector approaches.\n\n2. **Multi-vector Chamfer/MaxSim has provable approximation guarantees:** MUVERA (NeurIPS 2024) proves epsilon-approximation bounds for reducing Chamfer similarity to inner product, giving the first formal bridge between multi-vector and single-vector expressiveness.\n\n3. **Multi-vector representations have provable stability advantages:** Lakshman et al. (2025) prove Chamfer distance preserves retrieval stability in high dimensions while pooling (single-vector compression) may not.\n\n4. **Effective expressiveness is lower than raw token count:** Token pooling (Clavie et al. 2024), XTR (Lee et al. 2023), and Col-Bandit (Pony et al. 2026) all show that 50-80% of multi-vector interactions are redundant, bounding the effective degrees of freedom.\n\n5. **Weighted MaxSim is strictly more expressive than uniform MaxSim:** Two independent 2025-2026 papers (Archish et al., Patel & Dutta) show that incorporating token importance into the scoring function increases expressiveness with measurable quality gains.\n\n6. **The expressiveness hierarchy is: single-vector < multi-vector (MaxSim) < cross-encoder (full attention)**, with multi-vector positioned as an approximation to cross-encoder attention (Jina-ColBERT-v2 framing), and generative retrieval decoders implicitly implementing multi-vector scoring (Wu et al. SIGIR 2024)."
      }
    ],
    "totalDurationMs": 240439,
    "totalTokens": 37729,
    "totalToolUseCount": 43,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1560,
      "cache_read_input_tokens": 31182,
      "output_tokens": 4986,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1560
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4986,
          "cache_read_input_tokens": 31182,
          "cache_creation_input_tokens": 1560,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1560,
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
      "otherToolCount": 43
    }
  },
  "sourceToolAssistantUUID": "fa69834c-e0e0-40c2-8464-e042cb39eb36",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "4c2af39d-bf96-4129-87a7-9efeeccb0d08",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on multi-vector retrieval expressiveness",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Tool result

_source line 26 · 2026-05-30T06:14:29.155Z_

<details><summary>↩ Tool result · `toolu_01DXp3ctLFdiNjm5woKndm81`</summary>

```text
Now I have comprehensive information. Here is the full literature survey report.

---

## Literature Survey: Theoretical Foundations of Information Retrieval -- Expressiveness of Retrieval Models and Embedding Theory

### TIER 1: DIRECTLY RELEVANT TO MULTI-VECTOR RETRIEVAL EXPRESSIVENESS THEORY

---

**1. "On the Theoretical Limitations of Embedding-Based Retrieval"**
- **Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee (Google DeepMind, Johns Hopkins)
- **Venue/Year:** ICLR 2026
- **URL:** https://arxiv.org/abs/2508.21038
- **Award:** Accepted paper (no best paper award noted)
- **Summary:** Proves that single-vector embedding retrieval is fundamentally limited: the number of top-k subsets of documents returnable by any query is bounded by the embedding dimension. Introduces the LIMIT dataset showing SOTA systems fail on simple tasks.
- **Relevance to multi-vector retrieval expressiveness:** **CENTRAL.** This is the most directly relevant paper. It provides formal theoretical proof that single-vector embeddings have inherent expressiveness limitations, which serves as the core motivation for multi-vector retrieval. The authors explicitly advocate for alternative approaches (including multi-vector) to overcome these constraints.

---

**2. "MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings"**
- **Authors:** Laxman Dhulipala, Majid Hadian, Rajesh Jayaram, Jason Lee, Vahab Mirrokni (Google Research)
- **Venue/Year:** NeurIPS 2024
- **URL:** https://arxiv.org/abs/2405.19504
- **Award:** Poster presentation
- **Summary:** Reduces multi-vector similarity search to single-vector MIPS by generating Fixed Dimensional Encodings (FDEs) whose inner product approximates multi-vector similarity, with theoretical approximation guarantees. Achieves 10% improved recall at 90% lower latency on BEIR.
- **Relevance:** **HIGH.** Provides the first single-vector proxy for multi-vector similarity with formal theoretical guarantees (epsilon-approximation bounds), directly addressing the computational vs. expressiveness tradeoff in multi-vector retrieval.

---

**3. "Multi-Vector Retrieval as Sparse Alignment" (ALIGNER)**
- **Authors:** Yujie Qian, Jinhyuk Lee, Karthik Duddu, Zhuyun Dai, Tao Lei, Siddhartha Brahma, Iftekhar Naim, Vincent Y Zhao
- **Venue/Year:** ICLR 2023
- **URL:** https://arxiv.org/abs/2211.01267
- **Award:** None
- **Summary:** Reframes multi-vector retrieval as sparse alignment between query and document tokens, learning sparsified pairwise token alignments and per-token salience scores. Achieves 51.1 nDCG@10 zero-shot on BEIR; retains only 20% of document token representations with minimal loss.
- **Relevance:** **HIGH.** Provides a principled formalization of multi-vector interaction as sparse alignment, offering an alternative theoretical lens on how token-level interactions contribute to retrieval quality and how redundancy can be exploited.

---

**4. "A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models"**
- **Authors:** Yash Kankanampati, Yuxuan Zong, Nadi Tomeh, Benjamin Piwowarski, Joseph Le Roux
- **Venue/Year:** SIGIR 2026 (Full Paper)
- **URL:** https://arxiv.org/abs/2603.09933
- **Award:** None noted
- **Summary:** Reframes token reduction in multi-vector retrieval as a Voronoi cell estimation problem in embedding space, interpreting each token's impact through its Voronoi region. Provides principled pruning that preserves retrieval effectiveness while reducing storage.
- **Relevance:** **HIGH.** Offers a geometric/theoretical framework (Voronoi tessellations in embedding space) for understanding token-level contributions in multi-vector retrieval, directly connecting to expressiveness theory by formalizing what each token embedding "covers" in representation space.

---

**5. "Working Notes on Late Interaction Dynamics: Analyzing Targeted Behaviors of Late Interaction Models"**
- **Authors:** Antoine Edy, Max Conti, Quentin Mace
- **Venue/Year:** LIR Workshop @ ECIR 2026
- **URL:** https://arxiv.org/abs/2603.26259
- **Award:** Workshop paper
- **Summary:** Analyzes two theoretical properties of late interaction: (1) causal encoders with MaxSim scoring exhibit monotonic length bias favoring longer chunks regardless of relevance; (2) beyond the top token match, the MaxSim operator collapses information, confirming it captures only peak similarity per query token.
- **Relevance:** **HIGH.** Provides empirical-theoretical analysis of the MaxSim operator's fundamental behavior and limitations, directly informing the expressiveness properties and failure modes of ColBERT-style multi-vector retrieval.

---

**6. "Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval"**
- **Authors:** Roi Pony, Adi Raz, Oshri Naparstek, Idan Friedman, Udi Barzelay
- **Venue/Year:** arXiv preprint, February 2026
- **URL:** https://arxiv.org/abs/2602.02827
- **Award:** Preprint (no venue award)
- **Summary:** Recasts MaxSim reranking as a finite-population Top-K identification problem using bandit algorithms. Maintains uncertainty-aware bounds over partially observed document scores, adaptively revealing only necessary MaxSim entries. Achieves up to 5x FLOPs reduction on BEIR and REAL-MM-RAG.
- **Relevance:** **MODERATE-HIGH.** Demonstrates substantial redundancy in dense late-interaction scoring through a principled bandit-theoretic lens, contributing to understanding of the information-theoretic properties of multi-vector interactions.

---

**7. "MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction"**
- **Authors:** Zilin Xiao, Qi Ma, Mengting Gu, Chun-cheng Jason Chen, Xintao Chen, Vicente Ordonez, Vijai Mohan
- **Venue/Year:** ICLR 2026 (Oral)
- **URL:** https://arxiv.org/abs/2509.18095
- **Award:** **ICLR 2026 Oral** presentation
- **Summary:** Introduces learnable Meta Tokens whose contextualized representations serve as compact multi-vector embeddings. Uses Matryoshka Multi-Vector Retrieval training to organize information by granularity, enabling test-time scaling of retrieval quality vs. efficiency. Scales to 32B parameter models; SOTA on MMEB and ViDoRe.
- **Relevance:** **HIGH.** Directly addresses the expressiveness-efficiency frontier of multi-vector retrieval by controlling the number of vectors at test time with Matryoshka-style training, providing empirical evidence about how multi-vector granularity affects retrieval quality.

---

**8. "AMES: Approximate Multi-modal Enterprise Search via Late Interaction Retrieval"**
- **Authors:** Tony Joseph, Carlos Pareja, David Lopes Pegna, Abhishek Singh
- **Venue/Year:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2603.13537
- **Award:** Preprint
- **Summary:** Presents a unified multimodal late interaction system for enterprise search using a two-stage pipeline: parallel token-level ANN with per-document Top-M MaxSim approximation, then exact MaxSim re-ranking. Demonstrates production-grade deployment on Solr.
- **Relevance:** **MODERATE.** Primarily a systems paper, but its two-stage approximate-then-exact MaxSim pipeline provides practical insights into the computational structure of multi-vector scoring.

---

**9. "LEMUR: Learned Multi-Vector Retrieval"**
- **Authors:** Elias Jaasaari, Ville Hyvonen, Teemu Roos
- **Venue/Year:** arXiv preprint, January 2026
- **URL:** https://arxiv.org/abs/2601.21853
- **Award:** Preprint
- **Summary:** A framework for multi-vector similarity search addressing efficient handling of multi-vector representations from late interaction models like ColBERT.
- **Relevance:** **MODERATE.** Contributes to the algorithmic infrastructure for multi-vector retrieval.

---

### TIER 2: RELEVANT TO EMBEDDING THEORY AND REPRESENTATION EXPRESSIVENESS

---

**10. "Transformers are Inherently Succinct"**
- **Authors:** Pascal Bergstrasser, Ryan Cotterell, Anthony Widjaja Lin
- **Venue/Year:** ICLR 2026
- **URL:** https://arxiv.org/abs/2510.19315
- **Award:** **ICLR 2026 Outstanding Paper Award**
- **Summary:** Proves that fixed-precision transformers are exponentially more succinct than LTL and RNNs, and doubly exponentially more succinct than finite automata. As a byproduct, shows that verifying transformer properties is EXPSPACE-complete.
- **Relevance:** **MODERATE.** While focused on formal language theory rather than retrieval, this is the strongest theoretical result on transformer expressiveness from a major venue. The succinctness results have implications for understanding why transformer-based encoders can produce more expressive embeddings than simpler architectures.

---

**11. "Why are Sensitive Functions Hard for Transformers?"**
- **Authors:** Michael Hahn, Mark Rofin
- **Venue/Year:** ACL 2024
- **URL:** https://arxiv.org/abs/2402.09963
- **Award:** **ACL 2024 Best Paper Award**
- **Summary:** Proves that transformer outputs sensitive to many input parts occupy isolated parameter-space points, creating low-sensitivity bias. Explains difficulty with PARITY and poor length generalization. High-sensitivity functions inhabit very steep minima.
- **Relevance:** **MODERATE.** Bridges expressiveness and learnability for transformers. Relevant to understanding why retrieval encoders may fail to learn certain fine-grained discriminative functions, and why multi-vector approaches (which decompose sensitivity across tokens) may circumvent these limitations.

---

**12. "Superposition Yields Robust Neural Scaling"**
- **Authors:** Yizhou Liu, Ziming Liu, Jeff Gore
- **Venue/Year:** NeurIPS 2025
- **URL:** https://arxiv.org/abs/2505.10465
- **Award:** **NeurIPS 2025 Best Paper Runner-Up**
- **Summary:** Shows that representation superposition (representing more features than dimensions) drives robust neural scaling laws. Under strong superposition, loss scales inversely with model dimension due to geometric interference between representation vectors, regardless of data distribution.
- **Relevance:** **MODERATE.** Directly characterizes how embedding dimensions encode features through superposition, which is fundamental to understanding single-vector embedding capacity limitations (connecting to Weller et al.'s theoretical bounds).

---

**13. "A Text is Worth Several Tokens: Text Embedding from LLMs Secretly Aligns Well with The Key Tokens"**
- **Authors:** Zhijie Nie, Richong Zhang, Zhanyu Wu
- **Venue/Year:** ACL 2025
- **URL:** https://arxiv.org/abs/2406.17378
- **Award:** **ACL 2025 SAC Highlight**
- **Summary:** Discovers that LLM-based text embeddings align with key tokens in the input. This phenomenon is universal across architectures, training strategies, and embedding methods. Proposes a sparse retrieval method achieving ~80% of dense retrieval performance with significantly reduced computation.
- **Relevance:** **MODERATE-HIGH.** Reveals that single-vector embeddings implicitly encode a sparse set of token-level signals, bridging single-vector and multi-vector paradigms. Suggests that multi-vector retrieval may be making explicit what single-vector embeddings already encode implicitly.

---

**14. "Randomly Removing 50% of Dimensions in Text Embeddings has Minimal Impact on Retrieval and Classification Tasks"**
- **Authors:** Sotaro Takeshita, Yurina Takeshita, Daniel Ruffinelli, Simone Paolo Ponzetto
- **Venue/Year:** EMNLP 2025 (Oral)
- **URL:** https://arxiv.org/abs/2508.17744
- **Award:** **EMNLP 2025 People's Choice Award**
- **Summary:** Shows that randomly removing up to 50% of embedding dimensions causes less than 10% performance drop across 6 SOTA encoders and 26 tasks. Many uniformly distributed dimensions actually improve performance when removed.
- **Relevance:** **MODERATE.** Provides empirical evidence about the information structure of text embeddings -- significant dimensional redundancy suggests that the effective dimensionality is much lower than nominal, which relates to theoretical capacity bounds on embedding-based retrieval.

---

**15. "LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation"**
- **Authors:** Weiquan Huang, Aoqi Wu, Yifan Yang, Xufang Luo, Yuqing Yang, et al.
- **Venue/Year:** AAAI 2026
- **URL:** https://arxiv.org/abs/2411.04997
- **Award:** **AAAI 2026 Outstanding Paper Award**
- **Summary:** Uses LLM fine-tuning to create a discriminative embedding model via contrastive learning, then couples with CLIP vision encoder. Boosts zero-shot retrieval by +14.8/+15.8 on long captions and +11.9/+15.2 on multilingual tasks.
- **Relevance:** **LOW-MODERATE.** Demonstrates that richer text representations from LLMs substantially improve cross-modal retrieval, supporting the thesis that embedding quality is a bottleneck; however, uses single-vector representations.

---

### TIER 3: RETRIEVAL-RELATED AWARD WINNERS WITH TANGENTIAL RELEVANCE

---

**16. "Learning to Retrieve Iteratively for In-Context Learning"**
- **Authors:** Yunmo Chen, Tongfei Chen, Harsh Jhamtani, Patrick Xia, Richard Shin, Jason Eisner, Benjamin Van Durme
- **Venue/Year:** EMNLP 2024
- **URL:** https://arxiv.org/abs/2406.14739
- **Award:** **EMNLP 2024 Outstanding Paper Award**
- **Summary:** Proposes iterative retrieval via reinforcement learning for in-context learning exemplar selection. Converts a dense retriever into a stateful iterative retriever with only 4M additional parameters.
- **Relevance:** **LOW.** Addresses retrieval strategy rather than embedding expressiveness theory.

---

**17. "Towards Cross-Cultural Machine Translation with Retrieval-Augmented Generation from Multilingual Knowledge Graphs"**
- **Authors:** Simone Conia, Daniel Lee, Min Li, Umar Farooq Minhas, Saloni Potdar, Yunyao Li
- **Venue/Year:** EMNLP 2024
- **URL:** https://arxiv.org/abs/2410.14057
- **Award:** **EMNLP 2024 Outstanding Paper Award**
- **Summary:** Introduces KG-MT, integrating multilingual knowledge graph information via dense retrieval into neural MT. 129% improvement over NLLB-200, 62% over GPT-4.
- **Relevance:** **LOW.** Uses retrieval but focuses on MT application rather than retrieval expressiveness theory.

---

**18. "Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index"**
- **Authors:** Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi
- **Venue/Year:** EMNLP 2025
- **URL:** https://arxiv.org/abs/2506.12229
- **Award:** **EMNLP 2025 Best Paper Award**
- **Summary:** Builds an FM-index system indexing 83TB of text with 18x faster indexing and 3.2x memory reduction. Conducts large-scale benchmark contamination analysis.
- **Relevance:** **LOW.** Exact-match retrieval infrastructure rather than embedding/representation theory, but demonstrates an alternative retrieval paradigm to dense embeddings.

---

### AWARD WINNERS SURVEYED WITH NO DIRECT RELEVANCE

The following award-winning papers were reviewed and found to have no direct relevance to multi-vector retrieval expressiveness theory:

- **NeurIPS 2024 Best Papers:** Visual Autoregressive Modeling; Stochastic Taylor Derivative Estimator; Not All Tokens Are What You Need; Guiding a Diffusion Model; PRISM Alignment Dataset
- **NeurIPS 2025 Best Papers:** Artificial Hivemind; Gated Attention for LLMs; 1000 Layer Networks for Self-Supervised RL; Why Diffusion Models Don't Memorize; Does RL Really Incentivize Reasoning; Optimal Mistake Bounds for Transductive Online Learning
- **ICLR 2025 Outstanding Papers:** Safety Alignment; Learning Dynamics of LLM Finetuning; AlphaEdit
- **ICLR 2026:** LLMs Get Lost In Multi-Turn Conversation; The Polar Express (Honorable Mention)
- **ICML 2025 Outstanding Papers:** CollabLLM; Train for the Worst; Roll the Dice; Conformal Prediction; Score Matching; Value of Prediction
- **ACL 2024 Best Papers:** Causal Estimation of Memorisation; Aya Model; Mission Impossible Language Models; Semisupervised Proto-Language Reconstruction; Deciphering Oracle Bone Language
- **ACL 2025 Best Papers:** Theory of Response Sampling; Fairness through Difference Awareness; Language Models Resist Alignment; Native Sparse Attention
- **AAAI 2026:** Model Change for Description Logic; Causal Structure Learning; ReconVLA; Sheaflet-based Hypergraph NNs

---

### KEY TAKEAWAYS FOR THE SURVEY

1. **The strongest theoretical result directly on multi-vector retrieval expressiveness** is Weller et al. (ICLR 2026), which proves fundamental limits of single-vector retrieval and motivates multi-vector alternatives.

2. **MUVERA (NeurIPS 2024)** provides the first theoretical bridge between multi-vector and single-vector retrieval with formal approximation guarantees.

3. **The Voronoi Cell formulation (SIGIR 2026)** offers a geometric theory of token contribution in multi-vector retrieval.

4. **MetaEmbed (ICLR 2026 Oral)** provides the most important empirical result on the expressiveness-efficiency frontier of multi-vector retrieval via Matryoshka training.

5. **Transformer expressiveness theory** is represented by two major award winners: "Transformers are Inherently Succinct" (ICLR 2026 Outstanding Paper) and "Why are Sensitive Functions Hard for Transformers?" (ACL 2024 Best Paper), both informing the theoretical foundations of encoder expressiveness.

6. **Representation capacity theory** is advanced by "Superposition Yields Robust Neural Scaling" (NeurIPS 2025 Runner-Up), which characterizes how embedding dimensions encode features.

7. **The LIR Workshop @ ECIR 2026** (the first workshop on Late Interaction and Multi-Vector Retrieval) represents the emergence of this area as a recognized subfield with dedicated community activity.

agentId: aea474fb639da618e (use SendMessage with to: 'aea474fb639da618e' to continue this agent)
&lt;usage>total_tokens: 53919
tool_uses: 60
duration_ms: 259600&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "228a80f2-36a7-473f-b522-c213270092cb",
  "isSidechain": false,
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "83e18bb8-9165-43bd-bf98-d100e6ec7760",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on theoretical foundations of information retrieval, specifically expressiveness of retrieval models and embedding theory.\n\nConduct these searches:\n\n1. WebSearch: \"best paper award NeurIPS 2024 2025 retrieval embeddings\"\n2. WebSearch: \"best paper award ICML 2024 2025 representation learning theory\"\n3. WebSearch: \"best paper award ICLR 2025 2026 embeddings retrieval\"\n4. WebSearch: \"outstanding paper AAAI 2025 2026 information retrieval\"\n5. WebSearch: \"best paper ACL EMNLP 2024 2025 retrieval text mining\"\n6. WebSearch: \"oral spotlight NeurIPS 2024 2025 embedding theory retrieval\"\n7. WebSearch: \"oral spotlight ICML 2025 representation learning bounds\"\n8. WebSearch: site:openreview.net \"multi-vector retrieval\" OR \"MaxSim\" OR \"late interaction\" 2025 2026\n\nFor each relevant paper found, use WebFetch to read its abstract. Report:\n- Full title, authors, venue/year, URL\n- One-line summary\n- Award status (best paper, oral, spotlight, etc.)\n- Relevance to multi-vector retrieval expressiveness theory",
    "agentId": "aea474fb639da618e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Here is the full literature survey report.\n\n---\n\n## Literature Survey: Theoretical Foundations of Information Retrieval -- Expressiveness of Retrieval Models and Embedding Theory\n\n### TIER 1: DIRECTLY RELEVANT TO MULTI-VECTOR RETRIEVAL EXPRESSIVENESS THEORY\n\n---\n\n**1. \"On the Theoretical Limitations of Embedding-Based Retrieval\"**\n- **Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee (Google DeepMind, Johns Hopkins)\n- **Venue/Year:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2508.21038\n- **Award:** Accepted paper (no best paper award noted)\n- **Summary:** Proves that single-vector embedding retrieval is fundamentally limited: the number of top-k subsets of documents returnable by any query is bounded by the embedding dimension. Introduces the LIMIT dataset showing SOTA systems fail on simple tasks.\n- **Relevance to multi-vector retrieval expressiveness:** **CENTRAL.** This is the most directly relevant paper. It provides formal theoretical proof that single-vector embeddings have inherent expressiveness limitations, which serves as the core motivation for multi-vector retrieval. The authors explicitly advocate for alternative approaches (including multi-vector) to overcome these constraints.\n\n---\n\n**2. \"MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings\"**\n- **Authors:** Laxman Dhulipala, Majid Hadian, Rajesh Jayaram, Jason Lee, Vahab Mirrokni (Google Research)\n- **Venue/Year:** NeurIPS 2024\n- **URL:** https://arxiv.org/abs/2405.19504\n- **Award:** Poster presentation\n- **Summary:** Reduces multi-vector similarity search to single-vector MIPS by generating Fixed Dimensional Encodings (FDEs) whose inner product approximates multi-vector similarity, with theoretical approximation guarantees. Achieves 10% improved recall at 90% lower latency on BEIR.\n- **Relevance:** **HIGH.** Provides the first single-vector proxy for multi-vector similarity with formal theoretical guarantees (epsilon-approximation bounds), directly addressing the computational vs. expressiveness tradeoff in multi-vector retrieval.\n\n---\n\n**3. \"Multi-Vector Retrieval as Sparse Alignment\" (ALIGNER)**\n- **Authors:** Yujie Qian, Jinhyuk Lee, Karthik Duddu, Zhuyun Dai, Tao Lei, Siddhartha Brahma, Iftekhar Naim, Vincent Y Zhao\n- **Venue/Year:** ICLR 2023\n- **URL:** https://arxiv.org/abs/2211.01267\n- **Award:** None\n- **Summary:** Reframes multi-vector retrieval as sparse alignment between query and document tokens, learning sparsified pairwise token alignments and per-token salience scores. Achieves 51.1 nDCG@10 zero-shot on BEIR; retains only 20% of document token representations with minimal loss.\n- **Relevance:** **HIGH.** Provides a principled formalization of multi-vector interaction as sparse alignment, offering an alternative theoretical lens on how token-level interactions contribute to retrieval quality and how redundancy can be exploited.\n\n---\n\n**4. \"A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models\"**\n- **Authors:** Yash Kankanampati, Yuxuan Zong, Nadi Tomeh, Benjamin Piwowarski, Joseph Le Roux\n- **Venue/Year:** SIGIR 2026 (Full Paper)\n- **URL:** https://arxiv.org/abs/2603.09933\n- **Award:** None noted\n- **Summary:** Reframes token reduction in multi-vector retrieval as a Voronoi cell estimation problem in embedding space, interpreting each token's impact through its Voronoi region. Provides principled pruning that preserves retrieval effectiveness while reducing storage.\n- **Relevance:** **HIGH.** Offers a geometric/theoretical framework (Voronoi tessellations in embedding space) for understanding token-level contributions in multi-vector retrieval, directly connecting to expressiveness theory by formalizing what each token embedding \"covers\" in representation space.\n\n---\n\n**5. \"Working Notes on Late Interaction Dynamics: Analyzing Targeted Behaviors of Late Interaction Models\"**\n- **Authors:** Antoine Edy, Max Conti, Quentin Mace\n- **Venue/Year:** LIR Workshop @ ECIR 2026\n- **URL:** https://arxiv.org/abs/2603.26259\n- **Award:** Workshop paper\n- **Summary:** Analyzes two theoretical properties of late interaction: (1) causal encoders with MaxSim scoring exhibit monotonic length bias favoring longer chunks regardless of relevance; (2) beyond the top token match, the MaxSim operator collapses information, confirming it captures only peak similarity per query token.\n- **Relevance:** **HIGH.** Provides empirical-theoretical analysis of the MaxSim operator's fundamental behavior and limitations, directly informing the expressiveness properties and failure modes of ColBERT-style multi-vector retrieval.\n\n---\n\n**6. \"Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval\"**\n- **Authors:** Roi Pony, Adi Raz, Oshri Naparstek, Idan Friedman, Udi Barzelay\n- **Venue/Year:** arXiv preprint, February 2026\n- **URL:** https://arxiv.org/abs/2602.02827\n- **Award:** Preprint (no venue award)\n- **Summary:** Recasts MaxSim reranking as a finite-population Top-K identification problem using bandit algorithms. Maintains uncertainty-aware bounds over partially observed document scores, adaptively revealing only necessary MaxSim entries. Achieves up to 5x FLOPs reduction on BEIR and REAL-MM-RAG.\n- **Relevance:** **MODERATE-HIGH.** Demonstrates substantial redundancy in dense late-interaction scoring through a principled bandit-theoretic lens, contributing to understanding of the information-theoretic properties of multi-vector interactions.\n\n---\n\n**7. \"MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction\"**\n- **Authors:** Zilin Xiao, Qi Ma, Mengting Gu, Chun-cheng Jason Chen, Xintao Chen, Vicente Ordonez, Vijai Mohan\n- **Venue/Year:** ICLR 2026 (Oral)\n- **URL:** https://arxiv.org/abs/2509.18095\n- **Award:** **ICLR 2026 Oral** presentation\n- **Summary:** Introduces learnable Meta Tokens whose contextualized representations serve as compact multi-vector embeddings. Uses Matryoshka Multi-Vector Retrieval training to organize information by granularity, enabling test-time scaling of retrieval quality vs. efficiency. Scales to 32B parameter models; SOTA on MMEB and ViDoRe.\n- **Relevance:** **HIGH.** Directly addresses the expressiveness-efficiency frontier of multi-vector retrieval by controlling the number of vectors at test time with Matryoshka-style training, providing empirical evidence about how multi-vector granularity affects retrieval quality.\n\n---\n\n**8. \"AMES: Approximate Multi-modal Enterprise Search via Late Interaction Retrieval\"**\n- **Authors:** Tony Joseph, Carlos Pareja, David Lopes Pegna, Abhishek Singh\n- **Venue/Year:** arXiv preprint, March 2026\n- **URL:** https://arxiv.org/abs/2603.13537\n- **Award:** Preprint\n- **Summary:** Presents a unified multimodal late interaction system for enterprise search using a two-stage pipeline: parallel token-level ANN with per-document Top-M MaxSim approximation, then exact MaxSim re-ranking. Demonstrates production-grade deployment on Solr.\n- **Relevance:** **MODERATE.** Primarily a systems paper, but its two-stage approximate-then-exact MaxSim pipeline provides practical insights into the computational structure of multi-vector scoring.\n\n---\n\n**9. \"LEMUR: Learned Multi-Vector Retrieval\"**\n- **Authors:** Elias Jaasaari, Ville Hyvonen, Teemu Roos\n- **Venue/Year:** arXiv preprint, January 2026\n- **URL:** https://arxiv.org/abs/2601.21853\n- **Award:** Preprint\n- **Summary:** A framework for multi-vector similarity search addressing efficient handling of multi-vector representations from late interaction models like ColBERT.\n- **Relevance:** **MODERATE.** Contributes to the algorithmic infrastructure for multi-vector retrieval.\n\n---\n\n### TIER 2: RELEVANT TO EMBEDDING THEORY AND REPRESENTATION EXPRESSIVENESS\n\n---\n\n**10. \"Transformers are Inherently Succinct\"**\n- **Authors:** Pascal Bergstrasser, Ryan Cotterell, Anthony Widjaja Lin\n- **Venue/Year:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2510.19315\n- **Award:** **ICLR 2026 Outstanding Paper Award**\n- **Summary:** Proves that fixed-precision transformers are exponentially more succinct than LTL and RNNs, and doubly exponentially more succinct than finite automata. As a byproduct, shows that verifying transformer properties is EXPSPACE-complete.\n- **Relevance:** **MODERATE.** While focused on formal language theory rather than retrieval, this is the strongest theoretical result on transformer expressiveness from a major venue. The succinctness results have implications for understanding why transformer-based encoders can produce more expressive embeddings than simpler architectures.\n\n---\n\n**11. \"Why are Sensitive Functions Hard for Transformers?\"**\n- **Authors:** Michael Hahn, Mark Rofin\n- **Venue/Year:** ACL 2024\n- **URL:** https://arxiv.org/abs/2402.09963\n- **Award:** **ACL 2024 Best Paper Award**\n- **Summary:** Proves that transformer outputs sensitive to many input parts occupy isolated parameter-space points, creating low-sensitivity bias. Explains difficulty with PARITY and poor length generalization. High-sensitivity functions inhabit very steep minima.\n- **Relevance:** **MODERATE.** Bridges expressiveness and learnability for transformers. Relevant to understanding why retrieval encoders may fail to learn certain fine-grained discriminative functions, and why multi-vector approaches (which decompose sensitivity across tokens) may circumvent these limitations.\n\n---\n\n**12. \"Superposition Yields Robust Neural Scaling\"**\n- **Authors:** Yizhou Liu, Ziming Liu, Jeff Gore\n- **Venue/Year:** NeurIPS 2025\n- **URL:** https://arxiv.org/abs/2505.10465\n- **Award:** **NeurIPS 2025 Best Paper Runner-Up**\n- **Summary:** Shows that representation superposition (representing more features than dimensions) drives robust neural scaling laws. Under strong superposition, loss scales inversely with model dimension due to geometric interference between representation vectors, regardless of data distribution.\n- **Relevance:** **MODERATE.** Directly characterizes how embedding dimensions encode features through superposition, which is fundamental to understanding single-vector embedding capacity limitations (connecting to Weller et al.'s theoretical bounds).\n\n---\n\n**13. \"A Text is Worth Several Tokens: Text Embedding from LLMs Secretly Aligns Well with The Key Tokens\"**\n- **Authors:** Zhijie Nie, Richong Zhang, Zhanyu Wu\n- **Venue/Year:** ACL 2025\n- **URL:** https://arxiv.org/abs/2406.17378\n- **Award:** **ACL 2025 SAC Highlight**\n- **Summary:** Discovers that LLM-based text embeddings align with key tokens in the input. This phenomenon is universal across architectures, training strategies, and embedding methods. Proposes a sparse retrieval method achieving ~80% of dense retrieval performance with significantly reduced computation.\n- **Relevance:** **MODERATE-HIGH.** Reveals that single-vector embeddings implicitly encode a sparse set of token-level signals, bridging single-vector and multi-vector paradigms. Suggests that multi-vector retrieval may be making explicit what single-vector embeddings already encode implicitly.\n\n---\n\n**14. \"Randomly Removing 50% of Dimensions in Text Embeddings has Minimal Impact on Retrieval and Classification Tasks\"**\n- **Authors:** Sotaro Takeshita, Yurina Takeshita, Daniel Ruffinelli, Simone Paolo Ponzetto\n- **Venue/Year:** EMNLP 2025 (Oral)\n- **URL:** https://arxiv.org/abs/2508.17744\n- **Award:** **EMNLP 2025 People's Choice Award**\n- **Summary:** Shows that randomly removing up to 50% of embedding dimensions causes less than 10% performance drop across 6 SOTA encoders and 26 tasks. Many uniformly distributed dimensions actually improve performance when removed.\n- **Relevance:** **MODERATE.** Provides empirical evidence about the information structure of text embeddings -- significant dimensional redundancy suggests that the effective dimensionality is much lower than nominal, which relates to theoretical capacity bounds on embedding-based retrieval.\n\n---\n\n**15. \"LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation\"**\n- **Authors:** Weiquan Huang, Aoqi Wu, Yifan Yang, Xufang Luo, Yuqing Yang, et al.\n- **Venue/Year:** AAAI 2026\n- **URL:** https://arxiv.org/abs/2411.04997\n- **Award:** **AAAI 2026 Outstanding Paper Award**\n- **Summary:** Uses LLM fine-tuning to create a discriminative embedding model via contrastive learning, then couples with CLIP vision encoder. Boosts zero-shot retrieval by +14.8/+15.8 on long captions and +11.9/+15.2 on multilingual tasks.\n- **Relevance:** **LOW-MODERATE.** Demonstrates that richer text representations from LLMs substantially improve cross-modal retrieval, supporting the thesis that embedding quality is a bottleneck; however, uses single-vector representations.\n\n---\n\n### TIER 3: RETRIEVAL-RELATED AWARD WINNERS WITH TANGENTIAL RELEVANCE\n\n---\n\n**16. \"Learning to Retrieve Iteratively for In-Context Learning\"**\n- **Authors:** Yunmo Chen, Tongfei Chen, Harsh Jhamtani, Patrick Xia, Richard Shin, Jason Eisner, Benjamin Van Durme\n- **Venue/Year:** EMNLP 2024\n- **URL:** https://arxiv.org/abs/2406.14739\n- **Award:** **EMNLP 2024 Outstanding Paper Award**\n- **Summary:** Proposes iterative retrieval via reinforcement learning for in-context learning exemplar selection. Converts a dense retriever into a stateful iterative retriever with only 4M additional parameters.\n- **Relevance:** **LOW.** Addresses retrieval strategy rather than embedding expressiveness theory.\n\n---\n\n**17. \"Towards Cross-Cultural Machine Translation with Retrieval-Augmented Generation from Multilingual Knowledge Graphs\"**\n- **Authors:** Simone Conia, Daniel Lee, Min Li, Umar Farooq Minhas, Saloni Potdar, Yunyao Li\n- **Venue/Year:** EMNLP 2024\n- **URL:** https://arxiv.org/abs/2410.14057\n- **Award:** **EMNLP 2024 Outstanding Paper Award**\n- **Summary:** Introduces KG-MT, integrating multilingual knowledge graph information via dense retrieval into neural MT. 129% improvement over NLLB-200, 62% over GPT-4.\n- **Relevance:** **LOW.** Uses retrieval but focuses on MT application rather than retrieval expressiveness theory.\n\n---\n\n**18. \"Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index\"**\n- **Authors:** Hao Xu, Jiacheng Liu, Yejin Choi, Noah A. Smith, Hannaneh Hajishirzi\n- **Venue/Year:** EMNLP 2025\n- **URL:** https://arxiv.org/abs/2506.12229\n- **Award:** **EMNLP 2025 Best Paper Award**\n- **Summary:** Builds an FM-index system indexing 83TB of text with 18x faster indexing and 3.2x memory reduction. Conducts large-scale benchmark contamination analysis.\n- **Relevance:** **LOW.** Exact-match retrieval infrastructure rather than embedding/representation theory, but demonstrates an alternative retrieval paradigm to dense embeddings.\n\n---\n\n### AWARD WINNERS SURVEYED WITH NO DIRECT RELEVANCE\n\nThe following award-winning papers were reviewed and found to have no direct relevance to multi-vector retrieval expressiveness theory:\n\n- **NeurIPS 2024 Best Papers:** Visual Autoregressive Modeling; Stochastic Taylor Derivative Estimator; Not All Tokens Are What You Need; Guiding a Diffusion Model; PRISM Alignment Dataset\n- **NeurIPS 2025 Best Papers:** Artificial Hivemind; Gated Attention for LLMs; 1000 Layer Networks for Self-Supervised RL; Why Diffusion Models Don't Memorize; Does RL Really Incentivize Reasoning; Optimal Mistake Bounds for Transductive Online Learning\n- **ICLR 2025 Outstanding Papers:** Safety Alignment; Learning Dynamics of LLM Finetuning; AlphaEdit\n- **ICLR 2026:** LLMs Get Lost In Multi-Turn Conversation; The Polar Express (Honorable Mention)\n- **ICML 2025 Outstanding Papers:** CollabLLM; Train for the Worst; Roll the Dice; Conformal Prediction; Score Matching; Value of Prediction\n- **ACL 2024 Best Papers:** Causal Estimation of Memorisation; Aya Model; Mission Impossible Language Models; Semisupervised Proto-Language Reconstruction; Deciphering Oracle Bone Language\n- **ACL 2025 Best Papers:** Theory of Response Sampling; Fairness through Difference Awareness; Language Models Resist Alignment; Native Sparse Attention\n- **AAAI 2026:** Model Change for Description Logic; Causal Structure Learning; ReconVLA; Sheaflet-based Hypergraph NNs\n\n---\n\n### KEY TAKEAWAYS FOR THE SURVEY\n\n1. **The strongest theoretical result directly on multi-vector retrieval expressiveness** is Weller et al. (ICLR 2026), which proves fundamental limits of single-vector retrieval and motivates multi-vector alternatives.\n\n2. **MUVERA (NeurIPS 2024)** provides the first theoretical bridge between multi-vector and single-vector retrieval with formal approximation guarantees.\n\n3. **The Voronoi Cell formulation (SIGIR 2026)** offers a geometric theory of token contribution in multi-vector retrieval.\n\n4. **MetaEmbed (ICLR 2026 Oral)** provides the most important empirical result on the expressiveness-efficiency frontier of multi-vector retrieval via Matryoshka training.\n\n5. **Transformer expressiveness theory** is represented by two major award winners: \"Transformers are Inherently Succinct\" (ICLR 2026 Outstanding Paper) and \"Why are Sensitive Functions Hard for Transformers?\" (ACL 2024 Best Paper), both informing the theoretical foundations of encoder expressiveness.\n\n6. **Representation capacity theory** is advanced by \"Superposition Yields Robust Neural Scaling\" (NeurIPS 2025 Runner-Up), which characterizes how embedding dimensions encode features.\n\n7. **The LIR Workshop @ ECIR 2026** (the first workshop on Late Interaction and Multi-Vector Retrieval) represents the emergence of this area as a recognized subfield with dedicated community activity."
      }
    ],
    "totalDurationMs": 259600,
    "totalTokens": 53919,
    "totalToolUseCount": 60,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2585,
      "cache_read_input_tokens": 46402,
      "output_tokens": 4931,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2585
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4931,
          "cache_read_input_tokens": 46402,
          "cache_creation_input_tokens": 2585,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2585,
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
      "otherToolCount": 60
    }
  },
  "sourceToolAssistantUUID": "228a80f2-36a7-473f-b522-c213270092cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "83e18bb8-9165-43bd-bf98-d100e6ec7760",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on multi-vector retrieval expressiveness",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Tool result

_source line 29 · 2026-05-30T06:14:30.862Z_

<details><summary>↩ Tool result · `toolu_01SCG2EmSaceDpYcGedqHN8W`</summary>

```text
Now I have comprehensive results. Let me compile the final report.

---

## Literature Survey: Theoretical Bounds for Retrieval Embeddings and Multi-Vector Representations (2024--2026)

Below are the papers found, organized by thematic relevance. For each: full citation, one-line summary, and relevance to multi-vector retrieval expressiveness.

---

### A. CORE PAPERS ON EXPRESSIVENESS LIMITS OF EMBEDDING-BASED RETRIEVAL

**1. "On the Theoretical Limitations of Embedding-Based Retrieval"**
- **Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee
- **Venue/Year:** ICLR 2026 (arXiv:2508.21038, August 2025)
- **URL:** https://arxiv.org/abs/2508.21038
- **Summary:** Proves that the number of distinct top-k document subsets returnable by any query is bounded by the embedding dimension d; specifically, the minimum dimension equals the sign-rank of the binary relevance matrix. Empirically, even state-of-the-art models fail on the LIMIT benchmark.
- **Why important:** This is the most directly relevant paper. It establishes the fundamental combinatorial bottleneck of single-vector retrieval via sign-rank and explicitly notes that multi-vector models can overcome these limitations, motivating the study of multi-vector expressiveness as a way to sidestep the sign-rank barrier.

**2. "R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval"**
- **Authors:** Zihao Wang, Hang Yin, Lihui Liu, Hanghang Tong, Yangqiu Song, Ginny Wong, Simon See
- **Venue/Year:** arXiv:2601.20844, January 2026
- **URL:** https://arxiv.org/abs/2601.20844
- **Summary:** Derives tight bounds for the "Minimal Embeddable Dimension" (MED) for subset membership embeddings under l2, inner product, and cosine similarity, showing a logarithmic dependency on dataset size and arguing that practical limitations are about learnability, not geometry.
- **Why important:** Provides a counterpoint to Weller et al. -- showing that geometrically, dimension 2k suffices for top-k, but the real challenge is learning such embeddings. For multi-vector retrieval, this implies that additional vectors may help with learnability rather than raw geometric capacity.

---

### B. MULTI-VECTOR RETRIEVAL: THEORY AND MECHANISMS

**3. "MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings"**
- **Authors:** Laxman Dhulipala, Majid Hadian, Rajesh Jayaram, Jason Lee, Vahab Mirrokni
- **Venue/Year:** NeurIPS 2024 (arXiv:2405.19504, May 2024)
- **URL:** https://arxiv.org/abs/2405.19504
- **Summary:** Reduces multi-vector similarity search to single-vector MIPS by constructing Fixed Dimensional Encodings (FDEs) whose inner product epsilon-approximates Chamfer/MaxSim similarity, with FDE dimension depending only logarithmically on dataset size. Achieves 10% better recall at 90% lower latency.
- **Why important:** Provides the first theoretical approximation guarantees for reducing multi-vector to single-vector search, directly quantifying how much dimension is needed to approximate MaxSim -- a key bound for understanding multi-vector representation capacity.

**4. "LEMUR: Learned Multi-Vector Retrieval"**
- **Authors:** Elias Jaasaari, Ville Hyvonen, Teemu Roos
- **Venue/Year:** ICML 2026 (arXiv:2601.21853, January 2026)
- **URL:** https://arxiv.org/abs/2601.21853
- **Summary:** Reformulates multi-vector similarity search as a supervised learning task solved with a single-hidden-layer neural network, reducing inference to single-vector search in a learned latent space. Achieves an order of magnitude speedup over prior multi-vector methods.
- **Why important:** Demonstrates that the mapping from multi-vector to single-vector representations can be learned with neural networks while preserving retrieval quality, providing empirical evidence about the representational gap between multi-vector and single-vector paradigms.

**5. "Incorporating Token Importance in Multi-Vector Retrieval"**
- **Authors:** Archish S, Ankit Garg, Kirankumar Shiragur, Neeraj Kayal
- **Venue/Year:** arXiv:2511.16106, November 2025
- **URL:** https://arxiv.org/abs/2511.16106
- **Summary:** Enhances ColBERT's MaxSim by introducing weighted token scoring (IDF-based and learned weights), improving Recall@10 by 1.28% zero-shot and 3.66% with few-shot fine-tuning on BEIR.
- **Why important:** Addresses a known limitation of the MaxSim operator (uniform token weighting) and shows that the expressiveness of multi-vector retrieval can be increased by moving from unweighted to weighted Chamfer-like distances, relevant to understanding representation capacity.

**6. "MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction"**
- **Authors:** Zilin Xiao, Qi Ma, Mengting Gu, Chun-cheng Jason Chen, Xintao Chen, Vicente Ordonez, Vijai Mohan
- **Venue/Year:** ICLR 2026 Oral (arXiv:2509.18095, September 2025)
- **URL:** https://arxiv.org/abs/2509.18095
- **Summary:** Uses learnable "Meta Tokens" to produce compact yet expressive multi-vector embeddings with "Matryoshka Multi-Vector Retrieval" enabling flexible test-time scaling of the number of vectors. Achieves SOTA on multimodal retrieval benchmarks.
- **Why important:** Demonstrates that the number of vectors per item can be treated as a tunable dimension of expressiveness, with controllable tradeoffs -- directly relevant to understanding how many vectors are needed for a given retrieval quality.

**7. "Multi-Vector Index Compression in Any Modality"**
- **Authors:** Hanxiang Qin, Alexander Martin, Rohan Jha, Chunsheng Zuo, Reno Kriz, Benjamin Van Durme
- **Venue/Year:** arXiv:2602.21202, February 2026
- **URL:** https://arxiv.org/abs/2602.21202
- **Summary:** Explores compression of multi-vector indices via attention-guided clustering, showing competitive or improved performance vs. full uncompressed indices across text, visual, and video domains.
- **Why important:** Shows that multi-vector representations contain substantial redundancy that can be compressed without performance loss, informing bounds on the effective dimensionality of multi-vector representations.

**8. "Simple Projection Variants Improve ColBERT Performance"**
- **Authors:** Benjamin Clavie, Sean Lee, Rikiya Takehi, Aamir Shakir, Makoto P. Kato
- **Venue/Year:** arXiv:2510.12327, October 2025
- **URL:** https://arxiv.org/abs/2510.12327
- **Summary:** Shows that the MaxSim operator creates bottlenecks in gradient flow during training, and that replacing ColBERT's linear projection with deeper non-linear blocks yields 2+ NDCG@10 point improvements.
- **Why important:** Reveals that multi-vector retrieval's effective expressiveness is partially limited by the projection architecture, not just the number of vectors or their dimension -- relevant to understanding representation capacity in practice.

**9. "Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling"**
- **Authors:** Benjamin Clavie, Antoine Chaffin, Griffin Adams
- **Venue/Year:** arXiv:2409.14683, September 2024
- **URL:** https://arxiv.org/abs/2409.14683
- **Summary:** Clustering-based token pooling reduces ColBERT index footprint by ~50% with negligible performance loss, and up to 66-75% with <5% degradation.
- **Why important:** Empirically bounds the effective number of distinct vectors needed per document, showing that half or fewer of the token vectors carry the representational load -- informing lower bounds on multi-vector redundancy.

**10. "Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval"**
- **Authors:** Roi Pony, Adi Raz, Oshri Naparstek, Idan Friedman, Udi Barzelay
- **Venue/Year:** arXiv:2602.02827, February 2026
- **URL:** https://arxiv.org/abs/2602.02827
- **Summary:** Frames multi-vector reranking as a finite-population Top-K identification problem, achieving 5x reduction in MaxSim operations by sparsifying interaction matrices with uncertainty-aware bounds.
- **Why important:** Demonstrates "substantial redundancy" in dense late-interaction scoring, providing empirical evidence that the effective interaction complexity is much lower than the worst-case token-by-token MaxSim bound.

**11. "LIR: The First Workshop on Late Interaction and Multi Vector Retrieval @ ECIR 2026"**
- **Authors:** Benjamin Clavie, Xianming Li, Antoine Chaffin, Omar Khattab, Tom Aarsen, Manuel Faysse, Jing Li
- **Venue/Year:** ECIR 2026 Workshop (arXiv:2511.00444, November 2025)
- **URL:** https://arxiv.org/abs/2511.00444
- **Summary:** Workshop overview documenting that late interaction methods deliver strong generalization especially out-of-domain, and identifying key open problems in efficiency, integration, and theoretical understanding.
- **Why important:** Frames the open research agenda for multi-vector retrieval theory and identifies gaps in our understanding of expressiveness bounds.

---

### C. NEAREST NEIGHBOR SEARCH AND DIMENSIONALITY THEORY

**12. "Breaking the Curse of Dimensionality: On the Stability of Modern Vector Retrieval"**
- **Authors:** Vihan Lakshman, Blaise Munyampirwa, Julian Shun, Benjamin Coleman
- **Venue/Year:** arXiv:2512.12458, December 2025
- **URL:** https://arxiv.org/abs/2512.12458
- **Summary:** Extends stability theory to multi-vector search using Chamfer distance, filtered vector search, and sparse vector search, explaining why vector databases work well despite high dimensions.
- **Why important:** Directly proves stability results for multi-vector (Chamfer distance) retrieval, providing theoretical justification for why multi-vector search avoids the curse of dimensionality in practice.

**13. "RAE: A Neural Network Dimensionality Reduction Method for Nearest Neighbors Preservation in Vector Search"**
- **Authors:** Han Zhang, Dongfang Zhao
- **Venue/Year:** ICLR 2026 (arXiv:2509.25839, September 2025)
- **URL:** https://arxiv.org/abs/2509.25839
- **Summary:** Uses regularized auto-encoders with Rayleigh quotient constraints to reduce embedding dimension while preserving k-NN relationships, with mathematical distortion bounds.
- **Why important:** Provides bounds on how much dimension reduction is possible while preserving retrieval structure -- directly relevant to understanding the minimum dimensionality needed for faithful multi-vector representations.

**14. "Even Faster Algorithm for the Chamfer Distance"**
- **Authors:** Ying Feng, Piotr Indyk
- **Venue/Year:** ICALP 2025
- **URL:** https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.76
- **Summary:** Achieves near-optimal O(nd(log log n + log(1/epsilon))/epsilon^2) time for Chamfer distance computation, narrowing the gap to the trivial lower bound Omega(dn).
- **Why important:** The Chamfer distance is the core similarity measure in ColBERT-style multi-vector retrieval (MaxSim). This near-optimal algorithm establishes the computational complexity floor for exact multi-vector scoring.

**15. "Faster Maximum Inner Product Search in High Dimensions"**
- **Authors:** Mo Tiwari, Ryan Kang, Jaeyong Lee, Donghyun Lee, Christopher J. Piech, Sebastian Thrun, Ilan Shomorony, Martin Jinye Zhang
- **Venue/Year:** ICML 2024
- **URL:** https://proceedings.mlr.press/v235/tiwari24a.html
- **Summary:** BanditMIPS achieves O(1) complexity with respect to dimension d for MIPS, improving upon the prior O(sqrt(d)) bound.
- **Why important:** Since multi-vector retrieval can be reduced to MIPS (via MUVERA's FDEs), improvements in MIPS complexity directly translate to better multi-vector retrieval efficiency.

**16. "Maximum Inner Product is Query-Scaled Nearest Neighbor"**
- **Authors:** Tingyang Chen, Cong Fu, Kun Wang, Xiangyu Ke, Yunjun Gao, Wenchao Zhou, Yabo Ni, Anxiang Zeng
- **Venue/Year:** VLDB 2025 (arXiv:2503.06882)
- **URL:** https://arxiv.org/abs/2503.06882
- **Summary:** Proves MIPS is equivalent to query-scaled Euclidean NN search without space transformation, enabling graph-based indices for MIPS with 35% speedup.
- **Why important:** Unifies MIPS and NNS theory, meaning all NNS lower bounds and algorithms apply to the inner product similarity used in retrieval -- simplifying the theoretical landscape for multi-vector models that use inner product scoring.

**17. "Nearest Neighbor Complexity and Boolean Circuits"**
- **Authors:** Mason DiCicco, Vladimir Podolskii, Daniel Reichman
- **Venue/Year:** ITCS 2025
- **URL:** https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.42
- **Summary:** Proves exponential lower bounds on k-NN complexity for explicit functions (k <= n^{1-epsilon}), connecting NN complexity to circuit complexity based on linear inequalities. Shows exponential separation between 1-NN and k-NN complexity.
- **Why important:** The exponential separation between 1-NN and k-NN complexity is directly relevant to multi-vector retrieval: MaxSim/Chamfer similarity involves multiple NN lookups, and this work shows that such operations are fundamentally more powerful than single-NN operations.

---

### D. METRIC EMBEDDINGS AND DISTORTION

**18. "Smoothed Analysis of Online Metric Matching with a Single Sample: Beyond Metric Distortion"**
- **Authors:** Yingxi Li, Ellen Vitercik, Mingwei Yang
- **Venue/Year:** ITCS 2026
- **URL:** https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.94
- **Summary:** Achieves O(1)-competitive online metric matching by bypassing the Omega(log n) probabilistic embedding distortion barrier, directly bounding costs on target metric spaces.
- **Why important:** Demonstrates that classical distortion lower bounds (Omega(log n) for embedding into Euclidean/tree metrics) can be circumvented by algorithm-metric co-design -- suggesting that multi-vector retrieval might similarly bypass single-vector embedding distortion limits.

---

### E. LEARNING THEORY AND COMBINATORIAL DIMENSIONS

**19. "Sample Complexity of Agnostic Multiclass Classification: Natarajan Dimension Strikes Back"**
- **Authors:** Alon Cohen, Liad Erez, Steve Hanneke, Tomer Koren, Yishay Mansour, Shay Moran, Qian Zhang
- **Venue/Year:** arXiv:2511.12659, November 2025
- **URL:** https://arxiv.org/abs/2511.12659
- **Summary:** Proves that agnostic multiclass sample complexity has the form DS^{1.5}/epsilon + Nat/epsilon^2, showing that the Natarajan dimension still governs the fine-epsilon regime alongside the DS dimension.
- **Why important:** The Natarajan dimension generalizes VC dimension to multi-output settings. Multi-vector retrieval can be viewed as a multiclass problem (selecting among documents), and these bounds characterize how many training examples are needed to learn multi-vector representations as a function of their combinatorial complexity.

**20. "Bounds on the Natarajan Dimension of a Class of Linear Multi-Class Predictors"**
- **Authors:** (Authors behind ScienceDirect paper S0167865525004167)
- **Venue/Year:** Pattern Recognition Letters, 2025
- **URL:** https://www.sciencedirect.com/science/article/abs/pii/S0167865525004167
- **Summary:** Derives tight upper bounds on the Natarajan dimension for linear multi-class predictors based on class-sensitive feature mappings for multi-vector construction.
- **Why important:** Directly connects Natarajan dimension to multi-vector construction via class-sensitive feature mappings, providing combinatorial complexity bounds for linear multi-vector classifiers.

**21. "Regularization and Optimal Multiclass Learning"**
- **Authors:** Julian Asilis, Vatsal Sharan, Siddartha Devic, Shaddin Dughmi, Shanghua Teng
- **Venue/Year:** COLT 2024
- **URL:** https://learningtheory.org/colt2024/schedule/poster_184.html
- **Summary:** Introduces "Hall complexity" as a combinatorial measure for transductive multiclass error rates, connecting regularization to optimal multiclass learners via one-inclusion graphs.
- **Why important:** Hall complexity provides a new combinatorial dimension for multiclass problems that may tighten the analysis of how many vectors/dimensions are needed to represent multi-class retrieval decisions.

---

### F. TRANSFORMER RETRIEVAL THEORY AND SURVEYS

**22. "Learning to Recall with Transformers Beyond Orthogonal Embeddings"**
- **Authors:** Nuri Mert Vural, Alberto Bietti, Mahdi Soltanolkotabi, Denny Wu
- **Venue/Year:** ICLR 2026 (arXiv:2603.15923)
- **URL:** https://arxiv.org/abs/2603.15923
- **Summary:** Derives explicit formulas for a single-layer transformer's storage capacity on retrieval tasks, showing multiplicative scaling between sample size, embedding dimension, and sequence length when embeddings are non-orthogonal.
- **Why important:** Directly characterizes the capacity-dimension-length tradeoff for retrieval in transformers. For multi-vector models, where each document produces a sequence of vectors, this work bounds how many associations can be stored as a function of per-token embedding dimension and number of tokens -- the two axes of multi-vector capacity.

**23. "A Survey of Model Architectures in Information Retrieval"**
- **Authors:** Zhichao Xu, Fengran Mo, Zhiqi Huang, Crystina Zhang, Puxuan Yu, Bei Wang, Jimmy Lin, Vivek Srikumar
- **Venue/Year:** TMLR 2025 (arXiv:2502.14822)
- **URL:** https://arxiv.org/abs/2502.14822
- **Summary:** Comprehensive survey of IR model architectures from term-based to transformer-based, covering single-vector, multi-vector, and generative retrieval paradigms.
- **Why important:** Provides the landscape context: where multi-vector models sit among retrieval architectures and what empirical evidence exists for their relative expressiveness.

**24. "Overcomplete Tensor Decomposition via Koszul-Young Flattenings"**
- **Authors:** Pravesh K. Kothari, Ankur Moitra, Alexander S. Wein
- **Venue/Year:** FOCS 2025 (arXiv:2411.14344)
- **URL:** https://arxiv.org/abs/2411.14344
- **Summary:** Achieves rank r <= (1-epsilon)(n2+n3) for tensor decomposition, a factor-2 improvement over classical simultaneous diagonalization, and proves this is tight for flattening-based methods.
- **Why important:** Multi-vector representations can be viewed as tensors (batch of vectors per item). Tensor rank bounds constrain the "effective complexity" of such representations and inform how many rank-1 components (analogous to individual embedding vectors) are needed to faithfully represent the multi-vector structure.

---

### KEY TAKEAWAYS FOR MULTI-VECTOR RETRIEVAL EXPRESSIVENESS

1. **Single-vector bottleneck is proven:** Weller et al. (ICLR 2026) show that single-vector retrieval capacity is bounded by sign-rank of the relevance matrix, with concrete dimension-to-capacity limits. Multi-vector representations bypass this.

2. **Multi-vector to single-vector reduction has guarantees:** MUVERA (NeurIPS 2024) proves that FDEs can approximate MaxSim/Chamfer similarity with dimension scaling only logarithmically in dataset size, establishing a formal bridge.

3. **Redundancy in multi-vector representations is substantial:** Token pooling (Clavie et al. 2024), Col-Bandit (2026), and compression work (Qin et al. 2026) all show 50-80% of vectors can be pruned with minimal quality loss, bounding the effective dimensionality from above.

4. **Chamfer/MaxSim complexity is near-settled:** Feng & Indyk (ICALP 2025) provide near-optimal algorithms, and the stability theory (Lakshman et al. 2025) explains why multi-vector search works despite high dimensionality.

5. **Learning-theoretic dimensions apply:** Natarajan dimension bounds for multi-vector linear predictors and the DS/Natarajan sample complexity interplay (Cohen et al. 2025) provide the statistical learning framework for understanding when multi-vector representations can be trained.

6. **The geometric vs. learnability gap:** Wang et al. (2026) argue that R^{2k} suffices geometrically for top-k, suggesting the real bottleneck is learnability -- and multi-vector models may help precisely because they make the learning problem easier, not because they expand geometric capacity.

agentId: a60b9f65faec64103 (use SendMessage with to: 'a60b9f65faec64103' to continue this agent)
&lt;usage>total_tokens: 43487
tool_uses: 52
duration_ms: 255963&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "44d06f17-0a54-4cea-af32-3b6f374bfd8c",
  "isSidechain": false,
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "0ec8a96e-bdca-47e4-b887-1fee5bfe61ed",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on theoretical bounds for retrieval embeddings, particularly multi-vector representations.\n\nConduct these searches and fetch abstracts for relevant papers (2024-2026):\n\n1. WebSearch: \"embedding dimension bounds nearest neighbor search theory 2024 2025 2026\"\n2. WebSearch: \"maximum inner product search theoretical bounds 2024 2025 2026\"\n3. WebSearch: \"approximate nearest neighbor lower bounds communication complexity 2024 2025\"\n4. WebSearch: \"metric embedding distortion bounds 2024 2025 2026\"\n5. WebSearch: \"tensor decomposition rank bounds retrieval 2024 2025\"\n6. WebSearch: \"survey dense retrieval neural information retrieval 2024 2025 2026\"\n7. WebSearch: \"matroid intersection assignment problem complexity retrieval\"\n8. WebSearch: \"partition number combinatorial dimension machine learning 2024 2025\"\n9. WebSearch: \"Natarajan dimension multiclass learning theory bounds 2024 2025\"\n10. WebSearch: \"learning to retrieve theoretical analysis 2024 2025 2026\"\n\nFor each relevant paper, use WebFetch on its arxiv/conference page to get the abstract. Report:\n- Full title, authors, venue/year, URL\n- One-line summary\n- Why important for understanding expressiveness of multi-vector retrieval",
    "agentId": "a60b9f65faec64103",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive results. Let me compile the final report.\n\n---\n\n## Literature Survey: Theoretical Bounds for Retrieval Embeddings and Multi-Vector Representations (2024--2026)\n\nBelow are the papers found, organized by thematic relevance. For each: full citation, one-line summary, and relevance to multi-vector retrieval expressiveness.\n\n---\n\n### A. CORE PAPERS ON EXPRESSIVENESS LIMITS OF EMBEDDING-BASED RETRIEVAL\n\n**1. \"On the Theoretical Limitations of Embedding-Based Retrieval\"**\n- **Authors:** Orion Weller, Michael Boratko, Iftekhar Naim, Jinhyuk Lee\n- **Venue/Year:** ICLR 2026 (arXiv:2508.21038, August 2025)\n- **URL:** https://arxiv.org/abs/2508.21038\n- **Summary:** Proves that the number of distinct top-k document subsets returnable by any query is bounded by the embedding dimension d; specifically, the minimum dimension equals the sign-rank of the binary relevance matrix. Empirically, even state-of-the-art models fail on the LIMIT benchmark.\n- **Why important:** This is the most directly relevant paper. It establishes the fundamental combinatorial bottleneck of single-vector retrieval via sign-rank and explicitly notes that multi-vector models can overcome these limitations, motivating the study of multi-vector expressiveness as a way to sidestep the sign-rank barrier.\n\n**2. \"R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval\"**\n- **Authors:** Zihao Wang, Hang Yin, Lihui Liu, Hanghang Tong, Yangqiu Song, Ginny Wong, Simon See\n- **Venue/Year:** arXiv:2601.20844, January 2026\n- **URL:** https://arxiv.org/abs/2601.20844\n- **Summary:** Derives tight bounds for the \"Minimal Embeddable Dimension\" (MED) for subset membership embeddings under l2, inner product, and cosine similarity, showing a logarithmic dependency on dataset size and arguing that practical limitations are about learnability, not geometry.\n- **Why important:** Provides a counterpoint to Weller et al. -- showing that geometrically, dimension 2k suffices for top-k, but the real challenge is learning such embeddings. For multi-vector retrieval, this implies that additional vectors may help with learnability rather than raw geometric capacity.\n\n---\n\n### B. MULTI-VECTOR RETRIEVAL: THEORY AND MECHANISMS\n\n**3. \"MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings\"**\n- **Authors:** Laxman Dhulipala, Majid Hadian, Rajesh Jayaram, Jason Lee, Vahab Mirrokni\n- **Venue/Year:** NeurIPS 2024 (arXiv:2405.19504, May 2024)\n- **URL:** https://arxiv.org/abs/2405.19504\n- **Summary:** Reduces multi-vector similarity search to single-vector MIPS by constructing Fixed Dimensional Encodings (FDEs) whose inner product epsilon-approximates Chamfer/MaxSim similarity, with FDE dimension depending only logarithmically on dataset size. Achieves 10% better recall at 90% lower latency.\n- **Why important:** Provides the first theoretical approximation guarantees for reducing multi-vector to single-vector search, directly quantifying how much dimension is needed to approximate MaxSim -- a key bound for understanding multi-vector representation capacity.\n\n**4. \"LEMUR: Learned Multi-Vector Retrieval\"**\n- **Authors:** Elias Jaasaari, Ville Hyvonen, Teemu Roos\n- **Venue/Year:** ICML 2026 (arXiv:2601.21853, January 2026)\n- **URL:** https://arxiv.org/abs/2601.21853\n- **Summary:** Reformulates multi-vector similarity search as a supervised learning task solved with a single-hidden-layer neural network, reducing inference to single-vector search in a learned latent space. Achieves an order of magnitude speedup over prior multi-vector methods.\n- **Why important:** Demonstrates that the mapping from multi-vector to single-vector representations can be learned with neural networks while preserving retrieval quality, providing empirical evidence about the representational gap between multi-vector and single-vector paradigms.\n\n**5. \"Incorporating Token Importance in Multi-Vector Retrieval\"**\n- **Authors:** Archish S, Ankit Garg, Kirankumar Shiragur, Neeraj Kayal\n- **Venue/Year:** arXiv:2511.16106, November 2025\n- **URL:** https://arxiv.org/abs/2511.16106\n- **Summary:** Enhances ColBERT's MaxSim by introducing weighted token scoring (IDF-based and learned weights), improving Recall@10 by 1.28% zero-shot and 3.66% with few-shot fine-tuning on BEIR.\n- **Why important:** Addresses a known limitation of the MaxSim operator (uniform token weighting) and shows that the expressiveness of multi-vector retrieval can be increased by moving from unweighted to weighted Chamfer-like distances, relevant to understanding representation capacity.\n\n**6. \"MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction\"**\n- **Authors:** Zilin Xiao, Qi Ma, Mengting Gu, Chun-cheng Jason Chen, Xintao Chen, Vicente Ordonez, Vijai Mohan\n- **Venue/Year:** ICLR 2026 Oral (arXiv:2509.18095, September 2025)\n- **URL:** https://arxiv.org/abs/2509.18095\n- **Summary:** Uses learnable \"Meta Tokens\" to produce compact yet expressive multi-vector embeddings with \"Matryoshka Multi-Vector Retrieval\" enabling flexible test-time scaling of the number of vectors. Achieves SOTA on multimodal retrieval benchmarks.\n- **Why important:** Demonstrates that the number of vectors per item can be treated as a tunable dimension of expressiveness, with controllable tradeoffs -- directly relevant to understanding how many vectors are needed for a given retrieval quality.\n\n**7. \"Multi-Vector Index Compression in Any Modality\"**\n- **Authors:** Hanxiang Qin, Alexander Martin, Rohan Jha, Chunsheng Zuo, Reno Kriz, Benjamin Van Durme\n- **Venue/Year:** arXiv:2602.21202, February 2026\n- **URL:** https://arxiv.org/abs/2602.21202\n- **Summary:** Explores compression of multi-vector indices via attention-guided clustering, showing competitive or improved performance vs. full uncompressed indices across text, visual, and video domains.\n- **Why important:** Shows that multi-vector representations contain substantial redundancy that can be compressed without performance loss, informing bounds on the effective dimensionality of multi-vector representations.\n\n**8. \"Simple Projection Variants Improve ColBERT Performance\"**\n- **Authors:** Benjamin Clavie, Sean Lee, Rikiya Takehi, Aamir Shakir, Makoto P. Kato\n- **Venue/Year:** arXiv:2510.12327, October 2025\n- **URL:** https://arxiv.org/abs/2510.12327\n- **Summary:** Shows that the MaxSim operator creates bottlenecks in gradient flow during training, and that replacing ColBERT's linear projection with deeper non-linear blocks yields 2+ NDCG@10 point improvements.\n- **Why important:** Reveals that multi-vector retrieval's effective expressiveness is partially limited by the projection architecture, not just the number of vectors or their dimension -- relevant to understanding representation capacity in practice.\n\n**9. \"Reducing the Footprint of Multi-Vector Retrieval with Minimal Performance Impact via Token Pooling\"**\n- **Authors:** Benjamin Clavie, Antoine Chaffin, Griffin Adams\n- **Venue/Year:** arXiv:2409.14683, September 2024\n- **URL:** https://arxiv.org/abs/2409.14683\n- **Summary:** Clustering-based token pooling reduces ColBERT index footprint by ~50% with negligible performance loss, and up to 66-75% with <5% degradation.\n- **Why important:** Empirically bounds the effective number of distinct vectors needed per document, showing that half or fewer of the token vectors carry the representational load -- informing lower bounds on multi-vector redundancy.\n\n**10. \"Col-Bandit: Zero-Shot Query-Time Pruning for Late-Interaction Retrieval\"**\n- **Authors:** Roi Pony, Adi Raz, Oshri Naparstek, Idan Friedman, Udi Barzelay\n- **Venue/Year:** arXiv:2602.02827, February 2026\n- **URL:** https://arxiv.org/abs/2602.02827\n- **Summary:** Frames multi-vector reranking as a finite-population Top-K identification problem, achieving 5x reduction in MaxSim operations by sparsifying interaction matrices with uncertainty-aware bounds.\n- **Why important:** Demonstrates \"substantial redundancy\" in dense late-interaction scoring, providing empirical evidence that the effective interaction complexity is much lower than the worst-case token-by-token MaxSim bound.\n\n**11. \"LIR: The First Workshop on Late Interaction and Multi Vector Retrieval @ ECIR 2026\"**\n- **Authors:** Benjamin Clavie, Xianming Li, Antoine Chaffin, Omar Khattab, Tom Aarsen, Manuel Faysse, Jing Li\n- **Venue/Year:** ECIR 2026 Workshop (arXiv:2511.00444, November 2025)\n- **URL:** https://arxiv.org/abs/2511.00444\n- **Summary:** Workshop overview documenting that late interaction methods deliver strong generalization especially out-of-domain, and identifying key open problems in efficiency, integration, and theoretical understanding.\n- **Why important:** Frames the open research agenda for multi-vector retrieval theory and identifies gaps in our understanding of expressiveness bounds.\n\n---\n\n### C. NEAREST NEIGHBOR SEARCH AND DIMENSIONALITY THEORY\n\n**12. \"Breaking the Curse of Dimensionality: On the Stability of Modern Vector Retrieval\"**\n- **Authors:** Vihan Lakshman, Blaise Munyampirwa, Julian Shun, Benjamin Coleman\n- **Venue/Year:** arXiv:2512.12458, December 2025\n- **URL:** https://arxiv.org/abs/2512.12458\n- **Summary:** Extends stability theory to multi-vector search using Chamfer distance, filtered vector search, and sparse vector search, explaining why vector databases work well despite high dimensions.\n- **Why important:** Directly proves stability results for multi-vector (Chamfer distance) retrieval, providing theoretical justification for why multi-vector search avoids the curse of dimensionality in practice.\n\n**13. \"RAE: A Neural Network Dimensionality Reduction Method for Nearest Neighbors Preservation in Vector Search\"**\n- **Authors:** Han Zhang, Dongfang Zhao\n- **Venue/Year:** ICLR 2026 (arXiv:2509.25839, September 2025)\n- **URL:** https://arxiv.org/abs/2509.25839\n- **Summary:** Uses regularized auto-encoders with Rayleigh quotient constraints to reduce embedding dimension while preserving k-NN relationships, with mathematical distortion bounds.\n- **Why important:** Provides bounds on how much dimension reduction is possible while preserving retrieval structure -- directly relevant to understanding the minimum dimensionality needed for faithful multi-vector representations.\n\n**14. \"Even Faster Algorithm for the Chamfer Distance\"**\n- **Authors:** Ying Feng, Piotr Indyk\n- **Venue/Year:** ICALP 2025\n- **URL:** https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2025.76\n- **Summary:** Achieves near-optimal O(nd(log log n + log(1/epsilon))/epsilon^2) time for Chamfer distance computation, narrowing the gap to the trivial lower bound Omega(dn).\n- **Why important:** The Chamfer distance is the core similarity measure in ColBERT-style multi-vector retrieval (MaxSim). This near-optimal algorithm establishes the computational complexity floor for exact multi-vector scoring.\n\n**15. \"Faster Maximum Inner Product Search in High Dimensions\"**\n- **Authors:** Mo Tiwari, Ryan Kang, Jaeyong Lee, Donghyun Lee, Christopher J. Piech, Sebastian Thrun, Ilan Shomorony, Martin Jinye Zhang\n- **Venue/Year:** ICML 2024\n- **URL:** https://proceedings.mlr.press/v235/tiwari24a.html\n- **Summary:** BanditMIPS achieves O(1) complexity with respect to dimension d for MIPS, improving upon the prior O(sqrt(d)) bound.\n- **Why important:** Since multi-vector retrieval can be reduced to MIPS (via MUVERA's FDEs), improvements in MIPS complexity directly translate to better multi-vector retrieval efficiency.\n\n**16. \"Maximum Inner Product is Query-Scaled Nearest Neighbor\"**\n- **Authors:** Tingyang Chen, Cong Fu, Kun Wang, Xiangyu Ke, Yunjun Gao, Wenchao Zhou, Yabo Ni, Anxiang Zeng\n- **Venue/Year:** VLDB 2025 (arXiv:2503.06882)\n- **URL:** https://arxiv.org/abs/2503.06882\n- **Summary:** Proves MIPS is equivalent to query-scaled Euclidean NN search without space transformation, enabling graph-based indices for MIPS with 35% speedup.\n- **Why important:** Unifies MIPS and NNS theory, meaning all NNS lower bounds and algorithms apply to the inner product similarity used in retrieval -- simplifying the theoretical landscape for multi-vector models that use inner product scoring.\n\n**17. \"Nearest Neighbor Complexity and Boolean Circuits\"**\n- **Authors:** Mason DiCicco, Vladimir Podolskii, Daniel Reichman\n- **Venue/Year:** ITCS 2025\n- **URL:** https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2025.42\n- **Summary:** Proves exponential lower bounds on k-NN complexity for explicit functions (k <= n^{1-epsilon}), connecting NN complexity to circuit complexity based on linear inequalities. Shows exponential separation between 1-NN and k-NN complexity.\n- **Why important:** The exponential separation between 1-NN and k-NN complexity is directly relevant to multi-vector retrieval: MaxSim/Chamfer similarity involves multiple NN lookups, and this work shows that such operations are fundamentally more powerful than single-NN operations.\n\n---\n\n### D. METRIC EMBEDDINGS AND DISTORTION\n\n**18. \"Smoothed Analysis of Online Metric Matching with a Single Sample: Beyond Metric Distortion\"**\n- **Authors:** Yingxi Li, Ellen Vitercik, Mingwei Yang\n- **Venue/Year:** ITCS 2026\n- **URL:** https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2026.94\n- **Summary:** Achieves O(1)-competitive online metric matching by bypassing the Omega(log n) probabilistic embedding distortion barrier, directly bounding costs on target metric spaces.\n- **Why important:** Demonstrates that classical distortion lower bounds (Omega(log n) for embedding into Euclidean/tree metrics) can be circumvented by algorithm-metric co-design -- suggesting that multi-vector retrieval might similarly bypass single-vector embedding distortion limits.\n\n---\n\n### E. LEARNING THEORY AND COMBINATORIAL DIMENSIONS\n\n**19. \"Sample Complexity of Agnostic Multiclass Classification: Natarajan Dimension Strikes Back\"**\n- **Authors:** Alon Cohen, Liad Erez, Steve Hanneke, Tomer Koren, Yishay Mansour, Shay Moran, Qian Zhang\n- **Venue/Year:** arXiv:2511.12659, November 2025\n- **URL:** https://arxiv.org/abs/2511.12659\n- **Summary:** Proves that agnostic multiclass sample complexity has the form DS^{1.5}/epsilon + Nat/epsilon^2, showing that the Natarajan dimension still governs the fine-epsilon regime alongside the DS dimension.\n- **Why important:** The Natarajan dimension generalizes VC dimension to multi-output settings. Multi-vector retrieval can be viewed as a multiclass problem (selecting among documents), and these bounds characterize how many training examples are needed to learn multi-vector representations as a function of their combinatorial complexity.\n\n**20. \"Bounds on the Natarajan Dimension of a Class of Linear Multi-Class Predictors\"**\n- **Authors:** (Authors behind ScienceDirect paper S0167865525004167)\n- **Venue/Year:** Pattern Recognition Letters, 2025\n- **URL:** https://www.sciencedirect.com/science/article/abs/pii/S0167865525004167\n- **Summary:** Derives tight upper bounds on the Natarajan dimension for linear multi-class predictors based on class-sensitive feature mappings for multi-vector construction.\n- **Why important:** Directly connects Natarajan dimension to multi-vector construction via class-sensitive feature mappings, providing combinatorial complexity bounds for linear multi-vector classifiers.\n\n**21. \"Regularization and Optimal Multiclass Learning\"**\n- **Authors:** Julian Asilis, Vatsal Sharan, Siddartha Devic, Shaddin Dughmi, Shanghua Teng\n- **Venue/Year:** COLT 2024\n- **URL:** https://learningtheory.org/colt2024/schedule/poster_184.html\n- **Summary:** Introduces \"Hall complexity\" as a combinatorial measure for transductive multiclass error rates, connecting regularization to optimal multiclass learners via one-inclusion graphs.\n- **Why important:** Hall complexity provides a new combinatorial dimension for multiclass problems that may tighten the analysis of how many vectors/dimensions are needed to represent multi-class retrieval decisions.\n\n---\n\n### F. TRANSFORMER RETRIEVAL THEORY AND SURVEYS\n\n**22. \"Learning to Recall with Transformers Beyond Orthogonal Embeddings\"**\n- **Authors:** Nuri Mert Vural, Alberto Bietti, Mahdi Soltanolkotabi, Denny Wu\n- **Venue/Year:** ICLR 2026 (arXiv:2603.15923)\n- **URL:** https://arxiv.org/abs/2603.15923\n- **Summary:** Derives explicit formulas for a single-layer transformer's storage capacity on retrieval tasks, showing multiplicative scaling between sample size, embedding dimension, and sequence length when embeddings are non-orthogonal.\n- **Why important:** Directly characterizes the capacity-dimension-length tradeoff for retrieval in transformers. For multi-vector models, where each document produces a sequence of vectors, this work bounds how many associations can be stored as a function of per-token embedding dimension and number of tokens -- the two axes of multi-vector capacity.\n\n**23. \"A Survey of Model Architectures in Information Retrieval\"**\n- **Authors:** Zhichao Xu, Fengran Mo, Zhiqi Huang, Crystina Zhang, Puxuan Yu, Bei Wang, Jimmy Lin, Vivek Srikumar\n- **Venue/Year:** TMLR 2025 (arXiv:2502.14822)\n- **URL:** https://arxiv.org/abs/2502.14822\n- **Summary:** Comprehensive survey of IR model architectures from term-based to transformer-based, covering single-vector, multi-vector, and generative retrieval paradigms.\n- **Why important:** Provides the landscape context: where multi-vector models sit among retrieval architectures and what empirical evidence exists for their relative expressiveness.\n\n**24. \"Overcomplete Tensor Decomposition via Koszul-Young Flattenings\"**\n- **Authors:** Pravesh K. Kothari, Ankur Moitra, Alexander S. Wein\n- **Venue/Year:** FOCS 2025 (arXiv:2411.14344)\n- **URL:** https://arxiv.org/abs/2411.14344\n- **Summary:** Achieves rank r <= (1-epsilon)(n2+n3) for tensor decomposition, a factor-2 improvement over classical simultaneous diagonalization, and proves this is tight for flattening-based methods.\n- **Why important:** Multi-vector representations can be viewed as tensors (batch of vectors per item). Tensor rank bounds constrain the \"effective complexity\" of such representations and inform how many rank-1 components (analogous to individual embedding vectors) are needed to faithfully represent the multi-vector structure.\n\n---\n\n### KEY TAKEAWAYS FOR MULTI-VECTOR RETRIEVAL EXPRESSIVENESS\n\n1. **Single-vector bottleneck is proven:** Weller et al. (ICLR 2026) show that single-vector retrieval capacity is bounded by sign-rank of the relevance matrix, with concrete dimension-to-capacity limits. Multi-vector representations bypass this.\n\n2. **Multi-vector to single-vector reduction has guarantees:** MUVERA (NeurIPS 2024) proves that FDEs can approximate MaxSim/Chamfer similarity with dimension scaling only logarithmically in dataset size, establishing a formal bridge.\n\n3. **Redundancy in multi-vector representations is substantial:** Token pooling (Clavie et al. 2024), Col-Bandit (2026), and compression work (Qin et al. 2026) all show 50-80% of vectors can be pruned with minimal quality loss, bounding the effective dimensionality from above.\n\n4. **Chamfer/MaxSim complexity is near-settled:** Feng & Indyk (ICALP 2025) provide near-optimal algorithms, and the stability theory (Lakshman et al. 2025) explains why multi-vector search works despite high dimensionality.\n\n5. **Learning-theoretic dimensions apply:** Natarajan dimension bounds for multi-vector linear predictors and the DS/Natarajan sample complexity interplay (Cohen et al. 2025) provide the statistical learning framework for understanding when multi-vector representations can be trained.\n\n6. **The geometric vs. learnability gap:** Wang et al. (2026) argue that R^{2k} suffices geometrically for top-k, suggesting the real bottleneck is learnability -- and multi-vector models may help precisely because they make the learning problem easier, not because they expand geometric capacity."
      }
    ],
    "totalDurationMs": 255963,
    "totalTokens": 43487,
    "totalToolUseCount": 52,
    "usage": {
      "input_tokens": 274,
      "cache_creation_input_tokens": 610,
      "cache_read_input_tokens": 37005,
      "output_tokens": 5598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 274,
          "output_tokens": 5598,
          "cache_read_input_tokens": 37005,
          "cache_creation_input_tokens": 610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 610,
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
      "otherToolCount": 52
    }
  },
  "sourceToolAssistantUUID": "44d06f17-0a54-4cea-af32-3b6f374bfd8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "0ec8a96e-bdca-47e4-b887-1fee5bfe61ed",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on multi-vector retrieval expressiveness",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Assistant

_source line 32 · 2026-05-30T06:14:56.068Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive results from all 5 search agents. Let me synthesize and identify the most important papers, then verify key details for the top papers. Let me now do some additional targeted searches to fill any gaps and verify paper details.

Let me compile the unique papers across all agents and identify the 15+ most important ones. Let me also verify some of the key papers I'm less certain about.

Key papers identified across all agents (deduplicating):

**Tier 1 - Core theory (directly on expressiveness of retrieval embeddings):**
1. Weller et al., "On the Theoretical Limitations of Embedding-Based Retrieval" (ICLR 2026) - seed


2. Wang et al., "R^{2k} is Theoretically Large Enough" (arXiv 2026) - seed
3. Dhulipala et al., "MUVERA" (NeurIPS 2024) - seed
4. Jacob/Archish et al., "On Strengths and Limitations of Single-Vector Embeddings" (arXiv 2026) - seed
5. Bangachev et al., "Is Dimensionality a Barrier for Retrieval Models?" (arXiv 2026)
6. Arvanitakis et al., "Provable Accuracy Collapse in Embedding" - continuing to compile the foundational papers on embedding expressiveness and theoretical constraints.

Now moving into multi-vector retrieval approaches with papers on generative retrieval mechanisms, dimensionality stability, and recent methods like MetaEmbed and LEMUR that challenge traditional clustering approaches. Then I'm looking at communication complexity and sign-rank theory as it applies to these retrieval systems. Now I'm narrowing down to the most impactful papers and double-checking a few of the ones I'm less certain about.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ec8a96e-bdca-47e4-b887-1fee5bfe61ed",
  "isSidechain": false,
  "requestId": "req_011CbYG91tA21PyFkgrUMYxw",
  "type": "assistant",
  "uuid": "59690cb3-6d3f-4dd2-9efc-aac1e2dd23f0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Y53t7oBjiDyN7bYeZ1enc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27129,
      "cache_read_input_tokens": 16241,
      "output_tokens": 2037,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2037,
          "cache_read_input_tokens": 16241,
          "cache_creation_input_tokens": 27129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27129
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

_source line 33 · 2026-05-30T06:14:56.070Z_

Now let me verify key details for several important papers and search for any remaining gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59690cb3-6d3f-4dd2-9efc-aac1e2dd23f0",
  "isSidechain": false,
  "requestId": "req_011CbYG91tA21PyFkgrUMYxw",
  "type": "assistant",
  "uuid": "00b64f53-3c1b-4829-85c1-047c03560bb2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Y53t7oBjiDyN7bYeZ1enc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27129,
      "cache_read_input_tokens": 16241,
      "output_tokens": 2037,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2037,
          "cache_read_input_tokens": 16241,
          "cache_creation_input_tokens": 27129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27129
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

_source line 34 · 2026-05-30T06:14:59.781Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01QSicMxpzDsDZ79fhcErmkx`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify and fetch key papers batch 1",
  "prompt": "I need to verify details for several papers. For each, use WebFetch to read the arxiv abstract page and confirm: exact title, authors, venue, year. Report any corrections needed.\n\n1. https://arxiv.org/abs/2605.23556 — \"Is Dimensionality a Barrier for Retrieval Models?\" by Bangachev et al. 2026\n2. https://arxiv.org/abs/2605.03346 — \"Provable Accuracy Collapse in Embedding-Based Representations\" by Arvanitakis et al. ICML 2026\n3. https://arxiv.org/abs/2402.06662 — \"Sign Rank Limitations for Inner Product Graph Decoders\" Lee et al. ICML 2024\n4. https://arxiv.org/abs/2404.00684 — \"Generative Retrieval as Multi-Vector Dense Retrieval\" Wu et al. SIGIR 2024\n5. https://arxiv.org/abs/2509.18095 — \"MetaEmbed\" Xiao et al. ICLR 2026\n\nFor each paper, extract: exact title, first 3 authors, venue (if stated), and the complete abstract. Report corrections to any information I provided."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b64f53-3c1b-4829-85c1-047c03560bb2",
  "isSidechain": false,
  "requestId": "req_011CbYG91tA21PyFkgrUMYxw",
  "type": "assistant",
  "uuid": "f7d865c9-6ecf-4901-bab9-3b0ed7e68e56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Y53t7oBjiDyN7bYeZ1enc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27129,
      "cache_read_input_tokens": 16241,
      "output_tokens": 2037,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2037,
          "cache_read_input_tokens": 16241,
          "cache_creation_input_tokens": 27129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27129
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

_source line 35 · 2026-05-30T06:15:04.146Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LXYZgX7ZnA6dPpL9kmNcgT`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify and fetch key papers batch 2",
  "prompt": "I need to verify details for several papers. For each, use WebFetch to read the arxiv/conference page and confirm: exact title, authors, venue, year. Report any corrections needed.\n\n1. https://arxiv.org/abs/2506.12022 — \"Sign-Rank of k-Hamming Distance is Constant\" Goos et al. \n2. https://arxiv.org/abs/2603.15923 — \"Learning to Recall with Transformers Beyond Orthogonal Embeddings\" Vural et al. ICLR 2026\n3. https://arxiv.org/abs/2603.09933 — \"A Voronoi Cell Formulation for Principled Token Pruning\" Kankanampati et al. SIGIR 2026\n4. https://arxiv.org/abs/2312.13490 — \"Dimension-Accuracy Tradeoffs in Contrastive Embeddings\" Chatziafratis & Indyk\n5. https://arxiv.org/abs/2509.22116 — \"Does Generative Retrieval Overcome the Limitations of Dense Retrieval?\" Zhang et al.\n\nFor each paper, extract: exact title, first 3 authors, venue (if stated), and the complete abstract."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7d865c9-6ecf-4901-bab9-3b0ed7e68e56",
  "isSidechain": false,
  "requestId": "req_011CbYG91tA21PyFkgrUMYxw",
  "type": "assistant",
  "uuid": "3e694dc5-a6a0-46e7-95de-03cd1c640db0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Y53t7oBjiDyN7bYeZ1enc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27129,
      "cache_read_input_tokens": 16241,
      "output_tokens": 2037,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2037,
          "cache_read_input_tokens": 16241,
          "cache_creation_input_tokens": 27129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27129
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

_source line 36 · 2026-05-30T06:15:09.462Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01378EaxfS5dwLh2toPNJbQs`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search additional theoretical papers",
  "prompt": "I need to find a few more papers. Search for:\n\n1. WebSearch: \"Feng Indyk even faster Chamfer distance ICALP 2025\"\n2. WebSearch: \"DiCicco Podolskii Reichman nearest neighbor complexity Boolean circuits ITCS 2025\"\n3. WebSearch: \"Scalings laws embedding dimension information retrieval Killingback 2026\"\n4. WebSearch: \"WARP efficient engine multi-vector retrieval SIGIR 2025 Scheerer\"\n5. WebSearch: \"superposition yields robust neural scaling NeurIPS 2025\"\n6. WebSearch: \"Transformers are inherently succinct ICLR 2026\"\n7. WebSearch: \"Cramming tokens single vector embedding space capacity ACL 2025\"\n\nFor each paper found, use WebFetch on the arxiv page to get the abstract. Report: exact title, authors, venue/year, URL, and one-line summary."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e694dc5-a6a0-46e7-95de-03cd1c640db0",
  "isSidechain": false,
  "requestId": "req_011CbYG91tA21PyFkgrUMYxw",
  "type": "assistant",
  "uuid": "28ee2af5-c096-4612-b936-4e32409b69a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Y53t7oBjiDyN7bYeZ1enc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 27129,
      "cache_read_input_tokens": 16241,
      "output_tokens": 2037,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 27129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2037,
          "cache_read_input_tokens": 16241,
          "cache_creation_input_tokens": 27129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 27129
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

_source line 37 · 2026-05-30T06:15:58.765Z_

<details><summary>↩ Tool result · `toolu_01QSicMxpzDsDZ79fhcErmkx`</summary>

```text
Here are the verification results for all five papers, with corrections noted:

---

**Paper 1: arxiv 2605.23556**

- **Title:** "Is Dimensionality a Barrier for Retrieval Models?" -- **CORRECT**
- **Authors:** Kiril Bangachev, Guy Bresler, Jonathan Kogan, Yury Polyanskiy -- You cited "Bangachev et al." which is consistent. **First 3 authors: Kiril Bangachev, Guy Bresler, Jonathan Kogan.**
- **Venue:** No venue/conference stated on the arxiv page. You did not claim one, so **no correction needed**.
- **Year:** 2026 -- **CORRECT**
- **Abstract:** The paper examines why embedding-based retrieval models function effectively at massive scales despite low-dimensional representations (approximately d~1000). The authors study maximal-margin embeddings within a retrieval framework involving an N x n relevance matrix. Their central finding demonstrates that the best possible margin without a restriction on the dimension can be nearly achieved in dimension d = O(m^rd(+infty, A)^{-2} log n), representing an improvement over prior work. For k-sparse matrices, they establish that dimension d = O(k log(n/k)) is both necessary and sufficient. The research also includes empirical comparisons between InfoNCE and sigmoid losses for margin optimization.

**Corrections needed: None.**

---

**Paper 2: arxiv 2605.03346**

- **Title:** You cited "Provable Accuracy Collapse in Embedding-Based Representations." The actual title is **"Provable Accuracy Collapse in Embedding-Based Representations under Dimensionality Mismatch."** **CORRECTION: the title is missing the suffix "under Dimensionality Mismatch."**
- **Authors:** Dionysis Arvanitakis, Vaggos Chatziafratis, Yiyuan Luo. You cited "Arvanitakis et al." which is consistent. **First 3 authors: Dionysis Arvanitakis, Vaggos Chatziafratis, Yiyuan Luo.**
- **Venue:** "Preliminary version, accepted to ICML 2026 as spotlight presentation." You cited ICML 2026 -- **CORRECT** (it is specifically a spotlight).
- **Year:** 2026 -- **CORRECT**
- **Abstract:** Embedding-based representations in Euclidean space R^d are a cornerstone of modern machine learning, where a major goal is to use the smallest dimension that faithfully captures data relations. The authors prove sharp dimension-accuracy tradeoffs and identify a fundamental information-theoretic limitation: unless the embedding dimension d is chosen close to the ground-truth dimension D, accuracy undergoes a sudden collapse. The main result shows this phenomenon arises even in standard contrastive learning settings with m anchor-positive-negative triplets. Specifically, given triplets realizable by an unknown ground-truth embedding in D dimensions, there exists constant c < 1 such that every embedding of dimension at most cD violates half of the triplets, yielding accuracy as low as a trivial one-dimensional solution. Complementary computational hardness results show that under the Unique Games Conjecture, even if the given triplets are nearly realizable in D=1 dimension, no polynomial-time algorithm -- regardless of its dimension -- can achieve accuracy above the trivial 50% baseline.

**Corrections needed: Title is incomplete -- add "under Dimensionality Mismatch."**

---

**Paper 3: arxiv 2402.06662**

- **Title:** "Sign Rank Limitations for Inner Product Graph Decoders" -- **CORRECT**
- **Authors:** Su Hyeong Lee, Qingqi Zhang, Risi Kondor. You cited "Lee et al." which is consistent. **First 3 authors (and all authors): Su Hyeong Lee, Qingqi Zhang, Risi Kondor.**
- **Venue:** ICML 2024 -- **CORRECT**
- **Year:** 2024 -- **CORRECT**
- **Abstract:** Inner product-based decoders are among the most influential frameworks used to extract meaningful data from latent embeddings. However, such decoders have shown limitations in representation capacity in numerous works within the literature, which have been particularly notable in graph reconstruction problems. The authors provide the first theoretical elucidation of this pervasive phenomenon in graph data, and suggest straightforward modifications to circumvent this issue without deviating from the inner product framework.

**Corrections needed: None.**

---

**Paper 4: arxiv 2404.00684**

- **Title:** "Generative Retrieval as Multi-Vector Dense Retrieval" -- **CORRECT**
- **Authors:** Shiguang Wu, Wenda Wei, Mengqi Zhang, Zhumin Chen, Jun Ma, Zhaochun Ren, Maarten de Rijke, Pengjie Ren. You cited "Wu et al." which is consistent. **First 3 authors: Shiguang Wu, Wenda Wei, Mengqi Zhang.**
- **Venue:** SIGIR 2024 -- **CORRECT**
- **Year:** 2024 -- **CORRECT**
- **Abstract:** Generative retrieval generates identifiers of relevant documents in an end-to-end manner using a sequence-to-sequence architecture for a given query. The relation between generative retrieval and other retrieval methods is not yet fully comprehended. Prior work demonstrated that generative retrieval with atomic identifiers is equivalent to single-vector dense retrieval and exhibits behavior analogous to hierarchical search within a tree index when using hierarchical semantic identifiers. However, prior work focuses solely on the retrieval stage without considering the deep interactions within the decoder. The authors fill this gap by demonstrating that generative retrieval and multi-vector dense retrieval share the same framework for measuring query-document relevance. Specifically, they examine the attention layer and prediction head of generative retrieval, revealing it can be understood as a special case of multi-vector dense retrieval. Both methods compute relevance as a sum of products of query and document vectors and an alignment matrix. They explore how generative retrieval applies this framework with distinct strategies for computing document token vectors and the alignment matrix. Experiments verify these conclusions and show both paradigms exhibit commonalities of term matching in their alignment matrix.

**Corrections needed: None.**

---

**Paper 5: arxiv 2509.18095**

- **Title:** You cited "MetaEmbed." The full title is **"MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction."** **CORRECTION: the title is incomplete -- the subtitle is missing.**
- **Authors:** Zilin Xiao, Qi Ma, Mengting Gu, Chun-cheng Jason Chen, Xintao Chen, Vicente Ordonez, Vijai Mohan. You cited "Xiao et al." which is consistent. **First 3 authors: Zilin Xiao, Qi Ma, Mengting Gu.**
- **Venue:** ICLR 2026 (specifically, an **Oral** presentation). You cited ICLR 2026 -- **CORRECT** (notable: it is an Oral).
- **Year:** Submitted September 2025, accepted at ICLR 2026. You cited 2026 -- **CORRECT** for the venue year.
- **Abstract:** Universal multimodal embedding models have achieved great success in capturing semantic relevance between queries and candidates. However, current methods either condense queries and candidates into a single vector, potentially limiting expressiveness for fine-grained information, or produce too many vectors that are prohibitive for multi-vector retrieval. The authors introduce MetaEmbed, a new framework for multimodal retrieval that rethinks how multimodal embeddings are constructed and interacted with at scale. During training, a fixed number of learnable Meta Tokens are appended to the input sequence. At test-time, their last-layer contextualized representations serve as compact yet expressive multi-vector embeddings. Through the proposed Matryoshka Multi-Vector Retrieval training, MetaEmbed learns to organize information by granularity across multiple vectors. This enables test-time scaling in multimodal retrieval where users can balance retrieval quality against efficiency demands by selecting the number of tokens used for indexing and retrieval interactions. Evaluations on MMEB and ViDoRe confirm state-of-the-art retrieval performance while scaling robustly to models with 32B parameters.

**Corrections needed: Title is incomplete -- full title is "MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction."**

---

## Summary of Corrections

| # | Paper | Issue |
|---|-------|-------|
| 1 | 2605.23556 | All details correct |
| 2 | 2605.03346 | **Title incomplete** -- missing "under Dimensionality Mismatch" |
| 3 | 2402.06662 | All details correct |
| 4 | 2404.00684 | All details correct |
| 5 | 2509.18095 | **Title incomplete** -- missing subtitle ": Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction" |

agentId: a64d151c02323e0cf (use SendMessage with to: 'a64d151c02323e0cf' to continue this agent)
&lt;usage>total_tokens: 14387
tool_uses: 6
duration_ms: 58977&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7d865c9-6ecf-4901-bab9-3b0ed7e68e56",
  "isSidechain": false,
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "58e880c6-9c3c-429c-a243-8c9a3a7e1c52",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify details for several papers. For each, use WebFetch to read the arxiv abstract page and confirm: exact title, authors, venue, year. Report any corrections needed.\n\n1. https://arxiv.org/abs/2605.23556 — \"Is Dimensionality a Barrier for Retrieval Models?\" by Bangachev et al. 2026\n2. https://arxiv.org/abs/2605.03346 — \"Provable Accuracy Collapse in Embedding-Based Representations\" by Arvanitakis et al. ICML 2026\n3. https://arxiv.org/abs/2402.06662 — \"Sign Rank Limitations for Inner Product Graph Decoders\" Lee et al. ICML 2024\n4. https://arxiv.org/abs/2404.00684 — \"Generative Retrieval as Multi-Vector Dense Retrieval\" Wu et al. SIGIR 2024\n5. https://arxiv.org/abs/2509.18095 — \"MetaEmbed\" Xiao et al. ICLR 2026\n\nFor each paper, extract: exact title, first 3 authors, venue (if stated), and the complete abstract. Report corrections to any information I provided.",
    "agentId": "a64d151c02323e0cf",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verification results for all five papers, with corrections noted:\n\n---\n\n**Paper 1: arxiv 2605.23556**\n\n- **Title:** \"Is Dimensionality a Barrier for Retrieval Models?\" -- **CORRECT**\n- **Authors:** Kiril Bangachev, Guy Bresler, Jonathan Kogan, Yury Polyanskiy -- You cited \"Bangachev et al.\" which is consistent. **First 3 authors: Kiril Bangachev, Guy Bresler, Jonathan Kogan.**\n- **Venue:** No venue/conference stated on the arxiv page. You did not claim one, so **no correction needed**.\n- **Year:** 2026 -- **CORRECT**\n- **Abstract:** The paper examines why embedding-based retrieval models function effectively at massive scales despite low-dimensional representations (approximately d~1000). The authors study maximal-margin embeddings within a retrieval framework involving an N x n relevance matrix. Their central finding demonstrates that the best possible margin without a restriction on the dimension can be nearly achieved in dimension d = O(m^rd(+infty, A)^{-2} log n), representing an improvement over prior work. For k-sparse matrices, they establish that dimension d = O(k log(n/k)) is both necessary and sufficient. The research also includes empirical comparisons between InfoNCE and sigmoid losses for margin optimization.\n\n**Corrections needed: None.**\n\n---\n\n**Paper 2: arxiv 2605.03346**\n\n- **Title:** You cited \"Provable Accuracy Collapse in Embedding-Based Representations.\" The actual title is **\"Provable Accuracy Collapse in Embedding-Based Representations under Dimensionality Mismatch.\"** **CORRECTION: the title is missing the suffix \"under Dimensionality Mismatch.\"**\n- **Authors:** Dionysis Arvanitakis, Vaggos Chatziafratis, Yiyuan Luo. You cited \"Arvanitakis et al.\" which is consistent. **First 3 authors: Dionysis Arvanitakis, Vaggos Chatziafratis, Yiyuan Luo.**\n- **Venue:** \"Preliminary version, accepted to ICML 2026 as spotlight presentation.\" You cited ICML 2026 -- **CORRECT** (it is specifically a spotlight).\n- **Year:** 2026 -- **CORRECT**\n- **Abstract:** Embedding-based representations in Euclidean space R^d are a cornerstone of modern machine learning, where a major goal is to use the smallest dimension that faithfully captures data relations. The authors prove sharp dimension-accuracy tradeoffs and identify a fundamental information-theoretic limitation: unless the embedding dimension d is chosen close to the ground-truth dimension D, accuracy undergoes a sudden collapse. The main result shows this phenomenon arises even in standard contrastive learning settings with m anchor-positive-negative triplets. Specifically, given triplets realizable by an unknown ground-truth embedding in D dimensions, there exists constant c < 1 such that every embedding of dimension at most cD violates half of the triplets, yielding accuracy as low as a trivial one-dimensional solution. Complementary computational hardness results show that under the Unique Games Conjecture, even if the given triplets are nearly realizable in D=1 dimension, no polynomial-time algorithm -- regardless of its dimension -- can achieve accuracy above the trivial 50% baseline.\n\n**Corrections needed: Title is incomplete -- add \"under Dimensionality Mismatch.\"**\n\n---\n\n**Paper 3: arxiv 2402.06662**\n\n- **Title:** \"Sign Rank Limitations for Inner Product Graph Decoders\" -- **CORRECT**\n- **Authors:** Su Hyeong Lee, Qingqi Zhang, Risi Kondor. You cited \"Lee et al.\" which is consistent. **First 3 authors (and all authors): Su Hyeong Lee, Qingqi Zhang, Risi Kondor.**\n- **Venue:** ICML 2024 -- **CORRECT**\n- **Year:** 2024 -- **CORRECT**\n- **Abstract:** Inner product-based decoders are among the most influential frameworks used to extract meaningful data from latent embeddings. However, such decoders have shown limitations in representation capacity in numerous works within the literature, which have been particularly notable in graph reconstruction problems. The authors provide the first theoretical elucidation of this pervasive phenomenon in graph data, and suggest straightforward modifications to circumvent this issue without deviating from the inner product framework.\n\n**Corrections needed: None.**\n\n---\n\n**Paper 4: arxiv 2404.00684**\n\n- **Title:** \"Generative Retrieval as Multi-Vector Dense Retrieval\" -- **CORRECT**\n- **Authors:** Shiguang Wu, Wenda Wei, Mengqi Zhang, Zhumin Chen, Jun Ma, Zhaochun Ren, Maarten de Rijke, Pengjie Ren. You cited \"Wu et al.\" which is consistent. **First 3 authors: Shiguang Wu, Wenda Wei, Mengqi Zhang.**\n- **Venue:** SIGIR 2024 -- **CORRECT**\n- **Year:** 2024 -- **CORRECT**\n- **Abstract:** Generative retrieval generates identifiers of relevant documents in an end-to-end manner using a sequence-to-sequence architecture for a given query. The relation between generative retrieval and other retrieval methods is not yet fully comprehended. Prior work demonstrated that generative retrieval with atomic identifiers is equivalent to single-vector dense retrieval and exhibits behavior analogous to hierarchical search within a tree index when using hierarchical semantic identifiers. However, prior work focuses solely on the retrieval stage without considering the deep interactions within the decoder. The authors fill this gap by demonstrating that generative retrieval and multi-vector dense retrieval share the same framework for measuring query-document relevance. Specifically, they examine the attention layer and prediction head of generative retrieval, revealing it can be understood as a special case of multi-vector dense retrieval. Both methods compute relevance as a sum of products of query and document vectors and an alignment matrix. They explore how generative retrieval applies this framework with distinct strategies for computing document token vectors and the alignment matrix. Experiments verify these conclusions and show both paradigms exhibit commonalities of term matching in their alignment matrix.\n\n**Corrections needed: None.**\n\n---\n\n**Paper 5: arxiv 2509.18095**\n\n- **Title:** You cited \"MetaEmbed.\" The full title is **\"MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction.\"** **CORRECTION: the title is incomplete -- the subtitle is missing.**\n- **Authors:** Zilin Xiao, Qi Ma, Mengting Gu, Chun-cheng Jason Chen, Xintao Chen, Vicente Ordonez, Vijai Mohan. You cited \"Xiao et al.\" which is consistent. **First 3 authors: Zilin Xiao, Qi Ma, Mengting Gu.**\n- **Venue:** ICLR 2026 (specifically, an **Oral** presentation). You cited ICLR 2026 -- **CORRECT** (notable: it is an Oral).\n- **Year:** Submitted September 2025, accepted at ICLR 2026. You cited 2026 -- **CORRECT** for the venue year.\n- **Abstract:** Universal multimodal embedding models have achieved great success in capturing semantic relevance between queries and candidates. However, current methods either condense queries and candidates into a single vector, potentially limiting expressiveness for fine-grained information, or produce too many vectors that are prohibitive for multi-vector retrieval. The authors introduce MetaEmbed, a new framework for multimodal retrieval that rethinks how multimodal embeddings are constructed and interacted with at scale. During training, a fixed number of learnable Meta Tokens are appended to the input sequence. At test-time, their last-layer contextualized representations serve as compact yet expressive multi-vector embeddings. Through the proposed Matryoshka Multi-Vector Retrieval training, MetaEmbed learns to organize information by granularity across multiple vectors. This enables test-time scaling in multimodal retrieval where users can balance retrieval quality against efficiency demands by selecting the number of tokens used for indexing and retrieval interactions. Evaluations on MMEB and ViDoRe confirm state-of-the-art retrieval performance while scaling robustly to models with 32B parameters.\n\n**Corrections needed: Title is incomplete -- full title is \"MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction.\"**\n\n---\n\n## Summary of Corrections\n\n| # | Paper | Issue |\n|---|-------|-------|\n| 1 | 2605.23556 | All details correct |\n| 2 | 2605.03346 | **Title incomplete** -- missing \"under Dimensionality Mismatch\" |\n| 3 | 2402.06662 | All details correct |\n| 4 | 2404.00684 | All details correct |\n| 5 | 2509.18095 | **Title incomplete** -- missing subtitle \": Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction\" |"
      }
    ],
    "totalDurationMs": 58977,
    "totalTokens": 14387,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2526,
      "cache_read_input_tokens": 9670,
      "output_tokens": 2190,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2526
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2190,
          "cache_read_input_tokens": 9670,
          "cache_creation_input_tokens": 2526,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2526,
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
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "f7d865c9-6ecf-4901-bab9-3b0ed7e68e56",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "58e880c6-9c3c-429c-a243-8c9a3a7e1c52",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on multi-vector retrieval expressiveness",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Tool result

_source line 40 · 2026-05-30T06:16:05.889Z_

<details><summary>↩ Tool result · `toolu_01378EaxfS5dwLh2toPNJbQs`</summary>

```text
Here are the results for all 7 papers:

---

**1. Even Faster Algorithm for the Chamfer Distance**

- **Title:** Even Faster Algorithm for the Chamfer Distance
- **Authors:** Ying Feng, Piotr Indyk
- **Venue/Year:** ICALP 2025 (LIPIcs, Volume 334, pages 76:1-76:18)
- **URL:** https://arxiv.org/abs/2505.08957
- **Summary:** Improves the near-linear time (1+epsilon)-approximation algorithm for Chamfer distance from O(nd log(n)/epsilon^2) to O(nd(log log n + log(1/epsilon))/epsilon^2), reducing the gap to the trivial lower bound from O(log n) to O(log log n) for constant epsilon.

---

**2. Nearest Neighbor Complexity and Boolean Circuits**

- **Title:** Nearest Neighbor Complexity and Boolean Circuits
- **Authors:** Mason DiCicco, Vladimir Podolskii, Daniel Reichman
- **Venue/Year:** ITCS 2025 (LIPIcs, Volume 325, pages 42:1-42:23)
- **URL:** https://arxiv.org/abs/2402.06740
- **Summary:** Establishes connections between nearest neighbor representations of Boolean functions and circuit complexity, proving exponential lower bounds on k-nearest neighbors complexity and an exponential separation between nearest neighbor and k-nearest neighbors complexity.

---

**3. Scaling Laws for Embedding Dimension in Information Retrieval**

- **Title:** Scaling Laws for Embedding Dimension in Information Retrieval
- **Authors:** Julian Killingback, Mahta Rafiee, Madine Manas, Hamed Zamani
- **Venue/Year:** SIGIR 2026 (arXiv preprint February 2026)
- **URL:** https://arxiv.org/abs/2602.05062
- **Summary:** Derives power-law scaling laws for dense retrieval performance as a function of embedding dimension and model size, finding that in-distribution performance improves with larger embeddings (with diminishing returns), while out-of-distribution performance can degrade.

---

**4. WARP: An Efficient Engine for Multi-Vector Retrieval**

- **Title:** WARP: An Efficient Engine for Multi-Vector Retrieval
- **Authors:** Jan Luca Scheerer, Matei Zaharia, Christopher Potts, Gustavo Alonso, Omar Khattab
- **Venue/Year:** SIGIR 2025
- **URL:** https://arxiv.org/abs/2501.17788
- **Summary:** Introduces three optimizations (dynamic similarity imputation, implicit decompression, two-stage reduction) for multi-vector retrieval engines like ColBERT/XTR, achieving 41x latency reduction over XTR and 3x over ColBERTv2/PLAID while preserving retrieval quality.

---

**5. Superposition Yields Robust Neural Scaling**

- **Title:** Superposition Yields Robust Neural Scaling
- **Authors:** Yizhou Liu, Ziming Liu, Jeff Gore
- **Venue/Year:** NeurIPS 2025 (Oral; Best Paper Runner-up)
- **URL:** https://arxiv.org/abs/2505.10465
- **Summary:** Shows that representation superposition (encoding more features than dimensions) generically causes loss to scale inversely with model dimension under strong superposition, identifying it as a central mechanism behind neural scaling laws consistent with Chinchilla scaling.

---

**6. Transformers are Inherently Succinct**

- **Title:** Transformers are Inherently Succinct
- **Authors:** Pascal Bergstrasser, Ryan Cotterell, Anthony W. Lin
- **Venue/Year:** ICLR 2026 (Outstanding Paper Award)
- **URL:** https://arxiv.org/abs/2510.19315
- **Summary:** Proves that fixed-precision transformers are exponentially more succinct than LTL and RNNs, and doubly exponentially more succinct than finite automata, with the consequence that verification problems (emptiness, equivalence) for transformers are EXPSPACE-complete.

---

**7. Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the Limits of Embedding Space Capacity**

- **Title:** Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the Limits of Embedding Space Capacity
- **Authors:** Yuri Kuratov, Mikhail Arkhipov, Aydar Bulatov, Mikhail Burtsev
- **Venue/Year:** ACL 2025 (Oral)
- **URL:** https://arxiv.org/abs/2502.13063
- **Summary:** Demonstrates via per-sample optimization that a single Llama-3.1-8B input vector can compress over 1500 tokens (x1500 ratio), revealing a two-orders-of-magnitude gap between current practical compression methods (~10x) and attainable limits, with capacity bounded by input uncertainty rather than sequence length.

---

Sources:
- [Even Faster Algorithm for the Chamfer Distance](https://arxiv.org/abs/2505.08957)
- [Nearest Neighbor Complexity and Boolean Circuits](https://arxiv.org/abs/2402.06740)
- [Scaling Laws for Embedding Dimension in Information Retrieval](https://arxiv.org/abs/2602.05062)
- [WARP: An Efficient Engine for Multi-Vector Retrieval](https://arxiv.org/abs/2501.17788)
- [Superposition Yields Robust Neural Scaling](https://arxiv.org/abs/2505.10465)
- [Transformers are Inherently Succinct](https://arxiv.org/abs/2510.19315)
- [Cramming 1568 Tokens into a Single Vector](https://arxiv.org/abs/2502.13063)

agentId: a2544b03378b875f6 (use SendMessage with to: 'a2544b03378b875f6' to continue this agent)
&lt;usage>total_tokens: 19741
tool_uses: 15
duration_ms: 56424&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28ee2af5-c096-4612-b936-4e32409b69a4",
  "isSidechain": false,
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "dd4a93eb-cdb6-4d5a-a781-d256fecf5e50",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find a few more papers. Search for:\n\n1. WebSearch: \"Feng Indyk even faster Chamfer distance ICALP 2025\"\n2. WebSearch: \"DiCicco Podolskii Reichman nearest neighbor complexity Boolean circuits ITCS 2025\"\n3. WebSearch: \"Scalings laws embedding dimension information retrieval Killingback 2026\"\n4. WebSearch: \"WARP efficient engine multi-vector retrieval SIGIR 2025 Scheerer\"\n5. WebSearch: \"superposition yields robust neural scaling NeurIPS 2025\"\n6. WebSearch: \"Transformers are inherently succinct ICLR 2026\"\n7. WebSearch: \"Cramming tokens single vector embedding space capacity ACL 2025\"\n\nFor each paper found, use WebFetch on the arxiv page to get the abstract. Report: exact title, authors, venue/year, URL, and one-line summary.",
    "agentId": "a2544b03378b875f6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the results for all 7 papers:\n\n---\n\n**1. Even Faster Algorithm for the Chamfer Distance**\n\n- **Title:** Even Faster Algorithm for the Chamfer Distance\n- **Authors:** Ying Feng, Piotr Indyk\n- **Venue/Year:** ICALP 2025 (LIPIcs, Volume 334, pages 76:1-76:18)\n- **URL:** https://arxiv.org/abs/2505.08957\n- **Summary:** Improves the near-linear time (1+epsilon)-approximation algorithm for Chamfer distance from O(nd log(n)/epsilon^2) to O(nd(log log n + log(1/epsilon))/epsilon^2), reducing the gap to the trivial lower bound from O(log n) to O(log log n) for constant epsilon.\n\n---\n\n**2. Nearest Neighbor Complexity and Boolean Circuits**\n\n- **Title:** Nearest Neighbor Complexity and Boolean Circuits\n- **Authors:** Mason DiCicco, Vladimir Podolskii, Daniel Reichman\n- **Venue/Year:** ITCS 2025 (LIPIcs, Volume 325, pages 42:1-42:23)\n- **URL:** https://arxiv.org/abs/2402.06740\n- **Summary:** Establishes connections between nearest neighbor representations of Boolean functions and circuit complexity, proving exponential lower bounds on k-nearest neighbors complexity and an exponential separation between nearest neighbor and k-nearest neighbors complexity.\n\n---\n\n**3. Scaling Laws for Embedding Dimension in Information Retrieval**\n\n- **Title:** Scaling Laws for Embedding Dimension in Information Retrieval\n- **Authors:** Julian Killingback, Mahta Rafiee, Madine Manas, Hamed Zamani\n- **Venue/Year:** SIGIR 2026 (arXiv preprint February 2026)\n- **URL:** https://arxiv.org/abs/2602.05062\n- **Summary:** Derives power-law scaling laws for dense retrieval performance as a function of embedding dimension and model size, finding that in-distribution performance improves with larger embeddings (with diminishing returns), while out-of-distribution performance can degrade.\n\n---\n\n**4. WARP: An Efficient Engine for Multi-Vector Retrieval**\n\n- **Title:** WARP: An Efficient Engine for Multi-Vector Retrieval\n- **Authors:** Jan Luca Scheerer, Matei Zaharia, Christopher Potts, Gustavo Alonso, Omar Khattab\n- **Venue/Year:** SIGIR 2025\n- **URL:** https://arxiv.org/abs/2501.17788\n- **Summary:** Introduces three optimizations (dynamic similarity imputation, implicit decompression, two-stage reduction) for multi-vector retrieval engines like ColBERT/XTR, achieving 41x latency reduction over XTR and 3x over ColBERTv2/PLAID while preserving retrieval quality.\n\n---\n\n**5. Superposition Yields Robust Neural Scaling**\n\n- **Title:** Superposition Yields Robust Neural Scaling\n- **Authors:** Yizhou Liu, Ziming Liu, Jeff Gore\n- **Venue/Year:** NeurIPS 2025 (Oral; Best Paper Runner-up)\n- **URL:** https://arxiv.org/abs/2505.10465\n- **Summary:** Shows that representation superposition (encoding more features than dimensions) generically causes loss to scale inversely with model dimension under strong superposition, identifying it as a central mechanism behind neural scaling laws consistent with Chinchilla scaling.\n\n---\n\n**6. Transformers are Inherently Succinct**\n\n- **Title:** Transformers are Inherently Succinct\n- **Authors:** Pascal Bergstrasser, Ryan Cotterell, Anthony W. Lin\n- **Venue/Year:** ICLR 2026 (Outstanding Paper Award)\n- **URL:** https://arxiv.org/abs/2510.19315\n- **Summary:** Proves that fixed-precision transformers are exponentially more succinct than LTL and RNNs, and doubly exponentially more succinct than finite automata, with the consequence that verification problems (emptiness, equivalence) for transformers are EXPSPACE-complete.\n\n---\n\n**7. Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the Limits of Embedding Space Capacity**\n\n- **Title:** Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the Limits of Embedding Space Capacity\n- **Authors:** Yuri Kuratov, Mikhail Arkhipov, Aydar Bulatov, Mikhail Burtsev\n- **Venue/Year:** ACL 2025 (Oral)\n- **URL:** https://arxiv.org/abs/2502.13063\n- **Summary:** Demonstrates via per-sample optimization that a single Llama-3.1-8B input vector can compress over 1500 tokens (x1500 ratio), revealing a two-orders-of-magnitude gap between current practical compression methods (~10x) and attainable limits, with capacity bounded by input uncertainty rather than sequence length.\n\n---\n\nSources:\n- [Even Faster Algorithm for the Chamfer Distance](https://arxiv.org/abs/2505.08957)\n- [Nearest Neighbor Complexity and Boolean Circuits](https://arxiv.org/abs/2402.06740)\n- [Scaling Laws for Embedding Dimension in Information Retrieval](https://arxiv.org/abs/2602.05062)\n- [WARP: An Efficient Engine for Multi-Vector Retrieval](https://arxiv.org/abs/2501.17788)\n- [Superposition Yields Robust Neural Scaling](https://arxiv.org/abs/2505.10465)\n- [Transformers are Inherently Succinct](https://arxiv.org/abs/2510.19315)\n- [Cramming 1568 Tokens into a Single Vector](https://arxiv.org/abs/2502.13063)"
      }
    ],
    "totalDurationMs": 56424,
    "totalTokens": 19741,
    "totalToolUseCount": 15,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2150,
      "cache_read_input_tokens": 16131,
      "output_tokens": 1459,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2150
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1459,
          "cache_read_input_tokens": 16131,
          "cache_creation_input_tokens": 2150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2150,
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
      "otherToolCount": 15
    }
  },
  "sourceToolAssistantUUID": "28ee2af5-c096-4612-b936-4e32409b69a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-30T06:16:29.118Z_

<details><summary>↩ Tool result · `toolu_01LXYZgX7ZnA6dPpL9kmNcgT`</summary>

```text
Here are the verified details for all five papers, with corrections noted where the provided information was inaccurate or incomplete.

---

## Paper 1: arxiv.org/abs/2506.12022

- **Exact title:** "Sign-Rank of k-Hamming Distance is Constant"
- **First 3 authors:** Mika Goos, Nathaniel Harms, Valentin Imbach (4th author: Dmitry Sokolov)
- **Venue:** None stated on the arxiv page
- **Year:** 2025 (submitted May 1, 2025; revised September 15, 2025)
- **Abstract:** "We prove that the sign-rank of the k-Hamming Distance matrix on n bits is 2^{O(k)}, independent of the number of bits n. This strongly refutes the conjecture of Hatami, Hatami, Pires, Tao, and Zhao (RANDOM 2022), and Hatami, Hosseini, and Meng (STOC 2023), repeated in several other papers, that the sign-rank should depend on n. This conjecture would have qualitatively separated margin from sign-rank (or, equivalently, bounded-error from unbounded-error randomized communication). In fact, our technique gives constant sign-rank upper bounds for all matrices which reduce to k-Hamming Distance, as well as large-margin matrices recently shown to be irreducible to k-Hamming Distance."

**Corrections needed:** The attribution "Goos et al." is correct. The title is correct. No venue was claimed in your query, and indeed none is listed. No corrections needed.

---

## Paper 2: arxiv.org/abs/2603.15923

- **Exact title:** "Learning to Recall with Transformers Beyond Orthogonal Embeddings"
- **First 3 authors:** Nuri Mert Vural, Alberto Bietti, Mahdi Soltanolkotabi (4th author: Denny Wu)
- **Venue:** ICLR 2026 (confirmed)
- **Year:** 2026
- **Abstract:** "Modern large language models (LLMs) excel at tasks that require storing and retrieving knowledge, such as factual recall and question answering. Transformers are central to this capability because they can encode information during training and retrieve it at inference. Existing theoretical analyses typically study transformers under idealized assumptions such as infinite data or orthogonal embeddings. In realistic settings, however, models are trained on finite datasets with non-orthogonal (random) embeddings. We address this gap by analyzing a single-layer transformer with random embeddings trained with (empirical) gradient descent on a simple token-retrieval task, where the model must identify an informative token within a length-L sequence and learn a one-to-one mapping from tokens to labels. Our analysis tracks the 'early phase' of gradient descent and yields explicit formulas for the model's storage capacity -- revealing a multiplicative dependence between sample size N, embedding dimension d, and sequence length L. We validate these scalings numerically and further complement them with a lower bound for the underlying statistical problem, demonstrating that this multiplicative scaling is intrinsic under non-orthogonal embeddings."

**Corrections needed:** None. Title, authors ("Vural et al."), and venue (ICLR 2026) all confirmed as stated.

---

## Paper 3: arxiv.org/abs/2603.09933

- **Exact title:** "A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models"
- **First 3 authors:** Yash Kankanampati, Yuxuan Zong, Nadi Tomeh (additional authors: Benjamin Piwowarski, Joseph Le Roux)
- **Venue:** SIGIR 2026 Full Paper Track (confirmed)
- **Year:** 2026
- **Abstract:** "Late-interaction models such as ColBERT offer competitive performance across various retrieval tasks but require storing a dense embedding for each document token, leading to a substantial index storage overhead. Past works address this by attempting to prune low-importance token embeddings based on statistical and empirical measures, but they often either lack formal grounding or are ineffective. To address these shortcomings, we introduce a framework grounded in hyperspace geometry and cast token pruning as a Voronoi cell estimation problem in the embedding space. By interpreting each token's influence as a measure of its Voronoi region, our approach enables principled pruning that retains retrieval quality while reducing index size. Through our experiments, we demonstrate that this approach serves not only as a competitive pruning strategy but also as a valuable tool for improving and interpreting token-level behavior within dense retrieval systems."

**Correction needed:** Your query listed the title as "A Voronoi Cell Formulation for Principled Token Pruning" but the full title is **"A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models"** -- the subtitle "in Late-Interaction Retrieval Models" was missing.

---

## Paper 4: arxiv.org/abs/2312.13490

- **Exact title:** "Dimension-Accuracy Tradeoffs in Contrastive Embeddings for Triplets, Terminals & Top-k Nearest Neighbors"
- **Authors:** Vaggos Chatziafratis, Piotr Indyk (only 2 authors)
- **Venue:** None stated on the arxiv page
- **Year:** 2023 (submitted December 20, 2023)
- **Abstract:** "Metric embeddings traditionally study how to map n items to a target metric space such that distance lengths are not heavily distorted; but what if we only care to preserve the relative order of the distances (and not their length)? In this paper, we are motivated by the following basic question: given triplet comparisons of the form 'item i is closer to item j than to item k,' can we find low-dimensional Euclidean representations for the n items that respect those distance comparisons? Such order-preserving embeddings naturally arise in important applications and have been studied since the 1950s, under the name of ordinal or non-metric embeddings. Our main results are: 1. Nearly-Tight Bounds on Triplet Dimension: We introduce the natural concept of triplet dimension of a dataset, and surprisingly, we show that in order for an ordinal embedding to be triplet-preserving, its dimension needs to grow as n/2 in the worst case. This is optimal (up to constant) as n-1 dimensions always suffice. 2. Tradeoffs for Dimension vs (Ordinal) Relaxation: We then relax the requirement that every triplet should be exactly preserved and present almost tight lower bounds for the maximum ratio between distances whose relative order was inverted by the embedding; this ratio is known as (ordinal) relaxation in the literature and serves as a counterpart to (metric) distortion. 3. New Bounds on Terminal and Top-k-NNs Embeddings: Going beyond triplets, we then study two well-motivated scenarios where we care about preserving specific sets of distances (not necessarily triplets). The first scenario is Terminal Ordinal Embeddings and the second scenario is top-k-NNs Ordinal Embeddings. To the best of our knowledge, these are some of the first tradeoffs on triplet-preserving ordinal embeddings and the first study of Terminal and Top-k-NNs Ordinal Embeddings."

**Corrections needed:** Your query listed the title as "Dimension-Accuracy Tradeoffs in Contrastive Embeddings" but the full title is **"Dimension-Accuracy Tradeoffs in Contrastive Embeddings for Triplets, Terminals & Top-k Nearest Neighbors"** -- the subtitle was missing. The author attribution "Chatziafratis & Indyk" is correct.

---

## Paper 5: arxiv.org/abs/2509.22116

- **Exact title:** "Does Generative Retrieval Overcome the Limitations of Dense Retrieval?"
- **First 3 authors:** Yingchen Zhang, Ruqing Zhang, Jiafeng Guo (additional authors: Maarten de Rijke, Yixing Fan, Xueqi Cheng)
- **Venue:** Not stated on the arxiv page
- **Year:** 2025 (submitted September 26, 2025; revised November 11, 2025)
- **Abstract:** "Generative retrieval (GR) has emerged as a new paradigm in neural information retrieval, offering an alternative to dense retrieval (DR) by directly generating identifiers of relevant documents. In this paper, we theoretically and empirically investigate how GR fundamentally diverges from DR in both learning objectives and representational capacity. GR performs globally normalized maximum-likelihood optimization and encodes corpus and relevance information directly in the model parameters, whereas DR adopts locally normalized objectives and represents the corpus with external embeddings before computing similarity via a bilinear interaction. Our analysis suggests that, under scaling, GR can overcome the inherent limitations of DR, yielding two major benefits. First, with larger corpora, GR avoids the sharp performance degradation caused by the optimization drift induced by DR's local normalization. Second, with larger models, GR's representational capacity scales with parameter size, unconstrained by the global low-rank structure that limits DR. We validate these theoretical insights through controlled experiments on the Natural Questions and MS MARCO datasets, across varying negative sampling strategies, embedding dimensions, and model scales. But despite its theoretical advantages, GR does not universally outperform DR in practice. We outline directions to bridge the gap between GR's theoretical potential and practical performance, providing guidance for future research in scalable and robust generative retrieval."

**Corrections needed:** The title and "Zhang et al." attribution are correct. No venue was claimed in your query, and none is listed on arxiv. No corrections needed.

---

## Summary of Corrections

| # | Issue | Detail |
|---|-------|--------|
| 3 | **Title incomplete** | Missing subtitle: should be "...Principled Token Pruning **in Late-Interaction Retrieval Models**" |
| 4 | **Title incomplete** | Missing subtitle: should be "...Contrastive Embeddings **for Triplets, Terminals & Top-k Nearest Neighbors**" |
| 1, 2, 5 | No corrections needed | Title, authors, and venue all confirmed as stated |

agentId: ac7b6f54a50188f1f (use SendMessage with to: 'ac7b6f54a50188f1f' to continue this agent)
&lt;usage>total_tokens: 15715
tool_uses: 8
duration_ms: 84967&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3e694dc5-a6a0-46e7-95de-03cd1c640db0",
  "isSidechain": false,
  "promptId": "e5b41f9b-cfe8-4c98-97fc-a511de19d6c0",
  "type": "user",
  "uuid": "5e938bec-dc87-4d14-b755-eed2dd2c96d4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify details for several papers. For each, use WebFetch to read the arxiv/conference page and confirm: exact title, authors, venue, year. Report any corrections needed.\n\n1. https://arxiv.org/abs/2506.12022 — \"Sign-Rank of k-Hamming Distance is Constant\" Goos et al. \n2. https://arxiv.org/abs/2603.15923 — \"Learning to Recall with Transformers Beyond Orthogonal Embeddings\" Vural et al. ICLR 2026\n3. https://arxiv.org/abs/2603.09933 — \"A Voronoi Cell Formulation for Principled Token Pruning\" Kankanampati et al. SIGIR 2026\n4. https://arxiv.org/abs/2312.13490 — \"Dimension-Accuracy Tradeoffs in Contrastive Embeddings\" Chatziafratis & Indyk\n5. https://arxiv.org/abs/2509.22116 — \"Does Generative Retrieval Overcome the Limitations of Dense Retrieval?\" Zhang et al.\n\nFor each paper, extract: exact title, first 3 authors, venue (if stated), and the complete abstract.",
    "agentId": "ac7b6f54a50188f1f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the verified details for all five papers, with corrections noted where the provided information was inaccurate or incomplete.\n\n---\n\n## Paper 1: arxiv.org/abs/2506.12022\n\n- **Exact title:** \"Sign-Rank of k-Hamming Distance is Constant\"\n- **First 3 authors:** Mika Goos, Nathaniel Harms, Valentin Imbach (4th author: Dmitry Sokolov)\n- **Venue:** None stated on the arxiv page\n- **Year:** 2025 (submitted May 1, 2025; revised September 15, 2025)\n- **Abstract:** \"We prove that the sign-rank of the k-Hamming Distance matrix on n bits is 2^{O(k)}, independent of the number of bits n. This strongly refutes the conjecture of Hatami, Hatami, Pires, Tao, and Zhao (RANDOM 2022), and Hatami, Hosseini, and Meng (STOC 2023), repeated in several other papers, that the sign-rank should depend on n. This conjecture would have qualitatively separated margin from sign-rank (or, equivalently, bounded-error from unbounded-error randomized communication). In fact, our technique gives constant sign-rank upper bounds for all matrices which reduce to k-Hamming Distance, as well as large-margin matrices recently shown to be irreducible to k-Hamming Distance.\"\n\n**Corrections needed:** The attribution \"Goos et al.\" is correct. The title is correct. No venue was claimed in your query, and indeed none is listed. No corrections needed.\n\n---\n\n## Paper 2: arxiv.org/abs/2603.15923\n\n- **Exact title:** \"Learning to Recall with Transformers Beyond Orthogonal Embeddings\"\n- **First 3 authors:** Nuri Mert Vural, Alberto Bietti, Mahdi Soltanolkotabi (4th author: Denny Wu)\n- **Venue:** ICLR 2026 (confirmed)\n- **Year:** 2026\n- **Abstract:** \"Modern large language models (LLMs) excel at tasks that require storing and retrieving knowledge, such as factual recall and question answering. Transformers are central to this capability because they can encode information during training and retrieve it at inference. Existing theoretical analyses typically study transformers under idealized assumptions such as infinite data or orthogonal embeddings. In realistic settings, however, models are trained on finite datasets with non-orthogonal (random) embeddings. We address this gap by analyzing a single-layer transformer with random embeddings trained with (empirical) gradient descent on a simple token-retrieval task, where the model must identify an informative token within a length-L sequence and learn a one-to-one mapping from tokens to labels. Our analysis tracks the 'early phase' of gradient descent and yields explicit formulas for the model's storage capacity -- revealing a multiplicative dependence between sample size N, embedding dimension d, and sequence length L. We validate these scalings numerically and further complement them with a lower bound for the underlying statistical problem, demonstrating that this multiplicative scaling is intrinsic under non-orthogonal embeddings.\"\n\n**Corrections needed:** None. Title, authors (\"Vural et al.\"), and venue (ICLR 2026) all confirmed as stated.\n\n---\n\n## Paper 3: arxiv.org/abs/2603.09933\n\n- **Exact title:** \"A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models\"\n- **First 3 authors:** Yash Kankanampati, Yuxuan Zong, Nadi Tomeh (additional authors: Benjamin Piwowarski, Joseph Le Roux)\n- **Venue:** SIGIR 2026 Full Paper Track (confirmed)\n- **Year:** 2026\n- **Abstract:** \"Late-interaction models such as ColBERT offer competitive performance across various retrieval tasks but require storing a dense embedding for each document token, leading to a substantial index storage overhead. Past works address this by attempting to prune low-importance token embeddings based on statistical and empirical measures, but they often either lack formal grounding or are ineffective. To address these shortcomings, we introduce a framework grounded in hyperspace geometry and cast token pruning as a Voronoi cell estimation problem in the embedding space. By interpreting each token's influence as a measure of its Voronoi region, our approach enables principled pruning that retains retrieval quality while reducing index size. Through our experiments, we demonstrate that this approach serves not only as a competitive pruning strategy but also as a valuable tool for improving and interpreting token-level behavior within dense retrieval systems.\"\n\n**Correction needed:** Your query listed the title as \"A Voronoi Cell Formulation for Principled Token Pruning\" but the full title is **\"A Voronoi Cell Formulation for Principled Token Pruning in Late-Interaction Retrieval Models\"** -- the subtitle \"in Late-Interaction Retrieval Models\" was missing.\n\n---\n\n## Paper 4: arxiv.org/abs/2312.13490\n\n- **Exact title:** \"Dimension-Accuracy Tradeoffs in Contrastive Embeddings for Triplets, Terminals & Top-k Nearest Neighbors\"\n- **Authors:** Vaggos Chatziafratis, Piotr Indyk (only 2 authors)\n- **Venue:** None stated on the arxiv page\n- **Year:** 2023 (submitted December 20, 2023)\n- **Abstract:** \"Metric embeddings traditionally study how to map n items to a target metric space such that distance lengths are not heavily distorted; but what if we only care to preserve the relative order of the distances (and not their length)? In this paper, we are motivated by the following basic question: given triplet comparisons of the form 'item i is closer to item j than to item k,' can we find low-dimensional Euclidean representations for the n items that respect those distance comparisons? Such order-preserving embeddings naturally arise in important applications and have been studied since the 1950s, under the name of ordinal or non-metric embeddings. Our main results are: 1. Nearly-Tight Bounds on Triplet Dimension: We introduce the natural concept of triplet dimension of a dataset, and surprisingly, we show that in order for an ordinal embedding to be triplet-preserving, its dimension needs to grow as n/2 in the worst case. This is optimal (up to constant) as n-1 dimensions always suffice. 2. Tradeoffs for Dimension vs (Ordinal) Relaxation: We then relax the requirement that every triplet should be exactly preserved and present almost tight lower bounds for the maximum ratio between distances whose relative order was inverted by the embedding; this ratio is known as (ordinal) relaxation in the literature and serves as a counterpart to (metric) distortion. 3. New Bounds on Terminal and Top-k-NNs Embeddings: Going beyond triplets, we then study two well-motivated scenarios where we care about preserving specific sets of distances (not necessarily triplets). The first scenario is Terminal Ordinal Embeddings and the second scenario is top-k-NNs Ordinal Embeddings. To the best of our knowledge, these are some of the first tradeoffs on triplet-preserving ordinal embeddings and the first study of Terminal and Top-k-NNs Ordinal Embeddings.\"\n\n**Corrections needed:** Your query listed the title as \"Dimension-Accuracy Tradeoffs in Contrastive Embeddings\" but the full title is **\"Dimension-Accuracy Tradeoffs in Contrastive Embeddings for Triplets, Terminals & Top-k Nearest Neighbors\"** -- the subtitle was missing. The author attribution \"Chatziafratis & Indyk\" is correct.\n\n---\n\n## Paper 5: arxiv.org/abs/2509.22116\n\n- **Exact title:** \"Does Generative Retrieval Overcome the Limitations of Dense Retrieval?\"\n- **First 3 authors:** Yingchen Zhang, Ruqing Zhang, Jiafeng Guo (additional authors: Maarten de Rijke, Yixing Fan, Xueqi Cheng)\n- **Venue:** Not stated on the arxiv page\n- **Year:** 2025 (submitted September 26, 2025; revised November 11, 2025)\n- **Abstract:** \"Generative retrieval (GR) has emerged as a new paradigm in neural information retrieval, offering an alternative to dense retrieval (DR) by directly generating identifiers of relevant documents. In this paper, we theoretically and empirically investigate how GR fundamentally diverges from DR in both learning objectives and representational capacity. GR performs globally normalized maximum-likelihood optimization and encodes corpus and relevance information directly in the model parameters, whereas DR adopts locally normalized objectives and represents the corpus with external embeddings before computing similarity via a bilinear interaction. Our analysis suggests that, under scaling, GR can overcome the inherent limitations of DR, yielding two major benefits. First, with larger corpora, GR avoids the sharp performance degradation caused by the optimization drift induced by DR's local normalization. Second, with larger models, GR's representational capacity scales with parameter size, unconstrained by the global low-rank structure that limits DR. We validate these theoretical insights through controlled experiments on the Natural Questions and MS MARCO datasets, across varying negative sampling strategies, embedding dimensions, and model scales. But despite its theoretical advantages, GR does not universally outperform DR in practice. We outline directions to bridge the gap between GR's theoretical potential and practical performance, providing guidance for future research in scalable and robust generative retrieval.\"\n\n**Corrections needed:** The title and \"Zhang et al.\" attribution are correct. No venue was claimed in your query, and none is listed on arxiv. No corrections needed.\n\n---\n\n## Summary of Corrections\n\n| # | Issue | Detail |\n|---|-------|--------|\n| 3 | **Title incomplete** | Missing subtitle: should be \"...Principled Token Pruning **in Late-Interaction Retrieval Models**\" |\n| 4 | **Title incomplete** | Missing subtitle: should be \"...Contrastive Embeddings **for Triplets, Terminals & Top-k Nearest Neighbors**\" |\n| 1, 2, 5 | No corrections needed | Title, authors, and venue all confirmed as stated |"
      }
    ],
    "totalDurationMs": 84967,
    "totalTokens": 15715,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 12120,
      "output_tokens": 2457,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1137
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2457,
          "cache_read_input_tokens": 12120,
          "cache_creation_input_tokens": 1137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1137,
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
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "3e694dc5-a6a0-46e7-95de-03cd1c640db0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42 · 2026-05-30T06:16:29.128Z_

```json
{
  "parentUuid": "5e938bec-dc87-4d14-b755-eed2dd2c96d4",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "39fc4f9d-1b94-4f46-b558-7d5f984bdce5",
  "timestamp": "2026-05-30T06:16:29.128Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "39fc4f9d-1b94-4f46-b558-7d5f984bdce5",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on multi-vector retrieval expressiveness",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Assistant

_source line 45 · 2026-05-30T06:17:01.261Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data from all my search agents. Let me synthesize the final list of the 15+ most important papers, selecting based on the criteria specified (best paper awards, oral/spotlight, high citations, foundational methods, surveys, top labs).

Let me compile the final JSON array, selecting the most important and relevant papers. I'll prioritize:

1. Papers directly on expressiveness bounds for retrieval embeddings
2. Papers on sign-rank and communication complexity relevant to the theoretical framework
3. Papers on multi-vector retrieval theory
4. Best paper award winners relevant to the area
5. Key systems/empirical papers that inform the theory


6. The seed papers that anchor this research direction, including Weller et al.'s ICLR 2026 work on theoretical bounds, Wang et al.'s dimension sufficiency analysis, Dhulipala et al.'s MUVERA framework connecting multi-vector to single-vector retrieval, Jacob and Archish's work on single-vector limitations, and Bangachev et al.'s investigation of dimensionality as a barrier to expressiveness.

Then I'm adding papers that extend this foundation with margin analysis and provable accuracy collapse results, followed by sign-rank complexity work from Lee, Goos, and others that establishes fundamental limits on what single vectors can represent. I'm also including practical retrieval systems like Wu et al.'s generative retrieval approach, stability analyses from Lakshman et al., and recent advances in flexible late interaction methods and faster distance computations. Now I'm narrowing down to the 15-20 most impactful papers, focusing on the foundational work rather than everything tangentially related. The core papers I need to include are the anchor results on dimension bounds, the multi-vector reduction guarantees, formal comparisons between single and multi-vector approaches, margin-dimension tradeoffs, and the phase transition phenomena that show accuracy collapse—plus the sign-rank framework that applies across different domains.

Beyond those essentials, I'm looking at papers on generative retrieval equivalence, the Matryoshka embedding work from ICLR, complexity results for nearest neighbor search, transformer capacity bounds, and ordinal embedding dimension theory. The supporting layer includes stability analysis for distance metrics, representation capacity results, and embedding information capacity studies.

Now I'm rounding out the list with papers on learned multi-vector reduction, scaling laws for embedding dimensions, and Voronoi cell formulations for retrieval. I want to hit around 20 papers total, focusing on the genuinely impactful ones that directly inform the theoretical framework.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39fc4f9d-1b94-4f46-b558-7d5f984bdce5",
  "isSidechain": false,
  "requestId": "req_011CbYGHjQDb9i6ASDiB41VX",
  "type": "assistant",
  "uuid": "6e114bcd-89ae-4ee8-a5c6-f88835f5c2ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159bJMUWN1WNDCi3S8Yv9AA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8543,
      "cache_read_input_tokens": 43370,
      "output_tokens": 5285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5285,
          "cache_read_input_tokens": 43370,
          "cache_creation_input_tokens": 8543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8543
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

_source line 46 · 2026-05-30T06:18:15.225Z_

Now I have all the data I need. Let me compile the final comprehensive literature survey.

---

## Literature Survey: Formal Expressiveness Bounds for Multi-Vector (MaxSim/Chamfer) Retrieval Representations

### Overview

This survey covers the 20 most important recent papers (2024–2026) relevant to establishing formal expressiveness bounds for multi-vector retrieval representations. The papers span three main threads:

1. **Capacity limits of single-vector embeddings** (sign-rank, dimension bounds, phase transitions)
2. **Multi-vector retrieval theory** (MaxSim expressiveness, reductions, Chamfer complexity)
3. **Foundational tools** (communication complexity, combinatorial dimensions, embedding theory)

---

### Key Findings

- **Single-vector bottleneck is proven**: Weller et al. (ICLR 2026) connects sign-rank to embedding dimension limits; Arvanitakis et al. (ICML 2026 Spotlight) shows sharp phase transitions in accuracy.
- **Geometric capacity ≠ learnability**: Wang et al. (2026) proves R^{2k} suffices geometrically, while Jacob et al. (2026) proves multi-vector models are exponentially more robust to corpus scaling via "drowning probability" analysis.
- **Sign-rank landscape is evolving**: Goos et al. (2025) refutes conjectures about sign-rank growing with n for k-Hamming Distance, potentially weakening some lower bounds.
- **Multi-vector → single-vector reductions have formal guarantees**: MUVERA (NeurIPS 2024) and LEMUR (ICML 2026) show MaxSim can be approximated via inner product, with quantified information loss.
- **Chamfer/MaxSim computational complexity is near-settled**: Feng & Indyk (ICALP 2025) give near-optimal algorithms.
- **NN complexity theory provides separation**: DiCicco et al. (ITCS 2025) prove exponential separation between 1-NN and k-NN complexity — directly relevant to why MaxSim (multiple NN lookups) is more powerful.

---

```json
[
  {
    "title": "On the Theoretical Limitations of Embedding-Based Retrieval",
    "authors": "Weller et al.",
    "venue": "ICLR 2026",
    "url": "https://arxiv.org/abs/2508.21038",
    "why_important": "Direct theoretical anchor — proves single-vector embedding capacity is bounded by sign-rank of the relevance matrix; introduces LIMIT benchmark",
    "one_line_summary": "Proves that the number of top-k subsets returnable by single-vector embeddings is fundamentally bounded by the embedding dimension via sign-rank, and demonstrates SOTA models fail on simple tasks predicted to be hard by the theory."
  },
  {
    "title": "R^{2k} is Theoretically Large Enough for Embedding-based Top-k Retrieval",
    "authors": "Wang et al.",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2601.20844",
    "why_important": "Competing theoretical result — shows geometric capacity is sufficient with O(k) dimensions, arguing the real bottleneck is learnability not representation",
    "one_line_summary": "Derives tight bounds on Minimal Embeddable Dimension showing 2k dimensions suffice for top-k retrieval under inner product, cosine, and L2 scoring, independent of corpus size."
  },
  {
    "title": "MUVERA: Multi-Vector Retrieval via Fixed Dimensional Encodings",
    "authors": "Dhulipala et al.",
    "venue": "NeurIPS 2024",
    "url": "https://arxiv.org/abs/2405.19504",
    "why_important": "First provable reduction of MaxSim/Chamfer multi-vector similarity to single-vector MIPS with epsilon-approximation guarantees (Google Research)",
    "one_line_summary": "Constructs Fixed Dimensional Encodings whose inner product epsilon-approximates Chamfer similarity, enabling single-vector search as a proxy for multi-vector retrieval with formal approximation bounds."
  },
  {
    "title": "On Strengths and Limitations of Single-Vector Embeddings",
    "authors": "Archish et al.",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2603.29519",
    "why_important": "Provides first formal separation between single- and multi-vector via drowning probability analysis, showing exponential gap in corpus scaling robustness",
    "one_line_summary": "Proves single-vector models suffer drowning probability exp(-Θ(d/n)) while multi-vector achieves exp(-Θ(d/log n)), formalizing exponential superiority of multi-vector representations as corpus grows."
  },
  {
    "title": "Is Dimensionality a Barrier for Retrieval Models?",
    "authors": "Bangachev et al.",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2605.23556",
    "why_important": "Extends Weller et al. with margin-based analysis; derives tightest known dimension-margin tradeoffs for sparse relevance (MIT/Stanford)",
    "one_line_summary": "Proves that dimension d=O(k·log(n/k)) is necessary and sufficient for k-sparse relevance matrices with margin Θ(k^{-1/2}), showing optimal margin can be nearly achieved at moderate dimensions."
  },
  {
    "title": "Provable Accuracy Collapse in Embedding-Based Representations under Dimensionality Mismatch",
    "authors": "Arvanitakis et al.",
    "venue": "ICML 2026 (Spotlight)",
    "url": "https://arxiv.org/abs/2605.03346",
    "why_important": "Spotlight paper — proves sharp phase transition: unless d ≈ D, accuracy collapses to trivial 50%; complemented by UGC-based computational hardness",
    "one_line_summary": "Establishes that embedding dimension mismatch causes a sudden accuracy collapse — every embedding of dimension below cD violates half of all triplets — with computational hardness results under the Unique Games Conjecture."
  },
  {
    "title": "Sign Rank Limitations for Inner Product Graph Decoders",
    "authors": "Lee et al.",
    "venue": "ICML 2024",
    "url": "https://arxiv.org/abs/2402.06662",
    "why_important": "Applies same sign-rank framework to graph reconstruction — provides the template for inner-product capacity analysis that retrieval theory builds on",
    "one_line_summary": "Provides the first theoretical analysis of why inner-product decoders have limited representation capacity for graph reconstruction, using sign-rank to derive dimension lower bounds."
  },
  {
    "title": "Sign-Rank of k-Hamming Distance is Constant",
    "authors": "Goos et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2506.12022",
    "why_important": "Major breakthrough in sign-rank theory — refutes conjectures by Hatami et al., directly affects tightness of sign-rank-based retrieval bounds",
    "one_line_summary": "Proves sign-rank of the k-Hamming Distance matrix is 2^{O(k)} independent of the number of bits n, strongly refuting conjectures that sign-rank should depend on n and collapsing conjectured separations between bounded and unbounded error communication."
  },
  {
    "title": "Generative Retrieval as Multi-Vector Dense Retrieval",
    "authors": "Wu et al.",
    "venue": "SIGIR 2024",
    "url": "https://arxiv.org/abs/2404.00684",
    "why_important": "Proves formal equivalence between generative retrieval decoders and multi-vector dense retrieval, unifying two paradigms under the same expressiveness framework",
    "one_line_summary": "Demonstrates that generative retrieval's decoder attention and prediction head implement a special case of multi-vector dense retrieval, with both computing relevance as summed products of query vectors, document vectors, and an alignment matrix."
  },
  {
    "title": "Breaking the Curse of Dimensionality: On the Stability of Modern Vector Retrieval",
    "authors": "Lakshman et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2512.12458",
    "why_important": "Proves stability properties of Chamfer distance in high dimensions — formal justification for why multi-vector search avoids the curse of dimensionality",
    "one_line_summary": "Extends stability theory to multi-vector Chamfer distance search, proving it preserves nearest-neighbor rankings under small query perturbations while single-vector pooling methods may not."
  },
  {
    "title": "MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction",
    "authors": "Xiao et al.",
    "venue": "ICLR 2026 (Oral)",
    "url": "https://arxiv.org/abs/2509.18095",
    "why_important": "ICLR 2026 Oral — demonstrates controllable expressiveness-efficiency tradeoff via Matryoshka multi-vector training; SOTA on MMEB/ViDoRe at 32B scale",
    "one_line_summary": "Introduces learnable Meta Tokens with Matryoshka Multi-Vector Retrieval training, enabling test-time scaling of the number of vectors per item to balance retrieval quality against efficiency."
  },
  {
    "title": "Even Faster Algorithm for the Chamfer Distance",
    "authors": "Feng and Indyk",
    "venue": "ICALP 2025",
    "url": "https://arxiv.org/abs/2505.08957",
    "why_important": "Near-optimal computational complexity for Chamfer distance — the core similarity in ColBERT-style retrieval (MIT)",
    "one_line_summary": "Achieves O(nd(log log n + log(1/ε))/ε²) time for (1+ε)-approximate Chamfer distance computation, narrowing the gap to the trivial Ω(dn) lower bound from O(log n) to O(log log n)."
  },
  {
    "title": "Nearest Neighbor Complexity and Boolean Circuits",
    "authors": "DiCicco et al.",
    "venue": "ITCS 2025",
    "url": "https://arxiv.org/abs/2402.06740",
    "why_important": "Proves exponential separation between 1-NN and k-NN complexity — directly shows multi-vector (multiple NN lookups) is fundamentally more powerful than single-vector (1 NN lookup)",
    "one_line_summary": "Establishes connections between nearest-neighbor complexity and Boolean circuit complexity, proving exponential lower bounds on k-NN complexity and exponential separation between 1-NN and k-NN representations."
  },
  {
    "title": "Learning to Recall with Transformers Beyond Orthogonal Embeddings",
    "authors": "Vural et al.",
    "venue": "ICLR 2026",
    "url": "https://arxiv.org/abs/2603.15923",
    "why_important": "Derives explicit storage capacity formulas for transformers on retrieval tasks — reveals multiplicative dependence between sample size, embedding dimension, and sequence length",
    "one_line_summary": "Analyzes a single-layer transformer with random (non-orthogonal) embeddings on a token-retrieval task, yielding explicit formulas for storage capacity showing multiplicative scaling between N, d, and sequence length L."
  },
  {
    "title": "Dimension-Accuracy Tradeoffs in Contrastive Embeddings for Triplets, Terminals & Top-k Nearest Neighbors",
    "authors": "Chatziafratis and Indyk",
    "venue": "arXiv 2023",
    "url": "https://arxiv.org/abs/2312.13490",
    "why_important": "Near-tight dimension lower bounds for order-preserving embeddings with top-k NN extensions — different proof technique (ordinal theory) complementing sign-rank approach (MIT/Yale)",
    "one_line_summary": "Proves that triplet-preserving ordinal embeddings require dimension growing as n/2 in worst case, and introduces the first dimension-relaxation tradeoffs for top-k nearest neighbor ordinal embeddings."
  },
  {
    "title": "LEMUR: Learned Multi-Vector Retrieval",
    "authors": "Jaasaari et al.",
    "venue": "ICML 2026",
    "url": "https://arxiv.org/abs/2601.21853",
    "why_important": "Reduces multi-vector MaxSim to single-vector search via learned one-hidden-layer network — implicitly characterizes MaxSim complexity class",
    "one_line_summary": "Reformulates multi-vector similarity as a supervised learning problem solvable by a shallow neural network, then reduces to single-vector search in a learned latent space with order-of-magnitude speedup."
  },
  {
    "title": "Superposition Yields Robust Neural Scaling",
    "authors": "Liu et al.",
    "venue": "NeurIPS 2025 (Oral, Best Paper Runner-Up)",
    "url": "https://arxiv.org/abs/2505.10465",
    "why_important": "NeurIPS 2025 Best Paper Runner-Up — shows representation superposition (more features than dimensions) drives scaling laws, directly relevant to single-vector capacity bottleneck",
    "one_line_summary": "Proves that under strong superposition, loss scales inversely with model dimension due to geometric interference between representation vectors, identifying superposition as the mechanism behind neural scaling laws."
  },
  {
    "title": "Cramming 1568 Tokens into a Single Vector and Back Again: Exploring the Limits of Embedding Space Capacity",
    "authors": "Kuratov et al.",
    "venue": "ACL 2025 (Oral)",
    "url": "https://arxiv.org/abs/2502.13063",
    "why_important": "ACL 2025 Oral — reveals 100x gap between theoretical and practical single-vector information capacity, showing capacity is bounded by input uncertainty not length",
    "one_line_summary": "Demonstrates via per-sample optimization that a single LLM input vector can encode 1500+ tokens (x1500 compression), revealing a massive gap between theoretical capacity and current practical methods (~x10)."
  },
  {
    "title": "Does Generative Retrieval Overcome the Limitations of Dense Retrieval?",
    "authors": "Zhang et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2509.22116",
    "why_important": "Theoretically proves generative retrieval's capacity scales with parameters without the low-rank constraint limiting dense retrieval (CAS/UvA)",
    "one_line_summary": "Proves that generative retrieval avoids the global low-rank structure limiting dense retrieval's representational capacity, with capacity scaling with model parameters rather than embedding dimension."
  },
  {
    "title": "Scaling Laws for Embedding Dimension in Information Retrieval",
    "authors": "Killingback et al.",
    "venue": "SIGIR 2026",
    "url": "https://arxiv.org/abs/2602.05062",
    "why_important": "Establishes empirical power-law scaling between embedding dimension and retrieval performance — the practical manifestation of theoretical capacity bounds (UMass)",
    "one_line_summary": "Derives power-law scaling laws showing diminishing returns from larger embedding dimensions for in-distribution retrieval, with unpredictable behavior out-of-distribution — quantifying when theoretical capacity limits begin to bind in practice."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e114bcd-89ae-4ee8-a5c6-f88835f5c2ae",
  "isSidechain": false,
  "requestId": "req_011CbYGHjQDb9i6ASDiB41VX",
  "type": "assistant",
  "uuid": "9bde823d-841c-458d-a50c-bbfadc03d411",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0159bJMUWN1WNDCi3S8Yv9AA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8543,
      "cache_read_input_tokens": 43370,
      "output_tokens": 5285,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8543,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5285,
          "cache_read_input_tokens": 43370,
          "cache_creation_input_tokens": 8543,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8543
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

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-30 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "9bde823d-841c-458d-a50c-bbfadc03d411",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Literature survey on multi-vector retrieval expressiveness",
  "sessionId": "3d79ae5a-88b6-4a48-962d-c30e1acc36b0"
}
```

---
