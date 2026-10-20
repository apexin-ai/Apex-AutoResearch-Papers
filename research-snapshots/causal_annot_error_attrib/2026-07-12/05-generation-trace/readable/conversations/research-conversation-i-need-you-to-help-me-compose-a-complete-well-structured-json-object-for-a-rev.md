# Research conversation: I need you to help me compose a complete, well-structured JSON object for a revised research idea. I'll provide you with

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 4
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a0660a785004499b3.jsonl`
- **Structured JSON:** [`9d2fc14679443862a44c.json`](../../sessions/9d/9d2fc14679443862a44c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

4 recorded events

### User

_source line 1 · 2026-05-19T19:34:29.783Z_

I need you to help me compose a complete, well-structured JSON object for a revised research idea. I'll provide you with all the context and content — you just need to format it perfectly as a JSON object with proper escaping.

Here is the complete revised research idea content. Please output ONLY the JSON object, nothing else:

{
  "change_type": "major",
  "title": "Cross-Lingual Calibration Transfer via Language-Agnostic Confidence Directions: Navigating the Layer-Depth Pareto Frontier",
  "core_problem": "Non-English languages suffer from 5x worse calibration error (ECE) compared to English in multilingual LLMs. Existing fixes require per-language validation data (LACE) or expensive multilingual sampling (MKA). Can we transfer English calibration quality to underserved languages through shared intermediate-layer confidence directions — and if so, at what layer depth, given the fundamental tradeoff between calibration quality (which peaks at 75-91% depth) and cross-lingual transferability (which peaks at ~50% depth)?",
  "opportunity": "Ji et al. (EMNLP 2025) discovered that verbal uncertainty is governed by a single linear direction in representation space. Joshi et al. (EMNLP 2025) showed calibration evolves across layers with a low-dimensional calibration direction in the residual stream. Zhou et al. (arXiv 2510.03136) introduced LACE, demonstrating that late-intermediate layers encode better-calibrated multilingual signals but requiring per-language validation. Liu & Niehues (ACL 2025) showed that middle layers (~50% depth) form the strongest language-agnostic shared space. Critically, Civelli et al. (arXiv 2601.12731, Jan 2026) demonstrated that linear probes for problem difficulty transfer cross-lingually at shallow-to-intermediate layers (~49% depth) with ~0.78 Spearman rho, while deep probes achieve higher within-language accuracy but fail to transfer — establishing a shallow-transferable vs. deep-accurate tradeoff. The Confidence Manifold (arXiv 2602.08159, Feb 2026) showed correctness signals occupy just 3-8 dimensions and are linearly separable, with 25 labeled examples achieving 89% of full-data probe accuracy. Nobody has tested whether this correctness/calibration probe transfer works cross-lingually, and nobody has mapped the Pareto frontier of layer depth vs. calibration quality vs. cross-lingual transferability — this frontier is the key to practical deployment.",
  "landscape": "Zhou et al. (arXiv 2510.03136) introduced LACE, which adaptively ensembles late-intermediate layers (75-91% depth) per language but still requires per-language validation data, and confirmed the 5x ECE gap across 100+ languages and 6 model families (LLaMA-3: 23.1% vs 4.6% ECE for non-English vs English). MKA (Duwal et al., ICLR Workshop 2025) uses cross-lingual consensus for abstention but at 5x inference cost. Joshi et al. (EMNLP 2025) identified a low-dimensional calibration direction in the residual stream. Civelli et al. (arXiv 2601.12731, Jan 2026) showed cross-lingual probe transfer for problem difficulty at intermediate layers in LLaMA-3.1/3.2 and Qwen3-8B, finding shallow probes (~49% depth) transfer with ~0.78 Spearman rho while deep probes (~94% depth) achieve higher within-language accuracy but exhibit poor cross-lingual generalization (0.05-0.19 rho degradation). However, they probed IRT-based human difficulty — an inherent property of questions — not model correctness, which is a model-dependent property combining difficulty, language-specific capability, and representation quality. CORAL (Miao et al., arXiv 2602.06022, Feb 2026) demonstrates transferable correctness probes via regularized 4-layer MLP on residual activations with ~50% ECE improvement at layers 17-21 (~53-66% depth), but evaluates only in English across tasks and shows degraded transfer on domain-shifted benchmarks (e.g., HellaSwag). The Confidence Manifold (arXiv 2602.08159, Feb 2026) shows correctness signals occupy 3-8 dimensions and are linearly separable across 9 models and 5 architecture families, with few-shot (25 examples) achieving 89% of full-data probe accuracy — all English-only. Cross-lingual steering vectors have been demonstrated for language identity and task performance (Mahmoud et al., arXiv 2505.12584; arXiv 2601.16390) but never for calibration. Instruction-tuning studies (arXiv 2601.01362, Jan 2026) confirm that English-centric fine-tuning inflates confidence in low-resource languages without accuracy gains, worsening calibration. Confidence Geometry Reveals Trace-Level Correctness (arXiv 2605.16824, May 2026) extends geometric correctness analysis to reasoning traces using output-level confidence trajectories — operating at a different level (output tokens, not internal representations) with no multilingual evaluation, but suggesting convergent evidence that correctness has consistent geometric structure. No work has attempted to transfer the correctness/calibration direction itself cross-lingually, and no work has characterized the Pareto frontier between calibration quality and cross-lingual transferability across layer depth.",
  "inspired_by": "Gap: 5x non-English ECE gap (Zhou et al., LACE) + demonstrated cross-lingual difficulty probe transfer at intermediate layers (Civelli et al., Shared Geometry of Difficulty) that has never been extended to correctness/calibration. Pattern: Ji et al.'s linear verbal uncertainty direction + Joshi et al.'s residual-stream calibration direction + Confidence Manifold's 3-8 dimensional correctness signal + cross-lingual middle-layer alignment (Liu & Niehues, ACL 2025). Untried combination: extending representation-space correctness probes from English-only cross-task transfer (CORAL) to cross-lingual calibration transfer, while characterizing the layer-depth Pareto frontier between calibration quality and transferability.",
  "approach": "Phase 1 — Activation Extraction: Extract intermediate-layer activations at every 4th layer across the full depth of Qwen3-235B-A22B (94 layers, MoE), Llama 4 Scout (48 layers, MoE), and Gemma 4 31B Dense (46 layers, dense) on English QA tasks (MMLU, ARC-Challenge) with known correctness labels. Store activations for all layers to enable the Pareto frontier analysis. Phase 2 — English Probe Training: At each extracted layer, fit both a logistic regression probe (linear) and a lightweight 2-layer MLP probe to identify the calibration direction — the hyperplane or surface best separating correct from incorrect answers in representation space. Compare probe complexity: linear probes may transfer better cross-lingually (by analogy to the shallow-transferable finding in Civelli et al.), while MLPs may capture richer correctness signals (as CORAL found). Phase 3 — Pareto Frontier Analysis (Key Novel Contribution): Apply each layer's English-trained probe zero-shot to non-English activations across 50+ languages. For each layer, measure both (a) calibration quality (ECE, Brier score) and (b) cross-lingual transfer quality (AUROC degradation from English). Map the full Pareto frontier of layer depth × calibration quality × cross-lingual transferability. Identify whether there exists a 'sweet spot' layer range that achieves near-optimal calibration with strong cross-lingual transfer, or whether the tradeoff is strict. Phase 4 — Few-Shot Frontier Shifting: Test whether 25-100 non-English examples (motivated by Confidence Manifold's finding that 25 examples achieve 89% of full-data accuracy) can shift the Pareto frontier — specifically, whether few-shot adaptation at deeper layers (where calibration is better but transfer is worse) can recover cross-lingual transfer quality without sacrificing calibration. Phase 5 — Evaluation: Evaluate ECE, Brier score, and AUROC on MMLU-ProX (13 languages, same domain as MMLU training — controls for domain shift), Belebele (122 languages, reading comprehension — tests cross-task + cross-lingual compound transfer), and GlobalMMLU (42 languages, culturally-aware QA). Compare against final-layer softmax, temperature scaling, LACE (oracle with per-language validation), per-language probes (oracle upper bound), and MKA. Include explicit cross-task transfer analysis: training probes on MMLU/ARC and evaluating on Belebele isolates the compound effect of domain shift + language shift, following CORAL's finding of degraded cross-domain transfer. Risk Acknowledgment: The core empirical bet is that the calibration/correctness direction is sufficiently language-agnostic at intermediate layers. Unlike difficulty (an inherent question property that Civelli et al. showed transfers well), correctness is model-dependent — it combines question difficulty, model capability per language, and representation quality. If model capability is encoded language-specifically even at intermediate layers, zero-shot transfer may fail, and the Pareto frontier analysis will quantify exactly where and why. The fallback is that even partial transfer + few-shot adaptation significantly outperforms existing methods that require full per-language validation sets.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "300-450 A100-80GB hours (Qwen3-235B requires 6-8 A100s per run dominating compute; Llama 4 Scout requires 3-4 A100s at FP16; Gemma 4 31B Dense fits on 1 A100. Activation extraction across 3 models × 50+ languages × all layers dominates; probe training takes minutes on cached activations)",
      "timeline": "8-10 weeks (1-2 weeks infrastructure/data, 3-4 weeks experiments across 3 models, 2 weeks Pareto frontier analysis and ablations, 2 weeks writing)",
      "estimated_gpu_cost": "$700-1100 (at ~$2/hr A100 spot pricing, accounting for multi-GPU coordination overhead on Qwen3-235B and Llama 4 Scout)"
    },
    "human_in_loop": {
      "gpu_hours": "300-450 A100-80GB hours",
      "timeline": "6-8 weeks (Claude drafts experiment scripts, analysis code, Pareto frontier visualizations, and paper sections; human steers hypotheses, interprets results, and manages multi-GPU infrastructure)",
      "claude_api_cost": "$75-150",
      "estimated_gpu_cost": "$700-1100"
    },
    "auto_research": {
      "gpu_hours": "300-450 A100-80GB hours",
      "timeline": "5-6 weeks",
      "claude_api_cost": "$200-350",
      "estimated_gpu_cost": "$700-1100",
      "speed_bottleneck": "Sequential GPU activation extraction across 3 model families and 50+ languages; Qwen3-235B requires 6-8 A100-80GB GPUs (470GB FP16) and dominates compute. Each model requires 8-20 GPU-hours for full multi-layer extraction. Probe training and Pareto analysis are CPU-bound and take minutes on cached activations."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026 — tight but feasible with 10-week timeline)",
    "EACL 2027 (ARR submission deadline: August 3, 2026 — primary target, 11 weeks from now)",
    "ICLR 2027 (estimated deadline: ~October 2026, not yet announced — comfortable timeline)"
  ],
  "level": "solid",
  "key_references": [
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations — Ji et al. (EMNLP 2025)",
    "Calibration Across Layers: Understanding Calibration Evolution in LLMs — Joshi et al. (EMNLP 2025)",
    "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs — Zhou et al. (arXiv 2510.03136, 2025)",
    "MKA: Leveraging Cross-Lingual Consensus for Model Abstention — Duwal et al. (ICLR Workshop 2025)",
    "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs — Liu & Niehues (ACL 2025)",
    "A Shared Geometry of Difficulty in Multilingual Language Models — Civelli et al. (arXiv 2601.12731, Jan 2026)",
    "Correctness-Optimized Residual Activation Lens (CORAL) — Miao et al. (arXiv 2602.06022, Feb 2026)",
    "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, Feb 2026)",
    "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning (arXiv 2601.01362, Jan 2026)",
    "Confidence Geometry Reveals Trace-Level Correctness in LLM Reasoning (arXiv 2605.16824, May 2026)"
  ],
  "description": "Non-English languages suffer from 5x worse calibration error (ECE) compared to English in multilingual LLMs, yet existing fixes require per-language validation data (LACE) or expensive multilingual sampling (MKA). We propose extracting a linear calibration direction from English-only intermediate-layer activations and transferring it zero-shot to non-English languages — but crucially, we frame this around a fundamental and previously uncharacterized tradeoff: calibration quality peaks at 75-91% model depth (Zhou et al., 2025; CORAL, 2026), while cross-lingual transferability peaks at ~50% depth (Liu & Niehues, ACL 2025; Civelli et al., 2026). Our core contribution is mapping the Pareto frontier of layer depth × calibration quality × cross-lingual transfer quality across three architectures (Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B Dense) and 50+ languages. We differentiate from the closely related Shared Geometry of Difficulty work (Civelli et al., arXiv 2601.12731), which demonstrated cross-lingual probe transfer for IRT-based human difficulty at intermediate layers: difficulty is an inherent question property, while correctness is model-dependent — combining difficulty, language-specific capability, and representation quality — making cross-lingual transfer a stronger empirical bet with higher practical payoff for calibration. We synthesize three converging findings: (1) correctness signals are low-dimensional (3-8 dims) and linearly separable across architectures (Confidence Manifold, 2026), (2) intermediate layers contain calibration directions that outperform the final layer (Joshi et al., EMNLP 2025; Zhou et al., 2025), and (3) middle layers form the strongest language-agnostic shared space (Liu & Niehues, ACL 2025). We train logistic regression and lightweight MLP probes on English activations at every 4th layer, then evaluate zero-shot and few-shot (25-100 examples) transfer to 50+ languages on MMLU-ProX, Belebele, and GlobalMMLU, explicitly analyzing the compound effect of domain shift + language shift. If the calibration direction is sufficiently language-agnostic, this method can close the multilingual ECE gap without per-language supervision; the Pareto frontier analysis will quantify exactly how much calibration quality must be traded for cross-lingual transferability, and whether few-shot adaptation can shift this frontier favorably.",
  "project_name": "xling_calib_direction",
  "source": "web_research"
}

Please output this exactly as a properly formatted JSON object. Make sure all strings are properly escaped (especially quotes within strings). Output only the JSON, with no markdown code fences or other wrapping.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "52d40652-d8ee-4a07-b9d6-2035ecda9feb",
  "agentId": "a0660a785004499b3",
  "type": "user",
  "uuid": "45305ebb-9308-4551-974d-264f4d25e981",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "85345ead-20b5-4c36-8188-7eef517dd138",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-19T19:34:29.789Z_

```json
{
  "parentUuid": "45305ebb-9308-4551-974d-264f4d25e981",
  "isSidechain": true,
  "agentId": "a0660a785004499b3",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskStop",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": []
  },
  "type": "attachment",
  "uuid": "5c11a1f7-da3b-47bc-ac87-c2fcf4c7be9e",
  "timestamp": "2026-05-19T19:34:29.789Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "85345ead-20b5-4c36-8188-7eef517dd138",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 3 · 2026-05-19T19:34:29.790Z_

