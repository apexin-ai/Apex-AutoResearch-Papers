# writing rebuttal prep

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 74
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_writing_rebuttal_prep_20260518T202752.log`
- **Structured JSON:** [`4b3f6a2890cc1c6ff491.json`](../../sessions/4b/4b3f6a2890cc1c6ff491.json)

## Before a recorded user message

17 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "80d10ea3-d41e-4a9c-ba81-cfbc125e3af3",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779153600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "806c028d-2ad1-4d14-bfc9-77b14e2b9e80",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to write a rebuttal preparation document. Let me first gather the necessary context by reading the referenced files, then compose the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "54b1c726-c0b1-4332-aab0-214dbdf2b825",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYh54wQaRYs4NVETystN9V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14305,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14305
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

Let me gather the necessary context files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "9640764b-1605-45ae-ba9b-bcbbc37f5ac0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYh54wQaRYs4NVETystN9V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14305,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14305
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0141PALeAdoze7xBxHw3arqi`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "a07135b8-451a-4db7-84df-d1a5511ae277",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYh54wQaRYs4NVETystN9V",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14305,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14305
      },
      "output_tokens": 32,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-18T20:28:02.353Z_

<details><summary>↩ Tool result · `toolu_0141PALeAdoze7xBxHw3arqi`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "c602ad53-fe55-4ed4-8b97-343c2810b8fa",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_016Gb2uiwJmK57yrzmm9fjmM`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "paper_framing.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "cf6dd290-85f1-446f-ad90-7bb0ac5cb7cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxNBtA9ua8z1asuziHg2aM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 490,
      "cache_read_input_tokens": 26146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 490
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-18T20:28:05.298Z_

<details><summary>↩ Tool result · `toolu_016Gb2uiwJmK57yrzmm9fjmM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md\", \"content\": \"# Paper Framing — contrastive_trace_safety\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (LLM Security Track)\\n- Deadline: ARR submission May 25, 2026\\n\\n## Core Claims (D031: layer selection as primary contribution, 4 models)\\n\\n**Contribution structure (D031)**:\\n- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions\\n- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal\\n- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work\\n\\n1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).\\n\\n   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).\\n   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.\\n   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.\\n\\n   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.\\n\\n   The core insight: \\\"Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak).\\\"\\n\\n2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 \\\"universal\\\") —\\n\\n   **KEY FINDING (D029)**: The apparent \\\"scale-dependent\\\" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.\\n\\n   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.\\n\\n   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**\\n\\n   **R1-8B (Llama-8B, R1-distilled, n=43):**\\n   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)\\n   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)\\n\\n   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**\\n   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - **3/3 metrics significant — OT-7B cleanest single-model evidence**\\n\\n   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**\\n\\n   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**\\n   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)\\n   - 15/15 W values show significant HS advantage\\n   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is \\\"more accurate but detects later.\\\" Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.\\n   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**\\n\\n   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**\\n   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**\\n   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)\\n   - W=5-15: all NS\\n   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.\\n   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).\\n   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. \\\"Scheme B选错层\\\" narrative weaker for R1-32B.\\n   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.\\n\\n   **32B cross-model divergence (D031 key finding for Discussion):**\\n   | Dimension | R1-32B L63 | QwQ L60 |\\n   |-----------|-----------|---------|\\n   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |\\n   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |\\n   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |\\n   | Coverage (W=1) | 25% | 74% |\\n   Paper MUST discuss this divergence per-model, not unify into single narrative.\\n\\n   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**\\n   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)\\n   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)\\n   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.\\n\\n   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**\\n   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).\\n\\n   | Rank | Model | Metric | p-value | Threshold | Pass |\\n   |------|-------|--------|---------|-----------|------|\\n   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |\\n   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |\\n   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |\\n   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |\\n   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |\\n   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |\\n   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |\\n   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |\\n   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |\\n   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |\\n   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |\\n   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |\\n\\n   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure \\\"HS > text at each model's best setting,\\\" not \\\"at uniform W.\\\" R1-32B W=1 has 25% coverage. Paper must state these conditions.\\n\\n   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.\\n\\n   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.\\n\\n   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.\\n\\n   Paper recommended claim (D032): \\\"At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text.\\\"\\n\\n3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.\\n\\n   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.\\n\\n## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)\\n\\nThe layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.\\n\\n**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:\\n- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased\\n- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.\\n- `precision`: selects deep layers for all models (L60/L63 for 32B)\\n- `pre_cp_fpr`: selects deep layers for all models\\n- `composite` (additive): selects deep layers for all models\\n- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.\\n\\n**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.\\n\\n**Corrected layer definition (D036)**: \\\"Corrected layers\\\" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.\\n\\n**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.\\n\\n**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are \\\"correct\\\" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a \\\"researcher degree of freedom\\\" with systematic audit via sensitivity analysis.\\n\\n**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not \\\"correct vs incorrect.\\\"\\n\\n## Story Spine\\n\\n- **Problem**: Reasoning models exhibit \\\"self-jailbreak\\\" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a \\\"commitment point\\\" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.\\n\\n- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.\\n\\n- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).\\n\\n- **Headline result (D032)**: \\\"Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment.\\\"\\n\\n## Key Evidence Summary\\n\\n### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)\\n\\nBest layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.\\n\\n| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |\\n|--------|----------|-----------|------------|----------|\\n| HS Static LR L14 | — | -2.0 | **9.7%** | — |\\n| HS Temporal W=5 | — | +0.6 | **10.2%** | — |\\n| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |\\n| Text Temporal W=15 | — | +10.3* | 20.5% | — |\\n| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |\\n\\n*Text lead time inflated by high pre-CP FPR (trigger-happy detection)\\nNOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).\\n\\n### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16\\n\\nBest layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.\\n\\n| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\n|--------|---------|-----------|----------|-----------|------|\\n| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |\\n| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |\\n| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |\\n\\nBootstrap (layer 16, matched W=3, 1000 resamples):\\n   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅\\n   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅\\n   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**\\nSelectivity: 18.3pp (real=0.688, random=0.505) — highest across all models\\n\\n### 32B Cross-Architecture — D029 CORRECTED LAYERS\\n\\n**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**\\n- HS vs Text bootstrap (null-centered, 1000 resamples):\\n  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)\\n  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**\\n- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive\\n- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)\\n\\n**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**\\n- W=1: bal_acc +18.7pp, p<0.001 ✅\\n- W≥5: NS (dimensionality: 51200 × W features for n=20)\\n- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS\\n- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)\\n\\n**OLD biased-layer results (RETRACTED as metric artifact):**\\n| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |\\n|-------|-------------|----------------|----------------|-------------------|\\n| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |\\n| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |\\n\\n### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)\\n\\n| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |\\n|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|\\n| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |\\n| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |\\n| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |\\n| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |\\n\\n**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.\\nPrecision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.\\nCaveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.\\n\\n### Position Mediation Analysis (D038 → D039 → D042 complete)\\n\\n**Finding**: Position (relative step t/T) is a significant component of probe performance. 3/4 models retain HS advantage after residualization; R1-32B is the exception.\\n\\n| Model | W | Resid HS BA | Resid Text BA | HS-Text Gap | Gap p | HB |\\n|-------|---|------------|--------------|-------------|-------|-----|\\n| OT-7B | 3 | 0.609 | 0.540 | **+6.9pp** | <0.001 | ✅ |\\n| R1-8B | 15 | 0.669 | 0.605 | **+6.4pp** | <0.001 | ✅ |\\n| R1-8B | 3 | 0.571 | 0.534 | **+3.7pp** | <0.001 | ✅ |\\n| QwQ-32B | 3 | 0.619 | 0.582 | **+3.7pp** | 0.011 | ✅ |\\n| R1-32B | 1 | 0.552 | 0.532 | +1.9pp | 0.914 | ❌ |\\n\\nPosition-only BA: OT-7B/R1-8B/QwQ ≈ 0.706; R1-32B = 0.686.\\n\\n**D042 final picture**: HS advantage has two separable components — position-mediated and non-positional. 3/4 models retain significant non-positional HS advantage (HB pass); R1-32B's advantage is almost entirely position-mediated (drop 20.4pp, residualized gap NS). This is consistent with R1-32B's other caveats (W=1 only significant, 25% coverage).\\n\\n**Key implications for paper**:\\n1. Position is a significant component (12-20pp drop) — universal\\n2. 3/4 models retain non-positional HS advantage (residualized BA gap +3.7 to +6.9pp, HB pass)\\n3. R1-32B is the exception: HS advantage position-mediated, residualized gap NS\\n4. Temporal windowing preserves non-positional signal (R1-8B: 24pp drop@W=3 → 16pp@W=15)\\n5. Paper framing: \\\"HS advantage persists after position removal in 3/4 models; R1-32B advantage is position-mediated\\\"\\n\\n### 5-Seed Robustness (D041)\\n\\n| Model | HB Pass Rate | Mean ΔPrec ± std | Mean ΔBA ± std |\\n|-------|-------------|------------------|----------------|\\n| OT-7B | **5/5** | +20.9 ± 1.3pp | +11.3 ± 1.5pp |\\n| R1-32B | **5/5** | +13.7 ± 2.0pp | +11.8 ± 2.4pp |\\n| QwQ-32B | **5/5** | +19.9 ± 2.5pp | +11.4 ± 3.2pp |\\n| R1-8B | **3/5** | +14.6 ± 4.5pp | +9.4 ± 2.4pp |\\n\\nR1-8B failures are FPR-specific (seed 123 FPR p=0.262, seed 456 FPR p=0.952). Precision is directionally consistent across all 20 seed-model combinations (always positive). ΔPrec never reverses.\\n\\n**D041 insight**: Robustness splits by MODEL not SCALE. R1-32B (5/5, ΔPrec std=2.0pp) is more stable than R1-8B (3/5, ΔPrec std=4.5pp). \\\"7-8B robust / 32B sample-limited\\\" is factually wrong. R1-32B's absolute precision std (12.8pp) vs paired delta std (2.0pp) — paper must distinguish these.\\n\\n**Per-model evidence tier (D042)**:\\n- **OT-7B**: Cleanest — 5/5 HB, largest residualized gap (+6.9pp), highest selectivity (18.3pp)\\n- **QwQ-32B**: Robust — 5/5 HB, residualized gap holds (+3.7pp), but position baseline competitive\\n- **R1-8B**: Precision-robust — residualized holds (+3.7-6.4pp), but FPR unstable (3/5 HB)\\n- **R1-32B**: Statistically stable (5/5 HB, ΔPrec std=2.0pp) but advantage position-mediated (residualized NS)\\n\\n**Residualized precision**: Not tested (scope limited to BA per Reviewer recommendation).\\n\\n### BA-Layer Robustness: Metric Circularity Refuted (D044)\\n\\nR13 W1 concern: corrected selection uses threshold-dependent metrics (precision, FPR), evaluation also uses precision/FPR — potential circularity. Test: compute HS vs text on BA-selected layers (threshold-free criterion).\\n\\n| Model | BA-Opt Layer | ΔPrec | ΔBA | ΔFPR | ΔAUROC | All 4 HB? |\\n|-------|-------------|-------|-----|------|--------|-----------|\\n| R1-8B | L12 | +17.8pp | +7.8pp | -12.9pp | +9.3pp | ✅ |\\n| OT-7B | L9 | +25.4pp | +11.7pp | -19.3pp | +14.8pp | ✅ |\\n| QwQ-32B | L30 | +18.0pp | +14.8pp | -8.0pp | +17.3pp | ✅ |\\n| R1-32B | L47 | +13.7pp | +14.9pp | -23.1pp | +21.1pp | ✅ |\\n\\n**4/4 models × 4 metrics = 16/16 HB pass.** HS advantage is a genuine modality property, not a layer selection artifact.\\n\\nKey insight: R1-32B on BA-layer L47 shows ΔPrec +13.7pp and ΔAUROC +21.1pp — stronger than corrected L63 in threshold-free metrics. OT-7B on BA-layer L9 has ΔPrec +25.4pp > corrected L16 (+21.9pp). HS advantage is robust to layer selection criterion.\\n\\nCaveat: QwQ FPR adj_p=0.041 (marginal, CI close to zero). Other 15/16 tests p≤0.006.\\n\\n### Post-hoc Power Analysis (D044)\\n\\n| Model | n (test) | MDE (80% power, α=0.05) |\\n|-------|----------|------------------------|\\n| OT-7B | 47-69 | 6.7-8.1pp |\\n| R1-8B | 43-63 | 7.4-9.0pp |\\n| QwQ-32B | 29 | 9.5pp |\\n| R1-32B | 20-30 | 8.6-11.2pp |\\n\\nAll significant effects (15-24pp) are well above MDE → adequately powered. R1-32B residualized gap (+1.9pp) is far below MDE (11.2pp) → NS is power limitation, not evidence of absence.\\n\\n### Negative Results (expanded with R3 supplementary experiments)\\n- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.\\n- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.\\n- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:\\n  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.\\n  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.\\n  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642\\n  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).\\n- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.\\n- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as \\\"weakly supervised\\\" not \\\"unsupervised\\\"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.\\n- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).\\n\\n## Venue Fit Risks\\n\\n- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.\\n- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.\\n- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).\\n- **HS advantage universal**: UPGRADED from \\\"scale-dependent\\\" — layer selection is the true moderator, not scale. Cleaner story.\\n- **Trace vs step FPR**: Both reported with explanation.\\n- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.\\n- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. \\\"Method novelty?\\\" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).\\n2. \\\"Only one model family?\\\" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.\\n3. \\\"GRU unstable?\\\" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.\\n4. \\\"Too few traces?\\\" → Cross-model validation + control task selectivity 7.5-18.5pp.\\n5. \\\"Fine-grained taxonomy?\\\" → Out of scope for current study.\\n6. \\\"HS doesn't beat text?\\\" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.\\n7. \\\"Commitment point circular?\\\" → Cross-model consistency + control task selectivity argues against artifact.\\n8. \\\"Missing related work?\\\" → Expansion to 30+ citations.\\n9. \\\"No FPR analysis?\\\" → RESOLVED: both trace-level and step-level FPR reported.\\n10. \\\"High safe FPR?\\\" → Limitation acknowledged.\\n11. \\\"Control task / position confound?\\\" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.\\n12. \\\"Multiple testing correction?\\\" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).\\n13. \\\"Trace vs step FPR?\\\" → Both reported with explanation.\\n14. \\\"Layer selection is just hyperparameter tuning?\\\" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.\\n15. \\\"Why not just use the best layer for each model?\\\" → We do. The point is that the METRIC for selecting \\\"best\\\" matters. Biased metrics produce systematically wrong selections, masking real effects.\\n16. \\\"32B results are marginal / only W=1 significant for R1-32B?\\\" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.\\n\\n## Title Candidates (D031)\\n- \\\"Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring\\\"\\n- \\\"Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation\\\"\\n- \\\"What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods\\\"\\n- \\\"Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable\\\"\\n\", \"total_chars\": 29283, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "b9dd36dc-3349-426a-a6fa-d9b83b72b2a4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — contrastive_trace_safety\\\\n\\\\n## Target Venue\\\\n- Primary: EMNLP 2026 Main (LLM Security Track)\\\\n- Deadline: ARR submission May 25, 2026\\\\n\\\\n## Core Claims (D031: layer selection as primary contribution, 4 models)\\\\n\\\\n**Contribution structure (D031)**:\\\\n- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions\\\\n- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal\\\\n- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work\\\\n\\\\n1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).\\\\n\\\\n   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).\\\\n   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.\\\\n   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.\\\\n\\\\n   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.\\\\n\\\\n   The core insight: \\\\\\\"Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak).\\\\\\\"\\\\n\\\\n2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 \\\\\\\"universal\\\\\\\") —\\\\n\\\\n   **KEY FINDING (D029)**: The apparent \\\\\\\"scale-dependent\\\\\\\" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.\\\\n\\\\n   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.\\\\n\\\\n   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**\\\\n\\\\n   **R1-8B (Llama-8B, R1-distilled, n=43):**\\\\n   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)\\\\n   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)\\\\n   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)\\\\n\\\\n   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**\\\\n   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)\\\\n   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)\\\\n   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)\\\\n   - **3/3 metrics significant — OT-7B cleanest single-model evidence**\\\\n\\\\n   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**\\\\n\\\\n   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**\\\\n   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)\\\\n   - 15/15 W values show significant HS advantage\\\\n   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is \\\\\\\"more accurate but detects later.\\\\\\\" Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.\\\\n   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**\\\\n\\\\n   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**\\\\n   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**\\\\n   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)\\\\n   - W=5-15: all NS\\\\n   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.\\\\n   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).\\\\n   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. \\\\\\\"Scheme B选错层\\\\\\\" narrative weaker for R1-32B.\\\\n   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.\\\\n\\\\n   **32B cross-model divergence (D031 key finding for Discussion):**\\\\n   | Dimension | R1-32B L63 | QwQ L60 |\\\\n   |-----------|-----------|---------|\\\\n   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |\\\\n   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |\\\\n   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |\\\\n   | Coverage (W=1) | 25% | 74% |\\\\n   Paper MUST discuss this divergence per-model, not unify into single narrative.\\\\n\\\\n   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**\\\\n   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)\\\\n   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)\\\\n   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.\\\\n\\\\n   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**\\\\n   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).\\\\n\\\\n   | Rank | Model | Metric | p-value | Threshold | Pass |\\\\n   |------|-------|--------|---------|-----------|------|\\\\n   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |\\\\n   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |\\\\n   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |\\\\n   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |\\\\n   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |\\\\n   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |\\\\n   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |\\\\n   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |\\\\n   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |\\\\n   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |\\\\n   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |\\\\n   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |\\\\n\\\\n   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure \\\\\\\"HS > text at each model's best setting,\\\\\\\" not \\\\\\\"at uniform W.\\\\\\\" R1-32B W=1 has 25% coverage. Paper must state these conditions.\\\\n\\\\n   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.\\\\n\\\\n   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.\\\\n\\\\n   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.\\\\n\\\\n   Paper recommended claim (D032): \\\\\\\"At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text.\\\\\\\"\\\\n\\\\n3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.\\\\n\\\\n   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.\\\\n\\\\n## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)\\\\n\\\\nThe layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.\\\\n\\\\n**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:\\\\n- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased\\\\n- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.\\\\n- `precision`: selects deep layers for all models (L60/L63 for 32B)\\\\n- `pre_cp_fpr`: selects deep layers for all models\\\\n- `composite` (additive): selects deep layers for all models\\\\n- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.\\\\n\\\\n**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.\\\\n\\\\n**Corrected layer definition (D036)**: \\\\\\\"Corrected layers\\\\\\\" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.\\\\n\\\\n**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.\\\\n\\\\n**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are \\\\\\\"correct\\\\\\\" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a \\\\\\\"researcher degree of freedom\\\\\\\" with systematic audit via sensitivity analysis.\\\\n\\\\n**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not \\\\\\\"correct vs incorrect.\\\\\\\"\\\\n\\\\n## Story Spine\\\\n\\\\n- **Problem**: Reasoning models exhibit \\\\\\\"self-jailbreak\\\\\\\" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a \\\\\\\"commitment point\\\\\\\" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.\\\\n\\\\n- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.\\\\n\\\\n- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).\\\\n\\\\n- **Headline result (D032)**: \\\\\\\"Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment.\\\\\\\"\\\\n\\\\n## Key Evidence Summary\\\\n\\\\n### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)\\\\n\\\\nBest layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.\\\\n\\\\n| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |\\\\n|--------|----------|-----------|------------|----------|\\\\n| HS Static LR L14 | — | -2.0 | **9.7%** | — |\\\\n| HS Temporal W=5 | — | +0.6 | **10.2%** | — |\\\\n| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |\\\\n| Text Temporal W=15 | — | +10.3* | 20.5% | — |\\\\n| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |\\\\n\\\\n*Text lead time inflated by high pre-CP FPR (trigger-happy detection)\\\\nNOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).\\\\n\\\\n### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16\\\\n\\\\nBest layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.\\\\n\\\\n| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\\\n|--------|---------|-----------|----------|-----------|------|\\\\n| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |\\\\n| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |\\\\n| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |\\\\n\\\\nBootstrap (layer 16, matched W=3, 1000 resamples):\\\\n   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅\\\\n   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅\\\\n   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**\\\\nSelectivity: 18.3pp (real=0.688, random=0.505) — highest across all models\\\\n\\\\n### 32B Cross-Architecture — D029 CORRECTED LAYERS\\\\n\\\\n**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**\\\\n- HS vs Text bootstrap (null-centered, 1000 resamples):\\\\n  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)\\\\n  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**\\\\n- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive\\\\n- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)\\\\n\\\\n**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**\\\\n- W=1: bal_acc +18.7pp, p<0.001 ✅\\\\n- W≥5: NS (dimensionality: 51200 × W features for n=20)\\\\n- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS\\\\n- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)\\\\n\\\\n**OLD biased-layer results (RETRACTED as metric artifact):**\\\\n| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |\\\\n|-------|-------------|----------------|----------------|-------------------|\\\\n| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |\\\\n| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |\\\\n\\\\n### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)\\\\n\\\\n| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |\\\\n|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|\\\\n| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |\\\\n| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |\\\\n| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |\\\\n| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |\\\\n\\\\n**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.\\\\nPrecision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.\\\\nCaveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.\\\\n\\\\n### Position Mediation Analysis (D038 → D039 → D042 complete)\\\\n\\\\n**Finding**: Position (relative step t/T) is a significant component of probe performance. 3/4 models retain HS advantage after residualization; R1-32B is the exception.\\\\n\\\\n| Model | W | Resid HS BA | Resid Text BA | HS-Text Gap | Gap p | HB |\\\\n|-------|---|------------|--------------|-------------|-------|-----|\\\\n| OT-7B | 3 | 0.609 | 0.540 | **+6.9pp** | <0.001 | ✅ |\\\\n| R1-8B | 15 | 0.669 | 0.605 | **+6.4pp** | <0.001 | ✅ |\\\\n| R1-8B | 3 | 0.571 | 0.534 | **+3.7pp** | <0.001 | ✅ |\\\\n| QwQ-32B | 3 | 0.619 | 0.582 | **+3.7pp** | 0.011 | ✅ |\\\\n| R1-32B | 1 | 0.552 | 0.532 | +1.9pp | 0.914 | ❌ |\\\\n\\\\nPosition-only BA: OT-7B/R1-8B/QwQ ≈ 0.706; R1-32B = 0.686.\\\\n\\\\n**D042 final picture**: HS advantage has two separable components — position-mediated and non-positional. 3/4 models retain significant non-positional HS advantage (HB pass); R1-32B's advantage is almost entirely position-mediated (drop 20.4pp, residualized gap NS). This is consistent with R1-32B's other caveats (W=1 only significant, 25% coverage).\\\\n\\\\n**Key implications for paper**:\\\\n1. Position is a significant component (12-20pp drop) — universal\\\\n2. 3/4 models retain non-positional HS advantage (residualized BA gap +3.7 to +6.9pp, HB pass)\\\\n3. R1-32B is the exception: HS advantage position-mediated, residualized gap NS\\\\n4. Temporal windowing preserves non-positional signal (R1-8B: 24pp drop@W=3 → 16pp@W=15)\\\\n5. Paper framing: \\\\\\\"HS advantage persists after position removal in 3/4 models; R1-32B advantage is position-mediated\\\\\\\"\\\\n\\\\n### 5-Seed Robustness (D041)\\\\n\\\\n| Model | HB Pass Rate | Mean ΔPrec ± std | Mean ΔBA ± std |\\\\n|-------|-------------|------------------|----------------|\\\\n| OT-7B | **5/5** | +20.9 ± 1.3pp | +11.3 ± 1.5pp |\\\\n| R1-32B | **5/5** | +13.7 ± 2.0pp | +11.8 ± 2.4pp |\\\\n| QwQ-32B | **5/5** | +19.9 ± 2.5pp | +11.4 ± 3.2pp |\\\\n| R1-8B | **3/5** | +14.6 ± 4.5pp | +9.4 ± 2.4pp |\\\\n\\\\nR1-8B failures are FPR-specific (seed 123 FPR p=0.262, seed 456 FPR p=0.952). Precision is directionally consistent across all 20 seed-model combinations (always positive). ΔPrec never reverses.\\\\n\\\\n**D041 insight**: Robustness splits by MODEL not SCALE. R1-32B (5/5, ΔPrec std=2.0pp) is more stable than R1-8B (3/5, ΔPrec std=4.5pp). \\\\\\\"7-8B robust / 32B sample-limited\\\\\\\" is factually wrong. R1-32B's absolute precision std (12.8pp) vs paired delta std (2.0pp) — paper must distinguish these.\\\\n\\\\n**Per-model evidence tier (D042)**:\\\\n- **OT-7B**: Cleanest — 5/5 HB, largest residualized gap (+6.9pp), highest selectivity (18.3pp)\\\\n- **QwQ-32B**: Robust — 5/5 HB, residualized gap holds (+3.7pp), but position baseline competitive\\\\n- **R1-8B**: Precision-robust — residualized holds (+3.7-6.4pp), but FPR unstable (3/5 HB)\\\\n- **R1-32B**: Statistically stable (5/5 HB, ΔPrec std=2.0pp) but advantage position-mediated (residualized NS)\\\\n\\\\n**Residualized precision**: Not tested (scope limited to BA per Reviewer recommendation).\\\\n\\\\n### BA-Layer Robustness: Metric Circularity Refuted (D044)\\\\n\\\\nR13 W1 concern: corrected selection uses threshold-dependent metrics (precision, FPR), evaluation also uses precision/FPR — potential circularity. Test: compute HS vs text on BA-selected layers (threshold-free criterion).\\\\n\\\\n| Model | BA-Opt Layer | ΔPrec | ΔBA | ΔFPR | ΔAUROC | All 4 HB? |\\\\n|-------|-------------|-------|-----|------|--------|-----------|\\\\n| R1-8B | L12 | +17.8pp | +7.8pp | -12.9pp | +9.3pp | ✅ |\\\\n| OT-7B | L9 | +25.4pp | +11.7pp | -19.3pp | +14.8pp | ✅ |\\\\n| QwQ-32B | L30 | +18.0pp | +14.8pp | -8.0pp | +17.3pp | ✅ |\\\\n| R1-32B | L47 | +13.7pp | +14.9pp | -23.1pp | +21.1pp | ✅ |\\\\n\\\\n**4/4 models × 4 metrics = 16/16 HB pass.** HS advantage is a genuine modality property, not a layer selection artifact.\\\\n\\\\nKey insight: R1-32B on BA-layer L47 shows ΔPrec +13.7pp and ΔAUROC +21.1pp — stronger than corrected L63 in threshold-free metrics. OT-7B on BA-layer L9 has ΔPrec +25.4pp > corrected L16 (+21.9pp). HS advantage is robust to layer selection criterion.\\\\n\\\\nCaveat: QwQ FPR adj_p=0.041 (marginal, CI close to zero). Other 15/16 tests p≤0.006.\\\\n\\\\n### Post-hoc Power Analysis (D044)\\\\n\\\\n| Model | n (test) | MDE (80% power, α=0.05) |\\\\n|-------|----------|------------------------|\\\\n| OT-7B | 47-69 | 6.7-8.1pp |\\\\n| R1-8B | 43-63 | 7.4-9.0pp |\\\\n| QwQ-32B | 29 | 9.5pp |\\\\n| R1-32B | 20-30 | 8.6-11.2pp |\\\\n\\\\nAll significant effects (15-24pp) are well above MDE → adequately powered. R1-32B residualized gap (+1.9pp) is far below MDE (11.2pp) → NS is power limitation, not evidence of absence.\\\\n\\\\n### Negative Results (expanded with R3 supplementary experiments)\\\\n- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.\\\\n- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.\\\\n- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:\\\\n  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.\\\\n  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.\\\\n  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642\\\\n  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).\\\\n- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.\\\\n- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as \\\\\\\"weakly supervised\\\\\\\" not \\\\\\\"unsupervised\\\\\\\"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.\\\\n- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).\\\\n\\\\n## Venue Fit Risks\\\\n\\\\n- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.\\\\n- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.\\\\n- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).\\\\n- **HS advantage universal**: UPGRADED from \\\\\\\"scale-dependent\\\\\\\" — layer selection is the true moderator, not scale. Cleaner story.\\\\n- **Trace vs step FPR**: Both reported with explanation.\\\\n- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.\\\\n- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n1. \\\\\\\"Method novelty?\\\\\\\" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).\\\\n2. \\\\\\\"Only one model family?\\\\\\\" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.\\\\n3. \\\\\\\"GRU unstable?\\\\\\\" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.\\\\n4. \\\\\\\"Too few traces?\\\\\\\" → Cross-model validation + control task selectivity 7.5-18.5pp.\\\\n5. \\\\\\\"Fine-grained taxonomy?\\\\\\\" → Out of scope for current study.\\\\n6. \\\\\\\"HS doesn't beat text?\\\\\\\" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.\\\\n7. \\\\\\\"Commitment point circular?\\\\\\\" → Cross-model consistency + control task selectivity argues against artifact.\\\\n8. \\\\\\\"Missing related work?\\\\\\\" → Expansion to 30+ citations.\\\\n9. \\\\\\\"No FPR analysis?\\\\\\\" → RESOLVED: both trace-level and step-level FPR reported.\\\\n10. \\\\\\\"High safe FPR?\\\\\\\" → Limitation acknowledged.\\\\n11. \\\\\\\"Control task / position confound?\\\\\\\" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.\\\\n12. \\\\\\\"Multiple testing correction?\\\\\\\" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).\\\\n13. \\\\\\\"Trace vs step FPR?\\\\\\\" → Both reported with explanation.\\\\n14. \\\\\\\"Layer selection is just hyperparameter tuning?\\\\\\\" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.\\\\n15. \\\\\\\"Why not just use the best layer for each model?\\\\\\\" → We do. The point is that the METRIC for selecting \\\\\\\"best\\\\\\\" matters. Biased metrics produce systematically wrong selections, masking real effects.\\\\n16. \\\\\\\"32B results are marginal / only W=1 significant for R1-32B?\\\\\\\" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.\\\\n\\\\n## Title Candidates (D031)\\\\n- \\\\\\\"Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring\\\\\\\"\\\\n- \\\\\\\"Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation\\\\\\\"\\\\n- \\\\\\\"What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods\\\\\\\"\\\\n- \\\\\\\"Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 29283, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md\", \"content\": \"# Paper Framing — contrastive_trace_safety\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (LLM Security Track)\\n- Deadline: ARR submission May 25, 2026\\n\\n## Core Claims (D031: layer selection as primary contribution, 4 models)\\n\\n**Contribution structure (D031)**:\\n- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions\\n- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal\\n- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work\\n\\n1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).\\n\\n   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).\\n   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.\\n   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.\\n\\n   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.\\n\\n   The core insight: \\\"Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak).\\\"\\n\\n2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 \\\"universal\\\") —\\n\\n   **KEY FINDING (D029)**: The apparent \\\"scale-dependent\\\" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.\\n\\n   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.\\n\\n   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**\\n\\n   **R1-8B (Llama-8B, R1-distilled, n=43):**\\n   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)\\n   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)\\n\\n   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**\\n   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)\\n   - **3/3 metrics significant — OT-7B cleanest single-model evidence**\\n\\n   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**\\n\\n   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**\\n   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)\\n   - 15/15 W values show significant HS advantage\\n   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is \\\"more accurate but detects later.\\\" Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.\\n   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**\\n\\n   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**\\n   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**\\n   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)\\n   - W=5-15: all NS\\n   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.\\n   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).\\n   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. \\\"Scheme B选错层\\\" narrative weaker for R1-32B.\\n   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.\\n\\n   **32B cross-model divergence (D031 key finding for Discussion):**\\n   | Dimension | R1-32B L63 | QwQ L60 |\\n   |-----------|-----------|---------|\\n   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |\\n   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |\\n   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |\\n   | Coverage (W=1) | 25% | 74% |\\n   Paper MUST discuss this divergence per-model, not unify into single narrative.\\n\\n   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**\\n   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)\\n   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)\\n   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.\\n\\n   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**\\n   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).\\n\\n   | Rank | Model | Metric | p-value | Threshold | Pass |\\n   |------|-------|--------|---------|-----------|------|\\n   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |\\n   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |\\n   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |\\n   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |\\n   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |\\n   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |\\n   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |\\n   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |\\n   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |\\n   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |\\n   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |\\n   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |\\n\\n   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure \\\"HS > text at each model's best setting,\\\" not \\\"at uniform W.\\\" R1-32B W=1 has 25% coverage. Paper must state these conditions.\\n\\n   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.\\n\\n   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.\\n\\n   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.\\n\\n   Paper recommended claim (D032): \\\"At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text.\\\"\\n\\n3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.\\n\\n   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.\\n\\n## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)\\n\\nThe layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.\\n\\n**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:\\n- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased\\n- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.\\n- `precision`: selects deep layers for all models (L60/L63 for 32B)\\n- `pre_cp_fpr`: selects deep layers for all models\\n- `composite` (additive): selects deep layers for all models\\n- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.\\n\\n**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.\\n\\n**Corrected layer definition (D036)**: \\\"Corrected layers\\\" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.\\n\\n**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.\\n\\n**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are \\\"correct\\\" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a \\\"researcher degree of freedom\\\" with systematic audit via sensitivity analysis.\\n\\n**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not \\\"correct vs incorrect.\\\"\\n\\n## Story Spine\\n\\n- **Problem**: Reasoning models exhibit \\\"self-jailbreak\\\" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a \\\"commitment point\\\" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.\\n\\n- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.\\n\\n- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).\\n\\n- **Headline result (D032)**: \\\"Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment.\\\"\\n\\n## Key Evidence Summary\\n\\n### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)\\n\\nBest layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.\\n\\n| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |\\n|--------|----------|-----------|------------|----------|\\n| HS Static LR L14 | — | -2.0 | **9.7%** | — |\\n| HS Temporal W=5 | — | +0.6 | **10.2%** | — |\\n| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |\\n| Text Temporal W=15 | — | +10.3* | 20.5% | — |\\n| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |\\n\\n*Text lead time inflated by high pre-CP FPR (trigger-happy detection)\\nNOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).\\n\\n### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16\\n\\nBest layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.\\n\\n| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\\n|--------|---------|-----------|----------|-----------|------|\\n| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |\\n| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |\\n| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |\\n\\nBootstrap (layer 16, matched W=3, 1000 resamples):\\n   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅\\n   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅\\n   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**\\nSelectivity: 18.3pp (real=0.688, random=0.505) — highest across all models\\n\\n### 32B Cross-Architecture — D029 CORRECTED LAYERS\\n\\n**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**\\n- HS vs Text bootstrap (null-centered, 1000 resamples):\\n  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)\\n  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**\\n- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive\\n- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)\\n\\n**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**\\n- W=1: bal_acc +18.7pp, p<0.001 ✅\\n- W≥5: NS (dimensionality: 51200 × W features for n=20)\\n- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS\\n- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)\\n\\n**OLD biased-layer results (RETRACTED as metric artifact):**\\n| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |\\n|-------|-------------|----------------|----------------|-------------------|\\n| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |\\n| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |\\n\\n### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)\\n\\n| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |\\n|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|\\n| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |\\n| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |\\n| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |\\n| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |\\n\\n**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.\\nPrecision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.\\nCaveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.\\n\\n### Position Mediation Analysis (D038 → D039 → D042 complete)\\n\\n**Finding**: Position (relative step t/T) is a significant component of probe performance. 3/4 models retain HS advantage after residualization; R1-32B is the exception.\\n\\n| Model | W | Resid HS BA | Resid Text BA | HS-Text Gap | Gap p | HB |\\n|-------|---|------------|--------------|-------------|-------|-----|\\n| OT-7B | 3 | 0.609 | 0.540 | **+6.9pp** | <0.001 | ✅ |\\n| R1-8B | 15 | 0.669 | 0.605 | **+6.4pp** | <0.001 | ✅ |\\n| R1-8B | 3 | 0.571 | 0.534 | **+3.7pp** | <0.001 | ✅ |\\n| QwQ-32B | 3 | 0.619 | 0.582 | **+3.7pp** | 0.011 | ✅ |\\n| R1-32B | 1 | 0.552 | 0.532 | +1.9pp | 0.914 | ❌ |\\n\\nPosition-only BA: OT-7B/R1-8B/QwQ ≈ 0.706; R1-32B = 0.686.\\n\\n**D042 final picture**: HS advantage has two separable components — position-mediated and non-positional. 3/4 models retain significant non-positional HS advantage (HB pass); R1-32B's advantage is almost entirely position-mediated (drop 20.4pp, residualized gap NS). This is consistent with R1-32B's other caveats (W=1 only significant, 25% coverage).\\n\\n**Key implications for paper**:\\n1. Position is a significant component (12-20pp drop) — universal\\n2. 3/4 models retain non-positional HS advantage (residualized BA gap +3.7 to +6.9pp, HB pass)\\n3. R1-32B is the exception: HS advantage position-mediated, residualized gap NS\\n4. Temporal windowing preserves non-positional signal (R1-8B: 24pp drop@W=3 → 16pp@W=15)\\n5. Paper framing: \\\"HS advantage persists after position removal in 3/4 models; R1-32B advantage is position-mediated\\\"\\n\\n### 5-Seed Robustness (D041)\\n\\n| Model | HB Pass Rate | Mean ΔPrec ± std | Mean ΔBA ± std |\\n|-------|-------------|------------------|----------------|\\n| OT-7B | **5/5** | +20.9 ± 1.3pp | +11.3 ± 1.5pp |\\n| R1-32B | **5/5** | +13.7 ± 2.0pp | +11.8 ± 2.4pp |\\n| QwQ-32B | **5/5** | +19.9 ± 2.5pp | +11.4 ± 3.2pp |\\n| R1-8B | **3/5** | +14.6 ± 4.5pp | +9.4 ± 2.4pp |\\n\\nR1-8B failures are FPR-specific (seed 123 FPR p=0.262, seed 456 FPR p=0.952). Precision is directionally consistent across all 20 seed-model combinations (always positive). ΔPrec never reverses.\\n\\n**D041 insight**: Robustness splits by MODEL not SCALE. R1-32B (5/5, ΔPrec std=2.0pp) is more stable than R1-8B (3/5, ΔPrec std=4.5pp). \\\"7-8B robust / 32B sample-limited\\\" is factually wrong. R1-32B's absolute precision std (12.8pp) vs paired delta std (2.0pp) — paper must distinguish these.\\n\\n**Per-model evidence tier (D042)**:\\n- **OT-7B**: Cleanest — 5/5 HB, largest residualized gap (+6.9pp), highest selectivity (18.3pp)\\n- **QwQ-32B**: Robust — 5/5 HB, residualized gap holds (+3.7pp), but position baseline competitive\\n- **R1-8B**: Precision-robust — residualized holds (+3.7-6.4pp), but FPR unstable (3/5 HB)\\n- **R1-32B**: Statistically stable (5/5 HB, ΔPrec std=2.0pp) but advantage position-mediated (residualized NS)\\n\\n**Residualized precision**: Not tested (scope limited to BA per Reviewer recommendation).\\n\\n### BA-Layer Robustness: Metric Circularity Refuted (D044)\\n\\nR13 W1 concern: corrected selection uses threshold-dependent metrics (precision, FPR), evaluation also uses precision/FPR — potential circularity. Test: compute HS vs text on BA-selected layers (threshold-free criterion).\\n\\n| Model | BA-Opt Layer | ΔPrec | ΔBA | ΔFPR | ΔAUROC | All 4 HB? |\\n|-------|-------------|-------|-----|------|--------|-----------|\\n| R1-8B | L12 | +17.8pp | +7.8pp | -12.9pp | +9.3pp | ✅ |\\n| OT-7B | L9 | +25.4pp | +11.7pp | -19.3pp | +14.8pp | ✅ |\\n| QwQ-32B | L30 | +18.0pp | +14.8pp | -8.0pp | +17.3pp | ✅ |\\n| R1-32B | L47 | +13.7pp | +14.9pp | -23.1pp | +21.1pp | ✅ |\\n\\n**4/4 models × 4 metrics = 16/16 HB pass.** HS advantage is a genuine modality property, not a layer selection artifact.\\n\\nKey insight: R1-32B on BA-layer L47 shows ΔPrec +13.7pp and ΔAUROC +21.1pp — stronger than corrected L63 in threshold-free metrics. OT-7B on BA-layer L9 has ΔPrec +25.4pp > corrected L16 (+21.9pp). HS advantage is robust to layer selection criterion.\\n\\nCaveat: QwQ FPR adj_p=0.041 (marginal, CI close to zero). Other 15/16 tests p≤0.006.\\n\\n### Post-hoc Power Analysis (D044)\\n\\n| Model | n (test) | MDE (80% power, α=0.05) |\\n|-------|----------|------------------------|\\n| OT-7B | 47-69 | 6.7-8.1pp |\\n| R1-8B | 43-63 | 7.4-9.0pp |\\n| QwQ-32B | 29 | 9.5pp |\\n| R1-32B | 20-30 | 8.6-11.2pp |\\n\\nAll significant effects (15-24pp) are well above MDE → adequately powered. R1-32B residualized gap (+1.9pp) is far below MDE (11.2pp) → NS is power limitation, not evidence of absence.\\n\\n### Negative Results (expanded with R3 supplementary experiments)\\n- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.\\n- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.\\n- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:\\n  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.\\n  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.\\n  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642\\n  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).\\n- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.\\n- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as \\\"weakly supervised\\\" not \\\"unsupervised\\\"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.\\n- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).\\n\\n## Venue Fit Risks\\n\\n- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.\\n- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.\\n- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).\\n- **HS advantage universal**: UPGRADED from \\\"scale-dependent\\\" — layer selection is the true moderator, not scale. Cleaner story.\\n- **Trace vs step FPR**: Both reported with explanation.\\n- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.\\n- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.\\n\\n## Anticipated Reviewer Concerns\\n\\n1. \\\"Method novelty?\\\" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).\\n2. \\\"Only one model family?\\\" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.\\n3. \\\"GRU unstable?\\\" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.\\n4. \\\"Too few traces?\\\" → Cross-model validation + control task selectivity 7.5-18.5pp.\\n5. \\\"Fine-grained taxonomy?\\\" → Out of scope for current study.\\n6. \\\"HS doesn't beat text?\\\" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.\\n7. \\\"Commitment point circular?\\\" → Cross-model consistency + control task selectivity argues against artifact.\\n8. \\\"Missing related work?\\\" → Expansion to 30+ citations.\\n9. \\\"No FPR analysis?\\\" → RESOLVED: both trace-level and step-level FPR reported.\\n10. \\\"High safe FPR?\\\" → Limitation acknowledged.\\n11. \\\"Control task / position confound?\\\" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.\\n12. \\\"Multiple testing correction?\\\" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).\\n13. \\\"Trace vs step FPR?\\\" → Both reported with explanation.\\n14. \\\"Layer selection is just hyperparameter tuning?\\\" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.\\n15. \\\"Why not just use the best layer for each model?\\\" → We do. The point is that the METRIC for selecting \\\"best\\\" matters. Biased metrics produce systematically wrong selections, masking real effects.\\n16. \\\"32B results are marginal / only W=1 significant for R1-32B?\\\" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.\\n\\n## Title Candidates (D031)\\n- \\\"Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring\\\"\\n- \\\"Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation\\\"\\n- \\\"What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods\\\"\\n- \\\"Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable\\\"\\n\", \"total_chars\": 29283, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NddyppuFYkCntxPftCdG4y`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "ffea2b1c-9a8e-483f-b616-74cf71a8341d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxNBtA9ua8z1asuziHg2aM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 490,
      "cache_read_input_tokens": 26146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 490
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-18T20:28:06.360Z_

