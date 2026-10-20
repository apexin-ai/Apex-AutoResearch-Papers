# Research conversation: Axiom-Grounded Self-Verified Perception for Visual Math Reasoning ## Core Problem Current multimodal math reasoning syst

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/85a148a6-4b0f-4266-a8e7-f5b117647ad4.jsonl`
- **Structured JSON:** [`cd865dc51eae7641b13f.json`](../../sessions/cd/cd865dc51eae7641b13f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:33:40.425Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:33:40.425Z",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "content": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning\n\n## Core Problem\n\nCurrent multimodal math reasoning systems lack mechanisms to verify whether their perceived visual facts are mutually consistent under known mathematical constraints, causing individually plausible but collectively impossible perceptions to cascade into reasoning failures.\n\n## Research Opportunity\n\nMathematical diagrams encode structural invariants (geometric theorems like angle sums, Pythagorean constraints, parallel-line properties; chart constraints like sum-to-total; function constraints like monotonicity) that perceived facts must satisfy. These invariants provide a free, dense, automatically verifiable reward signal for RL-based perception training—requiring no ground truth annotations. This is newly feasible because (1) diagram formalization methods (DFE-GPS, Geoparsing) now reliably extract structured representations, (2) solver-in-the-loop RL has been proven effective for reasoning (FGeo-DRL achieves 86.4% on formalgeo7k via RL in formal geometry environments; sub-goal verifiable rewards unlock geometric reasoning gains), and (3) the perception bottleneck is now definitively established (61% of multimodal math errors are perception errors per MM-MATH).\n\n## Research Landscape\n\nPerception is the confirmed bottleneck: Qwen3-VL leads MathVista at 85.8% but models still fail systematically on vision-dense problems (MathVerse vision-only subsets). Perception-R1 (2025) introduces an LLM-judged visual perception reward but requires pre-collected textual annotations and checks individual claims, not inter-claim consistency. PEARL (2025) uses ground-truth perception checklists as gating rewards (+9.7% on MathVerse) but needs annotated sub-question answers. EVPV (Mar 2026) matches per-claim visual checklists against image-extracted constraints but does not check whether the set of perceived facts satisfies mathematical axioms. GeoDPO (Feb 2026) uses NL-to-DSL translator-guided RL for geometric perception (+26.5% in-domain, +39% downstream) but rewards DSL translation accuracy, not axiom-level consistency of perceived quantitative values. SymHPR (Dec 2025) enforces structural parsing consistency (point-on-line, shape-on-relation) for diagram reconstruction but operates at the topological level, not on quantitative perceived values. PDCR (May 2026) decomposes perception and reasoning rewards via model-internal confidence scores but does not use formal mathematical constraints. SSL-R1 (Apr 2026) derives self-supervised visual RL rewards from generic SSL puzzles (rotation prediction, patch ordering) rather than domain-specific mathematical invariants. M3-ACE (Mar 2026) uses multi-agentic context engineering to rectify perception at inference time but does not train perception via RL rewards. PRCO (Mar 2026) introduces Observer/Solver role separation with utility-based perception rewards but does not exploit mathematical structure for verification. PFlowNet (May 2026) applies variational RL with geometric reward shaping for visually grounded reasoning but 'geometric' refers to reward landscape geometry, not mathematical theorem constraints. No existing work uses mathematical invariant consistency of perceived quantitative facts as a self-supervised perception reward signal.\n\n## Proposed Approach\n\nWe train a VLM (Qwen3-VL-8B as base) to perceive mathematical diagrams accurately using axiom-consistency as a self-supervised RLVR reward, requiring zero ground-truth perception annotations. First, the model extracts structured perception claims (angles, lengths, coordinates, ratios) from diagrams into a formal constraint description language built on FormalGeo/Geoparsing primitives. Second, a lightweight axiom checker—implementing 40+ geometric theorems (angle sums, Pythagorean constraints, parallel-line properties, circle theorems) plus chart and function invariants—evaluates whether the perceived facts jointly satisfy all applicable mathematical constraints, producing a consistency score as the fraction of satisfied axioms. This score serves as a dense, annotation-free perception reward combined with outcome-based answer correctness in GRPO training via the veRL framework. We employ a two-stage curriculum: stage 1 trains perception-only on axiom rewards using diagram-to-formal-language extraction, stage 2 jointly optimizes perception and reasoning with combined axiom + answer rewards. At inference, perceived facts violating axioms trigger iterative re-perception, providing built-in self-verification without external judges.\n\n## Detailed Description\n\nWe propose Axiom-Grounded Self-Verified Perception (ASVP), a self-supervised RLVR framework that trains multimodal models to perceive mathematical diagrams more accurately by exploiting mathematical invariant consistency—without any ground truth annotations. The key insight is that perceived quantitative facts (angles, lengths, areas, ratios) from a diagram must jointly satisfy known mathematical axioms (triangle angle sum equals 180 degrees, Pythagorean theorem, parallel-line properties, chart sum-to-total constraints). We formalize diagram perception as structured extraction into a constraint description language built on FormalGeo and Geoparsing primitives, then compute an axiom-consistency score as the fraction of applicable theorems satisfied by perceived facts. This score serves as a dense, automatic reward signal for GRPO-based RL training of a VLM perception module using veRL. Unlike Perception-R1 and PEARL which require LLM judges or ground-truth checklists, EVPV which checks individual claims without inter-claim consistency, and GeoDPO which rewards DSL translation accuracy, ASVP provides a free, scalable signal targeting the inter-fact coherence gap responsible for cascading reasoning failures. Evaluated on MathVista, MathVerse, GeoQA, and formalgeo7k.\n\n## Key References\n\n- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)\n- PEARL: Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning (arXiv 2025)\n- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026)\n- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025)\n- MM-MATH: Advancing Multimodal Math Evaluation with Process Evaluation and Fine-grained Classification (arXiv 2024)\n- Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver [DFE-GPS] (AAAI 2025)\n- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)\n- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025)\n- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (arXiv 2023)\n- GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning (EMNLP 2025)\n- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026)\n- M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering (arXiv 2026)\n- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026)\n- SSL-R1: Self-Supervised Visual Reinforcement Post-Training for MLLMs (arXiv 2026)\n- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)\n- MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts (ICLR 2024)\n- FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning (arXiv 2024)\n- A Survey of Multimodal Mathematical Reasoning: From Perception, Alignment to Reasoning (arXiv 2026)\n- Figure It Out: Improve the Frontier of Reasoning with Executable Visual States [FIGR] (arXiv 2025)\n- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward (arXiv 2025)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 1200-1500 (8×H100: axiom checker development, 4-5 GRPO training runs at ~30h each, ablation studies, multi-benchmark evaluation), timeline: 8-10 weeks (2 wks axiom checker + data pipeline, 3-4 wks RL training iterations, 2 wks evaluation + paper writing), estimated_gpu_cost: $3,000-$3,750 (at ~$2.50/H100-hr mid-range cloud)\n- **human_in_loop**: gpu_hours: 800-1200 (Claude accelerates axiom checker coding, reward function design, and ablation analysis), timeline: 5-7 weeks (1 wk pipeline with Claude-assisted code generation, 2-3 wks RL training, 1-2 wks evaluation + writing), claude_api_cost: $300-$600, estimated_gpu_cost: $2,000-$3,000\n- **auto_research**: gpu_hours: 1500-2000 (broader axiom-weight tuning, architecture search over reward combinations, automated multi-seed runs), timeline: 3-5 weeks (parallelized experiment sweeps, automated evaluation pipelines), claude_api_cost: $800-$1,200, estimated_gpu_cost: $3,750-$5,000, speed_bottleneck: RL convergence under potentially sparse axiom-violation signals for near-correct perceptions; constraint checker must robustly handle degenerate/ambiguous diagram parses without false negatives\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:33:40.430Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:33:40.430Z",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

## Round 1

46 recorded events

### User

_source line 3 · 2026-05-27T08:33:40.505Z_

# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning

## Core Problem

Current multimodal math reasoning systems lack mechanisms to verify whether their perceived visual facts are mutually consistent under known mathematical constraints, causing individually plausible but collectively impossible perceptions to cascade into reasoning failures.

## Research Opportunity

Mathematical diagrams encode structural invariants (geometric theorems like angle sums, Pythagorean constraints, parallel-line properties; chart constraints like sum-to-total; function constraints like monotonicity) that perceived facts must satisfy. These invariants provide a free, dense, automatically verifiable reward signal for RL-based perception training—requiring no ground truth annotations. This is newly feasible because (1) diagram formalization methods (DFE-GPS, Geoparsing) now reliably extract structured representations, (2) solver-in-the-loop RL has been proven effective for reasoning (FGeo-DRL achieves 86.4% on formalgeo7k via RL in formal geometry environments; sub-goal verifiable rewards unlock geometric reasoning gains), and (3) the perception bottleneck is now definitively established (61% of multimodal math errors are perception errors per MM-MATH).

## Research Landscape

Perception is the confirmed bottleneck: Qwen3-VL leads MathVista at 85.8% but models still fail systematically on vision-dense problems (MathVerse vision-only subsets). Perception-R1 (2025) introduces an LLM-judged visual perception reward but requires pre-collected textual annotations and checks individual claims, not inter-claim consistency. PEARL (2025) uses ground-truth perception checklists as gating rewards (+9.7% on MathVerse) but needs annotated sub-question answers. EVPV (Mar 2026) matches per-claim visual checklists against image-extracted constraints but does not check whether the set of perceived facts satisfies mathematical axioms. GeoDPO (Feb 2026) uses NL-to-DSL translator-guided RL for geometric perception (+26.5% in-domain, +39% downstream) but rewards DSL translation accuracy, not axiom-level consistency of perceived quantitative values. SymHPR (Dec 2025) enforces structural parsing consistency (point-on-line, shape-on-relation) for diagram reconstruction but operates at the topological level, not on quantitative perceived values. PDCR (May 2026) decomposes perception and reasoning rewards via model-internal confidence scores but does not use formal mathematical constraints. SSL-R1 (Apr 2026) derives self-supervised visual RL rewards from generic SSL puzzles (rotation prediction, patch ordering) rather than domain-specific mathematical invariants. M3-ACE (Mar 2026) uses multi-agentic context engineering to rectify perception at inference time but does not train perception via RL rewards. PRCO (Mar 2026) introduces Observer/Solver role separation with utility-based perception rewards but does not exploit mathematical structure for verification. PFlowNet (May 2026) applies variational RL with geometric reward shaping for visually grounded reasoning but 'geometric' refers to reward landscape geometry, not mathematical theorem constraints. No existing work uses mathematical invariant consistency of perceived quantitative facts as a self-supervised perception reward signal.

## Proposed Approach

We train a VLM (Qwen3-VL-8B as base) to perceive mathematical diagrams accurately using axiom-consistency as a self-supervised RLVR reward, requiring zero ground-truth perception annotations. First, the model extracts structured perception claims (angles, lengths, coordinates, ratios) from diagrams into a formal constraint description language built on FormalGeo/Geoparsing primitives. Second, a lightweight axiom checker—implementing 40+ geometric theorems (angle sums, Pythagorean constraints, parallel-line properties, circle theorems) plus chart and function invariants—evaluates whether the perceived facts jointly satisfy all applicable mathematical constraints, producing a consistency score as the fraction of satisfied axioms. This score serves as a dense, annotation-free perception reward combined with outcome-based answer correctness in GRPO training via the veRL framework. We employ a two-stage curriculum: stage 1 trains perception-only on axiom rewards using diagram-to-formal-language extraction, stage 2 jointly optimizes perception and reasoning with combined axiom + answer rewards. At inference, perceived facts violating axioms trigger iterative re-perception, providing built-in self-verification without external judges.

## Detailed Description

We propose Axiom-Grounded Self-Verified Perception (ASVP), a self-supervised RLVR framework that trains multimodal models to perceive mathematical diagrams more accurately by exploiting mathematical invariant consistency—without any ground truth annotations. The key insight is that perceived quantitative facts (angles, lengths, areas, ratios) from a diagram must jointly satisfy known mathematical axioms (triangle angle sum equals 180 degrees, Pythagorean theorem, parallel-line properties, chart sum-to-total constraints). We formalize diagram perception as structured extraction into a constraint description language built on FormalGeo and Geoparsing primitives, then compute an axiom-consistency score as the fraction of applicable theorems satisfied by perceived facts. This score serves as a dense, automatic reward signal for GRPO-based RL training of a VLM perception module using veRL. Unlike Perception-R1 and PEARL which require LLM judges or ground-truth checklists, EVPV which checks individual claims without inter-claim consistency, and GeoDPO which rewards DSL translation accuracy, ASVP provides a free, scalable signal targeting the inter-fact coherence gap responsible for cascading reasoning failures. Evaluated on MathVista, MathVerse, GeoQA, and formalgeo7k.

## Key References

- Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)
- PEARL: Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning (arXiv 2025)
- Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv 2026)
- Hierarchical Process Reward Models are Symbolic Vision Learners [SymHPR] (arXiv 2025)
- MM-MATH: Advancing Multimodal Math Evaluation with Process Evaluation and Fine-grained Classification (arXiv 2024)
- Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver [DFE-GPS] (AAAI 2025)
- Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language (arXiv 2026)
- TrustGeoGen: Formal-Verified Data Engine for Trustworthy Multi-modal Geometric Problem Solving (arXiv 2025)
- FormalGeo: An Extensible Formalized Framework for Olympiad Geometric Problem Solving (arXiv 2023)
- GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning (EMNLP 2025)
- Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning [GeoDPO] (arXiv 2026)
- M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering (arXiv 2026)
- PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning (arXiv 2026)
- SSL-R1: Self-Supervised Visual Reinforcement Post-Training for MLLMs (arXiv 2026)
- Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)
- MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts (ICLR 2024)
- FGeo-DRL: Deductive Reasoning for Geometric Problems through Deep Reinforcement Learning (arXiv 2024)
- A Survey of Multimodal Mathematical Reasoning: From Perception, Alignment to Reasoning (arXiv 2026)
- Figure It Out: Improve the Frontier of Reasoning with Executable Visual States [FIGR] (arXiv 2025)
- Milestones over Outcome: Unlocking Geometric Reasoning with Sub-Goal Verifiable Reward (arXiv 2025)

## Resource Estimate

- **manual**: gpu_hours: 1200-1500 (8×H100: axiom checker development, 4-5 GRPO training runs at ~30h each, ablation studies, multi-benchmark evaluation), timeline: 8-10 weeks (2 wks axiom checker + data pipeline, 3-4 wks RL training iterations, 2 wks evaluation + paper writing), estimated_gpu_cost: $3,000-$3,750 (at ~$2.50/H100-hr mid-range cloud)
- **human_in_loop**: gpu_hours: 800-1200 (Claude accelerates axiom checker coding, reward function design, and ablation analysis), timeline: 5-7 weeks (1 wk pipeline with Claude-assisted code generation, 2-3 wks RL training, 1-2 wks evaluation + writing), claude_api_cost: $300-$600, estimated_gpu_cost: $2,000-$3,000
- **auto_research**: gpu_hours: 1500-2000 (broader axiom-weight tuning, architecture search over reward combinations, automated multi-seed runs), timeline: 3-5 weeks (parallelized experiment sweeps, automated evaluation pipelines), claude_api_cost: $800-$1,200, estimated_gpu_cost: $3,750-$5,000, speed_bottleneck: RL convergence under potentially sparse axiom-violation signals for near-correct perceptions; constraint checker must robustly handle degenerate/ambiguous diagram parses without false negatives


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "55f8eaad-46e0-439d-9b4a-d5df5aec9077",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:33:40.503Z_

```json
{
  "parentUuid": "55f8eaad-46e0-439d-9b4a-d5df5aec9077",
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
  "uuid": "c2c12feb-9c28-4e69-bc20-b1d3b8962f01",
  "timestamp": "2026-05-27T08:33:40.503Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:33:40.503Z_

```json
{
  "parentUuid": "c2c12feb-9c28-4e69-bc20-b1d3b8962f01",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "2d87da67-1823-4532-af06-77a0a52979ec",
  "timestamp": "2026-05-27T08:33:40.503Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
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
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Assistant

_source line 7 · 2026-05-27T08:33:50.844Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "发掘 agent" (Discovery Agent) to analyze this research proposal about "Axiom-Grounded Self-Verified Perception for Visual Math Reasoning" (ASVP). 

My job is to:
1. First do WebSearch-based literature research (3-5 searches)
2. Evaluate the proposal's novelty, significance, and related work differentiation
3. Try to find ways to raise the ceiling of the idea
4. Be objective - if it's already solid, say so

Let me first understand the proposal:


The core insight is that vision language models perceive individual visual math facts but don't verify whether they're mutually consistent under mathematical constraints. The proposed solution leverages mathematical axiom consistency—like the constraint that angles in a triangle sum to 180°—as a self-supervised reward signal to improve perception training. The key novelty claim is that no existing work uses mathematical invariant consistency of perceived quantitative facts as a self-supervised perception reward signal. The method would extract structured perception claims, have an axiom checker evaluate their consistency, and use that as a GRPO reward signal.

Now I need to search the literature to understand what's already been done in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d87da67-1823-4532-af06-77a0a52979ec",
  "isSidechain": false,
  "requestId": "req_011CbSmKkwednpjLmiKbDnTf",
  "type": "assistant",
  "uuid": "81a695d4-cb83-41ee-8e10-2ce313ecad33",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VwCirqdZpjVUPah8JDuKgi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6909,
      "cache_read_input_tokens": 11014,
      "output_tokens": 381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 381,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 6909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6909
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

_source line 8 · 2026-05-27T08:33:50.846Z_

I'll start by reading the proposal carefully and then conducting targeted web searches to understand the current research landscape before making any judgments.

Let me do the prerequisite literature research first:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81a695d4-cb83-41ee-8e10-2ce313ecad33",
  "isSidechain": false,
  "requestId": "req_011CbSmKkwednpjLmiKbDnTf",
  "type": "assistant",
  "uuid": "350464f6-556f-4ed3-aec9-e5d41daedb2e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VwCirqdZpjVUPah8JDuKgi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6909,
      "cache_read_input_tokens": 11014,
      "output_tokens": 381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 381,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 6909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6909
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

_source line 9 · 2026-05-27T08:33:50.848Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01N5a8QiE4owb8Z2gxwwen8c`</summary>

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
  "parentUuid": "350464f6-556f-4ed3-aec9-e5d41daedb2e",
  "isSidechain": false,
  "requestId": "req_011CbSmKkwednpjLmiKbDnTf",
  "type": "assistant",
  "uuid": "fd90a646-20ff-4232-87c7-132a9c0b7118",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VwCirqdZpjVUPah8JDuKgi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6909,
      "cache_read_input_tokens": 11014,
      "output_tokens": 381,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 381,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 6909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6909
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

_source line 10 · 2026-05-27T08:33:50.857Z_

<details><summary>↩ Tool result · `toolu_01N5a8QiE4owb8Z2gxwwen8c`</summary>

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
  "parentUuid": "fd90a646-20ff-4232-87c7-132a9c0b7118",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "8fbcfc3d-10c6-4a04-8095-212faee60b31",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "fd90a646-20ff-4232-87c7-132a9c0b7118",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-27T08:33:53.981Z_

Now let me conduct the targeted literature searches. I'll run multiple searches in parallel to cover the key aspects of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8fbcfc3d-10c6-4a04-8095-212faee60b31",
  "isSidechain": false,
  "requestId": "req_011CbSmLXV3kfFFHnqLfqYAj",
  "type": "assistant",
  "uuid": "6e02604d-46e2-4e33-a9f6-e97e1aa597b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hr8SZRd5zYYztpUmJET2Vw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 17923,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 908,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 17923,
          "cache_creation_input_tokens": 908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 908
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

_source line 12 · 2026-05-27T08:33:54.383Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uq1ARkMiMyRufzdPDvC5Bj`</summary>

```json
{
  "query": "axiom consistency self-supervised reward visual math reasoning VLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e02604d-46e2-4e33-a9f6-e97e1aa597b5",
  "isSidechain": false,
  "requestId": "req_011CbSmLXV3kfFFHnqLfqYAj",
  "type": "assistant",
  "uuid": "8444679e-0a83-485e-b66a-d3797888eb5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hr8SZRd5zYYztpUmJET2Vw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 908,
      "cache_read_input_tokens": 17923,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 908,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 17923,
          "cache_creation_input_tokens": 908,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 908
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
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem  Current multimodal math reasoning systems lack mechanisms to verify whether their perceived visual facts are mutua…",
  "leafUuid": "8444679e-0a83-485e-b66a-d3797888eb5a",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Tool result

_source line 15 · 2026-05-27T08:34:01.938Z_

<details><summary>↩ Tool result · `toolu_01Uq1ARkMiMyRufzdPDvC5Bj`</summary>

```text
Web search results for query: "axiom consistency self-supervised reward visual math reasoning VLM 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2509.25787v4"},{"title":"Self-Rewarding Vision-Language Model via Reasoning Decomposition","url":"https://arxiv.org/pdf/2508.19652"},{"title":"V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://arxiv.org/pdf/2601.10094"},{"title":"Through the Lens of Contrast: Self-Improving Visual Reasoning in VLMs","url":"https://arxiv.org/html/2603.02556"},{"title":"RISE: Enhancing VLM Image Annotation with Self-Supervised Reasoning","url":"https://arxiv.org/pdf/2508.13229"},{"title":"Through the Lens of Contrast: Self-Improving Visual Reasoning in VLMs","url":"https://arxiv.org/pdf/2603.02556"}]

I found several relevant research papers on this topic. Here's what the search results reveal:

## Self-Supervised Approaches for VLM Reasoning

Recent work has turned toward self-supervised post-training strategies that exploit the internal model outputs without reliance on ground-truth annotations. Self-consistency leverages the "wisdom of the crowd" effect within the model itself by generating multiple diverse reasoning traces for the same problem, with the final answer determined by aggregating these outputs, often through majority voting.

## Self-Rewarding VLMs

R1-style reinforcement learning (RL) methods have been shown to improve the reasoning abilities of VLMs across diverse tasks, though these methods often encourage "thinking over seeing" that lean heavily on language reasoning while underutilizing visual perception, making VLMs susceptible to reward hacking and spurious effects.

## Zero-Annotation Self-Improvement

V-Zero is a post-training framework that facilitates self-improvement using exclusively unlabeled images by establishing a co-evolutionary loop between a Questioner and Solver both trained with GRPO using internally generated reward signals.

## Visual Reasoning Improvements

Self-improving approaches form a prominent branch mainly because they can be easily applied and extended without external reward models, predefined step decomposition, or specially designed reasoning structures.

These papers from 2025-2026 demonstrate significant progress in developing self-supervised and self-rewarding mechanisms for improving VLM reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8444679e-0a83-485e-b66a-d3797888eb5a",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "901d28ff-75ec-4737-a82e-1f8521f5698e",
  "toolUseResult": {
    "query": "axiom consistency self-supervised reward visual math reasoning VLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QPMUXpJKaZkDLF78JhUd6r",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2509.25787v4"
          },
          {
            "title": "Self-Rewarding Vision-Language Model via Reasoning Decomposition",
            "url": "https://arxiv.org/pdf/2508.19652"
          },
          {
            "title": "V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://arxiv.org/pdf/2601.10094"
          },
          {
            "title": "Through the Lens of Contrast: Self-Improving Visual Reasoning in VLMs",
            "url": "https://arxiv.org/html/2603.02556"
          },
          {
            "title": "RISE: Enhancing VLM Image Annotation with Self-Supervised Reasoning",
            "url": "https://arxiv.org/pdf/2508.13229"
          },
          {
            "title": "Through the Lens of Contrast: Self-Improving Visual Reasoning in VLMs",
            "url": "https://arxiv.org/pdf/2603.02556"
          }
        ]
      },
      "I found several relevant research papers on this topic. Here's what the search results reveal:\n\n## Self-Supervised Approaches for VLM Reasoning\n\nRecent work has turned toward self-supervised post-training strategies that exploit the internal model outputs without reliance on ground-truth annotations. Self-consistency leverages the \"wisdom of the crowd\" effect within the model itself by generating multiple diverse reasoning traces for the same problem, with the final answer determined by aggregating these outputs, often through majority voting.\n\n## Self-Rewarding VLMs\n\nR1-style reinforcement learning (RL) methods have been shown to improve the reasoning abilities of VLMs across diverse tasks, though these methods often encourage \"thinking over seeing\" that lean heavily on language reasoning while underutilizing visual perception, making VLMs susceptible to reward hacking and spurious effects.\n\n## Zero-Annotation Self-Improvement\n\nV-Zero is a post-training framework that facilitates self-improvement using exclusively unlabeled images by establishing a co-evolutionary loop between a Questioner and Solver both trained with GRPO using internally generated reward signals.\n\n## Visual Reasoning Improvements\n\nSelf-improving approaches form a prominent branch mainly because they can be easily applied and extended without external reward models, predefined step decomposition, or specially designed reasoning structures.\n\nThese papers from 2025-2026 demonstrate significant progress in developing self-supervised and self-rewarding mechanisms for improving VLM reasoning capabilities."
    ],
    "durationSeconds": 7.547324483999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8444679e-0a83-485e-b66a-d3797888eb5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-27T08:34:04.424Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DSi8wKnZ7SQBY5AUx9gZeM`</summary>

```json
{
  "query": "Perception-R1 PEARL perception reward multimodal math reasoning RLVR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "901d28ff-75ec-4737-a82e-1f8521f5698e",
  "isSidechain": false,
  "requestId": "req_011CbSmMLS4Xd5GL7qrYwNrF",
  "type": "assistant",
  "uuid": "1c14055c-100e-4cc6-a98c-27fc32634975",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E7DBpqNRgyGaappYLEskXp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 711,
      "cache_read_input_tokens": 18831,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 711,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 18831,
          "cache_creation_input_tokens": 711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 711
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

_source line 17 · 2026-05-27T08:34:10.105Z_

<details><summary>↩ Tool result · `toolu_01DSi8wKnZ7SQBY5AUx9gZeM`</summary>

```text
Web search results for query: "Perception-R1 PEARL perception reward multimodal math reasoning RLVR 2025"

Links: [{"title":"Enhancing MLLM Reasoning with Visual Rewards","url":"https://www.emergentmind.com/papers/2506.07218"},{"title":"PERCEPTION-R1: ADVANCING MULTIMODAL REASON","url":"https://openreview.net/pdf/5bd5dd88b61fe3cdc20a2bfc0b357b67cd6cd0c4.pdf"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward [Quick Review]","url":"https://liner.com/review/perceptionr1-advancing-multimodal-reasoning-capabilities-of-mllms-via-visual-perception"},{"title":"[2506.07218] Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/abs/2506.07218"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/html/2506.07218v2"},{"title":"ICLR Poster Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://iclr.cc/virtual/2026/poster/10010085"},{"title":"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward","url":"https://arxiv.org/pdf/2506.07218"}]

Based on the search results, here's what I found about Perception-R1:

## Overview

Perception-R1 is a framework that adds visual perception rewards in RLVR to boost MLLMs' multimodal reasoning with state-of-the-art performance.

## The Problem It Addresses

Existing works largely overlook the enhancement of multimodal perception capabilities in MLLMs, which serve as a core prerequisite and foundational component of complex multimodal reasoning. Existing RLVR methods fail to effectively enhance the multimodal perception capabilities of MLLMs, thereby limiting their further improvement in multimodal reasoning.

## The Solution

Perception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive the visual content accurately, thereby can effectively incentivizing both their multimodal perception and reasoning capabilities. 

The approach first collects textual visual annotations from the CoT trajectories of multimodal problems which serve as visual references for reward assignment. During RLVR training, a judging LLM assesses the consistency between the visual annotations and the responses generated by MLLM, and assigns the visual perception reward based on these consistency judgments.

## Results

Extensive experiments on several multimodal reasoning benchmarks demonstrate the effectiveness of Perception-R1, which achieves state-of-the-art performance on most benchmarks using only 1,442 training data.

The code and dataset are available at GitHub: https://github.com/tongxiao2002/Perception-R1


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c14055c-100e-4cc6-a98c-27fc32634975",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "c0abe76c-7734-4220-9527-c480c19df18f",
  "toolUseResult": {
    "query": "Perception-R1 PEARL perception reward multimodal math reasoning RLVR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T8dnQJdW7urL2CERT4HNq4",
        "content": [
          {
            "title": "Enhancing MLLM Reasoning with Visual Rewards",
            "url": "https://www.emergentmind.com/papers/2506.07218"
          },
          {
            "title": "PERCEPTION-R1: ADVANCING MULTIMODAL REASON",
            "url": "https://openreview.net/pdf/5bd5dd88b61fe3cdc20a2bfc0b357b67cd6cd0c4.pdf"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward [Quick Review]",
            "url": "https://liner.com/review/perceptionr1-advancing-multimodal-reasoning-capabilities-of-mllms-via-visual-perception"
          },
          {
            "title": "[2506.07218] Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/abs/2506.07218"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/html/2506.07218v2"
          },
          {
            "title": "ICLR Poster Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://iclr.cc/virtual/2026/poster/10010085"
          },
          {
            "title": "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward",
            "url": "https://arxiv.org/pdf/2506.07218"
          }
        ]
      },
      "Based on the search results, here's what I found about Perception-R1:\n\n## Overview\n\nPerception-R1 is a framework that adds visual perception rewards in RLVR to boost MLLMs' multimodal reasoning with state-of-the-art performance.\n\n## The Problem It Addresses\n\nExisting works largely overlook the enhancement of multimodal perception capabilities in MLLMs, which serve as a core prerequisite and foundational component of complex multimodal reasoning. Existing RLVR methods fail to effectively enhance the multimodal perception capabilities of MLLMs, thereby limiting their further improvement in multimodal reasoning.\n\n## The Solution\n\nPerception-R1 introduces a novel visual perception reward that explicitly encourages MLLMs to perceive the visual content accurately, thereby can effectively incentivizing both their multimodal perception and reasoning capabilities. \n\nThe approach first collects textual visual annotations from the CoT trajectories of multimodal problems which serve as visual references for reward assignment. During RLVR training, a judging LLM assesses the consistency between the visual annotations and the responses generated by MLLM, and assigns the visual perception reward based on these consistency judgments.\n\n## Results\n\nExtensive experiments on several multimodal reasoning benchmarks demonstrate the effectiveness of Perception-R1, which achieves state-of-the-art performance on most benchmarks using only 1,442 training data.\n\nThe code and dataset are available at GitHub: https://github.com/tongxiao2002/Perception-R1"
    ],
    "durationSeconds": 5.676354074999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1c14055c-100e-4cc6-a98c-27fc32634975",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-27T08:34:12.921Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011XmZstFuf76RfGL4ixvkJN`</summary>

```json
{
  "query": "GeoDPO geometric perception VLM reinforcement learning translator-guided DSL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0abe76c-7734-4220-9527-c480c19df18f",
  "isSidechain": false,
  "requestId": "req_011CbSmMwLmucjkUkePF5GiR",
  "type": "assistant",
  "uuid": "4dd8cf4a-83bf-497b-9893-cee429163b4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JW1xgNjGFJo2Up5ajgqYbt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 862,
      "cache_read_input_tokens": 19542,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 862,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 19542,
          "cache_creation_input_tokens": 862,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 862
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

_source line 19 · 2026-05-27T08:34:19.960Z_

<details><summary>↩ Tool result · `toolu_011XmZstFuf76RfGL4ixvkJN`</summary>

```text
Web search results for query: "GeoDPO geometric perception VLM reinforcement learning translator-guided DSL 2026"

Links: [{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=O70LkLl3gW"},{"title":"[2602.22703] Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/abs/2602.22703"},{"title":"Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning","url":"https://arxiv.org/pdf/2602.22703"},{"title":"Does VLM Always Fail in Solving Geometry Problems? GEODPO: Starting from \"Seeing\", Using Structured Representation + DPO Optimization to Enable Model Understanding before Reasoning","url":"https://eu.36kr.com/en/p/3745344269893891"},{"title":"GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning","url":"https://arxiv.org/html/2509.17437v1"},{"title":"GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning","url":"https://arxiv.org/pdf/2509.17437"}]

Based on the search results, here's what I found about GeoDPO:

## Overview

GeoDPO addresses the challenge that vision-language models (VLMs) often struggle with geometric reasoning due to their limited perception of fundamental diagram elements. To tackle this, researchers introduced GeoPerceive, a benchmark comprising diagram instances paired with domain-specific language (DSL) representations.

## The GeoDPO Framework

GeoDPO is a translator-guided reinforcement learning framework proposed to enhance the geometric perception capabilities of VLMs. GeoDPO employs an NL-to-DSL translator trained on synthetic pairs generated by the data engine of GeoPerceive to bridge natural language and DSL, facilitating the computation of fine-grained, DSL-level scores which serve as reward signals in reinforcement learning.

## Key Results

Experimental results demonstrate that GeoDPO achieves substantial gains: +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks. These findings underscore the superior performance and generalization ability of GeoDPO over supervised fine-tuning (SFT).

The research was published in February 2026, with the paper available on arXiv and OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4dd8cf4a-83bf-497b-9893-cee429163b4e",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "db878f36-eece-4b90-bfa8-e2acd07c1958",
  "toolUseResult": {
    "query": "GeoDPO geometric perception VLM reinforcement learning translator-guided DSL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WLJaE7mj7QZmhH1tyoVVRE",
        "content": [
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning | OpenReview",
            "url": "https://openreview.net/forum?id=O70LkLl3gW"
          },
          {
            "title": "[2602.22703] Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/abs/2602.22703"
          },
          {
            "title": "Enhancing Geometric Perception in VLMs via Translator-Guided Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.22703"
          },
          {
            "title": "Does VLM Always Fail in Solving Geometry Problems? GEODPO: Starting from \"Seeing\", Using Structured Representation + DPO Optimization to Enable Model Understanding before Reasoning",
            "url": "https://eu.36kr.com/en/p/3745344269893891"
          },
          {
            "title": "GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning",
            "url": "https://arxiv.org/html/2509.17437v1"
          },
          {
            "title": "GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning",
            "url": "https://arxiv.org/pdf/2509.17437"
          }
        ]
      },
      "Based on the search results, here's what I found about GeoDPO:\n\n## Overview\n\nGeoDPO addresses the challenge that vision-language models (VLMs) often struggle with geometric reasoning due to their limited perception of fundamental diagram elements. To tackle this, researchers introduced GeoPerceive, a benchmark comprising diagram instances paired with domain-specific language (DSL) representations.\n\n## The GeoDPO Framework\n\nGeoDPO is a translator-guided reinforcement learning framework proposed to enhance the geometric perception capabilities of VLMs. GeoDPO employs an NL-to-DSL translator trained on synthetic pairs generated by the data engine of GeoPerceive to bridge natural language and DSL, facilitating the computation of fine-grained, DSL-level scores which serve as reward signals in reinforcement learning.\n\n## Key Results\n\nExperimental results demonstrate that GeoDPO achieves substantial gains: +26.5% on in-domain data, +8.0% on out-of-domain data, and +39.0% on downstream reasoning tasks. These findings underscore the superior performance and generalization ability of GeoDPO over supervised fine-tuning (SFT).\n\nThe research was published in February 2026, with the paper available on arXiv and OpenReview."
    ],
    "durationSeconds": 7.035998558000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4dd8cf4a-83bf-497b-9893-cee429163b4e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-27T08:34:22.480Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V8u4JfB9ev43zkbNJURzAe`</summary>

```json
{
  "query": "formal geometric constraint verification diagram parsing self-supervised learning FormalGeo 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db878f36-eece-4b90-bfa8-e2acd07c1958",
  "isSidechain": false,
  "requestId": "req_011CbSmNfT5jLDCWaasayKeK",
  "type": "assistant",
  "uuid": "c9a3a485-dd1b-49a5-bbbb-569386cf3ee1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019w7h64G6PqMhCNshWAKNd8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 723,
      "cache_read_input_tokens": 20404,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 723,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 20404,
          "cache_creation_input_tokens": 723,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 723
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

_source line 21 · 2026-05-27T08:34:34.442Z_

<details><summary>↩ Tool result · `toolu_01V8u4JfB9ev43zkbNJURzAe`</summary>

```text
Web search results for query: "formal geometric constraint verification diagram parsing self-supervised learning FormalGeo 2025 2026"

Links: [{"title":"FormalGeo: Formal representation and solving for Euclidean plane geometry problems","url":"https://formalgeo.github.io/"},{"title":"FormalGeo: An Extensible Formalized Framework For Olympiad Geometric Problem","url":"https://arxiv.org/pdf/2310.18021"},{"title":"FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems | MDPI","url":"https://www.mdpi.com/2073-8994/17/1/8"},{"title":"Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language","url":"https://arxiv.org/html/2604.11600"},{"title":"GeoFM: Enhancing Geometric Reasoning of MLLMs via Synthetic Data Generation through Formal Language","url":"https://arxiv.org/html/2510.27448v1"},{"title":"FormalGeo: An Extensible Formalized Framework For Olympiad Geometric Problem Solving","url":"https://arxiv.org/html/2310.18021v6"},{"title":"Hierarchical Process Reward Models are Symbolic Vision Learners","url":"https://arxiv.org/pdf/2512.03126"}]

Based on the web search results, here's what I found about formal geometric constraint verification, diagram parsing, and self-supervised learning related to FormalGeo in 2025-2026:

## FormalGeo Framework

FGeo-Parser is an enhanced geometric problem parsing method that converts problem diagrams and text into the formal language of the FormalGeo. The diagram parser leverages BLIP to generate construction CDL and image CDL, while text parser employs T5 to produce text CDL and goal CDL using symmetric encoder–decoder architecture.

## Recent Developments

A paper titled "Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver" was accepted by ICASSP 2025. Additionally, the FormalGeo7K dataset was refined and supplemented to create the FormalGeo7K-v2 dataset.

## Extended Applications

A unified formal language has been designed that integrates plane and solid geometry, with a large-scale dataset (GDP-29K) comprising 20k plane and 9k solid geometry samples. A training paradigm combining Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards has been proposed.

## Self-Supervised Learning Approaches

Recent work extends the auto-encoder paradigm to symbolic latent spaces, where the bottleneck is composed of explicit geometric primitives rather than continuous vectors, representing an advancement in self-supervised visual learning for geometry problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9a3a485-dd1b-49a5-bbbb-569386cf3ee1",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "f534ad35-f511-4314-8882-7d9e5571bbb3",
  "toolUseResult": {
    "query": "formal geometric constraint verification diagram parsing self-supervised learning FormalGeo 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SYDjxBZkgQYLtRrfEVPdgA",
        "content": [
          {
            "title": "FormalGeo: Formal representation and solving for Euclidean plane geometry problems",
            "url": "https://formalgeo.github.io/"
          },
          {
            "title": "FormalGeo: An Extensible Formalized Framework For Olympiad Geometric Problem",
            "url": "https://arxiv.org/pdf/2310.18021"
          },
          {
            "title": "FGeo-Parser: Autoformalization and Solution of Plane Geometric Problems | MDPI",
            "url": "https://www.mdpi.com/2073-8994/17/1/8"
          },
          {
            "title": "Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language",
            "url": "https://arxiv.org/html/2604.11600"
          },
          {
            "title": "GeoFM: Enhancing Geometric Reasoning of MLLMs via Synthetic Data Generation through Formal Language",
            "url": "https://arxiv.org/html/2510.27448v1"
          },
          {
            "title": "FormalGeo: An Extensible Formalized Framework For Olympiad Geometric Problem Solving",
            "url": "https://arxiv.org/html/2310.18021v6"
          },
          {
            "title": "Hierarchical Process Reward Models are Symbolic Vision Learners",
            "url": "https://arxiv.org/pdf/2512.03126"
          }
        ]
      },
      "Based on the web search results, here's what I found about formal geometric constraint verification, diagram parsing, and self-supervised learning related to FormalGeo in 2025-2026:\n\n## FormalGeo Framework\n\nFGeo-Parser is an enhanced geometric problem parsing method that converts problem diagrams and text into the formal language of the FormalGeo. The diagram parser leverages BLIP to generate construction CDL and image CDL, while text parser employs T5 to produce text CDL and goal CDL using symmetric encoder–decoder architecture.\n\n## Recent Developments\n\nA paper titled \"Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver\" was accepted by ICASSP 2025. Additionally, the FormalGeo7K dataset was refined and supplemented to create the FormalGeo7K-v2 dataset.\n\n## Extended Applications\n\nA unified formal language has been designed that integrates plane and solid geometry, with a large-scale dataset (GDP-29K) comprising 20k plane and 9k solid geometry samples. A training paradigm combining Supervised Fine-Tuning with Reinforcement Learning via Verifiable Rewards has been proposed.\n\n## Self-Supervised Learning Approaches\n\nRecent work extends the auto-encoder paradigm to symbolic latent spaces, where the bottleneck is composed of explicit geometric primitives rather than continuous vectors, representing an advancement in self-supervised visual learning for geometry problems."
    ],
    "durationSeconds": 11.955848343999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c9a3a485-dd1b-49a5-bbbb-569386cf3ee1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T08:34:37.082Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WWMaszeVeMVspzJMMUkqaT`</summary>

```json
{
  "query": "V-Zero self-improving VLM zero annotation GRPO unlabeled images 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f534ad35-f511-4314-8882-7d9e5571bbb3",
  "isSidechain": false,
  "requestId": "req_011CbSmPjPF3pZdG6dpa3WGH",
  "type": "assistant",
  "uuid": "0896ae7b-dcaf-473a-9e92-c63151094048",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UX8EXY8LZTM6YFXAa7b2in",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 21127,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 750,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 21127,
          "cache_creation_input_tokens": 750,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 750
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

_source line 23 · 2026-05-27T08:34:46.668Z_

<details><summary>↩ Tool result · `toolu_01WWMaszeVeMVspzJMMUkqaT`</summary>

```text
Web search results for query: "V-Zero self-improving VLM zero annotation GRPO unlabeled images 2026"

Links: [{"title":"[2601.10094] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://arxiv.org/abs/2601.10094"},{"title":"[Literature Review] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://www.themoonlight.io/en/review/v-zero-self-improving-multimodal-reasoning-with-zero-annotation"},{"title":"Jingyuan Hu's research works","url":"https://www.researchgate.net/scientific-contributions/Jingyuan-Hu-2337177897"},{"title":"GitHub - SatonoDia/V-Zero · GitHub","url":"https://github.com/SatonoDia/V-Zero"},{"title":"V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation","url":"https://arxiv.org/pdf/2601.10094"},{"title":"Han Wang","url":"https://www.catalyzex.com/author/Han%20Wang"},{"title":"GitHub - wangqinsi1/Vision-Zero: [ICLR 2026] Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play. · GitHub","url":"https://github.com/wangqinsi1/Vision-Zero"},{"title":"Vision-Zero: Scalable VLM Self-Evolution via Multi-Agent Self-Play | OpenReview","url":"https://openreview.net/forum?id=s00SNXREV6"},{"title":"Self-Evolving Vision-Language Models for Image Quality Assessment via Voting and Ranking","url":"https://arxiv.org/pdf/2509.25787"}]

Based on the search results, here's what I found about V-Zero:

V-Zero is a general post-training framework that facilitates self-improvement using exclusively unlabeled images. It overcomes the limitation of state-of-the-art approaches that rely heavily on large-scale human-annotated datasets, which are costly and time-consuming to acquire.

## Key Architecture

V-Zero establishes a co-evolutionary loop by instantiating two distinct roles: a Questioner and a Solver, where the Questioner learns to synthesize high-quality, challenging questions by leveraging a dual-track reasoning reward that contrasts intuitive guesses with reasoned results. The Solver is optimized using pseudo-labels derived from majority voting over its own sampled responses.

## Training Method

Both roles are trained iteratively via Group Relative Policy Optimization (GRPO), driving a cycle of mutual enhancement. V-Zero achieves self-improvement from unlabeled images via a dynamic co-evolutionary loop, where reward signals are internally generated through the interaction between a Questioner and a Solver.

The paper was published on January 15, 2026, and demonstrates a novel approach to vision-language model training that eliminates the need for human annotations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0896ae7b-dcaf-473a-9e92-c63151094048",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "e3e7e960-e615-4c6d-a82e-29c56993e9b2",
  "toolUseResult": {
    "query": "V-Zero self-improving VLM zero annotation GRPO unlabeled images 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RUm4UjYq5wfMrYFPvoqi89",
        "content": [
          {
            "title": "[2601.10094] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://arxiv.org/abs/2601.10094"
          },
          {
            "title": "[Literature Review] V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://www.themoonlight.io/en/review/v-zero-self-improving-multimodal-reasoning-with-zero-annotation"
          },
          {
            "title": "Jingyuan Hu's research works",
            "url": "https://www.researchgate.net/scientific-contributions/Jingyuan-Hu-2337177897"
          },
          {
            "title": "GitHub - SatonoDia/V-Zero · GitHub",
            "url": "https://github.com/SatonoDia/V-Zero"
          },
          {
            "title": "V-Zero: Self-Improving Multimodal Reasoning with Zero Annotation",
            "url": "https://arxiv.org/pdf/2601.10094"
          },
          {
            "title": "Han Wang",
            "url": "https://www.catalyzex.com/author/Han%20Wang"
          },
          {
            "title": "GitHub - wangqinsi1/Vision-Zero: [ICLR 2026] Vision-Zero: Scalable VLM Self-Improvement via Strategic Gamified Self-Play. · GitHub",
            "url": "https://github.com/wangqinsi1/Vision-Zero"
          },
          {
            "title": "Vision-Zero: Scalable VLM Self-Evolution via Multi-Agent Self-Play | OpenReview",
            "url": "https://openreview.net/forum?id=s00SNXREV6"
          },
          {
            "title": "Self-Evolving Vision-Language Models for Image Quality Assessment via Voting and Ranking",
            "url": "https://arxiv.org/pdf/2509.25787"
          }
        ]
      },
      "Based on the search results, here's what I found about V-Zero:\n\nV-Zero is a general post-training framework that facilitates self-improvement using exclusively unlabeled images. It overcomes the limitation of state-of-the-art approaches that rely heavily on large-scale human-annotated datasets, which are costly and time-consuming to acquire.\n\n## Key Architecture\n\nV-Zero establishes a co-evolutionary loop by instantiating two distinct roles: a Questioner and a Solver, where the Questioner learns to synthesize high-quality, challenging questions by leveraging a dual-track reasoning reward that contrasts intuitive guesses with reasoned results. The Solver is optimized using pseudo-labels derived from majority voting over its own sampled responses.\n\n## Training Method\n\nBoth roles are trained iteratively via Group Relative Policy Optimization (GRPO), driving a cycle of mutual enhancement. V-Zero achieves self-improvement from unlabeled images via a dynamic co-evolutionary loop, where reward signals are internally generated through the interaction between a Questioner and a Solver.\n\nThe paper was published on January 15, 2026, and demonstrates a novel approach to vision-language model training that eliminates the need for human annotations."
    ],
    "durationSeconds": 9.580875634999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0896ae7b-dcaf-473a-9e92-c63151094048",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
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
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem  Current multimodal math reasoning systems lack mechanisms to verify whether their perceived visual facts are mutua…",
  "leafUuid": "e3e7e960-e615-4c6d-a82e-29c56993e9b2",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Tool call

_source line 26 · 2026-05-27T08:34:54.826Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RnYVFjbVAxG6r53gb4MyDh`</summary>

```json
{
  "query": "EVPV \"explicit visual premise verification\" VLM process reward 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3e7e960-e615-4c6d-a82e-29c56993e9b2",
  "isSidechain": false,
  "requestId": "req_011CbSmQsmoQrSKxr1ZrAx9j",
  "type": "assistant",
  "uuid": "c1d2e3a8-a873-41b8-9381-914b3747e0c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CPCznVU41fgwuqbrjr96PT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 819,
      "cache_read_input_tokens": 21877,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 819,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 21877,
          "cache_creation_input_tokens": 819,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 819
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

_source line 27 · 2026-05-27T08:35:02.142Z_

<details><summary>↩ Tool result · `toolu_01RnYVFjbVAxG6r53gb4MyDh`</summary>

```text
Web search results for query: "EVPV "explicit visual premise verification" VLM process reward 2026"

Links: [{"title":"[2603.16253] Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/abs/2603.16253"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models","url":"https://arxiv.org/html/2603.16253"},{"title":"Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models","url":"https://arxiv.org/pdf/2603.16253"},{"title":"GitHub - Qwen-Applications/EVPV-PRM · GitHub","url":"https://github.com/Qwen-Applications/EVPV-PRM"},{"title":"CAPTION AS REWARD: ENHANCING VISION","url":"https://openreview.net/pdf/8fdf67ae5eeb96964eb7b8af53323db8d9050074.pdf"}]

Based on the search results, here's what I found about EVPV:

Explicit Visual Premise Verification (EVPV) is a lightweight verification interface that conditions step scoring on the reliability of the visual premises a step depends on.

**How it works:**

The policy is prompted to produce a step-wise visual checklist that makes its required visual facts explicit, while a constraint extractor independently derives structured visual constraints from the input image. EVPV matches checklist claims against these constraints to compute a scalar visual reliability signal, and calibrates PRM step rewards via reliability gating: rewards for visually dependent steps are attenuated when reliability is low and preserved when reliability is high.

**The Problem it Solves:**

The entanglement between perception and reasoning leads to systematic false positives (rewarding hallucinated visual premises) and false negatives (penalizing correct grounded statements), undermining both reranking and error localization.

**Results:**

Experiments on VisualProcessBench and six multimodal reasoning benchmarks show that EVPV improves step-level verification and consistently boosts Best-of-N reranking accuracy over strong baselines.

This research appears to be from March 2026 and was developed by researchers from Alibaba's Qwen team and other institutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1d2e3a8-a873-41b8-9381-914b3747e0c0",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "2edadd2d-0f9c-4cfb-a7f4-7a4e965f1ba4",
  "toolUseResult": {
    "query": "EVPV \"explicit visual premise verification\" VLM process reward 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M7BXtBkAFHPzSx7zooP8G7",
        "content": [
          {
            "title": "[2603.16253] Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/abs/2603.16253"
          },
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models",
            "url": "https://arxiv.org/html/2603.16253"
          },
          {
            "title": "Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models",
            "url": "https://arxiv.org/pdf/2603.16253"
          },
          {
            "title": "GitHub - Qwen-Applications/EVPV-PRM · GitHub",
            "url": "https://github.com/Qwen-Applications/EVPV-PRM"
          },
          {
            "title": "CAPTION AS REWARD: ENHANCING VISION",
            "url": "https://openreview.net/pdf/8fdf67ae5eeb96964eb7b8af53323db8d9050074.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about EVPV:\n\nExplicit Visual Premise Verification (EVPV) is a lightweight verification interface that conditions step scoring on the reliability of the visual premises a step depends on.\n\n**How it works:**\n\nThe policy is prompted to produce a step-wise visual checklist that makes its required visual facts explicit, while a constraint extractor independently derives structured visual constraints from the input image. EVPV matches checklist claims against these constraints to compute a scalar visual reliability signal, and calibrates PRM step rewards via reliability gating: rewards for visually dependent steps are attenuated when reliability is low and preserved when reliability is high.\n\n**The Problem it Solves:**\n\nThe entanglement between perception and reasoning leads to systematic false positives (rewarding hallucinated visual premises) and false negatives (penalizing correct grounded statements), undermining both reranking and error localization.\n\n**Results:**\n\nExperiments on VisualProcessBench and six multimodal reasoning benchmarks show that EVPV improves step-level verification and consistently boosts Best-of-N reranking accuracy over strong baselines.\n\nThis research appears to be from March 2026 and was developed by researchers from Alibaba's Qwen team and other institutions."
    ],
    "durationSeconds": 7.309419915000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c1d2e3a8-a873-41b8-9381-914b3747e0c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-27T08:35:05.147Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AhsjLqb3pwjVrceGKq3FbS`</summary>

```json
{
  "query": "PDCR perception-decomposed confidence reward PRCO perception-reasoning coevolution multimodal 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2edadd2d-0f9c-4cfb-a7f4-7a4e965f1ba4",
  "isSidechain": false,
  "requestId": "req_011CbSmRmnQuVqWK1XKMNkzD",
  "type": "assistant",
  "uuid": "1bcc5ae3-9a32-425d-8a59-0e8f28d70dfb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsyFbjiLy77zU2fFLxpuAA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 655,
      "cache_read_input_tokens": 22696,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 655,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 22696,
          "cache_creation_input_tokens": 655,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 655
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

_source line 29 · 2026-05-27T08:35:16.053Z_

<details><summary>↩ Tool result · `toolu_01AhsjLqb3pwjVrceGKq3FbS`</summary>

```text
Web search results for query: "PDCR perception-decomposed confidence reward PRCO perception-reasoning coevolution multimodal 2026"

Links: [{"title":"[2603.28618] Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/abs/2603.28618"},{"title":"GitHub - Dtc7w3PQ/PRCO: Official implementation of Seeing with You: Perception-Reasoning Co-evolution for Multimodal Reasoning. · GitHub","url":"https://github.com/Dtc7w3PQ/PRCO"},{"title":"Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/html/2603.28618v1"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Request PDF","url":"https://www.researchgate.net/publication/403307388_Seeing_with_You_Perception-Reasoning_Coevolution_for_Multimodal_Reasoning"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://chatpaper.com/paper/262369"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Takara TLDR","url":"https://tldr.takara.ai/p/2603.28618"},{"title":"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning","url":"https://arxiv.org/pdf/2603.28618"},{"title":"PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning","url":"https://arxiv.org/html/2605.13467"}]

Great! I found relevant information about both PRCO and PDCR. Here are the search results:

## PRCO (Perception-Reasoning Coevolution)

PRCO is a dual-role RLVR framework with a shared policy introduced to address the perception bottleneck in multimodal reasoning. PRCO consists of two cooperative roles: an Observer that generates an evidence caption tailored to the question and a Solver that predicts the final answer based on this caption.

Existing RLVR approaches typically rely on outcome-driven optimization that updates both perception and reasoning using a shared reward based solely on the final answer, which blurs credit assignment and frequently improves reasoning patterns while failing to reliably enhance the accuracy of upstream visual evidence extraction.

PRCO employs role-specific reward signals: the Solver is optimized using verifiable outcome rewards on the final answer, while the Observer receives a utility reward derived from the Solver's downstream success. Extensive experiments across eight challenging multimodal reasoning benchmarks demonstrate that PRCO yields consistent improvements across model scales by over 7 points on average accuracy compared to the base model.

## PDCR (Perception-Decomposed Confidence Reward)

The search results show that PDCR is titled "Perception-Decomposed Confidence Reward for Vision-Language Reasoning", though detailed information about this specific approach is limited in the retrieved results.

Both papers appear to be recent 2026 research focusing on improving multimodal reasoning by addressing perception and reasoning separately.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bcc5ae3-9a32-425d-8a59-0e8f28d70dfb",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "be29ac85-193d-4a83-a0ee-79b238860448",
  "toolUseResult": {
    "query": "PDCR perception-decomposed confidence reward PRCO perception-reasoning coevolution multimodal 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KJkkHNsyEZHM8AwRe3MZmw",
        "content": [
          {
            "title": "[2603.28618] Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/abs/2603.28618"
          },
          {
            "title": "GitHub - Dtc7w3PQ/PRCO: Official implementation of Seeing with You: Perception-Reasoning Co-evolution for Multimodal Reasoning. · GitHub",
            "url": "https://github.com/Dtc7w3PQ/PRCO"
          },
          {
            "title": "Seeing with You: Perception–Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2603.28618v1"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/403307388_Seeing_with_You_Perception-Reasoning_Coevolution_for_Multimodal_Reasoning"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://chatpaper.com/paper/262369"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2603.28618"
          },
          {
            "title": "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning",
            "url": "https://arxiv.org/pdf/2603.28618"
          },
          {
            "title": "PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning",
            "url": "https://arxiv.org/html/2605.13467"
          }
        ]
      },
      "Great! I found relevant information about both PRCO and PDCR. Here are the search results:\n\n## PRCO (Perception-Reasoning Coevolution)\n\nPRCO is a dual-role RLVR framework with a shared policy introduced to address the perception bottleneck in multimodal reasoning. PRCO consists of two cooperative roles: an Observer that generates an evidence caption tailored to the question and a Solver that predicts the final answer based on this caption.\n\nExisting RLVR approaches typically rely on outcome-driven optimization that updates both perception and reasoning using a shared reward based solely on the final answer, which blurs credit assignment and frequently improves reasoning patterns while failing to reliably enhance the accuracy of upstream visual evidence extraction.\n\nPRCO employs role-specific reward signals: the Solver is optimized using verifiable outcome rewards on the final answer, while the Observer receives a utility reward derived from the Solver's downstream success. Extensive experiments across eight challenging multimodal reasoning benchmarks demonstrate that PRCO yields consistent improvements across model scales by over 7 points on average accuracy compared to the base model.\n\n## PDCR (Perception-Decomposed Confidence Reward)\n\nThe search results show that PDCR is titled \"Perception-Decomposed Confidence Reward for Vision-Language Reasoning\", though detailed information about this specific approach is limited in the retrieved results.\n\nBoth papers appear to be recent 2026 research focusing on improving multimodal reasoning by addressing perception and reasoning separately."
    ],
    "durationSeconds": 10.90066810000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1bcc5ae3-9a32-425d-8a59-0e8f28d70dfb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-27T08:35:16.061Z_

```json
{
  "parentUuid": "be29ac85-193d-4a83-a0ee-79b238860448",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7b89ec9f-820a-4335-9d57-21827d338fe8",
  "timestamp": "2026-05-27T08:35:16.061Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-27T08:35:18.517Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHuUf4f2Je4SwTABFAibES`</summary>

```json
{
  "query": "constraint satisfaction verification reward signal reinforcement learning mathematical reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b89ec9f-820a-4335-9d57-21827d338fe8",
  "isSidechain": false,
  "requestId": "req_011CbSmSoKiRHrjFSy2R1BuY",
  "type": "assistant",
  "uuid": "c74b5016-264b-4c17-9642-c84e4dfa070d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CyNdPCcfmSD49N1YfoJSEf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 992,
      "cache_read_input_tokens": 23351,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 992,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 23351,
          "cache_creation_input_tokens": 992,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 992
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

_source line 32 · 2026-05-27T08:35:26.832Z_

<details><summary>↩ Tool result · `toolu_01LHuUf4f2Je4SwTABFAibES`</summary>

```text
Web search results for query: "constraint satisfaction verification reward signal reinforcement learning mathematical reasoning 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.19590"},{"title":"ReSyn: Autonomously Scaling Synthetic Environments for Reasoning Models","url":"https://arxiv.org/html/2602.20117v1"},{"title":"Reinforcement Learning with Verified Rewards (RLVR)","url":"https://www.emergentmind.com/topics/reinforcement-learning-with-verified-rewards-rlvr"},{"title":"The Surprising Effectiveness of Negative Reinforcement in LLM Reasoning","url":"https://arxiv.org/pdf/2506.01347"},{"title":"Reinforcement Learning with Verifiable Rewards","url":"https://www.emergentmind.com/topics/reinforcement-learning-with-verifiable-rewards-rlvr"},{"title":"Hybrid Reinforcement: When Reward Is Sparse, It's Better to Be Dense","url":"https://arxiv.org/pdf/2510.07242"},{"title":"SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning","url":"https://arxiv.org/pdf/2512.03244"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"}]

I found relevant research on constraint satisfaction, verification reward signals, reinforcement learning, and mathematical reasoning from 2025-2026. Here are the key findings:

## Reinforcement Learning with Verifiable Rewards (RLVR)

RLVR utilizes rule-based verification functions, such as exact answer matching, to provide reward signals, thereby avoiding the complexities and potential pitfalls of learned reward models. This approach has sparked significant advances, with models like DeepSeek-R1 achieving state-of-the-art reasoning capabilities.

## Recent Extensions and Approaches (2025-2026)

DeepSeek-AI (2025) demonstrated that large-scale RL, even when guided only by correctness and format rewards, can yield state-of-the-art performance on math and coding benchmarks.

VerIF (Peng et al., 11 Jun 2025) introduced a hybrid approach, combining rule-based code checking for "hard" constraints with LLM-based semantic verification for "soft" constraints in instruction-following tasks.

Process reward models with chain-of-thought verification (PRM-CoT) as the reward model in RL experiments on mathematical reasoning achieved 47.4% average accuracy across six mathematical reasoning benchmarks, outperforming ground-truth-based RLVR (43.9%).

## Challenges and Developments

Strict 0–1 verification is coarse and brittle: many reasoning tasks allow for partially correct solutions, and symbolic verifiers may under-credit valid solutions or fail to provide any useful signal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c74b5016-264b-4c17-9642-c84e4dfa070d",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "84dc50dd-6ad1-41de-9c81-e7b716612317",
  "toolUseResult": {
    "query": "constraint satisfaction verification reward signal reinforcement learning mathematical reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Arbn8jCDqGq4aVCEdmrw4H",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2505.19590"
          },
          {
            "title": "ReSyn: Autonomously Scaling Synthetic Environments for Reasoning Models",
            "url": "https://arxiv.org/html/2602.20117v1"
          },
          {
            "title": "Reinforcement Learning with Verified Rewards (RLVR)",
            "url": "https://www.emergentmind.com/topics/reinforcement-learning-with-verified-rewards-rlvr"
          },
          {
            "title": "The Surprising Effectiveness of Negative Reinforcement in LLM Reasoning",
            "url": "https://arxiv.org/pdf/2506.01347"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards",
            "url": "https://www.emergentmind.com/topics/reinforcement-learning-with-verifiable-rewards-rlvr"
          },
          {
            "title": "Hybrid Reinforcement: When Reward Is Sparse, It's Better to Be Dense",
            "url": "https://arxiv.org/pdf/2510.07242"
          },
          {
            "title": "SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2512.03244"
          },
          {
            "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview",
            "url": "https://openreview.net/forum?id=4OsgYD7em5"
          }
        ]
      },
      "I found relevant research on constraint satisfaction, verification reward signals, reinforcement learning, and mathematical reasoning from 2025-2026. Here are the key findings:\n\n## Reinforcement Learning with Verifiable Rewards (RLVR)\n\nRLVR utilizes rule-based verification functions, such as exact answer matching, to provide reward signals, thereby avoiding the complexities and potential pitfalls of learned reward models. This approach has sparked significant advances, with models like DeepSeek-R1 achieving state-of-the-art reasoning capabilities.\n\n## Recent Extensions and Approaches (2025-2026)\n\nDeepSeek-AI (2025) demonstrated that large-scale RL, even when guided only by correctness and format rewards, can yield state-of-the-art performance on math and coding benchmarks.\n\nVerIF (Peng et al., 11 Jun 2025) introduced a hybrid approach, combining rule-based code checking for \"hard\" constraints with LLM-based semantic verification for \"soft\" constraints in instruction-following tasks.\n\nProcess reward models with chain-of-thought verification (PRM-CoT) as the reward model in RL experiments on mathematical reasoning achieved 47.4% average accuracy across six mathematical reasoning benchmarks, outperforming ground-truth-based RLVR (43.9%).\n\n## Challenges and Developments\n\nStrict 0–1 verification is coarse and brittle: many reasoning tasks allow for partially correct solutions, and symbolic verifiers may under-credit valid solutions or fail to provide any useful signal."
    ],
    "durationSeconds": 8.308824590000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c74b5016-264b-4c17-9642-c84e4dfa070d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-27T08:35:29.513Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011frB7adBPmM9zD9UJAAbGp`</summary>

```json
{
  "query": "PFlowNet variational RL geometric reward shaping visually grounded reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84dc50dd-6ad1-41de-9c81-e7b716612317",
  "isSidechain": false,
  "requestId": "req_011CbSmTbLRF5Jugp85zusQy",
  "type": "assistant",
  "uuid": "9cd5fcb6-8dda-443a-ad17-3169d71e2db6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017L7gPDr4uMdzEWBQQhc3Bu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 823,
      "cache_read_input_tokens": 24343,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 823,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 24343,
          "cache_creation_input_tokens": 823,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 823
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

_source line 34 · 2026-05-27T08:35:39.359Z_

<details><summary>↩ Tool result · `toolu_011frB7adBPmM9zD9UJAAbGp`</summary>

```text
Web search results for query: "PFlowNet variational RL geometric reward shaping visually grounded reasoning 2026"

Links: [{"title":"Perceptual Flow Network for Visually Grounded Reasoning","url":"https://arxiv.org/html/2605.02730"},{"title":"Thinking with Constructions: A Benchmark and Policy Optimization for Visual-Text Interleaved Geometric Reasoning","url":"https://arxiv.org/pdf/2603.18662"},{"title":"Grounded Reinforcement Learning for Visual Reasoning","url":"https://arxiv.org/pdf/2505.23678"},{"title":"Perception-Aware Policy Optimization for Multimodal Reasoning","url":"https://arxiv.org/pdf/2507.06448"},{"title":"GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning","url":"https://arxiv.org/pdf/2509.17437"},{"title":"RationalRewards: Reasoning Rewards Scale Visual Generation Both Training and Test Time","url":"https://arxiv.org/html/2604.11626"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

PFlowNet (Perceptual Flow Network) employs a self-parameterized variational distribution to approximate the posterior of idealized perceptual behaviors instead of constraining visual rationales via rigid alignment with static geometric priors.

The approach proposes a variational Reinforcement Fine-Tuning (RFT) strategy that integrates a carefully-designed reward and a vicinal geometric shaping to ensure a better approximation of the target posterior.

The Variational Reinforcement Fine-Tuning Strategy integrates a multi-dimensional reward function with a vicinal geometric shaping scheme to encourage visual-reliable yet reasoning-oriented perceptual behaviors.

The method achieves substantial improvements of 13.1%, 10.4% and 21% over the base model (Qwen3-VL 8B) on V* Bench, TreeBench, and MME-RealWorld-lite, respectively.

The paper, titled "Perceptual Flow Network for Visually Grounded Reasoning," focuses on combining variational inference with reinforcement learning and geometric reward shaping to improve visually grounded reasoning in vision-language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9cd5fcb6-8dda-443a-ad17-3169d71e2db6",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "80682b25-3f4b-44d3-bb20-0fd4ae07cddb",
  "toolUseResult": {
    "query": "PFlowNet variational RL geometric reward shaping visually grounded reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WcfQGCSX7bZx8JF3SVR7ji",
        "content": [
          {
            "title": "Perceptual Flow Network for Visually Grounded Reasoning",
            "url": "https://arxiv.org/html/2605.02730"
          },
          {
            "title": "Thinking with Constructions: A Benchmark and Policy Optimization for Visual-Text Interleaved Geometric Reasoning",
            "url": "https://arxiv.org/pdf/2603.18662"
          },
          {
            "title": "Grounded Reinforcement Learning for Visual Reasoning",
            "url": "https://arxiv.org/pdf/2505.23678"
          },
          {
            "title": "Perception-Aware Policy Optimization for Multimodal Reasoning",
            "url": "https://arxiv.org/pdf/2507.06448"
          },
          {
            "title": "GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning",
            "url": "https://arxiv.org/pdf/2509.17437"
          },
          {
            "title": "RationalRewards: Reasoning Rewards Scale Visual Generation Both Training and Test Time",
            "url": "https://arxiv.org/html/2604.11626"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found:\n\nPFlowNet (Perceptual Flow Network) employs a self-parameterized variational distribution to approximate the posterior of idealized perceptual behaviors instead of constraining visual rationales via rigid alignment with static geometric priors.\n\nThe approach proposes a variational Reinforcement Fine-Tuning (RFT) strategy that integrates a carefully-designed reward and a vicinal geometric shaping to ensure a better approximation of the target posterior.\n\nThe Variational Reinforcement Fine-Tuning Strategy integrates a multi-dimensional reward function with a vicinal geometric shaping scheme to encourage visual-reliable yet reasoning-oriented perceptual behaviors.\n\nThe method achieves substantial improvements of 13.1%, 10.4% and 21% over the base model (Qwen3-VL 8B) on V* Bench, TreeBench, and MME-RealWorld-lite, respectively.\n\nThe paper, titled \"Perceptual Flow Network for Visually Grounded Reasoning,\" focuses on combining variational inference with reinforcement learning and geometric reward shaping to improve visually grounded reasoning in vision-language models."
    ],
    "durationSeconds": 9.840809743000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9cd5fcb6-8dda-443a-ad17-3169d71e2db6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-27T08:35:42.969Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LGDV5BCnFX1FjTkFbnZRDv`</summary>

```json
{
  "query": "SSL-R1 self-supervised visual reinforcement post-training MLLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80682b25-3f4b-44d3-bb20-0fd4ae07cddb",
  "isSidechain": false,
  "requestId": "req_011CbSmUWtocWFAWJC2yXtc5",
  "type": "assistant",
  "uuid": "84c19baa-ff37-4f8f-97c1-6b34f60397c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NxZDxCLvYWUpwWrxMjYDWp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 644,
      "cache_read_input_tokens": 25166,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 644,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 25166,
          "cache_creation_input_tokens": 644,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 644
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

_source line 36 · 2026-05-27T08:35:49.502Z_

<details><summary>↩ Tool result · `toolu_01LGDV5BCnFX1FjTkFbnZRDv`</summary>

```text
Web search results for query: "SSL-R1 self-supervised visual reinforcement post-training MLLM 2026"

Links: [{"title":"[2604.20705] SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models","url":"https://arxiv.org/abs/2604.20705"},{"title":"SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models","url":"https://arxiv.org/html/2604.20705"},{"title":"GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub","url":"https://github.com/smiles724/Awesome-LLM-RLVR"},{"title":"ViSS-R1: Self-Supervised Reinforcement Video Reasoning","url":"https://arxiv.org/html/2511.13054"},{"title":"Visual Jigsaw Post-Training Improves MLLMs","url":"https://arxiv.org/pdf/2509.25190"},{"title":"ViSS-R1: Self-Supervised Reinforcement Video Reasoning","url":"https://arxiv.org/pdf/2511.13054"}]

Based on the search results, here's what I found about SSL-R1:

## Overview

SSL-R1 is a generic self-supervised RL framework that derives verifiable rewards directly from images. It addresses the limitations of reinforcement learning with verifiable rewards (RLVR) in multimodal large language models, which rely on language-centric priors and expensive manual annotations that prevent MLLMs' intrinsic visual understanding and scalable reward designs.

## Methodology

SSL-R1 reformulates widely-used SSL tasks into a set of verifiable visual puzzles for RL post-training, requiring neither human nor external model supervision. The framework focuses on vision-centric approaches rather than language-centric ones.

## Results and Impact

SSL-R1 substantially improves the multimodal understanding and reasoning capabilities of MLLMs, demonstrating the potential of leveraging vision-centric self-supervised tasks for MLLM post-training. SSL-R1 is vision-centric, cost-effective, scalable, and consistently improves Qwen2.5-VL on 13 vision-centric multimodal benchmarks, spanning fine-grained perception, spatial understanding, and compositional understanding.

The SSL-R1 paper was released on April 22, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84c19baa-ff37-4f8f-97c1-6b34f60397c4",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "8e75c971-6c90-4d41-9001-d06b647af794",
  "toolUseResult": {
    "query": "SSL-R1 self-supervised visual reinforcement post-training MLLM 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X3PMAMHKY9TC2ghVx663Tm",
        "content": [
          {
            "title": "[2604.20705] SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models",
            "url": "https://arxiv.org/abs/2604.20705"
          },
          {
            "title": "SSL-R1: Self-Supervised Visual Reinforcement Post-Training for Multimodal Large Language Models",
            "url": "https://arxiv.org/html/2604.20705"
          },
          {
            "title": "GitHub - smiles724/Awesome-LLM-RLVR: Collection of latest papers and materials in the area of RLVR! · GitHub",
            "url": "https://github.com/smiles724/Awesome-LLM-RLVR"
          },
          {
            "title": "ViSS-R1: Self-Supervised Reinforcement Video Reasoning",
            "url": "https://arxiv.org/html/2511.13054"
          },
          {
            "title": "Visual Jigsaw Post-Training Improves MLLMs",
            "url": "https://arxiv.org/pdf/2509.25190"
          },
          {
            "title": "ViSS-R1: Self-Supervised Reinforcement Video Reasoning",
            "url": "https://arxiv.org/pdf/2511.13054"
          }
        ]
      },
      "Based on the search results, here's what I found about SSL-R1:\n\n## Overview\n\nSSL-R1 is a generic self-supervised RL framework that derives verifiable rewards directly from images. It addresses the limitations of reinforcement learning with verifiable rewards (RLVR) in multimodal large language models, which rely on language-centric priors and expensive manual annotations that prevent MLLMs' intrinsic visual understanding and scalable reward designs.\n\n## Methodology\n\nSSL-R1 reformulates widely-used SSL tasks into a set of verifiable visual puzzles for RL post-training, requiring neither human nor external model supervision. The framework focuses on vision-centric approaches rather than language-centric ones.\n\n## Results and Impact\n\nSSL-R1 substantially improves the multimodal understanding and reasoning capabilities of MLLMs, demonstrating the potential of leveraging vision-centric self-supervised tasks for MLLM post-training. SSL-R1 is vision-centric, cost-effective, scalable, and consistently improves Qwen2.5-VL on 13 vision-centric multimodal benchmarks, spanning fine-grained perception, spatial understanding, and compositional understanding.\n\nThe SSL-R1 paper was released on April 22, 2026."
    ],
    "durationSeconds": 6.526980263000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "84c19baa-ff37-4f8f-97c1-6b34f60397c4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem  Current multimodal math reasoning systems lack mechanisms to verify whether their perceived visual facts are mutua…",
  "leafUuid": "8e75c971-6c90-4d41-9001-d06b647af794",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Tool call

_source line 39 · 2026-05-27T08:35:52.089Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TZK56ZnMn1fv6NZhumFTYA`</summary>

```json
{
  "query": "mathematical constraint checking perception errors multimodal geometry diagram angle sum verification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e75c971-6c90-4d41-9001-d06b647af794",
  "isSidechain": false,
  "requestId": "req_011CbSmVGH1AtLFrtdHXbQo6",
  "type": "assistant",
  "uuid": "01a6813f-77f6-48ab-9494-52fe60628f24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVFcuY8BMwWzACddHiUy2R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 705,
      "cache_read_input_tokens": 25810,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 705,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 25810,
          "cache_creation_input_tokens": 705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 705
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

_source line 40 · 2026-05-27T08:36:02.658Z_

<details><summary>↩ Tool result · `toolu_01TZK56ZnMn1fv6NZhumFTYA`</summary>

```text
Web search results for query: "mathematical constraint checking perception errors multimodal geometry diagram angle sum verification 2025 2026"

Links: [{"title":"GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub","url":"https://github.com/majianz/dl4gps"},{"title":"What MLLMs Learn about When they Learn about Multimodal Reasoning: Perception, Reasoning, or their Integration?","url":"https://arxiv.org/pdf/2510.01719"},{"title":"BENCHMARKING MULTIMODAL MATHEMATICAL ...","url":"https://openreview.net/pdf?id=j3960MwHQn"},{"title":"Math Blind: Failures in Diagram Understanding Undermine Reasoning in MLLMs","url":"https://arxiv.org/pdf/2503.20745"},{"title":"GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning","url":"https://arxiv.org/html/2509.17437"},{"title":"Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver⋆ Equal contribution. ✉Corresponding author. Our model and dataset are available at https://github.com/zezeze97/DFE-GPS.","url":"https://arxiv.org/html/2409.04214v2"}]

Based on the web search results, I found relevant research on mathematical constraint checking, perception errors, and multimodal geometry diagram analysis from 2025-2026:

## Key Findings:

**Multimodal Model Perception Challenges in Geometry:**

Current multimodal large language models (MLLMs) face considerable challenges in accurately interpreting mathematical diagrams—abstract visual representations characterized by precise geometric structures and symbolic notations. These diagrams provide a unique perceptual challenge: the explicit structural constraints require genuine visual interpretation rather than pattern recognition or textual heuristics.

**Benchmarks for Evaluating Perception and Reasoning:**

MATHLENS is a controlled benchmark of geometry problems that separately probes perception, reasoning, and their integration. Additionally, research categorizes errors in multimodal mathematical reasoning into distinct types: visual perception errors, calculation errors, contextual misunderstandings, logical errors, and answer integration errors.

**Integration Issues in Reasoning:**

As perception and reasoning improve, a growing fraction of remaining errors fall outside these components and are categorized as integration, suggesting that progress in multimodal reasoning involves shifting balances among different subskills.

**Recent Approaches:**

Recent advances in reasoning models such as DeepSeek-R1 have demonstrated that reinforcement learning with verifiable reward can markedly strengthen the reasoning abilities of large language models, though gains in vision-intensive benchmarks remain limited.

These results indicate active research into how multimodal models handle geometric constraint verification and angle calculations in diagrams during 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "01a6813f-77f6-48ab-9494-52fe60628f24",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "c8d5a6bd-fb71-4de4-8c6f-a6918c142491",
  "toolUseResult": {
    "query": "mathematical constraint checking perception errors multimodal geometry diagram angle sum verification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Msgdgg6d7n32B6Rb9raCWQ",
        "content": [
          {
            "title": "GitHub - majianz/dl4gps: [ACL 2026 Main Conference] Paper list for the survey \"A Survey of Deep Learning for Geometry Problem Solving\" · GitHub",
            "url": "https://github.com/majianz/dl4gps"
          },
          {
            "title": "What MLLMs Learn about When they Learn about Multimodal Reasoning: Perception, Reasoning, or their Integration?",
            "url": "https://arxiv.org/pdf/2510.01719"
          },
          {
            "title": "BENCHMARKING MULTIMODAL MATHEMATICAL ...",
            "url": "https://openreview.net/pdf?id=j3960MwHQn"
          },
          {
            "title": "Math Blind: Failures in Diagram Understanding Undermine Reasoning in MLLMs",
            "url": "https://arxiv.org/pdf/2503.20745"
          },
          {
            "title": "GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning",
            "url": "https://arxiv.org/html/2509.17437"
          },
          {
            "title": "Diagram Formalization Enhanced Multi-Modal Geometry Problem Solver⋆ Equal contribution. ✉Corresponding author. Our model and dataset are available at https://github.com/zezeze97/DFE-GPS.",
            "url": "https://arxiv.org/html/2409.04214v2"
          }
        ]
      },
      "Based on the web search results, I found relevant research on mathematical constraint checking, perception errors, and multimodal geometry diagram analysis from 2025-2026:\n\n## Key Findings:\n\n**Multimodal Model Perception Challenges in Geometry:**\n\nCurrent multimodal large language models (MLLMs) face considerable challenges in accurately interpreting mathematical diagrams—abstract visual representations characterized by precise geometric structures and symbolic notations. These diagrams provide a unique perceptual challenge: the explicit structural constraints require genuine visual interpretation rather than pattern recognition or textual heuristics.\n\n**Benchmarks for Evaluating Perception and Reasoning:**\n\nMATHLENS is a controlled benchmark of geometry problems that separately probes perception, reasoning, and their integration. Additionally, research categorizes errors in multimodal mathematical reasoning into distinct types: visual perception errors, calculation errors, contextual misunderstandings, logical errors, and answer integration errors.\n\n**Integration Issues in Reasoning:**\n\nAs perception and reasoning improve, a growing fraction of remaining errors fall outside these components and are categorized as integration, suggesting that progress in multimodal reasoning involves shifting balances among different subskills.\n\n**Recent Approaches:**\n\nRecent advances in reasoning models such as DeepSeek-R1 have demonstrated that reinforcement learning with verifiable reward can markedly strengthen the reasoning abilities of large language models, though gains in vision-intensive benchmarks remain limited.\n\nThese results indicate active research into how multimodal models handle geometric constraint verification and angle calculations in diagrams during 2025-2026."
    ],
    "durationSeconds": 10.564347655999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "01a6813f-77f6-48ab-9494-52fe60628f24",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-27T08:36:05.510Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DTvn8zNFCbaiyRSudG3RBK`</summary>

```json
{
  "query": "M3-ACE multi-agentic context engineering rectify perception multimodal math 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c8d5a6bd-fb71-4de4-8c6f-a6918c142491",
  "isSidechain": false,
  "requestId": "req_011CbSmWEYbqDRjb7uV3e4FA",
  "type": "assistant",
  "uuid": "54cc9600-7bc1-4eb9-82ae-0e108d6008e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0123Ty78v8NrurvLbqkJBFN6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 776,
      "cache_read_input_tokens": 26515,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 776,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 26515,
          "cache_creation_input_tokens": 776,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 776
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

_source line 42 · 2026-05-27T08:36:12.254Z_

<details><summary>↩ Tool result · `toolu_01DTvn8zNFCbaiyRSudG3RBK`</summary>

```text
Web search results for query: "M3-ACE multi-agentic context engineering rectify perception multimodal math 2026"

Links: [{"title":"[2603.08369] M$^3$-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering","url":"https://arxiv.org/abs/2603.08369"},{"title":"M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering","url":"https://arxiv.org/html/2603.08369"},{"title":"M3-ACE: Rectifying Visual Perception in Multimodal Math ...","url":"https://arxiv.org/pdf/2603.08369"},{"title":"From Perception to Autonomous Computational Modeling: A Multi-Agent Approach","url":"https://arxiv.org/pdf/2604.06788"},{"title":"Context Engineering: From Prompts to Corporate Multi-Agent Architecture","url":"https://arxiv.org/pdf/2603.09619"},{"title":"Meta Context Engineering via Agentic Skill Evolution","url":"https://arxiv.org/pdf/2601.21557"}]

Based on the search results, I found relevant information about M3-ACE:

M3-ACE is a multi-agentic context engineering framework designed to rectify visual perception in multimodal math reasoning. 

The framework addresses a critical bottleneck in multimodal large language models' visual mathematical reasoning: inaccurate visual perception, with most failures originating from incorrect or incomplete visual evidence extraction rather than deficiencies in reasoning capability.

Instead of directly aggregating final answers, the approach decouples perception and reasoning by dynamically maintaining a shared context centered on visual evidence lists. Multiple agents collaboratively contribute complementary observations, enabling the system to expose inconsistencies and recover missing perceptual information.

To support stable multi-turn collaboration, the framework introduces two lightweight tools: a Summary Tool that organizes evidence from different agents into consistent, complementary, and conflicting components, and a Refine Tool that filters unreliable samples and guides iterative correction.

Extensive experiments demonstrate that M3-ACE substantially improves visual mathematical reasoning performance across multiple benchmarks. The paper was published on arxiv in March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "54cc9600-7bc1-4eb9-82ae-0e108d6008e2",
  "isSidechain": false,
  "promptId": "5428d206-324e-4ed1-97f2-c866166a22d2",
  "type": "user",
  "uuid": "fa9fb66d-7eb8-45f5-99c0-e3d294bc7c2a",
  "toolUseResult": {
    "query": "M3-ACE multi-agentic context engineering rectify perception multimodal math 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018WunS85KQCeS94fKDLQRoY",
        "content": [
          {
            "title": "[2603.08369] M$^3$-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering",
            "url": "https://arxiv.org/abs/2603.08369"
          },
          {
            "title": "M3-ACE: Rectifying Visual Perception in Multimodal Math Reasoning via Multi-Agentic Context Engineering",
            "url": "https://arxiv.org/html/2603.08369"
          },
          {
            "title": "M3-ACE: Rectifying Visual Perception in Multimodal Math ...",
            "url": "https://arxiv.org/pdf/2603.08369"
          },
          {
            "title": "From Perception to Autonomous Computational Modeling: A Multi-Agent Approach",
            "url": "https://arxiv.org/pdf/2604.06788"
          },
          {
            "title": "Context Engineering: From Prompts to Corporate Multi-Agent Architecture",
            "url": "https://arxiv.org/pdf/2603.09619"
          },
          {
            "title": "Meta Context Engineering via Agentic Skill Evolution",
            "url": "https://arxiv.org/pdf/2601.21557"
          }
        ]
      },
      "Based on the search results, I found relevant information about M3-ACE:\n\nM3-ACE is a multi-agentic context engineering framework designed to rectify visual perception in multimodal math reasoning. \n\nThe framework addresses a critical bottleneck in multimodal large language models' visual mathematical reasoning: inaccurate visual perception, with most failures originating from incorrect or incomplete visual evidence extraction rather than deficiencies in reasoning capability.\n\nInstead of directly aggregating final answers, the approach decouples perception and reasoning by dynamically maintaining a shared context centered on visual evidence lists. Multiple agents collaboratively contribute complementary observations, enabling the system to expose inconsistencies and recover missing perceptual information.\n\nTo support stable multi-turn collaboration, the framework introduces two lightweight tools: a Summary Tool that organizes evidence from different agents into consistent, complementary, and conflicting components, and a Refine Tool that filters unreliable samples and guides iterative correction.\n\nExtensive experiments demonstrate that M3-ACE substantially improves visual mathematical reasoning performance across multiple benchmarks. The paper was published on arxiv in March 2026."
    ],
    "durationSeconds": 6.738686619000014,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "54cc9600-7bc1-4eb9-82ae-0e108d6008e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-27T08:37:22.729Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the research landscape. Let me synthesize my findings and provide my analysis as the "发掘 agent."

Key observations from my research:

1. **The perception bottleneck is well-established**: Multiple papers (MM-MATH, Math Blind, MATHLENS, etc.) confirm that perception errors are a dominant source of failure in multimodal math reasoning.

2. **The RLVR + perception reward space is getting crowded**: Perception-R1 (LLM-judged per-claim), PEARL (ground-truth checklists), EVPV (per-claim matching against constraints), GeoDPO (DSL translation accuracy), SSL-R1 (generic visual puzzles), PDCR (confidence-based), PRCO (observer-solver roles), PFlowNet (variational RL with geometric reward shaping).
   
3. **ASVP's core novelty**: Using mathematical axiom consistency—checking whether extracted facts cohere through geometric theorems—as a self-supervised perception reward. This differs fundamentally from prior work: Perception-R1 judges individual claims with annotations, PEARL uses ground-truth checklists, EVPV matches claims against constraints without inter-claim logic, GeoDPO rewards DSL translation accuracy, SSL-R1 tackles generic visual puzzles rather than domain-specific geometry, and PRCO derives rewards from downstream solver performance.

4. **The critical question**: Whether inter-fact coherence through axiom consistency actually captures meaningful perception quality better than existing approaches.

5. **Evaluating the core insight**: The observation that perceived facts must be jointly consistent—not just individually plausible—is genuinely important, and leveraging mathematical theorems as free verification is elegant. The zero-annotation requirement is also practically valuable. But I need to probe whether this is truly novel or if simpler alternatives (like just checking individual claims against extracted constraints) would achieve similar results.

6. **Addressing the constraint propagation concern**: The key question is whether RL training to internalize constraints is fundamentally better than just doing constraint checking at test time with re-prompting, especially since M3-ACE already does multi-agent collaborative perception rectification. The proposal does mention inference-time re-perception, so the advantage of RL training needs to be clearer.

7. **The deeper problem with the axiom checker**: There's a circular dependency here—the axiom checker needs to identify which axioms apply to a given set of perceived facts, but the perception of which entities form a triangle (for example) is itself uncertain. If the model perceives three angles that don't actually belong to the same triangle, the axiom checker would still try to apply the triangle angle sum theorem, making the reward signal potentially unreliable.

8. **Structural vs. quantitative perception**: The topological and structural perception—which points form which shapes—has to be correct before any quantitative axiom checking can work. SymHPR handles structural parsing, and ASVP claims to improve on it by checking quantitative values, but if the structural parsing is wrong to begin with, the quantitative checks become meaningless.

9. **Identifying the actual novelty**: Using mathematical axiom consistency as a reward signal for RL training appears to be the genuine contribution here. Existing approaches use per-claim checking, ground-truth annotations, generic visual tasks, DSL translation accuracy, or downstream answer correctness, but none leverage inter-claim mathematical consistency as a dense reward signal.

10. **Why this matters**: The key insight is that inter-claim consistency avoids the reference problem that plagues per-claim verification—you don't need ground truth to check whether three angles in a triangle sum to 180°. This creates a self-referential, zero-shot verification mechanism built directly into the mathematical structure of the domain, which is both dense and reliable without requiring any annotations.

11. **Broadening the scope**: While the proposal focuses on geometry, the core mechanism (using domain constraints as free verification rewards) could extend to physics diagrams with conservation laws, circuit diagrams with Kirchhoff's laws, or chemical structures with valence constraints. Emphasizing this generalizability would strengthen the significance considerably.

12. **Sharpening the central thesis**: The distinction between inter-claim consistency and per-claim verification is the real novelty here, but it's currently scattered through the related work section. This should become the main argument driving the entire proposal.

13. **Addressing structural parsing dependencies**: The proposal should clarify how it relates to existing work like SymHPR on structural parsing. ASVP could be positioned as the quantitative verification layer that sits on top of structural parsing, making them complementary rather than competing approaches.

14. **Improving reward signal informativeness**: There's a potential concern about reward sparsity—if the model gets most perceptions correct, most axioms will be satisfied and the signal becomes less useful. The proposal mentions using a consistency score based on the fraction of satisfied axioms, which is already continuous, but this could be strengthened by weighting axioms differently or using soft satisfaction measures to keep the signal informative even when performance is high.

Now I'm thinking about what's actually improvable at the conceptual level. The inter-claim consistency angle is the sharpest novelty here, but it's buried among other differences from related work when it should be the central contribution. Reframing this as a general paradigm—domain constraints enabling free verification rewards—rather than just a geometry-specific method would significantly strengthen the significance claim. There's also a real vulnerability: inference-time constraint checking without RL training might achieve similar results, especially given that M3-ACE already does perception rectification at test time. The proposal needs to make a stronger case for why training-time internalization fundamentally outperforms test-time correction.

The key counterargument is that RL training internalizes constraints, making the model intrinsically more accurate rather than requiring expensive multi-agent inference, and the learned patterns should generalize to new domains. But this needs explicit articulation rather than being left implicit. I'm also noticing that the structural parsing premise itself could be a vulnerability if not carefully addressed.

Comparing to V-Zero's self-improvement loop, ASVP has a meaningful advantage: it exploits domain-specific mathematical structure for a more targeted reward signal, whereas V-Zero remains domain-agnostic. That distinction could strengthen the novelty positioning.

I'm seeing several concrete improvements that could elevate this work—sharpening the novelty framing around inter-claim consistency, addressing the trivial alternative of inference-time constraint checking, and making the generalizability argument more explicit as a paradigm-level contribution. There's definitely room to develop this further.

The proposal itself is already well-structured with thorough related work coverage, so these improvements are about raising the ceiling rather than fixing core issues. But I should examine whether there's a fundamental flaw lurking underneath. The core premise—that mathematical diagrams encode structural invariants that provide a dense, automatically verifiable reward signal—depends on a potential circularity: the axiom checker needs to know which axioms apply, which requires structural understanding, but that structural understanding is itself part of what the perception task is trying to learn. So the quality of rewards hinges on whether the axiom checker can reliably identify applicable constraints without already having solved the perception problem.

The proposal addresses this by having the model output both structural and quantitative information in a formal constraint language, then checking consistency across both dimensions. This creates an interesting dynamic where structural errors get penalized alongside quantitative ones, which could actually help the model learn correct structural parsing. It's a valid concern but not fatal—more of a design consideration that needs acknowledgment and careful handling, particularly in how the curriculum stages are structured to build up from simpler to more complex structural understanding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa9fb66d-7eb8-45f5-99c0-e3d294bc7c2a",
  "isSidechain": false,
  "requestId": "req_011CbSmWwXwTLpvy7RLMzv7B",
  "type": "assistant",
  "uuid": "84538528-4729-4c04-82a4-2fa1d23e4994",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhsFV6cEhYWkQh3Wzx8LmQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 27291,
      "output_tokens": 7204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7204,
          "cache_read_input_tokens": 27291,
          "cache_creation_input_tokens": 638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 638
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

_source line 44 · 2026-05-27T08:38:52.028Z_

Now I have sufficient research context. Let me synthesize my findings and provide my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- **Perception-R1** (ICLR 2026): 使用 LLM judge 评估生成 CoT 中的视觉描述与预收集文本标注的一致性作为感知 reward。核心是 per-claim 的个体验证，需要标注数据。与 ASVP 的差异在于不检查 claims 间的数学互洽性。
- **PEARL** (arXiv 2025): 用 ground-truth 感知 checklist 作为 gating reward，在 MathVerse 上 +9.7%。需要标注的子问题答案。
- **EVPV** (arXiv Mar 2026, Qwen team): 从图像中提取结构化视觉约束，将 policy 生成的 step-wise visual checklist 与之匹配，计算 reliability score 来校准 PRM step reward。核心是 per-claim 与图像约束的匹配，不检查 claims 之间的数学公理一致性。这是与 ASVP 最接近的工作。
- **GeoDPO** (arXiv Feb 2026): 训练 NL-to-DSL translator，将 DSL 翻译准确度作为 RL reward 来增强几何感知。Reward 目标是翻译保真度，不是公理一致性。
- **PRCO** (arXiv Mar 2026): Observer/Solver 双角色共享 policy 的 RLVR 框架。Observer 生成 evidence caption，Solver 基于 caption 推理。Observer 的 reward 来自 Solver 的下游成功（utility reward），不利用数学结构。
- **SSL-R1** (arXiv Apr 2026): 将 SSL 任务（旋转预测、patch 排序等）重构为 verifiable visual puzzles 用于 MLLM RL post-training。domain-agnostic 的视觉 reward，不利用数学领域结构。
- **M3-ACE** (arXiv Mar 2026): 多 agent 协作在推理时动态维护共享 visual evidence list，通过 Summary Tool 和 Refine Tool 暴露感知不一致并迭代修正。是 inference-time 方法，不做 RL 训练。
- **PFlowNet** (arXiv May 2026): 变分 RFT 策略，结合多维度 reward 和 vicinal geometric shaping。"geometric" 指的是 reward 空间的几何形状，不是数学定理约束。
- **V-Zero** (arXiv Jan 2026): Questioner-Solver co-evolutionary loop，完全零标注，用 GRPO 训练。domain-agnostic，不利用领域特定结构。
- **MATHLENS/Math Blind** (2025-2026): 控制实验确认感知-推理瓶颈，且发现 perception 和 reasoning 的 integration 本身也是独立的 error source。

- **调研总结**: 当前领域在"感知 reward 设计"上有大量并发工作，核心分歧在于 reward 信号的来源：(1) 标注依赖型（PEARL）、(2) LLM/外部模型判断型（Perception-R1）、(3) 翻译保真度型（GeoDPO）、(4) 下游任务效用型（PRCO）、(5) 通用视觉任务型（SSL-R1）、(6) 推理时修正型（M3-ACE）。ASVP 提出的"数学公理互洽性"作为 reward 在这个分类中确实是一个未被占据的独特位置，最核心的差异化在于利用 inter-claim 的数学结构约束而非 per-claim 的独立验证。

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: 当前 proposal 的核心 novelty（inter-claim consistency vs per-claim verification）埋在 related work 的对比描述中，没有被提升为第一性原理级别的 thesis statement。建议将核心 claim 重构为一个更锐利的命题：**"数学感知的正确性本质上是一个联合约束满足问题（joint constraint satisfaction），而非独立事实验证问题（independent fact checking）"**。这是一个有认识论深度的洞察——它意味着即使每个单独感知在边际概率上是高置信的，联合分布仍然可能与数学公理矛盾。这对应到概率推理中 marginal-consistent 但 joint-inconsistent 的经典问题。这个 framing 比"我们用公理做 reward"有力得多，因为它揭示了一个结构性盲区：所有 per-claim 方法（Perception-R1, EVPV, PEARL）在原理层面就无法捕捉这类错误，无论其 per-claim 验证多么精确。当前 proposal 只在 Research Landscape 中提到 EVPV "does not check whether the set of perceived facts satisfies mathematical axioms"，但这应该是整篇论文的 central thesis，而不是 related work 中的一句话。
- 价值: 直接提升 Novelty 的清晰度和说服力。审稿人读完 abstract 就能理解"这和之前所有工作有什么本质区别"，而不需要逐个对比 related work 才能拼凑出 novelty 在哪。
- 调研依据: 对比 EVPV（per-claim matching against image-extracted constraints）和 Perception-R1（per-claim LLM judgment）后发现，ASVP 的 inter-claim consistency checking 确实占据了一个结构性不同的位置，但 proposal 当前的表述力度与这个差异的实际深度不匹配。

【发掘点 2】
- 维度: significance 提升
- 内容: 当前 proposal 将自己 framing 为一个"multimodal math reasoning"方法，但核心 insight（"域内结构性不变量可以作为零标注的自监督感知 reward"）具有远超几何/数学的泛化潜力。建议在 significance 论证中明确阐述 paradigm-level generalization：物理电路图（Kirchhoff 定律）、化学结构图（化合价约束）、工程图纸（尺寸一致性约束）、乃至表格/图表（sum-to-total, monotonicity）都存在类似的"domain axioms provide free verification"结构。**这不是建议增加实验scope**——这是关于如何 frame 论文的 contribution level 的问题。一个"几何感知的 RL reward 设计"是一个 technique；一个"利用域内不变量构建零标注感知 reward 的通用范式"是一个 paradigm。后者的 significance 天花板远高于前者。Proposal 已经提到 "chart constraints like sum-to-total; function constraints like monotonicity"，但没有将其提升为 paradigm-level 的 contribution framing。
- 价值: 从 technique-level contribution 提升到 paradigm-level contribution，直接提升 Significance 维度的上限。审稿人更可能认为 "this opens up a new direction" 而非 "this is a nice technique for geometry"。
- 调研依据: SSL-R1 使用通用 SSL puzzles 作为视觉 reward（domain-agnostic），V-Zero 用 Questioner-Solver loop 实现零标注（domain-agnostic）。ASVP 的独特优势恰恰在于 domain-specific structure 提供了比 domain-agnostic 方法更强、更可靠的信号。将这个对比提升到 paradigm 层面（domain-specific invariants as free rewards vs. domain-agnostic self-play/SSL），可以为 ASVP 在这个拥挤的赛道上找到一个更高维度的差异化定位。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: M3-ACE 已经证明，在推理时通过多 agent 协作暴露感知不一致并迭代修正，可以显著提升 multimodal math reasoning 性能。一个自然的 trivial alternative 是：**直接将 ASVP 的公理检查器作为 M3-ACE 框架中的一个 tool/agent，在推理时做公理一致性检查和迭代修正，而不需要任何 RL 训练**。这个 baseline 成本极低（只需实现公理检查器本身），如果效果接近，ASVP 的 RL 训练部分就失去了增量价值。Proposal 需要正面回应这个 trivial alternative，论证为什么 training-time internalization 比 inference-time correction 更优。可能的论证方向：(1) RL 训练使模型内化了一致性约束，泛化到新的、训练时未见过的公理组合；(2) inference-time 方法需要多次前向传播，计算成本与 RL 训练后的单次推理不可比；(3) RL 训练改变了模型的感知表征，使其在 early layers 就倾向于产生互洽的感知，而 inference-time 方法只是在 output level 做 patch。**但这些论证必须在 proposal 中被显式提出**，否则审稿人一定会问 "why not just do constraint checking at inference time?"
- 价值: 预防审稿人的第一反应质疑，强化核心方法的必要性论证（Novelty 维度的 "incremental value" 子维度）。
- 调研依据: M3-ACE (Mar 2026) 的 Summary Tool + Refine Tool 机制已经实现了推理时的感知一致性修正，proposal 当前只提到 M3-ACE "does not train perception via RL rewards"，但没有论证为什么 RL 训练比推理时修正更好。

【发掘点 4】
- 维度: 前提假设质疑
- 内容: ASVP 的公理检查器要正确工作，有一个隐含的前提假设：**模型输出的结构化感知（哪些点构成三角形、哪些线平行）必须在拓扑层面大致正确，公理的量化一致性检查才有意义**。如果模型错误地认为三个不相关的角属于同一个三角形，公理检查器会错误地用"角度和=180°"来验证这组角度，产生误导性的 reward 信号。这意味着 ASVP 的 axiom-consistency reward 的有效性，实际上依赖于结构化感知的准确性——而结构化感知本身就是需要被训练的对象之一。这不是致命问题（因为 RL 训练可以逐步改善结构化感知和量化感知的协同），但它需要被显式承认和讨论。建议 proposal 增加对这个 bootstrapping challenge 的分析：stage 1 的 curriculum 设计可能需要从结构约束简单（如三角形角度和——结构容易识别）的样本开始，逐步过渡到结构约束复杂的样本。这不是实验设计建议，而是对核心方法 soundness 的论证要求。
- 价值: 预防审稿人对方法 soundness 的质疑（"your reward signal depends on correct structural parsing, which is what you're trying to learn"），提前给出合理的解释和应对策略，强化核心 claim 的可信度。
- 调研依据: SymHPR (Dec 2025) 专注于 topological/structural parsing consistency（point-on-line, shape-on-relation），而 ASVP 声称在 quantitative level 工作。两者实际上存在依赖关系：quantitative axiom checking 需要 structural parsing 作为前提。Proposal 当前将 SymHPR 定位为"不处理量化值"，但没有承认 ASVP 对 SymHPR 所处理的结构层信息的隐含依赖。

【发掘点 5】
- 维度: related work 差异化
- 内容: EVPV 是当前与 ASVP 最接近的工作，proposal 对其的区分是"does not check whether the set of perceived facts satisfies mathematical axioms"。但这个区分需要更精确。EVPV 从图像中提取 structured visual constraints，并将 policy 的 step-wise visual checklist 与之匹配。关键问题是：EVPV 的 "constraint extractor" 提取的是什么级别的约束？如果 EVPV 的约束包括"这个三角形的角度和应该是180°"这类 inter-claim 数学约束，那 ASVP 的 novelty claim 就被严重削弱。Proposal 需要做更精细的区分：EVPV 的约束是 image-level perceptual constraints（"图中这个角看起来是大约60°"），而 ASVP 的约束是 domain-level mathematical axioms（"无论图中角度看起来是多少，三角形三个角必须和为180°"）。前者仍然是 per-claim 的（每个约束独立关联到图像区域），后者是 inter-claim 的（约束连接多个感知 claims 的关系）。这个区分的精确性直接决定 novelty claim 是否站得住脚。
- 价值: 直接关系 Related Work 差异化维度。如果与 EVPV 的区分不够精确，审稿人可能判定 "incremental over EVPV"，这对中稿是致命的。
- 调研依据: 通过阅读 EVPV 的 arxiv 页面和 GitHub repo 描述，EVPV 的 constraint extractor 从图像提取的是视觉层面的约束（形状、位置、颜色等可从图像直接获取的信息），而非数学公理层面的约束。但 proposal 需要在论文中显式且精确地进行这个区分。

Sources:
- [Perception-R1 (ICLR 2026)](https://arxiv.org/abs/2506.07218)
- [EVPV: Grounding the Score (arXiv 2026)](https://arxiv.org/abs/2603.16253)
- [GeoDPO (arXiv 2026)](https://arxiv.org/abs/2602.22703)
- [PRCO: Seeing with You (arXiv 2026)](https://arxiv.org/abs/2603.28618)
- [SSL-R1 (arXiv 2026)](https://arxiv.org/abs/2604.20705)
- [V-Zero (arXiv 2026)](https://arxiv.org/abs/2601.10094)
- [M3-ACE (arXiv 2026)](https://arxiv.org/abs/2603.08369)
- [PFlowNet (arXiv 2026)](https://arxiv.org/html/2605.02730)
- [FormalGeo Framework](https://formalgeo.github.io/)
- [Geoparsing (arXiv 2026)](https://arxiv.org/html/2604.11600)
- [SymHPR (arXiv 2025)](https://arxiv.org/pdf/2512.03126)
- [Math Blind (arXiv 2025)](https://arxiv.org/pdf/2503.20745)
- [DL4GPS Survey (ACL 2026)](https://github.com/majianz/dl4gps)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84538528-4729-4c04-82a4-2fa1d23e4994",
  "isSidechain": false,
  "requestId": "req_011CbSmWwXwTLpvy7RLMzv7B",
  "type": "assistant",
  "uuid": "7d288d82-4696-43b8-9172-67b0f2409462",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhsFV6cEhYWkQh3Wzx8LmQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 638,
      "cache_read_input_tokens": 27291,
      "output_tokens": 7204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 638,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7204,
          "cache_read_input_tokens": 27291,
          "cache_creation_input_tokens": 638,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 638
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

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem  Current multimodal math reasoning systems lack mechanisms to verify whether their perceived visual facts are mutua…",
  "leafUuid": "7d288d82-4696-43b8-9172-67b0f2409462",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Axiom-Grounded Self-Verified Perception for Visual Math Reasoning  ## Core Problem  Current multimodal math reasoning systems lack mechanisms to verify whether their perceived visual facts are mutua…",
  "leafUuid": "7d288d82-4696-43b8-9172-67b0f2409462",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Axiom-grounded self-verified perception for math reasoning",
  "sessionId": "85a148a6-4b0f-4266-a8e7-f5b117647ad4"
}
```

---
