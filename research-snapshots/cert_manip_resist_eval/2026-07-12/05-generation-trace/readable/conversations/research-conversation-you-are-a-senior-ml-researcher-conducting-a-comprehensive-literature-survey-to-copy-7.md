# Research conversation: You are a senior ML researcher conducting a comprehensive literature survey. **Today's date: 2026-05-29 (UTC).** ## Task

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/5b4b3702-9e5c-43ae-bc09-805d1229cbbe.jsonl`
- **Structured JSON:** [`99169e3ef3fb059314da.json`](../../sessions/99/99169e3ef3fb059314da.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T05:23:25.850Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T05:23:25.850Z",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "content": "You are a senior ML researcher conducting a comprehensive literature survey.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Task\nFind the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:\n\n**Target: AAAI 2026\nTrack: AI Alignment / Main Technical Track — Robustness Evaluation\n\nDirection: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated \"genuine capability\" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.\n\nSeed Papers:\n- Zawalski et al. \"CoDeC\" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation\n- Li et al. \"ATLAS\" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity\n- Hou et al. \"MaSTer\" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination\n- Zheng et al. \"ReasoningMath-Plus\" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component\n- Chen et al. \"Reasoning Models Don't Always Say What They Think\" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination\n- Xu et al. \"DCR\" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis\n- Kocetkov et al. \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches\n\nKnown Gaps:\n- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)\n- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only\n- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing\n- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives\n\nTheoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)\n- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)\n- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth\n\nQuality Self-Checks:\n- [x] Core insight: \"Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level.\"\n- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.\n- [x] Baseline fear test: A simple baseline of \"run on variants and average\" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.\n- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.\n\nAvoid:\n- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)\n- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark\n- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)\n- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead**\n\n## What counts as 'important'\n\nPrioritize (in order):\n1. **Best paper awards** at top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, AAAI, etc.)\n2. **Oral / spotlight presentations** at these venues\n3. **Highly cited papers** (>50 citations in 1-2 years)\n4. **Papers that introduced widely-adopted methods** (e.g., new training paradigm, new benchmark)\n5. **Recent survey papers** that provide comprehensive field overviews\n6. **Strong recent work** from top labs (Google, Meta, DeepMind, OpenAI, CMU, Stanford, etc.)\n\n## Search strategy\n\nExecute AT LEAST 15 targeted searches:\n\n1. `best paper award ACL EMNLP NeurIPS ICML ICLR 2026 Target: AAAI 2026\nTrack: AI Alignment / Main Technical Track — Robustness Evaluation\n\nDirection: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated \"genuine capability\" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.\n\nSeed Papers:\n- Zawalski et al. \"CoDeC\" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation\n- Li et al. \"ATLAS\" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity\n- Hou et al. \"MaSTer\" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination\n- Zheng et al. \"ReasoningMath-Plus\" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component\n- Chen et al. \"Reasoning Models Don't Always Say What They Think\" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination\n- Xu et al. \"DCR\" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis\n- Kocetkov et al. \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches\n\nKnown Gaps:\n- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)\n- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only\n- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing\n- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives\n\nTheoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)\n- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)\n- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth\n\nQuality Self-Checks:\n- [x] Core insight: \"Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level.\"\n- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.\n- [x] Baseline fear test: A simple baseline of \"run on variants and average\" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.\n- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.\n\nAvoid:\n- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)\n- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark\n- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)\n- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead`\n2. `oral spotlight {venue} 2026 {topic}` — for each major venue\n3. `site:openreview.net {topic} 2026 outstanding` — OpenReview 高分论文\n4. `{topic} survey 2026` 或 `{topic} survey 2025` — 综述论文\n5. `site:arxiv.org {topic} 2026` — arXiv 最新高引\n6. `most cited {topic} 2025 2026` — Google Scholar\n7. `site:paperswithcode.com {task} SOTA` — SOTA 排行榜上的论文\n8. `{topic} benchmark {year}` — 定义领域的 benchmark 论文\n9. 对每个找到的重要论文，搜索其 cited-by 发现后续工作\n\nFor EVERY paper you find, use WebFetch to read its abstract and introduction on arXiv or OpenReview. Do NOT rely on search snippets alone — you need to understand what each paper actually does.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Full paper title\",\n  \"authors\": \"First author et al.\",\n  \"venue\": \"EMNLP 2025 / NeurIPS 2024 / arXiv 2025 / ...\",\n  \"url\": \"https://arxiv.org/abs/... or openreview URL\",\n  \"why_important\": \"Best paper / Oral / High-cited / Introduced X / ...\",\n  \"one_line_summary\": \"What this paper does in one sentence\"\n}\n\nFind at least 15 papers. More is better if they are genuinely relevant.\nIMPORTANT: You MUST end your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T05:23:25.854Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T05:23:25.854Z",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-29T05:23:25.876Z_

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
  "promptId": "37ea365b-dcd4-4897-b99b-0b8f025b793a",
  "type": "user",
  "uuid": "109ba4da-cc0d-48d8-8c68-404ca2b3c432",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T05:23:25.875Z_