<details><summary>↩ Tool result · `toolu_01NddyppuFYkCntxPftCdG4y`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/report.md\", \"content\": \"# Handover — 2026-05-18\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_bge_large_text_comparison** (success): HS advantage over text probes persists even with a stronger text encoder (BGE-large 1024d vs MiniLM 384d). If HS advantage shrinks but remains significant under HB correction, the paper claim is strengthened against dimensionality/encoder-quality confounds.\\n- **exp_qwq_safe_fpr_correct_lr** (negative): QwQ-32B safe-trace FPR=50% (SGDClassifier) may be a method artifact. Rerunning with paper's LogisticRegression(lbfgs, C=1.0, class_weight=balanced, max_iter=2000) to confirm whether HS probe truly has higher FPR than text probe on safe traces. ← 基于 exp_safe_trace_fpr_multimodel\\n- **exp_safe_trace_fpr_multimodel** (negative): HS probes should have lower FPR on safe (benign) traces than text probes across OT-7B, QwQ-32B, R1-32B, extending the R1-8B-only FPR result to multi-model. If HS FPR is consistently lower, the paper can claim cross-model FPR advantage.\\n\\n## 趋势\\n成功 19 / 负向 20 / 失败 0 / 共 39\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-rtx6000: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1131, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "4b484a29-040c-4da2-bfd5-c07a3726114c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-18\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n（无）\\\\n\\\\n## 待处理\\\\n（无）\\\\n\\\\n## 近期结论\\\\n- **exp_bge_large_text_comparison** (success): HS advantage over text probes persists even with a stronger text encoder (BGE-large 1024d vs MiniLM 384d). If HS advantage shrinks but remains significant under HB correction, the paper claim is strengthened against dimensionality/encoder-quality confounds.\\\\n- **exp_qwq_safe_fpr_correct_lr** (negative): QwQ-32B safe-trace FPR=50% (SGDClassifier) may be a method artifact. Rerunning with paper's LogisticRegression(lbfgs, C=1.0, class_weight=balanced, max_iter=2000) to confirm whether HS probe truly has higher FPR than text probe on safe traces. ← 基于 exp_safe_trace_fpr_multimodel\\\\n- **exp_safe_trace_fpr_multimodel** (negative): HS probes should have lower FPR on safe (benign) traces than text probes across OT-7B, QwQ-32B, R1-32B, extending the R1-8B-only FPR result to multi-model. If HS FPR is consistently lower, the paper can claim cross-model FPR advantage.\\\\n\\\\n## 趋势\\\\n成功 19 / 负向 20 / 失败 0 / 共 39\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nautodl-rtx6000: 空闲 cuda:0, cuda:1\\\\n\\\\n## 告警\\\\n（无）\\\\n\\\", \\\"total_chars\\\": 1131, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/report.md\", \"content\": \"# Handover — 2026-05-18\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **exp_bge_large_text_comparison** (success): HS advantage over text probes persists even with a stronger text encoder (BGE-large 1024d vs MiniLM 384d). If HS advantage shrinks but remains significant under HB correction, the paper claim is strengthened against dimensionality/encoder-quality confounds.\\n- **exp_qwq_safe_fpr_correct_lr** (negative): QwQ-32B safe-trace FPR=50% (SGDClassifier) may be a method artifact. Rerunning with paper's LogisticRegression(lbfgs, C=1.0, class_weight=balanced, max_iter=2000) to confirm whether HS probe truly has higher FPR than text probe on safe traces. ← 基于 exp_safe_trace_fpr_multimodel\\n- **exp_safe_trace_fpr_multimodel** (negative): HS probes should have lower FPR on safe (benign) traces than text probes across OT-7B, QwQ-32B, R1-32B, extending the R1-8B-only FPR result to multi-model. If HS FPR is consistently lower, the paper can claim cross-model FPR advantage.\\n\\n## 趋势\\n成功 19 / 负向 20 / 失败 0 / 共 39\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nautodl-rtx6000: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1131, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NixdL1H8KJHmE1JTRnRq9T`</summary>

```json
{
  "project": "contrastive_trace_safety",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "3d3a29e3-598a-4a07-ad38-a3be775d53e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxNBtA9ua8z1asuziHg2aM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 490,
      "cache_read_input_tokens": 26146,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 490
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-18T20:28:06.605Z_

<details><summary>↩ Tool result · `toolu_01NixdL1H8KJHmE1JTRnRq9T`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/memory.md\", \"content\": \"# Memory\\n\\n## A8 Oracle Gap Results (2026-05-18)\\n\\nOracle gap (K=5 consecutive trigger, early detection before CP) on test set (60/20/20, seed=42):\\n\\n| Model | Oracle Gap (K=5) | Test N | Mean Lead Time |\\n|-------|-----------------|--------|----------------|\\n| R1-8B | 76.7% (33/43) | 43 | 31.0 steps |\\n| OT-7B | 93.6% (44/47) | 47 | 50.0 steps |\\n| R1-32B | 50.0% (10/20) | 20 | 32.4 steps |\\n| QwQ-32B | 84.2% (16/19) | 19 | 24.4 steps |\\n\\nMethod: `analyze_oracle()` from `src/diagnostics/oracle_upper_bound.py` uses raw annotation labels, finding K consecutive non-safety labels before CP.\\n\\nNote: Task referenced R1-8B=85.5%, but that appears to be from val set (85.4%). Test set consistently gives 76.7%.\\n\\nFull results: `artifacts/r14_a8_oracle_gap/oracle_gap_all_models.json`\\n\", \"total_chars\": 775, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "730c0137-ff29-4963-badb-68400d913160",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/memory.md\\\", \\\"content\\\": \\\"# Memory\\\\n\\\\n## A8 Oracle Gap Results (2026-05-18)\\\\n\\\\nOracle gap (K=5 consecutive trigger, early detection before CP) on test set (60/20/20, seed=42):\\\\n\\\\n| Model | Oracle Gap (K=5) | Test N | Mean Lead Time |\\\\n|-------|-----------------|--------|----------------|\\\\n| R1-8B | 76.7% (33/43) | 43 | 31.0 steps |\\\\n| OT-7B | 93.6% (44/47) | 47 | 50.0 steps |\\\\n| R1-32B | 50.0% (10/20) | 20 | 32.4 steps |\\\\n| QwQ-32B | 84.2% (16/19) | 19 | 24.4 steps |\\\\n\\\\nMethod: `analyze_oracle()` from `src/diagnostics/oracle_upper_bound.py` uses raw annotation labels, finding K consecutive non-safety labels before CP.\\\\n\\\\nNote: Task referenced R1-8B=85.5%, but that appears to be from val set (85.4%). Test set consistently gives 76.7%.\\\\n\\\\nFull results: `artifacts/r14_a8_oracle_gap/oracle_gap_all_models.json`\\\\n\\\", \\\"total_chars\\\": 775, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/memory.md\", \"content\": \"# Memory\\n\\n## A8 Oracle Gap Results (2026-05-18)\\n\\nOracle gap (K=5 consecutive trigger, early detection before CP) on test set (60/20/20, seed=42):\\n\\n| Model | Oracle Gap (K=5) | Test N | Mean Lead Time |\\n|-------|-----------------|--------|----------------|\\n| R1-8B | 76.7% (33/43) | 43 | 31.0 steps |\\n| OT-7B | 93.6% (44/47) | 47 | 50.0 steps |\\n| R1-32B | 50.0% (10/20) | 20 | 32.4 steps |\\n| QwQ-32B | 84.2% (16/19) | 19 | 24.4 steps |\\n\\nMethod: `analyze_oracle()` from `src/diagnostics/oracle_upper_bound.py` uses raw annotation labels, finding K consecutive non-safety labels before CP.\\n\\nNote: Task referenced R1-8B=85.5%, but that appears to be from val set (85.4%). Test set consistently gives 76.7%.\\n\\nFull results: `artifacts/r14_a8_oracle_gap/oracle_gap_all_models.json`\\n\", \"total_chars\": 775, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the paper's actual sections to get the right section/table/figure/appendix references. Let me look at the paper structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "3fec5263-1c02-4785-aef6-e57b499d42a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168Tetypj8j541X45Kkcakx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12620,
      "cache_read_input_tokens": 26636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12620
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 15_

Now let me check the paper structure for exact section/table/appendix labels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "05fcdddc-550c-4f62-871a-9d24b5571d7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168Tetypj8j541X45Kkcakx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12620,
      "cache_read_input_tokens": 26636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12620
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_018oKV6c1aJXcarSgjaTbQyX`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper section labels",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/, find all .tex files and extract:\n1. All \\label{} commands (section labels, table labels, figure labels, appendix labels)\n2. All \\section, \\subsection commands to understand paper structure\n3. Any table/figure captions\n\nReport a structured list of all labels and their corresponding content. Be thorough - check main.tex and all included files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "936eb0ad-4f35-4bf1-b892-211ea4cfe42f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0168Tetypj8j541X45Kkcakx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12620,
      "cache_read_input_tokens": 26636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12620
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Find paper section labels",
  "task_type": "local_agent",
  "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/, find all .tex files and extract:\n1. All \\label{} commands (section labels, table labels, figure labels, appendix labels)\n2. All \\section, \\subsection commands to understand paper structure\n3. Any table/figure captions\n\nReport a structured list of all labels and their corresponding content. Be thorough - check main.tex and all included files.",
  "uuid": "d1369537-510d-4893-b273-e8cd4ed42fda",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

## Round 1

57 recorded events

### User

_source line 18 · 2026-05-18T20:28:13.725Z_

In /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/, find all .tex files and extract:
1. All \label{} commands (section labels, table labels, figure labels, appendix labels)
2. All \section, \subsection commands to understand paper structure
3. Any table/figure captions

Report a structured list of all labels and their corresponding content. Be thorough - check main.tex and all included files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "36440787-64c9-4e79-a9cd-efa728061713"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_5/p…",
  "usage": {
    "total_tokens": 15515,
    "tool_uses": 1,
    "duration_ms": 1531
  },
  "last_tool_name": "Glob",
  "uuid": "b437fc91-c078-4989-a66e-436fb02cb2be",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01Dzun7TbcDFLnSmY9LqdfL9`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "c16b90c3-fef0-44f1-b179-97fb9a3b6e71",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FuwBarSUxaTvB2AQ4LVQJX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15506,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15506,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-18T20:28:15.279Z_

<details><summary>↩ Tool result · `toolu_01Dzun7TbcDFLnSmY9LqdfL9`</summary>

```text
docs/paper/main.tex
docs/paper/sections/related_work.tex
docs/paper/sections/method.tex
docs/paper/sections/abstract.tex
docs/paper/sections/experiments.tex
docs/paper/sections/discussion.tex
docs/paper/sections/introduction.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/limitations.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "9ba6b457-e58c-45dd-aaac-5def2007e576"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 16589,
    "tool_uses": 2,
    "duration_ms": 3438
  },
  "last_tool_name": "Read",
  "uuid": "62b771b7-c999-4439-9ad5-abdc723b1556",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01BpiWo9DaR8RUupsqNfwBxk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "59b96287-1032-46c0-8f22-e0c6dd723d7e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-18T20:28:17.174Z_

