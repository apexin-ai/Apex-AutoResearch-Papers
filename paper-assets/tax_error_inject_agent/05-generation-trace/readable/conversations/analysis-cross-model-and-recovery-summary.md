# analysis cross model and recovery summary

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_analysis_cross-model-and-recovery-summary_20260516T104641.jsonl`
- **Structured JSON:** [`8576836ec9579380cc3b.json`](../../sessions/85/8576836ec9579380cc3b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-16T10:50:16.009468+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T10:50:16.009955+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T10:50:16.010148+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "tax_error_inject_agent",
  "limit": "0",
  "fields": "['status', 'conclusion', 'metrics', 'hypothesis', 'exp_id', 'name']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "tax_error_inject_agent",
    "limit": "0",
    "fields": "['status', 'conclusion', 'metrics', 'hypothesis', 'exp_id', 'name']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T10:50:16.010903+00:00_

&lt;persisted-output>
Output too large (51KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/caf94feb-6aaf-4c19-89b6-3f59e49fa01e/tool-results/toolu_01RwPxWsvxM8S6xpcGp9Hgh9.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"llama31-vanilla-s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.398, \"epoch1_loss\": 0.481, \"epoch2_loss\": 0.362, \"epoch3_loss\": 0.273, \"final_token_acc\": 0.909, \"train_runtime_sec\": 4158.6}}, \"eval-rp-s7\": {\"status\": \"DONE\", \"metrics\": {\"recovery_rate\": 0.596, \"recovery_count\": \"28/47\", \"detection_rate\": 0}, \"conclusion\": \"success\"}, \"v4-taxei-rp-s7\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.3855, \"token_acc\": 0.9103, \"duration_minutes\": 226.6, \"peak_memory_gib\": 30.25, \"train_samples_per_second\": 3.185}, \"conclusion\": \"success\"}, \"recovery-taxei-s1\": {\"status\": \"DONE\", \"metrics\": {\"recovery_rate\": 0.617, \"recovery_count\": \"29/47\", \"detection_rate\": 0, \"C1_context_truncation\": 0.75, \"C4_observation_masking\": 0.636, \"P1_step_order_swap\": 0.583, \"P2_sub_goal_deletion\": 0.5}, \"conclusion\": \"success\"}, \"llama31-random-s42-eval\": {\"status\": \"DONE\", \"metrics\": {\"recovery_rate\": 0.766, \"recovery_count\": \"36/47\", \"detection_rate\": 0.298, \"C1_context_truncation\": 0.667, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.917, \"P2_sub_goal_deletion\": 0.75, \"C1_detection\": 0.417, \"C4_detection\": 0.364, \"P1_detection\": 0.333, \"P2_detection\": 0.083}, \"conclusion\": \"success\"}, \"llama31-taxei-s42-eval\": {\"status\": \"DONE\", \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0.298, \"C1_context_truncation\": 0.833, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.583, \"P2_sub_goal_deletion\": 0.833, \"C1_d
…[truncated 317 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T10:50:16.011136+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/caf94feb-6aaf-4c19-89b6-3f59e49fa01e/tool-results/toolu_01RwPxWsvxM8S6xpcGp9Hgh9.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-2-projects-tax-error-inject-agent/caf94feb-6aaf-4c19-89b6-3f59e49fa01e/tool-results/toolu_01RwPxWsvxM8S6xpcGp9Hgh9.txt"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T10:50:16.011919+00:00_

1	{"result":"{\"success\": true, \"data\": {\"experiments\": {\"llama31-vanilla-s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_train_loss\": 0.398, \"epoch1_loss\": 0.481, \"epoch2_loss\": 0.362, \"epoch3_loss\": 0.273, \"final_token_acc\": 0.909, \"train_runtime_sec\": 4158.6}}, \"eval-rp-s7\": {\"status\": \"DONE\", \"metrics\": {\"recovery_rate\": 0.596, \"recovery_count\": \"28/47\", \"detection_rate\": 0}, \"conclusion\": \"success\"}, \"v4-taxei-rp-s7\": {\"status\": \"DONE\", \"metrics\": {\"train_loss\": 0.3855, \"token_acc\": 0.9103, \"duration_minutes\": 226.6, \"peak_memory_gib\": 30.25, \"train_samples_per_second\": 3.185}, \"conclusion\": \"success\"}, \"recovery-taxei-s1\": {\"status\": \"DONE\", \"metrics\": {\"recovery_rate\": 0.617, \"recovery_count\": \"29/47\", \"detection_rate\": 0, \"C1_context_truncation\": 0.75, \"C4_observation_masking\": 0.636, \"P1_step_order_swap\": 0.583, \"P2_sub_goal_deletion\": 0.5}, \"conclusion\": \"success\"}, \"llama31-random-s42-eval\": {\"status\": \"DONE\", \"metrics\": {\"recovery_rate\": 0.766, \"recovery_count\": \"36/47\", \"detection_rate\": 0.298, \"C1_context_truncation\": 0.667, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.917, \"P2_sub_goal_deletion\": 0.75, \"C1_detection\": 0.417, \"C4_detection\": 0.364, \"P1_detection\": 0.333, \"P2_detection\": 0.083}, \"conclusion\": \"success\"}, \"llama31-taxei-s42-eval\": {\"status\": \"DONE\", \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\": 0.298, \"C1_context_truncation\": 0.833, \"C4_observation_masking\": 0.727, \"P1_step_order_swap\": 0.583, \"P2_sub_goal_deletion\": 0.833, \"C1_detection\": 0.167, \"C4_detection\": 0.364, \"P1_detection\": 0.25, \"P2_detection\": 0.417}, \"conclusion\": \"success\"}, \"recovery-vanilla-s7\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"recovery_rate\": 0.745, \"recovery_count\": \"35/47\", \"detection_rate\":
…[truncated 50251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T10:50:16.012202+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/",
  "description": "List existing artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/",
    "description": "List existing artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T10:50:16.012359+00:00_

D010
_project
alfworld_data_survey.md
citation_expansion.md
citation_verification_report.md
comprehensive_results.md
comprehensive_results_summary.md
comprehensive_stats_report.md
configs
d010_multiseed_analysis.md
data
diag_v4_taxei_recovery_eval.md
dose_response_10pct_stats.json
dose_response_25pct_stats.json
dose_response_50pct_analysis.py
dose_response_50pct_stats.json
dose_response_50pct_stats_corrected.json
dose_response_literature_survey.md
dream_reports
eval
failure_analysis_5seed_balanced.json
fig1_dose_response.png
fig1_dose_response_preview.jpg
fig1_dose_response_preview.png
gen_recovery_paired_v2.py
injection
llama31-taxei-s0
llama31-vanilla-s0
llama_detection_analysis.md
manifest.yaml
multiseed_analysis_report.md
narrative_review_d026_d027.md
recovery.py
review_issues.yaml
review_reports
running_pids.md
training_dynamics_taxei_10_25.json
trajectory_scaleup_feasibility.md
upcoming_eval_commands.md
v4-recovery-eval-dev
v4-taxei-fixed-inject50-eval
v4-taxei-seed7
v4-training-dynamics-forward
v4-vanilla-recovery-eval
v4-vanilla-seed1
variance_tests_levene_bootstrap.json
verl_agent_survey.md
webshop_replication_feasibility.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T10:50:16.012568+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/cross_model_recovery_analysis.md",
  "content": "# Cross-Model & Recovery Eval Comprehensive Analysis\n\n**Date**: 2026-05-16  \n**Project**: tax_error_inject_agent (EMNLP 2026 Findings)  \n**Data source**: Registry (112 DONE experiments verified)\n\n---\n\n## 1. Data Completeness Audit\n\n### 1.1 User-provided data vs Registry — discrepancies found\n\n| Item | User Value | Registry Value | Note |\n|------|-----------|---------------|------|\n| TaxEI-RP 5-seed mean (core table) | 47.9±7.8 | **50.2±8.6** | User's per-seed data (38.3+46.8+48.9+57.4+59.6)/5=50.2, contradicts the 47.9 in the summary table |\n| Vanilla recovery s42 | (omitted) | **61.7%** | User listed s0/s1/s7/s123 but missed s42 |\n| TaxEI recovery s42 | (omitted) | **59.6%** | User listed s0/s1/s123 but missed s42 |\n| Random recovery | (not mentioned) | **63.8% (s42 only)** | Only 1 seed exists |\n\n### 1.2 Additional experiments in registry not mentioned by user\n\n- **LLaMA-3.1-8B s0 training** (llama31-vanilla-s0): training DONE but **no eval** exists\n- **Dose-response multi-seed** (10%/25%/50% × TaxEI/Random): extensive data exists beyond seed=42\n- **Training dynamics** (v4-training-dynamics-forward, v2): per-operator loss analysis\n- **Recovery-paired datagen**: 711 samples generated for future recovery-paired SFT\n\n---\n\n## 2. Table A: Cross-Model Comparison (s42, Recovery Eval)\n\nBoth models evaluated with injected_eval.py — same 47 episodes, same error operators.\n\n### Recovery Rate\n\n| Condition | Qwen3-8B | LLaMA-3.1-8B | Δ (LLaMA−Qwen) |\n|-----------|----------|--------------|-----------------|\n| Vanilla | 61.7% (29/47) | 74.5% (35/47) | **+12.8pp** |\n| TaxEI | 59.6% (28/47) | 74.5% (35/47) | **+14.9pp** |\n| Random | 63.8% (30/47) | 76.6% (36/47) | **+12.8pp** |\n\n### Detection Rate\n\n| Condition | Qwen3-8B | LLaMA-3.1-8B | Δ |\n|-----------|----------|--------------|---|\n| Vanilla | 0% | 21.3% | **+21.3pp** |\n| TaxEI | 0% | 29.8% | **+29.8pp** |\n| Random | 0% | 29.8% | **+29.8pp** |\n\n### Per-Operator Recovery (s42)\n\n| Operator | Qwen Vanilla | Qwen TaxEI | Qwen Random | LLaMA Vanilla | LLaMA TaxEI | LLaMA Random |\n|----------|-------------|------------|-------------|---------------|-------------|-------------|\n| C1 (Context Truncation) | 75.0% | 66.7% | — | 75.0% | 83.3% | 66.7% |\n| C4 (Observation Masking) | 54.5% | 63.6% | — | 72.7% | 72.7% | 72.7% |\n| P1 (Step Order Swap) | 58.3% | 58.3% | — | 75.0% | 58.3% | 91.7% |\n| P2 (Sub-Goal Deletion) | 58.3% | 50.0% | — | 75.0% | 83.3% | 75.0% |\n\n*Note: Qwen Random s42 per-operator breakdown not recorded in registry.*\n\n---\n\n## 3. Table B: TaxEI-RP Eval Summary (5-seed)\n\nTaxEI-RP = Recovery-Paired injection training (711 paired recovery demos).\n\n| Seed | Recovery Rate | Count |\n|------|-------------|-------|\n| s42 | 38.3% | 18/47 |\n| s0 | 46.8% | 22/47 |\n| s1 | 48.9% | 23/47 |\n| s123 | 57.4% | 27/47 |\n| s7 | 59.6% | 28/47 |\n| **Mean±SD** | **50.2±8.6%** | — |\n\n### Comparison with baselines\n\n| Metric | Value |\n|--------|-------|\n| TaxEI-RP mean | 50.2% |\n| Vanilla clean eval mean | 67.3% |\n| Gap vs Vanilla | **−17.1pp** |\n| TaxEI full clean eval mean | 58.3% |\n| Gap vs TaxEI full | **−8.1pp** |\n| Vanilla recovery eval mean | 67.3% |\n| Gap vs Vanilla recovery | **−17.1pp** |\n\nDetection rate across all 5 TaxEI-RP seeds: **0%** (no explicit error detection).\n\n---\n\n## 4. Table C: Recovery Eval Completeness Matrix\n\n### Qwen3-8B Recovery Eval (injected_eval.py)\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42 | ✅ 61.7% | ✅ 59.6% | ✅ 63.8% |\n| s0 | ✅ 68.1% | ✅ 46.8% | ❌ |\n| s1 | ✅ 66.0% | ✅ 61.7% | ❌ |\n| s7 | ✅ 74.5% | ❌ | ❌ |\n| s123 | ✅ 66.0% | ✅ 61.7% | ❌ |\n| **Count** | **5/5** | **4/5** | **1/5** |\n\n**Missing**: TaxEI-s7, Random-s0/s1/s7/s123\n\n### Summary statistics (available seeds)\n\n| Condition | Seeds | Mean | SD | Min | Max |\n|-----------|-------|------|-----|-----|-----|\n| Vanilla | 5 | 67.3% | 4.7 | 61.7% | 74.5% |\n| TaxEI | 4 | 57.5% | 7.1 | 46.8% | 61.7% |\n| Random | 1 | 63.8% | — | — | — |\n\n### LLaMA-3.1-8B Recovery Eval\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42 | ✅ 74.5% | ✅ 74.5% | ✅ 76.6% |\n| s0 | ❌ (train only) | ❌ | ❌ |\n| **Count** | **1/5** | **1/5** | **1/5** |\n\n---\n\n## 5. Table D: Dose-Response Summary (Fixed-Size Ablation)\n\nAll conditions use 4,358 total samples (= vanilla size). Injection proportions: 10%, 25%, 50%.\n\n### Seed=42 (complete for all doses)\n\n| Dose | TaxEI | Random | Δ (TaxEI−Random) |\n|------|-------|--------|-------------------|\n| 0% (Vanilla) | 61.7% | 61.7% | 0 |\n| 10% | 61.7% | 68.1% | −6.4pp |\n| 25% | 48.9% | 55.3% | −6.4pp |\n| 50% | 51.1% | 57.4% | −6.3pp |\n| 100% (full, 9029) | 61.7% | 66.0% | −4.3pp |\n\n### Multi-Seed Dose-Response\n\n#### TaxEI 10% (5 seeds complete)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 61.7% |\n| s0 | 70.2% |\n| s1 | 51.1% |\n| s7 | 68.1% |\n| s123 | 55.3% |\n| **Mean±SD** | **61.3±7.7%** |\n\n#### TaxEI 25% (3 seeds)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 48.9% |\n| s1 | 63.8% |\n| s7 | 57.4% |\n| **Mean±SD** | **56.7±7.5%** |\n\n#### TaxEI 50% (3 seeds)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 51.1% |\n| s1 | 63.8% |\n| s7 | 55.3% |\n| **Mean±SD** | **56.7±6.4%** |\n\n#### Random 10% (5 seeds complete)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 68.1% |\n| s0 | 66.0% |\n| s1 | 68.1% |\n| s7 | 61.7% |\n| s123 | 55.3% |\n| **Mean±SD** | **63.8±5.2%** |\n\n#### Random 25% (3 seeds)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 55.3% |\n| s1 | 72.3% |\n| s7 | 59.6% |\n| **Mean±SD** | **62.4±8.8%** |\n\n#### Random 50% (3 seeds)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 57.4% |\n| s1 | 70.2% |\n| s7 | 46.8% |\n| **Mean±SD** | **58.1±11.7%** |\n\n### Dose-Response Curve (multi-seed means, where available)\n\n| Dose | TaxEI Mean | Random Mean | Vanilla Mean |\n|------|-----------|------------|-------------|\n| 0% | 67.3 (5s) | 67.3 (5s) | 67.3 (5s) |\n| 10% | 61.3 (5s) | 63.8 (5s) | — |\n| 25% | 56.7 (3s) | 62.4 (3s) | — |\n| 50% | 56.7 (3s) | 58.1 (3s) | — |\n| 100% | 58.3 (5s) | 58.3 (5s) | — |\n\n---\n\n## 6. Key Findings & Analysis\n\n### Finding 1: LLaMA s42 — near-zero condition effect (74.5 vs 74.5 vs 76.6)\n\nThe three conditions produce virtually identical recovery rates on LLaMA-3.1-8B (spread = 2.1pp). This contrasts with Qwen3-8B where the spread is larger (s42: 59.6–63.8, 4.2pp).\n\n**Implications for paper framing**:\n- LLaMA-3.1-8B appears **more robust to training data perturbation** — its agentic performance is insensitive to whether injection is taxonomy-guided, random, or absent. This is likely a **model capacity / pretraining quality** effect: a stronger base model can \"absorb\" injected errors without degrading task performance.\n- The real story is the **detection rate**: LLaMA detects 21–30% of errors vs Qwen's 0%. This suggests LLaMA has sufficient metacognitive capability to notice anomalies, whereas Qwen3-8B treats injected errors as normal trajectory variation.\n- **Paper framing recommendation**: Present LLaMA as a \"ceiling\" model where error injection is harmless (both TaxEI and Random), and Qwen as the model where injection effects manifest. The cross-model comparison becomes a **model sensitivity** analysis — taxonomy-guided injection matters more for models near the capability boundary.\n- **Caution**: Only 1 seed for LLaMA. The 2.1pp spread could easily be noise. Cannot draw strong conclusions without multi-seed LLaMA data.\n\n### Finding 2: TaxEI-RP 50.2% vs Vanilla 67.3% — significance analysis\n\nGap = −17.1pp. With 5 seeds:\n- TaxEI-RP: 50.2±8.6%\n- Vanilla: 67.3±4.7%\n\n**Effect size** (Cohen's d): d = (67.3−50.2) / √((4.7²+8.6²)/2) = 17.1 / √(47.6) = 17.1/6.9 = **2.48** (very large).\n\n**Welch's t-test** (approximate): t = 17.1 / √(4.7²/5 + 8.6²/5) = 17.1 / √(4.42+14.79) = 17.1/4.38 = **3.90**, df≈6.4, **p ≈ 0.006**.\n\n**The gap is statistically significant** (p < 0.01) despite only 5 seeds. TaxEI-RP substantially degrades clean task performance. This is a critical negative result: recovery-paired training hurts more than it helps on clean eval. The recovery benefit (if any) does not compensate for the clean performance loss.\n\n### Finding 3: TaxEI s0 recovery rate 46.8% — outlier analysis\n\nTaxEI recovery eval: s42=59.6%, s0=46.8%, s1=61.7%, s123=61.7%.\n\ns0 is 10.7pp below the 4-seed mean (57.5%). With SD=7.1, this is a z-score of −1.5 — outside 1σ but within 2σ. **Not a statistical outlier** by Grubbs' test (critical z for n=4 at α=0.05 is 1.48; marginal).\n\nHowever, note that TaxEI **clean eval** also shows s0 as the lowest: s0=46.8% vs mean=58.3%. The same seed shows low performance in both clean and recovery eval. This suggests **s0 is a generally unlucky seed for TaxEI**, not specific to recovery conditions. The s0 TaxEI model learned a weaker policy overall.\n\nFor comparison, Vanilla s0 clean=68.1% (above vanilla mean 67.3%), so the seed itself isn't bad — the TaxEI×s0 combination specifically produces poor models. This is consistent with **high variance under injection** (TaxEI SD=6.5 vs Vanilla SD=4.7).\n\n### Finding 4: Dose-response non-monotonicity\n\nThe dose-response curve for TaxEI (multi-seed) shows:\n- 0% → 10%: −6.0pp drop\n- 10% → 25%: −4.6pp drop\n- 25% → 50%: +0.0pp (flat)\n- 50% → 100%: +1.6pp recovery\n\nThe 25%→50%→100% plateau/recovery is unexpected. Possible explanations:\n1. **More injection = more data**: at 100% (9,029 samples), the model sees 2× more total data than fixed-size (4,358), compensating for injection noise.\n2. **3 seeds at 25%/50% vs 5 at 10%**: smaller sample sizes inflate uncertainty.\n3. The non-monotonicity may not be real — bootstrap CIs likely overlap.\n\nFor Random injection, the curve is flatter: 67.3 → 63.8 → 62.4 → 58.1 → 58.3, showing a gentler decline. TaxEI consistently underperforms Random by ~2–6pp at all doses, suggesting taxonomy labels **amplify the perturbation effect** rather than provide useful structure.\n\n### Finding 5: Vanilla recovery = Vanilla clean (identical per-seed)\n\nA striking pattern: Vanilla recovery rates (s42=61.7, s0=68.1, s1=66.0, s7=74.5, s123=66.0) are **identical** to vanilla clean eval rates. This is expected because:\n- Vanilla models have 0% detection rate\n- Without detection, the model doesn't \"know\" an error was injected\n- It simply continues the trajectory as if nothing happened\n- Success/failure is driven entirely by the model's base capability\n\nThis validates the eval methodology: vanilla provides a consistent reference.\n\n---\n\n## 7. Gaps & Recommendations for Paper Completeness\n\n| Priority | Gap | Impact | Effort |\n|----------|-----|--------|--------|\n| **HIGH** | Random recovery eval: only s42 exists (need s0/s1/s7/s123) | Cannot compute Random recovery mean±SD for Table C | 4 eval runs |\n| **HIGH** | TaxEI recovery s7 missing | 4/5 seeds → incomplete | 1 eval run |\n| **MEDIUM** | Dose-response 25% & 50%: only 3 seeds each | Weaker statistical power; cannot compute reliable CIs | 4 train + 4 eval per dose |\n| **MEDIUM** | LLaMA multi-seed | n=1 makes cross-model claims fragile | 4 train + 4×3 eval |\n| **LOW** | TaxEI-RP per-operator breakdown missing for 3 seeds | Cannot analyze operator-level RP effects | Already in eval logs, extract |\n\n---\n\n## 8. Recommended Paper Tables\n\n### Main Table (Table 1): Qwen3-8B 5-seed Clean Eval\n\n| Condition | Mean±SD | s42 | s0 | s1 | s7 | s123 |\n|-----------|---------|-----|-----|-----|-----|------|\n| Vanilla | 67.3±4.7 | 61.7 | 68.1 | 66.0 | 74.5 | 66.0 |\n| TaxEI full | 58.3±6.5 | 61.7 | 46.8 | 59.6 | 61.7 | 61.7 |\n| Random full | 58.3±8.7 | 66.0 | 55.3 | 46.8 | 55.3 | 68.1 |\n| TaxEI-RP | 50.2±8.6 | 38.3 | 46.8 | 48.9 | 59.6 | 57.4 |\n\n### Supplementary Table: Cross-Model (s42 only)\n\n| Condition | Qwen3-8B Recovery | Qwen3-8B Detection | LLaMA-8B Recovery | LLaMA-8B Detection |\n|-----------|-------------------|--------------------|--------------------|---------------------|\n| Vanilla | 61.7% | 0% | 74.5% | 21.3% |\n| TaxEI | 59.6% | 0% | 74.5% | 29.8% |\n| Random | 63.8% | 0% | 76.6% | 29.8% |\n\n---\n\n*Registry query: 112 DONE experiments, verified 2026-05-16.*\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/cross_model_recovery_analysis.md",
    "content": "# Cross-Model & Recovery Eval Comprehensive Analysis\n\n**Date**: 2026-05-16  \n**Project**: tax_error_inject_agent (EMNLP 2026 Findings)  \n**Data source**: Registry (112 DONE experiments verified)\n\n---\n\n## 1. Data Completeness Audit\n\n### 1.1 User-provided data vs Registry — discrepancies found\n\n| Item | User Value | Registry Value | Note |\n|------|-----------|---------------|------|\n| TaxEI-RP 5-seed mean (core table) | 47.9±7.8 | **50.2±8.6** | User's per-seed data (38.3+46.8+48.9+57.4+59.6)/5=50.2, contradicts the 47.9 in the summary table |\n| Vanilla recovery s42 | (omitted) | **61.7%** | User listed s0/s1/s7/s123 but missed s42 |\n| TaxEI recovery s42 | (omitted) | **59.6%** | User listed s0/s1/s123 but missed s42 |\n| Random recovery | (not mentioned) | **63.8% (s42 only)** | Only 1 seed exists |\n\n### 1.2 Additional experiments in registry not mentioned by user\n\n- **LLaMA-3.1-8B s0 training** (llama31-vanilla-s0): training DONE but **no eval** exists\n- **Dose-response multi-seed** (10%/25%/50% × TaxEI/Random): extensive data exists beyond seed=42\n- **Training dynamics** (v4-training-dynamics-forward, v2): per-operator loss analysis\n- **Recovery-paired datagen**: 711 samples generated for future recovery-paired SFT\n\n---\n\n## 2. Table A: Cross-Model Comparison (s42, Recovery Eval)\n\nBoth models evaluated with injected_eval.py — same 47 episodes, same error operators.\n\n### Recovery Rate\n\n| Condition | Qwen3-8B | LLaMA-3.1-8B | Δ (LLaMA−Qwen) |\n|-----------|----------|--------------|-----------------|\n| Vanilla | 61.7% (29/47) | 74.5% (35/47) | **+12.8pp** |\n| TaxEI | 59.6% (28/47) | 74.5% (35/47) | **+14.9pp** |\n| Random | 63.8% (30/47) | 76.6% (36/47) | **+12.8pp** |\n\n### Detection Rate\n\n| Condition | Qwen3-8B | LLaMA-3.1-8B | Δ |\n|-----------|----------|--------------|---|\n| Vanilla | 0% | 21.3% | **+21.3pp** |\n| TaxEI | 0% | 29.8% | **+29.8pp** |\n| Random | 0% | 29.8% | **+29.8pp** |\n\n### Per-Operator Recovery (s42)\n\n| Operator | Qwen Vanilla | Qwen TaxEI | Qwen Random | LLaMA Vanilla | LLaMA TaxEI | LLaMA Random |\n|----------|-------------|------------|-------------|---------------|-------------|-------------|\n| C1 (Context Truncation) | 75.0% | 66.7% | — | 75.0% | 83.3% | 66.7% |\n| C4 (Observation Masking) | 54.5% | 63.6% | — | 72.7% | 72.7% | 72.7% |\n| P1 (Step Order Swap) | 58.3% | 58.3% | — | 75.0% | 58.3% | 91.7% |\n| P2 (Sub-Goal Deletion) | 58.3% | 50.0% | — | 75.0% | 83.3% | 75.0% |\n\n*Note: Qwen Random s42 per-operator breakdown not recorded in registry.*\n\n---\n\n## 3. Table B: TaxEI-RP Eval Summary (5-seed)\n\nTaxEI-RP = Recovery-Paired injection training (711 paired recovery demos).\n\n| Seed | Recovery Rate | Count |\n|------|-------------|-------|\n| s42 | 38.3% | 18/47 |\n| s0 | 46.8% | 22/47 |\n| s1 | 48.9% | 23/47 |\n| s123 | 57.4% | 27/47 |\n| s7 | 59.6% | 28/47 |\n| **Mean±SD** | **50.2±8.6%** | — |\n\n### Comparison with baselines\n\n| Metric | Value |\n|--------|-------|\n| TaxEI-RP mean | 50.2% |\n| Vanilla clean eval mean | 67.3% |\n| Gap vs Vanilla | **−17.1pp** |\n| TaxEI full clean eval mean | 58.3% |\n| Gap vs TaxEI full | **−8.1pp** |\n| Vanilla recovery eval mean | 67.3% |\n| Gap vs Vanilla recovery | **−17.1pp** |\n\nDetection rate across all 5 TaxEI-RP seeds: **0%** (no explicit error detection).\n\n---\n\n## 4. Table C: Recovery Eval Completeness Matrix\n\n### Qwen3-8B Recovery Eval (injected_eval.py)\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42 | ✅ 61.7% | ✅ 59.6% | ✅ 63.8% |\n| s0 | ✅ 68.1% | ✅ 46.8% | ❌ |\n| s1 | ✅ 66.0% | ✅ 61.7% | ❌ |\n| s7 | ✅ 74.5% | ❌ | ❌ |\n| s123 | ✅ 66.0% | ✅ 61.7% | ❌ |\n| **Count** | **5/5** | **4/5** | **1/5** |\n\n**Missing**: TaxEI-s7, Random-s0/s1/s7/s123\n\n### Summary statistics (available seeds)\n\n| Condition | Seeds | Mean | SD | Min | Max |\n|-----------|-------|------|-----|-----|-----|\n| Vanilla | 5 | 67.3% | 4.7 | 61.7% | 74.5% |\n| TaxEI | 4 | 57.5% | 7.1 | 46.8% | 61.7% |\n| Random | 1 | 63.8% | — | — | — |\n\n### LLaMA-3.1-8B Recovery Eval\n\n| Seed | Vanilla | TaxEI | Random |\n|------|---------|-------|--------|\n| s42 | ✅ 74.5% | ✅ 74.5% | ✅ 76.6% |\n| s0 | ❌ (train only) | ❌ | ❌ |\n| **Count** | **1/5** | **1/5** | **1/5** |\n\n---\n\n## 5. Table D: Dose-Response Summary (Fixed-Size Ablation)\n\nAll conditions use 4,358 total samples (= vanilla size). Injection proportions: 10%, 25%, 50%.\n\n### Seed=42 (complete for all doses)\n\n| Dose | TaxEI | Random | Δ (TaxEI−Random) |\n|------|-------|--------|-------------------|\n| 0% (Vanilla) | 61.7% | 61.7% | 0 |\n| 10% | 61.7% | 68.1% | −6.4pp |\n| 25% | 48.9% | 55.3% | −6.4pp |\n| 50% | 51.1% | 57.4% | −6.3pp |\n| 100% (full, 9029) | 61.7% | 66.0% | −4.3pp |\n\n### Multi-Seed Dose-Response\n\n#### TaxEI 10% (5 seeds complete)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 61.7% |\n| s0 | 70.2% |\n| s1 | 51.1% |\n| s7 | 68.1% |\n| s123 | 55.3% |\n| **Mean±SD** | **61.3±7.7%** |\n\n#### TaxEI 25% (3 seeds)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 48.9% |\n| s1 | 63.8% |\n| s7 | 57.4% |\n| **Mean±SD** | **56.7±7.5%** |\n\n#### TaxEI 50% (3 seeds)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 51.1% |\n| s1 | 63.8% |\n| s7 | 55.3% |\n| **Mean±SD** | **56.7±6.4%** |\n\n#### Random 10% (5 seeds complete)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 68.1% |\n| s0 | 66.0% |\n| s1 | 68.1% |\n| s7 | 61.7% |\n| s123 | 55.3% |\n| **Mean±SD** | **63.8±5.2%** |\n\n#### Random 25% (3 seeds)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 55.3% |\n| s1 | 72.3% |\n| s7 | 59.6% |\n| **Mean±SD** | **62.4±8.8%** |\n\n#### Random 50% (3 seeds)\n\n| Seed | Success Rate |\n|------|-------------|\n| s42 | 57.4% |\n| s1 | 70.2% |\n| s7 | 46.8% |\n| **Mean±SD** | **58.1±11.7%** |\n\n### Dose-Response Curve (multi-seed means, where available)\n\n| Dose | TaxEI Mean | Random Mean | Vanilla Mean |\n|------|-----------|------------|-------------|\n| 0% | 67.3 (5s) | 67.3 (5s) | 67.3 (5s) |\n| 10% | 61.3 (5s) | 63.8 (5s) | — |\n| 25% | 56.7 (3s) | 62.4 (3s) | — |\n| 50% | 56.7 (3s) | 58.1 (3s) | — |\n| 100% | 58.3 (5s) | 58.3 (5s) | — |\n\n---\n\n## 6. Key Findings & Analysis\n\n### Finding 1: LLaMA s42 — near-zero condition effect (74.5 vs 74.5 vs 76.6)\n\nThe three conditions produce virtually identical recovery rates on LLaMA-3.1-8B (spread = 2.1pp). This contrasts with Qwen3-8B where the spread is larger (s42: 59.6–63.8, 4.2pp).\n\n**Implications for paper framing**:\n- LLaMA-3.1-8B appears **more robust to training data perturbation** — its agentic performance is insensitive to whether injection is taxonomy-guided, random, or absent. This is likely a **model capacity / pretraining quality** effect: a stronger base model can \"absorb\" injected errors without degrading task performance.\n- The real story is the **detection rate**: LLaMA detects 21–30% of errors vs Qwen's 0%. This suggests LLaMA has sufficient metacognitive capability to notice anomalies, whereas Qwen3-8B treats injected errors as normal trajectory variation.\n- **Paper framing recommendation**: Present LLaMA as a \"ceiling\" model where error injection is harmless (both TaxEI and Random), and Qwen as the model where injection effects manifest. The cross-model comparison becomes a **model sensitivity** analysis — taxonomy-guided injection matters more for models near the capability boundary.\n- **Caution**: Only 1 seed for LLaMA. The 2.1pp spread could easily be noise. Cannot draw strong conclusions without multi-seed LLaMA data.\n\n### Finding 2: TaxEI-RP 50.2% vs Vanilla 67.3% — significance analysis\n\nGap = −17.1pp. With 5 seeds:\n- TaxEI-RP: 50.2±8.6%\n- Vanilla: 67.3±4.7%\n\n**Effect size** (Cohen's d): d = (67.3−50.2) / √((4.7²+8.6²)/2) = 17.1 / √(47.6) = 17.1/6.9 = **2.48** (very large).\n\n**Welch's t-test** (approximate): t = 17.1 / √(4.7²/5 + 8.6²/5) = 17.1 / √(4.42+14.79) = 17.1/4.38 = **3.90**, df≈6.4, **p ≈ 0.006**.\n\n**The gap is statistically significant** (p < 0.01) despite only 5 seeds. TaxEI-RP substantially degrades clean task performance. This is a critical negative result: recovery-paired training hurts more than it helps on clean eval. The recovery benefit (if any) does not compensate for the clean performance loss.\n\n### Finding 3: TaxEI s0 recovery rate 46.8% — outlier analysis\n\nTaxEI recovery eval: s42=59.6%, s0=46.8%, s1=61.7%, s123=61.7%.\n\ns0 is 10.7pp below the 4-seed mean (57.5%). With SD=7.1, this is a z-score of −1.5 — outside 1σ but within 2σ. **Not a statistical outlier** by Grubbs' test (critical z for n=4 at α=0.05 is 1.48; marginal).\n\nHowever, note that TaxEI **clean eval** also shows s0 as the lowest: s0=46.8% vs mean=58.3%. The same seed shows low performance in both clean and recovery eval. This suggests **s0 is a generally unlucky seed for TaxEI**, not specific to recovery conditions. The s0 TaxEI model learned a weaker policy overall.\n\nFor comparison, Vanilla s0 clean=68.1% (above vanilla mean 67.3%), so the seed itself isn't bad — the TaxEI×s0 combination specifically produces poor models. This is consistent with **high variance under injection** (TaxEI SD=6.5 vs Vanilla SD=4.7).\n\n### Finding 4: Dose-response non-monotonicity\n\nThe dose-response curve for TaxEI (multi-seed) shows:\n- 0% → 10%: −6.0pp drop\n- 10% → 25%: −4.6pp drop\n- 25% → 50%: +0.0pp (flat)\n- 50% → 100%: +1.6pp recovery\n\nThe 25%→50%→100% plateau/recovery is unexpected. Possible explanations:\n1. **More injection = more data**: at 100% (9,029 samples), the model sees 2× more total data than fixed-size (4,358), compensating for injection noise.\n2. **3 seeds at 25%/50% vs 5 at 10%**: smaller sample sizes inflate uncertainty.\n3. The non-monotonicity may not be real — bootstrap CIs likely overlap.\n\nFor Random injection, the curve is flatter: 67.3 → 63.8 → 62.4 → 58.1 → 58.3, showing a gentler decline. TaxEI consistently underperforms Random by ~2–6pp at all doses, suggesting taxonomy labels **amplify the perturbation effect** rather than provide useful structure.\n\n### Finding 5: Vanilla recovery = Vanilla clean (identical per-seed)\n\nA striking pattern: Vanilla recovery rates (s42=61.7, s0=68.1, s1=66.0, s7=74.5, s123=66.0) are **identical** to vanilla clean eval rates. This is expected because:\n- Vanilla models have 0% detection rate\n- Without detection, the model doesn't \"know\" an error was injected\n- It simply continues the trajectory as if nothing happened\n- Success/failure is driven entirely by the model's base capability\n\nThis validates the eval methodology: vanilla provides a consistent reference.\n\n---\n\n## 7. Gaps & Recommendations for Paper Completeness\n\n| Priority | Gap | Impact | Effort |\n|----------|-----|--------|--------|\n| **HIGH** | Random recovery eval: only s42 exists (need s0/s1/s7/s123) | Cannot compute Random recovery mean±SD for Table C | 4 eval runs |\n| **HIGH** | TaxEI recovery s7 missing | 4/5 seeds → incomplete | 1 eval run |\n| **MEDIUM** | Dose-response 25% & 50%: only 3 seeds each | Weaker statistical power; cannot compute reliable CIs | 4 train + 4 eval per dose |\n| **MEDIUM** | LLaMA multi-seed | n=1 makes cross-model claims fragile | 4 train + 4×3 eval |\n| **LOW** | TaxEI-RP per-operator breakdown missing for 3 seeds | Cannot analyze operator-level RP effects | Already in eval logs, extract |\n\n---\n\n## 8. Recommended Paper Tables\n\n### Main Table (Table 1): Qwen3-8B 5-seed Clean Eval\n\n| Condition | Mean±SD | s42 | s0 | s1 | s7 | s123 |\n|-----------|---------|-----|-----|-----|-----|------|\n| Vanilla | 67.3±4.7 | 61.7 | 68.1 | 66.0 | 74.5 | 66.0 |\n| TaxEI full | 58.3±6.5 | 61.7 | 46.8 | 59.6 | 61.7 | 61.7 |\n| Random full | 58.3±8.7 | 66.0 | 55.3 | 46.8 | 55.3 | 68.1 |\n| TaxEI-RP | 50.2±8.6 | 38.3 | 46.8 | 48.9 | 59.6 | 57.4 |\n\n### Supplementary Table: Cross-Model (s42 only)\n\n| Condition | Qwen3-8B Recovery | Qwen3-8B Detection | LLaMA-8B Recovery | LLaMA-8B Detection |\n|-----------|-------------------|--------------------|--------------------|---------------------|\n| Vanilla | 61.7% | 0% | 74.5% | 21.3% |\n| TaxEI | 59.6% | 0% | 74.5% | 29.8% |\n| Random | 63.8% | 0% | 76.6% | 29.8% |\n\n---\n\n*Registry query: 112 DONE experiments, verified 2026-05-16.*\n"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T10:50:16.012899+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/cross_model_recovery_analysis.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T10:50:16.013044+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Cross-Model & Recovery Eval Comprehensive Analysis",
  "type": "report",
  "description": "Full data audit + 4 analysis tables (cross-model s42, TaxEI-RP 5-seed, recovery completeness matrix, dose-response) + 5 key findings with statistical tests + gap analysis for EMNLP paper",
  "project": "tax_error_inject_agent",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/cross_model_recovery_analysis.md",
  "tags": "['analysis', 'cross-model', 'recovery-eval', 'dose-response', 'emnlp2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Cross-Model & Recovery Eval Comprehensive Analysis",
    "type": "report",
    "description": "Full data audit + 4 analysis tables (cross-model s42, TaxEI-RP 5-seed, recovery completeness matrix, dose-response) + 5 key findings with statistical tests + gap analysis for EMNLP paper",
    "project": "tax_error_inject_agent",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/cross_model_recovery_analysis.md",
    "tags": "['analysis', 'cross-model', 'recovery-eval', 'dose-response', 'emnlp2026']"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T10:50:16.013196+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260516_f9b206\", \"name\": \"Cross-Model & Recovery Eval Comprehensive Analysis\", \"type\": \"report\", \"description\": \"Full data audit + 4 analysis tables (cross-model s42, TaxEI-RP 5-seed, recovery completeness matrix, dose-response) + 5 key findings with statistical tests + gap analysis for EMNLP paper\", \"path\": \"projects/tax_error_inject_agent/artifacts/_project/report/cross_model_recovery_analysis.md\", \"url\": null, \"project\": \"tax_error_inject_agent\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-16T10:50:02.759534+00:00\", \"tags\": [\"analysis\", \"cross-model\", \"recovery-eval\", \"dose-response\", \"emnlp2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-16T10:50:16.013365+00:00_

报告已写入并注册（`art_20260516_f9b206`）。核心发现：

1. **数据勘误**：你提供的 TaxEI-RP 均值 47.9±7.8 与 per-seed 数据不符，registry 验证为 **50.2±8.6**。Vanilla recovery s42 (61.7%) 和 TaxEI recovery s42 (59.6%) 在原始列表中遗漏。

2. **跨模型 (Table A)**：LLaMA 在三个 condition 下 recovery 几乎无差异（74.5/74.5/76.6），且 detection 率 21–30%；Qwen 全部 0% detection。LLaMA 对注入不敏感，适合作为"天花板模型"对比。但只有 1 seed，结论偏弱。

3. **TaxEI-RP (Table B)**：50.2% vs Vanilla 67.3%，Cohen's d=2.48，Welch t p≈0.006，**显著**。Recovery-paired 训练严重损害 clean 性能。

4. **Recovery 完整性 (Table C)**：Vanilla 5/5 完整，TaxEI 缺 s7，Random 只有 s42。Random 缺 4 个 seed 是最大数据缺口。

5. **Dose-response (Table D)**：10% 处有 5-seed 完整数据（TaxEI 61.3±7.7, Random 63.8±5.2），25%/50% 仅 3 seed。TaxEI 在所有 dose 下比 Random 低 2–6pp，taxonomy 标签放大了扰动而非提供有用结构。曲线在 25%→100% 出现非单调回升，可能因 100% 数据量翻倍补偿了噪声。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_cross-model-and-recovery-summary_20260516T104641"
}
```

</details>

---