```json
{
  "parentUuid": "5c11a1f7-da3b-47bc-ac87-c2fcf4c7be9e",
  "isSidechain": true,
  "agentId": "a0660a785004499b3",
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e78c9b89-7633-4bf1-93b0-60529d11af4a",
  "timestamp": "2026-05-19T19:34:29.790Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "85345ead-20b5-4c36-8188-7eef517dd138",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 4 · 2026-05-19T19:35:47.027Z_



```json
{
  "change_type": "major",
  "title": "Cross-Lingual Calibration Transfer via Language-Agnostic Confidence Directions: Navigating the Layer-Depth Pareto Frontier",
  "core_problem": "Non-English languages suffer from 5x worse calibration error (ECE) compared to English in multilingual LLMs. Existing fixes require per-language validation data (LACE) or expensive multilingual sampling (MKA). Can we transfer English calibration quality to underserved languages through shared intermediate-layer confidence directions \u2014 and if so, at what layer depth, given the fundamental tradeoff between calibration quality (which peaks at 75-91% depth) and cross-lingual transferability (which peaks at ~50% depth)?",
  "opportunity": "Ji et al. (EMNLP 2025) discovered that verbal uncertainty is governed by a single linear direction in representation space. Joshi et al. (EMNLP 2025) showed calibration evolves across layers with a low-dimensional calibration direction in the residual stream. Zhou et al. (arXiv 2510.03136) introduced LACE, demonstrating that late-intermediate layers encode better-calibrated multilingual signals but requiring per-language validation. Liu & Niehues (ACL 2025) showed that middle layers (~50% depth) form the strongest language-agnostic shared space. Critically, Civelli et al. (arXiv 2601.12731, Jan 2026) demonstrated that linear probes for problem difficulty transfer cross-lingually at shallow-to-intermediate layers (~49% depth) with ~0.78 Spearman rho, while deep probes achieve higher within-language accuracy but fail to transfer \u2014 establishing a shallow-transferable vs. deep-accurate tradeoff. The Confidence Manifold (arXiv 2602.08159, Feb 2026) showed correctness signals occupy just 3-8 dimensions and are linearly separable, with 25 labeled examples achieving 89% of full-data probe accuracy. Nobody has tested whether this correctness/calibration probe transfer works cross-lingually, and nobody has mapped the Pareto frontier of layer depth vs. calibration quality vs. cross-lingual transferability \u2014 this frontier is the key to practical deployment.",
  "landscape": "Zhou et al. (arXiv 2510.03136) introduced LACE, which adaptively ensembles late-intermediate layers (75-91% depth) per language but still requires per-language validation data, and confirmed the 5x ECE gap across 100+ languages and 6 model families (LLaMA-3: 23.1% vs 4.6% ECE for non-English vs English). MKA (Duwal et al., ICLR Workshop 2025) uses cross-lingual consensus for abstention but at 5x inference cost. Joshi et al. (EMNLP 2025) identified a low-dimensional calibration direction in the residual stream. Civelli et al. (arXiv 2601.12731, Jan 2026) showed cross-lingual probe transfer for problem difficulty at intermediate layers in LLaMA-3.1/3.2 and Qwen3-8B, finding shallow probes (~49% depth) transfer with ~0.78 Spearman rho while deep probes (~94% depth) achieve higher within-language accuracy but exhibit poor cross-lingual generalization (0.05-0.19 rho degradation). However, they probed IRT-based human difficulty \u2014 an inherent property of questions \u2014 not model correctness, which is a model-dependent property combining difficulty, language-specific capability, and representation quality. CORAL (Miao et al., arXiv 2602.06022, Feb 2026) demonstrates transferable correctness probes via regularized 4-layer MLP on residual activations with ~50% ECE improvement at layers 17-21 (~53-66% depth), but evaluates only in English across tasks and shows degraded transfer on domain-shifted benchmarks (e.g., HellaSwag). The Confidence Manifold (arXiv 2602.08159, Feb 2026) shows correctness signals occupy 3-8 dimensions and are linearly separable across 9 models and 5 architecture families, with few-shot (25 examples) achieving 89% of full-data probe accuracy \u2014 all English-only. Cross-lingual steering vectors have been demonstrated for language identity and task performance (Mahmoud et al., arXiv 2505.12584; arXiv 2601.16390) but never for calibration. Instruction-tuning studies (arXiv 2601.01362, Jan 2026) confirm that English-centric fine-tuning inflates confidence in low-resource languages without accuracy gains, worsening calibration. Confidence Geometry Reveals Trace-Level Correctness (arXiv 2605.16824, May 2026) extends geometric correctness analysis to reasoning traces using output-level confidence trajectories \u2014 operating at a different level (output tokens, not internal representations) with no multilingual evaluation, but suggesting convergent evidence that correctness has consistent geometric structure. No work has attempted to transfer the correctness/calibration direction itself cross-lingually, and no work has characterized the Pareto frontier between calibration quality and cross-lingual transferability across layer depth.",
  "inspired_by": "Gap: 5x non-English ECE gap (Zhou et al., LACE) + demonstrated cross-lingual difficulty probe transfer at intermediate layers (Civelli et al., Shared Geometry of Difficulty) that has never been extended to correctness/calibration. Pattern: Ji et al.'s linear verbal uncertainty direction + Joshi et al.'s residual-stream calibration direction + Confidence Manifold's 3-8 dimensional correctness signal + cross-lingual middle-layer alignment (Liu & Niehues, ACL 2025). Untried combination: extending representation-space correctness probes from English-only cross-task transfer (CORAL) to cross-lingual calibration transfer, while characterizing the layer-depth Pareto frontier between calibration quality and transferability.",
  "approach": "Phase 1 \u2014 Activation Extraction: Extract intermediate-layer activations at every 4th layer across the full depth of Qwen3-235B-A22B (94 layers, MoE), Llama 4 Scout (48 layers, MoE), and Gemma 4 31B Dense (46 layers, dense) on English QA tasks (MMLU, ARC-Challenge) with known correctness labels. Store activations for all layers to enable the Pareto frontier analysis. Phase 2 \u2014 English Probe Training: At each extracted layer, fit both a logistic regression probe (linear) and a lightweight 2-layer MLP probe to identify the calibration direction \u2014 the hyperplane or surface best separating correct from incorrect answers in representation space. Compare probe complexity: linear probes may transfer better cross-lingually (by analogy to the shallow-transferable finding in Civelli et al.), while MLPs may capture richer correctness signals (as CORAL found). Phase 3 \u2014 Pareto Frontier Analysis (Key Novel Contribution): Apply each layer's English-trained probe zero-shot to non-English activations across 50+ languages. For each layer, measure both (a) calibration quality (ECE, Brier score) and (b) cross-lingual transfer quality (AUROC degradation from English). Map the full Pareto frontier of layer depth \u00d7 calibration quality \u00d7 cross-lingual transferability. Identify whether there exists a 'sweet spot' layer range that achieves near-optimal calibration with strong cross-lingual transfer, or whether the tradeoff is strict. Phase 4 \u2014 Few-Shot Frontier Shifting: Test whether 25-100 non-English examples (motivated by Confidence Manifold's finding that 25 examples achieve 89% of full-data accuracy) can shift the Pareto frontier \u2014 specifically, whether few-shot adaptation at deeper layers (where calibration is better but transfer is worse) can recover cross-lingual transfer quality without sacrificing calibration. Phase 5 \u2014 Evaluation: Evaluate ECE, Brier score, and AUROC on MMLU-ProX (13 languages, same domain as MMLU training \u2014 controls for domain shift), Belebele (122 languages, reading comprehension \u2014 tests cross-task + cross-lingual compound transfer), and GlobalMMLU (42 languages, culturally-aware QA). Compare against final-layer softmax, temperature scaling, LACE (oracle with per-language validation), per-language probes (oracle upper bound), and MKA. Include explicit cross-task transfer analysis: training probes on MMLU/ARC and evaluating on Belebele isolates the compound effect of domain shift + language shift, following CORAL's finding of degraded cross-domain transfer. Risk Acknowledgment: The core empirical bet is that the calibration/correctness direction is sufficiently language-agnostic at intermediate layers. Unlike difficulty (an inherent question property that Civelli et al. showed transfers well), correctness is model-dependent \u2014 it combines question difficulty, model capability per language, and representation quality. If model capability is encoded language-specifically even at intermediate layers, zero-shot transfer may fail, and the Pareto frontier analysis will quantify exactly where and why. The fallback is that even partial transfer + few-shot adaptation significantly outperforms existing methods that require full per-language validation sets.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "300-450 A100-80GB hours (Qwen3-235B requires 6-8 A100s per run dominating compute; Llama 4 Scout requires 3-4 A100s at FP16; Gemma 4 31B Dense fits on 1 A100. Activation extraction across 3 models \u00d7 50+ languages \u00d7 all layers dominates; probe training takes minutes on cached activations)",
      "timeline": "8-10 weeks (1-2 weeks infrastructure/data, 3-4 weeks experiments across 3 models, 2 weeks Pareto frontier analysis and ablations, 2 weeks writing)",
      "estimated_gpu_cost": "$700-1100 (at ~$2/hr A100 spot pricing, accounting for multi-GPU coordination overhead on Qwen3-235B and Llama 4 Scout)"
    },
    "human_in_loop": {
      "gpu_hours": "300-450 A100-80GB hours",
      "timeline": "6-8 weeks (Claude drafts experiment scripts, analysis code, Pareto frontier visualizations, and paper sections; human steers hypotheses, interprets results, and manages multi-GPU infrastructure)",
      "claude_api_cost": "$75-150",
      "estimated_gpu_cost": "$700-1100"
    },
    "auto_research": {
      "gpu_hours": "300-450 A100-80GB hours",
      "timeline": "5-6 weeks",
      "claude_api_cost": "$200-350",
      "estimated_gpu_cost": "$700-1100",
      "speed_bottleneck": "Sequential GPU activation extraction across 3 model families and 50+ languages; Qwen3-235B requires 6-8 A100-80GB GPUs (470GB FP16) and dominates compute. Each model requires 8-20 GPU-hours for full multi-layer extraction. Probe training and Pareto analysis are CPU-bound and take minutes on cached activations."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026 \u2014 tight but feasible with 10-week timeline)",
    "EACL 2027 (ARR submission deadline: August 3, 2026 \u2014 primary target, 11 weeks from now)",
    "ICLR 2027 (estimated deadline: ~October 2026, not yet announced \u2014 comfortable timeline)"
  ],
  "level": "solid",
  "key_references": [
    "Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations \u2014 Ji et al. (EMNLP 2025)",
    "Calibration Across Layers: Understanding Calibration Evolution in LLMs \u2014 Joshi et al. (EMNLP 2025)",
    "Beyond the Final Layer: Intermediate Representations for Better Multilingual Calibration in LLMs \u2014 Zhou et al. (arXiv 2510.03136, 2025)",
    "MKA: Leveraging Cross-Lingual Consensus for Model Abstention \u2014 Duwal et al. (ICLR Workshop 2025)",
    "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs \u2014 Liu & Niehues (ACL 2025)",
    "A Shared Geometry of Difficulty in Multilingual Language Models \u2014 Civelli et al. (arXiv 2601.12731, Jan 2026)",
    "Correctness-Optimized Residual Activation Lens (CORAL) \u2014 Miao et al. (arXiv 2602.06022, Feb 2026)",
    "The Confidence Manifold: Geometric Structure of Correctness Representations in Language Models (arXiv 2602.08159, Feb 2026)",
    "Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning (arXiv 2601.01362, Jan 2026)",
    "Confidence Geometry Reveals Trace-Level Correctness in LLM Reasoning (arXiv 2605.16824, May 2026)"
  ],
  "description": "Non-English languages suffer from 5x worse calibration error (ECE) compared to English in multilingual LLMs, yet existing fixes require per-language validation data (LACE) or expensive multilingual sampling (MKA). We propose extracting a linear calibration direction from English-only intermediate-layer activations and transferring it zero-shot to non-English languages \u2014 but crucially, we frame this around a fundamental and previously uncharacterized tradeoff: calibration quality peaks at 75-91% model depth (Zhou et al., 2025; CORAL, 2026), while cross-lingual transferability peaks at ~50% depth (Liu & Niehues, ACL 2025; Civelli et al., 2026). Our core contribution is mapping the Pareto frontier of layer depth \u00d7 calibration quality \u00d7 cross-lingual transfer quality across three architectures (Qwen3-235B-A22B, Llama 4 Scout, Gemma 4 31B Dense) and 50+ languages. We differentiate from the closely related Shared Geometry of Difficulty work (Civelli et al., arXiv 2601.12731), which demonstrated cross-lingual probe transfer for IRT-based human difficulty at intermediate layers: difficulty is an inherent question property, while correctness is model-dependent \u2014 combining difficulty, language-specific capability, and representation quality \u2014 making cross-lingual transfer a stronger empirical bet with higher practical payoff for calibration. We synthesize three converging findings: (1) correctness signals are low-dimensional (3-8 dims) and linearly separable across architectures (Confidence Manifold, 2026), (2) intermediate layers contain calibration directions that outperform the final layer (Joshi et al., EMNLP 2025; Zhou et al., 2025), and (3) middle layers form the strongest language-agnostic shared space (Liu & Niehues, ACL 2025). We train logistic regression and lightweight MLP probes on English activations at every 4th layer, then evaluate zero-shot and few-shot (25-100 examples) transfer to 50+ languages on MMLU-ProX, Belebele, and GlobalMMLU, explicitly analyzing the compound effect of domain shift + language shift. If the calibration direction is sufficiently language-agnostic, this method can close the multilingual ECE gap without per-language supervision; the Pareto frontier analysis will quantify exactly how much calibration quality must be traded for cross-lingual transferability, and whether few-shot adaptation can shift this frontier favorably.",
  "project_name": "xling_calib_direction",
  "source": "web_research"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e78c9b89-7633-4bf1-93b0-60529d11af4a",
  "isSidechain": true,
  "agentId": "a0660a785004499b3",
  "requestId": "req_011CbCVF9ZdKRGuwwjcoSoky",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a9c127a4-52de-4077-9b5b-3b9a78723910",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea-gen-pipeline",
  "sessionId": "85345ead-20b5-4c36-8188-7eef517dd138",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0112a69yBEJCq8wfqu986Ayk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13088,
      "cache_read_input_tokens": 0,
      "output_tokens": 4028,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 4028,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 13088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13088,
            "ephemeral_1h_input_tokens": 0
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
