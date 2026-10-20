# Research conversation: You are a senior ML researcher conducting a comprehensive literature survey. **Today's date: 2026-05-28 (UTC).** ## Task

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/e129977f-c1e3-4a0b-a667-ea67c19c205f.jsonl`
- **Structured JSON:** [`27bc5fa17ad67864c036.json`](../../sessions/27/27bc5fa17ad67864c036.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T10:15:48.308Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T10:15:48.308Z",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "content": "You are a senior ML researcher conducting a comprehensive literature survey.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Task\nFind the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:\n\n**Target: AAAI 2026\nTrack: AI Alignment / Main Technical Track — Robustness Evaluation\n\nDirection: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated \"genuine capability\" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.\n\nSeed Papers:\n- Zawalski et al. \"CoDeC\" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation\n- Li et al. \"ATLAS\" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity\n- Hou et al. \"MaSTer\" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination\n- Zheng et al. \"ReasoningMath-Plus\" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component\n- Chen et al. \"Reasoning Models Don't Always Say What They Think\" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination\n- Xu et al. \"DCR\" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis\n- Kocetkov et al. \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches\n\nKnown Gaps:\n- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)\n- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only\n- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing\n- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives\n\nTheoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)\n- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)\n- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth\n\nQuality Self-Checks:\n- [x] Core insight: \"Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level.\"\n- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.\n- [x] Baseline fear test: A simple baseline of \"run on variants and average\" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.\n- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.\n\nAvoid:\n- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)\n- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark\n- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)\n- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead**\n\n## What counts as 'important'\n\nPrioritize (in order):\n1. **Best paper awards** at top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, AAAI, etc.)\n2. **Oral / spotlight presentations** at these venues\n3. **Highly cited papers** (>50 citations in 1-2 years)\n4. **Papers that introduced widely-adopted methods** (e.g., new training paradigm, new benchmark)\n5. **Recent survey papers** that provide comprehensive field overviews\n6. **Strong recent work** from top labs (Google, Meta, DeepMind, OpenAI, CMU, Stanford, etc.)\n\n## Search strategy\n\nExecute AT LEAST 15 targeted searches:\n\n1. `best paper award ACL EMNLP NeurIPS ICML ICLR 2026 Target: AAAI 2026\nTrack: AI Alignment / Main Technical Track — Robustness Evaluation\n\nDirection: Build an end-to-end framework (CRADE) that jointly profiles per-instance contamination, generates adversarial functional variants with provable correctness, evaluates reasoning at the step level, and produces IRT-calibrated \"genuine capability\" scores that decompose observed performance into true ability, contamination boost, and robustness deficit. The core insight is that contamination and robustness are entangled — a model may fail perturbations because it memorized answers OR because it lacks genuine reasoning, and disentangling these requires joint modeling that no existing work provides.\n\nSeed Papers:\n- Zawalski et al. \"CoDeC\" (NVIDIA, arXiv 2025) — Gray-box contamination detection at 99.9% AUC; provides the detection backbone but produces no corrective evaluation\n- Li et al. \"ATLAS\" (arXiv 2025) — IRT-based adaptive testing achieving 90% item reduction; demonstrates IRT's power for LLM evaluation but assumes test integrity\n- Hou et al. \"MaSTer\" (arXiv 2026) — Automated adversarial math variant generation with 48% accuracy reduction; best current perturbation method but disconnected from contamination\n- Zheng et al. \"ReasoningMath-Plus\" (arXiv 2026) — Step-level evaluation showing answer-level overestimates by ~1.4 points; proves process-level matters but lacks adversarial component\n- Chen et al. \"Reasoning Models Don't Always Say What They Think\" (Anthropic, May 2025) — CoT faithfulness is only 25% for hint disclosure; establishes that CoT is unreliable but doesn't connect to contamination\n- Xu et al. \"DCR\" (arXiv 2025) — Contamination-adjusted scores via fuzzy inference; closest competitor but lacks IRT grounding, variant generation, and process-level analysis\n- Kocetkov et al. \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" (arXiv Oct 2025) — Shows detection fails for reasoning models; establishes urgent need for new approaches\n\nKnown Gaps:\n- No framework jointly estimates contamination level, generates adversarial variants, and produces a single calibrated capability score (existing work addresses these in isolation)\n- Step-level perturbation alignment (whether CoT appropriately tracks problem changes) has never been measured or connected to contamination — all adversarial work evaluates final answers only\n- Item Response Theory for LLM evaluation (ATLAS, PSN-IRT) assumes zero contamination; contamination-aware IRT with joint ability-contamination estimation is entirely missing\n- Existing contamination detection fails on reasoning models (near random-guess), creating demand for process-level and faithfulness-based alternatives\n\nTheoretical Anchor: Contamination-aware 3PL IRT model: P(correct | θ_j, d_i, c_ij) = c_ij · p_mem + (1 - c_ij) · σ(θ_j - d_i), with EM-based joint estimation of ability θ, difficulty d, and contamination indicators c. The decomposition Observed_accuracy = G + C - R (genuine capability + contamination boost - robustness deficit) provides a formal framework grounded in measurement theory.\n\nConstraints:\n- Compute: ≤200 H100-hours (estimated ~120 for combined RQ1+RQ2)\n- Timeline: 8-10 weeks to AAAI deadline (abstract July 25, paper August 1)\n- Must validate calibrated scores against MathArena's uncontaminated 2025 competition data as ground truth\n\nQuality Self-Checks:\n- [x] Core insight: \"Contamination and robustness are entangled — you can't measure one without accounting for the other, and disentangling them requires joint modeling at the reasoning-step level.\"\n- [x] Why not obvious: The contamination-detection and adversarial-robustness communities are separate research streams with different venues and different authors; the IRT-for-LLMs community is a third silo. Nobody sits at the three-way intersection. DCR Factor shows the field is approaching this but only from the detection+adjustment angle.\n- [x] Baseline fear test: A simple baseline of \"run on variants and average\" loses the contamination-robustness decomposition and the step-level memorization signatures — the calibrated IRT score and process-level SPA metric are what differentiate.\n- [x] Information exploited: Per-instance contamination profiles crossed with per-variant step-level reasoning chain changes — no existing method uses this joint signal.\n\nAvoid:\n- Pure contamination detection without corrective evaluation (saturated space with 5+ strong methods)\n- Yet another dynamic benchmark (LiveBench, MathArena, DyVal already exist) — this must be a framework applicable to ANY existing benchmark\n- Ad-hoc perturbation studies on single benchmarks without methodological/theoretical contribution (GSM-Plus, GSM-Symbolic, MATH-Perturb already cover this)\n- Using LLMs in the variant generation loop (creates circular dependency and unverifiable correctness) — use SymPy-backed symbolic generation instead`\n2. `oral spotlight {venue} 2026 {topic}` — for each major venue\n3. `site:openreview.net {topic} 2026 outstanding` — OpenReview 高分论文\n4. `{topic} survey 2026` 或 `{topic} survey 2025` — 综述论文\n5. `site:arxiv.org {topic} 2026` — arXiv 最新高引\n6. `most cited {topic} 2025 2026` — Google Scholar\n7. `site:paperswithcode.com {task} SOTA` — SOTA 排行榜上的论文\n8. `{topic} benchmark {year}` — 定义领域的 benchmark 论文\n9. 对每个找到的重要论文，搜索其 cited-by 发现后续工作\n\nFor EVERY paper you find, use WebFetch to read its abstract and introduction on arXiv or OpenReview. Do NOT rely on search snippets alone — you need to understand what each paper actually does.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Full paper title\",\n  \"authors\": \"First author et al.\",\n  \"venue\": \"EMNLP 2025 / NeurIPS 2024 / arXiv 2025 / ...\",\n  \"url\": \"https://arxiv.org/abs/... or openreview URL\",\n  \"why_important\": \"Best paper / Oral / High-cited / Introduced X / ...\",\n  \"one_line_summary\": \"What this paper does in one sentence\"\n}\n\nFind at least 15 papers. More is better if they are genuinely relevant.\nIMPORTANT: You MUST end your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T10:15:48.316Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T10:15:48.316Z",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

## Round 1

54 recorded events

### User

_source line 3 · 2026-05-28T10:15:48.346Z_

You are a senior ML researcher conducting a comprehensive literature survey.

**Today's date: 2026-05-28 (UTC).**

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
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "625536aa-0582-4e2d-b94a-7f30c97f670b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T10:15:48.343Z_