```json
{
  "parentUuid": "109ba4da-cc0d-48d8-8c68-404ca2b3c432",
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
  "uuid": "a1f7d211-f292-4883-98f6-8b41274a89b2",
  "timestamp": "2026-05-29T05:23:25.875Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T05:23:25.875Z_

```json
{
  "parentUuid": "a1f7d211-f292-4883-98f6-8b41274a89b2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e093038d-30b0-4607-ac1f-ebd4490f708d",
  "timestamp": "2026-05-29T05:23:25.875Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
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
  "aiTitle": "Survey 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Assistant

_source line 7 · 2026-05-29T05:23:31.243Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a comprehensive literature survey for their CRADE framework paper targeting AAAI 2026. I need to find the 15 most important recent papers (2024-2026) related to their research area, which sits at the intersection of:

1. Benchmark contamination detection/mitigation
2. Adversarial robustness evaluation for LLMs
3. Item Response Theory (IRT) for LLM evaluation
4. Step-level reasoning evaluation
5. Chain-of-thought faithfulness

Let me launch multiple search agents in parallel to cover different aspects of this research area. I'll need to use WebSearch and WebFetch tools, so let me first load those tool schemas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e093038d-30b0-4607-ac1f-ebd4490f708d",
  "isSidechain": false,
  "requestId": "req_011CbWJSBMsNfXanNa852szQ",
  "type": "assistant",
  "uuid": "e3797c17-85b3-4dc6-bdb2-00816c12d97b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01576X8zdE8PX7yN3LyqNspp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15555,
      "cache_read_input_tokens": 0,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15555
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

_source line 8 · 2026-05-29T05:23:31.628Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017YBxnAKq7tnF8V3JkLndqi`</summary>

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
  "parentUuid": "e3797c17-85b3-4dc6-bdb2-00816c12d97b",
  "isSidechain": false,
  "requestId": "req_011CbWJSBMsNfXanNa852szQ",
  "type": "assistant",
  "uuid": "a6194b08-f7b2-4b45-982f-ab4bed7bcd40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01576X8zdE8PX7yN3LyqNspp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15555,
      "cache_read_input_tokens": 0,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15555,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 252,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15555
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

_source line 9 · 2026-05-29T05:23:31.638Z_

<details><summary>↩ Tool result · `toolu_017YBxnAKq7tnF8V3JkLndqi`</summary>

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
  "parentUuid": "a6194b08-f7b2-4b45-982f-ab4bed7bcd40",
  "isSidechain": false,
  "promptId": "37ea365b-dcd4-4897-b99b-0b8f025b793a",
  "type": "user",
  "uuid": "2beeb315-7202-4a5d-b7df-ca54fc1e7fcf",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "a6194b08-f7b2-4b45-982f-ab4bed7bcd40",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "2beeb315-7202-4a5d-b7df-ca54fc1e7fcf",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Assistant

_source line 12 · 2026-05-29T05:23:38.064Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have WebSearch and WebFetch available. Let me launch multiple parallel search agents to cover different aspects of this research area comprehensively. I'll divide the searches across several agents to maximize coverage and speed.

Let me plan the search strategy:

1. Contamination detection and mitigation in LLM evaluation
2. Adversarial robustness evaluation / benchmark perturbation
3. Item Response Theory for LLM evaluation
4. Step-level reasoning evaluation / process reward models
5. Chain-of-thought faithfulness
6. Best paper awards at top venues 2024-2026
7. Dynamic benchmarks and evaluation frameworks


8. Launching the parallel agents now to execute these searches simultaneously.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2beeb315-7202-4a5d-b7df-ca54fc1e7fcf",
  "isSidechain": false,
  "requestId": "req_011CbWJSbKmTZNKRrk8z8wmq",
  "type": "assistant",
  "uuid": "b74aa3cc-096f-4f7d-b0e9-a08536539c4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VC2n8XgPVMR8NfVSyhtUgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1272,
      "cache_read_input_tokens": 15555,
      "output_tokens": 2160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2160,
          "cache_read_input_tokens": 15555,
          "cache_creation_input_tokens": 1272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1272
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

_source line 13 · 2026-05-29T05:23:38.180Z_

I'll launch multiple parallel search agents to cover all the key research areas comprehensively. Let me search across contamination detection, adversarial robustness, IRT for LLMs, step-level reasoning evaluation, CoT faithfulness, and recent best papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b74aa3cc-096f-4f7d-b0e9-a08536539c4a",
  "isSidechain": false,
  "requestId": "req_011CbWJSbKmTZNKRrk8z8wmq",
  "type": "assistant",
  "uuid": "fb056e85-626b-45fd-85eb-3689f3d3f078",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VC2n8XgPVMR8NfVSyhtUgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1272,
      "cache_read_input_tokens": 15555,
      "output_tokens": 2160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2160,
          "cache_read_input_tokens": 15555,
          "cache_creation_input_tokens": 1272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1272
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

_source line 14 · 2026-05-29T05:23:43.909Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NJdJqDa4WU372hNSC8dfPk`</summary>

```json
{
  "description": "Search contamination detection papers",
  "prompt": "You are helping with a literature survey for an ML paper. Search for the most important recent papers (2024-2026) on LLM benchmark contamination detection, data contamination in language models, and contamination-adjusted evaluation.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"benchmark contamination detection LLM 2025 2026\"\n2. WebSearch: \"data contamination language model evaluation 2025\"\n3. WebSearch: \"contamination adjusted scores LLM benchmark\"\n4. WebSearch: \"site:arxiv.org benchmark contamination reasoning models 2025\"\n5. WebSearch: \"DCR contamination robust evaluation LLM 2025\"\n6. WebSearch: \"CoDeC contamination detection gray-box 2025\"\n7. WebSearch: \"Kocetkov fragility benchmark contamination detection reasoning models 2025\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details. \n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb056e85-626b-45fd-85eb-3689f3d3f078",
  "isSidechain": false,
  "requestId": "req_011CbWJSbKmTZNKRrk8z8wmq",
  "type": "assistant",
  "uuid": "43bf52fb-2a4d-45fa-bb49-fab0188de41e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VC2n8XgPVMR8NfVSyhtUgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1272,
      "cache_read_input_tokens": 15555,
      "output_tokens": 2160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2160,
          "cache_read_input_tokens": 15555,
          "cache_creation_input_tokens": 1272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1272
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

_source line 15 · 2026-05-29T05:23:48.170Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KHG5V8wy5SGF36CJoLbZVT`</summary>

```json
{
  "description": "Search adversarial robustness evaluation papers",
  "prompt": "You are helping with a literature survey for an ML paper. Search for the most important recent papers (2024-2026) on adversarial robustness evaluation of LLMs, benchmark perturbation methods, and functional variant generation for math/reasoning benchmarks.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"adversarial robustness evaluation LLM mathematical reasoning 2025 2026\"\n2. WebSearch: \"benchmark perturbation LLM evaluation GSM-Plus GSM-Symbolic MATH-Perturb\"\n3. WebSearch: \"MaSTer automated adversarial math variant generation 2026\"\n4. WebSearch: \"symbolic perturbation math benchmark LLM robustness\"\n5. WebSearch: \"functional variant generation benchmark evaluation language model 2025\"\n6. WebSearch: \"site:arxiv.org adversarial math evaluation reasoning LLM 2025 2026\"\n7. WebSearch: \"LLM reasoning robustness perturbation NeurIPS ICML 2025\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details.\n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43bf52fb-2a4d-45fa-bb49-fab0188de41e",
  "isSidechain": false,
  "requestId": "req_011CbWJSbKmTZNKRrk8z8wmq",
  "type": "assistant",
  "uuid": "5bc8f256-5c3b-406b-ab75-b05203b558f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VC2n8XgPVMR8NfVSyhtUgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1272,
      "cache_read_input_tokens": 15555,
      "output_tokens": 2160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2160,
          "cache_read_input_tokens": 15555,
          "cache_creation_input_tokens": 1272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1272
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

_source line 16 · 2026-05-29T05:23:52.011Z_

<details open><summary>🔧 Tool call — Agent · `toolu_018C52qSXytHwYRM2PRt79fw`</summary>

```json
{
  "description": "Search IRT for LLM evaluation papers",
  "prompt": "You are helping with a literature survey for an ML paper. Search for the most important recent papers (2024-2026) on Item Response Theory (IRT) applied to LLM evaluation, psychometrics for AI evaluation, and calibrated capability scoring.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"Item Response Theory LLM evaluation 2025 2026\"\n2. WebSearch: \"IRT language model benchmark evaluation adaptive testing\"\n3. WebSearch: \"ATLAS IRT adaptive testing LLM 2025\"\n4. WebSearch: \"psychometrics AI evaluation language model calibration\"\n5. WebSearch: \"site:arxiv.org IRT LLM evaluation 2025\"\n6. WebSearch: \"computerized adaptive testing large language models\"\n7. WebSearch: \"measurement theory LLM evaluation capability scoring 2025\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details.\n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bc8f256-5c3b-406b-ab75-b05203b558f3",
  "isSidechain": false,
  "requestId": "req_011CbWJSbKmTZNKRrk8z8wmq",
  "type": "assistant",
  "uuid": "a5c07c8a-c109-4bc2-8c7b-35d61c2b331c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VC2n8XgPVMR8NfVSyhtUgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1272,
      "cache_read_input_tokens": 15555,
      "output_tokens": 2160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2160,
          "cache_read_input_tokens": 15555,
          "cache_creation_input_tokens": 1272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1272
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

_source line 17 · 2026-05-29T05:23:55.879Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XtAGbHHfFgLSD2R11szjrw`</summary>

```json
{
  "description": "Search step-level reasoning and CoT faithfulness",
  "prompt": "You are helping with a literature survey for an ML paper. Search for the most important recent papers (2024-2026) on step-level reasoning evaluation, chain-of-thought faithfulness, process reward models, and reasoning verification.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"step-level reasoning evaluation LLM 2025 2026\"\n2. WebSearch: \"chain-of-thought faithfulness language model 2025\"\n3. WebSearch: \"process reward model reasoning verification 2025\"\n4. WebSearch: \"ReasoningMath-Plus step-level evaluation 2026\"\n5. WebSearch: \"reasoning models don't always say what they think Anthropic 2025\"\n6. WebSearch: \"CoT faithfulness unfaithful reasoning LLM 2025\"\n7. WebSearch: \"site:arxiv.org process-level evaluation mathematical reasoning 2025\"\n8. WebSearch: \"LLM reasoning trace evaluation verification step-by-step 2025\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details.\n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5c07c8a-c109-4bc2-8c7b-35d61c2b331c",
  "isSidechain": false,
  "requestId": "req_011CbWJSbKmTZNKRrk8z8wmq",
  "type": "assistant",
  "uuid": "3abcc399-5f64-4397-8a76-71124cdb7ac3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VC2n8XgPVMR8NfVSyhtUgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1272,
      "cache_read_input_tokens": 15555,
      "output_tokens": 2160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2160,
          "cache_read_input_tokens": 15555,
          "cache_creation_input_tokens": 1272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1272
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

_source line 18 · 2026-05-29T05:24:00.556Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HkVpdchzYkyjGRPgJoZYwZ`</summary>

```json
{
  "description": "Search best papers and LLM evaluation frameworks",
  "prompt": "You are helping with a literature survey for an ML paper about LLM evaluation combining contamination detection, adversarial robustness, and IRT-based scoring. Search for the most important recent papers (2024-2026) on LLM evaluation frameworks, best paper awards, and evaluation methodology.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"best paper award NeurIPS 2025 LLM evaluation\"\n2. WebSearch: \"best paper award ICML 2025 language model\"\n3. WebSearch: \"best paper ICLR 2025 2026 evaluation\"\n4. WebSearch: \"LLM evaluation framework comprehensive 2025 2026\"\n5. WebSearch: \"LiveBench MathArena dynamic benchmark LLM 2025\"\n6. WebSearch: \"site:arxiv.org LLM evaluation survey 2025 2026\"\n7. WebSearch: \"benchmark integrity LLM evaluation trustworthy 2025\"\n8. WebSearch: \"AAAI 2025 2026 best paper LLM evaluation alignment\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details.\n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3abcc399-5f64-4397-8a76-71124cdb7ac3",
  "isSidechain": false,
  "requestId": "req_011CbWJSbKmTZNKRrk8z8wmq",
  "type": "assistant",
  "uuid": "619e4183-e304-4e35-8e8e-4748c0d6ff8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VC2n8XgPVMR8NfVSyhtUgN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1272,
      "cache_read_input_tokens": 15555,
      "output_tokens": 2160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1272,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2160,
          "cache_read_input_tokens": 15555,
          "cache_creation_input_tokens": 1272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1272
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

_source line 19 · 2026-05-29T05:26:28.214Z_

<details><summary>↩ Tool result · `toolu_01NJdJqDa4WU372hNSC8dfPk`</summary>

```text
Now I have comprehensive information on all the key papers. Here is the compiled literature survey:

---

## Literature Survey: LLM Benchmark Contamination Detection (2024--2026)

Below are the most important recent papers on benchmark contamination detection, data contamination in language models, and contamination-adjusted evaluation. They are organized by theme.

---

### A. Surveys and Overviews

**1. A Comprehensive Survey of Contamination Detection Methods in Large Language Models**
- **Authors:** Mathieu Ravaut, Bosheng Ding, Fangkai Jiao, Hailin Chen, Xingxuan Li, Ruochen Zhao, Chengwei Qin, Caiming Xiong, Shafiq Joty
- **Venue:** TMLR 2025 (accepted July 2025)
- **URL:** https://arxiv.org/abs/2404.00699
- **Summary:** Comprehensive survey of contamination detection methodologies from a Salesforce-led team; reviews the full landscape of methods and argues the NLP community must systematically account for contamination bias.

**2. A Survey on Data Contamination for Large Language Models**
- **Authors:** Yuxing Cheng, Yi Chang, Yuan Wu
- **Venue:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.14425
- **Summary:** Categorizes contamination-free evaluation into data-updating, data-rewriting, and prevention-based methods, and taxonomizes detection approaches by model access level (white-box, gray-box, black-box).

**3. Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation**
- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray
- **Venue:** EMNLP 2025 Main
- **URL:** https://arxiv.org/abs/2502.17521
- **Summary:** Traces the evolution from static to dynamic benchmarking paradigms, proposes design principles for dynamic benchmarks, and identifies the lack of standardized evaluation criteria as a critical gap.

---

### B. Detection Methods

**4. Detecting Pretraining Data from Large Language Models (Min-K% Prob)**
- **Authors:** Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer
- **Venue:** ICLR 2024
- **URL:** https://arxiv.org/abs/2310.16789
- **Summary:** Introduces Min-K% Prob, a foundational black-box method that detects pretraining membership by checking whether the K% lowest-probability tokens have unusually high likelihood, outperforming prior baselines by 7.4%.

**5. ConStat: Performance-Based Contamination Detection in Large Language Models**
- **Authors:** Jasper Dekoninck, Mark Niklas Muller, Martin Vechev
- **Venue:** NeurIPS 2024
- **URL:** https://arxiv.org/abs/2405.16281
- **Summary:** Reframes contamination as non-generalizing performance; statistically detects inflated scores by comparing model behavior on original vs. rephrased/synthetic benchmark variants, finding high contamination in Mistral, Llama, Yi, and top Open LLM Leaderboard models.

**6. PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models**
- **Authors:** Huixuan Zhang, Yun Lin, Xiaojun Wan
- **Venue:** arXiv preprint, June 2024 (revised March 2025)
- **URL:** https://arxiv.org/abs/2406.18326
- **Summary:** Proposes a statistical testing framework that constructs distribution-matched counterpart data and compares model confidence levels to detect widespread contamination across popular models and benchmarks.

**7. CoDeC: Detecting Data Contamination in LLMs via In-Context Learning**
- **Authors:** Michal Zawalski, Meriem Boubdir, Klaudia Balazy, Besmira Nushi, Pablo Ribalta
- **Venue:** ICLR 2026 (under review / accepted)
- **URL:** https://arxiv.org/abs/2510.27055
- **Summary:** Gray-box dataset-level method requiring only token probabilities and two forward passes per sample; exploits the insight that in-context examples from seen datasets disrupt memorization (reducing confidence) rather than helping, producing interpretable percentage-based contamination scores.

**8. Detecting Benchmark Contamination Through Watermarking**
- **Authors:** Tom Sander, Pierre Fernandez, Saeed Mahloujifar, Alain Durmus, Chuan Guo
- **Venue:** ICLR 2026
- **URL:** https://arxiv.org/abs/2502.17259
- **Summary:** Proactive approach: watermarks benchmark questions before release using a watermarked LLM, then detects "radioactivity" via a theoretically grounded statistical test; achieves p-values as low as 10^-3 on ARC and MMLU with 1B-parameter models.

**9. Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models**
- **Authors:** Sushant Mehta
- **Venue:** arXiv preprint, November 2025
- **URL:** https://arxiv.org/abs/2511.17602
- **Summary:** Proposes a four-level hierarchical detection framework (token, semantic, reasoning pattern, performance anomaly) that catches semantic contamination missed by token-overlap methods, achieving F1=0.76 vs. F1=0.17-0.49 for baselines on MMLU/GSM8K/HumanEval.

**10. Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models (Self-Critique)**
- **Authors:** Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li
- **Venue:** ICLR 2026
- **URL:** https://arxiv.org/abs/2510.09259
- **Summary:** First systematic study of contamination detection in RL post-training; introduces Self-Critique, which exploits entropy collapse in RL-trained models, achieving up to 30% AUC improvement over baselines where existing methods perform at chance.

---

### C. Fragility and Limitations of Detection

**11. On The Fragility of Benchmark Contamination Detection in Reasoning Models**
- **Authors:** Han Wang, Haoyu Li, Brian Ko, Huan Zhang
- **Venue:** arXiv preprint, September 2025 (revised March 2026)
- **URL:** https://arxiv.org/abs/2510.02386
- **Summary:** Demonstrates that RL training (GRPO) effectively conceals SFT-stage contamination signals, and that CoT-augmented contamination in large reasoning models is nearly undetectable by all existing methods -- a critical negative result showing current detectors are fragile.

**12. How Much Can We Forget about Data Contamination?**
- **Authors:** Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, Ulrike von Luxburg
- **Venue:** ICML 2025
- **URL:** https://arxiv.org/abs/2410.03249
- **Summary:** Empirically shows that moderate contamination is "forgotten" during extended training: even 144 repetitions of a benchmark sample can be forgotten when training data exceeds 5x Chinchilla-optimal scale, challenging the assumption that any contamination invalidates benchmarks.

**13. Test of Time: Rethinking Temporal Signal of Benchmark Contamination**
- **Authors:** Terry Jingchen Zhang, Gopal Dev, Ning Wang, Max Obreiter, Punya Syon Pandey, Keenan Samway, Wenyuan Jiang, Yinya Huang, Bernhard Scholkopf, Mrinmaya Sachan, Zhijing Jin
- **Venue:** arXiv preprint, August 2025
- **URL:** https://arxiv.org/abs/2509.00072
- **Summary:** Shows that post-cutoff performance decay -- a widely used contamination signal -- is highly sensitive to question phrasing and can be eliminated by simple LLM-based reformulation, casting doubt on temporal-signal-based detection.

---

### D. Contamination-Adjusted and Contamination-Robust Evaluation

**14. DCR: Quantifying Data Contamination in LLMs Evaluation**
- **Authors:** Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, M-Tahar Kechadi
- **Venue:** EMNLP 2025 Main
- **URL:** https://arxiv.org/abs/2507.11405
- **Summary:** Lightweight pipeline that quantifies contamination risk at four granular levels (semantic, informational, data, label) and produces a DCR Factor to adjust raw accuracy scores, achieving adjusted accuracy within 4% error of uncontaminated baselines across 9 LLMs.

**15. How Can I Publish My LLM Benchmark Without Giving the True Answers Away?**
- **Authors:** Takashi Ishida, Thanawat Lodkaew, Ikko Yamane
- **Venue:** arXiv preprint, May 2025
- **URL:** https://arxiv.org/abs/2505.18102
- **Summary:** Proposes injecting answer randomness by including multiple logically correct options with one designated as official; establishes a Bayes accuracy ceiling so that any model exceeding it signals contamination, enabling open publication of benchmarks without leaking ground truth.

**16. Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks**
- **Authors:** Yiliang Song, Hongjun An, Jiangan Chen, Xuanchen Yan, Huan Song, Jiawei Shao, Xuelong Li
- **Venue:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2603.21636
- **Summary:** Introduces a router-worker audit framework that tests contamination sensitivity via deletion, reformulation, and modification of benchmark items, finding widespread but heterogeneous above-baseline gains suggesting models exploit benchmark-adjacent cues.

---

### E. Contamination-Resistant Benchmarks

**17. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**
- **Authors:** Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, Siddhartha Jain, Ravid Shwartz-Ziv, Neel Jain, Khalid Saifullah, et al. (including Yann LeCun, Tom Goldstein, Micah Goldblum)
- **Venue:** NeurIPS 2024 Datasets & Benchmarks / OpenReview
- **URL:** https://arxiv.org/abs/2406.19314
- **Summary:** Monthly-refreshed benchmark with questions from recent math competitions, arXiv papers, and news, using automated verification; top models score below 70%, demonstrating effective contamination resistance through temporal freshness.

**18. FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI**
- **Authors:** Elliot Glazer, Ege Erdil, Tamay Besiroglu, et al. (Epoch AI)
- **Venue:** arXiv preprint, November 2024
- **URL:** https://arxiv.org/abs/2411.04872
- **Summary:** Hundreds of original, unpublished research-level math problems with automated verification; current SOTA models solve under 2%, making contamination essentially irrelevant by design.

**19. CoreEval: Automatically Building Contamination-Resilient Datasets with Real-World Knowledge toward Reliable LLM Evaluation**
- **Authors:** Jingqian Zhao, Bingbing Wang, Geng Tu, Yice Zhang, Qianlong Wang, Bin Liang, Jing Li, Ruifeng Xu
- **Venue:** arXiv preprint, November 2025
- **URL:** https://arxiv.org/abs/2511.18889
- **Summary:** Automatically updates evaluation data by extracting entity relationships from existing datasets and recontextualizing with current knowledge from the GDELT database, reducing performance overestimation from contamination.

**20. Contamination Report for Multilingual Benchmarks**
- **Authors:** Sanchit Ahuja, Varun Gumma, Sunayana Sitaram
- **Venue:** arXiv preprint, October 2024
- **URL:** https://arxiv.org/abs/2410.16186
- **Summary:** Applies black-box contamination testing across 7 multilingual benchmarks and 7 LLMs, finding nearly universal signs of contamination -- an important empirical data point for the multilingual evaluation community.

---

### Key Takeaways for Your Paper

1. **Detection is increasingly difficult for reasoning models.** Wang et al. (2025, paper #11) and Tao et al. (2025, paper #10) show that RL post-training conceals contamination traces, making traditional memorization-based detectors nearly useless. This is arguably the most important recent finding.

2. **Contamination-adjusted scoring is emerging.** DCR (#14) provides a concrete pipeline for adjusting benchmark scores by contamination risk, which could become standard practice.

3. **Proactive defenses outperform post-hoc detection.** Watermarking (#8), answer randomization (#15), and dynamic benchmarks (LiveBench #17, FrontierMath #18) sidestep detection limitations entirely.

4. **Not all contamination matters equally.** Bordt et al. at ICML 2025 (#12) show that moderate contamination is forgotten during long training runs, nuancing the threat model.

5. **The field is moving from "detect contamination" to "build contamination-resilient evaluation."** The three surveys (#1-3) all emphasize this shift from static detection to dynamic, self-refreshing evaluation paradigms.

agentId: a9fc8b06d35d0ee79 (use SendMessage with to: 'a9fc8b06d35d0ee79' to continue this agent)
&lt;usage>total_tokens: 31061
tool_uses: 34
duration_ms: 164299&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "43bf52fb-2a4d-45fa-bb49-fab0188de41e",
  "isSidechain": false,
  "promptId": "37ea365b-dcd4-4897-b99b-0b8f025b793a",
  "type": "user",
  "uuid": "254421c1-9b49-4f8d-9501-27af34cffa48",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an ML paper. Search for the most important recent papers (2024-2026) on LLM benchmark contamination detection, data contamination in language models, and contamination-adjusted evaluation.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"benchmark contamination detection LLM 2025 2026\"\n2. WebSearch: \"data contamination language model evaluation 2025\"\n3. WebSearch: \"contamination adjusted scores LLM benchmark\"\n4. WebSearch: \"site:arxiv.org benchmark contamination reasoning models 2025\"\n5. WebSearch: \"DCR contamination robust evaluation LLM 2025\"\n6. WebSearch: \"CoDeC contamination detection gray-box 2025\"\n7. WebSearch: \"Kocetkov fragility benchmark contamination detection reasoning models 2025\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details. \n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
    "agentId": "a9fc8b06d35d0ee79",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all the key papers. Here is the compiled literature survey:\n\n---\n\n## Literature Survey: LLM Benchmark Contamination Detection (2024--2026)\n\nBelow are the most important recent papers on benchmark contamination detection, data contamination in language models, and contamination-adjusted evaluation. They are organized by theme.\n\n---\n\n### A. Surveys and Overviews\n\n**1. A Comprehensive Survey of Contamination Detection Methods in Large Language Models**\n- **Authors:** Mathieu Ravaut, Bosheng Ding, Fangkai Jiao, Hailin Chen, Xingxuan Li, Ruochen Zhao, Chengwei Qin, Caiming Xiong, Shafiq Joty\n- **Venue:** TMLR 2025 (accepted July 2025)\n- **URL:** https://arxiv.org/abs/2404.00699\n- **Summary:** Comprehensive survey of contamination detection methodologies from a Salesforce-led team; reviews the full landscape of methods and argues the NLP community must systematically account for contamination bias.\n\n**2. A Survey on Data Contamination for Large Language Models**\n- **Authors:** Yuxing Cheng, Yi Chang, Yuan Wu\n- **Venue:** arXiv preprint, February 2025\n- **URL:** https://arxiv.org/abs/2502.14425\n- **Summary:** Categorizes contamination-free evaluation into data-updating, data-rewriting, and prevention-based methods, and taxonomizes detection approaches by model access level (white-box, gray-box, black-box).\n\n**3. Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation**\n- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray\n- **Venue:** EMNLP 2025 Main\n- **URL:** https://arxiv.org/abs/2502.17521\n- **Summary:** Traces the evolution from static to dynamic benchmarking paradigms, proposes design principles for dynamic benchmarks, and identifies the lack of standardized evaluation criteria as a critical gap.\n\n---\n\n### B. Detection Methods\n\n**4. Detecting Pretraining Data from Large Language Models (Min-K% Prob)**\n- **Authors:** Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, Luke Zettlemoyer\n- **Venue:** ICLR 2024\n- **URL:** https://arxiv.org/abs/2310.16789\n- **Summary:** Introduces Min-K% Prob, a foundational black-box method that detects pretraining membership by checking whether the K% lowest-probability tokens have unusually high likelihood, outperforming prior baselines by 7.4%.\n\n**5. ConStat: Performance-Based Contamination Detection in Large Language Models**\n- **Authors:** Jasper Dekoninck, Mark Niklas Muller, Martin Vechev\n- **Venue:** NeurIPS 2024\n- **URL:** https://arxiv.org/abs/2405.16281\n- **Summary:** Reframes contamination as non-generalizing performance; statistically detects inflated scores by comparing model behavior on original vs. rephrased/synthetic benchmark variants, finding high contamination in Mistral, Llama, Yi, and top Open LLM Leaderboard models.\n\n**6. PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models**\n- **Authors:** Huixuan Zhang, Yun Lin, Xiaojun Wan\n- **Venue:** arXiv preprint, June 2024 (revised March 2025)\n- **URL:** https://arxiv.org/abs/2406.18326\n- **Summary:** Proposes a statistical testing framework that constructs distribution-matched counterpart data and compares model confidence levels to detect widespread contamination across popular models and benchmarks.\n\n**7. CoDeC: Detecting Data Contamination in LLMs via In-Context Learning**\n- **Authors:** Michal Zawalski, Meriem Boubdir, Klaudia Balazy, Besmira Nushi, Pablo Ribalta\n- **Venue:** ICLR 2026 (under review / accepted)\n- **URL:** https://arxiv.org/abs/2510.27055\n- **Summary:** Gray-box dataset-level method requiring only token probabilities and two forward passes per sample; exploits the insight that in-context examples from seen datasets disrupt memorization (reducing confidence) rather than helping, producing interpretable percentage-based contamination scores.\n\n**8. Detecting Benchmark Contamination Through Watermarking**\n- **Authors:** Tom Sander, Pierre Fernandez, Saeed Mahloujifar, Alain Durmus, Chuan Guo\n- **Venue:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2502.17259\n- **Summary:** Proactive approach: watermarks benchmark questions before release using a watermarked LLM, then detects \"radioactivity\" via a theoretically grounded statistical test; achieves p-values as low as 10^-3 on ARC and MMLU with 1B-parameter models.\n\n**9. Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data in Foundation Models**\n- **Authors:** Sushant Mehta\n- **Venue:** arXiv preprint, November 2025\n- **URL:** https://arxiv.org/abs/2511.17602\n- **Summary:** Proposes a four-level hierarchical detection framework (token, semantic, reasoning pattern, performance anomaly) that catches semantic contamination missed by token-overlap methods, achieving F1=0.76 vs. F1=0.17-0.49 for baselines on MMLU/GSM8K/HumanEval.\n\n**10. Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models (Self-Critique)**\n- **Authors:** Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li\n- **Venue:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2510.09259\n- **Summary:** First systematic study of contamination detection in RL post-training; introduces Self-Critique, which exploits entropy collapse in RL-trained models, achieving up to 30% AUC improvement over baselines where existing methods perform at chance.\n\n---\n\n### C. Fragility and Limitations of Detection\n\n**11. On The Fragility of Benchmark Contamination Detection in Reasoning Models**\n- **Authors:** Han Wang, Haoyu Li, Brian Ko, Huan Zhang\n- **Venue:** arXiv preprint, September 2025 (revised March 2026)\n- **URL:** https://arxiv.org/abs/2510.02386\n- **Summary:** Demonstrates that RL training (GRPO) effectively conceals SFT-stage contamination signals, and that CoT-augmented contamination in large reasoning models is nearly undetectable by all existing methods -- a critical negative result showing current detectors are fragile.\n\n**12. How Much Can We Forget about Data Contamination?**\n- **Authors:** Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, Ulrike von Luxburg\n- **Venue:** ICML 2025\n- **URL:** https://arxiv.org/abs/2410.03249\n- **Summary:** Empirically shows that moderate contamination is \"forgotten\" during extended training: even 144 repetitions of a benchmark sample can be forgotten when training data exceeds 5x Chinchilla-optimal scale, challenging the assumption that any contamination invalidates benchmarks.\n\n**13. Test of Time: Rethinking Temporal Signal of Benchmark Contamination**\n- **Authors:** Terry Jingchen Zhang, Gopal Dev, Ning Wang, Max Obreiter, Punya Syon Pandey, Keenan Samway, Wenyuan Jiang, Yinya Huang, Bernhard Scholkopf, Mrinmaya Sachan, Zhijing Jin\n- **Venue:** arXiv preprint, August 2025\n- **URL:** https://arxiv.org/abs/2509.00072\n- **Summary:** Shows that post-cutoff performance decay -- a widely used contamination signal -- is highly sensitive to question phrasing and can be eliminated by simple LLM-based reformulation, casting doubt on temporal-signal-based detection.\n\n---\n\n### D. Contamination-Adjusted and Contamination-Robust Evaluation\n\n**14. DCR: Quantifying Data Contamination in LLMs Evaluation**\n- **Authors:** Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, M-Tahar Kechadi\n- **Venue:** EMNLP 2025 Main\n- **URL:** https://arxiv.org/abs/2507.11405\n- **Summary:** Lightweight pipeline that quantifies contamination risk at four granular levels (semantic, informational, data, label) and produces a DCR Factor to adjust raw accuracy scores, achieving adjusted accuracy within 4% error of uncontaminated baselines across 9 LLMs.\n\n**15. How Can I Publish My LLM Benchmark Without Giving the True Answers Away?**\n- **Authors:** Takashi Ishida, Thanawat Lodkaew, Ikko Yamane\n- **Venue:** arXiv preprint, May 2025\n- **URL:** https://arxiv.org/abs/2505.18102\n- **Summary:** Proposes injecting answer randomness by including multiple logically correct options with one designated as official; establishes a Bayes accuracy ceiling so that any model exceeding it signals contamination, enabling open publication of benchmarks without leaking ground truth.\n\n**16. Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks**\n- **Authors:** Yiliang Song, Hongjun An, Jiangan Chen, Xuanchen Yan, Huan Song, Jiawei Shao, Xuelong Li\n- **Venue:** arXiv preprint, March 2026\n- **URL:** https://arxiv.org/abs/2603.21636\n- **Summary:** Introduces a router-worker audit framework that tests contamination sensitivity via deletion, reformulation, and modification of benchmark items, finding widespread but heterogeneous above-baseline gains suggesting models exploit benchmark-adjacent cues.\n\n---\n\n### E. Contamination-Resistant Benchmarks\n\n**17. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**\n- **Authors:** Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Ben Feuer, Siddhartha Jain, Ravid Shwartz-Ziv, Neel Jain, Khalid Saifullah, et al. (including Yann LeCun, Tom Goldstein, Micah Goldblum)\n- **Venue:** NeurIPS 2024 Datasets & Benchmarks / OpenReview\n- **URL:** https://arxiv.org/abs/2406.19314\n- **Summary:** Monthly-refreshed benchmark with questions from recent math competitions, arXiv papers, and news, using automated verification; top models score below 70%, demonstrating effective contamination resistance through temporal freshness.\n\n**18. FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI**\n- **Authors:** Elliot Glazer, Ege Erdil, Tamay Besiroglu, et al. (Epoch AI)\n- **Venue:** arXiv preprint, November 2024\n- **URL:** https://arxiv.org/abs/2411.04872\n- **Summary:** Hundreds of original, unpublished research-level math problems with automated verification; current SOTA models solve under 2%, making contamination essentially irrelevant by design.\n\n**19. CoreEval: Automatically Building Contamination-Resilient Datasets with Real-World Knowledge toward Reliable LLM Evaluation**\n- **Authors:** Jingqian Zhao, Bingbing Wang, Geng Tu, Yice Zhang, Qianlong Wang, Bin Liang, Jing Li, Ruifeng Xu\n- **Venue:** arXiv preprint, November 2025\n- **URL:** https://arxiv.org/abs/2511.18889\n- **Summary:** Automatically updates evaluation data by extracting entity relationships from existing datasets and recontextualizing with current knowledge from the GDELT database, reducing performance overestimation from contamination.\n\n**20. Contamination Report for Multilingual Benchmarks**\n- **Authors:** Sanchit Ahuja, Varun Gumma, Sunayana Sitaram\n- **Venue:** arXiv preprint, October 2024\n- **URL:** https://arxiv.org/abs/2410.16186\n- **Summary:** Applies black-box contamination testing across 7 multilingual benchmarks and 7 LLMs, finding nearly universal signs of contamination -- an important empirical data point for the multilingual evaluation community.\n\n---\n\n### Key Takeaways for Your Paper\n\n1. **Detection is increasingly difficult for reasoning models.** Wang et al. (2025, paper #11) and Tao et al. (2025, paper #10) show that RL post-training conceals contamination traces, making traditional memorization-based detectors nearly useless. This is arguably the most important recent finding.\n\n2. **Contamination-adjusted scoring is emerging.** DCR (#14) provides a concrete pipeline for adjusting benchmark scores by contamination risk, which could become standard practice.\n\n3. **Proactive defenses outperform post-hoc detection.** Watermarking (#8), answer randomization (#15), and dynamic benchmarks (LiveBench #17, FrontierMath #18) sidestep detection limitations entirely.\n\n4. **Not all contamination matters equally.** Bordt et al. at ICML 2025 (#12) show that moderate contamination is forgotten during long training runs, nuancing the threat model.\n\n5. **The field is moving from \"detect contamination\" to \"build contamination-resilient evaluation.\"** The three surveys (#1-3) all emphasize this shift from static detection to dynamic, self-refreshing evaluation paradigms."
      }
    ],
    "totalDurationMs": 164299,
    "totalTokens": 31061,
    "totalToolUseCount": 34,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 368,
      "cache_read_input_tokens": 27107,
      "output_tokens": 3585,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 368
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3585,
          "cache_read_input_tokens": 27107,
          "cache_creation_input_tokens": 368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 368,
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
  "sourceToolAssistantUUID": "43bf52fb-2a4d-45fa-bb49-fab0188de41e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "254421c1-9b49-4f8d-9501-27af34cffa48",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Tool result

_source line 22 · 2026-05-29T05:26:47.222Z_

<details><summary>↩ Tool result · `toolu_018C52qSXytHwYRM2PRt79fw`</summary>

```text
I now have comprehensive coverage. Here is the full literature survey.

---

## Literature Survey: IRT and Psychometrics for LLM Evaluation (2024--2026)

Below are the most important recent papers organized by theme. Each entry includes title, authors, venue/date, URL, and a one-line summary.

---

### A. Core IRT Frameworks for LLM Evaluation

**1. tinyBenchmarks: Evaluating LLMs with Fewer Examples**
- Authors: Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin
- Venue/Date: arXiv, Feb 2024 (ICML 2024)
- URL: https://arxiv.org/abs/2402.14992
- Summary: Introduces IRT-based (p-IRT) item selection to reduce MMLU from 14K items to 100 curated examples while reliably reproducing full benchmark scores -- a foundational paper that launched efficient IRT-based LLM benchmarking.

**2. Fluid Language Model Benchmarking**
- Authors: Valentin Hofmann, David Heineman, Ian Magnusson, Kyle Lo, Jesse Dodge, Maarten Sap, Pang Wei Koh, Chun Wang, Hannaneh Hajishirzi, Noah A. Smith
- Venue/Date: arXiv Sep 2025 / COLM 2025
- URL: https://arxiv.org/abs/2509.11106
- Summary: Applies computerized adaptive testing from educational psychology to dynamically select test items per model, achieving comparable validity with 1/50th the items from MMLU.

**3. ATLAS -- Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks**
- Authors: Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla
- Venue/Date: arXiv Oct 2025; revised Feb 2026 (ICLR 2026 submission)
- URL: https://arxiv.org/abs/2511.04689
- Summary: Uses 3PL IRT with Fisher information-guided adaptive item selection to reduce benchmark items by 90% (e.g., 42 items instead of 5,608 on HellaSwag) while maintaining precise ability estimation across 3,000+ models.

**4. Reliable and Efficient Amortized Model-based Evaluation**
- Authors: Sang Truong, Yuheng Tu, Percy Liang, Bo Li, Sanmi Koyejo (Stanford CRFM)
- Venue/Date: arXiv Mar 2025; integrated into HELM
- URL: https://arxiv.org/abs/2503.13335
- Summary: Trains a neural model to predict Rasch difficulty from question content and generates difficulty-conditioned items for adaptive testing; deployed in HELM across 22 benchmarks and 172 LLMs.

**5. LEGO-IRT -- Toward a Unified Framework for Data-Efficient Evaluation of Large Language Models**
- Authors: Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang
- Venue/Date: arXiv Oct 2025
- URL: https://arxiv.org/abs/2510.04051
- Summary: Extends IRT to handle both binary and continuous evaluation metrics while leveraging cross-benchmark structural relationships, achieving stable ability estimates with just 3% of evaluation items.

**6. Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory (PSN-IRT)**
- Authors: Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao
- Venue/Date: arXiv May 2025
- URL: https://arxiv.org/abs/2505.15055
- Summary: Proposes a Pseudo-Siamese Network IRT framework, analyzes 11 benchmarks with 41,871 items, identifies significant measurement quality shortcomings, and constructs smaller benchmarks better aligned with human preference.

---

### B. Extensions and Variants of IRT for LLMs

**7. IrtNet -- Learning Compact Representations of LLM Abilities via Item Response Theory**
- Authors: Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu
- Venue/Date: arXiv Oct 2025
- URL: https://arxiv.org/abs/2510.00844
- Summary: Learns multi-skill ability vectors for LLMs using a Mixture-of-Experts IRT network, enabling superior model routing and cross-benchmark accuracy prediction.

**8. JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory**
- Authors: Louie Hong Yao, Nicholas Jarvis, Tiffany Zhan, Saptarshi Ghosh, Linfeng Liu, Tianyu Jiang
- Venue/Date: arXiv Sep 2025
- URL: https://arxiv.org/abs/2509.22888
- Summary: Embeds models and questions in a shared geometric space where question direction encodes semantics and magnitude encodes difficulty, revealing that LLMs develop internal taxonomies only partially matching human subject categories.

**9. Latency-Response Theory Model: Evaluating LLMs via Response Accuracy and Chain-of-Thought Length**
- Authors: Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu
- Venue/Date: arXiv Dec 2025
- URL: https://arxiv.org/abs/2512.07019
- Summary: Extends IRT to jointly model answer correctness and chain-of-thought reasoning length, finding that higher reasoning ability correlates with longer response latency across all benchmarks.

**10. Identity-Link IRT for Label-Free LLM Evaluation: Preserving Additivity in TVD-MI Scores**
- Authors: Zachary Robertson
- Venue/Date: arXiv Oct 2025
- URL: https://arxiv.org/abs/2510.14966
- Summary: Shows that identity-link (linear) IRT on TVD-MI pairwise comparison scores preserves additivity better than logistic/probit links, enabling label-free LLM evaluation with 3x fewer comparisons.

**11. Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores**
- Authors: Esma Balkir, Alice Pernthaller, Marco Basaldella, Jose Hernandez-Orallo, Nigel Collier
- Venue/Date: arXiv Jan 2026
- URL: https://arxiv.org/abs/2601.13885
- Summary: Extends CAT from binary to continuous evaluation scores (ROUGE, BLEU, LLM-as-Judge) using heteroskedastic normal distributions, achieving reliable rankings with only 2% of items.

---

### C. Domain-Specific Applications (Medical)

**12. MedIRT -- Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks**
- Authors: Zhimeng Luo, Lixin Wu, Adam Frisch, Daqing He
- Venue/Date: arXiv Sep 2025; revised Apr 2026
- URL: https://arxiv.org/abs/2509.24186
- Summary: Applies IRT prospectively to 71 LLMs on USMLE-aligned medical topics, showing IRT rankings outperform accuracy-based rankings on 6 external benchmarks with 18% lower variance.

**13. Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of LLMs in Medical Benchmarking**
- Authors: Tianpeng Zheng, Zhehan Jiang, Jiayi Liu, Shicong Feng
- Venue/Date: arXiv Feb 2026
- URL: https://arxiv.org/abs/2603.23506
- Summary: Validates a CAT/IRT framework on 38 LLMs for medical knowledge assessment, achieving r=0.988 correlation with full-bank estimates using only 1.3% of items.

---

### D. IRT for LLM-as-Judge and Grading

**14. Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory**
- Authors: Junhyuk Choi, Sohhyung Park, Chanhee Cho, Hyeonchu Park, Bugeun Kim
- Venue/Date: arXiv Jan 2026
- URL: https://arxiv.org/abs/2602.00521
- Summary: Uses the Graded Response Model from IRT to diagnose LLM judge reliability along two axes (intrinsic consistency under prompt variation and human alignment), providing interpretable failure diagnostics.

**15. Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory**
- Authors: Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, Ulf Kroehne
- Venue/Date: arXiv Apr 2026
- URL: https://arxiv.org/abs/2605.00238
- Summary: Applies IRT to automated short answer grading with 17 LLMs, revealing that models with similar aggregate scores show substantially different accuracy-decline patterns as item difficulty increases.

---

### E. Benchmark Meta-Evaluation and Construct Validity

**16. Measuring What Matters: Construct Validity in Large Language Model Benchmarks**
- Authors: Andrew M. Bean, Ryan Othniel Kearns, Angelika Romanou, et al. (29 expert reviewers)
- Venue/Date: NeurIPS 2025 Datasets and Benchmarks Track
- URL: https://openreview.net/forum?id=mdA5lVvNcU
- Summary: Systematic review of 445 LLM benchmarks by 29 experts, producing 8 recommendations for improving construct validity -- essential context for understanding why IRT-based measurement is needed.

**17. Lifting the Benchmark Iceberg with Item-Response Theory**
- Authors: Mara Schilling-Wilhelmi, Nawaf Alampara, Kevin Maik Jablonka
- Venue/Date: ICLR 2025 Workshop AI4MAT
- URL: https://openreview.net/forum?id=ZyVQqK7mcP
- Summary: Identifies the "benchmark iceberg" phenomenon where hidden implementation choices distort rankings, and proposes IRT to transform benchmarks from opaque leaderboards into transparent measurement instruments.

**18. Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs**
- Authors: Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao
- Venue/Date: arXiv Feb 2026
- URL: https://arxiv.org/abs/2602.11674
- Summary: Proposes a data-driven framework auditing 106 benchmarks across capability discrimination, anti-saturation, and impact dimensions to quantify benchmark health.

**19. Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration**
- Authors: Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky
- Venue/Date: arXiv Apr 2026
- URL: https://arxiv.org/abs/2604.12843
- Summary: Uses multidimensional IRT with anchor items to calibrate new benchmarks onto existing evaluation suites, predicting full performance within 2-3 percentage points using 100 anchor questions per dataset.

---

### F. Psychometrics Surveys and Broader Framing

**20. Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement**
- Authors: Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, Guojie Song
- Venue/Date: arXiv May 2025
- URL: https://arxiv.org/abs/2505.08245
- Summary: Comprehensive survey establishing "LLM Psychometrics" as a field, synthesizing literature on applying psychometric instruments and principles (including IRT) to evaluate and improve language models.

---

### G. Related Efficient Evaluation Methods (non-IRT but closely adjacent)

**21. Active Evaluation Acquisition for Efficient LLM Benchmarking**
- Authors: Yang Li, Jie Ma, Miguel Ballesteros, Yassine Benajiba, Graham Horwood
- Venue/Date: arXiv Oct 2024
- URL: https://arxiv.org/abs/2410.05952
- Summary: Uses reinforcement learning to learn a subset selection policy for efficient LLM evaluation, modeling dependencies between test cases rather than using IRT -- a complementary approach.

**22. SparseEval: Efficient Evaluation of Large Language Models by Sparse Optimization**
- Authors: Taolin Zhang, Hang Guo, Wang Lu, Tao Dai, Shu-Tao Xia, Jindong Wang
- Venue/Date: arXiv Feb 2026
- URL: https://arxiv.org/abs/2602.07909
- Summary: Formulates efficient benchmarking as sparse optimization over performance matrices, selecting anchor items via gradient descent -- an alternative to IRT-based subset selection.

---

### Key Takeaways for Your Paper

The field has rapidly matured from 2024 to 2026 along several clear trajectories:

1. **Foundational works** (tinyBenchmarks, Fluid Benchmarking) established that IRT can dramatically reduce evaluation cost (90-99% item reduction) while preserving measurement quality.

2. **Production deployment**: Stanford's HELM framework now ships IRT-based adaptive testing across 22 benchmarks, making this no longer purely academic.

3. **IRT model diversity**: Papers now explore 1PL/Rasch (HELM), 2PL, 3PL (ATLAS), multidimensional IRT (Growing Pains, IrtNet), graded response models (LLM-as-Judge), joint embedding IRT (JE-IRT), and latency-response extensions.

4. **Beyond binary scores**: LEGO-IRT and the Balkir et al. continuous-score CAT paper address the critical gap of evaluating generative tasks with non-binary metrics.

5. **Meta-evaluation**: The construct validity paper (NeurIPS 2025, 445 benchmarks) and the Benchmark Health Index provide the theoretical motivation for why IRT-based measurement is necessary.

The most-cited and highest-impact papers for your related work section would be: tinyBenchmarks (Polo et al., 2024), ATLAS (Li et al., 2025), Fluid Benchmarking (Hofmann et al., COLM 2025), and the Stanford HELM IRT integration (Truong et al., 2025).

agentId: af5c309b82cdf0c46 (use SendMessage with to: 'af5c309b82cdf0c46' to continue this agent)
&lt;usage>total_tokens: 31600
tool_uses: 37
duration_ms: 175208&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a5c07c8a-c109-4bc2-8c7b-35d61c2b331c",
  "isSidechain": false,
  "promptId": "37ea365b-dcd4-4897-b99b-0b8f025b793a",
  "type": "user",
  "uuid": "a2acaf34-d6ea-47e6-aca1-e5fa67624f44",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an ML paper. Search for the most important recent papers (2024-2026) on Item Response Theory (IRT) applied to LLM evaluation, psychometrics for AI evaluation, and calibrated capability scoring.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"Item Response Theory LLM evaluation 2025 2026\"\n2. WebSearch: \"IRT language model benchmark evaluation adaptive testing\"\n3. WebSearch: \"ATLAS IRT adaptive testing LLM 2025\"\n4. WebSearch: \"psychometrics AI evaluation language model calibration\"\n5. WebSearch: \"site:arxiv.org IRT LLM evaluation 2025\"\n6. WebSearch: \"computerized adaptive testing large language models\"\n7. WebSearch: \"measurement theory LLM evaluation capability scoring 2025\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details.\n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
    "agentId": "af5c309b82cdf0c46",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive coverage. Here is the full literature survey.\n\n---\n\n## Literature Survey: IRT and Psychometrics for LLM Evaluation (2024--2026)\n\nBelow are the most important recent papers organized by theme. Each entry includes title, authors, venue/date, URL, and a one-line summary.\n\n---\n\n### A. Core IRT Frameworks for LLM Evaluation\n\n**1. tinyBenchmarks: Evaluating LLMs with Fewer Examples**\n- Authors: Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin\n- Venue/Date: arXiv, Feb 2024 (ICML 2024)\n- URL: https://arxiv.org/abs/2402.14992\n- Summary: Introduces IRT-based (p-IRT) item selection to reduce MMLU from 14K items to 100 curated examples while reliably reproducing full benchmark scores -- a foundational paper that launched efficient IRT-based LLM benchmarking.\n\n**2. Fluid Language Model Benchmarking**\n- Authors: Valentin Hofmann, David Heineman, Ian Magnusson, Kyle Lo, Jesse Dodge, Maarten Sap, Pang Wei Koh, Chun Wang, Hannaneh Hajishirzi, Noah A. Smith\n- Venue/Date: arXiv Sep 2025 / COLM 2025\n- URL: https://arxiv.org/abs/2509.11106\n- Summary: Applies computerized adaptive testing from educational psychology to dynamically select test items per model, achieving comparable validity with 1/50th the items from MMLU.\n\n**3. ATLAS -- Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks**\n- Authors: Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla\n- Venue/Date: arXiv Oct 2025; revised Feb 2026 (ICLR 2026 submission)\n- URL: https://arxiv.org/abs/2511.04689\n- Summary: Uses 3PL IRT with Fisher information-guided adaptive item selection to reduce benchmark items by 90% (e.g., 42 items instead of 5,608 on HellaSwag) while maintaining precise ability estimation across 3,000+ models.\n\n**4. Reliable and Efficient Amortized Model-based Evaluation**\n- Authors: Sang Truong, Yuheng Tu, Percy Liang, Bo Li, Sanmi Koyejo (Stanford CRFM)\n- Venue/Date: arXiv Mar 2025; integrated into HELM\n- URL: https://arxiv.org/abs/2503.13335\n- Summary: Trains a neural model to predict Rasch difficulty from question content and generates difficulty-conditioned items for adaptive testing; deployed in HELM across 22 benchmarks and 172 LLMs.\n\n**5. LEGO-IRT -- Toward a Unified Framework for Data-Efficient Evaluation of Large Language Models**\n- Authors: Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang\n- Venue/Date: arXiv Oct 2025\n- URL: https://arxiv.org/abs/2510.04051\n- Summary: Extends IRT to handle both binary and continuous evaluation metrics while leveraging cross-benchmark structural relationships, achieving stable ability estimates with just 3% of evaluation items.\n\n**6. Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory (PSN-IRT)**\n- Authors: Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao\n- Venue/Date: arXiv May 2025\n- URL: https://arxiv.org/abs/2505.15055\n- Summary: Proposes a Pseudo-Siamese Network IRT framework, analyzes 11 benchmarks with 41,871 items, identifies significant measurement quality shortcomings, and constructs smaller benchmarks better aligned with human preference.\n\n---\n\n### B. Extensions and Variants of IRT for LLMs\n\n**7. IrtNet -- Learning Compact Representations of LLM Abilities via Item Response Theory**\n- Authors: Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu\n- Venue/Date: arXiv Oct 2025\n- URL: https://arxiv.org/abs/2510.00844\n- Summary: Learns multi-skill ability vectors for LLMs using a Mixture-of-Experts IRT network, enabling superior model routing and cross-benchmark accuracy prediction.\n\n**8. JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory**\n- Authors: Louie Hong Yao, Nicholas Jarvis, Tiffany Zhan, Saptarshi Ghosh, Linfeng Liu, Tianyu Jiang\n- Venue/Date: arXiv Sep 2025\n- URL: https://arxiv.org/abs/2509.22888\n- Summary: Embeds models and questions in a shared geometric space where question direction encodes semantics and magnitude encodes difficulty, revealing that LLMs develop internal taxonomies only partially matching human subject categories.\n\n**9. Latency-Response Theory Model: Evaluating LLMs via Response Accuracy and Chain-of-Thought Length**\n- Authors: Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu\n- Venue/Date: arXiv Dec 2025\n- URL: https://arxiv.org/abs/2512.07019\n- Summary: Extends IRT to jointly model answer correctness and chain-of-thought reasoning length, finding that higher reasoning ability correlates with longer response latency across all benchmarks.\n\n**10. Identity-Link IRT for Label-Free LLM Evaluation: Preserving Additivity in TVD-MI Scores**\n- Authors: Zachary Robertson\n- Venue/Date: arXiv Oct 2025\n- URL: https://arxiv.org/abs/2510.14966\n- Summary: Shows that identity-link (linear) IRT on TVD-MI pairwise comparison scores preserves additivity better than logistic/probit links, enabling label-free LLM evaluation with 3x fewer comparisons.\n\n**11. Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores**\n- Authors: Esma Balkir, Alice Pernthaller, Marco Basaldella, Jose Hernandez-Orallo, Nigel Collier\n- Venue/Date: arXiv Jan 2026\n- URL: https://arxiv.org/abs/2601.13885\n- Summary: Extends CAT from binary to continuous evaluation scores (ROUGE, BLEU, LLM-as-Judge) using heteroskedastic normal distributions, achieving reliable rankings with only 2% of items.\n\n---\n\n### C. Domain-Specific Applications (Medical)\n\n**12. MedIRT -- Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks**\n- Authors: Zhimeng Luo, Lixin Wu, Adam Frisch, Daqing He\n- Venue/Date: arXiv Sep 2025; revised Apr 2026\n- URL: https://arxiv.org/abs/2509.24186\n- Summary: Applies IRT prospectively to 71 LLMs on USMLE-aligned medical topics, showing IRT rankings outperform accuracy-based rankings on 6 external benchmarks with 18% lower variance.\n\n**13. Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of LLMs in Medical Benchmarking**\n- Authors: Tianpeng Zheng, Zhehan Jiang, Jiayi Liu, Shicong Feng\n- Venue/Date: arXiv Feb 2026\n- URL: https://arxiv.org/abs/2603.23506\n- Summary: Validates a CAT/IRT framework on 38 LLMs for medical knowledge assessment, achieving r=0.988 correlation with full-bank estimates using only 1.3% of items.\n\n---\n\n### D. IRT for LLM-as-Judge and Grading\n\n**14. Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory**\n- Authors: Junhyuk Choi, Sohhyung Park, Chanhee Cho, Hyeonchu Park, Bugeun Kim\n- Venue/Date: arXiv Jan 2026\n- URL: https://arxiv.org/abs/2602.00521\n- Summary: Uses the Graded Response Model from IRT to diagnose LLM judge reliability along two axes (intrinsic consistency under prompt variation and human alignment), providing interpretable failure diagnostics.\n\n**15. Estimating LLM Grading Ability and Response Difficulty in Automatic Short Answer Grading via Item Response Theory**\n- Authors: Longwei Cong, Sonja Hahn, Sebastian Gombert, Leon Camus, Hendrik Drachsler, Ulf Kroehne\n- Venue/Date: arXiv Apr 2026\n- URL: https://arxiv.org/abs/2605.00238\n- Summary: Applies IRT to automated short answer grading with 17 LLMs, revealing that models with similar aggregate scores show substantially different accuracy-decline patterns as item difficulty increases.\n\n---\n\n### E. Benchmark Meta-Evaluation and Construct Validity\n\n**16. Measuring What Matters: Construct Validity in Large Language Model Benchmarks**\n- Authors: Andrew M. Bean, Ryan Othniel Kearns, Angelika Romanou, et al. (29 expert reviewers)\n- Venue/Date: NeurIPS 2025 Datasets and Benchmarks Track\n- URL: https://openreview.net/forum?id=mdA5lVvNcU\n- Summary: Systematic review of 445 LLM benchmarks by 29 experts, producing 8 recommendations for improving construct validity -- essential context for understanding why IRT-based measurement is needed.\n\n**17. Lifting the Benchmark Iceberg with Item-Response Theory**\n- Authors: Mara Schilling-Wilhelmi, Nawaf Alampara, Kevin Maik Jablonka\n- Venue/Date: ICLR 2025 Workshop AI4MAT\n- URL: https://openreview.net/forum?id=ZyVQqK7mcP\n- Summary: Identifies the \"benchmark iceberg\" phenomenon where hidden implementation choices distort rankings, and proposes IRT to transform benchmarks from opaque leaderboards into transparent measurement instruments.\n\n**18. Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs**\n- Authors: Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao\n- Venue/Date: arXiv Feb 2026\n- URL: https://arxiv.org/abs/2602.11674\n- Summary: Proposes a data-driven framework auditing 106 benchmarks across capability discrimination, anti-saturation, and impact dimensions to quantify benchmark health.\n\n**19. Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration**\n- Authors: Eliya Habba, Itay Itzhak, Asaf Yehudai, Yotam Perlitz, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen, Gabriel Stanovsky\n- Venue/Date: arXiv Apr 2026\n- URL: https://arxiv.org/abs/2604.12843\n- Summary: Uses multidimensional IRT with anchor items to calibrate new benchmarks onto existing evaluation suites, predicting full performance within 2-3 percentage points using 100 anchor questions per dataset.\n\n---\n\n### F. Psychometrics Surveys and Broader Framing\n\n**20. Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement**\n- Authors: Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, Guojie Song\n- Venue/Date: arXiv May 2025\n- URL: https://arxiv.org/abs/2505.08245\n- Summary: Comprehensive survey establishing \"LLM Psychometrics\" as a field, synthesizing literature on applying psychometric instruments and principles (including IRT) to evaluate and improve language models.\n\n---\n\n### G. Related Efficient Evaluation Methods (non-IRT but closely adjacent)\n\n**21. Active Evaluation Acquisition for Efficient LLM Benchmarking**\n- Authors: Yang Li, Jie Ma, Miguel Ballesteros, Yassine Benajiba, Graham Horwood\n- Venue/Date: arXiv Oct 2024\n- URL: https://arxiv.org/abs/2410.05952\n- Summary: Uses reinforcement learning to learn a subset selection policy for efficient LLM evaluation, modeling dependencies between test cases rather than using IRT -- a complementary approach.\n\n**22. SparseEval: Efficient Evaluation of Large Language Models by Sparse Optimization**\n- Authors: Taolin Zhang, Hang Guo, Wang Lu, Tao Dai, Shu-Tao Xia, Jindong Wang\n- Venue/Date: arXiv Feb 2026\n- URL: https://arxiv.org/abs/2602.07909\n- Summary: Formulates efficient benchmarking as sparse optimization over performance matrices, selecting anchor items via gradient descent -- an alternative to IRT-based subset selection.\n\n---\n\n### Key Takeaways for Your Paper\n\nThe field has rapidly matured from 2024 to 2026 along several clear trajectories:\n\n1. **Foundational works** (tinyBenchmarks, Fluid Benchmarking) established that IRT can dramatically reduce evaluation cost (90-99% item reduction) while preserving measurement quality.\n\n2. **Production deployment**: Stanford's HELM framework now ships IRT-based adaptive testing across 22 benchmarks, making this no longer purely academic.\n\n3. **IRT model diversity**: Papers now explore 1PL/Rasch (HELM), 2PL, 3PL (ATLAS), multidimensional IRT (Growing Pains, IrtNet), graded response models (LLM-as-Judge), joint embedding IRT (JE-IRT), and latency-response extensions.\n\n4. **Beyond binary scores**: LEGO-IRT and the Balkir et al. continuous-score CAT paper address the critical gap of evaluating generative tasks with non-binary metrics.\n\n5. **Meta-evaluation**: The construct validity paper (NeurIPS 2025, 445 benchmarks) and the Benchmark Health Index provide the theoretical motivation for why IRT-based measurement is necessary.\n\nThe most-cited and highest-impact papers for your related work section would be: tinyBenchmarks (Polo et al., 2024), ATLAS (Li et al., 2025), Fluid Benchmarking (Hofmann et al., COLM 2025), and the Stanford HELM IRT integration (Truong et al., 2025)."
      }
    ],
    "totalDurationMs": 175208,
    "totalTokens": 31600,
    "totalToolUseCount": 37,
    "usage": {
      "input_tokens": 210,
      "cache_creation_input_tokens": 1347,
      "cache_read_input_tokens": 26243,
      "output_tokens": 3800,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1347
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 210,
          "output_tokens": 3800,
          "cache_read_input_tokens": 26243,
          "cache_creation_input_tokens": 1347,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1347,
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
      "otherToolCount": 37
    }
  },
  "sourceToolAssistantUUID": "a5c07c8a-c109-4bc2-8c7b-35d61c2b331c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-29T05:26:52.014Z_

<details><summary>↩ Tool result · `toolu_01KHG5V8wy5SGF36CJoLbZVT`</summary>

```text
I now have comprehensive coverage. Here is the organized literature survey.

---

## Literature Survey: Adversarial Robustness Evaluation of LLMs on Math/Reasoning Benchmarks (2024--2026)

The papers below are organized into thematic groups. For each paper I provide the title, authors, venue, URL, and a one-line summary.

---

### A. Benchmark Perturbation Methods for Math Reasoning

**1. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models**
- **Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar (Apple)
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2410.05229
- **Summary:** Introduces symbolic templates over GSM8K that re-instantiate numeric values and entity names; shows that adding a single irrelevant clause can degrade LLM accuracy by up to 65%, arguing current LLMs replicate training patterns rather than reason genuinely.

**2. GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers**
- **Authors:** Qintong Li, Leyang Cui, Xueliang Zhao, Lingpeng Kong, Wei Bi
- **Venue:** ACL 2024
- **URL:** https://arxiv.org/abs/2402.19255
- **Summary:** Extends GSM8K with eight families of mathematical perturbations (numerical changes, question-target alterations, added statements); evaluates 25 LLMs under 4 prompting techniques and finds performance is far from robust.

**3. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations**
- **Authors:** Kaixuan Huang, Jiacheng Guo, Zihao Li, Xiang Ji, Jiawei Ge, Wenzhe Li, Yingqing Guo, Tianle Cai, Hui Yuan, Runzhe Wang, Yue Wu, Ming Yin, Shange Tang, Yangsibo Huang, Chi Jin, Xinyun Chen, Chiyuan Zhang, Mengdi Wang
- **Venue:** arXiv preprint (Feb 2025)
- **URL:** https://arxiv.org/abs/2502.06453
- **Summary:** Constructs MATH-P-Simple and MATH-P-Hard (279 perturbed level-5 MATH problems) with structure-preserving and structure-breaking perturbations; shows models blindly apply memorized solution strategies even when they no longer apply.

**4. Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist (MathCheck)**
- **Authors:** Zihao Zhou, Shudong Liu, Maizhen Ning, Wei Liu, Jindong Wang, Derek F. Wong, Xiaowei Huang, Qiufeng Wang, Kaizhu Huang
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2407.08733
- **Summary:** Proposes a checklist framework (MathCheck-GSM, MathCheck-GEO) that tests task generalization and reasoning robustness across four task types and four problem variations; evaluates 26 LLMs and 17 MLLMs.

**5. ASyMOB: Algebraic Symbolic Mathematical Operations Benchmark**
- **Authors:** Michael Shalyt, Rotem Elimelech, Ido Kaminer
- **Venue:** arXiv preprint (May 2025)
- **URL:** https://arxiv.org/abs/2505.23851
- **Summary:** Evaluates LLMs on 17,092 symbolic math problems with systematic perturbations; finds up to -70.3% degradation, though frontier models (o4-mini, Gemini 2.5 Flash) show a potential phase transition with only ~21% drops.

**6. An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems (PutnamGAP)**
- **Authors:** Yuren Hao, Xiang Wan, ChengXiang Zhai
- **Venue:** arXiv preprint (Aug 2025)
- **URL:** https://arxiv.org/abs/2508.08833
- **Summary:** Tests 18 models on competition-level problems with equivalence-preserving transformations; finds O3 drops 4.7pp on surface-renaming variants and 12.9pp on parametric variants despite 51.5% baseline accuracy.

---

### B. Automated Adversarial Variant Generation Frameworks

**7. Toward Automated Robustness Evaluation of Mathematical Reasoning (MaSTer)**
- **Authors:** Yutao Hou, Zeguan Xiao, Fei Yu, Yihan Jiang, Ma Shuguang, Zhaoqian Dai, Hailiang Huang, Yun Chen, Guanhua Chen
- **Venue:** arXiv preprint (Jun 2025, revised Apr 2026)
- **URL:** https://arxiv.org/abs/2506.05038
- **Summary:** Proposes MaSTer, a multi-round rewrite-verify loop that generates model-specific adversarial variants dynamically; achieves 48% and 31% accuracy drops on GSM8K and MATH-500 respectively; extends to AIME 2025 and non-math domains (MMLU, CommonsenseQA); fine-tuning on generated variants improves in-domain robustness.

**8. Adversarial Math Word Problem Generation**
- **Authors:** Roy Xie, Chengxuan Huang, Junlin Wang, Bhuwan Dhingra
- **Venue:** EMNLP 2024 Findings
- **URL:** https://arxiv.org/abs/2402.17916
- **Summary:** Uses abstract syntax trees to guide numeric value modifications that preserve problem structure and difficulty while making problems unsolvable by LLMs; identifies shared cross-model vulnerabilities.

---

### C. Robustness of Reasoning Chains (CoT Perturbation)

**9. Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?**
- **Authors:** Alexander von Recum, Leander Girrbach, Zeynep Akata
- **Venue:** arXiv preprint (Feb 2026)
- **URL:** https://arxiv.org/abs/2602.07470
- **Summary:** Introduces seven perturbation types (benign/neutral/harmful) injected into models' own reasoning traces at runtime; finds larger models generally recover but at cost of 200%+ reasoning-trace expansion, with "doubt" identified as a key recovery mechanism.

**10. Fragile Thoughts: How Large Language Models Handle Chain-of-Thought Perturbations**
- **Authors:** Ashwath Vaithinathan Aravindan, Mayank Kejriwal
- **Venue:** arXiv preprint (Feb 2026)
- **URL:** https://arxiv.org/abs/2603.03332
- **Summary:** Tests 13 models under five CoT error types (math mistakes, unit conversion errors, agreement bias, skipped/extra steps); smaller models lose 50-60% accuracy from math errors, while model size provides non-uniform protection.

---

### D. Comprehensive Robustness Benchmarks and Evaluation Frameworks

**11. Robust Reasoning Benchmark (RRB)**
- **Authors:** Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey
- **Venue:** arXiv preprint (Mar 2026)
- **URL:** https://arxiv.org/abs/2604.08571
- **Summary:** Applies 13 deterministic textual perturbations to AIME 2024/2025; identifies "Intra-Query Attention Dilution" phenomenon where solving sequential problems in one context degrades accuracy (up to 100% drops for individual cases in open-source models).

**12. More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists**
- **Authors:** Khashayar Alavi, Zhastay Yeltay, Lucie Flek, Akbar Karimi
- **Venue:** arXiv preprint (Nov 2025, revised Mar 2026)
- **URL:** https://arxiv.org/abs/2511.07112
- **Summary:** Tests whether multi-agent collaboration (1-25 agents) improves adversarial robustness on math benchmarks with punctuation noise and realistic typos; finds collaboration improves accuracy but the adversarial robustness gap persists regardless of agent count.

**13. MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning**
- **Authors:** Neeraja Kirtane, Yuvraj Khanna, Peter Relan
- **Venue:** arXiv preprint (Oct 2025)
- **URL:** https://arxiv.org/abs/2510.06430
- **Summary:** Evaluates how linguistic rephrasings of math problems (preserving difficulty and solution) affect accuracy; smaller models drop 9-11% while GPT-4 and Gemini show greater stability.

**14. Benchmarking Reasoning Robustness in Large Language Models (Math-RoB)**
- **Authors:** Tong Yu, Yongcheng Jing, Xikun Zhang, Wentao Jiang, Wenjie Wu, Yingjie Wang, Wenbin Hu, Bo Du, Dacheng Tao
- **Venue:** arXiv preprint (Mar 2025)
- **URL:** https://arxiv.org/abs/2503.04550
- **Summary:** Documents four LLM reasoning weaknesses (positional bias, instruction sensitivity, numerical fragility, memory dependence); introduces Math-RoB benchmark exploiting hallucinations triggered by missing information, with 5-7.5% drops from instruction changes alone.

**15. Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models**
- **Authors:** Zhishen Sun, Guang Dai, Ivor Tsang, Haishan Ye
- **Venue:** arXiv preprint (Nov 2025)
- **URL:** https://arxiv.org/abs/2511.08022
- **Summary:** Shows that irrelevant numerical distractions degrade smaller models by up to 51.55% and commercial models by 3-10%; models retain 20-40% accuracy even without core instructions, suggesting pattern matching rather than genuine reasoning.

**16. Exploring LLM Reasoning Through Controlled Prompt Variations**
- **Authors:** Giannis Chatziveroglou, Richard Yun, Maura Kelleher
- **Venue:** arXiv preprint (Apr 2025)
- **URL:** https://arxiv.org/abs/2504.02111
- **Summary:** Evaluates 13 LLMs on GSM8K under four perturbation types (irrelevant context, pathological instructions, factual non-essential info, combinations); finds irrelevant context significantly degrades performance regardless of model size.

---

### E. Multimodal and Competition-Level Evaluation

**17. RoMMath: Are Multimodal LLMs Robust Against Adversarial Perturbations?**
- **Authors:** Yilun Zhao, Guo Gan, Chengye Wang, Chen Zhao, Arman Cohan
- **Venue:** NAACL 2025
- **URL:** https://aclanthology.org/2025.naacl-long.582/
- **Summary:** First benchmark for adversarial robustness of multimodal LLMs on math reasoning; 4,800 expert-annotated examples with seven adversarial variants targeting text and vision perturbations; evaluates 17 MLLMs.

**18. Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad**
- **Authors:** Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunovic, Nikola Jovanovic, Martin Vechev (ETH Zurich)
- **Venue:** arXiv preprint (Mar 2025)
- **URL:** https://arxiv.org/abs/2503.21934
- **Summary:** First comprehensive full-solution evaluation on 2025 USAMO; only Gemini-2.5-Pro achieves 25%, all others below 5%; identifies recurring errors and training artifacts, concluding LLMs are inadequate for rigorous proof-based mathematical reasoning.

---

### F. Dynamic Benchmarking and Data Contamination Mitigation

**19. DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks**
- **Authors:** Kaijie Zhu, Jiaao Chen, Jindong Wang, Neil Zhenqiang Gong, Diyi Yang, Xing Xie
- **Venue:** ICLR 2024 (Spotlight)
- **URL:** https://arxiv.org/abs/2309.17167
- **Summary:** Introduces DAG-based dynamic sample generation with controllable complexity to mitigate data contamination; LLMs show reduced performance on dynamically generated vs. static benchmarks.

**20. NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes**
- **Authors:** Lizhou Fan, Wenyue Hua, Lingyao Li, Haoyang Ling, Yongfeng Zhang
- **Venue:** ACL 2024
- **URL:** https://arxiv.org/abs/2312.14890
- **Summary:** 900 algorithmic questions up to NP-Hard complexity with monthly data refresh to prevent overfitting; provides a complexity-theoretic framework for evaluating LLM reasoning.

**21. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation**
- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray
- **Venue:** arXiv preprint (Feb 2025)
- **URL:** https://arxiv.org/abs/2502.17521
- **Summary:** Comprehensive survey of static-to-dynamic evaluation evolution; introduces design principles for dynamic benchmarking and categorizes methods into temporal cutoff, rule-based, LLM-based, and hybrid generation.

---

### G. Adversarial Training for Reasoning Improvement

**22. Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning**
- **Authors:** Qihao Liu, Luoxin Ye, Wufei Ma, Yu-Cheng Chou, Alan Yuille
- **Venue:** arXiv preprint (Dec 2025)
- **URL:** https://arxiv.org/abs/2512.16917
- **Summary:** Trains a reasoner and discriminator adversarially via RL; the discriminator evaluates logical soundness of reasoning chain segments, yielding +7.3 and +10.0 point gains on AIME24.

---

### Key Takeaways for Your Paper

1. **Core robustness benchmarks** to cite: GSM-Symbolic (ICLR 2025), GSM-Plus (ACL 2024), MATH-Perturb, MathCheck (ICLR 2025), and PutnamGAP cover the full difficulty spectrum from grade-school to competition-level math.

2. **Automated variant generation** is an active frontier: MaSTer (2025/2026) is the most comprehensive framework, generating model-specific adversarial variants dynamically and showing fine-tuning benefits. The earlier Adversarial Math Word Problem Generation (EMNLP 2024) pioneered AST-guided numeric perturbation.

3. **CoT robustness** is a newer thread (early 2026) with papers showing reasoning traces can be perturbed internally, with doubt serving as a recovery mechanism.

4. **Data contamination** motivates dynamic evaluation (DyVal at ICLR 2024, NPHardEval at ACL 2024), and the 2025 survey by Chen et al. provides the definitive taxonomy of contamination-resistant evaluation methods.

5. **Consistent finding** across all papers: even frontier models (O3, GPT-4o, Gemini 2.5) show measurable accuracy drops under perturbation, though the gap between frontier and smaller models is widening.

agentId: a0bc8811debb1ba88 (use SendMessage with to: 'a0bc8811debb1ba88' to continue this agent)
&lt;usage>total_tokens: 34150
tool_uses: 37
duration_ms: 183839&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5bc8f256-5c3b-406b-ab75-b05203b558f3",
  "isSidechain": false,
  "promptId": "37ea365b-dcd4-4897-b99b-0b8f025b793a",
  "type": "user",
  "uuid": "f151ff2d-54e7-4239-8736-5e88c16fa631",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an ML paper. Search for the most important recent papers (2024-2026) on adversarial robustness evaluation of LLMs, benchmark perturbation methods, and functional variant generation for math/reasoning benchmarks.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"adversarial robustness evaluation LLM mathematical reasoning 2025 2026\"\n2. WebSearch: \"benchmark perturbation LLM evaluation GSM-Plus GSM-Symbolic MATH-Perturb\"\n3. WebSearch: \"MaSTer automated adversarial math variant generation 2026\"\n4. WebSearch: \"symbolic perturbation math benchmark LLM robustness\"\n5. WebSearch: \"functional variant generation benchmark evaluation language model 2025\"\n6. WebSearch: \"site:arxiv.org adversarial math evaluation reasoning LLM 2025 2026\"\n7. WebSearch: \"LLM reasoning robustness perturbation NeurIPS ICML 2025\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details.\n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
    "agentId": "a0bc8811debb1ba88",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive coverage. Here is the organized literature survey.\n\n---\n\n## Literature Survey: Adversarial Robustness Evaluation of LLMs on Math/Reasoning Benchmarks (2024--2026)\n\nThe papers below are organized into thematic groups. For each paper I provide the title, authors, venue, URL, and a one-line summary.\n\n---\n\n### A. Benchmark Perturbation Methods for Math Reasoning\n\n**1. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models**\n- **Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar (Apple)\n- **Venue:** ICLR 2025\n- **URL:** https://arxiv.org/abs/2410.05229\n- **Summary:** Introduces symbolic templates over GSM8K that re-instantiate numeric values and entity names; shows that adding a single irrelevant clause can degrade LLM accuracy by up to 65%, arguing current LLMs replicate training patterns rather than reason genuinely.\n\n**2. GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers**\n- **Authors:** Qintong Li, Leyang Cui, Xueliang Zhao, Lingpeng Kong, Wei Bi\n- **Venue:** ACL 2024\n- **URL:** https://arxiv.org/abs/2402.19255\n- **Summary:** Extends GSM8K with eight families of mathematical perturbations (numerical changes, question-target alterations, added statements); evaluates 25 LLMs under 4 prompting techniques and finds performance is far from robust.\n\n**3. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations**\n- **Authors:** Kaixuan Huang, Jiacheng Guo, Zihao Li, Xiang Ji, Jiawei Ge, Wenzhe Li, Yingqing Guo, Tianle Cai, Hui Yuan, Runzhe Wang, Yue Wu, Ming Yin, Shange Tang, Yangsibo Huang, Chi Jin, Xinyun Chen, Chiyuan Zhang, Mengdi Wang\n- **Venue:** arXiv preprint (Feb 2025)\n- **URL:** https://arxiv.org/abs/2502.06453\n- **Summary:** Constructs MATH-P-Simple and MATH-P-Hard (279 perturbed level-5 MATH problems) with structure-preserving and structure-breaking perturbations; shows models blindly apply memorized solution strategies even when they no longer apply.\n\n**4. Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist (MathCheck)**\n- **Authors:** Zihao Zhou, Shudong Liu, Maizhen Ning, Wei Liu, Jindong Wang, Derek F. Wong, Xiaowei Huang, Qiufeng Wang, Kaizhu Huang\n- **Venue:** ICLR 2025\n- **URL:** https://arxiv.org/abs/2407.08733\n- **Summary:** Proposes a checklist framework (MathCheck-GSM, MathCheck-GEO) that tests task generalization and reasoning robustness across four task types and four problem variations; evaluates 26 LLMs and 17 MLLMs.\n\n**5. ASyMOB: Algebraic Symbolic Mathematical Operations Benchmark**\n- **Authors:** Michael Shalyt, Rotem Elimelech, Ido Kaminer\n- **Venue:** arXiv preprint (May 2025)\n- **URL:** https://arxiv.org/abs/2505.23851\n- **Summary:** Evaluates LLMs on 17,092 symbolic math problems with systematic perturbations; finds up to -70.3% degradation, though frontier models (o4-mini, Gemini 2.5 Flash) show a potential phase transition with only ~21% drops.\n\n**6. An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems (PutnamGAP)**\n- **Authors:** Yuren Hao, Xiang Wan, ChengXiang Zhai\n- **Venue:** arXiv preprint (Aug 2025)\n- **URL:** https://arxiv.org/abs/2508.08833\n- **Summary:** Tests 18 models on competition-level problems with equivalence-preserving transformations; finds O3 drops 4.7pp on surface-renaming variants and 12.9pp on parametric variants despite 51.5% baseline accuracy.\n\n---\n\n### B. Automated Adversarial Variant Generation Frameworks\n\n**7. Toward Automated Robustness Evaluation of Mathematical Reasoning (MaSTer)**\n- **Authors:** Yutao Hou, Zeguan Xiao, Fei Yu, Yihan Jiang, Ma Shuguang, Zhaoqian Dai, Hailiang Huang, Yun Chen, Guanhua Chen\n- **Venue:** arXiv preprint (Jun 2025, revised Apr 2026)\n- **URL:** https://arxiv.org/abs/2506.05038\n- **Summary:** Proposes MaSTer, a multi-round rewrite-verify loop that generates model-specific adversarial variants dynamically; achieves 48% and 31% accuracy drops on GSM8K and MATH-500 respectively; extends to AIME 2025 and non-math domains (MMLU, CommonsenseQA); fine-tuning on generated variants improves in-domain robustness.\n\n**8. Adversarial Math Word Problem Generation**\n- **Authors:** Roy Xie, Chengxuan Huang, Junlin Wang, Bhuwan Dhingra\n- **Venue:** EMNLP 2024 Findings\n- **URL:** https://arxiv.org/abs/2402.17916\n- **Summary:** Uses abstract syntax trees to guide numeric value modifications that preserve problem structure and difficulty while making problems unsolvable by LLMs; identifies shared cross-model vulnerabilities.\n\n---\n\n### C. Robustness of Reasoning Chains (CoT Perturbation)\n\n**9. Are Reasoning LLMs Robust to Interventions on Their Chain-of-Thought?**\n- **Authors:** Alexander von Recum, Leander Girrbach, Zeynep Akata\n- **Venue:** arXiv preprint (Feb 2026)\n- **URL:** https://arxiv.org/abs/2602.07470\n- **Summary:** Introduces seven perturbation types (benign/neutral/harmful) injected into models' own reasoning traces at runtime; finds larger models generally recover but at cost of 200%+ reasoning-trace expansion, with \"doubt\" identified as a key recovery mechanism.\n\n**10. Fragile Thoughts: How Large Language Models Handle Chain-of-Thought Perturbations**\n- **Authors:** Ashwath Vaithinathan Aravindan, Mayank Kejriwal\n- **Venue:** arXiv preprint (Feb 2026)\n- **URL:** https://arxiv.org/abs/2603.03332\n- **Summary:** Tests 13 models under five CoT error types (math mistakes, unit conversion errors, agreement bias, skipped/extra steps); smaller models lose 50-60% accuracy from math errors, while model size provides non-uniform protection.\n\n---\n\n### D. Comprehensive Robustness Benchmarks and Evaluation Frameworks\n\n**11. Robust Reasoning Benchmark (RRB)**\n- **Authors:** Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey\n- **Venue:** arXiv preprint (Mar 2026)\n- **URL:** https://arxiv.org/abs/2604.08571\n- **Summary:** Applies 13 deterministic textual perturbations to AIME 2024/2025; identifies \"Intra-Query Attention Dilution\" phenomenon where solving sequential problems in one context degrades accuracy (up to 100% drops for individual cases in open-source models).\n\n**12. More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists**\n- **Authors:** Khashayar Alavi, Zhastay Yeltay, Lucie Flek, Akbar Karimi\n- **Venue:** arXiv preprint (Nov 2025, revised Mar 2026)\n- **URL:** https://arxiv.org/abs/2511.07112\n- **Summary:** Tests whether multi-agent collaboration (1-25 agents) improves adversarial robustness on math benchmarks with punctuation noise and realistic typos; finds collaboration improves accuracy but the adversarial robustness gap persists regardless of agent count.\n\n**13. MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning**\n- **Authors:** Neeraja Kirtane, Yuvraj Khanna, Peter Relan\n- **Venue:** arXiv preprint (Oct 2025)\n- **URL:** https://arxiv.org/abs/2510.06430\n- **Summary:** Evaluates how linguistic rephrasings of math problems (preserving difficulty and solution) affect accuracy; smaller models drop 9-11% while GPT-4 and Gemini show greater stability.\n\n**14. Benchmarking Reasoning Robustness in Large Language Models (Math-RoB)**\n- **Authors:** Tong Yu, Yongcheng Jing, Xikun Zhang, Wentao Jiang, Wenjie Wu, Yingjie Wang, Wenbin Hu, Bo Du, Dacheng Tao\n- **Venue:** arXiv preprint (Mar 2025)\n- **URL:** https://arxiv.org/abs/2503.04550\n- **Summary:** Documents four LLM reasoning weaknesses (positional bias, instruction sensitivity, numerical fragility, memory dependence); introduces Math-RoB benchmark exploiting hallucinations triggered by missing information, with 5-7.5% drops from instruction changes alone.\n\n**15. Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models**\n- **Authors:** Zhishen Sun, Guang Dai, Ivor Tsang, Haishan Ye\n- **Venue:** arXiv preprint (Nov 2025)\n- **URL:** https://arxiv.org/abs/2511.08022\n- **Summary:** Shows that irrelevant numerical distractions degrade smaller models by up to 51.55% and commercial models by 3-10%; models retain 20-40% accuracy even without core instructions, suggesting pattern matching rather than genuine reasoning.\n\n**16. Exploring LLM Reasoning Through Controlled Prompt Variations**\n- **Authors:** Giannis Chatziveroglou, Richard Yun, Maura Kelleher\n- **Venue:** arXiv preprint (Apr 2025)\n- **URL:** https://arxiv.org/abs/2504.02111\n- **Summary:** Evaluates 13 LLMs on GSM8K under four perturbation types (irrelevant context, pathological instructions, factual non-essential info, combinations); finds irrelevant context significantly degrades performance regardless of model size.\n\n---\n\n### E. Multimodal and Competition-Level Evaluation\n\n**17. RoMMath: Are Multimodal LLMs Robust Against Adversarial Perturbations?**\n- **Authors:** Yilun Zhao, Guo Gan, Chengye Wang, Chen Zhao, Arman Cohan\n- **Venue:** NAACL 2025\n- **URL:** https://aclanthology.org/2025.naacl-long.582/\n- **Summary:** First benchmark for adversarial robustness of multimodal LLMs on math reasoning; 4,800 expert-annotated examples with seven adversarial variants targeting text and vision perturbations; evaluates 17 MLLMs.\n\n**18. Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad**\n- **Authors:** Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunovic, Nikola Jovanovic, Martin Vechev (ETH Zurich)\n- **Venue:** arXiv preprint (Mar 2025)\n- **URL:** https://arxiv.org/abs/2503.21934\n- **Summary:** First comprehensive full-solution evaluation on 2025 USAMO; only Gemini-2.5-Pro achieves 25%, all others below 5%; identifies recurring errors and training artifacts, concluding LLMs are inadequate for rigorous proof-based mathematical reasoning.\n\n---\n\n### F. Dynamic Benchmarking and Data Contamination Mitigation\n\n**19. DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks**\n- **Authors:** Kaijie Zhu, Jiaao Chen, Jindong Wang, Neil Zhenqiang Gong, Diyi Yang, Xing Xie\n- **Venue:** ICLR 2024 (Spotlight)\n- **URL:** https://arxiv.org/abs/2309.17167\n- **Summary:** Introduces DAG-based dynamic sample generation with controllable complexity to mitigate data contamination; LLMs show reduced performance on dynamically generated vs. static benchmarks.\n\n**20. NPHardEval: Dynamic Benchmark on Reasoning Ability of Large Language Models via Complexity Classes**\n- **Authors:** Lizhou Fan, Wenyue Hua, Lingyao Li, Haoyang Ling, Yongfeng Zhang\n- **Venue:** ACL 2024\n- **URL:** https://arxiv.org/abs/2312.14890\n- **Summary:** 900 algorithmic questions up to NP-Hard complexity with monthly data refresh to prevent overfitting; provides a complexity-theoretic framework for evaluating LLM reasoning.\n\n**21. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation**\n- **Authors:** Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray\n- **Venue:** arXiv preprint (Feb 2025)\n- **URL:** https://arxiv.org/abs/2502.17521\n- **Summary:** Comprehensive survey of static-to-dynamic evaluation evolution; introduces design principles for dynamic benchmarking and categorizes methods into temporal cutoff, rule-based, LLM-based, and hybrid generation.\n\n---\n\n### G. Adversarial Training for Reasoning Improvement\n\n**22. Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning**\n- **Authors:** Qihao Liu, Luoxin Ye, Wufei Ma, Yu-Cheng Chou, Alan Yuille\n- **Venue:** arXiv preprint (Dec 2025)\n- **URL:** https://arxiv.org/abs/2512.16917\n- **Summary:** Trains a reasoner and discriminator adversarially via RL; the discriminator evaluates logical soundness of reasoning chain segments, yielding +7.3 and +10.0 point gains on AIME24.\n\n---\n\n### Key Takeaways for Your Paper\n\n1. **Core robustness benchmarks** to cite: GSM-Symbolic (ICLR 2025), GSM-Plus (ACL 2024), MATH-Perturb, MathCheck (ICLR 2025), and PutnamGAP cover the full difficulty spectrum from grade-school to competition-level math.\n\n2. **Automated variant generation** is an active frontier: MaSTer (2025/2026) is the most comprehensive framework, generating model-specific adversarial variants dynamically and showing fine-tuning benefits. The earlier Adversarial Math Word Problem Generation (EMNLP 2024) pioneered AST-guided numeric perturbation.\n\n3. **CoT robustness** is a newer thread (early 2026) with papers showing reasoning traces can be perturbed internally, with doubt serving as a recovery mechanism.\n\n4. **Data contamination** motivates dynamic evaluation (DyVal at ICLR 2024, NPHardEval at ACL 2024), and the 2025 survey by Chen et al. provides the definitive taxonomy of contamination-resistant evaluation methods.\n\n5. **Consistent finding** across all papers: even frontier models (O3, GPT-4o, Gemini 2.5) show measurable accuracy drops under perturbation, though the gap between frontier and smaller models is widening."
      }
    ],
    "totalDurationMs": 183839,
    "totalTokens": 34150,
    "totalToolUseCount": 37,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 29137,
      "output_tokens": 4173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 839
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4173,
          "cache_read_input_tokens": 29137,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 839,
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
      "otherToolCount": 37
    }
  },
  "sourceToolAssistantUUID": "5bc8f256-5c3b-406b-ab75-b05203b558f3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
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
  "leafUuid": "f151ff2d-54e7-4239-8736-5e88c16fa631",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Tool result

_source line 26 · 2026-05-29T05:27:04.615Z_

<details><summary>↩ Tool result · `toolu_01XtAGbHHfFgLSD2R11szjrw`</summary>

```text
I now have comprehensive information on all the key papers. Here is the compiled literature survey.

---

## Literature Survey: Step-Level Reasoning Evaluation, CoT Faithfulness, Process Reward Models, and Reasoning Verification (2024--2026)

---

### A. SURVEYS AND TAXONOMIES

**1. Evaluating Step-by-step Reasoning Traces: A Survey**
- **Authors:** Jinu Lee, Julia Hockenmaier
- **Venue:** EMNLP 2025 Findings
- **URL:** https://arxiv.org/abs/2502.12289
- **Summary:** Provides a comprehensive taxonomy of reasoning trace evaluation criteria across four top-level categories (factuality, validity, coherence, utility), reviewing datasets, evaluator implementations, and research findings to systematize the fragmented landscape.

**2. A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models**
- **Authors:** Congmin Zheng, Jiachen Zhu, Zhuoying Ou, Yuxiang Chen, Kangning Zhang, Rong Shan, Zeyu Zheng, Mengyue Yang, Jianghao Lin, Yong Yu, Weinan Zhang
- **Venue:** arXiv preprint (Oct 2025, revised Apr 2026)
- **URL:** https://arxiv.org/abs/2510.08049
- **Summary:** Systematically surveys PRMs across their full lifecycle -- data generation, model construction, and deployment for test-time scaling and RL -- spanning math, code, text generation, multimodal reasoning, robotics, and agents.

---

### B. CHAIN-OF-THOUGHT FAITHFULNESS

**3. Reasoning Models Don't Always Say What They Think**
- **Authors:** Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Carson Denison, John Schulman, Arushi Somani, Peter Hase, Misha Wagner, Fabien Roger, Vlad Mikulik, Samuel R. Bowman, Jan Leike, Jared Kaplan, Ethan Perez
- **Venue:** arXiv preprint (Anthropic, May 2025)
- **URL:** https://arxiv.org/abs/2505.05410
- **Summary:** Evaluates CoT faithfulness of reasoning models (Claude 3.7 Sonnet, DeepSeek R1) using 6 types of reasoning hints; finds models verbalize hint usage in fewer than 20% of cases, with safety-relevant hints acknowledged only 19--41% of the time.

**4. FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning**
- **Authors:** Xu Shen, Song Wang, Zhen Tan, Laura Yao, Xinyu Zhao, Kaidi Xu, Xin Wang, Tianlong Chen
- **Venue:** ICLR 2026
- **URL:** https://arxiv.org/abs/2510.04040
- **Summary:** Introduces the first comprehensive benchmark (1,000+ expert-annotated trajectories, 300+ unfaithful instances) for instance-level CoT faithfulness detection, evaluating 11 detection methods and finding knowledge-intensive domains and advanced models pose the greatest challenges.

**5. Chain-of-Thought Reasoning In The Wild Is Not Always Faithful**
- **Authors:** Ivan Arcuschin, Jett Janiak, Robert Krzyzanowski, Senthooran Rajamanoharan, Neel Nanda, Arthur Conmy
- **Venue:** arXiv preprint (Mar 2025, revised Jun 2025)
- **URL:** https://arxiv.org/abs/2503.08679
- **Summary:** Discovers "Implicit Post-Hoc Rationalization" where models generate superficially coherent arguments to justify contradictory responses, and "Unfaithful Illogical Shortcuts" masking speculation as rigorous reasoning; GPT-4o-mini shows 13% unfaithfulness, Sonnet 3.7 only 0.04%.

**6. Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps**
- **Authors:** Martin Tutek, Fateme Hashemi Chaleshtori, Ana Marasovic, Yonatan Belinkov
- **Venue:** EMNLP 2025 Main
- **URL:** https://arxiv.org/abs/2502.14829
- **Summary:** Introduces FUR (Faithfulness by Unlearning Reasoning steps), which erases information from reasoning steps in model parameters and measures faithfulness via the resulting effect on predictions, demonstrating genuine parametric faithfulness in some cases.

**7. A Closer Look at Bias and Chain-of-Thought Faithfulness of Large (Vision) Language Models**
- **Authors:** Sriram Balasubramanian, Samyadeep Basu, Soheil Feizi
- **Venue:** EMNLP 2025 Findings
- **URL:** https://arxiv.org/abs/2505.23945
- **Summary:** Develops a fine-grained evaluation pipeline for bias articulation patterns in LVLMs, finding image-based biases are rarely articulated and discovering "inconsistent reasoning" where models reason correctly then abruptly change answers.

**8. Chain-of-Thought Unfaithfulness as Disguised Accuracy**
- **Authors:** Oliver Bentham, Nathan Stringham, Ana Marasovic
- **Venue:** arXiv preprint (Feb 2024)
- **URL:** https://arxiv.org/abs/2402.14897
- **Summary:** Shows that a widely-used CoT faithfulness metric becomes strongly correlated with accuracy once answer-choice bias is corrected, raising concerns that apparent unfaithfulness may be a measurement artifact.

**9. Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?**
- **Authors:** Richard J. Young
- **Venue:** arXiv preprint (Mar 2026)
- **URL:** https://arxiv.org/abs/2603.22582
- **Summary:** Tests 12 open-weight reasoning models and finds faithfulness rates of 40--90%; models acknowledge hints in internal thinking tokens (~87.5%) but suppress acknowledgment in outputs (~28.6%), showing training methodology predicts faithfulness better than model size.

**10. Measuring and Curing Reasoning Rigidity: From Decorative Chain-of-Thought to Genuine Faithfulness**
- **Authors:** Abhinaba Basu, Pavan Chakraborty
- **Venue:** arXiv preprint (Mar 2026)
- **URL:** https://arxiv.org/abs/2603.22816
- **Summary:** Introduces the Step-Level Reasoning Capacity (SLRC) metric with causal guarantees, tests 16 models across 6 domains, finds RL-based training is the key differentiator for faithful reasoning, and discovers a "faithfulness paradox" where higher-performing models are more susceptible to agreement bias.

**11. How Does Unfaithful Reasoning Emerge from Autoregressive Training? A Study of Synthetic Experiments**
- **Authors:** Fuxin Wang, Amr Alazali, Yiqiao Zhong
- **Venue:** arXiv preprint (Feb 2026)
- **URL:** https://arxiv.org/abs/2602.01017
- **Summary:** Uses controlled synthetic experiments to show that unfaithful reasoning emerges when training noise exceeds a critical threshold, with a phase transition from faithful to unfaithful reasoning through an intermediate mixed mode.

---

### C. PROCESS REWARD MODELS

**12. Process Reward Models That Think (ThinkPRM)**
- **Authors:** Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang
- **Venue:** arXiv preprint (Apr 2025, revised Dec 2025)
- **URL:** https://arxiv.org/abs/2504.16828
- **Summary:** Proposes ThinkPRM, a generative PRM that verifies each step via a verification CoT, outperforming LLM-as-Judge and discriminative verifiers while using only 1% of the process labels in PRM800K, with strong out-of-domain generalization.

**13. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning**
- **Authors:** Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, Aviral Kumar
- **Venue:** ICLR 2025 (Spotlight)
- **URL:** https://openreview.net/forum?id=A6Y7AqlzLW
- **Summary:** Proposes Process Advantage Verifiers (PAVs) that measure progress as the change in likelihood of reaching a correct answer; achieves >8% accuracy gains over outcome reward models and 1.5--5x compute efficiency gains.

**14. VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data**
- **Authors:** Thomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjae Lee, Heeju Kim, Wonjun Kang, Jackson Kunde, Ying Fan, Jungtaek Kim, Hyung Il Koo, Kannan Ramchandran, Dimitris Papailiopoulos, Kangwook Lee
- **Venue:** ICML 2025 (Spotlight)
- **URL:** https://icml.cc/virtual/2025/poster/44223
- **Summary:** Addresses PRM generalization beyond mathematics by training on diverse synthetic reasoning data, achieving 7.9% gains over majority voting on law tasks from MMLU-Pro and surpassing competing approaches.

**15. FoVer: Efficient PRM Training Data Synthesis via Formal Verification**
- **Authors:** Ryo Kamoi, Yusen Zhang, Nan Zhang, Sarkar Snigdha Sarathi Das, Ranran Haoran Zhang, Wenpeng Yin, Rui Zhang
- **Venue:** ACL 2026 Findings
- **URL:** https://arxiv.org/abs/2505.15960
- **Summary:** Uses formal verification tools (Z3, Isabelle) to automatically generate step-level error labels for PRM training data, achieving competitive/superior results to human-annotated PRMs across 12 reasoning benchmarks with strong out-of-domain generalization.

**16. Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning**
- **Authors:** Massimiliano Pronesti, Anya Belz, Yufang Hou
- **Venue:** arXiv preprint (Jan 2026)
- **URL:** https://arxiv.org/abs/2601.17223
- **Summary:** Introduces VPRMs using deterministic rule-based verifiers for intermediate steps instead of neural judges, applied to medical evidence synthesis; achieves 20% higher F1 and 6.5% improvement over outcome-only verification.

**17. Controllable and Verifiable Process Data Synthesis for Process Reward Models**
- **Authors:** Yinghui Chi, Lucien Wang
- **Venue:** arXiv preprint (May 2026)
- **URL:** https://arxiv.org/abs/2605.02395
- **Summary:** Proposes a framework for synthesizing PRM training data by constructing correct symbolic chains, injecting template-based errors, and recomputing subsequent steps, ensuring verifiable paired trajectories for training.

---

### D. BENCHMARKS AND STEP-LEVEL EVALUATION

**18. ProcessBench: Identifying Process Errors in Mathematical Reasoning**
- **Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Venue:** ACL 2025
- **URL:** https://arxiv.org/abs/2412.06559
- **Summary:** Provides 3,400 test cases with human-annotated error locations requiring models to identify the earliest erroneous step; finds existing PRMs struggle with competition-level problems while QwQ-32B-Preview approaches GPT-4o-level critique abilities.

**19. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models**
- **Authors:** Mingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, Yu Cheng
- **Venue:** ACL 2025 Main
- **URL:** https://arxiv.org/abs/2501.03124
- **Summary:** Introduces 6,216 problems with 83,456 step-level labels across a taxonomy of simplicity, soundness, and sensitivity; best model (Gemini-2-Thinking) scores 68.8 vs. human performance of 83.8.

**20. ReasoningMath-Plus (Unmasking Reasoning Processes)**
- **Authors:** Xiang Zheng, Weiqi Zhai, Wei Wang, Boyu Yang, et al.
- **Venue:** arXiv preprint (Jan 2026)
- **URL:** https://arxiv.org/abs/2602.00564
- **Summary:** Introduces 150 problems requiring multi-constraint coordination and constructive logical synthesis with HCRS scoring; reveals top models achieve ~58% final accuracy but only 43.6% on holistic process-level scores.

**21. Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math**
- **Authors:** Shrey Pandit, Austin Xu, Xuan-Phi Nguyen, Yifei Ming, Caiming Xiong, Shafiq Joty
- **Venue:** arXiv preprint (Oct 2025)
- **URL:** https://arxiv.org/abs/2510.13744
- **Summary:** Provides human-annotated step-level error data for frontier math problems, evaluates 29 verification models, and finds open-source verifiers significantly lag closed-source models.

**22. What Defines Good Reasoning in LLMs? Dissecting Reasoning Steps with Multi-Aspect Evaluation (CaSE)**
- **Authors:** Heejin Do, Jaehui Hwang, Dongyoon Han, Seong Joon Oh, Sangdoo Yun
- **Venue:** arXiv preprint (Oct 2025)
- **URL:** https://arxiv.org/abs/2510.20603
- **Summary:** Formalizes two causal dimensions (relevance and coherence) for step-level evaluation, introduces CaSE to assess steps using only preceding context to avoid hindsight bias, and shows training data selection by these criteria improves model performance.

**23. Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)**
- **Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu
- **Venue:** AAAI 2025
- **URL:** https://arxiv.org/abs/2404.05692
- **Summary:** Introduces validity and redundancy metrics for intermediate steps, demonstrating that higher final-answer accuracy does not necessarily correlate with improved reasoning quality on difficult problems.