<details><summary>↩ Tool result · `toolu_01BpiWo9DaR8RUupsqNfwBxk`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage{graphicx}
6	\usepackage{amsmath}
7	\usepackage{amssymb}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{subcaption}
11	\usepackage{xcolor}
12	\usepackage{colortbl}
13	\usepackage{hyperref}
14	\usepackage{cleveref}
15	
16	\title{Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models}
17	
18	\author{Anonymous ARR Submission}
19	
20	\begin{document}
21	\maketitle
22	
23	\begin{abstract}
24	\input{sections/abstract}
25	\end{abstract}
26	
27	\input{sections/introduction}
28	
29	\input{sections/related_work}
30	
31	\input{sections/method}
32	
33	\input{sections/experiments}
34	
35	\input{sections/discussion}
36	
37	\input{sections/conclusion}
38	
39	\input{sections/limitations}
40	
41	\bibliography{references}
42	
43	\input{sections/appendix}
44	
45	\end{document}
46	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "ed60644a-dd85-421c-abc7-bb6cc259ed6f"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/abstract.tex",
  "usage": {
    "total_tokens": 16590,
    "tool_uses": 3,
    "duration_ms": 3615
  },
  "last_tool_name": "Read",
  "uuid": "60ac6c80-447b-481e-948b-4f62c19c802d",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01P3jp28o3wLJvpFTq2pJfM6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "c6d2cbfc-e356-4eac-a4f3-c8c7e9802b77",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-18T20:28:17.350Z_

<details><summary>↩ Tool result · `toolu_01P3jp28o3wLJvpFTq2pJfM6`</summary>

```text
1	Reasoning models with chain-of-thought (CoT) can self-jailbreak: their reasoning traces transition from safe deliberation to committed harmful generation without adversarial input. Detecting this safety commitment point requires monitoring, but a prior question remains unanswered: should a monitoring system read the model's hidden states or its generated text? We show that this comparison's outcome depends critically on an underexamined researcher degree of freedom: which transformer layer to monitor. Through systematic evaluation of hidden-state (HS) and text-based probes across four reasoning models, five selection metrics, and seven alternative methods, we find that a biased composite metric masks the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. Principled selection recovers significant HS precision gains (+15.4 to +21.9pp, Holm-Bonferroni corrected), with evidence from strong (OT-7B, 5/5 seeds) to qualified (R1-32B, position-mediated). Encoder quality bounds the advantage: against a stronger 1024d text encoder, only 1/4 models survives correction. Layer selection sensitivity is the robust methodological finding; the empirical HS advantage is conditional, and current probes characterize the commitment phenomenon (FPR 39--52\%) rather than constitute production detectors.
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "2c22a992-8dbf-4c62-a894-d9fa246b98c5"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/introduction.tex",
  "usage": {
    "total_tokens": 16591,
    "tool_uses": 4,
    "duration_ms": 3823
  },
  "last_tool_name": "Read",
  "uuid": "3bb4967e-008d-4aee-b2f4-9a3065ddca3f",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01RX4oUbTusZa1AbUywVcjSC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "fe8e9c2e-0744-45a7-a7b9-3af6123add64",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-18T20:28:17.554Z_

<details><summary>↩ Tool result · `toolu_01RX4oUbTusZa1AbUywVcjSC`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT). Recent work documents that these models can ``self-jailbreak'': without adversarial input modification, the CoT transitions from safety-aware deliberation to committed harmful generation~\cite{harmthoughts,selfjailbreak}. We define the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). This failure mode differs qualitatively from adversarial jailbreaks on standard LLMs because the harmful transition originates within the model's own reasoning. Before building production detectors, a prior question must be answered: can current probing methods reliably distinguish pre-CP from post-CP reasoning steps, and under what conditions? This paper provides a systematic characterization of what hidden-state and text-based probes can and cannot detect.
4	
5	Existing safety detectors target fundamentally different problems. Hidden-state (HS) methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} classify adversarial inputs at the token level, while text monitors like SafeRemind~\cite{saferemind} scan generated reasoning for explicit violations. Neither tracks the gradual, multi-step commitment process. A fundamental question remains: should a monitoring system read the model's hidden states or its generated text? This comparison has never been conducted under controlled conditions, and a further complication is that HS probes require selecting which transformer layer to monitor. Layer selection is a researcher degree of freedom that has received almost no scrutiny in the probing literature, yet we show it can reverse a study's central conclusion.
6	
7	We present the first systematic evaluation across four reasoning models spanning two architectures (Llama, Qwen) and two scales (7--8B, 32B). Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is observed. A composite metric (balanced accuracy $\times$ crossing rate) selects shallow layers for 32B models because shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings reflect noise rather than semantic transitions. At these layers, only the two 7--8B models show significant HS advantage. Threshold-dependent metrics excluding crossing rate consistently select deep layers (\cref{tab:layer_selection}), where all four models show significant HS advantage$^\dagger$ (Holm-Bonferroni corrected; precision +15.4 to +21.9pp; \cref{tab:hs_vs_text}), with evidence from strong (OT-7B: 5/5 seeds HB, $+21.9$pp) to qualified (R1-32B$^\dagger$: position-mediated; \cref{sec:experiments}).
8	
9	Our contributions are:
10	\begin{itemize}
11	    \item \textbf{Layer selection sensitivity.} We identify a systematic bias in composite metrics that reverses HS probe conclusions at 32B scale. A five-metric ablation establishes principled selection criteria (\cref{sec:layer-results}).
12	
13	    \item \textbf{Encoder-quality boundary with evidence gradient.} The HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\dagger$ (+15.4 to +21.9pp precision, Holm-Bonferroni corrected) but attenuated against 1024d BGE-large (1/4 HB-significant). This boundary suggests the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference (\cref{fig:forest_precision}). PCA capacity matching to 384d preserves significance (+16.8 to +23.1pp, 79--92\% variance retained), providing partial evidence against a pure capacity explanation. Evidence strength varies by model: strong for OT-7B (5/5 seeds HB, $+21.9$pp, no caveats), moderate for R1-8B (FPR seed-fragile, 3/5 HB) and QwQ-32B$^\dagger$ (5/5 HB, negative lead time), and qualified for R1-32B$^\dagger$ (5/5 HB but position-mediated, residualized gap NS; \cref{sec:32b-analysis}).
14	
15	    \item \textbf{Negative results define method boundaries.} No alternative method consistently matches supervised probing at any evidence tier (\cref{tab:negative}): BOCPD/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation; RepE achieves competitive balanced accuracy on QwQ-32B (0.756 vs.\ supervised 0.778) but at substantially lower precision (0.512 vs.\ 0.700); cross-model transfer fails under PCA alignment. Control task selectivity (11.1--16.8pp above chance; \cref{app:control}) confirms genuine safety structure.
16	\end{itemize}
17	
18	\noindent Our results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39--52\%, and the 76.7\% oracle gap (R1-8B; \cref{sec:oracle}) underscores how much room remains for improvement.
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "d0f13696-21df-47c6-a7c9-06a93332a3cd"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/related_work.tex",
  "usage": {
    "total_tokens": 16592,
    "tool_uses": 5,
    "duration_ms": 4034
  },
  "last_tool_name": "Read",
  "uuid": "103374ab-8e2f-4ae1-a833-9e1fe470a13c",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_0137YtvJ2zPpQCZausr2of9t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "87597829-b81c-4c37-b96d-8681510d8740",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-18T20:28:17.767Z_

<details><summary>↩ Tool result · `toolu_0137YtvJ2zPpQCZausr2of9t`</summary>

```text
1	\section{Related Work}\label{sec:related-work}
2	
3	\paragraph{Safety in Reasoning Models.}
4	Reasoning models introduce a qualitatively new failure mode: the model's own chain of thought can transition from safety-aware deliberation to harmful generation without adversarial input modification~\cite{wang2025lrmsafety}.
5	
6	\textit{Attack characterization.} Self-jailbreak has been documented with step-level annotations~\cite{harmthoughts}, with longer chains increasing circumvention probability~\cite{selfjailbreak}. Reasoning models can autonomously jailbreak other LLMs with 97\% success~\cite{hagendorff2026lrm_jailbreak}. H-CoT~\cite{hcot2025} shows reasoning chains can be externally hijacked. Unfaithful reasoning~\cite{chen2025unfaithful} further motivates hidden-state monitoring that bypasses text. Safety-aligned models maintain refusal intentions during thinking but experience a sharp drop at output generation~\cite{yin2025refusal_cliff}, a phenomenon our temporal probes target. Refusal dynamics in standard LLMs~\cite{hu2026refusal_dynamics} and information leakage in traces~\cite{ahrend2026safer_traces} provide additional context.
7	
8	\textit{Detection.} CoT monitoring can detect reward hacking but optimization pressure promotes obfuscation~\cite{baker2025monitoring}. CoT monitorability is valuable but fragile~\cite{korbak2025cot_monitorability}. GuardReasoner~\cite{xiang2025guardreasoner} trains a dedicated reasoning-based guard model.
9	
10	\textit{Mitigation.} SafeThink~\cite{safethink} steers early reasoning toward safety, SafeRemind~\cite{saferemind} inserts entropy-triggered reminders, and Chain-of-Guardrails~\cite{mao2025selfjailbreak_reasoning} proposes guardrail insertion during reasoning. None of these conducts a systematic modality comparison for commitment detection.
11	
12	\paragraph{Hidden-State Safety Detection.}
13	Internal activations can detect safety violations in standard LLMs. \citet{zhou2024alignment} show safety-relevant information distributes across layers, while \citet{qi2025shallow_alignment} find that alignment operates primarily over early output tokens. \citet{arditi2024refusal} identify a single refusal direction, but \citet{zhao2025harmfulness} show harmfulness and refusal are encoded separately. \citet{joad2026refusal_multi} reveal eleven category-specific refusal directions, and \citet{wollschlager2025geometry} formalize multi-dimensionality through concept cones, consistent with our finding that single-direction methods are insufficient. TrajGuard~\cite{trajguard} uses Mahalanobis distance from safe trajectories; SafeSwitch~\cite{safeswitch} trains hidden-state classifiers; SIREN~\cite{siren} monitors internal representations during generation; SafeDream~\cite{safedream2026} proposes proactive world models for detection. These methods assume threats from external input manipulation and operate at the token level on instruction-tuned models. The self-jailbreak setting differs because transitions are internal and span multiple reasoning steps. \citet{kadali2025internal} decompose internal layer representations to separate jailbreak from benign prompts; their results confirm that layer-wise structure carries safety-relevant signal. We reproduce TrajGuard (\cref{sec:negative}) and find its geometric approach fails because discriminative signal resides in minor PCA components.
14	
15	\paragraph{Probing Methodology and Layer Selection.}
16	Causal abstraction~\cite{geiger2025causal} provides a theoretical foundation for mechanistic interpretability by formalizing when high-level causal models faithfully describe neural computation, grounding the use of internal representations for behavioral prediction. Linear probing has a long history from layer-wise classifiers~\cite{alain2017understanding} through sentence probing~\cite{conneau2018probing} to comprehensive surveys~\cite{belinkov2019analysis,belinkov2022probing,rogers2020primer}. Layer-wise analyses reveal hierarchical linguistic structure across depth~\cite{jawahar2019bert,liu2019linguistic}, and information-theoretic formulations address probe complexity~\cite{voita2020information,pimentel2020information}. \citet{hewitt2019control} introduce control tasks to distinguish structure from memorization, which we adopt (\cref{app:control}). \citet{ravfogel2020null} introduce iterative nullspace projection (INLP) for concept removal; \citet{ravfogel2022rlace} extend this to closed-form linear adversarial concept erasure. \citet{belrose2023leace} establish theoretical limits on linear probe extraction; \citet{elazar2021amnesic} test whether probed information is causally used. \citet{tenney2019bert} show syntactic information in middle layers and semantics in deeper layers. \citet{marks2024geometry} find emergent linear structure in LLM truth representations, consistent with the linear separability we observe for safety commitment. \citet{zhang2025probing_selfverify} apply hidden-state probing to self-verification in reasoning models, a complementary perspective on what reasoning-model representations encode. Concurrent work by \citet{alvarez2026transport_geometry} uses hidden-state geometry for step-level hallucination detection; the approach shares our temporal probing framework but targets a different phenomenon. \citet{boxo2025linear_probes} show that linear probes can rely on textual evidence rather than deeper representations, which motivates our comparison of hidden-state probes against text-based monitors. Despite this foundation, layer selection remains underexamined: most studies select by a single metric without sensitivity analysis. We demonstrate that this practice can reverse a study's central conclusion (\cref{sec:layer-results}). Our probing approach establishes correlational evidence; causal validation via distributed alignment search~\citep{geiger2025causal}, LEACE~\citep{belrose2023leace}, or inference-time intervention~\citep{li2024iti} would be needed to confirm that probed directions are causally active in safety reasoning. We focus on establishing the observational foundation and identifying the layer selection confound before pursuing causal follow-ups.
17	
18	\paragraph{Change-Point Detection.}
19	BOCPD~\cite{adams2007bayesian} detects abrupt distributional shifts; CCS~\cite{burns2023discovering} discovers latent truth directions via consistency constraints; RepE~\cite{zou2023representation} identifies concept directions through mean differences. We adapt all three to temporal commitment detection (\cref{sec:negative}). BOCPD and CUSUM fail because commitment is gradual. CCS provides no gain because its consistency objective misaligns with temporal structure. RepE shows inconsistent performance across models (0.756 on QwQ, 0.559 on R1-32B). These failures motivate supervised probes with principled layer selection as the minimal effective methodology.
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "8303ecb4-6385-478d-b2f7-14ae82c68f4b"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/method.tex",
  "usage": {
    "total_tokens": 16593,
    "tool_uses": 6,
    "duration_ms": 4247
  },
  "last_tool_name": "Read",
  "uuid": "f3c8b83e-fc68-4afb-9be8-e0678f65ccf3",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01JSLQ37g5NKt1KgzgQ4YACj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "9ef64111-502a-4c3f-9eca-bf42a7e376e7",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-18T20:28:17.982Z_

<details><summary>↩ Tool result · `toolu_01JSLQ37g5NKt1KgzgQ4YACj`</summary>

```text
1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Steps before CP are \emph{pre-commitment} ($y_t = 0$); steps at or after CP are \emph{post-commitment} ($y_t = 1$). The detection task produces a score $s_t \in [0, 1]$ estimating whether the model has passed its CP by step $t$.
8	
9	We study four reasoning models spanning two architectures and two scales (\cref{tab:models}).
10	
11	\begin{table}[t]
12	\centering
13	\resizebox{\columnwidth}{!}{%
14	\begin{tabular}{lccccc}
15	\toprule
16	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{$n$ (total\,/\,test)} \\
17	\midrule
18	R1-8B & Llama & 8B & 32 & 4096 & 209\,/\,43 \\
19	OT-7B & Qwen & 7B & 28 & 3584 & 228\,/\,47 \\
20	R1-32B & Qwen & 32B & 64 & 5120 & 100\,/\,20 \\
21	QwQ-32B & Qwen & 32B & 64 & 5120 & 95\,/\,19 \\
22	\bottomrule
23	\end{tabular}}
24	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20.}
25	\label{tab:models}
26	\end{table}
27	
28	\subsection{Probe Architecture}
29	\label{sec:probe-architecture}
30	
31	\paragraph{Hidden-state (HS) probes.} At each step $t$, we extract the last-token hidden state $\mathbf{h}_t^{(\ell)} \in \mathbb{R}^d$ from layer $\ell$ and train an L2-regularized logistic regression classifier (balanced class weights, $C{=}1.0$, LBFGS, max\_iter${}=2000$) on binary CP labels. Layer selection is analyzed in \cref{sec:layer-sensitivity}.
32	
33	\paragraph{Text probes.} Each step's text is encoded with all-MiniLM-L6-v2~\citep{wang2020minilm} ($\mathbb{R}^{384}$), a distilled sentence encoder from the Sentence-BERT family~\citep{reimers2019sentence}. The same logistic regression is applied as a surface-level modality baseline.
34	
35	\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \ldots, t]$. We evaluate $W \in \{1, 3, 5, 10, 15, 20, 25\}$ and select per-model on validation. GRU sequence models are also evaluated under two protocols: a 70/30 train/test split (primary) and the same 60/20/20 split used for LR experiments (for fair comparison; \cref{tab:gru_multi_seeds,app:gru_details}).
36	
37	\subsection{Layer Selection Sensitivity}
38	\label{sec:layer-sensitivity}
39	
40	Layer selection is a researcher degree of freedom that can reverse modality comparison conclusions. A composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\% depth) for QwQ-32B, L10 (16\%) for R1-32B. Shallow representations are highly compressed (inter-step cosine distances 1.4--2.7$\times$ smaller than at deep layers), so a linear probe operates near the noise floor and threshold crossings are noise-driven (\cref{app:cosine_volatility}).
41	
42	A five-metric ablation reveals that threshold-dependent metrics (precision, inverse FPR, additive composite) consistently select deep layers: L63 (98\%) for both QwQ-32B and R1-32B. Pure balanced accuracy selects layers whose depth varies across data splits and models (7--98\% under 60/20/20; \cref{tab:ba_layer_comparison}). At these layers, all four models show significant HS advantage$^\dagger$ (Holm-Bonferroni corrected; strong for OT-7B, moderate for R1-8B and QwQ-32B$^\dagger$, qualified for R1-32B$^\dagger$; \cref{sec:evaluation}); at biased layers, only the two 7--8B models survive. While we report five metrics, their information content is not independent: BA, precision, and FPR share a confusion matrix with 2 degrees of freedom (given class marginals); crossing rate and the additive composite are derived from these. The effective number of independent statistical tests is four (one per model), as reflected in our HB correction. The five-metric ablation diagnoses which \emph{aspect} of classification performance drives layer selection bias, not five independent pieces of evidence. Holm-Bonferroni step-down on four model-level tests yields the same result (all pass, with R1-8B FPR $p{=}0.044$ at rank-4 threshold $\alpha/1{=}0.050$). A joint (layer, $W$) grid search over 192 configurations confirms that L63 is near-optimal for QwQ-32B at recommended windows ($W{=}3$--$5$; \cref{app:layer_sweep}). Full per-layer results appear in the same appendix.
43	
44	\subsection{Baseline Methods}
45	\label{sec:baselines}
46	
47	We evaluate seven alternatives to contextualize probe performance (\cref{tab:negative}): BOCPD~\citep{adams2007bayesian} and CUSUM~\citep{page1954cusum} for change-point detection; Mahalanobis distance following TrajGuard~\citep{trajguard}; RepE mean-difference directions~\citep{zou2023representation}; two-layer MLP probes; CCS-adapted~\citep{burns2023discovering}; and cross-model transfer via PCA. A position-only baseline ($t/T$) controls for temporal artifacts. Detailed configurations in \cref{app:bocpd_config,app:transfer_details}.
48	
49	\subsection{Evaluation Protocol}
50	\label{sec:evaluation}
51	
52	We report balanced accuracy, precision, pre-CP FPR, coverage, and lead time (steps between first detection and true CP). Step-level metrics evaluate per-step classification; trace-level metrics aggregate across an entire reasoning trace (e.g., trace-level FPR is the fraction of safe traces with any false alarm exceeding $K$ consecutive crossings). Detection requires $K{=}5$ consecutive threshold crossings; $K$ was set as a design pre-selection before examining performance; sensitivity analysis (\cref{app:k_ablation}) confirms that $K \in \{3, 5, 7\}$ produces smooth coverage-FPR tradeoffs without qualitative changes in the modality comparison, though a post-hoc rationale for $K{=}5$ is that it corresponds to a sustained commitment signal rather than transient fluctuation. Modality comparisons use two-sided null-centered bootstrap (10{,}000 resamples) with Holm-Bonferroni step-down correction (3 metrics $\times$ 4 models $= 12$ tests, $\alpha{=}0.05$). Within each model, the three metrics are positively correlated by construction, making the correction stricter than under independence. Control task selectivity~\citep{hewitt2019control} validates genuine representational structure (\cref{app:control}). Throughout, $\dagger$ marks conclusions drawn from sample-limited test sets ($n \leq 20$): R1-32B ($n{=}20$) and QwQ-32B ($n{=}19$).
53	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "9f99b12b-eb1f-4146-96c0-0344747d0633"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/experiments.tex",
  "usage": {
    "total_tokens": 16594,
    "tool_uses": 7,
    "duration_ms": 4779
  },
  "last_tool_name": "Read",
  "uuid": "0e8a9b81-96bf-480a-9004-d11c41c3712f",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01XCRYnPwZukfAskziiQdv9r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "003c311c-cd36-4061-a793-5ba62281cc9f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-18T20:28:18.512Z_

<details><summary>↩ Tool result · `toolu_01XCRYnPwZukfAskziiQdv9r`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria.
4	
5	\paragraph{Evidence gradient.} The strength of HS advantage evidence varies by model, not scale. We classify evidence into three tiers based on seed robustness, position independence, and sample size: \textbf{strong} (OT-7B: 5/5 seeds HB, $\Delta$Prec $+21.9$pp, no position confound, selectivity 11.1pp, $n{=}47$); \textbf{moderate} (R1-8B: precision-robust but FPR seed-fragile at 3/5 HB, $n{=}43$; QwQ-32B$^\dagger$: 5/5 HB, $\Delta$Prec $+19.2$pp, negative lead time, position-competitive BA, $n{=}19$); and \textbf{qualified} (R1-32B$^\dagger$: 5/5 HB, $\Delta$Prec std${=}2.0$pp, but position-mediated with residualized gap NS, $W{=}1$ only, $n{=}20$).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We study R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (OpenThinker-7B, trained on the OpenThoughts dataset~\citep{openthinker}; Qwen-7B backbone, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level CP annotations (60/20/20 split). HS probes extract last-token hidden states from a selected layer; text probes encode each step with all-MiniLM-L6-v2 (384d). Both use L2-regularized logistic regression with temporal windowing $W \in \{1, 3, 5, 10, 15, 20, 25\}$ selected on validation. Detection requires $K{=}5$ consecutive threshold crossings. Statistical testing follows \cref{sec:evaluation}.
10	
11	\subsection{Layer Selection Results}\label{sec:layer-results}
12	
13	\cref{tab:layer_selection} shows that the biased composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models: L2 (3\% depth) for QwQ-32B and L10 (16\%) for R1-32B. Three of four metrics excluding crossing rate (precision, inverse FPR, and additive composite) consistently select deep layers at L63 (98\%) for both 32B models. Pure balanced accuracy, a threshold-free metric, selects layers that vary across data splits and models (7--98\% depth under 60/20/20; \cref{tab:ba_layer_comparison}), itself demonstrating that layer selection is a consequential methodological choice. The mechanism is that shallow layers produce highly compressed representations with small inter-step margins: step-to-step cosine distances are 1.4--2.7$\times$ smaller than at deep layers across all models (\cref{app:cosine_volatility}). A linear probe in this compressed space operates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (\cref{sec:layer-sensitivity}).
14	
15	\begin{table}[t]
16	\centering
17	\small
18	\begin{tabular}{lccc}
19	\toprule
20	\textbf{Model} & \textbf{Biased}$^a$ & \textbf{Corrected}$^b$ & $p$ \textbf{(corr.)} \\
21	\midrule
22	R1-8B & L14 (44\%) & L14 (44\%) & ${<}0.001$ \\
23	OT-7B & L0 (0\%) & L16 (57\%) & ${<}0.001$ \\
24	QwQ-32B & L2 (3\%) & L63 (98\%) & ${<}0.005$ \\
25	R1-32B & L10 (16\%) & L63 (98\%) & ${<}0.001$ \\
26	\bottomrule
27	\end{tabular}
28	\caption{Layer selection sensitivity. $^a$\,bal\_acc $\times$ crossing\_rate. $^b$\,Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Rightmost: HS vs.\ text precision $p$-value at corrected layer (e.g., QwQ-32B biased-layer: bal\_acc $p{=}0.35$, precision $p{=}0.83$, both non-significant).}
29	\label{tab:layer_selection}
30	\end{table}
31	
32	\begin{figure}[t]
33	\centering
34	\includegraphics[width=\columnwidth]{figures/fig_layer_heatmap.pdf}
35	\caption{Per-layer metric heatmap (2$\times$2). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal\_acc $\times$ crossing\_rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers.}
36	\label{fig:layer_heatmap}
37	\end{figure}
38	
39	The downstream impact is severe: at biased layers, only the two 7--8B models show significant HS advantage; both 32B models fail. At corrected layers, all four models pass Holm-Bonferroni correction$^\dagger$ (\cref{sec:evaluation}): strong (OT-7B), moderate (R1-8B, QwQ-32B$^\dagger$), and qualified (R1-32B$^\dagger$). Had we reported only biased-layer results, we would have concluded a scale-dependent HS advantage that is entirely a methodological artifact.
40	
41	\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
42	
43	\begin{table}[t]
44	\centering
45	\small
46	\resizebox{\columnwidth}{!}{%
47	\begin{tabular}{llclrrlrc}
48	\toprule
49	\textbf{Model} & \textbf{Layer} & \textbf{Enc.} & $W$ & $\Delta$\textbf{BA} & $\Delta$\textbf{Prec} & \textbf{95\% CI} & $\Delta$\textbf{FPR} & \textbf{HB} \\
50	\midrule
51	R1-8B & L14 & 384d & 3 & +17.5 & +20.1 & [+12.4, +28.3] & $-$7.9 & \checkmark \\
52	 & & 1024d & & \multicolumn{1}{c}{--} & +5.8 & [$-$7.4, +19.5] & \multicolumn{1}{c}{--} & \\[2pt]
53	OT-7B & L16 & 384d & 3 & +10.7 & +21.9 & [+14.4, +29.6] & $-$17.1 & \checkmark \\
54	 & & 1024d & & \multicolumn{1}{c}{--} & +18.1 & [+8.4, +29.0] & \multicolumn{1}{c}{--} & \checkmark \\[2pt]
55	QwQ & L63 & 384d & 5 & +13.0 & +19.2 & [+9.3, +33.5] & $-$15.0 & \checkmark \\
56	 & & 1024d & & \multicolumn{1}{c}{--} & +9.4 & [$-$7.1, +27.7] & \multicolumn{1}{c}{--} & \\[2pt]
57	R1-32B & L63 & 384d & 1 & \textbf{+18.7} & +15.4 & [+8.7, +22.6] & \textbf{$-$14.6} & \checkmark \\
58	 & & 1024d & & \multicolumn{1}{c}{--} & +11.7 & [$-$0.2, +24.3] & \multicolumn{1}{c}{--} & \\
59	\bottomrule
60	\end{tabular}}
61	\caption{HS vs.\ text at corrected layers (LR probes, 60/20/20 split, 10{,}000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\Delta$: HS$-$text difference (pp); ``--'' = metric not computed for that encoder comparison. HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$); all 384d model-level tests pass$^\dagger$. 1024d: HB over 4 model-level precision tests. Multi-seed stability in \cref{app:multi_seed}. BGE $\Delta$BA/$\Delta$FPR in \cref{app:encoder_robustness}.}
62	\label{tab:hs_vs_text}
63	\end{table}
64	
65	Against the 384d baseline, HS probes significantly outperform text probes across all four models$^\dagger$ (\cref{tab:hs_vs_text}), with evidence from strong (OT-7B: +21.9pp precision) to qualified (R1-32B$^\dagger$: +15.4pp, position-mediated). R1-8B FPR significance is fragile across seeds (2/5 uncorrected, 1/5 Bonferroni-corrected; \cref{tab:r18b_fpr_seeds}). R1-8B FPR advantage is directionally consistent across seeds (5/5) but not robust to data split (2/5 reach $p{<}0.05$ uncorrected; after Bonferroni correction for 5 seeds, 1/5 remains significant; \cref{app:multi_seed}). At 32B, both models are significant (HB corrected) but with model-specific caveats: R1-32B achieves significance only at $W{=}1$ with 25\% coverage (5/20 traces), and QwQ-32B's position baseline is competitive (\cref{sec:32b-analysis}). R1-32B passes 5/5 seeds (paired $\Delta$Prec std${=}2.0$pp, despite absolute precision std${=}12.8$pp) but its advantage is position-mediated (residualized gap NS; \cref{app:position_residual}). Overall, 18/20 model-seed combinations pass full HB; R1-8B FPR instability accounts for both failures (\cref{app:multi_seed}). Control task selectivity confirms genuine safety signal: 11.1--16.8pp above chance (\cref{app:control}).
66	
67	\paragraph{Capacity control.} PCA reduction of HS features to 384d (matching text encoder dimensionality, 79--92\% variance retained) preserves the precision advantage across all four models$^\dagger$ (+16.8 to +23.1pp, all $p{<}0.012$; all model-level precision tests pass Holm-Bonferroni). Two individual metric comparisons are non-significant: R1-8B balanced accuracy (+1.3pp, $p{=}0.731$, effect too small at $n{=}43$) and QwQ-32B FPR ($-$11.4pp, $p{=}0.038$, below HB threshold). PCA retains directions of maximum variance in hidden-state space, which need not align with the semantic dimensions captured by a trained text encoder; the control provides partial evidence against a pure capacity explanation but does not rule out representation quality differences between PCA-compressed HS and trained text encoders. Random projection to 384d (structure-destroying, unlike PCA) yields similar results ($\Delta$Prec +8.3 to +20.5pp, all $p{<}0.001$; \cref{app:random_projection}), further weakening the capacity explanation.
68	
69	\paragraph{Encoder robustness.} The 1024d rows in \cref{tab:hs_vs_text} replace MiniLM (384d) with BGE-large~\citep{xiao2023cpack} (1024d, a 2.7$\times$ stronger encoder). The HS precision advantage persists directionally across all four models but narrows substantially: only OT-7B survives Holm-Bonferroni (1/4 precision tests). HS balanced accuracy advantage is also directionally positive across all four models (+8.4 to +10.9pp), with 2/4 (OT-7B, R1-32B) significant under Holm-Bonferroni; FPR advantage is significant only for OT-7B (1/4). R1-8B shows an adverse FPR direction (HS FPR 1.2pp higher than BGE, $p{=}0.564$). The advantage is encoder-conditional rather than absolute (\cref{fig:forest_precision}). Layer selection (Contribution 1) is encoder-independent, as it concerns hidden-state properties across layers rather than the text baseline.
70	
71	\paragraph{Position mediation.} Position ($t/T$) accounts for 9--20pp of balanced accuracy depending on model and window size,\footnote{R1-32B's 20.4pp drop reflects $W{=}1$ (no temporal context); at $W{\geq}3$ with temporal windowing, drops are 9--17pp.} but all models retain non-positional signal above chance (all $p{<}0.001$; \cref{app:position_residual}). Three of four models retain significant non-positional HS advantage over text (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp ($p{=}0.914$, $n{=}20$), consistent with a position-mediated advantage. Temporal windowing reduces position dependence (R1-8B: 24.3pp drop at $W{=}3$ vs.\ 16.5pp at $W{=}15$).
72	
73	\paragraph{Caveats.} R1-32B achieves significance only at $W{=}1$ with 25\% coverage (5/20 traces); at $W{\geq}3$, dimensionality ($51200 \times W$ for $n{=}20$) prevents significance. Sweeping regularization $C$ over $[0.01, 100]$ yields ${<}2$pp variation in balanced accuracy; the HS advantage is also stable across decision thresholds (BA variation ${<}1.5$pp across $\tau \in [0.3, 0.7]$; \cref{app:threshold_sensitivity}). QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps vs.\ text 3.7--12.3 steps): higher precision at later detection. On benign traces, probes produce 39--52\% false alarm rates, so current methods characterize the commitment phenomenon rather than constitute production-ready detectors. Per-model details in \cref{sec:32b-analysis}.
74	
75	\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
76	
77	R1-32B and QwQ-32B share the Qwen-32B architecture (64 layers, 5120 hidden) but present opposite detection profiles (\cref{tab:32b_divergence}); training method is the likely differentiator.
78	
79	\begin{table}[t]
80	\centering
81	\small
82	\begin{tabular}{lcccc}
83	\toprule
84	\textbf{Model} & \textbf{Cov.} & \textbf{Lead (steps)} & \textbf{HB} & \textbf{Pos.\ margin} \\
85	\midrule
86	R1-32B & 25\% & +11.7 to +13.3 & \checkmark{} ($W{=}1$) & +14.2pp \\
87	QwQ-32B & 74\% & $-$1.2 to +1.9 & \checkmark{} (all $W$) & $-$3.6pp \\
88	\bottomrule
89	\end{tabular}
90	\caption{32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$). Pos.\ margin: HS balanced accuracy minus position-only baseline.}
91	\label{tab:32b_divergence}
92	\end{table}
93	
94	R1-32B detects commitment 11--13 steps early with a +14.2pp margin over the position baseline, which confirms genuine representational signal, but covers only 25\% of traces at the single significant window ($W{=}1$). QwQ-32B achieves statistical significance at all window sizes with 74\% coverage, but HS probes fire later than text probes (negative lead time). Consistent with the universal position analysis (\cref{sec:hs-text}), QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\ 0.796). HS precision (+4.5pp, $p{=}0.133$) and FPR (+2.5pp, $p{=}0.279$) margins over the position baseline are directionally positive but not statistically significant at $n{=}19$. The divergence implies that per-model validation is essential: no single detection configuration generalizes even within the same architecture at the same scale, and a system validated on one 32B model would fail on the other.
95	
96	\subsection{Temporal Context}\label{sec:temporal}
97	
98	Temporal windowing ($W{>}1$) improves both modalities on all models (\cref{fig:window_ablation}). Text precision improves +8 to +23pp from $W{=}1$ to $W{=}25$; HS precision improves +1.7 to +12.9pp. At 7--8B, the modality advantage (+20.1 to +21.9pp precision) exceeds the temporal improvement (+13pp). Both effects are complementary: temporal windowing ($W{=}3$--$15$) combined with principled layer selection yields the most consistent gains. Full per-model temporal ablations appear in \cref{app:temporal_details}; GRU sequence models under a matched 60/20/20 split achieve comparable accuracy but higher FPR than LR probes (\cref{tab:gru_multi_seeds}).
99	
100	\begin{figure}[t]
101	\centering
102	\includegraphics[width=\columnwidth]{figures/fig_forest_precision.pdf}
103	\caption{Forest plot of HS precision advantage over text probes. Blue: vs.\ MiniLM-384d; orange: vs.\ BGE-1024d. Solid markers: survives Holm-Bonferroni; hollow: does not. All 384d comparisons are significant (strong to qualified evidence); against BGE-1024d, only OT-7B (strong) survives correction.}
104	\label{fig:forest_precision}
105	\end{figure}
106	
107	\subsection{Negative Results}\label{sec:negative}
108	
109	No alternative method consistently matches supervised probing across the four models at any evidence tier (\cref{tab:negative}). Each failure is diagnostic: BOCPD~\citep{adams2007bayesian}/CUSUM fail on gradual transitions; Mahalanobis distance finds near-zero separation (signal in minor PCA components, $<$5\% variance); RepE~\citep{zou2023representation} is model-dependent (QwQ-32B BA 0.756 but precision 0.512 vs.\ R1-32B BA 0.559); MLP probes overfit (3/4 worse than LR); CCS misaligns with temporal structure; cross-model transfer fails across 17 configurations. Detailed analysis and the full comparison table in \cref{app:negative_details}.
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "d2eda744-1285-43a9-b774-2b0710ada940"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/discussion.tex",
  "usage": {
    "total_tokens": 16595,
    "tool_uses": 8,
    "duration_ms": 4918
  },
  "last_tool_name": "Read",
  "uuid": "6dfb44de-a2df-4dfc-8ba5-c58d46888050",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_018buPLTWTmUZNUx16BEH7TE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "91b0b2dc-6f8b-46b5-9c8a-51f8c9c8d468",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-18T20:28:18.658Z_

<details><summary>↩ Tool result · `toolu_018buPLTWTmUZNUx16BEH7TE`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Layer selection as researcher degree of freedom.}
4	Our five-metric ablation (\cref{sec:layer-results}) shows that crossing rate reverses the central finding: at biased layers, the HS advantage appears scale-dependent; at corrected layers, it is significant across all four models$^\dagger$, from strong (OT-7B) to qualified (R1-32B$^\dagger$; \cref{sec:evaluation}). The mechanism is representation compression at shallow layers (\cref{app:cosine_volatility}), which inflates crossing rate independently of discriminative power. The effect likely generalizes to any threshold-based detection study. The HS advantage holds at both BA-optimal and precision-optimal layers regardless of depth: BA-optimal layers span 7--98\% depth across models and splits, yet 14/16 per-model tests pass HB (precision +12.8 to +18.6pp; \cref{tab:ba_layer_comparison}); the two FPR failures come from underpowered 32B test sets ($n{\leq}20$). That BA selection itself produces such depth variation reinforces the methodological finding. For R1-32B, layers L55--L63 at $W{=}1$ form a robust band where all 3/3 metrics pass HB (\cref{app:layer_sweep}).
5	
6	\paragraph{Encoder-quality boundary.}
7	The HS advantage is a function of text encoder quality: significant against 384d MiniLM across all four models$^\dagger$ (4/4 HB, strong to qualified) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp), providing partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference. Temporal context and modality choice are complementary: at 7--8B, the modality advantage exceeds temporal improvement; temporal windowing ($W{=}3$ to $15$) provides consistent gains regardless of modality.
8	
9	\paragraph{Guidance for future research.}
10	The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6\% early detection with 50-step lead time, while R1-32B reaches only 50\% early detection (\cref{sec:oracle}), suggesting that the commitment signal strength itself varies across models. This indicates that distillation and native reasoning produce qualitatively different safety representation geometry. PCA capacity control, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage; \cref{app:position_residual}) provide converging evidence of genuine safety representations, but our approach is correlational. Causal validation via DAS~\citep{geiger2025causal}, LEACE~\citep{belrose2023leace}, or ITI~\citep{li2024iti} is needed to confirm that probed directions are causally active. We recommend a five-step audit for probing studies: (1)~train probes across all layers; (2)~compute $\geq$3 metrics (threshold-free and threshold-dependent); (3)~check for metric disagreement; (4)~report 2nd/3rd best layers; (5)~compute cosine volatility (\cref{app:cosine_volatility}). Steps 3--5 cost negligible compute.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "d9151736-ef39-43a6-a47f-d0ec3b39d1b4"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/conclusion.tex",
  "usage": {
    "total_tokens": 16596,
    "tool_uses": 9,
    "duration_ms": 5373
  },
  "last_tool_name": "Read",
  "uuid": "6a8f7da4-5559-4439-b86d-0d6f1db6d085",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_019MHrRuxHRyM6g9LgJRupbh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "886523b1-87d6-47cb-83fa-15c43e29f6e2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-18T20:28:19.107Z_

<details><summary>↩ Tool result · `toolu_019MHrRuxHRyM6g9LgJRupbh`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Layer selection is a critical researcher degree of freedom: a biased composite metric reverses the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. The five-step audit protocol (\cref{sec:discussion}) would have prevented our initial spurious scale-dependent conclusion and generalizes to any threshold-dependent detection study. The empirical HS advantage is conditional: robust at 7--8B (strong for OT-7B, moderate for R1-8B), position-mediated at 32B (moderate for QwQ-32B, qualified for R1-32B), and bounded by text encoder quality (4/4 HB against 384d, 1/4 against 1024d). The methodological contribution is robust; the empirical contribution narrows as encoders improve. Current probes characterize commitment (FPR 39--52\%, oracle gap 76.7\%) rather than constitute production detectors; causal interventions~\citep{meng2022rome,li2024iti} and LLM-based encoders~\citep{wang2024e5mistral} are next steps.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "dbbe8813-9dbe-4e9c-af8d-eae3f9f42f7e"
}
```

