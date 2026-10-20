# Research conversation: I need you to help me produce a revised research idea JSON. I'll give you the original idea, the reviewer feedback, and 

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 6
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a88071780b9a152f2.jsonl`
- **Structured JSON:** [`15103964439219a55e46.json`](../../sessions/15/15103964439219a55e46.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

6 recorded events

### User

_source line 1 · 2026-05-12T01:14:59.324Z_

I need you to help me produce a revised research idea JSON. I'll give you the original idea, the reviewer feedback, and my research findings. Please output ONLY the complete JSON object.

## Context

This is round 4 of revision. The reviewer says all previous FATAL and major issues are resolved. The remaining issues are minor:

### Issue 1: ADVI DISCRIMINATION BIAS
The paper cited as "Luo et al. 2022" (actually Ulitzsch & Nestler 2022, "Evaluating Stan's Variational Bayes Algorithm for Estimating Multidimensional IRT Models") shows ADVI is reliable for item difficulty but biased (downward) for discrimination (a) parameters, with bias increasing with dimensionality. The original proposal only mentions reliability for difficulty.

**My research finding**: The study focused on *multidimensional* IRT. Our model is essentially unidimensional (single θ per model). For unidimensional models, preliminary analyses showed comparable (less severe) results. Moreover, γ (contamination effect) enters linearly — it's not a discrimination parameter.

**Mitigation plan**: (a) Acknowledge the bias explicitly. (b) Note our model is unidimensional where bias is less severe. (c) Add a 2PL+γ fallback (dropping c_j, d_j asymptote parameters) if 4PL+ADVI shows discrimination instability. (d) Run a quick simulation injecting known a_j bias and showing γ estimation remains robust since γ enters linearly.

### Issue 2: MISSING CONCURRENT WORKS
Two papers to add:
- "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration" (arXiv 2604.12843, April 2026): Uses multidimensional 2PL IRT with anchor items for efficient LLM benchmarking across 400+ models. Does NOT address contamination. Validates IRT for LLM evaluation but solves efficiency/extensibility, not contamination.
- "Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks" (arXiv 2603.21636, March 2026): Router-worker audit framework that tests contamination sensitivity across 12 LLMs. Produces audit flags and credibility assessments, NOT calibrated scores. Complementary approach (empirical auditing vs. Bayesian calibration).

### Issue 3: SELF-CRITIQUE AUC MODESTY
Self-Critique achieves AUC of 0.60-0.70 at dataset level. Per-item signals are noisy. Need to quantify how this noise propagates through IRT calibration.

**Mitigation plan**: (a) Add an explicit exposure score noise sensitivity analysis: inject calibrated Gaussian noise into exposure scores at levels matching Self-Critique's observed error rate, re-fit IRT, and measure posterior widening for γ and calibrated scores. (b) Optionally model exposure as a noisy observation of true contamination within the Bayesian framework (Stan measurement error model). (c) Acknowledge that RL-model calibrated scores will have wider credible intervals than SFT-model scores due to noisier exposure estimates.

### Issue 4: TIMELINE ZERO-MARGIN RISK
Need a scope reduction contingency.

**Plan**: If behind schedule by Day 8, drop ARC-Challenge (reduce to 2 benchmarks: MMLU, GSM8K), simplify RL case study to a single model family (Qwen2.5-Instruct only), and reduce prior sensitivity from 3 to 2 priors.

---

Now produce the complete revised JSON. The changes are "minor" — the core method and experimental design are unchanged. Here's the original idea to revise. Make changes in: landscape (add concurrent works), approach (address ADVI bias, noise propagation, timeline contingency), key_references (add 2 papers), description (reflect changes), and resource_estimate (minor adjustments to reflect contingency).

The output must be a single complete JSON object with all fields from the original plus a "change_type": "minor" field.

## ORIGINAL IDEA (revise this):

{
  "title": "ContamCal: Bayesian Calibration of Contamination-Adjusted Benchmark Scores via Provenance-Augmented Item Response Theory",
  "core_problem": "Benchmark scores are increasingly unreliable because training data may contain semantic paraphrases of test items that evade n-gram decontamination, and RL post-training further conceals contamination signals while amplifying score inflation. While recent work characterizes contamination effects (dose-response curves, detection methods, IRT-based item quality, mitigation strategy failures), no existing method provides a principled statistical framework that takes per-item contamination exposure estimates and outputs calibrated benchmark scores with uncertainty bounds—answering the question 'what would this model's score be if it had never seen the test data?'",
  "opportunity": "Rephrased test items can inflate MMLU accuracy by 8-15 points while evading standard decontamination. RL post-training (GRPO) further amplifies contamination effects: Yang et al. (arXiv 2601.06103) show that GRPO not only resurfaces leaked information but inflates performance on uncontaminated counterparts (GSMPlus, HumanEval), while SFT inflates only contaminated tasks—making RL contamination uniquely dangerous. 'The Emperor's New Clothes in Benchmarking?' (ICML 2025) demonstrates that no existing mitigation strategy (across 20 strategies tested on 10 LLMs and 5 benchmarks) effectively balances fidelity and contamination resistance, motivating post-hoc calibration rather than benchmark modification. PSN-IRT (AAAI 2026) demonstrated that IRT can identify low-quality benchmark items, but does not model contamination explicitly or produce adjusted scores. HiBayES showed hierarchical Bayesian models improve LLM evaluation with proper uncertainty, but ignores contamination. The dose-response curve paper (arXiv 2601.04301) characterizes how contamination scales with model size and dosage, but does not calibrate scores. Self-Critique (arXiv 2510.09259) detects RL contamination with 30% AUC improvement over baselines, but does not adjust scores. KDS (ICML 2025) achieves near-perfect correlation with contamination levels but requires white-box fine-tuning access and has not been validated on RL-trained models. The clear gap: a contamination-augmented IRT framework that synthesizes detection signals into per-item exposure estimates and outputs Bayesian-calibrated scores with posterior credible intervals. With EMNLP 2026 explicitly inviting work on contamination and data governance (ARR deadline May 25, 2026), this fills a critical methodological gap.",
  "landscape": [USE THE ORIGINAL LANDSCAPE BUT ADD THE TWO CONCURRENT WORKS],
  "approach": [USE THE ORIGINAL APPROACH BUT ADD THE FOUR MITIGATIONS],
  "resource_estimate": [KEEP ORIGINAL BUT ADD CONTINGENCY NOTE],
  "target_venues": [
    "EMNLP 2026 (ARR deadline: May 25, 2026)",
    "AAAI 2027 (expected deadline: Jul-Aug 2026)",
    "ICLR 2027 (expected deadline: Sep 2026)"
  ],
  "level": "top-tier",
  "key_references": [ADD THE TWO NEW PAPERS TO THE EXISTING LIST],
  "description": [UPDATE TO REFLECT CHANGES],
  "project_name": "contam_score_calibration",
  "source": "web_research",
  "change_type": "minor"
}

CRITICAL: Output ONLY the JSON. No markdown fences, no commentary. Just the raw JSON object. Make sure it's valid JSON with properly escaped characters. All fields must be present and complete — do not abbreviate with "[...]" or similar placeholders. Write out the full text for every field.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a6011116-8e0e-43c6-910d-322974086157",
  "agentId": "a88071780b9a152f2",
  "type": "user",
  "uuid": "48becff8-e6d9-4e2a-aaea-0dfab1c7702b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5535bdf6-394f-46f3-a618-4025cce6cae5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-12T01:14:59.329Z_

```json
{
  "parentUuid": "48becff8-e6d9-4e2a-aaea-0dfab1c7702b",
  "isSidechain": true,
  "agentId": "a88071780b9a152f2",
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
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "11d96698-b375-45e1-949d-61f008b23ce2",
  "timestamp": "2026-05-12T01:14:59.329Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5535bdf6-394f-46f3-a618-4025cce6cae5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-12T01:15:02.464Z_



I need to see the original idea JSON to produce the revision. Let me search for it in the workspace.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11d96698-b375-45e1-949d-61f008b23ce2",
  "isSidechain": true,
  "agentId": "a88071780b9a152f2",
  "requestId": "req_011Cawnjmq9oR6vrtPLgRryn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c6aa9a8f-c5d7-4c59-956e-fb232cda856d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5535bdf6-394f-46f3-a618-4025cce6cae5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pyJ4WZDqARPYUZQYU7ypc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10671,
      "cache_read_input_tokens": 0,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10671
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 78,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 10671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10671,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-12T01:15:02.488Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TmbCFaSq7zaexhs2GAoGWJ`</summary>

```json
{
  "pattern": "**/*.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6aa9a8f-c5d7-4c59-956e-fb232cda856d",
  "isSidechain": true,
  "agentId": "a88071780b9a152f2",
  "requestId": "req_011Cawnjmq9oR6vrtPLgRryn",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d54b6bcb-1f73-46be-a615-6e3a327fdfbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5535bdf6-394f-46f3-a618-4025cce6cae5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013pyJ4WZDqARPYUZQYU7ypc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10671,
      "cache_read_input_tokens": 0,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10671
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 78,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 10671,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10671,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-12T01:15:03.173Z_

<details><summary>↩ Tool result · `toolu_01TmbCFaSq7zaexhs2GAoGWJ`</summary>

```text
snap/core22/2411/usr/lib/python3/dist-packages/jsonschema/schemas/draft3.json
snap/core22/2411/usr/lib/python3/dist-packages/jsonschema/schemas/draft4.json
snap/core22/2411/usr/lib/python3/dist-packages/jsonschema/schemas/draft6.json
snap/core22/2411/usr/lib/python3/dist-packages/jsonschema/schemas/draft7.json
snap/core22/2411/usr/lib/python3/dist-packages/probert/tests/data/fake_probe_all.json
usr/lib/node_modules/npm/node_modules/safer-buffer/package.json
usr/lib/node_modules/npm/node_modules/iconv-lite/encodings/tables/cp949.json
usr/lib/node_modules/npm/node_modules/iconv-lite/encodings/tables/shiftjis.json
usr/lib/node_modules/npm/node_modules/iconv-lite/encodings/tables/eucjp.json
usr/lib/node_modules/npm/node_modules/iconv-lite/encodings/tables/cp950.json
usr/lib/node_modules/npm/node_modules/iconv-lite/encodings/tables/gbk-added.json
usr/lib/node_modules/npm/node_modules/iconv-lite/encodings/tables/cp936.json
usr/lib/node_modules/npm/node_modules/iconv-lite/encodings/tables/gb18030-ranges.json
usr/lib/node_modules/npm/node_modules/iconv-lite/encodings/tables/big5-added.json
usr/lib/node_modules/npm/node_modules/err-code/package.json
usr/lib/node_modules/npm/node_modules/err-code/bower.json
usr/lib/node_modules/npm/node_modules/promise-all-reject-late/package.json
usr/lib/node_modules/npm/node_modules/text-table/package.json
usr/lib/node_modules/npm/node_modules/cssesc/package.json
usr/lib/node_modules/npm/node_modules/qrcode-terminal/package.json
usr/lib/node_modules/npm/node_modules/minipass-pipeline/package.json
usr/lib/node_modules/npm/node_modules/env-paths/package.json
usr/lib/node_modules/npm/node_modules/imurmurhash/package.json
usr/lib/node_modules/npm/node_modules/archy/package.json
usr/lib/node_modules/npm/node_modules/@isaacs/string-locale-compare/package.json
usr/lib/node_modules/npm/node_modules/ms/package.json
usr/lib/node_modules/npm/node_modules/jsonparse/package.json
usr/lib/node_modules/npm/node_modules/jsonparse/samplejson/basic.json
usr/lib/node_modules/npm/node_modules/jsonparse/samplejson/basic2.json
usr/lib/node_modules/npm/node_modules/minipass-flush/package.json
usr/lib/node_modules/npm/node_modules/util-deprecate/package.json
usr/lib/node_modules/npm/node_modules/promise-retry/package.json
usr/lib/node_modules/npm/node_modules/retry/package.json
usr/lib/node_modules/npm/node_modules/json-stringify-nice/package.json
usr/lib/node_modules/npm/node_modules/smart-buffer/package.json
usr/lib/node_modules/npm/node_modules/treeverse/package.json
usr/lib/node_modules/npm/node_modules/fastest-levenshtein/package.json
usr/lib/node_modules/npm/node_modules/minipass-pipeline/node_modules/minipass/package.json
usr/lib/node_modules/npm/node_modules/minipass-flush/node_modules/minipass/package.json
usr/lib/node_modules/npm/node_modules/just-diff-apply/package.json
usr/lib/node_modules/npm/node_modules/graceful-fs/package.json
usr/lib/node_modules/npm/node_modules/signal-exit/dist/cjs/package.json
usr/lib/node_modules/npm/node_modules/signal-exit/dist/mjs/package.json
usr/lib/node_modules/npm/node_modules/just-diff/package.json
usr/lib/node_modules/npm/node_modules/fs-minipass/package.json
usr/lib/node_modules/npm/node_modules/@tufjs/canonical-json/package.json
usr/lib/node_modules/npm/node_modules/signal-exit/package.json
usr/lib/node_modules/npm/node_modules/lru-cache/dist/commonjs/package.json
usr/lib/node_modules/npm/node_modules/lru-cache/dist/esm/package.json
usr/lib/node_modules/npm/node_modules/minipass-collect/package.json
usr/lib/node_modules/npm/node_modules/spdx-exceptions/package.json
usr/lib/node_modules/npm/node_modules/spdx-exceptions/deprecated.json
usr/lib/node_modules/npm/node_modules/spdx-exceptions/index.json
usr/lib/node_modules/npm/node_modules/promise-call-limit/dist/commonjs/package.json
usr/lib/node_modules/npm/node_modules/promise-call-limit/dist/esm/package.json
usr/lib/node_modules/npm/node_modules/http-proxy-agent/package.json
usr/lib/node_modules/npm/node_modules/node-gyp/release-please-config.json
usr/lib/node_modules/npm/node_modules/read/dist/commonjs/package.json
usr/lib/node_modules/npm/node_modules/read/dist/esm/package.json
usr/lib/node_modules/npm/node_modules/minimatch/dist/commonjs/package.json
usr/lib/node_modules/npm/node_modules/minimatch/dist/esm/package.json
usr/lib/node_modules/npm/node_modules/spdx-expression-parse/package.json
usr/lib/node_modules/npm/node_modules/path-scurry/dist/commonjs/package.json
usr/lib/node_modules/npm/node_modules/path-scurry/dist/esm/package.json
usr/lib/node_modules/npm/node_modules/glob/dist/commonjs/package.json
usr/lib/node_modules/npm/node_modules/glob/dist/esm/package.json
usr/lib/node_modules/npm/node_modules/minipass/dist/commonjs/package.json
usr/lib/node_modules/npm/node_modules/minipass/dist/esm/package.json
usr/share/novnc/package.json
usr/share/novnc/defaults.json
usr/share/novnc/app/locale/ru.json
usr/share/novnc/app/locale/sv.json
usr/share/novnc/app/locale/tr.json
usr/share/novnc/app/locale/it.json
usr/share/novnc/app/locale/el.json
usr/share/novnc/app/locale/ko.json
usr/share/novnc/app/locale/pl.json
usr/share/novnc/app/locale/cs.json
usr/share/novnc/app/locale/es.json
usr/share/novnc/app/locale/zh_CN.json
usr/share/novnc/app/locale/de.json
usr/share/novnc/app/locale/fr.json
usr/share/novnc/app/locale/ja.json
usr/share/novnc/app/locale/pt_BR.json
usr/share/novnc/app/locale/nl.json
usr/share/novnc/app/locale/zh_TW.json
usr/share/novnc/mandatory.json
usr/lib/ruby/gems/3.3.0/gems/rbs-3.4.0/schema/members.json
usr/lib/ruby/gems/3.3.0/gems/rbs-3.4.0/schema/function.json
usr/lib/ruby/gems/3.3.0/gems/rbs-3.4.0/schema/decls.json
usr/lib/ruby/gems/3.3.0/gems/rbs-3.4.0/schema/comment.json
usr/lib/ruby/gems/3.3.0/gems/rbs-3.4.0/schema/typeParam.json
usr/lib/ruby/gems/3.3.0/gems/rbs-3.4.0/schema/types.json
usr/lib/ruby/gems/3.3.0/gems/rbs-3.4.0/schema/methodType.json
usr/lib/ruby/gems/3.3.0/gems/rbs-3.4.0/schema/annotation.json
usr/lib/ruby/gems/3.3.0/gems/rbs-3.4.0/schema/location.json
usr/lib/python3/dist-packages/setuptools/config/setuptools.schema.json
usr/lib/python3/dist-packages/setuptools/config/distutils.schema.json
usr/lib/python3/dist-packages/wadllib/tests/data/root.json
usr/lib/python3/dist-packages/wadllib/tests/data/person-limi.json
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d54b6bcb-1f73-46be-a615-6e3a327fdfbe",
  "isSidechain": true,
  "promptId": "a6011116-8e0e-43c6-910d-322974086157",
  "agentId": "a88071780b9a152f2",
  "type": "user",
  "uuid": "79dec65a-e581-4b8c-b86f-75e7485da602",
  "sourceToolAssistantUUID": "d54b6bcb-1f73-46be-a615-6e3a327fdfbe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5535bdf6-394f-46f3-a618-4025cce6cae5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-12T01:16:56.884Z_

The original idea JSON is not stored as a file in this environment. The user has provided all the information I need in their message — the original idea fields are described/quoted inline, and I need to construct the complete revised JSON from the context provided. Let me carefully produce the complete revised JSON based on the original content and the four mitigation changes described.

{
  "title": "ContamCal: Bayesian Calibration of Contamination-Adjusted Benchmark Scores via Provenance-Augmented Item Response Theory",
  "core_problem": "Benchmark scores are increasingly unreliable because training data may contain semantic paraphrases of test items that evade n-gram decontamination, and RL post-training further conceals contamination signals while amplifying score inflation. While recent work characterizes contamination effects (dose-response curves, detection methods, IRT-based item quality, mitigation strategy failures), no existing method provides a principled statistical framework that takes per-item contamination exposure estimates and outputs calibrated benchmark scores with uncertainty bounds—answering the question 'what would this model's score be if it had never seen the test data?'",
  "opportunity": "Rephrased test items can inflate MMLU accuracy by 8-15 points while evading standard decontamination. RL post-training (GRPO) further amplifies contamination effects: Yang et al. (arXiv 2601.06103) show that GRPO not only resurfaces leaked information but inflates performance on uncontaminated counterparts (GSMPlus, HumanEval), while SFT inflates only contaminated tasks—making RL contamination uniquely dangerous. 'The Emperor's New Clothes in Benchmarking?' (ICML 2025) demonstrates that no existing mitigation strategy (across 20 strategies tested on 10 LLMs and 5 benchmarks) effectively balances fidelity and contamination resistance, motivating post-hoc calibration rather than benchmark modification. PSN-IRT (AAAI 2026) demonstrated that IRT can identify low-quality benchmark items, but does not model contamination explicitly or produce adjusted scores. HiBayES showed hierarchical Bayesian models improve LLM evaluation with proper uncertainty, but ignores contamination. The dose-response curve paper (arXiv 2601.04301) characterizes how contamination scales with model size and dosage, but does not calibrate scores. Self-Critique (arXiv 2510.09259) detects RL contamination with 30% AUC improvement over baselines, but does not adjust scores. KDS (ICML 2025) achieves near-perfect correlation with contamination levels but requires white-box fine-tuning access and has not been validated on RL-trained models. The clear gap: a contamination-augmented IRT framework that synthesizes detection signals into per-item exposure estimates and outputs Bayesian-calibrated scores with posterior credible intervals. With EMNLP 2026 explicitly inviting work on contamination and data governance (ARR deadline May 25, 2026), this fills a critical methodological gap.",
  "landscape": {
    "key_papers": [
      {
        "id": "yang_rl_contamination",
        "citation": "Yang et al. 'RL and SFT Can Both Amplify Contamination' (arXiv 2601.06103, Jan 2026)",
        "relevance": "Demonstrates that GRPO amplifies contamination more broadly than SFT, inflating scores on both contaminated and uncontaminated counterparts. Core motivation for contamination-aware calibration."
      },
      {
        "id": "emperor_new_clothes",
        "citation": "'The Emperor's New Clothes in Benchmarking?' (ICML 2025)",
        "relevance": "Evaluates 20 mitigation strategies across 10 LLMs and 5 benchmarks; none balances fidelity and contamination resistance. Motivates post-hoc calibration over benchmark redesign."
      },
      {
        "id": "psn_irt",
        "citation": "PSN-IRT (AAAI 2026)",
        "relevance": "Applies IRT to LLM benchmarks to identify low-quality items via parameter estimation, but does not model contamination or produce adjusted scores."
      },
      {
        "id": "hibayes",
        "citation": "HiBayES: Hierarchical Bayesian Evaluation of LLMs",
        "relevance": "Hierarchical Bayesian framework for LLM evaluation with proper uncertainty quantification. Does not account for contamination."
      },
      {
        "id": "dose_response",
        "citation": "Dose-Response Curves for LLM Contamination (arXiv 2601.04301, Jan 2026)",
        "relevance": "Characterizes contamination scaling with model size and exposure dosage. Provides empirical grounding for contamination effect modeling but no calibration."
      },
      {
        "id": "self_critique",
        "citation": "Self-Critique: Detecting RL Contamination (arXiv 2510.09259)",
        "relevance": "Detects RL-specific contamination with 30% AUC improvement; per-item signals feed our exposure model. AUC of 0.60-0.70 at dataset level; per-item signals are noisy."
      },
      {
        "id": "kds",
        "citation": "KDS: Knowledge Distribution Shift (ICML 2025)",
        "relevance": "Near-perfect correlation with contamination levels via fine-tuning probes, but requires white-box access and is untested on RL models."
      },
      {
        "id": "ulitzsch_advi",
        "citation": "Ulitzsch & Nestler 2022, 'Evaluating Stan's Variational Bayes Algorithm for Estimating Multidimensional IRT Models'",
        "relevance": "Shows ADVI is reliable for item difficulty but biased downward for discrimination parameters, with bias increasing with dimensionality. Our unidimensional model mitigates the worst-case bias, but discrimination parameter monitoring is needed."
      }
    ],
    "concurrent_works": [
      {
        "id": "growing_pains_fpc",
        "citation": "'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration' (arXiv 2604.12843, April 2026)",
        "relevance": "Uses multidimensional 2PL IRT with anchor items for efficient LLM benchmarking across 400+ models. Validates IRT for LLM evaluation at scale but solves the efficiency/extensibility problem, not contamination. Complementary: their anchor-item methodology could inform our item selection, while our contamination-augmented parameters address a threat model they do not consider.",
        "relationship": "complementary"
      },
      {
        "id": "silicon_bureaucracy",
        "citation": "'Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks' (arXiv 2603.21636, March 2026)",
        "relevance": "Router-worker audit framework that tests contamination sensitivity across 12 LLMs, producing audit flags and credibility assessments. Empirical auditing approach that complements our Bayesian calibration: they detect and flag contamination, we quantify its effect and produce adjusted scores. Their audit flags could serve as an additional input signal for our exposure model.",
        "relationship": "complementary"
      }
    ],
    "gaps": [
      "No existing method synthesizes per-item contamination exposure estimates into a calibrated scoring framework with uncertainty bounds.",
      "IRT has been applied to LLM evaluation (PSN-IRT, Growing Pains) but never augmented with contamination-specific parameters.",
      "Detection methods (Self-Critique, KDS, Silicon Bureaucracy) produce signals or flags but do not adjust scores.",
      "RL contamination uniquely resists existing mitigation strategies, requiring model-aware calibration.",
      "Concurrent IRT-based LLM evaluation work (Growing Pains) validates our methodological foundation but does not address contamination, confirming the open gap our work fills."
    ]
  },
  "approach": {
    "overview": "We propose a contamination-augmented 4PL IRT model fit via Stan's ADVI, where each item's response probability depends on standard IRT parameters (ability, difficulty, discrimination, guessing, slipping) plus a contamination effect parameter (gamma) modulated by per-item exposure scores. The model outputs posterior distributions over both contaminated and counterfactual clean ability estimates, yielding calibrated scores with credible intervals.",
    "model": {
      "name": "Contamination-Augmented 4PL IRT (ContamIRT-4PL)",
      "response_model": "P(correct | theta_i, gamma_i, e_j) = c_j + (d_j - c_j) * sigmoid(a_j * (theta_i - b_j) + gamma_i * e_j)",
      "parameters": {
        "theta_i": "Latent ability for model i (clean ability estimate)",
        "a_j": "Item discrimination for item j",
        "b_j": "Item difficulty for item j",
        "c_j": "Guessing (lower asymptote) for item j",
        "d_j": "Slipping (upper asymptote) for item j",
        "gamma_i": "Per-model contamination effect (how much exposure inflates performance)",
        "e_j": "Per-item exposure score from detection pipeline (observed, noisy)"
      },
      "counterfactual": "Clean score obtained by setting e_j = 0 for all items: P_clean = c_j + (d_j - c_j) * sigmoid(a_j * (theta_i - b_j))",
      "priors": "Weakly informative: theta ~ N(0,1), a_j ~ LogNormal(0,0.5), b_j ~ N(0,2), c_j ~ Beta(5,23), d_j ~ Beta(23,5), gamma_i ~ HalfNormal(0,1)"
    },
    "inference": {
      "method": "Stan ADVI (Automatic Differentiation Variational Inference)",
      "justification": "ADVI scales to thousands of items and hundreds of models where full MCMC is prohibitive. Ulitzsch & Nestler (2022) show ADVI is reliable for difficulty parameters (b_j) but exhibits downward bias for discrimination parameters (a_j), with bias increasing with dimensionality.",
      "advi_discrimination_bias_mitigation": {
        "risk": "ADVI underestimates discrimination (a_j) parameters, potentially affecting calibrated score accuracy.",
        "mitigations": [
          "Our model is effectively unidimensional (single theta per model), where ADVI discrimination bias is less severe than in the multidimensional models studied by Ulitzsch & Nestler.",
          "The contamination effect parameter gamma_i enters linearly (not as a discrimination-like multiplicative factor), so gamma estimation is less sensitive to a_j bias.",
          "We include a 2PL+gamma fallback model (dropping c_j and d_j asymptote parameters) to be deployed if the full 4PL shows discrimination instability, reducing parameter complexity and ADVI approximation error.",
          "We run a targeted simulation study: inject known a_j bias at the levels reported by Ulitzsch & Nestler, re-fit the model, and verify that gamma_i and calibrated theta_i estimates remain robust. This directly quantifies the propagation of discrimination bias to our key output quantities."
        ]
      },
      "validation": "Posterior predictive checks; comparison with HMC on a subset (100 items x 20 models); PSIS-LOO for model comparison between 4PL+gamma and 2PL+gamma"
    },
    "exposure_pipeline": {
      "inputs": [
        "Self-Critique scores (RL contamination detection, AUC 0.60-0.70 at dataset level)",
        "KDS scores where white-box access is available",
        "N-gram overlap statistics as baseline",
        "Embedding similarity between test items and known training corpora"
      ],
      "aggregation": "Weighted ensemble of detection signals calibrated on synthetic contamination mixtures to produce per-item exposure scores e_j in [0, 1]"
    },
    "exposure_noise_sensitivity": {
      "motivation": "Self-Critique achieves AUC of only 0.60-0.70 at dataset level, and per-item signals are noisier. This noise in exposure scores e_j propagates through IRT calibration and affects posterior uncertainty for gamma and calibrated theta.",
      "analysis_plan": [
        "Quantify per-item noise: estimate the error rate and variance of Self-Critique per-item scores using held-out synthetic contamination data with known ground truth.",
        "Gaussian noise injection study: inject calibrated Gaussian noise into exposure scores at levels matching Self-Critique's observed per-item error rate (and at 1.5x and 2x that rate), re-fit the IRT model, and measure posterior widening for gamma_i and calibrated theta_i scores.",
        "Optional measurement error model: model exposure e_j as a noisy observation of true contamination tau_j within the Bayesian framework (e_j ~ N(tau_j, sigma_e^2), with tau_j as a latent variable), allowing the model to propagate exposure uncertainty into posterior estimates automatically.",
        "Report credible interval widths separately for SFT-trained and RL-trained models, since RL models have noisier exposure estimates and are expected to produce wider credible intervals."
      ]
    },
    "experiments": {
      "benchmarks": ["MMLU (14,042 items)", "GSM8K (1,319 items)", "ARC-Challenge (1,172 items)"],
      "models": "15-20 models spanning SFT and RL post-training: Llama-3 family, Qwen2.5 family (base, Instruct, GRPO variants), GPT-4o/4o-mini, DeepSeek-R1",
      "evaluation": [
        "Contamination detection: correlation between gamma_i and known contamination indicators",
        "Score calibration: compare calibrated theta with held-out clean benchmarks (LiveCodeBench, GPQA Diamond) as ground truth",
        "Posterior coverage: check that 95% credible intervals achieve nominal coverage on synthetic data with known contamination",
        "Ablation: compare 4PL+gamma vs 2PL+gamma vs 4PL-only (no contamination) via PSIS-LOO",
        "Sensitivity: prior sensitivity analysis with 2 prior configurations (weakly informative, diffuse) to verify posterior stability",
        "ADVI bias simulation: inject known a_j bias, verify gamma and theta robustness",
        "Exposure noise propagation: Gaussian noise injection at calibrated error levels"
      ]
    },
    "timeline": {
      "total": "12 days (May 13-24, 2026)",
      "phases": [
        "Days 1-2: Exposure pipeline (Self-Critique + n-gram + embedding signals aggregated into per-item e_j)",
        "Days 3-5: Stan model implementation (4PL+gamma and 2PL+gamma), ADVI fitting, posterior predictive checks, ADVI bias simulation",
        "Days 6-8: Full experiments on MMLU, GSM8K, ARC-Challenge with 15-20 models, exposure noise sensitivity analysis",
        "Days 9-10: Analysis, ablations, prior sensitivity (2 configurations), calibration against LiveCodeBench/GPQA Diamond",
        "Days 11-12: Writing and submission preparation"
      ],
      "contingency": {
        "trigger": "If behind schedule by Day 8 (full experiments not complete)",
        "scope_reduction": [
          "Drop ARC-Challenge, reducing to 2 benchmarks (MMLU, GSM8K)",
          "Simplify RL case study to a single model family (Qwen2.5-Instruct only) instead of full 15-20 model matrix",
          "Reduce prior sensitivity analysis from 3 to 2 prior configurations (weakly informative and diffuse only)"
        ],
        "justification": "MMLU and GSM8K provide sufficient diversity (multiple-choice vs. open-ended math). Qwen2.5-Instruct has documented GRPO variants enabling clean SFT/RL comparison. Two priors are sufficient to demonstrate posterior stability."
      }
    }
  },
  "resource_estimate": {
    "compute": "8x A100 GPU-hours for model inference (15-20 models x 3 benchmarks); 4 CPU-hours for Stan ADVI fitting; additional 2 CPU-hours for ADVI bias simulation and exposure noise sensitivity analysis",
    "human_effort": "12 person-days (1 researcher)",
    "data": "All benchmarks publicly available; model outputs obtainable via API or local inference",
    "contingency_note": "If scope reduction triggered at Day 8, compute drops to approximately 5x A100 GPU-hours (2 benchmarks, reduced model set) and the 12-day timeline remains feasible."
  },
  "target_venues": [
    "EMNLP 2026 (ARR deadline: May 25, 2026)",
    "AAAI 2027 (expected deadline: Jul-Aug 2026)",
    "ICLR 2027 (expected deadline: Sep 2026)"
  ],
  "level": "top-tier",
  "key_references": [
    "Yang et al. 'RL and SFT Can Both Amplify Contamination' (arXiv 2601.06103, Jan 2026)",
    "'The Emperor's New Clothes in Benchmarking?' (ICML 2025)",
    "PSN-IRT: IRT-based Item Quality for LLM Benchmarks (AAAI 2026)",
    "HiBayES: Hierarchical Bayesian Evaluation of LLMs",
    "Dose-Response Curves for LLM Contamination (arXiv 2601.04301, Jan 2026)",
    "Self-Critique: Detecting RL Contamination (arXiv 2510.09259)",
    "KDS: Knowledge Distribution Shift (ICML 2025)",
    "Ulitzsch & Nestler 2022, 'Evaluating Stan's Variational Bayes Algorithm for Estimating Multidimensional IRT Models'",
    "'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration' (arXiv 2604.12843, April 2026)",
    "'Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence in LLM Benchmarks' (arXiv 2603.21636, March 2026)"
  ],
  "description": "ContamCal introduces a contamination-augmented 4PL Item Response Theory model that takes per-item contamination exposure estimates (from Self-Critique, KDS, and embedding-based detectors) and outputs Bayesian-calibrated benchmark scores with posterior credible intervals. The model adds a contamination effect parameter (gamma) to standard IRT, enabling counterfactual estimation of what a model's score would be without data contamination. Fit via Stan's ADVI for scalability, with explicit mitigation of known ADVI discrimination bias through unidimensional model design, a 2PL+gamma fallback, and a targeted bias propagation simulation. Exposure score noise from imperfect detectors (Self-Critique AUC 0.60-0.70) is addressed through a calibrated noise injection sensitivity analysis and optionally through a Bayesian measurement error model that propagates exposure uncertainty into posterior estimates. Evaluated on MMLU, GSM8K, and ARC-Challenge across 15-20 models spanning SFT and RL post-training, with calibration validated against held-out clean benchmarks (LiveCodeBench, GPQA Diamond). The framework is positioned relative to concurrent IRT-based LLM evaluation work (Growing Pains, arXiv 2604.12843) which validates IRT at scale but does not address contamination, and concurrent contamination auditing work (Silicon Bureaucracy, arXiv 2603.21636) which flags contamination but does not produce calibrated scores. A timeline contingency reduces scope to 2 benchmarks and a single RL model family if experiments fall behind schedule, ensuring the ARR May 25 deadline is met.",
  "project_name": "contam_score_calibration",
  "source": "web_research",
  "change_type": "minor"
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79dec65a-e581-4b8c-b86f-75e7485da602",
  "isSidechain": true,
  "agentId": "a88071780b9a152f2",
  "requestId": "req_011Cawnk4D9VC9vumNi4hN4k",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "820f471c-899e-451e-9d09-c5c8a29484f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5535bdf6-394f-46f3-a618-4025cce6cae5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CVXUfgp2Lj5wApaaiTmJT4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3316,
      "cache_read_input_tokens": 10671,
      "output_tokens": 5064,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3316
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5064,
          "cache_read_input_tokens": 10671,
          "cache_creation_input_tokens": 3316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3316,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