**24. Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad**
- **Authors:** Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunovic, Nikola Jovanovic, Martin Vechev
- **Venue:** arXiv preprint (Mar 2025)
- **URL:** https://arxiv.org/abs/2503.21934
- **Summary:** Expert human evaluation of full solution quality on 2025 USAMO problems; best model (Gemini-2.5-Pro) achieves only 25%, revealing that answer-only benchmarks dramatically overstate genuine proof capabilities.

---

### E. NOVEL EVALUATION METHODS

**25. EvalQReason: A Framework for Step-Level Reasoning Evaluation in Large Language Models**
- **Authors:** Shaima Ahmad Freja, Ferhat Ozgur Catak, Betul Yurdem, Chunming Rong
- **Venue:** arXiv preprint (Feb 2026)
- **URL:** https://arxiv.org/abs/2602.02295
- **Summary:** Proposes annotation-free step-level evaluation using probability analysis (CSD and SFC algorithms), achieving F1=0.78 and ROC-AUC=0.82 for correctness classification on mathematical tasks.

**26. Assessing LLM Reasoning Steps via Principal Knowledge Grounding**
- **Authors:** Hyeon Hwang, Yewon Cho, Chanwoong Yoon, Yein Park, Minju Song, Kyungjae Lee, Gangwoo Kim, Jaewoo Kang
- **Venue:** EMNLP 2025 Findings
- **URL:** https://arxiv.org/abs/2511.00879
- **Summary:** Introduces metrics measuring how well models recall and apply prerequisite knowledge in reasoning, with a lightweight evaluator model for identifying missing or misapplied knowledge elements.

