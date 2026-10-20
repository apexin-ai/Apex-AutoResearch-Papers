# Research conversation: You are a senior ML researcher conducting a comprehensive literature survey. **Today's date: 2026-05-29 (UTC).** ## Task

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 74
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/chats/exported-trajectories/account-1/48bf462a-d28d-43ae-96da-d57db5986663.jsonl`
- **Structured JSON:** [`4d0c484f6f0d7c1275f8.json`](../../sessions/4d/4d0c484f6f0d7c1275f8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T05:15:49.556Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T05:15:49.556Z",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "content": "You are a senior ML researcher conducting a comprehensive literature survey.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Task\nFind the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:\n\n**Target: AAAI 2026\nTrack: AI Alignment / Main Technical Track — Robustness Evaluation\n\nDirection: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated \"genuine capability\" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.\n\nSeed Papers:\n- Zawalski et al. \"CoDeC\" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation\n- Li et al. \"ATLAS\" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity\n- Hou et al. \"MaSTer\" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination\n- Zheng et al. \"ReasoningMath-Plus\" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component\n- Chen et al. \"Reasoning Models Don't Always Say What They Think\" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination\n- Xu et al. \"DCR\" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis\n- Kocetkov et al. \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches\n\nKnown Gaps:\n- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)\n- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only\n- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing\n- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives\n\nTheoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)\n- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)\n- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth\n\nQuality Self-Checks:\n- [x] Core insight: \"Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level.\"\n- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.\n- [x] Baseline fear test: A simple baseline of \"run on variants and average\" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.\n- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.\n\nAvoid:\n- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)\n- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark\n- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)\n- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead**\n\n## What counts as 'important'\n\nPrioritize (in order):\n1. **Best paper awards** at top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, AAAI, etc.)\n2. **Oral / spotlight presentations** at these venues\n3. **Highly cited papers** (>50 citations in 1-2 years)\n4. **Papers that introduced widely-adopted methods** (e.g., new training paradigm, new benchmark)\n5. **Recent survey papers** that provide comprehensive field overviews\n6. **Strong recent work** from top labs (Google, Meta, DeepMind, OpenAI, CMU, Stanford, etc.)\n\n## Search strategy\n\nExecute AT LEAST 15 targeted searches:\n\n1. `best paper award ACL EMNLP NeurIPS ICML ICLR 2026 Target: AAAI 2026\nTrack: AI Alignment / Main Technical Track — Robustness Evaluation\n\nDirection: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated \"genuine capability\" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.\n\nSeed Papers:\n- Zawalski et al. \"CoDeC\" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation\n- Li et al. \"ATLAS\" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity\n- Hou et al. \"MaSTer\" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination\n- Zheng et al. \"ReasoningMath-Plus\" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component\n- Chen et al. \"Reasoning Models Don't Always Say What They Think\" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination\n- Xu et al. \"DCR\" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis\n- Kocetkov et al. \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches\n\nKnown Gaps:\n- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)\n- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only\n- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing\n- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives\n\nTheoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)\n- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)\n- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth\n\nQuality Self-Checks:\n- [x] Core insight: \"Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level.\"\n- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.\n- [x] Baseline fear test: A simple baseline of \"run on variants and average\" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.\n- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.\n\nAvoid:\n- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)\n- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark\n- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)\n- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead`\n2. `oral spotlight {venue} 2026 {topic}` — for each major venue\n3. `site:openreview.net {topic} 2026 outstanding` — OpenReview 高分论文\n4. `{topic} survey 2026` 或 `{topic} survey 2025` — 综述论文\n5. `site:arxiv.org {topic} 2026` — arXiv 最新高引\n6. `most cited {topic} 2025 2026` — Google Scholar\n7. `site:paperswithcode.com {task} SOTA` — SOTA 排行榜上的论文\n8. `{topic} benchmark {year}` — 定义领域的 benchmark 论文\n9. 对每个找到的重要论文，搜索其 cited-by 发现后续工作\n\nFor EVERY paper you find, use WebFetch to read its abstract and introduction on arXiv or OpenReview. Do NOT rely on search snippets alone — you need to understand what each paper actually does.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Full paper title\",\n  \"authors\": \"First author et al.\",\n  \"venue\": \"EMNLP 2025 / NeurIPS 2024 / arXiv 2025 / ...\",\n  \"url\": \"https://arxiv.org/abs/... or openreview URL\",\n  \"why_important\": \"Best paper / Oral / High-cited / Introduced X / ...\",\n  \"one_line_summary\": \"What this paper does in one sentence\"\n}\n\nFind at least 15 papers. More is better if they are genuinely relevant.\nIMPORTANT: You MUST end your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T05:15:49.562Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T05:15:49.562Z",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

## Round 1

72 recorded events

### User

_source line 3 · 2026-05-29T05:15:49.584Z_

You are a senior ML researcher conducting a comprehensive literature survey.

**Today's date: 2026-05-29 (UTC).**

## Task
Find the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:

**Target: AAAI 2026
Track: AI Alignment / Main Technical Track — Robustness Evaluation

Direction: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated "genuine capability" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.

Seed Papers:
- Zawalski et al. "CoDeC" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation
- Li et al. "ATLAS" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity
- Hou et al. "MaSTer" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination
- Zheng et al. "ReasoningMath-Plus" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component
- Chen et al. "Reasoning Models Don't Always Say What They Think" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination
- Xu et al. "DCR" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis
- Kocetkov et al. "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches

Known Gaps:
- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)
- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only
- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing
- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives

Theoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.

Constraints:
- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)
- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)
- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth

Quality Self-Checks:
- [x] Core insight: "Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level."
- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.
- [x] Baseline fear test: A simple baseline of "run on variants and average" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.
- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.

Avoid:
- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)
- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark
- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)
- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead**

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
Track: AI Alignment / Main Technical Track — Robustness Evaluation

Direction: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated "genuine capability" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.

Seed Papers:
- Zawalski et al. "CoDeC" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation
- Li et al. "ATLAS" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity
- Hou et al. "MaSTer" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination
- Zheng et al. "ReasoningMath-Plus" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component
- Chen et al. "Reasoning Models Don't Always Say What They Think" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination
- Xu et al. "DCR" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis
- Kocetkov et al. "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches

Known Gaps:
- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)
- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only
- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing
- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives

Theoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.

Constraints:
- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)
- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)
- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth

Quality Self-Checks:
- [x] Core insight: "Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level."
- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.
- [x] Baseline fear test: A simple baseline of "run on variants and average" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.
- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.