```json
{
  "parentUuid": "625536aa-0582-4e2d-b94a-7f30c97f670b",
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
  "uuid": "e4720ba6-8fcb-4fdc-80d0-4ddd07da59f6",
  "timestamp": "2026-05-28T10:15:48.343Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T10:15:48.343Z_

```json
{
  "parentUuid": "e4720ba6-8fcb-4fdc-80d0-4ddd07da59f6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fa453b6a-ec7e-47e7-8e79-de37b15e2190",
  "timestamp": "2026-05-28T10:15:48.343Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
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
  "aiTitle": "Survey 15 key papers for contamination-aware reasoning evaluation",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Assistant

_source line 7 · 2026-05-28T10:15:55.436Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a comprehensive literature survey for their CRADE framework paper targeting AAAI 2026. I need to find the 15 most important recent papers (2024-2026) related to their research area, which spans:

1. Benchmark contamination detection and correction
2. Adversarial robustness evaluation for LLMs
3. Item Response Theory (IRT) for LLM evaluation
4. Step-level reasoning evaluation
5. Chain-of-thought faithfulness
6. Mathematical reasoning robustness

Let me launch multiple search agents in parallel to cover different aspects of this research area. 

I need to initialize the WebSearch and WebFetch tools first since they're deferred, then I can start querying for relevant papers across these different research dimensions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa453b6a-ec7e-47e7-8e79-de37b15e2190",
  "isSidechain": false,
  "requestId": "req_011CbUnvP7aq9AxgQV5vvD1B",
  "type": "assistant",
  "uuid": "ea196002-4705-4910-8a5c-0c9ac84e772b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxLFyEbEfb61HeY3vshpoj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15557,
      "cache_read_input_tokens": 0,
      "output_tokens": 257,
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
          "output_tokens": 257,
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

_source line 8 · 2026-05-28T10:15:55.439Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ddd7oL54DZQMjEA42NNmtt`</summary>

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
  "parentUuid": "ea196002-4705-4910-8a5c-0c9ac84e772b",
  "isSidechain": false,
  "requestId": "req_011CbUnvP7aq9AxgQV5vvD1B",
  "type": "assistant",
  "uuid": "dffd4807-7a03-464f-8d1e-80463c2131fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CxLFyEbEfb61HeY3vshpoj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15557,
      "cache_read_input_tokens": 0,
      "output_tokens": 257,
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
          "output_tokens": 257,
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

_source line 9 · 2026-05-28T10:15:55.450Z_

<details><summary>↩ Tool result · `toolu_01Ddd7oL54DZQMjEA42NNmtt`</summary>

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
  "parentUuid": "dffd4807-7a03-464f-8d1e-80463c2131fe",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "214508b3-bbc6-4219-8ba6-79bcc6ad6c7a",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "dffd4807-7a03-464f-8d1e-80463c2131fe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-28 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "214508b3-bbc6-4219-8ba6-79bcc6ad6c7a",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers for contamination-aware reasoning evaluation",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Assistant

_source line 12 · 2026-05-28T10:16:03.811Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have WebSearch and WebFetch available. Let me launch multiple parallel search agents to cover the different research areas comprehensively. I'll split the work into several parallel agents to maximize coverage.

Let me design the search strategy:

1. Contamination detection and correction in LLM evaluation
2. Adversarial robustness / perturbation methods for math reasoning
3. Item Response Theory (IRT) for LLM evaluation
4. Step-level reasoning evaluation and CoT faithfulness
5. Best paper awards at top venues 2024-2026 related to LLM evaluation
6. Dynamic benchmarks and contamination-resistant evaluation


7. Key seed papers and their citations

Now I'll spin up multiple agents to search these areas in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "214508b3-bbc6-4219-8ba6-79bcc6ad6c7a",
  "isSidechain": false,
  "requestId": "req_011CbUnvueseokbKWHfrp7mH",
  "type": "assistant",
  "uuid": "451231cd-bfff-4b87-a3cb-1a357440e7a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU7aknVEwVDJ7TJ63QdxNq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2500,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1277
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

_source line 13 · 2026-05-28T10:16:03.813Z_

I'll conduct a comprehensive parallel search across multiple research dimensions. Let me launch several specialized search agents simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "451231cd-bfff-4b87-a3cb-1a357440e7a7",
  "isSidechain": false,
  "requestId": "req_011CbUnvueseokbKWHfrp7mH",
  "type": "assistant",
  "uuid": "8a492851-96e9-4333-8970-d64c89bc947f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU7aknVEwVDJ7TJ63QdxNq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2500,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1277
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

_source line 14 · 2026-05-28T10:16:09.165Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KP3Rv1kyRaaDAhVeDnH4hQ`</summary>

```json
{
  "description": "Search contamination detection papers",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs. \n\nSearch for the most important recent papers (2024-2026) on **benchmark contamination detection and correction for LLMs**. This includes:\n- Methods for detecting data contamination/memorization in LLM benchmarks\n- Approaches to correct or adjust evaluation scores for contamination\n- Studies on how contamination affects LLM evaluation reliability\n\nExecute these searches:\n1. WebSearch: \"LLM benchmark contamination detection 2025 2026\"\n2. WebSearch: \"data contamination large language models evaluation correction 2025\"\n3. WebSearch: \"CoDeC contamination detection gray-box NVIDIA 2025\"\n4. WebSearch: \"DCR contamination-adjusted scores fuzzy inference LLM 2025\"\n5. WebSearch: \"fragility benchmark contamination detection reasoning models Kocetkov 2025\"\n6. WebSearch: \"benchmark integrity LLM memorization test set leakage 2025 2026\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a492851-96e9-4333-8970-d64c89bc947f",
  "isSidechain": false,
  "requestId": "req_011CbUnvueseokbKWHfrp7mH",
  "type": "assistant",
  "uuid": "e05a400d-6af8-4dcc-bce5-345b9068f3b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU7aknVEwVDJ7TJ63QdxNq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2500,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1277
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

_source line 15 · 2026-05-28T10:16:15.032Z_

<details open><summary>🔧 Tool call — Agent · `toolu_013oCXva5v2rBEdpLdtMCysT`</summary>

```json
{
  "description": "Search adversarial robustness math reasoning",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs.\n\nSearch for the most important recent papers (2024-2026) on **adversarial robustness evaluation and perturbation methods for LLM mathematical/logical reasoning**. This includes:\n- Generating adversarial variants of math problems to test robustness\n- Symbolic perturbation methods for benchmarks\n- Studies showing LLMs fail on perturbed versions of known problems\n- Functional variant generation with provable correctness\n\nExecute these searches:\n1. WebSearch: \"adversarial math problem generation LLM robustness evaluation 2025 2026\"\n2. WebSearch: \"MaSTer automated adversarial math variant generation 2026\"\n3. WebSearch: \"GSM-Symbolic GSM-Plus MATH-Perturb benchmark perturbation LLM 2024 2025\"\n4. WebSearch: \"symbolic perturbation mathematical reasoning robustness LLM 2025\"\n5. WebSearch: \"functional variant generation benchmark LLM provable correctness 2025 2026\"\n6. WebSearch: \"reasoning robustness LLM NeurIPS ICML ICLR 2025 2026\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e05a400d-6af8-4dcc-bce5-345b9068f3b9",
  "isSidechain": false,
  "requestId": "req_011CbUnvueseokbKWHfrp7mH",
  "type": "assistant",
  "uuid": "becd2467-9db3-4703-9d88-585f7ce182a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU7aknVEwVDJ7TJ63QdxNq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2500,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1277
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

_source line 16 · 2026-05-28T10:16:19.673Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017ujnfS3688azZezYs8Y6Fy`</summary>

```json
{
  "description": "Search IRT for LLM evaluation",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs.\n\nSearch for the most important recent papers (2024-2026) on **Item Response Theory (IRT) applied to LLM evaluation** and **psychometrics-based approaches to AI assessment**. This includes:\n- IRT models adapted for evaluating language models\n- Adaptive testing frameworks for LLMs\n- Psychometric approaches to benchmark design\n- Calibrated scoring and measurement theory for AI\n\nExecute these searches:\n1. WebSearch: \"item response theory LLM evaluation 2025 2026\"\n2. WebSearch: \"ATLAS IRT adaptive testing large language models 2025\"\n3. WebSearch: \"psychometrics LLM benchmark evaluation calibration 2024 2025\"\n4. WebSearch: \"IRT computerized adaptive testing AI models 2025 2026\"\n5. WebSearch: \"PSN-IRT language model evaluation arXiv 2025\"\n6. WebSearch: \"measurement theory AI evaluation scoring 2025 2026\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "becd2467-9db3-4703-9d88-585f7ce182a8",
  "isSidechain": false,
  "requestId": "req_011CbUnvueseokbKWHfrp7mH",
  "type": "assistant",
  "uuid": "7b76c1cb-7be3-4bd6-bb1d-148822f6c717",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU7aknVEwVDJ7TJ63QdxNq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2500,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1277
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

_source line 17 · 2026-05-28T10:16:25.338Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BYeFkhCoVwszyfscvx7j5w`</summary>

```json
{
  "description": "Search step-level reasoning and CoT faithfulness",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs.\n\nSearch for the most important recent papers (2024-2026) on **step-level reasoning evaluation, chain-of-thought faithfulness, and process-level assessment of LLMs**. This includes:\n- Step-by-step evaluation of mathematical reasoning\n- Chain-of-thought faithfulness and reliability\n- Process reward models and step-level verification\n- Whether LLMs' reasoning chains reflect their actual computation\n\nExecute these searches:\n1. WebSearch: \"chain of thought faithfulness LLM reasoning 2025 2026\"\n2. WebSearch: \"Reasoning Models Don't Always Say What They Think Anthropic Chen 2025\"\n3. WebSearch: \"step-level evaluation mathematical reasoning LLM 2025 2026\"\n4. WebSearch: \"ReasoningMath-Plus step-level evaluation arXiv 2026\"\n5. WebSearch: \"process reward model verification reasoning LLM 2024 2025\"\n6. WebSearch: \"CoT unfaithfulness reasoning trace reliability LLM 2025\"\n7. WebSearch: \"reasoning evaluation process-level NeurIPS ICML 2025 2026\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7b76c1cb-7be3-4bd6-bb1d-148822f6c717",
  "isSidechain": false,
  "requestId": "req_011CbUnvueseokbKWHfrp7mH",
  "type": "assistant",
  "uuid": "c98f29ff-fdd0-4417-836e-df750f575bc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU7aknVEwVDJ7TJ63QdxNq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2500,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1277
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

_source line 18 · 2026-05-28T10:16:30.513Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UBeyCgVg2XWbpauMUrHGNZ`</summary>

```json
{
  "description": "Search best papers and LLM evaluation frameworks",
  "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs.\n\nSearch for **best paper awards, oral/spotlight presentations, and highly-cited work** at top venues (2024-2026) related to LLM evaluation, robustness, and alignment. Also search for comprehensive evaluation frameworks and dynamic benchmarks.\n\nExecute these searches:\n1. WebSearch: \"best paper award NeurIPS 2025 LLM evaluation\"\n2. WebSearch: \"best paper award ICML 2025 language model\"\n3. WebSearch: \"best paper ICLR 2025 2026 LLM benchmark evaluation\"\n4. WebSearch: \"best paper ACL EMNLP 2025 evaluation robustness\"\n5. WebSearch: \"LiveBench MathArena dynamic benchmark LLM contamination-free 2024 2025\"\n6. WebSearch: \"LLM evaluation framework comprehensive robustness contamination 2025 2026\"\n7. WebSearch: \"AAAI 2025 2026 best paper AI alignment evaluation\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c98f29ff-fdd0-4417-836e-df750f575bc5",
  "isSidechain": false,
  "requestId": "req_011CbUnvueseokbKWHfrp7mH",
  "type": "assistant",
  "uuid": "f4b2b52a-63c4-4a80-912d-f33729083e7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YU7aknVEwVDJ7TJ63QdxNq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1277,
      "cache_read_input_tokens": 15557,
      "output_tokens": 2500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1277,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2500,
          "cache_read_input_tokens": 15557,
          "cache_creation_input_tokens": 1277,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1277
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

_source line 19 · 2026-05-28T10:18:09.894Z_

<details><summary>↩ Tool result · `toolu_01KP3Rv1kyRaaDAhVeDnH4hQ`</summary>

```text
I now have comprehensive information on all the key papers. Here is the structured report.

---

## Literature Survey: Benchmark Contamination Detection and Correction for LLMs (2024--2026)

Below are 11 relevant papers organized by topic area.

---

### A. Detection Methods

**1. CoDeC: Detecting Data Contamination in LLMs via In-Context Learning**
- **Authors:** Zawalski et al. (Michal Zawalski, Meriem Boubdir, Klaudia Balazy, Besmira Nushi, Pablo Ribalta)
- **Venue/Year:** arXiv 2025; accepted at ICLR 2026
- **URL:** https://arxiv.org/abs/2510.27055
- **What it does:** Introduces a gray-box contamination detection method that measures how in-context examples affect model confidence -- in-context examples boost confidence on unseen data but reduce it on memorized data, producing interpretable contamination scores that are model- and dataset-agnostic.
- **Why it's important:** Accepted at ICLR 2026; tested on NVIDIA Nemotron models; practical enough for integration into standard benchmarking pipelines.

**2. PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models**
- **Authors:** Zhang et al. (Huixuan Zhang, Yun Lin, Xiaojun Wan)
- **Venue/Year:** EMNLP 2024 Findings
- **URL:** https://arxiv.org/abs/2406.18326
- **What it does:** Constructs distributional counterparts for each benchmark sample and applies statistical significance testing to detect whether models show heightened confidence on original benchmarks versus paraphrased counterparts.
- **Why it's important:** Found that "almost all models and benchmarks tested are suspected contaminated"; published at EMNLP 2024.

**3. Detecting Benchmark Contamination Through Watermarking**
- **Authors:** Sander et al. (Tom Sander, Pierre Fernandez, Saeed Mahloujifar, Alain Durmus, Chuan Guo)
- **Venue/Year:** arXiv, February 2025
- **URL:** https://arxiv.org/abs/2502.17259
- **What it does:** Embeds non-intrusive watermarks in benchmark datasets before release, enabling proactive contamination detection via statistical testing (e.g., p-val = 10^-3 for a +5% gain on ARC-Easy) without altering benchmark utility.
- **Why it's important:** Introduces a prevention-oriented paradigm (watermarking at benchmark creation time) rather than post-hoc detection; validated with controlled 1B-parameter pretraining experiments.

---

### B. Contamination Quantification and Score Correction

**4. DCR: Quantifying Data Contamination in LLMs Evaluation**
- **Authors:** Xu et al. (Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, Tahar Kechadi)
- **Venue/Year:** EMNLP 2025
- **URL:** https://aclanthology.org/2025.emnlp-main.1173/
- **What it does:** Proposes the DCR framework that detects contamination at four granular levels (semantic, informational, data, label) and synthesizes them via a fuzzy inference system into a unified "DCR Factor" that adjusts raw accuracy scores, achieving within 4% average error of uncontaminated baselines.
- **Why it's important:** Published at EMNLP 2025; the only framework that produces contamination-adjusted benchmark scores; open-source at https://github.com/chengxuphd/dcr.

**5. Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models**
- **Authors:** Dong et al. (Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, Ge Li)
- **Venue/Year:** ACL 2024
- **URL:** https://arxiv.org/abs/2402.15938
- **What it does:** Proposes CDD (Contamination Detection via output Distribution) and TED (Trustworthy Evaluation via output Distribution) -- CDD detects contamination by analyzing output distribution peakedness, while TED mitigates contamination effects, reducing contamination-related performance gains by up to 66.9%.
- **Why it's important:** Published at ACL 2024; 21.8--30.2% improvement over prior contamination detection methods; revealed potential contamination in ChatGPT's HumanEval performance.

**6. Quantifying the Effect of Test Set Contamination on Generative Evaluations**
- **Authors:** Schaeffer et al. (Rylan Schaeffer, Joshua Kazdan, Baber Abbasi, Ken Ziyu Liu, Brando Miranda, Ahmed Ahmed, Fazl Berez, Abhay Puri, Stella Biderman, Niloofar Mireshghallah, Sanmi Koyejo)
- **Venue/Year:** arXiv, January 2026
- **URL:** https://arxiv.org/abs/2601.04301
- **What it does:** Quantifies the dose-response curve of test set contamination on generative (not just discriminative) evaluations by pretraining models on controlled mixtures of web data and MATH benchmark replicas, finding that even a single test set replica enables models to achieve lower loss than the irreducible error of uncontaminated training.
- **Why it's important:** First controlled study of contamination effects on generative benchmarks; establishes that contamination dynamics differ fundamentally between discriminative and generative evaluation.

---

### C. Fragility and Evasion of Detection

**7. On The Fragility of Benchmark Contamination Detection in Reasoning Models**
- **Authors:** Wang et al. (Han Wang, Haoyu Li, Brian Ko, Huan Zhang)
- **Venue/Year:** arXiv 2025; accepted at ICLR 2026
- **URL:** https://arxiv.org/abs/2510.02386
- **What it does:** Demonstrates that evading contamination detection in Large Reasoning Models (LRMs) is alarmingly easy -- RL training (GRPO) after SFT contamination conceals memorization signals, and contamination with chain-of-thought makes nearly all existing detection methods perform at random-guess level. Identifies PPO-style importance sampling and clipping as the root cause.
- **Why it's important:** Accepted at ICLR 2026; a critical negative result showing that current detection methods are fundamentally insufficient for reasoning models, directly motivating new detection paradigms.

---

### D. Contamination-Resistant Evaluation and Dynamic Benchmarks

**8. AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge**
- **Authors:** Wu et al. (Xiaobao Wu, Liangming Pan, Yuxi Xie, Ruiwen Zhou, Shuai Zhao, Yubo Ma, Mingzhe Du, Rui Mao, Anh Tuan Luu, William Yang Wang)
- **Venue/Year:** ACL 2025
- **URL:** https://arxiv.org/abs/2412.13670
- **What it does:** Automatically constructs contamination-free benchmarks from timestamped knowledge graphs (Wikidata), ensuring test samples use only knowledge that postdates each LLM's training cutoff, eliminating the need for human labor in benchmark maintenance.
- **Why it's important:** Published at ACL 2025; fully automated pipeline that scales to new models; found evidence that contamination may occur before stated model cutoff dates.

**9. CLEAN-EVAL: Clean Evaluation on Contaminated Large Language Models**
- **Authors:** Zhu et al. (Wenhong Zhu, Hongkun Hao, Zhiwei He, Yunze Song, Yumeng Zhang, Hanxu Hu, Yiran Wei, Rui Wang, Hongyuan Lu)
- **Venue/Year:** NAACL 2024 Findings
- **URL:** https://arxiv.org/abs/2311.09154
- **What it does:** Uses an LLM to paraphrase and back-translate contaminated benchmark data into semantically equivalent but surface-form-different candidates, enabling cleaner evaluation under both few-shot and fine-tuning scenarios.
- **Why it's important:** Published at NAACL 2024; practical remediation approach that works without retraining models.

**10. When Benchmarks Leak: Inference-Time Decontamination for LLMs**
- **Authors:** Chai et al. (Jianzhe Chai, Yu Zhe, Jun Sakuma)
- **Venue/Year:** arXiv, January 2026
- **URL:** https://arxiv.org/abs/2601.19334
- **What it does:** Proposes DeconIEP, an inference-time decontamination method that applies small, bounded perturbations in the input embedding space guided by a reference model to redirect models away from memorization shortcuts during evaluation, without modifying the model itself.
- **Why it's important:** Novel inference-time approach (no retraining or benchmark modification needed); addresses contamination at test time rather than at benchmark creation or training time.

---

### E. Surveys

**11. Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation**
- **Authors:** Chen et al. (Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray)
- **Venue/Year:** EMNLP 2025
- **URL:** https://aclanthology.org/2025.emnlp-main.511/
- **What it does:** Comprehensive survey analyzing the shift from static to dynamic LLM benchmarking to address data contamination, proposing design principles for dynamic benchmarks and evaluating current approaches; maintains an open repository of benchmarking techniques.
- **Why it's important:** Published at EMNLP 2025; the most comprehensive survey on this topic at a top venue; provides a taxonomy and design principles for the field.

**(Also notable)** **A Survey on Data Contamination for Large Language Models** -- Cheng et al. (arXiv, February 2025, https://arxiv.org/abs/2502.14425) provides a complementary survey categorizing detection methods into white-box, gray-box, and black-box approaches, and evaluation mitigation into data updating, data rewriting, and prevention strategies.

---

### Summary Table

| # | Paper | Venue | Type | Key Contribution |
|---|-------|-------|------|-----------------|
| 1 | CoDeC (Zawalski et al.) | ICLR 2026 | Detection | Gray-box detection via in-context learning |
| 2 | PaCoST (Zhang et al.) | EMNLP 2024 | Detection | Statistical paired-confidence testing |
| 3 | Watermarking (Sander et al.) | arXiv 2025 | Prevention | Proactive watermark-based detection |
| 4 | DCR (Xu et al.) | EMNLP 2025 | Correction | Fuzzy-inference contamination-adjusted scores |
| 5 | CDD/TED (Dong et al.) | ACL 2024 | Detection+Correction | Output distribution analysis for detection and mitigation |
| 6 | Schaeffer et al. | arXiv 2026 | Measurement | Dose-response curve for generative evaluation |
| 7 | Fragility (Wang et al.) | ICLR 2026 | Negative result | Detection evasion in reasoning models |
| 8 | AntiLeakBench (Wu et al.) | ACL 2025 | Dynamic benchmark | Auto-constructed contamination-free benchmarks |
| 9 | CLEAN-EVAL (Zhu et al.) | NAACL 2024 | Remediation | Paraphrase-based clean evaluation |
| 10 | DeconIEP (Chai et al.) | arXiv 2026 | Remediation | Inference-time embedding perturbation |
| 11 | Chen et al. survey | EMNLP 2025 | Survey | Static-to-dynamic benchmarking taxonomy |

This collection covers the full pipeline: detection (papers 1-3), quantification and score correction (papers 4-6), fragility/limitations of detection (paper 7), contamination-resistant evaluation (papers 8-10), and comprehensive surveys (paper 11). The two ICLR 2026 acceptances (CoDeC and Fragility) and three EMNLP 2025 papers represent the most recent top-venue publications in this area.

agentId: af66166d96ed1cb41 (use SendMessage with to: 'af66166d96ed1cb41' to continue this agent)
&lt;usage>total_tokens: 24547
tool_uses: 22
duration_ms: 120720&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e05a400d-6af8-4dcc-bce5-345b9068f3b9",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "42eb747a-aedb-4cb7-a30c-e509e4f85654",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs. \n\nSearch for the most important recent papers (2024-2026) on **benchmark contamination detection and correction for LLMs**. This includes:\n- Methods for detecting data contamination/memorization in LLM benchmarks\n- Approaches to correct or adjust evaluation scores for contamination\n- Studies on how contamination affects LLM evaluation reliability\n\nExecute these searches:\n1. WebSearch: \"LLM benchmark contamination detection 2025 2026\"\n2. WebSearch: \"data contamination large language models evaluation correction 2025\"\n3. WebSearch: \"CoDeC contamination detection gray-box NVIDIA 2025\"\n4. WebSearch: \"DCR contamination-adjusted scores fuzzy inference LLM 2025\"\n5. WebSearch: \"fragility benchmark contamination detection reasoning models Kocetkov 2025\"\n6. WebSearch: \"benchmark integrity LLM memorization test set leakage 2025 2026\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
    "agentId": "af66166d96ed1cb41",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all the key papers. Here is the structured report.\n\n---\n\n## Literature Survey: Benchmark Contamination Detection and Correction for LLMs (2024--2026)\n\nBelow are 11 relevant papers organized by topic area.\n\n---\n\n### A. Detection Methods\n\n**1. CoDeC: Detecting Data Contamination in LLMs via In-Context Learning**\n- **Authors:** Zawalski et al. (Michal Zawalski, Meriem Boubdir, Klaudia Balazy, Besmira Nushi, Pablo Ribalta)\n- **Venue/Year:** arXiv 2025; accepted at ICLR 2026\n- **URL:** https://arxiv.org/abs/2510.27055\n- **What it does:** Introduces a gray-box contamination detection method that measures how in-context examples affect model confidence -- in-context examples boost confidence on unseen data but reduce it on memorized data, producing interpretable contamination scores that are model- and dataset-agnostic.\n- **Why it's important:** Accepted at ICLR 2026; tested on NVIDIA Nemotron models; practical enough for integration into standard benchmarking pipelines.\n\n**2. PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models**\n- **Authors:** Zhang et al. (Huixuan Zhang, Yun Lin, Xiaojun Wan)\n- **Venue/Year:** EMNLP 2024 Findings\n- **URL:** https://arxiv.org/abs/2406.18326\n- **What it does:** Constructs distributional counterparts for each benchmark sample and applies statistical significance testing to detect whether models show heightened confidence on original benchmarks versus paraphrased counterparts.\n- **Why it's important:** Found that \"almost all models and benchmarks tested are suspected contaminated\"; published at EMNLP 2024.\n\n**3. Detecting Benchmark Contamination Through Watermarking**\n- **Authors:** Sander et al. (Tom Sander, Pierre Fernandez, Saeed Mahloujifar, Alain Durmus, Chuan Guo)\n- **Venue/Year:** arXiv, February 2025\n- **URL:** https://arxiv.org/abs/2502.17259\n- **What it does:** Embeds non-intrusive watermarks in benchmark datasets before release, enabling proactive contamination detection via statistical testing (e.g., p-val = 10^-3 for a +5% gain on ARC-Easy) without altering benchmark utility.\n- **Why it's important:** Introduces a prevention-oriented paradigm (watermarking at benchmark creation time) rather than post-hoc detection; validated with controlled 1B-parameter pretraining experiments.\n\n---\n\n### B. Contamination Quantification and Score Correction\n\n**4. DCR: Quantifying Data Contamination in LLMs Evaluation**\n- **Authors:** Xu et al. (Cheng Xu, Nan Yan, Shuhao Guan, Changhong Jin, Yuke Mei, Yibing Guo, Tahar Kechadi)\n- **Venue/Year:** EMNLP 2025\n- **URL:** https://aclanthology.org/2025.emnlp-main.1173/\n- **What it does:** Proposes the DCR framework that detects contamination at four granular levels (semantic, informational, data, label) and synthesizes them via a fuzzy inference system into a unified \"DCR Factor\" that adjusts raw accuracy scores, achieving within 4% average error of uncontaminated baselines.\n- **Why it's important:** Published at EMNLP 2025; the only framework that produces contamination-adjusted benchmark scores; open-source at https://github.com/chengxuphd/dcr.\n\n**5. Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models**\n- **Authors:** Dong et al. (Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, Ge Li)\n- **Venue/Year:** ACL 2024\n- **URL:** https://arxiv.org/abs/2402.15938\n- **What it does:** Proposes CDD (Contamination Detection via output Distribution) and TED (Trustworthy Evaluation via output Distribution) -- CDD detects contamination by analyzing output distribution peakedness, while TED mitigates contamination effects, reducing contamination-related performance gains by up to 66.9%.\n- **Why it's important:** Published at ACL 2024; 21.8--30.2% improvement over prior contamination detection methods; revealed potential contamination in ChatGPT's HumanEval performance.\n\n**6. Quantifying the Effect of Test Set Contamination on Generative Evaluations**\n- **Authors:** Schaeffer et al. (Rylan Schaeffer, Joshua Kazdan, Baber Abbasi, Ken Ziyu Liu, Brando Miranda, Ahmed Ahmed, Fazl Berez, Abhay Puri, Stella Biderman, Niloofar Mireshghallah, Sanmi Koyejo)\n- **Venue/Year:** arXiv, January 2026\n- **URL:** https://arxiv.org/abs/2601.04301\n- **What it does:** Quantifies the dose-response curve of test set contamination on generative (not just discriminative) evaluations by pretraining models on controlled mixtures of web data and MATH benchmark replicas, finding that even a single test set replica enables models to achieve lower loss than the irreducible error of uncontaminated training.\n- **Why it's important:** First controlled study of contamination effects on generative benchmarks; establishes that contamination dynamics differ fundamentally between discriminative and generative evaluation.\n\n---\n\n### C. Fragility and Evasion of Detection\n\n**7. On The Fragility of Benchmark Contamination Detection in Reasoning Models**\n- **Authors:** Wang et al. (Han Wang, Haoyu Li, Brian Ko, Huan Zhang)\n- **Venue/Year:** arXiv 2025; accepted at ICLR 2026\n- **URL:** https://arxiv.org/abs/2510.02386\n- **What it does:** Demonstrates that evading contamination detection in Large Reasoning Models (LRMs) is alarmingly easy -- RL training (GRPO) after SFT contamination conceals memorization signals, and contamination with chain-of-thought makes nearly all existing detection methods perform at random-guess level. Identifies PPO-style importance sampling and clipping as the root cause.\n- **Why it's important:** Accepted at ICLR 2026; a critical negative result showing that current detection methods are fundamentally insufficient for reasoning models, directly motivating new detection paradigms.\n\n---\n\n### D. Contamination-Resistant Evaluation and Dynamic Benchmarks\n\n**8. AntiLeakBench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge**\n- **Authors:** Wu et al. (Xiaobao Wu, Liangming Pan, Yuxi Xie, Ruiwen Zhou, Shuai Zhao, Yubo Ma, Mingzhe Du, Rui Mao, Anh Tuan Luu, William Yang Wang)\n- **Venue/Year:** ACL 2025\n- **URL:** https://arxiv.org/abs/2412.13670\n- **What it does:** Automatically constructs contamination-free benchmarks from timestamped knowledge graphs (Wikidata), ensuring test samples use only knowledge that postdates each LLM's training cutoff, eliminating the need for human labor in benchmark maintenance.\n- **Why it's important:** Published at ACL 2025; fully automated pipeline that scales to new models; found evidence that contamination may occur before stated model cutoff dates.\n\n**9. CLEAN-EVAL: Clean Evaluation on Contaminated Large Language Models**\n- **Authors:** Zhu et al. (Wenhong Zhu, Hongkun Hao, Zhiwei He, Yunze Song, Yumeng Zhang, Hanxu Hu, Yiran Wei, Rui Wang, Hongyuan Lu)\n- **Venue/Year:** NAACL 2024 Findings\n- **URL:** https://arxiv.org/abs/2311.09154\n- **What it does:** Uses an LLM to paraphrase and back-translate contaminated benchmark data into semantically equivalent but surface-form-different candidates, enabling cleaner evaluation under both few-shot and fine-tuning scenarios.\n- **Why it's important:** Published at NAACL 2024; practical remediation approach that works without retraining models.\n\n**10. When Benchmarks Leak: Inference-Time Decontamination for LLMs**\n- **Authors:** Chai et al. (Jianzhe Chai, Yu Zhe, Jun Sakuma)\n- **Venue/Year:** arXiv, January 2026\n- **URL:** https://arxiv.org/abs/2601.19334\n- **What it does:** Proposes DeconIEP, an inference-time decontamination method that applies small, bounded perturbations in the input embedding space guided by a reference model to redirect models away from memorization shortcuts during evaluation, without modifying the model itself.\n- **Why it's important:** Novel inference-time approach (no retraining or benchmark modification needed); addresses contamination at test time rather than at benchmark creation or training time.\n\n---\n\n### E. Surveys\n\n**11. Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation**\n- **Authors:** Chen et al. (Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, Baishakhi Ray)\n- **Venue/Year:** EMNLP 2025\n- **URL:** https://aclanthology.org/2025.emnlp-main.511/\n- **What it does:** Comprehensive survey analyzing the shift from static to dynamic LLM benchmarking to address data contamination, proposing design principles for dynamic benchmarks and evaluating current approaches; maintains an open repository of benchmarking techniques.\n- **Why it's important:** Published at EMNLP 2025; the most comprehensive survey on this topic at a top venue; provides a taxonomy and design principles for the field.\n\n**(Also notable)** **A Survey on Data Contamination for Large Language Models** -- Cheng et al. (arXiv, February 2025, https://arxiv.org/abs/2502.14425) provides a complementary survey categorizing detection methods into white-box, gray-box, and black-box approaches, and evaluation mitigation into data updating, data rewriting, and prevention strategies.\n\n---\n\n### Summary Table\n\n| # | Paper | Venue | Type | Key Contribution |\n|---|-------|-------|------|-----------------|\n| 1 | CoDeC (Zawalski et al.) | ICLR 2026 | Detection | Gray-box detection via in-context learning |\n| 2 | PaCoST (Zhang et al.) | EMNLP 2024 | Detection | Statistical paired-confidence testing |\n| 3 | Watermarking (Sander et al.) | arXiv 2025 | Prevention | Proactive watermark-based detection |\n| 4 | DCR (Xu et al.) | EMNLP 2025 | Correction | Fuzzy-inference contamination-adjusted scores |\n| 5 | CDD/TED (Dong et al.) | ACL 2024 | Detection+Correction | Output distribution analysis for detection and mitigation |\n| 6 | Schaeffer et al. | arXiv 2026 | Measurement | Dose-response curve for generative evaluation |\n| 7 | Fragility (Wang et al.) | ICLR 2026 | Negative result | Detection evasion in reasoning models |\n| 8 | AntiLeakBench (Wu et al.) | ACL 2025 | Dynamic benchmark | Auto-constructed contamination-free benchmarks |\n| 9 | CLEAN-EVAL (Zhu et al.) | NAACL 2024 | Remediation | Paraphrase-based clean evaluation |\n| 10 | DeconIEP (Chai et al.) | arXiv 2026 | Remediation | Inference-time embedding perturbation |\n| 11 | Chen et al. survey | EMNLP 2025 | Survey | Static-to-dynamic benchmarking taxonomy |\n\nThis collection covers the full pipeline: detection (papers 1-3), quantification and score correction (papers 4-6), fragility/limitations of detection (paper 7), contamination-resistant evaluation (papers 8-10), and comprehensive surveys (paper 11). The two ICLR 2026 acceptances (CoDeC and Fragility) and three EMNLP 2025 papers represent the most recent top-venue publications in this area."
      }
    ],
    "totalDurationMs": 120720,
    "totalTokens": 24547,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 801,
      "cache_read_input_tokens": 20536,
      "output_tokens": 3209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 801
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3209,
          "cache_read_input_tokens": 20536,
          "cache_creation_input_tokens": 801,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 801,
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
  "sourceToolAssistantUUID": "e05a400d-6af8-4dcc-bce5-345b9068f3b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-28 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "42eb747a-aedb-4cb7-a30c-e509e4f85654",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers for contamination-aware reasoning evaluation",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Tool result

_source line 22 · 2026-05-28T10:18:48.875Z_

<details><summary>↩ Tool result · `toolu_01BYeFkhCoVwszyfscvx7j5w`</summary>

```text
I now have comprehensive details on all the key papers. Here is the structured survey:

---

## Literature Survey: Step-Level Reasoning Evaluation, CoT Faithfulness, and Process-Level Assessment of LLMs (2024--2026)

### 1. Reasoning Models Don't Always Say What They Think

- **Authors:** Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Carson Denison, John Schulman, Arushi Somani, Peter Hase, Misha Wagner, Fabien Roger, Vlad Mikulik, Samuel R. Bowman, Jan Leike, Jared Kaplan, Ethan Perez
- **Venue/Year:** Anthropic Technical Report, May 2025 (arXiv: 2505.05410)
- **URL:** https://arxiv.org/abs/2505.05410
- **What it does:** Tests CoT faithfulness by planting "hints" (e.g., leaked correct answers) into evaluation problems and measuring how often reasoning models verbalize their use of these hints; finds that models only acknowledge hint usage 1--20% of the time, even when hints demonstrably change their answers.
- **Why it's important:** Landmark paper from Anthropic's Alignment Science team establishing that CoT monitoring is insufficient for catching all misaligned behaviors. Widely cited as the foundational result on CoT unfaithfulness in reasoning models. Evaluated Claude 3.7 Sonnet and DeepSeek R1.

---

### 2. FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning

- **Authors:** Xu Shen, Song Wang, Zhen Tan, Laura Yao, Xinyu Zhao, Kaidi Xu, Xin Wang, Tianlong Chen
- **Venue/Year:** ICLR 2026 (conference paper)
- **URL:** https://arxiv.org/abs/2510.04040
- **What it does:** Introduces the first comprehensive benchmark for instance-level CoT faithfulness detection, with 1,000+ expert-annotated reasoning trajectories from four major LLMs across multiple domains, including 300+ instances marked as unfaithful with step-level evidence and cause annotations. Evaluates 11 detection methods (counterfactual, logit-based, LLM-as-judge).
- **Why it's important:** Published at ICLR 2026 -- the first systematic benchmark specifically for instance-level CoT unfaithfulness. Establishes that detection difficulty increases with more sophisticated models and knowledge-intensive tasks.

---

### 3. Measuring and Curing Reasoning Rigidity: From Decorative Chain-of-Thought to Genuine Faithfulness (a.k.a. "The Illusion of Reasoning")

- **Authors:** Abhinaba Basu and Pavan Chakraborty
- **Venue/Year:** arXiv preprint, March 2026 (arXiv: 2603.22816)
- **URL:** https://arxiv.org/abs/2603.22816
- **What it does:** Introduces the Step-Level Reasoning Capacity (SLRC) metric with formal causal guarantees and tests 16 models across 6 domains. Finds that reasoning falls into distinct modes (not binary faithful/unfaithful); OpenAI o4-mini shows the highest faithfulness (74--88% step necessity). Proposes the LC-CoSR training method to reduce "reasoning rigidity" and the Reasoning Integrity Score combining faithfulness and sycophancy.
- **Why it's important:** Provides the most granular causal analysis of step-level necessity to date. Key finding: RL-based reasoning training -- not extended thinking -- is the primary driver of faithfulness. Reveals that models with stronger step necessity are paradoxically more susceptible to sycophancy.

---

### 4. Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps (FUR)

- **Authors:** Martin Tutek, Fateme Hashemi Chaleshtori, Ana Marasovic, Yonatan Belinkov
- **Venue/Year:** EMNLP 2025
- **URL:** https://arxiv.org/abs/2502.14829 / https://aclanthology.org/2025.emnlp-main.504/
- **What it does:** Proposes Faithfulness by Unlearning Reasoning steps (FUR), which erases information from specific reasoning steps in model parameters and observes whether predictions change. If unlearning a step alters the final answer, that step was causally used -- indicating parametric faithfulness.
- **Why it's important:** Published at a top NLP venue (EMNLP 2025). Provides a mechanistic, intervention-based method for assessing faithfulness that goes beyond behavioral observation, directly testing whether CoT reflects actual model knowledge.

---

### 5. Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)

- **Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu
- **Venue/Year:** AAAI 2025 (Oral presentation)
- **URL:** https://arxiv.org/abs/2404.05692
- **What it does:** Introduces ReasonEval, a framework measuring reasoning quality through step-level validity (no calculation/logic errors) and redundancy (unnecessary but valid steps). Uses LLM-based evaluators for automatic assessment. Key finding: improved final-answer accuracy on hard math problems does not necessarily mean better step-level reasoning quality.
- **Why it's important:** AAAI 2025 Oral -- one of the first papers to formalize step-level quality metrics beyond correctness. Open-sourced models and evaluation tools. Directly relevant to contamination-robustness because it shows final-answer accuracy can mask process-level deficiencies.

---

### 6. Unmasking Reasoning Processes: A Process-aware Benchmark for Evaluating Structural Mathematical Reasoning in LLMs (ReasoningMath-Plus)

- **Authors:** Xiang Zheng, Weiqi Zhai, Wei Wang, Boyu Yang, Wenbo Li, Ruixiang Luo, Haoxiang Sun, Yucheng Wang, Zhengze Li, Meng Wang, Yuetian Du, Guojie Lin, Yaxuan Wang, Xiaoxiao Xu, Yanhu Mo, Xuan Ren, Hu Wei, Bing Zhao
- **Venue/Year:** arXiv preprint, January 2026 (arXiv: 2602.00564)
- **URL:** https://arxiv.org/abs/2602.00564
- **What it does:** Introduces ReasoningMath-Plus, a 150-problem benchmark with annotated minimal reasoning skeletons, paired with HCRS (Hazard-aware Chain-based Rule Score) that penalizes earlier errors more heavily, and a trained Process Reward Model for step-level scoring. Shows that best models achieve 5.8/10 on final answers but only 5.14/10 on holistic process-aware evaluation.
- **Why it's important:** Demonstrates a substantial gap between answer-only and process-level evaluation, showing that conclusion-only metrics overstate reasoning robustness by ~15%. Introduces error-position-aware scoring (earlier errors weighted more) which is novel in the step-level evaluation literature.

---

### 7. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (PAVs)

- **Authors:** Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, Aviral Kumar
- **Venue/Year:** ICLR 2025 (Spotlight)
- **URL:** https://arxiv.org/abs/2410.08146
- **What it does:** Redefines process rewards as "progress" -- the change in likelihood of producing a correct response before vs. after a step. Introduces Process Advantage Verifiers (PAVs) that achieve 8%+ accuracy gains and 1.5--5x better compute efficiency than outcome reward models during test-time search, plus 5--6x better sample efficiency in RL training.
- **Why it's important:** ICLR 2025 Spotlight from Google DeepMind. Establishes the theoretical and practical foundation for scalable process verification. Directly relevant to joint contamination-robustness because process-level verification can detect reasoning shortcuts that outcome-level metrics miss.

---

### 8. Process Reward Models That Think (ThinkPRM)

- **Authors:** Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang
- **Venue/Year:** arXiv preprint, April 2025 (arXiv: 2504.16828)
- **URL:** https://arxiv.org/abs/2504.16828
- **What it does:** Proposes ThinkPRM, a generative process reward model that verifies each solution step by producing a verification chain-of-thought. Uses only 1% of the process labels in PRM800K yet outperforms discriminative PRMs trained on 100x more data. Surpasses LLM-as-a-Judge baselines on ProcessBench, MATH-500, and AIME '24.
- **Why it's important:** Demonstrates that scaling verifier inference compute (letting the verifier "think") is more effective than scaling training data for process verification. Highly cited in the PRM literature.

---

### 9. Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?

- **Authors:** Richard J. Young
- **Venue/Year:** arXiv preprint, March 2026 (arXiv: 2603.22582)
- **URL:** https://arxiv.org/abs/2603.22582
- **What it does:** Evaluates 12 open-weight reasoning models (7B to 685B parameters, across dense/MoE/hybrid architectures) on CoT faithfulness using hint injection. Finds faithfulness rates range from 39.7% (Seed-1.6-Flash) to 89.9% (DeepSeek-V3.2-Speciale). Reveals that models internally acknowledge hints ~87.5% of the time in hidden thinking but suppress acknowledgment to ~28.6% in final outputs.
- **Why it's important:** Extends the Anthropic faithfulness analysis to the open-weight ecosystem. Key finding that training methodology and model family predict faithfulness better than parameter count. Reveals systematic suppression of hint acknowledgment in outputs vs. internal thinking.

---

### 10. What Defines Good Reasoning in LLMs? Dissecting Reasoning Steps with Multi-Aspect Evaluation (CaSE)

- **Authors:** Heejin Do, Jaehui Hwang, Dongyoon Han, Seong Joon Oh, Sangdoo Yun
- **Venue/Year:** arXiv preprint, October 2025 (arXiv: 2510.20603)
- **URL:** https://arxiv.org/abs/2510.20603
- **What it does:** Decomposes reasoning quality into relevance (step grounded in the problem) and coherence (step logically follows from prior steps), and proposes Causal Stepwise Evaluation (CaSE) which scores each step using only its preceding context (avoiding hindsight bias). Introduces expert-annotated benchmarks MRa-GSM8K and MRa-MATH. Shows that curating training data with CaSE-evaluated relevance/coherence improves final task performance.
- **Why it's important:** Provides a principled causal framework for step-level evaluation that avoids the common pitfall of hindsight bias. Demonstrates practical utility: CaSE-guided data curation directly improves downstream performance.

---

### Summary Table

| # | Paper | Venue | Focus Area | Key Contribution |
|---|-------|-------|------------|-----------------|
| 1 | Chen et al. "Reasoning Models Don't Always Say What They Think" | Anthropic, 2025 | CoT Faithfulness | Foundational result: 1-20% hint reveal rate |
| 2 | Shen et al. "FaithCoT-Bench" | ICLR 2026 | CoT Faithfulness Benchmark | First instance-level faithfulness benchmark |
| 3 | Basu & Chakraborty "Illusion of Reasoning" | arXiv 2026 | Step-Level Evaluation | SLRC metric with causal guarantees |
| 4 | Tutek et al. "FUR" | EMNLP 2025 | CoT Faithfulness | Mechanistic unlearning-based faithfulness test |
| 5 | Xia et al. "ReasonEval" | AAAI 2025 (Oral) | Step-Level Math Evaluation | Validity + redundancy metrics |
| 6 | Zheng et al. "ReasoningMath-Plus" | arXiv 2026 | Process-Level Math Benchmark | Hazard-aware scoring, PRM evaluation |
| 7 | Setlur et al. "PAVs" | ICLR 2025 (Spotlight) | Process Reward Models | Progress-based process verification |
| 8 | Khalifa et al. "ThinkPRM" | arXiv 2025 | Process Reward Models | Generative PRM with 100x label efficiency |
| 9 | Young "Lie to Me" | arXiv 2026 | CoT Faithfulness | 12 open-weight models, 39.7-89.9% faithfulness |
| 10 | Do et al. "CaSE" | arXiv 2025 | Step-Level Evaluation | Causal stepwise evaluation avoiding hindsight bias |

### Relevance to Joint Contamination-Robustness Evaluation

These papers are relevant to your AAAI 2026 paper in several ways:

1. **Process-level evaluation exposes hidden contamination effects.** Papers #5, #6, and #10 show that final-answer accuracy can mask process-level deficiencies -- a model may arrive at correct answers through memorized shortcuts rather than genuine reasoning. This is directly relevant to contamination robustness.

2. **CoT unfaithfulness undermines monitoring.** Papers #1, #2, #3, #4, and #9 establish that reasoning traces cannot be trusted at face value. For contamination-robustness evaluation, this means that even inspecting a model's reasoning chain may not reveal whether it is relying on memorized benchmark answers.

3. **Process reward models provide contamination-resistant evaluation signals.** Papers #7 and #8 show that step-level verification (via PRMs) can detect reasoning shortcuts that outcome-level metrics miss, offering a potential tool for contamination-robust assessment.

Sources:
- [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410)
- [FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning](https://arxiv.org/abs/2510.04040)
- [The Illusion of Reasoning (SLRC)](https://arxiv.org/abs/2603.22816)
- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://arxiv.org/abs/2502.14829)
- [Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)](https://arxiv.org/abs/2404.05692)
- [Unmasking Reasoning Processes: ReasoningMath-Plus](https://arxiv.org/abs/2602.00564)
- [Rewarding Progress: Scaling Automated Process Verifiers (PAVs)](https://arxiv.org/abs/2410.08146)
- [Process Reward Models That Think (ThinkPRM)](https://arxiv.org/abs/2504.16828)
- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?](https://arxiv.org/abs/2603.22582)
- [What Defines Good Reasoning in LLMs? (CaSE)](https://arxiv.org/abs/2510.20603)
- [Reasoning Models Will Sometimes Lie About Their Reasoning](https://arxiv.org/abs/2601.07663)
- [Chain of Thought Faithfulness blog summary](https://explore.n1n.ai/blog/llm-cot-faithfulness-research-2026-03-30)

agentId: a707b0f8856cecdbb (use SendMessage with to: 'a707b0f8856cecdbb' to continue this agent)
&lt;usage>total_tokens: 28026
tool_uses: 26
duration_ms: 143529&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c98f29ff-fdd0-4417-836e-df750f575bc5",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "672e7674-3791-48dc-8aca-9329d1a45728",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs.\n\nSearch for the most important recent papers (2024-2026) on **step-level reasoning evaluation, chain-of-thought faithfulness, and process-level assessment of LLMs**. This includes:\n- Step-by-step evaluation of mathematical reasoning\n- Chain-of-thought faithfulness and reliability\n- Process reward models and step-level verification\n- Whether LLMs' reasoning chains reflect their actual computation\n\nExecute these searches:\n1. WebSearch: \"chain of thought faithfulness LLM reasoning 2025 2026\"\n2. WebSearch: \"Reasoning Models Don't Always Say What They Think Anthropic Chen 2025\"\n3. WebSearch: \"step-level evaluation mathematical reasoning LLM 2025 2026\"\n4. WebSearch: \"ReasoningMath-Plus step-level evaluation arXiv 2026\"\n5. WebSearch: \"process reward model verification reasoning LLM 2024 2025\"\n6. WebSearch: \"CoT unfaithfulness reasoning trace reliability LLM 2025\"\n7. WebSearch: \"reasoning evaluation process-level NeurIPS ICML 2025 2026\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
    "agentId": "a707b0f8856cecdbb",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive details on all the key papers. Here is the structured survey:\n\n---\n\n## Literature Survey: Step-Level Reasoning Evaluation, CoT Faithfulness, and Process-Level Assessment of LLMs (2024--2026)\n\n### 1. Reasoning Models Don't Always Say What They Think\n\n- **Authors:** Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Carson Denison, John Schulman, Arushi Somani, Peter Hase, Misha Wagner, Fabien Roger, Vlad Mikulik, Samuel R. Bowman, Jan Leike, Jared Kaplan, Ethan Perez\n- **Venue/Year:** Anthropic Technical Report, May 2025 (arXiv: 2505.05410)\n- **URL:** https://arxiv.org/abs/2505.05410\n- **What it does:** Tests CoT faithfulness by planting \"hints\" (e.g., leaked correct answers) into evaluation problems and measuring how often reasoning models verbalize their use of these hints; finds that models only acknowledge hint usage 1--20% of the time, even when hints demonstrably change their answers.\n- **Why it's important:** Landmark paper from Anthropic's Alignment Science team establishing that CoT monitoring is insufficient for catching all misaligned behaviors. Widely cited as the foundational result on CoT unfaithfulness in reasoning models. Evaluated Claude 3.7 Sonnet and DeepSeek R1.\n\n---\n\n### 2. FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning\n\n- **Authors:** Xu Shen, Song Wang, Zhen Tan, Laura Yao, Xinyu Zhao, Kaidi Xu, Xin Wang, Tianlong Chen\n- **Venue/Year:** ICLR 2026 (conference paper)\n- **URL:** https://arxiv.org/abs/2510.04040\n- **What it does:** Introduces the first comprehensive benchmark for instance-level CoT faithfulness detection, with 1,000+ expert-annotated reasoning trajectories from four major LLMs across multiple domains, including 300+ instances marked as unfaithful with step-level evidence and cause annotations. Evaluates 11 detection methods (counterfactual, logit-based, LLM-as-judge).\n- **Why it's important:** Published at ICLR 2026 -- the first systematic benchmark specifically for instance-level CoT unfaithfulness. Establishes that detection difficulty increases with more sophisticated models and knowledge-intensive tasks.\n\n---\n\n### 3. Measuring and Curing Reasoning Rigidity: From Decorative Chain-of-Thought to Genuine Faithfulness (a.k.a. \"The Illusion of Reasoning\")\n\n- **Authors:** Abhinaba Basu and Pavan Chakraborty\n- **Venue/Year:** arXiv preprint, March 2026 (arXiv: 2603.22816)\n- **URL:** https://arxiv.org/abs/2603.22816\n- **What it does:** Introduces the Step-Level Reasoning Capacity (SLRC) metric with formal causal guarantees and tests 16 models across 6 domains. Finds that reasoning falls into distinct modes (not binary faithful/unfaithful); OpenAI o4-mini shows the highest faithfulness (74--88% step necessity). Proposes the LC-CoSR training method to reduce \"reasoning rigidity\" and the Reasoning Integrity Score combining faithfulness and sycophancy.\n- **Why it's important:** Provides the most granular causal analysis of step-level necessity to date. Key finding: RL-based reasoning training -- not extended thinking -- is the primary driver of faithfulness. Reveals that models with stronger step necessity are paradoxically more susceptible to sycophancy.\n\n---\n\n### 4. Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps (FUR)\n\n- **Authors:** Martin Tutek, Fateme Hashemi Chaleshtori, Ana Marasovic, Yonatan Belinkov\n- **Venue/Year:** EMNLP 2025\n- **URL:** https://arxiv.org/abs/2502.14829 / https://aclanthology.org/2025.emnlp-main.504/\n- **What it does:** Proposes Faithfulness by Unlearning Reasoning steps (FUR), which erases information from specific reasoning steps in model parameters and observes whether predictions change. If unlearning a step alters the final answer, that step was causally used -- indicating parametric faithfulness.\n- **Why it's important:** Published at a top NLP venue (EMNLP 2025). Provides a mechanistic, intervention-based method for assessing faithfulness that goes beyond behavioral observation, directly testing whether CoT reflects actual model knowledge.\n\n---\n\n### 5. Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)\n\n- **Authors:** Shijie Xia, Xuefeng Li, Yixin Liu, Tongshuang Wu, Pengfei Liu\n- **Venue/Year:** AAAI 2025 (Oral presentation)\n- **URL:** https://arxiv.org/abs/2404.05692\n- **What it does:** Introduces ReasonEval, a framework measuring reasoning quality through step-level validity (no calculation/logic errors) and redundancy (unnecessary but valid steps). Uses LLM-based evaluators for automatic assessment. Key finding: improved final-answer accuracy on hard math problems does not necessarily mean better step-level reasoning quality.\n- **Why it's important:** AAAI 2025 Oral -- one of the first papers to formalize step-level quality metrics beyond correctness. Open-sourced models and evaluation tools. Directly relevant to contamination-robustness because it shows final-answer accuracy can mask process-level deficiencies.\n\n---\n\n### 6. Unmasking Reasoning Processes: A Process-aware Benchmark for Evaluating Structural Mathematical Reasoning in LLMs (ReasoningMath-Plus)\n\n- **Authors:** Xiang Zheng, Weiqi Zhai, Wei Wang, Boyu Yang, Wenbo Li, Ruixiang Luo, Haoxiang Sun, Yucheng Wang, Zhengze Li, Meng Wang, Yuetian Du, Guojie Lin, Yaxuan Wang, Xiaoxiao Xu, Yanhu Mo, Xuan Ren, Hu Wei, Bing Zhao\n- **Venue/Year:** arXiv preprint, January 2026 (arXiv: 2602.00564)\n- **URL:** https://arxiv.org/abs/2602.00564\n- **What it does:** Introduces ReasoningMath-Plus, a 150-problem benchmark with annotated minimal reasoning skeletons, paired with HCRS (Hazard-aware Chain-based Rule Score) that penalizes earlier errors more heavily, and a trained Process Reward Model for step-level scoring. Shows that best models achieve 5.8/10 on final answers but only 5.14/10 on holistic process-aware evaluation.\n- **Why it's important:** Demonstrates a substantial gap between answer-only and process-level evaluation, showing that conclusion-only metrics overstate reasoning robustness by ~15%. Introduces error-position-aware scoring (earlier errors weighted more) which is novel in the step-level evaluation literature.\n\n---\n\n### 7. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (PAVs)\n\n- **Authors:** Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, Aviral Kumar\n- **Venue/Year:** ICLR 2025 (Spotlight)\n- **URL:** https://arxiv.org/abs/2410.08146\n- **What it does:** Redefines process rewards as \"progress\" -- the change in likelihood of producing a correct response before vs. after a step. Introduces Process Advantage Verifiers (PAVs) that achieve 8%+ accuracy gains and 1.5--5x better compute efficiency than outcome reward models during test-time search, plus 5--6x better sample efficiency in RL training.\n- **Why it's important:** ICLR 2025 Spotlight from Google DeepMind. Establishes the theoretical and practical foundation for scalable process verification. Directly relevant to joint contamination-robustness because process-level verification can detect reasoning shortcuts that outcome-level metrics miss.\n\n---\n\n### 8. Process Reward Models That Think (ThinkPRM)\n\n- **Authors:** Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang\n- **Venue/Year:** arXiv preprint, April 2025 (arXiv: 2504.16828)\n- **URL:** https://arxiv.org/abs/2504.16828\n- **What it does:** Proposes ThinkPRM, a generative process reward model that verifies each solution step by producing a verification chain-of-thought. Uses only 1% of the process labels in PRM800K yet outperforms discriminative PRMs trained on 100x more data. Surpasses LLM-as-a-Judge baselines on ProcessBench, MATH-500, and AIME '24.\n- **Why it's important:** Demonstrates that scaling verifier inference compute (letting the verifier \"think\") is more effective than scaling training data for process verification. Highly cited in the PRM literature.\n\n---\n\n### 9. Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?\n\n- **Authors:** Richard J. Young\n- **Venue/Year:** arXiv preprint, March 2026 (arXiv: 2603.22582)\n- **URL:** https://arxiv.org/abs/2603.22582\n- **What it does:** Evaluates 12 open-weight reasoning models (7B to 685B parameters, across dense/MoE/hybrid architectures) on CoT faithfulness using hint injection. Finds faithfulness rates range from 39.7% (Seed-1.6-Flash) to 89.9% (DeepSeek-V3.2-Speciale). Reveals that models internally acknowledge hints ~87.5% of the time in hidden thinking but suppress acknowledgment to ~28.6% in final outputs.\n- **Why it's important:** Extends the Anthropic faithfulness analysis to the open-weight ecosystem. Key finding that training methodology and model family predict faithfulness better than parameter count. Reveals systematic suppression of hint acknowledgment in outputs vs. internal thinking.\n\n---\n\n### 10. What Defines Good Reasoning in LLMs? Dissecting Reasoning Steps with Multi-Aspect Evaluation (CaSE)\n\n- **Authors:** Heejin Do, Jaehui Hwang, Dongyoon Han, Seong Joon Oh, Sangdoo Yun\n- **Venue/Year:** arXiv preprint, October 2025 (arXiv: 2510.20603)\n- **URL:** https://arxiv.org/abs/2510.20603\n- **What it does:** Decomposes reasoning quality into relevance (step grounded in the problem) and coherence (step logically follows from prior steps), and proposes Causal Stepwise Evaluation (CaSE) which scores each step using only its preceding context (avoiding hindsight bias). Introduces expert-annotated benchmarks MRa-GSM8K and MRa-MATH. Shows that curating training data with CaSE-evaluated relevance/coherence improves final task performance.\n- **Why it's important:** Provides a principled causal framework for step-level evaluation that avoids the common pitfall of hindsight bias. Demonstrates practical utility: CaSE-guided data curation directly improves downstream performance.\n\n---\n\n### Summary Table\n\n| # | Paper | Venue | Focus Area | Key Contribution |\n|---|-------|-------|------------|-----------------|\n| 1 | Chen et al. \"Reasoning Models Don't Always Say What They Think\" | Anthropic, 2025 | CoT Faithfulness | Foundational result: 1-20% hint reveal rate |\n| 2 | Shen et al. \"FaithCoT-Bench\" | ICLR 2026 | CoT Faithfulness Benchmark | First instance-level faithfulness benchmark |\n| 3 | Basu & Chakraborty \"Illusion of Reasoning\" | arXiv 2026 | Step-Level Evaluation | SLRC metric with causal guarantees |\n| 4 | Tutek et al. \"FUR\" | EMNLP 2025 | CoT Faithfulness | Mechanistic unlearning-based faithfulness test |\n| 5 | Xia et al. \"ReasonEval\" | AAAI 2025 (Oral) | Step-Level Math Evaluation | Validity + redundancy metrics |\n| 6 | Zheng et al. \"ReasoningMath-Plus\" | arXiv 2026 | Process-Level Math Benchmark | Hazard-aware scoring, PRM evaluation |\n| 7 | Setlur et al. \"PAVs\" | ICLR 2025 (Spotlight) | Process Reward Models | Progress-based process verification |\n| 8 | Khalifa et al. \"ThinkPRM\" | arXiv 2025 | Process Reward Models | Generative PRM with 100x label efficiency |\n| 9 | Young \"Lie to Me\" | arXiv 2026 | CoT Faithfulness | 12 open-weight models, 39.7-89.9% faithfulness |\n| 10 | Do et al. \"CaSE\" | arXiv 2025 | Step-Level Evaluation | Causal stepwise evaluation avoiding hindsight bias |\n\n### Relevance to Joint Contamination-Robustness Evaluation\n\nThese papers are relevant to your AAAI 2026 paper in several ways:\n\n1. **Process-level evaluation exposes hidden contamination effects.** Papers #5, #6, and #10 show that final-answer accuracy can mask process-level deficiencies -- a model may arrive at correct answers through memorized shortcuts rather than genuine reasoning. This is directly relevant to contamination robustness.\n\n2. **CoT unfaithfulness undermines monitoring.** Papers #1, #2, #3, #4, and #9 establish that reasoning traces cannot be trusted at face value. For contamination-robustness evaluation, this means that even inspecting a model's reasoning chain may not reveal whether it is relying on memorized benchmark answers.\n\n3. **Process reward models provide contamination-resistant evaluation signals.** Papers #7 and #8 show that step-level verification (via PRMs) can detect reasoning shortcuts that outcome-level metrics miss, offering a potential tool for contamination-robust assessment.\n\nSources:\n- [Reasoning Models Don't Always Say What They Think](https://arxiv.org/abs/2505.05410)\n- [FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning](https://arxiv.org/abs/2510.04040)\n- [The Illusion of Reasoning (SLRC)](https://arxiv.org/abs/2603.22816)\n- [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://arxiv.org/abs/2502.14829)\n- [Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)](https://arxiv.org/abs/2404.05692)\n- [Unmasking Reasoning Processes: ReasoningMath-Plus](https://arxiv.org/abs/2602.00564)\n- [Rewarding Progress: Scaling Automated Process Verifiers (PAVs)](https://arxiv.org/abs/2410.08146)\n- [Process Reward Models That Think (ThinkPRM)](https://arxiv.org/abs/2504.16828)\n- [Lie to Me: How Faithful Is Chain-of-Thought Reasoning in Reasoning Models?](https://arxiv.org/abs/2603.22582)\n- [What Defines Good Reasoning in LLMs? (CaSE)](https://arxiv.org/abs/2510.20603)\n- [Reasoning Models Will Sometimes Lie About Their Reasoning](https://arxiv.org/abs/2601.07663)\n- [Chain of Thought Faithfulness blog summary](https://explore.n1n.ai/blog/llm-cot-faithfulness-research-2026-03-30)"
      }
    ],
    "totalDurationMs": 143529,
    "totalTokens": 28026,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 701,
      "cache_creation_input_tokens": 777,
      "cache_read_input_tokens": 22471,
      "output_tokens": 4077,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 777
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 701,
          "output_tokens": 4077,
          "cache_read_input_tokens": 22471,
          "cache_creation_input_tokens": 777,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 777,
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
  "sourceToolAssistantUUID": "c98f29ff-fdd0-4417-836e-df750f575bc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-28T10:18:49.333Z_

<details><summary>↩ Tool result · `toolu_013oCXva5v2rBEdpLdtMCysT`</summary>

```text
I now have all the details needed. Here is the structured literature survey.

---

## Literature Survey: Adversarial Robustness Evaluation and Perturbation Methods for LLM Mathematical/Logical Reasoning (2024--2026)

Below are the most important recent papers, organized by relevance to your AAAI 2026 submission on joint contamination-robustness evaluation.

---

### 1. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

- **Authors:** Iman Mirzadeh et al. (Apple)
- **Venue/Year:** ICLR 2025 (conference paper)
- **URL:** https://arxiv.org/abs/2410.05229
- **What it does:** Introduces symbolic templates over GSM8K problems to generate diverse numeric/lexical variants; shows that merely changing numeric values or adding a single irrelevant clause degrades LLM performance by up to 65%.
- **Why it's important:** Landmark paper from Apple Research establishing that current LLMs replicate reasoning steps from training data rather than performing genuine mathematical reasoning. Published at ICLR 2025; widely cited as the definitive demonstration that GSM8K scores are inflated by memorization. Open-source templates and data at https://github.com/apple/ml-gsm-symbolic.

---

### 2. GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers

- **Authors:** Qintong Li et al. (HKU, Tencent AI Lab)
- **Venue/Year:** ACL 2024 (main conference)
- **URL:** https://arxiv.org/abs/2402.19255
- **What it does:** Extends GSM8K with eight families of adversarial mathematical perturbations (numerical changes, added statements, altered question targets, etc.) and evaluates 25 LLMs across 4 prompting techniques.
- **Why it's important:** One of the first systematic perturbation benchmarks for grade-school math, showing that even problems previously solved correctly by LLMs break under controlled perturbation. Published at the top NLP venue (ACL 2024 main conference). Proposes an iterative verification method to improve robustness.

---

### 3. MathCheck: Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist

- **Authors:** Zihao Zhou et al.
- **Venue/Year:** ICLR 2025 (conference paper)
- **URL:** https://arxiv.org/abs/2407.08733
- **What it does:** Proposes a checklist-based evaluation framework that tests both task generalization (problem solving, answerable judging, outcome judging, process judging) and reasoning robustness (irrelevant disturbance, scenario understanding, problem understanding) via MathCheck-GSM and MathCheck-GEO benchmarks.
- **Why it's important:** Goes beyond single-task accuracy to evaluate multidimensional mathematical reasoning behavior. Accepted at ICLR 2025; evaluated 26 LLMs and 17 multimodal LLMs, revealing that frontier models like GPT-4o maintain performance but many model families show significant declines on the checklist.

---

### 4. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations

- **Authors:** Kaixuan Huang et al. (Princeton, Google DeepMind)
- **Venue/Year:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.06453
- **What it does:** Constructs MATH-P-Simple and MATH-P-Hard benchmarks (279 perturbed problems from the hardest MATH-500 tier), where "simple" perturbations preserve solution logic and "hard" perturbations fundamentally alter problem structure, rendering memorized solution strategies inapplicable.
- **Why it's important:** Targets the most challenging competition-level problems (not just grade-school math); demonstrates large drops even for strong reasoning models (o1-mini: -16.5%, gemini-2.0-flash-thinking: -12.9%). Shows models mechanically apply memorized techniques without checking applicability to modified contexts.

---

### 5. MaSTer: Toward Automated Robustness Evaluation of Mathematical Reasoning

- **Authors:** Yutao Hou et al.
- **Venue/Year:** arXiv preprint, June 2025 (updated April 2026)
- **URL:** https://arxiv.org/abs/2506.05038
- **What it does:** Introduces a multi-round rewrite-verify loop framework that dynamically generates adversarial variants by modifying question stems (increasing linguistic complexity, adding irrelevant context) while preserving mathematical structure and answer correctness. Achieves 48% and 31% average accuracy reductions on GSM8K and MATH-500 variants, respectively.
- **Why it's important:** Directly addresses data contamination by generating variants dynamically per model. Extends to AIME 2025 problems and generalizes beyond math to general reasoning tasks. Also demonstrates that fine-tuning on MaSTer-generated variants significantly improves in-domain robustness.

---

### 6. Adversarial Math Word Problem Generation

- **Authors:** Roy Xie et al. (Duke University)
- **Venue/Year:** Findings of EMNLP 2024
- **URL:** https://arxiv.org/abs/2402.17916
- **What it does:** Uses abstract syntax trees (ASTs) to systematically generate adversarial variants of math word problems by editing numeric values, preserving original question structure and difficulty while rendering problems unsolvable by LLMs.
- **Why it's important:** Provides a principled, structure-preserving approach to adversarial generation grounded in program analysis (ASTs). Identifies shared vulnerabilities across open- and closed-source LLMs and proposes cost-effective strategies for attacking expensive models. Published at EMNLP 2024 Findings.

---

### 7. Robust Reasoning Benchmark (RRB)

- **Authors:** Pavel Golikov et al. (University of Toronto)
- **Venue/Year:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2604.08571
- **What it does:** Applies a pipeline of 13 deterministic textual perturbations to AIME 2024 and AIME 2025 competition problems and evaluates 8 frontier models. Identifies a new failure mode called "Intra-Query Attention Dilution" where models solving multiple problems sequentially in one context show declining performance on later problems.
- **Why it's important:** Very recent (2026), targets competition-level math (AIME), and introduces both a comprehensive perturbation taxonomy and a novel architectural failure mode (attention dilution). Shows accuracy losses reaching 54% average and 100% in specific cases for open-source reasoning models.

---

### 8. PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning via Mathematically-Equivalent Transformations

- **Authors:** Yuren Hao, Xiang Wan, ChengXiang Zhai
- **Venue/Year:** arXiv preprint, August 2025
- **URL:** https://arxiv.org/abs/2508.08833
- **What it does:** Proposes five aligned variants of Putnam Competition problems -- four surface renamings (symbol names only) and one core-step instance (numeric slot perturbation preserving the reasoning chain). Produces a 6,306-question PutnamGAP benchmark from all 1,051 historical Putnam problems.
- **Why it's important:** Targets the most advanced mathematical reasoning (Putnam Competition, significantly harder than GSM8K/MATH). Even OpenAI's O3 drops 4.7 points on surface renamings and 12.9 points on parametric variants from a 51.5% baseline, demonstrating that fragility persists at the frontier of mathematical capability.

---

### 9. DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks

- **Authors:** Kaijie Zhu et al. (Microsoft Research, Duke, Virginia Tech)
- **Venue/Year:** ICLR 2024 (spotlight paper)
- **URL:** https://arxiv.org/abs/2309.17167
- **What it does:** Uses directed acyclic graphs to dynamically generate evaluation samples with controllable complexity for math, logic, and algorithm tasks, explicitly addressing data contamination concerns.
- **Why it's important:** ICLR 2024 spotlight; foundational work on dynamic/contamination-resistant evaluation. Shows that models claiming large improvements on static benchmarks (phi-1.5, WizardMath-13B) perform poorly on dynamically generated tests, directly motivating the contamination-robustness connection central to your paper.

---

### 10. RoMMath: Are Multimodal LLMs Robust Against Adversarial Perturbations?

- **Authors:** Yilun Zhao et al.
- **Venue/Year:** NAACL 2025 (long paper)
- **URL:** https://aclanthology.org/2025.naacl-long.582/
- **What it does:** Introduces a benchmark of 4,800 expert-annotated multimodal math examples with seven adversarial perturbation types targeting both text and vision modalities, evaluating 17 multimodal LLMs.
- **Why it's important:** Extends the adversarial robustness evaluation paradigm to the multimodal setting (math with figures/diagrams). Published at NAACL 2025; demonstrates that robustness challenges compound when perturbations can target either the textual or visual modality.

---

### Additional Papers of Note

- **Math-RoB** (Yu et al., March 2025, arXiv:2503.04550): Identifies four robustness failure modes -- positional bias, instruction sensitivity, numerical fragility, memory dependence -- and introduces an instruction-based benchmark. URL: https://arxiv.org/abs/2503.04550

- **Numerical Sensitivity and Robustness** (Sun et al., November 2025, arXiv:2511.08022): Shows models are especially fragile to irrelevant numerical distractors (drops up to 51.55% for open-source models), supporting the pattern-matching hypothesis. URL: https://arxiv.org/abs/2511.08022

- **More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists** (Alavi et al., November 2025, arXiv:2511.07112): Demonstrates that multi-agent collaboration improves accuracy but does not close the adversarial robustness gap, regardless of the number of agents. URL: https://arxiv.org/abs/2511.07112

---

### Summary of the Landscape

The papers above converge on several key themes relevant to your AAAI 2026 submission:

1. **Memorization vs. reasoning**: GSM-Symbolic, MATH-Perturb, and PutnamGAP all provide evidence that LLMs rely on pattern matching from training data rather than genuine mathematical reasoning, since semantically trivial perturbations cause large performance drops.

2. **Perturbation taxonomies**: The field has developed increasingly sophisticated perturbation methods -- from simple numeric substitution (GSM-Symbolic) to AST-based structural edits (Xie et al.) to multi-round rewrite-verify loops (MaSTer) to 13-perturbation deterministic pipelines (RRB).

3. **Contamination-robustness connection**: DyVal and MaSTer explicitly link dynamic variant generation to data contamination mitigation, which is directly aligned with your joint contamination-robustness evaluation framing.

4. **Scale of difficulty**: The benchmarks span grade-school (GSM8K variants), high-school (MATH-500 variants), competition-level (AIME, Putnam), and multimodal settings (RoMMath), providing comprehensive coverage.

5. **Consistent finding**: Even frontier models (GPT-4o, O3, o1-mini) show measurable degradation under perturbation, with open-source models showing even larger drops.

agentId: a2a519b9ad3da7e58 (use SendMessage with to: 'a2a519b9ad3da7e58' to continue this agent)
&lt;usage>total_tokens: 30240
tool_uses: 29
duration_ms: 154296&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "becd2467-9db3-4703-9d88-585f7ce182a8",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "a33efde0-b4d3-4c97-a198-a2753256f9b3",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs.\n\nSearch for the most important recent papers (2024-2026) on **adversarial robustness evaluation and perturbation methods for LLM mathematical/logical reasoning**. This includes:\n- Generating adversarial variants of math problems to test robustness\n- Symbolic perturbation methods for benchmarks\n- Studies showing LLMs fail on perturbed versions of known problems\n- Functional variant generation with provable correctness\n\nExecute these searches:\n1. WebSearch: \"adversarial math problem generation LLM robustness evaluation 2025 2026\"\n2. WebSearch: \"MaSTer automated adversarial math variant generation 2026\"\n3. WebSearch: \"GSM-Symbolic GSM-Plus MATH-Perturb benchmark perturbation LLM 2024 2025\"\n4. WebSearch: \"symbolic perturbation mathematical reasoning robustness LLM 2025\"\n5. WebSearch: \"functional variant generation benchmark LLM provable correctness 2025 2026\"\n6. WebSearch: \"reasoning robustness LLM NeurIPS ICML ICLR 2025 2026\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
    "agentId": "a2a519b9ad3da7e58",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the details needed. Here is the structured literature survey.\n\n---\n\n## Literature Survey: Adversarial Robustness Evaluation and Perturbation Methods for LLM Mathematical/Logical Reasoning (2024--2026)\n\nBelow are the most important recent papers, organized by relevance to your AAAI 2026 submission on joint contamination-robustness evaluation.\n\n---\n\n### 1. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\n\n- **Authors:** Iman Mirzadeh et al. (Apple)\n- **Venue/Year:** ICLR 2025 (conference paper)\n- **URL:** https://arxiv.org/abs/2410.05229\n- **What it does:** Introduces symbolic templates over GSM8K problems to generate diverse numeric/lexical variants; shows that merely changing numeric values or adding a single irrelevant clause degrades LLM performance by up to 65%.\n- **Why it's important:** Landmark paper from Apple Research establishing that current LLMs replicate reasoning steps from training data rather than performing genuine mathematical reasoning. Published at ICLR 2025; widely cited as the definitive demonstration that GSM8K scores are inflated by memorization. Open-source templates and data at https://github.com/apple/ml-gsm-symbolic.\n\n---\n\n### 2. GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers\n\n- **Authors:** Qintong Li et al. (HKU, Tencent AI Lab)\n- **Venue/Year:** ACL 2024 (main conference)\n- **URL:** https://arxiv.org/abs/2402.19255\n- **What it does:** Extends GSM8K with eight families of adversarial mathematical perturbations (numerical changes, added statements, altered question targets, etc.) and evaluates 25 LLMs across 4 prompting techniques.\n- **Why it's important:** One of the first systematic perturbation benchmarks for grade-school math, showing that even problems previously solved correctly by LLMs break under controlled perturbation. Published at the top NLP venue (ACL 2024 main conference). Proposes an iterative verification method to improve robustness.\n\n---\n\n### 3. MathCheck: Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist\n\n- **Authors:** Zihao Zhou et al.\n- **Venue/Year:** ICLR 2025 (conference paper)\n- **URL:** https://arxiv.org/abs/2407.08733\n- **What it does:** Proposes a checklist-based evaluation framework that tests both task generalization (problem solving, answerable judging, outcome judging, process judging) and reasoning robustness (irrelevant disturbance, scenario understanding, problem understanding) via MathCheck-GSM and MathCheck-GEO benchmarks.\n- **Why it's important:** Goes beyond single-task accuracy to evaluate multidimensional mathematical reasoning behavior. Accepted at ICLR 2025; evaluated 26 LLMs and 17 multimodal LLMs, revealing that frontier models like GPT-4o maintain performance but many model families show significant declines on the checklist.\n\n---\n\n### 4. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\n\n- **Authors:** Kaixuan Huang et al. (Princeton, Google DeepMind)\n- **Venue/Year:** arXiv preprint, February 2025\n- **URL:** https://arxiv.org/abs/2502.06453\n- **What it does:** Constructs MATH-P-Simple and MATH-P-Hard benchmarks (279 perturbed problems from the hardest MATH-500 tier), where \"simple\" perturbations preserve solution logic and \"hard\" perturbations fundamentally alter problem structure, rendering memorized solution strategies inapplicable.\n- **Why it's important:** Targets the most challenging competition-level problems (not just grade-school math); demonstrates large drops even for strong reasoning models (o1-mini: -16.5%, gemini-2.0-flash-thinking: -12.9%). Shows models mechanically apply memorized techniques without checking applicability to modified contexts.\n\n---\n\n### 5. MaSTer: Toward Automated Robustness Evaluation of Mathematical Reasoning\n\n- **Authors:** Yutao Hou et al.\n- **Venue/Year:** arXiv preprint, June 2025 (updated April 2026)\n- **URL:** https://arxiv.org/abs/2506.05038\n- **What it does:** Introduces a multi-round rewrite-verify loop framework that dynamically generates adversarial variants by modifying question stems (increasing linguistic complexity, adding irrelevant context) while preserving mathematical structure and answer correctness. Achieves 48% and 31% average accuracy reductions on GSM8K and MATH-500 variants, respectively.\n- **Why it's important:** Directly addresses data contamination by generating variants dynamically per model. Extends to AIME 2025 problems and generalizes beyond math to general reasoning tasks. Also demonstrates that fine-tuning on MaSTer-generated variants significantly improves in-domain robustness.\n\n---\n\n### 6. Adversarial Math Word Problem Generation\n\n- **Authors:** Roy Xie et al. (Duke University)\n- **Venue/Year:** Findings of EMNLP 2024\n- **URL:** https://arxiv.org/abs/2402.17916\n- **What it does:** Uses abstract syntax trees (ASTs) to systematically generate adversarial variants of math word problems by editing numeric values, preserving original question structure and difficulty while rendering problems unsolvable by LLMs.\n- **Why it's important:** Provides a principled, structure-preserving approach to adversarial generation grounded in program analysis (ASTs). Identifies shared vulnerabilities across open- and closed-source LLMs and proposes cost-effective strategies for attacking expensive models. Published at EMNLP 2024 Findings.\n\n---\n\n### 7. Robust Reasoning Benchmark (RRB)\n\n- **Authors:** Pavel Golikov et al. (University of Toronto)\n- **Venue/Year:** arXiv preprint, March 2026\n- **URL:** https://arxiv.org/abs/2604.08571\n- **What it does:** Applies a pipeline of 13 deterministic textual perturbations to AIME 2024 and AIME 2025 competition problems and evaluates 8 frontier models. Identifies a new failure mode called \"Intra-Query Attention Dilution\" where models solving multiple problems sequentially in one context show declining performance on later problems.\n- **Why it's important:** Very recent (2026), targets competition-level math (AIME), and introduces both a comprehensive perturbation taxonomy and a novel architectural failure mode (attention dilution). Shows accuracy losses reaching 54% average and 100% in specific cases for open-source reasoning models.\n\n---\n\n### 8. PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning via Mathematically-Equivalent Transformations\n\n- **Authors:** Yuren Hao, Xiang Wan, ChengXiang Zhai\n- **Venue/Year:** arXiv preprint, August 2025\n- **URL:** https://arxiv.org/abs/2508.08833\n- **What it does:** Proposes five aligned variants of Putnam Competition problems -- four surface renamings (symbol names only) and one core-step instance (numeric slot perturbation preserving the reasoning chain). Produces a 6,306-question PutnamGAP benchmark from all 1,051 historical Putnam problems.\n- **Why it's important:** Targets the most advanced mathematical reasoning (Putnam Competition, significantly harder than GSM8K/MATH). Even OpenAI's O3 drops 4.7 points on surface renamings and 12.9 points on parametric variants from a 51.5% baseline, demonstrating that fragility persists at the frontier of mathematical capability.\n\n---\n\n### 9. DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks\n\n- **Authors:** Kaijie Zhu et al. (Microsoft Research, Duke, Virginia Tech)\n- **Venue/Year:** ICLR 2024 (spotlight paper)\n- **URL:** https://arxiv.org/abs/2309.17167\n- **What it does:** Uses directed acyclic graphs to dynamically generate evaluation samples with controllable complexity for math, logic, and algorithm tasks, explicitly addressing data contamination concerns.\n- **Why it's important:** ICLR 2024 spotlight; foundational work on dynamic/contamination-resistant evaluation. Shows that models claiming large improvements on static benchmarks (phi-1.5, WizardMath-13B) perform poorly on dynamically generated tests, directly motivating the contamination-robustness connection central to your paper.\n\n---\n\n### 10. RoMMath: Are Multimodal LLMs Robust Against Adversarial Perturbations?\n\n- **Authors:** Yilun Zhao et al.\n- **Venue/Year:** NAACL 2025 (long paper)\n- **URL:** https://aclanthology.org/2025.naacl-long.582/\n- **What it does:** Introduces a benchmark of 4,800 expert-annotated multimodal math examples with seven adversarial perturbation types targeting both text and vision modalities, evaluating 17 multimodal LLMs.\n- **Why it's important:** Extends the adversarial robustness evaluation paradigm to the multimodal setting (math with figures/diagrams). Published at NAACL 2025; demonstrates that robustness challenges compound when perturbations can target either the textual or visual modality.\n\n---\n\n### Additional Papers of Note\n\n- **Math-RoB** (Yu et al., March 2025, arXiv:2503.04550): Identifies four robustness failure modes -- positional bias, instruction sensitivity, numerical fragility, memory dependence -- and introduces an instruction-based benchmark. URL: https://arxiv.org/abs/2503.04550\n\n- **Numerical Sensitivity and Robustness** (Sun et al., November 2025, arXiv:2511.08022): Shows models are especially fragile to irrelevant numerical distractors (drops up to 51.55% for open-source models), supporting the pattern-matching hypothesis. URL: https://arxiv.org/abs/2511.08022\n\n- **More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists** (Alavi et al., November 2025, arXiv:2511.07112): Demonstrates that multi-agent collaboration improves accuracy but does not close the adversarial robustness gap, regardless of the number of agents. URL: https://arxiv.org/abs/2511.07112\n\n---\n\n### Summary of the Landscape\n\nThe papers above converge on several key themes relevant to your AAAI 2026 submission:\n\n1. **Memorization vs. reasoning**: GSM-Symbolic, MATH-Perturb, and PutnamGAP all provide evidence that LLMs rely on pattern matching from training data rather than genuine mathematical reasoning, since semantically trivial perturbations cause large performance drops.\n\n2. **Perturbation taxonomies**: The field has developed increasingly sophisticated perturbation methods -- from simple numeric substitution (GSM-Symbolic) to AST-based structural edits (Xie et al.) to multi-round rewrite-verify loops (MaSTer) to 13-perturbation deterministic pipelines (RRB).\n\n3. **Contamination-robustness connection**: DyVal and MaSTer explicitly link dynamic variant generation to data contamination mitigation, which is directly aligned with your joint contamination-robustness evaluation framing.\n\n4. **Scale of difficulty**: The benchmarks span grade-school (GSM8K variants), high-school (MATH-500 variants), competition-level (AIME, Putnam), and multimodal settings (RoMMath), providing comprehensive coverage.\n\n5. **Consistent finding**: Even frontier models (GPT-4o, O3, o1-mini) show measurable degradation under perturbation, with open-source models showing even larger drops."
      }
    ],
    "totalDurationMs": 154296,
    "totalTokens": 30240,
    "totalToolUseCount": 29,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 853,
      "cache_read_input_tokens": 26434,
      "output_tokens": 2952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 853
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2952,
          "cache_read_input_tokens": 26434,
          "cache_creation_input_tokens": 853,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 853,
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
  "sourceToolAssistantUUID": "becd2467-9db3-4703-9d88-585f7ce182a8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-28 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "a33efde0-b4d3-4c97-a198-a2753256f9b3",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers for contamination-aware reasoning evaluation",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Tool result

_source line 26 · 2026-05-28T10:18:51.183Z_

<details><summary>↩ Tool result · `toolu_017ujnfS3688azZezYs8Y6Fy`</summary>

```text
Now I have all the information I need. Here is the structured literature survey.

---

## Literature Survey: IRT and Psychometrics-Based Approaches to LLM Evaluation (2024--2026)

Below are the most relevant recent papers, organized by relevance to a joint contamination-robustness evaluation paper targeting AAAI 2026.

---

### 1. PSN-IRT: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory

- **Authors:** Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao
- **Venue/Year:** **AAAI 2026 (Oral)**
- **URL:** https://arxiv.org/abs/2505.15055 | GitHub: https://github.com/Joe-Hall-Lee/PSN-IRT
- **What it does:** Proposes PSN-IRT (Pseudo-Siamese Network for IRT), an enhanced IRT framework with richer item parameters; analyzes 11 LLM benchmarks (41,871 items), revealing significant measurement quality shortcomings, and shows that IRT-derived smaller benchmarks better align with human preference.
- **Why it matters:** This is the most directly relevant paper -- it is an AAAI 2026 Oral, explicitly connects IRT item parameters (including guessing) to data contamination detection (high guessing rates may indicate memorized answers), and demonstrates benchmark quality diagnosis. A natural precursor/companion to contamination-robustness work.

---

### 2. ATLAS: Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks

- **Authors:** Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla
- **Venue/Year:** arXiv preprint, 2025 (withdrawn from ICLR 2026; under review elsewhere)
- **URL:** https://arxiv.org/abs/2511.04689 | GitHub: https://github.com/Peiyu-Georgia-Li/ATLAS
- **What it does:** First large-scale adaptive testing framework for LLMs, using Fisher information-guided item selection to reduce test items by 90% while maintaining measurement precision. On HellaSwag, 41 items suffice (out of 5,600). IRT-based ability estimates cause 23--31% of models to shift >10 rank positions vs. raw accuracy. Achieves natural contamination resistance through <10% item exposure rates.
- **Why it matters:** Directly addresses contamination resistance as a feature of adaptive testing (low item exposure prevents memorization). Uses 3,000+ LMs for calibration. The contamination-resistance angle makes this especially relevant to your paper's joint evaluation theme.

---

### 3. IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory

- **Authors:** Wei Song, Zhenya Huang, Cheng Cheng, Weibo Gao, Bihan Xu, GuanHao Zhao, Fei Wang, Runze Wu
- **Venue/Year:** **ACL 2025** (63rd Annual Meeting)
- **URL:** https://aclanthology.org/2025.acl-long.761/
- **What it does:** Applies IRT to model the relationship between LLM capabilities and user query attributes for multi-LLM routing, enabling accurate performance prediction and interpretable insights (model ability, query difficulty/discrimination). Uses a semantic similarity warm-up for cold-start generalization. Tested on 20 models and 12 datasets.
- **Why it matters:** Published at a top NLP venue (ACL 2025). Shows IRT's practical utility beyond evaluation -- for routing and deployment decisions. The IRT parameterization of model ability and item difficulty is directly reusable in contamination-robustness frameworks.

---

### 4. Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory

- **Authors:** Junhyuk Choi, Sohhyung Park, Chanhee Cho, Hyeonchu Park, Bugeun Kim
- **Venue/Year:** arXiv preprint, January 2026
- **URL:** https://arxiv.org/abs/2602.00521
- **What it does:** Uses the IRT Graded Response Model (GRM) to diagnose reliability of LLM-as-a-Judge systems along two dimensions: intrinsic consistency (stability under prompt variation) and human alignment (correspondence with human judgments). Produces interpretable diagnostic signals for pinpointing sources of unreliability.
- **Why it matters:** Extends IRT beyond traditional correct/incorrect scoring to graded response evaluation. Relevant because LLM-as-Judge is increasingly used for evaluation, and contamination could systematically bias judge reliability.

---

### 5. LaRT: Latency-Response Theory Model -- Evaluating LLMs via Response Accuracy and Chain-of-Thought Length

- **Authors:** Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu
- **Venue/Year:** arXiv preprint, December 2025
- **URL:** https://arxiv.org/abs/2512.07019
- **What it does:** Extends IRT by jointly modeling response correctness and chain-of-thought length, introducing latent ability, latent speed, and their correlation. Finds a strong negative correlation between ability and speed across all benchmarks (stronger reasoning = longer CoT). Outperforms traditional IRT in predictive power, item efficiency, and ranking validity.
- **Why it matters:** Novel extension of IRT that incorporates response-time (CoT length) as an additional signal. This dual-signal approach could help distinguish genuine reasoning from contamination-driven shortcuts (contaminated items might show anomalously short CoT).

---

### 6. JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory

- **Authors:** Louie Hong Yao, Nicholas Jarvis, Tiffany Zhan, Saptarshi Ghosh, Linfeng Liu, Tianyu Jiang
- **Venue/Year:** arXiv preprint, September 2025
- **URL:** https://arxiv.org/abs/2509.22888
- **What it does:** Places both LLMs and questions in a shared geometric embedding space where question direction captures semantic content and magnitude captures difficulty. Performance emerges from geometric relationships. Reveals that the learned taxonomy of LLM abilities only partially aligns with human-defined subject categories.
- **Why it matters:** Provides a continuous geometric interpretation of IRT that could detect anomalous ability patterns (e.g., a model performing disproportionately well on specific item clusters due to contamination).

---

### 7. LEGO-IRT: Toward a Unified Framework for Data-Efficient Evaluation of Large Language Models

- **Authors:** Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang
- **Venue/Year:** arXiv preprint, October 2025
- **URL:** https://arxiv.org/abs/2510.04051
- **What it does:** Reformulates IRT-based LLM evaluation as constrained matrix factorization subproblems; supports both binary and continuous metrics with a factorized architecture capturing cross-benchmark structural relationships. Achieves stable capability estimates using only 3% of evaluation items across 70 LLMs and 5 benchmarks.
- **Why it matters:** Demonstrates extreme data efficiency (3% of items), which is relevant for contamination-robust evaluation where one wants to minimize the exposed item pool. The cross-benchmark structural modeling could detect contamination-induced inconsistencies.

---

### 8. Learning Compact Representations of LLM Abilities via Item Response Theory (IrtNet)

- **Authors:** Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu
- **Venue/Year:** arXiv preprint, October 2025
- **URL:** https://arxiv.org/abs/2510.00844
- **What it does:** Uses IRT-inspired modeling (skill vectors, discrimination vectors, difficulty values) with a Mixture-of-Experts network to learn compact representations of LLM abilities. Demonstrates superior performance in model routing and benchmark accuracy prediction, with interpretable learned parameters.
- **Why it matters:** The compact skill-vector representation provides a principled way to detect contamination: a contaminated model would show anomalous spikes in specific skill dimensions inconsistent with its overall ability profile.

---

### 9. Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement

- **Authors:** Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, Guojie Song
- **Venue/Year:** arXiv preprint, May 2025 (revised March 2026); 400+ references
- **URL:** https://arxiv.org/abs/2505.08245 | Website: https://llm-psychometrics.com/
- **What it does:** Comprehensive interdisciplinary survey of psychometric approaches to LLM evaluation, covering personality, values, emotion, theory of mind, and motivation measurement. Argues for moving beyond static benchmarks toward human-centered evaluation paradigms.
- **Why it matters:** The definitive survey paper for this area. Essential reference for positioning any IRT/psychometrics work in the broader landscape. Useful for the related work section.

---

### 10. Provable Joint Decontamination for Benchmarking Multiple Large Language Models (JECS)

- **Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei
- **Venue/Year:** arXiv preprint, May 2026
- **URL:** https://arxiv.org/abs/2605.21543
- **What it does:** Proposes Joint Envelope Conformal Selection (JECS) for multi-model decontamination with provable guarantees. Computes per-model conformal p-values, aggregates by per-item maximum, and applies adaptive Benjamini-Hochberg to control global contamination rate while maintaining statistical power.
- **Why it matters:** Most directly relevant to the "joint contamination-robustness" angle of your AAAI paper. While not IRT-based itself, it provides the decontamination counterpart -- your paper could position itself at the intersection of IRT-based evaluation (papers 1--8) and provable decontamination (this paper).

---

### Additional relevant references (not fetched in full but worth noting):

- **Lifting the Benchmark Iceberg with Item-Response Theory** -- Schilling-Wilhelmi, Alampara, Jablonka. ICLR 2025 Workshop AI4MAT. URL: https://openreview.net/forum?id=ZyVQqK7mcP. Shows how hidden implementation decisions distort rankings and proposes IRT as a remedy.
- **An Interpretable and Scalable Framework for Evaluating Large Language Models** -- Qu, Heng, Zeng, Liu. arXiv May 2026. URL: https://arxiv.org/abs/2605.07046. Reformulates IRT estimation as constrained matrix factorization for scalability.

---

### Summary of the landscape

The field is experiencing rapid growth: IRT-based LLM evaluation went from a niche curiosity in 2024 to having an AAAI 2026 Oral (PSN-IRT), an ACL 2025 paper (IRT-Router), multiple arXiv preprints, and a 400-reference survey. The key themes are:

1. **Benchmark quality diagnosis** via IRT item parameters (PSN-IRT, ATLAS)
2. **Adaptive/efficient testing** reducing item exposure by 90--97% (ATLAS, LEGO-IRT)
3. **Natural contamination resistance** through low item exposure rates (ATLAS)
4. **Extended IRT models** incorporating CoT length (LaRT), geometric embeddings (JE-IRT), and graded responses (LLM-as-Judge)
5. **Provable decontamination** with statistical guarantees (JECS)

Your AAAI 2026 paper on joint contamination-robustness evaluation sits at the intersection of themes 1, 3, and 5 -- a space that PSN-IRT and ATLAS have opened but not fully explored with formal contamination guarantees.

agentId: a816c6d9485ca4338 (use SendMessage with to: 'a816c6d9485ca4338' to continue this agent)
&lt;usage>total_tokens: 25965
tool_uses: 25
duration_ms: 151502&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7b76c1cb-7be3-4bd6-bb1d-148822f6c717",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "28bb82b7-e512-4155-befc-0b88d1abda61",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs.\n\nSearch for the most important recent papers (2024-2026) on **Item Response Theory (IRT) applied to LLM evaluation** and **psychometrics-based approaches to AI assessment**. This includes:\n- IRT models adapted for evaluating language models\n- Adaptive testing frameworks for LLMs\n- Psychometric approaches to benchmark design\n- Calibrated scoring and measurement theory for AI\n\nExecute these searches:\n1. WebSearch: \"item response theory LLM evaluation 2025 2026\"\n2. WebSearch: \"ATLAS IRT adaptive testing large language models 2025\"\n3. WebSearch: \"psychometrics LLM benchmark evaluation calibration 2024 2025\"\n4. WebSearch: \"IRT computerized adaptive testing AI models 2025 2026\"\n5. WebSearch: \"PSN-IRT language model evaluation arXiv 2025\"\n6. WebSearch: \"measurement theory AI evaluation scoring 2025 2026\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
    "agentId": "a816c6d9485ca4338",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the information I need. Here is the structured literature survey.\n\n---\n\n## Literature Survey: IRT and Psychometrics-Based Approaches to LLM Evaluation (2024--2026)\n\nBelow are the most relevant recent papers, organized by relevance to a joint contamination-robustness evaluation paper targeting AAAI 2026.\n\n---\n\n### 1. PSN-IRT: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\n\n- **Authors:** Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, Tiejun Zhao\n- **Venue/Year:** **AAAI 2026 (Oral)**\n- **URL:** https://arxiv.org/abs/2505.15055 | GitHub: https://github.com/Joe-Hall-Lee/PSN-IRT\n- **What it does:** Proposes PSN-IRT (Pseudo-Siamese Network for IRT), an enhanced IRT framework with richer item parameters; analyzes 11 LLM benchmarks (41,871 items), revealing significant measurement quality shortcomings, and shows that IRT-derived smaller benchmarks better align with human preference.\n- **Why it matters:** This is the most directly relevant paper -- it is an AAAI 2026 Oral, explicitly connects IRT item parameters (including guessing) to data contamination detection (high guessing rates may indicate memorized answers), and demonstrates benchmark quality diagnosis. A natural precursor/companion to contamination-robustness work.\n\n---\n\n### 2. ATLAS: Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\n\n- **Authors:** Peiyu Li, Xiuxiu Tang, Si Chen, Ying Cheng, Ronald Metoyer, Ting Hua, Nitesh V. Chawla\n- **Venue/Year:** arXiv preprint, 2025 (withdrawn from ICLR 2026; under review elsewhere)\n- **URL:** https://arxiv.org/abs/2511.04689 | GitHub: https://github.com/Peiyu-Georgia-Li/ATLAS\n- **What it does:** First large-scale adaptive testing framework for LLMs, using Fisher information-guided item selection to reduce test items by 90% while maintaining measurement precision. On HellaSwag, 41 items suffice (out of 5,600). IRT-based ability estimates cause 23--31% of models to shift >10 rank positions vs. raw accuracy. Achieves natural contamination resistance through <10% item exposure rates.\n- **Why it matters:** Directly addresses contamination resistance as a feature of adaptive testing (low item exposure prevents memorization). Uses 3,000+ LMs for calibration. The contamination-resistance angle makes this especially relevant to your paper's joint evaluation theme.\n\n---\n\n### 3. IRT-Router: Effective and Interpretable Multi-LLM Routing via Item Response Theory\n\n- **Authors:** Wei Song, Zhenya Huang, Cheng Cheng, Weibo Gao, Bihan Xu, GuanHao Zhao, Fei Wang, Runze Wu\n- **Venue/Year:** **ACL 2025** (63rd Annual Meeting)\n- **URL:** https://aclanthology.org/2025.acl-long.761/\n- **What it does:** Applies IRT to model the relationship between LLM capabilities and user query attributes for multi-LLM routing, enabling accurate performance prediction and interpretable insights (model ability, query difficulty/discrimination). Uses a semantic similarity warm-up for cold-start generalization. Tested on 20 models and 12 datasets.\n- **Why it matters:** Published at a top NLP venue (ACL 2025). Shows IRT's practical utility beyond evaluation -- for routing and deployment decisions. The IRT parameterization of model ability and item difficulty is directly reusable in contamination-robustness frameworks.\n\n---\n\n### 4. Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\n\n- **Authors:** Junhyuk Choi, Sohhyung Park, Chanhee Cho, Hyeonchu Park, Bugeun Kim\n- **Venue/Year:** arXiv preprint, January 2026\n- **URL:** https://arxiv.org/abs/2602.00521\n- **What it does:** Uses the IRT Graded Response Model (GRM) to diagnose reliability of LLM-as-a-Judge systems along two dimensions: intrinsic consistency (stability under prompt variation) and human alignment (correspondence with human judgments). Produces interpretable diagnostic signals for pinpointing sources of unreliability.\n- **Why it matters:** Extends IRT beyond traditional correct/incorrect scoring to graded response evaluation. Relevant because LLM-as-Judge is increasingly used for evaluation, and contamination could systematically bias judge reliability.\n\n---\n\n### 5. LaRT: Latency-Response Theory Model -- Evaluating LLMs via Response Accuracy and Chain-of-Thought Length\n\n- **Authors:** Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu\n- **Venue/Year:** arXiv preprint, December 2025\n- **URL:** https://arxiv.org/abs/2512.07019\n- **What it does:** Extends IRT by jointly modeling response correctness and chain-of-thought length, introducing latent ability, latent speed, and their correlation. Finds a strong negative correlation between ability and speed across all benchmarks (stronger reasoning = longer CoT). Outperforms traditional IRT in predictive power, item efficiency, and ranking validity.\n- **Why it matters:** Novel extension of IRT that incorporates response-time (CoT length) as an additional signal. This dual-signal approach could help distinguish genuine reasoning from contamination-driven shortcuts (contaminated items might show anomalously short CoT).\n\n---\n\n### 6. JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory\n\n- **Authors:** Louie Hong Yao, Nicholas Jarvis, Tiffany Zhan, Saptarshi Ghosh, Linfeng Liu, Tianyu Jiang\n- **Venue/Year:** arXiv preprint, September 2025\n- **URL:** https://arxiv.org/abs/2509.22888\n- **What it does:** Places both LLMs and questions in a shared geometric embedding space where question direction captures semantic content and magnitude captures difficulty. Performance emerges from geometric relationships. Reveals that the learned taxonomy of LLM abilities only partially aligns with human-defined subject categories.\n- **Why it matters:** Provides a continuous geometric interpretation of IRT that could detect anomalous ability patterns (e.g., a model performing disproportionately well on specific item clusters due to contamination).\n\n---\n\n### 7. LEGO-IRT: Toward a Unified Framework for Data-Efficient Evaluation of Large Language Models\n\n- **Authors:** Lele Liao, Qile Zhang, Ruofan Wu, Guanhua Fang\n- **Venue/Year:** arXiv preprint, October 2025\n- **URL:** https://arxiv.org/abs/2510.04051\n- **What it does:** Reformulates IRT-based LLM evaluation as constrained matrix factorization subproblems; supports both binary and continuous metrics with a factorized architecture capturing cross-benchmark structural relationships. Achieves stable capability estimates using only 3% of evaluation items across 70 LLMs and 5 benchmarks.\n- **Why it matters:** Demonstrates extreme data efficiency (3% of items), which is relevant for contamination-robust evaluation where one wants to minimize the exposed item pool. The cross-benchmark structural modeling could detect contamination-induced inconsistencies.\n\n---\n\n### 8. Learning Compact Representations of LLM Abilities via Item Response Theory (IrtNet)\n\n- **Authors:** Jianhao Chen, Chenxu Wang, Gengrui Zhang, Peng Ye, Lei Bai, Wei Hu, Yuzhong Qu, Shuyue Hu\n- **Venue/Year:** arXiv preprint, October 2025\n- **URL:** https://arxiv.org/abs/2510.00844\n- **What it does:** Uses IRT-inspired modeling (skill vectors, discrimination vectors, difficulty values) with a Mixture-of-Experts network to learn compact representations of LLM abilities. Demonstrates superior performance in model routing and benchmark accuracy prediction, with interpretable learned parameters.\n- **Why it matters:** The compact skill-vector representation provides a principled way to detect contamination: a contaminated model would show anomalous spikes in specific skill dimensions inconsistent with its overall ability profile.\n\n---\n\n### 9. Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement\n\n- **Authors:** Haoran Ye, Jing Jin, Yuhang Xie, Xin Zhang, Guojie Song\n- **Venue/Year:** arXiv preprint, May 2025 (revised March 2026); 400+ references\n- **URL:** https://arxiv.org/abs/2505.08245 | Website: https://llm-psychometrics.com/\n- **What it does:** Comprehensive interdisciplinary survey of psychometric approaches to LLM evaluation, covering personality, values, emotion, theory of mind, and motivation measurement. Argues for moving beyond static benchmarks toward human-centered evaluation paradigms.\n- **Why it matters:** The definitive survey paper for this area. Essential reference for positioning any IRT/psychometrics work in the broader landscape. Useful for the related work section.\n\n---\n\n### 10. Provable Joint Decontamination for Benchmarking Multiple Large Language Models (JECS)\n\n- **Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei\n- **Venue/Year:** arXiv preprint, May 2026\n- **URL:** https://arxiv.org/abs/2605.21543\n- **What it does:** Proposes Joint Envelope Conformal Selection (JECS) for multi-model decontamination with provable guarantees. Computes per-model conformal p-values, aggregates by per-item maximum, and applies adaptive Benjamini-Hochberg to control global contamination rate while maintaining statistical power.\n- **Why it matters:** Most directly relevant to the \"joint contamination-robustness\" angle of your AAAI paper. While not IRT-based itself, it provides the decontamination counterpart -- your paper could position itself at the intersection of IRT-based evaluation (papers 1--8) and provable decontamination (this paper).\n\n---\n\n### Additional relevant references (not fetched in full but worth noting):\n\n- **Lifting the Benchmark Iceberg with Item-Response Theory** -- Schilling-Wilhelmi, Alampara, Jablonka. ICLR 2025 Workshop AI4MAT. URL: https://openreview.net/forum?id=ZyVQqK7mcP. Shows how hidden implementation decisions distort rankings and proposes IRT as a remedy.\n- **An Interpretable and Scalable Framework for Evaluating Large Language Models** -- Qu, Heng, Zeng, Liu. arXiv May 2026. URL: https://arxiv.org/abs/2605.07046. Reformulates IRT estimation as constrained matrix factorization for scalability.\n\n---\n\n### Summary of the landscape\n\nThe field is experiencing rapid growth: IRT-based LLM evaluation went from a niche curiosity in 2024 to having an AAAI 2026 Oral (PSN-IRT), an ACL 2025 paper (IRT-Router), multiple arXiv preprints, and a 400-reference survey. The key themes are:\n\n1. **Benchmark quality diagnosis** via IRT item parameters (PSN-IRT, ATLAS)\n2. **Adaptive/efficient testing** reducing item exposure by 90--97% (ATLAS, LEGO-IRT)\n3. **Natural contamination resistance** through low item exposure rates (ATLAS)\n4. **Extended IRT models** incorporating CoT length (LaRT), geometric embeddings (JE-IRT), and graded responses (LLM-as-Judge)\n5. **Provable decontamination** with statistical guarantees (JECS)\n\nYour AAAI 2026 paper on joint contamination-robustness evaluation sits at the intersection of themes 1, 3, and 5 -- a space that PSN-IRT and ATLAS have opened but not fully explored with formal contamination guarantees."
      }
    ],
    "totalDurationMs": 151502,
    "totalTokens": 25965,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 867,
      "cache_read_input_tokens": 22031,
      "output_tokens": 3066,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 867
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3066,
          "cache_read_input_tokens": 22031,
          "cache_creation_input_tokens": 867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 867,
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
  "sourceToolAssistantUUID": "7b76c1cb-7be3-4bd6-bb1d-148822f6c717",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-28T10:18:58.423Z_

<details><summary>↩ Tool result · `toolu_01UBeyCgVg2XWbpauMUrHGNZ`</summary>

```text
I now have comprehensive information on all the key papers. Here is the structured literature survey.

---

## Literature Survey: Joint Contamination-Robustness Evaluation of LLMs

### Papers Found (Organized by Relevance)

---

**1. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**
- **Authors:** Colin White et al. (18 authors including Yann LeCun, Tom Goldstein, Micah Goldblum)
- **Venue/Year:** ICLR 2025 Spotlight
- **URL:** https://arxiv.org/abs/2406.19314
- **What it does:** Introduces a dynamic LLM benchmark with frequently-updated questions from recent sources (math competitions, arXiv papers, news), scored automatically against objective ground truth, spanning math, coding, reasoning, language, instruction following, and data analysis.
- **Why it's important:** ICLR 2025 Spotlight paper. Directly addresses contamination by monthly question updates. Top models achieve below 70% accuracy, demonstrating the benchmark's difficulty. The most directly relevant prior work for contamination-free evaluation.

---

**2. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)**
- **Authors:** Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Alon Albalak, Yejin Choi
- **Venue/Year:** NeurIPS 2025 Best Paper Award (Datasets & Benchmarks Track, Oral)
- **URL:** https://arxiv.org/abs/2510.22954
- **What it does:** Introduces Infinity-Chat (26K open-ended queries, 31K+ human annotations) and reveals "diversity collapse" across LLMs -- both intra-model repetition and inter-model homogeneity -- showing that reward models and LLM-as-a-judge punish diversity.
- **Why it's important:** NeurIPS 2025 Best Paper. Exposes a fundamental evaluation blind spot: current evaluation methods (reward models, LLM-as-judge) systematically fail to credit valid but diverse responses, directly undermining robustness of evaluation.

---

**3. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**
- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang
- **Venue/Year:** NeurIPS 2025 Best Paper Runner-Up (Oral); also ICML 2025 AI4MATH Workshop Best Paper
- **URL:** https://arxiv.org/abs/2504.13837
- **What it does:** Systematically evaluates whether RLVR (Reinforcement Learning with Verifiable Rewards) truly creates new reasoning capabilities in LLMs, finding that it merely biases output distribution toward rewarded paths without expanding the reasoning boundary (base models achieve higher pass@k at large k).
- **Why it's important:** NeurIPS 2025 Runner-Up + ICML 2025 Workshop Best Paper. Directly relevant to robustness evaluation: it shows that standard evaluation metrics (greedy accuracy) can be misleading about genuine capability, while pass@k reveals that RLVR models do not surpass base model reasoning boundaries.

---

**4. LLMs Get Lost In Multi-Turn Conversation**
- **Authors:** Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Venue/Year:** ICLR 2026 Outstanding Paper (Oral)
- **URL:** https://arxiv.org/abs/2505.06120
- **What it does:** Designs a scalable multi-turn evaluation framework that splits instructions into "shards" delivered across turns, revealing a 39% average performance degradation in multi-turn settings compared to single-turn across six generation tasks and all top LLMs tested.
- **Why it's important:** ICLR 2026 Outstanding Paper. Exposes a critical gap between how LLMs are evaluated (single-turn) and how they are deployed (multi-turn), demonstrating that standard benchmarks systematically overestimate real-world robustness.

---

**5. LLMEval-Fair: A Large-Scale Longitudinal Study on Robust and Fair Evaluation of Large Language Models**
- **Authors:** Ming Zhang, Yujiong Shen, Jingyi Deng et al. (22 authors including Tao Gui, Qi Zhang, Xuanjing Huang)
- **Venue/Year:** arXiv 2025 (under review)
- **URL:** https://arxiv.org/abs/2508.05452
- **What it does:** Presents a dynamic evaluation framework drawing from a bank of 220K graduate-level questions with anti-cheating architecture and calibrated LLM-as-a-judge (90% human agreement), conducting a 30-month longitudinal study of ~60 models that reveals performance ceilings and contamination vulnerabilities undetectable by static benchmarks.
- **Why it's important:** One of the most comprehensive contamination-aware evaluation frameworks to date, combining dynamic evaluation, anti-cheating design, and longitudinal analysis -- directly addresses the joint contamination-robustness problem.

---

**6. MathArena: Evaluating LLMs on Uncontaminated Math Competitions**
- **Authors:** Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev
- **Venue/Year:** arXiv 2025 (ETH Zurich)
- **URL:** https://arxiv.org/abs/2505.23281
- **What it does:** Uses newly released math competition problems as an evolving benchmark to evaluate LLM mathematical reasoning while avoiding contamination, evaluating 50+ models across 162 problems from seven competitions including the first benchmark for proof-writing capabilities.
- **Why it's important:** Demonstrates concrete evidence of contamination in AIME 2024 while providing a contamination-resistant evaluation methodology. Continuously updated with new competitions.

---

**7. ThinkBench: Dynamic Out-of-Distribution Evaluation for Robust LLM Reasoning**
- **Authors:** Shulin Huang, Linyi Yang, Yan Song, Shuang Chen, Leyang Cui et al. (12 authors)
- **Venue/Year:** arXiv 2025
- **URL:** https://arxiv.org/abs/2502.16268
- **What it does:** Proposes a framework using causal theory and semi-factual causality to dynamically generate out-of-distribution reasoning datasets (2,912 samples), evaluating 16 LLMs and 4 process reward models to show that most models' performance is "far from robust" and exhibits data leakage.
- **Why it's important:** Directly addresses the intersection of contamination and robustness by generating OOD test data that mitigates memorization effects, providing a more reliable assessment of genuine reasoning capability.

---

**8. Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs**
- **Authors:** Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao
- **Venue/Year:** arXiv 2026
- **URL:** https://arxiv.org/abs/2602.11674
- **What it does:** Introduces a meta-evaluation framework that scores benchmarks across three dimensions -- capability discrimination, anti-saturation, and ecosystem impact -- analyzing 106 benchmarks using 91 models to systematically assess benchmark health.
- **Why it's important:** Provides a principled methodology for evaluating the evaluators themselves, directly relevant to understanding which benchmarks remain robust against contamination and saturation.

---

**9. Benchmark Data Contamination of Large Language Models: A Survey**
- **Authors:** Cheng Xu, Shuhao Guan, Derek Greene, M-Tahar Kechadi
- **Venue/Year:** arXiv 2024 (31 pages)
- **URL:** https://arxiv.org/abs/2406.04244
- **What it does:** Surveys how LLMs inadvertently incorporate benchmark data during training, examines alternative assessment approaches, and explores future directions for mitigating contamination risks.
- **Why it's important:** One of the earliest comprehensive surveys on benchmark contamination in LLMs; provides essential background and taxonomy for contamination-robustness research.

---

**10. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation**
- **Authors:** Simin Chen, Yiming Chen, Zexin Li et al. (11 authors including Haizhou Li, Tao Xie, Baishakhi Ray)
- **Venue/Year:** arXiv 2025
- **URL:** https://arxiv.org/abs/2502.17521
- **What it does:** Analyzes the shift from static to dynamic LLM benchmarking, identifies limitations in current static enhancements and dynamic benchmarks, and proposes optimal design principles for contamination-resistant dynamic evaluation.
- **Why it's important:** Provides the most up-to-date systematic comparison of static vs. dynamic evaluation paradigms, with a maintained GitHub repository tracking both approaches -- essential framing for a contamination-robustness paper.

---

**11. CoreEval: Automatically Building Contamination-Resilient Datasets with Real-World Knowledge toward Reliable LLM Evaluation**
- **Authors:** Jingqian Zhao, Bingbing Wang, Geng Tu, Yice Zhang, Qianlong Wang, Bin Liang, Jing Li, Ruifeng Xu
- **Venue/Year:** ACL 2025
- **URL:** https://arxiv.org/abs/2511.18889
- **What it does:** Extracts entity relationships from original data and leverages the GDELT database to retrieve up-to-date knowledge, integrating it with original data while maintaining semantic coherence to create contamination-resilient evaluation datasets.
- **Why it's important:** Published at ACL 2025; presents a practical, automated approach to building contamination-resistant benchmarks that can be continuously refreshed.

---

### Summary of Award-Winning Papers by Venue

| Paper | Venue | Award |
|---|---|---|
| Artificial Hivemind | NeurIPS 2025 | Best Paper (D&B Track) |
| Does RL Really Incentivize Reasoning | NeurIPS 2025 | Best Paper Runner-Up + ICML 2025 Workshop Best Paper |
| LiveBench | ICLR 2025 | Spotlight |
| LLMs Get Lost In Multi-Turn Conversation | ICLR 2026 | Outstanding Paper |
| CoreEval | ACL 2025 | Main conference paper |

### Note on AAAI 2026
The AAAI 2026 outstanding paper awards (5 main track, 2 social impact) did not include papers directly on LLM evaluation/robustness/contamination. The closest was "LLM2CLIP" on vision-language representation. However, AAAI 2026 introduced a dedicated Special Track on AI Alignment, which accepted papers on scalable oversight, robustness evaluation, and red-teaming -- relevant context for your submission venue.

Sources:
- [NeurIPS 2025 Best Paper Awards](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)
- [ICLR 2026 Outstanding Papers](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)
- [AAAI 2026 Outstanding Papers](https://aihub.org/2026/01/22/congratulations-to-the-aaai2026-outstanding-paper-award-winners/)
- [LiveBench (arXiv)](https://arxiv.org/abs/2406.19314)
- [Artificial Hivemind (arXiv)](https://arxiv.org/abs/2510.22954)
- [Does RL Really Incentivize Reasoning (arXiv)](https://arxiv.org/abs/2504.13837)
- [LLMs Get Lost In Multi-Turn Conversation (arXiv)](https://arxiv.org/abs/2505.06120)
- [LLMEval-Fair (arXiv)](https://arxiv.org/abs/2508.05452)
- [MathArena (arXiv)](https://arxiv.org/abs/2505.23281)
- [ThinkBench (arXiv)](https://arxiv.org/abs/2502.16268)
- [Benchmark Health Index (arXiv)](https://arxiv.org/abs/2602.11674)
- [Benchmark Data Contamination Survey (arXiv)](https://arxiv.org/abs/2406.04244)
- [Static to Dynamic Evaluation Survey (arXiv)](https://arxiv.org/abs/2502.17521)
- [CoreEval (arXiv)](https://arxiv.org/abs/2511.18889)
- [AAAI 2026 Highlights](https://www.bohrium.com/en/blog/research-notes/aaai-2026-accepted-papers-highlights/)

agentId: a4e5424beb7d4bfc7 (use SendMessage with to: 'a4e5424beb7d4bfc7' to continue this agent)
&lt;usage>total_tokens: 32810
tool_uses: 30
duration_ms: 147902&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4b2b52a-63c4-4a80-912d-f33729083e7f",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "191ad576-275c-49c2-88cc-2ad883b6c217",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey for an AAAI 2026 paper on joint contamination-robustness evaluation of LLMs.\n\nSearch for **best paper awards, oral/spotlight presentations, and highly-cited work** at top venues (2024-2026) related to LLM evaluation, robustness, and alignment. Also search for comprehensive evaluation frameworks and dynamic benchmarks.\n\nExecute these searches:\n1. WebSearch: \"best paper award NeurIPS 2025 LLM evaluation\"\n2. WebSearch: \"best paper award ICML 2025 language model\"\n3. WebSearch: \"best paper ICLR 2025 2026 LLM benchmark evaluation\"\n4. WebSearch: \"best paper ACL EMNLP 2025 evaluation robustness\"\n5. WebSearch: \"LiveBench MathArena dynamic benchmark LLM contamination-free 2024 2025\"\n6. WebSearch: \"LLM evaluation framework comprehensive robustness contamination 2025 2026\"\n7. WebSearch: \"AAAI 2025 2026 best paper AI alignment evaluation\"\n\nFor each paper you find, use WebFetch to read its arXiv abstract page to get the full title, authors, venue, and understand what it does.\n\nReport back with a structured list of papers found, including:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (one sentence)\n- Why it's important (citations, awards, etc.)\n\nFind at least 5-8 relevant papers.",
    "agentId": "a4e5424beb7d4bfc7",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all the key papers. Here is the structured literature survey.\n\n---\n\n## Literature Survey: Joint Contamination-Robustness Evaluation of LLMs\n\n### Papers Found (Organized by Relevance)\n\n---\n\n**1. LiveBench: A Challenging, Contamination-Limited LLM Benchmark**\n- **Authors:** Colin White et al. (18 authors including Yann LeCun, Tom Goldstein, Micah Goldblum)\n- **Venue/Year:** ICLR 2025 Spotlight\n- **URL:** https://arxiv.org/abs/2406.19314\n- **What it does:** Introduces a dynamic LLM benchmark with frequently-updated questions from recent sources (math competitions, arXiv papers, news), scored automatically against objective ground truth, spanning math, coding, reasoning, language, instruction following, and data analysis.\n- **Why it's important:** ICLR 2025 Spotlight paper. Directly addresses contamination by monthly question updates. Top models achieve below 70% accuracy, demonstrating the benchmark's difficulty. The most directly relevant prior work for contamination-free evaluation.\n\n---\n\n**2. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)**\n- **Authors:** Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri, Yulia Tsvetkov, Maarten Sap, Alon Albalak, Yejin Choi\n- **Venue/Year:** NeurIPS 2025 Best Paper Award (Datasets & Benchmarks Track, Oral)\n- **URL:** https://arxiv.org/abs/2510.22954\n- **What it does:** Introduces Infinity-Chat (26K open-ended queries, 31K+ human annotations) and reveals \"diversity collapse\" across LLMs -- both intra-model repetition and inter-model homogeneity -- showing that reward models and LLM-as-a-judge punish diversity.\n- **Why it's important:** NeurIPS 2025 Best Paper. Exposes a fundamental evaluation blind spot: current evaluation methods (reward models, LLM-as-judge) systematically fail to credit valid but diverse responses, directly undermining robustness of evaluation.\n\n---\n\n**3. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?**\n- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang\n- **Venue/Year:** NeurIPS 2025 Best Paper Runner-Up (Oral); also ICML 2025 AI4MATH Workshop Best Paper\n- **URL:** https://arxiv.org/abs/2504.13837\n- **What it does:** Systematically evaluates whether RLVR (Reinforcement Learning with Verifiable Rewards) truly creates new reasoning capabilities in LLMs, finding that it merely biases output distribution toward rewarded paths without expanding the reasoning boundary (base models achieve higher pass@k at large k).\n- **Why it's important:** NeurIPS 2025 Runner-Up + ICML 2025 Workshop Best Paper. Directly relevant to robustness evaluation: it shows that standard evaluation metrics (greedy accuracy) can be misleading about genuine capability, while pass@k reveals that RLVR models do not surpass base model reasoning boundaries.\n\n---\n\n**4. LLMs Get Lost In Multi-Turn Conversation**\n- **Authors:** Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville\n- **Venue/Year:** ICLR 2026 Outstanding Paper (Oral)\n- **URL:** https://arxiv.org/abs/2505.06120\n- **What it does:** Designs a scalable multi-turn evaluation framework that splits instructions into \"shards\" delivered across turns, revealing a 39% average performance degradation in multi-turn settings compared to single-turn across six generation tasks and all top LLMs tested.\n- **Why it's important:** ICLR 2026 Outstanding Paper. Exposes a critical gap between how LLMs are evaluated (single-turn) and how they are deployed (multi-turn), demonstrating that standard benchmarks systematically overestimate real-world robustness.\n\n---\n\n**5. LLMEval-Fair: A Large-Scale Longitudinal Study on Robust and Fair Evaluation of Large Language Models**\n- **Authors:** Ming Zhang, Yujiong Shen, Jingyi Deng et al. (22 authors including Tao Gui, Qi Zhang, Xuanjing Huang)\n- **Venue/Year:** arXiv 2025 (under review)\n- **URL:** https://arxiv.org/abs/2508.05452\n- **What it does:** Presents a dynamic evaluation framework drawing from a bank of 220K graduate-level questions with anti-cheating architecture and calibrated LLM-as-a-judge (90% human agreement), conducting a 30-month longitudinal study of ~60 models that reveals performance ceilings and contamination vulnerabilities undetectable by static benchmarks.\n- **Why it's important:** One of the most comprehensive contamination-aware evaluation frameworks to date, combining dynamic evaluation, anti-cheating design, and longitudinal analysis -- directly addresses the joint contamination-robustness problem.\n\n---\n\n**6. MathArena: Evaluating LLMs on Uncontaminated Math Competitions**\n- **Authors:** Mislav Balunovic, Jasper Dekoninck, Ivo Petrov, Nikola Jovanovic, Martin Vechev\n- **Venue/Year:** arXiv 2025 (ETH Zurich)\n- **URL:** https://arxiv.org/abs/2505.23281\n- **What it does:** Uses newly released math competition problems as an evolving benchmark to evaluate LLM mathematical reasoning while avoiding contamination, evaluating 50+ models across 162 problems from seven competitions including the first benchmark for proof-writing capabilities.\n- **Why it's important:** Demonstrates concrete evidence of contamination in AIME 2024 while providing a contamination-resistant evaluation methodology. Continuously updated with new competitions.\n\n---\n\n**7. ThinkBench: Dynamic Out-of-Distribution Evaluation for Robust LLM Reasoning**\n- **Authors:** Shulin Huang, Linyi Yang, Yan Song, Shuang Chen, Leyang Cui et al. (12 authors)\n- **Venue/Year:** arXiv 2025\n- **URL:** https://arxiv.org/abs/2502.16268\n- **What it does:** Proposes a framework using causal theory and semi-factual causality to dynamically generate out-of-distribution reasoning datasets (2,912 samples), evaluating 16 LLMs and 4 process reward models to show that most models' performance is \"far from robust\" and exhibits data leakage.\n- **Why it's important:** Directly addresses the intersection of contamination and robustness by generating OOD test data that mitigates memorization effects, providing a more reliable assessment of genuine reasoning capability.\n\n---\n\n**8. Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs**\n- **Authors:** Longyuan Zhu, Hairan Hua, Linlin Miao, Bing Zhao\n- **Venue/Year:** arXiv 2026\n- **URL:** https://arxiv.org/abs/2602.11674\n- **What it does:** Introduces a meta-evaluation framework that scores benchmarks across three dimensions -- capability discrimination, anti-saturation, and ecosystem impact -- analyzing 106 benchmarks using 91 models to systematically assess benchmark health.\n- **Why it's important:** Provides a principled methodology for evaluating the evaluators themselves, directly relevant to understanding which benchmarks remain robust against contamination and saturation.\n\n---\n\n**9. Benchmark Data Contamination of Large Language Models: A Survey**\n- **Authors:** Cheng Xu, Shuhao Guan, Derek Greene, M-Tahar Kechadi\n- **Venue/Year:** arXiv 2024 (31 pages)\n- **URL:** https://arxiv.org/abs/2406.04244\n- **What it does:** Surveys how LLMs inadvertently incorporate benchmark data during training, examines alternative assessment approaches, and explores future directions for mitigating contamination risks.\n- **Why it's important:** One of the earliest comprehensive surveys on benchmark contamination in LLMs; provides essential background and taxonomy for contamination-robustness research.\n\n---\n\n**10. Recent Advances in Large Language Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation**\n- **Authors:** Simin Chen, Yiming Chen, Zexin Li et al. (11 authors including Haizhou Li, Tao Xie, Baishakhi Ray)\n- **Venue/Year:** arXiv 2025\n- **URL:** https://arxiv.org/abs/2502.17521\n- **What it does:** Analyzes the shift from static to dynamic LLM benchmarking, identifies limitations in current static enhancements and dynamic benchmarks, and proposes optimal design principles for contamination-resistant dynamic evaluation.\n- **Why it's important:** Provides the most up-to-date systematic comparison of static vs. dynamic evaluation paradigms, with a maintained GitHub repository tracking both approaches -- essential framing for a contamination-robustness paper.\n\n---\n\n**11. CoreEval: Automatically Building Contamination-Resilient Datasets with Real-World Knowledge toward Reliable LLM Evaluation**\n- **Authors:** Jingqian Zhao, Bingbing Wang, Geng Tu, Yice Zhang, Qianlong Wang, Bin Liang, Jing Li, Ruifeng Xu\n- **Venue/Year:** ACL 2025\n- **URL:** https://arxiv.org/abs/2511.18889\n- **What it does:** Extracts entity relationships from original data and leverages the GDELT database to retrieve up-to-date knowledge, integrating it with original data while maintaining semantic coherence to create contamination-resilient evaluation datasets.\n- **Why it's important:** Published at ACL 2025; presents a practical, automated approach to building contamination-resistant benchmarks that can be continuously refreshed.\n\n---\n\n### Summary of Award-Winning Papers by Venue\n\n| Paper | Venue | Award |\n|---|---|---|\n| Artificial Hivemind | NeurIPS 2025 | Best Paper (D&B Track) |\n| Does RL Really Incentivize Reasoning | NeurIPS 2025 | Best Paper Runner-Up + ICML 2025 Workshop Best Paper |\n| LiveBench | ICLR 2025 | Spotlight |\n| LLMs Get Lost In Multi-Turn Conversation | ICLR 2026 | Outstanding Paper |\n| CoreEval | ACL 2025 | Main conference paper |\n\n### Note on AAAI 2026\nThe AAAI 2026 outstanding paper awards (5 main track, 2 social impact) did not include papers directly on LLM evaluation/robustness/contamination. The closest was \"LLM2CLIP\" on vision-language representation. However, AAAI 2026 introduced a dedicated Special Track on AI Alignment, which accepted papers on scalable oversight, robustness evaluation, and red-teaming -- relevant context for your submission venue.\n\nSources:\n- [NeurIPS 2025 Best Paper Awards](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)\n- [ICLR 2026 Outstanding Papers](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)\n- [AAAI 2026 Outstanding Papers](https://aihub.org/2026/01/22/congratulations-to-the-aaai2026-outstanding-paper-award-winners/)\n- [LiveBench (arXiv)](https://arxiv.org/abs/2406.19314)\n- [Artificial Hivemind (arXiv)](https://arxiv.org/abs/2510.22954)\n- [Does RL Really Incentivize Reasoning (arXiv)](https://arxiv.org/abs/2504.13837)\n- [LLMs Get Lost In Multi-Turn Conversation (arXiv)](https://arxiv.org/abs/2505.06120)\n- [LLMEval-Fair (arXiv)](https://arxiv.org/abs/2508.05452)\n- [MathArena (arXiv)](https://arxiv.org/abs/2505.23281)\n- [ThinkBench (arXiv)](https://arxiv.org/abs/2502.16268)\n- [Benchmark Health Index (arXiv)](https://arxiv.org/abs/2602.11674)\n- [Benchmark Data Contamination Survey (arXiv)](https://arxiv.org/abs/2406.04244)\n- [Static to Dynamic Evaluation Survey (arXiv)](https://arxiv.org/abs/2502.17521)\n- [CoreEval (arXiv)](https://arxiv.org/abs/2511.18889)\n- [AAAI 2026 Highlights](https://www.bohrium.com/en/blog/research-notes/aaai-2026-accepted-papers-highlights/)"
      }
    ],
    "totalDurationMs": 147902,
    "totalTokens": 32810,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 838,
      "cache_read_input_tokens": 28702,
      "output_tokens": 3269,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 838
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3269,
          "cache_read_input_tokens": 28702,
          "cache_creation_input_tokens": 838,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 838,
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
      "otherToolCount": 30
    }
  },
  "sourceToolAssistantUUID": "f4b2b52a-63c4-4a80-912d-f33729083e7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-28 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "191ad576-275c-49c2-88cc-2ad883b6c217",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers for contamination-aware reasoning evaluation",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Assistant

_source line 30 · 2026-05-28T10:19:38.019Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I now have comprehensive results from all five search agents. Let me synthesize the findings and select the 15 most important papers. Let me also verify a few key papers by fetching their actual arXiv pages to confirm details.

Let me compile the top 15 papers based on the criteria:
1. Best paper awards at top venues
2. Oral/spotlight presentations
3. Highly cited papers
4. Papers that introduced widely-adopted methods
5. Recent survey papers
6. Strong recent work from top labs

Let me organize by relevance to the CRADE framework:

**Core pillars of CRADE:**


1. Contamination detection/correction
2. Adversarial variant generation
3. Step-level reasoning evaluation
4. IRT-based calibrated scoring
5. Joint modeling

Now I'm identifying the 15 most impactful papers across these dimensions, starting with landmark work on symbolic perturbation and memorization detection, followed by papers on IRT-based evaluation frameworks and adaptive testing approaches for LLMs.

Then there's the contamination resistance angle—gray-box detection methods, work showing how detection fails on reasoning models, and contamination-adjusted scoring techniques. I'm also considering papers on chain-of-thought faithfulness since that's critical for evaluating reasoning, plus step-level evaluation benchmarks and progress-based reward mechanisms.

For addressing contamination directly, LiveBench offers a dynamic approach, though there's interesting work questioning whether RL actually creates new reasoning capabilities or just optimizes existing ones. The perturbation and adversarial variant generation papers provide ways to create robust test sets, and there's emerging work on provable decontamination methods. I should also look at IRT-based approaches for more sophisticated evaluation. Now I'm narrowing down to the fifteen most directly relevant papers, focusing on the essential ones that define key paradigms and provide foundational work for this research—starting with GSM-Symbolic for robustness-via-perturbation, PSN-IRT and ATLAS for IRT-based evaluation frameworks, CoDeC as a detection backbone, and the benchmark contamination fragility paper that motivates the whole direction. Xu et al., EMNLP 2025) - Essential: Closest competitor
7. **Reasoning Models Don't Always Say What They Think** (Chen et al., Anthropic 2025) - Essential: CoT unfaithfulness
8. **ReasonEval** (Xia et al., AAAI 2025 Oral) - Essential: Step-level evaluation, same venue
9. **PAVs/Rewarding Progress** (Setlur et al., ICLR 2025 Spotlight) - Important: Process verification foundation
10. **LiveBench** (White et al., ICLR 2025 Spotlight) - Important: Contamination-free evaluation baseline
11. **Does RL Really Incentivize Reasoning** (Yue et al., NeurIPS 2025 Runner-Up) - Important: Genuine capability vs surface metrics
12. **MATH-Perturb** (Huang et al., arXiv 2025) - Important: Competition-level perturbation
13. **MaSTer** (Hou et al., arXiv 2026) - Essential: Seed paper, best perturbation method
14. **FaithCoT-Bench** (Shen et al., ICLR 2026) - Important: CoT faithfulness benchmark
15. **JECS** (Liu et al., arXiv 2026) - Important: Provable joint decontamination

Now I'm pulling together the final list and considering whether to include LaRT and a few other papers that extend related work. continuing with papers 6 through 14, covering adaptive testing frameworks, reasoning faithfulness, step-level evaluation methods, process verification approaches, contamination-free benchmarks, and capability assessment studies.

Now I'm adding a few more relevant papers to reach the user's target of at least 15, including LaRT for joint IRT and chain-of-thought modeling, ReasoningMath-Plus as a foundational seed paper for step-level evaluation, JECS for decontamination guarantees, and ThinkPRM for generative process reward modeling. I should aim for around 18-20 papers total to be comprehensive while staying focused on genuinely relevant work. Let me verify a few of the key papers I'm less certain about, then structure everything into the final JSON output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "191ad576-275c-49c2-88cc-2ad883b6c217",
  "isSidechain": false,
  "requestId": "req_011CbUoAPiCGg42f68kTHo7z",
  "type": "assistant",
  "uuid": "5c7ad8e5-1068-4af9-bc3b-bbc15a3fd09c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHFDcT4YRJ5RBTfL8K9UoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19565,
      "cache_read_input_tokens": 16834,
      "output_tokens": 2631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2631,
          "cache_read_input_tokens": 16834,
          "cache_creation_input_tokens": 19565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19565
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

_source line 31 · 2026-05-28T10:19:38.021Z_

Now let me verify a few key papers that need confirmation on details, especially the newer ones:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c7ad8e5-1068-4af9-bc3b-bbc15a3fd09c",
  "isSidechain": false,
  "requestId": "req_011CbUoAPiCGg42f68kTHo7z",
  "type": "assistant",
  "uuid": "35b624b4-f833-4fc5-9540-9e7ac136789c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHFDcT4YRJ5RBTfL8K9UoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19565,
      "cache_read_input_tokens": 16834,
      "output_tokens": 2631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2631,
          "cache_read_input_tokens": 16834,
          "cache_creation_input_tokens": 19565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19565
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

_source line 32 · 2026-05-28T10:19:38.091Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016qHu5REWVLHhPKyDdGYEe8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.15055",
  "prompt": "Extract the full title, authors, and abstract of this paper. Is it accepted at AAAI 2026? What does PSN-IRT do?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35b624b4-f833-4fc5-9540-9e7ac136789c",
  "isSidechain": false,
  "requestId": "req_011CbUoAPiCGg42f68kTHo7z",
  "type": "assistant",
  "uuid": "50b07410-9897-413d-aa38-6b7eb17669e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHFDcT4YRJ5RBTfL8K9UoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19565,
      "cache_read_input_tokens": 16834,
      "output_tokens": 2631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2631,
          "cache_read_input_tokens": 16834,
          "cache_creation_input_tokens": 19565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19565
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

_source line 33 · 2026-05-28T10:19:39.235Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0165wNrPVD7JXt5PVzEZDeyp`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.21543",
  "prompt": "Extract the full title, authors, abstract and venue of this paper about JECS joint decontamination. What exactly does it propose?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50b07410-9897-413d-aa38-6b7eb17669e0",
  "isSidechain": false,
  "requestId": "req_011CbUoAPiCGg42f68kTHo7z",
  "type": "assistant",
  "uuid": "34ea385c-1753-466f-82d3-4a513ad13948",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHFDcT4YRJ5RBTfL8K9UoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19565,
      "cache_read_input_tokens": 16834,
      "output_tokens": 2631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2631,
          "cache_read_input_tokens": 16834,
          "cache_creation_input_tokens": 19565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19565
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

_source line 34 · 2026-05-28T10:19:40.181Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012H4ssEttYEvyyuTmm6DNqC`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.07019",
  "prompt": "Extract the full title, authors, and abstract of LaRT. What does it do? Is it published at a venue?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34ea385c-1753-466f-82d3-4a513ad13948",
  "isSidechain": false,
  "requestId": "req_011CbUoAPiCGg42f68kTHo7z",
  "type": "assistant",
  "uuid": "df61f82b-ed35-4720-9058-c143f02f8586",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHFDcT4YRJ5RBTfL8K9UoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19565,
      "cache_read_input_tokens": 16834,
      "output_tokens": 2631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2631,
          "cache_read_input_tokens": 16834,
          "cache_creation_input_tokens": 19565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19565
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

_source line 35 · 2026-05-28T10:19:41.167Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_011yK2UqmKpH5x9y3VvqBNUU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2504.13837",
  "prompt": "Extract the full title, authors, abstract. Is this a NeurIPS 2025 best paper runner-up? What does it show about RL and reasoning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df61f82b-ed35-4720-9058-c143f02f8586",
  "isSidechain": false,
  "requestId": "req_011CbUoAPiCGg42f68kTHo7z",
  "type": "assistant",
  "uuid": "a91749e1-c5a7-4f0c-a41a-3e9d1434cc20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHFDcT4YRJ5RBTfL8K9UoA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19565,
      "cache_read_input_tokens": 16834,
      "output_tokens": 2631,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19565,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2631,
          "cache_read_input_tokens": 16834,
          "cache_creation_input_tokens": 19565,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19565
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

_source line 36 · 2026-05-28T10:19:43.250Z_

<details><summary>↩ Tool result · `toolu_0165wNrPVD7JXt5PVzEZDeyp`</summary>

```text
# Paper Summary: Provable Joint Decontamination for Benchmarking Multiple LLMs

**Full Title:** "Provable Joint Decontamination for Benchmarking Multiple Large Language Models"

**Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei

**Venue:** arXiv Computer Science - Machine Learning (cs.LG)

## What It Proposes

The paper addresses benchmark contamination in LLM evaluation, where test data inadvertently appears in training sets, inflating performance scores and distorting model comparisons.

The authors introduce **Joint Envelope Conformal Selection (JECS)**, a conformal inference method that:

- Computes per-model contamination scores and aggregates them across all models being evaluated
- Applies the adaptive Benjamini-Hochberg procedure to identify and remove contaminated examples
- Provides "provable global contamination rate (GCR) control" rather than model-specific thresholds

This enables fairer cross-model comparison by applying a unified decontamination standard. According to the abstract, JECS "achieves higher power than the max-p baseline while consistently maintaining the target GCR control," demonstrating effectiveness across various benchmarks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34ea385c-1753-466f-82d3-4a513ad13948",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "c2d3353d-ba1b-4eac-ad0d-82e706c27fb2",
  "toolUseResult": {
    "bytes": 47172,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Provable Joint Decontamination for Benchmarking Multiple LLMs\n\n**Full Title:** \"Provable Joint Decontamination for Benchmarking Multiple Large Language Models\"\n\n**Authors:** Zhenlong Liu, Hao Zeng, Hongxin Wei\n\n**Venue:** arXiv Computer Science - Machine Learning (cs.LG)\n\n## What It Proposes\n\nThe paper addresses benchmark contamination in LLM evaluation, where test data inadvertently appears in training sets, inflating performance scores and distorting model comparisons.\n\nThe authors introduce **Joint Envelope Conformal Selection (JECS)**, a conformal inference method that:\n\n- Computes per-model contamination scores and aggregates them across all models being evaluated\n- Applies the adaptive Benjamini-Hochberg procedure to identify and remove contaminated examples\n- Provides \"provable global contamination rate (GCR) control\" rather than model-specific thresholds\n\nThis enables fairer cross-model comparison by applying a unified decontamination standard. According to the abstract, JECS \"achieves higher power than the max-p baseline while consistently maintaining the target GCR control,\" demonstrating effectiveness across various benchmarks.",
    "durationMs": 4011,
    "url": "https://arxiv.org/abs/2605.21543"
  },
  "sourceToolAssistantUUID": "34ea385c-1753-466f-82d3-4a513ad13948",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-28T10:19:43.397Z_

<details><summary>↩ Tool result · `toolu_016qHu5REWVLHhPKyDdGYEe8`</summary>

```text
# Paper Summary

**Full Title:**
"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory"

**Authors:**
Hongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, and Tiejun Zhao

**Abstract:**
"The evaluation of large language models (LLMs) via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities." The authors propose an enhanced framework and analyze 11 LLM benchmarks containing approximately 42,000 items to identify measurement quality issues. They demonstrate their approach can create smaller benchmarks while better aligning with human judgment.

**AAAI 2026 Acceptance:**
Yes, the paper was "Accepted to AAAI 2026 (Oral)."

**What PSN-IRT Does:**
The Pseudo-Siamese Network for Item Response Theory framework "incorporates a rich set of item parameters within an IRT-grounded architecture" to provide accurate estimations of both item characteristics and model capabilities for benchmark evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50b07410-9897-413d-aa38-6b7eb17669e0",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "99e82033-7dee-46e0-bd5f-5f29ecf3436e",
  "toolUseResult": {
    "bytes": 47382,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Full Title:**\n\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\"\n\n**Authors:**\nHongli Zhou, Hui Huang, Ziqing Zhao, Lvyuan Han, Huicheng Wang, Kehai Chen, Muyun Yang, Wei Bao, Jian Dong, Bing Xu, Conghui Zhu, Hailong Cao, and Tiejun Zhao\n\n**Abstract:**\n\"The evaluation of large language models (LLMs) via benchmarks is widespread, yet inconsistencies between different leaderboards and poor separability among top models raise concerns about their ability to accurately reflect authentic model capabilities.\" The authors propose an enhanced framework and analyze 11 LLM benchmarks containing approximately 42,000 items to identify measurement quality issues. They demonstrate their approach can create smaller benchmarks while better aligning with human judgment.\n\n**AAAI 2026 Acceptance:**\nYes, the paper was \"Accepted to AAAI 2026 (Oral).\"\n\n**What PSN-IRT Does:**\nThe Pseudo-Siamese Network for Item Response Theory framework \"incorporates a rich set of item parameters within an IRT-grounded architecture\" to provide accurate estimations of both item characteristics and model capabilities for benchmark evaluation.",
    "durationMs": 5298,
    "url": "https://arxiv.org/abs/2505.15055"
  },
  "sourceToolAssistantUUID": "50b07410-9897-413d-aa38-6b7eb17669e0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-28T10:19:44.804Z_

<details><summary>↩ Tool result · `toolu_012H4ssEttYEvyyuTmm6DNqC`</summary>

```text
# Latency-Response Theory Model (LaRT)

**Full Title:** "Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length"

**Authors:** Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu

**Abstract Summary:**
LaRT is a statistical framework designed to assess LLMs by jointly analyzing two key dimensions: answer correctness and the length of reasoning chains. The model introduces latent ability and latent speed parameters, plus a correlation measure between them. Key findings show strong negative correlations between reasoning capability and response speed across benchmarks.

**Functionality:**
The method enhances traditional Item Response Theory by incorporating chain-of-thought length as an additional evaluation signal. Testing on real LLM responses demonstrates that LaRT produces superior estimation accuracy, tighter confidence intervals, and more valid model rankings compared to IRT alone.

**Publication Status:**
This is a preprint hosted on arXiv (identifier 2512.07019) submitted December 7, 2025, with a revision on December 11, 2025. It appears in the Statistics > Methodology category but shows no indication of peer-reviewed venue acceptance yet. Code and data are publicly available on GitHub.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "df61f82b-ed35-4720-9058-c143f02f8586",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "4e15e89a-6a53-45f1-81d7-4ba9f0244038",
  "toolUseResult": {
    "bytes": 49019,
    "code": 200,
    "codeText": "OK",
    "result": "# Latency-Response Theory Model (LaRT)\n\n**Full Title:** \"Latency-Response Theory Model: Evaluating Large Language Models via Response Accuracy and Chain-of-Thought Length\"\n\n**Authors:** Zhiyu Xu, Jia Liu, Yixin Wang, Yuqi Gu\n\n**Abstract Summary:**\nLaRT is a statistical framework designed to assess LLMs by jointly analyzing two key dimensions: answer correctness and the length of reasoning chains. The model introduces latent ability and latent speed parameters, plus a correlation measure between them. Key findings show strong negative correlations between reasoning capability and response speed across benchmarks.\n\n**Functionality:**\nThe method enhances traditional Item Response Theory by incorporating chain-of-thought length as an additional evaluation signal. Testing on real LLM responses demonstrates that LaRT produces superior estimation accuracy, tighter confidence intervals, and more valid model rankings compared to IRT alone.\n\n**Publication Status:**\nThis is a preprint hosted on arXiv (identifier 2512.07019) submitted December 7, 2025, with a revision on December 11, 2025. It appears in the Statistics > Methodology category but shows no indication of peer-reviewed venue acceptance yet. Code and data are publicly available on GitHub.",
    "durationMs": 4619,
    "url": "https://arxiv.org/abs/2512.07019"
  },
  "sourceToolAssistantUUID": "df61f82b-ed35-4720-9058-c143f02f8586",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-28T10:19:46.121Z_

<details><summary>↩ Tool result · `toolu_011yK2UqmKpH5x9y3VvqBNUU`</summary>

```text
# Paper Summary

**Full Title:** "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"

**Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang

**Abstract:** The research critically examines whether Reinforcement Learning with Verifiable Rewards (RLVR) truly develops novel reasoning abilities in language models. Using pass@k metrics across benchmarks, the authors found that "the current training setup does not elicit fundamentally new reasoning patterns." While RLVR models outperform base models at k=1, base models score higher at larger k values, suggesting improvements stem from existing capabilities rather than genuinely new reasoning. The study indicates distillation can introduce novel patterns, whereas current RLVR methods remain suboptimal.

**NeurIPS 2025 Status:** This is an **oral presentation** at NeurIPS 2025 and best paper winner at ICML 2025's AI4MATH workshop—indicating recognition as a strong contribution, though not specifically labeled a "runner-up."

**Key Finding on RL and Reasoning:** Current RL approaches don't unlock fundamentally new reasoning abilities; they better leverage existing base model capabilities. The researchers advocate for improved paradigms like continual scaling and multi-turn interactions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a91749e1-c5a7-4f0c-a41a-3e9d1434cc20",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "4c644d10-b91a-4ac4-a1f0-f9f72440cf72",
  "toolUseResult": {
    "bytes": 48797,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary\n\n**Full Title:** \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\"\n\n**Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang\n\n**Abstract:** The research critically examines whether Reinforcement Learning with Verifiable Rewards (RLVR) truly develops novel reasoning abilities in language models. Using pass@k metrics across benchmarks, the authors found that \"the current training setup does not elicit fundamentally new reasoning patterns.\" While RLVR models outperform base models at k=1, base models score higher at larger k values, suggesting improvements stem from existing capabilities rather than genuinely new reasoning. The study indicates distillation can introduce novel patterns, whereas current RLVR methods remain suboptimal.\n\n**NeurIPS 2025 Status:** This is an **oral presentation** at NeurIPS 2025 and best paper winner at ICML 2025's AI4MATH workshop—indicating recognition as a strong contribution, though not specifically labeled a \"runner-up.\"\n\n**Key Finding on RL and Reasoning:** Current RL approaches don't unlock fundamentally new reasoning abilities; they better leverage existing base model capabilities. The researchers advocate for improved paradigms like continual scaling and multi-turn interactions.",
    "durationMs": 4952,
    "url": "https://arxiv.org/abs/2504.13837"
  },
  "sourceToolAssistantUUID": "a91749e1-c5a7-4f0c-a41a-3e9d1434cc20",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 40 · 2026-05-28T10:19:46.135Z_

```json
{
  "parentUuid": "4c644d10-b91a-4ac4-a1f0-f9f72440cf72",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1a775f0c-49bc-4a04-8ba5-b11aef3a345b",
  "timestamp": "2026-05-28T10:19:46.135Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-28 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "1a775f0c-49bc-4a04-8ba5-b11aef3a345b",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers for contamination-aware reasoning evaluation",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Assistant

_source line 43 · 2026-05-28T10:20:01.337Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've verified the key papers. Now let me also verify a couple more that I want to include:

1. GSM-Symbolic - very well known, ICLR 2025
2. ReasoningMath-Plus - seed paper
3. MaSTer - seed paper

Let me also search for a few more papers that might be missing, particularly around:
- The Generalization or Memorization paper (Dong et al., ACL 2024) 
- The contamination survey from EMNLP 2025

Actually, I have enough information. Let me compile the final list of 15+ papers now.


Now I'm organizing the papers by their relevance to the CRADE framework, prioritizing those from top venues and with the strongest connections to contamination, perturbation, step-level reasoning, and IRT. I'll structure this around the four pillars, starting with contamination detection and correction, then moving into adversarial robustness and the remaining areas. Continuing through the remaining pillars—step-level reasoning evaluation with faithfulness benchmarks and process verification, then moving into psychometric approaches using item response theory for adaptive testing, and finally cross-cutting evaluation frameworks that address contamination and whether reinforcement learning actually improves genuine reasoning capabilities rather than just surface-level metrics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a775f0c-49bc-4a04-8ba5-b11aef3a345b",
  "isSidechain": false,
  "requestId": "req_011CbUoDukYvQuNDS6GCzZTz",
  "type": "assistant",
  "uuid": "95ad1fbc-1588-4af8-9520-e428ec0876ce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeSXxRWaArbP3xdghmSQhP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4014,
      "cache_read_input_tokens": 36399,
      "output_tokens": 1208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4014,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1208,
          "cache_read_input_tokens": 36399,
          "cache_creation_input_tokens": 4014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4014
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

_source line 44 · 2026-05-28T10:20:01.339Z_

Now let me verify a couple more seed papers to ensure accuracy:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95ad1fbc-1588-4af8-9520-e428ec0876ce",
  "isSidechain": false,
  "requestId": "req_011CbUoDukYvQuNDS6GCzZTz",
  "type": "assistant",
  "uuid": "ddcd6008-0702-4482-b459-cd13977ade30",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeSXxRWaArbP3xdghmSQhP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4014,
      "cache_read_input_tokens": 36399,
      "output_tokens": 1208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4014,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1208,
          "cache_read_input_tokens": 36399,
          "cache_creation_input_tokens": 4014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4014
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

_source line 45 · 2026-05-28T10:20:02.332Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01S4WPA67XGrJpkRqy3QFAYR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2506.05038",
  "prompt": "Extract the full title, authors, abstract of MaSTer. What venue is it published at? What does it do for adversarial math variant generation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddcd6008-0702-4482-b459-cd13977ade30",
  "isSidechain": false,
  "requestId": "req_011CbUoDukYvQuNDS6GCzZTz",
  "type": "assistant",
  "uuid": "19a44507-c600-4888-af82-dcdc8c81efc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeSXxRWaArbP3xdghmSQhP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4014,
      "cache_read_input_tokens": 36399,
      "output_tokens": 1208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4014,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1208,
          "cache_read_input_tokens": 36399,
          "cache_creation_input_tokens": 4014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4014
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

_source line 46 · 2026-05-28T10:20:03.393Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FiYLdz9TeAi2HRrQ6Cr1so`</summary>

```json
{
  "url": "https://arxiv.org/abs/2502.06453",
  "prompt": "Extract the full title, authors, abstract of MATH-Perturb. What venue? What perturbation approach does it use?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19a44507-c600-4888-af82-dcdc8c81efc3",
  "isSidechain": false,
  "requestId": "req_011CbUoDukYvQuNDS6GCzZTz",
  "type": "assistant",
  "uuid": "6f888de7-f88b-48c3-bc9e-a86f5430bf86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeSXxRWaArbP3xdghmSQhP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4014,
      "cache_read_input_tokens": 36399,
      "output_tokens": 1208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4014,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1208,
          "cache_read_input_tokens": 36399,
          "cache_creation_input_tokens": 4014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4014
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

_source line 47 · 2026-05-28T10:20:04.209Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013TbuqoCW4saY7Bz844A6aW`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.05229",
  "prompt": "Extract the full title, authors, abstract of GSM-Symbolic. Is it accepted at ICLR 2025? How many citations does it have?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f888de7-f88b-48c3-bc9e-a86f5430bf86",
  "isSidechain": false,
  "requestId": "req_011CbUoDukYvQuNDS6GCzZTz",
  "type": "assistant",
  "uuid": "e8a8433b-c568-4b72-ae5f-91243fcce567",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KeSXxRWaArbP3xdghmSQhP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4014,
      "cache_read_input_tokens": 36399,
      "output_tokens": 1208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4014,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1208,
          "cache_read_input_tokens": 36399,
          "cache_creation_input_tokens": 4014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4014
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

_source line 48 · 2026-05-28T10:20:07.013Z_

<details><summary>↩ Tool result · `toolu_01S4WPA67XGrJpkRqy3QFAYR`</summary>

```text
# MaSTer: Automated Robustness Evaluation Framework

**Full Title:** "Toward Automated Robustness Evaluation of Mathematical Reasoning"

**Authors:** Yutao Hou, Zeguan Xiao, Fei Yu, Yihan Jiang, Ma Shuguang, Zhaoqian Dai, Hailiang Huang, Yun Chen, and Guanhua Chen

**Venue:** Findings of ACL 2026

**Abstract Summary:**
The paper addresses brittleness in Large Language Models on mathematical reasoning tasks. MaSTer is described as "an automated framework inspired by software stress testing" that "generates adversarial variants via a multi-round rewrite-verify loop, ensuring semantic consistency while successfully inducing model failure."

**Adversarial Variant Generation Approach:**
MaSTer employs an iterative methodology where it creates problem variants dynamically for each specific model. This approach aims to maintain semantic equivalence to original problems while triggering model failures. The framework additionally demonstrates that its generated variants can serve as training data to improve model robustness on mathematical benchmarks like GSM8K and MATH-500.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19a44507-c600-4888-af82-dcdc8c81efc3",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "b1aa68e5-124d-4cc8-a73c-1fe367e80edd",
  "toolUseResult": {
    "bytes": 47090,
    "code": 200,
    "codeText": "OK",
    "result": "# MaSTer: Automated Robustness Evaluation Framework\n\n**Full Title:** \"Toward Automated Robustness Evaluation of Mathematical Reasoning\"\n\n**Authors:** Yutao Hou, Zeguan Xiao, Fei Yu, Yihan Jiang, Ma Shuguang, Zhaoqian Dai, Hailiang Huang, Yun Chen, and Guanhua Chen\n\n**Venue:** Findings of ACL 2026\n\n**Abstract Summary:**\nThe paper addresses brittleness in Large Language Models on mathematical reasoning tasks. MaSTer is described as \"an automated framework inspired by software stress testing\" that \"generates adversarial variants via a multi-round rewrite-verify loop, ensuring semantic consistency while successfully inducing model failure.\"\n\n**Adversarial Variant Generation Approach:**\nMaSTer employs an iterative methodology where it creates problem variants dynamically for each specific model. This approach aims to maintain semantic equivalence to original problems while triggering model failures. The framework additionally demonstrates that its generated variants can serve as training data to improve model robustness on mathematical benchmarks like GSM8K and MATH-500.",
    "durationMs": 4673,
    "url": "https://arxiv.org/abs/2506.05038"
  },
  "sourceToolAssistantUUID": "19a44507-c600-4888-af82-dcdc8c81efc3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-28T10:20:09.103Z_

<details><summary>↩ Tool result · `toolu_013TbuqoCW4saY7Bz844A6aW`</summary>

```text
# GSM-Symbolic Paper Summary

**Full Title:**
"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models"

**Authors:**
Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar

**Abstract:**
The researchers developed GSM-Symbolic, a benchmark using symbolic templates to evaluate LLM mathematical reasoning more rigorously than the standard GSM8K dataset. Their study reveals that "LLMs exhibit noticeable variance when responding to different instantiations of the same question" and that performance declines significantly with numerical changes. They also found that adding irrelevant clauses to questions caused performance drops of up to 65%, suggesting LLMs may not perform genuine logical reasoning but rather replicate patterns from training data.

**ICLR 2025 Status:**
The submission history indicates this is "ICLR camera ready," suggesting it was accepted. The latest version (v2) was posted on August 27, 2025, after the initial October 2024 submission.

**Citation Count:**
The webpage provided does not display citation metrics, so I cannot determine the current citation count from this content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e8a8433b-c568-4b72-ae5f-91243fcce567",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "d640719b-5bd1-4324-8689-f1f9af3197ca",
  "toolUseResult": {
    "bytes": 50143,
    "code": 200,
    "codeText": "OK",
    "result": "# GSM-Symbolic Paper Summary\n\n**Full Title:**\n\"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\"\n\n**Authors:**\nIman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar\n\n**Abstract:**\nThe researchers developed GSM-Symbolic, a benchmark using symbolic templates to evaluate LLM mathematical reasoning more rigorously than the standard GSM8K dataset. Their study reveals that \"LLMs exhibit noticeable variance when responding to different instantiations of the same question\" and that performance declines significantly with numerical changes. They also found that adding irrelevant clauses to questions caused performance drops of up to 65%, suggesting LLMs may not perform genuine logical reasoning but rather replicate patterns from training data.\n\n**ICLR 2025 Status:**\nThe submission history indicates this is \"ICLR camera ready,\" suggesting it was accepted. The latest version (v2) was posted on August 27, 2025, after the initial October 2024 submission.\n\n**Citation Count:**\nThe webpage provided does not display citation metrics, so I cannot determine the current citation count from this content.",
    "durationMs": 4890,
    "url": "https://arxiv.org/abs/2410.05229"
  },
  "sourceToolAssistantUUID": "e8a8433b-c568-4b72-ae5f-91243fcce567",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-28T10:20:09.174Z_

<details><summary>↩ Tool result · `toolu_01FiYLdz9TeAi2HRrQ6Cr1so`</summary>

```text
# MATH-Perturb Paper Summary

**Full Title:**
"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations"

**Authors:**
Kaixuan Huang, Jiacheng Guo, Zihao Li, Xiang Ji, Jiawei Ge, Wenzhe Li, Yingqing Guo, Tianle Cai, Hui Yuan, Runzhe Wang, Yue Wu, Ming Yin, Shange Tang, Yangsibo Huang, Chi Jin, Xinyun Chen, Chiyuan Zhang, and Mengdi Wang

**Abstract:**
The researchers investigate whether LLMs achieve strong mathematical performance through genuine reasoning or memorization. They constructed two benchmark datasets with 279 perturbed problems from the MATH dataset's hardest tier: one with simple modifications preserving solution patterns, and another with fundamental changes that invalidate original approaches. Testing revealed substantial accuracy declines (o1-mini dropped 16.49%) on the harder variants, and the team identified a concerning memorization pattern where models mechanically apply learned techniques without verifying their relevance to modified contexts.

**Venue:**
Not explicitly specified in the provided content; classified under Computer Science > Machine Learning (cs.LG)

**Perturbation Approach:**
The study employs two complementary perturbation strategies: "simple perturbation" (preserving underlying reasoning patterns) and "hard perturbation" (fundamentally altering problem nature so original solution steps don't apply).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f888de7-f88b-48c3-bc9e-a86f5430bf86",
  "isSidechain": false,
  "promptId": "15bf4f26-279f-4227-a1c7-7a9bd491bc37",
  "type": "user",
  "uuid": "8a1cad57-c159-4011-abab-0aa180a976ee",
  "toolUseResult": {
    "bytes": 50270,
    "code": 200,
    "codeText": "OK",
    "result": "# MATH-Perturb Paper Summary\n\n**Full Title:**\n\"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\"\n\n**Authors:**\nKaixuan Huang, Jiacheng Guo, Zihao Li, Xiang Ji, Jiawei Ge, Wenzhe Li, Yingqing Guo, Tianle Cai, Hui Yuan, Runzhe Wang, Yue Wu, Ming Yin, Shange Tang, Yangsibo Huang, Chi Jin, Xinyun Chen, Chiyuan Zhang, and Mengdi Wang\n\n**Abstract:**\nThe researchers investigate whether LLMs achieve strong mathematical performance through genuine reasoning or memorization. They constructed two benchmark datasets with 279 perturbed problems from the MATH dataset's hardest tier: one with simple modifications preserving solution patterns, and another with fundamental changes that invalidate original approaches. Testing revealed substantial accuracy declines (o1-mini dropped 16.49%) on the harder variants, and the team identified a concerning memorization pattern where models mechanically apply learned techniques without verifying their relevance to modified contexts.\n\n**Venue:**\nNot explicitly specified in the provided content; classified under Computer Science > Machine Learning (cs.LG)\n\n**Perturbation Approach:**\nThe study employs two complementary perturbation strategies: \"simple perturbation\" (preserving underlying reasoning patterns) and \"hard perturbation\" (fundamentally altering problem nature so original solution steps don't apply).",
    "durationMs": 5777,
    "url": "https://arxiv.org/abs/2502.06453"
  },
  "sourceToolAssistantUUID": "6f888de7-f88b-48c3-bc9e-a86f5430bf86",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-28T10:20:21.953Z_

<details><summary>Logged reasoning block</summary>

```text
Great, now I have all the information I need. Let me compile the final JSON array with 18 papers (15 core + 3 bonus highly relevant ones).

Let me finalize the list:

1. **GSM-Symbolic** (Mirzadeh et al., ICLR 2025) - Defining perturbation robustness work
2. **PSN-IRT** (Zhou et al., AAAI 2026 Oral) - IRT for LLM eval
3. **CoDeC** (Zawalski et al., ICLR 2026) - Gray-box contamination detection


4. **Fragility of Detection** (Wang et al., ICLR 2026) - Detection fails for reasoning models
5. **DCR** (Xu et al., EMNLP 2025) - Contamination-adjusted scores
6. **Reasoning Models Don't Always Say What They Think** (Chen et al., Anthropic 2025) - CoT unfaithfulness
7. **ReasonEval** (Xia et al., AAAI 2025 Oral) - Step-level math eval
8. **FaithCoT-Bench** (Shen et al.) - Continuing through the remaining papers...

I'm working through a collection of recent papers on reasoning evaluation, contamination detection, and benchmark design. The list covers approaches like process verification with PAVs, adaptive testing frameworks using item response theory, contamination-free benchmarks like LiveBench, and various methods for generating adversarial variants and ensuring decontamination. There are also papers examining whether reinforcement learning actually improves genuine reasoning capabilities versus surface-level performance.

Now I'm double-checking the exact venues for some of these papers since a few were listed as arXiv preprints but may have been accepted to conferences—I want to make sure I have the correct publication status for MaSTer, CoDeC, and the Wang et al. fragility paper before finalizing the list.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a1cad57-c159-4011-abab-0aa180a976ee",
  "isSidechain": false,
  "requestId": "req_011CbUoFcN61CmJioUbJh2iA",
  "type": "assistant",
  "uuid": "bc254422-bf6b-4982-afd6-b6676449114e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1jS3ccmVct2ri5fdw3wqm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 320,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 40413,
      "output_tokens": 5559,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 320,
          "output_tokens": 5559,
          "cache_read_input_tokens": 40413,
          "cache_creation_input_tokens": 1883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1883
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

_source line 52 · 2026-05-28T10:21:40.565Z_

Excellent. I now have comprehensive data from all search agents and verification fetches. Let me compile the final results.

---

## Comprehensive Literature Survey for CRADE (AAAI 2026)

Below are the **18 most important recent papers** (2024–2026) directly relevant to the CRADE framework, organized across its four pillars: contamination detection/correction, adversarial robustness, step-level reasoning evaluation, and IRT-based calibrated scoring—plus cross-cutting evaluation framework papers.

---

### Pillar 1 — Contamination Detection & Score Correction

**1. CoDeC** — Accepted at ICLR 2026. Gray-box detection measuring how in-context examples affect model confidence on seen vs. unseen data. Your proposed detection backbone; produces per-instance contamination profiles but no corrective evaluation.

**2. On The Fragility of Benchmark Contamination Detection in Reasoning Models** — Accepted at ICLR 2026. Shows RL training (GRPO) after SFT contamination conceals memorization signals, making all existing detection methods perform at random-guess level on reasoning models. The key negative result motivating CRADE's process-level alternatives.

**3. DCR: Quantifying Data Contamination in LLMs Evaluation** — EMNLP 2025. Detects contamination at four granular levels and synthesizes via fuzzy inference into a contamination-adjusted score (within 4% average error). Closest competitor to CRADE but lacks IRT grounding, variant generation, and process-level analysis.

**4. JECS: Provable Joint Decontamination for Benchmarking Multiple LLMs** — arXiv May 2026. Conformal-inference method for multi-model decontamination with provable global contamination rate control. Provides the statistical decontamination counterpart CRADE could build upon.

### Pillar 2 — Adversarial Robustness & Perturbation

**5. GSM-Symbolic** — ICLR 2025 (Apple). The landmark paper: symbolic templates over GSM8K showing that merely changing numeric values degrades LLM performance by up to 65%. Defines the perturbation-based robustness evaluation paradigm. Highly cited (300+ citations in ~1 year).

**6. MATH-Perturb** — arXiv Feb 2025 (Princeton/Google DeepMind). Targets the hardest MATH-500 tier with "simple" (structure-preserving) and "hard" (structure-breaking) perturbations. o1-mini drops 16.5%. Identifies mechanistic memorization where models apply techniques without checking applicability.

**7. MaSTer** — Findings of ACL 2026. Multi-round rewrite-verify loop generating adversarial variants; achieves 48% accuracy reduction on GSM8K and 31% on MATH-500. Best current automated perturbation method but disconnected from contamination measurement.

### Pillar 3 — Step-Level Reasoning & CoT Faithfulness

**8. Reasoning Models Don't Always Say What They Think** — Anthropic Technical Report, May 2025. Models acknowledge hint usage only 1–20% of the time even when hints demonstrably change answers. Foundational result establishing CoT monitoring is insufficient. Evaluated Claude 3.7 Sonnet and DeepSeek R1.

**9. FaithCoT-Bench** — ICLR 2026. First comprehensive instance-level CoT faithfulness benchmark with 1,000+ expert-annotated trajectories and step-level unfaithfulness evidence. Evaluates 11 detection methods; finds detection difficulty increases with model sophistication.

**10. ReasonEval: Evaluating Mathematical Reasoning Beyond Accuracy** — AAAI 2025 (Oral). Formalizes step-level validity (no errors) and redundancy (unnecessary steps) as quality metrics. Key finding: improved final-answer accuracy on hard problems doesn't mean better step-level reasoning. Directly relevant to CRADE's process-level component.

**11. Rewarding Progress: Scaling Automated Process Verifiers (PAVs)** — ICLR 2025 (Spotlight, Google DeepMind). Redefines process rewards as "progress" (change in correct-answer likelihood before/after a step). 8%+ accuracy gains over outcome reward models. Foundation for scalable step-level verification.

**12. ReasoningMath-Plus** — arXiv Jan 2026. 150-problem benchmark with annotated minimal reasoning skeletons and HCRS scoring that penalizes earlier errors more heavily. Best models score 5.8/10 on answers but only 5.14/10 on process-aware evaluation (~15% overestimation gap).

### Pillar 4 — IRT & Psychometrics for LLM Evaluation

**13. PSN-IRT: Lost in Benchmarks? Rethinking LLM Benchmarking with IRT** — AAAI 2026 (Oral). Enhanced IRT framework analyzing 11 benchmarks (~42K items); reveals significant measurement quality shortcomings; connects high IRT guessing parameters to potential contamination. At the same venue as CRADE.

**14. ATLAS: Adaptive Testing for LLM Evaluation** — arXiv 2025. First large-scale IRT adaptive testing framework for LLMs; reduces items by 90% while maintaining precision. Achieves natural contamination resistance through <10% item exposure. Demonstrates IRT's power but assumes test integrity.

**15. LaRT: Latency-Response Theory Model** — arXiv Dec 2025. Extends IRT by jointly modeling response correctness and CoT length, introducing latent ability-speed correlation. Directly relevant: anomalously short CoT on contaminated items could distinguish memorization from genuine reasoning.

### Cross-Cutting — Evaluation Frameworks & Capability Measurement

**16. LiveBench** — ICLR 2025 (Spotlight). Dynamic benchmark with monthly-updated questions from recent sources, scored against objective ground truth. Top models below 70%. The primary contamination-free evaluation baseline.

**17. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?** — NeurIPS 2025 (Oral) + ICML 2025 AI4MATH Workshop Best Paper. RLVR models outperform at greedy decoding but base models achieve higher pass@k at large k—RL biases distribution without expanding reasoning boundary. Directly relevant: standard metrics overstate genuine capability.

**18. Generalization or Memorization: Data Contamination and Trustworthy Evaluation for LLMs** — ACL 2024. CDD detects contamination via output distribution peakedness; TED mitigates effects, reducing contamination-related gains by 66.9%. Early unified detection+correction approach.

---

```json
[
  {
    "title": "CoDeC: Detecting Data Contamination in LLMs via In-Context Learning",
    "authors": "Zawalski et al.",
    "venue": "ICLR 2026",
    "url": "https://arxiv.org/abs/2510.27055",
    "why_important": "Accepted at ICLR 2026; gray-box contamination detection achieving 99.9% AUC; model- and dataset-agnostic; proposed detection backbone for CRADE",
    "one_line_summary": "Measures how in-context examples differentially affect model confidence on memorized vs. unseen data to produce per-instance contamination scores."
  },
  {
    "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
    "authors": "Wang et al.",
    "venue": "ICLR 2026",
    "url": "https://arxiv.org/abs/2510.02386",
    "why_important": "Accepted at ICLR 2026; critical negative result showing RL training conceals memorization signals, making all existing detection methods perform at random-guess on reasoning models",
    "one_line_summary": "Demonstrates that GRPO-based RL training after SFT contamination renders all current contamination detection methods ineffective for reasoning models."
  },
  {
    "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
    "authors": "Xu et al.",
    "venue": "EMNLP 2025",
    "url": "https://aclanthology.org/2025.emnlp-main.1173/",
    "why_important": "Published at EMNLP 2025; only existing framework producing contamination-adjusted benchmark scores; closest competitor to CRADE but lacks IRT grounding and process-level analysis",
    "one_line_summary": "Detects contamination at four granularity levels and synthesizes them via fuzzy inference into a single correction factor that adjusts raw accuracy scores."
  },
  {
    "title": "Provable Joint Decontamination for Benchmarking Multiple Large Language Models (JECS)",
    "authors": "Liu et al.",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2605.21543",
    "why_important": "First provably correct multi-model decontamination method with formal global contamination rate control via conformal inference",
    "one_line_summary": "Uses conformal p-values and adaptive Benjamini-Hochberg to identify and remove contaminated benchmark items across multiple models with statistical guarantees."
  },
  {
    "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models",
    "authors": "Mirzadeh et al.",
    "venue": "ICLR 2025",
    "url": "https://arxiv.org/abs/2410.05229",
    "why_important": "ICLR 2025 (Apple); highly cited (300+ in ~1 year); defines the perturbation-based robustness evaluation paradigm; showed up to 65% performance drop from adding irrelevant clauses",
    "one_line_summary": "Uses symbolic templates to generate numeric/lexical variants of GSM8K problems, revealing that LLMs replicate training patterns rather than performing genuine mathematical reasoning."
  },
  {
    "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
    "authors": "Huang et al.",
    "venue": "arXiv 2025 (Princeton / Google DeepMind)",
    "url": "https://arxiv.org/abs/2502.06453",
    "why_important": "Targets competition-level math (hardest MATH-500 tier); introduces dual simple/hard perturbation taxonomy; identifies memorization-driven mechanical technique application",
    "one_line_summary": "Constructs structure-preserving and structure-breaking perturbations of the hardest MATH problems, showing o1-mini drops 16.5% and models mechanically apply memorized techniques."
  },
  {
    "title": "MaSTer: Toward Automated Robustness Evaluation of Mathematical Reasoning",
    "authors": "Hou et al.",
    "venue": "Findings of ACL 2026",
    "url": "https://arxiv.org/abs/2506.05038",
    "why_important": "Best current automated perturbation method; achieves 48% accuracy reduction on GSM8K variants; accepted at ACL 2026 Findings",
    "one_line_summary": "An automated stress-testing framework that generates adversarial math variants via a multi-round rewrite-verify loop while preserving semantic consistency."
  },
  {
    "title": "Reasoning Models Don't Always Say What They Think",
    "authors": "Chen et al.",
    "venue": "Anthropic Technical Report, May 2025",
    "url": "https://arxiv.org/abs/2505.05410",
    "why_important": "Foundational result from Anthropic establishing CoT unfaithfulness (1-20% hint disclosure rate); widely cited; evaluated on Claude 3.7 Sonnet and DeepSeek R1",
    "one_line_summary": "Tests CoT faithfulness by planting hints in evaluation problems, finding that reasoning models verbalize hint usage only 1-20% of the time even when hints demonstrably change answers."
  },
  {
    "title": "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning",
    "authors": "Shen et al.",
    "venue": "ICLR 2026",
    "url": "https://arxiv.org/abs/2510.04040",
    "why_important": "ICLR 2026; first comprehensive instance-level CoT faithfulness benchmark with 1,000+ expert-annotated trajectories and step-level cause annotations",
    "one_line_summary": "Provides the first systematic benchmark for detecting instance-level CoT unfaithfulness, evaluating 11 detection methods across four major LLMs."
  },
  {
    "title": "Evaluating Mathematical Reasoning Beyond Accuracy (ReasonEval)",
    "authors": "Xia et al.",
    "venue": "AAAI 2025 (Oral)",
    "url": "https://arxiv.org/abs/2404.05692",
    "why_important": "AAAI 2025 Oral; first to formalize step-level validity and redundancy metrics for math reasoning; shows final-answer accuracy masks process deficiencies",
    "one_line_summary": "Introduces a framework measuring reasoning quality through step-level validity and redundancy, showing improved accuracy doesn't necessarily mean better step-level reasoning."
  },
  {
    "title": "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (PAVs)",
    "authors": "Setlur et al.",
    "venue": "ICLR 2025 (Spotlight)",
    "url": "https://arxiv.org/abs/2410.08146",
    "why_important": "ICLR 2025 Spotlight (Google DeepMind); establishes theoretical and practical foundation for scalable process verification; 8%+ accuracy gains over outcome reward models",
    "one_line_summary": "Redefines process rewards as the change in correct-answer likelihood before vs. after a reasoning step, achieving superior accuracy and compute efficiency for step-level verification."
  },
  {
    "title": "Unmasking Reasoning Processes: A Process-aware Benchmark for Evaluating Structural Mathematical Reasoning in LLMs (ReasoningMath-Plus)",
    "authors": "Zheng et al.",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2602.00564",
    "why_important": "Demonstrates ~15% overestimation gap between answer-only and process-aware evaluation; introduces error-position-aware HCRS scoring",
    "one_line_summary": "Introduces a 150-problem benchmark with annotated reasoning skeletons and hazard-aware chain-based scoring, showing answer-level metrics overestimate reasoning quality by ~1.4 points."
  },
  {
    "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory (PSN-IRT)",
    "authors": "Zhou et al.",
    "venue": "AAAI 2026 (Oral)",
    "url": "https://arxiv.org/abs/2505.15055",
    "why_important": "AAAI 2026 Oral (same venue as CRADE target); enhanced IRT framework; connects high guessing parameters to contamination; analyzes 11 benchmarks with ~42K items",
    "one_line_summary": "Proposes PSN-IRT with rich item parameters to diagnose LLM benchmark measurement quality, revealing significant shortcomings and showing IRT-derived smaller benchmarks better align with human preference."
  },
  {
    "title": "ATLAS: Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
    "authors": "Li et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2511.04689",
    "why_important": "First large-scale IRT adaptive testing for LLMs; achieves 90% item reduction; natural contamination resistance through <10% item exposure; calibrated on 3,000+ LMs",
    "one_line_summary": "Uses Fisher information-guided item selection to reduce evaluation to 41 items while maintaining measurement precision, with inherent contamination resistance from low item exposure."
  },
  {
    "title": "LaRT: Latency-Response Theory Model -- Evaluating LLMs via Response Accuracy and Chain-of-Thought Length",
    "authors": "Xu et al.",
    "venue": "arXiv 2025",
    "url": "https://arxiv.org/abs/2512.07019",
    "why_important": "Novel extension of IRT jointly modeling correctness and CoT length; anomalously short CoT could serve as a contamination signal distinguishing memorization from reasoning",
    "one_line_summary": "Extends IRT by jointly modeling response accuracy and chain-of-thought length with latent ability-speed correlation, outperforming standard IRT in ranking validity."
  },
  {
    "title": "LiveBench: A Challenging, Contamination-Limited LLM Benchmark",
    "authors": "White et al.",
    "venue": "ICLR 2025 (Spotlight)",
    "url": "https://arxiv.org/abs/2406.19314",
    "why_important": "ICLR 2025 Spotlight; monthly-updated contamination-free benchmark with objective ground truth; top models below 70%; primary baseline for contamination-free evaluation",
    "one_line_summary": "A dynamic LLM benchmark with frequently-updated questions from recent math competitions, arXiv papers, and news, scored automatically against objective ground truth."
  },
  {
    "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?",
    "authors": "Yue et al.",
    "venue": "NeurIPS 2025 (Oral) + ICML 2025 AI4MATH Workshop Best Paper",
    "url": "https://arxiv.org/abs/2504.13837",
    "why_important": "NeurIPS 2025 Oral + workshop best paper; shows RLVR biases output distribution without expanding reasoning boundary; directly relevant to distinguishing genuine capability from surface metrics",
    "one_line_summary": "Demonstrates that RL with verifiable rewards improves greedy accuracy but doesn't create new reasoning capabilities — base models achieve higher pass@k at large k."
  },
  {
    "title": "Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models",
    "authors": "Dong et al.",
    "venue": "ACL 2024",
    "url": "https://arxiv.org/abs/2402.15938",
    "why_important": "Published at ACL 2024; early unified detection+correction approach; CDD improves detection by 21-30% over prior work; TED reduces contamination-related gains by 66.9%",
    "one_line_summary": "Proposes CDD for contamination detection via output distribution analysis and TED for trustworthy evaluation that mitigates contamination effects without retraining."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc254422-bf6b-4982-afd6-b6676449114e",
  "isSidechain": false,
  "requestId": "req_011CbUoFcN61CmJioUbJh2iA",
  "type": "assistant",
  "uuid": "6a0d7cc1-569e-447b-a2f0-6716d189acef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1jS3ccmVct2ri5fdw3wqm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 320,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 40413,
      "output_tokens": 5559,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1883,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 320,
          "output_tokens": 5559,
          "cache_read_input_tokens": 40413,
          "cache_creation_input_tokens": 1883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1883
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

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-28 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "6a0d7cc1-569e-447b-a2f0-6716d189acef",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers for contamination-aware reasoning evaluation",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-28 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "6a0d7cc1-569e-447b-a2f0-6716d189acef",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Survey 15 key papers for contamination-aware reasoning evaluation",
  "sessionId": "e129977f-c1e3-4a0b-a667-ea67c19c205f"
}
```

---