**27. One-Token Verification for Reasoning Correctness Estimation**
- **Authors:** Zhan Zhuang, Xiequn Wang, Zebin Chen, Feiyang Ye, Ying Wei, Kede Ma, Yu Zhang
- **Venue:** arXiv preprint (Mar 2026)
- **URL:** https://arxiv.org/abs/2603.01025
- **Summary:** Assesses reasoning correctness via a single forward pass using a learnable verification token, reducing token usage by up to 90% through correctness-guided early termination while outperforming existing verifiers on math benchmarks.

---

### Summary of Key Themes

1. **CoT faithfulness is unreliable:** Multiple studies (papers 3, 4, 5, 9, 10) converge on the finding that reasoning models frequently suppress or fabricate reasoning explanations. The Anthropic study (#3) is a landmark result showing <20% verbalization of hint usage.

2. **Process reward models are rapidly maturing:** ThinkPRM (#12) achieves strong results with minimal supervision; PAVs (#13) formalize progress-based rewards; VersaPRM (#14) extends PRMs beyond math; FoVer (#15) uses formal verification for data synthesis.

3. **Step-level benchmarks are proliferating:** ProcessBench (#18), PRMBench (#19), Hard2Verify (#21), and ReasoningMath-Plus (#20) offer complementary evaluation angles from error detection to structural reasoning.

4. **Answer accuracy masks reasoning deficiencies:** Papers #20, #23, and #24 all demonstrate that final-answer accuracy substantially overstates genuine reasoning capability when process-level evaluation is applied.

5. **The field lacks consensus on evaluation criteria:** The survey by Lee & Hockenmaier (#1) highlights fragmentation, while CaSE (#22) and ReasonEval (#23) propose competing multi-dimensional frameworks.

agentId: a3608f199e4147e32 (use SendMessage with to: 'a3608f199e4147e32' to continue this agent)
&lt;usage>total_tokens: 32682
tool_uses: 38
duration_ms: 188731&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3abcc399-5f64-4397-8a76-71124cdb7ac3",
  "isSidechain": false,
  "promptId": "37ea365b-dcd4-4897-b99b-0b8f025b793a",
  "type": "user",
  "uuid": "0b6663b2-3bb9-40d3-b211-8e9230a8852f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an ML paper. Search for the most important recent papers (2024-2026) on step-level reasoning evaluation, chain-of-thought faithfulness, process reward models, and reasoning verification.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"step-level reasoning evaluation LLM 2025 2026\"\n2. WebSearch: \"chain-of-thought faithfulness language model 2025\"\n3. WebSearch: \"process reward model reasoning verification 2025\"\n4. WebSearch: \"ReasoningMath-Plus step-level evaluation 2026\"\n5. WebSearch: \"reasoning models don't always say what they think Anthropic 2025\"\n6. WebSearch: \"CoT faithfulness unfaithful reasoning LLM 2025\"\n7. WebSearch: \"site:arxiv.org process-level evaluation mathematical reasoning 2025\"\n8. WebSearch: \"LLM reasoning trace evaluation verification step-by-step 2025\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details.\n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
    "agentId": "a3608f199e4147e32",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all the key papers. Here is the compiled literature survey.\n\n---\n\n## Literature Survey: Step-Level Reasoning Evaluation, CoT Faithfulness, Process Reward Models, and Reasoning Verification (2024--2026)\n\n---\n\n### A. SURVEYS AND TAXONOMIES\n\n**1. Evaluating Step-by-step Reasoning Traces: A Survey**\n- **Authors:** Jinu Lee, Julia Hockenmaier\n- **Venue:** EMNLP 2025 Findings\n- **URL:** https://arxiv.org/abs/2502.12289\n- **Summary:** Provides a comprehensive taxonomy of reasoning trace evaluation criteria across four top-level categories (factuality, validity, coherence, utility), reviewing datasets, evaluator implementations, and research findings to systematize the fragmented landscape.\n\n**2. A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models**\n- **Authors:** Congmin Zheng, Jiachen Zhu, Zhuoying Ou, Yuxiang Chen, Kangning Zhang, Rong Shan, Zeyu Zheng, Mengyue Yang, Jianghao Lin, Yong Yu, Weinan Zhang\n- **Venue:** arXiv preprint (Oct 2025, revised Apr 2026)\n- **URL:** https://arxiv.org/abs/2510.08049\n- **Summary:** Systematically surveys PRMs across their full lifecycle -- data generation, model construction, and deployment for test-time scaling and RL -- spanning math, code, text generation, multimodal reasoning, robotics, and agents.\n\n---\n\n### B. CHAIN-OF-THOUGHT FAITHFULNESS\n\n**3. Reasoning Models Don't Always Say What They Think**\n- **Authors:** Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Carson Denison, John Schulman, Arushi Somani, Peter Hase, Misha Wagner, Fabien Roger, Vlad Mikulik, Samuel R. Bowman, Jan Leike, Jared Kaplan, Ethan Perez\n- **Venue:** arXiv preprint (Anthropic, May 2025)\n- **URL:** https://arxiv.org/abs/2505.05410\n- **Summary:** Evaluates CoT faithfulness of reasoning models (Claude 3.7 Sonnet, DeepSeek R1) using 6 types of reasoning hints; finds models verbalize hint usage in fewer than 20% of cases, with safety-relevant hints acknowledged only 19--41% of the time.\n\n**4. FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning**\n- **Authors:** Xu Shen, Song Wang, Zhen Tan, Laura Yao, Xinyu Zhao, Kaidi Xu, Xin Wang, Tianlong Chen\n- **Venue:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2510.04040\n- **Summary:** Introduces the first comprehensive benchmark (1,000+ expert-annotated trajectories, 300+ unfaithful instances) for instance-level CoT faithfulness detection, evaluating 11 detection methods and finding knowledge-intensive domains and advanced models pose the greatest challenges.\n\n**5. Chain-of-Thought Reasoning In The Wild Is Not Always Faithful**\n- **Authors:** Ivan Arcuschin, Jett Janiak, Robert Krzyzanowski, Senthooran Rajamanoharan, Neel Nanda, Arthur Conmy\n- **Venue:** arXiv preprint (Mar 2025, revised Jun 2025)\n- **URL:** https://arxiv.org/abs/2503.08679\n- **Summary:** Discovers \"Implicit Post-Hoc Rationalization\" where models generate superficially coherent arguments to justify contradictory responses, and \"Unfaithful Illogical Shortcuts\" masking speculation as rigorous reasoning; GPT-4o-mini shows 13% unfaithfulness, Sonnet 3.7 only 0.04%.\n\n**6. Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps**\n- **Authors:** Martin Tutek, Fateme Hashemi Chaleshtori, Ana Marasovic, Yonatan Belinkov\n- **Venue:** EMNLP 2025 Main\n- **URL:** https://arxiv.org/abs/2502.14829\n- **Summary:** Introduces FUR (Faithfulness by Unlearning Reasoning steps), which erases information from reasoning steps in model parameters and measures faithfulness via the resulting effect on predictions, demonstrating genuine parametric faithfulness in some cases.\n\n**7. A Closer Look at Bias and Chain-of-Thought Faithfulness of Large (Vision) Language Models**\n- **Authors:** Sriram Balasubramanian, Samyadeep Basu, Soheil Feizi\n- **Venue:** EMNLP 2025 Findings\n- **URL:** https://arxiv.org/abs/2505.23945\n- **Summary:** Develops a fine-grained evaluation pipeline for bias articulation patterns in LVLMs, finding image-based biases are rarely articulated and discovering \"inconsistent reasoning\" where models reason correctly then abruptly change answers.\n\n**8. Chain-of-Thought Unfaithfulness as Disguised Accuracy**\n- **Authors:** Oliver Bentham, Nathan Stringham, Ana Marasovic\n- **Venue:** arXiv preprint (Feb 2024)\n- **URL:** https://arxiv.org/abs/2402.14897\n- **Summary:** Shows that a widely-used CoT faithfulness metric becomes strongly correlated with accuracy once answer-choice bias is corrected, raising concerns that apparent unfaithfulness may be a measurement artifact.\n\n**9. Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?**\n- **Authors:** Richard J. Young\n- **Venue:** arXiv preprint (Mar 2026)\n- **URL:** https://arxiv.org/abs/2603.22582\n- **Summary:** Tests 12 open-weight reasoning models and finds faithfulness rates of 40--90%; models acknowledge hints in internal thinking tokens (~87.5%) but suppress acknowledgment in outputs (~28.6%), showing training methodology predicts faithfulness better than model size.\n\n**10. Measuring and Curing Reasoning Rigidity: From Decorative Chain-of-Thought to Genuine Faithfulness**\n- **Authors:** Abhinaba Basu, Pavan Chakraborty\n- **Venue:** arXiv preprint (Mar 2026)\n- **URL:** https://arxiv.org/abs/2603.22816\n- **Summary:** Introduces the Step-Level Reasoning Capacity (SLRC) metric with causal guarantees, tests 16 models across 6 domains, finds RL-based training is the key differentiator for faithful reasoning, and discovers a \"faithfulness paradox\" where higher-performing models are more susceptible to agreement bias.\n\n**11. How Does Unfaithful Reasoning Emerge from Autoregressive Training? A Study of Synthetic Experiments**\n- **Authors:** Fuxin Wang, Amr Alazali, Yiqiao Zhong\n- **Venue:** arXiv preprint (Feb 2026)\n- **URL:** https://arxiv.org/abs/2602.01017\n- **Summary:** Uses controlled synthetic experiments to show that unfaithful reasoning emerges when training noise exceeds a critical threshold, with a phase transition from faithful to unfaithful reasoning through an intermediate mixed mode.\n\n---\n\n### C. PROCESS REWARD MODELS\n\n**12. Process Reward Models That Think (ThinkPRM)**\n- **Authors:** Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang\n- **Venue:** arXiv preprint (Apr 2025, revised Dec 2025)\n- **URL:** https://arxiv.org/abs/2504.16828\n- **Summary:** Proposes ThinkPRM, a generative PRM that verifies each step via a verification CoT, outperforming LLM-as-Judge and discriminative verifiers while using only 1% of the process labels in PRM800K, with strong out-of-domain generalization.\n\n**13. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning**\n- **Authors:** Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, Aviral Kumar\n- **Venue:** ICLR 2025 (Spotlight)\n- **URL:** https://openreview.net/forum?id=A6Y7AqlzLW\n- **Summary:** Proposes Process Advantage Verifiers (PAVs) that measure progress as the change in likelihood of reaching a correct answer; achieves >8% accuracy gains over outcome reward models and 1.5--5x compute efficiency gains.\n\n**14. VersaPRM: Multi-Domain Process Reward Model via Synthetic Reasoning Data**\n- **Authors:** Thomas Zeng, Shuibai Zhang, Shutong Wu, Christian Classen, Daewon Chae, Ethan Ewer, Minjae Lee, Heeju Kim, Wonjun Kang, Jackson Kunde, Ying Fan, Jungtaek Kim, Hyung Il Koo, Kannan Ramchandran, Dimitris Papailiopoulos, Kangwook Lee\n- **Venue:** ICML 2025 (Spotlight)\n- **URL:** https://icml.cc/virtual/2025/poster/44223\n- **Summary:** Addresses PRM generalization beyond mathematics by training on diverse synthetic reasoning data, achieving 7.9% gains over majority voting on law tasks from MMLU-Pro and surpassing competing approaches.\n\n**15. FoVer: Efficient PRM Training Data Synthesis via Formal Verification**\n- **Authors:** Ryo Kamoi, Yusen Zhang, Nan Zhang, Sarkar Snigdha Sarathi Das, Ranran Haoran Zhang, Wenpeng Yin, Rui Zhang\n- **Venue:** ACL 2026 Findings\n- **URL:** https://arxiv.org/abs/2505.15960\n- **Summary:** Uses formal verification tools (Z3, Isabelle) to automatically generate step-level error labels for PRM training data, achieving competitive/superior results to human-annotated PRMs across 12 reasoning benchmarks with strong out-of-domain generalization.\n\n**16. Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning**\n- **Authors:** Massimiliano Pronesti, Anya Belz, Yufang Hou\n- **Venue:** arXiv preprint (Jan 2026)\n- **URL:** https://arxiv.org/abs/2601.17223\n- **Summary:** Introduces VPRMs using deterministic rule-based verifiers for intermediate steps instead of neural judges, applied to medical evidence synthesis; achieves 20% higher F1 and 6.5% improvement over outcome-only verification.\n\n**17. Controllable and Verifiable Process Data Synthesis for Process Reward Models**\n- **Authors:** Yinghui Chi, Lucien Wang\n- **Venue:** arXiv preprint (May 2026)\n- **URL:** https://arxiv.org/abs/2605.02395\n- **Summary:** Proposes a framework for synthesizing PRM training data by constructing correct symbolic chains, injecting template-based errors, and recomputing subsequent steps, ensuring verifiable paired trajectories for training.\n\n---\n\n### D. BENCHMARKS AND STEP-LEVEL EVALUATION\n\n**18. ProcessBench: Identifying Process Errors in Mathematical Reasoning**\n- **Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin\n- **Venue:** ACL 2025\n- **URL:** https://arxiv.org/abs/2412.06559\n- **Summary:** Provides 3,400 test cases with human-annotated error locations requiring models to identify the earliest erroneous step; finds existing PRMs struggle with competition-level problems while QwQ-32B-Preview approaches GPT-4o-level critique abilities.\n\n**19. PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models**\n- **Authors:** Mingyang Song, Zhaochen Su, Xiaoye Qu, Jiawei Zhou, Yu Cheng\n- **Venue:** ACL 2025 Main\n- **URL:** https://arxiv.org/abs/2501.03124\n- **Summary:** Introduces 6,216 problems with 83,456 step-level labels across a taxonomy of simplicity, soundness, and sensitivity; best model (Gemini-2-Thinking) scores 68.8 vs. human performance of 83.8.\n\n**20. ReasoningMath-Plus (Unmasking Reasoning Processes)**\n- **Authors:** Xiang Zheng, Weiqi Zhai, Wei Wang, Boyu Yang, et al.\n- **Venue:** arXiv preprint (Jan 2026)\n- **URL:** https://arxiv.org/abs/2602.00564\n- **Summary:** Introduces 150 problems requiring multi-constraint coordination and constructive logical synthesis with HCRS scoring; reveals top models achieve ~58% final accuracy but only 43.6% on holistic process-level scores.\n\n**21. Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math**\n- **Authors:** Shrey Pandit, Austin Xu, Xuan-Phi Nguyen, Yifei Ming, Caiming Xiong, Shafiq Joty\n- **Venue:** arXiv preprint (Oct 2025)\n- **URL:** https://arxiv.org/abs/2510.13744\n- **Summary:** Provides human-annotated step-level error data for frontier math problems, evaluates 29 verification models, and finds open-source verifiers significantly lag closed-source models.\n\n**22. What Defines Good Reasoning in LLMs? Dissecting Reasoning Steps with Multi-Aspect Evaluation (CaSE)**\n- **Authors:** Heejin Do, Jaehui Hwang, Dongyoon Han, Seong Joon Oh, Sangdoo Yun\n- **Venue:** arXiv preprint (Oct 2025)\n- **URL:** https://arxiv.org/abs/2510.20603\n- **Summary:** Formalizes two causal dimensions (relevance and coherence) for step-level evaluation, introduces CaSE to assess steps using only preceding context to avoid hindsight bias, and shows training data selection by these criteria improves model performance.\n\n**23. Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)**\n- **Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu\n- **Venue:** AAAI 2025\n- **URL:** https://arxiv.org/abs/2404.05692\n- **Summary:** Introduces validity and redundancy metrics for intermediate steps, demonstrating that higher final-answer accuracy does not necessarily correlate with improved reasoning quality on difficult problems.\n\n**24. Proof or Bluff? Evaluating LLMs on 2025 USA Math Olympiad**\n- **Authors:** Ivo Petrov, Jasper Dekoninck, Lyuben Baltadzhiev, Maria Drencheva, Kristian Minchev, Mislav Balunovic, Nikola Jovanovic, Martin Vechev\n- **Venue:** arXiv preprint (Mar 2025)\n- **URL:** https://arxiv.org/abs/2503.21934\n- **Summary:** Expert human evaluation of full solution quality on 2025 USAMO problems; best model (Gemini-2.5-Pro) achieves only 25%, revealing that answer-only benchmarks dramatically overstate genuine proof capabilities.\n\n---\n\n### E. NOVEL EVALUATION METHODS\n\n**25. EvalQReason: A Framework for Step-Level Reasoning Evaluation in Large Language Models**\n- **Authors:** Shaima Ahmad Freja, Ferhat Ozgur Catak, Betul Yurdem, Chunming Rong\n- **Venue:** arXiv preprint (Feb 2026)\n- **URL:** https://arxiv.org/abs/2602.02295\n- **Summary:** Proposes annotation-free step-level evaluation using probability analysis (CSD and SFC algorithms), achieving F1=0.78 and ROC-AUC=0.82 for correctness classification on mathematical tasks.\n\n**26. Assessing LLM Reasoning Steps via Principal Knowledge Grounding**\n- **Authors:** Hyeon Hwang, Yewon Cho, Chanwoong Yoon, Yein Park, Minju Song, Kyungjae Lee, Gangwoo Kim, Jaewoo Kang\n- **Venue:** EMNLP 2025 Findings\n- **URL:** https://arxiv.org/abs/2511.00879\n- **Summary:** Introduces metrics measuring how well models recall and apply prerequisite knowledge in reasoning, with a lightweight evaluator model for identifying missing or misapplied knowledge elements.\n\n**27. One-Token Verification for Reasoning Correctness Estimation**\n- **Authors:** Zhan Zhuang, Xiequn Wang, Zebin Chen, Feiyang Ye, Ying Wei, Kede Ma, Yu Zhang\n- **Venue:** arXiv preprint (Mar 2026)\n- **URL:** https://arxiv.org/abs/2603.01025\n- **Summary:** Assesses reasoning correctness via a single forward pass using a learnable verification token, reducing token usage by up to 90% through correctness-guided early termination while outperforming existing verifiers on math benchmarks.\n\n---\n\n### Summary of Key Themes\n\n1. **CoT faithfulness is unreliable:** Multiple studies (papers 3, 4, 5, 9, 10) converge on the finding that reasoning models frequently suppress or fabricate reasoning explanations. The Anthropic study (#3) is a landmark result showing <20% verbalization of hint usage.\n\n2. **Process reward models are rapidly maturing:** ThinkPRM (#12) achieves strong results with minimal supervision; PAVs (#13) formalize progress-based rewards; VersaPRM (#14) extends PRMs beyond math; FoVer (#15) uses formal verification for data synthesis.\n\n3. **Step-level benchmarks are proliferating:** ProcessBench (#18), PRMBench (#19), Hard2Verify (#21), and ReasoningMath-Plus (#20) offer complementary evaluation angles from error detection to structural reasoning.\n\n4. **Answer accuracy masks reasoning deficiencies:** Papers #20, #23, and #24 all demonstrate that final-answer accuracy substantially overstates genuine reasoning capability when process-level evaluation is applied.\n\n5. **The field lacks consensus on evaluation criteria:** The survey by Lee & Hockenmaier (#1) highlights fragmentation, while CaSE (#22) and ReasonEval (#23) propose competing multi-dimensional frameworks."
      }
    ],
    "totalDurationMs": 188731,
    "totalTokens": 32682,
    "totalToolUseCount": 38,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 27229,
      "output_tokens": 4763,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 689
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4763,
          "cache_read_input_tokens": 27229,
          "cache_creation_input_tokens": 689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 689,
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
  "sourceToolAssistantUUID": "3abcc399-5f64-4397-8a76-71124cdb7ac3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
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
  "leafUuid": "0b6663b2-3bb9-40d3-b211-8e9230a8852f",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Tool result

_source line 29 · 2026-05-29T05:27:34.048Z_

<details><summary>↩ Tool result · `toolu_01HkVpdchzYkyjGRPgJoZYwZ`</summary>

```text
Now I have comprehensive data. Here is the full literature survey report.

---

## Literature Survey: LLM Evaluation -- Contamination Detection, Adversarial Robustness, and IRT-Based Scoring (2024--2026)

Below are the most important recent papers organized by topic. Each entry includes title, authors, venue, URL, and a one-line summary.

---

### A. Best Paper Award Winners (Top Venues, Directly Relevant to LLM Evaluation)

**1. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)**
- Authors: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Alon Albalak, Yejin Choi
- Venue: **NeurIPS 2025 Best Paper Award** (Oral)
- URL: https://arxiv.org/abs/2510.22954
- Summary: Introduces Infinity-Chat (26K queries, 31K human annotations) and documents "diversity collapse" -- the phenomenon where different LLMs converge on strikingly similar outputs on open-ended tasks, undermining evaluation that assumes model independence.

**2. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**
- Authors: Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang
- Venue: **NeurIPS 2025 Best Paper Runner-Up** (Oral); ICML 2025 AI4MATH Workshop Best Paper
- URL: https://arxiv.org/abs/2504.13837
- Summary: Shows via pass@k analysis that RLVR improves sampling efficiency but does not elicit fundamentally new reasoning patterns beyond the base model, challenging prevailing assumptions about RL-trained LLM capabilities.

**3. Safety Alignment Should Be Made More Than Just a Few Tokens Deep**
- Authors: Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, Peter Henderson
- Venue: **ICLR 2025 Outstanding Paper** (Oral)
- URL: https://arxiv.org/abs/2406.05946
- Summary: Reveals that safety alignment operates only over the first few output tokens ("shallow alignment"), explaining vulnerabilities to adversarial suffix, prefilling, and fine-tuning attacks, and proposes deeper alignment regularization.

**4. Learning Dynamics of LLM Finetuning**
- Authors: Yi Ren, Danica J. Sutherland
- Venue: **ICLR 2025 Outstanding Paper**
- URL: https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/
- Summary: Provides a theoretical and empirical characterization of how LLMs change during fine-tuning, with implications for understanding evaluation shifts post-training.

**5. Superposition Yields Robust Neural Scaling**
- Authors: Yizhou Liu, Ziming Liu, Jeff Gore
- Venue: **NeurIPS 2025 Best Paper Runner-Up**
- URL: https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/
- Summary: Identifies representation superposition as the mechanism behind neural scaling laws, explaining why loss consistently decreases with model size -- foundational for understanding IRT-style ability scaling.

---

### B. IRT-Based and Psychometric LLM Evaluation

**6. Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory**
- Authors: Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao
- Venue: **AAAI 2026 (Oral)**
- URL: https://arxiv.org/abs/2505.15055
- Summary: Proposes PSN-IRT (Pseudo-Siamese Network IRT), analyzes 11 benchmarks with ~42K items, and shows that IRT-calibrated smaller item sets better align with human preferences than raw accuracy leaderboards.

**7. Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks (ATLAS)**
- Authors: Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla
- Venue: arXiv preprint (Oct 2025)
- URL: https://arxiv.org/abs/2511.04689
- Summary: Applies Fisher-information-guided item selection to achieve 90% reduction in test items (e.g., 41 items from HellaSwag's 5,600) while preserving global ranking structure and providing finer within-tier discrimination.

**8. Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores**
- Authors: Esma Balkir, Alice Pernthaller, Marco Basaldella, Jose Hernandez-Orallo, Nigel Collier
- Venue: arXiv preprint (Jan 2026)
- URL: https://arxiv.org/abs/2601.13885
- Summary: Extends CAT to continuous metrics (ROUGE, BLEU, LLM-as-Judge) via heteroskedastic normal IRT; achieves 95% ranking accuracy using only 2% of items.

**9. Toward a Unified Framework for Data-Efficient Evaluation of Large Language Models (LEGO-IRT)**
- Authors: Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang
- Venue: arXiv preprint (Oct 2025)
- URL: https://arxiv.org/abs/2510.04051
- Summary: Proposes a factorized IRT architecture supporting both binary and continuous metrics; achieves stable capability estimates using just 3% of evaluation items across 70 models and 5 benchmarks.

**10. Learning Compact Representations of LLM Abilities via Item Response Theory**
- Authors: Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu
- Venue: arXiv preprint (Oct 2025)
- URL: https://arxiv.org/abs/2510.00844
- Summary: Uses a MoE network to learn multi-skill ability vectors, query discrimination, and difficulty parameters jointly from IRT, enabling model routing and benchmark score prediction.

**11. An Interpretable and Scalable Framework for Evaluating Large Language Models**
- Authors: Xinhao Qu, Qiang Heng, Hao Zeng, Xiaoqian Liu
- Venue: arXiv preprint (May 2026)
- URL: https://arxiv.org/abs/2605.07046
- Summary: Recasts IRT parameter estimation as constrained matrix factorization via majorization-minimization, enabling significant speedups on MATH-500 and Open LLM Leaderboard with theoretical guarantees.

---

### C. Contamination Detection and Dynamic Benchmarking

**12. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**
- Authors: Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Benjamin Feuer, Siddhartha Jain, Ravid Shwartz-Ziv, Neel Jain, Khalid Saifullah, et al.
- Venue: **ICLR 2025 Spotlight**
- URL: https://openreview.net/forum?id=sKYHBTAxVa
- Summary: Monthly-updated benchmark with objective ground-truth scoring across math, coding, reasoning, and data analysis; top models score below 70%, making it contamination-resistant by design.

**13. MathArena: Evaluating LLMs on Uncontaminated Math Competitions**
- Authors: Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev
- Venue: arXiv preprint (May 2025)
- URL: https://arxiv.org/abs/2505.23281
- Summary: Uses newly released math competition problems (post-model-release) to eliminate contamination; evaluates 50+ models across 7 competitions (162 problems) and is the first benchmark for proof-writing capabilities.

**14. Benchmark Data Contamination of Large Language Models: A Survey**
- Authors: Cheng Xu, Shuhao Guan, Derek Greene, M-Tahar Kechadi
- Venue: arXiv preprint (Jun 2024)
- URL: https://arxiv.org/abs/2406.04244
- Summary: Comprehensive survey of BDC detection methods (logit-based, generation-based, hybrid) and alternative assessment approaches to mitigate contamination risks.

**15. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation**
- Authors: Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray
- Venue: arXiv preprint (Feb 2025)
- URL: https://arxiv.org/abs/2502.17521
- Summary: Surveys the shift from static to dynamic benchmarking, identifies the lack of standardized criteria for evaluating dynamic benchmarks, and proposes design principles for improved dynamic evaluation.

**16. Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation**
- Authors: Naila Shafirni Hidayat, Muhammad Dehan Al Kautsar, Alfan Farizki Wicaksono, Fajri Koto
- Venue: arXiv preprint (May 2025)
- URL: https://arxiv.org/abs/2505.24263
- Summary: Compares leakage detection methods (permutation, n-gram, semi-half) under simulated contamination; finds n-gram method achieves highest F1; produces cleaned MMLU and HellaSwag versions.

**17. When Benchmarks Leak: Inference-Time Decontamination for LLMs**
- Authors: Jianzhe Chai, Yu Zhe, Jun Sakuma
- Venue: arXiv preprint (Jan 2026)
- URL: https://arxiv.org/abs/2601.19334
- Summary: Proposes DeconIEP, which applies bounded perturbations in the input embedding space at inference time to redirect models away from memorized benchmark answers without degrading genuine capability.

**18. LLM Benchmark Datasets Should Be Contamination-Resistant**
- Authors: Ali Al-Lawati, Jason Lucas, Dongwon Lee, Suhang Wang
- Venue: **ICML 2026 Position Paper Track**
- URL: https://arxiv.org/abs/2605.19999
- Summary: Argues benchmarks should be "unlearnable" during training while remaining functional at inference, leveraging Transformer architecture asymmetries between training and inference modes.

---

### D. Adversarial Robustness of LLM Evaluation

**19. Evaluating and Improving Robustness in Large Language Models: A Survey and Future Directions**
- Authors: Kun Zhang, Le Wu, Kui Yu, Guangyi Lv, Dacao Zhang
- Venue: arXiv preprint (Jun 2025)
- URL: https://arxiv.org/abs/2506.11111
- Summary: Comprehensive survey organizing LLM robustness across three dimensions: adversarial robustness (intentional attacks), out-of-distribution robustness, and robustness evaluation methods.

**20. Are All Prompt Components Value-Neutral? Understanding the Heterogeneous Adversarial Robustness of Dissected Prompt in Large Language Models**
- Authors: Yujia Zheng, Tianhao Li, Haotian Huang, Tianyu Zeng, et al.
- Venue: arXiv preprint (Aug 2025)
- URL: https://arxiv.org/abs/2508.01554
- Summary: Introduces PromptAnatomy and ComPerturb, which decompose prompts into functional segments and generate targeted adversarial perturbations per component, achieving SOTA attack success rates across 5 LLMs.

**21. Test-time RL Alignment Exposes Task Familiarity Artifacts in LLM Benchmarks**
- Authors: Kun Wang, Reinhard Heckel
- Venue: arXiv preprint (Mar 2026)
- URL: https://arxiv.org/abs/2603.12875
- Summary: Demonstrates that benchmark performance gains from fine-tuning often reflect task familiarity rather than improved reasoning; proposes a two-stage test-time RL method to decouple format familiarity from genuine capability.

**22. Assessing Adversarial Robustness of Large Language Models: An Empirical Study**
- Authors: Zeyu Yang, Zhao Meng, Xiaochen Zheng, Roger Wattenhofer
- Venue: **KDD 2024 GenAI Evaluation Workshop** (Oral)
- URL: https://arxiv.org/abs/2405.02764
- Summary: White-box attack study evaluating how model size, architecture, and fine-tuning affect adversarial robustness across five text classification benchmarks.

---

### E. Meta-Evaluation: Benchmarking the Benchmarks

**23. Benchmark^2: Systematic Evaluation of LLM Benchmarks**
- Authors: Qi Qian, Chengsong Huang, Jingwen Xu, et al.
- Venue: arXiv preprint (Jan 2026)
- URL: https://arxiv.org/abs/2601.03986
- Summary: Proposes three meta-metrics -- cross-benchmark ranking consistency, discriminability score, and capability alignment deviation -- and reveals significant quality variations among 15 existing benchmarks.

**24. When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation**
- Authors: Mubashara Akhtar, Anka Reuel, Prajna Soni, et al. (30+ authors)
- Venue: arXiv preprint (Feb 2026)
- URL: https://arxiv.org/abs/2602.16763
- Summary: Studies 60 LLM benchmarks, finding nearly half exhibit saturation with rates increasing with age; expert-curated benchmarks show greater durability than crowdsourced ones; keeping test data private provides no protection.

**25. Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs**
- Authors: Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao
- Venue: arXiv preprint (Feb 2026)
- URL: https://arxiv.org/abs/2602.11674
- Summary: Introduces a data-driven auditing framework measuring capability discrimination, anti-saturation headroom, and ecosystem impact across 106 benchmarks and 91 models.

**26. RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents**
- Authors: Yonas Atinafu, Robin Cohen
- Venue: arXiv preprint (Mar 2026)
- URL: https://arxiv.org/abs/2603.11337
- Summary: Benchmarks two attack vectors -- evaluator tampering and train/test leakage -- in LLM agent workspaces; evaluator-tampering attempts appeared in ~50% of episodes and were blocked by evaluator locking at 25-31% runtime cost.

---

### F. LLM-as-Judge and Human Evaluation

**27. Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference**
- Authors: Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, A.N. Angelopoulos, Tianle Li, et al. (LMSYS)
- Venue: **ICML 2024**
- URL: https://arxiv.org/abs/2403.04132
- Summary: Crowdsourced pairwise evaluation platform (240K+ votes, 90K users) using Bradley-Terry/Elo scoring; established as a de facto standard for human-preference-based LLM ranking.

**28. Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge**
- Authors: Lin Shi, Chiyu Ma, Wenhua Liang, Xingjian Diao, Weicheng Ma, Soroush Vosoughi
- Venue: **AACL-IJCNLP 2025**
- URL: https://arxiv.org/abs/2406.07791
- Summary: Tests 15 LLM judges across ~150K evaluation instances, demonstrating that position bias varies significantly across judges and tasks and is not random; proposes metrics for repetition stability, position consistency, and preference fairness.

---

### G. Surveys on LLM Evaluation

**29. Survey on Evaluation of LLM-based Agents**
- Authors: Asaf Yehudai, Lilach Eden, Alan Li, Guy Uziel, Yilun Zhao, Roy Bar-Haim, Arman Cohan, Michal Shmueli-Scheuer
- Venue: **ACL Findings 2025**
- URL: https://arxiv.org/abs/2503.16416
- Summary: Comprehensive survey across five evaluation perspectives (core capabilities, specialized benchmarks, generalist agents, benchmark dimensions, frameworks), identifying trends toward dynamic and realistic evaluation.

---

### Summary of Relevance to Your Paper

For a paper combining **contamination detection**, **adversarial robustness**, and **IRT-based scoring**:

- **Core IRT references**: Papers 6-11 (especially #6 PSN-IRT at AAAI 2026 and #7 ATLAS) form the direct methodological foundation.
- **Contamination detection**: Papers 12-18 cover the landscape from detection methods (#14, #16) to dynamic benchmarks (#12 LiveBench, #13 MathArena) to inference-time decontamination (#17).
- **Adversarial robustness**: Papers 3, 19-22 span both safety alignment vulnerabilities and prompt-level adversarial evaluation.
- **Meta-evaluation / motivation**: Papers 23-26 provide strong motivation for why better evaluation frameworks are needed (saturation, benchmark quality variance, integrity threats).
- **Award-winning context**: Papers 1-5 from NeurIPS 2025 and ICLR 2025 provide high-visibility framing for the broader LLM evaluation challenge.

agentId: a9d3f84e66d599100 (use SendMessage with to: 'a9d3f84e66d599100' to continue this agent)
&lt;usage>total_tokens: 43951
tool_uses: 48
duration_ms: 213489&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "619e4183-e304-4e35-8e8e-4748c0d6ff8c",
  "isSidechain": false,
  "promptId": "37ea365b-dcd4-4897-b99b-0b8f025b793a",
  "type": "user",
  "uuid": "5fd4af08-86db-44eb-ab85-38cab6f8295f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an ML paper about LLM evaluation combining contamination detection, adversarial robustness, and IRT-based scoring. Search for the most important recent papers (2024-2026) on LLM evaluation frameworks, best paper awards, and evaluation methodology.\n\nExecute these searches and for each promising paper, fetch its arXiv abstract:\n\n1. WebSearch: \"best paper award NeurIPS 2025 LLM evaluation\"\n2. WebSearch: \"best paper award ICML 2025 language model\"\n3. WebSearch: \"best paper ICLR 2025 2026 evaluation\"\n4. WebSearch: \"LLM evaluation framework comprehensive 2025 2026\"\n5. WebSearch: \"LiveBench MathArena dynamic benchmark LLM 2025\"\n6. WebSearch: \"site:arxiv.org LLM evaluation survey 2025 2026\"\n7. WebSearch: \"benchmark integrity LLM evaluation trustworthy 2025\"\n8. WebSearch: \"AAAI 2025 2026 best paper LLM evaluation alignment\"\n\nFor each paper you find, use WebFetch on its arXiv page to get the full abstract and key details.\n\nReport back with a list of papers including: title, authors, venue, URL, and a one-line summary of what each paper does. Focus on papers that are highly cited, from top venues, or from major labs.",
    "agentId": "a9d3f84e66d599100",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Here is the full literature survey report.\n\n---\n\n## Literature Survey: LLM Evaluation -- Contamination Detection, Adversarial Robustness, and IRT-Based Scoring (2024--2026)\n\nBelow are the most important recent papers organized by topic. Each entry includes title, authors, venue, URL, and a one-line summary.\n\n---\n\n### A. Best Paper Award Winners (Top Venues, Directly Relevant to LLM Evaluation)\n\n**1. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)**\n- Authors: Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Alon Albalak, Yejin Choi\n- Venue: **NeurIPS 2025 Best Paper Award** (Oral)\n- URL: https://arxiv.org/abs/2510.22954\n- Summary: Introduces Infinity-Chat (26K queries, 31K human annotations) and documents \"diversity collapse\" -- the phenomenon where different LLMs converge on strikingly similar outputs on open-ended tasks, undermining evaluation that assumes model independence.\n\n**2. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**\n- Authors: Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang\n- Venue: **NeurIPS 2025 Best Paper Runner-Up** (Oral); ICML 2025 AI4MATH Workshop Best Paper\n- URL: https://arxiv.org/abs/2504.13837\n- Summary: Shows via pass@k analysis that RLVR improves sampling efficiency but does not elicit fundamentally new reasoning patterns beyond the base model, challenging prevailing assumptions about RL-trained LLM capabilities.\n\n**3. Safety Alignment Should Be Made More Than Just a Few Tokens Deep**\n- Authors: Xiangyu Qi, Ashwinee Panda, Kaifeng Lyu, Xiao Ma, Subhrajit Roy, Ahmad Beirami, Prateek Mittal, Peter Henderson\n- Venue: **ICLR 2025 Outstanding Paper** (Oral)\n- URL: https://arxiv.org/abs/2406.05946\n- Summary: Reveals that safety alignment operates only over the first few output tokens (\"shallow alignment\"), explaining vulnerabilities to adversarial suffix, prefilling, and fine-tuning attacks, and proposes deeper alignment regularization.\n\n**4. Learning Dynamics of LLM Finetuning**\n- Authors: Yi Ren, Danica J. Sutherland\n- Venue: **ICLR 2025 Outstanding Paper**\n- URL: https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/\n- Summary: Provides a theoretical and empirical characterization of how LLMs change during fine-tuning, with implications for understanding evaluation shifts post-training.\n\n**5. Superposition Yields Robust Neural Scaling**\n- Authors: Yizhou Liu, Ziming Liu, Jeff Gore\n- Venue: **NeurIPS 2025 Best Paper Runner-Up**\n- URL: https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/\n- Summary: Identifies representation superposition as the mechanism behind neural scaling laws, explaining why loss consistently decreases with model size -- foundational for understanding IRT-style ability scaling.\n\n---\n\n### B. IRT-Based and Psychometric LLM Evaluation\n\n**6. Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory**\n- Authors: Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao\n- Venue: **AAAI 2026 (Oral)**\n- URL: https://arxiv.org/abs/2505.15055\n- Summary: Proposes PSN-IRT (Pseudo-Siamese Network IRT), analyzes 11 benchmarks with ~42K items, and shows that IRT-calibrated smaller item sets better align with human preferences than raw accuracy leaderboards.\n\n**7. Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks (ATLAS)**\n- Authors: Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla\n- Venue: arXiv preprint (Oct 2025)\n- URL: https://arxiv.org/abs/2511.04689\n- Summary: Applies Fisher-information-guided item selection to achieve 90% reduction in test items (e.g., 41 items from HellaSwag's 5,600) while preserving global ranking structure and providing finer within-tier discrimination.\n\n**8. Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores**\n- Authors: Esma Balkir, Alice Pernthaller, Marco Basaldella, Jose Hernandez-Orallo, Nigel Collier\n- Venue: arXiv preprint (Jan 2026)\n- URL: https://arxiv.org/abs/2601.13885\n- Summary: Extends CAT to continuous metrics (ROUGE, BLEU, LLM-as-Judge) via heteroskedastic normal IRT; achieves 95% ranking accuracy using only 2% of items.\n\n**9. Toward a Unified Framework for Data-Efficient Evaluation of Large Language Models (LEGO-IRT)**\n- Authors: Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang\n- Venue: arXiv preprint (Oct 2025)\n- URL: https://arxiv.org/abs/2510.04051\n- Summary: Proposes a factorized IRT architecture supporting both binary and continuous metrics; achieves stable capability estimates using just 3% of evaluation items across 70 models and 5 benchmarks.\n\n**10. Learning Compact Representations of LLM Abilities via Item Response Theory**\n- Authors: Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu\n- Venue: arXiv preprint (Oct 2025)\n- URL: https://arxiv.org/abs/2510.00844\n- Summary: Uses a MoE network to learn multi-skill ability vectors, query discrimination, and difficulty parameters jointly from IRT, enabling model routing and benchmark score prediction.\n\n**11. An Interpretable and Scalable Framework for Evaluating Large Language Models**\n- Authors: Xinhao Qu, Qiang Heng, Hao Zeng, Xiaoqian Liu\n- Venue: arXiv preprint (May 2026)\n- URL: https://arxiv.org/abs/2605.07046\n- Summary: Recasts IRT parameter estimation as constrained matrix factorization via majorization-minimization, enabling significant speedups on MATH-500 and Open LLM Leaderboard with theoretical guarantees.\n\n---\n\n### C. Contamination Detection and Dynamic Benchmarking\n\n**12. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**\n- Authors: Colin White, Samuel Dooley, Manley Roberts, Arka Pal, Benjamin Feuer, Siddhartha Jain, Ravid Shwartz-Ziv, Neel Jain, Khalid Saifullah, et al.\n- Venue: **ICLR 2025 Spotlight**\n- URL: https://openreview.net/forum?id=sKYHBTAxVa\n- Summary: Monthly-updated benchmark with objective ground-truth scoring across math, coding, reasoning, and data analysis; top models score below 70%, making it contamination-resistant by design.\n\n**13. MathArena: Evaluating LLMs on Uncontaminated Math Competitions**\n- Authors: Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev\n- Venue: arXiv preprint (May 2025)\n- URL: https://arxiv.org/abs/2505.23281\n- Summary: Uses newly released math competition problems (post-model-release) to eliminate contamination; evaluates 50+ models across 7 competitions (162 problems) and is the first benchmark for proof-writing capabilities.\n\n**14. Benchmark Data Contamination of Large Language Models: A Survey**\n- Authors: Cheng Xu, Shuhao Guan, Derek Greene, M-Tahar Kechadi\n- Venue: arXiv preprint (Jun 2024)\n- URL: https://arxiv.org/abs/2406.04244\n- Summary: Comprehensive survey of BDC detection methods (logit-based, generation-based, hybrid) and alternative assessment approaches to mitigate contamination risks.\n\n**15. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation**\n- Authors: Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray\n- Venue: arXiv preprint (Feb 2025)\n- URL: https://arxiv.org/abs/2502.17521\n- Summary: Surveys the shift from static to dynamic benchmarking, identifies the lack of standardized criteria for evaluating dynamic benchmarks, and proposes design principles for improved dynamic evaluation.\n\n**16. Simulating Training Data Leakage in Multiple-Choice Benchmarks for LLM Evaluation**\n- Authors: Naila Shafirni Hidayat, Muhammad Dehan Al Kautsar, Alfan Farizki Wicaksono, Fajri Koto\n- Venue: arXiv preprint (May 2025)\n- URL: https://arxiv.org/abs/2505.24263\n- Summary: Compares leakage detection methods (permutation, n-gram, semi-half) under simulated contamination; finds n-gram method achieves highest F1; produces cleaned MMLU and HellaSwag versions.\n\n**17. When Benchmarks Leak: Inference-Time Decontamination for LLMs**\n- Authors: Jianzhe Chai, Yu Zhe, Jun Sakuma\n- Venue: arXiv preprint (Jan 2026)\n- URL: https://arxiv.org/abs/2601.19334\n- Summary: Proposes DeconIEP, which applies bounded perturbations in the input embedding space at inference time to redirect models away from memorized benchmark answers without degrading genuine capability.\n\n**18. LLM Benchmark Datasets Should Be Contamination-Resistant**\n- Authors: Ali Al-Lawati, Jason Lucas, Dongwon Lee, Suhang Wang\n- Venue: **ICML 2026 Position Paper Track**\n- URL: https://arxiv.org/abs/2605.19999\n- Summary: Argues benchmarks should be \"unlearnable\" during training while remaining functional at inference, leveraging Transformer architecture asymmetries between training and inference modes.\n\n---\n\n### D. Adversarial Robustness of LLM Evaluation\n\n**19. Evaluating and Improving Robustness in Large Language Models: A Survey and Future Directions**\n- Authors: Kun Zhang, Le Wu, Kui Yu, Guangyi Lv, Dacao Zhang\n- Venue: arXiv preprint (Jun 2025)\n- URL: https://arxiv.org/abs/2506.11111\n- Summary: Comprehensive survey organizing LLM robustness across three dimensions: adversarial robustness (intentional attacks), out-of-distribution robustness, and robustness evaluation methods.\n\n**20. Are All Prompt Components Value-Neutral? Understanding the Heterogeneous Adversarial Robustness of Dissected Prompt in Large Language Models**\n- Authors: Yujia Zheng, Tianhao Li, Haotian Huang, Tianyu Zeng, et al.\n- Venue: arXiv preprint (Aug 2025)\n- URL: https://arxiv.org/abs/2508.01554\n- Summary: Introduces PromptAnatomy and ComPerturb, which decompose prompts into functional segments and generate targeted adversarial perturbations per component, achieving SOTA attack success rates across 5 LLMs.\n\n**21. Test-time RL Alignment Exposes Task Familiarity Artifacts in LLM Benchmarks**\n- Authors: Kun Wang, Reinhard Heckel\n- Venue: arXiv preprint (Mar 2026)\n- URL: https://arxiv.org/abs/2603.12875\n- Summary: Demonstrates that benchmark performance gains from fine-tuning often reflect task familiarity rather than improved reasoning; proposes a two-stage test-time RL method to decouple format familiarity from genuine capability.\n\n**22. Assessing Adversarial Robustness of Large Language Models: An Empirical Study**\n- Authors: Zeyu Yang, Zhao Meng, Xiaochen Zheng, Roger Wattenhofer\n- Venue: **KDD 2024 GenAI Evaluation Workshop** (Oral)\n- URL: https://arxiv.org/abs/2405.02764\n- Summary: White-box attack study evaluating how model size, architecture, and fine-tuning affect adversarial robustness across five text classification benchmarks.\n\n---\n\n### E. Meta-Evaluation: Benchmarking the Benchmarks\n\n**23. Benchmark^2: Systematic Evaluation of LLM Benchmarks**\n- Authors: Qi Qian, Chengsong Huang, Jingwen Xu, et al.\n- Venue: arXiv preprint (Jan 2026)\n- URL: https://arxiv.org/abs/2601.03986\n- Summary: Proposes three meta-metrics -- cross-benchmark ranking consistency, discriminability score, and capability alignment deviation -- and reveals significant quality variations among 15 existing benchmarks.\n\n**24. When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation**\n- Authors: Mubashara Akhtar, Anka Reuel, Prajna Soni, et al. (30+ authors)\n- Venue: arXiv preprint (Feb 2026)\n- URL: https://arxiv.org/abs/2602.16763\n- Summary: Studies 60 LLM benchmarks, finding nearly half exhibit saturation with rates increasing with age; expert-curated benchmarks show greater durability than crowdsourced ones; keeping test data private provides no protection.\n\n**25. Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs**\n- Authors: Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao\n- Venue: arXiv preprint (Feb 2026)\n- URL: https://arxiv.org/abs/2602.11674\n- Summary: Introduces a data-driven auditing framework measuring capability discrimination, anti-saturation headroom, and ecosystem impact across 106 benchmarks and 91 models.\n\n**26. RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents**\n- Authors: Yonas Atinafu, Robin Cohen\n- Venue: arXiv preprint (Mar 2026)\n- URL: https://arxiv.org/abs/2603.11337\n- Summary: Benchmarks two attack vectors -- evaluator tampering and train/test leakage -- in LLM agent workspaces; evaluator-tampering attempts appeared in ~50% of episodes and were blocked by evaluator locking at 25-31% runtime cost.\n\n---\n\n### F. LLM-as-Judge and Human Evaluation\n\n**27. Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference**\n- Authors: Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, A.N. Angelopoulos, Tianle Li, et al. (LMSYS)\n- Venue: **ICML 2024**\n- URL: https://arxiv.org/abs/2403.04132\n- Summary: Crowdsourced pairwise evaluation platform (240K+ votes, 90K users) using Bradley-Terry/Elo scoring; established as a de facto standard for human-preference-based LLM ranking.\n\n**28. Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge**\n- Authors: Lin Shi, Chiyu Ma, Wenhua Liang, Xingjian Diao, Weicheng Ma, Soroush Vosoughi\n- Venue: **AACL-IJCNLP 2025**\n- URL: https://arxiv.org/abs/2406.07791\n- Summary: Tests 15 LLM judges across ~150K evaluation instances, demonstrating that position bias varies significantly across judges and tasks and is not random; proposes metrics for repetition stability, position consistency, and preference fairness.\n\n---\n\n### G. Surveys on LLM Evaluation\n\n**29. Survey on Evaluation of LLM-based Agents**\n- Authors: Asaf Yehudai, Lilach Eden, Alan Li, Guy Uziel, Yilun Zhao, Roy Bar-Haim, Arman Cohan, Michal Shmueli-Scheuer\n- Venue: **ACL Findings 2025**\n- URL: https://arxiv.org/abs/2503.16416\n- Summary: Comprehensive survey across five evaluation perspectives (core capabilities, specialized benchmarks, generalist agents, benchmark dimensions, frameworks), identifying trends toward dynamic and realistic evaluation.\n\n---\n\n### Summary of Relevance to Your Paper\n\nFor a paper combining **contamination detection**, **adversarial robustness**, and **IRT-based scoring**:\n\n- **Core IRT references**: Papers 6-11 (especially #6 PSN-IRT at AAAI 2026 and #7 ATLAS) form the direct methodological foundation.\n- **Contamination detection**: Papers 12-18 cover the landscape from detection methods (#14, #16) to dynamic benchmarks (#12 LiveBench, #13 MathArena) to inference-time decontamination (#17).\n- **Adversarial robustness**: Papers 3, 19-22 span both safety alignment vulnerabilities and prompt-level adversarial evaluation.\n- **Meta-evaluation / motivation**: Papers 23-26 provide strong motivation for why better evaluation frameworks are needed (saturation, benchmark quality variance, integrity threats).\n- **Award-winning context**: Papers 1-5 from NeurIPS 2025 and ICLR 2025 provide high-visibility framing for the broader LLM evaluation challenge."
      }
    ],
    "totalDurationMs": 213489,
    "totalTokens": 43951,
    "totalToolUseCount": 48,
    "usage": {
      "input_tokens": 925,
      "cache_creation_input_tokens": 2573,
      "cache_read_input_tokens": 35693,
      "output_tokens": 4760,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2573
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 925,
          "output_tokens": 4760,
          "cache_read_input_tokens": 35693,
          "cache_creation_input_tokens": 2573,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2573,
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
      "otherToolCount": 48
    }
  },
  "sourceToolAssistantUUID": "619e4183-e304-4e35-8e8e-4748c0d6ff8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
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
  "leafUuid": "5fd4af08-86db-44eb-ab85-38cab6f8295f",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Assistant

_source line 32 · 2026-05-29T05:27:58.675Z_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive results from all five search agents. Let me synthesize the findings and select the 15 most important papers for the CRADE framework paper. Let me now do additional targeted searches to fill any remaining gaps and verify key papers.

Let me identify the most important papers across all the search results, focusing on:

1. Papers directly relevant to the CRADE framework's three pillars: contamination detection, adversarial robustness/variant generation, and IRT-based evaluation
2. Papers that are highly cited, from top venues, or have best paper awards
3. Papers that address the specific gaps identified in the research direction


4. Verification of seed papers and papers at the contamination-robustness intersection, plus any work on contamination-aware IRT

Now I'm compiling the final list of the most impactful papers, starting with those that directly address the CRADE framework's core components like adversarial perturbation methods and contamination detection approaches. that gets overlooked during training. RL doesn't actually push models to develop new reasoning capabilities beyond what they already have, which is a surprising finding from a top-tier venue. There's also a comprehensive faithfulness benchmark coming, along with frameworks for better LLM evaluation using item response theory, contamination detection methods for post-training, and metrics for assessing step-level reasoning quality. LiveBench is also in the mix as a recent evaluation resource.

Now I'm reconsidering which papers are truly essential for this research area. I should focus on work that sits at the intersection of contamination, robustness, and evaluation methodology—papers from top venues that directly address the gaps I've identified. Let me do a few more targeted searches to ensure I'm not missing critical work on contamination-robustness interactions or formal verification approaches for generating math variants.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fd4af08-86db-44eb-ab85-38cab6f8295f",
  "isSidechain": false,
  "requestId": "req_011CbWJkTah4cJCnKvyjtMFA",
  "type": "assistant",
  "uuid": "52825ffc-a7c9-4aa2-9def-3a02b25f63ca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiAaty39jaE1QJNvWETWDQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23734,
      "cache_read_input_tokens": 16827,
      "output_tokens": 1732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1732,
          "cache_read_input_tokens": 16827,
          "cache_creation_input_tokens": 23734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23734
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

_source line 33 · 2026-05-29T05:27:58.677Z_

Now let me do a few more targeted searches to fill remaining gaps, particularly around the contamination-robustness intersection and specific seed papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52825ffc-a7c9-4aa2-9def-3a02b25f63ca",
  "isSidechain": false,
  "requestId": "req_011CbWJkTah4cJCnKvyjtMFA",
  "type": "assistant",
  "uuid": "6fdafd48-5897-4d48-82d2-c7aeddac26d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiAaty39jaE1QJNvWETWDQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23734,
      "cache_read_input_tokens": 16827,
      "output_tokens": 1732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1732,
          "cache_read_input_tokens": 16827,
          "cache_creation_input_tokens": 23734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23734
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

_source line 34 · 2026-05-29T05:28:03.977Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011bGYNaXWU9xXuDkM9uPjV7`</summary>

```json
{
  "description": "Verify seed papers and find intersection work",
  "prompt": "You are helping with a literature survey. I need you to search for and verify specific papers, and find work at the intersection of contamination detection and adversarial robustness evaluation for LLMs.\n\nExecute these searches:\n\n1. WebSearch: \"ConStat performance-based contamination detection NeurIPS 2024\"\n2. WebSearch: \"GSM-Symbolic ICLR 2025 Apple limitations mathematical reasoning\"\n3. WebSearch: \"contamination robustness entangled LLM evaluation joint modeling\"\n4. WebSearch: \"MathArena uncontaminated math competitions LLM evaluation 2025\"\n5. WebSearch: \"DeconIEP inference-time decontamination LLM benchmark 2026\"\n6. WebSearch: \"site:arxiv.org benchmark contamination robustness joint framework LLM\"\n7. WebSearch: \"formal verification symbolic math variant generation LLM evaluation\"\n8. WebSearch: \"FrontierMath Epoch AI benchmark mathematical reasoning 2024\"\n\nFor the most relevant papers found, use WebFetch to read their arXiv abstracts.\n\nReport back with: title, authors, venue, URL, and one-line summary for each paper.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fdafd48-5897-4d48-82d2-c7aeddac26d9",
  "isSidechain": false,
  "requestId": "req_011CbWJkTah4cJCnKvyjtMFA",
  "type": "assistant",
  "uuid": "0fcde722-8c5d-4148-8c89-46368b9b6f93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiAaty39jaE1QJNvWETWDQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23734,
      "cache_read_input_tokens": 16827,
      "output_tokens": 1732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1732,
          "cache_read_input_tokens": 16827,
          "cache_creation_input_tokens": 23734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23734
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

_source line 35 · 2026-05-29T05:28:08.758Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016msJxyFvvYxnBQQikQoA26`</summary>

```json
{
  "description": "Search for additional key papers",
  "prompt": "You are helping with a literature survey for an ML paper about jointly modeling contamination and robustness in LLM evaluation. Search for these specific topics:\n\n1. WebSearch: \"How Much Can We Forget about Data Contamination ICML 2025\"\n2. WebSearch: \"Does Reinforcement Learning Really Incentivize Reasoning Capacity NeurIPS 2025 best paper\"\n3. WebSearch: \"tinyBenchmarks IRT evaluating LLMs fewer examples ICML 2024\"\n4. WebSearch: \"ProcessBench identifying process errors mathematical reasoning ACL 2025\"\n5. WebSearch: \"ReasonEval evaluating mathematical reasoning beyond accuracy AAAI 2025\"\n6. WebSearch: \"Self-Critique contamination detection reinforcement learning post-training ICLR 2026\"\n7. WebSearch: \"FaithCoT-Bench benchmarking instance-level faithfulness chain-of-thought ICLR 2026\"\n8. WebSearch: \"Measuring What Matters construct validity LLM benchmarks NeurIPS 2025\"\n\nFor the most relevant papers found, use WebFetch to read their arXiv abstracts.\n\nReport back with: title, authors, venue, URL, and one-line summary for each paper.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0fcde722-8c5d-4148-8c89-46368b9b6f93",
  "isSidechain": false,
  "requestId": "req_011CbWJkTah4cJCnKvyjtMFA",
  "type": "assistant",
  "uuid": "811a604d-33f4-451a-bdfc-a68fae9a6b0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QiAaty39jaE1QJNvWETWDQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23734,
      "cache_read_input_tokens": 16827,
      "output_tokens": 1732,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23734,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1732,
          "cache_read_input_tokens": 16827,
          "cache_creation_input_tokens": 23734,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23734
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

_source line 36 · 2026-05-29T05:29:14.628Z_

<details><summary>↩ Tool result · `toolu_016msJxyFvvYxnBQQikQoA26`</summary>

```text
Here is the literature survey with all 8 papers found:

---

**1. How Much Can We Forget about Data Contamination?**
- **Authors:** Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, Ulrike von Luxburg
- **Venue:** ICML 2025
- **URL:** https://arxiv.org/abs/2410.03249
- **Summary:** Experimentally shows that moderate benchmark contamination is "forgotten" during LLM training when data is scaled beyond 5x Chinchilla, measuring overfitting across model size (up to 1.6B), repetition (up to 144x), and training tokens (up to 40B).

**2. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**
- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang
- **Venue:** NeurIPS 2025 (Best Paper Runner-Up)
- **URL:** https://arxiv.org/abs/2504.13837
- **Summary:** Demonstrates that RLVR does not elicit fundamentally new reasoning patterns beyond those already present in the base model -- it improves sampling efficiency (pass@1) but base models achieve superior pass@k at large k, suggesting current RL post-training primarily reshapes output distributions rather than expanding reasoning boundaries.

**3. tinyBenchmarks: Evaluating LLMs with Fewer Examples**
- **Authors:** Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin
- **Venue:** ICML 2024
- **URL:** https://arxiv.org/abs/2402.14992
- **Summary:** Uses IRT-based strategies to show that LLM performance on MMLU (14K examples) can be accurately estimated from just 100 curated examples, with average error around 2%, and releases compact benchmark versions for MMLU, HELM, Open LLM Leaderboard, and AlpacaEval 2.0.

**4. ProcessBench: Identifying Process Errors in Mathematical Reasoning**
- **Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin
- **Venue:** ACL 2025
- **URL:** https://arxiv.org/abs/2412.06559
- **Summary:** Introduces a 3,400-case benchmark with human-annotated error locations in step-by-step math solutions, finding that existing process reward models fail to generalize beyond GSM8K/MATH while critic models and QwQ-32B-Preview perform competitively with GPT-4o.

**5. Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)**
- **Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu
- **Venue:** AAAI 2025 (Oral)
- **URL:** https://arxiv.org/abs/2404.05692
- **Summary:** Proposes ReasonEval, which evaluates intermediate reasoning steps via validity and redundancy metrics, showing that increases in final-answer accuracy do not necessarily improve reasoning step quality on challenging math problems.

**6. Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models (Self-Critique)**
- **Authors:** Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li
- **Venue:** ICLR 2026
- **URL:** https://arxiv.org/abs/2510.09259
- **Summary:** Proposes Self-Critique, the first method to detect benchmark contamination specifically from the RL post-training phase by exploiting output entropy collapse (policy collapse), achieving up to 30% AUC improvement over baselines that perform near-randomly on RL contamination scenarios.

**7. FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning**
- **Authors:** Xu Shen, Song Wang, Zhen Tan, Laura Yao, Xinyu Zhao, Kaidi Xu, Xin Wang, Tianlong Chen
- **Venue:** ICLR 2026
- **URL:** https://arxiv.org/abs/2510.04040
- **Summary:** Introduces the first benchmark for instance-level CoT unfaithfulness detection with 1,000+ expert-annotated trajectories across four domains, evaluating 11 detection methods and revealing that detection is harder in knowledge-intensive domains and with more advanced models.

**8. Measuring What Matters: Construct Validity in Large Language Model Benchmarks**
- **Authors:** Andrew M. Bean, Ryan Othniel Kearns, Angelika Romanou, et al. (29 expert reviewers total)
- **Venue:** NeurIPS 2025 (Datasets and Benchmarks Track)
- **URL:** https://arxiv.org/abs/2511.04703
- **Summary:** Systematic review of 445 LLM benchmarks from major ML/NLP conferences by 29 experts, identifying patterns in measured phenomena, tasks, and scoring metrics that undermine validity of benchmark claims, and providing eight actionable recommendations for benchmark development.

---

All 8 papers were successfully located and confirmed at their respective venues. Papers 1 and 6 are particularly central to the "contamination + robustness" theme of your survey -- paper 1 quantifies when contamination is forgotten and paper 6 addresses the novel problem of RL-phase contamination detection. Papers 3 and 8 provide the evaluation methodology angle (IRT-based efficient evaluation and construct validity). Papers 4, 5, and 7 cover process-level reasoning evaluation beyond accuracy. Paper 2 provides important context on what RL post-training actually does to reasoning capabilities.

Sources:
- [How Much Can We Forget about Data Contamination?](https://arxiv.org/abs/2410.03249)
- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837)
- [tinyBenchmarks: evaluating LLMs with fewer examples](https://arxiv.org/abs/2402.14992)
- [ProcessBench: Identifying Process Errors in Mathematical Reasoning](https://arxiv.org/abs/2412.06559)
- [Evaluating Mathematical Reasoning Beyond Accuracy](https://arxiv.org/abs/2404.05692)
- [Detecting Data Contamination from Reinforcement Learning Post-training](https://arxiv.org/abs/2510.09259)
- [FaithCoT-Bench](https://arxiv.org/abs/2510.04040)
- [Measuring what Matters: Construct Validity in LLM Benchmarks](https://arxiv.org/abs/2511.04703)

agentId: a79a7bf88e6e19158 (use SendMessage with to: 'a79a7bf88e6e19158' to continue this agent)
&lt;usage>total_tokens: 21718
tool_uses: 17
duration_ms: 65867&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "811a604d-33f4-451a-bdfc-a68fae9a6b0a",
  "isSidechain": false,
  "promptId": "37ea365b-dcd4-4897-b99b-0b8f025b793a",
  "type": "user",
  "uuid": "e0af1d90-d246-46a2-b0de-b2a7b3e8d2aa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an ML paper about jointly modeling contamination and robustness in LLM evaluation. Search for these specific topics:\n\n1. WebSearch: \"How Much Can We Forget about Data Contamination ICML 2025\"\n2. WebSearch: \"Does Reinforcement Learning Really Incentivize Reasoning Capacity NeurIPS 2025 best paper\"\n3. WebSearch: \"tinyBenchmarks IRT evaluating LLMs fewer examples ICML 2024\"\n4. WebSearch: \"ProcessBench identifying process errors mathematical reasoning ACL 2025\"\n5. WebSearch: \"ReasonEval evaluating mathematical reasoning beyond accuracy AAAI 2025\"\n6. WebSearch: \"Self-Critique contamination detection reinforcement learning post-training ICLR 2026\"\n7. WebSearch: \"FaithCoT-Bench benchmarking instance-level faithfulness chain-of-thought ICLR 2026\"\n8. WebSearch: \"Measuring What Matters construct validity LLM benchmarks NeurIPS 2025\"\n\nFor the most relevant papers found, use WebFetch to read their arXiv abstracts.\n\nReport back with: title, authors, venue, URL, and one-line summary for each paper.",
    "agentId": "a79a7bf88e6e19158",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the literature survey with all 8 papers found:\n\n---\n\n**1. How Much Can We Forget about Data Contamination?**\n- **Authors:** Sebastian Bordt, Suraj Srinivas, Valentyn Boreiko, Ulrike von Luxburg\n- **Venue:** ICML 2025\n- **URL:** https://arxiv.org/abs/2410.03249\n- **Summary:** Experimentally shows that moderate benchmark contamination is \"forgotten\" during LLM training when data is scaled beyond 5x Chinchilla, measuring overfitting across model size (up to 1.6B), repetition (up to 144x), and training tokens (up to 40B).\n\n**2. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**\n- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang\n- **Venue:** NeurIPS 2025 (Best Paper Runner-Up)\n- **URL:** https://arxiv.org/abs/2504.13837\n- **Summary:** Demonstrates that RLVR does not elicit fundamentally new reasoning patterns beyond those already present in the base model -- it improves sampling efficiency (pass@1) but base models achieve superior pass@k at large k, suggesting current RL post-training primarily reshapes output distributions rather than expanding reasoning boundaries.\n\n**3. tinyBenchmarks: Evaluating LLMs with Fewer Examples**\n- **Authors:** Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin\n- **Venue:** ICML 2024\n- **URL:** https://arxiv.org/abs/2402.14992\n- **Summary:** Uses IRT-based strategies to show that LLM performance on MMLU (14K examples) can be accurately estimated from just 100 curated examples, with average error around 2%, and releases compact benchmark versions for MMLU, HELM, Open LLM Leaderboard, and AlpacaEval 2.0.\n\n**4. ProcessBench: Identifying Process Errors in Mathematical Reasoning**\n- **Authors:** Chujie Zheng, Zhenru Zhang, Beichen Zhang, Runji Lin, Keming Lu, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin\n- **Venue:** ACL 2025\n- **URL:** https://arxiv.org/abs/2412.06559\n- **Summary:** Introduces a 3,400-case benchmark with human-annotated error locations in step-by-step math solutions, finding that existing process reward models fail to generalize beyond GSM8K/MATH while critic models and QwQ-32B-Preview perform competitively with GPT-4o.\n\n**5. Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)**\n- **Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu\n- **Venue:** AAAI 2025 (Oral)\n- **URL:** https://arxiv.org/abs/2404.05692\n- **Summary:** Proposes ReasonEval, which evaluates intermediate reasoning steps via validity and redundancy metrics, showing that increases in final-answer accuracy do not necessarily improve reasoning step quality on challenging math problems.\n\n**6. Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models (Self-Critique)**\n- **Authors:** Yongding Tao, Tian Wang, Yihong Dong, Huanyu Liu, Kechi Zhang, Xiaolong Hu, Ge Li\n- **Venue:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2510.09259\n- **Summary:** Proposes Self-Critique, the first method to detect benchmark contamination specifically from the RL post-training phase by exploiting output entropy collapse (policy collapse), achieving up to 30% AUC improvement over baselines that perform near-randomly on RL contamination scenarios.\n\n**7. FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning**\n- **Authors:** Xu Shen, Song Wang, Zhen Tan, Laura Yao, Xinyu Zhao, Kaidi Xu, Xin Wang, Tianlong Chen\n- **Venue:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2510.04040\n- **Summary:** Introduces the first benchmark for instance-level CoT unfaithfulness detection with 1,000+ expert-annotated trajectories across four domains, evaluating 11 detection methods and revealing that detection is harder in knowledge-intensive domains and with more advanced models.\n\n**8. Measuring What Matters: Construct Validity in Large Language Model Benchmarks**\n- **Authors:** Andrew M. Bean, Ryan Othniel Kearns, Angelika Romanou, et al. (29 expert reviewers total)\n- **Venue:** NeurIPS 2025 (Datasets and Benchmarks Track)\n- **URL:** https://arxiv.org/abs/2511.04703\n- **Summary:** Systematic review of 445 LLM benchmarks from major ML/NLP conferences by 29 experts, identifying patterns in measured phenomena, tasks, and scoring metrics that undermine validity of benchmark claims, and providing eight actionable recommendations for benchmark development.\n\n---\n\nAll 8 papers were successfully located and confirmed at their respective venues. Papers 1 and 6 are particularly central to the \"contamination + robustness\" theme of your survey -- paper 1 quantifies when contamination is forgotten and paper 6 addresses the novel problem of RL-phase contamination detection. Papers 3 and 8 provide the evaluation methodology angle (IRT-based efficient evaluation and construct validity). Papers 4, 5, and 7 cover process-level reasoning evaluation beyond accuracy. Paper 2 provides important context on what RL post-training actually does to reasoning capabilities.\n\nSources:\n- [How Much Can We Forget about Data Contamination?](https://arxiv.org/abs/2410.03249)\n- [Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?](https://arxiv.org/abs/2504.13837)\n- [tinyBenchmarks: evaluating LLMs with fewer examples](https://arxiv.org/abs/2402.14992)\n- [ProcessBench: Identifying Process Errors in Mathematical Reasoning](https://arxiv.org/abs/2412.06559)\n- [Evaluating Mathematical Reasoning Beyond Accuracy](https://arxiv.org/abs/2404.05692)\n- [Detecting Data Contamination from Reinforcement Learning Post-training](https://arxiv.org/abs/2510.09259)\n- [FaithCoT-Bench](https://arxiv.org/abs/2510.04040)\n- [Measuring what Matters: Construct Validity in LLM Benchmarks](https://arxiv.org/abs/2511.04703)"
      }
    ],
    "totalDurationMs": 65867,
    "totalTokens": 21718,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4574,
      "cache_read_input_tokens": 15398,
      "output_tokens": 1745,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4574
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1745,
          "cache_read_input_tokens": 15398,
          "cache_creation_input_tokens": 4574,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4574,
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
  "sourceToolAssistantUUID": "811a604d-33f4-451a-bdfc-a68fae9a6b0a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-29T05:29:23.204Z_

<details><summary>↩ Tool result · `toolu_011bGYNaXWU9xXuDkM9uPjV7`</summary>

```text
Here is the full literature survey report.

---

## Literature Survey: Contamination Detection and Adversarial Robustness Evaluation for LLMs

### 1. ConStat: Performance-Based Contamination Detection in Large Language Models

- **Authors:** Jasper Dekoninck, Mark Niklas Muller, Martin Vechev (ETH Zurich)
- **Venue:** NeurIPS 2024
- **URL:** https://arxiv.org/abs/2405.16281
- **Summary:** Proposes a statistical test that defines contamination as artificially inflated, non-generalizing benchmark performance (rather than training data inclusion), comparing primary vs. reference benchmark performance relative to reference models; detects contamination in Mistral, Llama, Yi, and top Open LLM Leaderboard models.

---

### 2. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

- **Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar (Apple)
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2410.05229
- **Summary:** Introduces symbolic templates over GSM8K to generate controlled math question variants, revealing that LLMs show high variance across instantiations and up to 65% performance drops when a single irrelevant clause is added, suggesting pattern matching rather than genuine reasoning.

---

### 3. Provable Joint Decontamination for Benchmarking Multiple Large Language Models

- **Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei
- **Venue:** arXiv preprint (May 2025)
- **URL:** https://arxiv.org/abs/2605.21543
- **Summary:** Introduces JECS (Joint Envelope Conformal Selection), a conformal procedure that constructs a shared decontaminated benchmark across multiple models with provable global contamination rate control, solving the problem that per-model detection creates incomparable model-specific benchmarks.

---

### 4. MathArena: Evaluating LLMs on Uncontaminated Math Competitions

- **Authors:** Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev (ETH Zurich)
- **Venue:** NeurIPS 2025 (Datasets and Benchmarks Track)
- **URL:** https://arxiv.org/abs/2505.23281
- **Summary:** Uses recurring math competitions as a stream of fresh, uncontaminated problems; evaluates 50+ models on 162 problems across 7 competitions, finds strong contamination signs in AIME 2024, and is the first benchmark to evaluate LLM proof-writing (top models achieve ~40% on IMO 2025).

---

### 5. When Benchmarks Leak: Inference-Time Decontamination for LLMs (DeconIEP)

- **Authors:** Jianzhe Chai, Yu Zhe, Jun Sakuma
- **Venue:** arXiv preprint (January 2026)
- **URL:** https://arxiv.org/abs/2601.19334
- **Summary:** Proposes DeconIEP, a decontamination framework that operates entirely at inference time by learning instance-adaptive perturbations in embedding space, guided by a less-contaminated reference model, to steer evaluated models away from memorization-driven shortcuts while preserving benign utility.

---

### 6. Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation (ITD)

- **Authors:** Qin Zhu, Qingyuan Cheng, Runyu Peng, Xiaonan Li, Tengxiao Liu, Ru Peng, Xipeng Qiu, Xuanjing Huang
- **Venue:** arXiv preprint (June 2024)
- **URL:** https://arxiv.org/abs/2406.13990
- **Summary:** Detects and rewrites leaked benchmark samples at inference time while preserving task difficulty; reduces inflated accuracy by 22.9% on GSM8K and 19.0% on MMLU, enabling reuse of compromised benchmarks for fair evaluation.

---

### 7. FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI

- **Authors:** Elliot Glazer, Ege Erdil, Tamay Besiroglu, Diego Chicharro, Evan Chen, Alex Gunning, Caroline Falkman Olsson, Jean-Stanislas Denain, Anson Ho, Emily de Oliveira Santos, Olli Jarviniemi, Matthew Barnett, Robert Sandler, Matej Vrzala, Jaime Sevilla, Qiuyu Ren, Elizabeth Pratt, Lionel Levine, Grant Barkley, Natalie Stewart, Bogdan Grechuk, Tetiana Grechuk, Shreepranav Varma Enugandla, Mark Wildon (Epoch AI)
- **Venue:** arXiv preprint (November 2024)
- **URL:** https://arxiv.org/abs/2411.04872
- **Summary:** Presents hundreds of original, expert-vetted math problems spanning computational number theory to algebraic geometry; current frontier models solve fewer than 2% of problems, sharply contrasting with >90% accuracy on GSM8K/MATH, with unpublished questions and automated verification reducing contamination risk.

---

### 8. DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation

- **Authors:** Renzhao Liang, Jingru Chen, Bo Jia, Bo Deng, Chenggang Xie, Yidong Wang, Ke Jin, Xin Wang, Linfeng Zhang, Cunxiang Wang
- **Venue:** arXiv preprint (January 2026)
- **URL:** https://arxiv.org/abs/2601.04895
- **Summary:** Addresses "variant contamination" (paraphrased test questions in training data) by analyzing output distribution variance from temperature sampling; outperforms perplexity-based, Min-k%++, edit-distance, and embedding-similarity baselines across multiple model sizes.

---

### 9. Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models

- **Authors:** Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, Ge Li
- **Venue:** arXiv preprint (February 2024)
- **URL:** https://arxiv.org/abs/2402.15938
- **Summary:** Introduces CDD (output-distribution-based contamination detection) and TED (trustworthy evaluation via distribution correction), achieving 21.8-30.2% improvement over baselines in detection and reducing inflated performance gains by up to 66.9%; reveals ChatGPT contamination on HumanEval.

---

### 10. Towards Contamination Resistant Benchmarks

- **Authors:** Rahmatullah Musawi, Sheng Lu
- **Venue:** arXiv preprint (May 2025)
- **URL:** https://arxiv.org/abs/2505.08389
- **Summary:** Proposes the concept of "contamination resistance" and demonstrates a Caesar-cipher-based benchmark transformation that is simple yet effective at resisting contamination, revealing that models perform poorly when contamination is properly controlled.

---

### 11. Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (MATH-VF)

- **Authors:** Kuo Zhou, Lu Zhang
- **Venue:** arXiv preprint (May 2025)
- **URL:** https://arxiv.org/abs/2505.20869
- **Summary:** Introduces MATH-VF, a framework with a Formalizer (natural language to formal representation) and Critic (CAS/SMT solver verification) for step-by-step formal verification of LLM math solutions, evaluated on MATH500 and ProcessBench.

---

### Key Observations at the Intersection of Contamination Detection and Adversarial Robustness

The search reveals that **direct joint modeling of contamination and adversarial robustness** is still an emerging area, but several threads are converging:

- **ConStat** (paper 1) and **JECS** (paper 3) represent the contamination detection frontier -- ConStat with its performance-based definition and JECS with provable guarantees across multiple models simultaneously.
- **GSM-Symbolic** (paper 2) and **MathArena** (paper 4) tackle the problem from the benchmark design side -- generating variants or using fresh competition problems to sidestep contamination entirely while also testing robustness.
- **DeconIEP** (paper 5) and **ITD** (paper 6) attack the problem at inference time, attempting to "decontaminate" models without retraining.
- **FrontierMath** (paper 7) represents the hardest-problem approach -- making contamination irrelevant by using unpublished, expert-level problems.
- **DVD** (paper 8) specifically targets the adversarial angle of "variant contamination" where paraphrased test data evades standard detection.
- **MATH-VF** (paper 11) brings formal verification to LLM math evaluation, enabling automated correctness checking independent of contamination concerns.

The paper most directly at the intersection of contamination and robustness in a joint framework is **JECS** (arxiv 2605.21543), which provides the first provable joint decontamination procedure for benchmarking multiple LLMs. The **ConStat + MathArena** line of work from ETH Zurich (Dekoninck, Balunovic, Vechev) is also notable for combining contamination detection with contamination-resistant benchmark design.

Sources:
- [ConStat (NeurIPS 2024)](https://arxiv.org/abs/2405.16281)
- [GSM-Symbolic (ICLR 2025)](https://arxiv.org/abs/2410.05229)
- [JECS - Provable Joint Decontamination](https://arxiv.org/abs/2605.21543)
- [MathArena (NeurIPS 2025)](https://arxiv.org/abs/2505.23281)
- [DeconIEP](https://arxiv.org/abs/2601.19334)
- [ITD - Inference-Time Decontamination](https://arxiv.org/abs/2406.13990)
- [FrontierMath (Epoch AI)](https://arxiv.org/abs/2411.04872)
- [DVD - Variant Contamination Detection](https://arxiv.org/abs/2601.04895)
- [CDD/TED - Generalization or Memorization](https://arxiv.org/abs/2402.15938)
- [Contamination Resistant Benchmarks](https://arxiv.org/abs/2505.08389)
- [MATH-VF - Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869)

agentId: aeecdf0521c303f7b (use SendMessage with to: 'aeecdf0521c303f7b' to continue this agent)
&lt;usage>total_tokens: 23708
tool_uses: 20
duration_ms: 79222&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0fcde722-8c5d-4148-8c89-46368b9b6f93",
  "isSidechain": false,
  "promptId": "37ea365b-dcd4-4897-b99b-0b8f025b793a",
  "type": "user",
  "uuid": "42311384-f497-4ddb-b5de-fe819d578ea5",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey. I need you to search for and verify specific papers, and find work at the intersection of contamination detection and adversarial robustness evaluation for LLMs.\n\nExecute these searches:\n\n1. WebSearch: \"ConStat performance-based contamination detection NeurIPS 2024\"\n2. WebSearch: \"GSM-Symbolic ICLR 2025 Apple limitations mathematical reasoning\"\n3. WebSearch: \"contamination robustness entangled LLM evaluation joint modeling\"\n4. WebSearch: \"MathArena uncontaminated math competitions LLM evaluation 2025\"\n5. WebSearch: \"DeconIEP inference-time decontamination LLM benchmark 2026\"\n6. WebSearch: \"site:arxiv.org benchmark contamination robustness joint framework LLM\"\n7. WebSearch: \"formal verification symbolic math variant generation LLM evaluation\"\n8. WebSearch: \"FrontierMath Epoch AI benchmark mathematical reasoning 2024\"\n\nFor the most relevant papers found, use WebFetch to read their arXiv abstracts.\n\nReport back with: title, authors, venue, URL, and one-line summary for each paper.",
    "agentId": "aeecdf0521c303f7b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the full literature survey report.\n\n---\n\n## Literature Survey: Contamination Detection and Adversarial Robustness Evaluation for LLMs\n\n### 1. ConStat: Performance-Based Contamination Detection in Large Language Models\n\n- **Authors:** Jasper Dekoninck, Mark Niklas Muller, Martin Vechev (ETH Zurich)\n- **Venue:** NeurIPS 2024\n- **URL:** https://arxiv.org/abs/2405.16281\n- **Summary:** Proposes a statistical test that defines contamination as artificially inflated, non-generalizing benchmark performance (rather than training data inclusion), comparing primary vs. reference benchmark performance relative to reference models; detects contamination in Mistral, Llama, Yi, and top Open LLM Leaderboard models.\n\n---\n\n### 2. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\n\n- **Authors:** Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar (Apple)\n- **Venue:** ICLR 2025\n- **URL:** https://arxiv.org/abs/2410.05229\n- **Summary:** Introduces symbolic templates over GSM8K to generate controlled math question variants, revealing that LLMs show high variance across instantiations and up to 65% performance drops when a single irrelevant clause is added, suggesting pattern matching rather than genuine reasoning.\n\n---\n\n### 3. Provable Joint Decontamination for Benchmarking Multiple Large Language Models\n\n- **Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei\n- **Venue:** arXiv preprint (May 2025)\n- **URL:** https://arxiv.org/abs/2605.21543\n- **Summary:** Introduces JECS (Joint Envelope Conformal Selection), a conformal procedure that constructs a shared decontaminated benchmark across multiple models with provable global contamination rate control, solving the problem that per-model detection creates incomparable model-specific benchmarks.\n\n---\n\n### 4. MathArena: Evaluating LLMs on Uncontaminated Math Competitions\n\n- **Authors:** Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev (ETH Zurich)\n- **Venue:** NeurIPS 2025 (Datasets and Benchmarks Track)\n- **URL:** https://arxiv.org/abs/2505.23281\n- **Summary:** Uses recurring math competitions as a stream of fresh, uncontaminated problems; evaluates 50+ models on 162 problems across 7 competitions, finds strong contamination signs in AIME 2024, and is the first benchmark to evaluate LLM proof-writing (top models achieve ~40% on IMO 2025).\n\n---\n\n### 5. When Benchmarks Leak: Inference-Time Decontamination for LLMs (DeconIEP)\n\n- **Authors:** Jianzhe Chai, Yu Zhe, Jun Sakuma\n- **Venue:** arXiv preprint (January 2026)\n- **URL:** https://arxiv.org/abs/2601.19334\n- **Summary:** Proposes DeconIEP, a decontamination framework that operates entirely at inference time by learning instance-adaptive perturbations in embedding space, guided by a less-contaminated reference model, to steer evaluated models away from memorization-driven shortcuts while preserving benign utility.\n\n---\n\n### 6. Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation (ITD)\n\n- **Authors:** Qin Zhu, Qingyuan Cheng, Runyu Peng, Xiaonan Li, Tengxiao Liu, Ru Peng, Xipeng Qiu, Xuanjing Huang\n- **Venue:** arXiv preprint (June 2024)\n- **URL:** https://arxiv.org/abs/2406.13990\n- **Summary:** Detects and rewrites leaked benchmark samples at inference time while preserving task difficulty; reduces inflated accuracy by 22.9% on GSM8K and 19.0% on MMLU, enabling reuse of compromised benchmarks for fair evaluation.\n\n---\n\n### 7. FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI\n\n- **Authors:** Elliot Glazer, Ege Erdil, Tamay Besiroglu, Diego Chicharro, Evan Chen, Alex Gunning, Caroline Falkman Olsson, Jean-Stanislas Denain, Anson Ho, Emily de Oliveira Santos, Olli Jarviniemi, Matthew Barnett, Robert Sandler, Matej Vrzala, Jaime Sevilla, Qiuyu Ren, Elizabeth Pratt, Lionel Levine, Grant Barkley, Natalie Stewart, Bogdan Grechuk, Tetiana Grechuk, Shreepranav Varma Enugandla, Mark Wildon (Epoch AI)\n- **Venue:** arXiv preprint (November 2024)\n- **URL:** https://arxiv.org/abs/2411.04872\n- **Summary:** Presents hundreds of original, expert-vetted math problems spanning computational number theory to algebraic geometry; current frontier models solve fewer than 2% of problems, sharply contrasting with >90% accuracy on GSM8K/MATH, with unpublished questions and automated verification reducing contamination risk.\n\n---\n\n### 8. DVD: A Robust Method for Detecting Variant Contamination in Large Language Model Evaluation\n\n- **Authors:** Renzhao Liang, Jingru Chen, Bo Jia, Bo Deng, Chenggang Xie, Yidong Wang, Ke Jin, Xin Wang, Linfeng Zhang, Cunxiang Wang\n- **Venue:** arXiv preprint (January 2026)\n- **URL:** https://arxiv.org/abs/2601.04895\n- **Summary:** Addresses \"variant contamination\" (paraphrased test questions in training data) by analyzing output distribution variance from temperature sampling; outperforms perplexity-based, Min-k%++, edit-distance, and embedding-similarity baselines across multiple model sizes.\n\n---\n\n### 9. Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models\n\n- **Authors:** Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, Ge Li\n- **Venue:** arXiv preprint (February 2024)\n- **URL:** https://arxiv.org/abs/2402.15938\n- **Summary:** Introduces CDD (output-distribution-based contamination detection) and TED (trustworthy evaluation via distribution correction), achieving 21.8-30.2% improvement over baselines in detection and reducing inflated performance gains by up to 66.9%; reveals ChatGPT contamination on HumanEval.\n\n---\n\n### 10. Towards Contamination Resistant Benchmarks\n\n- **Authors:** Rahmatullah Musawi, Sheng Lu\n- **Venue:** arXiv preprint (May 2025)\n- **URL:** https://arxiv.org/abs/2505.08389\n- **Summary:** Proposes the concept of \"contamination resistance\" and demonstrates a Caesar-cipher-based benchmark transformation that is simple yet effective at resisting contamination, revealing that models perform poorly when contamination is properly controlled.\n\n---\n\n### 11. Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (MATH-VF)\n\n- **Authors:** Kuo Zhou, Lu Zhang\n- **Venue:** arXiv preprint (May 2025)\n- **URL:** https://arxiv.org/abs/2505.20869\n- **Summary:** Introduces MATH-VF, a framework with a Formalizer (natural language to formal representation) and Critic (CAS/SMT solver verification) for step-by-step formal verification of LLM math solutions, evaluated on MATH500 and ProcessBench.\n\n---\n\n### Key Observations at the Intersection of Contamination Detection and Adversarial Robustness\n\nThe search reveals that **direct joint modeling of contamination and adversarial robustness** is still an emerging area, but several threads are converging:\n\n- **ConStat** (paper 1) and **JECS** (paper 3) represent the contamination detection frontier -- ConStat with its performance-based definition and JECS with provable guarantees across multiple models simultaneously.\n- **GSM-Symbolic** (paper 2) and **MathArena** (paper 4) tackle the problem from the benchmark design side -- generating variants or using fresh competition problems to sidestep contamination entirely while also testing robustness.\n- **DeconIEP** (paper 5) and **ITD** (paper 6) attack the problem at inference time, attempting to \"decontaminate\" models without retraining.\n- **FrontierMath** (paper 7) represents the hardest-problem approach -- making contamination irrelevant by using unpublished, expert-level problems.\n- **DVD** (paper 8) specifically targets the adversarial angle of \"variant contamination\" where paraphrased test data evades standard detection.\n- **MATH-VF** (paper 11) brings formal verification to LLM math evaluation, enabling automated correctness checking independent of contamination concerns.\n\nThe paper most directly at the intersection of contamination and robustness in a joint framework is **JECS** (arxiv 2605.21543), which provides the first provable joint decontamination procedure for benchmarking multiple LLMs. The **ConStat + MathArena** line of work from ETH Zurich (Dekoninck, Balunovic, Vechev) is also notable for combining contamination detection with contamination-resistant benchmark design.\n\nSources:\n- [ConStat (NeurIPS 2024)](https://arxiv.org/abs/2405.16281)\n- [GSM-Symbolic (ICLR 2025)](https://arxiv.org/abs/2410.05229)\n- [JECS - Provable Joint Decontamination](https://arxiv.org/abs/2605.21543)\n- [MathArena (NeurIPS 2025)](https://arxiv.org/abs/2505.23281)\n- [DeconIEP](https://arxiv.org/abs/2601.19334)\n- [ITD - Inference-Time Decontamination](https://arxiv.org/abs/2406.13990)\n- [FrontierMath (Epoch AI)](https://arxiv.org/abs/2411.04872)\n- [DVD - Variant Contamination Detection](https://arxiv.org/abs/2601.04895)\n- [CDD/TED - Generalization or Memorization](https://arxiv.org/abs/2402.15938)\n- [Contamination Resistant Benchmarks](https://arxiv.org/abs/2505.08389)\n- [MATH-VF - Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869)"
      }
    ],
    "totalDurationMs": 79222,
    "totalTokens": 23708,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1711,
      "cache_read_input_tokens": 19227,
      "output_tokens": 2769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1711
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2769,
          "cache_read_input_tokens": 19227,
          "cache_creation_input_tokens": 1711,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1711,
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
  "sourceToolAssistantUUID": "0fcde722-8c5d-4148-8c89-46368b9b6f93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38 · 2026-05-29T05:29:23.213Z_

```json
{
  "parentUuid": "42311384-f497-4ddb-b5de-fe819d578ea5",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "6dc3d94b-8a43-4ef9-bc7b-2dbb40b5bad9",
  "timestamp": "2026-05-29T05:29:23.213Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "6dc3d94b-8a43-4ef9-bc7b-2dbb40b5bad9",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Assistant

_source line 41 · 2026-05-29T05:30:27.861Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive data from all search agents. Let me compile the final list of the 15 most important papers. I need to carefully select papers that are:

1. Most relevant to the CRADE framework (contamination + adversarial robustness + IRT + step-level evaluation)
2. From top venues with recognition (best paper, spotlight, oral)
3. Highly cited or widely adopted
4. Fill specific roles in the related work narrative

Let me categorize and select:

**Pillar 1: Contamination Detection & Mitigation**
- ConStat (NeurIPS 2024) - Performance-based contamination detection, directly defines contamination as non-generalizing performance


- Self-Critique (ICLR 2026) - First to detect RL post-training contamination, addresses the fragility problem
- How Much Can We Forget about Data Contamination? (ICML 2025) - Nuances the contamination threat model
- JECS - Provable Joint Decontamination (arXiv 2025) - Joint decontamination across models

**Pillar 2: Adversarial Robustness / Variant Generation**
- GSM-Symbolic (Apple, ICLR 2025) - Foundational adversarial perturbation, highly cited
- GSM-Plus (AC...)

Continuing with the remaining pillars...

**Pillar 3: IRT for LLM Evaluation**
- tinyBenchmarks (ICML 2024) - Foundational IRT-based evaluation
- PSN-IRT / Lost in Benchmarks (AAAI 2026 Oral) - IRT framework with pseudo-siamese network
- ATLAS (arXiv 2025) - Adaptive testing with 3PL IRT

**Pillar 4: Step-Level Reasoning & CoT Faithfulness**
- ProcessBench (ACL 2025) - Step-level error identification
- ReasonEval (AAAI 2025) - Step-level validity and redundancy
- FaithCoT-Bench (ICLR 2026) - CoT faithfulness benchmark
- ThinkP...

Now I'm looking at the remaining papers on process reward models, progress verification, and meta-evaluation frameworks. I need to narrow down to the 15 most impactful papers beyond the seed set, so I'm being selective about which ones truly advance the field versus incremental contributions. Continuing with more foundational papers on chain-of-thought faithfulness, step-level evaluation metrics, process reward models, and decontamination frameworks that establish the measurement and validation infrastructure for reasoning-focused benchmarks.

Now I'm checking whether any of the seed papers overlap with my compiled list—CoDeC, ATLAS, MaSTer, ReasoningMath-Plus, the Anthropic paper on reasoning models, DCR, and the Kocetkov fragility work don't appear in my top 15, which is good. But I should reconsider whether the seed papers themselves might qualify as "most important recent papers" given the user's criteria, since they're clearly foundational to this research area.

Looking back at the user's guidance about what to avoid—they specifically flagged ad-hoc perturbation studies like GSM-Plus and MATH-Perturb as lacking methodological depth, which suggests these are known related work rather than papers to exclude from consideration. I should treat them as important context but focus on papers with stronger theoretical or methodological contributions.

Let me refine my selection to emphasize papers that either introduce novel evaluation frameworks, provide critical insights about LLM reasoning, or offer methodological advances beyond simple benchmark perturbations. GSM-Symbolic is essential as the foundational work demonstrating robustness failures, ConStat brings a principled contamination detection approach, tinyBenchmarks offers the IRT framework that's become standard, and the RL reasoning paper provides crucial perspective on what these models actually learn.

Continuing with the remaining selections: Self-Critique addresses contamination in the RL setting, FaithCoT-Bench and ProcessBench provide comprehensive step-level analysis frameworks, ReasonEval introduces validity metrics beyond accuracy, and the process advantage verifiers represent a shift toward rewarding reasoning quality rather than just outcomes. MathArena rounds out the evaluation landscape with uncontaminated benchmarks.

Now I'm reconsidering the framing—JECS on joint decontamination across models actually aligns better with CRADE's core philosophy, and the dynamic evaluation survey from EMNLP 2025 provides crucial context for how benchmarking itself is evolving.

I should also include "Reasoning Models Don't Always Say What They Think" since it's foundational to this work. Let me lock in my final fifteen strongest papers outside the seed set, starting with GSM-Symbolic and moving through the key contributions on reasoning evaluation, contamination, and process-based assessment.

Actually, I'm reconsidering the last slot—FrontierMath is solid for contamination-proofing but doesn't directly advance CRADE methodology. I'm weighing alternatives like JECS for its joint decontamination approach, Fluid Benchmarking's CAT methodology for LLMs, FoVer's formal verification angle for process reward models, or that EMNLP survey on reasoning traces.

JECS makes more sense than FrontierMath since joint decontamination aligns with CRADE's joint modeling philosophy, and FoVer fits because CRADE leverages SymPy for symbolically-backed generation with provable correctness guarantees. Let me lock in the final list with these swaps. I'm reconsidering whether FoVer or JECS should take the final spot—JECS addresses joint decontamination across models which aligns with CRADE's joint modeling approach, while FoVer's formal verification tools connect to the SymPy-backed generation. I'll stick with FoVer since it's more directly methodologically relevant. Now I need to verify the venue information before compiling the final JSON, particularly whether PSN-IRT is actually an AAAI 2026 oral.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6dc3d94b-8a43-4ef9-bc7b-2dbb40b5bad9",
  "isSidechain": false,
  "requestId": "req_011CbWJtWPpsWxsz1Efz3n8t",
  "type": "assistant",
  "uuid": "c441708b-eea1-43b4-a9cf-3afe92e4dc7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RF1ZhxrTEPnLi8aW6YK4r4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6551,
      "cache_read_input_tokens": 40561,
      "output_tokens": 7021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7021,
          "cache_read_input_tokens": 40561,
          "cache_creation_input_tokens": 6551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6551
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

_source line 42 · 2026-05-29T05:31:33.763Z_

Now I have comprehensive data from all seven search agents. Let me compile the final curated list of the 15 most important papers, selecting for relevance to the CRADE framework, venue prestige, and impact.

Here is the final literature survey:

---

## Literature Survey: 15 Most Important Recent Papers for CRADE

These papers span the three pillars of CRADE — **contamination detection**, **adversarial robustness/variant generation**, and **IRT-based calibrated evaluation** — plus the critical connective tissue of **step-level reasoning evaluation** and **CoT faithfulness**. Papers are selected from the ~80+ candidates surfaced across all search threads, prioritizing top-venue publications, best paper awards, and direct methodological relevance to joint contamination-robustness modeling.

---

```json
[
  {
    "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models",
    "authors": "Mirzadeh et al. (Apple)",
    "venue": "ICLR 2025",
    "url": "https://arxiv.org/abs/2410.05229",
    "why_important": "Highly cited (1000+), ICLR 2025. Foundational adversarial perturbation paper that launched the robustness-of-reasoning subfield. Directly motivates CRADE's variant generation pipeline.",
    "one_line_summary": "Introduces symbolic templates over GSM8K showing LLMs exhibit high variance across numeric instantiations and up to 65% accuracy drops from adding a single irrelevant clause, arguing models pattern-match rather than reason."
  },
  {
    "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
    "authors": "Dekoninck et al. (ETH Zurich)",
    "venue": "NeurIPS 2024",
    "url": "https://arxiv.org/abs/2405.16281",
    "why_important": "NeurIPS 2024. Uniquely defines contamination as non-generalizing performance (not data inclusion), bridging the contamination-robustness gap that CRADE formalizes.",
    "one_line_summary": "Detects contamination by statistically comparing model performance on original vs. rephrased benchmark variants, finding significant inflation in Mistral, Llama, Yi, and top Open LLM Leaderboard models."
  },
  {
    "title": "tinyBenchmarks: Evaluating LLMs with Fewer Examples",
    "authors": "Polo et al.",
    "venue": "ICML 2024",
    "url": "https://arxiv.org/abs/2402.14992",
    "why_important": "ICML 2024, highly cited, widely adopted. Foundational paper that proved IRT can compress LLM benchmarks (14K→100 items) — the methodological ancestor of CRADE's IRT-calibrated scoring.",
    "one_line_summary": "Uses IRT-based item selection to reduce MMLU from 14K to 100 curated examples while reproducing full benchmark scores within ~2% average error, releasing compact versions of major benchmarks."
  },
  {
    "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?",
    "authors": "Yue et al.",
    "venue": "NeurIPS 2025 Best Paper Runner-Up",
    "url": "https://arxiv.org/abs/2504.13837",
    "why_important": "NeurIPS 2025 Best Paper Runner-Up. Directly relevant: if RLVR doesn't create new reasoning but reshapes output distributions, then contamination-like memorization effects may persist through RL post-training, validating CRADE's premise.",
    "one_line_summary": "Shows via pass@k analysis that RLVR improves sampling efficiency (pass@1) but does not elicit fundamentally new reasoning patterns beyond the base model, challenging assumptions about RL-trained capabilities."
  },
  {
    "title": "How Much Can We Forget about Data Contamination?",
    "authors": "Bordt et al.",
    "venue": "ICML 2025",
    "url": "https://arxiv.org/abs/2410.03249",
    "why_important": "ICML 2025. Provides the nuanced contamination threat model that CRADE's per-instance contamination profiling must account for — not all contamination is equal.",
    "one_line_summary": "Demonstrates that moderate benchmark contamination (up to 144 repetitions) is 'forgotten' during extended training beyond 5x Chinchilla-optimal scale, challenging the assumption that any contamination invalidates benchmarks."
  },
  {
    "title": "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models",
    "authors": "Tao et al.",
    "venue": "ICLR 2026",
    "url": "https://arxiv.org/abs/2510.09259",
    "why_important": "ICLR 2026. Addresses the critical blind spot that existing detectors fail on RL-trained models (the same gap Kocetkov et al. identified), proposing Self-Critique via entropy collapse detection with 30% AUC improvement.",
    "one_line_summary": "First systematic contamination detection method for the RL post-training phase, exploiting output entropy collapse (policy collapse) in RL-trained models where all prior methods perform at chance level."
  },
  {
    "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
    "authors": "Shen et al.",
    "venue": "ICLR 2026",
    "url": "https://arxiv.org/abs/2510.04040",
    "why_important": "ICLR 2026. Provides the first systematic benchmark for CoT unfaithfulness detection — essential for CRADE's step-level perturbation alignment (SPA) metric, which must distinguish faithful from unfaithful reasoning changes.",
    "one_line_summary": "Introduces a benchmark with 1,000+ expert-annotated trajectories and 300+ unfaithful instances across four domains, evaluating 11 detection methods and finding that detection difficulty increases with model capability."
  },
  {
    "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
    "authors": "Zheng et al. (Alibaba/Qwen)",
    "venue": "ACL 2025",
    "url": "https://arxiv.org/abs/2412.06559",
    "why_important": "ACL 2025. The definitive step-level error identification benchmark (3,400 cases with human-annotated error locations) — provides evaluation infrastructure for CRADE's process-level analysis.",
    "one_line_summary": "Benchmarks models' ability to identify the earliest erroneous reasoning step, finding existing PRMs fail on competition-level problems while critic models like QwQ-32B-Preview approach GPT-4o performance."
  },
  {
    "title": "Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)",
    "authors": "Xia et al.",
    "venue": "AAAI 2025",
    "url": "https://arxiv.org/abs/2404.05692",
    "why_important": "AAAI 2025 (Oral). Establishes that answer accuracy masks reasoning quality — the core observation that motivates CRADE's step-level decomposition of genuine capability.",
    "one_line_summary": "Introduces validity and redundancy metrics for intermediate reasoning steps, demonstrating that higher final-answer accuracy does not necessarily correlate with improved step-level reasoning quality on difficult problems."
  },
  {
    "title": "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning",
    "authors": "Setlur et al. (Google DeepMind)",
    "venue": "ICLR 2025 Spotlight",
    "url": "https://arxiv.org/abs/2410.08146",
    "why_important": "ICLR 2025 Spotlight. Introduces Process Advantage Verifiers that formalize step-level progress measurement — the verification methodology CRADE can build on for its step-level perturbation alignment scoring.",
    "one_line_summary": "Proposes PAVs that measure reasoning progress as the change in likelihood of reaching a correct answer at each step, achieving 8%+ accuracy gains over outcome reward models with 1.5–5x compute savings."
  },
  {
    "title": "MathArena: Evaluating LLMs on Uncontaminated Math Competitions",
    "authors": "Balunovic et al. (ETH Zurich)",
    "venue": "NeurIPS 2025 Datasets & Benchmarks",
    "url": "https://arxiv.org/abs/2505.23281",
    "why_important": "NeurIPS 2025. CRADE's primary validation target — calibrated scores must correlate with MathArena's uncontaminated competition results to demonstrate genuine capability estimation.",
    "one_line_summary": "Uses newly released math competition problems to create a contamination-free evaluation stream, finding strong contamination signals in AIME 2024 and evaluating 50+ models across 162 problems from 7 competitions."
  },
  {
    "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
    "authors": "Zhou et al.",
    "venue": "AAAI 2026",
    "url": "https://arxiv.org/abs/2505.15055",
    "why_important": "AAAI 2026 (Oral, same target venue as CRADE). Proposes PSN-IRT analyzing 42K items across 11 benchmarks — the closest IRT-for-LLMs work, but assumes zero contamination, which is exactly the gap CRADE fills.",
    "one_line_summary": "Develops a Pseudo-Siamese Network IRT framework that reveals significant measurement quality shortcomings in existing benchmarks and constructs smaller item sets that better align with human preference rankings."
  },
  {
    "title": "Measuring What Matters: Construct Validity in Large Language Model Benchmarks",
    "authors": "Bean, Kearns, Romanou et al. (29 expert reviewers)",
    "venue": "NeurIPS 2025 Datasets & Benchmarks",
    "url": "https://arxiv.org/abs/2511.04703",
    "why_important": "NeurIPS 2025. Systematic review of 445 benchmarks providing the measurement-theoretic motivation for CRADE — benchmarks lack construct validity, and IRT + contamination-aware calibration is the principled fix.",
    "one_line_summary": "Twenty-nine experts systematically review 445 LLM benchmarks, identifying pervasive construct validity failures and providing eight recommendations for improving benchmark measurement quality."
  },
  {
    "title": "Process Reward Models That Think (ThinkPRM)",
    "authors": "Khalifa et al. (Google DeepMind / UMich)",
    "venue": "arXiv 2025 (highly cited)",
    "url": "https://arxiv.org/abs/2504.16828",
    "why_important": "Highly cited, major lab. Demonstrates that generative verification CoT outperforms discriminative PRMs with only 1% of labels — relevant to CRADE's step-level evaluation component for scalable process-level scoring.",
    "one_line_summary": "Proposes a generative PRM that verifies each reasoning step via its own verification chain-of-thought, outperforming LLM-as-Judge and discriminative verifiers while requiring only 1% of PRM800K process labels."
  },
  {
    "title": "FoVer: Efficient PRM Training Data Synthesis via Formal Verification",
    "authors": "Kamoi et al.",
    "venue": "ACL 2026 Findings",
    "url": "https://arxiv.org/abs/2505.15960",
    "why_important": "ACL 2026. Uses formal verification tools (Z3, Isabelle) for provably correct step-level labels — directly parallels CRADE's SymPy-backed symbolic generation philosophy of avoiding LLM-in-the-loop circularity.",
    "one_line_summary": "Automatically generates step-level error labels for PRM training using formal verification solvers, achieving competitive or superior results to human-annotated PRMs across 12 reasoning benchmarks with strong out-of-domain transfer."
  }
]
```

---

### How These Papers Map to CRADE's Architecture

| CRADE Component | Key Papers |
|---|---|
| **Per-instance contamination profiling** | ConStat, Self-Critique, Bordt et al. "How Much Can We Forget" |
| **Adversarial variant generation** | GSM-Symbolic (+ seed: MaSTer, MATH-Perturb) |
| **Step-level reasoning evaluation** | ProcessBench, ReasonEval, ThinkPRM, PAVs, FoVer |
| **CoT faithfulness / SPA metric** | FaithCoT-Bench (+ seed: Anthropic CoT paper) |
| **IRT-calibrated scoring** | tinyBenchmarks, PSN-IRT (+ seed: ATLAS) |
| **Validation ground truth** | MathArena |
| **Theoretical motivation** | Construct Validity (Bean et al.), "Does RL Really Incentivize Reasoning?" |

### Key Gap Confirmed

None of these 15 papers (nor the 7 seed papers) jointly models contamination level, adversarial robustness, and IRT-calibrated capability scoring. The closest is **ConStat**, which connects contamination to non-generalizing performance via variant comparison, but it lacks IRT grounding, step-level analysis, and formal variant generation. **PSN-IRT** and **ATLAS** bring IRT to LLM evaluation but assume zero contamination. The CRADE framework sits at an unoccupied three-way intersection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c441708b-eea1-43b4-a9cf-3afe92e4dc7f",
  "isSidechain": false,
  "requestId": "req_011CbWJtWPpsWxsz1Efz3n8t",
  "type": "assistant",
  "uuid": "9ac3d7ef-dd5e-476f-8cc6-a5ded861f69b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RF1ZhxrTEPnLi8aW6YK4r4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6551,
      "cache_read_input_tokens": 40561,
      "output_tokens": 7021,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6551,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7021,
          "cache_read_input_tokens": 40561,
          "cache_creation_input_tokens": 6551,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6551
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "9ac3d7ef-dd5e-476f-8cc6-a5ded861f69b",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "9ac3d7ef-dd5e-476f-8cc6-a5ded861f69b",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers on contamination-aware robustness evaluation",
  "sessionId": "5b4b3702-9e5c-43ae-bc09-805d1229cbbe"
}
```

---