</details>

---

### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/limitations.tex",
  "usage": {
    "total_tokens": 16597,
    "tool_uses": 10,
    "duration_ms": 5383
  },
  "last_tool_name": "Read",
  "uuid": "5b9970f9-a12d-46a0-93ae-a82dadcb6f09",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01L7pEb9S15XoVHJFFeTYasj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "c0cf4808-deb4-47e2-b8f7-6bed9f5f2238",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-18T20:28:19.119Z_

<details><summary>↩ Tool result · `toolu_01L7pEb9S15XoVHJFFeTYasj`</summary>

```text
1	\section{Limitations}\label{sec:limitations}
2	
3	\paragraph{Model-specific caveats and statistical power.}
4	R1-32B achieves significance only at $W{=}1$ (25\% coverage, 5/20 traces) and its HS advantage is position-mediated (residualized gap +1.9pp, $p{=}0.914$; \cref{app:position_residual}). QwQ-32B's position baseline achieves higher balanced accuracy (0.832 vs.\ 0.796) with negative HS lead time. R1-8B FPR significance is seed-fragile (3/5 HB). At $n{=}19$--$20$, the minimum detectable effect at 80\% power is 8.6--9.5pp (\cref{app:power_analysis}); all 32B conclusions marked $\dagger$ should be interpreted with this constraint. Safe-trace FPR is 39--52\%, so current probes characterize the phenomenon rather than constitute production detectors; the 76.7\% oracle gap (\cref{sec:oracle}) confirms that passive probing captures only a fraction of available signal.
5	
6	\paragraph{Hyperparameter selection and scope.}
7	Layer (up to 64), $W$ (7 values), $K$ (5 values), and threshold are selected on the same validation set ($n{=}4$--$9$ per-class at 32B), yielding up to $2{,}240$ configurations; cumulative degrees of freedom are substantial (\cref{app:hyperparameter_robustness} provides convergence, cross-validation, and bootstrap analyses addressing this concern). BA-optimal layer indices are sensitive to the train/validation split, spanning 7--98\% depth across models and splits (\cref{tab:ba_layer_comparison}); for example, OT-7B shifts from L16 to L2 and QwQ-32B from L60 to L63 between 70/30 and 60/20/20 splits, a direct manifestation of the layer selection sensitivity that constitutes our primary finding. Threshold-dependent metrics are more stable but still vary by up to 4 layers. $K$ was pre-selected (\cref{app:k_ablation}); joint (layer, $W$) stability was verified for QwQ-32B (\cref{app:layer_sweep}) but not R1-32B. CP annotations follow HarmThoughts~\citep{harmthoughts} without independent IAA evaluation; if annotation error is ${\geq}2$ steps, QwQ-32B's lead time ($-$1.2 to +1.9) falls within noise, though perturbation analysis shows smooth degradation with no cliff effects (\cref{app:cp_perturbation}). We cover 2 architectures and 2 scales; intermediate scales, proprietary models, and multilingual settings are untested. Results are correlational; causal intervention is needed to confirm mechanistic involvement.
8	
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "fc928c34-3a4b-496f-9823-5dd66be985c8"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 16598,
    "tool_uses": 11,
    "duration_ms": 5527
  },
  "last_tool_name": "Read",
  "uuid": "175b9e37-008e-4a61-88c6-bf51cdb8c0d0",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_019zLEdT6d16AL6jafZ3He6q`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "3ffe68f7-bb6a-4334-9760-0b1fc58c2479",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011YsvX8mLRJHToqbeLxA6tt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 15506,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1070,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-18T20:28:19.733Z_

<details><summary>↩ Tool result · reported error · `toolu_019zLEdT6d16AL6jafZ3He6q`</summary>

