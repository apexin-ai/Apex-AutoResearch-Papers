# Research conversation: You are a senior ML researcher performing deep analysis of multiple published papers. **Today's date: 2026-05-30 (UTC).*

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/71c77089-edc5-4f43-b783-1817930f1119.jsonl`
- **Structured JSON:** [`090a8ca7c729eb0d9153.json`](../../sessions/09/090a8ca7c729eb0d9153.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:20:38.125Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:20:38.125Z",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "content": "You are a senior ML researcher performing deep analysis of multiple published papers.\n\n**Today's date: 2026-05-30 (UTC).**\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: Information Retrieval and Text Mining (Main Technical Track)\n\nDirection: Train a single decoder-only LLM (Llama-3-8B) to simultaneously produce both SPLADE-style sparse representations and dense bi-encoder representations through dual output heads, with a lightweight learned query router that adaptively weights sparse vs. dense retrieval per query. The model is trained via a 3-stage curriculum (independent head pre-training, joint fine-tuning with bidirectional self-distillation, router refinement) and evaluated on MS MARCO, BEIR, and MTEB benchmarks.\n\nSeed Papers:\n- LACONIC-8B (arXiv, Jan 2026) — proves decoder-only LLMs (Llama-3-8B) achieve dense-level effectiveness for sparse retrieval via two-phase curriculum; establishes the sparse head baseline\n- Scaling Sparse and Dense Retrieval in Decoder-Only LLMs (SIGIR, 2025) — systematic comparison showing sparse outperforms dense by 10.5% on BEIR at 8B scale in decoder-only models; confirms complementarity but trains separate models\n- BGE M3-Embedding (arXiv, 2024) — unifies dense+sparse+multi-vec in one encoder-only model with self-KD; proves multi-functionality works but limited to XLM-RoBERTa backbone and fixed interpolation weights\n- RouterRetriever (AAAI, 2025) — learned per-query routing over expert embedding models with +2.1 NDCG@10 gain; proves routing works but routes between separate dense models only\n- CSplade (IJCNLP-AACL, 2025) — documents training instabilities with ReLU sparse heads in causal LMs and proposes mitigations; critical for training stability\n- Sparse and Dense Retrievers Learn Better Together (CIKM, 2025) — bidirectional self-KD between sparse and dense heads improves both in VLP models; proves the self-distillation mechanism but only for text-image retrieval\n\nKnown Gaps:\n- No decoder-only LLM produces both sparse AND dense representations from a single forward pass — LACONIC and Lion-SP/DS train separate models for each modality\n- No learned per-query router exists WITHIN a unified retrieval model — BGE-M3 uses fixed linear interpolation; RouterRetriever routes between separate external models\n- Bidirectional self-distillation between sparse and dense heads has never been studied in decoder-only backbones — only in encoder-only (BGE-M3) and VLP (CIKM 2025) models\n\nTheoretical Anchor: Sparse and dense representations capture complementary information — sparse captures lexical matching signals (exact term overlap, entity names) while dense captures semantic matching signals (paraphrases, conceptual similarity). Lion-SP (SIGIR 2025) showed this complementarity is especially pronounced in decoder-only models (10.5% gap on BEIR). A learned router can exploit query-level signals (specificity, entity density, ambiguity) to optimally weight these complementary representations per query, achieving near-oracle hybrid performance while avoiding the latency cost of always computing both.\n\nConstraints:\n- Compute: ≤200 H100-hours (3B model: ~60hrs for 3-stage training; 8B model: ~120hrs)\n\nQuality Self-Checks:\n- [x] Core insight: Sparse and dense retrieval are complementary in decoder-only LLMs, and a learned per-query router can exploit this complementarity within a single model.\n- [x] Why not obvious: Joint training of sparse and dense heads in decoder-only models faces instability (documented by CSplade); the BGE-M3 approach doesn't directly transfer because encoder-only and decoder-only attention patterns differ fundamentally; and existing routing work operates between separate models, not within a unified architecture.\n- [x] Baseline fear test: Fixed-weight interpolation (the simple baseline) cannot match learned routing because the optimal sparse-dense weight varies dramatically across query types — entity-heavy queries favor sparse while conceptual queries favor dense. The router exploits query-level features that fixed weights ignore.\n- [x] Information exploited: The method exploits (1) per-query lexical vs. semantic difficulty signals via the router head, (2) complementary error patterns between sparse and dense heads via bidirectional self-distillation, and (3) shared backbone representations that transfer knowledge between modalities during joint training.\n\nAvoid:\n- Fixed-weight linear interpolation between sparse and dense scores (this is the well-explored BM25+dense hybrid baseline; the contribution must be LEARNED per-query routing)\n- Separate model ensembles (the contribution requires a SINGLE backbone model with shared parameters; separate sparse and dense models with a router on top is just RouterRetriever)\n- ColBERT/multi-vector retrieval as a third head (adds complexity without addressing the core sparse-vs-dense question; save for future work)\n- Scaling beyond 8B parameters (diminishing returns documented by SIGIR 2025; focus on architecture and training, not scale)**\n\n## Your task (Batch 3)\n\nAnalyze the following 4 papers. For EACH paper:\n1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.\n2. If on OpenReview, also read reviewer comments.\n3. Write a concise analysis focusing on HOW the paper innovates.\n\n## Papers to analyze\n\n[\n  {\n    \"title\": \"NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models\",\n    \"authors\": \"Chankyu Lee, Rajarshi Roy, Mengyao Xu, Jonathan Raiman, Mohammad Shoeybi, Bryan Catanzaro, Wei Ping\",\n    \"venue\": \"ICLR 2025 (Spotlight)\",\n    \"url\": \"https://arxiv.org/abs/2405.17428\",\n    \"why_important\": \"ICLR 2025 Spotlight. Introduces latent attention pooling and demonstrates that removing causal attention masks during contrastive training improves decoder-only embeddings. Two-stage contrastive instruction-tuning pipeline is directly applicable to the proposed curriculum. Topped MTEB leaderboard.\",\n    \"one_line_summary\": \"Proposes latent attention pooling and a two-stage contrastive fine-tuning pipeline to convert Mistral-7B into the top-ranked generalist embedding model on MTEB, with key insight that removing causal masking during training helps.\"\n  },\n  {\n    \"title\": \"Scaling Laws for Dense Retrieval\",\n    \"authors\": \"Yan Fang, Jingtao Zhan, Qingyao Ai, Jiaxin Mao, Weihang Su, Jia Chen, Yiqun Liu\",\n    \"venue\": \"SIGIR 2024 — Best Paper Award\",\n    \"url\": \"https://arxiv.org/abs/2403.18684\",\n    \"why_important\": \"Best Paper at SIGIR 2024. Establishes precise power-law scaling relationships for dense retrieval as a function of model size and training data, enabling principled resource allocation. Directly informs the compute budget decisions for the proposed 3B/8B training.\",\n    \"one_line_summary\": \"Demonstrates that dense retrieval accuracy follows predictable power-law scaling in model parameters and annotation volume, providing actionable guidance for training budget allocation.\"\n  },\n  {\n    \"title\": \"SPLARE: Learning Retrieval Models with Sparse Autoencoders\",\n    \"authors\": \"Thibault Formal, Maxime Louis, Hervé Déjean, Stéphane Clinchant\",\n    \"venue\": \"arXiv 2026\",\n    \"url\": \"https://arxiv.org/abs/2603.13277\",\n    \"why_important\": \"Proposes a fundamentally new approach to learned sparse retrieval using sparse autoencoders to decompose LLM representations into interpretable latent features instead of vocabulary-space projection. More language-agnostic than SPLADE. SPLARE-7B achieves top results on MMTEB multilingual and English retrieval.\",\n    \"one_line_summary\": \"Replaces SPLADE's vocabulary-space projection with sparse autoencoders that decompose LLM representations into interpretable latent features, producing language-agnostic sparse representations that outperform SPLADE on multilingual retrieval.\"\n  },\n  {\n    \"title\": \"A Survey of Model Architectures in Information Retrieval\",\n    \"authors\": \"Zhichao Xu, Fengran Mo, Zhiqi Huang, Crystina Zhang, Puxuan Yu, Bei Wang, Jimmy Lin, Vivek Srikumar\",\n    \"venue\": \"TMLR 2025\",\n    \"url\": \"https://arxiv.org/abs/2502.14822\",\n    \"why_important\": \"Comprehensive survey (by the LACONIC first author) covering the full design space of sparse, dense, and hybrid retrieval architectures. Separates architecture from training methodology and traces the evolution from term-based to neural models. Essential reference for positioning the proposed work.\",\n    \"one_line_summary\": \"An exhaustive survey tracing IR model architectures from traditional term-based methods through BERT bi-encoders to decoder-only LLMs, covering dense, sparse, hybrid, and generative retrieval paradigms.\"\n  }\n]\n\n## Analysis requirements\n\nFor each paper, analyze:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- If reviewer comments are available: what was praised, what was criticized?\n\n## CRITICAL: Length constraint\n\n**Each paper's analysis MUST be under 2000 characters.** Be concise and analytical — no filler, no generic praise, no redundant descriptions. Every sentence must carry information.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem? How found? (1-2 sentences)\",\n  \"key_insight\": \"Core intellectual contribution (1 sentence)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach (2-3 sentences)\",\n  \"limitations_and_open_questions\": \"Gaps + follow-up questions (1-2 sentences)\",\n  \"building_blocks\": [\"Reusable methods/tools/datasets\"],\n  \"relevance_to_seed\": \"Relation to our research area (1 sentence)\"\n}\n\nYou MUST output exactly 4 analyses in the JSON array. IMPORTANT: End your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:20:38.137Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:20:38.137Z",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---

## Round 1

24 recorded events

### User

_source line 3 · 2026-05-30T06:20:38.272Z_

You are a senior ML researcher performing deep analysis of multiple published papers.

**Today's date: 2026-05-30 (UTC).**

## Research context

We are generating ideas in the area of: **Target: AAAI 2026
Track: Information Retrieval and Text Mining (Main Technical Track)

Direction: Train a single decoder-only LLM (Llama-3-8B) to simultaneously produce both SPLADE-style sparse representations and dense bi-encoder representations through dual output heads, with a lightweight learned query router that adaptively weights sparse vs. dense retrieval per query. The model is trained via a 3-stage curriculum (independent head pre-training, joint fine-tuning with bidirectional self-distillation, router refinement) and evaluated on MS MARCO, BEIR, and MTEB benchmarks.

Seed Papers:
- LACONIC-8B (arXiv, Jan 2026) — proves decoder-only LLMs (Llama-3-8B) achieve dense-level effectiveness for sparse retrieval via two-phase curriculum; establishes the sparse head baseline
- Scaling Sparse and Dense Retrieval in Decoder-Only LLMs (SIGIR, 2025) — systematic comparison showing sparse outperforms dense by 10.5% on BEIR at 8B scale in decoder-only models; confirms complementarity but trains separate models
- BGE M3-Embedding (arXiv, 2024) — unifies dense+sparse+multi-vec in one encoder-only model with self-KD; proves multi-functionality works but limited to XLM-RoBERTa backbone and fixed interpolation weights
- RouterRetriever (AAAI, 2025) — learned per-query routing over expert embedding models with +2.1 NDCG@10 gain; proves routing works but routes between separate dense models only
- CSplade (IJCNLP-AACL, 2025) — documents training instabilities with ReLU sparse heads in causal LMs and proposes mitigations; critical for training stability
- Sparse and Dense Retrievers Learn Better Together (CIKM, 2025) — bidirectional self-KD between sparse and dense heads improves both in VLP models; proves the self-distillation mechanism but only for text-image retrieval

Known Gaps:
- No decoder-only LLM produces both sparse AND dense representations from a single forward pass — LACONIC and Lion-SP/DS train separate models for each modality
- No learned per-query router exists WITHIN a unified retrieval model — BGE-M3 uses fixed linear interpolation; RouterRetriever routes between separate external models
- Bidirectional self-distillation between sparse and dense heads has never been studied in decoder-only backbones — only in encoder-only (BGE-M3) and VLP (CIKM 2025) models

Theoretical Anchor: Sparse and dense representations capture complementary information — sparse captures lexical matching signals (exact term overlap, entity names) while dense captures semantic matching signals (paraphrases, conceptual similarity). Lion-SP (SIGIR 2025) showed this complementarity is especially pronounced in decoder-only models (10.5% gap on BEIR). A learned router can exploit query-level signals (specificity, entity density, ambiguity) to optimally weight these complementary representations per query, achieving near-oracle hybrid performance while avoiding the latency cost of always computing both.

Constraints:
- Compute: ≤200 H100-hours (3B model: ~60hrs for 3-stage training; 8B model: ~120hrs)

Quality Self-Checks:
- [x] Core insight: Sparse and dense retrieval are complementary in decoder-only LLMs, and a learned per-query router can exploit this complementarity within a single model.
- [x] Why not obvious: Joint training of sparse and dense heads in decoder-only models faces instability (documented by CSplade); the BGE-M3 approach doesn't directly transfer because encoder-only and decoder-only attention patterns differ fundamentally; and existing routing work operates between separate models, not within a unified architecture.
- [x] Baseline fear test: Fixed-weight interpolation (the simple baseline) cannot match learned routing because the optimal sparse-dense weight varies dramatically across query types — entity-heavy queries favor sparse while conceptual queries favor dense. The router exploits query-level features that fixed weights ignore.
- [x] Information exploited: The method exploits (1) per-query lexical vs. semantic difficulty signals via the router head, (2) complementary error patterns between sparse and dense heads via bidirectional self-distillation, and (3) shared backbone representations that transfer knowledge between modalities during joint training.

Avoid:
- Fixed-weight linear interpolation between sparse and dense scores (this is the well-explored BM25+dense hybrid baseline; the contribution must be LEARNED per-query routing)
- Separate model ensembles (the contribution requires a SINGLE backbone model with shared parameters; separate sparse and dense models with a router on top is just RouterRetriever)
- ColBERT/multi-vector retrieval as a third head (adds complexity without addressing the core sparse-vs-dense question; save for future work)
- Scaling beyond 8B parameters (diminishing returns documented by SIGIR 2025; focus on architecture and training, not scale)**

## Your task (Batch 3)

Analyze the following 4 papers. For EACH paper:
1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.
2. If on OpenReview, also read reviewer comments.
3. Write a concise analysis focusing on HOW the paper innovates.

## Papers to analyze

[
  {
    "title": "NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models",
    "authors": "Chankyu Lee, Rajarshi Roy, Mengyao Xu, Jonathan Raiman, Mohammad Shoeybi, Bryan Catanzaro, Wei Ping",
    "venue": "ICLR 2025 (Spotlight)",
    "url": "https://arxiv.org/abs/2405.17428",
    "why_important": "ICLR 2025 Spotlight. Introduces latent attention pooling and demonstrates that removing causal attention masks during contrastive training improves decoder-only embeddings. Two-stage contrastive instruction-tuning pipeline is directly applicable to the proposed curriculum. Topped MTEB leaderboard.",
    "one_line_summary": "Proposes latent attention pooling and a two-stage contrastive fine-tuning pipeline to convert Mistral-7B into the top-ranked generalist embedding model on MTEB, with key insight that removing causal masking during training helps."
  },
  {
    "title": "Scaling Laws for Dense Retrieval",
    "authors": "Yan Fang, Jingtao Zhan, Qingyao Ai, Jiaxin Mao, Weihang Su, Jia Chen, Yiqun Liu",
    "venue": "SIGIR 2024 — Best Paper Award",
    "url": "https://arxiv.org/abs/2403.18684",
    "why_important": "Best Paper at SIGIR 2024. Establishes precise power-law scaling relationships for dense retrieval as a function of model size and training data, enabling principled resource allocation. Directly informs the compute budget decisions for the proposed 3B/8B training.",
    "one_line_summary": "Demonstrates that dense retrieval accuracy follows predictable power-law scaling in model parameters and annotation volume, providing actionable guidance for training budget allocation."
  },
  {
    "title": "SPLARE: Learning Retrieval Models with Sparse Autoencoders",
    "authors": "Thibault Formal, Maxime Louis, Hervé Déjean, Stéphane Clinchant",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2603.13277",
    "why_important": "Proposes a fundamentally new approach to learned sparse retrieval using sparse autoencoders to decompose LLM representations into interpretable latent features instead of vocabulary-space projection. More language-agnostic than SPLADE. SPLARE-7B achieves top results on MMTEB multilingual and English retrieval.",
    "one_line_summary": "Replaces SPLADE's vocabulary-space projection with sparse autoencoders that decompose LLM representations into interpretable latent features, producing language-agnostic sparse representations that outperform SPLADE on multilingual retrieval."
  },
  {
    "title": "A Survey of Model Architectures in Information Retrieval",
    "authors": "Zhichao Xu, Fengran Mo, Zhiqi Huang, Crystina Zhang, Puxuan Yu, Bei Wang, Jimmy Lin, Vivek Srikumar",
    "venue": "TMLR 2025",
    "url": "https://arxiv.org/abs/2502.14822",
    "why_important": "Comprehensive survey (by the LACONIC first author) covering the full design space of sparse, dense, and hybrid retrieval architectures. Separates architecture from training methodology and traces the evolution from term-based to neural models. Essential reference for positioning the proposed work.",
    "one_line_summary": "An exhaustive survey tracing IR model architectures from traditional term-based methods through BERT bi-encoders to decoder-only LLMs, covering dense, sparse, hybrid, and generative retrieval paradigms."
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

You MUST output exactly 4 analyses in the JSON array. IMPORTANT: End your response with the JSON array.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "type": "user",
  "uuid": "c4692dc7-1ff0-46c4-b38a-2b4c3118876c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:20:38.271Z_

```json
{
  "parentUuid": "c4692dc7-1ff0-46c4-b38a-2b4c3118876c",
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
  "uuid": "55bee29e-b5d3-4f79-9299-a8be4affc383",
  "timestamp": "2026-05-30T06:20:38.271Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:20:38.271Z_

```json
{
  "parentUuid": "55bee29e-b5d3-4f79-9299-a8be4affc383",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8ed95795-4ba2-4fd6-abac-22dba556aa08",
  "timestamp": "2026-05-30T06:20:38.271Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
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
  "aiTitle": "Analyze hybrid retrieval architecture papers for AAAI 2026",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---

### Assistant

_source line 7 · 2026-05-30T06:20:40.934Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze each of the 4 papers by searching for and reading their content. I'll launch parallel searches for all 4 papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ed95795-4ba2-4fd6-abac-22dba556aa08",
  "isSidechain": false,
  "requestId": "req_011CbYGc6t3i2eXx3wV2d3uy",
  "type": "assistant",
  "uuid": "c743fa56-4b5e-405e-94f5-9bd435bc9344",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LxCa8qE5YYcoySkU5CJ2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1433,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 8 · 2026-05-30T06:20:41.820Z_

I'll research all 4 papers in parallel to gather their details efficiently.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c743fa56-4b5e-405e-94f5-9bd435bc9344",
  "isSidechain": false,
  "requestId": "req_011CbYGc6t3i2eXx3wV2d3uy",
  "type": "assistant",
  "uuid": "38617623-d124-48c2-ae42-aa1aa2c57672",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LxCa8qE5YYcoySkU5CJ2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1433,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 9 · 2026-05-30T06:20:50.072Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TDku7xHdLCcvngU3UJjpbe`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research NV-Embed paper",
  "prompt": "Research the paper \"NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models\" (arXiv 2405.17428, ICLR 2025 Spotlight). \n\n1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2405.17428\n2. Use WebFetch to read the full paper PDF or HTML version for method details: https://arxiv.org/html/2405.17428\n3. Search for OpenReview reviews of NV-Embed ICLR 2025 and try to fetch them.\n\nFor each source, extract:\n- The exact gap/problem they identified\n- Their key technical contributions (latent attention pooling, removing causal mask, two-stage training)\n- Method details: architecture, training procedure, loss functions\n- Results on MTEB\n- Any reviewer comments (praise and criticism)\n\nBe thorough - I need specific technical details about:\n1. How latent attention pooling works (architecture details)\n2. Why removing causal attention mask helps\n3. The two-stage contrastive instruction-tuning pipeline\n4. What backbone they used (Mistral-7B)\n\nReturn all findings in a structured format."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38617623-d124-48c2-ae42-aa1aa2c57672",
  "isSidechain": false,
  "requestId": "req_011CbYGc6t3i2eXx3wV2d3uy",
  "type": "assistant",
  "uuid": "a14ca538-47b9-4ee5-ad18-cd21b4f29164",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LxCa8qE5YYcoySkU5CJ2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1433,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 10 · 2026-05-30T06:20:54.897Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01G1jCu2LA5cauqDax7jH5wa`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Scaling Laws paper",
  "prompt": "Research the paper \"Scaling Laws for Dense Retrieval\" (arXiv 2403.18684, SIGIR 2024 Best Paper). \n\n1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2403.18684\n2. Use WebFetch to read the HTML version for method details: https://arxiv.org/html/2403.18684\n3. Search for any reviews or discussions about this paper being SIGIR 2024 Best Paper.\n\nExtract:\n- The exact gap/problem they identified\n- Their key contributions: what scaling laws they discovered, the functional form (power-law relationships)\n- Method details: how they derived scaling laws, what models/data they used, experimental setup\n- How model size and training data quantity affect dense retrieval performance\n- Practical implications for compute budget allocation\n- Any specific numbers: scaling exponents, model sizes tested, datasets used\n\nBe thorough with technical details about the scaling law formulation and how it can guide resource allocation decisions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a14ca538-47b9-4ee5-ad18-cd21b4f29164",
  "isSidechain": false,
  "requestId": "req_011CbYGc6t3i2eXx3wV2d3uy",
  "type": "assistant",
  "uuid": "869b226c-7597-4f42-8b7d-66e1f7f27980",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LxCa8qE5YYcoySkU5CJ2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1433,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 11 · 2026-05-30T06:20:58.800Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Us9WCqa67XjNKtkBXmU7V5`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research SPLARE paper",
  "prompt": "Research the paper \"SPLARE: Learning Retrieval Models with Sparse Autoencoders\" (arXiv 2603.13277, 2026).\n\n1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2603.13277\n2. Use WebFetch to read the HTML version for method details: https://arxiv.org/html/2603.13277\n3. Search the web for any discussion or reviews of SPLARE sparse autoencoder retrieval.\n\nExtract:\n- The exact gap/problem they identified with SPLADE-style vocabulary-space projection\n- Their key insight: using sparse autoencoders (SAEs) to decompose LLM representations into interpretable latent features\n- Method details: how the sparse autoencoder is trained, how it replaces vocabulary projection, architecture\n- Why this is more language-agnostic than SPLADE\n- Results: SPLARE-7B performance on MMTEB multilingual and English retrieval benchmarks\n- How this differs from traditional SPLADE approaches\n- Any limitations or open questions\n\nBe thorough with technical details about the SAE architecture and training procedure."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "869b226c-7597-4f42-8b7d-66e1f7f27980",
  "isSidechain": false,
  "requestId": "req_011CbYGc6t3i2eXx3wV2d3uy",
  "type": "assistant",
  "uuid": "939b2adf-d171-4efb-b169-c17cec6fd60d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LxCa8qE5YYcoySkU5CJ2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1433,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 12 · 2026-05-30T06:21:04.728Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PVRFRTRB29V3qa3QAS6H4s`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research IR Survey paper",
  "prompt": "Research the paper \"A Survey of Model Architectures in Information Retrieval\" (arXiv 2502.14822, TMLR 2025).\n\n1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2502.14822\n2. Use WebFetch to read the HTML version for details: https://arxiv.org/html/2502.14822\n3. Search for TMLR reviews or OpenReview page for this paper.\n\nExtract:\n- The scope and organization of the survey\n- How they categorize/taxonomize IR model architectures\n- Key distinctions they make (e.g., architecture vs training methodology)\n- Coverage of sparse, dense, hybrid, and generative retrieval\n- Their analysis of decoder-only LLMs for retrieval\n- Any identified open problems or future directions\n- How they discuss the sparse-dense complementarity\n- Whether they identify the gap of unified sparse+dense in decoder-only models\n- The connection to LACONIC (same first author)\n- Any reviewer comments\n\nFocus especially on: what architectural design space they define, how they compare sparse vs dense approaches, and what gaps they identify for future work."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "939b2adf-d171-4efb-b169-c17cec6fd60d",
  "isSidechain": false,
  "requestId": "req_011CbYGc6t3i2eXx3wV2d3uy",
  "type": "assistant",
  "uuid": "3d2e7619-c9a4-416b-a13d-a83433eb4aaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019LxCa8qE5YYcoySkU5CJ2j",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3983,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1433,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3983,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1433,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 3983,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3983
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "3d2e7619-c9a4-416b-a13d-a83433eb4aaa",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze hybrid retrieval architecture papers for AAAI 2026",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---

### Tool result

_source line 15 · 2026-05-30T06:23:38.828Z_

<details><summary>↩ Tool result · `toolu_01G1jCu2LA5cauqDax7jH5wa`</summary>

````text
I now have comprehensive information. Here is the thorough research summary:

---

## "Scaling Laws for Dense Retrieval" -- Full Technical Summary

**Paper:** arXiv 2403.18684 (v2, July 15, 2024)
**Authors:** Yan Fang, Jingtao Zhan, Qingyao Ai, Jiaxin Mao, Weihang Su, Jia Chen, Yiqun Liu (Tsinghua University / Renmin University of China)
**Venue:** SIGIR 2024 (47th International ACM SIGIR Conference, Washington DC, July 14-18, 2024) -- **Best Long Paper Award** (co-winner with "A Workbench for Autograding Retrieve/Generate Systems" by Laura Dietz)

---

### 1. Problem / Gap Identified

While scaling laws have been extensively studied for language modeling (e.g., Kaplan et al., Chinchilla), they remained **entirely unexplored for dense retrieval**. Two specific challenges blocked progress:

- **Discrete metrics problem:** Traditional ranking metrics like NDCG and MAP are discrete and cannot smoothly reflect fine-grained performance changes, making it impossible to fit continuous power-law curves.
- **Entangled factors:** Dense retrieval performance depends on multiple interrelated factors -- model size, annotation quantity, and annotation quality -- making it difficult to isolate individual effects and derive clean scaling relationships.

---

### 2. Key Methodological Innovation: Contrastive Entropy

The authors introduced **contrastive entropy** (equivalently, contrastive log-likelihood) as a continuous evaluation metric for dense retrieval:

```
CE = -log( exp(s(q_i, p_i^+; theta)) / (exp(s(q_i, p_i^+; theta)) + sum_j exp(s(q_i, p_j^-; theta))) )
```

where `s(q, p) = &lt;f(q; theta), f(p; theta)>` is the inner product between query and passage embeddings. This metric mirrors the contrastive training loss and measures the likelihood of retrieving a relevant document from a randomly sampled candidate set.

**Crucially**, the authors demonstrated a strong positive linear correlation between contrastive entropy and traditional ranking metrics (NDCG@10, MAP@10, Recall@1000), validating it as a faithful proxy. They also observed an **emergent ability threshold** around contrastive entropy of approximately **0.25**, below which ranking performance sharply improves -- analogous to emergent abilities in large language models.

---

### 3. Scaling Law Formulations

The authors derived three power-law relationships:

**Model size scaling (fixed data):**
```
L(N) = (A / N)^alpha + delta_N
```

**Data size scaling (fixed model):**
```
L(D) = (B / D)^beta + delta_D
```

**Joint model-data scaling:**
```
L(N, D) = [(A / N)^(alpha/beta) + B / D]^beta + delta
```

Where:
- `N` = number of non-embedding model parameters
- `D` = number of annotated query-passage training pairs
- `L` = contrastive entropy (lower is better)
- `A, B` = scaling coefficients
- `alpha, beta` = scaling exponents
- `delta` = irreducible loss term (accounts for incomplete annotations and subjective relevance)

---

### 4. Fitted Coefficients and R-squared Values

**MS MARCO Passage Ranking:**
| Scaling | A | alpha | delta | R-squared |
|---------|---|-------|-------|-----------|
| Model size | 3.22 x 10^4 | 0.53 | 0.04 | 0.991 |
| Data size | 3.49 x 10^3 | 1.05 | 0.05 | 0.954 |

**T2Ranking (Chinese):**
| Scaling | A | alpha | delta | R-squared |
|---------|---|-------|-------|-----------|
| Model size | 9.89 x 10^6 | 0.53 | 0.14 | 0.999 |
| Data size | 6.04 x 10^4 | 0.50 | 0.15 | 0.991 |

**Joint scaling (MS MARCO):** A ~ 3.6 x 10^4, B ~ 7.1 x 10^3, alpha ~ 0.56, beta ~ 1.31, delta ~ 0.03

Notable: The model size exponent alpha = 0.53 is **consistent across both datasets** (MS MARCO and T2Ranking), suggesting a universal scaling relationship for model size in dense retrieval. The data exponents differ more (1.05 vs 0.50), reflecting dataset-specific annotation characteristics.

---

### 5. Experimental Setup

**Models:** 24 BERT checkpoints from Google's original release, ranging from BERT-Tiny (0.5M non-embedding parameters) to BERT-Base (82M non-embedding parameters). For Chinese experiments, ERNIE model variants were used.

**Architecture:** Transformer-based dual encoders with a projection layer mapping to 768-dimensional embeddings. Relevance scored via inner product between query and passage embeddings.

**Datasets:**
- **MS MARCO Passage Ranking:** ~0.5M training queries, 8.8M passages (English web search)
- **T2Ranking:** 300k+ queries, 2M+ unique passages (Chinese web search)

**Training protocol:** Fixed at 10,000 steps, batch size 256, random negative sampling with 256 negatives per step, contrastive ranking loss.

---

### 6. Data Augmentation / Annotation Quality Analysis

Three synthetic annotation methods were tested alongside human annotations:

1. **Inverse Cloze Task (ICT):** Lowest quality -- uses random sentences from passages as pseudo-queries
2. **DocT5query:** Medium quality -- a supervised T5 model trained on human annotations to generate queries
3. **ChatGLM3:** Zero-shot LLM-based generation -- higher per-sample diversity

**Key finding:** All methods followed power-law scaling, but with different slopes (higher quality = steeper improvement curve). ChatGLM3-generated annotations **surpassed human annotations when scaled to 500k+ pairs**, despite lower per-sample quality. This suggests that for large-scale annotation, LLM-generated data can be more cost-effective than human labeling, leveraging the power of scaling.

---

### 7. Budget Allocation and Practical Implications

The authors formulated a total lifecycle cost model:

```
Z(N, D) = Z_data * D + Z_train * N + Z_infer * N
```

With cost parameters:
- **Z_data** = $0.60 per annotated query-passage pair
- **Z_train** = 3.22 x 10^-8 (training compute cost per parameter)
- **Z_infer** = 0.43 (inference compute cost per parameter)

**Critical insight -- inference cost dominance:** The ratio Z_infer / Z_train is enormous (~10^7), meaning inference costs dwarf training costs for dense retrieval (unlike language modeling where training dominates).

**Optimal allocation results for a $20,000 budget:**
- **Excluding inference costs:** Optimal model size is ~13 billion parameters, with budget favoring larger models and less data annotation
- **Including inference costs:** Optimal model shrinks dramatically to **million-scale parameters** because inference cost is proportional to model size and dominates the budget

This leads to a fundamentally different recommendation than LLM scaling: **for dense retrieval, practitioners should favor smaller, more efficient models** because retrieval requires encoding the entire corpus at inference time, making per-parameter inference cost the binding constraint.

---

### 8. The Irreducible Loss Term (delta)

The delta term captures a performance floor that cannot be overcome regardless of model or data scaling. It exists because:
- Some relevant passages are never annotated in the training data
- Relevance judgments are inherently subjective across annotators
- No finite model can achieve perfect retrieval from incomplete labels

Delta values were consistently small but non-zero: 0.03-0.05 for MS MARCO, 0.14-0.15 for T2Ranking (reflecting T2Ranking's noisier annotation process).

---

### 9. Predictive Power and Practical Use

The scaling laws enable:
1. **Performance extrapolation:** Train small models cheaply and predict large-model performance without actually training them
2. **Annotation budgeting:** Estimate how many annotations are needed to reach a target performance level
3. **Compute-optimal allocation:** Given a fixed budget, determine the best split between model size, training data, and inference resources
4. **Method comparison:** Different annotation strategies can be compared by their scaling coefficients rather than single-point evaluations

The joint scaling law predictions were validated against real experiments, with predictions "relatively close to real values" when extrapolating from smaller configurations.

---

### 10. SIGIR 2024 Best Paper Recognition

The paper was one of **two co-winners of the SIGIR 2024 Best Long Paper Award**. The other best paper awards at SIGIR 2024 included:
- **Runner-ups:** "Efficient Inverted Indexes for Approximate Retrieval over Learned Sparse Representations" (Bruch et al.) and "A Reproducibility Study of PLAID" (MacAvaney & Tonellotto)
- **Honorable mentions** included five additional papers on topics ranging from generative retrieval to fair re-ranking

---

### Summary of the Paper's Core Contribution

This paper establishes that dense retrieval follows precise, predictable power-law scaling with respect to both model size and training data quantity -- a finding that parallels the famous neural scaling laws for language models but reveals a critical difference: because dense retrieval requires encoding entire corpora at inference time, the inference cost (not training cost) becomes the dominant budget constraint. This inverts the conventional "bigger is better" wisdom from language modeling and suggests that for practical dense retrieval, compute budgets should favor smaller models with more training data, with the exact optimal tradeoff calculable from the discovered scaling laws.

---

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2403.18684)
- [arXiv HTML Full Paper](https://arxiv.org/html/2403.18684)
- [SIGIR 2024 Best Papers Page](https://sigir-2024.github.io/best_papers.html)
- [ACM Digital Library Entry](https://dl.acm.org/doi/abs/10.1145/3626772.3657743)
- [EmergentMind Analysis](https://www.emergentmind.com/papers/2403.18684)
- [Moonlight Literature Review](https://www.themoonlight.io/en/review/scaling-laws-for-dense-retrieval)
- [OpenReview Page](https://openreview.net/forum?id=pC695J6QQd)
- [SIGIR Best Paper Awards History](https://sigir.org/awards/best-paper-awards/)

agentId: a68e4306d3984469c (use SendMessage with to: 'a68e4306d3984469c' to continue this agent)
&lt;usage>total_tokens: 20405
tool_uses: 12
duration_ms: 163926&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "869b226c-7597-4f42-8b7d-66e1f7f27980",
  "isSidechain": false,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "type": "user",
  "uuid": "77509a11-c1b3-40af-b389-5e1db3b25044",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"Scaling Laws for Dense Retrieval\" (arXiv 2403.18684, SIGIR 2024 Best Paper). \n\n1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2403.18684\n2. Use WebFetch to read the HTML version for method details: https://arxiv.org/html/2403.18684\n3. Search for any reviews or discussions about this paper being SIGIR 2024 Best Paper.\n\nExtract:\n- The exact gap/problem they identified\n- Their key contributions: what scaling laws they discovered, the functional form (power-law relationships)\n- Method details: how they derived scaling laws, what models/data they used, experimental setup\n- How model size and training data quantity affect dense retrieval performance\n- Practical implications for compute budget allocation\n- Any specific numbers: scaling exponents, model sizes tested, datasets used\n\nBe thorough with technical details about the scaling law formulation and how it can guide resource allocation decisions.",
    "agentId": "a68e4306d3984469c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Here is the thorough research summary:\n\n---\n\n## \"Scaling Laws for Dense Retrieval\" -- Full Technical Summary\n\n**Paper:** arXiv 2403.18684 (v2, July 15, 2024)\n**Authors:** Yan Fang, Jingtao Zhan, Qingyao Ai, Jiaxin Mao, Weihang Su, Jia Chen, Yiqun Liu (Tsinghua University / Renmin University of China)\n**Venue:** SIGIR 2024 (47th International ACM SIGIR Conference, Washington DC, July 14-18, 2024) -- **Best Long Paper Award** (co-winner with \"A Workbench for Autograding Retrieve/Generate Systems\" by Laura Dietz)\n\n---\n\n### 1. Problem / Gap Identified\n\nWhile scaling laws have been extensively studied for language modeling (e.g., Kaplan et al., Chinchilla), they remained **entirely unexplored for dense retrieval**. Two specific challenges blocked progress:\n\n- **Discrete metrics problem:** Traditional ranking metrics like NDCG and MAP are discrete and cannot smoothly reflect fine-grained performance changes, making it impossible to fit continuous power-law curves.\n- **Entangled factors:** Dense retrieval performance depends on multiple interrelated factors -- model size, annotation quantity, and annotation quality -- making it difficult to isolate individual effects and derive clean scaling relationships.\n\n---\n\n### 2. Key Methodological Innovation: Contrastive Entropy\n\nThe authors introduced **contrastive entropy** (equivalently, contrastive log-likelihood) as a continuous evaluation metric for dense retrieval:\n\n```\nCE = -log( exp(s(q_i, p_i^+; theta)) / (exp(s(q_i, p_i^+; theta)) + sum_j exp(s(q_i, p_j^-; theta))) )\n```\n\nwhere `s(q, p) = &lt;f(q; theta), f(p; theta)>` is the inner product between query and passage embeddings. This metric mirrors the contrastive training loss and measures the likelihood of retrieving a relevant document from a randomly sampled candidate set.\n\n**Crucially**, the authors demonstrated a strong positive linear correlation between contrastive entropy and traditional ranking metrics (NDCG@10, MAP@10, Recall@1000), validating it as a faithful proxy. They also observed an **emergent ability threshold** around contrastive entropy of approximately **0.25**, below which ranking performance sharply improves -- analogous to emergent abilities in large language models.\n\n---\n\n### 3. Scaling Law Formulations\n\nThe authors derived three power-law relationships:\n\n**Model size scaling (fixed data):**\n```\nL(N) = (A / N)^alpha + delta_N\n```\n\n**Data size scaling (fixed model):**\n```\nL(D) = (B / D)^beta + delta_D\n```\n\n**Joint model-data scaling:**\n```\nL(N, D) = [(A / N)^(alpha/beta) + B / D]^beta + delta\n```\n\nWhere:\n- `N` = number of non-embedding model parameters\n- `D` = number of annotated query-passage training pairs\n- `L` = contrastive entropy (lower is better)\n- `A, B` = scaling coefficients\n- `alpha, beta` = scaling exponents\n- `delta` = irreducible loss term (accounts for incomplete annotations and subjective relevance)\n\n---\n\n### 4. Fitted Coefficients and R-squared Values\n\n**MS MARCO Passage Ranking:**\n| Scaling | A | alpha | delta | R-squared |\n|---------|---|-------|-------|-----------|\n| Model size | 3.22 x 10^4 | 0.53 | 0.04 | 0.991 |\n| Data size | 3.49 x 10^3 | 1.05 | 0.05 | 0.954 |\n\n**T2Ranking (Chinese):**\n| Scaling | A | alpha | delta | R-squared |\n|---------|---|-------|-------|-----------|\n| Model size | 9.89 x 10^6 | 0.53 | 0.14 | 0.999 |\n| Data size | 6.04 x 10^4 | 0.50 | 0.15 | 0.991 |\n\n**Joint scaling (MS MARCO):** A ~ 3.6 x 10^4, B ~ 7.1 x 10^3, alpha ~ 0.56, beta ~ 1.31, delta ~ 0.03\n\nNotable: The model size exponent alpha = 0.53 is **consistent across both datasets** (MS MARCO and T2Ranking), suggesting a universal scaling relationship for model size in dense retrieval. The data exponents differ more (1.05 vs 0.50), reflecting dataset-specific annotation characteristics.\n\n---\n\n### 5. Experimental Setup\n\n**Models:** 24 BERT checkpoints from Google's original release, ranging from BERT-Tiny (0.5M non-embedding parameters) to BERT-Base (82M non-embedding parameters). For Chinese experiments, ERNIE model variants were used.\n\n**Architecture:** Transformer-based dual encoders with a projection layer mapping to 768-dimensional embeddings. Relevance scored via inner product between query and passage embeddings.\n\n**Datasets:**\n- **MS MARCO Passage Ranking:** ~0.5M training queries, 8.8M passages (English web search)\n- **T2Ranking:** 300k+ queries, 2M+ unique passages (Chinese web search)\n\n**Training protocol:** Fixed at 10,000 steps, batch size 256, random negative sampling with 256 negatives per step, contrastive ranking loss.\n\n---\n\n### 6. Data Augmentation / Annotation Quality Analysis\n\nThree synthetic annotation methods were tested alongside human annotations:\n\n1. **Inverse Cloze Task (ICT):** Lowest quality -- uses random sentences from passages as pseudo-queries\n2. **DocT5query:** Medium quality -- a supervised T5 model trained on human annotations to generate queries\n3. **ChatGLM3:** Zero-shot LLM-based generation -- higher per-sample diversity\n\n**Key finding:** All methods followed power-law scaling, but with different slopes (higher quality = steeper improvement curve). ChatGLM3-generated annotations **surpassed human annotations when scaled to 500k+ pairs**, despite lower per-sample quality. This suggests that for large-scale annotation, LLM-generated data can be more cost-effective than human labeling, leveraging the power of scaling.\n\n---\n\n### 7. Budget Allocation and Practical Implications\n\nThe authors formulated a total lifecycle cost model:\n\n```\nZ(N, D) = Z_data * D + Z_train * N + Z_infer * N\n```\n\nWith cost parameters:\n- **Z_data** = $0.60 per annotated query-passage pair\n- **Z_train** = 3.22 x 10^-8 (training compute cost per parameter)\n- **Z_infer** = 0.43 (inference compute cost per parameter)\n\n**Critical insight -- inference cost dominance:** The ratio Z_infer / Z_train is enormous (~10^7), meaning inference costs dwarf training costs for dense retrieval (unlike language modeling where training dominates).\n\n**Optimal allocation results for a $20,000 budget:**\n- **Excluding inference costs:** Optimal model size is ~13 billion parameters, with budget favoring larger models and less data annotation\n- **Including inference costs:** Optimal model shrinks dramatically to **million-scale parameters** because inference cost is proportional to model size and dominates the budget\n\nThis leads to a fundamentally different recommendation than LLM scaling: **for dense retrieval, practitioners should favor smaller, more efficient models** because retrieval requires encoding the entire corpus at inference time, making per-parameter inference cost the binding constraint.\n\n---\n\n### 8. The Irreducible Loss Term (delta)\n\nThe delta term captures a performance floor that cannot be overcome regardless of model or data scaling. It exists because:\n- Some relevant passages are never annotated in the training data\n- Relevance judgments are inherently subjective across annotators\n- No finite model can achieve perfect retrieval from incomplete labels\n\nDelta values were consistently small but non-zero: 0.03-0.05 for MS MARCO, 0.14-0.15 for T2Ranking (reflecting T2Ranking's noisier annotation process).\n\n---\n\n### 9. Predictive Power and Practical Use\n\nThe scaling laws enable:\n1. **Performance extrapolation:** Train small models cheaply and predict large-model performance without actually training them\n2. **Annotation budgeting:** Estimate how many annotations are needed to reach a target performance level\n3. **Compute-optimal allocation:** Given a fixed budget, determine the best split between model size, training data, and inference resources\n4. **Method comparison:** Different annotation strategies can be compared by their scaling coefficients rather than single-point evaluations\n\nThe joint scaling law predictions were validated against real experiments, with predictions \"relatively close to real values\" when extrapolating from smaller configurations.\n\n---\n\n### 10. SIGIR 2024 Best Paper Recognition\n\nThe paper was one of **two co-winners of the SIGIR 2024 Best Long Paper Award**. The other best paper awards at SIGIR 2024 included:\n- **Runner-ups:** \"Efficient Inverted Indexes for Approximate Retrieval over Learned Sparse Representations\" (Bruch et al.) and \"A Reproducibility Study of PLAID\" (MacAvaney & Tonellotto)\n- **Honorable mentions** included five additional papers on topics ranging from generative retrieval to fair re-ranking\n\n---\n\n### Summary of the Paper's Core Contribution\n\nThis paper establishes that dense retrieval follows precise, predictable power-law scaling with respect to both model size and training data quantity -- a finding that parallels the famous neural scaling laws for language models but reveals a critical difference: because dense retrieval requires encoding entire corpora at inference time, the inference cost (not training cost) becomes the dominant budget constraint. This inverts the conventional \"bigger is better\" wisdom from language modeling and suggests that for practical dense retrieval, compute budgets should favor smaller models with more training data, with the exact optimal tradeoff calculable from the discovered scaling laws.\n\n---\n\nSources:\n- [arXiv Abstract Page](https://arxiv.org/abs/2403.18684)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2403.18684)\n- [SIGIR 2024 Best Papers Page](https://sigir-2024.github.io/best_papers.html)\n- [ACM Digital Library Entry](https://dl.acm.org/doi/abs/10.1145/3626772.3657743)\n- [EmergentMind Analysis](https://www.emergentmind.com/papers/2403.18684)\n- [Moonlight Literature Review](https://www.themoonlight.io/en/review/scaling-laws-for-dense-retrieval)\n- [OpenReview Page](https://openreview.net/forum?id=pC695J6QQd)\n- [SIGIR Best Paper Awards History](https://sigir.org/awards/best-paper-awards/)"
      }
    ],
    "totalDurationMs": 163926,
    "totalTokens": 20405,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 16805,
      "output_tokens": 2686,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2686,
          "cache_read_input_tokens": 16805,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 913,
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
  "sourceToolAssistantUUID": "869b226c-7597-4f42-8b7d-66e1f7f27980",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 16 · 2026-05-30T06:23:43.945Z_

<details><summary>↩ Tool result · `toolu_01TDku7xHdLCcvngU3UJjpbe`</summary>

```text
I was able to extract the reviewer comments from the OpenReview API. Now I have comprehensive data from all sources. Here is the structured synthesis:

---

## NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models

**Paper:** arXiv 2405.17428 | **Venue:** ICLR 2025 (Spotlight)
**Authors:** Chankyu Lee, Rajarshi Roy, Mengyao Xu, Jonathan Raiman, Mohammad Shoeybi, Bryan Catanzaro, Wei Ping (NVIDIA)
**Submitted:** May 27, 2024 | **Latest revision (v3):** February 25, 2025

---

### 1. Problem / Gap Identified

Decoder-only LLMs are increasingly used as backbone encoders for text embedding, but existing approaches suffer from three interrelated shortcomings:

- **Pooling limitations:** Mean pooling dilutes important token information by simple averaging; EOS-token pooling suffers from "recency bias" (over-relying on the last token's hidden state). Neither extracts a maximally informative sentence representation from the full hidden-state sequence.
- **Causal attention bottleneck:** Decoder-only LLMs use a causal (unidirectional) attention mask that prevents each token from attending to future tokens. While necessary for autoregressive generation, this limits representation power for embedding tasks where the full input is available at inference time.
- **Task conflict in multi-task training:** Mixing retrieval datasets (which benefit from in-batch negatives and hard negatives) with non-retrieval datasets (classification, clustering, STS -- where in-batch negatives are harmful due to few-class label collisions) in a single training stage degrades overall performance.

---

### 2. Key Technical Contributions

#### A. Latent Attention Pooling

**Architecture:**
- A cross-attention layer is inserted on top of the final LLM hidden states.
- A **trainable latent array** `K = V` of shape `R^(r x d)` is introduced, where `r = 512` (number of latent vectors) and `d` is the hidden dimension of the LLM.
- The LLM's final-layer hidden states `H` (shape `l x d`, where `l` = sequence length) serve as the **query** `Q`.
- The attention computation is: `O = softmax(Q K^T / sqrt(d_k)) V`, using **8 multi-head attention heads**.
- The output `O` (shape `l x d`) is then passed through an **MLP with GELU activation**, followed by **mean pooling** over the sequence dimension to produce the final embedding vector.

**Intuition:** This acts as a form of dictionary learning -- the trainable latent array learns a set of "concept prototypes," and each token's hidden state attends to these prototypes to extract task-relevant features before averaging. This mitigates information dilution from plain mean pooling.

**Ablation results (NV-Embed-v2, bidirectional attention, Table 3):**

| Pooling Method | Retrieval | Overall MTEB |
|---|---|---|
| Mean pooling | 61.81 | 71.71 |
| EOS token | 62.13 | 71.63 |
| Self-attention | 69.10 (single metric) | -- |
| **Latent attention** | **62.65** | **72.31** |

The gain is +0.60 MTEB points over mean pooling for v2. For v1 (causal attention), the gain was larger: latent attention 64.18 vs mean 63.39.

#### B. Removing the Causal Attention Mask

During contrastive training (not during the original LLM pretraining), the causal mask in every decoder block is removed, enabling **bidirectional (full) attention**. Each token can attend to all other tokens in the sequence.

**Why this helps:** For embedding tasks, the entire input text is available at once -- there is no autoregressive generation. The causal mask artificially restricts information flow, particularly hurting early tokens that cannot see later context. Bidirectional attention allows every token to incorporate full-sequence context, producing richer representations.

**Ablation results (Table 2, first stage, latent attention pooling):**

| Attention | Retrieval | Avg MTEB |
|---|---|---|
| Causal | 57.65 | 63.39 |
| **Bidirectional** | **59.00** | **64.18** |

Bidirectional attention consistently outperforms causal across **all pooling types and all 56 MTEB tasks**.

#### C. Two-Stage Contrastive Instruction-Tuning

**Stage 1 -- Retrieval-focused training:**
- **Data:** 15-16 retrieval datasets: MS MARCO, HotpotQA, Natural Questions, PAQ, Stack Exchange, NLI, SQuAD, ArguAna, BioASQ, FiQA, FEVER, HoVer, SciFact, NFCorpus, MIRACL, Mr.TyDi.
- **Training signals:** In-batch negatives + curated hard negatives.
- **Hard-negative mining:** Uses a "positive-aware" technique with E5-Mistral-7B-instruct as teacher model. Threshold: `max_negative_score < pos_score * 0.95` (95% TopKPercPos).
- **Instruction format:** `"Instruct: {task_definition}\nQuery: {q}"`

**Stage 2 -- Blended multi-task training:**
- **Data:** All Stage-1 retrieval data PLUS non-retrieval datasets:
  - Classification (10 datasets): AmazonReviews, Banking77, Emotion, IMDB, MTOP, ToxicConversations, etc.
  - Clustering (8 datasets): raw_arxiv, raw_biorxiv, raw_medrxiv, TwentyNewsgroups, Reddit, StackExchange, etc.
  - STS: STS12, STS22, STS-Benchmark
- **Key design choice:** In-batch negatives are **disabled** for non-retrieval tasks (because classification/clustering tasks have few class labels, causing in-batch negative collisions that corrupt training signal).
- **Synthetic data:** 120,000 synthetic examples across 60,000 synthetic tasks generated by Mixtral-8x22B-Instruct (40k each of short-long, long-short, short-short pairs).
- **Multi-class labeling:** Uses an "example-based" approach -- randomly samples an example from the ground-truth class as the positive, and examples from other classes as negatives (vs. using class labels as text). This was critical: example-based = 72.31 MTEB vs. label-based = 70.82.

**Why two stages instead of one:**
Retrieval is the most difficult task and benefits most from in-batch negatives. Training retrieval first ensures strong retrieval capability, then Stage 2 blends in other tasks without the in-batch negative conflict. Empirical validation (Table 4):

| Strategy | Overall MTEB |
|---|---|
| Single-stage (in-batch ON) | 70.83 |
| Single-stage (in-batch OFF) | 71.94 |
| Reversed two-stage (non-retrieval first) | 71.85 |
| **Proposed two-stage (retrieval first)** | **72.31** |

**Loss function:** Contrastive loss (InfoNCE-style) with in-batch negatives and hard negatives for retrieval; contrastive loss without in-batch negatives for non-retrieval tasks.

---

### 3. Backbone Model

- **Base:** Mistral-7B (Jiang et al., 2023) -- the standard 7B parameter decoder-only model.
- **Modifications during training:** Causal mask removed; latent attention layer (512 latents, 8 heads) + MLP added on top.
- **Not dependent on other embedding models** for initialization -- trained from scratch on publicly available data (though E5-Mistral is used as a teacher for hard-negative mining only).
- **Model compression** explored in Appendix A: SparseGPT pruning (8B -> 3.5B params), knowledge distillation (MSE loss on intermediate states), INT8/E4M3/E5M2 quantization with minimal degradation.

---

### 4. Results on MTEB

**Overall leaderboard (56 tasks, Table 1):**

| Model | Overall | Retrieval | Reranking | Clustering | PairClass | Classification | STS |
|---|---|---|---|---|---|---|---|
| **NV-Embed-v2** | **72.31** | **62.65** | 60.65 | **58.46** | **88.67** | **90.37** | 84.31 |
| SFR-Embedding-2R | 70.31 | 60.18 | 60.14 | 56.17 | 88.07 | 89.05 | 81.26 |
| bge-en-icl | 71.24 | -- | -- | -- | -- | -- | -- |
| E5-Mistral-7B | 66.63 | 56.90 | 60.21 | 50.26 | 88.34 | 78.47 | 84.66 |
| GritLM-7B | 66.76 | 57.41 | 60.49 | 50.61 | 87.16 | 79.46 | 83.35 |

- NV-Embed-v1 achieved #1 on MTEB as of May 24, 2024.
- NV-Embed-v2 reclaimed and maintained #1 since August 30, 2024.
- Also achieved highest scores on AIR Benchmark Long Doc section (74.78) and second-highest on QA section.

**Ablation progression (Table 4, cumulative improvements):**

| Configuration | MTEB |
|---|---|
| Baseline (no improvements) | 70.73 |
| + Hard-negative mining | 71.83 |
| + Additional datasets | 72.07 |
| + Synthetic data + example-based labeling | **72.31** |

---

### 5. OpenReview Reviews (ICLR 2025)

**Decision:** Accept (Spotlight) -- unanimous positive reviews.

**Reviewer wm7z (Rating: 8/10, Confidence: 3/5):**
- **Praise:** Strong empirical gains with thorough ablations across a wide range of settings. Documents top-performing system on the competitive MTEB benchmark.
- **Criticism:** "Core methodological techniques are well known, only more effectively performed." Latent attention shows small average performance effect in Table 2. The hard-negative mining pipeline may contribute more than the architectural novelty.
- **Question:** How is the optimizer handled between training stages?

**Reviewer 9J2v (Rating: 6/10, Confidence: 4/5):**
- **Praise:** Out-of-domain testing on AIR Benchmark is valuable. Extensive ablation studies validate each module.
- **Criticism:** "Complexity of entire training process... involves too many operations, making it difficult to reproduce."

**Reviewer rURm (Rating: 8/10, Confidence: 3/5):**
- **Praise:** Strong empirical results with detailed ablations. Clear presentation.
- **Criticism:** Limited novelty (decoder-only embedding models are not new, cf. GritLM). Latent attention shows modest gains over mean pooling. "Limited explanation or intuition behind why two-stage training works."
- **Questions:** What happens with reversed training order? (Authors later added this ablation: proposed order 72.31 vs reversed 71.85.)

**Reviewer MUEH (Rating: 8/10, Confidence: 5/5):**
- **Praise:** Strong MTEB results with thorough ablations. Transparent data curation process. Good summary of SOTA system.
- **Criticism:** "Does not seem to be single innovative algorithm piece." Technical depth limited despite proven effectiveness.
- **Question:** More v1 vs v2 specific ablations?

**Meta-review:** Unanimous positive assessment. Reviewers acknowledged "strong empirical results and ablations" with high community value. The main caveat: "technical novelty of individual ingredients may be somewhat limited." However, the combination of techniques, thorough ablations, and state-of-the-art results were deemed sufficient for acceptance as a Spotlight paper.

**Author responses:** Provided reversed training order ablation (72.31 vs 71.85), contextualized latent attention gains (+0.60 MTEB points for v2), clarified optimizer specifications, and released model weights with reproduction instructions.

---

### Sources

- [arXiv Abstract Page](https://arxiv.org/abs/2405.17428)
- [arXiv Full HTML Paper](https://arxiv.org/html/2405.17428)
- [OpenReview Forum](https://openreview.net/forum?id=lgsyLSsDRe)
- [ICLR 2025 Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c4bf73386022473a652a18941e9ea6f8-Abstract-Conference.html)
- [Liner Quick Review](https://liner.com/review/nvembed-improved-techniques-for-training-llms-as-generalist-embedding-models)
- [Synced Review (NVIDIA summary)](https://syncedreview.com/2024/05/29/nvidias-nv-embed-superior-performance-in-embedding-tasks-without-proprietary-data/)

agentId: a82555f92a4b10ed0 (use SendMessage with to: 'a82555f92a4b10ed0' to continue this agent)
&lt;usage>total_tokens: 21463
tool_uses: 10
duration_ms: 173865&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a14ca538-47b9-4ee5-ad18-cd21b4f29164",
  "isSidechain": false,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "type": "user",
  "uuid": "fe41473a-561c-48ec-a55d-28433ee90afe",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models\" (arXiv 2405.17428, ICLR 2025 Spotlight). \n\n1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2405.17428\n2. Use WebFetch to read the full paper PDF or HTML version for method details: https://arxiv.org/html/2405.17428\n3. Search for OpenReview reviews of NV-Embed ICLR 2025 and try to fetch them.\n\nFor each source, extract:\n- The exact gap/problem they identified\n- Their key technical contributions (latent attention pooling, removing causal mask, two-stage training)\n- Method details: architecture, training procedure, loss functions\n- Results on MTEB\n- Any reviewer comments (praise and criticism)\n\nBe thorough - I need specific technical details about:\n1. How latent attention pooling works (architecture details)\n2. Why removing causal attention mask helps\n3. The two-stage contrastive instruction-tuning pipeline\n4. What backbone they used (Mistral-7B)\n\nReturn all findings in a structured format.",
    "agentId": "a82555f92a4b10ed0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I was able to extract the reviewer comments from the OpenReview API. Now I have comprehensive data from all sources. Here is the structured synthesis:\n\n---\n\n## NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models\n\n**Paper:** arXiv 2405.17428 | **Venue:** ICLR 2025 (Spotlight)\n**Authors:** Chankyu Lee, Rajarshi Roy, Mengyao Xu, Jonathan Raiman, Mohammad Shoeybi, Bryan Catanzaro, Wei Ping (NVIDIA)\n**Submitted:** May 27, 2024 | **Latest revision (v3):** February 25, 2025\n\n---\n\n### 1. Problem / Gap Identified\n\nDecoder-only LLMs are increasingly used as backbone encoders for text embedding, but existing approaches suffer from three interrelated shortcomings:\n\n- **Pooling limitations:** Mean pooling dilutes important token information by simple averaging; EOS-token pooling suffers from \"recency bias\" (over-relying on the last token's hidden state). Neither extracts a maximally informative sentence representation from the full hidden-state sequence.\n- **Causal attention bottleneck:** Decoder-only LLMs use a causal (unidirectional) attention mask that prevents each token from attending to future tokens. While necessary for autoregressive generation, this limits representation power for embedding tasks where the full input is available at inference time.\n- **Task conflict in multi-task training:** Mixing retrieval datasets (which benefit from in-batch negatives and hard negatives) with non-retrieval datasets (classification, clustering, STS -- where in-batch negatives are harmful due to few-class label collisions) in a single training stage degrades overall performance.\n\n---\n\n### 2. Key Technical Contributions\n\n#### A. Latent Attention Pooling\n\n**Architecture:**\n- A cross-attention layer is inserted on top of the final LLM hidden states.\n- A **trainable latent array** `K = V` of shape `R^(r x d)` is introduced, where `r = 512` (number of latent vectors) and `d` is the hidden dimension of the LLM.\n- The LLM's final-layer hidden states `H` (shape `l x d`, where `l` = sequence length) serve as the **query** `Q`.\n- The attention computation is: `O = softmax(Q K^T / sqrt(d_k)) V`, using **8 multi-head attention heads**.\n- The output `O` (shape `l x d`) is then passed through an **MLP with GELU activation**, followed by **mean pooling** over the sequence dimension to produce the final embedding vector.\n\n**Intuition:** This acts as a form of dictionary learning -- the trainable latent array learns a set of \"concept prototypes,\" and each token's hidden state attends to these prototypes to extract task-relevant features before averaging. This mitigates information dilution from plain mean pooling.\n\n**Ablation results (NV-Embed-v2, bidirectional attention, Table 3):**\n\n| Pooling Method | Retrieval | Overall MTEB |\n|---|---|---|\n| Mean pooling | 61.81 | 71.71 |\n| EOS token | 62.13 | 71.63 |\n| Self-attention | 69.10 (single metric) | -- |\n| **Latent attention** | **62.65** | **72.31** |\n\nThe gain is +0.60 MTEB points over mean pooling for v2. For v1 (causal attention), the gain was larger: latent attention 64.18 vs mean 63.39.\n\n#### B. Removing the Causal Attention Mask\n\nDuring contrastive training (not during the original LLM pretraining), the causal mask in every decoder block is removed, enabling **bidirectional (full) attention**. Each token can attend to all other tokens in the sequence.\n\n**Why this helps:** For embedding tasks, the entire input text is available at once -- there is no autoregressive generation. The causal mask artificially restricts information flow, particularly hurting early tokens that cannot see later context. Bidirectional attention allows every token to incorporate full-sequence context, producing richer representations.\n\n**Ablation results (Table 2, first stage, latent attention pooling):**\n\n| Attention | Retrieval | Avg MTEB |\n|---|---|---|\n| Causal | 57.65 | 63.39 |\n| **Bidirectional** | **59.00** | **64.18** |\n\nBidirectional attention consistently outperforms causal across **all pooling types and all 56 MTEB tasks**.\n\n#### C. Two-Stage Contrastive Instruction-Tuning\n\n**Stage 1 -- Retrieval-focused training:**\n- **Data:** 15-16 retrieval datasets: MS MARCO, HotpotQA, Natural Questions, PAQ, Stack Exchange, NLI, SQuAD, ArguAna, BioASQ, FiQA, FEVER, HoVer, SciFact, NFCorpus, MIRACL, Mr.TyDi.\n- **Training signals:** In-batch negatives + curated hard negatives.\n- **Hard-negative mining:** Uses a \"positive-aware\" technique with E5-Mistral-7B-instruct as teacher model. Threshold: `max_negative_score < pos_score * 0.95` (95% TopKPercPos).\n- **Instruction format:** `\"Instruct: {task_definition}\\nQuery: {q}\"`\n\n**Stage 2 -- Blended multi-task training:**\n- **Data:** All Stage-1 retrieval data PLUS non-retrieval datasets:\n  - Classification (10 datasets): AmazonReviews, Banking77, Emotion, IMDB, MTOP, ToxicConversations, etc.\n  - Clustering (8 datasets): raw_arxiv, raw_biorxiv, raw_medrxiv, TwentyNewsgroups, Reddit, StackExchange, etc.\n  - STS: STS12, STS22, STS-Benchmark\n- **Key design choice:** In-batch negatives are **disabled** for non-retrieval tasks (because classification/clustering tasks have few class labels, causing in-batch negative collisions that corrupt training signal).\n- **Synthetic data:** 120,000 synthetic examples across 60,000 synthetic tasks generated by Mixtral-8x22B-Instruct (40k each of short-long, long-short, short-short pairs).\n- **Multi-class labeling:** Uses an \"example-based\" approach -- randomly samples an example from the ground-truth class as the positive, and examples from other classes as negatives (vs. using class labels as text). This was critical: example-based = 72.31 MTEB vs. label-based = 70.82.\n\n**Why two stages instead of one:**\nRetrieval is the most difficult task and benefits most from in-batch negatives. Training retrieval first ensures strong retrieval capability, then Stage 2 blends in other tasks without the in-batch negative conflict. Empirical validation (Table 4):\n\n| Strategy | Overall MTEB |\n|---|---|\n| Single-stage (in-batch ON) | 70.83 |\n| Single-stage (in-batch OFF) | 71.94 |\n| Reversed two-stage (non-retrieval first) | 71.85 |\n| **Proposed two-stage (retrieval first)** | **72.31** |\n\n**Loss function:** Contrastive loss (InfoNCE-style) with in-batch negatives and hard negatives for retrieval; contrastive loss without in-batch negatives for non-retrieval tasks.\n\n---\n\n### 3. Backbone Model\n\n- **Base:** Mistral-7B (Jiang et al., 2023) -- the standard 7B parameter decoder-only model.\n- **Modifications during training:** Causal mask removed; latent attention layer (512 latents, 8 heads) + MLP added on top.\n- **Not dependent on other embedding models** for initialization -- trained from scratch on publicly available data (though E5-Mistral is used as a teacher for hard-negative mining only).\n- **Model compression** explored in Appendix A: SparseGPT pruning (8B -> 3.5B params), knowledge distillation (MSE loss on intermediate states), INT8/E4M3/E5M2 quantization with minimal degradation.\n\n---\n\n### 4. Results on MTEB\n\n**Overall leaderboard (56 tasks, Table 1):**\n\n| Model | Overall | Retrieval | Reranking | Clustering | PairClass | Classification | STS |\n|---|---|---|---|---|---|---|---|\n| **NV-Embed-v2** | **72.31** | **62.65** | 60.65 | **58.46** | **88.67** | **90.37** | 84.31 |\n| SFR-Embedding-2R | 70.31 | 60.18 | 60.14 | 56.17 | 88.07 | 89.05 | 81.26 |\n| bge-en-icl | 71.24 | -- | -- | -- | -- | -- | -- |\n| E5-Mistral-7B | 66.63 | 56.90 | 60.21 | 50.26 | 88.34 | 78.47 | 84.66 |\n| GritLM-7B | 66.76 | 57.41 | 60.49 | 50.61 | 87.16 | 79.46 | 83.35 |\n\n- NV-Embed-v1 achieved #1 on MTEB as of May 24, 2024.\n- NV-Embed-v2 reclaimed and maintained #1 since August 30, 2024.\n- Also achieved highest scores on AIR Benchmark Long Doc section (74.78) and second-highest on QA section.\n\n**Ablation progression (Table 4, cumulative improvements):**\n\n| Configuration | MTEB |\n|---|---|\n| Baseline (no improvements) | 70.73 |\n| + Hard-negative mining | 71.83 |\n| + Additional datasets | 72.07 |\n| + Synthetic data + example-based labeling | **72.31** |\n\n---\n\n### 5. OpenReview Reviews (ICLR 2025)\n\n**Decision:** Accept (Spotlight) -- unanimous positive reviews.\n\n**Reviewer wm7z (Rating: 8/10, Confidence: 3/5):**\n- **Praise:** Strong empirical gains with thorough ablations across a wide range of settings. Documents top-performing system on the competitive MTEB benchmark.\n- **Criticism:** \"Core methodological techniques are well known, only more effectively performed.\" Latent attention shows small average performance effect in Table 2. The hard-negative mining pipeline may contribute more than the architectural novelty.\n- **Question:** How is the optimizer handled between training stages?\n\n**Reviewer 9J2v (Rating: 6/10, Confidence: 4/5):**\n- **Praise:** Out-of-domain testing on AIR Benchmark is valuable. Extensive ablation studies validate each module.\n- **Criticism:** \"Complexity of entire training process... involves too many operations, making it difficult to reproduce.\"\n\n**Reviewer rURm (Rating: 8/10, Confidence: 3/5):**\n- **Praise:** Strong empirical results with detailed ablations. Clear presentation.\n- **Criticism:** Limited novelty (decoder-only embedding models are not new, cf. GritLM). Latent attention shows modest gains over mean pooling. \"Limited explanation or intuition behind why two-stage training works.\"\n- **Questions:** What happens with reversed training order? (Authors later added this ablation: proposed order 72.31 vs reversed 71.85.)\n\n**Reviewer MUEH (Rating: 8/10, Confidence: 5/5):**\n- **Praise:** Strong MTEB results with thorough ablations. Transparent data curation process. Good summary of SOTA system.\n- **Criticism:** \"Does not seem to be single innovative algorithm piece.\" Technical depth limited despite proven effectiveness.\n- **Question:** More v1 vs v2 specific ablations?\n\n**Meta-review:** Unanimous positive assessment. Reviewers acknowledged \"strong empirical results and ablations\" with high community value. The main caveat: \"technical novelty of individual ingredients may be somewhat limited.\" However, the combination of techniques, thorough ablations, and state-of-the-art results were deemed sufficient for acceptance as a Spotlight paper.\n\n**Author responses:** Provided reversed training order ablation (72.31 vs 71.85), contextualized latent attention gains (+0.60 MTEB points for v2), clarified optimizer specifications, and released model weights with reproduction instructions.\n\n---\n\n### Sources\n\n- [arXiv Abstract Page](https://arxiv.org/abs/2405.17428)\n- [arXiv Full HTML Paper](https://arxiv.org/html/2405.17428)\n- [OpenReview Forum](https://openreview.net/forum?id=lgsyLSsDRe)\n- [ICLR 2025 Proceedings](https://proceedings.iclr.cc/paper_files/paper/2025/hash/c4bf73386022473a652a18941e9ea6f8-Abstract-Conference.html)\n- [Liner Quick Review](https://liner.com/review/nvembed-improved-techniques-for-training-llms-as-generalist-embedding-models)\n- [Synced Review (NVIDIA summary)](https://syncedreview.com/2024/05/29/nvidias-nv-embed-superior-performance-in-embedding-tasks-without-proprietary-data/)"
      }
    ],
    "totalDurationMs": 173865,
    "totalTokens": 21463,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1036,
      "cache_creation_input_tokens": 992,
      "cache_read_input_tokens": 16086,
      "output_tokens": 3349,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 992
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1036,
          "output_tokens": 3349,
          "cache_read_input_tokens": 16086,
          "cache_creation_input_tokens": 992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 992,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "a14ca538-47b9-4ee5-ad18-cd21b4f29164",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
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
  "leafUuid": "fe41473a-561c-48ec-a55d-28433ee90afe",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze hybrid retrieval architecture papers for AAAI 2026",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---

### Tool result

_source line 19 · 2026-05-30T06:24:02.150Z_

<details><summary>↩ Tool result · `toolu_01Us9WCqa67XjNKtkBXmU7V5`</summary>

````text
Now I have comprehensive information. Here is the full research synthesis:

---

## SPLARE: Learning Retrieval Models with Sparse Autoencoders (arXiv 2603.13277)

**Authors:** Thibault Formal, Maxime Louis, Herve Dejean, Stephane Clinchant (Naver Labs Europe)
**Venue:** ICLR 2026 | Submitted October 8, 2025; arXiv February 27, 2026

---

### 1. The Problem with SPLADE-Style Vocabulary-Space Projection

SPLADE and other Learned Sparse Retrieval (LSR) methods project LLM representations onto the **vocabulary space** -- essentially using the language model head to produce a sparse vector where each dimension corresponds to a token in the model's wordpiece vocabulary. The authors identify several fundamental limitations:

- **Fixed vocabulary constraint:** LSR methods are "inherently constrained by the fixed vocabulary of their underlying backbone." The vocabulary was designed for tokenization, not for representing semantic concepts.
- **Tokenization redundancy:** Multiple vocabulary tokens encode the same semantic concept (e.g., "Indian" and "indian" as separate dimensions), wasting representational capacity.
- **Language specificity:** Subword tokenizers are heavily biased toward the languages dominant in pretraining data. Low-resource languages get poor coverage, leading to fragmented and semantically incoherent sparse representations.
- **Multilingual failure:** At the time of submission, **no sparse retrieval model appeared on the MTEB Multilingual v2 leaderboard** -- a stark indicator that vocabulary-based LSR had fundamentally failed to generalize across languages.
- **Fixed dimensionality:** The vocabulary size is locked at whatever the backbone model uses (e.g., 128k for Llama-3.1), with no mechanism to scale representation capacity.

---

### 2. Key Insight: SAEs Decompose LLM Representations into Language-Agnostic Semantic Features

The central insight draws from the **mechanistic interpretability** literature. Sparse autoencoders (SAEs), when trained on LLM residual stream activations, decompose dense hidden states into interpretable latent features that exhibit several properties ideal for retrieval:

- **Monosemanticity:** Most SAE features correspond to a single, coherent concept (e.g., "casualties in conflict," "references to India"), unlike individual neurons which are polysemantic.
- **Language-agnosticism:** SAE features activate consistently for the same semantic content regardless of input language. A feature for "historical/cultural contexts" fires on Tamil, English, and German text alike.
- **Scalability:** SAE width (number of latent features) can be scaled independently of the LLM vocabulary -- from 16k to over 1M features -- providing a tunable knob for representational capacity.

The authors' key realization: if SAEs already produce sparse, interpretable, language-agnostic features from LLM hidden states, they are a **natural replacement** for vocabulary projection in sparse retrieval.

---

### 3. Method Details: The SPLARE Architecture

#### 3.1 SAE Mathematical Foundation

A standard sparse autoencoder maps an LLM hidden state **x** in R^d to a high-dimensional sparse latent **z** in R^|W| (where |W| >> d):

```
z = f(W_enc * x + b_enc)       [encoder]
x_hat = W_dec * z + b_dec       [decoder/reconstruction]
```

The SAE is trained to minimize reconstruction loss ||x_hat - x||^2 with sparsity induced through the activation function f (ReLU, Top-K, or JumpReLU) and L1 regularization. The authors use **pre-trained, publicly available SAEs** (Llama Scope for Llama-3.1-8B with 131k features; Gemma Scope for Gemma-2-2B with 65k features).

#### 3.2 SPLARE Pipeline (Replacing Vocabulary Projection)

The pipeline mirrors SPLADE but swaps out the LM head for an SAE encoder:

1. **Forward pass to intermediate layer:** Process input tokens through the LLM backbone, but only up to an intermediate layer (optimally ~2/3 depth -- layer 20-22 for Llama-3.1-8B's 32 layers, layer 16-17 for Gemma-2-2B's 26 layers). This is a computational advantage since SPLADE must run the full model.

2. **SAE encoding:** Apply the frozen SAE encoder to each token's hidden state, producing sparse latent logits (v_i1, v_i2, ..., v_i|W|) for each token i.

3. **SPLADE-style pooling ("SPLADE-pool"):** Aggregate token-level features into a single document/query vector using max-pooling with log-saturation:
   ```
   u_j = max_{i=1...n} log(1 + ReLU(v_ij)),  for j in W (latent feature space)
   ```
   This is identical to SPLADE's pooling, but over the SAE latent space W instead of vocabulary V.

4. **Scoring:** Standard sparse dot product: s(q, d) = &lt;u_q, u_d>

#### 3.3 Training Procedure

**What is trained vs. frozen:**
- **SAE:** Completely frozen (preserves interpretability and language-agnostic properties)
- **LLM backbone:** Fine-tuned with **LoRA** (rank=64) to adapt hidden states for retrieval
- **Bidirectional attention:** Enabled across all LLM layers (critical for position-wise pooling)

**Pre-training step:** Masked Language Modeling (20% token masking) on MS MARCO for 10k steps (~5 hours). This adapts the LLM to bidirectional attention before retrieval fine-tuning.

**Loss function -- distillation-based:**
```
L = L_KL + lambda_q * L_FLOPS^q + lambda_d * L_FLOPS^d
```

Where L_KL is the KL divergence between a cross-encoder teacher's relevance distribution and the student's:
```
p_hat_i = exp(s(q, d_i)/tau) / sum_j exp(s(q, d_j)/tau)   [student, temperature-scaled]
p_i = exp(s_i) / sum_j exp(s_j)                             [teacher]
```

The FLOPS regularizer controls sparsity (lambda_q = lambda_d = 0.0001). Distillation was chosen over contrastive learning because it better handles false negatives.

**Key hyperparameters:**
- Learning rate: 5e-5
- Batch size: 128
- Temperature tau: 80 (Llama Scope), 50 (Gemma Scope) -- selected via grid search over {1, 10, 20, 40, 50, 80, 100}; critically important and SAE-suite-dependent
- Negatives per query: 8
- Epochs: 1
- Max sequence length: 128 (English), 512 (multilingual)

**Inference-time sparsity control -- Top-K pooling:**
After training, a Top-K selection is applied: keep only the top k=40 features for queries and k=400 for documents. This decouples sparsity from training, allowing a single trained model to operate at multiple sparsity levels without retraining.

**Training data:**
- English setting: MS MARCO with DeBERTa-v3 reranker distillation targets
- Multilingual setting: BGE multilingual training set (1.3M queries from MS MARCO, NQ, HotpotQA, Chinese retrieval datasets, MIRACL, Mr.TyDi) with BGE-reranker-v2-m3 as teacher

---

### 4. Why SPLARE Is More Language-Agnostic Than SPLADE

Several reinforcing factors:

1. **SAE features transcend tokenization:** SPLADE's dimensions are vocabulary tokens -- inherently language-specific surface forms. SPLARE's dimensions are learned semantic concepts that activate identically across languages.

2. **Empirical evidence from interpretability research:** The authors cite work showing SAE features on residual streams are "largely invariant across languages" -- the same feature fires for "casualties" whether the input is in Tamil, English, or Yoruba.

3. **No tokenization artifacts:** SPLADE wastes capacity on redundant tokens ("Indian" vs. "indian") and fragments low-resource language words into meaningless subwords. SPLARE operates at the concept level.

4. **Concrete example (Figure 3):** On a Tamil-to-English retrieval task from XTREME-UP, SPLARE's top features are coherent concepts ("historical/cultural contexts," "India mentions," "casualties") that match across languages. SPLADE produces scattered Latin-script tokens that fail cross-lingually. SPLARE ranks the correct document 4th; SPLADE ranks it 23rd.

5. **Performance on unseen languages:** SPLARE achieves state-of-the-art on "secret" languages in MIRACL (German, Yoruba) that had zero training data, demonstrating genuine cross-lingual transfer rather than memorization.

---

### 5. Results

#### MMTEB Multilingual Retrieval (Table 3)
- **SPLARE-7B: 62.3 nDCG@10** -- top-10 overall on the leaderboard, and the **#1 learned sparse retrieval model**
- For context: NV-Embed-v2 scores 56.7, gte-Qwen2-7B-instruct scores 60.1
- English subset: 59.3 nDCG@10

#### MIRACL (18-language benchmark, Table 11)
- **SPLARE-7B: 71.7 nDCG@10 average**
- Outperforms M3-Embeddings (hybrid dense+sparse) by +0.2 points
- State-of-the-art on 8 individual languages: English, Finnish, Hindi, Japanese, Russian, Swahili, German, Yoruba
- Strong on "secret" (zero-shot) languages: German, Yoruba

#### XTREME-UP (Low-Resource Languages, Table 12)
- SPLARE-7B: 58.6 MRR@10 (vs. Gemini Embedding 64.3, SPLADE-Llama 56.2)
- Especially strong on low-resource Indic languages: +2.4 over SPLADE-Llama

#### English-Only (MS MARCO training, Table 1)
- SPLARE: 52.9 = SPLADE-Llama: 52.9 (identical on English when both trained on English data only)
- The divergence appears on multilingual/out-of-domain tasks, confirming the language-agnostic advantage

#### Domain-Specific (multilingual models)
- Medical: 67.7 (+0.1 vs SPLADE), Law: 60.8 (+0.1), Chemical: 78.1 (+0.7)
- Code: 63.0 (-1.3) -- a notable weakness

#### WSDM Cup 2026 Multilingual Retrieval
- SPLARE-7B (non-pooled) achieved 0.498 nDCG@20, which was **+7.5 nDCG@20 over Qwen3-8B-Embed** (0.423)
- With fusion and reranking enhancements, reached 0.559 nDCG@20
- Substantially outperformed MILCO (0.395) and PLAID-X (0.396)

---

### 6. How SPLARE Differs from Traditional SPLADE

| Aspect | SPLADE | SPLARE |
|--------|--------|--------|
| Projection space | Vocabulary (128k tokens) | SAE latent space (65k-131k+ features) |
| Dimension semantics | Subword tokens | Monosemantic concepts |
| Scalability | Fixed by vocabulary | SAE width scales independently (log-linear improvement) |
| Multilingual | Poor (tokenizer-dependent) | Strong (language-agnostic features) |
| Inference depth | Full model forward pass | Intermediate layer only (~2/3 depth) |
| Sparsity control | Trained into model | Post-hoc Top-K (single model, multiple sparsity levels) |
| Robustness to sparsification | -6% at Top-K=100 | -2% at Top-K=100 |
| Feature utilization | <100k of 128k vocab activated | Nearly all 131k features utilized |

---

### 7. Key Ablation Findings

- **Layer depth:** Optimal SAE insertion is at ~2/3 model depth. This also provides an inference speedup since later layers are never computed.
- **SAE width:** Log-linear relationship between width and retrieval effectiveness (tested 16k to 1M on Gemma-2). Wider SAEs consistently improve performance.
- **Robustness to sparsification:** SPLARE degrades only 2% when aggressively pruning to Top-K=100 document features, versus 6% for SPLADE. SPLARE's activation distribution is more balanced across features.
- **Feature utilization:** SPLARE activates nearly all 131k dimensions across the corpus; SPLADE concentrates activation on a small subset of the 128k vocabulary, wasting capacity.

---

### 8. Limitations and Open Questions

1. **Code retrieval underperformance (-1.3 vs SPLADE):** The authors find that top-activated features on code tasks "appear overly generic rather than specialized to code semantics." They suggest domain-specific SAEs trained on code-focused corpora may be needed.

2. **SAE transfer challenges:** The authors acknowledge recent work showing SAEs can struggle to transfer to certain downstream tasks. The frozen SAE may not always capture the right features for every domain.

3. **Training data overlap:** The multilingual training set (BGE) overlaps with some MTEB benchmark tasks, complicating strict generalization claims.

4. **Temperature sensitivity:** The distillation temperature tau is critically important and SAE-suite-dependent (80 for Llama Scope, 50 for Gemma Scope), requiring careful tuning.

5. **Future directions mentioned:** Domain-specific SAEs for specialized domains; scaling to very large SAE widths (up to 14M features on large LLMs); multimodal extension of SPLARE; cross-modal sparse latent retrieval; integration with approximate sparse retrieval algorithms.

---

### Sources

- [SPLARE Paper - arXiv Abstract](https://arxiv.org/abs/2603.13277)
- [SPLARE Paper - Full HTML](https://arxiv.org/html/2603.13277)
- [OpenReview Submission](https://openreview.net/forum?id=TuFjICawSc)
- [Naver Labs Europe @ WSDM Cup](https://arxiv.org/abs/2602.20986)
- [SPLADE GitHub (Naver)](https://github.com/naver/splade)

agentId: afee5f8039c748a86 (use SendMessage with to: 'afee5f8039c748a86' to continue this agent)
&lt;usage>total_tokens: 21782
tool_uses: 9
duration_ms: 183344&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "939b2adf-d171-4efb-b169-c17cec6fd60d",
  "isSidechain": false,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "type": "user",
  "uuid": "37223c0b-ec00-41c9-bbc2-ccb5f4673fe7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"SPLARE: Learning Retrieval Models with Sparse Autoencoders\" (arXiv 2603.13277, 2026).\n\n1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2603.13277\n2. Use WebFetch to read the HTML version for method details: https://arxiv.org/html/2603.13277\n3. Search the web for any discussion or reviews of SPLARE sparse autoencoder retrieval.\n\nExtract:\n- The exact gap/problem they identified with SPLADE-style vocabulary-space projection\n- Their key insight: using sparse autoencoders (SAEs) to decompose LLM representations into interpretable latent features\n- Method details: how the sparse autoencoder is trained, how it replaces vocabulary projection, architecture\n- Why this is more language-agnostic than SPLADE\n- Results: SPLARE-7B performance on MMTEB multilingual and English retrieval benchmarks\n- How this differs from traditional SPLADE approaches\n- Any limitations or open questions\n\nBe thorough with technical details about the SAE architecture and training procedure.",
    "agentId": "afee5f8039c748a86",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Here is the full research synthesis:\n\n---\n\n## SPLARE: Learning Retrieval Models with Sparse Autoencoders (arXiv 2603.13277)\n\n**Authors:** Thibault Formal, Maxime Louis, Herve Dejean, Stephane Clinchant (Naver Labs Europe)\n**Venue:** ICLR 2026 | Submitted October 8, 2025; arXiv February 27, 2026\n\n---\n\n### 1. The Problem with SPLADE-Style Vocabulary-Space Projection\n\nSPLADE and other Learned Sparse Retrieval (LSR) methods project LLM representations onto the **vocabulary space** -- essentially using the language model head to produce a sparse vector where each dimension corresponds to a token in the model's wordpiece vocabulary. The authors identify several fundamental limitations:\n\n- **Fixed vocabulary constraint:** LSR methods are \"inherently constrained by the fixed vocabulary of their underlying backbone.\" The vocabulary was designed for tokenization, not for representing semantic concepts.\n- **Tokenization redundancy:** Multiple vocabulary tokens encode the same semantic concept (e.g., \"Indian\" and \"indian\" as separate dimensions), wasting representational capacity.\n- **Language specificity:** Subword tokenizers are heavily biased toward the languages dominant in pretraining data. Low-resource languages get poor coverage, leading to fragmented and semantically incoherent sparse representations.\n- **Multilingual failure:** At the time of submission, **no sparse retrieval model appeared on the MTEB Multilingual v2 leaderboard** -- a stark indicator that vocabulary-based LSR had fundamentally failed to generalize across languages.\n- **Fixed dimensionality:** The vocabulary size is locked at whatever the backbone model uses (e.g., 128k for Llama-3.1), with no mechanism to scale representation capacity.\n\n---\n\n### 2. Key Insight: SAEs Decompose LLM Representations into Language-Agnostic Semantic Features\n\nThe central insight draws from the **mechanistic interpretability** literature. Sparse autoencoders (SAEs), when trained on LLM residual stream activations, decompose dense hidden states into interpretable latent features that exhibit several properties ideal for retrieval:\n\n- **Monosemanticity:** Most SAE features correspond to a single, coherent concept (e.g., \"casualties in conflict,\" \"references to India\"), unlike individual neurons which are polysemantic.\n- **Language-agnosticism:** SAE features activate consistently for the same semantic content regardless of input language. A feature for \"historical/cultural contexts\" fires on Tamil, English, and German text alike.\n- **Scalability:** SAE width (number of latent features) can be scaled independently of the LLM vocabulary -- from 16k to over 1M features -- providing a tunable knob for representational capacity.\n\nThe authors' key realization: if SAEs already produce sparse, interpretable, language-agnostic features from LLM hidden states, they are a **natural replacement** for vocabulary projection in sparse retrieval.\n\n---\n\n### 3. Method Details: The SPLARE Architecture\n\n#### 3.1 SAE Mathematical Foundation\n\nA standard sparse autoencoder maps an LLM hidden state **x** in R^d to a high-dimensional sparse latent **z** in R^|W| (where |W| >> d):\n\n```\nz = f(W_enc * x + b_enc)       [encoder]\nx_hat = W_dec * z + b_dec       [decoder/reconstruction]\n```\n\nThe SAE is trained to minimize reconstruction loss ||x_hat - x||^2 with sparsity induced through the activation function f (ReLU, Top-K, or JumpReLU) and L1 regularization. The authors use **pre-trained, publicly available SAEs** (Llama Scope for Llama-3.1-8B with 131k features; Gemma Scope for Gemma-2-2B with 65k features).\n\n#### 3.2 SPLARE Pipeline (Replacing Vocabulary Projection)\n\nThe pipeline mirrors SPLADE but swaps out the LM head for an SAE encoder:\n\n1. **Forward pass to intermediate layer:** Process input tokens through the LLM backbone, but only up to an intermediate layer (optimally ~2/3 depth -- layer 20-22 for Llama-3.1-8B's 32 layers, layer 16-17 for Gemma-2-2B's 26 layers). This is a computational advantage since SPLADE must run the full model.\n\n2. **SAE encoding:** Apply the frozen SAE encoder to each token's hidden state, producing sparse latent logits (v_i1, v_i2, ..., v_i|W|) for each token i.\n\n3. **SPLADE-style pooling (\"SPLADE-pool\"):** Aggregate token-level features into a single document/query vector using max-pooling with log-saturation:\n   ```\n   u_j = max_{i=1...n} log(1 + ReLU(v_ij)),  for j in W (latent feature space)\n   ```\n   This is identical to SPLADE's pooling, but over the SAE latent space W instead of vocabulary V.\n\n4. **Scoring:** Standard sparse dot product: s(q, d) = &lt;u_q, u_d>\n\n#### 3.3 Training Procedure\n\n**What is trained vs. frozen:**\n- **SAE:** Completely frozen (preserves interpretability and language-agnostic properties)\n- **LLM backbone:** Fine-tuned with **LoRA** (rank=64) to adapt hidden states for retrieval\n- **Bidirectional attention:** Enabled across all LLM layers (critical for position-wise pooling)\n\n**Pre-training step:** Masked Language Modeling (20% token masking) on MS MARCO for 10k steps (~5 hours). This adapts the LLM to bidirectional attention before retrieval fine-tuning.\n\n**Loss function -- distillation-based:**\n```\nL = L_KL + lambda_q * L_FLOPS^q + lambda_d * L_FLOPS^d\n```\n\nWhere L_KL is the KL divergence between a cross-encoder teacher's relevance distribution and the student's:\n```\np_hat_i = exp(s(q, d_i)/tau) / sum_j exp(s(q, d_j)/tau)   [student, temperature-scaled]\np_i = exp(s_i) / sum_j exp(s_j)                             [teacher]\n```\n\nThe FLOPS regularizer controls sparsity (lambda_q = lambda_d = 0.0001). Distillation was chosen over contrastive learning because it better handles false negatives.\n\n**Key hyperparameters:**\n- Learning rate: 5e-5\n- Batch size: 128\n- Temperature tau: 80 (Llama Scope), 50 (Gemma Scope) -- selected via grid search over {1, 10, 20, 40, 50, 80, 100}; critically important and SAE-suite-dependent\n- Negatives per query: 8\n- Epochs: 1\n- Max sequence length: 128 (English), 512 (multilingual)\n\n**Inference-time sparsity control -- Top-K pooling:**\nAfter training, a Top-K selection is applied: keep only the top k=40 features for queries and k=400 for documents. This decouples sparsity from training, allowing a single trained model to operate at multiple sparsity levels without retraining.\n\n**Training data:**\n- English setting: MS MARCO with DeBERTa-v3 reranker distillation targets\n- Multilingual setting: BGE multilingual training set (1.3M queries from MS MARCO, NQ, HotpotQA, Chinese retrieval datasets, MIRACL, Mr.TyDi) with BGE-reranker-v2-m3 as teacher\n\n---\n\n### 4. Why SPLARE Is More Language-Agnostic Than SPLADE\n\nSeveral reinforcing factors:\n\n1. **SAE features transcend tokenization:** SPLADE's dimensions are vocabulary tokens -- inherently language-specific surface forms. SPLARE's dimensions are learned semantic concepts that activate identically across languages.\n\n2. **Empirical evidence from interpretability research:** The authors cite work showing SAE features on residual streams are \"largely invariant across languages\" -- the same feature fires for \"casualties\" whether the input is in Tamil, English, or Yoruba.\n\n3. **No tokenization artifacts:** SPLADE wastes capacity on redundant tokens (\"Indian\" vs. \"indian\") and fragments low-resource language words into meaningless subwords. SPLARE operates at the concept level.\n\n4. **Concrete example (Figure 3):** On a Tamil-to-English retrieval task from XTREME-UP, SPLARE's top features are coherent concepts (\"historical/cultural contexts,\" \"India mentions,\" \"casualties\") that match across languages. SPLADE produces scattered Latin-script tokens that fail cross-lingually. SPLARE ranks the correct document 4th; SPLADE ranks it 23rd.\n\n5. **Performance on unseen languages:** SPLARE achieves state-of-the-art on \"secret\" languages in MIRACL (German, Yoruba) that had zero training data, demonstrating genuine cross-lingual transfer rather than memorization.\n\n---\n\n### 5. Results\n\n#### MMTEB Multilingual Retrieval (Table 3)\n- **SPLARE-7B: 62.3 nDCG@10** -- top-10 overall on the leaderboard, and the **#1 learned sparse retrieval model**\n- For context: NV-Embed-v2 scores 56.7, gte-Qwen2-7B-instruct scores 60.1\n- English subset: 59.3 nDCG@10\n\n#### MIRACL (18-language benchmark, Table 11)\n- **SPLARE-7B: 71.7 nDCG@10 average**\n- Outperforms M3-Embeddings (hybrid dense+sparse) by +0.2 points\n- State-of-the-art on 8 individual languages: English, Finnish, Hindi, Japanese, Russian, Swahili, German, Yoruba\n- Strong on \"secret\" (zero-shot) languages: German, Yoruba\n\n#### XTREME-UP (Low-Resource Languages, Table 12)\n- SPLARE-7B: 58.6 MRR@10 (vs. Gemini Embedding 64.3, SPLADE-Llama 56.2)\n- Especially strong on low-resource Indic languages: +2.4 over SPLADE-Llama\n\n#### English-Only (MS MARCO training, Table 1)\n- SPLARE: 52.9 = SPLADE-Llama: 52.9 (identical on English when both trained on English data only)\n- The divergence appears on multilingual/out-of-domain tasks, confirming the language-agnostic advantage\n\n#### Domain-Specific (multilingual models)\n- Medical: 67.7 (+0.1 vs SPLADE), Law: 60.8 (+0.1), Chemical: 78.1 (+0.7)\n- Code: 63.0 (-1.3) -- a notable weakness\n\n#### WSDM Cup 2026 Multilingual Retrieval\n- SPLARE-7B (non-pooled) achieved 0.498 nDCG@20, which was **+7.5 nDCG@20 over Qwen3-8B-Embed** (0.423)\n- With fusion and reranking enhancements, reached 0.559 nDCG@20\n- Substantially outperformed MILCO (0.395) and PLAID-X (0.396)\n\n---\n\n### 6. How SPLARE Differs from Traditional SPLADE\n\n| Aspect | SPLADE | SPLARE |\n|--------|--------|--------|\n| Projection space | Vocabulary (128k tokens) | SAE latent space (65k-131k+ features) |\n| Dimension semantics | Subword tokens | Monosemantic concepts |\n| Scalability | Fixed by vocabulary | SAE width scales independently (log-linear improvement) |\n| Multilingual | Poor (tokenizer-dependent) | Strong (language-agnostic features) |\n| Inference depth | Full model forward pass | Intermediate layer only (~2/3 depth) |\n| Sparsity control | Trained into model | Post-hoc Top-K (single model, multiple sparsity levels) |\n| Robustness to sparsification | -6% at Top-K=100 | -2% at Top-K=100 |\n| Feature utilization | <100k of 128k vocab activated | Nearly all 131k features utilized |\n\n---\n\n### 7. Key Ablation Findings\n\n- **Layer depth:** Optimal SAE insertion is at ~2/3 model depth. This also provides an inference speedup since later layers are never computed.\n- **SAE width:** Log-linear relationship between width and retrieval effectiveness (tested 16k to 1M on Gemma-2). Wider SAEs consistently improve performance.\n- **Robustness to sparsification:** SPLARE degrades only 2% when aggressively pruning to Top-K=100 document features, versus 6% for SPLADE. SPLARE's activation distribution is more balanced across features.\n- **Feature utilization:** SPLARE activates nearly all 131k dimensions across the corpus; SPLADE concentrates activation on a small subset of the 128k vocabulary, wasting capacity.\n\n---\n\n### 8. Limitations and Open Questions\n\n1. **Code retrieval underperformance (-1.3 vs SPLADE):** The authors find that top-activated features on code tasks \"appear overly generic rather than specialized to code semantics.\" They suggest domain-specific SAEs trained on code-focused corpora may be needed.\n\n2. **SAE transfer challenges:** The authors acknowledge recent work showing SAEs can struggle to transfer to certain downstream tasks. The frozen SAE may not always capture the right features for every domain.\n\n3. **Training data overlap:** The multilingual training set (BGE) overlaps with some MTEB benchmark tasks, complicating strict generalization claims.\n\n4. **Temperature sensitivity:** The distillation temperature tau is critically important and SAE-suite-dependent (80 for Llama Scope, 50 for Gemma Scope), requiring careful tuning.\n\n5. **Future directions mentioned:** Domain-specific SAEs for specialized domains; scaling to very large SAE widths (up to 14M features on large LLMs); multimodal extension of SPLARE; cross-modal sparse latent retrieval; integration with approximate sparse retrieval algorithms.\n\n---\n\n### Sources\n\n- [SPLARE Paper - arXiv Abstract](https://arxiv.org/abs/2603.13277)\n- [SPLARE Paper - Full HTML](https://arxiv.org/html/2603.13277)\n- [OpenReview Submission](https://openreview.net/forum?id=TuFjICawSc)\n- [Naver Labs Europe @ WSDM Cup](https://arxiv.org/abs/2602.20986)\n- [SPLADE GitHub (Naver)](https://github.com/naver/splade)"
      }
    ],
    "totalDurationMs": 183344,
    "totalTokens": 21782,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 17608,
      "output_tokens": 3678,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 495
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3678,
          "cache_read_input_tokens": 17608,
          "cache_creation_input_tokens": 495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 495,
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
  "sourceToolAssistantUUID": "939b2adf-d171-4efb-b169-c17cec6fd60d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 20 · 2026-05-30T06:24:36.774Z_

<details><summary>↩ Tool result · `toolu_01PVRFRTRB29V3qa3QAS6H4s`</summary>

```text
Now I have comprehensive information. Let me compile the full research report.

---

## Research Report: "A Survey of Model Architectures in Information Retrieval" (arXiv 2502.14822)

### Paper Metadata
- **Title:** A Survey of Model Architectures in Information Retrieval
- **Authors:** Zhichao Xu, Fengran Mo, Zhiqi Huang, Crystina Zhang, Puxuan Yu, Bei Wang, Jimmy Lin, Vivek Srikumar
- **Affiliations:** University of Utah, University of Montreal, Capital One, University of Waterloo, Snowflake
- **Submitted:** February 20, 2025 (v1); last revised March 15, 2026 (v3)
- **Published:** TMLR (Transactions on Machine Learning Research), February 24, 2026, with Survey Certification
- **OpenReview:** https://openreview.net/forum?id=xAIbTbHRrX

---

### 1. Scope and Organization

The survey traces the evolution of IR model **architectures** from 2019 onward, covering the full arc from traditional term-based methods through neural pre-transformer models to transformer-based and LLM-based approaches. It is organized into 10 sections:

1. Introduction
2. Background and Terminology (task definition, retrieve-then-rerank, disentangling architecture from training)
3. Traditional IR Models (Boolean, Vector Space, Probabilistic, Statistical Language Models)
4. Learning-to-Rank Model Architectures
5. Neural Ranking Models (pre-Transformer)
6. IR with Pre-Trained Transformers
7. Large Language Models for IR
8. Architectures for Diverse Scenarios (multilingual, multimodal, efficiency)
9. Emerging Directions and Challenges
10. Conclusions

### 2. Taxonomy / Categorization of IR Architectures

The survey defines a multi-level taxonomy:

**Foundational evolution axis:** term-based --> dense neural --> transformer-based --> LLM-based

**Core architectural dichotomy** (the central organizing principle):
- **Cross-Encoder (deep interaction):** Concatenates query and document, processes them jointly through a transformer, enabling full token-level interaction. Expensive at retrieval time but powerful for reranking.
- **Bi-Encoder (separable pre-computation):** Encodes query and document independently into fixed representations. Enables offline document encoding and fast ANN search but has limited interaction depth.

**Within bi-encoders**, the survey further distinguishes:
- **Dense retrieval** (DPR, ANCE, E5, GTE): Low-dimensional dense vectors (~768 dims), relevance via dot product/cosine similarity
- **Learned sparse retrieval** (SPLADE, DeepImpact, uniCOIL): High-dimensional sparse vectors with vocabulary-size dimensionality, each dimension corresponding to a specific vocabulary term
- **Multi-vector representations** (ColBERT, Poly-Encoder, ME-BERT): Multiple vectors per query/document with "late interaction" mechanisms

Key figures support this taxonomy: **Figure 3** illustrates four paradigms: (a) cross-encoder reranker, (b) learned dense retrieval, (c) learned sparse retrieval, (d) multi-vector representations. **Table 3** catalogs 21+ transformer-based IR models with their architecture type, backbone LM, and training strategy.

### 3. Architecture vs. Training Methodology: A Deliberate Separation

This is a defining methodological choice of the survey. The authors explicitly state they "intentionally seek to disentangle these aspects to provide a focused analysis on the evolution of model architecture." They include backbone models, system architectures, and feature extraction designs, but exclude loss functions, data augmentation, optimization algorithms, indexing, quantization, and parallelization.

Their rationale: "This focus allows for a clearer narrative on how the core components for representation learning and relevance estimation have changed over time, from term-based logic to deep neural networks."

They acknowledge the co-evolution, however, noting that "the architectural dichotomy (cross-encoder vs. bi-encoder) has an impactful influence on the training methodology." Training strategies like contrastive objectives (InfoNCE), hard negative mining, and knowledge distillation are covered in Section 6.1 to the extent they are architecturally relevant.

### 4. Sparse, Dense, Hybrid, and Generative Retrieval Coverage

**Sparse retrieval:** The survey frames learned sparse retrieval (SPLADE, DeepImpact, uniCOIL) as "a sophisticated evolution of traditional term weighting schemes, learning context-aware token importance scores from data." Three architectural constraints distinguish sparse from dense encoders: (1) explicit sparsity regularization, (2) non-negative weight requirements for inverted index compatibility, (3) vocabulary-aligned vector dimensions. This preserves compatibility with existing retrieval infrastructure.

**Dense retrieval:** Covered through the standard dual-encoder paradigm using BERT encoders producing ~768-dimensional vectors. Key models (DPR, ANCE, E5, GTE) are cataloged. The advantage is solving the vocabulary mismatch problem; the limitation is that "a single fixed-size vector constrains expressiveness."

**Hybrid retrieval:** Multiple strategies are discussed:
- Multi-vector representations (ColBERT's MaxSim late interaction)
- System-level fusion (Reciprocal Rank Fusion for merging sparse and dense result lists)
- Representation-level fusion (COIL combining bag-of-words with BERT embeddings; SLIM mapping contextualized tokens to sparse lexical space; SPLATE combining token vectors with SPLADE modules)

**Generative retrieval:** Covered in Section 7.3, discussing encoder-decoder models (T5, BART) for direct document identifier generation. Key design dimensions include identifier taxonomy (semantic vs. lexical), inference constraints, and decoding strategies. Open challenges flagged: hallucination, identifier coverage, and training efficiency.

### 5. Decoder-Only LLMs for Retrieval

The survey identifies a fundamental architectural tension: decoder-only models use **unidirectional (causal) self-attention**, making their application to retrieval "less direct" than encoder-only models. This "requires architectural adaptations to create meaningful summary vectors from their unidirectional hidden states."

Three adaptation approaches are discussed:
1. **Scaling bi-encoders:** Applying decoder-only models with instruction tuning to create dense retrievers (e.g., TART-dual)
2. **Decoder-only adaptation:** Architectural modifications to extract meaningful representations despite causal attention constraints
3. **Unified modeling:** End-to-end frameworks treating retrieval as sequence generation

For reranking (Section 7.2), the survey covers fine-tuned rerankers via instruction-tuning and zero-shot/few-shot prompting approaches.

### 6. Sparse-Dense Complementarity

The survey frames this through a **unifying lens** (citing Lin 2021): "Dense retrieval models, learned sparse retrieval models, and traditional bag-of-words approaches such as BM25 can all be interpreted as parametric variations of [the bi-encoder] architecture."

The differentiation is along two axes: "(1) the representational basis (dense semantic embeddings versus sparse lexical vectors), and (2) whether those representations are learned from data or manually engineered."

The authors note that "hybrid models demonstrate that combining distributed representations with traditional local representations is favorable." However, hybrid strategies are discussed primarily at the system level (result fusion) or through specialized multi-vector architectures, not as unified single-model approaches.

### 7. Gap Regarding Unified Sparse+Dense in Decoder-Only Models

This is a notable **implicit gap** in the survey. The paper does NOT discuss whether a single decoder-only model can produce both sparse AND dense representations simultaneously. Decoder-only models are treated only as:
- Dense retriever adaptations
- Rerankers
- Generative retrieval systems

The possibility of a decoder-only backbone generating both sparse (vocabulary-aligned) and dense (semantic embedding) representations from the same model is not addressed as an architectural direction. This is precisely the space that LACONIC and related work later occupy.

### 8. Open Problems and Future Directions (Section 9)

Four major research frontiers:
1. **Advancing Core Components:** More powerful and efficient foundation models; flexible and scalable relevance estimators
2. **Paradigm Shift -- From Search for Humans to Retrieval for AI:** The "end user" of retrieval transitioning to AI systems; RAG integration; autonomous search agents performing multi-step reasoning
3. **Beyond Simple Relevance:** Instruction-following retrieval (models respecting complex user instructions); reasoning-aware retrieval (incorporating multi-step reasoning)
4. **Deployment and Robustness:** Efficiency-effectiveness tradeoff at scale; robustness against adversarial inputs and distribution shifts; architectural optimization for efficiency and scalability; handling multimodal and multilingual data

### 9. Connection to LACONIC

**LACONIC** (arXiv 2601.01684, January 2026) shares the same first author (Zhichao Xu) and several co-authors (Crystina Zhang, Jimmy Lin, Vivek Srikumar). LACONIC is a family of **learned sparse retrievers** built on the Llama-3 architecture (1B, 3B, 8B parameters) using a two-phase training curriculum: (1) weakly supervised pre-finetuning to adapt causal LLMs for bidirectional contextualization, and (2) high-signal finetuning with curated hard negatives. The 8B variant achieves 60.2 nDCG@10 on MTEB Retrieval with 71% less index memory than equivalent dense models.

The survey (submitted February 2025, accepted February 2026) does **not** cite LACONIC (published January 2026). However, the connection is clear: the survey's identification of decoder-only adaptation challenges and the sparse-dense architectural gap directly motivates LACONIC's contribution of making decoder-only LLMs work as effective sparse retrievers. The survey maps the design space; LACONIC fills a specific gap within it.

A closely related concurrent work is **"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs"** by Hansi Zeng et al. (arXiv 2502.15526, SIGIR 2025), which uses the same Llama-3 backbone and finds that sparse retrieval consistently outperforms dense retrieval across all scales with greater robustness to noisy training signals.

### 10. Reviewer Comments

Unfortunately, the TMLR reviews were not accessible through the OpenReview page (the page rendered only metadata, not the review discussion threads, which likely require JavaScript-based dynamic loading). What is confirmed:
- The paper was **accepted** at TMLR with **Survey Certification** status
- It is classified as a **long submission**
- Publication date: February 24, 2026
- The paper went through at least 3 revisions (v1 Feb 2025, v3 March 2026)

The 13-month revision timeline (Feb 2025 to March 2026) suggests substantive reviewer engagement and revision.

### Summary of Key Findings for Your Research

The survey's most relevant contributions to understanding the sparse+dense design space in decoder-only models:

1. **The bi-encoder unifying framework** treats sparse, dense, and BM25 as parametric variations, differing along representational basis and learnedness axes -- but does not extend this unification into decoder-only architectures.

2. **The identified architectural challenge** of decoder-only models -- that causal attention makes representation extraction "less direct" -- is exactly what LACONIC addresses through its bidirectional contextualization pre-finetuning phase.

3. **The gap is implicit but real:** the survey catalogs hybrid approaches (ColBERT, COIL, SLIM, SPLATE) but these are all encoder-only. No decoder-only model is discussed that produces unified sparse+dense representations. This is the precise architectural gap that motivates LACONIC and Zeng et al.'s work.

4. **The survey's architecture-vs-training separation** is both a strength (clarity) and a limitation: LACONIC's key innovation is partly architectural (adapting causal attention for sparse representation) and partly training curriculum (two-phase approach), making it a natural extension of the survey's framework.

agentId: a5d47badf0af062b8 (use SendMessage with to: 'a5d47badf0af062b8' to continue this agent)
&lt;usage>total_tokens: 26840
tool_uses: 17
duration_ms: 212041&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d2e7619-c9a4-416b-a13d-a83433eb4aaa",
  "isSidechain": false,
  "promptId": "0500c16e-7ea2-407e-bfcd-63f5d6e1769a",
  "type": "user",
  "uuid": "fcc9f945-b33a-4dff-8fe4-143fb81fd9d6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Research the paper \"A Survey of Model Architectures in Information Retrieval\" (arXiv 2502.14822, TMLR 2025).\n\n1. Use WebFetch to read the arxiv abstract page: https://arxiv.org/abs/2502.14822\n2. Use WebFetch to read the HTML version for details: https://arxiv.org/html/2502.14822\n3. Search for TMLR reviews or OpenReview page for this paper.\n\nExtract:\n- The scope and organization of the survey\n- How they categorize/taxonomize IR model architectures\n- Key distinctions they make (e.g., architecture vs training methodology)\n- Coverage of sparse, dense, hybrid, and generative retrieval\n- Their analysis of decoder-only LLMs for retrieval\n- Any identified open problems or future directions\n- How they discuss the sparse-dense complementarity\n- Whether they identify the gap of unified sparse+dense in decoder-only models\n- The connection to LACONIC (same first author)\n- Any reviewer comments\n\nFocus especially on: what architectural design space they define, how they compare sparse vs dense approaches, and what gaps they identify for future work.",
    "agentId": "a5d47badf0af062b8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the full research report.\n\n---\n\n## Research Report: \"A Survey of Model Architectures in Information Retrieval\" (arXiv 2502.14822)\n\n### Paper Metadata\n- **Title:** A Survey of Model Architectures in Information Retrieval\n- **Authors:** Zhichao Xu, Fengran Mo, Zhiqi Huang, Crystina Zhang, Puxuan Yu, Bei Wang, Jimmy Lin, Vivek Srikumar\n- **Affiliations:** University of Utah, University of Montreal, Capital One, University of Waterloo, Snowflake\n- **Submitted:** February 20, 2025 (v1); last revised March 15, 2026 (v3)\n- **Published:** TMLR (Transactions on Machine Learning Research), February 24, 2026, with Survey Certification\n- **OpenReview:** https://openreview.net/forum?id=xAIbTbHRrX\n\n---\n\n### 1. Scope and Organization\n\nThe survey traces the evolution of IR model **architectures** from 2019 onward, covering the full arc from traditional term-based methods through neural pre-transformer models to transformer-based and LLM-based approaches. It is organized into 10 sections:\n\n1. Introduction\n2. Background and Terminology (task definition, retrieve-then-rerank, disentangling architecture from training)\n3. Traditional IR Models (Boolean, Vector Space, Probabilistic, Statistical Language Models)\n4. Learning-to-Rank Model Architectures\n5. Neural Ranking Models (pre-Transformer)\n6. IR with Pre-Trained Transformers\n7. Large Language Models for IR\n8. Architectures for Diverse Scenarios (multilingual, multimodal, efficiency)\n9. Emerging Directions and Challenges\n10. Conclusions\n\n### 2. Taxonomy / Categorization of IR Architectures\n\nThe survey defines a multi-level taxonomy:\n\n**Foundational evolution axis:** term-based --> dense neural --> transformer-based --> LLM-based\n\n**Core architectural dichotomy** (the central organizing principle):\n- **Cross-Encoder (deep interaction):** Concatenates query and document, processes them jointly through a transformer, enabling full token-level interaction. Expensive at retrieval time but powerful for reranking.\n- **Bi-Encoder (separable pre-computation):** Encodes query and document independently into fixed representations. Enables offline document encoding and fast ANN search but has limited interaction depth.\n\n**Within bi-encoders**, the survey further distinguishes:\n- **Dense retrieval** (DPR, ANCE, E5, GTE): Low-dimensional dense vectors (~768 dims), relevance via dot product/cosine similarity\n- **Learned sparse retrieval** (SPLADE, DeepImpact, uniCOIL): High-dimensional sparse vectors with vocabulary-size dimensionality, each dimension corresponding to a specific vocabulary term\n- **Multi-vector representations** (ColBERT, Poly-Encoder, ME-BERT): Multiple vectors per query/document with \"late interaction\" mechanisms\n\nKey figures support this taxonomy: **Figure 3** illustrates four paradigms: (a) cross-encoder reranker, (b) learned dense retrieval, (c) learned sparse retrieval, (d) multi-vector representations. **Table 3** catalogs 21+ transformer-based IR models with their architecture type, backbone LM, and training strategy.\n\n### 3. Architecture vs. Training Methodology: A Deliberate Separation\n\nThis is a defining methodological choice of the survey. The authors explicitly state they \"intentionally seek to disentangle these aspects to provide a focused analysis on the evolution of model architecture.\" They include backbone models, system architectures, and feature extraction designs, but exclude loss functions, data augmentation, optimization algorithms, indexing, quantization, and parallelization.\n\nTheir rationale: \"This focus allows for a clearer narrative on how the core components for representation learning and relevance estimation have changed over time, from term-based logic to deep neural networks.\"\n\nThey acknowledge the co-evolution, however, noting that \"the architectural dichotomy (cross-encoder vs. bi-encoder) has an impactful influence on the training methodology.\" Training strategies like contrastive objectives (InfoNCE), hard negative mining, and knowledge distillation are covered in Section 6.1 to the extent they are architecturally relevant.\n\n### 4. Sparse, Dense, Hybrid, and Generative Retrieval Coverage\n\n**Sparse retrieval:** The survey frames learned sparse retrieval (SPLADE, DeepImpact, uniCOIL) as \"a sophisticated evolution of traditional term weighting schemes, learning context-aware token importance scores from data.\" Three architectural constraints distinguish sparse from dense encoders: (1) explicit sparsity regularization, (2) non-negative weight requirements for inverted index compatibility, (3) vocabulary-aligned vector dimensions. This preserves compatibility with existing retrieval infrastructure.\n\n**Dense retrieval:** Covered through the standard dual-encoder paradigm using BERT encoders producing ~768-dimensional vectors. Key models (DPR, ANCE, E5, GTE) are cataloged. The advantage is solving the vocabulary mismatch problem; the limitation is that \"a single fixed-size vector constrains expressiveness.\"\n\n**Hybrid retrieval:** Multiple strategies are discussed:\n- Multi-vector representations (ColBERT's MaxSim late interaction)\n- System-level fusion (Reciprocal Rank Fusion for merging sparse and dense result lists)\n- Representation-level fusion (COIL combining bag-of-words with BERT embeddings; SLIM mapping contextualized tokens to sparse lexical space; SPLATE combining token vectors with SPLADE modules)\n\n**Generative retrieval:** Covered in Section 7.3, discussing encoder-decoder models (T5, BART) for direct document identifier generation. Key design dimensions include identifier taxonomy (semantic vs. lexical), inference constraints, and decoding strategies. Open challenges flagged: hallucination, identifier coverage, and training efficiency.\n\n### 5. Decoder-Only LLMs for Retrieval\n\nThe survey identifies a fundamental architectural tension: decoder-only models use **unidirectional (causal) self-attention**, making their application to retrieval \"less direct\" than encoder-only models. This \"requires architectural adaptations to create meaningful summary vectors from their unidirectional hidden states.\"\n\nThree adaptation approaches are discussed:\n1. **Scaling bi-encoders:** Applying decoder-only models with instruction tuning to create dense retrievers (e.g., TART-dual)\n2. **Decoder-only adaptation:** Architectural modifications to extract meaningful representations despite causal attention constraints\n3. **Unified modeling:** End-to-end frameworks treating retrieval as sequence generation\n\nFor reranking (Section 7.2), the survey covers fine-tuned rerankers via instruction-tuning and zero-shot/few-shot prompting approaches.\n\n### 6. Sparse-Dense Complementarity\n\nThe survey frames this through a **unifying lens** (citing Lin 2021): \"Dense retrieval models, learned sparse retrieval models, and traditional bag-of-words approaches such as BM25 can all be interpreted as parametric variations of [the bi-encoder] architecture.\"\n\nThe differentiation is along two axes: \"(1) the representational basis (dense semantic embeddings versus sparse lexical vectors), and (2) whether those representations are learned from data or manually engineered.\"\n\nThe authors note that \"hybrid models demonstrate that combining distributed representations with traditional local representations is favorable.\" However, hybrid strategies are discussed primarily at the system level (result fusion) or through specialized multi-vector architectures, not as unified single-model approaches.\n\n### 7. Gap Regarding Unified Sparse+Dense in Decoder-Only Models\n\nThis is a notable **implicit gap** in the survey. The paper does NOT discuss whether a single decoder-only model can produce both sparse AND dense representations simultaneously. Decoder-only models are treated only as:\n- Dense retriever adaptations\n- Rerankers\n- Generative retrieval systems\n\nThe possibility of a decoder-only backbone generating both sparse (vocabulary-aligned) and dense (semantic embedding) representations from the same model is not addressed as an architectural direction. This is precisely the space that LACONIC and related work later occupy.\n\n### 8. Open Problems and Future Directions (Section 9)\n\nFour major research frontiers:\n1. **Advancing Core Components:** More powerful and efficient foundation models; flexible and scalable relevance estimators\n2. **Paradigm Shift -- From Search for Humans to Retrieval for AI:** The \"end user\" of retrieval transitioning to AI systems; RAG integration; autonomous search agents performing multi-step reasoning\n3. **Beyond Simple Relevance:** Instruction-following retrieval (models respecting complex user instructions); reasoning-aware retrieval (incorporating multi-step reasoning)\n4. **Deployment and Robustness:** Efficiency-effectiveness tradeoff at scale; robustness against adversarial inputs and distribution shifts; architectural optimization for efficiency and scalability; handling multimodal and multilingual data\n\n### 9. Connection to LACONIC\n\n**LACONIC** (arXiv 2601.01684, January 2026) shares the same first author (Zhichao Xu) and several co-authors (Crystina Zhang, Jimmy Lin, Vivek Srikumar). LACONIC is a family of **learned sparse retrievers** built on the Llama-3 architecture (1B, 3B, 8B parameters) using a two-phase training curriculum: (1) weakly supervised pre-finetuning to adapt causal LLMs for bidirectional contextualization, and (2) high-signal finetuning with curated hard negatives. The 8B variant achieves 60.2 nDCG@10 on MTEB Retrieval with 71% less index memory than equivalent dense models.\n\nThe survey (submitted February 2025, accepted February 2026) does **not** cite LACONIC (published January 2026). However, the connection is clear: the survey's identification of decoder-only adaptation challenges and the sparse-dense architectural gap directly motivates LACONIC's contribution of making decoder-only LLMs work as effective sparse retrievers. The survey maps the design space; LACONIC fills a specific gap within it.\n\nA closely related concurrent work is **\"Scaling Sparse and Dense Retrieval in Decoder-Only LLMs\"** by Hansi Zeng et al. (arXiv 2502.15526, SIGIR 2025), which uses the same Llama-3 backbone and finds that sparse retrieval consistently outperforms dense retrieval across all scales with greater robustness to noisy training signals.\n\n### 10. Reviewer Comments\n\nUnfortunately, the TMLR reviews were not accessible through the OpenReview page (the page rendered only metadata, not the review discussion threads, which likely require JavaScript-based dynamic loading). What is confirmed:\n- The paper was **accepted** at TMLR with **Survey Certification** status\n- It is classified as a **long submission**\n- Publication date: February 24, 2026\n- The paper went through at least 3 revisions (v1 Feb 2025, v3 March 2026)\n\nThe 13-month revision timeline (Feb 2025 to March 2026) suggests substantive reviewer engagement and revision.\n\n### Summary of Key Findings for Your Research\n\nThe survey's most relevant contributions to understanding the sparse+dense design space in decoder-only models:\n\n1. **The bi-encoder unifying framework** treats sparse, dense, and BM25 as parametric variations, differing along representational basis and learnedness axes -- but does not extend this unification into decoder-only architectures.\n\n2. **The identified architectural challenge** of decoder-only models -- that causal attention makes representation extraction \"less direct\" -- is exactly what LACONIC addresses through its bidirectional contextualization pre-finetuning phase.\n\n3. **The gap is implicit but real:** the survey catalogs hybrid approaches (ColBERT, COIL, SLIM, SPLATE) but these are all encoder-only. No decoder-only model is discussed that produces unified sparse+dense representations. This is the precise architectural gap that motivates LACONIC and Zeng et al.'s work.\n\n4. **The survey's architecture-vs-training separation** is both a strength (clarity) and a limitation: LACONIC's key innovation is partly architectural (adapting causal attention for sparse representation) and partly training curriculum (two-phase approach), making it a natural extension of the survey's framework."
      }
    ],
    "totalDurationMs": 212041,
    "totalTokens": 26840,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2020,
      "cache_read_input_tokens": 21909,
      "output_tokens": 2910,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2020
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2910,
          "cache_read_input_tokens": 21909,
          "cache_creation_input_tokens": 2020,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2020,
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
  "sourceToolAssistantUUID": "3d2e7619-c9a4-416b-a13d-a83433eb4aaa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
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
  "leafUuid": "fcc9f945-b33a-4dff-8fe4-143fb81fd9d6",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze hybrid retrieval architecture papers for AAAI 2026",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---

### Assistant

_source line 23 · 2026-05-30T06:24:47.038Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information on all 4 papers. Let me synthesize the analyses into the required JSON format, keeping each paper's analysis under 2000 characters.

Let me craft concise, analytical summaries for each paper:

1. **NV-Embed** - Key innovations: latent attention pooling, removing causal mask, two-stage training. ICLR 2025 Spotlight. Reviewers praised thoroughness but noted limited novelty of individual components.

2. **Scaling Laws for Dense Retrieval** - Key innovation: contrastive entropy metric enabling power-law fitting; inference-cost-dominant budget allocation inverts "bigger is better". SIGIR 2024 Best Paper.


3. **SPLARE** - Key innovation: leveraging sparse autoencoders from mechanistic interpretability to replace vocabulary projection, enabling language-agnostic sparse retrieval. arXiv 2026.

4. **IR Survey** - Comprehensive taxonomy separating architectural choices from training approaches; reveals an important gap in unified sparse+dense methods for decoder-only models. TMLR 2025 with Survey Certification.

Now I'll write these analyses in the JSON format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcc9f945-b33a-4dff-8fe4-143fb81fd9d6",
  "isSidechain": false,
  "requestId": "req_011CbYGugLfo36CUpWm5To2s",
  "type": "assistant",
  "uuid": "ff5296a7-6347-4d67-9ef6-a1c982eb1e9a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011t7VUMGkeFk38xsDk5HhDZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14451,
      "cache_read_input_tokens": 14997,
      "output_tokens": 2834,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2834,
          "cache_read_input_tokens": 14997,
          "cache_creation_input_tokens": 14451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14451
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

_source line 24 · 2026-05-30T06:25:52.791Z_

Now I have comprehensive data on all 4 papers. Let me synthesize the analyses into the required format.

```json
[
  {
    "title": "NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models",
    "venue": "ICLR 2025 (Spotlight)",
    "problem_identification": "Decoder-only LLMs used as embedding backbones suffer from (1) pooling that either dilutes information (mean) or has recency bias (EOS-token), (2) causal attention that artificially restricts information flow when full input is available, and (3) task conflicts when mixing retrieval (needs in-batch negatives) with non-retrieval tasks (where in-batch negatives cause label collisions). Identified through systematic ablation of existing decoder-only embedding pipelines.",
    "key_insight": "Removing the causal attention mask during contrastive training (not pretraining) unlocks bidirectional context for embedding tasks, and a latent attention layer using trainable prototype vectors acts as a learned dictionary that extracts task-relevant features before pooling — together enabling a decoder-only LLM to outperform purpose-built embedding models.",
    "innovation_type": "combination",
    "method_summary": "Inserts a cross-attention layer with 512 trainable latent vectors on top of Mistral-7B's final hidden states, where token representations attend to these prototypes before mean-pooling through an MLP. Removes the causal mask in all decoder blocks during training. Uses a two-stage pipeline: Stage 1 trains on 15+ retrieval datasets with in-batch + hard negatives; Stage 2 blends retrieval data with classification/clustering/STS tasks, disabling in-batch negatives for non-retrieval tasks to avoid label collisions. Hard negatives mined via E5-Mistral with a 95% positive-score threshold.",
    "limitations_and_open_questions": "Reviewers noted limited novelty of individual components (bidirectional attention, contrastive training are known) — the contribution is engineering integration. Latent attention gains are modest (+0.6 MTEB points in v2). The complex multi-stage pipeline with synthetic data generation raises reproducibility concerns. No sparse retrieval capability explored.",
    "building_blocks": ["Latent attention pooling architecture", "Bidirectional attention removal for decoder-only embeddings", "Two-stage retrieval-first contrastive instruction-tuning", "Task-aware in-batch negative toggling", "Positive-aware hard negative mining"],
    "relevance_to_seed": "Directly applicable to the dense head design: latent attention pooling and bidirectional attention removal should be adopted for the dense embedding head, and the two-stage curriculum validates the proposed multi-stage training approach."
  },
  {
    "title": "Scaling Laws for Dense Retrieval",
    "venue": "SIGIR 2024 (Best Paper Award)",
    "problem_identification": "Scaling laws were well-established for language modeling but entirely unexplored for dense retrieval, blocked by two challenges: discrete ranking metrics (NDCG, MAP) cannot fit smooth power-law curves, and retrieval performance entangles model size, annotation quantity, and annotation quality.",
    "key_insight": "Contrastive entropy — the contrastive log-likelihood of retrieving a relevant document — serves as a smooth, continuous proxy for ranking metrics, enabling power-law fitting; crucially, because retrieval requires encoding entire corpora, inference cost (not training cost) dominates the budget, inverting the 'bigger is better' wisdom from language modeling.",
    "innovation_type": "new_formulation",
    "method_summary": "Introduces contrastive entropy as a continuous metric linearly correlated with NDCG/MAP, then fits power-law scaling curves L(N)=(A/N)^α+δ and L(D)=(B/D)^β+δ across 24 BERT checkpoints (0.5M–82M params) on MS MARCO and T2Ranking. Derives a joint model-data scaling law and a lifecycle cost model incorporating annotation, training, and inference costs. Discovers that the model-size exponent α≈0.53 is consistent across datasets, and identifies an emergent ability threshold at CE≈0.25 where ranking performance sharply improves.",
    "limitations_and_open_questions": "Experiments limited to BERT-scale encoders (up to 82M params) — unclear if exponents hold for billion-parameter decoder-only models. Sparse retrieval scaling laws are not studied. The irreducible loss δ is dataset-specific and hard to estimate a priori. LLM-generated annotations surpassing human labels at 500k+ scale needs validation across more domains.",
    "building_blocks": ["Contrastive entropy metric for smooth evaluation", "Power-law scaling formulas for model/data size", "Inference-cost-aware budget allocation framework", "LLM-generated annotation scaling analysis"],
    "relevance_to_seed": "Directly informs compute budget allocation for the 3B/8B training — the inference-cost dominance finding suggests favoring the 3B model with more data over the 8B model, and the scaling exponents enable principled resource planning within the 200 H100-hour budget."
  },
  {
    "title": "SPLARE: Learning Retrieval Models with Sparse Autoencoders",
    "venue": "arXiv 2026 (submitted to ICLR 2026)",
    "problem_identification": "SPLADE-style learned sparse retrieval projects onto vocabulary space, inheriting three fundamental limitations: (1) vocabulary tokens are designed for tokenization, not semantic representation, causing redundancy (e.g., 'Indian'/'indian' as separate dimensions); (2) subword tokenizers are biased toward high-resource languages, crippling multilingual transfer; (3) dimensionality is fixed by vocabulary size. The failure is quantified by the absence of any sparse model on the MTEB Multilingual v2 leaderboard.",
    "key_insight": "Sparse autoencoders (SAEs) trained on LLM residual streams for mechanistic interpretability already produce sparse, monosemantic, language-agnostic features — making them a natural drop-in replacement for vocabulary projection in sparse retrieval, with the bonus that only intermediate-layer computation is needed (not full forward pass).",
    "innovation_type": "cross_domain",
    "method_summary": "Replaces SPLADE's vocabulary-space projection with a frozen pre-trained SAE (Llama Scope 131k features) applied at an intermediate LLM layer (~2/3 depth). The LLM backbone is fine-tuned with LoRA under bidirectional attention; SAE is frozen to preserve interpretability and language-agnosticism. Token-level SAE activations are aggregated via SPLADE-style max-pooling with log-saturation. Trained with KL-divergence distillation from a cross-encoder teacher plus FLOPS regularization. Post-hoc Top-K selection (k=40 queries, k=400 documents) controls sparsity at inference without retraining.",
    "limitations_and_open_questions": "Underperforms SPLADE on code retrieval (-1.3 nDCG) due to overly generic SAE features for code semantics — domain-specific SAEs may be needed. Temperature τ is critically SAE-suite-dependent (80 vs 50), requiring careful tuning. How well do frozen SAEs transfer when the backbone is fine-tuned aggressively? Could SAEs be jointly fine-tuned while preserving language-agnosticism?",
    "building_blocks": ["SAE-based sparse representation as vocabulary-projection replacement", "Intermediate-layer feature extraction for efficiency", "Post-hoc Top-K sparsity decoupling from training", "Frozen SAE + LoRA backbone fine-tuning paradigm"],
    "relevance_to_seed": "Presents a fundamentally different sparse head design than SPLADE — if adopted, the sparse head could use SAE decomposition instead of vocabulary projection, potentially improving multilingual generalization; however, the frozen SAE constraint may conflict with bidirectional self-distillation from the dense head."
  },
  {
    "title": "A Survey of Model Architectures in Information Retrieval",
    "venue": "TMLR 2025 (Survey Certification)",
    "problem_identification": "Existing IR surveys conflate architecture with training methodology, making it difficult to understand how the structural design of models has evolved independently. The explosion of LLM-based retrieval approaches (decoder-only adaptations, generative retrieval) further muddies the design space. Identified by the same group behind LACONIC, who needed a clear architectural map to position their own decoder-only sparse retrieval work.",
    "key_insight": "Sparse, dense, and BM25 retrieval are all parametric variations of a unified bi-encoder architecture, differing along two axes — representational basis (dense semantic vs. sparse lexical) and learnedness (data-driven vs. engineered) — but this unification has never been extended to decoder-only backbones, leaving unified sparse+dense decoder-only models as an uncharted architectural gap.",
    "innovation_type": "analysis",
    "method_summary": "Traces IR architectures from Boolean/VSM through BERT bi-encoders to decoder-only LLMs across a taxonomy of cross-encoder vs. bi-encoder designs, with bi-encoders further split into dense, sparse, and multi-vector paradigms. Deliberately separates architecture from training methodology. Catalogs 21+ transformer-based IR models with their architecture type, backbone, and training approach. Identifies decoder-only adaptation as requiring special architectural solutions due to causal attention constraints. Covers hybrid approaches (ColBERT, COIL, SLIM) but only for encoder-only backbones.",
    "limitations_and_open_questions": "Does not cite LACONIC (concurrent work by same group) or address unified sparse+dense decoder-only architectures — the exact gap our proposed work fills. The architecture-vs-training separation, while clarifying, may undersell innovations whose novelty lies precisely in their training curriculum (e.g., LACONIC's two-phase approach). TMLR reviews were not publicly accessible despite Survey Certification.",
    "building_blocks": ["Bi-encoder unifying framework (sparse/dense/BM25 as parametric variations)", "Taxonomy of decoder-only LLM adaptation strategies for retrieval", "Identification of causal attention as architectural bottleneck", "Catalog of hybrid retrieval architectures"],
    "relevance_to_seed": "Provides the definitive architectural positioning framework — our proposed dual-head decoder-only model fills the gap this survey implicitly identifies: no decoder-only architecture simultaneously produces both sparse and dense representations, and the survey's taxonomy confirms this is an unexplored point in the design space."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff5296a7-6347-4d67-9ef6-a1c982eb1e9a",
  "isSidechain": false,
  "requestId": "req_011CbYGugLfo36CUpWm5To2s",
  "type": "assistant",
  "uuid": "907e1579-8497-4849-b0d0-55fef5dd87c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011t7VUMGkeFk38xsDk5HhDZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14451,
      "cache_read_input_tokens": 14997,
      "output_tokens": 2834,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14451,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2834,
          "cache_read_input_tokens": 14997,
          "cache_creation_input_tokens": 14451,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14451
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-30 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "907e1579-8497-4849-b0d0-55fef5dd87c1",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze hybrid retrieval architecture papers for AAAI 2026",
  "sessionId": "71c77089-edc5-4f43-b783-1817930f1119"
}
```

---
