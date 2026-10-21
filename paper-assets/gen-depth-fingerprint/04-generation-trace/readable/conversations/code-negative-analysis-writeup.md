# code negative analysis writeup

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 7
- **Recorded user turns:** 0
- **Tool calls:** 3
- **Original source:** `logs/chats/worker_code_negative-analysis-writeup_20260517T033634.jsonl`
- **Structured JSON:** [`f8ff7f04b4312a7d5478.json`](../../sessions/f8/f8ff7f04b4312a7d5478.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

7 recorded events

### Tool call

_source line 1 · 2026-05-17T03:37:09.849017+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_negative-analysis-writeup_20260517T033634",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T03:37:09.849290+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_negative-analysis-writeup_20260517T033634",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T03:37:09.849442+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "mkdir -p /root/gen-depth-fingerprint/experiments/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_negative-analysis-writeup_20260517T033634",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "mkdir -p /root/gen-depth-fingerprint/experiments/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T03:37:09.849600+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.86}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_negative-analysis-writeup_20260517T033634",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T03:37:09.849780+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "autodl-5090",
  "command": "cat > /root/gen-depth-fingerprint/experiments/analysis/negative_experiment_review.json << 'JSONEOF'\n{\n  \"review_date\": \"2026-05-17\",\n  \"negative_experiments\": [\n    {\n      \"exp_id\": \"plan-004-v2\",\n      \"hypothesis\": \"Downstream utility: depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——5 variants × 3 seeds\",\n      \"result\": \"size_matched(2.367) < depth01(2.387) < binary_filtered(2.389), all(2.335) best by volume. Depth-aware curation does NOT improve CLM quality.\",\n      \"what_was_falsified\": \"The assumption that depth-aware data selection provides training signal superior to random subsampling. Data quantity dominates over depth composition.\",\n      \"handling\": \"D009: Reframed as diagnostic-not-curative. Paper honestly reports as negative finding in appendix.\",\n      \"parent_chain\": \"plan-004 (OOM failed) → plan-004-v2 (negative) → D009 reframe → [terminal]\",\n      \"missed_improvement_hints\": [\n        \"Could have tested OTHER downstream tasks (AI detection accuracy with depth-stratified training, style transfer, summarization) where depth information might actually help\",\n        \"Could have tested depth as a FEATURE (input signal to downstream model) rather than data FILTER — e.g., augmenting training data with depth labels as auxiliary signal\",\n        \"The negative result assumes CLM perplexity as sole metric. Depth-aware curation might help with output diversity or factuality even if perplexity is unchanged\"\n      ],\n      \"actionable_suggestion\": \"For future work / rebuttal: test depth as input feature for detection models, not just as data curation criterion. The negative finding is correctly scoped to 'curation for general CLM quality'.\"\n    }\n  ],\n  \"framing_level_negatives\": [\n    {\n      \"exp_id\": \"plan-001\",\n      \"original_hypothesis\": \"Claim 2 Feature Independence: reference-only features independently sufficient to discriminate depth\",\n      \"actual_result\": \"surface_only(0.76) > reference_only(0.72), original independence framing falsified\",\n      \"what_was_falsified\": \"The assumption that model-derived distributional features carry more depth signal than surface statistics. In reality, surface features (TTR, hapax) are stronger individual discriminators.\",\n      \"handling\": \"D003→D004→D005→D007: Progressive refinement from 'independence' to 'complementarity' to 'dual dynamics' to 'differential depth response'. Each step driven by data.\",\n      \"parent_chain\": \"plan-001 (framing negative) → D004 (reframe) → plan-002-eval (validates new framing) → D007 (re-dream validates) → [complete]\",\n      \"missed_improvement_hints\": [\n        \"entropy_min showed the most inconsistent behavior across experiments (direction reversal between prompt types). Could have investigated whether entropy_min captures a different phenomenon worth separating\",\n        \"The surface > reference finding might suggest that LEARNED features (e.g., fine-tuned probe on token distributions) could extract stronger signal than hand-crafted entropy statistics\",\n        \"tail_decay consistently low importance (0.012-0.015) across all experiments — suggests the rank 100-1000 range may not be optimal; could explore other tail ranges\"\n      ],\n      \"actionable_suggestion\": \"tail_decay's persistent low importance suggests either the feature definition needs revision (different rank range, or per-position rather than mean) or it genuinely adds minimal signal and could be replaced by a better shape feature.\"\n    },\n    {\n      \"exp_id\": \"plan-015\",\n      \"original_hypothesis\": \"No existing detector's continuous score achieves >0.70 ordinal depth classification\",\n      \"actual_result\": \"Avg-LogProb reaches 0.77, LD-Score 0.72 — both exceed threshold\",\n      \"what_was_falsified\": \"The assumption that existing detectors cannot capture depth signal. They can, but inconsistently across generators (CI spans 0.59-0.82).\",\n      \"handling\": \"D008: Reframe from 'detectors cannot' to 'detectors are inconsistent; our ensemble provides stable advantage'. plan-015-v2 confirmed with bug fixes + bootstrap CI.\",\n      \"parent_chain\": \"plan-015 (unexpected result) → plan-015-v2 (bug fix + CI) → D008 (reframe) → [complete]\",\n      \"missed_improvement_hints\": [\n        \"Avg-LogProb's strong performance (0.77) suggests our 7-feature set could be improved by including it as 8th feature (detector score as feature)\",\n        \"The wide CI of single detectors across generators reveals generator-specific detector biases — could be exploited with a generator-aware stacking approach\",\n        \"LD-Score's character trigram approach captures something our token-level features miss — could add character-level features to complement token-level ones\"\n      ],\n      \"actionable_suggestion\": \"Most impactful: add Avg-LogProb as 8th feature to the ensemble. The current 7-feature set + detector scores as additional features could close the gap with the 3-detector surface ensemble (Table 3: 0.70 vs 0.71).\"\n    }\n  ],\n  \"cross_cutting_insights\": {\n    \"feature_engineering\": \"tail_decay consistently underperforms (importance 0.01-0.02). entropy_min is unreliable (direction reversal). Both are candidates for replacement. Avg-LogProb as additional feature is the lowest-hanging fruit.\",\n    \"model_selection\": \"Error analysis shows Mistral-7B (45% error) and Qwen3-8B (38.5% error) are hardest. The reference model (Pythia-410M) may be too small/different to capture their distributional properties. A larger or multi-reference approach could help.\",\n    \"data_processing\": \"Depth-2 samples account for 48% error rate — the gen-1→gen-2 transition is where features haven't diverged enough. Possible fix: use confidence-based abstention (don't classify samples near decision boundary) or add depth-2-specific features.\",\n    \"overall_pattern\": \"All negatives point to the same root: our features capture ACCUMULATED drift well (gen-3, gen-4 easy) but not INITIAL divergence (gen-2 hard). Future work should focus on features that detect the first generation step's unique signature.\"\n  }\n}\nJSONEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_negative-analysis-writeup_20260517T033634",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "autodl-5090",
    "command": "cat > /root/gen-depth-fingerprint/experiments/analysis/negative_experiment_review.json << 'JSONEOF'\n{\n  \"review_date\": \"2026-05-17\",\n  \"negative_experiments\": [\n    {\n      \"exp_id\": \"plan-004-v2\",\n      \"hypothesis\": \"Downstream utility: depth-stratified 数据对 OLMo-2-0425-1B CLM fine-tuning 的影响——5 variants × 3 seeds\",\n      \"result\": \"size_matched(2.367) < depth01(2.387) < binary_filtered(2.389), all(2.335) best by volume. Depth-aware curation does NOT improve CLM quality.\",\n      \"what_was_falsified\": \"The assumption that depth-aware data selection provides training signal superior to random subsampling. Data quantity dominates over depth composition.\",\n      \"handling\": \"D009: Reframed as diagnostic-not-curative. Paper honestly reports as negative finding in appendix.\",\n      \"parent_chain\": \"plan-004 (OOM failed) → plan-004-v2 (negative) → D009 reframe → [terminal]\",\n      \"missed_improvement_hints\": [\n        \"Could have tested OTHER downstream tasks (AI detection accuracy with depth-stratified training, style transfer, summarization) where depth information might actually help\",\n        \"Could have tested depth as a FEATURE (input signal to downstream model) rather than data FILTER — e.g., augmenting training data with depth labels as auxiliary signal\",\n        \"The negative result assumes CLM perplexity as sole metric. Depth-aware curation might help with output diversity or factuality even if perplexity is unchanged\"\n      ],\n      \"actionable_suggestion\": \"For future work / rebuttal: test depth as input feature for detection models, not just as data curation criterion. The negative finding is correctly scoped to 'curation for general CLM quality'.\"\n    }\n  ],\n  \"framing_level_negatives\": [\n    {\n      \"exp_id\": \"plan-001\",\n      \"original_hypothesis\": \"Claim 2 Feature Independence: reference-only features independently sufficient to discriminate depth\",\n      \"actual_result\": \"surface_only(0.76) > reference_only(0.72), original independence framing falsified\",\n      \"what_was_falsified\": \"The assumption that model-derived distributional features carry more depth signal than surface statistics. In reality, surface features (TTR, hapax) are stronger individual discriminators.\",\n      \"handling\": \"D003→D004→D005→D007: Progressive refinement from 'independence' to 'complementarity' to 'dual dynamics' to 'differential depth response'. Each step driven by data.\",\n      \"parent_chain\": \"plan-001 (framing negative) → D004 (reframe) → plan-002-eval (validates new framing) → D007 (re-dream validates) → [complete]\",\n      \"missed_improvement_hints\": [\n        \"entropy_min showed the most inconsistent behavior across experiments (direction reversal between prompt types). Could have investigated whether entropy_min captures a different phenomenon worth separating\",\n        \"The surface > reference finding might suggest that LEARNED features (e.g., fine-tuned probe on token distributions) could extract stronger signal than hand-crafted entropy statistics\",\n        \"tail_decay consistently low importance (0.012-0.015) across all experiments — suggests the rank 100-1000 range may not be optimal; could explore other tail ranges\"\n      ],\n      \"actionable_suggestion\": \"tail_decay's persistent low importance suggests either the feature definition needs revision (different rank range, or per-position rather than mean) or it genuinely adds minimal signal and could be replaced by a better shape feature.\"\n    },\n    {\n      \"exp_id\": \"plan-015\",\n      \"original_hypothesis\": \"No existing detector's continuous score achieves >0.70 ordinal depth classification\",\n      \"actual_result\": \"Avg-LogProb reaches 0.77, LD-Score 0.72 — both exceed threshold\",\n      \"what_was_falsified\": \"The assumption that existing detectors cannot capture depth signal. They can, but inconsistently across generators (CI spans 0.59-0.82).\",\n      \"handling\": \"D008: Reframe from 'detectors cannot' to 'detectors are inconsistent; our ensemble provides stable advantage'. plan-015-v2 confirmed with bug fixes + bootstrap CI.\",\n      \"parent_chain\": \"plan-015 (unexpected result) → plan-015-v2 (bug fix + CI) → D008 (reframe) → [complete]\",\n      \"missed_improvement_hints\": [\n        \"Avg-LogProb's strong performance (0.77) suggests our 7-feature set could be improved by including it as 8th feature (detector score as feature)\",\n        \"The wide CI of single detectors across generators reveals generator-specific detector biases — could be exploited with a generator-aware stacking approach\",\n        \"LD-Score's character trigram approach captures something our token-level features miss — could add character-level features to complement token-level ones\"\n      ],\n      \"actionable_suggestion\": \"Most impactful: add Avg-LogProb as 8th feature to the ensemble. The current 7-feature set + detector scores as additional features could close the gap with the 3-detector surface ensemble (Table 3: 0.70 vs 0.71).\"\n    }\n  ],\n  \"cross_cutting_insights\": {\n    \"feature_engineering\": \"tail_decay consistently underperforms (importance 0.01-0.02). entropy_min is unreliable (direction reversal). Both are candidates for replacement. Avg-LogProb as additional feature is the lowest-hanging fruit.\",\n    \"model_selection\": \"Error analysis shows Mistral-7B (45% error) and Qwen3-8B (38.5% error) are hardest. The reference model (Pythia-410M) may be too small/different to capture their distributional properties. A larger or multi-reference approach could help.\",\n    \"data_processing\": \"Depth-2 samples account for 48% error rate — the gen-1→gen-2 transition is where features haven't diverged enough. Possible fix: use confidence-based abstention (don't classify samples near decision boundary) or add depth-2-specific features.\",\n    \"overall_pattern\": \"All negatives point to the same root: our features capture ACCUMULATED drift well (gen-3, gen-4 easy) but not INITIAL divergence (gen-2 hard). Future work should focus on features that detect the first generation step's unique signature.\"\n  }\n}\nJSONEOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T03:37:09.849981+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.31}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_negative-analysis-writeup_20260517T033634",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 7 · 2026-05-17T03:37:09.850136+00:00_

文件已写入 `/root/gen-depth-fingerprint/experiments/analysis/negative_experiment_review.json`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_negative-analysis-writeup_20260517T033634"
}
```

</details>

---