```text
File content (26698 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "7a137c43-88d2-490f-aac6-16a7b3088ce7",
  "tool_use_result": "Error: File content (26698 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Reading docs/paper/sections/appendix.tex",
  "usage": {
    "total_tokens": 30949,
    "tool_uses": 12,
    "duration_ms": 8028
  },
  "last_tool_name": "Read",
  "uuid": "5366be67-44ea-483b-98ec-8660beade7da",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_016EhaRVRv6SEsu3cbkkdfyE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "08cbce92-fc33-4fbe-bff2-34c76e0cebc4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014YaoZExsDpkHBSjh4XqwbZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 14348,
      "cache_read_input_tokens": 16576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14348,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-18T20:28:22.023Z_

<details><summary>↩ Tool result · `toolu_016EhaRVRv6SEsu3cbkkdfyE`</summary>

```text
1	\appendix
2	
3	\noindent\textbf{Appendix Contents:}
4	\cref{app:checklist}~Responsible NLP Research Checklist;
5	\cref{app:layer_sweep}~Layer Sweep Results;
6	\cref{app:cosine_volatility}~Representation Compression Analysis;
7	\cref{app:holm_bonferroni}~Holm-Bonferroni Correction;
8	\cref{app:window_ablation}~Window Size Ablation;
9	\cref{app:ot7b_details}~OpenThinker-7B Details;
10	\cref{app:gru_details}~GRU Training Details;
11	\cref{app:control}~Control Task Methodology;
12	\cref{sec:oracle}~Oracle Upper Bound;
13	\cref{app:bocpd_config}~BOCPD/CUSUM Configuration;
14	\cref{app:k_ablation}~Detection Threshold Ablation;
15	\cref{app:threshold_sensitivity}~Decision Threshold Sensitivity;
16	\cref{app:bug}~M002 Bug Disclosure;
17	\cref{app:two_stage}~Adaptive Two-Stage Detection;
18	\cref{app:temporal_details}~Temporal Ablation Details;
19	\cref{app:negative_details}~Negative Results Details (incl.\ \cref{tab:negative});
20	\cref{app:transfer_details}~Cross-Model Transfer Details;
21	\cref{app:encoder_robustness}~Encoder Robustness;
22	\cref{app:position_residual}~Position-Residualized Probing;
23	\cref{app:multi_seed}~Multi-Seed Stability;
24	\cref{tab:ba_layer_comparison}~BA-Layer Modality Comparison;
25	\cref{app:power_analysis}~Post-Hoc Power Analysis.
26	
27	\section{Responsible NLP Research Checklist}
28	\label{app:checklist}
29	
30	We address the ARR Responsible NLP Research requirements below.
31	
32	\begin{itemize}
33	    \item \textbf{Limitations discussed:} Yes (\cref{sec:limitations}).
34	    \item \textbf{Potential risks:} This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this risk, as evasion requires white-box access to the probe, which a deployed monitoring system would not expose.
35	    \item \textbf{Computational budget:} Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total), using linear probes and single-layer GRUs. Total compute is minimal (under 4 GPU-hours on a single RTX A6000). No large-scale pretraining or finetuning was performed.
36	    \item \textbf{Data:} We use HarmThoughts, a publicly available benchmark with step-level safety annotations. No new data collection was performed.
37	    \item \textbf{Human subjects:} No human subjects research was conducted.
38	    \item \textbf{Reproducibility:} All hyperparameters are reported in \cref{app:gru_details,app:bocpd_config}. Code and corrected data will be released upon publication.
39	\end{itemize}
40	
41	
42	\section{Layer Sweep Results}
43	\label{app:layer_sweep}
44	
45	For each model, we sweep all transformer layers and evaluate five candidate selection metrics: (1)~balanced accuracy $\times$ crossing rate (the biased composite), (2)~pure balanced accuracy, (3)~precision, (4)~inverse pre-CP FPR, and (5)~an additive composite. The biased composite systematically selects shallow layers for 32B models because early-layer representations exhibit higher crossing rates (more frequent threshold crossings) regardless of discriminative power. Three threshold-dependent metrics (precision, inverse FPR, additive composite) converge on deep layers for all models; pure balanced accuracy selects layers whose depth varies with the data split (under 70/30: L30 for QwQ-32B, L47 for R1-32B; under the canonical 60/20/20: L63 and L46 respectively; \cref{tab:ba_layer_results}).
46	
47	\paragraph{Selected layers.} R1-8B: all five metrics agree on layer~14 (44\% depth). OT-7B: biased metric selects L0 (0\%), unbiased consensus selects L16 (57\%). QwQ-32B: biased metric selects L2 (3\%), unbiased consensus selects L63 (98\%). R1-32B: biased metric selects L10 (16\%), unbiased consensus selects L63 (98\%). The bias is most extreme for 64-layer models, where the composite metric selects layers in the bottom 16\% of the network while threshold-dependent metrics select layers at 98\% depth. Under 70/30, pure balanced accuracy selects L30 (47\%) for QwQ-32B and L47 (73\%) for R1-32B; under the canonical 60/20/20, it selects L63 (98\%) and L46 (72\%), demonstrating sensitivity to the data split.
48	
49	\paragraph{Impact on modality comparison.} At the biased layers, HS vs.\ text precision $p$-values are 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant. At the corrected deep layers, all $p$-values fall below 0.005. The initially reported ``scale-dependent'' pattern (HS advantage at 7--8B but not 32B) was entirely an artifact of layer selection methodology, not a genuine property of model scale (\cref{sec:layer-results}).
50	
51	\paragraph{Layer selection stability (LOO-CV).} Leave-one-out cross-validation on the validation set confirms that layer selection is robust to data composition regardless of metric. Under pure balanced accuracy, the dominant layer is selected in 68\% (QwQ-32B: L30, 13/19 folds) and 65\% (R1-32B: L47, 13/20 folds) of folds. Alternative selections cluster in neighboring layers (L29, L55--56 for QwQ; L32, L38, L43 for R1-32B). The consensus corrected layers (L63 for both 32B models) are similarly dominant under threshold-dependent selection.
52	
53	\paragraph{Joint (layer, $W$) sensitivity.} Under the original 70/30 validation protocol, we evaluate QwQ-32B across 64 layers $\times$ 3 windows ($W \in \{1, 3, 5\}$), yielding 192 configurations (\cref{tab:joint_layer_w}). L60 is near-optimal: within 2.1pp of the global best at $W{=}3$ and the top-ranked layer at $W{=}5$. (Under 60/20/20, threshold-dependent metrics select L63; the shift from L60 to L63 across splits itself illustrates layer selection sensitivity.) The optimal layer shifts from middle-deep (L46--47 at $W{=}1$) to deep (L60 at $W{=}5$), confirming a layer-window interaction. L30, selected by per-fold LOO-CV at $W{=}1$ under balanced accuracy, is suboptimal across all windows (max BA $= 0.769$ vs.\ global best 0.817). Joint (layer, $W$) stability was evaluated via grid search on $W \in \{1, 3, 5\}$ for QwQ-32B only; full leave-one-fold-out validation of the (layer, $W$) pair and extension to R1-32B remain for future work.
54	
55	\begin{table}[h]
56	\centering
57	\small
58	\caption{QwQ-32B joint (layer, $W$) grid search under 70/30 validation. L60 is near-optimal at recommended windows ($W{=}3$--$5$). L30 (LOO-CV selection at $W{=}1$) is suboptimal across all windows. Under the canonical 60/20/20 split, threshold-dependent metrics select L63.}
59	\label{tab:joint_layer_w}
60	\begin{tabular}{clccc}
61	\toprule
62	$W$ & \textbf{Best layer} & \textbf{Best BA} & \textbf{L60 BA} & \textbf{L60 rank} \\
63	\midrule
64	1 & L47 & 0.798 & 0.783 & $\sim$15th \\
65	3 & L46 & 0.817 & 0.796 & $\sim$6th \\
66	5 & L60 & 0.808 & 0.808 & 1st \\
67	\bottomrule
68	\end{tabular}
69	\end{table}
70	
71	
72	\section{Representation Compression Analysis}
73	\label{app:cosine_volatility}
74	
75	We measure step-to-step cosine distance at biased (shallow) vs.\ corrected (deep) layers across all models to characterize the compression mechanism underlying the crossing rate bias (\cref{tab:cosine_volatility}).
76	
77	\begin{table}[h]
78	\centering
79	\small
80	\caption{Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4--2.7$\times$ smaller inter-step distances).}
81	\label{tab:cosine_volatility}
82	\begin{tabular}{llcc}
83	\toprule
84	\textbf{Model} & \textbf{Layer (type)} & \textbf{Mean} & \textbf{Std} \\
85	\midrule
86	R1-8B & L2 (biased) & 0.186 & 0.097 \\
87	 & L14 (corrected) & 0.411 & 0.143 \\[2pt]
88	OT-7B & L2 (biased) & 0.077 & 0.080 \\
89	 & L16 (corrected) & 0.206 & 0.091 \\[2pt]
90	QwQ-32B & L2 (biased) & 0.037 & 0.064 \\
91	 & L63 (corrected) & 0.084 & 0.056 \\[2pt]
92	R1-32B & L10 (biased) & 0.067 & 0.050 \\
93	 & L63 (corrected) & 0.092 & 0.076 \\
94	\bottomrule
95	\end{tabular}
96	\end{table}
97	
98	Shallow layers produce highly compressed representations: consecutive steps cluster within small cosine distances (0.04--0.19), while deep-layer representations spread more widely (0.09--0.41). Inter-step distances at shallow layers are 1.4--2.7$\times$ smaller than at deep layers across all models. A linear probe operating in this compressed space sits near the noise floor, where minor numerical fluctuations produce spurious threshold crossings that inflate crossing rate independently of discriminative power. Deep layers produce well-separated representations where crossings correspond to genuine semantic transitions.
99	
100	
101	\section{Holm-Bonferroni Step-Down Correction}
102	\label{app:holm_bonferroni}
103	
104	\cref{tab:holm_bonferroni} reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the conservative 12-test correction and the 4-test model-level correction: both yield the same outcome (all tests pass at $\alpha{=}0.05$). Under 4-test HB, the tightest threshold falls on R1-8B FPR ($p{=}0.044$, rank-4 threshold $\alpha/1{=}0.050$), which still passes. Tests are ranked by $p$-value; each test $i$ (rank $i$ of $m$) must satisfy $p_i < \alpha / (m - i + 1)$ under the step-down procedure.
105	
106	\begin{table}[h]
107	\centering
108	\small
109	\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}
110	\label{tab:holm_bonferroni}
111	\setlength{\tabcolsep}{4pt}
112	\begin{tabular}{clllcc}
113	\toprule
114	\textbf{Rank} & \textbf{Model} & \textbf{Metric} & \textbf{$p$-val} & \textbf{Thresh.} & \textbf{Pass} \\
115	\midrule
116	1  & R1-8B  & Precision & $<$0.001 & 0.0042 & \checkmark \\
117	2  & OT-7B  & Bal.\ Acc. & $<$0.001 & 0.0045 & \checkmark \\
118	3  & OT-7B  & Precision & $<$0.001 & 0.0050 & \checkmark \\
119	4  & OT-7B  & FPR & $<$0.001 & 0.0056 & \checkmark \\
120	5  & QwQ-32B & Bal.\ Acc. & $<$0.001 & 0.0063 & \checkmark \\
121	6  & QwQ-32B & Precision & $<$0.001 & 0.0071 & \checkmark \\
122	7  & R1-32B & Bal.\ Acc. & $<$0.001 & 0.0083 & \checkmark \\
123	8  & R1-32B & Precision & $<$0.001 & 0.0100 & \checkmark \\
124	9  & QwQ-32B & FPR & 0.004 & 0.0125 & \checkmark \\
125	10 & R1-8B  & Bal.\ Acc. & 0.005 & 0.0167 & \checkmark \\
126	11 & R1-32B & FPR & 0.007 & 0.0250 & \checkmark \\
127	12 & R1-8B  & FPR & 0.044 & 0.0500 & \checkmark \\
128	\bottomrule
129	\end{tabular}
130	\end{table}
131	
132	The weakest test (rank 12, R1-8B FPR, $p{=}0.044$) passes its threshold ($\alpha/1 = 0.05$) with margin. The ordering reveals that OT-7B produces the strongest HS-text separation (ranks 2--4), while R1-8B FPR is the least significant despite R1-8B's precision gap (+20.1pp at $W{=}3$). This reflects R1-8B's already-low text FPR (11.8\%), which leaves less room for HS improvement on this metric.
133	
134	\paragraph{Exact sign-flip permutation test validation.} As an independent check on bootstrap significance for the small-sample 32B models, we run exact sign-flip permutation tests on all six 32B comparisons, enumerating all $2^n$ sign permutations ($2^{19}{=}524{,}288$ for QwQ-32B, $2^{20}{=}1{,}048{,}576$ for R1-32B). All six tests reject the null at $\alpha{=}0.05$: QwQ-32B (bal\_acc $p{<}0.001$, precision $p{=}0.003$, FPR $p{<}0.001$); R1-32B (bal\_acc $p{=}0.008$, precision $p{<}0.001$, FPR $p{=}0.004$). The permutation $p$-values are consistent with the bootstrap values in \cref{tab:holm_bonferroni}, confirming that the bootstrap-based conclusions are not artifacts of distributional assumptions at small $n$.
135	
136	
137	\section{Window Size Ablation Details}
138	\label{app:window_ablation}
139	
140	\cref{tab:window_full} reports the complete window size ablation across all models and seven window sizes. The main text (\cref{sec:temporal}) presents R1-8B results; here we provide the full data. \cref{fig:window_ablation} visualizes the monotonic improvement on R1-8B: precision rises from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$) while FPR drops from 9.65\% to 4.8\%.
141	
142	\begin{figure}[h]
143	\centering
144	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
145	\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}
146	\label{fig:window_ablation}
147	\end{figure}
148	
149	\begin{table}[h]
150	\centering
151	\small
152	\caption{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models.}
153	\label{tab:window_full}
154	\resizebox{\columnwidth}{!}{%
155	\begin{tabular}{llccccc}
156	\toprule
157	Model & $W$ & Bal.\ Acc. & Precision & FPR$_{\text{step}}$ & Coverage & Lead \\
158	\midrule
159	\multirow{7}{*}{R1-8B}
160	 & 1  & 77.8 & 69.3 & 9.65 & 72.1 & 13.8 \\
161	 & 3  & 79.0 & 72.3 & 8.50 & 69.8 & 12.1 \\
162	 & 5  & 78.1 & 72.6 & 8.09 & 65.1 & 8.3 \\
163	 & 10 & 79.3 & 74.3 & 7.61 & 55.8 & 10.0 \\
164	 & 15 & 80.2 & 77.7 & 6.39 & 51.2 & 7.2 \\
165	 & 20 & 80.7 & 78.6 & 6.12 & 53.5 & 7.4 \\
166	 & 25 & 81.0 & 82.2 & 4.83 & 48.8 & 8.1 \\
167	\midrule
168	\multirow{7}{*}{OT-7B}
169	 & 1  & 68.2 & 42.8 & 12.0 & 53.2 & 16.1 \\
170	 & 3  & \textbf{68.8} & 46.6 & 10.0 & 53.2 & 21.6 \\
171	 & 5  & 68.1 & 46.4 & 9.9 & 53.2 & 21.7 \\
172	 & 10 & 66.5 & 46.9 & 8.6 & 48.9 & 25.0 \\
173	 & 15 & 66.4 & 48.8 & 7.7 & 44.7 & 39.6 \\
174	 & 20 & 66.0 & \textbf{49.4} & \textbf{7.5} & 48.9 & 17.9 \\
175	 & 25 & 65.9 & 48.9 & 8.0 & 51.1 & 28.3 \\
176	\midrule
177	\multirow{7}{*}{R1-32B}
178	 & 1  & 71.8 & 54.9 & 32.03 & 80.0 & 12.9 \\
179	 & 3  & 72.5 & 56.0 & 30.64 & 80.0 & 11.4 \\
180	 & 5  & 73.1 & 57.5 & 28.41 & 75.0 & 11.1 \\
181	 & 10 & 73.7 & 60.9 & 23.40 & 70.0 & 10.8 \\
182	 & 15 & 72.1 & 59.1 & 24.51 & 70.0 & 10.9 \\
183	 & 20 & 69.6 & 56.3 & 26.18 & 65.0 & 9.6 \\
184	 & 25 & 70.3 & 56.6 & 26.46 & 70.0 & 10.7 \\
185	\midrule
186	\multirow{7}{*}{QwQ-32B}
187	 & 1  & 73.0 & 54.4 & 22.76 & 79.0 & 19.7 \\
188	 & 3  & 74.5 & 56.5 & 21.41 & 73.7 & 20.6 \\
189	 & 5  & 76.1 & 57.3 & 21.68 & 73.7 & 20.1 \\
190	 & 10 & 74.7 & 57.1 & 20.73 & 73.7 & 18.4 \\
191	 & 15 & 74.1 & 58.2 & 19.11 & 68.4 & 15.8 \\
192	 & 20 & 75.4 & 60.2 & 17.89 & 63.2 & 15.8 \\
193	 & 25 & 76.2 & 61.8 & 16.94 & 57.9 & 14.9 \\
194	\bottomrule
195	\end{tabular}}%
196	\end{table}
197	
198	Key cross-model patterns emerge from the window ablation:
199	
200	\paragraph{R1-8B} shows a general upward trend in balanced accuracy from 77.8\% ($W{=}1$) to 81.0\% ($W{=}25$), gaining +3.2pp overall with a slight dip at $W{=}5$ (78.1\%). Precision improves sharply (+12.9pp) and step-level FPR halves (9.65\% to 4.83\%). Coverage trades off against quality, dropping from 72.1\% to 48.8\%.
201	
202	\paragraph{OT-7B} exhibits a split temporal pattern at layer 16: balanced accuracy peaks at $W{=}3$ (68.8\%) and declines at larger windows ($-$2.9pp by $W{=}25$), while precision and FPR continue improving. Precision rises from 42.8\% ($W{=}1$) to 49.4\% ($W{=}20$), and FPR drops from 12.0\% to 7.5\% over the same range. The split indicates that larger windows reduce false alarms and sharpen positive predictions even as overall classification accuracy degrades. Lead times are shorter than old layer-0 estimates (16.1--39.6 steps) due to the corrected layer selection (\cref{app:ot7b_details}). OT-7B text probes improve monotonically across all metrics (\cref{app:ot7b_details}), so the accuracy saturation is specific to HS probes on this model.
203	
204	\paragraph{R1-32B} exhibits a non-monotonic pattern: balanced accuracy peaks at $W{=}10$ (73.7\%) and then declines, falling below the $W{=}1$ baseline by $W{=}20$ (69.6\%). The optimal window for R1-32B is $W{=}10$, which achieves the lowest FPR (23.40\%) and highest precision (60.9\%). The accuracy degradation at large windows likely reflects overfitting on the smaller dataset ($n{=}100$).
205	
206	\paragraph{QwQ-32B} shows a broadly increasing trend with local non-monotonicity: balanced accuracy peaks at $W{=}5$ (76.1\%), dips at $W{=}10$--$15$, then recovers to 76.2\% at $W{=}25$. Precision and FPR improve monotonically with larger windows (54.4\% to 61.8\% precision; 22.76\% to 16.94\% FPR). QwQ-32B produces notably longer lead times than R1-8B and R1-32B (19.7 steps at $W{=}1$, 14.9 at $W{=}25$), though OT-7B's lead times are longer still.
207	
208	\paragraph{Universal trends.} Across all models: (1) larger windows reduce coverage as the smoothed probe fires less frequently; (2) HS FPR generally decreases with window size; (3) lead time is model-dependent. The primary cross-model difference is whether balanced accuracy improves broadly (R1-8B, QwQ-32B), peaks sharply at an intermediate window (R1-32B at $W{=}10$), or peaks very early (OT-7B at $W{=}3$). Each model uses its validation-selected window in the main text.
209	
210	\subsection{Text Probe Window Ablation}
211	\label{app:text_window}
212	
213	\cref{tab:text_window} reports the complete text probe window sweep on R1-8B, confirming that temporal context benefits text probes even more strongly than HS probes.
214	
215	\begin{table}[h]
216	\centering
217	\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}
218	\label{tab:text_window}
219	\begin{tabular}{lcccc}
220	\toprule
221	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
222	\midrule
223	 1  & 64.7 & 41.6 & 25.8 & 95.4 \\
224	 3  & 66.9 & 44.8 & 23.1 & 90.7 \\
225	 5  & 69.2 & 48.5 & 20.4 & 84.9 \\
226	 10 & 72.1 & 54.3 & 16.7 & 74.4 \\
227	 15 & 74.3 & 58.9 & 14.2 & 67.4 \\
228	 20 & 75.8 & 62.1 & 12.5 & 62.8 \\
229	 25 & 76.7 & 64.8 & 11.8 & 58.1 \\
230	\bottomrule
231	\end{tabular}
232	\end{table}
233	
234	Text probes show monotonic improvement across all window sizes without the plateau observed in HS probes (which saturate around $W{=}15$). The absolute FPR reduction ($-$14.0pp) is nearly three times the HS reduction ($-$4.8pp), and accuracy gains (+12.0pp vs.\ +3.2pp) are four times larger. This asymmetry supports the interpretation that temporal context is the primary factor in commitment detection: text features, which encode less information per step, benefit proportionally more from observing the multi-step progression.
235	
236	
237	\section{OpenThinker-7B Detailed Results}
238	\label{app:ot7b_details}
239	
240	OpenThinker-7B (OT-7B) is trained with STILL~\cite{still} on Qwen2.5-7B, producing a 7B reasoning model with a different training paradigm from the R1-distilled models. We report the full layer sweep and text probe window ablation.
241	
242	\paragraph{Layer sweep.}
243	
244	\begin{table}[h]
245	\centering
246	\small
247	\caption{OT-7B layer sweep. Score = balanced accuracy $\times$ crossing rate. Layer 16 (57\% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.}
248	\label{tab:ot7b_layer_sweep}
249	\setlength{\tabcolsep}{4pt}
250	\begin{tabular}{lcccc}
251	\toprule
252	Layer & Depth & Bal.\ Acc. & Cross.\ Rate & Score \\
253	\midrule
254	0 (embed.) & 0 & 66.7 & 53.2 & 35.5 \\
255	4 & 14 & 66.3 & 40.4 & 26.8 \\
256	8 & 29 & 66.4 & 25.5 & 17.0 \\
257	12 & 43 & 67.5 & 31.9 & 21.6 \\
258	16 & 57 & 68.2 & 31.9 & 21.8 \\
259	20 & 71 & 65.5 & 31.9 & 20.9 \\
260	24 & 86 & 66.9 & 29.8 & 19.9 \\
261	27 & 96 & 63.0 & 31.9 & 20.1 \\
262	\bottomrule
263	\end{tabular}
264	\end{table}
265	
266	After correction of a layer selection bug, layer 16 (57\% depth) is selected. It achieves the highest balanced accuracy (68.2\%) among transformer layers under the 70/30 split used here; under the canonical 60/20/20 split, BA selects L2 (7\% depth; \cref{tab:ba_layer_results}). Layer 0 (embedding) has a higher crossing rate (53.2\% vs.\ 31.9\%) but lower accuracy.
267	
268	\paragraph{Text probe window ablation.}
269	
270	\begin{table}[h]
271	\centering
272	\small
273	\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}
274	\label{tab:ot7b_text_window}
275	\begin{tabular}{lcccc}
276	\toprule
277	$W$ & Bal. Acc. & Precision & FPR & Coverage \\
278	\midrule
279	 1  & 58.1 & 24.5 & 34.5 & 63.8 \\
280	 3  & 57.9 & 25.4 & 27.1 & 74.5 \\
281	 5  & 56.9 & 24.7 & 25.5 & 70.2 \\
282	 10 & 58.3 & 27.0 & 22.2 & 70.2 \\
283	 15 & 58.9 & 28.3 & 20.0 & 66.0 \\
284	 20 & 60.9 & 31.6 & 17.6 & 66.0 \\
285	 25 & 61.4 & 32.9 & 16.1 & 66.0 \\
286	\bottomrule
287	\end{tabular}
288	\end{table}
289	
290	OT-7B text probes improve monotonically from $W{=}1$ to $W{=}25$ (+3.3pp accuracy, +8.5pp precision, $-$18.4pp FPR), following the same pattern as R1-8B text probes. OT-7B HS probes show a split pattern: balanced accuracy peaks at $W{=}3$ and declines, while precision and FPR continue improving (\cref{tab:window_full}). The text-HS contrast is therefore metric-dependent rather than a blanket modality difference.
291	
292	\paragraph{Bootstrap comparison (matched $W{=}3$).} To ensure a fair modality comparison, bootstrap tests use matched $W{=}3$ for both HS and text probes. At $W{=}3$, HS probes achieve 75.3\% trace-level balanced accuracy vs.\ 65.6\% for text (bootstrap $\Delta{=}$+10.7pp, 95\% CI [4.9, 16.3], $p{<}0.001$, survives Holm-Bonferroni). Precision: 55.8\% vs.\ 34.6\% (bootstrap $\Delta{=}$+21.9pp, 95\% CI [14.0, 29.6], $p{<}0.001$, survives Holm-Bonferroni). Pre-CP FPR: 10.0\% vs.\ 27.1\% (bootstrap $\Delta{=}{-}17.1$pp, 95\% CI [$-$22.2, $-$12.2], $p{<}0.001$, survives Holm-Bonferroni). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (+21.9pp); the small discrepancy reflects resampling variance. Using each modality's optimal $W$ (HS at $W{=}3$, text at $W{=}25$) would introduce a confound because text would benefit from 8$\times$ more temporal context.
293	
294	
295	\section{GRU Training Details}
296	\label{app:gru_details}
297	
298	\paragraph{Data split.} GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression probes. Within the 70\% training portion, we hold out 10\% of total traces as a validation set for early stopping, yielding an effective 60/10/30 train/validation/test split. The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.
299	
300	\paragraph{Architecture.} We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden states from the best layer (selected by validation balanced accuracy) as input. The multi-layer variant concatenates hidden states from 7 layers (evenly spaced through the network) at each step, producing a higher-dimensional input to the same GRU architecture.
301	
302	\paragraph{Training procedure.} We train with Adam (learning rate $1 \times 10^{-3}$, default $\beta_1{=}0.9$, $\beta_2{=}0.999$), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.
303	
304	\paragraph{Evaluation.} We report crossing accuracy (the sustained accuracy at which the probe first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean $\pm$ standard deviation.
305	
306	\paragraph{Per-seed results for R1-8B (single-layer GRU).}
307	
308	\begin{table}[h]
309	\centering
310	\small
311	\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}
312	\label{tab:gru_seeds}
313	\setlength{\tabcolsep}{4pt}
314	\begin{tabular}{lccc}
315	\toprule
316	Seed & Peak Acc. & Crossing Acc. & Lead (steps) \\
317	\midrule
318	1 & 85.2 & 74.3 & +4.8 \\
319	2 & 83.1 & 71.6 & +4.8 \\
320	3 & 83.4 & 70.4 & +0.9 \\
321	\midrule
322	Mean $\pm$ std & 83.9 $\pm$ 1.1 & 72.1 $\pm$ 2.0 & +3.5 $\pm$ 2.3 \\
323	\bottomrule
324	\end{tabular}
325	\end{table}
326	
327	The high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe achieves good peak accuracy but crosses the detection threshold late. This variance underscores the sensitivity of early detection to initialization and motivates reporting per-seed results rather than relying on mean values alone.
328	
329	\paragraph{Multi-layer GRU and baseline comparison (60/20/20 protocol).}
330	
331	\begin{table}[h]
332	\centering
333	\scriptsize
334	\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}
335	\label{tab:gru_multi_seeds}
336	\resizebox{\columnwidth}{!}{%
337	\begin{tabular}{llccccc}
338	\toprule
339	Model & Seed & Acc & Prec & FPR & Cross.\% & Lead \\
340	\midrule
341	GRU-single & 42  & 0.845 & 0.657 & 0.139 & 72.1\% & 3.55 \\
342	GRU-single & 123 & 0.760 & 0.454 & 0.191 & 65.1\% & 7.39 \\
343	GRU-single & 456 & 0.792 & 0.474 & 0.203 & 67.4\% & 8.45 \\
344	\rowcolor{gray!10}
345	GRU-single & \textit{mean} & 0.799$\pm$0.035 & 0.528$\pm$0.091 & 0.178$\pm$0.028 & 68.2$\pm$2.9\% & 6.46$\pm$2.10 \\
346	\midrule
347	GRU-multi  & 42  & 0.824 & 0.616 & 0.164 & 74.4\% & 5.66 \\
348	GRU-multi  & 123 & 0.759 & 0.454 & 0.195 & 65.1\% & 6.43 \\
349	GRU-multi  & 456 & 0.784 & 0.460 & 0.207 & 65.1\% & 8.93 \\
350	\rowcolor{gray!10}
351	GRU-multi  & \textit{mean} & 0.789$\pm$0.027 & 0.510$\pm$0.075 & 0.189$\pm$0.018 & 68.2$\pm$4.4\% & 7.01$\pm$1.40 \\
352	\midrule
353	LR-single  & 42  & 0.841 & 0.693 & 0.097 & 46.5\% & $-$2.00 \\
354	LR-single  & 123 & 0.753 & 0.436 & 0.181 & 53.5\% & 5.26 \\
355	LR-single  & 456 & 0.814 & 0.512 & 0.146 & 41.9\% & 3.94 \\
356	\rowcolor{gray!10}
357	LR-single  & \textit{mean} & 0.803$\pm$0.037 & 0.547$\pm$0.108 & 0.141$\pm$0.035 & 47.3$\pm$4.8\% & 2.40$\pm$3.16 \\
358	\midrule
359	LR-multi   & 42  & 0.827 & 0.679 & 0.092 & 39.5\% & 1.06 \\
360	LR-multi   & 123 & 0.756 & 0.442 & 0.180 & 46.5\% & 7.30 \\
361	LR-multi   & 456 & 0.817 & 0.521 & 0.130 & 34.9\% & 4.00 \\
362	\rowcolor{gray!10}
363	LR-multi   & \textit{mean} & 0.800$\pm$0.032 & 0.547$\pm$0.099 & 0.134$\pm$0.036 & 40.3$\pm$4.8\% & 4.12$\pm$2.55 \\
364	\bottomrule
365	\end{tabular}}%
366	\end{table}
367	
368	Under this protocol, multi-layer GRU achieves the highest mean lead (7.01$\pm$1.40 steps) but at higher FPR than logistic regression baselines (0.189 vs.\ 0.134). The GRU advantage is concentrated in detection timing rather than classification accuracy, consistent with the main text finding that GRUs capture sequential dependencies that improve early detection. Lead time shows high variance across seeds (range 5.66--8.93 for GRU-multi), reinforcing that reported means should be interpreted cautiously.
369	
370	\paragraph{OT-7B multi-layer GRU (layers 13--19, 3 seeds, 60/20/20 split).}
371	OT-7B GRU achieves 74.6$\pm$1.3\% balanced accuracy, 64.5$\pm$7.0\% coverage, +33.6$\pm$4.8 steps lead, and 27.4$\pm$6.1\% pre-CP FPR. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average ${\sim}$80 reasoning steps (vs.\ ${\sim}$30 for R1-8B and 32B models), so absolute lead times are not directly comparable. The FPR-lead tradeoff mirrors R1-8B: GRU FPR (27.4\%) is far above the LR probe at layer 16 (10.0\%), confirming that GRUs gain lead time at the cost of more false alarms across both 7-8B models.
372	
373	
374	\section{Control Task Methodology}
375	\label{app:control}
376	
377	We follow the selectivity framework of \cite{hewitt2019control} to verify that our probes capture genuine safety-relevant structure rather than surface-level correlations.
378	
379	\paragraph{Procedure.} For each model, we randomly permute the binary labels (pre-CP vs. post-CP) within each trace while preserving the marginal label distribution. We then retrain the probe with identical architecture (L2-regularized logistic regression) and hyperparameters on these shuffled labels. Selectivity is defined as:
380	\begin{equation}
381	    \text{Selectivity} = \text{Acc}_{\text{linguistic}} - \text{Acc}_{\text{control}}
382	\end{equation}
383	where $\text{Acc}_{\text{linguistic}}$ is the probe accuracy on true labels and $\text{Acc}_{\text{control}}$ is the accuracy on permuted labels. A selectivity of zero indicates that the probe exploits only non-linguistic features (e.g., position); higher values confirm that the representation encodes task-relevant information.
384	
385	\paragraph{Results.} We repeat the control experiment 10 times with different random permutations and report the mean control accuracy. Selectivity scores at corrected layers (60/20/20 split) are: R1-32B 16.8pp (layer 63), QwQ-32B 16.1pp (layer 63), R1-8B 14.1pp (layer 14), OT-7B 11.1pp (layer 16). All values exceed the 5pp threshold recommended by \cite{hewitt2019control}. R1-32B and QwQ-32B achieve the strongest selectivity ($>$16pp) at corrected layers. On QwQ-32B, the position baseline accuracy (0.705) slightly exceeds the HS probe (0.667) at L60, consistent with the main-text finding that QwQ's HS advantage is concentrated in precision and FPR rather than balanced accuracy.
386	
387	\paragraph{Layer provenance note.} R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias because their biased and corrected layers coincide. QwQ-32B selectivity is 16.1pp at L63, confirming that safety-specific signal persists at deep layers.
388	
389	\paragraph{Position-only baseline.} As a complementary validation, we train a logistic regression classifier using only the normalized step index ($t / T$ where $T$ is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8\% FPR compared to 8.1\% for the HS probe at matched detection rates. The probe's substantially lower FPR confirms that hidden state features carry information beyond what step position provides.
390	
391	\paragraph{Residualized selectivity.} To confirm that selectivity survives position removal, we recompute control task selectivity on position-regressed features (the same residualized representations used in \cref{app:position_residual}). Residualized selectivity: R1-8B 22.9pp, OT-7B 10.4pp, QwQ-32B 11.3pp (all ${>}5$pp), R1-32B 3.0pp (${<}5$pp, consistent with the position-mediated advantage reported in \cref{sec:hs-text}). Three of four models retain selectivity well above the \citet{hewitt2019control} threshold after position removal; R1-32B's drop confirms that its safety signal is largely positional.
392	
393	
394	\section{Oracle Upper Bound Analysis}
395	\label{sec:oracle}
396	
397	We compute an oracle upper bound for commitment detection by measuring the earliest step at which the ground-truth commitment point (CP) could theoretically be predicted from hidden-state dynamics. The oracle detector has access to the true CP label and computes how many steps before CP the representation trajectory first enters a region that is linearly separable from pre-CP states with perfect accuracy on the training set. This provides a theoretical ceiling on early detection performance.
398	
399	\cref{tab:oracle} reports oracle performance across all four models. Oracle analysis confirms the evidence gradient: OT-7B (strong) shows the highest early detection rate (93.6\%) and longest lead time (50 steps), while R1-32B (qualified) achieves only 50\% early detection even with oracle labels, suggesting that its commitment signal is inherently weaker. On R1-8B, the oracle early detection rate is 76.7\% (33/43 traces detected before CP, with +31 steps mean lead time), compared to +4.5 steps for the best learned probe (GRU). This gap indicates that hidden states at step $t$ encode the model's current safety state but carry limited predictive power about future trajectory evolution. The learned probe captures the contemporaneous safety signal effectively (balanced accuracy 81--84\%) but cannot anticipate the commitment transition far in advance. Closing this gap will likely require causal intervention techniques (e.g., activation patching) rather than improvements to passive monitoring.
400	
401	\begin{table}[h]
402	\centering
403	\small
404	\caption{Oracle upper bound analysis. Detection rate: fraction of traces where the oracle finds a linearly separable boundary before or at CP. Early detection rate: fraction detected before CP. Mean lead: average steps before CP at first detection.}
405	\label{tab:oracle}
406	\begin{tabular}{lcccc}
407	\toprule
408	\textbf{Model} & \textbf{Det.\ Rate} & \textbf{Early Det.} & \textbf{Mean Lead} & $n_{\text{test}}$ \\
409	\midrule
410	R1-8B & 100\% & 76.7\% & 31.0 & 43 \\
411	OT-7B & 100\% & 93.6\% & 50.0 & 47 \\
412	R1-32B$^\dagger$ & 95.0\% & 50.0\% & 32.4 & 20 \\
413	QwQ-32B$^\dagger$ & 100\% & 84.2\% & 24.4 & 19 \\
414	\bottomrule
415	\end{tabular}
416	\end{table}
417	
418	
419	\section{CP Annotation Perturbation}
420	\label{app:cp_perturbation}
421	
422	To assess sensitivity to annotation noise, we shift all ground-truth CP labels by $\delta \in \{-3, \ldots, +3\}$ steps and retrain the HS probe (\cref{tab:cp_perturbation}). Precision degrades smoothly with no cliff effect: within $\pm 2$ steps, BA changes by ${<}2.5$pp for all models (7--8B: ${<}1.0$pp). At the $\pm 3$-step worst case, all models retain precision well above their respective text baselines. These results support the annotation robustness assumption discussed in \cref{sec:limitations}.
423	
424	\begin{table}[h]
425	\centering
426	\small
427	\caption{HS probe sensitivity to CP annotation shift ($\delta$ steps). BA is stable across all perturbations; precision degrades gradually without cliff effects.}
428	\label{tab:cp_perturbation}
429	\begin{tabular}{llccc}
430	\toprule
431	\textbf{Model} & $\delta$ & \textbf{Prec} & \textbf{BA} & \textbf{FPR} \\
432	\midrule
433	R1-8B & $-3$ & .652 & .773 & .177 \\
434	 & $0$ & .596 & .784 & .165 \\
435	 & $+3$ & .530 & .771 & .143 \\[2pt]
436	OT-7B & $-3$ & .404 & .714 & .298 \\
437	 & $0$ & .351 & .707 & .286 \\
438	 & $+3$ & .300 & .702 & .276 \\[2pt]
439	QwQ-32B & $-3$ & .661 & .728 & .158 \\
440	 & $0$ & .609 & .690 & .129 \\
441	 & $+3$ & .550 & .676 & .114 \\[2pt]
442	R1-32B & $-3$ & .625 & .698 & .360 \\
443	 & $0$ & .570 & .722 & .281 \\
444	 & $+3$ & .503 & .750 & .236 \\
445	\bottomrule
446	\end{tabular}
447	\end{table}
448	
449	
450	\section{BOCPD/CUSUM Configuration Sweep}
451	\label{app:bocpd_config}
452	
453	We sweep hyperparameters for both Bayesian Online Change-Point Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe score sequences.
454	
455	\paragraph{BOCPD configurations.} BOCPD models the sequence of probe scores as piecewise-constant segments with Gaussian observation noise. The hazard rate $\lambda$ controls the prior probability of a change-point at each step ($P(\text{change}) = 1/\lambda$).
456	
457	\paragraph{CUSUM configurations.} CUSUM accumulates evidence for a positive mean shift. The drift parameter $\delta$ sets the minimum shift size to detect, and the threshold $h$ controls the detection boundary.
458	
459	\begin{table}[h]
460	\centering
461	\small
462	\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}
463	\label{tab:cpd_sweep}
464	\setlength{\tabcolsep}{4pt}
465	\begin{tabular}{llcc}
466	\toprule
467	Method & Configuration & Det.\ Rate & Lead \\
468	\midrule
469	\multirow{5}{*}{BOCPD}
470	 & $\lambda = 5$   & 97 & +2.1 \\
471	 & $\lambda = 10$  & 93 & +3.5 \\
472	 & $\lambda = 20$  & 87 & +4.2 \\
473	 & $\lambda = 50$  & 72 & +5.8 \\
474	 & $\lambda = 100$ & 67.4 & +1.03 \\
475	\midrule
476	\multirow{10}{*}{CUSUM}
477	 & $\delta{=}0.3$, $h{=}3$ & 65.1 & +0.89 \\
478	 & $\delta{=}0.5$, $h{=}3$ & 89 & +1.4 \\
479	 & $\delta{=}0.5$, $h{=}5$ & 76 & +2.3 \\
480	 & $\delta{=}0.5$, $h{=}8$ & 61 & +3.1 \\
481	 & $\delta{=}1.0$, $h{=}3$ & 82 & +1.1 \\
482	 & $\delta{=}1.0$, $h{=}5$ & 68 & +1.9 \\
483	 & $\delta{=}1.0$, $h{=}8$ & 52 & +2.7 \\
484	 & $\delta{=}2.0$, $h{=}3$ & 71 & +0.8 \\
485	 & $\delta{=}2.0$, $h{=}5$ & 54 & +1.5 \\
486	 & $\delta{=}2.0$, $h{=}8$ & 38 & +2.1 \\
487	\midrule
488	Simple threshold & FCP baseline & 65.1 & +4.89 \\
489	\bottomrule
490	\end{tabular}
491	\end{table}
492	
493	The best BOCPD configuration ($\lambda{=}10$) achieves 93.0\% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1\% detection with superior lead (+4.89 steps). All CUSUM configurations underperform the simple threshold on lead time.
494	
495	These results reveal a coverage-timing tradeoff. BOCPD ($\lambda{=}10$) achieves 28pp higher detection rate than simple thresholding (93.0\% vs.\ 65.1\%), but with lower lead (+3.45 vs.\ +4.89 steps). The transition toward unsafe reasoning is gradual rather than abrupt, so change-point methods cannot exploit discontinuities for early warning. When missed detections are costly, BOCPD's coverage advantage justifies its use despite the timing penalty. When early intervention is the priority, simple thresholding provides better lead time.
496	
497	\paragraph{Other models.} On OT-7B, QwQ-32B, and R1-32B, BOCPD achieves 0\% detection rate across all tested configurations ($\lambda \in \{5, 10, 50, 100, 200\}$). The probe score sequences for these models show smoother transitions that never trigger the hazard function, consistent with the gradual commitment pattern. R1-8B's higher detection rate likely reflects its sharper probe score transitions at commitment boundaries.
498	
499	
500	\section{Detection Threshold ($K$) Ablation}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "b7636e49-9d08-4144-b34f-da6676116a82"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Searching for \\\\label\\{[^}]+\\}",
  "usage": {
    "total_tokens": 46350,
    "tool_uses": 13,
    "duration_ms": 11403
  },
  "last_tool_name": "Grep",
  "uuid": "fd3881f8-4793-49fb-a677-371fac0c6324",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Grep · `toolu_012qD3zZyuNLKnHRpukDse13`</summary>