Avoid:
- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)
- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark
- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)
- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead`
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
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "3181c2ff-3fcb-49c8-8881-661340694936",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T05:15:49.582Z_

```json
{
  "parentUuid": "3181c2ff-3fcb-49c8-8881-661340694936",
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
  "uuid": "fc827da3-ae21-46a8-b53b-7581091eb8be",
  "timestamp": "2026-05-29T05:15:49.582Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T05:15:49.582Z_

```json
{
  "parentUuid": "fc827da3-ae21-46a8-b53b-7581091eb8be",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "aecb5c63-5cb1-45ba-bcf2-5110c3dcfc23",
  "timestamp": "2026-05-29T05:15:49.582Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
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
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Assistant

_source line 7 · 2026-05-29T05:15:54.072Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a comprehensive literature survey for their CRADE framework paper targeting AAAI 2026. I need to find the 15 most important recent papers (2024-2026) related to their research area, which sits at the intersection of:

1. Benchmark contamination detection/mitigation
2. Adversarial robustness evaluation for LLMs
3. Item Response Theory (IRT) for LLM evaluation
4. Step-level reasoning evaluation
5. Chain-of-thought faithfulness

Let me launch multiple search agents in parallel to cover different aspects of this research area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aecb5c63-5cb1-45ba-bcf2-5110c3dcfc23",
  "isSidechain": false,
  "requestId": "req_011CbWHrYLV9MPkF6CJHKomP",
  "type": "assistant",
  "uuid": "389f0313-7f23-4cee-8ac2-afc984829486",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcb2NJHzUR4XuVk5fG1vob",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15557,
      "cache_read_input_tokens": 0,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 267,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15557
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

_source line 8 · 2026-05-29T05:15:55.017Z_

I'll conduct a comprehensive literature survey by launching parallel search agents across the key research areas. Let me first load the WebSearch and WebFetch tools, then execute targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "389f0313-7f23-4cee-8ac2-afc984829486",
  "isSidechain": false,
  "requestId": "req_011CbWHrYLV9MPkF6CJHKomP",
  "type": "assistant",
  "uuid": "773d0d1b-952f-4ad9-aadd-4555b9d5d0c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcb2NJHzUR4XuVk5fG1vob",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15557,
      "cache_read_input_tokens": 0,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 267,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15557
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

_source line 9 · 2026-05-29T05:15:55.474Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Y7LX5eGnukubSPg4Yvg11y`</summary>

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
  "parentUuid": "773d0d1b-952f-4ad9-aadd-4555b9d5d0c6",
  "isSidechain": false,
  "requestId": "req_011CbWHrYLV9MPkF6CJHKomP",
  "type": "assistant",
  "uuid": "e1a58c8b-8124-41be-a732-3fd6dadedca0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bcb2NJHzUR4XuVk5fG1vob",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15557,
      "cache_read_input_tokens": 0,
      "output_tokens": 267,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15557,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 267,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15557,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15557
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

_source line 10 · 2026-05-29T05:15:55.482Z_

<details><summary>↩ Tool result · `toolu_01Y7LX5eGnukubSPg4Yvg11y`</summary>

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
  "parentUuid": "e1a58c8b-8124-41be-a732-3fd6dadedca0",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "c4a3be69-4b9e-46f9-91e2-d0fa4a20412d",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e1a58c8b-8124-41be-a732-3fd6dadedca0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "c4a3be69-4b9e-46f9-91e2-d0fa4a20412d",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Assistant

_source line 13 · 2026-05-29T05:16:01.498Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the WebSearch and WebFetch tools available. Let me launch multiple parallel search agents to cover the different research areas comprehensively. I'll organize searches around the key themes:

1. Benchmark contamination detection & mitigation for LLMs
2. Adversarial robustness evaluation / perturbation methods for LLM benchmarks
3. Item Response Theory (IRT) for LLM evaluation
4. Step-level / process-level reasoning evaluation
5. Chain-of-thought faithfulness


6. Best paper awards at top venues 2024-2026
7. Dynamic benchmarks and contamination-free evaluation
8. Contamination-aware scoring/calibration

I'll spin up agents to search across all these areas in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4a3be69-4b9e-46f9-91e2-d0fa4a20412d",
  "isSidechain": false,
  "requestId": "req_011CbWHryM8x1LuytvHA3oeo",
  "type": "assistant",
  "uuid": "63774516-53a3-4fb7-be6e-83de7d22c817",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByToMC8ZkehYdxwvEHUf9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2217,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1287
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

_source line 14 · 2026-05-29T05:16:01.499Z_

Now let me launch parallel search agents across the key research areas to find the most important papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "63774516-53a3-4fb7-be6e-83de7d22c817",
  "isSidechain": false,
  "requestId": "req_011CbWHryM8x1LuytvHA3oeo",
  "type": "assistant",
  "uuid": "d68269e7-1052-428d-920f-ce86f9505bfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByToMC8ZkehYdxwvEHUf9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2217,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1287
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

_source line 15 · 2026-05-29T05:16:06.363Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GQA8ft76EKQm3YrRxcquu8`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search contamination detection papers",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on jointly modeling benchmark contamination and robustness in LLM evaluation.\n\nSearch for the most important recent papers (2024-2026) on LLM benchmark contamination detection and mitigation. Execute these searches:\n\n1. WebSearch: \"LLM benchmark contamination detection 2025 2026\"\n2. WebSearch: \"benchmark data contamination large language models evaluation 2025\"\n3. WebSearch: \"CoDeC contamination detection NVIDIA 2025 arXiv\"\n4. WebSearch: \"DCR contamination adjusted scores LLM evaluation 2025\"\n5. WebSearch: \"Kocetkov fragility benchmark contamination reasoning models 2025\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on papers that:\n- Detect contamination in LLM training data\n- Propose methods to adjust or correct benchmark scores for contamination\n- Study contamination in reasoning models specifically\n- Propose contamination-free evaluation approaches\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d68269e7-1052-428d-920f-ce86f9505bfa",
  "isSidechain": false,
  "requestId": "req_011CbWHryM8x1LuytvHA3oeo",
  "type": "assistant",
  "uuid": "d326bb7e-bfa7-4f24-aeba-dc007b61a1e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByToMC8ZkehYdxwvEHUf9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2217,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1287
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

_source line 16 · 2026-05-29T05:16:11.564Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NpRVia5Mtc9Wze6UH8Tk6G`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search adversarial robustness evaluation papers",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on jointly modeling benchmark contamination and robustness in LLM evaluation.\n\nSearch for the most important recent papers (2024-2026) on adversarial robustness evaluation of LLMs, particularly for math reasoning benchmarks. Execute these searches:\n\n1. WebSearch: \"adversarial math benchmark LLM robustness evaluation 2025 2026\"\n2. WebSearch: \"MaSTer automated adversarial math variant generation 2026\"\n3. WebSearch: \"GSM-Symbolic GSM-Plus MATH-Perturb adversarial benchmark variants 2025\"\n4. WebSearch: \"LLM reasoning robustness perturbation functional variants 2025 2026\"\n5. WebSearch: \"symbolic perturbation math problems LLM evaluation SymPy 2025\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on papers that:\n- Generate adversarial or perturbed variants of math/reasoning benchmarks\n- Evaluate LLM robustness to problem reformulations\n- Use symbolic methods for provably correct variant generation\n- Study the gap between performance on original vs. perturbed problems\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d326bb7e-bfa7-4f24-aeba-dc007b61a1e9",
  "isSidechain": false,
  "requestId": "req_011CbWHryM8x1LuytvHA3oeo",
  "type": "assistant",
  "uuid": "84ec0b59-f5ae-4f90-9d03-2f501bddc656",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByToMC8ZkehYdxwvEHUf9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2217,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1287
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

_source line 17 · 2026-05-29T05:16:15.819Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01M7oV3yXySs1UhHpDtawjaM`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search IRT for LLM evaluation papers",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on jointly modeling benchmark contamination and robustness in LLM evaluation using Item Response Theory.\n\nSearch for the most important recent papers (2024-2026) on Item Response Theory applied to LLM evaluation. Execute these searches:\n\n1. WebSearch: \"item response theory LLM evaluation 2025 2026\"\n2. WebSearch: \"ATLAS IRT adaptive testing large language models 2025\"\n3. WebSearch: \"PSN-IRT LLM benchmark evaluation 2024 2025\"\n4. WebSearch: \"computerized adaptive testing LLM ability estimation 2025\"\n5. WebSearch: \"measurement theory psychometrics LLM evaluation calibration 2025\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on papers that:\n- Apply IRT or other psychometric models to LLM evaluation\n- Propose adaptive testing for efficient LLM benchmarking\n- Use measurement theory to produce calibrated ability scores\n- Study item difficulty and discrimination for LLM test items\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84ec0b59-f5ae-4f90-9d03-2f501bddc656",
  "isSidechain": false,
  "requestId": "req_011CbWHryM8x1LuytvHA3oeo",
  "type": "assistant",
  "uuid": "00b42f36-9d14-456b-ae3a-b6219df9c57c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByToMC8ZkehYdxwvEHUf9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2217,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1287
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

_source line 18 · 2026-05-29T05:16:21.233Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01L5AkD1RttbRthhqDtnFrGq`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search step-level reasoning evaluation papers",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on step-level reasoning evaluation and chain-of-thought faithfulness in LLMs.\n\nSearch for the most important recent papers (2024-2026) on step-level/process-level reasoning evaluation and CoT faithfulness. Execute these searches:\n\n1. WebSearch: \"step level reasoning evaluation LLM process reward model 2025 2026\"\n2. WebSearch: \"ReasoningMath-Plus step level evaluation math 2026\"\n3. WebSearch: \"chain of thought faithfulness LLM reasoning 2025 Anthropic\"\n4. WebSearch: \"reasoning models don't always say what they think Chen Anthropic 2025\"\n5. WebSearch: \"process level verification math reasoning LLM 2025\"\n6. WebSearch: \"CoT unfaithful reasoning LLM evaluation 2025 2026\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on papers that:\n- Evaluate reasoning at the step/process level rather than just final answers\n- Study faithfulness of chain-of-thought reasoning\n- Propose process reward models or step-level verification\n- Show discrepancies between step-level and answer-level evaluation\n- Study whether LLMs actually reason or just pattern match\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "00b42f36-9d14-456b-ae3a-b6219df9c57c",
  "isSidechain": false,
  "requestId": "req_011CbWHryM8x1LuytvHA3oeo",
  "type": "assistant",
  "uuid": "3a8ed8a3-1e30-4641-8f86-be0acf42a698",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByToMC8ZkehYdxwvEHUf9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2217,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1287
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

_source line 19 · 2026-05-29T05:16:26.505Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01EcAtgVcT4JMhkPK4Q2Xvyx`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search best papers and LLM eval frameworks",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on LLM evaluation robustness and contamination.\n\nSearch for best paper awards, highly-cited papers, and comprehensive evaluation frameworks from 2024-2026. Execute these searches:\n\n1. WebSearch: \"best paper award NeurIPS 2025 LLM evaluation\"\n2. WebSearch: \"best paper award ICML 2025 language model\"  \n3. WebSearch: \"best paper award ICLR 2025 2026 LLM benchmark\"\n4. WebSearch: \"LiveBench MathArena dynamic benchmark LLM contamination-free 2025 2026\"\n5. WebSearch: \"LLM evaluation framework robustness contamination survey 2025 2026\"\n6. WebSearch: \"site:openreview.net LLM benchmark contamination robustness 2025 outstanding\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on:\n- Best paper / oral / spotlight papers related to LLM evaluation\n- Comprehensive evaluation frameworks\n- Dynamic or contamination-resistant benchmarks\n- Survey papers on LLM evaluation methodology\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a8ed8a3-1e30-4641-8f86-be0acf42a698",
  "isSidechain": false,
  "requestId": "req_011CbWHryM8x1LuytvHA3oeo",
  "type": "assistant",
  "uuid": "b228f88d-2d8f-48a1-a836-00f11d297713",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByToMC8ZkehYdxwvEHUf9Q",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1287,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2217,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2217,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1287
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

_source line 20 · 2026-05-29T05:19:20.233Z_

<details><summary>↩ Tool result · `toolu_01GQA8ft76EKQm3YrRxcquu8`</summary>

```text
Now I have comprehensive data on all the important papers. Here is the structured list:

---

## Literature Survey: LLM Benchmark Contamination Detection and Mitigation (2024-2026)

### CATEGORY 1: CONTAMINATION DETECTION METHODS

**1. CoDeC: Detecting Data Contamination in LLMs via In-Context Learning**
- **Authors:** Michal Zawalski, Meriem Boubdir, Klaudia Balazy, Besmira Nushi, Pablo Ribalta (NVIDIA-affiliated)
- **Venue:** ICLR 2026 (accepted); arXiv:2510.27055
- **URL:** [https://arxiv.org/abs/2510.27055](https://arxiv.org/abs/2510.27055)
- **Summary:** Detects contamination by measuring how in-context learning affects model confidence -- ICL boosts confidence on unseen data but may reduce it on memorized data.
- **Why important:** Model- and dataset-agnostic black-box method; produces interpretable contamination scores; directly integrable into benchmark evaluations. State-of-the-art practical detection method.

**2. PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models**
- **Authors:** Huixuan Zhang, Yun Lin, Xiaojun Wan
- **Venue:** arXiv:2406.18326 (2024, revised March 2025)
- **URL:** [https://arxiv.org/abs/2406.18326](https://arxiv.org/abs/2406.18326)
- **Summary:** Constructs distributional counterparts of benchmark data and performs statistical significance testing on model confidence differences to detect contamination.
- **Why important:** Found nearly all tested popular models show some degree of suspected contamination; provides a principled statistical framework for detection.

**3. Detecting Benchmark Contamination Through Watermarking**
- **Authors:** Tom Sander, Pierre Fernandez, Saeed Mahloujifar, Alain Durmus, Chuan Guo
- **Venue:** arXiv:2502.17259 (Feb 2025, revised July 2025)
- **URL:** [https://arxiv.org/abs/2502.17259](https://arxiv.org/abs/2502.17259)
- **Summary:** Embeds non-intrusive watermarks in benchmark datasets before release; detects "radioactivity" traces left by watermarked text in training, providing a p-value as contamination score.
- **Why important:** Proactive (pre-release) detection approach rather than post-hoc; achieves p-values of 10^-3 for +5% accuracy inflation; preserves benchmark quality.

**4. Estimating Contamination via Perplexity: Quantifying Memorisation in Language Model Evaluation**
- **Authors:** Yucheng Li
- **Venue:** arXiv:2309.10677 (2023)
- **URL:** [https://arxiv.org/abs/2309.10677](https://arxiv.org/abs/2309.10677)
- **Summary:** Uses perplexity-based measurements to quantify data contamination without access to training data; reveals substantial memorization in foundation models on reading comprehension and summarization benchmarks.
- **Why important:** Foundational black-box detection method that works without training data access; widely cited baseline approach.

**5. Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models (CDD/TED)**
- **Authors:** Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, Ge Li
- **Venue:** arXiv:2402.15938 (Feb 2024)
- **URL:** [https://arxiv.org/abs/2402.15938](https://arxiv.org/abs/2402.15938)
- **Summary:** Proposes CDD (detection via output distribution peakedness) and TED (trustworthy evaluation via output distribution correction); CDD improves detection by 21.8-30.2% over prior methods; TED reduces contamination-driven performance gains by up to 66.9%.
- **Why important:** Jointly addresses both detection AND mitigation; provides evidence of ChatGPT contamination on HumanEval; one of few papers proposing score correction.

**6. Investigating Data Contamination in Modern Benchmarks for Large Language Models**
- **Authors:** Chunyuan Deng, Yilun Zhao, Xiangru Tang, Mark Gerstein, Arman Cohan
- **Venue:** arXiv:2311.09783 (Nov 2023, revised April 2024)
- **URL:** [https://arxiv.org/abs/2311.09783](https://arxiv.org/abs/2311.09783)
- **Summary:** Proposes "Testset Slot Guessing" -- masks incorrect answers/unlikely words and measures model ability to reconstruct them; GPT-4 achieved 57% exact match on MMLU masked options.
- **Why important:** Works on both open and proprietary models; provides alarming evidence of contamination in commercial LLMs.

**7. Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation**
- **Authors:** Naila Shafirni Hidayat, Muhammad Dehan Al Kautsar, Alfan Farizki Wicaksono, Fajri Koto
- **Venue:** Eval4NLP Workshop 2025; arXiv:2505.24263
- **URL:** [https://arxiv.org/abs/2505.24263](https://arxiv.org/abs/2505.24263)
- **Summary:** Benchmarks existing leakage detection methods (permutation, n-gram, semi-half question) under controlled continual pretraining simulation; finds n-gram methods achieve highest F1; creates cleaned MMLU and HellaSwag versions.
- **Why important:** Provides empirical comparison of detection methods under controlled conditions; produces decontaminated benchmark versions.

**8. Rethinking Benchmark and Contamination for Language Models with Rephrased Samples**
- **Authors:** Shuo Yang, Wei-Lin Chiang, Lianmin Zheng, Joseph E. Gonzalez, Ion Stoica
- **Venue:** arXiv:2311.04850 (Nov 2023)
- **URL:** [https://arxiv.org/abs/2311.04850](https://arxiv.org/abs/2311.04850)
- **Summary:** Shows string-matching decontamination is insufficient -- paraphrased test data bypasses safeguards; a 13B model can fake GPT-4 performance via undetected benchmark overfitting; proposes LLM-based decontamination and finds 8-18% HumanEval contamination in RedPajama/StarCoder.
- **Why important:** Demonstrates fundamental weakness of n-gram decontamination; quantifies contamination in major pretraining datasets.

---

### CATEGORY 2: CONTAMINATION SCORE ADJUSTMENT / QUANTIFICATION

**9. DCR: Quantifying Data Contamination in LLMs Evaluation**
- **Authors:** Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, M-Tahar Kechadi
- **Venue:** EMNLP 2025; arXiv:2507.11405
- **URL:** [https://arxiv.org/abs/2507.11405](https://arxiv.org/abs/2507.11405)
- **Summary:** Proposes a lightweight pipeline to detect and quantify contamination risk at four levels (semantic, informational, data, label); synthesizes a unified DCR Factor via fuzzy inference to adjust raw accuracy; achieves within 4% error of uncontaminated baselines across 9 LLMs.
- **Why important:** CRITICAL for joint contamination-robustness modeling -- provides the DCR Factor as a practical metric to produce contamination-adjusted benchmark scores. Directly relevant to the AAAI paper topic.

**10. How Can I Publish My LLM Benchmark Without Giving the True Answers Away?**
- **Authors:** Takashi Ishida, Thanawat Lodkaew, Ikko Yamane
- **Venue:** ICML 2025 Workshop (Oral); arXiv:2505.18102
- **URL:** [https://arxiv.org/abs/2505.18102](https://arxiv.org/abs/2505.18102)
- **Summary:** Proposes publishing benchmarks with injected randomness (multiple correct answers, one designated); caps theoretical max accuracy (Bayes accuracy), so models exceeding it are flagged as contaminated.
- **Why important:** Novel benchmark design philosophy that makes contamination self-revealing; ceiling-based detection approach.

---

### CATEGORY 3: CONTAMINATION IN REASONING MODELS

**11. On The Fragility of Benchmark Contamination Detection in Reasoning Models**
- **Authors:** Han Wang, Haoyu Li, Brian Ko, Huan Zhang
- **Venue:** arXiv:2510.02386 (Sept 2025, revised March 2026)
- **URL:** [https://arxiv.org/abs/2510.02386](https://arxiv.org/abs/2510.02386)
- **Summary:** Shows that RL training (PPO-style) effectively conceals SFT contamination signals in reasoning models, and CoT contamination on advanced LRMs leaves near-zero detectable evidence; existing detectors perform at random-guess level.
- **Why important:** CRITICAL paper for the AAAI topic -- directly demonstrates that contamination detection breaks down for reasoning models, creating an urgent need for new methods that jointly consider robustness and contamination.

**12. Test of Time: Rethinking Temporal Signal of Benchmark Contamination**
- **Authors:** Terry Jingchen Zhang, Gopal Dev, Ning Wang, Max Obreiter, Punya Syon Pandey, Keenan Samway, Wenyuan Jiang, Yinya Huang, Bernhard Scholkopf, Mrinmaya Sachan, Zhijing Jin
- **Venue:** arXiv:2509.00072 (Aug 2025, revised May 2026)
- **URL:** [https://arxiv.org/abs/2509.00072](https://arxiv.org/abs/2509.00072)
- **Summary:** Challenges the assumption that post-cutoff performance decay indicates contamination; shows question structure (not just source material) determines whether temporal patterns emerge; provides mechanistic insight via influence functions.
- **Why important:** Reveals fragility of temporal-signal-based contamination detection; calls for more robust evaluation paradigms.

---

### CATEGORY 4: CONTAMINATION SCALING AND FORGETTING

**13. How Much Can We Forget about Data Contamination?**
- **Authors:** Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, Ulrike von Luxburg
- **Venue:** ICML 2025; arXiv:2410.03249
- **URL:** [https://arxiv.org/abs/2410.03249](https://arxiv.org/abs/2410.03249)
- **Summary:** Experimentally quantifies contamination overfitting across model size (up to 1.6B), repetition (up to 144x), and training tokens (up to 40B); finds that even 144x contamination is "forgotten" when training data exceeds 5x Chinchilla optimal.
- **Why important:** Provides the scaling-law perspective on when contamination matters vs. when it washes out; essential counterpoint showing contamination severity depends on training regime.

---

### CATEGORY 5: CONTAMINATION-FREE / DYNAMIC EVALUATION

**14. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**
- **Authors:** Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, Siddhartha Jain, et al. (incl. Yann LeCun, Tom Goldstein, Micah Goldblum)
- **Venue:** ICLR 2025 (Spotlight); arXiv:2406.19314
- **URL:** [https://arxiv.org/abs/2406.19314](https://arxiv.org/abs/2406.19314)
- **Summary:** Monthly-updated benchmark with questions from recent sources (math competitions, arXiv, news); uses objective ground-truth scoring without LLM judges; spans math, coding, reasoning, language, instruction following, and data analysis.
- **Why important:** Leading contamination-resistant benchmark; top models score below 70%, showing headroom; monthly refresh cycle directly mitigates contamination.

**15. LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code**
- **Authors:** Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, Ion Stoica
- **Venue:** arXiv:2403.07974 (March 2024)
- **URL:** [https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)
- **Summary:** Continuously collects new coding problems from LeetCode, AtCoder, and CodeForces; evaluates code generation, self-repair, code execution, and test output prediction; 1055+ problems through April 2025.
- **Why important:** Gold-standard contamination-free code evaluation; temporal collection ensures freshness; widely adopted for code LLM evaluation.

**16. BeyondBench: Contamination-Resistant Evaluation of Reasoning in Language Models**
- **Authors:** Gaurav Srivastava, Aafiya Hussain, Zhenyu Bi, Swastik Roy, Priya Pitre, Meng Lu, Morteza Ziyadi, Xuan Wang
- **Venue:** arXiv:2509.24210 (Sept 2025, revised March 2026)
- **URL:** [https://arxiv.org/abs/2509.24210](https://arxiv.org/abs/2509.24210)
- **Summary:** Generates algorithmic problems dynamically (10^15+ unique instances per task) across 44 tasks in 3 difficulty tiers; evaluates 101 models; Gemini-2.5-pro achieves only 56.21% on hard suite; reveals 40%+ accuracy drops without computational tools.
- **Why important:** Infinite-instance generation makes pretraining contamination mathematically impossible; reveals genuine reasoning limitations masked by static benchmark contamination.

**17. LiveMedBench: A Contamination-Free Medical Benchmark for LLMs with Automated Rubric Evaluation**
- **Authors:** Zhiling Yan, Dingjie Song, Zhe Fang, Yisheng Ji, Xiang Li, Quanzheng Li, Lichao Sun
- **Venue:** arXiv:2602.10367 (Feb 2026)
- **URL:** [https://arxiv.org/abs/2602.10367](https://arxiv.org/abs/2602.10367)
- **Summary:** Weekly-updated medical benchmark with 2,756 cases across 38 specialties; multi-agent clinical validation; best model achieves only 39.2%; 84% of models degrade on newer cases.
- **Why important:** Domain-specific contamination-free benchmark; demonstrates temporal degradation pattern consistent with contamination in medical LLM evaluations.

**18. When Benchmarks Leak: Inference-Time Decontamination for LLMs (DeconIEP)**
- **Authors:** Jianzhe Chai, Yu Zhe, Jun Sakuma
- **Venue:** arXiv:2601.19334 (Jan 2026)
- **URL:** [https://arxiv.org/abs/2601.19334](https://arxiv.org/abs/2601.19334)
- **Summary:** Applies small bounded perturbations in the input embedding space at inference time, guided by a less-contaminated reference model, to redirect models away from memorization-driven shortcuts.
- **Why important:** Novel inference-time mitigation approach that does not alter the evaluation set or require retraining; directly addresses the robustness-contamination interface.

---

### CATEGORY 6: SURVEYS

**19. Benchmark Data Contamination of Large Language Models: A Survey**
- **Authors:** Cheng Xu, Shuhao Guan, Derek Greene, M-Tahar Kechadi
- **Venue:** arXiv:2406.04244 (June 2024)
- **URL:** [https://arxiv.org/abs/2406.04244](https://arxiv.org/abs/2406.04244)
- **Summary:** Comprehensive survey covering contamination taxonomy, detection methods, and alternative evaluation approaches for LLMs including GPT-4, Claude-3, and Gemini.
- **Why important:** Foundational survey paper; establishes taxonomy and terminology for the field.

**20. Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation**
- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray
- **Venue:** EMNLP 2025 (Main Conference)
- **URL:** [https://aclanthology.org/2025.emnlp-main.511/](https://aclanthology.org/2025.emnlp-main.511/)
- **Summary:** Charts the evolution from static to dynamic benchmarking paradigms; analyzes limitations of static enhancements (data encryption, post-hoc detection); proposes design principles for dynamic benchmarks.
- **Why important:** Top-venue survey at EMNLP 2025; provides the static-to-dynamic evaluation framework with maintained GitHub repository.

**21. A Survey on Data Contamination for Large Language Models**
- **Authors:** Yuxing Cheng, Yi Chang, Yuan Wu
- **Venue:** arXiv:2502.14425 (Feb 2025)
- **URL:** [https://arxiv.org/abs/2502.14425](https://arxiv.org/abs/2502.14425)
- **Summary:** Covers contamination-free evaluation strategies (data updating, rewriting, prevention), dynamic evaluation (rule-based, agent-based), and detection techniques (white-box, gray-box, black-box).
- **Why important:** Most recent comprehensive survey; provides clean taxonomy of detection methods by information access requirements.

**22. LLM Benchmark Datasets Should Be Contamination-Resistant**
- **Authors:** Ali Al-Lawati, Jason Lucas, Dongwon Lee, Suhang Wang
- **Venue:** arXiv:2605.19999 (May 2026)
- **URL:** [https://arxiv.org/abs/2605.19999](https://arxiv.org/abs/2605.19999)
- **Summary:** Proposes leveraging asymmetries in Transformer inference vs. training processes to build inherently contamination-resistant benchmarks; calls for community adoption of contamination-resistant evaluation pipelines.
- **Why important:** Most recent position/methodology paper (May 2026); proposes architectural-level solutions rather than data-level workarounds.

---

### SUMMARY OF MOST CRITICAL PAPERS FOR THE AAAI 2026 PAPER

For a paper on **jointly modeling benchmark contamination and robustness in LLM evaluation**, the highest-priority papers are:

1. **DCR (Paper #9)** -- directly provides contamination-adjusted scores, the closest existing work to joint contamination-robustness modeling
2. **Wang et al. Fragility (Paper #11)** -- shows contamination detection breaks for reasoning models, motivating the need for joint approaches
3. **CoDeC (Paper #1)** -- state-of-the-art detection method, accepted at ICLR 2026
4. **Dong et al. CDD/TED (Paper #5)** -- jointly detects and mitigates contamination via output distribution
5. **Bordt et al. Forgetting (Paper #13)** -- provides scaling-law perspective on when contamination matters
6. **DeconIEP (Paper #18)** -- inference-time decontamination connecting robustness and contamination
7. **BeyondBench (Paper #16)** -- contamination-impossible evaluation for reasoning
8. **Chen et al. Static-to-Dynamic Survey (Paper #20)** -- EMNLP 2025 survey providing field context

Sources:
- [CoDeC - arXiv:2510.27055](https://arxiv.org/abs/2510.27055)
- [PaCoST - arXiv:2406.18326](https://arxiv.org/abs/2406.18326)
- [Watermarking Detection - arXiv:2502.17259](https://arxiv.org/abs/2502.17259)
- [Perplexity Contamination - arXiv:2309.10677](https://arxiv.org/abs/2309.10677)
- [CDD/TED - arXiv:2402.15938](https://arxiv.org/abs/2402.15938)
- [Testset Slot Guessing - arXiv:2311.09783](https://arxiv.org/abs/2311.09783)
- [Simulating Leakage - arXiv:2505.24263](https://arxiv.org/abs/2505.24263)
- [Rephrased Samples - arXiv:2311.04850](https://arxiv.org/abs/2311.04850)
- [DCR - arXiv:2507.11405](https://arxiv.org/abs/2507.11405)
- [Benchmark Without Answers - arXiv:2505.18102](https://arxiv.org/abs/2505.18102)
- [Fragility in Reasoning Models - arXiv:2510.02386](https://arxiv.org/abs/2510.02386)
- [Test of Time - arXiv:2509.00072](https://arxiv.org/abs/2509.00072)
- [Forgetting Contamination - arXiv:2410.03249](https://arxiv.org/abs/2410.03249)
- [LiveBench - arXiv:2406.19314](https://arxiv.org/abs/2406.19314)
- [LiveCodeBench - arXiv:2403.07974](https://arxiv.org/abs/2403.07974)
- [BeyondBench - arXiv:2509.24210](https://arxiv.org/abs/2509.24210)
- [LiveMedBench - arXiv:2602.10367](https://arxiv.org/abs/2602.10367)
- [DeconIEP - arXiv:2601.19334](https://arxiv.org/abs/2601.19334)
- [Xu et al. Survey - arXiv:2406.04244](https://arxiv.org/abs/2406.04244)
- [EMNLP 2025 Survey](https://aclanthology.org/2025.emnlp-main.511/)
- [Cheng et al. Survey - arXiv:2502.14425](https://arxiv.org/abs/2502.14425)
- [Contamination-Resistant Benchmarks - arXiv:2605.19999](https://arxiv.org/abs/2605.19999)
- [LLM-Stats Guide](https://llm-stats.com/blog/research/what-is-a-contaminated-llm)

agentId: ab85ba930c57f2f1b (use SendMessage with to: 'ab85ba930c57f2f1b' to continue this agent)
&lt;usage>total_tokens: 33715
tool_uses: 34
duration_ms: 193862&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d326bb7e-bfa7-4f24-aeba-dc007b61a1e9",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "f9d020a2-84cc-4764-a26b-f252cdd87ce8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on jointly modeling benchmark contamination and robustness in LLM evaluation.\n\nSearch for the most important recent papers (2024-2026) on LLM benchmark contamination detection and mitigation. Execute these searches:\n\n1. WebSearch: \"LLM benchmark contamination detection 2025 2026\"\n2. WebSearch: \"benchmark data contamination large language models evaluation 2025\"\n3. WebSearch: \"CoDeC contamination detection NVIDIA 2025 arXiv\"\n4. WebSearch: \"DCR contamination adjusted scores LLM evaluation 2025\"\n5. WebSearch: \"Kocetkov fragility benchmark contamination reasoning models 2025\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on papers that:\n- Detect contamination in LLM training data\n- Propose methods to adjust or correct benchmark scores for contamination\n- Study contamination in reasoning models specifically\n- Propose contamination-free evaluation approaches\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details.",
    "agentId": "ab85ba930c57f2f1b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data on all the important papers. Here is the structured list:\n\n---\n\n## Literature Survey: LLM Benchmark Contamination Detection and Mitigation (2024-2026)\n\n### CATEGORY 1: CONTAMINATION DETECTION METHODS\n\n**1. CoDeC: Detecting Data Contamination in LLMs via In-Context Learning**\n- **Authors:** Michal Zawalski, Meriem Boubdir, Klaudia Balazy, Besmira Nushi, Pablo Ribalta (NVIDIA-affiliated)\n- **Venue:** ICLR 2026 (accepted); arXiv:2510.27055\n- **URL:** [https://arxiv.org/abs/2510.27055](https://arxiv.org/abs/2510.27055)\n- **Summary:** Detects contamination by measuring how in-context learning affects model confidence -- ICL boosts confidence on unseen data but may reduce it on memorized data.\n- **Why important:** Model- and dataset-agnostic black-box method; produces interpretable contamination scores; directly integrable into benchmark evaluations. State-of-the-art practical detection method.\n\n**2. PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models**\n- **Authors:** Huixuan Zhang, Yun Lin, Xiaojun Wan\n- **Venue:** arXiv:2406.18326 (2024, revised March 2025)\n- **URL:** [https://arxiv.org/abs/2406.18326](https://arxiv.org/abs/2406.18326)\n- **Summary:** Constructs distributional counterparts of benchmark data and performs statistical significance testing on model confidence differences to detect contamination.\n- **Why important:** Found nearly all tested popular models show some degree of suspected contamination; provides a principled statistical framework for detection.\n\n**3. Detecting Benchmark Contamination Through Watermarking**\n- **Authors:** Tom Sander, Pierre Fernandez, Saeed Mahloujifar, Alain Durmus, Chuan Guo\n- **Venue:** arXiv:2502.17259 (Feb 2025, revised July 2025)\n- **URL:** [https://arxiv.org/abs/2502.17259](https://arxiv.org/abs/2502.17259)\n- **Summary:** Embeds non-intrusive watermarks in benchmark datasets before release; detects \"radioactivity\" traces left by watermarked text in training, providing a p-value as contamination score.\n- **Why important:** Proactive (pre-release) detection approach rather than post-hoc; achieves p-values of 10^-3 for +5% accuracy inflation; preserves benchmark quality.\n\n**4. Estimating Contamination via Perplexity: Quantifying Memorisation in Language Model Evaluation**\n- **Authors:** Yucheng Li\n- **Venue:** arXiv:2309.10677 (2023)\n- **URL:** [https://arxiv.org/abs/2309.10677](https://arxiv.org/abs/2309.10677)\n- **Summary:** Uses perplexity-based measurements to quantify data contamination without access to training data; reveals substantial memorization in foundation models on reading comprehension and summarization benchmarks.\n- **Why important:** Foundational black-box detection method that works without training data access; widely cited baseline approach.\n\n**5. Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models (CDD/TED)**\n- **Authors:** Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, Ge Li\n- **Venue:** arXiv:2402.15938 (Feb 2024)\n- **URL:** [https://arxiv.org/abs/2402.15938](https://arxiv.org/abs/2402.15938)\n- **Summary:** Proposes CDD (detection via output distribution peakedness) and TED (trustworthy evaluation via output distribution correction); CDD improves detection by 21.8-30.2% over prior methods; TED reduces contamination-driven performance gains by up to 66.9%.\n- **Why important:** Jointly addresses both detection AND mitigation; provides evidence of ChatGPT contamination on HumanEval; one of few papers proposing score correction.\n\n**6. Investigating Data Contamination in Modern Benchmarks for Large Language Models**\n- **Authors:** Chunyuan Deng, Yilun Zhao, Xiangru Tang, Mark Gerstein, Arman Cohan\n- **Venue:** arXiv:2311.09783 (Nov 2023, revised April 2024)\n- **URL:** [https://arxiv.org/abs/2311.09783](https://arxiv.org/abs/2311.09783)\n- **Summary:** Proposes \"Testset Slot Guessing\" -- masks incorrect answers/unlikely words and measures model ability to reconstruct them; GPT-4 achieved 57% exact match on MMLU masked options.\n- **Why important:** Works on both open and proprietary models; provides alarming evidence of contamination in commercial LLMs.\n\n**7. Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation**\n- **Authors:** Naila Shafirni Hidayat, Muhammad Dehan Al Kautsar, Alfan Farizki Wicaksono, Fajri Koto\n- **Venue:** Eval4NLP Workshop 2025; arXiv:2505.24263\n- **URL:** [https://arxiv.org/abs/2505.24263](https://arxiv.org/abs/2505.24263)\n- **Summary:** Benchmarks existing leakage detection methods (permutation, n-gram, semi-half question) under controlled continual pretraining simulation; finds n-gram methods achieve highest F1; creates cleaned MMLU and HellaSwag versions.\n- **Why important:** Provides empirical comparison of detection methods under controlled conditions; produces decontaminated benchmark versions.\n\n**8. Rethinking Benchmark and Contamination for Language Models with Rephrased Samples**\n- **Authors:** Shuo Yang, Wei-Lin Chiang, Lianmin Zheng, Joseph E. Gonzalez, Ion Stoica\n- **Venue:** arXiv:2311.04850 (Nov 2023)\n- **URL:** [https://arxiv.org/abs/2311.04850](https://arxiv.org/abs/2311.04850)\n- **Summary:** Shows string-matching decontamination is insufficient -- paraphrased test data bypasses safeguards; a 13B model can fake GPT-4 performance via undetected benchmark overfitting; proposes LLM-based decontamination and finds 8-18% HumanEval contamination in RedPajama/StarCoder.\n- **Why important:** Demonstrates fundamental weakness of n-gram decontamination; quantifies contamination in major pretraining datasets.\n\n---\n\n### CATEGORY 2: CONTAMINATION SCORE ADJUSTMENT / QUANTIFICATION\n\n**9. DCR: Quantifying Data Contamination in LLMs Evaluation**\n- **Authors:** Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, M-Tahar Kechadi\n- **Venue:** EMNLP 2025; arXiv:2507.11405\n- **URL:** [https://arxiv.org/abs/2507.11405](https://arxiv.org/abs/2507.11405)\n- **Summary:** Proposes a lightweight pipeline to detect and quantify contamination risk at four levels (semantic, informational, data, label); synthesizes a unified DCR Factor via fuzzy inference to adjust raw accuracy; achieves within 4% error of uncontaminated baselines across 9 LLMs.\n- **Why important:** CRITICAL for joint contamination-robustness modeling -- provides the DCR Factor as a practical metric to produce contamination-adjusted benchmark scores. Directly relevant to the AAAI paper topic.\n\n**10. How Can I Publish My LLM Benchmark Without Giving the True Answers Away?**\n- **Authors:** Takashi Ishida, Thanawat Lodkaew, Ikko Yamane\n- **Venue:** ICML 2025 Workshop (Oral); arXiv:2505.18102\n- **URL:** [https://arxiv.org/abs/2505.18102](https://arxiv.org/abs/2505.18102)\n- **Summary:** Proposes publishing benchmarks with injected randomness (multiple correct answers, one designated); caps theoretical max accuracy (Bayes accuracy), so models exceeding it are flagged as contaminated.\n- **Why important:** Novel benchmark design philosophy that makes contamination self-revealing; ceiling-based detection approach.\n\n---\n\n### CATEGORY 3: CONTAMINATION IN REASONING MODELS\n\n**11. On The Fragility of Benchmark Contamination Detection in Reasoning Models**\n- **Authors:** Han Wang, Haoyu Li, Brian Ko, Huan Zhang\n- **Venue:** arXiv:2510.02386 (Sept 2025, revised March 2026)\n- **URL:** [https://arxiv.org/abs/2510.02386](https://arxiv.org/abs/2510.02386)\n- **Summary:** Shows that RL training (PPO-style) effectively conceals SFT contamination signals in reasoning models, and CoT contamination on advanced LRMs leaves near-zero detectable evidence; existing detectors perform at random-guess level.\n- **Why important:** CRITICAL paper for the AAAI topic -- directly demonstrates that contamination detection breaks down for reasoning models, creating an urgent need for new methods that jointly consider robustness and contamination.\n\n**12. Test of Time: Rethinking Temporal Signal of Benchmark Contamination**\n- **Authors:** Terry Jingchen Zhang, Gopal Dev, Ning Wang, Max Obreiter, Punya Syon Pandey, Keenan Samway, Wenyuan Jiang, Yinya Huang, Bernhard Scholkopf, Mrinmaya Sachan, Zhijing Jin\n- **Venue:** arXiv:2509.00072 (Aug 2025, revised May 2026)\n- **URL:** [https://arxiv.org/abs/2509.00072](https://arxiv.org/abs/2509.00072)\n- **Summary:** Challenges the assumption that post-cutoff performance decay indicates contamination; shows question structure (not just source material) determines whether temporal patterns emerge; provides mechanistic insight via influence functions.\n- **Why important:** Reveals fragility of temporal-signal-based contamination detection; calls for more robust evaluation paradigms.\n\n---\n\n### CATEGORY 4: CONTAMINATION SCALING AND FORGETTING\n\n**13. How Much Can We Forget about Data Contamination?**\n- **Authors:** Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, Ulrike von Luxburg\n- **Venue:** ICML 2025; arXiv:2410.03249\n- **URL:** [https://arxiv.org/abs/2410.03249](https://arxiv.org/abs/2410.03249)\n- **Summary:** Experimentally quantifies contamination overfitting across model size (up to 1.6B), repetition (up to 144x), and training tokens (up to 40B); finds that even 144x contamination is \"forgotten\" when training data exceeds 5x Chinchilla optimal.\n- **Why important:** Provides the scaling-law perspective on when contamination matters vs. when it washes out; essential counterpoint showing contamination severity depends on training regime.\n\n---\n\n### CATEGORY 5: CONTAMINATION-FREE / DYNAMIC EVALUATION\n\n**14. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**\n- **Authors:** Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, Siddhartha Jain, et al. (incl. Yann LeCun, Tom Goldstein, Micah Goldblum)\n- **Venue:** ICLR 2025 (Spotlight); arXiv:2406.19314\n- **URL:** [https://arxiv.org/abs/2406.19314](https://arxiv.org/abs/2406.19314)\n- **Summary:** Monthly-updated benchmark with questions from recent sources (math competitions, arXiv, news); uses objective ground-truth scoring without LLM judges; spans math, coding, reasoning, language, instruction following, and data analysis.\n- **Why important:** Leading contamination-resistant benchmark; top models score below 70%, showing headroom; monthly refresh cycle directly mitigates contamination.\n\n**15. LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code**\n- **Authors:** Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, Ion Stoica\n- **Venue:** arXiv:2403.07974 (March 2024)\n- **URL:** [https://arxiv.org/abs/2403.07974](https://arxiv.org/abs/2403.07974)\n- **Summary:** Continuously collects new coding problems from LeetCode, AtCoder, and CodeForces; evaluates code generation, self-repair, code execution, and test output prediction; 1055+ problems through April 2025.\n- **Why important:** Gold-standard contamination-free code evaluation; temporal collection ensures freshness; widely adopted for code LLM evaluation.\n\n**16. BeyondBench: Contamination-Resistant Evaluation of Reasoning in Language Models**\n- **Authors:** Gaurav Srivastava, Aafiya Hussain, Zhenyu Bi, Swastik Roy, Priya Pitre, Meng Lu, Morteza Ziyadi, Xuan Wang\n- **Venue:** arXiv:2509.24210 (Sept 2025, revised March 2026)\n- **URL:** [https://arxiv.org/abs/2509.24210](https://arxiv.org/abs/2509.24210)\n- **Summary:** Generates algorithmic problems dynamically (10^15+ unique instances per task) across 44 tasks in 3 difficulty tiers; evaluates 101 models; Gemini-2.5-pro achieves only 56.21% on hard suite; reveals 40%+ accuracy drops without computational tools.\n- **Why important:** Infinite-instance generation makes pretraining contamination mathematically impossible; reveals genuine reasoning limitations masked by static benchmark contamination.\n\n**17. LiveMedBench: A Contamination-Free Medical Benchmark for LLMs with Automated Rubric Evaluation**\n- **Authors:** Zhiling Yan, Dingjie Song, Zhe Fang, Yisheng Ji, Xiang Li, Quanzheng Li, Lichao Sun\n- **Venue:** arXiv:2602.10367 (Feb 2026)\n- **URL:** [https://arxiv.org/abs/2602.10367](https://arxiv.org/abs/2602.10367)\n- **Summary:** Weekly-updated medical benchmark with 2,756 cases across 38 specialties; multi-agent clinical validation; best model achieves only 39.2%; 84% of models degrade on newer cases.\n- **Why important:** Domain-specific contamination-free benchmark; demonstrates temporal degradation pattern consistent with contamination in medical LLM evaluations.\n\n**18. When Benchmarks Leak: Inference-Time Decontamination for LLMs (DeconIEP)**\n- **Authors:** Jianzhe Chai, Yu Zhe, Jun Sakuma\n- **Venue:** arXiv:2601.19334 (Jan 2026)\n- **URL:** [https://arxiv.org/abs/2601.19334](https://arxiv.org/abs/2601.19334)\n- **Summary:** Applies small bounded perturbations in the input embedding space at inference time, guided by a less-contaminated reference model, to redirect models away from memorization-driven shortcuts.\n- **Why important:** Novel inference-time mitigation approach that does not alter the evaluation set or require retraining; directly addresses the robustness-contamination interface.\n\n---\n\n### CATEGORY 6: SURVEYS\n\n**19. Benchmark Data Contamination of Large Language Models: A Survey**\n- **Authors:** Cheng Xu, Shuhao Guan, Derek Greene, M-Tahar Kechadi\n- **Venue:** arXiv:2406.04244 (June 2024)\n- **URL:** [https://arxiv.org/abs/2406.04244](https://arxiv.org/abs/2406.04244)\n- **Summary:** Comprehensive survey covering contamination taxonomy, detection methods, and alternative evaluation approaches for LLMs including GPT-4, Claude-3, and Gemini.\n- **Why important:** Foundational survey paper; establishes taxonomy and terminology for the field.\n\n**20. Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation**\n- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray\n- **Venue:** EMNLP 2025 (Main Conference)\n- **URL:** [https://aclanthology.org/2025.emnlp-main.511/](https://aclanthology.org/2025.emnlp-main.511/)\n- **Summary:** Charts the evolution from static to dynamic benchmarking paradigms; analyzes limitations of static enhancements (data encryption, post-hoc detection); proposes design principles for dynamic benchmarks.\n- **Why important:** Top-venue survey at EMNLP 2025; provides the static-to-dynamic evaluation framework with maintained GitHub repository.\n\n**21. A Survey on Data Contamination for Large Language Models**\n- **Authors:** Yuxing Cheng, Yi Chang, Yuan Wu\n- **Venue:** arXiv:2502.14425 (Feb 2025)\n- **URL:** [https://arxiv.org/abs/2502.14425](https://arxiv.org/abs/2502.14425)\n- **Summary:** Covers contamination-free evaluation strategies (data updating, rewriting, prevention), dynamic evaluation (rule-based, agent-based), and detection techniques (white-box, gray-box, black-box).\n- **Why important:** Most recent comprehensive survey; provides clean taxonomy of detection methods by information access requirements.\n\n**22. LLM Benchmark Datasets Should Be Contamination-Resistant**\n- **Authors:** Ali Al-Lawati, Jason Lucas, Dongwon Lee, Suhang Wang\n- **Venue:** arXiv:2605.19999 (May 2026)\n- **URL:** [https://arxiv.org/abs/2605.19999](https://arxiv.org/abs/2605.19999)\n- **Summary:** Proposes leveraging asymmetries in Transformer inference vs. training processes to build inherently contamination-resistant benchmarks; calls for community adoption of contamination-resistant evaluation pipelines.\n- **Why important:** Most recent position/methodology paper (May 2026); proposes architectural-level solutions rather than data-level workarounds.\n\n---\n\n### SUMMARY OF MOST CRITICAL PAPERS FOR THE AAAI 2026 PAPER\n\nFor a paper on **jointly modeling benchmark contamination and robustness in LLM evaluation**, the highest-priority papers are:\n\n1. **DCR (Paper #9)** -- directly provides contamination-adjusted scores, the closest existing work to joint contamination-robustness modeling\n2. **Wang et al. Fragility (Paper #11)** -- shows contamination detection breaks for reasoning models, motivating the need for joint approaches\n3. **CoDeC (Paper #1)** -- state-of-the-art detection method, accepted at ICLR 2026\n4. **Dong et al. CDD/TED (Paper #5)** -- jointly detects and mitigates contamination via output distribution\n5. **Bordt et al. Forgetting (Paper #13)** -- provides scaling-law perspective on when contamination matters\n6. **DeconIEP (Paper #18)** -- inference-time decontamination connecting robustness and contamination\n7. **BeyondBench (Paper #16)** -- contamination-impossible evaluation for reasoning\n8. **Chen et al. Static-to-Dynamic Survey (Paper #20)** -- EMNLP 2025 survey providing field context\n\nSources:\n- [CoDeC - arXiv:2510.27055](https://arxiv.org/abs/2510.27055)\n- [PaCoST - arXiv:2406.18326](https://arxiv.org/abs/2406.18326)\n- [Watermarking Detection - arXiv:2502.17259](https://arxiv.org/abs/2502.17259)\n- [Perplexity Contamination - arXiv:2309.10677](https://arxiv.org/abs/2309.10677)\n- [CDD/TED - arXiv:2402.15938](https://arxiv.org/abs/2402.15938)\n- [Testset Slot Guessing - arXiv:2311.09783](https://arxiv.org/abs/2311.09783)\n- [Simulating Leakage - arXiv:2505.24263](https://arxiv.org/abs/2505.24263)\n- [Rephrased Samples - arXiv:2311.04850](https://arxiv.org/abs/2311.04850)\n- [DCR - arXiv:2507.11405](https://arxiv.org/abs/2507.11405)\n- [Benchmark Without Answers - arXiv:2505.18102](https://arxiv.org/abs/2505.18102)\n- [Fragility in Reasoning Models - arXiv:2510.02386](https://arxiv.org/abs/2510.02386)\n- [Test of Time - arXiv:2509.00072](https://arxiv.org/abs/2509.00072)\n- [Forgetting Contamination - arXiv:2410.03249](https://arxiv.org/abs/2410.03249)\n- [LiveBench - arXiv:2406.19314](https://arxiv.org/abs/2406.19314)\n- [LiveCodeBench - arXiv:2403.07974](https://arxiv.org/abs/2403.07974)\n- [BeyondBench - arXiv:2509.24210](https://arxiv.org/abs/2509.24210)\n- [LiveMedBench - arXiv:2602.10367](https://arxiv.org/abs/2602.10367)\n- [DeconIEP - arXiv:2601.19334](https://arxiv.org/abs/2601.19334)\n- [Xu et al. Survey - arXiv:2406.04244](https://arxiv.org/abs/2406.04244)\n- [EMNLP 2025 Survey](https://aclanthology.org/2025.emnlp-main.511/)\n- [Cheng et al. Survey - arXiv:2502.14425](https://arxiv.org/abs/2502.14425)\n- [Contamination-Resistant Benchmarks - arXiv:2605.19999](https://arxiv.org/abs/2605.19999)\n- [LLM-Stats Guide](https://llm-stats.com/blog/research/what-is-a-contaminated-llm)"
      }
    ],
    "totalDurationMs": 193862,
    "totalTokens": 33715,
    "totalToolUseCount": 34,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1665,
      "cache_read_input_tokens": 26138,
      "output_tokens": 5911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1665
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5911,
          "cache_read_input_tokens": 26138,
          "cache_creation_input_tokens": 1665,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1665,
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
  "sourceToolAssistantUUID": "d326bb7e-bfa7-4f24-aeba-dc007b61a1e9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "f9d020a2-84cc-4764-a26b-f252cdd87ce8",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Tool result

_source line 23 · 2026-05-29T05:20:02.045Z_

<details><summary>↩ Tool result · `toolu_01NpRVia5Mtc9Wze6UH8Tk6G`</summary>

```text
I now have a comprehensive set of papers. Here is the structured literature survey:

---

## Literature Survey: Adversarial Robustness Evaluation of LLMs on Math Reasoning Benchmarks (2024--2026)

### TIER 1: Core Papers -- Adversarial/Perturbed Math Benchmark Generation

---

**1. MaSTer: Toward Automated Robustness Evaluation of Mathematical Reasoning**
- **Authors:** Yutao Hou, Zeguan Xiao, Fei Yu, Yihan Jiang, Ma Shuguang, Zhaoqian Dai, Hailiang Huang, Yun Chen, Guanhua Chen
- **Venue:** Findings of ACL 2026
- **URL:** https://arxiv.org/abs/2506.05038
- **Date:** June 2025 (revised April 2026)
- **Summary:** Automated stress-testing framework that generates adversarial math problem variants via a multi-round rewrite-verify loop; models lose 48% and 31% accuracy on GSM8K and MATH-500 variants respectively.
- **Why important:** Closest prior work to automated adversarial variant generation with semantic consistency verification. Directly relevant as a baseline method. Extends beyond math to MMLU, MMLU-Pro, CommonsenseQA.

---

**2. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models**
- **Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2410.05229
- **Date:** October 2024 (revised August 2025)
- **Summary:** Uses parameterized symbolic templates over GSM8K to generate controlled problem variants; changing numeric values causes noticeable variance, and adding irrelevant clauses degrades performance up to 65%.
- **Why important:** Seminal work demonstrating that LLMs replicate reasoning patterns from training data rather than performing genuine reasoning. Introduces the symbolic template methodology central to your paper's approach.

---

**3. GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers**
- **Authors:** Qintong Li, Leyang Cui, Xueliang Zhao, Lingpeng Kong, Wei Bi
- **Venue:** ACL 2024
- **URL:** https://arxiv.org/abs/2402.19255
- **Date:** February 2024 (revised July 2024)
- **Summary:** Extends GSM8K with 8 families of mathematical perturbations per problem; tests 25 LLMs across 4 prompting strategies and finds performance is far from robust on perturbed variants.
- **Why important:** Establishes the taxonomy of mathematical perturbation types (numerical variation, adding operations, reversing questions, etc.) that has become standard in the field.

---

**4. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations**
- **Authors:** Kaixuan Huang, Jiacheng Guo, Zihao Li, Xiang Ji, Jiawei Ge, Wenzhe Li, Yingqing Guo, Tianle Cai, Hui Yuan, Runzhe Wang, Yue Wu, Ming Yin, Shange Tang, Yangsibo Huang, Chi Jin, Xinyun Chen, Chiyuan Zhang, Mengdi Wang
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2502.06453
- **Date:** February 2025
- **Summary:** Creates MATH-P-Simple and MATH-P-Hard benchmarks (279 problems from MATH level-5); "hard" perturbations fundamentally change the problem nature so original solution steps do not apply, revealing memorization-driven reasoning.
- **Why important:** Distinguishes between surface-level and deep structural perturbations, directly addressing whether LLMs truly reason or memorize solution templates.

---

**5. GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations**
- **Authors:** Jyotika Singh, Fang Tu, Aziza Mirsaidova, Amit Agarwal, Hitesh Laxmichand Patel, Sandip Ghoshal, Miguel Ballesteros, Karan Dua, Yassine Benajiba, Weiyi Sun, Tao Sheng, Graham Horwood, Sujith Ravi, Dan Roth
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2605.07053
- **Date:** May 2026
- **Summary:** Generates semantically diverse GSM8K variants by perturbing entities, attributes, and relationships; coupling semantic perturbations with symbolic/numerical variations yields an average 28% accuracy drop across 14 LLMs.
- **Why important:** Very recent work combining semantic and symbolic perturbation axes, producing fresh variants on each run to combat memorization.

---

**6. Putnam-AXIOM: A Functional and Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs**
- **Authors:** Aryan Gulati, Brando Miranda, Eric Chen, Emily Xia, Kai Fronsdal, Bruno Dumont, Elyas Obbad, Sanmi Koyejo
- **Venue:** ICML 2025
- **URL:** https://arxiv.org/abs/2508.08292
- **Date:** August 2025
- **Summary:** 522 Putnam competition problems plus 100 programmatically generated functional variants; o1-preview drops 19.6% on variants, indicating memorization.
- **Why important:** Demonstrates the functional-variant methodology at competition level (university-level math), directly showing the contamination-robustness gap.

---

**7. PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning**
- **Authors:** Yuren Hao, Xiang Wan, ChengXiang Zhai
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2508.08833
- **Date:** August 2025 (revised December 2025)
- **Summary:** Evaluates 18 LLMs on mathematically-equivalent transformations of advanced problems; O3 drops 4.7pp on surface-renaming and 12.9pp on parametric variants from a 51.5% baseline.
- **Why important:** Introduces the "Generalization-and-Perturbation" (GAP) strategy that explicitly addresses both data leakage and robustness simultaneously.

---

**8. RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning**
- **Authors:** Xinyuan Li, Murong Xu, Wenbiao Tao, Hanlun Zhu, Yike Zhao, Jipeng Zhang, Yunshi Lan
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2511.04120
- **Date:** November 2025 (revised January 2026)
- **Summary:** Uses Item Response Theory calibrated on 35 LLMs to guide RL-based question rewriting; perturbed AIME/AMC questions cause average 21.73% performance decline across 26 models.
- **Why important:** Unique approach combining psychometric theory (IRT) with adversarial perturbation for principled difficulty control of generated variants.

---

**9. ASyMOB: Algebraic Symbolic Mathematical Operations Benchmark**
- **Authors:** Michael Shalyt, Rotem Elimelech, Ido Kaminer
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2505.23851
- **Date:** May 2025
- **Summary:** 17,092 symbolic math challenges with systematic perturbations; LLMs degrade up to 70.3% on perturbed problems; compares LLMs to computer algebra systems (SymPy), finding complementary strengths.
- **Why important:** Directly relevant to symbolic perturbation methodology. Demonstrates the gap between unperturbed (74.6% avg) and perturbed (46.8% avg) performance, and examines SymPy integration.

---

**10. Adversarial Math Word Problem Generation**
- **Authors:** Roy Xie, Chengxuan Huang, Junlin Wang, Bhuwan Dhingra
- **Venue:** Findings of EMNLP 2024
- **URL:** https://arxiv.org/abs/2402.17916
- **Date:** February 2024 (revised June 2024)
- **Summary:** Uses abstract syntax trees to generate adversarial math word problems through numeric value modifications; identifies common model vulnerabilities and proposes cost-effective attack transfer methods.
- **Why important:** Introduces AST-based symbolic manipulation for adversarial generation, a precursor to more sophisticated symbolic approaches.

---

**11. MathAttack: Attacking Large Language Models Towards Math Solving Ability**
- **Authors:** Zihao Zhou, Qiufeng Wang, Mingyu Jin, Jie Yao, Jianan Ye, Wei Liu, Wei Wang, Xiaowei Huang, Kaizhu Huang
- **Venue:** AAAI 2024
- **URL:** https://arxiv.org/abs/2309.01686
- **Date:** September 2023
- **Summary:** Proposes word-level adversarial attacks on math word problems that preserve mathematical logic via logical entity recognition; introduces the RobustMath dataset.
- **Why important:** First AAAI paper specifically on adversarial attacks against LLM math reasoning. Establishes that adversarial samples transfer across models.

---

### TIER 2: Robustness Evaluation & Perturbation Sensitivity

---

**12. Robust Reasoning Benchmark (RRB)**
- **Authors:** Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2604.08571
- **Date:** March 2026 (revised May 2026)
- **Summary:** Applies 13 deterministic textual perturbations to AIME 2024/2025; open-source reasoning models show accuracy drops up to 54% average and 100% in specific cases; identifies "Intra-Query Attention Dilution."
- **Why important:** Comprehensive perturbation taxonomy on competition-level problems; novel attention-dilution finding relevant to understanding why perturbations degrade reasoning.

---

**13. Fragile Thoughts: How Large Language Models Handle Chain-of-Thought Perturbations**
- **Authors:** Ashwath Vaithinathan Aravindan, Mayank Kejriwal
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2603.03332
- **Date:** February 2026 (revised April 2026)
- **Summary:** Tests 13 models across 5 CoT perturbation types (MathError, UnitConversion, Sycophancy, SkippedSteps, ExtraSteps); smaller models lose 50-60% accuracy on math errors.
- **Why important:** Addresses robustness of the reasoning chain itself, not just the problem statement -- a complementary angle to input perturbation.

---

**14. Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models**
- **Authors:** Zhishen Sun, Guang Dai, Ivor Tsang, Haishan Ye
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2511.08022
- **Date:** November 2025
- **Summary:** Studies LLM sensitivity to numerical distractors; performance drops 10-50%; models maintain 20-40% accuracy even when core instructions are removed, suggesting pattern matching over reasoning.
- **Why important:** Provides evidence that models use "memory templates" rather than genuine reasoning, supporting the contamination hypothesis.

---

**15. ArithmAttack: Evaluating Robustness of LLMs to Noisy Context in Math Problem Solving**
- **Authors:** Zain Ul Abedin, Shahzeb Qamar, Lucie Flek, Akbar Karimi
- **Venue:** LLMSEC Workshop at ACL 2025
- **URL:** https://arxiv.org/abs/2501.08203
- **Date:** January 2025
- **Summary:** Evaluates robustness to punctuation noise injection on GSM8K and MultiArith across 8 models; all models are vulnerable, with performance degrading monotonically with noise level.
- **Why important:** Demonstrates that even trivial surface-level perturbations (punctuation noise) break math reasoning, complementing deeper structural perturbation studies.

---

**16. Exploring LLM Reasoning Through Controlled Prompt Variations**
- **Authors:** Giannis Chatziveroglou, Richard Yun, Maura Kelleher
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2504.02111
- **Date:** April 2025
- **Summary:** Tests 13 models on GSM8K with 4 types of prompt disruptions (irrelevant context, bad instructions, unnecessary facts, combinations); degradation is insensitive to task complexity.
- **Why important:** Shows that extraneous information universally degrades performance, and some perturbations unexpectedly trigger chain-of-thought behavior.

---

**17. More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists**
- **Authors:** Khashayar Alavi, Zhastay Yeltay, Lucie Flek, Akbar Karimi
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2511.07112
- **Date:** November 2025 (revised March 2026)
- **Summary:** Scaling from 1 to 10 collaborative agents improves accuracy but the adversarial robustness gap persists regardless of agent count.
- **Why important:** Shows that multi-agent approaches do not solve the fundamental robustness problem, ruling out a potential mitigation strategy.

---

**18. Evaluating LLMs' Mathematical and Coding Competency through Ontology-guided Interventions**
- **Authors:** Pengfei Hong, Navonil Majumder, Deepanway Ghosal, Somak Aditya, Rada Mihalcea, Soujanya Poria
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2401.09395
- **Date:** January 2024 (revised November 2024)
- **Summary:** Introduces an ontology of perturbations for math and code; creates GSMORE (math) and HUMANEVAL-CORE (code) benchmarks; significant performance drops across all tested LLMs.
- **Why important:** Provides a principled perturbation ontology that can systematically guide variant generation.

---

### TIER 3: Contamination-Focused / Dynamic Evaluation

---

**19. MathArena: Evaluating LLMs on Uncontaminated Math Competitions**
- **Authors:** Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2505.23281
- **Date:** May 2025 (revised January 2026)
- **Summary:** Evaluates 50+ models on freshly released competition problems immediately after publication; detects strong contamination signs in AIME 2024 (10-20 point score inflation).
- **Why important:** Establishes ground truth for contamination in math benchmarks, providing the "contamination baseline" that robustness studies aim to control for.

---

**20. DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks**
- **Authors:** Kaijie Zhu, Jiaao Chen, Jindong Wang, Neil Zhenqiang Gong, Diyi Yang, Xing Xie
- **Venue:** ICLR 2024 (Spotlight)
- **URL:** https://arxiv.org/abs/2309.17167
- **Date:** September 2023 (revised March 2024)
- **Summary:** Uses directed acyclic graphs to dynamically generate evaluation samples with controllable complexity for math, logic, and algorithm tasks; exposes suspected contamination in phi-1.5, WizardMath, Xwin models.
- **Why important:** Foundational work on dynamic benchmark generation to combat contamination; DAG-based generation is a precursor to symbolic template approaches.

---

**21. Provable Joint Decontamination for Benchmarking Multiple Large Language Models**
- **Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2605.21543
- **Date:** May 2026
- **Summary:** Proposes JECS (Joint Envelope Conformal Selection) for provable global contamination rate control across multiple LLMs simultaneously using conformal p-values and adaptive BH procedure.
- **Why important:** Directly addresses the joint contamination-robustness modeling problem -- provides statistical framework for decontaminating benchmark results across multiple models.

---

**22. Test of Time: Rethinking Temporal Signal of Benchmark Contamination**
- **Authors:** Terry Jingchen Zhang, Gopal Dev, Ning Wang, Max Obreiter, Punya Syon Pandey, Keenan Samway, Wenyuan Jiang, Yinya Huang, Bernhard Scholkopf, Mrinmaya Sachan, Zhijing Jin
- **Venue:** ACL 2026
- **URL:** https://arxiv.org/abs/2509.00072
- **Date:** August 2025 (revised May 2026)
- **Summary:** Shows that post-cutoff performance decay (a widely used contamination signal) disappears when problems are reformulated via LLM-driven transformations; uses influence functions to explain why.
- **Why important:** Critically challenges standard contamination detection methodology, showing that problem reformulation (perturbation) can serve as both a robustness test AND a contamination probe.

---

**23. LLM Benchmark Datasets Should Be Contamination-Resistant**
- **Authors:** Ali Al-Lawati, Jason Lucas, Dongwon Lee, Suhang Wang
- **Venue:** ICML 2026 Position Paper Track
- **URL:** https://arxiv.org/abs/2605.19999
- **Date:** May 2026
- **Summary:** Position paper arguing benchmarks should be "contamination-resistant" (unlearnable during training yet functional at inference); establishes mathematical framework for cross-architecture compatibility.
- **Why important:** Provides the theoretical framing for why adversarial variant generation is needed as a systematic defense against contamination.

---

**24. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**
- **Authors:** Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, Siddhartha Jain, Ravid Shwartz-Ziv, Neel Jain, Khalid Saifullah, et al.
- **Venue:** ICLR 2025 (Spotlight)
- **URL:** https://arxiv.org/abs/2406.19314
- **Date:** June 2024 (revised April 2025)
- **Summary:** Frequently-updated benchmark with automatic scoring across math, coding, reasoning, and data analysis; top models achieve below 70% accuracy; refreshed monthly.
- **Why important:** Establishes the "living benchmark" paradigm that complements static adversarial variant generation approaches.

---

**25. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation**
- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray
- **Venue:** Preprint (arXiv)
- **URL:** https://arxiv.org/abs/2502.17521
- **Date:** February 2025 (revised September 2025)
- **Summary:** Survey paper analyzing the shift from static to dynamic benchmarking; proposes design principles for dynamic benchmarks and identifies the absence of standardized evaluation criteria.
- **Why important:** Comprehensive survey paper that contextualizes all the above work; useful for the Related Work section of your AAAI paper.

---

### Summary Statistics

- **Total papers found:** 25
- **Published at top venues:** ACL 2024/2026 (3), ICLR 2024/2025 (3), ICML 2025/2026 (2), AAAI 2024 (1)
- **Time range:** September 2023 -- May 2026 (bulk from 2025--2026)
- **Key themes covered:**
  - Symbolic template-based variant generation: GSM-Symbolic, ASyMOB, Adversarial Math Word Problem Generation
  - Perturbation taxonomy: GSM-Plus, GSMORE, RRB, MATH-Perturb
  - Automated adversarial generation: MaSTer, RIDE
  - Contamination detection/mitigation: MathArena, DyVal, JECS, Test of Time, LiveBench
  - Joint contamination + robustness: Putnam-AXIOM, PutnamGAP, LLM Benchmark Datasets Should Be Contamination-Resistant

The most directly relevant papers for your AAAI 2026 paper on "jointly modeling benchmark contamination and robustness" are: MaSTer (#1), GSM-Symbolic (#2), MATH-Perturb (#4), Putnam-AXIOM (#6), PutnamGAP (#7), Test of Time (#22), JECS (#21), and the contamination-resistance position paper (#23). These collectively define the space your paper operates in.

agentId: aa392d2f0cf04f8c0 (use SendMessage with to: 'aa392d2f0cf04f8c0' to continue this agent)
&lt;usage>total_tokens: 38377
tool_uses: 40
duration_ms: 230476&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84ec0b59-f5ae-4f90-9d03-2f501bddc656",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "cc93fb61-5567-4b95-a20b-010b2a8e1abb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on jointly modeling benchmark contamination and robustness in LLM evaluation.\n\nSearch for the most important recent papers (2024-2026) on adversarial robustness evaluation of LLMs, particularly for math reasoning benchmarks. Execute these searches:\n\n1. WebSearch: \"adversarial math benchmark LLM robustness evaluation 2025 2026\"\n2. WebSearch: \"MaSTer automated adversarial math variant generation 2026\"\n3. WebSearch: \"GSM-Symbolic GSM-Plus MATH-Perturb adversarial benchmark variants 2025\"\n4. WebSearch: \"LLM reasoning robustness perturbation functional variants 2025 2026\"\n5. WebSearch: \"symbolic perturbation math problems LLM evaluation SymPy 2025\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on papers that:\n- Generate adversarial or perturbed variants of math/reasoning benchmarks\n- Evaluate LLM robustness to problem reformulations\n- Use symbolic methods for provably correct variant generation\n- Study the gap between performance on original vs. perturbed problems\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details.",
    "agentId": "aa392d2f0cf04f8c0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive set of papers. Here is the structured literature survey:\n\n---\n\n## Literature Survey: Adversarial Robustness Evaluation of LLMs on Math Reasoning Benchmarks (2024--2026)\n\n### TIER 1: Core Papers -- Adversarial/Perturbed Math Benchmark Generation\n\n---\n\n**1. MaSTer: Toward Automated Robustness Evaluation of Mathematical Reasoning**\n- **Authors:** Yutao Hou, Zeguan Xiao, Fei Yu, Yihan Jiang, Ma Shuguang, Zhaoqian Dai, Hailiang Huang, Yun Chen, Guanhua Chen\n- **Venue:** Findings of ACL 2026\n- **URL:** https://arxiv.org/abs/2506.05038\n- **Date:** June 2025 (revised April 2026)\n- **Summary:** Automated stress-testing framework that generates adversarial math problem variants via a multi-round rewrite-verify loop; models lose 48% and 31% accuracy on GSM8K and MATH-500 variants respectively.\n- **Why important:** Closest prior work to automated adversarial variant generation with semantic consistency verification. Directly relevant as a baseline method. Extends beyond math to MMLU, MMLU-Pro, CommonsenseQA.\n\n---\n\n**2. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models**\n- **Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar\n- **Venue:** ICLR 2025\n- **URL:** https://arxiv.org/abs/2410.05229\n- **Date:** October 2024 (revised August 2025)\n- **Summary:** Uses parameterized symbolic templates over GSM8K to generate controlled problem variants; changing numeric values causes noticeable variance, and adding irrelevant clauses degrades performance up to 65%.\n- **Why important:** Seminal work demonstrating that LLMs replicate reasoning patterns from training data rather than performing genuine reasoning. Introduces the symbolic template methodology central to your paper's approach.\n\n---\n\n**3. GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers**\n- **Authors:** Qintong Li, Leyang Cui, Xueliang Zhao, Lingpeng Kong, Wei Bi\n- **Venue:** ACL 2024\n- **URL:** https://arxiv.org/abs/2402.19255\n- **Date:** February 2024 (revised July 2024)\n- **Summary:** Extends GSM8K with 8 families of mathematical perturbations per problem; tests 25 LLMs across 4 prompting strategies and finds performance is far from robust on perturbed variants.\n- **Why important:** Establishes the taxonomy of mathematical perturbation types (numerical variation, adding operations, reversing questions, etc.) that has become standard in the field.\n\n---\n\n**4. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations**\n- **Authors:** Kaixuan Huang, Jiacheng Guo, Zihao Li, Xiang Ji, Jiawei Ge, Wenzhe Li, Yingqing Guo, Tianle Cai, Hui Yuan, Runzhe Wang, Yue Wu, Ming Yin, Shange Tang, Yangsibo Huang, Chi Jin, Xinyun Chen, Chiyuan Zhang, Mengdi Wang\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2502.06453\n- **Date:** February 2025\n- **Summary:** Creates MATH-P-Simple and MATH-P-Hard benchmarks (279 problems from MATH level-5); \"hard\" perturbations fundamentally change the problem nature so original solution steps do not apply, revealing memorization-driven reasoning.\n- **Why important:** Distinguishes between surface-level and deep structural perturbations, directly addressing whether LLMs truly reason or memorize solution templates.\n\n---\n\n**5. GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations**\n- **Authors:** Jyotika Singh, Fang Tu, Aziza Mirsaidova, Amit Agarwal, Hitesh Laxmichand Patel, Sandip Ghoshal, Miguel Ballesteros, Karan Dua, Yassine Benajiba, Weiyi Sun, Tao Sheng, Graham Horwood, Sujith Ravi, Dan Roth\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2605.07053\n- **Date:** May 2026\n- **Summary:** Generates semantically diverse GSM8K variants by perturbing entities, attributes, and relationships; coupling semantic perturbations with symbolic/numerical variations yields an average 28% accuracy drop across 14 LLMs.\n- **Why important:** Very recent work combining semantic and symbolic perturbation axes, producing fresh variants on each run to combat memorization.\n\n---\n\n**6. Putnam-AXIOM: A Functional and Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs**\n- **Authors:** Aryan Gulati, Brando Miranda, Eric Chen, Emily Xia, Kai Fronsdal, Bruno Dumont, Elyas Obbad, Sanmi Koyejo\n- **Venue:** ICML 2025\n- **URL:** https://arxiv.org/abs/2508.08292\n- **Date:** August 2025\n- **Summary:** 522 Putnam competition problems plus 100 programmatically generated functional variants; o1-preview drops 19.6% on variants, indicating memorization.\n- **Why important:** Demonstrates the functional-variant methodology at competition level (university-level math), directly showing the contamination-robustness gap.\n\n---\n\n**7. PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning**\n- **Authors:** Yuren Hao, Xiang Wan, ChengXiang Zhai\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2508.08833\n- **Date:** August 2025 (revised December 2025)\n- **Summary:** Evaluates 18 LLMs on mathematically-equivalent transformations of advanced problems; O3 drops 4.7pp on surface-renaming and 12.9pp on parametric variants from a 51.5% baseline.\n- **Why important:** Introduces the \"Generalization-and-Perturbation\" (GAP) strategy that explicitly addresses both data leakage and robustness simultaneously.\n\n---\n\n**8. RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning**\n- **Authors:** Xinyuan Li, Murong Xu, Wenbiao Tao, Hanlun Zhu, Yike Zhao, Jipeng Zhang, Yunshi Lan\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2511.04120\n- **Date:** November 2025 (revised January 2026)\n- **Summary:** Uses Item Response Theory calibrated on 35 LLMs to guide RL-based question rewriting; perturbed AIME/AMC questions cause average 21.73% performance decline across 26 models.\n- **Why important:** Unique approach combining psychometric theory (IRT) with adversarial perturbation for principled difficulty control of generated variants.\n\n---\n\n**9. ASyMOB: Algebraic Symbolic Mathematical Operations Benchmark**\n- **Authors:** Michael Shalyt, Rotem Elimelech, Ido Kaminer\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2505.23851\n- **Date:** May 2025\n- **Summary:** 17,092 symbolic math challenges with systematic perturbations; LLMs degrade up to 70.3% on perturbed problems; compares LLMs to computer algebra systems (SymPy), finding complementary strengths.\n- **Why important:** Directly relevant to symbolic perturbation methodology. Demonstrates the gap between unperturbed (74.6% avg) and perturbed (46.8% avg) performance, and examines SymPy integration.\n\n---\n\n**10. Adversarial Math Word Problem Generation**\n- **Authors:** Roy Xie, Chengxuan Huang, Junlin Wang, Bhuwan Dhingra\n- **Venue:** Findings of EMNLP 2024\n- **URL:** https://arxiv.org/abs/2402.17916\n- **Date:** February 2024 (revised June 2024)\n- **Summary:** Uses abstract syntax trees to generate adversarial math word problems through numeric value modifications; identifies common model vulnerabilities and proposes cost-effective attack transfer methods.\n- **Why important:** Introduces AST-based symbolic manipulation for adversarial generation, a precursor to more sophisticated symbolic approaches.\n\n---\n\n**11. MathAttack: Attacking Large Language Models Towards Math Solving Ability**\n- **Authors:** Zihao Zhou, Qiufeng Wang, Mingyu Jin, Jie Yao, Jianan Ye, Wei Liu, Wei Wang, Xiaowei Huang, Kaizhu Huang\n- **Venue:** AAAI 2024\n- **URL:** https://arxiv.org/abs/2309.01686\n- **Date:** September 2023\n- **Summary:** Proposes word-level adversarial attacks on math word problems that preserve mathematical logic via logical entity recognition; introduces the RobustMath dataset.\n- **Why important:** First AAAI paper specifically on adversarial attacks against LLM math reasoning. Establishes that adversarial samples transfer across models.\n\n---\n\n### TIER 2: Robustness Evaluation & Perturbation Sensitivity\n\n---\n\n**12. Robust Reasoning Benchmark (RRB)**\n- **Authors:** Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2604.08571\n- **Date:** March 2026 (revised May 2026)\n- **Summary:** Applies 13 deterministic textual perturbations to AIME 2024/2025; open-source reasoning models show accuracy drops up to 54% average and 100% in specific cases; identifies \"Intra-Query Attention Dilution.\"\n- **Why important:** Comprehensive perturbation taxonomy on competition-level problems; novel attention-dilution finding relevant to understanding why perturbations degrade reasoning.\n\n---\n\n**13. Fragile Thoughts: How Large Language Models Handle Chain-of-Thought Perturbations**\n- **Authors:** Ashwath Vaithinathan Aravindan, Mayank Kejriwal\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2603.03332\n- **Date:** February 2026 (revised April 2026)\n- **Summary:** Tests 13 models across 5 CoT perturbation types (MathError, UnitConversion, Sycophancy, SkippedSteps, ExtraSteps); smaller models lose 50-60% accuracy on math errors.\n- **Why important:** Addresses robustness of the reasoning chain itself, not just the problem statement -- a complementary angle to input perturbation.\n\n---\n\n**14. Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models**\n- **Authors:** Zhishen Sun, Guang Dai, Ivor Tsang, Haishan Ye\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2511.08022\n- **Date:** November 2025\n- **Summary:** Studies LLM sensitivity to numerical distractors; performance drops 10-50%; models maintain 20-40% accuracy even when core instructions are removed, suggesting pattern matching over reasoning.\n- **Why important:** Provides evidence that models use \"memory templates\" rather than genuine reasoning, supporting the contamination hypothesis.\n\n---\n\n**15. ArithmAttack: Evaluating Robustness of LLMs to Noisy Context in Math Problem Solving**\n- **Authors:** Zain Ul Abedin, Shahzeb Qamar, Lucie Flek, Akbar Karimi\n- **Venue:** LLMSEC Workshop at ACL 2025\n- **URL:** https://arxiv.org/abs/2501.08203\n- **Date:** January 2025\n- **Summary:** Evaluates robustness to punctuation noise injection on GSM8K and MultiArith across 8 models; all models are vulnerable, with performance degrading monotonically with noise level.\n- **Why important:** Demonstrates that even trivial surface-level perturbations (punctuation noise) break math reasoning, complementing deeper structural perturbation studies.\n\n---\n\n**16. Exploring LLM Reasoning Through Controlled Prompt Variations**\n- **Authors:** Giannis Chatziveroglou, Richard Yun, Maura Kelleher\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2504.02111\n- **Date:** April 2025\n- **Summary:** Tests 13 models on GSM8K with 4 types of prompt disruptions (irrelevant context, bad instructions, unnecessary facts, combinations); degradation is insensitive to task complexity.\n- **Why important:** Shows that extraneous information universally degrades performance, and some perturbations unexpectedly trigger chain-of-thought behavior.\n\n---\n\n**17. More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists**\n- **Authors:** Khashayar Alavi, Zhastay Yeltay, Lucie Flek, Akbar Karimi\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2511.07112\n- **Date:** November 2025 (revised March 2026)\n- **Summary:** Scaling from 1 to 10 collaborative agents improves accuracy but the adversarial robustness gap persists regardless of agent count.\n- **Why important:** Shows that multi-agent approaches do not solve the fundamental robustness problem, ruling out a potential mitigation strategy.\n\n---\n\n**18. Evaluating LLMs' Mathematical and Coding Competency through Ontology-guided Interventions**\n- **Authors:** Pengfei Hong, Navonil Majumder, Deepanway Ghosal, Somak Aditya, Rada Mihalcea, Soujanya Poria\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2401.09395\n- **Date:** January 2024 (revised November 2024)\n- **Summary:** Introduces an ontology of perturbations for math and code; creates GSMORE (math) and HUMANEVAL-CORE (code) benchmarks; significant performance drops across all tested LLMs.\n- **Why important:** Provides a principled perturbation ontology that can systematically guide variant generation.\n\n---\n\n### TIER 3: Contamination-Focused / Dynamic Evaluation\n\n---\n\n**19. MathArena: Evaluating LLMs on Uncontaminated Math Competitions**\n- **Authors:** Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2505.23281\n- **Date:** May 2025 (revised January 2026)\n- **Summary:** Evaluates 50+ models on freshly released competition problems immediately after publication; detects strong contamination signs in AIME 2024 (10-20 point score inflation).\n- **Why important:** Establishes ground truth for contamination in math benchmarks, providing the \"contamination baseline\" that robustness studies aim to control for.\n\n---\n\n**20. DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks**\n- **Authors:** Kaijie Zhu, Jiaao Chen, Jindong Wang, Neil Zhenqiang Gong, Diyi Yang, Xing Xie\n- **Venue:** ICLR 2024 (Spotlight)\n- **URL:** https://arxiv.org/abs/2309.17167\n- **Date:** September 2023 (revised March 2024)\n- **Summary:** Uses directed acyclic graphs to dynamically generate evaluation samples with controllable complexity for math, logic, and algorithm tasks; exposes suspected contamination in phi-1.5, WizardMath, Xwin models.\n- **Why important:** Foundational work on dynamic benchmark generation to combat contamination; DAG-based generation is a precursor to symbolic template approaches.\n\n---\n\n**21. Provable Joint Decontamination for Benchmarking Multiple Large Language Models**\n- **Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2605.21543\n- **Date:** May 2026\n- **Summary:** Proposes JECS (Joint Envelope Conformal Selection) for provable global contamination rate control across multiple LLMs simultaneously using conformal p-values and adaptive BH procedure.\n- **Why important:** Directly addresses the joint contamination-robustness modeling problem -- provides statistical framework for decontaminating benchmark results across multiple models.\n\n---\n\n**22. Test of Time: Rethinking Temporal Signal of Benchmark Contamination**\n- **Authors:** Terry Jingchen Zhang, Gopal Dev, Ning Wang, Max Obreiter, Punya Syon Pandey, Keenan Samway, Wenyuan Jiang, Yinya Huang, Bernhard Scholkopf, Mrinmaya Sachan, Zhijing Jin\n- **Venue:** ACL 2026\n- **URL:** https://arxiv.org/abs/2509.00072\n- **Date:** August 2025 (revised May 2026)\n- **Summary:** Shows that post-cutoff performance decay (a widely used contamination signal) disappears when problems are reformulated via LLM-driven transformations; uses influence functions to explain why.\n- **Why important:** Critically challenges standard contamination detection methodology, showing that problem reformulation (perturbation) can serve as both a robustness test AND a contamination probe.\n\n---\n\n**23. LLM Benchmark Datasets Should Be Contamination-Resistant**\n- **Authors:** Ali Al-Lawati, Jason Lucas, Dongwon Lee, Suhang Wang\n- **Venue:** ICML 2026 Position Paper Track\n- **URL:** https://arxiv.org/abs/2605.19999\n- **Date:** May 2026\n- **Summary:** Position paper arguing benchmarks should be \"contamination-resistant\" (unlearnable during training yet functional at inference); establishes mathematical framework for cross-architecture compatibility.\n- **Why important:** Provides the theoretical framing for why adversarial variant generation is needed as a systematic defense against contamination.\n\n---\n\n**24. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**\n- **Authors:** Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, Siddhartha Jain, Ravid Shwartz-Ziv, Neel Jain, Khalid Saifullah, et al.\n- **Venue:** ICLR 2025 (Spotlight)\n- **URL:** https://arxiv.org/abs/2406.19314\n- **Date:** June 2024 (revised April 2025)\n- **Summary:** Frequently-updated benchmark with automatic scoring across math, coding, reasoning, and data analysis; top models achieve below 70% accuracy; refreshed monthly.\n- **Why important:** Establishes the \"living benchmark\" paradigm that complements static adversarial variant generation approaches.\n\n---\n\n**25. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation**\n- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray\n- **Venue:** Preprint (arXiv)\n- **URL:** https://arxiv.org/abs/2502.17521\n- **Date:** February 2025 (revised September 2025)\n- **Summary:** Survey paper analyzing the shift from static to dynamic benchmarking; proposes design principles for dynamic benchmarks and identifies the absence of standardized evaluation criteria.\n- **Why important:** Comprehensive survey paper that contextualizes all the above work; useful for the Related Work section of your AAAI paper.\n\n---\n\n### Summary Statistics\n\n- **Total papers found:** 25\n- **Published at top venues:** ACL 2024/2026 (3), ICLR 2024/2025 (3), ICML 2025/2026 (2), AAAI 2024 (1)\n- **Time range:** September 2023 -- May 2026 (bulk from 2025--2026)\n- **Key themes covered:**\n  - Symbolic template-based variant generation: GSM-Symbolic, ASyMOB, Adversarial Math Word Problem Generation\n  - Perturbation taxonomy: GSM-Plus, GSMORE, RRB, MATH-Perturb\n  - Automated adversarial generation: MaSTer, RIDE\n  - Contamination detection/mitigation: MathArena, DyVal, JECS, Test of Time, LiveBench\n  - Joint contamination + robustness: Putnam-AXIOM, PutnamGAP, LLM Benchmark Datasets Should Be Contamination-Resistant\n\nThe most directly relevant papers for your AAAI 2026 paper on \"jointly modeling benchmark contamination and robustness\" are: MaSTer (#1), GSM-Symbolic (#2), MATH-Perturb (#4), Putnam-AXIOM (#6), PutnamGAP (#7), Test of Time (#22), JECS (#21), and the contamination-resistance position paper (#23). These collectively define the space your paper operates in."
      }
    ],
    "totalDurationMs": 230476,
    "totalTokens": 38377,
    "totalToolUseCount": 40,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1982,
      "cache_read_input_tokens": 30797,
      "output_tokens": 5597,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1982
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5597,
          "cache_read_input_tokens": 30797,
          "cache_creation_input_tokens": 1982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1982,
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
  "sourceToolAssistantUUID": "84ec0b59-f5ae-4f90-9d03-2f501bddc656",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "cc93fb61-5567-4b95-a20b-010b2a8e1abb",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Tool result

_source line 26 · 2026-05-29T05:20:06.117Z_

<details><summary>↩ Tool result · `toolu_01M7oV3yXySs1UhHpDtawjaM`</summary>

```text
Now I have comprehensive coverage. Here is the structured list of all papers found:

---

## Literature Survey: Item Response Theory Applied to LLM Evaluation (2024--2026)

### Paper 1: ATLAS -- Adaptive Testing for LLM Evaluation
- **Title:** Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks
- **Authors:** Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla
- **Date:** October 2025 (v1); February 2026 (v2)
- **Venue:** arXiv preprint (under review at ICML 2026 per OpenReview)
- **URL:** https://arxiv.org/abs/2511.04689
- **Summary:** Introduces ATLAS, a computerized adaptive testing framework using 3PL IRT with Fisher information-guided item selection that reduces required test items by up to 90% (e.g., 41 items instead of 5,600 on HellaSwag) while maintaining measurement precision.
- **Why important:** The most direct application of psychometric adaptive testing to LLM benchmarking. Demonstrates that IRT-based CAT can produce finer-grained ability estimates than raw accuracy, with 23--31% of 3,000+ models shifting significantly in rank. Directly relevant to the paper's goal of efficient, calibrated ability estimation.

---

### Paper 2: PSN-IRT -- Lost in Benchmarks?
- **Title:** Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory
- **Authors:** Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao
- **Date:** May 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2505.15055
- **Summary:** Proposes Pseudo-Siamese Network for IRT (PSN-IRT) that models four item parameters (discriminability, difficulty, guessing-rate, feasibility) and analyzes 11 benchmarks with 41,871 items, revealing significant shortcomings in measurement quality.
- **Why important:** Core related work for jointly modeling item parameters and model ability. Demonstrates that IRT-selected item subsets produce rankings better aligned with human preferences, directly supporting the thesis that current benchmarks are psychometrically flawed.

---

### Paper 3: IrtNet -- Compact Representations of LLM Abilities
- **Title:** Learning Compact Representations of LLM Abilities via Item Response Theory
- **Authors:** Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu
- **Date:** October 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2510.00844
- **Summary:** Proposes IrtNet, an IRT-based framework using Mixture-of-Experts networks to learn compact multidimensional ability vectors for LLMs alongside query discrimination vectors and difficulty parameters, enabling model routing and performance forecasting.
- **Why important:** Extends IRT from scalar ability to multidimensional latent representations. Shows how IRT parameters can be learned jointly via neural networks, bridging classical psychometrics with deep learning -- a methodological precedent for neural IRT in LLM evaluation.

---

### Paper 4: JE-IRT -- Joint Embedding Item Response Theory
- **Title:** JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory
- **Authors:** Louie Hong Yao, Nicholas Jarvis, Tiffany Zhan, Saptarshi Ghosh, Linfeng Liu, Tianyu Jiang
- **Date:** September 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2509.22888
- **Summary:** Places LLMs and test items in a shared geometric embedding space where question direction encodes semantics, magnitude encodes difficulty, and model-question alignment determines performance. Reveals an internal LLM taxonomy that diverges from conventional subject classifications.
- **Why important:** Novel geometric/embedding-based extension of IRT that provides interpretable visualizations of model abilities. The geometric framework could complement contamination detection by revealing anomalous ability patterns.

---

### Paper 5: IRT-Router
- **Title:** IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory
- **Authors:** Wei Song, Zhenya Huang, Cheng Cheng, Weibo Gao, Bihan Xu, GuanHao Zhao, Fei Wang, Runze Wu
- **Date:** July 2025
- **Venue:** ACL 2025 (Long Papers), Vienna, Austria
- **URL:** https://aclanthology.org/2025.acl-long.761/
- **Summary:** Uses IRT to model LLM ability and query difficulty/discrimination for routing user queries to the most suitable model among 20 LLMs across 12 datasets, with strong cold-start performance.
- **Why important:** Demonstrates practical downstream use of IRT-estimated ability parameters. Published at a top venue (ACL 2025), validating the IRT-for-LLM-evaluation paradigm in the NLP community.

---

### Paper 6: LaRT -- Latency-Response Theory
- **Title:** Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length
- **Authors:** Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu
- **Date:** December 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2512.07019
- **Summary:** Extends IRT by jointly modeling response accuracy and chain-of-thought length, introducing latent ability, latent speed, and a correlation parameter between them. Finds strong negative correlation between ability and speed (more capable models produce longer reasoning chains).
- **Why important:** Extends classical IRT to incorporate process data (CoT length) alongside correctness, a novel psychometric direction. The joint modeling approach is conceptually parallel to jointly modeling contamination and robustness, offering methodological inspiration.

---

### Paper 7: Diagnosing LLM-as-a-Judge Reliability via IRT
- **Title:** Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory
- **Authors:** Junhyuk Choi, Sohhyung Park, Chanhee Cho, Hyeonchu Park, Bugeun Kim
- **Date:** January 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2602.00521
- **Summary:** Applies the Graded Response Model (GRM) from IRT to diagnose LLM judge reliability across two dimensions: intrinsic consistency (stability under prompt variations) and human alignment (correspondence with human assessments).
- **Why important:** Applies IRT not to evaluate LLM test-takers but LLM judges, broadening the psychometric framework to evaluation reliability. The GRM approach is relevant to modeling graded/partial responses in benchmark evaluation.

---

### Paper 8: IRT for Automatic Short Answer Grading
- **Title:** Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory
- **Authors:** Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, Ulf Kroehne
- **Date:** April 2026
- **Venue:** BEA 2026
- **URL:** https://arxiv.org/abs/2605.00238
- **Summary:** Models grading correctness as a function of latent grader ability and response difficulty using IRT. Analysis of 17 open-weight LLMs reveals that models with comparable aggregate performance differ substantially on difficult responses.
- **Why important:** Demonstrates IRT's ability to reveal performance differences invisible to aggregate metrics, supporting the argument that IRT-based evaluation is more informative than simple accuracy.

---

### Paper 9: LEGO-IRT -- Unified Framework for Data-Efficient Evaluation
- **Title:** Toward a unified framework for data-efficient evaluation of large language models
- **Authors:** Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang
- **Date:** October 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2510.04051
- **Summary:** Proposes LEGO-IRT, a multidimensional IRT framework that handles both discrete and continuous scoring metrics, decomposes ability into general and context-specific components, and achieves stable estimates with only 3% of evaluation items across 70 LLMs and 5 benchmarks.
- **Why important:** Addresses a key limitation of prior IRT-for-LLM work (restriction to binary correctness). The ability decomposition and structural modeling across benchmarks is directly relevant to jointly modeling multiple evaluation dimensions.

---

### Paper 10: tinyBenchmarks
- **Title:** tinyBenchmarks: evaluating LLMs with fewer examples
- **Authors:** Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin
- **Date:** February 2024
- **Venue:** ICML 2024 (Proceedings of the 41st International Conference on Machine Learning)
- **URL:** https://arxiv.org/abs/2402.14992
- **Summary:** Demonstrates that 100 IRT-curated examples suffice to estimate LLM performance on MMLU (14K items), achieving ~2% estimation error. Introduces the gp-IRT estimator combining direct sampling with IRT predictions, reducing evaluation cost by 140x.
- **Why important:** Foundational work establishing IRT-based benchmark reduction for LLMs at a top venue (ICML). The gp-IRT estimator and item selection strategies set the baseline that subsequent work (ATLAS, PSN-IRT, LEGO-IRT) builds upon.

---

### Paper 11: metabench
- **Title:** metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models
- **Authors:** Alex Kipnis, Konstantinos Voudouris, Luca M. Schulze Buschoff, Eric Schulz
- **Date:** July 2024 (v1); February 2025 (v2)
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2407.12844
- **Summary:** Uses IRT to distill six major LLM benchmarks (28,632 items) into 858 items (<3%) while reconstructing scores with 1.24% RMSE. Reveals a single latent factor capturing 79.3% of cross-benchmark variability (Spearman r=0.94 with total score).
- **Why important:** Published at ICLR 2025, demonstrating IRT-based benchmark compression at scale. The finding that a single factor dominates has implications for understanding what LLM benchmarks actually measure -- relevant to contamination analysis.

---

### Paper 12: Efficiently Measuring Cognitive Ability of LLMs
- **Title:** Efficiently Measuring the Cognitive Ability of LLMs: An Adaptive Testing Perspective
- **Authors:** Yan Zhuang, Qi Liu, Yuting Ning, Weizhe Huang, Rui Lv, Zhenya Huang, GuanHao Zhao, Zheng Zhang, Qingyang Mao, Shijin Wang, Enhong Chen
- **Date:** June 2023 (v1); published 2024
- **Venue:** ICLR 2024
- **URL:** https://ar5iv.labs.arxiv.org/html/2306.10512
- **Summary:** Pioneering work applying CAT to LLM evaluation across subject knowledge, math reasoning, and programming. Finds ChatGPT exhibits "careless student" behavior (high slip/guess rates) while GPT-4 reaches middle-level student ability.
- **Why important:** One of the earliest papers applying psychometric adaptive testing to LLMs, published at ICLR 2024. The "careless student" finding for ChatGPT is an early signal that IRT reveals qualitative behavioral patterns, not just scores.

---

### Paper 13: RIDE -- Adversarial Perturbation with IRT
- **Title:** RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning
- **Authors:** Xinyuan Li, Murong Xu, Wenbiao Tao, Hanlun Zhu, Yike Zhao, Jipeng Zhang, Yunshi Lan
- **Date:** November 2025
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2511.04120
- **Summary:** Combines IRT with RL-based adversarial question rewriting to generate difficulty-calibrated perturbations of math benchmarks. Uses 35 LLMs as simulated test-takers to build a difficulty ranker, causing an average 21.73% accuracy drop across 26 models.
- **Why important:** Directly bridges IRT and adversarial robustness evaluation -- the closest existing work to jointly modeling difficulty and robustness. The IRT-guided perturbation framework is a key methodological precedent for the proposed AAAI paper.

---

### Paper 14: Confident Rankings with Fewer Items (Continuous CAT)
- **Title:** Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores
- **Authors:** Esma Balkir, Alice Pernthaller, Marco Basaldella, Jose Hernandez-Orallo, Nigel Collier
- **Date:** January 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2601.13885
- **Summary:** Extends CAT from binary IRT to continuous scores using a heteroskedastic normal distribution, enabling adaptive testing with ROUGE, BLEU, and LLM-as-a-Judge metrics. Incorporates uncertainty-aware ranking with adaptive stopping.
- **Why important:** Generalizes IRT-based adaptive testing beyond multiple-choice to generation tasks, broadening the applicability of psychometric evaluation. The uncertainty-aware ranking methodology is relevant to producing calibrated ability estimates.

---

### Paper 15: CAT for Medical LLM Benchmarking
- **Title:** Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking
- **Authors:** Tianpeng Zheng, Zhehan Jiang, Jiayi Liu, Shicong Feng
- **Date:** February 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2603.23506
- **Summary:** Applies IRT-based CAT to medical LLM evaluation, achieving near-perfect correlation with full-bank estimates (r=0.988) using only 1.3% of items, reducing evaluation from hours to minutes per model across 38 models.
- **Why important:** Domain-specific validation of IRT-CAT for LLM evaluation in a high-stakes setting (medicine). The 1.3% item usage with r=0.988 is the strongest efficiency result reported, demonstrating the power of psychometric methods.

---

### Paper 16: Growing Pains -- Fixed Parameter Calibration
- **Title:** Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration
- **Authors:** Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky
- **Date:** April 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2604.12843
- **Summary:** Uses multidimensional IRT with anchor items to enable extensible benchmarking where new datasets are calibrated against fixed parameters, achieving score prediction within 2--3 percentage points and Spearman rho >= 0.9 across 400+ models.
- **Why important:** Addresses the practical challenge of benchmark extensibility -- new items and models can be added without re-evaluating everything. The anchor-item approach from educational testing is a mature psychometric technique newly applied to LLMs.

---

### Paper 17: Reliable and Efficient Amortized Model-Based Evaluation
- **Title:** Reliable and Efficient Amortized Model-based Evaluation
- **Authors:** Sang Truong, Yuheng Tu, Percy Liang, Bo Li, Sanmi Koyejo
- **Date:** March 2025
- **Venue:** arXiv preprint (Stanford CRFM)
- **URL:** https://arxiv.org/abs/2503.13335
- **Summary:** Trains a model to predict question difficulty from content alone using IRT, enabling reliable measurement at lower cost. Also develops a question generator that creates items at specified difficulty levels for adaptive testing. Validated across 22 benchmarks and 172 LLMs.
- **Why important:** From Stanford CRFM (HELM team), this work amortizes IRT calibration by predicting item parameters from question text, removing the need for large response matrices. The difficulty-controlled item generation capability is relevant to both contamination testing and adaptive evaluation.

---

### Paper 18: Scalable IRT via Matrix Factorization
- **Title:** An Interpretable and Scalable Framework for Evaluating Large Language Models
- **Authors:** Xinhao Qu, Qiang Heng, Hao Zeng, Xiaoqian Liu
- **Date:** May 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2605.07046
- **Summary:** Reformulates IRT parameter estimation as constrained matrix factorization using the majorization-minimization principle, achieving orders-of-magnitude speedups with theoretical guarantees for identifiability and convergence.
- **Why important:** Addresses scalability of IRT estimation for large LLM evaluation matrices (many models x many items), providing the computational infrastructure needed for practical deployment of IRT-based evaluation.

---

### Paper 19: Benchmark Health Index
- **Title:** Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs
- **Authors:** Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao
- **Date:** February 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2602.11674
- **Summary:** Proposes BHI, a data-driven framework evaluating benchmark quality across capability discrimination, anti-saturation, and impact dimensions, synthesizing 106 benchmarks from 91 models.
- **Why important:** While not strictly IRT-based, addresses benchmark quality assessment from a measurement perspective. The discrimination and saturation metrics are closely related to IRT item parameters, and the meta-evaluation approach complements IRT-based item analysis.

---

### Paper 20: M3IRT -- Multimodal Item Response Theory
- **Title:** Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory
- **Authors:** Shunki Uebayashi, Kento Masui, Kyohei Atarashi, Han Bao, Hisashi Kashima, Naoto Inoue, Mayu Otani, Koh Takeuchi
- **Date:** March 2026
- **Venue:** arXiv preprint
- **URL:** https://arxiv.org/abs/2603.02663
- **Summary:** Extends IRT to multimodal evaluation by decomposing model ability and question difficulty into image-only, text-only, and cross-modal components. Identifies shortcut questions and preserves ranking fidelity even when 50% of items are low-quality.
- **Why important:** Demonstrates IRT's extensibility to multimodal settings and shows robustness to low-quality items -- a property relevant to contamination-robust evaluation.

---

### Paper 21: LLM Psychometrics Survey
- **Title:** Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement
- **Authors:** Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, Guojie Song
- **Date:** May 2025 (v1); March 2026 (v3)
- **Venue:** arXiv preprint (survey)
- **URL:** https://arxiv.org/abs/2505.08245
- **Summary:** Comprehensive survey of "LLM Psychometrics" as an emerging field, synthesizing work on applying psychometric instruments, theories, and principles to evaluate, understand, and enhance LLMs. Covers benchmarking frameworks, validation methodologies, and enhancement techniques.
- **Why important:** The key survey paper positioning IRT-for-LLM-evaluation within the broader psychometrics landscape. Essential citation for framing the related work section and understanding the field's trajectory.

---

### Paper 22: Lifting the Benchmark Iceberg with IRT
- **Title:** Lifting the benchmark iceberg with item-response theory
- **Authors:** Mara Schilling-Wilhelmi, Nawaf Alampara, Kevin Maik Jablonka
- **Date:** 2025
- **Venue:** ICLR 2025 Workshop on AI4MAT
- **URL:** https://openreview.net/forum?id=ZyVQqK7mcP
- **Summary:** Investigates how hidden implementation choices in LLM benchmarks distort model rankings (the "benchmark iceberg" phenomenon) and proposes IRT as a transparency tool.
- **Why important:** Highlights a complementary angle -- IRT as a diagnostic tool for benchmark transparency rather than just efficiency. The "benchmark iceberg" framing connects to contamination concerns where hidden factors distort evaluation.

---

### Summary of Coverage by Theme

**Adaptive Testing / Efficient Evaluation:** Papers 1 (ATLAS), 10 (tinyBenchmarks), 11 (metabench), 12 (Cognitive Ability CAT), 14 (Continuous CAT), 15 (Medical CAT), 17 (Amortized Evaluation)

**IRT Model Extensions for LLMs:** Papers 2 (PSN-IRT), 3 (IrtNet), 4 (JE-IRT), 6 (LaRT), 9 (LEGO-IRT), 18 (Matrix Factorization IRT), 20 (M3IRT)

**IRT for Robustness/Adversarial Evaluation:** Paper 13 (RIDE) -- the most directly relevant to the proposed AAAI paper's joint contamination-robustness modeling

**Benchmark Quality / Meta-Evaluation:** Papers 11 (metabench), 19 (BHI), 22 (Benchmark Iceberg)

**Applied IRT for LLM Evaluation:** Papers 5 (IRT-Router), 7 (LLM-as-Judge), 8 (Short Answer Grading), 16 (Fixed Parameter Calibration)

**Survey:** Paper 21 (LLM Psychometrics)

agentId: ab1852e2a938e1f06 (use SendMessage with to: 'ab1852e2a938e1f06' to continue this agent)
&lt;usage>total_tokens: 36692
tool_uses: 38
duration_ms: 230293&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00b42f36-9d14-456b-ae3a-b6219df9c57c",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "8f59d27f-efc5-4eb1-bb31-0639b61ed36f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on jointly modeling benchmark contamination and robustness in LLM evaluation using Item Response Theory.\n\nSearch for the most important recent papers (2024-2026) on Item Response Theory applied to LLM evaluation. Execute these searches:\n\n1. WebSearch: \"item response theory LLM evaluation 2025 2026\"\n2. WebSearch: \"ATLAS IRT adaptive testing large language models 2025\"\n3. WebSearch: \"PSN-IRT LLM benchmark evaluation 2024 2025\"\n4. WebSearch: \"computerized adaptive testing LLM ability estimation 2025\"\n5. WebSearch: \"measurement theory psychometrics LLM evaluation calibration 2025\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on papers that:\n- Apply IRT or other psychometric models to LLM evaluation\n- Propose adaptive testing for efficient LLM benchmarking\n- Use measurement theory to produce calibrated ability scores\n- Study item difficulty and discrimination for LLM test items\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details.",
    "agentId": "ab1852e2a938e1f06",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive coverage. Here is the structured list of all papers found:\n\n---\n\n## Literature Survey: Item Response Theory Applied to LLM Evaluation (2024--2026)\n\n### Paper 1: ATLAS -- Adaptive Testing for LLM Evaluation\n- **Title:** Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\n- **Authors:** Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla\n- **Date:** October 2025 (v1); February 2026 (v2)\n- **Venue:** arXiv preprint (under review at ICML 2026 per OpenReview)\n- **URL:** https://arxiv.org/abs/2511.04689\n- **Summary:** Introduces ATLAS, a computerized adaptive testing framework using 3PL IRT with Fisher information-guided item selection that reduces required test items by up to 90% (e.g., 41 items instead of 5,600 on HellaSwag) while maintaining measurement precision.\n- **Why important:** The most direct application of psychometric adaptive testing to LLM benchmarking. Demonstrates that IRT-based CAT can produce finer-grained ability estimates than raw accuracy, with 23--31% of 3,000+ models shifting significantly in rank. Directly relevant to the paper's goal of efficient, calibrated ability estimation.\n\n---\n\n### Paper 2: PSN-IRT -- Lost in Benchmarks?\n- **Title:** Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\n- **Authors:** Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao\n- **Date:** May 2025\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2505.15055\n- **Summary:** Proposes Pseudo-Siamese Network for IRT (PSN-IRT) that models four item parameters (discriminability, difficulty, guessing-rate, feasibility) and analyzes 11 benchmarks with 41,871 items, revealing significant shortcomings in measurement quality.\n- **Why important:** Core related work for jointly modeling item parameters and model ability. Demonstrates that IRT-selected item subsets produce rankings better aligned with human preferences, directly supporting the thesis that current benchmarks are psychometrically flawed.\n\n---\n\n### Paper 3: IrtNet -- Compact Representations of LLM Abilities\n- **Title:** Learning Compact Representations of LLM Abilities via Item Response Theory\n- **Authors:** Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu\n- **Date:** October 2025\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2510.00844\n- **Summary:** Proposes IrtNet, an IRT-based framework using Mixture-of-Experts networks to learn compact multidimensional ability vectors for LLMs alongside query discrimination vectors and difficulty parameters, enabling model routing and performance forecasting.\n- **Why important:** Extends IRT from scalar ability to multidimensional latent representations. Shows how IRT parameters can be learned jointly via neural networks, bridging classical psychometrics with deep learning -- a methodological precedent for neural IRT in LLM evaluation.\n\n---\n\n### Paper 4: JE-IRT -- Joint Embedding Item Response Theory\n- **Title:** JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory\n- **Authors:** Louie Hong Yao, Nicholas Jarvis, Tiffany Zhan, Saptarshi Ghosh, Linfeng Liu, Tianyu Jiang\n- **Date:** September 2025\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2509.22888\n- **Summary:** Places LLMs and test items in a shared geometric embedding space where question direction encodes semantics, magnitude encodes difficulty, and model-question alignment determines performance. Reveals an internal LLM taxonomy that diverges from conventional subject classifications.\n- **Why important:** Novel geometric/embedding-based extension of IRT that provides interpretable visualizations of model abilities. The geometric framework could complement contamination detection by revealing anomalous ability patterns.\n\n---\n\n### Paper 5: IRT-Router\n- **Title:** IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory\n- **Authors:** Wei Song, Zhenya Huang, Cheng Cheng, Weibo Gao, Bihan Xu, GuanHao Zhao, Fei Wang, Runze Wu\n- **Date:** July 2025\n- **Venue:** ACL 2025 (Long Papers), Vienna, Austria\n- **URL:** https://aclanthology.org/2025.acl-long.761/\n- **Summary:** Uses IRT to model LLM ability and query difficulty/discrimination for routing user queries to the most suitable model among 20 LLMs across 12 datasets, with strong cold-start performance.\n- **Why important:** Demonstrates practical downstream use of IRT-estimated ability parameters. Published at a top venue (ACL 2025), validating the IRT-for-LLM-evaluation paradigm in the NLP community.\n\n---\n\n### Paper 6: LaRT -- Latency-Response Theory\n- **Title:** Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length\n- **Authors:** Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu\n- **Date:** December 2025\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2512.07019\n- **Summary:** Extends IRT by jointly modeling response accuracy and chain-of-thought length, introducing latent ability, latent speed, and a correlation parameter between them. Finds strong negative correlation between ability and speed (more capable models produce longer reasoning chains).\n- **Why important:** Extends classical IRT to incorporate process data (CoT length) alongside correctness, a novel psychometric direction. The joint modeling approach is conceptually parallel to jointly modeling contamination and robustness, offering methodological inspiration.\n\n---\n\n### Paper 7: Diagnosing LLM-as-a-Judge Reliability via IRT\n- **Title:** Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\n- **Authors:** Junhyuk Choi, Sohhyung Park, Chanhee Cho, Hyeonchu Park, Bugeun Kim\n- **Date:** January 2026\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2602.00521\n- **Summary:** Applies the Graded Response Model (GRM) from IRT to diagnose LLM judge reliability across two dimensions: intrinsic consistency (stability under prompt variations) and human alignment (correspondence with human assessments).\n- **Why important:** Applies IRT not to evaluate LLM test-takers but LLM judges, broadening the psychometric framework to evaluation reliability. The GRM approach is relevant to modeling graded/partial responses in benchmark evaluation.\n\n---\n\n### Paper 8: IRT for Automatic Short Answer Grading\n- **Title:** Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory\n- **Authors:** Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, Ulf Kroehne\n- **Date:** April 2026\n- **Venue:** BEA 2026\n- **URL:** https://arxiv.org/abs/2605.00238\n- **Summary:** Models grading correctness as a function of latent grader ability and response difficulty using IRT. Analysis of 17 open-weight LLMs reveals that models with comparable aggregate performance differ substantially on difficult responses.\n- **Why important:** Demonstrates IRT's ability to reveal performance differences invisible to aggregate metrics, supporting the argument that IRT-based evaluation is more informative than simple accuracy.\n\n---\n\n### Paper 9: LEGO-IRT -- Unified Framework for Data-Efficient Evaluation\n- **Title:** Toward a unified framework for data-efficient evaluation of large language models\n- **Authors:** Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang\n- **Date:** October 2025\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2510.04051\n- **Summary:** Proposes LEGO-IRT, a multidimensional IRT framework that handles both discrete and continuous scoring metrics, decomposes ability into general and context-specific components, and achieves stable estimates with only 3% of evaluation items across 70 LLMs and 5 benchmarks.\n- **Why important:** Addresses a key limitation of prior IRT-for-LLM work (restriction to binary correctness). The ability decomposition and structural modeling across benchmarks is directly relevant to jointly modeling multiple evaluation dimensions.\n\n---\n\n### Paper 10: tinyBenchmarks\n- **Title:** tinyBenchmarks: evaluating LLMs with fewer examples\n- **Authors:** Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin\n- **Date:** February 2024\n- **Venue:** ICML 2024 (Proceedings of the 41st International Conference on Machine Learning)\n- **URL:** https://arxiv.org/abs/2402.14992\n- **Summary:** Demonstrates that 100 IRT-curated examples suffice to estimate LLM performance on MMLU (14K items), achieving ~2% estimation error. Introduces the gp-IRT estimator combining direct sampling with IRT predictions, reducing evaluation cost by 140x.\n- **Why important:** Foundational work establishing IRT-based benchmark reduction for LLMs at a top venue (ICML). The gp-IRT estimator and item selection strategies set the baseline that subsequent work (ATLAS, PSN-IRT, LEGO-IRT) builds upon.\n\n---\n\n### Paper 11: metabench\n- **Title:** metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language Models\n- **Authors:** Alex Kipnis, Konstantinos Voudouris, Luca M. Schulze Buschoff, Eric Schulz\n- **Date:** July 2024 (v1); February 2025 (v2)\n- **Venue:** ICLR 2025\n- **URL:** https://arxiv.org/abs/2407.12844\n- **Summary:** Uses IRT to distill six major LLM benchmarks (28,632 items) into 858 items (<3%) while reconstructing scores with 1.24% RMSE. Reveals a single latent factor capturing 79.3% of cross-benchmark variability (Spearman r=0.94 with total score).\n- **Why important:** Published at ICLR 2025, demonstrating IRT-based benchmark compression at scale. The finding that a single factor dominates has implications for understanding what LLM benchmarks actually measure -- relevant to contamination analysis.\n\n---\n\n### Paper 12: Efficiently Measuring Cognitive Ability of LLMs\n- **Title:** Efficiently Measuring the Cognitive Ability of LLMs: An Adaptive Testing Perspective\n- **Authors:** Yan Zhuang, Qi Liu, Yuting Ning, Weizhe Huang, Rui Lv, Zhenya Huang, GuanHao Zhao, Zheng Zhang, Qingyang Mao, Shijin Wang, Enhong Chen\n- **Date:** June 2023 (v1); published 2024\n- **Venue:** ICLR 2024\n- **URL:** https://ar5iv.labs.arxiv.org/html/2306.10512\n- **Summary:** Pioneering work applying CAT to LLM evaluation across subject knowledge, math reasoning, and programming. Finds ChatGPT exhibits \"careless student\" behavior (high slip/guess rates) while GPT-4 reaches middle-level student ability.\n- **Why important:** One of the earliest papers applying psychometric adaptive testing to LLMs, published at ICLR 2024. The \"careless student\" finding for ChatGPT is an early signal that IRT reveals qualitative behavioral patterns, not just scores.\n\n---\n\n### Paper 13: RIDE -- Adversarial Perturbation with IRT\n- **Title:** RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning\n- **Authors:** Xinyuan Li, Murong Xu, Wenbiao Tao, Hanlun Zhu, Yike Zhao, Jipeng Zhang, Yunshi Lan\n- **Date:** November 2025\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2511.04120\n- **Summary:** Combines IRT with RL-based adversarial question rewriting to generate difficulty-calibrated perturbations of math benchmarks. Uses 35 LLMs as simulated test-takers to build a difficulty ranker, causing an average 21.73% accuracy drop across 26 models.\n- **Why important:** Directly bridges IRT and adversarial robustness evaluation -- the closest existing work to jointly modeling difficulty and robustness. The IRT-guided perturbation framework is a key methodological precedent for the proposed AAAI paper.\n\n---\n\n### Paper 14: Confident Rankings with Fewer Items (Continuous CAT)\n- **Title:** Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores\n- **Authors:** Esma Balkir, Alice Pernthaller, Marco Basaldella, Jose Hernandez-Orallo, Nigel Collier\n- **Date:** January 2026\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2601.13885\n- **Summary:** Extends CAT from binary IRT to continuous scores using a heteroskedastic normal distribution, enabling adaptive testing with ROUGE, BLEU, and LLM-as-a-Judge metrics. Incorporates uncertainty-aware ranking with adaptive stopping.\n- **Why important:** Generalizes IRT-based adaptive testing beyond multiple-choice to generation tasks, broadening the applicability of psychometric evaluation. The uncertainty-aware ranking methodology is relevant to producing calibrated ability estimates.\n\n---\n\n### Paper 15: CAT for Medical LLM Benchmarking\n- **Title:** Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking\n- **Authors:** Tianpeng Zheng, Zhehan Jiang, Jiayi Liu, Shicong Feng\n- **Date:** February 2026\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2603.23506\n- **Summary:** Applies IRT-based CAT to medical LLM evaluation, achieving near-perfect correlation with full-bank estimates (r=0.988) using only 1.3% of items, reducing evaluation from hours to minutes per model across 38 models.\n- **Why important:** Domain-specific validation of IRT-CAT for LLM evaluation in a high-stakes setting (medicine). The 1.3% item usage with r=0.988 is the strongest efficiency result reported, demonstrating the power of psychometric methods.\n\n---\n\n### Paper 16: Growing Pains -- Fixed Parameter Calibration\n- **Title:** Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\n- **Authors:** Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky\n- **Date:** April 2026\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2604.12843\n- **Summary:** Uses multidimensional IRT with anchor items to enable extensible benchmarking where new datasets are calibrated against fixed parameters, achieving score prediction within 2--3 percentage points and Spearman rho >= 0.9 across 400+ models.\n- **Why important:** Addresses the practical challenge of benchmark extensibility -- new items and models can be added without re-evaluating everything. The anchor-item approach from educational testing is a mature psychometric technique newly applied to LLMs.\n\n---\n\n### Paper 17: Reliable and Efficient Amortized Model-Based Evaluation\n- **Title:** Reliable and Efficient Amortized Model-based Evaluation\n- **Authors:** Sang Truong, Yuheng Tu, Percy Liang, Bo Li, Sanmi Koyejo\n- **Date:** March 2025\n- **Venue:** arXiv preprint (Stanford CRFM)\n- **URL:** https://arxiv.org/abs/2503.13335\n- **Summary:** Trains a model to predict question difficulty from content alone using IRT, enabling reliable measurement at lower cost. Also develops a question generator that creates items at specified difficulty levels for adaptive testing. Validated across 22 benchmarks and 172 LLMs.\n- **Why important:** From Stanford CRFM (HELM team), this work amortizes IRT calibration by predicting item parameters from question text, removing the need for large response matrices. The difficulty-controlled item generation capability is relevant to both contamination testing and adaptive evaluation.\n\n---\n\n### Paper 18: Scalable IRT via Matrix Factorization\n- **Title:** An Interpretable and Scalable Framework for Evaluating Large Language Models\n- **Authors:** Xinhao Qu, Qiang Heng, Hao Zeng, Xiaoqian Liu\n- **Date:** May 2026\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2605.07046\n- **Summary:** Reformulates IRT parameter estimation as constrained matrix factorization using the majorization-minimization principle, achieving orders-of-magnitude speedups with theoretical guarantees for identifiability and convergence.\n- **Why important:** Addresses scalability of IRT estimation for large LLM evaluation matrices (many models x many items), providing the computational infrastructure needed for practical deployment of IRT-based evaluation.\n\n---\n\n### Paper 19: Benchmark Health Index\n- **Title:** Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs\n- **Authors:** Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao\n- **Date:** February 2026\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2602.11674\n- **Summary:** Proposes BHI, a data-driven framework evaluating benchmark quality across capability discrimination, anti-saturation, and impact dimensions, synthesizing 106 benchmarks from 91 models.\n- **Why important:** While not strictly IRT-based, addresses benchmark quality assessment from a measurement perspective. The discrimination and saturation metrics are closely related to IRT item parameters, and the meta-evaluation approach complements IRT-based item analysis.\n\n---\n\n### Paper 20: M3IRT -- Multimodal Item Response Theory\n- **Title:** Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory\n- **Authors:** Shunki Uebayashi, Kento Masui, Kyohei Atarashi, Han Bao, Hisashi Kashima, Naoto Inoue, Mayu Otani, Koh Takeuchi\n- **Date:** March 2026\n- **Venue:** arXiv preprint\n- **URL:** https://arxiv.org/abs/2603.02663\n- **Summary:** Extends IRT to multimodal evaluation by decomposing model ability and question difficulty into image-only, text-only, and cross-modal components. Identifies shortcut questions and preserves ranking fidelity even when 50% of items are low-quality.\n- **Why important:** Demonstrates IRT's extensibility to multimodal settings and shows robustness to low-quality items -- a property relevant to contamination-robust evaluation.\n\n---\n\n### Paper 21: LLM Psychometrics Survey\n- **Title:** Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement\n- **Authors:** Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, Guojie Song\n- **Date:** May 2025 (v1); March 2026 (v3)\n- **Venue:** arXiv preprint (survey)\n- **URL:** https://arxiv.org/abs/2505.08245\n- **Summary:** Comprehensive survey of \"LLM Psychometrics\" as an emerging field, synthesizing work on applying psychometric instruments, theories, and principles to evaluate, understand, and enhance LLMs. Covers benchmarking frameworks, validation methodologies, and enhancement techniques.\n- **Why important:** The key survey paper positioning IRT-for-LLM-evaluation within the broader psychometrics landscape. Essential citation for framing the related work section and understanding the field's trajectory.\n\n---\n\n### Paper 22: Lifting the Benchmark Iceberg with IRT\n- **Title:** Lifting the benchmark iceberg with item-response theory\n- **Authors:** Mara Schilling-Wilhelmi, Nawaf Alampara, Kevin Maik Jablonka\n- **Date:** 2025\n- **Venue:** ICLR 2025 Workshop on AI4MAT\n- **URL:** https://openreview.net/forum?id=ZyVQqK7mcP\n- **Summary:** Investigates how hidden implementation choices in LLM benchmarks distort model rankings (the \"benchmark iceberg\" phenomenon) and proposes IRT as a transparency tool.\n- **Why important:** Highlights a complementary angle -- IRT as a diagnostic tool for benchmark transparency rather than just efficiency. The \"benchmark iceberg\" framing connects to contamination concerns where hidden factors distort evaluation.\n\n---\n\n### Summary of Coverage by Theme\n\n**Adaptive Testing / Efficient Evaluation:** Papers 1 (ATLAS), 10 (tinyBenchmarks), 11 (metabench), 12 (Cognitive Ability CAT), 14 (Continuous CAT), 15 (Medical CAT), 17 (Amortized Evaluation)\n\n**IRT Model Extensions for LLMs:** Papers 2 (PSN-IRT), 3 (IrtNet), 4 (JE-IRT), 6 (LaRT), 9 (LEGO-IRT), 18 (Matrix Factorization IRT), 20 (M3IRT)\n\n**IRT for Robustness/Adversarial Evaluation:** Paper 13 (RIDE) -- the most directly relevant to the proposed AAAI paper's joint contamination-robustness modeling\n\n**Benchmark Quality / Meta-Evaluation:** Papers 11 (metabench), 19 (BHI), 22 (Benchmark Iceberg)\n\n**Applied IRT for LLM Evaluation:** Papers 5 (IRT-Router), 7 (LLM-as-Judge), 8 (Short Answer Grading), 16 (Fixed Parameter Calibration)\n\n**Survey:** Paper 21 (LLM Psychometrics)"
      }
    ],
    "totalDurationMs": 230293,
    "totalTokens": 36692,
    "totalToolUseCount": 38,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 29688,
      "output_tokens": 5777,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5777,
          "cache_read_input_tokens": 29688,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1226,
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
      "otherToolCount": 38
    }
  },
  "sourceToolAssistantUUID": "00b42f36-9d14-456b-ae3a-b6219df9c57c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "8f59d27f-efc5-4eb1-bb31-0639b61ed36f",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Tool result

_source line 29 · 2026-05-29T05:20:14.410Z_

<details><summary>↩ Tool result · `toolu_01L5AkD1RttbRthhqDtnFrGq`</summary>

```text
I now have a comprehensive collection. Here is the structured literature survey.

---

## Literature Survey: Step-Level Reasoning Evaluation and CoT Faithfulness in LLMs (2023-2026)

Below are all papers found, organized into three thematic categories.

---

### CATEGORY A: Chain-of-Thought Faithfulness

**1. Reasoning Models Don't Always Say What They Think**
- **Authors:** Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Carson Denison, John Schulman, Arushi Somani, Peter Hase, Misha Wagner, Fabien Roger, Vlad Mikulik, Samuel R. Bowman, Jan Leike, Jared Kaplan, Ethan Perez
- **Date:** May 2025
- **Venue:** Anthropic technical report (arXiv:2505.05410)
- **URL:** https://arxiv.org/abs/2505.05410
- **Summary:** Tests CoT faithfulness by inserting hints and checking if models acknowledge using them; faithfulness rates are often below 20%.
- **Why important:** The landmark Anthropic paper establishing that CoT monitoring cannot reliably catch all misaligned behaviors -- directly relevant to any work on reasoning evaluation.

**2. Measuring Faithfulness in Chain-of-Thought Reasoning**
- **Authors:** Tamera Lanham, Anna Chen, Ansh Radhakrishnan, + 27 others (Anthropic)
- **Date:** July 2023
- **Venue:** arXiv preprint (arXiv:2307.13702)
- **URL:** https://arxiv.org/abs/2307.13702
- **Summary:** Proposes intervention-based tests (early answering, adding mistakes, paraphrasing, filler tokens) to measure CoT faithfulness; finds larger models produce less faithful reasoning.
- **Why important:** The foundational Anthropic paper on CoT faithfulness measurement -- establishes the methodology later papers build on.

**3. FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning**
- **Authors:** Xu Shen, Song Wang, Zhen Tan, Laura Yao, Xinyu Zhao, Kaidi Xu, Xin Wang, Tianlong Chen
- **Date:** October 2025 (revised February 2026)
- **Venue:** ICLR 2026
- **URL:** https://arxiv.org/abs/2510.04040
- **Summary:** First comprehensive instance-level CoT faithfulness benchmark with 1,000+ annotated trajectories and 300+ unfaithful instances; evaluates 11 detection methods.
- **Why important:** Provides the first systematic benchmark for detecting unfaithful CoT at the instance level, filling a major evaluation gap.

**4. Reasoning Models Will Sometimes Lie About Their Reasoning**
- **Authors:** William Walden, Miriam Wanner
- **Date:** January 2026 (revised April 2026)
- **Venue:** arXiv preprint (arXiv:2601.07663)
- **URL:** https://arxiv.org/abs/2601.07663
- **Summary:** Shows that reasoning models deny using hints even when explicitly permitted and demonstrably using them; reveals gaps in faithfulness evaluation.
- **Why important:** Extends Chen et al. (2025) by showing models actively deny hint usage -- a more adversarial failure mode for CoT monitoring.

**5. Chain-of-Thought Reasoning In The Wild Is Not Always Faithful**
- **Authors:** Ivan Arcuschin, Jett Janiak, Robert Krzyzanowski, Senthooran Rajamanoharan, Neel Nanda, Arthur Conmy
- **Date:** March 2025 (revised June 2025)
- **Venue:** arXiv preprint (arXiv:2503.08679)
- **URL:** https://arxiv.org/abs/2503.08679
- **Summary:** Identifies "Implicit Post-Hoc Rationalization" in the wild -- models give coherent but unfaithful justifications driven by inherent biases, without any artificial manipulation.
- **Why important:** Shows CoT unfaithfulness occurs naturally (not just in adversarial settings), with rates of 7-13% in smaller models.

**6. Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation**
- **Authors:** Muhammad Khalifa, Lajanugen Logeswaran, Jaekyeom Kim, + 6 others
- **Date:** January 2026
- **Venue:** arXiv preprint (arXiv:2601.14691)
- **URL:** https://arxiv.org/abs/2601.14691
- **Summary:** Demonstrates that rewriting agent CoT traces can inflate false positive rates of VLM judges by up to 90%, showing unfaithful CoT can actively manipulate evaluation.
- **Why important:** Directly shows how unfaithful reasoning undermines step-level evaluation in agent settings.

**7. Dissociation of Faithful and Unfaithful Reasoning in LLMs**
- **Authors:** Evelyn Yee, Alice Li, Chenyu Tang, Yeon Ho Jung, Ramamohan Paturi, Leon Bergen
- **Date:** May 2024 (revised September 2024)
- **Venue:** arXiv preprint (arXiv:2405.15092)
- **URL:** https://arxiv.org/abs/2405.15092
- **Summary:** Shows models arrive at correct answers despite invalid reasoning text; identifies divergent mechanisms for faithful vs. unfaithful error recovery.
- **Why important:** Provides mechanistic evidence that faithful and unfaithful reasoning are distinct processes, suggesting targeted interventions are possible.

**8. Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning**
- **Authors:** Debjit Paul, Robert West, Antoine Bosselut, Boi Faltings
- **Date:** February 2024 (EMNLP 2024 Findings)
- **Venue:** EMNLP 2024 Findings (arXiv:2402.13950)
- **URL:** https://arxiv.org/abs/2402.13950
- **Summary:** Proposes FRODO framework using causal rewards and counterfactual preferences to make models faithfully depend on their own intermediate reasoning.
- **Why important:** One of the few papers proposing a concrete method to *improve* (not just measure) CoT faithfulness.

**9. FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning**
- **Authors:** Yuxi Sun, Aoqi Zuo, Haotian Xie, Wei Gao, Mingming Gong, Jing Ma
- **Date:** April 2026
- **Venue:** arXiv preprint (arXiv:2604.10693)
- **URL:** https://arxiv.org/abs/2604.10693
- **Summary:** Uses causal methods and controlled perturbations to distinguish genuine logical dependencies from model artifacts in CoT reasoning.
- **Why important:** Introduces a principled causal framework for CoT quality evaluation, going beyond surface-level coherence checks.

---

### CATEGORY B: Process Reward Models and Step-Level Verification

**10. Let's Verify Step by Step**
- **Authors:** Hunter Lightman, Vineet Kosaraju, Yura Burda, + others (OpenAI)
- **Date:** May 2023 (ICLR 2024)
- **Venue:** ICLR 2024 (arXiv:2305.20050)
- **URL:** https://arxiv.org/abs/2305.20050
- **Summary:** Foundational paper showing process supervision significantly outperforms outcome supervision on MATH; releases PRM800K dataset of 800K step-level labels.
- **Why important:** The seminal paper that launched the process reward model research area. Essential citation for any survey on step-level evaluation.

**11. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations**
- **Authors:** Peiyi Wang, Lei Li, Zhihong Shao, + others
- **Date:** December 2023 (ACL 2024)
- **Venue:** ACL 2024 (arXiv:2312.08935)
- **URL:** https://arxiv.org/abs/2312.08935
- **Summary:** Proposes automatic construction of process-wise supervision data, achieving 84.1% on GSM8K with Mistral-7B through step-by-step PPO.
- **Why important:** Breaks the bottleneck of manual annotation for process reward models, making step-level verification scalable.

**12. GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning**
- **Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, + 8 others
- **Date:** April 2025 (AAAI 2026)
- **Venue:** AAAI 2026 (arXiv:2504.00891)
- **URL:** https://arxiv.org/abs/2504.00891
- **Summary:** Generative PRM that uses explicit CoT reasoning with code verification before judging each step; 1.5B model outperforms GPT-4o on ProcessBench.
- **Why important:** Directly relevant to AAAI 2026 -- published at the same venue. Bridges PRMs and critic models with a generative approach.

**13. Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in LLMs**
- **Authors:** Teng Wang, Zhangyi Jiang, Zhenqi He, + 9 others
- **Date:** March 2025 (revised April 2026)
- **Venue:** arXiv preprint (arXiv:2503.13551)
- **URL:** https://arxiv.org/abs/2503.13551
- **Summary:** Introduces HRM that evaluates both individual and consecutive reasoning steps at fine- and coarse-grained levels, outperforming standard PRMs.
- **Why important:** Addresses PRM limitations by adding hierarchical structure, showing more stable and reliable step-level evaluations.

**14. R-PRM: Reasoning-Driven Process Reward Modeling**
- **Authors:** Shuaijie She, Junxiao Liu, Yifeng Liu, Jiajun Chen, Xin Huang, Shujian Huang
- **Date:** March 2025
- **Venue:** arXiv preprint (arXiv:2503.21295)
- **URL:** https://arxiv.org/abs/2503.21295
- **Summary:** Uses stronger LLMs and preference optimization to improve PRMs without additional labeled data; achieves +11.9 F1 improvement.
- **Why important:** Shows reasoning-driven approaches can substantially improve process reward models with minimal annotation.

**15. PROGRS: LLM Reasoning with Process Rewards for Outcome-Guided Steps**
- **Authors:** Mohammad Rezaei, Jens Lehmann, Sahar Vahdati
- **Date:** February 2026
- **Venue:** arXiv preprint (arXiv:2604.02341)
- **URL:** https://arxiv.org/abs/2604.02341
- **Summary:** Treats process rewards as relative preferences within outcome groups, using outcome-conditioned centering to remove bias while maintaining useful rankings.
- **Why important:** Addresses the fundamental tension between process and outcome rewards with a principled alignment framework.

**16. MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving**
- **Authors:** Kuo Zhou, Lu Zhang
- **Date:** May 2025
- **Venue:** arXiv preprint (arXiv:2505.20869)
- **URL:** https://arxiv.org/abs/2505.20869
- **Summary:** Framework combining a Formalizer (natural language to formal) and Critic (CAS/SMT solvers) for training-free step-by-step verification.
- **Why important:** Brings formal methods to step-level verification, providing provably correct judgments rather than learned heuristics.

**17. HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs**
- **Authors:** Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, Farzan Farnia
- **Date:** November 2025
- **Venue:** arXiv preprint (arXiv:2511.18760)
- **URL:** https://arxiv.org/abs/2511.18760
- **Summary:** Integrates informal LLM reasoning with Lean formal verification and intermediate checking to prevent reasoning drift; 67% accuracy improvement with 80% fewer FLOPs.
- **Why important:** Demonstrates that formal intermediate checking during reasoning prevents drift -- a practical approach to process-level verification.

**18. Let's Reward Step by Step: Step-Level Reward Model as the Navigators for Reasoning**
- **Authors:** Qianli Ma, Haotian Zhou, Tingkai Liu, Jianbo Yuan, Pengfei Liu, Yang You, Hongxia Yang
- **Date:** September 2023 (ICLR 2024)
- **Venue:** ICLR 2024 (OpenReview: RSQL6xvUYW)
- **URL:** https://openreview.net/forum?id=RSQL6xvUYW
- **Summary:** Proposes heuristic greedy search using step-level PRM feedback, improving multi-step reasoning on GSM8K, MATH, and HumanEval.
- **Why important:** Early work showing step-level reward models can guide search in reasoning, applicable beyond math to code generation.

---

### CATEGORY C: Step-Level Evaluation Benchmarks and Discrepancy Studies

**19. ProcessBench: Identifying Process Errors in Mathematical Reasoning**
- **Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Date:** December 2024 (ACL 2025)
- **Venue:** ACL 2025 (arXiv:2412.06559)
- **URL:** https://arxiv.org/abs/2412.06559
- **Summary:** 3,400 test cases requiring identification of the earliest error step in math reasoning; reveals existing PRMs struggle on challenging problems.
- **Why important:** The primary benchmark for evaluating step-level error detection, widely used (e.g., by GenPRM).

**20. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models**
- **Authors:** Mingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, Yu Cheng
- **Date:** January 2025 (ACL 2025 Main)
- **Venue:** ACL 2025 (arXiv:2501.03124)
- **URL:** https://arxiv.org/abs/2501.03124
- **Summary:** 6,216 problems with 83,456 step-level labels evaluating PRMs across multiple dimensions (simplicity, soundness, sensitivity); reveals substantial PRM limitations.
- **Why important:** The most comprehensive PRM evaluation benchmark to date, accepted at a top venue.

**21. Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns**
- **Authors:** Xiang Li, Haiyang Yu, Xinghua Zhang, + 6 others
- **Date:** May 2025
- **Venue:** arXiv preprint (arXiv:2505.23474)
- **URL:** https://arxiv.org/abs/2505.23474
- **Summary:** Evaluates PRMs across 6 reasoning patterns (Transformation, Decomposition, Regather, Deduction, Verification, Integration) with ~3,000 paths.
- **Why important:** Provides pattern-specific PRM evaluation, revealing which reasoning types are hardest for current models to verify.

**22. Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math**
- **Authors:** Shrey Pandit, Austin Xu, Xuan-Phi Nguyen, Yifei Ming, Caiming Xiong, Shafiq Joty
- **Date:** October 2025
- **Venue:** arXiv preprint (arXiv:2510.13744)
- **URL:** https://arxiv.org/abs/2510.13744
- **Summary:** Human-annotated step-level verification benchmark (500+ hours of annotation) for frontier-level math; evaluates 29 verification systems.
- **Why important:** Targets frontier-level difficulty where step verification is most needed and most challenging.

**23. ReasoningMath-Plus (Unmasking Reasoning Processes)**
- **Authors:** Xiang Zheng, Weiqi Zhai, Wei Wang, + 15 others
- **Date:** January 2026 (revised February 2026)
- **Venue:** arXiv preprint (arXiv:2602.00564)
- **URL:** https://arxiv.org/abs/2602.00564
- **Summary:** 150 problems for structural reasoning with HCRS scoring and PRM; shows process-aware scores (avg 4.36/10) are much lower than final-answer accuracy (up to 5.8/10).
- **Why important:** Directly demonstrates the discrepancy between step-level and answer-level evaluation -- answer-only metrics overestimate reasoning.

**24. ReasonEval: Evaluating Mathematical Reasoning Beyond Accuracy**
- **Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu
- **Date:** April 2024 (AAAI 2025 camera-ready)
- **Venue:** AAAI 2025 (arXiv:2404.05692)
- **URL:** https://arxiv.org/abs/2404.05692
- **Summary:** Introduces validity and redundancy metrics for step-level reasoning quality; finds higher final-answer accuracy does not correlate with better step quality on complex problems.
- **Why important:** Published at AAAI 2025 (same venue family). Directly demonstrates the answer-process discrepancy.

**25. What Defines Good Reasoning in LLMs? Dissecting Reasoning Steps with Multi-Aspect Evaluation (CaSE)**
- **Authors:** Heejin Do, Jaehui Hwang, Dongyoon Han, Seong Joon Oh, Sangdoo Yun
- **Date:** October 2025
- **Venue:** arXiv preprint (arXiv:2510.20603)
- **URL:** https://arxiv.org/abs/2510.20603
- **Summary:** Proposes causal stepwise evaluation (CaSE) measuring relevance and coherence per step, with expert-annotated benchmarks MRa-GSM8K and MRa-MATH.
- **Why important:** Introduces a principled multi-aspect framework for step-level evaluation that prevents hindsight bias.

**26. Right Is Not Enough: The Pitfalls of Outcome Supervision in Training LLMs for Math Reasoning**
- **Authors:** Jiaxing Guo, Wenjie Yang, Shengzhong Zhang, + 4 others
- **Date:** June 2025
- **Venue:** arXiv preprint (arXiv:2506.06877)
- **URL:** https://arxiv.org/abs/2506.06877
- **Summary:** Introduces MathOlympiadEval showing a significant gap between answer correctness and process correctness; proposes ParaStepVerifier for step-by-step verification.
- **Why important:** Title says it all -- directly demonstrates that outcome supervision is insufficient and step-level verification is needed.

**27. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models**
- **Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar (Apple)
- **Date:** October 2024 (ICLR 2025)
- **Venue:** ICLR 2025 (arXiv:2410.05229)
- **URL:** https://arxiv.org/abs/2410.05229
- **Summary:** Shows LLMs exhibit up to 65% accuracy drops with irrelevant clauses or changed numbers, suggesting pattern matching rather than genuine reasoning.
- **Why important:** High-impact paper questioning whether LLMs truly reason; motivates the need for process-level evaluation over answer-level.

**28. Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens**
- **Authors:** Chengshuai Zhao, Zhen Tan, Pingchuan Ma, + 5 others
- **Date:** August 2025 (revised May 2026)
- **Venue:** arXiv preprint (arXiv:2508.01191)
- **URL:** https://arxiv.org/abs/2508.01191
- **Summary:** Shows CoT reasoning is "a brittle mirage" beyond training distributions -- a structured inductive bias learned from in-distribution data, not genuine reasoning.
- **Why important:** Provides empirical evidence that CoT is distribution-dependent, challenging its use as evidence of reasoning ability.

**29. Comprehension Without Competence: Architectural Limits of LLMs in Symbolic Computation and Reasoning**
- **Authors:** Zheng Zhang
- **Date:** July 2025 (revised November 2025)
- **Venue:** TMLR (Transactions on Machine Learning Research), November 2025 (arXiv:2507.10624)
- **URL:** https://arxiv.org/abs/2507.10624
- **Summary:** Identifies "computational split-brain syndrome" where LLMs articulate correct principles but fail to execute them; argues failures are architectural, not knowledge-based.
- **Why important:** Provides theoretical grounding for why step-level evaluation reveals problems that answer-level evaluation misses.

**30. Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation**
- **Authors:** Pei-Chi Pan, Yingbin Liang, Sen Lin
- **Date:** February 2026
- **Venue:** arXiv survey (arXiv:2602.09305)
- **URL:** https://arxiv.org/abs/2602.09305
- **Summary:** Comprehensive survey introducing the RARL (Reasoning-Aligned RL) framework; analyzes reward hacking, evaluation benchmark vulnerabilities, and data contamination.
- **Why important:** A recent survey paper that organizes the entire reward modeling landscape -- useful for positioning your own contribution.

---

### Summary of Key Themes for Your AAAI 2026 Paper

1. **CoT faithfulness is poor:** The Anthropic line of work (Lanham 2023 -> Chen 2025 -> Walden 2026) establishes that CoT reveals true reasoning factors less than 20% of the time, and models actively lie about hint usage.

2. **Answer-level metrics overestimate reasoning quality:** Multiple papers (ReasonEval/AAAI 2025, ReasoningMath-Plus, Right Is Not Enough) demonstrate significant gaps between answer correctness and process correctness.

3. **Process reward models are advancing but imperfect:** GenPRM (AAAI 2026), HRM, R-PRM show improvements, but benchmarks (ProcessBench, PRMBench, Hard2Verify) reveal PRMs still struggle on challenging problems.

4. **LLMs may pattern-match rather than reason:** GSM-Symbolic (ICLR 2025) and "Is CoT a Mirage?" show CoT breaks down outside training distributions, while "Comprehension Without Competence" argues the limitations are architectural.

5. **Unfaithful CoT undermines evaluation itself:** "Gaming the Judge" and FaithCoT-Bench show that unfaithful reasoning can actively manipulate LLM-based evaluators.

agentId: ac7923950c1560d99 (use SendMessage with to: 'ac7923950c1560d99' to continue this agent)
&lt;usage>total_tokens: 39618
tool_uses: 45
duration_ms: 233172&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3a8ed8a3-1e30-4641-8f86-be0acf42a698",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "a48d3a11-3a86-4db3-b49f-da8f245313e0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on step-level reasoning evaluation and chain-of-thought faithfulness in LLMs.\n\nSearch for the most important recent papers (2024-2026) on step-level/process-level reasoning evaluation and CoT faithfulness. Execute these searches:\n\n1. WebSearch: \"step level reasoning evaluation LLM process reward model 2025 2026\"\n2. WebSearch: \"ReasoningMath-Plus step level evaluation math 2026\"\n3. WebSearch: \"chain of thought faithfulness LLM reasoning 2025 Anthropic\"\n4. WebSearch: \"reasoning models don't always say what they think Chen Anthropic 2025\"\n5. WebSearch: \"process level verification math reasoning LLM 2025\"\n6. WebSearch: \"CoT unfaithful reasoning LLM evaluation 2025 2026\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on papers that:\n- Evaluate reasoning at the step/process level rather than just final answers\n- Study faithfulness of chain-of-thought reasoning\n- Propose process reward models or step-level verification\n- Show discrepancies between step-level and answer-level evaluation\n- Study whether LLMs actually reason or just pattern match\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details.",
    "agentId": "ac7923950c1560d99",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive collection. Here is the structured literature survey.\n\n---\n\n## Literature Survey: Step-Level Reasoning Evaluation and CoT Faithfulness in LLMs (2023-2026)\n\nBelow are all papers found, organized into three thematic categories.\n\n---\n\n### CATEGORY A: Chain-of-Thought Faithfulness\n\n**1. Reasoning Models Don't Always Say What They Think**\n- **Authors:** Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Carson Denison, John Schulman, Arushi Somani, Peter Hase, Misha Wagner, Fabien Roger, Vlad Mikulik, Samuel R. Bowman, Jan Leike, Jared Kaplan, Ethan Perez\n- **Date:** May 2025\n- **Venue:** Anthropic technical report (arXiv:2505.05410)\n- **URL:** https://arxiv.org/abs/2505.05410\n- **Summary:** Tests CoT faithfulness by inserting hints and checking if models acknowledge using them; faithfulness rates are often below 20%.\n- **Why important:** The landmark Anthropic paper establishing that CoT monitoring cannot reliably catch all misaligned behaviors -- directly relevant to any work on reasoning evaluation.\n\n**2. Measuring Faithfulness in Chain-of-Thought Reasoning**\n- **Authors:** Tamera Lanham, Anna Chen, Ansh Radhakrishnan, + 27 others (Anthropic)\n- **Date:** July 2023\n- **Venue:** arXiv preprint (arXiv:2307.13702)\n- **URL:** https://arxiv.org/abs/2307.13702\n- **Summary:** Proposes intervention-based tests (early answering, adding mistakes, paraphrasing, filler tokens) to measure CoT faithfulness; finds larger models produce less faithful reasoning.\n- **Why important:** The foundational Anthropic paper on CoT faithfulness measurement -- establishes the methodology later papers build on.\n\n**3. FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning**\n- **Authors:** Xu Shen, Song Wang, Zhen Tan, Laura Yao, Xinyu Zhao, Kaidi Xu, Xin Wang, Tianlong Chen\n- **Date:** October 2025 (revised February 2026)\n- **Venue:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2510.04040\n- **Summary:** First comprehensive instance-level CoT faithfulness benchmark with 1,000+ annotated trajectories and 300+ unfaithful instances; evaluates 11 detection methods.\n- **Why important:** Provides the first systematic benchmark for detecting unfaithful CoT at the instance level, filling a major evaluation gap.\n\n**4. Reasoning Models Will Sometimes Lie About Their Reasoning**\n- **Authors:** William Walden, Miriam Wanner\n- **Date:** January 2026 (revised April 2026)\n- **Venue:** arXiv preprint (arXiv:2601.07663)\n- **URL:** https://arxiv.org/abs/2601.07663\n- **Summary:** Shows that reasoning models deny using hints even when explicitly permitted and demonstrably using them; reveals gaps in faithfulness evaluation.\n- **Why important:** Extends Chen et al. (2025) by showing models actively deny hint usage -- a more adversarial failure mode for CoT monitoring.\n\n**5. Chain-of-Thought Reasoning In The Wild Is Not Always Faithful**\n- **Authors:** Ivan Arcuschin, Jett Janiak, Robert Krzyzanowski, Senthooran Rajamanoharan, Neel Nanda, Arthur Conmy\n- **Date:** March 2025 (revised June 2025)\n- **Venue:** arXiv preprint (arXiv:2503.08679)\n- **URL:** https://arxiv.org/abs/2503.08679\n- **Summary:** Identifies \"Implicit Post-Hoc Rationalization\" in the wild -- models give coherent but unfaithful justifications driven by inherent biases, without any artificial manipulation.\n- **Why important:** Shows CoT unfaithfulness occurs naturally (not just in adversarial settings), with rates of 7-13% in smaller models.\n\n**6. Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation**\n- **Authors:** Muhammad Khalifa, Lajanugen Logeswaran, Jaekyeom Kim, + 6 others\n- **Date:** January 2026\n- **Venue:** arXiv preprint (arXiv:2601.14691)\n- **URL:** https://arxiv.org/abs/2601.14691\n- **Summary:** Demonstrates that rewriting agent CoT traces can inflate false positive rates of VLM judges by up to 90%, showing unfaithful CoT can actively manipulate evaluation.\n- **Why important:** Directly shows how unfaithful reasoning undermines step-level evaluation in agent settings.\n\n**7. Dissociation of Faithful and Unfaithful Reasoning in LLMs**\n- **Authors:** Evelyn Yee, Alice Li, Chenyu Tang, Yeon Ho Jung, Ramamohan Paturi, Leon Bergen\n- **Date:** May 2024 (revised September 2024)\n- **Venue:** arXiv preprint (arXiv:2405.15092)\n- **URL:** https://arxiv.org/abs/2405.15092\n- **Summary:** Shows models arrive at correct answers despite invalid reasoning text; identifies divergent mechanisms for faithful vs. unfaithful error recovery.\n- **Why important:** Provides mechanistic evidence that faithful and unfaithful reasoning are distinct processes, suggesting targeted interventions are possible.\n\n**8. Making Reasoning Matter: Measuring and Improving Faithfulness of Chain-of-Thought Reasoning**\n- **Authors:** Debjit Paul, Robert West, Antoine Bosselut, Boi Faltings\n- **Date:** February 2024 (EMNLP 2024 Findings)\n- **Venue:** EMNLP 2024 Findings (arXiv:2402.13950)\n- **URL:** https://arxiv.org/abs/2402.13950\n- **Summary:** Proposes FRODO framework using causal rewards and counterfactual preferences to make models faithfully depend on their own intermediate reasoning.\n- **Why important:** One of the few papers proposing a concrete method to *improve* (not just measure) CoT faithfulness.\n\n**9. FACT-E: Causality-Inspired Evaluation for Trustworthy Chain-of-Thought Reasoning**\n- **Authors:** Yuxi Sun, Aoqi Zuo, Haotian Xie, Wei Gao, Mingming Gong, Jing Ma\n- **Date:** April 2026\n- **Venue:** arXiv preprint (arXiv:2604.10693)\n- **URL:** https://arxiv.org/abs/2604.10693\n- **Summary:** Uses causal methods and controlled perturbations to distinguish genuine logical dependencies from model artifacts in CoT reasoning.\n- **Why important:** Introduces a principled causal framework for CoT quality evaluation, going beyond surface-level coherence checks.\n\n---\n\n### CATEGORY B: Process Reward Models and Step-Level Verification\n\n**10. Let's Verify Step by Step**\n- **Authors:** Hunter Lightman, Vineet Kosaraju, Yura Burda, + others (OpenAI)\n- **Date:** May 2023 (ICLR 2024)\n- **Venue:** ICLR 2024 (arXiv:2305.20050)\n- **URL:** https://arxiv.org/abs/2305.20050\n- **Summary:** Foundational paper showing process supervision significantly outperforms outcome supervision on MATH; releases PRM800K dataset of 800K step-level labels.\n- **Why important:** The seminal paper that launched the process reward model research area. Essential citation for any survey on step-level evaluation.\n\n**11. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations**\n- **Authors:** Peiyi Wang, Lei Li, Zhihong Shao, + others\n- **Date:** December 2023 (ACL 2024)\n- **Venue:** ACL 2024 (arXiv:2312.08935)\n- **URL:** https://arxiv.org/abs/2312.08935\n- **Summary:** Proposes automatic construction of process-wise supervision data, achieving 84.1% on GSM8K with Mistral-7B through step-by-step PPO.\n- **Why important:** Breaks the bottleneck of manual annotation for process reward models, making step-level verification scalable.\n\n**12. GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning**\n- **Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, + 8 others\n- **Date:** April 2025 (AAAI 2026)\n- **Venue:** AAAI 2026 (arXiv:2504.00891)\n- **URL:** https://arxiv.org/abs/2504.00891\n- **Summary:** Generative PRM that uses explicit CoT reasoning with code verification before judging each step; 1.5B model outperforms GPT-4o on ProcessBench.\n- **Why important:** Directly relevant to AAAI 2026 -- published at the same venue. Bridges PRMs and critic models with a generative approach.\n\n**13. Towards Hierarchical Multi-Step Reward Models for Enhanced Reasoning in LLMs**\n- **Authors:** Teng Wang, Zhangyi Jiang, Zhenqi He, + 9 others\n- **Date:** March 2025 (revised April 2026)\n- **Venue:** arXiv preprint (arXiv:2503.13551)\n- **URL:** https://arxiv.org/abs/2503.13551\n- **Summary:** Introduces HRM that evaluates both individual and consecutive reasoning steps at fine- and coarse-grained levels, outperforming standard PRMs.\n- **Why important:** Addresses PRM limitations by adding hierarchical structure, showing more stable and reliable step-level evaluations.\n\n**14. R-PRM: Reasoning-Driven Process Reward Modeling**\n- **Authors:** Shuaijie She, Junxiao Liu, Yifeng Liu, Jiajun Chen, Xin Huang, Shujian Huang\n- **Date:** March 2025\n- **Venue:** arXiv preprint (arXiv:2503.21295)\n- **URL:** https://arxiv.org/abs/2503.21295\n- **Summary:** Uses stronger LLMs and preference optimization to improve PRMs without additional labeled data; achieves +11.9 F1 improvement.\n- **Why important:** Shows reasoning-driven approaches can substantially improve process reward models with minimal annotation.\n\n**15. PROGRS: LLM Reasoning with Process Rewards for Outcome-Guided Steps**\n- **Authors:** Mohammad Rezaei, Jens Lehmann, Sahar Vahdati\n- **Date:** February 2026\n- **Venue:** arXiv preprint (arXiv:2604.02341)\n- **URL:** https://arxiv.org/abs/2604.02341\n- **Summary:** Treats process rewards as relative preferences within outcome groups, using outcome-conditioned centering to remove bias while maintaining useful rankings.\n- **Why important:** Addresses the fundamental tension between process and outcome rewards with a principled alignment framework.\n\n**16. MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving**\n- **Authors:** Kuo Zhou, Lu Zhang\n- **Date:** May 2025\n- **Venue:** arXiv preprint (arXiv:2505.20869)\n- **URL:** https://arxiv.org/abs/2505.20869\n- **Summary:** Framework combining a Formalizer (natural language to formal) and Critic (CAS/SMT solvers) for training-free step-by-step verification.\n- **Why important:** Brings formal methods to step-level verification, providing provably correct judgments rather than learned heuristics.\n\n**17. HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs**\n- **Authors:** Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, Farzan Farnia\n- **Date:** November 2025\n- **Venue:** arXiv preprint (arXiv:2511.18760)\n- **URL:** https://arxiv.org/abs/2511.18760\n- **Summary:** Integrates informal LLM reasoning with Lean formal verification and intermediate checking to prevent reasoning drift; 67% accuracy improvement with 80% fewer FLOPs.\n- **Why important:** Demonstrates that formal intermediate checking during reasoning prevents drift -- a practical approach to process-level verification.\n\n**18. Let's Reward Step by Step: Step-Level Reward Model as the Navigators for Reasoning**\n- **Authors:** Qianli Ma, Haotian Zhou, Tingkai Liu, Jianbo Yuan, Pengfei Liu, Yang You, Hongxia Yang\n- **Date:** September 2023 (ICLR 2024)\n- **Venue:** ICLR 2024 (OpenReview: RSQL6xvUYW)\n- **URL:** https://openreview.net/forum?id=RSQL6xvUYW\n- **Summary:** Proposes heuristic greedy search using step-level PRM feedback, improving multi-step reasoning on GSM8K, MATH, and HumanEval.\n- **Why important:** Early work showing step-level reward models can guide search in reasoning, applicable beyond math to code generation.\n\n---\n\n### CATEGORY C: Step-Level Evaluation Benchmarks and Discrepancy Studies\n\n**19. ProcessBench: Identifying Process Errors in Mathematical Reasoning**\n- **Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin\n- **Date:** December 2024 (ACL 2025)\n- **Venue:** ACL 2025 (arXiv:2412.06559)\n- **URL:** https://arxiv.org/abs/2412.06559\n- **Summary:** 3,400 test cases requiring identification of the earliest error step in math reasoning; reveals existing PRMs struggle on challenging problems.\n- **Why important:** The primary benchmark for evaluating step-level error detection, widely used (e.g., by GenPRM).\n\n**20. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models**\n- **Authors:** Mingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, Yu Cheng\n- **Date:** January 2025 (ACL 2025 Main)\n- **Venue:** ACL 2025 (arXiv:2501.03124)\n- **URL:** https://arxiv.org/abs/2501.03124\n- **Summary:** 6,216 problems with 83,456 step-level labels evaluating PRMs across multiple dimensions (simplicity, soundness, sensitivity); reveals substantial PRM limitations.\n- **Why important:** The most comprehensive PRM evaluation benchmark to date, accepted at a top venue.\n\n**21. Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns**\n- **Authors:** Xiang Li, Haiyang Yu, Xinghua Zhang, + 6 others\n- **Date:** May 2025\n- **Venue:** arXiv preprint (arXiv:2505.23474)\n- **URL:** https://arxiv.org/abs/2505.23474\n- **Summary:** Evaluates PRMs across 6 reasoning patterns (Transformation, Decomposition, Regather, Deduction, Verification, Integration) with ~3,000 paths.\n- **Why important:** Provides pattern-specific PRM evaluation, revealing which reasoning types are hardest for current models to verify.\n\n**22. Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math**\n- **Authors:** Shrey Pandit, Austin Xu, Xuan-Phi Nguyen, Yifei Ming, Caiming Xiong, Shafiq Joty\n- **Date:** October 2025\n- **Venue:** arXiv preprint (arXiv:2510.13744)\n- **URL:** https://arxiv.org/abs/2510.13744\n- **Summary:** Human-annotated step-level verification benchmark (500+ hours of annotation) for frontier-level math; evaluates 29 verification systems.\n- **Why important:** Targets frontier-level difficulty where step verification is most needed and most challenging.\n\n**23. ReasoningMath-Plus (Unmasking Reasoning Processes)**\n- **Authors:** Xiang Zheng, Weiqi Zhai, Wei Wang, + 15 others\n- **Date:** January 2026 (revised February 2026)\n- **Venue:** arXiv preprint (arXiv:2602.00564)\n- **URL:** https://arxiv.org/abs/2602.00564\n- **Summary:** 150 problems for structural reasoning with HCRS scoring and PRM; shows process-aware scores (avg 4.36/10) are much lower than final-answer accuracy (up to 5.8/10).\n- **Why important:** Directly demonstrates the discrepancy between step-level and answer-level evaluation -- answer-only metrics overestimate reasoning.\n\n**24. ReasonEval: Evaluating Mathematical Reasoning Beyond Accuracy**\n- **Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu\n- **Date:** April 2024 (AAAI 2025 camera-ready)\n- **Venue:** AAAI 2025 (arXiv:2404.05692)\n- **URL:** https://arxiv.org/abs/2404.05692\n- **Summary:** Introduces validity and redundancy metrics for step-level reasoning quality; finds higher final-answer accuracy does not correlate with better step quality on complex problems.\n- **Why important:** Published at AAAI 2025 (same venue family). Directly demonstrates the answer-process discrepancy.\n\n**25. What Defines Good Reasoning in LLMs? Dissecting Reasoning Steps with Multi-Aspect Evaluation (CaSE)**\n- **Authors:** Heejin Do, Jaehui Hwang, Dongyoon Han, Seong Joon Oh, Sangdoo Yun\n- **Date:** October 2025\n- **Venue:** arXiv preprint (arXiv:2510.20603)\n- **URL:** https://arxiv.org/abs/2510.20603\n- **Summary:** Proposes causal stepwise evaluation (CaSE) measuring relevance and coherence per step, with expert-annotated benchmarks MRa-GSM8K and MRa-MATH.\n- **Why important:** Introduces a principled multi-aspect framework for step-level evaluation that prevents hindsight bias.\n\n**26. Right Is Not Enough: The Pitfalls of Outcome Supervision in Training LLMs for Math Reasoning**\n- **Authors:** Jiaxing Guo, Wenjie Yang, Shengzhong Zhang, + 4 others\n- **Date:** June 2025\n- **Venue:** arXiv preprint (arXiv:2506.06877)\n- **URL:** https://arxiv.org/abs/2506.06877\n- **Summary:** Introduces MathOlympiadEval showing a significant gap between answer correctness and process correctness; proposes ParaStepVerifier for step-by-step verification.\n- **Why important:** Title says it all -- directly demonstrates that outcome supervision is insufficient and step-level verification is needed.\n\n**27. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models**\n- **Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar (Apple)\n- **Date:** October 2024 (ICLR 2025)\n- **Venue:** ICLR 2025 (arXiv:2410.05229)\n- **URL:** https://arxiv.org/abs/2410.05229\n- **Summary:** Shows LLMs exhibit up to 65% accuracy drops with irrelevant clauses or changed numbers, suggesting pattern matching rather than genuine reasoning.\n- **Why important:** High-impact paper questioning whether LLMs truly reason; motivates the need for process-level evaluation over answer-level.\n\n**28. Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens**\n- **Authors:** Chengshuai Zhao, Zhen Tan, Pingchuan Ma, + 5 others\n- **Date:** August 2025 (revised May 2026)\n- **Venue:** arXiv preprint (arXiv:2508.01191)\n- **URL:** https://arxiv.org/abs/2508.01191\n- **Summary:** Shows CoT reasoning is \"a brittle mirage\" beyond training distributions -- a structured inductive bias learned from in-distribution data, not genuine reasoning.\n- **Why important:** Provides empirical evidence that CoT is distribution-dependent, challenging its use as evidence of reasoning ability.\n\n**29. Comprehension Without Competence: Architectural Limits of LLMs in Symbolic Computation and Reasoning**\n- **Authors:** Zheng Zhang\n- **Date:** July 2025 (revised November 2025)\n- **Venue:** TMLR (Transactions on Machine Learning Research), November 2025 (arXiv:2507.10624)\n- **URL:** https://arxiv.org/abs/2507.10624\n- **Summary:** Identifies \"computational split-brain syndrome\" where LLMs articulate correct principles but fail to execute them; argues failures are architectural, not knowledge-based.\n- **Why important:** Provides theoretical grounding for why step-level evaluation reveals problems that answer-level evaluation misses.\n\n**30. Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation**\n- **Authors:** Pei-Chi Pan, Yingbin Liang, Sen Lin\n- **Date:** February 2026\n- **Venue:** arXiv survey (arXiv:2602.09305)\n- **URL:** https://arxiv.org/abs/2602.09305\n- **Summary:** Comprehensive survey introducing the RARL (Reasoning-Aligned RL) framework; analyzes reward hacking, evaluation benchmark vulnerabilities, and data contamination.\n- **Why important:** A recent survey paper that organizes the entire reward modeling landscape -- useful for positioning your own contribution.\n\n---\n\n### Summary of Key Themes for Your AAAI 2026 Paper\n\n1. **CoT faithfulness is poor:** The Anthropic line of work (Lanham 2023 -> Chen 2025 -> Walden 2026) establishes that CoT reveals true reasoning factors less than 20% of the time, and models actively lie about hint usage.\n\n2. **Answer-level metrics overestimate reasoning quality:** Multiple papers (ReasonEval/AAAI 2025, ReasoningMath-Plus, Right Is Not Enough) demonstrate significant gaps between answer correctness and process correctness.\n\n3. **Process reward models are advancing but imperfect:** GenPRM (AAAI 2026), HRM, R-PRM show improvements, but benchmarks (ProcessBench, PRMBench, Hard2Verify) reveal PRMs still struggle on challenging problems.\n\n4. **LLMs may pattern-match rather than reason:** GSM-Symbolic (ICLR 2025) and \"Is CoT a Mirage?\" show CoT breaks down outside training distributions, while \"Comprehension Without Competence\" argues the limitations are architectural.\n\n5. **Unfaithful CoT undermines evaluation itself:** \"Gaming the Judge\" and FaithCoT-Bench show that unfaithful reasoning can actively manipulate LLM-based evaluators."
      }
    ],
    "totalDurationMs": 233172,
    "totalTokens": 39618,
    "totalToolUseCount": 45,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1627,
      "cache_read_input_tokens": 32009,
      "output_tokens": 5981,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1627
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5981,
          "cache_read_input_tokens": 32009,
          "cache_creation_input_tokens": 1627,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1627,
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
      "otherToolCount": 45
    }
  },
  "sourceToolAssistantUUID": "3a8ed8a3-1e30-4641-8f86-be0acf42a698",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "a48d3a11-3a86-4db3-b49f-da8f245313e0",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Tool result

_source line 32 · 2026-05-29T05:21:22.431Z_

<details><summary>↩ Tool result · `toolu_01EcAtgVcT4JMhkPK4Q2Xvyx`</summary>

```text
Now I have comprehensive data. Let me compile the final structured list.

---

Here is the structured literature survey covering best paper awards, highly-cited papers, and comprehensive evaluation frameworks from 2024--2026, organized by relevance to LLM evaluation robustness and contamination.

---

## TIER 1: BEST PAPER / OUTSTANDING PAPER AWARDS DIRECTLY ON LLM EVALUATION

### 1. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)
- **Authors:** Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Alon Albalak, Yejin Choi
- **Venue:** NeurIPS 2025 -- Best Paper Award (Datasets & Benchmarks Track, Oral)
- **URL:** https://arxiv.org/abs/2510.22954
- **Why important:** Best Paper at NeurIPS 2025 that directly addresses a fundamental failure mode in LLM evaluation: diversity collapse. Introduces INFINITY-CHAT (26K queries, 31K human annotations) for measuring open-ended generation diversity.
- **Summary:** Reveals the "Artificial Hivemind" effect where 70+ LLMs produce strikingly similar outputs both within and across model families on open-ended tasks, undermining evaluations that assume diverse model behaviors.

### 2. LLMs Get Lost In Multi-Turn Conversation
- **Authors:** Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Venue:** ICLR 2026 -- Outstanding Paper Award
- **URL:** https://arxiv.org/abs/2505.06120
- **Why important:** Outstanding Paper at ICLR 2026 exposing a critical gap in LLM evaluation -- most benchmarks use single-turn settings, masking a 39% average performance drop in multi-turn conversations.
- **Summary:** Simulates 200K+ conversations showing all top LLMs suffer severe performance degradation in multi-turn settings, with models making premature assumptions and failing to recover from wrong turns.

### 3. The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models
- **Authors:** Seungone Kim, Juyoung Suk, Ji Yong Cho, Shayne Longpre, and 28 additional authors
- **Venue:** NAACL 2025 -- Best Paper Award
- **URL:** https://arxiv.org/abs/2406.05761
- **Why important:** Best Paper at NAACL 2025 (only 1 of 2000+ submissions). Provides a principled framework for fine-grained LLM evaluation using instance-specific criteria across 77 diverse tasks.
- **Summary:** Evaluates 103 frontier LLMs across nine distinct capabilities using instance-specific evaluation criteria and LLM-as-judge, with public code, data, and results.

### 4. LiveBench: A Challenging, Contamination-Limited LLM Benchmark
- **Authors:** Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, Siddhartha Jain, Ravid Shwartz-Ziv, Neel Jain, Khalid Saifullah, Sreemanti Dey, and others including Yann LeCun, Tom Goldstein, Micah Goldblum
- **Venue:** ICLR 2025 -- Spotlight Paper
- **URL:** https://arxiv.org/abs/2406.19314 | OpenReview: https://openreview.net/forum?id=sKYHBTAxVa
- **Why important:** Spotlight at ICLR 2025. The first benchmark designed from the ground up for contamination resistance with monthly updates, objective ground-truth scoring, and no LLM judge dependency.
- **Summary:** Releases new questions monthly drawn from recent math competitions, arXiv papers, news, and datasets; top models achieve below 70% accuracy; all questions, code, and answers are public.

### 5. MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models
- **Authors:** Zhongzhan Huang, Guoming Ling, Shanshan Zhong, Hefeng Wu, Liang Lin
- **Venue:** ACL 2025 -- Outstanding Paper Award
- **URL:** https://arxiv.org/abs/2505.19959
- **Why important:** Outstanding Paper at ACL 2025. Addresses the cost and scalability problems of LLM evaluation by compressing LongBench to 4.5% of the original cost while maintaining 0.97 rank correlation.
- **Summary:** Proposes a data compression method for long-context benchmarks, reducing evaluation to 237 test samples across 21 tasks while preserving ranking fidelity across 60+ LLMs.

### 6. Measuring what Matters: Construct Validity in Large Language Model Benchmarks
- **Authors:** Andrew M. Bean, Ryan Othniel Kearns, Angelika Romanou, and 39 additional authors
- **Venue:** NeurIPS 2025 -- Datasets and Benchmarks Track
- **URL:** https://arxiv.org/abs/2511.04703
- **Why important:** Systematic review of 445 LLM benchmarks by 29 expert reviewers, providing the most comprehensive meta-analysis of LLM evaluation methodology to date. Directly relevant to evaluation robustness.
- **Summary:** Finds widespread construct validity problems in LLM benchmarks -- poorly defined phenomena, mismatched tasks, and flawed scoring metrics -- and provides eight actionable recommendations for improving benchmark design.

---

## TIER 2: AWARD-WINNING PAPERS HIGHLY RELEVANT TO LLM EVALUATION

### 7. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?
- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang
- **Venue:** NeurIPS 2025 -- Best Paper Runner-Up
- **URL:** https://arxiv.org/abs/2504.13837
- **Why important:** Runner-up for NeurIPS 2025 Best Paper. Challenges the narrative that RLVR creates new reasoning capabilities, with major implications for how we evaluate "reasoning" in LLMs.
- **Summary:** Shows that RLVR improves sampling efficiency (pass@1) but does not create fundamentally new reasoning patterns -- base models achieve higher pass@k for large k, suggesting RLVR is inference-time optimization baked into weights.

### 8. Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction
- **Authors:** Vaishnavh Nagarajan, Chen Henry Wu, Charles Ding, Aditi Raghunathan
- **Venue:** ICML 2025 -- Outstanding Paper Award
- **URL:** https://arxiv.org/abs/2504.15266
- **Why important:** Outstanding Paper at ICML 2025. Provides theoretical grounding for why LLMs fail on open-ended/creative tasks, directly relevant to understanding evaluation limitations.
- **Summary:** Designs algorithmic tasks to quantify creative limits of next-token prediction, showing that multi-token approaches (teacherless training, diffusion models) excel at diverse and original output where autoregressive models fail.

### 9. CollabLLM: From Passive Responders to Active Collaborators
- **Authors:** Shirley Wu, Michel Galley, Baolin Peng, Hao Cheng, Gavin Li, Yao Dou, Weixin Cai, James Zou, Jure Leskovec, Jianfeng Gao
- **Venue:** ICML 2025 -- Outstanding Paper Award
- **URL:** https://arxiv.org/abs/2502.00640
- **Why important:** Outstanding Paper at ICML 2025. Introduces multi-turn evaluation methodology with user studies (201 judges) measuring collaboration quality, relevant to evaluation beyond single-turn benchmarks.
- **Summary:** Introduces multiturn-aware rewards for LLM training that optimize long-term conversational outcomes, achieving 18.5% higher task performance and 17.6% improved user satisfaction.

### 10. Learning Dynamics of LLM Finetuning
- **Authors:** Yi Ren, Danica J. Sutherland
- **Venue:** ICLR 2025 -- Outstanding Paper Award
- **URL:** https://arxiv.org/abs/2407.10490
- **Why important:** Outstanding Paper at ICLR 2025 (1 of 3 from 3,704 accepted papers). Explains why finetuning can strengthen hallucinations and why DPO can degrade desired outputs -- critical for understanding evaluation artifacts.
- **Summary:** Provides a step-wise framework analyzing how training on specific examples influences predictions on others, explaining hallucination amplification during finetuning and the "squeezing effect" in off-policy DPO.

### 11. A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive
- **Authors:** Sarath Sivaprasad, Pramod Kaushik, Sahar Abdelnabi, Mario Fritz
- **Venue:** ACL 2025 -- Best Paper Award
- **URL:** https://2025.aclweb.org/program/awards/
- **Why important:** Best Paper at ACL 2025. Directly relevant to evaluation methodology -- understanding the theoretical properties of LLM response sampling affects how we interpret benchmark results.
- **Summary:** Provides theoretical framework for understanding LLM response sampling, with both descriptive and prescriptive components for how sampling strategies affect output quality.

### 12. Benchmarking LLMs' Judgments with No Gold Standard (GRE-bench)
- **Authors:** Shengwei Xu, Yuxuan Lu, Grant Schoenebeck, Yuqing Kong
- **Venue:** ICLR 2025 -- Poster
- **URL:** https://arxiv.org/abs/2411.07127
- **Why important:** Introduces GEM metric and GRE-bench, which circumvents contamination by using continuously updated research papers for evaluation, and avoids gold-standard dependency.
- **Summary:** Proposes mutual-information-based evaluation (GEM) that works without gold-standard references, enabling contamination-resistant benchmarking of subjective tasks like peer review generation.

---

## TIER 3: SURVEYS AND FRAMEWORKS ON CONTAMINATION AND EVALUATION ROBUSTNESS

### 13. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation
- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray
- **Venue:** EMNLP 2025 (Main Conference)
- **URL:** https://arxiv.org/abs/2502.17521 | ACL Anthology: https://aclanthology.org/2025.emnlp-main.511/
- **Why important:** The most comprehensive survey of the static-to-dynamic evaluation transition, published at EMNLP 2025. Proposes design principles for dynamic benchmarking and identifies limitations.
- **Summary:** Surveys static and dynamic benchmarking methods for contamination resistance, proposes optimal design principles, and maintains a living GitHub repository of methods.

### 14. A Survey on Data Contamination for Large Language Models
- **Authors:** Yuxing Cheng, Yi Chang, Yuan Wu
- **Venue:** arXiv preprint (2025)
- **URL:** https://arxiv.org/abs/2502.14425
- **Why important:** Comprehensive taxonomy of contamination types (data updating, rewriting, prevention) and detection methods (white-box, gray-box, black-box). Advocates for stricter evaluation protocols.
- **Summary:** Categorizes contamination solutions and detection approaches across varying levels of model access, providing a structured framework for understanding the contamination landscape.

### 15. LLMEval-Fair: A Large-Scale Longitudinal Study on Robust and Fair Evaluation of Large Language Models
- **Authors:** Ming Zhang, Yujiong Shen, Jingyi Deng, and 19 additional authors
- **Venue:** arXiv preprint (2025-2026)
- **URL:** https://arxiv.org/abs/2508.05452
- **Why important:** Largest longitudinal LLM evaluation study to date -- 30 months, ~60 models, 220K graduate-level questions with anti-cheating architecture achieving 90% agreement with human experts.
- **Summary:** Dynamic evaluation framework with contamination-resistant data curation revealing performance ceilings in knowledge memorization and exposing contamination vulnerabilities undetectable by static benchmarks.

### 16. Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics
- **Authors:** Pankaj Kumar, Subhankar Mishra
- **Venue:** TMLR (Transactions on Machine Learning Research)
- **URL:** https://arxiv.org/abs/2505.18658
- **Why important:** Accepted at TMLR. Comprehensive survey of LLM robustness covering vulnerability sources, mitigation approaches, and assessment tools.
- **Summary:** Examines robustness as consistent performance across varying inputs, identifies vulnerability sources (model limitations, data weaknesses, adversarial threats), and reviews mitigation strategies.

### 17. Survey on Evaluation of LLM-based Agents
- **Authors:** Asaf Yehudai, Lilach Eden, Alan Li, Guy Uziel, Yilun Zhao, Roy Bar-Haim, Arman Cohan, Michal Shmueli-Scheuer
- **Venue:** ACL 2025 Findings
- **URL:** https://arxiv.org/abs/2503.16416
- **Why important:** Covers LLM agent evaluation across five dimensions including planning, tool use, and generalist capabilities. Identifies gaps in cost-efficiency, safety, and robustness evaluation.
- **Summary:** Surveys evaluation methods for LLM-based agents, covering core capabilities, application-specific benchmarks, generalist agent assessment, and evaluation frameworks.

---

## TIER 4: CONTAMINATION DETECTION AND MITIGATION METHODS

### 18. MathArena: Evaluating LLMs on Uncontaminated Math Competitions
- **Authors:** Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev
- **Venue:** arXiv preprint (2025-2026)
- **URL:** https://arxiv.org/abs/2505.23281 | Website: https://matharena.ai/
- **Why important:** Demonstrates contamination in AIME 2024 and provides an evolving benchmark using new math competitions (7 competitions, 162 problems, 50+ models).
- **Summary:** Uses recurring math competitions for contamination-free mathematical reasoning evaluation; shows evidence of contamination in existing benchmarks and benchmarks proof-writing with IMO 2025.

### 19. How Much Can We Forget about Data Contamination?
- **Authors:** Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, Ulrike von Luxburg
- **Venue:** ICML 2025 -- Poster
- **URL:** https://openreview.net/forum?id=Pf0PaYS9KG
- **Why important:** Provides an important nuance to the contamination debate -- showing that contamination can be "forgotten" with sufficient subsequent training data, tempering some contamination concerns.
- **Summary:** Shows that even 144 repetitions of contaminated data can be forgotten if training data is scaled beyond 5x Chinchilla-optimal, suggesting many modern LLMs have naturally decontaminated through scale.

### 20. Detecting Benchmark Contamination Through Watermarking
- **Authors:** Tom Sander, Pierre Fernandez, Alain Oliviero Durmus, Saeed Mahloujifar, Chuan Guo
- **Venue:** ICLR 2026 submission
- **URL:** https://openreview.net/forum?id=WFGxFzFDmQ
- **Why important:** Proposes a proactive contamination detection method using cryptographic watermarks embedded before benchmark release, achieving p-values below 10^-5 for detecting contamination.
- **Summary:** Embeds cryptographic watermarks into benchmarks through question reformulation; detects if 1B-parameter models were trained on MMLU/ARC test data with high statistical significance.

### 21. When Benchmarks Leak: Inference-Time Decontamination for LLMs
- **Authors:** Jianzhe Chai, Yu Zhe, Jun Sakuma
- **Venue:** arXiv preprint (January 2026)
- **URL:** https://arxiv.org/abs/2601.19334
- **Why important:** Novel approach to decontamination at inference time rather than training time, using embedding-space perturbations guided by a reference model.
- **Summary:** Proposes DeconIEP framework applying bounded perturbations in embedding space during evaluation to steer models away from memorization-based shortcuts, with minimal impact on clean performance.

### 22. AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge
- **Authors:** Xiaobao Wu, Liangming Pan, Yuxi Xie, Ruiwen Zhou, Shuai Zhao, Yubo Ma, Mingzhe Du, Rui Mao, Anh Tuan Luu, William Yang Wang
- **Venue:** ACL 2025 -- Main Conference
- **URL:** https://arxiv.org/abs/2412.13670
- **Why important:** Accepted at ACL 2025 main conference. Provides a fully automated framework for constructing contamination-free benchmarks using knowledge absent from LLM training sets.
- **Summary:** Automatically constructs test samples with explicitly new knowledge absent from training sets, demonstrating that contamination exists even before model cutoff dates.

### 23. Quantifying Data Contamination in Psychometric Evaluations of LLMs
- **Authors:** Jongwook Han, Woojung Song, Jonggeun Lee, Yohan Jo
- **Venue:** EACL 2026 Findings
- **URL:** https://arxiv.org/abs/2510.07175
- **Why important:** Exposes contamination in widely-used psychological assessment tools for LLMs, showing models can memorize items and adjust responses for desired outcomes.
- **Summary:** Develops a systematic framework measuring item memorization, evaluation memorization, and target score matching across 21 models and four psychometric inventories.

### 24. Towards Contamination Resistant Benchmarks
- **Authors:** Rahmatullah Musawi, Sheng Lu
- **Venue:** arXiv preprint (May 2025)
- **URL:** https://arxiv.org/abs/2505.08389
- **Why important:** Proposes a simple but effective contamination-resistance approach using Caesar cipher transformations, revealing capability gaps when contamination is controlled.
- **Summary:** Uses Caesar cipher-based benchmarks as contamination-resistant evaluation, showing that widely-used LLMs struggle when contamination is effectively controlled.

---

## TIER 5: ADDITIONAL AWARD-WINNING PAPERS WITH INDIRECT RELEVANCE

### 25. Safety Alignment Should be Made More Than Just a Few Tokens Deep
- **Authors:** Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, Peter Henderson
- **Venue:** ICLR 2025 -- Outstanding Paper Award
- **URL:** https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/
- **Why important:** Outstanding Paper at ICLR 2025. Relevant to evaluation robustness -- demonstrates that safety alignment (which benchmarks attempt to measure) can be superficial.
- **Summary:** Shows that safety alignment can take "shortcuts" that are only a few tokens deep, meaning safety evaluations may overestimate actual robustness.

### 26. Language Models Resist Alignment: Evidence From Data Compression
- **Authors:** Jiaming Ji, Kaile Wang, Tianyi Qiu, Boyuan Chen, Jiayi Zhou, Changye Li, Hantao Lou, Juntao Dai, Yunhuai Liu, Yaodong Yang
- **Venue:** ACL 2025 -- Best Paper Award
- **URL:** https://2025.aclweb.org/program/awards/
- **Why important:** Best Paper at ACL 2025. Provides evidence that alignment may not fundamentally change model behavior, with implications for how we evaluate aligned vs. unaligned models.
- **Summary:** Uses data compression theory to show that language models resist alignment, suggesting evaluation differences between aligned and base models may be more superficial than assumed.

### 27. Superposition Yields Robust Neural Scaling
- **Authors:** Yizhou Liu, Ziming Liu, Jeff Gore
- **Venue:** NeurIPS 2025 -- Best Paper Runner-Up
- **URL:** https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/
- **Why important:** Explains why scaling laws work through representation superposition, relevant to understanding when and why benchmark improvements reflect genuine capability gains.
- **Summary:** Proposes that representation superposition (more features than dimensions) explains neural scaling laws and power-law performance improvements with scale.

---

**Total papers found: 27**
- Best Paper / Outstanding Paper awards: 12 papers (entries 1-12)
- Surveys on contamination and evaluation robustness: 5 papers (entries 13-17)
- Contamination detection/mitigation methods: 7 papers (entries 18-24)
- Indirectly relevant award winners: 3 papers (entries 25-27)

**Key venues represented:** NeurIPS 2025 (Best Paper + Runner-Ups), ICLR 2025 (Outstanding + Spotlight), ICLR 2026 (Outstanding), ICML 2025 (Outstanding), ACL 2025 (Best Paper + Outstanding), NAACL 2025 (Best Paper), EMNLP 2025, EACL 2026, TMLR.

agentId: a6204bbd91fb8bd49 (use SendMessage with to: 'a6204bbd91fb8bd49' to continue this agent)
&lt;usage>total_tokens: 49646
tool_uses: 51
duration_ms: 295919&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b228f88d-2d8f-48a1-a836-00f11d297713",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "a4471ae8-ab84-4613-8fb7-c3b5044f2459",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on LLM evaluation robustness and contamination.\n\nSearch for best paper awards, highly-cited papers, and comprehensive evaluation frameworks from 2024-2026. Execute these searches:\n\n1. WebSearch: \"best paper award NeurIPS 2025 LLM evaluation\"\n2. WebSearch: \"best paper award ICML 2025 language model\"  \n3. WebSearch: \"best paper award ICLR 2025 2026 LLM benchmark\"\n4. WebSearch: \"LiveBench MathArena dynamic benchmark LLM contamination-free 2025 2026\"\n5. WebSearch: \"LLM evaluation framework robustness contamination survey 2025 2026\"\n6. WebSearch: \"site:openreview.net LLM benchmark contamination robustness 2025 outstanding\"\n\nFor each promising paper found, use WebFetch on its arXiv page to read the abstract and understand what it does.\n\nFocus on:\n- Best paper / oral / spotlight papers related to LLM evaluation\n- Comprehensive evaluation frameworks\n- Dynamic or contamination-resistant benchmarks\n- Survey papers on LLM evaluation methodology\n\nFor each paper found, record: title, authors, venue, URL, why it's important, and a one-line summary.\n\nReturn a structured list of ALL papers found with these details.",
    "agentId": "a6204bbd91fb8bd49",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Let me compile the final structured list.\n\n---\n\nHere is the structured literature survey covering best paper awards, highly-cited papers, and comprehensive evaluation frameworks from 2024--2026, organized by relevance to LLM evaluation robustness and contamination.\n\n---\n\n## TIER 1: BEST PAPER / OUTSTANDING PAPER AWARDS DIRECTLY ON LLM EVALUATION\n\n### 1. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)\n- **Authors:** Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Alon Albalak, Yejin Choi\n- **Venue:** NeurIPS 2025 -- Best Paper Award (Datasets & Benchmarks Track, Oral)\n- **URL:** https://arxiv.org/abs/2510.22954\n- **Why important:** Best Paper at NeurIPS 2025 that directly addresses a fundamental failure mode in LLM evaluation: diversity collapse. Introduces INFINITY-CHAT (26K queries, 31K human annotations) for measuring open-ended generation diversity.\n- **Summary:** Reveals the \"Artificial Hivemind\" effect where 70+ LLMs produce strikingly similar outputs both within and across model families on open-ended tasks, undermining evaluations that assume diverse model behaviors.\n\n### 2. LLMs Get Lost In Multi-Turn Conversation\n- **Authors:** Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville\n- **Venue:** ICLR 2026 -- Outstanding Paper Award\n- **URL:** https://arxiv.org/abs/2505.06120\n- **Why important:** Outstanding Paper at ICLR 2026 exposing a critical gap in LLM evaluation -- most benchmarks use single-turn settings, masking a 39% average performance drop in multi-turn conversations.\n- **Summary:** Simulates 200K+ conversations showing all top LLMs suffer severe performance degradation in multi-turn settings, with models making premature assumptions and failing to recover from wrong turns.\n\n### 3. The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models\n- **Authors:** Seungone Kim, Juyoung Suk, Ji Yong Cho, Shayne Longpre, and 28 additional authors\n- **Venue:** NAACL 2025 -- Best Paper Award\n- **URL:** https://arxiv.org/abs/2406.05761\n- **Why important:** Best Paper at NAACL 2025 (only 1 of 2000+ submissions). Provides a principled framework for fine-grained LLM evaluation using instance-specific criteria across 77 diverse tasks.\n- **Summary:** Evaluates 103 frontier LLMs across nine distinct capabilities using instance-specific evaluation criteria and LLM-as-judge, with public code, data, and results.\n\n### 4. LiveBench: A Challenging, Contamination-Limited LLM Benchmark\n- **Authors:** Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, Siddhartha Jain, Ravid Shwartz-Ziv, Neel Jain, Khalid Saifullah, Sreemanti Dey, and others including Yann LeCun, Tom Goldstein, Micah Goldblum\n- **Venue:** ICLR 2025 -- Spotlight Paper\n- **URL:** https://arxiv.org/abs/2406.19314 | OpenReview: https://openreview.net/forum?id=sKYHBTAxVa\n- **Why important:** Spotlight at ICLR 2025. The first benchmark designed from the ground up for contamination resistance with monthly updates, objective ground-truth scoring, and no LLM judge dependency.\n- **Summary:** Releases new questions monthly drawn from recent math competitions, arXiv papers, news, and datasets; top models achieve below 70% accuracy; all questions, code, and answers are public.\n\n### 5. MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models\n- **Authors:** Zhongzhan Huang, Guoming Ling, Shanshan Zhong, Hefeng Wu, Liang Lin\n- **Venue:** ACL 2025 -- Outstanding Paper Award\n- **URL:** https://arxiv.org/abs/2505.19959\n- **Why important:** Outstanding Paper at ACL 2025. Addresses the cost and scalability problems of LLM evaluation by compressing LongBench to 4.5% of the original cost while maintaining 0.97 rank correlation.\n- **Summary:** Proposes a data compression method for long-context benchmarks, reducing evaluation to 237 test samples across 21 tasks while preserving ranking fidelity across 60+ LLMs.\n\n### 6. Measuring what Matters: Construct Validity in Large Language Model Benchmarks\n- **Authors:** Andrew M. Bean, Ryan Othniel Kearns, Angelika Romanou, and 39 additional authors\n- **Venue:** NeurIPS 2025 -- Datasets and Benchmarks Track\n- **URL:** https://arxiv.org/abs/2511.04703\n- **Why important:** Systematic review of 445 LLM benchmarks by 29 expert reviewers, providing the most comprehensive meta-analysis of LLM evaluation methodology to date. Directly relevant to evaluation robustness.\n- **Summary:** Finds widespread construct validity problems in LLM benchmarks -- poorly defined phenomena, mismatched tasks, and flawed scoring metrics -- and provides eight actionable recommendations for improving benchmark design.\n\n---\n\n## TIER 2: AWARD-WINNING PAPERS HIGHLY RELEVANT TO LLM EVALUATION\n\n### 7. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\n- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang\n- **Venue:** NeurIPS 2025 -- Best Paper Runner-Up\n- **URL:** https://arxiv.org/abs/2504.13837\n- **Why important:** Runner-up for NeurIPS 2025 Best Paper. Challenges the narrative that RLVR creates new reasoning capabilities, with major implications for how we evaluate \"reasoning\" in LLMs.\n- **Summary:** Shows that RLVR improves sampling efficiency (pass@1) but does not create fundamentally new reasoning patterns -- base models achieve higher pass@k for large k, suggesting RLVR is inference-time optimization baked into weights.\n\n### 8. Roll the dice & look before you leap: Going beyond the creative limits of next-token prediction\n- **Authors:** Vaishnavh Nagarajan, Chen Henry Wu, Charles Ding, Aditi Raghunathan\n- **Venue:** ICML 2025 -- Outstanding Paper Award\n- **URL:** https://arxiv.org/abs/2504.15266\n- **Why important:** Outstanding Paper at ICML 2025. Provides theoretical grounding for why LLMs fail on open-ended/creative tasks, directly relevant to understanding evaluation limitations.\n- **Summary:** Designs algorithmic tasks to quantify creative limits of next-token prediction, showing that multi-token approaches (teacherless training, diffusion models) excel at diverse and original output where autoregressive models fail.\n\n### 9. CollabLLM: From Passive Responders to Active Collaborators\n- **Authors:** Shirley Wu, Michel Galley, Baolin Peng, Hao Cheng, Gavin Li, Yao Dou, Weixin Cai, James Zou, Jure Leskovec, Jianfeng Gao\n- **Venue:** ICML 2025 -- Outstanding Paper Award\n- **URL:** https://arxiv.org/abs/2502.00640\n- **Why important:** Outstanding Paper at ICML 2025. Introduces multi-turn evaluation methodology with user studies (201 judges) measuring collaboration quality, relevant to evaluation beyond single-turn benchmarks.\n- **Summary:** Introduces multiturn-aware rewards for LLM training that optimize long-term conversational outcomes, achieving 18.5% higher task performance and 17.6% improved user satisfaction.\n\n### 10. Learning Dynamics of LLM Finetuning\n- **Authors:** Yi Ren, Danica J. Sutherland\n- **Venue:** ICLR 2025 -- Outstanding Paper Award\n- **URL:** https://arxiv.org/abs/2407.10490\n- **Why important:** Outstanding Paper at ICLR 2025 (1 of 3 from 3,704 accepted papers). Explains why finetuning can strengthen hallucinations and why DPO can degrade desired outputs -- critical for understanding evaluation artifacts.\n- **Summary:** Provides a step-wise framework analyzing how training on specific examples influences predictions on others, explaining hallucination amplification during finetuning and the \"squeezing effect\" in off-policy DPO.\n\n### 11. A Theory of Response Sampling in LLMs: Part Descriptive and Part Prescriptive\n- **Authors:** Sarath Sivaprasad, Pramod Kaushik, Sahar Abdelnabi, Mario Fritz\n- **Venue:** ACL 2025 -- Best Paper Award\n- **URL:** https://2025.aclweb.org/program/awards/\n- **Why important:** Best Paper at ACL 2025. Directly relevant to evaluation methodology -- understanding the theoretical properties of LLM response sampling affects how we interpret benchmark results.\n- **Summary:** Provides theoretical framework for understanding LLM response sampling, with both descriptive and prescriptive components for how sampling strategies affect output quality.\n\n### 12. Benchmarking LLMs' Judgments with No Gold Standard (GRE-bench)\n- **Authors:** Shengwei Xu, Yuxuan Lu, Grant Schoenebeck, Yuqing Kong\n- **Venue:** ICLR 2025 -- Poster\n- **URL:** https://arxiv.org/abs/2411.07127\n- **Why important:** Introduces GEM metric and GRE-bench, which circumvents contamination by using continuously updated research papers for evaluation, and avoids gold-standard dependency.\n- **Summary:** Proposes mutual-information-based evaluation (GEM) that works without gold-standard references, enabling contamination-resistant benchmarking of subjective tasks like peer review generation.\n\n---\n\n## TIER 3: SURVEYS AND FRAMEWORKS ON CONTAMINATION AND EVALUATION ROBUSTNESS\n\n### 13. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation\n- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray\n- **Venue:** EMNLP 2025 (Main Conference)\n- **URL:** https://arxiv.org/abs/2502.17521 | ACL Anthology: https://aclanthology.org/2025.emnlp-main.511/\n- **Why important:** The most comprehensive survey of the static-to-dynamic evaluation transition, published at EMNLP 2025. Proposes design principles for dynamic benchmarking and identifies limitations.\n- **Summary:** Surveys static and dynamic benchmarking methods for contamination resistance, proposes optimal design principles, and maintains a living GitHub repository of methods.\n\n### 14. A Survey on Data Contamination for Large Language Models\n- **Authors:** Yuxing Cheng, Yi Chang, Yuan Wu\n- **Venue:** arXiv preprint (2025)\n- **URL:** https://arxiv.org/abs/2502.14425\n- **Why important:** Comprehensive taxonomy of contamination types (data updating, rewriting, prevention) and detection methods (white-box, gray-box, black-box). Advocates for stricter evaluation protocols.\n- **Summary:** Categorizes contamination solutions and detection approaches across varying levels of model access, providing a structured framework for understanding the contamination landscape.\n\n### 15. LLMEval-Fair: A Large-Scale Longitudinal Study on Robust and Fair Evaluation of Large Language Models\n- **Authors:** Ming Zhang, Yujiong Shen, Jingyi Deng, and 19 additional authors\n- **Venue:** arXiv preprint (2025-2026)\n- **URL:** https://arxiv.org/abs/2508.05452\n- **Why important:** Largest longitudinal LLM evaluation study to date -- 30 months, ~60 models, 220K graduate-level questions with anti-cheating architecture achieving 90% agreement with human experts.\n- **Summary:** Dynamic evaluation framework with contamination-resistant data curation revealing performance ceilings in knowledge memorization and exposing contamination vulnerabilities undetectable by static benchmarks.\n\n### 16. Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics\n- **Authors:** Pankaj Kumar, Subhankar Mishra\n- **Venue:** TMLR (Transactions on Machine Learning Research)\n- **URL:** https://arxiv.org/abs/2505.18658\n- **Why important:** Accepted at TMLR. Comprehensive survey of LLM robustness covering vulnerability sources, mitigation approaches, and assessment tools.\n- **Summary:** Examines robustness as consistent performance across varying inputs, identifies vulnerability sources (model limitations, data weaknesses, adversarial threats), and reviews mitigation strategies.\n\n### 17. Survey on Evaluation of LLM-based Agents\n- **Authors:** Asaf Yehudai, Lilach Eden, Alan Li, Guy Uziel, Yilun Zhao, Roy Bar-Haim, Arman Cohan, Michal Shmueli-Scheuer\n- **Venue:** ACL 2025 Findings\n- **URL:** https://arxiv.org/abs/2503.16416\n- **Why important:** Covers LLM agent evaluation across five dimensions including planning, tool use, and generalist capabilities. Identifies gaps in cost-efficiency, safety, and robustness evaluation.\n- **Summary:** Surveys evaluation methods for LLM-based agents, covering core capabilities, application-specific benchmarks, generalist agent assessment, and evaluation frameworks.\n\n---\n\n## TIER 4: CONTAMINATION DETECTION AND MITIGATION METHODS\n\n### 18. MathArena: Evaluating LLMs on Uncontaminated Math Competitions\n- **Authors:** Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev\n- **Venue:** arXiv preprint (2025-2026)\n- **URL:** https://arxiv.org/abs/2505.23281 | Website: https://matharena.ai/\n- **Why important:** Demonstrates contamination in AIME 2024 and provides an evolving benchmark using new math competitions (7 competitions, 162 problems, 50+ models).\n- **Summary:** Uses recurring math competitions for contamination-free mathematical reasoning evaluation; shows evidence of contamination in existing benchmarks and benchmarks proof-writing with IMO 2025.\n\n### 19. How Much Can We Forget about Data Contamination?\n- **Authors:** Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, Ulrike von Luxburg\n- **Venue:** ICML 2025 -- Poster\n- **URL:** https://openreview.net/forum?id=Pf0PaYS9KG\n- **Why important:** Provides an important nuance to the contamination debate -- showing that contamination can be \"forgotten\" with sufficient subsequent training data, tempering some contamination concerns.\n- **Summary:** Shows that even 144 repetitions of contaminated data can be forgotten if training data is scaled beyond 5x Chinchilla-optimal, suggesting many modern LLMs have naturally decontaminated through scale.\n\n### 20. Detecting Benchmark Contamination Through Watermarking\n- **Authors:** Tom Sander, Pierre Fernandez, Alain Oliviero Durmus, Saeed Mahloujifar, Chuan Guo\n- **Venue:** ICLR 2026 submission\n- **URL:** https://openreview.net/forum?id=WFGxFzFDmQ\n- **Why important:** Proposes a proactive contamination detection method using cryptographic watermarks embedded before benchmark release, achieving p-values below 10^-5 for detecting contamination.\n- **Summary:** Embeds cryptographic watermarks into benchmarks through question reformulation; detects if 1B-parameter models were trained on MMLU/ARC test data with high statistical significance.\n\n### 21. When Benchmarks Leak: Inference-Time Decontamination for LLMs\n- **Authors:** Jianzhe Chai, Yu Zhe, Jun Sakuma\n- **Venue:** arXiv preprint (January 2026)\n- **URL:** https://arxiv.org/abs/2601.19334\n- **Why important:** Novel approach to decontamination at inference time rather than training time, using embedding-space perturbations guided by a reference model.\n- **Summary:** Proposes DeconIEP framework applying bounded perturbations in embedding space during evaluation to steer models away from memorization-based shortcuts, with minimal impact on clean performance.\n\n### 22. AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge\n- **Authors:** Xiaobao Wu, Liangming Pan, Yuxi Xie, Ruiwen Zhou, Shuai Zhao, Yubo Ma, Mingzhe Du, Rui Mao, Anh Tuan Luu, William Yang Wang\n- **Venue:** ACL 2025 -- Main Conference\n- **URL:** https://arxiv.org/abs/2412.13670\n- **Why important:** Accepted at ACL 2025 main conference. Provides a fully automated framework for constructing contamination-free benchmarks using knowledge absent from LLM training sets.\n- **Summary:** Automatically constructs test samples with explicitly new knowledge absent from training sets, demonstrating that contamination exists even before model cutoff dates.\n\n### 23. Quantifying Data Contamination in Psychometric Evaluations of LLMs\n- **Authors:** Jongwook Han, Woojung Song, Jonggeun Lee, Yohan Jo\n- **Venue:** EACL 2026 Findings\n- **URL:** https://arxiv.org/abs/2510.07175\n- **Why important:** Exposes contamination in widely-used psychological assessment tools for LLMs, showing models can memorize items and adjust responses for desired outcomes.\n- **Summary:** Develops a systematic framework measuring item memorization, evaluation memorization, and target score matching across 21 models and four psychometric inventories.\n\n### 24. Towards Contamination Resistant Benchmarks\n- **Authors:** Rahmatullah Musawi, Sheng Lu\n- **Venue:** arXiv preprint (May 2025)\n- **URL:** https://arxiv.org/abs/2505.08389\n- **Why important:** Proposes a simple but effective contamination-resistance approach using Caesar cipher transformations, revealing capability gaps when contamination is controlled.\n- **Summary:** Uses Caesar cipher-based benchmarks as contamination-resistant evaluation, showing that widely-used LLMs struggle when contamination is effectively controlled.\n\n---\n\n## TIER 5: ADDITIONAL AWARD-WINNING PAPERS WITH INDIRECT RELEVANCE\n\n### 25. Safety Alignment Should be Made More Than Just a Few Tokens Deep\n- **Authors:** Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, Peter Henderson\n- **Venue:** ICLR 2025 -- Outstanding Paper Award\n- **URL:** https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/\n- **Why important:** Outstanding Paper at ICLR 2025. Relevant to evaluation robustness -- demonstrates that safety alignment (which benchmarks attempt to measure) can be superficial.\n- **Summary:** Shows that safety alignment can take \"shortcuts\" that are only a few tokens deep, meaning safety evaluations may overestimate actual robustness.\n\n### 26. Language Models Resist Alignment: Evidence From Data Compression\n- **Authors:** Jiaming Ji, Kaile Wang, Tianyi Qiu, Boyuan Chen, Jiayi Zhou, Changye Li, Hantao Lou, Juntao Dai, Yunhuai Liu, Yaodong Yang\n- **Venue:** ACL 2025 -- Best Paper Award\n- **URL:** https://2025.aclweb.org/program/awards/\n- **Why important:** Best Paper at ACL 2025. Provides evidence that alignment may not fundamentally change model behavior, with implications for how we evaluate aligned vs. unaligned models.\n- **Summary:** Uses data compression theory to show that language models resist alignment, suggesting evaluation differences between aligned and base models may be more superficial than assumed.\n\n### 27. Superposition Yields Robust Neural Scaling\n- **Authors:** Yizhou Liu, Ziming Liu, Jeff Gore\n- **Venue:** NeurIPS 2025 -- Best Paper Runner-Up\n- **URL:** https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/\n- **Why important:** Explains why scaling laws work through representation superposition, relevant to understanding when and why benchmark improvements reflect genuine capability gains.\n- **Summary:** Proposes that representation superposition (more features than dimensions) explains neural scaling laws and power-law performance improvements with scale.\n\n---\n\n**Total papers found: 27**\n- Best Paper / Outstanding Paper awards: 12 papers (entries 1-12)\n- Surveys on contamination and evaluation robustness: 5 papers (entries 13-17)\n- Contamination detection/mitigation methods: 7 papers (entries 18-24)\n- Indirectly relevant award winners: 3 papers (entries 25-27)\n\n**Key venues represented:** NeurIPS 2025 (Best Paper + Runner-Ups), ICLR 2025 (Outstanding + Spotlight), ICLR 2026 (Outstanding), ICML 2025 (Outstanding), ACL 2025 (Best Paper + Outstanding), NAACL 2025 (Best Paper), EMNLP 2025, EACL 2026, TMLR."
      }
    ],
    "totalDurationMs": 295919,
    "totalTokens": 49646,
    "totalToolUseCount": 51,
    "usage": {
      "input_tokens": 269,
      "cache_creation_input_tokens": 1394,
      "cache_read_input_tokens": 42426,
      "output_tokens": 5557,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1394
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 269,
          "output_tokens": 5557,
          "cache_read_input_tokens": 42426,
          "cache_creation_input_tokens": 1394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1394,
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
      "otherToolCount": 51
    }
  },
  "sourceToolAssistantUUID": "b228f88d-2d8f-48a1-a836-00f11d297713",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "a4471ae8-ab84-4613-8fb7-c3b5044f2459",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Assistant

_source line 35 · 2026-05-29T05:22:22.361Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I now have comprehensive results from all five search agents. Let me synthesize the findings and select the 15 most important papers that are most relevant to the CRADE framework. Let me now verify key papers by fetching their arXiv pages to confirm details, and then compile the final JSON array.

Let me identify the top papers across all results:

**From contamination detection agent:**
1. CoDeC (Zawalski et al., ICLR 2026) - Seed paper, contamination detection backbone
2. DCR (Xu et al., EMNLP 2025) - Seed paper, closest competitor


3. On The Fragility (Kocetkov/Wang et al., 2025) - Seed paper, detection fails for reasoning models
4. CDD/TED (Dong et al., 2024) - Joint detection AND mitigation
5. How Much Can We Forget (Bordt et al., ICML 2025) - Scaling perspective on contamination
6. Detecting Benchmark Contamination Through Watermarking (Sander et al., ICLR 2026)
7. When Benchmarks Leak: DeconIEP (Chai et al., 2026) - Inference-time decontamination

**From adversarial robustness agent:**

Now looking at the robustness literature, I'm seeing GSM-Symbolic as the foundational work on symbolic perturbations, followed by MaSTer's automated variant generation approach. There's also MATH-Perturb for harder perturbations, Putnam-AXIOM for competition-level variants, RIDE combining IRT with adversarial methods, and JECS providing provable joint decontamination guarantees.

**From IRT agent:**

Starting with ATLAS as the seed paper on IRT adaptive testing, and PSN-IRT appears to be the next key work in this direction. Now I'm cataloging the process reward model papers, starting with the foundational work on verifying reasoning step-by-step, then moving through generative approaches and benchmarks designed to evaluate intermediate reasoning quality. I'm also pulling in papers on faithfulness evaluation and contamination-resistant benchmarks from the best papers category.

For my final selection, I'm focusing on papers at the intersection of contamination robustness and evaluation methodology, prioritizing those with top venue recognition. I'm starting with GSM-Symbolic as the seminal work on symbolic perturbation that questions whether LLMs truly reason, then RIDE which directly connects item response theory with adversarial robustness—exactly what CRADE aims to model jointly. tinyBenchmarks provides the foundational IRT framework for LLM evaluation, while Putnam-AXIOM demonstrates the gap between contamination and robustness through competition-level functional variants with provable correctness.

For step-level evaluation, I'm including the foundational PRM paper by Lightman et al., ProcessBench as the primary benchmark for detecting step-level errors, and GenPRM as the state-of-the-art generative approach. I'm also including papers that challenge conventional narratives—Yue et al.'s work questioning whether RL actually incentivizes reasoning, and Bordt et al.'s scaling perspective on contamination. LiveBench and metabench represent the leading contamination-resistant benchmarks and IRT compression work showing single latent factor dominance. Finally, JECS provides the statistical framework for joint decontamination across models, and FaithCoT-Bench addresses faithfulness in chain-of-thought reasoning.

Beyond those, I'm considering CDD/TED for joint detection and mitigation strategies, and MATH-Perturb for revealing memorization through hard perturbations. I should focus on papers that aren't among the seed papers the user already knows, prioritizing novel contributions that extend the research area.

Looking at the most impactful recent work, GSM-Symbolic stands out as seminal adversarial evaluation research, while RIDE bridges IRT and adversarial perturbation nicely. tinyBenchmarks provides foundational IRT methodology for LLM evaluation, and Putnam-AXIOM demonstrates functional variants at competition level. For process-level reasoning, Let's Verify Step by Step is the key PRM paper, with ProcessBench and GenPRM offering step-level benchmarking at different venues. I'm also noting Does RL Really Incentivize Reasoning as a strong NeurIPS runner-up and How Much Can We Forget from ICML 2025 as relevant recent work.

Now considering the contamination angle more carefully—LiveBench and metabench both address this from different angles at ICLR 2025, while JECS offers provable joint decontamination. FaithCoT-Bench tackles CoT faithfulness specifically, MATH-Perturb uses hard structural perturbations, and ReasonEval examines answer-process discrepancies. I should also weigh in CDD/TED for its joint detection and mitigation approach, the watermarking detection work from ICLR 2026, LEGO-IRT for multidimensional IRT, and Test of Time from ACL 2026.

Now narrowing down to my strongest 15 papers, prioritizing direct relevance to CRADE and impact: GSM-Symbolic leads as the seminal symbolic perturbation work at ICLR 2025, RIDE bridges IRT and adversarial perturbation directly, tinyBenchmarks provides foundational IRT for LLMs from ICML 2024, Putnam-AXIOM offers functional variants with provable correctness at ICML 2025, and Let's Verify Step by Step remains the seminal PRM paper from ICLR 2024.

Continuing with ProcessBench as the primary step-level benchmark from ACL 2025, GenPRM as the generative PRM approach from AAAI 2026, Does RL Really Incentivize Reasoning as a NeurIPS 2025 runner-up, How Much Can We Forget addressing scaling contamination at ICML 2025, and LiveBench as the contamination-resistant benchmark from ICLR 2025. Then metabench for IRT compression from ICLR 2025, JECS for provable joint decontamination in 2026, FaithCoT-Bench for CoT faithfulness from ICLR 2026, MATH-Perturb for hard structural perturbations in 2025, and ReasonEval for answer-process discrepancy from AAAI 2025.

I should double-check the papers I'm least confident about—RIDE, JECS, and a few others—to verify they actually exist and match my descriptions.

Actually, the verification is already done. Now I'm deciding whether to include the seed papers or focus entirely on new ones. Since the user already has detailed notes on those 7 seed papers, it makes more sense to present 15 fresh papers they might not have encountered yet, ordered by how directly they relate to CRADE.

Starting with RIDE at the top since it combines IRT with adversarial perturbation—exactly what CRADE is about. Then GSM-Symbolic as the foundational symbolic perturbation work from ICLR 2025, tinyBenchmarks for IRT applied to LLMs from ICML 2024, and Putnam as the next critical paper.

The list continues through ProcessBench for step-level error detection, GenPRM for generative process reward models, the seminal "Let's Verify Step by Step" PRM paper, and several others covering faithfulness, contamination, and reasoning evaluation. I'm also weighing whether to add a few more highly relevant papers like CDD/TED for joint detection and mitigation, or LaRT for combining IRT with chain-of-thought, but 15 feels like a solid, focused set.

Since the user wants at least 15 with more being better if genuinely relevant, I should expand to around 18 papers to give comprehensive coverage. Let me double-check a few of these to make sure I'm citing them accurately before finalizing the list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4471ae8-ab84-4613-8fb7-c3b5044f2459",
  "isSidechain": false,
  "requestId": "req_011CbWJH4pDdvPagwo375nG1",
  "type": "assistant",
  "uuid": "097be958-0bb6-47b0-82be-93e982b08ca6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NL8YGuhuw2QXfheUKXjhKy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31529,
      "cache_read_input_tokens": 16844,
      "output_tokens": 4018,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4018,
          "cache_read_input_tokens": 16844,
          "cache_creation_input_tokens": 31529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31529
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

_source line 36 · 2026-05-29T05:22:22.608Z_

Now let me verify key papers that sit at the critical intersection of the research areas, and fetch a few more targeted searches for papers I may have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "097be958-0bb6-47b0-82be-93e982b08ca6",
  "isSidechain": false,
  "requestId": "req_011CbWJH4pDdvPagwo375nG1",
  "type": "assistant",
  "uuid": "dc71d0c8-f302-4619-afec-66f2f0d79a19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NL8YGuhuw2QXfheUKXjhKy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31529,
      "cache_read_input_tokens": 16844,
      "output_tokens": 4018,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4018,
          "cache_read_input_tokens": 16844,
          "cache_creation_input_tokens": 31529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31529
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

_source line 37 · 2026-05-29T05:22:22.815Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DwsvF5g2sKUSfY3VWeaMpd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.04120",
  "prompt": "Extract the full title, authors, date, and abstract of this paper (RIDE). Is this about combining IRT with adversarial perturbation for math reasoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc71d0c8-f302-4619-afec-66f2f0d79a19",
  "isSidechain": false,
  "requestId": "req_011CbWJH4pDdvPagwo375nG1",
  "type": "assistant",
  "uuid": "c31c12d1-52a6-4aa3-aab3-738f6be3ebae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NL8YGuhuw2QXfheUKXjhKy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31529,
      "cache_read_input_tokens": 16844,
      "output_tokens": 4018,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4018,
          "cache_read_input_tokens": 16844,
          "cache_creation_input_tokens": 31529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31529
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

_source line 38 · 2026-05-29T05:22:23.918Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019gkvSZR8wVW6RXCj2Yv593`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.21543",
  "prompt": "Extract the full title, authors, date, and abstract of this paper (JECS). Is this about provable joint decontamination across multiple LLMs using conformal p-values?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c31c12d1-52a6-4aa3-aab3-738f6be3ebae",
  "isSidechain": false,
  "requestId": "req_011CbWJH4pDdvPagwo375nG1",
  "type": "assistant",
  "uuid": "21c0d410-a67b-40e7-a84a-8afea6996301",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NL8YGuhuw2QXfheUKXjhKy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31529,
      "cache_read_input_tokens": 16844,
      "output_tokens": 4018,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4018,
          "cache_read_input_tokens": 16844,
          "cache_creation_input_tokens": 31529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31529
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

_source line 39 · 2026-05-29T05:22:24.825Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CorJ9j9Q9acySi5YzHVDKe`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.13837",
  "prompt": "Extract the full title, authors, date, and abstract of this paper. Is this about whether reinforcement learning truly incentivizes reasoning in LLMs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21c0d410-a67b-40e7-a84a-8afea6996301",
  "isSidechain": false,
  "requestId": "req_011CbWJH4pDdvPagwo375nG1",
  "type": "assistant",
  "uuid": "f0db29da-62d2-474b-a5fd-75349bd5f7f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NL8YGuhuw2QXfheUKXjhKy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31529,
      "cache_read_input_tokens": 16844,
      "output_tokens": 4018,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4018,
          "cache_read_input_tokens": 16844,
          "cache_creation_input_tokens": 31529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31529
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

_source line 40 · 2026-05-29T05:22:25.855Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014z9dyQKadE3XqyTfJRBEL9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.05229",
  "prompt": "Extract the full title, authors, date, and abstract. Is this GSM-Symbolic about symbolic templates showing LLMs fail on perturbed math problems?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0db29da-62d2-474b-a5fd-75349bd5f7f7",
  "isSidechain": false,
  "requestId": "req_011CbWJH4pDdvPagwo375nG1",
  "type": "assistant",
  "uuid": "08a37a06-1499-45e2-9d5a-71704243244f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NL8YGuhuw2QXfheUKXjhKy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31529,
      "cache_read_input_tokens": 16844,
      "output_tokens": 4018,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 31529,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4018,
          "cache_read_input_tokens": 16844,
          "cache_creation_input_tokens": 31529,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 31529
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

_source line 41 · 2026-05-29T05:22:27.140Z_

<details><summary>↩ Tool result · `toolu_01DwsvF5g2sKUSfY3VWeaMpd`</summary>

```text
# RIDE Paper Summary

**Full Title:** "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning"

**Authors:** Xinyuan Li, Murong Xu, Wenbiao Tao, Hanlun Zhu, Yike Zhao, Jipeng Zhang, and Yunshi Lan

**Date:** Submitted November 6, 2025 (revised January 31, 2026)

**Abstract Summary:**
The researchers developed a framework that combines Item Response Theory with adversarial question modification techniques. According to the abstract, the method "leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical problems."

**Does it combine IRT with adversarial perturbation?** Yes, precisely. The work uses 35 language models to evaluate difficulty levels, then employs reinforcement learning to guide rewrites of math problems across varying challenge tiers. Testing showed an approximate 21.73% performance reduction across 26 models, revealing weaknesses in their mathematical reasoning robustness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c31c12d1-52a6-4aa3-aab3-738f6be3ebae",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "c6131c17-21bf-46b6-b49d-fe80031bf77d",
  "toolUseResult": {
    "bytes": 47129,
    "code": 200,
    "codeText": "OK",
    "result": "# RIDE Paper Summary\n\n**Full Title:** \"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning\"\n\n**Authors:** Xinyuan Li, Murong Xu, Wenbiao Tao, Hanlun Zhu, Yike Zhao, Jipeng Zhang, and Yunshi Lan\n\n**Date:** Submitted November 6, 2025 (revised January 31, 2026)\n\n**Abstract Summary:**\nThe researchers developed a framework that combines Item Response Theory with adversarial question modification techniques. According to the abstract, the method \"leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical problems.\"\n\n**Does it combine IRT with adversarial perturbation?** Yes, precisely. The work uses 35 language models to evaluate difficulty levels, then employs reinforcement learning to guide rewrites of math problems across varying challenge tiers. Testing showed an approximate 21.73% performance reduction across 26 models, revealing weaknesses in their mathematical reasoning robustness.",
    "durationMs": 4319,
    "url": "https://arxiv.org/abs/2511.04120"
  },
  "sourceToolAssistantUUID": "c31c12d1-52a6-4aa3-aab3-738f6be3ebae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "c6131c17-21bf-46b6-b49d-fe80031bf77d",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Tool result

_source line 44 · 2026-05-29T05:22:28.017Z_

<details><summary>↩ Tool result · `toolu_019gkvSZR8wVW6RXCj2Yv593`</summary>

```text
# Paper Summary: JECS

**Full Title:** "Provable Joint Decontamination for Benchmarking Multiple Large Language Models"

**Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei

**Submission Date:** May 20, 2026

**Abstract Overview:**

Yes, your understanding is accurate. The paper addresses benchmark contamination in LLM evaluation by proposing Joint Envelope Conformal Selection (JECS). 

The core innovation involves using conformal methodology to enable "global contamination rate (GCR) control." The approach computes "per-model conformal p-values, aggregates them by the per-item maximum," then reconstructs a conservative statistical envelope from tail observations. The adaptive Benjamini-Hochberg procedure is applied to rescaled values to select a decontaminated benchmark.

The key distinction from prior work is that JECS operates as a unified joint selection process rather than applying conformal procedures separately to each model, thereby preserving fair cross-model comparisons while maintaining theoretical guarantees on contamination control.

**Field:** Machine Learning (cs.LG)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21c0d410-a67b-40e7-a84a-8afea6996301",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "66669550-8895-4dcc-8c9b-98aaf7cd2767",
  "toolUseResult": {
    "bytes": 47172,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: JECS\n\n**Full Title:** \"Provable Joint Decontamination for Benchmarking Multiple Large Language Models\"\n\n**Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei\n\n**Submission Date:** May 20, 2026\n\n**Abstract Overview:**\n\nYes, your understanding is accurate. The paper addresses benchmark contamination in LLM evaluation by proposing Joint Envelope Conformal Selection (JECS). \n\nThe core innovation involves using conformal methodology to enable \"global contamination rate (GCR) control.\" The approach computes \"per-model conformal p-values, aggregates them by the per-item maximum,\" then reconstructs a conservative statistical envelope from tail observations. The adaptive Benjamini-Hochberg procedure is applied to rescaled values to select a decontaminated benchmark.\n\nThe key distinction from prior work is that JECS operates as a unified joint selection process rather than applying conformal procedures separately to each model, thereby preserving fair cross-model comparisons while maintaining theoretical guarantees on contamination control.\n\n**Field:** Machine Learning (cs.LG)",
    "durationMs": 4095,
    "url": "https://arxiv.org/abs/2605.21543"
  },
  "sourceToolAssistantUUID": "21c0d410-a67b-40e7-a84a-8afea6996301",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-29T05:22:29.664Z_

<details><summary>↩ Tool result · `toolu_01CorJ9j9Q9acySi5YzHVDKe`</summary>

```text
# Paper Information

**Title:** "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"

**Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang

**Date:** Submitted April 18, 2025; last revised November 24, 2025

**Abstract Summary:**
The paper investigates whether Reinforcement Learning with Verifiable Rewards (RLVR) genuinely develops new reasoning abilities in language models. The researchers found that "the current training setup does not elicit fundamentally new reasoning patterns." While RLVR models performed better at small sample sizes, base models achieved higher scores at larger k values. The analysis indicates that reasoning abilities remain bounded by the base model's capabilities, with current RLVR algorithms performing far below optimal levels.

## Answer to Your Question

Yes, this paper directly addresses whether reinforcement learning truly incentivizes reasoning in LLMs. However, the findings suggest it does **not** enable genuinely novel reasoning beyond base model capabilities—challenging the prevailing assumption about RL's potential in this domain.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0db29da-62d2-474b-a5fd-75349bd5f7f7",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "46c53b1b-0ee6-4686-8bad-18e145e094c4",
  "toolUseResult": {
    "bytes": 48797,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Information\n\n**Title:** \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\"\n\n**Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang\n\n**Date:** Submitted April 18, 2025; last revised November 24, 2025\n\n**Abstract Summary:**\nThe paper investigates whether Reinforcement Learning with Verifiable Rewards (RLVR) genuinely develops new reasoning abilities in language models. The researchers found that \"the current training setup does not elicit fundamentally new reasoning patterns.\" While RLVR models performed better at small sample sizes, base models achieved higher scores at larger k values. The analysis indicates that reasoning abilities remain bounded by the base model's capabilities, with current RLVR algorithms performing far below optimal levels.\n\n## Answer to Your Question\n\nYes, this paper directly addresses whether reinforcement learning truly incentivizes reasoning in LLMs. However, the findings suggest it does **not** enable genuinely novel reasoning beyond base model capabilities—challenging the prevailing assumption about RL's potential in this domain.",
    "durationMs": 4838,
    "url": "https://arxiv.org/abs/2504.13837"
  },
  "sourceToolAssistantUUID": "f0db29da-62d2-474b-a5fd-75349bd5f7f7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-29T05:22:30.109Z_

<details><summary>↩ Tool result · `toolu_014z9dyQKadE3XqyTfJRBEL9`</summary>

```text
# GSM-Symbolic Paper Information

**Full Title:** GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

**Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar

**Date:** Submitted October 7, 2024; revised August 27, 2025

**Abstract Summary:**
The paper introduces GSM-Symbolic, a benchmark built from "symbolic templates that allow for the generation of a diverse set of questions." The research reveals that when numerical values change in identical problem structures, LLM performance drops noticeably. Additionally, the study finds that "adding a single clause that seems relevant to the question causes significant performance drops (up to 65%)" even when the clause is unnecessary for solving the problem.

**Your Question:** Yes, this paper is fundamentally about that topic. It demonstrates that LLMs show "noticeable variance when responding to different instantiations of the same question" and suggests models struggle with genuine logical reasoning rather than pattern matching from training data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08a37a06-1499-45e2-9d5a-71704243244f",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "cc397d37-5a10-44ce-87e6-872c5a0592bb",
  "toolUseResult": {
    "bytes": 50143,
    "code": 200,
    "codeText": "OK",
    "result": "# GSM-Symbolic Paper Information\n\n**Full Title:** GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\n\n**Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar\n\n**Date:** Submitted October 7, 2024; revised August 27, 2025\n\n**Abstract Summary:**\nThe paper introduces GSM-Symbolic, a benchmark built from \"symbolic templates that allow for the generation of a diverse set of questions.\" The research reveals that when numerical values change in identical problem structures, LLM performance drops noticeably. Additionally, the study finds that \"adding a single clause that seems relevant to the question causes significant performance drops (up to 65%)\" even when the clause is unnecessary for solving the problem.\n\n**Your Question:** Yes, this paper is fundamentally about that topic. It demonstrates that LLMs show \"noticeable variance when responding to different instantiations of the same question\" and suggests models struggle with genuine logical reasoning rather than pattern matching from training data.",
    "durationMs": 4251,
    "url": "https://arxiv.org/abs/2410.05229"
  },
  "sourceToolAssistantUUID": "08a37a06-1499-45e2-9d5a-71704243244f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47 · 2026-05-29T05:22:30.115Z_

```json
{
  "parentUuid": "cc397d37-5a10-44ce-87e6-872c5a0592bb",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "9dcf7db4-c382-4c0d-81e0-2c5d0562d57b",
  "timestamp": "2026-05-29T05:22:30.115Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 48 · 2026-05-29T05:22:33.314Z_

<details><summary>Logged reasoning block</summary>

```text
Great, the papers I verified check out. Let me now do a couple more targeted searches to make sure I haven't missed anything critical, especially at the intersection of these areas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9dcf7db4-c382-4c0d-81e0-2c5d0562d57b",
  "isSidechain": false,
  "requestId": "req_011CbWJN48Rxk9TqQd1p46bf",
  "type": "assistant",
  "uuid": "3a7d2dcd-e3ea-40b1-b705-1bc9ea53c630",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4AKn8XqAZfFuUUZFb74gH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5249,
      "cache_read_input_tokens": 48373,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 48373,
          "cache_creation_input_tokens": 5249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5249
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

_source line 49 · 2026-05-29T05:22:33.315Z_

Let me do a few more targeted searches to ensure I haven't missed critical papers at the intersection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a7d2dcd-e3ea-40b1-b705-1bc9ea53c630",
  "isSidechain": false,
  "requestId": "req_011CbWJN48Rxk9TqQd1p46bf",
  "type": "assistant",
  "uuid": "0be9d378-a732-4002-9c99-6066db38e34c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4AKn8XqAZfFuUUZFb74gH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5249,
      "cache_read_input_tokens": 48373,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 48373,
          "cache_creation_input_tokens": 5249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5249
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

_source line 50 · 2026-05-29T05:22:36.044Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JEx4Av6H8ZhujzgD1htGYh`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.08292",
  "prompt": "Extract the full title, authors, date, and abstract of this paper (Putnam-AXIOM). What exactly does it do with functional variants?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0be9d378-a732-4002-9c99-6066db38e34c",
  "isSidechain": false,
  "requestId": "req_011CbWJN48Rxk9TqQd1p46bf",
  "type": "assistant",
  "uuid": "78c38352-de9b-4cf4-b8e1-3ded0744f0fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4AKn8XqAZfFuUUZFb74gH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5249,
      "cache_read_input_tokens": 48373,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 48373,
          "cache_creation_input_tokens": 5249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5249
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

_source line 51 · 2026-05-29T05:22:36.200Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NqWS4k8LcDDnbubptR8prR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.00891",
  "prompt": "Extract the full title, authors, date, and abstract of this paper (GenPRM). Is this about generative process reward models? What venue is it published at?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78c38352-de9b-4cf4-b8e1-3ded0744f0fa",
  "isSidechain": false,
  "requestId": "req_011CbWJN48Rxk9TqQd1p46bf",
  "type": "assistant",
  "uuid": "ac5bfdf3-8583-4191-9d2c-ebc1732e1411",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4AKn8XqAZfFuUUZFb74gH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5249,
      "cache_read_input_tokens": 48373,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 48373,
          "cache_creation_input_tokens": 5249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5249
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

_source line 52 · 2026-05-29T05:22:36.670Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K46dRHZYgg5RkWSvQPujss`</summary>

```json
{
  "query": "contamination-aware IRT ability estimation LLM benchmark joint modeling 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac5bfdf3-8583-4191-9d2c-ebc1732e1411",
  "isSidechain": false,
  "requestId": "req_011CbWJN48Rxk9TqQd1p46bf",
  "type": "assistant",
  "uuid": "e5390ea6-5cf8-4e9f-ba0f-9fd394c6c574",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4AKn8XqAZfFuUUZFb74gH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5249,
      "cache_read_input_tokens": 48373,
      "output_tokens": 340,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 340,
          "cache_read_input_tokens": 48373,
          "cache_creation_input_tokens": 5249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5249
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

_source line 53 · 2026-05-29T05:22:40.656Z_

<details><summary>↩ Tool result · `toolu_01NqWS4k8LcDDnbubptR8prR`</summary>

```text
# GenPRM Paper Summary

**Full Title:** "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning"

**Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, and Bowen Zhou

**Submission Date:** April 1, 2025 (revised April 5, 2025)

**Is it about generative process reward models?** Yes. The paper introduces GenPRM, which performs "explicit Chain-of-Thought reasoning with code verification before providing judgment for each reasoning step."

**Venue:** This is an arXiv preprint (arXiv:2504.00891) in the Computer Science > Computation and Language category. The abstract indicates it has not yet been published at a traditional conference or journal venue—it appears to be a recent preprint submission.

**Key Innovation:** The work bridges process reward models and critic models by enabling test-time scaling, where a 1.5B parameter GenPRM reportedly outperforms GPT-4o on ProcessBench evaluation tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac5bfdf3-8583-4191-9d2c-ebc1732e1411",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "bae2c330-e21a-47d3-a89c-514b630461dd",
  "toolUseResult": {
    "bytes": 47432,
    "code": 200,
    "codeText": "OK",
    "result": "# GenPRM Paper Summary\n\n**Full Title:** \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\"\n\n**Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, Zhimu Zhou, Junqi Gao, Dong Li, Jiafei Lyu, Zhouyi Qian, Biqing Qi, Xiu Li, and Bowen Zhou\n\n**Submission Date:** April 1, 2025 (revised April 5, 2025)\n\n**Is it about generative process reward models?** Yes. The paper introduces GenPRM, which performs \"explicit Chain-of-Thought reasoning with code verification before providing judgment for each reasoning step.\"\n\n**Venue:** This is an arXiv preprint (arXiv:2504.00891) in the Computer Science > Computation and Language category. The abstract indicates it has not yet been published at a traditional conference or journal venue—it appears to be a recent preprint submission.\n\n**Key Innovation:** The work bridges process reward models and critic models by enabling test-time scaling, where a 1.5B parameter GenPRM reportedly outperforms GPT-4o on ProcessBench evaluation tasks.",
    "durationMs": 4451,
    "url": "https://arxiv.org/abs/2504.00891"
  },
  "sourceToolAssistantUUID": "ac5bfdf3-8583-4191-9d2c-ebc1732e1411",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-29T05:22:40.972Z_

<details><summary>↩ Tool result · `toolu_01JEx4Av6H8ZhujzgD1htGYh`</summary>

```text
# Putnam-AXIOM Paper Summary

**Full Title:** "Putnam-AXIOM: A Functional and Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs"

**Authors:** Aryan Gulati, Brando Miranda, Eric Chen, Emily Xia, Kai Fronsdal, Bruno Dumont, Elyas Obbad, and Sanmi Koyejo

**Date:** Submitted August 5, 2025 (revised August 27, 2025)

**Abstract Overview:**
The benchmark addresses saturation in current mathematical reasoning tests by introducing 522 university-level problems from the Putnam Mathematical Competition, plus 100 functional variants. The abstract states: "The variation protocol produces an unlimited stream of equally difficult, unseen instances -- yielding a contamination-resilient test bed."

**Functional Variants Approach:**
The researchers generate variants through "programmatically perturbing variables and constants" in original problems. This method serves multiple purposes: it creates fresh test instances that circumvent training-set contamination, maintains consistent difficulty levels, and reveals memorization patterns. The results showed OpenAI's o1-preview's accuracy dropped significantly (from 41.9% to 22.3%) on variants, suggesting models may rely on memorized solutions rather than genuine reasoning capabilities.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "78c38352-de9b-4cf4-b8e1-3ded0744f0fa",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "d628337c-3829-4d73-814d-cf9352bc07a2",
  "toolUseResult": {
    "bytes": 49420,
    "code": 200,
    "codeText": "OK",
    "result": "# Putnam-AXIOM Paper Summary\n\n**Full Title:** \"Putnam-AXIOM: A Functional and Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs\"\n\n**Authors:** Aryan Gulati, Brando Miranda, Eric Chen, Emily Xia, Kai Fronsdal, Bruno Dumont, Elyas Obbad, and Sanmi Koyejo\n\n**Date:** Submitted August 5, 2025 (revised August 27, 2025)\n\n**Abstract Overview:**\nThe benchmark addresses saturation in current mathematical reasoning tests by introducing 522 university-level problems from the Putnam Mathematical Competition, plus 100 functional variants. The abstract states: \"The variation protocol produces an unlimited stream of equally difficult, unseen instances -- yielding a contamination-resilient test bed.\"\n\n**Functional Variants Approach:**\nThe researchers generate variants through \"programmatically perturbing variables and constants\" in original problems. This method serves multiple purposes: it creates fresh test instances that circumvent training-set contamination, maintains consistent difficulty levels, and reveals memorization patterns. The results showed OpenAI's o1-preview's accuracy dropped significantly (from 41.9% to 22.3%) on variants, suggesting models may rely on memorized solutions rather than genuine reasoning capabilities.",
    "durationMs": 4924,
    "url": "https://arxiv.org/abs/2508.08292"
  },
  "sourceToolAssistantUUID": "78c38352-de9b-4cf4-b8e1-3ded0744f0fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-29T05:22:44.501Z_

<details><summary>↩ Tool result · `toolu_01K46dRHZYgg5RkWSvQPujss`</summary>

```text
Web search results for query: "contamination-aware IRT ability estimation LLM benchmark joint modeling 2025 2026"

Links: [{"title":"Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/html/2605.21543"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"Contamination Report for Multilingual Benchmarks","url":"https://arxiv.org/pdf/2410.16186"},{"title":"Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination","url":"https://arxiv.org/pdf/2509.00072"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2602.12424"},{"title":"livebench:achallenging, contamination-limited llm benchmark","url":"https://arxiv.org/pdf/2406.19314"},{"title":"How Can I Publish My LLM Benchmark Without Giving the True Answers Away?","url":"https://arxiv.org/pdf/2505.18102"},{"title":"LiveBench: A Challenging, Contamination-Limited LLM Benchmark | OpenReview","url":"https://openreview.net/forum?id=sKYHBTAxVa"},{"title":"Soft Contamination Means Benchmarks Test Shallow Generalization","url":"https://arxiv.org/pdf/2602.12413"}]

I found relevant research on this topic. Here are the search results:

## Key Findings:

**IRT-Based LLM Benchmarking:**

A recent paper provides critical analysis of LLM benchmark effectiveness using Item Response Theory, proposing Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced IRT framework that incorporates a rich set of item parameters within an IRT-grounded architecture. The analysis covers 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.

**Contamination-Aware Approaches:**

In practical benchmark evaluation, auditors require a shared decontaminated benchmark that supports fair assessment across multiple models, motivating the development of methods for selecting one shared benchmark with a controlled contamination rate across all audited models. Recent work leverages conformal inference to identify training data for a single model with provable false-identification control.

**Joint Modeling and Benchmark Contamination:**

If an LLM has seen the questions of a benchmark during training, its performance on that benchmark will be artificially inflated (referred to as "test set contamination"), making many LLM benchmarks unreliable. Several approaches address this through dynamic benchmark construction and contamination-free curation methods to improve reliability of LLM ability estimation.

The research appears to be emerging in 2025-2026 with increased focus on integrating contamination awareness into IRT-based ability estimation frameworks for fairer LLM benchmarking.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e5390ea6-5cf8-4e9f-ba0f-9fd394c6c574",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "ee58a626-845a-46b0-be51-395aa6d9ec50",
  "toolUseResult": {
    "query": "contamination-aware IRT ability estimation LLM benchmark joint modeling 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012YsusUQRPvvGyVMm3psb1V",
        "content": [
          {
            "title": "Provable Joint Decontamination for Benchmarking Multiple Large Language Models",
            "url": "https://arxiv.org/html/2605.21543"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v3"
          },
          {
            "title": "Contamination Report for Multilingual Benchmarks",
            "url": "https://arxiv.org/pdf/2410.16186"
          },
          {
            "title": "Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination",
            "url": "https://arxiv.org/pdf/2509.00072"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2602.12424"
          },
          {
            "title": "livebench:achallenging, contamination-limited llm benchmark",
            "url": "https://arxiv.org/pdf/2406.19314"
          },
          {
            "title": "How Can I Publish My LLM Benchmark Without Giving the True Answers Away?",
            "url": "https://arxiv.org/pdf/2505.18102"
          },
          {
            "title": "LiveBench: A Challenging, Contamination-Limited LLM Benchmark | OpenReview",
            "url": "https://openreview.net/forum?id=sKYHBTAxVa"
          },
          {
            "title": "Soft Contamination Means Benchmarks Test Shallow Generalization",
            "url": "https://arxiv.org/pdf/2602.12413"
          }
        ]
      },
      "I found relevant research on this topic. Here are the search results:\n\n## Key Findings:\n\n**IRT-Based LLM Benchmarking:**\n\nA recent paper provides critical analysis of LLM benchmark effectiveness using Item Response Theory, proposing Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced IRT framework that incorporates a rich set of item parameters within an IRT-grounded architecture. The analysis covers 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality.\n\n**Contamination-Aware Approaches:**\n\nIn practical benchmark evaluation, auditors require a shared decontaminated benchmark that supports fair assessment across multiple models, motivating the development of methods for selecting one shared benchmark with a controlled contamination rate across all audited models. Recent work leverages conformal inference to identify training data for a single model with provable false-identification control.\n\n**Joint Modeling and Benchmark Contamination:**\n\nIf an LLM has seen the questions of a benchmark during training, its performance on that benchmark will be artificially inflated (referred to as \"test set contamination\"), making many LLM benchmarks unreliable. Several approaches address this through dynamic benchmark construction and contamination-free curation methods to improve reliability of LLM ability estimation.\n\nThe research appears to be emerging in 2025-2026 with increased focus on integrating contamination awareness into IRT-based ability estimation frameworks for fairer LLM benchmarking."
    ],
    "durationSeconds": 7.82771102399996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e5390ea6-5cf8-4e9f-ba0f-9fd394c6c574",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-29T05:22:47.667Z_

<details><summary>Logged reasoning block</summary>

```text
Let me check a couple more papers that seem very relevant - the "Soft Contamination" paper and the ICLR 2026 paper that appeared in the search.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee58a626-845a-46b0-be51-395aa6d9ec50",
  "isSidechain": false,
  "requestId": "req_011CbWJP7fnNw1SVobJGkFYc",
  "type": "assistant",
  "uuid": "fb35eefb-4c4d-465a-9ea7-73b266c3bda9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxxTsqvaxTHyrsDsorQxNG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 53622,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 53622,
          "cache_creation_input_tokens": 1752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1752
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

_source line 57 · 2026-05-29T05:22:48.609Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HNWKVBvTCLgaiK8NLaigpb`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.12413",
  "prompt": "Extract the full title, authors, date, and abstract. What does this paper about \"soft contamination\" argue about benchmarks and shallow generalization?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb35eefb-4c4d-465a-9ea7-73b266c3bda9",
  "isSidechain": false,
  "requestId": "req_011CbWJP7fnNw1SVobJGkFYc",
  "type": "assistant",
  "uuid": "b6b4258f-5e39-469a-9282-1910c9d797a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxxTsqvaxTHyrsDsorQxNG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 53622,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 53622,
          "cache_creation_input_tokens": 1752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1752
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

_source line 58 · 2026-05-29T05:22:50.035Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01CqghDdKkGGzFAoZPfd95Rx`</summary>

```json
{
  "url": "https://arxiv.org/abs/2402.15938",
  "prompt": "Extract the full title, authors, date, and abstract. This should be about CDD (contamination detection) and TED (trustworthy evaluation) - a paper that jointly detects and mitigates contamination."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b4258f-5e39-469a-9282-1910c9d797a5",
  "isSidechain": false,
  "requestId": "req_011CbWJP7fnNw1SVobJGkFYc",
  "type": "assistant",
  "uuid": "b84fbc4f-2b26-43b4-9b5c-3956f8288774",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxxTsqvaxTHyrsDsorQxNG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1752,
      "cache_read_input_tokens": 53622,
      "output_tokens": 276,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 276,
          "cache_read_input_tokens": 53622,
          "cache_creation_input_tokens": 1752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1752
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

_source line 59_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "b84fbc4f-2b26-43b4-9b5c-3956f8288774",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 60_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Tool result

_source line 61 · 2026-05-29T05:22:53.912Z_

<details><summary>↩ Tool result · `toolu_01HNWKVBvTCLgaiK8NLaigpb`</summary>

```text
# Paper Summary: Soft Contamination and Benchmark Validity

**Full Title:** Soft Contamination Means Benchmarks Test Shallow Generalization

**Authors:** Ari Spiesberger, Juan J. Vazquez, Nicky Pochinkov, Tomáš Gavenčiak, Peli Grietzer, Gavin Leech, Nandi Schoots

**Date:** Submitted February 12, 2026

## Abstract

The paper examines how semantic duplicates of benchmark test data in training corpora—which escape detection by standard n-gram matching filters—distort performance evaluations. After analyzing the Olmo3 training corpus, researchers discovered that "contamination remains widespread" with semantic duplicates present for 78% of CodeForces problems and exact duplicates in 50% of ZebraLogic problems.

## Key Argument

The authors contend that reported benchmark improvements conflate genuine capability gains with data leakage. They demonstrate that training on semantic duplicates of benchmark data improves performance both on those benchmarks and on truly held-out datapoints from the same benchmark. This indicates benchmark gains "reflect both genuine capability improvements and the accumulation of test data" in expanding training corpora, undermining claims about true out-of-distribution generalization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6b4258f-5e39-469a-9282-1910c9d797a5",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "5a4a52e7-c830-4b88-9ba2-029bef9b290e",
  "toolUseResult": {
    "bytes": 47034,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Soft Contamination and Benchmark Validity\n\n**Full Title:** Soft Contamination Means Benchmarks Test Shallow Generalization\n\n**Authors:** Ari Spiesberger, Juan J. Vazquez, Nicky Pochinkov, Tomáš Gavenčiak, Peli Grietzer, Gavin Leech, Nandi Schoots\n\n**Date:** Submitted February 12, 2026\n\n## Abstract\n\nThe paper examines how semantic duplicates of benchmark test data in training corpora—which escape detection by standard n-gram matching filters—distort performance evaluations. After analyzing the Olmo3 training corpus, researchers discovered that \"contamination remains widespread\" with semantic duplicates present for 78% of CodeForces problems and exact duplicates in 50% of ZebraLogic problems.\n\n## Key Argument\n\nThe authors contend that reported benchmark improvements conflate genuine capability gains with data leakage. They demonstrate that training on semantic duplicates of benchmark data improves performance both on those benchmarks and on truly held-out datapoints from the same benchmark. This indicates benchmark gains \"reflect both genuine capability improvements and the accumulation of test data\" in expanding training corpora, undermining claims about true out-of-distribution generalization.",
    "durationMs": 5298,
    "url": "https://arxiv.org/abs/2602.12413"
  },
  "sourceToolAssistantUUID": "b6b4258f-5e39-469a-9282-1910c9d797a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-29T05:22:54.604Z_

<details><summary>↩ Tool result · `toolu_01CqghDdKkGGzFAoZPfd95Rx`</summary>

```text
# Paper Summary

**Full Title:** "Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models"

**Authors:** Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, Ge Li

**Date:** Submitted February 24, 2024; last revised May 31, 2024 (v3)

**Abstract Overview:**

The paper addresses a critical issue in LLM evaluation: training data may inadvertently include test data, compromising benchmark validity. The researchers introduce two complementary methods:

1. **CDD (Contamination Detection via output Distribution):** Detects contamination by analyzing the peakedness of an LLM's output distribution, requiring only sampled texts. The method achieved "average relative improvements of 21.8%-30.2%" compared to other detection approaches.

2. **TED (Trustworthy Evaluation via output Distribution):** Mitigates contamination's impact through output distribution correction, reducing inflated performance gains by up to 66.9%.

The study presents two benchmarks (DetCon and ComiEval) and reveals that "ChatGPT exhibits a high potential to suffer from data contamination on HumanEval benchmark." The paper was accepted to ACL.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b84fbc4f-2b26-43b4-9b5c-3956f8288774",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "2dab3bc3-74ac-4beb-b919-de52b6ab70f2",
  "toolUseResult": {
    "bytes": 49000,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Full Title:** \"Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models\"\n\n**Authors:** Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, Ge Li\n\n**Date:** Submitted February 24, 2024; last revised May 31, 2024 (v3)\n\n**Abstract Overview:**\n\nThe paper addresses a critical issue in LLM evaluation: training data may inadvertently include test data, compromising benchmark validity. The researchers introduce two complementary methods:\n\n1. **CDD (Contamination Detection via output Distribution):** Detects contamination by analyzing the peakedness of an LLM's output distribution, requiring only sampled texts. The method achieved \"average relative improvements of 21.8%-30.2%\" compared to other detection approaches.\n\n2. **TED (Trustworthy Evaluation via output Distribution):** Mitigates contamination's impact through output distribution correction, reducing inflated performance gains by up to 66.9%.\n\nThe study presents two benchmarks (DetCon and ComiEval) and reveals that \"ChatGPT exhibits a high potential to suffer from data contamination on HumanEval benchmark.\" The paper was accepted to ACL.",
    "durationMs": 4566,
    "url": "https://arxiv.org/abs/2402.15938"
  },
  "sourceToolAssistantUUID": "b84fbc4f-2b26-43b4-9b5c-3956f8288774",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 63 · 2026-05-29T05:23:19.734Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the final list of 15+ most important papers. Let me carefully curate the list excluding the 7 seed papers the user already knows, and focusing on maximum relevance to CRADE.

The seed papers are:
1. Zawalski et al. "CoDeC" 
2. Li et al. "ATLAS"
3. Hou et al. "MaSTer"
4. Zheng et al. "ReasoningMath-Plus"
5. Chen et al. "Reasoning Models Don't Always Say What They Think"


6. Xu et al. "DCR"
7. Kocetkov et al. "On The Fragility of Benchmark Contamination Detection in Reasoning Models"

Now I'm organizing my final 15+ papers by relevance to CRADE. Starting with Tier 1 papers that sit at the intersection of IRT and adversarial evaluation—RIDE is the only one directly bridging these two areas, and GSM-Symbolic from Apple established the foundational symbolic perturbation approach that's central to this work.

tinyBenchmarks provides the IRT framework for LLM evaluation, while Putnam-AXIOM and MATH-Perturb both tackle structural perturbations to distinguish surface-level pattern matching from genuine reasoning. ProcessBench and GenPRM address step-level error detection and verification, with the Lightman et al. PRM paper being the seminal work in this space.

On the faithfulness and contamination front, FaithCoT-Bench measures CoT reliability, while LiveBench and metabench tackle the contamination problem through different approaches—one as a leading contamination-resistant benchmark and the other through IRT compression. The Yue et al. paper questions whether RL actually incentivizes reasoning, and Bordt et al. examine when contamination becomes critical. JECS and ReasonEval push further into provable decontamination and distinguishing between answer correctness and reasoning quality.

I'm also pulling in CDD/TED for joint detection and mitigation, Soft Contamination for testing shallow generalization through semantic duplicates, and GSM-Plus for its perturbation taxonomy. That gives me 18 papers total, which covers the user's request well. I should verify GenPRM's venue though—the WebFetch indicated it's an arXiv preprint from 2025, so I'll note it that way rather than claiming AAAI 2026 without confirmation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dab3bc3-74ac-4beb-b919-de52b6ab70f2",
  "isSidechain": false,
  "requestId": "req_011CbWJPrpr54KXD5DfE1Hea",
  "type": "assistant",
  "uuid": "36f19f78-3a32-4084-9689-0fd103689457",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSTSALAH53dpYXUJwftq8G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 931,
      "cache_read_input_tokens": 55374,
      "output_tokens": 1378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 931,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1378,
          "cache_read_input_tokens": 55374,
          "cache_creation_input_tokens": 931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 931
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

_source line 64 · 2026-05-29T05:23:20.014Z_

Now I have comprehensive data from all searches. Let me compile the final curated list of the most important papers, excluding the 7 seed papers you already have detailed notes on. Let me verify one more critical paper:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36f19f78-3a32-4084-9689-0fd103689457",
  "isSidechain": false,
  "requestId": "req_011CbWJPrpr54KXD5DfE1Hea",
  "type": "assistant",
  "uuid": "621dfcba-c048-4f10-9c14-06dd7c324ffa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSTSALAH53dpYXUJwftq8G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 931,
      "cache_read_input_tokens": 55374,
      "output_tokens": 1378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 931,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1378,
          "cache_read_input_tokens": 55374,
          "cache_creation_input_tokens": 931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 931
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

_source line 65 · 2026-05-29T05:23:21.489Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01UB1zmqFvccd5Ux5ha4tASp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2412.06559",
  "prompt": "Extract full title, authors, date, abstract, and venue for ProcessBench. Is it accepted at ACL 2025?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "621dfcba-c048-4f10-9c14-06dd7c324ffa",
  "isSidechain": false,
  "requestId": "req_011CbWJPrpr54KXD5DfE1Hea",
  "type": "assistant",
  "uuid": "da4c161b-baea-43ed-874f-22c7053b2941",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSTSALAH53dpYXUJwftq8G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 931,
      "cache_read_input_tokens": 55374,
      "output_tokens": 1378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 931,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1378,
          "cache_read_input_tokens": 55374,
          "cache_creation_input_tokens": 931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 931
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

_source line 66 · 2026-05-29T05:23:22.116Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018NyKKMLG6nLxLD1eZoVyvF`</summary>

```json
{
  "url": "https://arxiv.org/abs/2404.05692",
  "prompt": "Extract full title, authors, date, abstract, and venue for ReasonEval. Is it accepted at AAAI 2025?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da4c161b-baea-43ed-874f-22c7053b2941",
  "isSidechain": false,
  "requestId": "req_011CbWJPrpr54KXD5DfE1Hea",
  "type": "assistant",
  "uuid": "97482663-fb3a-4eaf-a4e1-225c76f32b70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SSTSALAH53dpYXUJwftq8G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 931,
      "cache_read_input_tokens": 55374,
      "output_tokens": 1378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 931,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1378,
          "cache_read_input_tokens": 55374,
          "cache_creation_input_tokens": 931,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 931
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

_source line 67 · 2026-05-29T05:23:25.651Z_

<details><summary>↩ Tool result · `toolu_018NyKKMLG6nLxLD1eZoVyvF`</summary>

```text
# ReasonEval Paper Details

**Full Title:** "Evaluating Mathematical Reasoning Beyond Accuracy"

**Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu

**Date:** Submitted April 8, 2024; revised January 14, 2025

**Venue:** AAAI 2025 (accepted)

**Abstract Summary:** The paper introduces ReasonEval, a methodology for assessing reasoning quality in mathematical tasks. Rather than focusing solely on final answers, it evaluates intermediate reasoning steps using "validity and redundancy" metrics. The authors demonstrate that improved final-answer accuracy doesn't necessarily correlate with better overall reasoning quality in challenging problems. They've open-sourced their best model, evaluation scripts, and results.

**Acceptance Status:** Yes—the submission history notes that v2 represents "the AAAI 2025 camera ready version," confirming acceptance at this venue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97482663-fb3a-4eaf-a4e1-225c76f32b70",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "8e10acda-9472-4bde-9c8c-f5da2dbc3499",
  "toolUseResult": {
    "bytes": 47121,
    "code": 200,
    "codeText": "OK",
    "result": "# ReasonEval Paper Details\n\n**Full Title:** \"Evaluating Mathematical Reasoning Beyond Accuracy\"\n\n**Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu\n\n**Date:** Submitted April 8, 2024; revised January 14, 2025\n\n**Venue:** AAAI 2025 (accepted)\n\n**Abstract Summary:** The paper introduces ReasonEval, a methodology for assessing reasoning quality in mathematical tasks. Rather than focusing solely on final answers, it evaluates intermediate reasoning steps using \"validity and redundancy\" metrics. The authors demonstrate that improved final-answer accuracy doesn't necessarily correlate with better overall reasoning quality in challenging problems. They've open-sourced their best model, evaluation scripts, and results.\n\n**Acceptance Status:** Yes—the submission history notes that v2 represents \"the AAAI 2025 camera ready version,\" confirming acceptance at this venue.",
    "durationMs": 3530,
    "url": "https://arxiv.org/abs/2404.05692"
  },
  "sourceToolAssistantUUID": "97482663-fb3a-4eaf-a4e1-225c76f32b70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-29T05:23:25.773Z_

<details><summary>↩ Tool result · `toolu_01UB1zmqFvccd5Ux5ha4tASp`</summary>

```text
# ProcessBench Paper Information

**Full Title:** "ProcessBench: Identifying Process Errors in Mathematical Reasoning"

**Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin

**Submission Date:** December 9, 2024 (most recent version: May 26, 2025)

**Abstract Summary:** The paper introduces a benchmark containing 3,400 test cases focused on competition- and Olympiad-level mathematics. The work evaluates models' capacity to "identify the earliest step that contains an error, or conclude that all steps are correct." Researchers tested process reward models and critic models, finding that existing PRMs struggle with harder problems, while QwQ-32B-Preview demonstrates competitive performance with GPT-4o.

**Venue:** Yes, the paper indicates "ACL 2025" in the comments section, suggesting acceptance at the Association for Computational Linguistics 2025 conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da4c161b-baea-43ed-874f-22c7053b2941",
  "isSidechain": false,
  "promptId": "84dbaf4c-3911-4231-b0f2-284bc794a129",
  "type": "user",
  "uuid": "9a0bf6a3-146b-46c2-97a6-98b1400e9dbf",
  "toolUseResult": {
    "bytes": 48079,
    "code": 200,
    "codeText": "OK",
    "result": "# ProcessBench Paper Information\n\n**Full Title:** \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\"\n\n**Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin\n\n**Submission Date:** December 9, 2024 (most recent version: May 26, 2025)\n\n**Abstract Summary:** The paper introduces a benchmark containing 3,400 test cases focused on competition- and Olympiad-level mathematics. The work evaluates models' capacity to \"identify the earliest step that contains an error, or conclude that all steps are correct.\" Researchers tested process reward models and critic models, finding that existing PRMs struggle with harder problems, while QwQ-32B-Preview demonstrates competitive performance with GPT-4o.\n\n**Venue:** Yes, the paper indicates \"ACL 2025\" in the comments section, suggesting acceptance at the Association for Computational Linguistics 2025 conference.",
    "durationMs": 4280,
    "url": "https://arxiv.org/abs/2412.06559"
  },
  "sourceToolAssistantUUID": "da4c161b-baea-43ed-874f-22c7053b2941",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 69 · 2026-05-29T05:23:35.155Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the final JSON array with the 15+ most important papers, excluding the 7 seed papers the user already knows about. I'll organize by relevance to CRADE.

Let me finalize my selections:

1. **RIDE** - IRT + adversarial perturbation (directly at the three-way intersection)
2. **GSM-Symbolic** - Seminal symbolic perturbation (ICLR 2025, Apple)


3. **tinyBenchmarks** - Foundational IRT for LLM evaluation (ICML 2024)
4. **Putnam-AXIOM** - Functional variants with provable correctness (ICML 2025)
5. **MATH-Perturb** - Hard structural perturbations (2025)
6. **ProcessBench** - Step-level error detection (ACL 2025)
7. **GenPRM** - Generative PRM with code verification (arXiv 2025)
8. **Let's Verify Step by Step** - Seminal PRM paper (ICLR 2024)
9. **FaithCoT-Bench** - CoT faithfulness benchmark (ICLR 2026)
10. Continuing through the remaining high-impact papers that bridge IRT, perturbation strategies, and process-level reasoning... I've compiled all 18 relevant papers and now I'm ready to write up the final output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a0bf6a3-146b-46c2-97a6-98b1400e9dbf",
  "isSidechain": false,
  "requestId": "req_011CbWJSAKNAyRKgdJYJt8vD",
  "type": "assistant",
  "uuid": "244d3610-3b52-43f3-ac6f-f1334d0327f6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxL4mFv7Rt5oHyD1TG4eCq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 250,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 56305,
      "output_tokens": 4989,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 250,
          "output_tokens": 4989,
          "cache_read_input_tokens": 56305,
          "cache_creation_input_tokens": 1647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1647
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

_source line 70 · 2026-05-29T05:24:52.543Z_

I now have comprehensive, verified data from all five parallel research agents covering contamination detection, adversarial robustness, IRT for LLM evaluation, step-level reasoning, and best paper awards. Let me synthesize the final curated list.

---

## Literature Survey: CRADE Framework — Key Related Papers (2024–2026)

Below are the **18 most important recent papers** beyond your 7 seed papers, organized by relevance to the CRADE framework's three-way intersection of contamination detection, adversarial robustness, and IRT-calibrated evaluation. Each was verified by reading the actual arXiv abstract.

### Why these papers matter for CRADE

Your framework sits at a unique three-way intersection: **contamination × robustness × IRT**. No existing paper occupies this exact space. The papers below cover the strongest work in each of the three component areas, plus the rare papers that bridge two of the three — most critically, **RIDE** (IRT × robustness) and **JECS** (contamination × joint statistical modeling), which are your closest methodological neighbors.

---

```json
[
  {
    "title": "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
    "authors": "Xinyuan Li et al.",
    "venue": "arXiv 2025 (revised Jan 2026)",
    "url": "https://arxiv.org/abs/2511.04120",
    "why_important": "Only paper bridging IRT and adversarial perturbation — uses IRT-calibrated difficulty to guide RL-based adversarial question rewriting; closest methodological precursor to CRADE's joint IRT-robustness modeling",
    "one_line_summary": "Combines Item Response Theory with reinforcement learning to generate difficulty-calibrated adversarial variants of math problems, causing 21.7% average accuracy drops across 26 LLMs."
  },
  {
    "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models",
    "authors": "Mirzadeh et al. (Apple)",
    "venue": "ICLR 2025",
    "url": "https://arxiv.org/abs/2410.05229",
    "why_important": "Seminal work establishing symbolic template methodology for adversarial math evaluation; highly cited; introduced the paradigm CRADE's SymPy-backed variant generation builds upon",
    "one_line_summary": "Uses parameterized symbolic templates over GSM8K to show LLMs exhibit up to 65% accuracy drops from irrelevant clauses, suggesting pattern matching rather than genuine reasoning."
  },
  {
    "title": "tinyBenchmarks: Evaluating LLMs with Fewer Examples",
    "authors": "Polo et al.",
    "venue": "ICML 2024",
    "url": "https://arxiv.org/abs/2402.14992",
    "why_important": "Foundational paper establishing IRT-based benchmark reduction for LLMs; introduced the gp-IRT estimator that achieves 2% error with 100 items instead of 14K; baseline for all subsequent IRT-for-LLM work",
    "one_line_summary": "Demonstrates that 100 IRT-curated examples suffice to estimate LLM performance on MMLU, reducing evaluation cost by 140x while maintaining accuracy."
  },
  {
    "title": "Putnam-AXIOM: A Functional and Static Benchmark for Measuring Higher Level Mathematical Reasoning in LLMs",
    "authors": "Gulati et al.",
    "venue": "ICML 2025",
    "url": "https://arxiv.org/abs/2508.08292",
    "why_important": "Top-venue paper demonstrating functional variant methodology at competition level; o1-preview drops from 41.9% to 22.3% on variants, directly quantifying the contamination-robustness gap CRADE aims to decompose",
    "one_line_summary": "Creates 522 Putnam competition problems plus 100 programmatically generated functional variants, showing major accuracy drops that suggest memorization over reasoning."
  },
  {
    "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
    "authors": "Huang et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2502.06453",
    "why_important": "Distinguishes surface-level from deep structural perturbations; 'hard' perturbations fundamentally change problem nature so original solution steps fail, directly testing for memorization vs. reasoning",
    "one_line_summary": "Creates MATH-P-Simple and MATH-P-Hard benchmarks with perturbations that either preserve or break original solution strategies, revealing memorization-driven reasoning in frontier LLMs."
  },
  {
    "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
    "authors": "Zheng et al. (Alibaba/Qwen)",
    "venue": "ACL 2025",
    "url": "https://arxiv.org/abs/2412.06559",
    "why_important": "Primary benchmark for step-level error detection (3,400 test cases); directly relevant to CRADE's step-level perturbation alignment metric; reveals that existing PRMs struggle on hard problems",
    "one_line_summary": "Evaluates models' ability to identify the earliest error step in mathematical reasoning chains, finding process reward models struggle on competition-level problems."
  },
  {
    "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
    "authors": "Zhao et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2504.00891",
    "why_important": "State-of-the-art step-level verification via generative reasoning with code verification; 1.5B model outperforms GPT-4o on ProcessBench; directly usable as CRADE's step-level evaluation component",
    "one_line_summary": "Introduces a generative process reward model that performs explicit CoT reasoning with code verification before judging each step, achieving SOTA step-level verification."
  },
  {
    "title": "Let's Verify Step by Step",
    "authors": "Lightman et al. (OpenAI)",
    "venue": "ICLR 2024",
    "url": "https://arxiv.org/abs/2305.20050",
    "why_important": "Seminal paper launching the process reward model research area; proved process supervision significantly outperforms outcome supervision on MATH; released PRM800K dataset",
    "one_line_summary": "Demonstrates that process-level supervision (verifying each reasoning step) substantially outperforms outcome-level supervision for mathematical reasoning, establishing the PRM paradigm."
  },
  {
    "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
    "authors": "Shen et al.",
    "venue": "ICLR 2026",
    "url": "https://arxiv.org/abs/2510.04040",
    "why_important": "First comprehensive instance-level CoT faithfulness benchmark with 1,000+ annotated trajectories; directly relevant to CRADE's step-level perturbation alignment where CoT must faithfully track problem changes",
    "one_line_summary": "Provides the first systematic benchmark for detecting unfaithful chain-of-thought at the instance level, evaluating 11 detection methods across 300+ unfaithful reasoning instances."
  },
  {
    "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?",
    "authors": "Yue et al.",
    "venue": "NeurIPS 2025 (Best Paper Runner-Up)",
    "url": "https://arxiv.org/abs/2504.13837",
    "why_important": "NeurIPS 2025 Runner-Up challenging the RLVR narrative; shows RL improves sampling efficiency but creates no new reasoning patterns — critical context for interpreting what CRADE's 'genuine capability' score actually measures",
    "one_line_summary": "Shows that RLVR does not create fundamentally new reasoning abilities beyond the base model — it optimizes inference-time sampling rather than expanding reasoning capacity."
  },
  {
    "title": "How Much Can We Forget about Data Contamination?",
    "authors": "Bordt et al.",
    "venue": "ICML 2025",
    "url": "https://arxiv.org/abs/2410.03249",
    "why_important": "Provides the scaling-law perspective on contamination severity; shows 144x contamination can be 'forgotten' at 5x Chinchilla-optimal, essential for calibrating CRADE's contamination estimates",
    "one_line_summary": "Experimentally quantifies contamination persistence across model size and training tokens, finding contamination washes out when training data is sufficiently large."
  },
  {
    "title": "LiveBench: A Challenging, Contamination-Limited LLM Benchmark",
    "authors": "White et al.",
    "venue": "ICLR 2025 (Spotlight)",
    "url": "https://arxiv.org/abs/2406.19314",
    "why_important": "ICLR 2025 Spotlight; leading contamination-resistant benchmark with monthly updates; uses objective ground-truth scoring; provides the 'living benchmark' paradigm that CRADE's framework must interoperate with",
    "one_line_summary": "Monthly-updated benchmark with questions from recent math competitions, arXiv, and news, using objective scoring without LLM judges to minimize contamination effects."
  },
  {
    "title": "metabench — A Sparse Benchmark of Reasoning and Knowledge in Large Language Models",
    "authors": "Kipnis et al.",
    "venue": "ICLR 2025",
    "url": "https://arxiv.org/abs/2407.12844",
    "why_important": "Uses IRT to compress 28,632 items to 858 (<3%) with 1.24% RMSE; reveals a single latent factor captures 79.3% of cross-benchmark variability — validates IRT for LLM evaluation at scale",
    "one_line_summary": "Applies IRT to distill six major LLM benchmarks into 858 items while preserving rankings, revealing that a single latent factor dominates LLM benchmark performance."
  },
  {
    "title": "Provable Joint Decontamination for Benchmarking Multiple Large Language Models",
    "authors": "Liu et al.",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2605.21543",
    "why_important": "Proposes JECS with provable global contamination rate control across multiple LLMs via conformal p-values; the statistical framework for joint contamination modeling most relevant to CRADE's EM-based joint estimation",
    "one_line_summary": "Uses conformal inference with adaptive Benjamini-Hochberg to select a decontaminated benchmark subset with provable contamination rate guarantees across multiple LLMs simultaneously."
  },
  {
    "title": "ReasonEval: Evaluating Mathematical Reasoning Beyond Accuracy",
    "authors": "Xia et al.",
    "venue": "AAAI 2025",
    "url": "https://arxiv.org/abs/2404.05692",
    "why_important": "Same venue family (AAAI); introduces validity and redundancy metrics for step-level reasoning; proves higher final-answer accuracy doesn't correlate with better step quality on hard problems",
    "one_line_summary": "Introduces step-level evaluation metrics (validity and redundancy) showing that improved final-answer accuracy does not necessarily indicate better reasoning quality."
  },
  {
    "title": "Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models",
    "authors": "Dong et al.",
    "venue": "ACL 2024",
    "url": "https://arxiv.org/abs/2402.15938",
    "why_important": "One of few papers jointly addressing detection (CDD) AND score correction (TED); reduces contamination-inflated gains by up to 66.9%; direct methodological precedent for CRADE's corrective evaluation",
    "one_line_summary": "Proposes CDD for contamination detection via output distribution peakedness and TED for score correction via distribution adjustment, jointly detecting and mitigating contamination effects."
  },
  {
    "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers",
    "authors": "Li et al.",
    "venue": "ACL 2024",
    "url": "https://arxiv.org/abs/2402.19255",
    "why_important": "Establishes the canonical taxonomy of mathematical perturbation types (8 families) that subsequent work including MaSTer builds upon; top-venue reference for systematic robustness evaluation",
    "one_line_summary": "Extends GSM8K with 8 families of mathematical perturbations, testing 25 LLMs across 4 prompting strategies and finding performance is far from robust on perturbed variants."
  },
  {
    "title": "Soft Contamination Means Benchmarks Test Shallow Generalization",
    "authors": "Spiesberger et al.",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2602.12413",
    "why_important": "Shows semantic duplicates escape n-gram detection (78% of CodeForces contaminated); training on them improves both contaminated AND held-out items — proving contamination and generalization are entangled, supporting CRADE's core thesis",
    "one_line_summary": "Demonstrates that semantic duplicates in training data inflate benchmark scores while escaping standard decontamination, showing benchmark gains conflate genuine capability with data leakage."
  }
]
```

### How these papers map to CRADE's components

| CRADE Component | Key Papers |
|---|---|
| **Contamination profiling** | JECS (provable joint decontamination), CDD/TED (detection + correction), Bordt et al. (scaling perspective), Soft Contamination (semantic leakage) |
| **Adversarial variant generation** | GSM-Symbolic (symbolic templates), GSM-Plus (perturbation taxonomy), MATH-Perturb (hard perturbations), Putnam-AXIOM (functional variants), RIDE (IRT-guided perturbation) |
| **Step-level reasoning evaluation** | Let's Verify Step by Step (seminal PRM), ProcessBench (step-level benchmark), GenPRM (generative PRM), ReasonEval (validity metrics), FaithCoT-Bench (CoT faithfulness) |
| **IRT-calibrated scoring** | tinyBenchmarks (foundational IRT), metabench (IRT compression), RIDE (IRT + perturbation) |
| **Core thesis support** | Yue et al. (RL doesn't create new reasoning), LiveBench (contamination-resistant baseline), Soft Contamination (contamination-robustness entanglement) |

### Critical gap confirmed

None of these 18 papers (nor any other paper found across 150+ search results) performs **joint contamination-aware IRT estimation** — the contamination indicator $c_{ij}$ in your 3PL model $P(\text{correct} | \theta_j, d_i, c_{ij}) = c_{ij} \cdot p_{\text{mem}} + (1 - c_{ij}) \cdot \sigma(\theta_j - d_i)$ is entirely novel. **RIDE** comes closest by connecting IRT to perturbation, but uses IRT only for difficulty calibration (not contamination-aware ability estimation). **JECS** comes closest from the contamination side but uses conformal inference (not IRT). The $G + C - R$ decomposition has no precedent in any paper found.

Sources:
- [RIDE](https://arxiv.org/abs/2511.04120)
- [GSM-Symbolic](https://arxiv.org/abs/2410.05229)
- [tinyBenchmarks](https://arxiv.org/abs/2402.14992)
- [Putnam-AXIOM](https://arxiv.org/abs/2508.08292)
- [MATH-Perturb](https://arxiv.org/abs/2502.06453)
- [ProcessBench](https://arxiv.org/abs/2412.06559)
- [GenPRM](https://arxiv.org/abs/2504.00891)
- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)
- [FaithCoT-Bench](https://arxiv.org/abs/2510.04040)
- [Does RL Really Incentivize Reasoning?](https://arxiv.org/abs/2504.13837)
- [How Much Can We Forget](https://arxiv.org/abs/2410.03249)
- [LiveBench](https://arxiv.org/abs/2406.19314)
- [metabench](https://arxiv.org/abs/2407.12844)
- [JECS](https://arxiv.org/abs/2605.21543)
- [ReasonEval](https://arxiv.org/abs/2404.05692)
- [CDD/TED](https://arxiv.org/abs/2402.15938)
- [GSM-Plus](https://arxiv.org/abs/2402.19255)
- [Soft Contamination](https://arxiv.org/abs/2602.12413)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "244d3610-3b52-43f3-ac6f-f1334d0327f6",
  "isSidechain": false,
  "requestId": "req_011CbWJSAKNAyRKgdJYJt8vD",
  "type": "assistant",
  "uuid": "838b411e-f9ae-4906-8bfc-5973788ca3d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxL4mFv7Rt5oHyD1TG4eCq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 250,
      "cache_creation_input_tokens": 1647,
      "cache_read_input_tokens": 56305,
      "output_tokens": 4989,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 250,
          "output_tokens": 4989,
          "cache_read_input_tokens": 56305,
          "cache_creation_input_tokens": 1647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1647
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

_source line 71_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "838b411e-f9ae-4906-8bfc-5973788ca3d1",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 73_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "838b411e-f9ae-4906-8bfc-5973788ca3d1",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---

### Runtime record

_source line 74_

```json
{
  "type": "ai-title",
  "aiTitle": "Find 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "48bf462a-d28d-43ae-96da-d57db5986663"
}
```

---