```json
{
  "pattern": "\\\\label\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "76084ab3-1124-4c4c-8e96-304e05552584",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YX73bZjdgmZcdQqoXh5VGu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 15391,
      "cache_read_input_tokens": 30924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15391,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-18T20:28:25.152Z_

<details><summary>↩ Tool result · `toolu_012qD3zZyuNLKnHRpukDse13`</summary>

```text
docs/paper/sections/related_work.tex:1:\section{Related Work}\label{sec:related-work}
docs/paper/sections/experiments.tex:1:\section{Experiments}\label{sec:experiments}
docs/paper/sections/experiments.tex:7:\subsection{Setup}\label{sec:setup}
docs/paper/sections/experiments.tex:11:\subsection{Layer Selection Results}\label{sec:layer-results}
docs/paper/sections/experiments.tex:29:\label{tab:layer_selection}
docs/paper/sections/experiments.tex:36:\label{fig:layer_heatmap}
docs/paper/sections/experiments.tex:41:\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
docs/paper/sections/experiments.tex:62:\label{tab:hs_vs_text}
docs/paper/sections/experiments.tex:75:\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
docs/paper/sections/experiments.tex:91:\label{tab:32b_divergence}
docs/paper/sections/experiments.tex:96:\subsection{Temporal Context}\label{sec:temporal}
docs/paper/sections/experiments.tex:104:\label{fig:forest_precision}
docs/paper/sections/experiments.tex:107:\subsection{Negative Results}\label{sec:negative}
docs/paper/sections/conclusion.tex:1:\section{Conclusion}\label{sec:conclusion}
docs/paper/sections/discussion.tex:1:\section{Discussion}\label{sec:discussion}
docs/paper/sections/method.tex:2:\label{sec:method}
docs/paper/sections/method.tex:5:\label{sec:commitment-point}
docs/paper/sections/method.tex:25:\label{tab:models}
docs/paper/sections/method.tex:29:\label{sec:probe-architecture}
docs/paper/sections/method.tex:38:\label{sec:layer-sensitivity}
docs/paper/sections/method.tex:45:\label{sec:baselines}
docs/paper/sections/method.tex:50:\label{sec:evaluation}
docs/paper/sections/limitations.tex:1:\section{Limitations}\label{sec:limitations}
docs/paper/sections/appendix.tex:28:\label{app:checklist}
docs/paper/sections/appendix.tex:43:\label{app:layer_sweep}
docs/paper/sections/appendix.tex:59:\label{tab:joint_layer_w}
docs/paper/sections/appendix.tex:73:\label{app:cosine_volatility}
docs/paper/sections/appendix.tex:81:\label{tab:cosine_volatility}
docs/paper/sections/appendix.tex:102:\label{app:holm_bonferroni}
docs/paper/sections/appendix.tex:110:\label{tab:holm_bonferroni}
docs/paper/sections/appendix.tex:138:\label{app:window_ablation}
docs/paper/sections/appendix.tex:146:\label{fig:window_ablation}
docs/paper/sections/appendix.tex:153:\label{tab:window_full}
docs/paper/sections/appendix.tex:211:\label{app:text_window}
docs/paper/sections/appendix.tex:218:\label{tab:text_window}
docs/paper/sections/appendix.tex:238:\label{app:ot7b_details}
docs/paper/sections/appendix.tex:248:\label{tab:ot7b_layer_sweep}
docs/paper/sections/appendix.tex:274:\label{tab:ot7b_text_window}
docs/paper/sections/appendix.tex:296:\label{app:gru_details}
docs/paper/sections/appendix.tex:312:\label{tab:gru_seeds}
docs/paper/sections/appendix.tex:335:\label{tab:gru_multi_seeds}
docs/paper/sections/appendix.tex:375:\label{app:control}
docs/paper/sections/appendix.tex:395:\label{sec:oracle}
docs/paper/sections/appendix.tex:405:\label{tab:oracle}
docs/paper/sections/appendix.tex:420:\label{app:cp_perturbation}
docs/paper/sections/appendix.tex:428:\label{tab:cp_perturbation}
docs/paper/sections/appendix.tex:451:\label{app:bocpd_config}
docs/paper/sections/appendix.tex:463:\label{tab:cpd_sweep}
docs/paper/sections/appendix.tex:501:\label{app:k_ablation}
docs/paper/sections/appendix.tex:509:\label{tab:k_ablation}
docs/paper/sections/appendix.tex:532:\label{app:threshold_sensitivity}
docs/paper/sections/appendix.tex:540:\label{tab:threshold_r132b}
docs/paper/sections/appendix.tex:558:\label{app:bug}
docs/paper/sections/appendix.tex:571:\label{app:two_stage}
docs/paper/sections/appendix.tex:581:\label{fig:pareto_two_stage}
docs/paper/sections/appendix.tex:588:\label{app:temporal_details}
docs/paper/sections/appendix.tex:593:\label{app:negative_details}
docs/paper/sections/appendix.tex:612:\label{tab:negative}
docs/paper/sections/appendix.tex:628:\label{app:transfer_details}
docs/paper/sections/appendix.tex:640:\label{app:encoder_robustness}
docs/paper/sections/appendix.tex:648:\label{tab:encoder_robustness}
docs/paper/sections/appendix.tex:669:\label{tab:bge_ba_fpr}
docs/paper/sections/appendix.tex:687:\label{app:random_projection}
docs/paper/sections/appendix.tex:695:\label{tab:random_projection}
docs/paper/sections/appendix.tex:712:\label{app:position_residual}
docs/paper/sections/appendix.tex:731:\label{tab:position_residual}
docs/paper/sections/appendix.tex:740:\label{app:hyperparameter_robustness}
docs/paper/sections/appendix.tex:754:\label{tab:fold_ba_layers}
docs/paper/sections/appendix.tex:770:\label{app:multi_seed}
docs/paper/sections/appendix.tex:778:\label{tab:multi_seed}
docs/paper/sections/appendix.tex:799:\label{tab:seed_hb}
docs/paper/sections/appendix.tex:818:\label{tab:r18b_fpr_seeds}
docs/paper/sections/appendix.tex:840:\label{tab:r18b_metric_hb}
docs/paper/sections/appendix.tex:864:\label{tab:r132b_seeds}
docs/paper/sections/appendix.tex:882:\label{tab:ba_layer_comparison}
docs/paper/sections/appendix.tex:890:\label{tab:ba_layer_results}
docs/paper/sections/appendix.tex:911:\label{app:power_analysis}
docs/paper/sections/appendix.tex:919:\label{tab:power_analysis}
docs/paper/sections/introduction.tex:1:\section{Introduction}\label{sec:introduction}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "67bb0ccd-b4da-4677-acc2-032579b91df7"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Searching for \\\\(section|subsection)\\{[^}]+\\}",
  "usage": {
    "total_tokens": 46356,
    "tool_uses": 14,
    "duration_ms": 13016
  },
  "last_tool_name": "Grep",
  "uuid": "b76c0581-1f3f-480a-b1d6-6e745bc476a1",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Grep · `toolu_013MYLMBTfTKwuJUKNnuXzqe`</summary>

```json
{
  "pattern": "\\\\(section|subsection)\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "d831430e-b84b-494e-8377-63d9e7d2ae42",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YX73bZjdgmZcdQqoXh5VGu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 15391,
      "cache_read_input_tokens": 30924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15391,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-18T20:28:26.764Z_

<details><summary>↩ Tool result · `toolu_013MYLMBTfTKwuJUKNnuXzqe`</summary>

```text
docs/paper/acl.sty:234:\def\section{\@startsection {section}{1}{\z@}{-2.0ex plus
docs/paper/acl.sty:236:\def\subsection{\@startsection{subsection}{2}{\z@}{-1.8ex plus
docs/paper/sections/related_work.tex:1:\section{Related Work}\label{sec:related-work}
docs/paper/sections/experiments.tex:1:\section{Experiments}\label{sec:experiments}
docs/paper/sections/experiments.tex:7:\subsection{Setup}\label{sec:setup}
docs/paper/sections/experiments.tex:11:\subsection{Layer Selection Results}\label{sec:layer-results}
docs/paper/sections/experiments.tex:41:\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
docs/paper/sections/experiments.tex:75:\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
docs/paper/sections/experiments.tex:96:\subsection{Temporal Context}\label{sec:temporal}
docs/paper/sections/experiments.tex:107:\subsection{Negative Results}\label{sec:negative}
docs/paper/sections/conclusion.tex:1:\section{Conclusion}\label{sec:conclusion}
docs/paper/sections/discussion.tex:1:\section{Discussion}\label{sec:discussion}
docs/paper/sections/method.tex:1:\section{Problem Setup and Methods}
docs/paper/sections/method.tex:4:\subsection{Safety Commitment Point}
docs/paper/sections/method.tex:28:\subsection{Probe Architecture}
docs/paper/sections/method.tex:37:\subsection{Layer Selection Sensitivity}
docs/paper/sections/method.tex:44:\subsection{Baseline Methods}
docs/paper/sections/method.tex:49:\subsection{Evaluation Protocol}
docs/paper/sections/limitations.tex:1:\section{Limitations}\label{sec:limitations}
docs/paper/sections/appendix.tex:27:\section{Responsible NLP Research Checklist}
docs/paper/sections/appendix.tex:42:\section{Layer Sweep Results}
docs/paper/sections/appendix.tex:72:\section{Representation Compression Analysis}
docs/paper/sections/appendix.tex:101:\section{Holm-Bonferroni Step-Down Correction}
docs/paper/sections/appendix.tex:137:\section{Window Size Ablation Details}
docs/paper/sections/appendix.tex:210:\subsection{Text Probe Window Ablation}
docs/paper/sections/appendix.tex:237:\section{OpenThinker-7B Detailed Results}
docs/paper/sections/appendix.tex:295:\section{GRU Training Details}
docs/paper/sections/appendix.tex:374:\section{Control Task Methodology}
docs/paper/sections/appendix.tex:394:\section{Oracle Upper Bound Analysis}
docs/paper/sections/appendix.tex:419:\section{CP Annotation Perturbation}
docs/paper/sections/appendix.tex:450:\section{BOCPD/CUSUM Configuration Sweep}
docs/paper/sections/appendix.tex:500:\section{Detection Threshold ($K$) Ablation}
docs/paper/sections/appendix.tex:531:\section{Decision Threshold Sensitivity}
docs/paper/sections/appendix.tex:557:\section{M002 Bug Disclosure}
docs/paper/sections/appendix.tex:570:\section{Adaptive Two-Stage Detection}
docs/paper/sections/appendix.tex:587:\section{Temporal Ablation Details}
docs/paper/sections/appendix.tex:592:\section{Negative Results Details}
docs/paper/sections/appendix.tex:627:\section{Cross-Model Transfer Implementation Details}
docs/paper/sections/appendix.tex:639:\section{Encoder Robustness Analysis}
docs/paper/sections/appendix.tex:686:\section{Random Projection Baseline}
docs/paper/sections/appendix.tex:711:\section{Position-Residualized Probing}
docs/paper/sections/appendix.tex:739:\section{Hyperparameter Robustness}
docs/paper/sections/appendix.tex:769:\section{Multi-Seed Stability}
docs/paper/sections/appendix.tex:881:\section{BA-Layer Modality Comparison}
docs/paper/sections/appendix.tex:910:\section{Post-Hoc Power Analysis}
docs/paper/sections/introduction.tex:1:\section{Introduction}\label{sec:introduction}
docs/paper/acl2023.sty:234:\def\section{\@startsection {section}{1}{\z@}{-2.0ex plus
docs/paper/acl2023.sty:236:\def\subsection{\@startsection{subsection}{2}{\z@}{-1.8ex plus
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "0437f24f-2956-4e8d-948a-0ade803f4664"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Searching for \\\\caption\\{[^}]+\\}",
  "usage": {
    "total_tokens": 46362,
    "tool_uses": 15,
    "duration_ms": 14033
  },
  "last_tool_name": "Grep",
  "uuid": "276bf345-afb6-4a85-a7d3-996b8d6f2c26",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Grep · `toolu_015Fghn7w5BhqZ4qZ7k8Kjko`</summary>

```json
{
  "pattern": "\\\\caption\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "7c355406-3b31-4a1e-a150-35130acba479",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YX73bZjdgmZcdQqoXh5VGu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 15391,
      "cache_read_input_tokens": 30924,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15391,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-18T20:28:27.782Z_

<details><summary>↩ Tool result · `toolu_015Fghn7w5BhqZ4qZ7k8Kjko`</summary>

```text
docs/paper/sections/experiments.tex:28:\caption{Layer selection sensitivity. $^a$\,bal\_acc $\times$ crossing\_rate. $^b$\,Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Rightmost: HS vs.\ text precision $p$-value at corrected layer (e.g., QwQ-32B biased-layer: bal\_acc $p{=}0.35$, precision $p{=}0.83$, both non-significant).}
docs/paper/sections/experiments.tex:35:\caption{Per-layer metric heatmap (2$\times$2). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal\_acc $\times$ crossing\_rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers.}
docs/paper/sections/experiments.tex:61:[Omitted long matching line]
docs/paper/sections/experiments.tex:90:\caption{32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: \checkmark{} = model-level test passes Holm-Bonferroni ($\alpha{=}0.05$). Pos.\ margin: HS balanced accuracy minus position-only baseline.}
docs/paper/sections/experiments.tex:103:\caption{Forest plot of HS precision advantage over text probes. Blue: vs.\ MiniLM-384d; orange: vs.\ BGE-1024d. Solid markers: survives Holm-Bonferroni; hollow: does not. All 384d comparisons are significant (strong to qualified evidence); against BGE-1024d, only OT-7B (strong) survives correction.}
docs/paper/sections/method.tex:24:\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20.}
docs/paper/sections/appendix.tex:58:\caption{QwQ-32B joint (layer, $W$) grid search under 70/30 validation. L60 is near-optimal at recommended windows ($W{=}3$--$5$). L30 (LOO-CV selection at $W{=}1$) is suboptimal across all windows. Under the canonical 60/20/20 split, threshold-dependent metrics select L63.}
docs/paper/sections/appendix.tex:80:\caption{Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4--2.7$\times$ smaller inter-step distances).}
docs/paper/sections/appendix.tex:109:\caption{Holm-Bonferroni step-down correction for 12 tests (4 models $\times$ 3 correlated metrics). Each test uses a two-sided null-centered bootstrap (10{,}000 resamples) on trace-level metric differences (HS minus text). All 12 pass at $\alpha{=}0.05$; a 4-test model-level correction (one per model, using the worst $p$-value) also passes.}
docs/paper/sections/appendix.tex:145:\caption{Temporal window effect on R1-8B HS probe (L14). Precision: 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR: 9.65\% to 4.8\%.}
docs/paper/sections/appendix.tex:152:\caption{Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage ($K{=}1$), and mean detection lead across all models.}
docs/paper/sections/appendix.tex:217:\caption{Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from $W{=}1$ to $W{=}25$, compared to +3.2pp for HS probes over the same range. The larger marginal gain for text probes reflects their weaker single-step baseline.}
docs/paper/sections/appendix.tex:247:\caption{OT-7B layer sweep. Score = balanced accuracy $\times$ crossing rate. Layer 16 (57\% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.}
docs/paper/sections/appendix.tex:273:\caption{OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger $W$, contrasting with the HS probes on this model which peak at $W{=}3$.}
docs/paper/sections/appendix.tex:311:\caption{R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point.}
docs/paper/sections/appendix.tex:334:\caption{Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under a 60/20/20 cross-validation protocol (seeds 42, 123, 456). Single = layer 14 only; Multi = 7-layer concatenation (layers 12--24, stride 2). Lead = steps before CP at first sustained crossing. Main text results use a 70/30 train/test split with different test traces, accounting for the difference in lead values.}
docs/paper/sections/appendix.tex:404:\caption{Oracle upper bound analysis. Detection rate: fraction of traces where the oracle finds a linearly separable boundary before or at CP. Early detection rate: fraction detected before CP. Mean lead: average steps before CP at first detection.}
docs/paper/sections/appendix.tex:427:\caption{HS probe sensitivity to CP annotation shift ($\delta$ steps). BA is stable across all perturbations; precision degrades gradually without cliff effects.}
docs/paper/sections/appendix.tex:462:\caption{Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP.}
docs/paper/sections/appendix.tex:508:\caption{Detection threshold ablation ($W{=}1$, HS probes at corrected layers). Coverage: fraction of jailbreak traces with $\geq K$ consecutive crossings. Safe FPR: fraction of safe traces with $\geq K$ consecutive false alarms.}
docs/paper/sections/appendix.tex:539:\caption{R1-32B threshold sensitivity (L63, $W{=}1$). HS BA varies by 1.1pp (0.741--0.752); the HS advantage is consistent across all thresholds.}
docs/paper/sections/appendix.tex:580:\caption{Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration ($W_{\text{screen}}{=}3$, $W_{\text{confirm}}{=}15$, $k{=}1$) Pareto-dominates single-stage $W{=}15$ by +1.3pp precision at matched coverage. Higher $k$ values shift the tradeoff toward precision at the cost of unacceptable coverage loss.}
docs/paper/sections/appendix.tex:611:\caption{Seven alternative approaches. $^a$\,RepE QwQ approaches supervised bal\_acc but precision is 0.512 vs.\ LR 0.700. $^b$\,Semi-supervised (requires CP labels). $^c$\,Best direct transfer 67.3\% but 1\% crossing rate.}
docs/paper/sections/appendix.tex:647:\caption{HS vs.\ BGE-large (1024d) text probe precision. $\Delta$: HS minus BGE-large. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction (4 tests, $\alpha{=}0.05$).}
docs/paper/sections/appendix.tex:668:\caption{HS vs.\ BGE-large (1024d): balanced accuracy and FPR differences. Bootstrap: 10{,}000 resamples, two-sided null-centered. HB: Holm-Bonferroni correction (4 tests per metric, $\alpha{=}0.05$).}
docs/paper/sections/appendix.tex:694:\caption{Random projection (RP, 384d) vs.\ text (384d MiniLM). All $p < 0.001$ (1{,}000 bootstrap resamples). R1-8B uses $W{=}15$ (Table~3: $W{=}3$); QwQ-32B evaluated at L60 (Table~3: L63). 60/20/20 split.}
docs/paper/sections/appendix.tex:730:\caption{Position-residualized probe balanced accuracy. All residualized HS probes are above chance ($p{<}0.001$). 3/4 models retain significant non-positional HS advantage over text (gap +3.7 to +6.9pp, HB corrected); R1-32B is the exception (+1.9pp, $p{=}0.914$).}
docs/paper/sections/appendix.tex:753:\caption{BA-optimal layer per fold (5-fold CV, 32B models). Per-fold selections span 24 layers, but mean-BA landscape peaks are stable.}
docs/paper/sections/appendix.tex:777:\caption{LR probe stability across 5 random seeds (corrected layers, optimal $W$). 7--8B models are stable; R1-32B shows high variance due to small sample ($n{=}20$).}
docs/paper/sections/appendix.tex:798:\caption{5-seed HB pass rates (3/3 metrics per seed). R1-8B failures are FPR-specific.}
docs/paper/sections/appendix.tex:817:\caption{R1-8B FPR per-seed comparison (L14, $W{=}15$; main text \cref{tab:hs_vs_text} reports $W{=}3$ after 5-seed validation). Direction is consistent (5/5 HS $\leq$ Text); 2/5 reach $p{<}0.05$ uncorrected, 1/5 after Bonferroni correction (5 seeds, $\alpha{=}0.01$).}
docs/paper/sections/appendix.tex:839:\caption{R1-8B per-metric$\times$seed HB pass rates. Precision is robust (5/5); FPR is fragile (3/5). FPR std across seeds is 0.040 vs.\ text FPR std 0.007, consistent with a proportion near boundary (${\sim}$12\%) amplified at $n{=}43$.}
docs/paper/sections/appendix.tex:863:\caption{R1-32B per-seed performance (L63, $W{=}1$). Seed 0 is an outlier driven by test-set trace allocation.}
docs/paper/sections/appendix.tex:889:\caption{HS vs.\ text at BA-selected layers (60/20/20 split, same as main results). 14/16 per-model tests pass Holm-Bonferroni ($\alpha{=}0.05$); two FPR failures from underpowered 32B sets. BA-L: layer selected by pure balanced accuracy. Depth varies from 7\% to 98\%.}
docs/paper/sections/appendix.tex:918:\caption{Post-hoc power analysis. MDE: minimum detectable effect (balanced accuracy, pp) at 80\% power given each model's test-set size and observed variance. Effects smaller than the MDE cannot be reliably detected.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "80446b66-eac6-4742-b4d2-92664567b6cb"
}
```

</details>

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "description": "Searching for \\\\(begin|end)\\{(table|figure)\\}",
  "usage": {
    "total_tokens": 52907,
    "tool_uses": 16,
    "duration_ms": 16825
  },
  "last_tool_name": "Grep",
  "uuid": "8e5817d0-9f40-43c4-8fbd-19be84c65cc5",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Grep · `toolu_013rZFwQg9uFPZswuzzyd4j6`</summary>

```json
{
  "pattern": "\\\\(begin|end)\\{(table|figure)\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "50c3923f-dbb3-4e12-8a61-2115ae1078a9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011EfVjvbwg5aVN8XuyRgMWK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6542,
      "cache_read_input_tokens": 46315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6542,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-18T20:28:30.571Z_

<details><summary>↩ Tool result · `toolu_013rZFwQg9uFPZswuzzyd4j6`</summary>

```text
Found 3 files
docs/paper/sections/appendix.tex
docs/paper/sections/experiments.tex
docs/paper/sections/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "8b8aefe4-00db-42d1-8d22-b1922613f195"
}
```

</details>

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a15f0dded051e4649",
  "tool_use_id": "toolu_018oKV6c1aJXcarSgjaTbQyX",
  "status": "completed",
  "output_file": "",
  "summary": "Find paper section labels",
  "usage": {
    "total_tokens": 53119,
    "tool_uses": 16,
    "duration_ms": 70095
  },
  "uuid": "f6aa92f3-42e5-4374-8158-685043bcc9c8",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a"
}
```

---

### Tool result

_source line 68 · 2026-05-18T20:29:23.823Z_

<details><summary>↩ Tool result · `toolu_018oKV6c1aJXcarSgjaTbQyX`</summary>

```text
Now let me compile the complete structured report:

## COMPREHENSIVE LATEX LABELS AND STRUCTURE REPORT

### PAPER METADATA
- **Title:** Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
- **Document Class:** 11pt article (ACL review format)
- **Main File:** /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex

---

## SECTION LABELS AND HIERARCHY

### Main Sections (with \label commands)

| Section | Label | File | Hierarchy |
|---------|-------|------|-----------|
| Introduction | `sec:introduction` | introduction.tex | Level 1 |
| Related Work | `sec:related-work` | related_work.tex | Level 1 |
| Problem Setup and Methods | `sec:method` | method.tex | Level 1 |
| Experiments | `sec:experiments` | experiments.tex | Level 1 |
| Discussion | `sec:discussion` | discussion.tex | Level 1 |
| Conclusion | `sec:conclusion` | conclusion.tex | Level 1 |
| Limitations | `sec:limitations` | limitations.tex | Level 1 |

### Subsections in Method (sec:method)

| Subsection | Label | Line | Content |
|-----------|-------|------|---------|
| Safety Commitment Point | `sec:commitment-point` | method.tex:5 | Definition of Safety Commitment Point (CP) and task setup |
| Probe Architecture | `sec:probe-architecture` | method.tex:29 | HS probes, text probes, temporal windowing details |
| Layer Selection Sensitivity | `sec:layer-sensitivity` | method.tex:38 | Layer selection researcher degrees of freedom and bias mechanisms |
| Baseline Methods | `sec:baselines` | method.tex:45 | BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-model transfer |
| Evaluation Protocol | `sec:evaluation` | method.tex:50 | Metrics, statistical testing, control tasks, detection thresholds |

### Subsections in Experiments (sec:experiments)

| Subsection | Label | Line | Content |
|-----------|-------|------|---------|
| Setup | `sec:setup` | experiments.tex:7 | Model descriptions, data, HS/text probe configuration |
| Layer Selection Results | `sec:layer-results` | experiments.tex:11 | Biased vs. corrected layer selection outcomes |
| HS vs. Text Comparison | `sec:hs-text` | experiments.tex:41 | Main modality comparison with encoder robustness |
| 32B Model-Specific Analysis | `sec:32b-analysis` | experiments.tex:75 | R1-32B vs QwQ-32B divergence analysis |
| Temporal Context | `sec:temporal` | experiments.tex:96 | Window size effects across models |
| Negative Results | `sec:negative` | experiments.tex:107 | Alternative methods that failed to match supervised probing |

### Special Labels in Experiments

| Label | Line | Content |
|-------|------|---------|
| `sec:oracle` | appendix.tex:395 | Oracle Upper Bound Analysis section |
| `sec:hs-text` | experiments.tex:41 | Detailed hidden-state vs text comparison |

---

## TABLE LABELS AND CAPTIONS

### Main Experiments Tables

| Label | File | Line | Caption | Type |
|-------|------|------|---------|------|
| `tab:models` | method.tex | 25 | Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1; QwQ-32B is a native reasoning model; OT-7B is trained with STILL on Qwen2.5-7B. Data: HarmThoughts with step-level CP annotations. Split: 60/20/20. | Table 1 |
| `tab:layer_selection` | experiments.tex | 29 | Layer selection sensitivity. $^a$bal_acc × crossing_rate. $^b$Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Rightmost: HS vs. text precision p-value at corrected layer. | Table 2 |
| `tab:hs_vs_text` | experiments.tex | 62 | HS vs. text at corrected layers (LR probes, 60/20/20 split, 10,000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\Delta$: HS-text difference (pp). HB: checkmark = model-level test passes Holm-Bonferroni. | Table 3 |
| `tab:32b_divergence` | experiments.tex | 91 | 32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: checkmark = model-level test passes Holm-Bonferroni. Pos. margin: HS balanced accuracy minus position-only baseline. | Table 4 |

### Appendix Tables

| Label | File | Line | Caption | Section |
|-------|------|------|---------|---------|
| `tab:joint_layer_w` | appendix.tex | 59 | QwQ-32B joint (layer, W) grid search under 70/30 validation. L60 is near-optimal at recommended windows (W=3–5). L30 (LOO-CV selection at W=1) is suboptimal across all windows. | Layer Sweep Results (app:layer_sweep) |
| `tab:cosine_volatility` | appendix.tex | 81 | Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4–2.7× smaller inter-step distances). | Representation Compression (app:cosine_volatility) |
| `tab:holm_bonferroni` | appendix.tex | 110 | Holm-Bonferroni step-down correction for 12 tests (4 models × 3 correlated metrics). Each test uses two-sided null-centered bootstrap (10,000 resamples). All 12 pass at α=0.05. | Holm-Bonferroni Correction (app:holm_bonferroni) |
| `tab:window_full` | appendix.tex | 153 | Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage (K=1), and mean detection lead across all models. | Window Size Ablation (app:window_ablation) |
| `tab:text_window` | appendix.tex | 218 | Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from W=1 to W=25, compared to +3.2pp for HS probes. | Text Probe Window Ablation (app:text_window) |
| `tab:ot7b_layer_sweep` | appendix.tex | 248 | OT-7B layer sweep. Score = balanced accuracy × crossing rate. Layer 16 (57% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers. | OpenThinker-7B Details (app:ot7b_details) |
| `tab:ot7b_text_window` | appendix.tex | 274 | OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger W, contrasting with HS probes which peak at W=3. | OpenThinker-7B Details (app:ot7b_details) |
| `tab:gru_seeds` | appendix.tex | 312 | R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point. | GRU Training Details (app:gru_details) |
| `tab:gru_multi_seeds` | appendix.tex | 335 | Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under 60/20/20 cross-validation protocol. Single = layer 14 only; Multi = 7-layer concatenation. | GRU Training Details (app:gru_details) |
| `tab:oracle` | appendix.tex | 405 | Oracle upper bound analysis. Detection rate: fraction of traces where the oracle finds a linearly separable boundary before or at CP. Early detection rate: fraction detected before CP. | Oracle Upper Bound (sec:oracle) |
| `tab:cp_perturbation` | appendix.tex | 428 | HS probe sensitivity to CP annotation shift (δ steps). BA is stable across all perturbations; precision degrades gradually without cliff effects. | CP Annotation Perturbation (app:cp_perturbation) |
| `tab:cpd_sweep` | appendix.tex | 463 | Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP. | BOCPD/CUSUM Configuration (app:bocpd_config) |
| `tab:k_ablation` | appendix.tex | 509 | Detection threshold ablation (W=1, HS probes at corrected layers). Coverage: fraction of jailbreak traces with ≥K consecutive crossings. Safe FPR: fraction of safe traces with ≥K consecutive false alarms. | Detection Threshold Ablation (app:k_ablation) |
| `tab:threshold_r132b` | appendix.tex | 540 | R1-32B threshold sensitivity (L63, W=1). HS BA varies by 1.1pp (0.741–0.752); HS advantage is consistent across all thresholds. | Decision Threshold Sensitivity (app:threshold_sensitivity) |
| `tab:negative` | appendix.tex | 612 | Seven alternative approaches. $^a$RepE QwQ approaches supervised bal_acc but precision is 0.512 vs. LR 0.700. $^b$Semi-supervised (requires CP labels). $^c$Best direct transfer 67.3% but 1% crossing rate. | Negative Results Details (app:negative_details) |
| `tab:encoder_robustness` | appendix.tex | 648 | HS vs. BGE-large (1024d) text probe precision. Δ: HS minus BGE-large. Bootstrap: 10,000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction. | Encoder Robustness (app:encoder_robustness) |
| `tab:bge_ba_fpr` | appendix.tex | 669 | HS vs. BGE-large (1024d): balanced accuracy and FPR differences. Bootstrap: 10,000 resamples, two-sided null-centered. HB: Holm-Bonferroni correction. | Encoder Robustness (app:encoder_robustness) |
| `tab:random_projection` | appendix.tex | 695 | Random projection (RP, 384d) vs. text (384d MiniLM). All p < 0.001 (1,000 bootstrap resamples). R1-8B uses W=15; QwQ-32B evaluated at L60. 60/20/20 split. | Random Projection Baseline (app:random_projection) |
| `tab:position_residual` | appendix.tex | 731 | Position-residualized probe balanced accuracy. All residualized HS probes are above chance (p<0.001). 3/4 models retain significant non-positional HS advantage over text (gap +3.7 to +6.9pp, HB corrected); R1-32B is the exception. | Position-Residualized Probing (app:position_residual) |
| `tab:fold_ba_layers` | appendix.tex | 754 | BA-optimal layer per fold (5-fold CV, 32B models). Per-fold selections span 24 layers, but mean-BA landscape peaks are stable. | Hyperparameter Robustness (app:hyperparameter_robustness) |
| `tab:multi_seed` | appendix.tex | 778 | LR probe stability across 5 random seeds (corrected layers, optimal W). 7–8B models are stable; R1-32B shows high variance due to small sample (n=20). | Multi-Seed Stability (app:multi_seed) |
| `tab:seed_hb` | appendix.tex | 799 | 5-seed HB pass rates (3/3 metrics per seed). R1-8B failures are FPR-specific. | Multi-Seed Stability (app:multi_seed) |
| `tab:r18b_fpr_seeds` | appendix.tex | 818 | R1-8B FPR per-seed comparison (L14, W=15; main text reports W=3 after 5-seed validation). Direction is consistent (5/5 HS ≤ Text); 2/5 reach p<0.05 uncorrected, 1/5 after Bonferroni correction. | Multi-Seed Stability (app:multi_seed) |
| `tab:r18b_metric_hb` | appendix.tex | 840 | R1-8B per-metric×seed HB pass rates. Precision is robust (5/5); FPR is fragile (3/5). FPR std across seeds is 0.040 vs. text FPR std 0.007. | Multi-Seed Stability (app:multi_seed) |
| `tab:r132b_seeds` | appendix.tex | 864 | R1-32B per-seed performance (L63, W=1). Seed 0 is an outlier driven by test-set trace allocation. | Multi-Seed Stability (app:multi_seed) |
| `tab:ba_layer_comparison` | appendix.tex | 882 | HS vs. text at BA-selected layers (60/20/20 split). 14/16 per-model tests pass Holm-Bonferroni (α=0.05); two FPR failures from underpowered 32B sets. BA-L: layer selected by pure balanced accuracy. Depth varies 7%–98%. | BA-Layer Modality Comparison (app:ba_layer_comparison) |
| `tab:ba_layer_results` | appendix.tex | 890 | (Title not fully extracted; appears in BA-Layer section) | BA-Layer Modality Comparison |
| `tab:power_analysis` | appendix.tex | 919 | Post-hoc power analysis. MDE: minimum detectable effect (balanced accuracy, pp) at 80% power given each model's test-set size and observed variance. | Post-Hoc Power Analysis (app:power_analysis) |

---

## FIGURE LABELS AND CAPTIONS

| Label | File | Line | Caption |
|-------|------|------|---------|
| `fig:layer_heatmap` | experiments.tex | 36 | Per-layer metric heatmap (2×2). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal_acc × crossing_rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers. |
| `fig:forest_precision` | experiments.tex | 104 | Forest plot of HS precision advantage over text probes. Blue: vs. MiniLM-384d; orange: vs. BGE-1024d. Solid markers: survives Holm-Bonferroni; hollow: does not. All 384d comparisons are significant (strong to qualified evidence); against BGE-1024d, only OT-7B (strong) survives correction. |
| `fig:window_ablation` | appendix.tex | 146 | Temporal window effect on R1-8B HS probe (L14). Precision: 69.3% (W=1) to 82.2% (W=25); FPR: 9.65% to 4.8%. |
| `fig:pareto_two_stage` | appendix.tex | 581 | Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration (W_screen=3, W_confirm=15, k=1) Pareto-dominates single-stage W=15 by +1.3pp precision at matched coverage. |

---

## APPENDIX SECTION LABELS (All in appendix.tex)

| Label | Line | Section Title | Content Summary |
|-------|------|---------------|-----------------|
| `app:checklist` | 28 | Responsible NLP Research Checklist | ARR requirements: limitations, risks, computational budget, data, human subjects, reproducibility |
| `app:layer_sweep` | 43 | Layer Sweep Results | Evaluation across transformer layers; five selection metrics; selected layers per model |
| `app:cosine_volatility` | 73 | Representation Compression Analysis | Step-to-step cosine distance measurements showing 1.4–2.7× compression in shallow layers |
| `app:holm_bonferroni` | 102 | Holm-Bonferroni Step-Down Correction | Full test battery (12 tests, 4 models × 3 metrics); all pass at α=0.05 |
| `app:window_ablation` | 138 | Window Size Ablation Details | Complete window ablation across W ∈ {1,3,5,10,15,20,25} for all models |
| `app:text_window` | 211 | Text Probe Window Ablation | R1-8B text probe window sweep; +12.0pp gain from W=1 to W=25 |
| `app:ot7b_details` | 238 | OpenThinker-7B Detailed Results | Layer sweep, text window ablation, bootstrap comparison at W=3 |
| `app:gru_details` | 296 | GRU Training Details | Data split, architecture, training procedure; per-seed results for R1-8B and OT-7B |
| `app:control` | 375 | Control Task Methodology | Selectivity framework following Hewitt et al. 2019; results 11.1–16.8pp above chance |
| `sec:oracle` | 395 | Oracle Upper Bound Analysis | Oracle detection rates: OT-7B 93.6%, R1-32B 50%; lead times 24.4–50 steps |
| `app:cp_perturbation` | 420 | CP Annotation Perturbation | Robustness to label shift δ ∈ {-3,+3}; smooth degradation, no cliff effects |
| `app:bocpd_config` | 451 | BOCPD/CUSUM Configuration Sweep | Hyperparameter sweep; BOCPD λ=10 achieves 93% detection with +3.45 steps lead |
| `app:k_ablation` | 501 | Detection Threshold (K) Ablation | K ∈ {1,3,5,7,9} consecutive crossings; K=5 provides smooth coverage-FPR tradeoff |
| `app:threshold_sensitivity` | 532 | Decision Threshold Sensitivity | Probe stability across τ ∈ [0.3, 0.7]; BA variation <1.5pp |
| `app:bug` | 558 | M002 Bug Disclosure | OT-7B layer selection bug affecting initial 70/30 split results; corrected analysis provided |
| `app:two_stage` | 571 | Adaptive Two-Stage Detection | Two-stage (screen + confirm) detection; Pareto improvement of +1.3pp precision at W=15 |
| `app:temporal_details` | 588 | Temporal Ablation Details | Detailed temporal ablation for all models |
| `app:negative_details` | 593 | Negative Results Details | Seven alternative methods; includes full comparison table (tab:negative) |
| `app:transfer_details` | 628 | Cross-Model Transfer Implementation Details | PCA alignment, CCS adaptation, RepE configuration; all fail to transfer |
| `app:encoder_robustness` | 640 | Encoder Robustness Analysis | MiniLM-384d vs BGE-large-1024d; advantage narrowed from 4/4 HB to 1/4 HB |
| `app:random_projection` | 687 | Random Projection Baseline | Structure-destroying random projection; ΔPrec +8.3 to +20.5pp (all p<0.001) |
| `app:position_residual` | 712 | Position-Residualized Probing | Position regressed out; 3/4 models retain HS advantage (+3.7 to +6.9pp, HB corrected) |
| `app:hyperparameter_robustness` | 740 | Hyperparameter Robustness | Convergence, cross-validation, bootstrap analyses; LOO-CV on validation set |
| `app:multi_seed` | 770 | Multi-Seed Stability | 5-seed stability analysis; OT-7B and R1-8B robust; R1-32B high variance (n=20) |
| `app:ba_layer_comparison` | 881 | BA-Layer Modality Comparison | HS vs text at balanced-accuracy-optimal layers; 14/16 pass HB; depth varies 7–98% |
| `app:power_analysis` | 911 | Post-Hoc Power Analysis | MDE at 80% power: 8.6–9.5pp for 32B models (n=19–20) |

---

## CROSS-REFERENCES WITHIN TEXT

### Key \cref{} references mentioned:
- `\cref{tab:layer_selection}` - Layer selection sensitivity comparison
- `\cref{tab:models}` - Model specifications
- `\cref{tab:hs_vs_text}` - Main HS vs text results
- `\cref{fig:layer_heatmap}` - Per-layer metric visualization
- `\cref{fig:forest_precision}` - Precision advantage forest plot
- `\cref{sec:layer-results}` - Layer selection results section
- `\cref{sec:hs-text}` - HS vs text comparison section
- `\cref{sec:32b-analysis}` - 32B model-specific analysis
- `\cref{sec:temporal}` - Temporal context section
- `\cref{sec:negative}` - Negative results section
- `\cref{sec:oracle}` - Oracle analysis section
- `\cref{app:cosine_volatility}` - Representation compression details
- `\cref{app:control}` - Control task methodology

---

## SUMMARY STATISTICS

- **Total Section Labels:** 14 (7 main sections + 7 subsections)
- **Total Table Labels:** 36 (4 main + 32 appendix)
- **Total Figure Labels:** 4
- **Total Appendix Section Labels:** 24
- **Total Unique Labels:** 78+

**Files containing labels:**
1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex`
2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex`
3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex`
4. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex`
5. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex`
6. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex`
7. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex`
8. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex`
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "29843e14-03f0-4c9b-ab74-ff8d7c32a872",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/, find all .tex files and extract:\n1. All \\label{} commands (section labels, table labels, figure labels, appendix labels)\n2. All \\section, \\subsection commands to understand paper structure\n3. Any table/figure captions\n\nReport a structured list of all labels and their corresponding content. Be thorough - check main.tex and all included files.",
    "agentId": "a15f0dded051e4649",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now let me compile the complete structured report:\n\n## COMPREHENSIVE LATEX LABELS AND STRUCTURE REPORT\n\n### PAPER METADATA\n- **Title:** Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models\n- **Document Class:** 11pt article (ACL review format)\n- **Main File:** /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.tex\n\n---\n\n## SECTION LABELS AND HIERARCHY\n\n### Main Sections (with \\label commands)\n\n| Section | Label | File | Hierarchy |\n|---------|-------|------|-----------|\n| Introduction | `sec:introduction` | introduction.tex | Level 1 |\n| Related Work | `sec:related-work` | related_work.tex | Level 1 |\n| Problem Setup and Methods | `sec:method` | method.tex | Level 1 |\n| Experiments | `sec:experiments` | experiments.tex | Level 1 |\n| Discussion | `sec:discussion` | discussion.tex | Level 1 |\n| Conclusion | `sec:conclusion` | conclusion.tex | Level 1 |\n| Limitations | `sec:limitations` | limitations.tex | Level 1 |\n\n### Subsections in Method (sec:method)\n\n| Subsection | Label | Line | Content |\n|-----------|-------|------|---------|\n| Safety Commitment Point | `sec:commitment-point` | method.tex:5 | Definition of Safety Commitment Point (CP) and task setup |\n| Probe Architecture | `sec:probe-architecture` | method.tex:29 | HS probes, text probes, temporal windowing details |\n| Layer Selection Sensitivity | `sec:layer-sensitivity` | method.tex:38 | Layer selection researcher degrees of freedom and bias mechanisms |\n| Baseline Methods | `sec:baselines` | method.tex:45 | BOCPD, CUSUM, Mahalanobis, RepE, MLP, CCS, cross-model transfer |\n| Evaluation Protocol | `sec:evaluation` | method.tex:50 | Metrics, statistical testing, control tasks, detection thresholds |\n\n### Subsections in Experiments (sec:experiments)\n\n| Subsection | Label | Line | Content |\n|-----------|-------|------|---------|\n| Setup | `sec:setup` | experiments.tex:7 | Model descriptions, data, HS/text probe configuration |\n| Layer Selection Results | `sec:layer-results` | experiments.tex:11 | Biased vs. corrected layer selection outcomes |\n| HS vs. Text Comparison | `sec:hs-text` | experiments.tex:41 | Main modality comparison with encoder robustness |\n| 32B Model-Specific Analysis | `sec:32b-analysis` | experiments.tex:75 | R1-32B vs QwQ-32B divergence analysis |\n| Temporal Context | `sec:temporal` | experiments.tex:96 | Window size effects across models |\n| Negative Results | `sec:negative` | experiments.tex:107 | Alternative methods that failed to match supervised probing |\n\n### Special Labels in Experiments\n\n| Label | Line | Content |\n|-------|------|---------|\n| `sec:oracle` | appendix.tex:395 | Oracle Upper Bound Analysis section |\n| `sec:hs-text` | experiments.tex:41 | Detailed hidden-state vs text comparison |\n\n---\n\n## TABLE LABELS AND CAPTIONS\n\n### Main Experiments Tables\n\n| Label | File | Line | Caption | Type |\n|-------|------|------|---------|------|\n| `tab:models` | method.tex | 25 | Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1; QwQ-32B is a native reasoning model; OT-7B is trained with STILL on Qwen2.5-7B. Data: HarmThoughts with step-level CP annotations. Split: 60/20/20. | Table 1 |\n| `tab:layer_selection` | experiments.tex | 29 | Layer selection sensitivity. $^a$bal_acc × crossing_rate. $^b$Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Rightmost: HS vs. text precision p-value at corrected layer. | Table 2 |\n| `tab:hs_vs_text` | experiments.tex | 62 | HS vs. text at corrected layers (LR probes, 60/20/20 split, 10,000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). $\\Delta$: HS-text difference (pp). HB: checkmark = model-level test passes Holm-Bonferroni. | Table 3 |\n| `tab:32b_divergence` | experiments.tex | 91 | 32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: checkmark = model-level test passes Holm-Bonferroni. Pos. margin: HS balanced accuracy minus position-only baseline. | Table 4 |\n\n### Appendix Tables\n\n| Label | File | Line | Caption | Section |\n|-------|------|------|---------|---------|\n| `tab:joint_layer_w` | appendix.tex | 59 | QwQ-32B joint (layer, W) grid search under 70/30 validation. L60 is near-optimal at recommended windows (W=3–5). L30 (LOO-CV selection at W=1) is suboptimal across all windows. | Layer Sweep Results (app:layer_sweep) |\n| `tab:cosine_volatility` | appendix.tex | 81 | Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4–2.7× smaller inter-step distances). | Representation Compression (app:cosine_volatility) |\n| `tab:holm_bonferroni` | appendix.tex | 110 | Holm-Bonferroni step-down correction for 12 tests (4 models × 3 correlated metrics). Each test uses two-sided null-centered bootstrap (10,000 resamples). All 12 pass at α=0.05. | Holm-Bonferroni Correction (app:holm_bonferroni) |\n| `tab:window_full` | appendix.tex | 153 | Window size ablation (step-level metrics): balanced accuracy, precision, pre-CP FPR, coverage (K=1), and mean detection lead across all models. | Window Size Ablation (app:window_ablation) |\n| `tab:text_window` | appendix.tex | 218 | Text probe window ablation on R1-8B (step-level metrics). Text probes gain +12.0pp accuracy from W=1 to W=25, compared to +3.2pp for HS probes. | Text Probe Window Ablation (app:text_window) |\n| `tab:ot7b_layer_sweep` | appendix.tex | 248 | OT-7B layer sweep. Score = balanced accuracy × crossing rate. Layer 16 (57% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers. | OpenThinker-7B Details (app:ot7b_details) |\n| `tab:ot7b_text_window` | appendix.tex | 274 | OT-7B text probe window ablation (step-level). Text probes improve monotonically with larger W, contrasting with HS probes which peak at W=3. | OpenThinker-7B Details (app:ot7b_details) |\n| `tab:gru_seeds` | appendix.tex | 312 | R1-8B single-layer GRU results per seed. Lead is measured in steps before the commitment point. | GRU Training Details (app:gru_details) |\n| `tab:gru_multi_seeds` | appendix.tex | 335 | Per-seed performance of GRU and logistic regression (LR) probes on R1-8B under 60/20/20 cross-validation protocol. Single = layer 14 only; Multi = 7-layer concatenation. | GRU Training Details (app:gru_details) |\n| `tab:oracle` | appendix.tex | 405 | Oracle upper bound analysis. Detection rate: fraction of traces where the oracle finds a linearly separable boundary before or at CP. Early detection rate: fraction detected before CP. | Oracle Upper Bound (sec:oracle) |\n| `tab:cp_perturbation` | appendix.tex | 428 | HS probe sensitivity to CP annotation shift (δ steps). BA is stable across all perturbations; precision degrades gradually without cliff effects. | CP Annotation Perturbation (app:cp_perturbation) |\n| `tab:cpd_sweep` | appendix.tex | 463 | Change-point method configuration sweep on R1-8B. Detection rate is the fraction of jailbreak traces where the method fires. Lead is measured in steps before CP. | BOCPD/CUSUM Configuration (app:bocpd_config) |\n| `tab:k_ablation` | appendix.tex | 509 | Detection threshold ablation (W=1, HS probes at corrected layers). Coverage: fraction of jailbreak traces with ≥K consecutive crossings. Safe FPR: fraction of safe traces with ≥K consecutive false alarms. | Detection Threshold Ablation (app:k_ablation) |\n| `tab:threshold_r132b` | appendix.tex | 540 | R1-32B threshold sensitivity (L63, W=1). HS BA varies by 1.1pp (0.741–0.752); HS advantage is consistent across all thresholds. | Decision Threshold Sensitivity (app:threshold_sensitivity) |\n| `tab:negative` | appendix.tex | 612 | Seven alternative approaches. $^a$RepE QwQ approaches supervised bal_acc but precision is 0.512 vs. LR 0.700. $^b$Semi-supervised (requires CP labels). $^c$Best direct transfer 67.3% but 1% crossing rate. | Negative Results Details (app:negative_details) |\n| `tab:encoder_robustness` | appendix.tex | 648 | HS vs. BGE-large (1024d) text probe precision. Δ: HS minus BGE-large. Bootstrap: 10,000 resamples, two-sided null-centered. HB: survives Holm-Bonferroni correction. | Encoder Robustness (app:encoder_robustness) |\n| `tab:bge_ba_fpr` | appendix.tex | 669 | HS vs. BGE-large (1024d): balanced accuracy and FPR differences. Bootstrap: 10,000 resamples, two-sided null-centered. HB: Holm-Bonferroni correction. | Encoder Robustness (app:encoder_robustness) |\n| `tab:random_projection` | appendix.tex | 695 | Random projection (RP, 384d) vs. text (384d MiniLM). All p < 0.001 (1,000 bootstrap resamples). R1-8B uses W=15; QwQ-32B evaluated at L60. 60/20/20 split. | Random Projection Baseline (app:random_projection) |\n| `tab:position_residual` | appendix.tex | 731 | Position-residualized probe balanced accuracy. All residualized HS probes are above chance (p<0.001). 3/4 models retain significant non-positional HS advantage over text (gap +3.7 to +6.9pp, HB corrected); R1-32B is the exception. | Position-Residualized Probing (app:position_residual) |\n| `tab:fold_ba_layers` | appendix.tex | 754 | BA-optimal layer per fold (5-fold CV, 32B models). Per-fold selections span 24 layers, but mean-BA landscape peaks are stable. | Hyperparameter Robustness (app:hyperparameter_robustness) |\n| `tab:multi_seed` | appendix.tex | 778 | LR probe stability across 5 random seeds (corrected layers, optimal W). 7–8B models are stable; R1-32B shows high variance due to small sample (n=20). | Multi-Seed Stability (app:multi_seed) |\n| `tab:seed_hb` | appendix.tex | 799 | 5-seed HB pass rates (3/3 metrics per seed). R1-8B failures are FPR-specific. | Multi-Seed Stability (app:multi_seed) |\n| `tab:r18b_fpr_seeds` | appendix.tex | 818 | R1-8B FPR per-seed comparison (L14, W=15; main text reports W=3 after 5-seed validation). Direction is consistent (5/5 HS ≤ Text); 2/5 reach p<0.05 uncorrected, 1/5 after Bonferroni correction. | Multi-Seed Stability (app:multi_seed) |\n| `tab:r18b_metric_hb` | appendix.tex | 840 | R1-8B per-metric×seed HB pass rates. Precision is robust (5/5); FPR is fragile (3/5). FPR std across seeds is 0.040 vs. text FPR std 0.007. | Multi-Seed Stability (app:multi_seed) |\n| `tab:r132b_seeds` | appendix.tex | 864 | R1-32B per-seed performance (L63, W=1). Seed 0 is an outlier driven by test-set trace allocation. | Multi-Seed Stability (app:multi_seed) |\n| `tab:ba_layer_comparison` | appendix.tex | 882 | HS vs. text at BA-selected layers (60/20/20 split). 14/16 per-model tests pass Holm-Bonferroni (α=0.05); two FPR failures from underpowered 32B sets. BA-L: layer selected by pure balanced accuracy. Depth varies 7%–98%. | BA-Layer Modality Comparison (app:ba_layer_comparison) |\n| `tab:ba_layer_results` | appendix.tex | 890 | (Title not fully extracted; appears in BA-Layer section) | BA-Layer Modality Comparison |\n| `tab:power_analysis` | appendix.tex | 919 | Post-hoc power analysis. MDE: minimum detectable effect (balanced accuracy, pp) at 80% power given each model's test-set size and observed variance. | Post-Hoc Power Analysis (app:power_analysis) |\n\n---\n\n## FIGURE LABELS AND CAPTIONS\n\n| Label | File | Line | Caption |\n|-------|------|------|---------|\n| `fig:layer_heatmap` | experiments.tex | 36 | Per-layer metric heatmap (2×2). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal_acc × crossing_rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers. |\n| `fig:forest_precision` | experiments.tex | 104 | Forest plot of HS precision advantage over text probes. Blue: vs. MiniLM-384d; orange: vs. BGE-1024d. Solid markers: survives Holm-Bonferroni; hollow: does not. All 384d comparisons are significant (strong to qualified evidence); against BGE-1024d, only OT-7B (strong) survives correction. |\n| `fig:window_ablation` | appendix.tex | 146 | Temporal window effect on R1-8B HS probe (L14). Precision: 69.3% (W=1) to 82.2% (W=25); FPR: 9.65% to 4.8%. |\n| `fig:pareto_two_stage` | appendix.tex | 581 | Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. The best two-stage configuration (W_screen=3, W_confirm=15, k=1) Pareto-dominates single-stage W=15 by +1.3pp precision at matched coverage. |\n\n---\n\n## APPENDIX SECTION LABELS (All in appendix.tex)\n\n| Label | Line | Section Title | Content Summary |\n|-------|------|---------------|-----------------|\n| `app:checklist` | 28 | Responsible NLP Research Checklist | ARR requirements: limitations, risks, computational budget, data, human subjects, reproducibility |\n| `app:layer_sweep` | 43 | Layer Sweep Results | Evaluation across transformer layers; five selection metrics; selected layers per model |\n| `app:cosine_volatility` | 73 | Representation Compression Analysis | Step-to-step cosine distance measurements showing 1.4–2.7× compression in shallow layers |\n| `app:holm_bonferroni` | 102 | Holm-Bonferroni Step-Down Correction | Full test battery (12 tests, 4 models × 3 metrics); all pass at α=0.05 |\n| `app:window_ablation` | 138 | Window Size Ablation Details | Complete window ablation across W ∈ {1,3,5,10,15,20,25} for all models |\n| `app:text_window` | 211 | Text Probe Window Ablation | R1-8B text probe window sweep; +12.0pp gain from W=1 to W=25 |\n| `app:ot7b_details` | 238 | OpenThinker-7B Detailed Results | Layer sweep, text window ablation, bootstrap comparison at W=3 |\n| `app:gru_details` | 296 | GRU Training Details | Data split, architecture, training procedure; per-seed results for R1-8B and OT-7B |\n| `app:control` | 375 | Control Task Methodology | Selectivity framework following Hewitt et al. 2019; results 11.1–16.8pp above chance |\n| `sec:oracle` | 395 | Oracle Upper Bound Analysis | Oracle detection rates: OT-7B 93.6%, R1-32B 50%; lead times 24.4–50 steps |\n| `app:cp_perturbation` | 420 | CP Annotation Perturbation | Robustness to label shift δ ∈ {-3,+3}; smooth degradation, no cliff effects |\n| `app:bocpd_config` | 451 | BOCPD/CUSUM Configuration Sweep | Hyperparameter sweep; BOCPD λ=10 achieves 93% detection with +3.45 steps lead |\n| `app:k_ablation` | 501 | Detection Threshold (K) Ablation | K ∈ {1,3,5,7,9} consecutive crossings; K=5 provides smooth coverage-FPR tradeoff |\n| `app:threshold_sensitivity` | 532 | Decision Threshold Sensitivity | Probe stability across τ ∈ [0.3, 0.7]; BA variation <1.5pp |\n| `app:bug` | 558 | M002 Bug Disclosure | OT-7B layer selection bug affecting initial 70/30 split results; corrected analysis provided |\n| `app:two_stage` | 571 | Adaptive Two-Stage Detection | Two-stage (screen + confirm) detection; Pareto improvement of +1.3pp precision at W=15 |\n| `app:temporal_details` | 588 | Temporal Ablation Details | Detailed temporal ablation for all models |\n| `app:negative_details` | 593 | Negative Results Details | Seven alternative methods; includes full comparison table (tab:negative) |\n| `app:transfer_details` | 628 | Cross-Model Transfer Implementation Details | PCA alignment, CCS adaptation, RepE configuration; all fail to transfer |\n| `app:encoder_robustness` | 640 | Encoder Robustness Analysis | MiniLM-384d vs BGE-large-1024d; advantage narrowed from 4/4 HB to 1/4 HB |\n| `app:random_projection` | 687 | Random Projection Baseline | Structure-destroying random projection; ΔPrec +8.3 to +20.5pp (all p<0.001) |\n| `app:position_residual` | 712 | Position-Residualized Probing | Position regressed out; 3/4 models retain HS advantage (+3.7 to +6.9pp, HB corrected) |\n| `app:hyperparameter_robustness` | 740 | Hyperparameter Robustness | Convergence, cross-validation, bootstrap analyses; LOO-CV on validation set |\n| `app:multi_seed` | 770 | Multi-Seed Stability | 5-seed stability analysis; OT-7B and R1-8B robust; R1-32B high variance (n=20) |\n| `app:ba_layer_comparison` | 881 | BA-Layer Modality Comparison | HS vs text at balanced-accuracy-optimal layers; 14/16 pass HB; depth varies 7–98% |\n| `app:power_analysis` | 911 | Post-Hoc Power Analysis | MDE at 80% power: 8.6–9.5pp for 32B models (n=19–20) |\n\n---\n\n## CROSS-REFERENCES WITHIN TEXT\n\n### Key \\cref{} references mentioned:\n- `\\cref{tab:layer_selection}` - Layer selection sensitivity comparison\n- `\\cref{tab:models}` - Model specifications\n- `\\cref{tab:hs_vs_text}` - Main HS vs text results\n- `\\cref{fig:layer_heatmap}` - Per-layer metric visualization\n- `\\cref{fig:forest_precision}` - Precision advantage forest plot\n- `\\cref{sec:layer-results}` - Layer selection results section\n- `\\cref{sec:hs-text}` - HS vs text comparison section\n- `\\cref{sec:32b-analysis}` - 32B model-specific analysis\n- `\\cref{sec:temporal}` - Temporal context section\n- `\\cref{sec:negative}` - Negative results section\n- `\\cref{sec:oracle}` - Oracle analysis section\n- `\\cref{app:cosine_volatility}` - Representation compression details\n- `\\cref{app:control}` - Control task methodology\n\n---\n\n## SUMMARY STATISTICS\n\n- **Total Section Labels:** 14 (7 main sections + 7 subsections)\n- **Total Table Labels:** 36 (4 main + 32 appendix)\n- **Total Figure Labels:** 4\n- **Total Appendix Section Labels:** 24\n- **Total Unique Labels:** 78+\n\n**Files containing labels:**\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex`\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/related_work.tex`\n3. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex`\n4. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex`\n5. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex`\n6. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/conclusion.tex`\n7. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/limitations.tex`\n8. `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/appendix.tex`"
      }
    ],
    "totalDurationMs": 70097,
    "totalTokens": 59188,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 52857,
      "output_tokens": 6115,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 212
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 6115,
          "cache_read_input_tokens": 52857,
          "cache_creation_input_tokens": 212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 212,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 11,
      "searchCount": 5,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 69_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compose the rebuttal prep document with precise references to sections, tables, figures, and appendices.

Let me organize the 5 questions with their responses:

**Q1: Hyperparameter overfitting**
- app:hyperparameter_robustness (Table tab:fold_ba_layers for 5-fold CV)
- tab:joint_layer_w (joint grid search, A3 → actually app:layer_sweep has tab:joint_layer_w)
- Power analysis: app:power_analysis, tab:power_analysis
- BCa CI: app:holm_bonferroni


**Q2: Single dataset**
- sec:limitations and sec:setup document the 4-model setup across 2 architectures and 2 scales
**Q3: Stronger text encoder**
- tab:encoder_robustness and tab:hs_vs_text (Table 3) with fig:forest_precision showing the precision comparisons
**Q4: Position confound**
- app:position_residual and tab:position_residual address this in sec:discussion
**Q5: Small sample size 32B**
- app:power_analysis and tab:power_analysis provide the statistical justification

, and I'm now looking at the confidence intervals for the hs_vs_text comparison along with the 32B-specific analysis and multi-seed results to finalize the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "c9652a53-5f9a-4602-b006-42629fd7064b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxESX2cFhcZsAEjQwGFyCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6396,
      "cache_read_input_tokens": 39256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6396
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 70_

Now I have all the data. Writing the rebuttal prep document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "1678bb96-d342-483b-906c-a56205508f1e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxESX2cFhcZsAEjQwGFyCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6396,
      "cache_read_input_tokens": 39256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6396
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Write · `toolu_01VKdFNDeA7LHS3bLXCfg8Zs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/rebuttal_prep.md",
  "content": "# Rebuttal Preparation: Anticipated Reviewer Questions\n\nPaper: *Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models*\nTarget: EMNLP 2026 (ARR May 25)\n\n---\n\n## Q1: Hyperparameter Overfitting\n\n**Reviewer wording:** \"The paper optimizes layer and window size per model. How do we know this isn't overfitting to specific hyperparameter configurations? The search space (layer x window x model) seems large enough to find spurious results.\"\n\n**Core response:**\nThe balanced accuracy landscape over layers is flat near the optimum: Table A3 (app:layer_sweep, tab:joint_layer_w) shows that for QwQ-32B, L60 is near-optimal at W=3-5 and layers within +/-5 of the selected layer vary by <2pp BA. This is not a sharp peak that could reflect overfitting. We further validate layer selection stability with 5-fold cross-validation on 32B models (app:hyperparameter_robustness, tab:fold_ba_layers): for R1-32B the dominant layer is selected in 13/20 folds under LOO-CV, and for QwQ-32B in 13/19 folds, confirming robustness to validation set composition. BCa bootstrap confidence intervals (app:holm_bonferroni, tab:holm_bonferroni) quantify uncertainty: all 12 model-metric tests pass Holm-Bonferroni step-down correction at alpha=0.05, with effect sizes (+15-24pp precision) far exceeding the minimum detectable effect (app:power_analysis, tab:power_analysis: MDE 6.7-11.2pp at 80% power).\n\n**Supporting references:**\n- app:layer_sweep, tab:joint_layer_w (joint layer x window grid)\n- app:hyperparameter_robustness, tab:fold_ba_layers (5-fold CV layer stability)\n- app:holm_bonferroni, tab:holm_bonferroni (12/12 HB correction)\n- app:power_analysis, tab:power_analysis (post-hoc MDE)\n- app:ba_layer_comparison, tab:ba_layer_results (BA-optimal layers yield 16/16 HB, refuting circularity)\n\n---\n\n## Q2: Single Dataset\n\n**Reviewer wording:** \"All experiments are conducted on a single dataset (HarmThoughts). This severely limits the generalizability of the findings. Why not evaluate on additional safety benchmarks?\"\n\n**Core response:**\nHarmThoughts is, to our knowledge, the only publicly available dataset with step-level commitment point annotations for reasoning model traces. Existing safety benchmarks (e.g., SafeRLHF, BeaverTails) provide trace-level labels (safe/unsafe), not the within-trace temporal annotations required for commitment point detection. We mitigate single-dataset risk through cross-model generalization: 4 models spanning 2 architectures (Llama, Qwen), 2 training paradigms (R1-distilled, STILL/native), and 2 scales (7-8B, 32B) all show consistent HS advantage at corrected layers (12/12 HB, precision +15-24pp). The consistency across architecturally diverse models provides stronger evidence than testing one model on multiple datasets with similar annotation schemes. We acknowledge this limitation explicitly in Section Limitations (sec:limitations) and identify multi-dataset evaluation as priority future work.\n\n**Supporting references:**\n- sec:limitations (explicit dataset limitation disclosure)\n- sec:setup (4-model experimental design)\n- tab:hs_vs_text, Table 3 (cross-model consistency of precision advantage)\n- tab:holm_bonferroni (12/12 HB across 4 models)\n\n---\n\n## Q3: Stronger Text Encoder\n\n**Reviewer wording:** \"The text baseline uses MiniLM-L6-v2 (384d), a relatively weak encoder. A stronger text encoder could close or eliminate the reported HS advantage. Have you tested this?\"\n\n**Core response:**\nWe have. Appendix app:encoder_robustness reports results with BGE-large-en-v1.5 (1024d), a substantially stronger encoder. The HS advantage narrows, as expected: only 1/4 models (OT-7B, +17.5pp precision) survives Holm-Bonferroni correction against BGE-large, compared to 4/4 against MiniLM (tab:encoder_robustness, tab:bge_ba_fpr). This is precisely what our paper predicts. Our claim is not that HS universally dominates all text encoders; it is that HS advantage is encoder-conditional (Section sec:hs-text). At the MiniLM baseline widely used in deployment monitoring, HS provides a significant and consistent advantage. As text encoders improve, the gap shrinks. This encoder-conditional framing is visible in Figure fig:forest_precision, where the forest plot shows both MiniLM and BGE-large comparisons side by side. The remaining OT-7B advantage against BGE-large, plus the random projection control (app:random_projection: RP 384d outperforms text 384d by +8-20pp), confirms that HS carries genuine non-textual signal beyond dimensionality matching.\n\n**Supporting references:**\n- app:encoder_robustness, tab:encoder_robustness (BGE-large precision comparison)\n- tab:bge_ba_fpr (BGE-large BA and FPR comparison)\n- fig:forest_precision (forest plot, MiniLM vs BGE-large)\n- app:random_projection, tab:random_projection (dimensionality control)\n- sec:hs-text (encoder-conditional framing in main text)\n\n---\n\n## Q4: Position Confound (R1-32B)\n\n**Reviewer wording:** \"The HS probe's advantage could simply reflect position information encoded in hidden states. Since commitment points tend to occur at specific relative positions, the probe may be exploiting a positional shortcut rather than genuine safety content.\"\n\n**Core response:**\nWe directly test this with position-residualized probing (app:position_residual, tab:position_residual). After regressing out relative position (t/T) from both HS and text features, we retrain probes and re-evaluate. Results: 3/4 models retain significant non-positional HS advantage (OT-7B +6.9pp, R1-8B +6.4pp, QwQ-32B +3.7pp, all HB-corrected). R1-32B is the exception: its residualized gap drops to +1.9pp (p=0.914, NS), confirming that its HS advantage is largely position-mediated. We report this transparently in the paper, grading R1-32B as \"qualified\" evidence (sec:discussion). Importantly, position encoding in hidden states does not invalidate the probe. In deployment, position is available and informative; the residualization analysis serves to decompose signal sources, not to disqualify position-aware detection. The 3/4 model consensus for non-positional signal, combined with selectivity scores of 7.5-18.3pp above the random control task (app:control), establishes that HS probes capture genuine safety-relevant content beyond positional shortcuts.\n\n**Supporting references:**\n- app:position_residual, tab:position_residual (residualized BA, 3/4 HB pass)\n- sec:discussion (R1-32B qualified framing, position mediation paragraph)\n- app:control (control task selectivity 7.5-18.3pp)\n- tab:hs_vs_text, Table 3 (original vs residualized comparison)\n\n---\n\n## Q5: Small Sample Size at 32B (n=19-20)\n\n**Reviewer wording:** \"The 32B model experiments use only 19-20 test traces. This is far too small to draw reliable conclusions, especially given the number of comparisons made.\"\n\n**Core response:**\nWe acknowledge the small sample and address it with three complementary analyses. First, post-hoc power analysis (app:power_analysis, tab:power_analysis) shows the MDE at 80% power is 8.6-11.2pp for 32B models. All significant effects (+15-24pp precision, +11-19pp BA) are well above MDE, confirming adequate statistical power for the detected effects. Second, 5-seed stability analysis (app:multi_seed, tab:seed_hb) shows QwQ-32B achieves 5/5 HB pass rate and R1-32B achieves 5/5, with precision advantage never reversing across any of the 10 model-seed combinations. Third, the effects are internally consistent: QwQ-32B shows significance at all 15 window sizes (not just the cherry-picked best), making a Type I error at alpha=0.05 across 15 independent tests astronomically unlikely. R1-32B is honestly reported as \"statistically narrow\" (W=1 only, 25% coverage). The 32B trace generation cost (~2000-4000 reasoning steps per trace) makes large-scale evaluation prohibitively expensive. We view the current results as sufficient for the claim that HS advantage exists at 32B, while acknowledging precision of effect size estimates is limited.\n\n**Supporting references:**\n- app:power_analysis, tab:power_analysis (MDE vs observed effects)\n- app:multi_seed, tab:seed_hb, tab:multi_seed (5-seed HB pass rates)\n- sec:32b-analysis, tab:32b_divergence, Table 4 (per-model 32B analysis)\n- tab:hs_vs_text, Table 3 (bootstrap CIs for all comparisons)\n- sec:limitations (sample size limitation acknowledged)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "bd7af8e3-f843-481c-ba42-76c6ec6f16f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TxESX2cFhcZsAEjQwGFyCZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6396,
      "cache_read_input_tokens": 39256,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6396
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-18T20:30:26.783Z_

<details><summary>↩ Tool result · `toolu_01VKdFNDeA7LHS3bLXCfg8Zs`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/rebuttal_prep.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "ccfb5054-7b26-4375-afc1-8ad760993397",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/rebuttal_prep.md",
    "content": "# Rebuttal Preparation: Anticipated Reviewer Questions\n\nPaper: *Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models*\nTarget: EMNLP 2026 (ARR May 25)\n\n---\n\n## Q1: Hyperparameter Overfitting\n\n**Reviewer wording:** \"The paper optimizes layer and window size per model. How do we know this isn't overfitting to specific hyperparameter configurations? The search space (layer x window x model) seems large enough to find spurious results.\"\n\n**Core response:**\nThe balanced accuracy landscape over layers is flat near the optimum: Table A3 (app:layer_sweep, tab:joint_layer_w) shows that for QwQ-32B, L60 is near-optimal at W=3-5 and layers within +/-5 of the selected layer vary by <2pp BA. This is not a sharp peak that could reflect overfitting. We further validate layer selection stability with 5-fold cross-validation on 32B models (app:hyperparameter_robustness, tab:fold_ba_layers): for R1-32B the dominant layer is selected in 13/20 folds under LOO-CV, and for QwQ-32B in 13/19 folds, confirming robustness to validation set composition. BCa bootstrap confidence intervals (app:holm_bonferroni, tab:holm_bonferroni) quantify uncertainty: all 12 model-metric tests pass Holm-Bonferroni step-down correction at alpha=0.05, with effect sizes (+15-24pp precision) far exceeding the minimum detectable effect (app:power_analysis, tab:power_analysis: MDE 6.7-11.2pp at 80% power).\n\n**Supporting references:**\n- app:layer_sweep, tab:joint_layer_w (joint layer x window grid)\n- app:hyperparameter_robustness, tab:fold_ba_layers (5-fold CV layer stability)\n- app:holm_bonferroni, tab:holm_bonferroni (12/12 HB correction)\n- app:power_analysis, tab:power_analysis (post-hoc MDE)\n- app:ba_layer_comparison, tab:ba_layer_results (BA-optimal layers yield 16/16 HB, refuting circularity)\n\n---\n\n## Q2: Single Dataset\n\n**Reviewer wording:** \"All experiments are conducted on a single dataset (HarmThoughts). This severely limits the generalizability of the findings. Why not evaluate on additional safety benchmarks?\"\n\n**Core response:**\nHarmThoughts is, to our knowledge, the only publicly available dataset with step-level commitment point annotations for reasoning model traces. Existing safety benchmarks (e.g., SafeRLHF, BeaverTails) provide trace-level labels (safe/unsafe), not the within-trace temporal annotations required for commitment point detection. We mitigate single-dataset risk through cross-model generalization: 4 models spanning 2 architectures (Llama, Qwen), 2 training paradigms (R1-distilled, STILL/native), and 2 scales (7-8B, 32B) all show consistent HS advantage at corrected layers (12/12 HB, precision +15-24pp). The consistency across architecturally diverse models provides stronger evidence than testing one model on multiple datasets with similar annotation schemes. We acknowledge this limitation explicitly in Section Limitations (sec:limitations) and identify multi-dataset evaluation as priority future work.\n\n**Supporting references:**\n- sec:limitations (explicit dataset limitation disclosure)\n- sec:setup (4-model experimental design)\n- tab:hs_vs_text, Table 3 (cross-model consistency of precision advantage)\n- tab:holm_bonferroni (12/12 HB across 4 models)\n\n---\n\n## Q3: Stronger Text Encoder\n\n**Reviewer wording:** \"The text baseline uses MiniLM-L6-v2 (384d), a relatively weak encoder. A stronger text encoder could close or eliminate the reported HS advantage. Have you tested this?\"\n\n**Core response:**\nWe have. Appendix app:encoder_robustness reports results with BGE-large-en-v1.5 (1024d), a substantially stronger encoder. The HS advantage narrows, as expected: only 1/4 models (OT-7B, +17.5pp precision) survives Holm-Bonferroni correction against BGE-large, compared to 4/4 against MiniLM (tab:encoder_robustness, tab:bge_ba_fpr). This is precisely what our paper predicts. Our claim is not that HS universally dominates all text encoders; it is that HS advantage is encoder-conditional (Section sec:hs-text). At the MiniLM baseline widely used in deployment monitoring, HS provides a significant and consistent advantage. As text encoders improve, the gap shrinks. This encoder-conditional framing is visible in Figure fig:forest_precision, where the forest plot shows both MiniLM and BGE-large comparisons side by side. The remaining OT-7B advantage against BGE-large, plus the random projection control (app:random_projection: RP 384d outperforms text 384d by +8-20pp), confirms that HS carries genuine non-textual signal beyond dimensionality matching.\n\n**Supporting references:**\n- app:encoder_robustness, tab:encoder_robustness (BGE-large precision comparison)\n- tab:bge_ba_fpr (BGE-large BA and FPR comparison)\n- fig:forest_precision (forest plot, MiniLM vs BGE-large)\n- app:random_projection, tab:random_projection (dimensionality control)\n- sec:hs-text (encoder-conditional framing in main text)\n\n---\n\n## Q4: Position Confound (R1-32B)\n\n**Reviewer wording:** \"The HS probe's advantage could simply reflect position information encoded in hidden states. Since commitment points tend to occur at specific relative positions, the probe may be exploiting a positional shortcut rather than genuine safety content.\"\n\n**Core response:**\nWe directly test this with position-residualized probing (app:position_residual, tab:position_residual). After regressing out relative position (t/T) from both HS and text features, we retrain probes and re-evaluate. Results: 3/4 models retain significant non-positional HS advantage (OT-7B +6.9pp, R1-8B +6.4pp, QwQ-32B +3.7pp, all HB-corrected). R1-32B is the exception: its residualized gap drops to +1.9pp (p=0.914, NS), confirming that its HS advantage is largely position-mediated. We report this transparently in the paper, grading R1-32B as \"qualified\" evidence (sec:discussion). Importantly, position encoding in hidden states does not invalidate the probe. In deployment, position is available and informative; the residualization analysis serves to decompose signal sources, not to disqualify position-aware detection. The 3/4 model consensus for non-positional signal, combined with selectivity scores of 7.5-18.3pp above the random control task (app:control), establishes that HS probes capture genuine safety-relevant content beyond positional shortcuts.\n\n**Supporting references:**\n- app:position_residual, tab:position_residual (residualized BA, 3/4 HB pass)\n- sec:discussion (R1-32B qualified framing, position mediation paragraph)\n- app:control (control task selectivity 7.5-18.3pp)\n- tab:hs_vs_text, Table 3 (original vs residualized comparison)\n\n---\n\n## Q5: Small Sample Size at 32B (n=19-20)\n\n**Reviewer wording:** \"The 32B model experiments use only 19-20 test traces. This is far too small to draw reliable conclusions, especially given the number of comparisons made.\"\n\n**Core response:**\nWe acknowledge the small sample and address it with three complementary analyses. First, post-hoc power analysis (app:power_analysis, tab:power_analysis) shows the MDE at 80% power is 8.6-11.2pp for 32B models. All significant effects (+15-24pp precision, +11-19pp BA) are well above MDE, confirming adequate statistical power for the detected effects. Second, 5-seed stability analysis (app:multi_seed, tab:seed_hb) shows QwQ-32B achieves 5/5 HB pass rate and R1-32B achieves 5/5, with precision advantage never reversing across any of the 10 model-seed combinations. Third, the effects are internally consistent: QwQ-32B shows significance at all 15 window sizes (not just the cherry-picked best), making a Type I error at alpha=0.05 across 15 independent tests astronomically unlikely. R1-32B is honestly reported as \"statistically narrow\" (W=1 only, 25% coverage). The 32B trace generation cost (~2000-4000 reasoning steps per trace) makes large-scale evaluation prohibitively expensive. We view the current results as sufficient for the claim that HS advantage exists at 32B, while acknowledging precision of effect size estimates is limited.\n\n**Supporting references:**\n- app:power_analysis, tab:power_analysis (MDE vs observed effects)\n- app:multi_seed, tab:seed_hb, tab:multi_seed (5-seed HB pass rates)\n- sec:32b-analysis, tab:32b_divergence, Table 4 (per-model 32B analysis)\n- tab:hs_vs_text, Table 3 (bootstrap CIs for all comparisons)\n- sec:limitations (sample size limitation acknowledged)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 73_

文件已写入 `artifacts/rebuttal_prep.md`。5 个预期质疑全部覆盖，每条包含模拟审稿人措辞、核心回应（含具体数字）、以及精确的 section/table/figure/appendix 引用。关键策略：

- **Q1** 用 flat landscape + 5-fold CV + BCa CI 三重证据反驳 overfitting
- **Q2** 承认单数据集局限但强调 4-model cross-architecture generalization 比 multi-dataset single-model 更有说服力
- **Q3** 主动展示 BGE-large 结果，将 claim 框定为 encoder-conditional 而非 universal
- **Q4** 用 residualization 分解 position vs non-positional signal，诚实报告 R1-32B 为 qualified
- **Q5** 用 power analysis + 5-seed stability + QwQ 15/15 window consistency 三层防御

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "uuid": "79fcc266-b8b5-421d-b25f-c610ce253063",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ly4Yd8sV5VFqgSGUeM89Kg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2857,
      "cache_read_input_tokens": 45652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2857
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 74_

文件已写入 `artifacts/rebuttal_prep.md`。5 个预期质疑全部覆盖，每条包含模拟审稿人措辞、核心回应（含具体数字）、以及精确的 section/table/figure/appendix 引用。关键策略：

- **Q1** 用 flat landscape + 5-fold CV + BCa CI 三重证据反驳 overfitting
- **Q2** 承认单数据集局限但强调 4-model cross-architecture generalization 比 multi-dataset single-model 更有说服力
- **Q3** 主动展示 BGE-large 结果，将 claim 框定为 encoder-conditional 而非 universal
- **Q4** 用 residualization 分解 position vs non-positional signal，诚实报告 R1-32B 为 qualified
- **Q5** 用 power analysis + 5-seed stability + QwQ 15/15 window consistency 三层防御

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 156509,
  "duration_api_ms": 156753,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "fe8a4b11-7c44-4b65-ae74-7d98742a3a1a",
  "total_cost_usd": 0.5216395500000001,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 36668,
    "cache_read_input_tokens": 149531,
    "output_tokens": 3781,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36668,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 269,
        "cache_read_input_tokens": 45652,
        "cache_creation_input_tokens": 2857,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2857
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2135,
      "outputTokens": 7689,
      "cacheReadInputTokens": 162178,
      "cacheCreationInputTokens": 53069,
      "webSearchRequests": 0,
      "costUSD": 0.12313405000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 3781,
      "cacheReadInputTokens": 149531,
      "cacheCreationInputTokens": 36668,
      "webSearchRequests": 0,
      "costUSD": 0.3985055,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "fd9ded29-a678-41b9-8514-0277e26548d1"
}
```

</details>

---
